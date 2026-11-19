"""
Checkpoint Manager Module.
Provides durable, session-resilient state management for Kaggle Cloud execution.
Enables atomic batch saving and automatic resumption without reprocessing completed chunks.
"""

import json
import logging
from pathlib import Path
from typing import List, Set
from .base import VectorRecord

logger = logging.getLogger("CheckpointManager")


class CheckpointManager:
    """Manages intermediate vector checkpoints and resumption state."""

    def __init__(self, checkpoint_dir: Path):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)

    def _get_model_checkpoint_dir(self, model_name: str) -> Path:
        model_dir = self.checkpoint_dir / model_name
        model_dir.mkdir(parents=True, exist_ok=True)
        return model_dir

    def load_completed_chunk_ids(self, model_name: str) -> Set[str]:
        """
        Scan all checkpoint files for the given model to extract completed chunk IDs.
        Provides robust resumption even across disconnected Kaggle sessions.
        """
        completed_ids: Set[str] = set()
        model_dir = self._get_model_checkpoint_dir(model_name)
        
        jsonl_files = list(model_dir.glob("batch_*.jsonl"))
        for fpath in jsonl_files:
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            record = json.loads(line)
                            cid = record.get("chunk_id")
                            if cid:
                                completed_ids.add(cid)
            except Exception as e:
                logger.warning(f"Error reading checkpoint {fpath}: {e}")

        logger.info(f"Loaded {len(completed_ids)} completed chunk IDs for model '{model_name}'.")
        return completed_ids

    def filter_pending_chunks(self, chunks: List[dict], model_name: str) -> List[dict]:
        """Filter out chunks that have already been embedded in prior runs."""
        completed_ids = self.load_completed_chunk_ids(model_name)
        if not completed_ids:
            return chunks
        
        pending = [c for c in chunks if c.get("id") not in completed_ids]
        logger.info(
            f"Model '{model_name}': {len(chunks)} total -> {len(completed_ids)} already done -> {len(pending)} pending."
        )
        return pending

    def save_batch(
        self,
        model_name: str,
        batch_idx: int,
        records: List[VectorRecord]
    ) -> Path:
        """
        Atomically persist a batch of VectorRecords to disk.
        Uses JSONL for universal compatibility across minimal environments.
        """
        model_dir = self._get_model_checkpoint_dir(model_name)
        filename = f"batch_{batch_idx:05d}.jsonl"
        filepath = model_dir / filename
        temp_path = model_dir / f"{filename}.tmp"

        with open(temp_path, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec.to_dict(), ensure_ascii=False) + "\n")

        # Atomic rename to prevent partial writes
        temp_path.replace(filepath)
        return filepath

    def consolidate_checkpoints(self, model_name: str, output_path: Path) -> int:
        """
        Merge all batch checkpoint files into a single consolidated file
        for downstream vector indexing and final delivery.
        """
        model_dir = self._get_model_checkpoint_dir(model_name)
        batch_files = sorted(list(model_dir.glob("batch_*.jsonl")))
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        total_records = 0
        with open(output_path, "w", encoding="utf-8") as out_f:
            for bf in batch_files:
                with open(bf, "r", encoding="utf-8") as in_f:
                    for line in in_f:
                        if line.strip():
                            out_f.write(line)
                            total_records += 1

        logger.info(
            f"Consolidated {len(batch_files)} batches into {output_path} ({total_records} records)."
        )
        return total_records

    # Alias for convenience
    consolidate = consolidate_checkpoints

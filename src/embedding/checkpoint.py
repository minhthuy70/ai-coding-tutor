"""
Checkpoint Manager Module.
Provides durable, session-resilient state management for Kaggle Cloud execution.
Enables atomic batch saving, persistent manifest tracking, and cross-session resumption.
"""

import datetime
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Set
from .base import VectorRecord

logger = logging.getLogger("CheckpointManager")


class CheckpointManager:
    """
    Manages intermediate vector checkpoints and resumption state.
    Supports two distinct resumption scenarios:
    1. Intra-session Resume: Recovers from crashes/interrupts within the same live Kaggle session (/kaggle/working/).
    2. Cross-session Resume: Recovers across new Kaggle sessions by mounting prior outputs as input datasets (/kaggle/input/).
    """

    def __init__(
        self,
        checkpoint_dir: Path,
        input_checkpoint_dirs: Optional[List[Path]] = None
    ):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        
        # Directories from prior Kaggle dataset outputs mounted in /kaggle/input/ (Read-only)
        self.input_checkpoint_dirs = [
            Path(p) for p in (input_checkpoint_dirs or []) if Path(p).exists()
        ]

    def _get_working_model_dir(self, model_name: str) -> Path:
        model_dir = self.checkpoint_dir / model_name
        model_dir.mkdir(parents=True, exist_ok=True)
        return model_dir

    def load_completed_chunk_ids(self, model_name: str) -> Set[str]:
        """
        Scan all checkpoint sources (both prior mounted inputs and current working dir)
        to extract the deduplicated set of completed chunk IDs.
        """
        completed_ids: Set[str] = set()
        scanned_dirs = []

        # 1. Scan external read-only checkpoint directories (Cross-session resumption)
        for input_root in self.input_checkpoint_dirs:
            # Check direct or nested path
            candidate = input_root / model_name if (input_root / model_name).exists() else input_root
            if candidate.exists() and candidate.is_dir():
                scanned_dirs.append(candidate)

        # 2. Scan current session working checkpoint directory (Intra-session resumption)
        working_model_dir = self._get_working_model_dir(model_name)
        scanned_dirs.append(working_model_dir)

        # 3. Read records from all scanned directories
        for sdir in scanned_dirs:
            jsonl_files = list(sdir.glob("batch_*.jsonl"))
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

        logger.info(
            f"Model '{model_name}': Loaded {len(completed_ids):,} completed chunk IDs "
            f"across {len(scanned_dirs)} checkpoint location(s)."
        )
        return completed_ids

    def filter_pending_chunks(self, chunks: List[dict], model_name: str) -> List[dict]:
        """Filter out chunks that have already been embedded in prior runs/sessions."""
        completed_ids = self.load_completed_chunk_ids(model_name)
        if not completed_ids:
            return chunks
        
        pending = [c for c in chunks if c.get("id") not in completed_ids]
        logger.info(
            f"Model '{model_name}': {len(chunks):,} total -> {len(completed_ids):,} already completed -> {len(pending):,} pending."
        )
        return pending

    def save_batch(
        self,
        model_name: str,
        batch_idx: int,
        records: List[VectorRecord]
    ) -> Path:
        """
        Atomically persist a batch of VectorRecords and update the checkpoint manifest.
        Always writes to writable self.checkpoint_dir.
        """
        model_dir = self._get_working_model_dir(model_name)
        filename = f"batch_{batch_idx:05d}.jsonl"
        filepath = model_dir / filename
        temp_path = model_dir / f"{filename}.tmp"

        with open(temp_path, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec.to_dict(), ensure_ascii=False) + "\n")

        # Atomic rename prevents corrupted files on sudden termination
        temp_path.replace(filepath)

        # Update checkpoint manifest
        self._update_manifest(model_name, batch_idx, len(records), filepath.name)
        return filepath

    def _update_manifest(self, model_name: str, batch_idx: int, records_count: int, filename: str):
        """Update or create checkpoint_manifest.json to track execution state."""
        model_dir = self._get_working_model_dir(model_name)
        manifest_path = model_dir / "checkpoint_manifest.json"

        manifest_data: Dict[str, any] = {
            "model_name": model_name,
            "last_updated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "total_batches_saved": 0,
            "total_records_saved": 0,
            "batches": []
        }

        if manifest_path.exists():
            try:
                with open(manifest_path, "r", encoding="utf-8") as f:
                    manifest_data = json.load(f)
            except Exception:
                pass

        manifest_data["batches"].append({
            "batch_idx": batch_idx,
            "file": filename,
            "records_count": records_count,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        })
        manifest_data["total_batches_saved"] = len(manifest_data["batches"])
        manifest_data["total_records_saved"] = sum(b["records_count"] for b in manifest_data["batches"])
        manifest_data["last_updated"] = datetime.datetime.now(datetime.timezone.utc).isoformat()

        temp_manifest = model_dir / "checkpoint_manifest.json.tmp"
        with open(temp_manifest, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, ensure_ascii=False, indent=2)
        temp_manifest.replace(manifest_path)

    def consolidate_checkpoints(self, model_name: str, output_path: Path) -> int:
        """
        Merge all batch checkpoint files (from prior inputs and current working dir)
        into a single consolidated JSONL file without duplicate chunk IDs.
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        scanned_dirs = []
        for input_root in self.input_checkpoint_dirs:
            candidate = input_root / model_name if (input_root / model_name).exists() else input_root
            if candidate.exists() and candidate.is_dir():
                scanned_dirs.append(candidate)

        working_model_dir = self._get_working_model_dir(model_name)
        scanned_dirs.append(working_model_dir)

        seen_ids: Set[str] = set()
        total_records = 0

        with open(output_path, "w", encoding="utf-8") as out_f:
            for sdir in scanned_dirs:
                batch_files = sorted(list(sdir.glob("batch_*.jsonl")))
                for bf in batch_files:
                    with open(bf, "r", encoding="utf-8") as in_f:
                        for line in in_f:
                            if line.strip():
                                rec = json.loads(line)
                                cid = rec.get("chunk_id")
                                if cid and cid not in seen_ids:
                                    seen_ids.add(cid)
                                    out_f.write(line)
                                    total_records += 1

        logger.info(
            f"Consolidated checkpoints into {output_path} ({total_records:,} deduplicated records)."
        )
        return total_records

    # Alias for convenience
    consolidate = consolidate_checkpoints

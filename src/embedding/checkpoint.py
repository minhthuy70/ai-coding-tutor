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


class CheckpointCompatibilityError(ValueError):
    """Raised when an existing checkpoint is incompatible with the expected configuration."""
    pass


class CheckpointManager:
    """
    Manages intermediate vector checkpoints and resumption state.
    Supports two distinct resumption scenarios:
    1. Intra-session Resume: Recovers from crashes/interrupts within the same live Kaggle session (/kaggle/working/).
    2. Cross-session Resume: Recovers across new Kaggle sessions by mounting prior outputs as input datasets (/kaggle/input/).
    Validates model identity, dimension, and dataset fingerprint to prevent silent data corruption.
    """

    def __init__(
        self,
        checkpoint_dir: Path,
        input_checkpoint_dirs: Optional[List[Path]] = None,
        dataset_fingerprint: Optional[str] = None
    ):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        
        # Directories from prior Kaggle dataset outputs mounted in /kaggle/input/ (Read-only)
        self.input_checkpoint_dirs = [
            Path(p) for p in (input_checkpoint_dirs or []) if Path(p).exists()
        ]
        self.dataset_fingerprint = dataset_fingerprint

    def _get_working_model_dir(self, model_name: str) -> Path:
        model_dir = self.checkpoint_dir / model_name
        model_dir.mkdir(parents=True, exist_ok=True)
        return model_dir

    def load_completed_chunk_ids(
        self,
        model_name: str,
        expected_dimension: Optional[int] = None,
        expected_model_id: Optional[str] = None
    ) -> Set[str]:
        """
        Scan all checkpoint sources (both prior mounted inputs and current working dir)
        to extract the deduplicated set of completed chunk IDs.
        Validates checkpoint compatibility before including records.
        """
        completed_ids: Set[str] = set()
        scanned_dirs = []

        # 1. Scan external read-only checkpoint directories (Cross-session resumption)
        for input_root in self.input_checkpoint_dirs:
            candidate = input_root / model_name if (input_root / model_name).exists() else input_root
            if candidate.exists() and candidate.is_dir():
                scanned_dirs.append(candidate)

        # 2. Scan current session working checkpoint directory (Intra-session resumption)
        working_model_dir = self._get_working_model_dir(model_name)
        scanned_dirs.append(working_model_dir)

        # 3. Read records from all scanned directories after compatibility checks
        for sdir in scanned_dirs:
            manifest_file = sdir / "checkpoint_manifest.json"
            if manifest_file.exists():
                try:
                    with open(manifest_file, "r", encoding="utf-8") as mf:
                        mdata = json.load(mf)
                    # Verify model name
                    manifest_model = mdata.get("model_name")
                    if manifest_model and manifest_model != model_name:
                        logger.warning(
                            f"Skipping checkpoint in {sdir}: Model name mismatch (expected '{model_name}', got '{manifest_model}')"
                        )
                        continue
                    # Verify model id
                    if expected_model_id and mdata.get("model_id"):
                        if mdata["model_id"] != expected_model_id:
                            raise CheckpointCompatibilityError(
                                f"Checkpoint {sdir} incompatible: expected model_id '{expected_model_id}', got '{mdata['model_id']}'"
                            )
                    # Verify dimension
                    if expected_dimension and mdata.get("dimension"):
                        if mdata["dimension"] != expected_dimension:
                            raise CheckpointCompatibilityError(
                                f"Checkpoint {sdir} incompatible: expected dimension {expected_dimension}, got {mdata['dimension']}"
                            )
                    # Verify dataset fingerprint
                    if self.dataset_fingerprint and mdata.get("dataset_fingerprint"):
                        if mdata["dataset_fingerprint"] != self.dataset_fingerprint:
                            raise CheckpointCompatibilityError(
                                f"Checkpoint {sdir} dataset mismatch: expected '{self.dataset_fingerprint}', got '{mdata['dataset_fingerprint']}'"
                            )
                except CheckpointCompatibilityError:
                    raise
                except Exception as e:
                    logger.warning(f"Could not parse manifest at {manifest_file}: {e}")

            jsonl_files = list(sdir.glob("batch_*.jsonl"))
            for fpath in jsonl_files:
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        for line in f:
                            if line.strip():
                                record = json.loads(line)
                                # Vector dimension sanity check
                                if expected_dimension:
                                    vec_dim = record.get("embedding_dimension") or (len(record.get("vector", [])) if isinstance(record.get("vector"), list) else None)
                                    if vec_dim and vec_dim != expected_dimension:
                                        raise CheckpointCompatibilityError(
                                            f"Record in {fpath} has dimension {vec_dim} != expected {expected_dimension}"
                                        )
                                cid = record.get("chunk_id")
                                if cid:
                                    completed_ids.add(cid)
                except CheckpointCompatibilityError:
                    raise
                except Exception as e:
                    logger.warning(f"Error reading checkpoint {fpath}: {e}")

        logger.info(
            f"Model '{model_name}': Loaded {len(completed_ids):,} completed chunk IDs "
            f"across {len(scanned_dirs)} checkpoint location(s)."
        )
        return completed_ids

    def filter_pending_chunks(
        self,
        chunks: List[dict],
        model_name: str,
        expected_dimension: Optional[int] = None,
        expected_model_id: Optional[str] = None
    ) -> List[dict]:
        """Filter out chunks that have already been embedded in prior runs/sessions."""
        completed_ids = self.load_completed_chunk_ids(
            model_name,
            expected_dimension=expected_dimension,
            expected_model_id=expected_model_id
        )
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
        records: List[VectorRecord],
        dimension: Optional[int] = None,
        model_id: Optional[str] = None
    ) -> Path:
        """
        Atomically persist a batch of VectorRecords and update the checkpoint manifest.
        Guarantees that existing batches are NEVER overwritten.
        """
        model_dir = self._get_working_model_dir(model_name)
        
        # Guard against collision/overwrite: find next unused batch index
        target_idx = batch_idx
        filepath = model_dir / f"batch_{target_idx:05d}.jsonl"
        while filepath.exists():
            target_idx += 1
            filepath = model_dir / f"batch_{target_idx:05d}.jsonl"

        temp_path = model_dir / f"batch_{target_idx:05d}.jsonl.tmp"

        with open(temp_path, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec.to_dict(), ensure_ascii=False) + "\n")

        # Atomic rename prevents corrupted files on sudden termination
        temp_path.replace(filepath)

        # Update checkpoint manifest with full provenance
        record_dim = dimension or (records[0].embedding_dimension if records else None)
        record_mid = model_id or (records[0].model_name if records else None)
        self._update_manifest(
            model_name=model_name,
            batch_idx=target_idx,
            records_count=len(records),
            filename=filepath.name,
            dimension=record_dim,
            model_id=record_mid
        )
        return filepath

    def _update_manifest(
        self,
        model_name: str,
        batch_idx: int,
        records_count: int,
        filename: str,
        dimension: Optional[int] = None,
        model_id: Optional[str] = None
    ):
        """Update or create checkpoint_manifest.json to track execution state."""
        model_dir = self._get_working_model_dir(model_name)
        manifest_path = model_dir / "checkpoint_manifest.json"

        manifest_data: Dict[str, any] = {
            "model_name": model_name,
            "model_id": model_id,
            "dimension": dimension,
            "dataset_fingerprint": self.dataset_fingerprint,
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

        if dimension and "dimension" not in manifest_data:
            manifest_data["dimension"] = dimension
        if model_id and "model_id" not in manifest_data:
            manifest_data["model_id"] = model_id
        if self.dataset_fingerprint and "dataset_fingerprint" not in manifest_data:
            manifest_data["dataset_fingerprint"] = self.dataset_fingerprint

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

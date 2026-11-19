"""
ChromaDB Ingestion Pipeline Module.
Performs batch upsert of pre-computed embedding vectors and documents into ChromaDB collections.
Strictly offline: Zero model downloads, zero tokenizer calls, zero inference.
"""

import json
import logging
import math
import time
from pathlib import Path
from typing import Dict, Any, List, Set, Optional, Tuple

from .config import VectorStoreConfig, CollectionConfig
from .chroma_manager import ChromaManager

logger = logging.getLogger("vector_store.ingestion")


class IngestionError(Exception):
    """Exception raised for unrecoverable errors during ingestion."""
    pass


class ChromaIngestionPipeline:
    """
    Orchestrates batch ingestion of pre-computed vector datasets into ChromaDB collections.
    Provides resume capability, metadata sanitation, and strict vector validation.
    """

    def __init__(
        self,
        config: Optional[VectorStoreConfig] = None,
        chroma_manager: Optional[ChromaManager] = None,
    ):
        self.config = config or VectorStoreConfig()
        self.manager = chroma_manager or ChromaManager(self.config)
        self._chunks_map: Optional[Dict[str, Dict[str, Any]]] = None

    def load_chunks_map(self) -> Dict[str, Dict[str, Any]]:
        """Load all_chunks.json into memory for 1:1 ID -> full document text mapping."""
        if self._chunks_map is None:
            chunks_path = Path(self.config.all_chunks_path)
            if not chunks_path.exists():
                raise FileNotFoundError(f"Input chunks file not found: {chunks_path}")
            logger.info("Loading reference chunks from %s ...", chunks_path)
            with open(chunks_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._chunks_map = {c["id"]: c for c in data}
            logger.info("Loaded %d reference chunks successfully.", len(self._chunks_map))
        return self._chunks_map

    @staticmethod
    def sanitize_metadata(raw_meta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sanitize metadata dictionary to ensure full compatibility with ChromaDB.
        ChromaDB strictly accepts: str, int, float, bool.
        Complex values (list, dict) are JSON-stringified; None values are omitted.
        """
        clean = {}
        for k, v in raw_meta.items():
            if v is None:
                continue
            if isinstance(v, (str, int, float, bool)):
                clean[k] = v
            elif isinstance(v, (list, dict)):
                clean[k] = json.dumps(v, ensure_ascii=False)
            else:
                clean[k] = str(v)
        return clean

    @staticmethod
    def validate_record(
        rec: Dict[str, Any],
        expected_dim: int,
    ) -> Tuple[bool, List[str]]:
        """Validate an individual vector record before batch insertion."""
        errors = []
        cid = rec.get("chunk_id")
        if not cid:
            errors.append("Missing chunk_id")
        vec = rec.get("vector")
        if not vec or not isinstance(vec, list):
            errors.append("Vector is missing or not a list")
            return False, errors
        if len(vec) != expected_dim:
            errors.append(f"Dimension mismatch: {len(vec)} != {expected_dim}")
        if any(math.isnan(x) or math.isinf(x) for x in vec):
            errors.append("Vector contains NaN or Inf values")
        return len(errors) == 0, errors

    def get_existing_ids(self, collection_name: str) -> Set[str]:
        """Fetch set of already ingested IDs in the collection for idempotent resume."""
        try:
            coll = self.manager.get_collection(collection_name)
            # Retrieve only IDs
            existing = coll.get(include=[])
            return set(existing.get("ids", []))
        except Exception:
            return set()

    def ingest_collection(
        self,
        collection_config: CollectionConfig,
        vectors_path: Path,
        batch_size: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Ingest a vector file into its corresponding ChromaDB collection.
        Features batch upserts, resume capability, and complete execution metrics.
        """
        start_time = time.time()
        bsize = batch_size or self.config.batch_size
        vectors_file = Path(vectors_path)
        if not vectors_file.exists():
            raise FileNotFoundError(f"Vector artifact not found: {vectors_file}")

        chunks_map = self.load_chunks_map()
        collection = self.manager.get_or_create_collection(
            name=collection_config.name,
            metadata=collection_config.metadata,
        )

        existing_ids = self.get_existing_ids(collection_config.name)
        logger.info(
            "Collection '%s' already contains %d items.",
            collection_config.name,
            len(existing_ids),
        )

        # Read all records from vector artifact
        records = []
        with open(vectors_file, "r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f):
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError as e:
                    raise IngestionError(
                        f"Corrupt JSON line {line_idx} in {vectors_file}: {e}"
                    )

        total_records = len(records)
        # Filter out already ingested records for resume
        pending_records = [r for r in records if r["chunk_id"] not in existing_ids]
        skipped_count = total_records - len(pending_records)
        logger.info(
            "Collection '%s': Total=%d, Already Present=%d, Pending=%d",
            collection_config.name,
            total_records,
            skipped_count,
            len(pending_records),
        )

        ingested_count = 0
        failed_batches = []
        total_batches = math.ceil(len(pending_records) / bsize) if pending_records else 0

        for b_idx in range(total_batches):
            batch_slice = pending_records[b_idx * bsize : (b_idx + 1) * bsize]
            b_ids = []
            b_embeddings = []
            b_docs = []
            b_metadatas = []
            batch_has_error = False

            for rec in batch_slice:
                is_valid, val_errors = self.validate_record(rec, collection_config.dimension)
                if not is_valid:
                    logger.error("Validation failed for %s: %s", rec.get("chunk_id"), val_errors)
                    batch_has_error = True
                    break

                cid = rec["chunk_id"]
                chunk_ref = chunks_map.get(cid)
                if chunk_ref is None:
                    logger.error("Chunk ID '%s' not found in all_chunks.json!", cid)
                    batch_has_error = True
                    break

                doc_text = chunk_ref.get("text") or rec.get("content_preview", "")
                
                # Combine metadata from vector record and original chunk metadata
                combined_meta = dict(chunk_ref.get("metadata", {}))
                combined_meta.update(rec.get("metadata", {}))
                combined_meta["chunk_id"] = cid
                combined_meta["model_name"] = rec.get("model_name", "")
                combined_meta["embedding_dimension"] = collection_config.dimension

                b_ids.append(cid)
                b_embeddings.append(rec["vector"])
                b_docs.append(doc_text)
                b_metadatas.append(self.sanitize_metadata(combined_meta))

            if batch_has_error:
                failed_batches.append({
                    "batch_index": b_idx,
                    "reason": "Pre-validation or chunk mapping failure",
                    "chunk_ids": [r.get("chunk_id") for r in batch_slice],
                })
                continue

            try:
                collection.upsert(
                    ids=b_ids,
                    embeddings=b_embeddings,
                    documents=b_docs,
                    metadatas=b_metadatas,
                )
                ingested_count += len(b_ids)
                if (b_idx + 1) % 5 == 0 or (b_idx + 1) == total_batches:
                    logger.info(
                        "Collection '%s': Batch %d/%d completed (+%d items, cumulative: %d/%d)",
                        collection_config.name,
                        b_idx + 1,
                        total_batches,
                        len(b_ids),
                        ingested_count,
                        len(pending_records),
                    )
            except Exception as exc:
                logger.error("ChromaDB upsert failed at batch %d: %s", b_idx, exc)
                failed_batches.append({
                    "batch_index": b_idx,
                    "reason": str(exc),
                    "chunk_ids": b_ids,
                })

        duration = time.time() - start_time
        final_count = self.manager.count(collection_config.name)

        summary = {
            "collection_name": collection_config.name,
            "dimension": collection_config.dimension,
            "total_records_in_file": total_records,
            "skipped_already_present": skipped_count,
            "newly_ingested": ingested_count,
            "final_collection_count": final_count,
            "failed_batches_count": len(failed_batches),
            "failed_batches": failed_batches,
            "duration_seconds": round(duration, 2),
            "status": "SUCCESS" if len(failed_batches) == 0 else "PARTIAL_FAILURE",
        }
        logger.info("Collection '%s' ingestion summary: %s", collection_config.name, summary)
        return summary

"""
Embedding Pipeline Orchestrator.
Coordinates Modality Routing, Model-specific Embedding, Batch Validation,
Checkpoint Persistence, and QA Scorecard Generation.
"""

import json
import logging
import time
from pathlib import Path
from typing import Dict, List, Optional
from .base import BaseEmbedder, Modality, VectorRecord
from .checkpoint import CheckpointManager
from .config import EmbeddingPipelineConfig
from .router import ModalityRouter
from .validator import VectorValidator

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("EmbeddingPipeline")


class EmbeddingPipeline:
    """Main orchestrator for RAG Embedding pipeline on Kaggle Cloud GPU."""

    def __init__(self, config: Optional[EmbeddingPipelineConfig] = None):
        self.config = config or EmbeddingPipelineConfig()
        self.router = ModalityRouter(code_ratio_threshold=self.config.code_ratio_threshold)
        self.validator = VectorValidator({
            "qwen3_text": self.config.qwen3_text.dimension,
            "jina_code": self.config.jina_code.dimension,
            "jina_visual": self.config.jina_visual.dimension,
            "colqwen2_page": self.config.colqwen2_page.dimension
        })
        
        self.working_dir = self.config.resolve_working_dir()
        self.checkpoint_dir = self.working_dir / self.config.checkpoint_dir_name
        self.embeddings_dir = self.working_dir / self.config.embeddings_dir_name
        self.reports_dir = self.working_dir / self.config.reports_dir_name
        
        self.checkpoint_manager = CheckpointManager(
            self.checkpoint_dir,
            dataset_fingerprint=getattr(self.config, "dataset_fingerprint", None)
        )
        self._ensure_directories()

    def _ensure_directories(self):
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.embeddings_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def load_dataset(self, file_path: Optional[Path] = None) -> List[dict]:
        """Load the unified chunk dataset."""
        input_path = file_path or self.config.resolve_input_file()
        logger.info(f"Loading chunk dataset from: {input_path}")
        with open(input_path, "r", encoding="utf-8") as f:
            chunks = json.load(f)
        logger.info(f"Loaded {len(chunks):,} chunks successfully.")
        return chunks

    def route_dataset(self, chunks: List[dict]) -> Dict[Modality, List[dict]]:
        """Route chunks into exclusive Modality groups (TEXT vs CODE)."""
        partition = self.router.route_chunks(chunks)
        text_count = len(partition[Modality.TEXT])
        code_count = len(partition[Modality.CODE])
        logger.info(
            f"Modality Routing completed: TEXT = {text_count:,} ({text_count/len(chunks)*100:.1f}%), "
            f"CODE = {code_count:,} ({code_count/len(chunks)*100:.1f}%)."
        )
        return partition

    def process_modality(
        self,
        embedder: BaseEmbedder,
        chunks: List[dict],
        model_name: str,
        modality: Modality,
        batch_size: int = 32,
        limit: Optional[int] = None
    ) -> Dict[str, any]:
        """
        Embed a list of chunks using the assigned embedder with batching,
        validation, and resilient checkpointing.
        """
        start_time = time.time()
        target_chunks = chunks[:limit] if limit else chunks
        logger.info(
            f"=== Starting Embedding for '{model_name}' (Modality: {modality.value}) | "
            f"Target: {len(target_chunks):,} chunks ==="
        )

        # 1. Resume check: filter out already completed chunks with compatibility validation
        expected_dim = getattr(embedder.config, "dimension", None)
        expected_mid = getattr(embedder.config, "model_id", None)
        pending_chunks = self.checkpoint_manager.filter_pending_chunks(
            target_chunks,
            model_name,
            expected_dimension=expected_dim,
            expected_model_id=expected_mid
        )
        completed_ids = self.checkpoint_manager.load_completed_chunk_ids(
            model_name,
            expected_dimension=expected_dim,
            expected_model_id=expected_mid
        )
        
        all_valid_records = []
        all_failures = []
        batches_count = (len(pending_chunks) + batch_size - 1) // batch_size if pending_chunks else 0

        # 2. Main processing loop
        for b_idx in range(batches_count):
            batch_data = pending_chunks[b_idx * batch_size : (b_idx + 1) * batch_size]
            batch_texts = [c.get("text", "") for c in batch_data]

            # Generate vectors
            vectors = embedder.embed_documents(batch_texts, batch_size=batch_size)

            # Package into VectorRecords
            unvalidated_records = []
            for chunk, vec in zip(batch_data, vectors):
                record = VectorRecord(
                    chunk_id=chunk.get("id", ""),
                    source_file=chunk.get("metadata", {}).get("source_file", ""),
                    section_path=chunk.get("metadata", {}).get("section_path", ""),
                    modality=modality.value,
                    model_name=embedder.config.model_id,
                    model_version="1.0",
                    embedding_dimension=len(vec) if isinstance(vec, list) else 0,
                    vector=vec,
                    token_count=chunk.get("metadata", {}).get("token_count", 0),
                    content_preview=chunk.get("text", "")[:120].replace("\n", " "),
                    metadata=chunk.get("metadata", {})
                )
                unvalidated_records.append(record)

            # Validate batch
            valid_batch, batch_failures = self.validator.validate_batch(
                unvalidated_records, model_name, completed_ids
            )
            all_valid_records.extend(valid_batch)
            all_failures.extend(batch_failures)

            # Persist batch checkpoint atomically
            if valid_batch:
                self.checkpoint_manager.save_batch(
                    model_name=model_name,
                    batch_idx=b_idx,
                    records=valid_batch,
                    dimension=expected_dim,
                    model_id=expected_mid
                )

            if (b_idx + 1) % 5 == 0 or (b_idx + 1) == batches_count:
                logger.info(
                    f"[{model_name}] Progress: {b_idx + 1}/{batches_count} batches | "
                    f"New valid vectors: {len(all_valid_records):,} | Failures: {len(all_failures)}"
                )

        elapsed = time.time() - start_time

        # 3. Consolidate final checkpoint into clean output file
        final_output_file = self.embeddings_dir / model_name / f"{model_name}_vectors.jsonl"
        total_consolidated = self.checkpoint_manager.consolidate_checkpoints(model_name, final_output_file)

        summary = {
            "model_name": model_name,
            "model_id": embedder.config.model_id,
            "modality": modality.value,
            "total_target_chunks": len(target_chunks),
            "pending_chunks_processed": len(pending_chunks),
            "newly_embedded": len(all_valid_records),
            "total_consolidated_records": total_consolidated,
            "failures_count": len(all_failures),
            "elapsed_seconds": round(elapsed, 2),
            "output_file": str(final_output_file),
            "failures_sample": all_failures[:10]
        }

        # Save summary report
        report_file = self.reports_dir / f"{model_name}_embedding_summary.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        logger.info(
            f"=== Finished '{model_name}': {total_consolidated:,} total vectors in {elapsed:.2f}s ==="
        )
        return summary

"""
Unit Tests for RAG Embedding Framework using Mock Components.
Runs 100% on local machine using standard library and mock data.
Zero AI models loaded, zero inference, zero GPU/VRAM consumed.
"""

import json
import math
import shutil
import tempfile
import unittest
from pathlib import Path
from typing import List, Optional

from src.embedding.base import BaseEmbedder, Modality, VectorRecord
from src.embedding.checkpoint import CheckpointManager, CheckpointCompatibilityError
from src.embedding.config import EmbeddingPipelineConfig, ModelConfig
from src.embedding.pipeline import EmbeddingPipeline
from src.embedding.router import ModalityRouter
from src.embedding.sampler import PilotSampler
from src.embedding.validator import VectorValidator


class MockEmbedder(BaseEmbedder):
    """Lightweight mock embedder generating deterministic synthetic vectors."""

    def __init__(self, config: ModelConfig):
        super().__init__(config)

    def load_model(self) -> None:
        self._is_loaded = True

    def embed_documents(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        dim = self.config.dimension
        results = []
        for idx, t in enumerate(texts):
            raw = [(float((idx + j) % 10) + 1.0) / 10.0 for j in range(dim)]
            norm = math.sqrt(sum(x * x for x in raw))
            norm_vec = [x / norm for x in raw]
            results.append(norm_vec)
        return results

    def embed_query(self, query: str) -> List[float]:
        return self.embed_documents([query])[0]


class TestEmbeddingFrameworkMock(unittest.TestCase):
    """Test suite for embedding framework validation, routing, checkpointing, and sampling."""

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp(prefix="test_emb_"))
        self.router = ModalityRouter(code_ratio_threshold=0.50)  # Threshold 0.50 as required in Stage 3
        self.validator = VectorValidator({
            "qwen3_text": 1024,
            "jina_code": 768
        })

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    # 1. Test Modality Classification Rules
    def test_modality_routing_code_example(self):
        chunk = {
            "id": "c_code_01",
            "text": "Đây là code:\n```python\ndef add(a, b):\n    return a + b\n```",
            "metadata": {"content_type": "code_example", "has_code": True}
        }
        mod, ratio = self.router.classify_chunk(chunk)
        self.assertEqual(mod, Modality.CODE)

    def test_modality_routing_high_code_ratio(self):
        code_body = "def calculate_matrix():\n    matrix = []\n    return matrix"
        chunk = {
            "id": "c_code_02",
            "text": f"Ghi chú ngắn.\n```python\n{code_body}\n```",
            "metadata": {"content_type": "concept", "has_code": True}
        }
        mod, ratio = self.router.classify_chunk(chunk)
        self.assertGreaterEqual(ratio, 0.50)
        self.assertEqual(mod, Modality.CODE)

    def test_modality_routing_text_dominant(self):
        explanation = (
            "Khái niệm về vòng lặp for trong Python là một cơ chế lặp qua các phần tử của một chuỗi "
            "như danh sách, chuỗi ký tự hoặc tuple. Cú pháp cơ bản của vòng lặp for rất đơn giản và dễ hiểu. "
            "Ví dụ minh họa được đưa ra như sau:"
        )
        chunk = {
            "id": "c_text_01",
            "text": f"{explanation}\n```python\nfor i in range(5):\n    pass\n```",
            "metadata": {"content_type": "concept", "has_code": True}
        }
        mod, ratio = self.router.classify_chunk(chunk)
        self.assertLess(ratio, 0.50)
        self.assertEqual(mod, Modality.TEXT)

    def test_modality_routing_pure_text(self):
        chunk = {
            "id": "c_text_02",
            "text": "## Giới thiệu\nToán học rời rạc là nền tảng cốt lõi của Khoa học máy tính.",
            "metadata": {"content_type": "concept", "has_code": False}
        }
        mod, ratio = self.router.classify_chunk(chunk)
        self.assertEqual(mod, Modality.TEXT)
        self.assertEqual(ratio, 0.0)

    # 2. Test Full Real Dataset Routing Statistics
    def test_full_dataset_routing_counts(self):
        dataset_path = Path("data/06_rag_dataset/chunks/all_chunks.json")
        if not dataset_path.exists():
            self.skipTest("all_chunks.json not present at local path")

        with open(dataset_path, "r", encoding="utf-8") as f:
            all_chunks = json.load(f)

        partition = self.router.route_chunks(all_chunks)
        code_chunks = partition[Modality.CODE]
        text_chunks = partition[Modality.TEXT]

        # Verify routing completeness across all chunks (baseline 5,230 or extended corpus)
        self.assertGreaterEqual(len(all_chunks), 5230, "Total chunks must be at least 5,230")
        self.assertEqual(len(code_chunks) + len(text_chunks), len(all_chunks), "No chunks lost or duplicated")
        if len(all_chunks) == 5230:
            self.assertEqual(len(code_chunks), 937, "CODE chunks must be exactly 937 (17.92%)")
            self.assertEqual(len(text_chunks), 4293, "TEXT chunks must be exactly 4,293 (82.08%)")

    # 3. Test Vector Validator QA Checks
    def test_validator_missing_id(self):
        rec = VectorRecord(
            chunk_id="",
            source_file="test.md",
            section_path="Section 1",
            modality="text",
            model_name="qwen3_text",
            model_version="1.0",
            embedding_dimension=1024,
            vector=[1.0 / math.sqrt(1024)] * 1024,
            token_count=50,
            content_preview="preview",
            metadata={"source_file": "test.md", "section_title": "T", "section_path": "P", "section_depth": 1, "content_type": "c", "language": "py", "token_count": 50, "has_code": False, "has_table": False, "has_equation": False}
        )
        is_valid, errs = self.validator.validate_record(rec, "qwen3_text", set())
        self.assertFalse(is_valid)
        self.assertIn("Missing or invalid chunk_id", errs)

    def test_validator_dimension_mismatch(self):
        rec = VectorRecord(
            chunk_id="chunk_01",
            source_file="test.md",
            section_path="Section 1",
            modality="text",
            model_name="qwen3_text",
            model_version="1.0",
            embedding_dimension=512,
            vector=[1.0 / math.sqrt(512)] * 512,  # Expected 1024
            token_count=50,
            content_preview="preview",
            metadata={"source_file": "test.md", "section_title": "T", "section_path": "P", "section_depth": 1, "content_type": "c", "language": "py", "token_count": 50, "has_code": False, "has_table": False, "has_equation": False}
        )
        is_valid, errs = self.validator.validate_record(rec, "qwen3_text", set())
        self.assertFalse(is_valid)
        self.assertTrue(any("Dimension mismatch" in e for e in errs))

    def test_validator_nan_and_inf(self):
        vec_nan = [0.1] * 1023 + [float("nan")]
        rec_nan = VectorRecord(
            chunk_id="chunk_nan",
            source_file="test.md",
            section_path="Section 1",
            modality="text",
            model_name="qwen3_text",
            model_version="1.0",
            embedding_dimension=1024,
            vector=vec_nan,
            token_count=50,
            content_preview="preview",
            metadata={"source_file": "test.md", "section_title": "T", "section_path": "P", "section_depth": 1, "content_type": "c", "language": "py", "token_count": 50, "has_code": False, "has_table": False, "has_equation": False}
        )
        is_valid, errs = self.validator.validate_record(rec_nan, "qwen3_text", set())
        self.assertFalse(is_valid)
        self.assertIn("Vector contains NaN values", errs)

    def test_validator_l2_norm(self):
        # Non-normalized vector (sum of squares = 100 != 1.0)
        unnorm_vec = [10.0] + [0.0] * 1023
        rec = VectorRecord(
            chunk_id="chunk_unnorm",
            source_file="test.md",
            section_path="Section 1",
            modality="text",
            model_name="qwen3_text",
            model_version="1.0",
            embedding_dimension=1024,
            vector=unnorm_vec,
            token_count=50,
            content_preview="preview",
            metadata={"source_file": "test.md", "section_title": "T", "section_path": "P", "section_depth": 1, "content_type": "c", "language": "py", "token_count": 50, "has_code": False, "has_table": False, "has_equation": False}
        )
        is_valid, errs = self.validator.validate_record(rec, "qwen3_text", set())
        self.assertFalse(is_valid)
        self.assertTrue(any("L2 norm deviation" in e for e in errs))

    def test_validator_duplicate_id(self):
        val = 1.0 / math.sqrt(1024)
        rec1 = VectorRecord(
            chunk_id="dup_01",
            source_file="test.md",
            section_path="Section 1",
            modality="text",
            model_name="qwen3_text",
            model_version="1.0",
            embedding_dimension=1024,
            vector=[val] * 1024,
            token_count=50,
            content_preview="preview",
            metadata={"source_file": "test.md", "section_title": "T", "section_path": "P", "section_depth": 1, "content_type": "c", "language": "py", "token_count": 50, "has_code": False, "has_table": False, "has_equation": False}
        )
        seen = {"dup_01"}
        is_valid, errs = self.validator.validate_record(rec1, "qwen3_text", seen)
        self.assertFalse(is_valid)
        self.assertTrue(any("Duplicate chunk_id detected" in e for e in errs))

    # 4. Test Checkpoint & Resume Logic Simulation (Intra-session)
    def test_checkpoint_and_resume_simulation(self):
        ckpt_mgr = CheckpointManager(self.test_dir / "checkpoints")
        model_name = "test_model"

        # Create batch 0
        records_b0 = [
            VectorRecord(
                chunk_id=f"c_{i:03d}",
                source_file="test.md",
                section_path="Section",
                modality="text",
                model_name=model_name,
                model_version="1.0",
                embedding_dimension=1024,
                vector=[0.1] * 1024,
                token_count=20,
                content_preview=f"chunk {i}"
            )
            for i in range(10)
        ]
        ckpt_mgr.save_batch(model_name, 0, records_b0)

        # Check completed IDs
        completed = ckpt_mgr.load_completed_chunk_ids(model_name)
        self.assertEqual(len(completed), 10)
        self.assertIn("c_005", completed)

        # Filter pending chunks for a dataset of 25 chunks
        dataset = [{"id": f"c_{i:03d}", "text": f"text {i}"} for i in range(25)]
        pending = ckpt_mgr.filter_pending_chunks(dataset, model_name)
        self.assertEqual(len(pending), 15, "10 chunks should be skipped, 15 pending")
        self.assertEqual(pending[0]["id"], "c_010")

        # Consolidate
        merged_file = self.test_dir / "consolidated.jsonl"
        total = ckpt_mgr.consolidate(model_name, merged_file)
        self.assertEqual(total, 10)
        self.assertTrue(merged_file.exists())

    # 5. Test Cross-Session Resumption and Compatibility Validation
    def test_cross_session_resumption_and_compatibility(self):
        # 1. Create a simulated read-only external checkpoint folder with manifest
        prior_dir = self.test_dir / "prior_kaggle_input" / "checkpoints" / "qwen3_text"
        prior_dir.mkdir(parents=True, exist_ok=True)
        
        prior_records = [
            VectorRecord(
                chunk_id=f"prior_c_{i:03d}",
                source_file="prior.md",
                section_path="Section",
                modality="text",
                model_name="qwen3_text",
                model_version="1.0",
                embedding_dimension=1024,
                vector=[0.1] * 1024,
                token_count=20,
                content_preview=f"prior chunk {i}"
            )
            for i in range(20)
        ]
        batch_file = prior_dir / "batch_00000.jsonl"
        with open(batch_file, "w", encoding="utf-8") as f:
            for r in prior_records:
                f.write(json.dumps(r.to_dict(), ensure_ascii=False) + "\n")

        # Write manifest
        manifest_path = prior_dir / "checkpoint_manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump({
                "model_name": "qwen3_text",
                "model_id": "Qwen/Qwen3-Embedding-0.6B",
                "dimension": 1024,
                "dataset_fingerprint": "pilot_v3",
                "batches": [{"batch_idx": 0, "file": "batch_00000.jsonl", "records": 20}]
            }, mf)

        # 2. Resuming with compatible settings works
        new_working = self.test_dir / "working_compat" / "checkpoints"
        ckpt_mgr = CheckpointManager(
            checkpoint_dir=new_working,
            input_checkpoint_dirs=[self.test_dir / "prior_kaggle_input" / "checkpoints"],
            dataset_fingerprint="pilot_v3"
        )
        completed = ckpt_mgr.load_completed_chunk_ids("qwen3_text", expected_dimension=1024)
        self.assertEqual(len(completed), 20)

        # 3. Resuming with incompatible dimension raises CheckpointCompatibilityError
        incompat_working = self.test_dir / "working_incompat" / "checkpoints"
        incompat_ckpt_mgr = CheckpointManager(
            checkpoint_dir=incompat_working,
            input_checkpoint_dirs=[self.test_dir / "prior_kaggle_input" / "checkpoints"],
            dataset_fingerprint="pilot_v3"
        )
        with self.assertRaises(CheckpointCompatibilityError):
            incompat_ckpt_mgr.load_completed_chunk_ids("qwen3_text", expected_dimension=768)

    # 6. Test Pilot Deterministic Sampling
    def test_pilot_sampler_determinism(self):
        dataset_path = Path("data/06_rag_dataset/chunks/all_chunks.json")
        if not dataset_path.exists():
            self.skipTest("all_chunks.json not present at local path")

        with open(dataset_path, "r", encoding="utf-8") as f:
            all_chunks = json.load(f)

        sampler1 = PilotSampler(seed=42)
        pilot1 = sampler1.sample_pilot_dataset(all_chunks, text_limit=120, code_limit=40)

        sampler2 = PilotSampler(seed=42)
        pilot2 = sampler2.sample_pilot_dataset(all_chunks, text_limit=120, code_limit=40)

        self.assertEqual(len(pilot1["text_chunks"]), 120)
        self.assertEqual(len(pilot1["code_chunks"]), 40)
        self.assertEqual(pilot1["total_chunks"], 160)

        # Check determinism: same seed produces identical IDs in identical order
        ids1 = [c["id"] for c in pilot1["text_chunks"]] + [c["id"] for c in pilot1["code_chunks"]]
        ids2 = [c["id"] for c in pilot2["text_chunks"]] + [c["id"] for c in pilot2["code_chunks"]]
        self.assertEqual(ids1, ids2, "Sampler with seed 42 must be 100% deterministic")
        self.assertEqual(len(set(ids1)), 160, "All 160 sampled IDs must be unique")

    # 7. Test End-to-End Pipeline with Mock Embedder
    def test_pipeline_with_mock_embedder(self):
        config = EmbeddingPipelineConfig(
            local_working_dir=self.test_dir / "pipeline_run",
            local_data_path=self.test_dir / "mock_chunks.json"
        )
        pipeline = EmbeddingPipeline(config)

        # Create mock dataset with full required schema
        mock_chunks = [
            {
                "id": f"txt_{i:02d}",
                "text": f"Lý thuyết số {i}",
                "metadata": {
                    "source_file": "doc1.md",
                    "section_title": f"Chương {i}",
                    "section_path": f"Chương {i}",
                    "section_depth": 1,
                    "content_type": "concept",
                    "language": "python",
                    "token_count": 30,
                    "has_code": False,
                    "has_table": False,
                    "has_equation": False
                }
            }
            for i in range(15)
        ] + [
            {
                "id": f"cod_{i:02d}",
                "text": f"```python\ndef fn_{i}():\n    return {i}\n```",
                "metadata": {
                    "source_file": "doc2.md",
                    "section_title": f"Hàm {i}",
                    "section_path": f"Hàm {i}",
                    "section_depth": 1,
                    "content_type": "code_example",
                    "language": "python",
                    "token_count": 25,
                    "has_code": True,
                    "has_table": False,
                    "has_equation": False
                }
            }
            for i in range(5)
        ]

        # Route dataset
        partition = pipeline.route_dataset(mock_chunks)
        self.assertEqual(len(partition[Modality.TEXT]), 15)
        self.assertEqual(len(partition[Modality.CODE]), 5)

        # Run Text Embedder (Mock)
        mock_qwen_config = ModelConfig(
            model_name="qwen3_text",
            model_id="mock_qwen3",
            dimension=1024,
            context_length=8192,
            batch_size=8
        )
        mock_qwen_embedder = MockEmbedder(mock_qwen_config)
        
        summary = pipeline.process_modality(
            embedder=mock_qwen_embedder,
            chunks=partition[Modality.TEXT],
            model_name="qwen3_text",
            modality=Modality.TEXT,
            batch_size=8
        )

        self.assertEqual(summary["newly_embedded"], 15)
        self.assertEqual(summary["failures_count"], 0)
        self.assertEqual(summary["total_consolidated_records"], 15)
        self.assertTrue(Path(summary["output_file"]).exists())


if __name__ == "__main__":
    unittest.main()

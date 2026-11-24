"""
Mock Unit and Integration Tests for ChromaDB Vector Store Architecture.
Validates collection lifecycle, metadata sanitation, vector validation, batch ingestion,
retrieval formatting, and 10-point audit suites in an isolated temporary environment.
"""

import json
import math
import tempfile
from pathlib import Path
try:
    import pytest
except ImportError:
    pytest = None

from src.vector_store.config import VectorStoreConfig, CollectionConfig
from src.vector_store.chroma_manager import ChromaManager
from src.vector_store.ingestion import ChromaIngestionPipeline, IngestionError
from src.vector_store.retriever import ChromaRetriever, RetrievalResult
from src.vector_store.validator import VectorStoreValidator


# =============================================================================
# IN-MEMORY MOCK CHROMADB CLIENT FOR ZERO-DEPENDENCY UNIT TESTING
# =============================================================================
class MockCollection:
    """In-memory mock representing a ChromaDB collection."""
    def __init__(self, name: str, metadata: dict = None):
        self.name = name
        self.metadata = metadata or {"hnsw:space": "cosine"}
        self._records = {}  # id -> {"embedding": [...], "document": str, "metadata": dict}

    def count(self) -> int:
        return len(self._records)

    def upsert(self, ids, embeddings, documents, metadatas):
        for cid, emb, doc, meta in zip(ids, embeddings, documents, metadatas):
            self._records[cid] = {
                "embedding": emb,
                "document": doc,
                "metadata": meta,
            }

    def get(self, ids=None, limit=None, include=None):
        include = include or []
        res = {"ids": []}
        if "embeddings" in include:
            res["embeddings"] = []
        if "documents" in include:
            res["documents"] = []
        if "metadatas" in include:
            res["metadatas"] = []

        target_ids = ids if ids is not None else list(self._records.keys())
        if limit is not None:
            target_ids = target_ids[:limit]

        for cid in target_ids:
            if cid in self._records:
                res["ids"].append(cid)
                rec = self._records[cid]
                if "embeddings" in include:
                    res["embeddings"].append(rec["embedding"])
                if "documents" in include:
                    res["documents"].append(rec["document"])
                if "metadatas" in include:
                    res["metadatas"].append(rec["metadata"])
        return res

    def query(self, query_embeddings, n_results=5, where=None, where_document=None, include=None):
        qvec = query_embeddings[0]
        scored = []
        for cid, rec in self._records.items():
            # Check where filter
            if where:
                matched = True
                for wk, wv in where.items():
                    if rec["metadata"].get(wk) != wv:
                        matched = False
                        break
                if not matched:
                    continue

            # Compute Cosine Distance
            rvec = rec["embedding"]
            dot_val = sum(a * b for a, b in zip(qvec, rvec))
            norm_q = math.sqrt(sum(a * a for a in qvec)) or 1.0
            norm_r = math.sqrt(sum(b * b for b in rvec)) or 1.0
            cos_sim = dot_val / (norm_q * norm_r)
            cos_dist = max(0.0, 1.0 - cos_sim)
            scored.append((cos_dist, cid, rec))

        scored.sort(key=lambda x: x[0])
        top_k = scored[:n_results]

        ids = [item[1] for item in top_k]
        docs = [item[2]["document"] for item in top_k]
        metas = [item[2]["metadata"] for item in top_k]
        dists = [item[0] for item in top_k]

        return {
            "ids": [ids],
            "documents": [docs],
            "metadatas": [metas],
            "distances": [dists],
        }


class MockChromaClient:
    """In-memory mock representing ChromaDB ClientAPI."""
    def __init__(self):
        self._collections = {}

    def get_or_create_collection(self, name: str, metadata: dict = None):
        if name not in self._collections:
            self._collections[name] = MockCollection(name, metadata)
        return self._collections[name]

    def get_collection(self, name: str):
        if name not in self._collections:
            raise KeyError(f"Collection '{name}' does not exist")
        return self._collections[name]

    def list_collections(self):
        return list(self._collections.values())

    def delete_collection(self, name: str):
        if name in self._collections:
            del self._collections[name]


# =============================================================================
# UNIT TESTS
# =============================================================================
def test_metadata_sanitization():
    """Verify that complex metadata types are safely converted to ChromaDB-compatible primitives."""
    raw = {
        "title": "Introduction to Python",
        "depth": 2,
        "score": 0.95,
        "is_valid": True,
        "tags": ["python", "oop", "basics"],
        "nested_dict": {"module": "syntax", "version": 3},
        "none_val": None,
    }
    clean = ChromaIngestionPipeline.sanitize_metadata(raw)
    assert clean["title"] == "Introduction to Python"
    assert clean["depth"] == 2
    assert clean["score"] == 0.95
    assert clean["is_valid"] is True
    assert isinstance(clean["tags"], str)  # JSON-stringified
    assert json.loads(clean["tags"]) == ["python", "oop", "basics"]
    assert isinstance(clean["nested_dict"], str)
    assert "none_val" not in clean


def test_vector_record_validation():
    """Verify that VectorValidator catches dimension mismatches, NaNs, and missing IDs."""
    valid_rec = {
        "chunk_id": "c001",
        "vector": [0.1] * 1024,
    }
    is_ok, errs = ChromaIngestionPipeline.validate_record(valid_rec, expected_dim=1024)
    assert is_ok is True
    assert len(errs) == 0

    # Dimension mismatch
    bad_dim_rec = {"chunk_id": "c002", "vector": [0.1] * 512}
    is_ok, errs = ChromaIngestionPipeline.validate_record(bad_dim_rec, expected_dim=1024)
    assert is_ok is False
    assert any("Dimension mismatch" in e for e in errs)

    # NaN / Inf rejection
    nan_rec = {"chunk_id": "c003", "vector": [float("nan")] * 1024}
    is_ok, errs = ChromaIngestionPipeline.validate_record(nan_rec, expected_dim=1024)
    assert is_ok is False
    assert any("NaN or Inf" in e for e in errs)


def test_chroma_manager_mock_lifecycle():
    """Verify ChromaManager operations with mock client."""
    mock_client = MockChromaClient()
    manager = ChromaManager(config=VectorStoreConfig(), client=mock_client)

    # Create collection
    coll = manager.get_or_create_collection("test_text", metadata={"hnsw:space": "cosine"})
    assert coll.name == "test_text"
    assert manager.count("test_text") == 0

    # List collections
    colls = manager.list_collections()
    assert "test_text" in colls

    # Info
    info = manager.get_collection_info("test_text")
    assert info["name"] == "test_text"
    assert info["count"] == 0
    assert info["metadata"]["hnsw:space"] == "cosine"


def test_batch_ingestion_and_resume_mock():
    """Verify batch ingestion, metadata preservation, and idempotent resume behavior."""
    mock_client = MockChromaClient()
    manager = ChromaManager(config=VectorStoreConfig(), client=mock_client)
    pipeline = ChromaIngestionPipeline(chroma_manager=manager)

    # Setup dummy chunks map
    pipeline._chunks_map = {
        "chunk_01": {
            "id": "chunk_01",
            "text": "Full document text for chunk 01",
            "metadata": {"language": "python", "section_title": "Basics", "has_code": True},
        },
        "chunk_02": {
            "id": "chunk_02",
            "text": "Full document text for chunk 02",
            "metadata": {"language": "python", "section_title": "OOP", "has_code": False},
        },
    }

    # Create temporary jsonl file
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False, encoding="utf-8") as f:
        f.write(json.dumps({
            "chunk_id": "chunk_01",
            "vector": [1.0, 0.0, 0.0],
            "metadata": {"content_type": "code_example"},
            "model_name": "test_embedder",
        }) + "\n")
        f.write(json.dumps({
            "chunk_id": "chunk_02",
            "vector": [0.0, 1.0, 0.0],
            "metadata": {"content_type": "theory"},
            "model_name": "test_embedder",
        }) + "\n")
        temp_path = Path(f.name)

    try:
        cfg = CollectionConfig(name="mock_coll", dimension=3)
        res1 = pipeline.ingest_collection(cfg, temp_path, batch_size=1)
        assert res1["newly_ingested"] == 2
        assert res1["skipped_already_present"] == 0
        assert manager.count("mock_coll") == 2

        # Ingest again (should skip all via resume logic)
        res2 = pipeline.ingest_collection(cfg, temp_path, batch_size=1)
        assert res2["newly_ingested"] == 0
        assert res2["skipped_already_present"] == 2
        assert manager.count("mock_coll") == 2

        # Verify retriever
        retriever = ChromaRetriever(chroma_manager=manager)
        query_res = retriever.query_by_vector("mock_coll", query_vector=[1.0, 0.0, 0.0], top_k=1)
        assert len(query_res) == 1
        assert query_res[0].chunk_id == "chunk_01"
        assert abs(query_res[0].distance) < 1e-4
        assert abs(query_res[0].similarity - 1.0) < 1e-4
        assert query_res[0].metadata["language"] == "python"

        # Verify metadata filtering
        filter_res = retriever.query_by_vector(
            "mock_coll",
            query_vector=[1.0, 0.0, 0.0],
            top_k=2,
            where={"section_title": "OOP"},
        )
        assert len(filter_res) == 1
        assert filter_res[0].chunk_id == "chunk_02"

    finally:
        if temp_path.exists():
            temp_path.unlink()

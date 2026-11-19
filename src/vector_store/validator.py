"""
ChromaDB Vector Store Validator Module.
Conducts 10-point comprehensive audit and verification after ingestion.
Generates structured JSON validation reports for QA and governance.
"""

import json
import logging
import math
from pathlib import Path
from typing import Dict, Any, List, Set, Optional

try:
    import chromadb
except ImportError:
    chromadb = None

from .config import VectorStoreConfig, CollectionConfig
from .chroma_manager import ChromaManager
from .retriever import ChromaRetriever

logger = logging.getLogger("vector_store.validator")


class VectorStoreValidator:
    """
    Executes comprehensive 10-point validation on ChromaDB vector collections:
    1. Count per collection.
    2. Total system count matching 5,230.
    3. Zero duplicate IDs.
    4. Zero missing IDs compared to all_chunks.json.
    5. Correct embedding dimensions (1024 for Qwen3, 768 for Jina Code).
    6. Preservation of mandatory metadata fields.
    7. Numerical vector fidelity (retrieved vector matches input vector within float tolerance).
    8. Cosine distance accuracy (self-query distance ~ 0.0).
    9. Persistence integrity across client reopen.
    10. Top-K semantic retrieval functionality.
    """

    MANDATORY_METADATA_FIELDS = [
        "chunk_id",
        "source_file",
        "section_title",
        "section_path",
        "section_depth",
        "content_type",
        "language",
        "token_count",
        "length_chars",
        "has_code",
        "has_table",
        "has_equation",
    ]

    def __init__(
        self,
        chroma_manager: Optional[ChromaManager] = None,
        config: Optional[VectorStoreConfig] = None,
    ):
        self.config = config or VectorStoreConfig()
        self.manager = chroma_manager or ChromaManager(self.config)
        self.retriever = ChromaRetriever(self.manager, self.config)

    def validate_all(
        self,
        sample_size: int = 20,
        numerical_tolerance: float = 1e-4,
    ) -> Dict[str, Any]:
        """Run the complete 10-point audit suite and generate a detailed report."""
        logger.info("Starting ChromaDB 10-point validation suite...")
        report: Dict[str, Any] = {
            "timestamp": None,
            "overall_status": "UNKNOWN",
            "passed_checks": 0,
            "total_checks": 10,
            "checks": {},
            "collections": {},
            "metrics": {},
        }
        import datetime
        report["timestamp"] = datetime.datetime.now(datetime.timezone.utc).isoformat()

        # Load reference all_chunks.json
        with open(self.config.all_chunks_path, "r", encoding="utf-8") as f:
            all_chunks = json.load(f)
        expected_ids: Set[str] = {c["id"] for c in all_chunks}
        total_expected_count = len(expected_ids)

        # 1. Count per collection & 2. Total count
        qwen_count = self.manager.count(self.config.qwen3.name)
        jina_count = self.manager.count(self.config.jina.name)
        total_actual_count = qwen_count + jina_count

        coll_qwen = self.manager.get_collection(self.config.qwen3.name)
        coll_jina = self.manager.get_collection(self.config.jina.name)

        qwen_all = coll_qwen.get(include=["metadatas"])
        jina_all = coll_jina.get(include=["metadatas"])

        qwen_ids = set(qwen_all.get("ids", []))
        jina_ids = set(jina_all.get("ids", []))

        # Check 1: Record counts per collection
        check_1_passed = (qwen_count > 0 and jina_count > 0)
        report["checks"]["check_1_collection_counts"] = {
            "passed": check_1_passed,
            "qwen3_text_count": qwen_count,
            "jina_code_count": jina_count,
        }

        # Check 2: Total count equals expected (5,230)
        check_2_passed = (total_actual_count == total_expected_count)
        report["checks"]["check_2_total_system_count"] = {
            "passed": check_2_passed,
            "actual_total": total_actual_count,
            "expected_total": total_expected_count,
        }

        # Check 3: Zero duplicate IDs
        internal_duplicates = (
            len(qwen_all.get("ids", [])) != len(qwen_ids)
            or len(jina_all.get("ids", [])) != len(jina_ids)
        )
        cross_collection_overlap = qwen_ids & jina_ids
        check_3_passed = (not internal_duplicates) and (len(cross_collection_overlap) == 0)
        report["checks"]["check_3_zero_duplicate_ids"] = {
            "passed": check_3_passed,
            "cross_collection_overlap_count": len(cross_collection_overlap),
            "internal_duplicates": internal_duplicates,
        }

        # Check 4: Zero missing IDs against all_chunks.json
        combined_ids = qwen_ids | jina_ids
        missing_ids = expected_ids - combined_ids
        unexpected_ids = combined_ids - expected_ids
        check_4_passed = (len(missing_ids) == 0 and len(unexpected_ids) == 0)
        report["checks"]["check_4_zero_missing_ids"] = {
            "passed": check_4_passed,
            "missing_count": len(missing_ids),
            "unexpected_count": len(unexpected_ids),
        }

        # Check 5: Dimension validation
        qwen_sample = coll_qwen.get(limit=5, include=["embeddings"])
        jina_sample = coll_jina.get(limit=5, include=["embeddings"])
        
        qwen_dims = [len(v) for v in qwen_sample.get("embeddings", [])]
        jina_dims = [len(v) for v in jina_sample.get("embeddings", [])]
        
        qwen_dim_ok = all(d == self.config.qwen3.dimension for d in qwen_dims) if qwen_dims else False
        jina_dim_ok = all(d == self.config.jina.dimension for d in jina_dims) if jina_dims else False
        check_5_passed = qwen_dim_ok and jina_dim_ok
        report["checks"]["check_5_dimension_validation"] = {
            "passed": check_5_passed,
            "qwen3_expected": self.config.qwen3.dimension,
            "qwen3_actual": qwen_dims[0] if qwen_dims else None,
            "jina_expected": self.config.jina.dimension,
            "jina_actual": jina_dims[0] if jina_dims else None,
        }

        # Check 6: Metadata preservation
        missing_meta_keys = set()
        for sample_meta in (qwen_all.get("metadatas", [])[:50] + jina_all.get("metadatas", [])[:50]):
            for field in self.MANDATORY_METADATA_FIELDS:
                if field not in sample_meta:
                    missing_meta_keys.add(field)
        check_6_passed = (len(missing_meta_keys) == 0)
        report["checks"]["check_6_metadata_preservation"] = {
            "passed": check_6_passed,
            "missing_fields": list(missing_meta_keys),
            "verified_fields": self.MANDATORY_METADATA_FIELDS,
        }

        # Check 7: Numerical vector fidelity (comparing retrieved vector vs input artifact)
        fidelity_errors = []
        max_diff = 0.0
        
        # Test sample from Qwen
        sample_qwen_records = self._read_sample_records(self.config.qwen3_vectors_path, sample_size // 2)
        sample_ids_q = [r["chunk_id"] for r in sample_qwen_records]
        retrieved_q = coll_qwen.get(ids=sample_ids_q, include=["embeddings"])
        retrieved_q_map = dict(zip(retrieved_q["ids"], retrieved_q["embeddings"]))

        for rec in sample_qwen_records:
            cid = rec["chunk_id"]
            orig_vec = rec["vector"]
            chroma_vec = retrieved_q_map.get(cid)
            if chroma_vec is None:
                fidelity_errors.append(f"Missing vector in Chroma for {cid}")
                continue
            if hasattr(chroma_vec, "tolist"):
                chroma_vec = chroma_vec.tolist()
            diff = max(abs(a - b) for a, b in zip(orig_vec, chroma_vec))
            if diff > max_diff:
                max_diff = diff
            if diff > numerical_tolerance:
                fidelity_errors.append(f"{cid} diff {diff:.6e} > {numerical_tolerance}")

        check_7_passed = (len(fidelity_errors) == 0)
        report["checks"]["check_7_numerical_fidelity"] = {
            "passed": check_7_passed,
            "max_absolute_difference": max_diff,
            "tolerance": numerical_tolerance,
            "error_count": len(fidelity_errors),
        }

        # Check 8: Cosine distance correctness (Self-query should produce distance ~ 0.0, similarity ~ 1.0)
        if sample_ids_q:
            test_cid = sample_ids_q[0]
            self_query_res = self.retriever.query_by_chunk_id(
                collection_name=self.config.qwen3.name,
                chunk_id=test_cid,
                top_k=1,
            )
            top_match = self_query_res[0] if self_query_res else None
            is_self = (top_match is not None and top_match.chunk_id == test_cid)
            dist_near_zero = (top_match is not None and top_match.distance < 1e-4)
            check_8_passed = is_self and dist_near_zero
            report["checks"]["check_8_cosine_distance"] = {
                "passed": check_8_passed,
                "queried_chunk_id": test_cid,
                "top_match_id": top_match.chunk_id if top_match else None,
                "distance": top_match.distance if top_match else None,
                "similarity": top_match.similarity if top_match else None,
            }
        else:
            check_8_passed = False
            report["checks"]["check_8_cosine_distance"] = {"passed": False, "reason": "No sample ID"}

        # Check 9: PersistentClient reload test
        check_9_passed = False
        try:
            storage_path = Path(self.config.chroma_db_dir)
            if chromadb is not None:
                reopened_client = chromadb.PersistentClient(path=str(storage_path))
                c_q = reopened_client.get_collection(self.config.qwen3.name).count()
                c_j = reopened_client.get_collection(self.config.jina.name).count()
                check_9_passed = (c_q == qwen_count and c_j == jina_count)
            report["checks"]["check_9_persistence_reload"] = {
                "passed": check_9_passed,
                "reopened_qwen_count": c_q if check_9_passed else None,
                "reopened_jina_count": c_j if check_9_passed else None,
            }
        except Exception as exc:
            report["checks"]["check_9_persistence_reload"] = {
                "passed": False,
                "error": str(exc),
            }

        # Check 10: Top-K retrieval functionality
        check_10_passed = False
        try:
            if sample_ids_q:
                top_k_res = self.retriever.query_by_chunk_id(
                    collection_name=self.config.qwen3.name,
                    chunk_id=sample_ids_q[0],
                    top_k=3,
                )
                check_10_passed = (len(top_k_res) == 3 and all(r.distance >= 0.0 for r in top_k_res))
            report["checks"]["check_10_top_k_retrieval"] = {
                "passed": check_10_passed,
                "returned_results": len(top_k_res) if check_10_passed else 0,
            }
        except Exception as exc:
            report["checks"]["check_10_top_k_retrieval"] = {
                "passed": False,
                "error": str(exc),
            }

        passed_count = sum(1 for c in report["checks"].values() if c.get("passed") is True)
        report["passed_checks"] = passed_count
        report["overall_status"] = "PASSED" if passed_count == 10 else "FAILED"

        # Summary metrics
        report["metrics"] = {
            "total_records": total_actual_count,
            "qwen3_text_records": qwen_count,
            "jina_code_records": jina_count,
            "max_fidelity_delta": max_diff,
        }

        # Write report to disk
        out_report = Path(self.config.ingestion_report_path)
        out_report.parent.mkdir(parents=True, exist_ok=True)
        with open(out_report, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        logger.info("Validation report written to %s", out_report)

        return report

    def _read_sample_records(self, filepath: Path, n: int) -> List[Dict[str, Any]]:
        """Read first n records from a vector jsonl file."""
        records = []
        if not Path(filepath).exists():
            return records
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
                    if len(records) >= n:
                        break
        return records

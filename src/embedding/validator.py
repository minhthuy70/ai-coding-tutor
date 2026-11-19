"""
Vector Validator Module.
Conducts strict quality assurance on generated vector records, checking for:
- Non-empty vector
- Correct dimensionality
- Absence of NaN and Infinity values
- Preservation of original chunk identifiers
- Detection of duplicate chunk IDs
"""

import math
from typing import Dict, List, Set, Tuple
from .base import VectorRecord


class VectorValidator:
    """Validates vector embeddings before persistence or indexing."""

    def __init__(self, expected_dimensions: Dict[str, int] = None):
        # Default expected dimensions for models
        self.expected_dimensions = expected_dimensions or {
            "qwen3_text": 1024,
            "jina_code": 768,
            "jina_visual": 2048,
            "colqwen2_page": 128
        }

    def validate_record(
        self,
        record: VectorRecord,
        model_name: str,
        seen_ids: Set[str]
    ) -> Tuple[bool, List[str]]:
        """
        Validate an individual VectorRecord.
        Returns (is_valid, list_of_error_reasons).
        """
        errors = []

        # 1. Chunk ID check
        if not record.chunk_id or not isinstance(record.chunk_id, str):
            errors.append("Missing or invalid chunk_id")
        elif record.chunk_id in seen_ids:
            errors.append(f"Duplicate chunk_id detected: {record.chunk_id}")

        # 2. Vector presence & structure
        if record.vector is None or len(record.vector) == 0:
            errors.append("Embedding vector is empty")
            return False, errors

        # 3. Dimensionality check
        expected_dim = self.expected_dimensions.get(model_name)
        if expected_dim is not None:
            # Handle single vector vs multi-vector
            if isinstance(record.vector[0], list):
                # Multi-vector (e.g. ColQwen2 patch vectors)
                for patch_idx, patch_vec in enumerate(record.vector):
                    if len(patch_vec) != expected_dim:
                        errors.append(
                            f"Multi-vector patch {patch_idx} dimension mismatch: expected {expected_dim}, got {len(patch_vec)}"
                        )
                        break
            else:
                # Single dense vector
                if len(record.vector) != expected_dim:
                    errors.append(
                        f"Dimension mismatch: expected {expected_dim}, got {len(record.vector)}"
                    )

        # 4. Numerical validity: No NaN or Infinity
        flat_values = (
            [val for patch in record.vector for val in patch]
            if isinstance(record.vector[0], list)
            else record.vector
        )

        has_nan = any(math.isnan(v) for v in flat_values)
        if has_nan:
            errors.append("Vector contains NaN values")

        has_inf = any(math.isinf(v) for v in flat_values)
        if has_inf:
            errors.append("Vector contains Infinity values")

        # 5. Metadata integrity
        if not record.source_file:
            errors.append("Missing source_file in metadata")
        if not record.modality:
            errors.append("Missing modality designation")

        is_valid = len(errors) == 0
        return is_valid, errors

    def validate_batch(
        self,
        records: List[VectorRecord],
        model_name: str,
        seen_ids: Set[str]
    ) -> Tuple[List[VectorRecord], List[dict]]:
        """
        Validate a batch of VectorRecords.
        Returns (valid_records, failed_records_log).
        """
        valid_records = []
        failures = []

        for record in records:
            is_valid, errors = self.validate_record(record, model_name, seen_ids)
            if is_valid:
                seen_ids.add(record.chunk_id)
                valid_records.append(record)
            else:
                failures.append({
                    "chunk_id": record.chunk_id,
                    "model_name": model_name,
                    "errors": errors
                })

        return valid_records, failures

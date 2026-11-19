"""
Modality Router Module.
Classifies chunks into exclusive modalities (TEXT / CODE) based on empirical
content analysis without altering original chunk text or metadata.
"""

import re
from typing import Dict, List, Tuple
from .base import Modality


class ModalityRouter:
    """
    Deterministic Router implementing the Dominance-based Modality Rule:
    1. content_type == 'code_example' -> Modality.CODE (864 chunks)
    2. has_code == True AND code length ratio >= threshold (48.27% ~ 50%) -> Modality.CODE (79 chunks)
    3. All remaining cases -> Modality.TEXT (4,287 chunks)
    Total: 943 CODE + 4,287 TEXT = 5,230 chunks.
    """

    def __init__(self, code_ratio_threshold: float = 0.4827):
        self.code_ratio_threshold = code_ratio_threshold
        # Regex capturing markdown code block contents
        self._code_pattern = re.compile(
            r"```[a-zA-Z0-9_\-\.\+]*\s*([\s\S]*?)```", re.MULTILINE
        )

    def calculate_code_ratio(self, text: str) -> float:
        """Calculate the proportion of characters inside markdown code fences."""
        if not text:
            return 0.0
        code_matches = self._code_pattern.findall(text)
        if not code_matches:
            return 0.0
        code_chars = sum(len(block) for block in code_matches)
        return code_chars / len(text)

    def classify_chunk(self, chunk: dict) -> Tuple[Modality, float]:
        """
        Classify a single chunk into a Modality.
        Returns tuple of (Modality, code_ratio).
        """
        metadata = chunk.get("metadata", {})
        content_type = metadata.get("content_type", "")
        has_code = metadata.get("has_code", False)
        text = chunk.get("text", "")

        # Rule 1: Explicit code examples from pedagogical tagging (864 chunks)
        if content_type == "code_example":
            ratio = self.calculate_code_ratio(text)
            return Modality.CODE, ratio

        # Rule 2: Chunks with code fences exceeding the dominance threshold
        if has_code:
            ratio = self.calculate_code_ratio(text)
            if ratio >= self.code_ratio_threshold:
                return Modality.CODE, ratio
            return Modality.TEXT, ratio

        # Rule 3: Pure text, theory, math equations, or markdown tables
        return Modality.TEXT, 0.0

    def route_chunks(self, chunks: List[dict]) -> Dict[Modality, List[dict]]:
        """
        Partition list of chunks into disjoint modality groups without modifying chunk content.
        Preserves original chunk dictionary and index order.
        """
        partition: Dict[Modality, List[dict]] = {
            Modality.TEXT: [],
            Modality.CODE: []
        }

        for chunk in chunks:
            modality, ratio = self.classify_chunk(chunk)
            partition[modality].append(chunk)

        return partition

    def extract_code_subchunks_hook(self, chunk: dict) -> List[dict]:
        """
        Architectural hook for future extension:
        Extracts standalone code subchunks from mixed text/code chunks
        for dual-representation embedding.
        Currently returns empty list (stub for future phase).
        """
        text = chunk.get("text", "")
        code_matches = self._code_pattern.findall(text)
        if not code_matches:
            return []
        
        subchunks = []
        for idx, block in enumerate(code_matches):
            subchunks.append({
                "parent_id": chunk.get("id"),
                "subchunk_id": f"{chunk.get('id')}_code_{idx:02d}",
                "text": block.strip(),
                "modality": Modality.CODE
            })
        return subchunks

"""
ColQwen2 Page Embedder Interface (Phase 4 Extension Specification).
Defines abstract contracts for Multi-Vector Late Interaction (token-patch MaxSim)
without executing inference in Phase 2/3.
"""

import logging
from typing import Any, List, Optional
from .base import BaseEmbedder
from .config import ModelConfig

logger = logging.getLogger("ColQwen2PageEmbedder")


class ColQwen2PageEmbedder(BaseEmbedder):
    """
    Interface and Configuration Stub for vidore/colqwen2-v1.0-hf.
    Produces Multi-Vector representations for full PDF page visual retrieval.
    Active inference is scheduled for Phase 4 (Selective PDF execution).
    """

    def __init__(self, config: ModelConfig):
        super().__init__(config)
        self.patch_dimension = config.dimension  # 128 dimensions per patch

    def load_model(self) -> None:
        """Stub: Raises NotImplementedError until Phase 4 activation."""
        raise NotImplementedError(
            "ColQwen2PageEmbedder is an interface stub for Phase 4. "
            "Model weights should not be loaded during Phase 2/3."
        )

    def embed_documents(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        raise NotImplementedError("PDF Page embedding requires rendered image input (Phase 4).")

    def embed_page_images(self, page_image_paths: List[str]) -> List[List[List[float]]]:
        """Specification for multi-vector extraction from full PDF page images."""
        raise NotImplementedError("Multi-vector page encoding scheduled for Phase 4.")

    def embed_query(self, query: str) -> List[List[float]]:
        """Specification for query token multi-vector extraction."""
        raise NotImplementedError("ColQwen2 query encoding scheduled for Phase 4.")

    def compute_maxsim(self, query_multivec: List[List[float]], doc_multivec: List[List[float]]) -> float:
        """Specification for Late Interaction ColBERT MaxSim computation."""
        raise NotImplementedError("Late Interaction MaxSim scheduled for Phase 4/5.")

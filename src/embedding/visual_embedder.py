"""
Jina Visual Embedder Interface (Phase 4 Extension Specification).
Defines abstract contracts and configuration schema for jinaai/jina-embeddings-v4
without executing inference in Phase 2/3.
"""

import logging
from typing import Any, List, Optional
from .base import BaseEmbedder
from .config import ModelConfig

logger = logging.getLogger("JinaVisualEmbedder")


class JinaVisualEmbedder(BaseEmbedder):
    """
    Interface and Configuration Stub for Jina Embeddings v4 (Multimodal Vision + Text).
    Active inference is scheduled for Phase 4.
    """

    def __init__(self, config: ModelConfig):
        super().__init__(config)
        self.target_dimension = config.dimension  # 2048 default (Matryoshka to 768)

    def load_model(self) -> None:
        """Stub: Raises NotImplementedError until Phase 4 activation."""
        raise NotImplementedError(
            "JinaVisualEmbedder is an interface stub for Phase 4. "
            "Model weights should not be loaded during Phase 2/3."
        )

    def embed_documents(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        raise NotImplementedError("Visual embedding scheduled for Phase 4.")

    def embed_image(self, image_path: str, caption: Optional[str] = None) -> List[float]:
        """Specification for single multimodal image + context embedding."""
        raise NotImplementedError("Multimodal image embedding scheduled for Phase 4.")

    def embed_query(self, query: str) -> List[float]:
        raise NotImplementedError("Visual query embedding scheduled for Phase 4.")

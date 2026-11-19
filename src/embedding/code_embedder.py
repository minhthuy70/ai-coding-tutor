"""
Jina Code Embedder Wrapper.
Implements code-specialized dense embedding for Python, AST structures, and programming logic.
"""

import logging
from typing import List, Optional
from .base import BaseEmbedder
from .config import ModelConfig

logger = logging.getLogger("JinaCodeEmbedder")


class JinaCodeEmbedder(BaseEmbedder):
    """
    Wrapper for jinaai/jina-embeddings-v2-base-code.
    Dynamic import of sentence-transformers inside load_model() for local safety.
    """

    def __init__(self, config: ModelConfig):
        super().__init__(config)
        self.model = None

    def load_model(self) -> None:
        """Load Jina Code Embeddings v2 checkpoint on Kaggle GPU."""
        if self._is_loaded:
            return

        logger.info(f"Loading Jina Code checkpoint: {self.config.model_id}...")
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as e:
            raise RuntimeError(
                f"sentence-transformers not installed ({e}). "
                "Ensure execution occurs within Kaggle environment."
            )

        self.model = SentenceTransformer(
            self.config.model_id,
            trust_remote_code=self.config.extra_kwargs.get("trust_remote_code", True),
            device=self.config.device
        )
        self._is_loaded = True
        logger.info(f"Jina Code model successfully loaded. Dimension: {self.config.dimension}")

    def embed_documents(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        """Encode code snippets into 768-dim normalized vectors with OOM protection."""
        if not self._is_loaded:
            self.load_model()

        bs = batch_size or self.config.batch_size
        try:
            embeddings = self.model.encode(
                texts,
                batch_size=bs,
                show_progress_bar=False,
                normalize_embeddings=self.config.normalize_embeddings,
                convert_to_numpy=True
            )
            return embeddings.tolist()
        except Exception as e:
            # Check for CUDA OOM
            if "out of memory" in str(e).lower() or "CUDA out of memory" in str(e):
                logger.warning(f"CUDA OOM in JinaCodeEmbedder with batch_size {bs}. Retrying with batch_size=8...")
                try:
                    import torch
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()
                except ImportError:
                    pass
                embeddings = self.model.encode(
                    texts,
                    batch_size=max(1, bs // 4),
                    show_progress_bar=False,
                    normalize_embeddings=self.config.normalize_embeddings,
                    convert_to_numpy=True
                )
                return embeddings.tolist()
            raise e

    def embed_query(self, query: str) -> List[float]:
        """Encode query for code retrieval."""
        return self.embed_documents([query])[0]

    def unload_model(self) -> None:
        """Release VRAM."""
        if self._is_loaded:
            del self.model
            self.model = None
            self._is_loaded = False
            try:
                import torch
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except ImportError:
                pass
            logger.info("Unloaded Jina Code model and freed GPU cache.")

"""
RAG Embedding Framework for AI Coding Tutor.
Provides structured, model-specific embedding routers and pipelines
optimized for Kaggle Cloud GPU execution.
"""

from .base import BaseEmbedder, Modality, VectorRecord
from .checkpoint import CheckpointManager
from .code_embedder import JinaCodeEmbedder
from .config import EmbeddingPipelineConfig, ModelConfig
from .page_embedder import ColQwen2PageEmbedder
from .pipeline import EmbeddingPipeline
from .router import ModalityRouter
from .text_embedder import Qwen3TextEmbedder
from .validator import VectorValidator
from .visual_embedder import JinaVisualEmbedder

__all__ = [
    "BaseEmbedder",
    "Modality",
    "VectorRecord",
    "CheckpointManager",
    "ModelConfig",
    "EmbeddingPipelineConfig",
    "ModalityRouter",
    "VectorValidator",
    "Qwen3TextEmbedder",
    "JinaCodeEmbedder",
    "JinaVisualEmbedder",
    "ColQwen2PageEmbedder",
    "EmbeddingPipeline",
]

"""
Base Interfaces and Data Structures for RAG Embedding Framework.
Provides abstract contract for all model embedders and standardized vector record schema.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List, Optional, Union
import datetime


class Modality(str, Enum):
    """Supported modalities in the multimodal RAG architecture."""
    TEXT = "text"
    CODE = "code"
    VISUAL = "visual"
    PDF_PAGE = "pdf_page"


@dataclass
class VectorRecord:
    """Standardized record holding vector embedding and complete chunk metadata."""
    chunk_id: str
    source_file: str
    section_path: str
    modality: str
    model_name: str
    model_version: str
    embedding_dimension: int
    vector: Union[List[float], List[List[float]]]  # Single vector or multi-vector
    token_count: int
    content_preview: str
    metadata: dict = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())

    def to_dict(self) -> dict:
        """Serialize record to dictionary representation."""
        return {
            "chunk_id": self.chunk_id,
            "source_file": self.source_file,
            "section_path": self.section_path,
            "modality": self.modality,
            "model_name": self.model_name,
            "model_version": self.model_version,
            "embedding_dimension": self.embedding_dimension,
            "vector": self.vector,
            "token_count": self.token_count,
            "content_preview": self.content_preview,
            "metadata": self.metadata,
            "created_at": self.created_at
        }


class BaseEmbedder(ABC):
    """Abstract base class for all embedding model wrappers."""

    def __init__(self, config: Any):
        self.config = config
        self._is_loaded: bool = False

    @property
    def is_loaded(self) -> bool:
        """Check if underlying model checkpoint is loaded in memory."""
        return self._is_loaded

    @abstractmethod
    def load_model(self) -> None:
        """Load model weights into GPU/CPU memory."""
        pass

    @abstractmethod
    def embed_documents(self, texts: List[str], batch_size: Optional[int] = None) -> List[List[float]]:
        """Compute embeddings for a list of document texts."""
        pass

    @abstractmethod
    def embed_query(self, query: str) -> List[float]:
        """Compute embedding for a single search query."""
        pass

    def unload_model(self) -> None:
        """Optional hook to clean up memory and release VRAM."""
        self._is_loaded = False

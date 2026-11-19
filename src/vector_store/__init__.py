"""
Vector Store Package for AI Coding Tutor RAG Architecture.
Provides ChromaDB persistent management, batch ingestion, query retrieval, and validation suites.
"""

from .config import VectorStoreConfig, CollectionConfig
from .chroma_manager import ChromaManager
from .ingestion import ChromaIngestionPipeline, IngestionError
from .retriever import ChromaRetriever, RetrievalResult
from .validator import VectorStoreValidator

__all__ = [
    "VectorStoreConfig",
    "CollectionConfig",
    "ChromaManager",
    "ChromaIngestionPipeline",
    "IngestionError",
    "ChromaRetriever",
    "RetrievalResult",
    "VectorStoreValidator",
]

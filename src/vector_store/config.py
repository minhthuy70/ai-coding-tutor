"""
Configuration Module for ChromaDB Vector Store.
Defines persistent storage paths, collection settings, distance metrics, and batch sizes.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Any


@dataclass
class CollectionConfig:
    """Configuration for an individual ChromaDB collection."""
    name: str
    dimension: int
    distance_metric: str = "cosine"
    description: str = ""
    metadata: Dict[str, Any] = field(default_factory=lambda: {"hnsw:space": "cosine"})


@dataclass
class VectorStoreConfig:
    """Global configuration for ChromaDB storage, ingestion, and retrieval."""
    # Storage paths
    chroma_db_dir: Path = Path("data/07_vector_store/chroma_db")
    
    # Input vector artifact paths
    qwen3_vectors_path: Path = Path("data/08_rag_dataset/embeddings/qwen3_text/qwen3_text_vectors.jsonl")
    jina_vectors_path: Path = Path("data/08_rag_dataset/embeddings/jina_code/jina_code_vectors.jsonl")
    all_chunks_path: Path = Path("data/06_rag_dataset/chunks/all_chunks.json")
    
    # Output reports
    reports_dir: Path = Path("reports")
    ingestion_report_path: Path = Path("reports/chromadb_ingestion_report.json")
    
    # Ingestion settings
    batch_size: int = 250
    distance_metric: str = "cosine"
    
    # Collections
    qwen3: CollectionConfig = field(default_factory=lambda: CollectionConfig(
        name="qwen3_text",
        dimension=1024,
        distance_metric="cosine",
        description="Text and theoretical chunks embedded with Qwen3-Embedding-0.6B (1024-dim)",
        metadata={"hnsw:space": "cosine"}
    ))
    
    jina: CollectionConfig = field(default_factory=lambda: CollectionConfig(
        name="jina_code",
        dimension=768,
        distance_metric="cosine",
        description="Code-heavy chunks embedded with jina-embeddings-v2-base-code (768-dim)",
        metadata={"hnsw:space": "cosine"}
    ))

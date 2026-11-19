"""
ChromaDB Manager Module.
Encapsulates PersistentClient lifecycle, collection creation with HNSW cosine distance,
and administrative operations.
"""

import logging
import sys
import warnings
from pathlib import Path
from typing import Dict, Any, List, Optional
from unittest.mock import MagicMock

# Safe telemetry fallback: On Windows with Smart App Control, unused gRPC telemetry exporter
# DLL can be blocked. ChromaDB PersistentClient is purely local and does not use gRPC.
if "grpc" not in sys.modules:
    try:
        import grpc  # noqa: F401
    except (ImportError, OSError):
        dummy_grpc = MagicMock()
        dummy_grpc.__version__ = "1.85.3"
        sys.modules["grpc"] = dummy_grpc
        sys.modules["grpc._compression"] = dummy_grpc
        sys.modules["grpc._cython"] = dummy_grpc
        sys.modules["grpc._cython.cygrpc"] = dummy_grpc

# Filter harmless opentelemetry gRPC version runtime warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, module="opentelemetry")

try:
    import chromadb
    from chromadb.api import ClientAPI
    from chromadb.api.models.Collection import Collection
except ImportError:
    chromadb = None
    ClientAPI = Any
    Collection = Any

from .config import VectorStoreConfig, CollectionConfig

logger = logging.getLogger("vector_store.chroma_manager")


class ChromaManager:
    """
    Manages ChromaDB PersistentClient lifecycle and collection operations.
    Supports dependency injection of custom clients (e.g. EphemeralClient for testing).
    """

    def __init__(
        self,
        config: Optional[VectorStoreConfig] = None,
        client: Optional[ClientAPI] = None,
    ):
        self.config = config or VectorStoreConfig()
        if client is not None:
            self._client = client
        else:
            if chromadb is None:
                raise ImportError(
                    "chromadb is not installed. Please install with 'pip install chromadb'."
                )
            storage_path = Path(self.config.chroma_db_dir)
            storage_path.mkdir(parents=True, exist_ok=True)
            self._client = chromadb.PersistentClient(path=str(storage_path))
            logger.info("Initialized ChromaDB PersistentClient at %s", storage_path)

    @property
    def client(self) -> ClientAPI:
        """Return the underlying ChromaDB ClientAPI instance."""
        return self._client

    def get_or_create_collection(
        self,
        name: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Collection:
        """
        Get an existing collection or create a new one with specified metadata.
        Default distance metric is 'cosine' via HNSW space parameter.
        """
        coll_metadata = metadata or {"hnsw:space": self.config.distance_metric}
        collection = self._client.get_or_create_collection(
            name=name,
            metadata=coll_metadata,
        )
        logger.debug("Accessed collection '%s' (metadata=%s)", name, coll_metadata)
        return collection

    def get_collection(self, name: str) -> Collection:
        """Get an existing collection. Raises error if not found."""
        return self._client.get_collection(name=name)

    def list_collections(self) -> List[str]:
        """List all collection names in the vector store."""
        collections = self._client.list_collections()
        # Newer chromadb returns list of Collection objects or names
        names = []
        for c in collections:
            names.append(c.name if hasattr(c, "name") else str(c))
        return names

    def delete_collection(self, name: str) -> None:
        """Delete a collection by name."""
        self._client.delete_collection(name=name)
        logger.info("Deleted collection '%s'", name)

    def count(self, name: str) -> int:
        """Return the record count for a specific collection."""
        try:
            coll = self.get_collection(name)
            return coll.count()
        except Exception:
            return 0

    def get_collection_info(self, name: str) -> Dict[str, Any]:
        """Retrieve metadata, item count, and configuration for a collection."""
        coll = self.get_collection(name)
        return {
            "name": name,
            "count": coll.count(),
            "metadata": coll.metadata,
        }

    def close(self) -> None:
        """Release any client resources if applicable."""
        # ChromaDB PersistentClient manages SQLite connection internally
        pass

"""
ChromaDB Retriever Module.
Provides vector-based querying interface, metadata filtering, and result formatting.
Strictly offline: Only queries using pre-computed embeddings; never invokes models.
"""

import logging
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

from .config import VectorStoreConfig
from .chroma_manager import ChromaManager

logger = logging.getLogger("vector_store.retriever")


@dataclass
class RetrievalResult:
    """Represents a single retrieved document chunk from ChromaDB."""
    chunk_id: str
    document: str
    metadata: Dict[str, Any]
    distance: float
    similarity: float  # For cosine distance, similarity = 1.0 - distance
    collection_name: str


class ChromaRetriever:
    """
    Query interface for retrieving relevant chunks from ChromaDB collections.
    Accepts pre-computed query vectors or chunk IDs; does not perform local model inference.
    """

    def __init__(
        self,
        chroma_manager: Optional[ChromaManager] = None,
        config: Optional[VectorStoreConfig] = None,
    ):
        self.config = config or VectorStoreConfig()
        self.manager = chroma_manager or ChromaManager(self.config)

    def query_by_vector(
        self,
        collection_name: str,
        query_vector: List[float],
        top_k: int = 5,
        where: Optional[Dict[str, Any]] = None,
        where_document: Optional[Dict[str, Any]] = None,
    ) -> List[RetrievalResult]:
        """
        Query top-k nearest neighbors in a collection using a pre-computed embedding vector.
        """
        collection = self.manager.get_collection(collection_name)
        
        # Build query parameters
        query_kwargs: Dict[str, Any] = {
            "query_embeddings": [query_vector],
            "n_results": top_k,
            "include": ["documents", "metadatas", "distances"],
        }
        if where:
            query_kwargs["where"] = where
        if where_document:
            query_kwargs["where_document"] = where_document

        raw_results = collection.query(**query_kwargs)
        
        results: List[RetrievalResult] = []
        ids = raw_results.get("ids", [[]])[0]
        docs = raw_results.get("documents", [[]])[0]
        metas = raw_results.get("metadatas", [[]])[0]
        dists = raw_results.get("distances", [[]])[0]

        for cid, doc, meta, dist in zip(ids, docs, metas, dists):
            # For cosine space: cosine_distance = 1 - cosine_similarity
            cos_dist = float(dist)
            cos_sim = max(0.0, min(1.0, 1.0 - cos_dist))
            results.append(
                RetrievalResult(
                    chunk_id=cid,
                    document=doc or "",
                    metadata=meta or {},
                    distance=cos_dist,
                    similarity=cos_sim,
                    collection_name=collection_name,
                )
            )

        return results

    def query_by_chunk_id(
        self,
        collection_name: str,
        chunk_id: str,
        top_k: int = 5,
        where: Optional[Dict[str, Any]] = None,
    ) -> List[RetrievalResult]:
        """
        Query top-k nearest neighbors using an existing chunk's stored vector as the query.
        """
        collection = self.manager.get_collection(collection_name)
        chunk_data = collection.get(ids=[chunk_id], include=["embeddings"])
        embeddings = chunk_data.get("embeddings")
        if embeddings is None or len(embeddings) == 0:
            raise KeyError(f"Chunk ID '{chunk_id}' not found in collection '{collection_name}'")

        query_vector = embeddings[0]
        if hasattr(query_vector, "tolist"):
            query_vector = query_vector.tolist()

        return self.query_by_vector(
            collection_name=collection_name,
            query_vector=query_vector,
            top_k=top_k,
            where=where,
        )

    def get_by_id(
        self,
        collection_name: str,
        chunk_id: str,
    ) -> Optional[RetrievalResult]:
        """Fetch a specific document and its metadata by chunk ID."""
        collection = self.manager.get_collection(collection_name)
        data = collection.get(
            ids=[chunk_id],
            include=["documents", "metadatas"],
        )
        ids = data.get("ids", [])
        if not ids:
            return None
        return RetrievalResult(
            chunk_id=ids[0],
            document=data.get("documents", [""])[0],
            metadata=data.get("metadatas", [{}])[0],
            distance=0.0,
            similarity=1.0,
            collection_name=collection_name,
        )

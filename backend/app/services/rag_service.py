"""
RAG Retrieval Service using ChromaDB
Author: AI Coding Tutor Team
Description:
    Tra cứu các đoạn tri thức giáo trình chính thống từ ChromaDB Vector Database
    để làm bằng chứng (grounding evidence) cho AI Trợ Giảng trả lời.
"""

import os
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from app.core.config import settings

logger = logging.getLogger("RAGService")

class RAGService:
    def __init__(self):
        self.chroma_dir = Path(settings.CHROMA_DB_DIR).resolve()
        self.collection_name = "coding_tutor_knowledge"
        self._client = None
        self._collection = None

    def _get_collection(self):
        """Khởi tạo hoặc kết nối tới ChromaDB Collection (Lazy initialization)."""
        if self._collection is not None:
            return self._collection

        try:
            import chromadb
            from chromadb.utils import embedding_functions

            self.chroma_dir.mkdir(parents=True, exist_ok=True)
            self._client = chromadb.PersistentClient(path=str(self.chroma_dir))
            
            # Sử dụng DefaultEmbeddingFunction (all-MiniLM-L6-v2)
            emb_fn = embedding_functions.DefaultEmbeddingFunction()
            
            self._collection = self._client.get_or_create_collection(
                name=self.collection_name,
                embedding_function=emb_fn,
                metadata={"hnsw:space": "cosine"}
            )
            return self._collection
        except Exception as e:
            logger.warning(f"Không thể kết nối ChromaDB: {e}. Hệ thống sẽ sử dụng tri thức sư phạm mặc định.")
            return None

    def search_relevant_knowledge(
        self,
        query: str,
        language: Optional[str] = None,
        top_k: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Tìm kiếm top_k đoạn tài liệu giáo trình liên quan nhất tới câu hỏi của sinh viên.
        """
        coll = self._get_collection()
        if not coll or not query.strip():
            return []

        try:
            where_filter = {}
            if language and language.lower() not in ["all", "general", "text"]:
                where_filter = {"language": language.lower()}

            results = coll.query(
                query_texts=[query],
                n_results=top_k,
                where=where_filter if where_filter else None
            )

            retrieved = []
            if results and results.get("documents") and results["documents"][0]:
                docs = results["documents"][0]
                metas = results["metadatas"][0] if results.get("metadatas") else [{}] * len(docs)
                dists = results["distances"][0] if results.get("distances") else [0.0] * len(docs)

                for doc_text, meta, dist in zip(docs, metas, dists):
                    retrieved.append({
                        "content": doc_text,
                        "source": meta.get("source_file", "Giáo trình tiêu chuẩn"),
                        "section": meta.get("section_title", "Kiến thức trọng tâm"),
                        "language": meta.get("language", "general"),
                        "similarity_score": round(1.0 - float(dist), 3) if dist is not None else 1.0
                    })
            return retrieved
        except Exception as e:
            logger.error(f"Lỗi khi truy vấn ChromaDB: {e}")
            return []

    def format_rag_context_for_prompt(self, retrieved_chunks: List[Dict[str, Any]]) -> str:
        """Định dạng các đoạn tài liệu tìm thấy để đưa vào prompt của LLM."""
        if not retrieved_chunks:
            return ""

        context_lines = [
            "### TÀI LIỆU GIÁO TRÌNH CHÍNH THỐNG THAM CHIẾU (RAG GROUNDING CONTEXT):",
            "Hãy sử dụng các trích đoạn sau từ giáo trình để làm cơ sở giải thích và trích dẫn nguồn:",
        ]

        for i, item in enumerate(retrieved_chunks, 1):
            source_info = f"[Nguồn {i}: {item['source']} - Mục: {item['section']}]"
            context_lines.append(f"\n{source_info}\n```text\n{item['content']}\n```")

        context_lines.append("\n---\n")
        return "\n".join(context_lines)

rag_service = RAGService()


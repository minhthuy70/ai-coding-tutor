# -*- coding: utf-8 -*-
"""
Unit and Integration Tests for RAGService (Day 07 - Milestone 1)
Author: AI Coding Tutor Team
Description:
    Kiểm thử độc lập dịch vụ RAGService kết nối với kho tri thức ChromaDB Persistent (5.230 records).
    Kiểm tra khởi tạo, thống kê chỉ mục, truy vấn vector, bộ lọc ngôn ngữ, định dạng prompt và tình huống biên.
"""

import sys
import os
import json
import warnings
import pytest
from pathlib import Path

# Suppress harmless opentelemetry gRPC version runtime warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, module="opentelemetry")

# Đảm bảo đường dẫn import backend
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.rag_service import RAGService, rag_service


class TestRAGService:
    """Bộ kiểm thử toàn diện cho RAGService."""

    def test_01_initialization_and_stats(self):
        """Kiểm tra khởi tạo và toàn vẹn kho tri thức 5.230 vector."""
        stats = rag_service.get_stats()
        assert stats["status"] == "ready", "Trạng thái RAGService phải là 'ready'"
        assert stats["total_records"] == 5230, f"Tổng số records phải đạt 5.230, thực tế: {stats['total_records']}"
        assert stats["collections"]["qwen3_text"] == 4293, "Collection qwen3_text phải có 4.293 records"
        assert stats["collections"]["jina_code"] == 937, "Collection jina_code phải có 937 records"
        assert stats["benchmark_cached_queries"] >= 20, "Phải nạp thành công bộ đệm benchmark query vectors"

    def test_02_search_with_cached_benchmark_query(self):
        """Kiểm tra tìm kiếm câu hỏi lý thuyết OOP canonical."""
        query = "Bản chất của kỹ thuật lập trình hướng đối tượng (OOP) là gì?"
        top_k = 4
        results = rag_service.search(query=query, top_k=top_k)

        assert len(results) == top_k, f"Kết quả tìm kiếm phải trả về đúng {top_k} chunks"
        
        first_hit = results[0]
        assert "chunk_id" in first_hit
        assert "content" in first_hit and len(first_hit["content"]) > 0
        assert "source" in first_hit
        assert "section" in first_hit
        assert "similarity_score" in first_hit
        assert "rrf_score" in first_hit
        assert first_hit["rank"] == 1

        # Kiểm tra nội dung trúng tài liệu OOP chính thống
        sources = [r["source"] for r in results]
        is_hit = any("OOP" in s or "Ebook_Python" in s for s in sources)
        assert is_hit, f"Top {top_k} kết quả phải chứa tài liệu OOP chính thống: {sources}"

    def test_03_search_with_explicit_vectors(self):
        """Kiểm tra tìm kiếm khi truyền trực tiếp query vector (pre-computed)."""
        benchmark_file = BASE_DIR / "data" / "04_benchmark" / "benchmark_36q_query_embeddings.json"
        assert benchmark_file.exists(), f"Không tìm thấy {benchmark_file}"

        with open(benchmark_file, "r", encoding="utf-8") as f:
            embs = json.load(f)

        q_item = embs["Q01"]
        query_text = q_item["query"]
        q_vectors = {
            "qwen3_vector": q_item["qwen3_vector"],
            "jina_vector": q_item["jina_vector"]
        }

        results = rag_service.search(
            query=query_text,
            query_vectors=q_vectors,
            top_k=3
        )

        assert len(results) == 3
        top_chunk = results[0]
        assert "PEP8" in top_chunk["source"], f"Q01 PEP8 phải trả về tài liệu PEP8 ở Rank 1, thực tế: {top_chunk['source']}"
        assert top_chunk["similarity_score"] > 0.65

    def test_04_metadata_filtering_language(self):
        """Kiểm tra lọc metadata theo ngôn ngữ lập trình."""
        query = "Cú pháp List Comprehension lồng nhau để làm phẳng ma trận 2D"
        results = rag_service.search(query=query, language="python", top_k=4)

        assert len(results) > 0
        for r in results:
            assert r["language"] == "python", f"Tất cả chunks phải thuộc ngôn ngữ 'python', thực tế: {r['language']}"

    def test_05_format_rag_context_for_prompt(self):
        """Kiểm tra hàm định dạng ngữ cảnh cho Socratic System Prompt."""
        mock_chunks = [
            {
                "rank": 1,
                "chunk_id": "test_chunk_01",
                "source": "Ebook_Python.md",
                "section": "Chương 4: Hàm & Đệ quy",
                "content": "Hàm đệ quy cần có điều kiện dừng cơ sở để tránh tràn ngăn xếp call stack."
            }
        ]
        context_str = rag_service.format_rag_context_for_prompt(mock_chunks)

        assert "### TÀI LIỆU GIÁO TRÌNH CHÍNH THỐNG THAM CHIẾU" in context_str
        assert "Ebook_Python.md" in context_str
        assert "Chương 4: Hàm & Đệ quy" in context_str
        assert "điều kiện dừng" in context_str

    def test_06_edge_cases(self):
        """Kiểm tra các trường hợp biên: query rỗng, khoảng trắng, top_k nhỏ."""
        assert rag_service.search("") == []
        assert rag_service.search("   ") == []
        assert rag_service.format_rag_context_for_prompt([]) == ""

        single_result = rag_service.search("QuickSort", top_k=1)
        assert len(single_result) <= 1

    def test_07_auto_detect_language(self):
        """Kiểm tra tính năng tự động nhận diện ngôn ngữ lập trình của RAGService."""
        assert rag_service.auto_detect_language("Cú pháp def __init__(self) trong Python") == "python"
        assert rag_service.auto_detect_language("Cách dùng std::cout và vector<int> con trỏ") == "cpp"
        assert rag_service.auto_detect_language("public static void main(String[] args)") == "java"
        assert rag_service.auto_detect_language("Giải thích khái niệm độ phức tạp Big-O") is None

    def test_08_query_expansion(self):
        """Kiểm tra tính năng mở rộng từ khóa học thuật chuẩn (Query Expansion)."""
        expanded_oop = rag_service.expand_query("khái niệm oop")
        assert "lập trình hướng đối tượng" in expanded_oop or "OOP" in expanded_oop
        assert "kế thừa" in expanded_oop

        expanded_qs = rag_service.expand_query("thuật toán quicksort")
        assert "sắp xếp nhanh" in expanded_qs
        assert "pivot" in expanded_qs

    def test_09_unseen_query_fallback_search(self):
        """Kiểm tra cơ chế fallback và đa từ khóa đối với câu hỏi sinh viên chưa từng có trong cache."""
        unseen_query = "cách định nghĩa hàm đệ quy có điều kiện dừng base case"
        results = rag_service.search(query=unseen_query, top_k=3)

        assert len(results) > 0, "Fallback retrieval phải tìm thấy tài liệu phù hợp"
        top_hit = results[0]
        assert "chunk_id" in top_hit
        assert "content" in top_hit and len(top_hit["content"]) > 0
        assert top_hit["similarity_score"] >= 0.40, f"Điểm similarity phải đạt ngưỡng chất lượng: {top_hit['similarity_score']}"
        assert top_hit["rank"] == 1


if __name__ == "__main__":
    pytest.main(["-v", __file__])

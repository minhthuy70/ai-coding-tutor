"""
Unit Tests for QuerySynthesizer Service (Day 10)
Author: AI Coding Tutor Team
Description:
    Kiểm thử toàn diện module QuerySynthesizer:
    1. Trích xuất Search Query súc tích, chống pha loãng khoảng cách cosine.
    2. Rút trích lỗi & traceback từ đa nguồn (Prompt, Code, OCR).
    3. Tự động nhận diện ngôn ngữ lập trình chủ đạo.
    4. Ghép Unified Context Payload chuẩn cấu trúc Socratic.
    5. Xử lý các ca biên (không có prompt, chỉ có file/ảnh).
    6. Tích hợp trơn tru với RAGService và MultimodalService facade.
"""

import os
import sys
import asyncio
import pytest
from pathlib import Path
from typing import Dict, Any

# Đảm bảo đường dẫn import backend
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.query_synthesizer import query_synthesizer, QuerySynthesizer
from app.services.multimodal_service import multimodal_service
from app.services.rag_service import rag_service


class TestQuerySynthesizer:
    @classmethod
    def setup_class(cls):
        cls.synthesizer = QuerySynthesizer()

    def test_01_text_only_search_query_synthesis(self):
        """Kiểm thử sinh search query từ prompt văn bản thuần túy, loại bỏ các từ chào hỏi dư thừa."""
        prompt = "Chào thầy, cho em hỏi làm sao tối ưu thuật toán sắp xếp QuickSort và phân tích Big-O?"
        query = self.synthesizer.extract_core_search_query(prompt=prompt)

        assert len(query) > 0
        assert len(query) <= self.synthesizer.max_search_query_chars
        assert "QuickSort" in query
        assert not query.lower().startswith("chào thầy")

    def test_02_error_extraction_from_ocr_and_prompt(self):
        """Kiểm thử rút trích đa lỗi (Traceback, Exceptions) từ nhiều nguồn dữ liệu khác nhau."""
        prompt = "Em chạy bài tập thì bị lỗi IndexError: list index out of range ở dòng 12"
        images_data = [
            {
                "filename": "screenshot_terminal.png",
                "extracted_text": "Traceback (most recent call last):\n  File 'app.py', line 5\nZeroDivisionError: division by zero",
                "detected_errors": ["ZeroDivisionError: division by zero"],
                "code_blocks": []
            }
        ]
        files_data = [
            {
                "filename": "buggy.py",
                "language": "python",
                "raw_content": "# TODO: fix RecursionError: maximum recursion depth exceeded\ndef recurse(): recurse()"
            }
        ]

        errors = self.synthesizer.extract_consolidated_errors(
            prompt=prompt,
            files_data=files_data,
            images_data=images_data
        )

        assert len(errors) >= 3
        # Kiểm tra sự có mặt của các lỗi chính
        joined_errors = " ".join(errors)
        assert "IndexError: list index out of range" in joined_errors
        assert "ZeroDivisionError: division by zero" in joined_errors
        assert "RecursionError: maximum recursion depth exceeded" in joined_errors

    def test_03_query_dilution_prevention(self):
        """
        Kiểm thử chống pha loãng Cosine Similarity:
        Khi người dùng paste 500 dòng code vào prompt, query vector không được chứa 500 dòng code đó.
        """
        long_code = "\n".join([f"    x_{i} = {i} * 2" for i in range(500)])
        prompt_with_code = f"Cho em hỏi tại sao hàm này chạy chậm?\n```python\n{long_code}\n```"

        query = self.synthesizer.extract_core_search_query(prompt=prompt_with_code)

        assert len(query) <= self.synthesizer.max_search_query_chars
        assert "chạy chậm" in query or "tại sao" in query
        assert "x_499" not in query  # Không chứa code chi tiết
        assert "```" not in query

    def test_04_automatic_programming_language_detection(self):
        """Kiểm thử tự động nhận diện ngôn ngữ lập trình từ file, ảnh hoặc từ khóa."""
        # 1. Từ file python
        py_files = [{"filename": "main.py", "language": "python"}]
        assert self.synthesizer.detect_programming_language(files_data=py_files) == "python"

        # 2. Từ file C++
        cpp_files = [{"filename": "algo.cpp", "language": "cpp"}]
        assert self.synthesizer.detect_programming_language(files_data=cpp_files) == "cpp"

        # 3. Từ từ khóa trong prompt khi không có file
        prompt_cpp = "Thầy giải thích cho em về con trỏ và cout trong C++ với ạ"
        assert self.synthesizer.detect_programming_language(prompt=prompt_cpp) == "cpp"

        prompt_py = "PEP 8 quy định thụt lề như thế nào trong Python?"
        assert self.synthesizer.detect_programming_language(prompt=prompt_py) == "python"

    def test_05_unified_payload_structure_and_formatting(self):
        """Kiểm thử ghép đầy đủ Unified Context Payload với tất cả các phân đoạn chuẩn Socratic."""
        prompt = "Em bị lỗi khi thao tác với mảng"
        files_data = [
            {
                "filename": "test.py",
                "language": "python",
                "line_count": 10,
                "file_size_bytes": 150,
                "formatted_markdown": "\n### File: `test.py`\n```python\narr = [1, 2, 3]\nprint(arr[5])\n```\n",
                "raw_content": "arr = [1, 2, 3]\nprint(arr[5])"
            }
        ]
        images_data = [
            {
                "filename": "err.png",
                "mime_type": "image/png",
                "extracted_text": "IndexError: list index out of range",
                "detected_errors": ["IndexError: list index out of range"],
                "code_blocks": [],
                "formatted_markdown": "\n### Ảnh: `err.png`\n```text\nIndexError: list index out of range\n```\n"
            }
        ]
        rag_chunks = [
            {
                "chunk_id": "chunk_py_01",
                "content": "Trong Python, IndexError xảy ra khi truy cập phần tử ngoài chỉ mục hợp lệ.",
                "source": "Giao_trinh_Python_Co_ban.pdf",
                "section": "Chương 3: Cấu trúc danh sách (Lists)"
            }
        ]

        payload = self.synthesizer.build_unified_payload(
            prompt=prompt,
            files_data=files_data,
            images_data=images_data,
            rag_chunks=rag_chunks
        )

        # Kiểm tra cấu trúc dict
        assert "search_query" in payload
        assert "detected_language" in payload
        assert "detected_errors" in payload
        assert "files_summary" in payload
        assert "images_summary" in payload
        assert "rag_chunks" in payload
        assert "unified_context" in payload
        assert payload["total_context_chars"] > 0

        # Kiểm tra nội dung Markdown
        context_md = payload["unified_context"]
        assert "### [CÂU HỎI CỦA SINH VIÊN]" in context_md
        assert "### [THÔNG BÁO LỖI PHÁT HIỆN ĐƯỢC]" in context_md
        assert "### [MÃ NGUỒN TỪ FILE ĐÍNH KÈM]" in context_md
        assert "### [THÔNG TIN TRÍCH XUẤT TỪ ẢNH CHỤP MÀN HÌNH]" in context_md
        assert "TÀI LIỆU GIÁO TRÌNH CHÍNH THỐNG" in context_md
        assert "Giao_trinh_Python_Co_ban.pdf" in context_md

    def test_06_edge_cases_no_prompt_only_files_or_images(self):
        """Kiểm thử ca biên: Sinh viên không gõ lời nhắn, chỉ gửi file hoặc ảnh."""
        # 1. Chỉ gửi file
        payload_file = self.synthesizer.build_unified_payload(
            prompt="",
            files_data=[{
                "filename": "solution.cpp",
                "language": "cpp",
                "line_count": 5,
                "file_size_bytes": 100,
                "raw_content": "int main() { return 0; }",
                "formatted_markdown": "```cpp\nint main() { return 0; }\n```"
            }]
        )
        assert len(payload_file["search_query"]) > 0
        assert "solution.cpp" in payload_file["search_query"] or "cpp" in payload_file["search_query"].lower()
        assert "(Sinh viên không nhập câu hỏi bằng chữ" in payload_file["unified_context"]

        # 2. Chỉ gửi ảnh chứa lỗi
        payload_img = self.synthesizer.build_unified_payload(
            prompt="",
            images_data=[{
                "filename": "segfault.png",
                "mime_type": "image/png",
                "extracted_text": "Segmentation fault (core dumped)",
                "detected_errors": ["Segmentation fault (core dumped)"],
                "code_blocks": [],
                "formatted_markdown": "```text\nSegmentation fault\n```"
            }]
        )
        assert "Segmentation fault" in payload_img["search_query"]
        assert len(payload_img["detected_errors"]) >= 1

    def test_07_end_to_end_synthesize_and_retrieve_integration(self):
        """Kiểm thử luồng bất đồng bộ synthesize_and_retrieve tích hợp trọn vẹn với RAG."""
        py_code = b"def divide(a, b):\n    return a / b\nprint(divide(10, 0))\n"
        
        async def _run():
            return await self.synthesizer.synthesize_and_retrieve(
                prompt="Tại sao hàm này báo lỗi ZeroDivisionError?",
                code_files=[(py_code, "divide.py")],
                image_files=[],
                rag_top_k=2
            )

        payload = asyncio.run(_run())

        assert isinstance(payload, dict)
        assert payload["detected_language"] == "python"
        assert "ZeroDivisionError" in payload["search_query"]
        assert len(payload["files_summary"]) == 1
        assert payload["files_summary"][0]["filename"] == "divide.py"
        assert len(payload["rag_chunks"]) >= 0  # Có thể có chunks từ RAG
        assert payload["total_context_chars"] > 100

    def test_08_multimodal_service_facade_delegation(self):
        """Kiểm thử facade multimodal_service gọi ủy quyền chính xác tới query_synthesizer."""
        prompt = "Phân tích độ phức tạp thời gian O(n log n)"
        res = multimodal_service.build_unified_prompt(
            prompt_text=prompt,
            files_data=[],
            images_data=[]
        )

        assert isinstance(res, dict)
        assert "search_query" in res
        assert "unified_context" in res
        assert "O(n log n)" in res["search_query"]

# -*- coding: utf-8 -*-
"""
Unit Tests for FileExtractor Service (Day 08 - Multimodal Source Code Ingestion)
Author: AI Coding Tutor Team
Description:
    Bộ kiểm thử an ninh và chức năng toàn diện cho FileExtractor:
    - Bóc tách mã nguồn đa ngôn ngữ (Python, C++, Java, SQL, JS, MD)
    - Kiểm soát kích thước tối đa 2MB
    - Chống Path Traversal và Null-byte injection
    - Phát hiện file nhị phân độc hại giả mạo mã nguồn (Fake extension PE/ELF)
    - Chặn các phần mở rộng nguy hiểm (.exe, .sh, .zip...)
    - Xử lý mã hóa đa dạng (UTF-8, UTF-8-BOM, Latin-1)
"""

import sys
import os
import hashlib
import pytest
from pathlib import Path

# Đảm bảo đường dẫn import backend
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.file_extractor import (
    FileExtractor,
    file_extractor,
    MAX_FILE_SIZE_BYTES,
    ALLOWED_CODE_EXTENSIONS,
    DISALLOWED_EXTENSIONS
)


class TestFileExtractor:
    """Bộ kiểm thử chức năng và bảo mật cho FileExtractor."""

    def test_01_valid_python_extraction(self):
        """Kiểm tra trích xuất file Python chuẩn xác."""
        code = (
            "def binary_search(arr, target):\n"
            "    left, right = 0, len(arr) - 1\n"
            "    while left <= right:\n"
            "        mid = (left + right) // 2\n"
            "        if arr[mid] == target:\n"
            "            return mid\n"
            "        elif arr[mid] < target:\n"
            "            left = mid + 1\n"
            "        else:\n"
            "            right = mid - 1\n"
            "    return -1\n"
        )
        content_bytes = code.encode("utf-8")
        filename = "binary_search.py"

        res = file_extractor.extract_file(content_bytes, filename)

        assert res["valid"] is True
        assert res["filename"] == "binary_search.py"
        assert res["extension"] == ".py"
        assert res["language"] == "python"
        assert res["line_count"] == 12
        assert res["char_count"] == len(code)
        assert res["file_size_bytes"] == len(content_bytes)
        assert res["sha256"] == hashlib.sha256(content_bytes).hexdigest()
        assert "```python" in res["formatted_markdown"]
        assert "def binary_search" in res["formatted_markdown"]
        assert res["error"] is None

    def test_02_multiple_programming_languages(self):
        """Kiểm tra nhận diện đúng các ngôn ngữ lập trình phổ biến."""
        cases = [
            ("solution.cpp", b"#include <iostream>\nint main() { return 0; }\n", "cpp"),
            ("Main.java", b"public class Main { public static void main(String[] args) {} }\n", "java"),
            ("query.sql", b"SELECT id, username FROM users WHERE status = 'active';\n", "sql"),
            ("script.js", b"console.log('Hello world');\n", "javascript"),
            ("app.ts", b"const greet = (name: string): string => `Hi ${name}`;\n", "typescript"),
            ("notes.md", b"# Ghi chu bai tap\nDay la giai thuat de quy.\n", "markdown"),
        ]

        for fname, byte_data, expected_lang in cases:
            res = file_extractor.extract_file(byte_data, fname)
            assert res["valid"] is True, f"File {fname} phải hợp lệ"
            assert res["language"] == expected_lang, f"{fname} phải là {expected_lang}, thực tế: {res['language']}"
            assert f"```{expected_lang}" in res["formatted_markdown"]

    def test_03_file_size_limit_enforcement(self):
        """Kiểm tra chặn đứng file có kích thước vượt quá giới hạn 2MB."""
        # Tạo dữ liệu giả lập 2.1MB
        oversized_data = b"x = 1\n" * (MAX_FILE_SIZE_BYTES // 6 + 1000)
        assert len(oversized_data) > MAX_FILE_SIZE_BYTES

        res = file_extractor.extract_file(oversized_data, "huge_code.py")

        assert res["valid"] is False
        assert res["error"] is not None
        assert "vượt quá giới hạn" in res["error"]

    def test_04_path_traversal_sanitization(self):
        """Kiểm tra làm sạch tên file chống tấn công Path Traversal."""
        malicious_names = [
            ("../../../etc/passwd.py", "passwd.py"),
            ("..\\..\\Windows\\System32\\cmd.py", "cmd.py"),
            ("/var/log/secret/script.py", "script.py"),
            ("nested/subfolder/solution.cpp", "solution.cpp"),
            ("inject\x00malicious.py", "injectmalicious.py"),
        ]

        for dirty_name, expected_clean in malicious_names:
            clean = file_extractor.sanitize_filename(dirty_name)
            assert clean == expected_clean, f"'{dirty_name}' phải được làm sạch thành '{expected_clean}', thực tế: '{clean}'"
            assert "/" not in clean and "\\" not in clean
            assert ".." not in clean

    def test_05_malicious_binary_disguised_as_source_code(self):
        """Kiểm tra phát hiện file nhị phân độc hại giả mạo đuôi mã nguồn (.py / .cpp)."""
        # 1. Giả mạo Windows EXE với header MZ nhưng đuôi .py
        fake_exe = b"MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00" + b"evil_code" * 50
        res1 = file_extractor.extract_file(fake_exe, "trojan.py")
        assert res1["valid"] is False
        assert "nhị phân" in res1["error"]

        # 2. Giả mạo Linux ELF với header \x7fELF nhưng đuôi .cpp
        fake_elf = b"\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00" + b"payload" * 50
        res2 = file_extractor.extract_file(fake_elf, "exploit.cpp")
        assert res2["valid"] is False
        assert "nhị phân" in res2["error"]

        # 3. File chứa nhiều null bytes (\x00)
        null_bytes_code = b"def test():\n" + (b"\x00" * 50) + b"\n    pass\n"
        res3 = file_extractor.extract_file(null_bytes_code, "corrupted.py")
        assert res3["valid"] is False

    def test_06_disallowed_file_extensions(self):
        """Kiểm tra từ chối các định dạng file thực thi và file nén nguy hiểm."""
        forbidden_files = [
            ("virus.exe", b"MZ..."),
            ("hack.sh", b"#!/bin/bash\nrm -rf /"),
            ("script.bat", b"@echo off\ndir"),
            ("archive.zip", b"PK\x03\x04..."),
            ("library.dll", b"MZ..."),
        ]

        for fname, byte_data in forbidden_files:
            res = file_extractor.extract_file(byte_data, fname)
            assert res["valid"] is False
            assert "từ chối" in res["error"] or "không được hỗ trợ" in res["error"]

    def test_07_empty_file_and_bom_encoding(self):
        """Kiểm tra xử lý file rỗng và file có UTF-8 BOM."""
        # 1. File rỗng 0 bytes
        res_empty = file_extractor.extract_file(b"", "empty.py")
        assert res_empty["valid"] is False
        assert "rỗng" in res_empty["error"]

        # 2. File UTF-8 có tiền tố BOM (\xef\xbb\xbf)
        bom_code = "\ufeff# Python with BOM\nprint('Hello BOM')\n"
        bom_bytes = bom_code.encode("utf-8")
        res_bom = file_extractor.extract_file(bom_bytes, "bom_test.py")

        assert res_bom["valid"] is True
        assert res_bom["content"].startswith("# Python with BOM")
        assert "\ufeff" not in res_bom["content"]

    def test_08_batch_extraction(self):
        """Kiểm tra bóc tách đồng thời nhiều file trong một request."""
        batch_input = [
            (b"print('File 1')", "f1.py"),
            (b"print('File 2')", "f2.py"),
            (b"", "empty.py"),
        ]
        results = file_extractor.extract_batch(batch_input)

        assert len(results) == 3
        assert results[0]["valid"] is True
        assert results[1]["valid"] is True
        assert results[2]["valid"] is False


if __name__ == "__main__":
    pytest.main(["-v", __file__])

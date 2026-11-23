# -*- coding: utf-8 -*-
"""
Unit Tests for ImageExtractor Service (Day 09 - Multimodal Vision OCR Ingestion)
Author: AI Coding Tutor Team
Description:
    Bộ kiểm thử an ninh và chức năng toàn diện cho ImageExtractor:
    - Nhận diện Magic Bytes và định dạng MIME (PNG, JPEG, WEBP)
    - Kiểm soát kích thước tối đa 5MB
    - Chống Path Traversal trong tên file ảnh
    - Từ chối file nhị phân / định dạng không được hỗ trợ (.gif, .bmp, text giả mạo)
    - Tự động thu nhỏ ảnh vượt ngưỡng (> 2048px)
    - Bóc tách mã nguồn và thông báo lỗi (Traceback/IndexError) qua Vision OCR Mock Client
    - Chế độ Fallback an toàn khi offline hoặc thiếu API Key
"""

import io
import sys
import os
import asyncio
import hashlib
import warnings
import pytest
from pathlib import Path
from PIL import Image

# Suppress harmless warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Đảm bảo đường dẫn import backend
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.image_extractor import (
    ImageExtractor,
    image_extractor,
    MAX_IMAGE_SIZE_BYTES,
    MAX_IMAGE_DIMENSION,
    ALLOWED_IMAGE_MIMES
)


def create_test_image_bytes(fmt: str = "PNG", size: tuple = (150, 150), color: str = "blue") -> bytes:
    """Tạo chuỗi bytes ảnh hợp lệ trong bộ nhớ phục vụ kiểm thử."""
    img = Image.new("RGB", size, color=color)
    buf = io.BytesIO()
    img.save(buf, format=fmt)
    return buf.getvalue()


class TestImageExtractor:
    """Bộ kiểm thử chức năng và bảo mật cho ImageExtractor."""

    def test_01_valid_png_and_jpeg_detection(self):
        """Kiểm tra nhận diện đúng file PNG và JPEG qua magic bytes."""
        png_bytes = create_test_image_bytes("PNG")
        res_png = asyncio.run(image_extractor.extract_image(png_bytes, "terminal_error.png"))

        assert res_png["valid"] is True
        assert res_png["mime_type"] == "image/png"
        assert res_png["filename"] == "terminal_error.png"
        assert res_png["image_size_bytes"] == len(png_bytes)
        assert res_png["sha256"] == hashlib.sha256(png_bytes).hexdigest()
        assert res_png["error"] is None

        jpeg_bytes = create_test_image_bytes("JPEG")
        res_jpeg = asyncio.run(image_extractor.extract_image(jpeg_bytes, "ide_screenshot.jpg"))

        assert res_jpeg["valid"] is True
        assert res_jpeg["mime_type"] == "image/jpeg"
        assert res_jpeg["filename"] == "ide_screenshot.jpg"

    def test_02_oversized_image_rejection(self):
        """Kiểm tra chặn đứng ảnh có kích thước vượt quá 5MB."""
        # Giả lập payload > 5MB
        huge_bytes = b"\x89PNG\r\n\x1a\n" + (b"\x00" * (MAX_IMAGE_SIZE_BYTES + 1024))
        res = asyncio.run(image_extractor.extract_image(huge_bytes, "huge_screenshot.png"))

        assert res["valid"] is False
        assert res["error"] is not None
        assert "vượt quá giới hạn" in res["error"]

    def test_03_unsupported_or_fake_image_rejection(self):
        """Kiểm tra từ chối file văn bản hoặc file thực thi đổi đuôi thành .png."""
        fake_image = b"THIS IS JUST TEXT CONTENT, NOT AN IMAGE"
        res1 = asyncio.run(image_extractor.extract_image(fake_image, "fake.png"))

        assert res1["valid"] is False
        assert "không được hỗ trợ" in res1["error"]

        empty_res = asyncio.run(image_extractor.extract_image(b"", "empty.png"))
        assert empty_res["valid"] is False
        assert "rỗng" in empty_res["error"]

    def test_04_path_traversal_sanitization(self):
        """Kiểm tra làm sạch tên file ảnh chống Path Traversal."""
        dirty_names = [
            ("../../secret/screen.png", "screen.png"),
            ("..\\..\\Windows\\leak.jpg", "leak.jpg"),
            ("nested/subfolder/terminal.webp", "terminal.webp"),
            ("inject\x00file.png", "injectfile.png"),
        ]

        for dirty, expected in dirty_names:
            clean = image_extractor.sanitize_filename(dirty)
            assert clean == expected
            assert "/" not in clean and "\\" not in clean
            assert ".." not in clean

    def test_05_fallback_when_api_key_missing(self):
        """Kiểm tra phản hồi fallback thân thiện khi chưa có GEMINI_API_KEY."""
        offline_extractor = ImageExtractor(custom_vision_client=None)
        offline_extractor.api_key = ""  # Ép rỗng API key

        png_bytes = create_test_image_bytes("PNG")
        res = asyncio.run(offline_extractor.extract_image(png_bytes, "error_trace.png"))

        assert res["valid"] is True
        assert "Vui lòng cấu hình GEMINI_API_KEY" in res["extracted_text"]
        assert "THÔNG TIN TRÍCH XUẤT TỪ ẢNH CHỤP" in res["formatted_markdown"]

    def test_06_mock_vision_ocr_code_and_error_parsing(self):
        """Kiểm tra bóc tách mã nguồn và traceback lỗi terminal từ kết quả Vision."""
        mock_terminal_ocr = (
            "Phát hiện lỗi runtime khi chạy script:\n\n"
            "Traceback (most recent call last):\n"
            "  File \"solution.py\", line 15, in <module>\n"
            "    print(arr[10])\n"
            "IndexError: list index out of range\n\n"
            "Đoạn mã nguồn được quan sát trên IDE:\n"
            "```python\n"
            "arr = [1, 2, 3]\n"
            "for i in range(10):\n"
            "    print(arr[i])\n"
            "```"
        )

        def mock_client(img_bytes, filename, mime):
            return mock_terminal_ocr

        mock_extractor = ImageExtractor(custom_vision_client=mock_client)
        png_bytes = create_test_image_bytes("PNG")

        res = asyncio.run(mock_extractor.extract_image(png_bytes, "terminal_index_error.png"))

        assert res["valid"] is True
        assert res["has_code"] is True
        assert res["has_error"] is True
        assert len(res["code_snippets"]) == 1
        assert "```python" in res["code_snippets"][0]
        assert res["error_traceback"] is not None
        assert "IndexError: list index out of range" in res["error_traceback"]
        assert "solution.py" in res["error_traceback"]

    def test_07_image_resizing_preprocessing(self):
        """Kiểm tra tự động thu nhỏ kích thước ảnh nếu vượt quá 2048px."""
        huge_dim_img = create_test_image_bytes("PNG", size=(2500, 1800))
        processed = image_extractor.preprocess_image(huge_dim_img, "image/png")

        # Đọc lại kích thước sau khi xử lý
        with Image.open(io.BytesIO(processed)) as img:
            w, h = img.size
            assert max(w, h) <= MAX_IMAGE_DIMENSION
            assert w == 2048  # Chiều lớn nhất bị giới hạn về 2048

    def test_08_batch_image_extraction(self):
        """Kiểm tra xử lý đồng thời danh sách nhiều ảnh đính kèm."""
        img1 = create_test_image_bytes("PNG")
        img2 = create_test_image_bytes("JPEG")

        batch_input = [
            (img1, "screen1.png", "image/png"),
            (img2, "screen2.jpg", "image/jpeg"),
            (b"", "empty.png", "image/png"),
        ]

        results = asyncio.run(image_extractor.extract_batch(batch_input))

        assert len(results) == 3
        assert results[0]["valid"] is True
        assert results[1]["valid"] is True
        assert results[2]["valid"] is False


if __name__ == "__main__":
    pytest.main(["-v", __file__])

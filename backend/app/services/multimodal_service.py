"""
Multimodal Processing Service
Author: AI Coding Tutor Team
Description:
    Bóc tách và chuẩn hóa dữ liệu đa phương thức (Files mã nguồn, Ảnh chụp màn hình lỗi/code, Text prompt)
    chuyển thành một Ngữ cảnh Thống nhất (Unified Context) chuẩn bị cho RAG & LLM.
"""

import os
import re
import logging
from typing import List, Dict, Any, Optional
from app.core.config import settings
from app.services.file_extractor import file_extractor, ALLOWED_CODE_EXTENSIONS
from app.services.image_extractor import image_extractor, ALLOWED_IMAGE_MIMES

logger = logging.getLogger("MultimodalService")

SUPPORTED_CODE_EXTS = ALLOWED_CODE_EXTENSIONS

class MultimodalService:
    def __init__(self):
        self.gemini_api_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")

    def process_code_file(self, content_bytes: bytes, filename: str) -> Dict[str, Any]:
        """Bóc tách nội dung từ file mã nguồn người dùng tải lên thông qua FileExtractor bảo mật."""
        return file_extractor.extract_file(content_bytes, filename)

    async def process_image_vision(self, image_bytes: bytes, filename: str, mime_type: str = "image/png") -> Dict[str, Any]:
        """Sử dụng ImageExtractor chuyên sâu (Gemini 1.5 Flash Vision) để nhận diện code & lỗi từ ảnh chụp."""
        return await image_extractor.extract_image(image_bytes, filename, mime_type)

    def build_unified_prompt(
        self,
        prompt_text: str,
        files_data: List[Dict[str, Any]],
        images_data: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Tổng hợp tất cả đầu vào (Text + Files + Images) thành một Ngữ cảnh Thống nhất.
        """
        sections = []
        if prompt_text.strip():
            sections.append(f"### Câu hỏi của sinh viên:\n{prompt_text.strip()}\n")

        if files_data:
            sections.append("### Danh sách file code đính kèm:")
            for f in files_data:
                sections.append(f["formatted_markdown"])

        if images_data:
            sections.append("### Thông tin trích xuất từ ảnh chụp màn hình:")
            for img in images_data:
                sections.append(img["formatted_markdown"])

        unified_context = "\n".join(sections)
        
        # Tạo chuỗi truy vấn ngắn gọn để search Vector DB
        search_query = prompt_text
        if not search_query and images_data:
            # Lấy 200 ký tự đầu của ảnh trích xuất làm query
            search_query = images_data[0]["extracted_text"][:200]
        elif not search_query and files_data:
            search_query = f"Lỗi trong mã nguồn {files_data[0]['filename']}"

        return {
            "search_query": search_query or "Lập trình cơ bản và xử lý lỗi",
            "unified_context": unified_context
        }

multimodal_service = MultimodalService()


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
from typing import List, Dict, Any, Optional, Tuple, Union
from app.core.config import settings
from app.services.file_extractor import file_extractor, ALLOWED_CODE_EXTENSIONS
from app.services.image_extractor import image_extractor, ALLOWED_IMAGE_MIMES
from app.services.query_synthesizer import query_synthesizer

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
        images_data: List[Dict[str, Any]],
        rag_chunks: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Tổng hợp tất cả đầu vào (Text + Files + Images + RAG Chunks) thành một Ngữ cảnh Thống nhất
        thông qua QuerySynthesizer.
        """
        return query_synthesizer.build_unified_payload(
            prompt=prompt_text,
            files_data=files_data,
            images_data=images_data,
            rag_chunks=rag_chunks
        )

    async def synthesize_and_retrieve(
        self,
        prompt: str = "",
        code_files: Optional[List[Union[Dict[str, Any], Tuple[bytes, str]]]] = None,
        image_files: Optional[List[Union[Dict[str, Any], Tuple[bytes, str, str]]]] = None,
        rag_top_k: int = 4,
        language_filter: Optional[str] = None
    ) -> Dict[str, Any]:
        """Ủy quyền thực thi toàn bộ pipeline đa phương thức tới QuerySynthesizer."""
        return await query_synthesizer.synthesize_and_retrieve(
            prompt=prompt,
            code_files=code_files,
            image_files=image_files,
            rag_top_k=rag_top_k,
            language_filter=language_filter
        )

multimodal_service = MultimodalService()

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

logger = logging.getLogger("MultimodalService")

SUPPORTED_CODE_EXTS = ALLOWED_CODE_EXTENSIONS

class MultimodalService:
    def __init__(self):
        self.gemini_api_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")

    def process_code_file(self, content_bytes: bytes, filename: str) -> Dict[str, Any]:
        """Bóc tách nội dung từ file mã nguồn người dùng tải lên thông qua FileExtractor bảo mật."""
        return file_extractor.extract_file(content_bytes, filename)

    async def process_image_vision(self, image_bytes: bytes, filename: str, mime_type: str = "image/png") -> Dict[str, Any]:
        """
        Sử dụng Vision Model (Google Gemini 1.5 Flash Vision) để nhận diện code & lỗi từ ảnh chụp.
        Nếu không có API Key, sử dụng fallback thông báo rõ ràng.
        """
        if not self.gemini_api_key:
            logger.warning("Chưa cấu hình GEMINI_API_KEY. Sử dụng fallback mô phỏng cho ảnh.")
            fallback_text = f"[Ảnh đính kèm `{filename}`: Đã tiếp nhận ảnh chụp lỗi/code. Vui lòng cấu hình GEMINI_API_KEY trong .env để kích hoạt AI Vision OCR tự động.]"
            return {
                "filename": filename,
                "extracted_text": fallback_text,
                "formatted_markdown": f"### Phân tích ảnh: `{filename}`\n{fallback_text}\n"
            }

        try:
            import google.generativeai as genai
            genai.configure(api_key=self.gemini_api_key)
            model = genai.GenerativeModel(settings.GEMINI_MODEL)

            vision_prompt = (
                "Bạn là bộ trích xuất OCR chuyên sâu cho lập trình viên. Hãy quan sát ảnh chụp được gửi lên:\n"
                "1. Nếu ảnh chứa mã nguồn (Code): Trích xuất chính xác 100% từng dòng code, giữ nguyên cấu trúc thụt lề, đặt trong khối ```<language>.\n"
                "2. Nếu ảnh chứa thông báo lỗi / màn hình Terminal: Trích xuất loại lỗi (Error type), dòng phát sinh lỗi và Call Stack / Traceback.\n"
                "3. Nếu ảnh là đề bài bài tập: Trích xuất yêu cầu, ràng buộc (constraints) và ví dụ I/O.\n"
                "Trả về kết quả bằng định dạng Markdown rõ ràng, trung thực, không tự ý giải bài."
            )

            response = model.generate_content([
                vision_prompt,
                {"mime_type": mime_type, "data": image_bytes}
            ])
            extracted = response.text or "[Không phát hiện văn bản hoặc code trong ảnh]"
            
            return {
                "filename": filename,
                "extracted_text": extracted,
                "formatted_markdown": f"### Phân tích từ ảnh chụp `{filename}`:\n{extracted}\n"
            }
        except Exception as e:
            logger.error(f"Lỗi khi xử lý Vision API: {e}")
            return {
                "filename": filename,
                "extracted_text": f"[Lỗi xử lý ảnh {filename}: {str(e)}]",
                "formatted_markdown": f"### Phân tích ảnh `{filename}`:\n[Lỗi bóc tách ảnh: {str(e)}]\n"
            }

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


"""
Socratic AI Tutor Service (Day 11 Sprint)
Author: AI Coding Tutor Team
Description:
    Trợ giảng AI Socratic dựa trên kho tri thức RAG và mô hình LLM (Gemini 1.5 Flash).
    - Áp dụng phương pháp Socratic: Định hướng tư duy, không giải hộ.
    - Grounding chặt chẽ trên tài liệu giáo trình RAG.
    - Dự phòng thông minh (Fallback) khi chạy offline hoặc thiếu API Key.
"""

import os
import re
import asyncio
import logging
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

from app.core.config import settings
from app.services.rag_service import rag_service
from app.services.query_synthesizer import query_synthesizer

logger = logging.getLogger("TutorService")

SOCRATIC_SYSTEM_PROMPT = """Bạn là "Socratic Coding Tutor" - Trợ giảng lập trình thông minh, ân cần và kiên nhẫn của trường Đại học.
Mục tiêu cao nhất của bạn là giúp sinh viên TỰ PHÁT HIỆN LỖI và HIỂU BẢN CHẤT THUẬT TOÁN, tuyệt đối không đưa ra lời giải hoàn chỉnh ngay từ đầu.

NGUYÊN TẮC HOẠT ĐỘNG BẮT BUỘC:
1. DỰA TRÊN TÀI LIỆU CHÍNH THỐNG (RAG GROUNDING):
   - Mọi giải thích về cú pháp, quy chuẩn và lý thuyết PHẢI dựa vào thông tin được cung cấp trong [TÀI LIỆU GIÁO TRÌNH CHÍNH THỐNG TỪ RAG].
   - Khi đưa ra khái niệm, hãy nêu rõ nguồn (Ví dụ: "Theo Giáo trình C++ - Chương 5 về Quản lý bộ nhớ...").

2. PHƯƠNG PHÁP GỢI MỞ (SOCRATIC METHOD):
   - Bước 1: Công nhận nỗ lực bài làm của sinh viên và xác định vị trí gặp sự cố (dòng code, điều kiện vòng lặp, giải phóng bộ nhớ).
   - Bước 2: Chỉ ra hiện tượng và triệu chứng lỗi (Ví dụ: Chỉ mục mảng vượt ngoài biên / Con trỏ bị treo / Time Limit Exceeded).
   - Bước 3: Đặt 1-2 câu hỏi dẫn dắt để sinh viên tự suy nghĩ nguyên nhân cốt lõi.
   - Bước 4: Viện dẫn kiến thức giáo trình liên quan để sinh viên đối chiếu.

3. KHÔNG VI PHẠM NỘI QUY HỌC THUẬT:
   - Tuyệt đối KHÔNG viết lại toàn bộ mã nguồn bài giải đúng cho sinh viên.
   - Chỉ đưa ra gợi ý logic hoặc snippet 1-2 dòng tối giản minh họa cho khái niệm trừu tượng.
"""


class TutorService:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
        self.model_name = settings.GEMINI_MODEL or "gemini-3-flash-preview"
        self._init_llm()

    def _init_llm(self):
        self._genai_client = None
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key, transport="rest")
                self._genai_client = genai.GenerativeModel(
                    model_name=self.model_name,
                    system_instruction=SOCRATIC_SYSTEM_PROMPT,
                    generation_config={
                        "temperature": 0.2,
                        "top_p": 0.95,
                        "max_output_tokens": 2048,
                    }
                )
                logger.info(f"Khởi tạo Gemini LLM Engine ({self.model_name}) thành công.")
            except Exception as e:
                logger.warning(f"Không thể khởi tạo Gemini API: {e}. Kích hoạt chế độ Socratic Fallback.")
                self._genai_client = None

    def _build_socratic_fallback(
        self,
        prompt: str,
        detected_language: Optional[str],
        detected_errors: List[str],
        rag_chunks: List[Dict[str, Any]],
        files_data: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Tạo phản hồi chuẩn Socratic khi chạy offline hoặc chưa cấu hình Gemini API Key."""
        lang_display = (detected_language or "lập trình").upper()
        sections = []

        # Lời chào & ghi nhận
        sections.append(f"Chào em! Thầy đã xem qua câu hỏi và phần bài làm ngôn ngữ **{lang_display}** của em.\n")

        # Phân tích lỗi nếu có
        if detected_errors:
            err_list_str = ", ".join([f"`{e}`" for e in detected_errors[:2]])
            sections.append(f"🔍 **Phát hiện sự cố:** Mã nguồn của em đang phát sinh thông báo lỗi: {err_list_str}.")
            sections.append("Hiện tượng này thường xảy ra khi chương trình truy cập vùng dữ liệu chưa hợp lệ hoặc vi phạm logic thực thi.\n")
        elif prompt:
            sections.append(f"💡 **Vấn đề cần làm rõ:** Em đang tìm hiểu về chủ đề: *\"{prompt.strip()[:100]}\"*.\n")

        # Dẫn chứng giáo trình RAG
        if rag_chunks:
            top_doc = rag_chunks[0]
            sections.append("📖 **Cơ sở lý thuyết tham khảo từ Giáo trình chuẩn:**")
            sections.append(f"> Theo **{top_doc.get('source', 'Giáo trình chuẩn')}** - *{top_doc.get('section', 'Chương lý thuyết')}*:")
            
            # Trích đoạn ngắn gọn
            snippet = top_doc.get("content", "").strip()[:300].replace("\n", " ")
            sections.append(f"> \"{snippet}...\"\n")

        # Câu hỏi Socratic gợi mở tư duy
        sections.append("❓ **Câu hỏi gợi mở dành cho em:**")
        if detected_errors:
            sections.append("1. Em hãy đặt điểm kiểm tra (print/debugger) ngay trước dòng phát sinh lỗi, giá trị của biến tại thời điểm đó là bao nhiêu?")
            sections.append("2. Đối chiếu với đoạn tài liệu giáo trình phía trên, điều kiện biên của vòng lặp hoặc cấu trúc dữ liệu của em đã bao quát trường hợp này chưa?")
        else:
            sections.append("1. Theo em, trong trường hợp xấu nhất (worst-case), thuật toán này cần thực hiện bao nhiêu bước?")
            sections.append("2. Em có thể tối ưu không gian bộ nhớ bằng cách tận dụng biến có sẵn thay vì cấp phát mới không?")

        sections.append("\n*Em hãy thử kiểm tra lại theo gợi ý trên và gửi kết quả lại cho thầy cùng trao đổi tiếp nhé!*")

        # Sinh câu hỏi tiếp nối thông minh
        follow_ups = [
            "Làm thế nào để đặt breakpoint kiểm tra lỗi này?",
            "Giáo trình giải thích nguyên lý này chi tiết ở phần nào?",
            "Cách viết test case kiểm tra trường hợp biên (edge case)?"
        ]

        formatted_sources = [
            {
                "content": c.get("content", ""),
                "source": c.get("source", "Giáo trình tiêu chuẩn"),
                "section": c.get("section", "Kiến thức trọng tâm"),
                "language": c.get("language", "general"),
                "similarity_score": c.get("similarity_score", 0.85)
            }
            for c in rag_chunks
        ]

        return {
            "reply": "\n".join(sections),
            "sources": formatted_sources,
            "follow_ups": follow_ups
        }

    async def generate_tutor_response(
        self,
        prompt: str = "",
        language: Optional[str] = None,
        code_files_data: Optional[List[Dict[str, Any]]] = None,
        images_data: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Xử lý toàn diện câu hỏi của sinh viên thông qua RAG + LLM Socratic Engine.
        """
        code_files_data = code_files_data or []
        images_data = images_data or []

        # 1. Rút trích Search Query & Nhận diện ngôn ngữ
        search_query = query_synthesizer.extract_core_search_query(
            prompt=prompt,
            files_data=code_files_data,
            images_data=images_data
        )
        detected_lang = language or query_synthesizer.detect_programming_language(
            prompt=prompt,
            files_data=code_files_data,
            images_data=images_data
        )
        detected_errors = query_synthesizer.extract_consolidated_errors(
            prompt=prompt,
            files_data=code_files_data,
            images_data=images_data
        )

        # 2. Truy xuất RAG Chunks từ Dual-Collection ChromaDB
        rag_chunks = rag_service.search(
            query=search_query,
            language=detected_lang,
            top_k=settings.RAG_TOP_K or 4
        )

        # 3. Đóng gói Unified Context
        payload = query_synthesizer.build_unified_payload(
            prompt=prompt,
            files_data=code_files_data,
            images_data=images_data,
            rag_chunks=rag_chunks,
            detected_language=detected_lang
        )

        # 4. Gọi LLM Engine hoặc Socratic Fallback
        if not self._genai_client and (self.api_key or settings.GEMINI_API_KEY):
            self.api_key = self.api_key or settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
            self._init_llm()

        if self._genai_client:
            try:
                user_content = payload["unified_context"]
                response = await asyncio.to_thread(self._genai_client.generate_content, user_content)
                reply_text = response.text

                # Tạo danh sách câu hỏi gợi ý
                follow_ups = [
                    "Thầy có thể gợi ý thêm về điều kiện biên không?",
                    "Làm sao để tối ưu độ phức tạp thuật toán này?",
                    "Tài liệu giáo trình đề cập phương pháp giải nào tương tự?"
                ]

                formatted_sources = [
                    {
                        "content": c.get("content", ""),
                        "source": c.get("source", "Giáo trình tiêu chuẩn"),
                        "section": c.get("section", "Kiến thức trọng tâm"),
                        "language": c.get("language", "general"),
                        "similarity_score": c.get("similarity_score", 0.85)
                    }
                    for c in rag_chunks
                ]

                return {
                    "reply": reply_text,
                    "sources": formatted_sources,
                    "follow_ups": follow_ups
                }
            except Exception as e:
                logger.error(f"Lỗi khi gọi Gemini API ({e}), chuyển sang chế độ Socratic Fallback.")

        # Fallback an toàn khi offline hoặc Gemini API gặp sự cố
        return self._build_socratic_fallback(
            prompt=prompt,
            detected_language=detected_lang,
            detected_errors=detected_errors,
            rag_chunks=rag_chunks,
            files_data=code_files_data
        )


# Singleton instance toàn cục
tutor_service = TutorService()

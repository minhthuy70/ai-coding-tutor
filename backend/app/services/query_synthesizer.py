"""
Query Synthesizer & Unified Context Payload Service
Author: AI Coding Tutor Team (Day 10 Sprint)
Description:
    Tổng hợp dữ liệu đa phương thức (Văn bản câu hỏi, File mã nguồn, Ảnh chụp màn hình lỗi/code)
    thành:
    1. Câu truy vấn Vector cốt lõi (Core Search Query) ngắn gọn, súc tích, tránh pha loãng cosine.
    2. Tự động nhận diện ngôn ngữ lập trình chủ đạo (Python, C/C++, Java, JavaScript...).
    3. Trích xuất thông báo lỗi & Traceback tổng hợp.
    4. Tích hợp RAGService tìm kiếm Top-K chunks tài liệu giáo trình sát nhất.
    5. Đóng gói Unified Context Payload chuẩn bị nạp thẳng vào LLM Socratic Tutor.
"""

import os
import re
import logging
from typing import List, Dict, Any, Optional, Tuple, Union
from app.services.file_extractor import file_extractor
from app.services.image_extractor import image_extractor
from app.services.rag_service import rag_service

logger = logging.getLogger("QuerySynthesizer")

# Mẫu Regex bắt lỗi phổ biến trong lập trình
ERROR_PATTERNS = [
    # Python Traceback và Exceptions
    r"([A-Za-z]+(?:Error|Exception|Warning):\s+[^\n]+)",
    # C/C++ và System runtime errors
    r"(Segmentation fault(?:\s*\(core dumped\))?)",
    r"(core dumped)",
    r"(double free or corruption[^\n]*)",
    r"(stack smashing detected[^\n]*)",
    r"(Stack overflow[^\n]*)",
    r"(out of memory[^\n]*)",
    r"(Access violation[^\n]*)",
    # Compiler / Linker errors (gcc, g++, clang, msvc)
    r"(error:\s+[^\n]+)",
    r"(fatal error:\s+[^\n]+)",
    r"(undefined reference to\s+[^\n]+)",
    # Java / General exceptions
    r"(Exception in thread [^\n]+)",
    r"(NullPointerException[^\n]*)",
    r"(ArrayIndexOutOfBoundsException[^\n]*)",
]

# Từ khóa nhận diện ngôn ngữ trong câu hỏi
LANGUAGE_KEYWORDS = {
    "python": [r"\bpython\b", r"\bpy\b", r"\bpep\s*8\b", r"\bpytest\b", r"\bpip\b", r"\bdjango\b", r"\bfastapi\b", r"\bflask\b"],
    "cpp": [r"\bc\+\+\b", r"\bcpp\b", r"\bcon trỏ\b", r"\bpointer\b", r"\bvector\b", r"\bcout\b", r"\bcin\b", r"\bsegmentation fault\b", r"\bmalloc\b", r"\bfree\b"],
    "c": [r"\blập trình c\b", r"\bngôn ngữ c\b", r"\bfile c\b", r"\bstdio\.h\b", r"\bstdlib\.h\b"],
    "java": [r"\bjava\b", r"\bjvm\b", r"\bspring\b", r"\bpublic static void main\b"],
    "javascript": [r"\bjavascript\b", r"\bjs\b", r"\btypescript\b", r"\bts\b", r"\bnode\.?js\b", r"\breact\b"],
    "sql": [r"\bsql\b", r"\bselect\b", r"\bdatabase\b", r"\bpostgres\b", r"\bmysql\b"],
}


class QuerySynthesizer:
    """
    Bộ tổng hợp ngữ cảnh đa phương thức và sinh truy vấn RAG tối ưu.
    """

    def __init__(self):
        self.max_search_query_chars = 250

    def extract_consolidated_errors(
        self,
        prompt: str = "",
        files_data: Optional[List[Dict[str, Any]]] = None,
        images_data: Optional[List[Dict[str, Any]]] = None
    ) -> List[str]:
        """
        Quét và trích xuất tất cả các thông báo lỗi, exception, traceback xuất hiện trong prompt, code hoặc ảnh OCR.
        """
        detected_errors: List[str] = []
        seen = set()

        def _add_error(err: str):
            clean_err = err.strip()
            if clean_err and clean_err.lower() not in seen:
                seen.add(clean_err.lower())
                detected_errors.append(clean_err)

        # 1. Trích xuất từ ảnh OCR (đã được image_extractor nhận diện)
        if images_data:
            for img in images_data:
                # Nếu image_extractor đã phân tích detected_errors
                for err in img.get("detected_errors", []):
                    _add_error(err)
                
                # Quét thêm trong extracted_text
                ocr_text = img.get("extracted_text", "")
                if ocr_text:
                    for pattern in ERROR_PATTERNS:
                        matches = re.findall(pattern, ocr_text, flags=re.IGNORECASE)
                        for m in matches:
                            _add_error(m)

        # 2. Quét trong prompt của người dùng
        if prompt:
            for pattern in ERROR_PATTERNS:
                matches = re.findall(pattern, prompt, flags=re.IGNORECASE)
                for m in matches:
                    _add_error(m)

        # 3. Quét trong nội dung các file code đính kèm (nếu file chứa log hoặc comment lỗi)
        if files_data:
            for f in files_data:
                raw_code = f.get("raw_content", "")
                if raw_code:
                    for pattern in ERROR_PATTERNS:
                        matches = re.findall(pattern, raw_code, flags=re.IGNORECASE)
                        for m in matches:
                            _add_error(m)

        return detected_errors

    def detect_programming_language(
        self,
        prompt: str = "",
        files_data: Optional[List[Dict[str, Any]]] = None,
        images_data: Optional[List[Dict[str, Any]]] = None
    ) -> Optional[str]:
        """
        Tự động nhận diện ngôn ngữ lập trình chủ đạo từ File extensions, Image OCR code blocks hoặc Prompt text.
        """
        # Ưu tiên 1: Lấy từ file mã nguồn đính kèm
        if files_data:
            for f in files_data:
                lang = f.get("language")
                if lang and lang != "text":
                    return lang.lower()

        # Ưu tiên 2: Lấy từ code blocks trích xuất từ ảnh OCR
        if images_data:
            for img in images_data:
                code_blocks = img.get("code_blocks", [])
                for block in code_blocks:
                    lang = block.get("language")
                    if lang and lang not in ("text", "", "plain"):
                        return lang.lower()

        # Ưu tiên 3: Quét từ khóa trong prompt của sinh viên
        if prompt:
            prompt_lower = prompt.lower()
            for lang, patterns in LANGUAGE_KEYWORDS.items():
                for pat in patterns:
                    if re.search(pat, prompt_lower):
                        return lang

        # Mặc định: None (cho phép RAG tìm trên toàn bộ kho tri thức)
        return None

    def extract_core_search_query(
        self,
        prompt: str = "",
        files_data: Optional[List[Dict[str, Any]]] = None,
        images_data: Optional[List[Dict[str, Any]]] = None
    ) -> str:
        """
        Trích xuất câu truy vấn tìm kiếm Vector DB cốt lõi (Search Query).
        Nguyên tắc SOTA:
        - Tuyệt đối KHÔNG đưa toàn bộ 500 dòng code vào vector query vì sẽ làm loãng cosine similarity.
        - Tập trung vào: Ý định câu hỏi cốt lõi + Tên lỗi / Loại ngoại lệ cụ thể + Khái niệm thuật toán.
        - Giới hạn độ dài tối đa (max 250 ký tự) để embedding model biểu diễn chính xác nhất.
        """
        clean_prompt = prompt.strip() if prompt else ""
        errors = self.extract_consolidated_errors(clean_prompt, files_data, images_data)

        # Loại bỏ các đoạn code dài trong prompt nếu người dùng paste trực tiếp vào chat
        clean_prompt_no_code = re.sub(r"```[\s\S]*?```", "", clean_prompt).strip()
        # Loại bỏ các dòng trống liên tiếp
        clean_prompt_no_code = re.sub(r"\s+", " ", clean_prompt_no_code)

        query_components: List[str] = []

        # Tình huống 1: Người dùng có đặt câu hỏi
        if clean_prompt_no_code:
            # Lọc bỏ các từ đệm chào hỏi không mang nghĩa kỹ thuật
            filtered_prompt = re.sub(
                r"^(?:chào (?:thầy|cô|bạn|bot|trợ giảng)|alo|hi|hello|cho em hỏi|thầy ơi|giúp em|ad ơi)[,\s]+",
                "",
                clean_prompt_no_code,
                flags=re.IGNORECASE
            ).strip()

            # Lấy câu hỏi chính (tối đa 150 ký tự đầu)
            if filtered_prompt:
                query_components.append(filtered_prompt[:150])

        # Tình huống 2: Có lỗi cụ thể phát hiện được
        if errors:
            # Lấy tối đa 2 lỗi tiêu biểu nhất
            error_str = " | ".join(errors[:2])
            # Nếu chưa có trong query components thì thêm vào
            if not any(error_str.lower() in comp.lower() for comp in query_components):
                query_components.append(f"Lỗi {error_str}")

        # Tình huống 3: Không có prompt, chỉ có file hoặc ảnh
        if not query_components:
            if images_data:
                # Lấy tên file hoặc 100 ký tự đầu trích xuất được từ ảnh
                img = images_data[0]
                ocr_snippet = img.get("extracted_text", "").strip()[:100]
                if ocr_snippet:
                    # Lấy dòng đầu tiên không trống
                    first_line = [l.strip() for l in ocr_snippet.splitlines() if l.strip()]
                    query_components.append(first_line[0] if first_line else "Lỗi hiển thị màn hình lập trình")
                else:
                    query_components.append(f"Xử lý lỗi ảnh chụp {img.get('filename', 'màn hình')}")
            elif files_data:
                f = files_data[0]
                lang = f.get("language", "mã nguồn")
                query_components.append(f"Tối ưu và phân tích cấu trúc {lang} trong file {f.get('filename', 'code')}")
            else:
                query_components.append("Khái niệm lập trình và tối ưu thuật toán")

        # Ghép các thành phần và cắt tỉa
        unified_query = " - ".join(query_components).strip()
        if len(unified_query) > self.max_search_query_chars:
            unified_query = unified_query[:self.max_search_query_chars].rsplit(" ", 1)[0]

        return unified_query

    def build_unified_payload(
        self,
        prompt: str = "",
        files_data: Optional[List[Dict[str, Any]]] = None,
        images_data: Optional[List[Dict[str, Any]]] = None,
        rag_chunks: Optional[List[Dict[str, Any]]] = None,
        detected_language: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Ghép toàn bộ đầu vào thành Unified Context Payload hoàn chỉnh theo cấu trúc chuẩn giáo trình.
        """
        files_data = files_data or []
        images_data = images_data or []
        rag_chunks = rag_chunks or []

        search_query = self.extract_core_search_query(prompt, files_data, images_data)
        lang = detected_language or self.detect_programming_language(prompt, files_data, images_data)
        errors = self.extract_consolidated_errors(prompt, files_data, images_data)

        # Xây dựng các phân đoạn Markdown cho LLM Prompt
        sections: List[str] = []

        # 1. CÂU HỎI CỦA SINH VIÊN
        if prompt.strip():
            sections.append(f"### [CÂU HỎI CỦA SINH VIÊN]\n{prompt.strip()}\n")
        else:
            sections.append("### [CÂU HỎI CỦA SINH VIÊN]\n(Sinh viên không nhập câu hỏi bằng chữ, gửi trực tiếp tệp mã nguồn hoặc ảnh chụp lỗi)\n")

        # 2. THÔNG BÁO LỖI PHÁT HIỆN ĐƯỢC
        if errors:
            sections.append("### [THÔNG BÁO LỖI PHÁT HIỆN ĐƯỢC]")
            for idx, err in enumerate(errors, 1):
                sections.append(f"- Lỗi {idx}: `{err}`")
            sections.append("")

        # 3. MÃ NGUỒN TỪ FILE ĐÍNH KÈM
        if files_data:
            sections.append("### [MÃ NGUỒN TỪ FILE ĐÍNH KÈM]")
            for f in files_data:
                if f.get("formatted_markdown"):
                    sections.append(f["formatted_markdown"])
                else:
                    sections.append(f"\n#### File: `{f.get('filename')}`\n```{f.get('language', '')}\n{f.get('raw_content', '')}\n```\n")

        # 4. THÔNG TIN TRÍCH XUẤT TỪ ẢNH CHỤP MÀN HÌNH (VISION OCR)
        if images_data:
            sections.append("### [THÔNG TIN TRÍCH XUẤT TỪ ẢNH CHỤP MÀN HÌNH]")
            for img in images_data:
                if img.get("formatted_markdown"):
                    sections.append(img["formatted_markdown"])
                else:
                    sections.append(f"\n#### Ảnh: `{img.get('filename')}`\n```text\n{img.get('extracted_text', '')}\n```\n")

        # 5. TÀI LIỆU GIÁO TRÌNH CHÍNH THỐNG TỪ RAG
        if rag_chunks:
            rag_markdown = rag_service.format_rag_context_for_prompt(rag_chunks)
            if rag_markdown:
                sections.append(rag_markdown)
        else:
            sections.append("### [TÀI LIỆU GIÁO TRÌNH CHÍNH THỐNG TỪ RAG]\n(Không tìm thấy đoạn trích dẫn giáo trình cụ thể khớp với truy vấn)\n")

        unified_markdown = "\n".join(sections).strip()

        return {
            "search_query": search_query,
            "detected_language": lang,
            "detected_errors": errors,
            "user_prompt": prompt,
            "files_summary": [
                {
                    "filename": f.get("filename"),
                    "language": f.get("language"),
                    "lines": f.get("line_count"),
                    "size_bytes": f.get("file_size_bytes")
                }
                for f in files_data
            ],
            "images_summary": [
                {
                    "filename": img.get("filename"),
                    "mime_type": img.get("mime_type"),
                    "code_blocks_count": len(img.get("code_blocks", [])),
                    "errors_count": len(img.get("detected_errors", []))
                }
                for img in images_data
            ],
            "rag_chunks": rag_chunks,
            "unified_context": unified_markdown,
            "total_context_chars": len(unified_markdown)
        }

    async def synthesize_and_retrieve(
        self,
        prompt: str = "",
        code_files: Optional[List[Union[Dict[str, Any], Tuple[bytes, str]]]] = None,
        image_files: Optional[List[Union[Dict[str, Any], Tuple[bytes, str, str]]]] = None,
        rag_top_k: int = 4,
        language_filter: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Luồng end-to-end trọn gói của Day 10:
        1. Xử lý bóc tách các file code (nếu truyền dạng raw bytes/filename).
        2. Xử lý OCR các ảnh chụp màn hình (nếu truyền dạng raw bytes/filename/mime).
        3. Rút trích Search Query & Nhận diện ngôn ngữ.
        4. Tìm kiếm tri thức liên quan từ RAGService (Dual-collection RRF).
        5. Đóng gói Unified Context Payload sẵn sàng cho Day 11 Tutor Engine.
        """
        # 1. Chuẩn hóa files mã nguồn
        processed_files: List[Dict[str, Any]] = []
        if code_files:
            for item in code_files:
                if isinstance(item, dict):
                    processed_files.append(item)
                elif isinstance(item, tuple) and len(item) == 2:
                    content_bytes, fname = item
                    ext_res = file_extractor.extract_file(content_bytes, fname)
                    processed_files.append(ext_res)

        # 2. Chuẩn hóa ảnh chụp
        processed_images: List[Dict[str, Any]] = []
        if image_files:
            for item in image_files:
                if isinstance(item, dict):
                    processed_images.append(item)
                elif isinstance(item, tuple) and len(item) >= 2:
                    img_bytes = item[0]
                    fname = item[1]
                    mime = item[2] if len(item) > 2 else "image/png"
                    ocr_res = await image_extractor.extract_image(img_bytes, fname, mime)
                    processed_images.append(ocr_res)

        # 3. Tạo search query và nhận diện ngôn ngữ
        search_query = self.extract_core_search_query(prompt, processed_files, processed_images)
        detected_lang = language_filter or self.detect_programming_language(prompt, processed_files, processed_images)

        # 4. Tìm kiếm tri thức từ RAGService
        logger.info(f"RAG Search Query: '{search_query}' (Language: {detected_lang}, Top-K: {rag_top_k})")
        rag_chunks = rag_service.search(
            query=search_query,
            language=detected_lang,
            top_k=rag_top_k
        )

        # 5. Đóng gói Unified Context Payload
        payload = self.build_unified_payload(
            prompt=prompt,
            files_data=processed_files,
            images_data=processed_images,
            rag_chunks=rag_chunks,
            detected_language=detected_lang
        )

        return payload


# Singleton instance toàn cục
query_synthesizer = QuerySynthesizer()

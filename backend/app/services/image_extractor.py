# -*- coding: utf-8 -*-
"""
Image Extractor Service (Day 09 - Multimodal Vision OCR Ingestion)
Author: AI Coding Tutor Team
Description:
    Module tiếp nhận, kiểm tra an ninh (Security Validation) và trích xuất nội dung
    từ ảnh chụp màn hình terminal, lỗi IDE hoặc đề bài của sinh viên.
    Tích hợp Google Gemini 1.5 Flash Vision API với prompt chuyên biệt cho lập trình,
    hỗ trợ nén ảnh lớn, chống Path Traversal và fallback an toàn khi offline.
"""

import os
import re
import io
import hashlib
import logging
import warnings
from typing import Dict, Any, List, Optional, Tuple

# Suppress harmless deprecation warnings from Google API
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

from app.core.config import settings

logger = logging.getLogger("ImageExtractor")

# Giới hạn kích thước ảnh tối đa: 5MB
MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024

# Kích thước chiều tối đa khuyến nghị cho OCR (tránh nghẽn băng thông và quota)
MAX_IMAGE_DIMENSION = 2048

# Danh mục định dạng ảnh MIME hợp lệ và extension tương ứng
ALLOWED_IMAGE_MIMES: Dict[str, str] = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/webp": ".webp"
}

ALLOWED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

# Magic bytes nhận diện định dạng ảnh
IMAGE_MAGIC_HEADERS = [
    (b"\x89PNG\r\n\x1a\n", "image/png"),
    (b"\xff\xd8\xff", "image/jpeg"),
    (b"RIFF", "image/webp")  # bytes 0-4 RIFF, bytes 8-12 WEBP
]


class ImageExtractorError(Exception):
    """Exception cơ sở cho lỗi xử lý ảnh."""
    pass


class ImageExtractor:
    """
    Dịch vụ trích xuất ảnh đa phương thức (Vision OCR) cho AI Coding Tutor.
    """

    def __init__(
        self,
        max_size_bytes: int = MAX_IMAGE_SIZE_BYTES,
        custom_vision_client: Optional[Any] = None
    ):
        self.max_size_bytes = max_size_bytes
        self.custom_vision_client = custom_vision_client
        self.api_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")

    def sanitize_filename(self, filename: str) -> str:
        r"""
        Làm sạch tên file ảnh, chống Path Traversal (../, ..\, null bytes).
        """
        if not filename:
            return "unnamed_image.png"

        cleaned = filename.replace("\x00", "").strip()
        cleaned = os.path.basename(cleaned)
        cleaned = re.sub(r'\.\.+[/\\?]', '', cleaned)
        cleaned = re.sub(r'[^a-zA-Z0-9_\.\- ]', '_', cleaned)

        if not cleaned or cleaned.startswith('.'):
            ext = os.path.splitext(filename)[1].lower()
            return f"upload_image{ext}" if ext in ALLOWED_IMAGE_EXTENSIONS else "upload_image.png"

        return cleaned

    def detect_mime_type(self, image_bytes: bytes, filename: str) -> Optional[str]:
        """
        Nhận diện chính xác MIME type của ảnh qua Magic Bytes và PIL header.
        Từ chối file không phải ảnh ngay cả khi có extension giả mạo.
        """
        if not image_bytes or len(image_bytes) < 12:
            return None

        # 1. Kiểm tra Magic Bytes
        if image_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
            return "image/png"
        if image_bytes.startswith(b"\xff\xd8\xff"):
            return "image/jpeg"
        if image_bytes.startswith(b"RIFF") and image_bytes[8:12] == b"WEBP":
            return "image/webp"

        # 2. Xác thực cấu trúc nhị phân qua PIL
        if PIL_AVAILABLE:
            try:
                with Image.open(io.BytesIO(image_bytes)) as img:
                    pil_fmt = (img.format or "").lower()
                    if pil_fmt == "png":
                        return "image/png"
                    elif pil_fmt in ("jpeg", "jpg"):
                        return "image/jpeg"
                    elif pil_fmt == "webp":
                        return "image/webp"
            except Exception:
                return None

        return None

    def validate_image(self, image_bytes: bytes, filename: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Kiểm tra tính an ninh và tính hợp lệ của file ảnh:
        - Kiểm tra rỗng
        - Kiểm tra kích thước (<= 5MB)
        - Kiểm tra magic bytes và MIME type
        """
        if not image_bytes or len(image_bytes) == 0:
            return False, "File ảnh rỗng (0 bytes).", None

        size = len(image_bytes)
        if size > self.max_size_bytes:
            max_mb = self.max_size_bytes / (1024 * 1024)
            size_mb = size / (1024 * 1024)
            return False, f"Kích thước ảnh ({size_mb:.2f}MB) vượt quá giới hạn tối đa cho phép ({max_mb:.1f}MB).", None

        mime_type = self.detect_mime_type(image_bytes, filename)
        if not mime_type or mime_type not in ALLOWED_IMAGE_MIMES:
            ext = os.path.splitext(filename)[1].lower()
            return False, f"Định dạng ảnh '{ext}' không được hỗ trợ hoặc file bị lỗi cấu trúc. Chỉ chấp nhận PNG, JPG, JPEG, WEBP.", None

        return True, None, mime_type

    def preprocess_image(self, image_bytes: bytes, mime_type: str) -> bytes:
        """
        Tối ưu hóa ảnh trước khi gửi sang Vision API:
        Nếu kích thước chiều vượt quá MAX_IMAGE_DIMENSION (2048px), thu nhỏ giữ tỷ lệ để tiết kiệm token và tăng tốc.
        """
        if not PIL_AVAILABLE:
            return image_bytes

        try:
            with Image.open(io.BytesIO(image_bytes)) as img:
                width, height = img.size
                if max(width, height) > MAX_IMAGE_DIMENSION:
                    scale = MAX_IMAGE_DIMENSION / max(width, height)
                    new_size = (int(width * scale), int(height * scale))
                    
                    # Chuyển đổi mode RGBA sang RGB nếu là JPEG
                    resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                    out_io = io.BytesIO()
                    
                    fmt = "PNG" if mime_type == "image/png" else ("WEBP" if mime_type == "image/webp" else "JPEG")
                    if fmt == "JPEG" and resized_img.mode in ("RGBA", "P"):
                        resized_img = resized_img.convert("RGB")
                        
                    resized_img.save(out_io, format=fmt, quality=85)
                    logger.info(f"Đã tối ưu hóa ảnh từ ({width}x{height}) xuống {new_size}")
                    return out_io.getvalue()
        except Exception as e:
            logger.warning(f"Lỗi tiền xử lý ảnh: {e}. Giữ nguyên ảnh gốc.")

        return image_bytes

    def parse_vision_response(self, text: str) -> Dict[str, Any]:
        """
        Phân tích kết quả văn bản trả về từ Vision Model:
        - Tách các khối mã nguồn ```<lang> ... ```
        - Nhận diện thông báo lỗi / traceback
        """
        code_snippets = re.findall(r'```[a-zA-Z0-9_\-]*\n[\s\S]*?```', text)
        has_code = len(code_snippets) > 0

        # Kiểm tra sự xuất hiện của lỗi terminal / exception
        error_keywords = [
            "traceback", "error", "exception", "segmentation fault",
            "syntaxerror", "typeerror", "valueerror", "indexerror",
            "keyerror", "nameerror", "attributeerror", "zerodivisionerror",
            "recursionerror", "assertionerror", "runtimeerror"
        ]
        has_error = any(kw in text.lower() for kw in error_keywords)

        # Trích xuất đoạn lỗi nếu có
        error_traceback = None
        if has_error:
            # Tìm đoạn có chứa Traceback hoặc dòng lỗi kết thúc
            tb_match = re.search(r'(Traceback[\s\S]+?)(?=\n\n|\Z|```)', text, re.IGNORECASE)
            if tb_match:
                error_traceback = tb_match.group(1).strip()

        return {
            "has_code": has_code,
            "has_error": has_error,
            "code_snippets": code_snippets,
            "error_traceback": error_traceback
        }

    async def extract_image(
        self,
        image_bytes: bytes,
        filename: str,
        mime_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Bóc tách toàn diện một ảnh chụp màn hình mã nguồn hoặc lỗi terminal:
        1. Làm sạch tên file và kiểm tra an ninh
        2. Tối ưu kích thước ảnh (nếu cần)
        3. Gọi Vision OCR (Gemini 1.5 Flash Vision hoặc Mock Client khi kiểm thử)
        4. Phân tích mã nguồn và lỗi, đóng gói Markdown chuẩn.
        """
        sanitized_name = self.sanitize_filename(filename)
        is_valid, error_msg, detected_mime = self.validate_image(image_bytes, sanitized_name)

        effective_mime = mime_type or detected_mime or "image/png"

        if not is_valid:
            logger.warning(f"Ảnh '{filename}' không hợp lệ: {error_msg}")
            return {
                "valid": False,
                "filename": sanitized_name,
                "original_filename": filename,
                "mime_type": effective_mime,
                "image_size_bytes": len(image_bytes) if image_bytes else 0,
                "image_size_kb": round((len(image_bytes) if image_bytes else 0) / 1024, 2),
                "sha256": None,
                "has_code": False,
                "has_error": False,
                "code_snippets": [],
                "error_traceback": None,
                "extracted_text": "",
                "formatted_markdown": f"### Phân tích ảnh: `{sanitized_name}` (Lỗi: {error_msg})\n",
                "error": error_msg
            }

        image_hash = hashlib.sha256(image_bytes).hexdigest()
        processed_bytes = self.preprocess_image(image_bytes, effective_mime)

        # 1. Trường hợp sử dụng Custom Vision Client (phục vụ Unit Test hoặc Offline Mock)
        if self.custom_vision_client is not None:
            extracted_text = self.custom_vision_client(processed_bytes, sanitized_name, effective_mime)
        # 2. Trường hợp chưa cấu hình GEMINI_API_KEY
        elif not self.api_key:
            logger.warning("Chưa cấu hình GEMINI_API_KEY. Kích hoạt fallback an toàn.")
            extracted_text = (
                f"[Ảnh đính kèm `{sanitized_name}`: Đã tiếp nhận ảnh chụp lỗi/code. "
                f"Vui lòng cấu hình GEMINI_API_KEY trong file .env để kích hoạt AI Vision OCR tự động.]"
            )
        # 3. Gọi Google Gemini 1.5 Flash Vision
        else:
            try:
                genai.configure(api_key=self.api_key)
                model = genai.GenerativeModel(settings.GEMINI_MODEL)

                vision_prompt = (
                    "Bạn là chuyên gia thị giác máy tính lập trình và trợ giảng code chuyên sâu. "
                    "Hãy quan sát ảnh chụp được gửi lên và trích xuất thông tin một cách trung thực, chính xác:\n"
                    "1. NẾU CÓ CODE: Trích xuất chính xác 100% từng dòng code, giữ nguyên cấu trúc thụt lề, đặt trong khối ```<ngôn_ngữ>.\n"
                    "2. NẾU CÓ LỖI TERMINAL/CONSOLE: Trích xuất loại lỗi (Error type), dòng phát sinh lỗi và thông báo chi tiết (Traceback/Stack trace).\n"
                    "3. NẾU LÀ ĐỀ BÀI: Trích xuất yêu cầu, ràng buộc (constraints) và ví dụ I/O.\n"
                    "Trả về kết quả bằng định dạng Markdown ngắn gọn, rõ ràng, không tự ý viết giải thuật thay thế."
                )

                response = model.generate_content([
                    vision_prompt,
                    {"mime_type": effective_mime, "data": processed_bytes}
                ])
                extracted_text = response.text or "[Không phát hiện văn bản hoặc mã nguồn trong ảnh]"
            except Exception as e:
                logger.error(f"Lỗi khi gọi Gemini Vision API cho {sanitized_name}: {e}")
                extracted_text = f"[Lỗi trích xuất ảnh {sanitized_name}: {str(e)}]"

        # Phân tích nội dung trích xuất
        analysis = self.parse_vision_response(extracted_text)

        formatted_markdown = (
            f"### THÔNG TIN TRÍCH XUẤT TỪ ẢNH CHỤP: `{sanitized_name}`\n"
            f"{extracted_text.strip()}\n"
        )

        return {
            "valid": True,
            "filename": sanitized_name,
            "original_filename": filename,
            "mime_type": effective_mime,
            "image_size_bytes": len(image_bytes),
            "image_size_kb": round(len(image_bytes) / 1024, 2),
            "sha256": image_hash,
            "has_code": analysis["has_code"],
            "has_error": analysis["has_error"],
            "code_snippets": analysis["code_snippets"],
            "error_traceback": analysis["error_traceback"],
            "extracted_text": extracted_text,
            "formatted_markdown": formatted_markdown,
            "error": None
        }

    async def extract_batch(
        self,
        images: List[Tuple[bytes, str, Optional[str]]]
    ) -> List[Dict[str, Any]]:
        """
        Bóc tách một danh sách các ảnh đính kèm.
        """
        results = []
        for img_bytes, fname, mime in images:
            res = await self.extract_image(img_bytes, fname, mime)
            results.append(res)
        return results


# Khởi tạo Singleton instance phục vụ toàn hệ thống
image_extractor = ImageExtractor()

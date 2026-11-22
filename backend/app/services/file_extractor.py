# -*- coding: utf-8 -*-
"""
File Extractor Service (Day 08 - Multimodal Source Code Ingestion)
Author: AI Coding Tutor Team
Description:
    Module tiếp nhận, kiểm tra an ninh (Security Validation) và trích xuất nội dung
    từ các file mã nguồn và tài liệu văn bản do người dùng tải lên.
    Hỗ trợ kiểm tra giới hạn kích thước (<= 2MB), chống Path Traversal,
    phát hiện file nhị phân độc hại giả mạo, trích xuất mã SHA-256 và định dạng Markdown chuẩn.
"""

import os
import re
import hashlib
import logging
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger("FileExtractor")

# Giới hạn kích thước file tối đa: 2MB (2 * 1024 * 1024 bytes)
MAX_FILE_SIZE_BYTES = 2 * 1024 * 1024

# Danh mục định dạng file mã nguồn và ngôn ngữ tương ứng
ALLOWED_CODE_EXTENSIONS: Dict[str, str] = {
    ".py": "python",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".c": "c",
    ".h": "cpp",
    ".hpp": "cpp",
    ".java": "java",
    ".js": "javascript",
    ".ts": "typescript",
    ".html": "html",
    ".css": "css",
    ".sql": "sql",
    ".json": "json",
    ".txt": "text",
    ".md": "markdown"
}

# Danh mục phần mở rộng nguy hiểm tuyệt đối bị cấm
DISALLOWED_EXTENSIONS = {
    ".exe", ".dll", ".so", ".bin", ".sh", ".bat", ".cmd", ".vbs",
    ".ps1", ".msi", ".jar", ".class", ".pyc", ".zip", ".tar", ".gz",
    ".7z", ".rar", ".iso"
}

# Magic bytes của các file thực thi và nén nhị phân phổ biến
BINARY_MAGIC_HEADERS = [
    b"MZ",                # Windows PE executable (EXE/DLL)
    b"\x7fELF",          # Linux ELF executable
    b"\xca\xfe\xba\xbe",  # Java Class file
    b"PK\x03\x04",        # ZIP / JAR archive
    b"\x1f\x8b\x08",      # GZIP compressed file
    b"Rar!\x1a\x07",      # RAR archive
    b"7z\xbc\xaf\x27\x1c" # 7-Zip archive
]


class FileExtractorError(Exception):
    """Exception cơ sở cho lỗi xử lý file."""
    pass


class FileSecurityError(FileExtractorError):
    """Lỗi vi phạm chính sách an ninh (kích thước, định dạng cấm, mã độc)."""
    pass


class FileExtractor:
    """
    Dịch vụ xử lý và trích xuất file mã nguồn đa phương thức cho AI Coding Tutor.
    """

    def __init__(self, max_size_bytes: int = MAX_FILE_SIZE_BYTES):
        self.max_size_bytes = max_size_bytes

    def sanitize_filename(self, filename: str) -> str:
        r"""
        Làm sạch tên file, chống tấn công Path Traversal (../, ..\, /etc/passwd, C:\...)
        và loại bỏ null bytes hoặc ký tự điều khiển nguy hiểm.
        """
        if not filename:
            return "unnamed_code.txt"

        # Loại bỏ null bytes
        cleaned = filename.replace("\x00", "").strip()

        # Lấy tên file gốc (basename), loại bỏ toàn bộ đường dẫn thư mục
        cleaned = os.path.basename(cleaned)

        # Xóa các chuỗi relative path nếu sót lại
        cleaned = re.sub(r'\.\.+[/\\?]', '', cleaned)

        # Chỉ giữ lại các ký tự an toàn cho tên file
        cleaned = re.sub(r'[^a-zA-Z0-9_\.\- ]', '_', cleaned)

        if not cleaned or cleaned.startswith('.'):
            # Nếu tên file chỉ có dấu chấm hoặc rỗng, bảo toàn đuôi file hợp lý
            ext = os.path.splitext(filename)[1].lower()
            return f"upload{ext}" if ext in ALLOWED_CODE_EXTENSIONS else "upload_file.txt"

        return cleaned

    def is_binary_content(self, content_bytes: bytes, threshold: float = 0.05) -> bool:
        """
        Kiểm tra xem nội dung file có phải là file nhị phân (binary/executable) giả mạo hay không.
        Kiểm tra qua 2 lớp:
        1. Kiểm tra Magic Byte Header của file thực thi.
        2. Đo tỷ lệ Null bytes (\x00) và ký tự không in được trong 4096 bytes đầu tiên.
        """
        if not content_bytes:
            return False

        # 1. Kiểm tra magic bytes
        for magic in BINARY_MAGIC_HEADERS:
            if content_bytes.startswith(magic):
                return True

        # 2. Kiểm tra tỷ lệ ký tự nhị phân / null bytes trong mẫu đầu tiên
        sample = content_bytes[:4096]
        if b"\x00" in sample:
            return True

        # Đếm ký tự điều khiển không in được (ngoại trừ \t, \n, \r)
        non_printable = sum(
            1 for byte in sample
            if (byte < 32 and byte not in (9, 10, 13)) or byte == 127
        )
        return (non_printable / len(sample)) > threshold

    def validate_file(self, content_bytes: bytes, filename: str) -> Tuple[bool, Optional[str]]:
        """
        Xác thực tính hợp lệ và an ninh của file:
        - Kiểm tra rỗng
        - Kiểm tra kích thước (<= 2MB)
        - Kiểm tra extension hợp lệ
        - Kiểm tra không phải file nhị phân giả mạo
        """
        # 1. Kiểm tra rỗng
        if not content_bytes or len(content_bytes) == 0:
            return False, "File rỗng (0 bytes). Vui lòng tải lên file có chứa mã nguồn."

        # 2. Kiểm tra kích thước
        size = len(content_bytes)
        if size > self.max_size_bytes:
            max_mb = self.max_size_bytes / (1024 * 1024)
            size_mb = size / (1024 * 1024)
            return False, f"Kích thước file ({size_mb:.2f}MB) vượt quá giới hạn tối đa cho phép ({max_mb:.1f}MB)."

        # 3. Kiểm tra phần mở rộng
        ext = os.path.splitext(filename)[1].lower()
        if ext in DISALLOWED_EXTENSIONS:
            return False, f"Định dạng file '{ext}' bị từ chối vì lý do an toàn bảo mật."

        if ext not in ALLOWED_CODE_EXTENSIONS:
            allowed_list = ", ".join(ALLOWED_CODE_EXTENSIONS.keys())
            return False, f"Định dạng file '{ext}' không được hỗ trợ. Chỉ chấp nhận các định dạng: {allowed_list}"

        # 4. Kiểm tra file nhị phân giả mạo (ví dụ .exe đổi đuôi thành .py)
        if self.is_binary_content(content_bytes):
            return False, "Phát hiện nội dung file dạng nhị phân/thực thi không hợp lệ. Chỉ chấp nhận mã nguồn văn bản thuần."

        return True, None

    def decode_text_content(self, content_bytes: bytes) -> str:
        """
        Giải mã chuỗi bytes thành văn bản an toàn:
        Ưu tiên UTF-8, UTF-8 with BOM, fallback sang latin-1.
        """
        encodings = ["utf-8-sig", "utf-8", "latin-1"]
        for enc in encodings:
            try:
                return content_bytes.decode(enc)
            except UnicodeDecodeError:
                continue
        # Fallback an toàn thay thế ký tự lỗi
        return content_bytes.decode("utf-8", errors="replace")

    def extract_file(self, content_bytes: bytes, filename: str) -> Dict[str, Any]:
        """
        Bóc tách toàn diện một file mã nguồn:
        - Làm sạch tên file
        - Xác thực an ninh
        - Tính toán hash SHA-256, dung lượng, số dòng, số ký tự
        - Trích xuất văn bản và đóng gói Markdown chuẩn kèm metadata.
        """
        sanitized_name = self.sanitize_filename(filename)
        is_valid, error_msg = self.validate_file(content_bytes, sanitized_name)

        if not is_valid:
            logger.warning(f"File '{filename}' không vượt qua kiểm tra an ninh: {error_msg}")
            return {
                "valid": False,
                "filename": sanitized_name,
                "original_filename": filename,
                "extension": os.path.splitext(sanitized_name)[1].lower(),
                "language": "unknown",
                "file_size_bytes": len(content_bytes) if content_bytes else 0,
                "file_size_kb": round((len(content_bytes) if content_bytes else 0) / 1024, 2),
                "sha256": None,
                "line_count": 0,
                "char_count": 0,
                "content": "",
                "formatted_markdown": f"### File đính kèm: `{sanitized_name}` (Lỗi: {error_msg})\n",
                "error": error_msg
            }

        # Giải mã văn bản
        text_content = self.decode_text_content(content_bytes)
        ext = os.path.splitext(sanitized_name)[1].lower()
        language = ALLOWED_CODE_EXTENSIONS.get(ext, "text")

        # Thống kê
        lines = text_content.count("\n") + (1 if text_content else 0)
        chars = len(text_content)
        file_hash = hashlib.sha256(content_bytes).hexdigest()

        # Định dạng khối Markdown chuẩn phục vụ AI Prompt
        markdown_block = (
            f"### FILE MÃ NGUỒN ĐÍNH KÈM: `{sanitized_name}` ({language.upper()} | {lines} dòng)\n"
            f"```{language}\n"
            f"{text_content}\n"
            f"```\n"
        )

        return {
            "valid": True,
            "filename": sanitized_name,
            "original_filename": filename,
            "extension": ext,
            "language": language,
            "file_size_bytes": len(content_bytes),
            "file_size_kb": round(len(content_bytes) / 1024, 2),
            "sha256": file_hash,
            "line_count": lines,
            "char_count": chars,
            "content": text_content,
            "formatted_markdown": markdown_block,
            "error": None
        }

    def extract_batch(self, files: List[Tuple[bytes, str]]) -> List[Dict[str, Any]]:
        """
        Bóc tách một danh sách các file đính kèm.
        """
        results = []
        for content_bytes, filename in files:
            res = self.extract_file(content_bytes, filename)
            results.append(res)
        return results


# Khởi tạo Singleton instance phục vụ toàn hệ thống
file_extractor = FileExtractor()

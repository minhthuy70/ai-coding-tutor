"""
Data Cleaning & Normalization Script for MinerU / PDF Outputs
Author: AI Coding Tutor Team
Description:
    Làm sạch sâu các file Markdown sinh ra từ MinerU:
    1. Chuẩn hóa mã hóa Unicode tiếng Việt (NFC).
    2. Loại bỏ các dòng Header/Footer rác, số trang (Page X of Y).
    3. Bảo tồn và làm sạch cấu trúc Code Blocks (```python, ```cpp,...).
    4. Xóa liên kết ảnh rác, bảng rỗng và chuẩn hóa các khoảng trắng thừa.
    5. Lưu kết quả sạch sẽ vào `data/06_rag_dataset/cleaned/`.
"""

import os
import re
import sys
import unicodedata
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("DataCleaner")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"
OUTPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "cleaned"

def clean_markdown_text(raw_text: str) -> str:
    """Xử lý làm sạch toàn diện một chuỗi Markdown."""
    # 1. Chuẩn hóa Unicode tiếng Việt về chuẩn dựng sẵn NFC
    text = unicodedata.normalize('NFC', raw_text)

    # 2. Xóa các ký tự điều khiển (Control characters) ngoại trừ \n, \t, \r
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)

    # 3. Xóa các mẫu số trang phổ biến
    text = re.sub(r'^(?:Page|Trang)\s+\d+(?:\s*(?:of|/)\s*\d+)?\s*$', '', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^\s*[-–—]\s*\d+\s*[-–—]\s*$', '', text, flags=re.MULTILINE)

    # 4. Xóa các watermark và tiêu đề tài liệu lặp lại ở đầu trang
    text = re.sub(r'^\s*(?:DRAFT|CONFIDENTIAL|INTERNAL USE ONLY)\s*$', '', text, flags=re.MULTILINE | re.IGNORECASE)

    # 5. Xóa các liên kết hình ảnh cục bộ bị vỡ hoặc rác từ MinerU (ví dụ: ![](images/...))
    text = re.sub(r'!\[.*?\]\((?!https?://).*?\)', '', text)

    # 6. Chuẩn hóa định dạng Code Block
    # Đảm bảo trước và sau ``` luôn có dòng trống để parser markdown không bị dính chữ
    text = re.sub(r'([^\n])\n(```[a-zA-Z0-9_\+\#\-]*)', r'\1\n\n\2', text)
    text = re.sub(r'(```)\n([^\n])', r'\1\n\n\2', text)

    # 7. Xóa các dòng chỉ chứa dấu gạch nối hoặc khoảng trắng thừa liên tiếp
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 8. Cắt tỉa khoảng trắng ở cuối mỗi dòng (trailing spaces)
    lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(lines)

    return text.strip()

def process_all_files():
    logger.info("=== BẮT ĐẦU QUÁ TRÌNH DATA CLEANING ===")
    logger.info(f"Nguồn dữ liệu: {INPUT_DIR}")
    logger.info(f"Đích lưu trữ: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md_files = list(INPUT_DIR.rglob("*.md"))

    if not md_files:
        logger.warning(f"Không tìm thấy file markdown nào trong {INPUT_DIR}.")
        # Nếu chưa có file từ parser, thử kiểm tra nếu có file markdown mẫu
        return

    logger.info(f"Tìm thấy {len(md_files)} file Markdown cần làm sạch.")
    total_processed = 0

    for file_path in md_files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                raw_content = f.read()

            cleaned_content = clean_markdown_text(raw_content)

            # Tên file đầu ra giữ nguyên tên tài liệu
            out_filename = file_path.name
            out_file = OUTPUT_DIR / out_filename

            with open(out_file, "w", encoding="utf-8") as f:
                f.write(cleaned_content)

            reduction = (1 - len(cleaned_content) / max(len(raw_content), 1)) * 100
            logger.info(f"✅ Đã làm sạch: {file_path.name} (Giảm {reduction:.1f}% dung lượng rác) -> {out_file.name}")
            total_processed += 1
        except Exception as e:
            logger.error(f"❌ Lỗi khi làm sạch {file_path.name}: {e}")

    logger.info(f"=== HOÀN TẤT: Đã làm sạch thành công {total_processed} files ===")

if __name__ == "__main__":
    process_all_files()


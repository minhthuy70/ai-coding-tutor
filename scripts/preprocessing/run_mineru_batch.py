"""
Batch Runner for MinerU (Magic-PDF) Document Parser
Author: AI Coding Tutor Team
Description:
    Tự động quét đệ quy các tài liệu trong `data/01_original_documents`:
    - File .pdf: Bóc tách bố cục, code block, bảng biểu bằng MinerU (magic-pdf)
    - File .md, .rst, .html: Chuẩn hóa và đưa vào pipeline xử lý
"""

import os
import sys
import shutil
import subprocess
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("MinerU_BatchRunner")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_DIR = BASE_DIR / "data" / "01_original_documents"
OUTPUT_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"

def check_magic_pdf_installed() -> bool:
    """Kiểm tra xem magic-pdf CLI có khả dụng trong môi trường không."""
    try:
        res = subprocess.run(["magic-pdf", "--version"], capture_output=True, text=True, check=False)
        return res.returncode == 0
    except FileNotFoundError:
        return False

def parse_with_magic_pdf_cli(pdf_path: Path, out_dir: Path) -> bool:
    """Thực thi lệnh magic-pdf CLI."""
    logger.info(f"Đang bóc tách bằng MinerU (magic-pdf): {pdf_path.name}")
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "magic-pdf",
        "-p", str(pdf_path),
        "-o", str(out_dir),
        "-m", "auto"
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode == 0:
            logger.info(f"✅ Hoàn thành MinerU cho: {pdf_path.name}")
            return True
        else:
            logger.warning(f"MinerU trả về mã {proc.returncode}. Log: {proc.stderr[:200]}")
            return False
    except Exception as e:
        logger.error(f"Lỗi gọi magic-pdf CLI: {e}")
        return False

def fallback_pdf_extractor(pdf_path: Path, out_dir: Path):
    """Fallback an toàn bằng pypdf nếu máy chưa có GPU/weights MinerU."""
    logger.info(f"[FALLBACK] Trích xuất text an toàn cho: {pdf_path.name}")
    out_doc_dir = out_dir / pdf_path.stem
    out_doc_dir.mkdir(parents=True, exist_ok=True)
    out_md_file = out_doc_dir / f"{pdf_path.stem}.md"

    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf_path))
        extracted = []
        for i, page in enumerate(reader.pages):
            txt = page.extract_text() or ""
            extracted.append(f"\n\n## Trang {i + 1}\n\n{txt}")
        full_text = "\n".join(extracted)
    except Exception as e:
        full_text = f"# {pdf_path.stem}\n\n[Lỗi trích xuất PDF: {e}]"

    with open(out_md_file, "w", encoding="utf-8") as f:
        f.write(full_text)
    logger.info(f"✅ [FALLBACK] Đã lưu: {out_md_file.name}")

def handle_text_document(doc_path: Path, out_dir: Path):
    """Chuyển đổi trực tiếp các file .md, .rst, .html vào thư mục mineru output."""
    out_doc_dir = out_dir / doc_path.stem
    out_doc_dir.mkdir(parents=True, exist_ok=True)
    out_md_file = out_doc_dir / f"{doc_path.stem}.md"

    try:
        with open(doc_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        with open(out_md_file, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"✅ Đã đồng bộ tài liệu văn bản: {doc_path.name} -> {out_md_file.name}")
    except Exception as e:
        logger.error(f"Lỗi khi xử lý {doc_path.name}: {e}")

def main():
    logger.info("=== BẮT ĐẦU BATCH INGESTION VỚI MINERU & DOCUMENT PARSER ===")
    logger.info(f"Thư mục tài liệu gốc: {INPUT_DIR}")
    logger.info(f"Thư mục kết quả: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Quét đệ quy toàn bộ thư mục
    all_files = list(INPUT_DIR.rglob("*"))
    pdf_files = [f for f in all_files if f.is_file() and f.suffix.lower() == ".pdf"]
    text_files = [f for f in all_files if f.is_file() and f.suffix.lower() in [".md", ".rst", ".html", ".txt"]]

    logger.info(f"Tổng cộng: {len(pdf_files)} file PDF và {len(text_files)} file Markdown/RST/HTML.")
    has_mineru = check_magic_pdf_installed()
    logger.info(f"Trạng thái MinerU (magic-pdf): {'CÓ SẴN' if has_mineru else 'CHƯA CÓ / DÙNG FALLBACK NHANH'}")

    # 1. Xử lý các file PDF
    for pdf in pdf_files:
        success = False
        if has_mineru:
            success = parse_with_magic_pdf_cli(pdf, OUTPUT_DIR)
        if not success:
            fallback_pdf_extractor(pdf, OUTPUT_DIR)

    # 2. Xử lý các file Text / Markdown / RST / HTML
    for txt in text_files:
        handle_text_document(txt, OUTPUT_DIR)

    logger.info("=== HOÀN TẤT BATCH INGESTION! SẴN SÀNG CHO BƯỚC DATA CLEANING ===")

if __name__ == "__main__":
    main()

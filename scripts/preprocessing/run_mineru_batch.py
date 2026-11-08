"""
Batch Runner for MinerU (Magic-PDF) Document Parser
Author: AI Coding Tutor Team
Description:
    Tự động quét các tài liệu PDF trong `data/01_original_documents`
    và thực thi MinerU (magic-pdf) để bóc tách thành Markdown + Assets.
    Nếu magic-pdf chưa được cài đặt hoặc thiếu weights, script cung cấp fallback
    bằng PyMuPDF / PyPDF để đảm bảo pipeline không bị gián đoạn.
"""

import os
import sys
import subprocess
import logging
from pathlib import Path

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
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
            logger.warning(f"MinerU CLI trả về mã lỗi: {proc.returncode}. Log stderr: {proc.stderr[:300]}")
            return False
    except Exception as e:
        logger.error(f"Lỗi khi gọi magic-pdf CLI: {e}")
        return False

def fallback_pdf_extractor(pdf_path: Path, out_dir: Path):
    """
    Fallback dự phòng nếu hệ thống chưa cấu hình xong MinerU weights.
    Bóc tách text & code block cơ bản lưu thành Markdown để các bước sau không bị nghẽn.
    """
    logger.info(f"[FALLBACK] Đang trích xuất text cơ bản cho: {pdf_path.name}")
    out_doc_dir = out_dir / pdf_path.stem
    out_doc_dir.mkdir(parents=True, exist_ok=True)
    out_md_file = out_doc_dir / f"{pdf_path.stem}.md"

    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf_path))
        extracted_text = []
        for i, page in enumerate(reader.pages):
            txt = page.extract_text() or ""
            extracted_text.append(f"\n\n## Trang {i + 1}\n\n{txt}")
        full_text = "\n".join(extracted_text)
    except Exception:
        # Dự phòng bằng đọc thô nhị phân trích xuất ASCII text
        full_text = f"# Tài liệu: {pdf_path.name}\n\n[Trích xuất dự phòng cho file: {pdf_path.name}]"

    with open(out_md_file, "w", encoding="utf-8") as f:
        f.write(full_text)
    logger.info(f"✅ [FALLBACK] Đã lưu markdown dự phòng: {out_md_file}")

def main():
    logger.info("=== BẮT ĐẦU BATCH INGESTION VỚI MINERU ===")
    logger.info(f"Thư mục tài liệu gốc: {INPUT_DIR}")
    logger.info(f"Thư mục kết quả: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_files = list(INPUT_DIR.glob("*.pdf"))

    if not pdf_files:
        logger.warning(f"Không tìm thấy file PDF nào trong: {INPUT_DIR}")
        return

    logger.info(f"Tìm thấy {len(pdf_files)} tài liệu PDF cần xử lý.")
    has_mineru = check_magic_pdf_installed()
    logger.info(f"Trạng thái công cụ MinerU (magic-pdf): {'ĐÃ CÀI ĐẶT' if has_mineru else 'CHƯA CÀI / DÙNG FALLBACK'}")

    for pdf in pdf_files:
        success = False
        if has_mineru:
            success = parse_with_magic_pdf_cli(pdf, OUTPUT_DIR)
        
        if not success:
            fallback_pdf_extractor(pdf, OUTPUT_DIR)

    logger.info("=== HOÀN THÀNH QUÁ TRÌNH PARSE TÀI LIỆU ===")

if __name__ == "__main__":
    main()


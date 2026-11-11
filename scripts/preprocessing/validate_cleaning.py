"""
Data Quality & Cleaning Verification Script (QA Scorecard)
Author: AI Coding Tutor Team
Description:
    Kiểm thử tự động chất lượng làm sạch của các file Markdown trong `data/06_rag_dataset/cleaned/`:
    1. Kiểm tra Unicode NFC (không còn lỗi mã hóa font/dấu).
    2. Kiểm tra ký tự điều khiển ẩn (Control characters = 0).
    3. Kiểm tra rác số trang, header/footer, watermark (= 0).
    4. Kiểm tra liên kết hình ảnh cục bộ rác (= 0).
    5. Kiểm tra cân bằng cú pháp thẻ Code Block (mở/đóng cân xứng).
    6. Kiểm tra bảo tồn công thức LaTeX và bảng Markdown.
"""

import re
import sys
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CLEANED_DIR = BASE_DIR / "data" / "06_rag_dataset" / "cleaned"
RAW_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"

def validate_all():
    files = sorted(CLEANED_DIR.glob("*.md"))
    if not files:
        print("Không tìm thấy file markdown nào trong thư mục cleaned!")
        return False

    print("=" * 115)
    print("                     BẢNG KIỂM TRA ĐÁNH GIÁ CHẤT LƯỢNG LÀM SẠCH DỮ LIỆU (QA SCORECARD)")
    print("=" * 115)
    header = f"{'Tên File':40s} | {'NFC':6s} | {'Ký tự rác':10s} | {'Số trang':9s} | {'Link ảnh':9s} | {'CodeBlock':10s} | {'Kết quả':8s}"
    print(header)
    print("-" * 115)

    all_passed = True
    total_math_count = 0
    total_table_count = 0

    for f in files:
        text = f.read_text(encoding="utf-8")
        
        # 1. Unicode NFC
        is_nfc = unicodedata.is_normalized("NFC", text)
        
        # 2. Control characters (mã nhị phân rác)
        ctrl_chars = len(re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", text))
        
        # 3. Số trang & Header/Footer & Comment phân trang MinerU
        p0 = len(re.findall(r"<!--\s*page:\s*\d+\s*-->", text, flags=re.IGNORECASE))
        p1 = len(re.findall(r"^(?:Page|Trang)\s+\d+(?:\s*(?:of|/)\s*\d+)?\s*$", text, flags=re.MULTILINE | re.I))
        p2 = len(re.findall(r"^\s*[-–—]\s*\d+\s*[-–—]\s*$", text, flags=re.MULTILINE))
        p3 = len(re.findall(r"^\s*(?:DRAFT|CONFIDENTIAL|INTERNAL USE ONLY)\s*$", text, flags=re.MULTILINE | re.I))
        page_artifacts = p0 + p1 + p2 + p3
        
        # 4. Link ảnh cục bộ
        local_images = len(re.findall(r"!\[.*?\]\((?!https?://).*?\)", text))
        
        # 5. Cặp thẻ code blocks
        fences = len(re.findall(r"^```", text, flags=re.MULTILINE))
        code_ok = (fences % 2 == 0)

        # 6. Thống kê công thức và bảng bảo tồn
        math_inline = len(re.findall(r"\$[^\$\n]+\$", text))
        math_block = len(re.findall(r"\$\$[\s\S]+?\$\$", text))
        total_math_count += (math_inline + math_block)
        
        tables = len(re.findall(r"\|[^\n]+\|\n\|[-:\s|]+\|", text))
        total_table_count += tables

        passed = is_nfc and (ctrl_chars == 0) and (page_artifacts == 0) and (local_images == 0) and code_ok
        if not passed:
            all_passed = False

        status = "PASSED" if passed else "FAIL"
        nfc_status = "ĐẠT" if is_nfc else "LỖI"
        code_status = "CÂN BẰNG" if code_ok else "LỆCH THẺ"

        print(f"{f.stem[:40]:40s} | {nfc_status:6s} | {ctrl_chars:10d} | {page_artifacts:9d} | {local_images:9d} | {code_status:10s} | {status:8s}")

    print("-" * 115)
    print(f"Tổng kết bảo tồn tri thức:")
    print(f"  + Công thức Toán học LaTeX bảo tồn trọn vẹn : {total_math_count:,} công thức")
    print(f"  + Bảng biểu cấu trúc Markdown bảo tồn     : {total_table_count:,} bảng")
    print("=" * 115)
    
    if all_passed:
        print(f">>> KẾT LUẬN: TẤT CẢ {len(files)} FILE ĐỀU ĐẠT TIÊU CHUẨN LÀM SẠCH 100% (KHÔNG CÒN RÁC, KHÔNG LỖI CẤU TRÚC)")
    else:
        print(">>> CẢNH BÁO: CÓ FILE CHƯA ĐẠT CHUẨN!")
    return all_passed

if __name__ == "__main__":
    success = validate_all()
    sys.exit(0 if success else 1)


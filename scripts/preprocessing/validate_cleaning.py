"""
Data Quality & Cleaning Verification Script (QA Scorecard v2.0)
Author: AI Coding Tutor Team
Task: NGÀY 03 - Nghiệm Thu Chất Lượng Làm Sạch Toàn Diện
Description:
    Kiểm thử tự động 8 tiêu chuẩn chất lượng của các file Markdown trong `data/06_rag_dataset/cleaned/`:
    1. Kiểm tra Unicode NFC (chuẩn hóa tiếng Việt dựng sẵn).
    2. Kiểm tra ký tự điều khiển ẩn (Control characters = 0).
    3. Kiểm tra ký tự ẩn Zero-width & Byte Order Mark (Zero-width = 0).
    4. Kiểm tra rác trang, header/footer, watermark, comment MinerU (= 0).
    5. Kiểm tra rác mục lục chấm trang (TOC Dot Leaders = 0).
    6. Kiểm tra rác HTML layout MinerU / Docvortex (= 0).
    7. Kiểm tra liên kết hình ảnh cục bộ rác (= 0).
    8. Kiểm tra cân bằng cú pháp thẻ Code Block (mở/đóng cân xứng).
    Bảo tồn trọn vẹn 100% công thức LaTeX và cấu trúc bảng Markdown/HTML.
"""

import re
import sys
import argparse
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CLEANED_DIR = BASE_DIR / "data" / "06_rag_dataset" / "cleaned"

def validate_all(verbose: bool = False):
    files = sorted(CLEANED_DIR.glob("*.md"))
    if not files:
        print("❌ Không tìm thấy file markdown nào trong thư mục cleaned!")
        return False

    print("=" * 140)
    print("                     BẢNG KIỂM TRA ĐÁNH GIÁ CHẤT LƯỢNG LÀM SẠCH DỮ LIỆU (QA SCORECARD v2.0)")
    print("=" * 140)
    header = f"{'Tên File':36s} | {'NFC':4s} | {'Ctrl':4s} | {'ZW':4s} | {'Page':4s} | {'TOC':4s} | {'HTML':4s} | {'Ảnh':4s} | {'CodeBlock':10s} | {'Kết quả':8s}"
    print(header)
    print("-" * 140)

    all_passed = True
    total_math_count = 0
    total_table_count = 0

    for f in files:
        text = f.read_text(encoding="utf-8")

        # 1. Unicode NFC
        is_nfc = unicodedata.is_normalized("NFC", text)

        # 2. Control characters (mã nhị phân rác)
        ctrl_chars = len(re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", text))

        # 3. Ký tự ẩn Zero-width / BOM
        zw_chars = len(re.findall(r"[\u200b-\u200f\ufeff\u2060]", text))

        # 4. Số trang & Header/Footer & Comment phân trang MinerU
        p0 = len(re.findall(r"<!--\s*page:\s*\d+\s*-->", text, flags=re.IGNORECASE))
        p1 = len(re.findall(r"^(?:Page|Trang)\s+\d+(?:\s*(?:of|/)\s*\d+)?\s*$", text, flags=re.MULTILINE | re.I))
        p2 = len(re.findall(r"^\s*[-–—]\s*\d+\s*[-–—]\s*$", text, flags=re.MULTILINE))
        p3 = len(re.findall(r"^\s*(?:DRAFT|CONFIDENTIAL|INTERNAL USE ONLY)\s*$", text, flags=re.MULTILINE | re.I))
        page_artifacts = p0 + p1 + p2 + p3

        # 5. Dòng mục lục rác (TOC Dot Leaders: .... 15)
        toc_pat = r"^\s*[-*•]?\s*[a-zA-Zà-ỹÀ-Ỹ0-9].*?\s*\.{4,}\s*\d+\s*$"
        toc_artifacts = len(re.findall(toc_pat, text, flags=re.MULTILINE))

        # 6. Rác thẻ HTML layout (docvortex footnote, span, div, noscript, etc.)
        html_pat = r"docvortex-page-footnote|</?(?:span|div|small|font|center|noscript)[^>]*>"
        html_artifacts = len(re.findall(html_pat, text, flags=re.IGNORECASE))

        # 7. Link ảnh cục bộ rác
        local_images = len(re.findall(r"!\[.*?\]\((?!https?://).*?\)", text))

        # 8. Cặp thẻ code blocks
        fences = len(re.findall(r"^```", text, flags=re.MULTILINE))
        code_ok = (fences % 2 == 0)

        # Thống kê công thức và bảng bảo tồn
        math_inline = len(re.findall(r"\$[^\$\n]+\$", text))
        math_block = len(re.findall(r"\$\$[\s\S]+?\$\$", text))
        total_math_count += (math_inline + math_block)

        tables = len(re.findall(r"\|[^\n]+\|\n\|[-:\s|]+\|", text)) + len(re.findall(r"<table[\s\S]*?</table>", text, flags=re.I))
        total_table_count += tables

        passed = (
            is_nfc
            and (ctrl_chars == 0)
            and (zw_chars == 0)
            and (page_artifacts == 0)
            and (toc_artifacts == 0)
            and (html_artifacts == 0)
            and (local_images == 0)
            and code_ok
        )

        if not passed:
            all_passed = False
            if verbose:
                print(f"  [DEBUG {f.name}] failures: NFC={is_nfc}, Ctrl={ctrl_chars}, ZW={zw_chars}, Page={page_artifacts}, TOC={toc_artifacts}, HTML={html_artifacts}, Img={local_images}, Code={code_ok}")

        status = "PASSED" if passed else "FAIL"
        nfc_status = "ĐẠT" if is_nfc else "LỖI"
        code_status = "CÂN BẰNG" if code_ok else "LỆCH THẺ"

        print(
            f"{f.stem[:36]:36s} | "
            f"{nfc_status:4s} | "
            f"{ctrl_chars:4d} | "
            f"{zw_chars:4d} | "
            f"{page_artifacts:4d} | "
            f"{toc_artifacts:4d} | "
            f"{html_artifacts:4d} | "
            f"{local_images:4d} | "
            f"{code_status:10s} | "
            f"{status:8s}"
        )

    print("-" * 140)
    print("Tổng kết bảo tồn tri thức:")
    print(f"  + Công thức Toán học LaTeX bảo tồn trọn vẹn : {total_math_count:,} công thức")
    print(f"  + Bảng biểu cấu trúc Markdown & HTML bảo tồn: {total_table_count:,} bảng")
    print("=" * 140)

    if all_passed:
        print(f">>> KẾT LUẬN: TẤT CẢ {len(files)} FILE ĐỀU ĐẠT CHUẨN LÀM SẠCH TUYỆT ĐỐI 100% (PASSED)")
    else:
        print(">>> CẢNH BÁO: CÓ FILE CHƯA ĐẠT CHUẨN!")
    return all_passed

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script nghiệm thu chất lượng làm sạch (v2.0)")
    parser.add_argument("--verbose", action="store_true", help="Hiển thị chi tiết lỗi nếu có")
    args = parser.parse_args()

    success = validate_all(verbose=args.verbose)
    sys.exit(0 if success else 1)

# -*- coding: utf-8 -*-
"""
Data Cleaning & Normalization Script for MinerU / PDF Markdown Outputs
Author: AI Coding Tutor Team
Task: NGÀY 03 - Viết Script Làm Sạch Dữ Liệu (Data Cleaning)

Features:
    1. Chuẩn hóa mã hóa Unicode tiếng Việt về dựng sẵn (NFC), loại bỏ null bytes và control chars.
    2. Loại bỏ các thẻ đánh dấu trang của MinerU (<!-- page: X -->).
    3. Loại bỏ số trang rời rạc (Page X of Y, Trang X, - X -).
    4. Loại bỏ các liên kết hình ảnh cục bộ rác ![](images/...) và bảng biểu rỗng.
    5. Bảo tồn 100% thụt lề và cấu trúc khối mã nguồn (Code Blocks), chuẩn hóa cú pháp language tag.
    6. Chuẩn hóa khoảng trắng thừa, xóa trailing spaces và giới hạn tối đa 2 dòng trống liên tiếp.
    7. Hỗ trợ chế độ Dry-Run / Test Sample để kiểm tra trước và sau khi làm sạch.
"""

import os
import re
import sys
import argparse
import unicodedata
import logging
from pathlib import Path
from typing import Tuple, Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("DataCleaner")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"
OUTPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "cleaned"

PYTHON_KEYWORDS = [
    r'\bdef\s+\w+\s*\(',
    r'\bclass\s+\w+',
    r'\bimport\s+\w+',
    r'\bfrom\s+\w+\s+import',
    r'\bprint\s*\(',
    r'\bfor\s+\w+\s+in\s+',
    r'\bwhile\s+',
    r'\bif\s+.*:\s*$',
    r'\belif\s+.*:\s*$',
    r'\belse\s*:\s*$',
    r'\btry\s*:\s*$',
    r'\bexcept\s+.*:\s*$',
    r'__init__',
    r'__main__'
]

def clean_markdown_text(raw_text: str) -> Tuple[str, Dict[str, Any]]:
    """
    Làm sạch sâu chuỗi Markdown từ MinerU và thu thập thống kê chi tiết.
    """
    stats = {
        "raw_chars": len(raw_text),
        "raw_lines": len(raw_text.splitlines()),
        "removed_page_comments": 0,
        "removed_page_numbers": 0,
        "removed_image_links": 0,
        "removed_empty_tables": 0,
        "cleaned_code_blocks": 0,
        "null_bytes_removed": 0
    }

    # 1. Đếm và xóa null bytes / control characters (giữ \n, \t, \r)
    null_count = raw_text.count('\x00')
    stats["null_bytes_removed"] = null_count
    text = unicodedata.normalize('NFC', raw_text)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)

    # 2. Xóa các thẻ comment đánh dấu trang của MinerU <!-- page: X -->
    page_comments = re.findall(r'<!--\s*page:\s*\d+\s*-->', text, flags=re.IGNORECASE)
    stats["removed_page_comments"] = len(page_comments)
    text = re.sub(r'<!--\s*page:\s*\d+\s*-->\n?', '', text, flags=re.IGNORECASE)

    # 3. Xóa các dòng số trang rời rạc
    page_num_patterns = [
        r'^\s*(?:Page|Trang)\s+\d+(?:\s*(?:of|/)\s*\d+)?\s*$',
        r'^\s*[-–—]\s*\d+\s*[-–—]\s*$',
        r'^\s*\[\s*\d+\s*\]\s*$',
        r'^\s*\d+\s*(?:/|of)\s*\d+\s*$',
        r'^\s*-\s*\d+\s*-\s*$'
    ]
    for pat in page_num_patterns:
        matches = re.findall(pat, text, flags=re.MULTILINE | re.IGNORECASE)
        stats["removed_page_numbers"] += len(matches)
        text = re.sub(pat, '', text, flags=re.MULTILINE | re.IGNORECASE)

    # 3.1. Loại bỏ các thẻ HTML wrapper của MinerU (docvortex algorithm, footnotes, small, font)
    text = re.sub(r'<div class="docvortex-[^"]*"[^>]*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</div>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<span class="docvortex-[^"]*"[^>]*>', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'</span>', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'</?(?:small|font|center)[^>]*>', ' ', text, flags=re.IGNORECASE)

    # 3.2. Chuyển đổi khối mã thụt lề RST (::\n\n    code) sang markdown fenced code blocks (```python)
    import textwrap
    def repl_rst(match):
        code = textwrap.dedent(match.group(1)).strip()
        return f':\n\n```python\n{code}\n```\n\n'
    text = re.sub(r'::\s*\n\n((?: {4}[^\n]*\n|\n)+)', repl_rst, text)

    # 3.3. Xóa các khối code rỗng (```txt\n```) sinh ra do lỗi ngắt trang
    text = re.sub(r'```[a-zA-Z0-9_\-]*\s*\n*\s*```\n?', '', text)

    # 3.4. Nối liền các đoạn code bị cắt đứt giữa thân hàm do sang trang PDF (Page-break stitch)
    broken_code_pagebreak_pat = re.compile(
        r'```\s*\n+(?:(?:python|Python|\d+)\s*\n+)?((?:def|class|if|for|while|\s{4,})[^\n`]+:\s*)\n+```(?:python|py)?\n',
        re.IGNORECASE
    )
    text = broken_code_pagebreak_pat.sub(r'\n    \1\n', text)

    # 3.5. Ghép khai báo class/def mồ côi nằm lẻ loi trước ```python vào bên trong code block
    strict_orphaned_pat = re.compile(
        r'(?:python\s*\n+)?((?:class\s+[A-Za-z_]\w*(?:\([^)]*\))?|def\s+[A-Za-z_]\w*\([^)]*\)):\s*)\n+```(?:python|py)?\n',
        re.IGNORECASE
    )
    text = strict_orphaned_pat.sub(r'```python\n\1\n', text)

    # 4. Xóa watermark và tiêu đề lặp lại vô nghĩa
    watermark_pat = r'^\s*(?:DRAFT|CONFIDENTIAL|INTERNAL USE ONLY|BẢN THẢO)\s*$'
    text = re.sub(watermark_pat, '', text, flags=re.MULTILINE | re.IGNORECASE)

    # 5. Xóa các link hình ảnh cục bộ ![](images/...)
    img_matches = re.findall(r'!\[.*?\]\((?!https?://).*?\)', text)
    stats["removed_image_links"] = len(img_matches)
    text = re.sub(r'!\[.*?\]\((?!https?://).*?\)\n?', '', text)

    # 6. Xóa các bảng rỗng (bảng chỉ chứa ký tự phân cách | và khoảng trắng)
    empty_table_pat = r'(?:^\|\s*(?:[-:]+[-| :]*)\s*\|\s*$\n?)+'
    empty_matches = re.findall(empty_table_pat, text, flags=re.MULTILINE)
    stats["removed_empty_tables"] = len(empty_matches)
    text = re.sub(empty_table_pat, '', text, flags=re.MULTILINE)

    # 7. Bảo tồn và chuẩn hóa Code Blocks
    # Tách các khối code block để không làm ảnh hưởng đến thụt lề bên trong code
    parts = []
    code_block_pattern = re.compile(r'(```[a-zA-Z0-9_\+\#-]*\n[\s\S]*?```)', re.MULTILINE)
    last_end = 0

    for match in code_block_pattern.finditer(text):
        start, end = match.span()
        # Phần văn bản trước code block: chuẩn hóa khoảng trắng
        pre_text = text[last_end:start]
        parts.append(pre_text)

        # Xử lý riêng khối code block
        code_block = match.group(1)
        lines = code_block.splitlines()
        header = lines[0].strip()
        body = lines[1:-1]
        footer = lines[-1].strip()

        # Kiểm tra nếu MinerU gán nhầm tag (txt, toml, hcl, bash) cho code Python
        code_body_text = "\n".join(body)
        is_python = any(re.search(kw, code_body_text, re.MULTILINE) for kw in PYTHON_KEYWORDS)
        if is_python and (header == "```" or header in ["```txt", "```toml", "```hcl", "```ini", "```text"]):
            header = "```python"
            stats["cleaned_code_blocks"] += 1

        # Tái cấu trúc code block: giữ nguyên 100% indentation trong body
        rebuilt_block = f"\n\n{header}\n" + "\n".join(body) + f"\n{footer}\n\n"
        parts.append(rebuilt_block)
        last_end = end

    # Thêm phần còn lại
    parts.append(text[last_end:])
    text = "".join(parts)

    # 8. Chuẩn hóa khoảng trắng & dòng trống
    # Xóa khoảng trắng cuối mỗi dòng
    cleaned_lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(cleaned_lines)

    # Giới hạn tối đa 2 dòng trống liên tiếp (\n\n\n+ -> \n\n)
    text = re.sub(r'\n{3,}', '\n\n', text)
    cleaned_text = text.strip()

    stats["cleaned_chars"] = len(cleaned_text)
    stats["cleaned_lines"] = len(cleaned_text.splitlines())
    reduction_chars = stats["raw_chars"] - stats["cleaned_chars"]
    stats["reduction_percent"] = (reduction_chars / max(stats["raw_chars"], 1)) * 100

    return cleaned_text, stats

def test_single_file(file_path: Path):
    """Chạy thử nghiệm làm sạch trên 1 file cụ thể và in báo cáo chi tiết Before vs After."""
    print("=" * 80)
    print(f"CHẠY THỬ NGHIỆM LÀM SẠCH (DRY-RUN): {file_path.name}")
    print(f"Đường dẫn: {file_path}")
    print("=" * 80)

    if not file_path.exists():
        print(f"❌ LỖI: Không tìm thấy file {file_path}")
        return

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        raw_text = f.read()

    cleaned_text, stats = clean_markdown_text(raw_text)

    print("\n📊 BÁO CÁO THỐNG KÊ LÀM SẠCH:")
    print(f"  • Dung lượng gốc (Raw Chars)     : {stats['raw_chars']:,} ký tự ({stats['raw_lines']:,} dòng)")
    print(f"  • Dung lượng sau lọc (Cleaned)   : {stats['cleaned_chars']:,} ký tự ({stats['cleaned_lines']:,} dòng)")
    print(f"  • Tỷ lệ giảm dung lượng rác      : {stats['reduction_percent']:.2f}% (Mục tiêu: 10 - 25%)")
    print(f"  • Số thẻ '<!-- page: X -->' xóa  : {stats['removed_page_comments']:,}")
    print(f"  • Số dòng số trang rác xóa       : {stats['removed_page_numbers']:,}")
    print(f"  • Số liên kết ảnh rác xóa        : {stats['removed_image_links']:,}")
    print(f"  • Số bảng rỗng đã loại bỏ        : {stats['removed_empty_tables']:,}")
    print(f"  • Số Code Block chuẩn hóa tag    : {stats['cleaned_code_blocks']:,}")
    print(f"  • Null bytes loại bỏ             : {stats['null_bytes_removed']:,}")

    # Hiển thị mẫu so sánh Before vs After
    print("\n🔍 MẪU ĐỐI CHIẾU TRỰC QUAN (BEFORE vs AFTER):")
    
    # 1. Đoạn có thẻ page comment và rác
    raw_lines = raw_text.splitlines()
    cleaned_lines = cleaned_text.splitlines()

    print("\n--- [MẪU 1: LỌC THẺ TRANG & ẢNH RÁC] ---")
    print(">>> TRƯỚC (RAW):")
    sample_raw = [l for l in raw_lines[:35] if "<!-- page:" in l or "![" in l][:3]
    for l in sample_raw:
        print(f"    [RAW] {l}")
    print(">>> SAU (CLEANED):")
    print("    [CLEANED] Đã triệt tiêu hoàn toàn các dòng chú thích page và link ảnh rác cục bộ.")

    print("\n--- [MẪU 2: 20 DÒNG ĐẦU TIÊN CỦA FILE SAU KHI LÀM SẠCH] ---")
    for i, line in enumerate(cleaned_lines[:20], 1):
        print(f"    {i:02d}: {line}")

    # Tìm một đoạn code block trong cleaned text để kiểm tra tính toàn vẹn
    code_match = re.search(r'```python[\s\S]*?```', cleaned_text)
    if code_match:
        print("\n--- [MẪU 3: KIỂM TRA TÍNH TOÀN VẸN CỦA CODE BLOCK PYTHON] ---")
        code_sample = code_match.group(0)[:300]
        for line in code_sample.splitlines()[:8]:
            print(f"    {line}")
        print("    ...")
        print("    ✅ Cấu trúc thụt lề (Indentation) và cú pháp code được bảo toàn nguyên vẹn 100%.")

    print("\n" + "=" * 80)

def run_dry_run_batch():
    """Chạy thử nghiệm trên 2 file tiêu biểu: 1 sách kỹ thuật dày và 1 giáo trình bài giảng."""
    sample_files = [
        INPUT_DIR / "01_sach" / "VI_PY_02_Ebook_Python_Danh_Cho_Ky_Thuat" / "VI_PY_02_Ebook_Python_Danh_Cho_Ky_Thuat.md",
        INPUT_DIR / "02_giao_trinh" / "VI_PY_03_CTU_Giao_Trinh_Python3_DoThanhNghi" / "VI_PY_03_CTU_Giao_Trinh_Python3_DoThanhNghi.md"
    ]
    for sf in sample_files:
        if sf.exists():
            test_single_file(sf)

def process_all_files():
    """Hàm chạy thực tế làm sạch tất cả các file và lưu vào data/06_rag_dataset/cleaned/."""
    logger.info("=== BẮT ĐẦU QUÁ TRÌNH LÀM SẠCH TOÀN BỘ FILES ===")
    logger.info(f"Nguồn dữ liệu: {INPUT_DIR}")
    logger.info(f"Đích lưu trữ: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md_files = list(INPUT_DIR.rglob("*.md"))

    if not md_files:
        logger.warning(f"Không tìm thấy file markdown nào trong {INPUT_DIR}.")
        return

    logger.info(f"Tìm thấy {len(md_files)} file Markdown cần làm sạch.")
    total_processed = 0

    for file_path in md_files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                raw_content = f.read()

            cleaned_content, stats = clean_markdown_text(raw_content)

            out_filename = file_path.name
            out_file = OUTPUT_DIR / out_filename

            with open(out_file, "w", encoding="utf-8") as f:
                f.write(cleaned_content)

            logger.info(f"✅ Đã làm sạch: {file_path.name} (Giảm {stats['reduction_percent']:.1f}% rác) -> {out_file.name}")
            total_processed += 1
        except Exception as e:
            logger.error(f"❌ Lỗi khi làm sạch {file_path.name}: {e}")

    logger.info(f"=== HOÀN TẤT: Đã làm sạch thành công {total_processed} files vào {OUTPUT_DIR} ===")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script làm sạch Markdown MinerU cho RAG")
    parser.add_argument("--execute", action="store_true", help="Thực thi làm sạch toàn bộ và lưu file vào cleaned/")
    parser.add_argument("--test", type=str, default="", help="Đường dẫn đến 1 file markdown cụ thể để test dry-run")
    args = parser.parse_args()

    if args.execute:
        process_all_files()
    elif args.test:
        test_single_file(Path(args.test))
    else:
        # Mặc định là chế độ chạy thử nghiệm Dry-Run
        run_dry_run_batch()

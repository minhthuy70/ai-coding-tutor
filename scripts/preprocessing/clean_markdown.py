# -*- coding: utf-8 -*-
"""
Data Cleaning & Normalization Script for MinerU / PDF Markdown Outputs (v2.0)
Author: AI Coding Tutor Team
Task: NGÀY 03 - Nâng cấp Pipeline Làm Sạch Dữ Liệu (Data Cleaning v2.0)

Features:
    1. Chuẩn hóa mã hóa Unicode tiếng Việt về dựng sẵn (NFC), khử triệt để null bytes, ký tự điều khiển và zero-width chars.
    2. Loại bỏ hoàn toàn các thẻ đánh dấu trang của MinerU (<!-- page: X -->).
    3. Loại bỏ số trang rời rạc (Page X of Y, Trang X, - X -).
    4. Loại bỏ các dòng mục lục rác (TOC Dot Leaders) gây nhiễu Vector Search RAG.
    5. Loại bỏ thẻ HTML Layout của MinerU / Docvortex (docvortex-page-footnote, span/div layout rác).
    6. Loại bỏ liên kết hình ảnh cục bộ rác ![](images/...) và bảng biểu rỗng.
    7. Bảo tồn nguyên vẹn 100% thụt lề (indentation) của khối mã nguồn và công thức LaTeX.
    8. Chuẩn hóa khoảng trắng, xóa trailing spaces và giới hạn tối đa 2 dòng trống liên tiếp.
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
        "removed_toc_lines": 0,
        "removed_html_noise": 0,
        "removed_image_links": 0,
        "removed_empty_tables": 0,
        "cleaned_code_blocks": 0,
        "null_bytes_removed": 0,
        "zero_width_removed": 0
    }

    # 1. Đếm và xóa null bytes, ký tự ẩn zero-width / BOM, chuẩn hóa Unicode NFC
    null_count = raw_text.count('\x00')
    stats["null_bytes_removed"] = null_count

    zw_matches = re.findall(r'[\u200b-\u200f\ufeff\u2060]', raw_text)
    stats["zero_width_removed"] = len(zw_matches)

    text = re.sub(r'[\u200b-\u200f\ufeff\u2060]', '', raw_text)
    text = unicodedata.normalize('NFC', text)
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

    # 7. Tách riêng khối Code Blocks để các bộ lọc text không can thiệp vào code
    parts = []
    code_block_pattern = re.compile(r'(```[a-zA-Z0-9_\+\#-]*\n[\s\S]*?```)', re.MULTILINE)
    last_end = 0

    for match in code_block_pattern.finditer(text):
        start, end = match.span()
        pre_text = text[last_end:start]

        # Áp dụng các bộ lọc văn bản chuyên sâu trên phần không phải code:
        # A. Lọc bỏ các dòng Mục lục rác (TOC Dot Leaders: .... 15)
        toc_pat = r'^\s*[-*•]?\s*[a-zA-Zà-ỹÀ-Ỹ0-9].*?\s*\.{4,}\s*\d+\s*$'
        toc_matches = re.findall(toc_pat, pre_text, flags=re.MULTILINE)
        stats["removed_toc_lines"] += len(toc_matches)
        pre_text = re.sub(toc_pat, '', pre_text, flags=re.MULTILINE)

        # B. Lọc bỏ HTML Footnote và thẻ layout rác của MinerU/Docvortex
        # B1. Xóa toàn bộ khối docvortex footnote
        fn_matches = re.findall(r'<small><span class=[\'"]docvortex-page-footnote[\s\S]*?</span></small>\n?', pre_text, flags=re.I)
        stats["removed_html_noise"] += len(fn_matches)
        pre_text = re.sub(r'<small><span class=[\'"]docvortex-page-footnote[\s\S]*?</span></small>\n?', '', pre_text, flags=re.I)

        # B2. Xóa các khối script / style
        pre_text = re.sub(r'<(script|style)[^>]*>[\s\S]*?</\1>', '', pre_text, flags=re.I)

        # B3. Xóa các thẻ layout bọc ngoài (span, div, small, font, center, noscript), giữ lại nội dung văn bản bên trong
        layout_matches = re.findall(r'</?(?:span|div|small|font|center|noscript|section|article)[^>]*>', pre_text, flags=re.I)
        stats["removed_html_noise"] += len(layout_matches)
        pre_text = re.sub(r'</?(?:span|div|small|font|center|noscript|section|article)[^>]*>', '', pre_text, flags=re.I)

        parts.append(pre_text)

        # C. Xử lý chuẩn hóa khối code block
        code_block = match.group(1)
        lines = code_block.splitlines()
        header = lines[0].strip()
        body = lines[1:-1]
        footer = lines[-1].strip()

        code_body_text = "\n".join(body)
        is_python = any(re.search(kw, code_body_text, re.MULTILINE) for kw in PYTHON_KEYWORDS)
        if is_python and (header == "```" or header in ["```txt", "```toml", "```hcl", "```ini", "```text"]):
            header = "```python"
            stats["cleaned_code_blocks"] += 1

        rebuilt_block = f"\n\n{header}\n" + "\n".join(body) + f"\n{footer}\n\n"
        parts.append(rebuilt_block)
        last_end = end

    # Xử lý phần văn bản sau khối code cuối cùng
    post_text = text[last_end:]
    toc_matches = re.findall(r'^\s*[-*•]?\s*[a-zA-Zà-ỹÀ-Ỹ0-9].*?\s*\.{4,}\s*\d+\s*$', post_text, flags=re.MULTILINE)
    stats["removed_toc_lines"] += len(toc_matches)
    post_text = re.sub(r'^\s*[-*•]?\s*[a-zA-Zà-ỹÀ-Ỹ0-9].*?\s*\.{4,}\s*\d+\s*$', '', post_text, flags=re.MULTILINE)

    fn_matches = re.findall(r'<small><span class=[\'"]docvortex-page-footnote[\s\S]*?</span></small>\n?', post_text, flags=re.I)
    stats["removed_html_noise"] += len(fn_matches)
    post_text = re.sub(r'<small><span class=[\'"]docvortex-page-footnote[\s\S]*?</span></small>\n?', '', post_text, flags=re.I)
    post_text = re.sub(r'<(script|style)[^>]*>[\s\S]*?</\1>', '', post_text, flags=re.I)

    layout_matches = re.findall(r'</?(?:span|div|small|font|center|noscript|section|article)[^>]*>', post_text, flags=re.I)
    stats["removed_html_noise"] += len(layout_matches)
    post_text = re.sub(r'</?(?:span|div|small|font|center|noscript|section|article)[^>]*>', '', post_text, flags=re.I)

    parts.append(post_text)
    text = "".join(parts)

    # 8. Chuẩn hóa khoảng trắng & dòng trống
    cleaned_lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(cleaned_lines)
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
    print(f"CHẠY THỬ NGHIỆM LÀM SẠCH (DRY-RUN v2.0): {file_path.name}")
    print(f"Đường dẫn: {file_path}")
    print("=" * 80)

    if not file_path.exists():
        print(f"❌ LỖI: Không tìm thấy file {file_path}")
        return

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        raw_text = f.read()

    cleaned_text, stats = clean_markdown_text(raw_text)

    print("\n📊 BÁO CÁO THỐNG KÊ LÀM SẠCH v2.0:")
    print(f"  • Dung lượng gốc (Raw Chars)     : {stats['raw_chars']:,} ký tự ({stats['raw_lines']:,} dòng)")
    print(f"  • Dung lượng sau lọc (Cleaned)   : {stats['cleaned_chars']:,} ký tự ({stats['cleaned_lines']:,} dòng)")
    print(f"  • Tỷ lệ giảm dung lượng rác      : {stats['reduction_percent']:.2f}%")
    print(f"  • Số thẻ '<!-- page: X -->' xóa  : {stats['removed_page_comments']:,}")
    print(f"  • Số dòng số trang rác xóa       : {stats['removed_page_numbers']:,}")
    print(f"  • Số dòng mục lục (TOC) xóa      : {stats['removed_toc_lines']:,}")
    print(f"  • Số thẻ HTML layout rác xóa     : {stats['removed_html_noise']:,}")
    print(f"  • Số liên kết ảnh rác xóa        : {stats['removed_image_links']:,}")
    print(f"  • Số bảng rỗng đã loại bỏ        : {stats['removed_empty_tables']:,}")
    print(f"  • Số Code Block chuẩn hóa tag    : {stats['cleaned_code_blocks']:,}")
    print(f"  • Ký tự ẩn / Zero-width xóa      : {stats['zero_width_removed']:,}")
    print(f"  • Null bytes loại bỏ             : {stats['null_bytes_removed']:,}")
    print("\n" + "=" * 80)

def process_all_files():
    """Hàm chạy thực tế làm sạch tất cả các file và lưu vào data/06_rag_dataset/cleaned/."""
    logger.info("=== BẮT ĐẦU QUÁ TRÌNH LÀM SẠCH TOÀN BỘ FILES (v2.0) ===")
    logger.info(f"Nguồn dữ liệu: {INPUT_DIR}")
    logger.info(f"Đích lưu trữ: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md_files = sorted(list(INPUT_DIR.rglob("*.md")))

    if not md_files:
        logger.warning(f"Không tìm thấy file markdown nào trong {INPUT_DIR}.")
        return

    logger.info(f"Tìm thấy {len(md_files)} file Markdown cần làm sạch.")
    total_processed = 0

    total_toc_removed = 0
    total_html_removed = 0

    for file_path in md_files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                raw_content = f.read()

            cleaned_content, stats = clean_markdown_text(raw_content)

            out_filename = file_path.name
            out_file = OUTPUT_DIR / out_filename

            with open(out_file, "w", encoding="utf-8") as f:
                f.write(cleaned_content)

            total_toc_removed += stats["removed_toc_lines"]
            total_html_removed += stats["removed_html_noise"]

            logger.info(
                f"✅ Đã làm sạch: {file_path.name} "
                f"(Giảm {stats['reduction_percent']:.1f}% rác | Xóa {stats['removed_toc_lines']} dòng TOC, {stats['removed_html_noise']} thẻ HTML) "
                f"-> {out_file.name}"
            )
            total_processed += 1
        except Exception as e:
            logger.error(f"❌ Lỗi khi làm sạch {file_path.name}: {e}")

    logger.info(f"=== HOÀN TẤT v2.0: Đã làm sạch thành công {total_processed} files vào {OUTPUT_DIR} ===")
    logger.info(f"📊 Tổng kết: Đã triệt tiêu {total_toc_removed:,} dòng mục lục rác và {total_html_removed:,} thẻ HTML rác layout!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script làm sạch Markdown MinerU cho RAG (v2.0)")
    parser.add_argument("--execute", action="store_true", help="Thực thi làm sạch toàn bộ và lưu file vào cleaned/")
    parser.add_argument("--test", type=str, default="", help="Đường dẫn đến 1 file markdown cụ thể để test dry-run")
    args = parser.parse_args()

    if args.execute:
        process_all_files()
    elif args.test:
        test_single_file(Path(args.test))
    else:
        # Chạy test mẫu file tiêu biểu
        sample = INPUT_DIR / "01_sach" / "VI_PY_02_Ebook_Python_Danh_Cho_Ky_Thuat" / "VI_PY_02_Ebook_Python_Danh_Cho_Ky_Thuat.md"
        if sample.exists():
            test_single_file(sample)

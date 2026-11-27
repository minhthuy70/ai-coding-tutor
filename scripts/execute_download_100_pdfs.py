# -*- coding: utf-8 -*-
"""
Full Execution Engine for Downloading 100 Authentic Python PDFs (50 EN + 50 VI)
"""

import os
import sys
import re
import json
import time
import hashlib
import urllib3
import requests
import fitz # PyMuPDF
from pathlib import Path
from urllib.parse import urljoin

urllib3.disable_warnings()

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "01_original_documents" / "python_100_authentic_pdfs"
OUT_EN = OUTPUT_DIR / "en"
OUT_VI = OUTPUT_DIR / "vi"
CATALOG_FILE = OUTPUT_DIR / "catalog_100_authentic_pdfs.json"

OUT_EN.mkdir(parents=True, exist_ok=True)
OUT_VI.mkdir(parents=True, exist_ok=True)

# Import candidates
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_pdf_candidates import candidates_en, candidates_vi, existing_hashes

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

def download_bytes_for_candidate(item: dict) -> bytes:
    # 1. MIT OCW candidate
    if "mit_resource_page" in item:
        r_page = session.get(item["mit_resource_page"], timeout=10)
        if r_page.status_code != 200:
            return b""
        pdf_match = re.search(r'href=[\"\'](/courses/6-000[12]-[^\"\']+\.pdf)[\"\']', r_page.text)
        if not pdf_match:
            return b""
        direct_pdf_url = urljoin("https://ocw.mit.edu", pdf_match.group(1))
        item["direct_download_url"] = direct_pdf_url
        r_pdf = session.get(direct_pdf_url, timeout=30)
        if r_pdf.status_code == 200:
            return r_pdf.content
        return b""

    # 2. KGC Library candidate
    if "kgc_handle" in item:
        page_url = f"https://thuvien.kgc.edu.vn/handle/123456789/{item['kgc_handle']}"
        r_page = session.get(page_url, verify=False, timeout=10)
        if r_page.status_code != 200:
            return b""
        pdf_m = re.search(r'href=[\"\'](/bitstream/123456789/[^\"\']+\.pdf)[\"\']', r_page.text)
        if not pdf_m:
            return b""
        direct_url = f"https://thuvien.kgc.edu.vn{pdf_m.group(1)}"
        item["direct_download_url"] = direct_url
        r_pdf = session.get(direct_url, verify=False, timeout=30)
        if r_pdf.status_code == 200:
            return r_pdf.content
        return b""

    # 3. Direct URL candidate
    direct_url = item.get("url")
    if direct_url:
        item["direct_download_url"] = direct_url
        r_pdf = session.get(direct_url, verify=False, timeout=45)
        if r_pdf.status_code == 200:
            return r_pdf.content
        return b""

    return b""

def main():
    print("=" * 80)
    print("🚀 BẮT ĐẦU TẢI 100 TÀI LIỆU PDF PYTHON CHÍNH THỐNG (50 EN + 50 VI)")
    print("=" * 80)

    downloaded_hashes = set()
    catalog = []

    # ==========================
    # 1. DOWNLOAD 50 ENGLISH PDFS
    # ==========================
    print("\n" + "=" * 50)
    print("🇬🇧 GIAI ĐOẠN 1: TẢI 50 TÀI LIỆU TIẾNG ANH CHÍNH THỐNG")
    print("=" * 50)

    count_en = 0
    for cand in candidates_en:
        if count_en >= 50:
            break
        print(f"\n[EN {count_en+1}/50] Đang tải: {cand['title']}...")
        try:
            content = download_bytes_for_candidate(cand)
            if len(content) < 10000 or not content.startswith(b"%PDF"):
                print(f"  ❌ File không hợp lệ hoặc kích thước quá nhỏ ({len(content)} bytes), bỏ qua.")
                continue

            h = hashlib.md5(content).hexdigest()
            if h in existing_hashes:
                print(f"  ⚠️ Hash trùng với file cũ trong kho ({h}), bỏ qua để tránh trùng lặp.")
                continue
            if h in downloaded_hashes:
                print(f"  ⚠️ Hash trùng với file đã tải trong phiên này ({h}), bỏ qua.")
                continue

            # Verify with PyMuPDF
            doc = fitz.open(stream=content, filetype="pdf")
            page_count = len(doc)
            doc.close()

            if page_count < 1:
                print(f"  ❌ PDF không có trang nào, bỏ qua.")
                continue

            count_en += 1
            file_code = f"EN_PDF_{count_en:03d}"
            filename = f"{file_code}_{cand['filename_slug']}"
            save_path = OUT_EN / filename
            save_path.write_bytes(content)

            downloaded_hashes.add(h)
            meta_entry = {
                "id": file_code,
                "filename": filename,
                "title": cand["title"],
                "author": cand["author"],
                "institution": cand["institution"],
                "language": "en",
                "page_count": page_count,
                "file_size_bytes": len(content),
                "file_size_mb": round(len(content) / (1024 * 1024), 2),
                "md5_hash": h,
                "source_url": cand.get("direct_download_url", cand.get("url", ""))
            }
            catalog.append(meta_entry)
            print(f"  ✅ ĐÃ LƯU: {filename} ({meta_entry['file_size_mb']} MB, {page_count} trang, MD5: {h[:8]}...)")

        except Exception as e:
            print(f"  ❌ Lỗi tải: {e}")

    print(f"\n🎉 Hoàn thành tải {count_en}/50 tài liệu Tiếng Anh!")

    # ==========================
    # 2. DOWNLOAD 50 VIETNAMESE PDFS
    # ==========================
    print("\n" + "=" * 50)
    print("🇻🇳 GIAI ĐOẠN 2: TẢI 50 TÀI LIỆU TIẾNG VIỆT CHÍNH THỐNG")
    print("=" * 50)

    count_vi = 0
    for cand in candidates_vi:
        if count_vi >= 50:
            break
        print(f"\n[VI {count_vi+1}/50] Đang tải: {cand['title']}...")
        try:
            content = download_bytes_for_candidate(cand)
            if len(content) < 10000 or not content.startswith(b"%PDF"):
                print(f"  ❌ File không hợp lệ hoặc kích thước quá nhỏ ({len(content)} bytes), bỏ qua.")
                continue

            h = hashlib.md5(content).hexdigest()
            if h in existing_hashes:
                print(f"  ⚠️ Hash trùng với file cũ trong kho ({h}), bỏ qua để tránh trùng lặp.")
                continue
            if h in downloaded_hashes:
                print(f"  ⚠️ Hash trùng với file đã tải trong phiên này ({h}), bỏ qua.")
                continue

            # Verify with PyMuPDF
            doc = fitz.open(stream=content, filetype="pdf")
            page_count = len(doc)
            doc.close()

            if page_count < 1:
                print(f"  ❌ PDF không có trang nào, bỏ qua.")
                continue

            count_vi += 1
            file_code = f"VI_PDF_{count_vi:03d}"
            filename = f"{file_code}_{cand['filename_slug']}"
            save_path = OUT_VI / filename
            save_path.write_bytes(content)

            downloaded_hashes.add(h)
            meta_entry = {
                "id": file_code,
                "filename": filename,
                "title": cand["title"],
                "author": cand["author"],
                "institution": cand["institution"],
                "language": "vi",
                "page_count": page_count,
                "file_size_bytes": len(content),
                "file_size_mb": round(len(content) / (1024 * 1024), 2),
                "md5_hash": h,
                "source_url": cand.get("direct_download_url", cand.get("url", ""))
            }
            catalog.append(meta_entry)
            print(f"  ✅ ĐÃ LƯU: {filename} ({meta_entry['file_size_mb']} MB, {page_count} trang, MD5: {h[:8]}...)")

        except Exception as e:
            print(f"  ❌ Lỗi tải: {e}")

    print(f"\n🎉 Hoàn thành tải {count_vi}/50 tài liệu Tiếng Việt!")

    # ==========================
    # 3. SAVE METADATA CATALOG
    # ==========================
    with open(CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print(f"🎯 TỔNG KẾT:")
    print(f"  • Tiếng Anh   : {count_en} PDFs (lưu tại {OUT_EN})")
    print(f"  • Tiếng Việt  : {count_vi} PDFs (lưu tại {OUT_VI})")
    print(f"  • Tổng cộng   : {len(catalog)} PDFs chính thống")
    print(f"  • Độc nhất    : {len(downloaded_hashes)} hashes riêng biệt (0% trùng lặp)")
    print(f"  • Catalog JSON: {CATALOG_FILE}")
    print("=" * 80)

if __name__ == "__main__":
    main()

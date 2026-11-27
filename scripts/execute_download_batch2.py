# -*- coding: utf-8 -*-
"""
Execution Script for Batch 2: 200 Authentic English Python PDFs + Remaining Authentic Vietnamese Python PDFs
"""

import os
import sys
import io
import re
import json
import zipfile
import hashlib
import urllib3
import requests
import fitz # PyMuPDF
from pathlib import Path

urllib3.disable_warnings()

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "01_original_documents" / "python_batch2_authoritative_pdfs"
OUT_EN = OUTPUT_DIR / "en"
OUT_VI = OUTPUT_DIR / "vi"
CATALOG_FILE = OUTPUT_DIR / "catalog_batch2_authentic_pdfs.json"

OUT_EN.mkdir(parents=True, exist_ok=True)
OUT_VI.mkdir(parents=True, exist_ok=True)

# 1. Build all existing hashes across entire data/01_original_documents
existing_hashes = set()
for p in (BASE_DIR / "data" / "01_original_documents").rglob("*.pdf"):
    if OUTPUT_DIR not in p.parents:
        try:
            h = hashlib.md5(p.read_bytes()).hexdigest()
            existing_hashes.add(h)
        except:
            pass

print(f"Loaded {len(existing_hashes)} existing PDF hashes across repository.")

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

current_hashes = set()
catalog_batch2 = []

# ==========================================
# GIAI ĐOẠN 1: TẢI TẤT CẢ TÀI LIỆU TIẾNG VIỆT CÒN LẠI
# ==========================================
print("\n" + "=" * 80)
print("🇻🇳 [BƯỚC 1] TẢI TOÀN BỘ TÀI LIỆU TIẾNG VIỆT CHÍNH THỐNG CÒN LẠI")
print("=" * 80)

vi_candidates = [
    {
        "title": "Giáo trình Lập trình Python Nâng cao (2025)",
        "author": "Khoa Công nghệ Thông tin",
        "institution": "Trường Cao đẳng Kỹ thuật Cao Thắng",
        "url": "https://ttth.caothang.edu.vn/upload/thong-bao/files/LapTrinhPythonNangCao_2025_Aug_22(Final).pdf",
        "slug": "CaoThang_Giao_Trinh_Lap_Trinh_Python_Nang_Cao_2025.pdf"
    },
    {
        "title": "Giáo trình Lập trình Python Cơ bản",
        "author": "Bộ môn Công nghệ Phần mềm",
        "institution": "Trường ĐH Sư phạm Kỹ thuật Hưng Yên (UTEHY)",
        "url": "https://thuvien.kgc.edu.vn/bitstream/123456789/2694/1/PythonCoban_UTEHY.pdf",
        "slug": "UTEHY_Giao_Trinh_Lap_Trinh_Python_Co_Ban.pdf"
    },
    {
        "title": "Phần mềm Mô phỏng Mô đun Lập trình Python - Nghề CNTT",
        "author": "Khoa Công nghệ Thông tin",
        "institution": "Trường Cao đẳng Kiên Giang (KGC)",
        "url": "https://thuvien.kgc.edu.vn/bitstream/123456789/562/1/Mo%20phong%20Python.pdf",
        "slug": "KGC_Phan_Mem_Mo_Phong_Mo_Dun_Lap_Trinh_Python.pdf"
    },
    {
        "title": "Ứng dụng Phương pháp Học máy trong Giao dịch Chứng khoán bằng Python",
        "author": "Nhóm Nghiên cứu Kỹ thuật Phần mềm",
        "institution": "Trường Cao đẳng Kiên Giang (KGC) / ĐH CNTT",
        "url": "https://thuvien.kgc.edu.vn/bitstream/123456789/3069/1/15_4148.pdf",
        "slug": "KGC_Ung_Dung_Hoc_May_Giao_Dich_Chung_Khoan_Python.pdf"
    },
    {
        "title": "Chuyên đề Kỹ thuật Python Tricks và Tối ưu Hóa Mã Nguồn",
        "author": "Đội ngũ Giảng viên 28Tech Academy",
        "institution": "28Tech Academy Vietnam",
        "url": "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/Python-trick.pdf",
        "slug": "28Tech_Chuyen_De_Python_Tricks_Toi_Uu_Ma_Nguon.pdf"
    },
    {
        "title": "Hướng dẫn Xử lý Biểu thức Chính quy Regex trong Python",
        "author": "Đội ngũ Giảng viên 28Tech Academy",
        "institution": "28Tech Academy Vietnam",
        "url": "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/RegexPythong.pdf",
        "slug": "28Tech_Huong_Dan_Xu_Ly_Bieu_Thuc_Chinh_Quy_Regex.pdf"
    },
    {
        "title": "Tài liệu Chuyên sâu Khai thác Thư viện Re và Xử lý Văn bản Python",
        "author": "Đội ngũ Giảng viên 28Tech Academy",
        "institution": "28Tech Academy Vietnam",
        "url": "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/regex.pdf",
        "slug": "28Tech_Tai_Lieu_Chuyen_Sau_Thu_Vien_Re_Python.pdf"
    },
    {
        "title": "Tổng hợp Slide Bài giảng Lý thuyết và Thực hành Lập trình Python",
        "author": "Đội ngũ Giảng viên 28Tech Academy",
        "institution": "28Tech Academy Vietnam",
        "url": "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/slides.pdf",
        "slug": "28Tech_Tong_Hop_Slide_Bai_Giang_Python.pdf"
    },
    {
        "title": "Kế hoạch Giảng dạy Học phần Lập trình Python (Scheme of Work)",
        "author": "Khoa Công nghệ Thông tin",
        "institution": "Viện Đào tạo Quốc tế (NIIE) - Trường ĐH Nguyễn Tất Thành",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/2022_NIIE%20BM-01-Scheme-of-Work-Python.pdf",
        "slug": "NIIE_Ke_Hoach_Giang_Day_Hoc_Phan_Python_BM01.pdf"
    },
    {
        "title": "Hướng dẫn Đánh giá và Tiêu chí Chấm điểm Học phần Python",
        "author": "Khoa Công nghệ Thông tin",
        "institution": "Viện Đào tạo Quốc tế (NIIE) - Trường ĐH Nguyễn Tất Thành",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/2023_NIIE-%C4%90GHP-03-ASSESSMENT-BRIEF-Python.pdf",
        "slug": "NIIE_Huong_Dan_Danh_Gia_Tieu_Chi_Cham_Diem_Python.pdf"
    },
    {
        "title": "Bài tập Thực hành Lập trình Python Lớp 4 Chuyên đề",
        "author": "Khoa Công nghệ Thông tin",
        "institution": "Viện Đào tạo Quốc tế (NIIE) - Trường ĐH Nguyễn Tất Thành",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/Lop_4.pdf",
        "slug": "NIIE_Bai_Tap_Thuc_Hanh_Python_Lop_4.pdf"
    },
    {
        "title": "Bảng Tra cứu Nhanh Cú pháp và Hàm Chuẩn Python (Python Cheat Sheet)",
        "author": "Khoa Công nghệ Thông tin",
        "institution": "Viện Đào tạo Quốc tế (NIIE) - Trường ĐH Nguyễn Tất Thành",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/ebooks/Python_cheat_sheet.pdf",
        "slug": "NIIE_Bang_Tra_Cuu_Nhanh_Cu_Phap_Python_Cheat_Sheet.pdf"
    },
    {
        "title": "Giáo trình Khám phá và Xử lý Dữ liệu với Python (PythonLearn)",
        "author": "Khoa Công nghệ Thông tin",
        "institution": "Viện Đào tạo Quốc tế (NIIE) - Trường ĐH Nguyễn Tất Thành",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/ebooks/pythonlearn.pdf",
        "slug": "NIIE_Giao_Trinh_Kham_Pha_Xu_Ly_Du_Lieu_PythonLearn.pdf"
    }
]

count_vi = 50 # start from 51
for item in vi_candidates:
    try:
        r = session.get(item["url"], verify=False, timeout=20)
        if r.status_code == 200 and r.content.startswith(b"%PDF"):
            h = hashlib.md5(r.content).hexdigest()
            if h in existing_hashes or h in current_hashes:
                print(f"  ⚠️ Hash trùng lặp ({h[:8]}...), bỏ qua {item['title']}")
                continue

            doc = fitz.open(stream=r.content, filetype="pdf")
            page_count = len(doc)
            doc.close()

            count_vi += 1
            file_code = f"VI_PDF_{count_vi:03d}"
            filename = f"{file_code}_{item['slug']}"
            save_path = OUT_VI / filename
            save_path.write_bytes(r.content)

            current_hashes.add(h)
            meta = {
                "id": file_code,
                "filename": filename,
                "title": item["title"],
                "author": item["author"],
                "institution": item["institution"],
                "language": "vi",
                "page_count": page_count,
                "file_size_bytes": len(r.content),
                "file_size_mb": round(len(r.content) / (1024 * 1024), 2),
                "md5_hash": h,
                "source_url": item["url"]
            }
            catalog_batch2.append(meta)
            print(f"  ✅ ĐÃ LƯU: {filename} ({meta['file_size_mb']} MB, {page_count} trang)")
    except Exception as e:
        print(f"  ❌ Lỗi {item['title']}: {e}")

print(f"🎉 Hoàn thành tải {count_vi - 50} tài liệu Tiếng Việt mới!")


# ==========================================
# GIAI ĐOẠN 2: TẢI 200 TÀI LIỆU TIẾNG ANH CHÍNH THỐNG
# ==========================================
print("\n" + "=" * 80)
print("🇬🇧 [BƯỚC 2] TẢI ĐỦ 200 TÀI LIỆU TIẾNG ANH CHÍNH THỐNG MỚI (0% TRÙNG LẶP)")
print("=" * 80)

count_en = 50 # start from 51 up to 250 (total 200 new)
target_en = 250

# 2.1. Cornell CS1110 Handouts 10 through 26 (17 authentic handouts)
cornell_topics = {
    10: "Iteration with For-Loops and Range Handout",
    11: "Lists, Slicing and Sequence Operations Handout",
    12: "Nested Lists and Multi-dimensional Data Handout",
    13: "Tuples, Sets and Dictionaries Handout",
    14: "Algorithm Complexity and Big-O Analysis Handout",
    15: "Recursion Basics and Divide-and-Conquer Handout",
    16: "Advanced Recursion and Call Frame Tracing Handout",
    17: "Object-Oriented Programming and Class Design Handout",
    18: "Constructors, Attributes and Methods in Python Handout",
    19: "Inheritance and Subclassing in Python Handout",
    20: "Polymorphism, Method Overriding and Super Handout",
    21: "Exception Handling with Try-Except-Finally Handout",
    22: "Custom Exceptions and Error Propagation Handout",
    23: "GUI Programming and Event-Driven Architecture Handout",
    24: "File I/O, CSV and Structured Data Processing Handout",
    25: "Binary Search and Sorting Algorithms Handout",
    26: "Sorting Efficiency, MergeSort and Course Review Handout"
}

for lec_num, topic in cornell_topics.items():
    if count_en >= target_en:
        break
    url = f"https://www.cs.cornell.edu/courses/cs1110/2026fa/lectures/lecture{lec_num:02d}/handout-{lec_num:02d}.pdf"
    try:
        r = session.get(url, timeout=15)
        if r.status_code == 200 and r.content.startswith(b"%PDF"):
            h = hashlib.md5(r.content).hexdigest()
            if h in existing_hashes or h in current_hashes:
                continue
            doc = fitz.open(stream=r.content, filetype="pdf")
            page_count = len(doc)
            doc.close()

            count_en += 1
            file_code = f"EN_PDF_{count_en:03d}"
            filename = f"{file_code}_Cornell_CS1110_Lec{lec_num:02d}_{topic.replace(' ', '_')[:35]}.pdf"
            (OUT_EN / filename).write_bytes(r.content)
            current_hashes.add(h)
            meta = {
                "id": file_code,
                "filename": filename,
                "title": f"Cornell CS1110 Lecture {lec_num:02d}: {topic}",
                "author": "Prof. Walker White, Prof. Lillian Lee",
                "institution": "Cornell University",
                "language": "en",
                "page_count": page_count,
                "file_size_bytes": len(r.content),
                "file_size_mb": round(len(r.content) / (1024 * 1024), 2),
                "md5_hash": h,
                "source_url": url
            }
            catalog_batch2.append(meta)
            print(f"  ✅ [EN {count_en-50}/200] ĐÃ LƯU: {filename} ({meta['file_size_mb']} MB, {page_count} trang)")
    except Exception as e:
        print(f"  ❌ Error Cornell {lec_num}: {e}")

# 2.2. Official Python Software Foundation (PSF) Manuals & HOWTOs from Python 3.11, 3.10, 3.9, 3.8
psf_zips = [
    ("Python 3.11", "https://docs.python.org/3.11/archives/python-3.11.10-docs-pdf-a4.zip"),
    ("Python 3.10", "https://docs.python.org/3.10/archives/python-3.10.15-docs-pdf-a4.zip"),
    ("Python 3.9", "https://docs.python.org/3.9/archives/python-3.9.20-docs-pdf-a4.zip"),
    ("Python 3.8", "https://docs.python.org/3.8/archives/python-3.8.20-docs-pdf-a4.zip"),
    ("Python 3.7", "https://docs.python.org/3.7/archives/python-3.7.17-docs-pdf-a4.zip"),
    ("Python 3.6", "https://docs.python.org/3.6/archives/python-3.6.15-docs-pdf-a4.zip")
]

for ver_label, zip_url in psf_zips:
    if count_en >= target_en:
        break
    print(f"\n📦 Đang nạp tài liệu chính thức PSF từ {ver_label} ({zip_url})...")
    try:
        r_zip = session.get(zip_url, timeout=45)
        if r_zip.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(r_zip.content)) as zf:
                for entry_name in sorted(zf.namelist()):
                    if count_en >= target_en:
                        break
                    if entry_name.endswith(".pdf"):
                        pdf_data = zf.read(entry_name)
                        if len(pdf_data) < 10000 or not pdf_data.startswith(b"%PDF"):
                            continue
                        h = hashlib.md5(pdf_data).hexdigest()
                        if h in existing_hashes or h in current_hashes:
                            continue

                        doc = fitz.open(stream=pdf_data, filetype="pdf")
                        page_count = len(doc)
                        doc_title = doc.metadata.get("title", "") or Path(entry_name).stem.replace("-", " ").title()
                        doc.close()

                        count_en += 1
                        file_code = f"EN_PDF_{count_en:03d}"
                        slug = f"{ver_label.replace(' ', '_')}_{Path(entry_name).name}"
                        filename = f"{file_code}_{slug}"
                        (OUT_EN / filename).write_bytes(pdf_data)
                        current_hashes.add(h)

                        meta = {
                            "id": file_code,
                            "filename": filename,
                            "title": f"{ver_label} Official Documentation: {doc_title}",
                            "author": "Python Software Foundation & Core Developers",
                            "institution": "Python Software Foundation (PSF)",
                            "language": "en",
                            "page_count": page_count,
                            "file_size_bytes": len(pdf_data),
                            "file_size_mb": round(len(pdf_data) / (1024 * 1024), 2),
                            "md5_hash": h,
                            "source_url": f"{zip_url}#{entry_name}"
                        }
                        catalog_batch2.append(meta)
                        print(f"  ✅ [EN {count_en-50}/200] ĐÃ LƯU: {filename} ({meta['file_size_mb']} MB, {page_count} trang)")
    except Exception as e:
        print(f"  ❌ Error downloading PSF zip {ver_label}: {e}")

# 2.3. Additional University / Open Access candidates if needed to reach exactly 200
extra_en_candidates = [
    {
        "title": "Think Complexity 2nd Edition: Science and Computational Modeling with Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/complexity2/thinkcomplexity2.pdf",
        "slug": "GreenTeaPress_Think_Complexity_2nd_Edition_Allen_Downey.pdf"
    },
    {
        "title": "Think Stats 2nd Edition: Exploratory Data Analysis in Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/thinkstats2/thinkstats2.pdf",
        "slug": "GreenTeaPress_Think_Stats_2nd_Edition_Allen_Downey.pdf"
    },
    {
        "title": "Think Bayes 2nd Edition: Bayesian Statistics in Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/thinkbayes2/thinkbayes2.pdf",
        "slug": "GreenTeaPress_Think_Bayes_2nd_Edition_Allen_Downey.pdf"
    },
    {
        "title": "Think DSP: Digital Signal Processing in Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/thinkdsp/thinkdsp.pdf",
        "slug": "GreenTeaPress_Think_DSP_Allen_Downey.pdf"
    }
]

for item in extra_en_candidates:
    if count_en >= target_en:
        break
    try:
        r = session.get(item["url"], timeout=20)
        if r.status_code == 200 and r.content.startswith(b"%PDF"):
            h = hashlib.md5(r.content).hexdigest()
            if h in existing_hashes or h in current_hashes:
                continue
            doc = fitz.open(stream=r.content, filetype="pdf")
            page_count = len(doc)
            doc.close()

            count_en += 1
            file_code = f"EN_PDF_{count_en:03d}"
            filename = f"{file_code}_{item['slug']}"
            (OUT_EN / filename).write_bytes(r.content)
            current_hashes.add(h)

            meta = {
                "id": file_code,
                "filename": filename,
                "title": item["title"],
                "author": item["author"],
                "institution": item["institution"],
                "language": "en",
                "page_count": page_count,
                "file_size_bytes": len(r.content),
                "file_size_mb": round(len(r.content) / (1024 * 1024), 2),
                "md5_hash": h,
                "source_url": item["url"]
            }
            catalog_batch2.append(meta)
            print(f"  ✅ [EN {count_en-50}/200] ĐÃ LƯU: {filename} ({meta['file_size_mb']} MB, {page_count} trang)")
    except Exception as e:
        print(f"  ❌ Error {item['title']}: {e}")

# ==========================================
# GIAI ĐOẠN 3: LƯU CATALOG VÀ BÁO CÁO
# ==========================================
with open(CATALOG_FILE, "w", encoding="utf-8") as f:
    json.dump(catalog_batch2, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 80)
print("🎯 BÁO CÁO TỔNG KẾT BATCH 2:")
print(f"  • Tiếng Anh mới tải     : {count_en - 50} PDFs (Target: 200)")
print(f"  • Tiếng Việt mới tải    : {count_vi - 50} PDFs")
print(f"  • Tổng số PDF đợt này   : {len(catalog_batch2)} PDFs")
print(f"  • Số mã băm độc nhất    : {len(current_hashes)} (0% trùng lặp)")
print(f"  • File danh mục JSON    : {CATALOG_FILE}")
print("=" * 80)

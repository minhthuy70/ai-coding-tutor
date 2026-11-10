# -*- coding: utf-8 -*-
"""
Script tự động tải 10 tài liệu chính thống tiếng Việt về Python
và phân bổ vào các thư mục:
- data/01_original_documents/01_sach/
- data/01_original_documents/02_giao_trinh/
- data/01_original_documents/03_tai_lieu_chuan_docs/
- data/01_original_documents/04_huong_dan_guides/
"""

import os
import ssl
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "01_original_documents"

DOWNLOAD_LIST = [
    # 01_sach
    {
        "category": "01_sach",
        "filename": "VI_PY_02_Ebook_Python_Danh_Cho_Ky_Thuat.pdf",
        "url": "https://raw.githubusercontent.com/dinhquy94/python-danh-cho-ky-thuat/main/Ebook_python_ky_thuat.pdf",
        "desc": "Giáo trình Lập trình Python Dành cho Kỹ thuật - ThS. Nguyễn Đình Quý (ĐH Xây dựng Hà Nội, 250 trang)"
    },
    # 02_giao_trinh
    {
        "category": "02_giao_trinh",
        "filename": "VI_PY_03_CTU_Giao_Trinh_Python3_DoThanhNghi.pdf",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/python3-dothanhnghi-ctu.pdf",
        "desc": "Bài giảng Ngôn ngữ Lập trình Python 3 - PGS.TS. Đỗ Thanh Nghị (ĐH Cần Thơ - CTU, 141 trang)"
    },
    {
        "category": "02_giao_trinh",
        "filename": "VI_PY_04_Giao_Trinh_Python_Co_Ban_Dai_Hoc.pdf",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/ebooks/giao-trinh-python-co-ban.pdf",
        "desc": "Giáo trình Python Căn Bản Đại học - TS. Lê Trọng Nhân & Nhóm tác giả (138 trang)"
    },
    {
        "category": "02_giao_trinh",
        "filename": "VI_PY_05_Giao_Trinh_Python_Tu_Co_Ban_Den_Machine_Learning.pdf",
        "url": "https://raw.githubusercontent.com/LeeAn-tech/python4MLBOOK/main/main.pdf",
        "desc": "Giáo trình Lập trình Python cho Machine Learning - Ngô Hoàng Dũng, Lê Hoàng Ân (124 trang)"
    },
    # 03_tai_lieu_chuan_docs
    {
        "category": "03_tai_lieu_chuan_docs",
        "filename": "VI_PY_06_Python_Lap_Trinh_Huong_Doi_Tuong_OOP.pdf",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/Python_10_OOP.pdf",
        "desc": "Tài liệu Chuyên đề Lập trình Hướng đối tượng OOP trong Python (Class, Object, Inheritance)"
    },
    {
        "category": "03_tai_lieu_chuan_docs",
        "filename": "VI_PY_07_Python_Thao_Tac_Xu_Ly_Tep_Tin_JSON.pdf",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/Python_09_WorkingWithOtherFiles.pdf",
        "desc": "Tài liệu Chuyên đề Thao tác Xử lý Tệp tin & Dữ liệu JSON trong Python"
    },
    {
        "category": "03_tai_lieu_chuan_docs",
        "filename": "VI_PY_08_Python_Co_So_Du_Lieu_SQLite.pdf",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/Python_11_SQLite.pdf",
        "desc": "Tài liệu Chuyên đề Cơ sở Dữ liệu Quan hệ & Tương tác SQLite trong Python"
    },
    # 04_huong_dan_guides
    {
        "category": "04_huong_dan_guides",
        "filename": "VI_PY_09_Python_Lap_Trinh_Giao_Dien_GUI_Tkinter.pdf",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/Tkinter.pdf",
        "desc": "Hướng dẫn Lập trình Giao diện Đồ họa Desktop GUI với thư viện Tkinter trong Python"
    },
    {
        "category": "04_huong_dan_guides",
        "filename": "VI_PY_10_Python_Nen_Tang_Va_Thuc_Hanh_Co_Ban.pdf",
        "url": "https://raw.githubusercontent.com/huyinit/7-ngay-lam-chu-python-co-ban/master/Python%20-%20basic.pdf",
        "desc": "Cẩm nang Nền tảng Python và Bài tập Thực hành Căn bản (Huy Init)"
    },
    {
        "category": "04_huong_dan_guides",
        "filename": "VI_PY_11_Python_Huong_Dan_Thuc_Hanh_Va_Bai_Tap_Lab01.pdf",
        "url": "https://raw.githubusercontent.com/niie-it/python/main/Python_Exercise_Lab01.pdf",
        "desc": "Tài liệu Hướng dẫn Thực hành Bài tập Lab Lập trình Python (Quản lý Sinh viên)"
    }
]

def download_all():
    ctx = ssl._create_unverified_context()
    print("=" * 70)
    print("BẮT ĐẦU TẢI 10 TÀI LIỆU CHÍNH THỐNG TIẾNG VIỆT VỀ PYTHON")
    print("=" * 70)

    success_count = 0
    for idx, item in enumerate(DOWNLOAD_LIST, 1):
        target_dir = DOCS_DIR / item["category"]
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / item["filename"]

        print(f"\n[{idx}/10] Đang tải: {item['filename']}")
        print(f"       Mô tả: {item['desc']}")
        print(f"       Lưu vào: data/01_original_documents/{item['category']}/")

        try:
            req = urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                data = resp.read()
                target_file.write_bytes(data)
                size_mb = len(data) / (1024 * 1024)
                print(f"       ✅ Thành công ({size_mb:.2f} MB)")
                success_count += 1
        except Exception as e:
            print(f"       ❌ Thất bại: {e}")

    print("\n" + "=" * 70)
    print(f"HOÀN THÀNH: Đã tải thành công {success_count}/{len(DOWNLOAD_LIST)} tài liệu.")
    print("=" * 70)

if __name__ == "__main__":
    download_all()


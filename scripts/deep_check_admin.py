# -*- coding: utf-8 -*-
import fitz
from pathlib import Path

check_files = [
    Path('data/01_original_documents/python_100_authentic_pdfs/vi/VI_PDF_002_DongA_De_Cuong_Hoc_Phan_Lap_Trinh_Python.pdf'),
    Path('data/01_original_documents/python_batch2_authoritative_pdfs/vi/VI_PDF_059_NIIE_Ke_Hoach_Giang_Day_Hoc_Phan_Python_BM01.pdf'),
    Path('data/01_original_documents/python_batch2_authoritative_pdfs/vi/VI_PDF_060_NIIE_Huong_Dan_Danh_Gia_Tieu_Chi_Cham_Diem_Python.pdf')
]

for cf in check_files:
    if cf.exists():
        doc = fitz.open(cf)
        pages = len(doc)
        text = ""
        for p in doc:
            text += p.get_text() + " "
        doc.close()
        code_words = ['def ', 'class ', 'import ', 'print(', 'for ', 'while ', 'return ', 'lambda ']
        total_code = sum(text.count(w) for w in code_words)
        print(f"{cf.name}: {pages} pages, {total_code} code words")
        print("  Snippet:", " ".join(text[:250].split()))
    else:
        print(f"File not found: {cf}")

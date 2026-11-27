# -*- coding: utf-8 -*-
import fitz
from pathlib import Path
import json

base_dirs = [
    Path('data/01_original_documents/python_100_authentic_pdfs/vi'),
    Path('data/01_original_documents/python_batch2_authoritative_pdfs/vi')
]

print("=== ALL VIETNAMESE FILES AUDIT ===")
for b in base_dirs:
    print(f"\n--- Directory: {b} ---")
    for p in sorted(b.glob("*.pdf")):
        try:
            doc = fitz.open(p)
            n_pages = len(doc)
            txt = ""
            for i in range(min(n_pages, 3)):
                txt += doc[i].get_text().replace("\n", " ") + " "
            doc.close()
            txt_clean = " ".join(txt.split())
            print(f"{p.name} | {n_pages} trang | {txt_clean[:120]}")
        except Exception as e:
            print(f"{p.name} | ERROR: {e}")


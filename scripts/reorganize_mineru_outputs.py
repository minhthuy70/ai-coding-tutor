# -*- coding: utf-8 -*-
"""
Reorganize MinerU parser outputs into standard category directories
matching data/02_pending_parse:
- 01_sach
- 02_giao_trinh
- 03_tai_lieu_chuan_docs
- 04_huong_dan_guides
- 05_bai_tap_contests
"""
import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PENDING_DIR = BASE_DIR / "data" / "02_pending_parse"
MINERU_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"

def build_pdf_category_map():
    pdf_map = {}
    for pdf in PENDING_DIR.rglob("*.pdf"):
        rel_parts = pdf.relative_to(PENDING_DIR).parts
        # e.g., ('03_tai_lieu_chuan_docs', 'EN_PDF_005_....pdf') or ('01_sach', 'en', 'EN_PDF_....pdf')
        cat = rel_parts[0]
        stem = pdf.stem
        pdf_map[stem] = (cat, rel_parts[1:-1])  # category and any subdirs (like 'en' or 'vi')
    return pdf_map

def main():
    print("=" * 70)
    print("📂 REORGANIZING MINERU PARSER OUTPUTS TO STANDARD CATEGORIES")
    print("=" * 70)

    pdf_map = build_pdf_category_map()
    print(f"Total PDFs mapped in data/02_pending_parse: {len(pdf_map)}")

    # Check data/03_parser_outputs/mineru/en/
    en_dir = MINERU_DIR / "en"
    moved_count = 0
    if en_dir.exists() and en_dir.is_dir():
        for doc_dir in sorted(en_dir.iterdir()):
            if not doc_dir.is_dir():
                continue
            doc_name = doc_dir.name
            if doc_name in pdf_map:
                cat, subdirs = pdf_map[doc_name]
                if subdirs:
                    dest_dir = MINERU_DIR / cat / Path(*subdirs) / doc_name
                else:
                    dest_dir = MINERU_DIR / cat / "en" / doc_name
                
                dest_dir.parent.mkdir(parents=True, exist_ok=True)
                print(f"Moving: {doc_name} -> {dest_dir.relative_to(MINERU_DIR)}")
                shutil.move(str(doc_dir), str(dest_dir))
                moved_count += 1
            else:
                # Try finding without exact match or prefix
                found = False
                for stem, (cat, subdirs) in pdf_map.items():
                    if stem in doc_name or doc_name in stem:
                        dest_dir = MINERU_DIR / cat / "en" / doc_name
                        dest_dir.parent.mkdir(parents=True, exist_ok=True)
                        print(f"Moving (fuzzy): {doc_name} -> {dest_dir.relative_to(MINERU_DIR)}")
                        shutil.move(str(doc_dir), str(dest_dir))
                        moved_count += 1
                        found = True
                        break
                if not found:
                    print(f"⚠️ Unmapped doc in en/: {doc_name}")

        # If en_dir is now empty, remove it
        if en_dir.exists() and not any(en_dir.iterdir()):
            en_dir.rmdir()
            print("Removed empty data/03_parser_outputs/mineru/en directory.")

    print(f"\nTotal directories moved: {moved_count}")

    # Summary of all categories in MINERU_DIR
    print("\n📊 Current MinerU Categories:")
    for d in sorted(MINERU_DIR.iterdir()):
        if d.is_dir():
            md_files = list(d.rglob("*.md"))
            print(f"  • {d.name:30s}: {len(md_files)} markdown files")

if __name__ == "__main__":
    main()

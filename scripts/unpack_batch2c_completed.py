# -*- coding: utf-8 -*-
"""
Unpack the 4 massive library manuals from scratch/kaggle_output_batch2c/mineru_rag_output.zip
into data/03_parser_outputs/mineru/03_tai_lieu_chuan_docs/en/
"""
import zipfile
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ZIP_PATH = BASE_DIR / "scratch" / "kaggle_output_batch2c" / "mineru_rag_output.zip"
TARGET_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru" / "03_tai_lieu_chuan_docs" / "en"

def main():
    print(f"Opening {ZIP_PATH.name}...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        # Find all files belonging to the 4 completed documents
        members = zf.namelist()
        for member in members:
            # e.g., minhthuy70/python-rag-curated-batch2c/en/EN_PDF_089_Python_3.11_library/...
            parts = Path(member).parts
            if len(parts) >= 4 and parts[0] == "minhthuy70" and parts[1] == "python-rag-curated-batch2c":
                # relative to 'en'
                sub_rel = Path(*parts[3:])  # e.g. EN_PDF_089_... / ...
                dest = TARGET_DIR / sub_rel
                if member.endswith("/"):
                    dest.mkdir(parents=True, exist_ok=True)
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    with zf.open(member) as src, open(dest, "wb") as dst:
                        shutil.copyfileobj(src, dst)

    print("Extraction complete!")
    for doc in TARGET_DIR.glob("EN_PDF_*_library"):
        md_file = list(doc.glob("*.md"))
        print(f"  • {doc.name}: {len(md_file)} md file(s)")

if __name__ == "__main__":
    main()

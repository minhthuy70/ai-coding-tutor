# -*- coding: utf-8 -*-
"""
Extract Batch 2A zip directly into data/03_parser_outputs/mineru
"""
import zipfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ZIP_PATH = BASE_DIR / "scratch" / "kaggle_output_batch2" / "mineru_rag_output.zip"
DEST_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"

def main():
    print(f"Extracting {ZIP_PATH} ({round(ZIP_PATH.stat().st_size / (1024*1024), 2)} MB) to {DEST_DIR}...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        zf.extractall(DEST_DIR)

    mds = list(DEST_DIR.rglob("*.md"))
    successes = list(DEST_DIR.rglob("_SUCCESS.json"))
    print(f"✅ Extracted successfully!")
    print(f"  • Total markdown files: {len(mds)}")
    print(f"  • Total _SUCCESS markers: {len(successes)}")

if __name__ == "__main__":
    main()

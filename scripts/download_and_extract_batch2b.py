# -*- coding: utf-8 -*-
"""
Download Batch 2B outputs from Kaggle and extract into data/03_parser_outputs/mineru
"""
import os
import zipfile
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = BASE_DIR / "scratch" / "kaggle_output_batch2b"
MINERU_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"

def main():
    print("=" * 70)
    print("📥 DOWNLOADING BATCH 2B MINERU OUTPUTS FROM KAGGLE")
    print("=" * 70)

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    api = KaggleApi()
    api.authenticate()

    print("Fetching kernel output files from minhthuy70/mineru...")
    files, msg = api.kernels_output("minhthuy70/mineru", path=str(DOWNLOAD_DIR))
    print(f"Downloaded files: {len(files)}")
    for f in files:
        sz_mb = Path(f).stat().st_size / (1024 * 1024)
        print(f"  • {Path(f).name} ({sz_mb:.2f} MB)")

    # Find the zip file
    zip_candidates = list(DOWNLOAD_DIR.glob("*.zip"))
    if not zip_candidates:
        print("❌ No zip file found in download directory!")
        return

    target_zip = zip_candidates[0]
    print(f"\n📦 Extracting {target_zip.name} ({target_zip.stat().st_size / (1024*1024):.2f} MB) to {MINERU_DIR}...")
    with zipfile.ZipFile(target_zip, "r") as zf:
        zf.extractall(MINERU_DIR)

    all_mds = list(MINERU_DIR.rglob("*.md"))
    all_success = list(MINERU_DIR.rglob("_SUCCESS.json"))
    print(f"✅ Extraction complete!")
    print(f"  • Total markdown files in mineru: {len(all_mds)}")
    print(f"  • Total _SUCCESS markers in mineru: {len(all_success)}")

if __name__ == "__main__":
    main()

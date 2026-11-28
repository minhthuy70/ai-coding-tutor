# -*- coding: utf-8 -*-
"""
Download MinerU Batch 2 outputs from Kaggle and extract into data/03_parser_outputs/mineru/
"""
import zipfile
import shutil
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = BASE_DIR / "scratch" / "kaggle_output_batch2"
DEST_PARSER_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"

def main():
    print("=" * 70)
    print("📥 DOWNLOADING MINERU BATCH 2 OUTPUT FROM KAGGLE")
    print("=" * 70)

    if DOWNLOAD_DIR.exists():
        shutil.rmtree(DOWNLOAD_DIR)
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    DEST_PARSER_DIR.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    api.authenticate()
    print("Authenticated Kaggle API. Downloading kernel output for minhthuy70/mineru...")

    api.kernels_output("minhthuy70/mineru", path=str(DOWNLOAD_DIR))
    print(f"Downloaded files into {DOWNLOAD_DIR}")

    zip_path = DOWNLOAD_DIR / "mineru_rag_output.zip"
    if not zip_path.exists():
        # Check subdirectories
        zips = list(DOWNLOAD_DIR.rglob("*.zip"))
        if zips:
            zip_path = zips[0]
        else:
            raise FileNotFoundError(f"Cannot find mineru_rag_output.zip in {DOWNLOAD_DIR}")

    print(f"Extracting {zip_path} ({round(zip_path.stat().st_size / (1024*1024), 2)} MB) to {DEST_PARSER_DIR}...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(DEST_PARSER_DIR)

    extracted_mds = list(DEST_PARSER_DIR.rglob("*.md"))
    print(f"✅ Extracted successfully! Total markdown files now in {DEST_PARSER_DIR}: {len(extracted_mds)}")

if __name__ == "__main__":
    main()

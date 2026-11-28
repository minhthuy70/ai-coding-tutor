# -*- coding: utf-8 -*-
"""
Upload updated all_chunks.json (65,653 chunks) to Kaggle dataset minhthuy70/embedding
and trigger Kaggle GPU Dual-Model Embedding Pipeline.
"""
import shutil
import json
import time
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
CHUNKS_FILE = BASE_DIR / "data" / "06_rag_dataset" / "chunks" / "all_chunks.json"
UPLOAD_DIR = BASE_DIR / "scratch" / "kaggle_embedding_upload"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
DATASET_SLUG = "embedding"
KERNEL_SLUG = "ai-coding-tutor-embedding-pilot"

def main():
    print("=" * 70)
    print("🚀 PREPARING & LAUNCHING KAGGLE GPU DUAL-MODEL EMBEDDING PIPELINE")
    print("=" * 70)

    # 1. Prepare upload folder
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    dest_chunks = UPLOAD_DIR / "all_chunks.json"
    
    print(f"Copying {CHUNKS_FILE.name} ({CHUNKS_FILE.stat().st_size:,} bytes) to {UPLOAD_DIR}...")
    shutil.copy2(CHUNKS_FILE, dest_chunks)
    print("File copied successfully.")

    ds_meta = {
        "title": "embedding",
        "id": f"minhthuy70/{DATASET_SLUG}",
        "licenses": [{"name": "CC0-1.0"}]
    }
    with open(UPLOAD_DIR / "dataset-metadata.json", "w", encoding="utf-8") as f:
        json.dump(ds_meta, f, indent=2)

    # 2. Authenticate Kaggle API
    api = KaggleApi()
    api.authenticate()
    print("Authenticated Kaggle user:", api.get_config_value("username"))

    ds_ref = f"minhthuy70/{DATASET_SLUG}"
    print(f"📦 Uploading new version for dataset {ds_ref}...")
    api.dataset_create_version(
        folder=str(UPLOAD_DIR),
        version_notes="Upload complete 65,653 chunks (100% authentic python corpus)",
        dir_mode="zip",
        quiet=False
    )

    print("Waiting for Kaggle dataset to be ready...")
    for i in range(60):
        try:
            status = api.dataset_status(ds_ref)
            print(f"Dataset status check #{i+1}: {status}")
            if status == "ready":
                break
        except Exception as e:
            print(f"Check #{i+1}: Waiting for dataset processing...", e)
        time.sleep(5)

    # 3. Push embedding kernel
    print(f"\n🚀 Pushing kernel {KERNEL_SLUG} to Kaggle (Tesla T4 GPU)...")
    res = api.kernels_push(str(NOTEBOOKS_DIR))
    print("Kernel push response:", vars(res) if hasattr(res, "__dict__") else res)
    print(f"✅ Successfully launched Kaggle GPU Embedding kernel: minhthuy70/{KERNEL_SLUG}")

if __name__ == "__main__":
    main()

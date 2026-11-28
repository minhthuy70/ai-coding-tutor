# -*- coding: utf-8 -*-
"""
Upload python-rag-curated-batch2a dataset to Kaggle and push kernel
"""
import time
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "scratch" / "kaggle_batch2a_upload"
KERNEL_DIR = BASE_DIR / "scratch" / "kaggle_mineru"
DATASET_SLUG = "python-rag-curated-batch2a"

def main():
    api = KaggleApi()
    api.authenticate()
    print("Authenticated Kaggle user:", api.get_config_value("username"))

    existing = [d.ref for d in api.dataset_list(user="minhthuy70")]
    dataset_ref = f"minhthuy70/{DATASET_SLUG}"

    if dataset_ref in existing:
        print(f"📦 Dataset {dataset_ref} already exists, creating new version...")
        api.dataset_create_version(folder=str(UPLOAD_DIR), version_notes="Upload Batch 2A (136 PDFs)", dir_mode="zip", quiet=False)
    else:
        print(f"📦 Creating new dataset {dataset_ref}...")
        api.dataset_create_new(folder=str(UPLOAD_DIR), dir_mode="zip", quiet=False)

    print("Waiting for Kaggle dataset to be ready...")
    for _ in range(60):
        status = api.dataset_status(dataset_ref)
        print("Dataset status:", status)
        if status == "ready":
            break
        time.sleep(5)

    print("🚀 Pushing updated mineru kernel to Kaggle...")
    res = api.kernels_push(str(KERNEL_DIR))
    print("Kernel push response:", vars(res) if hasattr(res, "__dict__") else res)
    print("✅ Kernel launched on Kaggle!")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Prepare and launch dedicated Kaggle kernel for EN_PDF_191_Python_3.7_library.pdf
Achieves 323 / 323 documents parsed (100.0% completion).
"""
import shutil
import json
import time
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_PDF = BASE_DIR / "scratch" / "kaggle_batch2c_upload" / "03_tai_lieu_chuan_docs" / "en" / "EN_PDF_191_Python_3.7_library.pdf"
UPLOAD_DIR = BASE_DIR / "scratch" / "kaggle_upload_191"
KERNEL_DIR = BASE_DIR / "scratch" / "kaggle_mineru_191"
DATASET_SLUG = "python-rag-curated-191"
KERNEL_SLUG = "mineru-191-final"

def main():
    print("=" * 70)
    print("🚀 PREPARING AND LAUNCHING DEDICATED KAGGLE KERNEL FOR EN_PDF_191")
    print("=" * 70)

    # 1. Prepare Dataset Folder
    dest_pdf_dir = UPLOAD_DIR / "03_tai_lieu_chuan_docs" / "en"
    dest_pdf_dir.mkdir(parents=True, exist_ok=True)
    dest_pdf = dest_pdf_dir / "EN_PDF_191_Python_3.7_library.pdf"
    
    if not dest_pdf.exists():
        print(f"Copying {SRC_PDF.name} to upload directory...")
        shutil.copy2(SRC_PDF, dest_pdf)
    print(f"Dataset source ready: {dest_pdf} ({dest_pdf.stat().st_size:,} bytes)")

    ds_meta = {
        "title": "Python RAG Curated 191",
        "id": f"minhthuy70/{DATASET_SLUG}",
        "licenses": [{"name": "CC0-1.0"}]
    }
    with open(UPLOAD_DIR / "dataset-metadata.json", "w", encoding="utf-8") as f:
        json.dump(ds_meta, f, indent=2)

    # 2. Authenticate Kaggle API
    api = KaggleApi()
    api.authenticate()
    print("Authenticated Kaggle user:", api.get_config_value("username"))

    existing_ds = [d.ref for d in api.dataset_list(user="minhthuy70")]
    ds_ref = f"minhthuy70/{DATASET_SLUG}"

    if ds_ref in existing_ds:
        print(f"📦 Dataset {ds_ref} already exists, creating new version...")
        api.dataset_create_version(folder=str(UPLOAD_DIR), version_notes="EN_PDF_191 dedicated upload", dir_mode="zip", quiet=False)
    else:
        print(f"📦 Creating new dataset {ds_ref}...")
        api.dataset_create_new(folder=str(UPLOAD_DIR), dir_mode="zip", quiet=False)

    print("Waiting for Kaggle dataset to be ready...")
    for _ in range(60):
        try:
            status = api.dataset_status(ds_ref)
            print("Dataset status:", status)
            if status == "ready":
                break
        except Exception as e:
            print("Waiting for dataset metadata...", e)
        time.sleep(5)

    # 3. Prepare Kernel
    KERNEL_DIR.mkdir(parents=True, exist_ok=True)
    src_nb = BASE_DIR / "scratch" / "kaggle_mineru" / "mineru.ipynb"
    dest_nb = KERNEL_DIR / "mineru.ipynb"
    shutil.copy2(src_nb, dest_nb)

    kernel_meta = {
        "id": f"minhthuy70/{KERNEL_SLUG}",
        "title": "MinerU 191 Final",
        "code_file": "mineru.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": False,
        "enable_gpu": True,
        "enable_tpu": False,
        "enable_internet": True,
        "keywords": ["gpu"],
        "dataset_sources": [ds_ref],
        "kernel_sources": [],
        "competition_sources": [],
        "model_sources": [],
        "machine_shape": "NvidiaTeslaT4"
    }
    with open(KERNEL_DIR / "kernel-metadata.json", "w", encoding="utf-8") as f:
        json.dump(kernel_meta, f, indent=2)

    print(f"🚀 Pushing kernel {KERNEL_SLUG} to Kaggle (2x Tesla T4 GPU)...")
    res = api.kernels_push(str(KERNEL_DIR))
    print("Kernel push response:", vars(res) if hasattr(res, "__dict__") else res)
    print(f"✅ Successfully launched dedicated kernel: minhthuy70/{KERNEL_SLUG}")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Create and launch a brand new Kaggle Kernel 'mineru-batch2c'
This avoids the stale queue of the old kernel and starts running immediately.
"""
import shutil
import json
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "scratch" / "kaggle_mineru"
NEW_KERNEL_DIR = BASE_DIR / "scratch" / "kaggle_mineru_batch2c"
DATASET_SLUG = "python-rag-curated-batch2c"
NEW_KERNEL_SLUG = "mineru-batch2c"

def main():
    print("=" * 70)
    print("🚀 CREATING & LAUNCHING BRAND NEW KAGGLE KERNEL FOR BATCH 2C")
    print("=" * 70)

    NEW_KERNEL_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Copy verified notebook
    src_nb = SRC_DIR / "mineru.ipynb"
    dest_nb = NEW_KERNEL_DIR / "mineru.ipynb"
    shutil.copy2(src_nb, dest_nb)
    print(f"Copied verified notebook to {dest_nb}")

    # 2. Create new kernel-metadata.json
    metadata = {
        "id": f"minhthuy70/{NEW_KERNEL_SLUG}",
        "title": "MinerU Batch 2C Final",
        "code_file": "mineru.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": False,
        "enable_gpu": True,
        "enable_tpu": False,
        "enable_internet": True,
        "keywords": ["gpu"],
        "dataset_sources": [f"minhthuy70/{DATASET_SLUG}"],
        "kernel_sources": [],
        "competition_sources": [],
        "model_sources": [],
        "machine_shape": "NvidiaTeslaT4"
    }

    meta_file = NEW_KERNEL_DIR / "kernel-metadata.json"
    with open(meta_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print(f"Created metadata for new kernel: minhthuy70/{NEW_KERNEL_SLUG}")

    # 3. Authenticate and push kernel
    api = KaggleApi()
    api.authenticate()
    print("Pushing new kernel to Kaggle...")
    res = api.kernels_push(str(NEW_KERNEL_DIR))
    print("Kernel push response:", vars(res) if hasattr(res, "__dict__") else res)
    print(f"✅ Successfully launched new kernel: minhthuy70/{NEW_KERNEL_SLUG}")

if __name__ == "__main__":
    main()

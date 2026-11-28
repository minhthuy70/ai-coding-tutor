# -*- coding: utf-8 -*-
"""
Prepare Batch 2 dataset (Remaining 245 English files: Cornell, MIT, Oxford, Cambridge, PSF Docs & HOWTOs),
Upload dataset to Kaggle, update minerU kernel metadata, and launch kernel run on Kaggle (2x Tesla T4 GPU).
"""

import os
import shutil
import json
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "01_original_documents"
UPLOAD_DIR = BASE_DIR / "scratch" / "kaggle_batch2_upload"
KERNEL_DIR = BASE_DIR / "scratch" / "kaggle_mineru"

# 1. Prepare upload folder
if UPLOAD_DIR.exists():
    shutil.rmtree(UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

batch2_sources = [
    DOCS_DIR / "02_giao_trinh" / "en",
    DOCS_DIR / "04_huong_dan_guides" / "en",
    DOCS_DIR / "03_tai_lieu_chuan_docs" / "en"
]

copied_files = 0
total_bytes = 0

for src in batch2_sources:
    if src.exists():
        rel = src.relative_to(DOCS_DIR)
        dest = UPLOAD_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)

for p in UPLOAD_DIR.rglob("*.pdf"):
    copied_files += 1
    total_bytes += p.stat().st_size

print(f"✅ Prepared {copied_files} PDF files ({round(total_bytes/(1024*1024), 2)} MB) in {UPLOAD_DIR}")

# 2. Create dataset-metadata.json
DATASET_SLUG = "python-rag-curated-batch2"
meta = {
    "title": "Python RAG Curated Batch 2",
    "id": f"minhthuy70/{DATASET_SLUG}",
    "licenses": [{"name": "CC0-1.0"}]
}

meta_file = UPLOAD_DIR / "dataset-metadata.json"
with open(meta_file, "w", encoding="utf-8") as f:
    json.dump(meta, f, indent=2)

print(f"✅ Created dataset metadata: {meta_file}")

# 3. Authenticate and create dataset on Kaggle
api = KaggleApi()
api.authenticate()
print(f"Authenticated Kaggle user: {api.get_config_value('username')}")

existing = [d.ref for d in api.dataset_list(user='minhthuy70')]
if f"minhthuy70/{DATASET_SLUG}" in existing:
    print(f"📦 Dataset minhthuy70/{DATASET_SLUG} already exists, creating new version...")
    api.dataset_create_version(folder=str(UPLOAD_DIR), version_notes="Upload Batch 2 remaining 245 PDFs", dir_mode="zip", quiet=False)
else:
    print(f"📦 Creating new dataset minhthuy70/{DATASET_SLUG}...")
    api.dataset_create_new(folder=str(UPLOAD_DIR), dir_mode="zip", quiet=False)

print("✅ Dataset uploaded successfully to Kaggle!")

# 4. Update kernel-metadata.json in KERNEL_DIR
kernel_meta_file = KERNEL_DIR / "kernel-metadata.json"
kernel_meta = json.loads(kernel_meta_file.read_text(encoding="utf-8"))

# Attach new dataset
kernel_meta["dataset_sources"] = [f"minhthuy70/{DATASET_SLUG}"]
kernel_meta["enable_gpu"] = True
kernel_meta["enable_internet"] = True
kernel_meta["machine_shape"] = "NvidiaTeslaT4"

with open(kernel_meta_file, "w", encoding="utf-8") as f:
    json.dump(kernel_meta, f, indent=2)

print(f"✅ Updated {kernel_meta_file} with dataset: minhthuy70/{DATASET_SLUG}")

# -*- coding: utf-8 -*-
"""
Prepare Batch 2C (Final 5 Massive Python Standard Library Manuals: 3.11, 3.9, 3.8, 3.7, 2.7)
Upload to Kaggle dataset 'python-rag-curated-batch2c'
Update kernel metadata and launch on Kaggle 2x Tesla T4 GPU
"""
import os
import shutil
import json
from pathlib import Path
import pypdf

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "01_original_documents"
MINERU_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"
UPLOAD_DIR = BASE_DIR / "scratch" / "kaggle_batch2c_upload"
KERNEL_DIR = BASE_DIR / "scratch" / "kaggle_mineru"
DATASET_SLUG = "python-rag-curated-batch2c"

def main():
    print("=" * 70)
    print("🚀 PREPARING BATCH 2C (FINAL 5 MASSIVE PYTHON LIBRARY MANUALS)")
    print("=" * 70)

    # 1. Get already parsed documents
    parsed_stems = set()
    for s in MINERU_DIR.rglob("_SUCCESS.json"):
        parsed_stems.add(s.parent.name)

    # 2. Select remaining unparsed PDFs
    target_dir = DOCS_DIR / "03_tai_lieu_chuan_docs" / "en"
    remaining = [p for p in target_dir.glob("*.pdf") if p.stem not in parsed_stems]

    print(f"Remaining unparsed PDFs for Batch 2C: {len(remaining)}")

    if UPLOAD_DIR.exists():
        shutil.rmtree(UPLOAD_DIR)
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    total_bytes = 0
    total_pages = 0
    for p in remaining:
        try:
            reader = pypdf.PdfReader(str(p))
            pages = len(reader.pages)
        except Exception:
            pages = 0
        rel = p.relative_to(DOCS_DIR)
        dest = UPLOAD_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
        total_bytes += p.stat().st_size
        total_pages += pages
        print(f"  • {p.name}: {pages} pages ({p.stat().st_size / (1024*1024):.2f} MB)")

    print(f"\nCopied {len(remaining)} PDFs ({total_pages} pages, {round(total_bytes/(1024*1024), 2)} MB) to {UPLOAD_DIR}")

    # 3. Create dataset-metadata.json
    meta = {
        "title": "Python RAG Curated Batch 2C",
        "id": f"minhthuy70/{DATASET_SLUG}",
        "licenses": [{"name": "CC0-1.0"}]
    }
    with open(UPLOAD_DIR / "dataset-metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    # 4. Update kernel metadata
    km_file = KERNEL_DIR / "kernel-metadata.json"
    km = json.loads(km_file.read_text(encoding="utf-8"))
    km["dataset_sources"] = [f"minhthuy70/{DATASET_SLUG}"]
    km_file.write_text(json.dumps(km, indent=2), encoding="utf-8")
    print(f"✅ Updated kernel metadata to point to: minhthuy70/{DATASET_SLUG}")

if __name__ == "__main__":
    main()

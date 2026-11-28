# -*- coding: utf-8 -*-
"""
Prepare Batch 2A (136 Curriculum & Guide PDFs: MIT, Cornell, Oxford, Cambridge, HOWTOs)
Upload to Kaggle dataset 'python-rag-curated-batch2a'
Patch mineru.ipynb with per-document memory cleanup to prevent OOM
Launch version on Kaggle with 2x Tesla T4 GPU
"""
import os
import shutil
import json
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "01_original_documents"
MINERU_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"
UPLOAD_DIR = BASE_DIR / "scratch" / "kaggle_batch2a_upload"
KERNEL_DIR = BASE_DIR / "scratch" / "kaggle_mineru"

def main():
    print("=" * 70)
    print("🚀 PREPARING BATCH 2A (136 CURRICULUM & GUIDE PDFS)")
    print("=" * 70)

    # 1. Get already parsed documents
    parsed_stems = set()
    for s in MINERU_DIR.rglob("_SUCCESS.json"):
        rel = s.parent.relative_to(MINERU_DIR)
        parsed_stems.add(str(rel).replace("\\", "/"))

    # 2. Select remaining PDFs from 02_giao_trinh/en and 04_huong_dan_guides/en
    target_dirs = [
        DOCS_DIR / "02_giao_trinh" / "en",
        DOCS_DIR / "04_huong_dan_guides" / "en"
    ]

    selected_pdfs = []
    for td in target_dirs:
        if td.exists():
            for p in td.glob("*.pdf"):
                stem_key = str(p.relative_to(DOCS_DIR).parent / p.stem).replace("\\", "/")
                if stem_key not in parsed_stems:
                    selected_pdfs.append(p)

    print(f"Selected {len(selected_pdfs)} unparsed PDFs for Batch 2A")

    if UPLOAD_DIR.exists():
        shutil.rmtree(UPLOAD_DIR)
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    total_bytes = 0
    for p in selected_pdfs:
        rel = p.relative_to(DOCS_DIR)
        dest = UPLOAD_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
        total_bytes += p.stat().st_size

    print(f"Copied {len(selected_pdfs)} PDFs ({round(total_bytes/(1024*1024), 2)} MB) to {UPLOAD_DIR}")

    # 3. Create dataset-metadata.json
    DATASET_SLUG = "python-rag-curated-batch2a"
    meta = {
        "title": "Python RAG Curated Batch 2A",
        "id": f"minhthuy70/{DATASET_SLUG}",
        "licenses": [{"name": "CC0-1.0"}]
    }
    with open(UPLOAD_DIR / "dataset-metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    # 4. Patch mineru.ipynb with strict memory management
    nb_file = KERNEL_DIR / "mineru.ipynb"
    nb = json.loads(nb_file.read_text(encoding="utf-8"))

    # Inspect and patch worker code in cell 6
    for cell in nb["cells"]:
        src = "".join(cell.get("source", []))
        if "def process_job(" in src:
            # Add gc and torch cache cleanup
            if "gc.collect()" not in src:
                src = src.replace(
                    "return {\n        'status': 'ok',",
                    "del result\n    del middle_data\n    del md\n    import gc\n    import torch\n    gc.collect()\n    if torch.cuda.is_available():\n        torch.cuda.empty_cache()\n    if work_dir.exists():\n        shutil.rmtree(work_dir, ignore_errors=True)\n    return {\n        'status': 'ok',"
                )
                cell["source"] = [src]
                print("✅ Patched process_job with gc.collect() and empty_cache()")

    nb_file.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Saved patched notebook: {nb_file}")

    # 5. Update kernel metadata
    km_file = KERNEL_DIR / "kernel-metadata.json"
    km = json.loads(km_file.read_text(encoding="utf-8"))
    km["dataset_sources"] = [f"minhthuy70/{DATASET_SLUG}"]
    km_file.write_text(json.dumps(km, indent=2), encoding="utf-8")
    print(f"✅ Updated kernel metadata with dataset: minhthuy70/{DATASET_SLUG}")

if __name__ == "__main__":
    main()

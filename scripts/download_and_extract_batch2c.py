# -*- coding: utf-8 -*-
"""
Download Batch 2C outputs from Kaggle (mineru-batch-2c-final)
and extract into data/03_parser_outputs/mineru under standard categories.
"""
import os
import zipfile
import shutil
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = BASE_DIR / "scratch" / "kaggle_output_batch2c"
MINERU_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"
PENDING_DIR = BASE_DIR / "data" / "02_pending_parse"
KERNEL_SLUG = "minhthuy70/mineru-batch-2c-final"

def build_pdf_category_map():
    pdf_map = {}
    for pdf in PENDING_DIR.rglob("*.pdf"):
        rel_parts = pdf.relative_to(PENDING_DIR).parts
        cat = rel_parts[0]
        stem = pdf.stem
        pdf_map[stem] = (cat, rel_parts[1:-1])
    return pdf_map

def main():
    print("=" * 70)
    print("📥 DOWNLOADING BATCH 2C MINERU OUTPUTS FROM KAGGLE")
    print("=" * 70)

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    api = KaggleApi()
    api.authenticate()

    print(f"Fetching kernel output files from {KERNEL_SLUG}...")
    files, msg = api.kernels_output(KERNEL_SLUG, path=str(DOWNLOAD_DIR))
    print(f"Downloaded files: {len(files) if files else 0}")
    if files:
        for f in files:
            sz_mb = Path(f).stat().st_size / (1024 * 1024)
            print(f"  • {Path(f).name} ({sz_mb:.2f} MB)")

    # Find the zip file
    zip_candidates = list(DOWNLOAD_DIR.glob("*.zip"))
    if not zip_candidates:
        print("❌ No zip file found in download directory!")
        # Check if directories or markdown files were downloaded directly
        all_downloaded = list(DOWNLOAD_DIR.rglob("*"))
        print(f"Total items in {DOWNLOAD_DIR}: {len(all_downloaded)}")
        return

    target_zip = zip_candidates[0]
    print(f"\n📦 Extracting {target_zip.name} ({target_zip.stat().st_size / (1024*1024):.2f} MB) to temp staging...")
    
    extract_temp = DOWNLOAD_DIR / "unpacked"
    extract_temp.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target_zip, "r") as zf:
        zf.extractall(extract_temp)

    pdf_map = build_pdf_category_map()
    print(f"Mapped {len(pdf_map)} PDF paths from {PENDING_DIR.name}")

    # Inspect what was unpacked
    unpacked_mds = list(extract_temp.rglob("*.md"))
    print(f"Total markdown files found in zip: {len(unpacked_mds)}")

    # Move each extracted doc directory into the appropriate MINERU_DIR category
    # Doc directories usually contain: <doc_name>/<doc_name>.md, _SUCCESS.json, images/, etc.
    doc_dirs = set()
    for md in unpacked_mds:
        # parent of the md file is the document folder
        doc_dirs.add(md.parent)

    print(f"Distinct document directories to place: {len(doc_dirs)}")
    placed_count = 0
    for d in sorted(doc_dirs):
        doc_name = d.name
        # Match against pdf_map
        matched_cat = None
        matched_subdirs = ()
        if doc_name in pdf_map:
            matched_cat, matched_subdirs = pdf_map[doc_name]
        else:
            for stem, (cat, subdirs) in pdf_map.items():
                if stem in doc_name or doc_name in stem:
                    matched_cat, matched_subdirs = cat, subdirs
                    break

        if not matched_cat:
            matched_cat = "03_tai_lieu_chuan_docs"
            matched_subdirs = ("en",)

        if matched_subdirs:
            dest = MINERU_DIR / matched_cat / Path(*matched_subdirs) / doc_name
        else:
            dest = MINERU_DIR / matched_cat / "en" / doc_name

        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            shutil.rmtree(dest)
        print(f"Placing {doc_name} -> {dest.relative_to(MINERU_DIR)}")
        shutil.move(str(d), str(dest))
        placed_count += 1

    print(f"\n✅ Successfully placed {placed_count} documents into {MINERU_DIR}!")

    total_mds = list(MINERU_DIR.rglob("*.md"))
    total_success = list(MINERU_DIR.rglob("_SUCCESS.json"))
    print(f"🎉 Current overall MinerU totals:")
    print(f"  • Total markdown files: {len(total_mds)}")
    print(f"  • Total _SUCCESS markers: {len(total_success)}")

if __name__ == "__main__":
    main()

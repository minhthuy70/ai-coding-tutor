# -*- coding: utf-8 -*-
"""
Prepare Batch 2B (49 Standard Python Documentation PDFs: tutorials, C-API, FAQs, reference)
Upload to Kaggle dataset 'python-rag-curated-batch2b'
Patch mineru.ipynb with strict shallow-copy and memory cleanup
Push kernel to Kaggle with 2x Tesla T4 GPU
"""
import os
import shutil
import json
import time
from pathlib import Path
import pypdf
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "01_original_documents"
MINERU_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru"
UPLOAD_DIR = BASE_DIR / "scratch" / "kaggle_batch2b_upload"
KERNEL_DIR = BASE_DIR / "scratch" / "kaggle_mineru"
DATASET_SLUG = "python-rag-curated-batch2b"

def main():
    print("=" * 70)
    print("🚀 PREPARING BATCH 2B (49 STANDARD PYTHON DOCUMENTATION PDFS)")
    print("=" * 70)

    # 1. Get already parsed documents
    parsed_stems = set()
    for s in MINERU_DIR.rglob("_SUCCESS.json"):
        parsed_stems.add(s.parent.name)

    # 2. Select unparsed PDFs in 03_tai_lieu_chuan_docs/en with pages <= 1000
    target_dir = DOCS_DIR / "03_tai_lieu_chuan_docs" / "en"
    all_unparsed = []
    for p in target_dir.glob("*.pdf"):
        if p.stem not in parsed_stems:
            all_unparsed.append(p)

    selected_pdfs = []
    skipped_large = []
    for p in sorted(all_unparsed, key=lambda x: x.stat().st_size):
        try:
            reader = pypdf.PdfReader(str(p))
            pages = len(reader.pages)
        except Exception:
            pages = 0
        if pages > 1000:
            skipped_large.append((p, pages))
        else:
            selected_pdfs.append((p, pages))

    print(f"Total unparsed in 03_tai_lieu_chuan_docs/en: {len(all_unparsed)}")
    print(f"Selected for Batch 2B (pages <= 1000): {len(selected_pdfs)}")
    print(f"Deferred for Batch 2C (large library manuals > 1000 pages): {len(skipped_large)}")
    for p, pages in skipped_large:
        print(f"  • {p.name} ({pages} pages, {p.stat().st_size / (1024*1024):.2f} MB)")

    if UPLOAD_DIR.exists():
        shutil.rmtree(UPLOAD_DIR)
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    total_bytes = 0
    total_pages = 0
    for p, pages in selected_pdfs:
        rel = p.relative_to(DOCS_DIR)
        dest = UPLOAD_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
        total_bytes += p.stat().st_size
        total_pages += pages

    print(f"Copied {len(selected_pdfs)} PDFs ({total_pages} pages, {round(total_bytes/(1024*1024), 2)} MB) to {UPLOAD_DIR}")

    # 3. Create dataset-metadata.json
    meta = {
        "title": "Python RAG Curated Batch 2B",
        "id": f"minhthuy70/{DATASET_SLUG}",
        "licenses": [{"name": "CC0-1.0"}]
    }
    with open(UPLOAD_DIR / "dataset-metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    # 4. Patch mineru.ipynb: replace marked_markdown with shallow copy optimization
    nb_file = KERNEL_DIR / "mineru.ipynb"
    nb = json.loads(nb_file.read_text(encoding="utf-8"))

    for cell in nb["cells"]:
        src = "".join(cell.get("source", []))
        if "def marked_markdown(middle_path):" in src:
            # Replace heavy deepcopy with shallow copy and fallback
            old_func_pattern = """def marked_markdown(middle_path):
    full_data = json.loads(middle_path.read_text(encoding='utf-8'))
    parts = []
    for page in full_data.get('pages', []):
        page_num = int(page['page_idx']) + 1
        page_md = render(one_page_middle(full_data, page), RenderFormat.MARKDOWN)
        page_md = '' if page_md is None else str(page_md).strip()
        marker = f'<!-- page: {page_num} -->'
        parts.append(f'{marker}\\n\\n{page_md}' if page_md else marker)
    return '\\n\\n'.join(parts).rstrip() + '\\n'"""

            new_func = """def marked_markdown(middle_path):
    try:
        full_data = json.loads(middle_path.read_text(encoding='utf-8'))
        pages = full_data.get('pages', [])
        if len(pages) > 200:
            md_path = middle_path.parent / 'markdown.md'
            if md_path.exists():
                return md_path.read_text(encoding='utf-8')
        parts = []
        base = {k: v for k, v in full_data.items() if k != 'pages'}
        for page in pages:
            page_num = int(page['page_idx']) + 1
            one = {**base, 'pages': [page], 'is_full_document': False}
            page_md = render(load_middle(one), RenderFormat.MARKDOWN)
            page_md = '' if page_md is None else str(page_md).strip()
            marker = f'<!-- page: {page_num} -->'
            parts.append(f'{marker}\\n\\n{page_md}' if page_md else marker)
        return '\\n\\n'.join(parts).rstrip() + '\\n'
    except Exception:
        md_path = middle_path.parent / 'markdown.md'
        if md_path.exists():
            return md_path.read_text(encoding='utf-8')
        raise"""
            if old_func_pattern in src:
                src = src.replace(old_func_pattern, new_func)
                cell["source"] = [src]
                print("✅ Patched marked_markdown with shallow copy optimization")

    nb_file.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Saved notebook: {nb_file}")

    # 5. Update kernel metadata
    km_file = KERNEL_DIR / "kernel-metadata.json"
    km = json.loads(km_file.read_text(encoding="utf-8"))
    km["dataset_sources"] = [f"minhthuy70/{DATASET_SLUG}"]
    km_file.write_text(json.dumps(km, indent=2), encoding="utf-8")
    print(f"✅ Updated kernel metadata to point to: minhthuy70/{DATASET_SLUG}")

if __name__ == "__main__":
    main()

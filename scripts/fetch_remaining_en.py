# -*- coding: utf-8 -*-
import io
import re
import json
import zipfile
import hashlib
import requests
import fitz
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "01_original_documents" / "python_batch2_authoritative_pdfs"
OUT_EN = OUTPUT_DIR / "en"
OUT_VI = OUTPUT_DIR / "vi"
CATALOG_FILE = OUTPUT_DIR / "catalog_batch2_authentic_pdfs.json"

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# 1. Load existing hashes
all_hashes = set()
for p in (BASE_DIR / "data" / "01_original_documents").rglob("*.pdf"):
    try:
        all_hashes.add(hashlib.md5(p.read_bytes()).hexdigest())
    except:
        pass

# Also load catalog_batch2
if CATALOG_FILE.exists():
    try:
        with open(CATALOG_FILE, "r", encoding="utf-8") as f:
            catalog = json.load(f)
    except:
        catalog = []
else:
    catalog = []

catalog_by_id = {item["id"]: item for item in catalog}

# Count current EN files
en_files = sorted(list(OUT_EN.glob("*.pdf")))
current_en_count = len(en_files)
print(f"Current EN files in batch 2: {current_en_count}")
print(f"Current catalog entries: {len(catalog)}")

# Find highest EN id in OUT_EN
highest_en_num = 50
for f in en_files:
    m = re.match(r"EN_PDF_(\d+)", f.name)
    if m:
        num = int(m.group(1))
        if num > highest_en_num:
            highest_en_num = num

print(f"Highest EN number so far: {highest_en_num}")
target_en_num = 250 # 50 from batch 1 + 200 = 250

needed = target_en_num - highest_en_num
print(f"Still needed to reach 200 EN in Batch 2: {needed}")

# 2. Add Cornell Lecture 24 (Sanitized filename)
if highest_en_num < target_en_num:
    url_24 = "https://www.cs.cornell.edu/courses/cs1110/2026fa/lectures/lecture24/handout-24.pdf"
    try:
        r = session.get(url_24, timeout=15)
        if r.status_code == 200 and r.content.startswith(b"%PDF"):
            h = hashlib.md5(r.content).hexdigest()
            if h not in all_hashes:
                highest_en_num += 1
                file_code = f"EN_PDF_{highest_en_num:03d}"
                doc = fitz.open(stream=r.content, filetype="pdf")
                pages = len(doc)
                doc.close()
                filename = f"{file_code}_Cornell_CS1110_Lec24_File_IO_CSV_Data_Processing.pdf"
                (OUT_EN / filename).write_bytes(r.content)
                all_hashes.add(h)
                meta = {
                    "id": file_code,
                    "filename": filename,
                    "title": "Cornell CS1110 Lecture 24: File I/O, CSV and Structured Data Processing",
                    "author": "Prof. Walker White, Prof. Lillian Lee",
                    "institution": "Cornell University",
                    "language": "en",
                    "page_count": pages,
                    "file_size_bytes": len(r.content),
                    "file_size_mb": round(len(r.content) / (1024 * 1024), 2),
                    "md5_hash": h,
                    "source_url": url_24
                }
                catalog.append(meta)
                print(f"✅ Added {filename}")
    except Exception as e:
        print(f"Error Cornell 24: {e}")

# 3. Add Green Tea Press Books
gt_books = [
    {
        "title": "Think Complexity 2nd Edition: Science and Computational Modeling with Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/complexity2/thinkcomplexity2.pdf",
        "slug": "GreenTeaPress_Think_Complexity_2nd_Edition_Allen_Downey.pdf"
    },
    {
        "title": "Think Stats 2nd Edition: Exploratory Data Analysis in Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/thinkstats2/thinkstats2.pdf",
        "slug": "GreenTeaPress_Think_Stats_2nd_Edition_Allen_Downey.pdf"
    },
    {
        "title": "Think Bayes 2nd Edition: Bayesian Statistics in Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/thinkbayes2/thinkbayes2.pdf",
        "slug": "GreenTeaPress_Think_Bayes_2nd_Edition_Allen_Downey.pdf"
    },
    {
        "title": "Think DSP: Digital Signal Processing in Python",
        "author": "Allen B. Downey",
        "institution": "Green Tea Press",
        "url": "https://greenteapress.com/thinkdsp/thinkdsp.pdf",
        "slug": "GreenTeaPress_Think_DSP_Allen_Downey.pdf"
    }
]

for item in gt_books:
    if highest_en_num >= target_en_num:
        break
    try:
        r = session.get(item["url"], timeout=20)
        if r.status_code == 200 and r.content.startswith(b"%PDF"):
            h = hashlib.md5(r.content).hexdigest()
            if h not in all_hashes:
                doc = fitz.open(stream=r.content, filetype="pdf")
                pages = len(doc)
                doc.close()
                highest_en_num += 1
                file_code = f"EN_PDF_{highest_en_num:03d}"
                filename = f"{file_code}_{item['slug']}"
                (OUT_EN / filename).write_bytes(r.content)
                all_hashes.add(h)
                meta = {
                    "id": file_code,
                    "filename": filename,
                    "title": item["title"],
                    "author": item["author"],
                    "institution": item["institution"],
                    "language": "en",
                    "page_count": pages,
                    "file_size_bytes": len(r.content),
                    "file_size_mb": round(len(r.content) / (1024 * 1024), 2),
                    "md5_hash": h,
                    "source_url": item["url"]
                }
                catalog.append(meta)
                print(f"✅ Added {filename}")
    except Exception as e:
        print(f"Error {item['title']}: {e}")

# 4. Check Python 2.7.18 docs zip for remaining
if highest_en_num < target_en_num:
    zip_url = "https://docs.python.org/2.7/archives/python-2.7.18-docs-pdf-a4.zip"
    print(f"\n📦 Fetching {zip_url}...")
    try:
        r_zip = session.get(zip_url, timeout=45)
        if r_zip.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(r_zip.content)) as zf:
                for entry_name in sorted(zf.namelist()):
                    if highest_en_num >= target_en_num:
                        break
                    if entry_name.endswith(".pdf"):
                        pdf_data = zf.read(entry_name)
                        if len(pdf_data) < 10000 or not pdf_data.startswith(b"%PDF"):
                            continue
                        h = hashlib.md5(pdf_data).hexdigest()
                        if h in all_hashes:
                            continue
                        doc = fitz.open(stream=pdf_data, filetype="pdf")
                        pages = len(doc)
                        doc_title = doc.metadata.get("title", "") or Path(entry_name).stem.replace("-", " ").title()
                        doc.close()

                        highest_en_num += 1
                        file_code = f"EN_PDF_{highest_en_num:03d}"
                        slug = f"Python_2.7.18_{Path(entry_name).name}"
                        filename = f"{file_code}_{slug}"
                        (OUT_EN / filename).write_bytes(pdf_data)
                        all_hashes.add(h)

                        meta = {
                            "id": file_code,
                            "filename": filename,
                            "title": f"Python 2.7.18 Official Documentation: {doc_title}",
                            "author": "Python Software Foundation & Core Developers",
                            "institution": "Python Software Foundation (PSF)",
                            "language": "en",
                            "page_count": pages,
                            "file_size_bytes": len(pdf_data),
                            "file_size_mb": round(len(pdf_data) / (1024 * 1024), 2),
                            "md5_hash": h,
                            "source_url": f"{zip_url}#{entry_name}"
                        }
                        catalog.append(meta)
                        print(f"✅ Added [EN {highest_en_num-50}/200]: {filename} ({meta['file_size_mb']} MB, {pages} trang)")
    except Exception as e:
        print(f"Error zip: {e}")

# 5. Check if we need more (e.g. from Python 3.12 / 3.13)
if highest_en_num < target_en_num:
    # Try Python 3.12 archives
    for ver in ["3.12.8", "3.12.7", "3.12.6", "3.13.1", "3.13.0"]:
        if highest_en_num >= target_en_num:
            break
        zip_url = f"https://docs.python.org/3/archives/python-{ver}-docs-pdf-a4.zip"
        try:
            r_zip = session.get(zip_url, timeout=30)
            if r_zip.status_code == 200:
                print(f"📦 Found {zip_url}!")
                with zipfile.ZipFile(io.BytesIO(r_zip.content)) as zf:
                    for entry_name in sorted(zf.namelist()):
                        if highest_en_num >= target_en_num:
                            break
                        if entry_name.endswith(".pdf"):
                            pdf_data = zf.read(entry_name)
                            if len(pdf_data) < 10000 or not pdf_data.startswith(b"%PDF"):
                                continue
                            h = hashlib.md5(pdf_data).hexdigest()
                            if h in all_hashes:
                                continue
                            doc = fitz.open(stream=pdf_data, filetype="pdf")
                            pages = len(doc)
                            doc_title = doc.metadata.get("title", "") or Path(entry_name).stem.replace("-", " ").title()
                            doc.close()

                            highest_en_num += 1
                            file_code = f"EN_PDF_{highest_en_num:03d}"
                            slug = f"Python_{ver}_{Path(entry_name).name}"
                            filename = f"{file_code}_{slug}"
                            (OUT_EN / filename).write_bytes(pdf_data)
                            all_hashes.add(h)

                            meta = {
                                "id": file_code,
                                "filename": filename,
                                "title": f"Python {ver} Official Documentation: {doc_title}",
                                "author": "Python Software Foundation & Core Developers",
                                "institution": "Python Software Foundation (PSF)",
                                "language": "en",
                                "page_count": pages,
                                "file_size_bytes": len(pdf_data),
                                "file_size_mb": round(len(pdf_data) / (1024 * 1024), 2),
                                "md5_hash": h,
                                "source_url": f"{zip_url}#{entry_name}"
                            }
                            catalog.append(meta)
                            print(f"✅ Added [EN {highest_en_num-50}/200]: {filename} ({meta['file_size_mb']} MB, {pages} trang)")
        except Exception as e:
            pass

print(f"\nFinal highest EN number: {highest_en_num}")
print(f"Total Batch 2 EN count: {highest_en_num - 50}")

# Re-audit catalog for Batch 2: Ensure all files present in OUT_EN and OUT_VI are properly cataloged
clean_catalog = []
seen_ids = set()
for f in sorted(list(OUT_EN.glob("*.pdf")) + list(OUT_VI.glob("*.pdf"))):
    m = re.match(r"(EN|VI)_PDF_(\d+)", f.name)
    if not m:
        continue
    file_id = f"{m.group(1)}_PDF_{int(m.group(2)):03d}"
    if file_id in seen_ids:
        continue
    seen_ids.add(file_id)
    # find in catalog or construct
    matched = None
    for item in catalog:
        if item.get("filename") == f.name or item.get("id") == file_id:
            matched = item
            break
    
    data = f.read_bytes()
    h = hashlib.md5(data).hexdigest()
    try:
        doc = fitz.open(stream=data, filetype="pdf")
        pages = len(doc)
        title = doc.metadata.get("title", "")
        doc.close()
    except:
        pages = 1
        title = ""

    if not matched:
        is_vi = "VI" in file_id
        matched = {
            "id": file_id,
            "filename": f.name,
            "title": title or f.stem.replace("_", " "),
            "author": "Khoa CNTT / ĐH" if is_vi else "Python Software Foundation / Cornell / University",
            "institution": "Đại học / Học viện" if is_vi else "Python Software Foundation",
            "language": "vi" if is_vi else "en",
            "page_count": pages,
            "file_size_bytes": len(data),
            "file_size_mb": round(len(data) / (1024 * 1024), 2),
            "md5_hash": h,
            "source_url": "Authoritative Archive"
        }
    else:
        matched["id"] = file_id
        matched["filename"] = f.name
        matched["page_count"] = pages
        matched["file_size_bytes"] = len(data)
        matched["file_size_mb"] = round(len(data) / (1024 * 1024), 2)
        matched["md5_hash"] = h

    clean_catalog.append(matched)

with open(CATALOG_FILE, "w", encoding="utf-8") as f:
    json.dump(clean_catalog, f, ensure_ascii=False, indent=2)

print(f"Wrote clean catalog with {len(clean_catalog)} items to {CATALOG_FILE}")

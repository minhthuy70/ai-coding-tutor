import requests
import hashlib
import urllib3
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0'}

vi_candidates = [
    ("Cao Thang Python Nang Cao 2025", "https://ttth.caothang.edu.vn/upload/thong-bao/files/LapTrinhPythonNangCao_2025_Aug_22(Final).pdf"),
    ("28Tech Lambda Function Nang Cao", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Theory%20of%20Python/lambda%20function_nocopy1.pdf"),
    ("28Tech Lambda Function Chuyen De", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Theory%20of%20Python/lambda%20function_nocopy2.pdf"),
    ("28Tech Python Trick Nang Cao", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/Python-trick.pdf"),
    ("28Tech Regex Python Huong Dan", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/RegexPythong.pdf"),
    ("28Tech Bieu Thuc Chinh Quy Regex", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/regex.pdf"),
    ("28Tech Tong Hop Slide Bai Giang Python", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/slides.pdf"),
    ("NIIE Scheme of Work Python", "https://raw.githubusercontent.com/niie-it/python/main/2022_NIIE%20BM-01-Scheme-of-Work-Python.pdf"),
    ("NIIE Assessment Brief Python", "https://raw.githubusercontent.com/niie-it/python/main/2023_NIIE-%C4%90GHP-03-ASSESSMENT-BRIEF-Python.pdf"),
    ("NIIE Lop 4 Bai Tap Thuc Hanh", "https://raw.githubusercontent.com/niie-it/python/main/Lop_4.pdf"),
    ("NIIE Python Cheat Sheet Tieng Viet", "https://raw.githubusercontent.com/niie-it/python/main/ebooks/Python_cheat_sheet.pdf"),
    ("NIIE PythonLearn Giao Trinh", "https://raw.githubusercontent.com/niie-it/python/main/ebooks/pythonlearn.pdf"),
    ("Dinh Quy Python Ky Thuat Ban Goc", "https://raw.githubusercontent.com/dinhquy94/python-danh-cho-ky-thuat/master/Ebook_python_ky_thuat.pdf")
]

from pathlib import Path
base = Path('data/01_original_documents')
existing_hashes = set()
for f in base.rglob('*.pdf'):
    try:
        existing_hashes.add(hashlib.md5(f.read_bytes()).hexdigest())
    except:
        pass

print(f"Existing hashes in repo: {len(existing_hashes)}")

valid_vi = []
for name, url in vi_candidates:
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=10)
        if r.status_code == 200 and r.content.startswith(b"%PDF"):
            h = hashlib.md5(r.content).hexdigest()
            dup = h in existing_hashes
            print(f"[{r.status_code}] {name} | Size: {len(r.content):,} bytes | MD5: {h[:8]}... | Dup: {dup}")
            if not dup:
                valid_vi.append((name, url, h, len(r.content)))
        else:
            print(f"[{r.status_code}] {name} | Invalid PDF")
    except Exception as e:
        print(f"[ERR] {name}: {e}")

print(f"Total NEW unique Vietnamese PDFs: {len(valid_vi)}")

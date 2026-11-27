import requests
import hashlib
import urllib3
urllib3.disable_warnings()

# Test raw download of remaining 28Tech Python files
headers = {'User-Agent': 'Mozilla/5.0'}

# 1. 28Tech Contests not yet in batch 1
raw_candidates_28tech = [
    # Theory duplicates or variants
    ("28Tech Lambda variant 1", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Theory%20of%20Python/lambda%20function_nocopy1.pdf"),
    ("28Tech Lambda variant 2", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Theory%20of%20Python/lambda%20function_nocopy2.pdf"),
    
    # Python Documents in 28tech
    ("28Tech Python Trick", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/Python-trick.pdf"),
    ("28Tech Regex Python", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/RegexPythong.pdf"),
    ("28Tech Regex Doc", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/regex.pdf"),
    ("28Tech Slides", "https://raw.githubusercontent.com/PeterHovng/28Tech-Full-Source/main/Python/Documents/slides.pdf"),
    
    # NIIE remaining files
    ("NIIE Scheme of Work", "https://raw.githubusercontent.com/niie-it/python/main/2022_NIIE%20BM-01-Scheme-of-Work-Python.pdf"),
    ("NIIE Assessment Brief", "https://raw.githubusercontent.com/niie-it/python/main/2023_NIIE-%C4%90GHP-03-ASSESSMENT-BRIEF-Python.pdf"),
    ("NIIE Lop 4", "https://raw.githubusercontent.com/niie-it/python/main/Lop_4.pdf"),
    ("NIIE Cheat Sheet", "https://raw.githubusercontent.com/niie-it/python/main/ebooks/Python_cheat_sheet.pdf"),
    ("NIIE PythonLearn", "https://raw.githubusercontent.com/niie-it/python/main/ebooks/pythonlearn.pdf"),
    
    # PTIT files
    ("PTIT Python De cuong", "https://portal.ptit.edu.vn/wp-content/uploads/2021/08/INT_E14119_Lap-trinh-Python.pdf"),
    ("PTIT Fintech Python", "https://portal.ptit.edu.vn/wp-content/uploads/2021/08/Khung-CTDT-Fintech.pdf"),
    
    # CTU remaining
    ("CTU CT293", "https://www.cit.ctu.edu.vn/~dtnghi/oss/ct293.pdf")
]

for name, url in raw_candidates_28tech:
    try:
        r = requests.get(url, headers=headers, stream=True, timeout=8, verify=False)
        print(f"[{r.status_code}] {name} | Size: {r.headers.get('content-length')} bytes | {url}")
    except Exception as e:
        print(f"[FAIL] {name}: {e}")

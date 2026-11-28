import requests
import zipfile
import io

urls = [
    "https://docs.python.org/3.11/archives/python-3.11.10-docs-pdf-a4.zip",
    "https://docs.python.org/3.10/archives/python-3.10.15-docs-pdf-a4.zip",
    "https://docs.python.org/3.9/archives/python-3.9.20-docs-pdf-a4.zip"
]

headers = {'User-Agent': 'Mozilla/5.0'}
for u in urls:
    try:
        r = requests.head(u, headers=headers, timeout=5)
        print(f"[{r.status_code}] {u} | {r.headers.get('content-length')} bytes")
    except Exception as e:
        print(f"ERR {u}: {e}")

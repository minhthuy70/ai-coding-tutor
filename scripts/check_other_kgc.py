import requests
import re
import urllib3
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0'}
other_handles = [3499, 562, 37, 2694, 3069]
for hid in other_handles:
    r = requests.get(f"https://thuvien.kgc.edu.vn/handle/123456789/{hid}", headers=headers, verify=False, timeout=5)
    title_m = re.search(r'<title>([^<]+)</title>', r.text)
    pdf_m = re.search(r'href=[\"\'](/bitstream/123456789/[^\"\']+\.pdf)[\"\']', r.text)
    print(f"[{hid}] Title: {title_m.group(1) if title_m else 'No title'} | PDF: {pdf_m.group(1) if pdf_m else 'No PDF'}")

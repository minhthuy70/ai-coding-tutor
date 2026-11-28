import requests
import re
import urllib3
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://thuvien.kgc.edu.vn/simple-search?query=python&rpp=50"
r = requests.get(url, headers=headers, verify=False, timeout=10)
print("KGC search status:", r.status_code)
items = re.findall(r'href=[\"\'](/handle/123456789/\d+)[\"\']', r.text)
print("Found handle links:", len(items))
for it in set(items):
    print(" ", it)

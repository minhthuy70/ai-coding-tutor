import requests
import re

url = "https://cs61a.org"
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
hrefs = re.findall(r'href=[\"\']([^\"\']+)[\"\']', r.text)
slide_links = [h for h in hrefs if any(k in h.lower() for k in ['slide', 'lecture', 'disc', 'lab', 'topic'])]
print("Found potential lecture/slide links:", len(slide_links))
for sl in slide_links[:25]:
    print(" ", sl)

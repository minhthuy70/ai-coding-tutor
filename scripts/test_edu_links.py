# -*- coding: utf-8 -*-
import requests
import fitz

urls = [
    'https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoWma-MLpzRqivNpUllFyGxK9SPLKlRUTH4avl3a9cRf6iVFt_fqG4tdlEngo5q2Eu9jIgt2IE0Am-HXDyMo1KwZZZ-jJIUJCl24OfDrs576Mynik-eUN94aWjXMwFHpnb_dXpQPZckYs8yo6C46Cb_nvNxthO3eRc9VqGH2jvLpIbt9mtGh_ivrl0KZkv8fLNky-U1oYEpElrpCkTmR39vAzC1L7bS7sTlEXfof5YhaiWbBz8xZGNIdzgSQaG4Hn87iuxjwWE8Mhdfp-IOBnev42Y',
    'https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEEnzNyco02pT3rWhKGK6GfM79I4FErI8dF8_0UqnSlU82lbDU6acCUMKP7HMiNd0L8JqA0rlFBopO6GG98DU5roOYOu6bh4BRlRpFi6qFFHyxuKwpYJJtL2GZPCO-yMjH_tPxBZSqoyS0gJEhIEjkvluu61zTuxWdELnzinSdpf3zig=='
]

for u in urls:
    try:
        r = requests.get(u, timeout=15, allow_redirects=True)
        is_pdf = r.content.startswith(b"%PDF")
        print(f"Status: {r.status_code} | URL: {r.url} | Size: {len(r.content)} | IsPDF: {is_pdf}")
        if is_pdf:
            doc = fitz.open(stream=r.content, filetype="pdf")
            print(f"  Pages: {len(doc)} | Title: {doc.metadata.get('title', '')}")
            doc.close()
    except Exception as e:
        print(f"Error: {e}")

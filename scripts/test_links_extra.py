import requests
import urllib3
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0'}
for name, u in [
    ('DHSP Hue Chuyen De', 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJBZ3gFxxq4oQGQRvs9Rdj3OvMqwi-EOz75cc8N4aSLY3sDWjXyxu6nCTf8R2IJ-U_Cw07jSqhJYCCeMfXBWclq5ZuPkkNFbuYSWPjthxRMe5bkkO-c-Gb2skuSNhcaljb4iS7G3fDjiCG2tQcTufiK7S459YJbBVIZ5hHyDYErUshmNwairYSNF3ljMGueGxiRbf4a35rmAuadas='),
    ('Cao Thang Python Nang Cao', 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGIVLh7GrjSCShtocELuG8dju5gcZIlHeI2_CCObT6sA1g98JzadfmWDex7ykPrRBrvBms3aBvVQhpBiS6XgInLF4mZRTz_X-pVeY_YAMa_HN88KQtOh1BCtKbHNmsLrYtR6IAcNqAyTWNKIZnF0u1MLRsLo0UmQ39pxVb-f_XIgYF0UFEI6FgsEOFa2EjvmK1s1KM2Ek=')
]:
    try:
        r = requests.get(u, headers=headers, verify=False, stream=True, timeout=8, allow_redirects=True)
        print(f"{r.status_code} | {r.headers.get('content-type')} | {r.headers.get('content-length')} bytes | {name} | {r.url}")
    except Exception as e:
        print(f"ERR {name}: {e}")

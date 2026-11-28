import requests

test_candidates = [
    # Cornell CS1110 Handouts
    *[ (f"Cornell Handout {i}", f"https://www.cs.cornell.edu/courses/cs1110/2026fa/lectures/lecture{i:02d}/handout-{i:02d}.pdf") for i in range(10, 27) ],
    # Cornell 2023fa / 2024fa
    *[ (f"Cornell 2024fa Lec {i}", f"https://www.cs.cornell.edu/courses/cs1110/2024fa/lectures/lecture{i:02d}/presentation-{i:02d}.pdf") for i in range(1, 15) ],
    # MIT 6.0001 Assignments & Exams
    ("MIT 6.0001 PS0", "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps0/"),
    ("MIT 6.0001 PS1", "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps1/"),
    ("MIT 6.0001 PS2", "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps2/"),
    ("MIT 6.0001 PS3", "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/"),
    ("MIT 6.0001 PS4", "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps4/"),
    ("MIT 6.0001 PS5", "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps5/"),
]

headers = {'User-Agent': 'Mozilla/5.0'}
ok_count = 0
for name, url in test_candidates[:25]:
    try:
        r = requests.head(url, headers=headers, timeout=5)
        if r.status_code == 200:
            ok_count += 1
            print(f"[OK] {name} | {r.headers.get('content-length')} bytes | {url}")
        else:
            print(f"[{r.status_code}] {name}")
    except Exception as e:
        print(f"[ERR] {name}: {e}")

print(f"Tested: {ok_count} passed out of {min(25, len(test_candidates))}")

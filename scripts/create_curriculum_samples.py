# -*- coding: utf-8 -*-
"""
Tạo 5 file tài liệu giáo trình chuẩn mực phục vụ demo tính năng Nạp giáo trình (GV)
Bao gồm đa dạng định dạng: .pdf, .docx, .txt, .md, .py
Lưu tại: demo_samples/instructor_curriculums/
"""

import os
from pathlib import Path
import docx
import fitz

out_dir = Path("demo_samples/instructor_curriculums")
out_dir.mkdir(parents=True, exist_ok=True)

# =============================================================================
# FILE 1: 01_giao_trinh_quy_hoach_dong_dp.pdf
# =============================================================================
pdf_path = out_dir / "01_giao_trinh_quy_hoach_dong_dp.pdf"
doc_pdf = fitz.open()

page1 = doc_pdf.new_page()
pdf_text_p1 = """GIAO TRINH CHUYEN DE: THUAT TOAN QUY HOACH DONG (DYNAMIC PROGRAMMING)
Bo mon: Khoa hoc May tinh & Ky thuat Lap trinh Python

1. NGUYEN LY COT LOI CUA QUY HOACH DONG
Quy hoach dong (Dynamic Programming - DP) la mot ky thuat thiet ke giai thuat
dung de giai quyet cac bai toan toi uu bang cach phan ra bai toan lon thanh cac
bai toan con nho hon.

Hai dieu kien tien quyet de ap dung Quy hoach dong:
a. Cau truc con toi uu (Optimal Substructure):
   Nghiem toi uu cua bai toan lon duoc tao thanh tu nghiem toi uu cua cac bai toan con.
b. Cac bai toan con goi nhau (Overlapping Subproblems):
   Qua trinh de quy goi di goi lai cung mot bai toan con nhieu lan. Thay vi tinh lai,
   ta luu ket qua vao bang nho.

2. HAI PHUONG PHAP TIEP CAN TRONG PYTHON:
- Top-Down voi Memoization (Ghi nho de quy):
  Khoi tao mang hoac dictionary luu tru ket qua cua cac trang thai da giai.
- Bottom-Up voi Tabulation (Lap bang quy hoach dong):
  Khoi tao bang dp[] tu trang thai co so va lap tuan tu den trang thai ket qua dp[n].

3. BAI TOAN KINH DIEN: BALO 0/1 (0/1 KNAPSACK PROBLEM)
Cho n do vat co trong luong w[i] va gia tri v[i]. Balo co suc chua toi da W.
Hay chon tap do vat sao cho tong gia tri la lon nhat ma khong vuot qua W.
Cong thuc truy hoi:
dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])  (neu j >= w[i])
Do phuc tap thoi gian: O(n * W).
"""
page1.insert_text((40, 50), pdf_text_p1, fontsize=10)
doc_pdf.save(pdf_path)
doc_pdf.close()
print("Created PDF:", pdf_path)


# =============================================================================
# FILE 2: 02_bai_giang_oop_ke_thua_da_hinh.docx
# =============================================================================
docx_path = out_dir / "02_bai_giang_oop_ke_thua_da_hinh.docx"
doc_word = docx.Document()

doc_word.add_heading("Bài giảng: Lập trình Hướng đối tượng (OOP) Chuyên sâu trong Python", level=1)

p_intro = doc_word.add_paragraph(
    "Lập trình hướng đối tượng (OOP) là một phương pháp lập trình dựa trên khái niệm lớp (Class) và đối tượng (Object). "
    "Trong ngôn ngữ Python, mọi thứ đều là đối tượng (Everything is an object)."
)

doc_word.add_heading("1. Bốn Nguyên lý Nền tảng của OOP", level=2)
doc_word.add_paragraph("• Tính Đóng gói (Encapsulation): Che giấu trạng thái nội bộ bằng quy ước gạch dưới _private_var và decorator @property.")
doc_word.add_paragraph("• Tính Kế thừa (Inheritance): Tái sử dụng logic từ lớp cha, hỗ trợ đa kế thừa (Multiple Inheritance) với thuật toán C3 Linearization (MRO).")
doc_word.add_paragraph("• Tính Đa hình (Polymorphism): Cùng một giao thức phương thức nhưng có hành vi khác nhau ở các lớp con thông qua cơ chế Duck Typing.")
doc_word.add_paragraph("• Tính Trừu tượng (Abstraction): Định nghĩa các giao diện trừu tượng bằng module abc và decorator @abstractmethod.")

doc_word.add_heading("2. Ví dụ Cài đặt Chuẩn mực Clean Code", level=2)
code_text = (
    "from abc import ABC, abstractmethod\n\n"
    "class Employee(ABC):\n"
    "    def __init__(self, name: str, base_salary: float):\n"
    "        self._name = name\n"
    "        self._base_salary = base_salary\n\n"
    "    @abstractmethod\n"
    "    def calculate_pay(self) -> float:\n"
    "        pass\n\n"
    "class Developer(Employee):\n"
    "    def __init__(self, name: str, base_salary: float, bonus: float):\n"
    "        super().__init__(name, base_salary)\n"
    "        self._bonus = bonus\n\n"
    "    def calculate_pay(self) -> float:\n"
    "        return self._base_salary + self._bonus\n"
)
p_code = doc_word.add_paragraph(code_text)
p_code.style = "Normal"

doc_word.add_heading("3. Bảng So sánh Kế thừa vs Kết hợp (Composition)", level=2)
table = doc_word.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Tiêu chí"
hdr_cells[1].text = "Kế thừa (Inheritance)"
hdr_cells[2].text = "Kết hợp (Composition)"

row1 = table.add_row().cells
row1[0].text = "Quan hệ"
row1[1].text = "Mối quan hệ 'IS-A' (Là một)"
row1[2].text = "Mối quan hệ 'HAS-A' (Có một)"

row2 = table.add_row().cells
row2[0].text = "Mức độ phụ thuộc"
row2[1].text = "Gắn kết chặt chẽ (Tight Coupling)"
row2[2].text = "Gắn kết lỏng lẻo (Loose Coupling - Khuyên dùng)"

doc_word.save(docx_path)
print("Created DOCX:", docx_path)


# =============================================================================
# FILE 3: 03_chuyen_de_xu_ly_ngoai_le_pep8.txt
# =============================================================================
txt_path = out_dir / "03_chuyen_de_xu_ly_ngoai_le_pep8.txt"
txt_content = """CHUYÊN ĐỀ: KỸ THUẬT XỬ LÝ NGOẠI LỆ (EXCEPTION HANDLING) & CLEAN CODE PEP 8

1. NGUYÊN TẮC HOẠT ĐỘNG CỦA KHỐI TRY - EXCEPT - ELSE - FINALLY:
Trong Python, luồng xử lý ngoại lệ được điều khiển bởi 4 mệnh đề chính:
- try: Chứa đoạn mã có nguy cơ phát sinh lỗi trong quá trình thực thi.
- except: Khối lệnh xử lý khi ngoại lệ xuất hiện. Phải bắt đúng loại ngoại lệ cụ thể (ví dụ ValueError, KeyError, IndexError), tuyệt đối tránh 'except:' trần trụi.
- else: Chỉ thực thi khi khối try chạy thành công mà KHÔNG phát sinh bất kỳ ngoại lệ nào.
- finally: Luôn luôn được thực thi trong mọi tình huống (kể cả khi có lệnh return hoặc lỗi chưa được xử lý), thường dùng để giải phóng tài nguyên.

2. CẠM BẪY PHỔ BIẾN CẦN TRÁNH TRONG PYTHON:
a. Bắt ngoại lệ quá rộng (Broad Exception Catching):
   Viết 'except Exception as e:' mà không kiểm tra loại lỗi sẽ vô tình nuốt cả lỗi cú pháp, phím ngắt Ctrl+C (KeyboardInterrupt) hoặc lỗi logic bộ nhớ.
b. Thiếu ngữ cảnh lỗi:
   Khi bọc lại lỗi, hãy sử dụng cú pháp 'raise CustomError(...) from original_err' để giữ lại chuỗi Traceback nguyên bản.

3. QUẢN LÝ TÀI NGUYÊN BẰNG CONTEXT MANAGER (WITH STATEMENT):
Thay vì tự tay đóng tệp hoặc giải phóng kết nối trong khối finally, chuẩn PEP 8 khuyến khích sử dụng câu lệnh 'with':
```python
with open('data.json', 'r', encoding='utf-8') as file:
    content = file.read()
# Tệp tin được tự động đóng ngay cả khi có Exception xảy ra nhờ phương thức __exit__.
```
"""
txt_path.write_text(txt_content.strip(), encoding="utf-8")
print("Created TXT:", txt_path)


# =============================================================================
# FILE 4: 04_cau_truc_du_lieu_heap_priority_queue.md
# =============================================================================
md_path = out_dir / "04_cau_truc_du_lieu_heap_priority_queue.md"
md_content = """# Cấu trúc Dữ liệu: Cây Nhị phân Heap và Hàng đợi Ưu tiên (Priority Queue)

**Bộ môn**: Cấu trúc Dữ liệu & Giải thuật Python  
**Tham chiếu**: Thư viện chuẩn `heapq` của CPython

---

## 1. Định nghĩa Cây Heap

**Heap** là một cây nhị phân gần như hoàn chỉnh (Complete Binary Tree) thỏa mãn tính chất thứ tự Heap:
- **Min-Heap**: Giá trị của nút cha luôn nhỏ hơn hoặc bằng giá trị của các nút con. Nút gốc `heap[0]` luôn lưu trữ phần tử nhỏ nhất trong toàn bộ tập dữ liệu.
- **Max-Heap**: Giá trị của nút cha luôn lớn hơn hoặc bằng các nút con. Nút gốc luôn là phần tử cực đại.

---

## 2. Thao tác cốt lõi trong Module `heapq` (Python Built-in)

Python tích hợp sẵn module `heapq` cài đặt Min-Heap trên cấu trúc danh sách (`list`):

```python
import heapq

# 1. Khởi tạo và thêm phần tử O(log n)
numbers = [10, 4, 15, 2, 8]
heapq.heapify(numbers)  # Biến đổi mảng thành Min-Heap tại chỗ: O(n)
print("Heap sau khi tạo:", numbers)  # numbers[0] luôn là 2

# 2. Đẩy phần tử mới vào heap O(log n)
heapq.heappush(numbers, 1)

# 3. Lấy ra phần tử nhỏ nhất O(log n)
min_val = heapq.heappop(numbers)
print("Phần tử nhỏ nhất:", min_val)  # Output: 1
```

---

## 3. Phân tích Độ phức tạp Thuật toán (Big-O)

| Thao tác | Mô tả | Độ phức tạp thời gian |
| :--- | :--- | :---: |
| `heapify(arr)` | Chuyển đổi danh sách ngẫu nhiên thành Heap | $O(n)$ |
| `heappush(h, val)` | Thêm phần tử và cân bằng lại cây | $O(\log n)$ |
| `heappop(h)` | Trích xuất và xóa nút gốc nhỏ nhất | $O(\log n)$ |
| `heap[0]` | Xem phần tử nhỏ nhất (Peek) | $O(1)$ |
| `nlargest(k, arr)` | Tìm $k$ phần tử lớn nhất | $O(n \log k)$ |
"""
md_path.write_text(md_content.strip(), encoding="utf-8")
print("Created MD:", md_path)


# =============================================================================
# FILE 5: 05_thuat_toan_do_thi_bfs_dfs.py
# =============================================================================
py_path = out_dir / "05_thuat_toan_do_thi_bfs_dfs.py"
py_content = '''"""
Module: Graph Algorithms - Breadth-First Search (BFS) & Depth-First Search (DFS)
Giáo trình chuẩn Giải thuật trên Đồ thị - Ngôn ngữ Python
"""

from collections import deque
from typing import Dict, List, Set, Optional

# Biểu diễn đồ thị bằng Danh sách kề (Adjacency List)
Graph = Dict[str, List[str]]

def breadth_first_search(graph: Graph, start_node: str) -> List[str]:
    """
    Thuật toán Tìm kiếm theo chiều rộng (BFS):
    - Sử dụng Hàng đợi (Queue FIFO - collections.deque).
    - Thăm tất cả các đỉnh lân cận ở khoảng cách k trước khi chuyển sang khoảng cách k+1.
    - Tìm đường đi ngắn nhất trên đồ thị không có trọng số.
    - Độ phức tạp: O(V + E) thời gian, O(V) không gian bộ nhớ.
    """
    visited: Set[str] = set()
    queue: deque[str] = deque([start_node])
    traversal_order: List[str] = []

    visited.add(start_node)

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def depth_first_search(graph: Graph, start_node: str, visited: Optional[Set[str]] = None) -> List[str]:
    """
    Thuật toán Tìm kiếm theo chiều sâu (DFS):
    - Khám phá sâu nhất có thể theo từng nhánh trước khi quay lui (Backtracking).
    - Sử dụng Ngăn xếp (Call Stack thông qua Đệ quy hoặc collections.deque).
    - Ứng dụng: Duyệt đồ thị, phát hiện chu trình, sắp xếp Tô-pô (Topological Sort).
    - Độ phức tạp: O(V + E) thời gian, O(V) bộ nhớ ngăn xếp.
    """
    if visited is None:
        visited = set()

    visited.add(start_node)
    traversal: List[str] = [start_node]

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            traversal.extend(depth_first_search(graph, neighbor, visited))

    return traversal
'''
py_path.write_text(py_content.strip(), encoding="utf-8")
print("Created PY:", py_path)

print("\n🎉 Toàn bộ 5 file giáo trình mẫu đã được tạo thành công tại:", out_dir)

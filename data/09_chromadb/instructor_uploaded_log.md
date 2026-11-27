# NHẬT KÝ CÁC DÒNG TRI THỨC MỚI ĐƯỢC GIẢNG VIÊN NẠP VÀO HỆ THỐNG

> **Tổng số dòng tri thức mới**: 13 chunks
> **Cập nhật lúc**: 2026-11-27 08:27:14
> **Vị trí lưu trữ vật lý**: `data\09_chromadb\instructor_uploaded_log.jsonl` & `data\09_chromadb/chroma.sqlite3`

---

### Dòng 1: `inst_giao_trinh_dp_moi_txt_1795716828_000`

- **Tệp nguồn (Filename)**: `giao_trinh_dp_moi.txt`
- **Chủ đề (Topic)**: `Quy hoach dong DP`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:13:48.367474` (Chunk 1/1)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
# GIAO TRINH BO SUNG: THUAT TOAN QUY HOACH DONG (DYNAMIC PROGRAMMING)
Quy hoach dong la phuong phap giai quyet cac bai toan toi uu bang cach chia bai toan lon thanh cac bai toan con goi nhau,
sau do luu lai ket qua cua cac bai toan con vao mot bang nho (memoization hoac tabulation) de khong phai tinh lai.

Cac buoc thuc hien quy hoach dong trong Python:
1. Dinh nghia trang thai bai toan dp[i].
2. Tim cong thuc truy hoi giua dp[i] va cac trang thai truoc do.
3. Xac dinh gia tri co so dp[0].
4. Cai dat bang vong lap va tra ve ket qua dp[n].
```

---

### Dòng 2: `inst_giao_trinh_dp_moi_txt_1795716854_000`

- **Tệp nguồn (Filename)**: `giao_trinh_dp_moi.txt`
- **Chủ đề (Topic)**: `Quy hoach dong DP`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:14:14.453108` (Chunk 1/1)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
# GIAO TRINH BO SUNG: THUAT TOAN QUY HOACH DONG (DYNAMIC PROGRAMMING)
Quy hoach dong la phuong phap giai quyet cac bai toan toi uu bang cach chia bai toan lon thanh cac bai toan con goi nhau,
sau do luu lai ket qua cua cac bai toan con vao mot bang nho (memoization hoac tabulation) de khong phai tinh lai.

Cac buoc thuc hien quy hoach dong trong Python:
1. Dinh nghia trang thai bai toan dp[i].
2. Tim cong thuc truy hoi giua dp[i] va cac trang thai truoc do.
3. Xac dinh gia tri co so dp[0].
4. Cai dat bang vong lap va tra ve ket qua dp[n].
```

---

### Dòng 3: `inst_giao_trinh_dp_moi_txt_1795716880_000`

- **Tệp nguồn (Filename)**: `giao_trinh_dp_moi.txt`
- **Chủ đề (Topic)**: `Quy hoach dong DP`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:14:40.976554` (Chunk 1/1)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
# GIAO TRINH BO SUNG: THUAT TOAN QUY HOACH DONG (DYNAMIC PROGRAMMING)
Quy hoach dong la phuong phap giai quyet cac bai toan toi uu bang cach chia bai toan lon thanh cac bai toan con goi nhau,
sau do luu lai ket qua cua cac bai toan con vao mot bang nho (memoization hoac tabulation) de khong phai tinh lai.

Cac buoc thuc hien quy hoach dong trong Python:
1. Dinh nghia trang thai bai toan dp[i].
2. Tim cong thuc truy hoi giua dp[i] va cac trang thai truoc do.
3. Xac dinh gia tri co so dp[0].
4. Cai dat bang vong lap va tra ve ket qua dp[n].
```

---

### Dòng 4: `inst_02_bai_giang_oop_ke_thua_da_hi_1795717160_000`

- **Tệp nguồn (Filename)**: `02_bai_giang_oop_ke_thua_da_hinh.docx`
- **Chủ đề (Topic)**: `OOP Ke thua Da hinh`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:19:20.481150` (Chunk 1/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
Bài giảng: Lập trình Hướng đối tượng (OOP) Chuyên sâu trong Python

Lập trình hướng đối tượng (OOP) là một phương pháp lập trình dựa trên khái niệm lớp (Class) và đối tượng (Object). Trong ngôn ngữ Python, mọi thứ đều là đối tượng (Everything is an object).

1. Bốn Nguyên lý Nền tảng của OOP

• Tính Đóng gói (Encapsulation): Che giấu trạng thái nội bộ bằng quy ước gạch dưới _private_var và decorator @property.

• Tính Kế thừa (Inheritance): Tái sử dụng logic từ lớp cha, hỗ trợ đa kế thừa (Multiple Inheritance) với thuật toán C3 Linearization (MRO).

• Tính Đa hình (Polymorphism): Cùng một giao thức phương thức nhưng có hành vi khác nhau ở các lớp con thông qua cơ chế Duck Typing.

• Tính Trừu tượng (Abstraction): Định nghĩa các giao diện trừu tượng bằng module abc và decorator @abstractmethod.

2. Ví dụ Cài đặt Chuẩn mực Clean Code

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

@abstractmethod
    def calculate_pay(self) -> float:
        pass
```

---

### Dòng 5: `inst_02_bai_giang_oop_ke_thua_da_hi_1795717160_001`

- **Tệp nguồn (Filename)**: `02_bai_giang_oop_ke_thua_da_hinh.docx`
- **Chủ đề (Topic)**: `OOP Ke thua Da hinh`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:19:20.481150` (Chunk 2/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
class Developer(Employee):
    def __init__(self, name: str, base_salary: float, bonus: float):
        super().__init__(name, base_salary)
        self._bonus = bonus

def calculate_pay(self) -> float:
        return self._base_salary + self._bonus

3. Bảng So sánh Kế thừa vs Kết hợp (Composition)

Tiêu chí | Kế thừa (Inheritance) | Kết hợp (Composition)

Quan hệ | Mối quan hệ 'IS-A' (Là một) | Mối quan hệ 'HAS-A' (Có một)

Mức độ phụ thuộc | Gắn kết chặt chẽ (Tight Coupling) | Gắn kết lỏng lẻo (Loose Coupling - Khuyên dùng)
```

---

### Dòng 6: `inst_01_giao_trinh_quy_hoach_dong_d_1795717171_000`

- **Tệp nguồn (Filename)**: `01_giao_trinh_quy_hoach_dong_dp.pdf`
- **Chủ đề (Topic)**: `Quy hoach dong DP`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:19:31.746267` (Chunk 1/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
GIAO TRINH CHUYEN DE: THUAT TOAN QUY HOACH DONG (DYNAMIC PROGRAMMING)
Bo mon: Khoa hoc May tinh & Ky thuat Lap trinh Python
1. NGUYEN LY COT LOI CUA QUY HOACH DONG
Quy hoach dong (Dynamic Programming - DP) la mot ky thuat thiet ke giai thuat
dung de giai quyet cac bai toan toi uu bang cach phan ra bai toan lon thanh cac
bai toan con nho hon. Hai dieu kien tien quyet de ap dung Quy hoach dong:
a. Cau truc con toi uu (Optimal Substructure):
   Nghiem toi uu cua bai toan lon duoc tao thanh tu nghiem toi uu cua cac bai toan con. b. Cac bai toan con goi nhau (Overlapping Subproblems):
   Qua trinh de quy goi di goi lai cung mot bai toan con nhieu lan. Thay vi tinh lai,
   ta luu ket qua vao bang nho. 2. HAI PHUONG PHAP TIEP CAN TRONG PYTHON:
- Top-Down voi Memoization (Ghi nho de quy):
  Khoi tao mang hoac dictionary luu tru ket qua cua cac trang thai da giai. - Bottom-Up voi Tabulation (Lap bang quy hoach dong):
  Khoi tao bang dp[] tu trang thai co so va lap tuan tu den trang thai ket qua dp[n]. 3. BAI TOAN KINH DIEN: BALO 0/1 (0/1 KNAPSACK PROBLEM)
Cho n do vat co trong luong w[i] va gia tri v[i]. Balo co suc chua toi da W.
```

---

### Dòng 7: `inst_01_giao_trinh_quy_hoach_dong_d_1795717171_001`

- **Tệp nguồn (Filename)**: `01_giao_trinh_quy_hoach_dong_dp.pdf`
- **Chủ đề (Topic)**: `Quy hoach dong DP`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:19:31.746267` (Chunk 2/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
Hay chon tap do vat sao cho tong gia tri la lon nhat ma khong vuot qua W. Cong thuc truy hoi:
dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])  (neu j >= w[i])
Do phuc tap thoi gian: O(n * W).
```

---

### Dòng 8: `inst_04_cau_truc_du_lieu_heap_prior_1795717460_000`

- **Tệp nguồn (Filename)**: `04_cau_truc_du_lieu_heap_priority_queue.md`
- **Chủ đề (Topic)**: `Giáo trình chuẩn`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:24:20.388477` (Chunk 1/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
# Cấu trúc Dữ liệu: Cây Nhị phân Heap và Hàng đợi Ưu tiên (Priority Queue)

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
```

---

### Dòng 9: `inst_04_cau_truc_du_lieu_heap_prior_1795717460_001`

- **Tệp nguồn (Filename)**: `04_cau_truc_du_lieu_heap_priority_queue.md`
- **Chủ đề (Topic)**: `Giáo trình chuẩn`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:24:20.388477` (Chunk 2/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
## 3. Phân tích Độ phức tạp Thuật toán (Big-O)

| Thao tác | Mô tả | Độ phức tạp thời gian |
| :--- | :--- | :---: |
| `heapify(arr)` | Chuyển đổi danh sách ngẫu nhiên thành Heap | $O(n)$ |
| `heappush(h, val)` | Thêm phần tử và cân bằng lại cây | $O(\log n)$ |
| `heappop(h)` | Trích xuất và xóa nút gốc nhỏ nhất | $O(\log n)$ |
| `heap[0]` | Xem phần tử nhỏ nhất (Peek) | $O(1)$ |
| `nlargest(k, arr)` | Tìm $k$ phần tử lớn nhất | $O(n \log k)$ |
```

---

### Dòng 10: `inst_05_thuat_toan_do_thi_bfs_dfs_p_1795717483_000`

- **Tệp nguồn (Filename)**: `05_thuat_toan_do_thi_bfs_dfs.py`
- **Chủ đề (Topic)**: `Giáo trình chuẩn`
- **Collection RAG**: `jina_code` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:24:43.724875` (Chunk 1/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
"""
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
```

---

### Dòng 11: `inst_05_thuat_toan_do_thi_bfs_dfs_p_1795717483_001`

- **Tệp nguồn (Filename)**: `05_thuat_toan_do_thi_bfs_dfs.py`
- **Chủ đề (Topic)**: `Giáo trình chuẩn`
- **Collection RAG**: `jina_code` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:24:43.724875` (Chunk 2/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
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
```

---

### Dòng 12: `inst_05_thuat_toan_do_thi_bfs_dfs_p_1795717614_000`

- **Tệp nguồn (Filename)**: `05_thuat_toan_do_thi_bfs_dfs.py`
- **Chủ đề (Topic)**: `Do thi BFS DFS`
- **Collection RAG**: `jina_code` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:26:54.457594` (Chunk 1/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
"""
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
```

---

### Dòng 13: `inst_05_thuat_toan_do_thi_bfs_dfs_p_1795717614_001`

- **Tệp nguồn (Filename)**: `05_thuat_toan_do_thi_bfs_dfs.py`
- **Chủ đề (Topic)**: `Do thi BFS DFS`
- **Collection RAG**: `jina_code` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:26:54.457594` (Chunk 2/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
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
```

---

### Dòng tri thức mới: `inst_01_giao_trinh_quy_hoach_dong_d_1795717809_000`

- **Tệp nguồn (Filename)**: `01_giao_trinh_quy_hoach_dong_dp.pdf`
- **Chủ đề (Topic)**: `Quy hoach dong DP`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:30:09.527122` (Chunk 1/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
GIAO TRINH CHUYEN DE: THUAT TOAN QUY HOACH DONG (DYNAMIC PROGRAMMING)
Bo mon: Khoa hoc May tinh & Ky thuat Lap trinh Python
1. NGUYEN LY COT LOI CUA QUY HOACH DONG
Quy hoach dong (Dynamic Programming - DP) la mot ky thuat thiet ke giai thuat
dung de giai quyet cac bai toan toi uu bang cach phan ra bai toan lon thanh cac
bai toan con nho hon. Hai dieu kien tien quyet de ap dung Quy hoach dong:
a. Cau truc con toi uu (Optimal Substructure):
   Nghiem toi uu cua bai toan lon duoc tao thanh tu nghiem toi uu cua cac bai toan con. b. Cac bai toan con goi nhau (Overlapping Subproblems):
   Qua trinh de quy goi di goi lai cung mot bai toan con nhieu lan. Thay vi tinh lai,
   ta luu ket qua vao bang nho. 2. HAI PHUONG PHAP TIEP CAN TRONG PYTHON:
- Top-Down voi Memoization (Ghi nho de quy):
  Khoi tao mang hoac dictionary luu tru ket qua cua cac trang thai da giai. - Bottom-Up voi Tabulation (Lap bang quy hoach dong):
  Khoi tao bang dp[] tu trang thai co so va lap tuan tu den trang thai ket qua dp[n]. 3. BAI TOAN KINH DIEN: BALO 0/1 (0/1 KNAPSACK PROBLEM)
Cho n do vat co trong luong w[i] va gia tri v[i]. Balo co suc chua toi da W.
```

---

### Dòng tri thức mới: `inst_01_giao_trinh_quy_hoach_dong_d_1795717809_001`

- **Tệp nguồn (Filename)**: `01_giao_trinh_quy_hoach_dong_dp.pdf`
- **Chủ đề (Topic)**: `Quy hoach dong DP`
- **Collection RAG**: `qwen3_text` (Ngôn ngữ: `python`)
- **Thời gian nạp**: `2026-11-27T01:30:09.527122` (Chunk 2/2)

**Nội dung đoạn trích đã chunk & vector hóa:**
```markdown
Hay chon tap do vat sao cho tong gia tri la lon nhat ma khong vuot qua W. Cong thuc truy hoi:
dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])  (neu j >= w[i])
Do phuc tap thoi gian: O(n * W).
```

---


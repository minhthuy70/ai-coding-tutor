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

## 3. Phân tích Độ phức tạp Thuật toán (Big-O)

| Thao tác | Mô tả | Độ phức tạp thời gian |
| :--- | :--- | :---: |
| `heapify(arr)` | Chuyển đổi danh sách ngẫu nhiên thành Heap | $O(n)$ |
| `heappush(h, val)` | Thêm phần tử và cân bằng lại cây | $O(\log n)$ |
| `heappop(h)` | Trích xuất và xóa nút gốc nhỏ nhất | $O(\log n)$ |
| `heap[0]` | Xem phần tử nhỏ nhất (Peek) | $O(1)$ |
| `nlargest(k, arr)` | Tìm $k$ phần tử lớn nhất | $O(n \log k)$ |
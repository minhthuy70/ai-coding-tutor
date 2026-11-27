# ⚡ BẢNG TRA CỨU DEMO NHANH (SIÊU NGẮN & DỄ NHỚ)

> 💡 **Mẹo số 1:** Bạn **KHÔNG CẦN GÕ CHỮ**! Phía trên khung chat luôn có hàng nút bấm **`Demo 1-chạm`**. Bạn chỉ cần bấm 1 cái là hệ thống tự điền ngay câu hỏi.  
> 💡 **Mẹo số 2:** Nếu tự gõ trước mặt thầy cô, chỉ cần gõ đúng **5 - 8 chữ** siêu ngắn như bảng dưới:

---

## 📋 BẢNG TỔNG HỢP 7 TÌNH HUỐNG DEMO

| # | Tình huống Demo | Tệp đính kèm kéo thả | Nút 1-chạm hoặc Câu gõ nhanh (Chỉ 5-8 chữ) | Điểm nhấn để giải thích với Hội đồng |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Lý thuyết CTDL** | *(Không cần)* | Nút `[List vs Tuple]`<br>👉 Gõ: `List khác gì Tuple vậy thầy?` | RAG trích giáo trình Python về tính bất biến (mutability). |
| **2** | **Thuật toán Big-O** | *(Không cần)* | Nút `[Binary Search]`<br>👉 Gõ: `Binary search hoạt động thế nào?` | AI Socratic phân tích O(log n), điều kiện mảng đã sắp xếp. |
| **3** | **Bắt lỗi duyệt mảng** | File: `04_off_by_one_index.py` | Nút `[Lỗi IndexError]`<br>👉 Gõ: `Sao code này bị IndexError ạ?` | AI đọc code file `.py`, chỉ ra lỗi `len + 1` mà không giải hộ. |
| **4** | **Bắt lỗi Scope biến** | File: `05_unbound_local_scope_error.py` | Nút `[Lỗi UnboundLocal]`<br>👉 Gõ: `Sao bị lỗi UnboundLocalError vậy ạ?` | AI phân tích quy tắc LEGB Scope trong Python. |
| **5** | **OCR lỗi Terminal** | Ảnh: `01_terminal_index_error.png` | Nút `[Terminal trong ảnh]`<br>👉 Gõ: `Terminal trong ảnh báo lỗi gì vậy thầy?` | Vision OCR đọc chữ từ ảnh terminal, phân tích nguyên nhân. |
| **6** | **OCR lỗi Đệ quy** | Ảnh: `02_terminal_recursion_error.png` | 👉 Gõ: `Lỗi RecursionError trong ảnh sửa sao ạ?` | OCR đọc lỗi tràn stack, hỏi gợi mở điều kiện dừng (Base case). |
| **7** | **Đa phương thức đỉnh cao** | File `02...py` + Ảnh `02...png` | 👉 Gõ: `Xem giúp em code và ảnh lỗi này!` | Hệ thống nhận đồng thời cả file code và ảnh chụp terminal. |

---

## 📚 BẢNG DEMO TÍNH NĂNG NẠP GIÁO TRÌNH (GV INGESTION)

Thư mục lưu sẵn 5 file: `demo_samples/instructor_curriculums/`

| # | Định dạng file | Tên file giáo trình chuẩn | Thao tác nạp trên web | Câu hỏi ngắn kiểm chứng ngay (Dưới 8 từ) | Kết quả AI trích xuất |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **1** | 📄 **PDF** | `01_giao_trinh_quy_hoach_dong_dp.pdf` | Bấm nút **"Nạp giáo trình (GV)"** $\rightarrow$ Kéo file `.pdf` vào $\rightarrow$ Bấm Nạp | 👉 `Quy hoạch động trong Python là gì?` | AI trích dẫn đúng bài giảng PDF: Balo 0/1, Memoization & Tabulation |
| **2** | 📝 **DOCX** | `02_bai_giang_oop_ke_thua_da_hinh.docx` | Bấm nút **"Nạp giáo trình (GV)"** $\rightarrow$ Kéo file `.docx` vào $\rightarrow$ Bấm Nạp | 👉 `Kế thừa trong OOP Python hoạt động sao?` | AI trích dẫn đúng bảng Word: Quan hệ IS-A, abstractmethod & super() |
| **3** | 📑 **TXT** | `03_chuyen_de_xu_ly_ngoai_le_pep8.txt` | Bấm nút **"Nạp giáo trình (GV)"** $\rightarrow$ Kéo file `.txt` vào $\rightarrow$ Bấm Nạp | 👉 `Khối try except finally chạy thế nào?` | AI trích dẫn đúng quy tắc PEP 8 và Context Manager `with` |
| **4** | 📋 **MD** | `04_cau_truc_du_lieu_heap_priority_queue.md` | Bấm nút **"Nạp giáo trình (GV)"** $\rightarrow$ Kéo file `.md` vào $\rightarrow$ Bấm Nạp | 👉 `Cấu trúc Heap trong Python dùng module nào?` | AI trích dẫn bảng Big-O và module `heapq` từ file Markdown |
| **5** | 🐍 **PY** | `05_thuat_toan_do_thi_bfs_dfs.py` | Bấm nút **"Nạp giáo trình (GV)"** $\rightarrow$ Kéo file `.py` vào $\rightarrow$ Bấm Nạp | 👉 `BFS và DFS duyệt đồ thị khác nhau sao?` | AI trích xuất module mã nguồn: `collections.deque` FIFO vs Call Stack |

---

## 🎯 3 BƯỚC THAO TÁC THẦN TỐC KHI TRÌNH DIỄN:

1. **Kéo thả** file (nếu có) vào ô chat.
2. **Bấm 1 nút** trên thanh `Demo 1-chạm` (hoặc gõ 5 chữ).
3. **Bấm Enter** (hoặc nút Gửi mũi tên xanh) $\rightarrow$ Xem AI trả lời + cuộn xuống xem trích dẫn RAG!

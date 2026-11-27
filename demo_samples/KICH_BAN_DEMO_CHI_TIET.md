# 🎯 KỊCH BẢN DEMO HỆ THỐNG TRỢ GIẢNG AI SOCRATIC (AI CODING TUTOR)

> **Tài liệu hướng dẫn thực hành Demo trực tiếp trên giao diện Web (`http://localhost:3000`)**  
> Dành cho buổi Báo cáo Tiến độ, Demo Đồ án tốt nghiệp và Vấn đáp Hội đồng.

---

## 📌 CHUẨN BỊ TRƯỚC KHI DEMO

1. **Khởi động hệ thống:**
   - Mở terminal chạy file: `start_dev.bat` (hoặc mở 2 terminal chạy Backend `uvicorn app.main:app --port 8000` và Frontend `npm run dev`).
   - Mở trình duyệt truy cập: `http://localhost:3000`.
   - Kiểm tra thanh header: Hiển thị `Gemini 3 Flash` và `RAG 11,731 Chunks`.

2. **Thư mục tài nguyên demo có sẵn:**
   - Mã nguồn mẫu: `demo_samples/code_files/`
   - Ảnh chụp terminal lỗi: `demo_samples/terminal_images/`

---

## 🎬 4 KỊCH BẢN DEMO TIÊU BIỂU (TỪ CƠ BẢN ĐẾN ĐA PHƯƠNG THỨC)

---

### KỊCH BẢN 1: HỎI ĐÁP LÝ THUYẾT & THUẬT TOÁN (TEXT ONLY)
*Mục tiêu: Chứng minh RAG truy xuất chính xác giáo trình chuẩn và AI giải thích theo phương pháp Socratic, phân tích Big-O.*

> 💡 **Mẹo:** Bạn có thể bấm nút **Demo 1-chạm** phía trên khung chat để tự động điền, không cần gõ phím!

#### 🔹 Trường hợp 1.1: Khác biệt cấu trúc dữ liệu kinh điển (List vs Tuple)
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  List khác gì Tuple vậy thầy?
  ```
  *(Hoặc bấm nút: `[List vs Tuple]` trên hàng Demo 1-chạm)*
* **Kỳ vọng AI phản hồi:**
  1. Phân tích rõ: List là `mutable` (cho phép thêm/sửa/xóa), Tuple là `immutable` (bất biến, tối ưu bộ nhớ hơn).
  2. Đặt câu hỏi gợi mở Socratic: Khi lưu trữ tọa độ địa lý `(latitude, longitude)` hoặc danh sách sinh viên có thể thay đổi, em sẽ chọn cấu trúc nào?
  3. **Khối RAG Evidence:** Trích dẫn từ giáo trình chuẩn CPython (`PY_01_Official_Tutorial.md` hoặc `PY_06_Official_Collections_and_Data_Structures.md`). Bấm *"Xem đoạn trích"* để đối chiếu tài liệu gốc.

#### 🔹 Trường hợp 1.2: Tối ưu thuật toán & Độ phức tạp Big-O (Binary Search)
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Binary search hoạt động thế nào?
  ```
  *(Hoặc bấm nút: `[Binary Search]` trên hàng Demo 1-chạm)*
* **Kỳ vọng AI phản hồi:**
  1. Dẫn dắt nguyên lý "chia để trị" (mỗi bước giảm một nửa không gian tìm kiếm).
  2. Nhấn mạnh điều kiện mảng phải được **sắp xếp thứ tự trước**.
  3. Đặt câu hỏi thử thách: Nếu mảng chưa sắp xếp, tổng thời gian sắp xếp rồi tìm kiếm nhị phân có tối ưu hơn tìm kiếm tuần tự $O(n)$ không?

---

### KỊCH BẢN 2: ĐÍNH KÈM FILE MÃ NGUỒN CÓ LỖI (CODE ATTACHMENT)
*Mục tiêu: Chứng minh AI bóc tách file code Python (.py), chỉ ra vị trí nghi vấn nhưng không viết hộ lời giải hoàn chỉnh.*

#### 🔹 Trường hợp 2.1: Lỗi duyệt mảng vượt biên (Off-by-one Error)
* **Tệp đính kèm:** Kéo thả tệp `demo_samples/code_files/04_off_by_one_index.py` vào ô chat.
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Sao code này bị IndexError ạ?
  ```
  *(Hoặc bấm nút: `[Lỗi IndexError]` trên hàng Demo 1-chạm)*
* **Kỳ vọng AI phản hồi:**
  1. Nhận diện file đính kèm `04_off_by_one_index.py`.
  2. Phát hiện vòng lặp `for i in range(len(students) + 1):`.
  3. Hỏi gợi mở Socratic:
     - *"Chỉ số index của một mảng có $N$ phần tử trong Python chạy từ mấy đến mấy?"*
     - *"Khi `i = len(students)`, giá trị đó có còn nằm trong mảng `students` không?"*
  4. Trích dẫn RAG từ tài liệu về Sequences và Indexing.

#### 🔹 Trường hợp 2.2: Lỗi cạm bẫy Mutable Default Argument
* **Tệp đính kèm:** Kéo thả `demo_samples/code_files/03_mutable_default_argument.py`.
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Sao hàm này dồn kết quả cũ ạ?
  ```
* **Kỳ vọng AI phản hồi:**
  1. Nhận diện lỗi kinh điển `target_list=[]` được khởi tạo đúng 1 lần khi định nghĩa hàm.
  2. Hướng dẫn tư duy: Thay vì dùng mutable object làm default, trong Python chuẩn PEP 8 lập trình viên thường dùng `target_list=None` rồi xử lý thế nào trong thân hàm?

#### 🔹 Trường hợp 2.3: Lỗi phạm vi biến cục bộ vs toàn cục (LEGB Scope & UnboundLocalError)
* **Tệp đính kèm:** Kéo thả `demo_samples/code_files/05_unbound_local_scope_error.py`.
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Sao bị lỗi UnboundLocalError vậy ạ?
  ```
  *(Hoặc bấm nút: `[Lỗi UnboundLocal]` trên hàng Demo 1-chạm)*
* **Kỳ vọng AI phản hồi:**
  1. Nhận diện quy tắc phạm vi biến LEGB (Local, Enclosing, Global, Built-in) trong Python.
  2. Phân tích: Do trong hàm có toán tử gán `counter += 1`, Python tự động coi `counter` là biến cục bộ (Local), nhưng biến này chưa được gán giá trị trước khi đọc.
  3. Đặt câu hỏi gợi mở:
     - *"Trong Python, từ khóa nào cho phép một hàm truy cập và cập nhật biến ở phạm vi toàn cục (Global)?"*
     - *"Theo chuẩn thiết kế Clean Code, liệu việc truyền tham số và return kết quả (Pure Function) có an toàn hơn việc lạm dụng biến toàn cục không?"*
  4. Trích dẫn RAG từ Giáo trình chuẩn Python về Scopes và Namespaces.

---

### KỊCH BẢN 3: ĐÍNH KÈM ẢNH CHỤP MÀN HÌNH TERMINAL (VISION OCR)
*Mục tiêu: Chứng minh tính năng Vision OCR trích xuất thông tin lỗi từ ảnh chụp, đối chiếu RAG và giải thích nguyên nhân.*

#### 🔹 Trường hợp 3.1: Ảnh chụp Terminal lỗi IndexError
* **Tệp đính kèm:** Kéo thả ảnh `demo_samples/terminal_images/01_terminal_index_error.png` vào ô chat.
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Terminal trong ảnh báo lỗi gì vậy thầy?
  ```
  *(Hoặc bấm nút: `[Terminal trong ảnh]` trên hàng Demo 1-chạm)*
* **Kỳ vọng AI phản hồi:**
  1. Hệ thống OCR tự động đọc dòng: `IndexError: list index out of range` tại dòng lệnh `print(students[i])`.
  2. AI giải thích ý nghĩa lỗi: Chương trình đang cố gắng truy cập vào một vị trí (index) không tồn tại trong danh sách.
  3. Gợi ý sinh viên dùng `print(len(students))` hoặc kiểm tra lại chỉ số kết thúc của vòng lặp.

#### 🔹 Trường hợp 3.2: Ảnh chụp Terminal lỗi Tràn đệ quy (RecursionError)
* **Tệp đính kèm:** Kéo thả ảnh `demo_samples/terminal_images/02_terminal_recursion_error.png`.
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Lỗi RecursionError trong ảnh sửa sao ạ?
  ```
* **Kỳ vọng AI phản hồi:**
  1. OCR nhận diện: `RecursionError: maximum recursion depth exceeded in comparison`.
  2. Phân tích hiện tượng: Hàm tự gọi chính nó vô hạn lần mà không chạm tới điều kiện dừng (Base Case).
  3. Đặt câu hỏi: Đối với bài toán tính Fibonacci, với $n = 0$ hoặc $n = 1$ thì kết quả là bao nhiêu mà không cần đệ quy tiếp?

#### 🔹 Trường hợp 3.3: Ảnh chụp Terminal lỗi TypeError (Cộng chuỗi với số)
* **Tệp đính kèm:** Kéo thả ảnh `demo_samples/terminal_images/03_terminal_type_error.png`.
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Ảnh terminal này báo lỗi gì vậy thầy?
  ```
* **Kỳ vọng AI phản hồi:**
  1. OCR nhận diện: `TypeError: can only concatenate str (not "int") to str`.
  2. Gợi ý: Trong Python, ép kiểu dữ liệu tường minh bằng hàm `str()` như thế nào hoặc dùng f-string cú pháp ra sao?

#### 🔹 Trường hợp 3.4: Ảnh chụp Terminal lỗi Phạm vi biến (UnboundLocalError)
* **Tệp đính kèm:** Kéo thả ảnh `demo_samples/terminal_images/05_terminal_unboundlocal_error.png`.
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Ảnh này bị lỗi gì vậy thầy?
  ```
* **Kỳ vọng AI phản hồi:**
  1. OCR nhận diện: `UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value`.
  2. Giải thích cơ chế ràng buộc tên biến (Name Binding) trong hàm Python theo chuẩn tài liệu chính thống.

---

### KỊCH BẢN 4: ĐA PHƯƠNG THỨC TỔNG HỢP (CODE + ẢNH + CÂU HỎI)
*Mục tiêu: Thể hiện đỉnh cao của hệ thống: Tiếp nhận đồng thời cả file mã nguồn và ảnh terminal chụp lỗi cùng lúc.*

* **Tệp đính kèm:**
  1. Kéo thả file: `demo_samples/code_files/02_infinite_recursion_fibonacci.py`
  2. Kéo thả ảnh: `demo_samples/terminal_images/02_terminal_recursion_error.png`
* **Câu hỏi cực ngắn (dễ nhớ):**
  ```text
  Xem giúp em code và ảnh lỗi này!
  ```
* **Kỳ vọng AI phản hồi:**
  1. Header tin nhắn hiển thị huy hiệu: Đính kèm 2 tệp (1 file code + 1 ảnh).
  2. AI đọc code và đối chiếu với thông báo lỗi trong ảnh.
  3. Xác định rõ: Hàm `fib(n)` đang gọi `fib(n-1) + fib(n-2)` mà không có `if n <= 1: return n`.
  4. Gợi mở sinh viên thêm điều kiện biên và thử lại trên code sandbox.

---

### KỊCH BẢN 5: NẠP GIÁO TRÌNH MỚI CHO GIẢNG VIÊN (INSTRUCTOR INGESTION)
*Mục tiêu: Chứng minh tính năng động (Dynamic Knowledge Base): Giảng viên có thể nạp thêm tài liệu bài giảng mới (.pdf, .docx, .txt, .md, .py) và AI cập nhật tri thức ngay lập tức để dạy cho sinh viên.*

* **Tài nguyên mẫu có sẵn tại:** `demo_samples/instructor_curriculums/`
  1. `01_giao_trinh_quy_hoach_dong_dp.pdf` (Tài liệu PDF về Quy hoạch động)
  2. `02_bai_giang_oop_ke_thua_da_hinh.docx` (Tài liệu Word về OOP Kế thừa & Đa hình)
  3. `03_chuyen_de_xu_ly_ngoai_le_pep8.txt` (Tài liệu Text về Ngoại lệ & Context Manager)
  4. `04_cau_truc_du_lieu_heap_priority_queue.md` (Tài liệu Markdown về Cây Heap)
  5. `05_thuat_toan_do_thi_bfs_dfs.py` (Mã nguồn Python giải thuật BFS & DFS)

* **Các bước thao tác trực tiếp:**
  1. Nhìn lên góc trên bên phải màn hình, bấm nút **"Nạp giáo trình (GV)"** (nút màu xanh lá có biểu tượng cuốn sách).
  2. Kéo thả file `01_giao_trinh_quy_hoach_dong_dp.pdf` (hoặc `02_bai_giang_oop_ke_thua_da_hinh.docx`) vào khung nạp.
  3. Bấm nút **"Bắt đầu nạp tri thức"**. Hệ thống chạy pipeline bóc tách, cắt chunk, embedding và lưu vào ChromaDB trong vòng 1 giây.
  4. Màn hình báo thành công: *Đã bổ sung các đoạn tri thức mới vào kho tri thức RAG*.
  5. Đóng modal, quay lại ô Chat và nhập câu hỏi kiểm chứng:
     ```text
     Quy hoạch động trong Python là gì?
     ```
* **Kỳ vọng AI phản hồi:**
  - AI giải thích nguyên lý chia bài toán con, Memoization và Tabulation.
  - Khối **RAG Evidence** hiển thị trực tiếp dẫn chứng trích từ file vừa nạp: `01_giao_trinh_quy_hoach_dong_dp.pdf` (Độ khớp > 75%)!

---

## 💡 MẸO TRÌNH DIỄN KHI DEMO TRƯỚC HỘI ĐỒNG

1. **Nhấn mạnh tính năng RAG Grounding:**
   - Sau khi AI trả lời, hãy cuộn chuột xuống khối **`📚 Cơ sở Tri thức Giáo trình (RAG Evidence)`** màu xanh lục.
   - Bấm vào nút **"Xem đoạn trích"** để mở đoạn văn bản gốc trong giáo trình (11,731 chunks) nhằm chứng minh câu trả lời không phải là bịa đặt (hallucination).

2. **Nhấn mạnh tính Socratic (Không giải hộ):**
   - Chỉ ra cho hội đồng thấy: AI không viết nguyên lời giải hoàn chỉnh mà đặt câu hỏi gợi mở, giúp người học phát triển tư duy thuật toán độc lập.

3. **Thử nghiệm các tính năng phụ trợ trên giao diện:**
   - Bấm vào nút **"Đọc to"** (Text-to-Speech) để AI phát âm câu trả lời bằng tiếng Việt.
   - Bấm vào các **Gợi ý câu hỏi tiếp theo (Follow-up chips)** để AI tiếp tục đào sâu bài toán.
   - Bấm nút **"Soát lỗi" (Code Quality)** hoặc **"Chạy" (Sandbox)** trên khối code để minh họa môi trường IDE mini tích hợp.

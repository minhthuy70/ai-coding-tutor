# HƯỚNG DẪN KHỞI CHẠY VÀ DEMO HỆ THỐNG AI CODING TUTOR
## HỆ THỐNG TRỢ GIẢNG LẬP TRÌNH THÔNG MINH ĐA PHƯƠNG THỨC (MULTIMODAL RAG)

> **Tài liệu hướng dẫn thực hành "cầm tay chỉ việc":** Giúp bạn tự khởi chạy hệ thống, truy cập giao diện, kiểm thử tự động và thực hiện các kịch bản demo thuyết phục nhất trước Giảng viên và Hội đồng.

---

## 1. CHUẨN BỊ TRƯỚC KHI CHẠY (PREREQUISITES)

### Bước 1: Kiểm tra tệp cấu hình môi trường `.env`
Đảm bảo tệp `.env` tại thư mục gốc dự án đã có ít nhất cấu hình sau:
```ini
PROJECT_NAME="AI-Powered Coding Tutor"
ENVIRONMENT="development"

# Khóa API Gemini (bắt buộc để chạy AI Tutor)
GEMINI_API_KEY="AIzaSy..."
GEMINI_MODEL="gemini-3-flash-preview"

# Cấu hình Vector Database ChromaDB
CHROMA_DB_DIR="data/09_chromadb"
RAG_BENCHMARK_EMBEDDINGS_PATH="data/04_benchmark/benchmark_36q_query_embeddings.json"

# Cấu hình Cơ sở dữ liệu và Cache (tùy chọn khi chạy dev)
DATABASE_URL="postgresql+asyncpg://postgres:postgres_dev_password@localhost:5432/ai_coding_tutor"
REDIS_URL="redis://localhost:6379/0"
```

---

## 2. CÁCH KHỞI CHẠY HỆ THỐNG

### CÁCH 1: KHỞI CHẠY 1-CLICK BẰNG FILE SCRIPT (KHUYÊN DÙNG ĐỂ DEMO)
Đây là cách nhanh nhất và tiện lợi nhất khi bạn mang máy tính lên thuyết trình:

1. Mở thư mục dự án `d:\CNTT2311\HK9\DOAN4\ai-coding-tutor`.
2. Nhấp đúp chuột vào tệp: **`start_dev.bat`**  
   *(Hoặc mở PowerShell gõ: `.\start_dev.bat`)*.
3. Hệ thống sẽ tự động bật:
   * **Backend API (FastAPI):** `http://localhost:8000`
   * **Tài liệu API Swagger:** `http://localhost:8000/docs`
   * **Giao diện Web (Frontend):** `http://localhost:3000`

---

### CÁCH 2: KHỞI CHẠY BẰNG DOCKER COMPOSE (CHẠY CHUẨN DOANH NGHIỆP / ON-PREMISE)
Dùng khi bạn muốn demo tính năng đóng gói độc lập, không phụ thuộc vào môi trường cài đặt của máy:

1. Mở PowerShell hoặc Terminal tại thư mục gốc dự án.
2. Chạy lệnh khởi động:
   ```bash
   docker compose up -d
   ```
3. Kiểm tra trạng thái các container đang chạy:
   ```bash
   docker compose ps
   ```
4. Xem log hoạt động của Backend:
   ```bash
   docker compose logs -f backend
   ```
5. Khi muốn tắt hệ thống:
   ```bash
   docker compose down
   ```

---

### CÁCH 3: KHỞI CHẠY THỦ CÔNG TỪNG PHẦN QUA TERMINAL (DÀNH CHO LẬP TRÌNH VIÊN)

#### Terminal 1: Chạy Backend (FastAPI Server)
```bash
# Di chuyển vào thư mục backend
cd backend

# Cài đặt các thư viện cần thiết (nếu chưa cài)
py -3.11 -m pip install -r requirements.txt

# Khởi chạy server Uvicorn
py -3.11 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Server backend sẽ chạy tại: **`http://localhost:8000`**

#### Terminal 2: Chạy Frontend (Next.js - nếu có)
```bash
cd frontend
npm install
npm run dev
```
Giao diện sinh viên sẽ chạy tại: **`http://localhost:3000`**

---

## 3. CÁC ĐỊA CHỈ TRUY CẬP QUAN TRỌNG

| Thành phần | Địa chỉ truy cập URL | Chức năng chính |
| :--- | :--- | :--- |
| **Giao diện Web Sinh viên** | `http://localhost:3000` | Màn hình chat hỏi bài, tải file code và upload ảnh lỗi |
| **Swagger API Docs** | `http://localhost:8000/docs` | Kiểm tra trực quan toàn bộ các endpoint API của Backend |
| **Kiểm tra trạng thái Health** | `http://localhost:8000/api/v1/health` | Kiểm tra trạng thái kết nối Database, Redis, ChromaDB |
| **Kho tri thức ChromaDB** | Thư mục `data/09_chromadb/` | Chứa 1.221 chunks tri thức chuẩn hóa từ các giáo trình |

---

## 4. LỆNH CHẠY BỘ KIỂM THỬ TỰ ĐỘNG (CHỨNG MINH CHẤT LƯỢNG TRƯỚC HỘI ĐỒNG)

Trước khi bắt đầu buổi thuyết trình, bạn có thể mở sẵn một Terminal và gõ các lệnh sau để show cho Thầy/Cô thấy **100% các bài test tự động đều vượt qua**:

### 1. Chạy 33 Unit Tests (Bảo mật, OCR, Query Synthesizer, RAG):
```bash
py -3.11 -m pytest tests/test_rag_service.py tests/test_file_extractor.py tests/test_image_extractor.py tests/test_query_synthesizer.py -v
```
👉 *Kết quả:* **33 passed in ~4.0s (100% Pass)**.

### 2. Chạy 30 Kịch bản Thực tế End-to-End (Text, File Code, Terminal OCR):
```bash
py -3.11 -m pytest tests/test_day13_e2e_scenarios.py -v
```
👉 *Kết quả:* **30 passed in ~30s (100% Pass)**.

---

## 5. HƯỚNG DẪN 3 KỊCH BẢN DEMO TRỰC TIẾP TRƯỚC HỘI ĐỒNG

Khi đứng trước Thầy/Cô, bạn chỉ cần thực hiện lần lượt 3 kịch bản này để chứng minh toàn bộ các tính năng đột phá của hệ thống:

### KỊCH BẢN 1: HỎI LÝ THUYẾT & ĐỘ PHỨC TẠP THUẬT TOÁN (TEXT ONLY)
* **Thao tác:** Nhập câu hỏi vào ô chat:
  > *"Tại sao thuật toán QuickSort có độ phức tạp trường hợp xấu nhất là O(n^2) và trong thực tế người ta khắc phục điều này như thế nào?"*
* **Hiện tượng quan sát được:**
  * AI không trả lời lan man, mà trích dẫn ngay: `[Giáo trình: Cấu trúc dữ liệu & Giải thuật | Chương: Các giải thuật sắp xếp]`.
  * AI giải thích nguyên nhân do chọn phần tử chốt (Pivot) lệch (dãy đã sắp xếp sẵn).
  * AI gợi ý kỹ thuật chọn chốt trung vị của 3 phần tử (Median-of-Three).

---

### KỊCH BẢN 2: TẢI TỆP MÃ NGUỒN C++ BỊ LỖI RÒ RỈ BỘ NHỚ (SOURCE CODE ATTACHMENT)
* **Thao tác:** Tải lên tệp mã nguồn C++ có lỗi cấp phát động nhưng quên giải phóng (ví dụ: `leak.cpp`):
  ```cpp
  #include <iostream>
  using namespace std;

  void processData() {
      int* arr = new int[100];
      for(int i = 0; i < 100; i++) arr[i] = i * 2;
      // Quên delete[] arr;
  }

  int main() {
      processData();
      return 0;
  }
  ```
  Nhập kèm câu hỏi: *"Hàm này của em chạy ổn không ạ?"*
* **Hiện tượng quan sát được:**
  * **AI không viết lại code hộ.**
  * AI đóng vai trò Socratic đặt câu hỏi: *"Bạn đã kiểm tra vùng nhớ Heap cấp phát bằng `new int[100]` ở dòng 5 chưa? Trong hàm `processData()`, tài nguyên này được giải phóng ở đâu trước khi kết thúc hàm?"*
  * Kèm thẻ trích dẫn giáo trình C++: `[Chương 4: Con trỏ và Quản lý bộ nhớ]`.

---

### KỊCH BẢN 3: TẢI ẢNH CHỤP MÀN HÌNH TERMINAL BÁO LỖI (TERMINAL VISION OCR)
* **Thao tác:** Tải lên ảnh chụp màn hình terminal báo lỗi Python:
  > `IndexError: list index out of range at line 14: for i in range(len(arr) + 1): print(arr[i])`
* **Hiện tượng quan sát được:**
  * Module **Vision OCR** đọc được chính xác dòng chữ bị lỗi từ ảnh.
  * Thuật toán **Query Synthesizer** bóc tách tên lỗi `IndexError` và điều kiện biên.
  * AI giải thích nguyên nhân: *"Chỉ số mảng trong Python chạy từ 0 đến len(arr) - 1, nhưng vòng lặp của bạn duyệt tới len(arr)"*, đồng thời trích dẫn đúng bài học về Kiểu dữ liệu List trong Giáo trình Python.

---

## 6. XỬ LÝ NHANH CÁC SỰ CỐ THƯỜNG GẶP (TROUBLESHOOTING)

1. **Lỗi cổng 8000 hoặc 3000 đã bị chiếm dụng (Port already in use):**
   * Mở CMD gõ lệnh giải phóng cổng:
     ```cmd
     netstat -ano | findstr :8000
     taskkill /PID <PID_tìm_thấy> /F
     ```
2. **Lỗi không gọi được AI (Gemini API Key missing):**
   * Mở tệp `.env`, kiểm tra biến `GEMINI_API_KEY` đã được điền khóa API hợp lệ chưa.
3. **Lỗi thiếu thư viện khi chạy bằng terminal:**
   * Chạy lại lệnh:
     ```bash
     py -3.11 -m pip install -r backend/requirements.txt
     ```

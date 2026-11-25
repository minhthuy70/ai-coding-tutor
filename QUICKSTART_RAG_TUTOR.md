# 🚀 HƯỚNG DẪN KHỞI CHẠY NHANH & NGHIỆM THU HỆ THỐNG
## AI-POWERED SOCRATIC CODING TUTOR & MULTIMODAL RAG PLATFORM
### (Tài liệu chuyển giao kỹ thuật & Hướng dẫn nghiệm thu Sprint Ngày 14)

> **Tác giả:** Nhóm Phát Triển Dự Án AI Coding Tutor  
> **Repository:** [https://github.com/minhthuy70/ai-coding-tutor](https://github.com/minhthuy70/ai-coding-tutor)  
> **Thời điểm nghiệm thu:** Tháng 11/2026 (Hoàn thành trọn vẹn 14 Ngày)

---

## 1. TỔNG QUAN HỆ THỐNG

Hệ thống **AI Coding Tutor** là nền tảng trợ giảng lập trình thông minh ứng dụng kỹ thuật **Gợi mở Socratic (Socratic Method)** kết hợp kiến trúc **RAG đa không gian vector (Dual-Collection RAG)** và **xử lý đa phương thức (Multimodal Ingestion: Text + Source Code + Terminal Image)**.

### Các cổng dịch vụ mặc định:
- 🌐 **Giao diện Web Người dùng (Frontend):** [http://localhost:3000](http://localhost:3000)
- 📚 **Tài liệu API Tương tác (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)
- 🩺 **Kiểm tra trạng thái hệ thống (Health Check):** [http://localhost:8000/api/health](http://localhost:8000/api/health)

---

## 2. YÊU CẦU MÔI TRƯỜNG (PREREQUISITES)

1. **Git & Git LFS:** Để tải toàn bộ mã nguồn và kho tri thức vector 5.230 records.
   ```bash
   git lfs install
   ```
2. **Python:** Phiên bản 3.11.x (Đã kiểm thử tối ưu trên Python 3.11).
3. **Node.js:** Phiên bản 18.x hoặc 20.x LTS.
4. **(Tùy chọn) Docker & Docker Compose:** Dành cho chế độ triển khai đóng gói container.

---

## 3. CÁCH 1: KHỞI CHẠY 1 CHẠM TRÊN MÁY CÁ NHÂN (KHUYÊN DÙNG)

Đây là cách nhanh nhất và thuận tiện nhất để demo và phát triển tại máy cục bộ:

### Bước 1: Kéo mã nguồn & Kéo dữ liệu Vector
```bash
git clone https://github.com/minhthuy70/ai-coding-tutor.git
cd ai-coding-tutor
git lfs pull
```

### Bước 2: Thiết lập biến môi trường
Sao chép tệp mẫu `.env.example` thành `.env` và điền khóa API:
```bash
cp .env.example .env
```
Nội dung tối thiểu cần thiết trong `.env`:
```env
GEMINI_API_KEY=AIzaSy...your_gemini_api_key_here
GEMINI_MODEL=gemini-3-flash-preview
CHROMA_DB_DIR=data/09_chromadb
BACKEND_CORS_ORIGINS=["http://localhost:3000","http://127.0.0.1:3000"]
```

### Bước 3: Cài đặt thư viện phụ thuộc (Làm 1 lần)
```bash
# Cài đặt Backend
cd backend
pip install -r requirements.txt
cd ..

# Cài đặt Frontend
cd frontend
npm install
cd ..
```

### Bước 4: Chạy file khởi động 1 chạm
Trên Windows, bạn chỉ cần nhấp đúp chuột vào file:
👉 **`start_dev.bat`**

*(Hệ thống sẽ tự động mở 2 cửa sổ terminal khởi chạy song song Backend FastAPI tại Port 8000 và Frontend Next.js tại Port 3000).*

---

## 4. CÁCH 2: TRIỂN KHAI ĐÓNG GÓI TRỌN GÓI VỚI DOCKER COMPOSE

Dành cho môi trường máy chủ (Server) hoặc máy tính có cài đặt Docker:

```bash
# 1. Khởi động toàn bộ cụm dịch vụ (Postgres + Redis + FastAPI + Next.js)
docker compose up -d --build

# 2. Xem logs hoạt động
docker compose logs -f backend

# 3. Dừng hệ thống khi kết thúc
docker compose down
```

---

## 5. BA KỊCH BẢN DEMO THỰC TẾ CHO BUỔI BÁO CÁO NGHIỆM THU

### 🎯 Kịch bản Demo 1: Câu hỏi lý thuyết & Thuật toán (Text Only)
- **Thao tác:** Nhập câu hỏi:  
  `"Em chọn phần tử đầu tiên làm Pivot trong QuickSort thì khi nào thuật toán bị chạy chậm nhất O(n^2) ạ?"`
- **Quan sát kết quả:**
  1. Huy hiệu **RAG Grounding Evidence** xuất hiện, hiển thị trích dẫn từ cuốn *MIT Mathematics for Computer Science & DSA* hoặc *Ebook Python Kỹ Thuật*.
  2. AI phản hồi theo phương pháp **Socratic**: Phân tích kịch bản mảng đã sắp xếp sẵn, giải thích việc phân hoạch mất cân bằng mà không đưa ra code giải hộ, đặt câu hỏi gợi ý sinh viên chọn phần tử ngẫu nhiên hoặc Median-of-Three.

### 🎯 Kịch bản Demo 2: Phân tích file mã nguồn C++ có lỗi bộ nhớ (Text + File Code)
- **Thao tác:** Nhấn nút **Đính kèm Tệp (📎)** và tải lên file code C++ (ví dụ `student_code.cpp` chứa lỗi con trỏ trôi nổi *Dangling Pointer* hoặc quên `delete[]`).
- **Nội dung hỏi:** `"Bài này của em chạy xong bị cảnh báo rò rỉ bộ nhớ, thầy chỉ giúp em lỗi ở đâu với ạ."`
- **Quan sát kết quả:**
  1. Hệ thống tự động nhận diện ngôn ngữ C++, gán nhãn `CPP` trên thanh input.
  2. RAG trích xuất tài liệu *ISO C++ Standard & Memory Management*.
  3. AI khoanh vùng chính xác dòng cấp phát `new int[...]`, nhắc nhở nguyên tắc RAII hoặc `std::unique_ptr` chuẩn mực.

### 🎯 Kịch bản Demo 3: Phân tích ảnh chụp màn hình lỗi Terminal IDE (Text + Ảnh OCR)
- **Thao tác:** Kéo thả hoặc dán (Ctrl+V) ảnh chụp màn hình terminal chứa thông báo lỗi:  
  `IndexError: list index out of range at line 14`.
- **Nội dung hỏi:** `"Em bị lỗi này khi duyệt mảng, tại sao lại lỗi ạ?"`
- **Quan sát kết quả:**
  1. Module **Gemini Vision OCR** bóc tách nguyên văn dòng lỗi `IndexError` và đoạn code trên ảnh.
  2. RAG tra cứu tài liệu *Official Python Tutorial: Sequence Types & Indexing*.
  3. Trợ giảng đặt câu hỏi về chỉ số mảng bắt đầu từ `0` đến `n - 1`, chỉ ra điều kiện dừng vòng lặp `range(len(arr) + 1)` đang vượt biên.

---

## 6. HƯỚNG DẪN KIỂM THỬ TỰ ĐỘNG TOÀN HỆ THỐNG (AUTOMATED TEST SUITE)

Để chứng minh tính toàn vẹn và độ tin cậy kỹ thuật với hội đồng, chạy bộ kiểm thử:

```bash
# 1. Chạy toàn bộ Unit Tests RAG & Pipeline Đa phương thức
py -3.11 -m pytest tests/test_rag_service.py tests/test_file_extractor.py tests/test_query_synthesizer.py -v

# 2. Chạy kiểm thử chất lượng Retrieval Benchmark (Hit@3 = 100%)
py -3.11 scripts/rag/evaluate_retrieval.py
```

---
*Tài liệu bàn giao ngày 26/11/2026 — Dự án AI-Powered Coding Tutor & Code Assessment Platform.*

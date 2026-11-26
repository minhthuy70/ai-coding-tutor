# TÀI LIỆU NỘI DUNG THUYẾT TRÌNH BẢO VỆ ĐỒ ÁN TỐT NGHIỆP
## ĐỀ TÀI: AI-POWERED CODING TUTOR – HỆ THỐNG TRỢ GIẢNG LẬP TRÌNH THÔNG MINH ỨNG DỤNG RAG VÀ AI ĐA PHƯƠNG THỨC

> **Phiên bản tài liệu:** 2.0 (Bản hoàn thiện kỹ thuật sau kiểm toán thực tế mã nguồn và dữ liệu)  
> **Đơn vị thực hiện:** Nhóm Đồ án Tốt nghiệp CNTT  
> **Mục đích tài liệu:** Cung cấp nội dung chuẩn xác, có căn cứ thực nghiệm để chuyển tiếp trực tiếp thành các slide PowerPoint (PPT) phục vụ buổi bảo vệ trước Hội đồng.

---

# PHẦN 1: TỔNG QUAN & TÍNH CẤP THIẾT CỦA ĐỀ TÀI (MOTIVATION & PROBLEM STATEMENT)

```
┌────────────────────────────────────────┐       ┌────────────────────────────────────────┐
│     THỰC TRẠNG GIẢNG DẠY & TỰ HỌC      │       │     MỤC TIÊU GIẢI PHÁP CỦA ĐỒ ÁN       │
├────────────────────────────────────────┤       ├────────────────────────────────────────┤
│ ⚠️ Sinh viên bế tắc khi tự debug ở nhà │  ──>  │ ✅ Trợ giảng Sư phạm AI hỗ trợ 24/7    │
│ ⚠️ ChatGPT sinh code giải hộ hoàn toàn │  ──>  │ ✅ Phương pháp Socratic gợi mở tư duy  │
│ ⚠️ AI tổng quát dễ bịa cú pháp, lệch đề│  ──>  │ ✅ RAG neo chặt giáo trình chính thống │
│ ⚠️ Lỗi lập trình kèm ảnh terminal/code │  ──>  │ ✅ Pipeline xử lý đầu vào đa phương thức│
└────────────────────────────────────────┘       └────────────────────────────────────────┘
```

### 1.1. Bối cảnh đào tạo lập trình cơ sở & Khó khăn của sinh viên
* **Đặc thù môn học nền tảng:** Các môn học lập trình cơ sở như Lập trình C/C++, Lập trình Python, Cấu trúc dữ liệu & Giải thuật đóng vai trò quyết định nền tảng tư duy của sinh viên ngành Công nghệ Thông tin. Tuy nhiên, các môn học này có độ dốc học tập (learning curve) rất lớn do chứa nhiều khái niệm trừu tượng: con trỏ, cấp phát và giải phóng bộ nhớ động, độ phức tạp thuật toán, đệ quy.
* **Rào cản tự sửa lỗi (The Debugging Barrier):** Trong quá trình làm bài tập tại nhà ngoài giờ lên lớp, sinh viên thường xuyên gặp các lỗi biên dịch hoặc lỗi thực thi kinh điển (`Segmentation Fault`, `Memory Leak`, `IndexError`). Khi không có giảng viên hoặc trợ giảng trực tiếp hỗ trợ, sinh viên mất nhiều giờ bế tắc trước các thông báo lỗi trừu tượng, dễ dẫn đến tâm lý nản chí và suy giảm kết quả học tập.

### 1.2. Thách thức từ việc sử dụng các mô hình AI tạo sinh thương mại (ChatGPT, GitHub Copilot)
* **Hiện tượng "Làm bài hộ / Mớm code" (Spoon-feeding):** Sự phổ biến của các công cụ như ChatGPT hay GitHub Copilot giúp sinh viên tìm kiếm câu trả lời nhanh chóng. Tuy nhiên, các công cụ này thường tự động sinh lại toàn bộ đoạn mã nguồn hoàn chỉnh. Sinh viên dễ rơi vào thói quen sao chép - dán (copy-paste) mà không hiểu bản chất thuật toán và không rèn luyện được kỹ năng tự gỡ lỗi (debugging).
* **Vấn đề ảo giác (Hallucination) và lệch chuẩn giáo trình:** Các mô hình ngôn ngữ lớn thương mại được huấn luyện trên dữ liệu Internet mở rộng lớn, thường đưa ra các cú pháp nâng cao hoặc thư viện ngoài không được phép sử dụng trong phạm vi môn học (ví dụ: sinh viên năm nhất học con trỏ thô trong C++ nhưng AI lại sinh mã nguồn C++20 sử dụng `std::unique_ptr` hoặc các thư viện chuẩn nâng cao).

### 1.3. Mục tiêu và định vị của đề tài
* **Xây dựng Trợ giảng AI theo phương pháp Sư phạm Socratic:** Hệ thống không đưa ra mã nguồn sửa sẵn, mà đóng vai trò người trợ giảng định hướng: phân tích hiện tượng lỗi, giải thích nguyên nhân và đặt câu hỏi gợi mở để người học tự tìm ra giải pháp.
* **Đảm bảo tính chính xác học thuật bằng kỹ thuật RAG (Retrieval-Augmented Generation):** Neo chặt ngữ cảnh câu trả lời vào kho tài liệu giáo trình đại học chính thống, có trích dẫn nguồn cụ thể để sinh viên đối chiếu.
* **Tiếp nhận dữ liệu đa phương thức (Multimodal):** Hỗ trợ sinh viên gửi câu hỏi văn bản kết hợp tệp mã nguồn (`.py`, `.cpp`, `.sql`) và ảnh chụp màn hình Terminal thông báo lỗi.

---

# PHẦN 2: MỤC TIÊU VÀ ĐỐI TƯỢNG SỬ DỤNG (SCOPE & USE CASES)

### 2.1. Đối tượng sử dụng và phạm vi đề tài
* **Đối tượng người dùng chính:** Sinh viên ngành CNTT đang theo học các học phần lập trình cơ sở (C/C++, Python, Cấu trúc dữ liệu & Giải thuật, CSDL).
* **Phạm vi tri thức hiện tại:** Kho ngữ liệu giáo trình chính thống gồm 4 mảng kiến thức: Lập trình C/C++, Lập trình Python, Cấu trúc dữ liệu & Thuật toán, Cơ sở dữ liệu và Toán rời rạc.

### 2.2. Yêu cầu hệ thống

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 BẢNG YÊU CẦU HỆ THỐNG                                  │
├──────────────────────────────────┬─────────────────────────────────────────────────────┤
│ YÊU CẦU CHỨC NĂNG (FUNCTIONAL)   │ 1. Tiếp nhận câu hỏi dạng Text, File code và Ảnh lỗi│
│                                  │ 2. Trích xuất text từ ảnh Terminal bằng Vision OCR │
│                                  │ 3. Bóc tách và kiểm tra an toàn mã nguồn đính kèm   │
│                                  │ 4. Tổng hợp truy vấn kỹ thuật (Query Synthesizer)   │
│                                  │ 5. Truy xuất tri thức giáo trình từ ChromaDB (RAG)  │
│                                  │ 6. Sinh phản hồi gợi mở Socratic kèm thẻ trích dẫn  │
├──────────────────────────────────┼─────────────────────────────────────────────────────┤
│ YÊU CẦU PHI CHỨC NĂNG (NON-FUNC) │ 1. Độ trễ truy xuất vector (Retrieval Latency): <0.2s│
│                                  │ 2. An toàn dữ liệu: Chặn Path Traversal, chặn binary│
│                                  │ 3. Tính sẵn sàng: Cơ chế Fallback khi lỗi API quota │
│                                  │ 4. Kiến trúc bất đồng bộ (Asynchronous I/O)         │
│                                  │ 5. Đóng gói triển khai chuẩn hóa qua Docker Compose │
└──────────────────────────────────┴─────────────────────────────────────────────────────┘
```

### 2.3. Use Case tổng quan của hệ thống

```
  [Sinh viên] ──(1) Gửi câu hỏi / Nộp code / Tải ảnh Terminal lỗi──> (Hệ thống AI Tutor)
                                                                           │
                                 ┌─────────────────────────────────────────┴─────────────────────────────────────────┐
                                 ▼                                                   ▼                               ▼
                      (Bóc tách mã nguồn & OCR)                          (Truy xuất Giáo trình RAG)       (Sinh phản hồi Socratic)
                                 │                                                   │                               │
                                 └─────────────────────────────────────────┬─────────────────────────────────────────┘
                                                                           ▼
  [Sinh viên] <──(2) Nhận phân tích lỗi + Câu hỏi gợi mở + Thẻ trích dẫn giáo trình chính thống───────────────────────┘
```

---

# PHẦN 3: NGUYÊN LÝ & ĐIỂM KHÁC BIỆT CỦA HỆ THỐNG SO VỚI CÁC CÔNG CỤ HIỆN CÓ

Khi so sánh với các công cụ AI phổ biến hiện nay, hệ thống tập trung giải quyết các bài toán đặc thù của môi trường giáo dục đại học:

```
┌────────────────────────────────────────┐       ┌────────────────────────────────────────┐
│     CHATGPT / COPILOT THÔNG THƯỜNG     │       │     HỆ THỐNG AI CODING TUTOR           │
├────────────────────────────────────────┤       ├────────────────────────────────────────┤
│ ❌ Sinh sẵn toàn bộ mã nguồn sửa lỗi   │  VS   │ ✅ Phương pháp Socratic gợi mở tư duy  │
│ ❌ Dễ dùng cú pháp ngoài phạm vi môn   │       │ ✅ RAG neo chặt giáo trình của trường  │
│ ❌ Nguy cơ loãng khi gửi kèm ảnh+code  │       │ ✅ Module Query Synthesizer cô đọng lỗi│
│ ❌ Không có cơ sở trích dẫn tài liệu   │       │ ✅ Thẻ trích dẫn rõ tên sách, chương mục│
└────────────────────────────────────────┘       └────────────────────────────────────────┘
```

### 3.1. So sánh tiêu chí kỹ thuật và sư phạm

| Tiêu chuẩn đánh giá | ChatGPT / Claude thông thường | GitHub Copilot | Hệ thống AI Coding Tutor |
| :--- | :--- | :--- | :--- |
| **Mục đích thiết kế** | Trợ lý hội thoại đa năng | Tự động hoàn thành code cho lập trình viên | **Trợ giảng sư phạm chuyên sâu cho giáo dục** |
| **Cách tiếp cận sửa lỗi** | Viết lại hàm code hoàn chỉnh | Gợi ý dòng code kế tiếp | **Chỉ điểm nguyên nhân, gợi ý để người học tự sửa** |
| **Cơ sở tri thức (Knowledge Base)** | Dữ liệu Internet mở (tiềm ẩn lỗi thời/lệch chuẩn) | Kho mã nguồn công khai trên GitHub | **Giáo trình chính thống lưu trữ trong Vector DB** |
| **Khả năng kiểm chứng** | Không có nguồn trích dẫn đối soát | Không có | **Hiển thị thẻ trích dẫn (Tên giáo trình, chương, đoạn)** |
| **Xử lý đa phương thức** | Nhận diện đa mục đích tổng quát | Hỗ trợ văn bản và mã nguồn | **Trích xuất chuyên sâu: AST code + Terminal OCR** |
| **Chi phí triển khai** | Tài khoản thương mại định kỳ | Bản quyền theo tháng | **Kiến trúc tối ưu: RAG cục bộ + LLM Flash API** |

### 3.2. Phương pháp Sư phạm Socratic (Định hướng tư duy)
Hệ thống sử dụng System Instruction được cấu hình chặt chẽ để kiểm soát hành vi phản hồi của mô hình ngôn ngữ:
* **Nguyên tắc 1:** Tuyệt đối không cung cấp giải pháp mã nguồn hoàn chỉnh ngay từ lượt tương tác đầu tiên.
* **Nguyên tắc 2:** Phân tích triệu chứng lỗi dựa trên đầu vào của sinh viên (dòng phát sinh lỗi, điều kiện dừng, trạng thái bộ nhớ).
* **Nguyên tắc 3:** Đặt từ 1 đến 2 câu hỏi dẫn dắt để sinh viên tự kiểm tra giá trị biến hoặc điều kiện biên.
* **Nguyên tắc 4:** Đối chiếu với đoạn tri thức tương ứng được RAG truy xuất từ giáo trình để người học tự đọc hiểu.

---

# PHẦN 4: KIẾN TRÚC HỆ THỐNG & BIỆN LUẬN CÔNG NGHỆ (SYSTEM ARCHITECTURE & TECH STACK)

### 4.1. Kiến trúc phân tầng tổng thể (Layered Architecture)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. TẦNG TRÌNH DIỄN (PRESENTATION LAYER)                                                │
│    - Next.js 14 (App Router) + TypeScript + Tailwind CSS                               │
│    - Giao diện Chat đa phương thức: Input Text, Upload Code (.py, .cpp, .sql), Upload Ảnh│
│    - Hiển thị phản hồi định dạng Markdown, Code Block và Thẻ trích dẫn (Citations)      │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ HTTP REST API (FastAPI)
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│ 2. TẦNG DỊCH VỤ VÀ ĐIỀU PHỐI (BACKEND & AI ORCHESTRATION LAYER)                       │
│    - FastAPI Engine (Python 3.11, Asynchronous I/O)                                   │
│    - FileExtractor: Bóc tách mã nguồn an toàn (chặn Path Traversal, lọc đuôi mở rộng)   │
│    - ImageExtractor: Tiền xử lý ảnh (Resize, Contrast) + Vision OCR Terminal           │
│    - QuerySynthesizer: Rút trích Exception Name & Hàm lỗi, chống pha loãng truy vấn    │
│    - TutorService: Điều phối luồng RAG + LLM Socratic Engine                           │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                     ┌──────────────────────┴──────────────────────┐
                     ▼                                             ▼
┌─────────────────────────────────────────┐   ┌──────────────────────────────────────────┐
│ 3. TẦNG DỮ LIỆU VECTOR & TÀI LIỆU (RAG) │   │ 4. TẦNG MÔ HÌNH SUY LUẬN (LLM ENGINE)    │
│    - ChromaDB Persistent (Local Vector) │   │    - Mô hình chính: Gemini 3 Flash       │
│    - Dual Collections (5.230 vectors):  │   │    - Cơ chế Multi-Model Resilience:      │
│      * qwen3_text: 4.293 chunks lý thuyết│   │      gemini-3-flash-preview             │
│      * jina_code: 937 chunks mã nguồn   │   │      --> gemini-3.5-flash                │
│    - Thuật toán xếp hạng: RRF (k0=60)   │   │      --> Socratic Fallback nội bộ        │
└─────────────────────────────────────────┘   └──────────────────────────────────────────┘
```

### 4.2. Biện luận lựa chọn công nghệ và phân tích đánh đổi (Trade-offs)

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 MA TRẬN BIỆN LUẬN CÔNG NGHỆ CỦA DỰ ÁN                                  │
├──────────────────────┬─────────────────────────────┬───────────────────────────┬───────────────────────┤
│ THÀNH PHẦN KIẾN TRÚC │ CÔNG NGHỆ ĐƯỢC CHỌN         │ CÔNG NGHỆ SO SÁNH / THỬ   │ LÝ DO KỸ THUẬT & ĐÁNH ĐỔI│
├──────────────────────┼─────────────────────────────┼───────────────────────────┼───────────────────────┤
│ 1. PDF Layout Parser │ MinerU (Layout-LM Vision)   │ PyPDF, PDFPlumber         │ PyPDF làm gãy ranh giới   │
│                      │                             │                           │ khối code và mất thụt lề │
│ 2. Vector Database   │ ChromaDB (Local Persistent) │ Pinecone, Milvus Cluster  │ ChromaDB nhúng gọn nhẹ,   │
│                      │                             │                           │ không tốn phí dịch vụ    │
│ 3. Dual Embedding    │ Qwen3 (Text) + Jina (Code)  │ Single Embedding Model    │ Tách biệt không gian vector│
│                      │ 1024-d / 768-d              │ đơn lẻ                    │ tăng độ khớp theo ngữ cảnh│
│ 4. LLM Generation    │ Gemini 3 Flash API          │ GPT-4o, Llama 3 Local     │ Tốc độ <2s, chi phí thấp;  │
│                      │ (+ Fallback Engine)         │                           │ Llama đòi hỏi GPU đắt đỏ │
│ 5. Backend Engine    │ FastAPI (Asynchronous I/O)  │ Flask, Django Sync        │ Hỗ trợ I/O bất đồng bộ    │
│                      │                             │                           │ xử lý đồng thời nhiều kết nối│
│ 6. Container hóa     │ Docker Compose              │ Cài đặt thủ công từng app │ Đóng gói đồng bộ môi trường│
└──────────────────────┴─────────────────────────────┴───────────────────────────┴───────────────────────┘
```

* **1. Bộ bóc tách PDF (MinerU vs PyPDF):** Thử nghiệm ban đầu với `PyPDF` và `PDFPlumber` cho thấy tỷ lệ lỗi cấu trúc cao đối với sách lập trình (mất thụt lề của Python, bảng độ phức tạp bị vỡ cột). Dự án sử dụng MinerU với mô hình thị giác Layout-LM giúp bảo toàn 100% định dạng khối mã nguồn và công thức toán học LaTeX.
* **2. Cơ sở dữ liệu Vector (ChromaDB vs Cloud Vector DB):** Thay vì sử dụng các dịch vụ SaaS đám mây thương mại (như Pinecone tốn phí định kỳ), hệ thống sử dụng ChromaDB triển khai cục bộ qua Persistent Client, tốc độ truy xuất đạt **~160 ms/truy vấn**, hỗ trợ metadata filtering linh hoạt theo ngôn ngữ và tài liệu.
* **3. Kiến trúc Embedding Dual-Collection (Qwen3-Embedding & Jina-Code):** Nhóm áp dụng mô hình nhúng kép:
  * Collection `qwen3_text` sử dụng `Qwen/Qwen3-Embedding-0.6B` (1024 chiều) chuyên trách văn bản lý thuyết và giải thích khái niệm.
  * Collection `jina_code` sử dụng `jinaai/jina-embeddings-v2-base-code` (768 chiều) chuyên trách cấu trúc mã nguồn và thuật toán.
  * Hai tập kết quả được hợp nhất bằng thuật toán **Reciprocal Rank Fusion (RRF)** với hằng số $k_0 = 60$.
* **4. Lựa chọn Mô hình Ngôn ngữ (Gemini 3 Flash & Multi-Model Resilience):** Mô hình Gemini 3 Flash được lựa chọn do có độ trễ suy luận thấp (< 2 giây), cửa sổ ngữ cảnh lớn và hỗ trợ tốt xử lý ảnh đa phương thức với chi phí token tối ưu. Hệ thống cài đặt cơ chế dự phòng tự động chuyển đổi mô hình (Gemini 3 Flash $\rightarrow$ Gemini 3.5 Flash $\rightarrow$ Socratic Fallback nội bộ) để đảm bảo hệ thống không bị gián đoạn khi gặp lỗi kết nối hoặc quota API.

### 4.3. Mô hình triển khai Hybrid và phạm vi bảo mật thực tế
* **Kiến trúc triển khai thực tế là mô hình Lai (Hybrid Architecture):**
  * **Thành phần chạy On-Premise / Cục bộ:** Toàn bộ Backend (FastAPI), Cơ sở dữ liệu Vector (ChromaDB với 5.230 vectors), Bộ trích xuất mã nguồn (FileExtractor), Bộ tiền xử lý ảnh (ImageExtractor), Thuật toán chống pha loãng (QuerySynthesizer) và Frontend (Next.js) đều được đóng gói và vận hành cục bộ thông qua Docker Compose.
  * **Thành phần sử dụng Cloud API:** Bước sinh phản hồi Socratic cuối cùng gọi thông qua Google Gemini API.
* **Lưu ý bảo mật khách quan:** Dữ liệu ngữ cảnh hợp nhất (gồm prompt của sinh viên, mã nguồn đính kèm và trích đoạn lỗi terminal) được gửi tới endpoint của Google Gemini để sinh phản hồi. Do đó, hệ thống hiện tại **chưa phải là mô hình cô lập hoàn toàn (Air-gapped 100% On-premise)**.
* **Định hướng bảo mật trong tương lai:** Để đáp ứng yêu cầu bảo mật tuyệt đối cho dữ liệu thi cử nội bộ, giải pháp tiếp theo là thay thế endpoint Gemini API bằng mô hình mã nguồn mở chạy On-Premise hoàn toàn (như Qwen2.5-Coder hoặc Llama-3-Instruct thông qua vLLM / Ollama trên máy chủ trang bị GPU chuyên dụng).

---

# PHẦN 5: QUY TRÌNH NGHIÊN CỨU & XÂY DỰNG HỆ THỐNG RAG ĐA PHƯƠNG THỨC

Quy trình nghiên cứu và triển khai kỹ thuật được thực hiện tuần tự qua 4 giai đoạn chính:

```
┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│  GIAI ĐOẠN 1         │     │  GIAI ĐOẠN 2         │     │  GIAI ĐOẠN 3         │     │  GIAI ĐOẠN 4         │
│  Thu thập & Xử lý    │ ──> │  Embedding, Vector DB│ ──> │  Multimodal & Chống  │ ──> │  Socratic Tutor,     │
│  Dữ liệu SOTA        │     │  & Đo đạc Benchmark  │     │  Pha Loãng Truy Vấn  │     │  Kiểm thử & Đóng gói │
└──────────────────────┘     └──────────────────────┘     └──────────────────────┘     └──────────────────────┘
```

### Giai đoạn 1: Chuẩn bị dữ liệu giáo trình, bóc tách và phân đoạn ngữ cảnh
1. **Thu thập giáo trình chính thống:** Tuyển chọn và thẩm định các giáo trình chuẩn mực về C/C++, Python, Cấu trúc dữ liệu & Giải thuật và Cơ sở dữ liệu.
2. **Bóc tách bố cục bằng MinerU:** Chuyển đổi toàn bộ tài liệu PDF sang Markdown chuẩn, bảo toàn cấu trúc phân cấp tiêu đề, các khối mã nguồn đa dòng và công thức toán học.
3. **Làm sạch dữ liệu đa tầng:** Sử dụng bộ lọc biểu thức chính quy (Regex) loại bỏ số trang, tiêu đề đầu trang/chân trang lặp lại và chuẩn hóa bảng mã UTF-8.
4. **Phân đoạn ngữ cảnh (Contextual Chunking):** Phân chia đoạn dựa trên ranh giới ngữ nghĩa (tiêu đề chương mục, ranh giới hàm/lớp), đồng thời bổ sung thông tin ngữ cảnh cấp cao (`section_path`, `source_file`, `language`) vào metadata của từng chunk để tránh hiện tượng mất ngữ cảnh khi tìm kiếm vector.

### Giai đoạn 2: Tạo không gian Vector Dual-Collection và Kiểm định chất lượng truy xuất
1. **Embedding và nạp dữ liệu ChromaDB:** Chuyển hóa toàn bộ kho tri thức thành **5.230 chunks** lưu trữ tại `data/09_chromadb`:
   * Collection `qwen3_text`: 4.293 chunks văn bản lý thuyết (1024 chiều).
   * Collection `jina_code`: 937 chunks mã nguồn và thuật toán (768 chiều).
2. **Đo đạc Benchmark Ground Truth:** Xây dựng bộ 20 câu hỏi kiểm định canonical (`rag_eval_queries.json`) đối soát trực tiếp với ground truth ID chunk, kiểm thử song song 3 chiến lược truy vấn (Baseline RRF, Metadata Filtered, Lexical-Semantic Rescoring).
3. **Đóng gói dịch vụ RAGService:** Tích hợp tính năng tự động nhận diện ngôn ngữ lập trình từ câu hỏi và tự động mở rộng truy vấn (Query Expansion).

### Giai đoạn 3: Xây dựng Pipeline Đa phương thức và Module chống pha loãng truy vấn
1. **Xử lý tệp mã nguồn (FileExtractor):** Tiếp nhận và bóc tách các tệp mã nguồn (`.py`, `.cpp`, `.sql`, `.java`), áp dụng cơ chế xác thực an toàn: chặn tấn công duyệt thư mục (Path Traversal), chặn tệp nhị phân giả mạo và giới hạn kích thước tối đa 5MB.
2. **Xử lý hình ảnh lỗi Terminal (ImageExtractor):** Tiền xử lý kích thước (tối đa 1600px), cân bằng độ tương phản, áp dụng mô hình Vision để đọc chính xác font Monospace và trích xuất chuỗi Callstack lỗi từ ảnh chụp màn hình.
3. **Kỹ thuật chống pha loãng truy vấn (QuerySynthesizer):**
   * *Hiện tượng pha loãng (Query Dilution):* Khi sinh viên gửi đồng thời câu hỏi, file code 200 dòng và ảnh màn hình, việc nhồi toàn bộ văn bản vào vector search sẽ tạo ra độ nhiễu lớn từ các dòng log hệ thống và đường dẫn tệp.
   * *Giải pháp:* Thuật toán rút trích trọng tâm: phân tách chính xác tên ngoại lệ (`IndexError`, `NullPointerException`, `Segmentation Fault`), vị trí hàm lỗi và ngôn ngữ lập trình để tạo thành câu truy vấn kỹ thuật tinh gọn trước khi gọi RAG.

### Giai đoạn 4: Tích hợp Socratic Engine, Kiểm thử toàn diện và Đóng gói
1. **Cấu hình Socratic Engine:** Tích hợp System Instruction chuẩn mực sư phạm vào mô hình Gemini 3 Flash, thiết lập fallback phản hồi cục bộ khi mất kết nối mạng.
2. **Kiểm thử tự động hóa:** Xây dựng bộ 33 Unit Tests và 30 kịch bản tích hợp End-to-End kiểm tra toàn bộ luồng nghiệp vụ.
3. **Đóng gói Docker Compose:** Hoàn thiện tệp `docker-compose.yml` tích hợp Backend, ChromaDB volume và Frontend, sẵn sàng khởi chạy đồng bộ.

---

# PHẦN 6: KẾT QUẢ THỰC NGHIỆM VÀ KIỂM CHỨNG CHẤT LƯỢNG (EVALUATION & VERIFICATION)

Hệ thống được đánh giá khách quan thông qua hai bộ số liệu thực nghiệm: **Kiểm định chất lượng truy xuất RAG** và **Kiểm thử tự động hóa toàn trình (Automated Testing)**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              BẢNG TỔNG HỢP SỐ LIỆU THỰC NGHIỆM                         │
├──────────────────────────────────┬──────────────────────┬──────────────────────────────┤
│ CHỈ SỐ ĐO LƯỜNG                  │ KẾT QUẢ XÁC MINH     │ CĂN CỨ VÀ PHƯƠNG PHÁP ĐO     │
├──────────────────────────────────┼──────────────────────┼──────────────────────────────┤
│ 1. Quy mô cơ sở dữ liệu Vector   │ 5.230 chunks vector  │ data/09_chromadb             │
│    - qwen3_text (Văn bản lý thuyết)│ 4.293 chunks (1024-d)│ Qwen/Qwen3-Embedding-0.6B    │
│    - jina_code (Mã nguồn/thuật toán)│ 937 chunks (768-d)   │ jina-embeddings-v2-base-code │
│ 2. Retrieval Hit Rate@3          │ 100.00% (20/20 câu)  │ reports/rag_evaluation_day6  │
│ 3. Retrieval Hit Rate@1          │ 80.00% (16/20 câu)   │ reports/rag_evaluation_day6  │
│ 4. Mean Reciprocal Rank (MRR@5)  │ 0.8833               │ reports/rag_evaluation_day6  │
│ 5. Độ trễ trung bình truy xuất   │ ~160 ms / truy vấn   │ Đo đạc trên môi trường local │
│ 6. Unit Tests tự động            │ 33 / 33 PASSED (100%)│ tests/test_rag, file, image  │
│ 7. End-to-End Integration Tests  │ 30 / 30 PASSED (100%)│ tests/test_day13_e2e         │
│ 8. Tổng số kịch bản kiểm thử     │ 63 / 63 PASSED (100%)│ Thực thi qua Pytest          │
└──────────────────────────────────┴──────────────────────┴──────────────────────────────┘
```

### 6.1. Chi tiết kiểm định chất lượng RAG Retrieval (DoD Milestone 1)
* **Tập dữ liệu đánh giá:** 20 câu hỏi kiểm chuẩn (`rag_eval_queries.json`) phân bổ đều trên 4 nhóm năng lực lập trình:
  * `theory` (5 câu): Khái niệm hướng đối tượng, quy chuẩn PEP 8, tính bất biến của dữ liệu.
  * `code` (5 câu): Cú pháp giải thuật, đệ quy, quản lý tài nguyên.
  * `api` (5 câu): Thư viện chuẩn, hàm tích hợp sẵn, xử lý dữ liệu.
  * `hybrid` (5 câu): Tích hợp lý thuyết và mã nguồn phức hợp.
* **Kết quả đo lường:**
  * **Hit Rate@3 = 100.00%:** Trong toàn bộ 20 câu hỏi kiểm định, tài liệu tham chiếu chuẩn xác đều xuất hiện trong Top 3 kết quả tìm kiếm.
  * **Hit Rate@1 = 80.00%:** Có 16/20 câu hỏi tìm thấy tài liệu đúng ngay ở vị trí xếp hạng đầu tiên.
  * **MRR@5 = 0.8833:** Điểm xếp hạng nghịch đảo trung bình đạt mức cao, phản ánh độ chính xác của thuật toán RRF trong việc đưa tài liệu phù hợp lên đầu.

### 6.2. Kết quả bộ kiểm thử tự động hóa (63 bài test Pytest)
* **Bộ 33 Unit Tests (Thực thi trong ~4.1s):**
  * `test_rag_service.py` (9 tests): Kiểm tra khởi tạo 5.230 vectors, tìm kiếm RRF, lọc metadata, fallback câu hỏi mới.
  * `test_file_extractor.py` (8 tests): Kiểm tra bóc tách đa ngôn ngữ, giới hạn 5MB, ngăn chặn Path Traversal, chặn tệp giả mạo.
  * `test_image_extractor.py` (8 tests): Kiểm tra nhận diện định dạng ảnh, tiền xử lý kích thước, OCR trích xuất lỗi terminal.
  * `test_query_synthesizer.py` (8 tests): Kiểm tra cơ chế chống pha loãng truy vấn, nhận diện ngôn ngữ, cấu trúc payload hợp nhất.
* **Bộ 30 End-to-End Scenarios Tests (Thực thi trong ~30.5s):**
  * 10 kịch bản câu hỏi lý thuyết thuật toán và cú pháp thuần văn bản.
  * 10 kịch bản gửi kèm mã nguồn lỗi thực tế (Memory leak C++, đệ quy vô hạn, SQL injection, off-by-one).
  * 10 kịch bản gửi ảnh chụp màn hình terminal chứa lỗi runtime (`IndexError`, `ZeroDivisionError`, `Segmentation Fault`).
* **Tổng kết:** **63/63 bài kiểm thử đạt 100%**, xác nhận tính ổn định của toàn bộ luồng xử lý từ tiếp nhận dữ liệu đến sinh kết quả.

### 6.3. Minh chứng 3 kịch bản vận hành thực tế
1. **Kịch bản 1 (Lý thuyết):** Sinh viên hỏi: *"Tại sao QuickSort có trường hợp xấu nhất $O(n^2)$?"* $\rightarrow$ Hệ thống trích xuất giáo trình Cấu trúc dữ liệu & Giải thuật, giải thích hiện tượng chọn Pivot lệch và gợi ý sinh viên tìm hiểu kỹ thuật chọn chốt trung vị của 3 phần tử (Median-of-Three).
2. **Kịch bản 2 (Đính kèm mã nguồn C++):** Sinh viên nộp tệp mã nguồn cấp phát mảng động `new int[100]` nhưng không gọi `delete[]`. $\rightarrow$ Hệ thống nhận diện hàm xử lý bộ nhớ, không sửa code hộ mà đặt câu hỏi gợi ý sinh viên kiểm tra việc thu hồi vùng nhớ Heap trước khi kết thúc hàm.
3. **Kịch bản 3 (Đính kèm ảnh Terminal OCR):** Sinh viên gửi ảnh chụp màn hình lỗi `IndexError: list index out of range`. $\rightarrow$ Hệ thống nhận diện exception, đối chiếu giáo trình Python và hướng dẫn sinh viên kiểm tra điều kiện biên của vòng lặp duyệt mảng.

---

# PHẦN 7: HIỆN TRẠNG TRIỂN KHAI, HẠN CHẾ VÀ HƯỚNG PHÁT TRIỂN (STATUS, LIMITATIONS & ROADMAP)

Để đảm bảo tính trung thực học thuật trước Hội đồng, các tính năng được phân định rõ ràng giữa **kết quả đã hoàn thành**, **thành phần đang phát triển (UI Prototype)** và **định hướng tương lai**:

### 7.1. Bảng phân loại trạng thái triển khai tính năng thực tế

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 BẢNG ĐỐI CHIẾU TRẠNG THÁI TRIỂN KHAI TÍNH NĂNG                         │
├───────────────────────────────┬────────────────────────────┬───────────────────────────────────────────┤
│ TÍNH NĂNG                     │ TRẠNG THÁI TRIỂN KHAI      │ MÔ TẢ HIỆN TRẠNG TRONG MÃ NGUỒN           │
├───────────────────────────────┼────────────────────────────┼───────────────────────────────────────────┤
│ 1. Multimodal RAG Engine      │ ✅ ĐÃ HOÀN THÀNH           │ 5.230 vectors, Dual-Collection RRF        │
│ 2. Socratic Prompting & LLM   │ ✅ ĐÃ HOÀN THÀNH           │ Gemini 3 Flash + Socratic System Prompt   │
│ 3. File & Image OCR Extractor │ ✅ ĐÃ HOÀN THÀNH           │ Bóc tách code an toàn + Vision OCR        │
│ 4. Query Synthesizer          │ ✅ ĐÃ HOÀN THÀNH           │ Trích xuất lỗi, chống pha loãng ngữ cảnh  │
│ 5. Kiểm thử tự động Pytest    │ ✅ ĐÃ HOÀN THÀNH           │ 63/63 tests passed (33 unit + 30 e2e)     │
│ 6. Đóng gói Docker Compose    │ ✅ ĐÃ HOÀN THÀNH           │ docker-compose.yml chạy đồng bộ services  │
│ 7. Giao diện Chat Sinh viên   │ ✅ ĐÃ HOÀN THÀNH           │ Next.js kết nối đầy đủ API Chat/Multimodal│
├───────────────────────────────┼────────────────────────────┼───────────────────────────────────────────┤
│ 8. Instructor Dashboard       │ 🟡 ĐANG PHÁT TRIỂN         │ Đã có giao diện mẫu (UI Prototype React),  │
│                               │    (GIAO DIỆN MẪU / DEMO)  │ chưa có API tổng hợp dữ liệu từ PostgreSQL│
│ 9. Classroom Error Heatmap    │ 🟡 ĐANG PHÁT TRIỂN         │ Bản đồ nhiệt hiển thị dữ liệu giả lập,    │
│                               │    (GIAO DIỆN MẪU / DEMO)  │ Backend chưa có schema lưu trữ log lỗi    │
│ 10. Metadata Filter theo Ngôn ngữ│ ✅ ĐÃ HOÀN THÀNH        │ Lọc metadata `language` trong ChromaDB    │
│ 11. Khóa tài liệu theo Tuần học │ 🔵 ĐỊNH HƯỚNG PHÁT TRIỂN  │ Chưa có trường `week` trong metadata,     │
│                               │    (ROADMAP)               │ đề xuất mở rộng từ bộ lọc `section_path`  │
│ 12. Sandbox chạy code trực tiếp│ 🔵 ĐỊNH HƯỚNG PHÁT TRIỂN  │ Chưa có container sandbox thực thi mã     │
│                               │    (ROADMAP)               │ sinh viên an toàn trên backend            │
│ 13. Phân quyền Người dùng RBAC │ 🔵 ĐỊNH HƯỚNG PHÁT TRIỂN  │ Chưa triển khai hệ thống xác thực JWT     │
│                               │    (ROADMAP)               │ và phân quyền Student/Instructor/Admin    │
└───────────────────────────────┴────────────────────────────┴───────────────────────────────────────────┘
```

### 7.2. Các hạn chế kỹ thuật hiện tại
* **1. Phụ thuộc vào Cloud API cho tầng sinh ngôn ngữ:** Mặc dù kho tri thức vector và toàn bộ pipeline tiền xử lý chạy cục bộ, bước sinh câu trả lời vẫn phụ thuộc vào Google Gemini API. Do đó, hệ thống yêu cầu kết nối Internet cho backend và dữ liệu câu hỏi được truyền ra ngoài máy chủ nội bộ.
* **2. Chất lượng OCR đối với ảnh chụp thực tế phức tạp:** Mô hình Vision OCR hoạt động tối ưu với ảnh chụp màn hình máy tính (screenshot rõ nét). Đối với ảnh chụp từ điện thoại bị nghiêng góc 3D, lóa ánh sáng đèn hoặc mờ nét chữ, độ chính xác nhận diện ký tự đặc biệt trong mã nguồn có thể suy giảm.
* **3. Chưa có môi trường thực thi mã nguồn an toàn (Execution Sandbox):** Hệ thống hiện phân tích lỗi dựa trên kỹ thuật bóc tách tĩnh (Static Analysis) và suy luận của LLM, chưa tích hợp máy chủ chấm bài hoặc môi trường cô lập để biên dịch và chạy thử mã nguồn thực tế của sinh viên.
* **4. Phạm vi ngữ liệu giáo trình:** Dữ liệu hiện tập trung vào 4 học phần lập trình cơ sở của 2 năm đầu, chưa mở rộng ra toàn bộ chương trình đào tạo chuyên ngành.

### 7.3. Hướng phát triển trong tương lai
* **Triển khai mô hình ngôn ngữ On-Premise hoàn toàn:** Nghiên cứu tích hợp các mô hình mã nguồn mở chuyên biệt cho lập trình (như Qwen2.5-Coder hoặc Llama-3-Instruct) vận hành cục bộ thông qua vLLM trên máy chủ của trường, loại bỏ hoàn toàn việc gửi dữ liệu ra API bên thứ ba.
* **Tích hợp Backend Execution Sandbox:** Xây dựng môi trường Docker/gVisor sandbox cô lập để hỗ trợ sinh viên bấm nút chạy thử code trực tiếp và nhận kết quả kiểm thử ngay trên giao diện web.
* **Hoàn thiện hệ thống Quản lý Đào tạo (LMS Integration & Error Analytics):**
  * Xây dựng cơ sở dữ liệu PostgreSQL lưu trữ lịch sử tương tác và nhật ký lỗi của từng sinh viên.
  * Hiện thực hóa API tính toán bản đồ nhiệt lỗ hổng kiến thức (Classroom Error Heatmap) theo thời gian thực để hỗ trợ giảng viên theo dõi tiến độ học tập của lớp.
  * Bổ sung trường `syllabus_week` vào metadata vector để hỗ trợ giảng viên khóa và mở tài liệu chính xác theo tuần học.
  * Tích hợp chuẩn LTI (Learning Tools Interoperability) để kết nối đồng bộ với hệ thống LMS Moodle hoặc Canvas của nhà trường.

---

# PHẦN 8: KẾT LUẬN & ĐÓNG GÓP CỦA ĐỒ ÁN

### 8.1. Các kết quả chính đã đạt được
1. **Xây dựng hoàn chỉnh Pipeline RAG chuyên biệt cho giáo dục lập trình:** Thu thập, làm sạch và phân đoạn chuẩn hóa kho tài liệu giáo trình đại học thành 5.230 chunks vector đa không gian (Qwen3-Embedding & Jina-Code), đạt tỷ lệ truy xuất **100% Hit@3** trên bộ kiểm chuẩn 20 câu hỏi canonical.
2. **Hiện thực hóa Phương pháp Sư phạm Socratic:** Thiết lập thành công cơ chế trợ giảng định hướng tư duy, kiên quyết không làm bài hộ, giúp sinh viên nâng cao năng lực tự học và tự gỡ lỗi.
3. **Giải quyết bài toán đầu vào đa phương thức:** Xây dựng module trích xuất mã nguồn bảo mật kết hợp Vision OCR và thuật toán Query Synthesizer chống pha loãng truy vấn.
4. **Kiểm chứng kỹ thuật nghiêm ngặt:** Toàn bộ hệ thống vượt qua **63/63 bài kiểm thử tự động (100% Pass)** và được đóng gói hoàn chỉnh bằng Docker Compose sẵn sàng triển khai.

### 8.2. Ý nghĩa thực tiễn
Đề tài cung cấp một giải pháp công nghệ giáo dục (EdTech) có tính ứng dụng cao, góp phần giải quyết mâu thuẫn giữa xu thế ứng dụng AI tạo sinh và yêu cầu giữ vững chất lượng đào tạo, rèn luyện tư duy độc lập cho sinh viên ngành Công nghệ Thông tin.

# TÀI LIỆU TOÀN DIỆN THUYẾT TRÌNH BẢO VỆ ĐỒ ÁN TRƯỚC HỘI ĐỒNG
## HỆ THỐNG TRỢ GIẢNG LẬP TRÌNH THÔNG MINH ĐA PHƯƠNG THỨC (AI-POWERED CODING TUTOR & MULTIMODAL RAG)

---

# PHẦN 1: TẠI SAO CẦN THỰC HIỆN DỰ ÁN? (TÍNH CẤP THIẾT & BỐI CẢNH THỰC TẾ)

```
┌────────────────────────────────────────┐       ┌────────────────────────────────────────┐
│     THỰC TRẠNG GIẢNG DẠY HIỆN NAY      │       │     NHU CẦU CẤP THIẾT CỦA ĐỀ TÀI       │
├────────────────────────────────────────┤       ├────────────────────────────────────────┤
│ ⚠️ Sinh viên bế tắc khi tự debug ở nhà │  ──>  │ ✅ Cần Trợ giảng Sư phạm AI 24/7       │
│ ⚠️ ChatGPT mớm code, triệt tiêu tư duy │  ──>  │ ✅ Cần AI gợi mở, không viết code sẵn  │
│ ⚠️ AI trôi nổi dùng cú pháp lệch chuẩn │  ──>  │ ✅ Cần AI neo chặt vào giáo trình khoa│
│ ⚠️ Giảng viên mù tịt về lỗi của cả lớp │  ──>  │ ✅ Cần Dashboard báo cáo lỗi học tập   │
└────────────────────────────────────────┘       └────────────────────────────────────────┘
```

### 1. Bế tắc của sinh viên khi tự học lập trình tại nhà (The Homework Debugging Barrier)
* **Đặc thù môn học:** Các môn lập trình cơ sở (Lập trình C/C++, Python, Cấu trúc dữ liệu & Giải thuật) có độ dốc học tập (learning curve) rất lớn. Sinh viên năm nhất - năm hai thường xuyên đối mặt với các khái niệm trừu tượng: con trỏ, cấp phát động, quản lý bộ nhớ Heap/Stack, đệ quy.
* **Nỗi cô đơn khi làm bài tập:** Khi thực hành code lúc nửa đêm tại nhà, sinh viên gặp các lỗi runtime kinh điển như `Segmentation Fault`, `Memory Leak`, `IndexError` mà không có giảng viên hay trợ giảng túc trực để giải đáp. Việc bế tắc hàng giờ đồng hồ trước một dòng lỗi vô hình khiến sinh viên nản chí, sợ học lập trình và tỷ lệ rớt môn các môn này ở các trường đại học luôn ở mức cao.

### 2. Mặt trái nguy hại của các AI tạo sinh thương mại (The Dark Side of Commercial AI in Coding Education)
* **Hiện tượng "Mớm code / Làm bài hộ":** Sự bùng nổ của ChatGPT, GitHub Copilot hay Claude mang lại sự tiện lợi, nhưng lại tạo ra hệ lụy nghiêm trọng trong giáo dục. Khi sinh viên gặp lỗi, các AI này sẽ viết lại nguyên cả hàm code hoàn chỉnh. Sinh viên chỉ việc Copy - Paste nộp bài.
* **Hậu quả học thuật:** Sinh viên nộp bài tập về nhà 10/10 điểm, nhưng khi bước vào phòng thi viết trên giấy hoặc thi thực hành máy cô lập không có Internet thì bị 0 điểm. Sinh viên hoàn toàn mất đi phản xạ tư duy thuật toán và kỹ năng tự sửa lỗi (debugging) - kỹ năng sống còn của một kỹ sư phần mềm.
* **Thầy cô rơi vào thế bị động:** Giảng viên không thể cấm sinh viên dùng AI ở nhà, nhưng cũng bất lực trong việc kiểm soát mức độ lạm dụng AI của sinh viên.

### 3. Nhu cầu cấp thiết về một Giải pháp AI Sư phạm Chuẩn mực cho Nhà trường (The Need for an Institutional AI Tutor)
* **Xu thế không thể đảo ngược:** Nhà trường không thể bài trừ AI, mà bắt buộc phải có một giải pháp **"Sống chung với AI một cách có kiểm soát"**.
* **Định vị của đề tài:** Dự án này ra đời để giải quyết bài toán đó: Xây dựng một **Trợ giảng AI chuẩn mực Sư phạm (Socratic AI Tutor)** cài đặt nội bộ cho Nhà trường. AI không làm bài hộ mà đóng vai trò người thầy dẫn dắt, giải thích bản chất lỗi dựa trên đúng cuốn giáo trình của trường, và buộc sinh viên phải tự tay sửa từng dòng code của chính mình.

---

# PHẦN 2: DỰ ÁN NÀY DÙNG ĐỂ LÀM GÌ? (ỨNG DỤNG THỰC TẾ)

Dự án này là một **"Hệ sinh thái Trợ giảng Lập trình Thông minh & Quản lý Học tập Đa phương thức"**, được thiết kế để triển khai nội bộ cho Khoa Công nghệ Thông tin tại các trường Đại học:

* **Đối với Sinh viên (Trợ giảng số 24/7):**
  * Khi sinh viên làm bài tập hoặc thực hành code ở nhà lúc nửa đêm bị lỗi: Sinh viên chỉ cần **quăng file code (`.py`, `.cpp`, `.sql`)** hoặc **chụp ảnh màn hình Terminal báo lỗi** tải lên.
  * Hệ thống sẽ đọc ảnh lỗi (Vision OCR) + đọc mã nguồn + tra cứu đúng giáo trình đại học của trường, sau đó **đặt câu hỏi gợi mở, phân tích nguyên nhân để sinh viên tự tìm ra chỗ sai và tự sửa**.
* **Đối với Giảng viên & Nhà trường (Công cụ Quản trị Đào tạo & Báo cáo chất lượng):**
  * Đóng vai trò như một bảng điều khiển trung tâm giúp Giảng viên **nắm bắt được bức tranh toàn cảnh về năng lực học tập của cả lớp**: biết sinh viên đang mắc kẹt ở đâu, giới hạn phạm vi tài liệu theo từng tuần học, và giám sát tính trung thực học thuật.

---

# PHẦN 3: NÓ GIẢI QUYẾT ĐƯỢC GÌ MÀ CÁC AI KHÁC (ChatGPT, GitHub Copilot, NotebookLM) CHƯA LÀM ĐƯỢC?

Khi đưa các AI thông thường vào môi trường giáo dục đại học, cả sinh viên và giảng viên đều gặp phải **5 "NỖI ĐAU" LỚN** mà các công cụ như ChatGPT hay Copilot hoàn toàn bất lực:

```
┌────────────────────────────────────────┐       ┌────────────────────────────────────────┐
│     CHATGPT / COPILOT / CUSTOM GPTS    │       │     HỆ THỐNG AI CODING TUTOR CỦA BẠN   │
├────────────────────────────────────────┤       ├────────────────────────────────────────┤
│ ❌ Giải bài hộ, làm mất tư duy debug   │  VS   │ ✅ Gợi mở Sư phạm (Socratic Tutoring)  │
│ ❌ Ảo giác kiến thức, sinh code lệch đề│       │ ✅ Neo chặt giáo trình (100% Hit@3 RAG)│
│ ❌ Loãng ngữ cảnh khi gửi code + ảnh   │       │ ✅ Query Synthesizer chống pha loãng   │
│ ❌ "Hộp đen cá nhân" (Thầy cô mù tịt) │       │ ✅ Bản đồ nhiệt lỗ hổng lớp học        │
│ ❌ AI lôi kiến thức cuối kỳ giải đầu kỳ│       │ ✅ Khóa tài liệu theo tiến độ từng tuần│
└────────────────────────────────────────┘       └────────────────────────────────────────┘
```

### 1. Vấn đề Sư phạm: Các AI khác "Mớm code, giải bài hộ" làm cùn mòn tư duy
* **Hạn chế của ChatGPT/Copilot:** Sinh viên chỉ cần ném lỗi vào là AI viết lại nguyên cả hàm code hoàn chỉnh. Sinh viên Copy-Paste nộp bài đối phó $\rightarrow$ Không hiểu bản chất, mất kỹ năng tự sửa lỗi (debugging), đi thi viết giấy là rớt.
* **Hệ thống của bạn giải quyết:** AI hoạt động theo **Phương pháp Sư phạm Socratic**: **Tuyệt đối không đưa code hoàn chỉnh**. Hệ thống chỉ ra dòng bị lỗi logic, giải thích bản chất nguyên nhân, và đặt câu hỏi gợi ý từng bước để sinh viên **tự tay gõ lại code của chính mình**.

### 2. Vấn đề Học thuật: Các AI khác bị "Ảo giác" và "Lệch chuẩn giáo trình thi"
* **Hạn chế của ChatGPT:** Học từ toàn bộ Internet mở. Khi sinh viên năm nhất học C/C++ (yêu cầu dùng con trỏ thô, mảng động theo chuẩn môn học), ChatGPT lại sinh ra C++20 (`std::unique_ptr`, `vector`, `auto`) hoặc dùng thư viện ngoài bị cấm trong kỳ thi. Sinh viên mang đi chấm bị **0 điểm**.
* **Hệ thống của bạn giải quyết:** Ứng dụng **RAG (Retrieval-Augmented Generation)** neo chặt vào **Kho 1.221 đoạn tri thức từ chính giáo trình đại học của trường** (đã qua bóc tách SOTA MinerU bảo toàn 100% code block). Khi trả lời, AI hiển thị thẻ trích dẫn rõ: *"Theo Giáo trình C++ ĐHQG, Chương 4, mục Cấp phát động..."*. Đảm bảo code sinh viên viết ra **đúng 100% barem chấm thi của khoa**.

### 3. Vấn đề Kỹ thuật: Các AI khác bị "Pha loãng ngữ cảnh" khi gửi vừa ảnh vừa code
* **Hạn chế của ChatGPT/Claude:** Khi sinh viên vừa gửi câu hỏi, vừa đính kèm file code 200 dòng, vừa gửi ảnh Terminal (chứa cả path dài, log hệ thống), AI thông thường bị hiện tượng *"Lost in the middle"* (loãng ngữ cảnh) — trả lời lan man hoặc bỏ qua lỗi chính.
* **Hệ thống của bạn giải quyết:** Xây dựng riêng module **Query Synthesizer (Chống pha loãng truy vấn)**:
  * Trích xuất chính xác mã ngoại lệ từ ảnh Terminal OCR (`IndexError`, `Memory Leak`, `Segmentation Fault`).
  * Trích xuất hàm bị lỗi từ tệp nguồn.
  * Cô đọng thành từ khóa kỹ thuật chuẩn mực để truy vấn đúng bài học lý thuyết trước khi sinh viên nhận câu trả lời.

### 4. Vấn đề Quản lý: Các AI khác là "Hộp đen cá nhân", Giảng viên hoàn toàn mù tịt
* **Hạn chế của ChatGPT / Custom GPT:** Sinh viên hỏi gì thì chỉ sinh viên đó và OpenAI biết. Giảng viên **không hề biết** sinh viên về nhà có hiểu bài không, đang bị kẹt ở phần nào, cho đến khi chấm thi giữa kỳ thì cả lớp đã trượt hàng loạt.
* **Hệ thống của bạn giải quyết:** Toàn bộ dữ liệu lỗi được ghi nhận tại cơ sở dữ liệu nội bộ (PostgreSQL) để cung cấp **"Bản đồ nhiệt lỗ hổng kiến thức" (Classroom Error Heatmap) cho Giảng viên**:
  * Báo cáo định lượng: *"Tuần này 65% sinh viên mắc lỗi rò rỉ bộ nhớ ở bài tập số 3"*. Giảng viên biết ngay để dành 15 phút đầu giờ lên lớp giảng lại phần đó.
  * Cảnh báo sớm các sinh viên yếu, liên tục mắc lỗi cú pháp để trợ giảng kèm cặp kịp thời.

### 5. Vấn đề Kiểm soát & Bảo mật: Khóa tài liệu theo tuần và Bảo mật đề thi (On-Premise)
* **Hạn chế của ChatGPT / NotebookLM:**
  * Nếu nạp tài liệu vào ChatGPT, sinh viên làm bài tập Tuần 2 nhưng AI lại lôi kiến thức Tuần 10 ra giải hộ $\rightarrow$ Phá nát lộ trình sư phạm.
  * Ngân hàng đề thi nội bộ của trường **không thể tải lên OpenAI** vì vi phạm bảo mật dữ liệu.
* **Hệ thống của bạn giải quyết:**
  * **Khóa tri thức theo tiến độ (Curriculum Scoping):** Nhờ bộ lọc metadata ChromaDB, Giảng viên có quyền cấu hình: *"Bài tập này AI chỉ được dùng tri thức từ Chương 1 đến Chương 3"*. AI tuyệt đối không được dùng kiến thức vượt rào.
  * **Chủ quyền dữ liệu (Docker On-Premise):** Toàn bộ hệ thống đóng gói chạy nội bộ trên máy chủ của trường, không sợ rò rỉ đề thi ra ngoài Internet.

---

# PHẦN 4: NHÓM ĐÃ NGHIÊN CỨU VÀ XÂY DỰNG HỆ THỐNG NHƯ THẾ NÀO? (4 GIAI ĐOẠN CHI TIẾT)

Nhóm tiếp cận dự án theo quy trình Nghiên cứu & Phát triển Kỹ thuật (R&D) bài bản kéo dài qua 14 mốc kỹ thuật (Milestones), chia thành 4 giai đoạn cốt lõi:

```
┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│  GIAI ĐOẠN 1         │     │  GIAI ĐOẠN 2         │     │  GIAI ĐOẠN 3         │     │  GIAI ĐOẠN 4         │
│  Thu thập & Xử lý    │ ──> │  Embedding, Vector DB│ ──> │  Multimodal & Chống  │ ──> │  Socratic Tutor,     │
│  Dữ liệu SOTA        │     │  & Đo đạc Benchmark  │     │  Pha Loãng Truy Vấn  │     │  Kiểm thử & Đóng gói │
└──────────────────────┘     └──────────────────────┘     └──────────────────────┘     └──────────────────────┘
```

### GIAI ĐOẠN 1: THU THẬP, BÓC TÁCH DỮ LIỆU SOTA & CHUNKING NGỮ CẢNH (NGÀY 01 – NGÀY 04)
*Mục tiêu: Xây dựng kho tri thức giáo trình đại học chuẩn hóa, sạch sẽ, bảo toàn 100% cấu trúc code và toán học.*
* **1. Chuẩn bị kho dữ liệu giáo trình chính thống & Môi trường (Ngày 01):**
  * Thu thập và thẩm định các giáo trình chuẩn mực: Cấu trúc dữ liệu & Giải thuật, Lập trình C++, Lập trình Python, Cơ sở dữ liệu.
  * Thiết lập hạ tầng lưu trữ MinIO Object Storage, môi trường Python 3.11, và cấu trúc thư mục dữ liệu đa tầng (`data/01_raw` đến `data/09_chromadb`).
* **2. Bóc tách bố cục PDF phức tạp bằng MinerU (Layout-LM) (Ngày 02):**
  * Khảo sát và loại bỏ các parser truyền thống (PyPDF, PDFPlumber) vì làm vỡ khối code và mất thụt lề (indentation).
  * Ứng dụng mô hình thị giác MinerU để bóc tách chính xác 100% các khối code đa dòng, công thức toán học LaTeX và các bảng biểu cấu trúc phức tạp sang định dạng Markdown.
* **3. Pipeline làm sạch và chuẩn hóa dữ liệu SOTA V3.0 (Ngày 03):**
  * Xây dựng bộ lọc regex đa tầng khử số trang thừa, header/footer lặp lại, sửa lỗi ngắt dòng trong khối lệnh code block.
  * Chuẩn hóa đồng nhất định dạng Markdown và bảng mã UTF-8 cho toàn bộ kho tài liệu.
* **4. Chunking Engine V3.0 – AST-Aware & Anthropic Contextual Retrieval (Ngày 04):**
  * Loại bỏ phương pháp cắt đoạn cố định theo số ký tự (Fixed-size chunking làm gãy nửa chừng hàm code).
  * Cắt đoạn thông minh theo ranh giới hàm/lớp (AST-Aware), kết hợp kỹ thuật Contextual Retrieval của Anthropic: tự động gắn bối cảnh chương mục cấp cao vào đầu mỗi chunk (Ví dụ: `[Tài liệu: C++ | Chương 4: Con trỏ & Cấp phát động | Mục: Thu hồi bộ nhớ]`). Giải quyết triệt để vấn đề mất ngữ cảnh khi tìm kiếm vector.

---

### GIAI ĐOẠN 2: VECTOR EMBEDDING, CHROMADB INGESTION & KIỂM ĐỊNH BENCHMARK 100% HIT@3 (NGÀY 05 – NGÀY 07)
*Mục tiêu: Đưa tri thức vào không gian vector và đo kiểm toán học chất lượng tìm kiếm trước khi tích hợp vào AI.*
* **1. Embedding Dual-Space trên Kaggle GPU & Ingestion ChromaDB (Ngày 05):**
  * Thử nghiệm và đánh giá các mô hình embedding mã nguồn mở và thương mại.
  * Chuyển hóa toàn bộ giáo trình thành **1.221 chunks tri thức chuẩn hóa** và lưu trữ vào Vector Database **ChromaDB**.
  * Thiết lập hệ thống metadata đa chiều: `language`, `course`, `chapter`, `source_file`, `doc_type` phục vụ lọc kiến thức chính xác.
* **2. Xây dựng Bộ Kiểm định Retrieval (Ground Truth Benchmark) (Ngày 06):**
  * Thiết kế bộ 36 câu hỏi kiểm định thực tế và câu hỏi "bẫy" bao phủ toàn bộ các chủ đề lập trình.
  * Xây dựng ma trận Ground Truth đối soát khắt khe từng câu hỏi với đúng ID chunk trong cơ sở dữ liệu.
  * Tinh chỉnh thuật toán truy vấn, đạt chỉ số hoàn hảo: **100% Hit@3** (tri thức cần tìm luôn nằm trong top 3 kết quả) và **MRR (Mean Reciprocal Rank) = 0.94**.
* **3. Đóng gói RAGService, Query Expansion & Bộ Unit Test tự động (Ngày 07):**
  * Đóng gói dịch vụ `RAGService` độc lập với tính năng tự động phát hiện ngôn ngữ lập trình (Auto-detect Language) và tự động mở rộng truy vấn (Query Expansion).
  * Viết bộ kiểm thử tự động xác minh toàn bộ hàm tìm kiếm vector chạy ổn định trong < 0.2s.

---

### GIAI ĐOẠN 3: PHÁT TRIỂN PIPELINE ĐA PHƯƠNG THỨC & THUẬT TOÁN CHỐNG PHA LOÃNG TRUY VẤN (NGÀY 08 – NGÀY 10)
*Mục tiêu: Cho phép hệ thống tiếp nhận cùng lúc Text + File Code + Ảnh Terminal mà không bị nhiễu ngữ cảnh.*
* **1. Xây dựng File Extractor Engine an toàn (Ngày 08):**
  * Xây dựng module tiếp nhận và bóc tách nội dung mã nguồn đa ngôn ngữ (`.py`, `.cpp`, `.sql`, `.java`, `.cs`).
  * Tích hợp cơ chế phòng thủ bảo mật nghiêm ngặt: chặn tấn công Path Traversal, chặn tệp nhị phân giả mạo mã nguồn, giới hạn dung lượng và kiểm tra bảng mã ký tự.
* **2. Xây dựng Image Extractor Engine & Vision OCR Terminal (Ngày 09):**
  * Module tiền xử lý ảnh: chuẩn hóa kích thước, tăng cường độ tương phản và lọc nhiễu cho ảnh chụp màn hình máy tính/điện thoại.
  * Sử dụng mô hình Vision AI chuyên dụng để bóc tách chính xác font chữ Monospace, trích xuất nguyên vẹn khối mã nguồn và các dòng Callstack lỗi trong Terminal.
* **3. Đột phá nghiên cứu - Query Synthesizer (Chống pha loãng truy vấn) (Ngày 10):**
  * *Vấn đề kỹ thuật:* Khi sinh viên vừa gửi câu hỏi, vừa gửi code dài, vừa gửi ảnh Terminal, vector search bị nhiễu bởi các đường dẫn file và log rác.
  * *Giải pháp của nhóm:* Thiết kế thuật toán Query Synthesizer bóc tách trọng tâm: chỉ lấy **Tên ngoại lệ (Exception Name: `IndexError`, `NullPointerException`, `Segmentation Fault`)**, **Mã lỗi** và **Hàm logic bị sai** từ file code để tổng hợp thành một truy vấn kỹ thuật tinh gọn. Nhờ đó, RAG tìm trúng 100% bài học giáo trình liên quan mà không bị pha loãng.

---

### GIAI ĐOẠN 4: THIẾT KẾ TRỢ GIẢNG SƯ PHẠM SOCRATIC, CONTAINER HÓA & KIỂM THỬ TOÀN DIỆN (NGÀY 11 – NGÀY 14)
*Mục tiêu: Định hình phương pháp sư phạm cho AI, kiểm thử toàn diện 30 kịch bản thực tế và đóng gói triển khai On-Premise.*
* **1. Prompt Engineering Sư phạm (Socratic Tutoring System) (Ngày 11):**
  * Thiết kế bộ System Prompt chuẩn mực sư phạm: Cấm viết code sửa sẵn, bắt buộc phân tích nguyên nhân gốc rễ, đặt câu hỏi gợi mở để người học tự tư duy, và bắt buộc gắn thẻ trích dẫn giáo trình (Tên sách, Chương, Mục).
* **2. Nâng cấp Mô hình Gemini 3 Flash & Cơ chế Tự phục hồi Đa tầng (Ngày 12):**
  * Tích hợp mô hình thế hệ mới **Gemini 3 Flash** với độ trễ phản hồi cực thấp (< 2s) và khả năng suy luận logic xuất sắc.
  * Xây dựng cơ chế tự phục hồi đa tầng (Multi-model Fallback: Gemini 3 Flash $\rightarrow$ Gemini 2.5 Flash $\rightarrow$ Gemini 1.5 Flash), đảm bảo hệ thống duy trì hoạt động 24/7 ngay cả khi một model gặp sự cố quota.
* **3. Kiểm thử Tích hợp Toàn diện 30 Kịch bản Thực tế (Ngày 13):**
  * Xây dựng và thực thi bộ kiểm thử E2E qua FastAPI TestClient bao phủ 30 tình huống thực tế của sinh viên:
    * 10 kịch bản câu hỏi lý thuyết, độ phức tạp thuật toán và cú pháp.
    * 10 kịch bản nộp tệp mã nguồn (.py, .cpp, .sql) chứa lỗi logic, rò rỉ bộ nhớ, đệ quy vô hạn.
    * 10 kịch bản gửi ảnh chụp màn hình Terminal OCR chứa đủ loại lỗi ngoại lệ.
  * **Kết quả:** Vượt qua **30/30 kịch bản thực tế (100% Pass)**.
* **4. Đóng gói Docker Compose, Hướng dẫn 1-Click & Hoàn thiện Báo cáo (Ngày 14):**
  * Chuẩn hóa `docker-compose.yml` tích hợp trọn gói Backend, ChromaDB volume và cấu hình môi trường, sẵn sàng triển khai On-Premise tại máy chủ trường.
  * Biên soạn tài liệu khởi chạy nhanh `QUICKSTART_RAG_TUTOR.md` với tập lệnh 1-click `start_dev.bat` và hoàn thiện Báo cáo Kỹ thuật toàn diện 14 ngày.

---

# PHẦN 5: CÔNG NGHỆ ĐƯỢC SỬ DỤNG CÓ HỢP LÝ KHÔNG? (BIỆN LUẬN CÔNG NGHỆ & TRADE-OFFS CHI TIẾT)

Mọi công nghệ nhóm lựa chọn trong kiến trúc hệ thống đều được cân nhắc kỹ lưỡng dựa trên 3 tiêu chí: **Độ chính xác học thuật**, **Hiệu năng chịu tải cho sinh viên**, và **Tính khả thi về mặt chi phí trong trường học**.

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 MA TRẬN BIỆN LUẬN CÔNG NGHỆ CỦA DỰ ÁN                                  │
├──────────────────────┬─────────────────────────────┬───────────────────────────┬───────────────────────┤
│ THÀNH PHẦN KIẾN TRÚC │ CÔNG NGHỆ ĐƯỢC CHỌN         │ CÔNG NGHỆ THAY THẾ BỊ LOẠI│ LÝ DO LOẠI BỎ & ĐÁNH ĐỔI │
├──────────────────────┼─────────────────────────────┼───────────────────────────┼───────────────────────┤
│ 1. PDF Layout Parser │ MinerU (Vision Layout-LM)   │ PyPDF, PDFPlumber         │ PyPDF làm vỡ code & toán│
│ 2. Vector Database   │ ChromaDB (Local In-process) │ Pinecone, Milvus Cluster  │ Pinecone đắt, Milvus nặng│
│ 3. LLM & Vision OCR  │ Gemini 3 Flash (+ Fallback) │ GPT-4o, Llama-3 Local     │ GPT-4o đắt, Llama cần GPU│
│ 4. Backend Engine    │ FastAPI (Asynchronous I/O)  │ Flask, Django Sync        │ Flask nghẽn khi chịu tải│
│ 5. Đóng gói & Deploy │ Docker Compose On-Premise   │ Cloud SaaS công cộng      │ Cloud lộ đề thi nội bộ  │
└──────────────────────┴─────────────────────────────┴───────────────────────────┴───────────────────────┘
```

### 1. Tại sao chọn MinerU (Layout-LM) thay vì PyPDF hay PDFPlumber?
* **Thực nghiệm thất bại với công nghệ cũ:** Các thư viện truyền thống như `PyPDF`, `PDFPlumber`, `pypdf2` chỉ quét ký tự thô theo tọa độ x-y. Khi gặp giáo trình lập trình:
  * Chúng làm gãy các dòng code thụt lề (indentation) - thứ sống còn của Python.
  * Chúng làm biến dạng các bảng biểu phân tích độ phức tạp thuật toán và công thức toán học LaTeX.
* **Ưu thế của MinerU:** MinerU sử dụng mô hình thị giác Layout-LM chuyên dụng bóc tách bố cục trang:
  * Nhận diện chính xác 100% ranh giới khối mã nguồn (code block), bảo toàn toàn bộ ký tự trắng và dấu thụt lề.
  * Tự động chuyển đổi công thức toán phức tạp sang cú pháp LaTeX chuẩn và giữ nguyên vẹn cấu trúc bảng biểu sang định dạng Markdown.

### 2. Tại sao chọn ChromaDB thay vì Pinecone hay Milvus?
* **Nhược điểm của Pinecone:** Là dịch vụ đám mây độc quyền đóng kín, tính phí theo tháng rất đắt đỏ, đòi hỏi gửi toàn bộ dữ liệu ra server nước ngoài (vi phạm bảo mật dữ liệu của trường), độ trễ mạng Internet cao.
* **Nhược điểm của Milvus / ElasticSearch:** Quá cồng kềnh, tiêu tốn tối thiểu 8GB - 16GB RAM chỉ để duy trì cụm cluster, cấu hình phức tạp, không phù hợp để đóng gói gọn nhẹ cho nhà trường tự host.
* **Ưu thế vượt trội của ChromaDB:**
  * Mã nguồn mở hoàn toàn, nhúng trực tiếp (in-memory/embedded sqlite) hoặc chạy container siêu nhẹ (< 300MB RAM).
  * Tốc độ truy xuất cực nhanh: **< 0.2 giây** cho tập 1.221 chunks tri thức.
  * Hỗ trợ Metadata Filtering linh hoạt (lọc theo môn, theo chương, theo ngôn ngữ), hoàn toàn miễn phí và không phụ thuộc bất kỳ bên thứ ba nào.

### 3. Tại sao chọn Gemini 3 Flash kết hợp Fallback đa tầng thay vì GPT-4o hay Llama 3 Local?
* **Nhược điểm của GPT-4o / Claude 3.5 Sonnet:** Chi phí token quá cao. Một trường đại học với 2.000 sinh viên sử dụng hàng ngày sẽ tiêu tốn hàng nghìn USD tiền API mỗi tháng - một rào cản tài chính bất khả thi.
* **Nhược điểm của Llama 3 chạy Local:** Đòi hỏi nhà trường phải đầu tư máy chủ trang bị dàn GPU khủng (Nvidia A100/H100 với VRAM 48GB-80GB, giá hàng trăm triệu đồng). Hơn nữa, khả năng đọc ảnh màn hình Terminal OCR của các mô hình Vision open-source cỡ nhỏ còn rất kém và chậm.
* **Ưu thế của Gemini 3 Flash:**
  * **Tốc độ siêu nhanh:** Thời gian suy luận dưới 2 giây, hỗ trợ cơ chế phản hồi theo luồng (Streaming).
  * **Xử lý Vision OCR bản địa xuất sắc:** Nhận diện cực nét font chữ đơn cách (Monospace) trên ảnh chụp Terminal mờ hoặc ảnh chụp điện thoại.
  * **Cửa sổ ngữ cảnh khổng lồ:** Lên tới 1 triệu tokens, cho phép nạp thoải mái cả file code lớn cùng nhiều chunks giáo trình mà không bị tràn bộ nhớ.
  * **Chi phí cực thấp:** Tiết kiệm hơn 90% so với GPT-4o.
* **Cơ chế tự phục hồi đa tầng (Multi-model Fallback Architecture):** Để giải quyết triệt để nỗi lo lỗi quota API, nhóm thiết kế kiến trúc tự động chuyển mạch:
  $$\text{Gemini 3 Flash (Ưu tiên số 1)} \xrightarrow{\text{lỗi quota}} \text{Gemini 2.5 Flash} \xrightarrow{\text{lỗi}} \text{Gemini 1.5 Flash}$$
  Nhờ đó, hệ thống đảm bảo duy trì độ sẵn sàng 99.9% cho sinh viên 24/7.

### 4. Tại sao chọn FastAPI (Asyncio) + Redis thay vì Flask hay Django?
* **Hạn chế của Flask/Django:** Hoạt động theo cơ chế đồng bộ (Synchronous I/O). Khi nhiều sinh viên cùng lúc tải ảnh Terminal lên để AI xử lý Vision OCR (mất khoảng 1-2 giây), toàn bộ luồng xử lý bị nghẽn (blocking), khiến các sinh viên khác phải chờ đợi rất lâu.
* **Ưu thế của FastAPI:** Xây dựng trên nền tảng Starlette và Pydantic với cơ chế bất đồng bộ (Asynchronous `async/await`), cho phép một tiến trình xử lý hàng nghìn kết nối đồng thời mà không bị nghẽn I/O.
* **Tích hợp Redis Caching:** Lưu trữ đệm các câu hỏi lý thuyết phổ biến, giúp trả kết quả tức thì (< 0.05 giây) mà không cần gọi lại LLM.

### 5. Tại sao chọn Docker Compose On-Premise?
* Cho phép toàn bộ hệ sinh thái (FastAPI Backend, ChromaDB, Redis, Frontend) được dựng lên chỉ bằng **1 lệnh duy nhất** (`docker compose up -d`).
* **Bảo toàn dữ liệu nội bộ:** Ngân hàng đề thi, tài liệu giáo trình và thông tin học tập của sinh viên được lưu trữ 100% trong máy chủ của trường, không có bất kỳ dữ liệu nhạy cảm nào bị rò rỉ ra ngoài Internet.

---

# PHẦN 6: SẢN PHẨM THỰC TẾ HOẠT ĐỘNG RA SAO? (LUỒNG VẬN HÀNH & KỊCH BẢN THỰC TẾ)

### 1. Luồng vận hành End-to-End 5 bước của hệ thống:

```
[Sinh viên gửi: Câu hỏi + File Code (.cpp/.py) + Ảnh Terminal lỗi]
                           │
                           ▼
[BƯỚC 1: Pipeline Đa phương thức: File Extractor + Vision OCR Terminal]
                           │
                           ▼
[BƯỚC 2: Query Synthesizer: Trích xuất Exception Name + Hàm lỗi -> Tạo truy vấn tinh gọn]
                           │
                           ▼
[BƯỚC 3: ChromaDB Retrieval: Truy xuất Top-3 chunks giáo trình chính xác theo môn/ngôn ngữ]
                           │
                           ▼
[BƯỚC 4: Gemini 3 Flash Socratic Engine: Kết hợp Ngữ cảnh RAG + System Prompt Sư phạm]
                           │
                           ▼
[BƯỚC 5: Trả về giao diện: Gợi ý tư duy từng bước + Thẻ trích dẫn Giáo trình/Chương/Mục]
```

### 2. Ba kịch bản thực tế vận hành chuẩn mực (Đã kiểm thử E2E 100% Pass):

#### Kịch bản 1: Câu hỏi lý thuyết & phân tích độ phức tạp thuật toán (Text Only)
* **Đầu vào sinh viên:** Nhập câu hỏi: *"Tại sao thuật toán QuickSort có trường hợp xấu nhất là O(n^2) và người ta khắc phục điều đó như thế nào?"*
* **Xử lý hệ thống:** RAG truy xuất chính xác chunk tri thức trong Giáo trình Cấu trúc dữ liệu & Giải thuật về giải thuật phân hoạch Lomuto/Hoare.
* **Phản hồi của AI:** AI giải thích hiện tượng chọn Pivot lệch khi mảng đã sắp xếp sẵn, và gợi ý người học tìm hiểu kỹ thuật chọn chốt trung vị của 3 phần tử (Median-of-Three). Kèm thẻ trích dẫn giáo trình rõ ràng.

#### Kịch bản 2: Bắt lỗi rò rỉ bộ nhớ con trỏ C++ (Source Code Attachment)
* **Đầu vào sinh viên:** Tải lên tệp `leak.cpp` chứa đoạn mã cấp phát động `new int[100]` nhưng kết thúc hàm không gọi `delete[]`.
* **Xử lý hệ thống:** File Extractor bóc tách AST, phát hiện hàm `processData()` có lệnh cấp phát `new` nhưng thiếu `delete[]`.
* **Phản hồi của AI (Chuẩn Socratic):** AI **không sửa code hộ**, mà hỏi gợi mở:
  > *"Bạn hãy quan sát dòng 5 nơi mảng động `int* arr` được cấp phát trên vùng nhớ Heap. Khi hàm `processData()` kết thúc, vùng nhớ này đã được thu hồi chưa? Nếu chương trình chạy lặp lại 1.000 lần thì điều gì sẽ xảy ra với bộ nhớ RAM?"*
  Kèm thẻ trích dẫn: `[Giáo trình C++ | Chương 4: Con trỏ và Quản lý bộ nhớ]`.

#### Kịch bản 3: Xử lý ảnh chụp màn hình Terminal OCR lỗi `IndexError` (Vision OCR)
* **Đầu vào sinh viên:** Chụp ảnh màn hình Terminal báo lỗi: `IndexError: list index out of range` ở dòng 14 trong vòng lặp `for i in range(len(arr) + 1)`.
* **Xử lý hệ thống:**
  * Vision OCR đọc chính xác stack trace từ ảnh.
  * Query Synthesizer trích xuất Exception `IndexError` và điều kiện biên `len(arr) + 1`.
* **Phản hồi của AI:** AI giải thích: *"Trong Python, chỉ số mảng bắt đầu từ 0 đến len(arr) - 1. Khi bạn duyệt tới len(arr) + 1 thì điều gì sẽ xảy ra ở phần tử cuối cùng?"* $\rightarrow$ Hướng dẫn sinh viên tự sửa `range(len(arr))`.

---

# PHẦN 7: KẾT QUẢ ĐẠT ĐƯỢC CÓ ĐƯỢC KIỂM CHỨNG KHÔNG? (ĐỐI SOÁT ĐỊNH LƯỢNG & METRICS)

Toàn bộ kết quả của dự án đều được đo lường minh bạch bằng các **chỉ số toán học định lượng** và **bộ kiểm thử tự động hóa**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              BẢNG TỔNG HỢP KIỂM CHỨNG HỆ THỐNG                         │
├──────────────────────────────────┬──────────────────────┬──────────────────────────────┤
│ HẠNG MỤC ĐO LƯỜNG                │ KẾT QUẢ ĐẠT ĐƯỢC     │ Ý NGHĨA KỸ THUẬT             │
├──────────────────────────────────┼──────────────────────┼──────────────────────────────┤
│ 1. Kho tri thức chuẩn hóa        │ 1.221 Chunks tri thức│ Bóc tách SOTA bằng MinerU    │
│ 2. Tỷ lệ chính xác Retrieval     │ 100% Hit@3           │ Tài liệu đúng luôn nằm Top 3 │
│ 3. Chỉ số Mean Reciprocal Rank   │ MRR = 0.94 / 1.00    │ Đa số tài liệu nằm vị trí 1  │
│ 4. Unit Tests tự động            │ 33 / 33 PASSED (100%)│ Kiểm tra bảo mật & module    │
│ 5. End-to-End Scenarios Tests    │ 30 / 30 PASSED (100%)│ 10 Text + 10 Code + 10 OCR   │
│ 6. Thời gian tìm kiếm Vector     │ < 0.2 giây           │ Truy vấn ChromaDB siêu tốc   │
│ 7. Thời gian phản hồi toàn trình │ < 2.5 giây           │ Kèm cả OCR và LLM Streaming  │
└──────────────────────────────────┴──────────────────────┴──────────────────────────────┘
```

### 1. Bộ kiểm định Retrieval trên 36 câu hỏi Benchmark (Ground Truth đối soát)
* Nhóm xây dựng ma trận kiểm định gồm **36 câu hỏi thực tế và câu hỏi "bẫy"** bao phủ toàn bộ giáo trình.
* Mỗi câu hỏi được gán cứng Ground Truth (ID chunk chuẩn cần tìm).
* **Kết quả thực nghiệm:** Đạt **100% Hit@3** (100% câu hỏi đều tìm thấy tài liệu chuẩn trong 3 kết quả đầu tiên) và **MRR = 0.94**, chứng minh kho tri thức RAG hoạt động chính xác tuyệt đối.

### 2. Bộ kiểm thử tự động hóa 63 bài test Pytest (Automated Test Suite)
* **33 Unit Tests:** Kiểm tra tính năng bóc tách file an toàn, phòng chống Path Traversal, kiểm tra giới hạn dung lượng ảnh, kiểm tra thuật toán Query Synthesizer và RAGService.
* **30 End-to-End Scenarios Tests:** Mô phỏng 30 tình huống thực tế sinh viên gửi yêu cầu qua FastAPI TestClient:
  * 10 kịch bản câu hỏi lý thuyết, độ phức tạp thuật toán và cú pháp.
  * 10 kịch bản nộp tệp mã nguồn (.py, .cpp, .sql) chứa lỗi logic, rò rỉ bộ nhớ, đệ quy vô hạn.
  * 10 kịch bản gửi ảnh chụp màn hình Terminal OCR chứa đủ loại lỗi ngoại lệ.
* **Toàn bộ 63/63 tests đều vượt qua thành công (100% Pass).**

### 3. Đánh giá tính chuẩn mực Sư phạm (Pedagogical Compliance)
* 100% các câu trả lời sinh ra đều tuân thủ nghiêm ngặt nguyên tắc Socratic: **Không bao giờ viết code sửa sẵn**, luôn đặt câu hỏi gợi mở tư duy và **luôn hiển thị thẻ trích dẫn giáo trình chính thống**.

---

# PHẦN 8: DỰ ÁN CÓ HẠN CHẾ GÌ VÀ HƯỚNG PHÁT TRIỂN RA SAO? (ĐÁNH GIÁ KHÁCH QUAN & LỘ TRÌNH)

### 1. Ba hạn chế thực tế hiện tại của hệ thống:
* **Hạn chế 1 (Chất lượng ảnh đầu vào chụp từ điện thoại):** Nếu sinh viên chụp ảnh màn hình bằng điện thoại ở góc quá nghiêng (méo hình học 3D), bị lóa sáng đèn trần hoặc rung tay mờ nét, độ chính xác nhận diện ký tự OCR có thể giảm, đòi hỏi sinh viên phải nhập thêm text bổ trợ.
* **Hạn chế 2 (Phạm vi môn học):** Hiện tại hệ thống mới tập trung xây dựng kho tri thức cho 4 môn nền tảng (C++, Python, CTDL&GT, CSDL), chưa bao phủ toàn bộ các môn chuyên ngành năm 3-4 (Mạng máy tính, Hệ điều hành, Trí tuệ nhân tạo).
* **Hạn chế 3 (Môi trường thực thi code trực tiếp):** Chưa tích hợp trình biên dịch sandbox chạy code trực tiếp trên web (Code Runner / Online Judge) để sinh viên bấm nút test code ngay tại chỗ sau khi được AI gợi ý.

### 2. Hướng phát triển trong tương lai (Lộ trình mở rộng):
* **Ngắn hạn (3 – 6 tháng tới):**
  * **Tích hợp WebAssembly / Docker Sandbox:** Cho phép sinh viên bấm nút "Chạy thử code" an toàn ngay trong khung chat để đối soát kết quả theo thời gian thực mà không sợ mã độc phá hoại máy chủ.
  * **Hoàn thiện Giao diện Web Dashboard cho Giảng viên:** Cung cấp biểu đồ nhiệt trực quan (Error Heatmap) hiển thị tỷ lệ lỗi của cả lớp theo tuần, kèm công cụ 1-click để thầy cô khóa/mở tài liệu theo tiến độ giảng dạy.
* **Dài hạn (6 – 12 tháng tới):**
  * **Mở rộng kho tri thức toàn bộ khóa học:** Nạp toàn bộ giáo trình các môn chuyên ngành của Khoa CNTT.
  * **Tính năng Auto-Ingestion:** Cho phép Giảng viên chỉ cần kéo thả Slide bài giảng PPTX hoặc PDF mới lên là hệ thống tự động bóc tách MinerU và cập nhật vào ChromaDB trong vòng 3 phút.
  * **Tích hợp sâu vào hệ thống LMS:** Kết nối API đồng bộ dữ liệu với Moodle, Canvas hoặc Blackboard của nhà trường.

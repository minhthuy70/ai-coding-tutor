# ĐỀ CƯƠNG THUYẾT TRÌNH SLIDE PPT & KỊCH BẢN VẤN ĐÁP TRƯỚC HỘI ĐỒNG
## HỆ THỐNG TRỢ GIẢNG LẬP TRÌNH THÔNG MINH ĐA PHƯƠNG THỨC (AI-POWERED CODING TUTOR & MULTIMODAL RAG)

> **Tài liệu phục vụ:** Soạn thảo slide thuyết trình (PowerPoint/Canva) và luyện tập trả lời vấn đáp bảo vệ Đồ án / Khóa luận tốt nghiệp.  
> **Repository dự án:** [ai-coding-tutor](https://github.com/minhthuy70/ai-coding-tutor)  
> **Tài liệu kỹ thuật liên quan:**
> - [NHAT_KY_TRIEN_KHAI_CHI_TIET_NGAY_1_DEN_14.md](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/NHAT_KY_TRIEN_KHAI_CHI_TIET_NGAY_1_DEN_14.md)
> - [QUICKSTART_RAG_TUTOR.md](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/QUICKSTART_RAG_TUTOR.md)
> - [LOTRINH_14_NGAY_RAG_MULTIMODAL_TUTOR.md](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/LOTRINH_14_NGAY_RAG_MULTIMODAL_TUTOR.md)

---

## CẤU TRÚC BỘ SLIDE THUYẾT TRÌNH PPT GỢI Ý (10 - 12 SLIDES)

```
SLIDE 01: Trang bìa & Giới thiệu đề tài
SLIDE 02: Bối cảnh & Thực trạng (Nỗi đau của Sinh viên & Giảng viên)
SLIDE 03: Hệ thống này dùng để làm gì? (Mục đích & Ứng dụng thực tế)
SLIDE 04: Vì sao ChatGPT / Copilot thất bại trong môi trường Đại học?
SLIDE 05: 5 Đột phá khác biệt mà các AI khác chưa làm được (Core Values)
SLIDE 06: Bảng so sánh đối đầu toàn diện (ChatGPT vs. Copilot vs. Hệ thống AI Tutor)
SLIDE 07: Kiến trúc hệ thống tổng thể (SOTA Multimodal RAG Pipeline)
SLIDE 08: Kết quả thực nghiệm & Kiểm định chất lượng (100% Hit@3 Benchmark)
SLIDE 09: Kịch bản Live Demo hệ thống (Text, Source Code, Terminal OCR)
SLIDE 10: Tổng kết, Giá trị đóng góp & Hướng phát triển
PHỤ LỤC : Bộ câu hỏi vấn đáp hiểm hóc của Hội đồng & Kịch bản phản biện
```

---

## CHI TIẾT TỪNG SLIDE: NỘI DUNG HIỂN THỊ & LỜI THOẠI THUYẾT TRÌNH

---

### SLIDE 01: TRANG BÌA & GIỚI THIỆU ĐỀ TÀI

* **🎯 Gợi ý bố cục Slide:** Logo Trường/Khoa, Tên đề tài in đậm nổi bật, Họ tên sinh viên, Giảng viên hướng dẫn, Khung mô tả công nghệ cốt lõi: *Gemini 3 Flash • Multimodal RAG • Socratic Method • ChromaDB*.
* **📝 Nội dung hiển thị:**
  * **Đề tài:** Nghiên cứu và Xây dựng Hệ thống Trợ giảng Lập trình Thông minh Đa phương thức hỗ trợ sinh viên học tập theo chuẩn Sư phạm Socratic.
  * **Từ khóa công nghệ:** Multimodal RAG, Query Synthesizer, AST Chunking, Vision OCR, Socratic Tutoring.
* **🎙️ Lời thoại thuyết trình (Speaker Notes - 30 giây):**
  > *"Kính thưa quý Thầy/Cô trong Hội đồng, em xin phép được trình bày đề tài: 'Hệ thống Trợ giảng Lập trình Thông minh Đa phương thức'. Đề tài tập trung giải quyết bài toán hỗ trợ sinh viên tự học lập trình hiệu quả 24/7 và cung cấp công cụ quản lý chất lượng đào tạo chuyên sâu cho giảng viên khoa Công nghệ Thông tin."*

---

### SLIDE 02: BỐI CẢNH & THỰC TRẠNG (VÌ SAO ĐỀ TÀI RA ĐỜI?)

* **🎯 Gợi ý bố cục Slide:** Chia 2 cột trực quan:
  * Cột 1: Khó khăn của Sinh viên khi tự học code ở nhà.
  * Cột 2: Bế tắc của Giảng viên khi sinh viên lạm dụng AI.
* **📝 Nội dung hiển thị:**
  * **Sinh viên:**
    * Kẹt lỗi code lúc nửa đêm (Memory Leak, Segmentation Fault, Stack Trace dài) không có ai trợ giúp.
    * Đọc tài liệu tiếng Anh khó hiểu, không biết tra cứu phần nào trong giáo trình.
  * **Giảng viên & Nhà trường:**
    * Sinh viên lạm dụng ChatGPT để copy code hoàn chỉnh nộp bài $\rightarrow$ Mất tư duy lập trình căn bản.
    * Giảng viên không có công cụ giám sát: Không biết lớp học đang yếu ở thuật toán nào để điều chỉnh giáo án.
* **🎙️ Lời thoại thuyết trình (45 giây):**
  > *"Thưa Thầy/Cô, khi sinh viên CNTT tự làm bài tập ở nhà, các bạn thường gặp các lỗi khó hiểu lúc nửa đêm. Nếu hỏi ChatGPT, các bạn nhận ngay một đoạn code giải sẵn đút tận miệng. Điều này dẫn tới hệ quả sinh viên nộp bài thì điểm cao nhưng đi thi viết giấy lại rớt vì không hiểu bản chất. Giảng viên thì hoàn toàn mù tịt về lỗ hổng kiến thức thực sự của lớp học. Đó chính là lý do thôi thúc em xây dựng hệ thống này."*

---

### SLIDE 03: HỆ THỐNG NÀY DÙNG ĐỂ LÀM GÌ? (ỨNG DỤNG THỰC TẾ)

* **🎯 Gợi ý bố cục Slide:** Vẽ sơ đồ tương tác 2 chiều: Sinh viên $\leftrightarrow$ Hệ thống AI $\leftrightarrow$ Giảng viên.
* **📝 Nội dung hiển thị:**
  * **Đối với Sinh viên (Trợ giảng số 24/7):**
    * Tiếp nhận đầu vào đa phương thức: Câu hỏi văn bản, Tệp mã nguồn (`.py`, `.cpp`, `.sql`), hoặc Ảnh chụp màn hình Terminal lỗi.
    * Đối soát trực tiếp với giáo trình chuẩn của trường.
    * Phân tích nguyên nhân và hướng dẫn sinh viên tự sửa lỗi (debugging).
  * **Đối với Giảng viên (Hệ thống Quản lý Đào tạo Thông minh):**
    * Cung cấp **Bản đồ nhiệt lỗ hổng kiến thức (Classroom Error Heatmap)** theo thời gian thực.
    * Kiểm soát phạm vi tài liệu tra cứu theo từng tuần học (Curriculum Scoping).
    * Bảo mật đề thi nội bộ trên máy chủ riêng (Docker On-Premise).
* **🎙️ Lời thoại thuyết trình (45 giây):**
  > *"Vậy hệ thống này dùng để làm gì? Xin thưa Thầy/Cô, đây là một 'Hệ sinh thái Trợ giảng số và Quản trị Đào tạo':  
  > Với sinh viên, hệ thống là một trợ giảng 24/7 đọc được cả file code lẫn ảnh chụp lỗi màn hình để chỉ điểm sai và gợi ý cách sửa.  
  > Với giảng viên, hệ thống là một chiếc rada soi sáng toàn bộ điểm nghẽn kiến thức của cả lớp học, giúp thầy cô can thiệp và nâng cao chất lượng dạy học kịp thời."*

---

### SLIDE 04: VÌ SAO CHATGPT & GITHUB COPILOT THẤT BẠI TRONG GIÁO DỤC ĐẠI HỌC?

* **🎯 Gợi ý bố cục Slide:** 3 icon cảnh báo lớn thể hiện 3 "nỗi đau":
  1. ❌ *Spoon-feeding* (Mớm bài/Viết hộ)
  2. ❌ *Hallucination & Misalignment* (Ảo giác & Lệch chuẩn)
  3. ❌ *Black Box* (Hộp đen đối với Nhà trường)
* **📝 Nội dung hiển thị:**
  * **Vấn đề 1: 'Kẻ phá hoại việc học' (Mớm code có sẵn):** ChatGPT sinh sẵn 100% code $\rightarrow$ Triệt tiêu khả năng tư duy giải thuật và kỹ năng tự debug của sinh viên.
  * **Vấn đề 2: Ảo giác & Lệch chuẩn barem môn học:** ChatGPT học từ Internet tự do, dùng thư viện ngoài hoặc chuẩn C++20 hiện đại (`std::unique_ptr`) trong khi môn học yêu cầu con trỏ thô $\rightarrow$ Sinh viên bị chấm 0 điểm vì phạm quy chế thi.
  * **Vấn đề 3: Hộp đen cá nhân:** Giảng viên không có quyền kiểm soát phạm vi bài học và không thu được bất kỳ dữ liệu học tập nào của sinh viên.
* **🎙️ Lời thoại thuyết trình (45 giây):**
  > *"Nhiều người nghĩ chỉ cần dùng ChatGPT là đủ. Nhưng thực tế trong môi trường học thuật, ChatGPT thất bại vì nó là 'kẻ mớm bài', sinh viên chỉ việc copy-paste mà không học được gì. Hơn nữa, ChatGPT rất hay bị 'ảo giác' dùng các cú pháp nâng cao bị cấm trong giáo trình thi. Cuối cùng, ChatGPT là một 'hộp đen'—thầy cô không hề biết sinh viên học được gì từ nó."*

---

### SLIDE 05: 5 ĐỘT PHÁ KHÁC BIỆT MÀ CÁC AI KHÁC CHƯA LÀM ĐƯỢC

* **🎯 Gợi ý bố cục Slide:** Thiết kế dạng 5 thẻ (Cards) hiện đại, có icon nổi bật:
* **📝 Nội dung hiển thị:**
  * **1. Phương pháp Sư phạm Socratic (Không đưa code hoàn chỉnh):**  
    Chỉ điểm dòng lỗi logic, giải thích bản chất và đặt câu hỏi định hướng để sinh viên **tự tay sửa code của chính mình**.
  * **2. RAG Giáo trình chính thống (Chống ảo giác 100%):**  
    Neo chặt vào kho **1.221 chunks tri thức giáo trình đại học chuẩn hóa** (MinerU SOTA Layout Parser). Trả về thẻ trích dẫn chính xác (Tên giáo trình, Chương, Trang).
  * **3. Query Synthesizer chống pha loãng ngữ cảnh:**  
    Tự động bóc tách mã lỗi từ Terminal Vision OCR (`IndexError`, `Memory Leak`) và hàm lỗi từ file code, cô đọng thành từ khóa truy vấn chuẩn xác.
  * **4. Bản đồ nhiệt lỗ hổng kiến thức (Classroom Error Heatmap):**  
    Báo cáo cho giảng viên: *"Tuần này 65% sinh viên mắc lỗi con trỏ ở bài 3"*, cảnh báo sinh viên có nguy cơ rớt môn.
  * **5. Khóa tài liệu theo tiến độ tuần & Bảo mật On-Premise:**  
    Giảng viên khóa phạm vi chỉ cho AI dùng tri thức Chương 1-3. Toàn bộ hệ thống chạy Docker nội bộ, bảo mật tuyệt đối ngân hàng đề thi của khoa.
* **🎙️ Lời thoại thuyết trình (1 phút):**
  > *"Để giải quyết triệt để các hạn chế trên, hệ thống của em mang lại 5 đột phá độc quyền:  
  > Thứ nhất là tính Sư phạm Socratic: cấm AI đưa code sẵn, bắt sinh viên tự tư duy.  
  > Thứ hai là kho tri thức RAG chính thống từ chính giáo trình của trường, nói có sách mách có chứng.  
  > Thứ ba là bộ Query Synthesizer lọc nhiễu ảnh terminal để tìm đúng bài học.  
  > Thứ tư là Dashboard phân tích lỗ hổng kiến thức giúp thầy cô biết cả lớp đang kẹt ở đâu.  
  > Và thứ năm là khả năng khóa tài liệu theo tuần cùng hạ tầng Docker nội bộ bảo vệ dữ liệu đề thi của trường."*

---

### SLIDE 06: BẢNG SO SÁNH ĐỐI ĐẦU TOÀN DIỆN

* **🎯 Gợi ý bố cục Slide:** Chiếu nguyên bảng so sánh để gây ấn tượng mạnh với Hội đồng:
* **📝 Nội dung hiển thị:**

| Tiêu chí so sánh | ChatGPT / Claude | GitHub Copilot | Custom GPT / NotebookLM | **Hệ thống AI Tutor của Đề tài** |
| :--- | :---: | :---: | :---: | :---: |
| **Mục đích thiết kế** | Trả lời đa năng | Sinh code đi làm | Tra cứu tài liệu | **Sư phạm & Quản lý Đào tạo** |
| **Cách xử lý lỗi code** | Viết code sửa đút tận miệng | Tự gõ hoàn thành code | Viết code sửa sẵn | **Gợi mở Socratic để SV tự sửa** |
| **Nguồn tri thức kiểm chứng** | Toàn bộ Internet (dễ bịa) | GitHub Repos | File nạp vào | **Giáo trình Đại học chuẩn hóa** |
| **Xử lý ảnh lỗi Terminal** | Dễ loãng ngữ cảnh | Không hỗ trợ | Không tối ưu Monospace | **Vision OCR + Query Synthesizer** |
| **Kiểm soát bài học theo tuần** | ❌ Không | ❌ Không | ❌ Không | **✅ Có (Metadata Filtering)** |
| **Báo cáo lỗi cho Giảng viên** | ❌ Không | ❌ Không | ❌ Không | **✅ Có (Error Heatmap Dashboard)** |
| **Bảo mật đề thi nội bộ** | Đám mây công cộng | Đám mây công cộng | Đám mây công cộng | **✅ Docker On-Premise tại trường** |

* **🎙️ Lời thoại thuyết trình (30 giây):**
  > *"Nhìn vào bảng so sánh này, quý Thầy/Cô có thể thấy rõ: Các giải pháp thương mại như ChatGPT, Copilot hay NotebookLM hoàn toàn thiếu vắng tính năng Sư phạm và khả năng Quản trị Đào tạo. Hệ thống của em là giải pháp duy nhất giải quyết trọn vẹn cả bài toán học tập của sinh viên lẫn bài toán giảng dạy của giảng viên."*

---

### SLIDE 07: KIẾN TRÚC HỆ THỐNG & MULTIMODAL RAG PIPELINE

* **🎯 Gợi ý bố cục Slide:** Sơ đồ kiến trúc 3 tầng chuẩn mực:
  * Tầng 1: Data Ingestion (MinerU PDF $\rightarrow$ Text Cleaning $\rightarrow$ AST Chunking $\rightarrow$ ChromaDB).
  * Tầng 2: Multimodal Processing (File Extractor + Vision OCR $\rightarrow$ Query Synthesizer $\rightarrow$ Vector Search).
  * Tầng 3: Socratic Inference (Gemini 3 Flash + Citation UI + Multi-model Fallback).
* **📝 Nội dung hiển thị:**
  * **Cơ sở dữ liệu Vector:** ChromaDB lưu trữ 1.221 chunks tri thức đa nguồn (C++, Python, DSA, CSDL).
  * **Mô hình AI:** Gemini 3 Flash với cơ chế tự phục hồi đa tầng (Fallback sang Gemini 2.5/1.5 khi quá tải).
  * **Đóng gói:** Docker Compose tích hợp PostgreSQL, Redis, FastAPI Backend, Next.js Frontend.
* **🎙️ Lời thoại thuyết trình (45 giây):**
  > *"Về mặt kiến trúc kỹ thuật, hệ thống sử dụng pipeline bóc tách bố cục SOTA MinerU bảo toàn 100% các khối code và bảng biểu từ giáo trình PDF, phân đoạn bằng kỹ thuật AST-aware chunking và lưu vào ChromaDB với 1.221 đoạn tri thức. Khi người dùng gửi yêu cầu, tầng xử lý đa phương thức sẽ bóc tách code và ảnh terminal, qua bộ tổng hợp truy vấn để tìm tri thức và đưa vào Gemini 3 Flash để sinh phản hồi sư phạm."*

---

### SLIDE 08: KẾT QUẢ THỰC NGHIỆM & KIỂM ĐỊNH CHẤT LƯỢNG

* **🎯 Gợi ý bố cục Slide:** 3 con số ấn tượng dạng Metric Cards:
  * 🟢 **100% Hit@3** (Bộ kiểm định Benchmark 36 câu hỏi RAG)
  * 🟢 **63/63 Tests PASSED** (33 Unit Tests + 30 End-to-End Scenarios)
  * 🟢 **< 2.0 giây** (Thời gian phản hồi trung bình)
* **📝 Nội dung hiển thị:**
  * **Độ chính xác truy xuất RAG:** Đạt **100% Hit@3** và **MRR = 0.94** trên bộ 36 câu hỏi kiểm định ground-truth đa nguồn (C++, Python, CSDL).
  * **Độ bao phủ kiểm thử:** Vượt qua **30 kịch bản thực tế** liên tục trong bộ test tự động Ngày 13:
    * 10/10 kịch bản câu hỏi Lý thuyết / Độ phức tạp thuật toán.
    * 10/10 kịch bản kèm Tệp mã nguồn lỗi (.cpp, .py, .sql).
    * 10/10 kịch bản kèm Ảnh chụp màn hình lỗi Terminal (Vision OCR).
* **🎙️ Lời thoại thuyết trình (45 giây):**
  > *"Để chứng minh tính ổn định và chính xác của hệ thống, nhóm em đã xây dựng bộ kiểm định tự động nghiêm ngặt: Đạt tỷ lệ truy xuất chính xác 100% Hit@3 trên bộ benchmark 36 câu hỏi thực tế, và vượt qua toàn bộ 63/63 bài kiểm thử unit test và end-to-end scenarios, đảm bảo hệ thống phản hồi cực nhanh dưới 2 giây và hoạt động bền bỉ."*

---

### SLIDE 09: KỊCH BẢN LIVE DEMO TRỰC TIẾP TRƯỚC HỘI ĐỒNG

* **🎯 Gợi ý bố cục Slide:** Chụp 3 ảnh màn hình giao diện ứng dụng thực tế ứng với 3 tình huống demo:
* **📝 Nội dung hiển thị:**
  * **Demo 1 (Lý thuyết):** Sinh viên hỏi *"Độ phức tạp xấu nhất của QuickSort là gì?"*  
    $\rightarrow$ AI giải thích $O(n^2)$, trích dẫn Giáo trình Cấu trúc dữ liệu và gợi mở giải pháp Median-of-Three.
  * **Demo 2 (Gửi file C++ lỗi):** Sinh viên nộp `solution.cpp` có lỗi `new int[100]` không `delete[]`.  
    $\rightarrow$ AI chỉ ra nguy cơ rò rỉ bộ nhớ (Memory Leak), trích dẫn Giáo trình C++, hướng dẫn sinh viên bổ sung toán tử giải phóng.
  * **Demo 3 (Tải ảnh chụp Terminal lỗi):** Tải ảnh chụp màn hình terminal lỗi `IndexError: list index out of range`.  
    $\rightarrow$ Vision OCR bóc tách stack trace, AI đối soát bài học Indexing của Python và đặt câu hỏi gợi ý sửa biên vòng lặp.
* **🎙️ Lời thoại thuyết trình (Chuyển sang phần thực nghiệm):**
  > *"Sau đây, em xin phép được thực hiện Live Demo trực tiếp 3 kịch bản thực tế trên hệ thống đang chạy để quý Thầy/Cô cùng kiểm chứng tính năng sư phạm và khả năng xử lý đa phương thức của phần mềm."*

---

### SLIDE 10: TỔNG KẾT & LỜI KẾT THUYẾT TRÌNH

* **🎯 Gợi ý bố cục Slide:** Tóm tắt 3 thông điệp cốt lõi & Lời cảm ơn Hội đồng.
* **📝 Nội dung hiển thị:**
  * **Giá trị thực tiễn:** Tạo ra người bạn đồng hành 24/7 cho sinh viên tự học lập trình đúng chuẩn.
  * **Giá trị sư phạm:** Giữ vững phương pháp gợi mở Socratic, chống gian lận và chống học vẹt.
  * **Giá trị quản lý:** Cung cấp dữ liệu thực tế giúp nhà trường nâng cao chất lượng đào tạo.
* **🎙️ Lời thoại thuyết trình (30 giây kết thúc):**
  > *"Kính thưa Hội đồng, hệ thống của em không chỉ dừng lại ở một công cụ công nghệ, mà là một giải pháp chuyển đổi số giáo dục toàn diện—vừa giúp sinh viên phát triển tư duy lập trình độc lập, vừa trao quyền cho giảng viên quản lý chất lượng đào tạo một cách khoa học.  
  > Em xin chân thành cảm ơn quý Thầy/Cô đã chú ý lắng nghe và em rất mong nhận được những câu hỏi đóng góp quý báu từ Hội đồng ạ!"*

---

## PHỤ LỤC: BỘ CÂU HỎI VẤN ĐÁP HIỂM HÓC & KỊCH BẢN PHẢN BIỆN

### ❓ Câu 1: "Thầy thấy chỉ cần tạo 1 con Custom GPT trên ChatGPT rồi tải giáo trình lên cho sinh viên hỏi là xong, sao phải viết cả hệ thống này làm gì cho tốn công?"
> **💡 Kịch bản trả lời đỉnh cao:**  
> *"Dạ thưa Thầy, câu hỏi của Thầy chạm đúng vào trăn trở lớn nhất của nhóm em khi làm đề tài:*  
> *Nếu chỉ là chat 1 chiều, đúng là dùng Custom GPT là xong. **Nhưng đối với Nhà trường và Giảng viên, Custom GPT là một 'hộp đen' thất bại** vì 3 lý do:*  
> *1. **Giảng viên không thấy được dữ liệu học tập:** Custom GPT là hộp đen cá nhân của sinh viên, Thầy cô không biết sinh viên đang yếu ở đâu để điều chỉnh giáo án. Hệ thống của em phân tích toàn bộ lỗi thực tế của lớp để vẽ ra **'Bản đồ lỗ hổng kiến thức'** cho Giảng viên.*  
> *2. **Không khóa được phạm vi bài học:** Custom GPT sẽ lôi kiến thức cuối kỳ ra giải bài đầu kỳ làm hỏng tư duy sinh viên. Hệ thống của em cho phép Giảng viên **giới hạn kho tài liệu theo từng tuần học**.*  
> *3. **Bảo mật đề thi:** Ngân hàng đề của Khoa không thể tải lên các nền tảng đám mây công cộng. Hệ thống của em chạy Docker nội bộ bảo vệ dữ liệu tuyệt đối của trường.*  
> *Vì vậy, đây là **Hệ sinh thái Quản lý Đào tạo Thông minh**, chứ không phải một con chatbot đơn lẻ ạ!"*

---

### ❓ Câu 2: "Tại sao không cho AI sửa code luôn cho nhanh, sinh viên đang cần sửa bài mà cứ hỏi vòng vo có làm sinh viên khó chịu không?"
> **💡 Kịch bản trả lời:**  
> *"Dạ thưa Thầy/Cô, mục tiêu cao nhất của giáo dục đại học là rèn luyện **Kỹ năng giải quyết vấn đề (Problem Solving) và Kỹ năng gỡ lỗi (Debugging)**.  
> Nếu AI sửa sẵn code, sinh viên sẽ hình thành thói quen 'ỷ lại', đi làm thực tế gặp lỗi mới không biết cách tra cứu. Phương pháp Socratic của hệ thống không hề hỏi vòng vo vô nghĩa, mà **chỉ điểm ngay dòng lỗi và giải thích bản chất**, chỉ giữ lại bước cuối cùng là bắt sinh viên tự gõ lại code của mình. Theo các nghiên cứu giáo dục hiện đại (EdTech), đây là cách duy nhất giúp sinh viên nhớ lâu và hiểu sâu kiến thức ạ."*

---

### ❓ Câu 3: "Dữ liệu giáo trình của em được đưa vào hệ thống thế nào và làm sao bảo đảm AI không trích dẫn sai?"
> **💡 Kịch bản trả lời:**  
> *"Dạ thưa Thầy/Cô, hệ thống không nạp file text thô mà sử dụng pipeline **MinerU Layout Parser** chuyên dụng để nhận diện chuẩn xác các khối code, công thức toán và bảng biểu từ PDF giáo trình.  
> Sau đó, hệ thống áp dụng kỹ thuật **AST-aware chunking** để không bao giờ cắt đôi một hàm code, và bổ sung ngữ cảnh chương mục theo phương pháp Contextual Retrieval của Anthropic. Nhờ đó, trong bộ kiểm định 36 câu hỏi khắt khe, hệ thống đạt **100% Hit@3**, nghĩa là tri thức liên quan luôn nằm trong top 3 kết quả và được đưa trực tiếp vào prompt để AI trích dẫn chính xác tên tài liệu và số trang ạ."*

---

### ❓ Câu 4: "Nếu sinh viên tải ảnh chụp màn hình mờ, chụp nghiêng bằng điện thoại thì hệ thống có đọc được không?"
> **💡 Kịch bản trả lời:**  
> *"Dạ, pipeline xử lý đa phương thức ở Ngày 10 của nhóm em có module tiền xử lý ảnh (`ImageExtractor`):  
> 1. Tự động chuẩn hóa kích thước và tăng cường độ tương phản văn bản.  
> 2. Sử dụng mô hình Vision chuyên dụng nhận diện font Monospace đặc thù của Terminal.  
> 3. Bộ lọc `QuerySynthesizer` có cơ chế khử nhiễu: nó loại bỏ các thông tin rác như đường dẫn thư mục `C:\Users\...` hay ngày giờ, mà chỉ bóc tách đúng tên ngoại lệ cốt lõi (`IndexError`, `Segmentation Fault`) và số dòng báo lỗi. Vì vậy, ngay cả khi ảnh có viền thừa hay nhiễu thì hệ thống vẫn truy vấn chính xác giáo trình ạ."*

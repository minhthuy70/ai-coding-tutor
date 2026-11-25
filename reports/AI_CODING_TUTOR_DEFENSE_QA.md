# AI Coding Tutor — Bộ câu hỏi phản biện bảo vệ

> Bản ôn tập này được xây dựng sau khi đối chiếu mã nguồn, test, dữ liệu và báo cáo trong repository.  
> **Quy ước:** “Đã xác minh” nghĩa là có dấu vết trong source/data; không đồng nghĩa đã được đánh giá chất lượng trong môi trường thực tế. Những mục chưa triển khai được ghi rõ, không trình bày như kết quả hoàn thành.

## Luận điểm bảo vệ trong 30 giây

> “Em không tạo mô hình AI mới và không khẳng định ChatGPT/Gemini không thể làm các tác vụ tương tự. Đồ án xây một prototype trợ giảng lập trình tích hợp kho tài liệu RAG, nhận câu hỏi cùng code/ảnh lỗi và dùng prompt Socratic để định hướng phản hồi trong một luồng. Đóng góp kỹ thuật là pipeline dữ liệu, retrieval và tích hợp đa phương thức; benchmark cho thấy giới hạn retrieval cần cải thiện. Đồ án chưa chứng minh hiệu quả học tập vượt chatbot phổ thông, chưa có backend auto-grading production-grade; đó là các hướng cần kiểm chứng tiếp.”

## Trạng thái đã đối chiếu — cần nắm trước khi bảo vệ

| Hạng mục | Trạng thái có bằng chứng |
|---|---|
| API chat, multimodal, upload curriculum | Có trong FastAPI routers |
| File code và ảnh | Có extractor; code tối đa 2 MB, ảnh tối đa 5 MB và chiều tối đa 2048 px |
| RAG | Có ChromaDB persistent, hai collection và RRF khi có query vectors |
| Embedding | Pipeline offline cấu hình Qwen3 1024-dim và Jina Code 768-dim |
| ChromaDB hiện tại | Đọc metadata DB: qwen3_text 4.293 records/1024-dim; jina_code 937 records/768-dim |
| Phiên bản embedding | Báo cáo ingestion ghi Version A 4.851/379; DB hiện tại là 4.293/937 (Version B) — chưa đồng nhất |
| Retrieval truy vấn mới | Backend RAG không gọi Qwen/Jina encoder cho query mới; dùng keyword fallback với distance heuristic nếu không khớp cache |
| Parser benchmark | README đánh dấu dữ liệu benchmark parser là SIMULATED_DATA / NOT_EXECUTED |
| Auto-grading | Có UI demo/heuristics; chưa thấy backend code-execution grader |
| Database và vai trò | SQLAlchemy models còn placeholder; chưa thấy auth/RBAC hay lưu gradebook/chat ở backend |
| Đánh giá | Có báo cáo 36-query A/B và báo cáo riêng 20-query; test E2E chủ yếu assert HTTP/status, chưa đo chất lượng câu trả lời hay learning gain |

---

# Nhóm 1 — Tổng quan và lý do chọn đề tài

### 1. Vì sao chọn đề tài này thay vì tự xây một chatbot tổng quát? *(Slide 2, 16, 18)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra khả năng nêu bài toán và đóng góp thực tế.
- **Trả lời tham khảo:** Đồ án không nhằm tạo mô hình nền tảng mới. Mục tiêu là tích hợp một quy trình chuyên cho học lập trình: tra cứu kho tài liệu, nhận code/ảnh lỗi và phản hồi theo prompt gợi mở. Khác biệt là workflow và phạm vi, không phải năng lực nền tảng vượt ChatGPT/Gemini.
- **Ví dụ dự án:** `POST /api/tutor/multimodal-chat` nhận prompt, file code và ảnh trong cùng request.
- **Hỏi tiếp:** Nếu chatbot phổ thông được cấu hình giống vậy thì lợi thế còn gì? Dự án hiện có nghiên cứu người dùng nào chứng minh nhu cầu chưa?

### 2. ChatGPT cho tải PDF và code lên rồi; vậy dự án có thực sự cần không? *(Slide 2, 16, 18)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra khả năng thừa nhận giới hạn và phân biệt tích hợp với tính mới.
- **Trả lời tham khảo:** Với một sinh viên và một tài liệu, chatbot phổ thông có thể đủ dùng; em không phủ nhận điều đó. Giá trị tiềm năng của dự án là chuẩn hóa kho môn học và luồng hỗ trợ cho cả lớp, không yêu cầu từng người tự chuẩn bị prompt/tài liệu. Tuy nhiên, dự án chưa có thử nghiệm chứng minh lợi ích lớp học, nên đây là giả thuyết chứ chưa phải kết luận.
- **Ví dụ dự án:** Có kho RAG tập trung và màn hình upload giáo trình, nhưng dashboard lớp hiện dùng mock data.
- **Hỏi tiếp:** Cần thử nghiệm nào để chứng minh đáng dùng hơn? Nếu kết quả không khác biệt, em sẽ kết luận gì?

### 3. Vấn đề cốt lõi mà đề tài nhắm tới là gì? *(Slide 2)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra câu phát biểu vấn đề.
- **Trả lời tham khảo:** Hệ thống nhắm tới việc gom kiến thức môn học và ngữ cảnh debug (câu hỏi, code, ảnh lỗi) vào một luồng trợ giảng có dẫn nguồn và định hướng Socratic. Không nên nói “AI khác không làm được”; vấn đề là chưa tích hợp sẵn theo workflow cụ thể của dự án.
- **Ví dụ dự án:** QuerySynthesizer rút query ngắn từ prompt, file và OCR rồi đóng gói context cho TutorService.
- **Hỏi tiếp:** Vấn đề đó được khảo sát ở sinh viên nào? Có dữ liệu về tần suất họ gặp khó khăn không?

### 4. Ai là người dùng mục tiêu và hiện mỗi nhóm làm được gì? *(Slide 3–4)*
- **Mức độ:** Cơ bản
- **Mục đích:** Phân biệt vai trò nghiệp vụ với chức năng đã triển khai.
- **Trả lời tham khảo:** Luồng chat hướng tới sinh viên; có endpoint upload curriculum và UI hướng giảng viên. Tuy nhiên, code chưa cho thấy xác thực/ủy quyền theo Student, Lecturer, Admin. Vì vậy, các vai trò là định hướng sản phẩm, chưa phải phân quyền an toàn hoàn chỉnh.
- **Ví dụ dự án:** Các router hiện có là health, tutor và knowledge; không thấy router quản lý account/role.
- **Hỏi tiếp:** Làm sao ngăn sinh viên gọi endpoint upload? Dữ liệu giảng viên hiện lưu ở đâu?

### 5. Mục tiêu kỹ thuật chính của phiên bản hiện tại là gì? *(Slide 3, 5)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra phạm vi không bị nói quá.
- **Trả lời tham khảo:** Mục tiêu đã thấy trong source là xây API chat có RAG, tiếp nhận file/ảnh, tổng hợp ngữ cảnh và gọi LLM. Không nên gộp mọi ý tưởng trong tên “Auto-Grader” thành chức năng hoàn thành.
- **Ví dụ dự án:** Tutor router trả reply, sources và suggested follow-ups.
- **Hỏi tiếp:** Tính năng nào em xem là MVP? Tính năng nào chỉ là prototype giao diện?

### 6. Đóng góp chính của đồ án là gì nếu không phải mô hình mới? *(Slide 6–9, 16)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra đóng góp kỹ thuật và tính nghiên cứu.
- **Trả lời tham khảo:** Đóng góp là pipeline dữ liệu và RAG, thiết kế hai vector space, xử lý text/code/ảnh trong cùng luồng, cùng các benchmark giúp phát hiện routing và query-runtime còn yếu. Đây là đóng góp tích hợp/đánh giá prototype, không phải đóng góp thuật toán nền tảng mới.
- **Ví dụ dự án:** Báo cáo A/B 36 câu so sánh hai chiến lược đưa chunk vào TEXT/CODE.
- **Hỏi tiếp:** Thành phần nào có thể tái sử dụng độc lập? Đóng góp nào có số liệu tốt nhất?

### 7. Ý nghĩa học thuật khác gì ý nghĩa ứng dụng? *(Slide 16–18)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra khả năng phân biệt giá trị nghiên cứu và sản phẩm.
- **Trả lời tham khảo:** Ý nghĩa học thuật là mô tả và đánh giá quyết định pipeline/retrieval trên tập benchmark xác định. Ý nghĩa ứng dụng là có thể tạo một trải nghiệm trợ giảng tích hợp. Hiện chưa có pilot lớp học nên chưa được kết luận về hiệu quả ứng dụng hoặc learning gain.
- **Ví dụ dự án:** Có metric Hit@k/MRR cho retrieval, nhưng chưa có đo trước–sau của người học.
- **Hỏi tiếp:** Cần bổ sung nhóm đối chứng nào? Kết quả nào sẽ bác bỏ giả thuyết của đề tài?

### 8. Làm sao chứng minh dự án có ích hơn chatbot đa năng? *(Slide 2, 14, 17)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra thiết kế đánh giá thực nghiệm.
- **Trả lời tham khảo:** Cho cùng một nhóm sinh viên giải bài tương đương, phân ngẫu nhiên dùng chatbot phổ thông hoặc Tutor; kiểm soát tài liệu/thời lượng; chấm mù độ đúng, khả năng tự giải bài mới và mức hiểu sau học. Hiện repository chưa có bằng chứng nghiên cứu này.
- **Ví dụ dự án:** 30 API test không đo learning gain; chỉ chủ yếu xác nhận request không lỗi.
- **Hỏi tiếp:** Cỡ mẫu bao nhiêu là hợp lý? Làm sao giảm thiên lệch do prompt hoặc độ khó bài?

---

# Nhóm 2 — Phân tích và thiết kế hệ thống

### 9. Hãy mô tả luồng một câu hỏi text từ giao diện tới phản hồi. *(Slide 5)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra hiểu kiến trúc runtime.
- **Trả lời tham khảo:** Frontend gọi tutor API; TutorService tạo query, gọi RAGService lấy chunks, dựng unified context rồi gọi Gemini. API trả reply, sources và follow-ups. Khi backend không gọi được model, có nhánh fallback dựng phản hồi.
- **Ví dụ dự án:** Endpoint text là `/api/tutor/chat`; multimodal là `/api/tutor/multimodal-chat`.
- **Hỏi tiếp:** RAG không tìm ra đoạn nào thì payload thế nào? LLM có bị gọi không?

### 10. Vai trò FastAPI là gì trong kiến trúc? *(Slide 5)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra ranh giới API/service.
- **Trả lời tham khảo:** FastAPI khai báo HTTP endpoints, nhận request, gọi services và định dạng JSON response. Logic trích xuất file/ảnh, truy xuất RAG và sinh tutor response được đặt ở service riêng.
- **Ví dụ dự án:** `tutor.py` gọi `multimodal_service` và `tutor_service`.
- **Hỏi tiếp:** Vì sao không viết toàn bộ logic trong router? Lỗi service được trả cho client thế nào?

### 11. QuerySynthesizer làm gì và tại sao cần nó? *(Slide 5, 8, 10)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra hiểu xử lý truy vấn đa phương thức.
- **Trả lời tham khảo:** Nó trích lỗi phổ biến, nhận diện ngôn ngữ theo tín hiệu, rút gọn query tìm kiếm và đóng gói câu hỏi, file, OCR, RAG chunks. Query ngắn giúp tránh đưa hàng trăm dòng code vào vector search.
- **Ví dụ dự án:** Query được giới hạn tối đa 250 ký tự; unified context giữ riêng từng phần dữ liệu.
- **Hỏi tiếp:** Nếu OCR nhận dạng sai lỗi thì ảnh hưởng gì? Vì sao query gọn không đồng nghĩa context LLM cũng phải gọn như vậy?

### 12. ChromaDB khác gì PostgreSQL trong dự án? *(Slide 5–7)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra lựa chọn lưu trữ.
- **Trả lời tham khảo:** ChromaDB lưu document, metadata và vector để truy xuất láng giềng gần. PostgreSQL là cơ sở dữ liệu quan hệ được cấu hình trong Compose, nhưng schema nghiệp vụ của dự án hiện còn placeholder; không nên nói lịch sử chat/điểm đã persist ở đó.
- **Ví dụ dự án:** RAGService đọc persistent ChromaDB tại `data/09_chromadb`.
- **Hỏi tiếp:** Metadata nào cần chỉ mục? Khi nào PostgreSQL phù hợp hơn vector store?

### 13. Thành phần nào gọi LLM và thành phần nào truy xuất tri thức? *(Slide 5, 11)*
- **Mức độ:** Cơ bản
- **Mục đích:** Phân biệt retrieval với generation.
- **Trả lời tham khảo:** RAGService chọn chunks từ ChromaDB; TutorService dựng prompt/context và gọi Gemini để sinh câu trả lời. ChromaDB không sinh ngôn ngữ tự nhiên và Gemini không trực tiếp quản lý index.
- **Ví dụ dự án:** `format_rag_context_for_prompt` định dạng nguồn trước khi gửi LLM.
- **Hỏi tiếp:** Nếu bỏ Gemini, còn phần nào chạy được? Nếu bỏ ChromaDB thì phần nào mất căn cứ?

### 14. Tại sao chat text và multimodal có endpoint riêng? *(Slide 4–5)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra thiết kế giao tiếp API.
- **Trả lời tham khảo:** Chat text nhận Pydantic JSON đơn giản; multimodal nhận multipart FormData gồm prompt, danh sách file và ảnh. Cách này phù hợp kiểu payload khác nhau, dù cả hai cùng gọi TutorService sau chuẩn hóa.
- **Ví dụ dự án:** Frontend `sendMultimodalChat` thêm các trường `code_files` và `image_files`.
- **Hỏi tiếp:** Vì sao file upload thường cần multipart? Cần giới hạn tổng kích thước request ở đâu?

### 15. PostgreSQL và Redis có tham gia luồng tutoring không? *(Slide 5, 15)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra phân biệt cấu hình với triển khai nghiệp vụ.
- **Trả lời tham khảo:** Compose và health service cấu hình PostgreSQL/Redis, nhưng luồng tutor hiện đọc ChromaDB và gọi Gemini; chưa thấy code lưu hội thoại/gradebook vào PostgreSQL hoặc dùng Redis làm queue/cache cho request tutoring.
- **Ví dụ dự án:** `models/__init__.py` chỉ khai báo Base placeholder.
- **Hỏi tiếp:** Nếu triển khai lịch sử chat, cần bảng và chính sách retention nào? Redis nên dùng cho loại tác vụ nào?

### 16. Hệ thống phân quyền Student/Lecturer/Admin ra sao? *(Slide 4, 15)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra nhận diện thiếu sót bảo mật.
- **Trả lời tham khảo:** Hiện chưa thấy authentication middleware/dependency hay role checks ở routers. UI có thành phần hướng tới giảng viên nhưng không đủ chứng minh quyền được bảo vệ ở backend. RBAC cần triển khai server-side trước khi dùng thực tế.
- **Ví dụ dự án:** Endpoint upload curriculum hiện được khai báo trực tiếp trong knowledge router.
- **Hỏi tiếp:** Vì sao ẩn nút trên frontend không phải phân quyền? Bạn sẽ kiểm tra quyền upload ở đâu?

---

# Nhóm 3 — Công nghệ

### 17. Vì sao dùng Next.js cho frontend? *(Slide 5, 13)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra hiểu stack giao diện.
- **Trả lời tham khảo:** Repository dùng Next.js/React để tạo giao diện chat component-based, Tailwind để bố trí giao diện và Axios để gọi API. Đây là lựa chọn triển khai, không phải đóng góp mới; React SPA khác cũng có thể đáp ứng.
- **Ví dụ dự án:** `frontend/src/lib/api.ts` định nghĩa client gọi `/api/tutor/multimodal-chat`.
- **Hỏi tiếp:** Điểm nào trong bài toán cần Next.js đặc biệt? Nếu UI cần SEO thì App Router giúp gì?

### 18. Vì sao dùng FastAPI thay cho Flask? *(Slide 5)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra lý do chọn backend.
- **Trả lời tham khảo:** FastAPI có khai báo kiểu/Pydantic, sinh OpenAPI docs và hỗ trợ endpoint async, phù hợp API nhận text/file. Tuy nhiên, việc dùng async không tự làm mọi tác vụ blocking thành non-blocking; service gọi model có đoạn đưa qua thread.
- **Ví dụ dự án:** App công bố docs tại `/docs`, tutor router khai báo request/response path.
- **Hỏi tiếp:** Khi nào tác vụ CPU-bound cần worker riêng? Lỗi blocking trong event loop gây hậu quả gì?

### 19. Vì sao không lưu vector vào PostgreSQL thường? *(Slide 7)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra lựa chọn vector store.
- **Trả lời tham khảo:** ChromaDB cung cấp API lưu embedding và ANN search tiện cho prototype RAG. PostgreSQL quan hệ thích hợp cho dữ liệu nghiệp vụ; nếu dùng extension vector thì cũng có thể làm vector search. Chọn lựa cần dựa trên quy mô, filter, vận hành và chi phí.
- **Ví dụ dự án:** ChromaDB PersistentClient và hai collection đang lưu corpus.
- **Hỏi tiếp:** Khi nào chuyển sang Qdrant/Milvus? Migrate dữ liệu cần giữ những gì?

### 20. PostgreSQL đã lưu dữ liệu nào của sinh viên chưa? *(Slide 5, 15)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra claims persistence.
- **Trả lời tham khảo:** Source hiện xác minh kết nối/health PostgreSQL và cấu hình Compose; package model ghi rõ placeholder, chưa thấy schema và CRUD lịch sử chat, user hay gradebook. Vì vậy em không khẳng định dữ liệu nghiệp vụ đang được lưu ở PostgreSQL.
- **Ví dụ dự án:** Backend DB module thực hiện `SELECT 1`; models package chỉ có `Base`.
- **Hỏi tiếp:** Nếu bổ sung, entity nào cần tạo? Có nên lưu code người học nguyên văn không?

### 21. Redis đang được dùng để làm gì? *(Slide 5, 15)*
- **Mức độ:** Nâng cao
- **Mục đích:** Phân biệt hạ tầng khai báo với chức năng thực thi.
- **Trả lời tham khảo:** Redis được cấu hình URL và health check; chưa thấy tutoring router sử dụng queue/cache thực tế. Nên mô tả là thành phần hạ tầng có trong Compose, không khẳng định đã xử lý hàng đợi.
- **Ví dụ dự án:** `health.py` ping Redis; tutor service không gọi redis client.
- **Hỏi tiếp:** Redis có thể cache query embedding thế nào? Cache sai version model gây vấn đề gì?

### 22. Vì sao API multimodal dùng FormData? *(Slide 4–5, 10)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra hiểu truyền file qua HTTP.
- **Trả lời tham khảo:** Multipart cho phép gửi trường văn bản và byte file trong cùng request. JSON thuần phù hợp text nhưng cần encode file phức tạp/kém hiệu quả hơn. Server vẫn cần giới hạn tổng payload, kiểm tra MIME thực tế và xử lý file lỗi.
- **Ví dụ dự án:** `sendMultimodalChat` append prompt, code_files, image_files.
- **Hỏi tiếp:** Content-Type do ai tạo boundary? Vì sao không nên chỉ tin filename/MIME client gửi?

### 23. Vì sao backend chọn Gemini? *(Slide 11)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra lựa chọn model và phụ thuộc.
- **Trả lời tham khảo:** Backend cấu hình provider Gemini và model name trong Settings. Đây là lựa chọn của prototype; cần so sánh chất lượng, latency, cost, context và điều khoản dữ liệu trước production. Source không có benchmark so sánh Gemini với mọi model khác.
- **Ví dụ dự án:** TutorService dùng `settings.GEMINI_MODEL`, mặc định `gemini-3-flash-preview`.
- **Hỏi tiếp:** Nếu model ngừng khả dụng thì làm sao? Có cách nào thay model mà không đổi business logic?

### 24. Dự án có hỗ trợ Ollama không? *(Slide 11, 15)*
- **Mức độ:** Nâng cao
- **Mục đích:** Phân biệt code path frontend và backend.
- **Trả lời tham khảo:** `socraticEngine.ts` có hàm gọi Ollama cục bộ; backend TutorService lại gọi Google Gemini. Vì vậy có code path hỗ trợ Ollama ở frontend, nhưng không nên nói toàn bộ RAG backend có local LLM mode thống nhất nếu chưa kiểm thử tích hợp.
- **Ví dụ dự án:** Frontend gọi `http://localhost:11434/api/generate`; backend dùng `google.generativeai`.
- **Hỏi tiếp:** Ollama path có gọi RAG backend không? Nếu không, nguồn kiến thức nào được dùng?

---

# Nhóm 4 — AI và LLM

### 25. LLM đóng vai trò gì và không đóng vai trò gì? *(Slide 5, 11)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra hiểu ranh giới năng lực.
- **Trả lời tham khảo:** LLM sinh lời giải thích/gợi ý từ prompt và context. Nó không phải cơ sở dữ liệu nguồn chân lý, không thực thi bài code ở backend và không tự bảo đảm câu trả lời đúng. Retrieval, kiểm thử và cơ chế an toàn cần đảm nhiệm phần khác.
- **Ví dụ dự án:** Gemini nhận unified context sau khi RAG trả chunks.
- **Hỏi tiếp:** Vì sao LLM có thể bịa? Có thể bỏ hoàn toàn LLM không?

### 26. Vì sao chọn model hiện tại thay vì model khác? *(Slide 11)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra căn cứ lựa chọn.
- **Trả lời tham khảo:** Source cấu hình Gemini Flash làm model backend; đây là cấu hình triển khai chứ chưa phải kết luận khoa học rằng nó tốt hơn. Cần benchmark cùng bộ câu hỏi, rubric, độ trễ và chi phí để chứng minh lựa chọn.
- **Ví dụ dự án:** Không có báo cáo A/B LLM model nào trong các bằng chứng đã đối chiếu.
- **Hỏi tiếp:** Chỉ số nào quan trọng hơn benchmark token/s? Ai chấm chất lượng tutor response?

### 27. RAG có loại bỏ hallucination không? *(Slide 8, 11)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra hiểu hạn chế RAG.
- **Trả lời tham khảo:** Không. RAG chỉ cung cấp ngữ cảnh có liên quan hơn; retriever có thể lấy sai đoạn và LLM vẫn có thể suy diễn ngoài nguồn. Cần abstain khi không đủ căn cứ, kiểm tra citation và đánh giá factuality.
- **Ví dụ dự án:** System prompt yêu cầu dựa vào context nhưng chưa có metric đo grounding.
- **Hỏi tiếp:** Làm sao phát hiện câu trả lời không được nguồn hỗ trợ? Khi nào tutor nên từ chối trả lời?

### 28. Prompt grounding được thực hiện như thế nào? *(Slide 8, 11)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra prompt engineering.
- **Trả lời tham khảo:** TutorService đưa system instruction về dùng tài liệu RAG, nêu nguồn, đặt câu hỏi gợi mở và không viết toàn bộ lời giải. QuerySynthesizer ghép các đoạn truy xuất vào user context. Đây là hướng dẫn cho model, không phải cơ chế cưỡng chế.
- **Ví dụ dự án:** `SOCRATIC_SYSTEM_PROMPT` và `format_rag_context_for_prompt`.
- **Hỏi tiếp:** Prompt injection trong code/tài liệu được xử lý thế nào? Model có thể bỏ qua system prompt không?

### 29. Temperature thấp giúp gì? *(Slide 11)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra tham số sinh.
- **Trả lời tham khảo:** Temperature 0.2 giảm tính ngẫu nhiên tương đối, có thể làm phản hồi ổn định hơn nhưng không bảo đảm deterministic hoặc đúng. Kết quả còn phụ thuộc model version, prompt, context và backend provider.
- **Ví dụ dự án:** TutorService đặt temperature 0.2, top_p 0.95.
- **Hỏi tiếp:** Vì sao cùng prompt vẫn có output khác? Có nên tăng temperature cho câu hỏi sáng tạo không?

### 30. Fallback hoạt động ra sao khi Gemini lỗi? *(Slide 11)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra resilience.
- **Trả lời tham khảo:** TutorService thử danh sách model ứng viên và nếu không gọi được thì dựng phản hồi mẫu từ lỗi, ngôn ngữ và RAG chunk. Fallback giúp API có nội dung phản hồi, nhưng nội dung mẫu không tương đương chất lượng của LLM và phải được thể hiện rõ cho người dùng.
- **Ví dụ dự án:** `_build_socratic_fallback` đưa snippet top RAG và câu hỏi debug.
- **Hỏi tiếp:** Làm sao UI phân biệt fallback? Khi nào nên trả lỗi thay vì phản hồi mẫu?

### 31. Đánh giá chất lượng câu trả lời AI thế nào? *(Slide 14, 17)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra thiết kế đánh giá generation.
- **Trả lời tham khảo:** Cần rubric chuyên gia cho tính đúng, grounding, tính sư phạm, mức độ giải hộ, an toàn; thêm đánh giá người dùng và test hồi quy. Hiện test E2E đa số xác nhận HTTP/status, nên chưa chứng minh chất lượng câu trả lời.
- **Ví dụ dự án:** Test `test_t01...` kiểm tra reply dài hơn 50 ký tự, không kiểm tra đúng/sai.
- **Hỏi tiếp:** Nên dùng LLM-as-judge không? Làm sao kiểm định độ nhất quán giữa người chấm?

### 32. Code và ảnh người dùng có được giữ riêng tư không? *(Slide 15)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra hiểu luồng dữ liệu đến dịch vụ bên ngoài.
- **Trả lời tham khảo:** Khi cấu hình Gemini, prompt, context và ảnh được gửi tới Google API theo luồng xử lý. Repository chưa chứng minh chính sách retention/consent/ẩn danh. Cần thông báo cho người dùng, lọc secret và xác định thời gian lưu trước khi dùng dữ liệu thật.
- **Ví dụ dự án:** `image_extractor.py` gửi bytes ảnh tới Gemini Vision; TutorService gửi payload tới Gemini.
- **Hỏi tiếp:** Làm sao phát hiện API key trong code tải lên? Có lựa chọn local model nào đã được tích hợp end-to-end?

---

# Nhóm 5 — RAG

### 33. RAG là gì? *(Slide 6–8)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra nền tảng kỹ thuật.
- **Trả lời tham khảo:** Retrieval-Augmented Generation gồm lấy các đoạn tri thức phù hợp từ kho ngoài rồi đưa chúng vào context để LLM tạo câu trả lời. “Augmented” nghĩa là bổ sung context, không phải fine-tune trọng số mô hình.
- **Ví dụ dự án:** ChromaDB trả chunks rồi TutorService đính kèm trích đoạn vào prompt.
- **Hỏi tiếp:** RAG khác fine-tuning thế nào? Dữ liệu mới cập nhật theo cách nào?

### 34. Tại sao không dùng LLM thuần? *(Slide 2, 6, 11)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra lý do dùng kho kiến thức ngoài.
- **Trả lời tham khảo:** Kho ngoài cho phép chọn tài liệu tham chiếu và cập nhật tri thức mà không huấn luyện lại model; có thể trả trích dẫn. Tuy nhiên, nếu retrieval sai thì lợi ích giảm và RAG vẫn không bảo đảm chính xác tuyệt đối.
- **Ví dụ dự án:** Corpus có tài liệu Python, DSA và tài liệu bảo mật.
- **Hỏi tiếp:** Nếu câu hỏi không có trong corpus thì sao? Làm sao tránh citation giả?

### 35. Hãy mô tả các bước RAG của dự án. *(Slide 5–8)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra toàn bộ data flow.
- **Trả lời tham khảo:** Dữ liệu được clean/chunk, embedding offline và ingest ChromaDB; request được tổng hợp thành query, truy xuất top-k, định dạng context rồi gọi LLM. Cần nhấn mạnh query runtime hiện có cache/fallback lexical, không phải mọi truy vấn mới đều được embedding live.
- **Ví dụ dự án:** `all_chunks.json` và persistent ChromaDB.
- **Hỏi tiếp:** Metadata filter áp dụng ở bước nào? Top-k 4 ảnh hưởng prompt thế nào?

### 36. Chunking là gì và vì sao quan trọng? *(Slide 6)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra chất lượng đơn vị retrieval.
- **Trả lời tham khảo:** Chunking chia tài liệu thành các đoạn để lập chỉ mục. Chunk quá ngắn mất ngữ cảnh; quá dài làm nhiều ý trộn vào nhau và tăng token context. Dự án có chunk engine nhận diện heading/bảng/code; cần đánh giá chất lượng đầu ra thay vì chỉ đếm chunks.
- **Ví dụ dự án:** Báo cáo dataset ghi 5.230 chunks.
- **Hỏi tiếp:** Chunk overlap có ích gì? Làm sao chọn kích thước chunk theo loại tài liệu?

### 37. Breadcrumb/context header giải quyết vấn đề nào? *(Slide 6)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra hiểu metadata ngữ cảnh.
- **Trả lời tham khảo:** Breadcrumb gắn tên tài liệu, chương/mục để một đoạn rời vẫn mang vị trí và chủ đề. Nó giúp retrieval và trích dẫn có ngữ cảnh, nhưng không tự sửa nội dung parser sai.
- **Ví dụ dự án:** Chunk metadata lưu source_file, section_title, section_path.
- **Hỏi tiếp:** Metadata có được index để filter không? Nếu section_path sai thì hậu quả gì?

### 38. RAG trả về rỗng thì hệ thống làm gì? *(Slide 8, 11)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra tình huống không có evidence.
- **Trả lời tham khảo:** Unified payload ghi rõ không tìm thấy đoạn trích cụ thể; Tutor vẫn có thể gửi context đó tới LLM hoặc fallback. Cần cân nhắc chế độ trả lời có điều kiện/abstain để tránh model tự bịa nguồn khi không có evidence.
- **Ví dụ dự án:** QuerySynthesizer thêm thông báo không tìm thấy chunk.
- **Hỏi tiếp:** Có threshold để trả “không đủ tài liệu” chưa? Làm sao kiểm thử trường hợp này?

### 39. Reranking là gì và dự án đã triển khai chưa? *(Slide 8, 17)*
- **Mức độ:** Nâng cao
- **Mục đích:** Phân biệt thuật toán được làm với hướng đề xuất.
- **Trả lời tham khảo:** Reranking chấm lại các candidate, thường bằng cross-encoder so trực tiếp query và document. Báo cáo A/B đề xuất reranker, nhưng trong backend được đối chiếu chưa thấy cross-encoder reranker được gọi trong runtime.
- **Ví dụ dự án:** RAGService hiện hợp nhất RRF; không có lời gọi reranker.
- **Hỏi tiếp:** Reranker tăng latency thế nào? Chọn candidate pool ra sao?

### 40. Ground truth đa nguồn có tác dụng gì? *(Slide 9, 14)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra chất lượng đánh giá retrieval.
- **Trả lời tham khảo:** Một truy vấn có thể có nhiều đoạn đúng từ nhiều tài liệu; đánh giá nhiều ground-truth IDs giảm việc phạt retriever chỉ vì nó tìm đoạn tương đương từ nguồn khác. Tuy nhiên, việc gán ground truth phải có quy tắc và reviewer, nếu không điểm số có thể bị thiên lệch.
- **Ví dụ dự án:** Day 06 report nói tới multi-source canonical GT.
- **Hỏi tiếp:** Ai xác nhận một chunk thực sự trả lời được câu hỏi? Có thể dùng graded relevance thay binary hit không?

---

# Nhóm 6 — Embedding, ChromaDB và Retrieval

### 41. Embedding là gì? *(Slide 7)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra hiểu vector biểu diễn ngữ nghĩa.
- **Trả lời tham khảo:** Embedding ánh xạ văn bản/code thành vector số. Các vector gần nhau theo metric đã chọn thường được kỳ vọng biểu diễn nội dung liên quan; chất lượng phụ thuộc model, dữ liệu, hướng dẫn query và domain.
- **Ví dụ dự án:** Pipeline cấu hình Qwen3 1024 chiều và Jina Code 768 chiều.
- **Hỏi tiếp:** Vector gần nhau có luôn cùng nghĩa không? Embedding có giữ nguyên cú pháp code không?

### 42. Vì sao tách TEXT và CODE? *(Slide 7)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra quyết định routing.
- **Trả lời tham khảo:** Văn xuôi đa ngữ và code có dạng token/cấu trúc khác nhau; model chuyên code có thể hữu ích với code thuần, model text tốt hơn với giải thích. Nhưng chunk thường pha trộn; benchmark A/B cho thấy routing theo nhãn code_example làm giảm điểm tổng trên tập 36 câu.
- **Ví dụ dự án:** Version A/B đổi cách phân 558 chunks; A Hit@3 36.11%, B 33.33%.
- **Hỏi tiếp:** Dùng dual representation cho mixed chunk có đáng thử không? Nhãn content_type có đáng tin không?

### 43. Vì sao Qwen3 và Jina có số chiều khác nhau? *(Slide 7)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra cấu hình model.
- **Trả lời tham khảo:** Kích thước embedding là đặc tính model/configuration: Qwen3 được cấu hình 1024; Jina Code là 768. Hai vector space được lưu riêng nên không cần ép chiều bằng nhau; không được tính cosine giữa vector của hai model khác nhau.
- **Ví dụ dự án:** Chroma metadata hiện xác nhận dimension 1024 và 768.
- **Hỏi tiếp:** Nếu đổi dimension cần làm gì? Chroma collection có cho mixed dimension không?

### 44. Cosine distance/similarity được hiểu ra sao? *(Slide 7–8)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra metric và interpretation.
- **Trả lời tham khảo:** Cosine similarity so hướng hai vector; cosine distance trong Chroma thường là 1 trừ similarity theo cấu hình. Cần kiểm tra space thực tế và không gọi heuristic score là cosine. Trong lexical fallback hiện tại, khoảng cách được gán theo số từ khớp, không phải đo cosine.
- **Ví dụ dự án:** `_fuse_rrf` chuyển distance thành similarity; fallback tạo dist theo hit_count.
- **Hỏi tiếp:** Vì sao vector chuẩn hóa L2 vẫn dùng cosine? Cosine distance có thể âm không?

### 45. ChromaDB lưu gì và tìm kiếm thế nào? *(Slide 7)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra vector database.
- **Trả lời tham khảo:** Mỗi record gồm ID, document, metadata và embedding. Collection dùng cấu hình cosine/HNSW để tìm gần đúng; persistent client giữ dữ liệu trên đĩa. Hai collection của dự án có dimension độc lập.
- **Ví dụ dự án:** `qwen3_text`, `jina_code` nằm trong `data/09_chromadb`.
- **Hỏi tiếp:** ANN khác exact nearest neighbor thế nào? Metadata filter có thể làm giảm số candidate không?

### 46. Backend tạo embedding query mới bằng cách nào? *(Slide 8)*
- **Mức độ:** Phản biện
- **Mục đích:** Phát hiện hiểu biết về giới hạn runtime.
- **Trả lời tham khảo:** RAGService dò query cache trong file benchmark; nếu có vector thì dùng để query. Nếu không có vector phù hợp, đường đi hiện tại rơi về keyword matching/`where_document` và heuristic distance; service không gọi query encoder Qwen/Jina để embed câu hỏi tùy ý.
- **Ví dụ dự án:** `search()` gọi `_match_cached_vector`, sau đó fallback khi `q_vectors` rỗng.
- **Hỏi tiếp:** Vì sao đây là vấn đề cho người dùng thật? Em sẽ tích hợp query embedding ở đâu và kiểm thử bằng câu hỏi unseen thế nào?

### 47. RRF hoạt động ra sao? *(Slide 8)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra cơ chế hợp nhất.
- **Trả lời tham khảo:** Reciprocal Rank Fusion cộng điểm `1/(k0 + rank)` từ mỗi danh sách. Nó tận dụng thứ hạng mà không cộng thẳng distance khác scale; nếu ID chỉ xuất hiện ở một list thì vẫn có điểm từ list đó.
- **Ví dụ dự án:** RAGService đặt k0 mặc định 60 và fuse hai collection.
- **Hỏi tiếp:** Kết quả thay đổi thế nào nếu chọn k0 nhỏ? Có nên gán trọng số khác nhau cho hai nguồn không?

### 48. Vì sao số lượng collection giữa báo cáo và database khác nhau? *(Slide 7, 9)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra tính nhất quán báo cáo.
- **Trả lời tham khảo:** Đây là sai khác phiên bản cần công khai: ingestion report ghi Version A 4.851/379; DB hiện tại đọc trực tiếp là 4.293/937, trùng phân bổ Version B; test cũng kỳ vọng B. Chưa đủ căn cứ để gọi một báo cáo là current production truth nếu chưa đồng bộ manifest và artifacts.
- **Ví dụ dự án:** `chromadb_ingestion_report.md`, `routing_ab_benchmark_report.md`, test RAG và SQLite DB không cùng snapshot.
- **Hỏi tiếp:** Trước bảo vệ em sẽ chốt con số nào? Cần lưu fingerprint/version manifest nào để tránh lặp lại?

---

# Nhóm 7 — Đánh giá và phân tích mã nguồn

### 49. Hệ thống phân tích code người dùng ở đâu? *(Slide 10, 12)*
- **Mức độ:** Trung bình
- **Mục đích:** Phân biệt đọc code qua LLM với static analyzer.
- **Trả lời tham khảo:** FileExtractor kiểm tra và đóng gói code; QuerySynthesizer đưa nội dung vào prompt; LLM có thể nhận xét theo prompt. Đây không đồng nghĩa dự án có compiler, AST analyzer hoặc backend static analysis service.
- **Ví dụ dự án:** Tutor router không gọi code grading endpoint riêng.
- **Hỏi tiếp:** Làm sao định vị line chính xác? LLM nhận code lớn sẽ bị giới hạn context thế nào?

### 50. Hệ thống xác định Big-O bằng cách nào? *(Slide 12)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra phân biệt heuristic và phân tích thuật toán.
- **Trả lời tham khảo:** UI CodeSandbox có heuristic regex đếm vòng lặp lồng/đệ quy; đây không phải phân tích AST hay chứng minh độ phức tạp. Nó có thể sai với vòng lặp có bound khác nhau, vòng lặp tuần tự, input-dependent recursion hoặc helper calls.
- **Ví dụ dự án:** `estimateComplexity` trả kết quả dựa trên regex `for/while`.
- **Hỏi tiếp:** Hãy cho trường hợp heuristic kết luận sai. Em sẽ dùng AST hoặc symbolic analysis thế nào?

### 51. Static analysis khác dynamic analysis thế nào? *(Slide 12, 17)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra khái niệm kiểm thử code.
- **Trả lời tham khảo:** Static analysis kiểm tra source mà không chạy chương trình; dynamic analysis quan sát khi chạy với input cụ thể. UI hiện có rule-based scan một số pattern, nhưng chưa đủ bằng chứng tích hợp linter chuẩn hoặc runtime backend an toàn.
- **Ví dụ dự án:** Quality modal dò một số pattern như broad except/nested loops.
- **Hỏi tiếp:** Test cases thuộc loại nào? Static analysis có thể phát hiện mọi lỗi runtime không?

### 52. Phát hiện vulnerability trong code được triển khai thế nào? *(Slide 12, 15)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra độ chính xác claim bảo mật.
- **Trả lời tham khảo:** Tutor prompt có thể được hỏi về lỗi; CodeQuality UI có heuristics hạn chế. Chưa thấy backend scanner hay security ruleset có kiểm thử benchmark. Không nên trình bày là hệ thống phát hiện CWE/SAST đáng tin cậy.
- **Ví dụ dự án:** Router backend không có endpoint dedicated security scan.
- **Hỏi tiếp:** Làm sao đo false positive/false negative? Có thể tích hợp Bandit/Semgrep thế nào?

### 53. Code người dùng có được chạy an toàn không? *(Slide 12, 15)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra rủi ro thực thi mã tùy ý.
- **Trả lời tham khảo:** Chưa có backend sandbox runner được xác minh. UI chạy JavaScript bằng `new Function`; một số ngôn ngữ khác mô phỏng đầu ra và số đo. Không nên dùng tính năng này để chấm code không tin cậy hoặc tuyên bố cô lập an toàn.
- **Ví dụ dự án:** `CodeSandboxModal.tsx` có nhánh simulator cho Python/C++/Java.
- **Hỏi tiếp:** Cần cô lập filesystem/network/process thế nào? CPU, RAM, wall-clock và cleanup cần kiểm soát ở đâu?

### 54. “30 kịch bản PASS” chứng minh điều gì? *(Slide 14)*
- **Mức độ:** Phản biện
- **Mục đích:** Đánh giá độ mạnh của kiểm thử.
- **Trả lời tham khảo:** Nó cho thấy các request trong fixture được endpoint xử lý và trả status/field cơ bản theo assertion. Nó không chứng minh OCR đọc đúng, câu trả lời đúng về code hay chất lượng sư phạm; ảnh trong test được tạo tổng hợp bằng code.
- **Ví dụ dự án:** Các assertion chủ yếu kiểm tra `status_code == 200`, status success hoặc file/image count.
- **Hỏi tiếp:** Bạn sẽ sửa assertion nào trước? Làm sao đưa expected facts vào regression test?

### 55. Upload curriculum tạo vector thế nào? *(Slide 13)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra sự nhất quán encoder/index.
- **Trả lời tham khảo:** Endpoint cắt text theo ký tự/đoạn; gọi Gemini embedding nếu có key, nếu lỗi/no key thì dùng pseudo-normalized vector xác định từ hash. Điều này không tương thích ngữ nghĩa với index Qwen/Jina hiện có, dù dimension có thể khớp; cần sửa trước khi tin kết quả search trên tài liệu mới.
- **Ví dụ dự án:** `generate_embedding()` trong knowledge router.
- **Hỏi tiếp:** Vì sao cùng số chiều không đồng nghĩa cùng vector space? Cần tạo collection/version riêng hay re-embed?

### 56. Có plagiarism detector thật không? *(Slide 3, 12)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra các tính năng giao diện dễ bị hiểu nhầm.
- **Trả lời tham khảo:** Có component PlagiarismCheckerModal trong frontend, nhưng chưa thấy backend service/API hoặc thuật toán được đánh giá trong evidence đã đối chiếu. Vì vậy chỉ nên gọi là giao diện/ý tưởng demo, không tuyên bố phát hiện đạo văn thực tế.
- **Ví dụ dự án:** Các backend routers hiện có không gồm plagiarism endpoint.
- **Hỏi tiếp:** Similarity giữa hai code có chứng minh gian lận không? Cần xử lý false accusation thế nào?

---

# Nhóm 8 — Kiểm thử và thực nghiệm

### 57. Hit@K là gì? *(Slide 9)*
- **Mức độ:** Cơ bản
- **Mục đích:** Kiểm tra hiểu metric retrieval.
- **Trả lời tham khảo:** Hit@K là tỷ lệ query mà ít nhất một ground-truth item xuất hiện trong top K. Nó không đo đầy đủ chất lượng nội dung hoặc câu trả lời generation.
- **Ví dụ dự án:** Hit@3 trên 36 query của A là 36.11% theo báo cáo A/B.
- **Hỏi tiếp:** Hit@K khác Recall@K thế nào? Một query có nhiều GT thì Hit@K phản ánh gì?

### 58. Ground truth là gì trong benchmark này? *(Slide 9, 14)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra nền tảng đánh giá.
- **Trả lời tham khảo:** Ground truth là ID chunk được đánh dấu liên quan/đáp ứng cho từng query để đối chiếu thứ hạng. Chất lượng metric phụ thuộc vào tính đầy đủ và chính xác của nhãn; báo cáo có nhiều lần điều chỉnh ground truth.
- **Ví dụ dự án:** `routing_ab_eval_36q.json` chứa query và canonical IDs.
- **Hỏi tiếp:** Vì sao single-source GT có thể đánh giá thấp retriever? Ai duyệt relevance?

### 59. MRR đo gì? *(Slide 9)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra hiểu vị trí của kết quả đúng.
- **Trả lời tham khảo:** Mean Reciprocal Rank lấy nghịch đảo thứ hạng của kết quả đúng đầu tiên rồi trung bình trên query; đúng ở rank 1 cho 1.0, rank 5 cho 0.2, không thấy trong cutoff thường là 0.
- **Ví dụ dự án:** A MRR@5 0.3213, B 0.2843 trên benchmark 36 câu.
- **Hỏi tiếp:** Vì sao MRR không đo mức độ đầy đủ các đoạn liên quan? Metric nào bổ sung được?

### 60. Kết quả 36-query A/B nói lên điều gì? *(Slide 9)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra khả năng diễn giải số liệu.
- **Trả lời tham khảo:** Version A đạt Hit@3 36.11%, Hit@5 41.67%, MRR@5 0.3213; Version B đạt 33.33%, 38.89%, 0.2843. Trên tập này A nhỉnh hơn, nhưng điểm tuyệt đối còn thấp và mẫu nhỏ; không chứng minh hiệu quả mọi query.
- **Ví dụ dự án:** B giúp một phần truy vấn code nhưng làm giảm theory.
- **Hỏi tiếp:** Kết quả có ý nghĩa thống kê không? Cần tăng loại query nào?

### 61. Tại sao report Day 06 nói Hit@3 100% trong khi A/B chỉ 33–36%? *(Slide 9, 14)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra reconciliation giữa báo cáo.
- **Trả lời tham khảo:** Hai kết quả dùng benchmark khác: Day 06 dùng 20 query và multi-source canonical GT; A/B dùng 36 query cân bằng 4 nhóm và so Version A/B routing. Không được gộp hoặc chọn số đẹp nhất; cần trình bày tập, GT, version và thời điểm rõ ràng. Còn có sai khác version DB trong repo.
- **Ví dụ dự án:** Day06 report và routing_ab_benchmark_report.
- **Hỏi tiếp:** Nếu hội đồng chỉ cho một chỉ số, em chọn báo cáo nào và vì sao? Em sẽ tái lập benchmark thế nào?

### 62. Vì sao benchmark parser PDF không được trình bày như kết quả thực nghiệm? *(Slide 6, 14)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra trung thực nguồn dữ liệu.
- **Trả lời tham khảo:** README ghi rõ dataset parser là synthetic, `NOT_EXECUTED`, không có parser thực thi và các score là giả định mô phỏng. Dự án có cleaned corpus cho RAG, nhưng điều đó không chứng minh benchmark so sánh parser đã chạy thực tế.
- **Ví dụ dự án:** README có mục “Important Limitations” cấm dùng synthetic data để chọn parser.
- **Hỏi tiếp:** Làm benchmark thật cần ground truth nào? Cần đo accuracy và runtime ra sao?

### 63. Test E2E hiện tại đo mức nào? *(Slide 14)*
- **Mức độ:** Trung bình
- **Mục đích:** Phân biệt integration coverage với semantic evaluation.
- **Trả lời tham khảo:** Test gọi FastAPI TestClient với 10 text, 10 file, 10 ảnh synthetic; phần lớn xác nhận status 200 và response fields. Chưa có oracle để chấm đúng nội dung, và OCR mock tests chỉ kiểm tra parser output được mock client cung cấp.
- **Ví dụ dự án:** `create_synthetic_terminal_image()` tự dựng ảnh cho test.
- **Hỏi tiếp:** Nên bổ sung test nào để đo OCR? Làm sao test không phụ thuộc Gemini API?

### 64. Hạn chế lớn nhất của thực nghiệm là gì? *(Slide 9, 14, 17)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra tư duy nghiên cứu.
- **Trả lời tham khảo:** Bộ truy vấn nhỏ và có thể trùng cache; ground truth có chỉnh sửa; các version vector/report không đồng bộ; E2E test chủ yếu kiểm tra HTTP; chưa có user study. Do đó số liệu là bằng chứng bước đầu về pipeline, chưa phải bằng chứng sản phẩm học tập hiệu quả.
- **Ví dụ dự án:** 36-query A/B cùng 20-query Day06 có kết quả rất khác.
- **Hỏi tiếp:** Hạn chế nào ảnh hưởng nhiều nhất tới kết luận? Bạn ưu tiên khắc phục theo thứ tự nào?

---

# Nhóm 9 — Bảo mật, riêng tư và mở rộng

### 65. FileExtractor có những lớp kiểm tra nào? *(Slide 10, 15)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra triển khai nhận file.
- **Trả lời tham khảo:** Có giới hạn 2 MB, allowlist extension, denylist một số định dạng nguy hiểm, magic-byte/binary checks, sanitize filename, giải mã text và hash SHA-256. Đây là kiểm tra đầu vào, không phải virus scanner hay sandbox.
- **Ví dụ dự án:** `MAX_FILE_SIZE_BYTES = 2 * 1024 * 1024`.
- **Hỏi tiếp:** Kiểm tra magic bytes bỏ sót gì? Có kiểm tra tổng kích thước nhiều file không?

### 66. Ảnh được xử lý và gửi đi thế nào? *(Slide 10, 15)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra luồng Vision và giới hạn.
- **Trả lời tham khảo:** ImageExtractor kiểm tra tối đa 5 MB và định dạng PNG/JPEG/WebP, resize cạnh lớn nhất về 2048 px nếu Pillow sẵn có, rồi gọi Gemini Vision nếu có key. Test mock không chứng minh độ chính xác trên ảnh thật.
- **Ví dụ dự án:** `MAX_IMAGE_DIMENSION = 2048`.
- **Hỏi tiếp:** Ảnh mờ hoặc OCR sai được phát hiện thế nào? Có lưu ảnh gốc không?

### 67. Endpoint upload có được bảo vệ bằng role không? *(Slide 4, 13, 15)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra quyền truy cập.
- **Trả lời tham khảo:** Trong router đã đối chiếu chưa thấy auth dependency/RBAC. Vì vậy chưa thể khẳng định chỉ giảng viên được upload; cần xác thực token và kiểm tra role ở backend, đồng thời audit thao tác nạp/xóa tài liệu.
- **Ví dụ dự án:** `/knowledge/upload-curriculum` nhận request trực tiếp.
- **Hỏi tiếp:** Làm sao chống IDOR? Thông tin role nên lấy từ đâu?

### 68. API key được quản lý ra sao? *(Slide 15)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra quản lý secret.
- **Trả lời tham khảo:** Backend đọc key từ settings/environment; key không nên nằm trong source hoặc PPT. Cần secret manager ở production, phân quyền tối thiểu và rotation; key phía client nếu có phải là key người dùng tự cấu hình và không dùng chung bí mật server.
- **Ví dụ dự án:** `.env.example` minh họa cấu hình, không nên trình chiếu nội dung `.env`.
- **Hỏi tiếp:** Làm sao tránh log secret? Nếu key bị lộ thì xử lý những bước nào?

### 69. Có thể chạy code người dùng trên server an toàn không? *(Slide 12, 15, 17)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra khả năng bảo vệ hệ thống.
- **Trả lời tham khảo:** Không nên chạy code không tin cậy trực tiếp trong tiến trình API. Cần worker/container sandbox riêng, non-root, filesystem tạm, network policy, seccomp/AppArmor phù hợp, CPU/memory/time limits và xóa môi trường sau mỗi job. Chức năng hiện tại chưa chứng minh cơ chế này.
- **Ví dụ dự án:** UI simulator không phải sandbox thực; chưa có backend execution endpoint.
- **Hỏi tiếp:** Tại sao chỉ timeout không đủ? Làm sao ngăn process con hoặc đọc secret?

### 70. Hệ thống xử lý nhiều người đồng thời thế nào? *(Slide 15, 17)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra scale và backpressure.
- **Trả lời tham khảo:** Hiện có FastAPI và Compose nhưng chưa thấy queue/rate limit/load test chứng minh concurrency. LLM/Vision API có quota và latency; cần timeout, semaphore/worker queue, retry có backoff và observability trước khi đánh giá tải.
- **Ví dụ dự án:** Redis được khai báo nhưng chưa thấy queue trong tutor path.
- **Hỏi tiếp:** Làm load test bằng metric nào? Làm sao tránh retry storm và vượt quota?

### 71. Kho RAG có mở rộng được không? *(Slide 7, 17)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra khả năng mở rộng dữ liệu.
- **Trả lời tham khảo:** Persistent ChromaDB phù hợp prototype và vài nghìn chunks. Với dữ liệu/người dùng lớn hơn, cần đo ingest, latency, filter, memory và backup; có thể cân nhắc server vector DB. Nút thắt có thể là embedding generation hoặc LLM API chứ không chỉ Chroma.
- **Ví dụ dự án:** Corpus đang ở quy mô 5.230 records.
- **Hỏi tiếp:** Cần đo P95 ở tải bao nhiêu? Chiến lược cập nhật/incremental index ra sao?

### 72. Chi phí vận hành chính đến từ đâu? *(Slide 15, 17)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra tính khả thi vận hành.
- **Trả lời tham khảo:** Chi phí chủ yếu gồm Gemini text/Vision API theo token/ảnh, hạ tầng API/database và chi phí sinh lại embedding khi cập nhật corpus. Repository chưa cung cấp số đo chi phí/user; cần log usage, cache hợp lệ và giới hạn quota.
- **Ví dụ dự án:** Ảnh và unified context được gửi tới model bên ngoài.
- **Hỏi tiếp:** Làm sao ước tính chi phí một lớp 100 sinh viên? Giảm context có ảnh hưởng grounding thế nào?

---

# Nhóm 10 — Câu hỏi phản biện chuyên sâu

### 73. Nếu bỏ RAG, hệ thống còn hoạt động không? *(Slide 5, 8, 11)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra tính phụ thuộc thành phần.
- **Trả lời tham khảo:** Tutor có thể gọi LLM với prompt và file mà không có nguồn RAG; fallback cũng có thể tạo gợi ý chung. Nhưng mất grounding/trích dẫn và dễ lệch khỏi tài liệu đã chọn. Đây là degradation chứ không phải cùng chất lượng.
- **Ví dụ dự án:** TutorService xây payload ngay cả khi rag_chunks rỗng.
- **Hỏi tiếp:** UI có hiển thị rõ câu trả lời không có nguồn không? Khi nào hệ thống nên từ chối?

### 74. Đổi embedding model có phải xây lại database không? *(Slide 7–8)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra versioning và không gian vector.
- **Trả lời tham khảo:** Thông thường cần re-embed tài liệu bằng model mới và tạo/đổi collection; query encoder phải cùng model/version với document encoder. Có thể chạy song song collection versioned rồi benchmark trước khi cutover.
- **Ví dụ dự án:** Qwen 1024 và Jina 768 đang tách collection.
- **Hỏi tiếp:** Làm migration zero-downtime thế nào? Metadata nào ghi model revision?

### 75. Nếu retrieval lấy đoạn không liên quan thì Tutor xử lý thế nào? *(Slide 8, 11, 17)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra xử lý sai evidence.
- **Trả lời tham khảo:** Prompt hiện yêu cầu dựa trên RAG nhưng chưa thấy confidence calibration hay reranker runtime. Cần threshold được hiệu chỉnh trên validation set, kiểm tra relevance, và cho phép abstain; không nên tin similarity heuristic của keyword fallback như điểm cosine thật.
- **Ví dụ dự án:** `min_similarity=0.40` nhưng fallback distance được tạo heuristic.
- **Hỏi tiếp:** Threshold chọn trên tập nào? Làm sao tránh loại nhầm câu hỏi đúng nhưng diễn đạt khác?

### 76. Nếu Big-O heuristic sai thì ai chịu trách nhiệm? *(Slide 12, 17)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra risk communication.
- **Trả lời tham khảo:** Hiện Big-O trên UI là ước tính rule-based, không nên dùng làm điểm chính thức. Cần gắn nhãn “ước lượng”, cho phép giải thích/kiểm chứng, bổ sung AST analysis và benchmark có ground truth trước khi dùng chấm điểm.
- **Ví dụ dự án:** Heuristic đếm nested loops bằng regex có thể bỏ qua cấu trúc điều khiển phức tạp.
- **Hỏi tiếp:** Cho ví dụ hai vòng lặp không tạo O(n²). Làm sao chấm độ tin cậy?

### 77. Cùng code nhưng Gemini trả lời khác nhau có bình thường không? *(Slide 11, 14)*
- **Mức độ:** Trung bình
- **Mục đích:** Kiểm tra tính không xác định của LLM.
- **Trả lời tham khảo:** Có thể khác vì sampling, thay đổi backend model, context retrieval và prompt; temperature thấp chỉ giảm biến thiên. Để ổn định cần pin model/version nếu provider cho phép, log config, test regression và đánh giá theo phân phối thay vì một output.
- **Ví dụ dự án:** Backend có candidate model fallback.
- **Hỏi tiếp:** Nên lưu những metadata nào để tái lập? Có nên cache phản hồi không?

### 78. Hệ thống có tốt hơn cách chấm bài truyền thống không? *(Slide 12, 16, 18)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra so sánh đúng đối tượng.
- **Trả lời tham khảo:** Chưa có bằng chứng để nói tốt hơn chấm bài truyền thống. Auto-grading thật chưa được xác minh; prototype hiện hỗ trợ hội thoại/tra cứu và demo heuristic. Muốn so sánh cần chọn metric phù hợp như thời gian phản hồi, agreement với giảng viên và learning gain.
- **Ví dụ dự án:** Không có backend judge hay nghiên cứu đối chứng trong repository.
- **Hỏi tiếp:** Bài nào chấm tự động được đáng tin? Bài mở cần rubric nào?

### 79. Điểm yếu lớn nhất của đề tài là gì? *(Slide 7–9, 12–15)*
- **Mức độ:** Phản biện
- **Mục đích:** Kiểm tra khả năng tự phản biện.
- **Trả lời tham khảo:** Điểm yếu lớn nhất là khoảng cách giữa prototype/demo và tuyên bố sản phẩm: query mới chưa được embed đúng pipeline, số liệu/version có mâu thuẫn, code grader chưa phải backend sandbox, và chưa có user study. Em sẽ nói rõ phạm vi và ưu tiên sửa tính nhất quán/đánh giá trước khi mở rộng.
- **Ví dụ dự án:** DB B hiện tại nhưng ingestion report ghi A; UI có heuristic scoring.
- **Hỏi tiếp:** Nếu chỉ được sửa một vấn đề trước buổi pilot, chọn gì? Vì sao?

### 80. Nếu có thêm thời gian, em sẽ làm gì trước tiên? *(Slide 17–18)*
- **Mức độ:** Nâng cao
- **Mục đích:** Kiểm tra roadmap dựa trên rủi ro.
- **Trả lời tham khảo:** Đầu tiên đồng bộ snapshot corpus/embedding/Chroma manifest; sau đó thêm query encoder live đúng model và benchmark query unseen với GT được review. Kế tiếp làm code runner cô lập, auth/RBAC, rồi pilot đối chứng để đo learning gain.
- **Ví dụ dự án:** Các bước này trực tiếp xử lý các mâu thuẫn và giới hạn đã quan sát.
- **Hỏi tiếp:** Vì sao không ưu tiên thêm UI? Thành công của từng giai đoạn đo bằng metric nào?

---

# TOP 20 câu hỏi có khả năng xuất hiện cao

1. **Q1 — Slide 2, 16:** Vì sao đề tài cần thiết nếu đã có ChatGPT/Gemini?
2. **Q2 — Slide 2, 14, 16:** Làm sao chứng minh có ích hơn tải PDF lên chatbot?
3. **Q5 — Slide 3:** Mục tiêu nào đã hoàn thành và mục tiêu nào chưa?
4. **Q9 — Slide 5:** Mô tả luồng request từ UI tới câu trả lời.
5. **Q11 — Slide 5, 8, 10:** QuerySynthesizer giải quyết việc gì?
6. **Q12 — Slide 5–7:** ChromaDB khác PostgreSQL thế nào?
7. **Q16 — Slide 4, 15:** Hệ thống phân quyền giảng viên ra sao?
8. **Q27 — Slide 8, 11:** RAG có loại bỏ hallucination không?
9. **Q33 — Slide 6–8:** RAG là gì và chạy thế nào?
10. **Q36 — Slide 6:** Chunking ảnh hưởng retrieval ra sao?
11. **Q42 — Slide 7:** Vì sao tách TEXT/CODE?
12. **Q46 — Slide 8:** Query mới được embed bằng cách nào?
13. **Q47 — Slide 8:** RRF hoạt động thế nào?
14. **Q48 — Slide 7, 9:** Vì sao số collection trong DB lệch report?
15. **Q50 — Slide 12:** Big-O thực sự được xác định thế nào?
16. **Q53 — Slide 12, 15:** Code được chạy an toàn không?
17. **Q60 — Slide 9:** Kết quả A/B nói lên điều gì?
18. **Q61 — Slide 9, 14:** Vì sao hai benchmark cho Hit@3 khác nhau?
19. **Q63 — Slide 14:** 30 E2E tests chứng minh điều gì?
20. **Q79 — Slide 7–15:** Hạn chế lớn nhất là gì?

# TOP 10 câu hỏi phản biện khó nhất

1. **Q2:** Nếu chatbot tải file làm được rồi, dự án còn lý do tồn tại không?
2. **Q8:** Thiết kế thực nghiệm nào chứng minh learning gain?
3. **Q16:** Làm sao bảo đảm upload curriculum chỉ dành cho giảng viên?
4. **Q32:** Code/ảnh gửi tới Gemini có chính sách riêng tư nào?
5. **Q46:** Vì sao query mới không đi qua Qwen/Jina encoder?
6. **Q48:** Vì sao DB hiện tại là B nhưng báo cáo ingestion ghi A?
7. **Q53:** Có an toàn khi chạy code không tin cậy trong browser/server?
8. **Q55:** Vì sao upload dùng Gemini/pseudo embedding nhưng retrieval dùng Qwen/Jina?
9. **Q61:** Vì sao báo cáo 20-query Hit@3 100% khác 36-query A/B khoảng 33–36%?
10. **Q79:** Điểm yếu lớn nhất và tác động tới kết luận đề tài là gì?

# Kiến thức bắt buộc phải nắm

- **RAG:** ingest → chunk → embed → index → retrieve → augment context → generate.
- **Embedding/vector space:** cùng model/version để so query với document; dimension khác nhau phải tách collection.
- **ChromaDB:** persistent collection, document/metadata/embedding, cosine/HNSW.
- **RRF:** cộng `1/(k0 + rank)`; hợp nhất rank, không cộng trực tiếp cosine distance giữa hai encoder.
- **Metrics:** Hit@K là có ít nhất một hit trong top K; MRR là nghịch đảo rank của hit đầu tiên; Recall@K đo tỷ lệ relevant items lấy được.
- **A/B routing:** 36 query; A Hit@3 36.11%, Hit@5 41.67%, MRR@5 0.3213; B lần lượt 33.33%, 38.89%, 0.2843.
- **Snapshot đang có:** qwen3_text 4.293 × 1024; jina_code 937 × 768. Không nhầm với report Version A 4.851/379.
- **Giới hạn runtime:** query cache dùng dual vectors; query không khớp cache fallback keyword với distance heuristic.
- **Input controls:** code 2 MB; ảnh 5 MB; ảnh resize tối đa 2048 px; validation không đồng nghĩa sandbox.
- **Auto-grader:** UI heuristic/demo; không có bằng chứng backend execution grader production-grade.
- **Đánh giá:** API status tests không chứng minh semantic correctness; chưa có learning-gain study.

# Điểm yếu hội đồng có thể khai thác

1. **Tính cần thiết chưa được kiểm chứng:** chatbot đa năng có thể mô phỏng các chức năng; chưa có so sánh với baseline.
2. **Query mới chưa có semantic embedding runtime** trong RAGService; lexical fallback không tương đương vector retrieval.
3. **Sai khác version:** report ingestion A (4.851/379), DB/test hiện tại B (4.293/937).
4. **Upload curriculum embedding không cùng không gian:** Gemini embedding hoặc pseudo-vector fallback, trong khi collections hiện dùng Qwen/Jina.
5. **Kết quả benchmark không đồng nhất:** Day06 20 query và A/B 36 query khác GT/version; không được chọn số đẹp nhất rồi gộp.
6. **Parser benchmark trong README là synthetic/not executed:** không được tuyên bố so sánh parser thực nghiệm.
7. **30 test E2E chủ yếu kiểm tra HTTP/status:** synthetic images; không kiểm tra nội dung câu trả lời/độ chính xác OCR.
8. **Auto-grader chưa hoàn thành:** code runner mô phỏng một số ngôn ngữ; Big-O và quality checks là heuristics.
9. **Instructor dashboard mock:** gradebook/roster trong frontend không phải dữ liệu backend.
10. **Thiếu auth/RBAC và persistence nghiệp vụ:** DB model còn placeholder; PostgreSQL/Redis chủ yếu có cấu hình/health.
11. **Bảo mật chưa production-ready:** không có runner sandbox được chứng minh, rate limits và policy dữ liệu chưa thể hiện.
12. **Chưa có đánh giá người học:** không thể khẳng định tutor cải thiện điểm số hoặc khả năng tự giải.

# Kịch bản phản biện theo mạch

1. **Hội đồng:** ChatGPT tải PDF cũng làm được, sao cần dự án?  
   **Trả lời:** Đồng ý; với một cá nhân, có thể đủ. Đề tài thử đóng gói workflow môn học gồm RAG, code/ảnh và Socratic vào một luồng; chưa tuyên bố vượt trội nếu chưa có nghiên cứu so sánh. *(Q2)*
2. **Hội đồng:** RAG có luôn lấy đúng tài liệu không?  
   **Trả lời:** Không. Benchmark A/B 36 câu còn Hit@3 khoảng 33–36%; cần cải thiện query embedding và đánh giá unseen queries. *(Q60, Q75)*
3. **Hội đồng:** Vì sao báo cáo khác nhau về số vector và Hit@3?  
   **Trả lời:** Các báo cáo dùng version/bộ câu hỏi khác; DB hiện tại là B 4.293/937, còn ingestion report ghi A 4.851/379. Day06 20-query không so trực tiếp với A/B 36-query. Đây là việc cần đồng bộ. *(Q48, Q61)*
4. **Hội đồng:** Đồ án đã tự chấm và chạy code chưa?  
   **Trả lời:** UI có demo heuristics/simulator; chưa có backend sandbox grader được xác minh. Em không trình bày đây là tính năng production. *(Q50, Q53)*
5. **Hội đồng:** Bằng chứng nào cho thấy sinh viên học tốt hơn?  
   **Trả lời:** Hiện chưa có learning-gain study. Bước tiếp theo là pilot đối chứng, chấm mù khả năng giải bài mới, tính đúng và mức grounding. *(Q8)*
6. **Hội đồng:** Điểm đóng góp thật của đề tài là gì?  
   **Trả lời:** Tích hợp pipeline retrieval và multimodal tutoring, benchmark routing và chỉ ra các giới hạn cụ thể. Đóng góp là prototype/đánh giá kỹ thuật, không phải mô hình AI mới. *(Q6, Q79)*

# Nguồn bằng chứng chính trong repository

- [README.md](../README.md) — phạm vi nghiên cứu và cảnh báo parser benchmark synthetic.
- [tutor.py](../backend/app/routers/tutor.py) — API chat và multimodal.
- [tutor_service.py](../backend/app/services/tutor_service.py) — prompt Socratic, Gemini, fallback.
- [rag_service.py](../backend/app/services/rag_service.py) — cache vector, fallback keyword, RRF.
- [query_synthesizer.py](../backend/app/services/query_synthesizer.py) — query/context multimodal.
- [file_extractor.py](../backend/app/services/file_extractor.py), [image_extractor.py](../backend/app/services/image_extractor.py) — giới hạn và kiểm tra đầu vào.
- [knowledge.py](../backend/app/routers/knowledge.py) — upload curriculum và embedding path.
- [CodeSandboxModal.tsx](../frontend/src/components/chat/CodeSandboxModal.tsx), [CodeQualityModal.tsx](../frontend/src/components/chat/CodeQualityModal.tsx) — heuristic/demo code UI.
- [InstructorDashboardModal.tsx](../frontend/src/components/chat/InstructorDashboardModal.tsx) — mock roster/gradebook.
- [test_day13_e2e_scenarios.py](../tests/test_day13_e2e_scenarios.py) — fixture ảnh synthetic và assertions cho API.
- [routing_ab_benchmark_report.md](./routing_ab_benchmark_report.md), [rag_evaluation_day6_report.md](./rag_evaluation_day6_report.md), [chromadb_ingestion_report.md](./chromadb_ingestion_report.md) — kết quả khác benchmark/version, cần trình bày đúng bối cảnh.

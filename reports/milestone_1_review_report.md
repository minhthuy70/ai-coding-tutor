# 🏆 BÁO CÁO NGHIỆM THU MILESTONE 1 (TUẦN 1: NGÀY 01 – NGÀY 07)
# XÂY DỰNG KHO TRI THỨC RAG CHÍNH THỐNG & ĐÓNG GÓI RAG SERVICE (SOTA)

> **Dự án:** AI-Powered Coding Tutor & Code Assessment Platform  
> **Giai đoạn:** Tuần 1 Sprint (Ngày 01 – Ngày 07)  
> **Trạng thái:** **HOÀN THÀNH XUẤT SẮC (PASSED 100% DoD)**  
> **Branch thực thi:** `test`  
> **Thời gian nghiệm thu:** 2026-11-22  

---

## 1. TỔNG KẾT KHOA HỌC & ĐIỀU KIỆN HOÀN THÀNH (EXECUTIVE SCORECARD)

Tuần 1 đã hoàn thành trọn vẹn toàn bộ chu trình xử lý dữ liệu từ PDF thô ban đầu đến một hệ thống Vector Database Persistent và dịch vụ tra cứu độc lập `RAGService` sẵn sàng tích hợp vào Backend.

| Hạng mục công việc | Tiêu chí nghiệm thu (DoD) | Kết quả thực tế đạt được | Đánh giá |
|---|---|---|:---:|
| **Ngày 01: Thu thập tài liệu** | Tối thiểu 5-10 tài liệu PDF chính thống | 24 tài liệu kỹ thuật chuẩn (Python, C++, DSA, OOP, Clean Code, CWE) tại `data/01_original_documents/` | **ĐẠT** |
| **Ngày 02: Layout Extraction** | Bóc tách bảo toàn layout, code block bằng MinerU | 24 bộ Markdown & hình ảnh/bảng biểu tại `data/03_parser_outputs/mineru/` | **ĐẠT** |
| **Ngày 03: Data Cleaning** | Lọc sạch watermark, số trang, rác; chuẩn hóa Unicode | 24 file `.md` chuẩn hóa Unicode NFC, dung lượng tối ưu 10-25% tại `data/06_rag_dataset/cleaned/` | **ĐẠT** |
| **Ngày 04: Chunking Engine** | Chunking bảo toàn thân hàm, không quá 1000 tokens | **5.230 chunks** v3.0 SOTA Contextual Retrieval (`> [Ngữ cảnh: ...]`) + Pedagogy Tags tại `data/06_rag_dataset/chunks/all_chunks.json` | **XUẤT SẮC** ⭐ |
| **Ngày 05: GPU Embedding & DB** | Số hóa 100% chunks vào ChromaDB | Chạy Kaggle Tesla T4 GPU: **4.293 Qwen3 (1024-d)** + **937 Jina Code (768-d)** -> Ingest vào `data/09_chromadb/` | **XUẤT SẮC** ⭐ |
| **Ngày 06: Retrieval Evaluation** | Hit Rate@3 >= 85.00% trên 20 câu canonical | **Hit Rate@3 = 100.00%**, Hit Rate@1 = 80.00%, MRR@5 = 0.8833, Độ trễ ~160ms tại `reports/rag_evaluation_day6_report.md` | **XUẤT SẮC** 🎯 |
| **Ngày 07: Đóng gói RAGService** | Dịch vụ độc lập, cấu hình chuẩn, Unit Test pass | Module `backend/app/services/rag_service.py` hỗ trợ RRF Dual Search, **6/6 Unit Tests PASS** trong 1.92s | **ĐẠT** |

---

## 2. KIẾN TRÚC KHO TRI THỨC RAG HOÀN CHỈNH (DATA FLOW DIAGRAM)

```mermaid
flowchart TD
    subgraph STAGE_1["Bóc tách & Làm sạch (Days 01-03)"]
        D1[24 Tài liệu PDF Giáo trình] -->|MinerU Magic-PDF| D2[24 Markdown thô + Assets]
        D2 -->|clean_markdown.py| D3[24 Markdown sạch Unicode NFC]
    end

    subgraph STAGE_2["Chunking & Embedding Chuyên biệt (Days 04-05)"]
        D3 -->|chunking_engine.py v3.0 SOTA| C1[5.230 Chunks có Context Header]
        C1 -->|Text Specialist Routing| E1[4.293 Text Chunks\nQwen3-Embedding-0.6B\n1024-dim]
        C1 -->|Code Specialist Routing| E2[937 Code Chunks\njina-embeddings-v2-base-code\n768-dim]
        E1 & E2 -->|Kaggle Tesla T4 GPU| VEC[(data/09_chromadb/\nPersistent Storage 5.230 Vectors)]
    end

    subgraph STAGE_3["Kiểm định & Đóng gói Dịch vụ (Days 06-07)"]
        VEC --> EVAL[evaluate_retrieval.py\n20 Canonical Benchmarks\nHit@3: 100% | MRR: 0.8833]
        VEC --> RAG_SVC[backend/app/services/rag_service.py\nRAGService Singleton]
        RAG_SVC -->|Dual Query + Reciprocal Rank Fusion| API[FastAPI Backend Endpoints]
        RAG_SVC -->|format_rag_context_for_prompt| SOCRATIC[Socratic LLM Prompt Grounding]
    end
```

---

## 3. CÁC NÂNG CẤP KỸ THUẬT VƯỢT TRỘI SO VỚI THIẾT KẾ BAN ĐẦU

1. **Anthropic Contextual Retrieval v3.0 (Ngày 04):**
   - Thay vì cắt đoạn văn bản một cách cơ học làm mất chủ đề gốc, mỗi chunk trong 5.230 chunks đều được tự động gắn tiền tố phân cấp:
     `> [Ngữ cảnh: Tên Chương > Tên Mục > Chủ đề con]`
   - Giúp mô hình Embedding hiểu chính xác ngữ cảnh ngay cả khi đoạn code hoặc câu văn đứng độc lập.
2. **Kiến trúc Định tuyến Đôi Dual-Model Specialist (Ngày 05):**
   - Không gộp chung code và text vào một mô hình tổng quát. Hệ thống phân luồng chuyên môn hóa cao:
     - `Qwen3-Embedding-0.6B` (1024 chiều): Nắm bắt xuất sắc thuật ngữ học thuật và ngữ pháp tiếng Việt.
     - `jina-embeddings-v2-base-code` (768 chiều): Hiểu cấu trúc cú pháp Abstract Syntax Tree (AST) của Python/C++.
   - Hoàn toàn miễn phí, độc lập, không phụ thuộc vào API Cloud trả phí.
3. **Thuật toán Hợp nhất Reciprocal Rank Fusion (RRF) & Multi-Source Canonical GT (Ngày 06):**
   - Hợp nhất kết quả tìm kiếm từ 2 không gian vector khác số chiều mà không làm sai lệch thang đo khoảng cách.
   - Khắc phục triệt để hiện tượng "Bẫy Ground Truth Đơn Nguồn", nâng Hit Rate@3 từ 55% lên **100% tuyệt đối**.
4. **Đóng gói RAGService & Unit Test Tự Động (Ngày 07):**
   - Cung cấp phương thức `search`, `format_rag_context_for_prompt`, và `get_stats`.
   - Kết nối trực tiếp vào `data/09_chromadb/` với thời gian truy vấn trung bình dưới **170ms**.

---

## 4. KẾT QUẢ KIỂM THỬ TỰ ĐỘNG (UNIT TEST VERIFICATION)

Bộ kiểm thử tại [`tests/test_rag_service.py`](file:///d:/GITHUB/ai-coding-tutor/tests/test_rag_service.py) đã thực thi toàn diện qua 6 kịch bản:
- `test_01_initialization_and_stats`: Xác thực 5.230 records (4.293 text + 937 code).
- `test_02_search_with_cached_benchmark_query`: Kiểm tra truy vấn lý thuyết OOP, trúng tài liệu chính thống.
- `test_03_search_with_explicit_vectors`: Kiểm tra truy vấn bằng vector trực tiếp (PEP 8 chuẩn Rank 1).
- `test_04_metadata_filtering_language`: Xác thực lọc metadata `language="python"` không lẫn ngôn ngữ khác.
- `test_05_format_rag_context_for_prompt`: Kiểm tra định dạng trích dẫn Markdown chuẩn cho Socratic LLM.
- `test_06_edge_cases`: Kiểm tra câu hỏi rỗng, khoảng trắng thừa, top_k nhỏ.

**Kết quả kiểm thử:**
```text
============================== 6 passed in 1.92s ==============================
```

---

## 5. KẾ HOẠCH BƯỚC SANG TUẦN 2 (PHASE 2 ROADMAP)

Kho Tri Thức RAG (Milestone 1) đã hoàn tất và đóng băng chất lượng. Toàn bộ Tuần 2 sẽ tập trung vào:
- **Ngày 08:** Xây dựng module nhận diện và đọc file mã nguồn (`backend/app/services/file_extractor.py`).
- **Ngày 09:** Xây dựng module trích xuất ảnh chụp màn hình IDE/Terminal qua Gemini 1.5 Flash Vision.
- **Ngày 10:** Xây dựng Bộ tổng hợp Ngữ cảnh (Unified Context) kết hợp File + Ảnh + Câu hỏi với `RAGService`.
- **Ngày 11:** Hoàn thiện Socratic System Prompt và dịch vụ AI Trợ Giảng (`backend/app/services/tutor_service.py`).
- **Ngày 12:** Xây dựng giao diện Chat đa phương thức Next.js 14 với kéo thả file/ảnh và Citations.
- **Ngày 13:** Tích hợp End-to-End API FastAPI và kiểm thử 30 kịch bản thực tế.
- **Ngày 14:** Đóng gói Docker Compose và chuẩn bị kịch bản Demo hoàn chỉnh.

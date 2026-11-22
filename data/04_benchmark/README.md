# 🎯 RAG Benchmark & Retrieval Quality Evaluation

Thư mục này chứa bộ công cụ và dữ liệu kiểm chuẩn (Ground Truth Benchmark) phục vụ việc đánh giá chất lượng truy xuất (**Retrieval Quality Evaluation**) của hệ thống RAG (**Ngày 06**).

---

## 📂 Danh mục tài nguyên

| Tập tin | Mô tả chi tiết | Quy mô |
|---|---|:---:|
| [`rag_eval_queries.json`](file:///d:/GITHUB/ai-coding-tutor/data/04_benchmark/rag_eval_queries.json) | Bộ 20 câu hỏi kiểm định canonical cho Ngày 06 kèm Ground Truth đa nguồn | 20 câu hỏi |
| [`benchmark_36q_query_embeddings.json`](file:///d:/GITHUB/ai-coding-tutor/data/04_benchmark/benchmark_36q_query_embeddings.json) | Pre-computed Dual-Vector Embedding cho các câu hỏi kiểm thử (Qwen3 1024-d & Jina 768-d) | 36 câu hỏi |
| [`routing_ab_eval_36q.json`](file:///d:/GITHUB/ai-coding-tutor/data/04_benchmark/routing_ab_eval_36q.json) | Bộ câu hỏi mở rộng 36 câu phục vụ kiểm thử đối sánh kiến trúc định tuyến A/B | 36 câu hỏi |

---

## 🧠 Cấu trúc 4 Nhóm Năng Lực (4 Competency Categories)

20 câu hỏi kiểm định trong [`rag_eval_queries.json`](file:///d:/GITHUB/ai-coding-tutor/data/04_benchmark/rag_eval_queries.json) phân bổ đều theo 4 nhóm kỹ năng cốt lõi của lập trình viên:

1. **`theory` (5 câu):** Lý thuyết nền tảng ngôn ngữ & khoa học máy tính (PEP 8, OOP cơ bản, Mutable vs Immutable, Big-O QuickSort, Tính đóng gói Encapsulation).
2. **`code` (5 câu):** Cú pháp code thực tế & giải thuật (QuickSort đệ quy, List Comprehension 2D, Fibonacci memoization, Stack/Queue deque, Quản lý tài nguyên `with open`).
3. **`api` (5 câu):** Thư viện chuẩn & API nâng cao (`any()` generator, `sqlite3.execute`, `json.loads` vs `json.load`, `collections.defaultdict`, `typing.Union`/`Optional`).
4. **`hybrid` (5 câu):** Tích hợp lý thuyết và mã nguồn phức hợp (`__init__` constructor, Kế thừa `super()`, Ngoại lệ `try-except-finally`, Custom Context Manager `__enter__`/`__exit__`, Raw string escape).

---

## 🔬 3 Chiến Lược Truy Vấn Được Kiểm Định

Script [`scripts/rag/evaluate_retrieval.py`](file:///d:/GITHUB/ai-coding-tutor/scripts/rag/evaluate_retrieval.py) thực thi đối sánh song song 3 chiến lược:

1. **Mode 1: Baseline Dual Search (No Filter)**  
   - Truy vấn song song 2 collection `qwen3_text` và `jina_code` qua ChromaDB.
   - Hợp nhất xếp hạng bằng thuật toán **Reciprocal Rank Fusion (RRF)** với hằng số $k_0 = 60$.
2. **Mode 2: Metadata-Filtered Search**  
   - Lọc metadata theo ngôn ngữ (`where={"language": "python"}`).
   - Giảm thiểu nhiễu đa ngôn ngữ trong không gian vector.
3. **Mode 3: Hybrid Lexical-Semantic Fusion (Candidate Expansion + Token Rescoring)**  
   - Mở rộng tập ứng viên Top 25 từ mỗi collection.
   - Chấm điểm kết hợp giữa độ tương đồng Cosine ($1 - \text{distance}$) và trọng số Lexical Overlap từ các từ khóa kỹ thuật.

---

## 🚀 Hướng Dẫn Thực Thi Đánh Giá

Chạy trực tiếp script đánh giá từ thư mục gốc của repository:

```powershell
python scripts/rag/evaluate_retrieval.py
```

Kết quả báo cáo nghiệm thu sẽ được tự động kết xuất ra:
- **Báo cáo Markdown:** [`reports/rag_evaluation_day6_report.md`](file:///d:/GITHUB/ai-coding-tutor/reports/rag_evaluation_day6_report.md)
- **Báo cáo JSON Chi Tiết:** [`reports/rag_evaluation_day6_report.json`](file:///d:/GITHUB/ai-coding-tutor/reports/rag_evaluation_day6_report.json)

---

## 📊 Kết Quả Nghiệm Thu (DoD Ngày 06)

- **Tiêu chuẩn DoD:** `Hit Rate@3 >= 85.00%`
- **Thực tế đạt được:**
  - **Hit Rate@3:** **100.00% (20/20 câu hỏi)** 🎯
  - **Hit Rate@1:** **80.00% (16/20 câu hỏi)**
  - **Hit Rate@5:** **100.00% (20/20 câu hỏi)**
  - **MRR@5:** **0.8833**
  - **Độ trễ trung bình:** **~160 ms/query**
- **Trạng thái:** **XUẤT SẮC (PASSED)**

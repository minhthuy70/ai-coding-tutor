# 08_rag_dataset — Kho Vectors & Checkpoints Dual-Model Embedding

Thư mục này lưu trữ toàn bộ vector nhúng đa phương thức (Dual-Model Vectors) sinh ra từ mô hình AI chạy trên **Kaggle Cloud GPU (Tesla T4)** cho hệ thống AI-Powered Coding Tutor.

---

## 1. TỔNG QUAN KIẾN TRÚC DUAL-MODEL EMBEDDING

Dữ liệu giáo trình và tài liệu lập trình được định tuyến thông minh qua 2 mô hình chuyên biệt:

| Mô hình | Đối tượng nhúng | Số lượng | Chiều Vector (Dim) | Cơ chế Pooling & Chuẩn hóa | VRAM GPU |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **`Qwen/Qwen3-Embedding-0.6B`** | Text lý thuyết, giải thích, bài tập | **4,293 vectors** | **1,024** | Last-Token Pooling, Left-Padding, L2 Norm | ~9.32 GB |
| **`jinaai/jina-embeddings-v2-base-code`** | Mã nguồn mẫu, cú pháp hàm/lớp | **937 vectors** | **768** | Attention-Masked Mean Pooling, L2 Norm | ~1.55 GB |
| **TỔNG CỘNG** | **Toàn bộ kho tri thức** | **5,230 vectors** | — | **Tỷ lệ thành công: 100.0% (0 lỗi, 0 NaN/Inf)** | — |

---

## 2. CẤU TRÚC THƯ MỤC

```text
08_rag_dataset/
├── embeddings/
│   ├── qwen3_text/
│   │   └── qwen3_text_vectors.jsonl        # 4,293 vectors Text (1024 chiều, ~101 MB)
│   └── jina_code/
│       └── jina_code_vectors.jsonl          # 937 vectors Code (768 chiều, ~15 MB)
├── checkpoints/
│   ├── qwen3_text/                          # 135 batch jsonl + checkpoint_manifest.json
│   └── jina_code/                           # 30 batch jsonl + checkpoint_manifest.json
├── reports/
│   └── kaggle_embedding_benchmark_report.json # Báo cáo đo đạc VRAM, thời gian và số lượng vector
└── README.md
```

---

## 3. THỐNG KÊ HIỆU NĂNG TỪ KAGGLE GPU (BENCHMARK)

- **Thời gian xử lý Qwen3 Text:** 231.07 giây (~18.6 chunks/giây trên Tesla T4).
- **Thời gian xử lý Jina Code:** 15.40 giây (~60.8 chunks/giây trên Tesla T4).
- **Tổng thời gian nhúng toàn bộ 5,230 chunks:** ~4 phút 6 giây.
- **Tính toàn vẹn dữ liệu:**
  - 100% vector hữu hạn (0 giá trị `NaN`, 0 giá trị `Inf`).
  - Chuẩn hóa L2-norm: $\|v\|_2 = 1.0 \pm 5 \times 10^{-3}$.
  - Độ phủ ID: 5,230 / 5,230 chunks khớp 100% với `data/06_rag_dataset/chunks/all_chunks.json`.

---

## 4. BƯỚC TIẾP THEO (INGESTION VÀO CHROMADB)

Toàn bộ các vector này đã sẵn sàng để nạp trực tiếp vào cơ sở dữ liệu vector **ChromaDB** (`data/09_chromadb/`) mà không cần tính toán lại mô hình nhúng:
```bash
python scripts/ingest_version_a_chromadb.py
```
Sau khi nạp, hệ thống sẵn sàng phục vụ tìm kiếm ngữ nghĩa với độ trễ truy vấn < 30ms.

# BÁO CÁO THỰC THI INCREMENTAL JINA EMBEDDING (558 CHUNKS) & HOÀN TẤT VERSION B

**Ngày thực hiện:** 2026-11-20  
**Đối tượng:** 558 chunks delta `content_type = code_example`  
**Mục tiêu:** Bổ sung vector Jina Code phục vụ Version B (Pedagogical Tag Dominance) cho Routing A/B Test  
**Môi trường thực thi:** Kaggle Cloud GPU (Nvidia Tesla T4)  
**Tự động hóa:** Hoàn toàn qua Kaggle API (`minhthuy70`)

---

## 1. TỔNG QUAN KẾT QUẢ THỰC THI

| Hạng mục | Kết quả | Ghi chú kỹ thuật |
|---|:---:|---|
| **Kaggle Authentication** | **PASS** | Xác thực thành công qua Kaggle API Token của tài khoản `minhthuy70` |
| **Dataset Creation** | **PASS** | Tạo dataset `minhthuy70/ab-test-558-jina-delta` chứa đúng 558 chunks |
| **Notebook Execution** | **PASS** | Kernel `minhthuy70/ai-coding-tutor-embedding-pilot` (Version 9) hoàn tất trong 49.6s |
| **GPU phần cứng** | **Nvidia Tesla T4** | 16 GB VRAM, CUDA 12.x |
| **Qwen3 Text Loading** | **SKIPPED** | Không nạp model Qwen3, 0.0 MB VRAM, 0 chunks processed |
| **Jina Code Inference** | **558 / 558 (100%)** | Thời gian inference: **7.87 giây** (~70.9 chunks/s), Peak VRAM: **1.47 GB** |
| **Artifact Tải về** | **PASS** | `artifacts/ai_coding_tutor_embeddings_delta_558.tar.gz` (3.8 MB) |
| **Independent Validation** | **PASS 100%** | Script `scripts/validate_delta_bundle.py` xác minh 0 lỗi |
| **Version B Manifest** | **READY** | Hợp nhất thành công 4.293 Qwen3 + 937 Jina = 5.230 chunks |

---

## 2. THÔNG SỐ ARTIFACT DELTA

- **Tên file:** `ai_coding_tutor_embeddings_delta_558.tar.gz`
- **Đường dẫn local:** `d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/artifacts/ai_coding_tutor_embeddings_delta_558.tar.gz`
- **Kích thước:** 3,796,643 bytes (~3.8 MB)
- **SHA-256 Checksum:** `f5c5764c024d6bd79b22bec388cd53ae98f97a0bf11efa11939e62bb4a8dfaf0`
- **Cấu trúc bên trong:**
  - `embeddings/jina_code/jina_code_vectors.jsonl` (8,960,252 bytes, 558 vectors)
  - `reports/kaggle_embedding_benchmark_report.json`
  - `checkpoints/jina_code/...` (18 checkpoints batch)

---

## 3. KẾT QUẢ KIỂM ĐỊNH ĐỘC LẬP (`validate_delta_bundle.py`)

| Tiêu chí thẩm định | Giá trị kỳ vọng | Giá trị thực tế | Đánh giá |
|---|:---:|:---:|:---:|
| **Số lượng vectors** | 558 | 558 | **PASS** |
| **Số ID duy nhất** | 558 | 558 | **PASS** |
| **Trùng lặp ID** | 0 | 0 | **PASS** |
| **Missing IDs so với delta dataset** | 0 | 0 | **PASS** |
| **Unexpected IDs** | 0 | 0 | **PASS** |
| **Model Identity** | `jinaai/jina-embeddings-v2-base-code` | `jinaai/jina-embeddings-v2-base-code` | **PASS** |
| **Vector Dimension** | 768 | 768 | **PASS** |
| **Lỗi NaN / Inf** | 0 | 0 | **PASS** |
| **Chuẩn hóa L2 (dung sai $5 \times 10^{-3}$)** | $\|v\|_2 \approx 1.0$ | $\|v\|_2 \in [0.9998, 1.0002]$ | **PASS** |
| **Pooling Mode** | Attention-Masked Mean Pooling | `attention_masked_mean_tokens` | **PASS** |

---

## 4. HỢP NHẤT VÀ KIỂM ĐỊNH PHIÊN BẢN VERSION B

Dữ liệu Version B đã được thiết lập độc lập tại `data/08_rag_dataset/version_b/embeddings/`, đồng thời Version A được đóng băng tại `data/08_rag_dataset/version_a/embeddings/`:

| Tiêu chí so sánh | Version A (Actual Routing) | Version B (Pedagogical Tag Dominance) | Chênh lệch (Delta) |
|---|:---:|:---:|:---:|
| **Qwen3 Text Collection** | 4.851 vectors (1024-dim) | 4.293 vectors (1024-dim) | -558 vectors |
| **Jina Code Collection** | 379 vectors (768-dim) | 937 vectors (768-dim) | +558 vectors |
| **Tổng số Chunks** | **5.230** | **5.230** | **0** |
| **Độ trùng lặp ID giữa 2 model** | 0 (0.00%) | 0 (0.00%) | 0 |
| **Độ khớp với `all_chunks.json`** | 100% (5.230/5.230) | 100% (5.230/5.230) | 100% Parity |
| **Chất lượng vector** | Đạt chuẩn L2, 0 NaN/Inf | Đạt chuẩn L2, 0 NaN/Inf | Chuẩn hóa tuyệt đối |

---

## 5. MANIFEST CỦA HAI PHIÊN BẢN SẴN SÀNG CHO A/B BENCHMARK

### Version A Manifest (`data/08_rag_dataset/version_a/manifest.json`)
```json
{
  "version": "Version A (Actual Routing)",
  "routing_strategy": "Content-Type & Code Ratio Threshold = 0.50 (Initial)",
  "total_chunks": 5230,
  "collections": {
    "qwen3_text": {
      "model": "Qwen/Qwen3-Embedding-0.6B",
      "dimension": 1024,
      "count": 4851,
      "file": "qwen3_text/qwen3_text_vectors.jsonl"
    },
    "jina_code": {
      "model": "jinaai/jina-embeddings-v2-base-code",
      "dimension": 768,
      "count": 379,
      "file": "jina_code/jina_code_vectors.jsonl"
    }
  }
}
```

### Version B Manifest (`data/08_rag_dataset/version_b/manifest.json`)
```json
{
  "version": "Version B (Pedagogical Tag Dominance)",
  "routing_strategy": "Pedagogical Tag code_example Dominance + Code Ratio >= 0.50",
  "total_chunks": 5230,
  "collections": {
    "qwen3_text": {
      "model": "Qwen/Qwen3-Embedding-0.6B",
      "dimension": 1024,
      "count": 4293,
      "file": "qwen3_text/qwen3_text_vectors.jsonl"
    },
    "jina_code": {
      "model": "jinaai/jina-embeddings-v2-base-code",
      "dimension": 768,
      "count": 937,
      "file": "jina_code/jina_code_vectors.jsonl"
    }
  },
  "delta_info": {
    "source_bundle": "artifacts/ai_coding_tutor_embeddings_delta_558.tar.gz",
    "delta_chunks_reassigned": 558,
    "reassigned_from": "qwen3_text",
    "reassigned_to": "jina_code"
  }
}
```

---

## 6. SỰ CỐ VÀ BIỆN PHÁP XỬ LÝ TRONG QUÁ TRÌNH TỰ ĐỘNG HÓA

1. **Dataset Mounting trên Kaggle:**  
   - *Vấn đề:* Để tránh Kaggle nạp nhầm `all_chunks.json` (7.7 MB) từ dataset cũ `minhthuy70/embedding`, hệ thống cần một dataset độc lập.  
   - *Xử lý:* Tự động tạo Kaggle Dataset riêng biệt `minhthuy70/ab-test-558-jina-delta` chỉ chứa `ab_test_558_jina_delta.json` và gán duy nhất dataset này vào `kernel-metadata.json`.
2. **Qwen3 Skip Mechanism:**  
   - *Vấn đề:* Notebook phải tuyệt đối không nạp Qwen3 vào GPU VRAM khi `target_text == 0`.  
   - *Xử lý:* Cờ `qwen_checkpoint_verified = True` đã ngăn hoàn toàn các lệnh `AutoConfig`, `AutoTokenizer` và `AutoModel`, giúp tiết kiệm 100% VRAM và đưa thời gian chạy tổng xuống dưới 50s.
3. **Quản lý Download Artifact:**  
   - *Vấn đề:* Lệnh tải kernel outputs mặc định tải cả 18 file checkpoint con qua kết nối mạng.  
   - *Xử lý:* Đã xác minh tính toàn vẹn của tệp nén chính `ai_coding_tutor_embeddings_delta_558.tar.gz` ngay khi tệp này hoàn tất, hủy tác vụ tải các checkpoint rời thừa và dọn dẹp thư mục `artifacts/` gọn gàng.

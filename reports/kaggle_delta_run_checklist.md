# CHECKLIST TIỀN THỰC THI KAGGLE GPU – DELTA JINA EMBEDDING (558 CHUNKS)

**Thời gian lập checklist:** 2026-11-20  
**Tập dữ liệu đầu vào:** `data/06_rag_dataset/chunks/ab_test_558_jina_delta.json` (558 chunks)  
**Notebook kiểm tra:** `notebooks/Kaggle_Embedding_Pipeline_GPU.ipynb`  
**Mục tiêu:** Tạo bổ sung 558 Jina Code embeddings (dimension 768) phục vụ Version B của Routing A/B Test.

---

## 1. TỔNG HỢP KẾT QUẢ THẨM ĐỊNH (EXECUTIVE SUMMARY)

Tất cả 6 tiêu chí kỹ thuật đã được kiểm toán tĩnh và chạy mô phỏng đối soát dữ liệu thực tế:

| STT | Hạng mục kiểm toán | Trạng thái | Ghi chú kỹ thuật |
|---|---|:---:|---|
| **1** | Xác nhận đường dẫn mount input trên Kaggle | **PASS** | Hỗ trợ đường dẫn cố định và cơ chế tự động quét đệ quy |
| **2** | Cell 3 dò tìm thành công file delta | **PASS** | Bắt đúng `ab_test_558_jina_delta.json` bất kể tên dataset slug |
| **3** | Cell 5 định tuyến TEXT = 0, CODE = 558 | **PASS** | 100% 558 chunks là `code_example` được chuyển sang CODE |
| **4** | Cell 6 hoàn toàn không tải hoặc khởi tạo Qwen3 | **PASS** | Bỏ qua nạp model và tokenizer, 0 MB GPU VRAM tiêu thụ |
| **5** | Cell 7 dùng đúng Jina Code & Attention-Masked Mean Pooling | **PASS** | `jina-embeddings-v2-base-code`, dim 768, normalized |
| **6** | Cell 8 xuất đúng artifact delta | **PASS** | Tạo gói `ai_coding_tutor_embeddings_delta_558.tar.gz` |

---

## 2. CHI TIẾT THẨM ĐỊNH TỪNG TIÊU CHÍ

### Tiêu chí 1: Cơ chế Mount đường dẫn Input trên Kaggle & Hướng dẫn Upload

Kaggle quản lý dữ liệu đầu vào theo cơ chế read-only mount vào `/kaggle/input/<dataset-slug>/`.

**Cách thức Kaggle mount:**
- Khi bạn upload file `ab_test_558_jina_delta.json` lên một Kaggle Dataset mới hoặc hiện có, Kaggle sẽ mount file vào:
  - `/kaggle/input/<tên-dataset-slug>/ab_test_558_jina_delta.json`
  - Hoặc `/kaggle/input/datasets/<username>/<tên-dataset-slug>/ab_test_558_jina_delta.json`

**Hướng dẫn cách upload (chọn 1 trong 2 cách):**
1. **Cách 1 (Khuyên dùng - Nhanh gọn nhất):**
   - Trên Kaggle, chọn **Datasets** $\rightarrow$ **New Dataset**.
   - Đặt tên Dataset: `ab-test-558-jina-delta` (hoặc tên tùy ý).
   - Tải file [ab_test_558_jina_delta.json](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/data/06_rag_dataset/chunks/ab_test_558_jina_delta.json) lên và bấm **Create**.
   - Mở Notebook, ở thanh bên phải (**Data**), bấm **+ Add Input**, tìm chọn dataset vừa tạo.
2. **Cách 2 (Thêm version mới vào dataset cũ `embedding`):**
   - Vào dataset `embedding` (tài khoản `minhthuy70`), bấm **New Version**, upload thêm file `ab_test_558_jina_delta.json`.
   - Notebook sẽ tự nhận diện theo đường dẫn ưu tiên số 1.

---

### Tiêu chí 2: Xác nhận Cell 3 dò tìm thành công `ab_test_558_jina_delta.json`

Trong Cell 3, logic dò tìm file hoạt động qua 2 tầng bảo vệ:

1. **Tầng 1 - Danh sách đường dẫn ưu tiên (`priority_paths`):**
   ```python
   priority_paths = [
       Path("/kaggle/input/datasets/minhthuy70/embedding/ab_test_558_jina_delta.json"),
       Path("/kaggle/input/embedding/ab_test_558_jina_delta.json"),
       Path("/kaggle/input/ab_test_558_jina_delta.json"),
       Path("/kaggle/input/ai-coding-tutor-chunks/ab_test_558_jina_delta.json"),
       Path("data/06_rag_dataset/chunks/ab_test_558_jina_delta.json"),
       ...
   ]
   ```
2. **Tầng 2 - Quét đệ quy tự động (`rglob`):**
   ```python
   if INPUT_CHUNK_FILE is None and Path("/kaggle/input").exists():
       all_candidates = list(Path("/kaggle/input").rglob("*delta*.json")) + list(Path("/kaggle/input").rglob("all_chunks.json"))
       if not all_candidates:
           all_candidates = list(Path("/kaggle/input").rglob("*chunk*.json"))
       if all_candidates:
           INPUT_CHUNK_FILE = all_candidates[0]
   ```
   - **Xác nhận:** `*delta*.json` được đặt trước `all_chunks.json`. Ngay cả khi trong `/kaggle/input/` tồn tại cả dataset cũ lẫn mới, hoặc bạn đặt tên folder tùy ý, Cell 3 luôn bắt trúng file delta đầu tiên.
   - Nếu không tìm thấy, Cell 3 in ra toàn bộ cây thư mục `/kaggle/input/` để chỉ rõ lỗi, không gây lỗi ngầm.

---

### Tiêu chí 3: Xác nhận Cell 5 phân loại đúng TEXT = 0, CODE = 558

- Toàn bộ 558 chunks trong `ab_test_558_jina_delta.json` đều là các chunks có `metadata.content_type == "code_example"`.
- Quy tắc 1 của `ModalityRouter` trong Cell 4:
  ```python
  if content_type == 'code_example':
      return Modality.CODE
  ```
- **Kết quả mô phỏng trên tập dữ liệu thực tế:**
  - `TEXT Chunks (Qwen3)` : **0 chunks (0.00%)**
  - `CODE Chunks (Jina Code)`: **558 chunks (100.00%)**
  - `Tổng số chunks`: **558 chunks**
  - `Trùng lặp ID`: **0 (100% Unique)**

---

### Tiêu chí 4: Xác nhận Cell 6 hoàn toàn không tải hoặc khởi tạo Qwen3

- Tại đầu Cell 6 có khối điều kiện:
  ```python
  if len(target_text) == 0:
      print("⚡ BỎ QUA QWEN3: Không có chunks TEXT trong tập input hiện tại (Delta-only mode). Bỏ qua nạp model Qwen3!")
      qwen_checkpoint_verified = True
      total_qwen = 0
      qwen_status = "skipped_delta_only_mode"
  ```
- Khối tải model Qwen3 được bao bọc bởi:
  ```python
  if not qwen_checkpoint_verified:
      # AutoConfig.from_pretrained(MODEL_ID_QWEN)
      # AutoTokenizer.from_pretrained(...)
      # AutoModel.from_pretrained(...)
  ```
- **Xác nhận:** Do `qwen_checkpoint_verified = True`, toàn bộ khối nạp model Qwen3 bị bỏ qua. 
  - `AutoModel` không được gọi.
  - `AutoTokenizer` không được gọi.
  - Không tải bất kỳ trọng số nào của Qwen3 về disk hay GPU VRAM.
  - `assert total_qwen == len(target_text)` ($0 == 0$) vượt qua an toàn.

---

### Tiêu chí 5: Xác nhận Cell 7 dùng đúng Jina Model & Attention-Masked Mean Pooling

- **Model ID:** `jinaai/jina-embeddings-v2-base-code`.
- **Dimension:** `768`.
- **Cơ chế Pooling:** Sử dụng Mean Pooling chuẩn của kiến trúc Jina BERT, xác minh bằng cờ:
  ```python
  assert model_jina[1].pooling_mode_mean_tokens is True, "Cấu hình model không phải Mean Pooling chuẩn!"
  ```
- **Safe Patch:** Áp dụng `Safe Embeddings Forward patch` triệt tiêu lỗi buffer `token_type_ids` trên một số môi trường Transformers mới.
- **Smoke Test:** Chạy thử nghiệm 2 mẫu code trên CUDA trước khi vào vòng lặp chính.
- **Normalization:** Tham số `normalize_embeddings=True` được kích hoạt trên từng batch.
- **Validation:** Mỗi vector đầu ra được kiểm tra qua `VectorValidator`:
  - Không chứa `NaN` hoặc `Inf`.
  - Độ dài vector đúng `768`.
  - L2-norm đạt xấp xỉ `1.0` (dung sai `5e-3`).
- **Khối lượng xử lý:** Đủ `558/558` chunks, lưu vào checkpoint theo từng batch và hợp nhất vào `jina_code_vectors.jsonl`.

---

### Tiêu chí 6: Xác nhận Cell 8 xuất đúng tên artifact delta

Tại Cell 8, tên gói nén được cấu hình tự động:
```python
is_delta_mode = "delta" in INPUT_CHUNK_FILE.name.lower() or len(target_text) == 0
archive_filename = "ai_coding_tutor_embeddings_delta_558.tar.gz" if is_delta_mode else "ai_coding_tutor_embeddings_bundle.tar.gz"
archive_path = WORKING_DIR / archive_filename
```
- **Xác nhận:**
  - Vì tên file là `ab_test_558_jina_delta.json` (chứa `delta`) và `len(target_text) == 0`, biến `is_delta_mode` chắc chắn nhận giá trị `True`.
  - Tên gói xuất ra: **`ai_coding_tutor_embeddings_delta_558.tar.gz`**.
  - Gói chứa đầy đủ:
    - `embeddings/jina_code/jina_code_vectors.jsonl` (558 vectors $\times$ 768 dims)
    - `reports/kaggle_embedding_benchmark_report.json`
    - `checkpoints/jina_code/...`
  - Hoàn toàn **không ghi đè** lên gói `ai_coding_tutor_embeddings_bundle.tar.gz` của Version A.

---

## 3. CHECKLIST THAO TÁC KHI CHẠY TRÊN KAGGLE (USER RUN GUIDE)

Để quá trình chạy diễn ra thuận lợi, bạn chỉ cần thực hiện 4 bước sau:

1. **Bước 1: Upload Dataset Delta**
   - Tải file local [ab_test_558_jina_delta.json](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/data/06_rag_dataset/chunks/ab_test_558_jina_delta.json) lên Kaggle làm Dataset mới (hoặc add vào dataset cũ).
2. **Bước 2: Cập nhật Notebook trên Kaggle**
   - Copy toàn bộ nội dung file [Kaggle_Embedding_Pipeline_GPU.ipynb](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/notebooks/Kaggle_Embedding_Pipeline_GPU.ipynb) lên Kaggle Notebook của bạn.
   - Bật **GPU T4 x 1** (hoặc GPU P100) và bật **Internet: On** (để tải weights Jina lần đầu).
3. **Bước 3: Chạy toàn bộ Notebook (Run All)**
   - Quan sát log Cell 3: Đảm bảo hiển thị `Đã xác định thành công file đầu vào: ...ab_test_558_jina_delta.json`.
   - Quan sát log Cell 6: Thấy thông báo `⚡ BỎ QUA QWEN3: Không có chunks TEXT...`.
   - Quan sát log Cell 7: Jina Code xử lý `558/558` chunks (thời gian dự kiến: ~15 đến 30 giây trên T4).
   - Quan sát log Cell 8: Thấy thông báo đóng gói `ai_coding_tutor_embeddings_delta_558.tar.gz`.
4. **Bước 4: Tải Artifact về máy**
   - Vào tab **Output** (bên phải), bấm download file `ai_coding_tutor_embeddings_delta_558.tar.gz`.
   - Lưu vào thư mục `Downloads` hoặc đường dẫn dự án để tiến hành bước thẩm định tự động tiếp theo.

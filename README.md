# AI-Powered Coding Tutor & Auto-Grader

Research project on an AI-powered platform for automated code assessment and intelligent programming tutoring.

## Research Areas

- Automated Programming Assessment
- Code Execution and Auto-Grading
- Static Code Analysis
- LLM-based Code Analysis
- AI Programming Tutor
- Secure Code Execution
- Code Quality Assessment

## PDF Parser Benchmark Dataset

### Overview

Project includes a synthetic PDF parser benchmark dataset for demonstration and workflow testing purposes.

**⚠️ QUAN TRỌNG: DỮ LIỆU TỰ TẠO (SYNTHETIC)**

- **Tên nhãn simulation:** `SIMULATED_DATA`
- **Trạng thái thực thi:** `NOT_EXECUTED`
- **Trạng thái dữ liệu:** `SYNTHETIC_ONLY`

Tập dữ liệu này được tạo hoàn toàn bằng script Python với giả định có chủ đích. Không có parser nào được cài đặt hoặc thực thi thực tế. Tất cả điểm số và chỉ số là giả định mô phỏng, không phải kết quả đo đạc thực nghiệm.

### Dataset Structure

```
data/
├── 01_original_documents/          # 5 PDF documents gốc
│   ├── DOC01_C++23_Working_Draft.pdf
│   ├── DOC02_Python_Tutorial.pdf
│   ├── DOC03_The_Java_Language_Java_SE_26_Edition.pdf
│   ├── DOC04_Mathematics_for_Computer_Science.pdf
│   └── DOC05_Security_Engineering_Explained.pdf
│
├── 02_ground_truth/               # Ground truth (synthetic)
│   ├── GROUND_TRUTH_PAGE_TEMPLATE.md
│   ├── DOC01/
│   ├── DOC02/
│   ├── DOC03/
│   ├── DOC04/
│   └── DOC05/
│
├── 03_parser_outputs/              # Output từ parsers (chưa có)
│   ├── docling/
│   ├── mineru/
│   ├── mineru_test/
│   └── pymupdf/
│
├── 04_benchmark/                   # Benchmark data và reports
│   ├── benchmark_config.json
│   ├── synthetic_ground_truth.csv        # 100 records
│   ├── synthetic_parser_results.csv      # 300 records
│   ├── benchmark_results.csv             # 18 records
│   ├── processing_times.csv              # 15 records
│   ├── resource_usage.csv                # 15 records
│   ├── evaluation_notes.md
│   ├── simulation_methodology.md
│   ├── data_validation_report.md
│   └── mineru_test.log
│
├── 05_reports/                     # Final reports
│   ├── benchmark_summary.json
│   ├── benchmark_summary.md
│   ├── parser_comparison.md
│   ├── final_selection.md
│   └── synthetic_pdf_benchmark.xlsx      # Excel workbook
│
└── 06_rag_dataset/                 # RAG dataset (chưa có)
    ├── chunks/
    ├── cleaned/
    ├── embeddings/
    ├── manifests/
    └── normalized/
```

### Dataset Statistics

- **Documents:** 5
- **Samples per document:** 20
- **Total samples:** 100
- **Parser candidates:** 3 (MinerU, Docling, PyMuPDF)
- **Parser-page records:** 300 (100 samples × 3 parsers)
- **Sampling method:** Stratified sampling (6-8-6 distribution)

### Evaluation Metrics

| Metric | Weight | Description |
|---|---:|---|
| Text Accuracy | 20% | Độ chính xác văn bản |
| Content Completeness | 15% | Tính đầy đủ nội dung |
| Reading Order | 10% | Thứ tự đọc |
| Heading Detection | 10% | Phát hiện tiêu đề |
| Table Extraction | 15% | Trích xuất bảng |
| Code Preservation | 10% | Bảo toàn code |
| Formula Preservation | 10% | Bảo toàn công thức |
| Layout Preservation | 10% | Bảo toàn layout |

### Generated Files

#### CSV Files
- `synthetic_ground_truth.csv` - 100 synthetic sample records
- `synthetic_parser_results.csv` - 300 synthetic parser results
- `benchmark_results.csv` - 18 aggregated results
- `processing_times.csv` - 15 processing time records
- `resource_usage.csv` - 15 resource usage records

#### JSON Files
- `benchmark_config.json` - Benchmark configuration
- `benchmark_summary.json` - Benchmark summary

#### Markdown Files
- `evaluation_notes.md` - Evaluation notes and methodology
- `simulation_methodology.md` - Detailed simulation methodology
- `benchmark_summary.md` - Benchmark summary in Vietnamese
- `parser_comparison.md` - Parser comparison in Vietnamese
- `final_selection.md` - Final selection (PENDING_REAL_BENCHMARK)
- `data_validation_report.md` - Data validation report

#### Excel Workbook
- `synthetic_pdf_benchmark.xlsx` - Complete workbook with 7 worksheets:
  - README
  - Synthetic_Ground_Truth
  - Synthetic_Parser_Results
  - Benchmark_Results
  - Processing_Times
  - Resource_Usage
  - Metric_Weights

### Purpose of Synthetic Dataset

Tập dữ liệu tự tạo này được tạo với mục đích:

1. **Demonstration:** Demo workflow và cấu trúc benchmark
2. **Testing:** Test aggregation và reporting pipeline
3. **Validation:** Validate format dữ liệu và cấu trúc file
4. **Preparation:** Chuẩn bị template cho benchmark thực tế

### Important Limitations

**KHÔNG sử dụng dữ liệu này để:**
- Chọn parser cho sản xuất
- So sánh hiệu năng thực tế
- Ra quyết định kỹ thuật
- Công bố kết quả nghiên cứu

**Lý do:**
- Không có thực thi parsing thực tế
- Không có ground truth thực tế
- Không có đo đạc thời gian/tài nguyên thực tế
- Tất cả điểm số là giả định mô phỏng

### How to Replace with Real Data

Để chuyển từ dữ liệu tự tạo sang benchmark thực tế:

1. **Cài đặt parsers:**
   ```bash
   pip install mineru  # (chưa thực hiện)
   pip install docling  # (chưa thực hiện)
   pip install pymupdf  # (chưa thực hiện)
   ```

2. **Thực thi parsing:**
   - Chạy từng parser trên 5 tài liệu PDF gốc
   - Lưu output theo cấu trúc chuẩn
   - Document lỗi và warning

3. **Tạo ground truth thực tế:**
   - Mở PDF gốc bằng PDF viewer
   - Chọn 20 trang mẫu theo stratified sampling
   - Chép thủ công nội dung chính xác
   - Phân loại page type
   - Xác minh bởi reviewer

4. **Đánh giá chỉ số thực tế:**
   - So sánh output parser với ground truth
   - Tính toán accuracy từng metric
   - Document lỗi cụ thể

5. **Đo đạc hiệu năng:**
   - Đo thời gian xử lý thực tế
   - Đo sử dụng CPU/RAM/GPU thực tế
   - Lặp 3 lần cho độ tin cậy

6. **Thay thế dữ liệu:**
   - Thay thế các file CSV với dữ liệu thực tế
   - Xóa nhãn "SIMULATED_DATA"
   - Cập nhật status field
   - Re-run validation

### Scripts Used

- `generate_synthetic_data.py` - Tạo ground truth và parser results
- `generate_operational_data.py` - Tạo processing times và resource usage
- `generate_benchmark_results.py` - Tạo benchmark results (aggregation)
- `create_excel_workbook.py` - Tạo Excel workbook
- `validate_data.py` - Validate dữ liệu

### Validation

Tất cả dữ liệu đã được validate qua 13 checks:

1. ✓ Exactly 5 document IDs (DOC01-DOC05)
2. ✓ Exactly 20 synthetic samples per document
3. ✓ Exactly 100 synthetic sample records
4. ✓ Exactly 300 parser-page records
5. ✓ Exactly 3 parser candidates (MinerU, Docling, PyMuPDF)
6. ✓ All 8 evaluation metrics exist
7. ✓ Metric weights sum to 100%
8. ✓ All weighted scores between 0 and 100
9. ✓ No actual PDF page numbers fabricated
10. ✓ No actual measurement fields contain synthetic values
11. ✓ All 5 original PDF files exist and unchanged
12. ✓ mineru_test.log exists and unchanged
13. ✓ All records have SIMULATED_DATA label

Validation report: `data/04_benchmark/data_validation_report.md`

### Next Steps

Để thực hiện benchmark thực tế:

1. Review dataset tự tạo hiện tại
2. Cài đặt parsers thực tế
3. Thực hiện parsing trên PDF gốc
4. Tạo ground truth thủ công
5. Đánh giá các metric thực tế
6. Đo đạc thời gian và tài nguyên thực tế
7. Thay thế dữ liệu tự tạo bằng dữ liệu thực tế
8. Ra quyết định dựa trên dữ liệu thực tế

---

## Objectives

The system aims to evaluate student source code using:

1. Traditional test-case based grading
2. Static code analysis
3. Algorithm complexity analysis
4. Security analysis
5. LLM-based code understanding
6. AI-generated pedagogical feedback

## Research Direction

Traditional Auto-Grader
        +
Static Analysis
        +
Execution Evidence
        +
LLM
        ↓
AI-Powered Code Assessment & Tutor

## Project Status

- **Sprint:** Day 1 Foundation Complete (01/10/2026)
- **Architecture:** Modular Monolith (FastAPI + Next.js + PostgreSQL + Redis)

## Quick Start / Chạy hệ thống

### Yêu cầu tiên quyết (Prerequisites)
- **Docker Desktop đang chạy** (Docker Engine daemon hoạt động trên máy host).
- Docker Compose v2+.
- Git.

### 1. Chuẩn bị biến môi trường
Tạo file `.env` từ mẫu `.env.example`:
```bash
cp .env.example .env
```
*(Lưu ý: Không commit file `.env` chứa cấu hình nội bộ lên Git).*

### 2. Khởi động toàn bộ hệ thống
Khởi chạy đồng thời 4 dịch vụ (Frontend, Backend, PostgreSQL, Redis) qua Docker Compose:
```bash
docker compose up -d --build
```

### 3. Kiểm tra trạng thái containers
```bash
docker compose ps
```

### 4. Kiểm tra sức khỏe hệ thống (Health Check)
Kiểm tra kết nối giữa FastAPI, PostgreSQL và Redis:
```bash
curl http://localhost:8000/api/health
```
Kết quả mong đợi (HTTP 200 OK):
```json
{
  "status": "ok",
  "database": "connected",
  "redis": "connected",
  "environment": "development"
}
```

### 5. Danh sách Ports & URLs truy cập

|| Dịch vụ | Port | URL / Điểm truy cập |
|| :--- | :--- | :--- |
|| **Frontend (Next.js)** | `3000` | http://localhost:3000 |
|| **Backend API (FastAPI)** | `8000` | http://localhost:8000 (API Docs: http://localhost:8000/docs) |
|| **Backend Health Check** | `8000` | http://localhost:8000/api/health |
|| **PostgreSQL Database** | `5432` | `localhost:5432` |
|| **Redis Cache / Broker** | `6379` | `localhost:6379` |

### 6. Dừng hệ thống
```bash
docker compose down
```

## Team

- [Your Name]

## License

MIT

## Objectives

The system aims to evaluate student source code using:

1. Traditional test-case based grading
2. Static code analysis
3. Algorithm complexity analysis
4. Security analysis
5. LLM-based code understanding
6. AI-generated pedagogical feedback

## Research Direction

Traditional Auto-Grader
        +
Static Analysis
        +
Execution Evidence
        +
LLM
        ↓
AI-Powered Code Assessment & Tutor

## Project Status

- **Sprint:** Day 1 Foundation Complete (01/10/2026)
- **Architecture:** Modular Monolith (FastAPI + Next.js + PostgreSQL + Redis)

## Quick Start / Chạy hệ thống

### Yêu cầu tiên quyết (Prerequisites)
- **Docker Desktop đang chạy** (Docker Engine daemon hoạt động trên máy host).
- Docker Compose v2+.
- Git.

### 1. Chuẩn bị biến môi trường
Tạo file `.env` từ mẫu `.env.example`:
```bash
cp .env.example .env
```
*(Lưu ý: Không commit file `.env` chứa cấu hình nội bộ lên Git).*

### 2. Khởi động toàn bộ hệ thống
Khởi chạy đồng thời 4 dịch vụ (Frontend, Backend, PostgreSQL, Redis) qua Docker Compose:
```bash
docker compose up -d --build
```

### 3. Kiểm tra trạng thái containers
```bash
docker compose ps
```

### 4. Kiểm tra sức khỏe hệ thống (Health Check)
Kiểm tra kết nối giữa FastAPI, PostgreSQL và Redis:
```bash
curl http://localhost:8000/api/health
```
Kết quả mong đợi (HTTP 200 OK):
```json
{
  "status": "ok",
  "database": "connected",
  "redis": "connected",
  "environment": "development"
}
```

### 5. Danh sách Ports & URLs truy cập

| Dịch vụ | Port | URL / Điểm truy cập |
| :--- | :--- | :--- |
| **Frontend (Next.js)** | `3000` | http://localhost:3000 |
| **Backend API (FastAPI)** | `8000` | http://localhost:8000 (API Docs: http://localhost:8000/docs) |
| **Backend Health Check** | `8000` | http://localhost:8000/api/health |
| **PostgreSQL Database** | `5432` | `localhost:5432` |
| **Redis Cache / Broker** | `6379` | `localhost:6379` |

### 6. Dừng hệ thống
```bash
docker compose down
```

## Team

- [Your Name]

## License

MIT
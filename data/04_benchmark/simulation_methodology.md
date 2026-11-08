# Phương pháp Tạo Dữ liệu Mô phỏng (Simulation Methodology)

## ⚠️ QUAN TRỌNG: TÀI LIỆU NÀY GIẢI THÍCH CÁCH TẠO DỮ LIỆU TỰ TẠO

**TÊN NHÃN SIMULATION:** `SIMULATED_DATA`
**TRẠNG THÁI THỰC THI:** `NOT_EXECUTED`
**TRẠNG THÁI DỮ LIỆU:** `SYNTHETIC_ONLY`

---

## Tổng quan

Tài liệu này giải thích chi tiết phương pháp tạo dữ liệu tự tạo (synthetic) cho benchmark PDF parser. Tất cả dữ liệu được tạo bằng script Python với giả định có chủ đích, không dựa trên thực tế.

## Mục đích Tạo Dữ liệu Tự tạo

1. **Demo Workflow:** Demo cấu trúc và quy trình benchmark
2. **Test Pipeline:** Test aggregation và reporting pipeline
3. **Validate Format:** Validate format dữ liệu và cấu trúc file
4. **Prepare Template:** Chuẩn bị template cho benchmark thực tế

## Tổng quan Dữ liệu

| Dataset | Số records | Mô tả |
|---|---:|---|
| Synthetic Ground Truth | 100 | 20 samples × 5 documents |
| Synthetic Parser Results | 300 | 100 samples × 3 parsers |
| Processing Times | 15 | 5 documents × 3 parsers |
| Resource Usage | 15 | 5 documents × 3 parsers |
| Benchmark Results | 18 | 15 document-level + 3 overall |

## Phương pháp Tạo Ground Truth Synthetic

### Script: `generate_synthetic_data.py` (phần ground truth)

### Bước 1: Xác định Documents

```python
documents = ["DOC01", "DOC02", "DOC03", "DOC04", "DOC05"]
```

### Bước 2: Xác định Page Types

```python
page_types = ["TEXT", "CODE", "TABLE", "EQUATION", "FIGURE", "HEADING", "MIXED"]
```

### Bước 3: Stratified Sampling

Mỗi document có 20 samples được phân phối:

- **First Third (samples 1-6):** 6 samples
- **Middle Third (samples 7-14):** 8 samples
- **Final Third (samples 15-20):** 6 samples

### Bước 4: Gán Page Type theo Pattern

Pattern cố định cho 20 samples mỗi document:

| Sample | Page Type | Sample | Page Type |
|---|---|---|---|
| 1 | TEXT | 11 | HEADING |
| 2 | CODE | 12 | MIXED |
| 3 | HEADING | 13 | TEXT |
| 4 | TEXT | 14 | FIGURE |
| 5 | EQUATION | 15 | CODE |
| 6 | MIXED | 16 | TEXT |
| 7 | TEXT | 17 | TABLE |
| 8 | TABLE | 18 | HEADING |
| 9 | CODE | 19 | TEXT |
| 10 | TEXT | 20 | MIXED |

### Bước 5: Gán Complexity

Rules giả định:

- **HIGH:** CODE, EQUATION, MIXED
- **LOW:** HEADING, TEXT ở vị trí 3, 11, 18, 19
- **MEDIUM:** Các trường hợp còn lại

### Bước 6: Tạo Fields

Mỗi record có các fields:

- `simulation_label`: "SIMULATED_DATA"
- `document_id`: DOC01-DOC05
- `pdf_filename`: Tên file PDF tương ứng
- `document_domain`: Lĩnh vực tài liệu
- `sample_id`: DOC01_001 đến DOC05_020
- `synthetic_sample_order`: 1-20
- `synthetic_relative_position_pct`: 5-98%
- `sampling_stratum`: First/Middle/Final Third
- `primary_page_type`: Theo pattern
- `secondary_page_types`: Để trống hoặc CODE;TEXT
- `complexity`: LOW/MEDIUM/HIGH/MIDDLE
- `synthetic_content_profile`: Mô tả giả định
- `actual_pdf_page_number`: Để trống (không giả định)
- `ground_truth_status`: "SYNTHETIC"
- `review_status`: "NOT_VERIFIED"
- `notes`: "SIMULATED_DATA - NOT_REAL_EXPERIMENTAL_RESULTS"

## Phương pháp Tạo Parser Results Synthetic

### Script: `generate_synthetic_data.py` (phần parser results)

### Bước 1: Xác định Parsers

```python
parsers = ["MinerU", "Docling", "PyMuPDF"]
```

### Bước 2: Xác định Base Scores

Giả định base score cho mỗi parser:

| Parser | Base Score | Giả định |
|---|---:|---|
| MinerU | 85 | Mạnh trên layout phức tạp |
| Docling | 88 | Mạnh trên text và code |
| PyMuPDF | 78 | Tốt trên layout đơn giản |

### Bước 3: Xác định Page Type Adjustments

Giả định adjustment theo page type:

| Page Type | MinerU | Docling | PyMuPDF |
|---|---:|---:|---:|
| TEXT | +5 | +8 | +3 |
| CODE | +7 | +10 | +2 |
| TABLE | +10 | +5 | +4 |
| EQUATION | +8 | +6 | 0 |
| FIGURE | +9 | +7 | +3 |
| HEADING | +4 | +6 | +5 |
| MIXED | +9 | +8 | +3 |

### Bước 4: Complexity Penalty

Giả định penalty theo complexity:

- **LOW:** 0 penalty
- **MEDIUM:** 2 penalty
- **HIGH:** 5 penalty

### Bước 5: Tính Individual Metric Scores

Công thức:

```
score = base_score + page_type_adjustment - complexity_penalty + random_variation
```

Random variation: ±5 điểm

### Bước 6: Tính Weighted Score

Trọng số metric:

| Metric | Weight |
|---|---:|
| text_accuracy | 0.20 |
| content_completeness | 0.15 |
| reading_order | 0.10 |
| heading_detection | 0.10 |
| table_extraction | 0.15 |
| code_preservation | 0.10 |
| formula_preservation | 0.10 |
| layout_preservation | 0.10 |

Công thức:

```
weighted_score = Σ(metric_score × metric_weight)
```

### Bước 7: Tạo Fields

Mỗi record có các fields:

- `simulation_label`: "SIMULATED_DATA"
- `document_id`: DOC01-DOC05
- `sample_id`: DOC01_001 đến DOC05_020
- `parser`: MinerU/Docling/PyMuPDF
- `text_accuracy`: 0-100 (simulated)
- `content_completeness`: 0-100 (simulated)
- `reading_order`: 0-100 (simulated)
- `heading_detection`: 0-100 (simulated)
- `table_extraction`: 0-100 (simulated)
- `code_preservation`: 0-100 (simulated)
- `formula_preservation`: 0-100 (simulated)
- `layout_preservation`: 0-100 (simulated)
- `weighted_quality_score`: 0-100 (simulated)
- `actual_execution_performed`: false
- `model_or_runtime_version`: "NOT_MEASURED"

## Phương pháp Tạo Processing Times Synthetic

### Script: `generate_operational_data.py`

### Bước 1: Xác định Base Times

Giả định base time (giây):

| Parser | Base Time | Giả định |
|---|---:|---|
| MinerU | 45.0 | Chậm hơn, AI-powered |
| Docling | 35.0 | Tốc độ vừa phải |
| PyMuPDF | 25.0 | Nhanh nhất |

### Bước 2: Thêm Variation

```python
doc_factor = random.uniform(0.8, 1.2)
parser_factor = random.uniform(0.9, 1.1)
simulated_time = base_time × doc_factor × parser_factor
```

### Bước 3: Tạo Fields

- `simulation_label`: "SIMULATED_DATA"
- `document_id`: DOC01-DOC05
- `pdf_filename`: Tên file PDF
- `parser`: MinerU/Docling/PyMuPDF
- `sample_pages`: 20
- `simulated_elapsed_seconds`: Giá trị giả định
- `actual_elapsed_seconds`: Để trống
- `measurement_status`: "NOT_MEASURED"

## Phương pháp Tạo Resource Usage Synthetic

### Script: `generate_operational_data.py`

### Bước 1: Xác định Base Values

Giả định base CPU (%):

| Parser | Base CPU |
|---|---:|
| MinerU | 65 |
| Docling | 55 |
| PyMuPDF | 40 |

Giả định base RAM (MB):

| Parser | Base RAM |
|---|---:|
| MinerU | 2048 |
| Docling | 1536 |
| PyMuPDF | 1024 |

Giả định base GPU VRAM (MB):

| Parser | Base GPU |
|---|---:|
| MinerU | 512 |
| Docling | 256 |
| PyMuPDF | 0 |

### Bước 2: Thêm Variation

```python
cpu_factor = random.uniform(0.9, 1.1)
ram_factor = random.uniform(0.85, 1.15)
gpu_factor = random.uniform(0.9, 1.1)
```

### Bước 3: Tạo Fields

- `simulation_label`: "SIMULATED_DATA"
- `document_id`: DOC01-DOC05
- `parser`: MinerU/Docling/PyMuPDF
- `sample_pages`: 20
- `simulated_avg_cpu_percent`: Giá trị giả định
- `simulated_peak_ram_mb`: Giá trị giả định
- `simulated_peak_gpu_vram_mb`: Giá trị giả định
- `actual_cpu_percent`: Để trống
- `actual_peak_ram_mb`: Để trống
- `actual_peak_gpu_vram_mb`: Để trống
- `measurement_status`: "NOT_MEASURED"

## Phương pháp Tạo Benchmark Results Synthetic

### Script: `generate_benchmark_results.py`

### Bước 1: Đọc Parser Results

Đọc `synthetic_parser_results.csv`

### Bước 2: Tính Average theo Document

Tính average cho mỗi (document, parser) pair:

- 15 records (5 documents × 3 parsers)

### Bước 3: Tính Average Overall

Tính average cho mỗi parser trên tất cả documents:

- 3 records (3 parsers)

### Bước 4: Tạo Fields

- `simulation_label`: "SIMULATED_DATA"
- `aggregation_level`: "DOCUMENT" hoặc "OVERALL"
- `document_id`: DOC01-DOC05 hoặc "ALL"
- `parser`: MinerU/Docling/PyMuPDF
- `sample_count`: 20 hoặc 100
- `avg_text_accuracy`: Average simulated
- `avg_content_completeness`: Average simulated
- `avg_reading_order`: Average simulated
- `avg_heading_detection`: Average simulated
- `avg_table_extraction`: Average simulated
- `avg_code_preservation`: Average simulated
- `avg_formula_preservation`: Average simulated
- `avg_layout_preservation`: Average simulated
- `avg_weighted_quality_score`: Average simulated
- `ranking`: "SIMULATED_RANKING_NOT_EMPIRICAL"

## Random Seed

Tất cả script sử dụng random seed cố định:

```python
random.seed(42)
```

Điều này đảm bảo tính tái tạo (reproducibility) của dữ liệu tự tạo.

## Scripts Được Sử Dụng

1. **generate_synthetic_data.py:** Tạo ground truth và parser results
2. **generate_operational_data.py:** Tạo processing times và resource usage
3. **generate_benchmark_results.py:** Tạo benchmark results (aggregation)

## Files Được Tạo

### Benchmark Data

- `data/04_benchmark/synthetic_ground_truth.csv`
- `data/04_benchmark/synthetic_parser_results.csv`
- `data/04_benchmark/processing_times.csv`
- `data/04_benchmark/resource_usage.csv`
- `data/04_benchmark/benchmark_results.csv`
- `data/04_benchmark/benchmark_config.json`

### Ground Truth Manifests

- `data/02_ground_truth/DOC01/synthetic_page_manifest.csv`
- `data/02_ground_truth/DOC02/synthetic_page_manifest.csv`
- `data/02_ground_truth/DOC03/synthetic_page_manifest.csv`
- `data/02_ground_truth/DOC04/synthetic_page_manifest.csv`
- `data/02_ground_truth/DOC05/synthetic_page_manifest.csv`

### Reports

- `data/05_reports/benchmark_summary.json`
- `data/05_reports/benchmark_summary.md`
- `data/05_reports/parser_comparison.md`
- `data/05_reports/final_selection.md`

### Documentation

- `data/04_benchmark/evaluation_notes.md`
- `data/04_benchmark/simulation_methodology.md` (file này)

## Hạn chế

1. **Không có thực tế:** Tất cả dữ liệu là giả định
2. **Không có đo đạc:** Không có measurement thực tế
3. **Không có ground truth:** Không có verification thủ công
4. **Giả định đơn giản:** Giả định không dựa trên nghiên cứu
5. **Không tổng quát:** Không thể áp dụng cho trường hợp khác

## Cách Thay thế bằng Dữ liệu Thực tế

Để thay thế dữ liệu tự tạo bằng dữ liệu thực tế:

1. Cài đặt parsers thực tế
2. Thực thi parsing trên PDF gốc
3. Tạo ground truth thủ công
4. Đánh giá các metric thực tế
5. Đo đạc thời gian và tài nguyên thực tế
6. Thay thế các file CSV với dữ liệu thực tế
7. Xóa tất cả nhãn "SIMULATED_DATA"
8. Cập nhật các status field

---

**Ngày tạo:** 2026-11-04
**Phiên bản:** 1.0.0
**Random Seed:** 42
**Trạng thái:** `SYNTHETIC_DATA_ONLY`

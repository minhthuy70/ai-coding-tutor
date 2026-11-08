# So sánh Parser PDF

## ⚠️ QUAN TRỌNG: DỮ LIỆU TỰ TẠO (SYNTHETIC)

**TÊN NHÃN SIMULATION:** `SIMULATED_DATA`
**TRẠNG THÁI THỰC THI:** `NOT_EXECUTED`
**TRẠNG THÁI DỮ LIỆU:** `SYNTHETIC_ONLY`

Đây là báo cáo so sánh dựa trên dữ liệu tự tạo. Không có parser nào được cài đặt hoặc thực thi thực tế.

---

## Tổng quan So sánh

### Ứng viên Parser

| Parser | Đặc điểm chính | Trạng thái |
|---|---|---|
| **MinerU** | AI-powered parser với khả năng hiểu layout phức tạp | NOT_INSTALLED |
| **Docling** | Thư viện document understanding từ IBM | NOT_INSTALLED |
| **PyMuPDF** | Parser nhẹ, tốc độ nhanh, phù hợp layout đơn giản | NOT_INSTALLED |

### Giả định Hiệu năng Mô phỏng

**CẢNH BÁO:** Các điểm số dưới đây là giả định mô phỏng cho demonstration, không phải kết quả đo đạc thực tế.

#### Giả định Base Scores

| Parser | Base Score | Giả định điểm mạnh |
|---|---:|---|
| MinerU | 85 | Layout phức tạp, bảng, công thức |
| Docling | 88 | Văn bản, code |
| PyMuPDF | 78 | Layout đơn giản, tốc độ |

## So sánh theo Chỉ số

### Chỉ số Đánh giá

| Chỉ số | Trọng số | Mô tả |
|---|---:|---|
| Text Accuracy | 20% | Độ chính xác văn bản |
| Content Completeness | 15% | Tính đầy đủ nội dung |
| Reading Order | 10% | Thứ tự đọc |
| Heading Detection | 10% | Phát hiện tiêu đề |
| Table Extraction | 15% | Trích xuất bảng |
| Code Preservation | 10% | Bảo toàn code |
| Formula Preservation | 10% | Bảo toàn công thức |
| Layout Preservation | 10% | Bảo toàn layout |

### So sánh Giả định theo Tài liệu

**Lưu ý:** Các điểm số dưới đây được tổng hợp từ `benchmark_results.csv` và là giả định mô phỏng.

#### DOC01 - C++23 Working Draft

| Parser | Avg Weighted Score | Text Accuracy | Table Extraction | Code Preservation |
|---|---:|---:|---:|---:|
| MinerU | SIMULATED | SIMULATED | SIMULATED | SIMULATED |
| Docling | SIMULATED | SIMULATED | SIMULATED | SIMULATED |
| PyMuPDF | SIMULATED | SIMULATED | SIMULATED | SIMULATED |

#### DOC02 - Python Tutorial

| Parser | Avg Weighted Score | Text Accuracy | Code Preservation |
|---|---:|---:|---:|
| MinerU | SIMULATED | SIMULATED | SIMULATED |
| Docling | SIMULATED | SIMULATED | SIMULATED |
| PyMuPDF | SIMULATED | SIMULATED | SIMULATED |

#### DOC03 - Java Language SE 26

| Parser | Avg Weighted Score | Text Accuracy | Code Preservation |
|---|---:|---:|---:|
| MinerU | SIMULATED | SIMULATED | SIMULATED |
| Docling | SIMULATED | SIMULATED | SIMULATED |
| PyMuPDF | SIMULATED | SIMULATED | SIMULATED |

#### DOC04 - Mathematics for Computer Science

| Parser | Avg Weighted Score | Formula Preservation | Layout Preservation |
|---|---:|---:|---:|
| MinerU | SIMULATED | SIMULATED | SIMULATED |
| Docling | SIMULATED | SIMULATED | SIMULATED |
| PyMuPDF | SIMULATED | SIMULATED | SIMULATED |

#### DOC05 - Security Engineering Explained

| Parser | Avg Weighted Score | Text Accuracy | Code Preservation |
|---|---:|---:|---:|
| MinerU | SIMULATED | SIMULATED | SIMULATED |
| Docling | SIMULATED | SIMULATED | SIMULATED |
| PyMuPDF | SIMULATED | SIMULATED | SIMULATED |

## So sánh Thời gian Xử lý

### Giả định Thời gian (giây)

| Parser | DOC01 | DOC02 | DOC03 | DOC04 | DOC05 | Trung bình |
|---|---:|---:|---:|---:|---:|---:|
| MinerU | SIMULATED | SIMULATED | SIMULATED | SIMULATED | SIMULATED | SIMULATED |
| Docling | SIMULATED | SIMULATED | SIMULATED | SIMULATED | SIMULATED | SIMULATED |
| PyMuPDF | SIMULATED | SIMULATED | SIMULATED | SIMULATED | SIMULATED | SIMULATED |

**Lưu ý:** Các giá trị thời gian là giả định mô phỏng trong `processing_times.csv`.

## So sánh Sử dụng Tài nguyên

### Giả định CPU (%)

| Parser | Trung bình |
|---|---:|
| MinerU | SIMULATED |
| Docling | SIMULATED |
| PyMuPDF | SIMULATED |

### Giả định RAM (MB)

| Parser | Trung bình |
|---|---:|
| MinerU | SIMULATED |
| Docling | SIMULATED |
| PyMuPDF | SIMULATED |

### Giả định GPU VRAM (MB)

| Parser | Trung bình |
|---|---:|
| MinerU | SIMULATED |
| Docling | SIMULATED |
| PyMuPDF | SIMULATED |

**Lưu ý:** Các giá trị tài nguyên là giả định mô phỏng trong `resource_usage.csv`.

## Phân tích theo Loại Trang

### Hiệu năng giả định theo loại trang

| Loại trang | MinerU | Docling | PyMuPDF |
|---|---:|---:|---:|
| TEXT | SIMULATED | SIMULATED | SIMULATED |
| CODE | SIMULATED | SIMULATED | SIMULATED |
| TABLE | SIMULATED | SIMULATED | SIMULATED |
| EQUATION | SIMULATED | SIMULATED | SIMULATED |
| FIGURE | SIMULATED | SIMULATED | SIMULATED |
| HEADING | SIMULATED | SIMULATED | SIMULATED |
| MIXED | SIMULATED | SIMULATED | SIMULATED |

## Xếp hạng Mô phỏng

**CẢNH BÁO:** `SIMULATED_RANKING_NOT_EMPIRICAL`

Xếp hạng dưới đây dựa trên giả định mô phỏng, không phải kết quả thực nghiệm.

### Xếp hạng Tổng quan (Giả định)

1. **Parser 1** - `SIMULATED_RANK`
2. **Parser 2** - `SIMULATED_RANK`
3. **Parser 3** - `SIMULATED_RANK`

**QUAN TRỌNG:** Không sử dụng xếp hạng này để ra quyết định thực tế.

## Điểm mạnh và Điểm yếu (Giả định)

### MinerU (Giả định)

**Điểm mạnh giả định:**
- Layout phức tạp
- Bảng có cấu trúc phức tạp
- Công thức toán học
- Hình ảnh và diagram

**Điểm yếu giả định:**
- Thời gian xử lý lâu hơn
- Sử dụng tài nguyên cao hơn

### Docling (Giả định)

**Điểm mạnh giả định:**
- Trích xuất văn bản chính xác
- Bảo toàn code tốt
- Tốc độ xử lý vừa phải

**Điểm yếu giả định:**
- Bảng có thể gặp vấn đề
- Layout phức tạp hạn chế

### PyMuPDF (Giả định)

**Điểm mạnh giả định:**
- Tốc độ xử lý nhanh
- Sử dụng tài nguyên thấp
- Layout đơn giản tốt

**Điểm yếu giả định:**
- Layout phức tạp kém
- Code và công thức hạn chế

## Cảnh báo Quan trọng

Tất cả so sánh trong báo cáo này dựa trên **dữ liệu tự tạo (synthetic)**. Không có parser nào được cài đặt hoặc thực thi thực tế.

**Không sử dụng báo cáo này để:**
- Chọn parser cho sản xuất
- So sánh hiệu năng thực tế
- Ra quyết định kỹ thuật
- Công bố kết quả nghiên cứu

## Bước Tiếp theo

Để có so sánh thực tế:

1. Cài đặt các parser
2. Thực thi parsing trên PDF gốc
3. Tạo ground truth thực tế
4. Đo đạc chỉ số thực tế
5. Thu thập thời gian và tài nguyên thực tế
6. Thay thế dữ liệu tự tạo bằng dữ liệu thực nghiệm

---

**Ngày tạo:** 2026-11-04
**Phiên bản:** 1.0.0

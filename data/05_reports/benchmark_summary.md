# Tóm tắt Benchmark PDF Parser

## ⚠️ QUAN TRỌNG: DỮ LIỆU TỰ TẠO (SYNTHETIC)

**TÊN NHÃN SIMULATION:** `SIMULATED_DATA`
**TRẠNG THÁI THỰC THI:** `NOT_EXECUTED`
**TRẠNG THÁI DỮ LIỆU:** `SYNTHETIC_ONLY`

Đây là tập dữ liệu benchmark tự tạo để phục vụ mục đích **demonstration và testing workflow**. Không có bất kỳ hoạt động parsing PDF thực tế nào được thực hiện. Tất cả điểm số và chỉ số đều là giả định mô phỏng, không phải kết quả đo đạc thực nghiệm.

---

## Tổng quan Benchmark

- **Tổng số tài liệu:** 5
- **Tổng số mẫu:** 100
- **Mẫu trên mỗi tài liệu:** 20
- **Tổng số ứng viên parser:** 3
- **Tổng số bản ghi parser-trang:** 300
- **Phương pháp lấy mẫu:** Stratified sampling (lấy mẫu phân tầng)

## Danh sách Tài liệu

| Document ID | Tên file PDF | Lĩnh vực | Số mẫu |
|---|---|---|---:|
| DOC01 | DOC01_C++23_Working_Draft.pdf | Programming Language Specification | 20 |
| DOC02 | DOC02_Python_Tutorial.pdf | Programming Tutorial | 20 |
| DOC03 | DOC03_The_Java_Language_Java_SE_26_Edition.pdf | Programming Language Specification | 20 |
| DOC04 | DOC04_Mathematics_for_Computer_Science.pdf | Computer Science Mathematics | 20 |
| DOC05 | DOC05_Security_Engineering_Explained.pdf | Security Engineering | 20 |

## Ứng viên Parser

| Parser | Mô tả | Trạng thái cài đặt | Trạng thái thực thi |
|---|---|---|---|
| MinerU | AI-powered PDF parser với khả năng hiểu layout | NOT_INSTALLED | NOT_EXECUTED |
| Docling | Thư viện hiểu tài liệu từ IBM | NOT_INSTALLED | NOT_EXECUTED |
| PyMuPDF | Python bindings cho thư viện MuPDF | NOT_INSTALLED | NOT_EXECUTED |

## Chỉ số Đánh giá

| Chỉ số | Trọng số | Mô tả |
|---|---:|---|
| Text Accuracy | 20% | Độ chính xác của nội dung văn bản được trích xuất |
| Content Completeness | 15% | Tính đầy đủ của nội dung được trích xuất |
| Reading Order | 10% | Độ chính xác của thứ tự đọc |
| Heading Detection | 10% | Độ chính xác của việc phát hiện tiêu đề |
| Table Extraction | 15% | Độ chính xác của việc trích xuất bảng |
| Code Preservation | 10% | Bảo toàn định dạng code |
| Formula Preservation | 10% | Bảo toàn công thức toán học |
| Layout Preservation | 10% | Bảo toàn layout tài liệu |

**Tổng trọng số:** 100%

## Phân phối Lấy mẫu

Mỗi tài liệu được lấy mẫu theo phương pháp phân tầng (stratified sampling):

- **Phần đầu (First Third):** 6 mẫu
- **Phần giữa (Middle Third):** 8 mẫu
- **Phần cuối (Final Third):** 6 mẫu

## Loại Trang

Các loại trang được phân loại:

- TEXT
- CODE
- TABLE
- EQUATION
- FIGURE
- HEADING
- MIXED

## Xếp hạng Mô phỏng

**CẢNH BÁO:** `SIMULATED_RANKING_NOT_EMPIRICAL`

Xếp hạng này dựa trên giả định mô phỏng, không phải kết quả thực nghiệm. Không sử dụng xếp hạng này để ra quyết định chọn parser thực tế.

## Tệp Dữ liệu

- **Ground Truth:** `data/04_benchmark/synthetic_ground_truth.csv`
- **Parser Results:** `data/04_benchmark/synthetic_parser_results.csv`
- **Benchmark Results:** `data/04_benchmark/benchmark_results.csv`
- **Processing Times:** `data/04_benchmark/processing_times.csv`
- **Resource Usage:** `data/04_benchmark/resource_usage.csv`

## Thời gian và Tài nguyên

- **Processing Times:** Thời gian xử lý giả định cho mỗi parser trên mỗi tài liệu
- **Resource Usage:** Sử dụng CPU, RAM, GPU giả định

## Cảnh báo Quan trọng

Tất cả dữ liệu trong báo cáo này là **tự tạo (synthetic)** và chỉ phục vụ mục đích:

1. Testing workflow báo cáo
2. Demo cấu trúc benchmark
3. Xác định định dạng dữ liệu mong muốn
4. Chuẩn bị cho benchmark thực tế trong tương lai

**Không sử dụng dữ liệu này để:**
- Chọn parser cho sản xuất
- So sánh hiệu năng thực tế
- Ra quyết định kỹ thuật
- Công bố kết quả nghiên cứu

## Bước Tiếp theo

Để chuyển từ dữ liệu tự tạo sang benchmark thực tế:

1. Cài đặt các parser: MinerU, Docling, PyMuPDF
2. Thực thi parsing trên các tài liệu PDF gốc
3. Tạo ground truth thực tế bằng cách kiểm tra thủ công
4. Đo đạc các chỉ số thực tế
5. Thu thập thời gian xử lý và sử dụng tài nguyên thực tế
6. Thay thế dữ liệu tự tạo bằng dữ liệu thực nghiệm

---

**Ngày tạo:** 2026-11-04
**Phiên bản:** 1.0.0

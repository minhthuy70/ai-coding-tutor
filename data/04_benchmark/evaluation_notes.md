# Ghi chú Đánh giá Benchmark

## ⚠️ QUAN TRỌNG: DỮ LIỆU TỰ TẠO (SYNTHETIC)

**TÊN NHÃN SIMULATION:** `SIMULATED_DATA`
**TRẠNG THÁI THỰC THI:** `NOT_EXECUTED`
**TRẠNG THÁI DỮ LIỆU:** `SYNTHETIC_ONLY`

---

## Tổng quan

Bài ghi chú này document quá trình tạo và đánh giá tập dữ liệu benchmark tự tạo (synthetic).

## Mục đích

Tập dữ liệu này được tạo với mục đích:

1. **Demonstration:** Demo workflow và cấu trúc benchmark
2. **Testing:** Test quy trình báo cáo và aggregation
3. **Preparation:** Chuẩn bị format và cấu trúc cho benchmark thực tế
4. **Validation:** Validate cấu trúc dữ liệu và workflow

## Giả định Mô phỏng

### Giả định về Parser Performance

Điểm số parser được tạo dựa trên các giả định:

- **MinerU:** Giả định mạnh trên layout phức tạp, bảng, công thức (base score: 85)
- **Docling:** Giả định mạnh trên văn bản và code (base score: 88)
- **PyMuPDF:** Giả định mạnh trên layout đơn giản, tốc độ nhanh (base score: 78)

### Giả định về Page Type

Các loại trang được phân loại giả định:

- **TEXT:** Trang chủ yếu chứa văn bản
- **CODE:** Trang chứa code snippet
- **TABLE:** Trang chứa bảng
- **EQUATION:** Trang chứa công thức toán học
- **FIGURE:** Trang chứa hình ảnh/diagram
- **HEADING:** Trang chủ yếu là tiêu đề
- **MIXED:** Trang kết hợp nhiều loại nội dung

### Giả định về Complexity

Độ phức tạp được phân loại giả định:

- **LOW:** Nội dung đơn giản, layout rõ ràng
- **MEDIUM:** Layout vừa phải, nội dung trung bình
- **HIGH:** Layout phức tạp, nhiều thành phần
- **MIDDLE:** Chỉ số giữa LOW và HIGH

## Phương pháp Tạo Dữ liệu

### Ground Truth Synthetic

- Tạo 100 sample records (20 trên mỗi tài liệu)
- Sử dụng stratified sampling (6-8-6 phân phối)
- Gán page type giả định dựa trên vị trí trong tài liệu
- Gán complexity giả định dựa trên page type
- Không sử dụng số trang PDF thực tế

### Parser Results Synthetic

- Tạo 300 records (100 samples × 3 parsers)
- Base score theo parser
- Điều chỉnh theo page type và complexity
- Thêm random variation (±5 điểm)
- Tính weighted score theo trọng số metric

### Processing Times Synthetic

- Base time theo parser (MinerU: 45s, Docling: 35s, PyMuPDF: 25s)
- Điều chỉnh theo document và random factor
- Không có đo đạc thực tế

### Resource Usage Synthetic

- Base CPU/RAM/GPU theo parser
- Thêm random variation
- Không có đo đạc thực tế

## Hạn chế

### Không có Thực thi Thực tế

- Không parser nào được cài đặt
- Không có parsing PDF thực tế
- Không có output parser thực tế

### Không có Ground Truth Thực tế

- Không có kiểm tra thủ công PDF gốc
- Không có transcription thực tế
- Không có verification bởi reviewer

### Không có Đo đạc Thực tế

- Không có đo thời gian thực tế
- Không có đo tài nguyên thực tế
- Không có profiling

### Dữ liệu Giả định

- Tất cả điểm số là giả định
- Không có cơ sở thực nghiệm
- Không thể tổng quát hóa

## Quy trình Đánh giá (cho Benchmark Thực tế)

Khi thực hiện benchmark thực tế, quy trình đánh giá sẽ như sau:

### 1. Cài đặt Parser

- Cài đặt MinerU, Docling, PyMuPDF
- Cấu hình theo tài liệu
- Test trên sample đơn giản

### 2. Thực thi Parsing

- Chạy từng parser trên 5 tài liệu PDF
- Lưu output theo cấu trúc chuẩn
- Document lỗi và warning

### 3. Tạo Ground Truth

- Mở PDF gốc
- Chọn 20 trang mẫu theo stratified sampling
- Chép thủ công nội dung chính xác
- Phân loại page type
- Ghi độ phức tạp
- Xác minh bởi reviewer

### 4. Đánh giá Chỉ số

- So sánh output parser với ground truth
- Tính toán accuracy từng metric
- Document lỗi cụ thể
- Phân tích pattern lỗi

### 5. Đo đạc Hiệu năng

- Đo thời gian xử lý
- Đo sử dụng CPU/RAM/GPU
- Lặp 3 lần cho độ tin cậy
- Tính thống kê

### 6. Phân tích Kết quả

- Tổng hợp kết quả
- So sánh parser
- Phân tích trade-off
- Ra quyết định

## Tiêu chí Đánh giá Chất lượng

### Text Accuracy

- So sánh từng character/word
- Tính Levenshtein distance
- Báo cáo % match

### Content Completeness

- Đếm số lượng elements
- So sánh với ground truth
- Báo cáo % elements trích xuất

### Reading Order

- So sánh thứ tự blocks
- Kiểm tra sự hợp lý
- Báo cáo % order chính xác

### Heading Detection

- So sánh heading text
- Kiểm tra level hierarchy
- Báo cáo % heading phát hiện

### Table Extraction

- So sánh số rows/columns
- Kiểm tra cell content
- Báo cáo % cells chính xác

### Code Preservation

- So sánh code character
- Kiểm tra indentation
- Kiểm tra special characters
- Báo cáo % code chính xác

### Formula Preservation

- So sánh LaTeX notation
- Kiểm tra symbols
- Báo cáo % formula chính xác

### Layout Preservation

- So sánh vị trí elements
- Kiểm tra spacing
- Báo cáo % layout chính xác

## Công cụ Đánh giá Đề xuất

### Công cụ tự động

- Difflib cho text comparison
- Levenshtein distance
- Regular expressions cho code
- LaTeX parser cho formulas

### Công cụ thủ công

- Visual inspection
- Side-by-side comparison
- Reviewer checklist

## Lưu ý cho Future Benchmark

### Mở rộng Dataset

- Thêm nhiều tài liệu hơn
- Đa dạng hóa domain
- Thêm page types khác
- Tăng số samples

### Cải thiện Metrics

- Thêm metrics mới (image extraction, OCR accuracy)
- Tinh trọng số metric
- Thêm domain-specific metrics

### Automation

- Tự động hóa ground truth creation
- Tự động hóa evaluation
- CI/CD pipeline cho benchmark

## Bước Tiếp theo

1. Review dataset tự tạo hiện tại
2. Validate cấu trúc và format
3. Cài đặt parsers thực tế
4. Thực hiện benchmark thực tế
5. Thay thế dữ liệu tự tạo bằng dữ liệu thực tế

---

**Ngày tạo:** 2026-11-04
**Phiên bản:** 1.0.0
**Trạng thái:** `SYNTHETIC_DATA_ONLY`

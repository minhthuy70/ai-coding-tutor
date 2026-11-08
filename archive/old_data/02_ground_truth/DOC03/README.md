# Ground Truth - DOC03

## Document information

- Document ID: DOC03
- PDF filename:
- Total pages:
- Selected pages: 20
- Sampling method: Stratified sampling
- Review status: Not started

## Sampling distribution

- First third: 6 pages
- Middle third: 8 pages
- Final third: 6 pages

## Notes

Ground Truth must be manually verified against the original PDF.
Do not use parser output as the reference answer.

## ⚠️ Synthetic Data Warning

**TRẠNG THÁI:** `SYNTHETIC_ONLY`

Ground truth hiện tại là dữ liệu tự tạo (synthetic) cho mục đích demonstration và testing workflow.
- Không có kiểm tra thủ công đối với PDF gốc
- Không có transcription thực tế
- synthetic_page_manifest.csv chứa giả định về page type và complexity
- Không có số trang PDF thực tế được gán

Để tạo ground truth thực tế:
1. Mở file PDF gốc: DOC03_The_Java_Language_Java_SE_26_Edition.pdf
2. Chọn 20 trang mẫu theo stratified sampling
3. Chép thủ công nội dung chính xác vào các file trong thư mục pages/
4. Cập nhật synthetic_page_manifest.csv với thông tin thực tế
5. Xác minh bởi reviewer

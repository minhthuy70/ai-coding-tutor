# BÁO CÁO KIỂM TRA & NHẬT KÝ ĐỒNG BỘ THEO MASTER RULES
### Nền tảng AI-Powered Coding Tutor & Auto-Grader

---

## 1. TỔNG QUAN ĐỐI SOÁT (AUDIT SUMMARY)

Toàn bộ các tài liệu trong dự án (`RULES.md`, `nopbai.md`, `DOAN4.md`, `docs/02_ACTORS_AND_USE_CASES.md`, `docs/03_USE_CASE_FLOWS.md`, `docs/USE_CASE_DIAGRAMS.md`) đã được rà soát và cập nhật đồng bộ 100% theo đúng **MASTER RULES** (56 điều khoản) cùng các yêu cầu chuẩn hóa mới nhất:

1. **Chuẩn hóa Tên Tác nhân (Actor Names) sang Tiếng Việt:**
   - **Sinh viên**
   - **Giáo viên**
   - **Quản trị viên** (Phòng Đào tạo)
   - **Giáo vụ** (Khoa / Bộ môn)
   - **Quản trị viên hệ thống** (IT Vận hành nền tảng)
   *(Loại bỏ hoàn toàn các thuật ngữ tiếng Anh như Student, Teacher, Admin, Staff, SuperAdmin trong toàn bộ tài liệu, ma trận và sơ đồ Use Case).*

2. **Cập nhật danh mục và tên Use Case:**
   - **UC-10:** Đổi tên thành **"Upload file bài làm"** *(Phân hệ Sinh viên)*.
   - **UC-17 (Tạo lớp học của Giáo viên):** **XÓA BỎ.** Chức năng tạo lớp tập trung ở cấp Quản trị viên / Giáo vụ trong UC-38.
   - **UC-18 (Chỉnh sửa lớp của Giáo viên):** **XÓA BỎ.** Chức năng chỉnh sửa lớp tập trung ở cấp Quản trị viên / Giáo vụ trong UC-39.
   - **UC-19 (Đóng/Mở lớp của Giáo viên):** **XÓA BỎ.** Chức năng đóng/mở lớp được thực hiện trong UC-40.
   - **UC-20 (Quản lý sinh viên của Giáo viên):** **XÓA BỎ.** Chức năng quản lý sinh viên trong lớp tập trung ở cấp Quản trị viên / Giáo vụ trong UC-42.
   - **UC-21:** Đổi tên từ *"Quản lý/ Cấu hình bài tập"* thành **"Tạo bài tập"** *(Phân hệ Giáo viên)*.

---

## 2. BẢNG ĐỐI CHIẾU THAY ĐỔI THEO MASTER RULES

| STT | Nội dung / Chức năng | Logic cũ (Bị hủy bỏ) | Logic mới đã cập nhật theo MASTER RULES |
| :---: | :--- | :--- | :--- |
| **1** | **Chạy thử mã nguồn của Sinh viên** | Sinh viên được bấm nút "Chạy thử" (Run Code) trên 1–2 Sample Test Cases trong thời gian làm bài. | **BỎ HOÀN TOÀN.** Sinh viên **không được chạy thử code trên Sample Test Cases**. Không có nút Run Code. Việc thực thi code chỉ diễn ra sau Deadline trong Batch Grading bằng Docker Sandbox. |
| **2** | **Quy tắc Nộp bài & Giới hạn lượt nộp** | Tồn tại `Max Submissions`, `submission_count`, lượt nộp tối đa, chế độ unlimited attempts. | **BỎ HOÀN TOÀN.** Không còn Max Submissions, không đếm attempt. Mỗi Sinh viên chỉ có **1 bản nộp chính thức duy nhất** cho mỗi bài tập. |
| **3** | **Chính sách tính điểm** | Có chính sách `Highest Score` / `Latest Score` giữa nhiều lần nộp. | **BỎ HOÀN TOÀN.** Mỗi bài tập chỉ có 1 bản nộp duy nhất nên không còn so sánh điểm giữa các lần nộp. |
| **4** | **Nộp muộn (Late Submission)** | Hỗ trợ nộp muộn trong Late Window kèm trừ điểm phạt (Late Penalty). | **BỎ HOÀN TOÀN.** Áp dụng **Strict No-Late Submission**. Đến Deadline là đóng hoàn toàn, Backend chặn request gửi code (403 Forbidden / Assignment Closed), Editor bị khóa Read-only. |
| **5** | **Thời điểm chấm bài & Auto-Grader** | Sinh viên nộp $\rightarrow$ Đưa vào Queue $\rightarrow$ Chấm Auto-Grader và AI ngay lập tức. | **BỎ HOÀN TOÀN.** Nộp bài (Explicit Submit hoặc Auto-submit) chỉ chuyển trạng thái sang `SUBMITTED` và bị khóa Read-only. Chờ đến sau Deadline mới chốt danh sách và kích hoạt **Batch Grading** (Chấm gom tập trung). |
| **6** | **Chỉnh sửa sau khi nộp bài** | Có cấu hình "Cho phép chỉnh sửa sau khi nộp = Có/Không". | **BỎ HOÀN TOÀN.** Nộp bài (hoặc hết giờ Auto-submit) là bài làm bị **khóa vĩnh viễn (Read-only)**, không thể sửa, upload hay nộp lại dưới bất kỳ hình thức nào. |
| **7** | **Cơ chế Auto-submit tại Deadline** | Auto-submit dựa vào trình duyệt / client. | **Backend Worker / Cron Job** tự động quét các bài còn ở `DRAFT`, lấy bản Autosave/Save mới nhất trên database/cache để chuyển thành `SUBMITTED` với `trigger_type = AUTO_EXPIRED`. Không phụ thuộc mạng hay máy của sinh viên. |
| **8** | **AI Tutor trong lúc làm bài** | AI Tutor hỗ trợ gợi ý Socratic ngay khi sinh viên đang viết code trong Editor. | **BỎ HOÀN TOÀN.** AI Tutor **chỉ là chức năng hậu kiểm sau đánh giá** (sau khi đã có kết quả/điểm). Không được dùng trong giai đoạn `DRAFT`. |
| **9** | **Xác nhận Điểm chính thức** | Điểm số tự động có thể coi là điểm chính thức; AI có thể tính điểm. | **Điểm chính thức do Giáo viên xác nhận (Teacher Score $\rightarrow$ Official Score).** Auto-Grader và AI chỉ là kết quả tự động hỗ trợ/tham khảo. |
| **10** | **Quản trị viên hệ thống (IT)** | Quản trị viên hệ thống tham gia quản lý lớp (UC-40, UC-41, UC-42, UC-43, UC-47). | **BỎ HOÀN TOÀN.** Quản trị viên hệ thống **chỉ phụ trách kỹ thuật nền tảng** (UC-44 AI Config, UC-45 Docker Config, UC-46 Docker Monitor, UC-48 System Logs, UC-35 cấp quyền hệ thống). **Không tham gia** UC-38 $\rightarrow$ UC-43 và UC-47. |
| **11** | **Quản lý tổ chức (UC-47)** | Actor: Quản trị viên hệ thống & Quản trị viên. | **Actor chỉ là Quản trị viên (Phòng Đào tạo).** Quản lý Tổ chức, Khoa/Bộ môn và phân công Giáo vụ. |
| **12** | **Quản lý lớp cấp Giáo viên (UC-17, 18, 20)** | Giáo viên tạo lớp, sửa lớp, quản lý SV trong lớp riêng biệt. | **XÓA BỎ.** Quản lý lớp tập trung ở cấp Quản trị viên / Giáo vụ (UC-38, UC-39, UC-42). Giáo viên chỉ đóng/mở lớp phụ trách (UC-40). |
| **13** | **Điều kiện Hard Delete lớp (UC-41)** | Xóa lớp có thể chỉ kiểm tra sinh viên và bài tập. | Phải thỏa mãn đồng thời: `student_count = 0` AND `assignment_count = 0` AND `schedule_count = 0` (0 SV, 0 bài tập, 0 lịch học). Không thỏa $\rightarrow$ Chặn xóa $\rightarrow$ Chuyển Archive. |
| **14** | **Trạng thái khi Restore lớp (UC-41)** | Restore có thể mở lại lớp. | Restore lớp từ `Lưu trữ` $\rightarrow$ `Đã đóng`. Muốn hoạt động lại phải qua bước Mở lại lớp (UC-40). |
| **15** | **Ranh giới cấu hình bài tập** | UC-21 chứa cấu hình nộp muộn, max submissions, highest score. | UC-21 đổi tên thành "Tạo bài tập" (chỉ tạo bài & cấu hình ban đầu); UC-22 chỉ sửa thông tin chung; UC-24 chỉ sửa Deadline; UC-25 chỉ sửa Test Cases; UC-26 chỉ sửa Rubric; UC-27 chỉ giao bài cho lớp. |

---

## 3. DANH SÁCH CÁC TỆP ĐÃ ĐỒNG BỘ TRONG REPOSITORY

1. [RULES.md](file:///d:/GITHUB/ai-coding-tutor/RULES.md)
   - Cập nhật định danh toàn bộ Actor sang Tiếng Việt.
   - Ghi nhận việc xóa bỏ UC-17, UC-18, UC-19, UC-20 và đổi tên UC-10 ("Upload file bài làm"), UC-21 ("Tạo bài tập").
   - Giữ vững 56 điều khoản MASTER RULES làm Source of Truth duy nhất.

2. [DOAN4.md](file:///d:/GITHUB/ai-coding-tutor/DOAN4.md)
   - Cập nhật toàn bộ bảng đặc tả Use Case.
   - Đổi tên UC-10 thành "Upload file bài làm".
   - Đánh dấu đã xóa bỏ UC-17, UC-18, UC-19, UC-20.
   - Đổi tên UC-21 thành "Tạo bài tập".
   - Chuẩn hóa tác nhân Tiếng Việt và cấu trúc 9 phần (Luồng chính đánh số từng dòng).

3. [docs/02_ACTORS_AND_USE_CASES.md](file:///d:/GITHUB/ai-coding-tutor/docs/02_ACTORS_AND_USE_CASES.md)
   - Cập nhật ma trận RBAC với tên tác nhân Tiếng Việt.
   - Cập nhật bảng tổng hợp Use Case với UC-10 mới, UC-21 mới và loại bỏ UC-17, 18, 19, 20.

4. [docs/03_USE_CASE_FLOWS.md](file:///d:/GITHUB/ai-coding-tutor/docs/03_USE_CASE_FLOWS.md)
   - Cập nhật chi tiết luồng thực hiện của từng UC theo các thay đổi mới nhất.

5. [docs/USE_CASE_DIAGRAMS.md](file:///d:/GITHUB/ai-coding-tutor/docs/USE_CASE_DIAGRAMS.md)
   - Chuẩn hóa toàn bộ tên tác nhân trong sơ đồ Mermaid và PlantUML sang Tiếng Việt.
   - Cập nhật UC-10, UC-21 và loại bỏ UC-17, 18, 20 khỏi sơ đồ phân hệ Giáo viên.

6. [nopbai.md](file:///d:/GITHUB/ai-coding-tutor/nopbai.md)
   - Quy định rõ ràng chu trình DRAFT (Upload file bài làm/Autosave/Save - không chạy thử) $\rightarrow$ SUBMITTED $\rightarrow$ GRADING (Batch Grading sau Deadline) $\rightarrow$ COMPLETED $\rightarrow$ Điểm chính thức do Giáo viên xác nhận.

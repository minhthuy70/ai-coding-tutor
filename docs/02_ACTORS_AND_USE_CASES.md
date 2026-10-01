# 02. ĐẶC TẢ TÁC NHÂN (ACTORS) & DANH MỤC USE CASES (UC)

---

## 1. MÔ HÌNH PHÂN QUYỀN (RBAC MATRIX)

Hệ thống được thiết kế theo mô hình **Role-Based Access Control (RBAC)** với 5 nhóm Tác nhân (Actor) chính:

| Tác nhân | Cấp độ quản trị | Phạm vi dữ liệu truy cập |
| :--- | :--- | :--- |
| **Sinh viên** | Người học (End-user) | Chỉ xem được lớp mình tham gia, bài tập được giao, bài làm và điểm của chính mình; tương tác AI Tutor hậu kiểm sau đánh giá. **Không có quyền chạy thử code trên Sample Test Cases.** |
| **Giáo viên** | Giảng viên | Đóng/mở lớp được phân công phụ trách, tạo/cấu hình bài tập, giao bài, chấm điểm thủ công, xác nhận điểm chính thức và xem toàn bộ bài nộp của học viên trong lớp. |
| **Quản trị viên** | Quản trị Nghiệp vụ Đào tạo (Toàn trường) | Quản lý tài khoản (Sinh viên/Giáo viên/Giáo vụ), quản lý lớp toàn trường (Tạo, Sửa, Đóng/Mở, Archive/Restore/Hard Delete), phân công giảng viên, quản lý cơ cấu tổ chức/Khoa/Bộ môn và phân công Giáo vụ. |
| **Giáo vụ** | Hành chính Khoa/Bộ môn | Quản lý lớp, sinh viên trong lớp và phân công giáo viên trong phạm vi Khoa/Bộ môn được phân công phụ trách. |
| **Quản trị viên hệ thống** | Quản trị Kỹ thuật Nền tảng (IT) | Quản lý cấu hình hạ tầng, AI Engine (API Key, Model), Docker Sandbox, giám sát hệ thống và System Logs. **Không quản lý nghiệp vụ lớp học hay đào tạo.** |

---

## 2. MA TRẬN PHÂN QUYỀN CHỨC NĂNG

| Nhóm Chức Năng | Sinh viên | Giáo viên | Quản trị viên | Giáo vụ | Quản trị viên hệ thống |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Đăng nhập / Đăng xuất / Quên & Đổi mật khẩu | ✅ | ✅ | ✅ | ✅ | ✅ |
| Xem & Cập nhật thông tin cá nhân | ✅ | ✅ | ✅ | ✅ | ✅ |
| Viết code, Autosave nháp & Nộp bài chính thức | ✅ | ❌ | ❌ | ❌ | ❌ |
| Tương tác AI Tutor hậu kiểm sau đánh giá | ✅ | ❌ | ❌ | ❌ | ❌ |
| Xem bài đã nộp & Bảng điểm cá nhân | ✅ | ❌ | ❌ | ❌ | ❌ |
| Tạo/Sửa/Xóa bài tập & Thiết lập Test case / Rubric | ❌ | ✅ | ❌ | ❌ | ❌ |
| Giao bài tập cho lớp & Đặt Deadline | ❌ | ✅ | ❌ | ❌ | ❌ |
| Xem bài nộp, Chấm thủ công & Xác nhận điểm chính thức | ❌ | ✅ | ❌ | ❌ | ❌ |
| Đóng/Mở lại lớp học | ❌ | ✅ (lớp phụ trách) | ✅ (toàn trường) | ✅ (Khoa/Bộ môn) | ❌ |
| Quản lý tài khoản (Tạo, Khóa, Xóa, Phân quyền, Đặt lại MK) | ❌ | ❌ | ✅ (SV/GV/Giáo vụ) | ❌ | ✅ (Cấp hệ thống) |
| Import danh sách người dùng từ Excel/CSV (5 cột) | ❌ | ❌ | ✅ | ❌ | ❌ |
| Quản lý lớp cấp quản trị (Tạo, Sửa, Đóng/Mở) | ❌ | ❌ | ✅ (toàn trường) | ✅ (Khoa/Bộ môn) | ❌ |
| Lưu trữ & Xóa lớp học (Archive/Restore/Hard Delete) | ❌ | ❌ | ✅ (toàn trường) | ✅ (Khoa/Bộ môn) | ❌ |
| Quản lý sinh viên trong lớp (cấp quản trị) | ❌ | ❌ | ✅ (toàn trường) | ✅ (Khoa/Bộ môn) | ❌ |
| Phân công giảng viên vào lớp | ❌ | ❌ | ✅ (toàn trường) | ✅ (Khoa/Bộ môn) | ❌ |
| Quản lý tổ chức, Khoa/Bộ môn & Phân công Giáo vụ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Cấu hình AI Engine (API Key, Model, Timeout) | ❌ | ❌ | ❌ | ❌ | ✅ |
| Cấu hình & Giám sát Docker Sandbox | ❌ | ❌ | ❌ | ❌ | ✅ |
| Quản lý System Logs | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## 3. DANH MỤC CHI TIẾT CÁC USE CASE

### 3.1. Các Use Case Xác Thực & Quản Lý Tài Khoản Chung (6 UC)
| Mã UC | Tên Use Case | Tác nhân | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- |
| **UC-01** | Đăng nhập | Tất cả tác nhân | Xác thực tài khoản bằng Email và Mật khẩu, cấp JWT token (access/refresh). Bắt buộc đổi mật khẩu nếu dùng mật khẩu tạm. |
| **UC-02** | Đăng xuất | Tất cả tác nhân | Kết thúc phiên làm việc, thu hồi refresh_token và xóa token trên client. |
| **UC-03** | Quên mật khẩu | Tất cả tác nhân | Gửi mã OTP/Link xác thực qua email để đặt lại mật khẩu mới. Vô hiệu hóa mã/link sau khi sử dụng. |
| **UC-04** | Xem thông tin cá nhân | Tất cả tác nhân | Hiển thị hồ sơ: Họ tên, Email, Số điện thoại, Ảnh đại diện, Vai trò. |
| **UC-05** | Cập nhật thông tin cá nhân | Tất cả tác nhân | Cho phép cập nhật họ tên, số điện thoại, ảnh đại diện. |
| **UC-06** | Đổi mật khẩu | Tất cả tác nhân | Thay đổi mật khẩu tài khoản sau khi xác thực mật khẩu hiện tại. Mật khẩu mới phải khác mật khẩu cũ. |

---

### 3.2. Phân Hệ Sinh Viên (10 Use Cases)
| Mã UC | Tên Use Case | Tác nhân | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- |
| **UC-07** | Xem danh sách bài tập | Sinh viên | Xem danh sách bài tập được giao theo lớp, hiển thị Deadline, trạng thái (DRAFT, SUBMITTED, GRADING, COMPLETED) và điểm chính thức nếu có. |
| **UC-08** | Xem chi tiết bài tập | Sinh viên | Xem đề bài (Markdown/LaTeX), yêu cầu I/O, ràng buộc, Time/Memory Limit, Sample Test Cases và Rubric. |
| **UC-09** | Viết code | Sinh viên | Soạn thảo mã nguồn trên Monaco Editor với Autosave/Save lưu vào bản nháp `DRAFT`. Không có chức năng chạy thử trên Sample Tests. |
| **UC-10** | Upload file bài làm | Sinh viên | Nạp file mã nguồn từ máy tính vào editor và lưu vào `DRAFT`. Không tạo Submission. |
| **UC-11** | Nộp bài | Sinh viên, Hệ thống | Explicit Submit với popup xác nhận cảnh báo $\rightarrow$ chuyển sang `SUBMITTED`, `trigger_type = MANUAL`, khóa Read-only. Auto-submit khi hết giờ lấy bản draft mới nhất $\rightarrow$ `SUBMITTED`, `trigger_type = AUTO_EXPIRED`. Strict No-Late sau Deadline. Chờ Batch Grading sau Deadline. |
| **UC-12** | Xem kết quả Auto-Grader | Sinh viên | Xem kết quả kiểm thử sau Batch Grading (COMPLETED): điểm Auto-Grader, trạng thái test cases (Input/Output của Hidden Test Cases được bảo mật). |
| **UC-13** | Xem nhận xét AI | Sinh viên | Xem phản hồi AI Review về Code Quality, Complexity, Code Style, giải thích lỗi và đề xuất cải thiện. |
| **UC-14** | Tương tác với AI Tutor | Sinh viên | Tương tác hậu kiểm sau đánh giá theo phương pháp Socratic (hỏi mở, định hướng, không đưa code giải sẵn). Context: Đề bài, code nộp cuối, kết quả Auto-Grader, AI Review, nhận xét GV, điểm chính thức. |
| **UC-15** | Xem bài đã nộp | Sinh viên | Xem bản nộp chính thức duy nhất của mình cho bài tập (mã nguồn, thời điểm nộp, trigger_type, trạng thái). |
| **UC-16** | Xem bảng điểm cá nhân | Sinh viên | Tổng hợp điểm các bài tập và lớp học. Điểm chính thức do Giáo viên xác nhận; điểm Auto-Grader tạm tính khi chưa có điểm GV. |

---

### 3.3. Phân Hệ Giáo Viên (11 Use Cases Hoạt Động)

> **Lưu ý**: Các UC-17, UC-18, UC-19, UC-20 đã bị hủy bỏ hoàn toàn. Việc tạo/chỉnh sửa lớp và quản lý sinh viên được quản lý tập trung ở cấp Quản trị viên / Giáo vụ (UC-38, UC-39, UC-42).

| Mã UC | Tên Use Case | Tác nhân | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- |
| **UC-17** | *(ĐÃ BỊ HỦY BỎ)* | - | Đã bỏ chức năng tạo lớp ở cấp Giáo viên $\rightarrow$ chuyển sang UC-38. |
| **UC-18** | *(ĐÃ BỊ HỦY BỎ)* | - | Đã bỏ chức năng sửa lớp ở cấp Giáo viên $\rightarrow$ chuyển sang UC-39. |
| **UC-19** | *(ĐÃ BỊ HỦY BỎ)* | - | Đã bỏ để tránh trùng lặp $\rightarrow$ chuyển sang UC-40 và UC-41. |
| **UC-20** | *(ĐÃ BỊ HỦY BỎ)* | - | Đã bỏ chức năng quản lý sinh viên ở cấp Giáo viên $\rightarrow$ chuyển sang UC-42. |
| **UC-21** | Tạo bài tập | Giáo viên | Tạo bài tập mới và cấu hình ban đầu: Tên bài, đề bài, ngôn ngữ, độ khó, Time/Memory Limit, Deadline ban đầu. |
| **UC-22** | Chỉnh sửa thông tin chung bài tập | Giáo viên | Cập nhật Tên, Đề bài, Ngôn ngữ, Độ khó, Giới hạn tài nguyên. Không sửa Deadline, Test Case, Rubric. |
| **UC-23** | Xóa bài tập | Giáo viên | Xóa mềm / vô hiệu hóa bài tập để bảo toàn dữ liệu học tập. |
| **UC-24** | Thiết lập hạn nộp bài | Giáo viên | Thiết lập / điều chỉnh Deadline kết thúc nhận bài. |
| **UC-25** | Thiết lập test case | Giáo viên | Quản lý bộ Test Cases (Sample/Hidden, Input, Output, Trọng số điểm). Sample Test Cases không dùng để chạy thử cho SV. |
| **UC-26** | Thiết lập rubric | Giáo viên | Cấu hình tiêu chí và trọng số điểm. Correctness do hệ thống tự tính từ Hidden Test Cases. Tổng trọng số = 100%. |
| **UC-27** | Giao bài tập cho lớp | Giáo viên | Giao bài tập cho một hoặc nhiều lớp phụ trách (lớp đang Hoạt động). |
| **UC-28** | Xem bài nộp | Giáo viên | Xem bản nộp chính thức duy nhất của từng sinh viên cho bài tập. |
| **UC-29** | Xem điểm | Giáo viên | Xem bảng điểm của lớp phụ trách theo từng bài tập và tiêu chí Rubric. |
| **UC-30** | Xem AI đánh giá | Giáo viên | Xem phân tích AI Review (Code Quality, Complexity, Style) và kết quả đối soát trùng lặp/đạo văn. |
| **UC-31** | Đánh giá / chấm bài thủ công | Giáo viên | Đánh giá theo Rubric, nhập/chỉnh điểm, nhập nhận xét và xác nhận Điểm chính thức (Official Score). |

---

### 3.4. Phân Hệ Quản Trị Viên & Giáo Vụ (12 Use Cases)
| Mã UC | Tên Use Case | Tác nhân | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- |
| **UC-32** | Tạo tài khoản người dùng | Quản trị viên | Tạo tài khoản SV/GV/Giáo vụ; sinh mật khẩu tạm, bắt buộc đổi lần đầu, gửi email. |
| **UC-33** | Khóa/mở tài khoản | Quản trị viên | Khóa/mở khóa tài khoản; thu hồi toàn bộ active sessions khi khóa. |
| **UC-34** | Xóa tài khoản | Quản trị viên | Xóa tài khoản; áp dụng Soft Delete nếu có dữ liệu học tập liên quan. |
| **UC-35** | Phân quyền người dùng | Quản trị viên, Quản trị viên hệ thống | Quản trị viên phân quyền SV/GV/Giáo vụ; Quản trị viên hệ thống phân quyền cấp hệ thống. |
| **UC-36** | Đặt lại mật khẩu | Quản trị viên | Sinh mật khẩu tạm ngẫu nhiên, gửi email, bắt buộc đổi lần đầu, thu hồi active sessions. |
| **UC-37** | Nhập danh sách từ Excel/CSV | Quản trị viên | Import người dùng từ file đúng 5 cột quy định; xem trước và báo lỗi từng dòng. |
| **UC-38** | Tạo lớp | Quản trị viên, Giáo vụ | Quản trị viên tạo lớp toàn trường; Giáo vụ tạo lớp trong phạm vi Khoa/Bộ môn phụ trách. |
| **UC-39** | Chỉnh sửa lớp | Quản trị viên, Giáo vụ | Quản trị viên chỉnh sửa mọi lớp; Giáo vụ chỉnh sửa lớp thuộc Khoa/Bộ môn phụ trách (lớp đang Hoạt động). |
| **UC-40** | Đóng/Mở lại lớp học | Giáo viên, Quản trị viên, Giáo vụ | Chuyển đổi trạng thái giữa Hoạt động và Đã đóng theo phạm vi quyền. |
| **UC-41** | Quản lý Lưu trữ & Xóa lớp học | Quản trị viên, Giáo vụ | Archive (Đã đóng $\rightarrow$ Lưu trữ), Restore (Lưu trữ $\rightarrow$ Đã đóng), Hard Delete (chỉ khi 0 SV + 0 bài + 0 lịch học; không đạt $\rightarrow$ chuyển Archive). |
| **UC-42** | Quản lý sinh viên trong lớp | Quản trị viên, Giáo vụ | Thêm/Xóa/Xem sinh viên trong lớp cấp quản trị theo phạm vi quyền. Lớp phải đang Hoạt động. |
| **UC-43** | Phân công Giáo viên vào lớp | Quản trị viên, Giáo vụ | Phân công/Hủy phân công GV cho lớp. Giáo vụ chỉ thao tác trong Khoa/Bộ môn phụ trách. |
| **UC-47** | Quản lý tổ chức | Quản trị viên | Quản lý tổ chức, Khoa/Bộ môn trực thuộc; phân công Giáo vụ phụ trách. |

---

### 3.5. Phân Hệ Quản Trị Hệ Thống (4 Use Cases Kỹ Thuật)
| Mã UC | Tên Use Case | Tác nhân | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- |
| **UC-44** | Quản lý cấu hình AI | Quản trị viên hệ thống | Thiết lập, cập nhật, kiểm tra kết nối (Test Connection) cấu hình AI (API Key, Model, Timeout). |
| **UC-45** | Cấu hình Docker Sandbox | Quản trị viên hệ thống | Cấu hình giới hạn CPU, RAM, Execution Timeout, Base Images cho môi trường thực thi cách ly. |
| **UC-46** | Giám sát Docker Sandbox | Quản trị viên hệ thống | Theo dõi realtime trạng thái container, CPU/RAM usage trong quá trình Batch Grading; xử lý sự cố. |
| **UC-48** | Quản lý System Logs | Quản trị viên hệ thống | Xem, tìm kiếm, lọc, xem chi tiết và xuất System Logs toàn hệ thống. |

# 02. ĐẶC TẢ ACTOR & DANH MỤC USE CASES (UC)

---

## 1. MÔ HÌNH PHÂN QUYỀN (RBAC MATRIX)

Hệ thống được thiết kế theo mô hình **Role-Based Access Control (RBAC)** với 5 nhóm Actor chính:

| Actor | Ký hiệu | Cấp độ quản trị | Phạm vi dữ liệu truy cập |
| :--- | :---: | :--- | :--- |
| **Sinh viên** | `SV` | Người học (End-user) | Chỉ xem được lớp mình tham gia, bài tập được giao, bài làm và điểm của chính mình. |
| **Giáo viên** | `GV` | Giảng viên | Quản lý các lớp do mình phụ trách, tạo bài tập, chấm điểm và xem toàn bộ bài nộp của học viên trong lớp. |
| **Quản trị viên** | `QTV` | Quản lý Trường / Cơ sở | Quản lý tài khoản (Sinh viên/Giáo viên/Giáo vụ), quản lý danh sách lớp, phân công giảng viên trong phạm vi tổ chức. |
| **Giáo vụ** | `GVU` | Hành chính Khoa/Bộ môn | Quản lý lớp, sinh viên và phân công giáo viên trong phạm vi Khoa/Bộ môn được phân công. |
| **Quản trị viên hệ thống** | `QTVHT` | Quản trị Hệ thống | Toàn quyền cấu hình hạ tầng, AI Engine, Docker Sandbox, giám sát hệ thống và quản lý đa tổ chức. |

---

## 2. MA TRẬN PHÂN QUYỀN CHỨC NĂNG

| Nhóm Chức Năng | Sinh viên | Giáo viên | Quản trị viên | Giáo vụ | QTVHT |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Đăng nhập / Đăng xuất / Quên & Đổi mật khẩu | ✅ | ✅ | ✅ | ✅ | ✅ |
| Xem & Cập nhật thông tin cá nhân | ✅ | ✅ | ✅ | ✅ | ✅ |
| Viết code & Nộp bài (Monaco Editor) | ✅ | ❌ | ❌ | ❌ | ❌ |
| Tương tác AI Tutor & Xem gợi ý Socratic | ✅ | ❌ | ❌ | ❌ | ❌ |
| Xem lịch sử làm bài & Bảng điểm cá nhân | ✅ | ❌ | ❌ | ❌ | ❌ |
| Tạo/Sửa/Xóa bài tập & Thiết lập Test case / Rubric | ❌ | ✅ | ❌ | ❌ | ❌ |
| Giao bài tập cho lớp & Đặt hạn nộp | ❌ | ✅ | ❌ | ❌ | ❌ |
| Quản lý lớp học (lớp phụ trách) & Sinh viên trong lớp | ❌ | ✅ | ❌ | ❌ | ❌ |
| Xem bài nộp & Chấm bài thủ công | ❌ | ✅ | ❌ | ❌ | ❌ |
| Đóng/Mở lại lớp học | ❌ | ✅ | ✅ | ✅ | ❌ |
| Quản lý tài khoản (Tạo, Khóa, Xóa, Phân quyền, Đặt lại MK) | ❌ | ❌ | ✅ | ❌ | ✅ |
| Import danh sách người dùng từ Excel/CSV | ❌ | ❌ | ✅ | ❌ | ✅ |
| Quản lý lớp cấp quản trị (toàn trường) | ❌ | ❌ | ✅ | ❌ | ✅ |
| Quản lý lớp cấp Khoa/Bộ môn | ❌ | ❌ | ❌ | ✅ | ❌ |
| Lưu trữ & Xóa lớp học | ❌ | ❌ | ✅ | ✅ | ❌ |
| Quản lý sinh viên trong lớp (cấp quản trị) | ❌ | ❌ | ✅ | ✅ | ❌ |
| Phân công giảng viên vào lớp | ❌ | ❌ | ✅ | ✅ | ❌ |
| Quản lý tổ chức & Khoa/Bộ môn | ❌ | ❌ | ✅ | ❌ | ✅ |
| Cấu hình AI Engine (API Key, Model, Temperature) | ❌ | ❌ | ❌ | ❌ | ✅ |
| Cấu hình & Giám sát Docker Sandbox | ❌ | ❌ | ❌ | ❌ | ✅ |
| Quản lý System Logs | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## 3. DANH MỤC CHI TIẾT 48 USE CASES

### 3.1. Các Use Case Xác Thực & Quản Lý Tài Khoản Chung (6 UC)
| Mã UC | Tên Use Case | Tác nhân | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- |
| **UC-01** | Đăng nhập | Tất cả | Xác thực tài khoản bằng Email và Mật khẩu, cấp JWT token. Chuyển hướng theo vai trò hoặc trang yêu cầu ban đầu. Tài khoản dùng mật khẩu tạm phải đổi mật khẩu trước khi vào trang chính. |
| **UC-02** | Đăng xuất | Tất cả | Kết thúc phiên làm việc, thu hồi refresh_token và xóa token trên client. |
| **UC-03** | Quên mật khẩu | Tất cả | Gửi mã OTP/Link xác thực qua email để thiết lập mật khẩu mới. Vô hiệu hóa mã/link đã sử dụng. |
| **UC-04** | Xem thông tin cá nhân | Tất cả | Hiển thị thông tin hồ sơ: Họ tên, Email, Số điện thoại, Ảnh đại diện, Vai trò. |
| **UC-05** | Cập nhật thông tin cá nhân | Tất cả | Cho phép sửa đổi họ tên, số điện thoại, ảnh đại diện (avatar). |
| **UC-06** | Đổi mật khẩu | Tất cả | Thay đổi mật khẩu tài khoản (yêu cầu xác thực mật khẩu hiện tại). Mật khẩu mới phải khác mật khẩu cũ. |

---

### 3.2. Phân Hệ Sinh Viên (10 Use Cases)
| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-07** | Xem danh sách bài tập | Xem danh sách bài tập được giao theo lớp/chủ đề, lọc theo trạng thái. Hiển thị điểm chính thức hoặc tạm tính nếu đã có kết quả. |
| **UC-08** | Xem chi tiết bài tập | Xem đề bài (Markdown/LaTeX), yêu cầu I/O, ràng buộc, giới hạn, Sample Test Cases và Rubric công khai. Hỗ trợ xem lại bài đã quá hạn nếu chính sách cho phép. |
| **UC-09** | Viết code | Soạn thảo mã nguồn trực tiếp trên Monaco Editor với autosave. Bản nháp được khôi phục khi tải lại trang. |
| **UC-10** | Tải tệp bài làm lên | Tải file mã nguồn từ máy tính nạp vào editor. Kiểm tra phần mở rộng, kích thước và nội dung. |
| **UC-11** | Nộp bài | Gửi mã nguồn trực tiếp đến API (không chạy thử trước). Kiểm tra số lần nộp tối đa, chính sách nộp muộn. Grader Worker gửi code + Hidden Test Cases đến Docker Sandbox. Auto-Grading tính điểm Correctness theo trọng số, phân tích tĩnh nếu cấu hình, AI Engine tạo feedback. Bài nộp bị gián đoạn không tính vào số lần nộp. |
| **UC-12** | Xem kết quả Auto-Grader | Xem điểm, trạng thái từng test case, thời gian thực thi, bộ nhớ. Input/Output Hidden Test Cases được bảo mật. Hiển thị trạng thái "Bị gián đoạn" kèm hướng dẫn nộp lại nếu có. |
| **UC-13** | Xem nhận xét AI | Xem đánh giá về lỗi, chất lượng mã nguồn, độ phức tạp và đề xuất cải thiện do AI tạo ra. |
| **UC-14** | Tương tác với AI Tutor | Chat với AI Tutor theo phương pháp Socratic. Context gồm đề bài, mã nguồn, kết quả test. AI không cung cấp ngay lời giải nếu chính sách không cho phép. |
| **UC-15** | Xem lịch sử làm bài | Tra cứu các lần nộp, xem mã nguồn, kết quả test và feedback. Hỗ trợ lọc và so sánh giữa các phiên bản. |
| **UC-16** | Xem bảng điểm cá nhân | Tổng hợp điểm theo bài tập và lớp. Điểm chính thức = điểm chấm thủ công; nếu chưa có thì hiển thị điểm Auto-Grader theo chính sách (Highest/Latest Score) với nhãn "Tạm tính". Điểm AI chỉ để tham khảo. |

---

### 3.3. Phân Hệ Giáo Viên (15 Use Cases)

> **Lưu ý**: UC-17, UC-18, UC-20 chỉ áp dụng cho các lớp do Giáo viên phụ trách.

| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-17** | Tạo lớp học | Khởi tạo lớp học mới do mình phụ trách; hệ thống sinh mã tham gia nếu cần. |
| **UC-18** | Chỉnh sửa lớp học | Cập nhật tên lớp, mô tả, niên khóa. Chỉ lớp đang ở trạng thái Hoạt động. |
| **UC-19** | *(Xem UC-40)* | Chức năng đóng/mở lại lớp được tích hợp vào UC-40. |
| **UC-20** | Quản lý sinh viên trong lớp | Thêm/Xóa sinh viên trong lớp phụ trách qua email, mã SV hoặc mã tham gia. Lớp phải đang Hoạt động. |
| **UC-21** | Quản lý/Cấu hình bài tập | Tạo bài tập với cấu hình: số lần nộp tối đa (0 = không giới hạn), chính sách tính điểm (Highest Score / Latest Score), quy tắc nộp muộn và tỷ lệ trừ điểm, trọng số tiêu chí chấm điểm. |
| **UC-22** | Chỉnh sửa thông tin chung bài tập | Cập nhật Tên, Đề bài, Ngôn ngữ, Mức độ khó, Giới hạn tài nguyên. Không bao gồm Hạn nộp, Test Case, Rubric. Bài đã có bài nộp chỉ cho sửa mô tả/đề bài hoặc yêu cầu tạo phiên bản mới. |
| **UC-23** | Xóa bài tập | Xóa mềm/vô hiệu hóa bài tập. Bài có bài nộp được vô hiệu hóa thay vì xóa vật lý. |
| **UC-24** | Thiết lập hạn nộp bài | Thiết lập/điều chỉnh thời hạn nộp bài (phải > thời điểm hiện tại). Không thể thay đổi hạn nộp của bài tập đã đóng. |
| **UC-25** | Thiết lập test case | Quản lý bộ Test Case: Input, Output mong đợi, Sample/Hidden, Trọng số điểm. |
| **UC-26** | Thiết lập rubric | Cấu hình tiêu chí và trọng số. Correctness do hệ thống tự tính từ Test Case. Tổng trọng số phải bằng 100%. |
| **UC-27** | Giao bài tập cho lớp | Giao bài tập cho một/nhiều lớp. Hỗ trợ giao lại hoặc cập nhật cấu hình giao bài. |
| **UC-28** | Xem bài nộp | Xem danh sách sinh viên và trạng thái nộp bài; xem chi tiết mã nguồn, kết quả kiểm thử, phân tích và điểm. |
| **UC-29** | Xem điểm | Xem bảng điểm sinh viên theo bài tập và lớp; xem chi tiết điểm theo tiêu chí đánh giá. |
| **UC-30** | Xem AI đánh giá | Xem kết quả đánh giá AI: điểm, kết quả Test Case, phân tích mã nguồn, nhận xét chi tiết theo từng tiêu chí. |
| **UC-31** | Đánh giá/chấm bài thủ công | Chấm bài theo Rubric, nhập điểm và nhận xét. Điểm thủ công là điểm chính thức, ưu tiên hơn Auto-Grader; điểm Auto-Grader và AI được giữ lại tham khảo. Hỗ trợ lưu tạm. Khi chưa có điểm thủ công, điểm Auto-Grader hiển thị ở trạng thái "Tạm tính". |

---

### 3.4. Phân Hệ Quản Trị Viên (12 Use Cases)
| Mã UC | Tên Use Case | Tác nhân | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- |
| **UC-32** | Tạo tài khoản người dùng | QTV | Tạo tài khoản SV/GV/Giáo vụ; sinh mật khẩu tạm, bắt buộc đổi lần đăng nhập đầu, gửi email. |
| **UC-33** | Khóa/mở tài khoản | QTV | Khóa/mở khóa tài khoản; thu hồi phiên đăng nhập khi khóa. |
| **UC-34** | Xóa tài khoản | QTV | Xóa tài khoản; xóa mềm nếu có dữ liệu bài nộp/điểm liên quan. |
| **UC-35** | Phân quyền người dùng | QTV, QTVHT | QTV phân quyền SV/GV/Giáo vụ; QTVHT phân quyền QTV/QTVHT. Không được cấp quyền vượt phạm vi. |
| **UC-36** | Đặt lại mật khẩu | QTV | Sinh mật khẩu tạm, đánh dấu bắt buộc đổi, gửi email; thu hồi phiên hiện tại. |
| **UC-37** | Nhập danh sách từ Excel/CSV | QTV | Import hàng loạt từ file 5 cột bắt buộc; preview, báo lỗi từng bản ghi. |
| **UC-38** | Tạo lớp | QTV, Giáo vụ | QTV tạo lớp toàn hệ thống; Giáo vụ tạo lớp trong phạm vi Khoa/Bộ môn phụ trách. |
| **UC-39** | Chỉnh sửa lớp | QTV, Giáo vụ | QTV chỉnh sửa mọi lớp; Giáo vụ chỉnh sửa lớp thuộc Khoa/Bộ môn phụ trách. Lớp phải đang Hoạt động. |
| **UC-40** | Đóng/Mở lại lớp học | GV, QTV, Giáo vụ | GV đóng/mở lại lớp phụ trách; QTV/Giáo vụ trong phạm vi quản lý. Lớp đóng ngăn hoạt động học tập; dữ liệu được bảo toàn. |
| **UC-41** | Quản lý Lưu trữ & Xóa lớp học | QTV, Giáo vụ | Lưu trữ/Khôi phục/Xóa lớp. Hard Delete chỉ khi 0 SV + 0 bài tập + 0 lịch học. Có dữ liệu thì chuyển Lưu trữ. Khôi phục về "Đã đóng". |
| **UC-42** | Quản lý sinh viên trong lớp | QTV, Giáo vụ | Thêm/Xóa/Xem sinh viên trong lớp theo phạm vi quyền. Lớp phải đang Hoạt động. |
| **UC-43** | Phân công Giáo viên vào lớp | QTV, Giáo vụ | Phân công/Hủy phân công GV cho lớp; hỗ trợ phân công nhiều GV. Giáo vụ chỉ thao tác lớp thuộc Khoa/Bộ môn phụ trách. |

---

### 3.5. Phân Hệ Quản Trị Viên Hệ Thống (5 Use Cases Đặc Thù)
| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-44** | Quản lý cấu hình AI | Thiết lập, cập nhật, kích hoạt/vô hiệu hóa cấu hình AI. Hỗ trợ kiểm tra kết nối (Test Connection). |
| **UC-45** | Cấu hình Docker Sandbox | Cấu hình RAM Limit, CPU Limit, Execution Timeout, Base Images. Hỗ trợ khôi phục mặc định và kiểm tra khả năng khởi tạo. |
| **UC-46** | Giám sát Docker Sandbox | Theo dõi realtime trạng thái container, CPU/RAM usage. Dừng phiên thực thi bị kẹt; bài nộp bị dừng chuyển sang "Bị gián đoạn", không tự chấm lại, không tăng submission_count. |
| **UC-47** | Quản lý tổ chức | Quản lý tổ chức, Khoa/Bộ môn trực thuộc; phân công Giáo vụ phụ trách (1 Giáo vụ có thể phụ trách nhiều Khoa/Bộ môn). |
| **UC-48** | Quản lý System Logs | Xem, tìm kiếm, lọc, xem chi tiết và xuất System Logs theo thời gian, người dùng, hành động, loại sự kiện. |

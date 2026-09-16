# 02. ĐẶC TẢ ACTOR & DANH MỤC USE CASES (UC)

---

## 1. MÔ HÌNH PHÂN QUYỀN (RBAC MATRIX)

Hệ thống được thiết kế theo mô hình **Role-Based Access Control (RBAC)** với 4 nhóm Actor chính:

| Actor | Ký hiệu | Cấp độ quản trị | Phạm vi dữ liệu truy cập |
| :--- | :---: | :--- | :--- |
| **Student** | `ST` | Người học (End-user) | Chỉ xem được lớp mình tham gia, bài tập được giao, bài làm và điểm của chính mình. |
| **Teacher** | `TE` | Giảng viên | Quản lý các lớp được phân công, tạo bài tập, chấm điểm và xem toàn bộ bài nộp của học viên trong lớp. |
| **Admin** | `AD` | Quản lý Trường / Cơ sở | Quản lý tài khoản (Student/Teacher), quản lý danh sách lớp, phân công giảng viên trong phạm vi tổ chức. |
| **Super Admin** | `SA` | Quản trị Hệ thống | Toàn quyền cấu hình hạ tầng, API Key AI, Docker Sandbox, giám sát hệ thống và quản lý đa tổ chức. |

---

## 2. MA TRẬN PHÂN QUYỀN CHỨC NĂNG

| Nhóm Chức Năng | Student | Teacher | Admin | Super Admin |
| :--- | :---: | :---: | :---: | :---: |
| Đăng nhập / Đăng xuất / Quên & Đổi mật khẩu | ✅ | ✅ | ✅ | ✅ |
| Xem & Cập nhật thông tin cá nhân | ✅ | ✅ | ✅ | ✅ |
| Viết code, Chạy thử & Nộp bài (Monaco Editor) | ✅ | ❌ | ❌ | ❌ |
| Tương tác AI Tutor & Xem gợi ý Socratic | ✅ | ❌ | ❌ | ❌ |
| Xem lịch sử làm bài & Bảng điểm cá nhân | ✅ | ❌ | ❌ | ❌ |
| Tạo, sửa, xóa bài tập & Thiết lập Test cases / Rubric | ❌ | ✅ | ❌ | ❌ |
| Giao bài tập cho lớp & Đặt deadline | ❌ | ✅ | ❌ | ❌ |
| Xem danh sách nộp bài & Đánh giá/Chấm đè thủ công | ❌ | ✅ | ❌ | ❌ |
| Quản lý tài khoản (Tạo, Khóa, Xóa, Phân quyền, Reset pass) | ❌ | ❌ | ✅ | ✅ |
| Import danh sách người dùng từ Excel/CSV | ❌ | ❌ | ✅ | ✅ |
| Tạo lớp & Phân công giảng viên phụ trách | ❌ | ❌ | ✅ | ✅ |
| Cấu hình AI Engine (API Key, Model, Temperature) | ❌ | ❌ | ❌ | ✅ |
| Cấu hình & Giám sát Docker Sandbox | ❌ | ❌ | ❌ | ✅ |
| Quản lý Tổ chức (Multi-organization) & System Logs | ❌ | ❌ | ❌ | ✅ |

---

## 3. DANH MỤC CHI TIẾT 48 USE CASES

### 3.1. Các Use Case Xác Thực & Quản Lý Tài Khoản Chung
| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-01** | Đăng nhập | Xác thực tài khoản bằng Email và Mật khẩu, cấp JWT token. |
| **UC-02** | Đăng xuất | Kết thúc phiên làm việc và thu hồi token trên client. |
| **UC-03** | Quên mật khẩu | Gửi mã OTP/Link xác thực qua email để thiết lập mật khẩu mới. |
| **UC-04** | Xem thông tin cá nhân | Hiển thị thông tin hồ sơ: Họ tên, Email, Vai trò, Lớp tham gia. |
| **UC-05** | Cập nhật thông tin cá nhân | Cho phép sửa đổi họ tên, số điện thoại, ảnh đại diện (avatar). |

---

### 3.2. Phân Hệ Student (12 Use Cases)
| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-ST06** | Đổi mật khẩu | Thay đổi mật khẩu tài khoản (yêu cầu xác thực mật khẩu hiện tại). |
| **UC-ST07** | Xem danh sách bài tập | Xem danh sách bài tập được giao theo từng lớp/chủ đề, lọc theo trạng thái. |
| **UC-ST08** | Xem chi tiết bài tập | Xem mô tả bài toán, giới hạn thời gian/bộ nhớ, ví dụ mẫu và rubric. |
| **UC-ST09** | Viết / chỉnh sửa code | Soạn thảo mã nguồn trực tiếp trên giao diện tích hợp Monaco Editor. |
| **UC-ST10** | Upload file bài làm | Tải file mã nguồn từ máy tính (`.py`, `.cpp`, `.java`) đưa vào editor. |
| **UC-ST11** | Chạy thử chương trình | Thực thi code trên các Sample Test Cases công khai để debug nhanh. |
| **UC-ST12** | Nộp bài chính thức | Gửi bài làm vào hàng đợi để Docker Sandbox chấm full Hidden Tests và kích hoạt AI. |
| **UC-ST13** | Xem kết quả Auto-Grader | Xem chi tiết điểm số, trạng thái từng test case (AC, WA, TLE, MLE, CE, RE). |
| **UC-ST14** | Xem nhận xét AI | Xem đánh giá tổng quan về chất lượng mã, độ phức tạp $O(n)$ và code smells. |
| **UC-ST15** | Tương tác với AI Tutor | Chat với AI để nhận gợi ý logic sửa lỗi theo phương pháp Socratic. |
| **UC-ST16** | Xem lịch sử làm bài | Tra cứu các lần nộp trước đó, xem lại mã nguồn đã nộp và sự thay đổi qua từng lần. |
| **UC-ST17** | Xem bảng điểm cá nhân | Bảng tổng hợp điểm số các bài tập đã nộp theo môn học/lớp học. |

---

### 3.3. Phân Hệ Teacher (15 Use Cases)
| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-TE03** | Tạo lớp học | Khởi tạo lớp học mới do mình phụ trách. |
| **UC-TE04** | Chỉnh sửa lớp học | Cập nhật tên lớp, mô tả, niên khóa. |
| **UC-TE05** | Xóa / đóng lớp học | Đóng lớp khi kết thúc học kỳ hoặc xóa lớp rỗng. |
| **UC-TE06** | Quản lý sinh viên trong lớp | Thêm/Xóa sinh viên vào danh sách lớp thông qua mã SV hoặc email. |
| **UC-TE07** | Tạo bài tập | Soạn thảo tiêu đề, nội dung, chọn ngôn ngữ lập trình cho phép. |
| **UC-TE08** | Chỉnh sửa bài tập | Cập nhật đề bài hoặc các cấu hình liên quan. |
| **UC-TE09** | Xóa bài tập | Xóa hoặc ẩn bài tập khỏi danh sách bài được giao. |
| **UC-TE10** | Thiết lập deadline | Cài đặt thời gian mở đề và thời hạn nộp bài (cho phép/chặn nộp muộn). |
| **UC-TE11** | Thiết lập test case | Nhập dữ liệu Input/Output, đánh dấu Sample/Hidden, thiết lập trọng số điểm. |
| **UC-TE12** | Thiết lập rubric | Thiết lập bảng tiêu chí chấm: Execution (Pass tests), Static Quality, Complexity. |
| **UC-TE13** | Giao bài tập cho lớp | Chỉ định một hoặc nhiều lớp nhận bài tập đã tạo. |
| **UC-TE14** | Xem submissions | Xem toàn bộ bài làm đã nộp của các sinh viên trong lớp. |
| **UC-TE15** | Xem bảng điểm lớp | Xem và xuất bảng điểm bài tập của toàn bộ sinh viên trong lớp. |
| **UC-TE16** | Xem AI đánh giá | Xem phân tích và báo cáo của AI đối với bài làm của từng sinh viên. |
| **UC-TE17** | Đánh giá / chấm bài thủ công | Chấm đè điểm số hoặc nhập nhận xét cá nhân của giảng viên cho sinh viên. |

---

### 3.4. Phân Hệ Admin (11 Use Cases)
| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-AD01** | Tạo tài khoản | Tạo thủ công tài khoản cho Student hoặc Teacher mới. |
| **UC-AD02** | Khóa / mở tài khoản | Tạm ngưng hoặc kích hoạt lại quyền đăng nhập của người dùng. |
| **UC-AD03** | Xóa tài khoản | Xóa bỏ tài khoản khỏi cơ sở dữ liệu (kèm cơ chế soft-delete). |
| **UC-AD04** | Phân quyền người dùng | Thay đổi vai trò (Role) của người dùng giữa Student, Teacher, Admin. |
| **UC-AD05** | Reset mật khẩu | Đặt lại mật khẩu tạm thời cho người dùng khi được yêu cầu. |
| **UC-AD06** | Import Excel / CSV | Tạo tài khoản hoặc ghi danh sinh viên vào lớp hàng loạt từ file Excel. |
| **UC-AD07** | Tạo lớp (Cấp quản trị) | Khởi tạo lớp học mới trong phạm vi tổ chức/khoa. |
| **UC-AD08** | Chỉnh sửa lớp | Cập nhật thông tin bất kỳ lớp học nào thuộc tổ chức. |
| **UC-AD09** | Xóa / đóng lớp | Đóng hoặc xóa lớp học ở cấp quản trị tổ chức. |
| **UC-AD10** | Quản lý sinh viên trong lớp | Thêm/Xóa sinh viên trong bất kỳ lớp học nào. |
| **UC-AD11** | Phân công giảng viên | Chỉ định hoặc thay đổi giảng viên phụ trách cho lớp học. |

---

### 3.5. Phân Hệ Super Admin (6 Use Cases Đặc Thù)
| Mã UC | Tên Use Case | Mô tả vắn tắt |
| :--- | :--- | :--- |
| **UC-SA06** | Đổi mật khẩu Super Admin | Đổi mật khẩu tài khoản quản trị tối cao. |
| **UC-SA07** | Quản lý cấu hình AI | Nhập/Đổi API Key (Gemini, OpenAI), cấu hình Model, Temperature, Prompts. |
| **UC-SA08** | Cấu hình Docker Sandbox | Cấu hình RAM Limit, CPU Limit, Execution Timeout, Base Images. |
| **UC-SA09** | Giám sát Docker Sandbox | Giám sát trạng thái hoạt động của sandbox containers, CPU/RAM usage realtime. |
| **UC-SA10** | Quản lý tổ chức | Quản lý các trường học / trung tâm trong hệ thống đa tổ chức (Multi-tenant). |
| **UC-SA11** | Quản lý System Logs | Tra cứu lịch sử lỗi, nhật ký chấm bài, audit logs của toàn bộ hệ thống. |

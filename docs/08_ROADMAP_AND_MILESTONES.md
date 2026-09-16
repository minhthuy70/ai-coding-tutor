# 08. LỘ TRÌNH TRIỂN KHAI ĐỀ XUẤT (8-WEEK ROADMAP & MILESTONES)

---

## 1. TỔNG QUAN 3 GIAI ĐOẠN PHÁT TRIỂN (3-PHASE TIMELINE)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 1: MVP CORE SYSTEM (Tuần 1 - Tuần 3)                          │
│ • Hoàn thiện 4 Trụ cột Cốt lõi: Quản lý bài tập -> Monaco Editor ->     │
│   Docker Sandbox Auto-Grader -> Tích hợp AI Reviewer / Socratic Prompt. │
├─────────────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 2: PHÂN QUYỀN RBAC & QUẢN TRỊ LỚP HỌC (Tuần 4 - Tuần 6)       │
│ • Xác thực JWT, hoàn thiện phân quyền 4 Roles (Student, Teacher,        │
│   Admin, Super Admin).                                                  │
│ • Quản lý Lớp học, giao bài theo lớp, cấu hình Rubric điểm số.          │
│ • Giảng viên xem bài nộp & can thiệp chấm đè thủ công.                  │
├─────────────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 3: HOÀN THIỆN QUẢN TRỊ, GIÁM SÁT & TỐI ƯU (Tuần 7 - Tuần 8)   │
│ • Import danh sách Excel/CSV, Cấu hình API Key & Giám sát Sandbox.      │
│ • System Logs, Queue Performance Tuning, Viết báo cáo / Tài liệu.       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. KẾ HOẠCH CHI TIẾT TỪNG TUẦN (WEEKLY SPRINT BREAKDOWN)

### GIAI ĐOẠN 1: MVP CORE PIPELINE (TUẦN 1 - 3)

#### Tuần 1: Dựng Hạ Tầng, Database & Docker Sandbox Runner
- [x] Khởi tạo Git Repo, cấu trúc thư mục Monorepo (`backend/`, `frontend/`, `sandbox/`, `docs/`).
- [ ] Dựng `docker-compose.yml` (PostgreSQL 15 + Redis 7).
- [ ] Xây dựng Dockerfile Sandbox Runner cho Python với cơ chế giới hạn tài nguyên và ngắt kết nối mạng an toàn.
- [ ] Viết script `runner.py` đo thời gian thực thi, bộ nhớ và bắt lỗi (TLE, MLE, RE, AC, WA).
- **Kết quả nghiệm thu (Milestone 1)**: Chạy thử nghiệm thành công một file `solution.py` trong Docker Sandbox và xuất ra JSON kết quả test cases.

#### Tuần 2: Backend API Quản Lý Bài Tập & Hàng Đợi Chấm Bài (Async Grader)
- [ ] Xây dựng Database Schema cơ bản (Users, Problems, TestCases, Submissions) bằng SQLAlchemy + Alembic.
- [ ] Viết REST API CRUD Bài tập và bộ Test Cases.
- [ ] Cấu hình Celery Worker kết nối Redis Queue để xử lý chấm bài bất đồng bộ.
- [ ] Kết nối Grader Worker gọi Docker Sandbox chấm các test cases ẩn.
- **Kết quả nghiệm thu (Milestone 2)**: API nhận mã nguồn $\rightarrow$ đẩy vào Queue $\rightarrow$ Worker chạy Sandbox $\rightarrow$ cập nhật điểm số vào Database.

#### Tuần 3: Web IDE (Monaco Editor) & Tích Hợp AI Tutor Cơ Bản
- [ ] Dựng giao diện Web Next.js: Màn hình xem đề bài & Trình soạn thảo **Monaco Editor**.
- [ ] Nút "Chạy thử" (Run Sample Tests) và nút "Nộp bài" (Submit).
- [ ] Tích hợp **Google Gemini API** (hoặc OpenAI): Phân tích mã nguồn sinh viên, chỉ ra lỗi logic và sinh câu hỏi Socratic.
- [ ] Giao diện xem kết quả Auto-Grader và Chat Box tương tác với AI Tutor.
- **Kết quả nghiệm thu (Milestone 3 - MVP Core Release)**: Một sinh viên có thể làm bài trên web từ đầu đến cuối, nộp bài, nhận điểm số từ Sandbox và nhận lời khuyên từ AI.

---

### GIAI ĐOẠN 2: HOÀN THIỆN RBAC & QUẢN TRỊ LỚP HỌC (TUẦN 4 - 6)

#### Tuần 4: Xác Thực & Phân Quyền Người Dùng (JWT & RBAC)
- [ ] Xây dựng hệ thống Đăng ký, Đăng nhập, Đổi/Quên mật khẩu với JWT (Access + Refresh Token).
- [ ] Middleware phân quyền 4 vai trò: `Student`, `Teacher`, `Admin`, `Super Admin`.
- [ ] Phân luồng điều hướng UI theo quyền của từng Actor.

#### Tuần 5: Phân Hệ Giảng Viên (Teacher Portal)
- [ ] Chức năng Tạo lớp học, mời/quản lý sinh viên trong lớp.
- [ ] Chức năng Giao bài tập cho lớp, thiết lập Deadline và cho phép nộp muộn.
- [ ] Cấu hình Rubric đánh giá đa tiêu chí (Test cases, Code Quality, Complexity).
- **Kết quả nghiệm thu (Milestone 4)**: Giảng viên có thể tạo lớp và giao bài tập riêng cho từng lớp học.

#### Tuần 6: Bảng Điểm, Submission Review & Chấm Thủ Công
- [ ] Giao diện cho Giảng viên xem danh sách toàn bộ bài nộp của sinh viên.
- [ ] Xem chi tiết mã nguồn, kết quả test cases và đánh giá của AI đối với từng sinh viên.
- [ ] Tính năng Giảng viên chấm đè điểm số (Override Grade) và gửi phản hồi cá nhân.
- [ ] Bảng điểm tổng hợp theo lớp và xuất báo cáo điểm.

---

### GIAI ĐOẠN 3: SUITE QUẢN TRỊ HỆ THỐNG & TỐI ƯU HÓA (TUẦN 7 - 8)

#### Tuần 7: Phân Hệ Quản Trị (Admin & Super Admin)
- [ ] Chức năng Import danh sách sinh viên / giảng viên từ file Excel (`.xlsx`, `.csv`).
- [ ] Super Admin Dashboard: Cấu hình API Key AI, Model Parameters (Temperature, Max Tokens).
- [ ] Giao diện Giám sát trạng thái Docker Sandbox & Quản lý System Logs.

#### Tuần 8: Tối Ưu Hiệu Năng, Kiểm Thử Toàn Diện & Đóng Gói
- [ ] Kiểm thử tải (Load Testing / Concurrency Test) khi nhiều bài nộp gửi đến cùng lúc.
- [ ] Tối ưu hóa bộ nhớ đệm (Redis Caching) và tối ưu độ dài Prompt AI.
- [ ] Hoàn thiện tài liệu hướng dẫn sử dụng (User Manual) và mã nguồn hoàn chỉnh.
- **Kết quả nghiệm thu (Final Milestone)**: Hệ thống hoàn chỉnh 48 Use Cases sẵn sàng bàn giao / báo cáo đề tài.

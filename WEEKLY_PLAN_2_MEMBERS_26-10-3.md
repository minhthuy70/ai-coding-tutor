# LỘ TRÌNH PHÁT TRIỂN CHI TIẾT - 2 NGƯỜI (28 DAYS)
# DETAILED DEVELOPMENT ROADMAP - 2 MEMBERS

**Deadline**: 31/10/2026
**Start Date**: 03/10/2026
**Total Duration**: 28 days (~4 weeks)

---

## PHÂN CÔNG VAI TRÒ (ROLE ASSIGNMENT)

### **Người A (Frontend Developer)**
- Chuyên trách: Next.js, Monaco Editor, UI/UX, WebSocket, User Experience
- Công cụ: React, Tailwind CSS, TypeScript, Monaco Editor

### **Người B (Backend Developer)**
- Chuyên trách: FastAPI, Database Schema, Docker Sandbox, Celery Worker, AI Integration
- Công cụ: Python, SQLAlchemy, PostgreSQL, Redis, Docker, Celery

---

## TUẦN 1: GIAI ĐOẠN MVP CORE (03/10 - 09/10)
### WEEK 1: MVP CORE INFRASTRUCTURE

### **NGÀY 1: 03/10/2026 (FRIDAY) - KHỞI TẠO & CẤU HÌNH MÔI TRƯỜNG**

#### **Người A (Frontend)**
- [ ] Khởi tạo project Next.js với TypeScript và Tailwind CSS
  - **Chi tiết**: Run `npx create-next-app@latest frontend --typescript --tailwind --app`
  - **Cấu trúc**: Setup folder structure (app/, components/, lib/, types/)
- [ ] Cài đặt Monaco Editor React
  - **Chi tiết**: `npm install @monaco-editor/react`
  - **Tạo component**: Basic Monaco Editor component với syntax highlighting
- [ ] Setup .env.local cho Frontend
  - **Chi tiết**: Copy từ .env.example, cấu hình NEXT_PUBLIC_API_URL
- [ ] Kiểm tra kết nối với Backend API
  - **Chi tiết**: Tạo test page gọi API health check từ http://localhost:8000/api/health

#### **Người B (Backend)**
- [ ] Review và hoàn thiện docker-compose.yml
  - **Chi tiết**: Đảm bảo PostgreSQL 15 và Redis 7 được cấu hình đúng
  - **Test**: Chạy `docker compose up -d postgres redis` và kiểm tra status
- [ ] Setup backend FastAPI project structure
  - **Chi tiết**: Tạo cấu trúc thư mục (app/api/, app/models/, app/schemas/, app/core/)
- [ ] Cài đặt dependencies cho Backend
  - **Chi tiết**: `pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary redis celery python-multipart python-jose[cryptography] passlib[bcrypt]`
- [ ] Tạo file .env và cấu hình database connection
  - **Chi tiết**: DATABASE_URL, REDIS_URL, SECRET_KEY, GEMINI_API_KEY

---

### **NGÀY 2: 04/10/2026 (SATURDAY) - DATABASE SCHEMA & AUTHENTICATION**

#### **Người A (Frontend)**
- [ ] Thiết kế và tạo Layout chính cho ứng dụng
  - **Chi tiết**: Sidebar navigation, Header với user profile placeholder
  - **Pages**: Trang Login, Trang Dashboard, Trang Problem List
- [ ] Tạo Login Form Component
  - **Chi tiết**: Form với Email và Password fields, validation cơ bản
  - **UI**: Styled với Tailwind CSS, responsive design
- [ ] Setup Authentication Context (React Context)
  - **Chi tiết**: Tạo AuthContext để quản lý token và user state
  - **Functions**: login, logout, refresh token logic

#### **Người B (Backend)**
- [ ] Tạo Database Models (SQLAlchemy)
  - **Chi tiết**: Models: User, Organization, Department, Class, Problem, TestCase, Submission, AIFeedback
  - **Tham khảo**: Theo ERD trong docs/05_SYSTEM_ARCHITECTURE.md
- [ ] Setup Alembic cho Database Migrations
  - **Chi tiết**: `alembic init alembic`, cấu hình alembic.ini
  - **Tạo migration**: `alembic revision --autogenerate -m "Initial schema"`
- [ ] Implement JWT Authentication (FastAPI)
  - **Chi tiết**: create_access_token, verify_token, get_current_user dependency
  - **Endpoints**: POST /api/v1/auth/login, POST /api/v1/auth/refresh
- [ ] Run database migration
  - **Chi tiết**: `alembic upgrade head`

---

### **NGÀY 3: 05/10/2026 (SUNDAY) - AUTHENTICATION FLOW**

#### **Người A (Frontend)**
- [ ] Kết nối Login Form với Backend API
  - **Chi tiết**: Gọi POST /api/v1/auth/login, lưu access_token và refresh_token
  - **Storage**: Lưu token vào localStorage hoặc httpOnly cookie
- [ ] Implement Protected Routes
  - **Chi tiết**: Tạo middleware để kiểm tra authentication trước khi truy cập các trang cần đăng nhập
- [ ] Tạo Profile Page Component
  - **Chi tiết**: Hiển thị thông tin user (name, email, role)
  - **API**: GET /api/v1/users/me
- [ ] Tạo Logout Functionality
  - **Chi tiết**: Gọi POST /api/v1/auth/logout (nếu có) hoặc xóa token local

#### **Người B (Backend)**
- [ ] Implement User CRUD APIs
  - **Chi tiết**: GET /api/v1/users/me, PUT /api/v1/users/me
  - **Validation**: Validate input data với Pydantic schemas
- [ ] Implement Password Change & Forgot Password APIs
  - **Chi tiết**: POST /api/v1/auth/change-password, POST /api/v1/auth/forgot-password
  - **OTP**: Tạo cơ chế OTP đơn giản lưu vào Redis (có thể chưa gửi email thật)
- [ ] Implement Role-based Authorization Middleware
  - **Chi tiết**: Decorator để kiểm tra role (STUDENT, TEACHER, ADMIN, STAFF, SUPER_ADMIN)
- [ ] Create seed data script
  - **Chi tiết**: Script tạo user test (admin, teacher, student) để demo

---

### **NGÀY 4: 06/10/2026 (MONDAY) - PROBLEM MANAGEMENT (BACKEND) & PROBLEM LIST UI (FRONTEND)**

#### **Người A (Frontend)**
- [ ] Tạo Problem List Page
  - **Chi tiết**: Hiển thị danh sách bài tập với các thông tin: Title, Difficulty, Deadline, Status
  - **UI**: Card layout hoặc Table, hỗ trợ search và filter
- [ ] Tạo Problem Detail Page Layout
  - **Chi tiết**: Split view - Bên trái: Đề bài, Bên phải: Monaco Editor (đang ẩn)
  - **UI**: Hiển thị title, description, input/output format, constraints, sample test cases
- [ ] Implement Markdown rendering cho Problem Description
  - **Chi tiết**: Cài `react-markdown` để render Markdown và LaTeX
- [ ] Tạo API client functions cho Problems
  - **Chi tiết**: Hàm fetchProblems(), fetchProblemById()

#### **Người B (Backend)**
- [ ] Implement Problem CRUD APIs
  - **Chi tiết**: POST /api/v1/problems, GET /api/v1/problems, GET /api/v1/problems/{id}, PUT /api/v1/problems/{id}
  - **Authorization**: Chỉ Teacher và Admin được tạo/sửa
- [ ] Implement TestCase Management APIs
  - **Chi tiết**: POST /api/v1/problems/{id}/testcases, GET /api/v1/problems/{id}/testcases
  - **Fields**: input_data, expected_output, is_sample, score_weight
- [ ] Implement Rubric Configuration APIs
  - **Chi tiết**: POST /api/v1/problems/{id}/rubrics
  - **Fields**: criteria_name, weight, description
- [ ] Create sample problem data
  - **Chi tiết**: Tạo 3-5 bài tập mẫu (Hello World, Sum of Two Numbers, Basic Loop)

---

### **NGÀY 5: 07/10/2026 (TUESDAY) - MONACO EDITOR & SUBMISSION**

#### **Người A (Frontend)**
- [ ] Tích hợp Monaco Editor vào Problem Detail Page
  - **Chi tiết**: Config language selector (Python, C++, Java), theme, font size
  - **Features**: Syntax highlighting, auto-indent, basic intellisense
- [ ] Implement Auto-save functionality
  - **Chi tiết**: Auto-save code draft mỗi 30 seconds vào Backend API
  - **Endpoint**: POST /api/v1/submissions/draft
- [ ] Implement File Upload Feature
  - **Chi tiết**: Button "Upload File" để nạp code từ máy tính vào editor
  - **Validation**: Kiểm tra file extension (.py, .cpp, .java)
- [ ] Tạo Submit Button với Confirmation Dialog
  - **Chi tiết**: Popup cảnh báo "Sau khi nộp không thể chỉnh sửa"
  - **API**: POST /api/v1/submissions

#### **Người B (Backend)**
- [ ] Implement Draft Submission API
  - **Chi tiết**: POST /api/v1/submissions/draft - lưu code nháp
  - **Database**: Lưu vào bảng submissions với status = DRAFT
- [ ] Implement Submit Submission API
  - **Chi tiết**: POST /api/v1/submissions - nộp bài chính thức
  - **Logic**: Convert DRAFT → SUBMITTED, set trigger_type = MANUAL, lock editor
- [ ] Setup Celery Worker for Async Grading
  - **Chi tiết**: Configure Celery với Redis broker
  - **Task**: Tạo celery task cho grading pipeline
- [ ] Implement Submission Retrieval APIs
  - **Chi tiết**: GET /api/v1/submissions/{id}, GET /api/v1/submissions/history

---

### **NGÀY 6: 08/10/2026 (WEDNESDAY) - DOCKER SANDBOX**

#### **Người A (Frontend)**
- [ ] Tạo Submission Status Component
  - **Chi tiết**: Hiển thị trạng thái bài nộp (PENDING, RUNNING, COMPLETED)
  - **UI**: Progress bar hoặc loading spinner
- [ ] Implement WebSocket Connection
  - **Chi tiết**: Kết nối WebSocket để nhận realtime update khi grading hoàn tất
  - **Events**: SUBMISSION_QUEUED, RUNNING_TESTS, ANALYZING_AI, SUBMISSION_COMPLETED
- [ ] Tạo Submission Result Page
  - **Chi tiết**: Hiển thị điểm số, trạng thái từng test case, execution time, memory usage
  - **UI**: Table với các cột: Test Case, Status, Time, Memory
- [ ] Polish Monaco Editor UI
  - **Chi tiết**: Thêm line numbers, minimap, fullscreen mode

#### **Người B (Backend)**
- [ ] Create Dockerfile for Python Sandbox
  - **Chi tiết**: Base image python:3.11-slim, install dependencies
  - **Security**: Non-root user, read-only filesystem, network none
- [ ] Build Sandbox Docker Image
  - **Chi tiết**: `docker build -t sandbox-python:latest -f Dockerfile.python .`
- [ ] Implement Sandbox Runner Script (runner.py)
  - **Chi tiết**: Execute code in Docker container with resource limits
  - **Metrics**: Capture execution time, memory usage, exit status
- [ ] Implement Test Case Executor
  - **Chi tiết**: Run code against each test case, capture stdout/stderr
  - **Comparison**: Compare output with expected_output

---

### **NGÀY 7: 09/10/2026 (THURSDAY) - GRADING PIPELINE INTEGRATION**

#### **Người A (Frontend)**
- [ ] Tạo AI Feedback Display Component
  - **Chi tiết**: Hiển thị nhận xét từ AI (quality_score, complexity_score, logic_analysis, pedagogical_hints)
  - **UI**: Card layout với các section cho từng loại feedback
- [ ] Tạo AI Tutor Chat Interface
  - **Chi tiết**: Chat box để sinh viên tương tác với AI Tutor
  - **UI**: Message bubbles, input field, send button
- [ ] Implement Chat API Integration
  - **Chi tiết**: POST /api/v1/tutor/chat - gửi câu hỏi và nhận phản hồi
  - **Context**: Include problem_id, submission_id, chat history
- [ ] Polish Overall UI/UX
  - **Chi tiết**: Responsive design, loading states, error handling, toast notifications

#### **Người B (Backend)**
- [ ] Implement Grading Celery Task
  - **Chi tiết**: Task lấy submission từ queue, chạy Docker Sandbox, chấm test cases
  - **Logic**: Update submission status → RUNNING → COMPLETED
- [ ] Implement AI Integration (Gemini/OpenAI)
  - **Chi tiết**: Gọi LLM API để phân tích code và tạo feedback
  - **Prompt**: Socratic prompt template từ docs/04_TECHNICAL_EVALUATION.md
- [ ] Implement AI Tutor Chat API
  - **Chi tiết**: POST /api/v1/tutor/chat - context-aware chat
  - **Socratic**: Ensure AI follows Socratic method (no direct code solutions)
- [ ] Implement WebSocket for Realtime Updates
  - **Chi tiết**: WebSocket endpoint để broadcast grading progress
  - **Events**: SUBMISSION_QUEUED, RUNNING_TESTS, ANALYZING_AI, SUBMISSION_COMPLETED

---

## TUẦN 2: GIAI ĐOẠN RBAC & CLASS MANAGEMENT (10/10 - 16/10)
### WEEK 2: RBAC & CLASS MANAGEMENT

### **NGÀY 8: 10/10/2026 (FRIDAY) - CLASS MANAGEMENT**

#### **Người A (Frontend)**
- [ ] Tạo Class List Page (cho Admin/Staff)
  - **Chi tiết**: Hiển thị danh sách lớp học với thông tin: Name, Code, Teacher, Status
  - **UI**: Table với actions (View, Edit, Delete)
- [ ] Tạo Class Detail Page
  - **Chi tiết**: Hiển thị thông tin lớp, danh sách sinh viên, danh sách bài tập được giao
  - **UI**: Tabs cho Students và Assignments
- [ ] Tạo Create/Edit Class Form
  - **Chi tiết**: Form với fields: Name, Code, Description, Teacher selection
  - **Validation**: Validate unique code
- [ ] Implement Role-based UI Rendering
  - **Chi tiết**: Hiển thị/ẩn các menu items dựa trên user role

#### **Người B (Backend)**
- [ ] Implement Class CRUD APIs
  - **Chi tiết**: POST /api/v1/classes, GET /api/v1/classes, GET /api/v1/classes/{id}, PUT /api/v1/classes/{id}
  - **Authorization**: Admin (toàn trường), Staff (Khoa/Bộ môn)
- [ ] Implement Class Member Management APIs
  - **Chi tiết**: POST /api/v1/classes/{id}/students, DELETE /api/v1/classes/{id}/students/{student_id}
  - **Logic**: Thêm/xóa sinh viên vào lớp
- [ ] Implement Teacher Assignment API
  - **Chi tiết**: POST /api/v1/classes/{id}/teachers
  - **Logic**: Phân công giáo viên phụ trách lớp
- [ ] Implement Class Status Management
  - **Chi tiết**: PUT /api/v1/classes/{id}/status - ACTIVE, CLOSED, ARCHIVED

---

### **NGÀY 9: 11/10/2026 (SATURDAY) - ASSIGNMENT TO CLASS**

#### **Người A (Frontend)**
- [ ] Tạo Assignment Management Page (cho Teacher)
  - **Chi tiết**: Giao diện giao bài tập cho lớp
  - **UI**: Multi-select dropdown để chọn lớp, deadline picker
- [ ] Tạo Teacher Dashboard
  - **Chi tiết**: Tổng quan các lớp đang phụ trách, số sinh viên, số bài tập
  - **UI**: Cards với statistics, links đến các classes
- [ ] Tạo Student Class View
  - **Chi tiết**: Sinh viên xem các lớp mình tham gia và bài tập của từng lớp
  - **UI**: Filter Problem List theo class
- [ ] Implement Deadline Countdown
  - **Chi tiết**: Hiển thị countdown timer cho mỗi bài tập

#### **Người B (Backend)**
- [ ] Implement Class Assignment APIs
  - **Chi tiết**: POST /api/v1/problems/{id}/assign - giao bài tập cho lớp
  - **Fields**: class_ids[], deadline
- [ ] Implement Class Assignment Database Schema
  - **Chi tiết**: Table class_assignments (problem_id, class_id, deadline)
- [ ] Implement Student Class Enrollment APIs
  - **Chi tiết**: GET /api/v1/users/me/classes - lấy danh sách lớp của sinh viên
- [ ] Implement Auto-submit Logic
  - **Chi tiết**: Celery task kiểm tra deadline, auto-submit draft khi hết hạn
  - **Trigger**: trigger_type = AUTO_EXPIRED

---

### **NGÀY 10: 12/10/2026 (SUNDAY) - GRADEBOOK & MANUAL GRADING**

#### **Người A (Frontend)**
- [ ] Tạo Gradebook Page (cho Teacher)
  - **Chi tiết**: Bảng điểm tổng hợp theo lớp và bài tập
  - **UI**: Matrix table với rows = students, columns = assignments
- [ ] Tạo Submission Review Page (cho Teacher)
  - **Chi tiết**: Xem chi tiết bài nộp của sinh viên
  - **UI**: Hiển thị code, test results, AI feedback, manual grading form
- [ ] Implement Manual Grading Form
  - **Chi tiết**: Form để giáo viên nhập điểm thủ công và nhận xét
  - **Fields**: final_score, comments, confirm_official_score
- [ ] Tạo Export Gradebook Feature
  - **Chi tiết**: Export bảng điểm ra Excel/CSV

#### **Người B (Backend)**
- [ ] Implement Gradebook APIs
  - **Chi tiết**: GET /api/v1/classes/{id}/gradebook - lấy bảng điểm lớp
  - **Logic**: Join submissions, problems, students, calculate scores
- [ ] Implement Manual Grading APIs
  - **Chi tiết**: PUT /api/v1/submissions/{id}/manual-grade
  - **Fields**: final_score, comments, official_score
- [ ] Implement Official Score Confirmation
  - **Chi tiết**: Logic để xác nhận điểm chính thức (giáo viên confirm)
- [ ] Implement Gradebook Export
  - **Chi tiết**: GET /api/v1/classes/{id}/gradebook/export - Excel/CSV

---

### **NGÀY 11: 13/10/2026 (MONDAY) - USER MANAGEMENT (ADMIN)**

#### **Người A (Frontend)**
- [ ] Tạo User Management Page (cho Admin)
  - **Chi tiết**: Danh sách tất cả users với thông tin: Name, Email, Role, Status
  - **UI**: Table với search/filter, actions (Edit, Delete, Change Role)
- [ ] Tạo Create User Form
  - **Chi tiết**: Form tạo user mới với các fields: Name, Email, Role, Department
  - **Features**: Auto-generate temporary password
- [ ] Tạo Import Users from Excel/CSV Page
  - **Chi tiết**: Upload file Excel/CSV với 5 cột chuẩn
  - **UI**: Drag & drop area, preview table, error handling
- [ ] Implement User Status Management
  - **Chi tiết**: Active/Inactive, Lock/Unlock accounts

#### **Người B (Backend)**
- [ ] Implement User Management APIs
  - **Chi tiết**: POST /api/v1/users, GET /api/v1/users, PUT /api/v1/users/{id}, DELETE /api/v1/users/{id}
  - **Authorization**: Chỉ Admin được tạo/sửa/xóa users
- [ ] Implement Role Assignment API
  - **Chi tiết**: PUT /api/v1/users/{id}/role - thay đổi role
- [ ] Implement User Import API
  - **Chi tiết**: POST /api/v1/users/import - Excel/CSV import
  - **Validation**: Validate 5 columns, handle errors per row
- [ ] Implement User Status Management
  - **Chi tiết**: PUT /api/v1/users/{id}/status - active/inactive/locked
  - **Logic**: Revoke sessions when locked

---

### **NGÀY 12: 14/10/2026 (TUESDAY) - ORGANIZATION & DEPARTMENT MANAGEMENT**

#### **Người A (Frontend)**
- [ ] Tạo Organization Management Page (cho Admin)
  - **Chi tiết**: Quản lý cơ cấu tổ chức, Khoa/Bộ môn
  - **UI**: Tree view hoặc hierarchical list
- [ ] Tạo Department Management Page
  - **Chi tiết**: Tạo, sửa, xóa Khoa/Bộ môn
  - **UI**: Form với fields: Name, Code, Organization
- [ ] Tạo Staff Assignment Page
  - **Chi tiết**: Phân công Giáo vụ phụ trách Khoa/Bộ môn
  - **UI**: Multi-select để phân công staff
- [ ] Polish Admin Dashboard
  - **Chi tiết**: Tổng quan hệ thống: số users, classes, submissions

#### **Người B (Backend)**
- [ ] Implement Organization Management APIs
  - **Chi tiết**: POST /api/v1/organizations, GET /api/v1/organizations, PUT /api/v1/organizations/{id}
- [ ] Implement Department Management APIs
  - **Chi tiết**: POST /api/v1/departments, GET /api/v1/departments, PUT /api/v1/departments/{id}
- [ ] Implement Staff Assignment APIs
  - **Chi tiết**: POST /api/v1/departments/{id}/staff - phân công giáo vụ
- [ ] Implement Admin Dashboard APIs
  - **Chi tiết**: GET /api/v1/admin/dashboard - statistics
  - **Metrics**: total_users, total_classes, total_submissions, system_health

---

### **NGÀY 13: 15/10/2026 (WEDNESDAY) - STUDENT VIEW & PERSONAL GRADEBOOK**

#### **Người A (Frontend)**
- [ ] Tạo Student Dashboard
  - **Chi tiết**: Tổng quan cá nhân: các lớp đang học, bài tập pending, deadline sắp tới
  - **UI**: Cards với statistics, list các bài tập cần làm
- [ ] Tạo Personal Gradebook Page
  - **Chi tiết**: Bảng điểm cá nhân theo lớp và bài tập
  - **UI**: Table với điểm Auto-Grader (tạm tính) và điểm chính thức
- [ ] Tạo Submission History Page
  - **Chi tiết**: Lịch sử các bài đã nộp với kết quả chi tiết
  - **UI**: List với links đến submission detail
- [ ] Implement AI Tutor Chat History
  - **Chi tiết**: Hiển thị lịch sử chat với AI cho từng bài nộp

#### **Người B (Backend)**
- [ ] Implement Student Dashboard APIs
  - **Chi tiết**: GET /api/v1/students/dashboard - stats cá nhân
  - **Logic**: Classes enrolled, pending assignments, upcoming deadlines
- [ ] Implement Personal Gradebook APIs
  - **Chi tiết**: GET /api/v1/students/gradebook - điểm cá nhân
  - **Logic**: Join submissions, show auto_score vs final_score
- [ ] Implement Submission History APIs
  - **Chi tiết**: GET /api/v1/students/submissions - lịch sử nộp bài
- [ ] Implement AI Chat History APIs
  - **Chi tiết**: GET /api/v1/tutor/conversations/{submission_id}

---

### **NGÀY 14: 16/10/2026 (THURSDAY) - TESTING & BUG FIXING WEEK 2**

#### **Người A (Frontend)**
- [ ] End-to-end Testing cho Class Management Flow
  - **Chi tiết**: Test: Tạo class → Giao bài → Sinh viên làm bài → Giáo viên chấm
- [ ] Test Role-based Access Control
  - **Chi tiết**: Verify các features được ẩn/hiện đúng theo role
- [ ] Bug Fixing UI/UX Issues
  - **Chi tiết**: Fix các lỗi từ testing, polish UI
- [ ] Responsive Design Testing
  - **Chi tiết**: Test trên mobile và tablet

#### **Người B (Backend)**
- [ ] Integration Testing cho Grading Pipeline
  - **Chi tiết**: Test: Submit → Queue → Worker → Sandbox → AI → Result
- [ ] Load Testing cho Concurrent Submissions
  - **Chi tiết**: Test với 10-20 submissions đồng thời
- [ ] Bug Fixing Backend Issues
  - **Chi tiết**: Fix các lỗi từ testing, optimize queries
- [ ] Database Performance Optimization
  - **Chi tiết**: Add indexes, optimize slow queries

---

## TUẦN 3: GIAI ĐOẠN ADMIN SYSTEM & OPTIMIZATION (17/10 - 23/10)
### WEEK 3: ADMIN SYSTEM & OPTIMIZATION

### **NGÀY 15: 17/10/2026 (FRIDAY) - AI CONFIGURATION MANAGEMENT**

#### **Người A (Frontend)**
- [ ] Tạo AI Configuration Page (cho Super Admin)
  - **Chi tiết**: Cấu hình AI Engine (API Key, Model, Parameters)
  - **UI**: Form với fields: provider (Gemini/OpenAI), api_key, model, temperature, max_tokens
- [ ] Tạo AI Model Selection Component
  - **Chi tiết**: Dropdown để chọn model (Gemini Flash, Gemini Pro, GPT-4o, etc.)
- [ ] Implement AI Test Endpoint UI
  - **Chi tiết**: Button để test AI connection và response
- [ ] Tạo AI Usage Statistics Page
  - **Chi tiết**: Hiển thị token usage, cost estimation

#### **Người B (Backend)**
- [ ] Implement AI Configuration APIs
  - **Chi tiết**: GET /api/v1/system/ai-config, PUT /api/v1/system/ai-config
  - **Fields**: provider, api_key, model, temperature, max_tokens, timeout
  - **Encryption**: Encrypt API keys trước khi lưu vào DB
- [ ] Implement AI Provider Abstraction Layer
  - **Chi tiết**: Interface để hỗ trợ multiple AI providers (Gemini, OpenAI, Local Ollama)
- [ ] Implement AI Test Endpoint
  - **Chi tiết**: POST /api/v1/system/ai-config/test - test connection
- [ ] Implement AI Usage Tracking
  - **Chi tiết**: Track token usage per submission, store in database

---

### **NGÀY 16: 18/10/2026 (SATURDAY) - DOCKER SANDBOX CONFIGURATION**

#### **Người A (Frontend)**
- [ ] Tạo Sandbox Configuration Page (cho Super Admin)
  - **Chi tiết**: Cấu hình Docker Sandbox parameters
  - **UI**: Form với fields: cpu_limit, memory_limit, time_limit, pids_limit
- [ ] Tạo Sandbox Status Dashboard
  - **Chi tiết**: Hiển thị trạng thái các sandbox containers đang chạy
  - **UI**: Real-time metrics: CPU, Memory, Active containers
- [ ] Implement Sandbox Log Viewer
  - **Chi tiết**: Hiển thị logs từ Docker containers
  - **UI**: Terminal-like interface with auto-scroll

#### **Người B (Backend)**
- [ ] Implement Sandbox Configuration APIs
  - **Chi tiết**: GET /api/v1/system/sandbox/config, PUT /api/v1/system/sandbox/config
  - **Fields**: cpu_limit, memory_limit, time_limit, pids_limit, network_mode
- [ ] Implement Sandbox Monitoring APIs
  - **Chi tiết**: GET /api/v1/system/sandbox/metrics - real-time metrics
  - **Logic**: Docker stats API, active containers list
- [ ] Implement Sandbox Log APIs
  - **Chi tiết**: GET /api/v1/system/sandbox/logs/{container_id}
- [ ] Implement Sandbox Container Management
  - **Chi tiết**: Force stop container, cleanup old containers

---

### **NGÀY 17: 19/10/2026 (SUNDAY) - SYSTEM LOGS & MONITORING**

#### **Người A (Frontend)**
- [ ] Tạo System Logs Page (cho Super Admin)
  - **Chi tiết**: Xem, tìm kiếm, lọc system logs
  - **UI**: Log viewer với filters: level, timestamp, user, action
- [ ] Implement Log Search & Filter
  - **Chi tiết**: Search by keyword, filter by date range, log level
- [ ] Tạo System Health Dashboard
  - **Chi tiết**: Hiển thị health status: Database, Redis, Docker, AI
  - **UI**: Status indicators (green/red/yellow)
- [ ] Implement Error Alert UI
  - **Chi tiết**: Hiển thị errors và warnings trong hệ thống

#### **Người B (Backend)**
- [ ] Implement Structured Logging
  - **Chi tiết**: Setup Python logging với structured format (JSON)
  - **Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- [ ] Implement System Log APIs
  - **Chi tiết**: GET /api/v1/system/logs - paginated logs
  - **Filters**: level, start_date, end_date, user_id, action
- [ ] Implement Health Check Endpoints
  - **Chi tiết**: GET /api/v1/system/health - check all services
  - **Services**: Database, Redis, Docker, AI Provider
- [ ] Implement Error Tracking
  - **Chi tiết**: Capture exceptions, store in logs table

---

### **NGÀY 18: 20/10/2026 (MONDAY) - PERFORMANCE OPTIMIZATION**

#### **Người A (Frontend)**
- [ ] Implement Code Splitting
  - **Chi tiết**: Split code by routes để giảm initial load time
- [ ] Optimize Asset Loading
  - **Chi tiết**: Lazy load images, optimize fonts, minify CSS/JS
- [ ] Implement Client-side Caching
  - **Chi tiết**: Cache API responses với React Query hoặc SWR
- [ ] Optimize Monaco Editor Performance
  - **Chi tiết**: Lazy load Monaco, reduce bundle size

#### **Người B (Backend)**
- [ ] Implement Redis Caching
  - **Chi tiết**: Cache frequent queries (problems list, user profile)
  - **TTL**: Set appropriate TTL for each cache key
- [ ] Optimize Database Queries
  - **Chi tiết**: Add indexes, use select_related/prefetch, avoid N+1 queries
- [ ] Implement Response Compression
  - **Chi tiết**: Gzip compression cho API responses
- [ ] Optimize Celery Worker Performance
  - **Chi tiết**: Tune worker count, prefetch multiplier, task time limit

---

### **NGÀY 19: 21/10/2026 (TUESDAY) - SECURITY HARDENING**

#### **Người A (Frontend)**
- [ ] Implement CSRF Protection
  - **Chi tiết**: Add CSRF tokens to forms
- [ ] Implement XSS Protection
  - **Chi tiết**: Sanitize user input, use DOMPurify for HTML
- [ ] Implement Rate Limiting on Client
  - **Chi tiết**: Debounce button clicks, limit API calls
- [ ] Security Audit Frontend Code
  - **Chi tiết**: Review for security vulnerabilities

#### **Người B (Backend)**
- [ ] Implement Rate Limiting
  - **Chi tiết**: Rate limit API endpoints bằng Redis
  - **Limits**: Login attempts, submission rate, chat messages
- [ ] Implement Input Validation & Sanitization
  - **Chi tiết**: Validate all inputs với Pydantic, sanitize strings
- [ ] Implement SQL Injection Protection
  - **Chi tiết**: Ensure all queries use parameterized statements
- [ ] Security Audit Backend Code
  - **Chi tiết**: Review for security vulnerabilities

---

### **NGÀY 20: 22/10/2026 (WEDNESDAY) - ERROR HANDLING & USER FEEDBACK**

#### **Người A (Frontend)**
- [ ] Implement Global Error Boundary
  - **Chi tiết**: Catch React errors, display friendly error page
- [ ] Implement Toast Notifications
  - **Chi tiết**: Success, error, warning, info toasts
- [ ] Implement Loading States
  - **Chi tiết**: Skeleton loaders, spinners, progress bars
- [ ] Implement Offline Support (Optional)
  - **Chi tiết**: Service worker for offline mode

#### **Người B (Backend)**
- [ ] Implement Global Exception Handlers
  - **Chi tiết**: Custom exception handlers cho FastAPI
- [ ] Implement Detailed Error Responses
  - **Chi tiết**: Structured error responses with error codes
- [ ] Implement Request Logging
  - **Chi tiết**: Log all requests with timing and status
- [ ] Implement Graceful Degradation
  - **Chi tiết**: Fallback logic when services are down

---

### **NGÀY 21: 23/10/2026 (THURSDAY) - TESTING & BUG FIXING WEEK 3**

#### **Người A (Frontend)**
- [ ] End-to-end Testing cho Admin Features
  - **Chi tiết**: Test: AI config, Sandbox config, System logs
- [ ] Cross-browser Testing
  - **Chi tiết**: Test trên Chrome, Firefox, Edge, Safari
- [ ] Bug Fixing
  - **Chi tiết**: Fix các lỗi từ testing
- [ ] UI Polish
  - **Chi tiết**: Final UI adjustments, animations, transitions

#### **Người B (Backend)**
- [ ] Integration Testing cho Admin APIs
  - **Chi tiết**: Test all admin endpoints
- [ ] Security Testing
  - **Chi tiết**: Test rate limiting, input validation, auth
- [ ] Bug Fixing
  - **Chi tiết**: Fix các lỗi từ testing
- [ ] Performance Testing
  - **Chi tiết**: Load test với realistic traffic

---

## TUẦN 4: GIAI ĐOẠN FINAL TESTING & DOCUMENTATION (24/10 - 31/10)
### WEEK 4: FINAL TESTING & DOCUMENTATION

### **NGÀY 22: 24/10/2026 (FRIDAY) - COMPREHENSIVE TESTING**

#### **Người A (Frontend)**
- [ ] Full User Flow Testing - Student
  - **Chi tiết**: Login → View problems → Write code → Submit → View results → Chat with AI
- [ ] Full User Flow Testing - Teacher
  - **Chi tiết**: Login → Create problem → Assign to class → Review submissions → Manual grade
- [ ] Full User Flow Testing - Admin
  - **Chi tiết**: Login → Manage users → Manage classes → View logs → Configure AI
- [ ] Cross-device Testing
  - **Chi tiết**: Test trên desktop, tablet, mobile

#### **Người B (Backend)**
- [ ] Full API Testing
  - **Chi tiết**: Test all endpoints with various inputs
- [ ] Concurrency Testing
  - **Chi tiết**: Test với 50+ concurrent submissions
- [ ] Long-running Task Testing
  - **Chi tiết**: Test grading pipeline with various code scenarios
- [ ] Database Integrity Testing
  - **Chi tiết**: Test foreign keys, cascading deletes, data consistency

---

### **NGÀY 23: 25/10/2026 (SATURDAY) - BUG FIXING & REFINEMENT**

#### **Người A (Frontend)**
- [ ] Fix Critical Bugs
  - **Chi tiết**: Priority 1 bugs blocking core functionality
- [ ] Fix UI/UX Issues
  - **Chi tiết**: Priority 2 bugs affecting user experience
- [ ] Performance Optimization
  - **Chi tiết**: Fix slow pages, large bundle sizes
- [ ] Accessibility Improvements
  - **Chi tiết**: ARIA labels, keyboard navigation, screen reader support

#### **Người B (Backend)**
- [ ] Fix Critical Bugs
  - **Chi tiết**: Priority 1 bugs blocking core functionality
- [ ] Fix Performance Issues
  - **Chi tiết**: Slow queries, memory leaks, connection pool issues
- [ ] Fix Security Issues
  - **Chi tiết**: Any security vulnerabilities found
- [ ] Data Migration Scripts
  - **Chi tiết**: Scripts để migrate data nếu cần

---

### **NGÀY 24: 26/10/2026 (SUNDAY) - DOCUMENTATION - USER MANUAL**

#### **Người A (Frontend)**
- [ ] Create User Guide - Student
  - **Chi tiết**: How to login, view problems, write code, submit, view results
- [ ] Create User Guide - Teacher
  - **Chi tiết**: How to create problems, assign to class, grade submissions
- [ ] Create User Guide - Admin
  - **Chi tiết**: How to manage users, classes, configure system
- [ ] Create Screenshots & Diagrams
  - **Chi tiết**: Screenshots cho các workflows chính

#### **Người B (Backend)**
- [ ] Create API Documentation
  - **Chi tiết**: Document all endpoints with examples
- [ ] Create Deployment Guide
  - **Chi tiết**: How to deploy to production (Docker, environment variables)
- [ ] Create Architecture Documentation
  - **Chi tiết**: Update system architecture docs with actual implementation
- [ ] Create Troubleshooting Guide
  - **Chi tiết**: Common issues and solutions

---

### **NGÀY 25: 27/10/2026 (MONDAY) - DOCUMENTATION - DEVELOPER GUIDE**

#### **Người A (Frontend)**
- [ ] Create Frontend Developer Guide
  - **Chi tiết**: Project structure, component library, coding standards
- [ ] Document Frontend Dependencies
  - **Chi tiết**: List all npm packages and their purposes
- [ ] Create Component Documentation
  - **Chi tiết**: Storybook or markdown docs for reusable components
- [ ] Document State Management
  - **Chi tiết**: How state is managed (Context, React Query, etc.)

#### **Người B (Backend)**
- [ ] Create Backend Developer Guide
  - **Chi tiết**: Project structure, coding standards, testing guidelines
- [ ] Document Backend Dependencies
  - **Chi tiết**: List all Python packages and their purposes
- [ ] Create Database Schema Documentation
  - **Chi tiết**: ERD, table descriptions, relationships
- [ ] Document Celery Tasks
  - **Chi tiết**: List all tasks, their parameters, retry logic

---

### **NGÀY 26: 28/10/2026 (TUESDAY) - DEMO PREPARATION**

#### **Người A (Frontend)**
- [ ] Prepare Demo Data
  - **Chi tiết**: Create realistic demo data (users, classes, problems, submissions)
- [ ] Create Demo Scenarios
  - **Chi tiết**: Prepare step-by-step demo scripts for each user role
- [ ] Polish Demo UI
  - **Chi tiết**: Ensure demo data looks good in UI
- [ ] Prepare Demo Environment
  - **Chi tiết**: Clean demo database, reset to known state

#### **Người B (Backend)**
- [ ] Create Demo Data Script
  - **Chi tiết**: Script to populate database with demo data
- [ ] Prepare Demo API Keys
  - **Chi tiết**: Test AI API keys with enough quota for demo
- [ ] Configure Demo Environment
  - **Chi tiết**: Set appropriate timeouts, limits for demo
- [ ] Test Demo Flow End-to-End
  - **Chi tiết**: Run through all demo scenarios

---

### **NGÀY 27: 29/10/2026 (WEDNESDAY) - FINAL REVIEW & ACCEPTANCE TESTING**

#### **Người A (Frontend)**
- [ ] Final UI Review
  - **Chi tiết**: Check all pages for consistency, errors, broken links
- [ ] Final User Acceptance Testing
  - **Chi tiết**: Walk through all use cases from DOAN4.md
- [ ] Final Performance Check
  - **Chi tiết**: Check page load times, responsiveness
- [ ] Final Cross-browser Check
  - **Chi tiết**: Verify on all target browsers

#### **Người B (Backend)**
- [ ] Final API Review
  - **Chi tiết**: Check all endpoints, error handling, validation
- [ ] Final Security Review
  - **Chi tiết**: Check auth, rate limiting, input validation
- [ ] Final Performance Check
  - **Chi tiết**: Check response times, database query performance
- [ ] Final Data Integrity Check
  - **Chi tiết**: Verify database constraints, foreign keys

---

### **NGÀY 28: 30/10/2026 (THURSDAY) - DEPLOYMENT PREPARATION**

#### **Người A (Frontend)**
- [ ] Production Build
  - **Chi tiết**: `npm run build`, verify build output
- [ ] Environment Configuration
  - **Chi tiết**: Prepare production .env variables
- [ ] Asset Optimization
  - **Chi tiết**: Verify minification, compression, CDN setup
- [ ] Final Deployment Checklist
  - **Chi tiết**: Checklist for deployment steps

#### **Người B (Backend)**
- [ ] Production Docker Images
  - **Chi tiết**: Build and tag production images
- [ ] Database Migration Preparation
  - **Chi tiết**: Prepare migration scripts for production
- [ ] Backup Strategy
  - **Chi tiết**: Setup database backup, log backup
- [ ] Monitoring Setup
  - **Chi tiết**: Setup monitoring, alerting, logging

---

### **NGÀY 29: 31/10/2026 (FRIDAY) - FINAL DELIVERY**

#### **Người A (Frontend)**
- [ ] Final Code Review
  - **Chi tiết**: Review all frontend code one last time
- [ ] Tag Release
  - **Chi tiết**: Create git tag for release
- [ ] Handover Documentation
  - **Chi tiết**: Ensure all documentation is complete
- [ ] Final Sign-off
  - **Chi tiết**: Confirm all frontend tasks complete

#### **Người B (Backend)**
- [ ] Final Code Review
  - **Chi tiết**: Review all backend code one last time
- [ ] Tag Release
  - **Chi tiết**: Create git tag for release
- [ ] Handover Documentation
  - **Chi tiết**: Ensure all documentation is complete
- [ ] Final Sign-off
  - **Chi tiết**: Confirm all backend tasks complete

---

## MILESTONES & DELIVERABLES

### **Milestone 1: MVP Core Infrastructure (End of Week 1 - 09/10)**
- ✅ Authentication system working
- ✅ Problem management APIs working
- ✅ Monaco Editor integrated
- ✅ Submission flow working
- ✅ Docker Sandbox running
- ✅ AI Integration basic working

### **Milestone 2: RBAC & Class Management (End of Week 2 - 16/10)**
- ✅ Role-based access control complete
- ✅ Class management working
- ✅ Assignment to class working
- ✅ Manual grading working
- ✅ Gradebook working
- ✅ User management working

### **Milestone 3: Admin System & Optimization (End of Week 3 - 23/10)**
- ✅ AI configuration working
- ✅ Sandbox configuration working
- ✅ System logs working
- ✅ Performance optimized
- ✅ Security hardened
- ✅ Error handling complete

### **Milestone 4: Final Delivery (End of Week 4 - 31/10)**
- ✅ All 44 use cases implemented
- ✅ Comprehensive testing complete
- ✅ Documentation complete
- ✅ Demo prepared
- ✅ Deployment ready
- ✅ Project delivered

---

## NOTES & REMINDERS

### **Coordination Between Team Members**
- **Daily Standup**: Brief sync on progress and blockers
- **Code Review**: Review each other's code before merging
- **Conflict Resolution**: Use separate branches for frontend/backend work
- **API Contract**: Define API contracts early, use OpenAPI/Swagger

### **Risk Management**
- **AI API Costs**: Monitor token usage, set budget limits
- **Docker Resource Limits**: Monitor CPU/Memory usage, adjust limits
- **Database Performance**: Monitor slow queries, add indexes as needed
- **Time Management**: Prioritize MVP features, defer non-essential features

### **Quality Assurance**
- **Testing**: Write unit tests for critical business logic
- **Code Quality**: Use linters (ESLint, Pylint), follow code style
- **Documentation**: Keep documentation updated as code changes
- **Backups**: Regular database backups before major changes

---

## EMERGENCY BUFFER DAYS

### **Days 30-31: Buffer for Unexpected Issues**
- Use these days if any task takes longer than expected
- Prioritize critical path items
- Can defer non-essential documentation if needed
- Focus on ensuring MVP is fully functional

---

**Last Updated**: 03/10/2026
**Version**: 1.0

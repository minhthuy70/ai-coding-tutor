# RULES.md
# SRS & Business Rules — AI-Powered Coding Tutor & Auto-Grader

> **Source of Truth** cho các quyết định nghiệp vụ, business rules, ràng buộc logic và các lưu ý khi phát triển hệ thống.
>
> Khi sửa SRS, Use Case, ERD, API, UI hoặc test, phải đối chiếu tài liệu này. Nếu business rule thay đổi, cập nhật RULES.md và đồng bộ các UC liên quan.

---

# 1. ACTOR & PHẠM VI

| Actor | Phạm vi |
|---|---|
| **Sinh viên** | Làm bài, nộp bài, xem kết quả và điểm của bản thân. |
| **Giáo viên** | Quản lý lớp, bài tập, chấm điểm trong phạm vi lớp mình phụ trách. |
| **Giáo vụ** | Quản lý nghiệp vụ lớp học trong phạm vi Khoa/Bộ môn được phân công. |
| **Quản trị viên** | Quản lý nghiệp vụ đào tạo toàn trường/toàn hệ thống. |
| **Quản trị viên hệ thống** | Quản trị kỹ thuật nền tảng: AI, Docker Sandbox, System Logs và cấu hình hệ thống. |

## Scope

```text
Giáo viên
→ lớp mình phụ trách

Giáo vụ
→ Khoa/Bộ môn được phân công

Quản trị viên
→ toàn trường

Quản trị viên hệ thống
→ kỹ thuật nền tảng, KHÔNG quản lý nghiệp vụ lớp
```

## Business Admin ≠ System Admin

**Quản trị viên** phụ trách nghiệp vụ đào tạo: tài khoản, lớp, sinh viên trong lớp, phân công Giáo viên, tổ chức/Khoa/Bộ môn và phân công Giáo vụ.

**Quản trị viên hệ thống** phụ trách: Docker Sandbox, AI configuration, AI Key, System Logs và các cấu hình kỹ thuật.

System Admin **không**:
- tạo/chỉnh sửa lớp;
- đóng/mở lớp;
- Archive/Restore/Delete lớp;
- quản lý sinh viên trong lớp;
- phân công Giáo viên.

---

# 2. AUTHENTICATION & SECURITY

## 2.1 Đăng nhập

Cả 5 actor đều dùng nhóm UC-01 → UC-06.

Luồng chuẩn:

```text
Email + Password
→ kiểm tra tài khoản
→ kiểm tra trạng thái
→ tạo phiên
→ Access Token + Refresh Token
→ điều hướng theo Role
```

Nếu tài khoản đang dùng mật khẩu tạm:

```text
Login
→ bắt buộc đổi mật khẩu
→ đổi thành công
→ vào hệ thống
```

## 2.2 Mật khẩu

- Mật khẩu phải được lưu dưới dạng băm.
- Tạo tài khoản mới: hệ thống tự sinh mật khẩu tạm.
- Reset mật khẩu: hệ thống tự sinh mật khẩu tạm hoặc cơ chế reset tương ứng.
- Admin không tự nhập mật khẩu người dùng.
- Mật khẩu tạm gửi tới email đã đăng ký.
- Tài khoản có mật khẩu tạm phải đổi ở lần đăng nhập đầu tiên.
- Reset mật khẩu phải xử lý/thu hồi các phiên đăng nhập hiện tại theo chính sách bảo mật.

## 2.3 Quên mật khẩu

- Dùng OTP hoặc reset link có thời hạn.
- OTP/link đã dùng phải bị vô hiệu hóa.
- Không tiết lộ email có tồn tại hay không.
- Gửi lại OTP/link phải tuân thủ cooldown/rate limit.

## 2.4 Đăng xuất

- Kết thúc phiên.
- Xóa thông tin xác thực cục bộ.
- Refresh token được thu hồi hoặc vô hiệu hóa theo cơ chế hệ thống.
- Phiên hết hạn → yêu cầu đăng nhập lại.

---

# 3. ACCOUNT MANAGEMENT

## 3.1 Tạo tài khoản

Quản trị viên có thể tạo:
- Sinh viên;
- Giáo viên;
- Giáo vụ.

Luồng:

```text
QTV tạo tài khoản
→ kiểm tra dữ liệu
→ tạo tài khoản
→ sinh mật khẩu tạm
→ gửi email
→ bắt buộc đổi mật khẩu lần đầu
```

## 3.2 Khóa/Mở khóa

- Tài khoản bị khóa/vô hiệu hóa không được đăng nhập.
- Khóa tài khoản không đồng nghĩa xóa dữ liệu học tập.

## 3.3 Xóa tài khoản

- Phải kiểm tra dữ liệu liên quan.
- Nếu có dữ liệu học tập cần bảo toàn, dùng Soft Delete/vô hiệu hóa.
- Không làm mất lịch sử Submission, điểm và đánh giá chỉ vì xóa tài khoản.

## 3.4 Reset mật khẩu

- QTV chọn tài khoản.
- Hệ thống tạo mật khẩu tạm/cơ chế reset.
- Người dùng phải đổi mật khẩu theo chính sách.
- Các phiên hiện tại được xử lý theo chính sách bảo mật.

## 3.5 Import Excel/CSV

File có đúng 5 cột:

```text
Mã sinh viên
Họ tên
Email
Vai trò
Lớp
```

**Không có cột mật khẩu.**

Thứ tự:

```text
Upload
→ kiểm tra cấu trúc
→ kiểm tra từng bản ghi
→ hiển thị kết quả + lỗi
→ QTV xác nhận
→ Import
```

Nếu cập nhật tài khoản đã tồn tại:
- chỉ đổi **họ tên**;
- không đổi email;
- không đổi vai trò;
- không nhập mật khẩu qua import.

---

# 4. AUTHORIZATION

Mọi nghiệp vụ phải kiểm tra:

```text
Authentication
+ Role
+ Scope
+ Resource
+ Resource Status
```

Không chỉ kiểm tra `role`.

## Không tự nâng quyền

Người thực hiện chỉ được cấp quyền nằm trong phạm vi quyền của mình.

```text
QTV
→ không tự cấp QTV hệ thống
→ không tự nâng quyền vượt phạm vi

System Admin
→ quản lý vai trò/quyền quản trị cấp hệ thống
```

---

# 5. CLASS MANAGEMENT

## 5.1 Trạng thái lớp

```text
Hoạt động
   ↓ Đóng
Đã đóng
   ↓ Lưu trữ
Lưu trữ
```

Mở lại:

```text
Đã đóng
   ↓ Mở lại
Hoạt động
```

Restore:

```text
Lưu trữ
   ↓ Restore
Đã đóng
```

**Restore không tự động đưa lớp về Hoạt động.**

## 5.2 Hoạt động

Lớp Hoạt động cho phép các nghiệp vụ học tập hợp lệ theo quyền.

Ví dụ:
- giao bài;
- quản lý sinh viên;
- phân công Giáo viên;
- đóng lớp.

## 5.3 Đã đóng

- Ngăn các hoạt động học tập/tương tác không còn được phép.
- Không giao bài mới.
- Dữ liệu vẫn được bảo toàn.
- Có thể mở lại.
- Có thể Archive.

## 5.4 Lưu trữ

- Không hoạt động.
- Không xuất hiện trong danh sách vận hành thông thường.
- Dữ liệu được bảo toàn.
- Có thể Restore.
- Restore → Đã đóng.

---

# 6. CLASS LIFECYCLE

## 6.1 UC-40 — Đóng/Mở lại

Actor:
- Giáo viên;
- Giáo vụ;
- Quản trị viên.

Không có System Admin.

```text
Hoạt động
   ↓ Close
Đã đóng
   ↓ Reopen
Hoạt động
```

Phải kiểm tra:
- lớp tồn tại;
- trạng thái phù hợp;
- người thực hiện có quyền.

## 6.2 UC-41 — Archive/Restore/Hard Delete

Actor:
- Giáo vụ;
- Quản trị viên.

Scope:

```text
Giáo vụ → Khoa/Bộ môn
QTV → toàn trường
```

## 6.3 Hard Delete

Chỉ được Hard Delete khi **đồng thời**:

```text
student_count = 0
AND
assignment_count = 0
AND
schedule_count = 0
```

Nếu bất kỳ điều kiện nào không thỏa:

```text
Hard Delete = BLOCKED
→ Archive
```

Không Hard Delete lớp đã phát sinh dữ liệu học vụ.

---

# 7. ASSIGNMENT CONFIGURATION

## 7.1 Ranh giới UC

```text
UC-21 → tạo/cấu hình bài tập lần đầu
UC-22 → thông tin chung
UC-24 → Deadline
UC-25 → Test Cases
UC-26 → Rubric
```

Không để các UC này chồng lấn trách nhiệm.

## 7.2 UC-21

Tạo bài tập mới và cấu hình lần đầu:
- tên;
- đề bài;
- ngôn ngữ;
- độ khó;
- giới hạn tài nguyên;
- deadline;
- Max Submissions;
- Highest/Latest Score;
- chính sách nộp muộn;
- test cases;
- rubric.

UC-21 không thay thế các UC chỉnh sửa độc lập sau khi bài tập đã tồn tại.

## 7.3 UC-22

Chỉ chỉnh sửa:
- tên;
- đề bài;
- ngôn ngữ;
- độ khó;
- giới hạn tài nguyên.

Không chỉnh:
- Deadline;
- Test Cases;
- Rubric.

Không tự thêm versioning nếu hệ thống chưa định nghĩa chính sách quản lý phiên bản.

## 7.4 UC-24

- Thiết lập Deadline.
- Cập nhật/gia hạn Deadline.
- Không bắt buộc bài tập phải đã giao mới được cấu hình Deadline; bài tập tồn tại + có quyền là điều kiện chính.

## 7.5 UC-25

Test Case gồm:
- Input;
- Expected Output;
- Sample/Hidden;
- trọng số.

Có thể:
- thêm;
- sửa;
- xóa.

Hidden Test Case không được lộ dữ liệu bí mật cho Sinh viên.

## 7.6 UC-26

Rubric gồm:
- tiêu chí;
- mô tả;
- mức điểm;
- trọng số.

`Correctness` được tính từ Test Cases.

Tổng trọng số phải hợp lệ.

---

# 8. GIAO BÀI

UC-27:

```text
Chọn bài tập
→ chọn lớp
→ xác nhận giao
```

Chỉ được giao vào lớp mà Giáo viên có quyền quản lý.

Lớp không Hoạt động:

```text
Không được giao bài.
```

---

# 9. STUDENT CODE WORKSPACE

## 9.1 Draft

- Autosave.
- Có thể khôi phục bản nháp gần nhất.
- Draft chưa phải Submission.

## 9.2 Upload source

Upload:
- kiểm tra extension;
- kiểm tra kích thước;
- kiểm tra khả năng đọc;
- nạp vào editor;
- lưu draft.

**Upload code không tạo Submission.**

---

# 10. SUBMISSION — CORE BUSINESS RULE

## 10.1 Mỗi Submit hợp lệ = một Submission

```text
Source A
→ Submit
→ Submission #1

Source A chỉnh sửa
→ Submit
→ Submission #2
```

Submission cũ không bị ghi đè.

## 10.2 Không sửa trực tiếp Submission cũ

Muốn nộp phiên bản mới:

```text
Submission cũ
→ Reuse source
→ Edit
→ Submit
→ Submission mới
```

## 10.3 submission_count

Chỉ Submission hợp lệ mới tăng:

```text
submission_count
```

Các trường hợp không tăng:
- System failure;
- Execution interruption;
- Teacher-authorized failure/exemption.

## 10.4 Submit history

Mọi click `Submit` phải được lưu log để:
- Audit;
- Debug;
- theo dõi Submission;
- điều tra lỗi.

Nhưng:

```text
Submit click log ≠ valid Submission
```

---

# 11. SUBMISSION LIMIT

## 11.1 Max Submissions

```text
N > 0
→ tối đa N Submission hợp lệ

N = 0 hoặc blank
→ Unlimited
```

Khi:

```text
submission_count >= Max Submissions
```

→ không tạo Submission mới.

Không dùng số lượng click Submit để tính attempt.

---

# 12. DEADLINE & LATE SUBMISSION

## Đúng hạn

Submission hợp lệ khi:

```text
Current Time <= Deadline
AND
còn lượt nộp
AND
bài/lớp cho phép nộp
```

## Nộp muộn

Chỉ nhận nếu bài tập cho phép và còn trong late window:

```text
Current Time <= Late Deadline
AND
còn lượt nộp
```

Nếu được phép:
- áp dụng Late Penalty theo cấu hình.

Hết late window:

```text
Reject
→ không tạo Submission
```

---

# 13. SUBMISSION PROCESSING

Luồng chuẩn:

```text
Student writes code
→ Submit
→ check permission
→ check deadline
→ check attempt
→ check source/language
→ create Submission(PENDING)
→ queue
→ Grader Worker
→ Docker Sandbox
→ Execution Evidence
→ Auto-Grader
→ Static Analysis (nếu cấu hình)
→ AI Analysis
→ save results
→ COMPLETED
```

## Trạng thái

```text
PENDING
RUNNING
COMPLETED
Bị gián đoạn
```

---

# 14. DOCKER SANDBOX

Mã nguồn phải được thực thi trong môi trường cách ly.

Docker Sandbox:
- compile nếu cần;
- execute;
- giới hạn tài nguyên;
- thu execution evidence.

Execution Evidence có thể gồm:
- output;
- error;
- execution time;
- memory;
- trạng thái từng test.

Hidden Test Case được dùng để chấm nhưng không lộ Input/Output bí mật.

---

# 15. INTERRUPTION / SYSTEM FAILURE

Nếu execution bị dừng/gián đoạn:

```text
Submission
→ Bị gián đoạn
```

Bắt buộc:

- Không auto regrade.
- Không tự tạo Submission mới.
- Không tăng `submission_count`.
- Sinh viên phải **Submit lại**.
- Submission cũ vẫn được giữ.
- Sự kiện phải được ghi nhận phù hợp trong log.

Trạng thái chuẩn là:

```text
Bị gián đoạn
```

Không dùng cách ghi mơ hồ kiểu `lỗi/bị gián đoạn`.

Rule này phải đồng bộ giữa UC-11, UC-12 và UC-46.

---

# 16. AUTO-GRADER

Auto-Grader dựa trên:
- Execution Evidence;
- Test Cases;
- Rubric.

`Correctness` được tính từ kết quả Test Cases theo trọng số.

Nếu có Static Analysis:
- dùng để cung cấp evidence cho Code Quality/Complexity;
- điểm tổng hợp theo Rubric.

AI không được trở thành nguồn duy nhất của Auto-Grader.

---

# 17. AI ANALYSIS & FEEDBACK

AI có thể:
- phân tích source code;
- phân tích execution/test evidence;
- đánh giá theo Rubric;
- tạo feedback;
- giải thích lỗi;
- gợi ý cải thiện.

Luồng:

```text
Source Code
+ Execution Evidence
+ Rubric
→ AI
→ Feedback / AI Assessment
```

AI phải dựa trên evidence liên quan.

## AI Score

```text
AI Score ≠ Official Score
```

AI Score chỉ:

```text
Tham khảo
```

trừ khi sau này có business rule mới được chốt rõ ràng.

---

# 18. SCORING

## 18.1 Có Manual Score

```text
Manual Score
→ Official Score
```

Auto-Grader và AI giữ lại để tham khảo.

## 18.2 Chưa có Manual Score

Dùng Auto-Grader theo policy của bài:

```text
Highest Score
hoặc
Latest Score
```

Hiển thị:

```text
Tạm tính
```

## 18.3 Highest Score

Ví dụ:

```text
#1 → 50
#2 → 70
#3 → 60
```

Policy = Highest Score:

```text
Tạm tính = 70
```

## 18.4 Latest Score

Nếu Submission cuối = 60:

```text
Policy = Latest Score
→ Tạm tính = 60
```

## 18.5 Không tự gán 0

```text
Chưa có kết quả ≠ 0 điểm
```

Dùng trạng thái như:
- Đang chờ chấm;
- Chưa có kết quả.

---

# 19. MANUAL GRADING

Giáo viên:

```text
Chọn bài tập
→ chọn Sinh viên
→ xem Submission
→ xem source
→ đánh giá theo Rubric
→ nhập điểm
→ nhập nhận xét
→ lưu
```

Khi lưu hợp lệ:

```text
Manual Score → Official Score
```

Nếu chỉ lưu tạm:

```text
Chưa áp dụng điểm thủ công
```

---

# 20. STUDENT VISIBILITY

Sinh viên chỉ xem dữ liệu thuộc quyền của mình.

Được xem:
- bài tập được giao;
- Submission của bản thân;
- Auto-Grader result;
- điểm được phép hiển thị;
- AI feedback được phép hiển thị.

Không được xem:
- Submission của người khác;
- Hidden Test Case Input/Output;
- dữ liệu nội bộ Grader;
- AI Key;
- System Logs;
- cấu hình kỹ thuật nhạy cảm.

---

# 21. CLASS ACTOR MATRIX

| Chức năng | Giáo viên | Giáo vụ | QTV | System Admin |
|---|:---:|:---:|:---:|:---:|
| Tạo lớp | ✓ | ✓ | ✓ | ✗ |
| Chỉnh sửa lớp | ✓ | ✓ | ✓ | ✗ |
| Đóng/Mở lớp | ✓ | ✓ | ✓ | ✗ |
| Archive | ✗ | ✓ | ✓ | ✗ |
| Restore | ✗ | ✓ | ✓ | ✗ |
| Hard Delete | ✗ | ✓ | ✓ | ✗ |
| Quản lý SV trong lớp | ✓ | ✓ | ✓ | ✗ |
| Phân công GV | ✗ | ✓ | ✓ | ✗ |

Scope:
- Giáo viên → lớp mình phụ trách.
- Giáo vụ → Khoa/Bộ môn được phân công.
- QTV → toàn trường.
- System Admin → không có scope nghiệp vụ lớp.

---

# 22. ORGANIZATION / KHOA / BỘ MÔN / GIÁO VỤ

Quản trị viên quản lý:
- Tổ chức;
- Khoa/Bộ môn;
- cơ cấu trực thuộc;
- phân công Giáo vụ.

Một Giáo vụ có thể phụ trách một hoặc nhiều Khoa/Bộ môn.

Giáo vụ không được thao tác trên lớp ngoài phạm vi được phân công.

---

# 23. SYSTEM ADMINISTRATION

## AI
- AI configuration.
- AI Key.
- Thông số AI.

## Docker
- Cấu hình Docker Sandbox.
- Giám sát Docker.
- Theo dõi execution.
- Dừng execution nếu được phân quyền.

## System Logs
- Xem.
- Tìm kiếm.
- Lọc.
- Xem chi tiết.
- Theo dõi lỗi/vận hành.

Dừng execution:

```text
Execution stopped
→ Bị gián đoạn
→ không auto regrade
→ không tăng submission_count
→ Sinh viên Submit lại
```

---

# 24. DATA INTEGRITY

Không làm mất liên kết:

```text
Student
→ Class
→ Assignment
→ Submission
→ Auto-Grader
→ AI Feedback
→ Manual Score
```

Submission là lịch sử độc lập.

Không ghi đè Submission cũ bằng Submission mới.

Điểm phải phân biệt nguồn:

```text
Manual
Auto-Grader
AI
```

và trạng thái:

```text
Official
Tạm tính
Tham khảo
```

---

# 25. STATUS VOCABULARY

## Class

```text
Hoạt động
Đã đóng
Lưu trữ
```

## Submission

```text
PENDING
RUNNING
COMPLETED
Bị gián đoạn
```

## Score

```text
Official Score
Tạm tính
Tham khảo
```

Thuật ngữ phải thống nhất giữa SRS, UI, DB, API và test.

---

# 26. UC BOUNDARY MAP

## Authentication

```text
UC-01 → Đăng nhập
UC-02 → Đăng xuất
UC-03 → Quên mật khẩu
UC-04 → Xem thông tin cá nhân
UC-05 → Cập nhật thông tin cá nhân
UC-06 → Đổi mật khẩu
```

## Student

```text
UC-07 → Xem danh sách bài tập
UC-08 → Xem chi tiết bài tập
UC-09 → Viết code
UC-10 → Tải tệp bài làm
UC-11 → Nộp bài
UC-12 → Xem kết quả Auto-Grader
```

## Assignment

```text
UC-21 → Tạo/cấu hình lần đầu
UC-22 → Thông tin chung
UC-24 → Deadline
UC-25 → Test Cases
UC-26 → Rubric
UC-27 → Giao bài
```

## Administration

```text
UC-32 → Tạo tài khoản
UC-33 → Khóa/Mở khóa
UC-34 → Xóa tài khoản
UC-35 → Phân quyền
UC-36 → Reset mật khẩu
UC-37 → Import Excel/CSV
```

## Class

```text
UC-17 → UC-20
→ cấp Giáo viên

UC-38 → UC-43
→ cấp Giáo vụ/QTV
```

**UC-19 không sử dụng.**

## System

Các UC kỹ thuật từ nhóm UC-44 trở đi phải giữ đúng ranh giới System Admin và không kéo sang nghiệp vụ lớp.

---

# 27. QUY TẮC KHÔNG DUPLICATE UC

Nếu một UC chuyên trách một cấu hình/chức năng thì UC khác không mô tả lại nó như chức năng chính.

Ví dụ:

```text
Deadline → UC-24
Test Cases → UC-25
Rubric → UC-26
Close/Open → UC-40
Archive/Restore/Delete → UC-41
```

Không tạo thêm UC hoặc flow chính trùng các chức năng trên.

---

# 28. CHECK LOGIC CHO MỖI UC

Trước khi chốt một UC, kiểm tra:

### Actor
- đúng actor;
- đúng scope;
- System Admin không bị lẫn với QTV nghiệp vụ.

### Precondition
- thực sự cần;
- không mâu thuẫn flow;
- không thêm điều kiện nghiệp vụ thừa.

### Main Flow
- đúng actor;
- không chứa nghiệp vụ thuộc UC khác;
- không duplicate.

### Alternative Flow
- là nhánh thực sự;
- không lặp Main Flow.

### Exception
- nguyên nhân rõ;
- không làm mất dữ liệu;
- trạng thái sau lỗi rõ.

### Postcondition
- biết dữ liệu nào được tạo/sửa;
- biết status sau thao tác;
- biết count có thay đổi hay không.

---

# 29. GOLDEN RULES

## Rule 01 — Scope trước Action

Có quyền thực hiện Action không đồng nghĩa có quyền trên mọi Resource.

```text
Role + Scope + Resource
```

## Rule 02 — Business Admin ≠ System Admin

```text
QTV = nghiệp vụ đào tạo
System Admin = kỹ thuật nền tảng
```

## Rule 03 — Submission hợp lệ mới tính lượt

```text
Valid Submission → count
System Failure → no count
Interrupted → no count
```

## Rule 04 — Interrupted không auto regrade

```text
Bị gián đoạn
→ không auto regrade
→ không tạo Submission mới
→ Student Submit lại
```

## Rule 05 — Submission không overwrite

```text
Submit mới → Submission mới
```

## Rule 06 — Chưa có điểm ≠ 0

```text
No Result ≠ 0
```

## Rule 07 — Manual Score ưu tiên

```text
Manual → Official
```

## Rule 08 — Auto-Grader khi chưa có Manual

```text
No Manual
→ Highest/Latest
→ Tạm tính
```

## Rule 09 — AI không tự thành Official

```text
AI → Tham khảo
```

## Rule 10 — Hard Delete bảo vệ dữ liệu

```text
0 Student
AND
0 Assignment
AND
0 Schedule
→ Hard Delete allowed
```

Nếu không → Block → Archive.

## Rule 11 — Restore không tự mở lớp

```text
Archive → Restore → Đã đóng
```

## Rule 12 — Hidden Test Case không lộ dữ liệu

Sinh viên chỉ thấy kết quả cần thiết, không thấy dữ liệu bí mật.

## Rule 13 — Upload ≠ Submit

```text
Upload → Draft
Submit → Submission
```

## Rule 14 — Submit log ≠ Submission count

```text
Submit click → Audit Log
Valid Submission → submission_count + 1
```

## Rule 15 — Không tự suy diễn business rule mới

Nếu logic mới chưa được chốt:
- không tự thêm vào UC;
- xác định business rule trước;
- sau đó cập nhật RULES.md và UC liên quan.

---

# 30. NOTE CHO DATABASE / API

## Submission

Phải phân biệt Submission theo từng lần nộp.

Không dùng một record duy nhất cho toàn bộ lịch sử.

## Score

Nên phân biệt:

```text
manual_score
auto_grader_score
ai_score
```

và nguồn/trạng thái tương ứng.

## Count

Không tính:

```text
COUNT(Submit logs)
```

để ra số lần nộp.

Chỉ tính Submission hợp lệ.

## Class

Phải kiểm soát transition:

```text
ACTIVE ↔ CLOSED
CLOSED → ARCHIVED
ARCHIVED → CLOSED
```

Không cho transition tùy ý.

## Authorization

Không chỉ kiểm tra:

```text
user.role
```

mà phải kiểm tra cả:

```text
user.role
+ scope
+ resource
```

---

# 31. NOTE CHO USE CASE DIAGRAM

Không biến mọi bước kỹ thuật thành một Use Case riêng.

Các bước nội bộ như:
- kiểm tra quyền;
- kiểm tra deadline;
- tính điểm;
- lưu kết quả;
- chạy Docker;
- gọi AI;

không tự động trở thành Actor/UC độc lập.

Các thành phần:

```text
Docker Sandbox
AI Engine
Database
Queue
WebSocket
```

là thành phần hệ thống, không mặc nhiên là Actor của Use Case Diagram.

Actor phải nối đúng phạm vi:

```text
Giáo viên → nghiệp vụ lớp/bài tập của mình
Giáo vụ → nghiệp vụ Khoa/Bộ môn
QTV → nghiệp vụ toàn trường
System Admin → kỹ thuật hệ thống
```

---

# 32. QUY TRÌNH KHI THAY ĐỔI SRS

Khi thay đổi một business rule:

```text
RULES.md
→ Use Case
→ Use Case Diagram
→ ERD / Database
→ API
→ UI
→ Test Case
```

Các rule có tính lan truyền cao:
1. Max Submissions.
2. Highest/Latest Score.
3. Late Submission.
4. Manual Score.
5. AI Score.
6. Class Lifecycle.
7. Role Scope.
8. Hard Delete.
9. Interrupted Execution.
10. Account Lifecycle.

---

# 33. FINAL CHECKLIST

- [ ] Actor đúng.
- [ ] Scope đúng.
- [ ] QTV và System Admin không bị trộn.
- [ ] Giáo vụ có scope Khoa/Bộ môn.
- [ ] Giáo viên chỉ quản lý lớp phụ trách.
- [ ] QTV có phạm vi toàn trường.
- [ ] Class có 3 trạng thái chính.
- [ ] Close/Open tách khỏi Archive/Delete.
- [ ] Hard Delete có đủ 3 điều kiện 0 Student + 0 Assignment + 0 Schedule.
- [ ] Restore → Đã đóng.
- [ ] UC-21 chỉ tạo/cấu hình lần đầu.
- [ ] UC-22 chỉ thông tin chung.
- [ ] UC-24 chỉ Deadline.
- [ ] UC-25 chỉ Test Cases.
- [ ] UC-26 chỉ Rubric.
- [ ] Upload code không tạo Submission.
- [ ] Mỗi Submission hợp lệ là một record riêng.
- [ ] Có Max Submissions.
- [ ] 0/blank = Unlimited.
- [ ] Chỉ Submission hợp lệ tăng count.
- [ ] Late Submission có window + penalty.
- [ ] Interrupted = Bị gián đoạn.
- [ ] Interrupted không auto regrade.
- [ ] Interrupted không tăng count.
- [ ] Sinh viên phải Submit lại.
- [ ] Highest/Latest áp dụng đúng policy.
- [ ] Manual Score = Official.
- [ ] Auto-Grader khi chưa có Manual = Tạm tính.
- [ ] AI = Tham khảo.
- [ ] Chưa có kết quả ≠ 0.
- [ ] Hidden Test Cases không lộ dữ liệu.
- [ ] Submit log tách khỏi Submission count.
- [ ] System Admin chỉ xử lý kỹ thuật.
- [ ] Không tạo UC trùng chức năng.
- [ ] Không tự thêm business rule chưa được chốt.

---

# 34. GOLDEN FLOW

```text
ACCOUNT
   ↓
Login
   ↓
Role + Scope
   │
   ├── Student
   │      ↓
   │   Assignment
   │      ↓
   │   Write Code
   │      ↓
   │   Draft
   │      ↓
   │   Submit
   │      ↓
   │   Permission + Deadline + Attempt
   │      ↓
   │   Valid?
   │    ┌─┴─┐
   │   NO  YES
   │    │    ↓
   │ Reject Submission
   │         ↓
   │       Queue
   │         ↓
   │       Docker
   │         ↓
   │ Execution Evidence
   │         ↓
   │ Auto-Grader
   │         ↓
   │ AI Analysis
   │         ↓
   │ Save Results
   │         ↓
   │ Score Policy
   │      ┌──┴──┐
   │ Manual   No Manual
   │   ↓          ↓
   │ Official  Highest/Latest
   │              ↓
   │           Tạm tính
   │
   └── Staff/Admin
          ↓
       nghiệp vụ
       theo Role + Scope
```

Nếu execution bị dừng:

```text
Execution
→ Bị gián đoạn
→ không auto regrade
→ không tăng submission_count
→ Sinh viên Submit lại
```

---

# 35. SOURCE OF TRUTH PRIORITY

Khi có mâu thuẫn tài liệu:

1. Business Rule đã được chốt là ưu tiên.
2. Cập nhật RULES.md theo quyết định mới nhất.
3. Đồng bộ tất cả UC liên quan.
4. Đồng bộ Use Case Diagram.
5. Đồng bộ Database/API/UI/Test.

> **Không dùng một câu riêng lẻ trong một UC để tự ý thay đổi business rule chung của hệ thống.**

# END

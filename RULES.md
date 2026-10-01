# RULES.md — BỘ QUY TẮC NGHIỆP VỤ MASTER
# Nền tảng AI-Powered Coding Tutor & Auto-Grader

> **Source of Truth duy nhất** cho các quyết định nghiệp vụ, business rules, ràng buộc logic và các tài liệu liên quan (Use Case, Activity Diagram, Sequence Diagram, Database, API, UI và Test).
>
> **Nguyên tắc ưu tiên:** Rule được chốt sau cùng trong tài liệu này sẽ ưu tiên và thay thế rule cũ nếu có mâu thuẫn.

---

# I. TỔNG QUAN HỆ THỐNG

Hệ thống là nền tảng hỗ trợ đào tạo lập trình, cho phép:
- Sinh viên làm bài lập trình trực tiếp trên hệ thống.
- Sinh viên viết/chỉnh sửa/upload mã nguồn.
- Autosave và lưu bản nháp (Draft).
- Nộp bài chính thức.
- Tự động khóa bài khi Sinh viên nộp hoặc khi hết deadline.
- Auto-submit bản code cuối cùng khi Sinh viên chưa chủ động nộp.
- Chấm bài theo đợt (Batch Grading) sau deadline.
- Thực thi mã nguồn bằng Docker Sandbox.
- Auto-Grader chấm dựa trên Hidden Test Cases.
- Phân tích chất lượng/độ tối ưu mã nguồn.
- AI Review tạo phản hồi dựa trên evidence.
- Đối soát trùng lặp mã nguồn/đạo văn (Plagiarism Check).
- Giáo viên xem kết quả và chấm thủ công.
- Giáo viên xác nhận điểm chính thức.
- Sinh viên xem kết quả và sử dụng AI Tutor để hậu kiểm sau đánh giá.

### Quy tắc thực thi mã nguồn của Sinh viên:
- **Sinh viên không được chạy thử mã nguồn trên các Sample Test Cases.**
- **Hệ thống không cung cấp chức năng cho Sinh viên chủ động thực thi code trên Sample Test Cases trong thời gian làm bài.**
- Việc thực thi mã nguồn được thực hiện bởi hệ thống trong quy trình Batch Grading sau Deadline thông qua Docker Sandbox.
- Hệ thống không theo hướng LLM-only. AI phải sử dụng context/evidence từ:
  - Mã nguồn.
  - Kết quả thực thi.
  - Test Cases.
  - Phân tích mã nguồn.
  - Rubric/thông tin bài tập.

---

# II. TÁC NHÂN (ACTORS) & PHẠM VI

Tất cả tác nhân được định danh chuẩn bằng Tiếng Việt:
1. **Sinh viên**
2. **Giáo viên**
3. **Quản trị viên** (Phòng Đào tạo)
4. **Giáo vụ** (Khoa / Bộ môn)
5. **Quản trị viên hệ thống** (IT Vận hành nền tảng)

---

## 1. Sinh viên
- **Quyền hạn:**
  - Đăng nhập / đăng xuất / quên mật khẩu / đổi mật khẩu / xem và cập nhật thông tin cá nhân.
  - Xem lớp mình tham gia.
  - Xem bài tập được giao (UC-07, UC-08).
  - Làm bài: viết/chỉnh sửa code (UC-09), Upload file bài làm (UC-10), lưu bản nháp, autosave.
  - Nộp bài chính thức (UC-11 - Explicit Submit hoặc Auto-submit khi hết giờ).
  - Xem bài đã nộp (UC-15 - bản nộp duy nhất).
  - Xem kết quả Auto-Grader được phép công bố (UC-12).
  - Xem AI Review được phép công bố (UC-13).
  - Xem bảng điểm cá nhân & điểm chính thức sau khi Giáo viên xác nhận (UC-16).
  - Tương tác với AI Tutor sau đánh giá để hậu kiểm (UC-14).
- **Ràng buộc:**
  - Sinh viên không được chạy thử mã nguồn trên Sample Test Cases.
  - Sinh viên chỉ được truy cập dữ liệu thuộc quyền của mình.

---

# III. GIÁO VIÊN

- **Phạm vi:** Các lớp / bài tập do Giáo viên được phân công phụ trách.
- **Quyền hạn:**
  - Đóng / mở lại lớp do mình phụ trách (UC-40).
  - Tạo bài tập và cấu hình ban đầu (UC-21).
  - Chỉnh sửa thông tin chung bài tập (UC-22).
  - Xóa / vô hiệu hóa bài tập (UC-23).
  - Thiết lập Deadline (UC-24).
  - Thiết lập Test Cases (UC-25).
  - Thiết lập Rubric (UC-26).
  - Giao bài tập cho lớp (UC-27).
  - Xem bài nộp (UC-28).
  - Xem điểm (UC-29).
  - Xem AI đánh giá & kết quả đối soát trùng lặp (UC-30).
  - Chấm thủ công và xác nhận điểm chính thức (UC-31).
  - Xem kết quả / bảng điểm của lớp mình phụ trách.
- **Lưu ý đặc tả:**
  - *Đã bỏ UC-17 (Tạo lớp học của Giáo viên), UC-18 (Chỉnh sửa lớp của Giáo viên), UC-20 (Quản lý sinh viên của Giáo viên)*. Việc tạo lớp, sửa lớp và quản lý sinh viên trong lớp được tập trung quản lý tại cấp Quản trị viên / Giáo vụ (UC-38, UC-39, UC-42).

---

# IV. QUẢN TRỊ VIÊN

- **Định danh:** Quản trị viên = Phòng Đào tạo / Người quản lý nghiệp vụ đào tạo.
- **Phạm vi:** Toàn trường về nghiệp vụ đào tạo.
- **Quyền hạn:**
  - Tạo tài khoản Sinh viên, Giáo viên, Giáo vụ (UC-32).
  - Khóa / mở khóa tài khoản (UC-33).
  - Xóa tài khoản (UC-34 - Soft Delete nếu có dữ liệu học tập).
  - Phân quyền người dùng trong phạm vi nghiệp vụ đào tạo (UC-35).
  - Đặt lại mật khẩu (UC-36).
  - Nhập danh sách từ Excel/CSV (UC-37 - 5 cột: Mã người dùng, Họ tên, Email, Vai trò, Lớp).
  - Quản lý lớp toàn trường: Tạo lớp (UC-38), Chỉnh sửa lớp (UC-39), Đóng / mở lại lớp (UC-40), Archive / Restore / Hard Delete lớp nếu đủ điều kiện (UC-41).
  - Quản lý Sinh viên trong lớp cấp toàn trường (UC-42).
  - Phân công Giáo viên vào lớp cấp toàn trường (UC-43).
  - Quản lý cơ cấu tổ chức, Khoa / Bộ môn và phân công Giáo vụ (UC-47).

---

# V. GIÁO VỤ

- **Định danh:** Giáo vụ là actor riêng biệt, không gộp vào Quản trị viên.
- **Phạm vi:** Khoa / Bộ môn được phân công phụ trách.
- **Quyền hạn:**
  - Tạo lớp trong phạm vi Khoa/Bộ môn (UC-38).
  - Chỉnh sửa lớp trong phạm vi Khoa/Bộ môn (UC-39).
  - Đóng / mở lại lớp trong phạm vi Khoa/Bộ môn (UC-40).
  - Archive / Restore / Hard Delete lớp trong phạm vi Khoa/Bộ môn nếu đủ điều kiện (UC-41).
  - Quản lý Sinh viên trong lớp thuộc Khoa/Bộ môn (UC-42).
  - Phân công Giáo viên vào lớp thuộc Khoa/Bộ môn (UC-43).
- **Ràng buộc:** Giáo vụ không được thao tác ngoài Khoa/Bộ môn được phân công.

---

# VI. QUẢN TRỊ VIÊN HỆ THỐNG

- **Định danh:** Quản trị viên hệ thống = IT / Người vận hành kỹ thuật nền tảng.
- **Phụ trách:**
  - Quản lý cấu hình AI, API Key, tham số mô hình AI (UC-44).
  - Cấu hình Docker Sandbox (UC-45).
  - Giám sát Docker Sandbox, theo dõi execution (UC-46).
  - Quản lý System Logs (UC-48).
  - Phân quyền cấp hệ thống (UC-35: cấp vai trò Quản trị viên / Quản trị viên hệ thống).
- **Đặc biệt (Ràng buộc nghiêm ngặt):**
  - Quản trị viên hệ thống **không** quản lý nghiệp vụ lớp học hay đào tạo.
  - **Không được:** Tạo lớp, chỉnh sửa lớp, đóng lớp, mở lớp, archive lớp, restore lớp, hard delete lớp, quản lý Sinh viên trong lớp, phân công Giáo viên, quản lý tổ chức / Khoa / Bộ môn (không tham gia UC-38, UC-39, UC-40, UC-41, UC-42, UC-43, UC-47).

---

# VII. PHẠM VI QUẢN LÝ LỚP

| Tác nhân (Actor) | Phạm vi |
|---|---|
| **Giáo viên** | Đóng / mở lớp mình được phân công phụ trách (UC-40) |
| **Giáo vụ** | Khoa/Bộ môn được phân công (UC-38 $\rightarrow$ UC-43) |
| **Quản trị viên** | Toàn trường (UC-38 $\rightarrow$ UC-43, UC-47) |
| **Quản trị viên hệ thống** | Không quản lý nghiệp vụ lớp |

---

# VIII. LIFECYCLE LỚP HỌC

```text
Hoạt động
    ↓ Đóng (UC-40)
Đã đóng
    ↓ Lưu trữ (UC-41)
Lưu trữ
```

### 1. Đóng lớp (UC-40)
- **Tác nhân:** Giáo viên (lớp phụ trách), Giáo vụ (Khoa/Bộ môn), Quản trị viên (toàn trường).
- Chuyển trạng thái: `Hoạt động` $\rightarrow$ `Đã đóng`.
- Lớp đã đóng: Ngăn các hoạt động học tập bình thường; dữ liệu vẫn được bảo toàn; có thể mở lại theo quyền.

### 2. Mở lại lớp (UC-40)
- **Tác nhân:** Giáo viên, Giáo vụ, Quản trị viên.
- Chuyển trạng thái: `Đã đóng` $\rightarrow$ `Hoạt động`.

### 3. Archive (Lưu trữ lớp - UC-41)
- **Tác nhân:** Giáo vụ (trong phạm vi Khoa/Bộ môn), Quản trị viên (trên toàn trường).
- Chuyển trạng thái: `Đã đóng` $\rightarrow$ `Lưu trữ`.
- Lớp lưu trữ: Không xuất hiện trong danh sách vận hành thông thường; dữ liệu vẫn được bảo lưu.

### 4. Restore (Khôi phục lớp - UC-41)
- **Tác nhân:** Giáo vụ, Quản trị viên.
- Chuyển trạng thái: `Lưu trữ` $\rightarrow$ `Đã đóng`.
- **Restore không tự động đưa lớp về Hoạt động.** Muốn hoạt động lại:
  ```text
  Lưu trữ ──(Restore UC-41)──> Đã đóng ──(Mở lại UC-40)──> Hoạt động
  ```

### 5. Hard Delete (Xóa vĩnh viễn - UC-41)
- Chỉ được Hard Delete khi thỏa mãn đồng thời:
  ```text
  student_count = 0
  AND
  assignment_count = 0
  ```
  *(Tức là: 0 Sinh viên và 0 bài tập).*
- Nếu chỉ cần 1 trong 2 điều kiện không đạt: **Hard Delete bị chặn $\rightarrow$ chuyển sang Archive (Lưu trữ).**
- Rule này áp dụng cho Giáo vụ và Quản trị viên. Quản trị viên hệ thống không tham gia lifecycle lớp.

---

# IX. UC ĐÃ BỊ HỦY BỎ (UC-17, UC-18, UC-19, UC-20)

- **UC-17 (Tạo lớp học của Giáo viên):** Đã bỏ. Chức năng tạo lớp tập trung ở cấp Quản trị viên / Giáo vụ (UC-38).
- **UC-18 (Chỉnh sửa lớp của Giáo viên):** Đã bỏ. Chức năng chỉnh sửa lớp tập trung ở cấp Quản trị viên / Giáo vụ (UC-39).
- **UC-19 (Đóng/Mở lớp của Giáo viên):** Đã bỏ hoàn toàn để tránh trùng lặp với UC-40.
- **UC-20 (Quản lý sinh viên của Giáo viên):** Đã bỏ. Chức năng quản lý sinh viên trong lớp tập trung ở cấp Quản trị viên / Giáo vụ (UC-42).

---

# X. CẤU HÌNH BÀI TẬP

Một bài tập bao gồm các nhóm thông tin:
1. **Thông tin chung:** Tên bài, đề bài / mô tả, ngôn ngữ lập trình, độ khó, giới hạn thời gian chạy, giới hạn bộ nhớ / tài nguyên.
2. **Deadline:** Có một thời điểm kết thúc nhận bài. Sau thời điểm này hệ thống đóng hoàn toàn, không nhận bài mới.
3. **Test Cases:** Gồm Sample Test Cases và Hidden Test Cases (Input, Expected Output, Trọng số điểm).
   - *Quy tắc Sample Test Cases:* Sample Test Cases không phải chức năng chạy thử dành cho Sinh viên. Sinh viên không được chủ động thực thi mã nguồn trên Sample Test Cases.
4. **Rubric:** Tiêu chí, mô tả, mức điểm / trọng số. Tiêu chí `Correctness` được tính tự động dựa trên kết quả Hidden Test Cases.

---

# XI. RANH GIỚI CÁC USE CASE CẤU HÌNH BÀI TẬP

- **UC-21 – Tạo bài tập:** Dùng để tạo bài tập và thiết lập cấu hình ban đầu (thông tin chung, ngôn ngữ, độ khó, giới hạn tài nguyên, deadline ban đầu, cấu hình ban đầu cần thiết cho Test Case/Rubric).
- **UC-22 – Chỉnh sửa thông tin chung:** Chỉ xử lý Tên, Đề bài, Ngôn ngữ, Độ khó, Giới hạn tài nguyên. **Không** xử lý Deadline, Test Cases, Rubric.
- **UC-24 – Thiết lập hạn nộp:** Chỉ xử lý Deadline.
- **UC-25 – Thiết lập Test Case:** Chỉ xử lý Test Cases (Thêm, Sửa, Xóa, Sample/Hidden, Input, Output, Trọng số). Việc cấu hình Sample Test Cases không đồng nghĩa với việc cung cấp chức năng chạy thử cho Sinh viên.
- **UC-26 – Thiết lập Rubric:** Chỉ xử lý Rubric (Tiêu chí, Mô tả, Trọng số, Mức điểm).
- **UC-27 – Giao bài tập cho lớp:** Chỉ xử lý việc giao bài tập cho một hoặc nhiều lớp. **Không** đưa logic Max Submission / Scoring Policy / Late Submission vào UC-27.

---

# XII. QUY TẮC NỘP BÀI — BẢN MỚI NHẤT

### 1. Không còn Max Submissions
- Đã loại bỏ hoàn toàn: Max Submissions, Attempt limit, Unlimited attempts, `submission_count` dùng để giới hạn số lần nộp.

### 2. Không còn Highest Score / Latest Score
- Đã loại bỏ hoàn toàn: Highest Score, Latest Score, chính sách chọn điểm giữa nhiều Submission.
- Lý do: Mỗi Sinh viên chỉ có một bản nộp chính thức hiện tại cho một bài tập.

### 3. Không còn Late Submission (Strict No-Late Submission)
- Sau Deadline:
  - Không nhận Submission mới.
  - Không nhận chỉnh sửa code.
  - Không nhận Upload file bài làm.
  - Không nhận Save / Autosave.
  - Không nhận bất kỳ request gửi code mới nào.
- Backend phải chặn request sau Deadline (trả về lỗi `403 Forbidden` / `Assignment Closed`).
- Frontend: Hiển thị "Bài tập đã đóng", vô hiệu hóa Editor, ẩn/vô hiệu hóa nút Nộp bài.

---

# XIII. TRẠNG THÁI BÀI LÀM

Hệ thống sử dụng 4 trạng thái nghiệp vụ chính:

```text
DRAFT ──> SUBMITTED ──> GRADING ──> COMPLETED
```

1. **`DRAFT` (Bản nháp):**
   - Sinh viên đang làm bài trong thời gian mở bài tập ($T < T_{\text{deadline}}$).
   - Cho phép: Viết/sửa code, Upload file bài làm, Save thủ công, Autosave tự động.
   - **Không có chức năng Chạy thử mã nguồn trên Sample Test Cases cho Sinh viên.**
   - Chưa phải bài nộp chính thức.
2. **`SUBMITTED` (Đã nộp bài):**
   - Bài đã được chốt (Read-only).
   - Không sửa code, không Upload, không Save, không Submit lại.
   - Bản Submit được giữ nguyên cho đến khi Batch Grading bắt đầu sau Deadline.
3. **`GRADING` (Đang chấm gom sau Deadline):**
   - Bài được đưa vào quy trình chấm theo đợt sau Deadline: Message Queue $\rightarrow$ Docker Sandbox execution $\rightarrow$ Hidden Test Cases $\rightarrow$ Auto-Grader $\rightarrow$ AI Review $\rightarrow$ Anti-cheat / Plagiarism Check.
4. **`COMPLETED` (Đã đánh giá tự động hoàn tất):**
   - Đã có đầy đủ: Kết quả Test Cases, điểm Auto-Grader, AI feedback, kết quả đối soát trùng lặp/đạo văn.
   - Giáo viên sử dụng các kết quả này để hỗ trợ chấm thủ công và xác nhận điểm chính thức.

---

# XIV. DRAFT & AUTOSAVE

- Trong thời gian làm bài ($T < T_{\text{deadline}}$):
  ```text
  Viết / sửa / upload code ──> Autosave / Save thủ công ──> DRAFT
  ```
- Hệ thống hỗ trợ:
  - Autosave tự động (theo chu kỳ cấu hình, ví dụ 5–10s hoặc sau 2s ngừng gõ).
  - Save thủ công ("Lưu bài làm").

---

# XV. QUY TẮC CHẠY THỬ MÃ NGUỒN

- **Sinh viên không được Chạy thử mã nguồn trên các Sample Test Cases.**
- Không có nút / chức năng Run Code dành cho Sinh viên.
- Sinh viên chỉ viết, chỉnh sửa, Upload file bài làm, Save và Autosave code trong thời gian `DRAFT`.
- Việc thực thi mã nguồn thuộc quy trình đánh giá của hệ thống sau Deadline trong Docker Sandbox.

---

# XVI. UPLOAD FILE BÀI LÀM (UC-10)

```text
File mã nguồn ──> Editor ──> DRAFT
```
- Upload không phải Submission.
- Sinh viên vẫn có thể tiếp tục chỉnh sửa sau Upload nếu Deadline chưa đến và bài vẫn ở trạng thái `DRAFT`.

---

# XVII. EXPLICIT SUBMIT (NỘP BÀI THỦ CÔNG)

Quy trình nộp bài chủ động của Sinh viên:
1. Sinh viên chọn "Nộp bài".
2. Hệ thống kiểm tra bài còn trong thời gian nhận bài ($T < T_{\text{deadline}}$).
3. Hệ thống hiển thị popup xác nhận cảnh báo:
   > *"Sau khi nộp, bài làm sẽ bị khóa và không thể chỉnh sửa hoặc nộp lại."*
4. Sinh viên xác nhận.
5. Hệ thống lấy code `DRAFT` hiện tại.
6. Hệ thống tạo bản nộp chính thức: Chuyển `DRAFT` $\rightarrow$ `SUBMITTED`, ghi `trigger_type = MANUAL`.
7. Editor chuyển sang chế độ Read-only. Sinh viên bị khóa hoàn toàn, không được chỉnh sửa hay nộp lại.

---

# XVIII. KHÔNG CHỈNH SỬA SAU SUBMIT

- Rule này là **tuyệt đối**.
- Không có setting "Cho phép chỉnh sửa sau khi nộp = Có/Không".
- Sau khi Submit: `SUBMITTED` $\rightarrow$ `LOCKED` (Không Edit, Không Upload, Không Save, Không Submit lần 2).

---

# XIX. AUTO-SUBMIT KHI HẾT DEADLINE

Dành cho trường hợp Sinh viên chưa chủ động bấm "Nộp bài" trước thời điểm kết thúc:
- **Cơ chế:** Xử lý bằng Backend Worker / Cron Job / Scheduled Worker độc lập (không phụ thuộc vào Browser, kết nối mạng hay thiết bị của Sinh viên).
- **Quy trình:**
  1. Backend quét các bài vẫn ở trạng thái `DRAFT` của bài tập vừa hết hạn.
  2. Lấy bản Autosave / Save mới nhất được lưu trên Database / Cache.
  3. Tạo bản Submission chính thức: Chuyển `DRAFT` $\rightarrow$ `SUBMITTED`, ghi `trigger_type = AUTO_EXPIRED`.
  4. Khóa Editor trên giao diện người dùng.

---

# XX. CHỈ GIỮ MỘT BẢN NỘP DUY NHẤT

- Mỗi cặp **(Sinh viên + Bài tập)** chỉ có **1 bản nộp chính thức hiện tại**.
- Không lưu Submission #1, Submission #2, Submission #3.
- Không có lịch sử nhiều phiên bản Submission trong phạm vi bài tập.

---

# XXI. BATCH GRADING (CHẤM THEO ĐỢT SAU DEADLINE)

- Auto-Grader **không** chạy ngay khi Sinh viên bấm Submit.
- Toàn bộ bài nộp ở trạng thái `SUBMITTED` sẽ chờ đến khi Deadline đóng hoàn toàn.
- Trình tự:
  ```text
  Sinh viên Submit / Auto-submit
          ↓
      SUBMITTED
          ↓
     Chờ Deadline
          ↓
  Deadline đóng hoàn toàn
          ↓
  Chốt danh sách SUBMITTED
          ↓
    Message Queue
          ↓
       GRADING
  ```

---

# XXII. MANUAL GRADING & ĐIỂM CHÍNH THỨC

- Sau khi Batch Grading hoàn tất (`COMPLETED`):
  1. Giáo viên xem mã nguồn bản nộp cuối cùng, kết quả Auto-Grader, AI Review, Rubric, kết quả đối soát trùng lặp.
  2. Giáo viên đánh giá theo Rubric, nhập/chỉnh điểm, nhập nhận xét.
  3. Giáo viên xác nhận kết quả $\rightarrow$ Điểm chính thức (Official Score).
- `Teacher Score` $\rightarrow$ `Official Score`. Auto-Grader và AI chỉ là kết quả hỗ trợ.

---

# XXIII. AI TUTOR (HẬU KIỂM SOCRATIC)

- **AI Tutor là chức năng hậu kiểm sau đánh giá** (sau khi đã có kết quả đánh giá / công bố điểm).
- **AI Tutor không được dùng để hỗ trợ Sinh viên trong lúc đang làm bài (giai đoạn `DRAFT`).**
- Tiếp cận theo phương pháp Socratic (gợi mở, đặt câu hỏi định hướng, không đưa ngay đáp án). Context: Đề bài, code nộp cuối, Auto-Grader, AI Review, nhận xét GV, điểm chính thức.

---

# XXIV. SYSTEM ADMINISTRATION (QUẢN TRỊ HỆ THỐNG)

- **UC-44:** Quản lý cấu hình AI (Tác nhân: Quản trị viên hệ thống).
- **UC-45:** Cấu hình Docker Sandbox (Tác nhân: Quản trị viên hệ thống).
- **UC-46:** Giám sát Docker Sandbox (Tác nhân: Quản trị viên hệ thống).
- **UC-48:** Quản lý System Logs (Tác nhân: Quản trị viên hệ thống).

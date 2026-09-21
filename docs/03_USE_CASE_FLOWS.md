# 03. LUỒNG THỰC HIỆN CHI TIẾT CỦA CÁC USE CASE (USE CASE FLOWS)

---

## I. CÁC USE CASE XÁC THỰC & QUẢN TRỊ TÀI KHOẢN CHUNG

### UC-01 — Đăng Nhập
- **Mô tả**: Cho phép người dùng xác thực tài khoản để bắt đầu phiên làm việc trên hệ thống.
- **Tác nhân**: Student, Teacher, Admin, Super Admin.
- **Tiền điều kiện**:
  - Người dùng đã có tài khoản trong hệ thống.
  - Tài khoản chưa bị khóa hoặc vô hiệu hóa.
- **Hậu điều kiện**:
  - Phiên đăng nhập được tạo thành công.
  - Hệ thống cấp token xác thực và chuyển người dùng đến trang chính phù hợp với vai trò.
  - Nếu đăng nhập thất bại, phiên đăng nhập không được tạo và dữ liệu biểu mẫu vẫn được giữ để người dùng thử lại.
- **Luồng tương tác chính**:
  1. Người dùng truy cập trang đăng nhập `/login`.
  2. Hệ thống hiển thị biểu mẫu yêu cầu Email và Mật khẩu.
  3. Người dùng nhập thông tin tài khoản và chọn **"Đăng nhập"**.
  4. Hệ thống kiểm tra định dạng dữ liệu và tìm tài khoản tương ứng.
  5. Hệ thống đối chiếu mật khẩu với mật khẩu đã được băm trong cơ sở dữ liệu, đồng thời kiểm tra trạng thái tài khoản.
  6. Hệ thống tạo phiên đăng nhập và cấp `access_token` cùng `refresh_token`.
  7. Hệ thống chuyển người dùng đến trang chính tương ứng với vai trò: `/student`, `/teacher`, `/admin` hoặc `/superadmin`.
- **Luồng tương tác thay thế**:
  - **7a. Người dùng đã truy cập một trang yêu cầu đăng nhập trước đó**: Hệ thống chuyển người dùng về trang được yêu cầu ban đầu thay vì trang chính.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Thông tin đăng nhập không hợp lệ**: Hệ thống thông báo **"Email hoặc mật khẩu không chính xác."** và giữ nguyên biểu mẫu.
  - **E2 - Tài khoản bị khóa hoặc vô hiệu hóa**: Hệ thống thông báo **"Tài khoản đã bị khóa hoặc vô hiệu hóa."**
  - **E3 - Lỗi hệ thống**: Hệ thống thông báo **"Đăng nhập thất bại, vui lòng thử lại sau."**

---

### UC-02 — Đăng Xuất
- **Mô tả**: Cho phép người dùng kết thúc phiên làm việc hiện tại trên hệ thống.
- **Tác nhân**: Student, Teacher, Admin, Super Admin.
- **Tiền điều kiện**: Người dùng đang có phiên đăng nhập hợp lệ.
- **Hậu điều kiện**:
  - Phiên đăng nhập của người dùng được kết thúc.
  - Các thông tin xác thực cục bộ được xóa và người dùng được chuyển về trang đăng nhập.
- **Luồng tương tác chính**:
  1. Người dùng chọn **"Đăng xuất"** trên thanh điều hướng.
  2. Hệ thống hiển thị yêu cầu xác nhận đăng xuất.
  3. Người dùng xác nhận yêu cầu.
  4. Hệ thống thu hồi hoặc đưa `refresh_token` vào danh sách vô hiệu hóa nếu cơ chế này được cấu hình.
  5. Hệ thống xóa token xác thực được lưu trên trình duyệt.
  6. Hệ thống kết thúc phiên đăng nhập và chuyển người dùng về trang `/login`.
- **Luồng tương tác thay thế**:
  - **3a. Người dùng hủy xác nhận**: Hệ thống đóng hộp thoại và giữ nguyên phiên đăng nhập.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Phiên đăng nhập đã hết hạn**: Hệ thống xóa thông tin xác thực cục bộ và chuyển người dùng về trang `/login`.

---

### UC-03 — Quên Mật Khẩu
- **Mô tả**: Cho phép người dùng xác thực quyền sở hữu tài khoản và đặt lại mật khẩu khi không nhớ mật khẩu hiện tại.
- **Tác nhân**: Student, Teacher, Admin, Super Admin.
- **Tiền điều kiện**: Người dùng đang ở trang đăng nhập và có quyền truy cập địa chỉ email đã đăng ký.
- **Hậu điều kiện**:
  - Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu.
  - Các mã hoặc liên kết khôi phục đã sử dụng bị vô hiệu hóa.
  - Nếu khôi phục thất bại, mật khẩu hiện tại vẫn được giữ nguyên.
- **Luồng tương tác chính**:
  1. Người dùng chọn **"Quên mật khẩu"** tại trang đăng nhập.
  2. Hệ thống hiển thị biểu mẫu yêu cầu nhập email tài khoản.
  3. Người dùng nhập email và chọn **"Gửi yêu cầu"**.
  4. Hệ thống kiểm tra định dạng email và tạo mã OTP hoặc liên kết đặt lại mật khẩu có thời hạn.
  5. Hệ thống gửi mã hoặc liên kết xác thực đến email của người dùng và thông báo đã gửi yêu cầu.
  6. Người dùng sử dụng mã hoặc liên kết nhận được để mở biểu mẫu đặt lại mật khẩu.
  7. Người dùng nhập mật khẩu mới, xác nhận mật khẩu và chọn **"Cập nhật mật khẩu"**.
  8. Hệ thống kiểm tra mã hoặc liên kết còn hợp lệ, đồng thời kiểm tra mật khẩu mới.
  9. Hệ thống băm mật khẩu mới, cập nhật vào cơ sở dữ liệu và vô hiệu hóa mã hoặc liên kết đã sử dụng.
  10. Hệ thống thông báo **"Khôi phục mật khẩu thành công."** và chuyển người dùng về trang đăng nhập.
- **Luồng tương tác thay thế**:
  - **5a. Người dùng không nhận được email**: Người dùng yêu cầu gửi lại mã hoặc liên kết khi thời gian chờ cho phép; hệ thống cấp thông tin xác thực mới.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Email không tồn tại hoặc không hợp lệ**: Hệ thống thông báo yêu cầu không thể thực hiện và không tiết lộ thông tin tài khoản tồn tại.
  - **E2 - Mã hoặc liên kết hết hạn hoặc không hợp lệ**: Hệ thống thông báo **"Mã hoặc liên kết khôi phục không hợp lệ hoặc đã hết hạn."**
  - **E3 - Mật khẩu mới không đạt yêu cầu**: Hệ thống thông báo **"Mật khẩu mới không hợp lệ hoặc không trùng khớp."**
  - **E4 - Lỗi gửi email hoặc lỗi lưu dữ liệu**: Hệ thống thông báo **"Không thể khôi phục mật khẩu, vui lòng thử lại sau."**

---

### UC-04 — Xem Thông Tin Cá Nhân
- **Mô tả**: Cho phép người dùng xem thông tin cá nhân đã lưu trong hệ thống.
- **Tác nhân**: Student, Teacher, Admin, Super Admin.
- **Tiền điều kiện**: Người dùng đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Thông tin cá nhân hiện tại của người dùng được hiển thị; dữ liệu trong cơ sở dữ liệu không bị thay đổi.
- **Luồng tương tác chính**:
  1. Người dùng truy cập trang cá nhân `/profile`.
  2. Hệ thống xác thực phiên đăng nhập và quyền truy cập của người dùng.
  3. Hệ thống truy vấn thông tin cá nhân từ cơ sở dữ liệu.
  4. Hệ thống hiển thị các thông tin được phép xem, như họ tên, email, số điện thoại, ảnh đại diện và vai trò của người dùng.
- **Luồng tương tác thay thế**:
  - **3a. Người dùng tải lại trang**: Hệ thống truy vấn lại dữ liệu mới nhất từ cơ sở dữ liệu và hiển thị thông tin cập nhật.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn**: Hệ thống thông báo yêu cầu đăng nhập và chuyển người dùng về trang `/login`.
  - **E2 - Không tìm thấy thông tin cá nhân**: Hệ thống thông báo **"Không tìm thấy thông tin cá nhân."**
  - **E3 - Lỗi truy vấn dữ liệu**: Hệ thống thông báo **"Không thể tải thông tin cá nhân, vui lòng thử lại sau."**

---

### UC-05 — Cập Nhật Thông Tin Cá Nhân
- **Mô tả**: Cho phép người dùng chỉnh sửa và lưu các thông tin cá nhân được hệ thống cho phép cập nhật.
- **Tác nhân**: Student, Teacher, Admin, Super Admin.
- **Tiền điều kiện**:
  - Người dùng đã đăng nhập và có phiên xác thực hợp lệ.
  - Thông tin cá nhân của người dùng đã tồn tại trong hệ thống.
- **Hậu điều kiện**:
  - Thông tin hợp lệ được cập nhật và lưu vào cơ sở dữ liệu.
  - Nếu cập nhật thất bại, thông tin cũ được giữ nguyên và hệ thống hiển thị thông báo lỗi.
- **Luồng tương tác chính**:
  1. Người dùng truy cập trang cá nhân `/profile`.
  2. Hệ thống xác thực phiên đăng nhập và hiển thị thông tin hiện tại.
  3. Người dùng chọn **"Chỉnh sửa"**.
  4. Hệ thống hiển thị biểu mẫu với các trường được phép cập nhật, như họ tên, số điện thoại và ảnh đại diện.
  5. Người dùng chỉnh sửa thông tin và chọn **"Lưu thay đổi"**.
  6. Hệ thống kiểm tra tính hợp lệ của dữ liệu.
  7. Hệ thống cập nhật thông tin vào cơ sở dữ liệu.
  8. Hệ thống thông báo **"Cập nhật thông tin cá nhân thành công."** và hiển thị dữ liệu mới.
- **Luồng tương tác thay thế**:
  - **5a. Người dùng chọn "Hủy"**: Hệ thống hủy thao tác chỉnh sửa và giữ nguyên thông tin hiện tại.
  - **5b. Người dùng không thay đổi thông tin**: Hệ thống không thực hiện cập nhật và giữ nguyên dữ liệu hiện tại.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn**: Hệ thống thông báo yêu cầu đăng nhập và chuyển người dùng về trang `/login`.
  - **E2 - Thông tin không hợp lệ**: Hệ thống thông báo **"Thông tin cá nhân không hợp lệ."** và giữ lại dữ liệu người dùng đã nhập để chỉnh sửa.
  - **E3 - Dữ liệu đã được cập nhật ở nơi khác**: Hệ thống thông báo **"Thông tin đã được cập nhật, vui lòng tải lại dữ liệu."** và không ghi đè dữ liệu mới.
  - **E4 - Lỗi khi lưu dữ liệu**: Hệ thống thông báo **"Cập nhật thông tin cá nhân thất bại."**

---

### UC-06 — Đổi Mật Khẩu
- **Mô tả**: Cho phép người dùng thay đổi mật khẩu hiện tại sau khi xác thực mật khẩu cũ.
- **Tác nhân**: Student, Teacher, Admin, Super Admin.
- **Tiền điều kiện**:
  - Người dùng đã đăng nhập và có phiên xác thực hợp lệ.
  - Người dùng biết mật khẩu hiện tại.
- **Hậu điều kiện**:
  - Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu.
  - Các phiên hoặc token cũ được xử lý theo chính sách bảo mật của hệ thống.
  - Nếu đổi mật khẩu thất bại, mật khẩu cũ vẫn được giữ nguyên.
- **Luồng tương tác chính**:
  1. Người dùng truy cập chức năng **"Đổi mật khẩu"** trong trang cá nhân.
  2. Hệ thống hiển thị biểu mẫu gồm Mật khẩu hiện tại, Mật khẩu mới và Xác nhận mật khẩu mới.
  3. Người dùng nhập đầy đủ thông tin và chọn **"Đổi mật khẩu"**.
  4. Hệ thống xác thực phiên đăng nhập và đối chiếu mật khẩu hiện tại.
  5. Hệ thống kiểm tra mật khẩu mới đạt chính sách bảo mật và trùng với phần xác nhận.
  6. Hệ thống băm mật khẩu mới và lưu vào cơ sở dữ liệu.
  7. Hệ thống thông báo **"Đổi mật khẩu thành công."**
- **Luồng tương tác thay thế**:
  - **3a. Người dùng chọn "Hủy"**: Hệ thống hủy thao tác và giữ nguyên mật khẩu hiện tại.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn**: Hệ thống yêu cầu người dùng đăng nhập lại.
  - **E2 - Mật khẩu hiện tại không chính xác**: Hệ thống thông báo **"Mật khẩu hiện tại không chính xác."**
  - **E3 - Mật khẩu mới không hợp lệ**: Hệ thống thông báo **"Mật khẩu mới không đáp ứng yêu cầu bảo mật hoặc không trùng khớp."**
  - **E4 - Mật khẩu mới trùng mật khẩu hiện tại**: Hệ thống thông báo **"Mật khẩu mới phải khác mật khẩu hiện tại."**
  - **E5 - Lỗi khi lưu dữ liệu**: Hệ thống thông báo **"Đổi mật khẩu thất bại."**

---

## II. PHÂN HỆ STUDENT (NGƯỜI HỌC)

### UC-ST07 — Xem Danh Sách Bài Tập
- **Luồng chính**:
  1. Sinh viên truy cập trang `/student/problems`.
  2. Hệ thống truy vấn danh sách lớp mà sinh viên đã tham gia.
  3. Hệ thống lấy danh sách bài tập được giao cho các lớp đó.
  4. Hệ thống hiển thị danh sách dạng bảng/card với các thông tin: Tên bài, Độ khó, Deadline, Trạng thái làm bài (*Chưa làm*, *Đạt*, *Chưa đạt*), Điểm cao nhất.
  5. Sinh viên có thể tìm kiếm theo tên hoặc lọc theo Lớp/Chủ đề/Trạng thái.

---

### UC-ST08 — Xem Chi Tiết Bài Tập
- **Luồng chính**:
  1. Sinh viên click chọn một bài tập từ danh sách.
  2. Hệ thống kiểm tra quyền: Sinh viên phải thuộc lớp được giao bài tập này và bài tập đang trong thời gian mở.
  3. Hệ thống tải và hiển thị:
     - Đề bài chi tiết (hỗ trợ định dạng Markdown và công thức toán học LaTeX).
     - Quy cách Input / Output chuẩn.
     - Các ràng buộc thuật toán (Constraints), Giới hạn Thời gian (Time limit) và Bộ nhớ (Memory limit).
     - Bộ Sample Test Cases công khai (Input mẫu, Output mẫu, Giải thích).
     - Rubric chấm điểm (nếu giảng viên công khai).
  4. Sinh viên bấm nút **"Làm bài"** để chuyển sang giao diện IDE.

---

### UC-ST09 — Viết & Chỉnh Sửa Code (Monaco Editor)
- **Luồng chính**:
  1. Sinh viên mở giao diện IDE làm bài (`/student/problems/{id}/solve`).
  2. Hệ thống khởi tạo trình soạn thảo **Monaco Editor** với template code khởi tạo theo ngôn ngữ đã chọn (Python/C++/Java).
  3. Sinh viên trực tiếp soạn thảo mã nguồn trên editor (hỗ trợ phím tắt, tự động thụt đầu dòng, cú pháp màu).
  4. Hệ thống tự động lưu bản nháp code (Auto-save) vào LocalStorage hoặc DB sau mỗi khoảng thời gian nhất định để tránh mất code khi reload trang.

---

### UC-ST10 — Upload File Bài Làm
- **Luồng chính**:
  1. Tại màn hình IDE, sinh viên chọn tính năng **"Upload File"**.
  2. Hệ thống mở hộp thoại chọn file từ máy tính cá nhân.
  3. Sinh viên chọn file mã nguồn (chỉ chấp nhận phần mở rộng hợp lệ: `.py`, `.cpp`, `.c`, `.java`).
  4. Hệ thống đọc nội dung file và điền trực tiếp vào khung soạn thảo Monaco Editor.
  5. Sinh viên kiểm tra lại nội dung và tiếp tục chỉnh sửa hoặc nộp bài.

---

### UC-ST11 — Chạy Thử Chương Trình (Run Code trên Sample Tests)
- **Tiền điều kiện**: Sinh viên đã nhập mã nguồn vào editor.
- **Luồng chính**:
  1. Sinh viên bấm nút **"Chạy thử" (Run Code)** hoặc dùng phím tắt `Ctrl + Enter`.
  2. Web Client gửi mã nguồn cùng dữ liệu các **Sample Test Cases** lên API `POST /api/v1/submissions/run`.
  3. Hệ thống gọi nhanh container Docker Sandbox để thực thi code với Sample Test Cases.
  4. Sandbox trả về: Standard Output (`stdout`), Standard Error (`stderr`), Thời gian chạy và Trạng thái (Passed / Failed từng test mẫu).
  5. Hệ thống hiển thị kết quả so sánh giữa *Output thực tế* của sinh viên và *Output mong đợi* tại tab "Kết quả Chạy thử".

---

### UC-ST12 — Nộp Bài Chính Thức (Submit Code)
- **Tiền điều kiện**: Sinh viên hoàn thành bài làm và bài tập chưa hết hạn nộp (hoặc cho phép nộp muộn).
- **Luồng chính**:
  1. Sinh viên bấm nút **"Nộp bài" (Submit Code)**.
  2. Web Client gửi mã nguồn lên `POST /api/v1/submissions`.
  3. Backend tạo bản ghi Submission với trạng thái `PENDING` và đẩy Job vào **Redis Queue**.
  4. Backend trả về `submission_id` ngay lập tức cho Client và chuyển giao diện sang trạng thái *"Đang chấm bài..."*.
  5. **Grader Worker (Celery)** nhận Job từ Queue:
     - Gửi code và toàn bộ **Hidden Test Cases** vào **Docker Sandbox**.
     - Sandbox biên dịch (nếu cần) và chạy code cách ly với từng test case.
     - Thu thập kết quả: Điểm số pass test, Memory, Time Limit.
     - Chạy phân tích tĩnh (**Static Code Analyzer**) đo Cyclomatic Complexity, AST, Code Smells.
     - Gửi dữ liệu (Đề bài + Code + Test Results + Rubric) tới **AI Engine (LLM)** để tạo nhận xét và phân tích lỗi.
     - Tổng hợp điểm cuối cùng theo Rubric và lưu toàn bộ kết quả vào CSDL.
  6. Backend thông báo cho Client thông qua **WebSocket** hoặc kết nối Polling: Trạng thái chuyển thành `COMPLETED`.
  7. Client tự động tải và hiển thị kết quả bài nộp hoàn chỉnh.

---

### UC-ST13 & UC-ST14 — Xem Kết Quả Auto-Grader & Nhận Xét AI
- **Luồng chính**:
  1. Sau khi bài nộp hoàn tất chấm, giao diện hiển thị 2 bảng thông tin:
     - **Bảng Auto-Grader**: Tổng điểm đạt được (ví dụ: `80/100`), thời gian chạy trung bình, trạng thái từng test case (Ví dụ: `Test 1: Passed`, `Test 2: Passed`, `Test 3: Wrong Answer`).
     - **Bảng AI Reviewer**: Nhận xét chi tiết của AI về độ phức tạp thuật toán (Ví dụ: *"Thuật toán hiện tại có độ phức tạp O(n^2), có thể tối ưu về O(n log n) bằng cách dùng Hash Map"*), cảnh báo các biến chưa sử dụng hoặc vòng lặp lồng nhau sâu.

---

### UC-ST15 — Tương Tác Với AI Tutor (Socratic Hinting)
- **Luồng chính**:
  1. Tại màn hình xem kết quả hoặc màn hình IDE, sinh viên mở khung chat **"Trợ giảng AI"**.
  2. Hệ thống tự động đính kèm Context: Đề bài, Mã nguồn hiện tại của sinh viên, Test case bị lỗi gần nhất.
  3. Sinh viên nhập câu hỏi (Ví dụ: *"Tại sao test case số 3 của em bị Wrong Answer?"* hoặc *"Làm sao để xử lý trường hợp mảng rỗng?"*).
  4. Backend gửi prompt kèm Guardrails sư phạm tới LLM.
  5. AI phân tích và trả về câu trả lời mang tính gợi mở tư duy (đặt câu hỏi ngược, chỉ ra logic thiếu sót, không đưa ra code lời giải).
  6. Sinh viên tiếp tục hội thoại nhiều lượt (Multi-turn conversation) cho đến khi hiểu ra vấn đề.

---

### UC-ST16 & UC-ST17 — Xem Lịch Sử Làm Bài & Bảng Điểm Cá Nhân
- **Luồng chính**:
  1. Sinh viên truy cập tab **"Lịch sử nộp bài"** của bài tập để xem lại toàn bộ các lần submit trong quá khứ, so sánh diff giữa các phiên bản code.
  2. Sinh viên truy cập trang `/student/grades` để xem bảng điểm tổng hợp tất cả các môn học và bài tập đã hoàn thành.

---

## III. PHÂN HỆ TEACHER (GIẢNG VIÊN)

### UC-TE03 $\rightarrow$ UC-TE06 — Quản Lý Lớp Học & Sinh Viên
- **Luồng chính**:
  1. Giảng viên truy cập `/teacher/classes` $\rightarrow$ Chọn **"Tạo lớp mới"**.
  2. Nhập: Tên lớp (ví dụ: *CS101 - Lập trình Python K18*), Mô tả, Học kỳ.
  3. Giảng viên mở chi tiết lớp $\rightarrow$ Thêm sinh viên vào lớp bằng cách nhập Email/Mã sinh viên hoặc chia sẻ Mã tham gia lớp (Class Code).
  4. Giảng viên có quyền xóa sinh viên khỏi lớp hoặc đóng lớp khi hết kỳ học.

---

### UC-TE07 $\rightarrow$ UC-TE12 — Tạo & Cấu Hình Bài Tập
- **Luồng chính**:
  1. Giảng viên chọn **"Tạo bài tập mới"** (`/teacher/problems/create`).
  2. **Nhập thông tin chung**: Tiêu đề, Mô tả bài toán (Markdown), Ngôn ngữ cho phép nộp (Python, C++, Java).
  3. **Thiết lập giới hạn**: Time Limit (giây), Memory Limit (MB).
  4. **Cấu hình Test Cases**:
     - Thêm từng cặp `Input` và `Expected Output`.
     - Tích chọn `is_sample` (Công khai cho sinh viên chạy thử) hoặc `is_hidden` (Chấm điểm chính thức).
     - Thiết lập điểm cho từng testcase.
  5. **Cấu hình Rubric**:
     - Tiêu chí 1: *Correctness / Test cases pass rate* (Trọng số 70%).
     - Tiêu chí 2: *Code Quality & Cleanliness* (Trọng số 20%).
     - Tiêu chí 3: *Optimal Time Complexity* (Trọng số 10%).
  6. **Thiết lập Deadline**: Thời gian mở đề, Hạn chót nộp bài, Cho phép nộp muộn hay không (kèm mức phạt % điểm nếu có).
  7. Bấm **"Lưu bài tập"**.

---

### UC-TE13 — Giao Bài Tập Cho Lớp
- **Luồng chính**:
  1. Giảng viên chọn bài tập đã tạo $\rightarrow$ Bấm **"Giao bài"**.
  2. Chọn một hoặc nhiều lớp học phụ trách từ danh sách.
  3. Xác nhận giao bài $\rightarrow$ Toàn bộ sinh viên trong các lớp được chọn sẽ thấy bài tập xuất hiện trong danh sách của họ.

---

### UC-TE14 $\rightarrow$ UC-TE17 — Xem Submissions, Điểm & Chấm Thủ Công
- **Luồng chính**:
  1. Giảng viên truy cập chi tiết bài tập $\rightarrow$ Chọn tab **"Danh sách bài nộp"**.
  2. Hệ thống hiển thị bảng danh sách: Tên sinh viên, Thời gian nộp, Trạng thái, Điểm Auto-Grader, Điểm AI đánh giá, Điểm tổng kết.
  3. Giảng viên click vào một sinh viên cụ thể để xem chi tiết mã nguồn, kết quả từng testcase và nhận xét của AI.
  4. **Chấm thủ công (UC-TE17)**: Giảng viên có thể ghi đè điểm số (Override Grade) và nhập lời nhận xét cá nhân gửi trực tiếp đến sinh viên.
  5. Hệ thống lưu kết quả chấm thủ công và cập nhật bảng điểm.

---

## IV. PHÂN HỆ ADMIN (QUẢN TRỊ TRƯỜNG / CƠ SỞ)

### UC-AD01 $\rightarrow$ UC-AD05 — Quản Lý Tài Khoản Người Dùng
- **Luồng chính**:
  1. Admin truy cập `/admin/users`.
  2. Xem danh sách toàn bộ người dùng, tìm kiếm theo Tên/Email/Role.
  3. **Tạo tài khoản mới (UC-AD01)**: Nhập Email, Họ tên, Chọn vai trò (`Student` hoặc `Teacher`). Hệ thống tự động sinh mật khẩu tạm thời gửi về email người dùng.
  4. **Khóa/Mở tài khoản (UC-AD02)**: Thay đổi cờ `is_active` để chặn hoặc cho phép người dùng đăng nhập.
  5. **Phân quyền (UC-AD04)**: Nâng cấp hoặc hạ quyền tài khoản (chuyển đổi giữa Student, Teacher, Admin).
  6. **Reset mật khẩu (UC-AD05)**: Tạo liên kết thiết lập lại mật khẩu khi người dùng yêu cầu hỗ trợ.

---

### UC-AD06 — Import Danh Sách Từ Excel / CSV
- **Luồng chính**:
  1. Admin chọn chức năng **"Import Người dùng"**.
  2. Tải lên file `.xlsx` hoặc `.csv` theo mẫu quy định (gồm các cột: *MSSV, Họ tên, Email, Vai trò, Mã lớp*).
  3. Hệ thống kiểm tra tính hợp lệ của dữ liệu (validate định dạng email, kiểm tra trùng lặp email trong DB).
  4. Hệ thống hiển thị bản xem trước (Preview) với số lượng bản ghi hợp lệ và các dòng bị lỗi (nếu có).
  5. Admin xác nhận **"Bắt đầu Import"**. Hệ thống tự động tạo tài khoản hàng loạt và ghi danh sinh viên vào các lớp tương ứng.

---

### UC-AD07 $\rightarrow$ UC-AD11 — Quản Lý Lớp & Phân Công Giảng Viên
- **Luồng chính**:
  1. Admin có quyền xem, tạo mới, chỉnh sửa hoặc đóng bất kỳ lớp học nào trong trường.
  2. **Phân công giảng viên (UC-AD11)**: Admin chọn một lớp học $\rightarrow$ Chọn giảng viên phụ trách từ danh sách Teacher $\rightarrow$ Hệ thống cập nhật quyền sở hữu lớp cho giảng viên đó.

---

## V. PHÂN HỆ SUPER ADMIN (QUẢN TRỊ HỆ THỐNG CỐT LÕI)

### UC-SA07 — Quản Lý Cấu Hình AI Engine
- **Luồng chính**:
  1. Super Admin truy cập `/superadmin/ai-config`.
  2. Lựa chọn AI Provider: **Google Gemini**, **OpenAI**, **Anthropic** hoặc **Local LLM (Ollama)**.
  3. Nhập hoặc cập nhật **API Key** (dữ liệu được mã hóa trước khi lưu vào CSDL).
  4. Tùy chỉnh các tham số AI:
     - `Model Name` (ví dụ: `gemini-1.5-pro`, `gpt-4o`).
     - `Temperature` (ví dụ: `0.2` cho chấm code chính xác, `0.7` cho chat tutor).
     - `Max Output Tokens` (ví dụ: `2048`).
     - `System Prompt Template` (Mẫu prompt chuẩn định hướng sư phạm).
  5. Bấm **"Kiểm tra kết nối (Test Connection)"** $\rightarrow$ Hệ thống gửi một request thử nghiệm tới API $\rightarrow$ Báo kết nối thành công $\rightarrow$ Lưu cấu hình.

---

### UC-SA08 & UC-SA09 — Cấu Hình & Giám Sát Docker Sandbox
- **Luồng chính**:
  1. Super Admin truy cập `/superadmin/sandbox`.
  2. **Cấu hình Sandbox (UC-SA08)**:
     - Thiết lập giới hạn phần cứng tối đa cho mỗi container chạy code: RAM tối đa (`512MB`), CPU cores (`1.0 core`), Execution Timeout mặc định (`5.0s`).
     - Cấu hình danh sách Base Image được phép sử dụng (`sandbox-python:latest`, `sandbox-cpp:latest`).
  3. **Giám sát Sandbox (UC-SA09)**:
     - Xem biểu đồ realtime: Số lượng container đang hoạt động, độ dài hàng đợi chấm bài (Queue Length), lượng CPU/RAM máy chủ tiêu thụ.
     - Cung cấp nút khẩn cấp: **"Force Terminate Dangling Containers"** để dọn dẹp các container bị kẹt tài nguyên.

---

### UC-SA10 & UC-SA11 — Quản Lý Tổ Chức & Tra Cứu System Logs
- **Luồng chính**:
  1. **Quản lý Tổ chức (UC-SA10)**: Tạo mới hoặc kích hoạt/tạm dừng các Tổ chức/Trường đại học tham gia sử dụng nền tảng (Multi-tenancy).
  2. **Tra cứu System Logs (UC-SA11)**:
     - Xem danh sách logs hệ thống được phân loại theo level: `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
     - Bộ lọc tìm kiếm theo Thời gian, Mã lỗi (Error Code), User ID hoặc Module phát sinh lỗi (`Grader Worker`, `AI Service`, `Auth Gateway`).
     - Xuất log ra file JSON/CSV để phục vụ phân tích sự cố.

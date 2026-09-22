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

### UC-07 — Xem Danh Sách Bài Tập
- **Mô tả**: Cho phép Student xem và tra cứu danh sách các bài tập được giao cho những lớp mà mình tham gia.
- **Tác nhân**: Student.
- **Tiền điều kiện**: Student đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Danh sách bài tập phù hợp được hiển thị; dữ liệu bài tập không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student truy cập mục **"Bài tập"** tại `/student/problems`.
  2. Hệ thống xác thực phiên đăng nhập và quyền truy cập của Student.
  3. Hệ thống lấy danh sách lớp, môn học hoặc chủ đề mà Student đang tham gia.
  4. Hệ thống truy vấn các bài tập được giao cho Student theo những lớp hoặc môn học đó.
  5. Hệ thống hiển thị danh sách với các thông tin: Tên bài, lớp/chủ đề, độ khó, thời hạn nộp, trạng thái làm bài và điểm cao nhất nếu đã có kết quả.
  6. Student tìm kiếm hoặc lọc danh sách theo lớp, chủ đề hoặc trạng thái.
- **Luồng tương tác thay thế**:
  - **6a. Student không chọn bộ lọc**: Hệ thống hiển thị toàn bộ bài tập mà Student được phép xem.
  - **6b. Không có bài tập phù hợp**: Hệ thống hiển thị danh sách rỗng và thông báo phù hợp.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn**: Hệ thống yêu cầu Student đăng nhập lại.
  - **E2 - Lỗi truy vấn dữ liệu**: Hệ thống thông báo **"Không thể tải danh sách bài tập, vui lòng thử lại sau."**

---

### UC-08 — Xem Chi Tiết Bài Tập
- **Mô tả**: Cho phép Student xem nội dung và yêu cầu chi tiết của một bài tập được giao.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã đăng nhập và có phiên xác thực hợp lệ.
  - Bài tập tồn tại trong hệ thống.
- **Hậu điều kiện**:
  - Thông tin bài tập được hiển thị nếu Student có quyền truy cập.
  - Nếu Student chọn làm bài, hệ thống chuyển đến giao diện soạn thảo tương ứng.
- **Luồng tương tác chính**:
  1. Student chọn một bài tập từ danh sách.
  2. Hệ thống kiểm tra Student có thuộc lớp được giao bài tập và bài tập có được phép truy cập hay không.
  3. Hệ thống lấy thông tin bài tập từ cơ sở dữ liệu.
  4. Hệ thống hiển thị đề bài, hỗ trợ Markdown và công thức toán học LaTeX nếu có.
  5. Hệ thống hiển thị yêu cầu Input/Output, ràng buộc, giới hạn thời gian, giới hạn bộ nhớ, Sample Test Cases và Rubric được công khai.
  6. Student chọn **"Làm bài"**.
  7. Hệ thống chuyển Student đến giao diện làm bài và tải cấu hình cần thiết.
- **Luồng tương tác thay thế**:
  - **6a. Student quay lại danh sách**: Hệ thống không tạo hoặc thay đổi bài làm và đưa Student về danh sách bài tập.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Bài tập không tồn tại**: Hệ thống thông báo **"Không tìm thấy bài tập."**
  - **E2 - Student không có quyền truy cập**: Hệ thống thông báo **"Bạn không có quyền truy cập bài tập này."**
  - **E3 - Bài tập chưa mở hoặc đã đóng**: Hệ thống thông báo **"Bài tập hiện không khả dụng."**
  - **E4 - Lỗi tải dữ liệu**: Hệ thống thông báo **"Không thể tải chi tiết bài tập, vui lòng thử lại sau."**

---

### UC-09 — Viết & Chỉnh Sửa Code (Monaco Editor)
- **Mô tả**: Cho phép Student viết và chỉnh sửa mã nguồn trực tiếp trong trình soạn thảo của hệ thống.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã đăng nhập và có quyền truy cập bài tập.
  - Bài tập có cấu hình ngôn ngữ lập trình được phép sử dụng.
- **Hậu điều kiện**:
  - Mã nguồn của Student được hiển thị và bản nháp gần nhất được lưu theo cơ chế autosave.
  - Bài làm chưa được xem là bài nộp (submission) chính thức cho đến khi Student chọn **"Nộp bài"**.
- **Luồng tương tác chính**:
  1. Student chọn **"Làm bài"** từ trang chi tiết bài tập.
  2. Hệ thống tải đề bài, ngôn ngữ và cấu hình bài tập.
  3. Hệ thống mở **Monaco Editor** với template code phù hợp.
  4. Student nhập hoặc chỉnh sửa mã nguồn.
  5. Hệ thống kiểm tra cơ bản nội dung editor và tự động lưu bản nháp theo khoảng thời gian được cấu hình.
  6. Student tiếp tục chỉnh sửa hoặc chọn nộp bài trực tiếp.
- **Luồng tương tác thay thế**:
  - **5a. Student tải lại trang**: Hệ thống khôi phục bản nháp gần nhất nếu bản nháp tồn tại.
  - **6a. Student rời khỏi trang**: Hệ thống lưu bản nháp trước khi rời trang nếu kết nối còn hoạt động.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tải được cấu hình bài tập**: Hệ thống thông báo **"Không thể mở trình soạn thảo cho bài tập này."**
  - **E2 - Mã nguồn không hợp lệ hoặc vượt giới hạn**: Hệ thống thông báo lỗi và yêu cầu Student chỉnh sửa mã nguồn.
  - **E3 - Lỗi lưu bản nháp**: Hệ thống thông báo **"Không thể lưu bản nháp, vui lòng kiểm tra kết nối mạng."**

---

### UC-10 — Upload File Bài Làm
- **Mô tả**: Cho phép Student tải mã nguồn từ máy tính vào bài làm đang mở.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã mở giao diện làm bài và có quyền truy cập bài tập.
  - File mã nguồn có phần mở rộng thuộc danh sách ngôn ngữ được bài tập cho phép.
- **Hậu điều kiện**:
  - Nội dung file hợp lệ được nạp vào Monaco Editor và có thể được chỉnh sửa tiếp.
  - File upload không được xem là bài nộp (submission) chính thức cho đến khi Student nộp bài.
- **Luồng tương tác chính**:
  1. Student chọn **"Upload File"** tại màn hình làm bài.
  2. Hệ thống hiển thị giao diện chọn file.
  3. Student chọn file mã nguồn từ máy tính.
  4. Hệ thống kiểm tra phần mở rộng, kích thước và nội dung cơ bản của file.
  5. Hệ thống đọc file và nạp nội dung vào Monaco Editor.
  6. Hệ thống lưu bản nháp của nội dung đã nạp.
  7. Hệ thống thông báo **"Tải file lên thành công."**
- **Luồng tương tác thay thế**:
  - **3a. Student hủy chọn file**: Hệ thống đóng hộp thoại và giữ nguyên nội dung đang có trong editor.
  - **5a. Student tiếp tục chỉnh sửa**: Hệ thống cập nhật nội dung editor và lưu theo cơ chế autosave.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Định dạng file không được hỗ trợ**: Hệ thống thông báo **"Định dạng file không được hỗ trợ."**
  - **E2 - File vượt quá kích thước cho phép**: Hệ thống thông báo **"Kích thước file vượt quá giới hạn cho phép."**
  - **E3 - Không thể đọc file**: Hệ thống thông báo **"Không thể tải file, vui lòng chọn file khác."**

---

### UC-11 — Nộp Bài Chính Thức (Submit Code)
- **Mô tả**: Cho phép Student gửi mã nguồn để hệ thống chấm chính thức và lưu kết quả bài làm.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã đăng nhập và có quyền làm bài.
  - Bài tập còn hạn nộp hoặc cho phép nộp muộn.
  - Student đã nhập mã nguồn.
- **Hậu điều kiện**:
  - Hệ thống tạo và lưu bài nộp (submission), đồng thời ghi nhận trạng thái xử lý như **đang chờ chấm**, **đang chấm**, **đã chấm** hoặc **chấm lỗi**.
  - Sau khi chấm xong, hệ thống lưu kết quả chấm tự động (Auto-Grader) và nhận xét của AI (AI feedback) cho bài nộp.
  - Nếu không tiếp nhận được bài nộp, hệ thống không lưu một bài nộp dở dang hoặc không hợp lệ.
- **Luồng tương tác chính**:
  1. Student kiểm tra mã nguồn và chọn **"Nộp bài"**.
  2. Hệ thống kiểm tra quyền nộp, thời hạn, ngôn ngữ và dữ liệu bài nộp.
  3. Web Client gửi mã nguồn cùng thông tin bài tập đến API nộp bài.
  4. Backend tạo bài nộp (submission) với trạng thái `PENDING` và đưa tác vụ vào hàng đợi xử lý.
  5. Hệ thống trả về mã bài nộp (submission ID) và hiển thị trạng thái **"Đang chấm bài..."**.
  6. Grader Worker lấy tác vụ, gửi mã nguồn và toàn bộ Hidden Test Cases đến Docker Sandbox.
  7. Docker Sandbox biên dịch nếu cần, thực thi code cách ly và trả về execution evidence gồm output, lỗi, thời gian chạy, bộ nhớ và trạng thái từng test.
  8. Hệ thống thực hiện Auto-Grading, phân tích tĩnh nếu được cấu hình và tính điểm theo Rubric.
  9. Hệ thống lưu kết quả chấm vào cơ sở dữ liệu.
  10. AI Engine tạo feedback dựa trên đề bài, mã nguồn và kết quả chấm; hệ thống lưu feedback nếu tác vụ thành công.
  11. Hệ thống cập nhật trạng thái bài nộp (submission) thành `COMPLETED` hoặc trạng thái lỗi tương ứng.
  12. Hệ thống thông báo trạng thái cho Student qua WebSocket hoặc polling.
- **Luồng tương tác thay thế**:
  - **1a. Student xác nhận nộp bài muộn**: Hệ thống tiếp nhận bài nộp (submission) và áp dụng quy định phạt điểm nếu bài tập cho phép nộp muộn.
  - **12a. Student rời khỏi trang**: Hệ thống tiếp tục xử lý bài nộp (submission); Student có thể xem trạng thái từ lịch sử làm bài.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Hết hạn nộp bài**: Hệ thống thông báo **"Đã hết hạn nộp bài."**
  - **E2 - Mã nguồn không hợp lệ**: Hệ thống thông báo **"Bài nộp không hợp lệ."**
  - **E3 - Không thể đưa tác vụ vào hàng đợi**: Hệ thống thông báo **"Không thể tiếp nhận bài nộp, vui lòng thử lại sau."**
  - **E4 - Lỗi khi chấm bài**: Hệ thống cập nhật bài nộp (submission) ở trạng thái lỗi và thông báo **"Chấm bài thất bại, vui lòng thử lại sau."**

---

### UC-12 — Xem Kết Quả Auto-Grader
- **Mô tả**: Cho phép Student xem kết quả chấm tự động của một bài nộp (submission).
- **Tác nhân**: Student.
- **Tiền điều kiện**: Student đã đăng nhập và bài nộp (submission) thuộc về Student.
- **Hậu điều kiện**: Kết quả Auto-Grader được hiển thị; dữ liệu chấm không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student mở một bài nộp (submission) từ lịch sử làm bài hoặc trang kết quả.
  2. Hệ thống kiểm tra quyền truy cập bài nộp (submission).
  3. Hệ thống lấy kết quả Auto-Grader.
  4. Hệ thống hiển thị điểm số, trạng thái tổng quát và thời gian chấm.
  5. Hệ thống hiển thị trạng thái từng test case và các lỗi biên dịch, lỗi chạy hoặc giới hạn tài nguyên nếu có.
  6. Student xem chi tiết kết quả chấm bài.
- **Luồng tương tác thay thế**:
  - **4a. Bài nộp (submission) đang được xử lý**: Hệ thống hiển thị trạng thái `PENDING` hoặc `RUNNING` và cho phép Student tải lại kết quả.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Bài nộp (submission) không tồn tại**: Hệ thống thông báo **"Không tìm thấy bài nộp."**
  - **E2 - Student không có quyền truy cập**: Hệ thống từ chối yêu cầu và không hiển thị dữ liệu bài nộp (submission).
  - **E3 - Chưa có kết quả chấm**: Hệ thống thông báo **"Kết quả chấm bài chưa sẵn sàng."**

---

### UC-13 — Xem Nhận Xét AI
- **Mô tả**: Cho phép Student xem nhận xét do AI tạo ra dựa trên bài làm và kết quả chấm.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã đăng nhập và bài nộp (submission) thuộc về Student.
  - Bài nộp (submission) đã có kết quả chấm hoặc đủ dữ liệu để tạo feedback.
- **Hậu điều kiện**: Nhận xét AI được hiển thị nếu đã được tạo; dữ liệu bài nộp không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student mở trang kết quả của một bài nộp (submission).
  2. Hệ thống kiểm tra quyền truy cập và trạng thái AI feedback.
  3. Hệ thống lấy nhận xét AI đã lưu.
  4. Hệ thống hiển thị nhận xét về lỗi, chất lượng mã nguồn, độ phức tạp và đề xuất cải thiện nếu có.
  5. Student xem và sử dụng nhận xét để cải thiện bài làm.
- **Luồng tương tác thay thế**:
  - **3a. AI feedback đang được tạo**: Hệ thống hiển thị trạng thái chờ và cập nhật khi feedback sẵn sàng.
  - **3b. AI feedback chưa được bật cho bài tập**: Hệ thống thông báo tính năng không khả dụng cho bài nộp (submission) này.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tìm thấy bài nộp (submission)**: Hệ thống thông báo **"Không tìm thấy bài nộp."**
  - **E2 - Student không có quyền truy cập**: Hệ thống từ chối yêu cầu xem feedback.
  - **E3 - AI Service gặp lỗi**: Hệ thống thông báo **"Chưa thể tạo nhận xét AI, vui lòng thử lại sau."**

---

### UC-14 — Tương Tác Với AI Tutor (Socratic Hinting)
- **Mô tả**: Cho phép Student trao đổi với AI Tutor để nhận gợi ý định hướng giải quyết bài tập theo phương pháp Socratic.
- **Tác nhân**: Student; AI Tutor là hệ thống phụ trợ.
- **Tiền điều kiện**:
  - Student đã đăng nhập.
  - Student đang xem bài tập, bài làm hoặc kết quả bài nộp.
- **Hậu điều kiện**:
  - Câu hỏi và câu trả lời được hiển thị trong phiên hội thoại.
  - Lịch sử hội thoại được lưu theo chính sách của hệ thống nếu chức năng lưu được bật.
- **Luồng tương tác chính**:
  1. Student mở **"AI Tutor"** tại màn hình bài tập, IDE hoặc kết quả bài nộp.
  2. Hệ thống lấy context cần thiết gồm đề bài, mã nguồn, kết quả test và câu hỏi trước đó trong hội thoại.
  3. Student nhập câu hỏi và chọn **"Gửi"**.
  4. Hệ thống kiểm tra câu hỏi, quyền truy cập context và giới hạn sử dụng.
  5. Backend gửi prompt kèm guardrails sư phạm đến AI Engine.
  6. AI Tutor phân tích context và tạo câu trả lời mang tính gợi mở, không cung cấp ngay toàn bộ lời giải nếu chính sách không cho phép.
  7. Hệ thống hiển thị câu trả lời trong khung hội thoại.
  8. Student tiếp tục đặt câu hỏi trong cùng phiên.
- **Luồng tương tác thay thế**:
  - **2a. Student không chọn bài làm hoặc bài nộp (submission)**: Hệ thống chỉ gửi context của đề bài và các thông tin được phép xem.
  - **8a. Student bắt đầu hội thoại mới**: Hệ thống xóa context hội thoại trước khỏi phiên hiện tại và khởi tạo phiên mới.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Câu hỏi rỗng hoặc vượt giới hạn**: Hệ thống yêu cầu Student nhập câu hỏi hợp lệ.
  - **E2 - AI Service không khả dụng**: Hệ thống thông báo **"AI Tutor hiện không khả dụng, vui lòng thử lại sau."**
  - **E3 - Nội dung yêu cầu không phù hợp chính sách**: Hệ thống từ chối yêu cầu và hiển thị thông báo phù hợp.

---

### UC-15 — Xem Lịch Sử Làm Bài
- **Mô tả**: Cho phép Student tra cứu các bài nộp (submissions) của mình và xem chi tiết từng lần nộp bài.
- **Tác nhân**: Student.
- **Tiền điều kiện**: Student đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Lịch sử bài nộp (submissions) của Student được hiển thị; dữ liệu bài nộp không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student truy cập mục **"Lịch sử làm bài"** hoặc lịch sử nộp bài của một bài tập.
  2. Hệ thống xác thực phiên đăng nhập.
  3. Hệ thống truy vấn các bài nộp (submissions) thuộc về Student.
  4. Hệ thống sắp xếp lịch sử theo thời gian và hiển thị bài tập, thời điểm nộp, trạng thái, điểm và ngôn ngữ.
  5. Student chọn một bài nộp (submission) để xem mã nguồn, kết quả test và feedback được phép xem.
- **Luồng tương tác thay thế**:
  - **4a. Student lọc lịch sử**: Hệ thống lọc theo bài tập, lớp, trạng thái hoặc khoảng thời gian.
  - **5a. Student chọn hai bài nộp (submissions)**: Hệ thống hiển thị phần khác nhau giữa các phiên bản nếu chức năng so sánh được hỗ trợ.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không có lịch sử bài nộp (submissions)**: Hệ thống hiển thị danh sách rỗng và thông báo **"Chưa có bài nộp nào."**
  - **E2 - Lỗi truy vấn dữ liệu**: Hệ thống thông báo **"Không thể tải lịch sử làm bài, vui lòng thử lại sau."**

---

### UC-16 — Xem Bảng Điểm Cá Nhân
- **Mô tả**: Cho phép Student xem tổng hợp điểm các bài tập và lớp học mà mình tham gia.
- **Tác nhân**: Student.
- **Tiền điều kiện**: Student đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Bảng điểm cá nhân được hiển thị theo dữ liệu kết quả đã được chấm; dữ liệu điểm không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student truy cập trang **"Bảng điểm"** tại `/student/grades`.
  2. Hệ thống xác thực phiên đăng nhập.
  3. Hệ thống truy vấn các kết quả đã được chấm thuộc về Student.
  4. Hệ thống tổng hợp điểm theo bài tập và lớp học theo quy tắc đã cấu hình.
  5. Hệ thống hiển thị bảng điểm gồm bài tập, lớp, điểm, trạng thái và thời gian cập nhật.
  6. Student xem hoặc lọc điểm theo bài tập, lớp hoặc khoảng thời gian.
- **Luồng tương tác thay thế**:
  - **6a. Student không chọn bộ lọc**: Hệ thống hiển thị toàn bộ bảng điểm mà Student được phép xem.
  - **6b. Một số bài chưa có điểm cuối**: Hệ thống hiển thị trạng thái đang chờ chấm hoặc chưa có kết quả thay vì tự động coi là điểm 0.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không có kết quả đã chấm**: Hệ thống hiển thị bảng điểm rỗng và thông báo **"Chưa có kết quả được chấm."**
  - **E2 - Lỗi tổng hợp điểm**: Hệ thống thông báo **"Không thể tải bảng điểm, vui lòng thử lại sau."**

---

## III. PHÂN HỆ TEACHER (GIẢNG VIÊN)

### UC-17 — Tạo Lớp Học
- **Mô tả**: Cho phép Teacher khởi tạo một lớp học mới do mình phụ trách.
- **Tác nhân**: Teacher.
- **Tiền điều kiện**: Teacher đã đăng nhập và có quyền quản lý lớp trong tổ chức tương ứng.
- **Hậu điều kiện**: Lớp học hợp lệ được tạo và gắn với Teacher; hệ thống sinh mã tham gia nếu cần.
- **Luồng tương tác chính**:
  1. Teacher truy cập `/teacher/classes` và chọn **"Tạo lớp"**.
  2. Hệ thống hiển thị biểu mẫu gồm tên lớp, mã lớp, mô tả, học kỳ hoặc niên khóa.
  3. Teacher nhập thông tin và chọn **"Tạo lớp"**.
  4. Hệ thống kiểm tra quyền, định dạng dữ liệu và tính duy nhất của mã lớp.
  5. Hệ thống tạo lớp, gắn Teacher làm người phụ trách và sinh mã tham gia nếu cần.
  6. Hệ thống thông báo **"Tạo lớp thành công."** và hiển thị chi tiết lớp.
- **Luồng tương tác thay thế**:
  - **3a. Teacher chọn "Hủy"**: Hệ thống đóng biểu mẫu và không tạo lớp.
  - **3b. Teacher không nhập mã lớp**: Hệ thống tự sinh mã theo cấu hình.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Dữ liệu không hợp lệ**: Hệ thống thông báo **"Thông tin lớp học không hợp lệ."**
  - **E2 - Mã lớp đã tồn tại**: Hệ thống thông báo **"Mã lớp đã tồn tại, vui lòng chọn mã khác."**
  - **E3 - Lỗi khi tạo lớp**: Hệ thống thông báo **"Không thể tạo lớp, vui lòng thử lại sau."**

### UC-18 — Chỉnh Sửa Lớp Học
- **Mô tả**: Cho phép Teacher cập nhật thông tin của lớp học do mình phụ trách.
- **Tác nhân**: Teacher.
- **Tiền điều kiện**: Teacher đã đăng nhập; lớp tồn tại và chưa bị xóa.
- **Hậu điều kiện**: Thông tin hợp lệ của lớp được cập nhật; nếu thất bại, dữ liệu cũ được giữ nguyên.
- **Luồng tương tác chính**:
  1. Teacher truy cập `/teacher/classes` và chọn lớp cần chỉnh sửa.
  2. Hệ thống kiểm tra quyền và hiển thị thông tin hiện tại.
  3. Teacher chỉnh sửa tên lớp, mô tả, học kỳ hoặc niên khóa.
  4. Teacher chọn **"Lưu"**.
  5. Hệ thống kiểm tra dữ liệu và phiên bản hiện tại của lớp.
  6. Hệ thống cập nhật thông tin và thông báo **"Cập nhật lớp thành công."**
- **Luồng tương tác thay thế**:
  - **4a. Teacher chọn "Hủy"**: Hệ thống bỏ các thay đổi chưa lưu.
  - **4b. Teacher không thay đổi dữ liệu**: Hệ thống không tạo bản cập nhật mới.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tìm thấy lớp**: Hệ thống thông báo **"Không tìm thấy lớp học."**
  - **E2 - Teacher không có quyền**: Hệ thống từ chối yêu cầu và không hiển thị dữ liệu lớp.
  - **E3 - Dữ liệu đã thay đổi ở nơi khác**: Hệ thống thông báo **"Thông tin lớp đã thay đổi, vui lòng tải lại."**

### UC-19 — Xóa / Đóng Lớp Học
- **Mô tả**: Cho phép Teacher đóng lớp khi kết thúc hoạt động hoặc xóa lớp chưa sử dụng theo chính sách.
- **Tác nhân**: Teacher.
- **Tiền điều kiện**: Teacher đã đăng nhập, có quyền quản lý và lớp học tồn tại.
- **Hậu điều kiện**: Lớp được đóng hoặc xóa mềm; lớp đóng không còn nhận thành viên hoặc bài tập mới.
- **Luồng tương tác chính**:
  1. Teacher mở chi tiết lớp cần xử lý.
  2. Teacher chọn **"Đóng lớp"** hoặc **"Xóa lớp"**.
  3. Hệ thống hiển thị hộp thoại xác nhận và nêu ảnh hưởng đến dữ liệu liên quan.
  4. Teacher xác nhận thao tác.
  5. Hệ thống kiểm tra trạng thái lớp và thực hiện đóng hoặc xóa theo chính sách.
  6. Hệ thống thông báo **"Xử lý lớp thành công."** và cập nhật danh sách.
- **Luồng tương tác thay thế**:
  - **2a. Teacher hủy xác nhận**: Hệ thống đóng hộp thoại và giữ nguyên lớp.
  - **5a. Lớp có dữ liệu đang hoạt động**: Hệ thống chuyển lớp sang trạng thái đóng hoặc lưu trữ thay vì xóa vật lý.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Lớp đã đóng hoặc đã xóa**: Hệ thống thông báo **"Lớp học không còn ở trạng thái có thể xử lý."**
  - **E2 - Lỗi cập nhật trạng thái**: Hệ thống thông báo **"Không thể cập nhật trạng thái lớp, vui lòng thử lại sau."**

### UC-20 — Quản Lý Sinh Viên Trong Lớp
- **Mô tả**: Cho phép Teacher thêm hoặc xóa sinh viên khỏi lớp mình phụ trách.
- **Tác nhân**: Teacher.
- **Tiền điều kiện**: Teacher đã đăng nhập, có quyền quản lý và lớp đang mở.
- **Hậu điều kiện**: Danh sách thành viên được cập nhật theo yêu cầu hợp lệ.
- **Luồng tương tác chính**:
  1. Teacher mở chi tiết lớp.
  2. Hệ thống hiển thị danh sách sinh viên hiện tại.
  3. Teacher chọn **"Thêm sinh viên"** hoặc chọn sinh viên và chọn **"Xóa khỏi lớp"**.
  4. Với thao tác thêm, Teacher nhập email, mã sinh viên hoặc sử dụng mã tham gia lớp.
  5. Hệ thống kiểm tra tài khoản, tư cách thành viên và trạng thái lớp.
  6. Hệ thống cập nhật danh sách thành viên và hiển thị danh sách mới.
- **Luồng tương tác thay thế**:
  - **3a. Teacher thêm nhiều sinh viên**: Hệ thống xử lý danh sách và trả kết quả theo từng bản ghi.
  - **3b. Teacher hủy thao tác xóa**: Hệ thống đóng hộp thoại và giữ nguyên thành viên.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tìm thấy sinh viên**: Hệ thống thông báo **"Không tìm thấy tài khoản sinh viên."**
  - **E2 - Sinh viên đã là thành viên**: Hệ thống bỏ qua bản ghi trùng và thông báo kết quả.
  - **E3 - Không thể xóa sinh viên**: Hệ thống thông báo **"Không thể xóa sinh viên khỏi lớp."**

---

### UC-21 — Tạo Bài Tập
- **Mô tả**: Cho phép Teacher tạo bài tập mới với đề bài và cấu hình phục vụ chấm tự động.
- **Tác nhân**: Teacher.
- **Tiền điều kiện**: Teacher đã đăng nhập và có quyền quản lý bài tập.
- **Hậu điều kiện**: Bài tập hợp lệ được tạo ở trạng thái bản nháp hoặc sẵn sàng giao; test case, deadline và rubric được lưu cùng cấu hình.
- **Luồng tương tác chính**:
  1. Teacher truy cập trang quản lý bài tập và chọn **"Tạo bài tập"** tại `/teacher/problems/create`.
  2. Hệ thống hiển thị biểu mẫu tạo bài tập.
  3. Teacher nhập tiêu đề, mô tả bài toán bằng Markdown, yêu cầu Input/Output và ngôn ngữ được phép.
  4. Teacher cấu hình time limit, memory limit, thời gian mở đề, deadline và chính sách nộp muộn.
  5. Teacher thêm test case gồm Input, Expected Output, trạng thái sample/hidden và trọng số điểm.
  6. Teacher thiết lập rubric cho Correctness, Code Quality và Complexity.
  7. Teacher chọn **"Lưu bài tập"**.
  8. Hệ thống kiểm tra dữ liệu và tính nhất quán của cấu hình.
  9. Hệ thống tạo bài tập và thông báo **"Tạo bài tập thành công."**
- **Luồng tương tác thay thế**:
  - **7a. Teacher chọn lưu bản nháp**: Hệ thống lưu bài tập ở trạng thái `DRAFT` và chưa cho sinh viên truy cập.
  - **7b. Teacher rời biểu mẫu**: Hệ thống cảnh báo khi có thay đổi chưa lưu.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Thiếu thông tin bắt buộc**: Hệ thống thông báo **"Vui lòng hoàn thiện các trường bắt buộc."**
  - **E2 - Test case hoặc rubric không hợp lệ**: Hệ thống thông báo **"Cấu hình test case hoặc rubric không hợp lệ."**
  - **E3 - Deadline không hợp lệ**: Hệ thống thông báo **"Thời gian mở đề và hạn nộp bài không hợp lệ."**
  - **E4 - Lỗi khi tạo bài tập**: Hệ thống thông báo **"Không thể tạo bài tập, vui lòng thử lại sau."**

### UC-22 — Chỉnh Sửa Bài Tập
- **Mô tả**: Cho phép Teacher cập nhật nội dung hoặc cấu hình của bài tập do mình quản lý.
- **Tác nhân**: Teacher.
- **Tiền điều kiện**: Teacher đã đăng nhập; bài tập tồn tại và đang ở trạng thái cho phép chỉnh sửa.
- **Hậu điều kiện**: Nội dung và cấu hình hợp lệ được cập nhật; các bài nộp đã có không bị thay đổi ngoài chính sách phiên bản.
- **Luồng tương tác chính**:
  1. Teacher mở danh sách bài tập và chọn bài cần chỉnh sửa.
  2. Hệ thống kiểm tra quyền truy cập và hiển thị thông tin bài tập.
  3. Teacher chỉnh sửa đề bài, ngôn ngữ, giới hạn, deadline, test case hoặc rubric.
  4. Teacher chọn **"Lưu"**.
  5. Hệ thống kiểm tra dữ liệu, trạng thái bài tập và tính tương thích với bài nộp hiện có.
  6. Hệ thống cập nhật bài tập hoặc tạo phiên bản mới theo chính sách.
  7. Hệ thống thông báo **"Cập nhật bài tập thành công."**
- **Luồng tương tác thay thế**:
  - **4a. Teacher chọn "Hủy"**: Hệ thống bỏ thay đổi chưa lưu.
  - **5a. Bài tập đã được giao hoặc có bài nộp**: Hệ thống giới hạn trường được sửa hoặc yêu cầu xác nhận tạo phiên bản mới.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tìm thấy bài tập**: Hệ thống thông báo **"Không tìm thấy bài tập."**
  - **E2 - Teacher không có quyền**: Hệ thống từ chối yêu cầu và không cho phép chỉnh sửa.
  - **E3 - Dữ liệu không hợp lệ**: Hệ thống thông báo **"Thông tin bài tập không hợp lệ."**
  - **E4 - Lỗi khi lưu**: Hệ thống thông báo **"Không thể cập nhật bài tập, vui lòng thử lại sau."**

### UC-23 — Xóa Bài Tập
- **Mô tả**: Cho phép Teacher xóa hoặc vô hiệu hóa bài tập theo trạng thái và chính sách lưu trữ dữ liệu.
- **Tác nhân**: Teacher.
- **Tiền điều kiện**: Teacher đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại.
- **Hậu điều kiện**: Bài tập được xóa mềm, vô hiệu hóa hoặc xóa theo chính sách; bài nộp, điểm và lịch sử liên quan được giữ lại khi cần.
- **Luồng tương tác chính**:
  1. Teacher mở danh sách bài tập và chọn bài cần xóa.
  2. Teacher chọn **"Xóa"**.
  3. Hệ thống hiển thị yêu cầu xác nhận và thông tin về dữ liệu bị ảnh hưởng.
  4. Teacher xác nhận thao tác.
  5. Hệ thống kiểm tra trạng thái bài tập, quyền truy cập và dữ liệu liên quan.
  6. Hệ thống xóa hoặc vô hiệu hóa bài tập theo chính sách.
  7. Hệ thống thông báo **"Xử lý bài tập thành công."** và cập nhật danh sách.
- **Luồng tương tác thay thế**:
  - **2a. Teacher hủy thao tác**: Hệ thống đóng hộp thoại và giữ nguyên bài tập.
  - **5a. Bài tập đã có bài nộp**: Hệ thống vô hiệu hóa hoặc xóa mềm thay vì xóa dữ liệu vật lý.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tìm thấy bài tập**: Hệ thống thông báo **"Bài tập không tồn tại hoặc đã được xử lý."**
  - **E2 - Bài tập đang được sử dụng**: Hệ thống thông báo **"Bài tập đang có dữ liệu liên quan và không thể xóa trực tiếp."**
  - **E3 - Lỗi xử lý**: Hệ thống thông báo **"Không thể xóa hoặc vô hiệu hóa bài tập, vui lòng thử lại sau."**

### UC-24 $\rightarrow$ UC-26 — Cấu Hình Deadline, Test Case & Rubric
- **Luồng chính**:
  1. Teacher mở bài tập cần cấu hình.
  2. Teacher thiết lập deadline, test case và rubric theo các chức năng tương ứng.
  3. Hệ thống kiểm tra và lưu cấu hình.

---

### UC-27 — Giao Bài Tập Cho Lớp
- **Luồng chính**:
  1. Giảng viên chọn bài tập đã tạo $\rightarrow$ Bấm **"Giao bài"**.
  2. Chọn một hoặc nhiều lớp học phụ trách từ danh sách.
  3. Xác nhận giao bài $\rightarrow$ Toàn bộ sinh viên trong các lớp được chọn sẽ thấy bài tập xuất hiện trong danh sách của họ.

---

### UC-28 $\rightarrow$ UC-31 — Xem Bài Nộp (Submissions), Điểm & Chấm Thủ Công
- **Luồng chính**:
  1. Giảng viên truy cập chi tiết bài tập $\rightarrow$ Chọn tab **"Danh sách bài nộp"**.
  2. Hệ thống hiển thị bảng danh sách: Tên sinh viên, Thời gian nộp, Trạng thái, Điểm Auto-Grader, Điểm AI đánh giá, Điểm tổng kết.
  3. Giảng viên click vào một sinh viên cụ thể để xem chi tiết mã nguồn, kết quả từng testcase và nhận xét của AI.
  4. **Chấm thủ công (UC-31)**: Giảng viên có thể ghi đè điểm số (Override Grade) và nhập lời nhận xét cá nhân gửi trực tiếp đến sinh viên.
  5. Hệ thống lưu kết quả chấm thủ công và cập nhật bảng điểm.

---

## IV. PHÂN HỆ ADMIN (QUẢN TRỊ TRƯỜNG / CƠ SỞ)

### UC-32 $\rightarrow$ UC-36 — Quản Lý Tài Khoản Người Dùng
- **Luồng chính**:
  1. Admin truy cập `/admin/users`.
  2. Xem danh sách toàn bộ người dùng, tìm kiếm theo Tên/Email/Role.
  3. **Tạo tài khoản mới (UC-32)**: Nhập Email, Họ tên, Chọn vai trò (`Student` hoặc `Teacher`). Hệ thống tự động sinh mật khẩu tạm thời gửi về email người dùng.
  4. **Khóa/Mở tài khoản (UC-33)**: Thay đổi cờ `is_active` để chặn hoặc cho phép người dùng đăng nhập.
  5. **Phân quyền (UC-35)**: Nâng cấp hoặc hạ quyền tài khoản (chuyển đổi giữa Student, Teacher, Admin).
  6. **Reset mật khẩu (UC-36)**: Tạo liên kết thiết lập lại mật khẩu khi người dùng yêu cầu hỗ trợ.

---

### UC-37 — Import Danh Sách Từ Excel / CSV
- **Luồng chính**:
  1. Admin chọn chức năng **"Import Người dùng"**.
  2. Tải lên file `.xlsx` hoặc `.csv` theo mẫu quy định (gồm các cột: *MSSV, Họ tên, Email, Vai trò, Mã lớp*).
  3. Hệ thống kiểm tra tính hợp lệ của dữ liệu (validate định dạng email, kiểm tra trùng lặp email trong DB).
  4. Hệ thống hiển thị bản xem trước (Preview) với số lượng bản ghi hợp lệ và các dòng bị lỗi (nếu có).
  5. Admin xác nhận **"Bắt đầu Import"**. Hệ thống tự động tạo tài khoản hàng loạt và ghi danh sinh viên vào các lớp tương ứng.

---

### UC-38 $\rightarrow$ UC-42 — Quản Lý Lớp & Phân Công Giảng Viên
- **Luồng chính**:
  1. Admin có quyền xem, tạo mới, chỉnh sửa hoặc đóng bất kỳ lớp học nào trong trường.
  2. **Phân công giảng viên (UC-42)**: Admin chọn một lớp học $\rightarrow$ Chọn giảng viên phụ trách từ danh sách Teacher $\rightarrow$ Hệ thống cập nhật quyền sở hữu lớp cho giảng viên đó.

---

## V. PHÂN HỆ SUPER ADMIN (QUẢN TRỊ HỆ THỐNG CỐT LÕI)

### UC-43 — Đổi Mật Khẩu Super Admin
- **Luồng chính**:
  1. Super Admin truy cập chức năng **"Đổi mật khẩu"** trong trang cá nhân.
  2. Hệ thống hiển thị biểu mẫu gồm mật khẩu hiện tại, mật khẩu mới và xác nhận mật khẩu mới.
  3. Super Admin nhập thông tin và chọn **"Đổi mật khẩu"**.
  4. Hệ thống xác thực mật khẩu hiện tại, kiểm tra chính sách mật khẩu mới và lưu mật khẩu đã băm.
  5. Hệ thống thông báo **"Đổi mật khẩu thành công."**

### UC-44 — Quản Lý Cấu Hình AI Engine
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

### UC-45 & UC-46 — Cấu Hình & Giám Sát Docker Sandbox
- **Luồng chính**:
  1. Super Admin truy cập `/superadmin/sandbox`.
  2. **Cấu hình Sandbox (UC-45)**:
     - Thiết lập giới hạn phần cứng tối đa cho mỗi container chạy code: RAM tối đa (`512MB`), CPU cores (`1.0 core`), Execution Timeout mặc định (`5.0s`).
     - Cấu hình danh sách Base Image được phép sử dụng (`sandbox-python:latest`, `sandbox-cpp:latest`).
  3. **Giám sát Sandbox (UC-46)**:
     - Xem biểu đồ realtime: Số lượng container đang hoạt động, độ dài hàng đợi chấm bài (Queue Length), lượng CPU/RAM máy chủ tiêu thụ.
     - Cung cấp nút khẩn cấp: **"Force Terminate Dangling Containers"** để dọn dẹp các container bị kẹt tài nguyên.

---

### UC-47 & UC-48 — Quản Lý Tổ Chức & Tra Cứu System Logs
- **Luồng chính**:
  1. **Quản lý Tổ chức (UC-47)**: Tạo mới hoặc kích hoạt/tạm dừng các Tổ chức/Trường đại học tham gia sử dụng nền tảng (Multi-tenancy).
  2. **Tra cứu System Logs (UC-48)**:
     - Xem danh sách logs hệ thống được phân loại theo level: `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
     - Bộ lọc tìm kiếm theo Thời gian, Mã lỗi (Error Code), User ID hoặc Module phát sinh lỗi (`Grader Worker`, `AI Service`, `Auth Gateway`).
     - Xuất log ra file JSON/CSV để phục vụ phân tích sự cố.

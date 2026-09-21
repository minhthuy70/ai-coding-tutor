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

### UC-ST08 — Xem Chi Tiết Bài Tập
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

### UC-ST09 — Viết & Chỉnh Sửa Code (Monaco Editor)
- **Mô tả**: Cho phép Student viết và chỉnh sửa mã nguồn trực tiếp trong trình soạn thảo của hệ thống.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã đăng nhập và có quyền truy cập bài tập.
  - Bài tập có cấu hình ngôn ngữ lập trình được phép sử dụng.
- **Hậu điều kiện**:
  - Mã nguồn của Student được hiển thị và bản nháp gần nhất được lưu theo cơ chế autosave.
  - Bài làm chưa được xem là submission chính thức cho đến khi Student chọn **"Nộp bài"**.
- **Luồng tương tác chính**:
  1. Student chọn **"Làm bài"** từ trang chi tiết bài tập.
  2. Hệ thống tải đề bài, ngôn ngữ và cấu hình bài tập.
  3. Hệ thống mở **Monaco Editor** với template code phù hợp.
  4. Student nhập hoặc chỉnh sửa mã nguồn.
  5. Hệ thống kiểm tra cơ bản nội dung editor và tự động lưu bản nháp theo khoảng thời gian được cấu hình.
  6. Student tiếp tục chỉnh sửa, chạy thử hoặc chuyển sang nộp bài.
- **Luồng tương tác thay thế**:
  - **5a. Student tải lại trang**: Hệ thống khôi phục bản nháp gần nhất nếu bản nháp tồn tại.
  - **6a. Student rời khỏi trang**: Hệ thống lưu bản nháp trước khi rời trang nếu kết nối còn hoạt động.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tải được cấu hình bài tập**: Hệ thống thông báo **"Không thể mở trình soạn thảo cho bài tập này."**
  - **E2 - Mã nguồn không hợp lệ hoặc vượt giới hạn**: Hệ thống thông báo lỗi và yêu cầu Student chỉnh sửa mã nguồn.
  - **E3 - Lỗi lưu bản nháp**: Hệ thống thông báo **"Không thể lưu bản nháp, vui lòng kiểm tra kết nối mạng."**

---

### UC-ST10 — Upload File Bài Làm
- **Mô tả**: Cho phép Student tải mã nguồn từ máy tính vào bài làm đang mở.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã mở giao diện làm bài và có quyền truy cập bài tập.
  - File mã nguồn có phần mở rộng thuộc danh sách ngôn ngữ được bài tập cho phép.
- **Hậu điều kiện**:
  - Nội dung file hợp lệ được nạp vào Monaco Editor và có thể được chỉnh sửa tiếp.
  - File upload không được xem là submission chính thức cho đến khi Student nộp bài.
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

### UC-ST11 — Chạy Thử Chương Trình (Run Code trên Sample Tests)
- **Mô tả**: Cho phép Student chạy thử mã nguồn trên các Sample Test Cases trước khi nộp bài chính thức.
- **Tác nhân**: Student.
- **Tiền điều kiện**: Student đã mở bài tập và có mã nguồn trong editor.
- **Hậu điều kiện**: Kết quả chạy thử được hiển thị cho Student; kết quả này không tạo submission chính thức và không tính vào điểm.
- **Luồng tương tác chính**:
  1. Student chọn **"Chạy thử"** hoặc dùng phím tắt `Ctrl + Enter`.
  2. Hệ thống kiểm tra mã nguồn, ngôn ngữ và Sample Test Cases của bài tập.
  3. Web Client gửi mã nguồn và dữ liệu test đến API chạy thử.
  4. Hệ thống tạo môi trường thực thi tạm thời trong Docker Sandbox với giới hạn tài nguyên.
  5. Docker Sandbox biên dịch nếu cần và chạy mã nguồn trên từng Sample Test Case.
  6. Hệ thống thu thập `stdout`, `stderr`, thời gian chạy, mức sử dụng bộ nhớ và trạng thái từng test.
  7. Hệ thống hiển thị kết quả so sánh giữa output thực tế và output mong đợi.
- **Luồng tương tác thay thế**:
  - **1a. Student sửa mã nguồn sau khi xem kết quả**: Student chạy thử lại với nội dung mới.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Mã nguồn rỗng hoặc không hợp lệ**: Hệ thống yêu cầu Student nhập mã nguồn hợp lệ.
  - **E2 - Lỗi biên dịch, lỗi chạy hoặc vượt giới hạn tài nguyên**: Hệ thống hiển thị trạng thái tương ứng và thông tin lỗi.
  - **E3 - Sandbox không khả dụng**: Hệ thống thông báo **"Không thể chạy thử lúc này, vui lòng thử lại sau."**

---

### UC-ST12 — Nộp Bài Chính Thức (Submit Code)
- **Mô tả**: Cho phép Student gửi mã nguồn để hệ thống chấm chính thức và lưu kết quả bài làm.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã đăng nhập và có quyền làm bài.
  - Bài tập còn hạn nộp hoặc cho phép nộp muộn.
  - Student đã nhập mã nguồn.
- **Hậu điều kiện**:
  - Một submission được tạo và lưu với trạng thái xử lý tương ứng.
  - Kết quả Auto-Grader và AI feedback được lưu khi quá trình chấm hoàn tất.
  - Nếu không thể tiếp nhận bài, hệ thống không tạo submission không đầy đủ.
- **Luồng tương tác chính**:
  1. Student kiểm tra mã nguồn và chọn **"Nộp bài"**.
  2. Hệ thống kiểm tra quyền nộp, thời hạn, ngôn ngữ và dữ liệu bài nộp.
  3. Web Client gửi mã nguồn cùng thông tin bài tập đến API nộp bài.
  4. Backend tạo submission với trạng thái `PENDING` và đưa tác vụ vào hàng đợi xử lý.
  5. Hệ thống trả về mã submission và hiển thị trạng thái **"Đang chấm bài..."**.
  6. Grader Worker lấy tác vụ, gửi mã nguồn và toàn bộ Hidden Test Cases đến Docker Sandbox.
  7. Docker Sandbox biên dịch nếu cần, thực thi code cách ly và trả về execution evidence gồm output, lỗi, thời gian chạy, bộ nhớ và trạng thái từng test.
  8. Hệ thống thực hiện Auto-Grading, phân tích tĩnh nếu được cấu hình và tính điểm theo Rubric.
  9. Hệ thống lưu kết quả chấm vào cơ sở dữ liệu.
  10. AI Engine tạo feedback dựa trên đề bài, mã nguồn và kết quả chấm; hệ thống lưu feedback nếu tác vụ thành công.
  11. Hệ thống cập nhật trạng thái submission thành `COMPLETED` hoặc trạng thái lỗi tương ứng.
  12. Hệ thống thông báo trạng thái cho Student qua WebSocket hoặc polling.
- **Luồng tương tác thay thế**:
  - **1a. Student xác nhận nộp bài muộn**: Hệ thống tiếp nhận submission và áp dụng quy định phạt điểm nếu bài tập cho phép nộp muộn.
  - **12a. Student rời khỏi trang**: Hệ thống tiếp tục xử lý submission; Student có thể xem trạng thái từ lịch sử làm bài.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Hết hạn nộp bài**: Hệ thống thông báo **"Đã hết hạn nộp bài."**
  - **E2 - Mã nguồn không hợp lệ**: Hệ thống thông báo **"Bài nộp không hợp lệ."**
  - **E3 - Không thể đưa tác vụ vào hàng đợi**: Hệ thống thông báo **"Không thể tiếp nhận bài nộp, vui lòng thử lại sau."**
  - **E4 - Lỗi khi chấm bài**: Hệ thống cập nhật submission ở trạng thái lỗi và thông báo **"Chấm bài thất bại, vui lòng thử lại sau."**

---

### UC-ST13 — Xem Kết Quả Auto-Grader
- **Mô tả**: Cho phép Student xem kết quả chấm tự động của một submission.
- **Tác nhân**: Student.
- **Tiền điều kiện**: Student đã đăng nhập và submission thuộc về Student.
- **Hậu điều kiện**: Kết quả Auto-Grader được hiển thị; dữ liệu chấm không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student mở một submission từ lịch sử làm bài hoặc trang kết quả.
  2. Hệ thống kiểm tra quyền truy cập submission.
  3. Hệ thống lấy kết quả Auto-Grader.
  4. Hệ thống hiển thị điểm số, trạng thái tổng quát và thời gian chấm.
  5. Hệ thống hiển thị trạng thái từng test case và các lỗi biên dịch, lỗi chạy hoặc giới hạn tài nguyên nếu có.
  6. Student xem chi tiết kết quả chấm bài.
- **Luồng tương tác thay thế**:
  - **4a. Submission đang được xử lý**: Hệ thống hiển thị trạng thái `PENDING` hoặc `RUNNING` và cho phép Student tải lại kết quả.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Submission không tồn tại**: Hệ thống thông báo **"Không tìm thấy bài nộp."**
  - **E2 - Student không có quyền truy cập**: Hệ thống từ chối yêu cầu và không hiển thị dữ liệu submission.
  - **E3 - Chưa có kết quả chấm**: Hệ thống thông báo **"Kết quả chấm bài chưa sẵn sàng."**

---

### UC-ST14 — Xem Nhận Xét AI
- **Mô tả**: Cho phép Student xem nhận xét do AI tạo ra dựa trên bài làm và kết quả chấm.
- **Tác nhân**: Student.
- **Tiền điều kiện**:
  - Student đã đăng nhập và submission thuộc về Student.
  - Submission đã có kết quả chấm hoặc đủ dữ liệu để tạo feedback.
- **Hậu điều kiện**: Nhận xét AI được hiển thị nếu đã được tạo; dữ liệu bài nộp không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student mở trang kết quả của một submission.
  2. Hệ thống kiểm tra quyền truy cập và trạng thái AI feedback.
  3. Hệ thống lấy nhận xét AI đã lưu.
  4. Hệ thống hiển thị nhận xét về lỗi, chất lượng mã nguồn, độ phức tạp và đề xuất cải thiện nếu có.
  5. Student xem và sử dụng nhận xét để cải thiện bài làm.
- **Luồng tương tác thay thế**:
  - **3a. AI feedback đang được tạo**: Hệ thống hiển thị trạng thái chờ và cập nhật khi feedback sẵn sàng.
  - **3b. AI feedback chưa được bật cho bài tập**: Hệ thống thông báo tính năng không khả dụng cho submission này.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không tìm thấy submission**: Hệ thống thông báo **"Không tìm thấy bài nộp."**
  - **E2 - Student không có quyền truy cập**: Hệ thống từ chối yêu cầu xem feedback.
  - **E3 - AI Service gặp lỗi**: Hệ thống thông báo **"Chưa thể tạo nhận xét AI, vui lòng thử lại sau."**

---

### UC-ST15 — Tương Tác Với AI Tutor (Socratic Hinting)
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
  - **2a. Student không chọn bài làm hoặc submission**: Hệ thống chỉ gửi context của đề bài và các thông tin được phép xem.
  - **8a. Student bắt đầu hội thoại mới**: Hệ thống xóa context hội thoại trước khỏi phiên hiện tại và khởi tạo phiên mới.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Câu hỏi rỗng hoặc vượt giới hạn**: Hệ thống yêu cầu Student nhập câu hỏi hợp lệ.
  - **E2 - AI Service không khả dụng**: Hệ thống thông báo **"AI Tutor hiện không khả dụng, vui lòng thử lại sau."**
  - **E3 - Nội dung yêu cầu không phù hợp chính sách**: Hệ thống từ chối yêu cầu và hiển thị thông báo phù hợp.

---

### UC-ST16 — Xem Lịch Sử Làm Bài
- **Mô tả**: Cho phép Student tra cứu các submission của mình và xem chi tiết từng lần nộp bài.
- **Tác nhân**: Student.
- **Tiền điều kiện**: Student đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Lịch sử submission của Student được hiển thị; dữ liệu bài nộp không bị thay đổi.
- **Luồng tương tác chính**:
  1. Student truy cập mục **"Lịch sử làm bài"** hoặc lịch sử nộp bài của một bài tập.
  2. Hệ thống xác thực phiên đăng nhập.
  3. Hệ thống truy vấn các submission thuộc về Student.
  4. Hệ thống sắp xếp lịch sử theo thời gian và hiển thị bài tập, thời điểm nộp, trạng thái, điểm và ngôn ngữ.
  5. Student chọn một submission để xem mã nguồn, kết quả test và feedback được phép xem.
- **Luồng tương tác thay thế**:
  - **4a. Student lọc lịch sử**: Hệ thống lọc theo bài tập, lớp, trạng thái hoặc khoảng thời gian.
  - **5a. Student chọn hai submission**: Hệ thống hiển thị phần khác nhau giữa các phiên bản nếu chức năng so sánh được hỗ trợ.
- **Luồng tương tác ngoại lệ**:
  - **E1 - Không có lịch sử submission**: Hệ thống hiển thị danh sách rỗng và thông báo **"Chưa có bài nộp nào."**
  - **E2 - Lỗi truy vấn dữ liệu**: Hệ thống thông báo **"Không thể tải lịch sử làm bài, vui lòng thử lại sau."**

---

### UC-ST17 — Xem Bảng Điểm Cá Nhân
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

# 03. LUỒNG THỰC HIỆN CHI TIẾT CỦA CÁC USE CASE (USE CASE FLOWS)

---

### UC-01 — Đăng nhập
- **Mô tả**: Cho phép người dùng xác thực tài khoản để bắt đầu phiên làm việc trên hệ thống.
- **Tác nhân**: Sinh viên, Giáo viên, Quản trị viên, Giáo vụ, Quản trị viên hệ thống.
- **Tiền điều kiện**: Người dùng đã có tài khoản trong hệ thống.
- **Hậu điều kiện**: Phiên đăng nhập được tạo thành công. Hệ thống cấp access_token cùng refresh_token và chuyển người dùng đến trang chính phù hợp với vai trò. Nếu đăng nhập thất bại, phiên không được tạo.
- **Luồng tương tác chính**:
  1. Người dùng truy cập trang đăng nhập.
  2. Hệ thống hiển thị biểu mẫu yêu cầu Email và Mật khẩu.
  3. Người dùng nhập thông tin tài khoản và chọn "Đăng nhập".
  4. Hệ thống kiểm tra định dạng dữ liệu và tìm tài khoản tương ứng.
  5. Hệ thống đối chiếu mật khẩu với mật khẩu đã được băm trong cơ sở dữ liệu, đồng thời kiểm tra trạng thái tài khoản.
  6. Hệ thống tạo phiên đăng nhập và cấp access_token cùng refresh_token.
  7. Hệ thống chuyển người dùng đến giao diện tương ứng với vai trò (Sinh viên, Giáo viên, Giáo vụ, Quản trị viên, Quản trị viên hệ thống).
- **Luồng tương tác thay thế**:
  - 7a. Người dùng truy cập trang yêu cầu đăng nhập trước đó: Hệ thống chuyển người dùng về trang yêu cầu ban đầu.
  - 7b. Tài khoản đang dùng mật khẩu tạm: Hệ thống chuyển người dùng đến biểu mẫu đổi mật khẩu bắt buộc; đổi thành công mới vào trang chính.
- **Luồng tương tác ngoại lệ**:
  - E1 - Thông tin đăng nhập không hợp lệ: Hệ thống thông báo "Email hoặc mật khẩu không chính xác."
  - E2 - Tài khoản bị khóa hoặc vô hiệu hóa: Hệ thống thông báo "Tài khoản đã bị khóa hoặc vô hiệu hóa."
  - E3 - Lỗi hệ thống: Hệ thống thông báo "Đăng nhập thất bại, vui lòng thử lại sau."

---

### UC-02 — Đăng xuất
- **Mô tả**: Cho phép người dùng kết thúc phiên làm việc hiện tại trên hệ thống.
- **Tác nhân**: Sinh viên, Giáo viên, Quản trị viên, Giáo vụ, Quản trị viên hệ thống.
- **Tiền điều kiện**: Người dùng đang có phiên đăng nhập hợp lệ.
- **Hậu điều kiện**: Phiên đăng nhập của người dùng được kết thúc. Các thông tin xác thực cục bộ được xóa và người dùng được chuyển về trang đăng nhập.
- **Luồng tương tác chính**:
  1. Người dùng chọn "Đăng xuất" trên thanh điều hướng.
  2. Hệ thống hiển thị yêu cầu xác nhận đăng xuất.
  3. Người dùng xác nhận yêu cầu.
  4. Hệ thống thu hồi hoặc đưa refresh_token vào danh sách vô hiệu hóa.
  5. Hệ thống xóa token xác thực được lưu trên trình duyệt.
  6. Hệ thống kết thúc phiên đăng nhập và chuyển người dùng về trang đăng nhập.
- **Luồng tương tác thay thế**:
  - 3a. Người dùng hủy xác nhận: Hệ thống đóng hộp thoại và giữ nguyên phiên đăng nhập.
- **Luồng tương tác ngoại lệ**:
  - E1 - Phiên đăng nhập đã hết hạn: Hệ thống xóa thông tin xác thực cục bộ và chuyển người dùng về trang đăng nhập.

---

### UC-03 — Quên mật khẩu
- **Mô tả**: Cho phép người dùng xác thực quyền sở hữu tài khoản và đặt lại mật khẩu khi không nhớ mật khẩu hiện tại.
- **Tác nhân**: Sinh viên, Giáo viên, Quản trị viên, Giáo vụ, Quản trị viên hệ thống.
- **Tiền điều kiện**: Người dùng đang ở trang đăng nhập và có quyền truy cập địa chỉ email đã đăng ký.
- **Hậu điều kiện**: Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu. Mã/liên kết khôi phục đã sử dụng bị vô hiệu hóa.
- **Luồng tương tác chính**:
  1. Người dùng chọn "Quên mật khẩu" tại trang đăng nhập.
  2. Hệ thống hiển thị biểu mẫu yêu cầu nhập email tài khoản.
  3. Người dùng nhập email và chọn "Gửi yêu cầu".
  4. Hệ thống kiểm tra định dạng email và tạo mã OTP hoặc liên kết đặt lại mật khẩu có thời hạn.
  5. Hệ thống gửi mã hoặc liên kết xác thực đến email của người dùng.
  6. Người dùng sử dụng mã hoặc liên kết nhận được để mở biểu mẫu đặt lại mật khẩu.
  7. Người dùng nhập mật khẩu mới, xác nhận mật khẩu và chọn "Cập nhật mật khẩu".
  8. Hệ thống kiểm tra mã/liên kết còn hợp lệ, kiểm tra chính sách mật khẩu mới.
  9. Hệ thống băm mật khẩu mới, cập nhật vào cơ sở dữ liệu và vô hiệu hóa mã/liên kết đã sử dụng.
  10. Hệ thống thông báo "Khôi phục mật khẩu thành công." và chuyển người dùng về trang đăng nhập.
- **Luồng tương tác thay thế**:
  - 5a. Người dùng không nhận được email: Người dùng yêu cầu gửi lại sau khi hết thời gian chờ rate limit; hệ thống cấp mã/liên kết mới.
- **Luồng tương tác ngoại lệ**:
  - E1 - Email không tồn tại hoặc không hợp lệ: Hệ thống thông báo yêu cầu đã được tiếp nhận mà không tiết lộ tài khoản có tồn tại hay không.
  - E2 - Mã hoặc liên kết hết hạn/không hợp lệ: Hệ thống thông báo "Mã hoặc liên kết khôi phục không hợp lệ hoặc đã hết hạn."
  - E3 - Mật khẩu mới không đạt yêu cầu: Hệ thống thông báo "Mật khẩu mới không đáp ứng yêu cầu bảo mật hoặc không trùng khớp."
  - E4 - Lỗi hệ thống: Hệ thống thông báo "Không thể khôi phục mật khẩu, vui lòng thử lại sau."

---

### UC-04 — Xem thông tin cá nhân
- **Mô tả**: Cho phép người dùng xem thông tin cá nhân đã lưu trong hệ thống.
- **Tác nhân**: Sinh viên, Giáo viên, Quản trị viên, Giáo vụ, Quản trị viên hệ thống.
- **Tiền điều kiện**: Người dùng đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Thông tin cá nhân hiện tại của người dùng được hiển thị; dữ liệu trong cơ sở dữ liệu không bị thay đổi.
- **Luồng tương tác chính**:
  1. Người dùng truy cập trang cá nhân.
  2. Hệ thống xác thực phiên đăng nhập và quyền truy cập của người dùng.
  3. Hệ thống truy vấn thông tin cá nhân từ cơ sở dữ liệu.
  4. Hệ thống hiển thị các thông tin được phép xem gồm họ tên, email, số điện thoại, ảnh đại diện và vai trò.
- **Luồng tương tác thay thế**:
  - 3a. Người dùng tải lại trang: Hệ thống truy vấn lại dữ liệu mới nhất từ cơ sở dữ liệu và hiển thị thông tin cập nhật.
- **Luồng tương tác ngoại lệ**:
  - E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn: Hệ thống yêu cầu đăng nhập lại.
  - E2 - Không tìm thấy thông tin cá nhân: Hệ thống thông báo "Không tìm thấy thông tin cá nhân."
  - E3 - Lỗi truy vấn dữ liệu: Hệ thống thông báo "Không thể tải thông tin cá nhân, vui lòng thử lại sau."

---

### UC-05 — Cập nhật thông tin cá nhân
- **Mô tả**: Cho phép người dùng chỉnh sửa và lưu các thông tin cá nhân được hệ thống cho phép cập nhật.
- **Tác nhân**: Sinh viên, Giáo viên, Quản trị viên, Giáo vụ, Quản trị viên hệ thống.
- **Tiền điều kiện**: Người dùng đã đăng nhập và có phiên xác thực hợp lệ. Thông tin cá nhân đã tồn tại trong hệ thống.
- **Hậu điều kiện**: Thông tin hợp lệ được cập nhật và lưu vào cơ sở dữ liệu. Nếu cập nhật thất bại, thông tin cũ được giữ nguyên.
- **Luồng tương tác chính**:
  1. Người dùng truy cập trang cá nhân.
  2. Hệ thống xác thực phiên đăng nhập và hiển thị thông tin hiện tại.
  3. Người dùng chọn "Chỉnh sửa".
  4. Hệ thống hiển thị biểu mẫu với các trường được phép cập nhật (họ tên, số điện thoại, ảnh đại diện).
  5. Người dùng chỉnh sửa thông tin và chọn "Lưu thay đổi".
  6. Hệ thống kiểm tra tính hợp lệ của dữ liệu.
  7. Hệ thống cập nhật thông tin vào cơ sở dữ liệu.
  8. Hệ thống thông báo "Cập nhật thông tin cá nhân thành công." và hiển thị dữ liệu mới.
- **Luồng tương tác thay thế**:
  - 5a. Người dùng chọn "Hủy": Hệ thống hủy thao tác chỉnh sửa và giữ nguyên thông tin hiện tại.
  - 5b. Người dùng không thay đổi thông tin: Hệ thống giữ nguyên dữ liệu hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn: Hệ thống chuyển người dùng về trang đăng nhập.
  - E2 - Thông tin không hợp lệ: Hệ thống thông báo "Thông tin cá nhân không hợp lệ."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Cập nhật thông tin cá nhân thất bại."

---

### UC-06 — Đổi mật khẩu
- **Mô tả**: Cho phép người dùng thay đổi mật khẩu hiện tại sau khi xác thực mật khẩu cũ.
- **Tác nhân**: Sinh viên, Giáo viên, Quản trị viên, Giáo vụ, Quản trị viên hệ thống.
- **Tiền điều kiện**: Người dùng đã đăng nhập và có phiên xác thực hợp lệ. Người dùng biết mật khẩu hiện tại.
- **Hậu điều kiện**: Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu. Mật khẩu cũ không còn hiệu lực.
- **Luồng tương tác chính**:
  1. Người dùng truy cập chức năng "Đổi mật khẩu" trong trang cá nhân.
  2. Hệ thống hiển thị biểu mẫu gồm Mật khẩu hiện tại, Mật khẩu mới và Xác nhận mật khẩu mới.
  3. Người dùng nhập đầy đủ thông tin và chọn "Đổi mật khẩu".
  4. Hệ thống xác thực phiên đăng nhập và đối chiếu mật khẩu hiện tại.
  5. Hệ thống kiểm tra mật khẩu mới đáp ứng chính sách bảo mật và trùng khớp với phần xác nhận.
  6. Hệ thống băm mật khẩu mới và lưu vào cơ sở dữ liệu.
  7. Hệ thống thông báo "Đổi mật khẩu thành công."
- **Luồng tương tác thay thế**:
  - 3a. Người dùng chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên mật khẩu hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Phiên đăng nhập không hợp lệ: Hệ thống yêu cầu đăng nhập lại.
  - E2 - Mật khẩu hiện tại không chính xác: Hệ thống thông báo "Mật khẩu hiện tại không chính xác."
  - E3 - Mật khẩu mới không hợp lệ: Hệ thống thông báo "Mật khẩu mới không đáp ứng yêu cầu bảo mật hoặc không trùng khớp."
  - E4 - Mật khẩu mới trùng mật khẩu hiện tại: Hệ thống thông báo "Mật khẩu mới phải khác mật khẩu hiện tại."
  - E5 - Lỗi lưu dữ liệu: Hệ thống thông báo "Đổi mật khẩu thất bại."

---

### UC-07 — Xem danh sách bài tập
- **Mô tả**: Cho phép Sinh viên xem và tra cứu danh sách các bài tập được giao cho những lớp mà mình tham gia.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Danh sách bài tập phù hợp được hiển thị; dữ liệu bài tập không bị thay đổi.
- **Luồng tương tác chính**:
  1. Sinh viên truy cập mục "Bài tập".
  2. Hệ thống xác thực phiên đăng nhập và quyền truy cập của Sinh viên.
  3. Hệ thống lấy danh sách lớp mà Sinh viên đang tham gia.
  4. Hệ thống truy vấn các bài tập được giao cho các lớp đó.
  5. Hệ thống hiển thị danh sách với các thông tin: Tên bài, lớp, độ khó, thời hạn nộp (Deadline), trạng thái bài làm (DRAFT, SUBMITTED, GRADING, COMPLETED) và điểm chính thức nếu đã được Giáo viên xác nhận.
  6. Sinh viên tìm kiếm hoặc lọc danh sách theo lớp hoặc trạng thái.
- **Luồng tương tác thay thế**:
  - 6a. Sinh viên không chọn bộ lọc: Hệ thống hiển thị toàn bộ bài tập được giao.
  - 6b. Không có bài tập phù hợp: Hệ thống hiển thị danh sách rỗng và thông báo phù hợp.
- **Luồng tương tác ngoại lệ**:
  - E1 - Phiên đăng nhập hết hạn: Hệ thống yêu cầu Sinh viên đăng nhập lại.
  - E2 - Lỗi truy vấn dữ liệu: Hệ thống thông báo "Không thể tải danh sách bài tập, vui lòng thử lại sau."

---

### UC-08 — Xem chi tiết bài tập
- **Mô tả**: Cho phép Sinh viên xem nội dung và yêu cầu chi tiết của một bài tập được giao.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập và bài tập được giao cho lớp mà Sinh viên tham gia.
- **Hậu điều kiện**: Thông tin chi tiết bài tập được hiển thị. Nếu Sinh viên chọn "Làm bài", hệ thống chuyển đến không gian soạn thảo mã nguồn.
- **Luồng tương tác chính**:
  1. Sinh viên chọn một bài tập từ danh sách.
  2. Hệ thống kiểm tra quyền truy cập của Sinh viên với bài tập.
  3. Hệ thống lấy thông tin bài tập từ cơ sở dữ liệu.
  4. Hệ thống hiển thị đề bài (hỗ trợ Markdown, LaTeX), yêu cầu Input/Output, ràng buộc kỹ thuật, giới hạn thời gian (Time Limit), giới hạn bộ nhớ (Memory Limit), Sample Test Cases và Rubric đánh giá.
  5. Sinh viên chọn "Làm bài".
  6. Hệ thống chuyển Sinh viên đến không gian làm bài (Monaco Editor) với trạng thái DRAFT.
- **Luồng tương tác thay thế**:
  - 5a. Sinh viên quay lại danh sách: Hệ thống đưa Sinh viên về trang danh sách bài tập.
  - 5b. Bài tập đã qua Deadline: Hệ thống hiển thị thông báo "Bài tập đã đóng" và không cho phép làm bài mới.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Sinh viên không có quyền truy cập: Hệ thống thông báo "Bạn không có quyền truy cập bài tập này."
  - E3 - Bài tập đã đóng hoàn toàn: Hệ thống thông báo "Bài tập hiện không khả dụng."
  - E4 - Lỗi tải dữ liệu: Hệ thống thông báo "Không thể tải chi tiết bài tập, vui lòng thử lại sau."

---

### UC-09 — Viết code
- **Mô tả**: Cho phép Sinh viên viết, chỉnh sửa mã nguồn trực tiếp trong trình soạn thảo của hệ thống với cơ chế lưu nháp và Autosave.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập, bài tập đang mở (chưa qua Deadline), trạng thái bài làm chưa ở SUBMITTED.
- **Hậu điều kiện**: Mã nguồn được cập nhật trong Editor và lưu vào bản nháp DRAFT (thông qua Autosave hoặc nút Save). Bài làm chưa trở thành Submission chính thức cho đến khi được Submit hoặc Auto-submit tại Deadline.
- **Luồng tương tác chính**:
  1. Sinh viên mở không gian làm bài từ chi tiết bài tập.
  2. Hệ thống tải đề bài, cấu hình ngôn ngữ và nạp mã nguồn bản nháp DRAFT gần nhất (nếu có).
  3. Hệ thống mở Monaco Editor.
  4. Sinh viên nhập hoặc chỉnh sửa mã nguồn.
  5. Hệ thống tự động kích hoạt Autosave theo chu kỳ cấu hình (hoặc sau khi ngừng gõ) để lưu mã nguồn vào bản nháp DRAFT trên server/cache.
  6. Sinh viên có thể chủ động chọn "Lưu bài làm" để lưu thủ công bản nháp DRAFT.
  7. Sinh viên tiếp tục chỉnh sửa cho đến khi sẵn sàng nộp bài.
- **Luồng tương tác thay thế**:
  - 4a. Sinh viên tải lại trang: Hệ thống tự động khôi phục mã nguồn từ bản nháp DRAFT mới nhất được lưu trên server.
  - 6a. Sinh viên rời khỏi trang: Hệ thống thực hiện lưu bản nháp DRAFT trước khi thoát.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập đã hết hạn Deadline: Hệ thống khóa Editor (Read-only) và thông báo "Bài tập đã đóng, không thể tiếp tục chỉnh sửa."
  - E2 - Mã nguồn vượt quá dung lượng cho phép: Hệ thống thông báo lỗi và yêu cầu điều chỉnh.
  - E3 - Lỗi lưu bản nháp: Hệ thống hiển thị cảnh báo mất kết nối và khuyến nghị kiểm tra mạng.

---

### UC-10 — Upload file bài làm
- **Mô tả**: Cho phép Sinh viên tải tệp mã nguồn từ máy tính cá nhân vào trình soạn thảo đang mở để tiếp tục chỉnh sửa.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đang mở không gian làm bài của bài tập chưa hết hạn và bài làm đang ở trạng thái DRAFT.
- **Hậu điều kiện**: Nội dung file hợp lệ được nạp vào Monaco Editor và lưu vào bản nháp DRAFT. Thao tác Upload không tạo ra Submission chính thức.
- **Luồng tương tác chính**:
  1. Sinh viên chọn "Upload File" tại màn hình làm bài.
  2. Hệ thống hiển thị hộp thoại chọn tệp.
  3. Sinh viên chọn tệp mã nguồn từ máy tính.
  4. Hệ thống kiểm tra phần mở rộng (extension) phù hợp với ngôn ngữ bài tập và kích thước tệp trong giới hạn cho phép.
  5. Hệ thống đọc nội dung tệp và nạp vào Monaco Editor.
  6. Hệ thống lưu nội dung vừa nạp vào bản nháp DRAFT.
  7. Hệ thống thông báo "Tải tệp lên thành công."
- **Luồng tương tác thay thế**:
  - 3a. Sinh viên hủy chọn tệp: Hệ thống đóng hộp thoại và giữ nguyên nội dung hiện tại trong Editor.
  - 5a. Sinh viên tiếp tục chỉnh sửa code sau khi upload: Hệ thống tiếp tục lưu nháp theo cơ chế Autosave.
- **Luồng tương tác ngoại lệ**:
  - E1 - Định dạng tệp không được hỗ trợ: Hệ thống thông báo "Định dạng tệp không khớp với ngôn ngữ lập trình của bài tập."
  - E2 - Tệp vượt quá kích thước cho phép: Hệ thống thông báo "Kích thước tệp vượt quá giới hạn quy định."
  - E3 - Không thể đọc tệp: Hệ thống thông báo "Không thể đọc nội dung tệp, vui lòng thử lại."

---

### UC-11 — Nộp bài
- **Mô tả**: Cho phép Sinh viên chủ động nộp bài làm chính thức hoặc hệ thống tự động nộp khi hết Deadline. Sau khi nộp, bài làm chuyển sang trạng thái SUBMITTED và bị khóa vĩnh viễn (Read-only) để chờ quy trình Batch Grading sau Deadline.
- **Tác nhân**: Sinh viên, Hệ thống (Backend Worker).
- **Tiền điều kiện**: Sinh viên đang làm bài tập chưa qua Deadline (đối với nộp thủ công) hoặc đã đến thời điểm Deadline (đối với Auto-submit). Bài làm đang ở trạng thái DRAFT.
- **Hậu điều kiện**: Bản nộp duy nhất của Sinh viên được ghi nhận ở trạng thái SUBMITTED với trigger_type tương ứng (MANUAL hoặc AUTO_EXPIRED). Editor bị khóa Read-only. Sinh viên không thể sửa, upload hay nộp lại. Bài nộp được giữ nguyên chờ đến sau Deadline để tham gia Batch Grading.
- **Luồng tương tác chính**:
  1. Sinh viên chọn "Nộp bài" trên giao diện làm bài.
  2. Hệ thống kiểm tra thời gian hiện tại còn trước Deadline ($T < T_{\text{deadline}}$).
  3. Hệ thống hiển thị popup xác nhận cảnh báo: "Sau khi nộp, bài làm sẽ bị khóa và không thể chỉnh sửa hoặc nộp lại."
  4. Sinh viên chọn "Xác nhận nộp".
  5. Hệ thống lấy mã nguồn bản nháp DRAFT hiện tại.
  6. Hệ thống tạo bản nộp chính thức, chuyển trạng thái từ DRAFT sang SUBMITTED và ghi nhận trigger_type = MANUAL.
  7. Hệ thống khóa Editor sang chế độ Read-only.
  8. Hệ thống thông báo "Nộp bài thành công. Bài làm đã được khóa và sẽ được chấm sau khi hết thời hạn nộp bài."
- **Luồng tương tác thay thế**:
  - 1a. Đến thời điểm hết hạn Deadline mà Sinh viên chưa chủ động nộp bài (Auto-submit):
    - 1a.1. Backend Scheduled Worker quét các bài làm còn ở trạng thái DRAFT.
    - 1a.2. Backend lấy mã nguồn bản nháp DRAFT (Autosave/Save) mới nhất được lưu trên server/cache.
    - 1a.3. Hệ thống tạo bản nộp chính thức, chuyển trạng thái DRAFT sang SUBMITTED và ghi nhận trigger_type = AUTO_EXPIRED.
    - 1a.4. Hệ thống khóa toàn bộ Editor của các bài làm này trên giao diện người dùng.
  - 3a. Sinh viên chọn "Hủy" trong popup xác nhận: Hệ thống đóng popup và giữ nguyên trạng thái DRAFT để Sinh viên tiếp tục chỉnh sửa.
- **Luồng tương tác ngoại lệ**:
  - E1 - Quá hạn nộp bài (Strict No-Late): Hệ thống từ chối nhận bài, trả về mã lỗi 403 Forbidden / Assignment Closed, hiển thị "Bài tập đã đóng" và vô hiệu hóa nút nộp bài.
  - E2 - Mã nguồn không hợp lệ: Hệ thống thông báo "Mã nguồn không hợp lệ hoặc bị lỗi định dạng."
  - E3 - Lỗi kết nối hệ thống: Hệ thống thông báo "Không thể nộp bài, vui lòng kiểm tra kết nối mạng và thử lại."

---

### UC-12 — Xem kết quả Auto-Grader
- **Mô tả**: Cho phép Sinh viên xem kết quả chấm tự động của bài nộp sau khi hệ thống đã hoàn tất quy trình Batch Grading sau Deadline.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập, bài nộp thuộc về Sinh viên và hệ thống đã hoàn tất chấm bài (trạng thái COMPLETED).
- **Hậu điều kiện**: Kết quả Auto-Grader được hiển thị; dữ liệu chấm không bị thay đổi. Dữ liệu Input/Output của Hidden Test Cases được bảo mật và ẩn khỏi Sinh viên.
- **Luồng tương tác chính**:
  1. Sinh viên mở bài tập đã có kết quả.
  2. Hệ thống kiểm tra quyền truy cập và trạng thái bài làm (COMPLETED).
  3. Hệ thống truy vấn kết quả Auto-Grader từ cơ sở dữ liệu.
  4. Hệ thống hiển thị điểm số Auto-Grader, trạng thái tổng quát, thời gian chấm.
  5. Hệ thống hiển thị danh sách các test case với trạng thái đạt/không đạt, thời gian thực thi, mức sử dụng bộ nhớ (ẩn dữ liệu Input/Output của Hidden Test Cases).
  6. Sinh viên xem chi tiết kết quả kiểm thử.
- **Luồng tương tác thay thế**:
  - 2a. Bài nộp đang trong quy trình chấm gom (GRADING): Hệ thống hiển thị thông báo "Bài tập đang trong quá trình chấm tự động, vui lòng quay lại sau."
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài nộp không tồn tại: Hệ thống thông báo "Không tìm thấy bài nộp."
  - E2 - Sinh viên không có quyền truy cập: Hệ thống từ chối truy cập.
  - E3 - Chưa có kết quả chấm: Hệ thống thông báo "Kết quả chấm bài chưa sẵn sàng."

---

### UC-13 — Xem nhận xét AI
- **Mô tả**: Cho phép Sinh viên xem phản hồi và đánh giá chi tiết do AI Review tạo ra dựa trên evidence từ mã nguồn và kết quả thực thi sau Deadline.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập, bài nộp thuộc về Sinh viên và đã hoàn tất quy trình Batch Grading (COMPLETED).
- **Hậu điều kiện**: Phản hồi AI Review được hiển thị; dữ liệu bài nộp không bị thay đổi.
- **Luồng tương tác chính**:
  1. Sinh viên mở trang kết quả bài làm.
  2. Hệ thống kiểm tra quyền truy cập và trạng thái bài nộp.
  3. Hệ thống truy vấn nội dung AI Review đã được lưu.
  4. Hệ thống hiển thị nhận xét của AI về chất lượng mã nguồn (Code Quality), độ phức tạp (Complexity), Code Style, phân tích lỗi và các gợi ý cải thiện.
  5. Sinh viên đọc nhận xét để rút kinh nghiệm học tập.
- **Luồng tương tác thay thế**:
  - 4a. Phản hồi AI chưa được bật hoặc chưa công bố cho bài tập: Hệ thống thông báo nhận xét AI chưa khả dụng.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy bài nộp: Hệ thống thông báo "Không tìm thấy bài nộp."
  - E2 - Sinh viên không có quyền truy cập: Hệ thống từ chối yêu cầu.
  - E3 - Lỗi tải dữ liệu: Hệ thống thông báo "Không thể tải nhận xét AI, vui lòng thử lại sau."

---

### UC-14 — Tương tác với AI Tutor
- **Mô tả**: Cho phép Sinh viên tương tác với AI Tutor sau khi đã có kết quả đánh giá (hậu kiểm) để nhận giải thích, gợi mở tư duy theo phương pháp Socratic nhằm nâng cao kỹ năng lập trình.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập, bài tập đã hoàn tất đánh giá và công bố kết quả (COMPLETED / có điểm chính thức).
- **Hậu điều kiện**: Phiên hội thoại hậu kiểm được thực hiện. AI Tutor chỉ giải thích gợi mở, không đưa đáp án trực tiếp và không làm thay đổi bài nộp, điểm số hay Rubric.
- **Luồng tương tác chính**:
  1. Sinh viên mở chức năng "AI Tutor" từ màn hình kết quả bài làm.
  2. Hệ thống thu thập context hậu kiểm gồm: Đề bài, mã nguồn bản nộp cuối cùng, kết quả Auto-Grader, AI Review, nhận xét của Giáo viên và điểm chính thức.
  3. Sinh viên nhập câu hỏi thắc mắc về lỗi hoặc thuật toán và chọn "Gửi".
  4. Hệ thống kiểm tra tính hợp lệ của câu hỏi và quyền truy cập context.
  5. Backend gửi prompt kèm guardrails sư phạm Socratic đến AI Engine.
  6. AI Tutor phân tích context và phản hồi theo phương pháp Socratic: đặt câu hỏi định hướng, gợi ý từng bước tư duy, không đưa code giải sẵn.
  7. Hệ thống hiển thị câu trả lời trong khung hội thoại.
  8. Sinh viên tiếp tục tương tác trong phiên làm việc.
- **Luồng tương tác thay thế**:
  - 8a. Sinh viên làm mới phiên hội thoại: Hệ thống xóa lịch sử hội thoại tạm thời và bắt đầu phiên hỏi đáp mới.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập chưa có kết quả (đang DRAFT hoặc đang GRADING): Hệ thống từ chối mở AI Tutor và thông báo "AI Tutor chỉ khả dụng sau khi bài làm đã có kết quả đánh giá."
  - E2 - Câu hỏi rỗng hoặc vượt giới hạn: Hệ thống yêu cầu nhập lại câu hỏi hợp lệ.<br>  - E3 - Dịch vụ AI không khả dụng: Hệ thống thông báo "AI Tutor hiện không khả dụng, vui lòng thử lại sau."

---

### UC-15 — Xem bài đã nộp
- **Mô tả**: Cho phép Sinh viên xem lại bản nộp chính thức duy nhất của mình cho một bài tập, bao gồm mã nguồn đã nộp, thời gian nộp và trạng thái xử lý.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập và bài tập đã có bản nộp chính thức (SUBMITTED, GRADING, hoặc COMPLETED).
- **Hậu điều kiện**: Thông tin bản nộp duy nhất được hiển thị ở chế độ chỉ đọc (Read-only); không có dữ liệu nào bị thay đổi.
- **Luồng tương tác chính**:
  1. Sinh viên truy cập mục "Bài đã nộp" của một bài tập.
  2. Hệ thống xác thực phiên đăng nhập và quyền truy cập của Sinh viên.
  3. Hệ thống truy vấn bản nộp chính thức duy nhất của Sinh viên đối với bài tập đó.
  4. Hệ thống hiển thị thông tin chi tiết: Mã nguồn đã nộp, thời điểm nộp, hình thức nộp (MANUAL hoặc AUTO_EXPIRED), trạng thái hiện tại (SUBMITTED / GRADING / COMPLETED) và kết quả nếu đã chấm xong.
  5. Sinh viên xem lại mã nguồn và thông tin nộp bài.
- **Luồng tương tác thay thế**:
  - 4a. Sinh viên chưa nộp bài (vẫn ở DRAFT): Hệ thống hiển thị thông báo "Bạn chưa có bản nộp chính thức cho bài tập này."
- **Luồng tương tác ngoại lệ**:
  - E1 - Phiên đăng nhập hết hạn: Hệ thống yêu cầu đăng nhập lại.
  - E2 - Lỗi truy vấn dữ liệu: Hệ thống thông báo "Không thể tải thông tin bài nộp, vui lòng thử lại sau."

---

### UC-16 — Xem bảng điểm cá nhân
- **Mô tả**: Cho phép Sinh viên xem bảng tổng hợp điểm các bài tập và các lớp học mà mình tham gia.
- **Tác nhân**: Sinh viên.
- **Tiền điều kiện**: Sinh viên đã đăng nhập và có phiên xác thực hợp lệ.
- **Hậu điều kiện**: Bảng điểm cá nhân được hiển thị; dữ liệu điểm không bị thay đổi.
- **Luồng tương tác chính**:
  1. Sinh viên truy cập trang "Bảng điểm".
  2. Hệ thống xác thực phiên đăng nhập.
  3. Hệ thống truy vấn danh sách kết quả học tập của Sinh viên theo từng lớp và bài tập.
  4. Hệ thống hiển thị bảng điểm gồm: Tên bài tập, lớp học, điểm chính thức (do Giáo viên xác nhận kèm nhận xét), hoặc điểm Auto-Grader (với nhãn 'Tạm tính' nếu Giáo viên chưa xác nhận chính thức), trạng thái bài làm và thời gian cập nhật.
  5. Sinh viên tìm kiếm hoặc lọc bảng điểm theo lớp hoặc học kỳ.
- **Luồng tương tác thay thế**:
  - 4a. Bài tập đang trong quá trình chấm hoặc chưa tới hạn: Hệ thống hiển thị trạng thái "Đang chấm" hoặc "Chưa có kết quả", không hiển thị điểm 0.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không có kết quả: Hệ thống hiển thị bảng điểm trống và thông báo "Chưa có kết quả học tập."
  - E2 - Lỗi hệ thống: Hệ thống thông báo "Không thể tải bảng điểm, vui lòng thử lại sau."

---

### UC-17 — *(ĐÃ BỊ HỦY BỎ)*
- **Mô tả**: Đã bỏ chức năng tạo lớp ở cấp Giáo viên. Việc tạo lớp được quản lý tập trung ở cấp Quản trị viên / Giáo vụ trong UC-38.
- **Tác nhân**: Không áp dụng.

---

### UC-18 — *(ĐÃ BỊ HỦY BỎ)*
- **Mô tả**: Đã bỏ chức năng chỉnh sửa lớp ở cấp Giáo viên. Việc chỉnh sửa lớp được quản lý tập trung ở cấp Quản trị viên / Giáo vụ trong UC-39.
- **Tác nhân**: Không áp dụng.

---

### UC-19 — *(ĐÃ BỊ HỦY BỎ)*
- **Mô tả**: Chức năng Đóng/Mở lớp đã được chuyển sang UC-40. Chức năng Lưu trữ/Khôi phục/Xóa lớp đã được chuyển sang UC-41. Không sử dụng UC-19.
- **Tác nhân**: Không áp dụng.

---

### UC-20 — *(ĐÃ BỊ HỦY BỎ)*
- **Mô tả**: Đã bỏ chức năng quản lý sinh viên ở cấp Giáo viên. Việc quản lý sinh viên trong lớp được quản lý tập trung ở cấp Quản trị viên / Giáo vụ trong UC-42.
- **Tác nhân**: Không áp dụng.

---

### UC-21 — Tạo bài tập
- **Mô tả**: Cho phép Giáo viên tạo bài tập mới và thiết lập cấu hình ban đầu cần thiết cho bài tập.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập và có quyền quản lý bài tập trong hệ thống.
- **Hậu điều kiện**: Bài tập mới được tạo thành công với cấu hình ban đầu và lưu vào cơ sở dữ liệu.
- **Luồng tương tác chính**:
  1. Giáo viên chọn chức năng "Tạo bài tập".
  2. Hệ thống hiển thị biểu mẫu tạo bài tập gồm: Tên bài, đề bài/mô tả, ngôn ngữ lập trình cho phép, mức độ khó, giới hạn thời gian thực thi (Time Limit), giới hạn bộ nhớ (Memory Limit) và Deadline ban đầu.
  3. Giáo viên nhập đầy đủ thông tin cấu hình ban đầu.
  4. Giáo viên chọn "Lưu bài tập".
  5. Hệ thống kiểm tra tính hợp lệ của dữ liệu (tên bài, hạn nộp phải trong tương lai, giới hạn tài nguyên hợp lệ).
  6. Hệ thống lưu bài tập vào cơ sở dữ liệu.
  7. Hệ thống thông báo "Tạo bài tập thành công." và chuyển đến trang chi tiết bài tập để thiết lập Test Cases (UC-25) và Rubric (UC-26).
- **Luồng tương tác thay thế**:
  - 4a. Giáo viên chọn "Hủy": Hệ thống hủy thao tác và quay lại danh sách bài tập.
- **Luồng tương tác ngoại lệ**:
  - E1 - Thông tin bài tập không hợp lệ: Hệ thống thông báo lỗi các trường chưa đúng quy định.
  - E2 - Deadline không hợp lệ: Hệ thống thông báo "Hạn nộp phải lớn hơn thời điểm hiện tại."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Tạo bài tập thất bại, vui lòng thử lại sau."

---

### UC-22 — Chỉnh sửa thông tin chung bài tập
- **Mô tả**: Cho phép Giáo viên cập nhật các thông tin chung của bài tập (Tên bài, Đề bài, Ngôn ngữ hỗ trợ, Mức độ khó, Giới hạn tài nguyên). Không bao gồm Deadline, Test Cases hay Rubric.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại trong hệ thống.
- **Hậu điều kiện**: Thông tin chung của bài tập được cập nhật; các cấu hình Deadline, Test Cases, Rubric không bị ảnh hưởng.
- **Luồng tương tác chính**:
  1. Giáo viên mở danh sách bài tập và chọn bài tập cần chỉnh sửa.
  2. Hệ thống hiển thị thông tin chung hiện tại của bài tập.
  3. Giáo viên chỉnh sửa các trường thông tin chung (Tên bài, đề bài, ngôn ngữ, độ khó, Time/Memory Limit).
  4. Giáo viên chọn "Lưu thay đổi".
  5. Hệ thống kiểm tra tính hợp lệ của dữ liệu.
  6. Hệ thống cập nhật thông tin chung vào cơ sở dữ liệu.
  7. Hệ thống thông báo "Cập nhật thông tin chung bài tập thành công."
- **Luồng tương tác thay thế**:
  - 4a. Giáo viên chọn "Hủy": Hệ thống hủy bỏ thay đổi và giữ nguyên thông tin hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy bài tập: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Giáo viên không có quyền: Hệ thống từ chối truy cập.
  - E3 - Dữ liệu không hợp lệ: Hệ thống thông báo "Thông tin bài tập không hợp lệ."
  - E4 - Lỗi lưu dữ liệu: Hệ thống thông báo "Cập nhật bài tập thất bại."

---

### UC-23 — Xóa bài tập
- **Mô tả**: Cho phép Giáo viên xóa hoặc vô hiệu hóa bài tập theo chính sách bảo toàn dữ liệu.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại.
- **Hậu điều kiện**: Bài tập được xóa hoặc vô hiệu hóa (xóa mềm) để bảo toàn dữ liệu bài nộp và điểm đã có.
- **Luồng tương tác chính**:
  1. Giáo viên mở danh sách bài tập và chọn bài cần xóa.
  2. Giáo viên chọn "Xóa bài tập".
  3. Hệ thống hiển thị hộp thoại xác nhận cảnh báo về dữ liệu liên quan.
  4. Giáo viên xác nhận xóa.
  5. Hệ thống kiểm tra trạng thái bài tập và dữ liệu bài nộp liên quan.
  6. Hệ thống thực hiện xóa mềm (Soft Delete) hoặc vô hiệu hóa bài tập.
  7. Hệ thống thông báo "Xử lý bài tập thành công." và cập nhật lại danh sách.
- **Luồng tương tác thay thế**:
  - 4a. Giáo viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên bài tập.
  - 6a. Bài tập chưa giao và chưa có bài nộp nào: Hệ thống thực hiện xóa bản ghi bài tập.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy bài tập: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Giáo viên không có quyền: Hệ thống từ chối yêu cầu.
  - E3 - Lỗi hệ thống: Hệ thống thông báo "Không thể xóa bài tập, vui lòng thử lại sau."

---

### UC-24 — Thiết lập hạn nộp bài
- **Mô tả**: Cho phép Giáo viên thiết lập và điều chỉnh thời hạn kết thúc nộp bài (Deadline) cho bài tập.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại.
- **Hậu điều kiện**: Thời hạn nộp bài (Deadline) mới được cập nhật và áp dụng cho toàn bộ sinh viên được giao bài.
- **Luồng tương tác chính**:
  1. Giáo viên truy cập danh sách bài tập và chọn bài tập cần cấu hình Deadline.
  2. Hệ thống hiển thị thông tin bài tập và Deadline hiện tại.
  3. Giáo viên chọn/nhập ngày và giờ hạn nộp bài mới.
  4. Giáo viên chọn "Lưu hạn nộp".
  5. Hệ thống kiểm tra tính hợp lệ của thời gian (phải lớn hơn thời điểm hiện tại).
  6. Hệ thống cập nhật Deadline mới vào cơ sở dữ liệu.
  7. Hệ thống thông báo "Thiết lập hạn nộp bài thành công."
- **Luồng tương tác thay thế**:
  - 4a. Giáo viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên Deadline cũ.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Deadline không hợp lệ: Hệ thống thông báo "Hạn nộp bài phải lớn hơn thời điểm hiện tại."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Thiết lập hạn nộp bài thất bại."

---

### UC-25 — Thiết lập test case
- **Mô tả**: Cho phép Giáo viên quản lý bộ Test Cases (thêm, sửa, xóa) phục vụ quy trình chấm điểm tự động. Việc cấu hình Sample Test Cases không cung cấp chức năng chạy thử cho Sinh viên.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại trên hệ thống.
- **Hậu điều kiện**: Bộ Test Cases được cập nhật và lưu trữ làm cơ sở chấm tự động trong Docker Sandbox sau Deadline.
- **Luồng tương tác chính**:
  1. Giáo viên mở chi tiết bài tập và chọn mục "Thiết lập Test Case".
  2. Hệ thống hiển thị danh sách Test Cases hiện có của bài tập.
  3. Giáo viên thực hiện Thêm mới, Chỉnh sửa hoặc Xóa Test Case.
  4. Với mỗi Test Case, Giáo viên nhập: Input, Expected Output, Phân loại (Sample Test Case hoặc Hidden Test Case) và Trọng số điểm.
  5. Giáo viên chọn "Lưu bộ Test Case".
  6. Hệ thống kiểm tra tính hợp lệ của bộ Test Cases (Input, Output không rỗng, trọng số hợp lệ).
  7. Hệ thống lưu bộ Test Cases vào cơ sở dữ liệu và thông báo "Thiết lập Test Case thành công."
- **Luồng tương tác thay thế**:
  - 3a. Xóa Test Case: Giáo viên chọn xóa một test case, xác nhận trong hộp thoại và hệ thống cập nhật danh sách tạm trước khi Lưu.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Dữ liệu Test Case không hợp lệ: Hệ thống thông báo "Dữ liệu đầu vào hoặc kết quả mong đợi không được để trống."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Thiết lập Test Case thất bại."

---

### UC-26 — Thiết lập rubric
- **Mô tả**: Cho phép Giáo viên thiết lập bộ tiêu chí đánh giá và trọng số điểm (Rubric) cho bài tập.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại trên hệ thống.
- **Hậu điều kiện**: Rubric được lưu thành công làm căn cứ đánh giá tổng hợp cho bài tập.
- **Luồng tương tác chính**:
  1. Giáo viên mở chi tiết bài tập và chọn mục "Thiết lập Rubric".
  2. Hệ thống hiển thị danh sách tiêu chí đánh giá hiện tại.
  3. Giáo viên cấu hình danh sách tiêu chí (Tên tiêu chí, Mô tả, Mức điểm/Trọng số). Tiêu chí Correctness do hệ thống tự động tính từ kết quả Hidden Test Cases.
  4. Giáo viên chọn "Lưu Rubric".
  5. Hệ thống kiểm tra tổng trọng số các tiêu chí (phải bằng 100% hoặc tổng thang điểm quy định).
  6. Hệ thống lưu Rubric vào cơ sở dữ liệu.
  7. Hệ thống thông báo "Thiết lập Rubric thành công."
- **Luồng tương tác thay thế**:
  - 3a. Xóa tiêu chí: Giáo viên chọn xóa một tiêu chí (khác tiêu chí Correctness bắt buộc), xác nhận và lưu lại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Trùng lặp tiêu chí: Hệ thống thông báo "Tên tiêu chí đánh giá bị trùng lặp."
  - E3 - Tổng trọng số không hợp lệ: Hệ thống thông báo "Tổng trọng số của các tiêu chí phải bằng 100%."
  - E4 - Lỗi lưu dữ liệu: Hệ thống thông báo "Thiết lập Rubric thất bại."

---

### UC-27 — Giao bài tập cho lớp
- **Mô tả**: Cho phép Giáo viên giao một bài tập đã cấu hình cho một hoặc nhiều lớp học do mình phụ trách để sinh viên thực hiện.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền quản lý bài tập, bài tập tồn tại và lớp học cần giao đang ở trạng thái Hoạt động.
- **Hậu điều kiện**: Bài tập được giao thành công cho các lớp đã chọn. Sinh viên trong các lớp này có thể xem đề bài và làm bài.
- **Luồng tương tác chính**:
  1. Giáo viên mở danh sách bài tập và chọn bài tập cần giao.
  2. Giáo viên chọn chức năng "Giao bài tập cho lớp".
  3. Hệ thống hiển thị danh sách các lớp học mà Giáo viên có quyền phụ trách và đang Hoạt động.
  4. Giáo viên chọn một hoặc nhiều lớp cần giao.
  5. Giáo viên chọn "Xác nhận giao bài".
  6. Hệ thống kiểm tra tính hợp lệ của các lớp được chọn.
  7. Hệ thống lưu thông tin giao bài vào cơ sở dữ liệu.
  8. Hệ thống thông báo "Giao bài tập thành công."
- **Luồng tương tác thay thế**:
  - 4a. Giáo viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên trạng thái hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Lớp học không còn hoạt động: Hệ thống thông báo "Không thể giao bài cho lớp không ở trạng thái Hoạt động."
  - E3 - Giáo viên không có quyền quản lý lớp: Hệ thống từ chối yêu cầu.
  - E4 - Lỗi lưu dữ liệu: Hệ thống thông báo "Giao bài tập thất bại."

---

### UC-28 — Xem bài nộp
- **Mô tả**: Cho phép Giáo viên xem danh sách và chi tiết bản nộp chính thức duy nhất của từng sinh viên đối với bài tập đã giao.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền phụ trách lớp/bài tập và bài tập đã được giao.
- **Hậu điều kiện**: Thông tin bản nộp duy nhất của sinh viên được hiển thị gồm mã nguồn, thời gian nộp, trigger_type, trạng thái và kết quả chấm; không có dữ liệu nào bị thay đổi.
- **Luồng tương tác chính**:
  1. Giáo viên mở bài tập cần kiểm tra.
  2. Hệ thống hiển thị danh sách sinh viên trong lớp cùng trạng thái bài làm (DRAFT, SUBMITTED, GRADING, COMPLETED).
  3. Giáo viên chọn một sinh viên có bài nộp.
  4. Hệ thống truy vấn và hiển thị bản nộp chính thức duy nhất của sinh viên đó.
  5. Hệ thống hiển thị mã nguồn đã nộp, thời điểm nộp, trigger_type (MANUAL hoặc AUTO_EXPIRED), kết quả Auto-Grader, AI Review và kết quả đối soát trùng lặp nếu đã chấm xong.
  6. Giáo viên xem xét bài nộp của sinh viên.
- **Luồng tương tác thay thế**:
  - 3a. Sinh viên chưa có bản nộp chính thức: Hệ thống hiển thị trạng thái sinh viên chưa nộp bài.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Sinh viên không tồn tại: Hệ thống thông báo "Không tìm thấy sinh viên."
  - E3 - Lỗi tải dữ liệu: Hệ thống thông báo "Không thể tải thông tin bài nộp."

---

### UC-29 — Xem điểm
- **Mô tả**: Cho phép Giáo viên xem bảng điểm và kết quả đánh giá của sinh viên trong lớp đối với các bài tập đã giao.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập và có quyền phụ trách lớp học.
- **Hậu điều kiện**: Bảng điểm của lớp được hiển thị; dữ liệu trong hệ thống không bị thay đổi.
- **Luồng tương tác chính**:
  1. Giáo viên chọn chức năng "Xem điểm".
  2. Hệ thống hiển thị danh sách các bài tập đã giao trong lớp phụ trách.
  3. Giáo viên chọn bài tập cần xem điểm.
  4. Hệ thống hiển thị danh sách sinh viên trong lớp kèm điểm số: Điểm chính thức (sau khi Giáo viên xác nhận), điểm Auto-Grader tạm tính và trạng thái chấm bài.
  5. Giáo viên xem chi tiết điểm của từng sinh viên theo tiêu chí Rubric.
- **Luồng tương tác thay thế**:
  - 4a. Giáo viên lọc hoặc xuất bảng điểm: Hệ thống lọc theo tiêu chí hoặc xuất dữ liệu bảng điểm ra tệp.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy bài tập: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Chưa có kết quả chấm: Hệ thống hiển thị trạng thái đang chờ chấm.
  - E3 - Lỗi tải dữ liệu: Hệ thống thông báo "Không thể tải thông tin bảng điểm."

---

### UC-30 — Xem AI đánh giá
- **Mô tả**: Cho phép Giáo viên xem kết quả đánh giá tự động do AI Review thực hiện (phân tích lỗi, chất lượng code, độ phức tạp, đề xuất cải thiện) và kết quả đối soát trùng lặp mã nguồn để hỗ trợ chấm bài.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền quản lý bài tập và hệ thống đã hoàn tất Batch Grading (COMPLETED).
- **Hậu điều kiện**: Toàn bộ kết quả AI Review và thông tin đối soát trùng lặp được hiển thị để Giáo viên tham khảo; dữ liệu không bị thay đổi.
- **Luồng tương tác chính**:
  1. Giáo viên mở danh sách bài nộp của bài tập.
  2. Giáo viên chọn sinh viên cần xem đánh giá AI.
  3. Hệ thống hiển thị kết quả AI Review gồm: Đánh giá Code Quality, Code Style, độ phức tạp thuật toán (Complexity), phân tích lỗi test case và thông tin đối soát trùng lặp mã nguồn.
  4. Giáo viên xem xét thông tin đánh giá để chuẩn bị cho bước chấm thủ công.
- **Luồng tương tác thay thế**:
  - 3a. Giáo viên chuyển sang xem bài làm của sinh viên khác: Hệ thống tải dữ liệu đánh giá AI của sinh viên được chọn tiếp theo.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy bài nộp: Hệ thống thông báo "Không tìm thấy bài nộp."
  - E2 - Bài nộp chưa hoàn tất đánh giá: Hệ thống thông báo "Bài nộp chưa có kết quả đánh giá AI."
  - E3 - Lỗi tải dữ liệu: Hệ thống thông báo "Không thể tải kết quả đánh giá AI."

---

### UC-31 — Đánh giá / chấm bài thủ công
- **Mô tả**: Cho phép Giáo viên đánh giá mã nguồn theo Rubric, điều chỉnh điểm, nhập nhận xét và xác nhận điểm chính thức (Official Score) cho bài làm của sinh viên.
- **Tác nhân**: Giáo viên.
- **Tiền điều kiện**: Giáo viên đã đăng nhập, có quyền phụ trách lớp và bài nộp đã hoàn tất đánh giá tự động (COMPLETED).
- **Hậu điều kiện**: Điểm số và nhận xét của Giáo viên được lưu; điểm do Giáo viên xác nhận trở thành Điểm chính thức (Official Score) của bài tập. Kết quả Auto-Grader và AI được lưu giữ làm tài liệu tham khảo.
- **Luồng tương tác chính**:
  1. Giáo viên mở bài nộp của sinh viên cần chấm.
  2. Hệ thống hiển thị mã nguồn bản nộp cuối, kết quả Auto-Grader, AI Review, Rubric và thông tin đối soát trùng lặp.
  3. Giáo viên xem xét mã nguồn và đánh giá điểm theo từng tiêu chí trong Rubric.
  4. Giáo viên nhập/điều chỉnh điểm số cho từng tiêu chí.
  5. Giáo viên nhập nhận xét đánh giá dành cho sinh viên.
  6. Giáo viên chọn "Xác nhận điểm chính thức".
  7. Hệ thống kiểm tra tính hợp lệ của điểm số (nằm trong thang điểm quy định).
  8. Hệ thống lưu kết quả chấm, ghi nhận điểm Giáo viên thành Điểm chính thức (Official Score).
  9. Hệ thống thông báo "Chấm bài và xác nhận điểm chính thức thành công."
- **Luồng tương tác thay thế**:
  - 6a. Giáo viên chọn "Lưu tạm thời": Hệ thống lưu bản nháp kết quả chấm của Giáo viên nhưng chưa công bố thành Điểm chính thức.
- **Luồng tương tác ngoại lệ**:
  - E1 - Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập."
  - E2 - Điểm đánh giá không hợp lệ: Hệ thống thông báo "Điểm nhập vào vượt quá thang điểm quy định của tiêu chí."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Lưu kết quả chấm bài thất bại."

---

### UC-32 — Tạo tài khoản người dùng
- **Mô tả**: Cho phép Quản trị viên tạo tài khoản cho Sinh viên, Giáo viên hoặc Giáo vụ để sử dụng hệ thống.
- **Tác nhân**: Quản trị viên.
- **Tiền điều kiện**: Quản trị viên đã đăng nhập và có quyền quản lý tài khoản người dùng.
- **Hậu điều kiện**: Tài khoản được tạo thành công, gán đúng vai trò, mật khẩu tạm được sinh và gửi qua email, đánh dấu bắt buộc đổi mật khẩu ở lần đăng nhập đầu tiên.
- **Luồng tương tác chính**:
  1. Quản trị viên chọn chức năng "Quản lý tài khoản".
  2. Hệ thống hiển thị danh sách tài khoản người dùng.
  3. Quản trị viên chọn "Tạo tài khoản".
  4. Hệ thống hiển thị biểu mẫu yêu cầu: Họ tên, Email, Vai trò (Sinh viên, Giáo viên, Giáo vụ).
  5. Quản trị viên nhập thông tin và chọn vai trò phù hợp.
  6. Quản trị viên chọn "Tạo tài khoản".
  7. Hệ thống kiểm tra tính hợp lệ của dữ liệu và tính duy nhất của Email.
  8. Hệ thống tạo tài khoản, sinh mật khẩu tạm ngẫu nhiên, đánh dấu bắt buộc đổi mật khẩu và gửi email thông báo.
  9. Hệ thống lưu tài khoản vào cơ sở dữ liệu và thông báo "Tạo tài khoản thành công."
- **Luồng tương tác thay thế**:
  - 6a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác và quay lại danh sách tài khoản.
- **Luồng tương tác ngoại lệ**:
  - E1 - Dữ liệu không hợp lệ: Hệ thống thông báo "Thông tin tài khoản không hợp lệ."
  - E2 - Email đã tồn tại: Hệ thống thông báo "Địa chỉ email đã được sử dụng."
  - E3 - Lỗi tạo tài khoản: Hệ thống thông báo "Tạo tài khoản thất bại, vui lòng thử lại sau."

---

### UC-33 — Khóa / mở tài khoản
- **Mô tả**: Cho phép Quản trị viên khóa hoặc mở khóa tài khoản Sinh viên, Giáo viên, Giáo vụ. Khi khóa, hệ thống thu hồi toàn bộ phiên đăng nhập hiện tại.
- **Tác nhân**: Quản trị viên.
- **Tiền điều kiện**: Quản trị viên đã đăng nhập và có quyền quản lý tài khoản người dùng.
- **Hậu điều kiện**: Trạng thái tài khoản được cập nhật. Tài khoản bị khóa sẽ bị vô hiệu hóa phiên đăng nhập hiện tại và không thể đăng nhập tiếp.
- **Luồng tương tác chính**:
  1. Quản trị viên chọn chức năng "Quản lý tài khoản".
  2. Hệ thống hiển thị danh sách người dùng.
  3. Quản trị viên chọn tài khoản cần thay đổi trạng thái.
  4. Quản trị viên chọn "Khóa tài khoản" hoặc "Mở khóa tài khoản".
  5. Hệ thống hiển thị hộp thoại xác nhận thao tác.
  6. Quản trị viên xác nhận.
  7. Hệ thống cập nhật trạng thái tài khoản trong cơ sở dữ liệu.
  8. Nếu là thao tác Khóa, hệ thống lập tức thu hồi và vô hiệu hóa các active sessions/token của tài khoản.
  9. Hệ thống thông báo "Cập nhật trạng thái tài khoản thành công."
- **Luồng tương tác thay thế**:
  - 6a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên trạng thái tài khoản.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy tài khoản: Hệ thống thông báo "Không tìm thấy tài khoản."
  - E2 - Lỗi cập nhật dữ liệu: Hệ thống thông báo "Cập nhật trạng thái thất bại."

---

### UC-34 — Xóa tài khoản
- **Mô tả**: Cho phép Quản trị viên xóa tài khoản người dùng; áp dụng cơ chế Soft Delete nếu tài khoản đã có dữ liệu học tập liên quan.
- **Tác nhân**: Quản trị viên.
- **Tiền điều kiện**: Quản trị viên đã đăng nhập và tài khoản cần xóa tồn tại trong hệ thống.
- **Hậu điều kiện**: Tài khoản bị vô hiệu hóa hoặc xóa mềm (Soft Delete) để bảo toàn tính toàn vẹn dữ liệu học tập (bài nộp, điểm số, lịch sử).
- **Luồng tương tác chính**:
  1. Quản trị viên chọn tài khoản cần xóa từ danh sách người dùng.
  2. Quản trị viên chọn "Xóa tài khoản".
  3. Hệ thống hiển thị cảnh báo về việc xóa và dữ liệu liên quan.
  4. Quản trị viên xác nhận xóa.
  5. Hệ thống kiểm tra dữ liệu học tập liên quan (bài nộp, điểm, lớp học).
  6. Hệ thống thực hiện Soft Delete (vô hiệu hóa tài khoản, bảo lưu dữ liệu học tập).
  7. Hệ thống thu hồi phiên làm việc hiện tại của tài khoản.
  8. Hệ thống thông báo "Xóa tài khoản thành công."
- **Luồng tương tác thay thế**:
  - 4a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác xóa.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy tài khoản: Hệ thống thông báo "Không tìm thấy tài khoản."
  - E2 - Lỗi hệ thống: Hệ thống thông báo "Không thể xóa tài khoản, vui lòng thử lại sau."

---

### UC-35 — Phân quyền người dùng
- **Mô tả**: Quản trị viên phân quyền các vai trò nghiệp vụ (Sinh viên, Giáo viên, Giáo vụ). Quản trị viên hệ thống quản lý các vai trò quản trị cấp hệ thống (Quản trị viên, Quản trị viên hệ thống).
- **Tác nhân**: Quản trị viên, Quản trị viên hệ thống.
- **Tiền điều kiện**: Người dùng đã đăng nhập và có quyền phân quyền trong phạm vi của mình. Người thực hiện không được tự cấp quyền vượt quá phạm vi được giao.
- **Hậu điều kiện**: Vai trò và quyền hạn của tài khoản được cập nhật và lưu vào cơ sở dữ liệu.
- **Luồng tương tác chính**:
  1. Người dùng truy cập chức năng "Phân quyền người dùng".
  2. Hệ thống hiển thị danh sách tài khoản.
  3. Người dùng chọn tài khoản cần phân quyền.
  4. Hệ thống hiển thị danh sách các vai trò/quyền mà người thực hiện được phép cấp.
  5. Người dùng chọn vai trò hoặc quyền cần cập nhật.
  6. Người dùng chọn "Lưu phân quyền".
  7. Hệ thống kiểm tra quyền của người thực hiện và tính hợp lệ của phân quyền.
  8. Hệ thống cập nhật quyền của tài khoản vào cơ sở dữ liệu.
  9. Hệ thống thông báo "Phân quyền người dùng thành công."
- **Luồng tương tác thay thế**:
  - 6a. Người dùng chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên quyền hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Cấp quyền vượt quá phạm vi cho phép: Hệ thống thông báo "Bạn không có quyền cấp vai trò hoặc quyền này."
  - E2 - Không tìm thấy tài khoản: Hệ thống thông báo "Không tìm thấy tài khoản."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Phân quyền thất bại."

---

### UC-36 — Đặt lại mật khẩu
- **Mô tả**: Cho phép Quản trị viên reset mật khẩu cho tài khoản người dùng khi có yêu cầu hỗ trợ.
- **Tác nhân**: Quản trị viên.
- **Tiền điều kiện**: Quản trị viên đã đăng nhập và có quyền quản lý tài khoản người dùng.
- **Hậu điều kiện**: Hệ thống tự sinh mật khẩu tạm mới, lưu dưới dạng băm, gửi email cho người dùng, đánh dấu bắt buộc đổi mật khẩu và thu hồi các phiên đăng nhập hiện tại.
- **Luồng tương tác chính**:
  1. Quản trị viên chọn tài khoản cần reset mật khẩu.
  2. Quản trị viên chọn "Đặt lại mật khẩu".
  3. Hệ thống hiển thị hộp thoại xác nhận.
  4. Quản trị viên xác nhận thao tác.
  5. Hệ thống tự động sinh mật khẩu tạm thời ngẫu nhiên.
  6. Hệ thống băm mật khẩu tạm và cập nhật vào cơ sở dữ liệu.
  7. Hệ thống đánh dấu tài khoản bắt buộc phải đổi mật khẩu ở lần đăng nhập tới.
  8. Hệ thống gửi email chứa mật khẩu tạm đến địa chỉ email của người dùng.
  9. Hệ thống thu hồi toàn bộ active sessions hiện tại của tài khoản.
  10. Hệ thống thông báo "Đặt lại mật khẩu thành công."
- **Luồng tương tác thay thế**:
  - 4a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên mật khẩu cũ.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy tài khoản: Hệ thống thông báo "Không tìm thấy tài khoản."
  - E2 - Lỗi gửi email: Hệ thống thông báo "Không thể gửi email mật khẩu tạm, vui lòng thử lại sau."
  - E3 - Lỗi cập nhật: Hệ thống thông báo "Đặt lại mật khẩu thất bại."

---

### UC-37 — Nhập danh sách từ Excel/CSV
- **Mô tả**: Cho phép Quản trị viên nhập danh sách người dùng hàng loạt từ tệp Excel hoặc CSV với đúng 5 cột quy định.
- **Tác nhân**: Quản trị viên.
- **Tiền điều kiện**: Quản trị viên đã đăng nhập và tệp dữ liệu đã được chuẩn bị đúng cấu trúc 5 cột (Mã người dùng, Họ tên, Email, Vai trò, Lớp). Không có cột mật khẩu.
- **Hậu điều kiện**: Các bản ghi hợp lệ được tạo tài khoản trong hệ thống; hệ thống hiển thị chi tiết kết quả và danh sách lỗi cho các bản ghi không hợp lệ.
- **Luồng tương tác chính**:
  1. Quản trị viên chọn chức năng "Nhập danh sách từ Excel/CSV".
  2. Hệ thống hiển thị giao diện tải tệp kèm mô tả cấu trúc mẫu 5 cột.
  3. Quản trị viên chọn và tải lên tệp Excel/CSV.
  4. Hệ thống kiểm tra định dạng và cấu trúc cột của tệp.
  5. Hệ thống đọc và kiểm tra tính hợp lệ của từng dòng dữ liệu (định dạng email, vai trò hợp lệ, trùng lặp).
  6. Hệ thống hiển thị bảng xem trước (preview) gồm số bản ghi hợp lệ và danh sách bản ghi lỗi kèm lý do.
  7. Quản trị viên xác nhận thực hiện Import.
  8. Hệ thống tạo tài khoản cho các bản ghi hợp lệ, sinh mật khẩu tạm và gửi email thông báo.
  9. Hệ thống thông báo kết quả nhập dữ liệu thành công.
- **Luồng tương tác thay thế**:
  - 7a. Tệp có tài khoản đã tồn tại: Hệ thống cập nhật họ tên; giữ nguyên email, vai trò và không đổi mật khẩu qua file import.
  - 7b. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác và không lưu dữ liệu.
- **Luồng tương tác ngoại lệ**:
  - E1 - Tệp sai định dạng/cấu trúc cột: Hệ thống thông báo "Cấu trúc tệp không hợp lệ, yêu cầu đúng 5 cột quy định."
  - E2 - Tệp rỗng: Hệ thống thông báo "Tệp không chứa dữ liệu."
  - E3 - Không có bản ghi nào hợp lệ: Hệ thống thông báo "Không có dữ liệu hợp lệ để nhập."

---

### UC-38 — Tạo lớp (Cấp Quản trị viên / Giáo vụ)
- **Mô tả**: Quản trị viên tạo lớp học trong phạm vi toàn trường; Giáo vụ tạo lớp học trong phạm vi Khoa/Bộ môn được phân công phụ trách.
- **Tác nhân**: Quản trị viên, Giáo vụ.
- **Tiền điều kiện**: Người dùng đã đăng nhập với vai trò Quản trị viên (toàn trường) hoặc Giáo vụ (trong phạm vi Khoa/Bộ môn được phân công).
- **Hậu điều kiện**: Lớp học mới được tạo thành công ở trạng thái Hoạt động và lưu vào cơ sở dữ liệu.
- **Luồng tương tác chính**:
  1. Người dùng chọn chức năng "Quản lý lớp".
  2. Hệ thống hiển thị danh sách lớp theo phạm vi quyền (Quản trị viên thấy toàn trường; Giáo vụ chỉ thấy lớp thuộc Khoa/Bộ môn phụ trách).
  3. Người dùng chọn "Tạo lớp".
  4. Hệ thống hiển thị biểu mẫu tạo lớp: Tên lớp, mã lớp, mô tả, niên khóa, Khoa/Bộ môn (nếu là Giáo vụ thì tự động gán Khoa/Bộ môn phụ trách).
  5. Người dùng nhập thông tin và chọn "Lưu lớp".
  6. Hệ thống kiểm tra tính hợp lệ của thông tin, tính duy nhất của mã lớp và phạm vi quyền.
  7. Hệ thống tạo lớp mới ở trạng thái "Hoạt động".
  8. Hệ thống thông báo "Tạo lớp thành công."
- **Luồng tương tác thay thế**:
  - 5a. Người dùng chọn "Hủy": Hệ thống hủy thao tác tạo lớp.
- **Luồng tương tác ngoại lệ**:
  - E1 - Dữ liệu không hợp lệ: Hệ thống thông báo "Thông tin lớp học không hợp lệ."
  - E2 - Mã lớp đã tồn tại: Hệ thống thông báo "Mã lớp đã tồn tại."
  - E3 - Giáo vụ thao tác ngoài phạm vi: Hệ thống thông báo "Bạn không có quyền tạo lớp ngoài Khoa/Bộ môn được phân công."
  - E4 - Lỗi lưu dữ liệu: Hệ thống thông báo "Tạo lớp thất bại."

---

### UC-39 — Chỉnh sửa lớp (Cấp Quản trị viên / Giáo vụ)
- **Mô tả**: Quản trị viên chỉnh sửa lớp trên toàn trường; Giáo vụ chỉnh sửa lớp thuộc Khoa/Bộ môn được phân công phụ trách (lớp đang ở trạng thái Hoạt động).
- **Tác nhân**: Quản trị viên, Giáo vụ.
- **Tiền điều kiện**: Người dùng đã đăng nhập đúng phạm vi quyền và lớp đang ở trạng thái Hoạt động.
- **Hậu điều kiện**: Thông tin lớp học được cập nhật thành công trong cơ sở dữ liệu.
- **Luồng tương tác chính**:
  1. Người dùng chọn lớp cần chỉnh sửa trong danh sách quản lý.
  2. Hệ thống kiểm tra phạm vi quyền và hiển thị thông tin hiện tại của lớp.
  3. Người dùng chỉnh sửa tên lớp, mô tả, niên khóa.
  4. Người dùng chọn "Lưu thay đổi".
  5. Hệ thống kiểm tra tính hợp lệ của dữ liệu.
  6. Hệ thống cập nhật thông tin lớp vào cơ sở dữ liệu.
  7. Hệ thống thông báo "Chỉnh sửa lớp thành công."
- **Luồng tương tác thay thế**:
  - 4a. Người dùng chọn "Hủy": Hệ thống hủy thay đổi và giữ nguyên dữ liệu lớp.
- **Luồng tương tác ngoại lệ**:
  - E1 - Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp học."
  - E2 - Lớp không ở trạng thái Hoạt động: Hệ thống thông báo "Chỉ chỉnh sửa được lớp đang ở trạng thái Hoạt động."
  - E3 - Giáo vụ thao tác ngoài phạm vi: Hệ thống thông báo "Bạn không có quyền chỉnh sửa lớp thuộc Khoa/Bộ môn khác."
  - E4 - Lỗi lưu dữ liệu: Hệ thống thông báo "Chỉnh sửa lớp thất bại."

---

### UC-40 — Đóng / Mở lại lớp học
- **Mô tả**: Cho phép Giáo viên (lớp phụ trách), Giáo vụ (Khoa/Bộ môn phụ trách), Quản trị viên (toàn trường) chuyển đổi trạng thái lớp giữa Hoạt động và Đã đóng.
- **Tác nhân**: Giáo viên, Giáo vụ, Quản trị viên. *(Không có Quản trị viên hệ thống).*
- **Tiền điều kiện**: Người dùng đã đăng nhập và có quyền đối với lớp học. Lớp tồn tại trong hệ thống.
- **Hậu điều kiện**: Trạng thái lớp chuyển thành "Đã đóng" (khi đóng lớp) hoặc "Hoạt động" (khi mở lại). Khi lớp đã đóng, sinh viên bị ngăn các hoạt động học tập mới nhưng dữ liệu được bảo toàn.
- **Luồng tương tác chính**:
  1. Người dùng chọn lớp cần thay đổi trạng thái từ danh sách quản lý.
  2. Hệ thống hiển thị thông tin và trạng thái hiện tại của lớp (Hoạt động hoặc Đã đóng).
  3. Người dùng chọn thao tác "Đóng lớp" (nếu lớp đang Hoạt động) hoặc "Mở lại lớp" (nếu lớp đang Đã đóng).
  4. Hệ thống hiển thị hộp thoại yêu cầu xác nhận.
  5. Người dùng xác nhận thao tác.
  6. Hệ thống kiểm tra phạm vi quyền và cập nhật trạng thái lớp (Hoạt động $\leftrightarrow$ Đã đóng).
  7. Hệ thống thông báo "Cập nhật trạng thái lớp thành công."
- **Luồng tương tác thay thế**:
  - 5a. Người dùng chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên trạng thái hiện tại của lớp.
- **Luồng tương tác ngoại lệ**:
  - E1 - Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp học."
  - E2 - Lớp không ở trạng thái phù hợp: Hệ thống thông báo "Lớp không ở trạng thái phù hợp để thực hiện thao tác này."
  - E3 - Người dùng không có quyền: Hệ thống từ chối yêu cầu.
  - E4 - Lỗi cập nhật: Hệ thống thông báo "Không thể cập nhật trạng thái lớp, vui lòng thử lại sau."

---

### UC-41 — Quản lý Lưu trữ & Xóa lớp học
- **Mô tả**: Quản trị viên (toàn trường) và Giáo vụ (Khoa/Bộ môn) thực hiện Archive (Lưu trữ), Restore (Khôi phục) và Hard Delete (Xóa vĩnh viễn) lớp học theo quy tắc nghiệp vụ nghiêm ngặt.
- **Tác nhân**: Quản trị viên, Giáo vụ. *(Không có Quản trị viên hệ thống).*
- **Tiền điều kiện**: Người dùng đã đăng nhập với vai trò Quản trị viên hoặc Giáo vụ trong phạm vi phụ trách.
- **Hậu điều kiện**: Lớp được chuyển sang trạng thái "Lưu trữ" (khi Archive); lớp được khôi phục về trạng thái "Đã đóng" (khi Restore); hoặc lớp bị xóa hoàn toàn khỏi cơ sở dữ liệu nếu thỏa mãn điều kiện Hard Delete (0 Sinh viên và 0 bài tập).
- **Luồng tương tác chính**:
  1. Người dùng chọn chức năng quản lý vòng đời lớp học.
  2. Hệ thống hiển thị danh sách lớp theo phạm vi quyền.
  3. Người dùng chọn lớp cần xử lý.
  4. Người dùng chọn một trong các thao tác: "Lưu trữ lớp" (Archive), "Khôi phục lớp" (Restore), hoặc "Xóa vĩnh viễn" (Hard Delete).
  5. Hệ thống hiển thị hộp thoại xác nhận và kiểm tra điều kiện.
  6. Người dùng xác nhận thao tác.
  7. Hệ thống thực hiện xử lý theo quy tắc nghiệp vụ:
     - Archive: Chuyển lớp từ "Đã đóng" sang "Lưu trữ", ẩn khỏi danh sách vận hành thông thường.
     - Restore: Chuyển lớp từ "Lưu trữ" về "Đã đóng" (không tự động mở thành Hoạt động).
     - Hard Delete: Kiểm tra đồng thời student_count = 0 AND assignment_count = 0. Nếu đủ điều kiện, hệ thống xóa hoàn toàn bản ghi lớp. Nếu không đủ điều kiện, hệ thống chặn Hard Delete và tự động chuyển sang Archive.
  8. Hệ thống thông báo kết quả xử lý thành công.
- **Luồng tương tác thay thế**:
  - 6a. Người dùng chọn "Hủy": Hệ thống đóng hộp thoại và giữ nguyên trạng thái lớp.
  - 7a. Thao tác Hard Delete bị chặn do có dữ liệu: Hệ thống thông báo "Lớp đã phát sinh dữ liệu học vụ, hệ thống chuyển lớp sang trạng thái Lưu trữ để bảo toàn dữ liệu." và thực hiện Archive.
- **Luồng tương tác ngoại lệ**:
  - E1 - Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp học."
  - E2 - Thao tác không hợp lệ với trạng thái lớp: Hệ thống thông báo lỗi trạng thái.
  - E3 - Giáo vụ thao tác ngoài phạm vi: Hệ thống thông báo "Bạn không có quyền thao tác trên lớp thuộc Khoa/Bộ môn khác."
  - E4 - Lỗi hệ thống: Hệ thống thông báo "Thao tác thất bại, vui lòng thử lại sau."

---

### UC-42 — Quản lý sinh viên trong lớp (Cấp Quản trị viên / Giáo vụ)
- **Mô tả**: Quản trị viên (toàn trường) và Giáo vụ (Khoa/Bộ môn) quản lý danh sách sinh viên trong lớp (thêm, xóa, thêm/xóa hàng loạt, xem thông tin sinh viên).
- **Tác nhân**: Quản trị viên, Giáo vụ.
- **Tiền điều kiện**: Người dùng đã đăng nhập đúng phạm vi quyền và lớp đang ở trạng thái Hoạt động.
- **Hậu điều kiện**: Danh sách sinh viên thuộc lớp được cập nhật chính xác trong cơ sở dữ liệu.
- **Luồng tương tác chính**:
  1. Người dùng chọn lớp cần quản lý sinh viên từ danh sách lớp.
  2. Hệ thống hiển thị danh sách sinh viên hiện tại của lớp.
  3. Người dùng chọn chức năng "Thêm sinh viên" hoặc "Xóa sinh viên".
  4. Người dùng chọn hoặc nhập thông tin sinh viên (hỗ trợ chọn một hoặc nhiều sinh viên).
  5. Người dùng xác nhận thao tác.
  6. Hệ thống kiểm tra tài khoản sinh viên tồn tại, trạng thái thuộc lớp và quyền của người thực hiện.
  7. Hệ thống cập nhật danh sách sinh viên trong lớp.
  8. Hệ thống thông báo "Cập nhật danh sách sinh viên thành công."
- **Luồng tương tác thay thế**:
  - 5a. Người dùng chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên danh sách sinh viên.
- **Luồng tương tác ngoại lệ**:
  - E1 - Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp."
  - E2 - Sinh viên không tồn tại: Hệ thống thông báo "Không tìm thấy sinh viên."
  - E3 - Sinh viên đã có trong lớp: Hệ thống thông báo "Sinh viên đã thuộc lớp này."
  - E4 - Lớp không ở trạng thái Hoạt động: Hệ thống thông báo "Không thể thay đổi thành viên của lớp không hoạt động."
  - E5 - Giáo vụ thao tác ngoài phạm vi: Hệ thống thông báo "Bạn không có quyền quản lý sinh viên của lớp thuộc Khoa/Bộ môn khác."

---

### UC-43 — Phân công Giáo viên vào lớp
- **Mô tả**: Quản trị viên (toàn trường) và Giáo vụ (Khoa/Bộ môn) phân công một hoặc nhiều Giáo viên phụ trách giảng dạy cho lớp học.
- **Tác nhân**: Quản trị viên, Giáo vụ. *(Không có Quản trị viên hệ thống).*
- **Tiền điều kiện**: Người dùng đã đăng nhập đúng phạm vi quyền, lớp học đang ở trạng thái Hoạt động và Giáo viên tồn tại trong hệ thống.
- **Hậu điều kiện**: Thông tin phân công Giáo viên phụ trách lớp được lưu thành công trong cơ sở dữ liệu.
- **Luồng tương tác chính**:
  1. Người dùng chọn lớp cần phân công Giáo viên.
  2. Hệ thống hiển thị thông tin lớp và danh sách Giáo viên đang phụ trách hiện tại.
  3. Người dùng chọn chức năng "Phân công Giáo viên".
  4. Hệ thống hiển thị danh sách Giáo viên có thể phân công.
  5. Người dùng chọn một hoặc nhiều Giáo viên và chọn "Xác nhận phân công".
  6. Hệ thống kiểm tra tính hợp lệ của thông tin và phạm vi quyền của người thực hiện.
  7. Hệ thống lưu thông tin phân công Giáo viên vào cơ sở dữ liệu.
  8. Hệ thống thông báo "Phân công Giáo viên thành công."
- **Luồng tương tác thay thế**:
  - 5a. Người dùng hủy phân công Giáo viên hiện tại: Người dùng chọn Giáo viên cần hủy, xác nhận và hệ thống cập nhật gỡ bỏ phân công.
  - 5b. Người dùng chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên danh sách hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy lớp: Hệ thống thông báo "Không tìm thấy lớp học."
  - E2 - Không tìm thấy Giáo viên: Hệ thống thông báo "Không tìm thấy Giáo viên."
  - E3 - Giáo vụ thao tác ngoài phạm vi: Hệ thống thông báo "Bạn không có quyền phân công Giáo viên cho lớp thuộc Khoa/Bộ môn khác."
  - E4 - Lỗi lưu dữ liệu: Hệ thống thông báo "Phân công Giáo viên thất bại."

---

### UC-44 — Quản lý cấu hình AI
- **Mô tả**: Cho phép Quản trị viên hệ thống quản lý cấu hình các mô hình AI, API Key, endpoint và các tham số kỹ thuật phục vụ AI Review và AI Tutor.
- **Tác nhân**: Quản trị viên hệ thống.
- **Tiền điều kiện**: Quản trị viên hệ thống đã đăng nhập và có quyền quản trị kỹ thuật hệ thống.
- **Hậu điều kiện**: Cấu hình AI được cập nhật và kích hoạt an toàn trong hệ thống.
- **Luồng tương tác chính**:
  1. Quản trị viên hệ thống chọn chức năng "Quản lý cấu hình AI".
  2. Hệ thống hiển thị danh sách các cấu hình AI hiện có.
  3. Quản trị viên hệ thống chọn cấu hình cần chỉnh sửa hoặc tạo cấu hình mới.
  4. Quản trị viên hệ thống nhập/điều chỉnh các thông số: API Key, Provider, Model, Temperature, Max Tokens, Timeout.
  5. Quản trị viên hệ thống chọn chức năng "Kiểm tra kết nối" (Test Connection).
  6. Hệ thống thực hiện kiểm tra kết nối đến AI Service và hiển thị kết quả kiểm tra.
  7. Quản trị viên hệ thống chọn "Lưu cấu hình".
  8. Hệ thống lưu và kích hoạt cấu hình AI vào cơ sở dữ liệu.
  9. Hệ thống thông báo "Cập nhật cấu hình AI thành công."
- **Luồng tương tác thay thế**:
  - 4a. Quản trị viên hệ thống chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên cấu hình hiện tại.
  - 7a. Kích hoạt/Vô hiệu hóa cấu hình: Quản trị viên hệ thống chuyển đổi trạng thái hoạt động của cấu hình.
- **Luồng tương tác ngoại lệ**:
  - E1 - Thông số cấu hình không hợp lệ: Hệ thống thông báo "Thông số cấu hình AI không hợp lệ."
  - E2 - Kết nối đến dịch vụ AI thất bại: Hệ thống thông báo "Kiểm tra kết nối thất bại, vui lòng kiểm tra lại API Key hoặc endpoint."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Cập nhật cấu hình AI thất bại."

---

### UC-45 — Cấu hình Docker Sandbox
- **Mô tả**: Cho phép Quản trị viên hệ thống thiết lập và điều chỉnh các thông số môi trường Docker Sandbox dùng để thực thi mã nguồn cách ly an toàn.
- **Tác nhân**: Quản trị viên hệ thống.
- **Tiền điều kiện**: Quản trị viên hệ thống đã đăng nhập và dịch vụ Docker Sandbox đã tích hợp vào hệ thống.
- **Hậu điều kiện**: Các thông số cấu hình Docker Sandbox (giới hạn CPU, RAM, Execution Timeout, Base Images) được lưu và áp dụng cho các phiên thực thi mới.
- **Luồng tương tác chính**:
  1. Quản trị viên hệ thống chọn chức năng "Cấu hình Docker Sandbox".
  2. Hệ thống hiển thị các thông số cấu hình hiện tại: Base Images theo ngôn ngữ, CPU Limit, Memory Limit mặc định, Network Isolation, Execution Timeout.
  3. Quản trị viên hệ thống nhập hoặc chỉnh sửa các thông số cấu hình.
  4. Quản trị viên hệ thống chọn chức năng "Kiểm tra cấu hình".
  5. Hệ thống kiểm tra kết nối Docker daemon và khả năng khởi tạo container mẫu.
  6. Quản trị viên hệ thống chọn "Lưu cấu hình".
  7. Hệ thống lưu cấu hình vào cơ sở dữ liệu và áp dụng cho Docker Sandbox.
  8. Hệ thống thông báo "Cấu hình Docker Sandbox thành công."
- **Luồng tương tác thay thế**:
  - 3a. Quản trị viên hệ thống chọn "Khôi phục mặc định": Hệ thống nạp lại các thông số mặc định an toàn.
  - 6a. Quản trị viên hệ thống chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên cấu hình hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Thông số vượt quá giới hạn an toàn: Hệ thống thông báo "Thông số cấu hình vượt quá giới hạn cho phép."
  - E2 - Không thể kết nối Docker daemon: Hệ thống thông báo "Không thể kết nối đến Docker service."
  - E3 - Lỗi lưu cấu hình: Hệ thống thông báo "Cấu hình Docker Sandbox thất bại."

---

### UC-46 — Giám sát Docker Sandbox
- **Mô tả**: Cho phép Quản trị viên hệ thống giám sát trạng thái hoạt động, mức sử dụng tài nguyên (CPU, RAM) và theo dõi các container thực thi trong quá trình Batch Grading.
- **Tác nhân**: Quản trị viên hệ thống.
- **Tiền điều kiện**: Quản trị viên hệ thống đã đăng nhập và có quyền giám sát hệ thống.
- **Hậu điều kiện**: Trạng thái và thông số hoạt động của Docker Sandbox được hiển thị realtime; các sự cố hoặc lỗi được ghi nhận vào nhật ký.
- **Luồng tương tác chính**:
  1. Quản trị viên hệ thống chọn chức năng "Giám sát Docker Sandbox".
  2. Hệ thống kiểm tra và hiển thị trạng thái hoạt động của Docker Sandbox.
  3. Hệ thống hiển thị danh sách các container đang thực thi, hàng đợi Message Queue và mức sử dụng tài nguyên (CPU, RAM, số container active).
  4. Quản trị viên hệ thống theo dõi realtime tình trạng thực thi mã nguồn.
  5. Quản trị viên hệ thống xem chi tiết một phiên thực thi hoặc nhật ký lỗi phát sinh.
- **Luồng tương tác thay thế**:
  - 5a. Dừng khẩn cấp phiên thực thi bị kẹt: Quản trị viên hệ thống chọn dừng container bị treo, hệ thống giải phóng tài nguyên và ghi nhận sự kiện vào System Logs.
- **Luồng tương tác ngoại lệ**:
  - E1 - Docker Sandbox không khả dụng: Hệ thống thông báo "Dịch vụ Docker Sandbox hiện không phản hồi."
  - E2 - Lỗi tải dữ liệu giám sát: Hệ thống thông báo "Không thể tải thông tin giám sát, vui lòng thử lại sau."

---

### UC-47 — Quản lý tổ chức
- **Mô tả**: Cho phép Quản trị viên quản lý thông tin tổ chức, cơ cấu Khoa/Bộ môn trực thuộc và phân công Giáo vụ phụ trách từng Khoa/Bộ môn.
- **Tác nhân**: Quản trị viên. *(Quản trị viên hệ thống KHÔNG tham gia).*
- **Tiền điều kiện**: Quản trị viên đã đăng nhập và có quyền quản lý cơ cấu tổ chức đào tạo.
- **Hậu điều kiện**: Thông tin tổ chức, Khoa/Bộ môn được cập nhật và Giáo vụ được gán đúng Khoa/Bộ môn phụ trách (1 Giáo vụ có thể phụ trách một hoặc nhiều Khoa/Bộ môn).
- **Luồng tương tác chính**:
  1. Quản trị viên chọn chức năng "Quản lý tổ chức".
  2. Hệ thống hiển thị danh sách tổ chức và cơ cấu Khoa/Bộ môn trực thuộc.
  3. Quản trị viên chọn thao tác: Tạo mới tổ chức, Tạo Khoa/Bộ môn, Chỉnh sửa, Khóa/mở khóa, Xóa, hoặc Phân công Giáo vụ.
  4. Hệ thống hiển thị biểu mẫu hoặc yêu cầu xác nhận tương ứng.
  5. Quản trị viên nhập thông tin hoặc phân công Giáo vụ phụ trách Khoa/Bộ môn.
  6. Quản trị viên chọn "Lưu thay đổi".
  7. Hệ thống kiểm tra tính hợp lệ của dữ liệu và lưu vào cơ sở dữ liệu.
  8. Hệ thống thông báo "Thao tác quản lý tổ chức thành công."
- **Luồng tương tác thay thế**:
  - 3a. Quản trị viên phân công Giáo vụ phụ trách: Quản trị viên chọn tài khoản Giáo vụ và gán vào một hoặc nhiều Khoa/Bộ môn phụ trách; hệ thống lưu thông tin phân công.
  - 6a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên dữ liệu hiện tại.
- **Luồng tương tác ngoại lệ**:
  - E1 - Tên tổ chức hoặc Khoa/Bộ môn đã tồn tại: Hệ thống thông báo "Tên đã tồn tại."
  - E2 - Có dữ liệu liên quan khi xóa: Hệ thống thông báo "Đang có dữ liệu lớp/người dùng liên quan, không thể xóa trực tiếp."
  - E3 - Lỗi lưu dữ liệu: Hệ thống thông báo "Thao tác quản lý tổ chức thất bại."

---

### UC-48 — Quản lý System Logs
- **Mô tả**: Cho phép Quản trị viên hệ thống xem, tìm kiếm, lọc và xuất nhật ký hoạt động của toàn hệ thống (System Logs) nhằm phục vụ giám sát, audit và xử lý sự cố.
- **Tác nhân**: Quản trị viên hệ thống.
- **Tiền điều kiện**: Quản trị viên hệ thống đã đăng nhập và có quyền quản trị hệ thống.
- **Hậu điều kiện**: Nhật ký hệ thống được hiển thị và trích xuất theo nhu cầu; dữ liệu log không bị thay đổi.
- **Luồng tương tác chính**:
  1. Quản trị viên hệ thống chọn chức năng "Quản lý System Logs".
  2. Hệ thống hiển thị danh sách System Logs gồm: Thời gian, Actor/User, Action, Loại sự kiện (Info/Warn/Error), Module và Trạng thái.
  3. Quản trị viên hệ thống tìm kiếm hoặc lọc log theo khoảng thời gian, loại sự kiện hoặc từ khóa.
  4. Hệ thống hiển thị danh sách System Logs phù hợp với bộ lọc.
  5. Quản trị viên hệ thống chọn một bản ghi log để xem chi tiết thông tin.
  6. Quản trị viên hệ thống có thể chọn chức năng "Xuất Logs" để tải tệp nhật ký về máy.
- **Luồng tương tác thay thế**:
  - 6a. Quản trị viên hệ thống xuất dữ liệu: Hệ thống tạo tệp log theo khoảng thời gian được chọn và tải về máy.
- **Luồng tương tác ngoại lệ**:
  - E1 - Không tìm thấy log phù hợp: Hệ thống hiển thị danh sách trống.
  - E2 - Lỗi truy vấn dữ liệu: Hệ thống thông báo "Không thể tải System Logs, vui lòng thử lại sau."
  - E3 - Lỗi xuất tệp: Hệ thống thông báo "Xuất System Logs thất bại."

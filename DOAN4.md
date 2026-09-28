# TÀI LIỆU ĐẶC TẢ USE CASE HỆ THỐNG AI CODING TUTOR

> # 📢 BẢNG TỔNG HỢP CÁC ĐIỂM ĐÃ SỬA VÀ CHUẨN HÓA (CHANGELOG)
> 
> | Nhóm lỗi | Use Case liên quan | Chi tiết nội dung đã sửa |
> | :--- | :--- | :--- |
> | 🔴 **Lỗi nghiêm trọng (Nội dung copy nhầm)** | **UC-38 (Tạo lớp - Quản trị viên)** | **Viết lại 100% luồng chính**; xóa bỏ toàn bộ nội dung "Quản lý đề thi" bị copy nhầm, thay bằng luồng tạo lớp chuẩn và liên kết phân công giảng viên. |
> | 🔴 **Lỗi mâu thuẫn logic nộp muộn** | **UC-08 & UC-11** | Cho phép xem đề và nộp bài khi quá hạn nếu bài tập cho phép nộp muộn (kèm phạt điểm); chỉ chặn khi bài tập bị khóa hoàn toàn. |
> | 🔴 **Lỗi mâu thuẫn giao bài** | **UC-27** | Sửa xung đột E4 và luồng 1c: Luồng chính giao bài mới, luồng 3a cho phép cập nhật/gia hạn cho lớp đã giao. |
> | 🔴 **Lỗi quan hệ tạo & cấu hình bài tập** | **UC-21 & UC-24, 25, 26** | Làm rõ UC-21 là tạo bài tập tổng thể; UC-24/25/26 là usecase độc lập để tinh chỉnh Hạn nộp, Test Case, Rubric từ ngân hàng đề. |
> | 🔴 **Lỗi xung đột import dữ liệu** | **UC-37** | Phân định rõ xử lý bản ghi hợp lệ / bản ghi lỗi và tùy chọn cập nhật tài khoản trùng. |
> | 🔴 **Lỗi hậu điều kiện Docker** | **UC-45** | Sửa hậu điều kiện: Cho phép dừng phiên container lỗi và ghi log mà không làm thay đổi cấu hình chung. |
> | 🟡 **Bảo mật & Phân quyền RBAC** | **UC-35 & UC-36** | Chặn Admin tự cấp quyền Admin/Superadmin (chống leo thang đặc quyền); Tự động thu hồi token và bắt buộc đổi mật khẩu khi Admin reset mật khẩu. |
> | 🟡 **Chính sách dữ liệu Xóa / Đóng** | **UC-19, UC-23, UC-34, UC-40** | Thống nhất cơ chế: **Xóa mềm (Soft Delete)** khi chưa có dữ liệu; chuyển **Lưu trữ/Đóng (Archived)** khi đã có bài nộp/điểm số. |
> | 🟡 **Phạm vi hiển thị Test Case** | **UC-12** | Công khai chi tiết Input/Output cho **Sample Test Cases**; chỉ hiển thị trạng thái Passed/Failed/TLE/MLE cho **Hidden Test Cases**. |
> | 🟢 **Chuẩn hóa Thuật ngữ & Tác nhân** | **Toàn bộ 47 UCs** | Đồng nhất 4 tác nhân duy nhất: **Sinh viên, Giảng viên, Quản trị viên, Quản trị viên hệ thống**; sửa URL `/student/problems` ở UC-07. |
> | 🟢 **Đánh số thứ tự luồng** | **Toàn bộ 47 UCs** | Chuẩn hóa quy tắc đánh số luồng rẽ nhánh theo đúng bước thực tế (`2a`, `3a`, `4a`, `5a`, `7a`...). |

---

| Mã usecase | UC-01 |
| :---- | :---- |
| **Tên usecase** | Đăng nhập |
| **Mô tả** | Cho phép người dùng xác thực tài khoản để bắt đầu phiên làm việc trên hệ thống. |
| **Tác nhân** | Sinh viên, Giảng viên, Quản trị viên, Quản trị viên hệ thống |
| **Tiền điều kiện** | Người dùng đã có tài khoản trong hệ thống. |
| **Hậu điều kiện** | Phiên đăng nhập được tạo thành công. Hệ thống cấp token xác thực (JWT) và chuyển người dùng đến trang chính phù hợp với vai trò. Nếu đăng nhập thất bại, phiên không được tạo và dữ liệu biểu mẫu vẫn được giữ để người dùng thử lại. |
| **Luồng tương tác chính** | 1. Người dùng truy cập trang đăng nhập.<br>2. Hệ thống hiển thị biểu mẫu yêu cầu Email và Mật khẩu.<br>3. Người dùng nhập thông tin tài khoản và chọn "Đăng nhập".<br>4. Hệ thống kiểm tra định dạng dữ liệu và tìm tài khoản tương ứng.<br>5. Hệ thống đối chiếu mật khẩu với mật khẩu đã được băm trong cơ sở dữ liệu, đồng thời kiểm tra trạng thái hoạt động của tài khoản.<br>6. Hệ thống tạo phiên đăng nhập và cấp access_token cùng refresh_token.<br>7. Hệ thống chuyển người dùng đến trang chính tương ứng với vai trò: Sinh viên, Giảng viên, Quản trị viên hoặc Quản trị viên hệ thống. |
| **Luồng tương tác thay thế** | 7a. Người dùng đã truy cập một trang yêu cầu đăng nhập trước đó: Hệ thống chuyển người dùng về trang được yêu cầu ban đầu thay vì trang chính mặc định. |
| **Luồng tương tác ngoại lệ** | E1 - Thông tin đăng nhập không hợp lệ (bước 4, 5): Hệ thống thông báo "Email hoặc mật khẩu không chính xác." và giữ nguyên biểu mẫu.<br>E2 - Tài khoản bị khóa hoặc vô hiệu hóa (bước 5): Hệ thống thông báo "Tài khoản đã bị khóa hoặc vô hiệu hóa. Vui lòng liên hệ Quản trị viên."<br>E3 - Lỗi hệ thống (bước 4, 6): Hệ thống thông báo "Đăng nhập thất bại, vui lòng thử lại sau." |

> 🟢 **[ĐÃ SỬA TẠI UC-01]**: Bỏ điều kiện "Tài khoản chưa bị khóa" khỏi Tiền điều kiện để tránh xung đột với Luồng ngoại lệ E2; Đồng bộ hóa 4 tác nhân chuẩn.

---

| Mã usecase | UC-02 |
| :---- | :---- |
| **Tên usecase** | Đăng xuất |
| **Mô tả** | Cho phép người dùng kết thúc phiên làm việc hiện tại trên hệ thống một cách an toàn. |
| **Tác nhân** | Sinh viên, Giảng viên, Quản trị viên, Quản trị viên hệ thống |
| **Tiền điều kiện** | Người dùng đang có phiên đăng nhập hợp lệ. |
| **Hậu điều kiện** | Phiên đăng nhập của người dùng được kết thúc. Token xác thực cục bộ bị xóa và người dùng được chuyển về trang đăng nhập. |
| **Luồng tương tác chính** | 1. Người dùng chọn "Đăng xuất" trên thanh điều hướng.<br>2. Hệ thống hiển thị yêu cầu xác nhận đăng xuất.<br>3. Người dùng xác nhận yêu cầu.<br>4. Hệ thống thu hồi hoặc đưa refresh_token vào danh sách vô hiệu hóa (blacklist/revoked tokens).<br>5. Hệ thống xóa token xác thực được lưu trên trình duyệt (Cookie / LocalStorage).<br>6. Hệ thống kết thúc phiên đăng nhập và chuyển người dùng về trang /login. |
| **Luồng tương tác thay thế** | 3a. Người dùng hủy xác nhận: Hệ thống đóng hộp thoại và giữ nguyên phiên làm việc hiện tại. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập đã hết hạn từ trước (bước 1, 4): Hệ thống tự động xóa thông tin xác thực cục bộ và chuyển người dùng về trang /login. |

> 🟢 **[ĐÃ SỬA TẠI UC-02]**: Bổ sung đầy đủ 4 tác nhân; Đánh số bước luồng 3a chuẩn xác.

---

| Mã usecase | UC-03 |
| :---- | :---- |
| **Tên usecase** | Quên mật khẩu |
| **Mô tả** | Cho phép người dùng xác thực quyền sở hữu tài khoản qua email và đặt lại mật khẩu mới khi không nhớ mật khẩu hiện tại. |
| **Tác nhân** | Sinh viên, Giảng viên, Quản trị viên, Quản trị viên hệ thống |
| **Tiền điều kiện** | Người dùng đang ở trang đăng nhập và có quyền truy cập địa chỉ email đã đăng ký tài khoản. |
| **Hậu điều kiện** | Mật khẩu mới được kiểm tra, băm an toàn và cập nhật vào cơ sở dữ liệu. Mã OTP hoặc liên kết khôi phục đã sử dụng bị vô hiệu hóa. Nếu khôi phục thất bại, mật khẩu hiện tại vẫn được giữ nguyên. |
| **Luồng tương tác chính** | 1. Người dùng chọn "Quên mật khẩu" tại trang đăng nhập.<br>2. Hệ thống hiển thị biểu mẫu yêu cầu nhập email tài khoản.<br>3. Người dùng nhập email và chọn "Gửi yêu cầu".<br>4. Hệ thống kiểm tra định dạng email và tạo mã OTP hoặc liên kết đặt lại mật khẩu có thời hạn (ví dụ: 15 phút).<br>5. Hệ thống gửi mã hoặc liên kết xác thực đến email của người dùng và thông báo "Đã gửi hướng dẫn khôi phục mật khẩu đến email."<br>6. Người dùng sử dụng mã hoặc liên kết nhận được để mở biểu mẫu đặt lại mật khẩu.<br>7. Người dùng nhập mật khẩu mới, xác nhận mật khẩu và chọn "Cập nhật mật khẩu".<br>8. Hệ thống kiểm tra tính hợp lệ của mã/liên kết và đối chiếu chính sách bảo mật của mật khẩu mới.<br>9. Hệ thống băm mật khẩu mới, cập nhật vào cơ sở dữ liệu và vô hiệu hóa mã/liên kết đã sử dụng.<br>10. Hệ thống thông báo "Khôi phục mật khẩu thành công." và chuyển người dùng về trang đăng nhập. |
| **Luồng tương tác thay thế** | 5a. Người dùng không nhận được email: Người dùng chọn "Gửi lại mã" sau thời gian đếm ngược quy định; hệ thống tạo và gửi lại mã xác thực mới. |
| **Luồng tương tác ngoại lệ** | E1 - Email không tồn tại hoặc sai định dạng (bước 4): Hệ thống đưa ra thông báo chung "Nếu email tồn tại trong hệ thống, bạn sẽ nhận được hướng dẫn khôi phục" (tránh dò quét tài khoản).<br>E2 - Mã hoặc liên kết hết hạn/không hợp lệ (bước 8): Hệ thống thông báo "Mã xác thực hoặc liên kết khôi phục không hợp lệ hoặc đã hết hạn."<br>E3 - Mật khẩu mới không đạt yêu cầu bảo mật (bước 8): Hệ thống thông báo "Mật khẩu mới không đủ độ phức tạp hoặc không trùng khớp."<br>E4 - Lỗi gửi mail hoặc lỗi cơ sở dữ liệu (bước 5, 9): Hệ thống thông báo "Không thể hoàn tất khôi phục mật khẩu, vui lòng thử lại sau." |

---

| Mã usecase | UC-04 |
| :---- | :---- |
| **Tên usecase** | Xem thông tin cá nhân |
| **Mô tả** | Cho phép người dùng xem thông tin hồ sơ cá nhân đã lưu trong hệ thống. |
| **Tác nhân** | Sinh viên, Giảng viên, Quản trị viên, Quản trị viên hệ thống |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Thông tin cá nhân hiện tại của người dùng được hiển thị; dữ liệu trong cơ sở dữ liệu không bị thay đổi. |
| **Luồng tương tác chính** | 1. Người dùng chọn mục "Hồ sơ cá nhân" từ menu tài khoản.<br>2. Hệ thống xác thực phiên đăng nhập và quyền truy cập.<br>3. Hệ thống truy vấn thông tin cá nhân từ cơ sở dữ liệu.<br>4. Hệ thống hiển thị các thông tin: Họ tên, Email, Số điện thoại, Mã định danh (MSSV/MSGV nếu có), Ảnh đại diện, Vai trò và Đơn vị/Tổ chức trực thuộc. |
| **Luồng tương tác thay thế** | 3a. Người dùng tải lại trang: Hệ thống truy vấn lại dữ liệu mới nhất từ cơ sở dữ liệu và hiển thị thông tin cập nhật. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn (bước 2): Hệ thống thông báo yêu cầu đăng nhập lại và chuyển người dùng về trang /login.<br>E2 - Lỗi truy vấn dữ liệu (bước 3): Hệ thống thông báo "Không thể tải thông tin cá nhân, vui lòng thử lại sau." |

---

| Mã usecase | UC-05 |
| :---- | :---- |
| **Tên usecase** | Cập nhật thông tin cá nhân |
| **Mô tả** | Cho phép người dùng chỉnh sửa và lưu các thông tin hồ sơ được hệ thống cho phép cập nhật. |
| **Tác nhân** | Sinh viên, Giảng viên, Quản trị viên, Quản trị viên hệ thống |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Thông tin hợp lệ được cập nhật và lưu vào cơ sở dữ liệu. Nếu cập nhật thất bại, thông tin cũ được giữ nguyên và hệ thống hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | 1. Người dùng truy cập trang "Hồ sơ cá nhân".<br>2. Hệ thống xác thực phiên đăng nhập và hiển thị thông tin hiện tại.<br>3. Người dùng chọn "Chỉnh sửa hồ sơ".<br>4. Hệ thống hiển thị biểu mẫu cho phép sửa các trường: Họ tên, Số điện thoại, Ảnh đại diện, Tiểu sử ngắn.<br>5. Người dùng cập nhật thông tin và chọn "Lưu thay đổi".<br>6. Hệ thống kiểm tra tính hợp lệ của dữ liệu (định dạng ảnh, số điện thoại, ký tự tên).<br>7. Hệ thống cập nhật thông tin mới vào cơ sở dữ liệu.<br>8. Hệ thống thông báo "Cập nhật thông tin cá nhân thành công." và làm mới dữ liệu hiển thị. |
| **Luồng tương tác thay thế** | 5a. Người dùng chọn "Hủy": Hệ thống đóng chế độ chỉnh sửa và giữ nguyên thông tin hiện tại.<br>5b. Người dùng không thay đổi thông tin: Hệ thống giữ nguyên dữ liệu hiện tại mà không cần gửi truy vấn ghi vào CSDL. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn (bước 2): Hệ thống thông báo yêu cầu đăng nhập và chuyển người dùng về trang /login.<br>E2 - Thông tin nhập không hợp lệ (bước 6): Hệ thống thông báo chi tiết lỗi (ví dụ: "Số điện thoại không đúng định dạng", "Dung lượng ảnh vượt quá 2MB") và giữ lại dữ liệu đã nhập để người dùng sửa.<br>E3 - Lỗi kết nối hoặc lưu dữ liệu (bước 7): Hệ thống thông báo "Cập nhật thông tin cá nhân thất bại, vui lòng thử lại." |

> 🟢 **[ĐÃ SỬA TẠI UC-05]**: Đã sửa lỗi thiếu đích chuyển hướng trong E1 ("về trang /login").

---

| Mã usecase | UC-06 |
| :---- | :---- |
| **Tên usecase** | Đổi mật khẩu |
| **Mô tả** | Cho phép người dùng chủ động thay đổi mật khẩu hiện tại sau khi xác thực mật khẩu cũ. |
| **Tác nhân** | Sinh viên, Giảng viên, Quản trị viên, Quản trị viên hệ thống |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. Người dùng biết mật khẩu hiện tại. |
| **Hậu điều kiện** | Mật khẩu mới được kiểm tra, băm an toàn và lưu vào cơ sở dữ liệu. Các phiên đăng nhập cũ trên thiết bị khác có thể được thu hồi tùy theo chính sách bảo mật. |
| **Luồng tương tác chính** | 1. Người dùng truy cập chức năng "Đổi mật khẩu" trong trang cá nhân/cài đặt tài khoản.<br>2. Hệ thống hiển thị biểu mẫu gồm: Mật khẩu hiện tại, Mật khẩu mới và Xác nhận mật khẩu mới.<br>3. Người dùng nhập đầy đủ thông tin và chọn "Đổi mật khẩu".<br>4. Hệ thống đối chiếu mật khẩu hiện tại với mật khẩu đã lưu trong cơ sở dữ liệu.<br>5. Hệ thống kiểm tra mật khẩu mới đáp ứng chính sách bảo mật (độ dài, ký tự đặc biệt, không trùng mật khẩu cũ) và khớp với trường xác nhận.<br>6. Hệ thống băm mật khẩu mới và lưu vào cơ sở dữ liệu.<br>7. Hệ thống thông báo "Đổi mật khẩu thành công." |
| **Luồng tương tác thay thế** | 3a. Người dùng chọn "Hủy": Hệ thống hủy thao tác và đóng biểu mẫu đổi mật khẩu. |
| **Luồng tương tác ngoại lệ** | E1 - Mật khẩu hiện tại không chính xác (bước 4): Hệ thống thông báo "Mật khẩu hiện tại không chính xác."<br>E2 - Mật khẩu mới không hợp lệ (bước 5): Hệ thống thông báo "Mật khẩu mới không đáp ứng yêu cầu bảo mật hoặc xác nhận mật khẩu không khớp."<br>E3 - Mật khẩu mới trùng với mật khẩu hiện tại (bước 5): Hệ thống thông báo "Mật khẩu mới phải khác mật khẩu hiện tại."<br>E4 - Lỗi lưu dữ liệu (bước 6): Hệ thống thông báo "Đổi mật khẩu thất bại, vui lòng thử lại sau." |

---

| Mã usecase | UC-07 |
| :---- | :---- |
| **Tên usecase** | Xem danh sách bài tập |
| **Mô tả** | Cho phép Sinh viên xem và tra cứu danh sách các bài tập được giao cho các lớp mà mình tham gia. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Danh sách bài tập phù hợp được hiển thị; dữ liệu bài tập không bị thay đổi. |
| **Luồng tương tác chính** | 1. Sinh viên truy cập mục "Bài tập" (/student/problems).<br>2. Hệ thống xác thực phiên đăng nhập và quyền truy cập của Sinh viên.<br>3. Hệ thống lấy danh sách các lớp học mà Sinh viên đang tham gia.<br>4. Hệ thống truy vấn các bài tập đang được giao cho Sinh viên từ các lớp học đó.<br>5. Hệ thống hiển thị danh sách bài tập với các thông tin: Tên bài tập, Tên lớp, Độ khó, Thời hạn nộp (Deadline), Trạng thái làm bài (Chưa làm, Đang làm, Đã nộp, Quá hạn), Điểm cao nhất đạt được.<br>6. Sinh viên có thể tìm kiếm theo tên hoặc lọc theo Lớp, Trạng thái làm bài, Độ khó. |
| **Luồng tương tác thay thế** | 6a. Sinh viên không chọn bộ lọc: Hệ thống hiển thị toàn bộ bài tập theo thứ tự ưu tiên (bài sắp đến hạn lên đầu).<br>6b. Không có bài tập nào: Hệ thống hiển thị danh sách rỗng và thông báo "Hiện chưa có bài tập nào được giao." |
| **Luồng tương tác ngoại lệ** | E1 - Lỗi truy vấn dữ liệu (bước 4): Hệ thống thông báo "Không thể tải danh sách bài tập, vui lòng thử lại sau." |

> 🟢 **[ĐÃ SỬA TẠI UC-07]**: Sửa URL bị find/replace sai (`/Sinh viên/problems` -> `/student/problems`).

---

| Mã usecase | UC-08 |
| :---- | :---- |
| **Tên usecase** | Xem chi tiết bài tập |
| **Mô tả** | Cho phép Sinh viên xem nội dung, yêu cầu chi tiết, sample test cases và rubric của một bài tập được giao. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và bài tập tồn tại trong hệ thống. |
| **Hậu điều kiện** | Nội dung chi tiết bài tập được hiển thị nếu Sinh viên có quyền truy cập. Nếu Sinh viên chọn làm bài, hệ thống chuyển đến không gian làm bài (IDE). |
| **Luồng tương tác chính** | 1. Sinh viên chọn một bài tập từ danh sách bài tập.<br>2. Hệ thống kiểm tra Sinh viên có thuộc lớp được giao bài tập này và bài tập đã mở hay chưa.<br>3. Hệ thống tải thông tin chi tiết bài tập từ cơ sở dữ liệu.<br>4. Hệ thống hiển thị đề bài hỗ trợ Markdown và công thức LaTeX (nếu có).<br>5. Hệ thống hiển thị các thông số: Ngôn ngữ cho phép, Giới hạn thời gian (Time Limit), Giới hạn bộ nhớ (Memory Limit), Sample Test Cases công khai, Hạn nộp bài và Rubric đánh giá.<br>6. Sinh viên chọn "Làm bài".<br>7. Hệ thống chuyển Sinh viên đến không gian làm bài (IDE / Trình soạn thảo). |
| **Luồng tương tác thay thế** | 6a. Sinh viên quay lại: Sinh viên chọn "Quay lại", hệ thống đưa Sinh viên về lại danh sách bài tập.<br>6b. Bài tập đã quá hạn nhưng cho phép nộp muộn hoặc cho phép xem lại: Hệ thống hiển thị cảnh báo về chính sách nộp muộn/xem lại và vẫn cho phép xem đề bài cũng như bấm "Làm bài". |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại (bước 2): Hệ thống thông báo "Không tìm thấy bài tập."<br>E2 - Sinh viên không có quyền truy cập (bước 2): Hệ thống thông báo "Bạn không thuộc lớp được giao bài tập này."<br>E3 - Bài tập chưa đến thời gian mở hoặc đã đóng hoàn toàn (bước 2): Hệ thống thông báo "Bài tập chưa mở hoặc đã kết thúc thời gian truy cập."<br>E4 - Lỗi tải dữ liệu (bước 3): Hệ thống thông báo "Không thể tải chi tiết bài tập, vui lòng thử lại sau." |

> 🔴 **[ĐÃ SỬA TẠI UC-08]**: Đã xử lý triệt để mâu thuẫn giữa UC-08 và UC-11: Bổ sung luồng 6b cho phép sinh viên xem đề và vào IDE nộp muộn nếu bài tập cho phép; E3 chỉ chặn khi bài tập bị khóa hoàn toàn.

---

| Mã usecase | UC-09 |
| :---- | :---- |
| **Tên usecase** | Viết và chỉnh sửa code |
| **Mô tả** | Cho phép Sinh viên viết, chỉnh sửa mã nguồn trực tiếp trong trình soạn thảo Monaco Editor và tự động lưu bản nháp. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã mở giao diện làm bài của bài tập có quyền truy cập. |
| **Hậu điều kiện** | Mã nguồn của Sinh viên được cập nhật và bản nháp được lưu tự động (Autosave). Bài làm ở dạng nháp và chưa được coi là bài nộp chính thức (Submission). |
| **Luồng tương tác chính** | 1. Sinh viên vào giao diện làm bài từ trang chi tiết bài tập.<br>2. Hệ thống khởi tạo Monaco Editor với ngôn ngữ lập trình và template/starter code phù hợp.<br>3. Sinh viên nhập hoặc chỉnh sửa mã nguồn.<br>4. Hệ thống thực hiện kiểm tra cú pháp cơ bản (Syntax highlighting, Linter) và tự động lưu bản nháp vào LocalStorage / Backend theo định kỳ (mỗi 30 giây hoặc sau khi ngừng gõ).<br>5. Sinh viên có thể chạy thử chương trình với Sample Test Cases hoặc chuyển sang thao tác nộp bài. |
| **Luồng tương tác thay thế** | 2a. Sinh viên tải lại trang: Hệ thống khôi phục bản nháp gần nhất đã lưu.<br>5a. Sinh viên chọn "Chạy thử": Hệ thống gửi mã nguồn cùng Sample Input đến Docker Sandbox để chạy và hiển thị kết quả chạy thử (Standard Output, Execution Time) mà không ghi nhận điểm chính thức. |
| **Luồng tương tác ngoại lệ** | E1 - Trình soạn thảo không khởi tạo được (bước 2): Hệ thống thông báo "Không thể tải trình soạn thảo, vui lòng làm mới trang."<br>E2 - Lỗi lưu bản nháp (bước 4): Hệ thống hiển thị cảnh báo "Mất kết nối lưu bản nháp, vui lòng sao lưu code ra máy cục bộ." |

---

| Mã usecase | UC-10 |
| :---- | :---- |
| **Tên usecase** | Tải tệp bài làm lên |
| **Mô tả** | Cho phép Sinh viên tải tệp mã nguồn từ máy tính cá nhân vào trình soạn thảo bài làm đang mở. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đang ở giao diện làm bài. Tệp tải lên có phần mở rộng thuộc danh sách ngôn ngữ được bài tập cho phép (ví dụ: .cpp, .py, .java, .c). |
| **Hậu điều kiện** | Nội dung tệp mã nguồn hợp lệ được nạp vào Monaco Editor và có thể tiếp tục chỉnh sửa. |
| **Luồng tương tác chính** | 1. Sinh viên chọn nút "Upload File" tại màn hình làm bài.<br>2. Hệ thống hiển thị hộp thoại chọn tệp từ máy tính.<br>3. Sinh viên chọn tệp mã nguồn và xác nhận.<br>4. Hệ thống kiểm tra phần mở rộng tệp, mã hóa ký tự (UTF-8) và kích thước tệp (tối đa 1MB).<br>5. Hệ thống đọc nội dung tệp và nạp vào Monaco Editor.<br>6. Hệ thống tự động lưu bản nháp của nội dung vừa nạp.<br>7. Hệ thống thông báo "Tải file lên thành công." |
| **Luồng tương tác thay thế** | 3a. Sinh viên hủy chọn tệp: Hệ thống đóng hộp thoại và giữ nguyên nội dung hiện tại trong editor. |
| **Luồng tương tác ngoại lệ** | E1 - Định dạng tệp không được hỗ trợ (bước 4): Hệ thống thông báo "Định dạng file không khớp với ngôn ngữ được phép của bài tập."<br>E2 - Tệp vượt quá dung lượng cho phép (bước 4): Hệ thống thông báo "Kích thước file vượt quá giới hạn (tối đa 1MB)."<br>E3 - Không thể đọc tệp do lỗi mã hóa hoặc tệp hỏng (bước 5): Hệ thống thông báo "Không thể đọc nội dung file, vui lòng thử lại với file khác." |

---

| Mã usecase | UC-11 |
| :---- | :---- |
| **Tên usecase** | Nộp bài |
| **Mô tả** | Cho phép Sinh viên gửi mã nguồn chính thức để hệ thống kích hoạt Auto-Grader và AI Engine chấm điểm, đánh giá và lưu kết quả. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập, có quyền làm bài. Bài tập đang trong thời hạn hoặc cho phép nộp muộn. Mã nguồn không được rỗng. |
| **Hậu điều kiện** | Một bản ghi bài nộp (Submission) được tạo với trạng thái PENDING. Kết quả chấm của Auto-Grader và phản hồi của AI được lưu sau khi xử lý hoàn tất. |
| **Luồng tương tác chính** | 1. Sinh viên kiểm tra mã nguồn trong editor và chọn "Nộp bài".<br>2. Hệ thống kiểm tra quyền nộp, trạng thái thời hạn của bài tập và độ dài mã nguồn.<br>3. Client gửi mã nguồn cùng thông tin bài tập lên Submission API.<br>4. Backend tạo bản ghi Submission với trạng thái PENDING và đẩy tác vụ chấm vào hàng đợi (Grading Queue).<br>5. Hệ thống trả về Submission ID và hiển thị thông báo "Đang chấm bài...".<br>6. Grader Worker nhận tác vụ, đưa mã nguồn và toàn bộ Test Cases (Sample + Hidden) vào Docker Sandbox cách ly.<br>7. Docker Sandbox biên dịch/thực thi mã nguồn với từng test case, ghi nhận Execution Evidence (Output, Runtime, Memory, Exit Code, Time/Memory Limit Exceeded).<br>8. Auto-Grader tính điểm theo Rubric và lưu kết quả chi tiết từng Test Case vào cơ sở dữ liệu.<br>9. AI Engine phân tích mã nguồn, kết quả chấm và đề bài để sinh AI Feedback sư phạm.<br>10. Hệ thống cập nhật trạng thái Submission thành COMPLETED (hoặc FAILED nếu lỗi chấm).<br>11. Hệ thống gửi thông báo hoàn tất chấm bài cho Sinh viên qua WebSocket hoặc Polling. |
| **Luồng tương tác thay thế** | 2a. Sinh viên nộp bài sau thời hạn quy định: Nếu bài tập cấu hình "Cho phép nộp muộn", hệ thống hiển thị cảnh báo trừ điểm nộp muộn theo quy định và ghi nhận cờ LATE_SUBMISSION.<br>5a. Sinh viên rời khỏi trang làm bài khi đang chấm: Hệ thống vẫn tiếp tục tiến trình chấm bài ngầm trong Docker Sandbox; Sinh viên có thể xem kết quả sau tại trang Lịch sử làm bài. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập đã hết hạn và không cho phép nộp muộn (bước 2): Hệ thống từ chối nộp và thông báo "Đã hết hạn nộp bài."<br>E2 - Mã nguồn rỗng hoặc vượt quá giới hạn ký tự (bước 2): Hệ thống thông báo "Mã nguồn không hợp lệ."<br>E3 - Hàng đợi chấm bài bị nghẽn/quá tải (bước 4): Hệ thống thông báo "Hệ thống đang bận, bài nộp đã được ghi nhận và sẽ được chấm trong ít phút."<br>E4 - Docker Sandbox gặp sự cố thực thi (bước 7): Hệ thống cập nhật trạng thái Submission thành SYSTEM_ERROR và ghi log để quản trị viên kiểm tra. |

> 🟢 **[ĐÃ SỬA TẠI UC-11]**: Chuẩn hóa lại đánh số luồng (`2a`, `5a`); Bổ sung xử lý chi tiết cờ phạt nộp muộn.

---

| Mã usecase | UC-12 |
| :---- | :---- |
| **Tên usecase** | Xem kết quả Auto-Grader |
| **Mô tả** | Cho phép Sinh viên xem điểm số và chi tiết kết quả kiểm thử tự động của một bài nộp. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và bài nộp thuộc quyền sở hữu của Sinh viên. |
| **Hậu điều kiện** | Kết quả Auto-Grader được hiển thị; dữ liệu chấm không bị thay đổi. |
| **Luồng tương tác chính** | 1. Sinh viên mở một bài nộp từ thông báo nộp bài hoặc từ trang lịch sử làm bài.<br>2. Hệ thống xác thực quyền sở hữu bài nộp của Sinh viên.<br>3. Hệ thống truy vấn kết quả chấm Auto-Grader từ cơ sở dữ liệu.<br>4. Hệ thống hiển thị tổng điểm Auto-Grader, thời gian chấm, tổng số test case đạt/không đạt.<br>5. Hệ thống hiển thị chi tiết từng Test Case: Đối với Sample Test Cases hiển thị đầy đủ Input, Output mong đợi, Output thực tế; đối với Hidden Test Cases chỉ hiển thị trạng thái (Passed / Failed / TLE / MLE / Runtime Error) để bảo mật đề thi.<br>6. Hệ thống hiển thị chi tiết lỗi biên dịch (Compile Error) hoặc lỗi thực thi nếu có. |
| **Luồng tương tác thay thế** | 3a. Bài nộp đang trong trạng thái PENDING hoặc RUNNING: Hệ thống hiển thị biểu tượng đang xử lý cùng thông báo "Bài nộp đang được chấm, vui lòng đợi..." và tự động cập nhật khi có kết quả. |
| **Luồng tương tác ngoại lệ** | E1 - Bài nộp không tồn tại (bước 2): Hệ thống thông báo "Không tìm thấy bài nộp."<br>E2 - Sinh viên không có quyền truy cập bài nộp của người khác (bước 2): Hệ thống từ chối truy cập (403 Forbidden).<br>E3 - Lỗi tải dữ liệu chấm (bước 3): Hệ thống thông báo "Không thể tải kết quả chấm, vui lòng thử lại sau." |

> 🟡 **[ĐÃ SỬA TẠI UC-12]**: Làm rõ quy định bảo mật: Sample Test hiển thị đủ Input/Output, Hidden Test chỉ hiển thị trạng thái; Sửa đánh số luồng 3a.

---

| Mã usecase | UC-13 |
| :---- | :---- |
| **Tên usecase** | Xem nhận xét AI |
| **Mô tả** | Cho phép Sinh viên xem nhận xét, phân tích chất lượng code và gợi ý cải thiện do AI sinh ra cho bài nộp. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập; bài nộp thuộc quyền sở hữu của Sinh viên và đã có kết quả chấm từ Auto-Grader. |
| **Hậu điều kiện** | Nhận xét AI được hiển thị nếu đã tạo; dữ liệu bài nộp không bị thay đổi. |
| **Luồng tương tác chính** | 1. Sinh viên mở trang chi tiết bài nộp và chọn tab "Nhận xét AI".<br>2. Hệ thống kiểm tra quyền truy cập và trạng thái phản hồi của AI cho bài nộp.<br>3. Hệ thống tải nội dung nhận xét AI đã được lưu trữ trong cơ sở dữ liệu.<br>4. Hệ thống hiển thị các mục nhận xét: Phân tích nguyên nhân lỗi (nếu có test case sai), Đánh giá phong cách viết mã (Clean Code, Naming), Đánh giá độ phức tạp thuật toán (Time & Space Complexity) và Gợi ý hướng tối ưu hóa.<br>5. Sinh viên đọc nhận xét để cải thiện mã nguồn. |
| **Luồng tương tác thay thế** | 3a. Nhận xét AI đang trong quá trình tạo (Background Job): Hệ thống hiển thị trạng thái "AI đang phân tích bài làm của bạn..." và tự động làm mới khi sẵn sàng.<br>3b. Bài tập được cấu hình tắt tính năng AI Feedback: Hệ thống hiển thị thông báo "Tính năng nhận xét AI không được bật cho bài tập này." |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy bài nộp hoặc không có quyền xem (bước 2): Hệ thống từ chối truy cập.<br>E2 - AI Service gặp lỗi timeout/rate limit khi sinh nhận xét (bước 3): Hệ thống hiển thị thông báo "Chưa thể sinh nhận xét AI tại thời điểm này. Bạn có thể yêu cầu tạo lại sau." |

---

| Mã usecase | UC-14 |
| :---- | :---- |
| **Tên usecase** | Tương tác với AI Tutor |
| **Mô tả** | Cho phép Sinh viên trò chuyện tương tác với AI Tutor để nhận gợi ý định hướng tư duy giải quyết vấn đề theo phương pháp Socratic (không đưa trực tiếp lời giải). |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và đang ở giao diện làm bài hoặc xem chi tiết bài tập. |
| **Hậu điều kiện** | Phiên trò chuyện được ghi nhận, câu hỏi và gợi ý của AI Tutor được hiển thị trong khung hội thoại. |
| **Luồng tương tác chính** | 1. Sinh viên mở khung chat "AI Tutor" tại giao diện làm bài.<br>2. Hệ thống tổng hợp ngữ cảnh (Context) gồm: Đề bài, Mã nguồn hiện tại trong editor, Kết quả test case bị lỗi (nếu đã chạy thử/nộp) và lịch sử hội thoại gần nhất.<br>3. Sinh viên nhập câu hỏi/thắc mắc và bấm "Gửi".<br>4. Hệ thống kiểm tra nội dung câu hỏi, áp dụng các ràng buộc an toàn (Pedagogical Guardrails).<br>5. Backend gửi Prompt kèm ngữ cảnh đến AI Engine.<br>6. AI Engine sinh phản hồi theo phương pháp gợi mở từng bước (Socratic Hinting), định hướng giải thuật hoặc giải thích lỗi mà không đưa toàn bộ code giải.<br>7. Hệ thống hiển thị phản hồi của AI Tutor trong khung chat.<br>8. Sinh viên đọc gợi ý và tiếp tục trao đổi trong phiên. |
| **Luồng tương tác thay thế** | 2a. Sinh viên chưa viết code: Hệ thống chỉ gửi ngữ cảnh đề bài để AI hướng dẫn phân tích yêu cầu đầu vào/đầu ra.<br>8a. Sinh viên chọn "Bắt đầu cuộc trò chuyện mới": Hệ thống lưu trữ phiên cũ và khởi tạo phiên trò chuyện trống mới. |
| **Luồng tương tác ngoại lệ** | E1 - Câu hỏi chứa nội dung vi phạm hoặc yêu cầu AI giải hộ trực tiếp (bước 4, 6): AI Tutor phản hồi từ chối khéo léo và hướng dẫn sinh viên tự tư duy qua gợi ý nhỏ.<br>E2 - AI Engine mất kết nối hoặc quá tải (bước 5): Hệ thống thông báo "AI Tutor tạm thời gián đoạn, vui lòng thử lại sau giây lát." |

---

| Mã usecase | UC-15 |
| :---- | :---- |
| **Tên usecase** | Xem lịch sử làm bài |
| **Mô tả** | Cho phép Sinh viên tra cứu toàn bộ danh sách các lần nộp bài của mình cho một bài tập hoặc trong toàn bộ khóa học. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Danh sách lịch sử bài nộp được hiển thị; dữ liệu không bị thay đổi. |
| **Luồng tương tác chính** | 1. Sinh viên chọn mục "Lịch sử nộp bài" tại trang chi tiết bài tập hoặc trang tổng quan cá nhân.<br>2. Hệ thống truy vấn toàn bộ các lần nộp bài (Submissions) của Sinh viên theo thứ tự thời gian mới nhất lên đầu.<br>3. Hệ thống hiển thị danh sách gồm: Mã bài nộp, Thời gian nộp, Ngôn ngữ, Trạng thái (Accepted, Wrong Answer, TLE, Compile Error...), Điểm số đạt được, Dung lượng bộ nhớ và Thời gian thực thi.<br>4. Sinh viên chọn một bài nộp cụ thể để xem lại mã nguồn và kết quả chi tiết. |
| **Luồng tương tác thay thế** | 3a. Sinh viên sử dụng bộ lọc: Sinh viên lọc lịch sử theo Lớp học, Trạng thái bài nộp hoặc Ngôn ngữ lập trình; hệ thống cập nhật danh sách tương ứng. |
| **Luồng tương tác ngoại lệ** | E1 - Sinh viên chưa từng nộp bài (bước 2): Hệ thống hiển thị thông báo "Bạn chưa có lần nộp bài nào cho bài tập này."<br>E2 - Lỗi truy vấn cơ sở dữ liệu (bước 2): Hệ thống thông báo "Không thể tải lịch sử làm bài, vui lòng thử lại sau." |

---

| Mã usecase | UC-16 |
| :---- | :---- |
| **Tên usecase** | Xem bảng điểm cá nhân |
| **Mô tả** | Cho phép Sinh viên xem tổng hợp điểm số, kết quả đánh giá các bài tập và xếp loại học tập trong các lớp mình tham gia. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Bảng điểm cá nhân được hiển thị theo quy tắc tính điểm của hệ thống; dữ liệu không bị thay đổi. |
| **Luồng tương tác chính** | 1. Sinh viên chọn mục "Bảng điểm" trên thanh điều hướng.<br>2. Hệ thống xác thực phiên đăng nhập và lấy danh sách lớp học của Sinh viên.<br>3. Sinh viên chọn lớp học cần xem bảng điểm.<br>4. Hệ thống truy vấn toàn bộ danh sách bài tập của lớp và kết quả điểm của Sinh viên (quy tắc: lấy điểm chính thức sau khi Giảng viên chấm thủ công nếu có; nếu chưa chấm thủ công thì lấy điểm cao nhất từ Auto-Grader).<br>5. Hệ thống hiển thị bảng điểm gồm: Tên bài tập, Trọng số điểm, Điểm Auto-Grader, Điểm Giảng viên chấm (kèm nhận xét nếu có), Điểm tổng kết và Trạng thái hoàn thành.<br>6. Hệ thống hiển thị tổng kết tiến độ và điểm trung bình tích lũy trong lớp học. |
| **Luồng tương tác thay thế** | 3a. Sinh viên lọc theo học kỳ hoặc môn học: Hệ thống hiển thị bảng điểm tương ứng với bộ lọc đã chọn.<br>4a. Bài tập đang trong trạng thái chờ Giảng viên chấm: Hệ thống hiển thị ghi chú "Đang chờ chấm điểm thủ công". |
| **Luồng tương tác ngoại lệ** | E1 - Sinh viên chưa tham gia lớp học nào (bước 2): Hệ thống hiển thị thông báo "Bạn chưa tham gia lớp học nào."<br>E2 - Lỗi tổng hợp dữ liệu điểm (bước 4): Hệ thống thông báo "Không thể tải bảng điểm, vui lòng thử lại sau." |

> 🟡 **[ĐÃ SỬA TẠI UC-16]**: Quy định rõ quy tắc chọn điểm cuối cùng (ưu tiên điểm chấm thủ công của Giảng viên; nếu chưa chấm thì lấy điểm Auto-Grader cao nhất) và bổ sung quyền xem nhận xét thủ công.

---

| Mã usecase | UC-17 |
| :---- | :---- |
| **Tên usecase** | Tạo lớp học |
| **Mô tả** | Cho phép Giảng viên tạo một lớp học mới do mình trực tiếp quản lý và giảng dạy. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền tạo/quản lý lớp học trong hệ thống. |
| **Hậu điều kiện** | Lớp học mới được tạo thành công, gắn với Giảng viên phụ trách và sinh mã tham gia lớp (Invite Code). |
| **Luồng tương tác chính** | 1. Giảng viên truy cập mục "Quản lý lớp học" và chọn "Tạo lớp mới".<br>2. Hệ thống hiển thị biểu mẫu tạo lớp gồm: Tên lớp học, Mã lớp, Học kỳ/Niên khóa, Mô tả lớp học.<br>3. Giảng viên nhập thông tin lớp học và chọn "Tạo lớp".<br>4. Hệ thống kiểm tra tính hợp lệ của thông tin và tính duy nhất của Mã lớp trong học kỳ.<br>5. Hệ thống tạo bản ghi Lớp học trong CSDL, thiết lập Giảng viên hiện tại là Quản trị viên của lớp và tự động sinh Mã mời tham gia (Class Invite Code).<br>6. Hệ thống thông báo "Tạo lớp học thành công." và chuyển Giảng viên đến trang chi tiết lớp học vừa tạo. |
| **Luồng tương tác thay thế** | 3a. Giảng viên chọn "Hủy": Hệ thống đóng biểu mẫu và không lưu dữ liệu.<br>3b. Giảng viên không tự nhập mã lớp: Hệ thống tự động sinh mã lớp theo quy tắc cấu hình của trường/hệ thống. |
| **Luồng tương tác ngoại lệ** | E1 - Thông tin lớp học không hợp lệ (bước 4): Hệ thống báo lỗi chi tiết (ví dụ: "Tên lớp không được để trống").<br>E2 - Mã lớp đã tồn tại trong hệ thống (bước 4): Hệ thống thông báo "Mã lớp đã tồn tại, vui lòng chọn mã khác."<br>E3 - Lỗi lưu dữ liệu (bước 5): Hệ thống thông báo "Tạo lớp học thất bại, vui lòng thử lại sau." |

---

| Mã usecase | UC-18 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa lớp học |
| **Mô tả** | Cho phép Giảng viên cập nhật các thông tin cơ bản của lớp học do mình phụ trách. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền quản lý lớp học cần chỉnh sửa. Lớp học đang ở trạng thái hoạt động. |
| **Hậu điều kiện** | Thông tin lớp học được cập nhật thành công vào cơ sở dữ liệu. |
| **Luồng tương tác chính** | 1. Giảng viên mở trang chi tiết lớp học cần sửa và chọn "Cài đặt lớp / Chỉnh sửa".<br>2. Hệ thống hiển thị biểu mẫu chứa thông tin hiện tại của lớp học.<br>3. Giảng viên thay đổi Tên lớp, Mô tả, Học kỳ hoặc tạo lại Mã mời tham gia lớp mới.<br>4. Giảng viên chọn "Lưu thay đổi".<br>5. Hệ thống kiểm tra tính hợp lệ của dữ liệu sửa đổi.<br>6. Hệ thống cập nhật thông tin lớp học vào cơ sở dữ liệu.<br>7. Hệ thống thông báo "Cập nhật thông tin lớp học thành công." |
| **Luồng tương tác thay thế** | 4a. Giảng viên chọn "Hủy": Hệ thống hủy thao tác và khôi phục lại dữ liệu ban đầu. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp học không tồn tại hoặc đã bị xóa (bước 1): Hệ thống thông báo "Không tìm thấy lớp học."<br>E2 - Giảng viên không có quyền quản trị lớp học này (bước 1): Hệ thống từ chối truy cập.<br>E3 - Lỗi cập nhật CSDL (bước 6): Hệ thống thông báo "Chỉnh sửa lớp học thất bại, vui lòng thử lại." |

---

| Mã usecase | UC-19 |
| :---- | :---- |
| **Tên usecase** | Xóa/đóng lớp học |
| **Mô tả** | Cho phép Giảng viên đóng lớp khi học kỳ kết thúc hoặc xóa lớp học theo chính sách toàn vẹn dữ liệu. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền quản trị lớp học. |
| **Hậu điều kiện** | Nếu đóng lớp: Trạng thái lớp chuyển sang ARCHIVED/CLOSED (không nhận bài nộp mới, sinh viên chỉ có thể xem lại). Nếu xóa: Lớp được xóa mềm theo chính sách dữ liệu. |
| **Luồng tương tác chính** | 1. Giảng viên truy cập trang cài đặt của lớp học.<br>2. Giảng viên chọn thao tác "Đóng lớp" hoặc "Xóa lớp".<br>3. Hệ thống hiển thị hộp thoại cảnh báo về phạm vi ảnh hưởng của thao tác.<br>4. Giảng viên xác nhận thực hiện.<br>5. Hệ thống kiểm tra dữ liệu lớp học: Nếu lớp đã có sinh viên và bài nộp, hệ thống chỉ cho phép chuyển sang trạng thái "Đã đóng/Lưu trữ" (ARCHIVED); nếu lớp rỗng chưa có dữ liệu phát sinh, hệ thống thực hiện xóa mềm (Soft Delete).<br>6. Hệ thống cập nhật trạng thái lớp trong cơ sở dữ liệu.<br>7. Hệ thống thông báo thao tác thành công và cập nhật lại danh sách lớp học của Giảng viên. |
| **Luồng tương tác thay thế** | 4a. Giảng viên hủy xác nhận: Hệ thống đóng hộp thoại và giữ nguyên trạng thái hiện tại của lớp. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp học không tồn tại hoặc đã đóng trước đó (bước 1): Hệ thống thông báo trạng thái không hợp lệ.<br>E2 - Lỗi hệ thống khi cập nhật trạng thái (bước 6): Hệ thống thông báo "Không thể xử lý yêu cầu, vui lòng thử lại sau." |

> 🟡 **[ĐÃ SỬA TẠI UC-19]**: Đồng nhất chính sách Đóng/Xóa lớp với Quản trị viên (UC-40): Đóng/Lưu trữ khi có dữ liệu, Xóa mềm khi chưa có dữ liệu; Sửa số bước luồng 4a.

---

| Mã usecase | UC-20 |
| :---- | :---- |
| **Tên usecase** | Quản lý sinh viên trong lớp |
| **Mô tả** | Cho phép Giảng viên thêm sinh viên (qua email/mã SV/danh sách), duyệt sinh viên tham gia bằng mã mời hoặc xóa sinh viên ra khỏi lớp học do mình phụ trách. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền quản lý lớp học. Lớp học đang mở. |
| **Hậu điều kiện** | Danh sách sinh viên thuộc lớp được cập nhật thành công trong cơ sở dữ liệu. |
| **Luồng tương tác chính** | 1. Giảng viên mở chi tiết lớp học và chọn tab "Danh sách sinh viên".<br>2. Hệ thống hiển thị danh sách sinh viên hiện tại trong lớp (Họ tên, Mã SV, Email, Ngày tham gia, Trạng thái).<br>3. Giảng viên chọn thao tác: "Thêm sinh viên" (nhập email/MSSV) hoặc chọn một sinh viên và bấm "Xóa khỏi lớp".<br>4. Giảng viên nhập thông tin sinh viên cần thêm hoặc xác nhận xóa sinh viên được chọn.<br>5. Hệ thống kiểm tra tính hợp lệ của tài khoản sinh viên và trạng thái trong lớp.<br>6. Hệ thống cập nhật danh sách thành viên của lớp học trong cơ sở dữ liệu.<br>7. Hệ thống thông báo thao tác thành công và làm mới danh sách hiển thị. |
| **Luồng tương tác thay thế** | 3a. Giảng viên nhập danh sách sinh viên hàng loạt qua tệp Excel: Hệ thống đọc file, kiểm tra các tài khoản hợp lệ và thêm hàng loạt vào lớp.<br>3b. Giảng viên duyệt sinh viên tham gia qua Mã mời (Invite Code): Giảng viên xem danh sách sinh viên chờ duyệt và chọn "Chấp nhận" hoặc "Từ chối". |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy tài khoản sinh viên theo email/mã SV (bước 5): Hệ thống thông báo "Không tìm thấy tài khoản sinh viên tương ứng."<br>E2 - Sinh viên đã là thành viên của lớp (bước 5): Hệ thống thông báo "Sinh viên này đã có trong danh sách lớp."<br>E3 - Sinh viên đã có bài nộp trong lớp không thể xóa trực tiếp (bước 5): Hệ thống thông báo "Sinh viên đã có lịch sử làm bài, chuyển trạng thái thành Vô hiệu hóa trong lớp thay vì xóa hoàn toàn." |

---

| Mã usecase | UC-21 |
| :---- | :---- |
| **Tên usecase** | Tạo bài tập |
| **Mô tả** | Cho phép Giảng viên tạo một bài tập lập trình mới vào ngân hàng bài tập hoặc tạo trực tiếp để giao cho lớp học. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền tạo bài tập. |
| **Hậu điều kiện** | Bài tập mới được tạo ở trạng thái Bản nháp (DRAFT) hoặc Đã xuất bản (PUBLISHED) kèm theo cấu hình đề bài, ngôn ngữ và giới hạn tài nguyên. |
| **Luồng tương tác chính** | 1. Giảng viên truy cập "Ngân hàng bài tập" và chọn "Tạo bài tập mới".<br>2. Hệ thống hiển thị biểu mẫu tạo bài tập gồm: Tiêu đề, Độ khó, Chủ đề/Thẻ tag, Mô tả bài toán (Markdown + LaTeX), Ràng buộc dữ liệu, Định dạng Input/Output, Ngôn ngữ lập trình cho phép, Time Limit và Memory Limit.<br>3. Giảng viên nhập đầy đủ thông tin bài tập.<br>4. Giảng viên có thể thiết lập nhanh Sample Test Cases và cấu hình cơ bản.<br>5. Giảng viên chọn "Lưu bài tập" hoặc "Lưu bản nháp".<br>6. Hệ thống kiểm tra tính hợp lệ của các trường dữ liệu.<br>7. Hệ thống lưu bài tập vào cơ sở dữ liệu và thông báo "Tạo bài tập thành công." |
| **Luồng tương tác thay thế** | 5a. Giảng viên muốn thiết lập chuyên sâu Test Case / Rubric / Deadline: Giảng viên chọn chuyển tiếp sang các chức năng tương ứng (UC-24, UC-25, UC-26). |
| **Luồng tương tác ngoại lệ** | E1 - Thiếu thông tin bắt buộc hoặc dữ liệu không hợp lệ (bước 6): Hệ thống thông báo lỗi chi tiết tại các trường vi phạm.<br>E2 - Giới hạn thời gian/bộ nhớ không hợp lệ (bước 6): Hệ thống thông báo "Time Limit (100ms - 10000ms) và Memory Limit (16MB - 512MB) nằm ngoài phạm vi cho phép."<br>E3 - Lỗi lưu dữ liệu (bước 7): Hệ thống thông báo "Không thể tạo bài tập, vui lòng thử lại sau." |

> 🔴 **[ĐÃ SỬA TẠI UC-21]**: Phân tách rõ ràng: UC-21 là tạo bài tập vào ngân hàng đề với các thông số cơ bản; các UC-24, UC-25, UC-26 là các use case mở rộng độc lập để tinh chỉnh chuyên sâu.

---

| Mã usecase | UC-22 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa bài tập |
| **Mô tả** | Cho phép Giảng viên chỉnh sửa nội dung, mô tả hoặc cấu hình của bài tập do mình sở hữu. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập; bài tập tồn tại và thuộc quyền sở hữu của Giảng viên. |
| **Hậu điều kiện** | Nội dung bài tập được cập nhật vào cơ sở dữ liệu; nếu bài đã có submission, hệ thống áp dụng cơ chế đánh phiên bản (Versioning) để bảo toàn tính nhất quán. |
| **Luồng tương tác chính** | 1. Giảng viên mở danh sách bài tập và chọn bài tập cần sửa.<br>2. Hệ thống tải và hiển thị thông tin hiện tại của bài tập.<br>3. Giảng viên chỉnh sửa đề bài, định dạng Input/Output, ngôn ngữ hoặc giới hạn tài nguyên.<br>4. Giảng viên chọn "Lưu thay đổi".<br>5. Hệ thống kiểm tra tính hợp lệ của dữ liệu chỉnh sửa.<br>6. Nếu bài tập chưa có submission, hệ thống cập nhật trực tiếp; nếu bài tập đã có sinh viên nộp bài, hệ thống tạo phiên bản mới của bài tập (Version bump) và thông báo phạm vi ảnh hưởng.<br>7. Hệ thống thông báo "Cập nhật bài tập thành công." |
| **Luồng tương tác thay thế** | 4a. Giảng viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên nội dung cũ. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy bài tập hoặc không có quyền sửa (bước 1): Hệ thống từ chối truy cập.<br>E2 - Dữ liệu chỉnh sửa không hợp lệ (bước 5): Hệ thống hiển thị thông báo lỗi.<br>E3 - Lỗi lưu dữ liệu (bước 6): Hệ thống thông báo "Chỉnh sửa bài tập thất bại." |

---

| Mã usecase | UC-23 |
| :---- | :---- |
| **Tên usecase** | Xóa bài tập |
| **Mô tả** | Cho phép Giảng viên xóa hoặc lưu trữ/vô hiệu hóa bài tập khỏi ngân hàng đề. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền sở hữu bài tập. |
| **Hậu điều kiện** | Bài tập được xóa mềm (Soft Delete) hoặc vô hiệu hóa; các bài nộp và điểm số lịch sử của sinh viên (nếu có) được bảo toàn trong hệ thống. |
| **Luồng tương tác chính** | 1. Giảng viên chọn bài tập cần xóa trong danh sách bài tập.<br>2. Giảng viên chọn thao tác "Xóa bài tập".<br>3. Hệ thống hiển thị hộp thoại xác nhận và thông báo tình trạng sử dụng của bài tập (đã giao cho lớp nào, có bài nộp chưa).<br>4. Giảng viên xác nhận xóa.<br>5. Hệ thống kiểm tra: Nếu bài tập đã được giao và có bài nộp, hệ thống thực hiện vô hiệu hóa (Ẩn khỏi danh sách mới, giữ lại dữ liệu lịch sử); nếu bài tập chưa từng sử dụng, hệ thống đánh dấu xóa mềm (is_deleted = true).<br>6. Hệ thống thông báo "Xóa bài tập thành công." và cập nhật lại danh sách. |
| **Luồng tương tác thay thế** | 4a. Giảng viên chọn "Hủy": Hệ thống đóng hộp thoại và giữ nguyên bài tập. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy bài tập hoặc không có quyền xóa (bước 1): Hệ thống từ chối yêu cầu.<br>E2 - Lỗi hệ thống khi xóa (bước 5): Hệ thống thông báo "Không thể xóa bài tập, vui lòng thử lại sau." |

> 🟢 **[ĐÃ SỬA TẠI UC-23]**: Đánh số lại luồng 4a; Làm rõ chính sách xóa mềm (Soft delete) khi bài tập đã phát sinh lịch sử nộp bài.

---

| Mã usecase | UC-24 |
| :---- | :---- |
| **Tên usecase** | Thiết lập hạn nộp bài |
| **Mô tả** | Cho phép Giảng viên cấu hình hoặc điều chỉnh thời gian mở đề, hạn chót nộp bài (Deadline) và chính sách nộp muộn cho bài tập được giao. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập; bài tập đã tồn tại và đã được gán/giao cho lớp học. |
| **Hậu điều kiện** | Hạn nộp bài và chính sách nộp muộn mới được áp dụng cho sinh viên trong lớp. |
| **Luồng tương tác chính** | 1. Giảng viên chọn chức năng "Thiết lập hạn nộp" tại bài tập đã giao trong lớp học.<br>2. Hệ thống hiển thị cấu hình thời gian hiện tại: Thời gian bắt đầu mở đề, Hạn nộp chính thức (Due Date), Hạn chót đóng hoàn toàn (Cut-off Date), Tỷ lệ trừ điểm nộp muộn (%/ngày).<br>3. Giảng viên điều chỉnh các mốc thời gian và chính sách phạt nộp muộn.<br>4. Giảng viên chọn "Lưu cấu hình thời hạn".<br>5. Hệ thống kiểm tra tính hợp lý (Thời gian mở < Hạn nộp < Hạn chót).<br>6. Hệ thống cập nhật thời hạn vào cơ sở dữ liệu.<br>7. Hệ thống thông báo "Thiết lập hạn nộp bài thành công." |
| **Luồng tương tác thay thế** | 4a. Giảng viên chọn "Hủy": Hệ thống đóng biểu mẫu và giữ nguyên hạn nộp cũ.<br>4b. Giảng viên gia hạn riêng cho một nhóm sinh viên: Giảng viên chọn danh sách sinh viên được đặc cách gia hạn; hệ thống lưu thời hạn riêng biệt (Override Deadline). |
| **Luồng tương tác ngoại lệ** | E1 - Mốc thời gian không hợp lệ (bước 5): Hệ thống thông báo "Hạn nộp bài phải sau thời gian mở đề và không được nhỏ hơn thời điểm hiện tại."<br>E2 - Lỗi lưu dữ liệu (bước 6): Hệ thống thông báo "Không thể cập nhật hạn nộp, vui lòng thử lại." |

> 🟢 **[ĐÃ SỬA TẠI UC-24]**: Đánh số luồng thay thế theo bước thực tế (`4a`, `4b`); Làm rõ vai trò thiết lập hạn nộp theo từng lớp học.

---

| Mã usecase | UC-25 |
| :---- | :---- |
| **Tên usecase** | Thiết lập test case |
| **Mô tả** | Cho phép Giảng viên tạo, chỉnh sửa, nhập hàng loạt (Zip/Excel) các Test Cases (Sample, Hidden) phục vụ Auto-Grader. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập; bài tập đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Danh sách Test Cases hợp lệ được lưu vào cơ sở dữ liệu và sẵn sàng cho Docker Sandbox thực thi chấm điểm. |
| **Luồng tương tác chính** | 1. Giảng viên mở bài tập và chọn tab "Quản lý Test Case".<br>2. Hệ thống hiển thị danh sách Test Cases hiện có (loại Sample/Hidden, điểm/trọng số, Input, Expected Output).<br>3. Giảng viên chọn "Thêm Test Case", nhập Input, Output mong đợi, giải thích (cho Sample test), chọn loại test (Sample công khai hoặc Hidden bí mật) và điểm số.<br>4. Giảng viên chọn "Lưu Test Case".<br>5. Hệ thống kiểm tra tính hợp lệ của dữ liệu đầu vào/đầu ra và tổng trọng số điểm.<br>6. Hệ thống lưu Test Case vào cơ sở dữ liệu.<br>7. Hệ thống thông báo "Thiết lập Test Case thành công." |
| **Luồng tương tác thay thế** | 3a. Giảng viên tải lên tệp nén Zip chứa các cặp tệp .in / .out: Hệ thống tự động giải nén, phân tích cú pháp và nạp toàn bộ danh sách Test Case.<br>3b. Giảng viên chỉnh sửa hoặc xóa một Test Case hiện có: Giảng viên chọn Test Case tương ứng, thực hiện thay đổi và lưu. |
| **Luồng tương tác ngoại lệ** | E1 - Dữ liệu Input hoặc Expected Output rỗng/sai định dạng (bước 5): Hệ thống thông báo "Dữ liệu Test Case không hợp lệ."<br>E2 - Tệp Zip không đúng cấu trúc cặp .in/.out (bước 3a): Hệ thống thông báo "Cấu trúc file zip không đúng định dạng chuẩn."<br>E3 - Lỗi lưu CSDL (bước 6): Hệ thống thông báo "Thiết lập Test Case thất bại." |

---

| Mã usecase | UC-26 |
| :---- | :---- |
| **Tên usecase** | Thiết lập rubric |
| **Mô tả** | Cho phép Giảng viên thiết lập các tiêu chí đánh giá, trọng số điểm và quy tắc chấm (Correctness, Code Quality, Time/Space Complexity) cho bài tập. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập; bài tập đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Bảng tiêu chí Rubric được lưu thành công và áp dụng cho cả Auto-Grader, AI Engine và chấm thủ công. |
| **Luồng tương tác chính** | 1. Giảng viên mở bài tập và chọn tab "Thiết lập Rubric".<br>2. Hệ thống hiển thị cấu hình Rubric hiện tại hoặc mẫu Rubric mặc định (Correctness: 70%, Code Quality: 15%, Complexity: 15%).<br>3. Giảng viên tùy chỉnh danh sách tiêu chí, mô tả mức độ đạt (Levels) và tỷ lệ % hoặc điểm số tối đa cho từng tiêu chí.<br>4. Giảng viên chọn "Lưu Rubric".<br>5. Hệ thống kiểm tra tính hợp lệ: Tổng điểm các tiêu chí phải đúng bằng thang điểm tối đa (100% hoặc 10 điểm).<br>6. Hệ thống lưu Rubric vào cơ sở dữ liệu.<br>7. Hệ thống thông báo "Thiết lập Rubric thành công." |
| **Luồng tương tác thay thế** | 3a. Giảng viên chọn sử dụng mẫu Rubric chuẩn của hệ thống: Hệ thống tự động nạp cấu hình tiêu chí mẫu để Giảng viên chỉnh sửa nhanh. |
| **Luồng tương tác ngoại lệ** | E1 - Tổng tỷ lệ % tiêu chí không bằng 100% (bước 5): Hệ thống thông báo "Tổng trọng số các tiêu chí phải đúng 100%."<br>E2 - Tiêu chí không có tên hoặc thang điểm âm (bước 5): Hệ thống thông báo "Thông tin tiêu chí Rubric không hợp lệ."<br>E3 - Lỗi lưu CSDL (bước 6): Hệ thống thông báo "Thiết lập Rubric thất bại." |

---

| Mã usecase | UC-27 |
| :---- | :---- |
| **Tên usecase** | Giao bài tập cho lớp |
| **Mô tả** | Cho phép Giảng viên giao một bài tập từ ngân hàng đề cho một hoặc nhiều lớp học do mình phụ trách kèm thời hạn và cấu hình riêng cho từng lớp. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập; bài tập đã tồn tại; lớp học đang ở trạng thái hoạt động và Giảng viên có quyền quản lý lớp. |
| **Hậu điều kiện** | Bài tập được liên kết với lớp học; sinh viên trong lớp có thể xem đề và làm bài theo thời hạn quy định. |
| **Luồng tương tác chính** | 1. Giảng viên chọn bài tập trong ngân hàng đề và bấm "Giao cho lớp".<br>2. Hệ thống hiển thị danh sách các lớp học mà Giảng viên đang quản lý.<br>3. Giảng viên chọn (các) lớp cần giao bài và thiết lập thời gian bắt đầu mở đề, hạn nộp bài (Deadline) cho lớp đó.<br>4. Giảng viên chọn "Xác nhận giao bài".<br>5. Hệ thống kiểm tra: Lớp học chưa được giao bài tập này trước đó (hoặc xác nhận giao lại theo phiên bản mới).<br>6. Hệ thống tạo bản ghi liên kết Assignment-Class trong cơ sở dữ liệu và gửi thông báo cho sinh viên trong lớp.<br>7. Hệ thống thông báo "Giao bài tập thành công." |
| **Luồng tương tác thay thế** | 3a. Giảng viên giao cho lớp đã từng được giao bài tập này: Hệ thống thông báo bài tập đã được giao cho lớp và hiển thị tùy chọn "Cập nhật cấu hình/Gia hạn" thay vì tạo bản ghi trùng lặp; Giảng viên xác nhận cập nhật.<br>3b. Giảng viên chọn "Hủy": Hệ thống đóng biểu mẫu và không thực hiện giao bài. |
| **Luồng tương tác ngoại lệ** | E1 - Giảng viên không có quyền quản lý lớp được chọn (bước 5): Hệ thống từ chối yêu cầu.<br>E2 - Thời gian giao bài không hợp lệ (bước 5): Hệ thống thông báo "Thời hạn nộp bài không hợp lệ."<br>E3 - Lỗi lưu dữ liệu (bước 6): Hệ thống thông báo "Giao bài tập thất bại, vui lòng thử lại." |

> 🔴 **[ĐÃ SỬA TẠI UC-27]**: Giải quyết triệt để mâu thuẫn giữa E4 và luồng 1c: Luồng chính giao bài mới, luồng 3a cho phép cập nhật cấu hình nếu lớp đã giao trước đó, loại bỏ báo lỗi giả.

---

| Mã usecase | UC-28 |
| :---- | :---- |
| **Tên usecase** | Xem danh sách bài nộp (Submission) |
| **Mô tả** | Cho phép Giảng viên xem toàn bộ danh sách và chi tiết các bài nộp của sinh viên trong một bài tập đã giao. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền quản lý bài tập trong lớp học. |
| **Hậu điều kiện** | Danh sách bài nộp được hiển thị đầy đủ; dữ liệu hệ thống không bị thay đổi. |
| **Luồng tương tác chính** | 1. Giảng viên chọn một bài tập đã giao trong lớp học và chọn mục "Danh sách bài nộp".<br>2. Hệ thống hiển thị danh sách sinh viên cùng trạng thái nộp bài (Đã nộp, Chưa nộp, Nộp muộn, Số lần nộp, Điểm Auto-Grader, Điểm chính thức).<br>3. Giảng viên chọn một sinh viên để xem danh sách các lần nộp (Submissions) của sinh viên đó.<br>4. Giảng viên chọn một bài nộp cụ thể để xem chi tiết: Mã nguồn, Thời gian nộp, Kết quả thực thi từng Test Case, Lịch sử chạy thử, Nhận xét AI và Bảng chấm điểm Rubric. |
| **Luồng tương tác thay thế** | 2a. Giảng viên lọc/sắp xếp danh sách: Giảng viên lọc theo Trạng thái (Chưa chấm, Đã chấm, Nộp muộn) hoặc sắp xếp theo Điểm số / Thời gian nộp.<br>4a. Giảng viên tải về toàn bộ mã nguồn của cả lớp: Giảng viên chọn "Tải mã nguồn (Zip)"; hệ thống nén toàn bộ bài nộp mới nhất của sinh viên và cung cấp link tải. |
| **Luồng tương tác ngoại lệ** | E1 - Lỗi tải dữ liệu bài nộp (bước 2): Hệ thống thông báo "Không thể tải danh sách bài nộp, vui lòng thử lại sau." |

---

| Mã usecase | UC-29 |
| :---- | :---- |
| **Tên usecase** | Xem điểm |
| **Mô tả** | Cho phép Giảng viên theo dõi bảng tổng hợp điểm, phổ điểm và thống kê kết quả làm bài của cả lớp đối với các bài tập đã giao. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền quản lý lớp học. |
| **Hậu điều kiện** | Bảng điểm tổng hợp và biểu đồ phổ điểm của lớp được hiển thị; dữ liệu không bị thay đổi. |
| **Luồng tương tác chính** | 1. Giảng viên truy cập mục "Bảng điểm lớp học" tại lớp đang quản lý.<br>2. Hệ thống truy vấn điểm của toàn bộ sinh viên cho tất cả các bài tập trong lớp.<br>3. Hệ thống hiển thị bảng ma trận điểm (Sinh viên x Bài tập), điểm trung bình, tỷ lệ hoàn thành và biểu đồ phân bố điểm (Histogram).<br>4. Giảng viên có thể chọn xem chi tiết từng cột bài tập hoặc xuất bảng điểm. |
| **Luồng tương tác thay thế** | 4a. Giảng viên xuất bảng điểm ra file Excel/CSV: Giảng viên chọn "Xuất Excel"; hệ thống tạo tệp bảng điểm hoàn chỉnh và tải về máy tính. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp học chưa có bài tập hoặc chưa có sinh viên nào nộp bài (bước 2): Hệ thống hiển thị thông báo "Chưa có dữ liệu điểm số."<br>E2 - Lỗi truy vấn cơ sở dữ liệu (bước 2): Hệ thống thông báo "Không thể tải bảng điểm, vui lòng thử lại." |

---

| Mã usecase | UC-30 |
| :---- | :---- |
| **Tên usecase** | Xem AI đánh giá |
| **Mô tả** | Cho phép Giảng viên xem chi tiết phân tích của AI Engine đối với bài làm của sinh viên (phân tích lỗi, chất lượng code, độ phức tạp và cảnh báo gian lận/sao chép). |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập; bài nộp của sinh viên đã được hệ thống xử lý qua AI Engine. |
| **Hậu điều kiện** | Báo cáo đánh giá AI được hiển thị đầy đủ; dữ liệu hệ thống không bị thay đổi. |
| **Luồng tương tác chính** | 1. Giảng viên mở chi tiết bài nộp của sinh viên và chọn mục "Báo cáo AI Đánh giá".<br>2. Hệ thống truy vấn dữ liệu AI Feedback và chỉ số phân tích mã nguồn từ CSDL.<br>3. Hệ thống hiển thị: Điểm gợi ý từ AI theo Rubric, Nhận xét phong cách lập trình (Clean Code, Naming Conventions, Code Smells), Phân tích độ phức tạp thời gian/không gian và Điểm tương đồng mã nguồn (nếu có kiểm tra Plagiarism).<br>4. Giảng viên tham khảo kết quả AI để phục vụ việc chấm điểm thủ công hoặc phản hồi trực tiếp cho sinh viên. |
| **Luồng tương tác thay thế** | 3a. Bài nộp chưa được AI phân tích: Giảng viên bấm nút "Yêu cầu AI phân tích"; hệ thống gửi tác vụ vào hàng đợi AI và hiển thị kết quả sau khi hoàn tất. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy báo cáo AI (bước 2): Hệ thống thông báo "Báo cáo AI chưa sẵn sàng cho bài nộp này."<br>E2 - Lỗi kết nối dịch vụ AI (bước 3a): Hệ thống thông báo "Không thể kích hoạt AI phân tích, vui lòng thử lại sau." |

---

| Mã usecase | UC-31 |
| :---- | :---- |
| **Tên usecase** | Đánh giá/chấm bài thủ công |
| **Mô tả** | Cho phép Giảng viên trực tiếp chấm điểm, ghi đè điểm Auto-Grader, điền điểm theo tiêu chí Rubric và viết nhận xét cá nhân hóa cho bài nộp của sinh viên. |
| **Tác nhân** | Giảng viên |
| **Tiền điều kiện** | Giảng viên đã đăng nhập và có quyền chấm bài cho lớp học. Sinh viên đã có bài nộp. |
| **Hậu điều kiện** | Điểm chính thức và nhận xét của Giảng viên được lưu vào cơ sở dữ liệu, ghi đè lên điểm tạm thời và hiển thị cho Sinh viên. |
| **Luồng tương tác chính** | 1. Giảng viên mở bài nộp của sinh viên từ danh sách bài nộp.<br>2. Hệ thống hiển thị mã nguồn sinh viên, kết quả Auto-Grader, gợi ý của AI và biểu mẫu chấm điểm theo Rubric.<br>3. Giảng viên xem mã nguồn, nhập điểm cho từng tiêu chí trong Rubric (hoặc điều chỉnh tổng điểm) và nhập nhận xét (Feedback) chi tiết cho sinh viên.<br>4. Giảng viên chọn "Lưu kết quả chấm".<br>5. Hệ thống kiểm tra tính hợp lệ của điểm số (nằm trong thang điểm cho phép).<br>6. Hệ thống lưu điểm chính thức, nhận xét và thời gian chấm của Giảng viên vào cơ sở dữ liệu.<br>7. Hệ thống cập nhật bảng điểm của lớp và gửi thông báo kết quả cho Sinh viên.<br>8. Hệ thống thông báo "Chấm bài thành công." |
| **Luồng tương tác thay thế** | 4a. Giảng viên chọn "Lưu nháp": Hệ thống lưu điểm và nhận xét tạm thời mà chưa công bố cho sinh viên.<br>4b. Giảng viên chọn "Chấm bài tiếp theo": Hệ thống lưu kết quả bài hiện tại và tự động chuyển sang bài nộp của sinh viên kế tiếp trong danh sách. |
| **Luồng tương tác ngoại lệ** | E1 - Điểm nhập vượt quá thang điểm quy định (bước 5): Hệ thống thông báo "Điểm nhập không hợp lệ, vui lòng kiểm tra lại thang điểm Rubric."<br>E2 - Lỗi lưu dữ liệu (bước 6): Hệ thống thông báo "Lưu kết quả chấm thất bại, vui lòng thử lại." |

---

| Mã usecase | UC-32 |
| :---- | :---- |
| **Tên usecase** | Tạo tài khoản người dùng |
| **Mô tả** | Cho phép Quản trị viên tạo tài khoản mới cho Sinh viên hoặc Giảng viên trên hệ thống. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập và có quyền quản lý tài khoản người dùng. |
| **Hậu điều kiện** | Tài khoản mới được tạo, gán đúng vai trò (Sinh viên / Giảng viên), lưu vào CSDL và gửi email thông tin đăng nhập cho người dùng. |
| **Luồng tương tác chính** | 1. Quản trị viên truy cập mục "Quản lý người dùng" và chọn "Tạo tài khoản mới".<br>2. Hệ thống hiển thị biểu mẫu gồm: Họ và tên, Email, Mã định danh (MSSV/MSGV), Vai trò (Sinh viên / Giảng viên), Số điện thoại và Mật khẩu khởi tạo (hoặc tùy chọn hệ thống tự sinh mật khẩu).<br>3. Quản trị viên nhập thông tin, chọn vai trò và chọn "Tạo tài khoản".<br>4. Hệ thống kiểm tra định dạng email, tính duy nhất của email và mã định danh.<br>5. Hệ thống băm mật khẩu, tạo tài khoản trong CSDL và gửi email thông báo thông tin đăng nhập (kèm yêu cầu đổi mật khẩu ở lần đầu đăng nhập).<br>6. Hệ thống thông báo "Tạo tài khoản thành công." và cập nhật lại danh sách người dùng. |
| **Luồng tương tác thay thế** | 3a. Quản trị viên chọn "Hủy": Hệ thống đóng biểu mẫu và không tạo tài khoản. |
| **Luồng tương tác ngoại lệ** | E1 - Email hoặc Mã định danh đã tồn tại trong hệ thống (bước 4): Hệ thống thông báo "Email hoặc Mã người dùng đã được sử dụng."<br>E2 - Dữ liệu nhập không hợp lệ (bước 4): Hệ thống hiển thị lỗi tại các trường không đúng định dạng.<br>E3 - Lỗi hệ thống khi tạo tài khoản (bước 5): Hệ thống thông báo "Tạo tài khoản thất bại, vui lòng thử lại sau." |

> 🟢 **[ĐÃ SỬA TẠI UC-32]**: Khắc phục lỗi chọn vai trò 2 lần; gộp thành 1 bước nhập dữ liệu nhất quán.

---

| Mã usecase | UC-33 |
| :---- | :---- |
| **Tên usecase** | Khóa/mở khóa tài khoản |
| **Mô tả** | Cho phép Quản trị viên tạm thời khóa hoặc kích hoạt lại trạng thái hoạt động của tài khoản người dùng. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập; tài khoản cần khóa/mở khóa đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Trạng thái tài khoản được cập nhật; tài khoản bị khóa sẽ bị thu hồi toàn bộ token và không thể đăng nhập. |
| **Luồng tương tác chính** | 1. Quản trị viên chọn tài khoản cần xử lý trong danh sách người dùng.<br>2. Quản trị viên chọn thao tác "Khóa tài khoản" hoặc "Mở khóa tài khoản".<br>3. Hệ thống hiển thị hộp thoại xác nhận và yêu cầu nhập lý do (nếu khóa).<br>4. Quản trị viên xác nhận thao tác.<br>5. Hệ thống cập nhật trạng thái tài khoản (STATUS_ACTIVE / STATUS_LOCKED) trong CSDL.<br>6. Nếu là thao tác khóa, hệ thống lập tức thu hồi toàn bộ phiên đăng nhập/JWT Token đang hoạt động của tài khoản đó.<br>7. Hệ thống thông báo "Cập nhật trạng thái tài khoản thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hủy thao tác: Hệ thống đóng hộp thoại và giữ nguyên trạng thái tài khoản. |
| **Luồng tương tác ngoại lệ** | E1 - Quản trị viên cố tình khóa chính tài khoản của mình (bước 4): Hệ thống từ chối thao tác và thông báo "Không thể tự khóa tài khoản đang đăng nhập."<br>E2 - Lỗi cập nhật CSDL (bước 5): Hệ thống thông báo "Thao tác thất bại, vui lòng thử lại sau." |

---

| Mã usecase | UC-34 |
| :---- | :---- |
| **Tên usecase** | Xóa tài khoản |
| **Mô tả** | Cho phép Quản trị viên xóa tài khoản người dùng theo chính sách bảo toàn toàn vẹn dữ liệu học tập. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập; tài khoản cần xóa tồn tại trong hệ thống. |
| **Hậu điều kiện** | Tài khoản được xóa mềm (Soft Delete) hoặc vô hiệu hóa vĩnh viễn; các dữ liệu liên kết như bài nộp, điểm số lịch sử được ẩn danh hóa hoặc giữ nguyên tính toàn vẹn tham chiếu. |
| **Luồng tương tác chính** | 1. Quản trị viên chọn tài khoản cần xóa trong danh sách người dùng.<br>2. Quản trị viên chọn thao tác "Xóa tài khoản".<br>3. Hệ thống hiển thị hộp thoại cảnh báo nguy cơ và tóm tắt các dữ liệu liên quan (lớp học đang phụ trách, bài tập đã nộp, bảng điểm).<br>4. Quản trị viên xác nhận xóa.<br>5. Hệ thống kiểm tra: Nếu tài khoản đã có dữ liệu hoạt động trong CSDL, hệ thống thực hiện Xóa mềm (đánh dấu is_deleted = true, vô hiệu hóa đăng nhập, ẩn khỏi các danh sách hoạt động); nếu tài khoản mới tạo chưa phát sinh dữ liệu, hệ thống cho phép xóa vật lý.<br>6. Hệ thống thu hồi toàn bộ phiên làm việc của tài khoản và thông báo "Xóa tài khoản thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hủy thao tác: Hệ thống đóng hộp thoại và giữ nguyên tài khoản. |
| **Luồng tương tác ngoại lệ** | E1 - Quản trị viên cố tình xóa chính mình hoặc tài khoản Quản trị viên hệ thống cấp cao hơn (bước 4): Hệ thống từ chối thao tác (403 Forbidden).<br>E2 - Lỗi hệ thống khi xóa (bước 5): Hệ thống thông báo "Xóa tài khoản thất bại, vui lòng thử lại sau." |

> 🟡 **[ĐÃ SỬA TẠI UC-34]**: Đồng nhất chính sách Xóa mềm (Soft Delete) giữa Hậu điều kiện và Ngoại lệ E3; đảm bảo tính toàn vẹn tham chiếu dữ liệu.

---

| Mã usecase | UC-35 |
| :---- | :---- |
| **Tên usecase** | Phân quyền người dùng |
| **Mô tả** | Cho phép Quản trị viên điều chỉnh vai trò và quyền hạn (RBAC) của người dùng trong phạm vi cho phép (Sinh viên, Giảng viên). |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập và có quyền quản lý phân quyền. Tài khoản cần phân quyền đã tồn tại. |
| **Hậu điều kiện** | Quyền hạn mới của người dùng được cập nhật thành công trong cơ sở dữ liệu. |
| **Luồng tương tác chính** | 1. Quản trị viên chọn tài khoản cần phân quyền từ danh sách người dùng.<br>2. Quản trị viên chọn chức năng "Phân quyền người dùng".<br>3. Hệ thống hiển thị vai trò hiện tại và danh sách các quyền hạn được phép cấp/thu hồi (ví dụ: Quyền tạo bài tập, Quyền quản lý lớp học, Quyền trợ giảng).<br>4. Quản trị viên chọn vai trò hoặc bật/tắt các quyền hạn mong muốn (chỉ trong phạm vi vai trò Sinh viên / Giảng viên; không được tự ý nâng lên Admin/Superadmin).<br>5. Quản trị viên chọn "Lưu quyền hạn".<br>6. Hệ thống kiểm tra tính hợp lệ và ghi nhận thay đổi vào bảng phân quyền trong CSDL.<br>7. Hệ thống thông báo "Phân quyền người dùng thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn "Hủy": Hệ thống đóng biểu mẫu và giữ nguyên quyền hạn cũ. |
| **Luồng tương tác ngoại lệ** | E1 - Cố tình cấp quyền Admin/Superadmin vượt cấp đặc quyền (Privilege Escalation) (bước 4): Hệ thống chặn thao tác và thông báo "Bạn không có quyền cấp quyền Quản trị viên cấp cao."<br>E2 - Lỗi lưu quyền hạn (bước 6): Hệ thống thông báo "Cập nhật quyền thất bại, vui lòng thử lại." |

> 🟡 **[ĐÃ SỬA TẠI UC-35]**: Bổ sung cơ chế bảo mật chặn leo thang đặc quyền (Admin không được tự phong quyền Superadmin).

---

| Mã usecase | UC-36 |
| :---- | :---- |
| **Tên usecase** | Đặt lại mật khẩu |
| **Mô tả** | Cho phép Quản trị viên đặt lại mật khẩu cho tài khoản người dùng khi có yêu cầu hỗ trợ hoặc sự cố đăng nhập. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập và có quyền quản lý tài khoản. Tài khoản cần đặt lại mật khẩu tồn tại trong hệ thống. |
| **Hậu điều kiện** | Mật khẩu mới được băm và lưu vào CSDL; toàn bộ phiên đăng nhập cũ bị thu hồi; cờ yêu cầu đổi mật khẩu ở lần đăng nhập tới (must_change_password) được kích hoạt. |
| **Luồng tương tác chính** | 1. Quản trị viên chọn tài khoản cần đặt lại mật khẩu trong danh sách người dùng.<br>2. Quản trị viên chọn thao tác "Đặt lại mật khẩu".<br>3. Hệ thống hiển thị hộp thoại cho phép Quản trị viên tự nhập mật khẩu mới hoặc chọn "Tạo mật khẩu ngẫu nhiên an toàn".<br>4. Quản trị viên chọn tùy chọn và xác nhận "Đặt lại mật khẩu".<br>5. Hệ thống băm mật khẩu mới, cập nhật vào CSDL, kích hoạt cờ bắt buộc đổi mật khẩu và thu hồi toàn bộ token cũ của tài khoản.<br>6. Hệ thống gửi email thông báo mật khẩu mới cho người dùng (hoặc hiển thị một lần cho Quản trị viên sao chép).<br>7. Hệ thống thông báo "Đặt lại mật khẩu thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn "Hủy": Hệ thống đóng hộp thoại và giữ nguyên mật khẩu cũ. |
| **Luồng tương tác ngoại lệ** | E1 - Mật khẩu tự nhập không đáp ứng chính sách bảo mật (bước 4): Hệ thống thông báo "Mật khẩu không đạt tiêu chuẩn độ phức tạp."<br>E2 - Lỗi cập nhật CSDL (bước 5): Hệ thống thông báo "Đặt lại mật khẩu thất bại." |

> 🟡 **[ĐÃ SỬA TẠI UC-36]**: Bổ sung yêu cầu bảo mật: Thu hồi toàn bộ token cũ và kích hoạt cờ bắt buộc đổi mật khẩu ở lần đăng nhập tiếp theo.

---

| Mã usecase | UC-37 |
| :---- | :---- |
| **Tên usecase** | Nhập danh sách từ Excel/CSV |
| **Mô tả** | Cho phép Quản trị viên nhập danh sách người dùng hàng loạt từ tệp Excel/CSV để tạo tài khoản hoặc cập nhật thông tin nhanh chóng. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập và có tệp dữ liệu danh sách người dùng đúng định dạng mẫu. |
| **Hậu điều kiện** | Các tài khoản hợp lệ được tạo/cập nhật vào CSDL; hệ thống xuất báo cáo kết quả chi tiết kèm danh sách các dòng bị lỗi (nếu có). |
| **Luồng tương tác chính** | 1. Quản trị viên truy cập chức năng "Nhập từ Excel/CSV" tại trang Quản lý người dùng.<br>2. Hệ thống hiển thị giao diện tải tệp, cung cấp tệp mẫu (Template) và mô tả các trường bắt buộc.<br>3. Quản trị viên tải lên tệp Excel/CSV.<br>4. Hệ thống kiểm tra cấu trúc tệp, đọc dữ liệu và kiểm tra tính hợp lệ từng dòng (Email, Tên, Mã SV/GV, Vai trò).<br>5. Hệ thống hiển thị bảng xem trước (Preview) dữ liệu, thống kê số dòng hợp lệ và số dòng lỗi.<br>6. Quản trị viên xác nhận "Tiến hành nhập dữ liệu".<br>7. Hệ thống lưu toàn bộ bản ghi hợp lệ vào cơ sở dữ liệu, tự động tạo tài khoản và gửi email thông báo.<br>8. Hệ thống thông báo "Nhập danh sách thành công [X]/[Tổng] bản ghi." và cung cấp tệp tải về danh sách các bản ghi thất bại kèm lý do. |
| **Luồng tương tác thay thế** | 5a. Tệp có tài khoản đã tồn tại: Hệ thống cung cấp tùy chọn "Bỏ qua bản ghi trùng" hoặc "Cập nhật thông tin bản ghi trùng"; Quản trị viên chọn và hệ thống xử lý theo cấu hình.<br>6a. Quản trị viên chọn "Hủy": Hệ thống hủy toàn bộ tiến trình nhập dữ liệu và không thay đổi CSDL. |
| **Luồng tương tác ngoại lệ** | E1 - Tệp không đúng định dạng .xlsx/.csv hoặc dung lượng quá lớn (bước 4): Hệ thống thông báo "Tệp không đúng định dạng hoặc vượt quá 5MB."<br>E2 - Tệp sai hoàn toàn cấu trúc cột (bước 4): Hệ thống thông báo "Cấu trúc tệp không khớp với biểu mẫu chuẩn."<br>E3 - Toàn bộ dữ liệu trong tệp đều lỗi (bước 5): Hệ thống thông báo "Không có bản ghi hợp lệ nào để nhập."<br>E4 - Lỗi cơ sở dữ liệu khi nhập hàng loạt (bước 7): Hệ thống rollback transaction và thông báo "Nhập dữ liệu thất bại, không có bản ghi nào bị thay đổi." |

> 🔴 **[ĐÃ SỬA TẠI UC-37]**: Khắc phục mâu thuẫn nội bộ giữa E4/E5 và các luồng 1b/1c; làm rõ cơ chế nhập từng phần bản ghi hợp lệ và xuất file báo cáo dòng lỗi.

---

| Mã usecase | UC-38 |
| :---- | :---- |
| **Tên usecase** | Tạo lớp học (Quản trị viên) |
| **Mô tả** | Cho phép Quản trị viên khởi tạo lớp học mới trên toàn hệ thống/tổ chức và phân công Giảng viên phụ trách lớp. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập và có quyền quản lý lớp học toàn trường/tổ chức. |
| **Hậu điều kiện** | Lớp học mới được tạo thành công trong CSDL, được gán mã lớp duy nhất và phân công Giảng viên phụ trách (nếu có). |
| **Luồng tương tác chính** | 1. Quản trị viên truy cập mục "Quản lý lớp học" trên thanh điều hướng quản trị.<br>2. Hệ thống hiển thị danh sách các lớp học hiện có trong toàn hệ thống.<br>3. Quản trị viên chọn nút "Tạo lớp học mới".<br>4. Hệ thống hiển thị biểu mẫu tạo lớp gồm: Mã lớp học, Tên lớp học, Ngành/Khoa, Học kỳ/Niên khóa, Mô tả và Danh sách Giảng viên để phân công phụ trách.<br>5. Quản trị viên nhập thông tin lớp học, chọn Giảng viên phụ trách từ danh sách và chọn "Tạo lớp".<br>6. Hệ thống kiểm tra tính hợp lệ của dữ liệu và tính duy nhất của Mã lớp trong học kỳ.<br>7. Hệ thống tạo bản ghi lớp học trong CSDL, gán quyền Giảng viên phụ trách và sinh mã tham gia lớp.<br>8. Hệ thống thông báo "Tạo lớp học thành công." và hiển thị lớp học mới trên danh sách quản lý. |
| **Luồng tương tác thay thế** | 5a. Quản trị viên chọn "Hủy": Hệ thống đóng biểu mẫu và không tạo lớp mới.<br>5b. Quản trị viên chưa phân công Giảng viên ngay lúc tạo: Hệ thống cho phép tạo lớp ở trạng thái chưa phân công giảng viên để bổ sung sau (UC-42). |
| **Luồng tương tác ngoại lệ** | E1 - Thông tin lớp không hợp lệ hoặc để trống trường bắt buộc (bước 6): Hệ thống thông báo "Vui lòng nhập đầy đủ các trường bắt buộc."<br>E2 - Mã lớp học đã tồn tại trong học kỳ (bước 6): Hệ thống thông báo "Mã lớp đã tồn tại trong hệ thống."<br>E3 - Lỗi khi lưu cơ sở dữ liệu (bước 7): Hệ thống thông báo "Tạo lớp học thất bại, vui lòng thử lại sau." |

> 🔴 **[ĐÃ VIẾT LẠI HOÀN TOÀN TẠI UC-38]**: Đã xóa bỏ toàn bộ nội dung dán nhầm của "Quản lý đề thi", thay thế bằng luồng tạo lớp học chuẩn của Quản trị viên kèm tích hợp phân công giảng viên.

---

| Mã usecase | UC-39 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa lớp học (Quản trị viên) |
| **Mô tả** | Cho phép Quản trị viên cập nhật thông tin tổng thể của bất kỳ lớp học nào trong hệ thống. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập; lớp học cần chỉnh sửa tồn tại trong hệ thống. |
| **Hậu điều kiện** | Thông tin lớp học được cập nhật thành công vào cơ sở dữ liệu. |
| **Luồng tương tác chính** | 1. Quản trị viên truy cập mục "Quản lý lớp học" và chọn lớp cần chỉnh sửa.<br>2. Hệ thống hiển thị chi tiết và thông tin cấu hình hiện tại của lớp.<br>3. Quản trị viên chỉnh sửa Tên lớp, Khoa/Ngành, Học kỳ hoặc Mô tả lớp học.<br>4. Quản trị viên chọn "Lưu thay đổi".<br>5. Hệ thống kiểm tra tính hợp lệ của thông tin.<br>6. Hệ thống cập nhật thông tin lớp học vào cơ sở dữ liệu.<br>7. Hệ thống thông báo "Chỉnh sửa lớp học thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn "Hủy": Hệ thống đóng biểu mẫu và giữ nguyên thông tin lớp ban đầu. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp học không tồn tại hoặc đã bị xóa (bước 1): Hệ thống thông báo "Không tìm thấy lớp học."<br>E2 - Tên hoặc thông tin lớp không hợp lệ (bước 5): Hệ thống thông báo chi tiết lỗi.<br>E3 - Lỗi cập nhật CSDL (bước 6): Hệ thống thông báo "Chỉnh sửa lớp học thất bại." |

---

| Mã usecase | UC-40 |
| :---- | :---- |
| **Tên usecase** | Xóa/đóng lớp học (Quản trị viên) |
| **Mô tả** | Cho phép Quản trị viên đóng lớp học hoặc xóa lớp học khỏi hệ thống theo chính sách quản trị cấp cao. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập; lớp học tồn tại trong hệ thống. |
| **Hậu điều kiện** | Lớp học được chuyển sang trạng thái Đã đóng (ARCHIVED) hoặc Xóa mềm (Soft Delete) theo đúng chính sách toàn vẹn dữ liệu. |
| **Luồng tương tác chính** | 1. Quản trị viên chọn lớp học cần xử lý trong danh sách quản lý lớp.<br>2. Quản trị viên chọn thao tác "Đóng lớp" hoặc "Xóa lớp".<br>3. Hệ thống hiển thị hộp thoại xác nhận, thống kê các dữ liệu liên quan (số sinh viên, bài tập, bài nộp, giảng viên).<br>4. Quản trị viên xác nhận thao tác.<br>5. Hệ thống kiểm tra dữ liệu: Nếu lớp đã có bài nộp và điểm số, hệ thống chuyển lớp sang trạng thái ARCHIVED để bảo toàn lịch sử học tập; nếu lớp chưa phát sinh dữ liệu, hệ thống thực hiện xóa mềm (Soft Delete).<br>6. Hệ thống cập nhật CSDL và thông báo "Xử lý lớp học thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn "Hủy": Hệ thống đóng hộp thoại và giữ nguyên trạng thái lớp. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp học không tồn tại (bước 1): Hệ thống thông báo "Không tìm thấy lớp học."<br>E2 - Lỗi hệ thống khi cập nhật trạng thái (bước 5): Hệ thống thông báo "Thao tác thất bại, vui lòng thử lại sau." |

> 🟡 **[ĐÃ SỬA TẠI UC-40]**: Đồng nhất chính sách Đóng/Xóa lớp giữa Giảng viên (UC-19) và Quản trị viên (UC-40).

---

| Mã usecase | UC-41 |
| :---- | :---- |
| **Tên usecase** | Quản lý sinh viên trong lớp (Quản trị viên) |
| **Mô tả** | Cho phép Quản trị viên can thiệp quản lý danh sách sinh viên của lớp học (thêm, xóa, chuyển lớp hoặc nhập danh sách theo file). |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập; lớp học tồn tại trong hệ thống. |
| **Hậu điều kiện** | Danh sách sinh viên thuộc lớp được cập nhật chính xác trong cơ sở dữ liệu. |
| **Luồng tương tác chính** | 1. Quản trị viên mở trang chi tiết lớp học và chọn tab "Quản lý sinh viên".<br>2. Hệ thống hiển thị danh sách sinh viên hiện tại trong lớp.<br>3. Quản trị viên chọn thao tác: "Thêm sinh viên", "Xóa sinh viên khỏi lớp" hoặc "Nhập danh sách từ Excel".<br>4. Quản trị viên thực hiện nhập thông tin/chọn sinh viên tương ứng và xác nhận.<br>5. Hệ thống kiểm tra tính hợp lệ của tài khoản sinh viên.<br>6. Hệ thống cập nhật danh sách thành viên của lớp học trong CSDL.<br>7. Hệ thống thông báo "Cập nhật danh sách sinh viên thành công." |
| **Luồng tương tác thay thế** | 3a. Quản trị viên chuyển sinh viên sang lớp khác: Quản trị viên chọn sinh viên, chọn lớp đích; hệ thống cập nhật lớp cho sinh viên.<br>4a. Quản trị viên chọn "Hủy": Hệ thống giữ nguyên danh sách sinh viên. |
| **Luồng tương tác ngoại lệ** | E1 - Tài khoản sinh viên không tồn tại (bước 5): Hệ thống thông báo "Không tìm thấy sinh viên."<br>E2 - Sinh viên đã có trong lớp (bước 5): Hệ thống thông báo "Sinh viên đã thuộc lớp này."<br>E3 - Lỗi cập nhật CSDL (bước 6): Hệ thống thông báo "Thao tác thất bại, vui lòng thử lại." |

---

| Mã usecase | UC-42 |
| :---- | :---- |
| **Tên usecase** | Phân công giảng viên vào lớp |
| **Mô tả** | Cho phép Quản trị viên phân công, thay đổi hoặc gán thêm Giảng viên phụ trách giảng dạy cho một lớp học. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập; lớp học và tài khoản Giảng viên đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Giảng viên được phân công thành công vào lớp và có đầy đủ quyền hạn quản lý lớp học đó. |
| **Luồng tương tác chính** | 1. Quản trị viên mở trang quản lý lớp học và chọn chức năng "Phân công giảng viên".<br>2. Hệ thống hiển thị thông tin lớp và danh sách Giảng viên hiện đang phụ trách lớp.<br>3. Quản trị viên chọn "Thêm giảng viên phụ trách" hoặc chọn Giảng viên hiện tại để "Thay đổi / Hủy phân công".<br>4. Quản trị viên chọn Giảng viên từ danh sách và chọn vai trò trong lớp (Giảng viên chính / Trợ giảng).<br>5. Quản trị viên xác nhận phân công.<br>6. Hệ thống kiểm tra tính hợp lệ và lưu thông tin phân công vào CSDL.<br>7. Hệ thống gửi thông báo cho Giảng viên được phân công và thông báo "Phân công giảng viên thành công." |
| **Luồng tương tác thay thế** | 5a. Quản trị viên chọn "Hủy": Hệ thống đóng biểu mẫu và giữ nguyên danh sách phân công cũ. |
| **Luồng tương tác ngoại lệ** | E1 - Giảng viên không tồn tại hoặc tài khoản đang bị khóa (bước 6): Hệ thống thông báo "Giảng viên không hợp lệ hoặc đang bị khóa."<br>E2 - Giảng viên đã được phân công vào lớp này trước đó (bước 6): Hệ thống thông báo "Giảng viên đã được phân công vào lớp này."<br>E3 - Lớp học đã đóng (bước 6): Hệ thống thông báo "Không thể phân công giảng viên cho lớp học đã đóng."<br>E4 - Lỗi lưu CSDL (bước 6): Hệ thống thông báo "Phân công giảng viên thất bại." |

---

| Mã usecase | UC-43 |
| :---- | :---- |
| **Tên usecase** | Quản lý cấu hình AI |
| **Mô tả** | Cho phép Quản trị viên hệ thống quản lý các mô hình LLM, API Keys, Temperature, System Prompts và Guardrails cho AI Tutor và AI Grader. |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập và có quyền quản trị cấp cao nhất. |
| **Hậu điều kiện** | Cấu hình AI mới được lưu và áp dụng cho toàn bộ các tác vụ sinh phản hồi và phân tích của hệ thống. |
| **Luồng tương tác chính** | 1. Quản trị viên hệ thống truy cập mục "Cấu hình AI System".<br>2. Hệ thống hiển thị danh sách các cấu hình AI hiện có (Provider: OpenAI, Gemini, Claude, Ollama; Model; Temperature; Max Tokens; System Prompts; Trạng thái kích hoạt).<br>3. Quản trị viên hệ thống chọn cấu hình cần sửa hoặc chọn "Thêm cấu hình mới".<br>4. Quản trị viên hệ thống nhập các thông số API Key, Model ID, điều chỉnh System Prompt sư phạm và thiết lập Token Limit.<br>5. Quản trị viên hệ thống chọn "Kiểm tra kết nối (Test Connection)".<br>6. Hệ thống gửi request mẫu đến AI Provider và hiển thị trạng thái kết nối thành công.<br>7. Quản trị viên hệ thống chọn "Lưu & Kích hoạt cấu hình".<br>8. Hệ thống mã hóa lưu API Key, cập nhật cấu hình hoạt động vào cơ sở dữ liệu và thông báo "Cập nhật cấu hình AI thành công." |
| **Luồng tương tác thay thế** | 3a. Quản trị viên hệ thống chọn "Hủy": Hệ thống giữ nguyên cấu hình đang hoạt động.<br>7a. Quản trị viên hệ thống chỉ lưu cấu hình mà không kích hoạt ngay: Hệ thống lưu ở trạng thái không hoạt động (INACTIVE). |
| **Luồng tương tác ngoại lệ** | E1 - Thông số cấu hình thiếu hoặc không hợp lệ (bước 4): Hệ thống thông báo chi tiết thông số vi phạm.<br>E2 - Kết nối đến AI Provider thất bại (bước 6): Hệ thống hiển thị lỗi từ nhà cung cấp (Invalid API Key, Quota Exceeded, Timeout) và không cho kích hoạt.<br>E3 - Lỗi lưu CSDL (bước 8): Hệ thống thông báo "Lưu cấu hình AI thất bại." |

---

| Mã usecase | UC-44 |
| :---- | :---- |
| **Tên usecase** | Cấu hình Docker Sandbox |
| **Mô tả** | Cho phép Quản trị viên hệ thống cấu hình môi trường Container thực thi mã nguồn an toàn (Resource Limits, Network Isolation, Timeout, Security Profiles). |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập và có quyền cấu hình hạ tầng Docker Sandbox. |
| **Hậu điều kiện** | Cấu hình Docker Sandbox mới được lưu và áp dụng cho tất cả các phiên biên dịch và chạy test case mới. |
| **Luồng tương tác chính** | 1. Quản trị viên hệ thống truy cập mục "Cấu hình Docker Sandbox".<br>2. Hệ thống hiển thị các thông số hiện tại: Giới hạn CPU per container, Giới hạn RAM tối đa, Max Execution Timeout, Cấu hình cgroup, Trạng thái ngắt mạng hoàn toàn (Network Disabled = true), Danh sách Docker Images cho các ngôn ngữ (GCC, Python, OpenJDK...).<br>3. Quản trị viên hệ thống điều chỉnh các thông số và cập nhật danh sách Docker Images hỗ trợ.<br>4. Quản trị viên hệ thống chọn "Lưu cấu hình".<br>5. Hệ thống kiểm tra tính hợp lệ của các thông số an toàn.<br>6. Hệ thống cập nhật cấu hình vào CSDL và gửi tín hiệu đồng bộ đến Sandbox Grader Workers.<br>7. Hệ thống thông báo "Cấu hình Docker Sandbox thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn "Khôi phục mặc định": Hệ thống tải lại cấu hình an toàn khuyến nghị ban đầu.<br>4b. Quản trị viên hệ thống chọn "Chạy thử nghiệm Sandbox": Hệ thống khởi tạo container thử nghiệm, chạy một đoạn code mẫu và hiển thị kết quả kiểm tra cách ly. |
| **Luồng tương tác ngoại lệ** | E1 - Thông số cấu hình vượt ngưỡng an toàn của máy chủ (bước 5): Hệ thống cảnh báo "Thông số cấu hình vượt quá tài nguyên vật lý khả dụng."<br>E2 - Docker Daemon không phản hồi hoặc mất kết nối (bước 6): Hệ thống thông báo "Không thể kết nối đến Docker Host."<br>E3 - Lỗi lưu cấu hình (bước 6): Hệ thống thông báo "Cấu hình Docker Sandbox thất bại." |

---

| Mã usecase | UC-45 |
| :---- | :---- |
| **Tên usecase** | Giám sát Docker Sandbox |
| **Mô tả** | Cho phép Quản trị viên hệ thống theo dõi trực tiếp trạng thái các container thực thi mã nguồn, tải tài nguyên (CPU/RAM) và can thiệp dừng các phiên chạy lỗi hoặc treo vô hạn. |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập; dịch vụ Docker Sandbox đang chạy. |
| **Hậu điều kiện** | Thông tin giám sát thời gian thực được hiển thị; nếu thực hiện lệnh dừng phiên, container bị hủy an toàn, ghi nhận log và không ảnh hưởng đến cấu hình chung của hệ thống. |
| **Luồng tương tác chính** | 1. Quản trị viên hệ thống truy cập mục "Giám sát Docker Sandbox".<br>2. Hệ thống hiển thị Dashboard thời gian thực gồm: Số lượng container đang chạy, Số tác vụ trong hàng đợi, Tỷ lệ sử dụng CPU/RAM của Grader Worker Pool, Biểu đồ throughput chấm bài.<br>3. Hệ thống hiển thị danh sách các phiên thực thi đang hoạt động (Container ID, Submission ID, Ngôn ngữ, Thời gian chạy, Bộ nhớ chiếm dụng).<br>4. Quản trị viên hệ thống theo dõi và phát hiện các container bất thường (chạy quá lâu hoặc chiếm dụng tài nguyên cao). |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn một phiên để xem nhật ký container (Container Logs): Hệ thống hiển thị log chi tiết của container.<br>4b. Quản trị viên hệ thống can thiệp dừng phiên thực thi (Kill Container): Quản trị viên hệ thống chọn container bất thường và bấm "Dừng phiên"; hệ thống yêu cầu xác nhận, gửi lệnh hủy container ngay lập tức, cập nhật Submission liên quan thành SYSTEM_ERROR và ghi nhận sự kiện vào System Logs. |
| **Luồng tương tác ngoại lệ** | E1 - Không thể kết nối dịch vụ giám sát Docker (bước 2): Hệ thống thông báo "Mất kết nối với Docker Monitoring Daemon."<br>E2 - Lệnh hủy container thất bại do container đã tự kết thúc trước đó (bước 4b): Hệ thống làm mới danh sách và thông báo "Phiên thực thi đã kết thúc." |

> 🔴 **[ĐÃ SỬA TẠI UC-45]**: Điều chỉnh hậu điều kiện: Thao tác hủy container dừng phiên thực thi lỗi được mô tả rõ ràng, không mâu thuẫn với cam kết bảo toàn cấu hình hệ thống.

---

| Mã usecase | UC-46 |
| :---- | :---- |
| **Tên usecase** | Quản lý tổ chức |
| **Mô tả** | Cho phép Quản trị viên hệ thống quản lý danh sách các trường học, khoa, tổ chức sử dụng nền tảng (tạo mới, chỉnh sửa thông tin, khóa/mở khóa hoặc xóa tổ chức). |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập và có quyền quản trị Multi-tenant/Tổ chức. |
| **Hậu điều kiện** | Thông tin tổ chức được tạo mới, cập nhật hoặc điều chỉnh trạng thái thành công trong cơ sở dữ liệu. |
| **Luồng tương tác chính** | 1. Quản trị viên hệ thống truy cập mục "Quản lý tổ chức".<br>2. Hệ thống hiển thị danh sách các tổ chức/trường học hiện có trên nền tảng.<br>3. Quản trị viên hệ thống chọn thao tác: "Tạo tổ chức mới", "Chỉnh sửa tổ chức", "Khóa/Mở khóa" hoặc "Xóa tổ chức".<br>4. Quản trị viên hệ thống nhập thông tin tổ chức (Tên tổ chức, Mã định danh, Tên miền, Thông tin liên hệ, Gói dung lượng) hoặc xác nhận thay đổi trạng thái.<br>5. Hệ thống kiểm tra tính hợp lệ và tính duy nhất của Mã tổ chức/Tên miền.<br>6. Hệ thống cập nhật thông tin vào cơ sở dữ liệu.<br>7. Hệ thống thông báo thao tác thành công và cập nhật lại danh sách tổ chức. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn "Hủy": Hệ thống đóng biểu mẫu và giữ nguyên trạng thái cũ.<br>4b. Quản trị viên hệ thống chỉ định Quản trị viên cho tổ chức: Hệ thống tạo hoặc gán tài khoản Quản trị viên quản lý tổ chức đó. |
| **Luồng tương tác ngoại lệ** | E1 - Mã hoặc tên tổ chức đã tồn tại (bước 5): Hệ thống thông báo "Mã hoặc tên tổ chức đã tồn tại."<br>E2 - Tổ chức đang có nhiều lớp học và người dùng hoạt động không thể xóa trực tiếp (bước 5): Hệ thống thông báo "Tổ chức đang có dữ liệu hoạt động, chỉ được phép Khóa/Vô hiệu hóa thay vì xóa hoàn toàn."<br>E3 - Lỗi lưu CSDL (bước 6): Hệ thống thông báo "Quản lý tổ chức thất bại." |

---

| Mã usecase | UC-47 |
| :---- | :---- |
| **Tên usecase** | Quản lý System Logs |
| **Mô tả** | Cho phép Quản trị viên hệ thống tra cứu, lọc, xem chi tiết và xuất nhật ký hoạt động (Audit Logs, Security Logs, Error Logs) của toàn bộ hệ thống. |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập và có quyền truy cập nhật ký bảo mật hệ thống. |
| **Hậu điều kiện** | Thông tin nhật ký hệ thống được hiển thị chính xác theo bộ lọc; dữ liệu nhật ký là bất biến (Read-only) và không bị sửa đổi. |
| **Luồng tương tác chính** | 1. Quản trị viên hệ thống truy cập mục "Quản lý System Logs".<br>2. Hệ thống truy vấn và hiển thị danh sách các sự kiện mới nhất gồm: Timestamp, User ID / IP Address, Loại sự kiện (AUTH, CRUD, EXEC, ERROR), Mức độ nghiêm trọng (INFO, WARN, ERROR, CRITICAL), Hành động và Trạng thái.<br>3. Quản trị viên hệ thống tìm kiếm theo từ khóa hoặc lọc theo Khoảng thời gian, Mức độ lỗi, Tác nhân.<br>4. Hệ thống xử lý bộ lọc và hiển thị danh sách nhật ký phù hợp.<br>5. Quản trị viên hệ thống chọn một dòng sự kiện để xem chi tiết Payload, Stack Trace và Request Headers. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn "Xuất Logs": Quản trị viên hệ thống chọn định dạng (CSV / JSON) và khoảng thời gian; hệ thống kết xuất tệp nhật ký an toàn và cung cấp liên kết tải về. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy bản ghi nhật ký phù hợp với bộ lọc (bước 4): Hệ thống hiển thị danh sách rỗng và thông báo "Không có sự kiện nào khớp với điều kiện tìm kiếm."<br>E2 - Lỗi truy vấn dịch vụ Logging (bước 2, 4): Hệ thống thông báo "Không thể tải nhật ký hệ thống, vui lòng thử lại sau." |

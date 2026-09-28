| Mã usecase | UC-01 |
| :---- | :---- |
| **Tên usecase** | Đăng nhập |
| **Mô tả** | Cho phép người dùng xác thực tài khoản để bắt đầu phiên làm việc trên hệ thống. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống. |
| **Tiền điều kiện** | Người dùng đã có tài khoản trong hệ thống. |
| **Hậu điều kiện** | Phiên đăng nhập được tạo thành công. Hệ thống cấp token xác thực và chuyển người dùng đến trang chính phù hợp với vai trò. Nếu đăng nhập thất bại, phiên đăng nhập không được tạo và dữ liệu biểu mẫu vẫn được giữ để người dùng thử lại. |
| **Luồng tương tác chính** | Người dùng truy cập trang đăng nhập. Hệ thống hiển thị biểu mẫu yêu cầu Email và Mật khẩu. Người dùng nhập thông tin tài khoản và chọn "Đăng nhập". Hệ thống kiểm tra định dạng dữ liệu và tìm tài khoản tương ứng. Hệ thống đối chiếu mật khẩu với mật khẩu đã được băm trong cơ sở dữ liệu, đồng thời kiểm tra trạng thái tài khoản. Hệ thống tạo phiên đăng nhập và cấp access_token cùng refresh_token. Hệ thống chuyển người dùng đến trang chính tương ứng với vai trò: Sinh viên, Giáo viên, Quản trị viên hoặc Quản trị viên hệ thống. |
| **Luồng tương tác thay thế** | 7a. Người dùng đã truy cập một trang yêu cầu đăng nhập trước đó:  Hệ thống chuyển người dùng về trang được yêu cầu ban đầu thay vì trang chính. |
| **Luồng tương tác ngoại lệ** | E1 - Thông tin đăng nhập không hợp lệ:  Hệ thống thông báo "Email hoặc mật khẩu không chính xác." và giữ nguyên biểu mẫu. E2 - Tài khoản bị khóa hoặc vô hiệu hóa:  Hệ thống thông báo "Tài khoản đã bị khóa hoặc vô hiệu hóa." E3 - Lỗi hệ thống:  Hệ thống thông báo "Đăng nhập thất bại, vui lòng thử lại sau." |

| Mã usecase | UC-02 |
| :---- | :---- |
| **Tên usecase** | Đăng xuất |
| **Mô tả** | Cho phép người dùng kết thúc phiên làm việc hiện tại trên hệ thống. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống. |
| **Tiền điều kiện** | Người dùng đang có phiên đăng nhập hợp lệ. |
| **Hậu điều kiện** | Phiên đăng nhập của người dùng được kết thúc. Các thông tin xác thực cục bộ được xóa và người dùng được chuyển về trang đăng nhập. |
| **Luồng tương tác chính** | Người dùng chọn "Đăng xuất" trên thanh điều hướng. Hệ thống hiển thị yêu cầu xác nhận đăng xuất. Người dùng xác nhận yêu cầu. Hệ thống thu hồi hoặc đưa refresh_token vào danh sách vô hiệu hóa nếu cơ chế này được cấu hình. Hệ thống xóa token xác thực được lưu trên trình duyệt. Hệ thống kết thúc phiên đăng nhập và chuyển người dùng về trang login. |
| **Luồng tương tác thay thế** | 3a. Người dùng hủy xác nhận:  Hệ thống đóng hộp thoại và giữ nguyên phiên đăng nhập. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập đã hết hạn:  Hệ thống xóa thông tin xác thực cục bộ và chuyển người dùng về trang /login |

| Mã usecase | UC-03 |
| :---- | :---- |
| **Tên usecase** | Quên mật khẩu |
| **Mô tả** | Cho phép người dùng xác thực quyền sở hữu tài khoản và đặt lại mật khẩu khi không nhớ mật khẩu hiện tại. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống. |
| **Tiền điều kiện** | Người dùng đang ở trang đăng nhập và có quyền truy cập địa chỉ email đã đăng ký. |
| **Hậu điều kiện** | Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu. Các mã hoặc liên kết khôi phục đã sử dụng bị vô hiệu hóa. Nếu khôi phục thất bại, mật khẩu hiện tại vẫn được giữ nguyên. |
| **Luồng tương tác chính** | Người dùng chọn "Quên mật khẩu" tại trang đăng nhập. Hệ thống hiển thị biểu mẫu yêu cầu nhập email tài khoản. Người dùng nhập email và chọn "Gửi yêu cầu". Hệ thống kiểm tra định dạng email và tạo mã OTP hoặc liên kết đặt lại mật khẩu có thời hạn. Hệ thống gửi mã hoặc liên kết xác thực đến email của người dùng và thông báo đã gửi yêu cầu. Người dùng sử dụng mã hoặc liên kết nhận được để mở biểu mẫu đặt lại mật khẩu. Người dùng nhập mật khẩu mới, xác nhận mật khẩu và chọn "Cập nhật mật khẩu". Hệ thống kiểm tra mã hoặc liên kết còn hợp lệ, đồng thời kiểm tra mật khẩu mới. Hệ thống băm mật khẩu mới, cập nhật vào cơ sở dữ liệu và vô hiệu hóa mã hoặc liên kết đã sử dụng. Hệ thống thông báo "Khôi phục mật khẩu thành công." và chuyển người dùng về trang đăng nhập. |
| **Luồng tương tác thay thế** | 5a. Người dùng không nhận được email:  Người dùng yêu cầu gửi lại mã hoặc liên kết khi thời gian chờ cho phép; hệ thống cấp thông tin xác thực mới. |
| **Luồng tương tác ngoại lệ** | E1 - Email không tồn tại hoặc không hợp lệ:  Hệ thống thông báo yêu cầu không thể thực hiện và không tiết lộ thông tin tài khoản tồn tại. E2 - Mã hoặc liên kết hết hạn hoặc không hợp lệ:  Hệ thống thông báo "Mã hoặc liên kết khôi phục không hợp lệ hoặc đã hết hạn." E3 - Mật khẩu mới không đạt yêu cầu:  Hệ thống thông báo "Mật khẩu mới không hợp lệ hoặc không trùng khớp." E4 - Lỗi gửi email hoặc lỗi lưu dữ liệu:  Hệ thống thông báo "Không thể khôi phục mật khẩu, vui lòng thử lại sau." |

| Mã usecase | UC-04 |
| :---- | :---- |
| **Tên usecase** | Xem thông tin cá nhân |
| **Mô tả** | Cho phép người dùng xem thông tin cá nhân đã lưu trong hệ thống. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống. |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Thông tin cá nhân hiện tại của người dùng được hiển thị; dữ liệu trong cơ sở dữ liệu không bị thay đổi. |
| **Luồng tương tác chính** | Người dùng truy cập trang cá nhân. Hệ thống xác thực phiên đăng nhập và quyền truy cập của người dùng. Hệ thống truy vấn thông tin cá nhân từ cơ sở dữ liệu. Hệ thống hiển thị các thông tin được phép xem, như họ tên, email, số điện thoại, ảnh đại diện và vai trò của người dùng. |
| **Luồng tương tác thay thế** | 3a. Người dùng tải lại trang:  Hệ thống truy vấn lại dữ liệu mới nhất từ cơ sở dữ liệu và hiển thị thông tin cập nhật. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống thông báo yêu cầu đăng nhập và chuyển người dùng về trang /login. E2 - Không tìm thấy thông tin cá nhân:  Hệ thống thông báo "Không tìm thấy thông tin cá nhân." E3 - Lỗi truy vấn dữ liệu:  Hệ thống thông báo "Không thể tải thông tin cá nhân, vui lòng thử lại sau." |

| Mã usecase | UC-05 |
| :---- | :---- |
| **Tên usecase** | Cập nhật thông tin cá nhân |
| **Mô tả** | Cho phép người dùng chỉnh sửa và lưu các thông tin cá nhân được hệ thống cho phép cập nhật. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống. |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. Thông tin cá nhân của người dùng đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Thông tin hợp lệ được cập nhật và lưu vào cơ sở dữ liệu. Nếu cập nhật thất bại, thông tin cũ được giữ nguyên và hệ thống hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | Người dùng truy cập trang cá nhân. Hệ thống xác thực phiên đăng nhập và hiển thị thông tin hiện tại. Người dùng chọn "Chỉnh sửa". Hệ thống hiển thị biểu mẫu với các trường được phép cập nhật, như họ tên, số điện thoại và ảnh đại diện. Người dùng chỉnh sửa thông tin và chọn "Lưu thay đổi". Hệ thống kiểm tra tính hợp lệ của dữ liệu. Hệ thống cập nhật thông tin vào cơ sở dữ liệu. Hệ thống thông báo "Cập nhật thông tin cá nhân thành công." và hiển thị dữ liệu mới. |
| **Luồng tương tác thay thế** | 5a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác chỉnh sửa và giữ nguyên thông tin hiện tại. 5b. Người dùng không thay đổi thông tin:  Hệ thống không thực hiện cập nhật và giữ nguyên dữ liệu hiện tại. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống thông báo yêu cầu đăng nhập và chuyển người dùng về trang đăng nhập. E2 - Thông tin không hợp lệ:  Hệ thống thông báo "Thông tin cá nhân không hợp lệ." và giữ lại dữ liệu người dùng đã nhập để chỉnh sửa. E3 - Dữ liệu đã được cập nhật ở nơi khác:  Hệ thống thông báo "Thông tin đã được cập nhật, vui lòng tải lại dữ liệu." và không ghi đè dữ liệu mới. E4 - Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Cập nhật thông tin cá nhân thất bại." |

| Mã usecase | UC-06 |
| :---- | :---- |
| **Tên usecase** | Đổi mật khẩu |
| **Mô tả** | Cho phép người dùng thay đổi mật khẩu hiện tại sau khi xác thực mật khẩu cũ. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống. |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. Người dùng biết mật khẩu hiện tại. |
| **Hậu điều kiện** | Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu. Các phiên hoặc token cũ được xử lý theo chính sách bảo mật của hệ thống. Nếu đổi mật khẩu thất bại, mật khẩu cũ vẫn được giữ nguyên. |
| **Luồng tương tác chính** | Người dùng truy cập chức năng "Đổi mật khẩu" trong trang cá nhân. Hệ thống hiển thị biểu mẫu gồm Mật khẩu hiện tại, Mật khẩu mới và Xác nhận mật khẩu mới. Người dùng nhập đầy đủ thông tin và chọn "Đổi mật khẩu". Hệ thống xác thực phiên đăng nhập và đối chiếu mật khẩu hiện tại. Hệ thống kiểm tra mật khẩu mới đạt chính sách bảo mật và trùng với phần xác nhận. Hệ thống băm mật khẩu mới và lưu vào cơ sở dữ liệu. Hệ thống thông báo "Đổi mật khẩu thành công." |
| **Luồng tương tác thay thế** | 3a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác và giữ nguyên mật khẩu hiện tại. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống yêu cầu người dùng đăng nhập lại. E2 - Mật khẩu hiện tại không chính xác:  Hệ thống thông báo "Mật khẩu hiện tại không chính xác." E3 - Mật khẩu mới không hợp lệ:  Hệ thống thông báo "Mật khẩu mới không đáp ứng yêu cầu bảo mật hoặc không trùng khớp." E4 - Mật khẩu mới trùng mật khẩu hiện tại:  Hệ thống thông báo "Mật khẩu mới phải khác mật khẩu hiện tại." E5 - Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Đổi mật khẩu thất bại." |

| Mã usecase | UC-07 |
| :---- | :---- |
| **Tên usecase** | Xem danh sách bài tập |
| **Mô tả** | Cho phép Sinh viên xem và tra cứu danh sách các bài tập được giao cho những lớp mà mình tham gia |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Danh sách bài tập phù hợp được hiển thị; dữ liệu bài tập không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên truy cập mục "Bài tập". Hệ thống xác thực phiên đăng nhập và quyền truy cập của Sinh viên. Hệ thống lấy danh sách lớp, môn học hoặc chủ đề mà Sinh viên đang tham gia. Hệ thống truy vấn các bài tập được giao cho Sinh viên theo những lớp hoặc môn học đó. Hệ thống hiển thị danh sách với các thông tin: Tên bài, lớp/chủ đề, độ khó, thời hạn nộp, trạng thái làm bài và điểm cao nhất nếu đã có kết quả. Sinh viên tìm kiếm hoặc lọc danh sách theo lớp, chủ đề hoặc trạng thái. |
| **Luồng tương tác thay thế** | 6a. Sinh viên không chọn bộ lọc:  Hệ thống hiển thị toàn bộ bài tập mà Sinh viên được phép xem. 6b. Không có bài tập phù hợp:  Hệ thống hiển thị danh sách rỗng và thông báo phù hợp. |
| **Luồng tương tác ngoại lệ** | E1 - Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống yêu cầu Sinh viên đăng nhập lại. E2 - Lỗi truy vấn dữ liệu:  Hệ thống thông báo "Không thể tải danh sách bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-08 |
| :---- | :---- |
| **Tên usecase** | Xem chi tiết bài tập |
| **Mô tả** | Cho phép Sinh viên xem nội dung và yêu cầu chi tiết của một bài tập được giao. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. Bài tập tồn tại trong hệ thống. |
| **Hậu điều kiện** | Thông tin bài tập được hiển thị nếu Sinh viên có quyền truy cập. Nếu Sinh viên chọn làm bài, hệ thống chuyển đến giao diện soạn thảo tương ứng. |
| **Luồng tương tác chính** | Sinh viên chọn một bài tập từ danh sách. Hệ thống kiểm tra Sinh viên có thuộc lớp được giao bài tập và bài tập có được phép truy cập hay không. Hệ thống lấy thông tin bài tập từ cơ sở dữ liệu. Hệ thống hiển thị đề bài, hỗ trợ Markdown và công thức toán học LaTeX nếu có. Hệ thống hiển thị yêu cầu Input/Output, ràng buộc, giới hạn thời gian, giới hạn bộ nhớ, Sample Test Cases và Rubric được công khai. Sinh viên chọn "Làm bài". Hệ thống chuyển Sinh viên đến giao diện làm bài và tải cấu hình cần thiết. |
| **Luồng tương tác thay thế** | 6a. Sinh viên quay lại danh sách:  Hệ thống không tạo hoặc thay đổi bài làm và đưa Sinh viên về danh sách bài tập. 6b. Bài tập đã quá hạn nhưng cho phép nộp muộn hoặc cho phép xem lại:  Hệ thống hiển thị cảnh báo về chính sách nộp muộn/xem lại và vẫn cho phép xem đề bài cũng như bấm "Làm bài". |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại:  Hệ thống thông báo "Không tìm thấy bài tập." E2 - Sinh viên không có quyền truy cập:  Hệ thống thông báo "Bạn không có quyền truy cập bài tập này." E3 - Bài tập chưa mở hoặc đã đóng hoàn toàn:  Hệ thống thông báo "Bài tập hiện không khả dụng." E4 - Lỗi tải dữ liệu:  Hệ thống thông báo "Không thể tải chi tiết bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-09 |
| :---- | :---- |
| **Tên usecase** | Viết code |
| **Mô tả** | Cho phép Sinh viên viết và chỉnh sửa mã nguồn trực tiếp trong trình soạn thảo của hệ thống. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có quyền truy cập bài tập. Bài tập có cấu hình ngôn ngữ lập trình được phép sử dụng. |
| **Hậu điều kiện** | Mã nguồn của Sinh viên được hiển thị và bản nháp gần nhất được lưu theo cơ chế autosave. Bài làm chưa được xem là submission chính thức cho đến khi Sinh viên chọn "Nộp bài". |
| **Luồng tương tác chính** | Sinh viên chọn "Làm bài" từ trang chi tiết bài tập. Hệ thống tải đề bài, ngôn ngữ và cấu hình bài tập. Hệ thống mở Monaco Editor với template code phù hợp. Sinh viên nhập hoặc chỉnh sửa mã nguồn. Hệ thống kiểm tra cơ bản nội dung editor và tự động lưu bản nháp theo khoảng thời gian được cấu hình. Sinh viên tiếp tục chỉnh sửa, hoàn thiện bài làm và chuyển sang bước nộp bài. |
| **Luồng tương tác thay thế** | 4a. Sinh viên tải lại trang:  Hệ thống khôi phục bản nháp gần nhất nếu bản nháp tồn tại. 6a. Sinh viên rời khỏi trang:  Hệ thống lưu bản nháp trước khi rời trang nếu kết nối còn hoạt động. |
| **Luồng tương tác ngoại lệ** | E1 - Không tải được cấu hình bài tập:  Hệ thống thông báo "Không thể mở trình soạn thảo cho bài tập này." E2 - Mã nguồn không hợp lệ hoặc vượt giới hạn:  Hệ thống thông báo lỗi và yêu cầu Sinh viên chỉnh sửa mã nguồn. E3 - Lỗi lưu bản nháp:  Hệ thống thông báo "Không thể lưu bản nháp, vui lòng kiểm tra kết nối mạng." |

| Mã usecase | UC-10 |
| :---- | :---- |
| **Tên usecase** | Tải tệp bài làm lên |
| **Mô tả** | Cho phép Sinh viên tải mã nguồn từ máy tính vào bài làm đang mở. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã mở giao diện làm bài và có quyền truy cập bài tập. File mã nguồn có phần mở rộng thuộc danh sách ngôn ngữ được bài tập cho phép. |
| **Hậu điều kiện** | Nội dung file hợp lệ được nạp vào Monaco Editor và có thể được chỉnh sửa tiếp. File upload không được xem là submission chính thức cho đến khi Sinh viên nộp bài. |
| **Luồng tương tác chính** | Sinh viên chọn "Upload File" tại màn hình làm bài. Hệ thống hiển thị giao diện chọn file. Sinh viên chọn file mã nguồn từ máy tính. Hệ thống kiểm tra phần mở rộng, kích thước và nội dung cơ bản của file. Hệ thống đọc file và nạp nội dung vào Monaco Editor. Hệ thống lưu bản nháp của nội dung đã nạp. Hệ thống thông báo "Tải file lên thành công." |
| **Luồng tương tác thay thế** | 3a. Sinh viên hủy chọn file:  Hệ thống đóng hộp thoại và giữ nguyên nội dung đang có trong editor. 5a. Sinh viên tiếp tục chỉnh sửa:  Hệ thống cập nhật nội dung editor và lưu theo cơ chế autosave. |
| **Luồng tương tác ngoại lệ** | E1 - Định dạng file không được hỗ trợ:  Hệ thống thông báo "Định dạng file không được hỗ trợ." E2 - File vượt quá kích thước cho phép:  Hệ thống thông báo "Kích thước file vượt quá giới hạn cho phép." E3 - Không thể đọc file:  Hệ thống thông báo "Không thể tải file, vui lòng chọn file khác." |

| Mã usecase | UC-11 |
| :---- | :---- |
| **Tên usecase** | Nộp bài |
| **Mô tả** | Cho phép Sinh viên gửi mã nguồn để hệ thống chấm chính thức và lưu kết quả bài làm. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có quyền làm bài. Bài tập còn hạn nộp hoặc cho phép nộp muộn. Sinh viên đã nhập mã nguồn. |
| **Hậu điều kiện** | Một bài nộp được tạo và lưu với trạng thái xử lý tương ứng. Kết quả Auto-Grader và AI feedback được lưu khi quá trình chấm hoàn tất. Nếu không thể tiếp nhận bài, hệ thống sẽ không tạo bài nộp không đầy đủ. |
| **Luồng tương tác chính** | Sinh viên kiểm tra mã nguồn và chọn "Nộp bài". Hệ thống kiểm tra quyền nộp, thời hạn, ngôn ngữ và dữ liệu bài nộp. Web Client gửi trực tiếp mã nguồn cùng thông tin bài tập đến API nộp bài mà không qua bước chạy thử trước. Backend tạo bài nộp với trạng thái PENDING và đưa tác vụ vào hàng đợi xử lý. Hệ thống trả về mã bài nộp (submission ID) và hiển thị trạng thái "Đang chấm bài...". Grader Worker lấy tác vụ, gửi mã nguồn và toàn bộ Hidden Test Cases đến Docker Sandbox. Docker Sandbox biên dịch nếu cần, thực thi code cách ly và trả về execution evidence gồm output, lỗi, thời gian chạy, bộ nhớ và trạng thái từng test. Hệ thống thực hiện Auto-Grading, phân tích tĩnh nếu được cấu hình và tính điểm theo Rubric. Hệ thống lưu kết quả chấm vào cơ sở dữ liệu. AI Engine tạo feedback dựa trên đề bài, mã nguồn và kết quả chấm; hệ thống lưu feedback nếu tác vụ thành công. Hệ thống cập nhật trạng thái bài nộp thành COMPLETED hoặc trạng thái lỗi tương ứng. Hệ thống thông báo trạng thái cho Sinh viên qua WebSocket hoặc polling. |
| **Luồng tương tác thay thế** | 2a. Sinh viên xác nhận nộp bài muộn:  Hệ thống tiếp nhận bài nộp và áp dụng quy định phạt điểm nếu bài tập cho phép nộp muộn. 5a. Sinh viên rời khỏi trang:  Hệ thống tiếp tục xử lý bài nộp; Sinh viên có thể xem trạng thái từ lịch sử làm bài. |
| **Luồng tương tác ngoại lệ** | E1 - Hết hạn nộp bài:  Hệ thống thông báo "Đã hết hạn nộp bài." E2 - Mã nguồn không hợp lệ:  Hệ thống thông báo "Bài nộp không hợp lệ." E3 - Không thể đưa tác vụ vào hàng đợi:  Hệ thống thông báo "Không thể tiếp nhận bài nộp, vui lòng thử lại sau." E4 - Lỗi khi chấm bài:  Hệ thống cập nhật bài nộp (submission) ở trạng thái lỗi và thông báo "Chấm bài thất bại, vui lòng thử lại sau." |

| Mã usecase | UC-12 |
| :---- | :---- |
| **Tên usecase** | Xem kết quả Auto-Grader |
| **Mô tả** | Cho phép Sinh viên xem kết quả chấm tự động của một bài nộp. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và bài nộp thuộc về Sinh viên. |
| **Hậu điều kiện** | Kết quả Auto-Grader được hiển thị; dữ liệu chấm không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên mở một bài nộp từ lịch sử làm bài hoặc trang kết quả. Hệ thống kiểm tra quyền truy cập bài nộp. Hệ thống lấy kết quả Auto-Grader. Hệ thống hiển thị điểm số, trạng thái tổng quát và thời gian chấm. Hệ thống hiển thị trạng thái từng test case, thời gian thực thi, mức sử dụng bộ nhớ và lỗi nếu có (dữ liệu Input/Output của Hidden Test Cases được bảo mật và ẩn khỏi Sinh viên). Sinh viên xem chi tiết kết quả chấm bài. |
| **Luồng tương tác thay thế** | 4a. Bài nộp (submission) đang được xử lý:  Hệ thống hiển thị trạng thái PENDING hoặc RUNNING và cho phép Sinh viên tải lại kết quả. |
| **Luồng tương tác ngoại lệ** | E1 - Bài nộp không tồn tại:  Hệ thống thông báo "Không tìm thấy bài nộp." E2 - Sinh viên không có quyền truy cập:  Hệ thống từ chối yêu cầu và không hiển thị dữ liệu bài nộp. E3 - Chưa có kết quả chấm:  Hệ thống thông báo "Kết quả chấm bài chưa sẵn sàng." |

| Mã usecase | UC-13 |
| :---- | :---- |
| **Tên usecase** | Xem nhận xét AI |
| **Mô tả** | Cho phép Sinh viên xem nhận xét do AI tạo ra dựa trên bài làm và kết quả chấm. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và bài nộp thuộc về Sinh viên. Bài nộp đã có kết quả chấm hoặc đủ dữ liệu để tạo feedback. |
| **Hậu điều kiện** | Nhận xét AI được hiển thị nếu đã được tạo; dữ liệu bài nộp không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên mở trang kết quả của một bài nộp. Hệ thống kiểm tra quyền truy cập và trạng thái AI feedback. Hệ thống lấy nhận xét AI đã lưu. Hệ thống hiển thị nhận xét về lỗi, chất lượng mã nguồn, độ phức tạp và đề xuất cải thiện nếu có. Sinh viên xem và sử dụng nhận xét để cải thiện bài làm. |
| **Luồng tương tác thay thế** | 3a. AI feedback đang được tạo:  Hệ thống hiển thị trạng thái chờ và cập nhật khi feedback sẵn sàng. 3b. AI feedback chưa được bật cho bài tập:  Hệ thống thông báo tính năng không khả dụng cho bài nộp này. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy bài nộp:  Hệ thống thông báo "Không tìm thấy bài nộp." E2 - Sinh viên không có quyền truy cập:  Hệ thống từ chối yêu cầu xem feedback. E3 - AI Service gặp lỗi:  Hệ thống thông báo "Chưa thể tạo nhận xét AI, vui lòng thử lại sau." |

| Mã usecase | UC-14 |
| :---- | :---- |
| **Tên usecase** | Tương tác với AI Tutor |
| **Mô tả** | Cho phép Sinh viên trao đổi với AI Tutor để nhận gợi ý định hướng giải quyết bài tập theo phương pháp Socratic. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập. Sinh viên đang xem bài tập, bài làm hoặc kết quả bài nộp. |
| **Hậu điều kiện** | Câu hỏi và câu trả lời được hiển thị trong phiên hội thoại. Lịch sử hội thoại được lưu theo chính sách của hệ thống nếu chức năng lưu được bật. |
| **Luồng tương tác chính** | Sinh viên mở "AI Tutor" tại màn hình bài tập, IDE hoặc kết quả bài nộp. Hệ thống lấy context cần thiết gồm đề bài, mã nguồn, kết quả test và câu hỏi trước đó trong hội thoại. Sinh viên nhập câu hỏi và chọn "Gửi". Hệ thống kiểm tra câu hỏi, quyền truy cập context và giới hạn sử dụng. Backend gửi prompt kèm guardrails sư phạm đến AI Engine. AI Tutor phân tích context và tạo câu trả lời mang tính gợi mở, không cung cấp ngay toàn bộ lời giải nếu chính sách không cho phép. Hệ thống hiển thị câu trả lời trong khung hội thoại. Sinh viên tiếp tục đặt câu hỏi trong cùng phiên. |
| **Luồng tương tác thay thế** | 2a. Sinh viên không chọn bài làm hoặc bài nộp:  Hệ thống chỉ gửi context của đề bài và các thông tin được phép xem. 8a. Sinh viên bắt đầu hội thoại mới:  Hệ thống xóa context hội thoại trước khỏi phiên hiện tại và khởi tạo phiên mới. |
| **Luồng tương tác ngoại lệ** | E1 - Câu hỏi rỗng hoặc vượt giới hạn:  Hệ thống yêu cầu Sinh viên nhập câu hỏi hợp lệ. E2 - AI Service không khả dụng:  Hệ thống thông báo "AI Tutor hiện không khả dụng, vui lòng thử lại sau." E3 - Nội dung yêu cầu không phù hợp chính sách:  Hệ thống từ chối yêu cầu và hiển thị thông báo phù hợp. |

| Mã usecase | UC-15 |
| :---- | :---- |
| **Tên usecase** | Xem lịch sử làm bài |
| **Mô tả** | Cho phép Sinh viên tra cứu các bài nộp của mình và xem chi tiết từng lần nộp bài. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Lịch sử bài nộp của Sinh viên được hiển thị; dữ liệu bài nộp không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên truy cập mục "Lịch sử làm bài" hoặc lịch sử nộp bài của một bài tập. Hệ thống xác thực phiên đăng nhập. Hệ thống truy vấn các bài nộp thuộc về Sinh viên. Hệ thống sắp xếp lịch sử theo thời gian và hiển thị bài tập, thời điểm nộp, trạng thái, điểm và ngôn ngữ. Sinh viên chọn một bài nộp để xem mã nguồn, kết quả test và feedback được phép xem. |
| **Luồng tương tác thay thế** | 4a. Sinh viên lọc lịch sử:  Hệ thống lọc theo bài tập, lớp, trạng thái hoặc khoảng thời gian. 5a. Sinh viên chọn hai bài nộp:  Hệ thống hiển thị phần khác nhau giữa các phiên bản nếu chức năng so sánh được hỗ trợ. |
| **Luồng tương tác ngoại lệ** | E1 - Không có lịch sử bài nộp:  Hệ thống hiển thị danh sách rỗng và thông báo "Chưa có bài nộp nào." E2 - Lỗi truy vấn dữ liệu:  Hệ thống thông báo "Không thể tải lịch sử làm bài, vui lòng thử lại sau." |

| Mã usecase | UC-16 |
| :---- | :---- |
| **Tên usecase** | Xem bảng điểm cá nhân |
| **Mô tả** | Cho phép Sinh viên xem tổng hợp điểm các bài tập và lớp học mà mình tham gia. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Bảng điểm cá nhân được hiển thị theo dữ liệu kết quả đã được chấm; dữ liệu điểm không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên truy cập trang "Bảng điểm". Hệ thống xác thực phiên đăng nhập. Hệ thống truy vấn các kết quả đã được chấm thuộc về Sinh viên. Hệ thống tổng hợp điểm theo bài tập và lớp học theo quy tắc đã cấu hình (ưu tiên điểm chấm thủ công của Giáo viên nếu đã được chấm, ngược lại lấy điểm Auto-Grader cao nhất). Hệ thống hiển thị bảng điểm gồm bài tập, lớp, điểm, trạng thái và thời gian cập nhật. Sinh viên xem hoặc lọc điểm theo bài tập, lớp hoặc khoảng thời gian. |
| **Luồng tương tác thay thế** | 6a. Sinh viên không chọn bộ lọc:  Hệ thống hiển thị toàn bộ bảng điểm mà Sinh viên được phép xem. 6b. Một số bài chưa có điểm cuối:  Hệ thống hiển thị trạng thái đang chờ chấm hoặc chưa có kết quả thay vì tự động coi là điểm 0. |
| **Luồng tương tác ngoại lệ** | E1 - Không có kết quả đã chấm:  Hệ thống hiển thị bảng điểm rỗng và thông báo "Chưa có kết quả được chấm." E2 - Lỗi tổng hợp điểm:  Hệ thống thông báo "Không thể tải bảng điểm, vui lòng thử lại sau." |

| Mã usecase | UC-17 |
| :---- | :---- |
| **Tên usecase** | Tạo lớp học |
| **Mô tả** | Cho phép Giáo viên khởi tạo một lớp học mới do mình phụ trách. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập và có quyền quản lý lớp trong tổ chức tương ứng. |
| **Hậu điều kiện** | Lớp học hợp lệ được tạo và gắn với Giáo viên; hệ thống sinh mã tham gia nếu cần. |
| **Luồng tương tác chính** | Giáo viên truy cập quản lý lớp và chọn "Tạo lớp". Hệ thống hiển thị biểu mẫu gồm tên lớp, mã lớp, mô tả, học kỳ hoặc niên khóa. Giáo viên nhập thông tin và chọn "Tạo lớp". Hệ thống kiểm tra quyền, định dạng dữ liệu và tính duy nhất của mã lớp. Hệ thống tạo lớp, gắn Giáo viên làm người phụ trách và sinh mã tham gia nếu cần. Hệ thống thông báo "Tạo lớp thành công." và hiển thị chi tiết lớp. |
| **Luồng tương tác thay thế** | 3a. Giáo viên chọn "Hủy":  Hệ thống đóng biểu mẫu và không tạo lớp. 3b. Giáo viên không nhập mã lớp:  Hệ thống tự sinh mã theo cấu hình. |
| **Luồng tương tác ngoại lệ** | E1 - Dữ liệu không hợp lệ:  Hệ thống thông báo "Thông tin lớp học không hợp lệ." E2 - Mã lớp đã tồn tại:  Hệ thống thông báo "Mã lớp đã tồn tại, vui lòng chọn mã khác." E3 - Lỗi khi tạo lớp:  Hệ thống thông báo "Không thể tạo lớp, vui lòng thử lại sau." |

| Mã usecase | UC-18 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa lớp học |
| **Mô tả** | Cho phép Giáo viên cập nhật thông tin của lớp học do mình phụ trách. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập; lớp tồn tại và chưa bị xóa. |
| **Hậu điều kiện** | Thông tin hợp lệ của lớp được cập nhật; nếu thất bại, dữ liệu cũ được giữ nguyên. |
| **Luồng tương tác chính** | Giáo viên truy cập quản lý lớp và chọn lớp cần chỉnh sửa. Hệ thống kiểm tra quyền và hiển thị thông tin hiện tại. Giáo viên chỉnh sửa tên lớp, mô tả, học kỳ hoặc niên khóa. Giáo viên chọn "Lưu". Hệ thống kiểm tra dữ liệu và phiên bản hiện tại của lớp. Hệ thống cập nhật thông tin và thông báo "Cập nhật lớp thành công." |
| **Luồng tương tác thay thế** | 4a. Giáo viên chọn "Hủy":  Hệ thống bỏ các thay đổi chưa lưu. 4b. Giáo viên không thay đổi dữ liệu:  Hệ thống không tạo bản cập nhật mới. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy lớp:  Hệ thống thông báo "Không tìm thấy lớp học." E2 - Giáo viên không có quyền:  Hệ thống từ chối yêu cầu và không hiển thị dữ liệu lớp. E3 - Dữ liệu đã thay đổi ở nơi khác:  Hệ thống thông báo "Thông tin lớp đã thay đổi, vui lòng tải lại." |

| Mã usecase | UC-19 |
| :---- | :---- |
| **Tên usecase** | Xóa/đóng lớp |
| **Mô tả** | Cho phép Giáo viên đóng lớp khi kết thúc hoạt động hoặc xóa lớp chưa sử dụng theo chính sách. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập, có quyền quản lý và lớp học tồn tại. |
| **Hậu điều kiện** | Lớp được đóng hoặc xóa mềm; lớp đóng không còn nhận thành viên hoặc bài tập mới. |
| **Luồng tương tác chính** | Giáo viên mở chi tiết lớp cần xử lý. Giáo viên chọn "Đóng lớp" hoặc "Xóa lớp". Hệ thống hiển thị hộp thoại xác nhận và nêu ảnh hưởng đến dữ liệu liên quan. Giáo viên xác nhận thao tác. Hệ thống kiểm tra trạng thái lớp và thực hiện đóng hoặc xóa theo chính sách. Hệ thống thông báo "Xử lý lớp thành công." và cập nhật danh sách. |
| **Luồng tương tác thay thế** | 2a. Giáo viên hủy xác nhận:  Hệ thống đóng hộp thoại và giữ nguyên lớp. 5a. Lớp có dữ liệu đang hoạt động:  Hệ thống chuyển lớp sang trạng thái đóng hoặc lưu trữ thay vì xóa vật lý. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp đã đóng hoặc đã xóa:  Hệ thống thông báo "Lớp học không còn ở trạng thái có thể xử lý." E2 - Lỗi cập nhật trạng thái:  Hệ thống thông báo "Không thể cập nhật trạng thái lớp, vui lòng thử lại sau." |

| Mã usecase | UC-20 |
| :---- | :---- |
| **Tên usecase** | Quản lý sinh viên trong lớp |
| **Mô tả** | Cho phép Giáo viên thêm hoặc xóa sinh viên khỏi lớp mình phụ trách. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập, có quyền quản lý và lớp đang mở. |
| **Hậu điều kiện** | Danh sách thành viên được cập nhật theo yêu cầu hợp lệ. |
| **Luồng tương tác chính** | Giáo viên mở chi tiết lớp. Hệ thống hiển thị danh sách sinh viên hiện tại. Giáo viên chọn "Thêm sinh viên" hoặc chọn sinh viên và chọn "Xóa khỏi lớp". Với thao tác thêm, Giáo viên nhập email, mã sinh viên hoặc sử dụng mã tham gia lớp. Hệ thống kiểm tra tài khoản, tư cách thành viên và trạng thái lớp. Hệ thống cập nhật danh sách thành viên và hiển thị danh sách mới. |
| **Luồng tương tác thay thế** | 3a. Giáo viên thêm nhiều sinh viên:  Hệ thống xử lý danh sách và trả kết quả theo từng bản ghi. 3b. Giáo viên hủy thao tác xóa:  Hệ thống đóng hộp thoại và giữ nguyên thành viên. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy sinh viên:  Hệ thống thông báo "Không tìm thấy tài khoản sinh viên." E2 - Sinh viên đã là thành viên:  Hệ thống bỏ qua bản ghi trùng và thông báo kết quả. E3 - Không thể xóa sinh viên:  Hệ thống thông báo "Không thể xóa sinh viên khỏi lớp." |

| Mã usecase | UC-21 |
| :---- | :---- |
| **Tên usecase** | Tạo bài tập |
| **Mô tả** | Cho phép Giáo viên tạo bài tập mới với đề bài và cấu hình phục vụ chấm tự động. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập và có quyền quản lý bài tập. |
| **Hậu điều kiện** | Bài tập hợp lệ được tạo ở trạng thái bản nháp hoặc sẵn sàng giao; test case, deadline và rubric được lưu cùng cấu hình. |
| **Luồng tương tác chính** | Giáo viên truy cập trang quản lý bài tập và chọn "Tạo bài tập". Hệ thống hiển thị biểu mẫu tạo bài tập. Giáo viên nhập tiêu đề, mô tả bài toán bằng Markdown, yêu cầu Input/Output và ngôn ngữ được phép. Giáo viên cấu hình time limit, memory limit, thời gian mở đề, deadline và chính sách nộp muộn. Giáo viên thêm test case gồm Input, Expected Output, trạng thái sample/hidden và trọng số điểm. Giáo viên thiết lập rubric cho Correctness, Code Quality và Complexity. Giáo viên chọn "Lưu bài tập". Hệ thống kiểm tra dữ liệu và tính nhất quán của cấu hình. Hệ thống tạo bài tập và thông báo "Tạo bài tập thành công." |
| **Luồng tương tác thay thế** | 7a. Giáo viên chọn lưu bản nháp:  Hệ thống lưu bài tập ở trạng thái DRAFT và chưa cho sinh viên truy cập. 7b. Giáo viên rời biểu mẫu:  Hệ thống cảnh báo khi có thay đổi chưa lưu. |
| **Luồng tương tác ngoại lệ** | E1 - Thiếu thông tin bắt buộc:  Hệ thống thông báo "Vui lòng hoàn thiện các trường bắt buộc." E2 - Test case hoặc rubric không hợp lệ:  Hệ thống thông báo "Cấu hình test case hoặc rubric không hợp lệ." E3 - Deadline không hợp lệ:  Hệ thống thông báo "Thời gian mở đề và hạn nộp bài không hợp lệ." E4 - Lỗi khi tạo bài tập:  Hệ thống thông báo "Không thể tạo bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-22 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa bài tập |
| **Mô tả** | Cho phép Giáo viên cập nhật nội dung hoặc cấu hình của bài tập do mình quản lý. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập; bài tập tồn tại và đang ở trạng thái cho phép chỉnh sửa. |
| **Hậu điều kiện** | Nội dung và cấu hình hợp lệ được cập nhật; các bài nộp đã có không bị thay đổi ngoài chính sách phiên bản. |
| **Luồng tương tác chính** | Giáo viên mở danh sách bài tập và chọn bài cần chỉnh sửa. Hệ thống kiểm tra quyền truy cập và hiển thị thông tin bài tập. Giáo viên chỉnh sửa đề bài, ngôn ngữ, giới hạn, deadline, test case hoặc rubric. Giáo viên chọn "Lưu". Hệ thống kiểm tra dữ liệu, trạng thái bài tập và tính tương thích với bài nộp hiện có. Hệ thống cập nhật bài tập hoặc tạo phiên bản mới theo chính sách. Hệ thống thông báo "Cập nhật bài tập thành công." |
| **Luồng tương tác thay thế** | 4a. Giáo viên chọn "Hủy":  Hệ thống bỏ thay đổi chưa lưu. 5a. Bài tập đã được giao hoặc có bài nộp:  Hệ thống giới hạn trường được sửa hoặc yêu cầu xác nhận tạo phiên bản mới. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy bài tập:  Hệ thống thông báo "Không tìm thấy bài tập." E2 - Giáo viên không có quyền:  Hệ thống từ chối yêu cầu và không cho phép chỉnh sửa. E3 - Dữ liệu không hợp lệ:  Hệ thống thông báo "Thông tin bài tập không hợp lệ." E4 - Lỗi khi lưu:  Hệ thống thông báo "Không thể cập nhật bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-23 |
| :---- | :---- |
| **Tên usecase** | Xóa bài tập |
| **Mô tả** | Cho phép Giáo viên xóa hoặc vô hiệu hóa bài tập theo trạng thái và chính sách lưu trữ dữ liệu. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại. |
| **Hậu điều kiện** | Bài tập được xóa mềm, vô hiệu hóa hoặc xóa theo chính sách; bài nộp, điểm và lịch sử liên quan được giữ lại khi cần. |
| **Luồng tương tác chính** | Giáo viên mở danh sách bài tập và chọn bài cần xóa. Giáo viên chọn "Xóa". Hệ thống hiển thị yêu cầu xác nhận và thông tin về dữ liệu bị ảnh hưởng. Giáo viên xác nhận thao tác. Hệ thống kiểm tra trạng thái bài tập, quyền truy cập và dữ liệu liên quan. Hệ thống xóa hoặc vô hiệu hóa bài tập theo chính sách. Hệ thống thông báo "Xử lý bài tập thành công." và cập nhật danh sách. |
| **Luồng tương tác thay thế** | 2a. Giáo viên hủy thao tác:  Hệ thống đóng hộp thoại và giữ nguyên bài tập. 5a. Bài tập đã có bài nộp:  Hệ thống vô hiệu hóa hoặc xóa mềm thay vì xóa dữ liệu vật lý. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy bài tập:  Hệ thống thông báo "Bài tập không tồn tại hoặc đã được xử lý." E2 - Bài tập đang được sử dụng:  Hệ thống thông báo "Bài tập đang có dữ liệu liên quan và không thể xóa trực tiếp." E3 - Lỗi xử lý:  Hệ thống thông báo "Không thể xóa hoặc vô hiệu hóa bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-24 |
| :---- | :---- |
| **Tên usecase** | Thiết lập hạn nộp bài |
| **Mô tả** | Giáo viên thiết lập hoặc cập nhật thời hạn nộp bài cho một bài tập trong hệ thống. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền quản lý bài tập. Bài tập đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Hạn nộp bài của bài tập được thiết lập hoặc cập nhật thành công. Thời hạn mới được lưu vào cơ sở dữ liệu. Sinh viên được áp dụng thời hạn nộp bài mới. Nếu thiết lập không thành công, hạn nộp bài hiện tại được giữ nguyên và hệ thống hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Quản lý bài tập”. Hệ thống hiển thị danh sách bài tập do giáo viên quản lý. Giáo viên chọn bài tập cần thiết lập hạn nộp bài. Hệ thống hiển thị thông tin bài tập và hạn nộp bài hiện tại (nếu có). Giáo viên nhập hoặc chọn ngày, giờ hạn nộp bài và chính sách nộp muộn nếu có. Giáo viên chọn “Lưu”. Hệ thống kiểm tra tính hợp lệ của hạn nộp bài. Hệ thống cập nhật hạn nộp bài vào cơ sở dữ liệu. Hệ thống thông báo “Thiết lập hạn nộp bài thành công.” và hiển thị hạn nộp bài mới. |
| **Luồng tương tác thay thế** | 6a. Giáo viên chọn “Hủy”: Hệ thống hủy thao tác thiết lập hạn nộp bài và giữ nguyên hạn nộp bài hiện tại. 6b. Giáo viên không thay đổi hạn nộp bài: Hệ thống không thực hiện cập nhật và giữ nguyên hạn nộp bài hiện tại. 6c. Bài tập chưa có hạn nộp bài: Hệ thống tạo mới hạn nộp bài cho bài tập và lưu vào cơ sở dữ liệu. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Hạn nộp bài không hợp lệ: Hệ thống thông báo “Hạn nộp bài không hợp lệ.” E3 - Hạn nộp bài đã quá thời điểm hiện tại: Hệ thống thông báo “Hạn nộp bài phải lớn hơn thời điểm hiện tại.” E4 - Bài tập đã kết thúc: Hệ thống thông báo “Không thể thay đổi hạn nộp bài của bài tập đã kết thúc.” E5 - Lỗi khi lưu dữ liệu: Hệ thống thông báo “Thiết lập hạn nộp bài thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền thực hiện chức năng này.” |

| Mã usecase | UC-25 |
| :---- | :---- |
| **Tên usecase** | Thiết lập test case |
| **Mô tả** | Giáo viên thiết lập các Test Case cho một bài tập nhằm kiểm tra tính đúng đắn của chương trình do sinh viên nộp. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền quản lý bài tập. Bài tập cần thiết lập Test Case đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Các Test Case được thiết lập thành công cho bài tập. Thông tin Test Case được lưu vào cơ sở dữ liệu. Các Test Case được sử dụng để kiểm tra chương trình do sinh viên nộp. Nếu thiết lập không thành công, thông tin Test Case hiện tại được giữ nguyên và hệ thống hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Quản lý bài tập”. Hệ thống hiển thị danh sách bài tập. Giáo viên chọn bài tập cần thiết lập Test Case. Hệ thống hiển thị thông tin bài tập và danh sách Test Case hiện tại. Giáo viên chọn chức năng “Thiết lập Test Case”. Giáo viên nhập dữ liệu đầu vào, kết quả đầu ra mong đợi, phân loại Sample/Hidden và điểm số của Test Case. Giáo viên chọn “Lưu”. Hệ thống kiểm tra tính hợp lệ của Test Case. Hệ thống lưu thông tin Test Case vào cơ sở dữ liệu. Hệ thống thông báo “Thiết lập Test Case thành công.” và hiển thị danh sách Test Case đã thiết lập. |
| **Luồng tương tác thay thế** | 6a. Giáo viên chọn “Hủy”: Hệ thống hủy thao tác thiết lập và giữ nguyên danh sách Test Case hiện tại. 6b. Giáo viên chọn “Thêm Test Case”: Hệ thống hiển thị biểu mẫu để giáo viên nhập Test Case mới. Giáo viên nhập đầy đủ thông tin và xác nhận thêm Test Case. Hệ thống thêm Test Case vào danh sách. 6c. Giáo viên chỉnh sửa Test Case đã có: Hệ thống hiển thị thông tin Test Case hiện tại. Giáo viên chỉnh sửa thông tin và chọn “Cập nhật”. Hệ thống cập nhật thông tin Test Case. 6d. Giáo viên xóa Test Case: Hệ thống yêu cầu giáo viên xác nhận thao tác xóa. Giáo viên xác nhận xóa. Hệ thống xóa Test Case khỏi bài tập. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Thông tin Test Case không hợp lệ: Hệ thống thông báo “Thông tin Test Case không hợp lệ.” E3 - Test Case đã tồn tại: Hệ thống thông báo “Test Case đã tồn tại.” E4 - Dữ liệu đầu vào hoặc kết quả đầu ra không hợp lệ: Hệ thống thông báo “Dữ liệu Test Case không hợp lệ.” E5 - Lỗi khi lưu dữ liệu: Hệ thống thông báo “Thiết lập Test Case thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền thực hiện chức năng này.” |

| Mã usecase | UC-26 |
| :---- | :---- |
| **Tên usecase** | Thiết lập rubric |
| **Mô tả** | Giáo viên thiết lập các tiêu chí và mức điểm đánh giá cho một bài tập nhằm làm cơ sở chấm điểm chương trình do sinh viên nộp. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền quản lý bài tập. Bài tập cần thiết lập Rubric đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Rubric được thiết lập thành công cho bài tập. Các tiêu chí đánh giá và mức điểm được lưu vào cơ sở dữ liệu. Rubric được sử dụng làm cơ sở đánh giá bài làm của sinh viên. Nếu thiết lập không thành công, Rubric hiện tại được giữ nguyên và hệ thống hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Quản lý bài tập”. Hệ thống hiển thị danh sách bài tập. Giáo viên chọn bài tập cần thiết lập Rubric. Hệ thống hiển thị thông tin bài tập và Rubric hiện tại nếu đã có. Giáo viên chọn chức năng “Thiết lập Rubric”. Giáo viên nhập các tiêu chí đánh giá, mô tả tiêu chí và mức điểm tương ứng. Giáo viên xác định trọng số hoặc tổng điểm cho từng tiêu chí. Giáo viên chọn “Lưu”. Hệ thống kiểm tra tính hợp lệ của Rubric. Hệ thống lưu thông tin Rubric vào cơ sở dữ liệu. Hệ thống thông báo “Thiết lập Rubric thành công.” và hiển thị Rubric đã thiết lập. |
| **Luồng tương tác thay thế** | 7a. Giáo viên chọn “Hủy”: Hệ thống hủy thao tác thiết lập và giữ nguyên Rubric hiện tại. 7b. Giáo viên chọn “Thêm tiêu chí”: Hệ thống hiển thị biểu mẫu để giáo viên nhập tiêu chí đánh giá mới. Giáo viên nhập thông tin tiêu chí và xác nhận thêm. Hệ thống thêm tiêu chí vào Rubric. 7c. Giáo viên chỉnh sửa tiêu chí: Hệ thống hiển thị thông tin tiêu chí hiện tại. Giáo viên chỉnh sửa thông tin và chọn “Cập nhật”. Hệ thống cập nhật tiêu chí trong Rubric. 7d. Giáo viên xóa tiêu chí: Hệ thống yêu cầu giáo viên xác nhận thao tác xóa. Giáo viên xác nhận xóa. Hệ thống xóa tiêu chí khỏi Rubric. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Thông tin Rubric không hợp lệ: Hệ thống thông báo “Thông tin Rubric không hợp lệ.” E3 - Tổng điểm không hợp lệ: Hệ thống thông báo “Tổng điểm của các tiêu chí không hợp lệ.” E4 - Tiêu chí đánh giá bị trùng: Hệ thống thông báo “Tiêu chí đánh giá đã tồn tại.” E5 - Rubric không có tiêu chí đánh giá: Hệ thống thông báo “Rubric phải có ít nhất một tiêu chí đánh giá.” E6 - Lỗi khi lưu dữ liệu: Hệ thống thông báo “Thiết lập Rubric thất bại.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền thực hiện chức năng này.” |

| Mã usecase | UC-27 |
| :---- | :---- |
| **Tên usecase** | Giao bài tập cho lớp |
| **Mô tả** | Giáo viên giao một bài tập đã có trong hệ thống cho một hoặc nhiều lớp học để sinh viên thực hiện. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền quản lý và giao bài tập. Bài tập cần giao đã tồn tại trong hệ thống. Lớp học cần giao bài đã tồn tại và giáo viên có quyền quản lý lớp. |
| **Hậu điều kiện** | Bài tập được giao thành công cho lớp đã chọn. Thông tin giao bài được lưu vào cơ sở dữ liệu. Sinh viên thuộc lớp được giao bài có thể xem và thực hiện bài tập. Nếu giao bài không thành công, hệ thống giữ nguyên thông tin hiện tại và hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Quản lý bài tập”. Hệ thống hiển thị danh sách bài tập. Giáo viên chọn bài tập cần giao. Hệ thống hiển thị thông tin chi tiết của bài tập. Giáo viên chọn chức năng “Giao bài tập”. Hệ thống hiển thị danh sách các lớp mà giáo viên có quyền quản lý. Giáo viên chọn lớp cần giao bài tập. Giáo viên thiết lập các thông tin giao bài nếu cần. Giáo viên chọn “Giao bài”. Hệ thống kiểm tra tính hợp lệ của thông tin giao bài. Hệ thống lưu thông tin giao bài vào cơ sở dữ liệu. Hệ thống thông báo “Giao bài tập thành công.” |
| **Luồng tương tác thay thế** | 5a. Giáo viên chọn “Hủy”: Hệ thống hủy thao tác giao bài và giữ nguyên thông tin hiện tại. 5b. Giáo viên chọn nhiều lớp: Hệ thống cho phép giáo viên chọn nhiều lớp để giao cùng một bài tập. Giáo viên xác nhận giao bài. Hệ thống tạo thông tin giao bài cho các lớp đã chọn. 5c. Giáo viên giao bài đã từng giao cho lớp: Hệ thống hiển thị thông tin bài tập đã được giao cho lớp. Giáo viên xác nhận giao lại bài tập hoặc cập nhật cấu hình giao bài. Hệ thống cập nhật thông tin giao bài theo lựa chọn của giáo viên. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Lớp học không tồn tại: Hệ thống thông báo “Không tìm thấy lớp học.” E3 - Giáo viên không có quyền quản lý lớp: Hệ thống thông báo “Bạn không có quyền giao bài tập cho lớp này.” E4 - Thông tin giao bài không hợp lệ: Hệ thống thông báo “Thông tin giao bài không hợp lệ.” E5 - Lỗi khi lưu dữ liệu: Hệ thống thông báo “Giao bài tập thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền thực hiện chức năng này.” |

| Mã usecase | UC-28 |
| :---- | :---- |
| **Tên usecase** | Xem submission |
| **Mô tả** | Giáo viên xem thông tin và kết quả bài nộp của sinh viên đối với một bài tập đã được giao. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền quản lý bài tập. Bài tập đã được giao cho lớp. Sinh viên đã thực hiện và nộp bài tập. |
| **Hậu điều kiện** | Giáo viên xem được thông tin bài nộp của sinh viên. Hệ thống hiển thị mã bài nộp, thời gian nộp, mã nguồn, kết quả kiểm thử và điểm số nếu đã được chấm. Không có dữ liệu nào bị thay đổi trong hệ thống. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Quản lý bài tập”. Hệ thống hiển thị danh sách bài tập. Giáo viên chọn bài tập cần xem bài nộp. Hệ thống hiển thị danh sách sinh viên và trạng thái nộp bài. Giáo viên chọn sinh viên cần xem bài nộp. Hệ thống hiển thị danh sách các bài nộp của sinh viên. Giáo viên chọn một bài nộp. Hệ thống hiển thị thông tin chi tiết bài nộp gồm mã nguồn, thời gian nộp, kết quả kiểm thử, kết quả phân tích và điểm số nếu có. Giáo viên xem thông tin bài nộp. |
| **Luồng tương tác thay thế** | 7a. Giáo viên chọn “Quay lại”: Hệ thống quay lại danh sách bài nộp của sinh viên. 7b. Giáo viên chọn bài nộp khác: Hệ thống hiển thị thông tin chi tiết của bài nộp được chọn. 7c. Sinh viên có nhiều bài nộp: Hệ thống hiển thị toàn bộ các bài nộp của sinh viên theo thời gian nộp. Giáo viên chọn bài nộp cần xem. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Sinh viên không tồn tại: Hệ thống thông báo “Không tìm thấy sinh viên.” E3 - Không tìm thấy bài nộp: Hệ thống thông báo “Không tìm thấy bài nộp.” E4 - Bài nộp không có mã nguồn: Hệ thống thông báo “Không có mã nguồn trong bài nộp.” E5 - Kết quả chấm chưa có: Hệ thống thông báo “Bài nộp chưa có kết quả chấm.” E6 - Lỗi khi tải dữ liệu: Hệ thống thông báo “Không thể tải thông tin bài nộp.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền xem bài nộp này.” |

| Mã usecase | UC-29 |
| :---- | :---- |
| **Tên usecase** | Xem điểm |
| **Mô tả** | Giáo viên xem điểm và kết quả đánh giá bài làm của sinh viên đối với các bài tập đã được giao. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền xem kết quả bài tập. Bài tập đã được giao cho lớp. Bài làm của sinh viên đã được chấm hoặc có kết quả đánh giá. |
| **Hậu điều kiện** | Giáo viên xem được điểm và kết quả đánh giá của sinh viên. Thông tin trong hệ thống không bị thay đổi. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Xem điểm”. Hệ thống hiển thị danh sách các bài tập đã giao. Giáo viên chọn bài tập cần xem điểm. Hệ thống hiển thị danh sách sinh viên trong lớp và điểm tương ứng. Giáo viên chọn sinh viên cần xem chi tiết. Hệ thống hiển thị điểm và kết quả đánh giá bài làm của sinh viên. Giáo viên xem thông tin điểm và kết quả đánh giá. |
| **Luồng tương tác thay thế** | 5a. Giáo viên chọn “Quay lại”: Hệ thống quay lại danh sách bài tập. 5b. Giáo viên chọn lớp khác: Hệ thống hiển thị danh sách sinh viên và điểm của lớp được chọn. 5c. Giáo viên chọn sinh viên khác: Hệ thống hiển thị điểm và kết quả đánh giá của sinh viên được chọn. 5d. Giáo viên chọn xem chi tiết điểm: Hệ thống hiển thị điểm theo từng tiêu chí đánh giá và kết quả kiểm thử của bài làm. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Không tìm thấy sinh viên: Hệ thống thông báo “Không tìm thấy sinh viên.” E3 - Chưa có kết quả chấm: Hệ thống thông báo “Bài tập chưa có kết quả chấm.” E4 - Không có điểm: Hệ thống thông báo “Sinh viên chưa có điểm.” E5 - Lỗi khi tải dữ liệu: Hệ thống thông báo “Không thể tải thông tin điểm.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền xem điểm.” |

| Mã usecase | UC-30 |
| :---- | :---- |
| **Tên usecase** | Xem AI đánh giá |
| **Mô tả** | Giáo viên xem kết quả đánh giá bài làm của sinh viên do hệ thống AI thực hiện dựa trên kết quả kiểm thử, phân tích mã nguồn và các tiêu chí đánh giá. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền xem kết quả đánh giá. Bài tập đã được giao cho lớp. Sinh viên đã nộp bài. Hệ thống đã thực hiện đánh giá AI cho bài nộp. |
| **Hậu điều kiện** | Giáo viên xem được kết quả đánh giá của AI. Hệ thống hiển thị điểm AI, kết quả kiểm thử, kết quả phân tích mã nguồn và nhận xét đánh giá. Không có dữ liệu nào bị thay đổi trong hệ thống. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Xem AI đánh giá”. Hệ thống hiển thị danh sách bài tập đã được giao. Giáo viên chọn bài tập cần xem kết quả đánh giá AI. Hệ thống hiển thị danh sách sinh viên và trạng thái đánh giá AI. Giáo viên chọn sinh viên cần xem. Hệ thống hiển thị danh sách bài nộp của sinh viên. Giáo viên chọn bài nộp cần xem đánh giá AI. Hệ thống hiển thị kết quả đánh giá AI gồm điểm đánh giá, kết quả Test Case, kết quả phân tích mã nguồn và nhận xét. Giáo viên xem kết quả đánh giá AI. |
| **Luồng tương tác thay thế** | 7a. Giáo viên chọn “Quay lại”: Hệ thống quay lại danh sách bài nộp của sinh viên. 7b. Giáo viên chọn sinh viên khác: Hệ thống hiển thị danh sách bài nộp của sinh viên được chọn. 7c. Giáo viên chọn bài nộp khác: Hệ thống hiển thị kết quả đánh giá AI của bài nộp được chọn. 7d. Giáo viên chọn xem chi tiết đánh giá: Hệ thống hiển thị chi tiết điểm đánh giá theo từng tiêu chí. Hệ thống hiển thị kết quả từng Test Case và kết quả phân tích mã nguồn tương ứng. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Sinh viên không tồn tại: Hệ thống thông báo “Không tìm thấy sinh viên.” E3 - Không tìm thấy bài nộp: Hệ thống thông báo “Không tìm thấy bài nộp.” E4 - AI chưa đánh giá bài nộp: Hệ thống thông báo “Bài nộp chưa có kết quả đánh giá AI.” E5 - Kết quả đánh giá AI không đầy đủ: Hệ thống thông báo “Kết quả đánh giá AI chưa đầy đủ.” E6 - Lỗi khi tải kết quả đánh giá: Hệ thống thông báo “Không thể tải kết quả đánh giá AI.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền xem kết quả đánh giá này.” |

| Mã usecase | UC-31 |
| :---- | :---- |
| **Tên usecase** | Đánh giá/chấm bài thủ công |
| **Mô tả** | Giáo viên đánh giá và chấm điểm bài làm của sinh viên theo Rubric đã thiết lập cho bài tập. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền chấm bài. Bài tập đã được giao cho lớp. Sinh viên đã nộp bài. Bài tập đã có Rubric đánh giá. |
| **Hậu điều kiện** | Điểm và kết quả đánh giá của giáo viên được lưu vào hệ thống. Kết quả đánh giá được ghi nhận cho bài nộp của sinh viên (ghi đè hoặc bổ sung kết quả chấm tự động theo cấu hình). Sinh viên có thể xem điểm và nhận xét nếu hệ thống cho phép hiển thị kết quả. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng “Chấm bài”. Hệ thống hiển thị danh sách bài tập đã được giao. Giáo viên chọn bài tập cần chấm. Hệ thống hiển thị danh sách sinh viên và trạng thái chấm bài. Giáo viên chọn sinh viên cần chấm. Hệ thống hiển thị bài nộp của sinh viên gồm mã nguồn và các thông tin liên quan. Giáo viên xem và đánh giá bài làm theo từng tiêu chí trong Rubric. Giáo viên nhập điểm và nhận xét cho bài làm. Giáo viên chọn “Lưu kết quả”. Hệ thống kiểm tra tính hợp lệ của điểm và thông tin đánh giá. Hệ thống lưu kết quả chấm bài vào cơ sở dữ liệu. Hệ thống thông báo “Chấm bài thành công.” |
| **Luồng tương tác thay thế** | 7a. Giáo viên chọn “Quay lại”: Hệ thống quay lại danh sách bài nộp. 7b. Giáo viên chọn sinh viên khác: Hệ thống hiển thị bài nộp của sinh viên được chọn. 7c. Giáo viên chỉnh sửa điểm: Hệ thống hiển thị điểm hiện tại. Giáo viên điều chỉnh điểm theo từng tiêu chí trong Rubric. Hệ thống cập nhật tổng điểm theo điểm đã điều chỉnh. 7d. Giáo viên lưu bài chấm tạm thời: Hệ thống lưu các thông tin đánh giá hiện tại nhưng chưa hoàn tất chấm bài. Giáo viên có thể tiếp tục chấm bài sau. |
| **Luồng tương tác ngoại lệ** | E1 - Bài tập không tồn tại: Hệ thống thông báo “Không tìm thấy bài tập.” E2 - Không tìm thấy bài nộp: Hệ thống thông báo “Không tìm thấy bài nộp.” E3 - Bài tập chưa có Rubric: Hệ thống thông báo “Bài tập chưa được thiết lập Rubric.” E4 - Điểm không hợp lệ: Hệ thống thông báo “Điểm đánh giá không hợp lệ.” E5 - Tổng điểm vượt quá mức quy định: Hệ thống thông báo “Tổng điểm không hợp lệ.” E6 - Lỗi khi lưu kết quả: Hệ thống thông báo “Chấm bài thất bại.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền chấm bài này.” |

| Mã usecase | UC-32 |
| :---- | :---- |
| **Tên usecase** | Tạo tài khoản Sinh viên/Giáo viên |
| **Mô tả** | Quản trị viên tạo tài khoản cho sinh viên hoặc giáo viên để người dùng có thể đăng nhập và sử dụng hệ thống theo vai trò được cấp. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý tài khoản người dùng. |
| **Hậu điều kiện** | Tài khoản sinh viên hoặc giáo viên được tạo thành công. Thông tin tài khoản được lưu vào cơ sở dữ liệu. Tài khoản được gán đúng vai trò và trạng thái hoạt động. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý tài khoản”. Hệ thống hiển thị danh sách tài khoản người dùng. Quản trị viên chọn “Tạo tài khoản”. Hệ thống hiển thị biểu mẫu tạo tài khoản. Quản trị viên nhập thông tin tài khoản gồm họ tên, email, mật khẩu và vai trò. Quản trị viên chọn vai trò “Sinh viên” hoặc “Giáo viên”. Quản trị viên chọn “Tạo tài khoản”. Hệ thống kiểm tra tính hợp lệ của thông tin tài khoản. Hệ thống tạo và lưu tài khoản vào cơ sở dữ liệu. Hệ thống thông báo “Tạo tài khoản thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác tạo tài khoản và quay lại danh sách tài khoản. 4b. Quản trị viên tạo tài khoản Sinh viên: Quản trị viên chọn vai trò “Sinh viên”. Hệ thống hiển thị các thông tin cần thiết cho tài khoản Sinh viên. Quản trị viên nhập thông tin và xác nhận tạo tài khoản. Hệ thống tạo tài khoản Sinh viên. 4c. Quản trị viên tạo tài khoản Giáo viên: Quản trị viên chọn vai trò “Giáo viên”. Hệ thống hiển thị các thông tin cần thiết cho tài khoản Giáo viên. Quản trị viên nhập thông tin và xác nhận tạo tài khoản. Hệ thống tạo tài khoản Giáo viên. 4d. Quản trị viên tạo tài khoản với trạng thái không hoạt động: Quản trị viên chọn trạng thái tài khoản không hoạt động. Hệ thống tạo tài khoản với trạng thái không hoạt động. |
| **Luồng tương tác ngoại lệ** | E1 - Thông tin tài khoản không hợp lệ: Hệ thống thông báo “Thông tin tài khoản không hợp lệ.” E2 - Email đã tồn tại: Hệ thống thông báo “Email đã được sử dụng.” E3 - Mật khẩu không đáp ứng yêu cầu: Hệ thống thông báo “Mật khẩu không đáp ứng yêu cầu.” E4 - Chưa chọn vai trò: Hệ thống thông báo “Vui lòng chọn vai trò cho tài khoản.” E5 - Lỗi khi tạo tài khoản: Hệ thống thông báo “Tạo tài khoản thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền tạo tài khoản.” |

| Mã usecase | UC-33 |
| :---- | :---- |
| **Tên usecase** | Khóa/mở tài khoản |
| **Mô tả** | Quản trị viên khóa hoặc mở khóa tài khoản Sinh viên/Giáo viên nhằm quản lý trạng thái hoạt động của tài khoản trong hệ thống. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý tài khoản người dùng. Tài khoản cần khóa hoặc mở khóa đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Trạng thái tài khoản được cập nhật thành công. Tài khoản bị khóa không thể đăng nhập và sử dụng hệ thống. Tài khoản được mở khóa có thể đăng nhập và sử dụng hệ thống. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý tài khoản”. Hệ thống hiển thị danh sách tài khoản người dùng. Quản trị viên chọn tài khoản cần khóa hoặc mở khóa. Hệ thống hiển thị thông tin và trạng thái hiện tại của tài khoản. Quản trị viên chọn “Khóa tài khoản” hoặc “Mở khóa tài khoản”. Hệ thống hiển thị yêu cầu xác nhận thao tác. Quản trị viên xác nhận thao tác. Hệ thống cập nhật trạng thái tài khoản. Hệ thống thông báo thao tác thành công. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác và giữ nguyên trạng thái tài khoản. 4b. Quản trị viên chọn “Khóa tài khoản”: Hệ thống hiển thị thông tin tài khoản và yêu cầu xác nhận khóa. Quản trị viên xác nhận khóa tài khoản. Hệ thống chuyển trạng thái tài khoản sang “Đã khóa”. 4c. Quản trị viên chọn “Mở khóa tài khoản”: Hệ thống hiển thị thông tin tài khoản và yêu cầu xác nhận mở khóa. Quản trị viên xác nhận mở khóa tài khoản. Hệ thống chuyển trạng thái tài khoản sang “Hoạt động”. |
| **Luồng tương tác ngoại lệ** | E1 - Tài khoản không tồn tại: Hệ thống thông báo “Không tìm thấy tài khoản.” E2 - Tài khoản đã ở trạng thái được chọn: Hệ thống thông báo “Trạng thái tài khoản không cần thay đổi.” E3 - Tài khoản không thể khóa: Hệ thống thông báo “Không thể khóa tài khoản này.” E4 - Lỗi khi cập nhật trạng thái: Hệ thống thông báo “Cập nhật trạng thái tài khoản thất bại.” E5 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền thực hiện chức năng này.” |

| Mã usecase | UC-34 |
| :---- | :---- |
| **Tên usecase** | Xóa tài khoản |
| **Mô tả** | Quản trị viên xóa hoặc vô hiệu hóa tài khoản Sinh viên hoặc Giáo viên khỏi hệ thống. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý tài khoản người dùng. Tài khoản cần xóa đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Tài khoản được xóa hoặc xóa mềm khỏi hệ thống. Tài khoản không thể đăng nhập và sử dụng hệ thống. Thông tin và lịch sử học tập được lưu trữ theo chính sách lưu trữ dữ liệu của hệ thống. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý tài khoản”. Hệ thống hiển thị danh sách tài khoản người dùng. Quản trị viên chọn tài khoản cần xóa. Hệ thống hiển thị thông tin tài khoản được chọn. Quản trị viên chọn “Xóa tài khoản”. Hệ thống hiển thị yêu cầu xác nhận thao tác xóa. Quản trị viên xác nhận xóa tài khoản. Hệ thống kiểm tra điều kiện xóa tài khoản. Hệ thống xóa hoặc xóa mềm tài khoản khỏi hệ thống theo chính sách lưu trữ. Hệ thống thông báo “Xóa tài khoản thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác xóa và giữ nguyên tài khoản. 4b. Tài khoản đang bị khóa: Hệ thống hiển thị thông tin tài khoản đang bị khóa. Quản trị viên xác nhận xóa tài khoản. Hệ thống thực hiện xóa tài khoản. 5a. Tài khoản đang có dữ liệu bài nộp hoặc lịch sử điểm số: Hệ thống chuyển sang cơ chế xóa mềm (Soft Delete/Archive) để bảo toàn tính toàn vẹn dữ liệu học tập. |
| **Luồng tương tác ngoại lệ** | E1 - Tài khoản không tồn tại: Hệ thống thông báo “Không tìm thấy tài khoản.” E2 - Tài khoản không thể xóa: Hệ thống thông báo “Không thể xóa tài khoản này.” E3 - Lỗi khi xóa tài khoản: Hệ thống thông báo “Xóa tài khoản thất bại.” E4 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền xóa tài khoản.” |

| Mã usecase | UC-35 |
| :---- | :---- |
| **Tên usecase** | Phân quyền người dùng |
| **Mô tả** | Quản trị viên phân quyền cho tài khoản người dùng dựa trên vai trò và quyền được phép thực hiện trong tổ chức. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý và phân quyền người dùng trong tổ chức. Tài khoản cần phân quyền đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Quyền của người dùng được cập nhật thành công. Người dùng có thể thực hiện các chức năng tương ứng với quyền được cấp. Hệ thống lưu thông tin phân quyền vào cơ sở dữ liệu. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Phân quyền người dùng”. Hệ thống hiển thị danh sách tài khoản người dùng. Quản trị viên chọn tài khoản cần phân quyền. Hệ thống hiển thị thông tin và quyền hiện tại của tài khoản. Quản trị viên chọn vai trò hoặc các quyền cần cấp cho người dùng trong phạm vi cho phép. Hệ thống hiển thị danh sách quyền tương ứng với vai trò được chọn. Quản trị viên xác nhận phân quyền. Hệ thống kiểm tra tính hợp lệ của quyền được chọn. Hệ thống cập nhật quyền của người dùng. Hệ thống thông báo “Phân quyền người dùng thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác phân quyền và giữ nguyên quyền hiện tại của người dùng. 4b. Quản trị viên thay đổi vai trò: Quản trị viên chọn vai trò mới cho người dùng. Hệ thống hiển thị các quyền tương ứng với vai trò mới. Quản trị viên xác nhận thay đổi. Hệ thống cập nhật vai trò và quyền của người dùng. 4c. Quản trị viên cấp thêm quyền: Hệ thống hiển thị danh sách quyền có thể cấp thêm. Quản trị viên chọn các quyền cần cấp. Hệ thống cập nhật quyền của người dùng. 4d. Quản trị viên thu hồi quyền: Hệ thống hiển thị các quyền hiện tại của người dùng. Quản trị viên chọn quyền cần thu hồi. Hệ thống cập nhật lại quyền của người dùng. |
| **Luồng tương tác ngoại lệ** | E1 - Tài khoản không tồn tại: Hệ thống thông báo “Không tìm thấy tài khoản.” E2 - Vai trò không hợp lệ: Hệ thống thông báo “Vai trò được chọn không hợp lệ.” E3 - Quyền không hợp lệ: Hệ thống thông báo “Quyền được chọn không hợp lệ.” E4 - Vượt quá thẩm quyền phân quyền: Hệ thống thông báo “Quản trị viên không thể gán quyền vượt cấp hoặc gán quyền Quản trị viên hệ thống.” E5 - Lỗi khi lưu thông tin phân quyền: Hệ thống thông báo “Phân quyền người dùng thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền phân quyền người dùng.” |

| Mã usecase | UC-36 |
| :---- | :---- |
| **Tên usecase** | Đặt lại mật khẩu |
| **Mô tả** | Quản trị viên đặt lại mật khẩu cho tài khoản Sinh viên hoặc Giáo viên khi người dùng yêu cầu hoặc gặp vấn đề khi đăng nhập. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý tài khoản người dùng. Tài khoản cần đặt lại mật khẩu đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Mật khẩu mới được cập nhật thành công cho tài khoản và các token đăng nhập cũ bị thu hồi. Mật khẩu mới được băm và lưu trong cơ sở dữ liệu. Người dùng có thể sử dụng mật khẩu mới để đăng nhập. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý tài khoản”. Hệ thống hiển thị danh sách tài khoản người dùng. Quản trị viên chọn tài khoản cần đặt lại mật khẩu. Hệ thống hiển thị thông tin tài khoản. Quản trị viên chọn “Đặt lại mật khẩu”. Hệ thống hiển thị biểu mẫu đặt lại mật khẩu. Quản trị viên nhập mật khẩu mới và xác nhận mật khẩu. Quản trị viên chọn “Xác nhận”. Hệ thống kiểm tra tính hợp lệ của mật khẩu. Hệ thống băm mật khẩu mới, cập nhật vào cơ sở dữ liệu và thu hồi phiên làm việc hiện tại của người dùng. Hệ thống thông báo “Đặt lại mật khẩu thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác đặt lại mật khẩu và giữ nguyên mật khẩu hiện tại. 4b. Quản trị viên chọn tài khoản khác: Hệ thống hiển thị thông tin của tài khoản được chọn. Quản trị viên thực hiện thao tác đặt lại mật khẩu cho tài khoản mới. 4c. Mật khẩu mới được hệ thống tự động tạo: Hệ thống tạo mật khẩu mới ngẫu nhiên. Hệ thống hiển thị hoặc cung cấp mật khẩu mới cho quản trị viên theo chính sách bảo mật của hệ thống. Quản trị viên xác nhận đặt lại mật khẩu. |
| **Luồng tương tác ngoại lệ** | E1 - Tài khoản không tồn tại: Hệ thống thông báo “Không tìm thấy tài khoản.” E2 - Mật khẩu không đáp ứng yêu cầu: Hệ thống thông báo “Mật khẩu không đáp ứng yêu cầu.” E3 - Mật khẩu xác nhận không khớp: Hệ thống thông báo “Mật khẩu xác nhận không khớp.” E4 - Tài khoản không thể đặt lại mật khẩu: Hệ thống thông báo “Không thể đặt lại mật khẩu cho tài khoản này.” E5 - Lỗi khi cập nhật mật khẩu: Hệ thống thông báo “Đặt lại mật khẩu thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền đặt lại mật khẩu.” |

| Mã usecase | UC-37 |
| :---- | :---- |
| **Tên usecase** | Nhập danh sách từ Excel/CSV |
| **Mô tả** | Quản trị viên nhập danh sách người dùng từ tệp Excel hoặc CSV vào hệ thống để tạo hoặc cập nhật thông tin tài khoản hàng loạt. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý và nhập dữ liệu người dùng. Tệp Excel hoặc CSV chứa danh sách người dùng đã được chuẩn bị. |
| **Hậu điều kiện** | Danh sách người dùng hợp lệ được nhập thành công vào hệ thống. Thông tin người dùng được lưu vào cơ sở dữ liệu. Hệ thống hiển thị kết quả nhập dữ liệu và các bản ghi không hợp lệ nếu có. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Nhập danh sách từ Excel/CSV”. Hệ thống hiển thị giao diện nhập dữ liệu và hướng dẫn định dạng tệp. Quản trị viên chọn và tải lên tệp Excel hoặc CSV. Hệ thống kiểm tra định dạng và cấu trúc tệp. Hệ thống đọc và hiển thị dữ liệu trong tệp để quản trị viên kiểm tra. Quản trị viên xác nhận nhập dữ liệu. Hệ thống kiểm tra tính hợp lệ của từng bản ghi. Hệ thống lưu các bản ghi hợp lệ vào cơ sở dữ liệu. Hệ thống thông báo kết quả nhập dữ liệu. |
| **Luồng tương tác thay thế** | 3a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác nhập dữ liệu và không thay đổi dữ liệu hiện tại. 4a. Tệp chứa cả bản ghi hợp lệ và không hợp lệ: Hệ thống hiển thị danh sách các bản ghi không hợp lệ và lý do lỗi. Quản trị viên xác nhận tiếp tục nhập các bản ghi hợp lệ. Hệ thống lưu các bản ghi hợp lệ vào cơ sở dữ liệu. 4b. Tệp chứa tài khoản đã tồn tại: Hệ thống hiển thị các tài khoản đã tồn tại. Quản trị viên chọn bỏ qua hoặc cập nhật các tài khoản này. Hệ thống xử lý dữ liệu theo lựa chọn của quản trị viên. 4c. Quản trị viên tải lên tệp khác: Hệ thống hủy dữ liệu tệp hiện tại. Quản trị viên chọn tệp Excel hoặc CSV mới. Hệ thống thực hiện kiểm tra tệp mới. |
| **Luồng tương tác ngoại lệ** | E1 - Tệp không đúng định dạng: Hệ thống thông báo “Tệp không đúng định dạng Excel hoặc CSV.” E2 - Tệp không đúng cấu trúc: Hệ thống thông báo “Cấu trúc tệp không hợp lệ.” E3 - Tệp không có dữ liệu: Hệ thống thông báo “Tệp không chứa dữ liệu.” E4 - Dữ liệu không hợp lệ: Hệ thống thông báo “Tệp chứa dữ liệu không hợp lệ.” E5 - Tài khoản đã tồn tại: Hệ thống thông báo “Một hoặc nhiều tài khoản đã tồn tại trong hệ thống.” E6 - Lỗi khi đọc hoặc xử lý tệp: Hệ thống thông báo “Không thể đọc hoặc xử lý tệp.” E7 - Lỗi khi lưu dữ liệu: Hệ thống thông báo “Nhập dữ liệu thất bại.” E8 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền nhập dữ liệu.” |

| Mã usecase | UC-38 |
| :---- | :---- |
| **Tên usecase** | Tạo lớp |
| **Mô tả** | Quản trị viên tạo lớp học mới và thiết lập các thông tin cơ bản của lớp để quản lý sinh viên và giáo viên trong hệ thống. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý lớp học trong tổ chức. |
| **Hậu điều kiện** | Lớp học được tạo thành công. Thông tin lớp được lưu vào cơ sở dữ liệu. Lớp có thể được sử dụng để quản lý sinh viên và giáo viên. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý lớp”. Hệ thống hiển thị danh sách các lớp học hiện có. Quản trị viên chọn “Tạo lớp”. Hệ thống hiển thị biểu mẫu tạo lớp học gồm tên lớp, mã lớp, mô tả, niên khóa và giáo viên phụ trách (nếu có). Quản trị viên nhập thông tin lớp học và chọn “Tạo lớp”. Hệ thống kiểm tra tính hợp lệ của thông tin lớp học và tính duy nhất của mã lớp. Hệ thống tạo lớp và lưu thông tin vào cơ sở dữ liệu. Hệ thống thông báo “Tạo lớp thành công.” và hiển thị lớp mới trong danh sách. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác tạo lớp và quay lại danh sách lớp. 4b. Quản trị viên tạo lớp và phân công giáo viên ngay: Quản trị viên chọn giáo viên phụ trách lớp từ danh sách. Hệ thống lưu thông tin lớp cùng thông tin phân công giáo viên. |
| **Luồng tương tác ngoại lệ** | E1 - Thông tin lớp không hợp lệ: Hệ thống thông báo “Thông tin lớp không hợp lệ.” E2 - Mã lớp đã tồn tại: Hệ thống thông báo “Mã lớp đã tồn tại.” E3 - Tên lớp đã tồn tại: Hệ thống thông báo “Tên lớp đã tồn tại.” E4 - Giáo viên không tồn tại: Hệ thống thông báo “Không tìm thấy giáo viên được chọn.” E5 - Lỗi khi lưu thông tin lớp: Hệ thống thông báo “Tạo lớp thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền tạo lớp.” |

| Mã usecase | UC-39 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa lớp |
| **Mô tả** | Quản trị viên chỉnh sửa thông tin của lớp học đã được tạo trong hệ thống. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý lớp học. Lớp cần chỉnh sửa đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Thông tin lớp được cập nhật thành công. Thông tin mới được lưu vào cơ sở dữ liệu. Các thành viên của lớp tiếp tục được quản lý theo thông tin đã cập nhật. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý lớp”. Hệ thống hiển thị danh sách các lớp hiện có. Quản trị viên chọn lớp cần chỉnh sửa. Hệ thống hiển thị thông tin hiện tại của lớp. Quản trị viên chỉnh sửa thông tin lớp. Quản trị viên chọn “Lưu thay đổi”. Hệ thống kiểm tra tính hợp lệ của thông tin mới. Hệ thống cập nhật thông tin lớp vào cơ sở dữ liệu. Hệ thống thông báo “Chỉnh sửa lớp thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác chỉnh sửa và giữ nguyên thông tin lớp. 4b. Quản trị viên thay đổi tên lớp: Quản trị viên nhập tên lớp mới. Hệ thống kiểm tra tên lớp. Hệ thống cập nhật tên lớp mới. 4c. Quản trị viên thay đổi giáo viên phụ trách: Quản trị viên chọn giáo viên mới. Hệ thống cập nhật giáo viên phụ trách lớp. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp không tồn tại: Hệ thống thông báo “Không tìm thấy lớp.” E2 - Thông tin lớp không hợp lệ: Hệ thống thông báo “Thông tin lớp không hợp lệ.” E3 - Tên lớp đã tồn tại: Hệ thống thông báo “Tên lớp đã tồn tại.” E4 - Giáo viên không tồn tại: Hệ thống thông báo “Không tìm thấy giáo viên được chọn.” E5 - Lỗi khi cập nhật thông tin: Hệ thống thông báo “Chỉnh sửa lớp thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền chỉnh sửa lớp.” |

| Mã usecase | UC-40 |
| :---- | :---- |
| **Tên usecase** | Xóa/đóng lớp |
| **Mô tả** | Quản trị viên xóa hoặc đóng một lớp học đã được tạo trong hệ thống nhằm quản lý trạng thái hoạt động của lớp. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý lớp học. Lớp cần xóa hoặc đóng đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Nếu xóa, lớp được xóa hoặc xóa mềm khỏi danh sách lớp theo chính sách dữ liệu của hệ thống. Nếu đóng, trạng thái lớp được chuyển sang “Đã đóng”. Lớp đã đóng không thể tiếp nhận hoạt động mới của sinh viên và giáo viên. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý lớp”. Hệ thống hiển thị danh sách các lớp hiện có. Quản trị viên chọn lớp cần xóa hoặc đóng. Hệ thống hiển thị thông tin và trạng thái hiện tại của lớp. Quản trị viên chọn “Xóa lớp” hoặc “Đóng lớp”. Hệ thống hiển thị yêu cầu xác nhận thao tác. Quản trị viên xác nhận thao tác. Hệ thống kiểm tra điều kiện xóa hoặc đóng lớp. Hệ thống cập nhật trạng thái hoặc xóa lớp theo lựa chọn. Hệ thống thông báo “Thao tác thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác và giữ nguyên trạng thái lớp. 4b. Quản trị viên chọn “Đóng lớp”: Hệ thống yêu cầu xác nhận đóng lớp. Quản trị viên xác nhận đóng lớp. Hệ thống chuyển trạng thái lớp sang “Đã đóng”. 4c. Quản trị viên chọn “Xóa lớp”: Hệ thống kiểm tra dữ liệu liên quan đến lớp. Quản trị viên xác nhận xóa lớp. Hệ thống xóa hoặc chuyển sang lưu trữ lớp theo chính sách dữ liệu của hệ thống. 4d. Quản trị viên chọn lớp khác: Hệ thống hiển thị thông tin của lớp được chọn. Quản trị viên thực hiện thao tác xóa hoặc đóng lớp. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp không tồn tại: Hệ thống thông báo “Không tìm thấy lớp.” E2 - Lớp đã đóng: Hệ thống thông báo “Lớp đã được đóng.” E3 - Lớp đang có dữ liệu liên quan: Hệ thống chuyển sang cơ chế lưu trữ (archive) hoặc thông báo “Lớp đang có dữ liệu bài nộp liên quan, đã chuyển sang trạng thái đóng/lưu trữ.” E4 - Không thể đóng lớp: Hệ thống thông báo “Không thể đóng lớp này.” E5 - Lỗi khi cập nhật hoặc xóa lớp: Hệ thống thông báo “Thao tác xóa/đóng lớp thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền thực hiện chức năng này.” |

| Mã usecase | UC-41 |
| :---- | :---- |
| **Tên usecase** | Quản lý sinh viên trong lớp |
| **Mô tả** | Quản trị viên quản lý danh sách sinh viên thuộc một lớp, bao gồm thêm, xóa và xem thông tin sinh viên trong lớp. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý lớp học. Lớp cần quản lý đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Danh sách sinh viên trong lớp được cập nhật thành công. Thông tin phân lớp của sinh viên được lưu vào cơ sở dữ liệu. Danh sách sinh viên trong lớp phản ánh đúng các thay đổi đã thực hiện. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý lớp”. Hệ thống hiển thị danh sách các lớp. Quản trị viên chọn lớp cần quản lý sinh viên. Hệ thống hiển thị danh sách sinh viên hiện tại của lớp. Quản trị viên chọn thao tác quản lý sinh viên. Hệ thống hiển thị các chức năng thêm, xóa và xem thông tin sinh viên. Quản trị viên thực hiện thao tác cần thiết. Hệ thống kiểm tra tính hợp lệ của thao tác. Hệ thống cập nhật danh sách sinh viên trong lớp. Hệ thống thông báo “Cập nhật danh sách sinh viên thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Thêm sinh viên”: Hệ thống hiển thị danh sách sinh viên chưa thuộc lớp. Quản trị viên chọn sinh viên cần thêm. Quản trị viên xác nhận thêm sinh viên vào lớp. Hệ thống cập nhật danh sách sinh viên của lớp. 4b. Quản trị viên chọn “Xóa sinh viên”: Quản trị viên chọn sinh viên cần xóa khỏi lớp. Hệ thống yêu cầu xác nhận thao tác. Quản trị viên xác nhận xóa sinh viên khỏi lớp. Hệ thống cập nhật danh sách sinh viên của lớp. 4c. Quản trị viên chọn “Xem thông tin sinh viên”: Hệ thống hiển thị thông tin của sinh viên được chọn. 4d. Quản trị viên chọn nhiều sinh viên: Hệ thống cho phép quản trị viên chọn nhiều sinh viên để thêm hoặc xóa khỏi lớp. Quản trị viên xác nhận thao tác. Hệ thống cập nhật danh sách sinh viên theo lựa chọn. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp không tồn tại: Hệ thống thông báo “Không tìm thấy lớp.” E2 - Sinh viên không tồn tại: Hệ thống thông báo “Không tìm thấy sinh viên.” E3 - Sinh viên đã thuộc lớp: Hệ thống thông báo “Sinh viên đã thuộc lớp này.” E4 - Sinh viên chưa thuộc lớp: Hệ thống thông báo “Sinh viên không thuộc lớp này.” E5 - Không thể thêm hoặc xóa sinh viên: Hệ thống thông báo “Không thể cập nhật sinh viên trong lớp.” E6 - Lỗi khi lưu dữ liệu: Hệ thống thông báo “Cập nhật danh sách sinh viên thất bại.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền quản lý sinh viên trong lớp.” |

| Mã usecase | UC-42 |
| :---- | :---- |
| **Tên usecase** | Phân công giảng viên vào lớp |
| **Mô tả** | Quản trị viên phân công một hoặc nhiều giáo viên phụ trách giảng dạy cho lớp học trong hệ thống. |
| **Tác nhân** | Quản trị viên. |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý lớp học. Lớp cần phân công đã tồn tại trong hệ thống. Giáo viên cần phân công đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Giáo viên được phân công thành công vào lớp. Thông tin phân công được lưu vào cơ sở dữ liệu. Giáo viên có thể quản lý và giảng dạy lớp theo quyền được cấp. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng “Quản lý lớp”. Hệ thống hiển thị danh sách các lớp. Quản trị viên chọn lớp cần phân công giáo viên. Hệ thống hiển thị thông tin và danh sách giáo viên đang phụ trách lớp. Quản trị viên chọn chức năng “Phân công giáo viên”. Hệ thống hiển thị danh sách giáo viên có thể phân công. Quản trị viên chọn giáo viên cần phân công. Quản trị viên xác nhận phân công. Hệ thống kiểm tra tính hợp lệ của thông tin phân công. Hệ thống lưu thông tin phân công vào cơ sở dữ liệu. Hệ thống thông báo “Phân công giáo viên thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn “Hủy”: Hệ thống hủy thao tác phân công và giữ nguyên danh sách giáo viên của lớp. 4b. Quản trị viên phân công nhiều giáo viên: Hệ thống cho phép quản trị viên chọn nhiều giáo viên. Quản trị viên xác nhận phân công. Hệ thống phân công các giáo viên được chọn vào lớp. 4c. Quản trị viên thay đổi giáo viên phụ trách: Hệ thống hiển thị giáo viên đang phụ trách lớp. Quản trị viên chọn giáo viên mới. Quản trị viên xác nhận thay đổi. Hệ thống cập nhật thông tin phân công. 4d. Quản trị viên hủy phân công giáo viên: Quản trị viên chọn giáo viên cần hủy phân công. Hệ thống yêu cầu xác nhận thao tác. Quản trị viên xác nhận hủy phân công. Hệ thống xóa thông tin phân công khỏi lớp. |
| **Luồng tương tác ngoại lệ** | E1 - Lớp không tồn tại: Hệ thống thông báo “Không tìm thấy lớp.” E2 - Giáo viên không tồn tại: Hệ thống thông báo “Không tìm thấy giáo viên.” E3 - Giáo viên đã được phân công: Hệ thống thông báo “Giáo viên đã được phân công vào lớp này.” E4 - Lớp đã đóng: Hệ thống thông báo “Không thể phân công giáo viên vào lớp đã đóng.” E5 - Lỗi khi lưu thông tin phân công: Hệ thống thông báo “Phân công giáo viên thất bại.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền phân công giáo viên.” |

| Mã usecase | UC-43 |
| :---- | :---- |
| **Tên usecase** | Quản lý cấu hình AI |
| **Mô tả** | Quản trị viên hệ thống quản lý các cấu hình AI được sử dụng trong hệ thống, bao gồm thiết lập, cập nhật và kích hoạt hoặc vô hiệu hóa cấu hình. |
| **Tác nhân** | Quản trị viên hệ thống. |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền quản lý cấu hình AI. Các thành phần AI cần cấu hình đã được tích hợp vào hệ thống. |
| **Hậu điều kiện** | Cấu hình AI được tạo hoặc cập nhật thành công. Thông tin cấu hình được lưu vào hệ thống. Hệ thống sử dụng cấu hình đang được kích hoạt cho các chức năng AI tương ứng. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng “Quản lý cấu hình AI”. Hệ thống hiển thị danh sách các cấu hình AI hiện có. Quản trị viên hệ thống chọn cấu hình cần thiết lập hoặc chỉnh sửa. Hệ thống hiển thị thông tin cấu hình hiện tại. Quản trị viên hệ thống nhập hoặc chỉnh sửa các thông số cấu hình AI. Quản trị viên hệ thống chọn “Lưu cấu hình”. Hệ thống kiểm tra tính hợp lệ của các thông số. Hệ thống lưu cấu hình vào cơ sở dữ liệu. Hệ thống thông báo “Cập nhật cấu hình AI thành công.” |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn “Hủy”: Hệ thống hủy thao tác và giữ nguyên cấu hình hiện tại. 4b. Quản trị viên hệ thống tạo cấu hình AI mới: Hệ thống hiển thị biểu mẫu tạo cấu hình. Quản trị viên hệ thống nhập các thông số cấu hình. Quản trị viên hệ thống xác nhận tạo cấu hình. Hệ thống lưu cấu hình AI mới. 4c. Quản trị viên hệ thống kích hoạt cấu hình: Quản trị viên hệ thống chọn cấu hình cần kích hoạt. Hệ thống yêu cầu xác nhận. Quản trị viên hệ thống xác nhận kích hoạt. Hệ thống chuyển cấu hình sang trạng thái hoạt động. 4d. Quản trị viên hệ thống vô hiệu hóa cấu hình: Quản trị viên hệ thống chọn cấu hình cần vô hiệu hóa. Hệ thống yêu cầu xác nhận. Quản trị viên hệ thống xác nhận vô hiệu hóa. Hệ thống chuyển cấu hình sang trạng thái không hoạt động. 4e. Quản trị viên hệ thống kiểm tra cấu hình: Quản trị viên hệ thống chọn chức năng kiểm tra cấu hình. Hệ thống thực hiện kiểm tra kết nối và tính hợp lệ của cấu hình. Hệ thống hiển thị kết quả kiểm tra. |
| **Luồng tương tác ngoại lệ** | E1 - Cấu hình không hợp lệ: Hệ thống thông báo “Thông tin cấu hình AI không hợp lệ.” E2 - Thiếu thông số bắt buộc: Hệ thống thông báo “Vui lòng nhập đầy đủ các thông số bắt buộc.” E3 - Cấu hình đã tồn tại: Hệ thống thông báo “Cấu hình AI đã tồn tại.” E4 - Kết nối dịch vụ AI thất bại: Hệ thống thông báo “Không thể kết nối đến dịch vụ AI.” E5 - Không thể kích hoạt cấu hình: Hệ thống thông báo “Không thể kích hoạt cấu hình AI.” E6 - Lỗi khi lưu cấu hình: Hệ thống thông báo “Cập nhật cấu hình AI thất bại.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền quản lý cấu hình AI.” |

| Mã usecase | UC-44 |
| :---- | :---- |
| **Tên usecase** | Cấu hình Docker Sandbox |
| **Mô tả** | Quản trị viên hệ thống cấu hình môi trường Docker Sandbox để thực thi và kiểm tra mã nguồn của sinh viên một cách an toàn. |
| **Tác nhân** | Quản trị viên hệ thống. |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền quản lý cấu hình Docker Sandbox. Dịch vụ Docker Sandbox đã được tích hợp vào hệ thống. |
| **Hậu điều kiện** | Cấu hình Docker Sandbox được lưu thành công. Docker Sandbox sử dụng cấu hình mới cho quá trình thực thi mã nguồn. Các thông số cấu hình được áp dụng cho các phiên thực thi mới. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng “Cấu hình Docker Sandbox”. Hệ thống hiển thị các thông số cấu hình hiện tại. Quản trị viên hệ thống nhập hoặc chỉnh sửa các thông số cấu hình. Quản trị viên hệ thống chọn “Lưu cấu hình”. Hệ thống kiểm tra tính hợp lệ của các thông số. Hệ thống lưu cấu hình vào cơ sở dữ liệu. Hệ thống áp dụng cấu hình cho Docker Sandbox. Hệ thống thông báo “Cấu hình Docker Sandbox thành công.” |
| **Luồng tương tác thay thế** | 3a. Quản trị viên hệ thống chọn “Hủy”: Hệ thống hủy thao tác và giữ nguyên cấu hình hiện tại. 3b. Quản trị viên hệ thống khôi phục cấu hình mặc định: Quản trị viên hệ thống chọn “Khôi phục mặc định”. Hệ thống hiển thị các thông số cấu hình mặc định. Quản trị viên hệ thống xác nhận khôi phục. Hệ thống cập nhật cấu hình Docker Sandbox về giá trị mặc định. 3c. Quản trị viên hệ thống kiểm tra cấu hình: Quản trị viên hệ thống chọn chức năng “Kiểm tra cấu hình”. Hệ thống kiểm tra kết nối và khả năng khởi tạo Docker Sandbox. Hệ thống hiển thị kết quả kiểm tra. 3d. Quản trị viên hệ thống cập nhật giới hạn thực thi: Quản trị viên hệ thống điều chỉnh thời gian chạy, bộ nhớ và tài nguyên được cấp cho Docker Sandbox. Hệ thống kiểm tra và lưu các giới hạn mới. |
| **Luồng tương tác ngoại lệ** | E1 - Thông số cấu hình không hợp lệ: Hệ thống thông báo “Thông số cấu hình Docker Sandbox không hợp lệ.” E2 - Thiếu thông số bắt buộc: Hệ thống thông báo “Vui lòng nhập đầy đủ các thông số bắt buộc.” E3 - Docker Sandbox không khả dụng: Hệ thống thông báo “Docker Sandbox hiện không khả dụng.” E4 - Không thể kết nối Docker: Hệ thống thông báo “Không thể kết nối đến Docker.” E5 - Cấu hình vượt quá giới hạn cho phép: Hệ thống thông báo “Thông số cấu hình vượt quá giới hạn cho phép.” E6 - Lỗi khi lưu cấu hình: Hệ thống thông báo “Cấu hình Docker Sandbox thất bại.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền cấu hình Docker Sandbox.” |

| Mã usecase | UC-45 |
| :---- | :---- |
| **Tên usecase** | Giám sát Docker Sandbox |
| **Mô tả** | Quản trị viên hệ thống giám sát trạng thái và hoạt động của Docker Sandbox để theo dõi tình trạng thực thi mã nguồn và phát hiện các vấn đề trong quá trình vận hành. |
| **Tác nhân** | Quản trị viên hệ thống. |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền giám sát Docker Sandbox. Dịch vụ Docker Sandbox đã được tích hợp vào hệ thống. |
| **Hậu điều kiện** | Quản trị viên hệ thống xem được trạng thái và thông tin hoạt động của Docker Sandbox. Hệ thống ghi nhận các sự kiện và lỗi phát sinh trong quá trình thực thi. Không có dữ liệu cấu hình hoặc dữ liệu bài làm bị thay đổi. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng “Giám sát Docker Sandbox”. Hệ thống kiểm tra trạng thái của Docker Sandbox. Hệ thống hiển thị trạng thái hoạt động của Docker Sandbox. Hệ thống hiển thị thông tin các phiên thực thi đang hoạt động và đã hoàn thành. Quản trị viên hệ thống xem mức sử dụng tài nguyên của Docker Sandbox. Quản trị viên hệ thống xem các lỗi hoặc sự kiện phát sinh trong quá trình thực thi. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn một phiên thực thi: Hệ thống hiển thị thông tin chi tiết của phiên thực thi. Hệ thống hiển thị thời gian thực thi, trạng thái và kết quả của phiên. 4b. Quản trị viên hệ thống xem nhật ký hoạt động: Hệ thống hiển thị nhật ký hoạt động của Docker Sandbox. Quản trị viên hệ thống xem các sự kiện và lỗi phát sinh. 4c. Quản trị viên hệ thống làm mới thông tin giám sát: Hệ thống cập nhật trạng thái và thông tin tài nguyên mới nhất. 4d. Quản trị viên hệ thống dừng phiên thực thi: Quản trị viên hệ thống chọn phiên thực thi cần dừng. Hệ thống yêu cầu xác nhận thao tác. Quản trị viên hệ thống xác nhận dừng phiên. Hệ thống dừng container và cập nhật trạng thái phiên thành TERMINATED. |
| **Luồng tương tác ngoại lệ** | E1 - Docker Sandbox không khả dụng: Hệ thống thông báo “Docker Sandbox hiện không khả dụng.” E2 - Không thể lấy trạng thái Docker Sandbox: Hệ thống thông báo “Không thể lấy trạng thái Docker Sandbox.” E3 - Không thể lấy thông tin tài nguyên: Hệ thống thông báo “Không thể lấy thông tin tài nguyên.” E4 - Không tìm thấy phiên thực thi: Hệ thống thông báo “Không tìm thấy phiên thực thi.” E5 - Không thể dừng phiên thực thi: Hệ thống thông báo “Không thể dừng phiên thực thi.” E6 - Lỗi khi tải nhật ký: Hệ thống thông báo “Không thể tải nhật ký hoạt động.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền giám sát Docker Sandbox.” |

| Mã usecase | UC-46 |
| :---- | :---- |
| **Tên usecase** | Quản lý tổ chức |
| **Mô tả** | Quản trị viên hệ thống quản lý thông tin và trạng thái các tổ chức sử dụng nền tảng, bao gồm tạo, cập nhật, khóa/mở khóa và xóa tổ chức. |
| **Tác nhân** | Quản trị viên hệ thống. |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền quản lý tổ chức. |
| **Hậu điều kiện** | Thông tin tổ chức được tạo, cập nhật hoặc thay đổi trạng thái thành công. Thông tin tổ chức được lưu vào cơ sở dữ liệu. Các thay đổi được áp dụng cho tổ chức tương ứng. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng “Quản lý tổ chức”. Hệ thống hiển thị danh sách các tổ chức. Quản trị viên hệ thống chọn tổ chức cần quản lý. Hệ thống hiển thị thông tin và trạng thái hiện tại của tổ chức. Quản trị viên hệ thống chọn thao tác cần thực hiện. Hệ thống hiển thị biểu mẫu hoặc yêu cầu xác nhận tương ứng. Quản trị viên hệ thống nhập thông tin hoặc xác nhận thao tác. Hệ thống kiểm tra tính hợp lệ của dữ liệu. Hệ thống cập nhật thông tin hoặc trạng thái tổ chức. Hệ thống thông báo thao tác thành công. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn “Tạo tổ chức”: Hệ thống hiển thị biểu mẫu tạo tổ chức. Quản trị viên hệ thống nhập thông tin tổ chức. Quản trị viên hệ thống xác nhận tạo tổ chức. Hệ thống tạo tổ chức mới. 4b. Quản trị viên hệ thống chọn “Chỉnh sửa tổ chức”: Hệ thống hiển thị thông tin hiện tại của tổ chức. Quản trị viên hệ thống chỉnh sửa thông tin. Quản trị viên hệ thống xác nhận cập nhật. Hệ thống cập nhật thông tin tổ chức. 4c. Quản trị viên hệ thống chọn “Khóa/mở khóa tổ chức”: Hệ thống hiển thị trạng thái hiện tại của tổ chức. Quản trị viên hệ thống xác nhận thay đổi trạng thái. Hệ thống cập nhật trạng thái tổ chức. 4d. Quản trị viên hệ thống chọn “Xóa tổ chức”: Hệ thống kiểm tra dữ liệu liên quan đến tổ chức. Quản trị viên hệ thống xác nhận xóa tổ chức. Hệ thống xóa hoặc chuyển trạng thái lưu trữ theo chính sách dữ liệu của hệ thống. 4e. Quản trị viên hệ thống chọn “Hủy”: Hệ thống hủy thao tác và giữ nguyên thông tin tổ chức. |
| **Luồng tương tác ngoại lệ** | E1 - Tổ chức không tồn tại: Hệ thống thông báo “Không tìm thấy tổ chức.” E2 - Thông tin tổ chức không hợp lệ: Hệ thống thông báo “Thông tin tổ chức không hợp lệ.” E3 - Tổ chức đã tồn tại: Hệ thống thông báo “Tổ chức đã tồn tại.” E4 - Tổ chức đang có dữ liệu liên quan: Hệ thống thông báo “Tổ chức đang có dữ liệu liên quan và không thể xóa.” E5 - Không thể thay đổi trạng thái tổ chức: Hệ thống thông báo “Không thể thay đổi trạng thái tổ chức.” E6 - Lỗi khi lưu dữ liệu: Hệ thống thông báo “Quản lý tổ chức thất bại.” E7 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền quản lý tổ chức.” |

| Mã usecase | UC-47 |
| :---- | :---- |
| **Tên usecase** | Quản lý System Logs |
| **Mô tả** | Quản trị viên hệ thống xem, tìm kiếm và theo dõi các System Logs được ghi nhận trong quá trình hoạt động của hệ thống nhằm hỗ trợ giám sát và kiểm tra sự cố. |
| **Tác nhân** | Quản trị viên hệ thống. |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền quản lý System Logs. Hệ thống đã ghi nhận System Logs. |
| **Hậu điều kiện** | Quản trị viên hệ thống xem được các System Logs theo nhu cầu. Thông tin nhật ký không bị thay đổi trong quá trình xem và tra cứu. Các thao tác quản lý System Logs được ghi nhận nếu hệ thống có hỗ trợ. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng “Quản lý System Logs”. Hệ thống hiển thị danh sách System Logs. Quản trị viên hệ thống xem thông tin nhật ký gồm thời gian, người dùng, hành động, loại sự kiện và trạng thái. Quản trị viên hệ thống chọn điều kiện tìm kiếm hoặc lọc System Logs. Hệ thống xử lý điều kiện tìm kiếm hoặc lọc. Hệ thống hiển thị các System Logs phù hợp. Quản trị viên hệ thống chọn một System Log để xem chi tiết. Hệ thống hiển thị thông tin chi tiết của System Log được chọn. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống tìm kiếm System Logs: Quản trị viên hệ thống nhập từ khóa tìm kiếm. Hệ thống hiển thị các System Logs phù hợp. 4b. Quản trị viên hệ thống lọc System Logs: Quản trị viên hệ thống chọn khoảng thời gian, loại sự kiện hoặc trạng thái. Hệ thống hiển thị các System Logs theo điều kiện đã chọn. 4c. Quản trị viên hệ thống xem chi tiết System Log: Quản trị viên hệ thống chọn một System Log. Hệ thống hiển thị toàn bộ thông tin chi tiết của System Log. 4d. Quản trị viên hệ thống xuất System Logs: Quản trị viên hệ thống chọn khoảng dữ liệu cần xuất. Hệ thống tạo tệp chứa các System Logs được chọn. Hệ thống cung cấp tệp cho quản trị viên hệ thống. |
| **Luồng tương tác ngoại lệ** | E1 - Không tìm thấy System Logs: Hệ thống thông báo “Không tìm thấy System Logs phù hợp.” E2 - Điều kiện tìm kiếm không hợp lệ: Hệ thống thông báo “Điều kiện tìm kiếm không hợp lệ.” E3 - System Log không tồn tại: Hệ thống thông báo “Không tìm thấy System Log.” E4 - Không thể tải System Logs: Hệ thống thông báo “Không thể tải System Logs.” E5 - Lỗi khi xuất System Logs: Hệ thống thông báo “Không thể xuất System Logs.” E6 - Không có quyền thực hiện: Hệ thống thông báo “Bạn không có quyền quản lý System Logs.” |

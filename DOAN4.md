

| Mã usecase | UC-01 |
| :---- | :---- |
| **Tên usecase** | Đăng nhập |
| **Mô tả** | Cho phép người dùng xác thực tài khoản để bắt đầu phiên làm việc trên hệ thống. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống, Giáo vụ, Người dùng. |
| **Tiền điều kiện** | Người dùng đã có tài khoản trong hệ thống. |
| **Hậu điều kiện** | Phiên đăng nhập được tạo thành công. Hệ thống cấp token xác thực và chuyển người dùng đến trang chính phù hợp với vai trò. Nếu đăng nhập thất bại, phiên đăng nhập không được tạo và dữ liệu biểu mẫu vẫn được giữ để người dùng thử lại. |
| **Luồng tương tác chính** | Người dùng truy cập trang đăng nhập. Hệ thống hiển thị biểu mẫu yêu cầu Email và Mật khẩu. Người dùng nhập thông tin tài khoản và chọn "Đăng nhập". Hệ thống kiểm tra định dạng dữ liệu và tìm tài khoản tương ứng. Hệ thống đối chiếu mật khẩu với mật khẩu đã được băm trong cơ sở dữ liệu, đồng thời kiểm tra trạng thái tài khoản. Hệ thống tạo phiên đăng nhập và cấp access\_token cùng refresh\_token. Nếu đăng nhập thành công, hệ thống chuyển người dùng đến giao diện tương ứng với vai trò: Sinh viên, Giáo viên, Giáo vụ, Quản trị viên hoặc Quản trị viên hệ thống  |
| **Luồng tương tác thay thế** | 7a. Người dùng đã truy cập một trang yêu cầu đăng nhập trước đó:  Hệ thống chuyển người dùng về trang được yêu cầu ban đầu thay vì trang chính. 7b. Tài khoản đang dùng mật khẩu tạm: Hệ thống chuyển người dùng đến biểu mẫu đổi mật khẩu bắt buộc; đổi thành công mới vào trang chính.  |
| **Luồng tương tác ngoại lệ** | E1 \- Thông tin đăng nhập không hợp lệ:  Hệ thống thông báo "Email hoặc mật khẩu không chính xác." và giữ nguyên biểu mẫu. E2 \- Tài khoản bị khóa hoặc vô hiệu hóa:  Hệ thống thông báo "Tài khoản đã bị khóa hoặc vô hiệu hóa." E3 \- Lỗi hệ thống:  Hệ thống thông báo "Đăng nhập thất bại, vui lòng thử lại sau." |

| Mã usecase | UC-02 |
| :---- | :---- |
| **Tên usecase** | Đăng xuất |
| **Mô tả** | Cho phép người dùng kết thúc phiên làm việc hiện tại trên hệ thống. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống, Giáo vụ, Người dùng. |
| **Tiền điều kiện** | Người dùng đang có phiên đăng nhập hợp lệ. |
| **Hậu điều kiện** | Phiên đăng nhập của người dùng được kết thúc. Các thông tin xác thực cục bộ được xóa và người dùng được chuyển về trang đăng nhập. |
| **Luồng tương tác chính** | Người dùng chọn "Đăng xuất" trên thanh điều hướng. Hệ thống hiển thị yêu cầu xác nhận đăng xuất. Người dùng xác nhận yêu cầu. Hệ thống thu hồi hoặc đưa refresh\_token vào danh sách vô hiệu hóa nếu cơ chế này được cấu hình. Hệ thống xóa token xác thực được lưu trên trình duyệt. Hệ thống kết thúc phiên đăng nhập và chuyển người dùng về trang login. |
| **Luồng tương tác thay thế** | 3a. Người dùng hủy xác nhận:  Hệ thống đóng hộp thoại và giữ nguyên phiên đăng nhập. |
| **Luồng tương tác ngoại lệ** | E1 \- Phiên đăng nhập đã hết hạn:  Hệ thống xóa thông tin xác thực cục bộ và chuyển người dùng về trang đăng nhập. |

| Mã usecase | UC-03 |
| :---- | :---- |
| **Tên usecase** | Quên mật khẩu |
| **Mô tả** | Cho phép người dùng xác thực quyền sở hữu tài khoản và đặt lại mật khẩu khi không nhớ mật khẩu hiện tại. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống, Giáo vụ, Người dùng. |
| **Tiền điều kiện** | Người dùng đang ở trang đăng nhập và có quyền truy cập địa chỉ email đã đăng ký. |
| **Hậu điều kiện** | Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu. Các mã hoặc liên kết khôi phục đã sử dụng bị vô hiệu hóa. Nếu khôi phục thất bại, mật khẩu hiện tại vẫn được giữ nguyên. |
| **Luồng tương tác chính** | Người dùng chọn "Quên mật khẩu" tại trang đăng nhập. Hệ thống hiển thị biểu mẫu yêu cầu nhập email tài khoản. Người dùng nhập email và chọn "Gửi yêu cầu". Hệ thống kiểm tra định dạng email và tạo mã OTP hoặc liên kết đặt lại mật khẩu có thời hạn. Hệ thống gửi mã hoặc liên kết xác thực đến email của người dùng và thông báo đã gửi yêu cầu. Người dùng sử dụng mã hoặc liên kết nhận được để mở biểu mẫu đặt lại mật khẩu. Người dùng nhập mật khẩu mới, xác nhận mật khẩu và chọn "Cập nhật mật khẩu". Hệ thống kiểm tra mã hoặc liên kết còn hợp lệ, đồng thời kiểm tra mật khẩu mới. Hệ thống băm mật khẩu mới, cập nhật vào cơ sở dữ liệu và vô hiệu hóa mã hoặc liên kết đã sử dụng. Hệ thống thông báo "Khôi phục mật khẩu thành công." và chuyển người dùng về trang đăng nhập. |
| **Luồng tương tác thay thế** | 5a. Người dùng không nhận được email:  Người dùng yêu cầu gửi lại mã hoặc liên kết khi thời gian chờ cho phép; hệ thống cấp thông tin xác thực mới. |
| **Luồng tương tác ngoại lệ** | E1 \- Email không tồn tại hoặc không hợp lệ:  Hệ thống thông báo yêu cầu không thể thực hiện và không tiết lộ thông tin tài khoản tồn tại. E2 \- Mã hoặc liên kết hết hạn hoặc không hợp lệ:  Hệ thống thông báo "Mã hoặc liên kết khôi phục không hợp lệ hoặc đã hết hạn." E3 \- Mật khẩu mới không đạt yêu cầu:  Hệ thống thông báo "Mật khẩu mới không hợp lệ hoặc không trùng khớp." E4 \- Lỗi gửi email hoặc lỗi lưu dữ liệu:  Hệ thống thông báo "Không thể khôi phục mật khẩu, vui lòng thử lại sau." |

| Mã usecase | UC-04 |
| :---- | :---- |
| **Tên usecase** | Xem thông tin cá nhân |
| **Mô tả** | Cho phép người dùng xem thông tin cá nhân đã lưu trong hệ thống. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống, Giáo vụ, Người dùng. |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Thông tin cá nhân hiện tại của người dùng được hiển thị; dữ liệu trong cơ sở dữ liệu không bị thay đổi. |
| **Luồng tương tác chính** | Người dùng truy cập trang cá nhân. Hệ thống xác thực phiên đăng nhập và quyền truy cập của người dùng. Hệ thống truy vấn thông tin cá nhân từ cơ sở dữ liệu. Hệ thống hiển thị các thông tin được phép xem, như họ tên, email, số điện thoại, ảnh đại diện và vai trò của người dùng. |
| **Luồng tương tác thay thế** | 3a. Người dùng tải lại trang:  Hệ thống truy vấn lại dữ liệu mới nhất từ cơ sở dữ liệu và hiển thị thông tin cập nhật. |
| **Luồng tương tác ngoại lệ** | E1 \- Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống thông báo yêu cầu đăng nhập và chuyển người dùng về trang /login. E2 \- Không tìm thấy thông tin cá nhân:  Hệ thống thông báo "Không tìm thấy thông tin cá nhân." E3 \- Lỗi truy vấn dữ liệu:  Hệ thống thông báo "Không thể tải thông tin cá nhân, vui lòng thử lại sau." |

| Mã usecase | UC-05 |
| :---- | :---- |
| **Tên usecase** | Cập nhật thông tin cá nhân |
| **Mô tả** | Cho phép người dùng chỉnh sửa và lưu các thông tin cá nhân được hệ thống cho phép cập nhật. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống, Giáo vụ, Người dùng. |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. Thông tin cá nhân của người dùng đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Thông tin hợp lệ được cập nhật và lưu vào cơ sở dữ liệu. Nếu cập nhật thất bại, thông tin cũ được giữ nguyên và hệ thống hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | Người dùng truy cập trang cá nhân. Hệ thống xác thực phiên đăng nhập và hiển thị thông tin hiện tại. Người dùng chọn "Chỉnh sửa". Hệ thống hiển thị biểu mẫu với các trường được phép cập nhật, như họ tên, số điện thoại và ảnh đại diện. Người dùng chỉnh sửa thông tin và chọn "Lưu thay đổi". Hệ thống kiểm tra tính hợp lệ của dữ liệu. Hệ thống cập nhật thông tin vào cơ sở dữ liệu. Hệ thống thông báo "Cập nhật thông tin cá nhân thành công." và hiển thị dữ liệu mới. |
| **Luồng tương tác thay thế** | 5a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác chỉnh sửa và giữ nguyên thông tin hiện tại. 5b. Người dùng không thay đổi thông tin:  Hệ thống không thực hiện cập nhật và giữ nguyên dữ liệu hiện tại. |
| **Luồng tương tác ngoại lệ** | E1 \- Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống thông báo yêu cầu đăng nhập và chuyển người dùng về trang đăng nhập. E2 \- Thông tin không hợp lệ:  Hệ thống thông báo "Thông tin cá nhân không hợp lệ." và giữ lại dữ liệu người dùng đã nhập để chỉnh sửa. E3 \- Dữ liệu đã được cập nhật ở nơi khác:  Hệ thống thông báo "Thông tin đã được cập nhật, vui lòng tải lại dữ liệu." và không ghi đè dữ liệu mới. E4 \- Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Cập nhật thông tin cá nhân thất bại." |

| Mã usecase | UC-06 |
| :---- | :---- |
| **Tên usecase** | Đổi mật khẩu |
| **Mô tả** | Cho phép người dùng thay đổi mật khẩu hiện tại sau khi xác thực mật khẩu cũ. |
| **Tác nhân** | Sinh viên, Giáo viên, Quản trị viên, Quản trị viên hệ thống, Giáo vụ, Người dùng. |
| **Tiền điều kiện** | Người dùng đã đăng nhập và có phiên xác thực hợp lệ. Người dùng biết mật khẩu hiện tại. |
| **Hậu điều kiện** | Mật khẩu mới được kiểm tra, băm và lưu vào cơ sở dữ liệu. Các phiên hoặc token cũ được xử lý theo chính sách bảo mật của hệ thống. Nếu đổi mật khẩu thất bại, mật khẩu cũ vẫn được giữ nguyên. |
| **Luồng tương tác chính** | Người dùng truy cập chức năng "Đổi mật khẩu" trong trang cá nhân. Hệ thống hiển thị biểu mẫu gồm Mật khẩu hiện tại, Mật khẩu mới và Xác nhận mật khẩu mới. Người dùng nhập đầy đủ thông tin và chọn "Đổi mật khẩu". Hệ thống xác thực phiên đăng nhập và đối chiếu mật khẩu hiện tại. Hệ thống kiểm tra mật khẩu mới đạt chính sách bảo mật và trùng với phần xác nhận. Hệ thống băm mật khẩu mới và lưu vào cơ sở dữ liệu. Hệ thống thông báo "Đổi mật khẩu thành công." |
| **Luồng tương tác thay thế** | 3a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác và giữ nguyên mật khẩu hiện tại. |
| **Luồng tương tác ngoại lệ** | E1 \- Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống yêu cầu người dùng đăng nhập lại. E2 \- Mật khẩu hiện tại không chính xác:  Hệ thống thông báo "Mật khẩu hiện tại không chính xác." E3 \- Mật khẩu mới không hợp lệ:  Hệ thống thông báo "Mật khẩu mới không đáp ứng yêu cầu bảo mật hoặc không trùng khớp." E4 \- Mật khẩu mới trùng mật khẩu hiện tại:  Hệ thống thông báo "Mật khẩu mới phải khác mật khẩu hiện tại." E5 \- Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Đổi mật khẩu thất bại." |

| Mã usecase | UC-07 |
| :---- | :---- |
| **Tên usecase** | Xem danh sách bài tập |
| **Mô tả** | Cho phép Sinh viên xem và tra cứu danh sách các bài tập được giao cho những lớp mà mình tham gia |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Danh sách bài tập phù hợp được hiển thị; dữ liệu bài tập không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên truy cập mục "Bài tập". Hệ thống xác thực phiên đăng nhập và quyền truy cập của Sinh viên. Hệ thống lấy danh sách lớp, môn học hoặc chủ đề mà Sinh viên đang tham gia. Hệ thống truy vấn các bài tập được giao cho Sinh viên theo những lớp hoặc môn học đó. Hệ thống hiển thị danh sách với các thông tin: Tên bài, lớp/chủ đề, độ khó, thời hạn nộp, trạng thái làm bài và điểm hiện có (chính thức hoặc tạm tính) nếu đã có kết quả. Sinh viên tìm kiếm hoặc lọc danh sách theo lớp, chủ đề hoặc trạng thái. |
| **Luồng tương tác thay thế** | 6a. Sinh viên không chọn bộ lọc:  Hệ thống hiển thị toàn bộ bài tập mà Sinh viên được phép xem. 6b. Không có bài tập phù hợp:  Hệ thống hiển thị danh sách rỗng và thông báo phù hợp. |
| **Luồng tương tác ngoại lệ** | E1 \- Phiên đăng nhập không hợp lệ hoặc đã hết hạn:  Hệ thống yêu cầu Sinh viên đăng nhập lại. E2 \- Lỗi truy vấn dữ liệu:  Hệ thống thông báo "Không thể tải danh sách bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-08 |
| :---- | :---- |
| **Tên usecase** | Xem chi tiết bài tập |
| **Mô tả** | Cho phép Sinh viên xem nội dung và yêu cầu chi tiết của một bài tập được giao. |
| **Tác nhân** | Sinh viên |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. Bài tập tồn tại trong hệ thống. |
| **Hậu điều kiện** | Thông tin bài tập được hiển thị nếu Sinh viên có quyền truy cập. Nếu Sinh viên chọn làm bài, hệ thống chuyển đến giao diện soạn thảo tương ứng. |
| **Luồng tương tác chính** | Sinh viên chọn một bài tập từ danh sách. Hệ thống kiểm tra Sinh viên có thuộc lớp được giao bài tập và bài tập có được phép truy cập hay không. Hệ thống lấy thông tin bài tập từ cơ sở dữ liệu. Hệ thống hiển thị đề bài, hỗ trợ Markdown và công thức toán học LaTeX nếu có. Hệ thống hiển thị yêu cầu Input/Output, ràng buộc, giới hạn thời gian, giới hạn bộ nhớ, Sample Test Cases và Rubric được công khai. Sinh viên chọn "Làm bài". Hệ thống chuyển Sinh viên đến giao diện làm bài và tải cấu hình cần thiết. |
| **Luồng tương tác thay thế** | 6a. Sinh viên quay lại danh sách:  Hệ thống không tạo hoặc thay đổi bài làm và đưa Sinh viên về danh sách bài tập. 6b. Bài tập đã quá hạn nhưng cho phép nộp muộn hoặc cho phép xem lại:  Hệ thống hiển thị cảnh báo về chính sách nộp muộn/xem lại và vẫn cho phép xem đề bài cũng như bấm "Làm bài". |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại:  Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Sinh viên không có quyền truy cập:  Hệ thống thông báo "Bạn không có quyền truy cập bài tập này." E3 \- Bài tập chưa mở hoặc đã đóng hoàn toàn:  Hệ thống thông báo "Bài tập hiện không khả dụng." E4 \- Lỗi tải dữ liệu:  Hệ thống thông báo "Không thể tải chi tiết bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-09 |
| :---- | :---- |
| **Tên usecase** | Viết code |
| **Mô tả** | Cho phép Sinh viên viết và chỉnh sửa mã nguồn trực tiếp trong trình soạn thảo của hệ thống. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có quyền truy cập bài tập. Bài tập có cấu hình ngôn ngữ lập trình được phép sử dụng. |
| **Hậu điều kiện** | Mã nguồn của Sinh viên được hiển thị và bản nháp gần nhất được lưu theo cơ chế autosave. Bài làm chưa được xem là submission chính thức cho đến khi Sinh viên chọn "Nộp bài". |
| **Luồng tương tác chính** | Sinh viên chọn "Làm bài" từ trang chi tiết bài tập. Hệ thống tải đề bài, ngôn ngữ và cấu hình bài tập. Hệ thống mở Monaco Editor với template code phù hợp. Sinh viên nhập hoặc chỉnh sửa mã nguồn. Hệ thống kiểm tra cơ bản nội dung editor và tự động lưu bản nháp theo khoảng thời gian được cấu hình. Sinh viên tiếp tục chỉnh sửa, hoàn thiện bài làm và chuyển sang bước nộp bài. |
| **Luồng tương tác thay thế** | 4a. Sinh viên tải lại trang:  Hệ thống khôi phục bản nháp gần nhất nếu bản nháp tồn tại. 6a. Sinh viên rời khỏi trang:  Hệ thống lưu bản nháp trước khi rời trang nếu kết nối còn hoạt động. |
| **Luồng tương tác ngoại lệ** | E1 \- Không tải được cấu hình bài tập:  Hệ thống thông báo "Không thể mở trình soạn thảo cho bài tập này." E2 \- Mã nguồn không hợp lệ hoặc vượt giới hạn:  Hệ thống thông báo lỗi và yêu cầu Sinh viên chỉnh sửa mã nguồn. E3 \- Lỗi lưu bản nháp:  Hệ thống thông báo "Không thể lưu bản nháp, vui lòng kiểm tra kết nối mạng." |

| Mã usecase | UC-10 |
| :---- | :---- |
| **Tên usecase** | Tải tệp bài làm lên |
| **Mô tả** | Cho phép Sinh viên tải mã nguồn từ máy tính vào bài làm đang mở. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã mở giao diện làm bài và có quyền truy cập bài tập. File mã nguồn có phần mở rộng thuộc danh sách ngôn ngữ được bài tập cho phép. |
| **Hậu điều kiện** | Nội dung file hợp lệ được nạp vào Monaco Editor và có thể được chỉnh sửa tiếp. File upload không được xem là submission chính thức cho đến khi Sinh viên nộp bài. |
| **Luồng tương tác chính** | Sinh viên chọn "Upload File" tại màn hình làm bài. Hệ thống hiển thị giao diện chọn file. Sinh viên chọn file mã nguồn từ máy tính. Hệ thống kiểm tra phần mở rộng, kích thước và nội dung cơ bản của file. Hệ thống đọc file và nạp nội dung vào Monaco Editor. Hệ thống lưu bản nháp của nội dung đã nạp. Hệ thống thông báo "Tải file lên thành công." |
| **Luồng tương tác thay thế** | 3a. Sinh viên hủy chọn file:  Hệ thống đóng hộp thoại và giữ nguyên nội dung đang có trong editor. 5a. Sinh viên tiếp tục chỉnh sửa:  Hệ thống cập nhật nội dung editor và lưu theo cơ chế autosave. |
| **Luồng tương tác ngoại lệ** | E1 \- Định dạng file không được hỗ trợ:  Hệ thống thông báo "Định dạng file không được hỗ trợ." E2 \- File vượt quá kích thước cho phép:  Hệ thống thông báo "Kích thước file vượt quá giới hạn cho phép." E3 \- Không thể đọc file:  Hệ thống thông báo "Không thể tải file, vui lòng chọn file khác." |

| Mã usecase | UC-11 |
| :---- | :---- |
| **Tên usecase** | Nộp bài |
| **Mô tả** | Cho phép Sinh viên gửi mã nguồn để hệ thống chấm chính thức và lưu kết quả bài làm. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có quyền làm bài. Bài tập còn hạn nộp hoặc cho phép nộp muộn. Lớp của bài tập đang ở trạng thái Hoạt động. Sinh viên đã nhập mã nguồn. |
| **Hậu điều kiện** | Một bài nộp được tạo và lưu với trạng thái xử lý tương ứng. Kết quả Auto-Grader và AI feedback được lưu khi quá trình chấm hoàn tất. Nếu không thể tiếp nhận bài, hệ thống sẽ không tạo bài nộp không đầy đủ. Chỉ bài nộp hợp lệ mới làm tăng số lần nộp. Nếu bài nộp gặp lỗi hệ thống hoặc được Giáo viên/Quản trị viên hệ thống miễn trừ không làm tăng số lần nộp. |
| **Luồng tương tác chính** | Sinh viên kiểm tra mã nguồn và chọn "Nộp bài". Hệ thống kiểm tra quyền nộp, thời hạn, ngôn ngữ và dữ liệu bài nộp. Web Client gửi trực tiếp mã nguồn cùng thông tin bài tập đến API nộp bài mà không qua bước chạy thử trước. Backend tạo bài nộp với trạng thái PENDING và đưa tác vụ vào hàng đợi xử lý. Hệ thống trả về mã bài nộp (submission ID) và hiển thị trạng thái "Đang chấm bài...". Grader Worker lấy tác vụ, gửi mã nguồn và toàn bộ Hidden Test Cases đến Docker Sandbox. Docker Sandbox biên dịch nếu cần, thực thi code cách ly và trả về execution evidence gồm output, lỗi, thời gian chạy, bộ nhớ và trạng thái từng test. Hệ thống thực hiện Auto-Grading: tính điểm Correctness theo trọng số các test case đạt; phân tích tĩnh (nếu được cấu hình) để đánh giá Code Quality và Complexity theo Rubric; tổng hợp điểm theo công thức của hệ thống. Hệ thống lưu kết quả chấm vào cơ sở dữ liệu. AI Engine tạo feedback dựa trên đề bài, mã nguồn và kết quả chấm; hệ thống lưu feedback nếu tác vụ thành công. Hệ thống cập nhật trạng thái bài nộp thành COMPLETED hoặc trạng thái lỗi tương ứng. Hệ thống thông báo trạng thái cho Sinh viên qua WebSocket hoặc polling. |
| **Luồng tương tác thay thế** | 2a. Sinh viên xác nhận nộp bài muộn:  Hệ thống tiếp nhận bài nộp và áp dụng quy định phạt điểm nếu bài tập cho phép nộp muộn. 5a. Sinh viên rời khỏi trang:  Hệ thống tiếp tục xử lý bài nộp; Sinh viên có thể xem trạng thái từ lịch sử làm bài. |
| **Luồng tương tác ngoại lệ** | E1 \- Hết hạn nộp bài:  Hệ thống thông báo "Đã hết hạn nộp bài." E2 \- Mã nguồn không hợp lệ:  Hệ thống thông báo "Bài nộp không hợp lệ." E3 \- Không thể đưa tác vụ vào hàng đợi:  Hệ thống thông báo "Không thể tiếp nhận bài nộp, vui lòng thử lại sau." E4 \- Lỗi khi chấm bài:  Hệ thống cập nhật bài nộp (submission) ở trạng thái lỗi và thông báo "Chấm bài thất bại, vui lòng thử lại sau." E5 \- Phiên chấm bị dừng:  Hệ thống chuyển bài nộp sang trạng thái "Bị gián đoạn", không tự chấm lại và thông báo Sinh viên nộp lại; lượt nộp này không tính vào số lần nộp.  E6 \- Đã đạt số lần nộp tối đa:  Hệ thống thông báo "Bạn đã hết số lần nộp bài cho phép." và không tạo bài nộp mới.  |

| Mã usecase | UC-12 |
| :---- | :---- |
| **Tên usecase** | Xem kết quả Auto-Grader |
| **Mô tả** | Cho phép Sinh viên xem kết quả chấm tự động của một bài nộp. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và bài nộp thuộc về Sinh viên. |
| **Hậu điều kiện** | Kết quả Auto-Grader được hiển thị; dữ liệu chấm không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên mở một bài nộp từ lịch sử làm bài hoặc trang kết quả. Hệ thống kiểm tra quyền truy cập bài nộp. Hệ thống lấy kết quả Auto-Grader. Hệ thống hiển thị điểm số, trạng thái tổng quát và thời gian chấm. Hệ thống hiển thị trạng thái từng test case, thời gian thực thi, mức sử dụng bộ nhớ và lỗi nếu có (dữ liệu Input/Output của Hidden Test Cases được bảo mật và ẩn khỏi Sinh viên).  Sinh viên xem chi tiết kết quả chấm bài. |
| **Luồng tương tác thay thế** | 4a. Bài nộp đang được xử lý:   Hệ thống hiển thị trạng thái PENDING hoặc RUNNING, hoặc "Bị gián đoạn" (kèm hướng dẫn nộp lại) và cho phép Sinh viên tải lại kết quả. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài nộp không tồn tại:  Hệ thống thông báo "Không tìm thấy bài nộp." E2 \- Sinh viên không có quyền truy cập:  Hệ thống từ chối yêu cầu và không hiển thị dữ liệu bài nộp. E3 \- Chưa có kết quả chấm:  Hệ thống thông báo "Kết quả chấm bài chưa sẵn sàng." |

| Mã usecase | UC-13 |
| :---- | :---- |
| **Tên usecase** | Xem nhận xét AI |
| **Mô tả** | Cho phép Sinh viên xem nhận xét do AI tạo ra dựa trên bài làm và kết quả chấm. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và bài nộp thuộc về Sinh viên. Bài nộp đã có kết quả chấm hoặc đủ dữ liệu để tạo feedback. |
| **Hậu điều kiện** | Nhận xét AI được hiển thị nếu đã được tạo; dữ liệu bài nộp không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên mở trang kết quả của một bài nộp. Hệ thống kiểm tra quyền truy cập và trạng thái AI feedback. Hệ thống lấy nhận xét AI đã lưu. Hệ thống hiển thị nhận xét về lỗi, chất lượng mã nguồn, độ phức tạp và đề xuất cải thiện nếu có. Sinh viên xem và sử dụng nhận xét để cải thiện bài làm. |
| **Luồng tương tác thay thế** | 3a. AI feedback đang được tạo:  Hệ thống hiển thị trạng thái chờ và cập nhật khi feedback sẵn sàng. 3b. AI feedback chưa được bật cho bài tập:  Hệ thống thông báo tính năng không khả dụng cho bài nộp này. |
| **Luồng tương tác ngoại lệ** | E1 \- Không tìm thấy bài nộp:  Hệ thống thông báo "Không tìm thấy bài nộp." E2 \- Sinh viên không có quyền truy cập:  Hệ thống từ chối yêu cầu xem feedback. E3 \- AI Service gặp lỗi:  Hệ thống thông báo "Chưa thể tạo nhận xét AI, vui lòng thử lại sau." |

| Mã usecase | UC-14 |
| :---- | :---- |
| **Tên usecase** | Tương tác với AI Tutor |
| **Mô tả** | Cho phép Sinh viên trao đổi với AI Tutor để nhận gợi ý định hướng giải quyết bài tập theo phương pháp Socratic. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập. Sinh viên đang xem bài tập, bài làm hoặc kết quả bài nộp. |
| **Hậu điều kiện** | Câu hỏi và câu trả lời được hiển thị trong phiên hội thoại. Lịch sử hội thoại được lưu theo chính sách của hệ thống nếu chức năng lưu được bật. |
| **Luồng tương tác chính** | Sinh viên mở "AI Tutor" tại màn hình bài tập, IDE hoặc kết quả bài nộp. Hệ thống lấy context cần thiết gồm đề bài, mã nguồn, kết quả test và câu hỏi trước đó trong hội thoại. Sinh viên nhập câu hỏi và chọn "Gửi". Hệ thống kiểm tra câu hỏi, quyền truy cập context và giới hạn sử dụng. Backend gửi prompt kèm guardrails sư phạm đến AI Engine. AI Tutor phân tích context và tạo câu trả lời mang tính gợi mở, không cung cấp ngay toàn bộ lời giải nếu chính sách không cho phép. Hệ thống hiển thị câu trả lời trong khung hội thoại. Sinh viên tiếp tục đặt câu hỏi trong cùng phiên. |
| **Luồng tương tác thay thế** | 2a. Sinh viên không chọn bài làm hoặc bài nộp:  Hệ thống chỉ gửi context của đề bài và các thông tin được phép xem. 8a. Sinh viên bắt đầu hội thoại mới:  Hệ thống xóa context hội thoại trước khỏi phiên hiện tại và khởi tạo phiên mới. |
| **Luồng tương tác ngoại lệ** | E1 \- Câu hỏi rỗng hoặc vượt giới hạn:  Hệ thống yêu cầu Sinh viên nhập câu hỏi hợp lệ. E2 \- AI Service không khả dụng:  Hệ thống thông báo "AI Tutor hiện không khả dụng, vui lòng thử lại sau." E3 \- Nội dung yêu cầu không phù hợp chính sách:  Hệ thống từ chối yêu cầu và hiển thị thông báo phù hợp. |

| Mã usecase | UC-15 |
| :---- | :---- |
| **Tên usecase** | Xem lịch sử làm bài |
| **Mô tả** | Cho phép Sinh viên tra cứu các bài nộp của mình và xem chi tiết từng lần nộp bài. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Lịch sử bài nộp của Sinh viên được hiển thị; dữ liệu bài nộp không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên truy cập mục "Lịch sử làm bài" hoặc lịch sử nộp bài của một bài tập. Hệ thống xác thực phiên đăng nhập. Hệ thống truy vấn các bài nộp thuộc về Sinh viên. Hệ thống sắp xếp lịch sử theo thời gian và hiển thị bài tập, thời điểm nộp, trạng thái, điểm và ngôn ngữ. Sinh viên chọn một bài nộp để xem mã nguồn, kết quả test và feedback được phép xem. |
| **Luồng tương tác thay thế** | 4a. Sinh viên lọc lịch sử:  Hệ thống lọc theo bài tập, lớp, trạng thái hoặc khoảng thời gian. 5a. Sinh viên chọn hai bài nộp:  Hệ thống hiển thị phần khác nhau giữa các phiên bản nếu chức năng so sánh được hỗ trợ. |
| **Luồng tương tác ngoại lệ** | E1 \- Không có lịch sử bài nộp:  Hệ thống hiển thị danh sách rỗng và thông báo "Chưa có bài nộp nào." E2 \- Lỗi truy vấn dữ liệu:  Hệ thống thông báo "Không thể tải lịch sử làm bài, vui lòng thử lại sau." |

| Mã usecase | UC-16 |
| :---- | :---- |
| **Tên usecase** | Xem bảng điểm cá nhân |
| **Mô tả** | Cho phép Sinh viên xem tổng hợp điểm các bài tập và lớp học mà mình tham gia. |
| **Tác nhân** | Sinh viên. |
| **Tiền điều kiện** | Sinh viên đã đăng nhập và có phiên xác thực hợp lệ. |
| **Hậu điều kiện** | Bảng điểm cá nhân được hiển thị theo dữ liệu kết quả đã được chấm; dữ liệu điểm không bị thay đổi. |
| **Luồng tương tác chính** | Sinh viên truy cập trang "Bảng điểm". Hệ thống xác thực phiên đăng nhập. Hệ thống truy vấn các kết quả đã được chấm thuộc về Sinh viên. Hệ thống tổng hợp điểm theo bài tập và lớp học theo quy tắc đã cấu hình (Điểm chính thức là điểm chấm thủ công của bài nộp được Giáo viên chấm; nếu chưa có thì hiển thị điểm Auto-Grader theo chính sách tính điểm đã cấu hình (Highest Score hoặc Latest Score) cho bài tập, kèm nhãn 'Tạm tính' ; điểm AI chỉ để tham khảo). Hệ thống hiển thị bảng điểm gồm bài tập, lớp, điểm, trạng thái và thời gian cập nhật. Sinh viên xem hoặc lọc điểm theo bài tập, lớp hoặc khoảng thời gian. |
| **Luồng tương tác thay thế** | 6a. Sinh viên không chọn bộ lọc:  Hệ thống hiển thị toàn bộ bảng điểm mà Sinh viên được phép xem. 6b. Một số bài chưa có điểm cuối:  Hệ thống hiển thị trạng thái đang chờ chấm hoặc chưa có kết quả thay vì tự động coi là điểm 0\. |
| **Luồng tương tác ngoại lệ** | E1 \- Không có kết quả đã chấm:  Hệ thống hiển thị bảng điểm rỗng và thông báo "Chưa có kết quả được chấm." E2 \- Lỗi tổng hợp điểm:  Hệ thống thông báo "Không thể tải bảng điểm, vui lòng thử lại sau." |

| Mã usecase | UC-17 |
| :---- | :---- |
| **Tên usecase** | Tạo lớp học |
| **Mô tả** | Đây là chức năng quản lý lớp ở cấp Giáo viên, chỉ áp dụng đối với các lớp do Giáo viên phụ trách. Giáo viên được phép khởi tạo lớp học mới do mình phụ trách.  |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập và có quyền quản lý lớp trong tổ chức tương ứng. |
| **Hậu điều kiện** | Lớp học hợp lệ được tạo và gắn với Giáo viên; hệ thống sinh mã tham gia nếu cần. |
| **Luồng tương tác chính** | Giáo viên truy cập quản lý lớp và chọn "Tạo lớp". Hệ thống hiển thị biểu mẫu gồm tên lớp, mã lớp, mô tả, học kỳ hoặc niên khóa. Giáo viên nhập thông tin và chọn "Tạo lớp". Hệ thống kiểm tra quyền, định dạng dữ liệu và tính duy nhất của mã lớp. Hệ thống tạo lớp, gắn Giáo viên làm người phụ trách và sinh mã tham gia nếu cần. Hệ thống thông báo "Tạo lớp thành công." và hiển thị chi tiết lớp. |
| **Luồng tương tác thay thế** | 3a. Giáo viên chọn "Hủy":  Hệ thống đóng biểu mẫu và không tạo lớp. 3b. Giáo viên không nhập mã lớp:  Hệ thống tự sinh mã theo cấu hình. |
| **Luồng tương tác ngoại lệ** | E1 \- Dữ liệu không hợp lệ:  Hệ thống thông báo "Thông tin lớp học không hợp lệ." E2 \- Mã lớp đã tồn tại:  Hệ thống thông báo "Mã lớp đã tồn tại, vui lòng chọn mã khác." E3 \- Lỗi khi tạo lớp:  Hệ thống thông báo "Không thể tạo lớp, vui lòng thử lại sau." |

| Mã usecase | UC-18 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa lớp học |
| **Mô tả** | Đây là chức năng quản lý lớp ở cấp Giáo viên, chỉ áp dụng đối với các lớp do Giáo viên phụ trách. Cho phép Giáo viên cập nhật thông tin của lớp học do mình phụ trách. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập; lớp tồn tại và chưa bị xóa. Lớp đang ở trạng thái Hoạt động. |
| **Hậu điều kiện** | Thông tin hợp lệ của lớp được cập nhật; nếu thất bại, dữ liệu cũ được giữ nguyên. |
| **Luồng tương tác chính** | Giáo viên truy cập quản lý lớp và chọn lớp cần chỉnh sửa. Hệ thống kiểm tra quyền và hiển thị thông tin hiện tại. Giáo viên chỉnh sửa tên lớp, mô tả, học kỳ hoặc niên khóa. Giáo viên chọn "Lưu". Hệ thống kiểm tra dữ liệu và phiên bản hiện tại của lớp. Hệ thống cập nhật thông tin và thông báo "Cập nhật lớp thành công." |
| **Luồng tương tác thay thế** | 4a. Giáo viên chọn "Hủy":  Hệ thống bỏ các thay đổi chưa lưu. 4b. Giáo viên không thay đổi dữ liệu:  Hệ thống không tạo bản cập nhật mới. |
| **Luồng tương tác ngoại lệ** | E1 \- Không tìm thấy lớp:  Hệ thống thông báo "Không tìm thấy lớp học." E2 \- Giáo viên không có quyền:  Hệ thống từ chối yêu cầu và không hiển thị dữ liệu lớp. E3 \- Dữ liệu đã thay đổi ở nơi khác:  Hệ thống thông báo "Thông tin lớp đã thay đổi, vui lòng tải lại." |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

| Mã usecase | UC-20 |
| :---- | :---- |
| **Tên usecase** | Quản lý sinh viên trong lớp |
| **Mô tả** | Đây là chức năng quản lý lớp ở cấp Giáo viên, chỉ áp dụng đối với các lớp do Giáo viên phụ trách. Cho phép Giáo viên thêm hoặc xóa sinh viên khỏi lớp mình phụ trách. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập, có quyền quản lý và lớp đang ở trạng thái Hoạt động. |
| **Hậu điều kiện** | Danh sách thành viên được cập nhật theo yêu cầu hợp lệ. |
| **Luồng tương tác chính** | Giáo viên mở chi tiết lớp. Hệ thống hiển thị danh sách sinh viên hiện tại. Giáo viên chọn "Thêm sinh viên" hoặc chọn sinh viên và chọn "Xóa khỏi lớp". Với thao tác thêm, Giáo viên nhập email, mã sinh viên hoặc sử dụng mã tham gia lớp. Hệ thống kiểm tra tài khoản, tư cách thành viên và trạng thái lớp. Hệ thống cập nhật danh sách thành viên và hiển thị danh sách mới. |
| **Luồng tương tác thay thế** | 3a. Giáo viên thêm nhiều sinh viên:  Hệ thống xử lý danh sách và trả kết quả theo từng bản ghi. 3b. Giáo viên hủy thao tác xóa:  Hệ thống đóng hộp thoại và giữ nguyên thành viên. |
| **Luồng tương tác ngoại lệ** | E1 \- Không tìm thấy sinh viên:  Hệ thống thông báo "Không tìm thấy tài khoản sinh viên." E2 \- Sinh viên đã là thành viên:  Hệ thống bỏ qua bản ghi trùng và thông báo kết quả. E3 \- Không thể xóa sinh viên:  Hệ thống thông báo "Không thể xóa sinh viên khỏi lớp." |

| Mã usecase | UC-21 |
| :---- | :---- |
| **Tên usecase** | Quản lý/ Cấu hình bài tập |
| **Mô tả** | Cho phép Giáo viên tạo và cấu hình các thông tin, thời hạn, chính sách nộp bài và tiêu chí chấm điểm cho bài tập. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập vào hệ thống. Giáo viên có quyền quản lý bài tập trong lớp phụ trách. Lớp đang ở trạng thái Hoạt động. |
| **Hậu điều kiện** | Bài tập được tạo hoặc cập nhật thành công với các chính sách nộp bài và chấm điểm đã cấu hình. Hệ thống lưu số lần nộp tối đa, chính sách tính điểm và quy tắc nộp muộn của bài tập. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng quản lý bài tập. Hệ thống hiển thị danh sách các bài tập thuộc lớp. Giáo viên nhập thông tin để khởi tạo một bài tập mới.  Hệ thống hiển thị biểu mẫu thông tin bài tập. Giáo viên nhập hoặc cập nhật các thông tin của bài tập, bao gồm tên bài tập, mô tả, thời hạn và các yêu cầu liên quan. Giáo viên thiết lập số lần nộp tối đa cho bài tập. Giáo viên có thể chọn chế độ Không giới hạn số lần nộp bằng cách đặt giá trị giới hạn là 0 hoặc bỏ trống. Giáo viên thiết lập chính sách tính điểm cho bài tập, gồm Lấy điểm cao nhất (Highest Score) hoặc Lấy điểm lần nộp cuối (Latest Score). Giáo viên thiết lập quy tắc nộp muộn và tỷ lệ trừ điểm nếu bài tập cho phép nộp trong thời gian gia hạn. Giáo viên cấu hình các tiêu chí chấm điểm và trọng số tương ứng. Hệ thống kiểm tra tính hợp lệ của các thông tin cấu hình. Hệ thống lưu thông tin bài tập và các chính sách đã cấu hình. Hệ thống thông báo cấu hình bài tập thành công. |
| **Luồng tương tác thay thế** | 6a. Giáo viên chọn Không giới hạn số lần nộp: Hệ thống ghi nhận bài tập không giới hạn số lần nộp và tiếp tục luồng chính tại bước  8a. Giáo viên chọn Lấy điểm cao nhất: Hệ thống lưu chính sách Highest Score và tiếp tục luồng chính.  8b. Giáo viên chọn Lấy điểm lần nộp cuối: Hệ thống lưu chính sách Latest Score và tiếp tục luồng chính.  9a. Bài tập không cho phép nộp muộn: Hệ thống không áp dụng thời gian gia hạn hoặc mức trừ điểm và tiếp tục luồng chính.  |
| **Luồng tương tác ngoại lệ** | E1. Thông tin bài tập không hợp lệ: Hệ thống thông báo lỗi và yêu cầu Giáo viên kiểm tra, cập nhật lại thông tin. E2. Số lần nộp tối đa không hợp lệ: Hệ thống thông báo lỗi và yêu cầu Giáo viên nhập lại giá trị phù hợp. E3. Thời hạn hoặc thời gian gia hạn không hợp lệ: Hệ thống thông báo lỗi và yêu cầu Giáo viên kiểm tra lại thời gian cấu hình. E4. Không thể lưu cấu hình bài tập: Hệ thống thông báo lỗi và không ghi nhận thay đổi. |

| Mã usecase | UC-22 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa thông tin chung bài tập |
| **Mô tả** | Cho phép Giáo viên cập nhật các thông tin chung của bài tập do mình quản lý, gồm Tên bài tập, Đề bài, Ngôn ngữ hỗ trợ, Mức độ khó và Giới hạn tài nguyên. Chức năng này không bao gồm việc thay đổi Hạn nộp, Bộ Test Case hoặc Tiêu chí chấm điểm. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập. Bài tập tồn tại và đang ở trạng thái cho phép chỉnh sửa. |
| **Hậu điều kiện** | Thông tin chung của bài tập được cập nhật thành công Các bài nộp đã tồn tại không bị thay đổi bởi thao tác cập nhật thông tin chung.  |
| **Luồng tương tác chính** | Giáo viên mở danh sách bài tập và chọn bài cần chỉnh sửa. Hệ thống kiểm tra quyền truy cập và hiển thị thông tin bài tập hiện tại. Giáo viên chỉnh sửa thông tin chung của bài tập.  Giáo viên chọn "Lưu". Hệ thống kiểm tra tính hợp lệ của dữ liệu và tính tương thích với bài nộp hiện có. Hệ thống cập nhật bài tập hoặc lưu phiên bản mới theo quy định. Hệ thống thông báo "Cập nhật bài tập thành công." |
| **Luồng tương tác thay thế** | 5a. Bài tập đã được giao hoặc có bài nộp:  Hệ thống giới hạn các trường được phép sửa (chỉ cho sửa mô tả/đề bài) hoặc yêu cầu xác nhận tạo phiên bản mới trước khi lưu. . |
| **Luồng tương tác ngoại lệ** | E1 \- Không tìm thấy bài tập:  Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Giáo viên không có quyền:  Hệ thống từ chối yêu cầu và không cho phép chỉnh sửa. E3 \- Dữ liệu không hợp lệ:  Hệ thống thông báo "Thông tin bài tập không hợp lệ." E4 \- Lỗi khi lưu:  Hệ thống thông báo "Không thể cập nhật bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-23 |
| :---- | :---- |
| **Tên usecase** | Xóa bài tập |
| **Mô tả** | Cho phép Giáo viên xóa hoặc vô hiệu hóa bài tập theo trạng thái và chính sách lưu trữ dữ liệu. |
| **Tác nhân** | Giáo viên. |
| **Tiền điều kiện** | Giáo viên đã đăng nhập, có quyền quản lý bài tập và bài tập tồn tại. |
| **Hậu điều kiện** | Bài tập được xóa mềm, vô hiệu hóa hoặc xóa theo chính sách; bài nộp, điểm và lịch sử liên quan được lưu theo chính sách. |
| **Luồng tương tác chính** | Giáo viên mở danh sách bài tập và chọn bài cần xóa. Giáo viên chọn "Xóa". Hệ thống hiển thị hộp thoại xác nhận và thông tin về dữ liệu bị ảnh hưởng. Giáo viên xác nhận thao tác. Hệ thống kiểm tra trạng thái bài tập, quyền truy cập và dữ liệu liên quan. Hệ thống thực hiện xóa mềm hoặc vô hiệu hóa bài tập theo quy tắc nghiệp vụ. Hệ thống thông báo "Xử lý bài tập thành công." và cập nhật lại danh sách. |
| **Luồng tương tác thay thế** | 5a. Bài tập đã có bài nộp:  Hệ thống chuyển bài tập sang trạng thái vô hiệu hóa / xóa mềm thay vì xóa dữ liệu vật lý.  |
| **Luồng tương tác ngoại lệ** | E1 \- Không tìm thấy bài tập:  Hệ thống thông báo "Bài tập không tồn tại hoặc đã được xử lý." E2 \- Bài tập đang được sử dụng:  Hệ thống thông báo "Bài tập đang có dữ liệu liên quan và không thể xóa trực tiếp." E3 \- Lỗi xử lý:  Hệ thống thông báo "Không thể xóa hoặc vô hiệu hóa bài tập, vui lòng thử lại sau." |

| Mã usecase | UC-24 |
| :---- | :---- |
| **Tên usecase** | Thiết lập hạn nộp bài |
| **Mô tả** | Chức năng này cho phép Giáo viên thiết lập và điều chỉnh thời hạn nộp bài cho một bài tập đã được tạo. |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập, có quyền quản lý bài tập của lớp. Bài tập đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Hạn nộp bài mới được cập nhật thành công và áp dụng cho tất cả sinh viên thuộc các lớp được giao bài tập này.  Nếu thất bại, giữ nguyên hạn nộp cũ.  |
| **Luồng tương tác chính** | Giáo viên truy cập danh sách bài tập và chọn bài tập cần thiết lập hạn nộp. Hệ thống hiển thị thông tin bài tập và hạn nộp hiện tại (nếu có). Giáo viên nhập/chọn ngày và giờ hạn nộp bài mới. Giáo viên chọn "Lưu". Hệ thống kiểm tra tính hợp lệ của thời gian (phải lớn hơn thời điểm hiện tại). Hệ thống cập nhật hạn nộp bài mới vào CSDL. Hệ thống thông báo "Thiết lập hạn nộp bài thành công." và hiển thị hạn nộp mới. |
| **Luồng tương tác thay thế** | 3a. Bài tập chưa từng thiết lập hạn nộp:  Hệ thống tạo mới bản ghi hạn nộp bài và lưu vào CSDL.  |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại:  Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Hạn nộp không hợp lệ:  Hệ thống thông báo "Hạn nộp bài không hợp lệ hoặc phải lớn hơn thời điểm hiện tại." E3 \- Bài tập đã kết thúc/Đã đóng:  Hệ thống thông báo "Không thể thay đổi hạn nộp bài của bài tập đã đóng." E4 \- Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Thiết lập hạn nộp bài thất bại." |

| Mã usecase | UC-25 |
| :---- | :---- |
| **Tên usecase** | Thiết lập test case |
| **Mô tả** | Cho phép Giáo viên quản lý bộ Test Case (thêm, sửa, xóa) của một bài tập phục vụ chấm điểm tự động.  |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập; có quyền quản lý bài tập; bài tập đã tồn tại trên hệ thống.  |
| **Hậu điều kiện** | Bộ Test Case được cập nhật thành công và sẵn sàng sử dụng cho lượt nộp của sinh viên.  |
| **Luồng tương tác chính** | Giáo viên truy cập danh sách bài tập và chọn bài tập cần thiết lập Test Case. Hệ thống hiển thị thông tin bài tập và danh sách Test Case hiện có. Giáo viên thực hiện cấu hình bộ Test Case (Thêm mới, Chỉnh sửa, hoặc Xóa các Test Case). Đối với mỗi Test Case, Giáo viên nhập: Input, Output mong đợi, Phân loại (Sample/Hidden) và Trọng số điểm. Giáo viên chọn "Lưu". Hệ thống kiểm tra tính hợp lệ của bộ Test Case. Hệ thống lưu bộ Test Case vào CSDL và hiển thị thông báo "Thiết lập Test Case thành công." |
| **Luồng tương tác thay thế** | 3a. Xóa Test Case:  Giáo viên chọn xóa một Test Case. Hệ thống yêu cầu xác nhận. Giáo viên xác nhận. Hệ thống xoá khỏi danh sách tạm trước khi Lưu. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại:  Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Thông tin Test Case không hợp lệ:  Hệ thống thông báo "Dữ liệu đầu vào hoặc kết quả đầu ra của Test Case không được để trống." E3 \- Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Thiết lập Test Case thất bại." |

| Mã usecase | UC-26 |
| :---- | :---- |
| **Tên usecase** | Thiết lập rubric |
| **Mô tả** | Cho phép Giáo viên quản lý bộ tiêu chí và mức điểm đánh giá (Rubric) cho bài tập.  |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập; có quyền quản lý bài tập; bài tập đã tồn tại trên hệ thống.  |
| **Hậu điều kiện** | Rubric được lưu thành công làm cơ sở tính điểm tổng hợp cho bài nộp của sinh viên.  |
| **Luồng tương tác chính** | Giáo viên truy cập danh sách bài tập và chọn bài tập cần thiết lập Rubric. Hệ thống hiển thị danh sách các tiêu chí đánh giá hiện tại. Giáo viên cấu hình danh sách tiêu chí (Tên tiêu chí, Mô tả, Mức điểm/Trọng số).  Lưu ý: Tiêu chí Correctness do hệ thống tự động tính từ Test Case. Giáo viên chọn "Lưu". Hệ thống kiểm tra tổng trọng số/điểm các tiêu chí và tính hợp lệ của Rubric. Hệ thống lưu thông tin Rubric vào CSDL và hiển thị thông báo "Thiết lập Rubric thành công." |
| **Luồng tương tác thay thế** | 3a. Xóa tiêu chí:  Giáo viên chọn xóa một tiêu chí (khác Correctness). Hệ thống yêu cầu xác nhận.  Giáo viên xác nhận.  Xóa khỏi danh sách tạm. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại:  Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Trùng tiêu chí:  Hệ thống thông báo "Tên tiêu chí đánh giá bị trùng lặp." E3 \- Tổng trọng số không hợp lệ:  Hệ thống thông báo "Tổng trọng số của các tiêu chí phải bằng 100% (hoặc tổng thang điểm quy định)." E4 \- Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Thiết lập Rubric thất bại." |

| Mã usecase | UC-27 |
| :---- | :---- |
| **Tên usecase** | Giao bài tập cho lớp |
| **Mô tả** | Giáo viên giao một bài tập đã có trong hệ thống cho một hoặc nhiều lớp học để sinh viên thực hiện. |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền quản lý và giao bài tập. Bài tập cần giao đã tồn tại trong hệ thống. Lớp học cần giao bài đã tồn tại và Giáo viên có quyền quản lý lớp. |
| **Hậu điều kiện** | Bài tập được giao thành công cho lớp đã chọn. Thông tin giao bài được lưu vào cơ sở dữ liệu. Sinh viên thuộc lớp được giao bài có thể xem và thực hiện bài tập. Nếu giao bài không thành công, hệ thống giữ nguyên thông tin hiện tại và hiển thị thông báo lỗi. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng "Quản lý bài tập". Hệ thống hiển thị danh sách bài tập. Giáo viên chọn bài tập cần giao. Hệ thống hiển thị thông tin chi tiết của bài tập. Giáo viên chọn chức năng "Giao bài tập". Hệ thống hiển thị danh sách các lớp mà Giáo viên có quyền quản lý. Giáo viên chọn lớp cần giao bài tập. Giáo viên thiết lập các thông tin giao bài nếu cần. Giáo viên chọn "Giao bài". Hệ thống kiểm tra tính hợp lệ của thông tin giao bài. Hệ thống lưu thông tin giao bài vào cơ sở dữ liệu. Hệ thống thông báo "Giao bài tập thành công." |
| **Luồng tương tác thay thế** | 7a. Giáo viên chọn nhiều lớp: Hệ thống cho phép Giáo viên chọn nhiều lớp để giao cùng một bài tập. Giáo viên xác nhận giao bài. Hệ thống tạo thông tin giao bài cho các lớp đã chọn. 7b. Giáo viên giao bài đã từng giao cho lớp:  Hệ thống hiển thị thông tin bài tập đã được giao cho lớp.  Giáo viên xác nhận giao lại bài tập hoặc cập nhật cấu hình giao bài.  Hệ thống cập nhật thông tin giao bài theo lựa chọn của Giáo viên. 9a. Giáo viên chọn "Hủy": Hệ thống hủy thao tác giao bài và giữ nguyên thông tin hiện tại. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Không tìm thấy lớp học hoặc lớp không còn hoạt động:  Hệ thống thông báo "Không tìm thấy lớp học hoặc lớp không còn hoạt động." E3 \- Giáo viên không có quyền quản lý lớp: Hệ thống thông báo "Bạn không có quyền giao bài tập cho lớp này." E4 \- Thông tin giao bài không hợp lệ: Hệ thống thông báo "Thông tin giao bài không hợp lệ." E5 \- Lỗi khi lưu dữ liệu: Hệ thống thông báo "Giao bài tập thất bại." |

| Mã usecase | UC-28 |
| :---- | :---- |
| **Tên usecase** | Xem bài nộp |
| **Mô tả** | Giáo viên xem thông tin và kết quả bài nộp của sinh viên đối với một bài tập đã được giao. |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền quản lý bài tập. Bài tập đã được giao cho lớp. Sinh viên đã thực hiện và nộp bài tập. |
| **Hậu điều kiện** | Giáo viên xem được thông tin bài nộp của sinh viên. Hệ thống hiển thị mã bài nộp, thời gian nộp, mã nguồn, kết quả kiểm thử và điểm số nếu đã được chấm. Không có dữ liệu nào bị thay đổi trong hệ thống. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng "Quản lý bài tập". Hệ thống hiển thị danh sách bài tập. Giáo viên chọn bài tập cần xem bài nộp. Hệ thống hiển thị danh sách sinh viên và trạng thái nộp bài. Giáo viên chọn sinh viên cần xem bài nộp. Hệ thống hiển thị danh sách các bài nộp của sinh viên. Giáo viên chọn một bài nộp. Hệ thống hiển thị thông tin chi tiết bài nộp gồm mã nguồn, thời gian nộp, kết quả kiểm thử, kết quả phân tích và điểm số nếu có. Giáo viên xem thông tin bài nộp. |
| **Luồng tương tác thay thế** | 7a. Sinh viên có nhiều bài nộp: Hệ thống hiển thị toàn bộ các bài nộp của sinh viên theo thời gian nộp. Giáo viên chọn bài nộp cần xem. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Sinh viên không tồn tại: Hệ thống thông báo "Không tìm thấy sinh viên." E3 \- Không tìm thấy bài nộp: Hệ thống thông báo "Không tìm thấy bài nộp." E4 \- Bài nộp không có mã nguồn: Hệ thống thông báo "Không có mã nguồn trong bài nộp." E5 \- Kết quả chấm chưa có: Hệ thống thông báo "Bài nộp chưa có kết quả chấm." E6 \- Lỗi khi tải dữ liệu: Hệ thống thông báo "Không thể tải thông tin bài nộp." |

| Mã usecase | UC-29 |
| :---- | :---- |
| **Tên usecase** | Xem điểm |
| **Mô tả** | Giáo viên xem điểm và kết quả đánh giá bài làm của sinh viên đối với các bài tập đã được giao. |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền xem kết quả bài tập. Bài tập đã được giao cho lớp. |
| **Hậu điều kiện** | Giáo viên xem được điểm và kết quả đánh giá của sinh viên. Thông tin trong hệ thống không bị thay đổi. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng "Xem điểm". Hệ thống hiển thị danh sách các bài tập đã giao. Giáo viên chọn bài tập cần xem điểm. Hệ thống hiển thị danh sách sinh viên trong lớp và điểm tương ứng. Giáo viên chọn sinh viên cần xem chi tiết. Hệ thống hiển thị điểm và kết quả đánh giá bài làm của sinh viên. Giáo viên xem thông tin điểm và kết quả đánh giá. |
| **Luồng tương tác thay thế** | 5a. Giáo viên chọn lớp khác: Hệ thống hiển thị danh sách sinh viên và điểm của lớp được chọn. 5b. Giáo viên chọn sinh viên khác: Hệ thống hiển thị điểm và kết quả đánh giá của sinh viên được chọn. 5c. Giáo viên chọn xem chi tiết điểm: Hệ thống hiển thị điểm theo từng tiêu chí đánh giá và kết quả kiểm thử của bài làm. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Không tìm thấy sinh viên: Hệ thống thông báo "Không tìm thấy sinh viên." E3 \- Chưa có kết quả chấm: Hệ thống thông báo "Bài tập chưa có kết quả chấm." E4 \- Không có điểm: Hệ thống thông báo "Sinh viên chưa có điểm." E5 \- Lỗi khi tải dữ liệu: Hệ thống thông báo "Không thể tải thông tin điểm." |

| Mã usecase | UC-30 |
| :---- | :---- |
| **Tên usecase** | Xem AI đánh giá |
| **Mô tả** | Giáo viên xem kết quả đánh giá bài làm của sinh viên do hệ thống AI thực hiện dựa trên kết quả kiểm thử, phân tích mã nguồn và các tiêu chí đánh giá. |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền xem kết quả đánh giá. Bài tập đã được giao cho lớp. |
| **Hậu điều kiện** | Giáo viên xem được kết quả đánh giá của AI. Hệ thống hiển thị điểm AI, kết quả kiểm thử, kết quả phân tích mã nguồn và nhận xét đánh giá. Không có dữ liệu nào bị thay đổi trong hệ thống. |
| **Luồng tương tác chính** | Giáo viên chọn chức năng "Xem AI đánh giá". Hệ thống hiển thị danh sách bài tập đã được giao. Giáo viên chọn bài tập cần xem kết quả đánh giá AI. Hệ thống hiển thị danh sách sinh viên và trạng thái đánh giá AI. Giáo viên chọn sinh viên cần xem. Hệ thống hiển thị danh sách bài nộp của sinh viên. Giáo viên chọn bài nộp cần xem đánh giá AI. Hệ thống hiển thị kết quả đánh giá AI gồm điểm đánh giá, kết quả Test Case, kết quả phân tích mã nguồn và nhận xét. Giáo viên xem kết quả đánh giá AI.  |
| **Luồng tương tác thay thế** | 7a. Giáo viên chọn sinh viên khác: Hệ thống hiển thị danh sách bài nộp của sinh viên được chọn. 7b. Giáo viên chọn bài nộp khác: Hệ thống hiển thị kết quả đánh giá AI của bài nộp được chọn. 7c. Giáo viên chọn xem chi tiết đánh giá: Hệ thống hiển thị chi tiết điểm đánh giá theo từng tiêu chí. Hệ thống hiển thị kết quả từng Test Case và kết quả phân tích mã nguồn tương ứng. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Sinh viên không tồn tại: Hệ thống thông báo "Không tìm thấy sinh viên." E3 \- Không tìm thấy bài nộp: Hệ thống thông báo "Không tìm thấy bài nộp." E4 \- AI chưa đánh giá bài nộp: Hệ thống thông báo "Bài nộp chưa có kết quả đánh giá AI." E5 \- Kết quả đánh giá AI không đầy đủ: Hệ thống thông báo "Kết quả đánh giá AI chưa đầy đủ." E6 \- Lỗi khi tải kết quả đánh giá: Hệ thống thông báo "Không thể tải kết quả đánh giá AI." |

| Mã usecase | UC-31 |
| :---- | :---- |
| **Tên usecase** | Đánh giá/chấm bài thủ công |
| **Mô tả** | Giáo viên đánh giá và chấm điểm bài làm của sinh viên theo Rubric đã thiết lập cho bài tập. |
| **Tác nhân** | Giáo viên |
| **Tiền điều kiện** | Giáo viên đã đăng nhập hệ thống. Giáo viên có quyền chấm bài. Bài tập đã được giao cho lớp. Sinh viên đã nộp bài. |
| **Hậu điều kiện** | Điểm và nhận xét của Giáo viên được lưu cho bài nộp.   Điểm chấm thủ công được ưu tiên: bài nộp đã có điểm chấm thủ công thì dùng điểm này làm điểm chính thức; điểm Auto-Grader và AI được giữ lại để tham khảo, không bị xóa.   Trường hợp Giáo viên lưu tạm (chưa hoàn tất chấm) thì chưa áp dụng điểm thủ công.   Khi chưa có điểm thủ công, điểm Auto-Grader được xác định theo chính sách tính điểm của bài tập (Highest Score hoặc Latest Score) được hiển thị ở trạng thái "Tạm tính". |
| **Luồng tương tác chính** | Giáo viên chọn chức năng "Chấm bài". Hệ thống hiển thị danh sách bài tập đã được giao. Giáo viên chọn bài tập cần chấm. Hệ thống hiển thị danh sách sinh viên và trạng thái chấm bài. Giáo viên chọn sinh viên cần chấm. Hệ thống hiển thị bài nộp của sinh viên gồm mã nguồn và các thông tin liên quan. Giáo viên xem và đánh giá bài làm theo từng tiêu chí trong Rubric. Giáo viên nhập điểm và nhận xét cho bài làm. Giáo viên chọn "Lưu kết quả". Hệ thống kiểm tra tính hợp lệ của điểm và thông tin đánh giá. Hệ thống lưu kết quả chấm bài vào cơ sở dữ liệu. Hệ thống thông báo "Chấm bài thành công." |
| **Luồng tương tác thay thế** | 7a. Giáo viên chỉnh sửa điểm: Hệ thống hiển thị điểm hiện tại. Giáo viên điều chỉnh điểm theo từng tiêu chí trong Rubric. Hệ thống cập nhật tổng điểm theo điểm đã điều chỉnh. 7b. Giáo viên lưu bài chấm tạm thời: Hệ thống lưu các thông tin đánh giá hiện tại nhưng chưa hoàn tất chấm bài. Giáo viên có thể tiếp tục chấm bài sau. |
| **Luồng tương tác ngoại lệ** | E1 \- Bài tập không tồn tại: Hệ thống thông báo "Không tìm thấy bài tập." E2 \- Không tìm thấy bài nộp: Hệ thống thông báo "Không tìm thấy bài nộp." E3 \- Bài tập chưa có Rubric: Hệ thống thông báo "Bài tập chưa được thiết lập Rubric." E4 \- Điểm không hợp lệ: Hệ thống thông báo "Điểm đánh giá không hợp lệ." E5 \- Tổng điểm vượt quá mức quy định: Hệ thống thông báo "Tổng điểm không hợp lệ." E6 \- Lỗi khi lưu kết quả: Hệ thống thông báo "Chấm bài thất bại." |

| Mã usecase | UC-32 |
| :---- | :---- |
| **Tên usecase** | Tạo tài khoản người dùng |
| **Mô tả** | Quản trị viên tạo tài khoản cho Sinh viên, Giáo viên hoặc Giáo vụ để người dùng có thể đăng nhập và sử dụng hệ thống theo vai trò được cấp.  |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập, có quyền quản lý tài khoản người dùng. |
| **Hậu điều kiện** | Tài khoản Sinh viên, Giáo viên hoặc Giáo vụ được tạo thành công.  Thông tin tài khoản được lưu vào cơ sở dữ liệu.  Tài khoản được gán đúng vai trò và trạng thái hoạt động.  Người dùng phải đổi mật khẩu ở lần đăng nhập đầu tiên.  |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng "Quản lý tài khoản".  Hệ thống hiển thị danh sách tài khoản người dùng.  Quản trị viên chọn "Tạo tài khoản".  Hệ thống hiển thị biểu mẫu tạo tài khoản.  Quản trị viên nhập thông tin tài khoản gồm họ tên, email.  Quản trị viên chọn vai trò "Sinh viên", "Giáo viên" hoặc "Giáo vụ".  Quản trị viên chọn "Tạo tài khoản".  Hệ thống kiểm tra tính hợp lệ của thông tin tài khoản.  Hệ thống sinh mật khẩu tạm, đánh dấu bắt buộc đổi và gửi email.  Hệ thống tạo và lưu tài khoản vào cơ sở dữ liệu. Hệ thống thông báo "Tạo tài khoản thành công."  |
| **Luồng tương tác thay thế** | 4a. Quản trị viên chọn "Hủy":  Hệ thống hủy thao tác tạo tài khoản và quay lại danh sách tài khoản.  5a. Quản trị viên tạo tài khoản với trạng thái không hoạt động:  Quản trị viên chọn trạng thái tài khoản không hoạt động.  Hệ thống tạo tài khoản với trạng thái không hoạt động.  |
| **Luồng tương tác ngoại lệ** | E1 \- Thông tin tài khoản không hợp lệ: Hệ thống thông báo "Thông tin tài khoản không hợp lệ." E2 \- Email đã tồn tại: Hệ thống thông báo "Email đã được sử dụng." E3 \- Chưa chọn vai trò: Hệ thống thông báo "Vui lòng chọn vai trò cho tài khoản." E4 \- Lỗi khi tạo tài khoản: Hệ thống thông báo "Tạo tài khoản thất bại." |

| Mã usecase | UC-33 |
| :---- | :---- |
| **Tên usecase** | Khóa/mở tài khoản |
| **Mô tả** | Quản trị viên khóa hoặc mở khóa tài khoản Sinh viên, Giáo viên hoặc Giáo vụ nhằm quản lý trạng thái hoạt động của tài khoản trong hệ thống.  |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý tài khoản người dùng. Tài khoản cần khóa hoặc mở khóa đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Trạng thái tài khoản được cập nhật thành công.  Tài khoản bị khóa không thể đăng nhập và sử dụng hệ thống.  Khi khóa tài khoản, hệ thống thu hồi các phiên đăng nhập hiện tại. Tài khoản được mở khóa có thể đăng nhập và sử dụng hệ thống. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng "Quản lý tài khoản".  Hệ thống hiển thị danh sách tài khoản người dùng.  Quản trị viên chọn tài khoản cần khóa hoặc mở khóa.  Hệ thống hiển thị thông tin và trạng thái hiện tại của tài khoản.  Quản trị viên chọn "Khóa tài khoản" hoặc "Mở khóa tài khoản".  Hệ thống hiển thị yêu cầu xác nhận thao tác.  Quản trị viên xác nhận thao tác.  Hệ thống cập nhật trạng thái tài khoản.  Hệ thống thông báo thao tác thành công.  |
| **Luồng tương tác thay thế** | 5a. Quản trị viên chọn "Khóa tài khoản": Hệ thống hiển thị thông tin tài khoản và yêu cầu xác nhận khóa. Quản trị viên xác nhận khóa tài khoản. Hệ thống chuyển trạng thái tài khoản sang "Đã khóa". 5b. Quản trị viên chọn "Mở khóa tài khoản": Hệ thống hiển thị thông tin tài khoản và yêu cầu xác nhận mở khóa. Quản trị viên xác nhận mở khóa tài khoản. Hệ thống chuyển trạng thái tài khoản sang "Hoạt động". 7a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên trạng thái tài khoản. |
| **Luồng tương tác ngoại lệ** | E1 \- Tài khoản không tồn tại: Hệ thống thông báo "Không tìm thấy tài khoản." E2 \- Tài khoản đã ở trạng thái được chọn: Hệ thống thông báo "Trạng thái tài khoản không cần thay đổi." E3 \- Tài khoản không thể khóa: Hệ thống thông báo "Không thể khóa tài khoản này." E4 \- Lỗi khi cập nhật trạng thái: Hệ thống thông báo "Cập nhật trạng thái tài khoản thất bại." |

| Mã usecase | UC-34 |
| :---- | :---- |
| **Tên usecase** | Xóa tài khoản |
| **Mô tả** | Quản trị viên xóa tài khoản Sinh viên, Giáo viên hoặc Giáo vụ khỏi hệ thống.  |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý tài khoản người dùng. Tài khoản cần xóa đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Tài khoản được xóa khỏi hệ thống. Tài khoản không thể đăng nhập và sử dụng hệ thống. Thông tin tài khoản được cập nhật hoặc xóa theo chính sách lưu trữ dữ liệu của hệ thống. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng "Quản lý tài khoản". Hệ thống hiển thị danh sách tài khoản người dùng. Quản trị viên chọn tài khoản cần xóa. Hệ thống hiển thị thông tin tài khoản được chọn. Quản trị viên chọn "Xóa tài khoản". Hệ thống hiển thị yêu cầu xác nhận thao tác xóa. Quản trị viên xác nhận xóa tài khoản. Hệ thống kiểm tra điều kiện xóa tài khoản. Hệ thống xóa tài khoản khỏi hệ thống. Hệ thống thông báo "Xóa tài khoản thành công." |
| **Luồng tương tác thay thế** | 7a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác xóa và giữ nguyên tài khoản. 8a. Tài khoản đang có dữ liệu bài nộp hoặc lịch sử điểm số:   Hệ thống chuyển sang cơ chế xóa mềm (Soft Delete) để bảo toàn tính toàn vẹn dữ liệu học tập. |
| **Luồng tương tác ngoại lệ** | E1 \- Tài khoản không tồn tại: Hệ thống thông báo "Không tìm thấy tài khoản." E2 \- Tài khoản không thể xóa: Hệ thống thông báo "Không thể xóa tài khoản này." E3 \- Lỗi khi xóa tài khoản: Hệ thống thông báo "Xóa tài khoản thất bại." |

| Mã usecase | UC-35 |
| :---- | :---- |
| **Tên usecase** | Phân quyền người dùng |
| **Mô tả** | Quản trị viên được phân quyền cho Sinh viên/Giáo viên và các quyền nghiệp vụ thuộc phạm vi của mình.  Quản trị viên hệ thống quản lý các vai trò/quyền quản trị cấp hệ thống, bao gồm quyền của Quản trị viên và Quản trị viên hệ thống.  |
| **Tác nhân** | Quản trị viên, Quản trị viên hệ thống |
| **Tiền điều kiện** | Người dùng  đã đăng nhập hệ thống. Người dùng có quyền quản lý và phân quyền người dùng. Tài khoản cần phân quyền đã tồn tại trong hệ thống. Người dùng chỉ được cấp các vai trò và quyền nằm trong phạm vi quyền của mình; việc cấp vai trò Quản trị viên hoặc Quản trị viên hệ thống chỉ do Quản trị viên hệ thống thực hiện.  Quản trị viên được phép cấp và thay đổi các vai trò nghiệp vụ gồm Sinh viên, Giáo viên và Giáo vụ trong phạm vi quản lý. |
| **Hậu điều kiện** | Quyền của người dùng được cập nhật thành công. Người dùng có thể thực hiện các chức năng tương ứng với quyền được cấp. Hệ thống lưu thông tin phân quyền vào cơ sở dữ liệu. |
| **Luồng tương tác chính** | Người dùng chức năng "Phân quyền người dùng". Hệ thống hiển thị danh sách tài khoản người dùng. Người dùng chọn tài khoản cần phân quyền. Hệ thống hiển thị thông tin và quyền hiện tại của tài khoản. Hệ thống hiển thị danh sách vai trò và quyền mà Người dùng được phép cấp. Người dùng chọn vai trò hoặc các quyền cần cấp cho người dùng. Người dùng xác nhận phân quyền. Hệ thống kiểm tra tính hợp lệ của quyền được chọn. Hệ thống cập nhật quyền của người dùng. Hệ thống thông báo "Phân quyền người dùng thành công." |
| **Luồng tương tác thay thế** | 6a. Người dùng thay đổi vai trò: Người dùng chọn vai trò mới cho người dùng. Hệ thống hiển thị các quyền tương ứng với vai trò mới. Người dùng xác nhận thay đổi. Hệ thống cập nhật vai trò và quyền của người dùng. 6b. Người dùng cấp thêm quyền: Hệ thống hiển thị danh sách quyền có thể cấp thêm. Người dùng chọn các quyền cần cấp. Hệ thống cập nhật quyền của người dùng. 6c. Người dùng thu hồi quyền: Hệ thống hiển thị các quyền hiện tại của người dùng. Người dùng chọn quyền cần thu hồi. Hệ thống cập nhật lại quyền của người dùng. 7a. Người dùng chọn "Hủy": Hệ thống hủy thao tác phân quyền và giữ nguyên quyền hiện tại của người dùng. |
| **Luồng tương tác ngoại lệ** | E1 \- Tài khoản không tồn tại: Hệ thống thông báo "Không tìm thấy tài khoản." E2 \- Vai trò không hợp lệ: Hệ thống thông báo "Vai trò được chọn không hợp lệ." E3 \- Quyền không hợp lệ: Hệ thống thông báo "Quyền được chọn không hợp lệ." E4 \- Không thể thay đổi quyền: Hệ thống thông báo "Không thể cập nhật quyền của tài khoản này." E5 \- Lỗi khi lưu thông tin phân quyền: Hệ thống thông báo "Phân quyền người dùng thất bại." E6 \- Cấp vai trò hoặc quyền vượt phạm vi cho phép:  Hệ thống thông báo "Bạn không có quyền cấp vai trò hoặc quyền này."  |

| Mã usecase | UC-36 |
| :---- | :---- |
| **Tên usecase** | Đặt lại mật khẩu |
| **Mô tả** | Quản trị viên đặt lại mật khẩu cho tài khoản khi người dùng yêu cầu hoặc gặp vấn đề khi đăng nhập. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý tài khoản người dùng. Tài khoản cần đặt lại mật khẩu đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Mật khẩu mới được cập nhật thành công cho tài khoản. Mật khẩu mới được lưu dưới dạng an toàn trong hệ thống. Người dùng có thể sử dụng mật khẩu mới để đăng nhập. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng "Quản lý tài khoản". Hệ thống hiển thị danh sách tài khoản người dùng. Quản trị viên chọn tài khoản cần đặt lại mật khẩu. Hệ thống hiển thị thông tin tài khoản. Quản trị viên chọn "Đặt lại mật khẩu". Hệ thống hiển thị biểu mẫu đặt lại mật khẩu. Hệ thống tự sinh mật khẩu tạm, đánh dấu bắt buộc đổi mật khẩu ở lần đăng nhập đầu và gửi mật khẩu tạm đến email của người dùng.  Quản trị viên chọn "Xác nhận". Hệ thống tạo mật khẩu tạm thời theo chính sách bảo mật. Hệ thống cập nhật mật khẩu mới vào cơ sở dữ liệu và thu hồi phiên làm việc hiện tại của người dùng. Hệ thống thông báo "Đặt lại mật khẩu thành công." |
| **Luồng tương tác thay thế** | 3a. Quản trị viên chọn tài khoản khác: Hệ thống hiển thị thông tin của tài khoản được chọn. Quản trị viên thực hiện thao tác đặt lại mật khẩu cho tài khoản mới. 6a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác đặt lại mật khẩu và giữ nguyên mật khẩu hiện tại. |
| **Luồng tương tác ngoại lệ** | E1 \- Tài khoản không tồn tại: Hệ thống thông báo "Không tìm thấy tài khoản." E2 \- Tài khoản không thể đặt lại mật khẩu: Hệ thống thông báo "Không thể đặt lại mật khẩu cho tài khoản này." E3 \- Lỗi khi cập nhật mật khẩu: Hệ thống thông báo "Đặt lại mật khẩu thất bại." |

| Mã usecase | UC-37 |
| :---- | :---- |
| **Tên usecase** | Nhập danh sách từ Excel/CSV |
| **Mô tả** | Quản trị viên nhập danh sách người dùng từ tệp Excel hoặc CSV vào hệ thống để tạo hoặc cập nhật thông tin tài khoản hàng loạt. |
| **Tác nhân** | Quản trị viên |
| **Tiền điều kiện** | Quản trị viên đã đăng nhập hệ thống. Quản trị viên có quyền quản lý và nhập dữ liệu người dùng. Tệp Excel hoặc CSV chứa danh sách người dùng đã được chuẩn bị và có đủ 5 cột bắt buộc. |
| **Hậu điều kiện** | Danh sách người dùng hợp lệ được nhập thành công vào hệ thống. Thông tin người dùng được lưu vào cơ sở dữ liệu. Hệ thống hiển thị kết quả nhập dữ liệu và các bản ghi không hợp lệ nếu có. |
| **Luồng tương tác chính** | Quản trị viên chọn chức năng "Nhập danh sách từ Excel/CSV". Hệ thống hiển thị giao diện nhập dữ liệu và hướng dẫn định dạng tệp. Quản trị viên chọn và tải lên tệp Excel hoặc CSV. Hệ thống kiểm tra định dạng và cấu trúc tệp. Hệ thống đọc và hiển thị dữ liệu trong tệp để quản trị viên kiểm tra. Hệ thống kiểm tra tính hợp lệ của từng bản ghi. Quản trị viên xác nhận nhập dữ liệu. Hệ thống lưu các bản ghi hợp lệ vào cơ sở dữ liệu. Hệ thống thông báo kết quả nhập dữ liệu. |
| **Luồng tương tác thay thế** | 5a. Quản trị viên tải lên tệp khác: Hệ thống hủy dữ liệu tệp hiện tại. Quản trị viên chọn tệp Excel hoặc CSV mới. Hệ thống thực hiện kiểm tra tệp mới. 6a. Quản trị viên chọn "Hủy": Hệ thống hủy thao tác nhập dữ liệu và không thay đổi dữ liệu hiện tại. 7a. Tệp chứa cả bản ghi hợp lệ và không hợp lệ: Hệ thống hiển thị danh sách các bản ghi không hợp lệ và lý do lỗi. Quản trị viên xác nhận tiếp tục nhập các bản ghi hợp lệ. Hệ thống lưu các bản ghi hợp lệ vào cơ sở dữ liệu. 7b. Tệp chứa tài khoản đã tồn tại: Hệ thống hiển thị các tài khoản đã tồn tại. Quản trị viên chọn bỏ qua hoặc cập nhật họ tên; email và vai trò không bị thay đổi qua chức năng này.  |
| **Luồng tương tác ngoại lệ** | E1 \- Tệp không đúng định dạng: Hệ thống thông báo "Tệp không đúng định dạng Excel hoặc CSV." E2 \- Tệp không đúng cấu trúc: Hệ thống thông báo "Cấu trúc tệp không hợp lệ." E3 \- Tệp không có dữ liệu: Hệ thống thông báo "Tệp không chứa dữ liệu." E4 \- Bản ghi không hợp lệ: Hệ thống thông báo "Không có dữ liệu hợp lệ để nhập." và cho phép tải tệp khác. E5 \- Lỗi khi đọc hoặc xử lý tệp: Hệ thống thông báo "Không thể đọc hoặc xử lý tệp." E6 \- Lỗi khi lưu dữ liệu: Hệ thống thông báo "Nhập dữ liệu thất bại." |

| Mã usecase | UC-38 |
| :---- | :---- |
| **Tên usecase** | Tạo lớp |
| **Mô tả** | Quản trị viên có thể tạo lớp trong toàn hệ thống;  Giáo vụ có thể tạo lớp trong phạm vi Khoa/Bộ môn được phân công.  |
| **Tác nhân** | Quản trị viên, Giáo vụ. |
| **Tiền điều kiện** | Người dùng đã đăng nhập với vai trò Quản trị viên (quyền toàn hệ thống) hoặc Giáo vụ (quyền trong phạm vi Khoa/Bộ môn được phân công).  |
| **Hậu điều kiện** | Lớp học được tạo thành công. Thông tin lớp được lưu vào cơ sở dữ liệu. Lớp có thể được sử dụng để quản lý Sinh viên và Giáo viên. |
| **Luồng tương tác chính** | Người dùng chọn chức năng "Quản lý lớp".  Hệ thống hiển thị danh sách các lớp học mà Người dùng có quyền xem:  Quản trị viên thấy toàn bộ lớp trong trường;  Giáo vụ chỉ thấy lớp thuộc Khoa/Bộ môn mình phụ trách.  Người dùng chọn "Tạo lớp".  Hệ thống hiển thị biểu mẫu tạo lớp học gồm tên lớp, mã lớp, mô tả, niên khóa, Khoa/Bộ môn và Giáo viên phụ trách (nếu có); nếu Người dùng là Giáo vụ, hệ thống tự động gán Khoa/Bộ môn theo phạm vi phụ trách và không cho chọn Khoa/Bộ môn khác.  Người dùng nhập thông tin lớp học và chọn "Tạo lớp".  Hệ thống kiểm tra tính hợp lệ của thông tin lớp học, tính duy nhất của mã lớp và phạm vi Khoa/Bộ môn (nếu là Giáo vụ).  Hệ thống tạo lớp và lưu thông tin vào cơ sở dữ liệu.  Hệ thống thông báo "Tạo lớp thành công." và hiển thị lớp mới trong danh sách.  |
| **Luồng tương tác thay thế** | 5a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác tạo lớp và quay lại danh sách lớp.  |
| **Luồng tương tác ngoại lệ** | E1 \- Thông tin lớp không hợp lệ: Hệ thống thông báo "Thông tin lớp không hợp lệ." E2 \- Mã lớp đã tồn tại: Hệ thống thông báo "Mã lớp đã tồn tại." E3 \- Tên lớp đã tồn tại: Hệ thống thông báo "Tên lớp đã tồn tại." E4 \- Giáo viên không tồn tại: Hệ thống thông báo "Không tìm thấy Giáo viên được chọn." E5 \- Lỗi khi lưu thông tin lớp: Hệ thống thông báo "Tạo lớp thất bại." E6 \- Giáo vụ chọn Khoa/Bộ môn ngoài phạm vi phụ trách: Hệ thống thông báo "Bạn không có quyền tạo lớp trong Khoa/Bộ môn này.” |

| Mã usecase | UC-39 |
| :---- | :---- |
| **Tên usecase** | Chỉnh sửa lớp |
| **Mô tả** | Quản trị viên có thể chỉnh sửa lớp trong toàn hệ thống;  Giáo vụ có thể chỉnh sửa lớp trong phạm vi Khoa/Bộ môn được phân công.  |
| **Tác nhân** | Quản trị viên, Giáo vụ. |
| **Tiền điều kiện** | Người dùng đã đăng nhập với vai trò Quản trị viên (quyền toàn hệ thống) hoặc Giáo vụ (quyền trong phạm vi Khoa/Bộ môn được phân công).  Lớp cần chỉnh sửa đã tồn tại và đang ở trạng thái Hoạt động.  |
| **Hậu điều kiện** | Thông tin lớp được cập nhật thành công.  Thông tin mới được lưu vào cơ sở dữ liệu.  Các thành viên của lớp tiếp tục được quản lý theo thông tin đã cập nhật.  |
| **Luồng tương tác chính** | Người dùng chọn chức năng "Quản lý lớp".  Hệ thống hiển thị danh sách các lớp mà Người dùng có quyền quản lý:  Quản trị viên thấy toàn bộ lớp trong trường;  Giáo vụ chỉ thấy lớp thuộc Khoa/Bộ môn mình phụ trách.  Người dùng chọn lớp cần chỉnh sửa.  Hệ thống hiển thị thông tin hiện tại của lớp.  Người dùng chỉnh sửa thông tin lớp.  Người dùng chọn "Lưu thay đổi".  Hệ thống kiểm tra tính hợp lệ của thông tin mới.  Hệ thống cập nhật thông tin lớp vào cơ sở dữ liệu.  Hệ thống thông báo "Chỉnh sửa lớp thành công."  |
| **Luồng tương tác thay thế** | 5a. Người dùng chọn "Hủy": Hệ thống hủy thao tác chỉnh sửa và giữ nguyên thông tin lớp.  5b. Người dùng thay đổi tên lớp:  Người dùng nhập tên lớp mới.  Hệ thống kiểm tra tên lớp.  Hệ thống cập nhật tên lớp mới.  5c. Người dùng thay đổi Giáo viên phụ trách:  Người dùng chọn Giáo viên mới.  Hệ thống cập nhật Giáo viên phụ trách lớp.  5d. Người dùng thay đổi thông tin khác của lớp:  Người dùng chỉnh sửa thông tin cần thay đổi.  Hệ thống cập nhật thông tin lớp theo dữ liệu mới.  |
| **Luồng tương tác ngoại lệ** | E1 \- Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp." E2 \- Thông tin lớp không hợp lệ: Hệ thống thông báo "Thông tin lớp không hợp lệ." E3 \- Tên lớp đã tồn tại: Hệ thống thông báo "Tên lớp đã tồn tại." E4 \- Giáo viên không tồn tại: Hệ thống thông báo "Không tìm thấy Giáo viên được chọn." E5 \- Lỗi khi cập nhật thông tin: Hệ thống thông báo "Chỉnh sửa lớp thất bại." E6 \- Giáo vụ thao tác ngoài phạm vi phụ trách:  Hệ thống thông báo "Bạn không có quyền chỉnh sửa lớp thuộc Khoa/Bộ môn khác."  |

| Mã usecase | UC-40 |
| :---- | :---- |
| **Tên usecase** | Đóng/ Mở lại lớp học  |
| **Mô tả** | Đây là chức năng quản lý trạng thái hoạt động của lớp học.  Giáo viên thực hiện đóng hoặc mở lại các lớp thuộc phạm vi quản lý;  Quản trị viên có quyền đóng hoặc mở lại bất kỳ lớp nào trong toàn hệ thống nhằm quản lý hoạt động đào tạo.  |
| **Tác nhân** | Giáo viên, Quản trị viên, Giáo vụ. |
| **Tiền điều kiện** | Người dùng đã đăng nhập vào hệ thống.  Người dùng có quyền đóng hoặc mở lại lớp học.  Lớp học tồn tại trong hệ thống.  |
| **Hậu điều kiện** | Lớp được chuyển sang trạng thái "Đã đóng" khi thực hiện thao tác Đóng lớp. Lớp được chuyển sang trạng thái "Hoạt động" khi thực hiện thao tác Mở lại lớp. Khi lớp ở trạng thái "Đã đóng", các hoạt động học tập và tương tác của Sinh viên được ngăn chặn; dữ liệu lớp vẫn được bảo toàn.  |
| **Luồng tương tác chính** | Người dùng chọn chức năng "Quản lý lớp". Hệ thống hiển thị danh sách các lớp mà Người dùng có quyền quản lý. Người dùng chọn lớp cần thay đổi trạng thái. Hệ thống hiển thị thông tin và trạng thái hiện tại của lớp. Người dùng chọn "Đóng lớp" hoặc "Mở lại lớp" tùy theo trạng thái hiện tại. Hệ thống hiển thị yêu cầu xác nhận thao tác. Người dùng xác nhận thao tác. Hệ thống kiểm tra trạng thái hiện tại và quyền của Người dùng. Hệ thống cập nhật trạng thái lớp theo thao tác đã chọn. Hệ thống thông báo "Cập nhật trạng thái lớp thành công." |
| **Luồng tương tác thay thế** | 7a. Người dùng chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên trạng thái hiện tại của lớp. |
| **Luồng tương tác ngoại lệ** | E1 \- Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp học." E2 \- Lớp không ở trạng thái phù hợp để thực hiện thao tác này: Hệ thống thông báo "Lớp không ở trạng thái phù hợp để thực hiện thao tác này." E3 \- Không thể cập nhật trạng thái lớp: Hệ thống thông báo "Không thể cập nhật trạng thái lớp, vui lòng thử lại sau." |

| Mã usecase | UC-41 |
| :---- | :---- |
| **Tên usecase** | Quản lý Lưu trữ & Xóa lớp học |
| **Mô tả** | Đây là chức năng quản lý vòng đời dữ liệu lớp học.  Quản trị viên thực hiện trong toàn hệ thống;  Giáo vụ thực hiện trong phạm vi Khoa/Bộ môn được phân công.  Người dùng lưu trữ, xóa hoặc khôi phục lớp học nhằm quản lý dữ liệu đào tạo sau khi lớp kết thúc hoặc khi cần xử lý các lớp được tạo nhầm.  |
| **Tác nhân** | Quản trị viên, Giáo vụ. |
| **Tiền điều kiện** | Người dùng đã đăng nhập với vai trò Quản trị viên (quyền toàn hệ thống) hoặc Giáo vụ (quyền trong phạm vi Khoa/Bộ môn được phân công).  Lớp cần xử lý đã tồn tại trong hệ thống.  |
| **Hậu điều kiện** | Lớp được chuyển sang trạng thái "Lưu trữ" khi thực hiện thao tác Lưu trữ.  Chỉ cho phép Hard Delete khi lớp có 0 sinh viên, 0 bài tập được giao.   Lớp ở trạng thái "Lưu trữ" không xuất hiện trong danh sách lớp vận hành thông thường nhưng dữ liệu liên quan vẫn được bảo lưu để phục vụ tra cứu.  Lớp được khôi phục từ "Lưu trữ" về trạng thái "Đã đóng".  Việc khôi phục lớp không tự động chuyển lớp sang trạng thái "Hoạt động".  |
| **Luồng tương tác chính** | Người dùng chọn chức năng "Quản lý lớp".  Hệ thống hiển thị danh sách các lớp mà Người dùng có quyền quản lý và trạng thái tương ứng:  Quản trị viên thấy toàn bộ lớp trong trường;  Giáo vụ chỉ thấy lớp thuộc Khoa/Bộ môn mình phụ trách.  Người dùng chọn lớp cần quản lý vòng đời.  Hệ thống hiển thị thông tin và trạng thái hiện tại của lớp.  Người dùng chọn thao tác "Lưu trữ lớp", "Xóa lớp" hoặc "Khôi phục lớp".  Hệ thống kiểm tra trạng thái lớp và điều kiện thực hiện thao tác.  Hệ thống hiển thị yêu cầu xác nhận thao tác.  Người dùng xác nhận thao tác.  Hệ thống thực hiện thao tác theo chính sách quản lý vòng đời lớp.  Hệ thống thông báo "Thao tác thành công."  |
| **Luồng tương tác thay thế** | 6a. Người dùng chọn "Lưu trữ lớp":  Hệ thống kiểm tra dữ liệu liên quan của lớp.  Hệ thống chuyển lớp sang trạng thái "Lưu trữ".  Hệ thống ẩn lớp khỏi danh sách lớp học vận hành thông thường.  6b. Người dùng chọn "Xóa lớp":  Hệ thống kiểm tra lớp có sinh viên, bài tập được giao hoặc lịch học hay không.  Nếu không có cả 3 (Hard Delete), hệ thống xóa lớp hoàn toàn.  Nếu có ít nhất 1 trong 3, hệ thống không xóa mà chuyển lớp sang trạng thái “Lưu trữ”.  6c. Người dùng chọn "Khôi phục lớp":  Hệ thống kiểm tra lớp đang ở trạng thái "Lưu trữ".  Hệ thống khôi phục lớp về trạng thái "Đã đóng".  Dữ liệu liên quan của lớp được giữ nguyên.  9a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác và giữ nguyên trạng thái hiện tại của lớp.  |
| **Luồng tương tác ngoại lệ** | E1 \- Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp học." E2 \- Lớp không ở trạng thái phù hợp để thực hiện thao tác này: Hệ thống thông báo "Lớp không ở trạng thái phù hợp để thực hiện thao tác này." E3 \- Không thể lưu trữ hoặc khôi phục lớp: Hệ thống thông báo "Không thể cập nhật trạng thái lớp, vui lòng thử lại sau." E4 \- Không thể xóa lớp: Hệ thống thông báo "Không thể xóa lớp, vui lòng thử lại sau." E5 \- Giáo vụ thao tác ngoài phạm vi phụ trách:  Hệ thống thông báo "Bạn không có quyền thao tác trên lớp thuộc Khoa/Bộ môn khác."  |

| Mã usecase | UC-42 |
| :---- | :---- |
| **Tên usecase** | Quản lý sinh viên trong lớp |
| **Mô tả** | Đây là chức năng quản lý sinh viên trong lớp.  Quản trị viên áp dụng cho toàn hệ thống;  Giáo vụ áp dụng cho các lớp thuộc Khoa/Bộ môn được phân công.  Người dùng quản lý danh sách sinh viên thuộc một lớp, bao gồm thêm, xóa và xem thông tin sinh viên trong lớp.  |
| **Tác nhân** | Quản trị viên, Giáo vụ. |
| **Tiền điều kiện** | Người dùng đã đăng nhập với vai trò Quản trị viên (quyền toàn hệ thống) hoặc Giáo vụ (quyền trong phạm vi Khoa/Bộ môn được phân công).  Lớp cần quản lý đã tồn tại và đang ở trạng thái Hoạt động.  |
| **Hậu điều kiện** | Danh sách sinh viên trong lớp được cập nhật thành công.  Thông tin phân lớp của sinh viên được lưu vào cơ sở dữ liệu.  Danh sách sinh viên trong lớp phản ánh đúng các thay đổi đã thực hiện.  |
| **Luồng tương tác chính** | Người dùng chọn chức năng "Quản lý lớp".  Hệ thống hiển thị danh sách các lớp mà Người dùng có quyền quản lý:  Quản trị viên thấy toàn bộ lớp trong trường;  Giáo vụ chỉ thấy lớp thuộc Khoa/Bộ môn mình phụ trách.  Người dùng chọn lớp cần quản lý sinh viên.  Hệ thống hiển thị danh sách sinh viên hiện tại của lớp.  Người dùng chọn thao tác quản lý sinh viên.  Hệ thống hiển thị các chức năng thêm, xóa và xem thông tin sinh viên.  Người dùng thực hiện thao tác cần thiết.  Hệ thống kiểm tra tính hợp lệ của thao tác.  Hệ thống cập nhật danh sách sinh viên trong lớp.  Hệ thống thông báo "Cập nhật danh sách sinh viên thành công."  |
| **Luồng tương tác thay thế** | 5a. Người dùng chọn "Thêm sinh viên":  Hệ thống hiển thị danh sách sinh viên chưa thuộc lớp.  Người dùng chọn sinh viên cần thêm.  Người dùng xác nhận thêm sinh viên vào lớp.  Hệ thống cập nhật danh sách sinh viên của lớp.  5b. Người dùng chọn "Xóa sinh viên":  Người dùng chọn sinh viên cần xóa khỏi lớp.  Hệ thống yêu cầu xác nhận thao tác.  Người dùng xác nhận xóa sinh viên khỏi lớp.  Hệ thống cập nhật danh sách sinh viên của lớp.  5c. Người dùng chọn "Xem thông tin sinh viên":  Hệ thống hiển thị thông tin của sinh viên được chọn.  5d. Người dùng chọn nhiều sinh viên:  Hệ thống cho phép Người dùng chọn nhiều sinh viên để thêm hoặc xóa khỏi lớp.  Người dùng xác nhận thao tác.  Hệ thống cập nhật danh sách sinh viên theo lựa chọn. |
| **Luồng tương tác ngoại lệ** | E1 \- Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp." E2 \- Sinh viên không tồn tại: Hệ thống thông báo "Không tìm thấy sinh viên." E3 \- Sinh viên đã thuộc lớp: Hệ thống thông báo "Sinh viên đã thuộc lớp này." E4 \- Sinh viên chưa thuộc lớp: Hệ thống thông báo "Sinh viên không thuộc lớp này." E5 \- Không thể thêm hoặc xóa sinh viên: Hệ thống thông báo "Không thể cập nhật sinh viên trong lớp." E6 \- Lỗi khi lưu dữ liệu: Hệ thống thông báo "Cập nhật danh sách sinh viên thất bại." E7 \- Giáo vụ thao tác ngoài phạm vi phụ trách:  Hệ thống thông báo "Bạn không có quyền quản lý sinh viên của lớp thuộc Khoa/Bộ môn khác."  |

| Mã usecase | UC-43 |
| :---- | :---- |
| **Tên usecase** | Phân công Giáo viên vào lớp |
| **Mô tả** | Người dùng (Quản trị viên trong toàn hệ thống, hoặc Giáo vụ trong phạm vi Khoa/Bộ môn được phân công) phân công một hoặc nhiều Giáo viên phụ trách giảng dạy cho lớp học.  |
| **Tác nhân** | Quản trị viên, Giáo vụ. |
| **Tiền điều kiện** | Người dùng đã đăng nhập với vai trò Quản trị viên (quyền toàn hệ thống) hoặc Giáo vụ (quyền trong phạm vi Khoa/Bộ môn được phân công).  Lớp cần phân công đã tồn tại và đang ở trạng thái Hoạt động.  Giáo viên cần phân công đã tồn tại trong hệ thống.  |
| **Hậu điều kiện** | Giáo viên được phân công thành công vào lớp.  Thông tin phân công được lưu vào cơ sở dữ liệu.  Giáo viên có thể quản lý và giảng dạy lớp theo quyền được cấp.  |
| **Luồng tương tác chính** | Người dùng chọn chức năng "Quản lý lớp".  Hệ thống hiển thị danh sách các lớp mà Người dùng có quyền quản lý:  Quản trị viên thấy toàn bộ lớp trong trường;  Giáo vụ chỉ thấy lớp thuộc Khoa/Bộ môn mình phụ trách.  Người dùng chọn lớp cần phân công Giáo viên.  Hệ thống hiển thị thông tin và danh sách Giáo viên đang phụ trách lớp.  Người dùng chọn chức năng "Phân công Giáo viên".  Hệ thống hiển thị danh sách Giáo viên có thể phân công.  Người dùng chọn Giáo viên cần phân công.  Người dùng xác nhận phân công.  Hệ thống kiểm tra tính hợp lệ của thông tin phân công.  Hệ thống lưu thông tin phân công vào cơ sở dữ liệu.  Hệ thống thông báo "Phân công Giáo viên thành công."  |
| **Luồng tương tác thay thế** | 5a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác phân công và giữ nguyên danh sách Giáo viên của lớp.  5b. Người dùng phân công nhiều Giáo viên:  Hệ thống cho phép Người dùng chọn nhiều Giáo viên.  Người dùng xác nhận phân công.  Hệ thống phân công các Giáo viên được chọn vào lớp.  5c. Người dùng thay đổi Giáo viên phụ trách:  Hệ thống hiển thị Giáo viên đang phụ trách lớp.  Người dùng chọn Giáo viên mới.  Người dùng xác nhận thay đổi.  Hệ thống cập nhật thông tin phân công.  5d. Người dùng hủy phân công Giáo viên:  Người dùng chọn Giáo viên cần hủy phân công.  Hệ thống yêu cầu xác nhận thao tác.  Người dùng xác nhận hủy phân công.  Hệ thống xóa thông tin phân công khỏi lớp.  |
| **Luồng tương tác ngoại lệ** | E1 \- Lớp không tồn tại: Hệ thống thông báo "Không tìm thấy lớp." E2 \- Giáo viên không tồn tại: Hệ thống thông báo "Không tìm thấy Giáo viên." E3 \- Giáo viên đã được phân công: Hệ thống thông báo "Giáo viên đã được phân công vào lớp này." E4 \- Lỗi khi lưu thông tin phân công: Hệ thống thông báo "Phân công Giáo viên thất bại." E5 \- Giáo vụ thao tác ngoài phạm vi phụ trách:  Hệ thống thông báo "Bạn không có quyền phân công Giáo viên cho lớp thuộc Khoa/Bộ môn khác."  |

| Mã usecase | UC-44 |
| :---- | :---- |
| **Tên usecase** | Quản lý cấu hình AI |
| **Mô tả** | Quản trị viên hệ thống quản lý các cấu hình AI được sử dụng trong hệ thống, bao gồm thiết lập, cập nhật và kích hoạt hoặc vô hiệu hóa cấu hình. |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập, có quyền quản lý cấu hình AI. Các thành phần AI cần cấu hình đã được tích hợp vào hệ thống. |
| **Hậu điều kiện** | Cấu hình AI được tạo hoặc cập nhật thành công. Thông tin cấu hình được lưu vào hệ thống. Hệ thống sử dụng cấu hình đang được kích hoạt cho các chức năng AI tương ứng. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng "Quản lý cấu hình AI". Hệ thống hiển thị danh sách các cấu hình AI hiện có. Quản trị viên hệ thống chọn cấu hình cần thiết lập hoặc chỉnh sửa. Hệ thống hiển thị thông tin cấu hình hiện tại. Quản trị viên hệ thống nhập hoặc chỉnh sửa các thông số cấu hình AI. Quản trị viên hệ thống chọn "Lưu cấu hình". Hệ thống kiểm tra tính hợp lệ của các thông số. Hệ thống lưu cấu hình vào cơ sở dữ liệu. Hệ thống thông báo "Cập nhật cấu hình AI thành công." |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên cấu hình hiện tại. 4b. Quản trị viên hệ thống tạo cấu hình AI mới: Hệ thống hiển thị biểu mẫu tạo cấu hình. Quản trị viên hệ thống nhập các thông số cấu hình. Quản trị viên hệ thống xác nhận tạo cấu hình. Hệ thống lưu cấu hình AI mới. 4c. Quản trị viên hệ thống kích hoạt cấu hình: Quản trị viên hệ thống chọn cấu hình cần kích hoạt. Hệ thống yêu cầu xác nhận. Quản trị viên hệ thống xác nhận kích hoạt. Hệ thống chuyển cấu hình sang trạng thái hoạt động. 4d. Quản trị viên hệ thống vô hiệu hóa cấu hình: Quản trị viên hệ thống chọn cấu hình cần vô hiệu hóa. Hệ thống yêu cầu xác nhận. Quản trị viên hệ thống xác nhận vô hiệu hóa. Hệ thống chuyển cấu hình sang trạng thái không hoạt động. 4e. Quản trị viên hệ thống kiểm tra cấu hình: Quản trị viên hệ thống chọn chức năng kiểm tra cấu hình. Hệ thống thực hiện kiểm tra kết nối và tính hợp lệ của cấu hình. Hệ thống hiển thị kết quả kiểm tra. |
| **Luồng tương tác ngoại lệ** | E1 \- Cấu hình không hợp lệ: Hệ thống thông báo "Thông tin cấu hình AI không hợp lệ." E2 \- Thiếu thông số bắt buộc: Hệ thống thông báo "Vui lòng nhập đầy đủ các thông số bắt buộc." E3 \- Cấu hình đã tồn tại: Hệ thống thông báo "Cấu hình AI đã tồn tại." E4 \- Kết nối dịch vụ AI thất bại: Hệ thống thông báo "Không thể kết nối đến dịch vụ AI." E5 \- Không thể kích hoạt cấu hình: Hệ thống thông báo "Không thể kích hoạt cấu hình AI." E6 \- Lỗi khi lưu cấu hình: Hệ thống thông báo "Cập nhật cấu hình AI thất bại." |

| Mã usecase | UC-45 |
| :---- | :---- |
| **Tên usecase** | Cấu hình Docker Sandbox |
| **Mô tả** | Quản trị viên hệ thống cấu hình môi trường Docker Sandbox để thực thi và kiểm tra mã nguồn của sinh viên một cách an toàn. |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền quản lý cấu hình Docker Sandbox. Dịch vụ Docker Sandbox đã được tích hợp vào hệ thống. |
| **Hậu điều kiện** | Cấu hình Docker Sandbox được lưu thành công. Docker Sandbox sử dụng cấu hình mới cho quá trình thực thi mã nguồn. Các thông số cấu hình được áp dụng cho các phiên thực thi mới. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng "Cấu hình Docker Sandbox". Hệ thống hiển thị các thông số cấu hình hiện tại. Quản trị viên hệ thống nhập hoặc chỉnh sửa các thông số cấu hình. Quản trị viên hệ thống chọn "Lưu cấu hình". Hệ thống kiểm tra tính hợp lệ của các thông số. Hệ thống lưu cấu hình vào cơ sở dữ liệu. Hệ thống áp dụng cấu hình cho Docker Sandbox. Hệ thống thông báo "Cấu hình Docker Sandbox thành công." |
| **Luồng tương tác thay thế** | 3a. Quản trị viên hệ thống chọn "Hủy": Hệ thống hủy thao tác và giữ nguyên cấu hình hiện tại. 3b. Quản trị viên hệ thống khôi phục cấu hình mặc định: Quản trị viên hệ thống chọn "Khôi phục mặc định". Hệ thống hiển thị các thông số cấu hình mặc định. Quản trị viên hệ thống xác nhận khôi phục. Hệ thống cập nhật cấu hình Docker Sandbox về giá trị mặc định. 3c. Quản trị viên hệ thống kiểm tra cấu hình: Quản trị viên hệ thống chọn chức năng "Kiểm tra cấu hình". Hệ thống kiểm tra kết nối và khả năng khởi tạo Docker Sandbox. Hệ thống hiển thị kết quả kiểm tra. 3d. Quản trị viên hệ thống cập nhật giới hạn thực thi: Quản trị viên hệ thống điều chỉnh thời gian chạy, bộ nhớ và tài nguyên được cấp cho Docker Sandbox. Hệ thống kiểm tra và lưu các giới hạn mới. |
| **Luồng tương tác ngoại lệ** | E1 \- Thông số cấu hình không hợp lệ: Hệ thống thông báo "Thông số cấu hình Docker Sandbox không hợp lệ." E2 \- Thiếu thông số bắt buộc: Hệ thống thông báo "Vui lòng nhập đầy đủ các thông số bắt buộc." E3 \- Docker Sandbox không khả dụng: Hệ thống thông báo "Docker Sandbox hiện không khả dụng." E4 \- Không thể kết nối Docker: Hệ thống thông báo "Không thể kết nối đến Docker." E5 \- Cấu hình vượt quá giới hạn cho phép: Hệ thống thông báo "Thông số cấu hình vượt quá giới hạn cho phép." E6 \- Lỗi khi lưu cấu hình: Hệ thống thông báo "Cấu hình Docker Sandbox thất bại." |

| Mã usecase | UC-46 |
| :---- | :---- |
| **Tên usecase** | Giám sát Docker Sandbox |
| **Mô tả** | Quản trị viên hệ thống giám sát trạng thái và hoạt động của Docker Sandbox để theo dõi tình trạng thực thi mã nguồn và phát hiện các vấn đề trong quá trình vận hành. |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền giám sát Docker Sandbox. Dịch vụ Docker Sandbox đã được tích hợp vào hệ thống. |
| **Hậu điều kiện** | Quản trị viên hệ thống xem được trạng thái và thông tin hoạt động của Docker Sandbox. Hệ thống ghi nhận các sự kiện và lỗi phát sinh trong quá trình thực thi. Không có dữ liệu cấu hình bị thay đổi. Nếu Quản trị viên hệ thống dừng một phiên thực thi, phiên đó được kết thúc; hệ thống lưu trạng thái và kết quả đã thực hiện đến thời điểm dừng, đồng thời cập nhật bài nộp liên quan sang trạng thái “Bị gián đoạn”. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng "Giám sát Docker Sandbox". Hệ thống kiểm tra trạng thái của Docker Sandbox. Hệ thống hiển thị trạng thái hoạt động của Docker Sandbox. Hệ thống hiển thị thông tin các phiên thực thi đang hoạt động và đã hoàn thành. Quản trị viên hệ thống xem mức sử dụng tài nguyên của Docker Sandbox. Quản trị viên hệ thống xem các lỗi hoặc sự kiện phát sinh trong quá trình thực thi. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống chọn một phiên thực thi: Hệ thống hiển thị thông tin chi tiết của phiên thực thi. Hệ thống hiển thị thời gian thực thi, trạng thái và kết quả của phiên. 4b. Quản trị viên hệ thống xem nhật ký hoạt động: Hệ thống hiển thị nhật ký hoạt động của Docker Sandbox. Quản trị viên hệ thống xem các sự kiện và lỗi phát sinh. 4c. Quản trị viên hệ thống làm mới thông tin giám sát: Hệ thống cập nhật trạng thái và thông tin tài nguyên mới nhất. 4d. Quản trị viên hệ thống dừng phiên thực thi: Quản trị viên hệ thống chọn phiên thực thi cần dừng. Hệ thống yêu cầu xác nhận thao tác. Quản trị viên hệ thống xác nhận dừng phiên. Hệ thống dừng phiên thực thi được chọn, ghi nhận thao tác vào System Logs và cập nhật trạng thái bài nộp liên quan.  |
| **Luồng tương tác ngoại lệ** | E1 \- Docker Sandbox không khả dụng: Hệ thống thông báo "Docker Sandbox hiện không khả dụng." E2 \- Không thể lấy trạng thái Docker Sandbox: Hệ thống thông báo "Không thể lấy trạng thái Docker Sandbox." E3 \- Không thể lấy thông tin tài nguyên: Hệ thống thông báo "Không thể lấy thông tin tài nguyên." E4 \- Không tìm thấy phiên thực thi: Hệ thống thông báo "Không tìm thấy phiên thực thi." E5 \- Không thể dừng phiên thực thi: Hệ thống thông báo "Không thể dừng phiên thực thi." E6 \- Lỗi khi tải nhật ký: Hệ thống thông báo "Không thể tải nhật ký hoạt động." E7 \- Khi phiên chấm bị gián đoạn: Hệ thống không tự động chấm lại, không tăng submission\_count\- Hệ thống thông báo cho Sinh viên thực hiện nộp lại bài.  |

| Mã usecase | UC-47 |
| :---- | :---- |
| **Tên usecase** | Quản lý tổ chức |
| **Mô tả** | Quản trị viên hệ thống hoặc Quản trị viên quản lý thông tin tổ chức và cơ cấu Khoa/Bộ môn trực thuộc, đồng thời gán tài khoản Giáo vụ phụ trách từng Khoa/Bộ môn.  |
| **Tác nhân** | Quản trị viên hệ thống, Quản trị viên.  |
| **Tiền điều kiện** | Người dùng đã đăng nhập hệ thống.  Người dùng có quyền quản lý tổ chức và Khoa/Bộ môn.  |
| **Hậu điều kiện** | Thông tin tổ chức hoặc Khoa/Bộ môn được tạo, cập nhật hoặc thay đổi trạng thái thành công.  Tài khoản Giáo vụ được gán đúng Khoa/Bộ môn phụ trách.  Thông tin được lưu vào cơ sở dữ liệu.  |
| **Luồng tương tác chính** | Người dùng chọn chức năng "Quản lý tổ chức".  Hệ thống hiển thị danh sách tổ chức và cơ cấu Khoa/Bộ môn trực thuộc.  Người dùng chọn một thao tác: Tạo tổ chức, Tạo Khoa/Bộ môn, Chỉnh sửa, Khóa/mở khóa, Xóa, hoặc Phân công Giáo vụ.  Hệ thống hiển thị biểu mẫu hoặc yêu cầu xác nhận tương ứng.  Người dùng nhập thông tin hoặc xác nhận thao tác.  Hệ thống kiểm tra tính hợp lệ của dữ liệu.  Hệ thống cập nhật thông tin hoặc trạng thái tương ứng.  Hệ thống thông báo thao tác thành công.  |
| **Luồng tương tác thay thế** | 3a. Người dùng chọn "Tạo tổ chức":  Hệ thống hiển thị biểu mẫu tạo tổ chức mới.  3b. Người dùng chọn "Tạo Khoa/Bộ môn":  Người dùng chọn tổ chức trực thuộc và nhập tên Khoa/Bộ môn.  Hệ thống tạo Khoa/Bộ môn mới.  3c. Người dùng chọn "Chỉnh sửa":  Hệ thống hiển thị thông tin hiện tại của tổ chức hoặc Khoa/Bộ môn được chọn để cập nhật.  3d. Người dùng chọn "Khóa/mở khóa tổ chức":  Hệ thống cập nhật trạng thái tổ chức.  3e. Người dùng chọn "Xóa":  Hệ thống kiểm tra dữ liệu liên quan trước khi xóa tổ chức hoặc Khoa/Bộ môn.  3f. Người dùng chọn "Phân công Giáo vụ":  Người dùng chọn tài khoản Giáo vụ và Khoa/Bộ môn cần phụ trách.  Người dùng xác nhận.  Hệ thống lưu thông tin phân công (một Giáo vụ có thể phụ trách một hoặc nhiều Khoa/Bộ môn).  7a. Người dùng chọn "Hủy":  Hệ thống hủy thao tác và giữ nguyên dữ liệu hiện tại.  |
| **Luồng tương tác ngoại lệ** | E1 \- Tổ chức hoặc Khoa/Bộ môn không tồn tại:  Hệ thống thông báo "Không tìm thấy tổ chức hoặc Khoa/Bộ môn." E2 \- Thông tin không hợp lệ:  Hệ thống thông báo "Thông tin không hợp lệ."  E3 \- Tổ chức hoặc Khoa/Bộ môn đã tồn tại:  Hệ thống thông báo "Tên đã tồn tại."  E4 \- Đang có dữ liệu liên quan:  Hệ thống thông báo "Đang có dữ liệu liên quan và không thể xóa."  E5 \- Giáo vụ đã được phân công Khoa/Bộ môn này:  Hệ thống thông báo "Giáo vụ đã phụ trách Khoa/Bộ môn này."  E6 \\- Lỗi khi lưu dữ liệu:  Hệ thống thông báo "Thao tác thất bại."  |

| Mã usecase | UC-48 |
| :---- | :---- |
| **Tên usecase** | Quản lý System Logs |
| **Mô tả** | Quản trị viên hệ thống xem, tìm kiếm và theo dõi các System Logs được ghi nhận trong quá trình hoạt động của hệ thống nhằm hỗ trợ giám sát và kiểm tra sự cố. |
| **Tác nhân** | Quản trị viên hệ thống |
| **Tiền điều kiện** | Quản trị viên hệ thống đã đăng nhập hệ thống. Quản trị viên hệ thống có quyền quản lý System Logs. Hệ thống đã ghi nhận System Logs. |
| **Hậu điều kiện** | Quản trị viên hệ thống xem được các System Logs theo nhu cầu. Thông tin nhật ký không bị thay đổi trong quá trình xem và tra cứu. Các thao tác quản lý System Logs được ghi nhận nếu hệ thống có hỗ trợ. |
| **Luồng tương tác chính** | Quản trị viên hệ thống chọn chức năng "Quản lý System Logs". Hệ thống hiển thị danh sách System Logs. Quản trị viên hệ thống xem thông tin nhật ký gồm thời gian, người dùng, hành động, loại sự kiện và trạng thái. Quản trị viên hệ thống chọn điều kiện tìm kiếm hoặc lọc System Logs. Hệ thống xử lý điều kiện tìm kiếm hoặc lọc. Hệ thống hiển thị các System Logs phù hợp. Quản trị viên hệ thống chọn một System Log để xem chi tiết. Hệ thống hiển thị thông tin chi tiết của System Log được chọn. |
| **Luồng tương tác thay thế** | 4a. Quản trị viên hệ thống tìm kiếm System Logs: Quản trị viên hệ thống nhập từ khóa tìm kiếm. Hệ thống hiển thị các System Logs phù hợp. 4b. Quản trị viên hệ thống lọc System Logs: Quản trị viên hệ thống chọn khoảng thời gian, loại sự kiện hoặc trạng thái. Hệ thống hiển thị các System Logs theo điều kiện đã chọn. 4c. Quản trị viên hệ thống xem chi tiết System Log: Quản trị viên hệ thống chọn một System Log. Hệ thống hiển thị toàn bộ thông tin chi tiết của System Log. 4d. Quản trị viên hệ thống xuất System Logs: Quản trị viên hệ thống chọn khoảng dữ liệu cần xuất. Hệ thống tạo tệp chứa các System Logs được chọn. Hệ thống cung cấp tệp cho quản trị viên hệ thống. |
| **Luồng tương tác ngoại lệ** | E1 \- Không tìm thấy System Logs: Hệ thống thông báo "Không tìm thấy System Logs phù hợp." E2 \- Điều kiện tìm kiếm không hợp lệ: Hệ thống thông báo "Điều kiện tìm kiếm không hợp lệ." E3 \- System Log không tồn tại: Hệ thống thông báo "Không tìm thấy System Log." E4 \- Không thể tải System Logs: Hệ thống thông báo "Không thể tải System Logs." E5 \- Lỗi khi xuất System Logs: Hệ thống thông báo "Không thể xuất System Logs." |


# VI_PY_001: Cài đặt môi trường Python, PyCharm và cấu hình Interpreter

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Cài đặt | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

1
Giới thiệu
Python là một ngôn ngữlập trình cấp cao và dễtiếp cận hơn đối với những người
mới bắt đầu học ngôn ngữlập trình. Nếu so sánh Python với các ngôn ngữtruyền
thống như Pascal hay C thì mức độphức tạp của Python là thấp hơn. Một sốưu
điểm của ngôn ngữlập trình Python có thểkểra như sau:
• Python có cú pháp rất đơn giản. Nó dễđọc và viết hơn rất nhiều khi so sánh
với những ngôn ngữlập trình khác như Pascal hay C. Mặc dù đôi lúc sựđơn
giản này có thểgây ra một sốphiền phức trong việc quản lý chương trình.
Tuy nhiên Python làm cho việc lập trình trởđơn giản hơn, đặc biệt là các
tác vụnhập xuất (input và output), cho phép bạn tập trung vào những giải
pháp chứkhông phải cú pháp của ngôn ngữlập trình. Một cách so sánh trừu
tượng, Python tạo điều kiện cho bạn "giao tiếp ngôn ngữ", hơn là việc phải
"học ngôn ngữ" một cách truyền thống.
• Mã nguồn mởrộng rãi: Đây là yếu tốhết sức quan trọng dành cho người mới
bắt đầu. Vì là mã nguồn mở, bạn không những có thểsửdụng các phần mềm,
chương trình được viết trong Python mà còn có thểthay đổi mã nguồn của
nó. Python có một cộng đồng rộng lớn, không ngừng cải thiện nó mỗi lần cập
nhật. Rất nhiều mã nguồn mởliên quan đến trí tuệnhân tạo hay nhận diện
giọng nói đang có sẵn trên Python, đểngười dùng có thểphát triển những
ứng dụng rất cao cấp.
• Tương thích đa nền tảng: Rất nhiều hệthống, từmáy tính cho đến các bo
mạch nhúng, thậm chí là các bo mạch có tài nguyên thấp như MicroBit, cũng
hỗtrợngôn ngữlập trình Python. Do đó, bạn có thểhình dung rằng, phần
mềm có thểchỉcần phát triển một lần là có thểsửdụng cho rất nhiều nền
tảng khác nhau. Chỉvới những thay đổi rất nhỏ, một phần mềm đang chạy
trên máy tính cũng có thểchạy trên một bo mạch mini.
Như vậy, có thểthấy rằng, ngôn ngữlập trình Python là một khái niệm rất rộng.
Tùy vào việc phát triển ứng dụng trên nền tảng nào, mà phần mềm đi kèm phù hợp
sẽđược sửdụng, như minh họa ởHình 1.1. Phần mềm ởđây không chỉđóng vai
trò là chương trình đểchúng ta soạn thảo chương trình (hay còn gọi là lập trình),
mà nó còn đóng vai trò biên dịch từngôn ngữlập trình sang ngôn ngữthực thi.
Như minh họa ởHình 1.1, khi lập trình Python trên máy tính, chúng ta sẽcần 1
chương trình dịch từngôn ngữPython sang ngôn ngữmà máy tính có thểhiểu

được. Và chương trình này, thông dụng nhất hiện tại là Python3. Tuy nhiên, nếu
chúng ta muốn lập trình bằng ngôn ngữPython nhưng cho mạch MicroBit, chúng
ta sẽcần một chương trình khác, chẳng hạn như là Mu. Chương trình này sẽdịch
từngôn ngữPython sang ngôn ngữmà mạch MicroBit có thểhiểu được. Trong
hình Hình 1.1, chúng tôi gọi Máy tính hoặc mạch MicroBit là nền tảng thực thi.
Cuối cùng, là phương thức dịch từngôn ngữPython sang ngôn ngữmà nền tảng
thực thi có thểhiểu được, gọi là thông dịch (interpreter). Như một thông dịch viên,
phần mềm sẽdịch câu lệnh python đầu tiên, rồi thực thi nó. Sau đó, lại dịch tiếp
câu lệnh thứ2, và thực thi cho đến khi kết thúc chương trình. Đây là điểm vô cùng
khác biệt so với ngôn ngữPascal, trình biên dịch sẽdịch hết chương trình rồi mới

The Dariu Foundation

Hình 1.1: Ngôn ngữlập trình và Trình biên dịch
thực thi. Cũng vì lý do này, mà Python tương thích với nhiều nền tảng thực thi, vì
bản chất chương trình Python chỉlà một file văn bản. Chỉkhi thực thi, nó mới được
dịch sang ngôn ngữmà nền tảng phần cứng hiểu được.
Hướng dẫn bên dưới sẽhướng dẫn chi tiết các bước cài đặt trình thông dịch Python3.
Thực ra, sau khi cài đặt trình thông dịch này, chúng ta đã có một giao diện để
lập trình bằng ngôn ngữPython. Tuy nhiên, giao diện này khá nghèo nàn, nên
chúng tôi khuyến khích bạn cài thêm PyCharm, một phần mềm rất được cộng
đồng Python khuyên dùng.
2
Cài đặt Python trên Windows
• Bước 1: Bạn cần truy cập vào trang chủcủa Python là http://www.python.org/,
chọn tiếp vào mục Downloads, và lựa chọn phiên bản Python muốn cài. Tại
thời điểm của bài hướng dẫn này, Python bản mới nhất đang là 3.8.5
Hình 1.2: Tải phần mềm Python từtrang chủhttp://www.python.org/
• Bước 2: Khi tải xong, bạn tiến hành chạy file cài đặt có đuôi .exe vừa tải ở
bước 1. Nhấp vào Install Now đểcài đặt. Bạn cần phải chọn vào 2 tùy chọn
cuối cùng (Install for all user và Add Python to PATH), như minh họa ởhình
bên dưới.
• Bước 3: Bạn có thểnhìn thấy tiến trình cài đặt Python lên máy.
Hướng dẫn lập trình Python cơ bản

Hình 1.3: Chọn cả2 tùy chọn, trước khi nhấn vào Install Now đểcài đặt
Hình 1.4: Đợi chương trình cài đặt Python

The Dariu Foundation

• Bước 4: Khi cài đặt hoàn tất, bạn sẽnhìn thấy một màn hình thông báo như

dưới đây. Khi đó hãy click “Close” (ởgóc dưới bên phải) đểhoàn tất cài đặt.
Hình 1.5: Quá trình cài đặt Python thành công
3
Giao diện lập trình Python GUI
Ngay sau khi cài đặt xong Python, bạn đã có thểbắt đầu lập trình. Từnút khởi động
Windows, bạn tìm kiếm với từkhóa Python GUI là thấy ứng dụng này, như minh
họa ởHình 14.1.
Hình 1.6: Chương trình Python GUI
Giao diện Python Shell hiện ra, từmenu File, bạn chọn tiếp New Window, như
Hướng dẫn lập trình Python cơ bản

minh họa ởHình 14.3.
Hình 1.7: Mởmột cửa sổđểlập trình trên Python IDE
Chương trình đầu tiên rất đơn giản, chỉcó 1 câu lệnh là print("Xin chao"). Đểchạy
chương trình, bạn chọn vào Run, chọn tiếp Run mode hoặc nhấn F5. Kết quảcủa
chương trình sẽđược hiển thịtrên Python Shell. Rõ ràng, giao diện lập trình này
khá nghèo nàn và không có nhiều hỗtrợkhi viết câu lệnh, điều mà bạn sẽthấy rõ
ràng trên phần mềm PyCharm. Tuy nhiên phần mềm này cũng có thểdùng tạm
khi bạn chưa cài đặt PyCharm thành công. Trong phần hướng dẫn tiếp theo, chúng
tôi sẽhướng dẫn bạn cách cài đặt và viết chương trình trên PyCharm.
4
Cài đặt PyCharm trên Window
• Bước 1: Từtrang chủwww.jetbrains.com/pycharm/download/, nhấn vào nút
“Download”, và chọn phiên bản miễn phí Community, như hướng dẫn ở
hình bên dưới.
Hình 1.8: Tải Pycharm từtrang chủ
• Bước 2: Khi tải hoàn tất, tiến hành chạy đểcài đặt PyCharm. Một cửa sổcài
đặt sẽhiện ra, hãy nhấp vào “Next”.

The Dariu Foundation

Hình 1.9: Ấn "Next" đểtiếp tục
• Bước 3: Ởmàn hình tiếp theo, bạn có thểthay đổi đường dẫn đểcài đặt Py-
Charm hoặc đểmặc định. Sau đó nhấp vào “Next”.
Hình 1.10: Ấn "Next" đểtiếp tục
Hướng dẫn lập trình Python cơ bản

• Bước 4: Bạn sẽthấy một màn hình có một vài lựa chọn, bạn chọn vào các ô
như hình (chọn tương tựnếu như máy bạn chỉhiện 32-bit thay vì 64-bit). Sau
đó ấn vào “Next”.

Hình 1.11: Ấn "Next" đểtiếp tục
• Bên cạnh đó, nếu như trong bước này, trong khung cài đặt bạn có thêm lựa
chọn như hình bên dưới. Điều đó có nghĩa là bạn chưa cài thư viện Java, bạn
hãy chọn đểcài đặt thư viện Java tựđộng nhé.
Hình 1.12: Đánh dấu cho 2 lựa chọn

The Dariu Foundation

• Bước 5: Chọn thư mục trong start menu của Windows. Hãy đểmặc định là
thư mục JetBrains vào nhấp vào “Install”.
Hình 1.13: Nhấn vô "Install" đểtiến hành cài đặt
• Bước 6: Chờquá trình cài đặt hoàn tất.
Hình 1.14: Đợi chương trình cài đặt Pycharm
Hướng dẫn lập trình Python cơ bản

• Bước 7: Khi cài đặt hoàn thành, bạn sẽnhìn thấy màn hình thông báo như
dưới đây. PyCharm hỏi ta có muốn khởi động lại máy luôn hay không. Ta có
thểchọn RebootNow đểkhởi động lại máy tính nhằm hoàn tất quá trình cài
đặt.
Hình 1.15: Ấn "Finish" đểhoàn thành cài đặt
5
Hướng dẫn setup và chạy chương trình với PyCharm
Như vậy là vềcơ bản chúng ta đã cài đặt xong PyCharm. Nhưng đểbiết bạn đã cài
đúng chưa thì chúng ta cần phải thửxem chương trình python của bạn có chạy
được với PyCharm vừa cài không.
• Bước 1: Mởchương trình PyCharm vừa cài đặt thành công trên máy tính của
bạn.
• Bước 2: Ta sẽđược hỏi "Có muốn Import các thiết lập đã có từtrước hay
không?". Nếu cài mới hoàn toàn, ta chọn mục Do not import settings, rồi
nhấn OK, như hướng dẫn ởHình 1.16
Hình 1.16: Không import những setting cũ khi cài mới

The Dariu Foundation

Trong phần chính sách bảo mật (nếu có), ta nhấn xác nhận và nhấn Continue
đểtiếp tục.
Hình 1.17: Đồng ý với cách chính sách của PyCharm
• Bước 3: Trong màn hình tùy biến PyCharm, ta chọn Skip Remaining and Set
Defaults đểlựa chọn các thiết lập mặc định.
Hình 1.18: Chọn cấu hình mặc định cho phần mềm PyCharm
Hướng dẫn lập trình Python cơ bản

• Bước 4: Sau đó là màn hình chào hỏi của PyCharm, ta chọn mục Create New
Project đểtạo một Project mới.
Hình 1.19: Tạo mới một dựán bằng cách nhấn vào New Project
• Bước 5: Ta chọn thư mục đểlưu project tại mục Location. Đồng thời, bạn
kiểm tra các thông tin môi trường bên dưới, xem có giống với hình hướng
dẫn hay không. Thông thường các giá trịmặc định sẽchính xác và chúng ta
không phải chỉnh sửa gì cả. Cuối cùng, chúng ta nhấn vào nút Create.
Hình 1.20: Chọn đường dẫn cho dựán và kiểm tra thông tin môi trường

The Dariu Foundation
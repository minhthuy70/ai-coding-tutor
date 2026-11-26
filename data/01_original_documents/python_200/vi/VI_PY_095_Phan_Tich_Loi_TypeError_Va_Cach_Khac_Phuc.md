<!-- page: 1 -->
# VI_PY_095: Phân tích nguyên nhân và cách khắc phục lỗi kiểu dữ liệu TypeError

**Nguồn tài liệu chính thống**: Cẩm nang Chẩn đoán & Gỡ lỗi Python ĐH  
**Chuyên mục**: Gỡ lỗi | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 109 -->
CHƯƠNG 11
Trợlý ảo trên Python - Văn bản thành
Giọng nói

<!-- page: 110 -->
1
Giới thiệu
Trong bài hướng dẫn này, chúng tôi sẽđưa ra những bước cơ bản nhất đểlàm một
ứng dụng mô phỏng cho Trợlý ảo. Trong ứng dụng này sẽcó 3 phần chính: Nhận
dạng giọng nói từngười dùng, Trí tuệcủa máy tính, và cuối cùng là Trảlời lại cho
người dùng. Trong 3 phần này, chúng ta có thểxem Nhận dạng giọng nói là đầu
vào (Input), Trí tuệcủa máy tính là phần Xửlý, và cuối cùng, là đầu ra (Output).
Với một dựán, việc phân tích đâu là dữliệu đầu vào, dữliệu đầu ra là một bước
rất quan trọng, trước khi bắt đầu vào việc lập trình đểxửlý. Thông thường, khi so
sánh độphức tạp của dữliệu đầu và và đầu ra, thì đầu ra sẽđơn giản hơn, và nên
được hiện thực trước tiên.
Trong bài hướng dẫn này, một đoạn chương trình đơn giản sẽđược hiện thực để
máy tính trảlời kết quảlại cho chúng ta dưới dạng giọng nói. Kĩ thuật này gọi là
"Text To Speech". Tức là, bằng việc lập trình, chúng ta đưa cho máy tính một chuỗi
dữliệu, nó sẽnói ra thành lời thông qua loa của máy tính. Các bước hướng dẫn bên
dưới sẽtrình bày chi tiết cách hiện thực chức năng "Text To Speech", phần đầu ra
(Output) cho dựán Trợlý ảo.
2
Tạo mới một ứng dụng
Đối với các bài hướng dẫn trước, chúng ta đã quen thuộc với việc thêm mới 1 file
python vào chương trình và chạy được nó. Tuy nhiên, khi hiện thực một dựán mới,
chúng ta nên tạo lại ứng dụng từđầu đểdễquản lý. Trình tựđểtạo mới một ứng
dụng được trình bày như bên dưới.
Bước 1: Từmenu File, chúng ta chọn New Project..., như hướng dẫn ởHình 11.1.
Hình 11.1: Tạo mới một dựán
Bước 2: Tiếp theo đó, chúng ta cần chọn đường dẫn đểlưu mới dựán, tại mục
Location, như hướng dẫn ởHình 11.2. Cuối cùng bạn nhấn vào nút Create.
Bước 3: Cuối cùng, hệthống sẽxuất hiện một thông báo, với ý nghĩa rằng bạn sẽ
đóng dựán hiện tại, và mởdựán mới tại cửa sổnày, hay là vẫn giữdựán cũ và mở

<!-- page: 2 -->

một cửa sổmới cho dựán vừa tạo. Ởđây, chúng tôi khuyên bạn là nên chọn vào
This Window đểđóng lại dựán cũ và chỉmởdựán vừa tạo mà thôi, như minh họa
ởHình 11.3.
Tuy nhiên, chúng ta vẫn chưa thểbắt đầu lập trình được. Đối với các dựán dần lớn
hơn, việc đầu tiên là cài đặt các phần mềm hỗtrợcho việc hiện thực chương trình,
sẽđược trình bày ởphần tiếp theo của hướng dẫn này.
Trang 110
The Dariu Foundation

<!-- page: 111 -->
Hình 11.2: Chọn đường dẫn đểlưu dựán
Hình 11.3: Chọn This Window đểđóng dựán cũ và mởdựán mới
3
Cài đặt thư viện
Thực ra, khi hiện thực các dựán phức tạp, chúng ta sẽkhó có thểbắt đầu mọi thứ
từđầu. Thông thường, chúng ta sẽcài đặt thêm thư viện bên ngoài, đểhỗtrợcho
việc lập trình của chúng ta. Đây cũng chính là sức mạnh của cộng đồng lập trình
mã nguồn mở, và Python là một ví dụ. Khi tham khảo các dựán lớn, bạn sẽdễdàng
nhận ra, việc cài đặt thư viện sẽlà những bước đi đầu tiên.
Quá trình cài đặt thư viện sẽphức tạp ởchỗ, là thư viện bạn cần dùng, chẳng hạn
là thư viện A, nó lại phụthuộc vào một thư viện khác, chẳng hạn là thư viện B. Vấn
đềnày sẽxuất hiện khi bạn đang cài thư viện A, và hệthống sẽbáo lỗi là thiếu thư
viện B. Bạn cần phải cài đặt thư viện B trước, sau đó mới cài đặt lại thư viện A.
Trong bài này, chúng ta sẽlần lượt cài các thư viện sau đây: wheel, pipwin, pyaudio
và pyttsx3. Đây là thứtựcài đặt tốt nhất mà chúng tôi tìm hiểu đểviệc cài đặt sẽ
không bịbáo lỗi.
Bước 1: Đểbắt đầu việc cài đặt, chúng ta cần phải chuyển qua giao diện Terminal,
như minh họa ởHình 11.4
Hình 11.4: Giao diện Terminal đểcài đặt thư viện.
Hướng dẫn lập trình Python cơ bản
Trang 111

<!-- page: 112 -->
Từđây, bạn gõ vào dòng lệnh pip install wheel rồi nhấn Enter. Bạn cũng cần phải
kết nối mạng đểchương trình có thểtải thư viện vềtrước khi cài đặt. Trong trường
hợp mạng quá kém, quá thời gian cho phép, hệthống cũng sẽtựđộng dừng việc
cài đặt và bạn cần phải làm lại, cho đến khi nào thấy được dòng chữSuccessfully
installed wheel, như minh họa ởHình 12.1. Ởđây, pip là một công cụđểcài đặt
thư viện wheel.
Hình 11.5: Cài đặt thành công thư viện wheel.
Bước 2: Tương tự, chúng ta sẽcài đặt tiếp thư viện pipwin bằng công cụpip, với
câu lệnh pip install pipwin.
Bước 3: Đểcài đặt thư viện pyaudio, chúng ta không thểcài đặt bằng công cụpip
được. Lý do là nó không tương thích với một sốdriver vềâm thanh trên máy tính
xài hệđiều hành Windows. Chúng ta cần phải cài thư viện này bằng công cụpip-

<!-- page: 3 -->

win, tức là gõ pipwin install pyaudio trên cửa sổTerminal, rồi nhấn Enter.
Bước 4: Cuối cùng, chúng ta cài thư viện pyttsx3 bằng công cụpip, tức là gõ pip
install pyttsx3 rồi nhấn Enter.
4
Hiện thực chương trình
Trởlại với file main.py, chúng ta bắt đầu hiện thực chương trình bên dưới.
1 import pyttsx3
2
3 engine = pyttsx3.init ()
4 engine.say("I am AI python")
5 engine.runAndWait ()
Chương trình 11.1: Chương trình chuyển từchữsang giọng nói
Với thư viện hỗtrợlà pyttsx3 (được lấy vào chương trình bằng câu lệnh import ở
dòng 1), công việc của chúng ta khá đơn giản: Khởi tạo (dòng 3), truyền tham số
(dòng 4) và cuối cùng, cho phép chương trình nói ra loa. Bạn hãy lưu ý rằng, hiện
tại thư viện pyttsx3 chỉhỗtrợphát âm tiếng Anh mà thôi.
Trang 112
The Dariu Foundation
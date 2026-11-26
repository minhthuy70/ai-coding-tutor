<!-- page: 1 -->
# VI_PY_060: Kiểm thử độ chính xác số học dấu phẩy động và sai số tích lũy

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Độ chính xác | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 16 -->
Giới thiệu
Trong bối cảnh chuyển đổi sốmạnh mẽhiện nay, lập trình đã trởthành một công cụ
nền tảng không chỉđối với các nhà khoa học máy tính mà còn đối với kỹsư và nhà nghiên
cứu trong hầu hết các lĩnh vực khoa học – kỹthuật. Khảnăng mô hình hóa, mô phỏng, xử
lý dữliệu và tựđộng hóa bằng máy tính đóng vai trò then chốt trong việc giải quyết các
bài toán thực tiễn ngày càng phức tạp. Vì vậy, việc trang bịcho sinh viên những kiến thức
và kỹnăng lập trình ngay từgiai đoạn đào tạo đại học là một yêu cầu tất yếu.
Python là một trong những ngôn ngữlập trình phổbiến nhất hiện nay trong lĩnh vực
khoa học và kỹthuật nhờcú pháp đơn giản, dễtiếp cận, khảnăng biểu đạt cao và hệsinh
thái thư viện phong phú. Python cho phép người học tập trung vào tư duy thuật toán và
mô hình tính toán thay vì bịchi phối bởi các chi tiết cú pháp phức tạp. Đặc biệt, với các
thư viện mạnh như NumPy, SciPy và các công cụtrực quan hóa dữliệu, Python đã trở
thành ngôn ngữtiêu chuẩn trong tính toán khoa học, phân tích dữliệu và mô phỏng kỹ
thuật.
Giáo trình Lập trình Python dành cho kỹthuật được biên soạn nhằm phục vụgiảng dạy
và học tập cho sinh viên ngành Khoa học Máy tính, Trường Đại học Xây dựng Hà Nội.
Nội dung giáo trình được xây dựng theo hướng kết hợp chặt chẽgiữa lý thuyết và thực
hành, từnhững khái niệm cơ bản của lập trình Python đến các ứng dụng trong tính toán
số, xửlý dữliệu và mô hình hóa các bài toán kỹthuật. Giáo trình không chỉgiúp sinh viên
nắm vững cú pháp và cấu trúc của ngôn ngữPython mà còn hình thành tư duy lập trình
và khảnăng áp dụng Python như một công cụgiải quyết bài toán thực tế.
Bên cạnh việc trình bày các kiến thức nền tảng như kiểu dữliệu, điều khiển luồng, hàm
và module, giáo trình còn giới thiệu các thư viện quan trọng phục vụcho tính toán khoa
học và kỹthuật. Các ví dụminh họa và bài tập được thiết kếtheo hướng gần gũi với các
bài toán thực tế, giúp sinh viên từng bước làm quen với việc xây dựng mô hình tính toán,
thực hiện tính toán sốvà trực quan hóa kết quả.
Giáo trình được biên soạn với mục tiêu trởthành tài liệu học tập chính thức cho học
phần lập trình Python, đồng thời cũng có thểđược sửdụng như tài liệu tham khảo cho
sinh viên, học viên cao học và những người làm việc trong lĩnh vực khoa học – kỹthuật
có nhu cầu tiếp cận và ứng dụng Python trong công việc nghiên cứu và thực tiễn.
Tác giảxin chân thành cảm ơn các tài liệu, giáo trình và nguồn học thuật trong và
ngoài nước đã được tham khảo trong quá trình biên soạn. Mặc dù đã có nhiều cốgắng,
giáo trình khó tránh khỏi những thiếu sót, rất mong nhận được các ý kiến đóng góp của
đồng nghiệp và người học đểtài liệu ngày càng được hoàn thiện hơn.

<!-- page: 2 -->

1

<!-- page: 17 -->
CHƯƠNG 1. Biến, các kiểu dữliệu và toán tửcơ bản trong Python
1.1
Mởđầu
Trong mọi ngôn ngữlập trình, dữliệu là thành phần trung tâm quyết định cách chương
trình hoạt động và giải quyết bài toán. Đểlàm việc với dữliệu, người lập trình cần hiểu rõ
ba khái niệm nền tảng: biến, kiểu dữliệu và toán tử. Đây là những viên gạch đầu tiên để
xây dựng nên bất kỳchương trình nào, từnhững đoạn mã đơn giản cho đến các hệthống
phần mềm phức tạp trong kỹthuật và khoa học.
Python là một ngôn ngữlập trình bậc cao, được thiết kếvới mục tiêu đơn giản, dễđọc
và dễhọc. Khác với nhiều ngôn ngữlập trình truyền thống, Python cho phép người học
tiếp cận lập trình mà không cần khai báo kiểu dữliệu một cách tường minh. Tuy nhiên, sự
linh hoạt này chỉthực sựphát huy hiệu quảkhi người học hiểu rõ bản chất của các kiểu
dữliệu và cách Python xửlý chúng trong bộnhớ. Vì vậy, chương này tập trung trình bày
một cách chi tiết và có hệthống các khái niệm cơ bản nhất của Python, làm nền tảng cho
toàn bộnội dung phía sau của giáo trình.
1.2
Biến trong Python
1.2.1
Bản chất của biến
Trong Python, biến không đơn thuần là một vùng nhớnhư cách hiểu trong một sốngôn
ngữlập trình khác. Thực chất, biến là một tên gọi được dùng đểtham chiếu đến một đối
tượng tồn tại trong bộnhớ. Khi một giá trịđược gán cho biến, Python sẽtạo ra một đối
tượng tương ứng trong bộnhớvà liên kết tên biến với đối tượng đó.
Cách tiếp cận này giúp Python rất linh hoạt, cho phép một biến có thểtham chiếu đến
các đối tượng có kiểu dữliệu khác nhau tại các thời điểm khác nhau trong quá trình thực
thi chương trình. Điều này đặc biệt thuận tiện cho việc thửnghiệm, tính toán nhanh và mô
phỏng các bài toán kỹthuật.
1.2.2
Gán giá trịcho biến
Việc tạo biến trong Python được thực hiện thông qua phép gán bằng toán tử=. Không
cần bất kỳkhai báo nào trước đó, biến sẽtựđộng được tạo ra ngay tại thời điểm gán giá
trị.
x = 10
y = 3.5
message = "Hello Python"
Trong ví dụtrên, Python tựđộng nhận biết rằng x là một sốnguyên, y là một sốthực
và message là một chuỗi ký tự. Cơ chếnày được gọi là suy luận kiểu dữliệu (type
inference).
2

<!-- page: 18 -->
CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON

<!-- page: 3 -->

1.2.3
Đặt tên biến
Tên biến trong Python không chỉcó ý nghĩa kỹthuật mà còn ảnh hưởng trực tiếp đến
khảnăng đọc hiểu và bảo trì chương trình. Một tên biến tốt cần phản ánh đúng ý nghĩa
của dữliệu mà nó lưu trữ. Python cho phép sửdụng chữcái, chữsốvà dấu gạch dưới trong
tên biến, đồng thời phân biệt chữhoa và chữthường.
student_name = "An"
total_score = 85
Việc sửdụng những tên biến có ý nghĩa rõ ràng là một thói quen quan trọng trong lập
trình, đặc biệt trong các dựán kỹthuật và nghiên cứu có quy mô lớn.
Bên cạnh các quy tắc đặt tên biến hợp lệ, người học cũng cần nắm rõ những trường
hợp đặt tên biến sai thường gặp đểtránh lỗi cú pháp ngay từgiai đoạn viết chương trình.
Trong Python, các lỗi này sẽđược phát hiện ngay khi chương trình được thực thi, gây gián
đoạn quá trình chạy chương trình.
Một lỗi phổbiến là đặt tên biến bắt đầu bằng chữsố. Python không cho phép điều này
vì sẽgây nhầm lẫn với các hằng sốsốhọc.
2value = 10
Đoạn mã trên là không hợp lệvì tên biến không được phép bắt đầu bằng chữsố. Python
sẽbáo lỗi cú pháp ngay khi biên dịch.
Một lỗi thường gặp khác là sửdụng các ký tựđặc biệt như dấu gạch ngang hoặc khoảng
trắng trong tên biến.
student-name = "An"
total score = 100
Trong trường hợp này, dấu gạch ngang bịPython hiểu là toán tửtrừ, còn khoảng trắng
được coi là dấu phân tách giữa các từkhóa, do đó đều dẫn đến lỗi cú pháp.
Ngoài ra, việc sửdụng từkhóa (keyword) của Python làm tên biến cũng là một lỗi
nghiêm trọng. Các từkhóa này đã được Python định nghĩa sẵn cho các mục đích cú pháp
đặc biệt.
for = 5
class = "CS"
Những tên biến trên là không hợp lệvì for và class là các từkhóa của ngôn ngữ
Python. Đểtránh lỗi này, người học nên lựa chọn những tên biến có ý nghĩa, không trùng
3

<!-- page: 19 -->
CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON
với từkhóa và tuân thủđầy đủcác quy tắc đặt tên.
Việc hiểu rõ các cách đặt tên biến sai không chỉgiúp tránh lỗi cú pháp mà còn hình
thành thói quen lập trình đúng đắn, đặc biệt quan trọng trong các dựán kỹthuật và nghiên
cứu có quy mô lớn.
1.3
Các kiểu dữliệu cơ bản trong Python và đặc điểm bộnhớ
Trong quá trình lập trình, ngoài việc hiểu ý nghĩa logic của dữliệu, người lập trình kỹ
thuật cần quan tâm đến cách dữliệu được lưu trữtrong bộnhớvà phạm vi biểu diễn của
chúng. Điều này đặc biệt quan trọng khi xửlý dữliệu lớn, tính toán khoa học hoặc các bài

<!-- page: 4 -->

toán yêu cầu hiệu năng cao.
Python là ngôn ngữlập trình bậc cao với cơ chếquản lý bộnhớtựđộng. Không giống
như các ngôn ngữbậc thấp, người lập trình Python không cần trực tiếp cấp phát hay giải
phóng bộnhớ. Tuy nhiên, mỗi kiểu dữliệu trong Python vẫn chiếm một lượng bộnhớnhất
định và có phạm vi biểu diễn riêng, điều mà người học cần nắm rõ đểsửdụng hiệu quả.
1.3.1
Kiểu sốnguyên (int)
Kiểu sốnguyên trong Python được biểu diễn bằng int. Khác với các ngôn ngữnhư
C hoặc C++, Python không giới hạn sốnguyên trong một sốbit cốđịnh (ví dụ32-bit hay
64-bit). Thay vào đó, Python sửdụng cơ chếsốnguyên có độchính xác tùy ý (arbitrary
precision).
Điều này có nghĩa là phạm vi biểu diễn của sốnguyên trong Python chỉbịgiới hạn bởi
dung lượng bộnhớcủa hệthống. Tuy nhiên, đi kèm với sựlinh hoạt đó là chi phí bộnhớ
lớn hơn.
a = 10
b = 10**100
Vềmặt bộnhớ, một sốnguyên trong Python không chỉlưu giá trịmà còn lưu thêm
thông tin quản lý đối tượng. Trên hệthống 64-bit, một sốnguyên nhỏthường chiếm
khoảng 28 byte bộnhớ, và sẽtăng thêm khi giá trịlớn hơn.
1.3.2
Kiểu sốthực (float)
Kiểu sốthực trong Python được biểu diễn bằng float, tuân theo chuẩn IEEE 754
dạng double-precision. Mỗi sốthực chiếm 64 bit (8 byte) đểlưu giá trịdấu phẩy động.
x = 3.1415926535
Phạm vi biểu diễn xấp xỉcủa kiểu float là từ:
±1.8 × 10308
với độchính xác khoảng 15–16 chữsốthập phân. Do đặc điểm của biểu diễn dấu phẩy
4

<!-- page: 20 -->
CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON
động, các phép toán với float có thểphát sinh sai sốlàm tròn, điều này cần được lưu ý
trong các bài toán kỹthuật chính xác cao.
1.3.3
Kiểu logic (bool)
Kiểu logic bool chỉcó hai giá trịlà True và False. Vềmặt khái niệm, kiểu này chỉ
cần 1 bit đểbiểu diễn. Tuy nhiên, trong Python, bool là một đối tượng hoàn chỉnh, do đó
nó chiếm nhiều bộnhớhơn so với biểu diễn lý thuyết.
flag = True
Trên hệthống 64-bit, một giá trịbool thường chiếm khoảng 28 byte. Mặc dù chi phí
bộnhớlớn, kiểu bool đóng vai trò không thểthiếu trong điều khiển luồng chương trình
và biểu thức điều kiện.
1.3.4
Kiểu chuỗi (str)
Kiểu chuỗi str dùng đểlưu trữdữliệu văn bản. Chuỗi trong Python là một dãy các

<!-- page: 5 -->

ký tựUnicode, mỗi ký tựcó thểchiếm từ1 đến 4 byte tùy theo mã Unicode.
text = "Python"
Dung lượng bộnhớcủa một chuỗi phụthuộc vào:
• Sốlượng ký tự
• Loại ký tự(ASCII hay Unicode mởrộng)
• Thông tin quản lý đối tượng
Do đó, một chuỗi ngắn cũng có thểchiếm vài chục byte bộnhớ. Chuỗi trong Python là
bất biến (immutable), nghĩa là mỗi lần thay đổi nội dung, Python sẽtạo ra một đối tượng
mới trong bộnhớ.
1.3.5
So sánh bộnhớvà phạm vi biểu diễn của các kiểu dữliệu cơ bản
Bảng 1.1 tóm tắt đặc điểm bộnhớvà phạm vi biểu diễn của các kiểu dữliệu cơ bản
trong Python.
Bảng 1.1: So sánh các kiểu dữliệu cơ bản trong Python
Kiểu dữliệu
Bộnhớ(xấp xỉ)
Phạm vi biểu diễn
Ghi chú
int
∼28 byte
Không giới hạn
Tăng theo độlớn giá trị
float
8 byte
±1.8 × 10308
Sai sốlàm tròn
bool
∼28 byte
True / False
Kiểu logic
str
Phụthuộc độdài
Unicode
Bất biến
1.3.6
Nhận xét
Từbảng so sánh có thểthấy rằng Python đánh đổi hiệu năng và bộnhớđểđổi lấy tính
linh hoạt và dễsửdụng. Đối với các bài toán kỹthuật có quy mô lớn hoặc yêu cầu tối ưu
5
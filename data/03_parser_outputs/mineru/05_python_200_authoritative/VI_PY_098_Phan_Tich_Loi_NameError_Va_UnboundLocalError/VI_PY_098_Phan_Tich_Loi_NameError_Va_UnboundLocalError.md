<!-- page: 1 -->
# VI_PY_098: Phân tích lỗi biến chưa khai báo NameError và bẫy UnboundLocalError

**Nguồn tài liệu chính thống**: Cẩm nang Chẩn đoán & Gỡ lỗi Python ĐH  
**Chuyên mục**: Gỡ lỗi | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 96 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
diện cho sinh viên, các thuộc tính có thểlà tên, tuổi, mã sốsinh viên, điểm trung bình.
Mỗi đối tượng sinh viên sẽcó giá trịriêng cho các thuộc tính này, phản ánh thông tin cá
nhân của từng sinh viên.
Phương thức (Method) là các hàm được định nghĩa bên trong lớp, thểhiện các hành
động mà đối tượng có thểthực hiện. Phương thức thường hoạt động trên dữliệu của chính
đối tượng đó (tức là trên các thuộc tính của nó). Tiếp tục với ví dụvềsinh viên, các phương
thức có thểlà cập nhật điểm, tính điểm trung bình, hiển thịthông tin. Phương thức cho
phép đối tượng không chỉlưu trữdữliệu mà còn có khảnăng xửlý và thao tác trên dữliệu
đó.
5.2
Lớp và đối tượng trong Python
5.2.1
Định nghĩa lớp
Việc định nghĩa lớp trong Python là bước đầu tiên đểáp dụng tư duy hướng đối tượng
vào chương trình. Lớp được định nghĩa bằng từkhóa class, theo sau là tên lớp và dấu
hai chấm. Tên lớp theo quy ước thường được viết theo kiểu PascalCase, nghĩa là mỗi từ
trong tên đều viết hoa chữcái đầu và không có khoảng trắng hoặc ký tựđặc biệt ởgiữa.
Quy ước này giúp phân biệt rõ ràng giữa tên lớp và tên biến hoặc hàm, vốn thường được
viết theo kiểu snake_case.
Khi định nghĩa một lớp, chúng ta đang tạo ra một kiểu dữliệu mới trong Python. Kiểu
dữliệu này không chỉchứa dữliệu mà còn chứa cảcác hành vi liên quan đến dữliệu đó.
Điều này khác biệt hoàn toàn với các kiểu dữliệu nguyên thủy như int, str hay list,
vì chúng ta có toàn quyền kiểm soát cách thức hoạt động của kiểu dữliệu mới này.
a, Cú pháp định nghĩa lớp
class TenLop:
# Các thuộc tính và phương thức
pass
b, Ví dụđịnh nghĩa lớp đơn giản
Hãy bắt đầu với một ví dụđơn giản vềlớp Student đại diện cho sinh viên:
class Student:
pass
Lớp Student này chưa có bất kỳthuộc tính hay phương thức nào, nhưng đã là một
lớp hợp lệtrong Python. Từkhóa pass được sửdụng khi chúng ta muốn định nghĩa một

<!-- page: 2 -->

cấu trúc rỗng mà chưa cần triển khai chi tiết ngay lập tức.
5.2.2
Tạo đối tượng từlớp
Sau khi đã có định nghĩa lớp, bước tiếp theo là tạo ra các đối tượng cụthểtừlớp đó.
Quá trình này được gọi là khởi tạo đối tượng (instantiation) hoặc tạo thểhiện (instance
81

<!-- page: 97 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
creation). Mỗi đối tượng được tạo ra từlớp sẽcó cấu trúc giống nhau nhưng tồn tại độc
lập trong bộnhớvới trạng thái riêng biệt.
Khi gọi tên lớp với cặp dấu ngoặc tròn, Python thực hiện một chuỗi các thao tác phức
tạp bên dưới. Đầu tiên, Python cấp phát một vùng nhớmới đểchứa đối tượng. Sau đó,
nó khởi tạo các thuộc tính mặc định nếu có. Cuối cùng, nó gọi phương thức khởi tạo
__init__() nếu phương thức này được định nghĩa trong lớp. Kết quảtrảvềlà một
tham chiếu đến đối tượng mới được tạo, và tham chiếu này được gán cho biến mà chúng
ta chỉđịnh.
class Student:
pass
# Tạo đối tượng sinh viên
sv1 = Student()
sv2 = Student()
print(type(sv1))
print(type(sv2))
Kết quảhiển thị:
<class '__main__.Student'>
<class '__main__.Student'>
Trong ví dụtrên, sv1 và sv2 là hai đối tượng khác nhau được tạo từcùng lớp
Student. Mặc dù cùng được tạo từmột lớp, mỗi đối tượng chiếm một vùng nhớriêng
biệt và độc lập hoàn toàn với nhau. Điều này có nghĩa là bất kỳthay đổi nào trên sv1 sẽ
không ảnh hưởng đến sv2 và ngược lại.
5.2.3
Thuộc tính của đối tượng
Thuộc tính đóng vai trò như các biến thành viên của đối tượng, lưu trữtrạng thái và
thông tin đặc trưng của đối tượng đó. Mỗi đối tượng có bộgiá trịthuộc tính riêng, phản
ánh trạng thái hiện tại của nó. Đây chính là cơ chếcho phép các đối tượng được tạo từ
cùng một lớp có thểkhác biệt nhau vềmặt dữliệu.
Trong Python, thuộc tính của đối tượng được truy cập thông qua cú pháp chấm (dot
notation). Khi viết object.attribute, chúng ta đang yêu cầu Python lấy giá trịcủa
thuộc tính attribute thuộc vềđối tượng object. Cơ chếnày rất trực quan và phản
ánh đúng mối quan hệsởhữu giữa đối tượng và thuộc tính của nó.
a, Thêm thuộc tính động
Trong Python, chúng ta có thểthêm thuộc tính cho đối tượng bất kỳlúc nào sau khi
đối tượng được tạo:
82

<!-- page: 3 -->


<!-- page: 98 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
class Student:
pass
sv1 = Student()
sv1.name = "Nguyen Van An"
sv1.age = 20
sv1.major = "Computer Science"
print(f"Ten: {sv1.name}")
print(f"Tuoi: {sv1.age}")
print(f"Chuyen nganh: {sv1.major}")
Kết quảhiển thị:
Ten: Nguyen Van An
Tuoi: 20
Chuyen nganh: Computer Science
Tuy nhiên, cách thêm thuộc tính động như trên không được khuyến khích trong thực tế
vì không có tính nhất quán. Thay vào đó, chúng ta nên sửdụng phương thức khởi tạo.
5.3
Phương thức khởi tạo - Constructor
5.3.1
Phương thức __init__()
Phương thức __init__() là một trong những phương thức đặc biệt quan trọng nhất
trong lập trình hướng đối tượng với Python. Đây là phương thức được Python tựđộng gọi
ngay sau khi một đối tượng mới được tạo ra từlớp. Vai trò chính của phương thức này là
thiết lập trạng thái ban đầu cho đối tượng bằng cách khởi tạo các thuộc tính với những giá
trịphù hợp.
Mặc dù __init__() thường được gọi là constructor (hàm khởi tạo), vềmặt kỹthuật
nó không hoàn toàn giống với constructor trong các ngôn ngữnhư C++ hay Java. Trong
Python, việc tạo đối tượng thực sựđược thực hiện bởi phương thức __new__(), còn
__init__() chỉđảm nhiệm việc khởi tạo đối tượng đã được tạo. Tuy nhiên, trong hầu
hết các trường hợp, chúng ta chỉcần làm việc với __init__() mà không cần quan tâm
đến __new__().
Một đặc điểm quan trọng của __init__() là nó không trảvềgiá trị. Nếu cốgắng
trảvềmột giá trịkhác None, Python sẽbáo lỗi. Điều này hợp lý vì mục đích của phương
thức này là thiết lập đối tượng chứkhông phải tạo ra một giá trịmới đểtrảvề.
83
<!-- page: 1 -->
# VI_PY_049: Phạm vi biến trong hàm: Phân biệt Local, Global và từ khóa nonlocal

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Phạm vi biến | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 90 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print("Dict binh phuong:", squares_dict)
# Set comprehension (loại bỏtrùng lặp)
numbers_dup = [1, 2, 2, 3, 3, 3, 4, 5]
unique_squares = {x**2 for x in numbers_dup}
print("Set binh phuong:", unique_squares)
Kết quảhiển thị:
Dict binh phuong: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Set binh phuong: {1, 4, 9, 16, 25}
g, So sánh hiệu suất
List comprehension thường nhanh hơn so với vòng lặp thông thường hoặc map(),
đồng thời code ngắn gọn và dễđọc hơn.
# Ba cách tạo list
numbers = range(100)
# Cách 1: Vòng lặp for
result1 = []
for x in numbers:
result1.append(x ** 2)
# Cách 2: map()
result2 = list(map(lambda x: x ** 2, numbers))
# Cách 3: List comprehension (nhanh nhất)
result3 = [x ** 2 for x in numbers]
print("Cac cach cho ket qua giong nhau:",
result1[:5] == result2[:5] == result3[:5])
Kết quảhiển thị:
Cac cach cho ket qua giong nhau: True
h, Lưu ý khi sửdụng
Mặc dù list comprehension rất mạnh mẽ, cần tránh lạm dụng với các biểu thức quá
phức tạp vì sẽlàm giảm tính dễđọc của code. Với logic phức tạp, nên sửdụng vòng lặp
thông thường hoặc tách thành nhiều bước.
75

<!-- page: 2 -->


<!-- page: 91 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
4.10.10
So sánh các phương pháp xửlý tập hợp
Phương pháp
Đặc điểm
map()
Biến đổi từng phần tử, trảvềiterator
filter()
Lọc phần tửtheo điều kiện, trảvềiterator
reduce()
Rút gọn thành một giá trịduy nhất
List comprehension
Tạo list mới, cú pháp ngắn gọn, hiệu suất cao
Vòng lặp for
Linh hoạt nhất, phù hợp với logic phức tạp
Trong thực tế, lựa chọn phương pháp phụthuộc vào:
• Độphức tạp của logic
• Yêu cầu vềhiệu suất
• Tính dễđọc của code
• Quy ước của team/dựán
4.10.11
Khái niệm vềModule
Module là một tập tin Python chứa các hàm, biến và lớp. Việc sửdụng module cho
phép tổchức chương trình thành nhiều tệp nhỏ, giúp quản lý mã nguồn hiệu quảhơn.
4.10.12
Sửdụng module có sẵn
Python cung cấp rất nhiều module chuẩn hỗtrợtính toán và xửlý dữliệu.
import math
print(math.sqrt(16))
print(math.pi)
Kết quảhiển thị:
4.0
3.141592653589793
4.10.13
Tựxây dựng module
Giảsửtạo tập tin my_math.py với nội dung:
def cong(a, b):
return a + b
def tru(a, b):
return a - b
Sửdụng module này trong chương trình khác:
76


<!-- page: 3 -->

<!-- page: 92 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
import my_math
print(my_math.cong(3, 4))
print(my_math.tru(10, 5))
Kết quảhiển thị:
7
5
4.10.14
Ý nghĩa của hàm và module trong lập trình kỹthuật
Trong các hệthống kỹthuật, hàm và module giúp:
• Chuẩn hóa các phép tính và mô hình
• Tái sửdụng mã nguồn giữa các dựán
• Giảm lỗi và tăng độtin cậy của hệthống
4.10.15
Kết luận
Hàm và module là nền tảng của lập trình Python hiện đại. Việc nắm vững cách xây
dựng và sửdụng hàm, hàm vô danh và module giúp sinh viên chuyển từlập trình đơn giản
sang xây dựng các chương trình có cấu trúc, sẵn sàng cho các nội dung nâng cao như lập
trình hướng đối tượng và phân tích dữliệu.
4.11
Bài tập
Bài tập 1: Hàm tính toán cơ bản
Viết các hàm tính toán sau:
1. Hàm giai_thua(n): Tính giai thừa của sốnguyên dương n bằng đệquy
2. Hàm to_hop(n, k): Tính tổhợp Ck
n =
n!
k!(n−k)!
3. Hàm fibonacci(n): Tính sốFibonacci thứn
4. Hàm fibonacci_iterative(n): Tính Fibonacci bằng phương pháp lặp (so
sánh hiệu suất)
Yêu cầu: Kiểm tra tính hợp lệcủa tham sốđầu vào.
Bài tập 2: Hàm xửlý chuỗi
Viết các hàm xửlý chuỗi:
1. dem_tu(chuoi): Đếm sốtừtrong chuỗi
2. dao_nguoc_chuoi(chuoi): Đảo ngược toàn bộchuỗi
3. dao_nguoc_tu(chuoi): Đảo ngược từng từtrong chuỗi
4. loai_bo_ky_tu_dac_biet(chuoi): Chỉgiữlại chữcái, chữsốvà khoảng
trắng
77

<!-- page: 93 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
5. chuan_hoa_chuoi(chuoi): Loại bỏkhoảng trắng thừa

<!-- page: 4 -->

Bài tập 3: Hàm làm việc với List
Viết các hàm xửlý danh sách số:
1. thong_ke_list(ds): Trảvềdictionary chứa min, max, sum, mean, count
2. loc_chan(ds), loc_le(ds), loc_duong(ds): Lọc các phần tửthỏa điều
kiện
3. sap_xep_tang(ds), sap_xep_giam(ds): Sắp xếp danh sách
Kiểm tra với danh sách: [5, -3, 8, 12, -7, 0, 15, 4, -1, 9]
Bài tập 4: Lambda và Higher-order Functions
Cho danh sách sinh viên:
sinh_vien = [
{'ten': 'An', 'diem': 8.5},
{'ten': 'Binh', 'diem': 6.0},
{'ten': 'Cuong', 'diem': 7.5},
{'ten': 'Dung', 'diem': 9.0},
{'ten': 'Em', 'diem': 5.5}
]
Sửdụng map, filter, reduce và lambda để:
1. Lấy danh sách tên sinh viên
2. Tăng điểm mỗi sinh viên thêm 0.5 (tối đa 10)
3. Lọc sinh viên đạt (điểm ≥7)
4. Tính điểm trung bình của lớp
5. Tìm sinh viên có điểm cao nhất
Bài tập 5: Module và Package
Tạo module math_utils.py chứa:
1. Hàm la_so_nguyen_to(n): Kiểm tra sốnguyên tố
2. Hàm gcd(a, b): Tính ước chung lớn nhất
3. Hàm lcm(a, b): Tính bội chung nhỏnhất
4. Hàm giai_phuong_trinh_bac_2(a, b, c): Giải phương trình ax2 +bx+
c = 0
5. Các hằng số: PI, E
Tạo file main.py đểimport và test các hàm trong module.
Ghi chú: Xem lời giải chi tiết tại Phụlục - Lời giải bài tập.
78

<!-- page: 94 -->
CHƯƠNG 5. Lập trình hướng đối tượng trong Python
Trong các chương trước, chúng ta đã làm quen với lập trình theo hướng thủtục, nơi
chương trình được tổchức thành các hàm và dữliệu được xửlý tuần tự. Tuy nhiên, khi
chương trình trởnên phức tạp hơn, việc quản lý và bảo trì mã nguồn theo cách này có thể
gặp nhiều khó khăn. Lập trình hướng đối tượng (Object-Oriented Programming - OOP)
ra đời như một giải pháp mạnh mẽgiúp tổchức mã nguồn một cách logic, dễbảo trì và
tái sửdụng hơn.
Python là một ngôn ngữhỗtrợđầy đủcác tính năng của lập trình hướng đối tượng.
Hiểu và vận dụng tốt OOP không chỉgiúp sinh viên viết mã tốt hơn mà còn là nền tảng
đểhọc các framework và thư viện hiện đại trong Python.

<!-- page: 5 -->

5.1
Giới thiệu vềlập trình hướng đối tượng
5.1.1
Khái niệm lập trình hướng đối tượng
Lập trình hướng đối tượng là một phương pháp lập trình dựa trên khái niệm vềcác “đối
tượng”. Đối tượng là một thực thểcó thểchứa cảdữliệu (gọi là thuộc tính) và các hành
động liên quan đến dữliệu đó (gọi là phương thức). Đểhiểu rõ hơn vềOOP, chúng ta cần
nhìn nhận sựkhác biệt cơ bản giữa lập trình thủtục và lập trình hướng đối tượng.
Trong lập trình thủtục truyền thống, chương trình được tổchức thành các hàm độc lập,
mỗi hàm thực hiện một nhiệm vụcụthể. Dữliệu và các hàm xửlý dữliệu đó thường được
tách biệt nhau. Khi chương trình trởnên phức tạp với nhiều loại dữliệu và nhiều hàm xử
lý khác nhau, việc quản lý mối quan hệgiữa dữliệu và hàm trởnên khó khăn. Một thay
đổi nhỏtrong cấu trúc dữliệu có thểyêu cầu sửa đổi nhiều hàm khác nhau, dẫn đến nguy
cơ phát sinh lỗi và khó bảo trì.
Lập trình hướng đối tượng tiếp cận vấn đềtheo một cách khác. Thay vì tách biệt dữ
liệu và hành vi, OOP nhóm chúng lại với nhau thành các đối tượng. Mỗi đối tượng đại
diện cho một thực thểcụthểtrong bài toán, chứa đựng cảthông tin (thuộc tính) và hành vi
(phương thức) liên quan đến thực thểđó. Cách tiếp cận này phản ánh trực quan hơn cách
chúng ta nhìn nhận thếgiới thực, nơi mỗi sựvật đều có đặc điểm và hành động riêng.
Ví dụ, khi mô hình hóa một chiếc ô tô trong chương trình, lập trình thủtục có thể
tạo các biến riêng lẻđểlưu màu sắc, tốc độ, vịtrí, và các hàm riêng đểtăng tốc, phanh,
rẽ. Trong khi đó, OOP sẽtạo ra một đối tượng ô tô, bên trong nó chứa tất cảcác thuộc
tính (màu sắc, tốc độ, vịtrí) và các phương thức (tăng tốc, phanh, rẽ) liên quan. Điều này
không chỉlàm cho code dễhiểu hơn mà còn dễdàng mởrộng và bảo trì.
5.1.2
Lợi ích của lập trình hướng đối tượng
Lập trình hướng đối tượng mang lại nhiều lợi ích quan trọng trong phát triển phần
mềm, đặc biệt đối với các dựán có quy mô lớn và phức tạp. Một trong những lợi ích nổi
bật nhất là tính mô-đun hóa. Khi mã nguồn được tổchức thành các đối tượng độc lập, mỗi
đối tượng đảm nhận một trách nhiệm cụthể, việc phát triển và kiểm thửtrởnên dễdàng
79

<!-- page: 95 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
hơn nhiều. Các thành viên trong nhóm có thểlàm việc song song trên các lớp khác nhau
mà không lo xung đột code.
Tính tái sửdụng là một lợi thếquan trọng khác của OOP. Một khi đã xây dựng được
một lớp hoạt động tốt, lớp đó có thểđược sửdụng lại trong nhiều phần khác nhau của
chương trình, thậm chí trong các dựán khác. Điều này không chỉtiết kiệm thời gian mà
còn giảm thiểu lỗi, vì code đã được kiểm thửkỹlưỡng sẽít có khảnăng gây ra vấn đềkhi
được tái sửdụng.
Khảnăng bảo trì là một yếu tốthen chốt quyết định tuổi thọcủa phần mềm. Trong
OOP, việc thay đổi hoặc mởrộng chức năng thường chỉcần can thiệp vào một hoặc vài
lớp cụthể, mà không ảnh hưởng đến toàn bộhệthống. Điều này đặc biệt quan trọng khi
phần mềm cần được cập nhật thường xuyên đểđáp ứng yêu cầu thay đổi của người dùng.

<!-- page: 6 -->

Tính trừu tượng cho phép người lập trình ẩn đi các chi tiết triển khai phức tạp bên
trong đối tượng, chỉđểlộra bên ngoài những giao diện cần thiết. Người sửdụng đối
tượng không cần biết nó hoạt động như thếnào bên trong, chỉcần biết cách sửdụng các
phương thức công khai. Điều này giúp giảm độphức tạp nhận thức khi làm việc với hệ
thống lớn.
Cuối cùng, OOP cung cấp một cách tiếp cận tựnhiên đểmô hình hóa các vấn đềthực
tế. Trong thếgiới thực, chúng ta đã quen với việc tư duy theo các đối tượng cụthể: một
con chó, một chiếc xe, một tài khoản ngân hàng. OOP cho phép chúng ta chuyển đổi trực
tiếp các thực thểnày thành các đối tượng trong chương trình, làm cho quá trình thiết kế
và triển khai trởnên trực quan và dễhiểu hơn.
5.1.3
Các khái niệm cơ bản trong OOP
Trước khi đi sâu vào chi tiết kỹthuật, việc hiểu rõ các thuật ngữcơ bản trong OOP là
vô cùng quan trọng. Bốn khái niệm then chốt cần nắm vững là lớp, đối tượng, thuộc tính
và phương thức.
Lớp (Class) có thểđược hình dung như một bản thiết kếhoặc khuôn mẫu đểtạo ra các
đối tượng. Giống như bản vẽkiến trúc của một ngôi nhà, lớp định nghĩa cấu trúc và hành
vi mà các đối tượng được tạo ra từnó sẽcó. Lớp quy định những thuộc tính nào mỗi đối
tượng sẽchứa và những phương thức nào đối tượng đó có thểthực hiện. Tuy nhiên, bản
thân lớp không phải là một thực thểcụthể, nó chỉlà định nghĩa trừu tượng.
Đối tượng (Object), còn được gọi là thểhiện (instance), là một thực thểcụthểđược
tạo ra từlớp. Nếu lớp là bản vẽcủa ngôi nhà, thì đối tượng là ngôi nhà thực sựđược xây
dựng theo bản vẽđó. Từmột lớp, chúng ta có thểtạo ra nhiều đối tượng khác nhau, mỗi
đối tượng tồn tại độc lập với trạng thái riêng của nó. Mặc dù tất cảcác đối tượng cùng
được tạo từmột lớp sẽcó cùng cấu trúc và khảnăng, nhưng giá trịdữliệu cụthểmà mỗi
đối tượng lưu trữcó thểhoàn toàn khác nhau.
Thuộc tính (Attribute) là các biến được gắn liền với một đối tượng cụthể, dùng đểlưu
trữtrạng thái hoặc thông tin của đối tượng đó. Ví dụ, nếu chúng ta có một đối tượng đại
80

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

<!-- page: 7 -->

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

<!-- page: 8 -->

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

<!-- page: 9 -->

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

<!-- page: 99 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
a, Cú pháp
class TenLop:
def __init__(self, tham_so_1, tham_so_2):
self.thuoc_tinh_1 = tham_so_1
self.thuoc_tinh_2 = tham_so_2
Tham sốself xuất hiện như tham sốđầu tiên trong mọi phương thức của lớp và đóng
vai trò vô cùng quan trọng trong OOP với Python. Tham sốnày là tham chiếu đến chính
đối tượng mà phương thức đang được gọi trên đó. Khi chúng ta viết obj.method(),
Python tựđộng chuyển đổi thành Class.method(obj), do đó self sẽnhận được giá
trịlà obj.
Tên self chỉlà một quy ước được cộng đồng Python tuân theo rộng rãi, không phải
là từkhóa bắt buộc. Vềmặt lý thuyết, chúng ta có thểđặt tên khác cho tham sốnày, nhưng
việc sửdụng self giúp code trởnên dễđọc và dễhiểu hơn cho người khác. Thông qua
self, các phương thức có thểtruy cập và thay đổi các thuộc tính của đối tượng, cũng như
gọi các phương thức khác của cùng đối tượng đó.
Một điểm quan trọng cần lưu ý là mặc dù self xuất hiện trong định nghĩa phương
thức, chúng ta không truyền giá trịcho nó khi gọi phương thức. Python tựđộng xửlý việc
này, điều này giúp cú pháp gọi phương thức trởnên gọn gàng và tựnhiên hơn.
b, Ví dụsửdụng __init__()
class Student:
def __init__(self, name, age, major):
self.name = name
self.age = age
self.major = major
# Tạo đối tượng với các giá trịban đầu
sv1 = Student("Nguyen Van An", 20, "Computer Science")
sv2 = Student("Tran Thi Binh", 21, "Data Science")
print(f"Sinh vien 1: {sv1.name}, {sv1.age} tuoi")
print(f"Sinh vien 2: {sv2.name}, {sv2.age} tuoi")
Kết quảhiển thị:

<!-- page: 10 -->

Sinh vien 1: Nguyen Van An, 20 tuoi
Sinh vien 2: Tran Thi Binh, 21 tuoi
Với cách này, mỗi khi tạo một đối tượng Student, các thuộc tính name, age và
major sẽđược khởi tạo ngay lập tức với các giá trịđược truyền vào.
84

<!-- page: 100 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
5.3.2
Giá trịmặc định cho tham số
Các tham sốtrong __init__() có thểcó giá trịmặc định, cho phép tạo đối tượng
mà không cần truyền đầy đủcác tham số:
class Student:
def __init__(self, name, age=18, major="Undeclared"):
self.name = name
self.age = age
self.major = major
sv1 = Student("Nguyen Van An")
sv2 = Student("Tran Thi Binh", 21)
sv3 = Student("Le Van Cuong", 20, "AI")
print(f"{sv1.name}: {sv1.age} tuoi, {sv1.major}")
print(f"{sv2.name}: {sv2.age} tuoi, {sv2.major}")
print(f"{sv3.name}: {sv3.age} tuoi, {sv3.major}")
Kết quảhiển thị:
Nguyen Van An: 18 tuoi, Undeclared
Tran Thi Binh: 21 tuoi, Undeclared
Le Van Cuong: 20 tuoi, AI
5.4
Phương thức của lớp
5.4.1
Định nghĩa phương thức
Phương thức là các hàm được định nghĩa bên trong lớp. Chúng thểhiện các hành vi mà
đối tượng có thểthực hiện. Mọi phương thức đều có tham sốđầu tiên là self.
a, Ví dụđịnh nghĩa phương thức
class Student:
def __init__(self, name, age, major):
self.name = name
self.age = age
self.major = major
self.gpa = 0.0
def display_info(self):
print(f"Ten: {self.name}")
print(f"Tuoi: {self.age}")
print(f"Chuyen nganh: {self.major}")
print(f"GPA: {self.gpa}")

<!-- page: 11 -->

85
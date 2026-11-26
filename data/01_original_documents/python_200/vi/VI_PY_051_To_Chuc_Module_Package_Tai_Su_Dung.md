<!-- page: 1 -->
# VI_PY_051: Tổ chức Module và Package trong dự án phần mềm kỹ thuật

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Mô-đun | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 117 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
print(f"Sach '{book.title}' khong co san")
return False
def return_book(self, book):
if book in self.borrowed_books:
book.return_book()
self.borrowed_books.remove(book)
print(f"{self.name} da tra: {book.title}")
else:
print(f"{self.name} khong muon sach nay")
class Library:
def __init__(self, name):
self.name = name
self.books = []
self.members = []
def add_book(self, book):
self.books.append(book)
print(f"Da them sach: {book.title}")
def register_member(self, member):
self.members.append(member)
print(f"Da dang ky thanh vien: {member.name}")
def display_available_books(self):
print(f"\nSach con trong tai {self.name}:")
for book in self.books:
if not book.is_borrowed:
print(f"
- {book}")
# Sửdụng hệthống
library = Library("Thu vien HUCE")
# Thêm sách
book1 = Book("Python Programming", "John Smith", "ISBN001")
book2 = Book("Data Structures", "Jane Doe", "ISBN002")
book3 = Book("Algorithms", "Bob Johnson", "ISBN003")
library.add_book(book1)

<!-- page: 2 -->

library.add_book(book2)
library.add_book(book3)
# Đăng ký thành viên
102

<!-- page: 118 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
member1 = Member("Nguyen Van An", "M001")
member2 = Member("Tran Thi Binh", "M002")
library.register_member(member1)
library.register_member(member2)
# Mượn sách
print("\n--- Muon sach ---")
member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book1)
# Sách đã được mượn
# Hiển thịsách còn trống
library.display_available_books()
# Trảsách
print("\n--- Tra sach ---")
member1.return_book(book1)
# Hiển thịlại
library.display_available_books()
Kết quảhiển thị:
Da them sach: Python Programming
Da them sach: Data Structures
Da them sach: Algorithms
Da dang ky thanh vien: Nguyen Van An
Da dang ky thanh vien: Tran Thi Binh
--- Muon sach ---
Nguyen Van An da muon: Python Programming
Nguyen Van An da muon: Data Structures
Sach 'Python Programming' khong co san
Sach con trong tai Thu vien HUCE:
- Algorithms - Bob Johnson (Con trong)
--- Tra sach ---
Nguyen Van An da tra: Python Programming
Sach con trong tai Thu vien HUCE:
- Python Programming - John Smith (Con trong)
103

<!-- page: 119 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
- Algorithms - Bob Johnson (Con trong)

<!-- page: 3 -->

5.11
Bài tập thực hành
5.11.1
Bài tập cơ bản
Bài 1. Tạo lớp BankAccount với các yêu cầu:
• Thuộc tính: sốtài khoản, tên chủtài khoản, sốdư
• Phương thức: nộp tiền, rút tiền, kiểm tra sốdư
• Không cho phép rút quá sốdư hiện có
Bài 2. Tạo lớp Circle với:
• Thuộc tính: bán kính
• Phương thức: tính diện tích, tính chu vi
• Sửdụng property đểđảm bảo bán kính luôn dương
Bài 3. Tạo lớp Product đại diện cho sản phẩm trong cửa hàng với:
• Thuộc tính: tên, giá, sốlượng tồn kho
• Phương thức: bán hàng (giảm tồn kho), nhập hàng (tăng tồn kho)
• Không cho phép bán khi hết hàng
5.11.2
Bài tập nâng cao
Bài 4. Xây dựng hệthống quản lý phương tiện giao thông:
• Tạo lớp cha Vehicle với thuộc tính: tên, tốc độtối đa
• Tạo các lớp con: Car, Motorcycle, Truck
• Mỗi lớp con có thuộc tính riêng (ví dụ: Car có sốghếngồi, Truck có tải trọng)
• Tất cảđều có phương thức display_info() nhưng hiển thịthông tin khác nhau
Bài 5. Xây dựng hệthống quản lý sinh viên:
• Lớp Student với thuộc tính: họtên, mã sinh viên, danh sách điểm các môn
• Phương thức: thêm điểm, tính điểm trung bình, xếp loại học lực
• Sửdụng property đểbảo vệcác thuộc tính quan trọng
• Sửdụng magic methods đểso sánh sinh viên theo điểm trung bình
Bài 6. Tạo lớp Matrix đại diện cho ma trận với:
• Khởi tạo từlist 2 chiều
• Các phép toán: cộng, trừ, nhân ma trận (sửdụng magic methods)
• Phương thức: chuyển vị, tính định thức (nếu là ma trận vuông)
104

<!-- page: 120 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
5.12
Tổng kết chương
Lập trình hướng đối tượng là một trong những kỹnăng quan trọng nhất mà sinh viên
ngành Khoa học Máy tính cần nắm vững. Trong chương này, chúng ta đã học về:
• Khái niệm cơ bản: lớp, đối tượng, thuộc tính, phương thức
• Phương thức khởi tạo (__init__) và vai trò của self
• Tính đóng gói: cách bảo vệdữliệu thông qua thuộc tính private và getter/setter
• Tính kếthừa: tái sửdụng code và mởrộng chức năng
• Tính đa hình: cùng một giao diện, nhiều cách thức thực hiện khác nhau

<!-- page: 4 -->

• Magic methods: tùy biến cách đối tượng tương tác với các tính năng built-in
• Thuộc tính và phương thức lớp: dữliệu và hành vi được chia sẻ
OOP không chỉlà một kỹthuật lập trình mà còn là một cách tư duy vềcách tổchức và
thiết kếchương trình. Việc nắm vững OOP sẽgiúp sinh viên:
• Viết code dễđọc, dễbảo trì và dễmởrộng
• Làm việc hiệu quảvới các framework và thư viện hiện đại
• Phát triển các hệthống phần mềm quy mô lớn
• Chuẩn bịtốt cho việc học các chủđềnâng cao hơn
Đểthành thạo OOP, sinh viên cần luyện tập thường xuyên thông qua các bài tập và dự
án thực tế. Hãy bắt đầu từnhững ví dụđơn giản, sau đó dần dần xây dựng các hệthống
phức tạp hơn.
5.13
Bài tập
Bài tập 1: Class Sinh viên
Tạo class SinhVien đểquản lý thông tin sinh viên với các yêu cầu:
Thuộc tính:
• ma_sv: Mã sinh viên
• ho_ten: Họtên sinh viên
• nam_sinh: Năm sinh
• diem_list: Danh sách các điểm (mặc định là list rỗng)
Phương thức:
• them_diem(diem): Thêm điểm mới (kiểm tra 0 ≤điểm ≤10)
• tinh_diem_tb(): Tính điểm trung bình
• xep_loai(): Xếp loại học lực (Xuất sắc ≥9, Giỏi ≥8, Khá ≥7, Trung bình ≥
5, Yếu < 5)
105

<!-- page: 121 -->
CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
• __str__(): Hiển thịthông tin sinh viên
Bài tập 2: Class Hình học
Tạo hệthống phân cấp class cho các hình học:
Class cơ sởHinh:
• Phương thức dien_tich(): Tính diện tích (abstract)
• Phương thức chu_vi(): Tính chu vi (abstract)
• Phương thức __str__(): Hiển thịthông tin hình
Các class con:
1. HinhTron(ban_kinh): Kếthừa từHinh
2. HinhChuNhat(chieu_dai, chieu_rong): Kếthừa từHinh
3. TamGiac(a, b, c): Kếthừa từHinh (sửdụng công thức Heron)
Tạo danh sách các hình và tính tổng diện tích.
Bài tập 3: Class TaiKhoan Ngân hàng
Tạo class TaiKhoan đểquản lý tài khoản ngân hàng:
Thuộc tính:
• so_tai_khoan: Sốtài khoản

<!-- page: 5 -->

• chu_tai_khoan: Chủtài khoản
• __so_du: Sốdư (private attribute)
• lich_su: Lịch sửgiao dịch
• lai_suat_nam: Lãi suất (class variable = 0.05)
Phương thức:
• nap_tien(so_tien): Nạp tiền vào tài khoản
• rut_tien(so_tien): Rút tiền (kiểm tra sốdư đủ)
• chuyen_tien(tai_khoan_nhan, so_tien): Chuyển tiền đến tài khoản
khác
• xem_so_du(): Xem sốdư hiện tại
• _ghi_lich_su(loai, so_tien): Ghi lại giao dịch (protected method)
• in_lich_su(): In lịch sửcác giao dịch
Yêu cầu: Sửdụng encapsulation đểbảo vệthuộc tính sốdư, ghi lại thời gian và loại
giao dịch trong lịch sử.
Ghi chú: Xem lời giải chi tiết tại Phụlục - Lời giải bài tập.
106

<!-- page: 122 -->
CHƯƠNG 6. Thư viện NumPy trong Kỹthuật
6.1
Giới thiệu vềNumPy
NumPy (viết tắt của Numerical Python) là thư viện cốt lõi cho tính toán khoa học và
xửlý dữliệu sốtrong Python. Được phát triển từnăm 2005, NumPy cung cấp cấu trúc dữ
liệu mảng đa chiều (ndarray) với hiệu suất cao và một tập hợp phong phú các hàm toán
học đểthao tác trên các mảng này.
Trong lĩnh vực kỹthuật, NumPy đóng vai trò nền tảng cho hầu hết các công việc liên
quan đến tính toán số, xửlý ma trận, phân tích dữliệu đo lường, mô phỏng hệthống và
xửlý tín hiệu. Sựhiệu quảcủa NumPy đến từviệc các phép toán được thực thi bằng mã
C tối ưu, nhanh hơn nhiều lần so với các vòng lặp Python thông thường.
6.1.1
Tại sao NumPy quan trọng trong kỹthuật
Trong công việc kỹthuật, chúng ta thường xuyên làm việc với các tập dữliệu lớn từ
cảm biến, mô phỏng số, hoặc đo lường thực nghiệm. NumPy giúp:
• Xửlý ma trận và vector một cách hiệu quả, phục vụtính toán đại sốtuyến tính
• Thực hiện các phép biến đổi toán học phức tạp trên tập dữliệu lớn
• Tiết kiệm bộnhớnhờcấu trúc dữliệu tối ưu
• Tích hợp dễdàng với các thư viện khác như SciPy, Pandas, Matplotlib, TensorFlow
• Hỗtrợbroadcasting - cơ chếtựđộng mởrộng mảng khi thực hiện phép toán
6.1.2
Cài đặt và import NumPy
Cài đặt NumPy:
# Cài đặt qua pip
pip install numpy
# Hoặc qua conda
conda install numpy

<!-- page: 6 -->

Import thư viện:
import numpy as np
# Kiểm tra phiên bản
print(np.__version__)
Quy ước sửdụng alias np là chuẩn trong cộng đồng Python và được khuyến nghịsử
dụng đểcode ngắn gọn hơn.
107

<!-- page: 123 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
6.2
Mảng NumPy - ndarray
6.2.1
Khái niệm mảng đa chiều
Mảng NumPy (ndarray) là cấu trúc dữliệu đồng nhất chứa các phần tửcùng kiểu.
Khác với list Python có thểchứa nhiều kiểu dữliệu khác nhau, mảng NumPy yêu cầu tất
cảphần tửcó cùng kiểu, điều này giúp tối ưu hóa bộnhớvà tốc độtính toán.
Mảng có thểcó nhiều chiều:
• Mảng 1 chiều (1D): vector - biểu diễn chuỗi dữliệu đo, tín hiệu
• Mảng 2 chiều (2D): ma trận - biểu diễn dữliệu dạng bảng, ảnh grayscale
• Mảng 3 chiều (3D) trởlên: tensor - biểu diễn ảnh màu, dữliệu không gian-thời gian
6.2.2
Tạo mảng NumPy
a, Tạo từlist Python
import numpy as np
# Mảng 1 chiều từlist
arr1d = np.array([1, 2, 3, 4, 5])
print("Mang 1D:", arr1d)
print("Kieu:", type(arr1d))
# Mảng 2 chiều từlist lồng nhau
arr2d = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
print("\nMang 2D:")
print(arr2d)
# Mảng 3 chiều
arr3d = np.array([[[1, 2], [3, 4]],
[[5, 6], [7, 8]]])
print("\nMang 3D:")
print(arr3d)
Kết quả:
Mang 1D: [1 2 3 4 5]
Kieu: <class 'numpy.ndarray'>
Mang 2D:
[[1 2 3]

<!-- page: 7 -->

[4 5 6]
[7 8 9]]
108

<!-- page: 124 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
Mang 3D:
[[[1 2]
[3 4]]
[[5 6]
[7 8]]]
b, Các hàm tạo mảng đặc biệt
NumPy cung cấp nhiều hàm đểtạo mảng với giá trịđặc biệt, rất hữu ích trong các tính
toán kỹthuật.
# Ma trận không (zeros)
zeros = np.zeros((3, 4))
print("Ma tran khong 3x4:")
print(zeros)
# Ma trận một (ones)
ones = np.ones((2, 3))
print("\nMa tran mot 2x3:")
print(ones)
# Ma trận đơn vị(identity matrix)
identity = np.eye(4)
print("\nMa tran don vi 4x4:")
print(identity)
# Ma trận với giá trịcụthể
full = np.full((3, 3), 7)
print("\nMa tran toan gia tri 7:")
print(full)
# Ma trận đường chéo
diag = np.diag([1, 2, 3, 4])
print("\nMa tran duong cheo:")
print(diag)
Kết quả:
Ma tran khong 3x4:
[[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]]
109

<!-- page: 125 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
Ma tran mot 2x3:
[[1. 1. 1.]

<!-- page: 8 -->

[1. 1. 1.]]
Ma tran don vi 4x4:
[[1. 0. 0. 0.]
[0. 1. 0. 0.]
[0. 0. 1. 0.]
[0. 0. 0. 1.]]
c, Tạo mảng với dãy số
# Tạo dãy từ0 đến 9
arange1 = np.arange(10)
print("arange(10):", arange1)
# Tạo dãy từ5 đến 15 (không bao gồm 15)
arange2 = np.arange(5, 15)
print("arange(5, 15):", arange2)
# Tạo dãy với bước nhảy
arange3 = np.arange(0, 1, 0.1)
print("arange(0, 1, 0.1):", arange3)
# Tạo dãy chia đều (linspace)
linspace1 = np.linspace(0, 10, 5)
print("linspace(0, 10, 5):", linspace1)
# Dãy logarit
logspace1 = np.logspace(0, 3, 4)
print("logspace(0, 3, 4):", logspace1)
Kết quả:
arange(10): [0 1 2 3 4 5 6 7 8 9]
arange(5, 15): [ 5
6
7
8
9 10 11 12 13 14]
arange(0, 1, 0.1): [0.
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
linspace(0, 10, 5): [ 0.
2.5
5.
7.5 10. ]
logspace(0, 3, 4): [
1.
10.
100. 1000.]
Ứng dụng trong kỹthuật: Hàm linspace thường được dùng đểtạo trục thời gian
hoặc trục tần sốtrong phân tích tín hiệu.
110

<!-- page: 126 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT

<!-- page: 9 -->

d, Tạo mảng ngẫu nhiên
# Sốngẫu nhiên phân phối đều [0, 1)
rand1 = np.random.rand(3, 3)
print("random.rand(3, 3):")
print(rand1)
# Sốngẫu nhiên phân phối chuẩn (mean=0, std=1)
randn = np.random.randn(3, 3)
print("\nrandom.randn(3, 3):")
print(randn)
# Sốnguyên ngẫu nhiên
randint = np.random.randint(0, 100, (3, 4))
print("\nrandom.randint(0, 100, (3, 4)):")
print(randint)
# Chọn ngẫu nhiên từmảng cho trước
choice = np.random.choice([10, 20, 30, 40], size=(2, 3))
print("\nrandom.choice:")
print(choice)
6.2.3
Thuộc tính của mảng NumPy
Mảng NumPy có nhiều thuộc tính quan trọng giúp hiểu rõ cấu trúc dữliệu.
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print("Mang goc:")
print(arr)
print("\nshape (kich thuoc):", arr.shape)
# (3, 4)
print("ndim (so chieu):", arr.ndim)
# 2
print("size (tong phan tu):", arr.size)
# 12
print("dtype (kieu du lieu):", arr.dtype)
# int64
print("itemsize (kich thuoc 1 phan tu):", arr.itemsize)
# 8
bytes
,→
print("nbytes (tong kich thuoc):", arr.nbytes) # 96 bytes
Kết quả:
Mang goc:
[[ 1
2
3
4]
[ 5

<!-- page: 10 -->

6
7
8]
111

<!-- page: 127 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
[ 9 10 11 12]]
shape (kich thuoc): (3, 4)
ndim (so chieu): 2
size (tong phan tu): 12
dtype (kieu du lieu): int64
itemsize (kich thuoc 1 phan tu): 8
nbytes (tong kich thuoc): 96
6.2.4
Kiểu dữliệu trong NumPy
NumPy hỗtrợnhiều kiểu dữliệu sốvới độchính xác khác nhau, cho phép tối ưu bộ
nhớvà tốc độtính toán.
# Chỉđịnh kiểu dữliệu khi tạo mảng
int32_arr = np.array([1, 2, 3], dtype=np.int32)
float64_arr = np.array([1.5, 2.5, 3.5], dtype=np.float64)
bool_arr = np.array([True, False, True], dtype=np.bool_)
print("int32:", int32_arr.dtype)
print("float64:", float64_arr.dtype)
print("bool:", bool_arr.dtype)
# Chuyển đổi kiểu dữliệu
arr_float = np.array([1, 2, 3])
arr_int = arr_float.astype(np.float32)
print("\nChuyen doi kieu:", arr_int.dtype)
Các kiểu dữliệu phổbiến:
• int8, int16, int32, int64: Sốnguyên có dấu
• uint8, uint16, uint32, uint64: Sốnguyên không dấu
• float16, float32, float64: Sốthực dấu phẩy động
• complex64, complex128: Sốphức
• bool_: Boolean
6.3
Chỉmục và cắt lát mảng NumPy
Việc truy cập và thao tác với các phần tửhoặc các nhóm phần tửtrong mảng là kỹ
năng cơ bản nhưng cực kỳquan trọng khi làm việc với NumPy. NumPy cung cấp nhiều
cách linh hoạt đểlấy dữliệu từmảng, từchỉmục đơn giản đến các kỹthuật nâng cao như
fancy indexing và boolean indexing.
112

<!-- page: 128 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT

<!-- page: 11 -->

6.3.1
Chỉmục cơ bản
a, Chỉmục mảng 1 chiều
Tương tựnhư list Python, mảng 1 chiều có thểtruy cập bằng chỉsốtừ0.
arr = np.array([10, 20, 30, 40, 50])
print("Phan tu dau tien:", arr[0])
# 10
print("Phan tu cuoi cung:", arr[-1])
# 50
print("Phan tu thu 3:", arr[2])
# 30
# Thay đổi giá trị
arr[1] = 999
print("Sau khi thay doi:", arr)
Kết quả:
Phan tu dau tien: 10
Phan tu cuoi cung: 50
Phan tu thu 3: 30
Sau khi thay doi: [ 10 999
30
40
50]
b, Chỉmục mảng 2 chiều
Với mảng 2 chiều, ta sửdụng cú pháp arr[row, col] đểtruy cập phần tử. Lưu ý
rằng chỉsốhàng (row) đứng trước, chỉsốcột (col) đứng sau.
matrix = np.array([[10, 20, 30],
[40, 50, 60],
[70, 80, 90]])
print("Phan tu o hang 0, cot 1:", matrix[0, 1])
# 20
print("Phan tu o hang 2, cot 2:", matrix[2, 2])
# 90
print("Phan tu o hang 1, cot 0:", matrix[1, 0])
# 40
# Có thểdùng chỉsốâm
print("Hang cuoi, cot cuoi:", matrix[-1, -1])
# 90
# Thay đổi giá trị
matrix[1, 1] = 555
print("\nMa tran sau khi thay doi:")
print(matrix)
Kết quả:
Phan tu o hang 0, cot 1: 20
113


<!-- page: 12 -->

<!-- page: 129 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
Phan tu o hang 2, cot 2: 90
Phan tu o hang 1, cot 0: 40
Hang cuoi, cot cuoi: 90
Ma tran sau khi thay doi:
[[ 10
20
30]
[ 40 555
60]
[ 70
80
90]]
6.3.2
Cắt lát (Slicing)
Slicing cho phép trích xuất một phần của mảng theo cú pháp start:stop:step.
Đây là công cụmạnh mẽđểlấy các dòng, cột hoặc vùng dữliệu cụthể.
a, Cắt lát mảng 1 chiều
arr = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Phan tu tu 2 den 5:", arr[2:6])
# [20 30 40 50]
print("Tu dau den chi so 4:", arr[:5])
# [0 10 20 30
40]
,→
print("Tu chi so 5 den cuoi:", arr[5:])
# [50 60 70 80
90]
,→
print("Tat ca phan tu:", arr[:])
# Toan bo mang
print("Phan tu chan (buoc 2):", arr[::2])
# [0 20 40 60
80]
,→
print("Dao nguoc mang:", arr[::-1])
# [90 80 70 ...
0]
,→
Kết quả:
Phan tu tu 2 den 5: [20 30 40 50]
Tu dau den chi so 4: [ 0 10 20 30 40]
Tu chi so 5 den cuoi: [50 60 70 80 90]
Tat ca phan tu: [ 0 10 20 30 40 50 60 70 80 90]

<!-- page: 13 -->

Phan tu chan (buoc 2): [ 0 20 40 60 80]
Dao nguoc mang: [90 80 70 60 50 40 30 20 10
0]
b, Cắt lát mảng 2 chiều
Với mảng 2 chiều, ta có thểcắt lát theo từng chiều một cách độc lập.
A = np.array([[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120],
[130, 140, 150, 160]])
114

<!-- page: 130 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
print("Ma tran goc:")
print(A)
# Lấy toàn bộdòng đầu tiên
print("\nDong dau tien:", A[0, :])
# Lấy toàn bộcột thứhai
print("Cot thu hai:", A[:, 1])
# Lấy ma trận con 2x2 từgóc trên trái
print("\nMa tran con 2x2 (trai tren):")
print(A[:2, :2])
# Lấy ma trận con 2x3 ởgiữa
print("\nMa tran con 2x3 (giua):")
print(A[1:3, 1:4])
# Lấy từng dòng cách nhau
print("\nCac dong chan:")
print(A[::2, :])
# Lấy từng cột cách nhau
print("\nCac cot le:")
print(A[:, 1::2])
Kết quả:
Ma tran goc:
[[ 10
20
30
40]
[ 50
60
70
80]
[ 90 100 110 120]
[130 140 150 160]]
Dong dau tien: [10 20 30 40]
Cot thu hai: [ 20

<!-- page: 14 -->

60 100 140]
Ma tran con 2x2 (trai tren):
[[10 20]
[50 60]]
Ma tran con 2x3 (giua):
[[ 60
70
80]
115
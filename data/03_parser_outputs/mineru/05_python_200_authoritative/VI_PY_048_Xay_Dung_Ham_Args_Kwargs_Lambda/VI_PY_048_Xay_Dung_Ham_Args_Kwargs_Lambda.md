<!-- page: 1 -->
# VI_PY_048: Xây dựng hàm, tham số mặc định, *args, **kwargs và hàm ẩn danh lambda

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Hàm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 77 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
Trong ví dụnày, giá trị5 được gán cho chieu_dai và 3 được gán cho chieu_rong
dựa trên vịtrí.
b, Tham sốmặc định
Tham sốmặc định cho phép hàm có giá trịmặc định nếu người dùng không truyền
tham sốtương ứng. Điều này giúp hàm trởnên linh hoạt hơn và giảm sốlượng tham số
bắt buộc.
def tinh_lai_suat(von, lai_suat=0.05):
return von * lai_suat
print(tinh_lai_suat(1000000))
print(tinh_lai_suat(1000000, 0.1))
Kết quảhiển thị:
50000.0
100000.0
Trong các bài toán kỹthuật và kinh tế, tham sốmặc định thường được dùng cho các hệ
số, ngưỡng hoặc giá trịchuẩn.
c, Lưu ý khi sửdụng tham sốmặc định
Tham sốmặc định chỉđược đánh giá một lần tại thời điểm hàm được định nghĩa. Do
đó, không nên sửdụng các kiểu dữliệu mutable (như list hoặc dictionary) làm giá trịmặc
định.
def them_gia_tri(x, ds=[]):
ds.append(x)
return ds
print(them_gia_tri(1))
print(them_gia_tri(2))
Kết quảhiển thị:
[1]
[1, 2]
Cách viết trên dễgây lỗi logic. Cách đúng là:
62

<!-- page: 78 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
def them_gia_tri(x, ds=None):

<!-- page: 2 -->

if ds is None:
ds = []
ds.append(x)
return ds
print(them_gia_tri(1))
print(them_gia_tri(2))
d, Tham sốtừkhóa
Python cho phép truyền tham sốtheo tên, không phụthuộc vào thứtự.
def thong_tin_sv(ten, tuoi, diem):
print(ten, tuoi, diem)
thong_tin_sv(tuoi=20, ten="An", diem=8.5)
Cách truyền này giúp mã nguồn dễđọc và hạn chếnhầm lẫn khi hàm có nhiều tham
số.
e, Tham số*args
*args cho phép hàm nhận một sốlượng tham sốvịtrí không xác định. Các giá trị
truyền vào sẽđược gom lại thành một tuple.
def tinh_tong(*args):
tong = 0
for x in args:
tong += x
return tong
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20))
Kết quảhiển thị:
6
50
Trong các bài toán kỹthuật, *args thường được dùng khi sốlượng dữliệu đầu vào
không cốđịnh, ví dụnhư tập các giá trịđo.
f, Tham số**kwargs
**kwargs cho phép hàm nhận một sốlượng tham sốtừkhóa không xác định. Các
tham sốnày được lưu trữdưới dạng dictionary.
63

<!-- page: 79 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
def thong_tin_thiet_bi(**kwargs):
for key, value in kwargs.items():
print(key, ":", value)
thong_tin_thiet_bi(ten="Sensor A", do_chinh_xac=0.01,
trang_thai=True)
,→
Kết quảhiển thị:
ten : Sensor A
do_chinh_xac : 0.01
trang_thai : True

<!-- page: 3 -->

g, Kết hợp tham sốthường, *args và **kwargs
Python cho phép kết hợp nhiều loại tham sốtrong cùng một hàm, theo thứtự: tham số
thường →*args →**kwargs.
def xu_ly_du_lieu(loai, *values, **options):
print("Loai:", loai)
print("Gia tri:", values)
print("Tuy chon:", options)
xu_ly_du_lieu(
"nhiet_do",
20.5, 21.0, 22.3,
don_vi="C",
canh_bao=30
)
4.10.5
Hàm trảvềgiá trị
Nhiều hàm không chỉthực hiện thao tác mà còn cần trảvềkết quảđểsửdụng tiếp
trong chương trình. Python sửdụng từkhóa return cho mục đích này.
def tinh_trung_binh(a, b):
return (a + b) / 2
kq = tinh_trung_binh(6, 8)
print("Gia tri trung binh:", kq)
Kết quảhiển thị:
Gia tri trung binh: 7.0
Trong các bài toán kỹthuật, việc trảvềkết quảtừhàm là rất phổbiến, đặc biệt trong
64

<!-- page: 80 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
các phép tính lặp hoặc mô phỏng.
a, Hàm trảvềnhiều giá trị
Trong Python, một hàm có thểtrảvềnhiều giá trịcùng lúc. Thực chất, các giá trịnày
được đóng gói trong một tuple.
def thong_ke(ds):
tong = sum(ds)
trung_binh = tong / len(ds)
return tong, trung_binh
kq = thong_ke([2, 4, 6, 8])
print(kq)
Kết quảhiển thị:
(20, 5.0)
Có thểtách các giá trịtrảvề:
tong, tb = thong_ke([2, 4, 6, 8])
print("Tong:", tong)
print("Trung binh:", tb)
b, Ý nghĩa trong lập trình kỹthuật

<!-- page: 4 -->

Việc sửdụng linh hoạt các loại tham sốgiúp:
• Thiết kếhàm tổng quát, tái sửdụng cao
• Giảm sốlượng hàm cần viết
• Dễmởrộng chương trình khi yêu cầu thay đổi
Trong các hệthống kỹthuật lớn, các hàm thường nhận nhiều loại dữliệu đầu vào khác
nhau. Việc hiểu rõ tham sốmặc định, *args, **kwargs và cách trảvềnhiều giá trịlà
kỹnăng bắt buộc đối với lập trình viên Python.
4.10.6
Phạm vi biến trong hàm
Biến được khai báo bên trong hàm gọi là biến cục bộ. Biến này chỉtồn tại trong phạm
vi của hàm.
65

<!-- page: 81 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
x = 10
def test():
x = 5
print("x trong ham:", x)
test()
print("x ben ngoai:", x)
Kết quảhiển thị:
x trong ham: 5
x ben ngoai: 10
4.10.7
Hàm vô danh (Lambda function)
a, Khái niệm
Hàm vô danh, hay còn gọi là lambda function, là hàm không có tên, thường được sử
dụng cho các phép toán đơn giản trong thời gian ngắn. Hàm lambda giúp mã nguồn ngắn
gọn hơn, nhưng không nên lạm dụng trong các logic phức tạp.
b, Cú pháp hàm lambda
square = lambda x: x * x
print(square(4))
Kết quảhiển thị:
16
c, Ứng dụng lambda trong xửlý tập hợp
Hàm lambda thường được kết hợp với các hàm xửlý tập hợp như map(), filter(),
và reduce() đểxửlý dữliệu một cách ngắn gọn và hiệu quả.
values = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, values))
print(result)
Kết quảhiển thị:
[2, 4, 6, 8]
4.10.8
Các hàm xửlý tập hợp trong Python

<!-- page: 5 -->

Python cung cấp một sốhàm built-in mạnh mẽđểxửlý tập hợp dữliệu. Các hàm này
thường được sửdụng kết hợp với hàm lambda hoặc các hàm thông thường đểbiến đổi, lọc
và tổng hợp dữliệu một cách hiệu quả.
66

<!-- page: 82 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
a, Hàm map()
Hàm map() áp dụng một hàm lên từng phần tửcủa một hoặc nhiều iterable (như list,
tuple) và trảvềmột iterator chứa kết quả. Đây là công cụmạnh mẽđểbiến đổi dữliệu mà
không cần viết vòng lặp tường minh.
Cú pháp: map(function, iterable, ...)
Ví dụ1: Áp dụng hàm lên một list
# Sửdụng với hàm thông thường
def binh_phuong(x):
return x ** 2
numbers = [1, 2, 3, 4, 5]
result = list(map(binh_phuong, numbers))
print("Binh phuong:", result)
# Sửdụng với lambda
result2 = list(map(lambda x: x ** 3, numbers))
print("Lap phuong:", result2)
Kết quảhiển thị:
Binh phuong: [1, 4, 9, 16, 25]
Lap phuong: [1, 8, 27, 64, 125]
Ví dụ2: Chuyển đổi kiểu dữliệu
# Chuyển chuỗi thành số
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print("Chuyen sang int:", int_numbers)
# Chuyển sốthành chuỗi
numbers = [10, 20, 30]
str_nums = list(map(str, numbers))
print("Chuyen sang str:", str_nums)
Kết quảhiển thị:
Chuyen sang int: [1, 2, 3, 4, 5]
Chuyen sang str: ['10', '20', '30']
Ví dụ3: Map với nhiều iterable
Khi map() nhận nhiều iterable, hàm được áp dụng sẽnhận nhiều đối sốtương ứng.
67

<!-- page: 83 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
# Tính tổng từng cặp phần tử
a = [1, 2, 3, 4]

<!-- page: 6 -->

b = [10, 20, 30, 40]
tong = list(map(lambda x, y: x + y, a, b))
print("Tong cac cap:", tong)
# Tính trung bình hai list
tb = list(map(lambda x, y: (x + y) / 2, a, b))
print("Trung binh:", tb)
Kết quảhiển thị:
Tong cac cap: [11, 22, 33, 44]
Trung binh: [5.5, 11.0, 16.5, 22.0]
Ứng dụng trong kỹthuật:
Trong xửlý dữliệu đo từcảm biến, map() thường được dùng đểchuyển đổi đơn vị
hoặc chuẩn hóa dữliệu.
# Chuyển đổi nhiệt độtừCelsius sang Fahrenheit
celsius = [0, 10, 20, 30, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print("Fahrenheit:", fahrenheit)
# Chuẩn hóa dữliệu điện áp (chia cho 1000 đểđổi mV sang V)
voltage_mv = [1500, 3300, 5000, 12000]
voltage_v = list(map(lambda mv: mv / 1000, voltage_mv))
print("Dien ap (V):", voltage_v)
Kết quảhiển thị:
Fahrenheit: [32.0, 50.0, 68.0, 86.0, 212.0]
Dien ap (V): [1.5, 3.3, 5.0, 12.0]
b, Hàm filter()
Hàm filter() lọc các phần tửtrong iterable dựa trên một điều kiện. Chỉnhững
phần tửlàm cho hàm điều kiện trảvềTrue mới được giữlại.
Cú pháp: filter(function, iterable)
Ví dụ1: Lọc sốchẵn
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Lọc sốchẵn
68

<!-- page: 84 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
so_chan = list(filter(lambda x: x % 2 == 0, numbers))
print("So chan:", so_chan)
# Lọc sốlớn hơn 5
lon_hon_5 = list(filter(lambda x: x > 5, numbers))
print("Lon hon 5:", lon_hon_5)
Kết quảhiển thị:
So chan: [2, 4, 6, 8, 10]
Lon hon 5: [6, 7, 8, 9, 10]
Ví dụ2: Lọc chuỗi
names = ["An", "Binh", "C", "Dung", "E", "Phong"]
# Lọc tên có độdài lớn hơn 1

<!-- page: 7 -->

ten_dai = list(filter(lambda name: len(name) > 1, names))
print("Ten dai hon 1 ky tu:", ten_dai)
# Lọc tên bắt đầu bằng chữcái có mã ASCII > 68
ten_loc = list(filter(lambda name: ord(name[0]) > 68,
names))
,→
print("Ten bat dau tu 'E' tro di:", ten_loc)
Kết quảhiển thị:
Ten dai hon 1 ky tu: ['An', 'Binh', 'Dung', 'Phong']
Ten bat dau tu 'E' tro di: ['E', 'Phong']
Ứng dụng trong kỹthuật:
Lọc dữliệu không hợp lệhoặc vượt ngưỡng từtập dữliệu đo.
# Dữliệu nhiệt độtừcảm biến
nhiet_do = [22.5, 23.0, 150.0, 22.8, -50.0, 23.2, 24.0]
# Lọc dữliệu hợp lệ(từ0 đến 100 độC)
nhiet_do_hop_le = list(filter(lambda t: 0 <= t <= 100,
nhiet_do))
,→
print("Nhiet do hop le:", nhiet_do_hop_le)
# Cảnh báo nhiệt độcao
canh_bao = list(filter(lambda t: t > 30, nhiet_do_hop_le))
print("Canh bao nhiet do cao:", canh_bao)
69

<!-- page: 85 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
Kết quảhiển thị:
Nhiet do hop le: [22.5, 23.0, 22.8, 23.2, 24.0]
Canh bao nhiet do cao: []
c, Hàm reduce()
Hàm reduce() (trong module functools) áp dụng một hàm hai đối sốlên các
phần tửcủa iterable theo cách tích lũy, từtrái sang phải, đểrút gọn iterable thành một giá
trịduy nhất.
Cú pháp: reduce(function, iterable[, initializer])
Ví dụ1: Tính tổng và tích
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Tính tổng
tong = reduce(lambda x, y: x + y, numbers)
print("Tong:", tong)
# Tính tích
tich = reduce(lambda x, y: x * y, numbers)
print("Tich:", tich)
Kết quảhiển thị:
Tong: 15

<!-- page: 8 -->

Tich: 120
Quá trình hoạt động của reduce() với tổng:
• Bước 1: 1 + 2 = 3
• Bước 2: 3 + 3 = 6
• Bước 3: 6 + 4 = 10
• Bước 4: 10 + 5 = 15
Ví dụ2: Tìm giá trịlớn nhất và nhỏnhất
from functools import reduce
numbers = [15, 7, 23, 9, 31, 12]
# Tìm max
max_val = reduce(lambda x, y: x if x > y else y, numbers)
70

<!-- page: 86 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
print("Gia tri lon nhat:", max_val)
# Tìm min
min_val = reduce(lambda x, y: x if x < y else y, numbers)
print("Gia tri nho nhat:", min_val)
Kết quảhiển thị:
Gia tri lon nhat: 31
Gia tri nho nhat: 7
Ví dụ3: Ghép chuỗi
from functools import reduce
words = ["Python", "la", "ngon", "ngu", "manh", "me"]
cau = reduce(lambda x, y: x + " " + y, words)
print(cau)
Kết quảhiển thị:
Python la ngon ngu manh me
Ứng dụng trong kỹthuật:
Tính toán tích lũy trên chuỗi dữliệu.
from functools import reduce
# Tính tổng công suất tiêu thụcủa các thiết bị
cong_suat = [100, 250, 75, 300, 150]
# Watt
tong_cong_suat = reduce(lambda x, y: x + y, cong_suat)
print("Tong cong suat:", tong_cong_suat, "W")
# Tính điện trởtương đương mạch nối tiếp
dien_tro = [10, 20, 30, 15]
# Ohm
R_tuong_duong = reduce(lambda x, y: x + y, dien_tro)
print("Dien tro tuong duong:", R_tuong_duong, "Ohm")
Kết quảhiển thị:
Tong cong suat: 875 W
Dien tro tuong duong: 75 Ohm

<!-- page: 9 -->

71

<!-- page: 87 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
4.10.9
List Comprehension
List comprehension là một cú pháp ngắn gọn và pythonic đểtạo list mới từmột iterable
có sẵn. Đây là một trong những tính năng được yêu thích nhất của Python vì tính rõ ràng
và hiệu suất cao.
a, Cú pháp cơ bản
Cú pháp tổng quát: [expression for item in iterable if condition]
Ví dụ1: Tạo list đơn giản
# Cách thông thường
binh_phuong = []
for x in range(1, 6):
binh_phuong.append(x ** 2)
print("Cach thuong:", binh_phuong)
# Dùng list comprehension
binh_phuong_2 = [x ** 2 for x in range(1, 6)]
print("List comprehension:", binh_phuong_2)
Kết quảhiển thị:
Cach thuong: [1, 4, 9, 16, 25]
List comprehension: [1, 4, 9, 16, 25]
b, List comprehension với điều kiện
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Lọc sốchẵn
so_chan = [x for x in numbers if x % 2 == 0]
print("So chan:", so_chan)
# Bình phương các sốlẻ
binh_phuong_le = [x ** 2 for x in numbers if x % 2 != 0]
print("Binh phuong so le:", binh_phuong_le)
# Điều kiện if-else trong expression
phan_loai = ["chan" if x % 2 == 0 else "le" for x in
numbers]
,→
print("Phan loai:", phan_loai)
Kết quảhiển thị:
So chan: [2, 4, 6, 8, 10]
Binh phuong so le: [1, 9, 25, 49, 81]
72

<!-- page: 88 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
Phan loai: ['le', 'chan', 'le', 'chan', 'le', 'chan', 'le', 'chan', 'l
c, List comprehension lồng nhau

<!-- page: 10 -->

# Tạo ma trận
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in matrix:
print(row)
# Làm phẳng ma trận
flat = [num for row in matrix for num in row]
print("Ma tran phang:", flat)
Kết quảhiển thị:
[1, 2, 3]
[2, 4, 6]
[3, 6, 9]
Ma tran phang: [1, 2, 3, 2, 4, 6, 3, 6, 9]
d, Ứng dụng trong xửlý chuỗi
# Chuyển chữthường thành chữhoa
words = ["python", "programming", "language"]
upper_words = [w.upper() for w in words]
print("Chu hoa:", upper_words)
# Lọc từcó độdài > 5
long_words = [w for w in words if len(w) > 5]
print("Tu dai:", long_words)
# Lấy ký tựđầu của mỗi từ
first_chars = [w[0] for w in words]
print("Ky tu dau:", first_chars)
Kết quảhiển thị:
Chu hoa: ['PYTHON', 'PROGRAMMING', 'LANGUAGE']
Tu dai: ['python', 'programming', 'language']
Ky tu dau: ['p', 'p', 'l']
e, Ứng dụng trong kỹthuật
Ví dụ1: Xửlý dữliệu cảm biến
73
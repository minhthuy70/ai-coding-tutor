# VI_PY_058: Ứng dụng Python: Giải quyết bài toán cơ học kết cấu và sức bền vật liệu

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Ứng dụng | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
Tìm Nghiệm: Phương pháp bisection cung cấp giải pháp tin cậy nhưng chậm, trong
khi fsolve dựa trên Newton-Raphson hội tụnhanh hơn nhiều. Chúng ta đã học cách áp
dụng cho cảphương trình đơn và hệphương trình phi tuyến, với các ví dụtừtoán học
thuần túy đến bài toán cân bằng hóa học.
Nội suy: Từnội suy tuyến tính đơn giản đến cubic spline phức tạp, mỗi phương pháp
có ưu nhược điểm riêng. Cubic spline nổi bật với đường cong mượt mà và ổn định, phù
hợp cho đa sốứng dụng. Nội suy 2D mởrộng khảnăng xửlý dữliệu không gian như bản
đồđịa hình và phân bốnhiệt độ.
Thông qua các ví dụthực tếvà bài tập đa dạng, chương này không chỉdạy cách sử
dụng các hàm SciPy, mà còn giúp hiểu bản chất toán học đằng sau, khảnăng áp dụng vào
các bài toán thực tế, và cách đánh giá, so sánh các phương pháp khác nhau.
SciPy là công cụkhông thểthiếu trong hành trang của mọi kỹsư, nhà khoa học dữliệu,
và nhà nghiên cứu. Sựkết hợp giữa NumPy (xửlý mảng), SciPy (tính toán khoa học), và
Matplotlib (visualization) tạo nên một hệsinh thái mạnh mẽ, miễn phí và mã nguồn mở,
cạnh tranh với các phần mềm thương mại đắt tiền như MATLAB.
207

CHƯƠNG 9. Lời Giải Bài Tập
Phần này cung cấp lời giải chi tiết cho các bài tập trong từng chương của giáo trình.
Sinh viên nên tựgiải quyết bài tập trước khi tham khảo lời giải.
9.1
Chương 1: Biến, Toán tử, Kiểu dữliệu
9.1.1
Lời giải Bài tập 1
# Khai bao bien thong tin ca nhan
ten = "Nguyen Van A"
tuoi = 20
chieu_cao = 1.75
# met
can_nang = 68
# kg
# Tinh BMI = can_nang / (chieu_cao^2)

bmi = can_nang / (chieu_cao ** 2)
# In ket qua
print(f"Thong tin ca nhan:")
print(f"
Ho ten: {ten}")
print(f"
Tuoi: {tuoi}")
print(f"
Chieu cao: {chieu_cao} m")
print(f"
Can nang: {can_nang} kg")
print(f"
BMI: {bmi:.2f}")
# Danh gia BMI
if bmi < 18.5:
danh_gia = "Thieu can"
elif bmi < 25:
danh_gia = "Binh thuong"
elif bmi < 30:
danh_gia = "Thua can"
else:
danh_gia = "Beo phi"
print(f"
Danh gia: {danh_gia}")
9.1.2
Lời giải Bài tập 2
import math
# Hinh chu nhat
chieu_dai = 10
chieu_rong = 5
208

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
dien_tich_hcn = chieu_dai * chieu_rong
chu_vi_hcn = 2 * (chieu_dai + chieu_rong)
print("Hinh chu nhat:")
print(f"
Chieu dai: {chieu_dai}")
print(f"
Chieu rong: {chieu_rong}")
print(f"
Dien tich: {dien_tich_hcn}")
print(f"
Chu vi: {chu_vi_hcn}")

# Hinh tron
ban_kinh = 7
dien_tich_ht = math.pi * ban_kinh ** 2
chu_vi_ht = 2 * math.pi * ban_kinh
print(f"\nHinh tron:")
print(f"
Ban kinh: {ban_kinh}")
print(f"
Dien tich: {dien_tich_ht:.2f}")
print(f"
Chu vi: {chu_vi_ht:.2f}")
9.1.3
Lời giải Bài tập 3
# Nhap so nguyen
n = int(input("Nhap mot so nguyen: "))
# Kiem tra so chan duong
la_so_chan = (n % 2 == 0)
la_so_duong = (n > 0)
la_so_chan_duong = la_so_chan and la_so_duong
# In ket qua
print(f"So {n}:")
print(f"
La so chan: {la_so_chan}")
print(f"
La so duong: {la_so_duong}")
print(f"
La so chan duong: {la_so_chan_duong}")
# Kiem tra chi tiet
if la_so_chan_duong:
print(f"
=> {n} la so chan duong")
elif n > 0:
print(f"
=> {n} la so le duong")
elif la_so_chan:
print(f"
=> {n} la so chan khong duong")
209

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
else:
print(f"
=> {n} la so le khong duong")
9.1.4

Lời giải Bài tập 4
def celsius_to_fahrenheit(c):
return (c * 9/5) + 32
def celsius_to_kelvin(c):
return c + 273.15
def fahrenheit_to_celsius(f):
return (f - 32) * 5/9
def kelvin_to_celsius(k):
return k - 273.15
# Nhap nhiet do Celsius
celsius = float(input("Nhap nhiet do (Celsius): "))
# Chuyen doi
fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celsius_to_kelvin(celsius)
# In ket qua
print(f"\nChuyen doi nhiet do:")
print(f"
{celsius:.2f} do C")
print(f"
{fahrenheit:.2f} do F")
print(f"
{kelvin:.2f} K")
# Vi du nguoc lai
print(f"\nKiem tra chuyen doi nguoc:")
c_from_f = fahrenheit_to_celsius(fahrenheit)
c_from_k = kelvin_to_celsius(kelvin)
print(f"
Tu {fahrenheit:.2f} do F -> {c_from_f:.2f} do C")
print(f"
Tu {kelvin:.2f} K -> {c_from_k:.2f} do C")
9.1.5
Lời giải Bài tập 5
# Nhap chuoi
chuoi = input("Nhap mot chuoi: ")
# Thong ke co ban
210

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
so_ky_tu = len(chuoi)
so_chu_cai = sum(c.isalpha() for c in chuoi)
so_chu_so = sum(c.isdigit() for c in chuoi)
so_khoang_trang = chuoi.count(' ')
print(f"\nThong ke chuoi '{chuoi}':")
print(f"

So ky tu: {so_ky_tu}")
print(f"
So chu cai: {so_chu_cai}")
print(f"
So chu so: {so_chu_so}")
print(f"
So khoang trang: {so_khoang_trang}")
# Chuyen doi
print(f"\nChuyen doi:")
print(f"
Chu hoa: {chuoi.upper()}")
print(f"
Chu thuong: {chuoi.lower()}")
print(f"
Chu hoa dau: {chuoi.title()}")
# Kiem tra palindrome (doc xuoi nguoc giong nhau)
chuoi_sach = ''.join(c.lower() for c in chuoi if
c.isalnum())
,→
la_palindrome = chuoi_sach == chuoi_sach[::-1]
print(f"\n
La palindrome: {la_palindrome}")
# Vi du
if la_palindrome:
print(f"
'{chuoi}' doc xuoi nguoc giong nhau!")
9.2
Chương 2: Cấu trúc Dữliệu
9.2.1
Lời giải Bài tập 1
# Tao tuple sinh vien
sinh_vien = ("SV001", "Nguyen Van A", 8.5)
# In toan bo tuple
print("Thong tin sinh vien:", sinh_vien)
# Truy cap tung phan tu
print(f"Ma SV: {sinh_vien[0]}")
print(f"Ten: {sinh_vien[1]}")
print(f"Diem TB: {sinh_vien[2]}")
# Unpacking tuple
ma_sv, ten, diem = sinh_vien
211

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
print(f"\nSinh vien {ten} (Ma: {ma_sv}) co diem TB: {diem}")

9.2.2
Lời giải Bài tập 3
# Tao dictionary diem sinh vien
diem_sinh_vien = {
"SV001": {"ten": "Nguyen Van A", "diem": [8, 7.5, 9]},
"SV002": {"ten": "Tran Thi B", "diem": [7, 8.5, 8]},
"SV003": {"ten": "Le Van C", "diem": [9, 9.5, 8.5]}
}
# Truy cap thong tin
print("Thong tin SV001:", diem_sinh_vien["SV001"])
# Them sinh vien moi
diem_sinh_vien["SV004"] = {"ten": "Pham Thi D", "diem":
[8.5, 8, 9]}
,→
# Tinh diem trung binh
for ma_sv, thong_tin in diem_sinh_vien.items():
diem_tb = sum(thong_tin["diem"]) /
len(thong_tin["diem"])
,→
print(f"{thong_tin['ten']} (Ma: {ma_sv}): Diem TB =
{diem_tb:.2f}")
,→
# Xoa sinh vien
del diem_sinh_vien["SV004"]
print("\nSo sinh vien con lai:", len(diem_sinh_vien))
9.2.3
Lời giải Bài tập 5
# Hai danh sach mon hoc cua hai sinh vien
mon_hoc_A = {"Toan", "Ly", "Hoa", "Tin", "Anh"}
mon_hoc_B = {"Toan", "Van", "Hoa", "Su", "Anh"}
# Mon hoc chung (giao)
mon_chung = mon_hoc_A & mon_hoc_B
print("Mon hoc chung:", mon_chung)
# Mon hoc chi A hoc (hieu)
mon_chi_A = mon_hoc_A - mon_hoc_B
print("Mon chi A hoc:", mon_chi_A)
212

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
# Mon hoc chi B hoc
mon_chi_B = mon_hoc_B - mon_hoc_A
print("Mon chi B hoc:", mon_chi_B)
# Tat ca cac mon (hop)
tat_ca_mon = mon_hoc_A | mon_hoc_B

print("Tat ca cac mon:", tat_ca_mon)
# Mon khac nhau (symmetric difference)
mon_khac_nhau = mon_hoc_A ^ mon_hoc_B
print("Mon khac nhau:", mon_khac_nhau)
9.3
Chương 3: Nhập Xuất Dữliệu
9.3.1
Lời giải Bài tập 2
# Nhap hai so thuc
try:
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
# Tinh toan
tong = a + b
hieu = a - b
tich = a * b
# In ket qua
print(f"\nKet qua tinh toan:")
print(f"
{a} + {b} = {tong:.2f}")
print(f"
{a} - {b} = {hieu:.2f}")
print(f"
{a} * {b} = {tich:.2f}")
# Kiem tra chia cho 0
if b != 0:
thuong = a / b
print(f"
{a} / {b} = {thuong:.2f}")
else:
print(f"
{a} / {b} = Khong the chia cho 0!")
except ValueError:
print("Loi: Vui long nhap so hop le!")
213

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
9.3.2
Lời giải Bài tập 5
# Doc file va tinh toan
def tinh_toan_tu_file(ten_file):
try:
with open(ten_file, 'r', encoding='utf-8') as f:
# Doc tung dong va chuyen thanh so nguyen

so_nguyen = []
for dong in f:
dong = dong.strip()
if dong:
# Bo qua dong trong
so_nguyen.append(int(dong))
# Tinh toan
if len(so_nguyen) > 0:
tong = sum(so_nguyen)
trung_binh = tong / len(so_nguyen)
print(f"So luong so: {len(so_nguyen)}")
print(f"Tong: {tong}")
print(f"Trung binh: {trung_binh:.2f}")
print(f"So lon nhat: {max(so_nguyen)}")
print(f"So nho nhat: {min(so_nguyen)}")
else:
print("File rong!")
except FileNotFoundError:
print(f"Loi: Khong tim thay file '{ten_file}'")
except ValueError:
print("Loi: File chua du lieu khong hop le")
# Su dung
tinh_toan_tu_file('numbers.txt')
9.3.3
Lời giải Bài tập 8
def thong_ke_file(ten_file):
try:
with open(ten_file, 'r', encoding='utf-8') as f:
noi_dung = f.read()
dong = noi_dung.split('\n')
# Dem so dong
so_dong = len(dong)
214

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
# Dem so tu
tu = noi_dung.split()
so_tu = len(tu)
# Dem so ky tu (bao gom ca khoang trang)
so_ky_tu = len(noi_dung)
# Dem so ky tu (khong khoang trang)
so_ky_tu_khong_space = len(noi_dung.replace(' ',
'').replace('\n', ''))
,→

print(f"Thong ke file '{ten_file}':")
print(f"
So dong: {so_dong}")
print(f"
So tu: {so_tu}")
print(f"
So ky tu (co khoang trang):
{so_ky_tu}")
,→
print(f"
So ky tu (khong khoang trang):
{so_ky_tu_khong_space}")
,→
except FileNotFoundError:
print(f"Loi: Khong tim thay file '{ten_file}'")
# Su dung
thong_ke_file('document.txt')
9.4
Chương 4: Điều kiện và Vòng lặp
9.4.1
Lời giải Bài tập 1
def la_so_nguyen_to(n):
"""Kiem tra n co phai so nguyen to hay khong"""
if n < 2:
return False
if n == 2:
return True
if n % 2 == 0:
return False
# Kiem tra cac so le tu 3 den sqrt(n)
import math
for i in range(3, int(math.sqrt(n)) + 1, 2):
if n % i == 0:
return False
215

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
return True
# Test
n = int(input("Nhap so nguyen duong: "))
if la_so_nguyen_to(n):
print(f"{n} la so nguyen to")
else:
print(f"{n} khong phai so nguyen to")

# In cac so nguyen to tu 1 den 100
print("\nCac so nguyen to tu 1 den 100:")
so_nguyen_to = [i for i in range(2, 101) if
la_so_nguyen_to(i)]
,→
print(so_nguyen_to)
print(f"Tong cong co {len(so_nguyen_to)} so nguyen to")
9.4.2
Lời giải Bài tập 2
def in_tam_giac_so(n):
"""In tam giac so voi n dong"""
# Tam giac 1: Tang dan
print("Tam giac 1:")
for i in range(1, n + 1):
for j in range(1, i + 1):
print(j, end=" ")
print()
# Tam giac 2: Giam dan
print("\nTam giac 2:")
for i in range(n, 0, -1):
for j in range(1, i + 1):
print(j, end=" ")
print()
# Tam giac 3: Canh can
print("\nTam giac 3:")
for i in range(1, n + 1):
# In khoang trang
print(" " * (n - i), end="")
# In so
for j in range(1, i + 1):
print(j, end=" ")
print()
216

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
# Test
n = int(input("Nhap so dong: "))
in_tam_giac_so(n)
9.5
Chương 5: Hàm và Module
9.5.1
Lời giải Bài tập 1
def giai_thua(n):
"""Tinh n! (giai thua)"""

if n < 0:
return None
if n <= 1:
return 1
return n * giai_thua(n - 1)
def to_hop(n, k):
"""Tinh to hop C(n, k) = n! / (k! * (n-k)!)"""
if k < 0 or k > n:
return 0
return giai_thua(n) // (giai_thua(k) * giai_thua(n - k))
def fibonacci(n):
"""Tinh so Fibonacci thu n"""
if n <= 0:
return 0
if n == 1:
return 1
return fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci_iterative(n):
"""Tinh Fibonacci bang phuong phap lap (nhanh hon)"""
if n <= 0:
return 0
if n == 1:
return 1
a, b = 0, 1
for _ in range(2, n + 1):
a, b = b, a + b
return b
# Test
217

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
print("Giai thua:")
for i in range(6):
print(f"
{i}! = {giai_thua(i)}")
print("\nTo hop C(5, k):")
for k in range(6):
print(f"
C(5, {k}) = {to_hop(5, k)}")
print("\nDay Fibonacci (10 so dau):")
for i in range(10):
print(f"
F({i}) = {fibonacci_iterative(i)}")
9.5.2

Lời giải Bài tập 2
def dem_tu(chuoi):
"""Dem so tu trong chuoi"""
return len(chuoi.split())
def dao_nguoc_chuoi(chuoi):
"""Dao nguoc chuoi"""
return chuoi[::-1]
def dao_nguoc_tu(chuoi):
"""Dao nguoc tung tu trong chuoi"""
tu_list = chuoi.split()
tu_dao = [tu[::-1] for tu in tu_list]
return ' '.join(tu_dao)
def loai_bo_ky_tu_dac_biet(chuoi):
"""Chi giu lai chu cai, chu so va khoang trang"""
ket_qua = ''
for c in chuoi:
if c.isalnum() or c.isspace():
ket_qua += c
return ket_qua
def chuan_hoa_chuoi(chuoi):
"""Loai bo khoang trang thua va chuan hoa"""
return ' '.join(chuoi.split())
# Test
chuoi_test = "
Hoc
lap trinh
Python rat thu vi!
"
print(f"Chuoi goc: '{chuoi_test}'")
218

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
print(f"So tu: {dem_tu(chuoi_test)}")
print(f"Dao nguoc: '{dao_nguoc_chuoi(chuoi_test)}'")
print(f"Dao nguoc tu: '{dao_nguoc_tu(chuoi_test)}'")
print(f"Loai ky tu dac biet:
'{loai_bo_ky_tu_dac_biet(chuoi_test)}'")
,→
print(f"Chuan hoa: '{chuan_hoa_chuoi(chuoi_test)}'")
9.5.3
Lời giải Bài tập 3
def thong_ke_list(danh_sach):
"""Thong ke co ban cua list"""
if not danh_sach:

return None
return {
'min': min(danh_sach),
'max': max(danh_sach),
'sum': sum(danh_sach),
'mean': sum(danh_sach) / len(danh_sach),
'count': len(danh_sach)
}
def loc_chan(danh_sach):
"""Loc cac so chan"""
return [x for x in danh_sach if x % 2 == 0]
def loc_le(danh_sach):
"""Loc cac so le"""
return [x for x in danh_sach if x % 2 != 0]
def loc_duong(danh_sach):
"""Loc cac so duong"""
return [x for x in danh_sach if x > 0]
def sap_xep_tang(danh_sach):
"""Sap xep tang dan"""
return sorted(danh_sach)
def sap_xep_giam(danh_sach):
"""Sap xep giam dan"""
return sorted(danh_sach, reverse=True)
# Test
so_list = [5, -3, 8, 12, -7, 0, 15, 4, -1, 9]
219

CHƯƠNG 9. LỜI GIẢI BÀI TẬP
print("Danh sach goc:", so_list)
print("\nThong ke:")
stats = thong_ke_list(so_list)
for key, value in stats.items():
print(f"
{key}: {value}")
print(f"\nSo chan: {loc_chan(so_list)}")
print(f"So le: {loc_le(so_list)}")
print(f"So duong: {loc_duong(so_list)}")
print(f"Sap xep tang: {sap_xep_tang(so_list)}")
print(f"Sap xep giam: {sap_xep_giam(so_list)}")
9.5.4
Lời giải Bài tập 4
from functools import reduce
# Danh sach sinh vien
sinh_vien = [

{'ten': 'An', 'diem': 8.5},
{'ten': 'Binh', 'diem': 6.0},
{'ten': 'Cuong', 'diem': 7.5},
{'ten': 'Dung', 'diem': 9.0},
{'ten': 'Em', 'diem': 5.5}
]
# Map: Lay danh sach ten
ten_list = list(map(lambda sv: sv['ten'], sinh_vien))
print("Danh sach ten:", ten_list)
# Map: Tang diem them 0.5
diem_tang = list(map(lambda sv: {**sv, 'diem':
min(sv['diem'] + 0.5, 10)},
,→
sinh_vien))
print("\nDiem sau khi tang:")
for sv in diem_tang:
print(f"
{sv['ten']}: {sv['diem']}")
# Filter: Loc sinh vien dat (diem >= 7)
sv_dat = list(filter(lambda sv: sv['diem'] >= 7, sinh_vien))
print("\nSinh vien dat (diem >= 7):")
for sv in sv_dat:
print(f"
{sv['ten']}: {sv['diem']}")
220
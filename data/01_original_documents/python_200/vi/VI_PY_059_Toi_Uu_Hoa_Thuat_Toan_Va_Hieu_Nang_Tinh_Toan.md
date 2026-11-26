<!-- page: 1 -->
# VI_PY_059: Tối ưu hóa thời gian thực thi và tài nguyên bộ nhớ cho bài toán lớn

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Tối ưu hóa | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 237 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
return None
# Vo nghiem hoac vo so nghiem
return [-c / b]
# Phuong trinh bac nhat
delta = b**2 - 4*a*c
if delta < 0:
return []
# Vo nghiem thuc
elif delta == 0:
return [-b / (2*a)]
# Nghiem kep
else:
sqrt_delta = math.sqrt(delta)
x1 = (-b + sqrt_delta) / (2*a)
x2 = (-b - sqrt_delta) / (2*a)
return [x1, x2]
# Hang so
PI = math.pi
E = math.e
File: main.py (su dung module)
import math_utils
# Test cac ham
print("Kiem tra so nguyen to:")
for n in [7, 10, 17, 20]:
print(f"
{n}: {math_utils.la_so_nguyen_to(n)}")
print("\nUCLN va BCNN:")
a, b = 12, 18
print(f"
GCD({a}, {b}) = {math_utils.gcd(a, b)}")
print(f"
LCM({a}, {b}) = {math_utils.lcm(a, b)}")
print("\nGiai phuong trinh bac 2:")

<!-- page: 2 -->

# x^2 - 5x + 6 = 0
nghiem = math_utils.giai_phuong_trinh_bac_2(1, -5, 6)
print(f"
x^2 - 5x + 6 = 0: {nghiem}")
# 2x^2 + 3x - 5 = 0
nghiem = math_utils.giai_phuong_trinh_bac_2(2, 3, -5)
print(f"
2x^2 + 3x - 5 = 0: {nghiem}")
print(f"\nHang so: PI = {math_utils.PI:.4f}, E =
{math_utils.E:.4f}")
,→
222

<!-- page: 238 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
9.6
Chương 6: Lập trình Hướng Đối tượng
9.6.1
Lời giải Bài tập 1
class SinhVien:
"""Class quan ly thong tin sinh vien"""
def __init__(self, ma_sv, ho_ten, nam_sinh,
diem_list=None):
,→
self.ma_sv = ma_sv
self.ho_ten = ho_ten
self.nam_sinh = nam_sinh
self.diem_list = diem_list if diem_list else []
def them_diem(self, diem):
"""Them diem moi"""
if 0 <= diem <= 10:
self.diem_list.append(diem)
else:
print("Diem khong hop le!")
def tinh_diem_tb(self):
"""Tinh diem trung binh"""
if not self.diem_list:
return 0
return sum(self.diem_list) / len(self.diem_list)
def xep_loai(self):
"""Xep loai hoc luc"""
dtb = self.tinh_diem_tb()
if dtb >= 9.0:
return "Xuat sac"
elif dtb >= 8.0:

<!-- page: 3 -->

return "Gioi"
elif dtb >= 7.0:
return "Kha"
elif dtb >= 5.0:
return "Trung binh"
else:
return "Yeu"
def __str__(self):
"""String representation"""
dtb = self.tinh_diem_tb()
xl = self.xep_loai()
223

<!-- page: 239 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
return f"SV {self.ma_sv} - {self.ho_ten} - DTB:
{dtb:.2f} - {xl}"
,→
# Test
sv1 = SinhVien("SV001", "Nguyen Van A", 2005)
sv1.them_diem(8.5)
sv1.them_diem(7.0)
sv1.them_diem(9.0)
print(sv1)
sv2 = SinhVien("SV002", "Tran Thi B", 2004, [9.5, 9.0, 8.5])
print(sv2)
9.6.2
Lời giải Bài tập 2
import math
class Hinh:
"""Class co so cho cac hinh hoc"""
def dien_tich(self):
raise NotImplementedError
def chu_vi(self):
raise NotImplementedError
def __str__(self):
return f"{self.__class__.__name__} - DT:
{self.dien_tich():.2f}, CV: {self.chu_vi():.2f}"
,→
class HinhTron(Hinh):
def __init__(self, ban_kinh):
self.ban_kinh = ban_kinh
def dien_tich(self):
return math.pi * self.ban_kinh ** 2
def chu_vi(self):

<!-- page: 4 -->

return 2 * math.pi * self.ban_kinh
class HinhChuNhat(Hinh):
def __init__(self, chieu_dai, chieu_rong):
self.chieu_dai = chieu_dai
self.chieu_rong = chieu_rong
224

<!-- page: 240 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
def dien_tich(self):
return self.chieu_dai * self.chieu_rong
def chu_vi(self):
return 2 * (self.chieu_dai + self.chieu_rong)
class TamGiac(Hinh):
def __init__(self, a, b, c):
self.a = a
self.b = b
self.c = c
def dien_tich(self):
# Cong thuc Heron
p = (self.a + self.b + self.c) / 2
return math.sqrt(p * (p - self.a) * (p - self.b) *
(p - self.c))
,→
def chu_vi(self):
return self.a + self.b + self.c
# Test
hinh_list = [
HinhTron(5),
HinhChuNhat(10, 6),
TamGiac(3, 4, 5)
]
print("Danh sach cac hinh:")
for hinh in hinh_list:
print(f"
{hinh}")
# Tinh tong dien tich
tong_dt = sum(hinh.dien_tich() for hinh in hinh_list)
print(f"\nTong dien tich: {tong_dt:.2f}")
9.6.3
Lời giải Bài tập 3
from datetime import datetime
class TaiKhoan:
"""Class quan ly tai khoan ngan hang"""
225

<!-- page: 5 -->


<!-- page: 241 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
lai_suat_nam = 0.05
# Class variable: 5% per year
def __init__(self, so_tai_khoan, chu_tai_khoan,
so_du_ban_dau=0):
,→
self.so_tai_khoan = so_tai_khoan
self.chu_tai_khoan = chu_tai_khoan
self.__so_du = so_du_ban_dau
# Private attribute
self.lich_su = []
def nap_tien(self, so_tien):
"""Nap tien vao tai khoan"""
if so_tien > 0:
self.__so_du += so_tien
self._ghi_lich_su('Nap tien', so_tien)
print(f"Nap {so_tien:,.0f} VND thanh cong. So
du: {self.__so_du:,.0f}")
,→
else:
print("So tien khong hop le!")
def rut_tien(self, so_tien):
"""Rut tien tu tai khoan"""
if so_tien > 0:
if so_tien <= self.__so_du:
self.__so_du -= so_tien
self._ghi_lich_su('Rut tien', -so_tien)
print(f"Rut {so_tien:,.0f} VND thanh cong.
So du: {self.__so_du:,.0f}")
,→
else:
print("So du khong du!")
else:
print("So tien khong hop le!")
def chuyen_tien(self, tai_khoan_nhan, so_tien):
"""Chuyen tien den tai khoan khac"""
if so_tien > 0 and so_tien <= self.__so_du:
self.__so_du -= so_tien
tai_khoan_nhan.__so_du += so_tien
self._ghi_lich_su('Chuyen tien', -so_tien)
tai_khoan_nhan._ghi_lich_su('Nhan tien',
so_tien)
,→

<!-- page: 6 -->

print(f"Chuyen {so_tien:,.0f} VND thanh cong")
else:
print("Giao dich that bai!")
226

<!-- page: 242 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
def xem_so_du(self):
"""Xem so du tai khoan"""
return self.__so_du
def _ghi_lich_su(self, loai, so_tien):
"""Ghi lich su giao dich (protected method)"""
giao_dich = {
'thoi_gian': datetime.now().strftime("%Y-%m-%d
%H:%M:%S"),
,→
'loai': loai,
'so_tien': so_tien,
'so_du': self.__so_du
}
self.lich_su.append(giao_dich)
def in_lich_su(self):
"""In lich su giao dich"""
print(f"\nLich su giao dich -
{self.chu_tai_khoan}:")
,→
for gd in self.lich_su:
print(f"
{gd['thoi_gian']} | {gd['loai']}:
{gd['so_tien']:+,.0f} | So du:
{gd['so_du']:,.0f}")
,→
,→
def __str__(self):
return f"TK {self.so_tai_khoan} -
{self.chu_tai_khoan} - So du:
{self.__so_du:,.0f} VND"
,→
,→
# Test
tk1 = TaiKhoan("001", "Nguyen Van A", 1000000)
tk2 = TaiKhoan("002", "Tran Thi B", 500000)
print(tk1)
print(tk2)
tk1.nap_tien(500000)

<!-- page: 7 -->

tk1.rut_tien(200000)
tk1.chuyen_tien(tk2, 300000)
print(f"\n{tk1}")
print(tk2)
tk1.in_lich_su()
227

<!-- page: 243 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
9.7
Chương 7: NumPy trong Kỹthuật
9.7.1
Lời giải Bài tập 1
import numpy as np
# Tao cac loai mang
a = np.array([1, 2, 3, 4, 5])
print("Mang 1D:", a)
# Mang 2D
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMang 2D:\n", b)
# Mang zeros, ones
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
print("\nZeros:\n", zeros)
print("Ones:\n", ones)
# Mang ngau nhien
random = np.random.randint(0, 100, size=(3, 3))
print("\nRandom:\n", random)
# Thao tac
print("\nHinh dang:", b.shape)
print("Kich thuoc:", b.size)
print("Kieu du lieu:", b.dtype)
# Indexing va slicing
print("\nPhan tu [1,2]:", b[1, 2])
print("Hang thu 2:\n", b[1, :])
print("Cot thu 3:\n", b[:, 2])
# Thong ke
print("\nTong:", np.sum(b))
print("Trung binh:", np.mean(b))
print("Max:", np.max(b))
print("Min:", np.min(b))
228

<!-- page: 244 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP

<!-- page: 8 -->

9.7.2
Lời giải Bài tập 2
import numpy as np
# Tao hai ma tran
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Ma tran A:\n", A)
print("\nMa tran B:\n", B)
# Cong, tru
print("\nA + B:\n", A + B)
print("\nA - B:\n", A - B)
# Nhan phan tu (element-wise)
print("\nA * B (element-wise):\n", A * B)
# Nhan ma tran (matrix multiplication)
print("\nA @ B (matrix mult):\n", A @ B)
# Chuyen vi
print("\nChuyen vi A:\n", A.T)
# Dinh thuc (neu ma tran vuong)
if A.shape[0] == A.shape[1]:
det_A = np.linalg.det(A)
print(f"\nDet(A) = {det_A:.4f}")
# Ma tran nghich dao (neu ton tai)
try:
A_inv = np.linalg.inv(A)
print("\nMa tran nghich dao A:\n", A_inv)
# Kiem tra
print("\nKiem tra A * A_inv:\n", A @ A_inv)
except np.linalg.LinAlgError:
print("\nMa tran khong kha nghich")
# Tri rieng va vector rieng
C = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(C)
print("\nTri rieng:", eigenvalues)
print("Vector rieng:\n", eigenvectors)
229

<!-- page: 245 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
9.8
Chương 8: Visualization
9.8.1
Lời giải Bài tập 1
import matplotlib.pyplot as plt
import numpy as np
# Du lieu

<!-- page: 9 -->

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Tao figure
plt.figure(figsize=(10, 6))
# Ve do thi
plt.plot(x, y1, 'b-', label='sin(x)', linewidth=2)
plt.plot(x, y2, 'r--', label='cos(x)', linewidth=2)
# Tuy chinh
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Ham sin va cos', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
# Luu va hien thi
plt.savefig('bai_tap_plot.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
9.8.2
Lời giải Bài tập 2
import matplotlib.pyplot as plt
import numpy as np
# Tao du lieu ngau nhien phan phoi chuan
np.random.seed(42)
data1 = np.random.normal(100, 15, 1000)
# mean=100, std=15
data2 = np.random.normal(120, 20, 1000)
# mean=120, std=20
# Tao figure voi 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
# Histogram
230

<!-- page: 246 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
ax1.hist(data1, bins=30, alpha=0.7, color='blue',
edgecolor='black',
,→
label='Group 1')
ax1.hist(data2, bins=30, alpha=0.7, color='red',
edgecolor='black',
,→
label='Group 2')
ax1.set_xlabel('Gia tri', fontsize=12)

<!-- page: 10 -->

ax1.set_ylabel('Tan suat', fontsize=12)
ax1.set_title('Histogram', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)
# Density plot
ax2.hist(data1, bins=30, density=True, alpha=0.5,
color='blue',
,→
label='Group 1')
ax2.hist(data2, bins=30, density=True, alpha=0.5,
color='red',
,→
label='Group 2')
ax2.set_xlabel('Gia tri', fontsize=12)
ax2.set_ylabel('Mat do', fontsize=12)
ax2.set_title('Distribution Plot', fontsize=14,
fontweight='bold')
,→
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('bai_tap_histogram.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
9.9
Chương 9: SciPy
9.9.1
Lời giải Bài tập 1
import numpy as np
from scipy import integrate, optimize
import matplotlib.pyplot as plt
# Dinh nghia cac ham
def f1(x):
return x**2
def f2(x):
231

<!-- page: 247 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
return 2*x + 3
# Tim giao diem
def diff(x):
return f1(x) - f2(x)
# Su dung fsolve tim 2 nghiem

<!-- page: 11 -->

x_intersect = optimize.fsolve(diff, [-2, 4])
x1, x2 = sorted(x_intersect)
print(f"Giao diem: x1 = {x1:.4f}, x2 = {x2:.4f}")
# Tinh dien tich
# A = integral[x1, x2] (f2(x) - f1(x)) dx
area, error = integrate.quad(lambda x: f2(x) - f1(x), x1,
x2)
,→
print(f"Dien tich: {area:.4f}")
# Ve do thi
x = np.linspace(x1 - 1, x2 + 1, 500)
y1 = f1(x)
y2 = f2(x)
plt.figure(figsize=(10, 8))
plt.plot(x, y1, 'b-', label='y = x^2', linewidth=2)
plt.plot(x, y2, 'r-', label='y = 2x + 3', linewidth=2)
# To mau vung dien tich
x_fill = np.linspace(x1, x2, 100)
y1_fill = f1(x_fill)
y2_fill = f2(x_fill)
plt.fill_between(x_fill, y1_fill, y2_fill, alpha=0.3,
color='green',
,→
label=f'Dien tich = {area:.4f}')
# Danh dau giao diem
plt.plot([x1, x2], [f1(x1), f1(x2)], 'ko', markersize=8,
label='Giao diem')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Tinh dien tich hinh phang', fontsize=14,
fontweight='bold')
,→
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
232

<!-- page: 248 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.savefig('bai_tap_dien_tich.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
9.9.2

<!-- page: 12 -->

Lời giải Bài tập 4
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
# Du lieu nhiet do trung binh thang
thang = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
nhiet_do = np.array([17, 18, 21, 25, 29, 30, 30, 29, 28, 25,
22, 18])
,→
# Noi suy tuyen tinh
f_linear = interpolate.interp1d(thang, nhiet_do,
kind='linear')
,→
# Noi suy cubic
f_cubic = interpolate.interp1d(thang, nhiet_do,
kind='cubic')
,→
# Noi suy cubic spline
f_spline = interpolate.CubicSpline(thang, nhiet_do)
# Tao luoi chi tiet
thang_fine = np.linspace(1, 12, 365)
# Tinh nhiet do noi suy
nhiet_do_linear = f_linear(thang_fine)
nhiet_do_cubic = f_cubic(thang_fine)
nhiet_do_spline = f_spline(thang_fine)
# Ve do thi
plt.figure(figsize=(14, 8))
plt.plot(thang, nhiet_do, 'ko', markersize=8, label='Du lieu
thuc te')
,→
plt.plot(thang_fine, nhiet_do_linear, 'b-', linewidth=2,
label='Noi suy tuyen tinh')
233

<!-- page: 249 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
plt.plot(thang_fine, nhiet_do_cubic, 'r--', linewidth=2,
label='Noi suy cubic')
plt.plot(thang_fine, nhiet_do_spline, 'g-.', linewidth=2,
label='Cubic spline')
plt.xlabel('Thang', fontsize=12)
plt.ylabel('Nhiet do (do C)', fontsize=12)
plt.title('Noi suy du lieu nhiet do Ha Noi',
fontsize=14, fontweight='bold')
plt.legend(fontsize=11)

<!-- page: 13 -->

plt.grid(True, alpha=0.3)
plt.xticks(thang)
plt.savefig('bai_tap_noi_suy.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
# Tinh nhiet do ngay 15 cua moi thang
print("\nNhiet do uoc luong ngay 15:")
for i, t in enumerate(thang):
ngay = t + 0.5
# Giua thang (ngay 15)
if ngay <= 12:
temp_spline = f_spline(ngay)
print(f"
Thang {t}: {temp_spline:.2f} do C")
# Tinh dao ham (toc do thay doi nhiet do)
dao_ham = f_spline.derivative()
toc_do_thay_doi = dao_ham(thang)
print("\nToc do thay doi nhiet do (do C/thang):")
for i, t in enumerate(thang):
print(f"
Thang {t}: {toc_do_thay_doi[i]:.2f}")
9.10
Lưu ý chung
Khi giải các bài tập, sinh viên cần chú ý:
• Hiểu đềbài: Đọc kỹyêu cầu và xác định input/output cần thiết
• Phân tích bài toán: Chia nhỏbài toán thành các bước xửlý
• Chọn cấu trúc dữliệu phù hợp: List, tuple, dict, set, array...
• Xửlý ngoại lệ: Sửdụng try-except đểbắt lỗi
• Kiểm tra kết quả: Test với nhiều trường hợp khác nhau
• Tối ưu code: Sửdụng list comprehension, NumPy operations
• Comment code: Giải thích logic và thuật toán
234

<!-- page: 250 -->
CHƯƠNG 9. LỜI GIẢI BÀI TẬP
• Tuân thủPEP 8: Coding style chuẩn của Python
Sinh viên nên tựthực hiện các bài tập trước khi xem lời giải, sau đó so sánh và rút kinh
nghiệm. Có thểcó nhiều cách giải khác nhau cho cùng một bài toán, quan trọng là hiểu
logic và áp dụng đúng kiến thức đã học.
235
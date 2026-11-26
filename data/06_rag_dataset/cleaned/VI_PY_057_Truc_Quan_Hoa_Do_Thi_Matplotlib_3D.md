# VI_PY_057: Trực quan hóa không gian 3D: Biểu diễn mặt cong và biểu đồ nhiệt

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Matplotlib | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
from scipy.optimize import bisect
import numpy as np
import matplotlib.pyplot as plt
# Ví dụ11: Tìm nghiệm bằng phương pháp chia đôi
# Giải phương trình: x³ - 2x - 5 = 0
def f(x):
return x**3 - 2*x - 5
# Vẽđồthịđểxác định khoảng chứa nghiệm
x = np.linspace(0, 3, 1000)
y = f(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='f(x) = x³ - 2x -
5')
,→
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('ĐồthịHàm sốđểXác định Khoảng Chứa Nghiệm')
plt.legend()
plt.savefig('../Hinh_ve/ch9_bisection_plot.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
# Quan sát đồthị: f(2) = 8 - 4 - 5 = -1 < 0, f(3) = 27 - 6
- 5 = 16 > 0
,→
# Nghiệm nằm trong khoảng [2, 3]
root = bisect(f, 2, 3, xtol=1e-10)
print(f"Nghiệm tìm được: x = {root:.10f}")
print(f"Kiểm tra: f({root:.10f}) = {f(root):.2e}")
# So sánh với nghiệm chính xác
# Nghiệm chính xác: x ~= 2.0945514815

exact_root = 2.0945514815
print(f"Sai số: {abs(root - exact_root):.2e}")
Phương pháp chia đôi có ưu điểm là đơn giản, tin cậy và luôn hội tụnếu điều kiện ban
đầu thỏa mãn. Tuy nhiên, tốc độhội tụchậm là nhược điểm lớn khi cần độchính xác cao
hoặc giải nhiều phương trình.
192

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
8.5.3
Phương pháp Newton-Raphson và fsolve
Phương pháp Newton-Raphson (còn gọi là phương pháp tiếp tuyến) là một trong những
thuật toán mạnh mẽnhất đểtìm nghiệm phương trình phi tuyến. Khác với bisection chỉ
sửdụng giá trịhàm, Newton-Raphson khai thác thông tin đạo hàm đểhội tụnhanh hơn
nhiều.
Xuất phát từđiểm dựđoán xn, phương pháp xấp xỉhàm bằng tiếp tuyến tại điểm đó:
f(x) ≈f(xn) + f ′(xn)(x −xn)
Nghiệm của tiếp tuyến (cho f(x) = 0) cho điểm dựđoán mới:
xn+1 = xn −f(xn)
f ′(xn)
Phương pháp này có tốc độhội tụbậc hai (quadratic convergence): nếu xn gần nghiệm,
sai sốởbước tiếp theo tỷlệvới bình phương sai sốhiện tại: |xn+1 −x∗| ∝|xn −x∗|2.
Điều này có nghĩa sốchữsốchính xác tăng gấp đôi sau mỗi bước lặp khi gần nghiệm.
Tuy nhiên, phương pháp Newton có nhược điểm:
• Cần tính đạo hàm f ′(x), không phải lúc nào cũng dễdàng hoặc khảthi
• Có thểkhông hội tụnếu điểm xuất phát xa nghiệm
• Có thểgặp vấn đềkhi f ′(x) ≈0 (đạo hàm gần không)
Hàm optimize.fsolve của SciPy sửdụng thuật toán hybr (một biến thểcải tiến
của Powell’s hybrid method), kết hợp ưu điểm của Newton-Raphson với các kỹthuật tránh
phân kỳ. Nếu không cung cấp đạo hàm, fsolve tựđộng tính xấp xỉbằng sai phân hữu
hạn.
from scipy.optimize import fsolve, newton
# Ví dụ12: Sửdụng fsolve đểtìm nghiệm
# Giải phương trình: cos(x) = x
def equation(x):
return np.cos(x) - x
# Phương pháp 1: fsolve (không cần đạo hàm)
root_fsolve = fsolve(equation, 0.5)
# 0.5 là điểm xuất phát
print(f"Nghiệm (fsolve): x = {root_fsolve[0]:.10f}")
# Phương pháp 2: newton (cần đạo hàm, hội tụnhanh hơn)
def derivative(x):
193

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
return -np.sin(x) - 1
root_newton = newton(equation, 0.5, fprime=derivative)
print(f"Nghiệm (Newton): x = {root_newton:.10f}")
# Visualization
x = np.linspace(-1, 2, 1000)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, np.cos(x), 'b-', linewidth=2, label='y = cos(x)')
ax.plot(x, x, 'r-', linewidth=2, label='y = x')
ax.plot(root_fsolve[0], np.cos(root_fsolve[0]), 'go',
markersize=12, label=f'Nghiệm: x ~=
{root_fsolve[0]:.4f}')
,→
ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5,
alpha=0.3)
,→
ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5,
alpha=0.3)
,→
ax.grid(True, alpha=0.3)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Giao điểm cos(x) = x', fontsize=14,
fontweight='bold')
,→
ax.legend(fontsize=11)
plt.savefig('../Hinh_ve/ch9_fsolve.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
8.5.4
Giải HệPhương trình Phi tuyến
Trong thực tế, ta thường gặp hệnhiều phương trình phi tuyến đồng thời. Ví dụ, trong
kỹthuật điện, phân tích mạch phi tuyến yêu cầu giải hệphương trình Kirchhoff phi tuyến.
Trong hóa học, tính toán cân bằng phản ứng cũng dẫn đến hệphương trình phi tuyến.
Hàm fsolve có thểxửlý hệphương trình bằng cách mởrộng phương pháp Newton
lên không gian nhiều chiều. Thay vì đạo hàm, ta sửdụng ma trận Jacobian chứa các đạo
hàm riêng.
# Ví dụ13: Giải hệphương trình phi tuyến
# x² + y² = 4
# x - y² = 0
def system(vars):
x, y = vars
eq1 = x**2 + y**2 - 4
# x² + y² - 4 = 0

194

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
eq2 = x - y**2
# x - y² = 0
return [eq1, eq2]
# Giải với nhiều điểm xuất phát khác nhau đểtìm các nghiệm
khác nhau
,→
initial_guesses = [(1, 1), (-1, 1), (2, -1)]
print("Các nghiệm của hệphương trình:")
solutions = []
for guess in initial_guesses:
sol = fsolve(system, guess)
# Kiểm tra tính hợp lệ
residual = system(sol)
if np.allclose(residual, 0, atol=1e-6):
# Kiểm tra trùng lặp
is_duplicate = False
for existing_sol in solutions:
if np.allclose(sol, existing_sol, atol=1e-6):
is_duplicate = True
break
if not is_duplicate:
solutions.append(sol)
print(f"
x = {sol[0]:.6f}, y = {sol[1]:.6f}")
print(f"
Kiểm tra: x² + y² = {sol[0]**2 +
sol[1]**2:.6f}")
,→
print(f"
x - y² = {sol[0] -
sol[1]**2:.6f}")
,→
# Visualization
theta = np.linspace(0, 2*np.pi, 1000)
circle_x = 2 * np.cos(theta)
circle_y = 2 * np.sin(theta)
y_parabola = np.linspace(-2.5, 2.5, 1000)
x_parabola = y_parabola**2
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(circle_x, circle_y, 'b-', linewidth=2, label='x² +
y² = 4')

,→
ax.plot(x_parabola, y_parabola, 'r-', linewidth=2, label='x
= y²')
,→
for sol in solutions:
ax.plot(sol[0], sol[1], 'go', markersize=15)
195

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
ax.annotate(f'({sol[0]:.2f}, {sol[1]:.2f})',
xy=(sol[0], sol[1]), xytext=(sol[0]+0.3,
sol[1]+0.3),
,→
fontsize=11, fontweight='bold')
ax.set_xlim(-3, 5)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Nghiệm của HệPhương trình Phi tuyến',
fontsize=14, fontweight='bold')
ax.legend(fontsize=12)
plt.savefig('../Hinh_ve/ch9_system.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
8.5.5
Ứng dụng: Tính Điểm Cân bằng trong Phản ứng Hóa học
Trong hóa học, việc tính nồng độcác chất ởtrạng thái cân bằng thường dẫn đến hệ
phương trình phi tuyến từhằng sốcân bằng và định luật bảo toàn khối lượng.
# Ví dụ14: Cân bằng phản ứng: N2 + 3H2 <=> 2NH3
# Cho N2 = 1 mol, H2 = 3 mol ban đầu
# Hằng sốcân bằng K_c = 0.5 tại nhiệt độnhất định
def equilibrium(x):
"""
x: sốmol NH3 tạo thành
Tại cân bằng:
- N2: 1 - x/2
- H2: 3 - 3x/2
- NH3: x
K_c = [NH3]^2 / ([N2][H2]^3)

"""
K_c = 0.5
n_N2 = 1 - x / 2
n_H2 = 3 - 3 * x / 2
n_NH3 = x
# Điều kiện vật lý: tất cảnồng độphải dương
196

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
if n_N2 <= 0 or n_H2 <= 0 or n_NH3 <= 0:
return 1e10
# Trảvềgiá trịlớn nếu không hợp lý
# Phương trình cân bằng (giảsửthểtích V = 1 L)
return (n_NH3**2) / (n_N2 * n_H2**3) - K_c
# Tìm nghiệm
x_equilibrium = fsolve(equilibrium, 0.5)[0]
# Bắt đầu từ
0.5 mol
,→
n_N2_eq = 1 - x_equilibrium / 2
n_H2_eq = 3 - 3 * x_equilibrium / 2
n_NH3_eq = x_equilibrium
print("Trạng thái cân bằng:")
print(f"
N2: {n_N2_eq:.4f} mol")
print(f"
H2: {n_H2_eq:.4f} mol")
print(f"
NH3: {n_NH3_eq:.4f} mol")
print(f"Kiểm tra K_c: {(n_NH3_eq**2) / (n_N2_eq *
n_H2_eq**3):.4f}")
,→
8.6
Nội suy Dữliệu với SciPy
Nội suy (interpolation) là kỹthuật ước lượng giá trịcủa hàm sốtại các điểm trung gian
dựa trên tập hợp các điểm dữliệu đã biết. Trong thực tếkhoa học và kỹthuật, dữliệu
thường được đo đạc hoặc tính toán tại các điểm rời rạc, nhưng ta cần giá trịtại các điểm
khác. Ví dụ: nhiệt độđược đo mỗi giờnhưng cần biết nhiệt độvào lúc 10:30, hoặc tính
toán sốliệu chỉcó tại 10 điểm nhưng cần vẽđường cong mượt.
8.6.1
Cơ sởLý thuyết Nội suy
Cho tập điểm dữliệu (xi, yi) với i = 0, 1, ..., n, ta muốn tìm hàm f(x) sao cho f(xi) =
yi với mọi i, và có thểtính f(x) tại bất kỳx nào trong khoảng [x0, xn]. Hàm f(x) được
gọi là hàm nội suy.

Các yêu cầu đối với hàm nội suy:
• Chính xác: Phải đi qua tất cảcác điểm dữliệu đã cho
• Mịn: Đường cong nên liên tục và có đạo hàm liên tục (tránh gãy khúc)
• Ổn định: Không dao động mạnh giữa các điểm dữliệu
• Hiệu quả: Tính toán nhanh, đặc biệt khi có nhiều điểm cần nội suy
197

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
8.6.2
Nội suy Tuyến tính
Phương pháp đơn giản nhất là nối các điểm liên tiếp bằng đoạn thẳng. Trong mỗi đoạn
[xi, xi+1], hàm nội suy là:
f(x) = yi + yi+1 −yi
xi+1 −xi
(x −xi)
Nội suy tuyến tính có ưu điểm đơn giản, nhanh, và ổn định, nhưng hạn chếlà đường
cong không trơn (có góc tại các điểm dữliệu), không phù hợp khi cần đạo hàm.
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
# Ví dụ15: Nội suy tuyến tính
# Dữliệu nhiệt độđo được trong ngày
time_hours = np.array([0, 6, 12, 18, 24])
# giờ
temperature = np.array([15, 12, 25, 22, 16])
# °C
# Tạo hàm nội suy tuyến tính
f_linear = interp1d(time_hours, temperature, kind='linear')
# Tính nhiệt độtại các thời điểm chi tiết
time_detailed = np.linspace(0, 24, 1000)
temp_interpolated = f_linear(time_detailed)
# Visualization
plt.figure(figsize=(12, 6))
plt.plot(time_hours, temperature, 'ro', markersize=10,
label='Dữliệu đo đạc', zorder=3)
plt.plot(time_detailed, temp_interpolated, 'b-',
linewidth=2,
,→
label='Nội suy tuyến tính')
plt.grid(True, alpha=0.3)
plt.xlabel('Thời gian (giờ)', fontsize=12)
plt.ylabel('Nhiệt độ(°C)', fontsize=12)
plt.title('Nội suy Tuyến tính Dữliệu Nhiệt độ',
fontsize=14, fontweight='bold')

plt.legend(fontsize=11)
plt.xlim(0, 24)
plt.savefig('../Hinh_ve/ch9_linear_interp.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
198

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
# Tính nhiệt độtại thời điểm cụthể
time_query = 10.5
temp_at_query = f_linear(time_query)
print(f"Nhiệt độước lượng lúc {time_query}h:
{temp_at_query:.2f}°C")
,→
8.6.3
Nội suy Đa thức và Spline
Nội suy đa thức sửdụng một đa thức bậc n đi qua n + 1 điểm. Tuy nhiên, khi sốđiểm
nhiều, đa thức bậc cao dễgây ra hiện tượng Runge (dao động lớn ởbiên), làm hàm nội
suy không ổn định.
Giải pháp tốt hơn là sửdụng spline (đường cong trơn từng khúc). Spline là đường cong
ghép nối từnhiều đa thức bậc thấp (thường bậc 3 - cubic spline), mỗi đa thức áp dụng cho
một đoạn, với điều kiện liên tục của hàm và các đạo hàm tại điểm nối. Cubic spline đảm
bảo hàm, đạo hàm bậc nhất và bậc hai liên tục, cho đường cong mượt mà và tựnhiên.
from scipy.interpolate import interp1d, CubicSpline
# Ví dụ16: So sánh các phương pháp nội suy
# Hàm Runge: f(x) = 1/(1 + 25x²) - ví dụkinh điển vềvấn đề
của nội suy đa thức
,→
x_data = np.linspace(-1, 1, 9)
# 9 điểm dữliệu
y_data = 1 / (1 + 25 * x_data**2)
# Tạo các hàm nội suy
f_linear = interp1d(x_data, y_data, kind='linear')
f_quadratic = interp1d(x_data, y_data, kind='quadratic')
f_cubic = interp1d(x_data, y_data, kind='cubic')
f_spline = CubicSpline(x_data, y_data)
# Điểm chi tiết đểvẽ
x_plot = np.linspace(-1, 1, 1000)
y_exact = 1 / (1 + 25 * x_plot**2)
# So sánh
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
methods = [
('Linear', f_linear, axes[0, 0]),

('Quadratic', f_quadratic, axes[0, 1]),
('Cubic', f_cubic, axes[1, 0]),
('Cubic Spline', f_spline, axes[1, 1])
199

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
]
for name, f_interp, ax in methods:
y_interp = f_interp(x_plot)
ax.plot(x_plot, y_exact, 'g--', linewidth=2, label='Hàm
gốc', alpha=0.7)
,→
ax.plot(x_plot, y_interp, 'b-', linewidth=2, label=f'Nội
suy {name}')
,→
ax.plot(x_data, y_data, 'ro', markersize=8, label='Điểm
dữliệu', zorder=3)
,→
ax.set_title(f'{name} Interpolation', fontsize=13,
fontweight='bold')
,→
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
# Tính sai sốtrung bình
error = np.mean(np.abs(y_interp - y_exact))
ax.text(0.05, 0.95, f'Sai sốTB: {error:.4f}',
transform=ax.transAxes, verticalalignment='top',
bbox=dict(boxstyle='round', facecolor='wheat',
alpha=0.5),
,→
fontsize=10)
plt.tight_layout()
plt.savefig('../Hinh_ve/ch9_interp_comparison.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Từví dụtrên, ta thấy cubic spline cho kết quảtốt nhất: đường cong mịn và sai sốthấp.
Đây là phương pháp nội suy phổbiến nhất trong thực tếkỹthuật và khoa học.
8.6.4
Nội suy Hai chiều
Khi dữliệu phụthuộc hai biến độc lập, chẳng hạn nhiệt độtheo tọa độđịa lý (kinh độ,
vĩ độ) hoặc độcao địa hình trên bản đồ, ta cần nội suy hai chiều.

from scipy.interpolate import interp2d, RectBivariateSpline
# Ví dụ17: Nội suy 2D - Bản đồnhiệt độ
# Dữliệu nhiệt độtại các điểm lưới
200

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
x_grid = np.array([0, 1, 2, 3, 4])
# Kinh độ
y_grid = np.array([0, 1, 2, 3])
# Vĩ độ
# Ma trận nhiệt độ(độC)
temperature_data = np.array([
[20, 21, 22, 23, 24],
[21, 22, 24, 25, 26],
[22, 24, 26, 27, 28],
[21, 23, 25, 26, 27]
])
# Tạo hàm nội suy 2D
f_2d = RectBivariateSpline(y_grid, x_grid, temperature_data)
# Lưới chi tiết đểvẽcontour map
x_fine = np.linspace(0, 4, 100)
y_fine = np.linspace(0, 3, 100)
X_fine, Y_fine = np.meshgrid(x_fine, y_fine)
Z_fine = f_2d(y_fine, x_fine)
# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
# Dữliệu gốc
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
c1 = ax1.contourf(X_grid, Y_grid, temperature_data,
levels=15, cmap='RdYlBu_r')
,→
ax1.plot(X_grid, Y_grid, 'ko', markersize=8)
ax1.set_title('Dữliệu Nhiệt độGốc (5×4 điểm)',
fontsize=13, fontweight='bold')
ax1.set_xlabel('Kinh độ', fontsize=11)
ax1.set_ylabel('Vĩ độ', fontsize=11)
plt.colorbar(c1, ax=ax1, label='Nhiệt độ(°C)')
# Sau nội suy
c2 = ax2.contourf(X_fine, Y_fine, Z_fine, levels=50,
cmap='RdYlBu_r')
,→
ax2.plot(X_grid, Y_grid, 'ko', markersize=6, label='Điểm
đo')
,→

ax2.set_title('Bản đồNhiệt độsau Nội suy (100×100 điểm)',
fontsize=13, fontweight='bold')
ax2.set_xlabel('Kinh độ', fontsize=11)
ax2.set_ylabel('Vĩ độ', fontsize=11)
ax2.legend(fontsize=10)
201

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
plt.colorbar(c2, ax=ax2, label='Nhiệt độ(°C)')
plt.tight_layout()
plt.savefig('../Hinh_ve/ch9_2d_interp.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
# Tính nhiệt độtại điểm cụthể
lon, lat = 2.5, 1.5
temp_at_point = f_2d(lat, lon)[0, 0]
print(f"Nhiệt độước lượng tại ({lon}, {lat}):
{temp_at_point:.2f}°C")
,→
8.6.5
Ứng dụng: Xửlý Dữliệu Thiếu
Trong phân tích dữliệu thực tế, thường gặp tình huống dữliệu bịthiếu do lỗi cảm biến,
mất kết nối, hoặc chi phí đo đạc. Nội suy là phương pháp phổbiến đểđiền (impute) các
giá trịthiếu.
# Ví dụ18: Xửlý dữliệu cảm biến bịthiếu
# Dữliệu áp suất theo thời gian, một sốđiểm bịmất
np.random.seed(42)
time_full = np.arange(0, 24, 0.5)
# Đo mỗi 30 phút
pressure_full = 1013 + 5 * np.sin(2 * np.pi * time_full /
24) + \
,→
np.random.normal(0, 0.5, len(time_full))
# Giảlập mất dữliệu (30% điểm)
missing_indices = np.random.choice(len(time_full),
size=int(0.3 *
len(time_full)),
,→
replace=False)
time_measured = np.delete(time_full, missing_indices)
pressure_measured = np.delete(pressure_full,
missing_indices)
,→

# Nội suy đểkhôi phục
f_recover = CubicSpline(time_measured, pressure_measured)
pressure_recovered = f_recover(time_full)
# Visualization
plt.figure(figsize=(14, 6))
plt.plot(time_full, pressure_full, 'g-', linewidth=2,
202

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
label='Dữliệu đầy đủ(ground truth)', alpha=0.5)
plt.plot(time_measured, pressure_measured, 'ro',
markersize=6,
,→
label=f'Dữliệu đo được ({len(time_measured)}
điểm)', zorder=3)
,→
plt.plot(time_full, pressure_recovered, 'b--', linewidth=2,
label='Dữliệu sau khôi phục (nội suy)')
plt.xlabel('Thời gian (giờ)', fontsize=12)
plt.ylabel('Áp suất (hPa)', fontsize=12)
plt.title('Khôi phục Dữliệu Thiếu bằng Nội suy',
fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.savefig('../Hinh_ve/ch9_missing_data.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
# Đánh giá chất lượng khôi phục
mse = np.mean((pressure_recovered - pressure_full)**2)
print(f"Mean Squared Error: {mse:.4f} hPa²")
print(f"Root Mean Squared Error: {np.sqrt(mse):.4f} hPa")
Kết quảcho thấy cubic spline khôi phục dữliệu với độchính xác cao, sai sốtrung bình
chỉkhoảng 0.5-1 hPa so với dữliệu thực. Phương pháp này đặc biệt hữu ích trong xửlý
dữliệu chuỗi thời gian từcác cảm biến IoT, trạm khí tượng, hoặc thiết bịy tế.
8.7
Bài tập Thực hành
Bài tập 1: Tích phân Ứng dụng Tính diện tích hình phẳng giới hạn bởi các đường:
• y = x2
• y = 2x + 3
Yêu cầu:
1. Tìm tọa độgiao điểm bằng fsolve
2. Tính diện tích bằng tích phân
R x2

x1 (ftrên(x) −fdưới(x))dx
3. Vẽđồthịminh họa và tô màu vùng diện tích
Bài tập 2: Giải ODE - Mạch RC Mạch điện RC được mô tảbởi phương trình:
RC dVC
dt + VC = Vin(t)
Với R = 1000 Ω, C = 10−6 F, và điện áp đầu vào là sóng vuông có biên độ5V, chu kỳ
10ms.
203

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
1. Viết hàm mô tảODE
2. Giải phương trình với VC(0) = 0 trên khoảng 50ms
3. VẽđồthịVin(t) và VC(t) trên cùng một figure
4. Nhận xét vềquá trình nạp và xảcủa tụđiện
Bài tập 3: Tìm Nghiệm - Phương trình Kepler Phương trình Kepler trong cơ học
thiên thể:
M = E −e sin(E)
trong đó M là góc lệch tâm trung bình (mean anomaly), E là góc lệch tâm (eccentric
anomaly), và e là độlệch tâm quỹđạo.
Cho M = π/4 và e = 0.3:
1. Giải phương trình đểtìm E bằng phương pháp chia đôi trong khoảng [0, 2π]
2. Giải bằng fsolve với điểm xuất phát E0 = M
3. So sánh tốc độhội tụvà sốbước lặp của hai phương pháp
Bài tập 4: Nội suy - Dữliệu Nhiệt độCho dữliệu nhiệt độtrung bình tháng tại Hà
Nội (°C):
Tháng
1
2
3
4
5
6
7
8
9
10
11
12
Nhiệt độ
17
18
21
25
29

30
30
29
28
25
22
18
1. Nội suy tuyến tính, cubic, và cubic spline
2. Tính nhiệt độước lượng cho ngày 15 của mỗi tháng (tháng i = ngày thứ30i + 15
trong năm)
3. Vẽvà so sánh ba phương pháp trên cùng một đồthị
4. Tính đạo hàm của nhiệt độ(tốc độthay đổi nhiệt độ) bằng cubic spline
Bài tập 5: HệODE - Con lắc Kép Con lắc kép được mô tảbởi hệphương trình (giả
sửm1 = m2 = m, l1 = l2 = l):
¨θ1 = −g(2m1 + m2) sin θ1 −m2g sin(θ1 −2θ2)
l1(2m1 + m2 −m2 cos(2θ1 −2θ2))
−2 sin(θ1 −θ2)m2( ˙θ2
2l2 + ˙θ2
1l1 cos(θ1 −θ2))
l1(2m1 + m2 −m2 cos(2θ1 −2θ2))
¨θ2 = (phương trình tương tự)
1. Chuyển vềhệbậc nhất với 4 biến: [θ1, ω1, θ2, ω2]
2. Giải với điều kiện ban đầu: θ1 = 90, θ2 = −90, ω1 = ω2 = 0
3. Vẽquỹđạo của hai khối nặng trong không gian 2D
4. Vẽbiểu đồnăng lượng theo thời gian đểkiểm tra bảo toàn năng lượng
204

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
Bài tập 6: Tích phân Kép - Khối lượng Vật thểMột tấm kim loại hình tròn bán kính
R = 0.1 m có mật độkhối lượng phụthuộc vào khoảng cách đến tâm:
ρ(r) = ρ0(1 + αr2)
với ρ0 = 7850 kg/m3 (thép), α = 10 m−2, độdày đồng đều h = 0.01 m.
1. Thiết lập tích phân kép trong tọa độcực: M =
RR
ρ(r)h dA
2. Tính khối lượng bằng dblquad
3. Tính vịtrí trọng tâm (xc, yc)
4. So sánh với trường hợp mật độđều
Bài tập 7: Giải HệPhương trình - Thiết kếCầu Trong phân tích kết cấu dàn đơn
giản, ta có hệphương trình cân bằng lực. Cho dàn 3 thanh với các góc θ1 = 30, θ2 = 45,
θ3 = 60, chịu tải trọng đứng P = 1000 N:
T1 cos θ1 + T2 cos θ2 + T3 cos θ3 = 0
T1 sin θ1 + T2 sin θ2 + T3 sin θ3 = P
l1T1 + l2T2 −l3T3 = 0

với l1 = l2 = l3 = 1 m.
1. Giải hệphương trình đểtìm lực trong các thanh (T1, T2, T3)
2. Xác định thanh nào chịu kéo (dương), thanh nào chịu nén (âm)
3. Khảo sát sựthay đổi lực khi P biến thiên từ0 đến 2000 N
Bài tập 8: Nội suy 2D - Bản đồĐịa hình Cho độcao (m) tại 9 điểm trên lưới (x, y):
y \x
0
50
100
0
100
120
140
50
110
150
170
100
105
130
145
1. Nội suy 2D đểtạo lưới chi tiết 100 × 100 điểm
2. Vẽbản đồcontour và bản đồ3D
3. Tính gradient (độdốc) tại mỗi điểm
4. Xác định điểm có độdốc lớn nhất (nguy hiểm cho xây dựng)
Bài tập 9: Mô phỏng Động lực học - HệLò xo - Khối lượng Hệhai lò xo nối tiếp
với hai khối lượng:
m1¨x1 = −k1x1 + k2(x2 −x1) −c1 ˙x1
m2¨x2 = −k2(x2 −x1) −c2 ˙x2 + F(t)
205
# VI_PY_053: NumPy: Các phép toán đại số tuyến tính, định thức và nghịch đảo ma trận

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: NumPy | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
# Tích chập
filtered = np.convolve(signal, kernel, mode='same')
print("Tin hieu goc:", signal)
print("Tin hieu sau loc:", filtered)
# Kernel phát hiện cạnh
edge_kernel = np.array([1, 0, -1])
edges = np.convolve(signal, edge_kernel, mode='same')
print("Phat hien canh:", edges)
Kết quả:
Tin hieu goc: [1 2 3 4 5 4 3 2 1]
Tin hieu sau loc: [1.
2.
3.
4.
4.33
3.67
3.
2.
1.
Phat hien canh: [ 1.
2.
2.
1.
0. -1. -2. -2. -1.]
c, Biến đổi FFT (Fast Fourier Transform)
FFT là công cụmạnh mẽđểphân tích tín hiệu trong miền tần số.
# Tạo tín hiệu tổng hợp (2 tần số)
sampling_rate = 1000
# Hz
t = np.linspace(0, 1, sampling_rate)
# Tín hiệu = 50Hz + 120Hz
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi
* 120 * t)

,→
# Biến đổi FFT
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(signal), 1/sampling_rate)
# Lấy biên độ(magnitude)
magnitude = np.abs(fft_result)
# Chỉlấy nửa đầu (tần sốdương)
half = len(signal) // 2
print("Tan so (10 diem dau):", fft_freq[:10])
print("Bien do (10 diem dau):", magnitude[:10])
# Tìm tần sốcó biên độlớn nhất
dominant_freq_idx = np.argmax(magnitude[:half])
dominant_freq = fft_freq[dominant_freq_idx]
print(f"\nTan so chinh: {dominant_freq} Hz")
137

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
6.6.2
Xửlý dữliệu cảm biến
a, Làm sạch dữliệu nhiệt độ
# Dữliệu nhiệt độtừcảm biến (có lỗi)
temperatures = np.array([
22.5, 23.1, 22.8, 150.0, 23.4, 22.9, -10.0,
23.2, 24.1, 22.7, 200.0, 23.5, 22.8
])
print("Du lieu goc:", temperatures)
# Phát hiện outliers (ngoài khoảng hợp lệ)
valid_range = (0, 50)
outliers = (temperatures < valid_range[0]) | (temperatures >
valid_range[1])
,→
print("Outliers:", temperatures[outliers])
# Thay thếoutliers bằng median của dữliệu hợp lệ
valid_data = temperatures[~outliers]
median_temp = np.median(valid_data)
temperatures_clean = temperatures.copy()
temperatures_clean[outliers] = median_temp
print("Du lieu sau khi lam sach:", temperatures_clean)
print("Trung binh:", np.mean(temperatures_clean))
print("Do lech chuan:", np.std(temperatures_clean))
Kết quả:
Du lieu goc: [ 22.5
23.1
22.8 150.

... 200.
23.5
22.8]
Outliers: [150.
-10.
200. ]
Du lieu sau khi lam sach: [22.5 23.1 22.8 23.
23.4 22.9 23.
23.2 24.1 2
b, Tính trung bình trượt (Moving Average)
# Dữliệu đo dao động
measurements = np.array([
100, 102, 98, 105, 99, 101, 103, 97, 104, 100,
102, 98, 106, 99, 101, 103, 98, 104, 101, 102
])
# Trung bình trượt cửa sổ5
window = 5
smoothed = np.convolve(measurements,
np.ones(window)/window,
138

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
mode='valid')
print("Do dai du lieu goc:", len(measurements))
print("Do dai sau khi lam muot:", len(smoothed))
print("Du lieu goc (10 diem):", measurements[:10])
print("Du lieu lam muot (10 diem):", smoothed[:10])
6.6.3
Tính toán ma trận cho kết cấu
a, Phân tích khung phẳng
# Ma trận độcứng đơn giản cho hệlò xo
# k1 = 100 N/m, k2 = 200 N/m, k3 = 150 N/m
# Hệ3 lò xo nối tiếp-song song
K = np.array([[300, -200, 0],
[-200, 350, -150],
[0, -150, 150]])
print("Ma tran do cung K:")
print(K)
# Vector lực
F = np.array([100, 0, 0])
# N
# Giải hệ: K * u = F đểtìm chuyển vịu
u = np.linalg.solve(K, F)
print("\nChuyen vi (mm):", u)

# Tính lực phản lực
reactions = K @ u
print("Luc phan luc:", reactions)
b, Tính ứng suất trong vật liệu
# Ma trận biến dạng (strain tensor)
strain = np.array([[0.001, 0.0002, 0],
[0.0002, 0.0015, 0],
[0, 0, 0.0008]])
# Hệsốđàn hồi (đơn giản hóa - vật liệu đẳng hướng)
E = 200e9
# Pa (thép)
nu = 0.3
# HệsốPoisson
139

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
# Ma trận độcứng (simplified)
D = E / (1 - nu**2) * np.array([
[1, nu, 0],
[nu, 1, 0],
[0, 0, (1-nu)/2]
])
# Tính ứng suất (chỉtính trên mặt phẳng)
stress_2d = D @ strain[:2, :2].flatten()[:3]
print("Ung suat (Pa):", stress_2d)
print("Ung suat (MPa):", stress_2d / 1e6)
6.6.4
Mô phỏng và tính toán số
a, Mô phỏng Monte Carlo
# Ước lượng giá trịpi bằng phương pháp Monte Carlo
n_points = 100000
# Tạo điểm ngẫu nhiên trong hình vuông [-1, 1] x [-1, 1]
x = np.random.uniform(-1, 1, n_points)
y = np.random.uniform(-1, 1, n_points)
# Tính khoảng cách đến tâm
distances = np.sqrt(x**2 + y**2)
# Đếm điểm trong hình tròn bán kính 1
inside_circle = np.sum(distances <= 1)
# Ước lượng pi
pi_estimate = 4 * inside_circle / n_points
print(f"Uoc luong pi: {pi_estimate}")
print(f"Sai so: {abs(pi_estimate - np.pi)}")
b, Tính tích phân bằng phương pháp hình thang
# Tính tích phân của f(x) = x^2 từ0 đến 1

# Kết quảchính xác: 1/3 ~= 0.333...
def f(x):
return x**2
# Tạo lưới điểm
n = 1000
140

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
x = np.linspace(0, 1, n)
y = f(x)
# Phương pháp hình thang
integral = np.trapz(y, x)
print(f"Tich phan: {integral}")
print(f"Sai so: {abs(integral - 1/3)}")
# So sánh với sốđiểm khác nhau
for n in [10, 100, 1000, 10000]:
x = np.linspace(0, 1, n)
y = f(x)
result = np.trapz(y, x)
error = abs(result - 1/3)
print(f"n={n:5d}: {result:.10f}, sai so: {error:.2e}")
6.6.5
Xửlý ma trận hình ảnh
Mặc dù xửlý ảnh thường dùng OpenCV hoặc PIL, NumPy vẫn là nền tảng cho các
thao tác cơ bản.
# Tạo ảnh grayscale mô phỏng (8x8)
image = np.random.randint(0, 256, (8, 8), dtype=np.uint8)
print("Anh goc:")
print(image)
# Lật ảnh theo chiều dọc
flipped_v = np.flipud(image)
print("\nLat doc:")
print(flipped_v)
# Lật ảnh theo chiều ngang
flipped_h = np.fliplr(image)
print("\nLat ngang:")
print(flipped_h)
# Xoay ảnh 90 độ
rotated = np.rot90(image)
print("\nXoay 90 do:")
print(rotated)
# Ngưỡng hóa (thresholding)
threshold = 128
binary = (image > threshold).astype(np.uint8) * 255

141

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
print("\nAnh nhi phan:")
print(binary)
6.6.6
Phân tích thống kê dữliệu thực nghiệm
# Dữliệu đo cường độbê tông (MPa)
concrete_strength = np.array([
28.5, 29.1, 27.8, 28.9, 29.5, 28.2, 29.8,
28.0, 29.3, 28.7, 29.0, 28.4, 29.6, 28.8
])
print("So mau:", len(concrete_strength))
print("Trung binh:", np.mean(concrete_strength))
print("Trung vi:", np.median(concrete_strength))
print("Do lech chuan:", np.std(concrete_strength))
print("Phuong sai:", np.var(concrete_strength))
print("Min:", np.min(concrete_strength))
print("Max:", np.max(concrete_strength))
# Tính khoảng tin cậy 95% (giảđịnh phân phối chuẩn)
from scipy import stats
confidence = 0.95
n = len(concrete_strength)
mean = np.mean(concrete_strength)
std_err = stats.sem(concrete_strength)
ci = stats.t.interval(confidence, n-1, loc=mean,
scale=std_err)
,→
print(f"\nKhoang tin cay 95%: [{ci[0]:.2f}, {ci[1]:.2f}]")
# Phân vị(quartiles)
q1, q2, q3 = np.percentile(concrete_strength, [25, 50, 75])
print(f"\nQ1: {q1}, Q2: {q2}, Q3: {q3}")
print(f"IQR (Interquartile Range): {q3 - q1}")
6.6.7
Hồi quy tuyến tính
# Dữliệu: Quan hệgiữa nhiệt độvà điện trở
temperature = np.array([20, 30, 40, 50, 60, 70, 80])
# °C
resistance = np.array([100.2, 103.5, 107.1, 110.8,
114.2, 117.9, 121.5])
# Ohm
# Tạo ma trận cho hồi quy: [1, T]
142

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
X = np.column_stack([np.ones(len(temperature)),
temperature])
,→
y = resistance
# Giải phương trình chuẩn: (X^T X) beta = X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"He so hoi quy: R = {beta[0]:.2f} + {beta[1]:.4f} *
T")
,→
# Dựđoán
T_new = 55
R_pred = beta[0] + beta[1] * T_new
print(f"\nDu doan dien tro tai {T_new}°C: {R_pred:.2f} Ohm")
# Tính R²
y_pred = X @ beta
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R²: {r_squared:.4f}")
Kết quảmẫu:
He so hoi quy: R = 96.54 + 0.3127 * T
Du doan dien tro tai 55°C: 113.74 Ohm
R²: 0.9998
6.7
Bài tập thực hành
Phần bài tập này tập trung vào các kỹnăng NumPy cơ bản và một bài nâng cao, giúp
củng cốkiến thức đã học.
Bài 1: Tạo và thao tác mảng cơ bản
Viết chương trình thực hiện các yêu cầu sau:
1. Tạo mảng 1 chiều chứa các sốtừ10 đến 50 (bước nhảy 5)
2. Tạo ma trận 4x5 với các giá trịngẫu nhiên từ0 đến 100
3. Tạo ma trận đơn vị5x5
4. Tạo ma trận 3x3 với giá trịđường chéo là [1, 2, 3]
Gợi ý: Sửdụng np.arange(), np.random.randint(), np.eye(), np.diag()
Bài 2: Indexing và Slicing
143

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
Cho ma trận:
A = np.array([[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120],

[130, 140, 150, 160]])
Thực hiện các yêu cầu:
1. Lấy phần tửởhàng 2, cột 3
2. Lấy toàn bộhàng thứ2
3. Lấy toàn bộcột thứ3
4. Lấy ma trận con 2x2 từgóc dưới phải
5. Lấy các phần tửcó giá trịlớn hơn 80
6. Thay thếtất cảgiá trịchẵn bằng 0
Gợi ý: Sửdụng indexing, slicing, boolean indexing
Bài 3: Các phép toán ma trận cơ bản
Cho hai ma trận:
A = np.array([[1, 2], [3, 4], [5, 6]])
# 3x2
B = np.array([[7, 8, 9], [10, 11, 12]]) # 2x3
Thực hiện:
1. Nhân ma trận A và B (matrix multiplication)
2. Tìm ma trận chuyển vịcủa A
3. Tính tổng tất cảphần tửcủa ma trận A
4. Tính trung bình từng cột của ma trận A
5. Tìm giá trịlớn nhất và nhỏnhất trong mỗi hàng của B
Gợi ý: Sửdụng @ hoặc np.dot(), .T, np.sum(), np.mean(), np.max(),
np.min()
Bài 4: Thống kê và xửlý dữliệu
Cho dữliệu nhiệt độđo được trong 14 ngày (°C):
temps = np.array([22.5, 23.1, 22.8, 23.5, 150.0, 22.9, 23.7,
23.2, 24.1, 22.7, -20.0, 23.5, 23.0,
22.8])
,→
144

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
Yêu cầu:
1. Tìm nhiệt độtrung bình, độlệch chuẩn, min, max
2. Phát hiện và in ra các giá trịngoại lệ(outliers) nằm ngoài khoảng [0°C, 50°C]
3. Thay thếcác outliers bằng giá trịtrung vị(median) của dữliệu hợp lệ
4. Tính lại nhiệt độtrung bình sau khi làm sạch dữliệu
Gợi ý: Sửdụng np.mean(), np.std(), boolean indexing, np.median()
Bài 5: Reshape và Broadcasting
1. Tạo mảng 1D chứa các sốtừ1 đến 24
2. Reshape thành ma trận 4x6
3. Reshape thành ma trận 3D có kích thước 2x3x4
4. Cộng một vector [10, 20, 30, 40, 50, 60] vào từng hàng của ma trận 4x6 (sửdụng
broadcasting)
5. Tính tổng theo từng chiều của ma trận 3D

Gợi ý: Sửdụng np.arange(), reshape(), broadcasting, np.sum(axis=...)
Bài 6: Sắp xếp và tìm kiếm
Cho mảng điểm của sinh viên:
scores = np.array([7.5, 8.2, 6.8, 9.1, 5.5, 8.7, 7.9, 6.2,
8.5, 7.3])
,→
Yêu cầu:
1. Sắp xếp điểm theo thứtựtăng dần
2. Tìm chỉsốcủa sinh viên có điểm cao nhất
3. Đếm sốsinh viên có điểm >= 8.0
4. Tính điểm trung bình của 3 sinh viên có điểm cao nhất
5. Phân loại: >= 8.5: "Giỏi", >= 7.0: "Khá", >= 5.5: "Trung bình", còn lại: "Yếu"
Gợi ý: Sửdụng np.sort(), np.argmax(), boolean indexing, np.where()
Bài 7: Ma trận và hệphương trình (Nâng cao)
Trong một mạch điện có 3 node, áp dụng định luật Kirchhoff ta có hệphương trình:
3I1 −I2 = 12
−I1 + 4I2 −I3 = 0
−I2 + 3I3 = 6
145
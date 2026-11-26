<!-- page: 1 -->
# VI_PY_052: Thư viện NumPy: Mảng đa chiều ndarray và kỹ thuật vector hóa tính toán

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: NumPy | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 132 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
matrix = np.array([[10, 20, 30],
[40, 50, 60],
[70, 80, 90]])
# Lấy phần tửở(0,1), (1,2), (2,0)
rows = np.array([0, 1, 2])
cols = np.array([1, 2, 0])
print("Cac phan tu:", matrix[rows, cols])
# [20, 60, 70]
Kết quả:
Cac phan tu tai [1,3,5]: [20 40 60]
Lay theo thu tu: [80 30 60 20]
Cac phan tu: [20 60 70]
b, Boolean Indexing - Chỉmục điều kiện
Đây là kỹthuật mạnh mẽcho phép lọc dữliệu dựa trên điều kiện logic. Rất hữu ích
trong xửlý và làm sạch dữliệu.
arr = np.array([15, 22, 8, 31, 19, 7, 42, 11])
# Tạo mặt nạboolean
mask = arr > 20
print("Mat na boolean:", mask)
print("Cac phan tu > 20:", arr[mask])
# Viết gọn trong một dòng
print("Cac phan tu < 15:", arr[arr < 15])
# Kết hợp nhiều điều kiện
print("Phan tu trong khoang [10, 25]:",
arr[(arr >= 10) & (arr <= 25)])
# Lọc sốchẵn
print("So chan:", arr[arr % 2 == 0])
# Lọc sốlẻ
print("So le:", arr[arr % 2 != 0])
Kết quả:
Mat na boolean: [False
True False
True False False

<!-- page: 2 -->

True False]
Cac phan tu > 20: [22 31 42]
Cac phan tu < 15: [ 8
7 11]
Phan tu trong khoang [10, 25]: [15 22 19 11]
117

<!-- page: 133 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
So chan: [22
8 42]
So le: [15 31 19
7 11]
Ứng dụng trong kỹthuật: Lọc dữliệu đo từcảm biến, loại bỏcác giá trịngoài ngưỡng
hoặc lỗi.
# Dữliệu nhiệt độtừcảm biến
temperatures = np.array([22.5, 23.1, 150.0, 22.8, -10.0,
23.4, 24.1, 22.9, 200.0])
# Lọc dữliệu hợp lệ(0°C đến 50°C)
valid_temps = temperatures[(temperatures >= 0) &
(temperatures <= 50)]
print("Nhiet do hop le:", valid_temps)
# Thay thếdữliệu lỗi bằng giá trịtrung bình
mean_temp = np.mean(valid_temps)
temperatures[(temperatures < 0) | (temperatures > 50)] =
mean_temp
,→
print("Sau khi xu ly:", temperatures)
c, Chỉmục với np.where
Hàm np.where() trảvềchỉsốcủa các phần tửthỏa điều kiện, hoặc cho phép thay
thếgiá trịtheo điều kiện.
arr = np.array([10, 25, 30, 15, 40, 8])
# Tìm chỉsốcủa các phần tử> 20
indices = np.where(arr > 20)
print("Chi so cac phan tu > 20:", indices[0])
# Thay thếtheo điều kiện: nếu > 20 thì giữnguyên,
# ngược lại thay bằng 0
result = np.where(arr > 20, arr, 0)
print("Ket qua:", result)
# Phân loại: > 25 -> 'cao', <= 25 -> 'thap'
labels = np.where(arr > 25, 'cao', 'thap')
print("Phan loai:", labels)
Kết quả:
Chi so cac phan tu > 20: [1 2 4]
Ket qua: [ 0 25 30

<!-- page: 3 -->

0 40
0]
Phan loai: ['thap' 'thap' 'cao' 'thap' 'cao' 'thap']
118

<!-- page: 134 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
6.4
Các phép toán trên ma trận
Một trong những sức mạnh lớn nhất của NumPy là khảnăng thực hiện các phép toán
trên toàn bộmảng mà không cần vòng lặp tường minh. Các phép toán này được thực thi
rất nhanh nhờtối ưu hóa ởtầng thấp.
6.4.1
Phép toán từng phần tử(Element-wise Operations)
Các phép toán cơ bản được áp dụng trên từng phần tửtương ứng của hai mảng có cùng
kích thước.
a = np.array([[1, 2, 3],
[4, 5, 6]])
b = np.array([[10, 20, 30],
[40, 50, 60]])
# Cộng
print("a + b:")
print(a + b)
# Trừ
print("\na - b:")
print(a - b)
# Nhân từng phần tử
print("\na * b (element-wise):")
print(a * b)
# Chia
print("\nb / a:")
print(b / a)
# Lũy thừa
print("\na ** 2:")
print(a ** 2)
# Chia lấy phần nguyên
print("\nb // a:")
print(b // a)
# Chia lấy phần dư
print("\nb % 3:")
print(b % 3)
Kết quả:
119

<!-- page: 135 -->

<!-- page: 4 -->

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
a + b:
[[11 22 33]
[44 55 66]]
a - b:
[[-9 -18 -27]
[-36 -45 -54]]
a * b (element-wise):
[[ 10
40
90]
[160 250 360]]
b / a:
[[10. 10. 10.]
[10. 10. 10.]]
a ** 2:
[[ 1
4
9]
[16 25 36]]
6.4.2
Phép toán với scalar
NumPy tựđộng áp dụng phép toán với scalar lên tất cảphần tửcủa mảng.
arr = np.array([[1, 2, 3],
[4, 5, 6]])
print("arr * 10:")
print(arr * 10)
print("\narr + 5:")
print(arr + 5)
print("\n2 ** arr:")
print(2 ** arr)
print("\narr / 2:")
print(arr / 2)
Kết quả:
arr * 10:
[[10 20 30]
[40 50 60]]
120

<!-- page: 136 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
arr + 5:
[[ 6
7
8]

<!-- page: 5 -->

[ 9 10 11]]
2 ** arr:
[[ 2
4
8]
[16 32 64]]
6.4.3
Nhân ma trận (Matrix Multiplication)
Trong đại sốtuyến tính, nhân ma trận là phép toán quan trọng, khác hoàn toàn với nhân
từng phần tử.
# Ma trận A (2x3)
A = np.array([[1, 2, 3],
[4, 5, 6]])
# Ma trận B (3x2)
B = np.array([[7, 8],
[9, 10],
[11, 12]])
# Nhân ma trận - cách 1: dùng np.dot()
C1 = np.dot(A, B)
print("np.dot(A, B):")
print(C1)
# Nhân ma trận - cách 2: dùng toán tử@
C2 = A @ B
print("\nA @ B:")
print(C2)
# Nhân ma trận - cách 3: dùng matmul
C3 = np.matmul(A, B)
print("\nnp.matmul(A, B):")
print(C3)
# Kiểm tra kích thước
print("\nKich thuoc A:", A.shape)
print("Kich thuoc B:", B.shape)
print("Kich thuoc C:", C1.shape)
Kết quả:
np.dot(A, B):
121

<!-- page: 137 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
[[ 58
64]
[139 154]]
A @ B:
[[ 58
64]

<!-- page: 6 -->

[139 154]]
Kich thuoc A: (2, 3)
Kich thuoc B: (3, 2)
Kich thuoc C: (2, 2)
Lưu ý: Đểnhân được hai ma trận, sốcột của ma trận thứnhất phải bằng sốhàng của
ma trận thứhai.
6.4.4
Chuyển vịma trận (Transpose)
Chuyển vịlà phép hoán đổi hàng và cột của ma trận.
A = np.array([[1, 2, 3],
[4, 5, 6]])
print("Ma tran goc:")
print(A)
print("Kich thuoc:", A.shape)
# Chuyển vị- cách 1
A_T1 = np.transpose(A)
print("\nChuyen vi (transpose):")
print(A_T1)
# Chuyển vị- cách 2
A_T2 = A.T
print("\nChuyen vi (thuoc tinh .T):")
print(A_T2)
print("Kich thuoc:", A_T2.shape)
Kết quả:
Ma tran goc:
[[1 2 3]
[4 5 6]]
Kich thuoc: (2, 3)
Chuyen vi (transpose):
[[1 4]
122

<!-- page: 138 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
[2 5]
[3 6]]
Kich thuoc: (3, 2)
6.4.5
Các phép toán ma trận nâng cao
NumPy cung cấp module linalg chứa nhiều hàm đại sốtuyến tính nâng cao.
a, Ma trận nghịch đảo
# Ma trận vuông
A = np.array([[4, 7],
[2, 6]])
print("Ma tran A:")

<!-- page: 7 -->

print(A)
# Tính ma trận nghịch đảo
A_inv = np.linalg.inv(A)
print("\nMa tran nghich dao A^(-1):")
print(A_inv)
# Kiểm chứng: A * A^(-1) = I (ma trận đơn vị)
I = A @ A_inv
print("\nA @ A^(-1):")
print(I)
Kết quả:
Ma tran A:
[[4 7]
[2 6]]
Ma tran nghich dao A^(-1):
[[ 0.6 -0.7]
[-0.2
0.4]]
A @ A^(-1):
[[1. 0.]
[0. 1.]]
123

<!-- page: 139 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
b, Định thức
A = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 10]])
det_A = np.linalg.det(A)
print("Dinh thuc cua A:", det_A)
# Ma trận suy biến (định thức = 0)
B = np.array([[1, 2],
[2, 4]])
det_B = np.linalg.det(B)
print("Dinh thuc cua B:", det_B)
Kết quả:
Dinh thuc cua A: -3.0
Dinh thuc cua B: 0.0
c, Hạng của ma trận
A = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
rank = np.linalg.matrix_rank(A)
print("Hang cua ma tran:", rank)
d, Giá trịriêng và vector riêng

<!-- page: 8 -->

A = np.array([[4, -2],
[1,
1]])
# Tính giá trịriêng và vector riêng
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Gia tri rieng:")
print(eigenvalues)
print("\nVector rieng:")
print(eigenvectors)
# Kiem chung: A * v = lambda * v
v1 = eigenvectors[:, 0]
124

<!-- page: 140 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
lambda1 = eigenvalues[0]
print("\nKiem chung:")
print("A @ v1:", A @ v1)
print("lambda1 * v1:", lambda1 * v1)
e, Vết của ma trận (Trace)
A = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# Vết = tổng các phần tửtrên đường chéo chính
trace = np.trace(A)
print("Vet cua ma tran:", trace)
# 1 + 5 + 9 = 15
f, Giải hệphương trình tuyến tính
NumPy có thểgiải hệphương trình tuyến tính dạng Ax = b.
# Hệphương trình:
# 3x + 2y = 7
# x + 4y = 11
A = np.array([[3, 2],
[1, 4]])
b = np.array([7, 11])
# Giải hệ
x = np.linalg.solve(A, b)
print("Nghiem cua he:", x)
# Kiểm chứng
print("Kiem chung A @ x:", A @ x)
print("b:", b)
Kết quả:
Nghiem cua he: [1. 2.]
Kiem chung A @ x: [ 7. 11.]
b: [ 7 11]

<!-- page: 9 -->

Ứng dụng trong kỹthuật: Giải hệphương trình mô tảmạch điện, cân bằng lực trong
kết cấu, hoặc phân tích hệthống điều khiển.
125

<!-- page: 141 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
6.4.6
Broadcasting - Cơ chếmởrộng tựđộng
Broadcasting là một cơ chếmạnh mẽcho phép NumPy thực hiện các phép toán trên
các mảng có kích thước khác nhau.
# Ví dụ1: Cộng vector vào ma trận
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
vector = np.array([10, 20, 30])
# Vector được broadcast thành ma trận 3x3
result = matrix + vector
print("Ma tran + vector:")
print(result)
# Ví dụ2: Chuẩn hóa từng cột
data = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# Trung bình từng cột
col_means = np.mean(data, axis=0)
print("\nTrung binh cot:", col_means)
# Chuẩn hóa
normalized = data - col_means
print("Chuan hoa:")
print(normalized)
Kết quả:
Ma tran + vector:
[[11 22 33]
[14 25 36]
[17 28 39]]
Trung binh cot: [4. 5. 6.]
Chuan hoa:
[[-3. -3. -3.]
[ 0.
0.
0.]
[ 3.
3.
3.]]
Quy tắc broadcasting:

<!-- page: 10 -->

126

<!-- page: 142 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
1. Nếu hai mảng có sốchiều khác nhau, mảng có ít chiều hơn sẽđược thêm chiều mới
ởphía trước
2. Nếu kích thước ởmột chiều không khớp, chiều có kích thước 1 sẽđược kéo dãn để
khớp với chiều kia
3. Nếu kích thước không khớp và không có chiều nào bằng 1, sẽbáo lỗi
# Ví dụbroadcasting phức tạp hơn
A = np.ones((3, 4))
# shape (3, 4)
B = np.array([1, 2, 3, 4])
# shape (4,)
C = np.array([[10], [20], [30]])
# shape (3, 1)
print("A + B (broadcast hang):")
print(A + B)
print("\nA + C (broadcast cot):")
print(A + C)
print("\nB + C (broadcast 2 chieu):")
print(B + C)
6.5
Các phép xửlý và thống kê trên ma trận
NumPy cung cấp một bộcông cụphong phú đểxửlý và phân tích thống kê dữliệu.
Các hàm này có thểáp dụng trên toàn bộmảng hoặc theo từng trục (axis) cụthể.
6.5.1
Các hàm thống kê cơ bản
data = np.array([[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120]])
print("Ma tran du lieu:")
print(data)
# Tổng
print("\nTong toan bo:", np.sum(data))
print("Tong theo cot (axis=0):", np.sum(data, axis=0))
print("Tong theo dong (axis=1):", np.sum(data, axis=1))
# Trung bình
print("\nTrung binh toan bo:", np.mean(data))
print("Trung binh theo cot:", np.mean(data, axis=0))
print("Trung binh theo dong:", np.mean(data, axis=1))
127

<!-- page: 143 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT

<!-- page: 11 -->

# Min, Max
print("\nGia tri nho nhat:", np.min(data))
print("Gia tri lon nhat:", np.max(data))
print("Min theo cot:", np.min(data, axis=0))
print("Max theo dong:", np.max(data, axis=1))
Kết quả:
Ma tran du lieu:
[[ 10
20
30
40]
[ 50
60
70
80]
[ 90 100 110 120]]
Tong toan bo: 780
Tong theo cot (axis=0): [150 180 210 240]
Tong theo dong (axis=1): [100 260 420]
Trung binh toan bo: 65.0
Trung binh theo cot: [ 50.
60.
70.
80.]
Trung binh theo dong: [ 25.
65. 105.]
Gia tri nho nhat: 10
Gia tri lon nhat: 120
6.5.2
Chỉsốcủa giá trịmin/max
arr = np.array([[15, 32, 8],
[41, 25, 19],
[7, 50, 12]])
# Chỉsốcủa giá trịnhỏnhất (theo dạng phẳng)
print("Chi so min (flat):", np.argmin(arr))
# Chỉsốcủa giá trịlớn nhất
print("Chi so max (flat):", np.argmax(arr))
# Chỉsốmin theo từng cột
print("Chi so min theo cot:", np.argmin(arr, axis=0))
# Chỉsốmax theo từng dòng
print("Chi so max theo dong:", np.argmax(arr, axis=1))
# Tìm vịtrí (hàng, cột) của giá trịmax
128

<!-- page: 144 -->

<!-- page: 12 -->

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
max_pos = np.unravel_index(np.argmax(arr), arr.shape)
print("Vi tri max (hang, cot):", max_pos)
Kết quả:
Chi so min (flat): 6
Chi so max (flat): 7
Chi so min theo cot: [2 1 0]
Chi so max theo dong: [1 0 1]
Vi tri max (hang, cot): (2, 1)
6.5.3
Phương sai và độlệch chuẩn
data = np.array([[20, 25, 30],
[22, 28, 35],
[18, 24, 29]])
# Phương sai
variance = np.var(data)
print("Phuong sai:", variance)
# Độlệch chuẩn
std_dev = np.std(data)
print("Do lech chuan:", std_dev)
# Theo từng cột
print("\nDo lech chuan theo cot:", np.std(data, axis=0))
# Theo từng dòng
print("Do lech chuan theo dong:", np.std(data, axis=1))
6.5.4
Tích lũy và tích lũy theo chiều
arr = np.array([1, 2, 3, 4, 5])
# Tổng tích lũy
cumsum = np.cumsum(arr)
print("Tong tich luy:", cumsum)
# Tích tích lũy
cumprod = np.cumprod(arr)
print("Tich tich luy:", cumprod)
# Với ma trận
129

<!-- page: 145 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
matrix = np.array([[1, 2, 3],
[4, 5, 6]])
print("\nTong tich luy theo cot:")
print(np.cumsum(matrix, axis=0))
print("\nTong tich luy theo dong:")
print(np.cumsum(matrix, axis=1))
Kết quả:

<!-- page: 13 -->

Tong tich luy: [ 1
3
6 10 15]
Tich tich luy: [
1
2
6
24 120]
Tong tich luy theo cot:
[[1 2 3]
[5 7 9]]
Tong tich luy theo dong:
[[ 1
3
6]
[ 4
9 15]]
6.5.5
Sắp xếp mảng
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
# Sắp xếp (trảvềbản sao đã sắp xếp)
sorted_arr = np.sort(arr)
print("Sap xep:", sorted_arr)
# Chỉsốsắp xếp
indices = np.argsort(arr)
print("Chi so sap xep:", indices)
# Sắp xếp ma trận
matrix = np.array([[3, 1, 4],
[1, 5, 9],
[2, 6, 5]])
print("\nSap xep theo hang:")
print(np.sort(matrix, axis=1))
print("\nSap xep theo cot:")
print(np.sort(matrix, axis=0))
130

<!-- page: 146 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
Kết quả:
Sap xep: [1 1 2 3 4 5 6 9]
Chi so sap xep: [1 3 6 0 2 4 7 5]
Sap xep theo hang:
[[1 3 4]
[1 5 9]
[2 5 6]]

<!-- page: 14 -->

6.5.6
Loại bỏtrùng lặp và tìm giá trịduy nhất
arr = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5])
# Giá trịduy nhất
unique = np.unique(arr)
print("Gia tri duy nhat:", unique)
# Đếm sốlần xuất hiện
unique, counts = np.unique(arr, return_counts=True)
print("\nGia tri:", unique)
print("So lan xuat hien:", counts)
# Tìm giá trịduy nhất trong ma trận
matrix = np.array([[1, 2, 3],
[2, 3, 4],
[3, 4, 5]])
print("\nGia tri duy nhat trong ma tran:",
np.unique(matrix))
,→
Kết quả:
Gia tri duy nhat: [1 2 3 4 5]
Gia tri: [1 2 3 4 5]
So lan xuat hien: [1 2 3 1 2]
Gia tri duy nhat trong ma tran: [1 2 3 4 5]
6.5.7
Các hàm toán học phổbiến
NumPy cung cấp các hàm toán học áp dụng trên từng phần tửcủa mảng.
arr = np.array([1, 4, 9, 16, 25])
131

<!-- page: 147 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
# Căn bậc hai
print("Căn bậc hai:", np.sqrt(arr))
# Lũy thừa
print("Luy thua 2:", np.power(arr, 2))
# Hàm mũ
print("e^x:", np.exp([1, 2, 3]))
# Logarit
print("log(arr):", np.log(arr))
print("log10(arr):", np.log10(arr))
# Làm tròn
values = np.array([1.234, 2.567, 3.891])
print("\nLam tron 2 chu so:", np.round(values, 2))
print("Lam tron xuong:", np.floor(values))
print("Lam tron len:", np.ceil(values))
# Giá trịtuyệt đối

<!-- page: 15 -->

print("\nGia tri tuyet doi:", np.abs([-1, -2, 3, -4]))
Kết quả:
Căn bậc hai: [1. 2. 3. 4. 5.]
Luy thua 2: [
1
16
81 256 625]
e^x: [ 2.71828183
7.3890561
20.08553692]
log(arr): [0.
1.38629436 2.19722458 2.77258872 3.21887582]
Lam tron 2 chu so: [1.23 2.57 3.89]
Lam tron xuong: [1. 2. 3.]
Lam tron len: [2. 3. 4.]
Gia tri tuyet doi: [1 2 3 4]
6.5.8
Hàm lượng giác
angles_deg = np.array([0, 30, 45, 60, 90])
# Chuyển độsang radian
angles_rad = np.radians(angles_deg)
print("Sin:", np.sin(angles_rad))
print("Cos:", np.cos(angles_rad))
132

<!-- page: 148 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
print("Tan:", np.tan(angles_rad))
# Hàm ngược
print("\narcsin(0.5):", np.arcsin(0.5))
print("arccos(0.5):", np.arccos(0.5))
print("arctan(1):", np.arctan(1))
# Chuyển radian sang độ
print("\nChuyen sang do:", np.degrees(np.pi))
6.5.9
Chuẩn hóa dữliệu
Chuẩn hóa là kỹthuật quan trọng trong xửlý dữliệu và machine learning.
# Dữliệu mẫu
data = np.array([[100, 200, 300],
[150, 250, 350],
[200, 300, 400]])
print("Du lieu goc:")
print(data)
# Chuẩn hóa Min-Max về[0, 1]
data_min = np.min(data)

<!-- page: 16 -->

data_max = np.max(data)
normalized = (data - data_min) / (data_max - data_min)
print("\nChuan hoa Min-Max:")
print(normalized)
# Chuẩn hóa Z-score (mean=0, std=1)
mean = np.mean(data)
std = np.std(data)
z_normalized = (data - mean) / std
print("\nChuan hoa Z-score:")
print(z_normalized)
# Chuẩn hóa theo từng cột
col_means = np.mean(data, axis=0)
col_stds = np.std(data, axis=0)
col_normalized = (data - col_means) / col_stds
print("\nChuan hoa theo cot:")
print(col_normalized)
Ứng dụng trong kỹthuật: Chuẩn hóa dữliệu từnhiều cảm biến có đơn vịvà tỷlệ
khác nhau đểso sánh và phân tích thống nhất.
133

<!-- page: 149 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
6.5.10
Reshape và thay đổi cấu trúc mảng
# Mảng ban đầu
arr = np.arange(12)
print("Mang ban dau:", arr)
# Reshape thành ma trận 3x4
reshaped = arr.reshape(3, 4)
print("\nReshape 3x4:")
print(reshaped)
# Reshape thành 2x2x3
reshaped_3d = arr.reshape(2, 2, 3)
print("\nReshape 2x2x3:")
print(reshaped_3d)
# Làm phẳng (flatten)
flattened = reshaped.flatten()
print("\nLam phang:", flattened)
# Ravel (tương tựflatten nhưng trảvềview)
raveled = reshaped.ravel()
print("Ravel:", raveled)
# Reshape tựđộng (-1)
auto_reshape = arr.reshape(3, -1)
# Tựtính chiều thứ2
print("\nReshape tu dong 3x?:")

<!-- page: 17 -->

print(auto_reshape)
Kết quả:
Mang ban dau: [ 0
1
2
3
4
5
6
7
8
9 10 11]
Reshape 3x4:
[[ 0
1
2
3]
[ 4
5
6
7]
[ 8
9 10 11]]
Lam phang: [ 0
1
2
3
4
5
6
7
8
9 10 11]
Reshape tu dong 3x?:
[[ 0
1
2
3]
[ 4
5
6
7]
[ 8
9 10 11]]
134

<!-- page: 18 -->


<!-- page: 150 -->
CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
6.5.11
Nối và chia mảng
a = np.array([[1, 2],
[3, 4]])
b = np.array([[5, 6],
[7, 8]])
# Nối theo chiều dọc (vertical stack)
v_stack = np.vstack((a, b))
print("Vertical stack:")
print(v_stack)
# Nối theo chiều ngang (horizontal stack)
h_stack = np.hstack((a, b))
print("\nHorizontal stack:")
print(h_stack)
# Concatenate với axis
concat_0 = np.concatenate((a, b), axis=0)
print("\nConcatenate axis=0:")
print(concat_0)
concat_1 = np.concatenate((a, b), axis=1)
print("\nConcatenate axis=1:")
print(concat_1)
# Chia mảng
arr = np.arange(12).reshape(3, 4)
print("\nMang ban dau:")
print(arr)
# Chia thành 3 phần theo chiều ngang
splits = np.split(arr, 3, axis=0)
print("\nChia thanh 3 phan theo hang:")
for i, part in enumerate(splits):
print(f"Phan {i+1}:")
print(part)
Kết quả:
Vertical stack:
[[1 2]
[3 4]
[5 6]
135
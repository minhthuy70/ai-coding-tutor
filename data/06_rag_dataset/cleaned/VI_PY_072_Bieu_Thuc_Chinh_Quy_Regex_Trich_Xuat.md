# VI_PY_072: Biểu thức chính quy Regex trong tiền xử lý và trích xuất dữ liệu

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân
**Chuyên mục**: Regex | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 2. CÚ PHÁP PYTHON CƠ BẢN
8
3
if score >= 0.8:
4
print("Mo hinh dat do chinh xac cao")
5
else:
6
print("Can can thiep hoac toi uu them")
2.6
Tóm tắt chương
Trong chương này, chúng ta đã nắm được:
• Cách khai báo biến và chi tiết các kiểu dữliệu cơ bản trong Python.
• Các toán tửsốhọc và toán tửgán mởrộng.
• Cách sửdụng thư viện math cho các hàm toán học phức tạp.
• Cấu trúc dữliệu nâng cao: List, Tuple, Dictionary.
• Cấu trúc rẽnhánh trong Python.

Chương 3:
Lập trình hướng đối tượng trong
Python
Lập trình hướng đối tượng (Object-Oriented Programming - OOP) là phương pháp luận lập trình
đóng vai trò then chốt trong việc thiết kếcác thư viện Machine Learning hiện đại như Scikit-
Learn, PyTorch và TensorFlow. Chương này trình bày các khái niệm OOP cốt lõi và hướng dẫn
cách ứng dụng OOP đểtựđóng gói một mô hình Machine Learning.
3.1
Lớp và Đối tượng (Class and Object)
Định nghĩa 3.1 (Lớp và Đối tượng). Lớp (Class) là khuôn mẫu định nghĩa các thuộc tính (dữ
liệu) và phương thức (hành vi). Đối tượng (Object) là một thểhiện cụthểđược khởi tạo từlớp
đó.
Ví dụ3.1. Khai báo một lớp cơ bản lưu trữmẫu dữliệu:
Listing 3.1: Khai báo Class và tạo Object trong Python

1
class DataSample:
2
def __init__(self, feature_name , value):
3
self.feature_name = feature_name
# Thuoc tinh
4
self.value = value
5
6
def display_info(self):
# Phuong thuc
7
print(f"Feature: {self.feature_name}, Value: {self.value}")
8
9
# Khoi tao doi tuong
10
sample = DataSample(feature_name="Age", value=25)
11
sample.display_info()
3.2
Các phương thức đặc biệt (Magic Methods)
Các phương thức có cú pháp hai dấu gạch dưới (__method__) giúp tùy biến hành vi của đối
tượng trong Python.
3.2.1
Phương thức __init__ và __call__
• __init__: Hàm khởi tạo (constructor), tựđộng thực thi khi tạo mới một đối tượng.
9

CHƯƠNG 3. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
10
• __call__: Cho phép gọi trực tiếp một đối tượng giống như một hàm, thường dùng khi
thiết kếcác Layer trong Neural Network.
Listing 3.2: Sửdụng phương thức __call__
1
class Multiplier:
2
def __init__(self, factor):
3
self.factor = factor
4
5

def __call__(self, x):
6
return x * self.factor
7
8
# Su dung nhu mot ham
9
double = Multiplier(factor=2)
10
print(double(5))
# Output: 10
3.3
Tính Kếthừa (Inheritance)
Tính kếthừa cho phép tạo một lớp mới dựa trên lớp đã có, giúp tái sửdụng mã nguồn và chuẩn
hóa giao diện của các bộbiến đổi dữliệu (Transformers).
Listing 3.3: Kếthừa lớp BaseTransformer trong tiền xửlý dữliệu
1
class BaseTransformer:
2
def fit(self, arr):
3
raise NotImplementedError("Phuong thuc fit() bat buoc phai
duoc trien khai o lop con.")
4
5
def transform(self, arr):
6
raise NotImplementedError("Phuong thuc transform() bat buoc
phai trien khai o lop con.")
7
8
def fit_transform(self, arr):
9
self.fit(arr)
10
return self.transform(arr)
11
12
class MinMaxScaler(BaseTransformer):
13
def fit(self, arr):
14
self.min_ = min(arr)
15
self.max_ = max(arr)

16
return self
17
18
def transform(self, arr):
19
return [(x - self.min_) / (self.max_ - self.min_) for x in
arr]
20
21
def inverse_transform(self, arr):
22
return [x * (self.max_ - self.min_) + self.min_ for x in arr]

CHƯƠNG 3. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
11
3.4
Quản lý thuộc tính: Siêu tham số(Hyperparameters) và
Tham sốhọc được (Learned Parameters)
Trong thiết kếMachine Learning, ta cần phân biệt rõ giữa siêu tham số(cấu hình trước khi huấn
luyện) và tham sốhọc được (được sinh ra sau khi gọi hàm fit).
Listing 3.4: Bắt lỗi an toàn khi quản lý tham sốhọc được
1
class MinMaxScaler(BaseTransformer):
2
def __init__(self, feature_range=(0, 1)):
3
self.feature_range = feature_range
# Hyperparameter
4
5
def fit(self, arr):
6
self.min = float(min(arr))
# Learned Parameter
7
self.max = float(max(arr))
# Learned Parameter
8
return self
9
10
def transform(self, arr):
11

# Kiem tra an toan: Đam bao mo hinh da duoc fit()
12
if not hasattr(self, 'min') or not hasattr(self, 'max'):
13
raise RuntimeError("Loi: Ban phai goi ham fit() truoc khi
goi transform()!")
14
15
low, high = self.feature_range
16
std = [(x - self.min) / (self.max - self.min) for x in arr]
17
return [x * (high - low) + low for x in std]
3.5
Thiết kếCustom Estimator chuẩn Scikit-Learn
Trọng tâm ứng dụng OOP trong Machine Learning là đóng gói thuật toán thành một Class có
các giao diện chuẩn (fit, predict, evaluate). Dưới đây là triển khai mô hình Hồi quy tuyến
tính đơn biến (Simple Linear Regression) bằng công thức đại số.
Listing 3.5: Đóng gói thuật toán Simple Linear Regression
1
class SimpleLinearRegression:
2
def __init__(self):
3
self.w0 = 0
4
self.w1 = 0
5
6
def fit(self, X, y):
7
n = len(X)
8
mean_x = sum(X) / n
9
mean_y = sum(y) / n
10
11
numerator = sum((X[i] - mean_x) * (y[i] - mean_y) for i in
range(n))
12
denominator = sum((X[i] - mean_x) ** 2 for i in range(n))
13
14
if denominator == 0:

CHƯƠNG 3. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
12
15
raise ValueError("Bao loi: Phuong sai cua X bang 0, khong
the tinh toan.")
16
17
self.w1 = numerator / denominator
18
self.w0 = mean_y - (self.w1 * mean_x)
19
return self
20
21
def predict(self, X):
22
return [(self.w1 * x_i + self.w0) for x_i in X]
23
24
def evaluate(self, X, y):
25
predictions = self.predict(X)
26
mse = sum((predictions[i] - y[i]) ** 2 for i in range(len(y))
) / len(y)
27
return mse
3.6
Mẫu thiết kếPipeline
Pipeline là lớp quản lý chuỗi các bước biến đổi dữliệu nối tiếp nhau, cho phép tựđộng hóa toàn
bộquy trình tiền xửlý trước khi đưa vào mô hình dựđoán.
Listing 3.6: Triển khai cấu trúc Pipeline cơ bản
1
class Pipeline:
2
def __init__(self, steps):
3
self.steps = steps
4
5
def fit_transform(self, arr):
6
data = arr

7
for transformer in self.steps:
8
data = transformer.fit_transform(data)
9
return data
10
11
def transform(self, arr):
12
data = arr
13
for transformer in self.steps:
14
data = transformer.transform(data)
15
return data
3.7
Tóm tắt chương
• Khái niệm Lớp, Đối tượng và tư duy lập trình hướng đối tượng.
• Ứng dụng các Magic Methods (__init__, __call__) trong xây dựng Framework.
• Nguyên lý Kếthừa giúp tái sửdụng và quản lý mã nguồn linh hoạt.
• Đóng gói thuật toán Machine Learning thành Class theo giao diện tiêu chuẩn.
• Phân biệt rõ ràng siêu tham sốvà tham sốhọc được thông qua các thuộc tính của đối tượng

Chương 4:
XửLý DữLiệu Với NumPy Và
Pandas
(NumPy & Pandas)
Trong khoa học dữliệu và học máy, việc xửlý dữliệu đóng vai trò nền tảng. Dữliệu thực tế
thường lộn xộn, thiếu sót hoặc không đúng định dạng. Đểgiải quyết vấn đềnày, Python cung
cấp hệsinh thái các thư viện mạnh mẽ, trong đó nổi bật nhất là NumPy và Pandas. Chương này
sẽhướng dẫn bạn cách sửdụng hai thư viện này đểthực hiện các thao tác tiền xửlý, phân tích
và biến đổi dữliệu một cách hiệu quả.
4.1
Thư viện NumPy - Tính toán Khoa học
NumPy (Numerical Python) là thư viện cốt lõi cho tính toán khoa học trong Python. Nó cung
cấp đối tượng mảng đa chiều hiệu suất cao và các công cụđểlàm việc với các mảng này.
4.1.1
Khởi tạo mảng và kiểm tra thuộc tính
NumPy hỗtrợtạo mảng đa chiều từlist của Python hoặc sửdụng các hàm có sẵn đểkhởi tạo
các ma trận đặc biệt.
1
import numpy as np

2
3
arr1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
4
print("Shape 1D:", arr1D.shape, "| Dtype:", arr1D.dtype)
5
6
arr2D = np.array([[1, 2, 3, 4],
7
[5, 6, 7, 8],
8
[9, 10, 11, 12]])
9
print("Shape 2D:", arr2D.shape, "| So chieu (ndim):", arr2D.ndim)
10
11
12
arr_zeros = np.zeros((3, 4))
13
arr_ones = np.ones((2, 5))
14
arr_eye = np.identity(3)
15
arr_random = np.random.randn(3, 4)
13

CHƯƠNG 4. XỬLÝ DỮLIỆU VỚI NUMPY VÀ PANDAS
(NUMPY & PANDAS)
14
Hình 4.1: Khởi tạo và kiểm tra thuộc tính mảng NumPy
4.1.2
Thao tác trên mảng: Thêm phần tử, xóa, sửa
Trong quá trình xửlý, việc thay đổi cấu trúc mảng bằng cách thêm, xóa, sửa phần tửlà rất
thường xuyên. NumPy cung cấp các hàm như append, insert, và delete đểthao tác với phần
tửmảng.
1
arr1D[0] = 99
2
3
arr_appended = np.append(arr1D, [11, 12])
4
arr_inserted = np.insert(arr1D, 2, 999)
5
6

arr_deleted = np.delete(arr1D, 0)
4.1.3
Slicing và Boolean Indexing (Lọc dữliệu)
Slicing cho phép lấy một phần của mảng, trong khi Boolean Indexing cho phép lọc các phần tử
thỏa mãn điều kiện nhất định.
1
2
sub_arr = arr2D[:2, :3]
3
print("Cat mang [:2, :3]:\n", sub_arr)
4
5
6
city_data = np.random.randn(5, 3)
7
pos_values = city_data[city_data > 0]
8
print("Cac gia tri > 0:", pos_values)
9
10
city_data[city_data > 0] = 0
11
print("Ma tran sau khi thay the:\n", city_data)

CHƯƠNG 4. XỬLÝ DỮLIỆU VỚI NUMPY VÀ PANDAS
(NUMPY & PANDAS)
15
4.1.4
Đại sốtuyến tính (Linear Algebra)
NumPy tích hợp thư viện linalg cung cấp các hàm mạnh mẽcho đại sốtuyến tính như tính
tích ma trận, ma trận nghịch đảo, giải hệphương trình tuyến tính, v.v.
1
A = np.array([[7, 5, -3],
2
[3, -5, 2],
3
[5, 3, -7]])
4
b = np.array([16, -8, 0])
5
6
7
x = np.linalg.solve(A, b)
8

print("Nghiem x, y, z:", x)
9
print("Kiem tra nghiem dung:", np.allclose(np.dot(A, x), b))
4.2
Thư viện Pandas - Xửlý và Phân tích Dữliệu
Pandas được xây dựng dựa trên NumPy, cung cấp các cấu trúc dữliệu linh hoạt là Series (1D)
và DataFrame (2D), đặc biệt phù hợp cho dữliệu dạng bảng.
4.2.1
Tạo và Đọc dữliệu
Pandas cung cấp hàm read_csv() đểđọc dữliệu từtệp CSV và các hàm như head(), tail()
đểquan sát dữliệu. Ngoài ra, ta có thểkhởi tạo DataFrame từDictionary hoặc List.
1
import pandas as pd
2
3
data_dict = [
4
{'city': 'Delhi', 'data': 1000},
5
{'city': 'Bangalore', 'data': 2000},
6
{'city': 'Mumbai', 'data': 1500}
7
]
8
df_dict = pd.DataFrame(data_dict)
9
10
data_list = [[1, 'Apple'], [2, 'Banana']]
11
df_list = pd.DataFrame(data_list , columns=['ID', 'Fruit'])
12
13
data_vnm = {
14
'Date': ['10-01-2023', '10-02-2023', '10-03-2023', '10-04-2023',
'10-05-2023', '10-06-2023', '10-07-2023'],
15
'Ticker': ['VNM', 'VNM', 'VNM', 'VNM', 'VNM', 'VNM', 'VNM'],
16
'Open': [75.5, 76.0, 75.8, 77.2, 76.5, 78.0, 77.8],
17
'Close': [76.0, 75.5, 77.0, 76.5, 78.0, 77.5, 78.2],
18
'Volume': [12000, 15000, 13500, 18000, 16000, 20000, 19500]

19
}
20
df_mock = pd.DataFrame(data_vnm)
21
22
23
df_mock.to_csv('vinamilk_stock.csv', index=False)

CHƯƠNG 4. XỬLÝ DỮLIỆU VỚI NUMPY VÀ PANDAS
(NUMPY & PANDAS)
16
24
print("Đã ạto thành công file 'vinamilk_stock.csv' trong ưth ụmc ệhin
ạti!")
25
26
df_stock = pd.read_csv('vinamilk_stock.csv')
27
28
print("--- 5 DONG DAU CUA DU LIEU ---")
29
print(df_stock.head())
30
31
print("\n--- 3 DONG CUOI CUA DU LIEU ---")
32
print(df_stock.tail(3))
Hình 4.2: Tạo và Đọc dữliệu với Pandas
4.2.2
Truy xuất & Điều kiện lọc dữliệu
Hai thuộc tính quan trọng đểtruy cập dữliệu trong Pandas là loc (theo nhãn) và iloc (theo vị
trí sốnguyên).
1
data_fict = {
2
'price': [100, 200, 300],
3
'quantity_purchased': [10, 20, 32],
4
'user_type': ['A', 'B', 'C'],
5
'user_class': ['X', 'Y', 'Z']
6

}
7
df = pd.DataFrame(data_fict)
8
print(df.iloc[:5, :4])
9
df_filtered = df.loc[df['quantity_purchased'] > 25]
4.2.3
Xửlý dữliệu khuyết & Thống kê mô tả
Pandas cung cấp các công cụđểphát hiện và xửlý dữliệu bịthiếu (NaN) cũng như các hàm để
mô tảnhanh bộdữliệu như describe() hay info().

CHƯƠNG 4. XỬLÝ DỮLIỆU VỚI NUMPY VÀ PANDAS
(NUMPY & PANDAS)
17
1
print(df.describe())
2
3
mean_price = df['price'].mean()
4
df['price'].fillna(value=mean_price , inplace=True)
4.2.4
Thay thếvà Áp dụng hàm
Các phương thức replace() và apply() là những công cụmạnh mẽđểthay đổi hoặc biến đổi
dữliệu trên cột.
1
df['user_type'] = df['user_type'].replace({'A': 'Premium', 'B': '
Standard'})
2
3
df['discounted_price'] = df['price'].apply(lambda x: x * 0.9)
4.2.5
Gom nhóm (GroupBy) & Gộp dữliệu (Concat/Merge)
Hàm groupby() rất hữu ích đểnhóm các dòng theo giá trịcủa một cột và thực hiện các phép
toán thống kê.
1
grouped = df.groupby('user_class')['quantity_purchased'].agg(['sum',
'mean', 'count'])
2
print(grouped)

Chương 5:

Tiền xửlý dữliệu
(Data Preprocessing)
Các thuật toán học máy (Machine Learning – ML) cổđiển như hồi quy tuyến tính, KNN, K-
Means, SVM hay PCA đều được xây dựng trên nền tảng đại sốtuyến tính và giải tích: chúng
nhận đầu vào là các vector sốthực và thực hiện phép cộng, phép nhân, phép tính khoảng cách
giữa các vector đó. Trong khi đó, dữliệu ngoài đời thực lại rất đa dạng: tên màu sắc, tên khu
phố, đoạn văn bản bình luận, mức đánh giá “tốt – trung bình – kém”, diện tích nhà tính bằng
feet vuông bên cạnh sốphòng tắm chỉtừ0 đến 4… Khoảng cách giữa “dữliệu thô” và “dữliệu
mà mô hình hiểu được” chính là đối tượng nghiên cứu của chương này.
Nguyên tắc cốt lõi: Mô hình ML không làm việc được trực tiếp trên văn bản hay
nhãn chữ— mọi thứđều phải được biến đổi thành số, và phải biến đổi sao cho
không làm sai lệch ý nghĩa của dữliệu.
Sau khi học xong chương này, người học có khảnăng:
• Trình bày được nguồn gốc lịch sửvà vịtrí của tiền xửlý dữliệu trong quy trình khai phá
tri thức (KDD) và CRISP-DM.
• Phân biệt các kiểu dữliệu (định danh, thứbậc, số, văn bản) và chọn phép biến đổi phù
hợp cho từng kiểu.
• Xửlý dữliệu thiếu bằng Simple Imputer, KNN Imputer (khoảng cách nan-Euclid)
và Iterative Imputer; phát hiện ngoại lai bằng z-score, quy tắc IQR và Local Outlier
Factor.
• Mã hóa dữliệu phân loại bằng Label Encoder và One Hot Encoder, hiểu rõ ưu nhược
điểm của từng cách.
• Vector hóa văn bản bằng Count Vectorizer và TF-IDF Vectorizer, tựtính tay được ma
trận TF-IDF.
• Chuẩn hóa thang đo đặc trưng bằng Min Max Scaler, Max Abs Scaler, Standard Scaler
và Robust Scaler.
• Xửlý dữliệu mất cân bằng bằng SMOTE và đặt bước lấy mẫu đúng vịtrí trong pipeline.
• Xây dựng quy trình tiền xửlý hoàn chỉnh, tránh rò rỉdữliệu, trên bộdữliệu thực tếAmes
Housing.
18

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
19
5.1
Khởi nguồn và vai trò của tiền xửlý dữliệu
5.1.1
“Rác vào, rác ra”
Ngay từnhững ngày đầu của ngành máy tính, giới lập trình viên đã lưu truyền nguyên lý Garbage
In, Garbage Out (GIGO – “rác vào, rác ra”), thường được gán cho George Fuechsel, một kỹsư
IBM vào cuối thập niên 1950. Nguyên lý này nói rằng một chương trình dù đúng đến đâu cũng
chỉcho ra kết quảtốt khi dữliệu đầu vào tốt. Đối với học máy, nguyên lý này còn nghiêm trọng
hơn: mô hình học trực tiếp từdữliệu, nên mọi sai lệch, nhiễu hay cách mã hóa không phù hợp
đều được mô hình “học thuộc” và khuếch đại thành dựđoán sai.

5.1.2
Tiền xửlý trong quy trình khai phá tri thức (KDD)
Năm 1996, Fayyad, Piatetsky-Shapiro và Smyth công bốbài báo kinh điển From Data Mining
to Knowledge Discovery in Databases trên tạp chí AI Magazine, chính thức hóa quy trình khám
phá tri thức từcơ sởdữliệu (Knowledge Discovery in Databases – KDD). Trong quy trình
này, “khai phá dữliệu” (tức bước chạy thuật toán) chỉlà một bước, đứng sau hàng loạt bước
chuẩn bị:
1. Lựa chọn (Selection): chọn tập dữliệu, biến quan tâm.
2. Tiền xửlý (Preprocessing): làm sạch, xửlý nhiễu, xửlý giá trịthiếu.
3. Biến đổi (Transformation): mã hóa, chuẩn hóa, giảm chiều.
4. Khai phá dữliệu (Data Mining): áp dụng thuật toán.
5. Diễn giải / Đánh giá (Interpretation/Evaluation).
[Chỗchèn hình]
images/ch-preprocessing-kdd.jpg
Hình
5.1:
Quy
trình
KDD
theo
Fayyad
và
cộng
sự
(1996).
Tiền
xử
lý
và
biến
đổi
dữ
liệu
đứng
trước
bước
khai
phá
dữ
liệu.(https://onlinelibrary.wiley.com/doi/epdf/10.1609/aimag.v17i3.1230)
Cùng thời điểm, một liên minh công nghiệp gồm DaimlerChrysler, SPSS và NCR phát triển
chuẩn CRISP-DM (Cross-Industry Standard Process for Data Mining, công bốbản 1.0 năm
2000) gồm sáu pha: Hiểu nghiệp vụ– Hiểu dữliệu – Chuẩn bịdữliệu – Mô hình hóa – Đánh
giá – Triển khai. Pha Chuẩn bịdữliệu được nhiều tài liệu thực hành ước tính chiếm phần lớn thời
gian của một dựán (con sốthường được trích dẫn là khoảng 60–80%). Cuốn Data Preparation
<!-- page: 1 -->
# VI_PY_073: Cấu trúc dữ liệu nâng cao phục vụ phân tích dữ liệu lớn

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân  
**Chuyên mục**: Cấu trúc dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 27 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
21
Phương thức
Ý nghĩa
fit(X)
Học các tham sốtừdữliệu (từđiển nhãn, min/max, trung
bình, độlệch chuẩn…).
transform(X)
Áp dụng các tham sốđã học đểbiến đổi dữliệu.
fit_transform(X)
Gộp hai bước trên (chỉdùng trên tập huấn luyện).
inverse_transform(X)
Biến đổi ngược vềgiá trịgốc (khi phép biến đổi khảnghịch).
Bảng 5.2: Giao diện chung của các bộbiến đổi trong scikit-learn
Định nghĩa 5.1 (Rò rỉdữliệu – Data leakage). Rò rỉdữliệu xảy ra khi thông tin từtập kiểm tra
(test) được sửdụng, trực tiếp hay gián tiếp, trong quá trình huấn luyện. Với tiền xửlý, lỗi điển
hình là gọi fit trên toàn bộdữliệu trước khi chia train/test. Quy tắc đúng: chỉfit trên tập
huấn luyện, sau đó dùng transform cho cảtập huấn luyện và tập kiểm tra.
5.2
Các kiểu dữliệu và lựa chọn phép biến đổi
Trước khi chọn kỹthuật, cần xác định thang đo của từng biến. Stevens (1946) phân biệt bốn
thang đo: định danh (nominal), thứbậc (ordinal), khoảng (interval) và tỉlệ(ratio). Trong thực
hành ML, ta gom thành các nhóm sau:
Kiểu dữliệu
Đặc điểm
Ví dụ
Phép biến đổi
Định
danh
(nominal)
Các giá trịchỉkhác nhau,
không có thứtự
màu sắc, khu phố

<!-- page: 2 -->

One Hot Encoder
Thứ
bậc
(ordinal)
Có thứtựnhưng khoảng
cách không rõ ràng
kém < TB < tốt
Ordinal Encoder
Nhãn
đầu
ra
(target)
Biến cần dựđoán trong
phân lớp
“spam”/“ham”
Label Encoder
Số(numeric)
Có giá trịvà khoảng cách
thực
diện tích, giá
Các Scaler
Văn bản (text)
Chuỗi từcó độdài thay
đổi
bình luận, tài liệu
Count
/
TF-IDF
Vectorizer
Bảng 5.3: Kiểu dữliệu và kỹthuật tiền xửlý tương ứng
5.3
Xửlý dữliệu thiếu (Missing Values)
Dữliệu thiếu xuất hiện trong hầu hết các bộdữliệu thực tế: người được khảo sát bỏtrống câu
hỏi, cảm biến mất tín hiệu, dữliệu ghép từnhiều nguồn không khớp nhau… Trong NumPy và
pandas, giá trịthiếu được biểu diễn bằng NaN (Not a Number — một giá trịđặc biệt của chuẩn
sốthực dấu phẩy động IEEE 754). Phần lớn mô hình của scikit-learn (hồi quy tuyến tính, SVM,
KNN, PCA…) sẽbáo lỗi khi gặp NaN, vì vậy xửlý dữliệu thiếu là bước bắt buộc trước khi huấn
luyện.

<!-- page: 28 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
22
5.3.1
Cơ chếsinh dữliệu thiếu

<!-- page: 3 -->

Donald Rubin (1976) đặt nền móng lý thuyết cho bài toán dữliệu thiếu khi phân biệt ba cơ chế
thiếu:
Cơ chế
Ý nghĩa
Ví dụ
MCAR
–
Missing
Completely
At
Random
Việc thiếu hoàn toàn ngẫu nhiên,
không phụthuộc vào biến nào
Phiếu khảo sát bịthất lạc
ngẫu nhiên
MAR – Missing At
Random
Việc thiếu chỉphụthuộc vào các
biến quan sát được
Người trẻít khai thu nhập
hơn (tuổi đã biết)
MNAR
–
Missing
Not At Random
Việc thiếu phụthuộc vào chính
giá trịbịthiếu
Người thu nhập rất cao từ
chối khai thu nhập
Bảng 5.4: Ba cơ chếthiếu dữliệu theo Rubin (1976)
Xóa các dòng có ô trống (df.dropna()) chỉan toàn khi dữliệu thiếu kiểu MCAR và chiếm
tỉlệnhỏ; trong các trường hợp còn lại, xóa dòng vừa lãng phí dữliệu vừa làm lệch mẫu. Giải
pháp phổbiến hơn là điền giá trịthiếu (imputation). scikit-learn cung cấp ba bộđiền với mức
độphức tạp tăng dần: SimpleImputer, KNNImputer và IterativeImputer. Giống mọi bộ
biến đổi khác, bộđiền phải được fit chỉtrên tập huấn luyện.
5.3.2
Simple Imputer: trung bình, trung vị, giá trịphổbiến
Cách đơn giản nhất là thay mọi ô thiếu của một cột bằng một thống kê của chính cột đó, tính
trên các giá trịquan sát được:
• strategy="mean" – trung bình cộng: phù hợp với dữliệu gần đối xứng, ít ngoại lai.
• strategy="median" – trung vị: bền vững với ngoại lai và dữliệu lệch.
• strategy="most_frequent" – giá trịxuất hiện nhiều nhất (mode): dùng được cho cả
cột chữ.
• strategy="constant" – một hằng sốdo người dùng chọn (ví dụ"NA" hoặc 0).
Ví dụ5.1 (Điền bằng trung bình và trung vị). Hai cột dữliệu, mỗi cột thiếu một giá trị:

<!-- page: 4 -->

A = (7, 3, 4, 6, 2, ?),
B = (6, 8, 9, 8, 7, ?).
Cách 1 – theo trung bình:
¯A = 7 + 3 + 4 + 6 + 2
5
= 22
5 = 4,4,
¯B = 6 + 8 + 9 + 8 + 7
5
= 38
5 = 7,6.
Cách 2 – theo trung vị: sắp xếp các giá trịquan sát được rồi chọn phần tửởgiữa: A →
(2, 3, 4, 6, 7), điền 4;
B →(6, 7, 8, 8, 9), điền 8.
Khi sốgiá trịquan sát được là chẵn, trung vịlà trung bình cộng của hai phần tửởgiữa. Ví
dụvới (6, 9, 7, 3, 2, 5): sắp xếp thành (2, 3, 5, 6, 7, 9), trung vịbằng 5+6
2
= 5,5.

<!-- page: 29 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
23
Listing 5.1: SimpleImputer với ví dụtrên
1
import numpy as np
2
from sklearn.impute import SimpleImputer
3
4
X = np.array([[7, 6], [3, 8], [4, 9], [6, 8], [2, 7], [np.nan, np.nan
]])
5
for s in ["mean", "median", "most_frequent"]:
6
imp = SimpleImputer(strategy=s).fit(X)
7
print(s, imp.statistics_)
8
# mean
[4.4 7.6]
9
# median
[4.
8. ]

<!-- page: 5 -->

10
# most_frequent [2.
8. ]
(cot A khong co gia tri lap -> lay gia tri
nho nhat)
11
print(np.median([6, 9, 7, 3, 2, 5]))
# 5.5
Hạn chế.
Điền bằng một hằng sốlàm giảm phương sai của cột và làm yếu tương quan giữa
các cột, vì mọi ô thiếu nhận cùng một giá trịbất kểcác thuộc tính còn lại của bản ghi. Tham số
add_indicator=True bổsung cột nhịphân đánh dấu ô nào đã được điền — bản thân sựkiện
“bịthiếu” nhiều khi cũng mang thông tin có ích cho mô hình.
5.3.3
KNN Imputer và khoảng cách nan-Euclid
Troyanskaya và cộng sự(2001) đềxuất điền giá trịthiếu trong dữliệu biểu hiện gen bằng các
láng giềng gần nhất: hai bản ghi giống nhau ởcác cột quan sát được thì nhiều khảnăng cũng
giống nhau ởcột bịthiếu. Thuật toán KNN được trình bày đầy đủởChương 7; ởđây chỉcần ý
tưởng: giá trịđiền là trung bình của cột đó trên k bản ghi gần nhất.
Khó khăn là chính các bản ghi cũng có ô trống, nên không tính được khoảng cách Euclid
thông thường. Ta dùng khoảng cách nan-Euclid: chỉcộng trên những tọa độmà cảhai điểm
đều có giá trị, rồi nhân với một hệsốđểbù cho các tọa độbịbỏqua.
Định nghĩa 5.2 (Khoảng cách nan-Euclid). Với hai vector x, y ∈Rd có thểchứa giá trịthiếu,
gọi P là tập các tọa độmà cảhai vector cùng có giá trị:
dnan(x, y) =
s
d
|P|
X
j∈P
(xj −yj)2,
(5.1)
trong đó d là tổng sốchiều của bài toán và |P| là sốchiều tính được.
Ví dụ5.2 (Tính khoảng cách nan-Euclid).
• x = (5, nan) và y = (4, 5): chỉtọa độthứnhất
tính được, d = 2, |P| = 1:
dnan =
q
2
1(5 −4)2 =
√
2 ≈1,414.
• A = (3, nan, nan, 6) và B = (1, nan, 4, 5): tính được tọa độ1 và 4, d = 4, |P| = 2:
dnan =
q

<!-- page: 6 -->

4
2

(3 −1)2 + (6 −5)2
=
√
10 ≈3,162.
Ví dụ5.3 (Chạy tay KNN Imputer với k = 3). Điền ba ô thiếu trong Bảng 5.5.

<!-- page: 30 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
24
STT
x1
x2
x3
1
7
6
4
2
?
4
5
3
1
5
?
4
3
9
7
5
8
?
8
Bảng 5.5: Dữliệu ví dụcho KNN Imputer
Bước 1 – xác định X và y. Đểđiền x1 ởdòng 2, coi cột x1 là “nhãn” y, hai cột còn lại (x2, x3)
là đặc trưng X. Điểm cần dựđoán là q = (4, 5); các dòng được làm láng giềng phải có giá trị
x1 (dòng 1, 3, 4, 5).
Bước 2 – tính khoảng cách nan-Euclid trên hai cột (x2, x3), d = 2:
d(q, dòng 1) =
p
(4 −6)2 + (5 −4)2 =

<!-- page: 7 -->

√
5 ≈2,236,
d(q, dòng 3) =
q
2
1(4 −5)2 =
√
2 ≈1,414
(dòng 3 thiếu x3),
d(q, dòng 4) =
p
(4 −9)2 + (5 −7)2 =
√
29 ≈5,385,
d(q, dòng 5) =
q
2
1(5 −8)2 =
√
18 ≈4,243
(dòng 5 thiếu x2).
Bước 3 – lấy trung bình của k = 3 láng giềng gần nhất (dòng 3, 1, 5): x1 = 1+7+8
3
≈5,333.
Làm tương tựcho hai ô còn lại, ta được bảng tổng hợp:
Ô
cần
điền
Điểm q
Khoảng cách đến các dòng
3
láng
giềng
Giá trịđiền
x1, dòng 2
(x2, x3)
=
(4, 5)
d1 = 2,236; d3 = 1,414; d4 =
5,385; d5 = 4,243
3, 1, 5
1+7+8
3
≈5,333
x3, dòng 3

<!-- page: 8 -->

(x1, x2)
=
(1, 5)
d1 = 6,083; d2 = 1,414; d4 =
4,472; d5 = 9,899
2, 4, 1
5+7+4
3
≈5,333
x2, dòng 5
(x1, x3)
=
(8, 8)
d1 = 4,123; d2 = 4,243; d3 =
9,899; d4 = 5,099
1, 2, 4
6+4+9
3
≈6,333
Bảng 5.6: Kết quảchạy tay KNN Imputer (k = 3)
Lưu ý.
• Hệsốd/|P| phải được áp dụng mỗi khi có tọa độbịthiếu. Quên hệsốnày — chẳng hạn
viết d(q, dòng 5) =
p
(5 −8)2 = 3 thay vì
√
18 ≈4,243 — là lỗi hay gặp khi tính tay. Ở
ví dụnày lỗi đó tình cờkhông làm đổi tập láng giềng, nhưng trong trường hợp tổng quát
sẽcho kết quảsai.
• KNNImputer của scikit-learn đo khoảng cách trên toàn bộ3 cột. Tọa độđang cần điền
của dòng nhận vốn bịthiếu nên tựđộng bịloại, và hệsốtrởthành 3/|P| thay vì 2/|P|.
Mọi khoảng cách từdòng nhận vì thếcùng được nhân với
p
3/2, nên thứtựláng giềng
và giá trịđiền không đổi.
• KNN Imputer dựa trên khoảng cách nên cần chuẩn hóa thang đo (mục 5.7) trước khi
dùng; tham sốweights="distance" cho láng giềng gần hơn trọng sốlớn hơn.

<!-- page: 31 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
25
Listing 5.2: Khoảng cách nan-Euclid và KNNImputer
1
import numpy as np

<!-- page: 9 -->

2
from sklearn.impute import KNNImputer
3
from sklearn.metrics.pairwise import nan_euclidean_distances
4
5
nan = np.nan
6
print(nan_euclidean_distances([[5, nan]], [[4, 5]]))
# [[1.4142]]
7
print(nan_euclidean_distances([[3, nan, nan, 6]], [[1, nan, 4, 5]]))
# [[3.1623]]
8
9
X = np.array([[7, 6, 4], [nan, 4, 5], [1, 5, nan], [3, 9, 7], [8, nan
, 8]])
10
print(KNNImputer(n_neighbors=3).fit_transform(X).round(3))
11
# [[7.
6.
4.
]
12
#
[5.333 4.
5.
]
13
#
[1.
5.
5.333]
14
#
[3.
9.
7.
]
15
#
[8.
6.333 8.
]]

<!-- page: 10 -->

5.3.4
Iterative Imputer
Simple Imputer bỏqua quan hệgiữa các cột; KNN Imputer khai thác quan hệđó một cách cục
bộ. Iterative Imputer đi xa hơn: mô hình hóa mỗi cột có giá trịthiếu như một hàm hồi quy của
các cột còn lại. Ý tưởng này bắt nguồn từkỹthuật MICE (Multivariate Imputation by Chained
Equations) của van Buuren và Groothuis-Oudshoorn (2011), vốn phát triển từkhung điền khuyết
bội (multiple imputation) của Rubin (1987). Trong scikit-learn, lớp IterativeImputer vẫn
được xếp vào nhóm thửnghiệm, nên cần khai báo from sklearn.experimental import
enable_iterative_imputer trước khi dùng.
Thuật toán:
1. Khởi tạo: điền tạm mọi ô thiếu bằng trung bình cột.
2. Lần lượt với từng cột xj có ô thiếu: coi xj là biến mục tiêu y, các cột còn lại (với giá trị
đang điền tạm) là X; huấn luyện mô hình hồi quy trên các dòng mà xj được quan sát; dự
đoán và cập nhật các ô thiếu của xj.
3. Lặp lại bước 2 cho đến khi các giá trịđiền ổn định hoặc đạt sốvòng tối đa max_iter.
Bộhồi quy ởbước 2 có thểlà bất kỳmô hình nào. Trong ví dụdưới đây ta dùng hồi quy
tuyến tính, giải bằng phương trình chuẩn β = (X⊤X)−1X⊤y (Chương ??); cột đầu tiên của X
toàn số1 ứng với hệsốchặn β0.
Ví dụ5.4 (Chạy tay một vòng Iterative Imputer). Điền ba ô thiếu trong Bảng 5.7 theo thứtự
cột x1 →x2 →x3.

<!-- page: 32 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
26
STT
x1
x2
x3
1
3
7
1
2
?
4
8
3
6
3
7
4
5
?
4

<!-- page: 11 -->

5
1
9
?
Bảng 5.7: Dữliệu ví dụcho Iterative Imputer
Bước 1 – khởi tạo bằng trung bình cột:
¯x1 = 3 + 6 + 5 + 1
4
= 3,75,
¯x2 = 7 + 4 + 3 + 9
4
= 5,75,
¯x3 = 1 + 8 + 7 + 4
4
= 5.
Bước 2 – dựđoán x1 từ(x2, x3). Dùng bốn dòng có x1 (dòng 4 đang mang giá trịtạm x2 = 5,75,
dòng 5 mang x3 = 5):
X =




1
7
1
1
3
7
1
5,75
4
1
9
5



,
y =




3
6

<!-- page: 12 -->

5
1



,
X⊤X =


4
24,75
17
24,75
172,06
96
17
96
91

,
X⊤y =


15
76,75
70

,
(X⊤X)−1 ≈


5,9563
−0,5735
−0,5077
−0,5735
0,0693
0,0340
−0,5077
0,0340
0,0700

,
β = (X⊤X)−1X⊤y ≈



<!-- page: 13 -->

9,78895
−0,90153
−0,10841

.
Thay dòng 2 (x2 = 4, x3 = 8): x1 = 9,78895 −0,90153 × 4 −0,10841 × 8 ≈5,3155.
Bước 3 – dựđoán x2 từ(x1, x3), thếgiá trịvừa điền x1 = 5,3155 vào dòng 2 (dòng 5 vẫn mang
x3 = 5):
X =




1
3
1
1
5,3155
8
1
6
7
1
1
5



,
y =




7
4
3
9



⇒β ≈


10,4972

<!-- page: 14 -->

−1,1578
−0,0598

.
Thay dòng 4 (x1 = 5, x3 = 4): x2 = 10,4972 −1,1578 × 5 −0,0598 × 4 ≈4,469.
Bước 4 – dựđoán x3 từ(x1, x2) với các giá trịvừa điền (tính với đầy đủchữsố):
X =




1
3
7
1
5,3155
4
1
6
3
1
5
4,4689



,
y =




1
8
7
4



⇒β ≈


9,7807
0,3487
−1,4001

<!-- page: 15 -->


.
Thay dòng 5 (x1 = 1, x2 = 9): x3 = 9,7807 + 0,3487 × 1 −1,4001 × 9 ≈−2,47.
Kết thúc vòng thứnhất: x1 ≈5,32; x2 ≈4,47; x3 ≈−2,47.
Phân tích kết quả: bài toán điều kiện xấu.
Giá trịx3 ≈−2,47 nằm ngoài miền quan sát
[1; 8] của cột x3 — một dấu hiệu cảnh báo. Nguyên nhân nằm ởbốn dòng dùng đểhồi quy ở
bước 4: tổng x1 +x2 của chúng lần lượt là 10; 9,32; 9; 9,47, tức hai đặc trưng gần như phụthuộc
tuyến tính (đa cộng tuyến). Khi đó X⊤X gần suy biến: sốđiều kiện của nó vào khoảng 1,8×106
và phần tửlớn nhất của (X⊤X)−1 lên tới khoảng 9505. Hệquảlà nghiệm cực kỳnhạy với sai số
làm tròn ởcác bước trước:

<!-- page: 33 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
27
x1 (dòng 2)
x2 (dòng 4)
β0
β1
β2
x3 (dòng 5)
5,31553… (đủchữsố)
4,46889…
9,781
0,349
−1,400
−2,47
5,316
4,469
8,852
0,460
−1,316
−2,53
5,32
4,47
1,242
1,375
−0,624
−3,00
5,306
4,47
32,894
−2,430
−3,501

<!-- page: 16 -->

−1,04
5,3445
4,47
−41,058
6,445
3,224
−5,59
Bảng 5.8: Độnhạy của bước 4 khi các giá trịđiền trước đó bịlàm tròn
Chỉcần x1 lệch 0,01 là hệsốchặn β0 đã nhảy từkhoảng 9,8 lên 32,9 hay xuống −41. Vì vậy,
khi tính tay mỗi người làm tròn một kiểu sẽcho những hệsốrất khác nhau, dù không ai tính
sai phép tính. Lặp thêm nhiều vòng cũng không giúp gì: với max_iter=10, giá trịđiền của x3
còn trôi tới khoảng −28,5.
Bài học thực hành:
1. Luôn kiểm tra tính hợp lý của giá trịđược điền (so với miền quan sát, ý nghĩa nghiệp
vụ).
2. Giới hạn miền giá trịbằng min_value, max_value.
3. Ưu tiên bộhồi quy có điều chuẩn — mặc định của IterativeImputer là BayesianRidge
— vì hệsốổn định hơn khi có đa cộng tuyến (xem Ridge ởChương ??). Tuy vậy, điều
chuẩn không thay thếđược bước kiểm tra: trên chính ví dụnày, BayesianRidge không
giới hạn miền vẫn cho x3 ≈−2,51.
4. Chỉdùng Iterative Imputer khi có đủdữliệu đểước lượng quan hệgiữa các cột; với bốn
dòng như ví dụ, Simple Imputer hoặc KNN Imputer an toàn hơn.
Listing 5.3: IterativeImputer tái hiện ví dụtính tay
1
import numpy as np
2
from sklearn.experimental import enable_iterative_imputer
# bat tinh
nang thu nghiem
3
from sklearn.impute import IterativeImputer
4
from sklearn.linear_model import LinearRegression
5
6
nan = np.nan
7
X = np.array([[3, 7, 1], [nan, 4, 8], [6, 3, 7], [5, nan, 4], [1, 9,
nan]])
8
9
# Mot vong, hoi quy tuyen tinh, thu tu cot x1 -> x2 -> x3 (giong tinh
tay)
10
imp = IterativeImputer(estimator=LinearRegression(), initial_strategy

<!-- page: 17 -->

="mean",
11
imputation_order="roman", max_iter=1)
12
print(imp.fit_transform(X).round(4))
13
# dong 2: x1 = 5.3155 ; dong 4: x2 = 4.4689 ; dong 5: x3 = -2.4715
14
15
# Mac dinh BayesianRidge , 10 vong, gioi han mien gia tri theo du lieu
quan sat
16
lo, hi = np.nanmin(X, axis=0), np.nanmax(X, axis=0)

<!-- page: 34 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
28
17
imp = IterativeImputer(max_iter=10, min_value=lo, max_value=hi,
random_state=0)
18
print(imp.fit_transform(X).round(3))
19
# dong 2: x1 = 4.833 ; dong 4: x2 = 4.5 ; dong 5: x3 = 1.0 (bi chan
duoi)
Bộđiền
Ý tưởng
Ưu điểm
Nhược điểm
SimpleImputer
Thống kê của chính
cột
(mean,
median,
mode)
Nhanh, đơn giản,
ổn định
Bỏqua quan hệgiữa
các cột; làm giảm
phương sai
KNNImputer
Trung bình của k láng
giềng
theo

<!-- page: 18 -->

khoảng
cách nan-Euclid
Tận
dụng
sự
tương đồng giữa
các bản ghi
Chậm với dữliệu lớn;
cần chuẩn hóa thang
đo
IterativeImputer
Hồi quy lặp từng cột
theo các cột còn lại
(MICE)
Khai thác quan hệ
đa biến
Chậm; có thểngoại
suy phi thực tế; cần
kiểm tra kết quả
Bảng 5.9: So sánh ba bộđiền giá trịthiếu
5.4
Phát hiện ngoại lai (Outlier Detection)
Theo định nghĩa kinh điển của Hawkins (1980), ngoại lai (outlier) là “một quan sát lệch khỏi
các quan sát khác nhiều đến mức gợi nghi ngờrằng nó được sinh ra bởi một cơ chếkhác”.
Ngoại lai có thểlà lỗi nhập liệu (năm xây garage 2207 trong Ames Housing), lỗi đo đạc, hoặc
là hiện tượng có thật nhưng hiếm (một giao dịch gian lận). Vì vậy phát hiện và xửlý là hai
quyết định khác nhau: chỉloại bỏkhi chắc chắn đó là lỗi; trong các trường hợp khác có thểgiữ
nguyên, biến đổi (lấy logarit), cắt ngưỡng (winsorizing), hoặc dùng mô hình và bộchuẩn hóa
bền vững như RobustScaler.
5.4.1
Phương pháp một biến: z-score và quy tắc IQR
Quy tắc z-score.
Coi điểm có |z| = |x −¯x|/s > 3 là ngoại lai. Điểm yếu của quy tắc này
là chính ngoại lai kéo lệch ¯x và làm s phình to (hiệu ứng che lấp – masking). Với cột x =
(2, 4, 6, 8, 30) sẽdùng lại ởmục 5.7: ¯x = 10, s = 10,20 nên z(30) = 1,96 < 3 — giá trị30
không bịphát hiện. Thực ra có thểchứng minh |z| ≤√n −1 (Shiffler, 1988), nên với n = 5
không quan sát nào có thểvượt ngưỡng 3.
Quy tắc IQR (Tukey, 1977).
Dựa trên các tứphân vịQ1, Q3 và khoảng tứphân vịIQR =
Q3 −Q1; điểm nằm ngoài khoảng

Q1 −1,5 IQR, Q3 + 1,5 IQR

(5.2)
là ngoại lai — đây cũng chính là “râu” của biểu đồhộp (boxplot). Với cùng dữliệu: Q1 = 4,

<!-- page: 19 -->

Q3 = 8, IQR = 4, khoảng hợp lệlà [−2; 14], nên 30 bịphát hiện. Tứphân vịbền vững với
ngoại lai nên quy tắc IQR không bịche lấp.
Listing 5.4: z-score và quy tắc IQR

<!-- page: 35 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
29
1
import numpy as np
2
3
x = np.array([2, 4, 6, 8, 30])
4
z = (x - x.mean()) / x.std()
5
print(z.round(2))
# [-0.78
-0.59 -0.39 -0.2
1.96]
6
q1, q3 = np.percentile(x, [25, 75]); iqr = q3 - q1
7
print(x[(x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)])
# [30]
5.4.2
Phương pháp nhiều biến: Local Outlier Factor (LOF)
Trong không gian nhiều chiều, một điểm có thể“bình thường” trên từng biến riêng lẻnhưng bất
thường khi xét đồng thời. Breunig, Kriegel, Ng và Sander (2000) đềxuất LOF (Local Outlier
Factor): so sánh mật độcục bộcủa một điểm với mật độcủa các láng giềng; điểm nằm trong
vùng thưa hơn hẳn các láng giềng của nó là ngoại lai. LOF cùng tư tưởng “dựa trên mật độ” với
thuật toán phân cụm DBSCAN (Chương 9); hai công trình có chung hai tác giảlà Hans-Peter
Kriegel và Jörg Sander.
Định nghĩa 5.3 (Các đại lượng của LOF). Với sốláng giềng k và Nk(p) là tập k láng giềng gần
nhất của điểm p:
• k-khoảng cách: k-dist(p) là khoảng cách từp đến láng giềng thứk của nó.
• Khoảng cách tiếp cận (reachability distance):
reach-distk(p, o) = max{k-dist(o), d(p, o)}.
• Mật độtiếp cận cục bộ(local reachability density):
lrdk(p) =

1
k
X
o∈Nk(p)

<!-- page: 20 -->

reach-distk(p, o)


−1
.
• Hệsốngoại lai cục bộ:
LOFk(p) = 1
k
X
o∈Nk(p)
lrdk(o)
lrdk(p).
LOF ≈1: mật độtương đương các láng giềng (điểm bình thường); LOF ≫1: điểm thưa hơn
hẳn láng giềng (ngoại lai).
Phép lấy max trong khoảng cách tiếp cận có tác dụng làm trơn: các điểm nằm sâu trong
cùng một cụm dày đặc có khoảng cách tiếp cận bằng nhau, nhờđó LOF không dao động vì
những chênh lệch khoảng cách rất nhỏ.
Ví dụ5.5 (Tính tay LOF với k = 3). Cho 5 điểm A(0, 0), B(1, 0), C(0, 1), D(1, 1) và E(5, 4)
với ma trận khoảng cách Euclid trong Bảng 5.10.

<!-- page: 36 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
30
A
B
C
D
E
A
0
1
1
1,414
6,403
B
1
0
1,414
1
5,657
C
1
1,414
0

<!-- page: 21 -->

1
5,831
D
1,414
1
1
0
5
E
6,403
5,657
5,831
5
0
Bảng 5.10: Khoảng cách giữa 5 điểm của ví dụLOF
Bước 1 – k-khoảng cách. Mỗi điểm A, B, C, D có hai láng giềng ởkhoảng cách 1 và một láng
giềng ởkhoảng cách
√
2, nên k-dist = 1,414. Ba láng giềng của E là D, B, C, nên k-dist(E) =
5,831.
Bước 2 – khoảng cách tiếp cận. Chẳng hạn reach-dist(A, B) = max{k-dist(B), d(A, B)} =
max{1,414; 1} = 1,414: dù A chỉcách B một đơn vị, khoảng cách tiếp cận vẫn là 1,414. Với
E, các khoảng cách thật đều lớn hơn k-khoảng cách của láng giềng nên được giữnguyên.
Bước 3 – mật độvà hệsốLOF được tổng hợp trong Bảng 5.11.
Điểm
3 láng giềng
reach-dist
TB reach-dist
lrd
LOF
Nhãn
A
B, C, D
1,414; 1,414; 1,414
1,414
0,7071
1,000
1
B
A, D, C
1,414; 1,414; 1,414
1,414
0,7071
1,000
1

<!-- page: 22 -->

C
A, D, B
1,414; 1,414; 1,414
1,414
0,7071
1,000
1
D
B, C, A
1,414; 1,414; 1,414
1,414
0,7071
1,000
1
E
D, B, C
5; 5,657; 5,831
5,496
0,1820
3,886
−1
Bảng 5.11: Bảng tính LOF (k = 3); nhãn theo quy ước của scikit-learn: 1 là điểm bình thường,
−1 là ngoại lai
Chẳng hạn LOF(E) = (0,7071 + 0,7071 + 0,7071)/3
0,1820
≈3,886 ≫1, nên E là ngoại lai; các
điểm còn lại có LOF = 1. Với contamination="auto", scikit-learn coi điểm có LOF > 1,5
là ngoại lai.
[Chỗchèn hình]
images/ch-preprocessing-lof.png
Hình 5.3: Minh họa LOF: bốn điểm A, B, C, D tạo thành vùng dày đặc; điểm E nằm trong vùng
thưa với LOF ≈3,89.
Listing 5.5: Local Outlier Factor với scikit-learn
1
import numpy as np

<!-- page: 37 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
31
2
from sklearn.neighbors import LocalOutlierFactor
3
4
X = np.array([[0, 0], [1, 0], [0, 1], [1, 1], [5, 4]])

<!-- page: 23 -->

5
lof = LocalOutlierFactor(n_neighbors=3)
6
print(lof.fit_predict(X))
# [ 1
1
1
1 -1]
7
print(-lof.negative_outlier_factor_.round(4))
# [1.
1.
1.
1.
3.8862]
Đểphát hiện ngoại lai trên dữliệu mới (sau khi đã huấn luyện), đặt tham sốnovelty=True
cho LocalOutlierFactor. Một lựa chọn khác mởrộng tốt cho dữliệu lớn là IsolationForest
(Liu, Ting & Zhou, 2008): ngoại lai là những điểm bịcô lập sau rất ít lần chia ngẫu nhiên.
5.5
Mã hóa dữliệu phân loại
5.5.1
Label Encoder
Định nghĩa 5.4 (Label Encoding). Cho tập K nhãn phân biệt C = {c0, c1, . . . , cK−1}. Label
Encoding là một song ánh
ϕ : C →{0, 1, . . . , K −1},
ϕ(ck) = k,
(5.3)
gán cho mỗi nhãn một sốnguyên duy nhất. Kết quảlà một từđiển (dictionary) ánh xạnhãn →
số.
Ví dụ5.6. Cho dãy đầu vào gồm 7 phần tử: red, green, blue, red, green, red, orange.
Duyệt dãy từtrái sang phải, mỗi khi gặp một nhãn mới ta cấp cho nó sốtiếp theo:
Input
red
green
blue
red
green
red
orange
Output
0
1
2
0
1

<!-- page: 24 -->

0
3
Dictionary
red
0
green
1
blue
2
orange
3
Bảng 5.12: Label Encoding theo thứtựxuất hiện
[Chỗchèn hình]
images/ch-preprocessing-label-encoder.jpg
Hình 5.4: Minh họa Label Encoder trên bảng tính: dòng input, dòng output và từđiển ánh xạ.
Đểhiểu bản chất thuật toán, ta tựcài đặt Label Encoder chỉbằng các cấu trúc đã học ở
chương Python cơ bản: list, vòng lặp for và dictionary.

<!-- page: 38 -->
CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
32
Listing 5.6: Tựcài đặt Label Encoder bằng list, for và dictionary
1
data = ["red", "green", "blue", "red", "green", "red", "orange"]
2
3
# Buoc 1: xay dung tu dien nhan -> so (theo thu tu xuat hien)
4
dictionary = {}
5
for label in data:
6
if label not in dictionary:
7
dictionary[label] = len(dictionary)
8
print(dictionary)
9
# {'red': 0, 'green': 1, 'blue': 2, 'orange': 3}
10
11
# Buoc 2: ma hoa du lieu
12
encoded = [dictionary[label] for label in data]

<!-- page: 25 -->

13
print(encoded)
# [0, 1, 2, 0, 1, 0, 3]
14
15
# Buoc 3: giai ma (inverse) bang tu dien dao
16
inverse = {v: k for k, v in dictionary.items()}
17
print([inverse[v] for v in encoded])
Trong scikit-learn, lớp LabelEncoder làm việc tương tựnhưng có một điểm khác quan
trọng: các nhãn được sắp xếp theo thứtựtừđiển (alphabet) trước khi đánh số, chứkhông
theo thứtựxuất hiện.
Listing 5.7: Label Encoder với scikit-learn
1
from sklearn.preprocessing import LabelEncoder
2
3
data = ["red", "green", "blue", "red", "green", "red", "orange"]
4
le = LabelEncoder()
5
encoded = le.fit_transform(data)
6
7
print(le.classes_)
# ['blue' 'green' 'orange' 'red']
8
print(encoded)
# [3 1 0 3 1 3 2]
9
print(le.inverse_transform([0, 3]))
# ['blue' 'red']
Hạn chếcủa Label Encoder.
Label Encoder tạo ra một thứtựgiảgiữa các nhãn. Với từđiển
ởBảng 5.12, khoảng cách Euclid giữa các màu là:
d(red, green) = |0 −1| = 1,
d(red, orange) = |0 −3| = 3.
(5.4)
Nghĩa là mô hình sẽ“hiểu” rằng màu đỏgiống màu xanh lá hơn màu cam ba lần — một kết luận
hoàn toàn vô nghĩa, chỉxuất phát từviệc ta đánh sốtùy ý. Với các thuật toán dựa trên khoảng
cách như KNN, K-Means hoặc các mô hình tuyến tính, đây là nguồn sai lệch nghiêm trọng.
Lưu ý chuẩn mực: Trong scikit-learn, LabelEncoder được thiết kếđểmã hóa
biến mục tiêu y (nhãn lớp trong bài toán phân lớp). Với các đặc trưng đầu vào có
thứbậc, dùng OrdinalEncoder (cho phép tựkhai báo thứtự); với đặc trưng định

<!-- page: 26 -->

danh, dùng OneHotEncoder.
Listing 5.8: Ordinal Encoder với thứtựdo người dùng khai báo
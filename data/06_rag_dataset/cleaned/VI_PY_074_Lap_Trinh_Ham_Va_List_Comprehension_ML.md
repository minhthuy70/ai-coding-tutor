# VI_PY_074: Lập trình hàm, List Comprehension và tối ưu tốc độ xử lý

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân
**Chuyên mục**: Hàm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
34
[Chỗchèn hình]
images/ch-preprocessing-one-hot-encoder.jpg
Hình 5.5: Minh họa One Hot Encoder trên bảng tính: từđiển (Key – Value) và ma trận đầu ra;
ô được tô vàng là vịtrí số1 tương ứng với nhãn của từng hàng.
Listing 5.9: Tựcài đặt One Hot Encoder bằng list, for và dictionary
1
data = ["red", "blue", "red", "red", "blue",
2
"white", "red", "white", "orange"]
3
4
# Buoc 1: tu dien (Key -> Value)
5
dictionary = {}
6
for label in data:
7
if label not in dictionary:
8
dictionary[label] = len(dictionary)
9
K = len(dictionary)
# so cot = so nhan phan biet = 4
10
11
# Buoc 2: moi phan tu -> vector co dung mot so 1
12
one_hot = []
13
for label in data:
14

row = [0] * K
15
row[dictionary[label]] = 1
16
one_hot.append(row)
17
18
for i, row in enumerate(one_hot):
19
print(i, data[i], row)
20
# 0 red
[1, 0, 0, 0]
21
# 1 blue
[0, 1, 0, 0]
22
# ...
23
# 8 orange [0, 0, 0, 1]
Listing 5.10: One Hot Encoder với scikit-learn và pandas
1
import numpy as np
2
import pandas as pd
3
from sklearn.preprocessing import OneHotEncoder
4
5
data = np.array(["red", "blue", "red", "red", "blue",
6
"white", "red", "white", "orange"]).reshape(-1, 1)
7
8
ohe = OneHotEncoder(handle_unknown="ignore")
9
X = ohe.fit_transform(data)
# ket qua la ma tran thua (sparse)

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
35
10
print(ohe.get_feature_names_out())

11
# ['x0_blue' 'x0_orange' 'x0_red' 'x0_white']
(sap xep alphabet)
12
print(X.toarray()[:3])
13
# [[0. 0. 1. 0.]
14
#
[1. 0. 0. 0.]
15
#
[0. 0. 1. 0.]]
16
17
# Nhan moi chua tung gap -> vector toan 0 thay vi bao loi
18
print(ohe.transform([["green"]]).toarray())
# [[0. 0. 0. 0.]]
19
20
# Cach nhanh voi pandas
21
print(pd.get_dummies(pd.Series(data.ravel()), dtype=int).head(3))
Một sốvấn đềcần lưu ý.
• Bẫy biến giả(dummy variable trap): K cột one-hot luôn có tổng bằng 1, tức phụthuộc
tuyến tính hoàn toàn với cột hệsốchặn. Với hồi quy tuyến tính không chính quy hóa,
nên bỏmột cột bằng OneHotEncoder(drop="first") hoặc pd.get_dummies(...,
drop_first=True).
• Bùng nổsốchiều: biến có hàng nghìn giá trị(mã bưu chính, mã sản phẩm) sinh ra hàng
nghìn cột. Khi đó cần gộp các nhãn hiếm, dùng ma trận thưa hoặc các kỹthuật như target
encoding, hashing.
• Nhãn chưa từng gặp ởtập kiểm tra: dùng handle_unknown="ignore" đểtránh lỗi khi
triển khai.
Tiêu chí
Label / Ordinal Encoder
One Hot Encoder
Sốcột sinh ra
1
K (sốnhãn)
Tạo thứtựgiả
Có
Không
Phù hợp với
Biến mục tiêu; đặc trưng

thứbậc; mô hình cây
Đặc trưng định danh; KNN,
K-Means, SVM, mô hình
tuyến tính
Nhược điểm
Sai lệch khoảng cách
Tăng sốchiều, ma trận thưa
Bảng 5.14: So sánh Label Encoder và One Hot Encoder
5.6
Vector hóa văn bản
5.6.1
Mô hình túi từvà Count Vectorizer
Ý tưởng biểu diễn một văn bản bằng tần suất các từcó từrất sớm: nhà ngôn ngữhọc Zellig
Harris (1954) trong Distributional Structure đã nhắc đến “túi từ” (bag of words), và Hans Peter
Luhn (1957) tại IBM đềxuất dùng tần suất từđểđánh chỉmục tài liệu tựđộng. Năm 1975,
Salton, Wong và Yang hệthống hóa thành mô hình không gian vector (Vector Space Model):
mỗi văn bản là một vector trong không gian có sốchiều bằng kích thước từvựng.

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
36
Định nghĩa 5.6 (Count Vectorizer). Cho kho văn bản (corpus) D = {d1, . . . , dN} và từvựng
V = {t1, . . . , tM} gồm mọi từxuất hiện trong D. Count Vectorizer biểu diễn văn bản d bằng
vector
xd =
tf(t1, d), tf(t2, d), . . . , tf(tM, d)

,
(5.7)
trong đó tf(t, d) (term frequency) là sốlần từt xuất hiện trong d. Cảkho văn bản trởthành ma
trận văn bản – từ(document-term matrix) kích thước N × M.
Ví dụ5.8. Xét kho văn bản gồm 3 câu:
• d1: “the cats are in the house”
• d2: “the dogs are in the house and outside”
• d3: “the cats and dogs are friends”
Từvựng (sắp xếp alphabet) gồm M = 9 từ: and, are, cats, dogs, friends, house, in, outside, the.
and
are
cats
dogs
friends
house
in
outside

the
d1
0
1
1
0
0
1
1
0
2
d2
1
1
0
1
0
1
1
1
2
d3
1
1
1
1
1
0
0
0
1
df(t)
2
3
2
2
1
2
2
1
3
Bảng 5.15: Ma trận đếm từ(Count Vectorizer) và tần suất văn bản df(t)
Listing 5.11: Count Vectorizer với scikit-learn
1
from sklearn.feature_extraction.text import CountVectorizer

2
3
corpus = [
4
"the cats are in the house",
5
"the dogs are in the house and outside",
6
"the cats and dogs are friends",
7
]
8
cv = CountVectorizer()
9
X = cv.fit_transform(corpus)
10
11
print(cv.vocabulary_)
12
# {'the': 8, 'cats': 2, 'are': 1, 'in': 6, 'house': 5,
13
#
'dogs': 3, 'and': 0, 'outside': 7, 'friends': 4}
14
print(X.toarray())
15
# [[0 1 1 0 0 1 1 0 2]
16
#
[1 1 0 1 0 1 1 1 2]
17
#
[1 1 1 1 1 0 0 0 1]]
Mặc định CountVectorizer chuyển chữvềchữthường và tách từbằng biểu thức chính
quy (?u)\b\w\w+\b, tức bỏqua các từchỉcó 1 ký tự. Các tham sốhay dùng: stop_words
(loại từdừng), ngram_range=(1,2) (lấy thêm cặp từ), min_df/max_df (loại từquá hiếm/quá
phổbiến).

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
37
Chuẩn hóa L2.
Văn bản dài có sốđếm lớn hơn chỉvì dài hơn. Đểso sánh công bằng, mỗi
vector được chia cho chuẩn Euclid của nó:

ˆxd =
xd
∥xd∥2
,
∥xd∥2 =
qP
j x2
dj.
(5.8)
Với d1: ∥xd1∥2
2 = 1 + 1 + 1 + 1 + 22 = 8, nên các số1 trởthành 1/
√
8 ≈0,3536 và số2 trở
thành 2/
√
8 ≈0,7071. Tương tự∥xd2∥2 =
√
10 và ∥xd3∥2 =
√
6:
and
are
cats
dogs
friends
house
in
outside
the
d1
0
0.3536
0.3536
0
0
0.3536
0.3536
0
0.7071
d2
0.3162
0.3162
0
0.3162
0

0.3162
0.3162
0.3162
0.6325
d3
0.4082
0.4082
0.4082
0.4082
0.4082
0
0
0
0.4082
Bảng 5.16: Ma trận đếm sau khi chuẩn hóa L2 theo từng hàng
5.6.2
TF-IDF
Count Vectorizer có một nhược điểm: những từxuất hiện ởmọi văn bản (như “the”, “are”) có
sốđếm cao nhưng gần như không giúp phân biệt văn bản. Năm 1972, Karen Spärck Jones đề
xuất trong bài báo A statistical interpretation of term specificity and its application in retrieval
(Journal of Documentation) rằng trọng sốcủa một từnên tỉlệnghịch với sốvăn bản chứa nó —
đó là tần suất văn bản nghịch đảo (Inverse Document Frequency – IDF). Salton và Buckley
(1988) sau đó tổng kết các biến thểtrọng sốTF-IDF, trởthành chuẩn mực của ngành truy hồi
thông tin suốt nhiều thập kỷ.
Định nghĩa 5.7 (TF-IDF). Với N là sốvăn bản và df(t) là sốvăn bản chứa từt, trọng sốTF-IDF
của từt trong văn bản d là
tf-idf(t, d) = tf(t, d) × idf(t).
(5.9)
Dạng kinh điển của IDF là idf(t) = ln N
df(t). Thư viện scikit-learn dùng hai biến thểcó cộng
thêm 1 đểtừxuất hiện ởmọi văn bản không bịtriệt tiêu hoàn toàn:
Không làm trơn (smooth_idf=False) :
idf(t) = 1 + ln N
df(t),
(5.10)
Làm trơn (smooth_idf=True, mặc định) :
idf(t) = 1 + ln N + 1
df(t) + 1.
(5.11)
Công thức làm trơn tương đương việc thêm một “văn bản ảo” chứa mọi từđúng một lần, giúp
tránh phép chia cho 0.
Ví dụ5.9 (Tính tay IDF). Với N = 3 và df ởBảng 5.15, chỉcó ba giá trịdf ∈{1, 2, 3}:
df(t)
Các từ
IDF không làm trơn (5.10)

IDF làm trơn (5.11)
1
friends, outside
1 + ln 3 = 2,0986
1 + ln 2 = 1,6931
2
and, cats, dogs, house, in
1 + ln 1,5 = 1,4055
1 + ln 4
3 = 1,2877
3
are, the
1 + ln 1 = 1
1 + ln 1 = 1
Bảng 5.17: Giá trịIDF cho kho 3 văn bản

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
38
Nhân từng cột của ma trận đếm (Bảng 5.15) với IDF tương ứng, ta được ma trận TF-IDF
(chưa chuẩn hóa). Chẳng hạn với từ“cats” trong d1: tf = 1, df = 2 nên tf-idf = 1 × 1,2877 =
1,2877 (làm trơn); với “the” trong d1: 2 × 1 = 2.
and
are
cats
dogs
friends
house
in
outside
the
IDF làm trơn (smooth_idf=True)
d1
0
1
1.2877
0
0
1.2877
1.2877
0
2
d2
1.2877

1
0
1.2877
0
1.2877
1.2877
1.6931
2
d3
1.2877
1
1.2877
1.2877
1.6931
0
0
0
1
IDF không làm trơn (smooth_idf=False)
d1
0
1
1.4055
0
0
1.4055
1.4055
0
2
d2
1.4055
1
0
1.4055
0
1.4055
1.4055
2.0986
2
d3
1.4055
1
1.4055
1.4055
2.0986

0
0
0
1
Bảng 5.18: Ma trận TF-IDF chưa chuẩn hóa (norm=None)
[Chỗchèn hình]
images/ch-preprocessing-tfidf-excel.png
Hình 5.6: Tính TF-IDF trên bảng tính: ma trận đếm, df(t), idf(t, D) làm trơn, ma trận TF-IDF
và ma trận chuẩn hóa L2.
[Chỗchèn hình]
images/ch-preprocessing-tfidf-nosmooth.png
Hình 5.7: Ma trận TF-IDF với IDF không làm trơn (giá trị1,40547 và 2,09861) — khớp với kết
quảsmooth_idf=False của scikit-learn.
Chuẩn hóa L2 và độtương đồng cosine.
Mặc định TfidfVectorizer còn chuẩn hóa L2
từng hàng. Áp dụng cho ma trận làm trơn ởBảng 5.18:

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
39
and
are
cats
dogs
friends
house
in
outside
the
d1
0
0.3166
0.4077
0
0
0.4077
0.4077
0
0.6333
d2
0.3382
0.2626
0
0.3382

0
0.3382
0.3382
0.4447
0.5252
d3
0.4105
0.3188
0.4105
0.4105
0.5397
0
0
0
0.3188
Bảng 5.19: Ma trận TF-IDF mặc định của scikit-learn (smooth_idf=True, norm="l2")
Vì mỗi hàng có độdài 1, tích vô hướng giữa hai hàng chính là độtương đồng cosine:
cos(di, dj) = ˆxdi · ˆxdj.
(5.12)
Ta có cos(d1, d2) ≈0,6915, cos(d1, d3) ≈0,4702, cos(d2, d3) ≈0,5288: hai câu cùng nói về
“in the house” (d1, d2) giống nhau nhất — phù hợp với trực giác.
Listing 5.12: TF-IDF Vectorizer với các cấu hình khác nhau
1
from sklearn.feature_extraction.text import TfidfVectorizer
2
from sklearn.metrics.pairwise import cosine_similarity
3
4
corpus = [
5
"the cats are in the house",
6
"the dogs are in the house and outside",
7
"the cats and dogs are friends",
8
]
9
10
# 1) Chi dem tu (tuong duong CountVectorizer)
11
v = TfidfVectorizer(use_idf=False, smooth_idf=False, norm=None)
12
print(v.fit_transform(corpus).toarray())
13

14
# 2) TF-IDF khong lam tron, chua chuan hoa -> 1.4055, 2.0986
15
v = TfidfVectorizer(use_idf=True, smooth_idf=False, norm=None)
16
print(v.fit_transform(corpus).toarray().round(4))
17
18
# 3) TF-IDF lam tron, chua chuan hoa -> 1.2877, 1.6931
19
v = TfidfVectorizer(use_idf=True, smooth_idf=True, norm=None)
20
print(v.fit_transform(corpus).toarray().round(4))
21
print(v.idf_.round(4))
22
# [1.2877 1.
1.2877 1.2877 1.6931 1.2877 1.2877 1.6931 1.
]
23
24
# 4) Cau hinh mac dinh: lam tron + chuan hoa L2
25
v = TfidfVectorizer()
26
X = v.fit_transform(corpus)
27
print(X.toarray().round(4))
28
print(cosine_similarity(X).round(4))
29
# [[1.
0.6915 0.4702]
30
#
[0.6915 1.
0.5288]
31
#
[0.4702 0.5288 1.
]]

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)

40
Cấu hình
use_idf
smooth_idf
norm
Đếm từthuần túy
False
–
None
Đếm từchuẩn hóa L2
False
–
"l2"
TF-IDF thô
True
False
None
TF-IDF mặc định
True
True
"l2"
Bảng 5.20: Các cấu hình của TfidfVectorizer dùng trong chương
5.7
Chuẩn hóa thang đo đặc trưng (Feature Scaling)
5.7.1
Vì sao cần chuẩn hóa thang đo?
Xét hai đặc trưng của một căn nhà: diện tích lô đất (hàng nghìn đến hàng trăm nghìn feet vuông)
và sốphòng tắm (0 đến 4). Trong khoảng cách Euclid
d(x, z) =
p
(x1 −z1)2 + (x2 −z2)2,
(5.13)
chênh lệch diện tích sẽáp đảo hoàn toàn chênh lệch sốphòng tắm, dù trên thực tếsốphòng tắm
có thểquan trọng không kém. Chuẩn hóa thang đo đưa mọi đặc trưng vềcùng một “đơn vị” để:
• Các thuật toán dựa trên khoảng cách (KNN, K-Means, SVM với nhân RBF) đối xửcông
bằng giữa các đặc trưng.
• Gradient Descent hội tụnhanh hơn, vì mặt hàm mất mát bớt bịkéo dài theo một chiều.
• PCA không bịchi phối bởi đặc trưng có phương sai lớn chỉdo đơn vịđo.
• Các mô hình có chính quy hóa (Ridge, Lasso) phạt các hệsốmột cách công bằng.
Ngược lại, các mô hình dựa trên cây quyết định (Decision Tree, Random Forest, XGBoost) chỉ
so sánh ngưỡng trên từng đặc trưng nên không cần chuẩn hóa.
Ký hiệu một cột đặc trưng là x = (x1, . . . , xn). Bốn bộchuẩn hóa phổbiến trong scikit-learn
được định nghĩa như sau.
5.7.2
Min Max Scaler

x′
i =
xi −min(x)
max(x) −min(x) ∈[0, 1].
(5.14)
Tổng quát hơn, với feature_range=(a, b): x′′
i = a + x′
i(b −a). Phép biến đổi giữnguyên
hình dạng phân phối, nhưng rất nhạy với ngoại lai vì min và max chính là các giá trịcực trị.
5.7.3
Max Abs Scaler
x′
i =
xi
maxj |xj| ∈[−1, 1].
(5.15)
Max Abs Scaler không dịch chuyển dữliệu (không trừđi giá trịnào), nên giữnguyên các số0.
Đây là lựa chọn phù hợp cho ma trận thưa như ma trận TF-IDF ởmục trước: trừđi trung bình
sẽbiến mọi số0 thành khác 0 và phá vỡtính thưa.

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
41
5.7.4
Standard Scaler (chuẩn hóa z-score)
zi = xi −µ
σ
,
µ = 1
n
n
X
i=1
xi,
σ =
v
u
u
t1
n
n
X
i=1
(xi −µ)2.

(5.16)
Sau biến đổi, cột có trung bình 0 và độlệch chuẩn 1. Lưu ý scikit-learn dùng độlệch chuẩn
tổng thể(chia cho n, tức ddof=0), khác với pandas.Series.std() mặc định chia cho n −1.
Standard Scaler là lựa chọn mặc định cho hồi quy tuyến tính, hồi quy logistic, SVM, PCA và
mạng nơ-ron.
5.7.5
Robust Scaler
x′
i = xi −median(x)
IQR(x)
,
IQR = Q3 −Q1,
(5.17)
trong đó Q1, Q3 là các phân vị25% và 75%. Trung vịvà khoảng tứphân vịgần như không bị
ảnh hưởng bởi ngoại lai, nên Robust Scaler phù hợp với dữliệu lệch hoặc có giá trịbất thường.
5.7.6
Ví dụso sánh bốn bộchuẩn hóa
Ví dụ5.10. Cho cột x = (2, 4, 6, 8, 30), trong đó 30 là một ngoại lai. Các đại lượng cần thiết:
min = 2, max = 30, max |x| = 30, µ = 10, σ =
√
104 ≈10,198, median = 6, Q1 = 4, Q3 = 8,
IQR = 4.
x
MinMax
MaxAbs
Standard
Robust
2
0.0000
0.0667
−0.7845
−1.0
4
0.0714
0.1333
−0.5883
−0.5
6
0.1429
0.2000
−0.3922
0.0
8
0.2143
0.2667

−0.1961
0.5
30
1.0000
1.0000
1.9612
6.0
Bảng 5.21: Kết quảcủa bốn bộchuẩn hóa trên cột có ngoại lai
Quan sát Bảng 5.21: với Min Max Scaler, bốn giá trị“bình thường” bịép vào đoạn [0; 0,21]
— gần như mất khảnăng phân biệt — chỉvì một ngoại lai. Robust Scaler giữcác giá trịbình
thường trải đều trong [−1; 0,5] và đẩy ngoại lai ra xa (6,0), giúp ngoại lai dễnhận diện thay vì
làm méo phần còn lại.
Listing 5.13: So sánh bốn bộchuẩn hóa trong scikit-learn
1
import numpy as np
2
from sklearn.preprocessing import (MinMaxScaler , MaxAbsScaler ,
3
StandardScaler , RobustScaler)
4
5
x = np.array([2, 4, 6, 8, 30], dtype=float).reshape(-1, 1)
6
7
for scaler in [MinMaxScaler(), MaxAbsScaler(),
8
StandardScaler(), RobustScaler()]:
9
print(type(scaler).__name__ , scaler.fit_transform(x).ravel().
round(4))

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
42
10
# MinMaxScaler
[0.
0.0714 0.1429 0.2143 1.
]
11
# MaxAbsScaler
[0.0667 0.1333 0.2
0.2667 1.
]

12
# StandardScaler [-0.7845 -0.5883 -0.3922 -0.1961
1.9612]
13
# RobustScaler
[-1.
-0.5
0.
0.5
6. ]
[Chỗchèn hình]
images/ch-preprocessing-scalers.png
Hình 5.8: Phân phối của một đặc trưng trước và sau khi áp dụng bốn bộchuẩn hóa (gợi ý: vẽ
histogram hoặc boxplot bằng matplotlib).
Bộchuẩn hóa
Miền giá trị
Bền với ngoại lai
Khi nào dùng
MinMaxScaler
[0, 1]
Không
Cần miền cốđịnh (ảnh, mạng
nơ-ron), dữliệu ít ngoại lai
MaxAbsScaler
[−1, 1]
Không
Ma trận thưa (TF-IDF), dữliệu
đã tâm ở0
StandardScaler
Không giới hạn
Trung bình
Mặc định cho mô hình tuyến
tính, SVM, PCA
RobustScaler
Không giới hạn
Có
Dữliệu lệch, nhiều ngoại lai
Bảng 5.22: Tóm tắt lựa chọn bộchuẩn hóa
5.8
Dữliệu mất cân bằng và SMOTE
Trong nhiều bài toán phân lớp, lớp quan trọng nhất lại là lớp hiếm: giao dịch gian lận (thường
dưới 1%), bệnh hiếm, thiết bịsắp hỏng. Mô hình huấn luyện trên dữliệu như vậy có xu hướng
“bỏqua” lớp thiểu sốmà vẫn đạt accuracy cao — nghịch lý accuracy sẽđược phân tích ở
Chương 11. Có ba nhóm giải pháp:
• Ởmức thuật toán: gán trọng sốlớn hơn cho lỗi trên lớp thiểu số, ví dụđặt tham số

class_weight bằng "balanced".
• Giảm mẫu lớp đa số(undersampling): bỏbớt mẫu của lớp đông — đơn giản nhưng mất
thông tin.
• Tăng mẫu lớp thiểu số(oversampling): nhân bản ngẫu nhiên các mẫu hiếm dễgây quá
khớp, vì mô hình gặp đi gặp lại đúng những điểm đó.

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
43
SMOTE (Synthetic Minority Over-sampling Technique), do Chawla, Bowyer, Hall và Kegelmeyer
công bốnăm 2002, khắc phục nhược điểm của việc nhân bản: thay vì sao chép, SMOTE tổng
hợp mẫu mới nằm trên đoạn thẳng nối một mẫu thiểu sốvới một láng giềng cùng lớp của nó.
Định nghĩa 5.8 (Sinh mẫu SMOTE). Với mỗi mẫu thiểu sốxi: tìm k láng giềng gần nhất trong
lớp thiểu số; chọn ngẫu nhiên một láng giềng xnn và một sốλ ∼U(0, 1); mẫu mới là
xmới = xi + λ (xnn −xi).
(5.18)
Ví dụ5.11 (Tạo một mẫu SMOTE). Lớp thiểu sốgồm P1(2, 3), P2(4, 4), P3(3, 6); chọn k = 2.
Hai láng giềng của P1 là P2 (d =
√
5 ≈2,236) và P3 (d =
√
10 ≈3,162). Giảsửlần rút ngẫu
nhiên chọn được P2 và λ = 0,4:
xmới = (2, 3) + 0,4 ×

(4, 4) −(2, 3)

= (2, 3) + (0,8; 0,4) = (2,8; 3,4).
Điểm mới nằm trên đoạn P1P2, bên trong vùng của lớp thiểu số, và không trùng với mẫu nào
đã có.
[Chỗchèn hình]
images/ch-preprocessing-smote.png
Hình 5.9: SMOTE sinh mẫu tổng hợp trên đoạn thẳng nối các mẫu thiểu sốvới láng giềng cùng
lớp.
SMOTE được cài đặt trong thư viện imbalanced-learn (Lemaître, Nogueira & Aridas,
2017), cài bằng lệnh pip install imbalanced-learn. Các biến thểđáng chú ý: Borderline-
SMOTE (Han và cộng sự, 2005) chỉsinh mẫu gần biên quyết định; ADASYN (He và cộng sự,
2008) sinh nhiều mẫu hơn ởvùng khó học; SMOTE-NC xửlý dữliệu có cột định danh.
Listing 5.14: SMOTE với imbalanced-learn
1
from collections import Counter
2
from sklearn.datasets import make_classification
3

from imblearn.over_sampling import SMOTE
4
5
X, y = make_classification(n_samples=1000, n_features=4,
n_informative=2,
6
weights=[0.9, 0.1], random_state=42)
7
print(Counter(y))
# lop 0: 895, lop 1: 105
8
X_res, y_res = SMOTE(k_neighbors=5, random_state=42).fit_resample(X,
y)
9
print(Counter(y_res))
# lop 0: 895, lop 1: 895

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
44
Nguyên tắc vàng: chỉáp dụng SMOTE trên tập huấn luyện. Nếu sinh mẫu trước khi chia dữ
liệu, các mẫu tổng hợp được nội suy từchính những điểm sẽrơi vào tập kiểm tra, khiến kết
quảđánh giá lạc quan giảtạo (rò rỉdữliệu). Thư viện imbalanced-learn cung cấp Pipeline
riêng, trong đó bước lấy mẫu chỉchạy khi fit, tức chỉtrên phần huấn luyện của mỗi fold kiểm
định chéo:
Listing 5.15: So sánh các cách xửlý mất cân bằng trong Pipeline của imbalanced-learn
1
from imblearn.pipeline import Pipeline as ImbPipeline
2
from sklearn.preprocessing import StandardScaler
3
from sklearn.linear_model import LogisticRegression
4
from sklearn.model_selection import cross_validate
5
6
models = {
7
"khong xu ly": ImbPipeline([("scale", StandardScaler()),
8
("clf", LogisticRegression())]),
9
"class_weight": ImbPipeline([("scale", StandardScaler()),
10

("clf", LogisticRegression(
class_weight="balanced"))]),
11
"smote": ImbPipeline([("scale", StandardScaler()),
12
("smote", SMOTE(random_state=42)),
# chi
chay khi fit
13
("clf", LogisticRegression())]),
14
}
15
for name, m in models.items():
16
r = cross_validate(m, X, y, cv=5, scoring=["recall", "precision",
"f1"])
17
print(name, {k[5:]: round(v.mean(), 3) for k, v in r.items() if k
.startswith("test")})
Cách xửlý
Recall
Precision
F1
Không xửlý
0,486
0,807
0,589
class_weight="balanced"
0,838
0,437
0,572
SMOTE trong pipeline
0,838
0,441
0,575
Bảng 5.23: Hồi quy logistic trên dữliệu tỉlệ90/10, kiểm định chéo 5-fold; lớp dương là lớp
thiểu số
Kết quảcho một bài học quan trọng: SMOTE giúp mô hình tìm ra nhiều mẫu thiểu sốhơn hẳn
(recall tăng từ0,486 lên 0,838), nhưng phải trảgiá bằng nhiều báo động nhầm hơn (precision
giảm từ0,807 xuống 0,441); F1 gần như không đổi, và hiệu quảtương đương cách đơn giản
class_weight="balanced". SMOTE vì vậy không phải phép màu: nó dịch chuyển điểm
cân bằng giữa precision và recall, và nên được chọn khi bỏsót lớp thiểu sốđắt hơn báo động
nhầm (sàng lọc bệnh, phát hiện gian lận). Việc so sánh phải dựa trên độđo phù hợp với bài toán
(Chương 11), không phải accuracy.

5.9
Kết hợp các bước: Pipeline và ColumnTransformer
Dữliệu thực tếthường có nhiều kiểu cột cùng lúc. scikit-learn cung cấp:
<!-- page: 1 -->
# VI_PY_078: NumPy: Mảng ndarray, broadcast và các phép toán ma trận

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân  
**Chuyên mục**: NumPy | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 90 -->
CHƯƠNG 9. PHÂN CỤM
(CLUSTERING)
84
Tài liệu tham khảo của chương
1. Ankerst, M., Breunig, M. M., Kriegel, H.-P., & Sander, J. (1999). OPTICS: Ordering
Points To Identify the Clustering Structure. Proceedings of ACM SIGMOD ’99, 49–60.
2. Arthur, D., & Vassilvitskii, S. (2007). k-means++: The Advantages of Careful Seeding.
Proceedings of SODA ’07, 1027–1035.
3. Comaniciu, D., & Meer, P. (2002). Mean Shift: A Robust Approach Toward Feature Space
Analysis. IEEE Transactions on Pattern Analysis and Machine Intelligence, 24(5), 603–
619.
4. Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A Density-Based Algorithm for
Discovering Clusters in Large Spatial Databases with Noise. Proceedings of KDD ’96,
226–231.
5. Fukunaga, K., & Hostetler, L. (1975). The estimation of the gradient of a density function,
with applications in pattern recognition. IEEE Transactions on Information Theory, 21(1),
32–40.
6. Johnson, S. C. (1967). Hierarchical clustering schemes. Psychometrika, 32(3), 241–254.
7. Lloyd, S. P. (1982). Least squares quantization in PCM. IEEE Transactions on Information
Theory, 28(2), 129–137.
8. MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations.
Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability,
1, 281–297.
9. Rousseeuw, P. J. (1987). Silhouettes: a graphical aid to the interpretation and validation
of cluster analysis. Journal of Computational and Applied Mathematics, 20, 53–65.
10. Ward, J. H. (1963). Hierarchical Grouping to Optimize an Objective Function. Journal of
the American Statistical Association, 58(301), 236–244.

<!-- page: 91 -->
Chương 10:
Giảm chiều dữliệu
(Dimensionality Reduction)
Dữliệu thực tếthường có rất nhiều đặc trưng: một ảnh 28 × 28 có 784 chiều, một văn bản sau
khi qua TF-IDF (Chương 5) có hàng chục nghìn chiều, dữliệu gen có hàng triệu chiều. Sốchiều

<!-- page: 2 -->

lớn gây ra nhiều khó khăn mà Richard Bellman (1957) gọi chung là lời nguyền sốchiều (curse
of dimensionality). Giảm chiều dữliệu là quá trình biểu diễn dữliệu bằng ít chiều hơn nhưng
giữlại phần lớn thông tin.
Theo kếhoạch giảng dạy, chương này tập trung vào hai kỹthuật nền tảng: SVD (phân tích
giá trịsuy biến) và PCA (phân tích thành phần chính).
Sau khi học xong chương này, người học có khảnăng:
• Giải thích lời nguyền sốchiều và phân biệt lựa chọn đặc trưng với trích xuất đặc trưng.
• Tính tay phương sai, hiệp phương sai, hệsốtương quan và cặp trịriêng – vector riêng của
ma trận 2 × 2.
• Tính tay SVD của ma trận nhỏvà xấp xỉhạng thấp.
• Tính tay PCA (chuẩn hóa tâm, ma trận hiệp phương sai, trịriêng, chiếu dữliệu).
• Dùng PCA, TruncatedSVD của scikit-learn và chọn sốthành phần theo phương sai giải
thích.
10.1
Lời nguyền sốchiều
Khi sốchiều d tăng:
• Dữliệu trởnên thưa: đểphủđều khối lập phương đơn vịvới mật độ10 điểm mỗi trục
cần 10d điểm — 100 điểm cho d = 2, nhưng 1010 điểm cho d = 10.
• Khoảng cách mất ý nghĩa: trong không gian nhiều chiều, khoảng cách từmột điểm đến
láng giềng gần nhất và xa nhất gần bằng nhau (Beyer và cộng sự, 1999), khiến KNN và
K-Means kém hiệu quả.
• Quá khớp: sốtham sốtăng theo d, mô hình dễhọc thuộc nhiễu khi sốmẫu không đủ.
• Chi phí lưu trữvà tính toán tăng; không thểtrực quan hóa trên 3 chiều.
85

<!-- page: 92 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
86
Hướng tiếp cận
Ý tưởng
Ví dụ
Lựa chọn đặc trưng
(feature selection)
Giữlại một tập con các cột gốc
Lọc theo phương sai,
tương
quan,
Lasso,
SelectKBest
Trích xuất đặc trưng
tuyến tính
Tạo cột mới là tổhợp tuyến
tính các cột gốc
PCA, SVD, LDA

<!-- page: 3 -->

Trích xuất phi tuyến
(manifold learning)
Bảo toàn cấu trúc lân cận cục
bộ
Kernel
PCA,
t-SNE,
UMAP, Autoencoder
Bảng 10.1: Các hướng giảm chiều dữliệu
10.2
Kiến thức nền: phương sai, hiệp phương sai và trịriêng
CảSVD và PCA đều được xây dựng trên ba khái niệm: phương sai, hiệp phương sai và cặp trị
riêng – vector riêng. Mục này ôn lại chúng qua các ví dụtính tay.
10.2.1
Phương sai
Định nghĩa 10.1 (Phương sai). Phương sai (variance) đo mức độphân tán của dữliệu quanh
giá trịtrung bình:
Var(A) = 1
n
n
X
i=1
(ai −¯a)2.
(10.1)
Khi ước lượng phương sai của tổng thểtừmột mẫu, người ta thường chia cho n −1 thay vì n
(hiệu chỉnh Bessel) đểđược ước lượng không chệch. Độlệch chuẩn σ là căn bậc hai của phương
sai.
Ví dụ10.1 (Tính phương sai). A = (3, 7, 5) có ¯a = 3+7+5
3
= 5 và
Var(A) = (3 −5)2 + (7 −5)2 + (5 −5)2
3
= 8
3 ≈2,67.
Nếu chia cho n −1 thì được 8
2 = 4.
Lưu ý khi lập trình: np.var mặc định chia cho n (ddof=0), còn pandas.Series.var và np.cov
mặc định chia cho n −1 (ddof=1). Với mẫu nhỏ, hai quy ước cho kết quảkhác nhau đáng kể,
nên cần ghi rõ quy ước đang dùng.
10.2.2
Hiệp phương sai và hệsốtương quan
Định nghĩa 10.2 (Hiệp phương sai và hệsốtương quan). Hiệp phương sai (covariance) đo mức
độcùng biến thiên của hai biến:
Cov(A, B) = 1
n

<!-- page: 4 -->

n
X
i=1
(ai −¯a)(bi −¯b).
(10.2)
Cov > 0: hai biến có xu hướng cùng tăng; Cov < 0: biến này tăng thì biến kia giảm; Cov ≈0:
không có quan hệtuyến tính. Vì độlớn của hiệp phương sai phụthuộc đơn vịđo, Karl Pearson
(1896) chuẩn hóa nó thành hệsốtương quan
r = Cov(A, B)
σA σB
∈[−1, 1].
(10.3)

<!-- page: 93 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
87
Ví dụ10.2 (Tính hiệp phương sai và hệsốtương quan). A = (2, 8, 4) và B = (6, 1, 5) có
¯a = 14
3 ≈4,67, ¯b = 12
3 = 4:
Cov(A, B) = 1
3

(2 −4,67)(6 −4) + (8 −4,67)(1 −4) + (4 −4,67)(5 −4)

= 1
3 (−5,33 −10 −0,67) = −16
3 ≈−5,33.
Dấu âm cho biết khi A tăng thì B giảm: quan sát thứhai có A lớn nhất nhưng B nhỏnhất. Với
σ2
A = 56
9 ≈6,22 và σ2
B = 14
3 ≈4,67:
r =
−5,33
√6,22 × 4,67 ≈−0,99,
tức hai biến có quan hệtuyến tính nghịch rất mạnh. Khi tính tay cần giữđúng dấu của từng tích
(ai −¯a)(bi −¯b): bỏsót dấu âm sẽđảo ngược hoàn toàn ý nghĩa của kết quả.
Ma trận hiệp phương sai.
Với dữliệu d chiều, các phương sai và hiệp phương sai được gom
thành ma trận đối xứng C ∈Rd×d với Cjk = Cov(xj, xk); đường chéo chính là phương sai của
từng biến. Nếu Xc là dữliệu đã trừtrung bình từng cột thì C =
1

<!-- page: 5 -->

n−1X⊤
c Xc — quy ước chia n −1
mà PCA của scikit-learn sửdụng.
10.2.3
Trịriêng và vector riêng
Định nghĩa 10.3 (Trịriêng, vector riêng). Cho ma trận vuông A. Sốλ và vector v̸ = 0 thỏa
Av = λv được gọi là trịriêng và vector riêng tương ứng: nhân với A chỉco giãn v theo hệ
sốλ mà không làm đổi phương của nó. Các trịriêng là nghiệm của phương trình đặc trưng
det(A −λI) = 0.
Ví dụ10.3 (Tính tay trịriêng và vector riêng). Cho A =
2
3
4
1

.
Bước 1 – phương trình đặc trưng:
det
2 −λ
3
4
1 −λ

= (2 −λ)(1 −λ) −3 · 4 = λ2 −3λ −10 = 0 ⇔λ1 = 5, λ2 = −2.
Bước 2 – vector riêng ứng với λ1 = 5: giải (A −5I)v = 0,
−3
3
4
−4
 v1
v2

= 0 ⇔−v1 + v2 = 0 ⇔v1 = v2.
Chọn v2 = 1 thì v1 = 1; chuẩn hóa vềđộdài 1: v1 =
1
√
12+12(1, 1) ≈(0,7071; 0,7071).
Bước 3 – vector riêng ứng với λ2 = −2:
4
3
4
3
 v1
v2


<!-- page: 6 -->

= 0 ⇔4v1 + 3v2 = 0 ⇔v1 = −3
4v2.
Chọn v2 = 4 thì v1 = −3; chuẩn hóa: v2 =
1
√
(−3)2+42(−3, 4) = (−0,6; 0,8).
Kiểm tra nhanh: tổng các trịriêng bằng vết (tổng đường chéo) của ma trận, 5 + (−2) = 2 + 1;
tích các trịriêng bằng định thức, 5 × (−2) = 2 · 1 −3 · 4 = −10.
Ma trận A ởví dụnày không đối xứng nên hai vector riêng không vuông góc (v1 · v2 ≈
0,14̸ = 0). Ngược lại, với ma trận đối xứng như X⊤X hay ma trận hiệp phương sai, định lý phổ
bảo đảm mọi trịriêng là sốthực và có thểchọn các vector riêng đôi một vuông góc — đây chính
là tính chất mà SVD và PCA khai thác.

<!-- page: 94 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
88
Listing 10.1: Phương sai, hiệp phương sai và trịriêng với NumPy
1
import numpy as np
2
3
A = np.array([3, 7, 5])
4
print(np.var(A), np.var(A, ddof=1))
# 2.6667 4.0
5
a, b = np.array([2, 8, 4]), np.array([6, 1, 5])
6
print(np.cov(a, b, ddof=0)[0, 1])
# -5.3333
7
print(np.corrcoef(a, b)[0, 1])
# -0.9897
8
9
M = np.array([[2, 3], [4, 1]])
10
eigval, eigvec = np.linalg.eig(M)
# NumPy moi co the tra ve kieu so
phuc (5.+0.j)
11
print(eigval.real)
# [ 5. -2.]
12

<!-- page: 7 -->

print(eigvec.real)
# moi cot la mot vector rieng: (0.7071,
0.7071) va (-0.6, 0.8)
10.3
Phân tích giá trịsuy biến (SVD)
10.3.1
Lịch sử
SVD được Eugenio Beltrami (1873) và Camille Jordan (1874) phát hiện độc lập; Eckart và
Young (1936) chứng minh tính chất xấp xỉhạng thấp tối ưu — nền tảng của mọi ứng dụng nén
dữliệu. Thuật toán tính SVD ổn định sốdo Golub và Kahan (1965) đềxuất là cái mà NumPy
dùng ngày nay. SVD còn nổi tiếng nhờcuộc thi Netflix Prize (2006–2009), nơi các biến thểphân
rã ma trận chiếm ưu thếtrong hệgợi ý.
Định lý 10.1 (Phân tích giá trịsuy biến). Mọi ma trận thực A ∈Rm×n đều phân tích được thành
A = UΣV⊤,
(10.4)
trong đó U ∈Rm×m và V ∈Rn×n là các ma trận trực giao (cột là vector suy biến trái/phải),
Σ ∈Rm×n là ma trận đường chéo với các giá trịsuy biến σ1 ≥σ2 ≥· · · ≥0. Ngoài ra σ2
i là
trịriêng của AA⊤(và của A⊤A), cột của U là vector riêng của AA⊤, cột của V là vector riêng
của A⊤A.
Định lý 10.2 (Eckart–Young). Giữlại k giá trịsuy biến lớn nhất, Ak = Pk
i=1 σiuiv⊤
i là ma trận
hạng k gần A nhất theo chuẩn Frobenius, với sai số∥A −Ak∥F =
q
σ2
k+1 + · · · + σ2
r.
Ví dụ10.4 (Tính tay SVD). Cho M =
3
2
2
2
3
−2

.
Bước 1. MM⊤=
17
8
8
17

, phương trình đặc trưng (17 −λ)2 −64 = 0 cho λ1 = 25, λ2 = 9.
Vậy σ1 = 5, σ2 = 3.

<!-- page: 8 -->

Bước 2. Vector riêng của MM⊤: u1 =
1
√
2(1, 1)⊤, u2 =
1
√
2(1, −1)⊤.
Bước 3. vi = M⊤ui/σi:
v1 =
1
5
√
2(5, 5, 0)⊤=
1
√
2(1, 1, 0)⊤,
v2 =
1
3
√
2(1, −1, 4)⊤=
1
√
18(1, −1, 4)⊤.
Vector thứba v3 = 1
3(2, −2, −1)⊤vuông góc với hai vector trên (ứng với giá trịsuy biến 0).

<!-- page: 95 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
89
Bước 4 – xấp xỉhạng 1. M1 = σ1u1v⊤
1 = 5 · 1
2
1
1
0
1
1
0

=
2,5
2,5
0

<!-- page: 9 -->

2,5
2,5
0

, sai số∥M −
M1∥F = σ2 = 3. Thành phần thứnhất giữσ2
1/(σ2
1 + σ2
2) = 25/34 ≈73,5% “năng lượng” của
ma trận.
Listing 10.2: SVD với NumPy (ví dụtrên lớp)
1
import numpy as np
2
3
M = np.array([[3, 2, 2], [2, 3, -2]])
4
U, s, Vt = np.linalg.svd(M)
5
print(s)
# [5. 3.]
6
print(U)
# cot = vector suy bien trai (co the doi dau)
7
print(Vt)
# dong = vector suy bien phai
8
9
# Tai tao lai M tu 3 thanh phan
10
Sigma = np.zeros(M.shape); Sigma[:2, :2] = np.diag(s)
11
print(np.allclose(U @ Sigma @ Vt, M))
# True
12
13
# Xap xi hang 1
14
M1 = s[0] * np.outer(U[:, 0], Vt[0])
15
print(M1.round(2))
# [[2.5 2.5 0.] [2.5 2.5
0.]]
16

<!-- page: 10 -->

print(np.linalg.norm(M - M1))
# 3.0 = sigma_2
Lưu ý: vector suy biến chỉxác định duy nhất đến dấu: NumPy có thểtrảvề−u1, −v1, kết quả
vẫn đúng.
10.3.2
Tính SVD thông qua X⊤X
Định lý trên gợi ý cách tính SVD bằng tay cho ma trận có nhiều dòng: (1) lập X⊤X — ma trận
vuông, đối xứng, kích thước bằng sốcột; (2) tìm các trịriêng λi và vector riêng đơn vịvi của
nó; (3) giá trịsuy biến σi = √λi; (4) vector suy biến trái ui = Xvi/σi.
Ví dụ10.5 (SVD của ma trận 5 × 2). Cho X =






3
7
1
5
6
4
8
1
2
3






.
Bước 1 – lập X⊤X:
X⊤X =
3
1
6
8
2
7
5
4
1
3

<!-- page: 11 -->








3
7
1
5
6
4
8
1
2
3






=
114
64
64
100

,
trong đó 114 = 32 + 12 + 62 + 82 + 22 và 64 = 3 · 7 + 1 · 5 + 6 · 4 + 8 · 1 + 2 · 3.
Bước 2 – trịriêng:
(114 −λ)(100 −λ) −642 = λ2 −214λ + 7304 = 0 ⇔λ1 ≈171,38, λ2 ≈42,62.

<!-- page: 96 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
90
Bước 3 – vector riêng. Với λ1: (114 −171,38) v1 + 64 v2 = 0 ⇔v1 = 1,1153 v2. Chọn
v2 = 1 được (1,1153; 1), chuẩn hóa cho v1 = (1,1153; 1)/1,4980 ≈(0,7446; 0,6676). Với λ2:
(114 −42,62) v1 + 64 v2 = 0 ⇔v1 = −0,8966 v2. Chọn v2 = 1 được (−0,8966; 1), chuẩn hóa
cho v2 ≈(−0,6676; 0,7446). Hai vector vuông góc: 0,7446×(−0,6676)+0,6676×0,7446 = 0.
Bước 4 – giá trịvà vector suy biến: σ1 = √171,38 ≈13,09, σ2 = √42,62 ≈6,53, và
u1 = Xv1/σ1 ≈(0,528; 0,312; 0,545; 0,506; 0,267).
Sai lầm thường gặp khi chuẩn hóa vector riêng.

<!-- page: 12 -->

Từv1 = −0,8966 v2, nếu chọn v2 = 1 thì
vector là (v1, v2) = (−0,8966; 1) — không phải (1; −0,8966). Đảo chỗhai thành phần cho
ra một vector khác hẳn, không còn là vector riêng. Cách tựkiểm tra đơn giản nhất là nhân lại:
X⊤X v phải bằng λv, và vector sau khi chuẩn hóa phải có độdài đúng bằng 1.
Listing 10.3: Kiểm tra cách tính SVD qua trịriêng
1
X = np.array([[3, 7], [1, 5], [6, 4], [8, 1], [2, 3]])
2
lam, V = np.linalg.eigh(X.T @ X)
# tri rieng tang dan: [ 42.6183
171.3817]
3
print(np.sqrt(lam[::-1]))
# [13.0913
6.5283]
4
U, s, Vt = np.linalg.svd(X, full_matrices=False)
5
print(s)
# [13.0913
6.5283] -- trung
khop
6
print(Vt)
# moi dong la mot v_i (co the
doi dau)
10.3.3
Ứng dụng: nén ảnh và TruncatedSVD
Một ảnh xám là ma trận m×n. Lưu Ak chỉcần k(m+n+1) sốthay vì mn. Với ảnh 512 ×512
và k = 50: 50 × 1025 = 51 250 sốso với 262 144 — tiết kiệm khoảng 80%.
Listing 10.4: Nén ảnh bằng SVD
1
import matplotlib.pyplot as plt
2
from skimage import data, color
3
4
img = color.rgb2gray(data.astronaut())
# anh xam 512 x 512
5
U, s, Vt = np.linalg.svd(img, full_matrices=False)
6
fig, axes = plt.subplots(1, 4, figsize=(14, 4))
7
for ax, k in zip(axes, [5, 20, 50, 512]):

<!-- page: 13 -->

8
ax.imshow(U[:, :k] @ np.diag(s[:k]) @ Vt[:k], cmap="gray")
9
ax.set_title(f"k = {k}"); ax.axis("off")
10
plt.show()

<!-- page: 97 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
91
[Chỗchèn hình]
images/ch-reduce-svd-image.png
Hình 10.1: Ảnh tái tạo từk = 5, 20, 50 giá trịsuy biến lớn nhất so với ảnh gốc.
Với ma trận thưa như kết quảTF-IDF, scikit-learn cung cấp TruncatedSVD: tính trực tiếp k
thành phần đầu mà không cần trừtrung bình (trừtrung bình sẽphá vỡtính thưa). Áp dụng lên
ma trận văn bản – từ, kỹthuật này được gọi là Phân tích ngữnghĩa tiềm ẩn (Latent Semantic
Analysis – LSA, Deerwester và cộng sự, 1990): mỗi thành phần tương ứng một “chủđề”.
Listing 10.5: LSA: TF-IDF + TruncatedSVD
1
from sklearn.feature_extraction.text import TfidfVectorizer
2
from sklearn.decomposition import TruncatedSVD
3
4
docs = ["python machine learning", "python data analysis",
5
"deep learning neural network", "neural network training",
6
"data analysis with pandas"]
7
X = TfidfVectorizer().fit_transform(docs)
# ma tran thua 5 x
V
8
lsa = TruncatedSVD(n_components=2, random_state=0)
9
Z = lsa.fit_transform(X)
# 5 x 2
10
print(lsa.explained_variance_ratio_)
11
print(Z.round(3))
# van ban cung chu de nam gan nhau
10.4

<!-- page: 14 -->

Phân tích thành phần chính (PCA)
10.4.1
Lịch sửvà ý tưởng
PCA do Karl Pearson phát minh năm 1901 dưới dạng bài toán “tìm đường thẳng và mặt phẳng
khớp nhất với hệđiểm”, và được Harold Hotelling (1933) phát triển độc lập, đặt tên “thành phần
chính”. Trong xửlý tín hiệu, PCA còn được gọi là biến đổi Karhunen–Loève.
Định nghĩa 10.4 (Thành phần chính). Cho dữliệu đã chuẩn hóa tâm Xc (n × d). Thành phần
chính thứnhất là vector đơn vịw1 sao cho phương sai của dữliệu chiếu lên w1 là lớn nhất:
w1 = arg max
∥w∥=1 w⊤Cw,
C =
1
n−1X⊤
c Xc.
(10.5)
Các thành phần tiếp theo cũng cực đại phương sai nhưng phải vuông góc với các thành phần
trước.

<!-- page: 98 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
92
Giải bài toán tối ưu bằng nhân tửLagrange cho Cw = λw: các thành phần chính là vector
riêng của ma trận hiệp phương sai, và phương sai theo thành phần thứj chính là trịriêng λj.
Tương đương, cực đại phương sai cũng là cực tiểu sai sốtái tạo (khoảng cách bình phương từ
điểm đến không gian con) — đúng cách nhìn ban đầu của Pearson.
Quan hệPCA – SVD.
Nếu Xc = UΣV⊤thì C = V Σ2
n−1V⊤: thành phần chính là cột của V,
trịriêng λj = σ2
j/(n −1). scikit-learn tính PCA bằng SVD vì ổn định sốhơn việc lập ma trận
hiệp phương sai.
Các bước PCA:
1. Chuẩn hóa tâm (trừtrung bình mỗi cột); nếu các cột khác đơn vịđo thì chuẩn hóa thêm
bằng StandardScaler.
2. Tính ma trận hiệp phương sai C.
3. Tìm trịriêng, vector riêng; sắp xếp trịriêng giảm dần.
4. Chọn k vector riêng đầu làm ma trận Wk (d × k).
5. Chiếu dữliệu: Z = XcWk (n × k).
Ví dụ10.6 (Tính tay PCA). Giảm 5 điểm hai chiều trong Bảng 10.2 xuống còn một chiều.
x1
3
5
0
1

<!-- page: 15 -->

2
x2
6
4
2
0
3
Bảng 10.2: Dữliệu ví dụPCA
Bước 1 – chuẩn hóa tâm. ¯x1 = 3+5+0+1+2
5
= 2,2 và ¯x2 = 6+4+2+0+3
5
= 3. Trừtrung bình từng
cột, x′
ij = xij −¯xj:
Xc =






0,8
3
2,8
1
−2,2
−1
−1,2
−3
−0,2
0






.
Bước 2 – ma trận hiệp phương sai:
X⊤
c Xc =
14,8
11
11

<!-- page: 16 -->

20

,
C =
1
n −1 X⊤
c Xc = 1
4
14,8
11
11
20

=
 3,7
2,75
2,75
5

.
Hiệp phương sai dương (2,75) cho thấy hai biến có xu hướng tăng cùng nhau.
Bước 3 – trịriêng:
(3,7 −λ)(5 −λ) −2,752 = λ2 −8,7λ + 10,9375 = 0 ⇔λ1 ≈7,1758, λ2 ≈1,5242.
Bước 4 – vector riêng. Với λ1 = 7,1758:
−3,4758
2,75
2,75
−2,1758
 v1
v2

= 0 ⇔v1 = 0,7912 v2.

<!-- page: 99 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
93
Chọn v2 = 1 được (v1, v2) = (0,7912; 1); chuẩn hóa: w1 =
(0,7912; 1)
p
0,79122 + 12 = (0,7912; 1)
1,2751
≈
(0,6205; 0,7842).
Với λ2 = 1,5242: 2,1758 v1 + 2,75 v2 = 0 ⇔v1 = −1,2639 v2; chọn v2 = 1 được

<!-- page: 17 -->

(−1,2639; 1), chuẩn hóa cho w2 ≈(−0,7842; 0,6205).
Kiểm tra: Cw1 = (3,7 × 0,6205 + 2,75 × 0,7842;
2,75 × 0,6205 + 5 × 0,7842) ≈
(4,452; 5,627) ≈7,1758 × (0,6205; 0,7842).
Bước 5 – tỉlệphương sai giải thích:
7,1758
7,1758+1,5242 = 7,1758
8,7
≈82,5%; thành phần thứnhất giữ
khoảng 82,5% thông tin.
Bước 6 – chiếu dữliệu z = Xc w1. Chẳng hạn với điểm đầu tiên: z1 = 0,8 × 0,6205 + 3 ×
0,7842 ≈2,849. Toàn bộ:
z ≈(2,849; 2,522; −2,149; −3,097; −0,124).
Mỗi điểm hai chiều giờchỉcòn một con số; có thểtái tạo gần đúng điểm gốc bằng ˆx = ¯x+z w1.
Sai lầm thường gặp.
(1) Từv1 = 0,7912 v2 mà viết vector thành (1; 0,7912) là đảo nhầm
thành phần: vector chuẩn hóa thu được, (0,7842; 0,6205), không còn là vector riêng của C.
Hãy luôn kiểm tra lại Cw = λw như ởbước 4. (2) Quên chuẩn hóa tâm trước khi lập ma trận
hiệp phương sai: khi đó ta đang tính SVD của dữliệu gốc (như ví dụ5 × 2 ởmục SVD) chứ
không phải PCA, và thành phần chính đầu tiên bịkéo lệch vềphía vector trung bình của dữliệu.
Listing 10.6: Kiểm tra ví dụbằng NumPy và scikit-learn
1
import numpy as np
2
from sklearn.decomposition import PCA
3
4
X = np.array([[3, 6], [5, 4], [0, 2], [1, 0], [2, 3]])
5
6
# Cach 1: tu cai dat
7
Xc = X - X.mean(axis=0)
8
C = np.cov(Xc, rowvar=False)
# chia n - 1: [[3.7 2.75]
[2.75 5.]]
9
eigval, eigvec = np.linalg.eigh(C)
# tri rieng tang dan
10
order = np.argsort(eigval)[::-1]
11
eigval, eigvec = eigval[order], eigvec[:, order]
12

<!-- page: 18 -->

print(eigval)
# [7.1758 1.5242]
13
print(Xc @ eigvec[:, 0])
# toa do tren PC1 (co the
doi dau)
14
15
# Cach 2: scikit -learn
16
pca = PCA(n_components=1).fit(X)
17
print(pca.components_)
# [[0.6205 0.7842]]
18
print(pca.explained_variance_ratio_)
# [0.8248]
19
Z = pca.transform(X)
# [2.8491 2.5216 -2.1493
-3.0973 -0.1241]
20
X_rec = pca.inverse_transform(Z)
# tai tao (nam tren duong
PC1)

<!-- page: 100 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
94
[Chỗchèn hình]
images/ch-reduce-pca-2d.png
Hình 10.2: Dữliệu ví dụvới hai trục thành phần chính w1, w2 và hình chiếu của các điểm lên
w1.
10.4.2
Chọn sốthành phần
• Ngưỡng phương sai tích lũy: chọn k nhỏnhất đểP
j≤k λj/ P
j λj ≥90% (hoặc 95%).
Trong scikit-learn chỉcần PCA(n_components=0.95).
• Biểu đồscree (Cattell, 1966): vẽtrịriêng theo thứtự, chọn tại điểm “gãy”.
• Tiêu chí Kaiser: với dữliệu đã chuẩn hóa, giữcác thành phần có λj > 1.
• Theo mục tiêu: k = 2 hoặc 3 đểtrực quan hóa; với bài toán dựđoán, coi k là siêu tham
sốvà chọn bằng kiểm định chéo (Chương 11).
Listing 10.7: PCA trên tập chữsốviết tay

<!-- page: 19 -->

1
from sklearn.datasets import load_digits
2
import matplotlib.pyplot as plt
3
4
digits = load_digits()
# 1797 anh 8x8 = 64 chieu
5
pca = PCA().fit(digits.data)
6
cum = np.cumsum(pca.explained_variance_ratio_)
7
print("So thanh phan giu 95% phuong sai:", np.argmax(cum >= 0.95) +
1)
# 29
8
9
plt.plot(range(1, 65), cum, marker=".")
10
plt.axhline(0.95, linestyle="--"); plt.xlabel("So thanh phan")
11
plt.ylabel("Phuong sai tich luy"); plt.show()
12
13
Z = PCA(n_components=2).fit_transform(digits.data)
14
plt.scatter(Z[:, 0], Z[:, 1], c=digits.target, cmap="tab10", s=8)
15
plt.colorbar(); plt.show()
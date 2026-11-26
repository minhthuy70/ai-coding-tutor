# VI_PY_076: Lập trình hướng đối tượng trong thiết kế mô hình dữ liệu

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân
**Chuyên mục**: OOP | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
58
7
print("Accuracy:", knn.score(X_test , y_test))
8
9
# Cac vi du tinh tay o tren
10
import numpy as np
11
from sklearn.neighbors import KNeighborsRegressor
12
13
X5 = np.array([[7, 6], [2, 4], [1, 5], [3, 9], [8, 7]])
14
y5 = np.array([0, 1, 1, 1, 0])
15
print(KNeighborsClassifier(3).fit(X5, y5).predict([[2, 4]]))
# [1]
16
knn_w = KNeighborsClassifier(4, weights="distance").fit(X5, y5)
17
print(knn_w.predict_proba([[5, 6]]).round(4))
# [[0.5954 0.4046]]
18
19
y_reg = np.array([7.3, 5.4, 4.2, 5.1, 9.6])
20
for w in ["uniform", "distance"]:
21
reg = KNeighborsRegressor(4, weights=w).fit(X5, y_reg)
22
print(w, reg.predict([[3, 4]]).round(4))

# 5.5 ; 5.3082
7.3
Naive Bayes
Định lý Bayes do mục sư Thomas Bayes đềxuất và được công bốsau khi ông mất (1763), sau
đó Pierre-Simon Laplace phát triển độc lập và tổng quát hóa. Năm 1961, Maron dùng mô hình
Bayes “ngây thơ” đểphân loại tài liệu tựđộng; đến cuối thập niên 1990, Naive Bayes trởthành
phương pháp lọc thư rác kinh điển.
Định nghĩa 7.3 (Bộphân lớp Naive Bayes). Theo định lý Bayes:
P(y | x) = P(y) P(x | y)
P(x)
∝P(y) P(x | y).
(7.3)
Giảđịnh “ngây thơ” (naive): các đặc trưng độc lập có điều kiện khi biết lớp, nên P(x | y) =
Qd
j=1 P(xj | y). Nhãn dựđoán là
ˆy = arg max
k
P(y = k)
d
Y
j=1
P(xj | y = k).
(7.4)
Ví dụ7.5 (Lọc thư rác). Một hộp thư có 6 email: 3 spam, 3 không spam (ham). Từ“free” xuất
hiện trong 2/3 email spam và 1/3 email ham; từ“meeting” xuất hiện trong 1/3 email spam và
2/3 email ham. Phân lớp một email có “free” và không có “meeting”:
Spam :
P(spam) · P(free | spam) · P(¬meeting | spam) = 1
2 · 2
3 · 2
3 = 0,2222,
Ham :
P(ham) · P(free | ham) · P(¬meeting | ham) = 1
2 · 1
3 · 1
3 = 0,0556.
Chuẩn hóa: P(spam | x) = 0,2222/(0,2222 + 0,0556) = 0,8. Email được dựđoán là spam với
xác suất 80%.

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
59
Các biến thể.
GaussianNB (đặc trưng liên tục, giảđịnh phân phối chuẩn trong mỗi lớp),

MultinomialNB (đặc trưng đếm — rất hợp với ma trận Count/TF-IDF ởChương 5), BernoulliNB
(đặc trưng nhịphân có/không). Đểtránh xác suất bằng 0 khi một từchưa từng xuất hiện trong
một lớp, dùng làm trơn Laplace: P(xj | y) =
đếm+α
tổng+α·|V | (tham sốalpha).
Listing 7.3: Naive Bayes cho phân loại văn bản kết hợp TF-IDF
1
from sklearn.feature_extraction.text import TfidfVectorizer
2
from sklearn.naive_bayes import MultinomialNB , GaussianNB
3
from sklearn.pipeline import make_pipeline
4
5
texts = ["free money now", "win a free prize", "free offer today",
6
"meeting at noon", "project meeting notes", "lunch meeting
free"]
7
labels = ["spam", "spam", "spam", "ham", "ham", "ham"]
8
9
spam_filter = make_pipeline(TfidfVectorizer(), MultinomialNB(alpha
=1.0))
10
spam_filter.fit(texts, labels)
11
print(spam_filter.predict(["free prize money", "notes from the
meeting"]))
12
print(spam_filter.predict_proba(["free prize money"]).round(3))
13
14
# Du lieu so lien tuc: GaussianNB
15
print(GaussianNB().fit(X_train , y_train).score(X_test, y_test))
Dù giảđịnh độc lập hiếm khi đúng, Naive Bayes thường cho kết quảtốt bất ngờvới văn bản,
huấn luyện cực nhanh và cần ít dữliệu. Nhược điểm: xác suất ước lượng thường bị“quá tựtin”
(gần 0 hoặc 1).
7.4
Hồi quy logistic (Logistic Regression)
Hàm logistic được nhà toán học BỉPierre-François Verhulst dùng từthập niên 1830–1840 để
mô tảtăng trưởng dân số. Năm 1958, David Cox đềxuất mô hình hồi quy logistic cho biến đầu
ra nhịphân. Dù tên gọi có chữ“hồi quy”, đây là thuật toán phân lớp.
Định nghĩa 7.4 (Hồi quy logistic nhịphân). Mô hình ước lượng xác suất thuộc lớp dương:

P(y = 1 | x) = σ(w⊤x + b),
σ(z) =
1
1 + e−z ,
(7.5)
và dựđoán ˆy = 1 khi xác suất ≥0,5, tức khi w⊤x + b ≥0. Do đó biên quyết định là một siêu
phẳng.
z
−2
0
1
2
σ(z)
0.1192
0.5
0.7311
0.8808
Bảng 7.3: Một sốgiá trịcủa hàm sigmoid

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
60
Hàm mất mát.
Tham sốđược tìm bằng cách cực tiểu entropy chéo (log loss), tương đương
cực đại hợp lý:
J(w, b) = −1
n
n
X
i=1
h
yi ln ˆpi + (1 −yi) ln(1 −ˆpi)
i
,
ˆpi = σ(w⊤xi + b).
(7.6)
Hàm này lồi, không có nghiệm đóng, nên được giải bằng Gradient Descent hoặc các phương
pháp tối ưu bậc hai (thuật toán lbfgs mặc định của scikit-learn). Gradient có dạng rất gọn:
∇wJ = 1
n
P
i(ˆpi −yi) xi — giống hệt hồi quy tuyến tính, chỉthay ˆy bằng ˆp.
Diễn giải.
ln

p
1−p = w⊤x + b: mỗi khi xj tăng 1 đơn vị, odds (tỉsốp/(1 −p)) được nhân với
ewj. Đây là lý do hồi quy logistic được ưa chuộng trong y khoa và tài chính, nơi cần giải thích
mô hình.
Đa lớp.
Với K lớp, dùng hàm softmax: P(y = k | x) =
ezk
∑
j ezj với zk = w⊤
k x + bk. Tham
sốC trong scikit-learn là nghịch đảo của mức chính quy hóa L2 (giống Ridge): C nhỏ⇒chính
quy hóa mạnh.
Listing 7.4: Logistic Regression với scikit-learn
1
from sklearn.linear_model import LogisticRegression
2
3
logreg = make_pipeline(StandardScaler(), LogisticRegression(C=1.0,
max_iter=1000))
4
logreg.fit(X_train , y_train)
5
print("Accuracy:", logreg.score(X_test , y_test))
6
print(logreg.predict_proba(X_test[:3]).round(3))
# xac suat 3 lop
7
print(logreg[-1].coef_.round(2))
# he so cho tung
lop
[Chỗchèn hình]
images/ch-classify-sigmoid.png
Hình 7.2: Đồthịhàm sigmoid σ(z) và ngưỡng quyết định 0,5.
7.5
Cây quyết định (Decision Tree)
Cây quyết định mô phỏng cách con người ra quyết định bằng chuỗi câu hỏi “nếu – thì”. Hai
dòng thuật toán kinh điển: CART (Classification and Regression Trees) của Breiman, Friedman,
Olshen và Stone (1984), và ID3 (1986) cùng hậu duệC4.5 (1993) của Ross Quinlan. scikit-learn
cài đặt phiên bản tối ưu của CART.

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
61
7.5.1

Độđo độhỗn tạp
Tại mỗi nút có tỉlệcác lớp p1, . . . , pK, độ“hỗn tạp” (impurity) được đo bằng:
Gini (CART) :
G = 1 −
K
X
k=1
p2
k,
(7.7)
Entropy (ID3/C4.5) :
H = −
K
X
k=1
pk log2 pk.
(7.8)
Nút “thuần” (chỉmột lớp) có G = H = 0; với hai lớp cân bằng, G = 0,5 và H = 1. Thuật toán
chọn câu hỏi chia nút làm giảm độhỗn tạp nhiều nhất, tính theo trung bình có trọng sốcủa
các nút con. Với entropy, mức giảm này gọi là độlợi thông tin (Information Gain):
IG = H(cha) −
X
c∈con
nc
n H(c).
(7.9)
Ví dụ7.6 (Tính một lần chia nút). Nút cha có 10 mẫu: 6 “Có”, 4 “Không”. Một câu hỏi chia
thành nút trái 4 mẫu (4 Có, 0 Không) và nút phải 6 mẫu (2 Có, 4 Không).
• Gini cha: 1 −(0,62 + 0,42) = 0,48.
• Gini trái: 0; Gini phải: 1 −
(2/6)2 + (4/6)2
= 0,4444.
• Gini sau chia: 0,4 × 0 + 0,6 × 0,4444 = 0,2667 ⇒giảm 0,2133.
• Entropy cha: 0,9710; entropy phải: 0,9183; IG = 0,9710 −0,6 × 0,9183 = 0,4200.
Thuật toán thửmọi đặc trưng và mọi ngưỡng, rồi chọn phép chia có mức giảm lớn nhất.
Kiểm soát quá khớp.
Cây phát triển hết cỡsẽcó lá thuần, khớp hoàn hảo dữliệu huấn luyện
nhưng tổng quát kém. Các tham sốgiới hạn: max_depth, min_samples_split, min_samples_leaf,
hoặc cắt tỉa sau bằng ccp_alpha.
Ưu điểm.
Dễdiễn giải, vẽđược; không cần chuẩn hóa dữliệu; xửlý được quan hệphi tuyến
và tương tác. Nhược điểm: không ổn định (đổi dữliệu một chút, cây thay đổi nhiều), dễquá
khớp — được khắc phục bởi Random Forest ởchương sau.
Listing 7.5: Cây quyết định và trực quan hóa
1

from sklearn.tree import DecisionTreeClassifier , export_text ,
plot_tree
2
import matplotlib.pyplot as plt
3
4
tree = DecisionTreeClassifier(criterion="gini", max_depth=3,
random_state=42)
5
tree.fit(X_train , y_train)
6
print("Accuracy:", tree.score(X_test , y_test))
7
print(export_text(tree, feature_names=iris.feature_names))
8
9
plt.figure(figsize=(12, 6))
10
plot_tree(tree, feature_names=iris.feature_names ,
11
class_names=iris.target_names , filled=True)
12
plt.show()

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
62
[Chỗchèn hình]
images/ch-classify-tree.png
Hình 7.3: Cây quyết định độsâu 3 trên dữliệu Iris (kết quảcủa plot_tree).
7.6
Máy vector hỗtrợ(SVM)
Ý tưởng siêu phẳng lềcực đại được Vladimir Vapnik và Alexey Chervonenkis phát triển tại Liên
Xô từthập niên 1960. Năm 1992, Boser, Guyon và Vapnik kết hợp với thủthuật nhân (kernel
trick) đểtạo biên phi tuyến; năm 1995, Cortes và Vapnik đềxuất phiên bản lềmềm (soft margin)
dùng phổbiến đến ngày nay.
7.6.1
Lềcực đại
Với dữliệu hai lớp yi ∈{−1, +1} tách được tuyến tính, có vô sốsiêu phẳng w⊤x + b = 0 phân
tách hai lớp. SVM chọn siêu phẳng có lề(khoảng cách đến điểm gần nhất của mỗi lớp) lớn nhất.
Độrộng lềbằng 2/∥w∥, nên bài toán là:
min
w,b
1

2∥w∥2
với
yi(w⊤xi + b) ≥1, ∀i.
(7.10)
Các điểm nằm đúng trên biên của lềgọi là vector hỗtrợ(support vectors); chỉchúng quyết định
siêu phẳng — bỏcác điểm khác đi, kết quảkhông đổi.
7.6.2
Lềmềm và tham sốC
Dữliệu thực thường không tách được hoàn toàn. Lềmềm cho phép vi phạm với biến bù ξi ≥0:
min
w,b,ξ
1
2∥w∥2 + C
n
X
i=1
ξi
với
yi(w⊤xi + b) ≥1 −ξi.
(7.11)
C lớn: phạt vi phạm nặng, lềhẹp, dễquá khớp; C nhỏ: lềrộng, chấp nhận sai một sốđiểm, tổng
quát tốt hơn.
7.6.3
Thủthuật nhân
Ý tưởng: ánh xạdữliệu sang không gian nhiều chiều hơn, nơi chúng tách được tuyến tính. Vì
bài toán đối ngẫu của SVM chỉcần tích vô hướng giữa các điểm, ta thay tích vô hướng bằng
một hàm nhân k(x, z) mà không cần tính ánh xạtường minh:

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
63
• Tuyến tính: k(x, z) = x⊤z.
• Đa thức: k(x, z) = (γ x⊤z + r)p.
• RBF (Gauss): k(x, z) = exp(−γ∥x −z∥2) — mặc định trong scikit-learn; γ lớn cho biên
càng “uốn lượn”.
[Chỗchèn hình]
images/ch-classify-svm.png
Hình 7.4: SVM tuyến tính: siêu phẳng phân tách, lềcực đại và các vector hỗtrợ(khoanh tròn).
Listing 7.6: SVM với tìm kiếm tham sốC và gamma
1
from sklearn.svm import SVC
2
from sklearn.model_selection import GridSearchCV
3

4
svm = make_pipeline(StandardScaler(), SVC(kernel="rbf"))
5
grid = GridSearchCV(svm, {"svc__C": [0.1, 1, 10, 100],
6
"svc__gamma": [0.01, 0.1, 1]}, cv=5)
7
grid.fit(X_train , y_train)
8
print(grid.best_params_ , grid.score(X_test, y_test))
9
print("So vector ho tro:", grid.best_estimator_[-1].n_support_)
SVM cần chuẩn hóa dữliệu (vì dựa trên khoảng cách và tích vô hướng), hoạt động tốt trên
dữliệu sốchiều cao như văn bản, nhưng huấn luyện chậm khi sốmẫu lớn (độphức tạp cỡO(n2)
đến O(n3)) và không trực tiếp cho xác suất.
7.7
So sánh các thuật toán
Listing 7.7: So sánh năm thuật toán bằng kiểm định chéo
1
from sklearn.model_selection import cross_val_score
2
3
models = {
4
"KNN":
make_pipeline(StandardScaler(),
KNeighborsClassifier(5)),
5
"NaiveBayes":
GaussianNB(),
6
"Logistic":
make_pipeline(StandardScaler(), LogisticRegression
(max_iter=1000)),
7
"DecisionTree": DecisionTreeClassifier(max_depth=3, random_state
=42),

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
64
8
"SVM":
make_pipeline(StandardScaler(), SVC()),

9
}
10
for name, m in models.items():
11
s = cross_val_score(m, X, y, cv=5)
12
print(f"{name:12s} {s.mean():.3f} +/- {s.std():.3f}")
Thuật toán
Biên
quyết
định
Cần
chuẩn
hóa
Ưu điểm
Nhược điểm
KNN
Linh hoạt
Có
Đơn giản, không cần
huấn luyện
Chậm khi dựđoán,
kém ởsốchiều cao
Naive Bayes
Tuyến
tính/bậc 2
Không
Rất nhanh, tốt với văn
bản
Giảđịnh độc lập, xác
suất quá tựtin
Logistic
Regression
Tuyến tính
Có
Cho xác suất, dễdiễn
giải
Không nắm bắt phi
tuyến nếu không tạo
đặc trưng
Decision Tree
Song
song
trục

Không
Dễgiải thích, xửlý dữ
liệu hỗn hợp
Dễquá khớp, không
ổn định
SVM
Tuyến
tính
hoặc
theo
nhân
Có
Mạnh ởsốchiều cao,
lềtối ưu
Chậm với dữliệu lớn,
khó chọn tham số
Bảng 7.4: So sánh các thuật toán phân lớp cơ bản
Các chỉsốđánh giá như ma trận nhầm lẫn, precision, recall, F1 và ROC-AUC được trình
bày ởchương Đánh giá mô hình.
7.8
Tóm tắt chương
• KNN gán nhãn theo đa sốcủa K láng giềng gần nhất; bỏphiếu có trọng số1/(d+ε) giúp
phá thếhòa; với hồi quy, KNN lấy trung bình (có trọng số) giá trịmục tiêu của láng giềng.
Cần chuẩn hóa dữliệu và chọn K phù hợp.
• Naive Bayes áp dụng định lý Bayes với giảđịnh độc lập có điều kiện; rất hiệu quảcho
văn bản.
• Logistic Regression ước lượng xác suất qua hàm sigmoid/softmax, tối ưu entropy chéo;
biên tuyến tính, dễdiễn giải.
• Cây quyết định chia nút theo Gini hoặc Entropy; dễgiải thích nhưng dễquá khớp.
• SVM tìm siêu phẳng lềcực đại; thủthuật nhân cho phép biên phi tuyến.
7.9
Bài tập
1. Cho 6 điểm P1(1, 1), P2(2, 1), P3(1, 2) thuộc lớp A và P4(5, 5), P5(6, 5), P6(5, 6) thuộc
lớp B. (a) Phân lớp q = (2,5; 2,5) với K = 3 (đáp số: A). (b) Phân lớp q = (4, 4) với
K = 1, 3, 5. Khi K = 5, kết quảcó thay đổi nếu dùng bỏphiếu có trọng số1/d không?

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
65
2. Với dữliệu Bảng 7.2, dựđoán y tại q = (6, 6) bằng KNN hồi quy với K = 2 và K = 3,
theo cảtrung bình đều và trung bình có trọng số. Kiểm tra bằng KNeighborsRegressor.
3. Trong ví dụlọc thư rác, tính lại xác suất spam khi email có cả“free” và “meeting”.
4. Một nút có 8 mẫu (5 A, 3 B) được chia thành hai nút (4 A, 0 B) và (1 A, 3 B). Tính Gini,
Entropy trước và sau chia và độlợi thông tin.

5. Chứng minh σ′(z) = σ(z)(1 −σ(z)) và suy ra công thức gradient của hàm log loss.
6. Trên bộdữliệu load_breast_cancer, so sánh năm thuật toán có và không có StandardScaler.
Thuật toán nào nhạy với chuẩn hóa nhất? Giải thích.
7. Dùng TfidfVectorizer kết hợp MultinomialNB và LinearSVC trên bộdữliệu 20
Newsgroups (hàm fetch_20newsgroups, chọn 4 chủđề). So sánh độchính xác và thời
gian huấn luyện.
Tài liệu tham khảo của chương
1. Bayes, T. (1763). An Essay towards Solving a Problem in the Doctrine of Chances. Philosophical
Transactions of the Royal Society of London, 53, 370–418.
2. Boser, B. E., Guyon, I. M., & Vapnik, V. N. (1992). A training algorithm for optimal
margin classifiers. Proceedings of COLT ’92, 144–152.
3. Breiman, L., Friedman, J., Olshen, R., & Stone, C. (1984). Classification and Regression
Trees. Wadsworth.
4. Cortes, C., & Vapnik, V. (1995). Support-vector networks. Machine Learning, 20(3), 273–
297.
5. Cover, T., & Hart, P. (1967). Nearest neighbor pattern classification. IEEE Transactions
on Information Theory, 13(1), 21–27.
6. Cox, D. R. (1958). The Regression Analysis of Binary Sequences. Journal of the Royal
Statistical Society, Series B, 20(2), 215–242.
7. Dudani, S. A. (1976). The Distance-Weighted k-Nearest-Neighbor Rule. IEEE Transactions
on Systems, Man, and Cybernetics, SMC-6(4), 325–327.
8. Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals
of Eugenics, 7(2), 179–188.
9. Fix, E., & Hodges, J. L. (1951). Discriminatory Analysis. Nonparametric Discrimination:
Consistency Properties. USAF School of Aviation Medicine, Randolph Field, Texas.
10. Maron, M. E. (1961). Automatic Indexing: An Experimental Inquiry. Journal of the ACM,
8(3), 404–417.
11. Quinlan, J. R. (1986). Induction of decision trees. Machine Learning, 1(1), 81–106.

Chương 8:
Học kết hợp
(Ensemble Learning)
Một cây quyết định đơn lẻdễquá khớp và không ổn định; một mô hình tuyến tính có thểquá đơn
giản. Học kết hợp (ensemble learning) xây dựng nhiều mô hình rồi gộp dựđoán của chúng,
thường cho kết quảtốt hơn bất kỳmô hình thành phần nào. Trong kếhoạch giảng dạy, các thuật
toán Random Forest, AdaBoost, XGBoost thuộc nhóm phân lớp; chúng cũng dùng được cho
hồi quy. Trên dữliệu dạng bảng (tabular), các phương pháp boosting hiện vẫn là lựa chọn hàng
đầu trong nhiều cuộc thi khoa học dữliệu.
Sau khi học xong chương này, người học có khảnăng:
• Giải thích vì sao kết hợp nhiều mô hình yếu lại cho mô hình mạnh (định lý bồi thẩm đoàn
Condorcet, phân rã độchệch – phương sai).
• Phân biệt hai chiến lược chính: bagging (song song, giảm phương sai) và boosting (tuần
tự, giảm độchệch).
• Tựtính một vòng cập nhật trọng sốcủa AdaBoost.

• Cài đặt và tinh chỉnh Random Forest, AdaBoost, Gradient Boosting, XGBoost; đọc mức
độquan trọng của đặc trưng.
8.1
Trí tuệđám đông
Năm 1785, Hầu tước de Condorcet phát biểu định lý bồi thẩm đoàn: nếu mỗi thành viên độc
lập đưa ra quyết định đúng với xác suất p > 0,5, thì xác suất quyết định theo đa sốlà đúng sẽ
tăng dần về1 khi sốthành viên tăng. Năm 1907, Francis Galton quan sát 787 người dựđoán cân
nặng một con bò tại hội chợ: giá trịtrung vịcác dựđoán chỉlệch khoảng 1% so với cân nặng
thật — chính xác hơn hầu hết từng cá nhân.
Ví dụ8.1. Ba bộphân lớp độc lập, mỗi bộđúng với xác suất 0,7. Bỏphiếu đa sốđúng khi có ít
nhất 2 trong 3 bộđúng:
P(đa sốđúng) = 0,73 + 3 × 0,72 × 0,3 = 0,343 + 0,441 = 0,784 > 0,7.
Điều kiện then chốt là các mô hình phải đủtốt (tốt hơn đoán ngẫu nhiên) và đa dạng (sai
ởnhững chỗkhác nhau). Nếu cảba mô hình giống hệt nhau, bỏphiếu chẳng cải thiện gì. Mọi
phương pháp ensemble đều là các cách khác nhau đểtạo ra sựđa dạng.
66

CHƯƠNG 8. HỌC KẾT HỢP
(ENSEMBLE LEARNING)
67
8.1.1
Độchệch và phương sai
Sai sốkỳvọng của một mô hình trên dữliệu mới có thểphân rã thành
Sai số= Độchệch2 + Phương sai + Nhiễu không thểgiảm.
(8.1)
Độchệch (bias) cao: mô hình quá đơn giản, thiếu khớp. Phương sai (variance) cao: mô hình
thay đổi mạnh theo dữliệu huấn luyện, quá khớp. Lấy trung bình B mô hình có phương sai σ2,
tương quan đôi một ρ, phương sai của trung bình là
ρ σ2 + 1 −ρ
B
σ2,
(8.2)
nên giảm tương quan ρ giữa các mô hình là chìa khóa — đây chính là ý tưởng của Random
Forest.
[Chỗchèn hình]
images/ch-ensemble-bagging-boosting.png
Hình 8.1: So sánh hai chiến lược: bagging huấn luyện song song trên các mẫu bootstrap rồi bỏ
phiếu; boosting huấn luyện tuần tự, mỗi mô hình tập trung vào lỗi của mô hình trước.
8.2
Bagging và Random Forest
8.2.1
Bagging
Bagging (Bootstrap AGGregatING) do Leo Breiman đềxuất năm 1996:
1. Tạo B mẫu bootstrap: mỗi mẫu gồm n điểm được rút có hoàn lại từn điểm huấn luyện

(kỹthuật bootstrap của Efron, 1979).
2. Huấn luyện một mô hình (thường là cây quyết định sâu) trên mỗi mẫu.
3. Dựđoán bằng bỏphiếu đa số(phân lớp) hoặc lấy trung bình (hồi quy).
Xác suất một điểm không được chọn vào một mẫu bootstrap là (1−1/n)n ≈e−1 ≈0,368. Như
vậy mỗi cây chỉthấy khoảng 63,2% dữliệu; 36,8% còn lại gọi là dữliệu ngoài túi (out-of-bag,
OOB) và được dùng đểước lượng sai sốmiễn phí, không cần tập kiểm tra riêng.

CHƯƠNG 8. HỌC KẾT HỢP
(ENSEMBLE LEARNING)
68
8.2.2
Random Forest
Năm 2001, Breiman đềxuất Random Forest: bagging cây quyết định, và thêm một nguồn ngẫu
nhiên — tại mỗi nút, chỉxét một tập con ngẫu nhiên gồm m đặc trưng đểchọn phép chia (thường
m =
√
d cho phân lớp). Nhờvậy, dù có một đặc trưng rất mạnh, không phải cây nào cũng dùng
nó ởgốc; các cây ít tương quan hơn và phương sai của rừng giảm mạnh.
Tham số
Ý nghĩa
n_estimators
Sốcây; càng nhiều càng ổn định (không gây quá khớp),
chỉtốn thời gian.
max_features
Sốđặc trưng xét ởmỗi nút ("sqrt", "log2", sốthực);
nhỏ⇒cây đa dạng hơn.
max_depth, min_samples_leaf
Giới hạn độsâu và kích thước lá của từng cây.
oob_score
Tính độchính xác trên dữliệu ngoài túi.
n_jobs=-1
Huấn luyện song song trên mọi nhân CPU.
Bảng 8.1: Các tham sốchính của RandomForestClassifier
Mức độquan trọng của đặc trưng.
Random Forest cung cấp feature_importances_: tổng
mức giảm Gini do mỗi đặc trưng đóng góp, lấy trung bình qua các cây. Chỉsốnày thiên vịđặc
trưng có nhiều giá trị; permutation importance (xáo trộn một cột và đo mức giảm độchính
xác trên tập kiểm tra) đáng tin cậy hơn.
Listing 8.1: Random Forest trên dữliệu ung thư vú Wisconsin
1
from sklearn.datasets import load_breast_cancer
2
from sklearn.model_selection import train_test_split
3

from sklearn.ensemble import RandomForestClassifier
4
from sklearn.inspection import permutation_importance
5
import pandas as pd
6
7
data = load_breast_cancer()
8
X, y = data.data, data.target
# 569 mau, 30 dac trung
9
X_train , X_test , y_train , y_test = train_test_split(
10
X, y, test_size=0.25, random_state=42, stratify=y)
11
12
rf = RandomForestClassifier(n_estimators=300, max_features="sqrt",
13
oob_score=True, n_jobs=-1, random_state
=42)
14
rf.fit(X_train , y_train)
15
print("OOB score :", rf.oob_score_)
16
print("Test score:", rf.score(X_test , y_test))
17
18
imp = pd.Series(rf.feature_importances_ , index=data.feature_names)
19
print(imp.sort_values(ascending=False).head(5))
20
21
perm = permutation_importance(rf, X_test, y_test, n_repeats=10,
random_state=0)
22
print(pd.Series(perm.importances_mean , index=data.feature_names)
23
.sort_values(ascending=False).head(5))

CHƯƠNG 8. HỌC KẾT HỢP
(ENSEMBLE LEARNING)
69

[Chỗchèn hình]
images/ch-ensemble-rf-importance.png
Hình 8.2: Mức độquan trọng của 10 đặc trưng hàng đầu theo Random Forest trên dữliệu ung
thư vú.
8.3
AdaBoost
Năm 1988, Michael Kearns và Leslie Valiant đặt câu hỏi: liệu có thể“khuếch đại” một tập các bộ
học yếu (chỉtốt hơn đoán ngẫu nhiên một chút) thành một bộhọc mạnh? Robert Schapire trảlời
khẳng định năm 1990, và năm 1997 Yoav Freund cùng Schapire công bốAdaBoost (Adaptive
Boosting) — công trình được trao giải Gödel năm 2003.
Định nghĩa 8.1 (Thuật toán AdaBoost nhịphân, yi ∈{−1, +1}).
1. Khởi tạo trọng sốcác
mẫu wi = 1/n.
2. Với t = 1, . . . , T:
(a) Huấn luyện bộhọc yếu ht (thường là gốc cây – decision stump, cây độsâu 1) trên
dữliệu có trọng sốw.
(b) Tính sai sốcó trọng sốεt = P
i: ht(xi)̸=yi wi.
(c) Tính trọng sốcủa bộhọc: αt = 1
2 ln 1−εt
εt .
(d) Cập nhật: wi ←wi · e−αtyiht(xi), rồi chuẩn hóa đểP
i wi = 1.
3. Dựđoán: H(x) = sign
 PT
t=1 αtht(x)

.
Mẫu bịđoán sai được nhân với eαt > 1 (tăng trọng số), mẫu đoán đúng nhân với e−αt < 1
(giảm trọng số). Bộhọc kếtiếp vì thếphải “chú ý” nhiều hơn đến các mẫu khó. Bộhọc có sai
sốnhỏcó αt lớn, tức tiếng nói lớn hơn trong lần bỏphiếu cuối.
Ví dụ8.2 (Một vòng AdaBoost). Có 10 mẫu, trọng sốban đầu 0,1. Bộhọc yếu đầu tiên đoán
sai 3 mẫu:
• ε1 = 3 × 0,1 = 0,3;
α1 = 1
2 ln 0,7
0,3 = 0,4236.
• Mẫu sai: 0,1 × e0,4236 = 0,1 × 1,5275 = 0,15275.
• Mẫu đúng: 0,1 × e−0,4236 = 0,1 × 0,6547 = 0,06547.
• Hằng sốchuẩn hóa: Z = 3 × 0,15275 + 7 × 0,06547 = 0,9165.
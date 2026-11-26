# VI_PY_081: Kỹ thuật kiểm định tính hợp lệ của dữ liệu đầu vào bằng assert

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân
**Chuyên mục**: Kiểm thử | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 8. HỌC KẾT HỢP
(ENSEMBLE LEARNING)
72
[Chỗchèn hình]
images/ch-ensemble-boosting-curve.png
Hình 8.3: Sai sốtrên tập huấn luyện và tập kiểm định theo sốcây của Gradient Boosting; điểm
dừng sớm (early stopping) là nơi sai sốkiểm định nhỏnhất.
8.5
Voting và Stacking
Ngoài việc dùng nhiều phiên bản của cùng một thuật toán, ta có thểkết hợp các thuật toán khác
loại:
• Voting: bỏphiếu cứng (đa sốnhãn) hoặc mềm (trung bình xác suất) giữa các mô hình như
Logistic Regression, SVM, Random Forest.
• Stacking (Wolpert, 1992): dùng dựđoán của các mô hình tầng 1 làm đầu vào cho một mô
hình tầng 2 (meta-learner); các dựđoán này phải lấy từkiểm định chéo đểtránh rò rỉ.
Listing 8.4: Voting và Stacking
1
from sklearn.ensemble import VotingClassifier , StackingClassifier
2
from sklearn.linear_model import LogisticRegression
3
from sklearn.svm import SVC
4
from sklearn.pipeline import make_pipeline
5
from sklearn.preprocessing import StandardScaler
6
7
base = [
8
("lr",
make_pipeline(StandardScaler(), LogisticRegression(
max_iter=1000))),
9

("svm", make_pipeline(StandardScaler(), SVC(probability=True))),
10
("rf",
RandomForestClassifier(n_estimators=200, random_state=42)
),
11
]
12
vote = VotingClassifier(base, voting="soft").fit(X_train , y_train)
13
stack = StackingClassifier(base, final_estimator=LogisticRegression()
, cv=5)
14
stack.fit(X_train , y_train)
15
print("Voting:", vote.score(X_test , y_test), "Stacking:", stack.score
(X_test , y_test))

CHƯƠNG 8. HỌC KẾT HỢP
(ENSEMBLE LEARNING)
73
8.6
Tổng kết so sánh
Phương pháp
Chiến lược
Giảm chủyếu
Ưu điểm
Nhược điểm
Bagging
/
Random Forest
Song song
Phương sai
Ổn định, ít cần tinh
chỉnh, có OOB
Mô hình lớn, khó
diễn giải
AdaBoost
Tuần tự
Độchệch
Đơn giản, lý thuyết
đẹp
Nhạy
nhiễu

và
ngoại lai
Gradient
Boosting
/
XGBoost
Tuần tự
Độchệch (và
phương sai nhờ
chính quy hóa)
Độchính xác cao
nhất
trên
dữ
liệu
bảng
Nhiều
tham
số,
dễquá khớp nếu
không dừng sớm
Voting
/
Stacking
Kết hợp khác
loại
Cảhai
Tận dụng thếmạnh
từng mô hình
Tốn tài nguyên
Bảng 8.2: So sánh các phương pháp học kết hợp
8.7
Tóm tắt chương
• Ensemble dựa trên “trí tuệđám đông”: các mô hình tốt hơn ngẫu nhiên và đa dạng, khi
kết hợp sẽcho kết quảtốt hơn.
• Bagging huấn luyện trên các mẫu bootstrap, giảm phương sai; Random Forest thêm chọn
đặc trưng ngẫu nhiên ởmỗi nút đểgiảm tương quan giữa các cây.
• AdaBoost tăng trọng sốcác mẫu bịđoán sai; αt = 1
2 ln 1−εt
εt .
• Gradient Boosting khớp từng cây với gradient âm của hàm mất mát; XGBoost bổsung
chính quy hóa, đạo hàm bậc hai và nhiều tối ưu kỹthuật.
8.8
Bài tập
1. Tính xác suất bỏphiếu đa sốđúng với 5 bộphân lớp độc lập, mỗi bộđúng với xác suất

0,6. So sánh với trường hợp 1 bộphân lớp.
2. Mô phỏng bằng Python: rút 1000 mẫu bootstrap từn = 100 điểm và kiểm chứng tỉlệ
điểm ngoài túi xấp xỉ36,8%.
3. Làm tiếp ví dụAdaBoost: ởvòng 2, bộhọc yếu đoán sai 2 mẫu vốn được đoán đúng ở
vòng 1. Tính ε2, α2 và trọng sốmới.
4. Trên dữliệu ung thư vú, vẽđộchính xác của Random Forest theo n_estimators ∈
{1, 5, 10, 50, 100, 300} và theo max_features. Nhận xét.
5. So sánh Decision Tree, Random Forest, AdaBoost, Gradient Boosting và XGBoost trên
Ames Housing (bài toán hồi quy, dùng các lớp ...Regressor). Mô hình nào có RMSE
thấp nhất?

CHƯƠNG 8. HỌC KẾT HỢP
(ENSEMBLE LEARNING)
74
Tài liệu tham khảo của chương
1. Breiman, L. (1996). Bagging Predictors. Machine Learning, 24(2), 123–140.
2. Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5–32.
3. Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. Proceedings
of KDD ’16, 785–794.
4. Condorcet, M. de (1785). Essai sur l’application de l’analyse à la probabilité des décisions
rendues à la pluralité des voix. Paris.
5. Efron, B. (1979). Bootstrap Methods: Another Look at the Jackknife. The Annals of Statistics,
7(1), 1–26.
6. Freund, Y., & Schapire, R. E. (1997). A Decision-Theoretic Generalization of On-Line
Learning and an Application to Boosting. Journal of Computer and System Sciences,
55(1), 119–139.
7. Friedman, J. H. (2001). Greedy Function Approximation: A Gradient Boosting Machine.
The Annals of Statistics, 29(5), 1189–1232.
8. Galton, F. (1907). Vox Populi. Nature, 75, 450–451.
9. Ke, G. et al. (2017). LightGBM: A Highly Efficient Gradient Boosting Decision Tree.
Advances in Neural Information Processing Systems 30.
10. Schapire, R. E. (1990). The Strength of Weak Learnability. Machine Learning, 5(2), 197–
227.
11. Wolpert, D. H. (1992). Stacked Generalization. Neural Networks, 5(2), 241–259.

Chương 9:
Phân cụm
(Clustering)
Các chương trước đều là học có giám sát: dữliệu có sẵn nhãn y. Trong thực tế, phần lớn dữliệu
không có nhãn — gán nhãn tốn kém, hoặc ta chưa biết dữliệu có những nhóm nào. Phân cụm
(clustering) là bài toán học không giám sát (unsupervised learning): tựđộng chia dữliệu thành
các nhóm (cụm) sao cho các điểm trong cùng cụm giống nhau và các điểm ởcụm khác nhau thì
khác nhau. Ứng dụng tiêu biểu: phân khúc khách hàng, gom nhóm tài liệu, nén ảnh (lượng tử

hóa màu), phát hiện bất thường.
Theo kếhoạch giảng dạy, chương này trình bày bốn thuật toán: K-Means, Hierarchical
clustering, DBSCAN, Mean-shift.
Sau khi học xong chương này, người học có khảnăng:
• Phân biệt học có giám sát và không giám sát; nêu các họthuật toán phân cụm chính.
• Tựchạy tay thuật toán K-Means và DBSCAN trên dữliệu nhỏ.
• Đọc và cắt cây phân cấp (dendrogram).
• Chọn sốcụm và đánh giá chất lượng phân cụm bằng phương pháp khuỷu tay và hệsố
Silhouette.
9.1
Bài toán phân cụm
Định nghĩa 9.1 (Phân cụm). Cho tập dữliệu {x1, . . . , xn} ⊂Rd không có nhãn. Phân cụm là
tìm một phép gán c : {1, . . . , n} →{1, . . . , K} (hoặc thêm nhãn “nhiễu”) sao cho độtương tự
trong cụm cao và độtương tựgiữa các cụm thấp.
“Giống nhau” được đo bằng khoảng cách, nên mọi lưu ý ởChương 5 đều áp dụng: phải
chuẩn hóa thang đo và mã hóa One Hot các biến định danh; nếu không, đặc trưng có thang
đo lớn sẽquyết định toàn bộkết quảphân cụm.
75

CHƯƠNG 9. PHÂN CỤM
(CLUSTERING)
76
Họthuật toán
Ý tưởng
Đại diện
Phân hoạch
Chia thành K cụm, tối ưu một
hàm mục tiêu
K-Means, K-Medoids
Phân cấp
Xây dựng cây gộp/tách cụm lồng
nhau
Agglomerative
(single,
complete, average, Ward)
Dựa trên mật độ
Cụm là vùng dày đặc, ngăn cách
bởi vùng thưa
DBSCAN,
OPTICS,
Mean-shift
Dựa trên mô hình
Dữliệu sinh ra từhỗn hợp phân
phối

Gaussian Mixture Model
Bảng 9.1: Các họthuật toán phân cụm
9.2
K-Means
Thuật toán K-Means được Stuart Lloyd tại Bell Labs đềxuất năm 1957 cho bài toán lượng tử
hóa tín hiệu (công bốchính thức năm 1982); tên gọi “k-means” do James MacQueen đặt năm
1967. Đến nay đây vẫn là thuật toán phân cụm được dùng nhiều nhất nhờđơn giản và nhanh.
Định nghĩa 9.2 (Hàm mục tiêu K-Means). Cho sốcụm K, tìm các tâm cụm µ1, . . . , µK và phép
gán c đểcực tiểu tổng bình phương khoảng cách trong cụm (Within-Cluster Sum of Squares –
WCSS, thuộc tính inertia_ trong scikit-learn):
J =
n
X
i=1

xi −µc(i)

2.
(9.1)
Thuật toán Lloyd:
1. Khởi tạo K tâm cụm (ngẫu nhiên, chọn điểm dữliệu, hoặc K-Means++).
2. Bước gán: gán mỗi điểm vào cụm có tâm gần nhất.
3. Bước cập nhật: tâm cụm mới = trung bình cộng các điểm thuộc cụm.
4. Lặp lại bước 2–3 đến khi phép gán không đổi.
Mỗi bước đều không làm tăng J, nên thuật toán luôn hội tụ— nhưng chỉđến cực tiểu địa
phương, phụthuộc vào khởi tạo. Arthur và Vassilvitskii (2007) đềxuất K-Means++: chọn tâm
đầu tiên ngẫu nhiên, các tâm tiếp theo được chọn với xác suất tỉlệvới bình phương khoảng cách
đến tâm gần nhất đã chọn, giúp các tâm tản ra; đây là khởi tạo mặc định của scikit-learn. Tham
sốn_init chạy nhiều lần khởi tạo và giữkết quảcó J nhỏnhất.
Ví dụ9.1 (Chạy tay K-Means). Cho 5 điểm P1(22, 10), P2(25, 15), P3(45, 50), P4(50, 55),
P5(23, 12), K = 2, khởi tạo tâm µ1 = P1 = (22, 10) và µ2 = P4 = (50, 55).
Vòng 1 – bước gán:

CHƯƠNG 9. PHÂN CỤM
(CLUSTERING)
77
Điểm
Tọa độ
d(·, µ1)
d(·, µ2)
Cụm
P1

(22, 10)
0.00
53.00
1
P2
(25, 15)
5.83
47.17
1
P3
(45, 50)
46.14
7.07
2
P4
(50, 55)
53.00
0.00
2
P5
(23, 12)
2.24
50.77
1
Bảng 9.2: Khoảng cách Euclid đến hai tâm khởi tạo
Vòng 1 – bước cập nhật:
µ1 = 1
3

(22, 10) + (25, 15) + (23, 12)

= (23,33; 12,33),
µ2 = 1
2

(45, 50) + (50, 55)

= (47,5; 52,5).
Vòng 2: khoảng cách mới từP1, . . . , P5 đến µ1 là (2,69; 3,14; 43,45; 50,31; 0,47) và đến µ2
là (49,56; 43,73; 3,54; 3,54; 47,33). Phép gán không đổi {P1, P2, P5}, {P3, P4} ⇒hội tụ. Giá
trịhàm mục tiêu J = 42,33.
Listing 9.1: K-Means với scikit-learn (ví dụtrên lớp)
1
import numpy as np
2

from sklearn.cluster import KMeans
3
4
X = np.array([[22, 10], [25, 15], [45, 50], [50, 55], [23, 12]])
5
6
kmeans = KMeans(n_clusters=2, init=X[[0, 3]], n_init=1)
7
kmeans.fit(X)
8
print(kmeans.cluster_centers_)
# [[23.33 12.33] [47.5 52.5]]
9
print(kmeans.labels_)
# [0 0 1 1 0]
10
print(kmeans.inertia_)
# 42.33
11
print(kmeans.predict([[30, 20]]))
# gan diem moi vao cum gan nhat
[Chỗchèn hình]
images/ch-clustering-kmeans-steps.png
Hình 9.1: Các vòng lặp của K-Means trên 5 điểm: khởi tạo tâm, bước gán, bước cập nhật và hội
tụ.
9.2.1
Chọn sốcụm K
Phương pháp khuỷu tay (elbow).
VẽJ (inertia) theo K. J luôn giảm khi K tăng (bằng 0 khi
K = n), nhưng đến một điểm thì giảm chậm lại rõ rệt — “khuỷu tay” của đường cong là ứng
viên tốt cho K.

CHƯƠNG 9. PHÂN CỤM
(CLUSTERING)
78
HệsốSilhouette
(Rousseeuw, 1987). Với mỗi điểm i: a(i) là khoảng cách trung bình đến các
điểm cùng cụm, b(i) là khoảng cách trung bình nhỏnhất đến các điểm của một cụm khác:
s(i) =
b(i) −a(i)
max{a(i), b(i)} ∈[−1, 1].
(9.2)
s(i) gần 1: điểm nằm đúng cụm và xa cụm khác; gần 0: nằm ởranh giới; âm: có lẽbịgán sai
cụm. Silhouette trung bình càng cao, phân cụm càng tốt.

Listing 9.2: Chọn K bằng elbow và silhouette
1
from sklearn.datasets import make_blobs
2
from sklearn.metrics import silhouette_score
3
import matplotlib.pyplot as plt
4
5
X, _ = make_blobs(n_samples=500, centers=4, cluster_std=1.0,
random_state=42)
6
ks, inertias , sils = range(2, 10), [], []
7
for k in ks:
8
km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
9
inertias.append(km.inertia_)
10
sils.append(silhouette_score(X, km.labels_))
11
12
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
13
ax[0].plot(ks, inertias , "o-"); ax[0].set_title("Elbow (inertia)")
14
ax[1].plot(ks, sils, "o-");
ax[1].set_title("Silhouette")
15
plt.show()
[Chỗchèn hình]
images/ch-clustering-elbow.png
Hình 9.2: Đường cong inertia (khuỷu tay tại K = 4) và hệsốSilhouette theo sốcụm.
Hạn chếcủa K-Means.
Phải chọn trước K; giảđịnh cụm có dạng “cầu” và kích thước tương
đương; nhạy với ngoại lai (trung bình bịkéo lệch); chỉdùng được với khoảng cách Euclid (biến
thểK-Medoids dùng được khoảng cách bất kỳ).
9.3
Phân cụm phân cấp (Hierarchical Clustering)
Phân cụm phân cấp bắt nguồn từngành phân loại học số(numerical taxonomy) của Sokal và
Sneath (1963) và được Johnson (1967) hệthống hóa. Kết quảkhông phải một phân hoạch duy
nhất mà là một cây phân cấp (dendrogram): cắt cây ởđộcao nào sẽđược sốcụm tương ứng.

CHƯƠNG 9. PHÂN CỤM
(CLUSTERING)
79
Thuật toán gộp dần (agglomerative, từdưới lên):
1. Ban đầu mỗi điểm là một cụm.
2. Tìm hai cụm gần nhau nhất và gộp chúng lại.
3. Lặp lại đến khi chỉcòn một cụm.
Khoảng cách giữa hai cụm A, B được định nghĩa bởi tiêu chí liên kết (linkage):
Liên kết
Công thức
Đặc điểm
Single
mina∈A,b∈B d(a, b)
Tạo cụm dài, hình dạng tùy ý; dễbị
“hiệu ứng chuỗi”
Complete
maxa∈A,b∈B d(a, b)
Cụm gọn, đường kính nhỏ
Average
trung bình mọi cặp d(a, b)
Cân bằng giữa hai loại trên
Ward (1963)
mức tăng WCSS khi gộp
Cụm kích thước đều; mặc định của
scikit-learn
Bảng 9.3: Các tiêu chí liên kết
Ví dụ9.2 (Single linkage trên dữliệu một chiều). Cho 5 điểm trên trục số: 1, 2, 4, 7, 11.
1. Khoảng cách nhỏnhất là d(1, 2) = 1 ⇒gộp {1, 2} ởđộcao 1.
2. Khoảng cách từ{1, 2} đến 4 là min(3, 2) = 2 (nhỏnhất) ⇒gộp {1, 2, 4} ởđộcao 2.
3. Khoảng cách từ{1, 2, 4} đến 7 là 3 ⇒gộp {1, 2, 4, 7} ởđộcao 3.
4. Cuối cùng gộp với 11 ởđộcao 4.
Cắt dendrogram ởđộcao 3,5 được 2 cụm: {1, 2, 4, 7} và {11}.
Listing 9.3: Phân cụm phân cấp và vẽdendrogram
1
import numpy as np
2
from sklearn.cluster import AgglomerativeClustering
3
from scipy.cluster.hierarchy import linkage , dendrogram
4
import matplotlib.pyplot as plt
5
6
p = np.array([[1], [2], [4], [7], [11]])
7

print(AgglomerativeClustering(n_clusters=2, linkage="single")
8
.fit_predict(p))
# [0 0 0 0 1]
9
10
Z = linkage(p, method="single")
11
print(Z)
# moi dong: [cum_a, cum_b, do_cao, so_diem]
12
dendrogram(Z, labels=["1", "2", "4", "7", "11"])
13
plt.axhline(3.5, linestyle="--")
# duong cat -> 2 cum
14
plt.show()
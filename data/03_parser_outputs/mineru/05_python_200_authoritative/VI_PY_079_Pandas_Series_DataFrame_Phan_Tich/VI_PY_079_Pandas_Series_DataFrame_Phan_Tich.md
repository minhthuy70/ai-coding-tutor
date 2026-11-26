<!-- page: 1 -->
# VI_PY_079: Pandas: Khái niệm Series, DataFrame và các thao tác lọc dữ liệu

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân  
**Chuyên mục**: Pandas | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 102 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
96
Hạn chếcủa PCA.
• Chỉbắt được quan hệtuyến tính; với dữliệu nằm trên đa tạp cong (ví dụ“cuộn Thụy Sĩ”)
cần Kernel PCA, t-SNE (van der Maaten & Hinton, 2008) hoặc UMAP.
• Nhạy với thang đo và ngoại lai (phương sai bịchi phối bởi cột có giá trịlớn).
• Thành phần mới là tổhợp của mọi cột gốc nên khó diễn giải.
• PCA không dùng nhãn: hướng có phương sai lớn chưa chắc là hướng phân biệt lớp tốt
nhất — khi có nhãn, có thểdùng LDA (Fisher, 1936).
10.5
Tóm tắt chương
• Sốchiều lớn làm dữliệu thưa, khoảng cách mất ý nghĩa và tăng nguy cơ quá khớp.
• Phương sai, hiệp phương sai (chú ý dấu và quy ước chia n hay n −1) và cặp trịriêng –
vector riêng (kiểm tra bằng vết, định thức và phép nhân Av = λv) là nền tảng toán học
của SVD và PCA.
• SVD: A = UΣV⊤; giữk giá trịsuy biến lớn nhất cho xấp xỉhạng k tối ưu (Eckart–Young).
Dùng cho nén ảnh, LSA, hệgợi ý.
• PCA tìm các hướng trực giao có phương sai lớn nhất: vector riêng của ma trận hiệp phương
sai, tính thực tếbằng SVD của dữliệu đã chuẩn hóa tâm.
• Chọn sốthành phần theo phương sai tích lũy, biểu đồscree hoặc kiểm định chéo; luôn đặt
PCA trong pipeline.
10.6
Bài tập
1. Tính phương sai (chia n và chia n −1) của (4, 8, 6, 2). Tính hiệp phương sai và hệsố
tương quan của A = (1, 2, 3, 4) và B = (8, 6, 5, 1); giải thích ý nghĩa của dấu. Kiểm tra
bằng np.var, np.cov, np.corrcoef.
2. Tìm trịriêng và vector riêng đơn vịcủa
4
1
2
3

(đáp số: λ = 5 và λ = 2). Kiểm tra kết

<!-- page: 2 -->

quảbằng vết, định thức và np.linalg.eig.
3. Tiếp ví dụSVD của ma trận 5 × 2: tính u2 = Xv2/σ2, kiểm tra u1 ⊥u2 và tái tạo
X = σ1u1v⊤
1 + σ2u2v⊤
2 .
4. Làm lại toàn bộcác bước PCA cho 10 điểm của Smith (2002):
x1 = (2,5; 0,5; 2,2; 1,9; 3,1; 2,3; 2,0; 1,0; 1,5; 1,1),
x2 = (2,4; 0,7; 2,9; 2,2; 3,0; 2,7; 1,6; 1,1; 1,6; 0,9).
(Đáp số: λ1 ≈1,2840, w1 ≈(0,6779; 0,7352), thành phần thứnhất giữkhoảng 96,3%
phương sai.)

<!-- page: 103 -->
CHƯƠNG 10. GIẢM CHIỀU DỮLIỆU
(DIMENSIONALITY REDUCTION)
97
5. Tính tay SVD của A =


2
0
0
1
0
0

và B =
1
1
1
1

. Ma trận nào có hạng 1?
6. Với dữliệu ởBảng 10.2, tái tạo các điểm từ1 thành phần chính và tính tổng bình phương
sai sốtái tạo. So sánh với (n −1)λ2.
7. Chứng minh rằng các tọa độchiếu z trên thành phần chính thứnhất có trung bình 0 và
phương sai λ1.
8. Trên tập load_breast_cancer, so sánh tỉlệphương sai giải thích của PCA khi có và
không có StandardScaler. Giải thích.
9. Nén một bức ảnh bằng SVD với k = 10, 30, 100; tính tỉlệnén và sai sốFrobenius tương
đối.
10. Với tập Ames Housing đã tiền xửlý ởChương 5, đặt PCA vào pipeline Ridge. Dùng
GridSearchCV đểchọn n_components.
Tài liệu tham khảo của chương
1. Bellman, R. (1957). Dynamic Programming. Princeton University Press.
2. Beyer, K., Goldstein, J., Ramakrishnan, R., & Shaft, U. (1999). When Is “Nearest Neighbor”

<!-- page: 3 -->

Meaningful? Proceedings of ICDT ’99, 217–235.
3. Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990).
Indexing by Latent Semantic Analysis. Journal of the American Society for Information
Science, 41(6), 391–407.
4. Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower
rank. Psychometrika, 1(3), 211–218.
5. Golub, G., & Kahan, W. (1965). Calculating the Singular Values and Pseudo-Inverse of a
Matrix. SIAM Journal on Numerical Analysis, 2(2), 205–224.
6. Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components.
Journal of Educational Psychology, 24(6), 417–441.
7. Jolliffe, I. T. (2002). Principal Component Analysis (2nd ed.). Springer.
8. Pearson, K. (1896). Mathematical Contributions to the Theory of Evolution. III. Regression,
Heredity, and Panmixia. Philosophical Transactions of the Royal Society of London, Series
A, 187, 253–318.
9. Pearson, K. (1901). On Lines and Planes of Closest Fit to Systems of Points in Space.
Philosophical Magazine, 2(11), 559–572.
10. Smith, L. I. (2002). A tutorial on Principal Components Analysis. University of Otago.
11. Strang, G. (2016). Introduction to Linear Algebra (5th ed.). Wellesley-Cambridge Press.
12. van der Maaten, L., & Hinton, G. (2008). Visualizing Data using t-SNE. Journal of Machine
Learning Research, 9, 2579–2605.

<!-- page: 104 -->
Chương 11:
Đánh giá và lựa chọn mô hình
(Validation)
Các chương trước đã giới thiệu hàng chục mô hình, mỗi mô hình lại có nhiều siêu tham số. Câu
hỏi trung tâm của chương này là: làm sao biết một mô hình tốt đến đâu trên dữliệu nó chưa
từng thấy, và làm sao chọn được mô hình và siêu tham sốtốt nhất mà không tựlừa mình.
Đánh giá sai là nguyên nhân phổbiến nhất khiến mô hình đạt kết quảrất cao trong phòng thí
nghiệm nhưng thất bại khi triển khai.
Sau khi học xong chương này, người học có khảnăng:
• Giải thích lỗi tổng quát hóa, quá khớp, dưới khớp và đánh đổi bias – variance.
• Thiết kếđúng việc chia dữliệu: train / validation / test, k-fold, stratified, time series split.
• Tính tay và diễn giải các độđo phân lớp (ma trận nhầm lẫn, precision, recall, F1, ROC –
AUC) và hồi quy (MAE, MSE, RMSE, R2).
• Tìm siêu tham sốbằng GridSearchCV, RandomizedSearchCV và tránh rò rỉdữliệu.
11.1
Lỗi tổng quát hóa
Mục tiêu của học máy không phải là khớp dữliệu huấn luyện mà là tổng quát hóa (generalization):
dựđoán tốt trên dữliệu mới lấy từcùng phân phối. Gọi D là phân phối dữliệu và L là hàm mất
mát; lỗi tổng quát hóa (rủi ro thực) của mô hình f là
R(f) = E(x,y)∼D

L(y, f(x))


<!-- page: 4 -->

.
(11.1)
Ta không biết D, nên chỉcó thểước lượng R(f) bằng trung bình mất mát trên một tập dữliệu
độc lập với quá trình huấn luyện. Lỗi trên tập huấn luyện luôn là ước lượng quá lạc quan.
Tình trạng
Lỗi train
Lỗi test
Cách khắc phục
Dưới khớp (underfitting)
Cao
Cao
Mô hình phức tạp hơn, thêm đặc
trưng, giảm điều chuẩn
Vừa khớp
Thấp
Thấp
—
Quá khớp (overfitting)
Rất thấp
Cao
Thêm dữliệu, điều chuẩn, giảm
độphức tạp, ensemble
Bảng 11.1: Chẩn đoán qua lỗi huấn luyện và lỗi kiểm tra
98

<!-- page: 105 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
99
Đối với mất mát bình phương, sai sốkỳvọng tại một điểm phân tích được thành (Geman và
cộng sự, 1992):
E

(y −ˆf(x))2
=
 E[ ˆf(x)] −f(x)
2
|
{z
}
Bias2
+ Var[ ˆf(x)]
|
{z
}

<!-- page: 5 -->

Variance
+ σ2
|{z}
nhiễu
.
(11.2)
Mô hình đơn giản có bias cao, mô hình phức tạp có variance cao; điểm tối ưu nằm ởgiữa.
[Chỗchèn hình]
images/ch-validation-bias-variance.png
Hình 11.1: Lỗi huấn luyện và lỗi kiểm tra theo độphức tạp của mô hình: vùng dưới khớp, vùng
tối ưu và vùng quá khớp.
11.2
Chiến lược chia dữliệu
11.2.1
Hold-out: train / validation / test
• Tập huấn luyện (train): học tham sốmô hình.
• Tập kiểm định (validation): so sánh mô hình, chọn siêu tham số.
• Tập kiểm tra (test): đánh giá một lần duy nhất ởcuối. Nếu dùng tập test đểchọn mô
hình, nó trởthành tập validation và ước lượng không còn khách quan.
Tỉlệthường dùng là 60/20/20 hoặc 70/15/15; với dữliệu rất lớn, tập test chỉcần 1%. Với bài
toán phân lớp, dùng stratify=y đểgiữtỉlệcác lớp.
Listing 11.1: Chia dữliệu ba phần
1
from sklearn.datasets import load_breast_cancer
2
from sklearn.model_selection import train_test_split
3
4
X, y = load_breast_cancer(return_X_y=True)
5
X_tmp, X_test , y_tmp, y_test = train_test_split(
6
X, y, test_size=0.2, stratify=y, random_state=42)
7
X_train , X_val, y_train , y_val = train_test_split(
8
X_tmp, y_tmp, test_size=0.25, stratify=y_tmp, random_state=42)
#
0.25*0.8 = 0.2
9
print(len(X_train), len(X_val), len(X_test))
# 341 114 114

<!-- page: 106 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH

<!-- page: 6 -->

(VALIDATION)
100
11.2.2
Kiểm định chéo k-fold
Hold-out lãng phí dữliệu và kết quảphụthuộc vào cách chia ngẫu nhiên. Kiểm định chéo
(cross-validation), được Stone (1974) và Geisser (1975) hình thức hóa, khắc phục điều này:
1. Chia dữliệu thành k phần (fold) gần bằng nhau.
2. Lần lượt dùng mỗi phần làm tập validation, k −1 phần còn lại làm tập huấn luyện.
3. Điểm cuối cùng là trung bình (và độlệch chuẩn) của k lần đánh giá.
Mỗi mẫu được dùng đểkiểm định đúng một lần. k = 5 hoặc 10 là lựa chọn phổbiến (Kohavi,
1995). Trường hợp k = n gọi là Leave-One-Out (LOOCV): ít bias nhưng tốn kém và có
variance cao.
[Chỗchèn hình]
images/ch-validation-kfold.png
Hình 11.2: Sơ đồkiểm định chéo 5-fold: mỗi lượt một fold (tô đậm) làm tập kiểm định.
Bộchia
Khi nào dùng
KFold
Hồi quy, dữliệu độc lập cùng phân phối
StratifiedKFold
Phân lớp (mặc định của cross_val_score khi mô
hình là bộphân lớp), đặc biệt khi lớp mất cân bằng
GroupKFold
Nhiều mẫu từcùng một đối tượng (bệnh nhân,
khách hàng): mọi mẫu của một nhóm phải nằm
cùng phía
TimeSeriesSplit
Chuỗi thời gian: luôn huấn luyện trên quá khứ,
kiểm định trên tương lai (Chương ??)
Bảng 11.2: Các bộchia dữliệu trong scikit-learn
Listing 11.2: Kiểm định chéo với cross_val_score và cross_validate
1
from sklearn.model_selection import cross_val_score , cross_validate ,
StratifiedKFold
2
from sklearn.pipeline import make_pipeline
3
from sklearn.preprocessing import StandardScaler
4
from sklearn.linear_model import LogisticRegression
5
6
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter
=1000))


<!-- page: 7 -->

<!-- page: 107 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
101
7
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
8
9
scores = cross_val_score(model, X_tmp, y_tmp, cv=cv, scoring="
accuracy")
10
print(scores.round(4), scores.mean().round(4), scores.std().round(4))
11
12
res = cross_validate(model, X_tmp, y_tmp, cv=cv,
13
scoring=["accuracy", "f1", "roc_auc"],
return_train_score=True)
14
print({k: v.mean().round(4) for k, v in res.items() if "test" in k})
Quan trọng: bộtiền xửlý (scaler, encoder, PCA, …) phải nằm trong pipeline đểđược fit lại
trên từng fold huấn luyện. Nếu chuẩn hóa toàn bộdữliệu trước rồi mới kiểm định chéo, thông
tin của fold kiểm định đã rò rỉvào quá trình huấn luyện (xem Chương 5).
11.3
Độđo cho bài toán phân lớp
11.3.1
Ma trận nhầm lẫn
Với bài toán hai lớp (lớp dương là lớp ta quan tâm: có bệnh, thư rác, gian lận …), mọi dựđoán
rơi vào một trong bốn ô:
Dựđoán dương
Dựđoán âm
Thực tếdương
TP (True Positive)
FN (False Negative)
Thực tếâm
FP (False Positive)
TN (True Negative)
Bảng 11.3: Ma trận nhầm lẫn (confusion matrix)
Độđo
Công thức
Ý nghĩa
Accuracy
TP+TN
TP+TN+FP+FN
Tỉlệdựđoán đúng

<!-- page: 8 -->

Precision
TP
TP+FP
Trong các mẫu báo dương, bao
nhiêu là dương thật
Recall (Sensitivity)
TP
TP+FN
Trong các mẫu dương thật, tìm ra
được bao nhiêu
Specificity
TN
TN+FP
Trong các mẫu âm thật, nhận đúng
bao nhiêu
F1-score
2·P·R
P+R
Trung bình điều hòa của precision
và recall
Bảng 11.4: Các độđo phân lớp
Ví dụ11.1 (Tính tay các độđo). Một mô hình sàng lọc bệnh được thửtrên 100 người: 50 người
có bệnh, 50 người không. Kết quả: TP = 40, FN = 10, FP = 5, TN = 45.
Accuracy = 40+45
100
= 0,85,
Precision = 40
45 = 0,8889,
Recall = 40
50 = 0,80,
Specificity = 45
50 = 0,90,
F1 = 2×0,8889×0,80
0,8889+0,80
= 0,8421.

<!-- page: 108 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
102
Mô hình bỏsót 10 trong 50 người bệnh (recall 80%) — với bài toán y tế, đây là điều cần cải
thiện dù accuracy khá cao.
Nghịch lý accuracy.
Với dữliệu mất cân bằng (ví dụ1% giao dịch gian lận), mô hình luôn
đoán “không gian lận” đạt accuracy 99% nhưng recall bằng 0. Khi đó phải dùng precision, recall,

<!-- page: 9 -->

F1 hoặc AUC. Việc ưu tiên precision hay recall tùy vào chi phí của từng loại lỗi: lọc thư rác ưu
tiên precision (không muốn chặn nhầm thư quan trọng), sàng lọc ung thư ưu tiên recall (không
muốn bỏsót).
Bài toán nhiều lớp.
Tính độđo cho từng lớp (một lớp là dương, còn lại là âm) rồi lấy trung
bình: macro (trung bình cộng, mỗi lớp như nhau), weighted (trọng sốtheo sốmẫu), micro (cộng
dồn TP, FP, FN của mọi lớp).
11.3.2
Đường ROC và AUC
Hầu hết bộphân lớp đưa ra điểm sốhoặc xác suất (predict_proba), sau đó so với ngưỡng
(mặc định 0,5). Thay đổi ngưỡng sẽđổi precision lấy recall. Đường ROC (Receiver Operating
Characteristic) — bắt nguồn từlý thuyết phát hiện tín hiệu radar trong Thếchiến II — vẽTPR =
Recall theo FPR = 1 −Specificity khi ngưỡng chạy từcao đến thấp. AUC là diện tích dưới
đường ROC: bằng 1 với bộphân lớp hoàn hảo, 0,5 với đoán ngẫu nhiên. AUC có một diễn giải
xác suất đẹp (Hanley & McNeil, 1982): AUC là xác suất một mẫu dương ngẫu nhiên được chấm
điểm cao hơn một mẫu âm ngẫu nhiên.
Ví dụ11.2 (Tính AUC bằng cách đếm cặp). Bốn mẫu có nhãn y = (0, 0, 1, 1) và điểm số
s = (0,1; 0,4; 0,35; 0,8). Có 2 × 2 = 4 cặp (dương, âm):
• (0,35 vs 0,1): đúng thứtự; (0,35 vs 0,4): sai thứtự;
• (0,8 vs 0,1): đúng; (0,8 vs 0,4): đúng.
AUC = 3/4 = 0,75.
Listing 11.3: Ma trận nhầm lẫn, báo cáo phân lớp và ROC
1
from sklearn.metrics import (confusion_matrix , classification_report ,
2
roc_auc_score , RocCurveDisplay ,
ConfusionMatrixDisplay)
3
4
print(roc_auc_score([0, 0, 1, 1], [0.1, 0.4, 0.35, 0.8]))
# 0.75
5
6
model.fit(X_train , y_train)
7
y_pred = model.predict(X_test)
8
y_score = model.predict_proba(X_test)[:, 1]
9
10
print(confusion_matrix(y_test , y_pred))
11
print(classification_report(y_test , y_pred, digits=4))
12
print("AUC:", roc_auc_score(y_test , y_score))

<!-- page: 10 -->

13
14
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
15
RocCurveDisplay.from_predictions(y_test, y_score)

<!-- page: 109 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
103
[Chỗchèn hình]
images/ch-validation-roc.png
Hình 11.3: Đường ROC của mô hình Logistic Regression trên tập ung thư vú so với đường chéo
của bộđoán ngẫu nhiên.
Với dữliệu mất cân bằng nặng, đường Precision – Recall và diện tích dưới nó (Average
Precision) thường phản ánh chất lượng mô hình rõ hơn ROC (Saito & Rehmsmeier, 2015).
11.4
Độđo cho bài toán hồi quy
Độđo
Công thức
Ghi chú
MAE
1
n
P |yi −ˆyi|
Cùng đơn vịvới y, ít nhạy với ngoại
lai
MSE
1
n
P(yi −ˆyi)2
Phạt nặng sai sốlớn
RMSE
√
MSE
Cùng đơn vịvới y
R2
1 −
∑(yi−ˆyi)2
∑(yi−¯y)2
Tỉlệphương sai được giải thích; có
thểâm
MAPE
1
n

<!-- page: 11 -->

P 


 yi−ˆyi
yi




Sai sốtương đối; không dùng khi
yi ≈0
Bảng 11.5: Các độđo hồi quy
Ví dụ11.3 (Tính tay độđo hồi quy). y = (3; −0,5; 2; 7), ˆy = (2,5; 0; 2; 8). Sai số:
(0,5; −0,5; 0; −1).
MAE = 0,5+0,5+0+1
4
= 0,5,
MSE = 0,25+0,25+0+1
4
= 0,375,
RMSE = 0,6124.
¯y = 2,875, P(yi −¯y)2 = 29,1875, nên R2 = 1 −1,5/29,1875 = 0,9486.
Listing 11.4: Độđo hồi quy trong scikit-learn
1
from sklearn.metrics import (mean_absolute_error , mean_squared_error ,
2
root_mean_squared_error , r2_score)
3
y_true, y_hat = [3, -0.5, 2, 7], [2.5, 0.0, 2, 8]
4
print(mean_absolute_error(y_true , y_hat))
# 0.5
5
print(mean_squared_error(y_true , y_hat))
# 0.375
6
print(root_mean_squared_error(y_true , y_hat))
# 0.6124
7
print(r2_score(y_true , y_hat))
# 0.9486

<!-- page: 110 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)

<!-- page: 12 -->

104
Lưu ý: trong cross_val_score, scikit-learn quy ước “điểm càng lớn càng tốt”, nên các độđo
sai sốcó dạng âm như scoring="neg_root_mean_squared_error".
11.5
Tìm siêu tham số
Tham số(trọng sốhồi quy, ngưỡng chia của cây) được học từdữliệu; siêu tham số(alpha của
Ridge, n_neighbors của KNN, max_depth của cây) phải được chọn trước khi huấn luyện. Ta
chọn siêu tham sốbằng cách tối ưu điểm kiểm định chéo.
• Grid search: thửmọi tổhợp trên lưới giá trị— đầy đủnhưng chi phí tăng theo cấp số
nhân với sốsiêu tham số.
• Random search: lấy mẫu ngẫu nhiên N tổhợp từcác phân phối. Bergstra và Bengio
(2012) chỉra rằng với cùng ngân sách, random search thường tốt hơn vì chỉvài siêu tham
sốthực sựquan trọng.
• Tối ưu Bayes (Optuna, scikit-optimize): dùng kết quảcác lần thửtrước đểchọn điểm thử
tiếp theo.
Listing 11.5: GridSearchCV và RandomizedSearchCV
1
from sklearn.model_selection import GridSearchCV , RandomizedSearchCV
2
from sklearn.svm import SVC
3
from scipy.stats import loguniform
4
5
pipe = make_pipeline(StandardScaler(), SVC())
6
param_grid = {"svc__C": [0.1, 1, 10, 100],
7
"svc__gamma": [0.001, 0.01, 0.1, 1],
8
"svc__kernel": ["rbf"]}
9
grid = GridSearchCV(pipe, param_grid , cv=5, scoring="f1", n_jobs=-1)
10
grid.fit(X_tmp, y_tmp)
# 16 to hop x 5 fold =
80 lan fit
11
print(grid.best_params_ , round(grid.best_score_ , 4))
12
print("Test F1:", round(grid.score(X_test, y_test), 4))
# danh gia
1 lan cuoi
13
14

<!-- page: 13 -->

rand = RandomizedSearchCV(pipe, {"svc__C": loguniform(1e-2, 1e3),
15
"svc__gamma": loguniform(1e-4, 1e0)
},
16
n_iter=30, cv=5, scoring="f1", random_state
=0, n_jobs=-1)
17
rand.fit(X_tmp, y_tmp)
18
print(rand.best_params_)

<!-- page: 111 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
105
[Chỗchèn hình]
images/ch-validation-grid-heatmap.png
Hình 11.4: Bản đồnhiệt điểm F1 kiểm định chéo theo C và gamma của SVM.
Kiểm định chéo lồng nhau.
best_score_ của GridSearchCV là ước lượng lạc quan, vì chính
nó đã được dùng đểchọn siêu tham số(Cawley & Talbot, 2010). Đểước lượng khách quan khi
không có tập test riêng, dùng nested CV: vòng ngoài đánh giá, vòng trong tìm siêu tham số.
Listing 11.6: Nested cross-validation
1
outer = cross_val_score(GridSearchCV(pipe, param_grid , cv=3),
2
X, y, cv=5, scoring="f1")
3
print(outer.mean().round(4), outer.std().round(4))
11.5.1
Đường cong học và đường cong kiểm định
• Learning curve: điểm train và validation theo kích thước tập huấn luyện. Hai đường
cách xa nhau là dấu hiệu quá khớp, thêm dữliệu sẽcó ích; hai đường hội tụởmức thấp
là dưới khớp.
• Validation curve: điểm theo một siêu tham số, cho thấy vùng dưới khớp – quá khớp.
Listing 11.7: Learning curve và validation curve
1
from sklearn.model_selection import LearningCurveDisplay ,
ValidationCurveDisplay
2
from sklearn.tree import DecisionTreeClassifier
3
4
LearningCurveDisplay.from_estimator(pipe, X, y, cv=5,

<!-- page: 14 -->

5
train_sizes=np.linspace(0.1, 1.0,
8))
6
ValidationCurveDisplay.from_estimator(DecisionTreeClassifier(
random_state=0), X, y,
7
param_name="max_depth",
8
param_range=range(1, 15), cv=5)

<!-- page: 112 -->
CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
106
[Chỗchèn hình]
images/ch-validation-curves.png
Hình 11.5: Trái: learning curve; phải: validation curve theo max_depth của cây quyết định.
11.6
Những sai lầm thường gặp
1. Rò rỉdữliệu: tiền xửlý, chọn đặc trưng hoặc cân bằng lớp (SMOTE) trên toàn bộdữliệu
trước khi chia. Cách tránh: mọi bước đặt trong Pipeline.
2. Đặc trưng chứa thông tin tương lai: ví dụdùng “ngày xuất viện” đểdựđoán “có nhập
viện không”.
3. Xáo trộn chuỗi thời gian khi kiểm định chéo.
4. Trùng lặp mẫu giữa train và test (cùng một bệnh nhân, ảnh gần giống nhau).
5. Nhìn tập test nhiều lần đểchỉnh mô hình.
6. Chỉbáo accuracy với dữliệu mất cân bằng; không báo độlệch chuẩn giữa các fold.
11.7
Tóm tắt chương
• Mục tiêu là lỗi tổng quát hóa; lỗi huấn luyện luôn lạc quan. Cân bằng bias và variance.
• Chia train / validation / test; tập test chỉdùng một lần. Kiểm định chéo k-fold cho ước
lượng ổn định hơn; chọn bộchia phù hợp (stratified, group, time series).
• Phân lớp: ma trận nhầm lẫn, precision, recall, F1, ROC – AUC; hồi quy: MAE, MSE,
RMSE, R2.
• Tìm siêu tham sốbằng Grid/Random search trên pipeline; dùng nested CV đểcó ước
lượng khách quan.
11.8
Bài tập
1. Một bộlọc thư rác trên 1000 email (100 thư rác) cho TP = 80, FP = 30. Lập ma trận
nhầm lẫn và tính accuracy, precision, recall, F1, specificity.
2. Tính AUC bằng cách đếm cặp cho y = (1, 0, 1, 0, 1), s = (0,9; 0,8; 0,7; 0,3; 0,2), rồi
kiểm tra bằng roc_auc_score.
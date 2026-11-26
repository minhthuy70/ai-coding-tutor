# VI_PY_082: Kỹ thuật phát hiện và xử lý dữ liệu khuyết thiếu (NaN / None)

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân
**Chuyên mục**: Dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

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
mát; lỗi tổng quát hóa (rủi ro thực) của mô hình f là
R(f) = E(x,y)∼D

L(y, f(x))

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

CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
99
Đối với mất mát bình phương, sai sốkỳvọng tại một điểm phân tích được thành (Geman và
cộng sự, 1992):
E

(y −ˆf(x))2
=
E[ ˆf(x)] −f(x)
2
{z
}
Bias2
+ Var[ ˆf(x)]
{z
}
Variance
+ σ2
|{z}
nhiễu
.
(11.2)
Mô hình đơn giản có bias cao, mô hình phức tạp có variance cao; điểm tối ưu nằm ởgiữa.
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
Tỉlệthường dùng là 60/20/20 hoặc 70/15/15; với dữliệu rất lớn, tập test chỉcần 1%. Với bài
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

CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
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

CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
102
Mô hình bỏsót 10 trong 50 người bệnh (recall 80%) — với bài toán y tế, đây là điều cần cải
thiện dù accuracy khá cao.
Nghịch lý accuracy.
Với dữliệu mất cân bằng (ví dụ1% giao dịch gian lận), mô hình luôn
đoán “không gian lận” đạt accuracy 99% nhưng recall bằng 0. Khi đó phải dùng precision, recall,
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
• (0,35 vs 0,1): đúng thứtự; (0,35 vs 0,4): sai thứtự;
• (0,8 vs 0,1): đúng; (0,8 vs 0,4): đúng.
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
13
14
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
15
RocCurveDisplay.from_predictions(y_test, y_score)

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
Tỉlệphương sai được giải thích; có
thểâm
MAPE
1
n
P

 yi−ˆyi
yi

Sai sốtương đối; không dùng khi
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

CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
104
Lưu ý: trong cross_val_score, scikit-learn quy ước “điểm càng lớn càng tốt”, nên các độđo
sai sốcó dạng âm như scoring="neg_root_mean_squared_error".
11.5
Tìm siêu tham số
Tham số(trọng sốhồi quy, ngưỡng chia của cây) được học từdữliệu; siêu tham số(alpha của
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
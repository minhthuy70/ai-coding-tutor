# VI_PY_075: Thao tác tệp CSV, JSON và xử lý dữ liệu bán cấu trúc

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân
**Chuyên mục**: Dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
46
5.10.2
Những “cái bẫy” khi đọc dữliệu
Quan sát kỹfile dữliệu cho thấy nhiều vấn đềrất điển hình mà người làm ML phải xửlý:
1. “NA” không phải lúc nào cũng là thiếu dữliệu. Ởcác cột Alley, Fence, Pool QC,
Fireplace Qu, Garage Type, Bsmt Qual…, chuỗi NA mang nghĩa “không có” (không
có hẻm, không có hàng rào, không có garage). Nếu đọc bằng pd.read_csv mặc định,
pandas sẽbiến tất cảNA thành NaN và ta đánh mất thông tin. Trong khi đó, ô rỗng (ví
dụLot Frontage ởnhiều dòng, Mas Vnr Type ởmột sốdòng) mới thực sựlà dữliệu
thiếu.
2. Khoảng trắng thừa: cột Sale Type có giá trị"WD " (có dấu cách cuối). Không làm sạch
thì "WD" và "WD " bịcoi là hai nhãn khác nhau khi One Hot.
3. Sốnhưng là phân loại: MS SubClass (020, 060…) là mã loại nhà; dùng trực tiếp như
sốsẽgây thứtựgiảgiống hệt vấn đềcủa Label Encoder.
4. Lỗi nhập liệu: có bản ghi với Garage Yr Blt = 2207 — một năm không thểxảy ra
(nhiều khảnăng là 2007).
5. Ngoại lai: một vài căn có Gr Liv Area trên 4000 ft2 nhưng giá bán thấp bất thường (giao
dịch bán từng phần). Chính De Cock khuyến nghịloại các căn nhà trên 4000 ft2 khi dùng
dữliệu cho giảng dạy. Cột Lot Area cũng lệch phải rất mạnh (tối đa 215245 ft2).
5.10.3
Đọc và khảo sát dữliệu
Listing 5.16: Đọc Ames Housing và giữnguyên ý nghĩa của “NA”
1
import pandas as pd
2
3
# keep_default_na=False: KHONG bien "NA" thanh NaN
4
# na_values=[""]
: chi o rong moi la du lieu thieu
5
df = pd.read_csv("data/AmesHousing.txt", sep="\t",

6
keep_default_na=False, na_values=[""])
7
print(df.shape)
# (2930, 82)
8
9
# Lam sach khoang trang thua o cac cot chu
10
obj_cols = df.select_dtypes("object").columns
11
df[obj_cols] = df[obj_cols].apply(lambda s: s.str.strip())
12
13
# MS SubClass la ma phan loai -> doi sang kieu chuoi
14
df["MS SubClass"] = df["MS SubClass"].astype(str)
15
16
# Thong ke du lieu thieu that su
17
missing = df.isna().sum()
18
print(missing[missing > 0].sort_values(ascending=False))
19
20
# Sua loi nhap lieu va loai ngoai lai theo khuyen nghi cua De Cock
21
df.loc[df["Garage Yr Blt"] > 2010, "Garage Yr Blt"] = None
22
df = df[df["Gr Liv Area"] <= 4000]
23
print(df.shape)
24

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
47
25
print(df["Exter Qual"].value_counts())
26
print(df[["Lot Area", "Gr Liv Area", "SalePrice"]].describe())
[Chỗchèn hình]
images/ch-preprocessing-ames-outliers.png

Hình 5.11: Biểu đồphân tán Gr Liv Area – SalePrice của Ames Housing; các điểm bên phải
ngưỡng 4000 ft2 là ngoại lai.
5.10.4
Xây dựng quy trình tiền xửlý hoàn chỉnh
Ta chọn một tập con đặc trưng đại diện cho từng kiểu dữliệu và áp dụng đúng kỹthuật đã học
cho từng nhóm:
Listing 5.17: Pipeline tiền xửlý cho Ames Housing
1
import numpy as np
2
from sklearn.model_selection import train_test_split
3
from sklearn.compose import ColumnTransformer
4
from sklearn.pipeline import Pipeline
5
from sklearn.impute import SimpleImputer
6
from sklearn.preprocessing import (OneHotEncoder , OrdinalEncoder ,
7
StandardScaler , RobustScaler)
8
9
nominal = ["MS Zoning", "Neighborhood", "Bldg Type", "MS SubClass",
10
"Alley", "Garage Type"]
11
quality = ["Exter Qual", "Kitchen Qual", "Bsmt Qual", "Fireplace Qu"]
12
numeric = ["Gr Liv Area", "Total Bsmt SF", "Garage Cars",
13
"Full Bath", "Year Built", "Overall Qual"]
14
skewed
= ["Lot Area", "Lot Frontage"]
15
16
# "NA" o cac cot chat luong = khong co -> muc thap nhat
17
levels = ["NA", "Po", "Fa", "TA", "Gd", "Ex"]
18
19
X = df[nominal + quality + numeric + skewed]
20
y = np.log(df["SalePrice"])

# log giup giam do lech cua gia
21
22
X_train , X_test , y_train , y_test = train_test_split(
23
X, y, test_size=0.2, random_state=42)
24
25
preprocess = ColumnTransformer([
26
("nom", Pipeline([

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
48
27
("impute", SimpleImputer(strategy="most_frequent")),
28
("onehot", OneHotEncoder(handle_unknown="ignore")),
29
]), nominal),
30
("ord", Pipeline([
31
("impute", SimpleImputer(strategy="constant", fill_value="NA"
)),
32
("ordinal", OrdinalEncoder(categories=[levels] * len(quality)
)),
33
]), quality),
34
("num", Pipeline([
35
("impute", SimpleImputer(strategy="median")),
36
("scale", StandardScaler()),
37
]), numeric),
38
("skew", Pipeline([
39
("impute", SimpleImputer(strategy="median")),
40

("scale", RobustScaler()),
41
]), skewed),
42
])
43
44
# CHI fit tren tap huan luyen, transform cho ca hai tap
45
X_train_t = preprocess.fit_transform(X_train)
46
X_test_t
= preprocess.transform(X_test)
47
print(X_train_t.shape, X_test_t.shape)
48
print(preprocess.get_feature_names_out()[:10])
Ma trận X_train_t thu được chỉgồm các sốthực, đã đồng nhất thang đo và không còn giá
trịthiếu — sẵn sàng cho các mô hình hồi quy ởchương tiếp theo. Khi ghép preprocess với
một mô hình trong cùng một Pipeline, toàn bộquy trình có thểđược đánh giá bằng kiểm định
chéo mà không lo rò rỉdữliệu:
Listing 5.18: Ghép tiền xửlý với mô hình trong một Pipeline
1
from sklearn.linear_model import LinearRegression
2
from sklearn.model_selection import cross_val_score
3
4
model = Pipeline([("prep", preprocess), ("reg", LinearRegression())])
5
scores = cross_val_score(model, X_train , y_train , cv=5, scoring="r2")
6
print(scores.mean().round(3))
5.11
Tóm tắt chương
• Tiền xửlý dữliệu là bước nền tảng trong quy trình KDD (Fayyad và cộng sự, 1996) và
pha Chuẩn bịdữliệu của CRISP-DM; nguyên lý “rác vào, rác ra” nhắc rằng chất lượng
mô hình bịgiới hạn bởi chất lượng dữliệu.
• Dữliệu thiếu có ba cơ chếMCAR, MAR, MNAR (Rubin, 1976). Simple Imputer điền
bằng trung bình/trung vị/mode; KNN Imputer lấy trung bình k láng giềng theo khoảng
cách nan-Euclid
q
d
|P|
P

j∈P(xj −yj)2; Iterative Imputer hồi quy lặp từng cột theo các
cột còn lại — mạnh nhưng có thểngoại suy phi thực tếkhi dữliệu ít hoặc đa cộng tuyến,
nên luôn phải kiểm tra giá trịđiền.

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
49
• Ngoại lai: z-score dễbịche lấp; quy tắc IQR của Tukey bền vững hơn; LOF so sánh mật
độcục bộcủa một điểm với láng giềng, LOF ≫1 là ngoại lai.
• Mô hình ML chỉlàm việc với số: dữliệu chữphải được mã hóa sao cho không tạo ra
quan hệgiả.
• Label Encoder ánh xạnhãn →sốnguyên, gọn nhẹnhưng tạo thứtựgiả; dùng cho biến
mục tiêu. Ordinal Encoder dùng cho đặc trưng thứbậc.
• One Hot Encoder biến mỗi nhãn thành một vector đơn vị, mọi nhãn cách đều
√
2; phù
hợp với KNN, K-Means, mô hình tuyến tính.
• Count Vectorizer biểu diễn văn bản bằng sốlần xuất hiện của từ; TF-IDF (Spärck Jones,
1972) giảm trọng sốcủa các từphổbiến; chuẩn hóa L2 cho phép đo độtương đồng cosine
bằng tích vô hướng.
• Bốn bộchuẩn hóa MinMax, MaxAbs, Standard, Robust khác nhau vềmiền giá trị, khả
năng giữtính thưa và độbền với ngoại lai.
• SMOTE sinh mẫu thiểu sốbằng nội suy xi + λ(xnn −xi); chỉáp dụng trên tập huấn
luyện (dùng Pipeline của imbalanced-learn) và đánh giá bằng recall, precision, F1 thay vì
accuracy.
• Luôn fit trên tập huấn luyện; dùng Pipeline và ColumnTransformer đểquy trình gọn
gàng và tránh rò rỉdữliệu.
5.12
Bài tập
1. Cho dãy gồm các phần tửcat, dog, fish, dog, cat, bird. Hãy (a) tựcài đặt Label Encoder
theo thứtựxuất hiện; (b) so sánh với kết quảcủa LabelEncoder trong scikit-learn và giải
thích vì sao khác nhau.
2. Với dãy ởbài 1, tựcài đặt One Hot Encoder bằng list, for và dictionary. Chứng minh rằng
khoảng cách Euclid giữa hai vector one-hot khác nhau bất kỳluôn bằng
√
2.
3. Thêm câu d4 = “the birds are outside” vào kho văn bản ởmục TF-IDF. Tính tay df(t) và
idf(t) (làm trơn) cho các từare, outside, the, birds, sau đó kiểm tra bằng TfidfVectorizer.
4. Dùng bảng tính (Excel/Google Sheets) dựng lại toàn bộBảng 5.15–5.19. Gợi ý: hàm LN,
SQRT, SUMSQ.
5. Cho cột x = (10, 12, 11, 13, 12, 100). Tính tay kết quảcủa bốn bộchuẩn hóa và nhận xét
bộnào phù hợp nhất. Vì sao?
6. Giải thích vì sao gọi StandardScaler().fit(X) trên toàn bộdữliệu trước khi chia
train/test là rò rỉdữliệu. Thiết kếthí nghiệm trên Ames Housing đểminh họa.

7. Với Ames Housing: đếm sốlượng giá trịNA (“không có”) và ô rỗng (thiếu thật sự) trong
từng cột; bổsung các cột Heating QC, Garage Finish, Foundation vào pipeline với
kỹthuật mã hóa phù hợp.

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
50
8. Cho cột (5, 8, ?, 6, 100, 7). Điền giá trịthiếu bằng trung bình và bằng trung vị. Cách nào
hợp lý hơn? Vì sao? (Đáp số: 25,2 và 7.)
9. Tính khoảng cách nan-Euclid giữa (1, nan, 3, 4) và (2, 5, nan, 6), rồi kiểm tra bằng nan_euclidean_di
10. Với Bảng 5.5, chạy tay lại KNN Imputer với k = 2, sau đó với k = 3 và trọng số1/d. So
sánh với KNNImputer(n_neighbors=2) và KNNImputer(n_neighbors=3, weights="distance"
11. Tiếp tục ví dụIterative Imputer thêm một vòng nữa (bắt đầu từcác giá trịđiền của vòng 1),
rồi so sánh với IterativeImputer(estimator=LinearRegression(), imputation_order="ro
max_iter=2). Giải thích vì sao giá trịcủa x3 không hội tụvềmiền [1; 8].
12. Thêm điểm F(2, 2) vào ví dụLOF và tính lại bảng LOF với k = 3. HệsốLOF của E
thay đổi thếnào?
13. Trên load_breast_cancer, giữlại toàn bộlớp lành tính và chỉ10% lớp ác tính đểtạo
dữliệu mất cân bằng. So sánh recall, precision, F1 của hồi quy logistic khi: không xửlý,
class_weight="balanced", SMOTE trong pipeline, và SMOTE áp dụng sai lên toàn
bộdữliệu trước khi kiểm định chéo.
Tài liệu tham khảo của chương
1. Breunig, M. M., Kriegel, H.-P., Ng, R. T., & Sander, J. (2000). LOF: Identifying Density-
Based Local Outliers. Proceedings of ACM SIGMOD 2000, 93–104.
2. Buitinck, L. et al. (2013). API design for machine learning software: experiences from the
scikit-learn project. ECML PKDD Workshop: Languages for Data Mining and Machine
Learning.
3. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE:
Synthetic Minority Over-sampling Technique. Journal of Artificial Intelligence Research,
16, 321–357.
4. De Cock, D. (2011). Ames, Iowa: Alternative to the Boston Housing Data as an End of
Semester Regression Project. Journal of Statistics Education, 19(3).
5. Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). From Data Mining to Knowledge
Discovery in Databases. AI Magazine, 17(3), 37–54.
6. Han, J., Kamber, M., & Pei, J. (2011). Data Mining: Concepts and Techniques (3rd ed.),
Chương 3: Data Preprocessing. Morgan Kaufmann.
7. Han, H., Wang, W.-Y., & Mao, B.-H. (2005). Borderline-SMOTE: A New Over-Sampling
Method in Imbalanced Data Sets Learning. Advances in Intelligent Computing (ICIC
2005), LNCS 3644, 878–887.
8. Harris, Z. S. (1954). Distributional Structure. Word, 10(2–3), 146–162.
9. Hawkins, D. M. (1980). Identification of Outliers. Chapman and Hall.
10. He, H., Bai, Y., Garcia, E. A., & Li, S. (2008). ADASYN: Adaptive Synthetic Sampling
Approach for Imbalanced Learning. Proceedings of IJCNN 2008, 1322–1328.

CHƯƠNG 5. TIỀN XỬLÝ DỮLIỆU
(DATA PREPROCESSING)
51
11. Lemaître, G., Nogueira, F., & Aridas, C. K. (2017). Imbalanced-learn: A Python Toolbox
to Tackle the Curse of Imbalanced Datasets in Machine Learning. Journal of Machine
Learning Research, 18(17), 1–5.
12. Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008). Isolation Forest. Proceedings of the 8th
IEEE International Conference on Data Mining (ICDM), 413–422.
13. Luhn, H. P. (1957). A Statistical Approach to Mechanized Encoding and Searching of
Literary Information. IBM Journal of Research and Development, 1(4), 309–317.
14. Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine
Learning Research, 12, 2825–2830.
15. Pyle, D. (1999). Data Preparation for Data Mining. Morgan Kaufmann.
16. Rubin, D. B. (1976). Inference and Missing Data. Biometrika, 63(3), 581–592.
17. Rubin, D. B. (1987). Multiple Imputation for Nonresponse in Surveys. Wiley.
18. Salton, G., Wong, A., & Yang, C. S. (1975). A Vector Space Model for Automatic Indexing.
Communications of the ACM, 18(11), 613–620.
19. Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval.
Information Processing & Management, 24(5), 513–523.
20. Shiffler, R. E. (1988). Maximum Z Scores and Outliers. The American Statistician, 42(1),
79–80.
21. Spärck Jones, K. (1972). A statistical interpretation of term specificity and its application
in retrieval. Journal of Documentation, 28(1), 11–21.
22. Stevens, S. S. (1946). On the Theory of Scales of Measurement. Science, 103(2684), 677–
680.
23. Suits, D. B. (1957). Use of Dummy Variables in Regression Equations. Journal of the
American Statistical Association, 52(280), 548–551.
24. Troyanskaya, O., Cantor, M., Sherlock, G., Brown, P., Hastie, T., Tibshirani, R., Botstein,
D., & Altman, R. B. (2001). Missing value estimation methods for DNA microarrays.
Bioinformatics, 17(6), 520–525.
25. Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley.
26. van Buuren, S., & Groothuis-Oudshoorn, K. (2011). mice: Multivariate Imputation by
Chained Equations in R. Journal of Statistical Software, 45(3), 1–67.
27. Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a Standard Process Model for Data
Mining. Proceedings of the 4th International Conference on the Practical Applications of
Knowledge Discovery and Data Mining.

Chương 6:
Hồi quy tuyến tính
(Linear Regression)
Hồi quy tuyến tính là một trong những thuật toán học có giám sát (Supervised Learning) cơ bản
và phổbiến nhất trong Machine Learning, dùng đểdựđoán giá trịđầu ra liên tục.
6.1

Mô hình Hồi quy tuyến tính đơn biến
Định nghĩa 6.1 (Hồi quy tuyến tính đơn biến). Cho tập dữliệu (x1, y1), (x2, y2), . . . , (xn, yn).
Mô hình biểu diễn mối quan hệgiữa biến độc lập x và biến phụthuộc y theo dạng tuyến tính:
y = w0 + w1x + ϵ
(6.1)
trong đó w0 là hệsốchặn (intercept), w1 là hệsốgóc (slope), và ϵ là sai sốngẫu nhiên.
6.2
Hàm mất mát (Loss Function)
Đểtìm các hệsốw0, w1 tối ưu, người ta sửdụng sai sốbình phương trung bình (Mean Squared
Error - MSE):
J(w0, w1) = 1
2n
n
X
i=1
(yi −(w0 + w1xi))2
(6.2)
Mục tiêu của bài toán là tìm (w0, w1) sao cho J(w0, w1) đạt giá trịnhỏnhất.
6.3
Cài đặt Hồi quy tuyến tính với Scikit-Learn
Dưới đây là đoạn code Python minh họa việc xây dựng mô hình Linear Regression trên tập dữ
liệu thực tế:
Listing 6.1: Thực thi Linear Regression bằng Scikit-Learn
1
import numpy as np
2
from sklearn.linear_model import LinearRegression
3
4
# 1. Tao du lieu gia dinh
5
X = np.array([[1], [2], [3], [4], [5]])
6
y = np.array([2.1, 3.9, 6.1, 8.2, 9.9])
7
52

CHƯƠNG 6. HỒI QUY TUYẾN TÍNH
(LINEAR REGRESSION)
53
8
# 2. Khoi tao va huan luyen mo hinh
9
model = LinearRegression()

10
model.fit(X, y)
11
12
# 3. In ket qua trong so w0 va w1
13
print("He so w1 (slope):", model.coef_[0])
14
print("He so w0 (intercept):", model.intercept_)
15
16
# 4. Du doan gia tri moi
17
y_pred = model.predict([[6]])
18
print("Du doan cho X=6:", y_pred[0])
6.4
Tóm tắt chương
• Bản chất mô hình Hồi quy tuyến tính và bài toán tối ưu hàm MSE.
• Phương pháp hạđộdốc (Gradient Descent) đểcập nhật trọng số.
• Thao tác huấn luyện mô hình bằng thư viện scikit-learn.

Chương 7:
Phân lớp
(Classification)
Phân lớp (classification) là bài toán học có giám sát trong đó đầu ra là một nhãn rời rạc: thư
rác hay không, khối u lành hay ác tính, khách hàng có rời bỏdịch vụhay không, chữsốviết
tay là 0 hay 9… Nếu chỉcó hai nhãn ta có phân lớp nhịphân; nhiều hơn hai nhãn là phân lớp
đa lớp. Theo kếhoạch giảng dạy, chương này trình bày các thuật toán nền tảng: KNN, Naive
Bayes, Logistic Regression, Decision Tree, SVM; các phương pháp kết hợp (Random Forest,
AdaBoost, XGBoost) được trình bày ởchương kếtiếp.
Sau khi học xong chương này, người học có khảnăng:
• Trình bày ý tưởng, lịch sửvà giảđịnh của năm họthuật toán phân lớp kinh điển.
• Tựtính tay một bước dựđoán của KNN (bỏphiếu đều, có trọng số, và KNN cho hồi quy),
Naive Bayes, Logistic Regression và một lần chia nút của cây quyết định.
• Cài đặt và so sánh các thuật toán bằng scikit-learn trên dữliệu thực.
• Lựa chọn thuật toán và bước tiền xửlý phù hợp cho từng loại dữliệu.
7.1
Bài toán phân lớp
Định nghĩa 7.1 (Bài toán phân lớp). Cho tập huấn luyện {(xi, yi)}n
i=1 với xi ∈Rd và yi ∈
{1, . . . , K}. Cần học hàm f : Rd →{1, . . . , K} sao cho f(x) dựđoán đúng nhãn của các điểm
chưa từng thấy. Nhiều thuật toán còn ước lượng xác suất P(y = k | x) và chọn nhãn có xác
suất lớn nhất.

Vềmặt hình học, bộphân lớp chia không gian đặc trưng thành các vùng; ranh giới giữa các
vùng gọi là biên quyết định (decision boundary). Các thuật toán khác nhau tạo ra biên có hình
dạng khác nhau: tuyến tính (Logistic Regression, SVM tuyến tính), các đoạn song song trục
(Decision Tree), hay biên phức tạp tùy dữliệu (KNN, SVM với nhân).
54

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
55
[Chỗchèn hình]
images/ch-classify-boundaries.png
Hình 7.1: Biên quyết định của KNN, Logistic Regression, Decision Tree và SVM (nhân RBF)
trên cùng một tập dữliệu hai chiều.
Xuyên suốt chương, ta minh họa bằng bộdữliệu Iris do Ronald Fisher công bốnăm 1936:
150 bông hoa thuộc 3 loài (setosa, versicolor, virginica), mỗi bông có 4 đặc trưng: chiều dài,
chiều rộng của đài hoa và cánh hoa (cm).
Listing 7.1: Chuẩn bịdữliệu Iris
1
from sklearn.datasets import load_iris
2
from sklearn.model_selection import train_test_split
3
4
iris = load_iris()
5
X, y = iris.data, iris.target
6
print(X.shape, iris.target_names)
# (150, 4) ['setosa' 'versicolor'
'virginica']
7
8
# stratify=y: giu nguyen ti le cac lop trong tap train va test
9
X_train , X_test , y_train , y_test = train_test_split(
10
X, y, test_size=0.3, random_state=42, stratify=y)
7.2
K láng giềng gần nhất (KNN)
KNN (K-Nearest Neighbors) được Evelyn Fix và Joseph Hodges đềxuất năm 1951 trong một
báo cáo cho Không quân Hoa Kỳ; năm 1967, Cover và Hart chứng minh rằng khi sốmẫu tiến
ra vô cùng, sai sốcủa luật 1-NN không vượt quá hai lần sai sốBayes tối ưu. KNN là thuật toán
lười (lazy learning): không học tham sốnào, chỉghi nhớdữliệu và trì hoãn mọi tính toán đến
lúc dựđoán.

Định nghĩa 7.2 (Thuật toán KNN). Đểphân lớp điểm mới q:
1. Tính khoảng cách từq đến mọi điểm huấn luyện, thường dùng khoảng cách Euclid d(q, x) =
qP
j(qj −xj)2.
2. Chọn K điểm gần nhất.
3. Gán nhãn chiếm đa sốtrong K điểm đó (có thểbỏphiếu có trọng số1/d).

CHƯƠNG 7. PHÂN LỚP
(CLASSIFICATION)
56
Ví dụ7.1 (Tính tay KNN phân lớp). Cho 5 mẫu huấn luyện có hai đặc trưng x1, x2 và nhãn
y ∈{0, 1} (Bảng 7.1). Dựđoán nhãn của mẫu mới q = (2, 4) với khoảng cách Euclid d =
p
(x1 −2)2 + (x2 −4)2.
STT
x1
x2
y
Khoảng cách đến q = (2, 4)
Thứhạng
1
7
6
0
√
52 + 22 =
√
29 ≈5,385
4
2
2
4
1
√
02 + 02 = 0
1
3
1
5
1
√
12 + 12 =
√
2 ≈1,414

2
4
3
9
1
√
12 + 52 =
√
26 ≈5,099
3
5
8
7
0
√
62 + 32 =
√
45 ≈6,708
5
Bảng 7.1: Dữliệu huấn luyện và khoảng cách đến điểm cần dựđoán
Với K = 3: ba mẫu gần nhất là 2, 3, 4, đều có nhãn 1 ⇒ˆy = 1. Với K = 4: thêm mẫu 1
(nhãn 0), kết quảbỏphiếu 3 : 1, vẫn dựđoán ˆy = 1.
7.2.1
KNN có trọng số
Bỏphiếu đều coi láng giềng gần nhất và láng giềng thứK như nhau, dù một điểm có thểrất
gần còn điểm kia khá xa. Dudani (1976) đềxuất bỏphiếu có trọng số: láng giềng càng gần, lá
phiếu càng nặng. Trọng sốphổbiến nhất là nghịch đảo khoảng cách:
wi =
1
d(q, xi) + ε,
ˆy = arg max
c
X
i∈NK(q), yi=c
wi,
(7.1)
trong đó ε là một sốrất nhỏ(ví dụ10−5) đểtránh chia cho 0 khi q trùng với một điểm huấn
luyện.
Ví dụ7.2 (Trọng sốkhi điểm cần dựđoán trùng một mẫu). Tiếp ví dụtrên với K = 4 và
ε = 10−5:
w2 =
1
0 + 10−5 = 100 000,
w3 =
1

1,414 ≈0,707,
w4 =
1
5,099 ≈0,196,
w1 =
1
5,385 ≈0,186.
Tổng trọng sốcủa lớp 1 là 100 000+0,707+0,196 ≈100 000,9, của lớp 0 là 0,186. Chuẩn hóa
vềtỉlệ: lớp 0 chiếm
0,186
100 001,09 ≈1,86 × 10−6 ≈0, lớp 1 chiếm ≈1. Mẫu trùng khớp gần như
quyết định toàn bộkết quả. Chú ý
1
0+10−5 = 105 chứkhông phải 1 — một nhầm lẫn hay gặp khi
tính tay. Trong scikit-learn, nếu có láng giềng cách đúng 0 thì weights="distance" chỉtính
các láng giềng đó.
Ví dụ7.3 (Trọng sốphá thếhòa phiếu). Cũng với dữliệu ởBảng 7.1, xét q = (5, 6) và K = 4.
Khoảng cách đến các mẫu 1, 5, 2, 4 lần lượt là 2;
√
10 ≈3,162;
√
13 ≈3,606;
√
13 ≈3,606
(mẫu 3 xa nhất,
√
17 ≈4,123). Bỏphiếu đều cho kết quảhòa 2 : 2: mẫu 1, 5 nhãn 0; mẫu 2, 4
nhãn 1. Với trọng số1/d:
W0 = 1
2 +
1
3,162 ≈0,816,
W1 =
1
3,606 +
1
3,606 ≈0,555 ⇒ˆy = 0.
Khi hòa phiếu, scikit-learn với weights="uniform" chọn lớp có nhãn nhỏhơn — một quy ước
tùy ý; trọng sốkhoảng cách cho lời giải có cơ sởhơn. Đây là lý do khi K chẵn (dễhòa phiếu)
nên dùng KNN có trọng số.
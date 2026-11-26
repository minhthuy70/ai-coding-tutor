<!-- page: 1 -->
# VI_PY_071: Nền tảng Python cho khoa học dữ liệu và học máy căn bản

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân  
**Chuyên mục**: Học máy | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 2 -->
Mục lục
1
Giới thiệu vềPython
1
1.1
Python là gì?
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Lịch sửphát triển của Python . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2.1
Khởi nguồn & Phiên bản thửnghiệm (1989 – 1991)
. . . . . . . . . .
1
1.2.2
Python 1.0 & Chuẩn hóa quản trị(1994 – 1999) . . . . . . . . . . . . .
1
1.2.3
Python 2.0 & Sựtrỗi dậy của Cộng đồng (Tháng 10/2000) . . . . . . .
2
1.2.4
Python 3.0 – ”Cuộc đại tái thiết” (Tháng 12/2008)
. . . . . . . . . . .
2
1.2.5
Kỷnguyên AI/Machine Learning & Khai tửPython 2 (2015 – Nay) . .
2
1.3
Guido van Rossum – tác giảcủa Python . . . . . . . . . . . . . . . . . . . . .
2
1.4
Tên gọi Python . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2

<!-- page: 2 -->

1.5
Hướng dẫn cài đặt Python và Anaconda . . . . . . . . . . . . . . . . . . . . .
2
1.5.1
Cài đặt Python
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.5.2
Cài đặt Anaconda/Miniconda
. . . . . . . . . . . . . . . . . . . . . .
3
1.5.3
Tạo môi trường Conda . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.6
Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2
Cú pháp Python cơ bản
5
2.1
Biến và Kiểu dữliệu
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.1.1
Các kiểu dữliệu cơ bản . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.2
Toán tửtrong Python . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2.1
Toán tửcơ bản . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2.2
Toán tửgán mởrộng . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.3
Hàm toán học trong Python . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.3.1
Các hằng sốtoán học . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.3.2
Các hàm toán học thường dùng
. . . . . . . . . . . . . . . . . . . . .

<!-- page: 3 -->

7
2.4
Cấu trúc dữliệu nâng cao . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.4.1
List (Danh sách)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.5
Cấu trúc điều khiển và Vòng lặp . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.5.1
Câu lệnh điều kiện if-else
. . . . . . . . . . . . . . . . . . . . . . . .
7
2.6
Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
3
Lập trình hướng đối tượng trong Python
9
3.1
Lớp và Đối tượng (Class and Object) . . . . . . . . . . . . . . . . . . . . . . .
9
3.2
Các phương thức đặc biệt (Magic Methods) . . . . . . . . . . . . . . . . . . .
9
3.2.1
Phương thức __init__ và __call__ . . . . . . . . . . . . . . . . . .
9
3.3
Tính Kếthừa (Inheritance) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3.4
Quản lý thuộc tính: Siêu tham số(Hyperparameters) và Tham sốhọc được
(Learned Parameters) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
i

<!-- page: 3 -->
MỤC LỤC
ii
3.5
Thiết kếCustom Estimator chuẩn Scikit-Learn . . . . . . . . . . . . . . . . . .
11

<!-- page: 4 -->

3.6
Mẫu thiết kếPipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.7
Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
4
XửLý DữLiệu Với NumPy Và Pandas
(NumPy & Pandas)
13
4.1
Thư viện NumPy - Tính toán Khoa học
. . . . . . . . . . . . . . . . . . . . .
13
4.1.1
Khởi tạo mảng và kiểm tra thuộc tính . . . . . . . . . . . . . . . . . .
13
4.1.2
Thao tác trên mảng: Thêm phần tử, xóa, sửa . . . . . . . . . . . . . . .
14
4.1.3
Slicing và Boolean Indexing (Lọc dữliệu) . . . . . . . . . . . . . . . .
14
4.1.4
Đại sốtuyến tính (Linear Algebra) . . . . . . . . . . . . . . . . . . . .
15
4.2
Thư viện Pandas - Xửlý và Phân tích Dữliệu . . . . . . . . . . . . . . . . . .
15
4.2.1
Tạo và Đọc dữliệu . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
4.2.2
Truy xuất & Điều kiện lọc dữliệu . . . . . . . . . . . . . . . . . . . .
16
4.2.3
Xửlý dữliệu khuyết & Thống kê mô tả. . . . . . . . . . . . . . . . .
16
4.2.4
Thay thếvà Áp dụng hàm
. . . . . . . . . . . . . . . . . . . . . . . .
17
4.2.5
Gom nhóm (GroupBy) & Gộp dữliệu (Concat/Merge) . . . . . . . . .
17

<!-- page: 5 -->

5
Tiền xửlý dữliệu
(Data Preprocessing)
18
5.1
Khởi nguồn và vai trò của tiền xửlý dữliệu . . . . . . . . . . . . . . . . . . .
19
5.1.1
“Rác vào, rác ra” . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
5.1.2
Tiền xửlý trong quy trình khai phá tri thức (KDD) . . . . . . . . . . .
19
5.1.3
Phân loại các tác vụtiền xửlý . . . . . . . . . . . . . . . . . . . . . .
20
5.1.4
Thư viện scikit-learn và giao diện fit / transform . . . . . . . . . . .
20
5.2
Các kiểu dữliệu và lựa chọn phép biến đổi . . . . . . . . . . . . . . . . . . . .
21
5.3
Xửlý dữliệu thiếu (Missing Values) . . . . . . . . . . . . . . . . . . . . . . .
21
5.3.1
Cơ chếsinh dữliệu thiếu . . . . . . . . . . . . . . . . . . . . . . . . .
22
5.3.2
Simple Imputer: trung bình, trung vị, giá trịphổbiến . . . . . . . . . .
22
5.3.3
KNN Imputer và khoảng cách nan-Euclid . . . . . . . . . . . . . . . .
23
5.3.4
Iterative Imputer . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
5.4
Phát hiện ngoại lai (Outlier Detection) . . . . . . . . . . . . . . . . . . . . . .
28
5.4.1
Phương pháp một biến: z-score và quy tắc IQR . . . . . . . . . . . . .
28
5.4.2
Phương pháp nhiều biến: Local Outlier Factor (LOF) . . . . . . . . . .

<!-- page: 6 -->

29
5.5
Mã hóa dữliệu phân loại . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
5.5.1
Label Encoder
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
5.5.2
One Hot Encoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
5.6
Vector hóa văn bản . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
5.6.1
Mô hình túi từvà Count Vectorizer
. . . . . . . . . . . . . . . . . . .
35
5.6.2
TF-IDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
5.7
Chuẩn hóa thang đo đặc trưng (Feature Scaling) . . . . . . . . . . . . . . . . .
40
5.7.1
Vì sao cần chuẩn hóa thang đo? . . . . . . . . . . . . . . . . . . . . .
40
5.7.2
Min Max Scaler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
5.7.3
Max Abs Scaler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
5.7.4
Standard Scaler (chuẩn hóa z-score) . . . . . . . . . . . . . . . . . . .
41
5.7.5
Robust Scaler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
5.7.6
Ví dụso sánh bốn bộchuẩn hóa . . . . . . . . . . . . . . . . . . . . .
41
5.8
Dữliệu mất cân bằng và SMOTE . . . . . . . . . . . . . . . . . . . . . . . . .
42

<!-- page: 7 -->


<!-- page: 4 -->
MỤC LỤC
iii
5.9
Kết hợp các bước: Pipeline và ColumnTransformer . . . . . . . . . . . . . . .
44
5.10 Nghiên cứu tình huống: bộdữliệu Ames Housing . . . . . . . . . . . . . . . .
45
5.10.1 Giới thiệu bộdữliệu . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
5.10.2 Những “cái bẫy” khi đọc dữliệu . . . . . . . . . . . . . . . . . . . . .
46
5.10.3 Đọc và khảo sát dữliệu . . . . . . . . . . . . . . . . . . . . . . . . . .
46
5.10.4 Xây dựng quy trình tiền xửlý hoàn chỉnh . . . . . . . . . . . . . . . .
47
5.11 Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
5.12 Bài tập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
Tài liệu tham khảo của chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
6
Hồi quy tuyến tính
(Linear Regression)
52
6.1
Mô hình Hồi quy tuyến tính đơn biến . . . . . . . . . . . . . . . . . . . . . . .
52
6.2
Hàm mất mát (Loss Function)
. . . . . . . . . . . . . . . . . . . . . . . . . .
52
6.3
Cài đặt Hồi quy tuyến tính với Scikit-Learn . . . . . . . . . . . . . . . . . . .
52
6.4
Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
7
Phân lớp
(Classification)
54
7.1

<!-- page: 8 -->

Bài toán phân lớp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
7.2
K láng giềng gần nhất (KNN) . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
7.2.1
KNN có trọng số. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
7.2.2
KNN cho bài toán hồi quy . . . . . . . . . . . . . . . . . . . . . . . .
57
7.3
Naive Bayes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
58
7.4
Hồi quy logistic (Logistic Regression) . . . . . . . . . . . . . . . . . . . . . .
59
7.5
Cây quyết định (Decision Tree) . . . . . . . . . . . . . . . . . . . . . . . . . .
60
7.5.1
Độđo độhỗn tạp . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
7.6
Máy vector hỗtrợ(SVM) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.6.1
Lềcực đại . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.6.2
Lềmềm và tham sốC
. . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.6.3
Thủthuật nhân . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.7
So sánh các thuật toán . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
7.8
Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
64
7.9
Bài tập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
64

<!-- page: 9 -->

Tài liệu tham khảo của chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
8
Học kết hợp
(Ensemble Learning)
66
8.1
Trí tuệđám đông
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
8.1.1
Độchệch và phương sai
. . . . . . . . . . . . . . . . . . . . . . . . .
67
8.2
Bagging và Random Forest . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
8.2.1
Bagging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
8.2.2
Random Forest . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
8.3
AdaBoost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
69
8.4
Gradient Boosting và XGBoost . . . . . . . . . . . . . . . . . . . . . . . . . .
70
8.4.1
Gradient Boosting
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
8.4.2
XGBoost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
8.5
Voting và Stacking
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
8.6
Tổng kết so sánh
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73


<!-- page: 10 -->

<!-- page: 5 -->
MỤC LỤC
iv
8.7
Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73
8.8
Bài tập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73
Tài liệu tham khảo của chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
9
Phân cụm
(Clustering)
75
9.1
Bài toán phân cụm
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
75
9.2
K-Means
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
76
9.2.1
Chọn sốcụm K . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
9.3
Phân cụm phân cấp (Hierarchical Clustering)
. . . . . . . . . . . . . . . . . .
78
9.4
DBSCAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
9.5
Mean-shift . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
9.6
So sánh và ứng dụng
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
82
9.7
Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
9.8
Bài tập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- page: 11 -->

83
Tài liệu tham khảo của chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
84
10 Giảm chiều dữliệu
(Dimensionality Reduction)
85
10.1 Lời nguyền sốchiều . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
85
10.2 Kiến thức nền: phương sai, hiệp phương sai và trịriêng . . . . . . . . . . . . .
86
10.2.1 Phương sai . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
86
10.2.2 Hiệp phương sai và hệsốtương quan
. . . . . . . . . . . . . . . . . .
86
10.2.3 Trịriêng và vector riêng . . . . . . . . . . . . . . . . . . . . . . . . .
87
10.3 Phân tích giá trịsuy biến (SVD)
. . . . . . . . . . . . . . . . . . . . . . . . .
88
10.3.1 Lịch sử. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
88
10.3.2 Tính SVD thông qua X⊤X . . . . . . . . . . . . . . . . . . . . . . . .
89
10.3.3 Ứng dụng: nén ảnh và TruncatedSVD . . . . . . . . . . . . . . . . . .
90
10.4 Phân tích thành phần chính (PCA) . . . . . . . . . . . . . . . . . . . . . . . .
91
10.4.1 Lịch sửvà ý tưởng . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91
10.4.2 Chọn sốthành phần . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
10.4.3 PCA trong pipeline học máy . . . . . . . . . . . . . . . . . . . . . . .
95
10.5 Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
96
10.6 Bài tập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
96
Tài liệu tham khảo của chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
97
11 Đánh giá và lựa chọn mô hình
(Validation)
98
11.1 Lỗi tổng quát hóa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
98

<!-- page: 12 -->

11.2 Chiến lược chia dữliệu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
99
11.2.1 Hold-out: train / validation / test . . . . . . . . . . . . . . . . . . . . .
99
11.2.2 Kiểm định chéo k-fold . . . . . . . . . . . . . . . . . . . . . . . . . . 100
11.3 Độđo cho bài toán phân lớp
. . . . . . . . . . . . . . . . . . . . . . . . . . . 101
11.3.1 Ma trận nhầm lẫn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
11.3.2 Đường ROC và AUC . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
11.4 Độđo cho bài toán hồi quy . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
11.5 Tìm siêu tham số. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
11.5.1 Đường cong học và đường cong kiểm định
. . . . . . . . . . . . . . . 105
11.6 Những sai lầm thường gặp . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

<!-- page: 6 -->
MỤC LỤC
v
11.7 Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
11.8 Bài tập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Tài liệu tham khảo của chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
12 Mạng nơ-ron nhân tạo
(Neural Network)
108
12.1 Lịch sửphát triển . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
12.2 Perceptron . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
12.3 Mạng nơ-ron nhiều lớp (MLP) . . . . . . . . . . . . . . . . . . . . . . . . . . 111
12.3.1 Kiến trúc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
12.3.2 Hàm kích hoạt
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
12.3.3 Hàm mất mát và lớp đầu ra . . . . . . . . . . . . . . . . . . . . . . . . 112
12.4 Lan truyền ngược (Backpropagation) . . . . . . . . . . . . . . . . . . . . . . . 112
12.5 Huấn luyện mạng nơ-ron trong thực tế. . . . . . . . . . . . . . . . . . . . . . 114
12.5.1 Bộtối ưu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
12.5.2 Khởi tạo và chuẩn hóa . . . . . . . . . . . . . . . . . . . . . . . . . . 114
12.5.3 Chống quá khớp
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
12.6 MLP với scikit-learn
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
12.7 Giới thiệu thư viện học sâu . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
12.8 Tóm tắt chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
12.9 Bài tập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
Tài liệu tham khảo của chương . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

<!-- page: 7 -->

<!-- page: 13 -->

Chương 1:
Giới thiệu vềPython
1.1
Python là gì?
Python là một ngôn ngữlập trình được sửdụng rộng rãi trong các ứng dụng web, phát triển
phần mềm, khoa học dữliệu và máy học (ML). Các nhà phát triển sửdụng Python vì nó hiệu
quả, dễhọc và có thểchạy trên nhiều nền tảng khác nhau. Phần mềm Python được tải xuống
miễn phí, tích hợp tốt với tất cảcác loại hệthống và tăng tốc độphát triển. (Nguồn: https:
//aws.amazon.com/vi/what-is/python/)
Python hỗtrợnhiều mô hình lập trình, trong đó có lập trình thủtục, lập trình hướng đối
tượng và lập trình hàm.
Một chương trình Python đơn giản:
1
print("Hello, Python!")
Cú pháp của Python có xu hướng sửdụng khoảng trắng đểthểhiện cấu trúc của chương
trình. Ví dụ:
1
if age >= 18:
2
print("Adult")
3
else:
4
print("Under 18")
Cách tổchức này giúp mã nguồn Python có cấu trúc rõ ràng và dễđọc.
1.2
Lịch sửphát triển của Python
1.2.1
Khởi nguồn & Phiên bản thửnghiệm (1989 – 1991)
Vào cuối năm 1989, khi đang làm việc tại Viện Nghiên cứu Quốc gia vềToán học và Khoa học
Máy tính (CWI) ởHà Lan, Guido van Rossum quyết định viết một ngôn ngữlập trình mới trong
kỳnghỉGiáng sinh đểlàm dựán phụ. Ông muốn tạo ra một ngôn ngữkết hợp tính đơn giản của
ngôn ngữABC với khảnăng tương tác tốt với hệđiều hành Amoeba.
Tháng 2/1991, Guido đăng tải mã nguồn lên nhóm tin alt.sources với phiên bản Python 0.9.0.
Dù chỉlà bản phôi thai, nó đã có những nền móng rất hiện đại: Mô hình OOP, Hệthống xửlý
ngoại lệ, Các kiểu dữliệu cốt lõi (list, dict, str) và Hệthống module.
1.2.2
Python 1.0 & Chuẩn hóa quản trị(1994 – 1999)
Tháng 1/1994, Python 1.0 chính thức ra mắt, tích hợp mạnh mẽcác công cụcủa Lập trình chức
năng (Functional Programming) như lambda, map, filter và reduce.
1

<!-- page: 8 -->
CHƯƠNG 1. GIỚI THIỆU VỀPYTHON
2

<!-- page: 14 -->

Năm 1995 (Python 1.2), Guido tiếp tục phát triển Python tại Tập đoàn Sáng kiến Nghiên cứu
Quốc gia (CNRI) ởMỹ, bổsung khảnăng truyền tham sốtheo tên (Keyword arguments). Trong
giai đoạn này, Guido được cộng đồng trao danh hiệu BDFL (Benevolent Dictator for Life).
1.2.3
Python 2.0 & Sựtrỗi dậy của Cộng đồng (Tháng 10/2000)
Python 2.0 đánh dấu sựchuyển dịch lớn sang mô hình phát triển mã nguồn mởhoàn toàn. Các
tính năng đột phá bao gồm: List Comprehension, Garbage Collector (GC), và ra đời quy trình
PEP (Python Enhancement Proposal). Phiên bản Python 2.7 (2010) trởthành phiên bản ổn định
nhất của dòng Python 2.
1.2.4
Python 3.0 – ”Cuộc đại tái thiết” (Tháng 12/2008)
Sau nhiều năm phát triển, Python 2 bịtích tụnhiều lỗi thiết kế. Guido quyết định phát hành
Python 3.0 với đặc điểm cốt lõi là Không tương thích ngược (Backwards Incompatible) với
Python 2. Những cải tiến quan trọng bao gồm:
• Đồng bộUnicode cho mọi chuỗi ký tự.
• Thay đổi câu lệnh print thành hàm print().
• Tối ưu hóa bộnhớbằng cách chuyển các hàm như range(), zip(), map() sang dạng trả
vềIterator.
1.2.5
Kỷnguyên AI/Machine Learning & Khai tửPython 2 (2015 – Nay)
Cú pháp đơn giản giúp Python trởthành lựa chọn hàng đầu trong Khoa học dữliệu và AI với
các thư viện như NumPy, Pandas, Scikit-Learn, TensorFlow, PyTorch.
Ngày 01/01/2020, Python 2 chính thức bịkhai tử(EOL), đưa Python 3 trởthành tiêu chuẩn
duy nhất. Giai đoạn hiện tại (Python 3.8 – 3.13+) tập trung vào bổsung các toán tửmới và dự
án Faster CPython nhằm tối ưu hóa hiệu năng.
1.3
Guido van Rossum – tác giảcủa Python
Guido van Rossum là một nhà khoa học máy tính người Hà Lan. Ông là người giữquyền quyết
định tối cao vềđịnh hướng kiến trúc của ngôn ngữ(BDFL) cho đến khi từchức vào năm 2018.
1.4
Tên gọi Python
Tên gọi ”Python” không xuất phát từloài trăn, mà lấy cảm hứng từchương trình hài kịch yêu
thích của ông trên đài BBC: ”Monty Python’s Flying Circus”.
1.5
Hướng dẫn cài đặt Python và Anaconda
1.5.1
Cài đặt Python
1. Truy cập trang chủPython: https://www.python.org/downloads/

<!-- page: 9 -->
CHƯƠNG 1. GIỚI THIỆU VỀPYTHON
3
Hình 1.1: Guido van Rossum - Tác giảsáng lập Python. (Nguồn: Sauria Associates, LLC /
FlickrVision)
2. Tải phiên bản cài đặt (Ví dụ: Python 3.14.7 cho Windows).

<!-- page: 15 -->

3. Mởfile cài đặt. Lưu ý quan trọng: Nhớtick vào ô ”Add python.exe to PATH” trước khi
bấm ”Install Now”.
4. Bấm ”Close” khi cài đặt thành công. Có thểchọn ”Disable path length limit” nếu cần.
Hình 1.2: Tick chọn Add python.exe to PATH trong quá trình cài đặt
1.5.2
Cài đặt Anaconda/Miniconda
Anaconda là một nền tảng phân phối Python và R phục vụcho khoa học dữliệu.
1. Truy cập trang tải Anaconda: https://www.anaconda.com/download
2. Tải bản cài đặt Anaconda Distribution hoặc Miniconda.
3. Mởfile cài đặt, chọn ”Just Me”, chọn đường dẫn lưu (ví dụ: C:\miniconda3).

<!-- page: 10 -->
CHƯƠNG 1. GIỚI THIỆU VỀPYTHON
4
4. Trong phần Advanced Installation Options, có thểtick chọn ”Register Miniconda3 as my
default Python”.
5. Nhấn ”Install” và đợi quá trình cài đặt hoàn tất.
1.5.3
Tạo môi trường Conda
Sau khi cài đặt Anaconda/Miniconda, mởAnaconda Prompt và sửdụng lệnh sau đểtạo một môi
trường ảo (ví dụtên là ai) với phiên bản Python 3.14:
1
conda create -n ai python=3.14 anaconda
Xác nhận tiến trình cài đặt các gói bằng cách gõ y (yes) khi được yêu cầu.
1.6
Tóm tắt chương
Trong chương này, chúng ta đã tìm hiểu:
• Khái niệm cơ bản vềPython và ứng dụng của nó.
• Lịch sửhình thành chi tiết qua từng giai đoạn (từPython 0.9.0 đến Python 3.x).
• Tiểu sửcủa tác giảGuido van Rossum và nguồn gốc tên gọi thú vịcủa Python.
• Các bước cài đặt môi trường lập trình cơ bản với Python và Anaconda.

<!-- page: 11 -->
Chương 2:
Cú pháp Python cơ bản
Chương này trình bày các khái niệm nền tảng trong lập trình Python, bao gồm biến, kiểu dữliệu,
toán tử, cấu trúc điều khiển và các hàm toán học. Đây là các kiến thức bắt buộc trước khi đi vào
xửlý dữliệu và Machine Learning.
2.1
Biến và Kiểu dữliệu
Trong Python, biến được khởi tạo tựđộng khi gán giá trị. Python là ngôn ngữdynamically typed
(định kiểu động).
Định nghĩa 2.1 (Biến trong Python). Biến là tên gọi đại diện cho một vùng nhớchứa dữliệu.
Giá trịcủa biến có thểthay đổi trong quá trình thực thi chương trình.
2.1.1

<!-- page: 16 -->

Các kiểu dữliệu cơ bản
Dựa trên nền tảng Python Basic, dưới đây là bảng tổng hợp các kiểu dữliệu cốt lõi thường xuyên
được sửdụng:
Tên
Kiểu dữliệu
Ví dụ
str
Kiểu chuỗi (string)
a = 'Thien Thanh'
int
Kiểu sốnguyên
a = 79
float
Kiểu sốthực
a = 7.6
NoneType
Kiểu None
a = None
bool
Kiểu luận lý (True, False)
a = True
list
Kiểu danh sách
a = [3, 2, 1, 5]
tuple
Kiểu bộ
a = (1, 5, 3)
dict
Kiểu từđiển
b = {'one': 1, 'four': 4}
set
Kiểu tập hợp
a = {1, 3, 5}
Bảng 2.1: Các kiểu dữliệu cơ bản trong Python
Đểkiểm tra kiểu dữliệu của một biến trong Python, ta sửdụng hàm type():
Listing 2.1: Kiểm tra kiểu dữliệu
1
a = 7
2
print(type(a))
# Output: <class 'int'>
5

<!-- page: 12 -->
CHƯƠNG 2. CÚ PHÁP PYTHON CƠ BẢN

<!-- page: 17 -->

6
2.2
Toán tửtrong Python
Toán tửlà thành phần không thểthiếu đểthực hiện các phép tính từcơ bản đến phức tạp trong
các thuật toán.
2.2.1
Toán tửcơ bản
Tên toán tử
Ký hiệu
Ví dụ
Kết quả
Cộng
+
3 + 7
10
Trừ
-
7 - 2
5
Nhân
*
2 * 7
14
Chia
/
7 / 5
1.4
Chia lấy phần nguyên
//
10 // 4
2
Chia lấy phần dư
%
9 % 5
4
Lấy mũ
**
2 ** 3
8
Bảng 2.2: Các toán tửsốhọc cơ bản
2.2.2
Toán tửgán mởrộng
Đểmã nguồn ngắn gọn hơn, Python hỗtrợcác toán tửgán mởrộng kết hợp phép tính và phép
gán:
Tên toán tử

<!-- page: 18 -->

Ký hiệu
Ví dụ
Kết quả
Cộng
+=
a = 7; a += 3
10
Trừ
-=
b = 9; b -= 4
5
Nhân
*=
a = 2; a *= 7
14
Chia
/=
a = 7; b /= 5
1.4
Chia lấy phần nguyên
//=
a = 10; a //= 4
2
Chia lấy phần dư
%=
a = 9; a %= 5
4
Lấy mũ
**=
a = 2; a **= 3
8
Bảng 2.3: Các toán tửgán mởrộng
2.3
Hàm toán học trong Python
Đối với các ứng dụng khoa học dữliệu, thư viện math cung cấp các hằng sốvà hàm tính toán
nâng cao. Đểsửdụng, ta cần import thư viện:
Listing 2.2: Import thư viện math
1
import math
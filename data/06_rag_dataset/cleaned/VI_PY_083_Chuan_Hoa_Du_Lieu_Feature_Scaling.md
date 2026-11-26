# VI_PY_083: Kỹ thuật chuẩn hóa dữ liệu: Min-Max Scaling và Standard Z-Score

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân
**Chuyên mục**: Dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 11. ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH
(VALIDATION)
107
3. Chứng minh rằng R2 của mô hình luôn dựđoán ¯y bằng 0. Khi nào R2 < 0?
4. So sánh điểm accuracy của KNN (K = 5) trên tập Iris khi đánh giá bằng hold-out với 10
seed khác nhau và bằng 10-fold CV. Nhận xét vềđộbiến động.
5. Chứng minh bằng thực nghiệm hiện tượng rò rỉdữliệu: sinh dữliệu ngẫu nhiên X (100
mẫu, 10 000 cột) và nhãn ngẫu nhiên; chọn 20 cột tương quan cao nhất với y trên toàn bộ
dữliệu rồi mới kiểm định chéo. So sánh với việc đặt SelectKBest trong pipeline.
6. Trên Ames Housing, dùng GridSearchCV đểchọn alpha cho Ridge và Lasso (thang log),
báo cáo RMSE kiểm định chéo và RMSE trên tập test.
Tài liệu tham khảo của chương
1. Bergstra, J., & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization.
Journal of Machine Learning Research, 13, 281–305.
2. Cawley, G. C., & Talbot, N. L. C. (2010). On Over-fitting in Model Selection and Subsequent
Selection Bias in Performance Evaluation. Journal of Machine Learning Research, 11,
2079–2107.
3. Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8),
861–874.
4. Geisser, S. (1975). The Predictive Sample Reuse Method with Applications. Journal of
the American Statistical Association, 70(350), 320–328.
5. Geman, S., Bienenstock, E., & Doursat, R. (1992). Neural Networks and the Bias/Variance
Dilemma. Neural Computation, 4(1), 1–58.
6. Hanley, J. A., & McNeil, B. J. (1982). The meaning and use of the area under a receiver
operating characteristic (ROC) curve. Radiology, 143(1), 29–36.
7. Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning
(2nd ed.), Chapter 7. Springer.
8. Kohavi, R. (1995). A Study of Cross-Validation and Bootstrap for Accuracy Estimation
and Model Selection. Proceedings of IJCAI ’95, 1137–1143.
9. Saito, T., & Rehmsmeier, M. (2015). The Precision-Recall Plot Is More Informative than
the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets. PLoS ONE,
10(3), e0118432.
10. Stone, M. (1974). Cross-Validatory Choice and Assessment of Statistical Predictions.
Journal of the Royal Statistical Society: Series B, 36(2), 111–147.

Chương 12:
Mạng nơ-ron nhân tạo
(Neural Network)
Mạng nơ-ron nhân tạo là họmô hình đứng sau hầu hết thành tựu nổi bật của trí tuệnhân tạo hiện
đại: nhận dạng ảnh, dịch máy, nhận dạng giọng nói và các mô hình ngôn ngữlớn. Chương cuối
này trình bày nền tảng của mạng nơ-ron: từperceptron đơn lẻđến mạng nhiều lớp (Multilayer
Perceptron – MLP), thuật toán lan truyền ngược, các kỹthuật huấn luyện, và cách cài đặt bằng
scikit-learn cùng một thư viện học sâu.
Sau khi học xong chương này, người học có khảnăng:
• Trình bày lịch sửphát triển của mạng nơ-ron và lý do của các “mùa đông AI”.
• Tính tay đầu ra của perceptron và giải thích vì sao perceptron không học được XOR.
• Tính tay một bước lan truyền xuôi và lan truyền ngược trên mạng nhỏ.
• Huấn luyện MLPClassifier/MLPRegressor và một mạng Keras đơn giản, lựa chọn hàm
kích hoạt, hàm mất mát, bộtối ưu và kỹthuật điều chuẩn.
108

CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
109
12.1
Lịch sửphát triển
Năm
Sựkiện
1943
McCulloch và Pitts đềxuất mô hình toán học đầu tiên của nơ-ron sinh
học: nơ-ron ngưỡng với đầu vào nhịphân.
1949
Donald Hebb nêu quy tắc học “các nơ-ron cùng kích hoạt thì liên kết
mạnh lên”.
1958
Frank Rosenblatt công bốPerceptron — mô hình nơ-ron đầu tiên có
thuật toán học trọng sốtừdữliệu, cài đặt trên phần cứng Mark I.
1969
Minsky và Papert (sách Perceptrons) chứng minh perceptron một lớp
không biểu diễn được hàm XOR ⇒“mùa đông AI” thứnhất.
1986
Rumelhart, Hinton và Williams phổbiến thuật toán lan truyền ngược
(backpropagation) cho mạng nhiều lớp (ý tưởng đã có từLinnainmaa
1970, Werbos 1974).
1989
Cybenko, Hornik chứng minh định lý xấp xỉvạn năng. LeCun áp
dụng mạng tích chập (CNN) nhận dạng chữsốviết tay.

1997
Hochreiter và Schmidhuber đềxuất LSTM cho dữliệu chuỗi.
2006
Hinton và cộng sựhuấn luyện mạng sâu bằng tiền huấn luyện từng
lớp — khởi đầu thuật ngữ“deep learning”.
2012
AlexNet (Krizhevsky, Sutskever, Hinton) thắng ImageNet với cách
biệt lớn nhờGPU, ReLU, Dropout.
2017
Vaswani và cộng sựgiới thiệu kiến trúc Transformer (“Attention Is
All You Need”), nền tảng của các mô hình ngôn ngữlớn.
2018
Bengio, Hinton, LeCun nhận giải Turing cho những đóng góp vềhọc
sâu.
Bảng 12.1: Các mốc lịch sửcủa mạng nơ-ron
12.2
Perceptron
Định nghĩa 12.1 (Perceptron). Perceptron nhận vector đầu vào x ∈Rd, tính tổng có trọng số
rồi đưa qua hàm bước:
ˆy = step(w⊤x + b),
step(z) =
(
1
z ≥0
0
z < 0
(12.1)
Quy tắc học của Rosenblatt: với mỗi mẫu bịphân lớp sai, cập nhật
w ←w + η (y −ˆy) x,
b ←b + η (y −ˆy).
(12.2)
Định lý hội tụperceptron (Novikoff, 1962): nếu dữliệu tách được tuyến tính, thuật toán dừng
sau hữu hạn bước cập nhật.

CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
110
[Chỗchèn hình]
images/ch-nn-perceptron.png
Hình 12.1: Cấu trúc perceptron: đầu vào, trọng số, tổng có trọng số, hàm kích hoạt và đầu ra.
Ví dụ12.1 (Perceptron cho hàm AND). Chọn w = (1, 1), b = −1,5:
x1
x2
z = x1 + x2 −1,5

ˆy
AND
XOR
0
0
−1,5
0
0
0
0
1
−0,5
0
0
1
1
0
−0,5
0
0
1
1
1
0,5
1
1
0
Bảng 12.2: Perceptron biểu diễn hàm AND
Đường thẳng x1 + x2 = 1,5 tách điểm (1, 1) khỏi ba điểm còn lại. Nhưng với XOR, hai
điểm lớp 1 là (0, 1), (1, 0) nằm trên một đường chéo và hai điểm lớp 0 nằm trên đường chéo
kia: không đường thẳng nào tách được. Thật vậy, giảsửtồn tại w, b: từ(0, 0) 7→0 có b < 0;
từ(0, 1), (1, 0) 7→1 có w2 + b ≥0, w1 + b ≥0, cộng lại được w1 + w2 + b ≥−b > 0, mâu
thuẫn với (1, 1) 7→0. Lời giải: thêm một lớp ẩn — XOR = AND(OR, NAND).
Listing 12.1: Cài đặt perceptron từđầu
1
import numpy as np
2
3
class Perceptron:
4
def __init__(self, lr=1.0, epochs=10):
5
self.lr, self.epochs = lr, epochs
6
7

def fit(self, X, y):
8
self.w = np.zeros(X.shape[1]); self.b = 0.0
9
for _ in range(self.epochs):
10
errors = 0
11
for xi, yi in zip(X, y):
12
update = self.lr * (yi - self.predict(xi))
13
self.w += update * xi
14
self.b += update
15
errors += int(update != 0)
16
if errors == 0:
# hoi tu
17
break
18
return self
19

CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
111
20
def predict(self, X):
21
return (np.dot(X, self.w) + self.b >= 0).astype(int)
22
23
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
24
p_and = Perceptron().fit(X, np.array([0, 0, 0, 1]))
25
print(p_and.w, p_and.b, p_and.predict(X))
# hoc dung AND
26
p_xor = Perceptron(epochs=100).fit(X, np.array([0, 1, 1, 0]))
27

print(p_xor.predict(X))
# khong bao gio dung ca 4
12.3
Mạng nơ-ron nhiều lớp (MLP)
12.3.1
Kiến trúc
MLP gồm lớp đầu vào, một hoặc nhiều lớp ẩn và lớp đầu ra; mỗi nơ-ron nối với mọi nơ-ron
ởlớp kếtiếp (lớp kết nối đầy đủ– dense). Với lớp thứl:
z(l) = W(l)a(l−1) + b(l),
a(l) = g(l)z(l)
,
a(0) = x.
(12.3)
Hàm kích hoạt g phải phi tuyến: nếu không, nhiều lớp tuyến tính chồng lên nhau vẫn chỉlà một
phép biến đổi tuyến tính.
[Chỗchèn hình]
images/ch-nn-mlp.png
Hình 12.2: Mạng MLP với lớp đầu vào, hai lớp ẩn và lớp đầu ra.
Định lý 12.1 (Xấp xỉvạn năng – Cybenko 1989, Hornik 1991). Mạng một lớp ẩn với đủnhiều
nơ-ron và hàm kích hoạt phi tuyến (không phải đa thức) có thểxấp xỉmọi hàm liên tục trên tập
compact với độchính xác tùy ý.
Định lý chỉkhẳng định tồn tại, không nói cách tìm trọng sốhay cần bao nhiêu nơ-ron. Trong
thực tế, mạng sâu thường biểu diễn hiệu quảhơn mạng rộng một lớp.

CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
112
12.3.2
Hàm kích hoạt
Hàm
Công thức
Đạo hàm
Ghi chú
Sigmoid
σ(z) =
1
1+e−z
σ(1 −σ)
Đầu ra (0, 1); bão hòa ⇒
triệt tiêu gradient
Tanh
tanh z
1 −tanh2 z
Đầu ra (−1, 1), tâm 0

ReLU
max(0, z)
⊮[z > 0]
Mặc định cho lớp ẩn (Nair &
Hinton, 2010); nhanh
Leaky ReLU
max(0,01z, z)
1 hoặc 0,01
Tránh nơ-ron “chết”
Softmax
ezk
∑
j ezj
—
Lớp đầu ra phân lớp nhiều
lớp
Bảng 12.3: Các hàm kích hoạt phổbiến
[Chỗchèn hình]
images/ch-nn-activations.png
Hình 12.3: Đồthịcác hàm kích hoạt sigmoid, tanh, ReLU và Leaky ReLU.
12.3.3
Hàm mất mát và lớp đầu ra
Bài toán
Lớp đầu ra
Hàm mất mát
Hồi quy
1 nơ-ron, tuyến tính
MSE
Phân lớp nhịphân
1 nơ-ron, sigmoid
Binary cross-entropy
Phân lớp K lớp
K nơ-ron, softmax
Categorical cross-entropy −P
k yk log ˆyk
Bảng 12.4: Ghép cặp lớp đầu ra và hàm mất mát
12.4
Lan truyền ngược (Backpropagation)
Huấn luyện mạng là cực tiểu hàm mất mát L theo mọi trọng sốbằng gradient descent (Chương ??).
Lan truyền ngược là cách tính mọi đạo hàm riêng ∂L/∂w hiệu quảbằng quy tắc dây chuyền,
đi từlớp đầu ra vềlớp đầu vào và tái sửdụng kết quảtrung gian. Chi phí chỉcỡmột lần lan
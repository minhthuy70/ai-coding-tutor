<!-- page: 1 -->
# VI_PY_085: Trực quan hóa ma trận nhầm lẫn (Confusion Matrix) với Matplotlib

**Nguồn tài liệu chính thống**: Giáo trình Python cho ML - Ngô Hoàng Dũng, Lê Hoàng Ân  
**Chuyên mục**: Trực quan hóa | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 121 -->
CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
115
12.6
MLP với scikit-learn
Listing 12.3: MLPClassifier giải bài toán XOR
1
from sklearn.neural_network import MLPClassifier
2
3
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]); y = np.array([0, 1,
1, 0])
4
mlp = MLPClassifier(hidden_layer_sizes=(4,), activation="tanh",
5
solver="lbfgs", random_state=1, max_iter=1000)
6
mlp.fit(X, y)
7
print(mlp.predict(X))
# [0 1 1 0] -- mot lop an du de hoc XOR
Listing 12.4: Phân lớp chữsốviết tay với MLPClassifier
1
from sklearn.datasets import load_digits
2
from sklearn.model_selection import train_test_split , GridSearchCV
3
from sklearn.pipeline import make_pipeline
4
from sklearn.preprocessing import StandardScaler
5
from sklearn.metrics import classification_report
6
import matplotlib.pyplot as plt

<!-- page: 2 -->

7
8
X, y = load_digits(return_X_y=True)
9
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2,
10
stratify=y, random_state
=42)
11
pipe = make_pipeline(
12
StandardScaler(),
13
MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu",
14
solver="adam", alpha=1e-4, learning_rate_init=1e-3,
15
batch_size=64, max_iter=300, early_stopping=True,
16
random_state=42))
17
pipe.fit(X_tr, y_tr)
18
print(classification_report(y_te, pipe.predict(X_te), digits=4))
19
20
mlp = pipe[-1]
21
plt.plot(mlp.loss_curve_ , label="train loss")
22
plt.plot(mlp.validation_scores_ , label="validation accuracy")
23
plt.legend(); plt.xlabel("epoch"); plt.show()
24
25
# Tim sieu tham so (Chuong Validation)
26
grid = GridSearchCV(pipe, {"mlpclassifier__hidden_layer_sizes":
[(64,), (128, 64)],
27
"mlpclassifier__alpha": [1e-4, 1e-2, 1]},
cv=3, n_jobs=-1)
28
grid.fit(X_tr, y_tr); print(grid.best_params_ , grid.score(X_te, y_te)
)

<!-- page: 3 -->

Listing 12.5: MLPRegressor dựđoán giá nhà Ames
1
from sklearn.neural_network import MLPRegressor
2
from sklearn.compose import TransformedTargetRegressor

<!-- page: 122 -->
CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
116
3
4
# preprocess: ColumnTransformer da xay dung o Chuong Tien xu ly du
lieu
5
reg = make_pipeline(preprocess ,
6
MLPRegressor(hidden_layer_sizes=(64, 32), alpha=1
e-3,
7
early_stopping=True, max_iter=1000,
random_state=0))
8
model = TransformedTargetRegressor(regressor=reg, func=np.log1p,
inverse_func=np.expm1)
9
model.fit(X_train , y_train)
Giới hạn: MLPClassifier chỉchạy trên CPU và chỉhỗtrợlớp dense — phù hợp dữliệu dạng
bảng cỡvừa và mục đích học tập. Với ảnh, văn bản, âm thanh và mạng sâu, cần các thư viện
học sâu chuyên dụng.
12.7
Giới thiệu thư viện học sâu
TensorFlow/Keras (Google, 2015) và PyTorch (Meta, 2016) là hai thư viện phổbiến nhất.
Cảhai cung cấp tensor chạy trên GPU, tựđộng tính đạo hàm (automatic differentiation —
tổng quát hóa của lan truyền ngược) và các lớp dựng sẵn: Dense, Conv2D (CNN cho ảnh),
LSTM/GRU (dữliệu chuỗi), Attention/Transformer (văn bản).
Listing 12.6: Cùng bài toán digits với Keras
1
import keras
2
from keras import layers
3
4
scaler = StandardScaler().fit(X_tr)
5

<!-- page: 4 -->

model = keras.Sequential([
6
keras.Input(shape=(64,)),
7
layers.Dense(128, activation="relu"),
8
layers.Dropout(0.2),
9
layers.Dense(64, activation="relu"),
10
layers.Dense(10, activation="softmax"),
11
])
12
model.compile(optimizer=keras.optimizers.Adam(1e-3),
13
loss="sparse_categorical_crossentropy", metrics=["
accuracy"])
14
model.summary()
15
stop = keras.callbacks.EarlyStopping(patience=5, restore_best_weights
=True)
16
history = model.fit(scaler.transform(X_tr), y_tr, epochs=50,
batch_size=64,
17
validation_split=0.1, callbacks=[stop])
18
print(model.evaluate(scaler.transform(X_te), y_te))
Listing 12.7: Vòng lặp huấn luyện tối giản với PyTorch
1
import torch
2
from torch import nn
3

<!-- page: 123 -->
CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
117
4
net = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 10)
)
5

<!-- page: 5 -->

opt = torch.optim.Adam(net.parameters(), lr=1e-3)
6
loss_fn = nn.CrossEntropyLoss()
7
Xt = torch.tensor(scaler.transform(X_tr), dtype=torch.float32)
8
yt = torch.tensor(y_tr)
9
for epoch in range(100):
10
opt.zero_grad()
11
loss = loss_fn(net(Xt), yt)
# lan truyen xuoi
12
loss.backward()
# lan truyen nguoc (autograd)
13
opt.step()
# cap nhat trong so
Loại dữliệu
Kiến trúc phù hợp
Ví dụứng dụng
Dạng bảng
MLP; thường thua Gradient
Boosting (Chương 8)
Dựđoán giá, rủi ro tín dụng
Ảnh
CNN, Vision Transformer
Phân loại ảnh, phát hiện đối
tượng
Chuỗi, văn bản
RNN/LSTM, Transformer
Dịch máy, phân tích cảm
xúc, LLM
Bảng 12.5: Lựa chọn kiến trúc theo loại dữliệu
12.8
Tóm tắt chương
• Perceptron là bộphân lớp tuyến tính, không học được XOR; thêm lớp ẩn với hàm kích
hoạt phi tuyến cho MLP có khảnăng xấp xỉvạn năng.
• Lan truyền xuôi tính đầu ra; lan truyền ngược dùng quy tắc dây chuyền tính gradient cho
mọi trọng số; cập nhật bằng SGD/Adam.
• ReLU cho lớp ẩn; sigmoid/softmax cho lớp ra phân lớp; ghép đúng với cross-entropy.
• Chuẩn hóa đầu vào, khởi tạo hợp lý, điều chuẩn L2, Dropout và dừng sớm là các kỹthuật
thiết yếu.

<!-- page: 6 -->

• scikit-learn cho MLP cơ bản; Keras/PyTorch cho học sâu trên GPU.
12.9
Bài tập
1. Tìm trọng sốperceptron cho hàm OR và NAND. Ghép chúng với perceptron AND (Bảng 12.2)
thành mạng hai lớp biểu diễn XOR; kiểm tra trên cả4 đầu vào.
2. Chạy lại ví dụlan truyền ngược thêm 100 bước. Vẽmất mát theo sốbước. Lặp lại với
hàm kích hoạt ReLU ởlớp ẩn.
3. Chứng minh σ′(z) = σ(z)(1 −σ(z)) và σ′(z) ≤0,25. Ước lượng độlớn gradient ởlớp
đầu tiên của mạng 10 lớp sigmoid.
4. Với softmax và cross-entropy, chứng minh ∂L/∂zk = ˆyk −yk.

<!-- page: 124 -->
CHƯƠNG 12. MẠNG NƠ-RON NHÂN TẠO
(NEURAL NETWORK)
118
5. Huấn luyện MLPClassifier trên tập digits có và không có StandardScaler. So sánh
độchính xác và sốvòng lặp.
6. So sánh MLPRegressor, Ridge và Gradient Boosting trên Ames Housing bằng RMSE
kiểm định chéo 5-fold.
Tài liệu tham khảo của chương
1. Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. Mathematics
of Control, Signals and Systems, 2(4), 303–314.
2. Glorot, X., & Bengio, Y. (2010). Understanding the difficulty of training deep feedforward
neural networks. Proceedings of AISTATS 2010, 249–256.
3. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
4. Hornik, K. (1991). Approximation capabilities of multilayer feedforward networks. Neural
Networks, 4(2), 251–257.
5. Kingma, D. P., & Ba, J. (2015). Adam: A Method for Stochastic Optimization. ICLR 2015.
6. LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521, 436–444.
7. McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous
activity. Bulletin of Mathematical Biophysics, 5, 115–133.
8. Minsky, M., & Papert, S. (1969). Perceptrons. MIT Press.
9. Rosenblatt, F. (1958). The perceptron: A probabilistic model for information storage and
organization in the brain. Psychological Review, 65(6), 386–408.
10. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by
back-propagating errors. Nature, 323, 533–536.
11. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014).
Dropout: A Simple Way to Prevent Neural Networks from Overfitting. Journal of Machine
Learning Research, 15, 1929–1958.
12. Vaswani, A., et al. (2017). Attention Is All You Need. Advances in Neural Information
Processing Systems 30.
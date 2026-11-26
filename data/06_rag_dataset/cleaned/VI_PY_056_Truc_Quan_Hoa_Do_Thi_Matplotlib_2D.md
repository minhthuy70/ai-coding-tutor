# VI_PY_056: Trực quan hóa đồ thị 2D: Tùy biến trục tọa độ, chú giải và màu sắc

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Matplotlib | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
axes[1].plot(history['val_accuracy'],
label='Validation')
,→
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].set_title('Model Accuracy')
axes[1].legend()
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
return fig
# Sửdụng
# fig = plot_learning_curves(history)
# plt.savefig('learning_curves.png', dpi=300,
bbox_inches='tight')
,→
7.8
Bài tập thực hành
Bài tập 1: Biểu đồcơ bản Vẽbiểu đồđường thểhiện nhiệt độtrong 7 ngày: [25, 27,
26, 28, 30, 29, 27] độC. Thêm grid, labels, title và lưu hình với DPI cao.
Bài tập 2: Histogram và Distribution Tạo 1000 sốngẫu nhiên từphân phối chuẩn
(mean=100, std=15). Vẽhistogram với 30 bins, thêm đường KDE và đánh dấu mean,
median trên biểu đồ.
Bài tập 3: Scatter plot với màu sắc Tạo 100 điểm dữliệu 2D. Vẽscatter plot với màu
sắc thểhiện giá trịcủa biến thứ3. Thêm colorbar và tùy chỉnh colormap.
Bài tập 4: Bar chart so sánh Cho điểm thi của 5 sinh viên ở3 môn (Toán, Lý, Hóa).
Vẽgrouped bar chart so sánh điểm của từng sinh viên. Thêm giá trịtrên mỗi cột.
Bài tập 5: EDA với Iris Dataset Sửdụng dataset Iris từscikit-learn. Thực hiện EDA
đầy đủ:
• Vẽpairplot đểxem correlation giữa các features
• Vẽheatmap của correlation matrix
• Vẽboxplot đểphát hiện outliers cho mỗi feature theo từng class
• Vẽviolin plot đểso sánh distribution
Bài tập 6: Confusion Matrix Tạo confusion matrix giảđịnh cho bài toán phân loại 4

lớp với 200 samples. Vẽconfusion matrix dạng heatmap, thêm annotations. Tính và hiển
thị:
• Precision, Recall, F1-score cho mỗi class
• Overall accuracy
177

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
• Class-wise performance bar chart
Bài tập 7: Learning Curves Analysis Mô phỏng training history của một mô hình:
• Epochs: 50
• Train loss giảm từ2.0 xuống 0.1
• Val loss giảm từ2.0 xuống 0.3 rồi tăng lên 0.5 (overfitting)
• Train accuracy tăng từ0.3 lên 0.98
• Val accuracy tăng từ0.3 lên 0.92 rồi giảm xuống 0.88
Vẽlearning curves và phân tích:
• Mô hình có overfitting không?
• Từepoch nào bắt đầu overfitting?
• Đềxuất early stopping point
Bài tập 8: ROC và PR Curves (Nâng cao) Tạo dữliệu cho bài toán binary classification:
• 500 samples (250 positive, 250 negative)
• So sánh 3 models với predicted probabilities khác nhau
• VẽROC curves của cả3 models trên cùng một plot
• VẽPrecision-Recall curves của cả3 models
• Tính AUC cho mỗi model
• Phân tích model nào tốt nhất và tại sao
Bài tập 9: Feature Importance Visualization Tạo random forest model cho regression
problem. Trích xuất feature importance và visualization:
• Bar chart horizontal cho top 15 features
• Sắp xếp theo importance
• Color coding theo mức độquan trọng
• Thêm cumulative importance line
Bài tập 10: Dashboard tổng hợp (Nâng cao) Tạo một dashboard đầy đủcho một bài
toán classification:
• Dataset: Sửdụng wine quality dataset hoặc tương tự
• Chia layout: 2 rows, 3 columns (6 subplots)
• Subplot 1: Distribution của target variable
• Subplot 2: Correlation heatmap
• Subplot 3: Top 5 feature importance
178

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
• Subplot 4: Confusion matrix
• Subplot 5: ROC curve với AUC score

• Subplot 6: Learning curves (loss và accuracy)
Yêu cầu: Sửdụng consistent color scheme, proper spacing, informative titles, và lưu với
resolution cao.
7.9
Kết luận
Chương này đã giới thiệu toàn diện vềvisualization trong Python, với trọng tâm vào
các ứng dụng trong Data Science, Machine Learning và Deep Learning. Visualization
không chỉlà công cụđể"vẽđẹp" mà là kỹnăng thiết yếu trong toàn bộquy trình Data
Science. Từviệc hiểu dữliệu ban đầu (EDA), đến theo dõi quá trình training, đánh giá
model, và truyền đạt insights cho stakeholders - visualization đều đóng vai trò then chốt.
Trong các chương tiếp theo, chúng ta sẽáp dụng các kỹthuật visualization này vào các
bài toán thực tếvềxửlý dữliệu, machine learning và deep learning. Các bài tập thực hành
trong chương này sẽgiúp củng cốkỹnăng và chuẩn bịtốt cho các ứng dụng phức tạp hơn.
Lưu ý quan trọng: Mọi biểu đồtrong chương này đều có thểtái tạo bằng cách chạy
code examples. Hình ảnh được lưu trong thư mục Hinh_ve/ với prefix ch8_. Sinh viên
nên thực hành chạy từng đoạn code đểhiểu sâu hơn vềcách hoạt động của từng loại
visualization và tùy chỉnh cho bài toán cụthểcủa mình.
179

CHƯƠNG 8. Tính toán Khoa học với Thư viện SciPy
8.1
Giới thiệu vềSciPy
Trong lĩnh vực tính toán khoa học và kỹthuật, việc giải quyết các bài toán phức tạp
như tích phân, giải phương trình vi phân, tối ưu hóa hay nội suy dữliệu là những yêu cầu
thường xuyên. Thư viện SciPy (Scientific Python) được phát triển nhằm cung cấp một hệ
sinh thái đầy đủcác công cụtính toán sốcho Python, mởrộng và bổsung cho khảnăng
xửlý mảng của NumPy.
SciPy không chỉđơn thuần là một tập hợp các hàm toán học, mà còn là một framework
tổng thểđược thiết kếtheo triết lý khoa học: mỗi module được phát triển bởi các chuyên
gia trong lĩnh vực tương ứng, đảm bảo tính chính xác, hiệu suất cao và tuân thủcác chuẩn
mực toán học quốc tế. Điều này khiến SciPy trởthành công cụkhông thểthiếu trong
nghiên cứu khoa học, phát triển sản phẩm công nghệvà giảng dạy đại học.
8.1.1
Cài đặt và Import
Trước khi sửdụng SciPy, chúng ta cần cài đặt thư viện thông qua pip. Vì SciPy phụ
thuộc vào NumPy, hệthống sẽtựđộng cài đặt NumPy nếu chưa có sẵn.
pip install scipy numpy matplotlib
Sau khi cài đặt, việc import các module của SciPy tuân theo quy ước: thay vì import
toàn bộthư viện, ta chỉimport các submodule cần thiết đểtránh xung đột tên và tối ưu bộ
nhớ.
import numpy as np
from scipy import integrate, optimize, interpolate
import matplotlib.pyplot as plt
8.1.2

Các Hàm Cơ bản và Hằng sốToán học
SciPy cung cấp một bộsưu tập phong phú các hàm đặc biệt (special functions) và hằng
sốtoán học chính xác cao, được sửdụng rộng rãi trong các bài toán khoa học và kỹthuật.
a, Hằng sốToán học
Module scipy.constants chứa các hằng sốvật lý và toán học được định nghĩa
theo chuẩn quốc tếCODATA. Việc sửdụng các hằng sốnày đảm bảo tính chính xác và
nhất quán trong tính toán khoa học.
from scipy import constants
# Hằng sốtoán học
180

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
print(f"Sốpi: {constants.pi}")
print(f"Sốe: {np.e}")
print(f"Tỉsốvàng: {constants.golden}")
# Hằng sốvật lý
print(f"Tốc độánh sáng: {constants.c} m/s")
print(f"Hằng sốPlanck: {constants.h} J·s")
print(f"Hằng sốAvogadro: {constants.Avogadro} mol^-1")
print(f"Hằng sốkhí lý tưởng: {constants.R} J/(mol·K)")
b, Hàm Đặc biệt
Module scipy.special cung cấp hàng trăm hàm đặc biệt trong toán học, bao gồm
các hàm gamma, hàm Bessel, hàm elliptic, và nhiều hàm khác. Những hàm này xuất hiện
thường xuyên trong lý thuyết xác suất, cơ học lượng tử, xửlý tín hiệu và nhiều lĩnh vực
khác.
from scipy import special
# Hàm Gamma và log-Gamma
x = 5
print(f"Gamma({x}) = {special.gamma(x)}")
# Gamma(5) = 4! =
24
,→
print(f"ln[Gamma({x})] = {special.loggamma(x)}")
# Hàm Bessel bậc nhất loại thứnhất (quan trọng trong sóng
điện từ)
,→
x_values = np.linspace(0, 10, 100)
j0 = special.j0(x_values)
# Bessel function of first kind,
order 0
,→
# Hàm lỗi (Error function) - quan trọng trong xác suất và
thống kê
,→

z = 1.5
print(f"erf({z}) = {special.erf(z)}")
print(f"erfc({z}) = {special.erfc(z)}")
# Complementary
error function
,→
# Tổhợp và giai thừa
n, k = 10, 3
print(f"C({n},{k}) = {special.comb(n, k)}")
print(f"{n}! = {special.factorial(n)}")
Ví dụ, hàm Gamma Γ(n) = (n −1)! là mởrộng liên tục của giai thừa sang sốthực
181

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
và phức. Hàm lỗi erf(x) xuất hiện trong phân phối chuẩn và nhiều bài toán nhiệt động lực
học. Hiểu rõ các hàm này giúp chúng ta giải quyết các bài toán phức tạp một cách chính
xác và hiệu quả.
8.2
Tổng quan Các Gói của SciPy
SciPy được tổchức thành các module chuyên biệt, mỗi module tập trung vào một lĩnh
vực cụthểcủa tính toán khoa học. Kiến trúc modular này không chỉgiúp dễdàng bảo trì
và phát triển, mà còn cho phép người dùng chỉimport những phần cần thiết, tối ưu hóa
hiệu suất chương trình.
8.2.1
scipy.integrate - Tích phân và Phương trình Vi phân
Module này cung cấp các phương pháp tích phân sốchính xác cao và các công cụgiải
phương trình vi phân thường (ODE) cũng như phương trình vi phân đại số(DAE). Trong
kỹthuật, việc tính toán diện tích dưới đường cong, tổng năng lượng, hoặc mô phỏng động
học của hệthống đều dựa vào các công cụnày.
8.2.2
scipy.optimize - Tối ưu hóa và Tìm nghiệm
Tối ưu hóa là bài toán tìm giá trịcực đại hoặc cực tiểu của một hàm sốdưới các ràng
buộc nhất định. Module scipy.optimize cung cấp đầy đủcác thuật toán từcơ bản
(gradient descent, Newton) đến nâng cao (simulated annealing, differential evolution).
Bên cạnh đó, module này còn chứa các công cụtìm nghiệm của phương trình phi tuyến,
từphương pháp chia đôi (bisection) đến các phương pháp lặp Newton-Raphson.
8.2.3
scipy.interpolate - Nội suy và Xấp xỉ
Trong thực tế, dữliệu thường được thu thập tại các điểm rời rạc. Nội suy (interpolation)
là kỹthuật ước lượng giá trịtại các điểm trung gian dựa trên dữliệu đã biết. Module này
cung cấp nhiều phương pháp nội suy khác nhau: tuyến tính, đa thức, spline, và radial basis
functions, mỗi phương pháp phù hợp với từng loại dữliệu và yêu cầu độmịn khác nhau.
8.2.4
scipy.linalg - Đại sốTuyến tính

Mởrộng từnumpy.linalg, module này cung cấp các thuật toán đại sốtuyến tính
chuyên sâu hơn, bao gồm phân tích QR, SVD, phân tách Cholesky, và giải các hệphương
trình tuyến tính với ma trận đặc biệt (tam giác, băng, thưa). Đây là nền tảng cho machine
learning, xửlý ảnh, và mô phỏng hệthống vật lý.
8.2.5
scipy.signal - Xửlý Tín hiệu
Module này chuyên vềxửlý tín hiệu sốvà analog: thiết kếbộlọc, phân tích phổ,
convolution, correlation, và biến đổi Fourier. Ứng dụng rộng rãi trong viễn thông, âm
thanh, hình ảnh và điều khiển tựđộng.
8.2.6
scipy.stats - Thống kê và Xác suất
Cung cấp hơn 100 phân phối xác suất liên tục và rời rạc, các kiểm định thống kê (t-test,
chi-square, ANOVA), và công cụphân tích dữliệu thống kê. Đây là công cụthiết yếu cho
khoa học dữliệu và nghiên cứu thực nghiệm.
182

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
8.2.7
scipy.sparse - Ma trận Thưa
Trong nhiều bài toán thực tế(mạng xã hội, phương trình đạo hàm riêng, đồthị), ma
trận có kích thước lớn nhưng phần lớn phần tửbằng 0. Module này cung cấp các cấu trúc
dữliệu và thuật toán tối ưu cho ma trận thưa, tiết kiệm bộnhớvà tăng tốc độtính toán.
8.2.8
scipy.fft - Biến đổi Fourier Nhanh
Biến đổi Fourier là công cụchuyển đổi tín hiệu từmiền thời gian sang miền tần số.
Module này cung cấp các thuật toán FFT hiệu quảcao, hỗtrợnhiều loại biến đổi (DFT,
DCT, DST) và tối ưu cho các kiến trúc phần cứng khác nhau.
8.3
Tính Tích phân với SciPy
Tích phân là một trong những phép toán cơ bản nhất trong giải tích, có ứng dụng rộng
rãi từtính diện tích, thểtích, đến tính công, năng lượng, xác suất và nhiều đại lượng vật
lý khác. Trong khi tích phân giải tích đòi hỏi kỹnăng toán học cao và không phải lúc nào
cũng tìm được nghiệm dạng đóng, tích phân số(numerical integration) cung cấp phương
pháp xấp xỉgiá trịtích phân với độchính xác kiểm soát được.
8.3.1
Cơ sởLý thuyết Tích phân Số
Ý tưởng cơ bản của tích phân sốlà chia khoảng tích phân thành nhiều đoạn nhỏ, xấp
xỉdiện tích dưới đường cong trên mỗi đoạn bằng các hình đơn giản (hình chữnhật, hình
thang, parabol), rồi cộng tổng các diện tích này lại. Độchính xác phụthuộc vào sốlượng
đoạn chia và phương pháp xấp xỉđược sửdụng.
Các phương pháp tích phân sốphổbiến bao gồm:
• Phương pháp hình chữnhật: Xấp xỉđơn giản nhất, sửdụng hình chữnhật có chiều
cao bằng giá trịhàm tại một điểm trong đoạn.
• Phương pháp hình thang (Trapezoidal rule): Nối các điểm liên tiếp bằng đoạn

thẳng, diện tích là tổng các hình thang.
• Phương pháp Simpson: Sửdụng parabol bậc hai đểxấp xỉhàm trên mỗi cặp đoạn,
cho độchính xác cao hơn.
• Phương pháp Gauss: Lựa chọn thông minh các điểm lấy mẫu và trọng sốđểđạt độ
chính xác cao nhất với sốđiểm cho trước.
SciPy tích hợp các thuật toán adaptive (thích nghi), tựđộng điều chỉnh bước chia để
đạt độchính xác mong muốn, đặc biệt hiệu quảvới các hàm có dao động mạnh hoặc điểm
kỳdị.
8.3.2
Tích phân Một biến với quad
Hàm integrate.quad là công cụchính đểtính tích phân xác định một biến. Tên
"quad" xuất phát từ"quadrature", thuật ngữcổđiển chỉphép tính tích phân số.
183

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
from scipy import integrate
import numpy as np
# Ví dụ1: Tích phân cơ bản
# Tính integral từ0 đến pi của sin(x) dx = 2
def f1(x):
return np.sin(x)
result, error = integrate.quad(f1, 0, np.pi)
print(f"Integral[0,pi] sin(x) dx = {result:.10f}")
print(f"Sai sốước lượng: {error:.2e}")
# Ví dụ2: Hàm với tham số
# Tính integral từ0 đến vô cùng của e^(-ax) dx = 1/a với a
= 2
,→
def f2(x, a):
return np.exp(-a * x)
result, error = integrate.quad(f2, 0, np.inf, args=(2,))
print(f"Integral[0,inf] e^(-2x) dx = {result:.6f}")
print(f"Lý thuyết: 1/2 = {0.5}")
# Ví dụ3: Hàm phức tạp (phân phối chuẩn)
# Tích phân của hàm mật độxác suất chuẩn
def gaussian(x, mu, sigma):
return (1 / (sigma * np.sqrt(2 * np.pi))) * \
np.exp(-0.5 * ((x - mu) / sigma)**2)
# Xác suất P(mu-sigma <= X <= mu+sigma) ~= 0.6827
mu, sigma = 0, 1
prob, err = integrate.quad(gaussian, mu - sigma, mu + sigma,
args=(mu, sigma))
print(f"P(mu-sigma <= X <= mu+sigma) = {prob:.4f} (~=
68.27%)")

,→
Hàm quad trảvềhai giá trị: kết quảtích phân và ước lượng sai sốtuyệt đối. Việc có
sai sốước lượng giúp đánh giá độtin cậy của kết quả, đặc biệt quan trọng trong các tính
toán khoa học nghiêm ngặt.
8.3.3
Tích phân Bội
Trong nhiều bài toán thực tế, ta cần tính tích phân trên miền hai chiều hoặc ba chiều.
SciPy cung cấp các hàm dblquad (tích phân kép) và tplquad (tích phân bội ba) cho
mục đích này.
184

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
# Ví dụ4: Tích phân kép - Tính thểtích
# V = double integral f(x,y) dA trên miền D
# Tính thểtích dưới mặt z = x² + y² trên hình chữnhật
[0,1]×[0,1]
,→
def f_surface(y, x):
# Lưu ý: thứtựtham số(y, x) do thứtựtích phân
return x**2 + y**2
# Cận tích phân: x từ0 đến 1, y từ0 đến 1
volume, error = integrate.dblquad(f_surface, 0, 1,
# cận
của x
,→
lambda x: 0,
# cận
dưới của y
,→
lambda x: 1)
# cận
trên của y
,→
print(f"Thểtích dưới mặt z = x² + y²: {volume:.6f}")
# Ví dụ5: Tích phân với cận biến thiên
# Tính diện tích hình tròn đơn vịbằng tích phân kép
# A = double integral 1 dA trên x^2 + y^2 <= 1
def integrand(y, x):
return 1
# Với mỗi x, y chạy từ-sqrt(1-x^2) đến sqrt(1-x^2)
area, err = integrate.dblquad(
integrand,
-1, 1,
# x từ-1 đến 1

lambda x: -np.sqrt(1 - x**2),
# cận dưới y
lambda x: np.sqrt(1 - x**2)
# cận trên y
)
print(f"Diện tích hình tròn đơn vị: {area:.6f}")
print(f"So với pi = {np.pi:.6f}")
Cần lưu ý rằng trong dblquad, tích phân ngoài cùng (theo biến đầu tiên trong danh
sách tham số) được thực hiện sau, và các cận của tích phân trong có thểphụthuộc vào
biến của tích phân ngoài. Điều này cho phép mô tảcác miền tích phân phức tạp.
8.3.4
Ứng dụng: Tính Năng lượng và Công
Trong vật lý và kỹthuật, tích phân thường được sửdụng đểtính các đại lượng như
công, năng lượng, moment, và khối lượng.
185

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
# Ví dụ6: Tính công của lực biến thiên
# Một lò xo có độcứng k = 100 N/m được nén từvịtrí x=0
đến x=0.2m
,→
# Lực: F(x) = kx, Công: W = integral F(x)dx
k = 100
# N/m
x_max = 0.2
# m
def spring_force(x):
return k * x
work, err = integrate.quad(spring_force, 0, x_max)
print(f"Công nén lò xo: {work:.2f} J")
print(f"Lý thuyết: ½kx² = {0.5 * k * x_max**2:.2f} J")
# Ví dụ7: Khối lượng của vật thểcó mật độbiến thiên
# Thanh dài L = 2m có mật độtuyến tính rho(x) = rho0*(1 +
x^2) kg/m
,→
# Khối lượng: M = integral rho(x)dx
rho_0 = 5
# kg/m
L = 2
# m
def density(x):
return rho_0 * (1 + x**2)
mass, err = integrate.quad(density, 0, L)
print(f"Khối lượng thanh: {mass:.3f} kg")

8.4
Giải Phương trình Vi phân với SciPy
Phương trình vi phân (Differential Equations) là công cụtoán học mô tảsựbiến thiên
của các đại lượng theo thời gian hoặc không gian. Hầu hết các định luật vật lý, từcơ học
Newton, phương trình Maxwell, đến phương trình Schr¨odinger, đều được biểu diễn dưới
dạng phương trình vi phân. Trong kỹthuật, phương trình vi phân được sửdụng đểmô
hình hóa mạch điện, hệthống điều khiển, động lực học chất lỏng, và vô sốứng dụng khác.
8.4.1
Phương trình Vi phân Thường (ODE)
Phương trình vi phân thường (Ordinary Differential Equation - ODE) là phương trình
chứa hàm sốmột biến và các đạo hàm của nó. Dạng tổng quát của ODE bậc nhất là:
dy
dt = f(t, y)
186

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
với điều kiện ban đầu y(t0) = y0. Bài toán tìm hàm y(t) thỏa mãn phương trình và điều
kiện ban đầu được gọi là bài toán giá trịban đầu (Initial Value Problem - IVP).
8.4.2
Phương pháp SốGiải ODE
Không giống như tích phân, phần lớn các phương trình vi phân không có nghiệm giải
tích dạng đóng. Phương pháp sốlà cách tiếp cận chính đểgiải quyết các phương trình này.
Các phương pháp phổbiến bao gồm:
• Phương pháp Euler: Đơn giản nhất, sửdụng xấp xỉbằng đạo hàm hữu hạn, nhưng
độchính xác thấp.
• Phương pháp Runge-Kutta: Gia đình các phương pháp chính xác hơn, trong đó
RK45 (Runge-Kutta bậc 4-5) là phổbiến nhất, cân bằng giữa độchính xác và hiệu
suất.
• Phương pháp Predictor-Corrector: Kết hợp dựđoán và hiệu chỉnh đểcải thiện độ
ổn định.
• Phương pháp Implicit: Sửdụng cho các hệ"stiff" (cứng), khi có sựchênh lệch lớn
vềtốc độbiến thiên.
8.4.3
Sửdụng solve_ivp
Hàm integrate.solve_ivp (solve initial value problem) là công cụhiện đại và
linh hoạt nhất trong SciPy đểgiải ODE. Nó tựđộng lựa chọn thuật toán phù hợp và điều
chỉnh bước thời gian đểđảm bảo độchính xác.
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# Ví dụ8: Phân rã phóng xạ
# dN/dt = -lambda*N, với N(0) = N0
# Nghiệm giải tích: N(t) = N0 * e^(-lambda*t)
lambda_decay = 0.5
# hằng sốphân rã

N0 = 100
# sốnguyên tửban đầu
def decay_rate(t, N):
return -lambda_decay * N
# Giải trên khoảng thời gian [0, 10]
t_span = (0, 10)
t_eval = np.linspace(0, 10, 100)
# Các điểm muốn tính
nghiệm
,→
sol = solve_ivp(decay_rate, t_span, [N0], t_eval=t_eval)
187

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
# So sánh với nghiệm giải tích
N_exact = N0 * np.exp(-lambda_decay * sol.t)
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'b-', label='Numerical solution')
plt.plot(sol.t, N_exact, 'r--', label='Exact solution')
plt.xlabel('Time (s)')
plt.ylabel('N(t)')
plt.title('Radioactive Decay: dN/dt = -lambda*N')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../Hinh_ve/ch9_decay.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
print(f"Sai sốtối đa: {np.max(np.abs(sol.y[0] -
N_exact)):.6e}")
,→
8.4.4
HệPhương trình Vi phân
Nhiều hệthống thực tếđược mô tảbởi hệnhiều phương trình vi phân tương tác với
nhau. Ví dụ, chuyển động của con lắc kép, động lực học quần thểsinh học, hoặc mạch
điện RLC đều yêu cầu giải hệODE.
# Ví dụ9: Con lắc đơn
# Phương trình: theta'' + (g/L)sin(theta) = 0
# Chuyển vềhệbậc nhất: theta' = omega, omega' =
-(g/L)sin(theta)
,→
g = 9.81
# m/s²
L = 1.0

# m
def pendulum(t, y):
theta, omega = y
dtheta_dt = omega
domega_dt = -(g / L) * np.sin(theta)
return [dtheta_dt, domega_dt]
# Dieu kien ban dau: theta(0) = 30 do, omega(0) = 0
theta0 = np.radians(30)
omega0 = 0
y0 = [theta0, omega0]
t_span = (0, 10)
188

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
t_eval = np.linspace(0, 10, 500)
sol = solve_ivp(pendulum, t_span, y0, t_eval=t_eval,
method='RK45')
,→
# Vẽbiểu đồ
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
# Góc theo thời gian
ax1.plot(sol.t, np.degrees(sol.y[0]), 'b-', linewidth=2)
ax1.set_ylabel('Góc theta (độ)')
ax1.set_title('Dao động Con lắc Đơn')
ax1.grid(True, alpha=0.3)
# Không gian pha (theta, omega)
ax2.plot(np.degrees(sol.y[0]), sol.y[1], 'r-', linewidth=2)
ax2.set_xlabel('Goc theta (do)')
ax2.set_ylabel('Van toc goc omega (rad/s)')
ax2.set_title('Khong gian Pha')
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../Hinh_ve/ch9_pendulum.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
8.4.5
Ứng dụng: Mô hình Lotka-Volterra (Săn mồi - Con mồi)
Mô hình Lotka-Volterra mô tảđộng lực học của hai quần thểtương tác: con mồi (prey)
và kẻsăn mồi (predator). Đây là ví dụkinh điển của hệphi tuyến cho thấy hành vi phức
tạp từcác quy tắc đơn giản.
# Ví dụ10: Mô hình Lotka-Volterra
# dx/dt = alpha*x - beta*x*y
(con mồi)

# dy/dt = delta*x*y - gamma*y
(săn mồi)
def lotka_volterra(t, z, alpha, beta, delta, gamma):
x, y = z
# x: con mồi, y: săn mồi
dx_dt = alpha * x - beta * x * y
dy_dt = delta * x * y - gamma * y
return [dx_dt, dy_dt]
# Tham số
alpha = 1.0
# Tốc độsinh con mồi
189

CHƯƠNG 8. TÍNH TOÁN KHOA HỌC VỚI THƯ VIỆN SCIPY
beta = 0.1
# Tốc độsăn mồi tiêu diệt con mồi
delta = 0.075 # Hiệu suất chuyển đổi con mồi →săn mồi
gamma = 1.5
# Tốc độchết tựnhiên của săn mồi
# Điều kiện ban đầu
x0, y0 = 10, 5
# Sốlượng ban đầu
y0_state = [x0, y0]
t_span = (0, 50)
t_eval = np.linspace(0, 50, 1000)
sol = solve_ivp(lotka_volterra, t_span, y0_state,
t_eval=t_eval,
,→
args=(alpha, beta, delta, gamma),
method='RK45')
,→
# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
# Biến thiên theo thời gian
ax1.plot(sol.t, sol.y[0], 'b-', label='Con mồi (x)',
linewidth=2)
,→
ax1.plot(sol.t, sol.y[1], 'r-', label='Săn mồi (y)',
linewidth=2)
,→
ax1.set_xlabel('Thời gian')
ax1.set_ylabel('Sốlượng')
ax1.set_title('Động lực học Quần thể')
ax1.legend()

ax1.grid(True, alpha=0.3)
# Không gian pha
ax2.plot(sol.y[0], sol.y[1], 'g-', linewidth=2)
ax2.plot(x0, y0, 'ko', markersize=10, label='Điểm ban đầu')
ax2.set_xlabel('Con mồi (x)')
ax2.set_ylabel('Săn mồi (y)')
ax2.set_title('Không gian Pha')
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../Hinh_ve/ch9_lotka_volterra.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
190
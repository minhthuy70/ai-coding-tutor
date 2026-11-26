# VI_PY_054: Thư viện SciPy: Giải hệ phương trình phi tuyến và tối ưu hóa hàm số

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: SciPy | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 6. THƯ VIỆN NUMPY TRONG KỸTHUẬT
• Tổng công suất: ≈122.0 W
Lưu ý: Bài 7 là bài nâng cao kết hợp kiến thức NumPy với ứng dụng thực tếtrong kỹ
thuật điện. Sinh viên cần nắm vững đại sốtuyến tính và cách sửdụng module np.linalg.
147

CHƯƠNG 7. Trực quan hóa dữliệu - Visualization
7.1
Giới thiệu vềTrực quan hóa dữliệu trong Kỹthuật
Trong thời đại công nghệsốvà dữliệu lớn, khảnăng chuyển đổi những con sốphức
tạp thành hình ảnh trực quan dễhiểu đã trởthành một kỹnăng thiết yếu đối với mọi kỹsư
và nhà nghiên cứu. Trực quan hóa dữliệu không đơn thuần là việc vẽbiểu đồđẹp mắt, mà
là một công cụmạnh mẽgiúp con người khám phá tri thức ẩn chứa trong dữliệu, kiểm
chứng giảthuyết khoa học và truyền đạt kết quảnghiên cứu một cách thuyết phục.
Trong lĩnh vực kỹthuật, dữliệu được thu thập từvô sốnguồn khác nhau: cảm biến đo
lường tham sốmôi trường, thiết bịgiám sát hiệu suất máy móc, kết quảmô phỏng sốtrên
máy tính, hay các thí nghiệm trong phòng thí nghiệm. Khối lượng dữliệu này thường rất
lớn và phức tạp, khiến việc quan sát trực tiếp từbảng sốtrởnên không khảthi. Đây chính
là lúc trực quan hóa phát huy tác dụng. Một biểu đồđường đơn giản có thểgiúp kỹsư
nhận ra xu hướng biến đổi nhiệt độtheo thời gian. Một biểu đồphân tán có thểlàm rõ
mối quan hệphi tuyến giữa hai biến sốtrong quá trình thiết kế. Một histogram có thểtiết
lộsựphân bốkhông đồng đều của ứng suất trong kết cấu, từđó cảnh báo vềnhững điểm
yếu tiềm ẩn.
Vai trò của trực quan hóa không chỉdừng lại ởviệc hỗtrợphân tích dữliệu mà còn
là cầu nối giữa con người và máy tính trong quá trình giải quyết vấn đềkỹthuật. Khi xây
dựng mô hình toán học hoặc thuật toán tính toán, việc quan sát kết quảtrung gian thông
qua đồthịgiúp người thiết kếphát hiện sai lầm, điều chỉnh tham sốvà tối ưu hóa phương
pháp một cách trực quan và nhanh chóng. Trong giai đoạn kiểm chứng, biểu đồso sánh
giữa kết quảtính toán và dữliệu thực nghiệm là phương tiện quan trọng đểđánh giá độ
chính xác và tin cậy của mô hình.
Hơn nữa, trong môi trường làm việc đa ngành và hợp tác toàn cầu, khảnăng truyền đạt
ý tưởng và kết quảnghiên cứu một cách rõ ràng là vô cùng quan trọng. Một hình ảnh trực
quan được thiết kếtốt có thểvượt qua rào cản ngôn ngữvà chuyên môn, giúp các bên liên

quan từquản lý dựán đến chuyên gia kỹthuật cùng hiểu được bản chất vấn đềvà đưa ra
quyết định đúng đắn. Báo cáo kỹthuật, bài báo khoa học hay bản trình bày dựán đều trở
nên sinh động và thuyết phục hơn nhờcó sựhỗtrợcủa các biểu đồđược thiết kếcông
phu.
Python đã trởthành ngôn ngữlập trình được ưa chuộng nhất trong cộng đồng khoa
học và kỹthuật nhờvào hệsinh thái thư viện phong phú và mạnh mẽ. Trong lĩnh vực trực
quan hóa dữliệu, Python cung cấp nhiều công cụtừcơ bản đến nâng cao, phù hợp với mọi
nhu cầu. Matplotlib là thư viện nền tảng, cho phép kiểm soát chi tiết mọi yếu tốcủa biểu
đồtừmàu sắc, kiểu nét vẽđến vịtrí các nhãn và chú thích. Seaborn mởrộng Matplotlib
với các hàm tạo biểu đồthống kê chuyên nghiệp, đặc biệt hữu ích trong phân tích khám
phá dữliệu. Plotly cung cấp biểu đồtương tác, cho phép người xem phóng to, thu nhỏvà
khám phá chi tiết dữliệu ngay trên trình duyệt web.
148

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Chương này sẽgiới thiệu các kỹthuật trực quan hóa dữliệu cơ bản và nâng cao sử
dụng Python, tập trung vào ứng dụng thực tếtrong các bài toán kỹthuật. Sinh viên sẽ
học cách tạo các loại biểu đồphổbiến như đồthịđường, biểu đồcột, biểu đồphân tán
và histogram, đồng thời nắm vững cách tùy chỉnh biểu đồđểphù hợp với yêu cầu trình
bày chuyên nghiệp. Thông qua các ví dụminh họa từnhiều lĩnh vực kỹthuật khác nhau,
chương sẽgiúp người học phát triển khảnăng tư duy trực quan và kỹnăng phân tích dữ
liệu, những phẩm chất cần thiết cho một kỹsư thời đại mới.
7.2
Cài đặt và cấu hình
7.2.1
Cài đặt thư viện
pip install matplotlib seaborn pandas scikit-learn
7.2.2
Import và cấu hình
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# Cấu hình style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
# Cấu hình matplotlib
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
# Hiển thịinline trong Jupyter
%matplotlib inline
7.2.3
Lưu hình ảnh
# Lưu hình với resolution cao

plt.savefig('Hinh_ve/figure_name.png', dpi=300,
bbox_inches='tight')
,→
# Lưu nhiều formats
plt.savefig('Hinh_ve/figure_name.pdf', format='pdf',
bbox_inches='tight')
,→
7.3
Matplotlib: Nền tảng Visualization
Matplotlib là thư viện cốt lõi cho visualization trong Python, cung cấp kiểm soát chi
tiết cao và tính linh hoạt tuyệt vời.
149

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
7.3.1
Cấu trúc cơ bản: Figure và Axes
Matplotlib sửdụng kiến trúc phân tầng với hai khái niệm chính:
• Figure: Toàn bộcửa sổhoặc trang vẽ
• Axes: Vùng vẽcụthể(subplot) trong Figure
# Tạo figure và axes
fig, ax = plt.subplots(figsize=(8, 6))
# Vẽdữliệu
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')
# Tùy chỉnh
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Hàm lượng giác')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('Hinh_ve/ch8_basic_plot.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Hình 7.1: Đồthịhàm lượng giác cơ bản
150

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
7.3.2
Line Plot - Đồthịđường
Line plot phù hợp cho dữliệu chuỗi thời gian, theo dõi xu hướng.
# Tạo dữliệu thời gian

time = np.arange(0, 100)
temperature = 20 + 5 * np.sin(2 * np.pi * time / 24) + \
np.random.normal(0, 1, 100)
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(time, temperature, linewidth=2, color='coral',
marker='o', markersize=3, alpha=0.8)
ax.set_xlabel('Thời gian (giờ)')
ax.set_ylabel('Nhiệt độ(°C)')
ax.set_title('Biến động nhiệt độtheo thời gian')
ax.grid(True, linestyle='--', alpha=0.5)
ax.axhline(y=20, color='red', linestyle='--',
label='Nhiệt độtrung bình')
ax.legend()
plt.savefig('Hinh_ve/ch8_line_plot.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Hình 7.2: Line plot theo dõi nhiệt độtheo thời gian
7.3.3
Scatter Plot - Biểu đồphân tán
Scatter plot hiển thịmối quan hệgiữa hai biến liên tục, rất hữu ích trong EDA và phân
tích correlation.
# Tạo dữliệu với correlation
np.random.seed(42)
151

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
n = 200
x = np.random.randn(n)
y = 2 * x + np.random.randn(n) * 0.5
colors = x + y
# Màu theo tổng
fig, ax = plt.subplots(figsize=(8, 8))
scatter = ax.scatter(x, y, c=colors, cmap='viridis',
s=50, alpha=0.6, edgecolors='black')
ax.set_xlabel('Feature X', fontsize=12)
ax.set_ylabel('Feature Y', fontsize=12)
ax.set_title('Scatter Plot: Correlation giữa X và Y',
fontsize=14)
,→
plt.colorbar(scatter, ax=ax, label='X + Y')
# Vẽđường hồi quy
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

ax.plot(x, p(x), "r--", linewidth=2,
label=f'y={z[0]:.2f}x+{z[1]:.2f}')
,→
ax.legend()
plt.savefig('Hinh_ve/ch8_scatter_plot.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.3.4
Histogram và Distribution Plot
Histogram hiển thịphân phối của biến liên tục, quan trọng đểkiểm tra normality và
phát hiện skewness.
# Tạo dữliệu từcác phân phối khác nhau
normal_data = np.random.normal(100, 15, 1000)
uniform_data = np.random.uniform(50, 150, 1000)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Histogram 1: Normal distribution
axes[0].hist(normal_data, bins=30, color='skyblue',
edgecolor='black', alpha=0.7)
axes[0].axvline(normal_data.mean(), color='red',
linestyle='--', linewidth=2, label='Mean')
axes[0].set_xlabel('Giá trị')
axes[0].set_ylabel('Tần suất')
axes[0].set_title('Phân phối chuẩn (Normal)')
152

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.3: Scatter plot với regression line
axes[0].legend()
# Histogram 2: Uniform distribution
axes[1].hist(uniform_data, bins=30, color='lightcoral',
edgecolor='black', alpha=0.7)
axes[1].axvline(uniform_data.mean(), color='red',
linestyle='--', linewidth=2, label='Mean')
axes[1].set_xlabel('Giá trị')
axes[1].set_ylabel('Tần suất')
axes[1].set_title('Phân phối đều (Uniform)')
axes[1].legend()
plt.tight_layout()
plt.savefig('Hinh_ve/ch8_histogram.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.3.5

Bar Chart - Biểu đồcột
Bar chart phù hợp cho dữliệu categorical, so sánh giữa các nhóm.
153

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.4: So sánh histogram của phân phối chuẩn và phân phối đều
# Dữliệu accuracy của các models
models = ['Linear\nRegression', 'Decision\nTree',
'Random\nForest', 'XGBoost', 'Neural\nNetwork']
accuracy = [0.78, 0.82, 0.88, 0.91, 0.89]
colors_list = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A',
'#98D8C8']
,→
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(models, accuracy, color=colors_list,
edgecolor='black', linewidth=1.5)
# Thêm giá trịtrên mỗi cột
for bar in bars:
height = bar.get_height()
ax.text(bar.get_x() + bar.get_width()/2., height,
f'{height:.2f}',
ha='center', va='bottom', fontsize=11,
fontweight='bold')
,→
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('So sánh Accuracy của các Models', fontsize=14,
fontweight='bold')
,→
ax.set_ylim(0.7, 1.0)
ax.grid(axis='y', alpha=0.3)
plt.savefig('Hinh_ve/ch8_bar_chart.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.3.6
Subplots - Vẽnhiều biểu đồ
Subplots cho phép so sánh nhiều khía cạnh dữliệu cùng lúc.
154

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.5: Bar chart so sánh accuracy của các models
# Tạo dữliệu training history
epochs = np.arange(1, 51)

train_loss = 2.5 * np.exp(-epochs/10) + 0.1
val_loss = 2.5 * np.exp(-epochs/12) + 0.15 +
np.random.rand(50) * 0.1
,→
train_acc = 1 - train_loss / 3
val_acc = 1 - val_loss / 3
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
# Loss curves
axes[0, 0].plot(epochs, train_loss, label='Train Loss',
linewidth=2)
,→
axes[0, 0].plot(epochs, val_loss, label='Val Loss',
linewidth=2)
,→
axes[0, 0].set_xlabel('Epochs')
axes[0, 0].set_ylabel('Loss')
axes[0, 0].set_title('Training vs Validation Loss')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)
# Accuracy curves
axes[0, 1].plot(epochs, train_acc, label='Train Acc',
linewidth=2)
,→
axes[0, 1].plot(epochs, val_acc, label='Val Acc',
linewidth=2)
,→
155

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
axes[0, 1].set_xlabel('Epochs')
axes[0, 1].set_ylabel('Accuracy')
axes[0, 1].set_title('Training vs Validation Accuracy')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
# Learning rate schedule
lr = 0.01 * np.exp(-epochs/20)
axes[1, 0].plot(epochs, lr, color='green', linewidth=2)
axes[1, 0].set_xlabel('Epochs')
axes[1, 0].set_ylabel('Learning Rate')
axes[1, 0].set_title('Learning Rate Schedule')
axes[1, 0].grid(True, alpha=0.3)
# Overfitting gap
gap = val_loss - train_loss
axes[1, 1].fill_between(epochs, 0, gap, alpha=0.5,

color='red')
,→
axes[1, 1].plot(epochs, gap, color='darkred', linewidth=2)
axes[1, 1].set_xlabel('Epochs')
axes[1, 1].set_ylabel('Loss Gap')
axes[1, 1].set_title('Overfitting Gap (Val - Train)')
axes[1, 1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Hinh_ve/ch8_subplots.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.4
Seaborn: Statistical Visualization
Seaborn được xây dựng trên Matplotlib, tập trung vào statistical graphics với API đơn
giản và aesthetic mặc định đẹp hơn.
7.4.1
Boxplot - Phát hiện Outliers
Boxplot hiển thịfive-number summary (min, Q1, median, Q3, max) và outliers, rất
hữu ích trong EDA.
# Tạo dữliệu với outliers
np.random.seed(42)
model_a = np.append(np.random.normal(0.85, 0.05, 100), [0.5,
0.95, 0.98])
,→
model_b = np.append(np.random.normal(0.88, 0.04, 100), [0.6,
0.97])
,→
156

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.6: Subplots hiển thịtraining history của neural network
model_c = np.random.normal(0.90, 0.06, 100)
# Pad arrays to same length
max_len = max(len(model_a), len(model_b), len(model_c))
model_b = np.pad(model_b, (0, max_len - len(model_b)),
constant_values=np.nan)
model_c = np.pad(model_c, (0, max_len - len(model_c)),
constant_values=np.nan)
df = pd.DataFrame({'Model A': model_a, 'Model B': model_b,
'Model C': model_c})
,→
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, palette='Set2', ax=ax)

ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('Boxplot: Phân phối Accuracy của các Models',
fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
plt.savefig('Hinh_ve/ch8_boxplot.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
157

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.7: Boxplot phát hiện outliers trong performance của models
7.4.2
Violin Plot - Phân phối chi tiết
Violin plot kết hợp boxplot với kernel density estimation, cho thấy shape của distribution
rõ ràng hơn.
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# Violin plot
sns.violinplot(data=df, palette='muted', ax=axes[0])
axes[0].set_ylabel('Accuracy')
axes[0].set_title('Violin Plot')
axes[0].grid(axis='y', alpha=0.3)
# Swarm plot (hiển thịtừng điểm)
sns.swarmplot(data=df, palette='dark', size=3, ax=axes[1])
axes[1].set_ylabel('Accuracy')
axes[1].set_title('Swarm Plot')
axes[1].grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('Hinh_ve/ch8_violin_swarm.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.4.3
Heatmap - Correlation Matrix
Heatmap hiển thịcorrelation matrix, giúp phát hiện multicollinearity và chọn features.
158

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.8: Violin plot và Swarm plot cho phân phối chi tiết
# Tạo dữliệu features
np.random.seed(42)
n_samples = 500
feature_data = {

'age': np.random.randint(18, 65, n_samples),
'income': np.random.normal(50000, 15000, n_samples),
'credit_score': np.random.randint(300, 850, n_samples),
'debt': np.random.normal(10000, 5000, n_samples),
'loan_amount': np.random.normal(30000, 10000, n_samples)
}
df_features = pd.DataFrame(feature_data)
correlation_matrix = df_features.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f',
cmap='coolwarm', center=0, square=True,
linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Correlation Matrix của Features',
fontsize=14, fontweight='bold')
plt.savefig('Hinh_ve/ch8_heatmap.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.4.4
Pairplot - Quan hệgiữa nhiều biến
Pairplot tạo grid of scatter plots cho tất cảcác cặp biến, rất hữu ích trong EDA.
159

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.9: Heatmap hiển thịcorrelation matrix
# Load Iris dataset
from sklearn.datasets import load_iris
iris_data = load_iris()
iris_df = pd.DataFrame(data=iris_data.data,
columns=iris_data.feature_names)
iris_df['species'] = iris_data.target
iris_df['species'] = iris_df['species'].map(
{0: 'setosa', 1: 'versicolor', 2: 'virginica'})
# Pairplot
pairplot = sns.pairplot(iris_df, hue='species',
palette='Set1',
,→
diag_kind='kde', height=2.5,
aspect=1.2)
,→
pairplot.fig.suptitle('Pairplot: Iris Dataset',
y=1.02, fontsize=16,
fontweight='bold')
,→

plt.savefig('Hinh_ve/ch8_pairplot.png', dpi=300,
bbox_inches='tight')
,→
160
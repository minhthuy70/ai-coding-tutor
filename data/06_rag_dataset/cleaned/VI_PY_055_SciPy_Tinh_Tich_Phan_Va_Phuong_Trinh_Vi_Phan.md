# VI_PY_055: SciPy: Tính tích phân số và giải phương trình vi phân kỹ thuật

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: SciPy | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
axes[0, 1].set_title('Bimodal Distribution')
# Skewed distribution
skewed = np.random.exponential(2, 1000)
sns.histplot(skewed, kde=True, color='orange', ax=axes[1,
0])
,→
axes[1, 0].set_title('Right-Skewed Distribution')
# Multiple distributions
for i, (mu, sigma, label) in enumerate([(0, 1, 'Group 1'),
(3, 1.5, 'Group
2'),
,→
(-2, 0.8, 'Group
3')]):
,→
data = np.random.normal(mu, sigma, 500)
sns.kdeplot(data, ax=axes[1, 1], label=label,
linewidth=2)
,→
axes[1, 1].set_title('Comparison of Multiple Distributions')
axes[1, 1].legend()
plt.tight_layout()
plt.savefig('Hinh_ve/ch8_distributions.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.5
Visualization cho Machine Learning
7.5.1
Confusion Matrix
Confusion matrix hiển thịperformance của classification model, cho biết true/false
positives/negatives.
from sklearn.metrics import confusion_matrix

import seaborn as sns
# Giảlập dữliệu predictions
np.random.seed(42)
y_true = np.random.randint(0, 3, 300)
# 3 classes
y_pred = y_true.copy()
# Thêm một sốpredictions sai
errors = np.random.choice(300, 50, replace=False)
y_pred[errors] = np.random.randint(0, 3, 50)
# Tính confusion matrix
cm = confusion_matrix(y_true, y_pred)
162

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.11: Các loại phân phối dữliệu với histogram và KDE
# Vẽconfusion matrix
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
xticklabels=['Class 0', 'Class 1', 'Class 2'],
yticklabels=['Class 0', 'Class 1', 'Class 2'],
cbar_kws={'label': 'Count'}, ax=ax)
ax.set_xlabel('Predicted Label', fontsize=12)
ax.set_ylabel('True Label', fontsize=12)
ax.set_title('Confusion Matrix', fontsize=14,
fontweight='bold')
,→
plt.savefig('Hinh_ve/ch8_confusion_matrix.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.5.2
ROC Curve và AUC
ROC curve hiển thịtrade-off giữa True Positive Rate và False Positive Rate.
from sklearn.metrics import roc_curve, auc
# Giảlập probability predictions cho 3 models
163

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.12: Confusion Matrix cho multi-class classification
np.random.seed(42)
y_true_binary = np.random.randint(0, 2, 500)
# Model 1: Good
y_scores_1 = y_true_binary + np.random.normal(0, 0.3, 500)

# Model 2: Medium
y_scores_2 = y_true_binary + np.random.normal(0, 0.5, 500)
# Model 3: Poor
y_scores_3 = np.random.rand(500)
fig, ax = plt.subplots(figsize=(8, 8))
# VẽROC cho từng model
for scores, label, color in [(y_scores_1, 'Model 1',
'blue'),
,→
(y_scores_2, 'Model 2',
'green'),
,→
(y_scores_3, 'Model 3',
'red')]:
,→
fpr, tpr, _ = roc_curve(y_true_binary, scores)
roc_auc = auc(fpr, tpr)
ax.plot(fpr, tpr, color=color, linewidth=2,
label=f'{label} (AUC = {roc_auc:.2f})')
# Đường random baseline
164

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random
(AUC = 0.50)')
,→
ax.set_xlabel('False Positive Rate', fontsize=12)
ax.set_ylabel('True Positive Rate', fontsize=12)
ax.set_title('ROC Curves Comparison', fontsize=14,
fontweight='bold')
,→
ax.legend(loc='lower right', fontsize=11)
ax.grid(True, alpha=0.3)
plt.savefig('Hinh_ve/ch8_roc_curve.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Hình 7.13: ROC curves so sánh performance của nhiều models
7.5.3
Learning Curves - Phát hiện Overfitting
Learning curves giúp chẩn đoán overfitting, underfitting và đánh giá training progress.
# Tạo learning curves cho 3 scenarios
epochs = np.arange(1, 101)
165

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
# Scenario 1: Good fit
train_loss_good = 2 * np.exp(-epochs/15) + 0.05
val_loss_good = 2 * np.exp(-epochs/17) + 0.08
train_acc_good = 1 - 0.6 * np.exp(-epochs/12)
val_acc_good = 1 - 0.65 * np.exp(-epochs/14)
# Scenario 2: Overfitting
train_loss_over = 2 * np.exp(-epochs/10) + 0.02
val_loss_over = 2 * np.exp(-epochs/25) + 0.15 + epochs *
0.002
,→
train_acc_over = 1 - 0.5 * np.exp(-epochs/8)
val_acc_over = 1 - 0.8 * np.exp(-epochs/20) - epochs * 0.001
# Scenario 3: Underfitting
train_loss_under = 1.5 + np.random.rand(100) * 0.2
val_loss_under = 1.6 + np.random.rand(100) * 0.2
train_acc_under = 0.5 + np.random.rand(100) * 0.05
val_acc_under = 0.48 + np.random.rand(100) * 0.05
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
# Good Fit
axes[0, 0].plot(epochs, train_loss_good, label='Train',
linewidth=2)
,→
axes[0, 0].plot(epochs, val_loss_good, label='Validation',
linewidth=2)
,→
axes[0, 0].set_title('Good Fit: Loss', fontsize=12,
fontweight='bold')
,→
axes[0, 0].set_xlabel('Epochs')
axes[0, 0].set_ylabel('Loss')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)
axes[1, 0].plot(epochs, train_acc_good, label='Train',
linewidth=2)
,→
axes[1, 0].plot(epochs, val_acc_good, label='Validation',
linewidth=2)
,→
axes[1, 0].set_title('Good Fit: Accuracy', fontsize=12,
fontweight='bold')
,→
axes[1, 0].set_xlabel('Epochs')

axes[1, 0].set_ylabel('Accuracy')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)
166

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
# Overfitting
axes[0, 1].plot(epochs, train_loss_over, label='Train',
linewidth=2)
,→
axes[0, 1].plot(epochs, val_loss_over, label='Validation',
linewidth=2)
,→
axes[0, 1].set_title('Overfitting: Loss', fontsize=12,
fontweight='bold')
,→
axes[0, 1].set_xlabel('Epochs')
axes[0, 1].set_ylabel('Loss')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
axes[1, 1].plot(epochs, train_acc_over, label='Train',
linewidth=2)
,→
axes[1, 1].plot(epochs, val_acc_over, label='Validation',
linewidth=2)
,→
axes[1, 1].set_title('Overfitting: Accuracy', fontsize=12,
fontweight='bold')
,→
axes[1, 1].set_xlabel('Epochs')
axes[1, 1].set_ylabel('Accuracy')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)
# Underfitting
axes[0, 2].plot(epochs, train_loss_under, label='Train',
linewidth=2, alpha=0.7)
axes[0, 2].plot(epochs, val_loss_under, label='Validation',
linewidth=2, alpha=0.7)
axes[0, 2].set_title('Underfitting: Loss', fontsize=12,
fontweight='bold')
,→
axes[0, 2].set_xlabel('Epochs')
axes[0, 2].set_ylabel('Loss')
axes[0, 2].legend()

axes[0, 2].grid(True, alpha=0.3)
axes[1, 2].plot(epochs, train_acc_under, label='Train',
linewidth=2, alpha=0.7)
axes[1, 2].plot(epochs, val_acc_under, label='Validation',
linewidth=2, alpha=0.7)
axes[1, 2].set_title('Underfitting: Accuracy', fontsize=12,
fontweight='bold')
,→
axes[1, 2].set_xlabel('Epochs')
axes[1, 2].set_ylabel('Accuracy')
axes[1, 2].legend()
167

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
axes[1, 2].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Hinh_ve/ch8_learning_curves.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Hình 7.14: Learning curves cho 3 scenarios: Good fit, Overfitting, Underfitting
7.5.4
Feature Importance
Hiển thịmức độquan trọng của features trong model.
# Feature importance từRandom Forest (giảlập)
features = ['Age', 'Income', 'Credit Score', 'Employment
Years',
,→
'Debt Ratio', 'Loan Amount', 'Previous Loans',
'Property Value', 'Education Level', 'City
Size']
,→
importances = np.array([0.15, 0.22, 0.18, 0.09, 0.14,
0.08, 0.06, 0.04, 0.03, 0.01])
# Sort theo importance
indices = np.argsort(importances)[::-1]
sorted_features = [features[i] for i in indices]
sorted_importances = importances[indices]
fig, ax = plt.subplots(figsize=(10, 6))
168

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
colors = plt.cm.viridis(np.linspace(0.3, 0.9,

len(sorted_features)))
,→
bars = ax.barh(sorted_features, sorted_importances,
color=colors)
,→
# Thêm giá trị
for i, (bar, imp) in enumerate(zip(bars,
sorted_importances)):
,→
ax.text(imp + 0.005, i, f'{imp:.3f}',
va='center', fontsize=10, fontweight='bold')
ax.set_xlabel('Importance Score', fontsize=12)
ax.set_title('Feature Importance trong Random Forest Model',
fontsize=14, fontweight='bold')
ax.grid(axis='x', alpha=0.3)
plt.savefig('Hinh_ve/ch8_feature_importance.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Hình 7.15: Feature importance từRandom Forest model
7.5.5
Precision-Recall Curve
Precision-Recall curve phù hợp với imbalanced datasets.
from sklearn.metrics import precision_recall_curve,
average_precision_score
,→
# Giảlập dữliệu imbalanced
169

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
np.random.seed(42)
y_true_imb = np.concatenate([np.ones(100), np.zeros(900)])
y_scores_good = y_true_imb + np.random.normal(0, 0.3, 1000)
y_scores_poor = y_true_imb + np.random.normal(0, 0.7, 1000)
fig, ax = plt.subplots(figsize=(8, 8))
for scores, label, color in [(y_scores_good, 'Good Model',
'blue'),
,→
(y_scores_poor, 'Poor Model',
'red')]:
,→
precision, recall, _ =
precision_recall_curve(y_true_imb, scores)
,→

ap = average_precision_score(y_true_imb, scores)
ax.plot(recall, precision, color=color, linewidth=2,
label=f'{label} (AP = {ap:.2f})')
# Baseline
ax.axhline(y=0.1, color='k', linestyle='--', linewidth=2,
label='Baseline (Random)')
ax.set_xlabel('Recall', fontsize=12)
ax.set_ylabel('Precision', fontsize=12)
ax.set_title('Precision-Recall Curve (Imbalanced Data)',
fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3)
plt.savefig('Hinh_ve/ch8_pr_curve.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.6
Visualization cho Deep Learning
7.6.1
Training History Visualization
Theo dõi metrics trong quá trình training neural network.
# Giảlập training history từKeras/TensorFlow
epochs = np.arange(1, 51)
history = {
'loss': 1.5 * np.exp(-epochs/10) + 0.1 +
np.random.rand(50) * 0.05,
,→
'val_loss': 1.5 * np.exp(-epochs/12) + 0.15 +
np.random.rand(50) * 0.08,
,→
170

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.16: Precision-Recall curve cho imbalanced dataset
'accuracy': 1 - 0.8 * np.exp(-epochs/8),
'val_accuracy': 1 - 0.85 * np.exp(-epochs/10),
'lr': 0.001 * np.exp(-epochs/20)
}
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
# Loss
axes[0, 0].plot(epochs, history['loss'], 'b-',
label='Training Loss', linewidth=2)
,→
axes[0, 0].plot(epochs, history['val_loss'], 'r-',

label='Validation Loss', linewidth=2)
,→
axes[0, 0].set_xlabel('Epoch', fontsize=11)
axes[0, 0].set_ylabel('Loss', fontsize=11)
axes[0, 0].set_title('Model Loss', fontsize=13,
fontweight='bold')
,→
axes[0, 0].legend(fontsize=10)
axes[0, 0].grid(True, alpha=0.3)
# Accuracy
171

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
axes[0, 1].plot(epochs, history['accuracy'], 'b-',
label='Training Accuracy', linewidth=2)
,→
axes[0, 1].plot(epochs, history['val_accuracy'], 'r-',
label='Validation Accuracy', linewidth=2)
,→
axes[0, 1].set_xlabel('Epoch', fontsize=11)
axes[0, 1].set_ylabel('Accuracy', fontsize=11)
axes[0, 1].set_title('Model Accuracy', fontsize=13,
fontweight='bold')
,→
axes[0, 1].legend(fontsize=10)
axes[0, 1].grid(True, alpha=0.3)
# Learning Rate
axes[1, 0].plot(epochs, history['lr'], 'g-', linewidth=2)
axes[1, 0].set_xlabel('Epoch', fontsize=11)
axes[1, 0].set_ylabel('Learning Rate', fontsize=11)
axes[1, 0].set_title('Learning Rate Schedule', fontsize=13,
fontweight='bold')
,→
axes[1, 0].set_yscale('log')
axes[1, 0].grid(True, alpha=0.3)
# Loss Gap (Overfitting indicator)
gap = history['val_loss'] - history['loss']
axes[1, 1].fill_between(epochs, 0, gap, alpha=0.3,
color='red')
,→
axes[1, 1].plot(epochs, gap, 'r-', linewidth=2)
axes[1, 1].axhline(y=0, color='k', linestyle='--',
alpha=0.5)
,→

axes[1, 1].set_xlabel('Epoch', fontsize=11)
axes[1, 1].set_ylabel('Val Loss - Train Loss', fontsize=11)
axes[1, 1].set_title('Overfitting Gap', fontsize=13,
fontweight='bold')
,→
axes[1, 1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Hinh_ve/ch8_dl_training.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
7.6.2
Visualizing Neural Network Architecture
Mô tảkiến trúc neural network một cách trực quan.
# Visualization đơn giản cho NN architecture
fig, ax = plt.subplots(figsize=(12, 8))
172

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
Hình 7.17: Training history visualization cho deep learning model
layers = [4, 6, 6, 3]
# Input, Hidden1, Hidden2, Output
layer_names = ['Input\nLayer', 'Hidden\nLayer 1',
'Hidden\nLayer 2', 'Output\nLayer']
# Vẽneurons
for i, (n_neurons, name) in enumerate(zip(layers,
layer_names)):
,→
x = i * 3
for j in range(n_neurons):
y = j - n_neurons/2
circle = plt.Circle((x, y), 0.3, color='lightblue',
ec='black', linewidth=2)
ax.add_patch(circle)
ax.text(x, -n_neurons/2 - 1, name, ha='center',
fontsize=12, fontweight='bold')
# Vẽconnections (chỉvẽmột sốđểtránh rối)
for i in range(len(layers) - 1):
for j in range(min(layers[i], 3)):
for k in range(min(layers[i+1], 3)):
x1, y1 = i * 3, j - layers[i]/2
x2, y2 = (i+1) * 3, k - layers[i+1]/2
ax.plot([x1+0.3, x2-0.3], [y1, y2], 'gray',
173

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
alpha=0.3, linewidth=0.5)
ax.set_xlim(-1, 10)
ax.set_ylim(-5, 4)
ax.axis('off')
ax.set_title('Neural Network Architecture (4-6-6-3)',
fontsize=14, fontweight='bold')
plt.savefig('Hinh_ve/ch8_nn_architecture.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Hình 7.18: Visualization của neural network architecture
7.6.3
Activation Maps Visualization
Trực quan hóa activation outputs của các layers trong CNN.
# Giảlập activation maps từCNN layers
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
fig.suptitle('CNN Activation Maps', fontsize=16,
fontweight='bold')
,→
for idx, ax in enumerate(axes.flat):
# Tạo activation map giảlập
activation = np.random.rand(28, 28) * (idx + 1) / 8
activation = activation * (activation > 0.3)
#
ReLU-like
,→
174

CHƯƠNG 7. TRỰC QUAN HÓA DỮLIỆU - VISUALIZATION
im = ax.imshow(activation, cmap='hot',
interpolation='nearest')
,→
ax.set_title(f'Filter {idx + 1}', fontsize=11)
ax.axis('off')
plt.colorbar(im, ax=ax, fraction=0.046)
plt.tight_layout()
plt.savefig('Hinh_ve/ch8_activation_maps.png', dpi=300,
bbox_inches='tight')
,→
plt.show()
Hình 7.19: Activation maps từCNN convolutional layers

7.7
Best Practices trong Data Visualization
7.7.1
Nguyên tắc thiết kếbiểu đồhiệu quả
1. Chọn loại biểu đồphù hợp:
• Line plot: Dữliệu chuỗi thời gian, xu hướng
• Bar chart: So sánh giữa các categories
• Scatter plot: Quan hệgiữa hai biến liên tục
• Histogram: Phân phối của một biến
• Box plot: So sánh distributions, phát hiện outliers
• Heatmap: Ma trận correlation, confusion matrix
2. Sửdụng màu sắc hiệu quả:
• Chọn palette phù hợp: sequential, diverging, qualitative
• Tránh quá nhiều màu khác nhau
175
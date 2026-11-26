# VI_PY_031: Kết nối và thao tác cơ sở dữ liệu quan hệ Python - MySQL / SQLite

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)
**Chuyên mục**: Cơ sở dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

120
RADIO BUTTON

121
CHECKBOX

122
SLIDER

123
ENTRY

124
TEXT AREA

125
Nội dung
Giới thiệu
Lập trình căn bản
Các kiểu dữ liệu phức
Lập trình hướng đối tượng
Vào/ra, ngoại lệ
Lập trình mạng
Lập trình Web
Python-MySQL
Giao diện GUI
Vẽ đồ thị

126
Vẽ đồ thị với Matplotlib
Ví dụ đơn giản
from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()

127
Vẽ đồ thị với Matplotlib
Các tùy chọn màu
'r' = red; 'g' = green; 'b' = blue; 'c' = cyan
'm' = magenta; 'y' = yellow; 'k' = black; 'w' = white
Các tùy chọn linestyle
'-' = solid
'--' = dashed
':' = dotted
'-.' = dot-dashed
'.' = points
'o' = filled circles
'^' = filled triangles

128
Vẽ đồ thị với Matplotlib
Ví dụ đơn giản với label, title, legend, ylim, linestyle
from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0, 20, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, '-b', label='sine')
plt.plot(x, y2, '-r', label='cosine')
plt.legend(loc='upper right')
plt.ylim(-1.5, 2.0)
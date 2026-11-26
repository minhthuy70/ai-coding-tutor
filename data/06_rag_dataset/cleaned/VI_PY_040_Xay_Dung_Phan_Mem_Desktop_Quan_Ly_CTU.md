# VI_PY_040: Tích hợp giao diện Tkinter và cơ sở dữ liệu xây dựng phần mềm quản lý

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)
**Chuyên mục**: Phần mềm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

133
Vẽ đồ thị với Matplotlib
Vẽ biểu đồ histogram
from matplotlib import pyplot as plt
import numpy as np
x = np.random.normal(size=1000)
fig, ax = plt.subplots()
H = ax.hist(x, bins=50, alpha=0.5, histtype='stepfilled')
plt.show()

134
Vẽ đồ thị với Matplotlib
Vẽ đồ thị pie
import matplotlib.pyplot as plt
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
plt.pie(sizes, explode=explode,
labels=labels, colors=colors,
autopct='%1.1f%%',
shadow=True, startangle=140)
plt.axis('equal')
plt.show()

135
Vẽ đồ thị với Matplotlib
Vẽ đồ thị boxplot
import matplotlib.pyplot as plt
value1 = [82,76,24,40,67,62,75,78,
71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,

90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,
86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,
10,87,29,72,16,23,72,88,78,99,75,30]

box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data,patch_artist=True,

labels=['course1','course2','course3','course4'])
plt.show()

136
Vẽ đồ thị với Matplotlib
Vẽ đồ thị contour
from matplotlib import pyplot as plt
import numpy as np
xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
x, y = np.meshgrid(xlist, ylist)
z = np.sqrt(x**2 + y**2)
plt.figure()
cp = plt.contourf(x, y, z)
plt.colorbar(cp)
plt.show()

137
Vẽ đồ thị với Matplotlib
Vẽ đồ thị 3D
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
c = x + y
ax.scatter(x, y, z, c=c)
plt.show()

138

Vẽ đồ thị với Matplotlib
Vẽ đồ thị chuyển động
from matplotlib import animation
from matplotlib import pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(-2, 2)
x = np.linspace(0, 2, 1000)
y = np.zeros_like(x)
line, = ax.plot(x, y, lw=2)
# initialization function: plot the background of each frame
def init():
    line.set_data([], [])

```python
return line,

```

139
Vẽ đồ thị với Matplotlib
Vẽ đồ thị chuyển động
# animation function.  This is called sequentially
def animate(i):
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)

```python
return line,
```

# call the animator.  blit=True means only re-draw
# the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                         frames=200, interval=20, blit=True)
plt.show()

140
Vẽ đồ thị với Matplotlib
Ghi đồ thị
from matplotlib import pyplot as plt
plt.savefig(file_name)
Đóng đồ thị
plt.cla()
plt.clf()
plt.close()
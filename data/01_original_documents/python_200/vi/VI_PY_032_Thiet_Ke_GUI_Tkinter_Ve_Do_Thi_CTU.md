<!-- page: 1 -->
# VI_PY_032: Thiết kế giao diện đồ họa GUI Tkinter và vẽ đồ thị trực quan hóa

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)  
**Chuyên mục**: Giao diện & Đồ họa | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 130 -->
130
Vẽ đồ thị với Matplotlib
Ví dụ với linestyle 
from matplotlib import pyplot as plt
import numpy as np
x1 = np.linspace(0, 10, 20)
y1 = np.sin(x1)
x2 = np.linspace(0, 10, 1000)
y2 = np.sin(x2)
plt.plot(x1, y1, 'bo', label='sampled')
plt.plot(x2, y2, ':k', label='continuous')
plt.legend()
plt.show()

<!-- page: 131 -->
131
Vẽ đồ thị với Matplotlib
Vẽ nhiều đồ thị 
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
ax1.bar([1,2,3],[3,4,5])
ax2.barh([1,2,3],[3,1,2])
ax3.scatter([0,1,2,3,4],[2,1,3,6,4])
plt.show()

<!-- page: 132 -->
132
Vẽ đồ thị với Matplotlib
Vẽ nhiều đồ thị

<!-- page: 133 -->

<!-- page: 2 -->

133
Vẽ đồ thị với Matplotlib
Vẽ biểu đồ histogram 
from matplotlib import pyplot as plt
import numpy as np
x = np.random.normal(size=1000)
fig, ax = plt.subplots()
H = ax.hist(x, bins=50, alpha=0.5, histtype='stepfilled')
plt.show()

<!-- page: 134 -->
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

<!-- page: 135 -->
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

<!-- page: 3 -->


<!-- page: 136 -->
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

<!-- page: 137 -->
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

<!-- page: 138 -->
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

<!-- page: 4 -->

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
```python
return line,

```
<!-- page: 139 -->
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

<!-- page: 140 -->
140
Vẽ đồ thị với Matplotlib
Ghi đồ thị 
from matplotlib import pyplot as plt
plt.savefig(file_name)
Đóng đồ thị
plt.cla()
plt.clf()
plt.close()

<!-- page: 141 -->
141
Tài liệu tham khảo
D. Beazley, B.K. Jones, “Python Cookbook”, O'Reilly Media, 
3rd ed., 2013
M. O. Faruque Sarker, “Python Network Programming 
Cookbook”, Packt Publishing, 2014
Tutorialspoint, “Python Tutorial", 2019
W3Schools, "Python Tutorial", 2019
Python, https://www.python.org

<!-- page: 5 -->

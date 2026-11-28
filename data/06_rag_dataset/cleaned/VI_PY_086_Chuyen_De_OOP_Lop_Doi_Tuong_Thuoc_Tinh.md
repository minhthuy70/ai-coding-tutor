# VI_PY_086: Chuyên đề OOP: Lớp, đối tượng, phương thức khởi tạo __init__

**Nguồn tài liệu chính thống**: Tài liệu Chuyên đề OOP Python - Đại học
**Chuyên mục**: OOP | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

2
Hướng đối tượng là gì?
• Là kỹ thuật bao bọc dữ liệu, nhằm tạo ra một kiểu
dữ liệu mới.
• Các khái niệm:
– Trừu tượng (Abstraction)
– Đa hình (Polymorphism)
– Đóng gói (Encapsulation)
– Kế thừa (Inheritance)

3
OOP, định nghĩa Class
• Python được xây dựng như một ngôn ngữ lập trình
hướng thủ tục (procedural language).
– OOP có tồn tại, hoạt động tốt nhưng không chặt chẽ
• Khai báo class như sau
class name:
statements

4
Fields (thuộc tính)
name = value
– Ví dụ:
# main
p1 = Diem()
p1.x = 2
p1.y = -5
– Thuộc tính là biến nằm trong lớp, mô tả đặc tính của đối
tượng.
– Được khai báo trực tiếp trong lớp hay trong hàm tạo
(constructors)
– Python không có tính chất đóng gói (encapsulation) hay

private fields
diem.py
1
2
3
class Diem:
x = 0
y = 0

5
Sử dụng Class
import class
– client programs must import the classes they use
point_main.py
1
2
3
4
5
6
7
8
9
10
from Diem import *
# main
p1 = Diem()
p1.x = 7
p1.y = -3
# Python objects are dynamic (can add fields any time!)
p1.name = "Tyler Durden"

6
Object Methods
def name(self, parameter, ..., parameter):
statements
– self must be the first parameter to any object method
• represents the "implicit parameter" (this in Java)
– must access the object's fields through the self reference
class Diem:
def dich_chuyen(self, dx, dy):
self.x += dx

self.y += dy
7
Exercise Answer
diem.py
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
from math import *
class Diem:
x = 0
y = 0
def dat_vi_tri(self, x, y):
self.x = x
self.y = y
def khoang_cach_tu_tam_o(self):
return sqrt(self.x * self.x + self.y * self.y)
def khoang_cach(self, other):
dx = self.x - other.x
dy = self.y - other.y
return sqrt(dx * dx + dy * dy)

8
Calling Methods
• Có 2 cách”
1)
object.method(parameters)
hoặc

2)
Class.method(object, parameters)
• Ví dụ:
p = Diem(3, -4)
p.dich_chuyen(1, 5)
Diem.dich_chuyen(p, 1, 5)

9
Constructors (hàm tạo)
def __init__(self, parameter, ..., parameter):
statements
– a constructor is a special method with the name __init__
– Ví dụ:
class Diem:
def __init__(self, x, y):
self.x = x
self.y = y
• How would we make it possible to construct a
Diem() with no parameters to get (0, 0)?
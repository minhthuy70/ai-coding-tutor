# VI_PY_087: Chuyên đề OOP: Kế thừa đơn, kế thừa bội và hàm super()

**Nguồn tài liệu chính thống**: Tài liệu Chuyên đề OOP Python - Đại học
**Chuyên mục**: OOP | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

10
toString and __str__
def __str__(self):
return string
– equivalent to Java's toString (converts object to a string)
– invoked automatically when str or print is called
Exercise: Write a __str__ method for diem objects that
returns strings like  "(3, -14)"
def __str__(self):
return "(" + str(self.x) + ", " + str(self.y) + ")"

11
Complete Point Class
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
18
19

20
21
from math import *
class Diem:
def __init__(self, x, y):
self.x = x
self.y = y
def khoang_cach_tu_tam_o(self):
return sqrt(self.x * self.x + self.y * self.y)
def khoang_cach(self, other):
dx = self.x - other.x
dy = self.y - other.y
return sqrt(dx * dx + dy * dy)
def dich_chuyen(self, dx, dy):
self.x += dx
self.y += dy
def __str__(self):
return "(" + str(self.x) + ", " + str(self.y) + ")"

12
Operator Overloading
• operator overloading: You can define functions so that
Python's built-in operators can be used with your class.
• See also: http://docs.python.org/ref/customization.html
Operator
Class Method
-
__sub__(self, other)
+
__add__(self, other)
*
__mul__(self, other)
/
__truediv__(self, other)
Unary Operators
-
__neg__(self)
+
__pos__(self)
Operator
Class Method
==
__eq__(self, other)
!=

__ne__(self, other)
<
__lt__(self, other)
>
__gt__(self, other)
<=
__le__(self, other)
>=
__ge__(self, other)

13
Bài tập
• Viết class PhanSo để biểu diễn phân số như 1/2
hay -3/8.
• Viết hàm rút gọn phân số; ví dụ, rút gọn 4/12
thành 1/3 hay 6/-9 thành -2/3.
– Hint: Sử dụng hàm tìm ước chứng lớn nhất (greatest
common divisor)
math.gcd(a,b)
• Định nghĩa hàm cong và nhan 2 phân số
• Định nghĩa các toán tử +, *, ==, <

14
Generating Exceptions
raise ExceptionType("message")
– useful when the client uses your object improperly
– types: ArithmeticError, AssertionError, IndexError,
NameError, SyntaxError, TypeError, ValueError
– Example:
class BankAccount:
def deposit(self, amount):
if amount < 0:
raise ValueError("negative amount")
15
Inheritance (thừa kế)
class name(superclass):
statements
– Ví dụ:
class Diem3D(Diem):   # Diem3D extends Diem

z = 0
• Python also supports multiple inheritance
class name(superclass, ..., superclass):
statements
(if > 1 superclass has the same field/method, conflicts are resolved in left-to-right order)

16
Calling Superclass Methods
• methods:
class.method(object, parameters)
• constructors:
class.__init__(parameters)
class Diem3D(Diem):
z = 0
def __init__(self, x, y, z):
Diem.__init__(self, x, y)
self.z = z
def dich_chuyen(self, dx, dy, dz):
Diem.dich_chuyen(self, dx, dy)
self.z += dz

17
Static method
• Để định nghĩa method dạng static thì thêm từ khóa
@staticmethod
• Ví dụ:
class class_name:
@staticmethod
def static_method_name(param_list):
pass
• Cách gọi:
class_name.static_method_name()
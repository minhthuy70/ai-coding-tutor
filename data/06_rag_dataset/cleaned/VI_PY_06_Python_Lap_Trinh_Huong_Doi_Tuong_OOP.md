## python

Classes and Objects; Inheritance Hướng đối tượng

## Hướng đối tượng là gì?

• Là kỹ thuật bao bọc dữ liệu, nhằm tạo ra một kiểu dữ liệu mới.

• Các khái niệm:

– Trừu tượng (Abstraction)

– Đa hình (Polymorphism)

– Đóng gói (Encapsulation)

– Kế thừa (Inheritance)

## 2 python" HIENLTH

## OOP, định nghĩa Class

• Python được xây dựng như một ngôn ngữ lập trình hướng thủ tục (procedural language).

– OOP có tồn tại, hoạt động tốt nhưng không chặt chẽ

• Khai báo class như sau

**class name**: **statements**

2 python" HIENLTH

```python
class Diem:
    x = 0
    y = 0
```

## Fields (thuộc tính)

## name = value

```python
- Ví dụ:
  # main
  p1 = Diem()
  p1.x = 2
  p1.y = -5
```

## diem.py

– Thuộc tính là biến nằm trong lớp, mô tả đặc tính của đối tượng.

– Được khai báo trực tiếp trong lớp hay trong hàm tạo (constructors)

– Python không có tính chất đóng gói (encapsulation) hay private fields

## 2 python" HIENLTH

## Sử dụng Class

import **class**

– client programs must import the classes they use

## point\_main.py

```python
from Diem import *

# main
p1 = Diem()
p1.x = 7
p1.y = -3
...

# Python objects are dynamic (can add fields any time!)
p1.name = "Tyler Durden"
```

## Object Methods

## def name(self, parameter, ..., parameter): statements

– **self** must be the first parameter to any object method • represents the "implicit parameter" (this in Java)

– must access the object's fields through the self reference

class **Diem**:

**def dich\_chuyen(self, dx, dy):**

**self**.x += dx

**self**.y += dy

2 python HIENLTH

## Exercise Answer

## diem.py

```python
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
```

## Calling Methods

• Có 2 cách”

1) **object**.**method**(**parameters**)

hoặc

2) **Class**.**method**(**object**, **parameters**)

```python
• Ví dụ:
    p = Diem(3, -4)
    p.dich_chuyen(1, 5)
    Diem.dich_chuyen(p, 1, 5)
```

2 python" HIENLTH

## Constructors (hàm tạo)

def **\_\_init\_\_(**self**, parameter, ..., parameter**): **statements**

– a constructor is a special method with the name \_\_init

```python
- Ví dụ:
  class Diem:
    def __init__(self, x, y):
      self.x = x
      self.y = y
    ...
```

• How would we make it possible to construct a Diem() with no parameters to get (0, 0)?

## python HIENLTH

```python
def __str__(self):
    return string
```

## toString and str

– equivalent to Java's toString (converts object to a string)

– invoked automatically when str or print is called

Exercise: Write a \_\_str\_\_ method for diem objects that returns strings like "(3, -14)"

```python
def __str__(self):
    return "(" + str(self.x) + ", " + str(self.y) + ")"
```

## 2 python" HIENLTH

## Complete Point Class

## diem.py

```python
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
```

## Operator Overloading

**operator overloading**: You can define functions so that Python's built-in operators can be used with your class.

• See also: [http://docs.python.org/ref/customization.html](http://docs.python.org/ref/customization.html)

| Operator | Class Method |
| - | __sub__(self, other) |
| + | __add__(self, other) |
| * | __mul__(self, other) |
| / | __truediv__(self, other) |

Unary Operators

| - | __neg__(self) |
| + | __pos__(self) |

| Operator | Class Method |
| == | __eq__(self, other) |
| != | __ne__(self, other) |
| &lt; | __lt__(self, other) |
| > | __gt__(self, other) |
| &lt;= | __le__(self, other) |
| >= | __ge__(self, other) |

## 2 python" HIENLTH

## Bài tập

• **Viết class PhanSo** để biểu diễn phân số như 1/2 hay -3/8.

• Viết hàm rút gọn phân số; ví dụ, rút gọn 4/12 thành 1/3 hay 6/-9 thành -2/3.

– Hint: Sử dụng hàm tìm ước chứng lớn nhất (greatest common divisor) ➔ math.gcd(a,b)

• Định nghĩa hàm **cong** và **nhan** 2 phân số

• Định nghĩa các toán tử +, \*, ==, <

2 python HIENLTH

## Generating Exceptions

## raise ExceptionType("message")

## – useful when the client uses your object improperly

– types: ArithmeticError, AssertionError, IndexError, NameError, SyntaxError, TypeError, ValueError

## – Example:

class BankAccount:

```python
def deposit(self, amount):
    if amount < 0:
        raise ValueError("negative amount")
```

## 2 python HIENLTH

## Inheritance (thừa kế)

class **name**(**superclass**): **statements**

```python
- Ví dụ:
  class Diem3D(Diem):    # Diem3D extends Diem
    z = 0
    ...
```

## • Python also supports multiple inheritance class name(superclass, ..., superclass): statements

(if > 1 superclass has the same field/method, conflicts are resolved in left right order)

2 python HIENLTH

## Calling Superclass Methods

• methods: **class**.**method**(**object**, **parameters**)

• constructors: **class**.\_\_init\_\_(**parameters**)

```python
class Diem3D(Diem):
    z = 0
    def __init__(self, x, y, z):
        Diem.__init__(self, x, y)
        self.z = z
```

```python
def dich_chuyen(self, dx, dy, dz):
    Diem.dich_chuyen(self, dx, dy)
    self.z += dz
```

## 2 python" HIENLTH

## Static method

• Để định nghĩa method dạng static thì thêm từ khóa **@staticmethod**

• Ví dụ:

class **class\_name**:

@staticmethod

def **static\_method\_name**(param\_list):

pass

• Cách gọi:

**class\_name**.**static\_method\_name**()

2 python HIENLTH
# VI_PY_050: Xử lý ngoại lệ chuẩn mực: try, except, else, finally và bẫy lỗi runtime

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Ngoại lệ | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
def is_square(self):
return self.width == self.height
# Sửdụng
rect = Rectangle(5, 10)
print(f"Dien tich: {rect.calculate_area()}")
print(f"Chu vi: {rect.calculate_perimeter()}")
print(f"La hinh vuong: {rect.is_square()}")
square = Rectangle(5, 5)
print(f"\nLa hinh vuong: {square.is_square()}")
Kết quảhiển thị:
Dien tich: 50
Chu vi: 30
La hinh vuong: False
La hinh vuong: True
5.5
Tính đóng gói (Encapsulation)
5.5.1
Khái niệm đóng gói
Đóng gói là một trong bốn tính chất cơ bản của OOP. Nó đềcập đến việc ẩn giấu các
chi tiết nội bộcủa đối tượng và chỉcung cấp các giao diện công khai đểtương tác với đối
tượng đó.
Đóng gói giúp:
• Bảo vệdữliệu khỏi việc truy cập và sửa đổi trực tiếp không mong muốn
• Tăng tính bảo mật của chương trình
• Dễdàng thay đổi cài đặt nội bộmà không ảnh hưởng đến code bên ngoài
5.5.2
Thuộc tính và phương thức riêng tư
Trong Python, quy ước đặt tên đểchỉra mức độtruy cập của thuộc tính và phương
thức:
• Public: Không có dấu gạch dưới ởđầu, có thểtruy cập từbất kỳđâu
• Protected: Một dấu gạch dưới ởđầu (_), quy ước không nên truy cập từbên ngoài
lớp
• Private: Hai dấu gạch dưới ởđầu (__), khó truy cập hơn từbên ngoài lớp

87

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
a, Ví dụvềđóng gói
class BankAccount:
def __init__(self, account_number, balance):
self.account_number = account_number
# Public
self.__balance = balance
# Private
def deposit(self, amount):
if amount > 0:
self.__balance += amount
print(f"Nop {amount}. So du moi:
{self.__balance}")
,→
else:
print("So tien nop phai lon hon 0")
def withdraw(self, amount):
if 0 < amount <= self.__balance:
self.__balance -= amount
print(f"Rut {amount}. So du con lai:
{self.__balance}")
,→
else:
print("So tien khong hop le hoac khong du")
def get_balance(self):
return self.__balance
# Sửdụng
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
print(f"So du hien tai: {account.get_balance()}")
# Không thểtruy cập trực tiếp __balance từbên ngoài
# print(account.__balance)
# Sẽgây lỗi
Kết quảhiển thị:
Nop 500. So du moi: 1500
Rut 200. So du con lai: 1300
So du hien tai: 1300
Trong ví dụtrên, thuộc tính __balance được bảo vệ, chỉcó thểthay đổi thông qua
các phương thức deposit() và withdraw(), đảm bảo tính nhất quán của dữliệu.
88

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
5.5.3
Getter và Setter
Getter và setter là các phương thức được sửdụng đểtruy cập và sửa đổi giá trịcủa
thuộc tính private một cách có kiểm soát:
class Student:
def __init__(self, name, age):
self.__name = name
self.__age = age
# Getter cho name
def get_name(self):
return self.__name
# Setter cho name
def set_name(self, name):
if isinstance(name, str) and len(name) > 0:
self.__name = name
else:
print("Ten khong hop le")
# Getter cho age
def get_age(self):
return self.__age
# Setter cho age
def set_age(self, age):
if isinstance(age, int) and 0 < age < 150:
self.__age = age
else:
print("Tuoi khong hop le")
# Sửdụng
sv = Student("Nguyen Van An", 20)
print(f"Ten: {sv.get_name()}, Tuoi: {sv.get_age()}")
sv.set_age(21)
print(f"Tuoi moi: {sv.get_age()}")
sv.set_age(-5)
# Sẽbịtừchối
Kết quảhiển thị:
Ten: Nguyen Van An, Tuoi: 20
Tuoi moi: 21
Tuoi khong hop le
89

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
5.5.4
Property decorator

Python cung cấp decorator @property đểtạo getter và setter một cách pythonic hơn:
class Temperature:
def __init__(self, celsius):
self.__celsius = celsius
@property
def celsius(self):
return self.__celsius
@celsius.setter
def celsius(self, value):
if value < -273.15:
print("Nhiet do khong the thap hon -273.15°C")
else:
self.__celsius = value
@property
def fahrenheit(self):
return self.__celsius * 9/5 + 32
# Sửdụng
temp = Temperature(25)
print(f"Nhiet do: {temp.celsius}°C = {temp.fahrenheit}°F")
temp.celsius = 30
print(f"Nhiet do moi: {temp.celsius}°C =
{temp.fahrenheit}°F")
,→
temp.celsius = -300
# Sẽbịtừchối
Kết quảhiển thị:
Nhiet do: 25°C = 77.0°F
Nhiet do moi: 30°C = 86.0°F
Nhiet do khong the thap hon -273.15°C
5.6
Tính kếthừa (Inheritance)
5.6.1
Khái niệm kếthừa
Kếthừa là cơ chếcho phép một lớp (lớp con) kếthừa các thuộc tính và phương thức từ
một lớp khác (lớp cha). Điều này giúp tái sửdụng mã nguồn và tạo ra mối quan hệphân
cấp giữa các lớp.
Lợi ích của kếthừa:
90

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
• Tái sửdụng code: Không cần viết lại các thuộc tính và phương thức đã có trong lớp
cha
• Mởrộng chức năng: Lớp con có thểthêm các thuộc tính và phương thức mới
• Ghi đè (override): Lớp con có thểthay đổi cách thức hoạt động của phương thức từ

lớp cha
5.6.2
Cú pháp kếthừa
class LopCha:
# Định nghĩa lớp cha
pass
class LopCon(LopCha):
# Định nghĩa lớp con
pass
5.6.3
Ví dụkếthừa cơ bản
class Person:
def __init__(self, name, age):
self.name = name
self.age = age
def display_info(self):
print(f"Ten: {self.name}")
print(f"Tuoi: {self.age}")
class Student(Person):
def __init__(self, name, age, student_id, major):
# Gọi constructor của lớp cha
super().__init__(name, age)
self.student_id = student_id
self.major = major
def display_info(self):
# Gọi phương thức của lớp cha
super().display_info()
print(f"Ma sinh vien: {self.student_id}")
print(f"Chuyen nganh: {self.major}")
# Sửdụng
person = Person("Nguyen Van A", 30)
print("Thong tin person:")
person.display_info()
91

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
print("\nThong tin student:")
student = Student("Tran Thi B", 20, "SV001", "Computer
Science")
,→
student.display_info()
Kết quảhiển thị:
Thong tin person:
Ten: Nguyen Van A

Tuoi: 30
Thong tin student:
Ten: Tran Thi B
Tuoi: 20
Ma sinh vien: SV001
Chuyen nganh: Computer Science
5.6.4
Phương thức super()
Hàm super() được sửdụng đểgọi phương thức của lớp cha từlớp con. Điều này đặc
biệt hữu ích khi muốn mởrộng chức năng của lớp cha mà không viết lại toàn bộcode.
5.6.5
Kếthừa nhiều cấp
Python hỗtrợkếthừa nhiều cấp, cho phép tạo ra chuỗi kếthừa dài:
class Animal:
def __init__(self, name):
self.name = name
def speak(self):
print(f"{self.name} phat ra tieng keu")
class Mammal(Animal):
def __init__(self, name, fur_color):
super().__init__(name)
self.fur_color = fur_color
def feed_milk(self):
print(f"{self.name} cho con bu")
class Dog(Mammal):
def __init__(self, name, fur_color, breed):
super().__init__(name, fur_color)
92

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
self.breed = breed
def speak(self):
print(f"{self.name} sua: Gau gau!")
def fetch(self):
print(f"{self.name} chay theo qua bong")
# Sửdụng
dog = Dog("Lucky", "Nau", "Golden Retriever")
dog.speak()
dog.feed_milk()
dog.fetch()
print(f"Mau long: {dog.fur_color}")
print(f"Giong: {dog.breed}")
Kết quảhiển thị:
Lucky sua: Gau gau!

Lucky cho con bu
Lucky chay theo qua bong
Mau long: Nau
Giong: Golden Retriever
5.6.6
Kiểm tra quan hệkếthừa
Python cung cấp các hàm đểkiểm tra quan hệkếthừa giữa các lớp và đối tượng:
class Animal:
pass
class Dog(Animal):
pass
dog = Dog()
# Kiểm tra kiểu của đối tượng
print(isinstance(dog, Dog))
# True
print(isinstance(dog, Animal))
# True
print(isinstance(dog, object))
# True (mọi lớp đều kếthừa
từobject)
,→
# Kiểm tra quan hệgiữa các lớp
print(issubclass(Dog, Animal))
# True
print(issubclass(Animal, Dog))
# False
93

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
Kết quảhiển thị:
True
True
True
True
False
5.7
Tính đa hình (Polymorphism)
5.7.1
Khái niệm đa hình
Đa hình là khảnăng của các đối tượng thuộc các lớp khác nhau có thểphản ứng khác
nhau đối với cùng một thông điệp (gọi phương thức cùng tên). Đa hình cho phép viết code
linh hoạt hơn, có thểlàm việc với nhiều loại đối tượng khác nhau mà không cần biết chính
xác kiểu của chúng.
5.7.2

Đa hình thông qua ghi đè phương thức
Lớp con có thểghi đè (override) phương thức của lớp cha đểcung cấp cài đặt riêng:
class Shape:
def __init__(self, name):
self.name = name
def area(self):
return 0
def describe(self):
print(f"Hinh {self.name} co dien tich:
{self.area()}")
,→
class Circle(Shape):
def __init__(self, radius):
super().__init__("Tron")
self.radius = radius
def area(self):
return 3.14159 * self.radius ** 2
class Rectangle(Shape):
def __init__(self, width, height):
super().__init__("Chu nhat")
self.width = width
self.height = height
def area(self):
94

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
return self.width * self.height
class Triangle(Shape):
def __init__(self, base, height):
super().__init__("Tam giac")
self.base = base
self.height = height
def area(self):
return 0.5 * self.base * self.height
# Sửdụng đa hình
shapes = [
Circle(5),
Rectangle(4, 6),
Triangle(3, 8)
]
for shape in shapes:
shape.describe()
Kết quảhiển thị:
Hinh Tron co dien tich: 78.53975

Hinh Chu nhat co dien tich: 24
Hinh Tam giac co dien tich: 12.0
Trong ví dụtrên, mặc dù các đối tượng có kiểu khác nhau, chúng ta vẫn có thểgọi
phương thức describe() và area() một cách thống nhất. Đây là sức mạnh của đa
hình.
5.7.3
Đa hình với các toán tử
Python cho phép định nghĩa lại các toán tửcho các lớp tựđịnh nghĩa thông qua các
phương thức đặc biệt:
class Vector2D:
def __init__(self, x, y):
self.x = x
self.y = y
def __add__(self, other):
return Vector2D(self.x + other.x, self.y + other.y)
def __sub__(self, other):
95

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
return Vector2D(self.x - other.x, self.y - other.y)
def __str__(self):
return f"Vector2D({self.x}, {self.y})"
def __eq__(self, other):
return self.x == other.x and self.y == other.y
# Sửdụng
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2
print(f"v1 + v2 = {v3}")
v4 = v1 - v2
print(f"v1 - v2 = {v4}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == v1: {v1 == v1}")
Kết quảhiển thị:
v1 + v2 = Vector2D(4, 6)
v1 - v2 = Vector2D(2, 2)
v1 == v2: False
v1 == v1: True
5.8
Các phương thức đặc biệt (Magic Methods)
5.8.1
Giới thiệu vềmagic methods
Magic methods (còn gọi là dunder methods - double underscore methods) là các
phương thức đặc biệt trong Python có tên bắt đầu và kết thúc bằng hai dấu gạch dưới.

Chúng cho phép các lớp tựđịnh nghĩa tương tác với các tính năng built-in của Python.
96

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
5.8.2
Một sốmagic methods thường dùng
Phương thức
Mục đích
__init__()
Khởi tạo đối tượng
__str__()
Biểu diễn chuỗi của đối tượng (cho print)
__repr__()
Biểu diễn chính thức của đối tượng
__len__()
Trảvềđộdài khi gọi len()
__eq__()
So sánh bằng (==)
__lt__()
So sánh nhỏhơn (<)
__gt__()
So sánh lớn hơn (>)
__add__()
Phép cộng (+)
__sub__()
Phép trừ(-)
__mul__()
Phép nhân (*)
5.8.3
Ví dụsửdụng magic methods
class Book:
def __init__(self, title, author, pages):
self.title = title
self.author = author
self.pages = pages
def __str__(self):
return f"'{self.title}' cua {self.author}"
def __repr__(self):
return f"Book('{self.title}', '{self.author}',
{self.pages})"
,→
def __len__(self):
return self.pages
def __eq__(self, other):

return (self.title == other.title and
self.author == other.author)
def __lt__(self, other):
return self.pages < other.pages
# Sửdụng
book1 = Book("Python Programming", "John Smith", 300)
book2 = Book("Data Science", "Jane Doe", 250)
book3 = Book("Python Programming", "John Smith", 300)
97

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
print(book1)
# Gọi __str__
print(repr(book2))
# Gọi __repr__
print(f"So trang: {len(book1)}") # Gọi __len__
print(f"book1 == book3: {book1 == book3}")
# Gọi __eq__
print(f"book2 < book1: {book2 < book1}")
# Gọi __lt__
Kết quảhiển thị:
'Python Programming' cua John Smith
Book('Data Science', 'Jane Doe', 250)
So trang: 300
book1 == book3: True
book2 < book1: True
5.9
Thuộc tính và phương thức lớp (Class Attributes and Methods)
5.9.1
Thuộc tính lớp
Thuộc tính lớp là thuộc tính được chia sẻbởi tất cảcác đối tượng của lớp đó. Chúng
được định nghĩa bên trong lớp nhưng bên ngoài các phương thức.
class Student:
# Thuộc tính lớp
school_name = "Dai hoc Bach Khoa Ha Noi"
student_count = 0
def __init__(self, name, student_id):
# Thuộc tính đối tượng
self.name = name
self.student_id = student_id
# Tăng sốlượng sinh viên
Student.student_count += 1
def display_info(self):
print(f"Sinh vien: {self.name}")

print(f"Ma SV: {self.student_id}")
print(f"Truong: {Student.school_name}")
# Sửdụng
print(f"So sinh vien ban dau: {Student.student_count}")
sv1 = Student("Nguyen Van An", "SV001")
sv2 = Student("Tran Thi Binh", "SV002")
print(f"So sinh vien hien tai: {Student.student_count}")
98

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
sv1.display_info()
Kết quảhiển thị:
So sinh vien ban dau: 0
So sinh vien hien tai: 2
Sinh vien: Nguyen Van An
Ma SV: SV001
Truong: Dai hoc Bach Khoa Ha Noi
5.9.2
Phương thức lớp
Phương thức lớp được định nghĩa bằng decorator @classmethod và nhận tham số
đầu tiên là cls (tham chiếu đến lớp, không phải đối tượng):
class Employee:
company_name = "Tech Corp"
raise_amount = 1.05
def __init__(self, name, salary):
self.name = name
self.salary = salary
def apply_raise(self):
self.salary = int(self.salary * self.raise_amount)
@classmethod
def set_raise_amount(cls, amount):
cls.raise_amount = amount
@classmethod
def from_string(cls, emp_str):
name, salary = emp_str.split('-')
return cls(name, int(salary))
def display_info(self):
print(f"Nhan vien: {self.name}, Luong:
{self.salary}")
,→
# Sửdụng phương thức lớp
Employee.set_raise_amount(1.10)
emp1 = Employee("An", 50000)
99

CHƯƠNG 5. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON
emp2 = Employee.from_string("Binh-60000")
emp1.display_info()
emp1.apply_raise()
emp1.display_info()
emp2.display_info()
Kết quảhiển thị:
Nhan vien: An, Luong: 50000
Nhan vien: An, Luong: 55000
Nhan vien: Binh, Luong: 60000
5.9.3
Phương thức tĩnh
Phương thức tĩnh được định nghĩa bằng decorator @staticmethod và không nhận
self hay cls. Chúng giống như các hàm thông thường nhưng thuộc vềnamespace của
lớp:
class MathUtils:
@staticmethod
def is_even(num):
return num % 2 == 0
@staticmethod
def is_prime(num):
if num < 2:
return False
for i in range(2, int(num ** 0.5) + 1):
if num % i == 0:
return False
return True
@staticmethod
def factorial(n):
if n <= 1:
return 1
return n * MathUtils.factorial(n - 1)
# Sửdụng phương thức tĩnh
print(f"10 la so chan: {MathUtils.is_even(10)}")
print(f"7 la so nguyen to: {MathUtils.is_prime(7)}")
print(f"5! = {MathUtils.factorial(5)}")
100
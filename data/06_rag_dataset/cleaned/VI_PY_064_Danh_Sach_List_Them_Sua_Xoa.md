# VI_PY_064: Danh sách List trong Python: Thao tác thêm, sửa, xóa phần tử

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn
**Chuyên mục**: Cấu trúc dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

point = {'x': 1, 'y': 2}
Truy xuất một giá trị dựa vào key của đối tượng. Ví dụ:
point = {'x': 3, 'y': 6, 'z' : 9}
print point[x]
(Hiển thị 3)
2.9.1. Thêm một phần tử
Để thêm một phần tử vào đối tượng đã khai báo, sử dụng
cấu trúc dict[key] = value . Ví dụ:
user = {'name': 'Jone', 'age': 30}
user['country'] = 'Vietnam'
print user
(Hiển thị {'country': 'Vietnam', 'age': 30, 'name':
 'Jone'})
2.9.2. Một số hàm, phương thức thông dụng:
dict.clear() : Xóa toàn bộ dữ liệu bên trong đối

tượng
dict.copy() : Trả về một bản copy của đối tượng
dict.fromkeys(seq[, value]) : Tạo một đối tượng với
danh sách key từ seq và nếu có truyền value thì lấy
đó làm giá trị cho các phần tử.
dict.has_key(key) : kiểm tra một key có tồn tại trong
đối tượng hay không.
dict.keys() : Trả về một List chứa các key
dict.values() : Trả về một List chứa các value

Chương 3. Phân chia module
Tất cả ví dụ cho đến thời điểm này đều được thực thi trong
command line hoặc từ một file python .py . Tuy nhiên, đối
với các ứng dụng lớn, có nhiều chức năng thì phân chia nhỏ
dự án thành các file khác nhau sẽ giúp dễ bảo trì và tái sử
dụng các thành phần đã thiết kế.

Chương này sẽ giúp bạn thiết kế các tính năng theo mô
hình các module và khi cần thì sẽ gọi file tương ứng và sử
dụng.
3.1. Các loại module / thư viện
Có 3 loại module thường thấy là:
1. Viết bằng Python: có phần mở rộng là .py
2. Các thư viện liên kết động: có phần mở rộng là .dll ,
.pyd , .so , .sl ,…
3. C-Module liên kết với trình phiên dịch.

3.2. Đường dẫn tìm để load module
Để tải một module vào script của bạn, sử dụng cú pháp
đơn giản:
import modulename
khi gặp câu lệnh trên thì trình biên dịch sẽ tiến hành tìm
kiếm file module tương ứng theo thứ tự thư mục sau:
1. Thư mục hiện hành mà script đang gọi
2. Các thư mục trong PYTHONPATH (nếu có set)
3. Các thư mục cài đặt chuẩn trên Linux/Unix..
Có thể biết được đường dẫn mà một module đã được load
bằng đoạn code dưới đây:

import math
math.__file__
(Ví dụ trả về '/usr/lib/python2.5/lib-dynload/math.
so')

import random
random.__file__
(Ví dụ trả về '/usr/lib/python2.5/random.pyc')
3.3. Lấy danh sách thuộc tính và phương
thức của một module
Để lấy được danh sách các thuộc tính và phương thức mà
module hỗ trợ, sử dụng hàm dir(modulename) . Ví dụ:

dir(math)
['__doc__', '__file__', '__name__', '__package__',
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degree
s', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'fa
ctorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma'
, 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'lo

g', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians
', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
Có thể gọi hàm dir() không truyền tham số để lấy các
thuộc tính và phương thức của scope hiện tại đang thực
thi.
3.4. Cách khai báo và sử dụng module
Giả sử bạn tạo một file python mymath.py có nội dung như
sau:

```python
def cong(a, b):
return a + b

    def tru(a, b):
return a - b

    def nhan(a, b):
return a * b
```

Sau đó, tạo một file có tên myexample.py , trong cùng thư
mục với file mymath.py vừa tạo ở trên, có nội dung như
sau:
import mymath

num1 = 1
num2 = 2

print 'Tong hai so la: ', mymath.cong(num1, num2)
Vào command line, thực hiện gọi file myexample như sau:

\$ python myexample.py
Sau khi thực hiện sẽ hiển thị lên màn hình là
Tong hai so la: 3
3.5. Package module
Có thể gom nhiều module .py vào một thư mục và tên thư
mục là tên của package và tạo một file __init__.py trong
thư mục này.
Như vậy, cấu trúc thư của một package sẽ như sau:
|-- mypack

|   |-- __init__.py
|   |-- mymodule1.py
|   |-- mymodule2.py
Có thể sử dụng mymodule1 theo cú pháp import sau:

import mypack.mymodule1
hoặc
import mypack.mymodule1 as mymodule1
hoặc
import mypack.mymodule1 as mod
Khi sử dụng một module thuộc một package thì các lệnh
trong file __init__.py sẽ được thực hiện trước. Thông
thường thì file __init__.py sẽ rỗng.
Có thể tạo các subpackage bên trong một package theo
đúng cấu trúc thư mục, có file __init__.py . Ví dụ:
import mypack.mysubpack.mysubsubpack.module
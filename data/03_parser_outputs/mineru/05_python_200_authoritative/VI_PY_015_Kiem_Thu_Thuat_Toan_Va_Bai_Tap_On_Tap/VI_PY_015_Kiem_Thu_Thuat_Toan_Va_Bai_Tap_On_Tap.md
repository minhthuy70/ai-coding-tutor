<!-- page: 1 -->
# VI_PY_015: Tổng hợp bài tập thực hành thuật toán và rèn luyện tư duy logic

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Bài tập | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 44 -->
8
print("nghiem cua phuong trinh: x = ", x)
Chương trình 4.7: Đáp án gợi ý cho Bài 3
Trang 44
The Dariu Foundation

<!-- page: 45 -->
4. Viết phương trình mô phỏng việc giải phương trình bậc hai 1 ẩn số: Cho phép
người dùng nhập vào a, b và c, sau đó in ra kết quảcủa chương trình. Trong bài
này, chúng ta cần phảm thêm thư viện sqrt đểtính căn bậc 2 bằng câu lệnh from
math import sqrt.
1 from math import sqrt
2
3 print("Phuong trinh bac hai : ax^2 + bx + c = 0")
4 a = float(input("a = "))
5 b = float(input("b = "))
6 c = float(input("c = "))
7
8 if a == 0:
9
if b == 0:
10
if c == 0:
11
print("Phuong trinh vo so nghiem!")
12
else:
13
print("Phuong trinh vo nghiem!")
14
else:
15
if c == 0:
16

<!-- page: 2 -->

print("Phuong trinh co 1 nghiem x = 0")
17
else:
18
x = -c / b
19
print("Phuong trinh co 1 nghiem x = ", x)
20 else:
21
delta = b ** 2 - 4 * a * c
22
if delta < 0:
23
print("Phuong trinh vo nghiem!")
24
elif delta == 0:
25
x = -b / (2 * a)
26
print("Phuong trinh co 1 nghiem x = ", x)
27
else:
28
print("Phuong trinh co 2 nghiem phan biet!")
29
x1 = float((-b - sqrt(delta)) / (2 * a))
30
x2 = float((-b + sqrt(delta)) / (2 * a))
31
print("x1 = ", x1)
32
print("x2 = ", x2)
Chương trình 4.8: Đáp án gợi ý cho Bài 4
Hướng dẫn lập trình Python cơ bản
Trang 45

<!-- page: 46 -->
7
Câu hỏi ôn tập
1. Câu lệnh if nào là đúng cú pháp trong Python?
A. if a>=2:
B. if (a >= 2)
C. if a >=2
D. Tất cảđều đúng
2. Kết quảcủa đoạn chương trình sau là gì?

<!-- page: 3 -->

1 x = True
2 y = False
3 z = False
4 if not x or y:
5
print (1)
6 elif not x or not y and z:
7
print (2)
8 elif not x or y or not y and x:
9
print (3)
10 else:
11
print (4)
A. 1
B. 2
C. 3
D. 4
3. Đoạn lệnh nào sau đây sẽthực hiện không thành công?
A.
1 if (1, 2): print(’a’)
B.
1 if (1, 2):
2
print(’a’)
C.
1
if (1, 2):
2
print(’a’)
D.
1 if (1, 2):
2
3
print(’a’)
4. Đểkết thúc một khối các câu lệnh trong phần thân của câu lệnh if, chúng ta
dùng:
A. Dấu chấm phẩy
B. Dấu đóng ngoặc nhọn
C. end
D. Một câu lệnh được thụt lùi ít hơn so với câu lệnh trước
Trang 46
The Dariu Foundation


<!-- page: 4 -->

<!-- page: 47 -->
5. Đoạn code sau có lỗi hay không?
1 d = {’a’: 0, ’b’: 1, ’c’: 0}
2 if d[’a’] > 0:
3
print(’ok’)
4 elif d[’b’] > 0:
5
print(’ok’)
6 elif d[’c’] > 0:
7
print(’ok’)
8 elif d[’d’] > 0:
9
print(’ok’)
10 else:
11
print(’not ok’)
A. Không có lỗi
B. Có lỗi
6. Đoạn lệnh nào dưới đây sẽthực thi thành công, giảsửx và y đã được khởi tạo
từtrước?
A.
1 if x < y: if x > 10: print(’foo’)
B.
1 if x < y: print(’foo’) else: print(’bar’)
C.
1 if x < y: print(’foo’); print(’a’); print(’b’)
D.
1 if x < y: print(’foo’)
2 elif y < x: print(’bar’)
3 else: print(’baz’)
7. Đoạn lệnh sau dùng đểlàm gì:
1 a = int(input("a = "))
2 if a % 2 == 0:
3
print(a)
4 else:
5
print (0)
A. In ra giá trịcủa a
B. Nếu là sốchẵn thì in giá trịvừa nhập, ngược lại in ra 0
C. Vừa in ra giá trịcủa a vừa in ra 0
D. Nếu là sốlẽthì in giá trịvừa nhập, ngược lại in ra 0
Đáp án

<!-- page: 5 -->

1. A
2. C
3. C
4. D
5. A
6. C
6. D
7. B
Hướng dẫn lập trình Python cơ bản
Trang 47
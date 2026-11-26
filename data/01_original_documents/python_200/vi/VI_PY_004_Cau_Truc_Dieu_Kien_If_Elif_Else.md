<!-- page: 1 -->
# VI_PY_004: Cấu trúc điều kiện rẽ nhánh if - elif - else và câu lệnh lồng nhau

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Điều khiển luồng | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 42 -->
4
Câu lệnh if elif else
Với câu lệnh này, nhiều điều kiện sẽđược xem xét lần lượt trước khi phần cuối
cùng là else sẽđược hiện thực, nếu như tất cảcác điều kiện trước là sai. Cấu trúc
của câu lệnh này như sau:
1 if <Dieu_Kien_1 >:
2
<Cau_Lenh >
3 elif <Dieu_Kien_2 >:
4
<Cau_Lenh >
5 elif <Dien_Kien_3 >:
6
<Cau_Lenh >
7 else:
8
<Cau_Lenh >
Một nhầm lẫn mà người học sẽdễgặp phải khi sửdụng cấu trúc này, là từtrên
xuống, khi một điều kiện là đúng, các câu lệnh trong điều kiện đó sẽđược thực
thi và toàn bộcác điều kiện còn lại sẽkhông được xem xét nữa. Chẳng hạn điều
kiện thứnhất và thứ2 đều đúng, thì chương trình chỉthực hiện các câu lệnh trong
nhóm 1 mà thôi. Nói một cách khác, chỉđiều kiện đầu tiên đúng được thực thi
trong câu lệnh if.
Một ví dụcho câu lệnh này như sau:
1 a=200
2 b=10
3 if a<b:
4
print("a be hon b")
5 elif a==b:
6
print("a bang b")
7 else:
8

<!-- page: 2 -->

print("a lon hon b")
Chương trình 4.3: Ví dụlệnh if...elif...else
Lưu ý rằng, phần else là một phần tùy chọn, có thểcó hoặc không.
5
Câu lệnh lồng nhau
Thực ra if, if else hay thậm chí if elif else cũng chỉlà một câu lệnh. Do đó, nó có thể
xuất hiện bên trong một điều kiện của câu lệnh if, tạo ra hiện tượng các câu lệnh
điều kiện lồng nhau.
Phần trình bày này chỉmuốn nhấn mạnh lại với người đọc, là việc sửdụng cấu
trúc lồng nhau này có thểxảy ra nhầm lẫn, nếu như bạn không nắm vững nguyên
lý của lệnh if. Một chương trình ví dụvềviệc sửdụng các câu lệnh điều kiện lồng
nhau sẽnhư sau:
1 a = 2
2 b = 3
3 if a> 1:
4
if b > 4:
Trang 42
The Dariu Foundation

<!-- page: 43 -->
5
a = a + 1
6
b = b + 1
7 else:
8
a = a + 2
9
b = b + 2
10 print(a, b, sep=" - ")
Chương trình 4.4: Ví dụlệnh if lồng nhau
Nếu như không nắm vững nguyên lý của lệnh điều kiện, nhiều người sẽnhầm
rằng kết quảcuối cùng của a và b lần lượt là 4 và 5. Tuy nhiên, khi điều kiện a > 1
đã đúng, thì phần else của nó sẽkhông còn được thực hiện nữa. Bên trong phần
if đầu tiên, điều kiện b > 4 sai và không có đoạn chương trình nào được thực hiện
nữa. Cuối cùng, giá trịcủa a và b không thay đổi, vẫn là 2 và 3.
6
Bài tập
1. Nhập một sốtừbàn phím, in ra kết quảđó là sốchẵn hay sốlẻ.
1 num = float(input("Nhap mot so "))
2 if num % 2 == 0:
3
print("So chan")
4 else:

<!-- page: 3 -->

5
print("So le")
Chương trình 4.5: Đáp án gợi ý cho Bài 1
2. Nhập một sốtừbàn phím, in ra kết quảđó là sốdương, sốâm hay sốkhông (0).
1 num = float(input("Nhap mot so "))
2 if num >= 0:
3
if num == 0:
4
print("So khong")
5
else:
6
print("So duong")
7 else:
8
print("So am")
Chương trình 4.6: Đáp án gợi ý cho Bài 2
3. Viết chương trình mô phỏng việc giải phương trình bậc nhất 1 ẩn số: Cho phép
người dùng nhập sốa và b, sau đó in ra kết quảcủa phương trình.
1 print("Phuong trinh bac nhat: ax + b = 0")
2 a = int(input("a = "))
3 b = int(input("b = "))
4 if (a == 0):
5
print("Phuong trinh vo nghiem")
6 else:
7
x = -b/a
Hướng dẫn lập trình Python cơ bản
Trang 43

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

<!-- page: 4 -->

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

<!-- page: 5 -->

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

<!-- page: 6 -->

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

<!-- page: 7 -->

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

<!-- page: 48 -->
Trang 48
The Dariu Foundation
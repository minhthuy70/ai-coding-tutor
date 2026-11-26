<!-- page: 1 -->
# VI_PY_018: Cài đặt giải thuật đệ quy: Tính giai thừa và số hạng Fibonacci

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Giải thuật | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 90 -->
5
Bài tập
1. Viết hàm printMax, nhận hai giá trịđầu vào a và b. Sau đó in ra màn hình sốlớn
hơn. Nếu hai sốbằng nhau thì chỉcần in ra màn hình 1 số.
1 def printMax(a, b):
2
if a > b:
3
print(a)
4
elif a == b:
5
print(b)
6
else:
7
print(b)
8 a = int(input("Nhap so thu nhat: "))
9 b = int(input("Nhap so thu hai: "))
10 printMax(a, b)
Chương trình 9.1: Đáp án gợi ý cho Bài 1
2. Cho Dãy Fibonacci được tính dựa trên công thức sau:
f(n) = 0 nếu n = 0
f(n) = 1 nếu n = 1
f(n) = f(n-1) + f(n-2) nếu n>1
Hãy viết hàm đệquy tính giá trịcủa f(n) với n là sốđược người dùng nhập và và trả
vềgiá trịtương ứng. Ví dụ: Nếu n được nhập vào là 7 thì chương trình sẽtrảvề13.
1 def f(n):
2
if n == 0: return 0
3
elif n == 1: return 1
4
else: return f(n-1)+f(n-2)

<!-- page: 2 -->

5
6 n = int(input("Nhap n: "))
7 a = f(n)
8 print (a)
Chương trình 9.2: Đáp án gợi ý cho Bài 1
3. Viết hàm tính lũy thừa x mũ y (không được dùng toán tử**), với x, y nhập từbàn
phím và x,y > 0. Nếu x hoặc y nhỏhơn 0 thì trảvề0.
1 def power(x,y):
2
ketqua = 1
3
if x < 0 or y < 0:
4
ketqua = 0
5
else:
6
for i in range (0,y):
7
ketqua = ketqua * x
8
return ketqua
9
10 x = int(input("Nhap co so: "))
11 y = int(input("Nhap so mu: "))
12 a = power(x,y)
13 print(a)
Trang 90
The Dariu Foundation

<!-- page: 91 -->
6
Câu hỏi ôn tập
1. Chọn đáp án đúng: Phát biểu nào chính xác khi nói vềHàm trong Python?
A. Hàm có thểđược tái sửdụng trong chương trình.
B. Sửdụng hàm không có tác động tích cực gì đến các module trong chương
trình.
C. Không thểtựtạo các hàm của riêng người viết chương trình.
D. Tất cảcác đáp án trên đều đúng.
2. Từkhóa nào được sửdụng đểbắt đầu hàm?
A. Fun
B. Define
C. Def
D. Function
3. Output của chương trình dưới đây là gì?

<!-- page: 3 -->

1 def sayHello ():
2
print(’Hello World!’)
3 sayHello ()
4 sayHello ()
A.
Hello World!
Hello World!
B.
‘Hello World!’
‘Hello World!’
C.
Hello
Hello
D. Không có đáp án đúng
4. Output của chương trình dưới đây là gì?
1 def printMax(a, b):
2
if a > b:
3
print(a, ’is maximum ’)
4
elif a == b:
5
print(a, ’is equal to’, b)
6
else:
7
print(b, ’is maximum ’)
8 printMax (3, 4)
A. 3
B. 4
C. 4 is maximum
D. Không có đáp án đúng
Hướng dẫn lập trình Python cơ bản
Trang 91

<!-- page: 92 -->
5. Output của chương trình dưới đây là gì?
1 x = 50
2
def func(x):
3
print(’Gia tri cua x la’, x)
4

<!-- page: 4 -->

x = 2
5
print(’Gia tri cua x duoc thay doi thanh ’, x)
6 func(x)
7 print(’Gia tri hien tai cua x la’, x)
A. Gia tri hien tai cua x la 50
B. Gia tri hien tai cua x la 100
C. Gia tri hien tai cua x la 2
D. Không có đáp án đúng
6. Output của chương trình dưới đây là gì?
1 x = 50
2
def func ():
3
global x
4
print(’Gia tri cua x la’, x)
5
x = 2
6
print(’Gia tri cua x duoc thay doi thanh ’, x)
7 func ()
8 print(’Gia tri hien tai cua x la’, x)
A.
Gia tri cua x la 50
Gia tri cua x duoc thay doi thanh 2
Gia tri hien tai cua x la 50
B.
Gia tri cua x la 50
Gia tri cua x duoc thay doi thanh 2
Gia tri hien tai cua x la 2
C.
Gia tri cua x la 50
Gia tri cua x duoc thay doi thanhh 50
Gia tri hien tai cua x la 50
D. Không có đáp án đúng
7. Output của chương trình dưới đây là gì?
1 def maximum(x, y):
2
if x > y:
3
return x
4
elif x == y:
5

<!-- page: 5 -->

return ’Cac so bang nhau ’
6
else:
7
return y
8 print(maximum (2, 3))
Trang 92
The Dariu Foundation

<!-- page: 93 -->
A. 2
B. 3
C. Cac so bang nhau
D. Không có đáp án đúng
8. Đâu là kết quảcủa chương trình dưới đây?
1 def outerFunction ():
2
global a
3
a = 20
4
def innerFunction ():
5
global a
6
a = 30
7
print(’a =’, a)
8 a = 10
9 outerFunction ()
10 print(’a =’, a)
A. a = 10 a = 30
B. a = 10
C. a = 20
D. a = 30
9. Output của chương trình dưới đây là gì?
1 def cube(x):
2
return x * x * x
3 x = cube (3)
4 print x
A. 9
B. 3
C. 27
D. 30

<!-- page: 6 -->

10. Output của chương trình dưới đây là gì?
1 def C2F(c):
2
return c * 9/5 + 32
3 print C2F (100)
4 print C2F (0)
A.
212
32
B.
314
24
C.
567
Hướng dẫn lập trình Python cơ bản
Trang 93
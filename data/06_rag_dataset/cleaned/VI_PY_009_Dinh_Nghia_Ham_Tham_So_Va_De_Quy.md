# VI_PY_009: Định nghĩa hàm người dùng, truyền tham số và kỹ thuật đệ quy

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Hàm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

Ởví dụtrên hàmsum() sẽtrảvềgiá trịtổng của hai tham sốa và b. Chúng ta có thể
sửdụng giá trịtrảvềnày đểhiển thịmột thông báo hoặc gán cho một biến khác...
1 number_1 = 3
2 number_2 = 4
3
4 def sum(a, b):
5
return a + b
6
7 total = sum(number_1 , number_2)
8 print("Tong cua %s va %s la %s" %( number_1 , number_2 , total
))
Giá trịtrảvềkhi gọi hàm sum() ởtrên được gán vào biến total. Và như vậy khi chạy
đoạn code trên khi chạy sẽhiển thịkết quả:Tong cua 3 va 4 la 7.
Các hàm không sửdụng return hoặc sửdụng return (không có giá trịnào tiếp theo
sau từkhoá) sẽtrảvềgiá trịlà None:
1 def hello_1 ():
2
print("Hello 1!")
3
4 def hello_2 ():
5
print("Hello 2!")
6
return
7
8 returnValue = hello_1 ()
9 print(returnValue) # Hien thi: None
10 print(type(returnValue)) # Hien thi: <type ’NoneType ’>
11
12 return_value = hello_2 ()
13 print(returnValue) # Hien thi: None
14 print(type(returnValue)) # Hien thi: <type ’NoneType ’>
Một lưu ý khác khi sửdụng return trong hàm đó là một khi hàm đã return (trảvề

giá trị) thì Python sẽchấm dừng quá trình chạy hàm. Ví dụ:
1 def hello ():
2
print("Hello!")
3
return
4
print("Nice to meet you!")
5
6 hello () # Hien thi: Hello!
Trong đoạn code trên khi gọi hàm hello() thì chỉcó câu lệnh print("Hello!") đầu
tiên được chạy.
3.3
Câu lệnh pass
Hàm tựđịnh nghĩa không thểbịbỏtrống (tức là không thểkhông có hàm), tuy
nhiên vì một sốlý do nào đó mà hàm tựđịnh nghĩa không có nội dung. Thì câu
lệnh pass sẽgiúp cho việc định nghĩa hàm không bịlỗi. Ví dụ:

The Dariu Foundation

1 def myfunction ():
2
pass
4
Viết hàm đểtính giai thừa
Dựa vào những gì được biết vềhàm, thì chúng ta sẽtiến hành một ví dụvềcách
định nghĩa hàm. Ví dụ: Hàm tính giai thừa. Và chúng ta sẽthực hiện việc đĩnh
nghĩa hàm tính giai thừa theo 2 cách là vòng lặp for và đệquy.
Trong toán học, giai thừa là một toán tửmột ngôi trên tập hợp các sốtựnhiên. Cho
n là một sốtựnhiên dương,"n giai thừa", ký hiệu n! là tích của n sốtựnhiên dương
đầu tiên.
n! = 1x2x3x...x n
Ví dụ: 4! = 1.2.3.4 = 24
8! = 1.2.3.....7.8 = 40320
Đặc biệt, với n = 0, người ta quy ước 0! = 1.
4.1
Viết hàm sửdụng vòng lặp for
1 def tinhgiaithua(n):
2
giai_thua = 1;
3
if (n == 0 or n == 1):
4
return giai_thua;

5
else:
6
for i in range(2, n + 1):
7
giai_thua = giai_thua * i;
8
return giai_thua;
9
10 n=10
11 print("Giai thua cua", n, "la", tinhgiaithua(n));
Kết quảlà: Giai thua cua 10 la 3628800
4.2
Viết hàm sửdụng đệquy
1 def tinhgiaithua(n):
2
if n == 0:
3
return 1
4
return n * tinhgiaithua(n - 1)
5
6 n=9
7 print("Giai thua cua", n, "la", tinhgiaithua(n));
Kết quảlà: Giai thua cua 9 la 362880
Hướng dẫn lập trình Python cơ bản

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

The Dariu Foundation

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

5. Output của chương trình dưới đây là gì?
1 x = 50
2
def func(x):
3
print(’Gia tri cua x la’, x)
4
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
return ’Cac so bang nhau ’
6
else:
7
return y
8 print(maximum (2, 3))

The Dariu Foundation

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

98
D. Không có đáp án đúng
Đáp án
1. A
2. C
3. A
4. C
5. A
6. B

7. B
8. C
9. C
10. A

The Dariu Foundation
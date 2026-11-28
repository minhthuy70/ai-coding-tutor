## CẤU TRÚC RẼ NHÁNH

## NỘI DUNG

**/01** If và một số ví dụ về if

**/02** Else

**/03** Elif

**/04** Shorthand if và toán tử ba ngôi

**/05** If lồng nhau

## 1. If và một số ví dụ về if:

If được sử dụng khi bạn cần kiểm tra điều kiện nào đó trước khi thực hiện một hoặc nhiều câu lệnh. Các câu lệnh bên trong if được thụt lề so với if.

## Cú pháp

if condition: #code

00 EXAMPLE

00

if 100 > 50: print ('hello 28tech !')

OUTPUT hello 28tech

## 1. If và một số ví dụ về if:

Nếu condition có giá trị True thì code bên trong if được thực hiện, ngược lại nếu condition mang giá trị False thì code bên trong if sẽ được bỏ qua.

condition ở đây thường là các phép so sánh để kiểm tra điều kiện hoặc cũng có thể là kết hợp của nhiều phép so sánh.

Khi viết condition kết hợp các phép so sánh thì một là bạn dùng toàn toán tử and, 2 là dùng toán tử or, nếu có lẫn cả 2 toán tử này thì cần xem xét lại.

## 1. If và một số ví dụ về if:

00 EXAMPLE

**Kiểm tra số chẵn, lẻ**

$$
n = 2 0 0
$$

$$
m = 2 0 1
$$

**OUTPUT**

200 is even 201 is odd

00 EXAMPLE

## Kiểm tra số nằm trong đoạn [a, b]

a, b = 50, 100

$$
m = 7 \theta
$$

if (m >= a) and (m <= b):
    print('YES')

**OUTPUT** YES

## 2. Else:

Else được sử dụng trong trường hợp condition bên trong if là sai.

## Cú pháp

if condition : #code if condition is True else:

#code if condition is False

00 EXAMPLE

0

n = 100 if n % 2 == 0: print('Even') else: print('Odd')

**OUTPUT** Even

## 3. Elif:

Từ khóa elif (else if) trong python được sử dụng bên dưới if để kiểm tra thêm điều kiện bổ sung nếu điều kiện bên bên trên sai. Các điều kiện ở bên trong if và elif nếu đúng thì khối code tương ứng sẽ được thực thi, nếu không có điều kiện nào đúng thì khối lệnh bên trong else được thực thi.

## Cú pháp

if condition1: #code1 elif condition2: #code2

elif conditionN: #codeN else: #codeElse

## 00 EXAMPLE

0

a, b = 100, 200 if a < b : print(a, 'less than', b) elif a == b: print(a, 'equal to', b) else: print(a, 'greater than', b)

**OUTPUT**

100 less than 200

## 4. Shorthand if và toán tử ba ngôi: Shorthand if:

Shorthand if: Bạn có thể sử dụng câu lệnh if trên 1 dòng

00 EXAMPLE

00

a, b = 100, 200 if a < b : print(a, 'less than', b)

**OUTPUT**

100 less than 200

## 4. Shorthand if và toán tử ba ngôi: Shorthand if:

Nếu trong if có nhiều câu lệnh, bạn có thể đặt dấu chấm phẩy giữa các câu lệnh

00 EXAMPLE

00

a, b = 100, 200

if a < b : print(a, 'less than', b); print('28tech'); print('abcd')

**OUTPUT**

100 less than 200 28tech abcd

True branch

## 4. Shorthand if và toán tử ba ngôi: Toán tử ba ngôi:

False branch

00 EXAMPLE

**OUTPUT**

28tech

## 5. If lồng nhau:

Khi điều kiện trong if quá phức tạp, bạn có thể sử dụng if lồng nhau (nested if) để kiểm tra từng điều kiện một.

Kiểm tra N xem có phải là số nằm trong đoạn [20, 30] và chia hết cho ít nhất một trong ba số 2, 3, 5. Nếu đúng in ra YES, ngược lại in ra NO

## Cách 1:

$$
n = 2 7
$$

if n >= 20 and n <= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):

print('YES')

else:

print('NO')

**OUTPUT** YES

## 5. If lồng nhau:

Kiểm tra N xem có phải là số nằm trong đoạn [20, 30] và chia hết cho ít nhất một trong ba số 2, 3, 5. Nếu đúng in ra YES, ngược lại in ra NO

## Cách 2: Nested if

$$
n = 2 7
$$

if n >= 20 and n <= 30: if n >= 20 and n <= 30: n  or n % 3 == 0 or n % 5 == 0: if % 2 == 0

print('YES') else: print('NO') else: print('NO')

**OUTPUT** YES
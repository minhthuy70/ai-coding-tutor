## MỘT SỐ HÀM TOÁN HỌC PHỔ BIẾN

## <1>

Để sử dụng các hàm toán học trong module ta import modulo math vào chương trình. Để nắm được các hàm, giá trị mà module này cung cấp các bạn có thể in ra bằng câu lệnh print(help(math)).

import math print (help(math))

## 1. Hàm sqrt:

**Hàm sqrt** tính căn bậc 2 của một số và trả về số ở dạng float.

00 EXAMPLE

00

import math

can1 = math.sqrt(100)

can2 = math.sqrt(13) print(can1,can2)

**OUTPUT**

10.0 3.605551275463989

## 2. Hàm isqrt:

**Hàm isqrt** tính căn bậc 2 của một số nhưng làm tròn xuống số int gần nhất.

00

import math

can1 = math.isqrt(100)

can2 = math.isqrt(13)

print(can1,can2)

**OUTPUT**

10 3

## 3. Hàm pow:

**Hàm pow(a,b)** trả về a lũy thừa b ở dạng float.

00

import math res = math.pow(2,10) print(res)

**OUTPUT**

1024.0

## 4. Hàm ceil và floor:

**Hàm ceil(a)** trả về số nguyên gần a nhất khi làm tròn lên. **Hàm floor(a)** trả về số nguyên gần a nhất khi làm tròn xuống.

import math print(math.ceil(3.6), math.ceil(2.3)) print(math.floor(3.6), math.floor(2.3))

**OUTPUT**

4 3

## 5. Hàm fabs và abs:

**Hàm fabs** trả về trị tuyệt đối của một số ở dạng số thực, các bạn cũng có thể dùng built-in function là abs.

import math print(math.fabs(-50)) print(abs(-50))

**OUTPUT** 50.0 50

## 6. Hàm gcd:

**Hàm gcd(a,b)** trả về ước chung lớn nhất của a và b.

00

import math print(math.gcd(50,30)) print(math.gcd(-50,30))

**OUTPUT** 10 10

## 7. Hàm factorial:

**Hàm factorial(n)** trả về giai thừa của n.

import math print(math.factorial(10))

**OUTPUT**

3628800
<!-- page: 1 -->

## LIST COMPREHENSION

## 二<1>

<!-- page: 2 -->

Comprehension là một cách nhanh chóng để có thể tạo một cấu trúc dữ liệu từ iterable. Nó có thể kết hợp với điều kiện và vòng lặp để rút gọn cú pháp. List comprehension sẽ giúp code của bạn Pythonic hơn.

<!-- page: 3 -->

## 1. Cú pháp và các ví dụ cơ bản:

## CÚ PHÁP

## [Expression for var in iterable]

hàm lambda.**Expression:** Biểu thức được thực hiện mỗi khi vòng lặp thực thi.

**Var:** Một biến là một item trong iterable.

**Iterable:** Collections chứa các object (list, tuple, str...)

<!-- page: 4 -->

## 1. Cú pháp và các ví dụ cơ bản:

**VÍ DỤ**

00 EXAMPLE 00

## ách đơn giản để định nghĩa một hàCopy từ một list đã có:

hàa = ["python", "apple", "28tech"] b = [x for x in a]

print(b)

**OUTPUT**

['python', 'apple', '28tech']

00 EXAMPLE 00

**Tạo một list giá trị bình phương** bda thường được gọi dưới cái tên toán tử l**của các phần tử của một list đã có:**

a = [1, 2, 3, 4]

b = [x \*\* 2 for x in a]

print(b)

**OUTPUT** [1, 4, 9, 16]

<!-- page: 5 -->

## 1. Cú pháp và các ví dụ cơ bản:

00 EXAMPLE

ch đơn giản để định nghĩa một hTạo một list từ range: a = [x \*\* 3 for x in range(5)] print(a)

**OUTPUT** [0, 1, 8, 27, 64]

**VÍ DỤ**

EXAMPLE

ường được gọi dưới cái tên **Tạo một list từ str:**

$$
s = " 2 8 \text {tech}"
$$

a = [x for x in s]

print(a)

**OUTPUT**

['2', '8', 't', 'e', 'c', 'h']

<!-- page: 6 -->

## 1. Cú pháp và các ví dụ cơ bản:

EXAMPLE

ể**Tạo một list trị tuyệt đối của các phần tử của một list đã có:**

$$
a = [ 1, 2, - 3, 4, - 5, - 1 0 ]
$$

b = [abs(x) for x in a]

print(b)

**OUTPUT**

[1, 2, 3, 4, 5, 10]

**VÍ DỤ**

00 EXAMPLE

**Kết hợp hàm với list comprehension:**

def digitSum(n):

$$
\text {sum} = \theta
$$

while n != 0:

$$
\text {sum} + = n \% 10
$$

**OUTPUT**

$$
n / / = 1 0
$$

[6, 4, 2, 8, 6]

return sum

$a = [123, 31, 20, 503, 114]$

b = [digitSum(x) for x in a]

print(b)

<!-- page: 7 -->

## 2. List comp với câu lệnh if:

![](images/page_6_image_4.jpg)

Khi sử dụng list comprehension bạn có thể sử dụng mệnh đề if để lọc dữ liệu phù hợp.

## CÚ PHÁP

[Expression for var in iterable if\_clause]

## 00 EXAMPLE 00

## Lọc ra các số không âm

$$
\begin{array}{l} \text {a = [1, 2, 3, -5, 3, -4, 0]} \\ \text {b = [x for x in a if x >= 0]} \\ \text {print(b)} \end{array}
$$

EXAMPLE

## Lọc các số chẵn từ 0 tới n:

$$
n = 1 0
$$

[1, 2, 3, 3, 0]

print(a)

**OUTPUT**

[0, 2, 4, 6, 8]

<!-- page: 8 -->

## 3. Nested List comprehension:

![](images/page_7_image_4.jpg)

Biểu thức bên trong list comp có thể là một list comp khác.

[expression for var in iterable]

[expression for var in iterable for var in iterable]

![](images/page_7_image_8.jpg)

Đưa mọi phần tử trong nested list thành một list (flatten): a = [[1, 2, 3], [4, 5], [6, 7, 8]] b = [x for small\_list in a for x in small\_list] print(b) **OUTPUT** [1, 2, 3, 4, 5, 6, 7, 8]

<!-- page: 9 -->

## 4. List comprehension với map + lambda:

![](images/page_8_image_4.jpg)

## 00 EXAMPLE

Khi sử dụng các hàm có sẵn thì sử dụng map sẽ nhanh gọn hơn so với listcomp.

00

$$
\begin{array}{l} \text {s = "28tech"} \\ \text {a = list(map(ord, s))} \\ \text {print(a)} \\ \text {\#Listcomp} \\ \text {b = [ord(x) for x in s]} \\ \text {print(b)} \end{array}
$$

**OUTPUT**

[50, 56, 116, 101, 99, 104] [50, 56, 116, 101, 99, 104]

![](images/page_8_image_11.jpg)

Tuy nhiên khi apply một hàm khác các hàm có sẵn thì sự kết hợp của listcomp với lambda sẽ ngắn gọn hơn so với sự kết hợp của lambda vs map.

## 00 EXAMPLE

hon.

ambda thường đưa = range(5)

c = list(map(lambda x : x \*\* 2, a)) print(c)

**OUTPUT**

[0, 1, 4, 9, 16] [0, 1, 4, 9, 16]

<!-- page: 10 -->

## 5. List comprehension với filter:

![](images/page_9_image_4.jpg)

Lọc ra những số chẵn bằng listcomp và filter kết hợp vs lambda.

## 00 EXAMPLE

00

a = range(10) m c c#listcomp even = [x for x in a if x % 2 == 0] print(even) #map c = list(filter(lambda x : x % 2 == 0, a)) print(c)

**OUTPUT**

[0, 2, 4, 6, 8] [0, 2, 4, 6, 8]

![](images/page_9_image_11.jpg)

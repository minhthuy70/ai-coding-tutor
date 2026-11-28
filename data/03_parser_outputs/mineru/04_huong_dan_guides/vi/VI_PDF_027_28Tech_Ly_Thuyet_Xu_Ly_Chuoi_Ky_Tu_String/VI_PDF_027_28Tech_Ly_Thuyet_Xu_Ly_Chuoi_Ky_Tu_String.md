<!-- page: 1 -->

## STRING

## 二<1>

<!-- page: 2 -->

Xâu kí tự là là chuỗi các kí tự được đặt giữa dấu nháy đơn hoặc nháy kép. Xâu trong Python được hỗ trợ một tập các công cụ xử lý cực kì mạnh mẽ.

<!-- page: 3 -->

## 1. Tạo string:

![](images/page_2_image_4.jpg)

Để tạo string ta đặt nội dung của xâu giữa dấu nháy đơn hoặc dấu nháy kép. Xâu có thể có hoặc không có kí tự.

## 00 EXAMPLE

00

s = '28tech' #single quotes là một cách đơn giản đ định nghĩa một ht = "python" #double quotes #Multiline string

$$
u = ""
$$

cuoc song tuoi dep """

**OUTPUT**

28tech python

print(s, t) print(u)

cuoc song tuoi dep

## 2. str() constructor:

![](images/page_2_image_16.jpg)

Bạn có thể chuyển đổi hầu hết các đối tượng trong Python sang xâu kí tự bằng hàm khởi tạo str().

## 00 EXAMPLE

00

s = str(100)

ambda thường được gọit = str(100.20)

u = str(10 + 28j) print(type(s), type(t), type(u))

**OUTPUT**

&lt;class 'str'&gt; &lt;class 'str'&gt; &lt;class 'str'&gt;

<!-- page: 4 -->

## 3. Truy cập kí tự thông qua chỉ số và duyệt xâu:

![](images/page_3_image_4.jpg)

Để truy cập vào các kí tự trong string, ta dùng chỉ số bắt đầu tử 0, ngoài ra Python còn hỗ trợ chỉ số âm (negative index).

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| một cácSh đơn g | iản để 2 định ng | hĩa một8 hàm tr | ong PytThon. La | mbda tEhường đ | ược gọCi dưới c | ái tên tHoán tử l |
| Neg index | -6 | -5 | hàm l-a4mbda. | -3 | -2 | -1 |

00 EXAMPLE

00

s = "28TECH" print(s[1]) print(s[-2])

**OUTPUT**

8 C

<!-- page: 5 -->

## 3. Truy cập kí tự thông qua chỉ số và duyệt xâu:

**Bạn có thể sử dụng string slicing tương tự như list**

00 là một

00

s = "28TECH" print(s[1:4]) print(s[2:]) print(s[::-1])

**OUTPUT**

8TE TECH HCET82

**Duyệt xâu**

1日EXAMPLE

00

s = "28tech dsa" for x in s : g được gọi dưới cái tên toán tprint(x, end = ' ') print() for i in range(len(s)): print(s[i], end = ' '

**OUTPUT**

2 8 t e c h d s a 2 8 t e c h d s a

<!-- page: 6 -->

## 4. String is immutable:

![](images/page_5_image_4.jpg)

Bạn có thể truy cập các kí tự trong str thông qua chỉ số nhưng bạn không thể thay đổi được các kí tự đó bằng cách gán nó thành các kí tự hoặc xâu khác.

00 EXAMPLE

là m

$$
s = " 2 8 \text {TECH}"
$$

$$
s [ \emptyset ] = ""
$$

$$
\text {print} (s)
$$

**OUTPUT**

TypeError: 'str' object does not support item assignment

## 5. Nối xâu:

![](images/page_5_image_14.jpg)

Trong Python để nối 2 xâu bạn có thể sử dụng toán tử +, để nhân bản xâu bạn có thể dùng toán tử \*.

00 EXAMPLE

00

$$
s = " 2 8 \text {tech}"
$$

$$
t = \text {``python''}
$$

$$
s = s + \text {""} + t
$$

print(s)

$$
a = " a b"
$$

**OUTPUT**

$$
b = a * 3
$$

print(b)

28tech python ababab

<!-- page: 7 -->

## 6. Hàm replace:

![](images/page_6_image_4.jpg)

**Hàm replace()** được sử dụng để thay thế 1 xâu cũ bằng một xâu mới.

![](images/page_6_image_6.jpg)

**Chú ý:** Các hàm xử lý của str không thay đổi chính nó mà trả về xâu tương ứng.

## à m EXAMPLE

s = "28tech python C++" t = s.replace("python", "java") print(s) OUTPUT print(t)

28tech python C++ 28tech java C++

![](images/page_6_image_11.jpg)

<!-- page: 8 -->

## 7. Hàm split() và join():

![](images/page_7_image_4.jpg)

**split():** Tách các từ trong xâu, mặc định nếu hàm này không có tham số sẽ tách theo dấu cách.

## 00 EXAMPLE

00

$$
s = " 2 8 \text {tech}
$$

python

$$
C + +
$$

$$
a = s. \text {split} ()
$$

print(a)

$$
t = " 2 8 \text {tech, python, C++}"
$$

$$
b = t. \text {split}",")
$$

print(b)

**OUTPUT**

['28tech', 'python', 'C++']

['28tech', 'python', 'C++']

![](images/page_7_image_19.jpg)

**join():** Kết hợp các từ rời rạc thành 1 xâu được phân cách bởi kí tự cho trước

## 00 EXAMPLE

0

s = ["28tech", "python", "C++"]

$$
t = \text {','.join(s)}
$$

.print(t)

$$
\mathrm{u} = ^ {\prime} \#\#\'. \text {join(s)}
$$

print(u)

**OUTPUT**

28tech,python,C++ 28tech##python##C++

<!-- page: 9 -->

## 8. Các hàm case conversion:

• **upper():** Chuyển sang in hoa.

• **lower():** Chuyển sang in thường.

• **capitalize():** Viết hoa chữ cái đầu của xâu.

bda là một cách đơn giản để định nghĩa một hàm trong Pyt**swapcase():** Chuyển chữ hoa thành thường và ngược lại.

**title():** Viết hoa chữ cái đầu của từng từ,các kí tự còn lại viết thường

## OUTPUT

28TECH JAVA PYTHON 28tech java python i cái tên toán tử lamb28tEch JavA pYtHON 28Tech Java Python 28tech java python

<!-- page: 10 -->

## 9. Kiểm tra xâu con:

![](images/page_9_image_4.jpg)

Để kiểm tra xâu con có thể sử dụng **toán tử in** hoặc **hàm find**, hàm find sẽ trả về chỉ số nhỏ nhất của xâu con nếu nó tồn tại trong xâu lớn, trả về -1 nếu không tìm thấy xâu con.

![](images/page_9_image_6.jpg)

s = "28tech dsa 28tech" if "28tech" in s: print('FOUND') print(s.find("28tech")) print(s.find("C++")) **OUTPUT** FOUND 0 -1

![](images/page_9_image_8.jpg)

<!-- page: 11 -->

## 10. String format :

![](images/page_10_image_4.jpg)

Trong Python có 3 cách nhúng biến vào trong xâu kí tự.

**-% string formatting : %s : xâu kí tự, %d : số nguyên, %f : Số float**

00 giản để

hàm lambda.s = '%s is %d years old' % ('CR7', 37)

t = 'Pi = %.2f' % (3.14159)

print(s)

print(t)

**OUTPUT**

CR7 is 37 years old Pi = 3.14

<!-- page: 12 -->

## 10. String format:

![](images/page_11_image_4.jpg)

Trong Python có 3 cách nhúng biến vào trong xâu kí tự.

**-str.format()**

00 bda là

s = '{0} is {1} years old !'.format('CR7', 37) print(s)

**OUTPUT**

CR7 is 37 years old

**-f-String**

0 EXAMPLE

$$
\text {name} = \text {"CR7"}
$$

$$
\text{age} = 37
$$

s = f'{name} is {age} years old !' print(s) **OUTPUT**

CR7 is 37 years old

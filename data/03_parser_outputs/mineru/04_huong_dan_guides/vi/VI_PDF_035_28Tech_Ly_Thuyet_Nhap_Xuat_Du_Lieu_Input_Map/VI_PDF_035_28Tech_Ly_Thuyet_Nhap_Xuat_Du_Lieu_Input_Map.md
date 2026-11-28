<!-- page: 1 -->

## NHẬP INPUT

## <1>

<!-- page: 2 -->

## Nhập dữ liệu với hàm input:

**Cú pháp:** input(prompt)

![](images/page_1_image_5.jpg)

**Giá trị trả về:** input() trả về xâu kí tự ở kiểu str, các bạn cần chú ý ép kiểu sang dữ liệu tương ứng của biến trong đề bài.

## 00 EXAMPLE

00

n = input('Nhap so :') print(type(n)) print(n)

**INPUT**

**OUTPUT**

20

&lt;class 'str'&gt; 20

00

EXAMPLE

00

Ép sang kiểu là số nguyên hoặc thực bằng hàm int(), float() n = int(input('Nhap so :')) print(type(n)) print(n)

**INPUT** 20

**OUTPUT** &lt;class 'int'&gt; 20

<!-- page: 3 -->

## Nhập dữ liệu với hàm input:

## Nhập nhiều số

**Bước 1:** Nhập cả dòng bằng hàm input.

**Bước 2:** Dùng hàm split để tách các số trong xâu input ra.

**Bước 3:** Sử dụng map để ép các xâu được tách ra trong input sang số int hoặc float tùy theo đầu bài.

## 00 EXAMPLE

Nhập 2 số trên một dòng a, b = map(int, input().split()) print(a, b)

**INPUT**

**OUTPUT**

00 EXAMPLE

00 Nhập 4 số trên một dòng a, b, c, d = map(int, input().split()) print(a, b, c, d)

10 20

10 20

**INPUT**

**OUTPUT**

10 20 30 40

10 20 30 40

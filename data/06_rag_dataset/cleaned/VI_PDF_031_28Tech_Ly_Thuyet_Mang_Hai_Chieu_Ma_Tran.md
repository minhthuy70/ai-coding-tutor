## MẢNG HAI CHIỀU

## <1>

Trong Python để sử dụng mảng 2 hay nhiều chiều ta sử dụng nested list. Ở phần mảng 2 chiều này các bạn sẽ học về các bài toán cơ bản trên mảng 2 chiều như bài toán về hàng, cột, các phép toán trên ma trận, ma trận xoáy ốc…

Để giải quyết các bài toán liên quan tới ma trận các bạn cũng sử dụng nested list trong Python.

## 1. Tạo mảng 2 chiều và nhập xuất:

Để khai báo mảng 2 chiều, ta cần chỉ rõ số lượng hàng, số lượng cột của ma trận.

## Khai báo mảng 2 chiều có n hàng và m cột

```python
n, m = 2, 3
a = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()
```

## 2. Truy cập vào các phần tử trong mảng 2 chiều:

Để truy cập vào phần tử trong mảng, các bạn dùng chỉ số hàng và chỉ số cột. Chỉ số hàng và cột của mảng 2 chiều được đánh số từ 0 tương tự như mảng 1 chiều.

$$
\begin{array}{c c c c} & 0 & 1 & 2 \\ 0 & 1 & 2 & 3 \\ \hline 1 & 4 & 5 & 6 \\ 2 & 7 & 8 & 9 \end{array}
$$

$$
\begin{array}{l} \text {a[0][2] = 3} \\ \text {a[2][1] = 8} \end{array}
$$

**3. Các bài toán trên mảng 2 chiều:**

**a. Tìm phần tử lớn nhất, nhỏ nhất trong mảng:**

## 00 EXAMPLE

a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]] min\_val, max\_val = 10\*\*18, -10\*\*18 for row in a: min\_val = min(min\_val, min(row)) max\_val = max(max\_val, max(row)) print(min\_val, max\_val)

**OUTPUT** 0 5

**3. Các bài toán trên mảng 2 chiều: b. Flatten mảng 2 chiều thành mảng 1 chiều:**

## 00 EXAMPLE

a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]] b = [x for small\_list in a for x in small\_list] print(min(b)) print(max(b)) OUTPUT print(b) 05 [1, 2, 5, 3, 1, 0, 4, 1, 5]

**3. Các bài toán trên mảng 2 chiều:**

**c. Tính tổng từng hàng của ma trận (mảng 2 chiều):**

a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]] sum\_row = [sum(row) for row in a] print(sum\_row) **OUTPUT** 8 4 10

## 4. Các phép toán trên ma trận:

## a. Tạo ma trận chuyển vị:

Ma trận chuyển vị của ma trận a cỡ nxm là ma trận b có cỡ mxn, trong đó các hàng của ma trận a trở thành các cột của ma trận b.

```python
a = [[1, 2, 5],
[3, 1, 0],
[4, 1, 5]]
a_t = [[row[i] for row in a] for i in range(len(a))]
print(a_t)
OUTPUT
[[1, 3, 4],
[2, 1, 1],
[5, 0, 5]]
```

## 4. Các phép toán trên ma trận:

**b. Cộng trử hai ma trận:**

Trong đại số tuyến tính, ma trận tương tự như một mảng 2 chiều gồm n hàng và m cột. Để 2 ma trận có thể cộng hoặc trừ cho nhau thì chúng phải có cùng số hàng và số cột.

$$
\begin{array}{c c c} \hline 1 & 2 & 0 \\ \hline 0 & 4 & 1 \\ \hline \end{array} + \begin{array}{c c c} \hline 1 & 4 & 8 \\ \hline 9 & 2 & 3 \\ \hline \end{array} = \begin{array}{c c c} \hline 2 & 6 & 8 \\ \hline 9 & 6 & 4 \\ \hline \end{array}
$$

$$
\begin{array}{c c c} \hline 1 & 2 & 0 \\ \hline 0 & 4 & 1 \\ \hline \end{array} - \begin{array}{c c c} \hline 1 & 4 & 8 \\ \hline 9 & 2 & 3 \\ \hline \end{array} = \begin{array}{c c c} \hline 0 & - 2 & - 8 \\ \hline - 9 & 2 & - 2 \\ \hline \end{array}
$$

## 4. Các phép toán trên ma trận:

**b. Cộng trừ hai ma trận:**

EXAMPLE

## Cộng 2 ma trận cùng cỡ n hàng m cột

n, m = 3, 3 a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]] b = [[0, 1, 2], [1, 1, 1], [0, 1, 0]] c = [[0 for \_ in range(m)] for \_ in range(n)] for i in range(n): for j in range(m): c[i][j] = a[i][j] + b[i][j] print(c) **OUTPUT** [[1, 3, 7], [4, 2, 1], [4, 2, 5]]

## Trừ 2 ma trận cùng cỡ n hàng m cột

一品EXAMPLE

00

n, m = 3, 3 a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]] b = [[0, 1, 2], [1, 1, 1], [0, 1, 0]] c = [[0 for \_ in range(m)] for \_ in range(n)] for i in range(n): for j in range(m): c[i][j] = a[i][j] - b[i][j] print(c) **OUTPUT** [[1, 1, 3], [2, 0, -1], [4, 0, 5]]

## 4. Các phép toán trên ma trận:

## c. Nhân hai ma trận:

Giả sử có 2 ma trận a cỡ nxm, ma trận b cỡ pxq, để ma trận a có thể nhân với ma trận b thì số cột của ma trận a, tức là m phải bằng số hàng của ma trận b, tức là p.

## a[n][m] x b[p][q] = c[n][q]

Khi đó m = p thì ma trận tích của a với b sẽ là ma trận c có cỡ nxq. Phần tử ở chỉ số (i, j) của ma trận tích c được tính bằng cách nhân từng cặp phần tử ở hàng i của ma trận a với các phần tử ở cột j của ma trận b.

## 4. Các phép toán trên ma trận:

## c. Nhân hai ma trận:

00 EXAMPLE

## Chương trình mẫu

n, m, p = map(int, input().split()) a, b = [0] \* n, [0] \* m for i in range(n): a[i] = list(map(int, input().split())) for i in range(m): b[i] = list(map(int, input().split())) c = [[0 for \_ in range(n)] for \_ in range(p)] for i in range(n): for j in range(p): for k in range(m): c[i][j] += a[i][k] \* b[k][j] print(c)

## 5. Kỹ thuật duyệt các ô liền kề:

| i-1, j-1 | i-1, j | i-1, j+1 |
| --- | --- | --- |
| i, j-1 | i, j | i, j+1 |
| i+1, j-1 | i+1, j | i+1, j+1 |

## 5. Kỹ thuật duyệt các ô liền kề:

EXAMPLE

**Duyệt 4 ô chung cạnh với ô (i,j)**

$$
a =
$$

$$
\begin{array}{l} \left[ \begin{array}{c c c} 1, & 2, & 3 \end{array} \right], \\ \left[ \begin{array}{c c c} 4, & 5, & 6 \end{array} \right], \\ \left[ \begin{array}{c c c} 7, & 8, & 9 \end{array} \right] \end{array}
$$

**OUTPUT** 2 4 6 8

path = [[-1, 0], [0, -1], [0, 1], [1, 0]] i, j = 1, 1 # 5 for x in path: i1, j1 = i + x[0], j + x[1] print(a[i1][j1], end = ' ')

| 1 | 2 | 3 |
| --- | --- | --- |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

## 5. Kỹ thuật duyệt các ô liền kề:

00 EXAMPLE

## Duyệt 8 ô chung đỉnh với ô (i,j)

$$
\begin{array}{r l} \text {a} & = [ \\ & [ 1, 2, 3 ], \\ & [ 4, 5, 6 ], \\ & [ 7, 8, 9 ] \end{array}
$$

| 1 | 2 | 3 |
| --- | --- | --- |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

path = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]i, j = 1, 1 # 5

**OUTPUT** 1 2 3 4 6 7 8 9

## 5. Kỹ thuật duyệt các ô liền kề:

## Duyệt 8 ô xung quanh nước đi của quân mã

$$
\begin{array}{l} \left[ 1, 2, 3, 4, 1 \right], \\ \left[ 5, 6, 7, 8, 0 \right], \\ \left[ 9, 3, 2, 6, 0 \right], \\ \left[ 1, 2, 1, 4, 4 \right], \\ \left[ 1, 2, 3, 5, 3 \right] \end{array}
$$

| 1 | 2 | 3 | 4 | 1 |
| --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 0 |
| 9 | 3 | 2 | 6 | 0 |
| 1 | 2 | 1 | 4 | 4 |
| 1 | 2 | 3 | 5 | 3 |

path = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]] i, j = 2, 2 for x in path: OUTPUT i1, j1 = i + x[0], j + x[1] print(a[i1][j1], end = ' ') 2 4 5 0 1 4 2 5
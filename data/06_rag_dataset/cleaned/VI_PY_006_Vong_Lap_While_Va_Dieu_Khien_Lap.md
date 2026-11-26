# VI_PY_006: Vòng lặp while, điều kiện dừng và lệnh ngắt break, continue

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Vòng lặp | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

Hình 6.4: Chuyển chương trình sang file mới thêm vào
Hình 6.5: Tùy chọn thay đổi chương trình thực thi trên thanh công cụ

The Dariu Foundation

4
Duyệt mảng nhiều chiều
Qua việc khai báo mảng nhiều chiều, chúng ta có thểnhận ra rằng nó là 2 cấu trúc
mảng một chiều lồng nhau (từchuyên ngành là nested list). Do đó, cách duyệt
mảng nhiều chiều phổbiến nhất là dùng 2 vòng lặp for lồng nhau. Chương trình
sau đây, sẽin ra thông tin vềvịtrí hàng, cột đi kèm với giá trịcủa phần tửtại đó,
như ví dụởChương trình 6.2.
1 a = [[1, 2, 3], [4, 5, 6]]
2 ROW = len(a)
3 COL = len(a[0])
4 for i in range (0, ROW):
5
for j in range (0, COL):
6
print("Hang", i + 1, "Cot", j + 1, ":", a[i][j])
Chương trình 6.2: Duyệt mảng 2 chiều
Thực ra, cách duyệt mảng ởtrên chỉđúng khi giảđịnh rằng, tất cảcác hàng đều
có cùng sốlượng cột. Do đó, chương trình mởtrên chỉcần tính sốlượng cột của
hàng đầu tiên mà thôi (câu lệnh COL = len(a[0]). Đây cũng là nguyên tắc của mảng
trên các ngôn ngữlập trình có cấu trúc chặt chẽnhư Pascal hay C. Tuy nhiên, trên
Python, chúng ta được phép thay đổi sốlượng cột của mỗi hàng trong ma trận
nhiều chiều. Chương trình 6.2 cần phải thay đổi vòng lặp bên trong đểcó thểhoạt
động đúng chức năng, như ví dụởChương trình 6.3.
1 a = [[1, 2, 3], [4, 5, 6], [7, 8]]
2 ROW = len(a)
3 for i in range (0, ROW):
4
COL = len(a[i])

5
for j in range (0, COL):
6
print("Hang", i + 1, "Cot", j + 1, ":", a[i][j])
Chương trình 6.3: Duyệt mảng 2 chiều
Trong ví dụởChương trình 6.3, hàng thứ3 của mảng a chỉcó 2 cột mà thôi. Do đó,
trước khi vào vòng lặp của cột, chúng ta tính lại sốlượng cột bằng câu lệnh COL =
len(a[i]).
5
Nhập mảng nhiều chiều từbàn phím
Thực ra, nhu cầu nhập mảng nhiều chiều từbàn phím không nhiều do sốlượng
phần tửphải nhập là khá nhiều. Đối với chức năng đọc dữliệu từmảng nhiều
chiều, mà chủyếu là mảng 2 chiều, chúng ta sẽđọc dữliệu lên từ1 file có sẵn. Tuy
nhiên trong hướng dẫn này, chúng tôi cũng gợi ý cho người học những bước xử
lý căn bản nhất khi hiện thực việc đọc dữliệu từbàn phím cho mảng 2 chiều. Ý
tưởng chính ởđây là nhập vào từng hàng (mảng 1 chiều), rồi thêm từng hàng đó
vào mảng 2 chiều. Chương trình gợi ý như sau:
1 a=[]
2 ROW = int(input("Nhap so Hang"))
Hướng dẫn lập trình Python cơ bản

3 COL = int(input("Nhap so Cot"))
4 for i in range (0, ROW):
5
temp_row = []
6
for j in range (0, COL):
7
temp = int(input("Phan tu "+str(i)+"-"+str(j)))
8
temp_row.append(temp)
9
a.append(temp_row)
10 print(a)
Chương trình 6.4: Nhập mảng 2 chiều từbàn phím
Trong Chương trình 6.4, biến a dùng đểlưu thông tin của mảng 2 chiều, biến
temp_row dùng đểlưu từng hàng của mảng 2 chiều. Vòng lặp với biến j thực chất
là vòng lặp đểnhập mảng 1 chiều từbàn phím ởbài trước. Cuối cùng, biến a được
in ra đểkiểm tra kết quảnhập vào. Chương trình này đang cho phép nhập vào số
nguyên mà thôi. Trường hợp nhập vào sốthực sẽxem như là một bài tập nâng cao.
Chương trình 6.4 là sựluyện tập rất tốt cho việc phân biệt tầm vực trong Python.
Chúng ta có 2 vòng for lồng nhau và việc gán lại các giá trịcho biến sốcần phải
thực hiện đúng tầm vực thì mới có được kết quảmong muốn.

Trong chương trình này, chúng ta ngầm quy định rằng các hàng đều có sốlượng
cột bằng nhau. Nếu muốn nhập vào một ma trận với sốlượng không biết trước, ví
dụnhư nhập cho đến khi gặp số0, chúng ta sẽphải dùng kĩ thuật khác, sẽđược
trình bày trong bài hướng dẫn sau.
6
Bài tập
1. Viết chương trình tính tổng các phần tửtrong mảng 2 chiều. Mảng được nhập
cốđịnh ởđầu chương trình.
1 a = [[1, 2, 3], [4, 5, 6]]
2 ROW = len(a)
3 COL = len(a[0])
4 tong = 0
5 for i in range(0, ROW):
6
for j in range(0, COL):
7
tong = tong + a[i][j]
8 print("Tong cua cac phan tu la: ", tong)
Chương trình 6.5: Đáp án gợi ý cho bài 1
2. Viết chương trình đếm sốlượng sốchẵn trong mảng 2 chiều. Mảng được nhập
cốđịnh ởđầu chương trình.
1 a = [[1, 2, 3], [4, 5, 6]]
2 ROW = len(a)
3 COL = len(a[0])
4 chan = 0
5 for i in range(0, ROW):
6
for j in range(0, COL):
7
if a[i][j] % 2 == 0:
8
chan = chan + 1

The Dariu Foundation

9 print("So phan tu chan la: ", chan)
Chương trình 6.6: Đáp án gợi ý cho bài 2
3. Viết chương trình đếm sốlượng sốlẻtrong mảng 2 chiều. Mảng được nhập cố
định ởđầu chương trình.
1 a = [[1, 2, 3], [4, 5, 6]]
2 ROW = len(a)
3 COL = len(a[0])
4 le = 0
5 for i in range(0, ROW):

6
for j in range(0, COL):
7
if a[i][j] % 2 != 0:
8
le = le + 1
9 print("So phan tu chan la: ", le)
Chương trình 6.7: Đáp án gợi ý cho bài 3
4. Viết chương trình tìm sốlớn nhất trong mảng 2 chiều. Mảng được nhập cốđịnh
ởđầu chương trình.
1 a = [[1, 2, 3], [4, 5, 6]]
2 ROW = len(a)
3 COL = len(a[0])
4 max1 = a[0][0]
5 for i in range(0, ROW):
6
for j in range(0, COL):
7
if a[i][j] > max1:
8
max1 = a[i][j]
9 print("Phan tu lon nhat la: ", max1)
Chương trình 6.8: Đáp án gợi ý cho bài 4
5. Viết chương trình tìm sốbé nhất trong mảng 2 chiều. Mảng được nhập cốđịnh
ởđầu chương trình.
1 a = [[1, 2, 3], [4, 5, 6]]
2 ROW = len(a)
3 COL = len(a[0])
4 min1 = a[0][0]
5 for i in range(0, ROW):
6
for j in range(0, COL):
7
if a[i][j] < min1:
8
min1 = a[i][j]
9 print("Phan tu nho nhat la: ", min1)
Chương trình 6.9: Đáp án gợi ý cho bài 5
6. Hiện thực lại tất cảcác yêu cầu trên, với mảng được nhập vào từbàn phím.
1 a=[]
2 ROW = int(input("Nhap so Hang "))
3 COL = int(input("Nhap so Cot "))
4 for i in range (0, ROW):
5
temp_row = []

6
for j in range(0, COL):
Hướng dẫn lập trình Python cơ bản

7
temp = int(input("Phan tu "+str(i)+ "-"+ str(j) +"
")))
8
temp_row.append(temp)
9
a.append(temp_row)
10
11 for i in range(0, ROW):
12
for j in range(0, COL):
13
print(a[i][j])
14
15 # Tinh tong , tim so chan , le
16 tong = chan = le = 0
17 for i in range(0, ROW):
18
for j in range(0, COL):
19
tong = tong + a[i][j]
20
if a[i][j] % 2 == 0:
21
chan = chan + 1
22
else:
23
le = le + 1
24
25 # Tim min , max
26 max1 = min1 = a[0][0]
27 for i in range(0, ROW):
28
for j in range(0, COL):
29
if a[i][j] < min1:
30
min1 = a[i][j]

31
if a[i][j] > max1:
32
max1 = a[i][j]
33
34 print(tong , chan , le , max1 , min1)
Chương trình 6.10: Đáp án gợi ý cho bài 6
7
Câu hỏi ôn tập
1. Cách nào sau đây dùng đểkhai báo mảng hai chiều với 2 hàng và 3 cột:
A. a = [[1,2,3], [4,5,6]]
B. a = [1,2,3,4,5,6]
C. a = [1,2,3];[4,5,6]
2. Cách nào sau đây dùng đểgán giá trịcủa phần tửđầu tiên ởhàng thứ2 của
mảng hai chiều a cho biến x:
A. x = a[0,1]
B. x = a[2][1]
C. x = a[1,0]
D. x = a[1][0]
3. Cho đoạn code sau:
1 for i in range (0,2):
2
for j in range (0,2):

The Dariu Foundation

3
print (1)
Lệnh print được thực hiện bao nhiêu lần:
A. 2
B. 3
C. 4
D. 7
4. Cho đoạn code sau:
1 a = [[1 ,2 ,3] ,[4 ,5 ,6] ,[7 ,8 ,9]]
2 for i in range (0,2):
3
for j in range (0,2):
4
print(a[i][j])
Đoạn lệnh trên thực hiện công việc gì:
A. In tất cảcác giá trịcó trong mảng hai chiều a
B. In tất cảcác giá trịcủa 2 hàng đầu trong mảng hai chiều a
C. In 2 giá trịđầu của 2 hàng đầu trong mảng hai chiều a

5. Cho đoạn code sau:
1 x = 0
2 a = [[1 ,2 ,3] ,[4 ,5 ,6]]
3 for i in range (0,2):
4
for j in range (0,3):
5
if a[i][j] % 2 == 0:
6
x = x + a[i][j]
Giá trịcủa biến x là:
A. 9
B. 12
C. 21
6. Cho đoạn code sau:
1 x = 0
2 for i in range (0,1):
3
for j in range (0,2):
4
for j in k (0,3):
5
x = x + 1
Giá trịcủa biến x là:
A. 6
B. 8
C. 9
D. 12
Hướng dẫn lập trình Python cơ bản

7. Cho đoạn code sau:
1 x = 0
2 a = [[1 ,2 ,3] ,[4 ,5 ,6]]
3 for i in range (0,2):
4
for j in range (0,3):
5
if a[i][j] % 2 == 0:
6
break;
7
else:
8

x = x + a[i][j]
Giá trịcủa biến x là bao nhiêu, biết rằng lệnh break dùng đểthoát khỏi vòng
lặp đang chứa nó:
A. 0
B. 1
C. 4
D. 9
Đáp án
1. A
2. D
3. C
4. C
5. B
6. A
7. B

The Dariu Foundation
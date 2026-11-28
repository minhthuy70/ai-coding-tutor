# VI_PY_007: Chuỗi ký tự (str), bảng mã Unicode và các phương thức xử lý chuỗi

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Chuỗi | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

1
Giới thiệu
Vòng lặp là gì? Vòng lặp cho phép bạn lặp lại việc thực thi đoạn code cho tới khi một
điều kiện nhất định được thỏa mãn. Vòng lặp được sửdụng khá phổbiến trong lập
trình. Không giống các ngôn ngữlập trình khác với các vòng lặp khác nhau như
for, while, do...while..., Python chỉhỗtrợvòng lặp for và vòng lặp while.
Trong bài này chúng ta sẽtìm hiểu vềvòng lặp while trong Python, đây là vòng lặp
được sửdụng khá nhiều khi bạn làm các ứng dụng trong thực tế, không chỉriêng
ởPython mà ởcác ngôn ngữkhác đều vậy.
2
Cú pháp vòng lặp while
Python là ngôn ngữđơn giản nên cú pháp của nó cũng đơn giản. Sau đây là cú
pháp chung của vòng lặp while.
1 while expression:
2
statement(s)
Trong đó:
• statement(s): là một lệnh đơn hoặc một tập lênh gồm nhiều lênh đơn. Nếu
chỉcó một lệnh thì bạn có thểkhông cần khoảng trắng, tuy nhiên lời khuyên
là bạn nên sửdụng khoảng trắng đểchương trình được rõ ràng và dễbảo trì
hơn.
• expression: có thểlà một biến hoặc một biểu thức, nhưng bắt buộc giá trị
của nó phải là TRUE hoặc FALSE.
Ví dụ:
1 count = 0
2 while (count
<= 6):
3
print("Luot dem:", count)
4
count = count + 1
5
6 print("Good bye!")
Kết quảin ra:

1 Luot dem: 0
2 Luot dem: 1
3 Luot dem: 2
4 Luot dem: 3
5 Luot dem: 4
6 Luot dem: 5
7 Luot dem: 6
8 Good bye!
Dòng Good bye! không bịlặp bởi vì nó nằm ngoài vòng lặp, còn lượt đếm sẽbịlặp
7 lân biến count có giá trịban đầu là 0 (count = 0), sau mỗi vòng lặp nó tăng lên 1
đơn vị(count = count + 1) và điều kiện dừng vòng lặp là count bé hơn hoặc bằng 6
(count <= 6).

The Dariu Foundation

2.1
Câu lệnh break và continue trong vòng lặp while
2.1.1
Câu lệnh break
Dùng đểkết thúc vòng lặp. Cứnó nằm trong block của vòng lặp nào thì vòng lặp
đó sẽkết thúc khi chạy câu lệnh này.
Trong trường hợp vòng lặp a chứa vòng lặp b. Trong vòng lặp b chạy câu lệnh break
thì chỉvòng lặp b kết thúc, còn vòng lặp a thì không.
2.1.2
Câu lệnh continue
Câu lệnh này dùng đểchạy tiếp vòng lặp. Giảsửmột vòng lặp có cấu trúc như sau:
1 while expression:
2
#while -block -1
3
continue
4
#while -block -2
Khi thực hiện xong while-block-1, câu lệnh continue sẽtiếp tục vòng lặp, không
quan tâm những câu lệnh ởdưới continue và như vậy nó đã bỏqua while-block-2.
2.2
Sửdụng while trên một dòng
Nếu khối lệnh của bạn chỉcó một dòng code, bạn có thểviết vòng while của bạn
chỉtrên một dòng:
1 while True: print("hello")
Phía trên là một vòng lặp vô hạn, với điều kiện luôn luôn là True nên vòng lặp sẽ
chạy mãi cho tới khi bạn kết thúc chương trình.
3
Cú pháp vòng lặp while-else

Có một sựmới mẻđối với vòng lặp while trong Python đó là bạn có thểkết hợp
thêm từkhóa ELSE đểxửlý cho lần lặp không được thực hiện khi điều kiện lặp
false.
1 while expression:
2
statement(s)
3 else:
4
statement(s)
Ví dụ:
1 count = 0
2 while count < 5:
3
print(count , " is
less than 5")
4
count = count + 1
5 else:
6
print(count , " is not less than 5")
Chạy ví dụnày kết quảsẽnhư sau:
Hướng dẫn lập trình Python cơ bản

1 0 is less than 5
2 1 is less than 5
3 2 is less than 5
4 3 is less than 5
5 4 is less than 5
6 5 is not less than 5
Lần lặp thứ6 sẽkhông xảy ra nên code trong lệnh else sẽđược thực hiện.
4
Bài tập
1. Viết chương trình dùng vòng lặp while đểtính tổng các phần tửtrong mảng.
Mảng được nhập cốđịnh ởđầu chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 Tong = 0
4 i = 0
5 while (i < N):
6
Tong = Tong + a[i]
7
i = i + 1;

8 print("Tong cac phan tu trong mang la:", Tong)
Chương trình 7.1: Đáp án gợi ý cho Bài 1
2.Viết chương trình dùng vòng lặp while đểđếm sốlượng sốchẵn trong mảng.
Mảng được nhập cốđịnh ởđầu chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 chan = 0
4 i = 0
5 while (i < N):
6
if a[i] % 2 == 0:
7
chan = chan + 1
8
i = i + 1
9 print("So phan tu chan trong mang la:", chan)
Chương trình 7.2: Đáp án gợi ý cho Bài 2
3. Viết chương trình dùng vòng lặp while đểđếm sốlượng sốlẻtrong mảng. Mảng
được nhập cốđịnh ởđầu chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 le = 0
4 i = 0
5 while (i < N):
6
if a[i] % 2 != 0:
7
le = le + 1
8
i = i + 1
9 print("So phan tu le trong mang la:", le)
Chương trình 7.3: Đáp án gợi ý cho Bài 3

The Dariu Foundation

4. Viết chương trình dùng vòng lặp while đểtìm sốlớn nhất trong mảng. Mảng
được nhập cốđịnh ởđầu chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 max = a[0]
4 i = 0
5 while (i < N):
6
if max < a[i]:

7
max = a[i]
8
i = i + 1
9 print("Phan tu lon nhat trong mang la:", max)
Chương trình 7.4: Đáp án gợi ý cho Bài 4
5. Viết chương trình dùng vòng lặp while đểtìm sốbé nhất trong mảng. Mảng được
nhập cốđịnh ởđầu chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 min = a[0]
4 i = 0
5 while (i < N):
6
if min > a[i]:
7
min = a[i]
8
i = i + 1
9 print("Phan tu nho nhat trong mang la:", min)
Chương trình 7.5: Đáp án gợi ý cho Bài 5
6. Hiện thực lại tất cảcác yêu cầu trên bằng vòng lặp while, với mảng được nhập
vào từbàn phím.
1 a = []
2 N = int(input("Nhap kich thuoc mang: "))
3 i = 0
4 while (i < N):
5
temp = int(input("Nhap phan tu thu " + str(i+1)))
6
a.append(temp)
7
i = i + 1
8
9 #Tinh tong , tim so chan , le
10 tong = chan = le = 0
11 i = 0
12 while (i < N):
13
tong = tong + a[i]
14
if a[i] % 2 == 0:
15
chan = chan + 1
16

else:
17
le = le + 1
18
i = i + 1
19 #Tim min , max
20 max1 = min1 = a[0]
21 i = 0
Hướng dẫn lập trình Python cơ bản

22 while (i < N):
23
if a[i] < min1:
24
min1 = a[i]
25
if a[i] > max1:
26
max1 = a[i]
27
i = i + 1
28 print(tong , chan , le , max1 , min1)
Chương trình 7.6: Đáp án gợi ý cho Bài 6
5
Câu hỏi ôn tập
1. Giá trịcủa x là gì
1 x = 0
2 while (x > 10):
3
x+=2
4 print(x)
A. 0
B. 10
C. 12
D. Không biết giá trịcủa x vì vòng lặp vô tận
2. Giá trịcủa x là gì
1 x = 0
2 while (x < 10):
3
x+=2
4 print(x)
A. 8
B. 100

C. 101
D. Không biết giá trịcủa x vì vòng lặp vô tận
3. Giá trịcủa x là gì
1 x = 0
2 while (x < 50):
3
x-=2
4 print(x)
A. 49
B. 50
C. 51
D. Không biết giá trịcủa x vì vòng lặp vô tận
4. Trong các lệnh while bên dưới, lệnh while nào sẽtạo vòng lặp vô tận:
A.
1 while True:
2
The Dariu Foundation

B.
1 a = [1,2,3]
2 while a:
3
C.
1 while "0":
2
D. Còn phụthuộc vào đoạn lệnh bên trong lệnh while.
5. Đoạn lệnh bên dưới in ra màn hình bao nhiều lần ký tự"a" và ký tự"b" ?
1 x = 0
2 while x < 5:
3
print("a")
4
x = x + 2
5 else:
6
print("b")
A. 1 lần "a" và 1 lần "b"
B. 2 lần "a" và 1 lần "b"
C. 3 lần "a" và 2 lần "b"
D. 3 lần "a" và 2 lần "b"

6. Kết quảcủa s là gì?
1 s = ""
2 n = 5
3 while n > 0:
4
n -= 1
5
if (n % 2) == 0:
6
continue
7
a = [’foo’, ’bar’, ’baz’]
8
while a:
9
s += str(n) + a.pop (0)
10
if len(a) < 2:
11
break
A. 3bar3bar1for1for
B. 3foo3bar1foo1bar
C. 3foo3bar1bar1for
D. Tất cảđều sai
Đáp án
1. A
2. A
3. D
4. D
5. B
6. B
Hướng dẫn lập trình Python cơ bản

The Dariu Foundation

CHƯƠNG 8
Các thao tác trên FILE

1
Giới thiệu

Trong một sốtrường hợp, việc nhập dữliệu từbàn phím là không khảthi và mất
khá nhiều thời gian, chẳng hạn như đọc dữliệu từmảng nhiều chiều ởbài trước.
Hay như một ví dụkhác, chúng ta cần lưu lại kết quảcủa việc thực thi chương trình
đểxem lại. Trong những trường hợp như vậy, chúng ta sẽđọc nội dung từfile hoặc
lưu kết quảthực thi ra file.
Quy trình làm việc với file thường có 3 bước cơ bản như sau: Mởfile, đọc hoặc ghi
dữliệu, cuối cùng là đóng file. Nếu file quên mở, hiển nhiên bạn sẽkhông thao tác
được gì. Ngược lại, nếu file quên đóng, lần mởtiếp theo có thểchương trình sẽbáo
lỗi, tùy thuộc vào mức độhỗtrợcủa chương trình soạn thảo. Tuy nhiên đểcho an
toàn, hay luôn nhớđóng lại file ởcuối chương trình.
2
Ghi dữliệu ra File
Chúng tôi sẽbắt đầu với hướng dẫn ghi dữliệu ra file trước. Có thểxem đây là một
quá trình xuất dữliệu (output). Và thông thường, quá trình này sẽđơn giản hơn
so với việc đọc dữliệu từfile. Một chương trình ví dụcho việc mở1 file có tên là
test.txt, ghi 1 sốnội dung và đóng file đó lại như sau:
1 file = open("test.txt","w")
2 file.write("Test ghi file 1")
3 file.write("Test ghi file 2")
4 file.close ()
Chương trình 8.1: Chương trình mởfile ghi nội dung và đóng file
Trong Chương trình 8.1, file là một biến số, tham chiếu tới file cần làm việc. Biến
file sẽcó hiệu lực sau câu lệnh đầu tiên, là open. Câu lệnh open này có 2 tham số
quan trọng:
• Tên file: Đặt tên cho file cần lưu dữliệu. File này sẽđược đặt cùng thư mục
với file Python đang làm việc. Trong trường hợp bạn muốn lưu ởmột đường
dẫn nào đó trong bộnhớ, chúng ta có thểchỉđịnh đường dẫn tuyệt đối, ví dụ
như là "D:/test.txt". Bạn hãy lưu ý ký tựphân cách trong đường dẫn, là ký tự
hướng từphải sang trái, nó ngược lại với ký tựđường dẫn bình thường.
• Chếđộmởfile: Có rất nhiều chếđộmởfile trên Python, ởđây chúng tôi chỉ
trình bày những chếđộthường dùng nhất, như trình bày bên dưới:
– "r": Chỉmởfile đểđọc.
– "w": Chỉmởfile đểghi. Nếu file chưa tồn tại thì tạo file mới. Nếu file đã
có thì xóa nội dung file cũ và ghi nội dung mới.
– "a": Chỉmởfile đểghi thêm. Nếu file chưa tồn tại thì tạo file mới. Nếu
file đã có thì ghi thêm nội dung vào file.
Trong ví dụởChương trình 8.1, chúng ta mởfile ởchếđộ"w", tức là mởfile đểghi.
Mới ban đầu, file test.txt này không tồn tại, nên hệthống sẽtựtạo ra file này và lưu
ởcùng thư mục với file python mà chúng ta đang làm việc. Cứmỗi lần chạy chương
trình, nội dung cũ của file này sẽbịxóa và ghi lại nội dung mới. Trong trường hợp

The Dariu Foundation
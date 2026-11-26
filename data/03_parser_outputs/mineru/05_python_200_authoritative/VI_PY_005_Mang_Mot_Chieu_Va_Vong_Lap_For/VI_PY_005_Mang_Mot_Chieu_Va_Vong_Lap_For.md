<!-- page: 1 -->
# VI_PY_005: Mảng một chiều và cấu trúc vòng lặp for với hàm range()

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Vòng lặp | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 50 -->
1
Giới thiệu
Mảng là một cấu trúc dữliệu cơ bản của tất cảcác ngôn ngữlập trình. Khác với
biến đơn, chỉdùng đểlưu giá trịriêng lẻ, mảng là tập hợp của nhiều phần tửthuộc
cùng một kiểu dữliệu duy nhất, ví dụnhư mảng sốnguyên hay mảng chuỗi kí tự.
Tuy nhiên, trên Python, khái niệm mảng thuần túy như các ngôn ngữlập trình
khác như Pascal, C hay C++ khá phức tạp và không thân thiện với người mới bắt
đầu. Do đó, trong hướng dẫn này, chúng tôi sẽdùng khái niệm danh sách (list) để
thay cho mảng. Thoạt nhìn, chúng ta sẽthấy nó không khác gì là mảng trong các
ngôn ngữlập trình khác. Chúng tôi vẫn dùng thuật ngữ"mảng" (array) trong bài
hướng dẫn này, cho gần gũi với người đọc.
2
Khai báo và truy xuất mảng một chiều
Mảng được khai báo trên Python bằng chuỗi kí tự[], ởgiữa là các phần tửcủa
mảng, cách nhau bằng dấu phẩy (,), như ví dụbên dưới:
1 a = [1, 4, 5, 7]
2 print("So thu nhat", a[0])
3 print("So thu hai", a[1])
Chương trình 5.1: Khai báo và truy xuất một mảng
Như ví dụởChương trình 5.1, mảng a có tất cả4 phần tử. Việc truy xuất từng phần
tửtrong a được thực hiện qua tác vụa[0] hay a[1]. Điều này có nghĩa là, phần tử
đầu tiên sẽcó chỉsốlà 0, và phần tửcuối cùng sẽcó chỉsốlà 3. Vì lý do nào đó, mà
bạn truy xuất phần tửa[4], chương trình sẽbáo lỗi "list index out of range", tức là
truy xuất vượt tầm giới hạn của mảng.
Sựmềm dẻo trong ngôn ngữPython cho phép bạn truy cập các phần tửvới chỉsố
âm, ví dụnhư a[-1] cho phần tửcuối cùng và lùi dần tới phần tửđầu tiên, là a[-4].
Lỗi tràn giới hạn tương tựnhư trên cũng xuất hiện khi bạn truy xuất tới a[-5]. Tuy
nhiên chúng tôi thực sựkhông khuyến khích bạn làm theo quy luật này.
3
Cấu trúc lặp for
Khi làm việc với mảng, tác vụthường sửdụng nhất gọi là duyệt mảng. Chúng ta
cần 1 vòng lặp đểxửlý qua tất cảcác phần tửcủa mảng. Trong bài hướng dẫn này,
chúng ta sẽsửdụng cấu trúc lặp FOR.
Trong cấu trúc này, chúng ta cần một biến số, đặt tên là i, đểgiữchỉsốphần tử

<!-- page: 2 -->

hiện tại của mảng. Biến này sẽtựđộng tăng lên 1 sau mỗi lần lặp. Trong Python,
cách đơn giản nhất đểhiện thực chức năng này là xài câu lệnh range(Sốcận dưới,
Sốcận trên), được trình bài như chương trình bên dưới:
1 a = [1, 4, 5, 7]
2 N = len(a)
3 print("Kich thuoc mang", N)
Trang 50
The Dariu Foundation

<!-- page: 51 -->
4 for i in range(0,N):
5
print(i)
Chương trình 5.2: Câu lệnh range trên Python
Trong ví dụởChương trình 5.2, chúng ta lấy kích thước của mảng thông qua toán
tửlen rồi gán kết quảvào biến N. Biến N sau đó sẽcó giá trịlà 4, vì mảng a đang có
4 phần tử. Tuy nhiên trong vòng lặp for, các giá trịđược in ra từ0 đến 3 mà thôi.
Đó là lý do tại sao, câu lệnh range sẽvô vùng phù hợp với tác vụduyệt mảng trên
Python, bởi chỉsốcủa mảng được đánh từ0 cho tới N - 1, với N là kích thước của
mảng.
Chúng ta sẽcải tiến chương trình ởtrên đểin ra từng giá trịcủa mảng, như sau:
1 a = [1, 4, 5, 7]
2 N = len(a)
3 print("Kich thuoc mang", N)
4 for i in range(0,N):
5
print("So thu",i + 1, a[i])
Chương trình 5.3: In các giá trịtrong mảng
Một lần nữa, trong ngôn ngữtựnhiên, chúng ta thường định vịsốđầu tiên là số
thứnhất (số1), còn trong ngôn ngữlập trình Python, vịtrí đầu tiên là vịtrí 0. Do
đó, trong câu lệnh in ra màn hình, đểthông tin thân thiện hơn với người dùng,
chúng ta sẽcộng biếni thêm 1 đơn vị.
Cấu trúc lặp FOR trình bày trong hướng dẫn này còn gọi là cấu trúc lặp hữu hạn.
Điều này có nghĩa là trước khi bắt đầu vòng lặp, các giá trịcủa biến i đã được thiết
lập dựa vào giá trịcủa N. Từđó, vòng lặp được thực thi thông qua biến i và hoàn
toàn độc lập với N. Do đó, nếu chúng ta có thay đổi giá trịN bên trong vòng lặp,
kết quảvẫn là không thay đổi.
1 a = [1, 4, 5, 7]
2 N = len(a)
3 print("Kich thuoc mang", N)
4 for i in range(0,N):
5
print("So thu",i + 1, a[i])
6
N = N - 1

<!-- page: 3 -->

Chương trình 5.4: Vòng lặp hữu hạn for không phụthuộc vào giá trịN
Chương trình 5.4 là ví dụđểminh họa cho sốvòng lặp cốđịnh của cấu trúc FOR.
Tại thời điểm thiết lập ban đầu, N = 4 và chương trình sẽđược lặp 4 lần, bất chấp
việc chúng ta thay đổi giá trịN bên trong vòng lặp. Do đó, cấu trúc này thường
được sửdụng cho những trường hợp có sốvòng lặp cốđịnh.
Đến đây, người học có thểtạm dừng đểchuyển sang phần bài tập (từ1 đến 5) để
luyện tập với phần mảng trên Python. Phần tiếp theo của hướng dẫn này sẽtrình
bày cách nhập một mảng từbàn phím, thay vì gán một mảng cốđịnh như các ví
dụởtrên.
Hướng dẫn lập trình Python cơ bản
Trang 51

<!-- page: 52 -->
4
Nhập mảng từbàn phím
Theo tư tưởng trình bày trong hướng dẫn này, chúng tôi đặt biệt ưu tiên việc xuất
kết quảtrước, còn việc xửlý đầu vào sẽthực hiện sau. Lý do là việc xửlý dữliệu
đầu vào thường là phức tạp hơn. Ví dụnhư trong yêu cầu này, chúng ta mong đợi
người dùng sẽnhập vào một con số. Tuy nhiên vì lý do nào đó, người dùng lại nhập
vào một chuỗi kí tự. Việc xửlý những lỗi này cũng không hềđơn giản, chúng ta sẽ
yêu cầu người dùng nhập lại, hay là sẽmặc định cho các giá trịnhập sai là 0.
Trong hướng dẫn này, chúng tôi sẽchỉtập trung vào một ứng dụng đơn giản:
Chương trình yêu cầu nhập vào kích thước của mảng, một vòng lặp sẽhỏi người
dùng nhập vào từng phần tửcho mảng.
Với yêu cầu như trên, chúng ta sẽkhởi động mảng a = [], chưa có phần tửnào
cả. Sau khi hỏi người dùng nhập sốN, vòng lặp for sẽhỏi đểnhập từng phần tử.
Chương trình gợi ý như sau:
1 a = []
2 N = int(input("Nhap kich thuoc mang: "))
3 for i in range(0,N):
4
temp = int(input("Nhap phan tu thu " + str(i + 1)))
5
a.append(temp)
6 print(a)
Chương trình 5.5: Nhập các giá trịcủa mảng từbàn phím
Đểcho câu lệnh input trởnên thân thiện hơn, chúng ta sẽthêm thông tin vềsố
thứtựcủa mảng khi yêu cầu người dùng nhập vào. Do i + 1 là kiểu số, nên nó phải
được chuyển sang kiểu chuỗi trước khi ghép với một chuỗi khác. Cuối cùng, toán
tửappend là đểthêm phần tửvừa nhập vào mảng a. Kết thúc chương trình, chúng
ta sẽdùng lệnh print(a) đểkiểm tra các giá trịvừa nhập vào của mảng.
Cần lưu ý là, đối với các ngôn ngữlập trình, sẽkhông có toán tửthêm 1 phần tử
vào mảng như Chương trình 9.2. Ởđây, bản chất là chúng ta đang dùng danh sách
đểthay thếcho chức năng của một mảng, nên mới có toán tửnày.
5

<!-- page: 4 -->

Bài tập
1. Viết chương trình tính tổng các phần tửtrong mảng. Mảng được nhập cốđịnh ở
đầu chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 Tong = 0
4 for i in range(0,N):
5
Tong = Tong + a[i]
6 print("Tong cac phan tu trong mang la:", Tong)
Chương trình 5.6: Đáp án gợi ý cho Bài 1
2. Viết chương trình đếm sốlượng sốchẵn trong mảng. Mảng được nhập cốđịnh
ởđầu chương trình.
Trang 52
The Dariu Foundation

<!-- page: 53 -->
1 a = [1,2,3,4,5]
2 N = len(a)
3 chan = 0
4 for i in range(0,N):
5
if a[i] % 2 == 0:
6
chan = chan + 1
7 print("So phan tu chan trong mang la:", chan)
Chương trình 5.7: Đáp án gợi ý cho Bài 2
3. Viết chương trình đếm sốlượng sốlẻtrong mảng. Mảng được nhập cốđịnh ở
đầu chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 le = 0
4 for i in range(0,N):
5
if a[i] % 2 != 0:
6
le = le + 1
7 print("So phan tu le trong mang la:", le)
Chương trình 5.8: Đáp án gợi ý cho Bài 3
4. Viết chương trình tìm sốlớn nhất trong mảng. Mảng được nhập cốđịnh ởđầu
chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 max = a[0]
4 for i in range(1,N):

<!-- page: 5 -->

5
if max < a[i]:
6
max = a[i]
7 print("Phan tu lon nhat trong mang la:", max)
Chương trình 5.9: Đáp án gợi ý cho Bài 4
5. Viết chương trình tìm sốbé nhất trong mảng. Mảng được nhập cốđịnh ởđầu
chương trình.
1 a = [1,2,3,4,5]
2 N = len(a)
3 min = a[0]
4 for i in range(1,N):
5
if min > a[i]:
6
min = a[i]
7 print("Phan tu nho nhat trong mang la:", min)
Chương trình 5.10: Đáp án gợi ý cho Bài 5
6. Hiện thực lại tất cảcác yêu cầu trên, với mảng được nhập vào từbàn phím.
1 a = []
2 N = int(input("Nhap kich thuoc mang: "))
3 for i in range(0, N):
4
temp = int(input("Nhap phan tu thu " + str(i+1)))
5
a.append(temp)
6
Hướng dẫn lập trình Python cơ bản
Trang 53

<!-- page: 54 -->
7 #Tinh tong , tim so chan , le
8 tong = chan = le = 0
9 for i in range(0,N):
10
tong = tong + a[i]
11
if a[i] % 2 == 0:
12
chan = chan + 1
13
else:
14
le = le + 1
15

<!-- page: 6 -->

16 #Tim min , max
17 max1 = min1 = a[0]
18 for i in range(1,N):
19
if a[i] < min1:
20
min1 = a[i]
21
if a[i] > max1:
22
max1 = a[i]
23
24 print(tong , chan , le , max1 , min1)
Chương trình 5.11: Đáp án gợi ý cho Bài 6
Trang 54
The Dariu Foundation

<!-- page: 55 -->
6
Câu hỏi ôn tập
1. Kết quảcủa đoạn lệnh sau là gì?
1 numbers = [1, 2, 3, 4]
2 numbers.append ([5 ,6 ,7 ,8])
3 print(len(numbers))
A. 4
B. 5
C. 8
D. Báo lỗi
2. Kết quảcủa đoạn lệnh sau là gì?
1 list1 = [1, 2, 3, 4]
2 list2 = [5, 6, 7, 8]
3 print(len(list1 + list2))
A. 2
B. 4
C. 8
D. Báo lỗi
3. Kết quảcủa đoạn lệnh sau là gì?
1 list1 = [1, 2, 3, 4]
2 print(list1 [4])
A. 3
B. 4
C. 1
D. Báo lỗi
4. Kết quảcủa đoạn lệnh sau là gì?
1 x = sum(range (5))

<!-- page: 7 -->

2 print(x)
A. 4
B. 5
C. 10
D. 15
Hướng dẫn lập trình Python cơ bản
Trang 55

<!-- page: 56 -->
5. Đoạn lệnh nào sau đây được dùng đểin các phần tửcủa mảng lis1t ra màn
hình:
1 list1 = [1,2,3,4]
A.
1 for i in list1:
2
print(i)
B.
1 for i in range(len(list1))
2
print(a[i])
C. Cảhai đoạn lệnh trên đều đúng
D. Cảhai đoạn lệnh trên đều sai
6. Kết quảcủa đoạn code dưới đây là gì, biết rằng lệnh break dùng đểthoát khỏi
vòng lặp đang chứa nó:
1 for i in range (10):
2
if i == 4:
3
break
4
else:
5
print(i)
6 else:
7
print("Python")
A. 0 1 2 3 4
B. 0 1 2 3 Python
C. 0 1 2 3
D. 0 1 2 3 4 Python
7. Giá trịcủa a sau khi kết thúc vòng lặp là bao nhiêu :
1 a = 0
2 for i in range (10, 14):
3
a = a + 3

<!-- page: 8 -->

A. 9
B. 12
C. 15
D. 18
Đáp án
1. C
2. C
3. D
4. C
5. C
6. C
7. C
Trang 56
The Dariu Foundation

<!-- page: 57 -->
CHƯƠNG 6
Mảng nhiều chiều - FOR lồng nhau

<!-- page: 58 -->
1
Giới thiệu
Như đã giới thiệu ởbài trước, mảng một chiều chứa tập hợp nhiều phần tửcó cùng
kiểu dữliệu với nhau. Trong một sốtrường hợp, chúng ta sẽcó mỗi phần tửlà một
mảng. Điều này tạo nên một khái niệm mới, gọi là mảng nhiều chiều. Một trong
những ví dụđiển hình vềmảng nhiều chiều là ma trận, cấu trúc dữliệu thường
thấy cho việc xửlý ảnh hoặc xửlý trong toán học.
Cũng như ởbài trước, chúng ta có thểsửdụng danh sách (list) đểhiện thực mảng
nhiều chiều: Mỗi một phần tửcủa danh sách là một danh sách khác. Khi sửdụng
danh sách đểhiện thực thay cho mảng, các thao tác làm việc sẽrất giống với cấu
trúc mảng truyền thống trên các ngôn ngữkhác như Pascal hay C. Việc truy xuất
1 phần tửtrong mảng sẽcần 2 chỉsốcho mảng 2 chiều, tương tựnhư khái niệm
hàng và cột trong các ngôn ngữkhác.
Tuy nhiên, trước khi đi vào chi tiết của mảng nhiều chiều, chúng ta sẽtạo mới thêm
một file python trong dựán. Dựán đầu tiên này, chúng ta có thểlưu nó như một
dạng thư viện chương trình mẫu, và sửdụng nó cho các dựán sau này.
2
Thêm một file Python
Mặc định, khi mới tạo ra dựán (project), chúng ta chỉcó 1 file python, là main.py.
Khi bấm nút Run trên thanh công cụ(hoặc nhấn phím nóng Shift F10), Pycharm
sẽmặc định chạy chương trình trong file main.py. Trong hướng dẫn này, chúng ta
sẽthêm một file mới, đặt tên là mang_2_chieu.py, và cấu hình lại PyCharm đểnó
có thểchạy chương trình trong file này. Các bước hướng dẫn được trình bày chi
tiết bên dưới.
Bước 1: Từmenu File, chọn vào New... (tránh chọn nhầm vào New Project...). Một

<!-- page: 9 -->

giao diện hiện ra và chúng ta chọn tiếp vào Python File, như minh họa ởHình 6.1.
Hình 6.1: Thêm mới một file Python
Bước 2: Đặt tên cho file là mang_2_chieu rồi nhấn Enter, như minh họa ởHình
6.2. Phần đuôi mởrộng .py cho file sẽtựđộng thêm vào.
Trang 58
The Dariu Foundation
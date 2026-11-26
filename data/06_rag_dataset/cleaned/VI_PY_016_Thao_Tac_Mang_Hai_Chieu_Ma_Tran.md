# VI_PY_016: Thao tác mảng hai chiều, ma trận và bài tập xử lý bảng số liệu

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Mảng | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

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

The Dariu Foundation

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
2 print(x)
A. 4
B. 5
C. 10
D. 15
Hướng dẫn lập trình Python cơ bản

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

The Dariu Foundation

CHƯƠNG 6
Mảng nhiều chiều - FOR lồng nhau

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
giao diện hiện ra và chúng ta chọn tiếp vào Python File, như minh họa ởHình 6.1.
Hình 6.1: Thêm mới một file Python
Bước 2: Đặt tên cho file là mang_2_chieu rồi nhấn Enter, như minh họa ởHình
6.2. Phần đuôi mởrộng .py cho file sẽtựđộng thêm vào.

The Dariu Foundation
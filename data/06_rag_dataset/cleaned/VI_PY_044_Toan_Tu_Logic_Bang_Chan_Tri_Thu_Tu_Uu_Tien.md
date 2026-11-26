# VI_PY_044: Toán tử logic, bảng chân trị và thứ tự ưu tiên các phép toán

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Toán tử | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
Bài tập 8: Bài tập nâng cao
1. Viết chương trình đọc một đoạn văn bản, tách các từvà sửdụng set đểđếm sốtừ
khác nhau.
2. Sửdụng dictionary đểthống kê tần suất xuất hiện của từng ký tựtrong một chuỗi.
3. Kết hợp tuple, list và dictionary đểxây dựng cấu trúc dữliệu lưu trữbảng điểm của
một lớp học.
22

CHƯƠNG 3. Nhập xuất dữliệu trong Python
Trong hầu hết các chương trình máy tính, dữliệu không chỉđược xửlý nội bộmà còn
cần được nhập từbên ngoài và xuất ra cho người sửdụng hoặc lưu trữlâu dài. Đối với
sinh viên ngành Khoa học Máy tính, việc nắm vững các kỹthuật nhập xuất dữliệu trong
Python là nền tảng quan trọng đểxây dựng các chương trình hoàn chỉnh, có khảnăng
tương tác và xửlý dữliệu thực tế.
Chương này trình bày chi tiết các phương pháp nhập xuất dữliệu trong Python, bao
gồm xuất dữliệu ra màn hình, nhập dữliệu từbàn phím và làm việc với tập tin.
3.1
Xuất dữliệu ra màn hình
3.1.1
Hàm print()
Hàm print() là công cụcơ bản nhất đểhiển thịdữliệu ra màn hình. Hàm này có
thểin ra các kiểu dữliệu khác nhau như chuỗi, sốnguyên, sốthực và cảcác cấu trúc dữ
liệu.
print("Hello Python")
print(2025)
print(3.14)
Kết quảhiển thị:
Hello Python
2025
3.14
Python tựđộng chuyển đổi dữliệu sang dạng chuỗi trước khi in ra màn hình, giúp
người lập trình không cần xửlý thủcông.

3.1.2
In nhiều dữliệu cùng lúc
Hàm print() cho phép in nhiều giá trịtrong cùng một lệnh.
name = "An"
age = 20
score = 8.5
print("Ten:", name, "- Tuoi:", age, "- Diem:", score)
Kết quảhiển thị:
Ten: An - Tuoi: 20 - Diem: 8.5
23

CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
3.1.3
Tùy chỉnh định dạng khi in
a, Sửdụng sep và end
print(1, 2, 3, sep=" | ")
print("Xin", end=" ")
print("chao Python")
Kết quảhiển thị:
1 | 2 | 3
Xin chao Python
b, Định dạng bằng f-string
F-string cho phép chèn biến trực tiếp vào chuỗi và định dạng dữliệu một cách linh
hoạt.
a = 7
b = 3
print(f"{a} + {b} = {a + b}")
Kết quảhiển thị:
7 + 3 = 10
Định dạng sốthực:
pi = 3.14159265
print(f"Gia tri pi lam tron: {pi:.3f}")
Kết quảhiển thị:
Gia tri pi lam tron: 3.142
3.1.4
In dữliệu dạng bảng
Trong các bài toán kỹthuật, dữliệu thường được trình bày dưới dạng bảng đểdễso
sánh và phân tích.
print(f"{'Mon hoc':<10}{'Diem':>6}")
print(f"{'-'*16}")
print(f"{'Toan':<10}{8.5:>6}")
print(f"{'Ly':<10}{7.5:>6}")
print(f"{'Tin':<10}{9.0:>6}")
Kết quảhiển thị:

Mon hoc
Diem
24

CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
----------------
Toan
8.5
Ly
7.5
Tin
9.0
3.2
Nhập dữliệu từbàn phím
3.2.1
Hàm input()
Hàm input() cho phép chương trình nhận dữliệu từngười dùng thông qua bàn
phím.
name = input("Nhap ten: ")
print("Xin chao", name)
Ví dụnhập:
Nhap ten: Minh
Kết quảhiển thị:
Xin chao Minh
3.2.2
Nhập và chuyển đổi kiểu dữliệu
Dữliệu nhập vào từbàn phím luôn có kiểu chuỗi, do đó cần chuyển đổi sang kiểu phù
hợp.
age = int(input("Nhap tuoi: "))
height = float(input("Nhap chieu cao (m): "))
print(f"Tuoi: {age}, Chieu cao: {height} m")
Kết quảhiển thị(ví dụ):
Nhap tuoi: 20
Nhap chieu cao (m): 1.68
Tuoi: 20, Chieu cao: 1.68 m
3.3
Nhập xuất dữliệu với tập tin
3.3.1
Ví dụtập tin dữliệu
Giảsửcó tập tin scores.txt với nội dung sau:
SV01,Toan,8.5
SV01,Ly,7.5
SV01,Tin,9.0
SV02,Toan,6.5

SV02,Ly,7.0
SV02,Tin,8.0
25

CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
Tập tin này lưu trữdữliệu điểm của sinh viên, mỗi dòng gồm mã sinh viên, tên môn
học và điểm.
3.3.2
Đọc tập tin và xửlý dữliệu
total = 0
count = 0
with open("scores.txt", "r") as f:
for line in f:
parts = line.strip().split(",")
score = float(parts[2])
total += score
count += 1
average = total / count
print(f"Diem trung binh tat ca cac mon: {average:.2f}")
Kết quảhiển thị:
Diem trung binh tat ca cac mon: 7.75
3.3.3
Ghi kết quảra tập tin
with open("result.txt", "w") as f:
f.write(f"Diem trung binh: {average:.2f}\n")
Sau khi chạy chương trình, tập tin result.txt sẽchứa kết quảtính toán.
3.4
Các phương thức làm việc với tập tin trong Python
Khi mởmột tập tin bằng hàm open(), Python trảvềmột đối tượng file. Đối tượng
này cung cấp nhiều phương thức cho phép người lập trình thao tác linh hoạt với tập tin
như đọc, ghi, di chuyển con trỏ, kiểm tra trạng thái và quản lý bộnhớđệm.
Việc hiểu rõ các phương thức này giúp chương trình làm việc với tập tin an toàn, hiệu
quảvà phù hợp với các ứng dụng thực tế.
3.4.1
close()
Phương thức close() dùng đểđóng một tập tin đang mở. Sau khi tập tin đã được
đóng, mọi thao tác đọc hoặc ghi lên tập tin đó đều không còn hợp lệ.
f = open("example.txt", "w")
f.write("Hello Python")
f.close()
Sau khi gọi close(), dữliệu được ghi hoàn toàn xuống tập tin và tài nguyên hệthống
26

CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
được giải phóng.
3.4.2
fileno()
Phương thức fileno() trảvềmột sốnguyên đại diện cho file descriptor – một khái
niệm ởmức hệđiều hành dùng đểquản lý các luồng vào ra.
f = open("example.txt", "r")
print(f.fileno())
f.close()
Kết quảhiển thị(ví dụ):
3
Giá trịtrảvềcó thểkhác nhau tùy vào hệthống và thời điểm chạy chương trình.
3.4.3
flush()
Phương thức flush() dùng đểxóa sạch bộnhớđệm của luồng file, đảm bảo dữliệu
được ghi ngay xuống tập tin mà không cần chờđóng file.
f = open("example.txt", "w")
f.write("Du lieu tam thoi")
f.flush()
Phương thức này đặc biệt quan trọng trong các chương trình ghi log hoặc hệthống thời
gian thực.
3.4.4
isatty()
Phương thức isatty() trảvềTrue nếu tập tin được kết nối với một thiết bịđầu cuối
(terminal), ngược lại trảvềFalse.
f = open("example.txt", "r")
print(f.isatty())
f.close()
Kết quảhiển thị:
False
3.4.5
read(n)
Phương thức read(n) dùng đểđọc tối đa n ký tựtừtập tin, tính từvịtrí con trỏhiện
tại.
27

CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
with open("example.txt", "r") as f:
content = f.read(5)
print(content)
Kết quảhiển thị(ví dụ):
Hello
3.4.6
readable()

Phương thức readable() kiểm tra xem tập tin có thểđọc được hay không.
f = open("example.txt", "r")
print(f.readable())
f.close()
Kết quảhiển thị:
True
3.4.7
readline(n=-1)
Phương thức readline() đọc và trảvềmột dòng từtập tin. Nếu tham sốn được chỉ
định, phương thức sẽđọc tối đa n ký tự.
with open("scores.txt", "r") as f:
line = f.readline()
print(line)
Kết quảhiển thị(ví dụ):
SV01,Toan,8.5
3.4.8
readlines(n=-1)
Phương thức readlines() đọc toàn bộcác dòng trong tập tin và trảvềdưới dạng
một danh sách chuỗi.
with open("scores.txt", "r") as f:
lines = f.readlines()
print(lines)
Kết quảhiển thị(ví dụ):
['SV01,Toan,8.5\n', 'SV01,Ly,7.5\n', 'SV01,Tin,9.0\n']
3.4.9
seek(offset, from=SEEK_SET)
Phương thức seek() dùng đểthay đổi vịtrí con trỏđọc/ghi trong tập tin.
28

CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
with open("example.txt", "r") as f:
f.seek(6)
print(f.read())
Phương thức này thường được dùng khi cần truy cập ngẫu nhiên dữliệu trong tập tin.
3.4.10
seekable()
Phương thức seekable() trảvềTrue nếu luồng file hỗtrợtruy cập ngẫu nhiên.
f = open("example.txt", "r")
print(f.seekable())
f.close()
3.4.11
tell()
Phương thức tell() trảvềvịtrí hiện tại của con trỏtrong tập tin.
with open("example.txt", "r") as f:

print(f.tell())
f.read(5)
print(f.tell())
Kết quảhiển thị(ví dụ):
0
5
3.4.12
truncate(size=None)
Phương thức truncate() dùng đểcắt gọn kích thước tập tin vềsốbyte được chỉ
định.
with open("example.txt", "r+") as f:
f.truncate(5)
Sau khi thực hiện, nội dung tập tin chỉcòn 5 ký tựđầu tiên.
3.4.13
writable()
Phương thức writable() kiểm tra xem tập tin có cho phép ghi hay không.
f = open("example.txt", "w")
print(f.writable())
f.close()
Kết quảhiển thị:
29

CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
True
3.4.14
write(s)
Phương thức write() ghi chuỗi s vào tập tin và trảvềsốký tựđã ghi.
with open("example.txt", "w") as f:
n = f.write("Python File I/O")
print(n)
Kết quảhiển thị:
15
3.4.15
writelines(lines)
Phương thức writelines() ghi một danh sách các chuỗi vào tập tin.
lines = ["Dong 1\n", "Dong 2\n", "Dong 3\n"]
with open("example.txt", "w") as f:
f.writelines(lines)
Sau khi chạy, tập tin sẽchứa toàn bộcác dòng trong danh sách.
3.5
Nhận xét
Các phương thức làm việc với tập tin trong Python cung cấp khảnăng kiểm soát chi
tiết quá trình đọc, ghi và quản lý dữliệu. Việc sửdụng đúng phương thức không chỉgiúp
chương trình hoạt động chính xác mà còn nâng cao hiệu suất và độtin cậy của hệthống,

đặc biệt trong các ứng dụng kỹthuật và xửlý dữliệu lớn.
3.6
Ứng dụng thực tế
Trong thực tếkỹthuật và công nghệthông tin, nhập xuất dữliệu đóng vai trò then chốt
trong hầu hết các hệthống phần mềm.
Trong các hệthống thu thập dữliệu cảm biến, Python thường được sửdụng đểđọc dữ
liệu từtập tin log hoặc từthiết bịđo, xửlý và ghi lại kết quảphân tích. Trong các bài toán
quản lý, dữliệu sinh viên, thiết bịhoặc tài nguyên thường được nhập từtập tin, xửlý và
xuất ra dưới dạng báo cáo.
Đối với sinh viên ngành Khoa học Máy tính, việc thành thạo nhập xuất dữliệu giúp
hình thành tư duy xây dựng chương trình hoàn chỉnh, có khảnăng tương tác với người
dùng và làm việc với dữliệu thực tế, tạo tiền đềcho các học phần nâng cao như xửlý dữ
liệu, trí tuệnhân tạo và hệthống thông tin.
3.7
Bài tập chương
3.7.1
Câu hỏi trắc nghiệm
1. Phát biểu nào sau đây là đúng vềhàm print() trong Python?
30
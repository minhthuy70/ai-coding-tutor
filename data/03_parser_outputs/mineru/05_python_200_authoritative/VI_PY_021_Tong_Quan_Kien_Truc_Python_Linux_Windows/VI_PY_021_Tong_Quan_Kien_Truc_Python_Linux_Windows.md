<!-- page: 1 -->
# VI_PY_021: Tổng quan kiến trúc thông dịch Python trên hệ điều hành Linux và Windows

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)  
**Chuyên mục**: Kiến trúc | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 2 -->
2
Nội dung
Giới thiệu
Lập trình căn bản
Các kiểu dữ liệu phức
Lập trình hướng đối tượng
Vào/ra, ngoại lệ
Lập trình mạng
Lập trình Web
Python-MySQL
Giao diện GUI
Vẽ đồ thị

<!-- page: 3 -->
3
Nội dung
Giới thiệu
Lập trình căn bản
Các kiểu dữ liệu phức
Lập trình hướng đối tượng
Vào/ra, ngoại lệ
Lập trình mạng
Lập trình Web
Python-MySQL
Giao diện GUI
Vẽ đồ thị

<!-- page: 4 -->
4
Giới thiệu Python
Python là ngôn ngữ lập trình cấp cao, tương tác, thông 
dịch, hướng đối tượng
Do Guido van Rossum đề xuất từ 1985 – 1990
Mã nguồn Python: giấy phép GNU General Public 

<!-- page: 2 -->

License (GPL)
Python sẵn dùng trên Unix, Linux, Mac OS, Windows
Top 5 ngôn ngữ lập trình phổ biến
Được sử dụng bởi các tổ chức tập đoàn như Wikipedia, 
Google, Yahoo!, CERN

<!-- page: 5 -->
5
Giới thiệu Python
Dễ học (Easy-to-learn)
Dễ đọc (Easy-to-read)
Dễ bảo trì (Easy-to-maintain)
Thư viện chuẩn (standard library): tương thích UNIX, 
Linux, Windows và Mac
Chế độ tương tác: thực thi, kiểm tra, gỡ rối 
Khả chuyển (Portable): phần cứng, hệ điều hành
Khả năng mở rộng (Extendable): thêm mô-đun 
Kết nối với các hệ quản trị CSDL
Lập trình giao diện đồ họa GUI
Quy mô chương trình (Scalable)

<!-- page: 6 -->
6
Giới thiệu Python
Python được sử dụng trong giảng dạy, 
Tính toán khoa học, 
Công nghệ sinh-tin học, 
Phát triển ứng dụng Web, 
Lập trình ứng dụng mạng, nghiên cứu an ninh mạng, 
Kỹ thuật đồ họa, xử lý ảnh và thị giác máy tính, 
Máy học và khai thác dữ liệu, xử lý ngôn ngữ tự nhiên, 
trí tuệ nhân tạo
Lập trình nhúng, 
Quản trị hệ thống, 
Lập trình trò chơi, v.v.

<!-- page: 7 -->
7

<!-- page: 8 -->
8
Nội dung
Giới thiệu
Lập trình căn bản
Các kiểu dữ liệu phức

<!-- page: 3 -->

Lập trình hướng đối tượng
Vào/ra, ngoại lệ
Lập trình mạng
Lập trình Web
Python-MySQL
Giao diện GUI
Vẽ đồ thị

<!-- page: 9 -->
9
Trình thông dịch Python

<!-- page: 10 -->
10
Thực thi chương trình Python
Soạn thảo chương trình: PyCharm, Geany, notepad++, 
Nano, Gedit, v.v.
 
Chương trình hello.py
#!/usr/bin/python3
print('Hello World!')
Thực thi hello.py

<!-- page: 11 -->
11
Cú pháp
Phân biệt ký tự thường hoa 
Các từ khóa của Python được
and
exec
not
as
finally
or
assert
for
pass
break
from
print
class
global
raise
continue
if

<!-- page: 4 -->

return
def
import
try
del
in
while
elif
is
with
else 
lambda 
yield
except

<!-- page: 12 -->
12
Cú pháp
Sử dụng # để chú thích 1 dòng trong chương trình
# comment
Sử dụng ’’’ để chú thích 1 đoạn 
'''
print("We are in a comment")
print('We are still in a comment')
'''
Dấu ’ và "
word = 'word'
sentence = "This is a sentence."
message = """This message will
... span several lines."""
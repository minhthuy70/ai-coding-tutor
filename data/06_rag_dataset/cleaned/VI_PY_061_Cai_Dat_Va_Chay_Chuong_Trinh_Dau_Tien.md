# VI_PY_061: Cài đặt môi trường và viết chương trình Python đầu tiên

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn
**Chuyên mục**: Cơ bản | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

Giới thiệu
Hiện nay, Python là một trong những ngôn ngữ lập trình
đang được chú ý bởi tính đa dạng về ứng dụng, thư viện
phong phú và cộng đồng đông đảo.
Đã làm việc với PHP 10 năm, và có những tác vụ mà PHP
khó mà thực hiện tối ưu được, khiến mình phải tiếp cận với
Python trong giai đoạn này.
Cuốn sách nhỏ này được viết trong quá trình mình bắt đầu
học Python và giải quyết các bài toán cơ bản theo nhu cầu
của mình.
Hy vọng những ghi chép của mình cũng sẽ giúp ích cho
những ai đang quan tâm đến việc ứng dụng Python vào
công việc và xử lý hiện tại.
Mục lục
Sách được chia làm 15 chương, mỗi chương sẽ trình bày 1
khía cạnh của Python mà mình sẽ gặp phải và sẽ hữu ích

khi biết các kiến thức này trong việc áp dụng Python vào
công việc trong tương lai.
1. Hello world
2. Cú pháp
3. Phân chia module
4. Class
5. Thao tác trên tập tin
6. Xử lý hình ảnh
7. Xử lý file JSON
8. Xử lý file XML
9. Kết nối MySQL
10. Kết nối Redis
11. Kết nối Memcached
12. Kết nối RabbitMQ
13. Restful Client
14. Gởi email với SMTP

15. Socket Programming

Tác giả
Tên: Võ Duy Tuấn
Email: tuanmaster2012@gmail.com
Facebook: https://www.facebook.com/voduytuan

Chương 1. Hello world
Python là một ngôn ngữ phiên dịch (Interpreter Language),
tức là không cần build thành file thực thi mà chạy trực tiếp
như PHP.
Hiện tại Python có 2 nhánh chính là 2.x và 3.x. Ở nhánh 2.x
đã dừng phát triển và đang đứng ở phiên bản 2.7. Nhánh
Python 3.x thì vẫn đang được tiếp tục phát triển.
Website chính thức của Python: www.python.org
Cài đặt
Python hỗ trợ hầu hết các nền tảng và rất dễ tìm thấy sẵn
trên một số hệ điều hành như Mac OS…
Để biết là hệ thống của bạn đã cài Python chưa, có thể vào
màn hình command line và gõ:
$ python --version

Nếu đã cài đặt python thì sẽ hiển thị thông tin phiên bản
python. Nếu báo lỗi thì đồng nghĩa với bạn chưa cài đặt
Python.
Có thể tham khảo cách cài đặt Python tại:
https://www.python.org/downloads/
Công cụ phát triển
Chỉ cần dùng một text editor là bạn có thể viết được code
python hoặc có thể dùng các công cụ cao cấp hơn (IDE)
như Aptana, PyCharm…Các IDE thường hỗ trợ thêm quá
trình phân tích cú pháp dòng lệnh, debug…trong phạm vi
cuốn sách nhỏ này thì mình hướng đến cách thực thi
python bằng dòng lệnh.
Hello world
Tạo một file có tên là helloworld.py và có nội dung như
sau:
print 'Hello world'

print là lệnh cơ bản nhất để xuất một biến ra (thường là
màn hình)

Sau đó, vào màn hình command line, di chuyển đến thư
mục chứa file này và gõ.
$ python helloworld.py
Nếu thấy xuất hiện dòng chữ Hello world tức là bạn đã
hoàn thành việc viết ứng dụng python đầu tiên.

Chương 2. Cú pháp
2.1. Biến số
Khai báo biến bằng một câu lệnh gán.
a = 1
bạn có thể gán nhiều loại giá trị (số, chuỗi) cho một biến.
a = 1
a = 'Hello World'
a = [1, 2, 3]
a = [1.2, 'Hello', 'W', 2]
2.2. Toán tử số học
Python cũng hỗ trợ một số toán tử toán học thông dụng
như:
+ phép cộng

- phép trừ
* phép nhân
/ phép chia
% phép chia lấy dư (modulo)
2.3. Boolean và Toán tử logic
Giá trị đúng và sai tương ứng là True và False .
not để đảo giá trị.
and phép tính logic và (AND)
or phép tính logic hoặc (OR)
Một số phép so sánh thông thường như < (bé hơn), <= (bé
hơn hoặc bằng), > (lớn hơn), >= (lớn hơn hoặc bằng), ==
(bằng), != (khác) để so sánh 2 giá trị.
Hỗ trợ dạng so sánh kép như:
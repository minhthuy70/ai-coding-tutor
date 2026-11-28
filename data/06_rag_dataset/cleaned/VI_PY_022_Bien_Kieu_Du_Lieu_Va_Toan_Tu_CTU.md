# VI_PY_022: Biến, kiểu dữ liệu nguyên thủy, ép kiểu và toán tử số học trong Python 3

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)
**Chuyên mục**: Căn bản | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

14
Cú pháp
Lệnh được viết trên nhiều dòng sử dụng ký tự \
total = item_one + \
        item_two + \
        item_three
Lệnh được bao bằng các cặp dấu ngoặc: [], {}, ()
không cần phải sử dụng ký tự \ để tiếp tục dòng
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
Dấu ; để cách nhiều lệnh trên dòng
import sys; x = 'foo'; sys.stdout.write(x + '\n')

15
Cú pháp
Nhóm nhiều câu lệnh đơn tạo nên một khối lệnh và
cũng được gọi là bộ (suites)
Các lệnh phức như if, while, def và class cần một dòng
header và một bộ
Dòng header bắt đầu câu lệnh (bằng một từ khoá
tương ứng ví dụ như if, def, …) và kết thúc bằng dấu
hai chấm : theo sau là một suite
def hi(name):
print('Hello ' + name)
print('Have a good day!')
hi('nghi')

16
Lệnh print trong Python

17

Lệnh input trong Python

18
Biến, kiểu cơ bản, phép toán
Tên: ký tự bắt đầu phải là alphabet hoặc _
Không cần khai báo, chỉ gán giá trị (sử dụng dấu =)
Được tạo ra trong lần đầu gán giá trị
Phạm vi biến: cục bộ, toàn cục
Tham khảo đến đối tượng
Thông tin về kiểu gắn liền với đối tượng
Kiểu cơ bản: int, float, complex, bool, string
Các phép toán số học: +, -, *, /, %, **
Phép toán so sánh: ==, !=, >, >=, <, <=
Phép toán luận lý: and, or, not

19
Biến, kiểu cơ bản, phép toán

20
Biến, kiểu cơ bản, phép toán

21
Biến, kiểu cơ bản, phép toán

22
Biến, kiểu cơ bản, phép toán

23
Biến, kiểu cơ bản, phép toán

24
Cấu trúc điều khiển
Cấu trúc rẽ nhánh if
  if (cond1):
  elif (cond2):
  else:
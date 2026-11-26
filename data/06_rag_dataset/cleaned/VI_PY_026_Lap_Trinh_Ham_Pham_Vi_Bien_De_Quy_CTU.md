# VI_PY_026: Lập trình hàm, phạm vi biến LEGB, tham số và giải thuật đệ quy

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)
**Chuyên mục**: Hàm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

62
Định nghĩa chồng phép toán

63
Thuộc tính có tên bắt đầu __ là thuộc tính
ẩn bên trong đối tượng

64
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

65
Vào/ra
Lệnh print, input

66
Vào/ra tập tin
Hàm
file_obj = open(file_name [, access_mode][, buffering])
file_obj.close()
file_obj.write(string);

file_obj.read([count]);
file_obj.tell()
file_obj.seek(offset[, from])
import os
os.rename(current_file_name, new_file_name)
os.remove(file_name)
os.mkdir("newdir")
os.chdir("newdir")
os.getcwd()
os.rmdir('dirname')

67
Vào/ra tập tin

68
Vào/ra tập tin

69
Vào/ra tập tin

70
Ngoại lệ
Lệnh
assert Expression[, Arguments]
raise [Exception [, args [, traceback]]]
try:
   You do your operations here;
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
else:
   If there is no exception then execute this block.
finally:
   This would always be executed.

71
Ngoại lệ

72
Ngoại lệ
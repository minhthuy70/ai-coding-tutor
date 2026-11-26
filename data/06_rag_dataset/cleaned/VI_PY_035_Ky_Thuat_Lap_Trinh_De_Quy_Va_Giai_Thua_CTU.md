# VI_PY_035: Kỹ thuật lập trình đệ quy: Bản chất ngăn xếp hệ thống call stack

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)
**Chuyên mục**: Hàm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

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
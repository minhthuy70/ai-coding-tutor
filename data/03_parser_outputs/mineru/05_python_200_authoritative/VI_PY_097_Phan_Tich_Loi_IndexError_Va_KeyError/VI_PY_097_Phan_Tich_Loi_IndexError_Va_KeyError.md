<!-- page: 1 -->
# VI_PY_097: Phân tích lỗi tràn chỉ số IndexError và truy xuất sai khóa KeyError

**Nguồn tài liệu chính thống**: Cẩm nang Chẩn đoán & Gỡ lỗi Python ĐH  
**Chuyên mục**: Gỡ lỗi | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 46 -->
r+ : mở để đọc và ghi. Con trỏ nằm ở đầu file.
w+ : mở để đọc và ghi. Ghi đè nếu file đã tồn tại, nếu
file chưa tồn tại thì tạo file mới để ghi.
a+ : mở để đọc và thêm vào cuối file. Con trỏ nằm ở
cuối file. Nếu file chưa tồn tại thì tạo file mới để ghi.
Mặc định là mở file text, nếu muốn mở file nhị phân
(binary) thì thêm b , ví dụ: rb , wb , ab , rb+ , wb+ , ab+ .
Ví dụ:
f1 = open('test.txt', 'r')
f2 = open('access_log', 'a+'
Sau khi gọi hàm open() thành công thì sẽ trả về một
object có các thuộc tính:
closed : True nếu file đã đóng
mode : chế độ khi mở file
name : tên của file
softspace : cờ đánh dấu softspace khi dùng với hàm

<!-- page: 47 -->
print
5.1.2. Đọc nội dung từ file
Sau khi file đã mở ở chế độ đọc thì gọi phương thức
read([count]) để trả về toàn bộ nội dung của file. Ví dụ:
f1 = open('test.txt', 'r')
data = f1.read();
Hàm read() có nhận một tham số là số lượng byte muốn
đọc. Nếu không truyền vào thì sẽ đọc hết nội dung của file.
Ví dụ:
f2 = open('log.txt', 'r')
buffdata = f2.read(1024)
5.1.3. Ghi nội dung vào file
Nếu file được mở ở chế độ có thể ghi thì có thể dùng
phương thức write() để ghi một nội dung vào file. Ví dụ:

<!-- page: 48 -->

<!-- page: 2 -->

f2 = open('access_log', 'a+')
f2.write('Attack detected')
5.1.4. Đóng file đã mở
Sau khi hoàn tất các thao tác đọc ghi file thì gọi phương
thức close() để đóng file đã mở. Ví dụ:
f1.close()
f2.close()
5.1.5. Đổi tên file
Sử dụng phương thức os.rename(old, new) để đổi tên
một file. Ví dụ:
import os
os.rename('test.txt', 'test_new.txt')
5.1.6. Xóa file
Sử dụng phương thức os.remove(file) để xóa một file

<!-- page: 49 -->
khỏi hệ thống. Ví dụ:
import os
os.remove('test.txt')   
5.2. Thư mục (Directory)
5.2.1. Tạo thư mục
Sử dụng phương thức os.mkdir(dir) để tạo thư mục. Ví
dụ:
import os
os.mkdir('test')
5.2.2. Xóa thư mục
Sử dụng phương thức os.rmdir(dir) để xóa một thư mục.
Ví dụ:
import os
os.rmdir('test')

<!-- page: 50 -->
5.2.3. Đọc nội dung thư mục
Sử dụng phương thức os.listdir(dir) để lấy danh sách
tập tin, thư mục của thư mục dir . Khi gọi sẽ trả về một
mảng danh sách các tập tin, thư mục. Ví dụ:
import os
allfiles = os.listdir('/root/downloads')
print allfiles  
5.3. Module os
Module os là một module có nhiều phương thức hữu ích
trong việc làm việc với các file và directory, như:
os.chdir(path) : đổi thư mục hiện hành
os.getcwd() : trả về thư mục hiện hành
os.chmod(path, mode) : CHMOD một đường dẫn

<!-- page: 3 -->

os.chown(path, uid, gid) : CHOWN một đường dẫn
os.makedirs(path[, mode]) : tạo đường dẫn (có
recursive)
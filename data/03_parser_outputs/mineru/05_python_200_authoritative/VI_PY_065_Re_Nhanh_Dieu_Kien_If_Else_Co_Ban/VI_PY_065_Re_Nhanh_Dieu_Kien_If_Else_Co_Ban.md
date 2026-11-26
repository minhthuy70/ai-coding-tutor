<!-- page: 1 -->
# VI_PY_065: Rẽ nhánh điều kiện if...else và tư duy logic cho người mới học

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn  
**Chuyên mục**: Điều khiển luồng | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 42 -->
name = ''
    age = 0
```python
def __init__(self, name = '', age = 0):
    self.name = name
    self.age = age
def show(self):
    print 'My name is ', self.name
def run(self):
    print 'Animal is running...'
def go(self):
    print 'Animal is going...'

    
```
class dog(animal):
```python
def run(self):
    print 'Dog is running...'
    
```
myanimal = animal()
myanimal.show()
myanimal.run()
myanimal.go()
    
mydog = dog('Lucy')
mydog.show()
mydog.run()
mydog.go()

<!-- page: 43 -->
Sau khi thực thi sẽ cho ra kết quả:
My Name is

<!-- page: 2 -->

Animal is running...
Animal is going...
My Name is Lucy
Dog is running...
Animal is going...
Trong ví dụ trên thì:
animal và dog là 2 class. Trong đó class dog kế thừa
từ class cha là animal nên sẽ có các phương thức của
class animal .
name và age là thuộc tính (Attribute) của class.
Phương thức __init__(self) là hàm tạo của class.
Hàm này sẽ được gọi mỗi khi có một object mới được
tạo (từ một class), gọi là quá trình tạo instance.
show() , run() và go() là 2 phương thức của 2 class.
Khi khai báo phương thức có kèm tham số self dùng
để truy cập ngược lại object đang gọi. Lúc gọi phương

<!-- page: 44 -->
thức thì không cần truyền tham số này.
Phương thức run() của class dog gọi là override
của phương thức run() của class animal .

<!-- page: 45 -->
Chương 5. Thao tác trên tập tin
và Thư mục
Nội dung chương này sẽ hướng dẫn các thao tác liên quan
đến tập tin và thư mục.
5.1. Tập tin (File)
5.1.1. Mở file
Trước khi muốn đọc hoặc ghi file, bạn cần có thao tác mở
file theo cú pháp:
fh = open(filepath, mode)
Trong đó, filepath là đường dẫn của file sẽ mở và mode
là chế độ để mở. Có một số chế độ là:
r : mở để đọc nội dung (mặc định)
w : mở để ghi nội dung
a : mở để ghi thêm nội dung vào cuối file.

<!-- page: 46 -->
r+ : mở để đọc và ghi. Con trỏ nằm ở đầu file.
w+ : mở để đọc và ghi. Ghi đè nếu file đã tồn tại, nếu
file chưa tồn tại thì tạo file mới để ghi.
a+ : mở để đọc và thêm vào cuối file. Con trỏ nằm ở
cuối file. Nếu file chưa tồn tại thì tạo file mới để ghi.
Mặc định là mở file text, nếu muốn mở file nhị phân

<!-- page: 3 -->

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

<!-- page: 4 -->

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
os.chown(path, uid, gid) : CHOWN một đường dẫn
os.makedirs(path[, mode]) : tạo đường dẫn (có
recursive)
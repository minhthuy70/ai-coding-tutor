# VI_PY_066: Vòng lặp while, for và ứng dụng hàm range() trong thực hành

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn
**Chuyên mục**: Vòng lặp | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

os.path.getmtime(path) : trả về thời gian chỉnh sửa
cuối cùng
os.path.getctime(path) : trả về thời gian chỉnh sửa
cuối của metadata trên một số hệ thống. Hoặc trả về
thời gian tạo file trên Windows.
Xem thêm tại
https://docs.python.org/2/library/os.path.html

Chương 6. Xử lý hình ảnh
Sử dụng thư viện Pillow (PIL Fork) để tiến hành các thao
tác xử lý hình ảnh đơn giản như resize, crop, rotate…
6.1. Cài đặt PIL
Vào trang web sau để download / cài đặt package PIL cho
python của bạn
http://pillow.readthedocs.org/en/latest/installation.html
Sau khi cài đặt thì có thể sử dụng các module trong
package IPL
from PIL import Image
6.2. Mở file
from PIL import Image
im = Image.open("photo.jpg")

Sau khi mở file hình thành công thì có thể thao tác trên đối
tượng im .
6.3. Ghi file
Từ đối tượng Image có thể lưu file xuống máy tính bằng
phương thức save(path, type) . Ví dụ:
im.save('photo_new.jpg', 'JPEG')
6.4. Tạo thumbnail
Sử dụng phương thức thumbnail như sau:
from PIL import Image

im = Image.open('photo.jpg')
im.thumbnail((100, 100))
im.save('photo_thumbnail.jpg', 'JPEG')
thumbnail không trả về image mới mà thực hiện trên
object image đang gọi.

6.5. Các thao tác xử lý hình ảnh
Tham khảo thêm thư viện PIL tại:
http://pillow.readthedocs.org/en/latest/index.html

Chương 7. Xử lý file JSON
JSON là một trong những định dạng file trao đổi dữ liệu
thông dụng nhất hiện nay. Với kiến trúc đơn giản và tương
đồng với cấu trúc của Python nên việc thao tác JSON trên
Python rất dễ hiểu.
7.1. Load file từ Internet
Thông thường dữ liệu JSON được lấy từ nguồn khác (như
file, internet..) nên chương này sẽ bắt đầu bằng cách
hướng dẫn download một file JSON từ Internet và sau đó
mới parsing nội dung JSON download.
Sử dụng module urllib2 để download file và module
json để encode/decode JSON data. Ví dụ:

import urllib2
import json

response = urllib2.urlopen('https://api.github.com/
users/voduytuan/repos')

data = json.load(response)

print data
Ví dụ trên sẽ truy vấn đường dẫn
https://api.github.com/users/voduytuan/repos để lấy danh
sách Repository trên Github của mình dưới định dạng
JSON. Sau đó, sẽ được
7.2. Parsing JSON Data
Nếu như bạn đã có JSON data dưới dạng chuỗi, muốn
parsing chuỗi này thành Data thì sử dụng như cách dưới
đây:

import json
mystring = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
data = json.loads(mystring)
print data
(Hiển thị: {u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd
': 4})
7.3. Encoding JSON Data
Nếu như bạn đã có một biến và muốn encode thành JSON
string thì có thể dùng theo cách sau:
import json

mydata = {
    'name': 'John',
    'age': 10
}
jsonstring = json.dumps(mydata)
print jsonstring
(hiển thị: {"age": 10, "name": "John"})

Chương 8. Xử lý file XML
Trong phần này, chúng ta sẽ parsing nội dung XML thành
dữ liệu để xử lý. Để xử lý XML, ta sẽ sử dụng thư viện
Beautifulsoup 4. Đây là một thư viện giúp việc triển khai
việc parsing html, xml được nhanh chóng và tiện lợi.
8.1. Cài đặt Beautifulsoup
Bạn có thể tham khảo hướng dẫn cách cài đặt tại website
http://www.crummy.com/software/BeautifulSoup/bs4/doc
beautiful-soup.
Trên MacOS, có thể cài bằng pip như sau:
$ sudo pip install beautifulsoup4
8.2. Cài đặt lxml parser
Để parsing xml từ beautifulsoup, tao sử dụng bộ parser
xml có tên là lxml . Xem hướng dẫn cài đặt tại

http://www.crummy.com/software/BeautifulSoup/bs4/doc
a-parser
Trên MacOS, có thể cài bằng pip như sau:
sudo pip install lxml
8.3. Ví dụ về parsing XML
Cho ví dụ sau:
from bs4 import BeautifulSoup as Soup
note = '''
<?xml version="1.0" encoding="UTF-8"?>

<breakfast_menu>
    <food>
        <name>Belgian Waffles</name>
        <price>$5.95</price>
        <description>Two of our famous Belgian Waff
les with plenty of real maple syrup</description>
        <calories>650</calories>
    </food>
    <food>
<name>Strawberry Belgian Waffles</name>
<!-- page: 1 -->
# VI_PY_067: Cấu trúc từ điển Dictionary: Lưu trữ và tra cứu theo khóa key-value

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn  
**Chuyên mục**: Cấu trúc dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 62 -->
Trong ví dụ có một số cách truy xuất đến các phần tử như:
findAll() : trả về mảng các thẻ có tên cần tìm
find() : trả về phần tử đầu tiên có tên cần tìm
Truy xuất trực tiếp thông qua tên thẻ như
x.price.string
8.4. Parsing HTML
Tương tự như xml , BeautifulSoup có thể parsing nội dung
HTML thông qua hàm khởi tạo và chọn html ở tham số
thứ 2.
...
soup = Soup(websitehtml, 'html')

<!-- page: 63 -->
Chương 9. Kết nối MySQL
MySQL là một hệ cơ sở dữ liệu quan hệ phổ biến nhất hiện
nay. Rất nhiều ngôn ngữ có thể kết nối đến MySQL và
Python cũng không ngoại lệ.
Mặc định Python không có thư viện để kết nối đến MySQL
server. Trong phần này, để kết nối đến MySQL Server từ
Python, chúng ta sẽ sử dụng module MySQLdb
9.1. Cài đặt MySQLdb
Cài đặt thông qua pip như sau:
$ sudo pip install MySQL-python
Tham khảo thêm tại: https://pypi.python.org/pypi/MySQL-
python/1.2.5
Khai báo module MySQLdb là có thể sử dụng.

<!-- page: 64 -->
import MySQLdb
Trong một số trường hợp đã cài MySQLdb nhưng import
báo lỗi thiếu file libmysqlclient.18.dylib . Nguyên nhân
có thể là do hiện tại đường dẫn đến file không tồn tại. Thử
tạo symlink hoặc sử dụng câu lệnh sau để tạo symlink từ
file libmysqlclient.18.dylib đến thư mục /usr/lib/

<!-- page: 2 -->

$ sudo ln -s /usr/local/mysql/lib/libmysqlclient.18
.dylib /usr/lib/libmysqlclient.18.dylib
9.2. Kết nối đến MySQL Server
Bạn cần có một MySQL server đang chạy và cho kết nối
đến. Trong trường hợp này là localhost nên không cần cấu
hình đặc biệt, chỉ cần cung cấp username và password là
có thể kết nối đến MySQL Server.
Thực hiện gọi hàm như sau để trả về kết nối:

<!-- page: 65 -->
import MySQLdb
    
dbcon = MySQLdb.connect(host = 'localhost', user = 
'myusername', passwd = 'mypassword', db = 'mydbname
')
Nếu kết nối không thành công thì sẽ báo lỗi và ngưng
chương trình. Cách kết nối an toàn là đưa vào trong try
để bắt lỗi như sau:

<!-- page: 66 -->
import MySQLdb
    
db = None
    
try:
    db = MySQLdb.connect(host = 'localhost', user =
 'root', passwd = 'root', db = 'mysql')
    
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
if db:
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database version : %s " % ver
9.3. Kết nối với charset utf8
Mặc định kết nối đến MySQL server là charset latin nên
khi lấy dữ liệu unicode thì hiển thị Tiếng Việt không đúng,
bạn cần phải chọn charset là utf8 khi tạo kết nối. Cú pháp
như sau:

<!-- page: 67 -->
...

<!-- page: 3 -->

db = MySQLdb.connect(host = 'localhost', user = 'ro
ot', passwd = 'root', db = 'test', charset = 'utf8'
)
9.4. Query dữ liệu
Để truy vấn dữ liệu (chạy câu lệnh SQL) thì sử dụng cursor
của MySQLdb. Ví dụ:
import MySQLdb
    
db = MySQLdb.connect(host = 'localhost', user = 'ro
ot', passwd = 'root', db = 'mysql');
cursor = db.cursor()
sql = 'SELECT * FROM user'
cursor.execute(sql)
myusers = cursor.fetchall()
Ví dụ dữ liệu biến myusers là: ((1, 'John'), (2, 'Doe'))
Mặc định, cursor sẽ trả về mỗi dòng dữ liệu từ MySQL
theo kiểu tuple , tức là không có key. Nếu bạn muốn trả về

<!-- page: 68 -->
kiểu Dictionary thì có thể khai báo:
import MySQLdb
db = MySQLdb.connect(host = 'localhost', user = 'ro
ot', passwd = 'root', db = 'mysql')
cursor = db.cursor(MySQLdb.cursors.DictCursor)
...
9.5. Fetch dữ liệu
Có một số cách để fetch dữ liệu thông dụng từ cursor sau
khi đã exectute(sql) là fetchone() và fetchall() .
fetchone() : chỉ fetch một dòng dữ liệu. Nếu muốn
fetch nhiều dòng dữ liệu thì có thể gọi nhiều lần, mỗi
lần sẽ trả về một dòng dữ liệu. Tốt cho trường hợp truy
vấn rất nhiều dữ liệu một lúc. Nếu trả về None tức là
đã fetch hết dữ liệu từ câu truy vấn.
fetchall() : fetch toàn bộ dữ liệu truy vấn được từ
câu truy vấn và trả về một tuple chứa các dòng dữ

<!-- page: 69 -->
liệu. Mỗi phần tử của Tuple có thể là một Tuple khác
hoặc là một Dictionary tùy theo cài đặt ở bước lấy
cursor (Xem phần 9.4).
fetchmany(size) : nằm ở giữa 2 kiểu fetch trên, có thể
quy định số lượng row trong mỗi lần fetch. Nếu fetch
hết thì trả về Tuple rỗng.
9.6. Đóng kết nối
Sau khi kết nối và truy vấn thì có thể đóng kết nối theo ví

<!-- page: 4 -->

dụ sau:
import MySQLdb
db = MySQLdb.connect(...)
db.close()
Ngoài ra, bạn cũng nên đóng cursor khi không còn sử
dụng theo ví dụ:

<!-- page: 70 -->
import MySQLdb
    
db = MySQLdb.connect(...)
cursor = db.cursor()
cursor.close()
db.close()
9.7. Prepared Statement
Prepared statement là kỹ thuật tham số hóa các dữ liệu
truyền vào câu truy vấn thay vì nối chuỗi trực tiếp để xây
dựng một chuỗi truy vấn dài. Kỹ thuật này được áp dụng
nhiều và giúp tăng hiệu quả và tính bảo mật của câu truy
vấn. Ví dụ:
...
cur.execute("UPDATE Writers SET Name = %s WHERE Id 
= %s", ("John", "4")) 
...
Mỗi tham số truy vấn sẽ được thay thế bằng %s và phương
thức execute() sẽ có tham số thứ 2 là một Tuple có giá trị
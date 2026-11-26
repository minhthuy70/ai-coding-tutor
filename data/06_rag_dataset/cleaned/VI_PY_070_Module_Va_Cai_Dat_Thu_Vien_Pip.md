# VI_PY_070: Khái niệm Module và cài đặt thư viện ngoài qua công cụ pip

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn
**Chuyên mục**: Mô-đun | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

Chương 14. Gởi email với SMTP
SMTP là giao thức gởi mail thông dụng hiện nay. Python hỗ
trợ mặc định thư viện smtplib dùng để kết nối đến một
SMTP Server và gởi email. Tuy nhiên, việc sử dụng thư
viện này sẽ gây khó khăn cho việc định dạng và sử dụng
nên chúng ta sẽ sử dụng thư viện sender , là một thư viện
giúp định dạng và gởi email đơn giản hơn.
14.1. Cài đặt sender
Cài đặt từ pip như sau:
\$ sudo pip install sender
14.2. Gởi email đơn giản
Để gởi 1 email với sender , bạn cần có tài khoản và một số
thông tin của SMTP Server trước khi gởi. Ví dụ đoạn code
để gởi 1 email từ SMTP Server của Amazon.

from sender import Mail, Message

mail = Mail(
    "smtp.gmail.com",
    port = 465,
    username = "example@gmail.com",
    password = "yourpassword",
    use_tls = False,
    use_ssl = True,
    debug_level = False
)

msg = Message("msg subject")
msg.fromaddr = ("Vo Duy Tuan", "example@gmail.com")
msg.to = "destuser@gmail.com"
msg.body = "this is a msg plain text body"
msg.html = "<b>this is a msg text body</b>"
msg.reply_to = "example@gmail.com"

msg.charset = "utf-8"
msg.extra_headers = {}
msg.mail_options = []
msg.rcpt_options = []

# Send message
mail.send(msg)

14.3. Gởi email có đính kèm file
Bạn cần sử dụng thêm class Attachment để tạo
attachment.
from sender import Mail, Message, Attachment
mail = Main(...)
msg = Message(..)
...

# Open attached file and create Attachment object
with open("photo01.jpg") as f:
    file01 = Attachment("photo01.jpg", "image/jpeg"
, f.read())

msg.attach(file01)

# Send message
mail.send(msg)
14.4. Tìm hiểu thêm
Bạn có thể tìm hiểu thêm về thư viện sender tại website

chính thức tại địa chỉ http://sender.readthedocs.org/

Chương 15. Socket
programming
Chương này sẽ ví dụ việc xây dựng một môi trường Client -
Server sử dụng Socket. Server sẽ lắng nghe trên một port
(12345) và khi client kết nối vào sẽ thông báo hiển thị
thông tin của client (IP và Port) và gởi 1 message xuống
cho client.
15.1. Server side
Tạo file server.py với nội dung bên dưới.

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
   c, addr = s.accept()
   print 'Got connection from', addr

```python
c.send('Thank you for connecting')
c.close()
```

Đoạn code trên khi thực thi sẽ chạy và lắng nghe ở port
TCP 12345. Mỗi khi có một kết nối từ client sẽ hiện ra
thông báo kết nối từ IP và Port nào, ví dụ: Got connection
from Got connection from ('192.168.1.104', 60018) .
Sau đó, gởi trả một message với nội dung Thank you for
connecting về cho client. Sau đó, đóng kết nối với client.
15.2. Client side

Tạo file client.py với nội dung bên dưới.
import socket

s = socket.socket()
host = '127.0.0.1'
port = 12345

s.connect((host, port))
print s.recv(1024)
s.close
Đoạn code trên sẽ kết nối đến một socket server thông
qua hostname lấy được từ phương thức
socket.gethostname() và port 12345. Sau khi kết nối, sẽ
hiển thị ra kết quả trả về từ server. Sau đó thì đóng kết nối.
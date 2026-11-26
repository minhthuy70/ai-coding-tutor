# VI_PY_069: Đọc và ghi tệp tin trên ổ đĩa với phương thức open() an toàn

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn
**Chuyên mục**: Tệp tin | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

13.2. Request
Hỗ trợ sẵn các phương thức tương ứng cho Http request
như GET, POST, PUT, DELETE…
import requests

r = requests.get('https://api.github.com/events')
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
13.2.1. GET Query string
Đối với các request GET , có thể truyền tham số đường dẫn
thông qua tham số params khi gọi phương thức get() . Ví
dụ:

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params =
 payload)
print(r.url)
(Hiển thị: http://httpbin.org/get?key2=value2&key1=
value1)
13.2.2. Request Body
Trong hầu hết trường hợp các request như POST, PUT
thương cần truyền dữ liệu khi request, có thể sử dụng tham
số data để truyền data lên kèm request. Ví dụ:
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data =
 payload)

13.2.3. Upload file

Có thể gởi thêm tham số files để upload file kèm theo
request. Ví dụ:
import requests

url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
13.3. Response
Sau khi gọi các phương thức tương ứng để request, bạn sẽ
có đối tượng thuộc class Response . Đối tượng này có một
số thông tin như sau:
status_code : HTTP Status server trả về
headers : Các thông tin header mà server trả về dưới
dạng Dictionary.
cookies : Nếu server có trả về cookie thì có thể sử
dụng thuộc tính này để lấy các cookie.
text : Trả về nội dung response

Tham khảo về các tính năng khác của thư viện requests
tại website chính thức. http://docs.python-requests.org

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
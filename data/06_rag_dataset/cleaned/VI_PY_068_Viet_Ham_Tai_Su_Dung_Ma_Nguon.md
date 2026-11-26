# VI_PY_068: Viết hàm tự định nghĩa và tái sử dụng mã nguồn hiệu quả

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn
**Chuyên mục**: Hàm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

Chương 10. Kết nối Redis
Redis là một memory cache server hỗ trợ persistant data
thông dụng nhất hiện nay. Nội dung chương này sẽ hướng
dẫn bạn kết nối đến một Redis server (đã được cài đặt
sẵn) thông qua thư viện redis-py.
10.1. Cài đặt
Có thể xem thêm về hướng dẫn cài đặt thư viện này tại
https://github.com/andymccurdy/redis-py
Đơn giản cài thông qua pip là:
\$ sudo pip install redis
10.2 Kết nối đến Redis
Để kết nối đến Redis server thì bạn có thể xem ví dụ sau:

import redis
r = redis.StrictRedis(host='localhost', port=6379,
db=0)
10.3. Thực hiện lệnh
Thực hiện các lệnh bình thường trên đối tượng redis. Ví dụ:
import redis
r = redis.StrictRedis(...)
r.set('foo', 'bar')
print r.get('foo')
(Hiển thị 'bar')
10.4. Pipeline
Pipeline là kỹ thuật được dùng trong trường hợp bạn muốn
tăng performance bởi gộp nhiều lệnh vào một request thay
vì mỗi lệnh là một request như thông thường. Xem ví dụ
sau để hiểu cách sử dụng pipeline bằng redis-py :

import redis
r = redis.StrictRedis(...)
r.set('foo', 'bar')

pipe = r.pipeline()
pipe.set('a', 1)
pipe.set('b', 2)
pipe.set('c', 3)
pipe.get('foo')
pipe.execute()
Sau khi gọi phương thức execute() thì sẽ trả về List tương
ứng với các kết quả của từng lệnh. Ví dụ kết quả từ đoạn
code trên:
[True, True, True, 'bar']

Chương 11. Kết nối
Memcached
Memcached là một memory cache server thông dụng hiện
nay. Nội dung chương này sẽ hướng dẫn bạn kết nối đến
một Memcached server (đã được cài đặt sẵn) thông qua
thư viện pylibmc .
11.1. Cài đặt
Có thể xem thêm về hướng dẫn cài đặt thư viện này tại
http://sendapatch.se/projects/pylibmc/install.html
Đơn giản cài thông qua pip là:
\$ sudo pip install pylibmc
11.2 Kết nối đến Memcached Server
Để kết nối đến Memcached server thì bạn có thể xem ví dụ
sau:

import pylibmc
mc = pylibmc.Client(["127.0.0.1"], binary=True, beh
aviors={"tcp_nodelay": True, "ketama": True})
10.3. Thực hiện lệnh
Thực hiện các lệnh bình thường trên đối tượng memcache.
Ví dụ:
import pylibmc
mc = pylibmc.Client(...)
mc.set('foo', 'bar')
print mc.get('foo')
(Hiển thị 'bar')

Chương 12. Kết nối RabbitMQ
RabbitMQ là một phần mềm cho phép xây dựng Message
Queue theo protocol AMQP và khá thông dụng trên thế
giới. Để kết nối đến RabbitMQ trên Python, ta sẽ sử dụng

thư viện pika .
12.1. Cài đặt
Có thể xem thêm về hướng dẫn cài đặt thư viện này tại
https://pika.readthedocs.org/en/0.10.0/
Đơn giản cài thông qua pip là:
\$ sudo pip install pika
12.2 Gởi một message đến Server -
Provider
Ví dụ để gởi một message đến server

import pika
connection = pika.BlockingConnection(pika.Connectio
nParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hel
lo', body='Hello World!')
print " [x] Sent 'Hello World!'"

connection.close()
Để gởi một message, chúng ta cần kết nối đến server và
khai báo một channel, ở đây là channel có tên là hello .
Sau khi khai báo channel, tao tiến hành gởi message có
nội dung Hello World! thông qua channel này, kèm theo
khai báo routing_key là hello . Routing Key sẽ giúp điều
hướng message này đến đúng các worker được khai báo
nhận message theo routing key (Consumer)
12.3. Nhận message - Consumer

Ở bước trước, ta đã tạo một message lên queue. Ở bước
này, ta sẽ khai báo một worker xử lý các message nhận
được từ channel hello .
import pika
connection = pika.BlockingConnection(pika.Connectio
nParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTR
L+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback, queue='hello', no_a
ck=True)

channel.start_consuming()
Đoạn code này cũng có phần khai báo connection ,

channel . Tuy nhiên, vì là consumer nên sẽ sử dụng
phương thức basic_consume để lắng nghe trên queue
hello , khi có message đến sẽ gọi hàm callback() để xử
lý. Trong trường hợp ví dụ này thì callback chỉ đơn giản là
hiển thị chuỗi thông báo đã nhận được message.
12.4. Tìm hiểu thêm về RabbitMQ và Pika
Nội dung chương này không có ý định giới thiệu tất cả khái
niệm của AMQP cũng như RabbitMQ mà chủ yếu giới thiệu
thư viện pika để làm việc với RabbitMQ. Bạn có thể tiếp
tục theo dõi các hướng dẫn về khái niệm của RabbitMQ và
Pika tại website chính thức của RabbitMQ.
https://www.rabbitmq.com/tutorials/tutorial-one-
python.html
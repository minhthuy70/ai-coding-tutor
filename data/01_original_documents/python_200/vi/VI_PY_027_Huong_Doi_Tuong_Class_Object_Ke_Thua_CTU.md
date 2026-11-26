<!-- page: 1 -->
# VI_PY_027: Lập trình hướng đối tượng OOP: Class, Object, Kế thừa và Đa hình

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)  
**Chuyên mục**: OOP | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 74 -->
74
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

<!-- page: 75 -->
75
Socket

<!-- page: 76 -->
76
Nghi thức TCP

<!-- page: 77 -->
77
Nghi thức UDP

<!-- page: 78 -->
78
Socket trong Python
Mô-đun socket
import socket
Phương thức socket (s) phía server
s.bind((hostname, port))
s.listen(backlog)
s.accept()

<!-- page: 2 -->

Phương thức socket (s) phía client
s.connect(hostname, port)

<!-- page: 79 -->
79
Socket trong Python
Phương thức socket (s) chung
s.recv(buflen[, flags])
s.send(data[, flags])
s.recvfrom(buflen[, flags])
s.sendto(data[,flags], (addr, port))
s.close()
socket.gethostname()
socket.gethostbyname(hostname)

<!-- page: 80 -->
80
hello_s.py (Hello server, TCP)

<!-- page: 81 -->
81
hello_c.py (Hello client, TCP)

<!-- page: 82 -->
82
hello_s_udp.py (Hello server, UDP)

<!-- page: 83 -->
83
hello_c_udp.py (Hello client, UDP)

<!-- page: 84 -->
84
Cài đặt server phục vụ cùng lúc nhiều client
Phương thức cài đặt: luồng, tiến trình con, bất đồng bộ
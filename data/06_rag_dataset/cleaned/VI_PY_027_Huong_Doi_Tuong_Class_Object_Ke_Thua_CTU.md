# VI_PY_027: Lập trình hướng đối tượng OOP: Class, Object, Kế thừa và Đa hình

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)
**Chuyên mục**: OOP | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

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

75
Socket

76
Nghi thức TCP

77
Nghi thức UDP

78
Socket trong Python
Mô-đun socket
import socket
Phương thức socket (s) phía server
s.bind((hostname, port))
s.listen(backlog)
s.accept()

Phương thức socket (s) phía client
s.connect(hostname, port)

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

80
hello_s.py (Hello server, TCP)

81
hello_c.py (Hello client, TCP)

82
hello_s_udp.py (Hello server, UDP)

83
hello_c_udp.py (Hello client, UDP)

84
Cài đặt server phục vụ cùng lúc nhiều client
Phương thức cài đặt: luồng, tiến trình con, bất đồng bộ
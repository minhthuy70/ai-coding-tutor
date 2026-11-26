<!-- page: 1 -->
# VI_PY_046: Vòng lặp For, While và giải pháp phòng tránh bẫy lặp vô tận

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Vòng lặp | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 57 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
chương trình khó đọc và dễgây lỗi logic.
c, Ví dụkiểm tra quyền truy cập hệthống
username = "admin"
password = "123456"
if username == "admin":
if password == "123456":
print("Dang nhap thanh cong")
else:
print("Sai mat khau")
else:
print("Nguoi dung khong ton tai")
Kết quảhiển thị:
Dang nhap thanh cong
Trong ví dụnày, việc kiểm tra mật khẩu chỉđược thực hiện khi tên người dùng hợp lệ.
Điều này phản ánh đúng logic xửlý trong các hệthống thực tế.
d, Ví dụphân loại tín hiệu đo
signal = 4.2
if signal >= 0:
if signal < 1:
print("Tin hieu rat yeu")
elif signal < 3:
print("Tin hieu yeu")
elif signal < 5:
print("Tin hieu trung binh")
else:
print("Tin hieu manh")
else:
print("Gia tri tin hieu khong hop le")
Kết quảhiển thị:
Tin hieu trung binh
Ví dụtrên minh họa rõ việc kết hợp điều kiện lồng nhau và elif đểphân loại dữliệu
đo trong kỹthuật.
e, So sánh điều kiện lồng nhau và elif

<!-- page: 2 -->

Trong nhiều trường hợp, câu lệnh elif có thểthay thếcho điều kiện lồng nhau đểmã
nguồn trởnên gọn gàng và dễhiểu hơn. Tuy nhiên, điều kiện lồng nhau vẫn cần thiết khi
42

<!-- page: 58 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
các quyết định có mối quan hệphân cấp rõ ràng.
f, Lưu ý khi sửdụng điều kiện lồng nhau
Khi sửdụng câu lệnh điều kiện lồng nhau, cần lưu ý:
• Không lồng quá sâu nếu không cần thiết
• Đặt tên biến rõ ràng đểtránh nhầm lẫn logic
• Kiểm tra kỹcác trường hợp biên (edge cases)
• Ưu tiên tính dễđọc hơn độngắn của mã nguồn
4.7.8
Ứng dụng câu lệnh điều kiện trong bài toán kỹthuật
a, Vai trò của điều kiện trong lập trình kỹthuật
Trong các hệthống kỹthuật, chương trình thường phải đưa ra quyết định dựa trên dữ
liệu đo, trạng thái hệthống hoặc các ngưỡng an toàn. Câu lệnh điều kiện giúp chương
trình:
• Phản ứng với các tình huống khác nhau
• Đảm bảo an toàn cho hệthống
• Tựđộng hóa quá trình ra quyết định
b, Ứng dụng trong giám sát nhiệt độ
temperature = 85
if temperature < 70:
print("Nhiet do an toan")
elif temperature < 90:
print("Canh bao: Nhiet do cao")
else:
print("Nguy hiem: Can dung he thong")
Kết quảhiển thị:
Canh bao: Nhiet do cao
Đây là mô hình cơ bản của các hệthống giám sát nhiệt trong công nghiệp.
43

<!-- page: 59 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
c, Ứng dụng trong xửlý dữliệu đo
voltage = 220
if voltage < 200:
status = "Dien ap thap"
elif voltage <= 240:
status = "Dien ap binh thuong"
else:
status = "Dien ap cao"

<!-- page: 3 -->

print(status)
Kết quảhiển thị:
Dien ap binh thuong
Việc phân loại dữliệu đo như điện áp, dòng điện hoặc áp suất là bài toán phổbiến
trong kỹthuật điện và điều khiển.
d, Ứng dụng trong điều khiển thiết bị
speed = 45
if speed == 0:
print("Dong co dung")
elif speed < 30:
print("Dong co chay cham")
elif speed < 60:
print("Dong co chay binh thuong")
else:
print("Dong co chay nhanh")
Kết quảhiển thị:
Dong co chay binh thuong
Trong các hệthống điều khiển, các ngưỡng tốc độ, áp suất hoặc lưu lượng thường được
kiểm tra bằng câu lệnh điều kiện.
44

<!-- page: 60 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
e, Ứng dụng trong đánh giá chất lượng
error_rate = 2.5
if error_rate <= 1:
print("Chat luong tot")
elif error_rate <= 3:
print("Chat luong chap nhan duoc")
else:
print("Chat luong khong dat")
Kết quảhiển thị:
Chat luong chap nhan duoc
Ví dụnày phản ánh quy trình kiểm tra chất lượng trong sản xuất và kỹthuật.
Câu lệnh điều kiện đóng vai trò trung tâm trong hầu hết các bài toán kỹthuật, từxửlý
dữliệu đo, giám sát hệthống đến điều khiển tựđộng. Việc sửdụng linh hoạt các cấu trúc
if – elif – else và điều kiện lồng nhau giúp chương trình phản ứng chính xác, an
toàn và hiệu quảtrước các tình huống thực tế.
4.8
Vòng lặp trong Python
Trong quá trình xây dựng chương trình, rất nhiều bài toán yêu cầu thực hiện lặp đi lặp
lại một hoặc nhiều thao tác. Thay vì viết cùng một đoạn mã nhiều lần, Python cung cấp
các cấu trúc vòng lặp cho phép tựđộng hóa quá trình này. Hai cấu trúc vòng lặp cơ bản và
quan trọng nhất trong Python là vòng lặp for và vòng lặp while.
Vòng lặp không chỉgiúp chương trình ngắn gọn hơn mà còn đóng vai trò trung tâm

<!-- page: 4 -->

trong việc xửlý dữliệu dạng tập hợp, phân tích dữliệu đo, mô phỏng kỹthuật và xây
dựng các thuật toán.
4.8.1
Vòng lặp for
Vòng lặp for trong Python được thiết kếtheo hướng duyệt qua từng phần tửcủa một
tập hợp dữliệu. Khác với một sốngôn ngữlập trình truyền thống, for trong Python không
dựa trực tiếp vào chỉsốmà dựa trên chính các phần tửtrong tập hợp, giúp mã nguồn trở
nên trực quan và dễđọc hơn.
a, Cách hoạt động của vòng lặp for
Khi sửdụng vòng lặp for, Python sẽlần lượt lấy từng phần tửtrong một đối tượng có
thểlặp (iterable), gán vào biến vòng lặp và thực hiện khối lệnh tương ứng. Quá trình này
kết thúc khi không còn phần tửnào đểduyệt.
45

<!-- page: 61 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
b, Ví dụlặp với dãy số
for i in range(1, 6):
print(i)
Kết quảhiển thị:
1
2
3
4
5
Hàm range() thường được sửdụng đểtạo ra một dãy sốphục vụcho vòng lặp, đặc
biệt trong các bài toán tính toán sốvà kỹthuật.
c, Vòng lặp for với kiểu dữliệu String
Chuỗi ký tựtrong Python là một kiểu dữliệu tuần tự, do đó có thểđược duyệt từng ký
tựbằng vòng lặp for.
text = "Python"
for ch in text:
print(ch)
Kết quảhiển thị:
P
y
t
h
o
n
Ví dụnày cho thấy mỗi ký tựtrong chuỗi được xửlý như một phần tửđộc lập.
d, Vòng lặp for với List
Danh sách (list) là cấu trúc dữliệu được sửdụng rất phổbiến trong Python. Vòng lặp
for cho phép xửlý từng phần tửtrong danh sách một cách tựnhiên.
values = [2, 4, 6, 8]

<!-- page: 5 -->

for v in values:
print(v * v)
Kết quảhiển thị:
46

<!-- page: 62 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
4
16
36
64
Trong các bài toán kỹthuật, cách duyệt này thường được sửdụng đểtính toán trên các
tập dữliệu đo hoặc các tham sốđầu vào.
e, Vòng lặp for với Tuple
Tuple có cách sửdụng tương tựlist nhưng không thểthay đổi giá trị. Vòng lặp for vẫn
hoạt động hoàn toàn giống nhau.
coordinates = (3, 5, 7)
for c in coordinates:
print(c)
Kết quảhiển thị:
3
5
7
f, Vòng lặp for với Set
Set là kiểu dữliệu tập hợp không có thứtự. Khi duyệt bằng vòng lặp for, thứtựcác
phần tửcó thểkhác nhau giữa các lần chạy chương trình.
sensors = {"Temp", "Pressure", "Humidity"}
for s in sensors:
print(s)
Kết quảhiển thị(một khảnăng):
Pressure
Temp
Humidity
Điều này cho thấy set không đảm bảo thứtự, một điểm rất quan trọng khi xửlý dữliệu.
g, Vòng lặp for với Dictionary
Khi duyệt dictionary, vòng lặp for mặc định duyệt qua các khóa (key).
47

<!-- page: 63 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
scores = {"An": 8, "Binh": 7, "Cuong": 9}
for name in scores:
print(name, scores[name])
Kết quảhiển thị:
An 8

<!-- page: 6 -->

Binh 7
Cuong 9
4.8.2
Vòng lặp while
Khác với vòng lặp for, vòng lặp while hoạt động dựa trên một điều kiện logic.
Chương trình sẽtiếp tục lặp khi điều kiện còn đúng và dừng lại khi điều kiện trởthành
sai.
a, Cách hoạt động của vòng lặp while
Mỗi lần lặp, Python kiểm tra điều kiện. Nếu điều kiện là True, khối lệnh bên trong
sẽđược thực thi. Do đó, vòng lặp while thường được sửdụng khi sốlần lặp không biết
trước.
b, Ví dụđếm số
count = 1
while count <= 5:
print(count)
count += 1
Kết quảhiển thị:
1
2
3
3
4
5
Vòng lặp while yêu cầu người lập trình phải đảm bảo điều kiện kết thúc, nếu không
chương trình sẽrơi vào vòng lặp vô hạn.
48

<!-- page: 64 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
c, Ví dụkiểm tra dữliệu đo
value = 0
while value < 10:
value += 3
print("Gia tri hien tai:", value)
Kết quảhiển thị:
Gia tri hien tai: 3
Gia tri hien tai: 6
Gia tri hien tai: 9
Gia tri hien tai: 12
4.8.3
So sánh vòng lặp for và while
Vòng lặp for phù hợp khi làm việc với các tập hợp dữliệu hoặc khi biết trước sốlần
lặp. Ngược lại, vòng lặp while phù hợp hơn khi điều kiện kết thúc phụthuộc vào trạng
thái hoặc kết quảtính toán trong quá trình chạy chương trình.
Trong thực tế, việc lựa chọn đúng loại vòng lặp giúp chương trình trởnên rõ ràng, an

<!-- page: 7 -->

toàn và hiệu quảhơn. Vòng lặp for và while là nền tảng của lập trình Python. Việc hiểu
rõ cách hoạt động và ứng dụng của từng loại vòng lặp giúp sinh viên xửlý hiệu quảcác
bài toán liên quan đến dữliệu, mô phỏng và điều khiển trong kỹthuật, đồng thời tạo tiền
đềcho việc học các cấu trúc nâng cao hơn như vòng lặp lồng nhau và xửlý ngoại lệ.
4.8.4
Vòng lặp lồng nhau
a, Khái niệm
Vòng lặp lồng nhau là cấu trúc trong đó một vòng lặp được đặt bên trong một vòng lặp
khác. Trong Python, cảvòng lặp for và while đều có thểđược lồng nhau. Cấu trúc này
thường được sửdụng khi xửlý dữliệu nhiều chiều, chẳng hạn như ma trận, bảng sốliệu,
hoặc khi cần kết hợp nhiều điều kiện lặp trong cùng một bài toán.
Vềmặt thực thi, với mỗi lần lặp của vòng lặp bên ngoài, toàn bộvòng lặp bên trong sẽ
được thực hiện trọn vẹn.
b, Ví dụvòng lặp for lồng nhau
for i in range(1, 4):
for j in range(1, 4):
print(i, "*", j, "=", i * j)
Kết quảhiển thị:
1 * 1 = 1
1 * 2 = 2
49

<!-- page: 65 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
1 * 3 = 3
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
Ví dụtrên minh họa rõ cách vòng lặp lồng nhau được sửdụng đểxây dựng bảng nhân,
một dạng bài toán cơ bản nhưng rất quan trọng trong tư duy thuật toán.
c, Vòng lặp lồng nhau với dữliệu dạng bảng
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
for row in matrix:
for value in row:
print(value, end=" ")
print()
Kết quảhiển thị:
1 2 3

<!-- page: 8 -->

4 5 6
7 8 9
Trong các bài toán kỹthuật và khoa học, dữliệu thường được lưu trữdưới dạng ma
trận hoặc bảng hai chiều. Vòng lặp lồng nhau là công cụcơ bản đểduyệt và xửlý dạng dữ
liệu này.
d, Vòng lặp while lồng nhau
i = 1
while i <= 3:
j = 1
while j <= 3:
print(i, j)
j += 1
i += 1
Kết quảhiển thị:
1 1
50
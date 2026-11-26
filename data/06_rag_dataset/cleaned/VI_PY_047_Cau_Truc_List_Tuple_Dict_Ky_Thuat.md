# VI_PY_047: Cấu trúc List, Tuple, Dict ứng dụng trong lưu trữ dữ liệu kỹ thuật

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Cấu trúc dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
2
4
5
Trong các bài toán xửlý dữliệu, continue rất hữu ích đểbỏqua các giá trịkhông
hợp lệhoặc không cần thiết.
c, Lệnh pass
Lệnh pass không thực hiện hành động gì, nó chỉđóng vai trò là một câu lệnh rỗng.
pass thường được sửdụng khi cú pháp yêu cầu phải có một khối lệnh nhưng người lập
trình chưa muốn hoặc chưa cần cài đặt nội dung.
for i in range(3):
pass
print("Vong lap ket thuc")
Kết quảhiển thị:
Vong lap ket thuc
4.8.6
Ứng dụng vòng lặp trong bài toán kỹthuật
a, Tính giá trịtrung bình của dữliệu đo
measurements = [10.2, 10.5, 9.8, 10.1]
total = 0
for m in measurements:
total += m
average = total / len(measurements)
print("Gia tri trung binh:", average)
Kết quảhiển thị:
Gia tri trung binh: 10.15
Đây là ví dụđiển hình cho việc sửdụng vòng lặp đểxửlý dữliệu đo trong kỹthuật.
b, Phát hiện giá trịvượt ngưỡng an toàn
values = [45, 50, 72, 48, 90]
for v in values:
if v > 80:
print("Canh bao! Gia tri vuot nguong:", v)
break
52

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
Kết quảhiển thị:
Canh bao! Gia tri vuot nguong: 90
Ứng dụng này phản ánh cách vòng lặp kết hợp với điều kiện đểgiám sát an toàn trong
hệthống kỹthuật.
c, Xửlý dữliệu nhiều chiều
data = [
[2, 4, 6],
[1, 3, 5]
]
for row in data:
for value in row:
print(value * 2, end=" ")
print()
Kết quảhiển thị:
4 8 12
2 6 10
4.8.7
Xửlý ngoại lệtrong Python (try – except)
a, Khái niệm vềngoại lệ
Trong quá trình thực thi chương trình, không phải lúc nào mọi thao tác cũng diễn ra
đúng như mong muốn. Các lỗi như chia cho số0, nhập sai kiểu dữliệu, truy cập phần tử
không tồn tại hoặc lỗi đọc tập tin có thểxảy ra bất kỳlúc nào. Những lỗi này được Python
gọi là ngoại lệ(exception).
Nếu không được xửlý, ngoại lệsẽlàm chương trình dừng đột ngột, gây gián đoạn quá
trình tính toán hoặc điều khiển. Trong các hệthống kỹthuật và khoa học, điều này là
không thểchấp nhận được. Do đó, Python cung cấp cơ chếxửlý ngoại lệthông qua cấu
trúc try – except nhằm giúp chương trình tiếp tục hoạt động một cách an toàn.
b, Cú pháp cơ bản của try – except
Cấu trúc xửlý ngoại lệcơ bản trong Python có dạng:
try:
# đoạn mã có thểphát sinh lỗi
except:
# đoạn mã xửlý khi lỗi xảy ra
Python sẽthửthực thi các câu lệnh trong khối try. Nếu xảy ra ngoại lệ, chương trình
lập tức chuyển sang khối except thay vì dừng lại.
53

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
c, Ví dụchia cho số0
a = 10
b = 0

try:
result = a / b
print(result)
except:
print("Khong the chia cho 0")
Kết quảhiển thị:
Khong the chia cho 0
Ví dụtrên cho thấy chương trình không bịdừng mà xửlý lỗi một cách mềm dẻo.
d, Xửlý ngoại lệvới kiểu dữliệu nhập từbàn phím
Trong thực tế, dữliệu nhập từngười dùng thường không đảm bảo đúng kiểu mong
muốn.
try:
x = int(input("Nhap mot so nguyen: "))
print("Gia tri vua nhap:", x)
except:
print("Du lieu nhap vao khong hop le")
Ví dụngười dùng nhập:
abc
Kết quảhiển thị:
Du lieu nhap vao khong hop le
e, Bắt ngoại lệcụthể
Python cho phép bắt từng loại ngoại lệcụthểthay vì bắt tất cảcác lỗi chung chung.
Điều này giúp chương trình xửlý chính xác hơn.
try:
x = int("abc")
except ValueError:
print("Loi chuyen doi kieu du lieu")
Kết quảhiển thị:
Loi chuyen doi kieu du lieu
54

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
Một sốngoại lệthường gặp bao gồm: ValueError, ZeroDivisionError, TypeError,
IndexError, KeyError.
f, Cấu trúc try – except – else
Khối else được thực thi khi không có ngoại lệnào xảy ra trong try.
try:
a = 10
b = 2
result = a / b
except ZeroDivisionError:
print("Chia cho 0")
else:
print("Ket qua:", result)

Kết quảhiển thị:
Ket qua: 5.0
g, Cấu trúc try – except – finally
Khối finally luôn được thực thi, dù có xảy ra ngoại lệhay không. Cấu trúc này đặc
biệt quan trọng khi làm việc với tài nguyên như tập tin hoặc kết nối thiết bị.
try:
f = open("data.txt", "r")
content = f.read()
print(content)
except:
print("Khong mo duoc tap tin")
finally:
print("Ket thuc xu ly tap tin")
h, Kết hợp vòng lặp và xửlý ngoại lệ
Trong nhiều bài toán kỹthuật, chương trình cần liên tục yêu cầu dữliệu cho đến khi
hợp lệ.
55

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
while True:
try:
value = float(input("Nhap gia tri duong: "))
if value <= 0:
raise ValueError
break
except ValueError:
print("Gia tri khong hop le, vui long nhap lai")
print("Gia tri hop le:", value)
i, Ứng dụng xửlý ngoại lệtrong bài toán kỹthuật
Xửlý ngoại lệđược sửdụng rộng rãi trong:
• Kiểm tra dữliệu đo từcảm biến
• Đảm bảo an toàn khi điều khiển thiết bị
• Tránh dừng đột ngột hệthống trong môi trường thực
• Tăng độổn định và tin cậy của phần mềm kỹthuật
j, Ví dụkiểm tra dữliệu cảm biến
sensor_values = [10.5, 9.8, None, 11.2]
for v in sensor_values:
try:
print("Gia tri:", float(v))
except:
print("Du lieu cam bien khong hop le")
Kết quảhiển thị:
Gia tri: 10.5
Gia tri: 9.8

Du lieu cam bien khong hop le
Gia tri: 11.2
k, Kết luận
Xửlý ngoại lệlà một kỹnăng bắt buộc đối với lập trình viên Python, đặc biệt trong
các lĩnh vực kỹthuật và khoa học. Việc sửdụng hợp lý cấu trúc try – except giúp
chương trình trởnên an toàn, ổn định và sẵn sàng ứng phó với các tình huống không mong
muốn trong môi trường thực tế.
56

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
4.9
Bài tập chương: Câu lệnh điều kiện, vòng lặp và xửlý ngoại lệ
Phần bài tập này nhằm giúp sinh viên củng cốvà vận dụng các kiến thức đã học vềcâu
lệnh điều kiện, vòng lặp và xửlý ngoại lệtrong Python. Các bài tập được thiết kếtheo
hướng từcơ bản đến nâng cao, gắn với tư duy thuật toán và các tình huống thực tếtrong
kỹthuật.
4.9.1
Câu hỏi trắc nghiệm
Câu 1. Giá trịBoolean của biểu thức sau là gì?
3 < 5 and 10 > 7
A. True
B. False
C. None
D. Lỗi cú pháp
Câu 2. Đoạn mã sau in ra kết quảgì?
x = 5
if x > 5:
print("A")
else:
print("B")
A. A
B. B
C. A B
D. Không in gì
Câu 3. Câu lệnh nào được thực thi khi tất cảcác điều kiện trong if và elif đều sai?
A. if
B. elif
C. else
D. Không có câu lệnh nào
Câu 4. Đoạn mã sau in ra bao nhiêu dòng?
57

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON

for i in range(1, 6):
if i == 3:
continue
print(i)
A. 3
B. 4
C. 5
D. 6
Câu 5. Kết quảcủa đoạn mã sau là gì?
for i in range(3):
for j in range(2):
print(i, j)
A. 3 dòng
B. 4 dòng
C. 5 dòng
D. 6 dòng
Câu 6. Khi nào vòng lặp while kết thúc?
A. Khi điều kiện sai
B. Khi gặp continue
C. Khi gặp pass
D. Khi chương trình kết thúc
Câu 7. Lệnh nào dùng đểthoát ngay khỏi vòng lặp?
A. exit
B. stop
C. break
D. return
Câu 8. Lệnh continue có tác dụng gì?
A. Kết thúc vòng lặp
B. Bỏqua vòng lặp hiện tại và chuyển sang vòng lặp tiếp theo
C. Không làm gì
D. Kết thúc chương trình
58

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
Câu 9. Đoạn mã sau xửlý loại ngoại lệnào?
try:
x = int("abc")
except ValueError:
print("Loi")
A. TypeError
B. ZeroDivisionError
C. ValueError
D. IndexError
Câu 10. Khối lệnh nào luôn được thực thi trong cấu trúc xửlý ngoại lệ?

A. try
B. except
C. else
D. finally
4.9.2
Bài tập thực hành
Bài 1. Viết chương trình nhập vào một sốnguyên. Kiểm tra và in ra sốđó là sốdương,
sốâm hay bằng 0. Chương trình phải xửlý trường hợp người dùng nhập sai kiểu dữliệu.
Bài 2. Viết chương trình sửdụng vòng lặp for đểtính tổng các sốchẵn từ1 đến n, với
n được nhập từbàn phím. Nếu n không hợp lệ, chương trình yêu cầu nhập lại.
Bài 3. Cho một danh sách các giá trịđo:
data = [10.5, 12.3, -1, 9.8, None, 11.0]
Hãy sửdụng vòng lặp và xửlý ngoại lệđể:
• Bỏqua các giá trịkhông hợp lệ
• Tính giá trịtrung bình của các giá trịhợp lệ
Bài 4. Viết chương trình mô phỏng hệthống kiểm soát nhiệt độ:
• Nếu nhiệt độnhỏhơn 70: in “An toàn”
• Từ70 đến 90: in “Cảnh báo”
• Lớn hơn 90: in “Nguy hiểm”
Chương trình lặp cho đến khi người dùng nhập giá trịâm thì dừng.
Bài 5. Viết chương trình duyệt một dictionary chứa tên thiết bịvà trạng thái hoạt động
59

CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
(True/False). In ra danh sách các thiết bịđang hoạt động. Sửdụng vòng lặp và câu lệnh
điều kiện.
4.9.3
Bài tập tổng hợp
Bài tập lớn. Xây dựng chương trình quản lý dữliệu đo từmột hệthống kỹthuật đơn
giản với các yêu cầu sau:
• Cho phép người dùng nhập liên tiếp các giá trịđo (sốthực)
• Sửdụng vòng lặp đểtiếp tục nhập cho đến khi người dùng nhập “q”
• Sửdụng xửlý ngoại lệđểloại bỏcác dữliệu không hợp lệ
• Sau khi kết thúc nhập, chương trình tính và in ra:
– Sốlượng giá trịhợp lệ
– Giá trịlớn nhất, nhỏnhất
– Giá trịtrung bình
• Nếu không có dữliệu hợp lệ, in ra thông báo phù hợp
4.10
Hàm và Module trong Python
Trong các chương trước, chương trình Python chủyếu được xây dựng dưới dạng các
câu lệnh viết liên tiếp. Cách viết này phù hợp với các bài toán nhỏ, tuy nhiên khi chương
trình trởnên dài và phức tạp hơn, việc quản lý mã nguồn sẽgặp nhiều khó khăn. Đểgiải
quyết vấn đềnày, Python cung cấp khái niệm hàm và module, cho phép chia nhỏchương

trình thành các khối chức năng độc lập, dễhiểu và dễtái sửdụng.
4.10.1
Khái niệm vềhàm
Hàm (function) là một khối mã được thiết kếđểthực hiện một nhiệm vụcụthể. Một
khi đã được định nghĩa, hàm có thểđược gọi nhiều lần ởcác vịtrí khác nhau trong chương
trình. Việc sửdụng hàm giúp chương trình:
• Tránh lặp lại mã nguồn
• Dễbảo trì và mởrộng
• Tăng tính rõ ràng vềmặt logic
Trong lập trình kỹthuật, hàm thường được dùng đểmô tảcác phép tính, mô hình toán
học, xửlý dữliệu đo hoặc các thao tác điều khiển.
4.10.2
Định nghĩa và gọi hàm
a, Cú pháp định nghĩa hàm
Trong Python, hàm được định nghĩa bằng từkhóa def.
def say_hello():
print("Xin chao Python")
60
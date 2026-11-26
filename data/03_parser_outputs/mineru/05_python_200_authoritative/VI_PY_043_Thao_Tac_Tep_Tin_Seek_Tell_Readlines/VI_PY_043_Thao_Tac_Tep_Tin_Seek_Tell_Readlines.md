<!-- page: 1 -->
# VI_PY_043: Thao tác tệp tin nâng cao: Định vị con trỏ seek(), tell() và buffer

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Tệp tin | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 28 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union_set = A | B
intersection_set = A & B
difference_set = A - B
Những phép toán này rất hữu ích trong các bài toán xửlý dữliệu, phân tích tập mẫu và
loại bỏtrùng lặp.
2.6.4
Ứng dụng của Set
Set thường được sửdụng khi:
• Cần loại bỏcác giá trịtrùng lặp
• Kiểm tra nhanh sựtồn tại của phần tử
• Thực hiện các phép toán tập hợp
Trong nhiều bài toán kỹthuật, set giúp chương trình trởnên ngắn gọn và hiệu quảhơn
so với việc sửdụng danh sách.
2.7
Chỉmục trong kiểu dữliệu tuần tự
2.7.1
Vai trò của chỉmục
Trong các kiểu dữliệu tuần tựnhư chuỗi (str), danh sách (list) và bộdữliệu
(tuple), các phần tửkhông chỉđược lưu trữmột cách ngẫu nhiên mà được sắp xếp theo
một thứtựxác định. Đểtruy cập từng phần tửcụthểtrong tập hợp đó, Python sửdụng
khái niệm chỉmục (index).
Chỉmục có thểđược hiểu là vịtrí của phần tửtrong cấu trúc dữliệu tuần tự. Thông
qua chỉmục, người lập trình có thể:
• Truy cập một phần tửcụthể
• Thay đổi giá trịphần tử(đối với kiểu dữliệu có thểthay đổi)
• Thực hiện các thao tác cắt lát và duyệt dữliệu
Việc hiểu đúng và sửdụng chính xác chỉmục là nền tảng đểlàm việc hiệu quảvới các
kiểu dữliệu tuần tựtrong Python.
2.7.2
Chỉmục dương trong Python
Python sửdụng hệthống chỉmục bắt đầu từ0. Điều này có nghĩa là phần tửđầu tiên

<!-- page: 2 -->

trong cấu trúc dữliệu có chỉmục là 0, phần tửthứhai có chỉmục là 1, và cứtiếp tục như
vậy cho đến phần tửcuối cùng.
Xét ví dụdanh sách sau:
13

<!-- page: 29 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
data = [10, 20, 30, 40, 50]
Cách Python gán chỉmục dương cho các phần tửcó thểđược minh họa như sau:
Chỉmục
0
1
2
3
4
Giá trị
10
20
30
40
50
Khi sửdụng chỉmục dương, Python sẽtruy cập phần tửtính từđầu tập hợp.
print(data[0])
# 10
print(data[2])
# 30
print(data[4])
# 50
Cách đánh chỉmục từ0 này giúp việc tính toán độdài và cắt lát dữliệu trởnên thuận
tiện và nhất quán.
2.7.3
Chỉmục âm trong Python
Bên cạnh chỉmục dương, Python còn hỗtrợchỉmục âm. Chỉmục âm cho phép truy
cập các phần tửtừcuối cấu trúc dữliệu vềđầu. Phần tửcuối cùng có chỉmục là -1, phần
tửđứng trước nó có chỉmục là -2, và cứtiếp tục như vậy.
Với danh sách data ởtrên, cách Python gán chỉmục âm có thểđược minh họa như
sau:
Chỉmục âm
-5
-4
-3
-2
-1
Giá trị
10

<!-- page: 3 -->

20
30
40
50
Ví dụtruy cập bằng chỉmục âm:
print(data[-1])
# 50
print(data[-2])
# 40
print(data[-5])
# 10
Chỉmục âm đặc biệt hữu ích khi người lập trình không biết trước độdài của tập hợp
hoặc khi cần thao tác với các phần tửgần cuối, chẳng hạn như phần tửcuối cùng hoặc hai
phần tửcuối.
2.7.4
So sánh chỉmục dương và chỉmục âm
Mặc dù chỉmục dương và chỉmục âm có cách đánh sốkhác nhau, nhưng chúng đều
tham chiếu đến cùng một phần tửtrong cấu trúc dữliệu. Ví dụ, với danh sách data:
data[0]
== data[-5]
data[1]
== data[-4]
data[4]
== data[-1]
Việc hiểu rõ mối quan hệnày giúp người lập trình linh hoạt hơn trong việc truy cập dữ
14

<!-- page: 30 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
liệu và tránh nhầm lẫn khi viết chương trình.
2.7.5
Chỉmục và độdài dữliệu
Độdài của một cấu trúc dữliệu tuần tựtrong Python có thểđược xác định bằng hàm
len(). Nếu một cấu trúc dữliệu có độdài là n, thì:
• Chỉmục dương hợp lệnằm trong khoảng từ0 đến n −1
• Chỉmục âm hợp lệnằm trong khoảng từ−n đến −1
n = len(data)
print(n)
# 5
Việc truy cập chỉmục nằm ngoài các khoảng này sẽgây ra lỗi.
2.7.6
Lỗi truy cập ngoài phạm vi chỉmục
Một trong những lỗi phổbiến nhất khi làm việc với kiểu dữliệu tuần tựlà lỗi truy cập
ngoài phạm vi chỉmục (IndexError).
print(data[5])

<!-- page: 4 -->

# Lỗi
print(data[-6])
# Lỗi
Lỗi này xảy ra khi chỉmục được sửdụng không tồn tại trong cấu trúc dữliệu. Đểtránh
lỗi, người lập trình cần:
• Kiểm tra độdài dữliệu trước khi truy cập
• Sửdụng vòng lặp thay vì truy cập trực tiếp khi không chắc chắn vềphạm vi chỉmục
2.7.7
Chỉmục trong các kiểu dữliệu tuần tựkhác nhau
Cơ chếchỉmục trong Python hoạt động thống nhất cho tất cảcác kiểu dữliệu tuần tự.
Với chuỗi:
text = "Python"
print(text[0])
# P
print(text[-1])
# n
Với tuple:
point = (10, 20, 30)
print(point[1])
# 20
print(point[-1])
# 30
Điều này giúp người học dễdàng chuyển đổi tư duy giữa các kiểu dữliệu khác nhau
mà không phải học lại cách sửdụng chỉmục.
15

<!-- page: 31 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
2.8
Duyệt các kiểu dữliệu tuần tự
Duyệt là thao tác truy cập lần lượt từng phần tửtrong một cấu trúc dữliệu tuần tự. Đây
là thao tác nền tảng trong xửlý dữliệu và xây dựng thuật toán.
for value in data:
print(value)
Vòng lặp for trong Python được thiết kếđặc biệt phù hợp cho việc duyệt các cấu trúc
dữliệu tuần tự, giúp mã nguồn ngắn gọn và dễđọc.
2.9
Cắt lát dữliệu (Slicing) trong các kiểu dữliệu tuần tự
Trong quá trình làm việc với các kiểu dữliệu tuần tựnhư chuỗi, danh sách và tuple,
người lập trình thường không chỉquan tâm đến việc truy cập một phần tửđơn lẻmà còn
cần trích xuất một đoạn liên tiếp các phần tử. Thao tác này được gọi là cắt lát dữliệu
(slicing) và là một trong những cơ chếmạnh mẽ, linh hoạt nhất của Python.
Cắt lát cho phép tạo ra một cấu trúc dữliệu mới từmột phần của cấu trúc dữliệu ban
đầu, mà không làm thay đổi dữliệu gốc. Cơ chếnày đặc biệt hữu ích trong các bài toán
xửlý chuỗi, phân tích dữliệu, xửlý tín hiệu và các bài toán kỹthuật liên quan đến dãy số

<!-- page: 5 -->

theo thời gian.
2.9.1
Cú pháp tổng quát của cắt lát
Cú pháp cắt lát trong Python có dạng tổng quát như sau:
sequence[start : stop : step]
Trong đó:
• start là chỉmục bắt đầu (bao gồm phần tửtại vịtrí này)
• stop là chỉmục kết thúc (không bao gồm phần tửtại vịtrí này)
• step là bước nhảy giữa các phần tử
Ba thành phần này đều là tùy chọn. Nếu không được chỉđịnh, Python sẽtựđộng sử
dụng các giá trịmặc định phù hợp.
2.9.2
Cắt lát cơ bản với chỉsốbắt đầu và kết thúc
Trường hợp đơn giản nhất của cắt lát là chỉđịnh vịtrí bắt đầu và kết thúc. Python sẽ
trích xuất tất cảcác phần tửnằm trong khoảng từstart đến stop - 1.
data = [10, 20, 30, 40, 50, 60]
sub = data[1:4]
print(sub)
Trong ví dụtrên, kết quảthu được là danh sách [20, 30, 40]. Phần tửởvịtrí 4
16

<!-- page: 32 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
không được lấy vì stop không bao gồm điểm kết thúc.
Cách đánh chỉmục này giúp tránh chồng lấn khi ghép các đoạn dữliệu liên tiếp, một
kỹthuật thường được sửdụng trong xửlý mảng và thuật toán.
2.9.3
Cắt lát khi bỏqua chỉmục bắt đầu hoặc kết thúc
Nếu bỏqua chỉmục bắt đầu, Python sẽmặc định lấy từđầu cấu trúc dữliệu. Nếu bỏ
qua chỉmục kết thúc, Python sẽlấy đến phần tửcuối cùng.
data = [10, 20, 30, 40, 50]
first_part = data[:3]
last_part = data[2:]
Trong ví dụnày, first_part chứa ba phần tửđầu tiên, trong khi last_part chứa
các phần tửtừvịtrí 2 đến hết. Cách sửdụng này rất phổbiến khi cần tách dữliệu thành
các phần đầu và cuối.
2.9.4
Cắt lát với bước nhảy (step)
Thành phần step cho phép xác định khoảng cách giữa các phần tửđược lấy. Nếu
step = 1, Python sẽlấy các phần tửliên tiếp. Nếu step > 1, Python sẽbỏqua một
sốphần tửtheo bước nhảy đã chỉđịnh.
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_index = data[::2]
Kết quảcủa ví dụtrên là danh sách các phần tửởvịtrí chẵn. Cơ chếbước nhảy này rất
hữu ích khi cần lấy mẫu dữliệu (sampling) trong các bài toán kỹthuật và khoa học.

<!-- page: 6 -->

2.9.5
Cắt lát với chỉsốâm
Python cho phép sửdụng chỉsốâm đểđếm từcuối cấu trúc dữliệu vềđầu. Cơ chếnày
cũng áp dụng đầy đủcho cắt lát.
data = [10, 20, 30, 40, 50]
sub = data[-4:-1]
Trong trường hợp này, Python sẽlấy các phần tửtừvịtrí thứtư tính từcuối cho đến
trước phần tửcuối cùng. Việc sửdụng chỉsốâm giúp thao tác thuận tiện hơn khi làm việc
với các đoạn dữliệu gần cuối.
2.9.6
Đảo ngược dữliệu bằng cắt lát
Một ứng dụng rất đặc biệt và thường gặp của cắt lát là đảo ngược thứtựcủa cấu trúc
dữliệu bằng cách sửdụng bước nhảy âm.
17

<!-- page: 33 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
data = [1, 2, 3, 4, 5]
reversed_data = data[::-1]
Chỉvới một dòng lệnh, toàn bộdanh sách đã được đảo ngược. Đây là một ví dụđiển
hình cho thấy sức mạnh và tính ngắn gọn của cú pháp cắt lát trong Python.
2.9.7
Cắt lát với chuỗi
Cắt lát không chỉáp dụng cho danh sách mà còn hoạt động hoàn toàn tương tựđối với
chuỗi.
text = "LapTrinhPython"
sub_text = text[3:8]
Do chuỗi là kiểu dữliệu bất biến, thao tác cắt lát sẽluôn tạo ra một chuỗi mới, giữ
nguyên chuỗi ban đầu. Điều này đặc biệt hữu ích trong xửlý văn bản và phân tích dữliệu
đầu vào.
2.9.8
Cắt lát với Tuple
Tuple cũng hỗtrợcắt lát giống như danh sách và chuỗi.
point = (10, 20, 30, 40)
sub_point = point[1:3]
Kết quảcủa phép cắt lát là một tuple mới. Mặc dù tuple là bất biến, nhưng việc trích
xuất một phần dữliệu từtuple vẫn hoàn toàn hợp lệ.
2.9.9
Những lưu ý quan trọng khi sửdụng cắt lát
Mặc dù cắt lát rất tiện lợi nhưng chúng ta cần lưu ý rằng:
• Cắt lát luôn tạo ra một bản sao dữliệu mới
• Với các tập dữliệu lớn, việc cắt lát nhiều lần có thểlàm tăng tiêu thụbộnhớ
• Cần cẩn thận với chỉsốđểtránh nhầm lẫn vềphạm vi dữliệu được trích xuất
Việc hiểu rõ cơ chếcắt lát không chỉgiúp viết mã ngắn gọn hơn mà còn giúp tối ưu
hóa chương trình và tránh các lỗi logic khó phát hiện.

<!-- page: 7 -->

2.9.10
Ý nghĩa của cắt lát trong lập trình kỹthuật
Trong các bài toán kỹthuật, cắt lát thường được sửdụng đểxửlý các dãy sốđo, phân
đoạn tín hiệu, chia dữliệu thành các khung thời gian hoặc trích xuất các vùng quan tâm
trong dữliệu. Do đó, việc nắm vững thao tác cắt lát là kỹnăng quan trọng đối với sinh
viên và kỹsư khi sửdụng Python như một công cụtính toán và mô phỏng.
Chương này đã trình bày chi tiết các kiểu dữliệu tuần tựtrong Python, bao gồm chuỗi,
danh sách và tuple, cùng với các thao tác quan trọng như truy cập, duyệt và cắt lát. Đồng
18

<!-- page: 34 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
thời, kiểu dữliệu dictionary cũng được giới thiệu như một cấu trúc dữliệu ánh xạquan
trọng. Việc nắm vững các kiểu dữliệu này là nền tảng thiết yếu đểtiếp cận các nội dung
nâng cao hơn như thuật toán, cấu trúc dữliệu nâng cao và xửlý dữliệu trong các ứng
dụng kỹthuật.
2.10
Bài tập luyện tập
Phần bài tập này nhằm giúp sinh viên củng cốvà vận dụng các kiến thức đã học về
kiểu dữliệu tuple, dictionary, set cũng như cách truy cập, duyệt và thao tác trên
các cấu trúc dữliệu này trong Python. Các bài tập được sắp xếp theo mức độtừcơ bản
đến nâng cao, phù hợp cho việc tựhọc và rèn luyện kỹnăng lập trình.
2.10.1
Câu hỏi trắc nghiệm
1. Phát biểu nào sau đây là đúng vềkiểu dữliệu tuple?
(a) Tuple có thểthay đổi kích thước sau khi khởi tạo
(b) Tuple là kiểu dữliệu bất biến
(c) Tuple không thểchứa các kiểu dữliệu khác nhau
(d) Tuple không hỗtrợchỉmục
2. Chỉmục hợp lệđểtruy cập phần tửcuối cùng của một danh sách có độdài n là:
(a) n
(b) n −1
(c) −n
(d) 0
3. Kiểu dữliệu nào sau đây không cho phép các phần tửtrùng lặp?
(a) list
(b) tuple
(c) dictionary
(d) set
4. Trong dictionary, khóa (key) phải là:
(a) Kiểu dữliệu có thểthay đổi
(b) Kiểu dữliệu bất biến
(c) Luôn là chuỗi
(d) Có thểtrùng lặp
5. Đoạn mã nào sau đây sẽgây lỗi?

<!-- page: 8 -->

(a) t = (1, 2, 3)
19

<!-- page: 35 -->
CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
(b) t[0] = 10
(c) d = {"a": 1, "b": 2}
(d) s = {1, 2, 3}
6. Kết quảcủa đoạn mã sau là gì?
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)
7. Phương thức nào dùng đểduyệt cảkhóa và giá trịtrong dictionary?
(a) keys()
(b) values()
(c) items()
(d) get()
2.11
Bài tập thực hành
Bài tập 1: Làm quen với Tuple
Viết chương trình tạo một tuple lưu trữthông tin của một điểm trong mặt phẳng tọa độ
gồm hoành độvà tung độ. Thực hiện các yêu cầu sau:
• In ra hoành độvà tung độcủa điểm
• Tính khoảng cách từđiểm đó đến gốc tọa độ(0, 0)
Bài tập 2: Truy cập và duyệt Tuple
Cho tuple sau:
data = (5, 10, 15, 20, 25)
1. In ra phần tửđầu tiên và phần tửcuối cùng
2. Duyệt tuple bằng vòng lặp for và in ra từng phần tử
3. Tính tổng các phần tửtrong tuple
Bài tập 3: Dictionary cơ bản
Viết chương trình quản lý thông tin sinh viên bằng dictionary, trong đó mỗi sinh viên
có các thuộc tính: mã sinh viên, họtên, tuổi và điểm trung bình.
Yêu cầu:
• Khởi tạo dictionary lưu trữthông tin một sinh viên
• In ra toàn bộthông tin sinh viên
20
# VI_PY_042: Kỹ thuật cắt lát (Slicing) chuyên sâu với chỉ số âm và đảo ngược dữ liệu

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Cắt lát | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON
1.2.3
Đặt tên biến
Tên biến trong Python không chỉcó ý nghĩa kỹthuật mà còn ảnh hưởng trực tiếp đến
khảnăng đọc hiểu và bảo trì chương trình. Một tên biến tốt cần phản ánh đúng ý nghĩa
của dữliệu mà nó lưu trữ. Python cho phép sửdụng chữcái, chữsốvà dấu gạch dưới trong
tên biến, đồng thời phân biệt chữhoa và chữthường.
student_name = "An"
total_score = 85
Việc sửdụng những tên biến có ý nghĩa rõ ràng là một thói quen quan trọng trong lập
trình, đặc biệt trong các dựán kỹthuật và nghiên cứu có quy mô lớn.
Bên cạnh các quy tắc đặt tên biến hợp lệ, người học cũng cần nắm rõ những trường
hợp đặt tên biến sai thường gặp đểtránh lỗi cú pháp ngay từgiai đoạn viết chương trình.
Trong Python, các lỗi này sẽđược phát hiện ngay khi chương trình được thực thi, gây gián
đoạn quá trình chạy chương trình.
Một lỗi phổbiến là đặt tên biến bắt đầu bằng chữsố. Python không cho phép điều này
vì sẽgây nhầm lẫn với các hằng sốsốhọc.
2value = 10
Đoạn mã trên là không hợp lệvì tên biến không được phép bắt đầu bằng chữsố. Python
sẽbáo lỗi cú pháp ngay khi biên dịch.
Một lỗi thường gặp khác là sửdụng các ký tựđặc biệt như dấu gạch ngang hoặc khoảng
trắng trong tên biến.
student-name = "An"
total score = 100
Trong trường hợp này, dấu gạch ngang bịPython hiểu là toán tửtrừ, còn khoảng trắng
được coi là dấu phân tách giữa các từkhóa, do đó đều dẫn đến lỗi cú pháp.
Ngoài ra, việc sửdụng từkhóa (keyword) của Python làm tên biến cũng là một lỗi
nghiêm trọng. Các từkhóa này đã được Python định nghĩa sẵn cho các mục đích cú pháp
đặc biệt.
for = 5
class = "CS"
Những tên biến trên là không hợp lệvì for và class là các từkhóa của ngôn ngữ
Python. Đểtránh lỗi này, người học nên lựa chọn những tên biến có ý nghĩa, không trùng
3

CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON
với từkhóa và tuân thủđầy đủcác quy tắc đặt tên.
Việc hiểu rõ các cách đặt tên biến sai không chỉgiúp tránh lỗi cú pháp mà còn hình
thành thói quen lập trình đúng đắn, đặc biệt quan trọng trong các dựán kỹthuật và nghiên
cứu có quy mô lớn.
1.3
Các kiểu dữliệu cơ bản trong Python và đặc điểm bộnhớ
Trong quá trình lập trình, ngoài việc hiểu ý nghĩa logic của dữliệu, người lập trình kỹ
thuật cần quan tâm đến cách dữliệu được lưu trữtrong bộnhớvà phạm vi biểu diễn của
chúng. Điều này đặc biệt quan trọng khi xửlý dữliệu lớn, tính toán khoa học hoặc các bài
toán yêu cầu hiệu năng cao.
Python là ngôn ngữlập trình bậc cao với cơ chếquản lý bộnhớtựđộng. Không giống
như các ngôn ngữbậc thấp, người lập trình Python không cần trực tiếp cấp phát hay giải
phóng bộnhớ. Tuy nhiên, mỗi kiểu dữliệu trong Python vẫn chiếm một lượng bộnhớnhất
định và có phạm vi biểu diễn riêng, điều mà người học cần nắm rõ đểsửdụng hiệu quả.
1.3.1
Kiểu sốnguyên (int)
Kiểu sốnguyên trong Python được biểu diễn bằng int. Khác với các ngôn ngữnhư
C hoặc C++, Python không giới hạn sốnguyên trong một sốbit cốđịnh (ví dụ32-bit hay
64-bit). Thay vào đó, Python sửdụng cơ chếsốnguyên có độchính xác tùy ý (arbitrary
precision).
Điều này có nghĩa là phạm vi biểu diễn của sốnguyên trong Python chỉbịgiới hạn bởi
dung lượng bộnhớcủa hệthống. Tuy nhiên, đi kèm với sựlinh hoạt đó là chi phí bộnhớ
lớn hơn.
a = 10
b = 10**100
Vềmặt bộnhớ, một sốnguyên trong Python không chỉlưu giá trịmà còn lưu thêm
thông tin quản lý đối tượng. Trên hệthống 64-bit, một sốnguyên nhỏthường chiếm
khoảng 28 byte bộnhớ, và sẽtăng thêm khi giá trịlớn hơn.
1.3.2
Kiểu sốthực (float)
Kiểu sốthực trong Python được biểu diễn bằng float, tuân theo chuẩn IEEE 754
dạng double-precision. Mỗi sốthực chiếm 64 bit (8 byte) đểlưu giá trịdấu phẩy động.
x = 3.1415926535
Phạm vi biểu diễn xấp xỉcủa kiểu float là từ:
±1.8 × 10308
với độchính xác khoảng 15–16 chữsốthập phân. Do đặc điểm của biểu diễn dấu phẩy
4

CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON
động, các phép toán với float có thểphát sinh sai sốlàm tròn, điều này cần được lưu ý
trong các bài toán kỹthuật chính xác cao.

1.3.3
Kiểu logic (bool)
Kiểu logic bool chỉcó hai giá trịlà True và False. Vềmặt khái niệm, kiểu này chỉ
cần 1 bit đểbiểu diễn. Tuy nhiên, trong Python, bool là một đối tượng hoàn chỉnh, do đó
nó chiếm nhiều bộnhớhơn so với biểu diễn lý thuyết.
flag = True
Trên hệthống 64-bit, một giá trịbool thường chiếm khoảng 28 byte. Mặc dù chi phí
bộnhớlớn, kiểu bool đóng vai trò không thểthiếu trong điều khiển luồng chương trình
và biểu thức điều kiện.
1.3.4
Kiểu chuỗi (str)
Kiểu chuỗi str dùng đểlưu trữdữliệu văn bản. Chuỗi trong Python là một dãy các
ký tựUnicode, mỗi ký tựcó thểchiếm từ1 đến 4 byte tùy theo mã Unicode.
text = "Python"
Dung lượng bộnhớcủa một chuỗi phụthuộc vào:
• Sốlượng ký tự
• Loại ký tự(ASCII hay Unicode mởrộng)
• Thông tin quản lý đối tượng
Do đó, một chuỗi ngắn cũng có thểchiếm vài chục byte bộnhớ. Chuỗi trong Python là
bất biến (immutable), nghĩa là mỗi lần thay đổi nội dung, Python sẽtạo ra một đối tượng
mới trong bộnhớ.
1.3.5
So sánh bộnhớvà phạm vi biểu diễn của các kiểu dữliệu cơ bản
Bảng 1.1 tóm tắt đặc điểm bộnhớvà phạm vi biểu diễn của các kiểu dữliệu cơ bản
trong Python.
Bảng 1.1: So sánh các kiểu dữliệu cơ bản trong Python
Kiểu dữliệu
Bộnhớ(xấp xỉ)
Phạm vi biểu diễn
Ghi chú
int
∼28 byte
Không giới hạn
Tăng theo độlớn giá trị
float
8 byte
±1.8 × 10308
Sai sốlàm tròn
bool
∼28 byte
True / False
Kiểu logic
str
Phụthuộc độdài
Unicode

Bất biến
1.3.6
Nhận xét
Từbảng so sánh có thểthấy rằng Python đánh đổi hiệu năng và bộnhớđểđổi lấy tính
linh hoạt và dễsửdụng. Đối với các bài toán kỹthuật có quy mô lớn hoặc yêu cầu tối ưu
5

CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON
tài nguyên, người lập trình cần cân nhắc lựa chọn kiểu dữliệu phù hợp, cũng như sửdụng
các thư viện chuyên dụng như NumPy đểtối ưu bộnhớvà tốc độtính toán.
1.4
Kết luận
Việc hiểu rõ cách Python lưu trữdữliệu trong bộnhớvà phạm vi biểu diễn của từng
kiểu dữliệu giúp người học sửdụng ngôn ngữnày một cách hiệu quảvà khoa học hơn.
Đây là kiến thức nền tảng quan trọng đểtiếp cận các nội dung nâng cao như cấu trúc dữ
liệu, xửlý mảng lớn và tính toán sốtrong các chương tiếp theo.
1.5
Bài tập
Bài tập 1: Khai báo biến và tính BMI
Viết chương trình nhập vào chiều cao (m) và cân nặng (kg) của một người, sau đó tính
chỉsốBMI theo công thức:
BMI = Cân nặng (kg)
Chiều cao (m)
2
Chương trình cần:
• Sửdụng biến đểlưu chiều cao, cân nặng và BMI
• In kết quảBMI với 2 chữsốthập phân
• Đưa ra đánh giá dựa trên BMI:
– BMI < 18.5: Thiếu cân
– 18.5 ≤BMI < 25: Bình thường
– 25 ≤BMI < 30: Thừa cân
– BMI ≥30: Béo phì
Bài tập 2: Sửdụng toán tửsốhọc
Viết chương trình tính diện tích và chu vi của:
1. Hình chữnhật: nhập chiều dài và chiều rộng
2. Hình tròn: nhập bán kính (sửdụng π = 3.14159)
Yêu cầu: Sửdụng các toán tửsốhọc phù hợp và in kết quảvới định dạng rõ ràng.
Bài tập 3: Toán tửlogic và so sánh
Viết chương trình nhập vào một sốnguyên, sau đó kiểm tra và in ra:
• Sốđó có phải là sốchẵn không?
• Sốđó có phải là sốdương không?
• Sốđó có phải vừa chẵn vừa dương không?
Yêu cầu: Sửdụng toán tửso sánh và toán tửlogic (and, or, not).
6

CHƯƠNG 1. BIẾN, CÁC KIỂU DỮLIỆU VÀ TOÁN TỬCƠ BẢN TRONG PYTHON
Bài tập 4: Chuyển đổi kiểu dữliệu
Viết chương trình chuyển đổi nhiệt độgiữa các đơn vị:
• Celsius sang Fahrenheit: F = C × 9
5 + 32
• Fahrenheit sang Celsius: C = (F −32) × 5
9
• Celsius sang Kelvin: K = C + 273.15
Yêu cầu: Nhập vào giá trịvà đơn vịban đầu, sau đó chuyển đổi sang các đơn vịcòn
lại.
Bài tập 5: Xửlý chuỗi
Viết chương trình nhập vào một chuỗi ký tựtừbàn phím, sau đó:
1. Đếm sốký tự, sốtừtrong chuỗi
2. Chuyển đổi chuỗi sang chữhoa và chữthường
3. Kiểm tra chuỗi có phải là palindrome không (đọc xuôi và ngược giống nhau)
4. Thay thếtất cảkhoảng trắng bằng dấu gạch dưới
Ghi chú: Xem lời giải chi tiết tại Phụlục - Lời giải bài tập.
7

CHƯƠNG 2. Kiểu dữliệu tuần tự
2.1
Tổng quan vềkiểu dữliệu phức hợp trong Python
Trong các chương trước, người học đã làm quen với những kiểu dữliệu cơ bản như số
nguyên, sốthực, kiểu logic và chuỗi ký tự. Tuy nhiên, trong thực tếlập trình, đặc biệt là
trong các bài toán kỹthuật và khoa học máy tính, dữliệu hiếm khi chỉtồn tại ởdạng một
giá trịđơn lẻ. Thông thường, chúng xuất hiện dưới dạng một tập hợp gồm nhiều giá trịcó
liên quan với nhau, chẳng hạn như danh sách các phép đo, chuỗi tín hiệu theo thời gian,
bảng điểm sinh viên hoặc tập hợp các tham sốkỹthuật.
Đểbiểu diễn và xửlý những tập hợp dữliệu này, Python cung cấp các kiểu dữliệu
phức hợp. Trong sốđó, nhóm kiểu dữliệu có vai trò đặc biệt quan trọng là các kiểu dữ
liệu tuần tự. Đây là những kiểu dữliệu mà các phần tửđược lưu trữtheo một thứtựxác
định, cho phép truy cập lần lượt từng phần tửthông qua vịtrí của chúng trong tập hợp.
Bên cạnh các kiểu dữliệu tuần tự, Python còn cung cấp kiểu dữliệu ánh xạlà dictionary.
Mặc dù dictionary không phải là kiểu tuần tựtheo nghĩa truyền thống, nhưng nó lại là một
trong những cấu trúc dữliệu được sửdụng phổbiến nhất trong Python, đặc biệt khi cần
biểu diễn dữliệu có cấu trúc dạng thuộc tính.
Chương này sẽtrình bày một cách hệthống và chi tiết các kiểu dữliệu nói trên, tập
trung vào bản chất, cách sửdụng và các thao tác thường gặp.
2.2
Khái niệm kiểu dữliệu tuần tự
Kiểu dữliệu tuần tựlà kiểu dữliệu trong đó các phần tửđược sắp xếp theo một trật tự
nhất định. Trật tựnày được duy trì trong suốt vòng đời của cấu trúc dữliệu, trừkhi người

lập trình chủđộng thay đổi nó. Mỗi phần tửtrong tập hợp được gắn với một vịtrí cụthể,
gọi là chỉmục.
Đặc điểm quan trọng nhất của kiểu dữliệu tuần tựlà khảnăng:
• Truy cập phần tửtheo vịtrí
• Duyệt lần lượt các phần tửtheo thứtự
• Trích xuất một phần của tập hợp thông qua thao tác cắt lát
Trong Python, ba kiểu dữliệu tuần tựcơ bản nhất là chuỗi (str), danh sách (list) và
bộdữliệu (tuple). Mỗi kiểu có những đặc điểm riêng vềkhảnăng thay đổi, hiệu năng
và mục đích sửdụng.
2.3
Kiểu dữliệu String
2.3.1
Bản chất của chuỗi trong Python
Chuỗi ký tựtrong Python, được biểu diễn bởi kiểu str, là một dãy các ký tựUnicode
được lưu trữtheo thứtự. Mỗi ký tựtrong chuỗi là một đơn vịdữliệu riêng biệt, và toàn
bộchuỗi có thểđược xem như một tập hợp tuần tựcác ký tự.
8

CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
s = "Python"
Trong ví dụtrên, chuỗi "Python" gồm sáu ký tự, được lưu trữtheo thứtựtừtrái sang
phải. Python tựđộng gán cho mỗi ký tựmột chỉmục, bắt đầu từ0.
2.3.2
Tính bất biến của chuỗi
Một trong những đặc điểm quan trọng nhất của kiểu str là tính bất biến. Sau khi chuỗi
được tạo ra, nội dung của nó không thểbịthay đổi trực tiếp. Điều này có nghĩa là người
lập trình không thểgán một ký tựmới vào một vịtrí cụthểtrong chuỗi.
s[0] = 'p'
# Gây lỗi
Bất kỳthao tác nào làm thay đổi nội dung chuỗi thực chất đều dẫn đến việc tạo ra một
đối tượng chuỗi mới trong bộnhớ. Đặc điểm này giúp chuỗi trởnên an toàn hơn khi sử
dụng trong các chương trình lớn, đồng thời tránh được nhiều lỗi khó phát hiện liên quan
đến việc thay đổi dữliệu không mong muốn.
2.3.3
Các thao tác thường gặp với chuỗi
Chuỗi hỗtrợnhiều phép toán và phương thức phục vụcho xửlý văn bản. Người lập
trình có thểnối chuỗi, lặp chuỗi hoặc kiểm tra sựtồn tại của ký tựtrong chuỗi.
a = "Lap trinh"
b = "Python"
c = a + " " + b
Ngoài ra, Python cung cấp nhiều phương thức mạnh đểxửlý chuỗi như chuyển đổi
chữhoa, chữthường, tách chuỗi hoặc loại bỏkhoảng trắng thừa. Những thao tác này rất
thường xuyên được sửdụng trong các bài toán xửlý dữliệu đầu vào.
2.4

Kiểu dữliệu List
2.4.1
Khái niệm và đặc điểm của List
Danh sách trong Python, được biểu diễn bởi kiểu list, là một cấu trúc dữliệu tuần tự
cho phép lưu trữnhiều phần tửtrong cùng một biến. Không giống như chuỗi, danh sách
là kiểu dữliệu có thểthay đổi. Điều này có nghĩa là người lập trình có thểthêm, xóa hoặc
thay đổi phần tửtrong danh sách sau khi danh sách đã được tạo.
numbers = [1, 2, 3, 4, 5]
Danh sách có thểchứa các phần tửthuộc nhiều kiểu dữliệu khác nhau, điều này mang
lại sựlinh hoạt rất lớn trong lập trình Python.
9

CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
2.4.2
Truy cập và chỉnh sửa phần tửtrong List
Các phần tửtrong danh sách được truy cập thông qua chỉmục. Người lập trình có thể
thay đổi trực tiếp giá trịcủa một phần tửbằng cách gán giá trịmới cho vịtrí tương ứng.
numbers[0] = 10
numbers[-1] = 50
Khảnăng chỉnh sửa trực tiếp này là điểm khác biệt quan trọng giữa danh sách và các
kiểu dữliệu bất biến như chuỗi và tuple.
2.4.3
Thêm và xóa phần tửtrong List
Python cung cấp nhiều phương thức đểthao tác với danh sách. Phương thức append()
cho phép thêm một phần tửmới vào cuối danh sách, trong khi insert() cho phép chèn
phần tửvào một vịtrí bất kỳ.
numbers.append(6)
numbers.insert(2, 99)
Đểxóa phần tử, người lập trình có thểsửdụng các phương thức như remove(),
pop() hoặc câu lệnh del. Mỗi phương thức có cách hoạt động và mục đích sửdụng
khác nhau.
2.5
Kiểu dữliệu Tuple
2.5.1
Khái niệm và bản chất của Tuple
Tuple là một cấu trúc dữliệu dùng đểlưu trữmột tập hợp các phần tửtheo thứtựxác
định, tương tựnhư danh sách. Tuy nhiên, điểm khác biệt quan trọng nhất giữa tuple và list
là tuple có tính bất biến (immutable). Điều này có nghĩa là sau khi tuple được tạo ra, các
phần tửcủa nó không thểbịthay đổi, thêm mới hoặc xóa bỏ.
point = (10, 20)
Trong ví dụtrên, point là một tuple gồm hai phần tửbiểu diễn tọa độtrong mặt
phẳng. Sau khi được tạo, giá trịcủa point sẽkhông thểthay đổi trực tiếp.
2.5.2
Truy cập phần tửtrong Tuple

Tuple là kiểu dữliệu tuần tự, do đó các phần tửcủa tuple được truy cập thông qua chỉ
mục, hoàn toàn tương tựnhư danh sách và chuỗi.
x = point[0]
y = point[1]
Python cũng hỗtrợchỉmục âm khi làm việc với tuple, cho phép truy cập phần tửtừ
10

CHƯƠNG 2. KIỂU DỮLIỆU TUẦN TỰ
cuối vềđầu.
2.5.3
Tính bất biến và ý nghĩa thực tiễn
Tính bất biến của tuple mang lại nhiều lợi ích trong lập trình:
• Dữliệu an toàn hơn, tránh bịthay đổi ngoài ý muốn
• Có thểsửdụng tuple làm khóa trong dictionary
• Hiệu năng tốt hơn so với list trong một sốtrường hợp
Tuple thường được sửdụng để:
• Lưu trữcác nhóm dữliệu có cấu trúc cốđịnh (tọa độ, thông số)
• Trảvềnhiều giá trịtừmột hàm
• Biểu diễn các bản ghi dữliệu không thay đổi
2.5.4
Kiểu dữliệu Dictionary
2.5.5
Bản chất của Dictionary
Dictionary (từđiển) là kiểu dữliệu dùng đểlưu trữdữliệu dưới dạng ánh xạgiữa khóa
và giá trị. Mỗi phần tửtrong dictionary bao gồm một cặp key:value, trong đó khóa là
duy nhất và được dùng đểtruy cập nhanh đến giá trịtương ứng.
student = {
"name": "An",
"age": 20,
"score": 8.5
}
Khác với các kiểu dữliệu tuần tự, dictionary không truy cập dữliệu thông qua chỉmục
mà thông qua khóa.
2.5.6
Truy cập và thay đổi dữliệu trong Dictionary
Đểtruy cập giá trịtrong dictionary, người lập trình sửdụng khóa tương ứng.
print(student["name"])
Dictionary là kiểu dữliệu có thểthay đổi. Do đó, người lập trình có thểthêm mới,
thay đổi hoặc xóa các cặp khóa–giá trị.
student["age"] = 21
student["major"] = "Computer Science"
11
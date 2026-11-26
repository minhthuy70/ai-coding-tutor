<!-- page: 1 -->
# VI_PY_045: Cấu trúc điều kiện rẽ nhánh lồng nhau và phòng tránh lỗi logic

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý  
**Chuyên mục**: Điều khiển luồng | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 47 -->
CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
(b) if...else
(c) with
(d) for
3.7.2
Bài tập thực hành
Bài tập 1: Viết chương trình in ra màn hình thông tin cá nhân gồm họtên, tuổi và điểm
trung bình của sinh viên. Thông tin cần được trình bày rõ ràng trên từng dòng.
Bài tập 2: Viết chương trình nhập hai sốthực từbàn phím, tính tổng, hiệu, tích và
thương của hai sốđó, sau đó in kết quảra màn hình với định dạng dễđọc.
Bài tập 3: Viết chương trình in bảng cửu chương của một sốnguyên dương nhập từ
bàn phím. Bảng kết quảphải được trình bày theo dạng bảng, mỗi dòng là một phép nhân.
Bài tập 4: Viết chương trình nhập họtên và năm sinh của một người, sau đó in ra màn
hình tuổi hiện tại của người đó (giảsửnăm hiện tại là 2025).
Bài tập 5: Viết chương trình đọc một tập tin văn bản chứa danh sách các sốnguyên,
mỗi sốnằm trên một dòng. Tính tổng và trung bình cộng của các sốtrong tập tin, sau đó
in kết quảra màn hình.
Bài tập 6: Cho tập tin scores.txt lưu trữđiểm các môn học của sinh viên theo cấu
trúc:
TenMon,Diem
Viết chương trình đọc tập tin, tính điểm trung bình và in ra danh sách các môn có điểm
lớn hơn hoặc bằng điểm trung bình.
Bài tập 7: Viết chương trình cho phép người dùng nhập thông tin sinh viên gồm mã
sinh viên, họtên và điểm trung bình. Thông tin này được ghi vào tập tin. Sau đó, đọc lại
tập tin và in ra toàn bộdanh sách sinh viên.
Bài tập 8: Viết chương trình đọc một tập tin văn bản bất kỳvà đếm sốdòng, sốtừvà
sốký tựtrong tập tin đó. Kết quảđược in ra màn hình.
Bài tập 9: Viết chương trình ghi kết quảbảng điểm của một lớp học ra tập tin dưới
dạng bảng có căn lềrõ ràng. Mỗi dòng chứa tên sinh viên và điểm trung bình tương ứng.
Bài tập 10: Viết chương trình đọc dữliệu từmột tập tin chứa thông tin nhiều sinh viên
(mỗi sinh viên gồm mã, tên, điểm), thực hiện các yêu cầu sau:
• Tính điểm trung bình của toàn bộsinh viên
• Tìm sinh viên có điểm cao nhất
• Ghi kết quảthống kê ra một tập tin mới

<!-- page: 2 -->

32

<!-- page: 48 -->
CHƯƠNG 3. NHẬP XUẤT DỮLIỆU TRONG PYTHON
3.7.3
Gợi ý
Sinh viên nên sửdụng cấu trúc with khi làm việc với tập tin đểđảm bảo an toàn tài
nguyên, đồng thời chú ý định dạng dữliệu khi in ra màn hình nhằm nâng cao tính trực
quan và dễđọc của chương trình.
33

<!-- page: 49 -->
CHƯƠNG 4. Điều khiển luồng và câu lệnh điều kiện trong Python
Trong lập trình, không phải mọi chương trình đều thực hiện các câu lệnh theo một trình
tựcốđịnh từtrên xuống dưới. Thực tế, chương trình thường phải đưa ra quyết định dựa
trên điều kiện, từđó lựa chọn nhánh xửlý phù hợp. Cơ chếnày được gọi là điều khiển
luồng chương trình.
Trong Python, điều khiển luồng được xây dựng dựa trên các biểu thức logic và giá trị
Boolean. Việc hiểu rõ bản chất của giá trịBoolean, các toán tửlogic và cách chúng kết
hợp với nhau là nền tảng quan trọng đểsửdụng các câu lệnh điều kiện một cách chính
xác và hiệu quả.
4.1
Giá trịBoolean và vai trò trong điều khiển luồng
4.1.1
Khái niệm giá trịBoolean
Boolean là kiểu dữliệu logic chỉcó hai giá trị:
• True: biểu thịgiá trịđúng
• False: biểu thịgiá trịsai
Trong Python, kiểu Boolean được sửdụng đểbiểu diễn kết quảcủa các phép so sánh
và các phép toán logic. Các câu lệnh điều kiện như if, elif, else đều dựa trên giá trị
Boolean đểquyết định luồng thực thi của chương trình.
x = 5
print(x > 3)
Kết quả:
True
4.1.2
Biểu thức logic
Biểu thức logic là biểu thức khi được đánh giá sẽcho kết quảlà một giá trịBoolean.
Biểu thức logic thường được tạo thành từ:
• Các toán hạng (số, biến, biểu thức)
• Các toán tửso sánh hoặc toán tửlogic
4.2
Các toán tửtrảvềgiá trịBoolean
4.2.1
Toán tửso sánh

<!-- page: 3 -->

Các toán tửso sánh dùng đểso sánh hai giá trịvà trảvềkết quảBoolean.
34

<!-- page: 50 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
Toán tử
Ý nghĩa
==
Bằng nhau
!=
Khác nhau
>
Lớn hơn
<
Nhỏhơn
>=
Lớn hơn hoặc bằng
<=
Nhỏhơn hoặc bằng
a = 10
b = 20
print(a == b)
print(a < b)
Kết quả:
False
True
4.2.2
Toán tửkiểm tra thành viên
Python cung cấp các toán tửdùng đểkiểm tra sựtồn tại của phần tửtrong một tập hợp.
Toán tử
Ý nghĩa
in
Phần tửthuộc tập hợp
not in
Phần tửkhông thuộc tập hợp
numbers = [1, 2, 3, 4]
print(3 in numbers)
print(5 not in numbers)
Kết quả:
True
True
4.2.3
Toán tửso sánh đối tượng
Hai toán tửis và is not dùng đểso sánh danh tính của đối tượng trong bộnhớ,
không phải giá trịcủa chúng.

<!-- page: 4 -->

a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)
Kết quả:
35

<!-- page: 51 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
True
False
4.3
Các giá trịtương đương Boolean trong Python
4.3.1
Khái niệm Truthy và Falsy
Trong Python, không chỉTrue và False mới được dùng trong biểu thức điều kiện.
Mọi đối tượng đều có thểđược đánh giá là đúng hoặc sai trong ngữcảnh Boolean.
4.3.2
Các giá trịđược coi là False
Các giá trịsau được Python xem là False:
• False
• None
• Số0 dưới mọi dạng (0, 0.0)
• Chuỗi rỗng ""
• Danh sách, tuple, set, dictionary rỗng
print(bool(0))
print(bool(""))
print(bool([]))
Kết quả:
False
False
False
Mọi giá trịkhác đều được coi là True.
4.4
Toán tửlogic
4.4.1
Ba toán tửlogic cơ bản
Python cung cấp ba toán tửlogic cơ bản:
Toán tử
Ý nghĩa
and
Và
or
Hoặc
not

<!-- page: 5 -->

Phủđịnh
4.4.2
Bảng logic
Toán tửAND
36

<!-- page: 52 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
A
B
A and B
True
True
True
True
False
False
False
True
False
False
False
False
Toán tửOR
A
B
A or B
True
True
True
True
False
True
False
True
True
False
False
False
Toán tửNOT
A
not A
True
False
False

<!-- page: 6 -->

True
4.5
Thứtựưu tiên của các phép toán logic
Khi trong một biểu thức có nhiều toán tửlogic, Python sẽđánh giá theo thứtựưu tiên
sau:
1. not
2. and
3. or
result = not False or False and True
print(result)
Biểu thức trên tương đương với:
(not False) or (False and True)
Kết quả:
True
Việc sửdụng dấu ngoặc tròn giúp biểu thức rõ ràng hơn và tránh nhầm lẫn.
4.6
Các chú ý quan trọng khi làm việc với phép toán logic
Khi sửdụng các phép toán logic trong Python, cần lưu ý một sốđiểm sau:
• Tránh viết các biểu thức logic quá dài và phức tạp
• Nên sửdụng dấu ngoặc đểlàm rõ thứtựđánh giá
37

<!-- page: 53 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
• Phân biệt rõ giữa == và is
• Hiểu rõ khái niệm truthy và falsy đểtránh lỗi logic
4.7
Câu lệnh if – elif – else
Sau khi đã nắm vững các khái niệm vềgiá trịBoolean và các phép toán logic, bước tiếp
theo trong điều khiển luồng chương trình là sửdụng câu lệnh điều kiện. Trong Python,
câu lệnh if – elif – else cho phép chương trình lựa chọn và thực thi các khối lệnh
khác nhau tùy thuộc vào điều kiện logic.
Câu lệnh điều kiện là một trong những cấu trúc quan trọng nhất trong lập trình, giúp
chương trình có khảnăng đưa ra quyết định và xửlý linh hoạt các tình huống khác nhau.
4.7.1
Câu lệnh if
a, Cú pháp cơ bản
Câu lệnh if được sửdụng đểkiểm tra một điều kiện. Nếu điều kiện đúng (True),
khối lệnh bên trong if sẽđược thực thi.
if dieu_kien:
# khối lệnh được thực thi nếu điều kiện đúng
Trong Python, khối lệnh được xác định bằng thụt đầu dòng (indentation), thường là 4
dấu cách. Đây là đặc điểm quan trọng và bắt buộc của ngôn ngữPython.
b, Ví dụminh họa
x = 10

<!-- page: 7 -->

if x > 5:
print("x lon hon 5")
Kết quảhiển thị:
x lon hon 5
Nếu điều kiện không đúng, khối lệnh bên trong if sẽbịbỏqua và chương trình tiếp
tục thực hiện các câu lệnh phía sau.
4.7.2
Câu lệnh if – else
a, Cú pháp
Câu lệnh else được sửdụng đểchỉra khối lệnh sẽđược thực thi khi điều kiện trong
if là sai.
38

<!-- page: 54 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
if dieu_kien:
# khối lệnh nếu điều kiện đúng
else:
# khối lệnh nếu điều kiện sai
b, Ví dụminh họa
age = 16
if age >= 18:
print("Du dieu kien bo phieu")
else:
print("Chua du dieu kien bo phieu")
Kết quảhiển thị:
Chua du dieu kien bo phieu
Trong ví dụtrên, chương trình lựa chọn đúng một trong hai nhánh xửlý dựa trên giá
trịcủa điều kiện.
4.7.3
Câu lệnh if – elif – else
a, Nhu cầu sửdụng elif
Trong nhiều bài toán thực tế, chương trình cần kiểm tra nhiều điều kiện khác nhau chứ
không chỉhai trường hợp đúng hoặc sai. Khi đó, Python cung cấp từkhóa elif (viết tắt
của else if) đểkiểm tra các điều kiện bổsung.
b, Cú pháp tổng quát
if dieu_kien_1:
# khối lệnh 1
elif dieu_kien_2:
# khối lệnh 2
elif dieu_kien_3:
# khối lệnh 3
else:
# khối lệnh mặc định
Python sẽkiểm tra các điều kiện theo thứtựtừtrên xuống dưới. Khi gặp điều kiện đầu

<!-- page: 8 -->

tiên đúng, khối lệnh tương ứng sẽđược thực thi và các điều kiện phía sau sẽkhông được
kiểm tra nữa.
39

<!-- page: 55 -->
CHƯƠNG 4. ĐIỀU KHIỂN LUỒNG VÀ CÂU LỆNH ĐIỀU KIỆN TRONG PYTHON
c, Ví dụphân loại kết quảhọc tập
score = 7.8
if score >= 8.5:
print("Xep loai Gioi")
elif score >= 7.0:
print("Xep loai Kha")
elif score >= 5.0:
print("Xep loai Trung binh")
else:
print("Xep loai Yeu")
Kết quảhiển thị:
Xep loai Kha
Ví dụnày minh họa rõ cách Python chỉchọn một nhánh phù hợp nhất dựa trên thứtự
điều kiện.
4.7.4
Câu lệnh điều kiện lồng nhau
a, Khái niệm
Câu lệnh điều kiện lồng nhau là trường hợp bên trong một khối if hoặc elif lại chứa
một câu lệnh if khác. Cấu trúc này thường được sửdụng khi việc ra quyết định phụthuộc
vào nhiều mức điều kiện.
b, Ví dụminh họa
age = 20
has_id = True
if age >= 18:
if has_id:
print("Du dieu kien vao phong thi")
else:
print("Can giay to tuy than")
else:
print("Chua du tuoi")
Kết quảhiển thị:
Du dieu kien vao phong thi
Mặc dù điều kiện lồng nhau mạnh mẽ, nhưng nếu sửdụng quá nhiều mức lồng sẽlàm
chương trình khó đọc và khó bảo trì.
40
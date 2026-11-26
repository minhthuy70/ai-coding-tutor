<!-- page: 1 -->
# VI_PY_003: Toán tử số học, toán tử quan hệ và biểu thức điều kiện

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Toán tử | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 32 -->
1
Giới thiệu
Trước khi bắt đầu vào việc xửlý giải thuật, chúng ta phải thực hiện qua bước nhập
dữliệu đầu vào cho bài toán. Mặc dù là quy trình đầu tiên của một hệthống, độ
phức tạp của nó lại cao hơn nhiều so với việc xuất dữliệu. Một trong những khó
khăn cho quy trình này, là người dùng có thểnhập sai, hoặc không tuân theo cú
pháp dữliệu của chương trình. Điều này có thểdẫn tới việc xửlý dữliệu bịlỗi,
nặng hơn có thểlàm thoát chương trình của chúng ta. Vì vậy, khi làm các chương
trình lớn, luôn luôn đi kèm với quá trình nhập liệu, là quá trình xửlý lỗi dữliệu
đầu vào.
Trong hướng dẫn này, chúng tôi tập trung hướng dẫn việc nhập dữliệu từbàn
phím, và chỉtập trung vào dữliệu số, cũng như các phép toán cho dữliệu số. Một
kĩ thuật đơn giản nhưng hiệu quảđểxửlý lỗi dữliệu đầu vào cũng sẽđược giới
thiệu. Các cấu trúc dữliệu phức tạp hơn sẽđược trình bày ởnhững bài sau.
2
Câu lệnh nhập dữliệu
Đểkhởi tạo giá trịban đầu cho biến, ta có thểdùng lệnh gán đểgán một giá trịcho
biến. Những chương trình đưa dữliệu vào cho phép đưa dữliệu từbàn phím hoặc
từđĩa vào gán cho các biến, làm cho chương trình trởnên linh hoạt, có thểtính
toán với nhiều bộdữliệu đầu vào khác nhau.
Câu lệnh nhận dữliệu từbàn phím là input, có cú pháp như sau:
<tên biến> = input(<Thông báo>)
Lưu ý, giá trịnhận vào từbàn phím là giá trịkiểu chuỗi, vì vậy muốn trảvềgiá
trịkiểu gì ta phải ép kiểu cho giá trịđó. Thông thường, chúng ta cũng thêm 1 câu
thông báo đểhướng dẫn cho người dùng thông tin cần thiết cho việc nhập liệu,
chẳng hạn như ví dụbên dưới:
• Kiểu nguyên: a = int(input("Nhập sốnguyên a: "))
• Kiểu thực: b = float(input("Nhập sốthực b: "))
Trong bài hướng dẫn này, chúng ta sẽtìm hiểu 2 kiểu dữliệu sốthông dụng bậc
nhất khi mới bắt đầu với ngôn ngữlập trình, là kiểu sốnguyên và kiểu sốthực, sẽ
được trình bày ở2 phần tiếp theo.
3
Kiểu sốnguyên trên Python
3.1

<!-- page: 2 -->

Khai báo một biến kiểu sốnguyên
Với tính mềm dẻo và linh động, Python cho phép chúng ta không cần khai báo
biến lẫn xác định kiểu dữliệu cho nó. Chỉđơn giản bằng một phép gán, một biến
sẽđược tạo ra và Python tựđộng chọn kiểu dữliệu cho nó, phụthuộc vào giá trị
của phép gán. Đối với người lập trình bằng ngôn ngữPython, khai báo một biến
kiểu sốnguyên sẽthường sửdụng câu lệnh gán sau đây:
Trang 32
The Dariu Foundation

<!-- page: 33 -->
1 #Khai bao bien a, b la so nguyen
2 a = 5
3 b = int (6)
4 print(a, b)
Chương trình 3.1: Khai báo một biến là kiểu sốnguyên
Một cách truyền thống hơn, như ví dụởtrên, chúng ta có thểchỉđịnh kiểu cho
biến, bằng cách thêm từkhóa int. Tuy nhiên điều này thực sựkhông được sửdụng
nhiều với câu lệnh khai báo biến. Câu lệnh b = int(6) thực ra có 1 ý nghĩa lớn hơn,
là chuyển tất cảnhững gì trong dấu ngoặc sang sốnguyên. Nó sẽcó nhiều tác dụng
hơn trong phần hướng dẫn tiếp theo, là đọc biến từbàn phím.
3.2
Nhập sốnguyên từbàn phím
Một đoạn chương trình nhỏ, đểnhận sốnguyên từviệc nhập từbàn phím, như
sau:
1 a = int(input("Nhap so nguyen a: "))
2 print(a)
Chương trình 3.2: Nhận sốnguyên từbàn phím
Với chức năng này, bắt buộc chúng ta phải có từkhóa int chứkhông thểlược bỏ
như phần khai báo biến. Lý do là những gì nhập từbàn phím, là kiểu chuỗi. Từ
khóa int ởphía trước sẽlàm nhiệm vụchuyển đổi từkiểu chuỗi sang kiểu số. Do
đó, bạn có thểnhập vào sốnguyên 6 hoặc sốthập phân 6.1, thì giá trịcủa biến a
vẫn chỉcó giá trịlà 6 mà thôi.
3.3
Các phép toán trên sốnguyên
Trước khi thửnghiệm các phép toán trên sốnguyên, chúng ta sẽhiện thực một
đoạn chương trình nhỏ, là nhập 2 sốn n1 và n2 từbàn phím, và in ra tổng của 2 số.
Chương trình ví dụnhư sau:
1 n1 = int(input("So thu nhat: "))
2 n2 = int(input("So thu hai: "))
3
4 print("Tong cua 2 so: ", n1+n2)
Chương trình 3.3: Chương trình tính toán đơn giản trên 2 sốnguyên
Các phép toán phổbiến trên sốnguyên, được liệt kê ra như sau:
• + : Phép cộng
• - : Phép trừ

<!-- page: 3 -->

• * : Phép nhân
• //: Chia làm tròn
• / : Chia sốthực
• % : Chia lấy dư
Hướng dẫn lập trình Python cơ bản
Trang 33

<!-- page: 34 -->
• **: Phép mũ
Bây giờ, bạn có thểthửthay đổi phép toán trong Chương trình 3.3 đểhiểu rõ hơn
các phép toán được liệt kê ởtrên.
4
Kiểu sốthực trên Python
4.1
Khai báo một biến kiểu sốthực
Cũng tương tựnhư khi làm việc với sốnguyên, Python cho phép chúng ta không
cần khai báo biến lẫn xác định kiểu dữliệu cho nó. Chỉđơn giản bằng một phép
gán, một biến sẽđược tạo ra và Python tựđộng chọn kiểu dữliệu cho nó, phụ
thuộc vào giá trịcủa phép gán. Đối với người lập trình bằng ngôn ngữPython, khai
báo một biến kiểu sốthực sẽthường sửdụng câu lệnh gán sau đây:
1 #Khai bao bien a, b la so thuc
2 a = 5.2
3 b = float (6.7)
4 print(a, b)
Chương trình 3.4: Khai báo một biến là kiểu sốthực
4.2
Nhập sốthực từbàn phím
Một đoạn chương trình nhỏ, đểnhận sốthực từviệc nhập từbàn phím, như sau:
1 a = float(input("Nhap so thuc a: "))
2 print(a)
Chương trình 3.5: Nhận sốthực từbàn phím
Với chức năng này, bắt buộc chúng ta phải có từkhóa float chứkhông thểlược bỏ
như phần khai báo biến. Lý do là những gì nhập từbàn phím, là kiểu chuỗi. Từ
khóa float ởphía trước sẽlàm nhiệm vụchuyển đổi từkiểu chuỗi sang kiểu số. Do
đó, bạn có thểnhập vào sốnguyên 6, nó vẫn sẽlà con sốhợp lệđểchuyển sang số
thực.
4.3
Các phép toán trên sốthực
Trước khi thửnghiệm các phép toán trên sốnguyên, chúng ta sẽhiện thực một
đoạn chương trình nhỏ, là nhập 2 sốn n1 và n2 từbàn phím, và in ra tổng của 2 số.
Chương trình ví dụnhư sau:
1 n1 = float(input("So thu nhat: "))
2 n2 = float(input("So thu hai: "))
3
4 print("Tong cua 2 so: ", n1+n2)

<!-- page: 4 -->

Chương trình 3.6: Chương trình tính toán đơn giản trên 2 sốthực
Các phép toán phổbiến trên sốthực, cũng gần giống với sốnguyên, được liệt kê ra
như sau:
Trang 34
The Dariu Foundation

<!-- page: 35 -->
• + : Phép cộng
• - : Phép trừ
• * : Phép nhân
• / : Chia sốthực
• **: Phép mũ
Bây giờ, bạn có thểthửthay đổi phép toán trong Chương trình 3.7 đểhiểu rõ hơn
các phép toán được liệt kê ởtrên.
5
Xửlý lỗi nhập liệu
Đây sẽlà phần quan trọng bậc nhất trong việc xửlý dữliệu đầu vào. Khi đưa ra
thông báo đểnhập vào một sốnguyên, người sửdụng hoàn toàn có thểnhập vào
một chuỗi. Do đó, câu lệnh chuyển đổi kiểu có thểhoạt động sai và chương trình
phải dừng. Mặc dù Python sẽbỏqua lỗi nhập sốnguyên nhưng đầu vào lại là số
thực và ngược lại, vì 2 thông tin này cũng là số.
Đểxửlý cho trường hợp người dùng nhập vào chuỗi, hoặc gọi chung là giá trịsố
không hợp lệ, kĩ thuật đơn giản nhất là sửdụng câu lệnh try except, như chương
trình ví dụsau đây:
1 try:
2
a = int(input("Nhap so nguyen: "))
3 except:
4
a = 0
5 print(a)
Chương trình 3.7: Chương trình xửlý lỗi đầu vào
Trong đoạn chương trình trên, Python sẽcốgắng chuyển đổi giá trịchuỗi nhập vào
sang sốnguyên và gán nó vào biến a. Trong trường hợp quá trình này thất bại (do
dữliệu không hợp lệ), phần except sẽđược thực thi và a có giá trịlà 0. Ngược lại,
nếu việc chuyển đổi thành công, phần except sẽkhông được thực thi.
Hướng dẫn lập trình Python cơ bản
Trang 35

<!-- page: 36 -->
6
Câu hỏi ôn tập
1. Trong Python, cần phải khai báo một biến trước khi gán giá trịcho biến đó.
Nhận định trên đúng hay sai?
A. Đúng

<!-- page: 5 -->

B. Sai
2. Cách đểgán sốnguyên có giá trịlà 100 vào biến a là:
A. a := 100
B. a <- 100
C. a = 100
D. a « 100
3. Trong Python, một biến a được gán bằng 1 giá trịvới kiểu int, sau đó vẫn có thể
tiếp tục gán 1 giá trịcó kiểu float cho biến a. Nhận định trên đúng hay sai?
A. Sai
B. Đúng
4. Cho đoạn code như sau:
1 employeenumber = 4398
2 EmployeeNumber = 4398
3 employeeNumber = 4398
Nhận định nào dưới đây là đúng:
A. Các đoạn lệnh trên đều khởi tạo giá trịcho cùng 1 biến
B. Các đoạn lệnh trên khởi tạo giá trịcho các biến khác nhau
5. Hãy cho biết sau khi người dùng nhập giá trịxong thì kiểu dữliệu của biến N
trong đoạn lệnh sau là gì :
1 N = input("Nhap N") # Gia su nguoi dung nhap 5
2 print(N)
A. str
B. int
C. float
D. Không có kiểu dữliệu
6. Cho đoạn code như sau:
1 a = 4 / 2
Hãy cho biết kết quảvà kiểu dữliệu của biến a là gì:
A. a = 2.0, kiểu float
B. a = 2.0, kiểu int
C. a = 2, kiểu float
D. a = 2, kiểu int
Trang 36
The Dariu Foundation

<!-- page: 37 -->
7. Cho đoạn code như sau:
1 a = 5
2 b = 5.0
3 c = a + b
Hãy cho biết kết quảvà kiểu dữliệu của biến c là gì:
A. c = 10.0, kiểu float
B. c = 10, kiểu int
C. Báo lỗi do không thểcộng hai sốkhác kiểu
Đáp án

<!-- page: 6 -->

1. B
2. C
3. B
4. B
5. A
6. A
7. A
Hướng dẫn lập trình Python cơ bản
Trang 37

<!-- page: 38 -->
Trang 38
The Dariu Foundation

<!-- page: 39 -->
CHƯƠNG 4
Câu lệnh điều kiện IF

<!-- page: 40 -->
1
Giới thiệu
Trong bất kì một ngôn ngữlập trình nào, sẽđều có câu lệnh điều kiện. Nhờcâu
lệnh này, mà việc ánh xạnhững tác vụđược thực thi khi điều kiện nào đó xảy ra,
mới có thểđược hiện thực trên máy tính. Khi chúng ta nói "Nếu trời mưa thì tôi sẽ
mang dù", là một ví dụcho hành vi mang dù chỉđược thực hiện khi có trời mưa.
Trong ngôn ngữlập trình, trời mưa được xem là một điều kiện. Khi điều kiện này
là đúng, máy tính sẽthực hiện một chức năng nào đó, như là việc mang dù chẳng
hạn. Cũng từbài này, chúng ta chính thức bắt đầu vào khái niệm xửlý trên máy
tính. Những bài toán ngày một phức tạp hơn và cần phải có sựkết hợp của nhiều
câu lệnh phức tạp.
Trong ngôn ngữlập trình Python, một điều kiện đơn giản thường được thểhiện
qua một phép so sánh. Và một biểu thức so sánh sẽtrảvềkết quảcó có kiểu dữ
liệu là Boolean, tức là True hay False. Các toán tửso sánh có thểđược kểđến như
sau:
• So sánh bằng: a == b
• Khác nhau: a! = b
• Bé hơn: a < b
• Bé hơn hoặc bằng: a <= b
• Lớn hơn: a > b
• Lớn hơn hoặc bằng: a >= b
Ởđây a và b là ví dụcho 2 biến số. Tuy nhiên chúng ta cũng có thểso sánh giữa
một biến sốvà 1 hằng số, tương tựnhư những ngôn ngữlập trình các. Ngoài ra,
các toán tửluận lý như and và or cũng có thểsửdụng khi xét điều kiện kết hợp của
nhiều mệnh đềluận lí.
Thực ra, câu lệnh điều kiện if có nhiều cách sửdụng khác nhau, thông qua nhiều

<!-- page: 7 -->

biến thểcủa nó. Trong tài liệu này, chúng tôi phân ra 3 câu lệnh, bao gồm câu lệnh
if đơn giản, câu lệnh if else và câu lệnh if elif else. Cách sửdụng cũng như ý nghĩa
của từng câu lệnh trong Python lần lượt được trình bày bên dưới.
2
Câu lệnh if
Đây là câu lệnh đơn giản nhất, co cấu trúc câu lệnh điều kiện như sau:
1 if <Dieu_Kien >:
2
<Cau_Lenh >
Trong cấu trúc này, nếu điều kiện là đúng, thì các câu lệnh mới được thực thi.
Ngược lại, nếu điều kiện là sai, thì các câu lệnh sẽkhông được thực thi. Bắt buộc
chúng ta phải có ít nhất một câu lệnh theo sau câu lệnh if, nếu không chương trình
sẽbáo lỗi.
Trang 40
The Dariu Foundation
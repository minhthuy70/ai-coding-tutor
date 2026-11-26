# VI_PY_014: Thiết kế giao diện người dùng Desktop GUI căn bản với Python

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Giao diện GUI | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

1
Giới thiệu
Cũng như các ngôn ngữlập trình cấp cao khác, Python cho chúng ta cơ hội để
hiện thực các ứng dụng với giao diện thân thiện. Các ứng dụng này được gọi là ứng
dụng Winform. Sởdĩ có tên như vậy, là vì giao diện của ứng dụng thực sựgiống với
các ứng dụng mà chúng ta đang sửdụng trên hệđiều hành Windows.
Trong bài hướng dẫn này, chúng ta sẽthiết kếmột ứng dụng đơn giản: Người dùng
nhập vào 2 sốvà nhấn nút Cộng. Kết quảsẽđược in ra trên chương trình, như minh
họa ởhình bên dưới:
Hình 14.1: Một ứng dụng giao diện trên Python
Rõ ràng, một chương trình như minh họa ởHình 14.1 sẽthân thiện hơn với rất
nhiều người dùng, thay vì chỉtương tác từmàn hình console như các ứng dụng
truyền thống như Pascal hoặc phần hướng dẫn cơ bản của Python. Tuy nhiên, với
ứng dụng như vậy, chúng ta sẽcần phải tỉmỉờphần thiết kếgiao diện, trước khi
bắt đầu lập trình. Điều đặc biệt là trên Python, chúng ta sẽlập trình đểtạo ra giao
diện, thay vì kéo thảđểthiết kếgiao diện như các ngôn ngữcao cấp khác. Trong
bài hướng dẫn này, chúng tôi sẽtrình bày những câu lệnh đơn giản nhất đểthiết
kếra ứng dụng như trình bày ởHình 14.1.
2
Thiết kếgiao diện
Trên Python, đã có hỗtrợsẵn thư viện thiết kết giao diện là tkinter. Nguyên lý của
việc lập trình giao diện là chúng ta sẽtạo ra một cửa sổ(Windows), sau đó thêm
các đối tượng giao diện vào (khung nhập liệu, nút nhấn, v.v...). Chúng ta sẽbắt đầu
bước đầu tiên, là tạo ra cửa sổgiao diện, với chương trình sau đây:
1 import
tkinter as tk
2
3 window = tk.Tk()
4
5 window.title("Python App")
6 window.geometry("300 x200")
7

The Dariu Foundation

8 window.mainloop ()
Chương trình 14.1: Tạo ra cửa sổ(Windows) cho ứng dụng
Trong Chương trình 14.1, câu lệnh đầu tiên dùng đểthêm thư viện thiết kếgiao
diện tkinter. Vì sau này, chúng ta sẽphải gõ rất nhiều từkhóa tkinter, chúng ta đặt
cho nó một tên viết tắt, là tk. Tiếp theo đó, chúng ta tạo ra một cửa sổbằng câu
lệnh tk.Tk(), thay đổi các thông sốcủa cửa sổnhư tiêu đề, kích thước của cửa sổ
(ngang 300 và cao 200 pixel). Cuối cùng, chúng ta sẽkích hoạt cửa sổđó lên bằng
câu lệnh window.mainloop(). Khi chạy chương trình này, chúng ta sẽcó kết quả
như sau:
Hình 14.2: Cửa sổứng dụng trên Windows
Kết quảchương trình ởHình 14.2 là lý do tại sao ứng dụng được gọi là ứng dụng
winform, bởi nó có cấu trúc mặc định của một cửa sổtrên hệđiều hành Windows:
nút thu nhỏ, phóng to, tắt cửa sổcũng như thanh tiêu đềtrên ứng dụng.
3
Thêm đối tượng giao diện vào cửa sổ
Sau khi đã có khung cửa sổtiêu chuẩn, chúng ta bắt đầu thêm các đối tượng giao
diện vào. Đểcó thểhiển thịhướng dẫn nhập sốA, chúng ta cần 2 đối tượng giao
diện: Lable và Text. Đối tượng Label chỉdùng đểhiển thị, còn Text là đối tượng
dùng đểnhập liệu. Đối với mỗi đối tượng, chúng ta phải dùng 2 câu lệnh: Tạo ra
đối tượng và định vịtrí của nó trong khung cửa sổ. Chương trình cho phần này sẽ
như sau:
1 import
tkinter as tk
2
3 window = tk.Tk()
4
5 window.title("Python App")
6 window.geometry("300 x200")
7
8 labelA = tk.Label(text="Nhap so A: ")
9 labelA.place(x=5, y=5, width = 80, height = 30)
10
11 txtA = tk.Text ()
Hướng dẫn lập trình Python cơ bản

12 txtA.place(x = 80, y =5, width = 100, height = 30)
13
14 window.mainloop ()
Chương trình 14.2: Tạo ra cửa sổ(Windows) cho ứng dụng
Trong Chương trình 14.3, các thông sốvềx, y là vịtrí của đối tượng trong giao diện,
width và height là kích thước chiều rộng và cao của đối tượng. Bạn hãy thửthay

đổi nó đểthấy hiệu ứng thay đổi trên giao diện. Với đoạn chương trình trên, kết
quảcủa chúng ta sẽnhư sau:
Hình 14.3: Thêm đối tượng giao diện lên ứng dụng
Tiếp tục làm tương tựnhư vậy đểthêm phần hướng dẫn nhập sốB, và phần hiển
thịkết quả. Hãy lưu ý rằng chiều cao của dòng đầu tiên đang là 30, và tọa độy đang
là 5. Nên dòng thứ2 tối thiểu tọa độy phải là 35. Chúng tôi cho tọa độy của dòng 2
là 40 đểcó được một khoảng trống vừa phải. Tương tựnhư vậy, dòng 3 tọa độy sẽ
là 80. Nút nhấn sẽđược thêm vào cuối cùng. Chương trình hoàn thiện của chúng
ta như sau:
1 import
tkinter as tk
2
3 window = tk.Tk()
4
5 window.title("Python App")
6 window.geometry("300 x200")
7
8 labelA = tk.Label(text="Nhap so A: ")
9 labelA.place(x=5, y=5, width = 80, height = 30)
10
11 txtA = tk.Text ()
12 txtA.place(x = 80, y =5, width = 100, height = 30)
13
14 labelB = tk.Label(text="Nhap so B: ")
15 labelB.place(x=5, y= 40, width = 80, height = 30)
16
17 txtB = tk.Text ()
18 txtB.place(x = 80, y =40, width = 100, height = 30)

The Dariu Foundation

19
20 labelKQ = tk.Label(text="Ket Qua: ")
21 labelKQ.place(x=5, y= 75, width = 80, height = 30)
22
23 txtKQ = tk.Text ()
24 txtKQ.place(x = 80, y =75, width = 100, height = 30)
25
26 button = tk.Button(text = "Tong")
27 button.place(x = 5, y = 125, width =100, height = 50)
28
29 window.mainloop ()
Chương trình 14.3: Thiết kếgiao diện hoàn chỉnh cho ứng dụng
Cuối cùng, giao diện của ứng dụng của chúng ta sẽnhư minh họa ởHình 14.4.

Hình 14.4: Thiết kếgiao diện hoàn chỉnh
Hướng dẫn lập trình Python cơ bản

4
Câu hỏi ôn tập
1. Ứng dụng chạy trên Windows gọi là gì?
A. Winform
B. Console
C. Log
D. Tất cảđều đúng
2. Đểlập trình giao diện bằng Python trên PyCharm cần phải:
A. Kéo và thảđối tượng giao diện vào chương trình
B. Viết chương trình tạo ra giao diện
C. Python không hỗtrợlập trình giao diện
D. Tất cảđều sai
3. Thông thường, đểin thông tin hướng dẫn trên ứng dụng, đối tượng giao diện
nào sẽđược dùng?
A. Label
B. Text
C. Button
D. Windows
4. Thông thường, đểngười dùng nhập thông tin vào ứng dụng, đối tượng giao
diện nào sẽđược dùng?
A. Label
B. Text
C. Button
D. Windows
5. Thông thường, đểnhận tương tác từngười dùng, chẳng hạn như nhấp chuột,
đối tượng giao diện nào sẽđược dùng?
A. Label
B. Text
C. Button
D. Windows
6. Đểchỉnh vịtrí của đối tượng giao diện trên ứng dụng, chúng ta sẽcan thiệp
vào thuộc tính nào?
A. Tọa độx và tọa độy
B. Thông sốwidth và height
C. Cả2 câu trên đều đúng
D. Tất cảđều sai
7. Đểchỉnh kích thước của đối tượng giao diện trên ứng dụng, chúng ta sẽcan
thiệp vào thuộc tính nào?
A. Tọa độx và tọa độy
B. Thông sốwidth và height

C. Cả2 câu trên đều đúng
D. Tất cảđều sai
Đáp án
1. A
2. B
3. A
4. B
5. C
6. A
7. B

The Dariu Foundation

CHƯƠNG 15
Tạo hàm xửlý cho nút nhấn

1
Giới thiệu
Sau khi thiết kếxong giao diện, bước tiếp theo chúng ta cần phải tạo hàm xửlý khi
người dùng nhấn vào nút Tong. Nút nhấn gần như là đối tượng tương tác chính
của người dùng lên ứng dụng chạy trên máy tính. Hàm mà chúng ta chuẩn bịtạo
sẽđược tựđộng gọi khi người dùng nhấp vào nút nhấn.
2
Khai báo hàm xửlý
Trước tiên, chúng ta sẽkhai báo một hàm, đặt tên là onClick trên Python. Hàm này
trước mắt chỉin ra 1 thông báo ngắn, như ví dụbên dưới:
1 def onClick ():
2
print("Nhan nut")
Chương trình 15.1: Khai báo hàm onClick
Tiếp theo, chúng ta cần liên kết sựkiện nhấn nút Tong với hàm onClick này. Trong
câu lệnh khởi tạo nút nhấn ởbài trước, chúng ta hiệu chỉnh lại như sau:
1 button = tk.Button(text = "Tong", command = onClick)
Chương trình 15.2: Khai báo hàm onClick
Lưu ý quan trọng là chúng ta phải khai báo hàm onClick trước khi gán nó cho sự
kiện nút nhấn. Chương trình hoàn chỉnh của chúng ta sẽnhư sau
1 import
tkinter as tk
2
3 def onClick ():
4
print("Nhan nut")
5

6 window = tk.Tk()
7 window.title("Python App")
8
9 labelA = tk.Label(text="Nhap so A: ")
10 labelA.place(x=5, y=5, width = 80, height = 30)
11
12 txtA = tk.Text ()
13 txtA.place(x = 80, y =5, width = 100, height = 30)
14
15 labelB = tk.Label(text="Nhap so B: ")
16 labelB.place(x=5, y= 40, width = 80, height = 30)
17
18 txtB = tk.Text ()
19 txtB.place(x = 80, y =40, width = 100, height = 30)
20
21 labelKQ = tk.Label(text="Ket Qua: ")
22 labelKQ.place(x=5, y= 75, width = 80, height = 30)
23
24 txtKQ = tk.Text ()

The Dariu Foundation

25 txtKQ.place(x = 80, y =75, width = 100, height = 30)
26
27 button = tk.Button(text = "Tong", command = onClick)
28 button.place(x = 5, y = 125, width =100, height = 50)
29
30 window.geometry("300 x200")
31 window.mainloop ()
Chương trình 15.3: Hoàn thiện chương trình với sựkiện nút nhấn
3
Hiện thực hàm xửlý cho nút nhấn
Đểhiện thực cho hàm này, chúng ta cần phải lấy thông tin từ2 đối tượng là txtA và
txtB. Dữliệu từ2 đối tượng này đều là kiểu chuỗi, nên chúng ta phải đổi sang kiểu
dữliệu mong muốn, trong trường hợp này là dữliệu số. Đến bước này thì mọi việc
đã trởnên đơn giản hơn nhiều, chúng ta tính tổng của 2 s . Và cuối cùng là xuất kết
quảra txtKQ. Chương trình hướng dẫn cho hàm xửlý sựkiện này như sau:
1 def onClick ():
2
print("Nhan nut")
3
a = int(txtA.get("1.0"))
4
b = int(txtB.get("1.0"))

5
6
kq = a + b
7
8
txtKQ.delete (1.0)
9
txtKQ.insert (1.0, kq)
Chương trình 15.4: Hoàn thiện chương trình với sựkiện nút nhấn
Chương trình 15.4 là ví dụcho những thao tác xửlý cơ bản từviệc lấy dữliệu từ
Text, xửlý và xuất kết quảra lại trên một đối tượng Text. Trước khi xuất dữliệu mới,
chúng ta cần phải xóa đi dữliệu cũ. Con số"1.0" trong chương trình có ý nghĩ là
hàng 1, vịtrí đầu tiên (vịtrí 0). Đối với câu lệnh get, thì nó có nghĩa là đọc dữliệu
tại hàng 1, vịtrí đầu tiên đến hết. Đối với câu lệnh delete, nó có nghĩa là xóa toàn
bộhàng 1. Câu lệnh insert tức là thêm dữliệu mới ởhàng 1, từvịtrí đầu tiên.
Bây giờ, bạn đã có thểchạy chương trình, nó là mô phỏng cho việc tính tổng của 2
số. Chương trình sẽvẫn chạy cho đến khi bạn nhấn vào biểu tượng đóng cửa sổở
góc trên bên phải.
4
Bài tập
1. Hãy viết chương trình tính nghiệm của phương trình bậc nhất, với các hệsốa và
b được nhập vào từgiao diện. 2. Hãy viết chương trình giải phương trình bậc 2, với
các hệsốa, b và c được nhập từgiao diện.
Hướng dẫn lập trình Python cơ bản

5
Câu hỏi ôn tập
1. Đểtạo hàm xửlý sựkiện cho một nút nhấn, chúng ta cần phải làm gì?
A. Định nghĩa một hàm, ví dụlà def onClick()
B. Khai báo nó trong lệnh khởi tạo nút nhấn bằng lệnh command = onClick
C. Thực hiện cả2 bước trên
D. Tất cảđều sai
2. Câu phát biểu nào là đúng vềhàm xửlý sựkiện cho nút nhấn:
A. Nó phải được khai báo trước nút nhấn
B. Được khai báo ởbất kì vịtrí nào trong chương trình
C. Không cầu phải khai báo, Python mặc định gọi
D. Tất cảđều sai
3. Các bước đểhiện thực hàm xửlý xửkiện nút nhấn trên Python là gì?
A. Lấy dữliệu từgiao diện vào
B. Xửlý dữliệu
C. Xuất dữliệu ra giao diện
D. Tất cảđều đúng
4. Ý nghĩa của câu lệnh txtA.get("1.0") là gì?

A. Đọc toàn bộdữliệu của txtA
B. Xuất dữliệu ra txtA từvịtrí đầu tiên
C. Python không hỗtrợlệnh này
D. Tất cảđều sai
5. Ý nghĩa của câu lệnh txtA.insert("1.0") là gì?
A. Đọc toàn bộdữliệu của txtA
B. Xuất thêm dữliệu ra txtA từvịtrí đầu tiên
C. Python không hỗtrợlệnh này
D. Tất cảđều sai
6. Ý nghĩa của câu lệnh txtA.delete("1.0") là gì?
A. Xóa toàn bộdữliệu của txtA
B. Xóa dữliệu của txtA từhàng 1, vịtrí đầu tiên cho đến hết
C. Cả2 phát biểu trên đều đúng
D. Tất cảđều sai
Đáp án
1. A
2. A
3. D
4. A
5. B
6. C

The Dariu Foundation

CHƯƠNG 16
Xửlý lỗi trên giao diện

1
Giới thiệu
Thông qua dựán hiện thực một ứng dụng có giao diện trên Windows bằng ngôn
ngữPython, bạn có thểthấy rằng, việc xửlý của chúng ta chỉcó đúng 1 dòng lệnh,
là tính tổng 2 số. Còn lại, tất cảcác dòng lệnh chủyếu là dùng cho việc thiết kết
giao diện, lấy dữliệu từcác Text trên giao diện và xuất kết quảlại ra giao diện.
Tuy nhiên, cũng giống như bao ứng dụng khác, việc xửlý lỗi cho phần dữliệu đầu
vào luôn luôn phải được chú ý, đểgiúp cho ứng dụng trởnên thực tếhơn và tương
tác dễhơn với người sửdụng. Trong ứng dụng này, chúng ta đang mặc định là phải
nhập vào một sốnguyên. Tuy nhiên người dùng có thểnhập vào một chuỗi và
chương trình của chúng ta sẽbịbáo lỗi.
Bên cạnh việc dùng câu lệnh try except, trong bài này sẽhướng dẫn chúng ta cách
hiển thịmột hộp thông báo lỗi (message box), như minh họa ởhình bên dưới:
Hình 16.1: Thông báo báo lỗi từchương trình
Những thông báo như trên mới sẽlàm cho chương trình chúng ta trởnên thân
thiện hơn người dùng rất nhiều, thay vì chỉin ra những dòng chữtrên giao diện

Console.
2
Xửlý lỗi nhập liệu
Vềnguyên tắc, bất kì quy trình nhận dữliệu nào từphía người dùng cũng cần phải
được kiểm tra lỗi. Ởđây, chúng ta mong đợi người dùng sẽnhập vào một số, nên
viết câu lệnh chuyển nó qua sốnguyên. Một câu lệnh vô cùng mạnh mẽhỗtrợcho
chúng ta trong việc xửlý lỗi là try except. Bây giờ, trong phần except, chúng ta sẽ
hiển thịthêm thông báo lỗi.
Đầu tiên, chúng ta cần phải thêm thư viện cho việc hiển thịthông báo lỗi, bằng
câu lệnh import ởđầu chương trình, như sau:
1 import tkinter as tk
2 from tkinter import messagebox
Chương trình 16.1: Khai báo hàm onClick

The Dariu Foundation

Chương trình cho hàm xửlý sựkiện nhấn nút của chúng ta sẽnhư sau:
1
2 def onClick ():
3
4
print("Nhan nut")
5
try:
6
a = int(txtA.get("1.0"))
7
except:
8
messagebox.showerror("Loi Nhap Lieu", "Xin vui long
kiem tra lai so A")
9
return
10
try:
11
b = int(txtB.get("1.0"))
12
except:
13
messagebox.showerror("Loi Nhap Lieu", "Xin vui long
kiem tra lai so B")
14
return

15
16
c = a + b
17
18
txtKQ.delete (1.0)
19
txtKQ.insert (1.0, c)
Chương trình 16.2: Bắt lỗi và thông báo khi nhập dữliệu từngười dùng
Bạn hãy lưu ý cách sửdụng câu lệnh return: Khi xảy ra lỗi nhập liệu, chúng ta
thông báo cho người dùng và đồng thời phải dừng luồng xửlý bên dưới. Câu lệnh
return dùng đểthoát khỏi hàm xửlý sựkiện hiện tại, bởi đơn giản, dữliệu đầu vào
chưa hợp lệthì chúng ta chưa xửlý.
Các thao tác khôi phục lại giao diện của chương trình, chẳng hạn như khi người
dùng nhập sai dữliệu, chúng ta thông báo nhưng đồng thời cũng xóa dữliệu nhập
sai, sẽxem như là phần nâng cao cho người đọc tựhoàn thiện. Bạn có thểsửdụng
tiếng Việt trong câu thông báo. Trong giáo trình này, do font chữcho ngôn ngữ
Python, chúng tôi không thểdùng tiếng Việt có dấu.
Đến đây, bạn đã có thểtựxây dựng những ứng dụng lớn hơn, chẳng hạn như phần
mềm Calculator mà chúng ta đang sửdụng trên máy tính, hoặc các phần mềm hỗ
trợhọc Toán cho học sinh cấp 2 cấp 3.
Hướng dẫn lập trình Python cơ bản

3
Câu hỏi ôn tập
1. Tại sao chúng ta phải xửlý lỗi nhập liệu?
A. Chương trình sẽchạy sai nếu dữliệu không hợp lệ
B. Python không thực hiện được việc xửlý nếu dữliệu đầu vào không hợp lệ
C. Chương trình sẽbịthoát nếu dữliệu không hợp lệ
D. Tất cảđều đúng
2. Một công cụhiệu quảđểthông báo lỗi cho người dùng là:
A. Hiện chữtrên màn hình console
B. Hiện hộp thông báo trên ứng dụng
C. Không cầu phải làm gì, Python tựxửlý
D. Tất cảđều đúng
3. Các thêm thư viện đểsửdụng hộp thông báo (messageBox) là gì?
A. from tkinter import messagebox
B. from messagebox import tkinter
C. import messagebox
D. Tất cảđều đúng
4. Phát biểu nào sau đây là đúng cho messageBox?
A. Message box có thểhiển thịđược tiếng Việt
B. Đóng message box bằng cách nhấn vào nút OK

C. Có thểthay đổi tiêu đềcủa message box
D. Tất cảđều đúng
5. Ý nghĩa của câu lệnh return là gì?
A. Đóng ứng dụng hiện tại
B. Thoát khỏi luồng xửlý của hàm hiện tại
C. Tất cảđều đúng
D. Tất cảđều sai
Đáp án
1. D
2. B
3. A
3. D
4. D
5. B

The Dariu Foundation
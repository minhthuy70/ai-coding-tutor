# VI_PY_008: Danh sách List, bộ giá trị Tuple và các thao tác biến đổi dữ liệu

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Cấu trúc dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

4
Đọc mảng 1 chiều từFile
Đây là một yêu cầu thường xuyên sửdụng ởcác ngôn ngữnhư Pascal hay C. Đểcó
thểđọc 1 mảng 1 chiều từfile, thường chúng ta sẽphải quy định cấu trúc của file
đó. Giảsửchúng ta sẽquy định dòng đầu tiên của file là sốphần tửtrong mảng,
các dòng tiếp theo là các phần tửcủa mảng, mỗi dòng chỉchứa một phần tử. Nội
dung của 1 file như vậy sẽnhư sau:
Hình 8.2: File chứa dữliệu của 1 mảng 1 chiều 3 phần tử
Rõ ràng, việc đọc dữliệu từfile này và lưu vào một mảng khá đơn giản: đọc số
lượng phần tửvà dùng 1 vòng for đểđọc tiếp. Câu lệnh chính sẽsửdụng là read-
line, như minh họa sau đây:
1 file = open("test.txt", "r")
2 a = []
3 N = int(file.readline ())
4 for i in range(0,N):
5
temp = int(file.readline ())
6
a.append(temp)
7 print(a)
8 file.close ()
Chương trình 8.4: Đọc mảng một chiều từfile
Một bài toán phức tạp hơn, đó là trong file không có thông tin vềkích thước. Các
phần tửcủa mảng cách nhau bằng khoảng trắng và viết liền nhau trên một hàng
như minh họa ởHình 8.3.
Hình 8.3: Mảng 1 chiều không có thông tin vềsốphần tử
Với yêu cầu như trên, việc đọc dữliệu vào với các ngôn ngữkhác có thểsẽphức
tạp. Tuy nhiên với sựhỗtrợcủa Python, công việc này cực kì đơn giản. Chúng ta
chỉviệc đọc hết dòng dữliệu, và cắt nó ra bằng câu lệnh split(). Chương trình gợi
ý cho yêu cầu này như sau:

The Dariu Foundation

1 file = open("test.txt", "r")
2 a = []
3 data = file.readline ().split ()
4 for i in data:
5
temp = int(i)
6
a.append(temp)
7 print(a)
8 file.close ()
Chương trình 8.5: Đọc mảng không có thông tin vềsốphần tử
Sau khi dùng toán tửsplit(), bản thân biến data đã là mảng 1 chiều. Tuy nhiên, các
phần tửcủa nó đang là chuỗi ký tự. Vòng lặp for tiếp theo chỉđơn giản là chuyển
từkiểu ký tựsang kiểu sốnguyên, rồi nối vào mảng a của chúng ta. Một lỗi quan
trọng mà người dùng có thểgặp phải, là tựnhấn thêm ký tựEnter vào file text.
Điều này làm cho việc ép kiểu sang sốnguyên sẽxảy ra lỗi.
Thông qua ví dụnày, chúng tôi cũng muốn trình bày một cách khác đểdùng vòng
lặp for. Với cách dùng này, chúng ta không quan tâm tới chỉsốcủa phần tửtrong
mảng, mà chỉquan tâm tới việc duyệt hết mọi phần tửtrong mảng mà thôi. Ởcách
dùng này, biến data được xem là một tập hợp, và i sẽlần lượt là các giá trịtrong tập
hợp đó.
5
Đọc mảng nhiều chiều từFile
Trong yêu cầu này, chúng ta sẽđọc một mảng 2 chiều từfile: mỗi hàng của file là
một hàng của ma trận và không có ràng buộc là sốlượng phần tửcủa mỗi hàng
phải bằng nhau. Dữliệu của file test.txt như sau:
Hình 8.4: Dữliệu mảng nhiều chiều trong file
Chương trình gợi ý cho yêu cầu này sẽnhư sau:
1 file = open("test.txt", "r")
2 a = []
3
4 for i in file:
5
data = i.split ()
6
temp_row = []
7
for j in data:
8
temp = int(j)
9
temp_row.append(temp)
10
a.append(temp_row)
Hướng dẫn lập trình Python cơ bản

11 print(a)
12 file.close ()
Chương trình 8.6: Đọc mảng nhiều chiều từfile
Một lần nữa, cấu trúc mới của vòng for còn được thểhiện cho cảđối tượng file.
Chính nhờsựmềm dẻo trong Python, câu lệnh của chương trình đã được rút ngắn
rất nhiều. Những công cụnày được chúng tôi trình bày vì muốn rút ngắn thời gian
cho việc xửlý dữliệu đầu vào, đểngười học có thểtập trung vào việc xửlý giải thuật
tính toán phức tạp hơn. Thực ra, file cũng là một cấu trúc thuộc dạng tập hợp, với
mỗi phần tửcủa nó là một hàng. Do đó, chúng ta mới có thểviết được vòng for i
in file như trên. Khi đã truy xuất tới từng hàng, việc tách từng phần tửvà ép kiểu
vềsốnguyên là tương tựvới việc đọc mảng một chiều.

The Dariu Foundation

6
Bài tập
1. Đọc giá trịcủa mảng 1 chiều từfile "input.txt" và xuất kết quảra màn hình. Giả
sử, các giá trịtrong file đều nằm trên một dòng, cách nhau bởi 1 khoảng trắng.
1 # file input.txt duoc dat chung voi file chua code
2 f = open("input.txt", encoding = ’utf -8’)
3 x = f.readline ()
4 print(x)
5 f.close ()
Chương trình 8.7: Đáp án gợi ý cho Bài 1
2. Ghi giá trịtừng phần tửcủa một cho trước trên từng dòng vào file "output.txt"
1 a = [1,2,3,4,5]
2 f = open("output.txt","w")
3 for i in range(0,len(a)):
4
f.write(str(a[i] )+ "\n")
5 f.close ()
Chương trình 8.8: Đáp án gợi ý cho Bài 2
3. Đọc giá trịcủa mảng 1 chiều từfile "input.txt", tính giá trịtrung bình của mảng
đó và xuất kết quảra màn hình. Giảsử, các giá trịtrong file đều nằm trên một dòng,
cách nhau bởi 1 khoảng trắng.
1 # file input.txt duoc dat chung voi file chua code
2 f = open("input.txt", encoding = ’utf -8’)
3 x = f.readline ()
4 a = x.split ()
5 tb = 0
6 for i in range(0,len(a)):

7
tb = tb + int(a[i])
8 tb = tb / len(a)
9 print(tb)
10 f.close ()
Chương trình 8.9: Đáp án gợi ý cho Bài 3
4. Tương tựbài 3 nhưng giá trịcuối cùng được ghi vào file "output.txt"
1 # file input.txt duoc dat chung voi file chua code
2 f = open("input.txt", encoding = ’utf -8’)
3 x = f.readline ()
4 a = x.split ()
5 tb = 0
6 for i in range(0,len(a)):
7
tb = tb + int(a[i])
8 tb = tb / len(a)
9 fw = open("output.txt","w")
10 fw.write("Gia tri trung binh la: " + str(tb))
11 f.close ()
12 fw.close ()
Chương trình 8.10: Đáp án gợi ý cho Bài 4
Hướng dẫn lập trình Python cơ bản

7
Câu hỏi ôn tập
1. Mởfile với chếđộmode ’wb’ có ý nghĩa gì?
A. Mởfile đểghi.
B. Mởfile đểđọc và ghi.
C. Mởfile đểghi cho dạng nhịphân.
D. Mởfile đểđọc và ghi cho dạng nhịphân.
2. Đoạn code dưới đây có ý nghĩa gì?
1 f = open("sample.txt")
A. Mởfile sample.txt được phép đọc và ghi vào file.
B. Mởfile sample.txt và chỉđược phép đọc file.
C. Mởfile sample.txt và được phép ghi đè vào file
D. Mởfile sample.txt và được phép ghi tiếp vào file.
3. Đoạn code dưới đây có ý nghĩa gì?
1 f = open("sample.txt", "a")
A. Mởfile sample.txt được phép đọc và ghi vào file.
B. Mởfile sample.txt và chỉđược phép đọc file.
C. Mởfile sample.txt và được phép ghi đè vào file
D. Mởfile sample.txt và được phép ghi tiếp vào file.
4. Điều gì sẽxảy ra khi mởmột file không tồn tại?

A. Python tựđộng tạo một file mới dưới tên bạn đang gọi ra.
B. Không có gì xảy ra vì file không tồn tại.
C. Báo lỗi
D. Không có đáp án nào đúng
5. Cho cây thư mục như sau:
Hãy cho biết đường dẫn tuyệt đối đến tệp student1.gif là đường dẫn nào sau
đây? Giảsửđường dẫn chỉbắt đầu từUniversity.
A. University/student1.gif
B. University/ClassA/student1.gif.
C. /student1.gif
D. University/

The Dariu Foundation

6. Câu lệnh nào sau đây sẽđọc file từvịtrí hiện tại cho đến khi xuống dòng, vịtrí
mới nằm ởdòng tiếp theo?
A. read()
B. readline()
C. read(n)
D. Tất cảcác đáp án trên đều sai.
7. Câu lệnh nào sau đây sẽđọc n ký tựtiếp theo từvịtrí hiện tại, vịtrí mới tăng
thêm n ký tự?
A. read()
B. readline(n)
C. read(n)
D. Tất cảcác đáp án trên đều sai.
Đáp án
1. C
2. B
3. D
4. C
5. B
6. B
7. C
Hướng dẫn lập trình Python cơ bản

The Dariu Foundation

CHƯƠNG 9
Hàm và lời gọi hàm

1
Giới thiệu
Trong các bài học trước chúng ta đã từng sửdụng một sốhàm có trong Python như
print(), open(), write()... Vậy hàm là gì? Trong lập trình, hàm là một nhóm bao gồm
một hoặc nhiều câu lệnh và được dùng đểthực hiện một sốtác vụnhất định.
Hàm được chia thành hai nhóm:
• Hàm có sẵn (built-in function): là những hàm được cung cấp sẵn bởi ngôn
ngữPython. Ví dụnhư các hàm print(), range(), max()... Chúng ta không sửa
đổi logic bên trong các hàm này.
• Hàm tựđịnh nghĩa (user-defined function): là những hàm được định nghĩa
bởi các lập trình viên. Lập trình viên sẽtựkhai báo logic bên trong các hàm
tựđịnh nghĩa.
2
Định nghĩa hàm
Trong Python các hàm (tựđịnh nghĩa) được định nghĩa sửdụng cú pháp sau:
1 def <function_name >(<parameters >):
2
<statements >
Trong đó:
• < f unction_name >: là tên của hàm được định nghĩa.
• < parameter s >: (tham số) là danh sách các biến sốđặc biệt được sửdụng
bên trong hàm. Giá trịcủa từng tham sốđược xác định khi chúng ta sửdụng
hàm (hay gọi hàm). Một hàm được định nghĩa với một hoặc nhiều hoặc
không có tham sốnào.
• < statement >: bao gồm các câu lệnh sẽđược thực thi khi gọi hàm.
Ví dụmột hàm tựđịnh nghĩa helloPython() như sau:
1 def helloPython ():
2
print("Hello , Python!")
3
4 helloPython () # Hien thi: Hello , Python!
Ví dụhàm hello() dưới đây được định nghĩa với một tham sốđầu vào với tên là
language:
1 def hello(language):
2
print("Hello , %s!" %( language))
3
Gọi Hàm
Sau khi được định nghĩa thì đểsửdụng hàm chúng ta sẽthực hiện việc gọi hàm.
Gọi hàm được thực hiện đơn giản thông qua cú pháp sau:
1 <function_name >(<arguments >)

The Dariu Foundation
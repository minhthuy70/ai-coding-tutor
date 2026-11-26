# VI_PY_017: Cài đặt và đánh giá thuật toán sắp xếp nổi bọt trên danh sách sinh viên

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Giải thuật | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

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
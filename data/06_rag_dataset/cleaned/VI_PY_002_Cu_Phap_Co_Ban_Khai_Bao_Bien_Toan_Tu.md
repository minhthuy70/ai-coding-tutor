# VI_PY_002: Cú pháp cơ bản, khai báo biến, quy tắc đặt tên và các toán tử

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân
**Chuyên mục**: Cú pháp | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

Hình 1.23: Bấm chọn phần Project trong vùng khoanh màu đỏ
Hình 1.24: Hiển thịthanh công cụToolbar trên PyCharm
• Bước 9: Sau khi đã hiển thịthanh công cụ, chúng ta chọn vào dấu mũi tên
màu xanh. Sau đó chương trình sẽđược thực thi và kết quảsẽđược hiện thị
phía bên dưới như hình.
Hình 1.25: Nhấn nút Run đểchạy thửchương trình mặc định trên PyCharm
Như vậy là chúng ta đã cài đặt xong và chạy thửthành công một chương trình trên
PyCharm.
6
Chương trình đầu tiên trên PyCharm
Khi tạo mới một dựán (project) trên PyCharm, phần mềm tựtạo cho chúng ta file
mặc định là main.py cùng với một sốđoạn chương trình mẫu. Chúng ta có thể

The Dariu Foundation

nhấp đôi vào file này, xóa hết nội dung và bắt đầu bằng chương trình của mình.
Ởchương trình đầu tiên này, chúng ta cũng chỉđơn giản in ra màn hình một câu.
Chương trình của chúng ta chỉcó một lệnh là print("Hello World"). Và đây là kết
quảsau khi chạy chương trình:
Hình 1.26: Kết quảin ra màn hình cho chương trình đầu tiên trên PyCharm
7
Một sốthao tác khác trên PyCharm
Tông màu mặc định của PyCharm là màu tối (nền đen chữtrắng). Trong trường
hợp bạn muốn đổi tông màu hiển thị, có thểvào File, Settings. Với cửa sổmới hiện
ra, bạn chọn tiếp vào Appearance và lựa chọn tông màu ưa thích, như hướng dẫn
ởHình 1.27
Hình 1.27: Thay đổi tông màu hiển thịtrên PyCharm
Hướng dẫn lập trình Python cơ bản

Trong trường hợp muốn thay đổi kích thước của trình soạn thảo, đểviệc lập trình
được dễnhìn, từgiao diện Settings ởHình 1.27, chúng ta chọn tiếp qua Editor, và

chọn Font và thay đổi thông sốSize của nó, như minh họa ởHình 1.28 là 30.
Hình 1.28: Thay đổi kích thước chữkhi lập trình

The Dariu Foundation

8
Câu hỏi ôn tập
1. Phát biểu nào là đúng vềngôn ngữPython?
A. Ngôn ngữlập trình cấp thấp
B. Ngôn ngữlập trình cấp cao
C. Ngôn ngữmáy
D. Ngôn ngữMicroBit
2. Các lợi thếcủa ngôn ngữPython so với Pascal là gì?
A. Đơn giản dễtiếp cận
B. Tương thích với nhiều nền tảng
C. Mã nguồn mởvới nhiều thư viện hỗtrợ
D. Tất cảđều đúng
3. Đểchuyển từngôn ngữPython sang ngôn ngữmà máy tính hiểu được, chúng
ta cần:
A. Trình biên dịch Python3
B. Trình thông dịch Python3
C. Cả2 chương trình trên
D. Tất cảđều sai
4. Đặc điểm nào là đúng cho trình thông dịch?
A. Dịch từng lệnh và thực thi lệnh đó
B. Dịch toàn bộchương trình và thực thi
C. Tùy trường hợp mà 1 trong 2 phương pháp trên sẽđược chọn lựa
D. Tất cảđều đúng
5. Đặc điểm nào là đúng cho trình biên dịch?
A. Dịch từng lệnh và thực thi lệnh đó
B. Dịch toàn bộchương trình và thực thi
C. Tùy trường hợp mà 1 trong 2 phương pháp trên sẽđược chọn lựa
D. Tất cảđều đúng
6. Ngôn ngữlập trình Python là:
A. Ngôn ngữbiên dịch
B. Ngôn ngữthông dịch
C. Tất cảđều đúng
D. Tất cảđều sai
7. Ngôn ngữlập trình Pascal là:
A. Ngôn ngữbiên dịch
B. Ngôn ngữthông dịch
C. Tất cảđều đúng
D. Tất cảđều sai
Đáp án

1. B
2. D
3. B
4. A
5. B
6. B
7. A
Hướng dẫn lập trình Python cơ bản

The Dariu Foundation

CHƯƠNG 2
Hiển thịkết quảtrên Python

1
Giới thiệu
Đểtìm hiểu một ngôn ngữlập trình nói chung và python nói riêng, thông thường
chúng ta sẽbắt đầu bằng câu lệnh hiển thịđểin kết quảra màn hình. Thực ra,
trong một hệthống máy tính với 3 thành phần đặc trưng là Dữliệu đầu vào - Xử
lý - Kết quảđầu ra, thì bước cuối cùng lại là bước đơn giản nhất, tiếp theo là phần
dữliệu đầu vào và cuối cùng sẽlà xửlý. Cũng vì lý do đó, mà chúng ta thường tìm
hiểu câu lệnh hiển thịtrước, câu lệnh đơn giản nhất thuộc nhóm xuất kết quảđầu
ra (Output).
Ởbài trước, thực ra chúng ta đã xài câu lệnh hiển thịprint đểin chữ"Xin chao" ra
màn hình. Trong bài này, chúng tôi sẽtrình bày chi tiết hơn các tùy chọn của câu
lệnh print.
Các câu lệnh trong hướng dẫn bên dưới sẽđược nhập trực tiếp vào file mặc định
main.py. Sau đó, khi chạy chương trình, kết quảsẽđược in ra ởkhung cửa sổngay
bên dưới chương trình.
2
Hiển thịnhiều thông tin
Bên cạnh việc in ra 1 chuỗi như bài trước, hàm print có thểin nhiều thông tin, mỗi
thông tin cách nhau bằng dấu phẩy (,), như ví dụởchương trình sau đây:
1 print("Xin chao", 10, 12.1,"Ket thuc")
Chương trình 2.1: In nhiều thông tin
Bên cạnh chuỗi kí tự, hàm print cũng có thểin sốnguyên lẫn sốthập phân. Python
sẽtựđộng thêm dấu khoảng trắng vào giữa các thông tin cần in. Một biến sốcũng
được xem là một thông tin, và hoàn toàn có thểghép vào câu lệnh print theo cách
như trên. Một ví dụnhư sau:
1 x = 20

2 print("Xin chao", 10, 12.1,"Ket thuc", x)
Chương trình 2.2: In ra giá trịcủa biến số
Ởví dụtrên, x là một biến số. Tuy nhiên trên Python, việc khai báo một biến sốđã
được lược giản đi rất nhiều. Thậm chí, chúng ta không cần phải chỉđịnh kiểu dữ
liệu cho biến số. Chi tiết của việc khai báo biến và kiểu dữliệu sẽđược trình bài cụ
thểởnhững bài sau.
3
In với kí tựphân cách
Thay vì mỗi thông tin in ra được cách nhau bằng khoảng trắng như ởtrên, chúng
ta cũng có thểtùy chỉnh bằng chuỗi kí tựkhác, dựa vào tùy chọn sep như ví dụbên
dưới:
1 print("Xin chao", "Ket thuc", sep="---")
Chương trình 2.3: In kết quảvới kí tựphân cách

The Dariu Foundation

4
In với kí tựkết thúc
Cuối cùng, chúng ta cũng có thểthêm tùy chọn end đểđịnh nghĩa kí tựkết thúc
của chuỗi cần in, như ví dụsau:
1 print("Xin chao", "Ket thuc", sep="---", end="!!")
Chương trình 2.4: In kết quảvới tùy chọn end
Tất nhiên, vì là tùy chọn, sep và end có thểcó hoặc không, hoặc thậm chí xuất hiện
cùng nhau trong câu lệnh print. Yêu cầu duy nhất là các tùy chọn này phải cách
nhau bằng dấu phẩy và không có ràng buộc vềthứtự. Chương trình ?? cũng sẽin
ra kết quảtương tựnhư Chương trình ??
1 print("Xin chao", "Ket thuc", end="!!", sep="---")
Chương trình 2.5: Các tùy chọn không cần có thứtựtrước sau
5
In với sốthập phân
Một trong những thao tác quan trọng khi tính toán, kết quảcó thểlà sốthập phân
với rất nhiều kí sốsau dấy phẩy. Trong một sốtrường hợp, chúng ta chỉcần in 2 kí
sốsau dấu phẩy mà thôi. Câu lệnh print hỗtrợtrong trường hợp này sẽnhư ví dụ
bên dưới:
1 a = 3.14165
2 print("Ket qua la %.2f" %a)
Chương trình 2.6: Tùy chỉnh sốkí sốsau dấu thập phân
Ởđây, %.2f là định dạng của dữliệu cần in. Kết quảin ra màn hình sẽchỉlấy 2
chữsốthập phân của biến a mà thôi. Một lưu ý quan trọng là kết quảsẽđược làm
tròn.
Hướng dẫn lập trình Python cơ bản

6
Câu hỏi ôn tập
1. Câu lệnh đểin kết quảra màn hình trên Python là gì?
A. print
B. Log
C. Out
D. Tất cảđều đúng
2. Kết quảin ra màn hình của lệnh print("Xin chao", "123") là gì?
A. Xin chao
B. 123
C. Xin chao 123
D. Lệnh sai cú pháp
3. Kết quảin ra màn hình của lệnh print("Xin chao", "123", sep="*") là gì?
A. Xin chao 123 *
B. Xin chao * 123
C. Xin chao * 123 *
D. Lệnh sai cú pháp
4. Kết quảin ra màn hình của lệnh print("Xin chao", "123", end="*") là gì?
A. Xin chao 123 *
B. Xin chao * 123
C. Xin chao * 123 *
D. Lệnh sai cú pháp
5. Kết quảin ra màn hình của lệnh print("Xin chao", "123", sep = "*", end="*")
là gì?
A. Xin chao 123 *
B. Xin chao * 123
C. Xin chao * 123 *
D. Lệnh sai cú pháp
6. Kết quảin ra màn hình của lệnh print("Xin chao", "123", end = "*", sep="*")
là gì?
A. Xin chao 123 *
B. Xin chao * 123
C. Xin chao * 123 *
D. Lệnh sai cú pháp
7. Kết quảin ra màn hình của lệnh print("Vi du %.2f", % 3.14999) là gì?
A. Vi du 3.14
B. Vi du 3.15
C. Vi du 3.14999
D. Lệnh sai cú pháp
Đáp án
1. A
2. C
3. B
4. A
5. C

6. C
7. B

The Dariu Foundation
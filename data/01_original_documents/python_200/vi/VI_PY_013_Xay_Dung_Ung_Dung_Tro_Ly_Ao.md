<!-- page: 1 -->
# VI_PY_013: Xây dựng ứng dụng thực tế: Dự án trợ lý ảo điều khiển bằng Python

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Dự án | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 122 -->
1
Giới thiệu
Bài hướng dẫn này là bước thứ3, bước cuối cùng khi hiện thực 1 dựán: Xửlý dữ
liệu đầu vào, và xuất kết quảra đầu ra. Đây phải là bước hiện thực sau cùng, vì chỉ
khi việc xửlý đầu vào và đầu ra ổn định, chúng ta mới có cơ sởđểhiện thực giải
thuật ngày một hoàn thiện hơn và ổn định hơn.
Trong bài hướng dẫn này, chúng tôi chỉđưa ra những ý tưởng căn bản nhất để
người đọc có thểhiện thực một chương trình trợlý ảo đơn giản, đếnó ngày trởnên
thông minh hơn, người học có thểtựphát triển.
Trong hướng dẫn này, trợlý ảo của chúng tôi sẽtrảlời lại 2 câu hỏi từngười dùng
là "hello" (xin chào) và "what is today" (hôm nay là thứmấy)
2
Truy xuất ngày hiện tại
Có nhiều phương pháp đểlấy thông tin ngày hiện tại của hệthống, phần chương
trình hướng dẫn bên dưới là một ví dụ.
1 from datetime import date
2
3 today = date.today ()
4 strTextToday = today.strftime("%B %d, %Y")
5 print(strTextToday)
Chương trình 13.1: Lấy ngày hiện tại của hệthống
Trong chương trình trên, chúng ta cần phải thêm thưu viện date, sau đó định dạng
cho chuỗi dữliệu mô tảngày hiện tại. Tất nhiên, kết quảsẽlà tiếng Anh, bởi chúng
ta đang hiện thực trợlý ảo có thểnhận dạng và nói bằng tiếng Anh.
3
Hoàn thiện chương trình
Đơn giản nhất trong việc hiện thực chức năng trảlời tựđộng cho trợlý ảo là sử
dụng những câu lệnh if. Với mỗi lệnh từngười dùng nhận vào, chúng ta sẽcó
những câu trảlời tương ứng. Chương trình gợi ý cho phần này như sau:
1 import
speech_recognition
2 import pyttsx3
3 from datetime import date
4

<!-- page: 2 -->

5 today = date.today ()
6 strTextToday = today.strftime("%B %d, %Y")
7
8 voice = speech_recognition.Recognizer ()
9 with
speech_recognition.Microphone () as mic:
10
print("I am listenning ...")
11
audio = voice.listen(mic)
Trang 122
The Dariu Foundation

<!-- page: 123 -->
12
13 try:
14
input_text = voice.recognize_google(audio)
15 except:
16
input_text = "I do not understand"
17 print(input_text)
18
19 output_text = ""
20 if input_text == "hello":
21
output = "Hello , I am AI Python"
22 elif input_text == "what is today":
23
output_text = "Today is " + strTextToday
24 else:
25
output_text = "Sorry I do not understand"
26
27 engine = pyttsx3.init ()
28 engine.say(output_text)
29 engine.runAndWait ()
Chương trình 13.2: Hoàn thiện phần xửlý cho trợlý ảo
Thực ra, chương trình hiện tại vẫn còn phải phát triển thêm đểnó có thểgần giống
như một trợlý ảo. Các hướng ởmởrộng dành cho người học được liệt kê như sau:
• Cải thiện việc so trùng: Hiện tại, trong câu lệnh if, việc so sánh trùng sẽrất
khó xảy ra trong thực tế. Ví dụngười dùng nói "hello hello", thì trợlý của
chúng ta sẽkhông chào lại. Chúng ta sẽso sánh theo kiểu từkhóa: Trong câu
nói của người dùng có chữhello, thì chúng ta có thểchào lại. Câu lệnh gợi ý
cho chức năng này là if "hello" in input_text.

<!-- page: 3 -->

• Hiện tại, chương trình cũng chỉchạy một lần rồi dừng. Đây là cơ hội đểngười
học vận dụng câu lệnh while: Chương trình sẽliên tục hoạt động cho đến khi
người dùng nói bye bye.
• Chương trình hiện tại chỉhỗtrợ2 câu lệnh, người dùng có thểtựđịnh nghĩa
thêm nhiều câu lệnh khác, đểtrợlý ảo trởnên thông minh hơn!!!
Các hướng mởrộng trình bày ởtrên, chúng tôi không hướng dẫn bằng chương
trình cụthể, mà xem nó như là ý tưởng đểngười học tựsáng tạo. Chúc các bạn
thành công với trợlý ảo của mình.
Hướng dẫn lập trình Python cơ bản
Trang 123

<!-- page: 124 -->
4
Câu hỏi ôn tập
1. Quá trình hiện thực trí thông minh cho trợlý ảo, thuộc phần nào sau đây?
A. Xửlý đầu vào
B. Xửlý đầu ra
C. Xửlý giải thuật
D. Tất cảđều đúng
2. Đểtrợlý ảo có thểhoạt động liên tục cho đến khi người dùng nói "bye bye",
câu lệnh nào là tốt nhất đểhiện thực?
A. if
B. while
C. for
D. Tất cảđều sai
3. Đểhiện thực trí thông minh cho trợlý ảo, câu lệnh nào có thểđược sửdụng
một cách hiệu quảnhất?
A. if
B. while
C. for
D. Tất cảđều sai
4. Đểcó thểtruy xuất ngày hiện tại của hệthống, thư viện nào cần được thêm
vào chương trình?
A. pyttsx3
B. date
C. speech_recognition.Recognizer()
D. Tất cảcâu lệnh trên
5. Hạn chếcủa câu lệnh so sánh bằng giữa 2 chuỗi khi hiện thực trí thông minh
cho trợlý ảo là gì?
A. Xác suất nhận lệnh đúng từngười dùng sẽthấp
B. Khi người dùng nói "hello hello", hệthống sẽkhông hiểu nếu chỉso sánh
bằng với "hello"
C. Hạn chếrất nhiều khi triển khai thực tế
D. Tất cảđều đúng
Đáp án

<!-- page: 4 -->

1. C
2. B
3. A
4. B
5. D
Trang 124
The Dariu Foundation
<!-- page: 1 -->
# VI_PY_020: Kỹ thuật tổ chức mã nguồn chuẩn kiến trúc đa tầng và triển khai dự án

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Kiến trúc | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 116 -->
1
Giới thiệu
Trong phần tiếp theo của dựán trợlý ảo, chúng ta sẽthực hiện chức năng nhận
diện giọng nói từngười dùng. Chức năng này được xem như là phần dữliệu đầu
vào của dựán, còn được gọi là Speech To Text. Cũng giống như chức năng phát ra
giọng nói ởbài trước, đây hoàn toàn là một tác vụrất phức tạp. Tuy nhiên với sự
hỗtrợtừcác thư viện có sẵn, công việc lập trình của chúng ta trởnên đơn giản hơn.
Tuy nhiên, đối với chức năng nhập dữliệu, bao giờchúng ta cũng phải đi kèm với
việc xửlý lỗi, đểcho ứng dụng có thểhoạt động chính xác hơn. Ví dụchúng ta
mong đợi người dùng nói một câu, nhưng người dùng lại không nói câu nào cả,
hoặc chẳng hạn vì các lý do khác, như mất mạng, và hệthống không nhận được
kết quả. Tất cảnhững chức năng này, làm cho việc xửlý dữliệu đầu vào bao giờ
cũng phức tạp hơn so với dữliệu đầu ra.
2
Cài đặt thư viện
Đểthực hiện chức năng nhận diện giọng nói, chúng ta cần cài đặt thêm một thư
viện là speechrecognition đểthực hiện chức năng nhận dạng giọng nói. Trình tự
đểlàm gồm 2 bước như sau:
Bước 1: Đểbắt đầu việc cài đặt, chúng ta cần phải chuyển qua giao diện Terminal,
như minh họa ởHình 12.1.
Hình 12.1: Giao diện Terminal đểcài đặt thư viện.
Bước 2: Gõ dòng lệnh pip install wheel rồi nhấn Enter. Bạn cũng cần phải kết
nối mạng đểchương trình có thểtải thư viện vềtrước khi cài đặt. Trong trường
hợp mạng quá kém, quá thời gian cho phép, hệthống cũng sẽtựđộng dừng việc
cài đặt và bạn cần phải làm lại, cho đến khi nào thấy được dòng chữSuccessfully
installed speechrecognition, như minh họa ởHình 12.2.
Hình 12.2: Cài đặt thành công thư viện SpeechRecognition
Lưu ý: Nếu bạn muốn hiện thực một chương trình chỉcó chức năng nhận diện
giọng nói, bạn cần phải cài đặt wheel, pipwin, pyaudio và speechrecognition.
Trang 116
The Dariu Foundation

<!-- page: 117 -->
3

<!-- page: 2 -->

Hiện thực chương trình
Đểhiện thực chức năng nhận diện giọng nói, chúng ta cần những dòng lệnh căn
bản sau đây:
1 import
speech_recognition
2
3 voice = speech_recognition.Recognizer ()
4 with
speech_recognition.Microphone () as mic:
5
print("I am listenning ...")
6
audio = voice.listen(mic)
7 input_text = voice.recognize_google(audio)
8 print(input_text)
Chương trình 12.1: Chương trình chuyển từchữsang giọng nói
Ởdòng đầu tiên, chúng ta đang thêm thư viện vào chương trình. Bạn hãy lưu ý tên
thư viện lúc import, có thêm dấu gạch dưới(import speech_recognition), khác với
tên dính liền lúc cài đặt thư viện (pip install speechrecognition). Dòng tiếp theo
là đểkhởi tạo một đối tượng (đặt tên là voice) làm nhiệm vụchính là nhận diện
giọng nói. Câu lệnh with dùng đểkhởi tạo microphone của máy tính chúng ta, và
bắt đầu ghi âm lại, lưu vào biến audio. Khi việc ghi âm kết thúc (chúng ta ngừng
nói), dữliệu âm thanh sẽđược nhận dạng bằng phương thức recognize_goole. Với
kết quảlưu trong biến input_text, chúng ta có thểin ra màn hình đểtheo dõi.
Trong trường hợp người dùng không nói gì, hoặc mạng bịlỗi, câu lệnh text =
voice.recognize_google(audio) có thểxảy ra lỗi. Chúng ta sẽkhắc phục sựcốnày
bằng câu lệnh try except. Khéo léo kết hợp với chương trình đã hiện thực ởbài
trước, chúng ta có chương trình như sau:
1 import
speech_recognition
2 import pyttsx3
3
4 voice = speech_recognition.Recognizer ()
5 with
speech_recognition.Microphone () as mic:
6
print("I am listenning ...")
7
audio = voice.listen(mic)
8
9 try:
10
input_text = voice.recognize_google(audio)
11 except:
12

<!-- page: 3 -->

input_text = "I do not understand"
13 print(input_text)
14
15 engine = pyttsx3.init ()
16 engine.say("I hear " + input_text)
17 engine.runAndWait ()
Chương trình 12.2: Nhận diện giọng nói và phát âm lại
Trong chương trình ởtrên, chúng ta sẽcho máy tính nói lại những gì mà chúng ta
vừa nói. Đây là một cách rất hiệu quảđểkiểm tra quá trình xửlý đầu vào (input) và
Hướng dẫn lập trình Python cơ bản
Trang 117

<!-- page: 118 -->
đầu ra (output), trước khi chúng ta bắt tay vào hiện thực cho phần xửlý, tạm gọi là
"trí thông minh" của trợlý ảo. Lưu ý là, hệthống nhận dạng giọng nói vẫn chỉhỗ
trợcho tiếng Anh mà thôi. Đểcó thểlàm trợlý ảo hoàn toàn bằng tiếng Việt, bạn
phải xài những thư viện cao cấp hơn. Trong giới hạn của hướng dẫn này, chúng tôi
chỉsửdụng những thư viện đơn giản nhất.
Trang 118
The Dariu Foundation

<!-- page: 119 -->
4
Câu hỏi ôn tập
1. Quá trình nhạn dạng giọng nói, đóng vai trò gì trong hệthống trợlý ảo?
A. Xửlý đầu vào
B. Xửlý đầu ra
C. Xửlý trí thông minh
D. Tất cảđều đúng
2. Đểxửlý lỗi trong việc nhận dạng giọng nói, câu lệnh nào được sửdụng?
A. Regconizer()
B. try except
C. if else
D. Tất cảđều đúng
3. Thư viện chính đểnhận dạng giọng nói tiếng Anh là gì?
A. pyaudio
B. pyttsx3
C. speech recognition
D. Tất cảđều sai
4. Câu lệnh nào dùng đểkhởi động chương trình nhận diện giọng nói?
A. pyttsx3.init()
B. engine.say()
C. speech_recognition.Recognizer()
D. Tất cảcâu lệnh trên
5. Ngôn ngữhỗtrợcho thư viện speechrecognition là gì?

<!-- page: 4 -->

A. Tiếng Việt
B. Tiếng Anh
C. Tiếng Việt và Tiếng Anh
D. Tất cảcác thứtiếng
6. Câu lệnh đểthêm thư viện nhận dạng giọng nói vào chương trình Python là gì?
A. import pyttsx3
B. import speechrecognition
C. import speech_recognition
D. Tất cảđều đúng
7. Các lỗi có thểxảy ra khi nhận diện giọng nói là gì?
A. Người sửdụng không nói gì
B. Mất kết nối mạng
C. Nói bằng ngôn ngữhệthống không nhận dạng đượcn
D. Tất cảcác lỗi trên đều có thểxảy ra
Đáp án
1. A
2. B
3. C
4. C
5. B
6. C
7. D
Hướng dẫn lập trình Python cơ bản
Trang 119

<!-- page: 120 -->
Trang 120
The Dariu Foundation
<!-- page: 1 -->
# VI_PY_062: Khái niệm biến và các kiểu dữ liệu căn bản: Số, Chuỗi, Boolean

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn  
**Chuyên mục**: Kiểu dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 12 -->
if condition1 :
    indentedStatementBlockForTrueCondition1
elif condition2 :
    indentedStatementBlockForFirstTrueCondition2
elif condition3 :
    indentedStatementBlockForFirstTrueCondition3
elif condition4 :
    indentedStatementBlockForFirstTrueCondition4
else:
    indentedStatementBlockForEachConditionFalse
2.4.2. Switch…case
Python không có cấu trúc switch … case
2.4.3. For…in
for iterating_var in sequence:
    statements(s)
Ví dụ:

<!-- page: 13 -->
for letter in 'Python':     # First Example
    print 'Current Letter :', letter
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
    print 'Current fruit :', fruit
print "Good bye!"
Kết quả hiển thị của ví dụ trên:
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n
Current fruit : banana
Current fruit : apple
Current fruit : mango

<!-- page: 2 -->

Good bye!
2.4.4. While

<!-- page: 14 -->
while expression:
    statement(s)
Ví dụ:
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
    
print "Good bye!"
Kết quả hiển thị của ví dụ trên:

<!-- page: 15 -->
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
Good bye!
2.5. Hàm
Khai báo hàm theo cú pháp:
def functionname(param, param2,..):
    statements(s)
Hàm nếu không trả dữ liệu thì mặc định sẽ trả về giá trị
None
Ví dụ khai báo hàm tính và trả về giá trị tổng của 2 tham
số đầu vào:

<!-- page: 16 -->
def sum(a, b):
```python
return (a+b)    
```
Cách gọi hàm:
sum(1, 2)
(trả về giá trị là 3)   
Hàm có hỗ trợ giá trị mặc định cho tham số khi không
truyền vào. Ví dụ hàm sau:

<!-- page: 3 -->

def plus(c, d = 10):
```python
return (c+d)
```
Nếu gọi hàm trên như sau:
plus(2)
(kết quả trả về là 12)
Một khác biệt trong cách gọi hàm của Python so với PHP
là chúng ta có thể thay đổi thứ tự tham số truyền vào bằng

<!-- page: 17 -->
cách đặt tên tham số khi gọi hàm. Ví dụ ta có thể gọi hàm
sum(a,b) ở ví dụ trên bằng cách truyền tham số b trước a
như sau:
sum(b = 1, a = 10)
2.6. Xử lý chuỗi
Một chuỗi có thể khai báo bằng dấu nháy đôi " hoặc đơn
' . Ví dụ các chuỗi sau:
str1 = "Hello"
str2 = 'world'
Có thể truy xuất từng ký tự trong một chuỗi theo hình thức
index, ví dụ: str1[0] , str1[1] …
Có thể sử dụng 3 dấu nháy (đôi hoặc đơn) để khai báo
chuỗi trên nhiều dòng. Ví dụ:

<!-- page: 18 -->
paragraph = """This is line 1
This is line 2
This is line 3"""
2.6.1. Nối chuỗi
Có thể tạo một chuỗi dài từ việc nối các chuỗi lại theo cú
pháp:
str = str1 + " " + str2
2.6.2. Trích xuất chuỗi con
Có thể tạo các chuỗi con thông qua toán tử lấy khoản
[start:end] (range). Mặc định start là từ vị trí đầu chuỗi
( 0 ) và end là đến vị trí cuối chuỗi. Ví dụ:

<!-- page: 19 -->
str = 'Hello world'
    
print str[0:4]
(Hiển thị "Hell")   
    
print str[:4]

<!-- page: 4 -->

(Hiển thị "Hell")   
    
print str[-3:]
(Hiển thị "rld")
    
print str[6:-3]
(Hiển thị "wo")
2.6.3. Lấy độ dài của chuỗi
Sử dụng hàm len(...) để trả về độ dài của chuỗi. Ví dụ:
count = len("Hello world")  
(count có giá trị 11)
2.6.4. Tìm & thay thế nội dung
Có thể tìm và thay thế trong chuỗi bằng cách gọi phương

<!-- page: 20 -->
thức replace(search, replace[, max]) của một chuỗi. Ví
dụ:
str = 'Hello world'
newstr = str.replace('Hello', 'Bye')
print newstr
(Sẽ hiển thị chuỗi "Bye world" trên màn hình)
2.6.5. Tìm vị trí chuỗi con
Có thể tìm vị trí của một chuỗi con trong chuỗi lớn bằng
cách gọi phương thức find(str, beg=0
end=len(string)) . Bắt đầu là vị trí 0 , nếu không tìm ra thì
trả về -1 . Ví dụ:
str = 'Hello world'
print str.find('world')
(hiển thị 6)
    
print str.find('Bye');
(hiển thị -1)
Hàm find() sẽ tìm theo thứ tự từ trái qua phải của chuỗi,
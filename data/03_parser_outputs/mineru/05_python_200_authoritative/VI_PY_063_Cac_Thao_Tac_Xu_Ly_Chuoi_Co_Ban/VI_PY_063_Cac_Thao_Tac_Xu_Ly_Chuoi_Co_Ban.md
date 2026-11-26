<!-- page: 1 -->
# VI_PY_063: Các thao tác xử lý chuỗi: Ghép chuỗi, định dạng và cắt chuỗi

**Nguồn tài liệu chính thống**: Python Rất Là Cơ Bản - Võ Duy Tuấn  
**Chuyên mục**: Chuỗi | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 22 -->
strip([chars]) : loại bỏ trước và sau chuỗi
lstrip([chars]) : loại bỏ phía trước chuỗi
rstrip([chars]) : loại bỏ phía sau chuỗi
2.6.8. Một số hàm xử lý chuỗi
isnumeric() : Kiểm tra một chuỗi có phải là chuỗi số
lower() : Chuyển chuỗi hết thành chữ thường
upper() : Chuyển chuỗi hết thành chữ HOA
2.7. List
List trong Python là cấu trúc mảng và các phần tử có index
có thứ tự. Không như PHP, key của một mảng có thể vừa
là số, vừa là chuỗi (associated array).
Trong Python, muốn tạo một mảng có key là chuỗi thì sẽ
sử dụng cấu trúc Dictionary (phần tiếp tiếp). Trong phần
này, chúng ta sẽ nói đến List. Một List được khai báo như
mảng trong JSON. Sử dụng [..] để khai báo một mảng.
Ví dụ:

<!-- page: 23 -->
numbers = [1, 2, 3, 4, 5]
names = ['Marry', 'Peter']
Có thể truy xuất từng phần tử của mảng bằng index, phần
tử đầu tiên có thứ tự là 0 . Ví dụ:
print numbers[0]
(Hiển thị 1)
    
print numbers[-3]
(Hiển thị 3)
    
print names[1]
(Hiển thị 'Peter')
Để biết được số lượng phần tử của 1 List, có thể sử dụng
hàm len(array) để lấy số lượng phần tử của mảng tham
số truyền vào.
2.7.1. Kiểm tra sự tồn tại của một phần tử

<!-- page: 2 -->

2.7.1.1. Kiểm tra theo Index

<!-- page: 24 -->
Trong nhiều trường hợp bạn muốn truy xuất một phần tử
bất kỳ (dựa vào index) của mảng thì nếu truy xuất đến một
phần tử không tồn tại thì ứng dụng sẽ báo lỗi. Do đó, trước
khi truy xuất một phần tử, bạn cần kiểm tra xem phần tử
này đã tồn tại hay chưa. Hiện tại python không hỗ trợ hàm
nào để kiểm tra sự tồn tại của một phần tử trong mảng.
Có 2 cách thường thấy để kiểm tra đó là “Look before you
leap” (LBYL) và “Easier to ask forgiveness than
permission” (EAFP).
Ví dụ về “Look before you leap (LBYL)”:
if index < len(array):
    array[index]
else:
    # handle this
Ví dụ về “Easier to ask forgiveness than permission”
(EAFP):

<!-- page: 25 -->
try:
    array[index]
except IndexError:
    # handle this
2.7.1.2. Kiểm tra theo giá trị
Để kiểm tra một giá trị có tồn tại / không tồn tại trong
mảng hay không thì có thể sử dụng toán tử in / not in . Ví
dụ:
mylist = ['a', 'b', 'c']
    
print 'a' in mylist
(Hiển thị True)
    
print 'b' not in mylist
(Hiển thị False)
2.7.2. Trích xuất mảng con
Tương tự như chuỗi, tó thể tạo các mảng con thông qua
toán tử lấy khoản [start:end] (range). Mặc định start là

<!-- page: 26 -->
từ vị trí đầu chuỗi ( 0 ) và end là đến vị trí cuối chuỗi. Ví dụ:
numbers = ['a', 'b', 'c', 'd']
    
print numbers[:2]

<!-- page: 3 -->

(Hiển thị ['a', 'b'])
    
print numbers[-2:]
(Hiển thị ['c', 'd'])
2.7.3. Xóa phần tử của mảng
Có thể xóa một phần tử thông qua toán tử del . Thứ tự của
các phần tử sẽ dịch chuyển tùy vào vị trí của phần tử bị
xóa. Ví dụ:
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print numbers
(Hiển thị [2, 3, 4, 5])
Bạn có thể xóa một khoản dựa vào toán tử lấy khoản
[start:end] . Ví dụ:

<!-- page: 27 -->
numbers = [1, 2, 3, 4, 5, 6, 7]
del numbers[2:4]
print numbers
(Hiển thị [1, 2, 5, 6, 7])  
2.7.4. Nối 2 mảng
Bạn có thể sử dụng toán tử + để nối giá trị của 2 mảng và
tạo ra một mảng lớn có số lượng phần tử là tổng số lượng
phần tử của 2 mảng con. Ví dụ:
a = [1, 2]
b = [1, 3]
    
print a + b
(Hiển thị [1, 2, 1, 3])
2.7.5. Thêm phần tử vào mảng
Nếu bạn muốn thêm phần tử vào một mảng đã tồn tại, hãy
dùng phương thức list.append(newvalue) để thêm phần
tử có giá trị newvalue vào cuối mảng list . Ví dụ:

<!-- page: 28 -->
numbers = [1, 2, 3]
numbers.append(4)
print numbers
(Hiển thị [1, 2, 3, 4]
2.7.6. Lấy phần tử cuối mảng
Nếu muốn lấy phần tử cuối cùng của mảng ra khỏi mảng,
có thể sử dụng phương thức list.pop() , sẽ trả về giá trị
của phần tử cuối cùng và mảng bây giờ sẽ không còn phần
tử này.
numbers = [1, 2, 3]

<!-- page: 4 -->

mynumber = numbers.pop()
print mynumber
(Hiển thị 3)
    
print numbers
(Hiển thị [1, 2])
2.7.7. Tìm một giá trị trong mảng
Nếu bạn muốn tìm vị trí (index) của một giá trị trong một

<!-- page: 29 -->
mảng, có thể dùng phương thức list.index(obj) . Nếu
tìm thấy sẽ trả về index của phần tử đầu tiên tìm thấy. Nếu
không tìm thấy sẽ quăng Exception. Ví dụ:
aList = [123, 'xyz', 'zara', 'abc'];
print "Index for xyz : ", aList.index('xyz') 
print "Index for zara : ", aList.index('zara')
Khi chạy sẽ hiển thị kết quả:
Index for xyz :  1
Index for zara :  2 
2.7.8. Đảo ngược giá trị của mảng
Để đảo ngược thứ tự các giá trị của một mảng, sử dụng
phương thức list.reverse() . Phương thức này không trả
về kết quả mà thay đổi trực tiếp mảng list . Ví dụ:

<!-- page: 30 -->
numbers = [1, 2, 3, 4]
numbers.reverse()
print numbers
(Hiển thị [4, 3, 2, 1])
2.7.9. Sắp xếp giá trị các phần tử
Để sắp xếp thứ tự của giá trị trong mảng, sử dụng phương
thức list.sort([func]) để sắp xếp. Nếu tham số đầu
vào là hàm func không truyền vào thì mặc định là sắp xếp
theo giá trị tăng dần. Phương thức này không trả về kết
quả mà thay đổi trực tiếp mảng list . Ví dụ:
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.sort()
print "List : ", aList
(Hiển thị List :  [123, 'abc', 'xyz', 'xyz', 'zara'
])
Cách triển khai hàm compare func() cũng giống như hàm
usort trong PHP. Hàm trả về các giá trị 0 , -1 và 1 .
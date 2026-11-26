# VI_PY_100: Phương pháp sư phạm Socratic: Kỹ thuật đặt câu hỏi dẫn dắt tư duy phản biện

**Nguồn tài liệu chính thống**: Tài liệu Sư phạm Giảng dạy Lập trình ĐH
**Chuyên mục**: Sư phạm | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

4.3.4
Hiệu đối xứng của hai tập hợp (Symmetric difference)
Hiệu đối xứng của hai tập A và B được kết quảlà tập hợp các phần tửthuộc cảA và
B nhưng không đồng thời thuộc cảtập A và B.
1 a = {1, 2, 3}
2 b = {3, 4}
3 c = a.symmetric_difference(b)
4 print(c) # ket qua la {1, 2, 4}
Chương trình 10.14: Phép hiệu đối xứng của hai tập hợp
4.4
Khi nào sửdụng tập hợp
Tập hợp cũng là một cấu trúc dữliệu giống như với list và tuple nhưng nó lại được
xây dựng sẵn các phép toán tập hợp, do vậy nếu chương trình của chúng ta cần
thực hiện các phép toán như: union(), intersection(), ... thì chúng ta có thểcân
nhắc dùng đến tập hợp. Ngoài ra cũng cần phải lưu ý các đặc tính của tập hợp để
áp dụng vào các bài toán sao cho hợp lý.
5
Cấu trúc dữliệu từđiển (Dictionary)
Dictionary (hay còn gọi là từđiển) bao gồm rất nhiều các phần tửmà mỗi phần tử
đi theo cặp khóa - giá trị(key-value). Từđiển thường được sửdụng khi chúng ta có
một sốlượng lớn dữliệu và muốn tối ưu hóa chúng đểtrích xuất dữliệu với điều
kiện phải biết được khóa đểlấy giá trị.
5.1
Khởi tạo và truy xuất các phần tửtrong từđiển
Trong python, từđiển được định nghĩa trong dấu ngoặc nhọn tương tựnhư tập
hợp.Nhưng bên trong là các phần tửtheo cặp (khóa và giá trị) được phân tách bởi
dấu phẩy, phân tách giữa khóa và giá trịcủa từng phần tửbởi dấu hai chấm. Cụ
thể:
1 a = dict ({"A": 24, "B": 30, "C": 27})
2 b = dict ([("D", 24), ("E", 30), ("F", 27)])
3 # duyet lan luot cac khoa trong tu dien a
4 for key in a:
5
print(key)

Chương trình 10.15: Cách đểkhởi tạo từđiển
Lưu ý:
• Khóa của từđiển có thểlà chuỗi hoặc số, khóa này là duy nhất ởtừng cấp.
• Giá trịcủa từđiển có thểsố, chuỗi hoặc các cấu trúc list, tuple, tập hợp hoặc
thậm chí là một từđiển khác.
Chúng ta có thểtruy xuất đến các phần tửtrong từđiển thông qua các khóa, cụthể
như sau:
Hướng dẫn lập trình Python cơ bản

1 a = dict ({"A": 24, "B": 30, "C": {"D" : 21}})
2 print(a[A]) # ket qua la 24
3 #truy xuat phan tu cua cac tu dien long nhau
4 print(a["C"]["D"]) #ket qua la 21
Chương trình 10.16: Truy xuất các phần tửtrong từđiển
5.2
Thêm và cập nhật phần tửtrong từđiển
Từđiển có thểthay đổi, nên chúng ta có thểthêm mới hoặc thay đổi giá trịcủa
các phần tửhiện có bằng cách sửdụng toán tửgán. Và bởi vì từđiển truy xuất các
phần tửthông qua khó, nên khi gán gán giá trì cho một phần tửthì:
• Khóa tồn tại thì giá trịphần tửđược cập nhật.
• Khóa không tồn tại thì từđiển được thêm một phần tửcó khóa và giá trịtrong
câu lệnh.
1 dict = {"a": 1, "b": 2}
2 # them mot phan tu vao tu dien dict
3 dict["c"] = 2 # ket qua: {’a ’: 1, ’b ’: 2, ’c ’: 2}
4 # cap nhat gia tri cua mot phan tu
5 dict["c"] = 3 # ket qua: {’a ’: 1, ’b ’: 2, ’c ’: 3}
Chương trình 10.17: Thêm và cập nhật phần tửtrong từđiển
5.3
Xóa phần tửkhỏi từđiển
Giống như list, có nhiều phương thức có sẵn dùng đểxóa một phần tửkhỏi từđiển
như pop(), popitem() clear() del. Chức năng của các phương thức trên như sau:
• pop(): Xóa phần tửcó key đã cho và trảvềgiá trịcủa phần tửđó.
• popitem(): Xóa và trảvềmột phần tửngẫu nhiên dưới dạng (key, value)
• clear(): Xóa tất cảcác phần tửtrong từđiển
• del: Xóa một phần tửhoặc xóa hẳn biến chứa từđiển.
1 dict = {"a": 1, "b": 2, "c": 3}
2 a = dict.pop("a") # a = 1, dict = {"b": 2, "c": 3}
3 del dict["c"] #dict = {"b": 2}
4 dict.clear () # dict = {}
5 del dict
6 print(dict) #dict khong ton tai
Chương trình 10.18: Các phương pháp xóa phần tửkhỏi từđiển

The Dariu Foundation

5.4
Một sốphương thức hay dùng trong từđiển
• Phương thức get(): Trảvềgiá trịmột phần tửtrong từđiển với một khóa cho
trướ.,
• Phương thức key() và value: Trảvềdanh sách khóa và danh sách các giá trị
của từđiển
1 dict = {"a": 1, "b": 2, "c": 3}
2 a = dict.get("a") # a = 1
3 b = dict.keys () # b = [’a’, ’b’, ’c ’]
4 c = dict.values () # c = [1, 2, 3]
Chương trình 10.19: Phép hiệu đối xứng của hai tập hợp
5.5
Khi nào sửdụng từđiển
Chúng ta có thểcân nhắc sửdụng từđiển khi dữliệu thay đổi liên tục, có sựliên
kết giữa khóa và giá trịhay quan trọng là muốn tăng hiệu quảkhi truy xuất dữliệu
thông qua khóa.
6
Bài tập
1. Nhập 2 chuỗi bất kỳtừbàn phím, nối 2 chuỗi đó lại với nhau. In chuỗi kết quả
và cho biết chuỗi đó có bao nhiêu ký tự.
1 a = input("nhap chuoi thu nhat: ")
2 b = input("nhap chuoi thu hai: ")
3 ketqua = a + b
4 print(ketqua)
5 print("So ky tu cua chuoi tren la: ", len(ketqua))
Chương trình 10.20: Đáp án gợi ý bài 1
2. Viết một chương trình đểtạo một tuple khác, chứa các giá trịlà sốchẵn trong 1
tuple cho trước.
Gợi ý: Sửdụng tuple() đểtạo tuple từlist.
1 a = (1,2,3,4,5,6,7,8)
2 tp = list ()
3 for i in range(0,len(a)):
4
if a[i]%2==0:
5
tp.append(a[i])
6 tp1 = tuple(tp)
7 print(tp1)
Chương trình 10.21: Đáp án gợi ý bài 2
3. Viết một chương trình xóa các phần tửtrùng nhau giữa 2 tập hợp cho trước:
1 a = {1,2,3,4,5,6,7,8}

2 b = {2,4,6,8}
3 tp = a.difference(b)
Hướng dẫn lập trình Python cơ bản

4 print(tp)
Chương trình 10.22: Đáp án gợi ý bài 3
4. Nhập sốnguyên N từbàn phím, hãy viết chương trình đểtạo ra một từđiển chứa
(i, i*i) như là sốnguyên từ1 đến N (bao gồm cả1 và n) sau đó in ra từđiển này.
Ví dụ: Giảsửsốn là 8 thì đầu ra sẽlà: 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64.
1 n=int(input("Nhap vao so nguyen N:"))
2
3 d=dict ()
4 for i in range(1,n+1):
5
d[i]=i*i
6 print (d)
Chương trình 10.23: Đáp án gợi ý bài 4
7
Câu hỏi ôn tập
1. Cho đoạn code sau:
1 a = "Xin chao Viet Nam"
2 print(a.find("i")
Kết quảcủa đoạn lệnh trên là gì?
A. 1
B. 2
C. 3
D. i
2. Cách nào sau đây dùng đểkhai báo một tuple:
A. a = [1,2,3,4]
B. a = (1,)
C. a = (1,2,3,4)
D. a = (1)
3. Cho đoạn code sau:
1 a = (1,2,3,4)
2 a[1] = 3
3 print(a)
Kết quảđoạn lệnh trên sẽlà:
A. (1,3,3,4)
B. (3,2,3,4)
C. (1,2,3,4)
D. Báo lỗi
4. Có thểtruy xuất các phần tửcủa một tập hợp thông qua toán tửindex []. Nhận
định trên đúng hay sai?

A. Đúng
B. Sai

The Dariu Foundation
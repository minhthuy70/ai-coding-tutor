<!-- page: 1 -->
# VI_PY_019: Ứng dụng Dictionary: Thuật toán đếm tần suất xuất hiện từ trong văn bản

**Nguồn tài liệu chính thống**: Giáo trình Python Căn Bản ĐH - TS. Lê Trọng Nhân  
**Chuyên mục**: Ứng dụng | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 99 -->
• Sửdụng Tuple giúp code an toàn hơn, bởi vì đặc tính của tuple giúp cho dữ
liệu không thểthay đổi. Do vậy nên lựa chọn tuple cho những dữliệu dạng
hằng số, dữliệu không thay đổi theo thời gian.
4
Cấu trúc dữliệu tập hợp (Set)
Set (hay còn gọi là tập hợp) là tập hợp có thểchứa nhiều các phần tửvà các phần
tửnày không có thứtự, vịtrí của nó hỗn loạn trong tập hợp..
Chúng ta có thểduyệt qua các phần tửtrong tập hợp, có thểthêm hoặc xóa đi
các phần tửvà thực hiện các phép toán tập hợp như phép hợp (union), phép giao
(intersection), phép hiệu (difference)... Bên cạnh đó, các phần tửcủa tập hợp phải
là các dữliệu không thểthay đổi như một số(int), một chuỗi (string), hoặc một
Tuple.
4.1
Khởi tạo và truy xuất các phần tửtrong tập hợp
Chúng ta cần chú ý các đặc tính của tập hợp như sau:
• Các phần tửtrong tập hợp không có thứtự.
• Các phần tửnày là duy nhất, không cho phép lặp lại.
• tập hợp có thểthay đổi (thêm bớt phần tử) nhưng các phần tửcủa tập hợp
phải ởdạng không thểthay đổi.
Các phần tửtrong tập hợp phân cách nhau bằng dấu phẩy và nằm trong dấu ngoặc
nhọn . Và do tính chất của tập hợp nên chúng ta không thểdùng toán tửindex []
đểtruy xuất các phần tửmà phải truy xuất trực tiếp các phẩn tửđó. Cụthểnhư ví
dụbên dưới:
1 a = {1, 2, 3, 4}
2 b = {{7.0 , "Xin chao", (4, 5, 6)}}
3 c = set() # cach tao mot tap hop rong
4
5 #duyet va in tat ca phan tu trong tap hop
6 for x in b:
7
print(x)
Chương trình 10.10: Khởi tạo và duyệt phần tửtrong tập hượp
4.2
Thay đổi tập hợp

<!-- page: 2 -->

Python hỗtrợrất nhiều các phương thức đểthực hiện thao tác thay đổi tập hợp và
chú ý là kết quảcó thểkhác đi do tập hợp không sắp xếp các phần tửtheo một trật
tựnào cả.
• add(): Phương thức sửdụng đểthêm một phần tửvào tập hợp.
• remove(): Loại bỏmột phần tửtrong tập hợp và báo lỗi nếu phần tửđó không
tồn tại.
Hướng dẫn lập trình Python cơ bản
Trang 99

<!-- page: 100 -->
• discard(): Tương tựnhư remove() nhưng nếu phần tửđó không tồn tại sẽ
không báo lỗi gì cả.
• pop(): Loại bỏmột phần tửngẫu nhiên khỏi tập hợp.
• clear(): Loại bỏtất cảcác phần tửtrong tập hợp.
• update(): Dùng đểthêm nhiều phần tửvào tập hợp.
4.3
Các phép toán trong tập hợp
Các tập hợp có lợi thếhơn các cấu trúc dữliệu khác ởchỗnó thực hiện được các
phép toán tập hợp như hợp, hiệu, giao... Và đểhiểu rõ hơn vềcác phép toán được
dùng phổbiến trong các tập hợp, chúng ta xem xét các ví dụsau:
4.3.1
Phép hợp (Union)
Hợp của hai tập hợp cho kết quảlà tất cảcác phần tửtrong hai tập hợp, chú ý phần
tửnào lặp lại sẽchỉxuất hiện 1 lần trong tập kết quả.
1 a = {1, 2, 3}
2 b = {3, 4}
3 c = a.union(b)
4 print(c) # ket qua la {1,2,3,4}
Chương trình 10.11: Phép hợp trong tập hợp
4.3.2
Phép giao (Intersection)
Phép giao hai tập hợp cho kết quảlà các phần tửđồng thời thuộc cảhai tập hợp.
1 a = {1, 2, 3}
2 b = {3, 4}
3 c = a.intersection(b)
4 print(c) # ket qua la {3}
Chương trình 10.12: Phép giao trong tập hợp
4.3.3
Phép hiệu (Difference)
Hiệu của một tập A trừđi một tập B cho kết quảlà tất các phần tửthuộc A nhưng
không thuộc B.
1 a = {1, 2, 3}
2 b = {3, 4}
3 c = a.difference(b)
4 print(c) # ket qua la {1, 2}

<!-- page: 3 -->

Chương trình 10.13: Phép hiệu trong tập hợp
Trang 100
The Dariu Foundation

<!-- page: 101 -->
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

<!-- page: 4 -->

như sau:
Hướng dẫn lập trình Python cơ bản
Trang 101

<!-- page: 102 -->
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
Trang 102
The Dariu Foundation

<!-- page: 103 -->
5.4
Một sốphương thức hay dùng trong từđiển

<!-- page: 5 -->

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
Trang 103
<!-- page: 1 -->
# VI_PY_025: Tập hợp Set và Bảng băm Dictionary: Cơ chế lưu trữ và tra cứu

**Nguồn tài liệu chính thống**: Bài giảng Python 3 - PGS.TS Đỗ Thanh Nghị (ĐH Cần Thơ)  
**Chuyên mục**: Cấu trúc dữ liệu | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 50 -->
50
Lập trình hướng đối tượng
Đối tượng (object)
Lớp (class)
Thực thể / thể hiện (instance)
Trạng thái (state)
Phương thức (method)
Truyền thông điệp (message passing)
Trừu tượng hoá (abstraction)
Đóng gói (encapsulation)
Kế thừa (inheritance)
Đa hình (polymorphism)
Tổng quát hoá (generalization)
Cụ thể hoá (specialization)

<!-- page: 51 -->
51
Lập trình hướng đối tượng
Định nghĩa lớp 
class ClassName:
```python
'Optional class documentation string'
class_suite
```
class_suite: các thuộc tính, phương thức (hàm)
Tham số đầu tiên của phương thức thường được đặt 
tên là self để thỏa:
obj.meth(args) = class.meth(obj, args) 
name: public, _name: protected, __name: private

<!-- page: 52 -->
52
Định nghĩa lớp


<!-- page: 2 -->

<!-- page: 53 -->
53
Tạo và sử dụng đối tượng

<!-- page: 54 -->
54
Truy xuất thuộc tính

<!-- page: 55 -->
55
Thuộc tính định nghĩa sẵn

<!-- page: 56 -->
56
Xóa đối tượng

<!-- page: 57 -->
57
Kế thừa
Định nghĩa lớp kế thừa 
class SubClassName (ParentClass1[, ParentClass2, ...]):
```python
'Optional class documentation string'
class_suite
```
Hàm issubclass(sub, sup), isinstance(obj, Class),
Hàm super()

<!-- page: 58 -->
58
Kế thừa (đa hình)

<!-- page: 59 -->
59
Kế thừa (đa hình)

<!-- page: 60 -->
60
Đa kế thừa
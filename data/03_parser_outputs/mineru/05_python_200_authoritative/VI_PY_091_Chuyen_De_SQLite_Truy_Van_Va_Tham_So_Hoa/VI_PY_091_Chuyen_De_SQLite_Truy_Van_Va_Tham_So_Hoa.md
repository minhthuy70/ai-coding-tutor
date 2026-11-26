<!-- page: 1 -->
# VI_PY_091: Chuyên đề SQLite: Thực thi INSERT, UPDATE, SELECT và Parameterized Query

**Nguồn tài liệu chính thống**: Tài liệu Cơ sở dữ liệu SQLite - Đại học  
**Chuyên mục**: SQLite | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 12 -->
SQL: Update
Cập nhật một/một vài cột theo điều kiện
UPDATE HocVien SET HoTen=‘Hồng Anh’ 
WHERE MaHV=3

<!-- page: 13 -->
Retrieving Records: Select
The select statement retrieves a group of 
records - you can either retrieve all the records 
or a subset of the records with a WHERE clause
SELECT * FROM HocVien
SELECT * FROM HocVien 
WHERE DienThoai=‘0909123456'

<!-- page: 14 -->
Sắp xếp với ORDER BY
Sử dụng ORDER BY ở câu lệnh SELECT để lấy kết quả 
có sắp xếp tăng hay giảm dần theo điều kiện nào đó.
SELECT * FROM HocVien ORDER BY HoTen
SELECT * FROM HocVien ORDER BY DienThoai DESC

<!-- page: 15 -->
15
Python vs SQLite
• Chèn thư viện:
import sqlite3
• Mở database để thao tác:
MyDB=sqlite3.connect(‘NhatNgheDB.db’)
trả về đối tượng Connection

<!-- page: 16 -->
16
•
Đối tượng này trỏ tới các bảng ghi (records/rows) 

<!-- page: 2 -->

trong tập dữ liệu lấy về và thực thi các câu truy vấn
import sqlite3
MyDB = sqlite3.connect(‘N:\\NhatNgheDb.db’)
c = MyDB.cursor()
Đối tượng cursor()

<!-- page: 17 -->
17
Cú pháp: cursor.execute()
Ví dụ: Câu lệnh DDL tạo bảng
#create a table of students
c.execute('''
CREATE TABLE HocVien
(
MaHV text PRIMARY KEY,
HoTen text,
DienThoai text,
NgaySinh date,
Email text
)
''')
Thực thi truy vấn – execute()

<!-- page: 18 -->
18
Cú pháp: cursor.execute()
Ví dụ: Câu lệnh DDL tạo mới dữ liệu
#insert data into our table
c.execute('''INSERT INTO HocVien
VALUES (‘001’,’Hien Luong’, ’0909009900’, 
’1/1/1981’,’hyhien@gmail.com’)
''')
Thực thi truy vấn – execute()

<!-- page: 19 -->
19
Sử dụng hàm commit()để lưu các thay đổi và sử 
dụng hàm close()để đóng kết nối.
#insert data into our table
c.execute('''INSERT INTO HocVien
VALUES (‘001’,’Hien’,’Luong’,’1/1/1981’,’11W’)’’’)
#Save changes using the commit() function
MyDB.commit()
#Close the database connection
MyDB.close()

<!-- page: 3 -->

Chú ý

<!-- page: 20 -->
20
Phương thức executemany()
• Cho phép thực thi nhiều câu lệnh SQL cùng một lúc
• Ví dụ:
products = (
(1, 'Ti vi', 1234),
(2, 'Máy giặt', 5712),
(3, 'Điều hòa', 9000),
(4, 'Volvo', 29000),
(5, 'Bentley', 350000),
(6, 'Hummer', 41400),
(7, 'Volkswagen', 21600)
)
cursor.executemany("INSERT INTO HangHoa VALUES(?, ?, ?)", products)

<!-- page: 21 -->
21
Truy vấn lấy dữ liệu - SELECT
• Bước 1:
cursor.execute(“SELECT statement”)
• Bước 2:
data = cursor.fetchone()
rows = cursor.fetchall()
• Bước 3:
for row in rows:
print(row)

<!-- page: 22 -->
22
Xem thêm
• https://www.sqlitetutorial.net/
• https://www.sqlitetutorial.net/sqlite-python/
• https://www.datacamp.com/community/tutor
ials/sqlite-in-python
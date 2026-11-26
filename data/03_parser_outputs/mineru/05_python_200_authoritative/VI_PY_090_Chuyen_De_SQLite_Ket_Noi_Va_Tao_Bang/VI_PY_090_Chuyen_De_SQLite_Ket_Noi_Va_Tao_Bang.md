<!-- page: 1 -->
# VI_PY_090: Chuyên đề SQLite: Khởi tạo kết nối, tạo bảng và cấu trúc schema

**Nguồn tài liệu chính thống**: Tài liệu Cơ sở dữ liệu SQLite - Đại học  
**Chuyên mục**: SQLite | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 2 -->
2
SQLite Browser
http://sqlitebrowser.org/

<!-- page: 3 -->
3
Relational Databases
http://en.wikipedia.org/wiki/Relational_database
Relational databases model data by storing rows 
and columns in tables.  The power of the relational 
database lies in its ability to efficiently retrieve data 
from those tables and in particular where there are 
multiple tables and the relationships between 
those tables involved in the query.

<!-- page: 4 -->
4
Terminology
• Database - contains many tables
• Relation (or table) - contains tuples and attributes
• Tuple (or row) - a set of fields that generally 
represents an “object” like a person or a music track
• Attribute (also column or field) - one of possibly 
many elements of data corresponding to the object 
represented by the row

<!-- page: 5 -->
5
A relation is defined as a set of tuples that have the same 
attributes.   A tuple usually represents an object and information 
about that object.  Objects are typically physical objects or 
concepts.   A relation is usually described as a table, which is 
organized into rows and columns.   All the data referenced by 
an attribute are in the same domain and conform to the same 

<!-- page: 2 -->

constraints. (Wikipedia)

<!-- page: 6 -->
6
Tables / 
Relations
Columns / Attributes
Rows /
Tuples

<!-- page: 7 -->
7
SQL
Structured Query Language is the language we 
use to issue commands to the database
- Create data (a.k.a Insert)
- Retrieve data
- Update data
- Delete data 
http://en.wikipedia.org/wiki/SQL

<!-- page: 8 -->
8
Database 
File
Python
Programs
You
SQLite
Browser
SQL
SQL
Input
Files
Output
Files
R
Excel
D3.js

<!-- page: 9 -->
9
Database 
Data Server
Application

<!-- page: 3 -->

Software
End
User
Developer
DBA
Database
Tools
SQL
SQL

<!-- page: 10 -->
SQL: Insert
Câu lệnh INSERT Chèn 1 dòng vào bảng
INSERT INTO HocVien (HoTen, DienThoai) 
VALUES (‘Nhất Nghệ', '028393 22735')

<!-- page: 11 -->
SQL: Delete
Xóa các dòng dựa vào điều kiện chọn
DELETE FROM HocVien 
WHERE DienThoai=‘0909123456'
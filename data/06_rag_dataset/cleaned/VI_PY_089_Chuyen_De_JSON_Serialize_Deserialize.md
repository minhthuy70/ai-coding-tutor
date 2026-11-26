# VI_PY_089: Chuyên đề JSON: Chuyển đổi đối tượng Python sang định dạng JSON

**Nguồn tài liệu chính thống**: Tài liệu Thao tác Tệp tin & JSON - Đại học
**Chuyên mục**: JSON | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

17
csv file
• https://docs.python.org/3/library/csv.html
• Text file which each rows using (,), (;), or tab (\t)
to separate value.
• Python support csv module:
– csv.field_size_limit – return maximum field size
– csv.get_dialect – get the dialect which is associated with the
name
– csv.list_dialects – show all registered dialects
– csv.register_dialect - associate dialect with name
– csv.unregister_dialect - delete the dialect associated with the
name the dialect registry

18
csv module
• csv.reader – read data from a csv file
• csv.writer – write data to a csv file
• csv.QUOTE_ALL - Quote everything, regardless of type.
• csv.QUOTE_MINIMAL - Quote fields with special
characters
• csv.QUOTE_NONNUMERIC - Quote all fields that aren't
numbers value
• csv.QUOTE_NONE – Don't quote anything in output

19
Read csv

20
Read file csv into Dictionary
import csv

with ('employee_birthday.txt', mode='r') as csv_file:
csv_reader = csv.DictReader(csv_file)
for row in csv_reader:
print(f'\t{row["name"]} - {row[“age"]}.')

21
Write csv
import csv
with ('employee_file.csv', mode='w') as employee_file:
employee_writer = csv.writer(employee_file, delimiter=',’,
quotechar='"', quoting=csv.QUOTE_MINIMAL)
employee_writer.writerow(['John Smith', 'Accounting', 'November’])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

22
Write csv from Dict
import csv
with ('employee_file2.csv', mode='w') as csv_file:
fieldnames = ['emp_name', 'dept']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting'})
writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT'})

23
Xửlý csv trong thư viện Pandas
import pandas
df = pandas.read_csv('hrdata.csv',
index_col='Name')
print(df)
import pandas
df = pandas.read_csv('hrdata.csv',
index_col='Name',
parse_dates=[‘Birth Date'])
print(df)

24
Xử lý csv trong thư viện Pandas
df = pandas.read_csv('hrdata.csv',
index_col='Employee',
parse_dates=['Hired'],

header=0,
names=['Employee', 'Hired', 'Salary', 'Sick Days’])
# Process data
# Write new file
df.to_csv('hrdata_modified.csv')

Excel file

26
Working excel file with openpyxl
• There
are
many
libraries
for
working
(read/write) with Excel file
• Openpyxl library:
– pip install openpyxl
– https://openpyxl.readthedocs.io/en/stable

27
Write data to excel file excel with openpyxl
# File excel (Workbook), trong file sẽ có nhiều Worksheet,
# trong worksheet có nhiều cell
from openpyxl import Workbook
wb = Workbook()
# Tạo worksheet có tên NIIE
ws = wb.create_sheet(“NIIE", 1)
ws["A1"] = “Viện Đào tạo Quốc tế“
# Ghi ô "A1"
ws.append([2, 3, 4])
# Thêm dòng mới
wb.save("DemoOpenpyxl.xlsx")
# Lưu file

28
Read data from excel file
from openpyxl import load_workbook
wb = load_workbook('demo.xlsx')
print (wb.sheetnames)

ws = wb[wb.sheetnames[0]]
for row in ws.values:
for value in row:
print(value,"\t",end='')
print("")

29
Working excel file with xlsxwriter
• https://xlsxwriter.readthedocs.io/
import xlsxwriter
Import xlsxwriter library
Hover mouse into line import
Choose Install package xlsxwriter

30
Working excel file with xlsxwriter
import xlsxwriter
# Tạo một file excel cùng 1 sheet
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
# thiết lập các cột cho file
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)
# định dạng tiêu đềcột in đậm
bold = workbook.add_format({'bold': True})
# thêm dòng tiêu đềvà định dạng in đậm
worksheet.write('A1', 'STT',bold)
worksheet.write('B1', 'MÃ SẢN PHẨM',bold)
worksheet.write('C1', 'TÊN SẢN PHẨM',bold)
worksheet.write('D1', 'SỐLƯỢNG',bold)
worksheet.write('E1', 'ĐƠN GIÁ',bold)
#thêm một dòng dữliệu
worksheet.write('A2',1)
worksheet.write('B2','SP1')
worksheet.write('C2', 'Coca')
worksheet.write('D2', '15')
worksheet.write('E2', '15000')
#thêm một dòng dữliệu
worksheet.write('A3',2)
worksheet.write('B3','SP2')

worksheet.write('C3', 'Pepsi')
worksheet.write('D3', '20')
worksheet.write('E3', '18000')
#Chèn Logo vào
worksheet.insert_image('B5', ‘HIENLTH.png')
workbook.close()
Chạy phần mềm và vào thư mục
phần mềm xem file Excel sẽcó kết
quảnhư mong muốn

31

32
PyQRCode
• pip install PyQRCode
• https://pythonhosted.org/PyQRCode
import pyqrcode
# String which represent the QR code
s = "https://www.youtube.com/c/HIENLTHChannel"
# Generate QR code
qr = pyqrcode.create(s)
# Create and save the png file naming
qr.svg("myyoutube.svg", scale=8)
qr.png("myyoutube.png", scale=8)
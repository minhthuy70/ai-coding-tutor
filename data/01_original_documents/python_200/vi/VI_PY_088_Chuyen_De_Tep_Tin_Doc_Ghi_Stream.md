<!-- page: 1 -->
# VI_PY_088: Chuyên đề Tệp tin: Đọc ghi luồng dữ liệu text và nhị phân

**Nguồn tài liệu chính thống**: Tài liệu Thao tác Tệp tin & JSON - Đại học  
**Chuyên mục**: Tệp tin | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm  
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

<!-- page: 2 -->
2
JSON
• JSON (JavaScript Object Notation) is a lightweight 
data-interchange format. It is easy for humans to 
read and write. It is easy for machines to parse and 
generate.
• Example: (like dict type)
{
"name": “Hien Luong",
"age": 18,
"isActive": true
}

<!-- page: 3 -->
3
Python and JSON
• import json
• JSON to Python
jsonData = '{"name": "Hien Luong", "age": 18}'
jsonToPython = json.loads(jsonData)
• Python to JSON
pythonDictionary = {
'name':'Hien', 'age’:40, 'isEmployed':True
}
dictionaryToJson =
json.dumps(pythonDictionary)

<!-- page: 4 -->
4
Python JSON functions
• Python JSON parsing function
– obj = load(file)
– obj = loads(string)
• Python JSON Serialization Functions

<!-- page: 2 -->

– dump(obj, file)
– str = dumps(obj)

<!-- page: 5 -->
5
Map Python type to json
Python
JSON
dict
object
list, tuple
array
str
string
int, float, int- & float-derived Enums
number
True
true
False
false
None
null

<!-- page: 6 -->
6
Map JSON to python
JSON
Python
object
dict
array
list
string
str
number (int)
int
number (real)
float
true
True
false
False
null
None


<!-- page: 3 -->

<!-- page: 7 -->
7
What is an API?
• An API, or Application Programming Interface, is a server 
that you can use to retrieve and send data to using code. 
APIs are most commonly used to retrieve data.
• Making API Requests in Python
– pip install requests

<!-- page: 8 -->
8
Working With JSON from an API example
• Call API form https://dummyjson.com/, parse and store in 
json file
import json, requests
result = requests.get('https://dummyjson.com/products')
pythondict = result.json()
print(json.dumps(pythondict, indent=4))
print(list(pythondict.keys()))

<!-- page: 9 -->
Working with other files
Word (python-docx)

<!-- page: 10 -->
10
python-docx
• pip install python-docx
• https://python-docx.readthedocs.io/en/latest/
• https://buildmedia.readthedocs.org/media/pdf/python-
docx/latest/python-docx.pdf

<!-- page: 11 -->
11
python-docx
• Import library: 
from docx import Document 
• Open existed file: 
document = Document('existing-doc-file.docx’) 
• Create new file:
document = Document() 
• Save file (.docx): 
document.save(filename)

<!-- page: 12 -->

<!-- page: 4 -->

12
python-docx
• document.add_heading(content, level)
– Title: document.add_heading("This is a title part, level=0)
– Level 1: document.add_heading("This is a heading 1", level=1) 
• Paragraph:
– p = document.add_paragraph(content)
– Alignment:
• from docx.enum.text import
WD_PARAGRAPH_ALIGNMENT
•p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

<!-- page: 13 -->
13
python-docx
• Paragraph(tt):
– Add sentences into paragraph:
• sentence_element = p.add_run(str(content))
– Set format bold/italic:
• sentence_element.bold = bold
• sentence_element.italic = italic
• entence_element.underline = underline

<!-- page: 14 -->
14
python-docx
• Insert picture
• Insert table

<!-- page: 15 -->
Working with csv files
(Comma Separated Values)
csv module

<!-- page: 16 -->
16
Spread sheet and corresponding CSV file
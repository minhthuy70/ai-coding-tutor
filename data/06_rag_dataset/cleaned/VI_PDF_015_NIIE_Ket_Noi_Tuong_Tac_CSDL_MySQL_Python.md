## python TM

## Unit 12

Python + MySQL

## MySQL

• Free opensource database

Simple way to have MySQL is using XAMPP [– https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)

• Working with MySQL in Python:

– PyMySQL:

<u>https://github.com/PyMySQL/PyMySQL</u>

## PyMySQL

import pymysql

```python
# Connect to the database
connection = pymysql.connect(host='localhost',
    user='user',
    password='passwd',
    database='db',
    cursorclass=pymysql.cursors.DictCursor)
```

## CUD example

with connection.cursor() as cursor: cursor.execute(sql\_statement)

\# connection is not autocommit by default. So you must commit to save your changes. connection.commit()

## Read data

with connection.cursor() as cursor: cursor.execute(sql\_statement)

result = cursor.fetchone()

result = cursor.fetchall()
<!-- page: 1 -->

- **Contents**
- **Python** Tutorial BASIC....1 #!/bin/python3
- python Getting Started....1 print("Hello, World!")
- Python Syntax....1 Python Syntax
- if 5 > 2:
- Python Comments....1 print("Five is greater than two!")
- if 5 > 2:
- Python - Variable Exercises....1 print("Five is greater than two!")
- Python Data Types....1 x = 5
- y = "Hello, World!"
- Python Numbers....2 print(x)
- print(y)
- Python Casting....2 #Five is greater than two!
- Python Strings....2 #Five is greater than two!
- #5
- Python Booleans....4 #Hello, World!
- Python Lists....4 Python Comments
- #This is a comment.
- Python Tuples....6 print("Hello, World!")
- """
- Python Sets....7 This is a comment
- Python Dictionaries....9 <sup>written</sup> in
- more than just one line
- """
- Python - Nested Dictionaries : từ điển lòng
- 10 print("Hello, World!")
- Hello, World!
- Python If ... Else....11 Hello, World!
- Python While Loops....11 Python - <sub>V</sub>ariable Exercises
- Python For Loops....11 x = str(3) # x will be '3'
- y = int(3) # y will be 3
- Python Functions....11 z = float(3) # z will be 3.0
- print(x,y,z)
- Python Lambda (ẩn danh)....12 x = 5
- Python Arrays....12 y = "John"
- print(type(x),type(y))
- x, y, z = "Orange", "Banana", "Cherry"
- print(x,y,z)
- x = "awesome"
- Python
- Python
- **Framework**
- **Machine learning**
- **Deep learning**
- Máy cái sota
- **Linear algebra**
- **Statistic & probability**
- **Pytorch, sklearn, caffe, tensorflow, keras**
- **Python Data Types**

## Python Tutorial BASIC

int, float, complex

<!-- page: 2 -->

```julia
Slicing Strings
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
```

```txt
String Format

age = 36
txt = "My name is John, and I am {}"
```

```python
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
if "Lorem" in a:
    print("Yes, 'free' is present.")
Hello
5
e
b a n a n a
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
Yes, 'free' is present.
```

```erb
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
x = ["apple", "banana", "cherry"]
#display x:
print(x)
#display the data type of x:
print(type(x))
['apple', 'banana', 'cherry']
<class 'list'>
```

```python
Python Numbers
#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(x)
print(x,y,z)
print(type(x),type(y),type(z))
1.0 2 (1+0j)
<class 'float'> <class 'int'> <class 'complex'>
```

```matlab
Python Casting
x = int(1)
y = int(2.8)
z = int("3")
print(x,y,z)
x = str("s1")
y = str(2)
z = str(3.0)
print(x,y,z)
1 2 3
s1 2 3.0
```

```txt
Python - Modify Strings
a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip()) #Remove Whitespace
print(a.split(", "))
HELLO, WORLD!
hello, world!
Hello, World!
[' Hello', ' World!']
```

```txt
txt = "Hello my friends"
txt.upper()
print(txt)
txt=txt.upper()
print(txt)
Hello my friends
HELLO MY FRIENDS
```

```python
Python Strings
Basic:
a = "Hello"
print(a)
print(len(a))
print(a[1])
for x in "banana":
    print(x,end=' ')
print()
a = """Lorem ipsum dolor sit amet,
```

Huy init | https://www.facebook.com/huyinit13

<!-- page: 3 -->

<table><tr><td rowspan="4" colspan="2">print(txt.format(age))quantity = 3itemno = 567price = 49.95myorder = &quot;I want {} pieces of item {} for {} dollars.&quot;print(myorder.format(quantity, itemno, price))myorder = &quot;I want to pay {2} dollars for {0} pieces of item {1).&quot;print(myorder.format(quantity, itemno, price))My name is John, and I am 36I want 3 pieces of item 567 for 49.95 dollars.I want to pay 49.95 dollars for 3 pieces of item 567.</td><td>isalpha()</td><td>string are alphanumericReturns True if all characters in the string are in the alphabet</td></tr><tr><td>isdecimal()</td><td>Returns True if all characters in the string are decimals</td></tr><tr><td>isdigit()</td><td>Returns True if all characters in the string are digits</td></tr><tr><td>isidentifier()</td><td>Returns True if the string is an identifier</td></tr><tr><td rowspan="3" colspan="2">String MethodsPython has a set of built-in methods that you can use on strings.Note: All string methods returns new values. They do not change the original string.</td><td>islower()</td><td>Returns True if all characters in the string are lower case</td></tr><tr><td>isnumeric()</td><td>Returns True if all characters in the string are numeric</td></tr><tr><td>isprintable()</td><td>Returns True if all characters in the string are printable</td></tr><tr><td>Method</td><td>Description</td><td>isspace()</td><td>Returns True if all characters in the string are whitespaces</td></tr><tr><td>capitalize()</td><td>Converts the first character to upper case</td><td>istitle()</td><td>Returns True if the string follows the rules of a title</td></tr><tr><td>casefold()</td><td>Converts string into lower case</td><td>isupper()</td><td>Returns True if all characters in the string are upper case</td></tr><tr><td>center()</td><td>Returns a centered string</td><td>join()</td><td>Joins the elements of an iterable to the end of the string</td></tr><tr><td>count()</td><td>Returns the number of times a specified value occurs in a string</td><td>ljust()</td><td>Returns a left justified version of the string</td></tr><tr><td>encode()</td><td>Returns an encoded version of the string</td><td>lower()</td><td>Converts a string into lower case</td></tr><tr><td>endswith()</td><td>Returns true if the string ends with the specified value</td><td>lstrip()</td><td>Returns a left trim version of the string</td></tr><tr><td>expandtabs()</td><td>Sets the tab size of the string</td><td>maketrans()</td><td>Returns a translation table to be used in translations</td></tr><tr><td>find()</td><td>Searches the string for a specified value and returns the position of where it was found</td><td>partition()</td><td>Returns a tuple where the string is parted into three parts</td></tr><tr><td>format()</td><td>Formats specified values in a string</td><td>replace()</td><td>Returns a string where a specified value is replaced with a specified value</td></tr><tr><td>format_map()</td><td>Formats specified values in a string</td><td>rfind()</td><td>Searches the string for a specified</td></tr><tr><td>index()</td><td>Searches the string for a specified value and returns the position of where it was found</td><td></td><td></td></tr><tr><td>isalnum()</td><td>Returns True if all characters in the</td><td></td><td></td></tr></table>

<!-- page: 4 -->

<table><tr><td></td><td>value and returns the last position of where it was found</td><td rowspan="2">print(bool(&quot;&quot;) print(bool())) print(bool([])) print(bool({})) def myFunction() : return True print(&quot;end &quot;,myFunction())</td></tr><tr><td>rindex()</td><td>Searches the string for a specified value and returns the last position of where it was found</td></tr><tr><td>rjust()</td><td>Returns a right justified version of the string</td><td rowspan="5">TrueFalseFalseTrueTrueFalseFalseFalseFalseFalseFalseEnd True</td></tr><tr><td>rpartition()</td><td>Returns a tuple where the string is parted into three parts</td></tr><tr><td>rsplit()</td><td>Splits the string at the specified separator, and returns a list</td></tr><tr><td>rstrip()</td><td>Returns a right trim version of the string</td></tr><tr><td>split()</td><td>Splits the string at the specified separator, and returns a list</td></tr><tr><td>splitlines()</td><td>Splits the string at line breaks and returns a list</td><td rowspan="5">Bộ sưu tập Python (Măng)Có bốn kiểu dữ liệu thu thập trong ngôn ngữ lập trình Python:Danh sách là một tập hợp được sắp xếp và có thể thay đổi. Cho phép các thành viên trùng lặp.Tuplelà một bộ sưu tập có thứ tự và không thể thay đổi. Cho phép các thành viên trùng lặp.Tập hợplà một tập hợp không có thứ tự và không được lập chỉ mục. Không có thành viên trùng lặp.Từ diễnlà một bộ sưu tập không có thứ tự và có thể thay đổi. Không có thành viên trùng lặp.</td></tr><tr><td>startswith()</td><td>Returns true if the string starts with the specified value</td></tr><tr><td>strip()</td><td>Returns a trimmed version of the string</td></tr><tr><td>swapcase()</td><td>Swaps cases, lower case becomes upper case and vice versa</td></tr><tr><td>title()</td><td>Converts the first character of each word to upper case</td></tr><tr><td>translate()</td><td>Returns a translated string</td><td rowspan="2">Khi chơn một kiểu tập hợp, sẽ rất hữu ích khi hiểu các thuộc tính của kiểu đó. Chơn loại phù hợp cho một tập dữ liệu cụ thể có thể có nghĩa là duy trì ý nghĩa và, nó có thể có nghĩa là tăng hiệu quả hoặc bảo mật.</td></tr><tr><td>upper()</td><td>Converts a string into upper case</td></tr><tr><td>zfill()</td><td>Fills the string with a specified number of 0 values at the beginning</td><td>Python Liststhislist = [&quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;]print(thislist)print(len(thislist))print(type(thislist))list1 = [&quot;abc&quot;, 34, True, 40, &quot;male&quot;]print(list1)print(type(list1))[apple&#x27;, &#x27;banana&#x27;, &#x27;cherry&#x27;]3</td></tr></table>

Huy init | https://www.facebook.com/huyinit13

<!-- page: 5 -->

```python
<class 'list'>
['abc', 34, True, 40, 'male']
<class 'list'>
Python - Access List Items
thislist = ["apple", "banana", "cherry", "orange",
"kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
banana
mango
['cherry', 'orange', 'kiwi']
['apple', 'banana', 'cherry', 'orange']
['cherry', 'orange', 'kiwi', 'melon', 'mango']
['orange', 'kiwi', 'melon']
Yes, 'apple' is in the fruits list
Python - add List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "watermelon"
print(thislist)
thislist.insert(2, "kiwi")
print(thislist)
thislist.append("orange")
print(thislist)
['apple', 'watermelon', 'cherry']
['apple', 'watermelon', 'kiwi', 'cherry']
['apple', 'watermelon', 'kiwi', 'cherry', 'orange']
Python - Remove List Items
thislist = ["apple", "banana",
"cherry", "union", "peach"]
thislist.remove("banana")
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[1]
print(thislist)
thislist.pop()
print(thislist)
thislist.clear()
print(thislist)
del thislist
#print(len(thislist)) : #this will cause an error because you have successfully deleted "thislist".
['apple', 'cherry', 'union', 'peach']
['apple', 'union', 'peach']
['apple', 'peach']
['apple']
Python - Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x,end=' ')
    print()
    for i in range(len(thislist)):
        print(thislist[i],end=' ')
    print()
    i = 0
    while i < len(thislist):
        print(thislist[i],end=' ')
        i = i + 1
    print()
    [print(x,end=' ') for x in thislist]
    apple banana cherry
    apple banana cherry
    apple banana cherry
    apple banana cherry
    apple banana cherry
Python - Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple",
"banana"]
thislist.sort()
    print(thislist)
    thislist.sort(reverse = True)
    print(thislist)
    thislist = [100, 50, 65, 82, 23]
    thislist.sort()
    print(thislist)
    def myfunc(n):
        return abs(n - 50)
    thislist.sort(key = myfunc)
    print(thislist)
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort()
    print(thislist)
    thislist.sort(key = str.lower)
    print(thislist)
    thislist.reverse()
    print(thislist)
```

<!-- page: 6 -->

<table><tr><td rowspan="3" colspan="2">[&#x27;banana&#x27;, &#x27;kiwi&#x27;, &#x27;mango&#x27;, &#x27;orange&#x27;, &#x27;pineapple&#x27;][&#x27;pineapple&#x27;, &#x27;orange&#x27;, &#x27;mango&#x27;, &#x27;kiwi&#x27;, &#x27;banana&#x27;][23, 50, 65, 82, 100][50, 65, 23, 82, 100][&#x27;Kiwi&#x27;, &#x27;Orange&#x27;, &#x27;banana&#x27;, &#x27;cherry&#x27;][&#x27;banana&#x27;, &#x27;cherry&#x27;, &#x27;Kiwi&#x27;, &#x27;Orange&#x27;][&#x27;Orange&#x27;, &#x27;Kiwi&#x27;, &#x27;cherry&#x27;, &#x27;banana&#x27;]</td><td>insert()</td><td>Adds an element at the specified position</td></tr><tr><td>pop()</td><td>Removes the element at the specified position</td></tr><tr><td>remove()</td><td>Removes the item with the specified value</td></tr><tr><td rowspan="2" colspan="2">thislist = [&quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;]mylist = thislist.copy()print(mylist)mylist = list(thislist)print(mylist)&#x27;apple&#x27;, &#x27;banana&#x27;, &#x27;cherry&#x27;][&#x27;apple&#x27;, &#x27;banana&#x27;, &#x27;cherry&#x27;]</td><td>reverse()</td><td>Reverses the order of the list</td></tr><tr><td>sort()</td><td>Sorts the list</td></tr><tr><td colspan="2">Python - List Methodslist1 = [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]list2 = [1, 2, 3]list3 = list1 + list2print(list3)list3=list1for x in list2:list3.append(x)print(list3)&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;, 1, 2, 3]&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;, 1, 2, 3]</td><td colspan="2">Python TuplesTuples are used to store multiple items in a single variable.A tuple is a collection which is ordered and unchangeable.Tuples are written with round brackets.Tuples được sử dụng để lưu trữ nhiều mục trong một biến duy nhất.Bộ tuple là một bộ sưu tập được sắp xếp theo thứ tự và không thể thay đổi .Tuples được viết bằng dấu ngoặc tròn.basicthistuple = (&quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;)print(thistuple)print(len(thistuple))(&#x27;apple&#x27;, &#x27;banana&#x27;, &#x27;cherry&#x27;)</td></tr><tr><td colspan="2">List Methods</td><td colspan="2"></td></tr><tr><td colspan="2">Python has a set of built-in methods that you can use on lists.</td><td colspan="2"></td></tr><tr><td>Method</td><td>Description</td><td rowspan="3" colspan="2">thistuple = (&quot;apple&quot;,)#you have to add a comma print(type(thistuple))#NOT a tuplethisttuple = (&quot;apple&quot;)print(type(thisttuple))</td></tr><tr><td>append()</td><td>Adds an element at the end of the list</td></tr><tr><td>clear()</td><td>Removes all the elements from the list</td></tr><tr><td>copy()</td><td>Returns a copy of the list</td><td rowspan="2" colspan="2">tuple1 = (&quot;abc&quot;, 34, True, 40, &quot;male&quot;)print(tuple1)&lt;class &#x27;tuple&#x27;&gt;&lt;class &#x27;str&#x27;&gt;(&#x27;abc&#x27;, 34, True, 40, &#x27;male&#x27;)</td></tr><tr><td>count()</td><td>Returns the number of elements with the specified value</td></tr><tr><td>extend()</td><td>Add the elements of a list (or any iterable), to the end of the current list</td><td colspan="2">Python - Access Tuple Items</td></tr><tr><td>index()</td><td>Returns the index of the first element with the specified value</td><td colspan="2">thistuple = (&quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;, &quot;orange&quot;, &quot;kiwi&quot;, &quot;melon&quot;, &quot;mango&quot;)print(thistuple[1])print(thistuple[-1])</td></tr></table>

<!-- page: 7 -->

Huy init | https://www.facebook.com/huyinit13

<!-- page: 8 -->

<table><tr><td colspan="2">Set Methods</td></tr><tr><td colspan="2">Python has a set of built-in methods that you can use on sets.</td></tr><tr><td>Method</td><td>Description</td></tr><tr><td>add()</td><td>Adds an element to the set</td></tr><tr><td>clear()</td><td>Removes all the elements from the set</td></tr><tr><td>copy()</td><td>Returns a copy of the set</td></tr><tr><td>difference()</td><td>Returns a set containing the difference between two or more sets</td></tr><tr><td>difference update()</td><td>Removes the items in this set that are also included in</td></tr></table>

```txt
Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x,end=' ')
print()
print("banana" in thisset)
cherry apple banana
True
Python - Add Set Items
thisset = {"apple", "banana"}
thisset.add("orange")
print(thisset)
tropical = {"pineapple",}
thisset.update(tropical)
print(thisset)
#it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
{'banana', 'orange', 'apple'}
{'banana', 'orange', 'pineapple', 'apple'}
{'apple', 'kiwi', 'banana', 'orange', 'pineapple'}
```

```lua
Python - Remove Set Items
#if the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry", "kiwi", "oil"}
thisset.remove("banana")
print(thisset)
#if the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("apple")
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
thisset.clear()
print(thisset)
del thisset
# print(thisset) sẽ bị lõi
{'kiwi', 'oil', 'cherry', 'apple'}
{'kiwi', 'oil', 'cherry'}
kiwi
{'oil', 'cherry'}
set()
```

Huy init | https://www.facebook.com/huyinit13

```lua
print(x,end='')
print()

banana apple cherry
Python - Join Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
{'a', 1, 2, 3, 'c', 'b'}
{'a', 1, 2, 3, 'c', 'b'}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
z = x.intersection(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
z = x.symmetric_difference(y)
print(z)
{'apple'}
{'apple'}
{'banana', 'google', 'cherry', 'microsoft'}
{'banana', 'apple', 'cherry'}
```

<!-- page: 9 -->

```txt
another, specified set

discard() Remove the specified item

intersection() Returns a set, that is the intersection of two other sets

intersection_u pdate() Removes the items in this set that are not present in other, specified set(s)

isdisjoint() Returns whether two sets have a intersection or not

issubset() Returns whether another set contains this set or not

issuperset() Returns whether this set contains another set or not

pop() Removes an element from the set

remove() Removes the specified element

symmetric_dif ference() Returns a set with the symmetric differences of two sets

symmetric_dif ference_update() inserts the symmetric differences from this set and another

union() Return a set containing the union of sets

update() Update the set with the union of this set and others
```

## Python Dictionaries

Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered\*, changeable and does not allow duplicates. Dictionaries are written with curly brackets, and have keys and values: Từ điển được sử dụng để lưu trữ các giá trị dữ liệu trong các cặp key: value.

```txt
Từ diễn là một tập hợp được sắp xếp theo thứ tự *, có thể thay đổi và không cho phép trùng lặp.
Từ diễn được viết bằng dấu ngoặc nhọn và có các khóa và giá trị:
Basic:
thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
Ford
3
<class 'dict'>
```

<!-- page: 10 -->

```python
dict_keys(['brand', 'model', 'year', 'name'])
dict_values(['Ford', 'Mustang', 1964, 'huy'])
dict_values(['Ford', 'Mustang', 1964, 'HUY'])
Yes, 'model' is in the thisdict dictionary
dict_items(['brand', 'Ford'), ('model', 'Mustang'),
('year', 1964), ('name', 'HUY'])

Python - Change Dictionary Items
thisdict =    {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

Python - Remove Dictionary Items
thisdict =    {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"name":"Huy"
}
thisdict.pop("model")
print(thisdict)
thisdict.popitem()#removes the last inserted item
print(thisdict)
thisdict.clear()
print(thisdict)
{'brand': 'Ford', 'year': 1964, 'name': 'Huy'}
{'brand': 'Ford', 'year': 1964}
{}

Python - Loop Dictionaries
thisdict =    {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict:
print(x,end=' ')
print()
for x in thisdict:
print(thisdict[x],end=' ')
print()
for x in thisdict.values():
print(x,end=' ')
```

Huy init | https://www.facebook.com/huyinit13

<!-- page: 11 -->

```python
Python has a set of built-in methods that you can use on dictionaries.
Method Description
clear() Removes all the elements from the dictionary
copy() Returns a copy of the dictionary
fromkeys() Returns a dictionary with the specified keys and value
get() Returns the value of the specified key
items() Returns a list containing a tuple for each key value pair
keys() Returns a list containing the dictionary's keys
pop() Removes the element with the specified key
popitem() Removes the last inserted key-value pair
setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update() Updates the dictionary with the specified key-value pairs
values() Returns a list of all the values in the dictionary
Python If ... Else
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
#The else keyword catches anything which isn't caught by the preceding conditions.
# and+or
a = 200
b = 33
if b > a:
print("b is greater than a")
elif a == b:
print("a and b are equal")
else:
print("a is greater than b")
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
c = 500
if a > b and c > a:
print("Both conditions are True")
if a > b or a > c:
print("At least one of the conditions is True")
a is greater than b
a is greater than b
A
Both conditions are True
At least one of the conditions is True
Python While Loops
i = 1
while i < 6:
print(i,end=' ')
i += 1
else:
print("\ni is no longer less than 6")
1 2 3 4 5
i is no longer less than 6
Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
print(x)
if x == "banana":break
for x in fruits:
if x == "banana":continue
print(x)
for x in range(6):
print(x,end= ' ')
else:
print("Finally finished!")
apple
banana
apple
cherry
0 1 2 3 4 5 Finally finished!
Python Functions
def my_function(fname):
print(fname + " Refsnes")
my_function("Emil")
def my_function1(country = "Norway"):
print("I am from " + country)
my_function1("India")
my_function1()
def my_function3(x):
```

<!-- page: 12 -->

## 12

```python
return 5 * x
print(my_function3(3))
print(my_function3(5))

Emil Refsnes
I am from India
I am from Norway
15
25

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result,end=' ')
    else:
        result = 0
    return result
tri_recursion(6)
1 3 6 10 15 21
```

```python
Python Lambda (ân danh)
x = lambda a: a + 10
print(x(5))
x = lambda a, b: a * b
print(x(5, 6))
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
15
30
13
```

## Python Arrays

```python
Note: This page shows you how to use LISTS as
ARRAYS, however, to work with arrays in Python
you will have to import a library, like the NumPy
library.
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
x = len(cars)
print(x)
for x in cars:
    print(x,end=' ')
cars.append("Honda")
print('\n',cars)
cars.pop(3)
print(cars)
['Toyota', 'Volvo', 'BMW']
```

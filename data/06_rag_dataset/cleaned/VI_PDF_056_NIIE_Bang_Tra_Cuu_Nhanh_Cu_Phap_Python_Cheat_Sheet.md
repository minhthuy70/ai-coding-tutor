## DataCamp Learn Python for Data Science Interactively

## Python For Data Science Cheat Sheet

Python Basics

Learn More Python for Data Science Interactively at www.datacamp.com

## Variables and Data Types

## Variable Assignment

```python
>>> x=5
```

```python
>>> x
```

## Calculations With Variables

| >>> x+27>>> x-23>>> x*2 > 1>0> x**225>>> x%21>>> x/float(2)2.5 | Sum of two variables Subtraction of two variables Multiplication of two variables Exponentiation of a variable Remainder of a variable Division of a variable |
| --- | --- |

## Types and Type Conversion

| str() int() float() bool() | '5', '3.45', 'True'5, 3, 15.0, 1.0True, True, True | Variables to strings Variables to integers Variables to floats Variables to booleans |
| --- | --- | --- |

## Asking For Help

```python
>>> help(str)
```

## Strings

```python
>>> my\_string = 'thisStringIsAwesome'
```

```python
>>> my\_string
```

'thisStringIsAwesome'

## String Operations

```python
>>> my\_string \* 2
```

'thisStringIsAwesomethisStringIsAwesome'

```python
>>> my\_string + 'Innit'
```

'thisStringIsAwesomeInnit'

```python
>>> 'm' in my\_string
```

True

## Lists

## Also see NumPy Arrays

```python
>>> a = 'is'
```

```python
>>> b = 'nice'
```

```python
>>> my\_list = ['my', 'list', a, b]
```

<u>>>> my\_list2 = [[4,5,6,7], [3,4,5,6]]</u>

## Selecting List Elements

## Index starts at 0

| Subset |  |
| --- | --- |
| >>> my_list[1] | Select item at index 1 |
| >>> my_list[-3] | Select 3rd last item |
| Slice |  |
| >>> my_list[1:3] | Select items at index 1 and 2 |
| >>> my_list[1:] | Select items after index 0 |
| >>> my_list[:3] | Select items before index 3 |
| >>> my_list[:] | Copy my_list |
| Subset Lists of Lists |  |
| >>> my_list2[1][0] | my_list[list][itemOfList] |
| >>> my_list2[1][:2] |  |

## List Operations

```python
>>> my\_list + my\_list
```

['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice']

```python
>>> my\_list \* 2
```

['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice']

```python
>>> my\_list2 > 4
```

True

## List Methods

| >>> my_list.index(a) | Get the index of an item |
| --- | --- |
| >>> my_list.count(a) | Count an item |
| >>> my_list.append('!') | Append an item at a time |
| >>> my_list.remove('!') | Remove an item |
| >>> del(my_list[0:1]) | Remove an item |
| >>> my_list.reverse() | Reverse the list |
| >>> my_list.extend('!') | Append an item |
| >>> my_list.pop(-1) | Remove an item |
| >>> my_list.insert(0,'!') | Insert an item |
| >>> my_list.sort() | Sort the list |

## String Operations

```python
>>> my\_string[3]
```

```python
>>> my\_string[4:9]
```

## String Methods

```python
>>> my\_string.upper()
```

```python
>>> my\_string.lower()
```

```python
>>> my\_string.count('w')
```

String to uppercase

```python
>>> my\_string.replace('e', 'i')
```

## Index starts at 0

String to lowercase

```python
>>> my\_string.strip()
```

Count String elements

Replace String elements

Strip whitespaces

## Libraries

## Import libraries

```python
>>> import numpy
```

```python
>>> import numpy as np
```

**Selective import**

```python
>>> from math import pi
```

## Install Python

## ANACONDA

Leading open data science platform powered by Python

Machine learning

matplotlib

2D plotting

Free IDE that is included with Anaconda

## Numpy Arrays

## Also see Lists

```python
>>> my\_list = [1, 2, 3, 4]
```

```python
>>> my\_array = np.array(my\_list)
```

<u>>>> my\_2darray = np.array([[1,2,3],[4,5,6]])</u>

## Selecting Numpy Array Elements

## Index starts at 0

| Subset >>> my_array[1]2Slice >>> my_array[0:2] array([1, 2]) Subset 2D Numpy arrays >>> my_2darray[:,0] array([1, 4]) | Select item at index 1 Select items at index 0 and 1 my_2darray[rows, columns] |
| --- | --- |

## Numpy Array Operations

```python
>>> my\_array > 3
```

array([False, False, False, True], dtype=bool)

```python
>>> my\_array \* 2
```

array([2, 4, 6, 8])

```python
>>> my\_array + np.array([5, 6, 7, 8])
```

array([6, 8, 10, 12])

## Numpy Array Functions

```python
>>> my\_array.shape
```

```python
>>> np.append(other\_array)
```

```python
>>> np.insert(my\_array, 1, 5)
```

```python
>>> np.delete(my\_array,[1])
```

```python
>>> np.mean(my\_array)
```

```python
>>> np.median(my\_array)
```

```python
>>> my\_array.corrcoef()
```

```python
>>> np.std(my\_array)
```

Append items to an array

Insert items in an array

Delete items in an array

Mean of the array

Median of the array

Correlation coefficient

Standard deviation

```txt
On mutable sequences (list), remove with del lst[3:5] and modify with assignment lst[1:4]=[15,25]
```

```csv
integer, float, boolean, string, bytes
base Types
int 783 0 -192 0b010 0o642 0xF3
float 9.23 0.0 -1.7e-6
bool True False ×10⁻⁶
str "One\nTwo" Multiline string:
escaped new line """X\tY\tZ
'I\'m' 1\t2\t3"""
escaped ' escaped tab
bytes b"toto\xfe\775"
hexadecimal octal immutables
txt
■ ordered sequences, fast index access, repeatable values
    list [1,5,9]      ["x",11,8.9]      ["mot"]          []
    tuple (1,5,9)        11,"y",7.4       ("mot",)          ()
Non modifiable values (immutables)     expression with only comas →tuple
    str bytes (ordered sequences of chars / bytes)
■ key containers, no a priori order, fast key access, each key is unique
dictionary   dict {"key":"value"}     dict(a=3,b=4,k="v")    {}
(key/value associations) {1:"one",3:"three",2:"two",3.14:"n"}
collection     set {"key1","key2"}     {1,9,3,0}           set ()
keys=hashable values (base types, immutables...)     frozenset immutable set     empty
python
for variables, functions,
modules, classes... names
a...zA...Z_ followed by a...zA...Z_0...9
□ diacritics allowed but should be avoided
□ language keywords forbidden
□ lower/UPPER case discrimination
    ☺ a toto x7 y_max BigOne
    ☺ 8y and for
```

## Variables assignment

= Variables assignment
assignment $\Leftrightarrow$ binding of a name with a value
evaluation of right side expression value
assignment in order with left side names
x=1.2+8+sin(y)
a=b=c=0 assignment to same value
y,z,r=9.2,-7.6,0 multiple assignments
a,b=b,a values swap
$\left.\begin{array}{l}\text{a,*b=seq}\\ \text{*a,b=seq}\end{array}\right\}$ unpacking of sequence in item and list
x+=3 increment $\Leftrightarrow$ x=x+3 and *=
x-=2 decrement $\Leftrightarrow$ x=x-2 /=
x=None « undefined » constant value %=
del x remove name x ...

```csv
int("15") → 15
int("3f",16) → 63
int(15.56) → 15
float("-11.24e8") → -1124000000.0
round(15.56,1)→ 15.6
bool(x)
str(x) → "..." representation string of x for display (cf. formatting on the back)
chr(64) → '@' ord('@') → 64 code ↔ char
repr(x) → "..." literal representation string of x
bytes([72,9,64]) → b'H\t@
list("abc") → ['a','b','c']
dict([(3,"three"),(1,"one")]) → {1:'one',3:'three'}
set(["one","two"]) → {'one','two'}
separator str and sequence of str → assembled str
':'.join(['toto','12','pswd']) → 'toto:12:pswd'
str split on whitespaces → list of str
"words with spaces".split() → ['words','with','spaces']
str split on separator str → list of str
"1,4,8,2".split(",") → ['1','4','8','2']
sequence of one type → list of another type (via list comprehension)
[int(x) for x in ('1','29','-3')] → [1,29,-3]
```

## for lists, tuples, strings, bytes…

<table><tr><td>negative index</td><td>-5</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td></tr><tr><td>positive index</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td colspan="6">1st=[10, 20, 30, 40, 50]</td></tr><tr><td>positive slice</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>negative slice</td><td>-5</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td></tr></table>

**Items count**

## Access to sub-sequences via lst[start slice:end slice:step]

**lst[:-1]→[10,20,30,40]**

**lst[1:-1]→[20,30,40]**

**len(lst)→5**

☝ **index from 0** (here from 0 to 4)

```json
1st[::-2]→[50,30,10]
```

## Sequence Containers Indexing

Individual access to **items** via **lst[**index]

⇒ first one

**lst[-1]→50**⇒ last one

**lst[1]→20**

On mutable sequences (**list**), remove with **del lst[3]** and modify with assignment **lst[4]=25**

**lst[-2]→40**

**lst[1:3]→[20,30]**

**lst[:3]→[10,20,30]**

**lst[3:]→[40,50]**

```txt
1st [::2]→[10, 30, 50]    lst [:]→[10, 20, 30, 40, 50] shallow copy of sequence
```

## Missing slice indication → from start / up to end.

## Boolean Logic

Comparisons : **< > <= >= == !=** (boolean results) ≤ ≥ = ≠

**a and b** logical andboth simulta--neously

**a or b** logical orone or other or both

☝ pitfall : **and** and **or** return value of a or of b (under shortcut evaluation). ⇒ ensure that a and b are booleans.

**not a**logical not

True and False constants

**False**

## ☝ floating numbers… approximated values

Operators: **+ - \* / // % \*\***

Priority (…) × ÷ A A a<sup>b</sup>

## Statements Blocks

integer ÷ ÷ remainder

@ → matrix × python3.5+**numpy**

## parent statement:

statement block 1…

parent statement:

statement block2…

next statement after block 1

☝ configure editor to insert 4 spaces in place of an indentation tab.

## angles in radians

**from math import sin,pi…**

**sin(pi/4)→0.707…**

**cos(2\*pi/3)→-0.4999…**

**sqrt(81)→9.0**

**log(e\*\*2)→2.0**

**ceil(12.5)→13**

**floor(12.5)→12**

module **truc**⇔file **truc.py**

## Modules/Names Imports

**from monmod import nom1,nom2 as fct**

**import monmod** →access via **monmod.nom1** …

<u>☝ modules and packages searched in python path (cf</u> <strong><u>sys.path</u></strong><u>)</u>

## statement block executed only

**if** a condition is true

**if** logical condition:

statements block

Can go with several elif, elif... and only one final else. Only the block of first true condition is executed.

☝ with a var x:

**if bool(x)==True:** ⇔ **if x:**

**if bool(x)==False:** ⇔ **if not x:**

Signaling an error: **raise** ExcClass(…) Errors processing: **try:** normal procesising block **except** Exception **as e:** error processing block

## Conditional Statement

**if age<=18:**

**state="Kid"**

**elif age>65:**

**state="Retired"**

**else:**

**state="Active"**

## Exceptions on Errors

☝ **finally** block for final processing in all cases.

```python
s = input("Instructions:")
input always returns a string, convert it to required type (cf. boxed Conversions on the other side).
python
Go over sequence's values
s = "Some text" } initializations before the loop
cnt = 0
loop variable, assignment managed by for statement
for 'c' in s:
    if c == "e":          Algo: count
        cnt = cnt + 1         number of e
    print("found",cnt,"'e'")      in the string.
loop on dict/set ⇔ loop on keys sequences
use slices to loop on a subset of a sequence
```

**while** logical condition: statements block

**for var in** sequence: statements block

☝ make condition variable change !

## Display

items to display : literal values, variables, expressions **print** options:

```txt
items separator, default space
end of print, default new line
print to file, default standard output
```

<strong><u>Input</u></strong>

```python
len(c) → items count
min(c) max(c) sum(c)
sorted(c) → list sorted copy
val in c → boolean, membership operator in (absence not in)
enumerate(c) → iterator on (index, value)
zip(c1, c2...) → iterator on tuples containing c_i items at same index
all(c) → True if all c items evaluated to true, else False
any(c) → True if at least one item of c evaluated true, else False

Specific to ordered sequences containers (lists, tuples, strings, bytes...)
reversed(c) → inversed iterator c*5 → duplicate c+c2 → concatenate
c.index(val) → position c.count(val) → events count
import copy
copy.copy(c) → shallow copy of container
copy.deepcopy(c) → deep copy of container
kotlin
modify original list
lst.append(val)
lst.extend(seq)
lst.insert(idx, val)
lst.remove(val)
lst.pop([idx]) →value
lst.sort()    lst.re
```

## Operations on Lists

```txt
add item at end
add sequence of items at end
insert item at index
remove first item with value val
remove & return item at index idx (default last)
erse() sort / reverse liste in place
```

## Operations on Dictionaries

```txt
d[key]=value        d.clear()
d[key]→ value       del d[key]
d.update(d2) {update/add
                    associations
d.keys()
d.values()} → iterable views on
d.items()      keys/values/associations
d.pop(key[,default]) → value
d.popitem() → (key,value)
d.get(key[,default]) → value
d.setdefault(key[,default]) → value
```

## Operations on Sets

```python
Operators:
  | → union (vertical bar char)
  & → intersection
  - ^ → difference/symmetric diff.
  < <= > >= → inclusion relations
Operators also exist as methods.

s.update(s2) s.copy()
s.add(key) s.remove(key)
s.discard(key) s.clear()
s.pop()
python
Go over sequence's index
□ modify item at index
□ access items around index (before / after)
lst = [11,18,9,12,23,4,17]
lost = []
for idx in range(len(lst)):          Algo: limit values greater than 15, memorizing of lost values.
    val = lst[idx]                     lost.append(val)
    if val > 15:                    lost.append(val)
        lst[idx] = 15
print("modif:",lst,"-lost:",lost)
txt
range ([start,] end [,step])
start default 0, end not included in sequence, step signed, default 1
range (5) → 0 1 2 3 4 range (2, 12, 3) → 2 5 8 11
range (3, 8) → 3 4 5 6 7 range (20, 5, -5) → 20 15 10
range (len(seq)) → sequence of index of values in seq
range provides an immutable sequence of int constructed as needed
```

<strong><u>Function Definition</u></strong>

```python
def fct(x,y,z):
    """documentation"""
    # statements block, res computation, etc.
    return res← result value of the call, if no computed
    result to return: return None
parameters and all
variables of this block exist only in the block and during the function
call (think of a "black box")
Advanced: def fct(x,y,z,*args,a=3,b=5,**kwargs):
    *args variable positional arguments (→tuple), default values,
    **kwargs variable named arguments (→dict)
```

```txt
r = fct(3,i+2,2*i)
storage/use of      one argument per
returned value       parameter
```

<strong><u>Function Call</u></strong>

```txt
this is the use of function name with parentheses which does the call
```

Advanced: \*sequence \*\*dict

```txt
s.startswith(prefix[,start[,end]])
s.endswith(suffix[,start[,end]]) s.strip([chars])
s.count(sub[,start[,end]]) s.partition(sep) → (before,sep,after)
s.index(sub[,start[,end]]) s.find(sub[,start[,end]])
s.is...() tests on chars categories (ex. s.isalpha())
s.upper() s.lower() s.title() s.swapcase()
s.casefold() s.capitalize() s.center([width,fill])
s.ljust([width,fill]) s.rjust([width,fill]) s.zfill([width])
s.encode(encoding) s.split([sep]) s.join(seq)
formatting
formating directives
"modele{} {} {}".format(x,y,r) → str
"{selection: formatting!conversion}"
□ Selection:
2
nom
0.nom
4[key]
0[2]
Examples
{
:+2.3f}".format(45.72793)
→'+45.728'
"{1:>10s}".format(8,"toto")
→' toto'
"{x!r}".format(x="I'm")
→'"I\'m'"
□ Formatting:
fill char alignment sign mini width.precision~maxwidth type
<>^ = + - space 0 at start for filling with 0
integer: b binary, c char, d decimal (default), o octal, x or X hexa...
float: e or E exponential, f or F fixed point, g or G appropriate (default),
string: s ...
Conversion : s (readable text) or r (literal representation)
```

| s.lower() - Returns a lowercase version of s |
| --- |
| s.title() - Returns s with the first letter of every word capitalized |
| "23".zfill(4) - Returns "0023" by left-filling the string with 0's to make it's length 4. |
| s.splitlines() - Returns a list by splitting the string on any newline characters. |
| Python strings share some common methods with lists s[:5] - Returns the first 5 characters of s |
| "fri" + "end" - Returns "friend" |
| "end" in s - Returns True if the substring "end" is found in s |

# Data Science Cheat Sheet

Python - Intermediate

## KEY BASICS, PRINTING AND GETTING HELP

This cheat sheet assumes you are familiar with the content of our Python Basics Cheat Sheet

s - A Python string variable

i - A Python integer variable

f - A Python float variable

l - A Python list variable

d - A Python dictionary variable

## LISTS

| 1.pop(3) - Returns the fourth item from 1 and deletes it from the list |
| --- |
| 1.remove(x) - Removes the first item in 1 that is equal to x |
| 1.reverse() - Reverses the order of the items in 1 |
| 1[1::2] - Returns every second item from 1, commencing from the 1st item |
| 1[-5:] - Returns the last 5 items from 1 specific axis |

## STRINGS

## RANGE

Range objects are useful for creating sequences of integers for looping.

**range(5)** - Returns a sequence from 0 to 4

**range(2000,2018)** - Returns a sequence from **2000** to **2017**

**range(0,11,2)** - Returns a sequence from 0 to **10**, with each item incrementing by 2

**range(0,-10,-1)** - Returns a sequence from 0 to **-9 list(range(5))** - Returns a list from 0 to 4

## DICTIONARIES

**max(d, key=d.get)** - Return the key that corresponds to the largest value in d

**min(d, key=d.get)** - Return the key that

corresponds to the smallest value in d

## SETS

**my\_set = set(l)** - Return a **set** object containing the unique values from l

**a in my\_set** - Returns **True** if the value a exists in **my\_set**

## REGULAR EXPRESSIONS

**import re** - Import the Regular Expressions module **re.search("abc",s)** - Returns a **match** object if the regex **"abc"** is found in s, otherwise **None**

## LIST COMPREHENSION

A one-line expression of a for loop

**[i \*\* 2 for i in range(10)]** - Returns a list of the squares of values from 0 to 9

**[s.lower() for s in l\_strings]** - Returns the list **l\_strings**, with each item having had the**.lower()** method applied

**[i for i in l\_floats if i < 0.5]** - Returns the items from **l\_floats** that are less than **0.5**

## FUNCTIONS FOR LOOPING

**for i, value in enumerate(l): print("The value of item {} is {}". format(i,value))**

\- Iterate over the list l, printing the index location of each item and its value

**for one, two in zip(l\_one,l\_two): print("one: {}, two: {}".format(one,two))**

\- Iterate over two lists, **l\_one** and **l\_two** and print each value

**while x < 10:**

**x += 1**

\- Run the code in the body of the loop until the value of x is no longer less than **10**

## DATETIME

**import datetime as dt** - Import the **datetime** module

**now = dt.datetime.now()** - Assign **datetime** object representing the current time to **now wks4 = dt.datetime.timedelta(weeks=4)**

\- Assign a **timedelta** object representing a timespan of 4 weeks to **wks4**

## now - wks4 - Return a datetime object

representing the time 4 weeks prior to **now newyear\_2020 = dt.datetime(year=2020, month=12, day=31)** - Assign a **datetime** object representing December 25, 2020 to **newyear\_2020**

**newyear\_2020.strftime("%A, %b %d, %Y")** - Returns **"Thursday, Dec 31, 2020"**

**dt.datetime.strptime('Dec 31, 2020',"%b%d, %Y")** - Return a **datetime** object representing December 31, 2020

## RANDOM

| import random - Import the random module |
| --- |
| random.random() - Returns a random float between 0.0 and 1.0 |
| random.randint(0,10) - Returns a random integer between 0 and 10 |
| random.choice(1) - Returns a random item from the list 1 |

## COUNTER

**from collections import Counter** - Import the **Counter** class

**c = Counter(l)** - Assign a **Counter** (dict-like) object with the counts of each unique item from l, to c

**c.most\_common(3)** - Return the 3 most common items from l

## TRY/EXCEPT

Catch and deal with Errors

**l\_ints = [1, 2, 3, "", 5]** - Assign a list of integers with one missing value to **l\_ints**

**l\_floats = []**

**for i in l\_ints:**

**try:**

**l\_floats.append(float(i))**

**except:**

**l\_floats.append(i)**

\- Convert each value of **l\_ints** to a float, catching and handling **ValueError: could not convert string to float:** where values are missing.

## Python For Data Science Cheat Sheet

Pandas Basics

Learn Python for Data Science **Interactively** at www.DataCamp.com

## Pandas

The **Pandas** library is built on NumPy and provides easy-to-use **data structures** and **data analysis** tools for the Python

programming language.

pandas

Use the following import convention:

```python
>>> import pandas as pd
```

## Pandas Data Structures

## Series

A **one-dimensional** labeled array capable of holding any data type

```python
>>> s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
```

## DataFrame

Columns

Index

| Country | Capital | Population |
| --- | --- | --- |
| Belgium | Brussels | 11190846 |
| India | New Delhi | 1303171035 |
| Brazil | Brasília | 207847528 |

A **two-dimensional** labeled data structure with columns of potentially different types

```python
>>> data = {'Country': ['Belgium', 'India', 'Brazil'], 'Capital': ['Brussels', 'New Delhi', 'Brasília'] 'Population': [11190846, 1303171035, 207847528]}
```

```python
>>> df = pd.DataFrame(data,
```

columns=['Country', 'Capital', 'Population'])

## I/O

## Read and Write to CSV

```python
>>> pd.read\_csv('file.csv', header=None, nrows=5)
```

<u>>>> df.to\_csv('myDataFrame.csv')</u>

## Read and Write to Excel

```python
>>> pd.read\_excel('file.xlsx')
```

```python
>>> pd.to\_excel('dir/myDataFrame.xlsx', sheet\_name='Sheet1')
```

**Read multiple sheets from the same file**

```python
>>> xlsx = pd.ExcelFile('file.xls')
```

## Asking For Help

```python
>>> df = pd.read\_excel(xlsx, 'Sheet1')
```

```python
>>> help(pd.Series.loc)
```

## Selection

**Getting**

```python
>>> s['b'] -5
```

```python
>>> df[1:] Country Country
```

Capital Population

1 India New Delhi 1303171035

2 Brazil Brasília 207847528

## Selecting, Boolean Indexing & Setting

## By Position

```python
>>> df.iloc[[0],[0]]
```

'Belgium'

```python
>>> df.iat([0],[0])
```

Get one element

'Belgium'

## By Label

Get subset of a DataFrame

```python
>>> df.loc[[0], ['Country']] 'Belgium'
```

```python
>>> df.at([0], ['Country']) 'Belgium'
```

**Also see NumPy Arrays**

## By Label/Position

```python
>>> df.ix[2] Country Brazil Capital Brasília Population 207847528
```

```python
>>> df.ix[:,'Capital']
```

0 Brussels

1 New Delhi

2 Brasília

Select single value by row & column

Select single value by row & column labels

Select single row of subset of rows

Select a single column of subset of columns

## >>> df.ix[1,'Capital']

'New Delhi'

## Boolean Indexing

```python
>>> s[\~(s > 1)]
```

Select rows and columns

```python
>>> s[(s < -1) | (s > 2)]
```

```python
>>> df[df['Population']>1200000000] **Setting**
```

```python
>>> s['a'] = 6
```

Series s where value is not >1 s where value is <-1 or >2 Use filter to adjust DataFrame

Set index a of Series s to 6

## Read and Write to SQL Query or Database Table

```python
>>> from sqlalchemy import create\_engine
```

```python
>>> engine = create\_engine('sqlite:///:memory:')
```

```python
>>> pd.read\_sql("SELECT \* FROM my\_table;", engine)
```

```python
>>> pd.read\_sql\_table('my\_table', engine)
```

<u>>>> pd.read\_sql\_query("SELECT \* FROM my\_table;", engine)</u>

read\_sql()is a convenience wrapper around read\_sql\_table() and read\_sql\_query()

```python
>>> pd.to\_sql('myDf', engine)
```

## Dropping

```python
>>> s.drop(['a', 'c'])
```

```python
>>> df.drop('Country', axis=1)
```

Drop values from rows (axis=0)

## Sort & Rank

Drop values from columns(axis=1)

```python
>>> df.sort\_index() >>> df.sort\_values(by='Country') >>> df.rank()
```

Sort by labels along an axis Sort by the values along an axis Assign ranks to entries

## ~~Retrieving Series/DataFrame Information~~

## Basic Information

```python
>>> df.shape
```

```python
>>> df.index
```

```python
>>> df.columns
```

```python
>>> df.info()
```

```python
>>> df.count()
```

## Summary

(rows,columns) Describe index Describe DataFrame columns Info on DataFrame Number of non-NA values

```python
>>> df.sum()
```

```python
>>> df.cumsum()
```

```python
>>> df.min()/df.max()
```

Sum of values

```python
>>> df.idxmin()/df.idxmax()
```

Cummulative sum of values

```python
>>> df.describe()
```

Minimum/maximum values

```python
>>> df.mean()
```

Minimum/Maximum index value

```python
>>> df.median()
```

Summary statistics

Mean of values

Median of values

## Applying Functions

```python
>>> f = lambda x: x\*2
```

```python
>>> df.apply(f)
```

```python
>>> df.applymap(f)
```

Apply function

Apply function element-wise

## Data Alignment

## Internal Data Alignment

NA values are introduced in the indices that don’t overlap:

```python
>>> s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
```

```python
>>> s + s3
```

a 10.0

b **NaN**

c 5.0

d 7.0

## Arithmetic Operations with Fill Methods

## You can also do the internal data alignment yourself with the help of the fill methods:

```python
>>> s.add(s3, fill\_value=0)
```

a 10.0

b **-5.0**

c 5.0

d 7.0

```python
>>> s.sub(s3, fill\_value=2)
```

```python
>>> s.div(s3, fill\_value=4)
```

```python
>>> s.mul(s3, fill\_value=3)
```

## Python For Data Science Cheat Sheet

NumPy Basics

Learn Python for Data Science **Interactively** at www.DataCamp.com

## NumPy

The **NumPy** library is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.

Use the following import convention:

```python
>>> import numpy as np
```

## NumPy Arrays

**1D array**

**2D array**

1 2 3

**3D array**

axis 1

## Creating Arrays

```python
>>> a = np.array([1,2,3])
```

```python
>>> b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
```

```python
>>> c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],
```

dtype = float)

## Initial Placeholders

| >>> np.zeros((3,4))>>> np.ones((2,3,4),dtype=np.int16)>>> d = np.arange(10,25,5)>>> np.linspace(0,2,9)>>> e = np.full((2,2),7)>>> f = np.eye(2)>>> np.random.random((2,2))>>> np.empty((3,2)) | Create an array of zerosCreate an array of onesCreate an array of evenly spaced values (step value)Create an array of evenly spaced values (number of samples)Create a constant arrayCreate a 2X2 identity matrixCreate an array with random valuesCreate an empty array |
| --- | --- |

**I/O**

## Saving & Loading On Disk

```python
>>> np.save('my\_array', a)
```

```python
>>> np.savez('array.npz', a, b)
```

```python
>>> np.load('my\_array.npy')
```

## Saving & Loading Text Files

```python
>>> np.loadtxt("myfile.txt")
```

```python
>>> np.genfromtxt("my\_file.csv", delimiter=',')
```

<u>>>> np.savetxt("myarray.txt", a, delimiter=" ")</u>

## Data Types

```python
>>> np.int64
```

```python
>>> np.float32
```

```python
>>> np.complex
```

```python
>>> np.bool
```

```python
>>> np.object
```

```python
>>> np.string\_
```

```python
>>> np.unicode\_
```

Signed 64-bit integer types Standard double-precision floating point Complex numbers represented by 128 floats Boolean type storing TRUE and FALSE values Python object type Fixed-length string type Fixed-length unicode type

## Inspecting Your Array

```python
>>> a.shape
```

```python
>>> len(a)
```

```python
>>> b.ndim
```

```python
>>> e.size
```

```python
>>> b.dtype
```

```python
>>> b.dtype.name
```

```python
>>> b.astype(int)
```

## Asking For Help

Array dimensions Length of array Number of array dimensions Number of array elements Data type of array elements Name of data type Convert an array to a different type

```python
>>> np.info(np.ndarray.dtype)
```

## Array Mathematics

## Arithmetic Operations

```python
>>> g = a - b
```

array([[ 2.5, 4. , 6. ],

```python
>>> np.multiply(a,b) >>> np.exp(b) >>> np.sqrt(b) >>> np.sin(a) >>> np.cos(b) >>> np.log(a) >>> e.dot(f) array([[ 7., 7.], [ 7., 7.]])
```

## Comparison

Subtraction

Subtraction Addition

],]])

## Aggregate Functions

| >>> a == barray([[False, True, True],[False, False, False]], dtype=bool)>>> a &lt; 2array([True, False, False], dtype=bool)>>> np.array_equal(a, b) | Element-wise comparisonElement-wise comparisonArray-wise comparison |
| --- | --- |

Addition Division

Division Multiplication

Multiplication Exponentiation Square root Print sines of an array Element-wise cosine Element-wise natural logarithm Dot product

## Copying Arrays

| >>> a.sum() | Array-wise sum |
| --- | --- |
| >>> a.min() | Array-wise minimum value |
| >>> b.max(axis=0) | Maximum value of an array row |
| >>> b.cumsum(axis=1) | Cumulative sum of the elements |
| >>> a.mean() | Mean |
| >>> b.median() | Median |
| >>> a.corrcoef() | Correlation coefficient |
| >>> np.std(b) | Standard deviation |

## Sorting Arrays

```python
>>> a.sort()
```

```python
>>> c.sort(axis=0)
```

| >>> h = a.view() | Create a view of the array with the same data |
| --- | --- |
| >>> np.copy(a) | Create a copy of the array |
| >>> h = a.copy() | Create a deep copy of the array |

Sort an array

Sort the elements of an array's axis

## Subsetting, Slicing, Indexing

```python
>>> a[2]
```

## Array Manipulation

**Transposing Array**

```python
>>> i = np.transpose(b) >>> i.T
```

## Changing Array Shape

```python
>>> b.ravel()
```

```python
>>> g.reshape(3,-2)
```

## Adding/Removing Elements

```python
>>> h.resize((2,6))
```

```python
>>> np.append(h,g)
```

```python
>>> np.insert(a, 1, 5)
```

```python
>>> np.delete(a,[1])
```

## Combining Arrays

array([ 1, 2, 3, 10, 15, 20])

```python
>>> np.vstack((a,b))
```

```python
>>> np.r\_[e,f]
```

```python
>>> np.hstack((e,f)) array([[ 7., 7., 1., 0.], [ 7., 7., 0., 1.]])
```

```python
>>> np.column\_stack((a,d))
```

```python
>>> np.c\_[a,d]
```

## Splitting Arrays

```python
>>> np.hsplit(a,3)
```

[array([1]),array([2]),array([3])] >>> np.vsplit(c,2)

[array([[[ .5, 2. 1. ], , 4 . , 5. , 6. ]]]), array([[[ 3., 2 ., 3.] 4. 5 . , 6.]]])] Select the element at the 2nd index

Select the element at row 1 column 2 (equivalent to b[1][2])

Select items at index 0 and 1

Select items at rows 0 and 1 in column 1

Select all items at row 0 (equivalent to b[0:1, :])

Same as [1,:,:]

Reversed array a

Select elements from a less than 2

Select elements (1,0),(0,1),(1,2) and (0,0)

Select a subset of the matrix’s rows and columns

Permute array dimensions Permute array dimensions

Flatten the array

Reshape, but don’t change data

Return a new array with shape (2,6) Append items to an array Insert items in an array Delete items from an array

Concatenate arrays

Stack arrays vertically (row-wise)

Stack arrays vertically (row-wise) Stack arrays horizontally (column-wise)

Create stacked column-wise arrays

Create stacked column-wise arrays

Split the array horizontally at the 3rd index

Split the array vertically at the 2nd index

Pivot a level of column labels Pivot a level of index labels

Stacked

data2

# Python For Data Science Cheat Sheet

Pandas

Learn Python for Data Science **Interactively** at www.DataCamp.com

## Reshaping Data

## Pivot

```python
>>> df3= df2.pivot(index='Date', Spread rows into columns columns='Type', values='Value')
```

|  | Date | Type | Value |
| --- | --- | --- | --- |
| 0 | 2016-03-01 | a | 11.432 |
| 1 | 2016-03-02 | b | 13.031 |
| 2 | 2016-03-01 | c | 20.784 |
| 3 | 2016-03-03 | a | 99.906 |
| 4 | 2016-03-02 | a | 1.303 |
| 5 | 2016-03-03 | c | 20.784 |

| Type | a | b | c |
| --- | --- | --- | --- |
| Date |  |  |  |
| 2016-03-01 | 11.432 | NaN | 20.784 |
| 2016-03-02 | 1.303 | 13.031 | NaN |
| 2016-03-03 | 99.906 | NaN | 20.784 |

## Pivot Table

```python
>>> df4 = pd.pivot\_table(df2,
```

Spread rows into columns

values='Value',

columns='Type'])

## Stack / Unstack

```python
>>> stacked = df5.stack()
```

```python
>>> stacke<u>d.unstack()</u>
```

Unstacked

## Melt

```python
>>> pd.melt(df2,
```

id\_vars=["Date"], value\_vars=["Type", "Value"], value\_name="Observations")

|  | Date | Type | Value |
| --- | --- | --- | --- |
| 0 | 2016-03-01 | a | 11.432 |
| 1 | 2016-03-02 | b | 13.031 |
| 2 | 2016-03-01 | c | 20.784 |
| 3 | 2016-03-03 | a | 99.906 |
| 4 | 2016-03-02 | a | 1.303 |
| 5 | 2016-03-03 | c | 20.784 |

|  | Date | Variable | Observations |
| --- | --- | --- | --- |
| 0 | 2016-03-01 | Type | a |
| 1 | 2016-03-02 | Type | b |
| 2 | 2016-03-01 | Type | c |
| 3 | 2016-03-03 | Type | a |
| 4 | 2016-03-02 | Type | a |
| 5 | 2016-03-03 | Type | c |
| 6 | 2016-03-01 | Value | 11.432 |
| 7 | 2016-03-02 | Value | 13.031 |
| 8 | 2016-03-01 | Value | 20.784 |
| 9 | 2016-03-03 | Value | 99.906 |
| 10 | 2016-03-02 | Value | 1.303 |
| 11 | 2016-03-03 | Value | 20.784 |

## Iteration

| >>> df.iteritems( ) | (Column-index, Series) pairs |
| --- | --- |
| >>> df.iterrows( ) | (Row-index, Series) pairs |

## Advanced Indexing

## Selecting

## Also see NumPy Arrays

```python
>>> df3.loc[:,(df3>1).any()]
```

```python
>>> df3.loc[:,(df3>1).all()]
```

```python
>>> df3.loc[:,df3.isnull().any()]
```

Select cols with any vals >1 Select cols with vals > 1 Select cols with NaN Select cols without NaN

```python
>>> df[(df.Country.isin(df2.Type))]
```

```python
>>> df3.filter(items=”a”,”b”])
```

```python
>>> df.select(lambda x: not x%5) Where
```

Find same elements Filter on values Select specific elements

```python
>>> s.where(s > 0)
```

Query

Subset the data

```python
>>> df6.query('second > first')
```

Query DataFrame

## Setting/Resetting Index

| >>> df.set index('Country')_>>> df4 = df.reset index()_>>> df = df.rename(index=str, columns={"Country":"cntry", "Capital":"cptl", "Population":"ppltn"}) | Set the index Reset the index Rename DataFrame |
| --- | --- |

## Reindexing

<u>>>> s2 = s.reindex(['a','c','d','e','b'])</u>

## Forward Filling

## Backward Filling

<table><tr><td colspan="4">&gt;&gt;&gt; df.reindex(range(4), method=&#x27;ffill&#x27;)</td><td colspan="2">&gt;&gt;&gt; s3 = s.reindex(range(5), method=&#x27;bfill&#x27;)</td></tr><tr><td></td><td>Country</td><td>Capital</td><td>Population</td><td>0</td><td>3</td></tr><tr><td>0</td><td>Belgium</td><td>Brussels</td><td>11190846</td><td>1</td><td>3</td></tr><tr><td>1</td><td>India</td><td>New Delhi</td><td>1303171035</td><td>2</td><td>3</td></tr><tr><td>2</td><td>Brazil</td><td>Brasília</td><td>207847528</td><td>3</td><td>3</td></tr><tr><td>3</td><td>Brazil</td><td>Brasília</td><td>207847528</td><td>4</td><td>3</td></tr></table>

## MultiIndexing

```python
>>> arrays = [np.array([1,2,3]), np.array([5,4,3])] >>> df5 = pd.DataFrame(np.random.rand(3, 2), index=arrays)
```

```python
>>> tuples = list(zip(\*arrays))
```

```python
>>> index = pd.MultiIndex.from\_tuples(tuples,
```

names=['first', 'second'])

```python
>>> df6 = pd.DataFrame(np.random.rand(3, 2), index=index)
```

<u>>>> df2.set\_index(["Date", "Type"])</u>

## Duplicate Data

| >>> s3.unique( ) | Return unique values |
| --- | --- |
| >>> df2.duplicated('Type') | Check duplicates |
| >>> df2.drop_duplicates('Type', keep='last') | Drop duplicates |
| >>> df.index.duplicated( ) | Check index duplicates |

## Grouping Data

## Aggregation

```python
>>> df2.groupby(by=['Date','Type']).mean()
```

```python
>>> df4.groupby(level=0).sum()
```

```python
>>> df4.groupby(level=0).agg({'a':lambda x:sum(x)/len(x), 'b': np.sum})
```

## Transformation

```python
>>> customSum = lambda x: (x+x%2)
```

<u>>>> df4.groupby(level=0).transform(customSum)</u>

## Missing Data

| >>> df.dropna() | Drop NaN values |
| --- | --- |
| >>> df3.fillna(df3.mean()) | Fill NaN values with a predetermined value |
| >>> df2.replace("a", "f") | Replace values with others |

## Combining Data

## Merge

```python
>>> pd.merge(data1, data2, how='left', on='X1')
```

X1 X2 X3 a 11.432 20.784 b 1.303 NaN c 99.906 NaN

```python
>>> pd.merge(data1, data2, how='right', on='X1')
```

```python
>>> pd.merge(data1, data2, how='inner', on='X1')
```

```python
>>> pd.merge(data1, data2, how='outer', on='X1')
```

## Join

```python
>>> data1.join(data2, how='right')
```

## Concatenate

Vertical

```python
>>> s.append(s2)
```

Horizontal/Vertical

```python
>>> pd.concat([s,s2],axis=1, keys=['One','Two']) <u>>>> pd.concat([data1, data2], axis=1, join='inner')</u>
```

## Dates

```python
>>> df2['Date']= pd.to\_datetime(df2['Date']) >>> df2['Date']= pd.date\_range('2000-1-1', periods=6, freq='M')
```

```python
>>> dates = [datetime(2012,5,1), datetime(2012,5,2)]
```

```python
>>> index = pd.DatetimeIndex(dates)
```

<u>>>> index = pd.date\_range(datetime(2012,2,1), end, freq='BM')</u>

## Visualization

## Also see Matplotlib

## >>> import matplotlib.pyplot as plt

```python
>>> s.plot() >>> plt.show()
```

```python
>>> df2.plot() >>> plt.show()
```

```txt
>>> plt.plot(x, x, x, x**2, x, x**3)
>>> ax.plot(x, y, alpha = 0.4)
>>> ax.plot(x, y, c='k')
>>> fig.colorbar(im, orientation='horizontal')
>>> im = ax.imshow(img,
                             cmap='seismic')
```

# Python For Data Science Cheat Sheet

Matplotlib

Learn Python **Interactively** at www.DataCamp.com

## Matplotlib

**Matplotlib** is a Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments acrossplatforms. matplotlib

## Prepare The Data

## Also see Lists & NumPy

## 1D Data

```python
>>> import numpy as np >>> x = np.linspace(0, 10, 100) >>> y = np.cos(x) >>> z = np.sin(x)
```

## 2D Data or Images

```python
>>> data = 2 * np.random.random((10, 10))
>>> data2 = 3 * np.random.random((10, 10))
>>> Y, X = np.mgrid[-3:3:100j, -3:3:100j]
>>> U = -1 - X**2 + Y
>>> V = 1 + X - Y**2
>>> from matplotlib.cbook import get_sample_data
>>> img = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))
```

## Create Plot

<u>>>> import matplotlib.pyplot as plt</u>

## Figure

```python
>>> fig = plt.figure()
```

<u>>>> fig2 = plt.figure(figsize=plt.figaspect(2.0))</u>

## Axes

All plotting is done with respect to an Axes. In most cases, a subplot will fit your needs. A subplot is an axes on a grid system.

```python
>>> fig.add\_axes() >>> ax1 = fig.add\_subplot(221) # row-col-num >>> ax3 = fig.add\_subplot(212) >>> fig3, axes = plt.subplots(nrows=2,ncols=2) >>> fig4, axes2 = plt.subplots(ncols=3)
```

## Plotting Routines

## 1D Data

```python
>>> fig, ax = plt.subplots() >>> lines = ax.plot(x,y) >>> ax.scatter(x,y) >>> axes[0,0].bar([1,2,3],[3,4,5]) >>> axes[1,0].barh([0.5,1,2.5],[0,1,2]) >>> axes[1,1].axhline(0.45) >>> axes[0,1].axvline(0.65) >>> ax.fill(x,y,color='blue') >>> ax.fill\_between(x,y,color='yellow')
```

## 2D Data or Images

```python
>>> fig, ax = plt.subplots() >>> im = ax.imshow(img, cmap='gist\_earth', interpolation='nearest', vmin=-2, vmax=2)
```

## Plot Anatomy & Workflow

## Plot Anatomy

## Customize Plot

## Workflow

## Colors, Color Bars & Color Maps

## Markers

```python
>>> fig, ax = plt.subplots() >>> ax.scatter(x,y,marker=".") >>> ax.plot(x,y,marker="o")
```

## Linestyles

```txt
>>> plt.plot(x,y,linewidth=4.0)
>>> plt.plot(x,y,ls='solid')
>>> plt.plot(x,y,ls='---)
>>> plt.plot(x,y,'--',x**2,y**2,'-.')
>>> plt.setp(lines,color='r',linewidth=4.0)
```

## Text & Annotations

```python
>>> ax.text(1,
            -2.1,
            'Example Graph',
            style='italic')
>>> ax.annotate("Sine",
            xy=(8, 0),
            xycoords='data',
            xytext=(10.5, 0),
            textcoords='data',
            arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc3"),)
python
>>> import matplotlib.pyplot as plt
>>> x = [1,2,3,4]
>>> y = [10,20,25,30]
>>> fig = plt.figure()
>>> ax = fig.add_subplot(111)
>>> ax.plot(x, y, color='lightblue', linewidth=3)
>>> ax.scatter([2,4,6],
                          [5,15,25],
                          color='darkgreen',
                          marker='^')
>>> ax.set_xlim(1, 6.5)
>>> plt.savefig('foo.png')
>>> plt.show()
```

## Mathtext

```python
Limits, Legends & Layouts
Limits & Autoscaling
>>> ax.margins(x=0.0,y=0.1)
>>> ax.axis('equal')
>>> ax.set(xlim=[0,10.5],ylim=[-1.5,1.5])
>>> ax.set_xlim(0,10.5)
Legends
>>> ax.set(title='An Example Axes',
            ylabel='Y-Axis',
            xlabel='X-Axis')
>>> ax.legend(loc='best')
Ticks
>>> ax.xaxis.set(ticks=range(1,5),
            ticklabels=[3,100,-12,"foo"])
>>> ax.tick_params(axis='y',
            direction='inout',
            length=10)
Subplot Spacing
>>> fig3.subplots_adjust(wspace=0.5,
              hspace=0.3,
              left=0.125,
              right=0.9,
              top=0.9,
              bottom=0.1)
>>> fig.tight_layout()
Axis Spines
>>> ax1.spines['top'].set_visible(False)
>>> ax1.spines['bottom'].set_position(('outward',10))
```

Draw points with lines or markers connecting them Draw unconnected points, scaled or colored Plot vertical rectangles (constant width) Plot horiontal rectangles (constant height) Draw a horizontal line across axes Draw a vertical line across axes Draw filled polygons Fill between y-values and 0

Colormapped or RGB arrays

## Vector Fields

| >>> axes[0,1].arrow(0,0,0.5,0.5) | Add an arrow to the axes |
| --- | --- |
| >>> axes[1,1].quiver(y,z) | Plot a 2D field of arrows |
| >>> axes[0,1].streamplot(X,Y,U,V) | Plot a 2D field of arrows |

## Data Distributions

```python
>>> ax1.hist(y)
```

Make a violin plot

```python
>>> axes2[0].pcolor(data2) >>> axes2[0].pcolormesh(data) >>> CS = plt.contour(Y,X,U) >>> axes2[2].contourf(data1) >>> axes2[2]= ax.clabel(CS)
```

Pseudocolor plot of 2D array Pseudocolor plot of 2D array Plot contours Plot filled contours Label a contour plot

## Save Plot

**Save figures**

```python
>>> plt.savefig('foo.png')
```

**Save transparent figures**

```python
>>> plt.savefig('foo.png', transparent=True)
```

## Show Plot

```python
>>> plt.show()
```

## Close & Clear

```python
>>> plt.cla() >>> plt.clf() >>> plt.close()
```

Clear an axis Clear the entire figure Close a window

## DataCamp

**Learn Python for Data Science Interactively**

```erlang
>>> p4 = figure(plot_width = 100,
python
>>> p4.circle('mpg', 'cyl', source=cds_df)
```

```python
>>> import numpy as np
```

glyphs

Bokeh

Learn Bokeh **Interactively** at www.DataCamp.com,taught by Bryan Van de Ven, core contributor

## Plotting With Bokeh

The Python interactive visualization library **Bokeh** enables high-performance visual presentation of large datasets in modern web browsers.

Bokeh’s mid-level general purpose bokeh.plotting interface is centered around two main components: data and glyphs.

data

plot

The basic steps to creating plots with the bokeh.plotting interface are:

1. Prepare some data:

Python lists, NumPy arrays, Pandas DataFrames and other sequences of values

2. Create a new plot

3. Add renderers for your data, with visual customizations

4. Specify where to generate the output

5. Show or save the results

```python
>>> from bokeh.plotting import figure
>>> from bokeh.io import output_file, show
>>> x = [1, 2, 3, 4, 5]
>>> y = [6, 7, 2, 4, 5]
>>> p = figure(title="simple line example",
                   x_axis_label='x',
                   y_axis_label='y')
>>> p.line(x, y, legend="Temp.", line_width=2)
>>> output_file("lines.html")
>>> show(p)
```

## Data

## Also see Lists, NumPy & Pandas

Under the hood, your data is converted to Column Data Sources. You can also do this manually:

```python
>>> import pandas as pd
```

```python
>>> df = pd.DataFrame(np.array([[33.9,4,65, 'US'],
```

columns=['mpg','cyl', 'hp', 'origin'], index=['Toyota', 'Fiat', 'Volvo'])

```python
>>> from bokeh.models import ColumnDataSource
```

<u>>>> cds\_df = ColumnDataSource(df)</u>

## Plotting

from bokeh.plotting import figure

p1 = figure(plot\_width=300, tools='pan,box\_zoom')

p2 = figure(plot\_width=300, plot\_height=300,

```python
>>> p3 = figure()
```

x\_range=(0, 8), y\_range=(0, 8))

## Glyphs

## Scatter Markers

```python
>>> p1.circle(np.array([1,2,3]), np.array([3,2,1]), fill\_color='white')
```

```python
>>> p2.square(np.array([1.5,3.5,5.5]), [1,4,3], color='blue', size=1)
```

**Line Glyphs**

```python
>>> p1.line([1,2,3,4], [3,4,5,6], line\_width=2)
```

```python
>>> p2.multi\_line(pd.DataFrame([[1,2,3],[5,6,7]]),
```

pd.DataFrame([[3,4,5],[3,2,1]]),

## Customized Glyphs

## Also see Data

## Selection and Non-Selection Glyphs

```python
>>> p = figure(tools='box\_select')
```

```python
>>> p.circle('mpg', 'cyl', source=cds\_df,
```

nonselection\_alpha=0.1)

**Hover Glyphs**

```python
>>> from bokeh.models import HoverTool
```

```python
>>> hover = HoverTool(tooltips=None, mode='vline')
```

```python
>>> p3.add\_tools(hover)
```

## Colormapping

```python
>>> from bokeh.models import CategoricalColorMapper
```

```python
factors=['US', 'Asia', 'Europe'],
palette=['blue', 'red', 'green'])
```

transform=color\_mapper),

legend='Origin')

## Legend Location

**Inside Plot Area**

```python
>>> p.legend.location = 'bottom\_left'
```

**Outside Plot Area**

```python
>>> from bokeh.models import Legend
```

```python
>>> r1 = p2.asterisk(np.array([1,2,3]), np.array([3,2,1])
```

```python
>>> r2 = p2.line([1,2,3,4], [3,4,5,6])
```

```python
>>> legend = Legend(items=[("One" ,[p1, r1]),("Two",[r2])], location=(0, -30))
```

```python
>>> p.add\_layout(legend, 'right')
```

## Legend Orientation

```python
>>> p.legend.orientation = "horizontal"
```

```python
>>> p.legend.orientation = "vertical"
```

## Legend Background & Border

```python
>>> p.legend.border\_line\_color = "navy"
```

<u>>>> p.legend.background\_fill\_color = "white"</u>

## Rows & Columns Layout

**Rows**

```python
>>> from bokeh.layouts import row
```

```python
>>> layout = row(p1,p2,p3)
```

**Columns**

```python
>>> from bokeh.layouts import columns
```

```python
>>> layout = column(p1,p2,p3)
```

**Nesting Rows & Columns**

```python
>>>layout = row(column(p1,p2), p3)
```

## Grid Layout

```python
>>> from bokeh.layouts import gridplot
```

```python
>>> row1 = [p1,p2]
```

```python
>>> row2 = [p3]
```

```python
>>> layout = gridplot([[p1,p2],[p3]])
```

## Tabbed Layout

```python
>>> from bokeh.models.widgets import Panel, Tabs
```

```python
>>> tab1 = Panel(child=p1, title="tab1")
```

```python
>>> tab2 = Panel(child=p2, title="tab2")
```

```python
>>> layout = Tabs(tabs=[tab1, tab2])
```

## Linked Plots

**Linked Axes**

```python
>>> p2.x\_range = p1.x\_range
```

```python
>>> p2.y\_range = p1.y\_range
```

**Linked Brushing**

tools='box\_select,lasso\_select')

```erlang
>>> p5 = figure(plot_width = 200,
```

```python
>>> p5.circle('mpg', 'hp', source=cds\_df)
```

```python
>>> layout = row(p4,p5)
```

## Output & Export

## Notebook

```python
>>> from bokeh.io import output\_notebook, show >>> output\_notebook()
```

## HTML

**Standalone HTML**

```python
>>> from bokeh.embed import file\_html
```

```python
>>> from bokeh.resources import CDN
```

<u>>>> html = file\_html(p, CDN, "my\_plot")</u>

```python
>>> from bokeh.io import output\_file, show <u>>>> output\_file('my\_bar\_chart.html', mode='cdn')</u>
```

**Components**

```python
>>> from bokeh.embed import components
```

<u>>>> script, div = components(p)</u>

## PNG

<u>>>> export\_png(p, filename="plot.png")</u>

## SVG

```python
>>> from bokeh.io import export\_svgs
```

```python
>>> p.output\_backend = "svg"
```

<u>>>> export\_svgs(p, filename="plot.svg")</u>

## Show or Save Your Plots

```python
>>> show(p1) >>> save(p1)
```

```python
>>> show(layout)
```

```python
>>> save(layout)
```

## DataCamp

**Learn Python for Data Science Interactively**

```txt
>>> sns.pointplot(x="class",
              y="survived",
              hue="sex",
              data=titanic,
              palette={"male":"g",
                   "female":"m"},
              markers=["^","o"],
              linestyles=["-","--"])
```

| >>> sns.set( )>>> sns.set_style("whitegrid")>>> sns.set_style("ticks", {"xtick.major.size":8, "ytick.major.size":8})>>> sns.axes_style("whitegrid") | (Re)set the seaborn defaultSet the matplotlib parametersSet the matplotlib parametersReturn a dict of params or use withwith to temporarily set the style |
| --- | --- |

Seaborn

Learn Data Science **Interactively** at www.DataCamp.com

## Axis Grids

## Statistical Data Visualization With Seaborn

The Python visualization library **Seaborn** is based on matplotlib and provides a high-level interface for drawing attractive statistical graphics.

Make use of the following aliases to import the libraries:

```python
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
```

The basic steps to creating plots with Seaborn are:

1. Prepare some data

2. Control figure aesthetics

3. Plot with Seaborn

4. Further customize your plot

```python
>>> import matplotlib.pyplot as plt >>> import seaborn as sns >>> tips = sns.load\_dataset("tips") Step 1 >>> sns.set\_style("whitegrid") Step 2 >>> g = sns.lmplot(x="tip", Step 3 y="total\_bill", data=tips, aspect=2) >>> g = (g.set\_axis\_labels("Tip","Total bill(USD)"). set(xlim=(0,10),ylim=(0,100))) Step 4 >>> plt.title("title") >>> plt.show(g) Step 5
```

## Data

**Also see Lists, NumPy & Pandas**

```python
>>> import pandas as pd >>> import numpy as np >>> uniform\_data = np.random.rand(10, 12) >>> data = pd.DataFrame({'x':np.arange(1,101), 'y':np.random.normal(0,4,100)})
```

## Seaborn also offers built-in data sets:

```python
>>> titanic = sns.load\_dataset("titanic")
```

```python
>>> iris = sns.load\_dataset("iris")
```

## Figure Aesthetics

<u>>>> f, ax = plt.subplots(figsize=(5,6)) Create a figure and one subplot</u>

## Seaborn styles

## Categorical Plots

**Scatterplot**

```python
>>> sns.stripplot(x="species", y="petal\_length", data=iris)
```

```python
>>> sns.swarmplot(x="species", y="petal\_length", data=iris)
```

**Bar Chart**

```python
>>> sns.barplot(x="sex", y="survived", hue="class", data=titanic)
```

**Count Plot**

Subplot grid for plotting conditional relationships

Draw a categorical plot onto a Facetgrid

Plot data and regression model fits across a FacetGrid

Scatterplot with one categorical variable

**Point Plot**

## Show point estimates and confidence intervals with scatterplot glyphs

## Categorical scatterplot with non-overlapping points

**Boxplot**

```python
>>> sns.boxplot(data=iris,orient="h") **Violinplot**
```

```python
>>> sns.boxplot(x="alive", y="age", hue="adult\_male", data=titanic)
```

Subplot grid for plotting pairwise relationships Plot pairwise bivariate distributions Grid for bivariate plot with marginal univariate plots

Show count of observations

Plot bivariate distribution

```python
>>> sns.violinplot(x="age", y="sex", hue="survived", data=titanic)
```

## Regression Plots

```python
>>> plot = sns.distplot(data.y, kde=False, color="b")
```

```python
>>> sns.regplot(x="sepal\_width", y="sepal\_length", data=iris, ax=ax)
```

Plot univariate distribution

## Boxplot

## Distribution Plots

## Show point estimates and confidence intervals as rectangular bars

Plot data and a linear regression model fit

Heatmap

Boxplot with wide-form data

Violin plot

**Color Palette**

## Matrix Plots

```python
>>> sns.heatmap(uniform\_data,vmin=0,vmax=1)
```

## Also see Matplotlib

## Further Customizations

## Context Functions

| >>> sns.set_context("talk") | Set context to "talk" |
| --- | --- |
| >>> sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth":2.5}) | Set context to "notebook", scale font elements and override param mapping |

## Axisgrid Objects

## Also see Matplotlib

| >>> sns.set_palette("hus1",3) | Define the color palette |
| --- | --- |
| >>> sns.color_palette("hus1") | Use with with to temporarily set palette |
| >>> flatui = ["#9b59b6","#3498db","#95a5a6","#e74c3c","#34495e","#2ecc71"] |  |
| >>> sns.set_palette(flatui) | Set your own color palette |

| >>> g.despine(left=True) >>> g.set_ylabels("Survived") >>> g.set_xticklabels(rotation=45) >>> g.set_axis_labels("Survived", "Sex") >>> h.set(xlim=(0,5), ylim=(0,5),xticks=[0,2.5,5],yticks=[0,2.5,5]) | Remove left spine Set the labels of the y-axis Set the tick labels for x Set the axis labels S x-eatn tdhe y- liamxiist and ticks of the |
| --- | --- |

## Plot

| >>> plt.title("A Title") | Add plot title |
| --- | --- |
| >>> plt.ylabel("Survived") | Adjust the label of the y-axis |
| >>> plt.xlabel("Sex") | Adjust the label of the x-axis |
| >>> plt.ylim(0,100) | Adjust the limits of the y-axis |
| >>> plt.xlim(0,10) | Adjust the limits of the x-axis |
| >>> plt.setp(ax,yticks=[0,5]) | Adjust a plot property |
| >>> plt.tight_layout() | Adjust subplot params |

## Show or Save Plot

```python
>>> plt.show() >>> plt.savefig("foo.png") >>> plt.savefig("foo.png", transparent=True)
```

## Close & Clear

```python
>>> plt.cla()
```

```python
>>> plt.clf()
```

```python
>>> plt.close()
```

## DataCamp

**Learn Python for Data Science Interactively**

## Also see Matplotlib

Show the plot Save the plot as a figure Save transparent figure

## Also see Matplotlib

Clear an axis

Clear an entire figure

Close a window

## Python For Data Science Cheat Sheet

Importing Data

Learn Python for data science **Interactively** at www.DataCamp.com

## Importing Data in Python

Most of the time, you’ll use either **NumPy** or **pandas** to import

your data:

```python
>>> import numpy as np
```

```python
>>> import pandas as pd
```

## Help

```python
>>> np.info(np.ndarray.dtype)
```

```python
>>> help(pd.read\_csv)
```

## Text Files

## Plain Text Files

```python
>>> filename = 'huck_finn.txt'
>>> file = open(filename, mode='r')
>>> text = file.read()
>>> print(file.closed)
>>> file.close()
>>> print(text)
```

Open the file for reading Read a file’s contents Check whether file is closed Close file

## Using the context manager with

print(file.readline())

Read a single line

print(file.readline())

## Table Data: Flat Files

## Importing Flat Files with numpy

**Files with one data type**

```python
>>> filename = 'mnist.txt'
>>> data = np.loadtxt(filename,
                             delimiter=',',
                             skiprows=2,
                             usecols=[0,2],
                             dtype=str)
```

## Files with mixed data types

```python
>>> filename = 'titanic.csv
```

names=True,

Look for column header

<u>>>> data\_array = np.recfromcsv(filename)</u>

The default dtype of the np.recfromcsv() function is None.

## Importing Flat Files with pandas

```python
>>> filename = 'winequality-red.csv'
>>> data = pd.read_csv(filename,
                      nrows=5,
                      header=None,
                      sep='\t',
                      comment='#',
                      na_values=[""])
Number of rows of file to read
Row number to use as col names
Delimiter to use
Character to split comments
String to recognize as NA/NaN
```

## Excel Spreadsheets

```python
>>> file = 'urbanpop.xlsx'
>>> data = pd.ExcelFile(file)
>>> df_sheet2 = data.parse('1960-1966',
                                      skiprows=[0],
                                      names=['Country',
                                      'AAM: War(2002)'])
>>> df_sheet1 = data.parse(0,
                                      parse_cols=[0],
                                      skiprows=[0],
                                      names=['Country'])
```

## To access the sheet names, use the sheet\_names attribute:

```python
>>> data.sheet\_names
```

## SAS Files

```python
>>> from sas7bdat import SAS7BDAT >>> with SAS7BDAT('urbanpop.sas7bdat') as file: df\_sas = file.to\_data\_frame()
```

## Stata Files

<u>>>> data = pd.read\_stata('urbanpop.dta')</u>

## Relational Databases

```python
>>> from sqlalchemy import create\_engine <u>>>> engine = create\_engine('sqlite://Northwind.sqlite')</u>
```

Use the table\_names() method to fetch a list of table names:

<u>>>> table\_names = engine.table\_names()</u>

## Querying Relational Databases

```txt
>>> con = engine.connect()
>>> rs = con.execute("SELECT * FROM Orders")
>>> df = pd.DataFrame(rs.fetchall())
>>> df.columns = rs.keys()
>>> con.close()
```

## Using the context manager with

```python
>>> with engine.connect() as con: rs = con.execute("SELECT OrderID FROM Orders") df = pd.DataFrame(rs.fetchmany(size=5)) df.columns = rs.keys()
```

## Querying relational databases with pandas

<u>>>> df = pd.read\_sql\_query("SELECT \* FROM Orders", engine)</u>

## Exploring Your Data

## NumPy Arrays

```python
>>> data\_array.dtype
```

```python
>>> data\_array.shape
```

```python
>>> len(data\_array)
```

Data type of array elements Array dimensions Length of array

## pandas DataFrames

| >>> df.head() | Return first DataFrame rows |
| --- | --- |
| >>> df.tail() | Return last DataFrame rows |
| >>> df.index | Describe index |
| >>> df.columns | Describe DataFrame columns |
| >>> df.info() | Info on DataFrame |
| >>> data_array = data.values | Convert a DataFrame to an a NumPy array |

## Pickled Files

```python
>>> import pickle
```

```python
>>> with open('pickled\_fruit.pkl', 'rb') as file: pickled\_data = pickle.load(file)
```

## HDF5 Files

```python
>>> import h5py
```

```python
>>> filename = 'H-H1\_LOSC\_4\_v1-815411200-4096.hdf5'
```

<u>>>> data = h5py.File(filename, 'r')</u>

## Matlab Files

```python
>>> import scipy.io
```

```python
>>> filename = 'workspace.mat'
```

<u>>>> mat = scipy.io.loadmat(filename)</u>

## Exploring Dictionaries

## Accessing Elements with Functions

```python
>>> print(mat.keys())
```

```python
>>> for key in data.keys(): print(key)
```

meta

Print dictionary keys Print dictionary keys

quality

strain

```python
>>> pickled\_data.values()
```

```python
>>> print(mat.items())
```

Return dictionary values

Returns items in list format of (key, value) tuple pairs

## Accessing Data Items with Keys

```python
>>> for key in data ['meta'].keys() print(key)
```

Description

Explore the HDF5 structure

DescriptionURL

Detector

Duration

GPSstart

Observatory

Type

UTCstart

<u>>>> print(data['meta']['Description'].value) Retrieve the value for a key</u>

## ~~Navigating Your FileSystem~~

## Magic Commands

| !ls | List directory contents of files and directories |
| --- | --- |
| %cd .. | Change current working directory |
| %pwd | Return the current working directory path |

## os Library

```python
>>> import os
```

```python
>>> path = "/usr/tmp"
```

```python
>>> wd = os.getcwd()
```

```python
>>> os.listdir(wd)
```

```python
>>> os.chdir(path)
```

```python
>>> os.rename("test1.txt",
```

Store the name of current directory in a string Output contents of the directory in a list Change current working directory Rename a file

```python
>>> os.remove("test1.txt") Delete an existing file
```

```python
>>> os.mkdir("newdir")
```

Create a new directory

## DataCamp

**Learn R for Data Science Interactively**

# Python For Data Science Cheat Sheet

Jupyter Notebook

Learn More Python for Data Science Interactively at <u>www.DataCamp.com</u>

## Saving/Loading Notebooks

Create new notebook

Make a copy of the current notebook

Save current notebook and record checkpoint

Preview of the printed notebook

Close notebook & stop running any scripts

Open an existing notebook

Rename notebook

Revert notebook to a previous checkpoint

\- Python

Download notebook as - IPython notebook

\- HTML

\- Markdown

\- reST

\- LaTeX

\- PDF

## Writing Code And Text

Code and text are encapsulated by 3 basic cell types: markdown cells, code cells, and raw NBConvert cells.

## Edit Cells

Cut currently selected cells to clipboard

Paste cells from clipboard above current cell

Paste cells from clipboard on top of current cel

Revert “Delete Cells” invocation

Merge current cell with the one above

Move current cell up

Adjust metadata underlying the current notebook

Remove cell attachments

Paste attachments of current cell

## Insert Cells

Add new cell above the current one

Copy cells from clipboard to current cursor position

Paste cells from clipboard below current cell

Delete current cells

Split up a cell from current cursor position

Merge current cell with the one below

Move current cell down

Find and replace in selected cells

Copy attachments of current cell

Insert image in selected cells

Add new cell below the current one

## ~~Working with Different Programming Languages~~

Kernels provide computation and communication with front-end interfaces like the notebooks. There are three main kernels:

IP[y]: IPython

Restart kernel

Installing Jupyter Notebook will automatically install the IPython kernel.

Restart kernel & run all cells e.

Restart kernel & run all cells

## Command Mode:

## jupyter MyJupyterNotebook Last Checkpoint: a few seconds ago (unsaved changes)

**Edit Mode:**

Kernel

Run selected cell(s)

## Executing Cells

IJ[] IJulia

Run current cells down and create a new one above

Code

Interrupt kernel

Interrupt kernel & clear all output

Run all cells above the current cell

Connect back to a remote notebook

Change the cell type of current cell

Run other installed kernels

toggle, toggle scrolling and clear all output

**11**

## View Cells

Toggle display of Jupyter logo and filename

Toggle line numbers in cells

**12**

Run current cells down and create a new one below

Run all cells Run all cells below the current cell

toggle, toggle scrolling and clear current outputs

• •Toggle Line Numbers Cell Toolbar

Toggle display of toolbar Toggle display of cell action icons: - None - Edit metadata Raw cell format - Slideshow - Attachments - Tags

## Widgets

Notebook widgets provide the ability to visualize and control changes in your data, often as a control like a slider, textbox, etc.

You can use them to build interactive GUIs for your notebooks or to synchronize stateful and stateless information between Python and JavaScript.

Download serialized state of all widget models in use

Widgets

Save Notebook with Widgets •

•• • Download Widget State

Embed Widgets • . .

Save notebook with interactive widgets

Embed current widgets

Trusted

**13 14**

1. Save and checkpoint

2. Insert cell below

3. Cut cell

4. Copy cell(s)

9. Interrupt kernel

**10**. Restart kernel

5. Paste cell(s) below

6. Move cell up

**11**. Display characteristics

7. Move cell down

8. Run current cell

**12**. Open command palette

**13**. Current kernel

**14**. Kernel status

**15**. Log out from notebook server

## Asking For Help

Walk through a UI tour

Edit the built-in keyboard shortcuts

List of built-in keyboard shortcuts

Description of markdown available in notebook

Notebook help topics

Python help topics

Matplotlib help topics

Information on unofficial Jupyter Notebook extensions

Pandas help topics

IPython help topics

About Jupyter Notebook

# Python For Data Science Cheat Sheet SciPy - Linear Algebra

Learn More Python for Data Science Interactively at www.datacamp.com

## Linear Algebra

You’ll use the linalg and sparse modules. Note that scipy.linalg contains and expands on numpy.linalg.

## SciPy

The **SciPy** library is one of the core packages for scientific computing that provides mathematical algorithms and convenience functions built on the NumPy extension of Python.

## Interacting With NumPy

```python
>>> import numpy as np
```

```python
>>> a = np.array([1,2,3])
```

## Also see NumPy

```python
>>> b = np.array([(1+5j,2j,3j), (4j,5j,6j)])
```

```python
>>> c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]])
```

## Index Tricks

```python
>>> np.mgrid[0:5,0:5] >>> np.ogrid[0:2,0:2] >>> np.r\_[[3,[0]\*5,-1:1:10j] >>> np.c\_[b,c]
```

## Shape Manipulation

```python
>>> np.transpose(b) >>> b.flatten() >>> np.hstack((b,c)) >>> np.vstack((a,b)) >>> np.hsplit(c,2) >>> np.vpslit(d,2)
```

Create a dense meshgrid Create an open meshgrid Stack arrays vertically (row-wise) Create stacked column-wise arrays

## Polynomials

Permute array dimensions Flatten the array

```python
>>> from numpy import poly1d
```

Stack arrays horizontally (column-wise) Stack arrays vertically (row-wise) Split the array horizontally at the 2nd index Split the array vertically at the 2nd index

```python
>>> p = poly1d([3,4,5])
```

## Vectorizing Functions

Create a polynomial object

```python
>>> def myfunc(a): if a < 0: return a\*2 else: return a/2
```

```python
>>> np.vectorize(myfunc)
```

## Type Handling

Vectorize functions

| >>> np.real(c) >>> np.imag(c) >>> np.real_if_close(c,tol=1000) >>> np.cast['f'](np.pi) | Return the real part of the array elements Return the imaginary part of the array elements Return a real array if complex parts close to 0 Cast object to a data type |
| --- | --- |

## Other Useful Functions

| >>> np.angle(b,deg=True) >>> g = np.linspace(0,np.pi,num=5) >>> g [3:] += np.pi >>> np.unwrap(g) >>> np.logspace(0,10,3) >>> np.select([c&lt;4],[c*2]) >>> misc.factorial(a) >>> misc.comb(10,3,exact=True) >>> misc.central_diff_weights(3) >>> misc.derivative(myfunc,1.0) | Return the angle of the complex argument Create an array of evenly spaced values (number of samples) Unwrap Create an array of evenly spaced values (log scale) Return values from a list of arrays depending on conditions Factorial Combine N things taken at k time Weights for Np-point central derivative Find the n-th derivative of a function at a point |
| --- | --- |

<u>>>> from scipy import linalg, sparse</u>

## Creating Matrices

```python
>>> A = np.matrix(np.random.random((2,2)))
```

```python
>>> B = np.asmatrix(b)
```

```python
>>> C = np.mat(np.random.random((10,5)))
```

```python
>>> D = np.mat([[3,4], [5,6]])
```

## Basic Matrix Routines

**Inverse**

```python
>>> A.I >>> linalg.inv(A) >>> A.T >>> A.H >>> np.trace(A)
```

## Norm

```python
>>> linalg.norm(A) >>> linalg.norm(A,1) >>> linalg.norm(A,np.inf) **Rank** >>> np.linalg.matrix\_rank(C) **Determinant** >>> linalg.det(A) **Solving linear problems** >>> linalg.solve(A,b) >>> E = np.mat(a).T >>> linalg.lstsq(D,E)
```

## Generalized inverse

```python
>>> linalg.pinv(C)
```

```python
>>> linalg.pinv2(C)
```

## Creating Sparse Matrices

```python
>>> F = np.eye(3, k=1) >>> G = np.mat(np.identity(2) >>> C[C > 0.5] = 0 >>> H = sparse.csr\_matrix(C) >>> I = sparse.csc\_matrix(D) >>> J = sparse.dok\_matrix(A) >>> E.todense() >>> sparse.isspmatrix\_csc(A)
```

## Sparse Matrix Routines

Inverse Inverse Tranpose matrix Conjugate transposition Trace

Frobenius norm L1 norm (max column sum) L inf norm (max row sum)

Matrix rank

**Inverse**

Determinant

Solver for dense matrices Solver for dense matrices Least-squares solution to linear matrix equation

Compute the pseudo-inverse of a matrix (least-squares solver) Compute the pseudo-inverse of a matrix (SVD)

Compressed Sparse Row matrix Compressed Sparse Column matrix Dictionary Of Keys matrix Sparse matrix to full matrix Identify sparse matrix

| >>> sparse.linalg.inv(I) | Inverse |
| --- | --- |
| Norm |  |
| >>> sparse.linalg.norm(I) | Norm |
| Solving linear problems |  |
| >>> sparse.linalg.spsolve(H,I) | Solver for sparse matrices |

Create a 2X2 identity matrix Create a 2x2 identity matrix

## Sparse Matrix Functions

```python
>>> sparse.linalg.expm(I)
```

## Asking For Help

```python
>>> help(scipy.linalg.diagsvd) >>> np.info(np.matrix)
```

Sparse matrix exponential

## Matrix Functions

## Addition

```python
>>> np.add(A,D)
```

**Subtraction**

```python
>>> np.subtract(A,D)
```

```python
>>> np.divide(A,D)
```

## Multiplication

```python
>>> np.multiply(D,A) >>> np.dot(A,D) >>> np.vdot(A,D) >>> np.inner(A,D) >>> np.outer(A,D) >>> np.tensordot(A,D) >>> np.kron(A,D)
```

**Exponential Functions** >>> linalg.expm(A) >>> linalg.expm2(A) >>> linalg.expm3(D)

## Logarithm Function

```python
>>> linalg.logm(A) **Trigonometric Tunctions** >>> linalg.sinm(D) >>> linalg.cosm(D) >>> linalg.tanm(A)
```

**Hyperbolic Trigonometric Functions** >>> linalg.sinhm(D) >>> linalg.coshm(D) >>> linalg.tanhm(A)

**Matrix Sign Function** >>> np.sigm(A) **Matrix Square Root** >>> linalg.sqrtm(A) **Arbitrary Functions** >>> linalg.funm(A, lambda x: x\*x)

## Decompositions

**Eigenvalues and Eigenvectors** >>> la, v = linalg.eig(A)

```python
>>> l1, l2 = la >>> v[:,0] >>> v[:,1] >>> linalg.eigvals(A)
```

## Singular Value Decomposition

```python
>>> U,s,Vh = linalg.svd(B)
```

```python
>>> M,N = B.shape
```

```python
>>> Sig = linalg.diagsvd(s,M,N)
```

## LU Decomposition

```python
>>> P,L,U = linalg.lu(C)
```

## Sparse Matrix Decompositions

```python
>>> la, v = sparse.linalg.eigs(F,1) >>> sparse.linalg.svds(H, 2)
```

## DataCamp

**Learn Python for Data Science Interactively**

Addition

Subtraction

Division

Multiplication Dot product Vector dot product Inner product Outer product Tensor dot product Kronecker product

## Matrix exponential

Matrix exponential (Taylor Series) Matrix exponential (eigenvalue decomposition)

Matrix logarithm

Matrix sine Matrix cosine Matrix tangent

Hypberbolic matrix sine Hyperbolic matrix cosine Hyperbolic matrix tangent

Matrix sign function

Matrix square root

Evaluate matrix function

Solve ordinary or generalized eigenvalue problem for square matrix Unpack eigenvalues First eigenvector Second eigenvector Unpack eigenvalues

Singular Value Decomposition (SVD)

Construct sigma matrix in SVD

LU Decomposition

Eigenvalues and eigenvectors SVD

## Python For Data Science Cheat Sheet

Scikit-Learn

Learn Python for data science **Interactively** at www.DataCamp.com

## Scikit-learn

**Scikit-learn** is an open source Python library that implements a range of machine learning, preprocessing, cross-validation and visualization algorithms using a unified interface.

## A Basic Example

```python
>>> from sklearn import neighbors, datasets, preprocessing >>> from sklearn.model\_selection import train\_test\_split >>> from sklearn.metrics import accuracy\_score >>> iris = datasets.load\_iris() >>> X, y = iris.data[:, :2], iris.target >>> X\_train, X\_test, y\_train, y\_test = train\_test\_split(X, y, random\_state=33) >>> scaler = preprocessing.StandardScaler().fit(X\_train) >>> X\_train = scaler.transform(X\_train) >>> X\_test = scaler.transform(X\_test) >>> knn = neighbors.KNeighborsClassifier(n\_neighbors=5) >>> knn.fit(X\_train, y\_train) >>> y\_pred = knn.predict(X\_test) >>> accuracy\_score(y\_test, y\_pred)
```

## Loading The Data

## Also see NumPy & Pandas

**Your data needs to be numeric and stored as NumPy arrays or SciPy sparse matrices. Other types that are convertible to numeric arrays, such as Pandas DataFrame, are also acceptable.**

```python
>>> import numpy as np
```

```python
>>> X = np.random.random((10,5))
```

```python
>>> y = np.array(['M','M','F','F','M','F','M','M','F','F','F']) >>> X[X < 0.7] = 0
```

## Training And Test Data

```python
>>> from sklearn.model\_selection import train\_test\_split >>> X\_train, X\_test, y\_train, y\_test = train\_test\_split(X, y, random\_state=0)
```

## Preprocessing The Data

## Standardization

```python
>>> from sklearn.preprocessing import StandardScaler
```

```python
>>> scaler = StandardScaler().fit(X\_train)
```

```python
>>> standardized\_X = scaler.transform(X\_train)
```

<u>>>> standardized\_X\_test = scaler.transform(X\_test)</u>

## Normalization

```python
>>> from sklearn.preprocessing import Normalizer
```

```python
>>> scaler = Normalizer().fit(X\_train)
```

```python
>>> normalized\_X = scaler.transform(X\_train)
```

<u>>>> normalized\_X\_test = scaler.transform(X\_test)</u>

## Binarization

from sklearn.preprocessing import Binarizer >> binarizer = Binarizer(threshold=0.0).fit(X) >> binary\_X = binarizer.transform(X)

## Create Your Model

## Supervised Learning Estimators

## Linear Regression

```python
>>> from sklearn.linear\_model import LinearRegression >>> lr = LinearRegression(normalize=True)
```

## Support Vector Machines (SVM)

```python
>>> from sklearn.svm import SVC
```

```python
>>> svc = SVC(kernel='linear')
```

## Naive Bayes

```python
>>> from sklearn.naive\_bayes import GaussianNB >>> gnb = GaussianNB()
```

## KNN

```python
>>> from sklearn import neighbors
```

<u>>>> knn = neighbors.KNeighborsClassifier(n\_neighbors=5)</u>

## Unsupervised Learning Estimators

## Principal Component Analysis (PCA)

```python
>>> from sklearn.decomposition import PCA >>> pca = PCA(n\_components=0.95)
```

## K Means

```python
>>> from sklearn.cluster import KMeans
```

<u>>>> k\_means = KMeans(n\_clusters=3, random\_state=0)</u>

## Model Fitting

## Supervised learning

```python
>>> lr.fit(X, y)
```

```python
>>> knn.fit(X\_train, y\_train)
```

Fit the model to the data

```python
>>> svc.fit(X\_train, y\_train)
```

```python
>>> k\_means.fit(X\_train)
```

<u>>>> pca\_model = pca.fit\_transform(X\_train)</u>

Fit the model to the data

Fit to data, then transform it

## Prediction

## Supervised Estimators

```python
>>> y\_pred = svc.predict(np.random.random((2,5)))
```

```python
>>> y\_pred = lr.predict(X\_test)
```

```python
>>> y\_pred = knn.predict\_proba(X\_test)
```

**Unsupervised Estimators**

Predict labels

```python
>>> y\_pred = k\_means.predict(X\_test)
```

Predict labels

Estimate probability of a label

Predict labels in clustering algos

## Encoding Categorical Features

```python
>>> from sklearn.preprocessing import LabelEncoder
```

```python
>>> enc = LabelEncoder()
```

```python
>>> y = enc.fit\_transform(y)
```

## Imputing Missing Values

```python
>>> from sklearn.preprocessing import Imputer
```

```python
>>> imp = Imputer(missing\_values=0, strategy='mean', axis=0)
```

```python
>>> imp.fit\_transform(X\_train)
```

## Generating Polynomial Features

```python
>>> from sklearn.preprocessing import PolynomialFeatures
```

```python
>>> poly = PolynomialFeatures(5)
```

```python
>>> poly.fit\_transform(X)
```

## Evaluate Your Model’s Performance

## Classification Metrics

## Accuracy Score

```python
>>> knn.score(X\_test, y\_test)
```

```python
>>> from sklearn.metrics import accuracy\_score >>> accuracy\_score(y\_test, y\_pred)
```

Estimator score method

## Classification Report

Metric scoring functions

from sklearn.metrics import classification report \_>>> print(classification\_report(y\_test, y\_pred))

## Confusion Matrix

Precision, recall, f1-score and support

```python
>>> from sklearn.metrics import confusion\_matrix <u>>>> print(confusion\_matrix(y\_test, y\_pred))</u>
```

## Regression Metrics

## Mean Absolute Error

>> from sklearn.metrics import mean\_absolute\_error >> y\_true = [3, -0.5, 2] >>> mean\_absolute\_error(y\_true, y\_pred)

## Mean Squared Error

>> from sklearn.metrics import mean\_squared\_error >>> mean\_squared\_error(y\_test, y\_pred)

## R² Score

```python
>>> from sklearn.metrics import r2\_score >>> r2\_score(y\_true, y\_pred)
```

## Clustering Metrics

## Adjusted Rand Index

```python
>>> from sklearn.metrics import adjusted\_rand\_score >>> adjusted\_rand\_score(y\_true, y\_pred)
```

## Homogeneity

```python
>>> from sklearn.metrics import homogeneity\_score >>> homogeneity\_score(y\_true, y\_pred)
```

## V-measure

```python
>>> from sklearn.metrics import v\_measure\_score <u>>>> metrics.v\_measure\_score(y\_true, y\_pred)</u>
```

## Cross-Validation

from sklearn.cross\_validation import cross\_val\_score >> print(cross\_val\_score(knn, X\_train, y\_train, cv=4)) <u>>>> print(cross\_val\_score(lr, X, y, cv=2))</u>

## Tune Your Model

## Grid Search

```python
>>> from sklearn.grid search import GridSearchCV \_>>> params = {"n\_neighbors": np.arange(1,3), "metric": ["euclidean", "cityblock"]} >>> grid = GridSearchCV(estimator=knn,
```

param\_grid=params)

```python
>>> grid.fit(X\_train, y\_train)
```

```python
>>> print(grid.best\_score\_)
```

<u>>>> print(grid.best\_estimator\_.n\_neighbors)</u>

## Randomized Parameter Optimization

>> from sklearn.grid\_search import RandomizedSearchCV >> params = {"n\_neighbors": range(1,5), "weights": ["uniform", "distance"]} >> rsearch = RandomizedSearchCV(estimator=knn, param\_distributions=params, cv=4, n\_iter=8, random\_state=5) >> rsearch.fit(X\_train, y\_train) >>> print(rsearch.best\_score\_)

## DataCamp

## Python For Data Science Cheat Sheet

Keras

Learn Python for data science **Interactively** at www.DataCamp.com

## Keras

**Keras** is a powerful and easy-to-use deep learning library for Theano and TensorFlow that provides a high-level neural networks API to develop and evaluate deep learning models.

## A Basic Example

```python
>>> import numpy as np
>>> from keras.models import Sequential
>>> from keras.layers import Dense
>>> data = np.random.random((1000,100))
>>> labels = np.random.randint(2,size=(1000,1))
>>> model = Sequential()
>>> model.add(Dense(32,
                             activation='relu',
                             input_dim=100))
>>> model.add(Dense(1, activation='sigmoid'))
>>> model.compile(optimizer='rmsprop',
                             loss='binary_crossentropy',
                             metrics=['accuracy'])
>>> model.fit(data,labels,epochs=10,batch_size=32)
>>> predictions = model.predict(data)
```

## Data

## Also see NumPy, Pandas & Scikit-Learn

**Your data needs to be stored as NumPy arrays or as a list of NumPy arrays. Ideally, you split the data in training and test sets, for which you can also resort to the** train\_test\_split **module of** sklearn.cross\_validation.

## Keras Data Sets

```python
>>> from keras.datasets import boston\_housing, mnist, cifar10, imdb >> (x\_train,y\_train),(x\_test,y\_test) = mnist.load\_data() >> (x\_train2,y\_train2),(x\_test2,y\_test2) = boston\_housing.load\_data() >>> (x\_train3,y\_train3),(x\_test3,y\_test3) = cifar10.load\_data() >> (x\_train4,y\_train4),(x\_test4,y\_test4) = imdb.load\_data(num\_words=20000) >>> num\_classes = 10
```

## Other

```python
>>> from urllib.request import urlopen >>> data = np.loadtxt(urlopen("http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"),delimiter=",") >>> X = data[:,0:8] >>> y = data [:,8]
```

## Preprocessing

## Sequence Padding

```python
>>> from keras.preprocessing import sequence >>> x\_train4 = sequence.pad\_sequences(x\_train4,maxlen=80) <u>>>> x\_test4 = sequence.pad\_sequences(x\_test4,maxlen=80)</u>
```

## One-Hot Encoding

```python
>>> from keras.utils import to\_categorical >>> Y\_train = to\_categorical(y\_train, num\_classes) >>> Y\_test = to\_categorical(y\_test, num\_classes) >>> Y\_train3 = to\_categorical(y\_train3, num\_classes) >>> Y\_test3 = to\_categorical(y\_test3, num\_classes)
```

## Model Architecture

## Sequential Model

```python
>>> from keras.models import Sequential >>> model = Sequential() >>> model2 = Sequential() >>> model3 = Sequential()
```

## Multilayer Perceptron (MLP)

## Binary Classification

```python
>>> from keras.layers import Dense
>>> model.add(Dense(12,
                       input_dim=8,
                       kernel_initializer='uniform',
                       activation='relu'))
>>> model.add(Dense(8,kernel_initializer='uniform',activation='relu'))
>>> model.add(Dense(1,kernel_initializer='uniform',activation='sigmoid'))
```

## Multi-Class Classification

```python
>>> from keras.layers import Dropout >>> model.add(Dense(512,activation='relu',input\_shape=(784,))) >>> model.add(Dropout(0.2)) >>> model.add(Dense(512,activation='relu')) >>> model.add(Dropout(0.2)) >>> model.add(Dense(10,activation='softmax'))
```

## Regression

```python
>>> model.add(Dense(64,activation='relu',input\_dim=train\_data.shape[1])) >>> model.add(Dense(1))
```

## Convolutional Neural Network (CNN)

```python
>>> from keras.layers import Activation,Conv2D,MaxPooling2D,Flatten
>>> model2.add(Conv2D(32,(3,3),padding='same',input_shape=x_train.shape[1:]))
>>> model2.add(Activation('relu'))
>>> model2.add(Conv2D(32,(3,3)))
>>> model2.add(Activation('relu'))
>>> model2.add(MaxPooling2D(pool_size=(2,2)))
>>> model2.add(Dropout(0.25))
>>> model2.add(Conv2D(64,(3,3), padding='same'))
>>> model2.add(Activation('relu'))
>>> model2.add(Conv2D(64,(3, 3)))
>>> model2.add(Activation('relu'))
>>> model2.add(MaxPooling2D(pool_size=(2,2)))
>>> model2.add(Dropout(0.25))
>>> model2.add(Flatten())
>>> model2.add(Dense(512))
>>> model2.add(Activation('relu'))
>>> model2.add(Dropout(0.5))
>>> model2.add(Dense(num_classes))
>>> model2.add(Activation('softmax'))
```

## Recurrent Neural Network (RNN)

>> from keras.klayers import Embedding,LSTM >> model3.add(Embedding(20000,128)) >>> model3.add(LSTM(128,dropout=0.2,recurrent\_dropout=0.2)) >>> model3.add(Dense(1,activation='sigmoid'))

## Also see NumPy & Scikit-Learn

## Train and Test Sets

```python
>>> from sklearn.model\_selection import train\_test\_split
```

```python
>>> X\_train5,X\_test5,y\_train5,y\_test5 = train\_test\_split(X,
```

## Standardization/Normalization

```python
>>> from sklearn.preprocessing import StandardScaler >>> scaler = StandardScaler().fit(x\_train2) >>> standardized\_X = scaler.transform(x\_train2) <u>>>> standardized\_X\_test = scaler.transform(x\_test2)</u>
```

## Inspect Model

```python
>>> model.output\_shape >>> model.summary() >>> model.get\_config() >>> model.get\_weights()
```

Model output shape Model summary representation Model configuration List all weight tensors in the model

## Compile Model

## MLP: Binary Classification

```python
>>> model.compile(optimizer='adam', loss='binary\_crossentropy', metrics=['accuracy']) **MLP: Multi-Class Classification** >>> model.compile(optimizer='rmsprop', loss='categorical\_crossentropy', metrics=['accuracy']) **MLP: Regression** >>> model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
```

## Recurrent Neural Network

```python
>>> model3.compile(loss='binary\_crossentropy', optimizer='adam', metrics=['accuracy'])
```

## Model Training

```python
>>> model3.fit(x_train4,
                       y_train4,
                       batch_size=32,
                       epochs=15,
                       verbose=1,
                       validation_data=(x_test4,y_test4))
```

## Evaluate Your Model's Performance

```python
>>> score = model3.evaluate(x\_test, y\_test, batch\_size=32)
```

## Prediction

```python
>>> model3.predict(x\_test4, batch\_size=32)
```

<u>>>> model3.predict\_classes(x\_test4,batch\_size=32)</u>

## Save/ Reload Models

>> from keras.models import load\_model >> model3.save('model\_file.h5') >> my\_model = load\_model('my\_model.h5')

## Model Fine-tuning

## Optimization Parameters

```python
>>> from keras.optimizers import RMSprop
>>> opt = RMSprop(lr=0.0001, decay=1e-6)
>>> model2.compile(loss='categorical_crossentropy',
                      optimizer=opt,
                      metrics=['accuracy'])
```

## Early Stopping

from keras.callbacks import EarlyStopping >>> early\_stopping\_monitor = EarlyStopping(patience=2) >>> model3.fit(x\_train4, y\_train4, batch\_size=32, epochs=15, validation\_data=(x\_test4,y\_test4), callbacks=[early\_stopping\_monitor])

## DataCamp
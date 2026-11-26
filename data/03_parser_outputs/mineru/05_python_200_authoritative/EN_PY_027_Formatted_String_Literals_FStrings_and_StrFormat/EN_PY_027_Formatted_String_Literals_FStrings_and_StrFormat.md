<!-- page: 1 -->
# EN_PY_027: Fancier Output Formatting: Formatted String Literals (f-strings), str.format()

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Strings | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

7.1. Fancier Output Formatting
==============================

So far we’ve encountered two ways of writing values: *expression
statements* and the "print()" function.  (A third way is using the
"write()" method of file objects; the standard output file can be
referenced as "sys.stdout". See the Library Reference for more
information on this.)

Often you’ll want more control over the formatting of your output than
simply printing space-separated values. There are several ways to
format output.

* To use formatted string literals, begin a string with "f" or "F"
  before the opening quotation mark or triple quotation mark. Inside
  this string, you can write a Python expression between "{" and "}"
  characters that can refer to variables or literal values.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'

```
* The "str.format()" method of strings requires more manual effort.
  You’ll still use "{" and "}" to mark where a variable will be
  substituted and can provide detailed formatting directives, but
  you’ll also need to provide the information to be formatted. In the
  following code block there are two examples of how to format
  variables:

```python
>>> yes_votes = 42_572_654
>>> total_votes = 85_705_149
>>> percentage = yes_votes / total_votes
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'

```

<!-- page: 2 -->

  Notice how the "yes_votes" are padded with spaces and a negative
  sign only for negative numbers. The example also prints "percentage"
  multiplied by 100, with 2 decimal places and followed by a percent
  sign (see Format Specification Mini-Language for details).

* Finally, you can do all the string handling yourself by using string
  slicing and concatenation operations to create any layout you can
  imagine.  The string type has some methods that perform useful
  operations for padding strings to a given column width.

When you don’t need fancy output but just want a quick display of some
variables for debugging purposes, you can convert any value to a
string with the "repr()" or "str()" functions.

The "str()" function is meant to return representations of values
which are fairly human-readable, while "repr()" is meant to generate
representations which can be read by the interpreter (or will force a
"SyntaxError" if there is no equivalent syntax).  For objects which
don’t have a particular representation for human consumption, "str()"
will return the same value as "repr()".  Many values, such as numbers
or structures like lists and dictionaries, have the same
representation using either function.  Strings, in particular, have
two distinct representations.

Some examples:

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"

```

<!-- page: 3 -->

The "string" module contains a "Template" class that offers yet
another way to substitute values into strings, using placeholders like
"$x" and replacing them with values from a dictionary, but offers much
less control of the formatting.


7.1.1. Formatted String Literals
--------------------------------

Formatted string literals (also called f-strings for short) let you
include the value of Python expressions inside a string by prefixing
the string with "f" or "F" and writing expressions as "{expression}".

An optional format specifier can follow the expression. This allows
greater control over how the value is formatted. The following example
rounds pi to three places after the decimal:

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.

```
Passing an integer after the "':'" will cause that field to be a
minimum number of characters wide.  This is useful for making columns
line up.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

```
Other modifiers can be used to convert the value before it is
formatted. "'!a'" applies "ascii()", "'!s'" applies "str()", and
"'!r'" applies "repr()":

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.

```

<!-- page: 4 -->

The "=" specifier can be used to expand an expression to the text of
the expression, an equal sign, then the representation of the
evaluated expression:

>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'

See self-documenting expressions for more information on the "="
specifier. For a reference on these format specifications, see the
reference guide for the Format Specification Mini-Language.


7.1.2. The String format() Method
---------------------------------

Basic usage of the "str.format()" method looks like this:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

```
The brackets and characters within them (called format fields) are
replaced with the objects passed into the "str.format()" method.  A
number in the brackets can be used to refer to the position of the
object passed into the "str.format()" method.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

```
If keyword arguments are used in the "str.format()" method, their
values are referred to by using the name of the argument.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.

```

<!-- page: 5 -->

Positional and keyword arguments can be arbitrarily combined:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
...                                                    other='Georg'))
The story of Bill, Manfred, and Georg.

```
If you have a really long format string that you don’t want to split
up, it would be nice if you could reference the variables to be
formatted by name instead of by position.  This can be done by simply
passing the dict and using square brackets "'[]'" to access the keys.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

```
This could also be done by passing the "table" dictionary as keyword
arguments with the "**" notation.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

```
This is particularly useful in combination with the built-in function
"vars()", which returns a dictionary containing all local variables:

```python
>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: ...

```
As an example, the following lines produce a tidily aligned set of
columns giving integers and their squares and cubes:

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

```

<!-- page: 6 -->

For a complete overview of string formatting with "str.format()", see
Format String Syntax.


7.1.3. Manual String Formatting
-------------------------------

Here’s the same table of squares and cubes, formatted manually:

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

```
(Note that the one space between each column was added by the way
"print()" works: it always adds spaces between its arguments.)

The "str.rjust()" method of string objects right-justifies a string in
a field of a given width by padding it with spaces on the left. There
are similar methods "str.ljust()" and "str.center()". These methods do
not write anything, they just return a new string. If the input string
is too long, they don’t truncate it, but return it unchanged; this
will mess up your column lay-out but that’s usually better than the
alternative, which would be lying about a value. (If you really want
truncation you can always add a slice operation, as in
"x.ljust(n)[:n]".)

There is another method, "str.zfill()", which pads a numeric string on
the left with zeros.  It understands about plus and minus signs:

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'


```

<!-- page: 7 -->

7.1.4. Old string formatting
----------------------------

The % operator (modulo) can also be used for string formatting. Given
"format % values" (where *format* is a string), "%" conversion
specifications in *format* are replaced with zero or more elements of
*values*. This operation is commonly known as string interpolation.
For example:

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.

```
More information can be found in the printf-style String Formatting
section.

<!-- page: 1 -->
# EN_PY_018: Nested List Comprehensions, Matrix Transposition, and the del Statement

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Data Structures | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

5.1.4. Nested List Comprehensions
---------------------------------

The initial expression in a list comprehension can be any arbitrary
expression, including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list
of 3 lists of length 4:

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

```
The following list comprehension will transpose rows and columns:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

```
As we saw in the previous section, the inner list comprehension is
evaluated in the context of the "for" that follows it, so this example
is equivalent to:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

```

<!-- page: 2 -->

which, in turn, is the same as:

```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

```
In the real world, you should prefer built-in functions to complex
flow statements. The "zip()" function would do a great job for this
use case:

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

```
See Unpacking Argument Lists for details on the asterisk in this line.


5.2. The "del" statement
========================

There is a way to remove an item from a list given its index instead
of its value: the "del" statement.  This differs from the
"~list.pop()" method which returns a value.  The "del" statement can
also be used to remove slices from a list or clear the entire list
(which we did earlier by assignment of an empty list to the slice).
For example:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]

```

<!-- page: 3 -->

"del" can also be used to delete entire variables:

```python
>>> del a

```
Referencing the name "a" hereafter is an error (at least until another
value is assigned to it).  We’ll find other uses for "del" later.

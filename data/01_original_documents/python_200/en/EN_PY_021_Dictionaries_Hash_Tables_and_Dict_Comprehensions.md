<!-- page: 1 -->
# EN_PY_021: Dictionaries (dict): Key-Value Store, Hash Invariants, and Dict Comprehensions

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Data Structures | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

5.5. Dictionaries
=================

Another useful data type built into Python is the *dictionary* (see
Mapping Types — dict). Dictionaries are sometimes found in other
languages as “associative memories” or “associative arrays”.  Unlike
sequences, which are indexed by a range of numbers, dictionaries are
indexed by *keys*, which can be any immutable type; strings and
numbers can always be keys.  Tuples can be used as keys if they
contain only strings, numbers, or tuples; if a tuple contains any
mutable object either directly or indirectly, it cannot be used as a
key. You can’t use lists as keys, since lists can be modified in place
using index assignments, slice assignments, or methods like
"~list.append()" and "~list.extend()".

It is best to think of a dictionary as a set of *key: value* pairs,
with the requirement that the keys are unique (within one dictionary).
A pair of braces creates an empty dictionary: "{}". Placing a comma-
separated list of key:value pairs within the braces adds initial
key:value pairs to the dictionary; this is also the way dictionaries
are written on output.

The main operations on a dictionary are storing a value with some key
and extracting the value given the key.  It is also possible to delete
a key:value pair with "del". If you store using a key that is already
in use, the old value associated with that key is forgotten.  It is an
error to extract a value using a non-existent key.

Performing "list(d)" on a dictionary returns a list of all the keys
used in the dictionary, in insertion order (if you want it sorted,
just use "sorted(d)" instead). To check whether a single key is in the
dictionary, use the "in" keyword.

Here is a small example using a dictionary:

<!-- page: 2 -->


```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False

```
The "dict()" constructor builds dictionaries directly from sequences
of key-value pairs:

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}

```
In addition, dict comprehensions can be used to create dictionaries
from arbitrary key and value expressions:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

```
When the keys are simple strings, it is sometimes easier to specify
pairs using keyword arguments:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

```

<!-- page: 3 -->

<!-- page: 1 -->
# EN_PY_062: The Standard Type Hierarchy: None, Numbers, Sequences, Mappings, Callables

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: CPython Internals | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

~~~~~~~~~~~~~~~~~~~~~~~~~~~

These represent elements from the mathematical set of integers
(positive and negative).

Note:

  The rules for integer representation are intended to give the most
  meaningful interpretation of shift and mask operations involving
  negative integers.

There are two types of integers:

Integers ("int")
   These represent numbers in an unlimited range, subject to available
   (virtual) memory only.  For the purpose of shift and mask
   operations, a binary representation is assumed, and negative
   numbers are represented in a variant of 2’s complement which gives
   the illusion of an infinite string of sign bits extending to the
   left.

Booleans ("bool")
   These represent the truth values False and True.  The two objects
   representing the values "False" and "True" are the only Boolean
   objects. The Boolean type is a subtype of the integer type, and
   Boolean values behave like the values 0 and 1, respectively, in
   almost all contexts, the exception being that when converted to a
   string, the strings ""False"" or ""True"" are returned,
   respectively.


3.2.4.2. "numbers.Real" ("float")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


<!-- page: 2 -->

These represent machine-level double precision floating-point numbers.
You are at the mercy of the underlying machine architecture (and C or
Java implementation) for the accepted range and handling of overflow.
Python does not support single-precision floating-point numbers; the
savings in processor and memory usage that are usually the reason for
using these are dwarfed by the overhead of using objects in Python, so
there is no reason to complicate the language with two kinds of
floating-point numbers.


3.2.4.3. "numbers.Complex" ("complex")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These represent complex numbers as a pair of machine-level double
precision floating-point numbers.  The same caveats apply as for
floating-point numbers. The real and imaginary parts of a complex
number "z" can be retrieved through the read-only attributes "z.real"
and "z.imag".


3.2.5. Sequences
----------------

These represent finite ordered sets indexed by non-negative numbers.
The built-in function "len()" returns the number of items of a
sequence. When the length of a sequence is *n*, the index set contains
the numbers 0, 1, …, *n*-1.  Item *i* of sequence *a* is selected by
"a[i]". Some sequences, including built-in sequences, interpret
negative subscripts by adding the sequence length. For example,
"a[-2]" equals "a[n-2]", the second to last item of sequence a with
length "n".

Sequences also support slicing: "a[i:j]" selects all items with index
*k* such that *i* "<=" *k* "<" *j*.  When used as an expression, a
slice is a sequence of the same type. The comment above about negative
indexes also applies to negative slice positions.

Some sequences also support “extended slicing” with a third “step”
parameter: "a[i:j:k]" selects all items of *a* with index *x* where "x
= i + n*k", *n* ">=" "0" and *i* "<=" *x* "<" *j*.

Sequences are distinguished according to their mutability:


3.2.5.1. Immutable sequences

<!-- page: 3 -->

~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An object of an immutable sequence type cannot change once it is
created.  (If the object contains references to other objects, these
other objects may be mutable and may be changed; however, the
collection of objects directly referenced by an immutable object
cannot change.)

The following types are immutable sequences:

Strings
   A string is a sequence of values that represent Unicode code
   points. All the code points in the range "U+0000 - U+10FFFF" can be
   represented in a string.  Python doesn’t have a char type; instead,
   every code point in the string is represented as a string object
```python
with length "1".  The built-in function "ord()" converts a code
point from its string form to an integer in the range "0 - 10FFFF";
"chr()" converts an integer in the range "0 - 10FFFF" to the
corresponding length "1" string object. "str.encode()" can be used
to convert a "str" to "bytes" using the given text encoding, and
"bytes.decode()" can be used to achieve the opposite.

```
Tuples
   The items of a tuple are arbitrary Python objects. Tuples of two or
   more items are formed by comma-separated lists of expressions.  A
   tuple of one item (a ‘singleton’) can be formed by affixing a comma
   to an expression (an expression by itself does not create a tuple,
```python
since parentheses must be usable for grouping of expressions).  An
empty tuple can be formed by an empty pair of parentheses.

```
Bytes
   A bytes object is an immutable array.  The items are 8-bit bytes,
   represented by integers in the range 0 <= x < 256.  Bytes literals
   (like "b'abc'") and the built-in "bytes()" constructor can be used
   to create bytes objects.  Also, bytes objects can be decoded to
   strings via the "decode()" method.


3.2.5.2. Mutable sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~


<!-- page: 4 -->

Mutable sequences can be changed after they are created.  The
subscription and slicing notations can be used as the target of
assignment and "del" (delete) statements.

Note:

  The "collections" and "array" module provide additional examples of
  mutable sequence types.

There are currently two intrinsic mutable sequence types:

Lists
   The items of a list are arbitrary Python objects.  Lists are formed
   by placing a comma-separated list of expressions in square
   brackets. (Note that there are no special cases needed to form
   lists of length 0 or 1.)

Byte Arrays
   A bytearray object is a mutable array. They are created by the
```python
built-in "bytearray()" constructor.  Aside from being mutable (and
hence unhashable), byte arrays otherwise provide the same interface
and functionality as immutable "bytes" objects.


```
3.2.6. Set types
----------------

These represent unordered, finite sets of unique, immutable objects.
As such, they cannot be indexed by any subscript. However, they can be
iterated over, and the built-in function "len()" returns the number of
items in a set. Common uses for sets are fast membership testing,
removing duplicates from a sequence, and computing mathematical
operations such as intersection, union, difference, and symmetric
difference.

For set elements, the same immutability rules apply as for dictionary
keys. Note that numeric types obey the normal rules for numeric
comparison: if two numbers compare equal (e.g., "1" and "1.0"), only
one of them can be contained in a set.

There are currently two intrinsic set types:

Sets

<!-- page: 5 -->

   These represent a mutable set. They are created by the built-in
   "set()" constructor and can be modified afterwards by several
   methods, such as "add()".

Frozen sets
   These represent an immutable set.  They are created by the built-in
   "frozenset()" constructor.  As a frozenset is immutable and
   *hashable*, it can be used again as an element of another set, or
   as a dictionary key.


3.2.7. Mappings
---------------

These represent finite sets of objects indexed by arbitrary index
sets. The subscript notation "a[k]" selects the item indexed by "k"
from the mapping "a"; this can be used in expressions and as the
target of assignments or "del" statements. The built-in function
"len()" returns the number of items in a mapping.

There is currently a single intrinsic mapping type:


3.2.7.1. Dictionaries
~~~~~~~~~~~~~~~~~~~~~

These represent finite sets of objects indexed by nearly arbitrary
values.  The only types of values not acceptable as keys are values
containing lists or dictionaries or other mutable types that are
compared by value rather than by object identity, the reason being
that the efficient implementation of dictionaries requires a key’s
hash value to remain constant. Numeric types used for keys obey the
normal rules for numeric comparison: if two numbers compare equal
(e.g., "1" and "1.0") then they can be used interchangeably to index
the same dictionary entry.

Dictionaries preserve insertion order, meaning that keys will be
produced in the same order they were added sequentially over the
dictionary. Replacing an existing key does not change the order,
however removing a key and re-inserting it will add it to the end
instead of keeping its old place.

Dictionaries are mutable; they can be created by the "{}" notation
(see section Dictionary displays).


<!-- page: 6 -->

The extension modules "dbm.ndbm" and "dbm.gnu" provide additional
examples of mapping types, as does the "collections" module.

Changed in version 3.7: Dictionaries did not preserve insertion order
in versions of Python before 3.6. In CPython 3.6, insertion order was
preserved, but it was considered an implementation detail at that time
rather than a language guarantee.


3.2.8. Callable types
---------------------

These are the types to which the function call operation (see section
Calls) can be applied:


3.2.8.1. User-defined functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A user-defined function object is created by a function definition
(see section Function definitions).  It should be called with an
argument list containing the same number of items as the function’s
formal parameter list.


3.2.8.1.1. Special read-only attributes
"""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| Attribute                                          | Meaning                                            |
|====================================================|====================================================|
| function.__globals__                               | A reference to the "dictionary" that holds the     |
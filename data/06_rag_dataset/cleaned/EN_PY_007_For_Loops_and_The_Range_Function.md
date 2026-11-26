# EN_PY_007: For Loops, Iterables, and the range() Function

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Control Flow | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

4.2. "for" Statements
=====================

The "for" statement in Python differs a bit from what you may be used
to in C or Pascal.  Rather than always iterating over an arithmetic
progression of numbers (like in Pascal), or giving the user the
ability to define both the iteration step and halting condition (as
C), Python’s "for" statement iterates over the items of any sequence
(a list or a string), in the order that they appear in the sequence.
For example (no pun intended):

```python
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12

```

Code that modifies a collection while iterating over that same
collection can be tricky to get right.  Instead, it is usually more
straight-forward to loop over a copy of the collection or to create a
new collection:

   # Create a sample collection
   users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

   # Strategy:  Iterate over a copy

```python
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

```

4.3. The "range()" Function
===========================

If you do need to iterate over a sequence of numbers, the built-in
function "range()" comes in handy.  It generates arithmetic
progressions:

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4

```

The given end point is never part of the generated sequence;
"range(10)" generates 10 values, the legal indices for items of a
sequence of length 10.  It is possible to let the range start at
another number, or to specify a different increment (even negative;
sometimes this is called the ‘step’):

```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]

```

To iterate over the indices of a sequence, you can combine "range()"
and "len()" as follows:

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb

```

In most such cases, however, it is convenient to use the "enumerate()"
function, see Looping Techniques.

A strange thing happens if you just print a range:

```python
>>> range(10)
range(0, 10)

```

In many ways the object returned by "range()" behaves as if it is a
list, but in fact it isn’t. It is an object which returns the
successive items of the desired sequence when you iterate over it, but
it doesn’t really make the list, thus saving space.

We say such an object is *iterable*, that is, suitable as a target for
functions and constructs that expect something from which they can
obtain successive items until the supply is exhausted.  We have seen
that the "for" statement is such a construct, while an example of a
function that takes an iterable is "sum()":

```python
>>> sum(range(4))  # 0 + 1 + 2 + 3
6

```

Later we will see more functions that return iterables and take
iterables as arguments.  In chapter Data Structures, we will discuss
in more detail about "list()".
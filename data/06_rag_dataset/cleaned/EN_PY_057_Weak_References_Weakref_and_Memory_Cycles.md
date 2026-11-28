# EN_PY_057: Standard Library: Weak References (weakref) and Cyclic Garbage Collection

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Memory | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

Python does automatic memory management (reference counting for most
objects and *garbage collection* to eliminate cycles).  The memory is
freed shortly after the last reference to it has been eliminated.

This approach works fine for most applications but occasionally there
is a need to track objects only as long as they are being used by
something else. Unfortunately, just tracking them creates a reference
that makes them permanent. The "weakref" module provides tools for
tracking objects without creating a reference.  When the object is no
longer needed, it is automatically removed from a weakref table and a
callback is triggered for weakref objects.  Typical applications
include caching objects that are expensive to create:

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python312/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'

```

11.7. Tools for Working with Lists
==================================

Many data structure needs can be met with the built-in list type.
However, sometimes there is a need for alternative implementations
with different performance trade-offs.

The "array" module provides an "array" object that is like a list that
stores only homogeneous data and stores it more compactly.  The
following example shows an array of numbers stored as two byte
unsigned binary numbers (typecode ""H"") rather than the usual 16
bytes per entry for regular lists of Python int objects:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])

```

The "collections" module provides a "deque" object that is like a list
with faster appends and pops from the left side but slower lookups in
the middle. These objects are well suited for implementing queues and
breadth first tree searches:

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

```

In addition to alternative list implementations, the library also
offers other tools such as the "bisect" module with functions for

manipulating sorted lists:

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

```

The "heapq" module provides functions for implementing heaps based on
regular lists.  The lowest valued entry is always kept at position
zero.  This is useful for applications which repeatedly access the
smallest element but do not want to run a full list sort:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]

```

11.8. Decimal Floating-Point Arithmetic
=======================================

The "decimal" module offers a "Decimal" datatype for decimal floating-
point arithmetic.  Compared to the built-in "float" implementation of
binary floating point, the class is especially helpful for

* financial applications and other uses which require exact decimal
  representation,

* control over precision,

* control over rounding to meet legal or regulatory requirements,

* tracking of significant decimal places, or

* applications where the user expects the results to match
  calculations done by hand.

For example, calculating a 5% tax on a 70 cent phone charge gives

different results in decimal floating point and binary floating point.
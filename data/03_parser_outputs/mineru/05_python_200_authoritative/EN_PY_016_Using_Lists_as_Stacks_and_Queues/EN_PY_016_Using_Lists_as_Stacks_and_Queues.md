<!-- page: 1 -->
# EN_PY_016: Using Lists as Stacks (LIFO) and Queues (FIFO with deque)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Data Structures | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

5.1.1. Using Lists as Stacks
----------------------------

The list methods make it very easy to use a list as a stack, where the
last element added is the first element retrieved (“last-in, first-
out”).  To add an item to the top of the stack, use "~list.append()".
To retrieve an item from the top of the stack, use "~list.pop()"
without an explicit index.  For example:

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]


```
5.1.2. Using Lists as Queues
----------------------------

It is also possible to use a list as a queue, where the first element
added is the first element retrieved (“first-in, first-out”); however,
lists are not efficient for this purpose.  While appends and pops from

<!-- page: 2 -->

the end of list are fast, doing inserts or pops from the beginning of
a list is slow (because all of the other elements have to be shifted
by one).

To implement a queue, use "collections.deque" which was designed to
have fast appends and pops from both ends.  For example:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

```
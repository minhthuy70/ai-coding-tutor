<!-- page: 1 -->
# EN_PY_015: More on Lists: Methods (append, extend, insert, remove, pop, index, count, sort)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Data Structures | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

5.1. More on Lists
==================

The list data type has some more methods.  Here are all of the methods
of list objects:

list.append(x)

   Add an item to the end of the list.  Similar to "a[len(a):] = [x]".

list.extend(iterable)

```python
Extend the list by appending all the items from the iterable.
Similar to "a[len(a):] = iterable".

```
list.insert(i, x)

   Insert an item at a given position.  The first argument is the
   index of the element before which to insert, so "a.insert(0, x)"
   inserts at the front of the list, and "a.insert(len(a), x)" is
   equivalent to "a.append(x)".

list.remove(x)

```python
Remove the first item from the list whose value is equal to *x*.
It raises a "ValueError" if there is no such item.

```
list.pop([i])

```python
Remove the item at the given position in the list, and return it.
If no index is specified, "a.pop()" removes and returns the last
item in the list. It raises an "IndexError" if the list is empty or
the index is outside the list range.

```

<!-- page: 2 -->

list.clear()

```python
Remove all items from the list.  Similar to "del a[:]".

```
list.index(x[, start[, end]])

   Return zero-based index in the list of the first item whose value
```python
is equal to *x*. Raises a "ValueError" if there is no such item.

The optional arguments *start* and *end* are interpreted as in the
slice notation and are used to limit the search to a particular
subsequence of the list.  The returned index is computed relative
to the beginning of the full sequence rather than the *start*
argument.

```
list.count(x)

   Return the number of times *x* appears in the list.

list.sort(*, key=None, reverse=False)

   Sort the items of the list in place (the arguments can be used for
```python
sort customization, see "sorted()" for their explanation).

```
list.reverse()

   Reverse the elements of the list in place.

list.copy()

   Return a shallow copy of the list.  Similar to "a[:]".

An example that uses most of the list methods:

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'

```

<!-- page: 3 -->

You might have noticed that methods like "insert", "remove" or "sort"
that only modify the list have no return value printed – they return
the default "None". [1]  This is a design principle for all mutable
data structures in Python.

Another thing you might notice is that not all data can be sorted or
compared.  For instance, "[None, 'hello', 10]" doesn’t sort because
integers can’t be compared to strings and "None" can’t be compared to
other types.  Also, there are some types that don’t have a defined
ordering relation.  For example, "3+4j < 5+7j" isn’t a valid
comparison.

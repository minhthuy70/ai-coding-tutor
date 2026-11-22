# Official Python Documentation: Data Structures & Object-Oriented Programming

## 5. Data Structures (Lists, Stacks, Queues, Tuples, Dictionaries)

.. _tut-structures:

***************
Data Structures
***************

This chapter describes some things you've learned about already in more detail,
and adds some new things as well.

.. _tut-morelists:

More on Lists
=============

The :ref:`list <typesseq-list>` data type has some more methods. Here are all
of the methods of list objects:

.. method:: list.append(value, /)
   :noindex:

   Add an item to the end of the list.  Similar to ``a[len(a):] = [x]``.

.. method:: list.extend(iterable, /)
   :noindex:

   Extend the list by appending all the items from the iterable.  Similar to
   ``a[len(a):] = iterable``.

.. method:: list.insert(index, value, /)
   :noindex:

   Insert an item at a given position.  The first argument is the index of the
   element before which to insert, so ``a.insert(0, x)`` inserts at the front of
   the list, and ``a.insert(len(a), x)`` is equivalent to ``a.append(x)``.

.. method:: list.remove(value, /)
   :noindex:

   Remove the first item from the list whose value is equal to *value*.  It raises a
   :exc:`ValueError` if there is no such item.

.. method:: list.pop(index=-1, /)
   :noindex:

   Remove the item at the given position in the list, and return it.  If no index
   is specified, ``a.pop()`` removes and returns the last item in the list.
   It raises an :exc:`IndexError` if the list is empty or the index is
   outside the list range.

.. method:: list.clear()
   :noindex:

   Remove all items from the list.  Similar to ``del a[:]``.

.. method:: list.index(value[, start[, stop]])
   :noindex:

   Return zero-based index of the first occurrence of *value* in the list.
   Raises a :exc:`ValueError` if there is no such item.

   The optional arguments *start* and *end* are interpreted as in the slice
   notation and are used to limit the search to a particular subsequence of
   the list.  The returned index is computed relative to the beginning of the full
   sequence rather than the *start* argument.

.. method:: list.count(value, /)
   :noindex:

   Return the number of times *value* appears in the list.

.. method:: list.sort(*, key=None, reverse=False)
   :noindex:

   Sort the items of the list in place (the arguments can be used for sort
   customization, see :func:`sorted` for their explanation).

.. method:: list.reverse()
   :noindex:

   Reverse the elements of the list in place.

.. method:: list.copy()
   :noindex:

   Return a shallow copy of the list.  Similar to ``a[:]``.

An example that uses most of the list methods::

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

You might have noticed that methods like ``insert``, ``remove`` or ``sort`` that
only modify the list have no return value printed -- they return the default
``None``. [#]_  This is a design principle for all mutable data structures in
Python.

Another thing you might notice is that not all data can be sorted or
compared.  For instance, ``[None, 'hello', 10]`` doesn't sort because
integers can't be compared to strings and ``None`` can't be compared to
other types.  Also, there are some types that don't have a defined
ordering relation.  For example, ``3+4j < 5+7j`` isn't a valid
comparison.

.. _tut-lists-as-stacks:

Using Lists as Stacks
---------------------

The list methods make it very easy to use a list as a stack, where the last
element added is the first element retrieved ("last-in, first-out").  To add an
item to the top of the stack, use :meth:`~list.append`.  To retrieve an item from the
top of the stack, use :meth:`~list.pop` without an explicit index.  For example::

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

.. _tut-lists-as-queues:

Using Lists as Queues
---------------------

It is also possible to use a list as a queue, where the first element added is
the first element retrieved ("first-in, first-out"); however, lists are not
efficient for this purpose.  While appends and pops from the end of list are
fast, doing inserts or pops from the beginning of a list is slow (because all
of the other elements have to be shifted by one).  See
:ref:`time-complexity` for more information.

To implement a queue, use :class:`collections.deque` which was designed to
have fast appends and pops from both ends.  For example::

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

.. _tut-listcomps:

List Comprehensions
-------------------

List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element is the result of
some operations applied to each member of another sequence or iterable, or to
create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like::

   >>> squares = []
   >>> for x in range(10):
   ...     squares.append(x**2)
   ...
   >>> squares
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Note that this creates (or overwrites) a variable named ``x`` that still exists
after the loop completes.  We can calculate the list of squares without any
side effects using::

   squares = list(map(lambda x: x**2, range(10)))

or, equivalently::

   squares = [x**2 for x in range(10)]

which is more concise and readable.

A list comprehension consists of brackets containing an expression followed
by a :keyword:`!for` clause, then zero or more :keyword:`!for` or :keyword:`!if`
clauses.  The result will be a new list resulting from evaluating the expression
in the context of the :keyword:`!for` and :keyword:`!if` clauses which follow it.
For example, this listcomp combines the elements of two lists if they are not
equal::

   >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

and it's equivalent to::

   >>> combs = []
   >>> for x in [1,2,3]:
   ...     for y in [3,1,4]:
   ...         if x != y:
   ...             combs.append((x, y))
   ...
   >>> combs
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

Note how the order of the :keyword:`for` and :keyword:`if` statements is the
same in both these snippets.

If the expression is a tuple (e.g. the ``(x, y)`` in the previous example),
it must be parenthesized. ::

   >>> vec = [-4, -2, 0, 2, 4]
   >>> # create a new list with the values doubled
   >>> [x*2 for x in vec]
   [-8, -4, 0, 4, 8]
   >>> # filter the list to exclude negative numbers
   >>> [x for x in vec if x >= 0]
   [0, 2, 4]
   >>> # apply a function to all the elements
   >>> [abs(x) for x in vec]
   [4, 2, 0, 2, 4]
   >>> # call a method on each element
   >>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
   >>> [weapon.strip() for weapon in freshfruit]
   ['banana', 'loganberry', 'passion fruit']
   >>> # create a list of 2-tuples like (number, square)
   >>> [(x, x**2) for x in range(6)]
   [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
   >>> # the tuple must be parenthesized, otherwise an error is raised
   >>> [x, x**2 for x in range(6)]
     File "<stdin>", line 1
       [x, x**2 for x in range(6)]
        ^^^^^^^
   SyntaxError: did you forget parentheses around the comprehension target?
   >>> # flatten a list using a listcomp with two 'for'
   >>> vec = [[1,2,3], [4,5,6], [7,8,9]]
   >>> [num for elem in vec for num in elem]
   [1, 2, 3, 4, 5, 6, 7, 8, 9]

List comprehensions can contain complex expressions and nested functions::

   >>> from math import pi
   >>> [str(round(pi, i)) for i in range(1, 6)]
   ['3.1', '3.14', '3.142', '3.1416', '3.14159']

Nested List Comprehensions
--------------------------

The initial expression in a list comprehension can be any arbitrary expression,
including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list of
3 lists of length 4::

   >>> matrix = [
   ...     [1, 2, 3, 4],
   ...     [5, 6, 7, 8],
   ...     [9, 10, 11, 12],
   ... ]

The following list comprehension will transpose rows and columns::

   >>> [[row[i] for row in matrix] for i in range(4)]
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

As we saw in the previous section, the inner list comprehension is evaluated in
the context of the :keyword:`for` that follows it, so this example is
equivalent to::

   >>> transposed = []
   >>> for i in range(4):
   ...     transposed.append([row[i] for row in matrix])
   ...
   >>> transposed
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

which, in turn, is the same as::

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

In the real world, you should prefer built-in functions to complex flow statements.
The :func:`zip` function would do a great job for this use case::

   >>> list(zip(*matrix))
   [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

See :ref:`tut-unpacking-arguments` for details on the asterisk in this line.

Unpacking in Lists and List Comprehensions
------------------------------------------

The section on :ref:`tut-unpacking-arguments` describes the use of ``*`` to
"unpack" the elements of an iterable object, providing each one separately as
an argument to a function.  Unpacking can also be used in other contexts, for
example, when creating lists.  When specifying elements of a list, prefixing an
expression by a ``*`` will unpack the result of that expression, adding each of
its elements to the list we're creating::

   >>> x = [1, 2, 3]
   >>> [0, *x, 4, 5, 6]
   [0, 1, 2, 3, 4, 5, 6]

This only works if the expression following the ``*`` evaluates to an iterable
object; trying to unpack a non-iterable object will raise an exception::

   >>> x = 1
   >>> [0, *x, 2, 3, 4]
   Traceback (most recent call last):
     File "<python-input-1>", line 1, in <module>
       [0, *x, 2, 3, 4]
   TypeError: Value after * must be an iterable, not int

Unpacking can also be used in list comprehensions, as a way to build a new list
representing the concatenation of an arbitrary number of iterables::

   >>> x = [[1, 2, 3], [4, 5, 6], [], [7], [8, 9]]
   >>> [*element for element in x]
   [1, 2, 3, 4, 5, 6, 7, 8, 9]

Note that the effect is that each element from ``x`` is unpacked.  This works
for arbitrary iterable objects, not just lists::

   >>> x = [[1, 2, 3], 'cat', {'spam': 'eggs'}]
   >>> [*element for element in x]
   [1, 2, 3, 'c', 'a', 't', 'spam']

But if the objects in ``x`` are not iterable, this expression would again raise
an exception.

.. _tut-del:

The :keyword:`!del` statement
=============================

There is a way to remove an item from a list given its index instead of its
value: the :keyword:`del` statement.  This differs from the :meth:`~list.pop` method
which returns a value.  The :keyword:`!del` statement can also be used to remove
slices from a list or clear the entire list (which we did earlier by assignment
of an empty list to the slice).  For example::

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

:keyword:`del` can also be used to delete entire variables::

   >>> del a

Referencing the name ``a`` hereafter is an error (at least until another value
is assigned to it).  We'll find other uses for :keyword:`del` later.

.. _tut-tuples:

Tuples and Sequences
====================

We saw that lists and strings have many common properties, such as indexing and
slicing operations.  They are two examples of *sequence* data types (see
:ref:`typesseq`).  Since Python is an evolving language, other sequence data
types may be added.  There is also another standard sequence data type: the
*tuple*.

A tuple consists of a number of values separated by commas, for instance::

   >>> t = 12345, 54321, 'hello!'
   >>> t[0]
   12345
   >>> t
   (12345, 54321, 'hello!')
   >>> # Tuples may be nested:
   >>> u = t, (1, 2, 3, 4, 5)
   >>> u
   ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
   >>> # Tuples are immutable:
   >>> t[0] = 88888
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment
   >>> # but they can contain mutable objects:
   >>> v = ([1, 2, 3], [3, 2, 1])
   >>> v
   ([1, 2, 3], [3, 2, 1])
   >>> # they support unpacking just like lists:
   >>> x = [1, 2, 3]
   >>> 0, *x, 4
   (0, 1, 2, 3, 4)

As you see, on output tuples are always enclosed in parentheses, so that nested
tuples are interpreted correctly; they may be input with or without surrounding
parentheses, although often parentheses are necessary anyway (if the tuple is
part of a larger expression).  It is not possible to assign to the individual
items of a tuple, however it is possible to create tuples which contain mutable
objects, such as lists.

Though tuples may seem similar to lists, they are often used in different
situations and for different purposes.
Tuples are :term:`immutable`, and usually contain a heterogeneous sequence of
elements that are accessed via unpacking (see later in this section) or indexing
(or even by attribute in the case of :func:`namedtuples <collections.namedtuple>`).
Lists are :term:`mutable`, and their elements are usually homogeneous and are
accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the
syntax has some extra quirks to accommodate these.  Empty tuples are constructed
by an empty pair of parentheses; a tuple with one item is constructed by
following a value with a comma (it is not sufficient to enclose a single value
in parentheses). Ugly, but effective.  For example::

   >>> empty = ()
   >>> singleton = 'hello',    # <-- note trailing comma
   >>> len(empty)
   0
   >>> len(singleton)
   1
   >>> singleton
   ('hello',)

The statement ``t = 12345, 54321, 'hello!'`` is an example of *tuple packing*:
the values ``12345``, ``54321`` and ``'hello!'`` are packed together in a tuple.
The reverse operation is also possible::

   >>> x, y, z = t

This is called, appropriately enough, *sequence unpacking* and works for any
sequence on the right-hand side.  Sequence unpacking requires that there are as
many variables on the left side of the equals sign as there are elements in the
sequence.  Note that multiple assignment is really just a combination of tuple
packing and sequence unpacking.

.. _tut-sets:

Sets
====

Python also includes a data type for :ref:`sets <types-set>`.  A set is
an unordered collection with no duplicate elements.  Basic uses include
membership testing and eliminating duplicate entries.  Set objects also
support mathematical operations like union, intersection, difference, and
symmetric difference.

Curly braces or the :func:`set` function can be used to create sets.  Note: to
create an empty set you have to use ``set()``, not ``{}``; the latter creates an
empty dictionary, a data structure that we discuss in the next section.

Because sets are unordered, iterating over them or printing them can
produce the elements in a different order than you expect.

Here is a brief demonstration::

   >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
   >>> print(basket)                      # show that duplicates have been removed
   {'orange', 'banana', 'pear', 'apple'}
   >>> 'orange' in basket                 # fast membership testing
   True
   >>> 'crabgrass' in basket
   False

   >>> # Demonstrate set operations on unique letters from two words
   >>>
   >>> a = set('abracadabra')
   >>> b = set('alacazam')
   >>> a                                  # unique letters in a
   {'a', 'r', 'b', 'c', 'd'}
   >>> a - b                              # letters in a but not in b
   {'r', 'd', 'b'}
   >>> a | b                              # letters in a or b or both
   {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
   >>> a & b                              # letters in both a and b
   {'a', 'c'}
   >>> a ^ b                              # letters in a or b but not both
   {'r', 'd', 'b', 'm', 'z', 'l'}

Similarly to :ref:`list comprehensions <tut-listcomps>`, set comprehensions
are also supported, including comprehensions with unpacking::

   >>> a = {x for x in 'abracadabra' if x not in 'abc'}
   >>> a
   {'r', 'd'}

   >>> fruits = [{'apple', 'avocado', 'apricot'}, {'banana', 'blueberry'}]
   >>> {*fruit for fruit in fruits}
   {'blueberry', 'banana', 'avocado', 'apple', 'apricot'}

.. _tut-dictionaries:

Dictionaries
============

Another useful data type built into Python is the *dictionary* (see
:ref:`typesmapping`). Dictionaries are sometimes found in other languages as
"associative memories" or "associative arrays".  Unlike sequences, which are
indexed by a range of numbers, dictionaries are indexed by *keys*, which can be
any immutable type; strings and numbers can always be keys.  Tuples can be used
as keys if they contain only strings, numbers, or tuples; if a tuple contains
any mutable object either directly or indirectly, it cannot be used as a key.
You can't use lists as keys, since lists can be modified in place using index
assignments, slice assignments, or methods like :meth:`~list.append` and
:meth:`~list.extend`.

It is best to think of a dictionary as a set of *key: value* pairs,
with the requirement that the keys are unique (within one dictionary). A pair of
braces creates an empty dictionary: ``{}``. Placing a comma-separated list of
key:value pairs within the braces adds initial key:value pairs to the
dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and
extracting the value given the key.  It is also possible to delete a key:value
pair with ``del``. If you store using a key that is already in use, the old
value associated with that key is forgotten.

Extracting a value for a non-existent key by subscripting (``d[key]``) raises a
:exc:`KeyError`. To avoid getting this error when trying to access a possibly
non-existent key, use the :meth:`~dict.get` method instead, which returns
``None`` (or a specified default value) if the key is not in the dictionary.

Performing ``list(d)`` on a dictionary returns a list of all the keys
used in the dictionary, in insertion order (if you want it sorted, just use
``sorted(d)`` instead). To check whether a single key is in the
dictionary, use the :keyword:`in` keyword.

Here is a small example using a dictionary::

   >>> tel = {'jack': 4098, 'sape': 4139}
   >>> tel['guido'] = 4127
   >>> tel
   {'jack': 4098, 'sape': 4139, 'guido': 4127}
   >>> tel['jack']
   4098
   >>> tel['irv']
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   KeyError: 'irv'
   >>> print(tel.get('irv'))
   None
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

The :func:`dict` constructor builds dictionaries directly from sequences of
key-value pairs::

   >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
   {'sape': 4139, 'guido': 4127, 'jack': 4098}

In addition, dict comprehensions can be used to create dictionaries from
arbitrary key and value expressions::

   >>> {x: x**2 for x in (2, 4, 6)}
   {2: 4, 4: 16, 6: 36}

And dictionary unpacking (via ``**``) can be used to merge multiple
dictionaries::

   >>> odds = {i: i**2 for i in (1, 3, 5)}
   >>> evens = {i: i**2 for i in (2, 4, 6)}
   >>> {**odds, **evens}
   {1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36}

   >>> all_values = [odds, evens, {0: 0}]
   >>> {**i for i in all_values}
   {1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36, 0: 0}

When the keys are simple strings, it is sometimes easier to specify pairs using
keyword arguments::

   >>> dict(sape=4139, guido=4127, jack=4098)
   {'sape': 4139, 'guido': 4127, 'jack': 4098}

.. _tut-loopidioms:

Looping Techniques
==================

When looping through dictionaries, the key and corresponding value can be
retrieved at the same time using the :meth:`~dict.items` method. ::

   >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   >>> for k, v in knights.items():
   ...     print(k, v)
   ...
   gallahad the pure
   robin the brave

When looping through a sequence, the position index and corresponding value can
be retrieved at the same time using the :func:`enumerate` function. ::

   >>> for i, v in enumerate(['tic', 'tac', 'toe']):
   ...     print(i, v)
   ...
   0 tic
   1 tac
   2 toe

To loop over two or more sequences at the same time, the entries can be paired
with the :func:`zip` function. ::

   >>> questions = ['name', 'quest', 'favorite color']
   >>> answers = ['lancelot', 'the holy grail', 'blue']
   >>> for q, a in zip(questions, answers):
   ...     print('What is your {0}?  It is {1}.'.format(q, a))
   ...
   What is your name?  It is lancelot.
   What is your quest?  It is the holy grail.
   What is your favorite color?  It is blue.

To loop over a sequence in reverse, first specify the sequence in a forward
direction and then call the :func:`reversed` function. ::

   >>> for i in reversed(range(1, 10, 2)):
   ...     print(i)
   ...
   9
   7
   5
   3
   1

To loop over a sequence in sorted order, use the :func:`sorted` function which
returns a new sorted list while leaving the source unaltered. ::

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for i in sorted(basket):
   ...     print(i)
   ...
   apple
   apple
   banana
   orange
   orange
   pear

Using :func:`set` on a sequence eliminates duplicate elements. The use of
:func:`sorted` in combination with :func:`set` over a sequence is an idiomatic
way to loop over unique elements of the sequence in sorted order. ::

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for f in sorted(set(basket)):
   ...     print(f)
   ...
   apple
   banana
   orange
   pear

It is sometimes tempting to change a list while you are looping over it;
however, it is often simpler and safer to create a new list instead. ::

   >>> import math
   >>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
   >>> filtered_data = []
   >>> for value in raw_data:
   ...     if not math.isnan(value):
   ...         filtered_data.append(value)
   ...
   >>> filtered_data
   [56.2, 51.7, 55.3, 52.5, 47.8]

.. _tut-conditions:

More on Conditions
==================

The conditions used in ``while`` and ``if`` statements can contain any
operators, not just comparisons.

The comparison operators ``in`` and ``not in`` are membership tests that
determine whether a value is in (or not in) a container.  The operators ``is``
and ``is not`` compare whether two objects are really the same object.  All
comparison operators have the same priority, which is lower than that of all
numerical operators.

Comparisons can be chained.  For example, ``a < b == c`` tests whether ``a`` is
less than ``b`` and moreover ``b`` equals ``c``.

Comparisons may be combined using the Boolean operators ``and`` and ``or``, and
the outcome of a comparison (or of any other Boolean expression) may be negated
with ``not``.  These have lower priorities than comparison operators; between
them, ``not`` has the highest priority and ``or`` the lowest, so that ``A and
not B or C`` is equivalent to ``(A and (not B)) or C``. As always, parentheses
can be used to express the desired composition.

The Boolean operators ``and`` and ``or`` are so-called *short-circuit*
operators: their arguments are evaluated from left to right, and evaluation
stops as soon as the outcome is determined.  For example, if ``A`` and ``C`` are
true but ``B`` is false, ``A and B and C`` does not evaluate the expression
``C``.  When used as a general value and not as a Boolean, the return value of a
short-circuit operator is the last evaluated argument.

It is possible to assign the result of a comparison or other Boolean expression
to a variable.  For example, ::

   >>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
   >>> non_null = string1 or string2 or string3
   >>> non_null
   'Trondheim'

Note that in Python, unlike C, assignment inside expressions must be done
explicitly with the
:ref:`walrus operator <why-can-t-i-use-an-assignment-in-an-expression>` ``:=``.
This avoids a common class of problems encountered in C programs: typing ``=``
in an expression when ``==`` was intended.

.. _tut-comparing:

Comparing Sequences and Other Types
===================================
Sequence objects typically may be compared to other objects with the same sequence
type. The comparison uses *lexicographical* ordering: first the first two
items are compared, and if they differ this determines the outcome of the
comparison; if they are equal, the next two items are compared, and so on, until
either sequence is exhausted. If two items to be compared are themselves
sequences of the same type, the lexicographical comparison is carried out
recursively.  If all items of two sequences compare equal, the sequences are
considered equal. If one sequence is an initial sub-sequence of the other, the
shorter sequence is the smaller (lesser) one.  Lexicographical ordering for
strings uses the Unicode code point number to order individual characters.
Some examples of comparisons between sequences of the same type::

   (1, 2, 3)              < (1, 2, 4)
   [1, 2, 3]              < [1, 2, 4]
   'ABC' < 'C' < 'Pascal' < 'Python'
   (1, 2, 3, 4)           < (1, 2, 4)
   (1, 2)                 < (1, 2, -1)
   (1, 2, 3)             == (1.0, 2.0, 3.0)
   (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

Note that comparing objects of different types with ``<`` or ``>`` is legal
provided that the objects have appropriate comparison methods.  For example,
mixed numeric types are compared according to their numeric value, so 0 equals
0.0, etc.  Otherwise, rather than providing an arbitrary ordering, the
interpreter will raise a :exc:`TypeError` exception.

.. rubric:: Footnotes

.. [#] Other languages may return the mutated object, which allows method
       chaining, such as ``d->insert("a")->remove("b")->sort();``.

---

## 9. Classes & Object-Oriented Programming (Inheritance, Scopes, Iterators)

.. _tut-classes:

*******
Classes
*******

Classes provide a means of bundling data and functionality together.  Creating
a new class creates a new *type* of object, allowing new *instances* of that
type to be made.  Each class instance can have attributes attached to it for
maintaining its state.  Class instances can also have methods (defined by its
class) for modifying its state.

Compared with other programming languages, Python's class mechanism adds classes
with a minimum of new syntax and semantics.  It is a mixture of the class
mechanisms found in C++ and Modula-3.  Python classes provide all the standard
features of Object Oriented Programming: the class inheritance mechanism allows
multiple base classes, a derived class can override any methods of its base
class or classes, and a method can call the method of a base class with the same
name.  Objects can contain arbitrary amounts and kinds of data.  As is true for
modules, classes partake of the dynamic nature of Python: they are created at
runtime, and can be modified further after creation.

In C++ terminology, normally class members (including the data members) are
*public* (except see below :ref:`tut-private`), and all member functions are
*virtual*.  As in Modula-3, there are no shorthands for referencing the object's
members from its methods: the method function is declared with an explicit first
argument representing the object, which is provided implicitly by the call.  As
in Smalltalk, classes themselves are objects.  This provides semantics for
importing and renaming.  Unlike C++ and Modula-3, built-in types can be used as
base classes for extension by the user.  Also, like in C++, most built-in
operators with special syntax (arithmetic operators, subscripting etc.) can be
redefined for class instances.

(Lacking universally accepted terminology to talk about classes, I will make
occasional use of Smalltalk and C++ terms.  I would use Modula-3 terms, since
its object-oriented semantics are closer to those of Python than C++, but I
expect that few readers have heard of it.)

.. _tut-object:

A Word About Names and Objects
==============================

Objects have individuality, and multiple names (in multiple scopes) can be bound
to the same object.  This is known as aliasing in other languages.  This is
usually not appreciated on a first glance at Python, and can be safely ignored
when dealing with immutable basic types (numbers, strings, tuples).  However,
aliasing has a possibly surprising effect on the semantics of Python code
involving mutable objects such as lists, dictionaries, and most other types.
This is usually used to the benefit of the program, since aliases behave like
pointers in some respects.  For example, passing an object is cheap since only a
pointer is passed by the implementation; and if a function modifies an object
passed as an argument, the caller will see the change --- this eliminates the
need for two different argument passing mechanisms as in Pascal.

.. _tut-scopes:

Python Scopes and Namespaces
============================

Before introducing classes, I first have to tell you something about Python's
scope rules.  Class definitions play some neat tricks with namespaces, and you
need to know how scopes and namespaces work to fully understand what's going on.
Incidentally, knowledge about this subject is useful for any advanced Python
programmer.

Let's begin with some definitions.

A *namespace* is a mapping from names to objects.  Most namespaces are currently
implemented as Python dictionaries, but that's normally not noticeable in any
way (except for performance), and it may change in the future.  Examples of
namespaces are: the set of built-in names (containing functions such as :func:`abs`, and
built-in exception names); the global names in a module; and the local names in
a function invocation.  In a sense the set of attributes of an object also form
a namespace.  The important thing to know about namespaces is that there is
absolutely no relation between names in different namespaces; for instance, two
different modules may both define a function ``maximize`` without confusion ---
users of the modules must prefix it with the module name.

By the way, I use the word *attribute* for any name following a dot --- for
example, in the expression ``z.real``, ``real`` is an attribute of the object
``z``.  Strictly speaking, references to names in modules are attribute
references: in the expression ``modname.funcname``, ``modname`` is a module
object and ``funcname`` is an attribute of it.  In this case there happens to be
a straightforward mapping between the module's attributes and the global names
defined in the module: they share the same namespace!  [#]_

Attributes may be read-only or writable.  In the latter case, assignment to
attributes is possible.  Module attributes are writable: you can write
``modname.the_answer = 42``.  Writable attributes may also be deleted with the
:keyword:`del` statement.  For example, ``del modname.the_answer`` will remove
the attribute :attr:`!the_answer` from the object named by ``modname``.

Namespaces are created at different moments and have different lifetimes.  The
namespace containing the built-in names is created when the Python interpreter
starts up, and is never deleted.  The global namespace for a module is created
when the module definition is read in; normally, module namespaces also last
until the interpreter quits.  The statements executed by the top-level
invocation of the interpreter, either read from a script file or interactively,
are considered part of a module called :mod:`__main__`, so they have their own
global namespace.  (The built-in names actually also live in a module; this is
called :mod:`builtins`.)

The local namespace for a function is created when the function is called, and
deleted when the function returns or raises an exception that is not handled
within the function.  (Actually, forgetting would be a better way to describe
what actually happens.)  Of course, recursive invocations each have their own
local namespace.

A *scope* is a textual region of a Python program where a namespace is directly
accessible.  "Directly accessible" here means that an unqualified reference to a
name attempts to find the name in the namespace.

Although scopes are determined statically, they are used dynamically. At any
time during execution, there are 3 or 4 nested scopes whose namespaces are
directly accessible:

* the innermost scope, which is searched first, contains the local names
* the scopes of any enclosing functions, which are searched starting with the
  nearest enclosing scope, contain non-local, but also non-global names
* the next-to-last scope contains the current module's global names
* the outermost scope (searched last) is the namespace containing built-in names

If a name is declared global, then all references and assignments go directly to
the next-to-last scope containing the module's global names.  To rebind variables
found outside of the innermost scope, the :keyword:`nonlocal` statement can be
used; if not declared nonlocal, those variables are read-only (an attempt to
write to such a variable will simply create a *new* local variable in the
innermost scope, leaving the identically named outer variable unchanged).

Usually, the local scope references the local names of the (textually) current
function.  Outside functions, the local scope references the same namespace as
the global scope: the module's namespace. Class definitions place yet another
namespace in the local scope.

It is important to realize that scopes are determined textually: the global
scope of a function defined in a module is that module's namespace, no matter
from where or by what alias the function is called.  On the other hand, the
actual search for names is done dynamically, at run time --- however, the
language definition is evolving towards static name resolution, at "compile"
time, so don't rely on dynamic name resolution!  (In fact, local variables are
already determined statically.)

A special quirk of Python is that -- if no :keyword:`global` or :keyword:`nonlocal`
statement is in effect -- assignments to names always go into the innermost scope.
Assignments do not copy data --- they just bind names to objects.  The same is true
for deletions: the statement ``del x`` removes the binding of ``x`` from the
namespace referenced by the local scope.  In fact, all operations that introduce
new names use the local scope: in particular, :keyword:`import` statements and
function definitions bind the module or function name in the local scope.

The :keyword:`global` statement can be used to indicate that particular
variables live in the global scope and should be rebound there; the
:keyword:`nonlocal` statement indicates that particular variables live in
an enclosing scope and should be rebound there.

.. _tut-scopeexample:

Scopes and Namespaces Example
-----------------------------

This is an example demonstrating how to reference the different scopes and
namespaces, and how :keyword:`global` and :keyword:`nonlocal` affect variable
binding::

   def scope_test():
       def do_local():
           spam = "local spam"

       def do_nonlocal():
           nonlocal spam
           spam = "nonlocal spam"

       def do_global():
           global spam
           spam = "global spam"

       spam = "test spam"
       do_local()
       print("After local assignment:", spam)
       do_nonlocal()
       print("After nonlocal assignment:", spam)
       do_global()
       print("After global assignment:", spam)

   scope_test()
   print("In global scope:", spam)

The output of the example code is:

.. code-block:: none

   After local assignment: test spam
   After nonlocal assignment: nonlocal spam
   After global assignment: nonlocal spam
   In global scope: global spam

Note how the *local* assignment (which is default) didn't change *scope_test*\'s
binding of *spam*.  The :keyword:`nonlocal` assignment changed *scope_test*\'s
binding of *spam*, and the :keyword:`global` assignment changed the module-level
binding.

You can also see that there was no previous binding for *spam* before the
:keyword:`global` assignment.

.. _tut-firstclasses:

A First Look at Classes
=======================

Classes introduce a little bit of new syntax, three new object types, and some
new semantics.

.. _tut-classdefinition:

Class Definition Syntax
-----------------------

The simplest form of class definition looks like this::

   class ClassName:
       <statement-1>
       .
       .
       .
       <statement-N>

Class definitions, like function definitions (:keyword:`def` statements) must be
executed before they have any effect.  (You could conceivably place a class
definition in a branch of an :keyword:`if` statement, or inside a function.)

In practice, the statements inside a class definition will usually be function
definitions, but other statements are allowed, and sometimes useful --- we'll
come back to this later.  The function definitions inside a class normally have
a peculiar form of argument list, dictated by the calling conventions for
methods --- again, this is explained later.

When a class definition is entered, a new namespace is created, and used as the
local scope --- thus, all assignments to local variables go into this new
namespace.  In particular, function definitions bind the name of the new
function here.

When a class definition is left normally (via the end), a *class object* is
created.  This is basically a wrapper around the contents of the namespace
created by the class definition; we'll learn more about class objects in the
next section.  The original local scope (the one in effect just before the class
definition was entered) is reinstated, and the class object is bound here to the
class name given in the class definition header (:class:`!ClassName` in the
example).

.. _tut-classobjects:

Class Objects
-------------

Class objects support two kinds of operations: attribute references and
instantiation.

*Attribute references* use the standard syntax used for all attribute references
in Python: ``obj.name``.  Valid attribute names are all the names that were in
the class's namespace when the class object was created.  So, if the class
definition looked like this::

   class MyClass:
       """A simple example class"""
       i = 12345

       def f(self):
           return 'hello world'

then ``MyClass.i`` and ``MyClass.f`` are valid attribute references, returning
an integer and a function object, respectively. Class attributes can also be
assigned to, so you can change the value of ``MyClass.i`` by assignment.
:attr:`~type.__doc__` is also a valid attribute, returning the docstring
belonging to the class: ``"A simple example class"``.

Class *instantiation* uses function notation.  Just pretend that the class
object is a parameterless function that returns a new instance of the class.
For example (assuming the above class)::

   x = MyClass()

creates a new *instance* of the class and assigns this object to the local
variable ``x``.

The instantiation operation ("calling" a class object) creates an empty object.
Many classes like to create objects with instances customized to a specific
initial state. Therefore a class may define a special method named
:meth:`~object.__init__`, like this::

   def __init__(self):
       self.data = []

When a class defines an :meth:`~object.__init__` method, class instantiation
automatically invokes :meth:`!__init__` for the newly created class instance.  So
in this example, a new, initialized instance can be obtained by::

   x = MyClass()

Of course, the :meth:`~object.__init__` method may have arguments for greater
flexibility.  In that case, arguments given to the class instantiation operator
are passed on to :meth:`!__init__`.  For example, ::

   >>> class Complex:
   ...     def __init__(self, realpart, imagpart):
   ...         self.r = realpart
   ...         self.i = imagpart
   ...
   >>> x = Complex(3.0, -4.5)
   >>> x.r, x.i
   (3.0, -4.5)

.. _tut-instanceobjects:

Instance Objects
----------------

Now what can we do with instance objects?  The only operations understood by
instance objects are attribute references.  There are two kinds of valid
attribute names: data attributes and methods.

*Data attributes* correspond to "instance variables" in Smalltalk, and to "data
members" in C++.  Data attributes need not be declared; like local variables,
they spring into existence when they are first assigned to.  For example, if
``x`` is the instance of :class:`!MyClass` created above, the following piece of
code will print the value ``16``, without leaving a trace::

   x.counter = 1
   while x.counter < 10:
       x.counter = x.counter * 2
   print(x.counter)
   del x.counter

The other kind of instance attribute reference is a *method*. A method is a
function that "belongs to" an object.

.. index:: pair: object; method

Valid method names of an instance object depend on its class.  By definition,
all attributes of a class that are function  objects define corresponding
methods of its instances.  So in our example, ``x.f`` is a valid method
reference, since ``MyClass.f`` is a function, but ``x.i`` is not, since
``MyClass.i`` is not.  But ``x.f`` is not the same thing as ``MyClass.f`` --- it
is a *method object*, not a function object.

.. _tut-methodobjects:

Method Objects
--------------

Usually, a method is called right after it is bound::

   x.f()

If ``x = MyClass()``, as above, this will return the string ``'hello world'``.
However, it is not necessary to call a method right away: ``x.f`` is a method
object, and can be stored away and called at a later time.  For example::

   xf = x.f
   while True:
       print(xf())

will continue to print ``hello world`` until the end of time.

What exactly happens when a method is called?  You may have noticed that
``x.f()`` was called without an argument above, even though the function
definition for :meth:`!f` specified an argument.  What happened to the argument?
Surely Python raises an exception when a function that requires an argument is
called without any --- even if the argument isn't actually used...

Actually, you may have guessed the answer: the special thing about methods is
that the instance object is passed as the first argument of the function.  In our
example, the call ``x.f()`` is exactly equivalent to ``MyClass.f(x)``.  In
general, calling a method with a list of *n* arguments is equivalent to calling
the corresponding function with an argument list that is created by inserting
the method's instance object before the first argument.

In general, methods work as follows.  When a non-data attribute
of an instance is referenced, the instance's class is searched.
If the name denotes a valid class attribute that is a function object,
references to both the instance object and the function object
are packed into a method object.  When the method object is called
with an argument list, a new argument list is constructed from the instance
object and the argument list, and the function object is called with this new
argument list.

.. _tut-class-and-instance-variables:

Class and Instance Variables
----------------------------

Generally speaking, instance variables are for data unique to each instance
and class variables are for attributes and methods shared by all instances
of the class::

    class Dog:

        kind = 'canine'         # class variable shared by all instances

        def __init__(self, name):
            self.name = name    # instance variable unique to each instance

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.kind                  # shared by all dogs
    'canine'
    >>> e.kind                  # shared by all dogs
    'canine'
    >>> d.name                  # unique to d
    'Fido'
    >>> e.name                  # unique to e
    'Buddy'

As discussed in :ref:`tut-object`, shared data can have possibly surprising
effects involving :term:`mutable` objects such as lists and dictionaries.
For example, the *tricks* list in the following code should not be used as a
class variable because just a single list would be shared by all *Dog*
instances::

    class Dog:

        tricks = []             # mistaken use of a class variable

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks                # unexpectedly shared by all dogs
    ['roll over', 'play dead']

Correct design of the class should use an instance variable instead::

    class Dog:

        def __init__(self, name):
            self.name = name
            self.tricks = []    # creates a new empty list for each dog

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks
    ['roll over']
    >>> e.tricks
    ['play dead']

.. _tut-remarks:

Random Remarks
==============

.. These should perhaps be placed more carefully...

If the same attribute name occurs in both an instance and in a class,
then attribute lookup prioritizes the instance::

    >>> class Warehouse:
    ...    purpose = 'storage'
    ...    region = 'west'
    ...
    >>> w1 = Warehouse()
    >>> print(w1.purpose, w1.region)
    storage west
    >>> w2 = Warehouse()
    >>> w2.region = 'east'
    >>> print(w2.purpose, w2.region)
    storage east

Data attributes may be referenced by methods as well as by ordinary users
("clients") of an object.  In other words, classes are not usable to implement
pure abstract data types.  In fact, nothing in Python makes it possible to
enforce data hiding --- it is all based upon convention.  (On the other hand,
the Python implementation, written in C, can completely hide implementation
details and control access to an object if necessary; this can be used by
extensions to Python written in C.)

Clients should use data attributes with care --- clients may mess up invariants
maintained by the methods by stamping on their data attributes.  Note that
clients may add data attributes of their own to an instance object without
affecting the validity of the methods, as long as name conflicts are avoided ---
again, a naming convention can save a lot of headaches here.

There is no shorthand for referencing data attributes (or other methods!) from
within methods.  I find that this actually increases the readability of methods:
there is no chance of confusing local variables and instance variables when
glancing through a method.

Often, the first argument of a method is called ``self``.  This is nothing more
than a convention: the name ``self`` has absolutely no special meaning to
Python.  Note, however, that by not following the convention your code may be
less readable to other Python programmers, and it is also conceivable that a
*class browser* program might be written that relies upon such a convention.

Any function object that is a class attribute defines a method for instances of
that class.  It is not necessary that the function definition is textually
enclosed in the class definition: assigning a function object to a local
variable in the class is also ok.  For example::

   # Function defined outside the class
   def f1(self, x, y):
       return min(x, x+y)

   class C:
       f = f1

       def g(self):
           return 'hello world'

       h = g

Now ``f``, ``g`` and ``h`` are all attributes of class :class:`!C` that refer to
function objects, and consequently they are all methods of instances of
:class:`!C` --- ``h`` being exactly equivalent to ``g``.  Note that this practice
usually only serves to confuse the reader of a program.

Methods may call other methods by using method attributes of the ``self``
argument::

   class Bag:
       def __init__(self):
           self.data = []

       def add(self, x):
           self.data.append(x)

       def addtwice(self, x):
           self.add(x)
           self.add(x)

Methods may reference global names in the same way as ordinary functions.  The
global scope associated with a method is the module containing its
definition.  (A class is never used as a global scope.)  While one
rarely encounters a good reason for using global data in a method, there are
many legitimate uses of the global scope: for one thing, functions and modules
imported into the global scope can be used by methods, as well as functions and
classes defined in it.  Usually, the class containing the method is itself
defined in this global scope, and in the next section we'll find some good
reasons why a method would want to reference its own class.

Each value is an object, and therefore has a *class* (also called its *type*).
It is stored as ``object.__class__``.

.. _tut-inheritance:

Inheritance
===========

Of course, a language feature would not be worthy of the name "class" without
supporting inheritance.  The syntax for a derived class definition looks like
this::

   class DerivedClassName(BaseClassName):
       <statement-1>
       .
       .
       .
       <statement-N>

The name :class:`!BaseClassName` must be defined in a
namespace accessible from the scope containing the
derived class definition.  In place of a base class name, other arbitrary
expressions are also allowed.  This can be useful, for example, when the base
class is defined in another module::

   class DerivedClassName(modname.BaseClassName):

Execution of a derived class definition proceeds the same as for a base class.
When the class object is constructed, the base class is remembered.  This is
used for resolving attribute references: if a requested attribute is not found
in the class, the search proceeds to look in the base class.  This rule is
applied recursively if the base class itself is derived from some other class.

There's nothing special about instantiation of derived classes:
``DerivedClassName()`` creates a new instance of the class.  Method references
are resolved as follows: the corresponding class attribute is searched,
descending down the chain of base classes if necessary, and the method reference
is valid if this yields a function object.

Derived classes may override methods of their base classes.  Because methods
have no special privileges when calling other methods of the same object, a
method of a base class that calls another method defined in the same base class
may end up calling a method of a derived class that overrides it.  (For C++
programmers: all methods in Python are effectively ``virtual``.)

An overriding method in a derived class may in fact want to extend rather than
simply replace the base class method of the same name. There is a simple way to
call the base class method directly: just call ``BaseClassName.methodname(self,
arguments)``.  This is occasionally useful to clients as well.  (Note that this
only works if the base class is accessible as ``BaseClassName`` in the global
scope.)

Python has two built-in functions that work with inheritance:

* Use :func:`isinstance` to check an instance's type: ``isinstance(obj, int)``
  will be ``True`` only if ``obj.__class__`` is :class:`int` or some class
  derived from :class:`int`.

* Use :func:`issubclass` to check class inheritance: ``issubclass(bool, int)``
  is ``True`` since :class:`bool` is a subclass of :class:`int`.  However,
  ``issubclass(float, int)`` is ``False`` since :class:`float` is not a
  subclass of :class:`int`.

.. _tut-multiple:

Multiple Inheritance
--------------------

Python supports a form of multiple inheritance as well.  A class definition with
multiple base classes looks like this::

   class DerivedClassName(Base1, Base2, Base3):
       <statement-1>
       .
       .
       .
       <statement-N>

For most purposes, in the simplest cases, you can think of the search for
attributes inherited from a parent class as depth-first, left-to-right, not
searching twice in the same class where there is an overlap in the hierarchy.
Thus, if an attribute is not found in :class:`!DerivedClassName`, it is searched
for in :class:`!Base1`, then (recursively) in the base classes of :class:`!Base1`,
and if it was not found there, it was searched for in :class:`!Base2`, and so on.

In fact, it is slightly more complex than that; the method resolution order
changes dynamically to support cooperative calls to :func:`super`.  This
approach is known in some other multiple-inheritance languages as
call-next-method and is more powerful than the super call found in
single-inheritance languages.

Dynamic ordering is necessary because all cases of multiple inheritance exhibit
one or more diamond relationships (where at least one of the parent classes
can be accessed through multiple paths from the bottommost class).  For example,
all classes inherit from :class:`object`, so any case of multiple inheritance
provides more than one path to reach :class:`object`.  To keep the base classes
from being accessed more than once, the dynamic algorithm linearizes the search
order in a way that preserves the left-to-right ordering specified in each
class, that calls each parent only once, and that is monotonic (meaning that a
class can be subclassed without affecting the precedence order of its parents).
Taken together, these properties make it possible to design reliable and
extensible classes with multiple inheritance.  For more detail, see
:ref:`python_2.3_mro`.

In some cases multiple inheritance is not allowed; see :ref:`multiple-inheritance`
for details.

.. _tut-private:

Private Variables
=================

"Private" instance variables that cannot be accessed except from inside an
object don't exist in Python.  However, there is a convention that is followed
by most Python code: a name prefixed with an underscore (e.g. ``_spam``) should
be treated as a non-public part of the API (whether it is a function, a method
or a data member).  It should be considered an implementation detail and subject
to change without notice.

.. index::
   pair: name; mangling

Since there is a valid use-case for class-private members (namely to avoid name
clashes of names with names defined by subclasses), there is limited support for
such a mechanism, called :dfn:`name mangling`.  Any identifier of the form
``__spam`` (at least two leading underscores, at most one trailing underscore)
is textually replaced with ``_classname__spam``, where ``classname`` is the
current class name with leading underscore(s) stripped.  This mangling is done
without regard to the syntactic position of the identifier, as long as it
occurs within the definition of a class.

.. seealso::

   The :ref:`private name mangling specifications <private-name-mangling>`
   for details and special cases.

Name mangling is helpful for letting subclasses override methods without
breaking intraclass method calls.  For example::

   class Mapping:
       def __init__(self, iterable):
           self.items_list = []
           self.__update(iterable)

       def update(self, iterable):
           for item in iterable:
               self.items_list.append(item)

       __update = update   # private copy of original update() method

   class MappingSubclass(Mapping):

       def update(self, keys, values):
           # provides new signature for update()
           # but does not break __init__()
           for item in zip(keys, values):
               self.items_list.append(item)

The above example would work even if ``MappingSubclass`` were to introduce a
``__update`` identifier since it is replaced with ``_Mapping__update`` in the
``Mapping`` class  and ``_MappingSubclass__update`` in the ``MappingSubclass``
class respectively.

Note that the mangling rules are designed mostly to avoid accidents; it still is
possible to access or modify a variable that is considered private.  This can
even be useful in special circumstances, such as in the debugger.

Notice that code passed to ``exec()`` or ``eval()`` does not consider the
classname of the invoking class to be the current class; this is similar to the
effect of the ``global`` statement, the effect of which is likewise restricted
to code that is byte-compiled together.  The same restriction applies to
``getattr()``, ``setattr()`` and ``delattr()``, as well as when referencing
``__dict__`` directly.

.. _tut-odds:

Odds and Ends
=============

Sometimes it is useful to have a data type similar to the Pascal "record" or C
"struct", bundling together a few named data items. The idiomatic approach
is to use :mod:`dataclasses` for this purpose::

    from dataclasses import dataclass

    @dataclass
    class Employee:
        name: str
        dept: str
        salary: int

::

    >>> john = Employee('john', 'computer lab', 1000)
    >>> john.dept
    'computer lab'
    >>> john.salary
    1000

A piece of Python code that expects a particular abstract data type can often be
passed a class that emulates the methods of that data type instead.  For
instance, if you have a function that formats some data from a file object, you
can define a class with methods :meth:`~io.TextIOBase.read` and
:meth:`~io.TextIOBase.readline` that get the
data from a string buffer instead, and pass it as an argument.

.. (Unfortunately, this technique has its limitations: a class can't define
   operations that are accessed by special syntax such as sequence subscripting
   or arithmetic operators, and assigning such a "pseudo-file" to sys.stdin will
   not cause the interpreter to read further input from it.)

:ref:`Instance method objects <instance-methods>` have attributes, too:
:attr:`m.__self__ <method.__self__>` is the instance
object with the method :meth:`!m`, and :attr:`m.__func__ <method.__func__>` is
the :ref:`function object <user-defined-funcs>`
corresponding to the method.

.. _tut-iterators:

Iterators
=========

By now you have probably noticed that most container objects can be looped over
using a :keyword:`for` statement::

   for element in [1, 2, 3]:
       print(element)
   for element in (1, 2, 3):
       print(element)
   for key in {'one':1, 'two':2}:
       print(key)
   for char in "123":
       print(char)
   for line in open("myfile.txt"):
       print(line, end='')

This style of access is clear, concise, and convenient.  The use of iterators
pervades and unifies Python.  Behind the scenes, the :keyword:`for` statement
calls :func:`iter` on the container object.  The function returns an iterator
object that defines the method :meth:`~iterator.__next__` which accesses
elements in the container one at a time.  When there are no more elements,
:meth:`~iterator.__next__` raises a :exc:`StopIteration` exception which tells the
:keyword:`!for` loop to terminate.  You can call the :meth:`~iterator.__next__` method
using the :func:`next` built-in function; this example shows how it all works::

   >>> s = 'abc'
   >>> it = iter(s)
   >>> it
   <str_iterator object at 0x10c90e650>
   >>> next(it)
   'a'
   >>> next(it)
   'b'
   >>> next(it)
   'c'
   >>> next(it)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       next(it)
   StopIteration

Having seen the mechanics behind the iterator protocol, it is easy to add
iterator behavior to your classes.  Define an :meth:`~container.__iter__` method which
returns an object with a :meth:`~iterator.__next__` method.  If the class
defines :meth:`!__next__`, then :meth:`!__iter__` can just return ``self``::

   class Reverse:
       """Iterator for looping over a sequence backwards."""
       def __init__(self, data):
           self.data = data
           self.index = len(data)

       def __iter__(self):
           return self

       def __next__(self):
           if self.index == 0:
               raise StopIteration
           self.index = self.index - 1
           return self.data[self.index]

::

   >>> rev = Reverse('spam')
   >>> iter(rev)
   <__main__.Reverse object at 0x00A1DB50>
   >>> for char in rev:
   ...     print(char)
   ...
   m
   a
   p
   s

.. _tut-generators:

Generators
==========

:term:`Generators <generator>` are a simple and powerful tool for creating iterators.  They
are written like regular functions but use the :keyword:`yield` statement
whenever they want to return data.  Each time :func:`next` is called on it, the
generator resumes where it left off (it remembers all the data values and which
statement was last executed).  An example shows that generators can be trivially
easy to create::

   def reverse(data):
       for index in range(len(data)-1, -1, -1):
           yield data[index]

::

   >>> for char in reverse('golf'):
   ...     print(char)
   ...
   f
   l
   o
   g

Anything that can be done with generators can also be done with class-based
iterators as described in the previous section.  What makes generators so
compact is that the :meth:`~iterator.__iter__` and :meth:`~generator.__next__` methods
are created automatically.

Another key feature is that the local variables and execution state are
automatically saved between calls.  This made the function easier to write and
much more clear than an approach using instance variables like ``self.index``
and ``self.data``.

In addition to automatic method creation and saving program state, when
generators terminate, they automatically raise :exc:`StopIteration`. In
combination, these features make it easy to create iterators with no more effort
than writing a regular function.

.. _tut-genexps:

Generator Expressions
=====================

Some simple generators can be coded succinctly as expressions using a syntax
similar to list comprehensions but with parentheses instead of square brackets.
These expressions are designed for situations where the generator is used right
away by an enclosing function.  Generator expressions are more compact but less
versatile than full generator definitions and tend to be more memory friendly
than equivalent list comprehensions.

Examples::

   >>> sum(i*i for i in range(10))                 # sum of squares
   285

   >>> xvec = [10, 20, 30]
   >>> yvec = [7, 5, 3]
   >>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
   260

   >>> unique_words = set(word for line in page  for word in line.split())

   >>> valedictorian = max((student.gpa, student.name) for student in graduates)

   >>> data = 'golf'
   >>> list(data[i] for i in range(len(data)-1, -1, -1))
   ['f', 'l', 'o', 'g']

   >>> x = [[1,2,3], [], [4, 5]]
   >>> g = (*i for i in x)
   >>> list(g)
   [1, 2, 3, 4, 5]

In most cases, generator expressions must be wrapped in parentheses.  As a
special case, however, when provided as the sole argument to a function (as in
the examples involving ``sum``, ``set``, ``max``, and ``list`` above), the
generator expression does not need to be wrapped in an additional set of
parentheses.  That is to say, the following two pieces of code are semantically
equivalent::

   >>> f(x for x in y)
   >>> f((x for x in y))

as are the following::

   >>> f(*x for x in y)
   >>> f((*x for x in y))

.. rubric:: Footnotes

.. [#] Except for one thing.  Module objects have a secret read-only attribute called
   :attr:`~object.__dict__` which returns the dictionary used to implement the module's
   namespace; the name ``__dict__`` is an attribute but not a global name.
   Obviously, using this violates the abstraction of namespace implementation, and
   should be restricted to things like post-mortem debuggers.

---
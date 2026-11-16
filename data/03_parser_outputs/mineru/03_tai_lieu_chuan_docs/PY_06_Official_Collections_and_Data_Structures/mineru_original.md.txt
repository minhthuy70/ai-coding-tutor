# Official Python Documentation: Collections, Heap Queue and Bisect Algorithms

## :mod:`!collections` --- Container datatypes

    :synopsis: Container datatypes

**Source code:** :source:`Lib/collections/__init__.py`

    from collections import *
    import itertools
    __name__ = '<doctest>'

--------------

This module implements specialized container datatypes providing alternatives to
Python's general purpose built-in containers, `class`, `class`,
`class`, and `class`.

=====================   ====================================================================
`namedtuple()`      factory function for creating tuple subclasses with named fields
`class`          list-like container with fast appends and pops on either end
`class`       dict-like class for creating a single view of multiple mappings
`class`        dict subclass for counting `term` objects
`class`    dict subclass that remembers the order entries were added
`class`    dict subclass that calls a factory function to supply missing values
`class`       wrapper around dictionary objects for easier dict subclassing
`class`       wrapper around list objects for easier list subclassing
`class`     wrapper around string objects for easier string subclassing
=====================   ====================================================================

### :class:`ChainMap` objects

A `class` class is provided for quickly linking a number of mappings
so they can be treated as a single unit.  It is often much faster than creating
a new dictionary and running multiple `dict.update()` calls.

The class can be used to simulate nested scopes and is useful in templating.

### Class: `ChainMap(*maps)`

    A `class` groups multiple dicts or other mappings together to
    create a single, updateable view.  If no *maps* are specified, a single empty
    dictionary is provided so that a new chain always has at least one mapping.

    The underlying mappings are stored in a list.  That list is public and can
    be accessed or updated using the *maps* attribute.  There is no other state.

    Lookups search the underlying mappings successively until a key is found.  In
    contrast, writes, updates, and deletions only operate on the first mapping.

    A `class` incorporates the underlying mappings by reference.  So, if
    one of the underlying mappings gets updated, those changes will be reflected
    in `class`.

    All of the usual dictionary methods are supported.  In addition, there is a
    *maps* attribute, a method for creating new subcontexts, and a property for
    accessing all but the first mapping:

    .. attribute:: maps

        A user updateable list of mappings.  The list is ordered from
        first-searched to last-searched.  It is the only stored state and can
        be modified to change which mappings are searched.  The list should
        always contain at least one mapping.

    .. method:: new_child(m=None, **kwargs)

        Returns a new `class` containing a new map followed by
        all of the maps in the current instance.  If `m` is specified,
        it becomes the new map at the front of the list of mappings; if not
        specified, an empty dict is used, so that a call to `d.new_child()`
        is equivalent to: `ChainMap({}, *d.maps)`. If any keyword arguments
        are specified, they update passed map or new empty dict. This method
        is used for creating subcontexts that can be updated without altering
        values in any of the parent mappings.

        .. versionchanged:: 3.4
           The optional `m` parameter was added.

        .. versionchanged:: 3.10
           Keyword arguments support was added.

    .. attribute:: parents

        Property returning a new `class` containing all of the maps in
        the current instance except the first one.  This is useful for skipping
        the first map in the search.  Use cases are similar to those for the
        :keyword:`nonlocal` keyword used in :term:`nested scopes <nested
        scope>`.  The use cases also parallel those for the built-in
        `super()` function.  A reference to `d.parents` is equivalent to:
        `ChainMap(*d.maps[1:])`.

    Note, the iteration order of a `class` is determined by
scanning the mappings last to first

```python

     >>> baseline = {'music': 'bach', 'art': 'rembrandt'}
     >>> adjustments = {'art': 'van gogh', 'opera': 'carmen'}
     >>> list(ChainMap(adjustments, baseline))
     ['music', 'art', 'opera']

 This gives the same ordering as a series of :meth:`dict.update` calls
 starting with the last mapping::

     >>> combined = baseline.copy()
     >>> combined.update(adjustments)
     >>> list(combined)
     ['music', 'art', 'opera']

 .. versionchanged:: 3.9
    Added support for ``|`` and ``|=`` operators, specified in :pep:`584`.

```

.. seealso

```python

* The `MultiContext class
  <https://github.com/enthought/codetools/blob/4.0.0/codetools/contexts/multi_context.py>`_
  in the Enthought `CodeTools package
  <https://github.com/enthought/codetools>`_ has options to support
  writing to any mapping in the chain.

* Django's `Context class
  <https://github.com/django/django/blob/main/django/template/context.py>`_
  for templating is a read-only chain of mappings.  It also features
  pushing and popping of contexts similar to the
  :meth:`~collections.ChainMap.new_child` method and the
  :attr:`~collections.ChainMap.parents` property.

* The `Nested Contexts recipe
  <https://code.activestate.com/recipes/577434-nested-contexts-a-chain-of-mapping-objects/>`_ has options to control
  whether writes and other mutations apply only to the first mapping or to
  any mapping in the chain.

* A `greatly simplified read-only version of Chainmap
  <https://code.activestate.com/recipes/305268/>`_.

```

### :class:`ChainMap` Examples and Recipes

This section shows various approaches to working with chained maps.

Example of simulating Python's internal lookup chain

```python

     import builtins
     pylookup = ChainMap(locals(), globals(), vars(builtins))

```

Example of letting user specified command-line arguments take precedence over
environment variables which in turn take precedence over default values

```python

     import os, argparse

     defaults = {'color': 'red', 'user': 'guest'}

     parser = argparse.ArgumentParser()
     parser.add_argument('-u', '--user')
     parser.add_argument('-c', '--color')
     namespace = parser.parse_args()
     command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

     combined = ChainMap(command_line_args, os.environ, defaults)
     print(combined['color'])
     print(combined['user'])

```

Example patterns for using the `class` class to simulate nested
contexts

```python

     c = ChainMap()        # Create root context
     d = c.new_child()     # Create nested child context
     e = c.new_child()     # Child of c, independent from d
     e.maps[0]             # Current context dictionary -- like Python's locals()
     e.maps[-1]            # Root context -- like Python's globals()
     e.parents             # Enclosing context chain -- like Python's nonlocals

     d['x'] = 1            # Set value in current context
     d['x']                # Get first key in the chain of contexts
     del d['x']            # Delete from current context
     list(d)               # All nested values
     k in d                # Check all nested values
     len(d)                # Number of nested values
     d.items()             # All nested items
     dict(d)               # Flatten into a regular dictionary

```

The `class` class only makes updates (writes and deletions) to the
first mapping in the chain while lookups will search the full chain.  However,
if deep writes and deletions are desired, it is easy to make a subclass that
updates keys found deeper in the chain

```python

 class DeepChainMap(ChainMap):
     'Variant of ChainMap that allows direct updates to inner scopes'

     def __setitem__(self, key, value):
         for mapping in self.maps:
             if key in mapping:
                 mapping[key] = value
                 return
         self.maps[0][key] = value

     def __delitem__(self, key):
         for mapping in self.maps:
             if key in mapping:
                 del mapping[key]
                 return
         raise KeyError(key)

 >>> d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
 >>> d['lion'] = 'orange'         # update an existing key two levels down
 >>> d['snake'] = 'red'           # new keys get added to the topmost dict
 >>> del d['elephant']            # remove an existing key one level down
 >>> d                            # display result
 DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})

```

### :class:`Counter` objects

A counter tool is provided to support convenient and rapid tallies.
For example

```python

 >>> # Tally occurrences of words in a list
 >>> cnt = Counter()
 >>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
 ...     cnt[word] += 1
 ...
 >>> cnt
 Counter({'blue': 3, 'red': 2, 'green': 1})

 >>> # Find the ten most common words in Hamlet
 >>> import re
 >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
 >>> Counter(words).most_common(10)
 [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
  ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

```

### Class: `Counter(**kwargs)`

           Counter(iterable, /, **kwargs)
           Counter(mapping, /, **kwargs)

    A `class` is a `class` subclass for counting `term` objects.
    It is a collection where elements are stored as dictionary keys
    and their counts are stored as dictionary values.  Counts are allowed to be
    any integer value including zero or negative counts.  The `class`
    class is similar to bags or multisets in other languages.

    Elements are counted from an *iterable* or initialized from another
    *mapping* (or counter):

        >>> c = Counter()                           # a new, empty counter
        >>> c = Counter('gallahad')                 # a new counter from an iterable
        >>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
        >>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

    Counter objects have a dictionary interface except that they return a zero
    count for missing items instead of raising a `exc`:

        >>> c = Counter(['eggs', 'ham'])
        >>> c['bacon']                              # count of a missing element is zero
        0

    Setting a count to zero does not remove an element from a counter.
    Use `del` to remove it entirely:

        >>> c['sausage'] = 0                        # counter entry with a zero count
        >>> del c['sausage']                        # del actually removes the entry

    Counters maintain insertion order internally but display from most common to
    least common when possible:

        >>> c = Counter(a=1, b=2, c=3)
        >>> c                                       # display most common to least
        Counter({'c': 3, 'b': 2, 'a': 1})
        >>> list(c.items())                         # original insertion order
        [('a', 1), ('b', 2), ('c', 3)]

    .. versionadded:: 3.1

    .. versionchanged:: 3.7 As a `class` subclass, `class`
       inherited the capability to remember insertion order.  Math operations
       on *Counter* objects also preserve order.  Results are ordered
       according to when an element is first encountered in the left operand
       and then by the order encountered in the right operand.

    Counter objects support additional methods beyond those available for all
    dictionaries:

    .. method:: elements()

        Return an iterator over elements repeating each as many times as its
        count.  Elements are returned in the order first encountered. If an
        element's count is less than one, `elements()` will ignore it.

            >>> c = Counter(a=4, b=2, c=0, d=-2)
            >>> sorted(c.elements())
            ['a', 'a', 'a', 'a', 'b', 'b']

    .. method:: most_common(n=None)

        Return a list of the *n* most common elements and their counts from the
        most common to the least.  If *n* is omitted or `None`,
        `most_common()` returns *all* elements in the counter.
        Elements with equal counts are ordered in the order first encountered:

            >>> Counter('abracadabra').most_common(3)
            [('a', 5), ('b', 2), ('r', 2)]

    .. method:: subtract(**kwargs)
                subtract(iterable, /, **kwargs)
                subtract(mapping, /, **kwargs)

        Elements are subtracted from an *iterable* or from another *mapping*
        (or counter).  Like `dict.update()` but subtracts counts instead
        of replacing them.  Both inputs and outputs may be zero or negative.

            >>> c = Counter(a=4, b=2, c=0, d=-2)
            >>> d = Counter(a=1, b=2, c=3, d=4)
            >>> c.subtract(d)
            >>> c
            Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

        .. versionadded:: 3.2

    .. method:: total()

        Compute the sum of the counts.

            >>> c = Counter(a=10, b=5, c=0)
            >>> c.total()
            15

        .. versionadded:: 3.10

    The usual dictionary methods are available for `class` objects
    except for these two which work differently for counters:

    .. method:: fromkeys(iterable)

        This class method is not implemented for `class` objects.

    .. method:: update(**kwargs)
                update(iterable, /, **kwargs)
                update(mapping, /, **kwargs)

        Elements are counted from an *iterable* or added-in from another
        *mapping* (or counter).  Like `dict.update()` but adds counts
        instead of replacing them.  Also, the *iterable* is expected to be a
        sequence of elements, not a sequence of `(key, value)` pairs.

Counters support rich comparison operators for equality, subset, and
superset relationships: `==`, `!=`, `<`, `<=`, `>`, `>=`.
All of those tests treat missing elements as having zero counts so that
`Counter(a=1) == Counter(a=1, b=0)` returns true.

   Rich comparison operations were added.

   In equality tests, missing elements are treated as having zero counts.
   Formerly, `Counter(a=3)` and `Counter(a=3, b=0)` were considered
   distinct.

Common patterns for working with :class:`Counter` objects

```python

 c.total()                       # total of all counts
 c.clear()                       # reset all counts
 list(c)                         # list unique elements
 set(c)                          # convert to a set
 dict(c)                         # convert to a regular dictionary
 c.items()                       # access the (elem, cnt) pairs
 Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
 c.most_common()[:-n-1:-1]       # n least common elements
 +c                              # remove zero and negative counts

```

Several mathematical operations are provided for combining `class`
objects to produce multisets (counters that have counts greater than zero).
Addition and subtraction combine counters by adding or subtracting the counts
of corresponding elements.  Intersection and union return the minimum and
maximum of corresponding counts.  Symmetric difference returns the difference
between the maximum and minimum of the corresponding counts. Equality and
inclusion compare corresponding counts.  Each operation can accept inputs
with signed counts, but the output will exclude results with counts of zero
or below.

.. doctest

```python

 >>> c = Counter(a=3, b=1)
 >>> d = Counter(a=1, b=2)
 >>> c + d                       # add two counters together:  c[x] + d[x]
 Counter({'a': 4, 'b': 3})
 >>> c - d                       # subtract (keeping only positive counts)
 Counter({'a': 2})
 >>> c & d                       # intersection:  min(c[x], d[x])
 Counter({'a': 1, 'b': 1})
 >>> c | d                       # union:  max(c[x], d[x])
 Counter({'a': 3, 'b': 2})
 >>> c ^ d                       # max(c[x], d[x]) - min(c[x], d[x])
 Counter({'a': 2, 'b': 1})
 >>> c == d                      # equality:  c[x] == d[x]
 False
 >>> c <= d                      # inclusion:  c[x] <= d[x]
 False

```

Unary addition and subtraction are shortcuts for adding an empty counter
or subtracting from an empty counter.

    >>> c = Counter(a=2, b=-4)
    >>> +c
    Counter({'a': 2})
    >>> -c
    Counter({'b': 4})

    Added support for unary plus, unary minus, and in-place multiset operations.

    Added support for the symmetric difference multiset operation, `c ^ d`.

.. note

```python

 Counters were primarily designed to work with positive integers to represent
 running counts; however, care was taken to not unnecessarily preclude use
 cases needing other types or negative values.  To help with those use cases,
 this section documents the minimum range and type restrictions.

 * The :class:`Counter` class itself is a dictionary subclass with no
   restrictions on its keys and values.  The values are intended to be numbers
   representing counts, but you *could* store anything in the value field.

 * The :meth:`~Counter.most_common` method requires only that the values be orderable.

 * For in-place operations such as ``c[key] += 1``, the value type need only
   support addition and subtraction.  So fractions, floats, and decimals would
   work and negative values are supported.  The same is also true for
   :meth:`~Counter.update` and :meth:`~Counter.subtract` which allow negative and zero values
   for both inputs and outputs.

 * The multiset methods are designed only for use cases with positive values.
   The inputs may be negative or zero, but only outputs with positive values
   are created.  There are no type restrictions, but the value type needs to
   support addition, subtraction, and comparison.

 * The :meth:`~Counter.elements` method requires integer counts.  It ignores zero and
   negative counts.

```

.. seealso

```python

* `Bag class <https://www.gnu.org/software/smalltalk/manual-base/html_node/Bag.html>`_
  in Smalltalk.

* Wikipedia entry for `Multisets <https://en.wikipedia.org/wiki/Multiset>`_.

* `C++ multisets <http://www.java2s.com/Tutorial/Cpp/0380__set-multiset/Catalog0380__set-multiset.htm>`_
  tutorial with examples.

* For mathematical operations on multisets and their use cases, see
  *Knuth, Donald. The Art of Computer Programming Volume II,
  Section 4.6.3, Exercise 19*.

* To enumerate all distinct multisets of a given size over a given set of
  elements, see :func:`itertools.combinations_with_replacement`::

     map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC

```

### :class:`deque` objects

### Class: `deque([iterable, [maxlen]])`

    Returns a new deque object initialized left-to-right (using `append()`) with
    data from *iterable*.  If *iterable* is not specified, the new deque is empty.

    Deques are a generalization of stacks and queues (the name is pronounced "deck"
    and is short for "double-ended queue").  Deques support thread-safe, memory
    efficient appends and pops from either side of the deque with approximately the
    same *O*\ (1) performance in either direction.

    Though `class` objects support similar operations, they are optimized for
    fast fixed-length operations and incur *O*\ (*n*) memory movement costs for
    `pop(0)` and `insert(0, v)` operations which change both the size and
    position of the underlying data representation.

    If *maxlen* is not specified or is `None`, deques may grow to an
    arbitrary length.  Otherwise, the deque is bounded to the specified maximum
    length.  Once a bounded length deque is full, when new items are added, a
    corresponding number of items are discarded from the opposite end.  Bounded
    length deques provide functionality similar to the `tail` filter in
    Unix. They are also useful for tracking transactions and other pools of data
    where only the most recent activity is of interest.

    Deques are `ref` over the type of their contents.

    Deque objects support the following methods:

    .. method:: append(item, /)

        Add *item* to the right side of the deque.

    .. method:: appendleft(item, /)

        Add *item* to the left side of the deque.

    .. method:: clear()

        Remove all elements from the deque leaving it with length 0.

    .. method:: copy()

        Create a shallow copy of the deque.

        .. versionadded:: 3.5

    .. method:: count(value, /)

        Count the number of deque elements equal to *value*.

        .. versionadded:: 3.2

    .. method:: extend(iterable, /)

        Extend the right side of the deque by appending elements from the iterable
        argument.

    .. method:: extendleft(iterable, /)

        Extend the left side of the deque by appending elements from *iterable*.
        Note, the series of left appends results in reversing the order of
        elements in the iterable argument.

    .. method:: index(value[, start[, stop]])

        Return the position of *value* in the deque (at or after index *start*
        and before index *stop*).  Returns the first match or raises
        `exc` if not found.

        .. versionadded:: 3.5

    .. method:: insert(index, value, /)

        Insert *value* into the deque at position *index*.

        If the insertion would cause a bounded deque to grow beyond *maxlen*,
        an `exc` is raised.

        .. versionadded:: 3.5

    .. method:: pop()

        Remove and return an element from the right side of the deque. If no
        elements are present, raises an `exc`.

    .. method:: popleft()

        Remove and return an element from the left side of the deque. If no
        elements are present, raises an `exc`.

    .. method:: remove(value, /)

        Remove the first occurrence of *value*.  If not found, raises a
        `exc`.

    .. method:: reverse()

        Reverse the elements of the deque in-place and then return `None`.

        .. versionadded:: 3.2

    .. method:: rotate(n=1, /)

        Rotate the deque *n* steps to the right.  If *n* is negative, rotate
        to the left.

        When the deque is not empty, rotating one step to the right is equivalent
        to `d.appendleft(d.pop())`, and rotating one step to the left is
        equivalent to `d.append(d.popleft())`.

    Deque objects also provide one read-only attribute:

    .. attribute:: maxlen

        Maximum size of a deque or `None` if unbounded.

        .. versionadded:: 3.1

In addition to the above, deques support iteration, pickling, `len(d)`,
`reversed(d)`, `copy.copy(d)`, `copy.deepcopy(d)`, membership testing with
the :keyword:`in` operator, and subscript references such as `d[0]` to access
the first element.  Indexed access is *O*\ (1) at both ends but slows to *O*\ (*n*) in
the middle.  For fast random access, use lists instead.

Starting in version 3.5, deques support `__add__()`, `__mul__()`,
and `__imul__()`.

Example:

.. doctest

```python

 >>> from collections import deque
 >>> d = deque('ghi')                 # make a new deque with three items
 >>> for elem in d:                   # iterate over the deque's elements
 ...     print(elem.upper())
 G
 H
 I

 >>> d.append('j')                    # add a new entry to the right side
 >>> d.appendleft('f')                # add a new entry to the left side
 >>> d                                # show the representation of the deque
 deque(['f', 'g', 'h', 'i', 'j'])

 >>> d.pop()                          # return and remove the rightmost item
 'j'
 >>> d.popleft()                      # return and remove the leftmost item
 'f'
 >>> list(d)                          # list the contents of the deque
 ['g', 'h', 'i']
 >>> d[0]                             # peek at leftmost item
 'g'
 >>> d[-1]                            # peek at rightmost item
 'i'

 >>> list(reversed(d))                # list the contents of a deque in reverse
 ['i', 'h', 'g']
 >>> 'h' in d                         # search the deque
 True
 >>> d.extend('jkl')                  # add multiple elements at once
 >>> d
 deque(['g', 'h', 'i', 'j', 'k', 'l'])
 >>> d.rotate(1)                      # right rotation
 >>> d
 deque(['l', 'g', 'h', 'i', 'j', 'k'])
 >>> d.rotate(-1)                     # left rotation
 >>> d
 deque(['g', 'h', 'i', 'j', 'k', 'l'])

 >>> deque(reversed(d))               # make a new deque in reverse order
 deque(['l', 'k', 'j', 'i', 'h', 'g'])
 >>> d.clear()                        # empty the deque
 >>> d.pop()                          # cannot pop from an empty deque
 Traceback (most recent call last):
     File "<pyshell#6>", line 1, in -toplevel-
         d.pop()
 IndexError: pop from an empty deque

 >>> d.extendleft('abc')              # extendleft() reverses the input order
 >>> d
 deque(['c', 'b', 'a'])

```

### :class:`deque` Recipes

This section shows various approaches to working with deques.

Bounded length deques provide functionality similar to the `tail` filter
in Unix

```python

 def tail(filename, n=10):
     'Return the last n lines of a file'
     with open(filename) as f:
         return deque(f, n)

```

Another approach to using deques is to maintain a sequence of recently
added elements by appending to the right and popping to the left

```python

 def moving_average(iterable, n=3):
     # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
     # https://en.wikipedia.org/wiki/Moving_average
     it = iter(iterable)
     d = deque(itertools.islice(it, n-1))
     d.appendleft(0)
     s = sum(d)
     for elem in it:
         s += elem - d.popleft()
         d.append(elem)
         yield s / n

```

A `round-robin scheduler
<https://en.wikipedia.org/wiki/Round-robin_scheduling>`_ can be implemented with
input iterators stored in a `class`.  Values are yielded from the active
iterator in position zero.  If that iterator is `term`, it can be removed
with `deque.popleft()`; otherwise, it can be cycled back to the end with
the :meth:`~deque.rotate` method

```python

 def roundrobin(*iterables):
     "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
     iterators = deque(map(iter, iterables))
     while iterators:
         try:
             while True:
                 yield next(iterators[0])
                 iterators.rotate(-1)
         except StopIteration:
             # Remove an exhausted iterator.
             iterators.popleft()

```

The `deque.rotate()` method provides a way to implement `class` slicing and
deletion.  For example, a pure Python implementation of `del d[n]` relies on
the ``rotate()`` method to position elements to be popped

```python

 def delete_nth(d, n):
     d.rotate(-n)
     d.popleft()
     d.rotate(n)

```

To implement `class` slicing, use a similar approach applying
`deque.rotate()` to bring a target element to the left side of the deque. Remove
old entries with `deque.popleft()`, add new entries with `deque.extend()`, and then
reverse the rotation.
With minor variations on that approach, it is easy to implement Forth style
stack manipulations such as `dup`, `drop`, `swap`, `over`, `pick`,
`rot`, and `roll`.

### :class:`defaultdict` objects

### Class: `defaultdict(default_factory=None, /, **kwargs)`

           defaultdict(default_factory, mapping, /, **kwargs)
           defaultdict(default_factory, iterable, /, **kwargs)

    Return a new dictionary-like object.  `class` is a subclass of the
    built-in `class` class.  It overrides one method and adds one writable
    instance variable.  The remaining functionality is the same as for the
    `class` class and is not documented here.

    The first argument provides the initial value for the :attr:`default_factory`
    attribute; it defaults to `None`. All remaining arguments are treated the same
    as if they were passed to the `class` constructor, including keyword
    arguments.

    `class`\s are `ref` over two types,
    signifying (respectively) the types of the dictionary's keys and values.

    `class` objects support the following method in addition to the
    standard `class` operations:

    .. method:: __missing__(key, /)

        If the :attr:`default_factory` attribute is `None`, this raises a
        `exc` exception with the *key* as argument.

        If :attr:`default_factory` is not `None`, it is called without arguments
        to provide a default value for the given *key*, this value is inserted in
        the dictionary for the *key*, and returned.

        If calling :attr:`default_factory` raises an exception this exception is
        propagated unchanged.

        This method is called by the `object.__getitem__()` method of the
        `class` class when the requested key is not found; whatever it
        returns or raises is then returned or raised by `object.__getitem__()`.

        Note that `__missing__()` is *not* called for any operations besides
        `object.__getitem__()`. This means that `dict.get()` will, like
        normal dictionaries, return `None` as a default rather than using
        :attr:`default_factory`.

    `class` objects support the following instance variable:

    .. attribute:: default_factory

        This attribute is used by the `defaultdict.__missing__()` method;
        it is initialized from the first argument to the constructor, if present,
        or to `None`, if absent.

    .. versionchanged:: 3.9
       Added merge (`|`) and update (`|=`) operators, specified in
       `pep`.

### :class:`defaultdict` Examples

Using `class` as the :attr:`~defaultdict.default_factory`, it is easy to group a
sequence of key-value pairs into a dictionary of lists:

    >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    >>> d = defaultdict(list)
    >>> for k, v in s:
    ...     d[k].append(v)
    ...
    >>> sorted(d.items())
    [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

When each key is encountered for the first time, it is not already in the
mapping; so an entry is automatically created using the :attr:`~defaultdict.default_factory`
function which returns an empty `class`.  The `list.append()`
operation then attaches the value to the new list.  When keys are encountered
again, the look-up proceeds normally (returning the list for that key) and the
`list.append()` operation adds another value to the list. This technique is
simpler and faster than an equivalent technique using `dict.setdefault()`:

    >>> d = {}
    >>> for k, v in s:
    ...     d.setdefault(k, []).append(v)
    ...
    >>> sorted(d.items())
    [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

Setting the :attr:`~defaultdict.default_factory` to `class` makes the
`class` useful for counting (like a bag or multiset in other
languages):

    >>> s = 'mississippi'
    >>> d = defaultdict(int)
    >>> for k in s:
    ...     d[k] += 1
    ...
    >>> sorted(d.items())
    [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

When a letter is first encountered, it is missing from the mapping, so the
:attr:`~defaultdict.default_factory` function calls `int()` to supply a default count of
zero.  The increment operation then builds up the count for each letter.

The function `int()` which always returns zero is just a special case of
constant functions.  A faster and more flexible way to create constant functions
is to use a lambda function which can supply any constant value (not just
zero):

    >>> def constant_factory(value):
    ...     return lambda: value
    ...
    >>> d = defaultdict(constant_factory('<missing>'))
    >>> d.update(name='John', action='ran')
    >>> '%(name)s %(action)s to %(object)s' % d
    'John ran to <missing>'

Setting the :attr:`~defaultdict.default_factory` to `class` makes the
`class` useful for building a dictionary of sets:

    >>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    >>> d = defaultdict(set)
    >>> for k, v in s:
    ...     d[k].add(v)
    ...
    >>> sorted(d.items())
    [('blue', {2, 4}), ('red', {1, 3})]

### :func:`namedtuple` Factory Function for Tuples with Named Fields

Named tuples assign meaning to each position in a tuple and allow for more readable,
self-documenting code.  They can be used wherever regular tuples are used, and
they add the ability to access fields by name instead of position index.

### Function: `namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`

    Returns a new tuple subclass named *typename*.  The new subclass is used to
    create tuple-like objects that have fields accessible by attribute lookup as
    well as being indexable and iterable.  Instances of the subclass also have a
    helpful docstring (with *typename* and *field_names*) and a helpful
    `object.__repr__()` method which lists the tuple contents in a `name=value`
    format.

    The *field_names* are a sequence of strings such as `['x', 'y']`.
    Alternatively, *field_names* can be a single string with each fieldname
    separated by whitespace and/or commas, for example `'x y'` or `'x, y'`.

    Any valid Python identifier may be used for a fieldname except for names
    starting with an underscore.  Valid identifiers consist of letters, digits,
    and underscores but do not start with a digit or underscore and cannot be
    a `mod` such as *class*, *for*, *return*, *global*, *pass*,
    or *raise*.

    If *rename* is true, invalid fieldnames are automatically replaced
    with positional names.  For example, `['abc', 'def', 'ghi', 'abc']` is
    converted to `['abc', '_1', 'ghi', '_3']`, eliminating the keyword
    `def` and the duplicate fieldname `abc`.

    *defaults* can be `None` or an `term` of default values.
    Since fields with a default value must come after any fields without a
    default, the *defaults* are applied to the rightmost parameters.  For
    example, if the fieldnames are `['x', 'y', 'z']` and the defaults are
    `(1, 2)`, then `x` will be a required argument, `y` will default to
    `1`, and `z` will default to `2`.

    If *module* is defined, the :attr:`~type.__module__` attribute of the
    named tuple is set to that value.

    Named tuple instances do not have per-instance dictionaries, so they are
    lightweight and require no more memory than regular tuples.

    To support pickling, the named tuple class should be assigned to a variable
    that matches *typename*.

    .. versionchanged:: 3.1
       Added support for *rename*.

    .. versionchanged:: 3.6
       The *verbose* and *rename* parameters became
       `ref`.

    .. versionchanged:: 3.6
       Added the *module* parameter.

    .. versionchanged:: 3.7
       Removed the *verbose* parameter and the :attr:`!_source` attribute.

    .. versionchanged:: 3.7
       Added the *defaults* parameter and the :attr:`~somenamedtuple._field_defaults`
       attribute.

.. doctest

```python
 :options: +NORMALIZE_WHITESPACE

 >>> # Basic example
 >>> Point = namedtuple('Point', ['x', 'y'])
 >>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
 >>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
 33
 >>> x, y = p                # unpack like a regular tuple
 >>> x, y
 (11, 22)
 >>> p.x + p.y               # fields also accessible by name
 33
 >>> p                       # readable __repr__ with a name=value style
 Point(x=11, y=22)

```

Named tuples are especially useful for assigning field names to result tuples returned
by the :mod:`csv` or :mod:`sqlite3` modules

```python

 EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

 import csv
 for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
     print(emp.name, emp.title)

 import sqlite3
 conn = sqlite3.connect('/companydata')
 cursor = conn.cursor()
 cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
 for emp in map(EmployeeRecord._make, cursor.fetchall()):
     print(emp.name, emp.title)

```

In addition to the methods inherited from tuples, named tuples support
three additional methods and two attributes.  To prevent conflicts with
field names, the method and attribute names start with an underscore.

    Class method that makes a new instance from an existing sequence or iterable.

.. doctest

```python

     >>> t = [11, 22]
     >>> Point._make(t)
     Point(x=11, y=22)

```

### Method: `somenamedtuple._asdict()`

    Return a new `class` which maps field names to their corresponding
    values:

.. doctest

```python

     >>> p = Point(x=11, y=22)
     >>> p._asdict()
     {'x': 11, 'y': 22}

 .. versionchanged:: 3.1
     Returns an :class:`OrderedDict` instead of a regular :class:`dict`.

 .. versionchanged:: 3.8
     Returns a regular :class:`dict` instead of an :class:`OrderedDict`.
     As of Python 3.7, regular dicts are guaranteed to be ordered.  If the
     extra features of :class:`OrderedDict` are required, the suggested
     remediation is to cast the result to the desired type:
     ``OrderedDict(nt._asdict())``.

```

### Method: `somenamedtuple._replace(**kwargs)`

    Return a new instance of the named tuple replacing specified fields with new
values

```python

     >>> p = Point(x=11, y=22)
     >>> p._replace(x=33)
     Point(x=33, y=22)

     >>> for partnum, record in inventory.items():
     ...     inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())

 Named tuples are also supported by generic function :func:`copy.replace`.

 .. versionchanged:: 3.13
    Raise :exc:`TypeError` instead of :exc:`ValueError` for invalid
    keyword arguments.

```

    Tuple of strings listing the field names.  Useful for introspection
    and for creating new named tuple types from existing named tuples.

.. doctest

```python

     >>> p._fields            # view the field names
     ('x', 'y')

     >>> Color = namedtuple('Color', 'red green blue')
     >>> Pixel = namedtuple('Pixel', Point._fields + Color._fields)
     >>> Pixel(11, 22, 128, 255, 0)
     Pixel(x=11, y=22, red=128, green=255, blue=0)

```

   Dictionary mapping field names to default values.

.. doctest

```python

     >>> Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
     >>> Account._field_defaults
     {'balance': 0}
     >>> Account('premium')
     Account(type='premium', balance=0)

```

To retrieve a field whose name is stored in a string, use the `getattr()`
function:

    >>> getattr(p, 'x')
    11

To convert a dictionary to a named tuple, use the double-star-operator
(as described in `ref`):

    >>> d = {'x': 11, 'y': 22}
    >>> Point(**d)
    Point(x=11, y=22)

Since a named tuple is a regular Python class, it is easy to add or change
functionality with a subclass.  Here is how to add a calculated field and
a fixed-width print format:

.. doctest

```python

 >>> class Point(namedtuple('Point', ['x', 'y'])):
 ...     __slots__ = ()
 ...     @property
 ...     def hypot(self):
 ...         return (self.x ** 2 + self.y ** 2) ** 0.5
 ...     def __str__(self):
 ...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

 >>> for p in Point(3, 4), Point(14, 5/7):
 ...     print(p)
 Point: x= 3.000  y= 4.000  hypot= 5.000
 Point: x=14.000  y= 0.714  hypot=14.018

```

The subclass shown above sets `__slots__` to an empty tuple.  This helps
keep memory requirements low by preventing the creation of instance dictionaries.

Subclassing is not useful for adding new, stored fields.  Instead, simply
create a new named tuple type from the :attr:`~somenamedtuple._fields` attribute:

    >>> Point3D = namedtuple('Point3D', Point._fields + ('z',))

Docstrings can be customized by making direct assignments to the `__doc__`
fields:

   >>> Book = namedtuple('Book', ['id', 'title', 'authors'])
   >>> Book.__doc__ += ': Hardcover book in active collection'
   >>> Book.id.__doc__ = '13-digit ISBN'
   >>> Book.title.__doc__ = 'Title of first printing'
   >>> Book.authors.__doc__ = 'List of authors sorted by last name'

   Property docstrings became writeable.

.. seealso

```python

* See :class:`typing.NamedTuple` for a way to add type hints for named
  tuples.  It also provides an elegant notation using the :keyword:`class`
  keyword::

      class Component(NamedTuple):
          part_number: int
          weight: float
          description: Optional[str] = None

* See :meth:`types.SimpleNamespace` for a mutable namespace based on an
  underlying dictionary instead of a tuple.

* The :mod:`dataclasses` module provides a decorator and functions for
  automatically adding generated special methods to user-defined classes.

```

### :class:`OrderedDict` objects

Ordered dictionaries are just like regular dictionaries but have some extra
capabilities relating to ordering operations.  They have become less
important now that the built-in `class` class gained the ability
to remember insertion order (this new behavior became guaranteed in
Python 3.7).

Some differences from `class` still remain:

* The regular `class` was designed to be very good at mapping
  operations.  Tracking insertion order was secondary.

* The `class` was designed to be good at reordering operations.
  Space efficiency, iteration speed, and the performance of update
  operations were secondary.

* The `class` algorithm can handle frequent reordering operations
  better than `class`.  As shown in the recipes below, this makes it
  suitable for implementing various kinds of LRU caches.

* The equality operation for `class` checks for matching order.

  A regular `class` can emulate the order sensitive equality test with
  `p == q and all(k1 == k2 for k1, k2 in zip(p, q))`.

* The `OrderedDict.popitem()` method of `class` has a different
  signature.  It accepts an optional argument to specify which item is popped.

  A regular `class` can emulate OrderedDict's `od.popitem(last=True)`
  with `d.popitem()` which is guaranteed to pop the rightmost (last) item.

  A regular `class` can emulate OrderedDict's `od.popitem(last=False)`
  with `(k := next(iter(d)), d.pop(k))` which will return and remove the
  leftmost (first) item if it exists.

* `class` has a `OrderedDict.move_to_end()` method to efficiently
  reposition an element to an endpoint.

  A regular `class` can emulate OrderedDict's ``od.move_to_end(k,
  last=True)` with `d[k] = d.pop(k)`` which will move the key and its
  associated value to the rightmost (last) position.

  A regular `class` does not have an efficient equivalent for
  OrderedDict's `od.move_to_end(k, last=False)` which moves the key
  and its associated value to the leftmost (first) position.

* Until Python 3.8, `class` lacked a `object.__reversed__()` method.

### Class: `OrderedDict(**kwargs)`

           OrderedDict(mapping, /, **kwargs)
           OrderedDict(iterable, /, **kwargs)

    Return an instance of a `class` subclass that has methods
    specialized for rearranging dictionary order.

    .. versionadded:: 3.1

    .. method:: popitem(last=True)

        The `popitem()` method for ordered dictionaries returns and removes a
        (key, value) pair.  The pairs are returned in
        :abbr:`LIFO (last-in, first-out)` order if *last* is true
        or :abbr:`FIFO (first-in, first-out)` order if false.

    .. method:: move_to_end(key, last=True)

        Move an existing *key* to either end of an ordered dictionary.  The item
        is moved to the right end if *last* is true (the default) or to the
        beginning if *last* is false.  Raises `exc` if the *key* does
        not exist:

.. doctest

```python

         >>> d = OrderedDict.fromkeys('abcde')
         >>> d.move_to_end('b')
         >>> ''.join(d)
         'acdeb'
         >>> d.move_to_end('b', last=False)
         >>> ''.join(d)
         'bacde'

     .. versionadded:: 3.2

```

In addition to the usual mapping methods, ordered dictionaries also support
reverse iteration using `reversed()`.

Equality tests between `class` objects are order-sensitive
and are roughly equivalent to `list(od1.items())==list(od2.items())`.

Equality tests between `class` objects and other
`class` objects are order-insensitive like regular
dictionaries.  This allows `class` objects to be substituted
anywhere a regular dictionary is used.

   The items, keys, and values `term`
   of `class` now support reverse iteration using `reversed()`.

   With the acceptance of `pep`, order is retained for keyword arguments
   passed to the `class` constructor and its `dict.update()`
   method.

   Added merge (`|`) and update (`|=`) operators, specified in `pep`.

### :class:`OrderedDict` Examples and Recipes

It is straightforward to create an ordered dictionary variant
that remembers the order the keys were *last* inserted.
If a new entry overwrites an existing entry, the
original insertion position is changed and moved to the end

```python

 class LastUpdatedOrderedDict(OrderedDict):
     'Store items in the order that the keys were last updated.'

     def __setitem__(self, key, value):
         super().__setitem__(key, value)
         self.move_to_end(key)

```

An `class` would also be useful for implementing
variants of :deco:`functools.lru_cache`:

.. testcode

```python

 from collections import OrderedDict
 from time import monotonic

 class TimeBoundedLRU:
     "LRU Cache that invalidates and refreshes old entries."

     def __init__(self, func, maxsize=128, maxage=30):
         self.cache = OrderedDict()      # { args : (timestamp, result)}
         self.func = func
         self.maxsize = maxsize
         self.maxage = maxage

     def __call__(self, *args):
         if args in self.cache:
             self.cache.move_to_end(args)
             timestamp, result = self.cache[args]
             if monotonic() - timestamp <= self.maxage:
                 return result
         result = self.func(*args)
         self.cache[args] = monotonic(), result
         if len(self.cache) > self.maxsize:
             self.cache.popitem(last=False)
         return result

```

.. testcode

```python

 class MultiHitLRUCache:
     """ LRU cache that defers caching a result until
         it has been requested multiple times.

         To avoid flushing the LRU cache with one-time requests,
         we don't cache until a request has been made more than once.

     """

     def __init__(self, func, maxsize=128, maxrequests=4096, cache_after=1):
         self.requests = OrderedDict()   # { uncached_key : request_count }
         self.cache = OrderedDict()      # { cached_key : function_result }
         self.func = func
         self.maxrequests = maxrequests  # max number of uncached requests
         self.maxsize = maxsize          # max number of stored return values
         self.cache_after = cache_after

     def __call__(self, *args):
         if args in self.cache:
             self.cache.move_to_end(args)
             return self.cache[args]
         result = self.func(*args)
         self.requests[args] = self.requests.get(args, 0) + 1
         if self.requests[args] <= self.cache_after:
             self.requests.move_to_end(args)
             if len(self.requests) > self.maxrequests:
                 self.requests.popitem(last=False)
         else:
             self.requests.pop(args, None)
             self.cache[args] = result
             if len(self.cache) > self.maxsize:
                 self.cache.popitem(last=False)
         return result

```

.. doctest

```python
 :hide:

 >>> def square(x):
 ...     return x * x
 ...
 >>> f = MultiHitLRUCache(square, maxsize=4, maxrequests=6)
 >>> list(map(f, range(10)))  # First requests, don't cache
 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 >>> f(4)  # Cache the second request
 16
 >>> f(6)  # Cache the second request
 36
 >>> f(2)  # The first request aged out, so don't cache
 4
 >>> f(6)  # Cache hit
 36
 >>> f(4)  # Cache hit and move to front
 16
 >>> list(f.cache.values())
 [36, 16]
 >>> set(f.requests).isdisjoint(f.cache)
 True
 >>> list(map(f, [9, 8, 7]))   # Cache these second requests
 [81, 64, 49]
 >>> list(map(f, [7, 9]))  # Cache hits
 [49, 81]
 >>> list(f.cache.values())
 [16, 64, 49, 81]
 >>> set(f.requests).isdisjoint(f.cache)
 True

```

### :class:`UserDict` objects

The class, `class` acts as a wrapper around dictionary objects.
The need for this class has been partially supplanted by the ability to
subclass directly from `class`; however, this class can be easier
to work with because the underlying dictionary is accessible as an
attribute.

### Class: `UserDict(**kwargs)`

           UserDict(mapping, /, **kwargs)
           UserDict(iterable, /, **kwargs)

    Class that simulates a dictionary.  The instance's contents are kept in a
    regular dictionary, which is accessible via the :attr:`data` attribute of
    `class` instances.  If arguments are provided, they are used to
    initialize :attr:`data`, like a regular dictionary.

    In addition to supporting the methods and operations of mappings,
    `class` instances provide the following attribute:

    .. attribute:: data

        A real dictionary used to store the contents of the `class`
        class.

    `class` instances also override the following method:

    .. method:: popitem

        Remove and return a `(key, value)` pair from the wrapped dictionary. Pairs are
        returned in the same order as `data.popitem()`. (For the default
        `dict.popitem()`, this order is :abbr:`LIFO (last-in, first-out)`.) If the
        dictionary is empty, raises a `exc`.

### :class:`UserList` objects

This class acts as a wrapper around list objects.  It is a useful base class
for your own list-like classes which can inherit from them and override
existing methods or add new ones.  In this way, one can add new behaviors to
lists.

The need for this class has been partially supplanted by the ability to
subclass directly from `class`; however, this class can be easier
to work with because the underlying list is accessible as an attribute.

### Class: `UserList([list])`

    Class that simulates a list.  The instance's contents are kept in a regular
    list, which is accessible via the :attr:`data` attribute of `class`
    instances.  The instance's contents are initially set to a copy of *list*,
    defaulting to the empty list `[]`.  *list* can be any iterable, for
    example a real Python list or a `class` object.

    In addition to supporting the methods and operations of mutable sequences,
    `class` instances provide the following attribute:

    .. attribute:: data

        A real `class` object used to store the contents of the
        `class` class.

**Subclassing requirements:** Subclasses of `class` are expected to
offer a constructor which can be called with either no arguments or one
argument.  List operations which return a new sequence attempt to create an
instance of the actual implementation class.  To do so, it assumes that the
constructor can be called with a single parameter, which is a sequence object
used as a data source.

If a derived class does not wish to comply with this requirement, all of the
special methods supported by this class will need to be overridden; please
consult the sources for information about the methods which need to be provided
in that case.

### :class:`UserString` objects

The class, `class` acts as a wrapper around string objects.
The need for this class has been partially supplanted by the ability to
subclass directly from `class`; however, this class can be easier
to work with because the underlying string is accessible as an
attribute.

### Class: `UserString(seq)`

    Class that simulates a string object.  The instance's
    content is kept in a regular string object, which is accessible via the
    :attr:`data` attribute of `class` instances.  The instance's
    contents are initially set to a copy of *seq*.  The *seq* argument can
    be any object which can be converted into a string using the built-in
    `str()` function.

    In addition to supporting the methods and operations of strings,
    `class` instances provide the following attribute:

    .. attribute:: data

        A real `class` object used to store the contents of the
        `class` class.

    .. versionchanged:: 3.5
       New methods `__getnewargs__`, `__rmod__`, `casefold`,
       `format_map`, `isprintable`, and `maketrans`.

## :mod:`!heapq` --- Heap queue algorithm

   :synopsis: Heap queue algorithm (a.k.a. priority queue).

**Source code:** :source:`Lib/heapq.py`

--------------

This module provides an implementation of the heap queue algorithm, also known
as the priority queue algorithm.

Min-heaps are binary trees for which every parent node has a value less than
or equal to any of its children.
We refer to this condition as the heap invariant.

For min-heaps, this implementation uses lists for which
`heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all *k* for which
the compared elements exist.  Elements are counted from zero.  The interesting
property of a min-heap is that its smallest element is always the root,
`heap[0]`.

Max-heaps satisfy the reverse invariant: every parent node has a value
*greater* than any of its children.  These are implemented as lists for which
`maxheap[2*k+1] <= maxheap[k]` and `maxheap[2*k+2] <= maxheap[k]` for all
*k* for which the compared elements exist.
The root, `maxheap[0]`, contains the *largest* element;
`heap.sort(reverse=True)` maintains the max-heap invariant.

The `mod` API differs from textbook heap algorithms in two aspects: (a)
We use zero-based indexing.  This makes the relationship between the index for
a node and the indexes for its children slightly less obvious, but is more
suitable since Python uses zero-based indexing. (b) Textbooks often focus on
max-heaps, due to their suitability for in-place sorting. Our implementation
favors min-heaps as they better correspond to Python `class`.

These two aspects make it possible to view the heap as a regular Python list
without surprises: `heap[0]` is the smallest item, and `heap.sort()`
maintains the heap invariant!

Like `list.sort()`, this implementation uses only the `<` operator
for comparisons, for both min-heaps and max-heaps.

In the API below, and in this documentation, the unqualified term *heap*
generally refers to a min-heap.
The API for max-heaps is named using a `_max`  suffix.

To create a heap, use a list initialized as `[]`, or transform an existing list
into a min-heap or max-heap using the `heapify()` or `heapify_max()`
functions, respectively.

The following functions are provided for min-heaps:

### Function: `heapify(x)`

   Transform list *x* into a min-heap, in-place, in linear time.

### Function: `heappush(heap, item)`

   Push the value *item* onto the *heap*, maintaining the min-heap invariant.

### Function: `heappop(heap)`

   Pop and return the smallest item from the *heap*, maintaining the min-heap
   invariant.  If the heap is empty, `exc` is raised.  To access the
   smallest item without popping it, use `heap[0]`.

### Function: `heappushpop(heap, item)`

   Push *item* on the heap, then pop and return the smallest item from the
   *heap*.  The combined action runs more efficiently than `heappush()`
   followed by a separate call to `heappop()`.

### Function: `heapreplace(heap, item)`

   Pop and return the smallest item from the *heap*, and also push the new *item*.
   The heap size doesn't change. If the heap is empty, `exc` is raised.

   This one step operation is more efficient than a `heappop()` followed by
   `heappush()` and can be more appropriate when using a fixed-size heap.
   The pop/push combination always returns an element from the heap and replaces
   it with *item*.

   The value returned may be larger than the *item* added.  If that isn't
   desired, consider using `heappushpop()` instead.  Its push/pop
   combination returns the smaller of the two values, leaving the larger value
   on the heap.

For max-heaps, the following functions are provided:

### Function: `heapify_max(x)`

   Transform list *x* into a max-heap, in-place, in linear time.

   .. versionadded:: 3.14

### Function: `heappush_max(heap, item)`

   Push the value *item* onto the max-heap *heap*, maintaining the max-heap
   invariant.

   .. versionadded:: 3.14

### Function: `heappop_max(heap)`

   Pop and return the largest item from the max-heap *heap*, maintaining the
   max-heap invariant.  If the max-heap is empty, `exc` is raised.
   To access the largest item without popping it, use `maxheap[0]`.

   .. versionadded:: 3.14

### Function: `heappushpop_max(heap, item)`

   Push *item* on the max-heap *heap*, then pop and return the largest item
   from *heap*.
   The combined action runs more efficiently than `heappush_max()`
   followed by a separate call to `heappop_max()`.

   .. versionadded:: 3.14

### Function: `heapreplace_max(heap, item)`

   Pop and return the largest item from the max-heap *heap* and also push the
   new *item*.
   The max-heap size doesn't change. If the max-heap is empty,
   `exc` is raised.

   The value returned may be smaller than the *item* added.  Refer to the
   analogous function `heapreplace()` for detailed usage notes.

   .. versionadded:: 3.14

The module also offers three general purpose functions based on heaps.

### Function: `merge(*iterables, key=None, reverse=False)`

   Merge multiple sorted inputs into a single sorted output (for example, merge
   timestamped entries from multiple log files).  Returns an `term`
   over the sorted values.

   Similar to `sorted(itertools.chain(*iterables))` but returns an iterable, does
   not pull the data into memory all at once, and assumes that each of the input
   streams is already sorted (smallest to largest).

   Has two optional arguments which must be specified as keyword arguments.

   *key* specifies a `term` of one argument that is used to
   extract a comparison key from each input element.  The default value is
   `None` (compare the elements directly).

   *reverse* is a boolean value.  If set to `True`, then the input elements
   are merged as if each comparison were reversed. To achieve behavior similar
   to `sorted(itertools.chain(*iterables), reverse=True)`, all iterables must
   be sorted from largest to smallest.

   .. versionchanged:: 3.5
      Added the optional *key* and *reverse* parameters.

### Function: `nlargest(n, iterable, key=None)`

   Return a list with the *n* largest elements from the dataset defined by
   *iterable*.  *key*, if provided, specifies a function of one argument that is
   used to extract a comparison key from each element in *iterable* (for example,
   `key=str.lower`).  Equivalent to:  ``sorted(iterable, key=key,
   reverse=True)[:n]``.

### Function: `nsmallest(n, iterable, key=None)`

   Return a list with the *n* smallest elements from the dataset defined by
   *iterable*.  *key*, if provided, specifies a function of one argument that is
   used to extract a comparison key from each element in *iterable* (for example,
   `key=str.lower`).  Equivalent to:  `sorted(iterable, key=key)[:n]`.

The latter two functions perform best for smaller values of *n*.  For larger
values, it is more efficient to use the `sorted()` function.  Also, when
`n==1`, it is more efficient to use the built-in `min()` and `max()`
functions.  If repeated usage of these functions is required, consider turning
the iterable into an actual heap.

### Basic Examples

A `heapsort <https://en.wikipedia.org/wiki/Heapsort>`_ can be implemented by
pushing all values onto a heap and then popping off the smallest values one at a
time

```python

>>> def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

This is similar to `sorted(iterable)`, but unlike `sorted()`, this
implementation is not stable.

Heap elements can be tuples.  This is useful for assigning comparison values
(such as task priorities) alongside the main record being tracked

```python

 >>> h = []
 >>> heappush(h, (5, 'write code'))
 >>> heappush(h, (7, 'release product'))
 >>> heappush(h, (1, 'write spec'))
 >>> heappush(h, (3, 'create tests'))
 >>> heappop(h)
 (1, 'write spec')

```

### Other Applications

`Medians <https://en.wikipedia.org/wiki/Median>`_ are a measure of
central tendency for a set of numbers.  In distributions skewed by
outliers, the median provides a more stable estimate than an average
(arithmetic mean).  A running median is an `online algorithm
<https://en.wikipedia.org/wiki/Online_algorithm>`_ that updates
continuously as new data arrives.

A running median can be efficiently implemented by balancing two heaps,
a max-heap for values at or below the midpoint and a min-heap for values
above the midpoint.  When the two heaps have the same size, the new
median is the average of the tops of the two heaps; otherwise, the
median is at the top of the larger heap

```python

 def running_median(iterable):
     "Yields the cumulative median of values seen so far."

     lo = []  # max-heap
     hi = []  # min-heap (same size as or one smaller than lo)

     for x in iterable:
         if len(lo) == len(hi):
             heappush_max(lo, heappushpop(hi, x))
             yield lo[0]
         else:
             heappush(hi, heappushpop_max(lo, x))
             yield (lo[0] + hi[0]) / 2

```

For example

```python

 >>> list(running_median([5.0, 9.0, 4.0, 12.0, 8.0, 9.0]))
 [5.0, 7.0, 5.0, 7.0, 8.0, 8.5]

```

### Priority Queue Implementation Notes

A `priority queue <https://en.wikipedia.org/wiki/Priority_queue>`_ is common use
for a heap, and it presents several implementation challenges:

* Sort stability:  how do you get two tasks with equal priorities to be returned
  in the order they were originally added?

* Tuple comparison breaks for (priority, task) pairs if the priorities are equal
  and the tasks do not have a default comparison order.

* If the priority of a task changes, how do you move it to a new position in
  the heap?

* Or if a pending task needs to be deleted, how do you find it and remove it
  from the queue?

A solution to the first two challenges is to store entries as 3-element list
including the priority, an entry count, and the task.  The entry count serves as
a tie-breaker so that two tasks with the same priority are returned in the order
they were added. And since no two entry counts are the same, the tuple
comparison will never attempt to directly compare two tasks.

Another solution to the problem of non-comparable tasks is to create a wrapper
class that ignores the task item and only compares the priority field

```python

 from dataclasses import dataclass, field
 from typing import Any

 @dataclass(order=True)
 class PrioritizedItem:
     priority: int
     item: Any=field(compare=False)

```

The remaining challenges revolve around finding a pending task and making
changes to its priority or removing it entirely.  Finding a task can be done
with a dictionary pointing to an entry in the queue.

Removing the entry or changing its priority is more difficult because it would
break the heap structure invariants.  So, a possible solution is to mark the
entry as removed and add a new entry with the revised priority

```python

 pq = []                         # list of entries arranged in a heap
 entry_finder = {}               # mapping of tasks to entries
 REMOVED = '<removed-task>'      # placeholder for a removed task
 counter = itertools.count()     # unique sequence count

 def add_task(task, priority=0):
     'Add a new task or update the priority of an existing task'
     if task in entry_finder:
         remove_task(task)
     count = next(counter)
     entry = [priority, count, task]
     entry_finder[task] = entry
     heappush(pq, entry)

 def remove_task(task):
     'Mark an existing task as REMOVED.  Raise KeyError if not found.'
     entry = entry_finder.pop(task)
     entry[-1] = REMOVED

 def pop_task():
     'Remove and return the lowest priority task. Raise KeyError if empty.'
     while pq:
         priority, count, task = heappop(pq)
         if task is not REMOVED:
             del entry_finder[task]
             return task
     raise KeyError('pop from an empty priority queue')

```

### Theory

Heaps are arrays for which `a[k] <= a[2*k+1]` and `a[k] <= a[2*k+2]` for all
*k*, counting elements from 0.  For the sake of comparison, non-existing
elements are considered to be infinite.  The interesting property of a heap is
that `a[0]` is always its smallest element.

The strange invariant above is meant to be an efficient memory representation
for a tournament.  The numbers below are *k*, not `a[k]`:

   :class: invert-in-dark-mode
   :align: center
   :alt: Example (min-heap) binary tree.

In the tree above, each cell *k* is topping `2*k+1` and `2*k+2`. In a usual
binary tournament we see in sports, each cell is the winner over the two cells
it tops, and we can trace the winner down the tree to see all opponents s/he
had.  However, in many computer applications of such tournaments, we do not need
to trace the history of a winner. To be more memory efficient, when a winner is
promoted, we try to replace it by something else at a lower level, and the rule
becomes that a cell and the two cells it tops contain three different items, but
the top cell "wins" over the two topped cells.

If this heap invariant is protected at all time, index 0 is clearly the overall
winner.  The simplest algorithmic way to remove it and find the "next" winner is
to move some loser (let's say cell 30 in the diagram above) into the 0 position,
and then percolate this new 0 down the tree, exchanging values, until the
invariant is re-established. This is clearly logarithmic on the total number of
items in the tree. By iterating over all items, you get an *O*\ (*n* log *n*) sort.

A nice feature of this sort is that you can efficiently insert new items while
the sort is going on, provided that the inserted items are not "better" than the
last 0'th element you extracted.  This is especially useful in simulation
contexts, where the tree holds all incoming events, and the "win" condition
means the smallest scheduled time.  When an event schedules other events for
execution, they are scheduled into the future, so they can easily go into the
heap.  So, a heap is a good structure for implementing schedulers (this is what
I used for my MIDI sequencer :-).

Various structures for implementing schedulers have been extensively studied,
and heaps are good for this, as they are reasonably speedy, the speed is almost
constant, and the worst case is not much different than the average case.
However, there are other representations which are more efficient overall, yet
the worst cases might be terrible.

Heaps are also very useful in big disk sorts.  You most probably all know that a
big sort implies producing "runs" (which are pre-sorted sequences, whose size is
usually related to the amount of CPU memory), followed by a merging passes for
these runs, which merging is often very cleverly organised [#]_. It is very
important that the initial sort produces the longest runs possible.  Tournaments
are a good way to achieve that.  If, using all the memory available to hold a
tournament, you replace and percolate items that happen to fit the current run,
you'll produce runs which are twice the size of the memory for random input, and
much better for input fuzzily ordered.

Moreover, if you output the 0'th item on disk and get an input which may not fit
in the current tournament (because the value "wins" over the last output value),
it cannot fit in the heap, so the size of the heap decreases.  The freed memory
could be cleverly reused immediately for progressively building a second heap,
which grows at exactly the same rate the first heap is melting.  When the first
heap completely vanishes, you switch heaps and start a new run.  Clever and
quite effective!

In a word, heaps are useful memory structures to know.  I use them in a few
applications, and I think it is good to keep a 'heap' module around. :-)

   than clever, and this is a consequence of the seeking capabilities of the disks.
   On devices which cannot seek, like big tape drives, the story was quite
   different, and one had to be very clever to ensure (far in advance) that each
   tape movement will be the most effective possible (that is, will best
   participate at "progressing" the merge).  Some tapes were even able to read
   backwards, and this was also used to avoid the rewinding time. Believe me, real
   good tape sorts were quite spectacular to watch! From all times, sorting has
   always been a Great Art! :-)

## :mod:`!bisect` --- Array bisection algorithm

   :synopsis: Array bisection algorithms for binary searching.

**Source code:** :source:`Lib/bisect.py`

--------------

This module provides support for maintaining a list in sorted order without
having to sort the list after each insertion.  For long lists of items with
expensive comparison operations, this can be an improvement over
linear searches or frequent resorting.

The module is called `mod` because it uses a basic bisection
algorithm to do its work.  Unlike other bisection tools that search for a
specific value, the functions in this module are designed to locate an
insertion point. Accordingly, the functions never call an `object.__eq__()`
method to determine whether a value has been found.  Instead, the
functions only call the `object.__lt__()` method and will return an insertion
point between values in an array.

.. note

```python

The functions in this module are not thread-safe. If multiple threads
concurrently use :mod:`!bisect` functions on the same sequence, this
may result in undefined behaviour. Likewise, if the provided sequence
is mutated by a different thread while a :mod:`!bisect` function
is operating on it, the result is undefined. For example, using
:py:func:`~bisect.insort_left` on the same list from multiple threads
may result in the list becoming unsorted.

```

The following functions are provided:

### Function: `bisect_left(a, x, lo=0, hi=len(a), *, key=None)`

   Locate the insertion point for *x* in *a* to maintain sorted order.
   The parameters *lo* and *hi* may be used to specify a subset of the list
   which should be considered; by default the entire list is used.  If *x* is
   already present in *a*, the insertion point will be before (to the left of)
   any existing entries.  The return value is suitable for use as the first
   parameter to `list.insert()` assuming that *a* is already sorted.

   The returned insertion point *ip* partitions the array *a* into two
   slices such that `all(elem < x for elem in a[lo : ip])` is true for the
   left slice and `all(elem >= x for elem in a[ip : hi])` is true for the
   right slice.

   *key* specifies a `term` of one argument that is used to
   extract a comparison key from each element in the array.  To support
   searching complex records, the key function is not applied to the *x* value.

   If *key* is `None`, the elements are compared directly and
   no key function is called.

   .. versionchanged:: 3.10
      Added the *key* parameter.

### Function: `bisect_right(a, x, lo=0, hi=len(a), *, key=None)`

              bisect(a, x, lo=0, hi=len(a), *, key=None)

   Similar to :py`bisect.bisect_left()`, but returns an insertion point which comes
   after (to the right of) any existing entries of *x* in *a*.

   The returned insertion point *ip* partitions the array *a* into two slices
   such that `all(elem <= x for elem in a[lo : ip])` is true for the left slice and
   `all(elem > x for elem in a[ip : hi])` is true for the right slice.

   .. versionchanged:: 3.10
      Added the *key* parameter.

### Function: `insort_left(a, x, lo=0, hi=len(a), *, key=None)`

   Insert *x* in *a* in sorted order.

   This function first runs :py`bisect.bisect_left()` to locate an insertion point.
   Next, it runs the `sequence.insert()` method on *a* to insert *x* at the
   appropriate position to maintain sort order.

   To support inserting records in a table, the *key* function (if any) is
   applied to *x* for the search step but not for the insertion step.

   Keep in mind that the *O*\ (log *n*) search is dominated by the slow *O*\ (*n*)
   insertion step.

   .. versionchanged:: 3.10
      Added the *key* parameter.

### Function: `insort_right(a, x, lo=0, hi=len(a), *, key=None)`

              insort(a, x, lo=0, hi=len(a), *, key=None)

   Similar to :py`bisect.insort_left()`, but inserting *x* in *a* after any existing
   entries of *x*.

   This function first runs :py`bisect.bisect_right()` to locate an insertion point.
   Next, it runs the `sequence.insert()` method on *a* to insert *x* at the
   appropriate position to maintain sort order.

   To support inserting records in a table, the *key* function (if any) is
   applied to *x* for the search step but not for the insertion step.

   Keep in mind that the *O*\ (log *n*) search is dominated by the slow *O*\ (*n*)
   insertion step.

   .. versionchanged:: 3.10
      Added the *key* parameter.

### Performance Notes

When writing time sensitive code using *bisect()* and *insort()*, keep these
thoughts in mind:

* Bisection is effective for searching ranges of values.
  For locating specific values, dictionaries are more performant.

* The *insort()* functions are *O*\ (*n*) because the logarithmic search step
  is dominated by the linear time insertion step.

* The search functions are stateless and discard key function results after
  they are used.  Consequently, if the search functions are used in a loop,
  the key function may be called again and again on the same array elements.
  If the key function isn't fast, consider wrapping it with
  :py:deco:`functools.cache` to avoid duplicate computations.  Alternatively,
  consider searching an array of precomputed keys to locate the insertion
  point (as shown in the examples section below).

.. seealso

```python

* `Sorted Collections
  <https://grantjenks.com/docs/sortedcollections/>`_ is a high performance
  module that uses *bisect* to managed sorted collections of data.

* The `SortedCollection recipe
  <https://code.activestate.com/recipes/577197-sortedcollection/>`_ uses
  bisect to build a full-featured collection class with straight-forward search
  methods and support for a key-function.  The keys are precomputed to save
  unnecessary calls to the key function during searches.

```

### Searching Sorted Lists

The above `bisect functions`_ are useful for finding insertion points but
can be tricky or awkward to use for common searching tasks. The following five
functions show how to transform them into the standard lookups for sorted
lists

```python

 def index(a, x):
     'Locate the leftmost value exactly equal to x'
     i = bisect_left(a, x)
     if i != len(a) and a[i] == x:
         return i
     raise ValueError

 def find_lt(a, x):
     'Find rightmost value less than x'
     i = bisect_left(a, x)
     if i:
         return a[i-1]
     raise ValueError

 def find_le(a, x):
     'Find rightmost value less than or equal to x'
     i = bisect_right(a, x)
     if i:
         return a[i-1]
     raise ValueError

 def find_gt(a, x):
     'Find leftmost value greater than x'
     i = bisect_right(a, x)
     if i != len(a):
         return a[i]
     raise ValueError

 def find_ge(a, x):
     'Find leftmost item greater than or equal to x'
     i = bisect_left(a, x)
     if i != len(a):
         return a[i]
     raise ValueError

```

### Examples

The :py`bisect.bisect()` function can be useful for numeric table lookups. This
example uses :py`bisect.bisect()` to look up a letter grade for an exam score (say)
based on a set of ordered numeric breakpoints: 90 and up is an 'A', 80 to 89 is
a 'B', and so on

```python

>>> def grade(score):
...     i = bisect([60, 70, 80, 90], score)
...     return "FDCBA"[i]
...
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']

```

The :py`bisect.bisect()` and :py`bisect.insort()` functions also work with
lists of tuples.  The *key* argument can serve to extract the field used for ordering
records in a table

```python

 >>> from collections import namedtuple
 >>> from operator import attrgetter
 >>> from bisect import bisect, insort
 >>> from pprint import pprint

 >>> Movie = namedtuple('Movie', ('name', 'released', 'director'))

 >>> movies = [
 ...     Movie('Jaws', 1975, 'Spielberg'),
 ...     Movie('Titanic', 1997, 'Cameron'),
 ...     Movie('The Birds', 1963, 'Hitchcock'),
 ...     Movie('Aliens', 1986, 'Cameron')
 ... ]

 >>> # Find the first movie released after 1960
 >>> by_year = attrgetter('released')
 >>> movies.sort(key=by_year)
 >>> movies[bisect(movies, 1960, key=by_year)]
 Movie(name='The Birds', released=1963, director='Hitchcock')

 >>> # Insert a movie while maintaining sort order
 >>> romance = Movie('Love Story', 1970, 'Hiller')
 >>> insort(movies, romance, key=by_year)
 >>> pprint(movies)
 [Movie(name='The Birds', released=1963, director='Hitchcock'),
  Movie(name='Love Story', released=1970, director='Hiller'),
  Movie(name='Jaws', released=1975, director='Spielberg'),
  Movie(name='Aliens', released=1986, director='Cameron'),
  Movie(name='Titanic', released=1997, director='Cameron')]

```

If the key function is expensive, it is possible to avoid repeated function
calls by searching a list of precomputed keys to find the index of a record

```python

 >>> data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
 >>> data.sort(key=lambda r: r[1])       # Or use operator.itemgetter(1).
 >>> keys = [r[1] for r in data]         # Precompute a list of keys.
 >>> data[bisect_left(keys, 0)]
 ('black', 0)
 >>> data[bisect_left(keys, 1)]
 ('blue', 1)
 >>> data[bisect_left(keys, 5)]
 ('red', 5)
 >>> data[bisect_left(keys, 8)]
 ('yellow', 8)
```

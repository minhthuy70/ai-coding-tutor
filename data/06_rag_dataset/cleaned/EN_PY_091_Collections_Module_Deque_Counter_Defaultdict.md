# EN_PY_091: collections Module: deque, Counter, defaultdict, and OrderedDict

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Standard Library | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

"collections" — Container datatypes
***********************************

**Source code:** Lib/collections/__init__.py

======================================================================

This module implements specialized container datatypes providing
alternatives to Python’s general purpose built-in containers, "dict",
"list", "set", and "tuple".

+-----------------------+----------------------------------------------------------------------+
| "namedtuple()"        | factory function for creating tuple subclasses with named fields     |
+-----------------------+----------------------------------------------------------------------+
| "deque"               | list-like container with fast appends and pops on either end         |
+-----------------------+----------------------------------------------------------------------+
| "ChainMap"            | dict-like class for creating a single view of multiple mappings      |
+-----------------------+----------------------------------------------------------------------+
| "Counter"             | dict subclass for counting *hashable* objects                        |
+-----------------------+----------------------------------------------------------------------+
| "OrderedDict"         | dict subclass that remembers the order entries were added            |
+-----------------------+----------------------------------------------------------------------+
| "defaultdict"         | dict subclass that calls a factory function to supply missing values |
+-----------------------+----------------------------------------------------------------------+
| "UserDict"            | wrapper around dictionary objects for easier dict subclassing        |
+-----------------------+----------------------------------------------------------------------+
| "UserList"            | wrapper around list objects for easier list subclassing              |
+-----------------------+----------------------------------------------------------------------+
| "UserString"          | wrapper around string objects for easier string subclassing          |
+-----------------------+----------------------------------------------------------------------+

"ChainMap" objects
==================

Added in version 3.3.

A "ChainMap" class is provided for quickly linking a number of
mappings so they can be treated as a single unit.  It is often much
faster than creating a new dictionary and running multiple "update()"
calls.

The class can be used to simulate nested scopes and is useful in
templating.

class collections.ChainMap(*maps)

   A "ChainMap" groups multiple dicts or other mappings together to
   create a single, updateable view.  If no *maps* are specified, a
   single empty dictionary is provided so that a new chain always has
   at least one mapping.

   The underlying mappings are stored in a list.  That list is public
   and can be accessed or updated using the *maps* attribute.  There
   is no other state.

   Lookups search the underlying mappings successively until a key is
   found.  In contrast, writes, updates, and deletions only operate on
   the first mapping.

   A "ChainMap" incorporates the underlying mappings by reference.

```python
So, if one of the underlying mappings gets updated, those changes
will be reflected in "ChainMap".

All of the usual dictionary methods are supported.  In addition,
there is a *maps* attribute, a method for creating new subcontexts,
and a property for accessing all but the first mapping:

maps

   A user updateable list of mappings.  The list is ordered from
   first-searched to last-searched.  It is the only stored state
   and can be modified to change which mappings are searched.  The
   list should always contain at least one mapping.

new_child(m=None, **kwargs)

   Returns a new "ChainMap" containing a new map followed by all of
   the maps in the current instance.  If "m" is specified, it
   becomes the new map at the front of the list of mappings; if not
   specified, an empty dict is used, so that a call to
   "d.new_child()" is equivalent to: "ChainMap({}, *d.maps)". If
   any keyword arguments are specified, they update passed map or
   new empty dict. This method is used for creating subcontexts
   that can be updated without altering values in any of the parent
   mappings.

   Changed in version 3.4: The optional "m" parameter was added.

   Changed in version 3.10: Keyword arguments support was added.

parents

   Property returning a new "ChainMap" containing all of the maps
   in the current instance except the first one.  This is useful
   for skipping the first map in the search.  Use cases are similar
   to those for the "nonlocal" keyword used in *nested scopes*.
   The use cases also parallel those for the built-in "super()"
   function.  A reference to "d.parents" is equivalent to:
   "ChainMap(*d.maps[1:])".

Note, the iteration order of a "ChainMap" is determined by scanning
the mappings last to first:

   >>> baseline = {'music': 'bach', 'art': 'rembrandt'}
   >>> adjustments = {'art': 'van gogh', 'opera': 'carmen'}
   >>> list(ChainMap(adjustments, baseline))
   ['music', 'art', 'opera']

This gives the same ordering as a series of "dict.update()" calls
starting with the last mapping:

   >>> combined = baseline.copy()
   >>> combined.update(adjustments)
   >>> list(combined)
   ['music', 'art', 'opera']

Changed in version 3.9: Added support for "|" and "|=" operators,
specified in **PEP 584**.

```

See also:

  * The MultiContext class in the Enthought CodeTools package has
    options to support writing to any mapping in the chain.

  * Django’s Context class for templating is a read-only chain of
    mappings.  It also features pushing and popping of contexts
    similar to the "new_child()" method and the "parents" property.

  * The Nested Contexts recipe has options to control whether writes
    and other mutations apply only to the first mapping or to any
    mapping in the chain.

  * A greatly simplified read-only version of Chainmap.

"ChainMap" Examples and Recipes
-------------------------------

This section shows various approaches to working with chained maps.

Example of simulating Python’s internal lookup chain:

```python
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))

```

Example of letting user specified command-line arguments take
precedence over environment variables which in turn take precedence
over default values:

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

Example patterns for using the "ChainMap" class to simulate nested
contexts:

   c = ChainMap()        # Create root context
   d = c.new_child()     # Create nested child context

```python
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

The "ChainMap" class only makes updates (writes and deletions) to the
first mapping in the chain while lookups will search the full chain.
However, if deep writes and deletions are desired, it is easy to make
a subclass that updates keys found deeper in the chain:

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

"Counter" objects
=================

A counter tool is provided to support convenient and rapid tallies.
For example:

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

class collections.Counter([iterable-or-mapping])

```python
A "Counter" is a "dict" subclass for counting *hashable* objects.
It is a collection where elements are stored as dictionary keys and
their counts are stored as dictionary values.  Counts are allowed
to be any integer value including zero or negative counts.  The
"Counter" class is similar to bags or multisets in other languages.

Elements are counted from an *iterable* or initialized from another
*mapping* (or counter):

>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

Counter objects have a dictionary interface except that they return
a zero count for missing items instead of raising a "KeyError":

>>> c = Counter(['eggs', 'ham'])
>>> c['bacon']                              # count of a missing element is zero
0

Setting a count to zero does not remove an element from a counter.
Use "del" to remove it entirely:

>>> c['sausage'] = 0                        # counter entry with a zero count
>>> del c['sausage']                        # del actually removes the entry

Added in version 3.1.

Changed in version 3.7: As a "dict" subclass, "Counter" inherited
the capability to remember insertion order.  Math operations on
*Counter* objects also preserve order.  Results are ordered
according to when an element is first encountered in the left
operand and then by the order encountered in the right operand.

Counter objects support additional methods beyond those available
for all dictionaries:

elements()

   Return an iterator over elements repeating each as many times as
   its count.  Elements are returned in the order first
   encountered. If an element’s count is less than one,
   "elements()" will ignore it.

   >>> c = Counter(a=4, b=2, c=0, d=-2)
   >>> sorted(c.elements())
   ['a', 'a', 'a', 'a', 'b', 'b']

most_common([n])

   Return a list of the *n* most common elements and their counts
   from the most common to the least.  If *n* is omitted or "None",
   "most_common()" returns *all* elements in the counter. Elements
   with equal counts are ordered in the order first encountered:

   >>> Counter('abracadabra').most_common(3)
   [('a', 5), ('b', 2), ('r', 2)]

subtract([iterable-or-mapping])

   Elements are subtracted from an *iterable* or from another
   *mapping* (or counter).  Like "dict.update()" but subtracts
   counts instead of replacing them.  Both inputs and outputs may
   be zero or negative.

   >>> c = Counter(a=4, b=2, c=0, d=-2)
   >>> d = Counter(a=1, b=2, c=3, d=4)
   >>> c.subtract(d)
   >>> c
   Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

   Added in version 3.2.

total()

   Compute the sum of the counts.

   >>> c = Counter(a=10, b=5, c=0)
   >>> c.total()
   15

   Added in version 3.10.

The usual dictionary methods are available for "Counter" objects
except for two which work differently for counters.

fromkeys(iterable)

   This class method is not implemented for "Counter" objects.

update([iterable-or-mapping])

   Elements are counted from an *iterable* or added-in from another
   *mapping* (or counter).  Like "dict.update()" but adds counts
   instead of replacing them.  Also, the *iterable* is expected to
   be a sequence of elements, not a sequence of "(key, value)"
   pairs.

```

Counters support rich comparison operators for equality, subset, and
superset relationships: "==", "!=", "<", "<=", ">", ">=". All of those
tests treat missing elements as having zero counts so that
"Counter(a=1) == Counter(a=1, b=0)" returns true.

Changed in version 3.10: Rich comparison operations were added.

Changed in version 3.10: In equality tests, missing elements are
treated as having zero counts. Formerly, "Counter(a=3)" and
"Counter(a=3, b=0)" were considered distinct.

Common patterns for working with "Counter" objects:

   c.total()                       # total of all counts
   c.clear()                       # reset all counts
   list(c)                         # list unique elements
   set(c)                          # convert to a set
   dict(c)                         # convert to a regular dictionary
   c.items()                       # convert to a list of (elem, cnt) pairs

```python
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts

```

Several mathematical operations are provided for combining "Counter"
objects to produce multisets (counters that have counts greater than
zero). Addition and subtraction combine counters by adding or
subtracting the counts of corresponding elements.  Intersection and
union return the minimum and maximum of corresponding counts.
Equality and inclusion compare corresponding counts.  Each operation
can accept inputs with signed counts, but the output will exclude
results with counts of zero or less.

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
>>> c == d                      # equality:  c[x] == d[x]
False
>>> c <= d                      # inclusion:  c[x] <= d[x]
False

```

Unary addition and subtraction are shortcuts for adding an empty
counter or subtracting from an empty counter.

>>> c = Counter(a=2, b=-4)
>>> +c
Counter({'a': 2})
>>> -c
Counter({'b': 4})

Added in version 3.3: Added support for unary plus, unary minus, and
in-place multiset operations.

Note:

  Counters were primarily designed to work with positive integers to
  represent running counts; however, care was taken to not
  unnecessarily preclude use cases needing other types or negative
  values.  To help with those use cases, this section documents the
  minimum range and type restrictions.

  * The "Counter" class itself is a dictionary subclass with no
    restrictions on its keys and values.  The values are intended to
    be numbers representing counts, but you *could* store anything in
    the value field.

  * The "most_common()" method requires only that the values be
    orderable.

  * For in-place operations such as "c[key] += 1", the value type need
    only support addition and subtraction.  So fractions, floats, and
    decimals would work and negative values are supported.  The same

```python
is also true for "update()" and "subtract()" which allow negative
and zero values for both inputs and outputs.

```

  * The multiset methods are designed only for use cases with positive
    values. The inputs may be negative or zero, but only outputs with
    positive values are created.  There are no type restrictions, but
    the value type needs to support addition, subtraction, and
    comparison.

  * The "elements()" method requires integer counts.  It ignores zero
    and negative counts.

See also:

  * Bag class in Smalltalk.

  * Wikipedia entry for Multisets.

  * C++ multisets tutorial with examples.

  * For mathematical operations on multisets and their use cases, see
    *Knuth, Donald. The Art of Computer Programming Volume II, Section
    4.6.3, Exercise 19*.

  * To enumerate all distinct multisets of a given size over a given
    set of elements, see "itertools.combinations_with_replacement()":

       map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC

"deque" objects
===============

class collections.deque([iterable[, maxlen]])

   Returns a new deque object initialized left-to-right (using

```python
"append()") with data from *iterable*.  If *iterable* is not
```
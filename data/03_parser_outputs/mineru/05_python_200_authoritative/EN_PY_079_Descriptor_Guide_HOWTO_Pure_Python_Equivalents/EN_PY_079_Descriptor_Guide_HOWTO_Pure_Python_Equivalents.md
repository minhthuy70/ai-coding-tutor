<!-- page: 1 -->
# EN_PY_079: Descriptor Guide HOWTO: Pure Python Equivalents of Properties and Method Binding

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Advanced OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

-----------------

Here are three practical data validation utilities:

1. "OneOf" verifies that a value is one of a restricted set of
   options.

2. "Number" verifies that a value is either an "int" or "float".
   Optionally, it verifies that a value is between a given minimum or
   maximum.

3. "String" verifies that a value is a "str".  Optionally, it
   validates a given minimum or maximum length.  It can validate a
   user-defined predicate as well.

```python
class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')

class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )

class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} to be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f'Expected {self.predicate} to be true for {value!r}'
            )


```

<!-- page: 2 -->

Practical application
---------------------

Here’s how the data validators can be used in a real class:

```python
class Component:

    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf('wood', 'metal', 'plastic')
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity

```
The descriptors prevent invalid instances from being created:

```python
>>> Component('Widget', 'metal', 5)      # Blocked: 'Widget' is not all uppercase
Traceback (most recent call last):
    ...
ValueError: Expected <method 'isupper' of 'str' objects> to be true for 'Widget'

>>> Component('WIDGET', 'metle', 5)      # Blocked: 'metle' is misspelled
Traceback (most recent call last):
    ...
ValueError: Expected 'metle' to be one of {'metal', 'plastic', 'wood'}

>>> Component('WIDGET', 'metal', -5)     # Blocked: -5 is negative
Traceback (most recent call last):
    ...
ValueError: Expected -5 to be at least 0
>>> Component('WIDGET', 'metal', 'V')    # Blocked: 'V' isn't a number
Traceback (most recent call last):
    ...
TypeError: Expected 'V' to be an int or float

>>> c = Component('WIDGET', 'metal', 5)  # Allowed:  The inputs are valid


```
Technical Tutorial

<!-- page: 3 -->

==================

What follows is a more technical tutorial for the mechanics and
details of how descriptors work.


Abstract
--------

Defines descriptors, summarizes the protocol, and shows how
descriptors are called.  Provides an example showing how object
relational mappings work.

Learning about descriptors not only provides access to a larger
toolset, it creates a deeper understanding of how Python works.


Definition and introduction
---------------------------

In general, a descriptor is an attribute value that has one of the
methods in the descriptor protocol.  Those methods are "__get__()",
"__set__()", and "__delete__()".  If any of those methods are defined
for an attribute, it is said to be a *descriptor*.

The default behavior for attribute access is to get, set, or delete
the attribute from an object’s dictionary.  For instance, "a.x" has a
lookup chain starting with "a.__dict__['x']", then
"type(a).__dict__['x']", and continuing through the method resolution
order of "type(a)". If the looked-up value is an object defining one
of the descriptor methods, then Python may override the default
behavior and invoke the descriptor method instead. Where this occurs
in the precedence chain depends on which descriptor methods were
defined.

Descriptors are a powerful, general purpose protocol.  They are the
mechanism behind properties, methods, static methods, class methods,
and "super()".  They are used throughout Python itself.  Descriptors
simplify the underlying C code and offer a flexible set of new tools
for everyday Python programs.


Descriptor protocol
-------------------


<!-- page: 4 -->

"descr.__get__(self, obj, type=None)"

"descr.__set__(self, obj, value)"

"descr.__delete__(self, obj)"

That is all there is to it.  Define any of these methods and an object
is considered a descriptor and can override default behavior upon
being looked up as an attribute.

If an object defines "__set__()" or "__delete__()", it is considered a
data descriptor.  Descriptors that only define "__get__()" are called
non-data descriptors (they are often used for methods but other uses
are possible).

Data and non-data descriptors differ in how overrides are calculated
with respect to entries in an instance’s dictionary.  If an instance’s
dictionary has an entry with the same name as a data descriptor, the
data descriptor takes precedence.  If an instance’s dictionary has an
entry with the same name as a non-data descriptor, the dictionary
entry takes precedence.

To make a read-only data descriptor, define both "__get__()" and
"__set__()" with the "__set__()" raising an "AttributeError" when
called.  Defining the "__set__()" method with an exception raising
placeholder is enough to make it a data descriptor.


Overview of descriptor invocation
---------------------------------

A descriptor can be called directly with "desc.__get__(obj)" or
"desc.__get__(None, cls)".

But it is more common for a descriptor to be invoked automatically
from attribute access.

The expression "obj.x" looks up the attribute "x" in the chain of
namespaces for "obj".  If the search finds a descriptor outside of the
instance "__dict__", its "__get__()" method is invoked according to
the precedence rules listed below.

The details of invocation depend on whether "obj" is an object, class,
or instance of super.


<!-- page: 5 -->


Invocation from an instance
---------------------------

Instance lookup scans through a chain of namespaces giving data
descriptors the highest priority, followed by instance variables, then
non-data descriptors, then class variables, and lastly "__getattr__()"
if it is provided.

If a descriptor is found for "a.x", then it is invoked with:
"desc.__get__(a, type(a))".

The logic for a dotted lookup is in "object.__getattribute__()".  Here
is a pure Python equivalent:

```python
def find_name_in_mro(cls, name, default):
    "Emulate _PyType_Lookup() in Objects/typeobject.c"
    for base in cls.__mro__:
        if name in vars(base):
            return vars(base)[name]
    return default

def object_getattribute(obj, name):
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
    null = object()
    objtype = type(obj)
    cls_var = find_name_in_mro(objtype, name, null)
    descr_get = getattr(type(cls_var), '__get__', null)
    if descr_get is not null:
        if (hasattr(type(cls_var), '__set__')
            or hasattr(type(cls_var), '__delete__')):
            return descr_get(cls_var, obj, objtype)     # data descriptor
    if hasattr(obj, '__dict__') and name in vars(obj):
        return vars(obj)[name]                          # instance variable
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype)         # non-data descriptor
    if cls_var is not null:
        return cls_var                                  # class variable
    raise AttributeError(name)

```
Note, there is no "__getattr__()" hook in the "__getattribute__()"
code.  That is why calling "__getattribute__()" directly or with
"super().__getattribute__" will bypass "__getattr__()" entirely.

<!-- page: 6 -->


Instead, it is the dot operator and the "getattr()" function that are
responsible for invoking "__getattr__()" whenever "__getattribute__()"
raises an "AttributeError".  Their logic is encapsulated in a helper
function:

```python
def getattr_hook(obj, name):
    "Emulate slot_tp_getattr_hook() in Objects/typeobject.c"
    try:
        return obj.__getattribute__(name)
    except AttributeError:
        if not hasattr(type(obj), '__getattr__'):
            raise
    return type(obj).__getattr__(obj, name)             # __getattr__


```
Invocation from a class
-----------------------

The logic for a dotted lookup such as "A.x" is in
"type.__getattribute__()".  The steps are similar to those for
"object.__getattribute__()" but the instance dictionary lookup is
replaced by a search through the class’s *method resolution order*.

If a descriptor is found, it is invoked with "desc.__get__(None, A)".

The full C implementation can be found in "type_getattro()" and
"_PyType_Lookup()" in Objects/typeobject.c.


Invocation from super
---------------------

The logic for super’s dotted lookup is in the "__getattribute__()"
method for object returned by "super()".

A dotted lookup such as "super(A, obj).m" searches
"obj.__class__.__mro__" for the base class "B" immediately following
"A" and then returns "B.__dict__['m'].__get__(obj, A)".  If not a
descriptor, "m" is returned unchanged.

The full C implementation can be found in "super_getattro()" in
Objects/typeobject.c.  A pure Python equivalent can be found in

<!-- page: 7 -->

Guido’s Tutorial.


Summary of invocation logic
---------------------------

The mechanism for descriptors is embedded in the "__getattribute__()"
methods for "object", "type", and "super()".

The important points to remember are:

* Descriptors are invoked by the "__getattribute__()" method.

* Classes inherit this machinery from "object", "type", or "super()".

* Overriding "__getattribute__()" prevents automatic descriptor calls
  because all the descriptor logic is in that method.

* "object.__getattribute__()" and "type.__getattribute__()" make
  different calls to "__get__()".  The first includes the instance and
  may include the class.  The second puts in "None" for the instance
  and always includes the class.

* Data descriptors always override instance dictionaries.

* Non-data descriptors may be overridden by instance dictionaries.


Automatic name notification
---------------------------

Sometimes it is desirable for a descriptor to know what class variable
name it was assigned to.  When a new class is created, the "type"
metaclass scans the dictionary of the new class.  If any of the
entries are descriptors and if they define "__set_name__()", that
method is called with two arguments.  The *owner* is the class where
the descriptor is used, and the *name* is the class variable the
descriptor was assigned to.

The implementation details are in "type_new()" and "set_names()" in
Objects/typeobject.c.

Since the update logic is in "type.__new__()", notifications only take
place at the time of class creation.  If descriptors are added to the
class afterwards, "__set_name__()" will need to be called manually.

<!-- page: 8 -->



ORM example
-----------

The following code is a simplified skeleton showing how data
descriptors could be used to implement an object relational mapping.

The essential idea is that the data is stored in an external database.
The Python instances only hold keys to the database’s tables.
Descriptors take care of lookups or updates:

```python
class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchone()[0]

    def __set__(self, obj, value):
        conn.execute(self.store, [value, obj.key])
        conn.commit()

```
We can use the "Field" class to define models that describe the schema
for each table in a database:

```python
class Movie:
    table = 'Movies'                    # Table name
    key = 'title'                       # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

class Song:
    table = 'Music'
    key = 'title'
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key):
        self.key = key

```

<!-- page: 9 -->

To use the models, first connect to the database:

```python
>>> import sqlite3
>>> conn = sqlite3.connect('entertainment.db')

```
An interactive session shows how data is retrieved from the database
and how it can be updated:

```python
>>> Movie('Star Wars').director
'George Lucas'
>>> jaws = Movie('Jaws')
>>> f'Released in {jaws.year} by {jaws.director}'
'Released in 1975 by Steven Spielberg'

>>> Song('Country Roads').artist
'John Denver'

>>> Movie('Star Wars').director = 'J.J. Abrams'
>>> Movie('Star Wars').director
'J.J. Abrams'


```
Pure Python Equivalents
=======================
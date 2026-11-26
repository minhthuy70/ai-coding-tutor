# EN_PY_078: Descriptor Guide HOWTO: Property Implementation, Methods, Static/Class Methods

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Advanced OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

Descriptor Guide
****************

Author:
   Raymond Hettinger

Contact:
   <python at rcn dot com>

Contents
^^^^^^^^

* Descriptor Guide

  * Primer

    * Simple example: A descriptor that returns a constant

    * Dynamic lookups

    * Managed attributes

    * Customized names

    * Closing thoughts

  * Complete Practical Example

    * Validator class

    * Custom validators

    * Practical application

  * Technical Tutorial

    * Abstract

    * Definition and introduction

    * Descriptor protocol

    * Overview of descriptor invocation

```python
* Invocation from an instance

* Invocation from a class

* Invocation from super

* Summary of invocation logic

* Automatic name notification

* ORM example

```

  * Pure Python Equivalents

    * Properties

    * Functions and methods

    * Kinds of methods

    * Static methods

    * Class methods

    * Member objects and __slots__

*Descriptors* let objects customize attribute lookup, storage, and
deletion.

This guide has four major sections:

1. The “primer” gives a basic overview, moving gently from simple

```python
examples, adding one feature at a time.  Start here if you’re new
to descriptors.

```

2. The second section shows a complete, practical descriptor example.
   If you already know the basics, start there.

3. The third section provides a more technical tutorial that goes into
   the detailed mechanics of how descriptors work.  Most people don’t
   need this level of detail.

4. The last section has pure Python equivalents for built-in

```python
descriptors that are written in C.  Read this if you’re curious
about how functions turn into bound methods or about the
implementation of common tools like "classmethod()",
"staticmethod()", "property()", and *__slots__*.

```

Primer
======

In this primer, we start with the most basic possible example and then
we’ll add new capabilities one by one.

Simple example: A descriptor that returns a constant
----------------------------------------------------

The "Ten" class is a descriptor whose "__get__()" method always
returns the constant "10":

```python
class Ten:
    def __get__(self, obj, objtype=None):
        return 10

```

To use the descriptor, it must be stored as a class variable in
another class:

```python
class A:
    x = 5                       # Regular class attribute
    y = Ten()                   # Descriptor instance

```

An interactive session shows the difference between normal attribute
lookup and descriptor lookup:

```python
>>> a = A()                     # Make an instance of class A
>>> a.x                         # Normal attribute lookup
5
>>> a.y                         # Descriptor lookup
10

```

In the "a.x" attribute lookup, the dot operator finds "'x': 5" in the
class dictionary.  In the "a.y" lookup, the dot operator finds a
descriptor instance, recognized by its "__get__" method. Calling that
method returns "10".

Note that the value "10" is not stored in either the class dictionary
or the instance dictionary.  Instead, the value "10" is computed on
demand.

This example shows how a simple descriptor works, but it isn’t very
useful. For retrieving constants, normal attribute lookup would be
better.

In the next section, we’ll create something more useful, a dynamic
lookup.

Dynamic lookups
---------------

Interesting descriptors typically run computations instead of
returning constants:

```python
import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

```

An interactive session shows that the lookup is dynamic — it computes
different, updated answers each time:

```python
>>> s = Directory('songs')
>>> g = Directory('games')
>>> s.size                              # The songs directory has twenty files
20
>>> g.size                              # The games directory has three files
3
>>> os.remove('games/chess')            # Delete a game
>>> g.size                              # File count is automatically updated
2

```

Besides showing how descriptors can run computations, this example
also reveals the purpose of the parameters to "__get__()".  The *self*
parameter is *size*, an instance of *DirectorySize*.  The *obj*
parameter is either *g* or *s*, an instance of *Directory*.  It is the
*obj* parameter that lets the "__get__()" method learn the target
directory.  The *objtype* parameter is the class *Directory*.

Managed attributes
------------------

A popular use for descriptors is managing access to instance data.
The descriptor is assigned to a public attribute in the class
dictionary while the actual data is stored as a private attribute in
the instance dictionary.  The descriptor’s "__get__()" and "__set__()"
methods are triggered when the public attribute is accessed.

In the following example, *age* is the public attribute and *_age* is
the private attribute.  When the public attribute is accessed, the
descriptor logs the lookup or update:

```python
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1                   # Calls both __get__() and __set__()

```

An interactive session shows that all access to the managed attribute
*age* is logged, but that the regular attribute *name* is not logged:

```python
>>> mary = Person('Mary M', 30)         # The initial age update is logged
INFO:root:Updating 'age' to 30
>>> dave = Person('David D', 40)
INFO:root:Updating 'age' to 40

>>> vars(mary)                          # The actual data is in a private attribute
{'name': 'Mary M', '_age': 30}
>>> vars(dave)
{'name': 'David D', '_age': 40}

>>> mary.age                            # Access the data and log the lookup
INFO:root:Accessing 'age' giving 30
30
>>> mary.birthday()                     # Updates are logged as well
INFO:root:Accessing 'age' giving 30
INFO:root:Updating 'age' to 31

>>> dave.name                           # Regular attribute lookup isn't logged
'David D'
>>> dave.age                            # Only the managed attribute is logged
INFO:root:Accessing 'age' giving 40
40

```

One major issue with this example is that the private name *_age* is
hardwired in the *LoggedAgeAccess* class.  That means that each
instance can only have one logged attribute and that its name is
unchangeable.  In the next example, we’ll fix that problem.

Customized names
----------------

When a class uses descriptors, it can inform each descriptor about
which variable name was used.

In this example, the "Person" class has two descriptor instances,
*name* and *age*.  When the "Person" class is defined, it makes a
callback to "__set_name__()" in *LoggedAccess* so that the field names
can be recorded, giving each descriptor its own *public_name* and
*private_name*:

```python
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)

class Person:

    name = LoggedAccess()                # First descriptor instance
    age = LoggedAccess()                 # Second descriptor instance

    def __init__(self, name, age):
        self.name = name                 # Calls the first descriptor
        self.age = age                   # Calls the second descriptor

    def birthday(self):
        self.age += 1

```

An interactive session shows that the "Person" class has called
"__set_name__()" so that the field names would be recorded.  Here we
call "vars()" to look up the descriptor without triggering it:

```python
>>> vars(vars(Person)['name'])
{'public_name': 'name', 'private_name': '_name'}
>>> vars(vars(Person)['age'])
{'public_name': 'age', 'private_name': '_age'}

```

The new class now logs access to both *name* and *age*:

```python
>>> pete = Person('Peter P', 10)
INFO:root:Updating 'name' to 'Peter P'
INFO:root:Updating 'age' to 10
>>> kate = Person('Catherine C', 20)
INFO:root:Updating 'name' to 'Catherine C'
INFO:root:Updating 'age' to 20

```

The two *Person* instances contain only the private names:

```python
>>> vars(pete)
{'_name': 'Peter P', '_age': 10}
>>> vars(kate)
{'_name': 'Catherine C', '_age': 20}

```

Closing thoughts
----------------

A *descriptor* is what we call any object that defines "__get__()",
"__set__()", or "__delete__()".

Optionally, descriptors can have a "__set_name__()" method.  This is
only used in cases where a descriptor needs to know either the class
where it was created or the name of class variable it was assigned to.
(This method, if present, is called even if the class is not a
descriptor.)

Descriptors get invoked by the dot operator during attribute lookup.
If a descriptor is accessed indirectly with
"vars(some_class)[descriptor_name]", the descriptor instance is
returned without invoking it.

Descriptors only work when used as class variables.  When put in
instances, they have no effect.

The main motivation for descriptors is to provide a hook allowing
objects stored in class variables to control what happens during
attribute lookup.

Traditionally, the calling class controls what happens during lookup.
Descriptors invert that relationship and allow the data being looked-
up to have a say in the matter.

Descriptors are used throughout the language.  It is how functions
turn into bound methods.  Common tools like "classmethod()",
"staticmethod()", "property()", and "functools.cached_property()" are
all implemented as descriptors.

Complete Practical Example
==========================

In this example, we create a practical and powerful tool for locating
notoriously hard to find data corruption bugs.

Validator class
---------------

A validator is a descriptor for managed attribute access.  Prior to
storing any data, it verifies that the new value meets various type
and range restrictions.  If those restrictions aren’t met, it raises
an exception to prevent data corruption at its source.

This "Validator" class is both an *abstract base class* and a managed
attribute descriptor:

```python
from abc import ABC, abstractmethod

class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass

```

Custom validators need to inherit from "Validator" and must supply a
"validate()" method to test various restrictions as needed.

Custom validators
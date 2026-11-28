# EN_PY_070: Emulating Numeric Types: Operator Overloading (__add__, __sub__, __mul__, __pow__)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Magic Methods | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

This class object is the one that will be referenced by the zero-
argument form of "super()". "__class__" is an implicit closure
reference created by the compiler if any methods in a class body refer
to either "__class__" or "super". This allows the zero argument form
of "super()" to correctly identify the class being defined based on
lexical scoping, while the class or instance that was used to make the
current call is identified based on the first argument passed to the
method.

**CPython implementation detail:** In CPython 3.6 and later, the
"__class__" cell is passed to the metaclass as a "__classcell__" entry
in the class namespace. If present, this must be propagated up to the
"type.__new__" call in order for the class to be initialised
correctly. Failing to do so will result in a "RuntimeError" in Python
3.8.

When using the default metaclass "type", or any metaclass that
ultimately calls "type.__new__", the following additional
customization steps are invoked after creating the class object:

1. The "type.__new__" method collects all of the attributes in the

```python
class namespace that define a "__set_name__()" method;

```

2. Those "__set_name__" methods are called with the class being
   defined and the assigned name of that particular attribute;

3. The "__init_subclass__()" hook is called on the immediate parent of

```python
the new class in its method resolution order.

```

After the class object is created, it is passed to the class
decorators included in the class definition (if any) and the resulting
object is bound in the local namespace as the defined class.

When a new class is created by "type.__new__", the object provided as
the namespace parameter is copied to a new ordered mapping and the
original object is discarded. The new copy is wrapped in a read-only
proxy, which becomes the "__dict__" attribute of the class object.

See also:

  **PEP 3135** - New super
     Describes the implicit "__class__" closure reference

3.3.3.7. Uses for metaclasses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The potential uses for metaclasses are boundless. Some ideas that have
been explored include enum, logging, interface checking, automatic
delegation, automatic property creation, proxies, frameworks, and
automatic resource locking/synchronization.

3.3.4. Customizing instance and subclass checks
-----------------------------------------------

The following methods are used to override the default behavior of the
"isinstance()" and "issubclass()" built-in functions.

In particular, the metaclass "abc.ABCMeta" implements these methods in
order to allow the addition of Abstract Base Classes (ABCs) as
“virtual base classes” to any class or type (including built-in
types), including other ABCs.

type.__instancecheck__(self, instance)

```python
Return true if *instance* should be considered a (direct or
indirect) instance of *class*. If defined, called to implement
"isinstance(instance, class)".

```

type.__subclasscheck__(self, subclass)

```python
Return true if *subclass* should be considered a (direct or
indirect) subclass of *class*.  If defined, called to implement
"issubclass(subclass, class)".

```

Note that these methods are looked up on the type (metaclass) of a
class.  They cannot be defined as class methods in the actual class.
This is consistent with the lookup of special methods that are called
on instances, only in this case the instance is itself a class.

See also:

  **PEP 3119** - Introducing Abstract Base Classes

```python
Includes the specification for customizing "isinstance()" and
"issubclass()" behavior through "__instancecheck__()" and
"__subclasscheck__()", with motivation for this functionality in
the context of adding Abstract Base Classes (see the "abc"
module) to the language.

```

3.3.5. Emulating generic types
------------------------------

When using *type annotations*, it is often useful to *parameterize* a
*generic type* using Python’s square-brackets notation. For example,
the annotation "list[int]" might be used to signify a "list" in which
all the elements are of type "int".

See also:

  **PEP 484** - Type Hints

```python
Introducing Python’s framework for type annotations

```

  Generic Alias Types

```python
Documentation for objects representing parameterized generic
classes

```

  Generics, user-defined generics and "typing.Generic"

     Documentation on how to implement generic classes that can be
     parameterized at runtime and understood by static type-checkers.

A class can *generally* only be parameterized if it defines the
special class method "__class_getitem__()".

classmethod object.__class_getitem__(cls, key)

   Return an object representing the specialization of a generic class
   by type arguments found in *key*.

   When defined on a class, "__class_getitem__()" is automatically a

```python
class method. As such, there is no need for it to be decorated with
"@classmethod" when it is defined.

```

3.3.5.1. The purpose of *__class_getitem__*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of "__class_getitem__()" is to allow runtime
parameterization of standard-library generic classes in order to more
easily apply *type hints* to these classes.

To implement custom generic classes that can be parameterized at
runtime and understood by static type-checkers, users should either
inherit from a standard library class that already implements
"__class_getitem__()", or inherit from "typing.Generic", which has its
own implementation of "__class_getitem__()".

Custom implementations of "__class_getitem__()" on classes defined
outside of the standard library may not be understood by third-party
type-checkers such as mypy. Using "__class_getitem__()" on any class
for purposes other than type hinting is discouraged.

3.3.5.2. *__class_getitem__* versus *__getitem__*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually, the subscription of an object using square brackets will call
the "__getitem__()" instance method defined on the object’s class.
However, if the object being subscribed is itself a class, the class
method "__class_getitem__()" may be called instead.
"__class_getitem__()" should return a GenericAlias object if it is

properly defined.

Presented with the *expression* "obj[x]", the Python interpreter
follows something like the following process to decide whether
"__getitem__()" or "__class_getitem__()" should be called:

```python
from inspect import isclass

def subscribe(obj, x):
    """Return the result of the expression 'obj[x]'"""

    class_of_obj = type(obj)

    # If the class of obj defines __getitem__,
    # call class_of_obj.__getitem__(obj, x)
    if hasattr(class_of_obj, '__getitem__'):
        return class_of_obj.__getitem__(obj, x)

    # Else, if obj is a class and defines __class_getitem__,
    # call obj.__class_getitem__(x)
    elif isclass(obj) and hasattr(obj, '__class_getitem__'):
        return obj.__class_getitem__(x)

    # Else, raise an exception
    else:
        raise TypeError(
            f"'{class_of_obj.__name__}' object is not subscriptable"
        )

```

In Python, all classes are themselves instances of other classes. The
class of a class is known as that class’s *metaclass*, and most
classes have the "type" class as their metaclass. "type" does not
define "__getitem__()", meaning that expressions such as "list[int]",
"dict[str, float]" and "tuple[str, bytes]" all result in
"__class_getitem__()" being called:

```python
>>> # list has class "type" as its metaclass, like most classes:
>>> type(list)
<class 'type'>
>>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
True
>>> # "list[int]" calls "list.__class_getitem__(int)"
>>> list[int]
list[int]
>>> # list.__class_getitem__ returns a GenericAlias object:
>>> type(list[int])
<class 'types.GenericAlias'>

```

However, if a class has a custom metaclass that defines
"__getitem__()", subscribing the class may result in different
behaviour. An example of this can be found in the "enum" module:

```python
>>> from enum import Enum
>>> class Menu(Enum):
...     """A breakfast menu"""
...     SPAM = 'spam'
...     BACON = 'bacon'
>>> # Enum classes have a custom metaclass:
>>> type(Menu)
<class 'enum.EnumMeta'>
>>> # EnumMeta defines __getitem__,
>>> # so __class_getitem__ is not called,
>>> # and the result is not a GenericAlias object:
>>> Menu['SPAM']
<Menu.SPAM: 'spam'>
>>> type(Menu['SPAM'])
<enum 'Menu'>

```

See also:

  **PEP 560** - Core Support for typing module and generic types
     Introducing "__class_getitem__()", and outlining when a
     subscription results in "__class_getitem__()" being called
     instead of "__getitem__()"

3.3.6. Emulating callable objects
---------------------------------

object.__call__(self[, args...])

```python
Called when the instance is “called” as a function; if this method
is defined, "x(arg1, arg2, ...)" roughly translates to
"type(x).__call__(x, arg1, ...)". The "object" class itself does
not provide this method.

```

3.3.7. Emulating container types

--------------------------------

The following methods can be defined to implement container objects.
None of them are provided by the "object" class itself. Containers
usually are *sequences* (such as "lists" or "tuples") or *mappings*
(like *dictionaries*), but can represent other containers as well.
The first set of methods is used either to emulate a sequence or to
emulate a mapping; the difference is that for a sequence, the
allowable keys should be the integers *k* for which "0 <= k < N" where
*N* is the length of the sequence, or "slice" objects, which define a
range of items.  It is also recommended that mappings provide the
methods "keys()", "values()", "items()", "get()", "clear()",
"setdefault()", "pop()", "popitem()", "copy()", and "update()"
behaving similar to those for Python’s standard "dictionary" objects.
The "collections.abc" module provides a "MutableMapping" *abstract
base class* to help create those methods from a base set of
"__getitem__()", "__setitem__()", "__delitem__()", and "keys()".
Mutable sequences should provide methods "append()", "count()",
"index()", "extend()", "insert()", "pop()", "remove()", "reverse()"
and "sort()", like Python standard "list" objects. Finally, sequence
types should implement addition (meaning concatenation) and
multiplication (meaning repetition) by defining the methods
"__add__()", "__radd__()", "__iadd__()", "__mul__()", "__rmul__()" and
"__imul__()" described below; they should not define other numerical
operators.  It is recommended that both mappings and sequences
implement the "__contains__()" method to allow efficient use of the
"in" operator; for mappings, "in" should search the mapping’s keys;
for sequences, it should search through the values.  It is further
recommended that both mappings and sequences implement the
"__iter__()" method to allow efficient iteration through the
container; for mappings, "__iter__()" should iterate through the
object’s keys; for sequences, it should iterate through the values.

object.__len__(self)

   Called to implement the built-in function "len()".  Should return
   the length of the object, an integer ">=" 0.  Also, an object that
   doesn’t define a "__bool__()" method and whose "__len__()" method
   returns zero is considered to be false in a Boolean context.

   **CPython implementation detail:** In CPython, the length is
   required to be at most "sys.maxsize". If the length is larger than
   "sys.maxsize" some features (such as "len()") may raise
   "OverflowError".  To prevent raising "OverflowError" by truth value
   testing, an object must define a "__bool__()" method.

object.__length_hint__(self)

```python
Called to implement "operator.length_hint()". Should return an
estimated length for the object (which may be greater or less than
the actual length). The length must be an integer ">=" 0. The
return value may also be "NotImplemented", which is treated the
same as if the "__length_hint__" method didn’t exist at all. This
method is purely an optimization and is never required for
correctness.

Added in version 3.4.

```

Note:

  Slicing is done exclusively with the following three methods.  A
  call like

     a[1:2] = b

  is translated to

     a[slice(1, 2, None)] = b

  and so forth.  Missing slice items are always filled in with "None".

object.__getitem__(self, key)

   Called to implement evaluation of "self[key]". For *sequence*
   types, the accepted keys should be integers. Optionally, they may
   support "slice" objects as well.  Negative index support is also
   optional. If *key* is of an inappropriate type, "TypeError" may be

```python
raised; if *key* is a value outside the set of indexes for the
sequence (after any special interpretation of negative values),
"IndexError" should be raised. For *mapping* types, if *key* is
missing (not in the container), "KeyError" should be raised.

Note:

  "for" loops expect that an "IndexError" will be raised for
  illegal indexes to allow proper detection of the end of the
  sequence.

Note:

  When subscripting a *class*, the special class method
  "__class_getitem__()" may be called instead of "__getitem__()".
  See __class_getitem__ versus __getitem__ for more details.

```

object.__setitem__(self, key, value)

   Called to implement assignment to "self[key]".  Same note as for

```python
"__getitem__()".  This should only be implemented for mappings if
the objects support changes to the values for keys, or if new keys
can be added, or for sequences if elements can be replaced.  The
same exceptions should be raised for improper *key* values as for
the "__getitem__()" method.

```

object.__delitem__(self, key)

   Called to implement deletion of "self[key]".  Same note as for

```python
"__getitem__()".  This should only be implemented for mappings if
the objects support removal of keys, or for sequences if elements
```
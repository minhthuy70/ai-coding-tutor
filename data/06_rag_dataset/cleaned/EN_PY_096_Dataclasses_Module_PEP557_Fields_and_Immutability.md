# EN_PY_096: dataclasses Module (PEP 557): @dataclass, field(), and frozen Immutability

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Modern Python | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

"dataclasses" — Data Classes
****************************

**Source code:** Lib/dataclasses.py

======================================================================

This module provides a decorator and functions for automatically
adding generated *special methods* such as "__init__()" and
"__repr__()" to user-defined classes.  It was originally described in
**PEP 557**.

The member variables to use in these generated methods are defined
using **PEP 526** type annotations.  For example, this code:

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

```

will add, among other things, a "__init__()" that looks like:

```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand

```

Note that this method is automatically added to the class: it is not
directly specified in the "InventoryItem" definition shown above.

Added in version 3.7.

Module contents
===============

@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)

   This function is a *decorator* that is used to add generated
   *special methods* to classes, as described below.

```python
The "@dataclass" decorator examines the class to find "field"s.  A
"field" is defined as a class variable that has a *type
annotation*.  With two exceptions described below, nothing in
"@dataclass" examines the type specified in the variable
annotation.

The order of the fields in all of the generated methods is the
order in which they appear in the class definition.

The "@dataclass" decorator will add various “dunder” methods to the
class, described below.  If any of the added methods already exist
in the class, the behavior depends on the parameter, as documented
below. The decorator returns the same class that it is called on;
no new class is created.

If "@dataclass" is used just as a simple decorator with no
parameters, it acts as if it has the default values documented in
this signature.  That is, these three uses of "@dataclass" are
equivalent:

   @dataclass
   class C:
       ...

   @dataclass()
   class C:
       ...

   @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
              match_args=True, kw_only=False, slots=False, weakref_slot=False)
   class C:
       ...

The parameters to "@dataclass" are:

* *init*: If true (the default), a "__init__()" method will be
  generated.

  If the class already defines "__init__()", this parameter is
  ignored.

* *repr*: If true (the default), a "__repr__()" method will be
  generated.  The generated repr string will have the class name
  and the name and repr of each field, in the order they are
  defined in the class.  Fields that are marked as being excluded
  from the repr are not included.  For example:
  "InventoryItem(name='widget', unit_price=3.0,
  quantity_on_hand=10)".

  If the class already defines "__repr__()", this parameter is
  ignored.

* *eq*: If true (the default), an "__eq__()" method will be
  generated.  This method compares the class as if it were a tuple
  of its fields, in order.  Both instances in the comparison must
  be of the identical type.

  If the class already defines "__eq__()", this parameter is
  ignored.

* *order*: If true (the default is "False"), "__lt__()",
  "__le__()", "__gt__()", and "__ge__()" methods will be generated.
  These compare the class as if it were a tuple of its fields, in
  order.  Both instances in the comparison must be of the identical
  type.  If *order* is true and *eq* is false, a "ValueError" is
  raised.

  If the class already defines any of "__lt__()", "__le__()",
  "__gt__()", or "__ge__()", then "TypeError" is raised.

* *unsafe_hash*: If "False" (the default), a "__hash__()" method is
  generated according to how *eq* and *frozen* are set.

  "__hash__()" is used by built-in "hash()", and when objects are
  added to hashed collections such as dictionaries and sets.
  Having a "__hash__()" implies that instances of the class are
  immutable. Mutability is a complicated property that depends on
  the programmer’s intent, the existence and behavior of
  "__eq__()", and the values of the *eq* and *frozen* flags in the
  "@dataclass" decorator.

  By default, "@dataclass" will not implicitly add a "__hash__()"
  method unless it is safe to do so.  Neither will it add or change
  an existing explicitly defined "__hash__()" method.  Setting the
  class attribute "__hash__ = None" has a specific meaning to
  Python, as described in the "__hash__()" documentation.

  If "__hash__()" is not explicitly defined, or if it is set to
  "None", then "@dataclass" *may* add an implicit "__hash__()"
  method. Although not recommended, you can force "@dataclass" to
  create a "__hash__()" method with "unsafe_hash=True". This might
  be the case if your class is logically immutable but can still be
  mutated. This is a specialized use case and should be considered
  carefully.

  Here are the rules governing implicit creation of a "__hash__()"
  method.  Note that you cannot both have an explicit "__hash__()"
  method in your dataclass and set "unsafe_hash=True"; this will
  result in a "TypeError".

  If *eq* and *frozen* are both true, by default "@dataclass" will
  generate a "__hash__()" method for you.  If *eq* is true and
  *frozen* is false, "__hash__()" will be set to "None", marking it
  unhashable (which it is, since it is mutable).  If *eq* is false,
  "__hash__()" will be left untouched meaning the "__hash__()"
  method of the superclass will be used (if the superclass is
  "object", this means it will fall back to id-based hashing).

* *frozen*: If true (the default is "False"), assigning to fields
  will generate an exception.  This emulates read-only frozen
  instances.  If "__setattr__()" or "__delattr__()" is defined in
  the class, then "TypeError" is raised.  See the discussion below.

* *match_args*: If true (the default is "True"), the
  "__match_args__" tuple will be created from the list of
  parameters to the generated "__init__()" method (even if
  "__init__()" is not generated, see above).  If false, or if
  "__match_args__" is already defined in the class, then
  "__match_args__" will not be generated.

   Added in version 3.10.

* *kw_only*: If true (the default value is "False"), then all
  fields will be marked as keyword-only.  If a field is marked as
  keyword-only, then the only effect is that the "__init__()"
  parameter generated from a keyword-only field must be specified
  with a keyword when "__init__()" is called.  There is no effect
  on any other aspect of dataclasses.  See the *parameter* glossary
  entry for details.  Also see the "KW_ONLY" section.

   Added in version 3.10.

* *slots*: If true (the default is "False"), "__slots__" attribute
  will be generated and new class will be returned instead of the
  original one. If "__slots__" is already defined in the class,
  then "TypeError" is raised.

   Warning:

     Calling no-arg "super()" in dataclasses using "slots=True"
     will result in the following exception being raised:
     "TypeError: super(type, obj): obj must be an instance or
     subtype of type". The two-arg "super()" is a valid workaround.
     See gh-90562 for full details.

   Warning:

     Passing parameters to a base class "__init_subclass__()" when
     using "slots=True" will result in a "TypeError". Either use
     "__init_subclass__" with no parameters or use default values
     as a workaround. See gh-91126 for full details.

   Added in version 3.10.

   Changed in version 3.11: If a field name is already included in
   the "__slots__" of a base class, it will not be included in the
   generated "__slots__" to prevent overriding them. Therefore, do
   not use "__slots__" to retrieve the field names of a dataclass.
   Use "fields()" instead. To be able to determine inherited slots,
   base class "__slots__" may be any iterable, but *not* an
   iterator.

* *weakref_slot*: If true (the default is "False"), add a slot
  named “__weakref__”, which is required to make an instance
  "weakref-able". It is an error to specify "weakref_slot=True"
  without also specifying "slots=True".

   Added in version 3.11.

"field"s may optionally specify a default value, using normal
Python syntax:

   @dataclass
   class C:
       a: int       # 'a' has no default value
       b: int = 0   # assign a default value for 'b'

In this example, both "a" and "b" will be included in the added
"__init__()" method, which will be defined as:

   def __init__(self, a: int, b: int = 0):

"TypeError" will be raised if a field without a default value
follows a field with a default value.  This is true whether this
occurs in a single class, or as a result of class inheritance.

```

dataclasses.field(*, default=MISSING, default_factory=MISSING, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=MISSING)

   For common and simple use cases, no other functionality is

```python
required.  There are, however, some dataclass features that require
additional per-field information.  To satisfy this need for
additional information, you can replace the default field value
with a call to the provided "field()" function.  For example:

   @dataclass
   class C:
       mylist: list[int] = field(default_factory=list)

   c = C()
   c.mylist += [1, 2, 3]

As shown above, the "MISSING" value is a sentinel object used to
detect if some parameters are provided by the user. This sentinel
is used because "None" is a valid value for some parameters with a
distinct meaning.  No code should directly use the "MISSING" value.

The parameters to "field()" are:

* *default*: If provided, this will be the default value for this
  field.  This is needed because the "field()" call itself replaces
  the normal position of the default value.

* *default_factory*: If provided, it must be a zero-argument
  callable that will be called when a default value is needed for
  this field.  Among other purposes, this can be used to specify
  fields with mutable default values, as discussed below.  It is an
  error to specify both *default* and *default_factory*.

* *init*: If true (the default), this field is included as a
  parameter to the generated "__init__()" method.

* *repr*: If true (the default), this field is included in the
  string returned by the generated "__repr__()" method.

* *hash*: This can be a bool or "None".  If true, this field is
  included in the generated "__hash__()" method.  If "None" (the
  default), use the value of *compare*: this would normally be the
  expected behavior.  A field should be considered in the hash if
  it’s used for comparisons.  Setting this value to anything other
  than "None" is discouraged.

  One possible reason to set "hash=False" but "compare=True" would
  be if a field is expensive to compute a hash value for, that
  field is needed for equality testing, and there are other fields
  that contribute to the type’s hash value.  Even if a field is
  excluded from the hash, it will still be used for comparisons.

* *compare*: If true (the default), this field is included in the
  generated equality and comparison methods ("__eq__()",
  "__gt__()", et al.).

* *metadata*: This can be a mapping or "None". "None" is treated as
  an empty dict.  This value is wrapped in "MappingProxyType()" to
  make it read-only, and exposed on the "Field" object. It is not
  used at all by Data Classes, and is provided as a third-party
  extension mechanism. Multiple third-parties can each have their
  own key, to use as a namespace in the metadata.

* *kw_only*: If true, this field will be marked as keyword-only.
  This is used when the generated "__init__()" method’s parameters
  are computed.

   Added in version 3.10.

If the default value of a field is specified by a call to
"field()", then the class attribute for this field will be replaced
by the specified *default* value.  If *default* is not provided,
then the class attribute will be deleted.  The intent is that after
the "@dataclass" decorator runs, the class attributes will all
contain the default values for the fields, just as if the default
value itself were specified.  For example, after:

   @dataclass
   class C:
       x: int
       y: int = field(repr=False)
       z: int = field(repr=False, default=10)
       t: int = 20

The class attribute "C.z" will be "10", the class attribute "C.t"
will be "20", and the class attributes "C.x" and "C.y" will not be
set.

```

class dataclasses.Field

   "Field" objects describe each defined field. These objects are
   created internally, and are returned by the "fields()" module-level
   method (see below).  Users should never instantiate a "Field"
   object directly.  Its documented attributes are:

   * "name": The name of the field.

   * "type": The type of the field.

   * "default", "default_factory", "init", "repr", "hash", "compare",
     "metadata", and "kw_only" have the identical meaning and values
     as they do in the "field()" function.

   Other attributes may exist, but they are private and must not be
   inspected or relied on.

dataclasses.fields(class_or_instance)

```python
Returns a tuple of "Field" objects that define the fields for this
dataclass.  Accepts either a dataclass, or an instance of a
dataclass. Raises "TypeError" if not passed a dataclass or instance
of one. Does not return pseudo-fields which are "ClassVar" or
"InitVar".

```

dataclasses.asdict(obj, *, dict_factory=dict)

```python
Converts the dataclass *obj* to a dict (by using the factory
function *dict_factory*).  Each dataclass is converted to a dict of
its fields, as "name: value" pairs.  dataclasses, dicts, lists, and
tuples are recursed into.  Other objects are copied with
"copy.deepcopy()".

Example of using "asdict()" on nested dataclasses:

   @dataclass
   class Point:
        x: int
        y: int

   @dataclass
   class C:
        mylist: list[Point]

   p = Point(10, 20)
   assert asdict(p) == {'x': 10, 'y': 20}

   c = C([Point(0, 0), Point(10, 4)])
   assert asdict(c) == {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}

To create a shallow copy, the following workaround may be used:

   {field.name: getattr(obj, field.name) for field in fields(obj)}

"asdict()" raises "TypeError" if *obj* is not a dataclass instance.

```

dataclasses.astuple(obj, *, tuple_factory=tuple)

```python
Converts the dataclass *obj* to a tuple (by using the factory
function *tuple_factory*).  Each dataclass is converted to a tuple
of its field values.  dataclasses, dicts, lists, and tuples are
recursed into. Other objects are copied with "copy.deepcopy()".

Continuing from the previous example:

   assert astuple(p) == (10, 20)
   assert astuple(c) == ([(0, 0), (10, 4)],)

To create a shallow copy, the following workaround may be used:

   tuple(getattr(obj, field.name) for field in dataclasses.fields(obj))

"astuple()" raises "TypeError" if *obj* is not a dataclass
instance.

```

dataclasses.make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False, module=None)

```python
Creates a new dataclass with name *cls_name*, fields as defined in
*fields*, base classes as given in *bases*, and initialized with a
namespace as given in *namespace*.  *fields* is an iterable whose
elements are each either "name", "(name, type)", or "(name, type,
Field)".  If just "name" is supplied, "typing.Any" is used for
"type".  The values of *init*, *repr*, *eq*, *order*,
*unsafe_hash*, *frozen*, *match_args*, *kw_only*, *slots*, and
*weakref_slot* have the same meaning as they do in "@dataclass".

If *module* is defined, the "__module__" attribute of the dataclass
is set to that value. By default, it is set to the module name of
the caller.

This function is not strictly required, because any Python
mechanism for creating a new class with "__annotations__" can then
apply the "@dataclass" function to convert that class to a
dataclass.  This function is provided as a convenience.  For
example:

   C = make_dataclass('C',
                      [('x', int),
                        'y',
                       ('z', int, field(default=5))],
                      namespace={'add_one': lambda self: self.x + 1})

Is equivalent to:

   @dataclass
   class C:
       x: int
       y: 'typing.Any'
       z: int = 5

       def add_one(self):
           return self.x + 1

```

dataclasses.replace(obj, /, **changes)

   Creates a new object of the same type as *obj*, replacing fields

```python
with values from *changes*.  If *obj* is not a Data Class, raises
"TypeError".  If keys in *changes* are not field names of the given
dataclass, raises "TypeError".

The newly returned object is created by calling the "__init__()"
method of the dataclass.  This ensures that "__post_init__()", if
present, is also called.

Init-only variables without default values, if any exist, must be
specified on the call to "replace()" so that they can be passed to
"__init__()" and "__post_init__()".
```
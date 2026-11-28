# EN_PY_089: Enumerations HOWTO: Enum, IntEnum, Flag, and Bitmask Operations

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Data Types | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

Enum HOWTO
**********

An "Enum" is a set of symbolic names bound to unique values.  They are
similar to global variables, but they offer a more useful "repr()",
grouping, type-safety, and a few other features.

They are most useful when you have a variable that can take one of a
limited selection of values.  For example, the days of the week:

```python
>>> from enum import Enum
>>> class Weekday(Enum):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 3
...     THURSDAY = 4
...     FRIDAY = 5
...     SATURDAY = 6
...     SUNDAY = 7

```

Or perhaps the RGB primary colors:

```python
>>> from enum import Enum
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3

```

As you can see, creating an "Enum" is as simple as writing a class
that inherits from "Enum" itself.

Note:

  Case of Enum MembersBecause Enums are used to represent constants,
  and to help avoid issues with name clashes between mixin-class
  methods/attributes and enum names, we strongly recommend using
  UPPER_CASE names for members, and will be using that style in our
  examples.

Depending on the nature of the enum a member’s value may or may not be
important, but either way that value can be used to get the
corresponding member:

```python
>>> Weekday(3)
<Weekday.WEDNESDAY: 3>

```

As you can see, the "repr()" of a member shows the enum name, the
member name, and the value.  The "str()" of a member shows only the
enum name and member name:

```python
>>> print(Weekday.THURSDAY)
Weekday.THURSDAY

```

The *type* of an enumeration member is the enum it belongs to:

```python
>>> type(Weekday.MONDAY)
<enum 'Weekday'>
>>> isinstance(Weekday.FRIDAY, Weekday)
True

```

Enum members have an attribute that contains just their "name":

```python
>>> print(Weekday.TUESDAY.name)
TUESDAY

```

Likewise, they have an attribute for their "value":

```python
>>> Weekday.WEDNESDAY.value
3

```

Unlike many languages that treat enumerations solely as name/value
pairs, Python Enums can have behavior added.  For example,
"datetime.date" has two methods for returning the weekday: "weekday()"
and "isoweekday()". The difference is that one of them counts from 0-6
and the other from 1-7. Rather than keep track of that ourselves we
can add a method to the "Weekday" enum to extract the day from the
"date" instance and return the matching enum member:

   @classmethod

```python
def from_date(cls, date):
    return cls(date.isoweekday())

```

The complete "Weekday" enum now looks like this:

```python
>>> class Weekday(Enum):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 3
...     THURSDAY = 4
...     FRIDAY = 5
...     SATURDAY = 6
...     SUNDAY = 7
...     #
...     @classmethod
...     def from_date(cls, date):
...         return cls(date.isoweekday())

```

Now we can find out what today is!  Observe:

```python
>>> from datetime import date
>>> Weekday.from_date(date.today())
<Weekday.TUESDAY: 2>

```

Of course, if you’re reading this on some other day, you’ll see that

day instead.

This "Weekday" enum is great if our variable only needs one day, but
what if we need several?  Maybe we’re writing a function to plot
chores during a week, and don’t want to use a "list" – we could use a
different type of "Enum":

```python
>>> from enum import Flag
>>> class Weekday(Flag):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 4
...     THURSDAY = 8
...     FRIDAY = 16
...     SATURDAY = 32
...     SUNDAY = 64

```

We’ve changed two things: we’re inherited from "Flag", and the values
are all powers of 2.

Just like the original "Weekday" enum above, we can have a single
selection:

```python
>>> first_week_day = Weekday.MONDAY
>>> first_week_day
<Weekday.MONDAY: 1>

```

But "Flag" also allows us to combine several members into a single
variable:

```python
>>> weekend = Weekday.SATURDAY | Weekday.SUNDAY
>>> weekend
<Weekday.SATURDAY|SUNDAY: 96>

```

You can even iterate over a "Flag" variable:

```python
>>> for day in weekend:
...     print(day)
Weekday.SATURDAY
Weekday.SUNDAY

```

Okay, let’s get some chores set up:

```python
>>> chores_for_ethan = {
...     'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
...     'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
...     'answer SO questions': Weekday.SATURDAY,
...     }

```

And a function to display the chores for a given day:

```python
>>> def show_chores(chores, day):
...     for chore, days in chores.items():
...         if day in days:
...             print(chore)
>>> show_chores(chores_for_ethan, Weekday.SATURDAY)
answer SO questions

```

In cases where the actual values of the members do not matter, you can
save yourself some work and use "auto()" for the values:

```python
>>> from enum import auto
>>> class Weekday(Flag):
...     MONDAY = auto()
...     TUESDAY = auto()
...     WEDNESDAY = auto()
...     THURSDAY = auto()
...     FRIDAY = auto()
...     SATURDAY = auto()
...     SUNDAY = auto()
...     WEEKEND = SATURDAY | SUNDAY

```

Programmatic access to enumeration members and their attributes
===============================================================

Sometimes it’s useful to access members in enumerations
programmatically (i.e. situations where "Color.RED" won’t do because
the exact color is not known at program-writing time).  "Enum" allows

such access:

```python
>>> Color(1)
<Color.RED: 1>
>>> Color(3)
<Color.BLUE: 3>

    If you want to access enum members by *name*, use item access:

>>> Color['RED']
<Color.RED: 1>
>>> Color['GREEN']
<Color.GREEN: 2>

    If you have an enum member and need its "name" or "value":

>>> member = Color.RED
>>> member.name
'RED'
>>> member.value
1

```

Duplicating enum members and values
===================================

Having two enum members with the same name is invalid:

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     SQUARE = 3
Traceback (most recent call last):
TypeError: 'SQUARE' already defined as 2

```

However, an enum member can have other names associated with it.

Given two entries "A" and "B" with the same value (and "A" defined
first), "B" is an alias for the member "A".  By-value lookup of the
value of "A" will return the member "A".  By-name lookup of "A" will
return the member "A". By-name lookup of "B" will also return the
member "A":

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     DIAMOND = 1
...     CIRCLE = 3
...     ALIAS_FOR_SQUARE = 2
>>> Shape.SQUARE
<Shape.SQUARE: 2>
>>> Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
>>> Shape(2)
<Shape.SQUARE: 2>

```

Note:

  Attempting to create a member with the same name as an already
  defined attribute (another member, a method, etc.) or attempting to
  create an attribute with the same name as a member is not allowed.

Ensuring unique enumeration values
==================================

By default, enumerations allow multiple names as aliases for the same
value. When this behavior isn’t desired, you can use the "unique()"
decorator:

```python
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...     FOUR = 3
Traceback (most recent call last):
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE

```

Using automatic values
======================

If the exact value is unimportant you can use "auto":

```python
>>> from enum import Enum, auto
>>> class Color(Enum):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
>>> [member.value for member in Color]
[1, 2, 3]

```

The values are chosen by "_generate_next_value_()", which can be
overridden:

```python
>>> class AutoName(Enum):
...     @staticmethod
...     def _generate_next_value_(name, start, count, last_values):
...         return name
>>> class Ordinal(AutoName):
...     NORTH = auto()
...     SOUTH = auto()
...     EAST = auto()
...     WEST = auto()
>>> [member.value for member in Ordinal]
['NORTH', 'SOUTH', 'EAST', 'WEST']

```

Note:

  The "_generate_next_value_()" method must be defined before any
  members.

Iteration
=========

Iterating over the members of an enum does not provide the aliases:

```python
>>> list(Shape)
[<Shape.SQUARE: 2>, <Shape.DIAMOND: 1>, <Shape.CIRCLE: 3>]
>>> list(Weekday)
[<Weekday.MONDAY: 1>, <Weekday.TUESDAY: 2>, <Weekday.WEDNESDAY: 4>, <Weekday.THURSDAY: 8>, <Weekday.FRIDAY: 16>, <Weekday.SATURDAY: 32>, <Weekday.SUNDAY: 64>]

```

Note that the aliases "Shape.ALIAS_FOR_SQUARE" and "Weekday.WEEKEND"
aren’t shown.

The special attribute "__members__" is a read-only ordered mapping of
names to members.  It includes all names defined in the enumeration,
including the aliases:

```python
>>> for name, member in Shape.__members__.items():
...     name, member
('SQUARE', <Shape.SQUARE: 2>)
('DIAMOND', <Shape.DIAMOND: 1>)
('CIRCLE', <Shape.CIRCLE: 3>)
('ALIAS_FOR_SQUARE', <Shape.SQUARE: 2>)

```

The "__members__" attribute can be used for detailed programmatic
access to the enumeration members.  For example, finding all the
aliases:

```python
>>> [name for name, member in Shape.__members__.items() if member.name != name]
['ALIAS_FOR_SQUARE']

```

Note:

  Aliases for flags include values with multiple flags set, such as
  "3", and no flags set, i.e. "0".

Comparisons
===========

Enumeration members are compared by identity:

```python
>>> Color.RED is Color.RED
True
>>> Color.RED is Color.BLUE
False
>>> Color.RED is not Color.BLUE
True

```

Ordered comparisons between enumeration values are *not* supported.
Enum members are not integers (but see IntEnum below):

```python
>>> Color.RED < Color.BLUE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Color' and 'Color'

```

Equality comparisons are defined though:

```python
>>> Color.BLUE == Color.RED
False
>>> Color.BLUE != Color.RED
True
>>> Color.BLUE == Color.BLUE
True

```

Comparisons against non-enumeration values will always compare not
equal (again, "IntEnum" was explicitly designed to behave differently,
see below):

```python
>>> Color.BLUE == 2
False

```

Warning:

  It is possible to reload modules – if a reloaded module contains
  enums, they will be recreated, and the new members may not compare
  identical/equal to the original members.

Allowed members and attributes of enumerations
==============================================

Most of the examples above use integers for enumeration values.  Using
integers is short and handy (and provided by default by the Functional
API), but not strictly enforced.  In the vast majority of use-cases,
one doesn’t care what the actual value of an enumeration is.  But if
the value *is* important, enumerations can have arbitrary values.

Enumerations are Python classes, and can have methods and special
methods as usual.  If we have this enumeration:

```python
>>> class Mood(Enum):
...     FUNKY = 1
...     HAPPY = 3
...     def describe(self):
...         # self is the member here
...         return self.name, self.value
...     def __str__(self):
...         return 'my custom str! {0}'.format(self.value)
...     @classmethod
...     def favorite_mood(cls):
...         # cls here is the enumeration
...         return cls.HAPPY
```

Then:

```python
>>> Mood.favorite_mood()
<Mood.HAPPY: 3>
>>> Mood.HAPPY.describe()
('HAPPY', 3)
>>> str(Mood.FUNKY)
'my custom str! 1'

```

The rules for what is allowed are as follows: names that start and end
with a single underscore are reserved by enum and cannot be used; all

other attributes defined within an enumeration will become members of
this enumeration, with the exception of special methods ("__str__()",
"__add__()", etc.), descriptors (methods are also descriptors), and
variable names listed in "_ignore_".

Note:  if your enumeration defines "__new__()" and/or "__init__()",
any value(s) given to the enum member will be passed into those
methods. See Planet for an example.

Note:

  The "__new__()" method, if defined, is used during creation of the
  Enum members; it is then replaced by Enum’s "__new__()" which is
  used after class creation for lookup of existing members.  See When
  to use __new__() vs. __init__() for more details.

Restricted Enum subclassing
===========================

A new "Enum" class must have one base enum class, up to one concrete
data type, and as many "object"-based mixin classes as needed.  The
order of these base classes is:

```python
class EnumName([mix-in, ...,] [data-type,] base-enum):
    pass

```

Also, subclassing an enumeration is allowed only if the enumeration
does not define any members.  So this is forbidden:

```python
>>> class MoreColor(Color):
...     PINK = 17
Traceback (most recent call last):
TypeError: <enum 'MoreColor'> cannot extend <enum 'Color'>

```

But this is allowed:

```python
>>> class Foo(Enum):
...     def some_behavior(self):
...         pass
>>> class Bar(Foo):
...     HAPPY = 1
...     SAD = 2
```

Allowing subclassing of enums that define members would lead to a
violation of some important invariants of types and instances.  On the
other hand, it makes sense to allow sharing some common behavior
between a group of enumerations. (See OrderedEnum for an example.)

Dataclass support
=================

When inheriting from a "dataclass", the "__repr__()" omits the
inherited class’ name.  For example:

```python
>>> from dataclasses import dataclass, field
>>> @dataclass
... class CreatureDataMixin:
...     size: str
...     legs: int
...     tail: bool = field(repr=False, default=True)
>>> class Creature(CreatureDataMixin, Enum):
...     BEETLE = 'small', 6
...     DOG = 'medium', 4
>>> Creature.DOG
<Creature.DOG: size='medium', legs=4>

```

Use the "dataclass()" argument "repr=False" to use the standard
# EN_PY_038: A First Look at Classes: Class Definitions, Class Objects, and Instances

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

9.3. A First Look at Classes
============================

Classes introduce a little bit of new syntax, three new object types,
and some new semantics.

9.3.1. Class Definition Syntax
------------------------------

The simplest form of class definition looks like this:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

```

Class definitions, like function definitions ("def" statements) must
be executed before they have any effect.  (You could conceivably place
a class definition in a branch of an "if" statement, or inside a
function.)

In practice, the statements inside a class definition will usually be
function definitions, but other statements are allowed, and sometimes
useful — we’ll come back to this later.  The function definitions
inside a class normally have a peculiar form of argument list,
dictated by the calling conventions for methods — again, this is
explained later.

When a class definition is entered, a new namespace is created, and

used as the local scope — thus, all assignments to local variables go
into this new namespace.  In particular, function definitions bind the
name of the new function here.

When a class definition is left normally (via the end), a *class
object* is created.  This is basically a wrapper around the contents
of the namespace created by the class definition; we’ll learn more
about class objects in the next section.  The original local scope
(the one in effect just before the class definition was entered) is
reinstated, and the class object is bound here to the class name given
in the class definition header ("ClassName" in the example).

9.3.2. Class Objects
--------------------

Class objects support two kinds of operations: attribute references
and instantiation.

*Attribute references* use the standard syntax used for all attribute
references in Python: "obj.name".  Valid attribute names are all the
names that were in the class’s namespace when the class object was
created.  So, if the class definition looked like this:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

```

then "MyClass.i" and "MyClass.f" are valid attribute references,
returning an integer and a function object, respectively. Class
attributes can also be assigned to, so you can change the value of
"MyClass.i" by assignment. "__doc__" is also a valid attribute,
returning the docstring belonging to the class: ""A simple example
class"".

Class *instantiation* uses function notation.  Just pretend that the
class object is a parameterless function that returns a new instance
of the class. For example (assuming the above class):

   x = MyClass()

creates a new *instance* of the class and assigns this object to the
local variable "x".

The instantiation operation (“calling” a class object) creates an
empty object. Many classes like to create objects with instances
customized to a specific initial state. Therefore a class may define a
special method named "__init__()", like this:

```python
def __init__(self):
    self.data = []

```

When a class defines an "__init__()" method, class instantiation
automatically invokes "__init__()" for the newly created class
instance.  So in this example, a new, initialized instance can be
obtained by:

   x = MyClass()

Of course, the "__init__()" method may have arguments for greater
flexibility.  In that case, arguments given to the class instantiation
operator are passed on to "__init__()".  For example,

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

```

9.3.3. Instance Objects
-----------------------

Now what can we do with instance objects?  The only operations
understood by instance objects are attribute references.  There are
two kinds of valid attribute names: data attributes and methods.

*data attributes* correspond to “instance variables” in Smalltalk, and

to “data members” in C++.  Data attributes need not be declared; like
local variables, they spring into existence when they are first
assigned to.  For example, if "x" is the instance of "MyClass" created
above, the following piece of code will print the value "16", without
leaving a trace:

   x.counter = 1

```python
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

```

The other kind of instance attribute reference is a *method*. A method
is a function that “belongs to” an object.

Valid method names of an instance object depend on its class.  By
definition, all attributes of a class that are function  objects
define corresponding methods of its instances.  So in our example,
"x.f" is a valid method reference, since "MyClass.f" is a function,
but "x.i" is not, since "MyClass.i" is not.  But "x.f" is not the same
thing as "MyClass.f" — it is a *method object*, not a function object.
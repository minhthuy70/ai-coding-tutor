<!-- page: 1 -->
# EN_PY_039: Method Objects, the self Parameter, and Data Attributes

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

9.3.4. Method Objects
---------------------

Usually, a method is called right after it is bound:

   x.f()

In the "MyClass" example, this will return the string "'hello world'".
However, it is not necessary to call a method right away: "x.f" is a
method object, and can be stored away and called at a later time.  For
example:

   xf = x.f
```python
while True:
    print(xf())

```
will continue to print "hello world" until the end of time.

What exactly happens when a method is called?  You may have noticed
that "x.f()" was called without an argument above, even though the
function definition for "f()" specified an argument.  What happened to
the argument? Surely Python raises an exception when a function that
requires an argument is called without any — even if the argument
isn’t actually used…

Actually, you may have guessed the answer: the special thing about
methods is that the instance object is passed as the first argument of
the function.  In our example, the call "x.f()" is exactly equivalent
to "MyClass.f(x)".  In general, calling a method with a list of *n*
arguments is equivalent to calling the corresponding function with an
argument list that is created by inserting the method’s instance
object before the first argument.

<!-- page: 2 -->


In general, methods work as follows.  When a non-data attribute of an
instance is referenced, the instance’s class is searched. If the name
denotes a valid class attribute that is a function object, references
to both the instance object and the function object are packed into a
method object.  When the method object is called with an argument
list, a new argument list is constructed from the instance object and
the argument list, and the function object is called with this new
argument list.


9.3.5. Class and Instance Variables
-----------------------------------

Generally speaking, instance variables are for data unique to each
instance and class variables are for attributes and methods shared by
all instances of the class:

```python
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

```
As discussed in A Word About Names and Objects, shared data can have
possibly surprising effects with involving *mutable* objects such as
lists and dictionaries. For example, the *tricks* list in the
following code should not be used as a class variable because just a
single list would be shared by all *Dog* instances:

```python
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

```

<!-- page: 3 -->

Correct design of the class should use an instance variable instead:

```python
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

```
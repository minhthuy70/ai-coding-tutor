# EN_PY_076: Functional Programming HOWTO: Iterators, Generator Functions, and itertools

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Functional Programming | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

Functional Programming HOWTO
****************************

Author:
   A. M. Kuchling

Release:
   0.32

In this document, we’ll take a tour of Python’s features suitable for
implementing programs in a functional style.  After an introduction to
the concepts of functional programming, we’ll look at language
features such as *iterator*s and *generator*s and relevant library
modules such as "itertools" and "functools".

Introduction
============

This section explains the basic concept of functional programming; if
you’re just interested in learning about Python language features,
skip to the next section on Iterators.

Programming languages support decomposing problems in several
different ways:

* Most programming languages are **procedural**: programs are lists of
  instructions that tell the computer what to do with the program’s
  input.  C, Pascal, and even Unix shells are procedural languages.

* In **declarative** languages, you write a specification that
  describes the problem to be solved, and the language implementation
  figures out how to perform the computation efficiently.  SQL is the
  declarative language you’re most likely to be familiar with; a SQL

  query describes the data set you want to retrieve, and the SQL
  engine decides whether to scan tables or use indexes, which
  subclauses should be performed first, etc.

* **Object-oriented** programs manipulate collections of objects.
  Objects have internal state and support methods that query or modify
  this internal state in some way. Smalltalk and Java are object-
  oriented languages.  C++ and Python are languages that support
  object-oriented programming, but don’t force the use of object-
  oriented features.

* **Functional** programming decomposes a problem into a set of
  functions. Ideally, functions only take inputs and produce outputs,
  and don’t have any internal state that affects the output produced
  for a given input.  Well-known functional languages include the ML
  family (Standard ML, OCaml, and other variants) and Haskell.

The designers of some computer languages choose to emphasize one
particular approach to programming.  This often makes it difficult to
write programs that use a different approach.  Other languages are
multi-paradigm languages that support several different approaches.
Lisp, C++, and Python are multi-paradigm; you can write programs or
libraries that are largely procedural, object-oriented, or functional
in all of these languages.  In a large program, different sections
might be written using different approaches; the GUI might be object-
oriented while the processing logic is procedural or functional, for
example.

In a functional program, input flows through a set of functions. Each
function operates on its input and produces some output.  Functional
style discourages functions with side effects that modify internal
state or make other changes that aren’t visible in the function’s
return value.  Functions that have no side effects at all are called
**purely functional**.  Avoiding side effects means not using data
structures that get updated as a program runs; every function’s output
must only depend on its input.

Some languages are very strict about purity and don’t even have
assignment statements such as "a=3" or "c = a + b", but it’s difficult
to avoid all side effects, such as printing to the screen or writing
to a disk file. Another example is a call to the "print()" or
"time.sleep()" function, neither of which returns a useful value. Both
are called only for their side effects of sending some text to the
screen or pausing execution for a second.

Python programs written in functional style usually won’t go to the
extreme of avoiding all I/O or all assignments; instead, they’ll
provide a functional-appearing interface but will use non-functional
features internally. For example, the implementation of a function
will still use assignments to local variables, but won’t modify global
variables or have other side effects.

Functional programming can be considered the opposite of object-
oriented programming.  Objects are little capsules containing some
internal state along with a collection of method calls that let you
modify this state, and programs consist of making the right set of
state changes.  Functional programming wants to avoid state changes as
much as possible and works with data flowing between functions.  In
Python you might combine the two approaches by writing functions that
take and return instances representing objects in your application
(e-mail messages, transactions, etc.).

Functional design may seem like an odd constraint to work under.  Why
should you avoid objects and side effects?  There are theoretical and
practical advantages to the functional style:

* Formal provability.

* Modularity.

* Composability.

* Ease of debugging and testing.

Formal provability
------------------

A theoretical benefit is that it’s easier to construct a mathematical
proof that a functional program is correct.

For a long time researchers have been interested in finding ways to
mathematically prove programs correct.  This is different from testing
a program on numerous inputs and concluding that its output is usually
correct, or reading a program’s source code and concluding that the
code looks right; the goal is instead a rigorous proof that a program
produces the right result for all possible inputs.

The technique used to prove programs correct is to write down
**invariants**, properties of the input data and of the program’s

variables that are always true.  For each line of code, you then show
that if invariants X and Y are true **before** the line is executed,
the slightly different invariants X’ and Y’ are true **after** the
line is executed.  This continues until you reach the end of the
program, at which point the invariants should match the desired
conditions on the program’s output.

Functional programming’s avoidance of assignments arose because
assignments are difficult to handle with this technique; assignments
can break invariants that were true before the assignment without
producing any new invariants that can be propagated onward.

Unfortunately, proving programs correct is largely impractical and not
relevant to Python software. Even trivial programs require proofs that
are several pages long; the proof of correctness for a moderately
complicated program would be enormous, and few or none of the programs
you use daily (the Python interpreter, your XML parser, your web
browser) could be proven correct.  Even if you wrote down or generated
a proof, there would then be the question of verifying the proof;
maybe there’s an error in it, and you wrongly believe you’ve proved
the program correct.

Modularity
----------

A more practical benefit of functional programming is that it forces
you to break apart your problem into small pieces.  Programs are more
modular as a result.  It’s easier to specify and write a small
function that does one thing than a large function that performs a
complicated transformation.  Small functions are also easier to read
and to check for errors.

Ease of debugging and testing
-----------------------------

Testing and debugging a functional-style program is easier.

Debugging is simplified because functions are generally small and
clearly specified.  When a program doesn’t work, each function is an
interface point where you can check that the data are correct.  You
can look at the intermediate inputs and outputs to quickly isolate the
function that’s responsible for a bug.

Testing is easier because each function is a potential subject for a
unit test. Functions don’t depend on system state that needs to be
replicated before running a test; instead you only have to synthesize
the right input and then check that the output matches expectations.

Composability
-------------

As you work on a functional-style program, you’ll write a number of
functions with varying inputs and outputs.  Some of these functions
will be unavoidably specialized to a particular application, but
others will be useful in a wide variety of programs.  For example, a
function that takes a directory path and returns all the XML files in
the directory, or a function that takes a filename and returns its
contents, can be applied to many different situations.

Over time you’ll form a personal library of utilities.  Often you’ll
assemble new programs by arranging existing functions in a new
configuration and writing a few functions specialized for the current
task.

Iterators
=========

I’ll start by looking at a Python language feature that’s an important
foundation for writing functional-style programs: iterators.

An iterator is an object representing a stream of data; this object
returns the data one element at a time.  A Python iterator must
support a method called "__next__()" that takes no arguments and
always returns the next element of the stream.  If there are no more
elements in the stream, "__next__()" must raise the "StopIteration"
exception. Iterators don’t have to be finite, though; it’s perfectly
reasonable to write an iterator that produces an infinite stream of
data.

The built-in "iter()" function takes an arbitrary object and tries to
return an iterator that will return the object’s contents or elements,
raising "TypeError" if the object doesn’t support iteration.  Several
of Python’s built-in data types support iteration, the most common
being lists and dictionaries.  An object is called *iterable* if you
can get an iterator for it.

You can experiment with the iteration interface manually:

>>> L = [1, 2, 3]
>>> it = iter(L)
>>> it
<...iterator object at ...>
>>> it.__next__()  # same as next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

Python expects iterable objects in several different contexts, the
most important being the "for" statement.  In the statement "for X in
Y", Y must be an iterator or some object for which "iter()" can create
an iterator.  These two statements are equivalent:

```python
for i in iter(obj):
    print(i)

for i in obj:
    print(i)

```

Iterators can be materialized as lists or tuples by using the "list()"
or "tuple()" constructor functions:

>>> L = [1, 2, 3]
>>> iterator = iter(L)
>>> t = tuple(iterator)
>>> t
(1, 2, 3)

Sequence unpacking also supports iterators: if you know an iterator
will return N elements, you can unpack them into an N-tuple:

>>> L = [1, 2, 3]
>>> iterator = iter(L)

>>> a, b, c = iterator
>>> a, b, c
(1, 2, 3)

Built-in functions such as "max()" and "min()" can take a single
iterator argument and will return the largest or smallest element.
The ""in"" and ""not in"" operators also support iterators: "X in
iterator" is true if X is found in the stream returned by the
iterator.  You’ll run into obvious problems if the iterator is
infinite; "max()", "min()" will never return, and if the element X
never appears in the stream, the ""in"" and ""not in"" operators won’t
return either.

Note that you can only go forward in an iterator; there’s no way to
get the previous element, reset the iterator, or make a copy of it.
Iterator objects can optionally provide these additional capabilities,
but the iterator protocol only specifies the "__next__()" method.
Functions may therefore consume all of the iterator’s output, and if
you need to do something different with the same stream, you’ll have
to create a new iterator.

Data Types That Support Iterators
---------------------------------

We’ve already seen how lists and tuples support iterators.  In fact,
any Python sequence type, such as strings, will automatically support
creation of an iterator.

Calling "iter()" on a dictionary returns an iterator that will loop
over the dictionary’s keys:

```python
>>> m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
...      'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
>>> for key in m:
...     print(key, m[key])
Jan 1
Feb 2
Mar 3
Apr 4
May 5
Jun 6
Jul 7
Aug 8
Sep 9
Oct 10
Nov 11
Dec 12

```

Note that starting with Python 3.7, dictionary iteration order is
guaranteed to be the same as the insertion order. In earlier versions,
the behaviour was unspecified and could vary between implementations.

Applying "iter()" to a dictionary always loops over the keys, but
dictionaries have methods that return other iterators.  If you want to
iterate over values or key/value pairs, you can explicitly call the
"values()" or "items()" methods to get an appropriate iterator.

The "dict()" constructor can accept an iterator that returns a finite
stream of "(key, value)" tuples:

>>> L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
>>> dict(iter(L))
{'Italy': 'Rome', 'France': 'Paris', 'US': 'Washington DC'}

Files also support iteration by calling the "readline()" method until
there are no more lines in the file.  This means you can read each
line of a file like this:

```python
for line in file:
    # do something for each line
    ...

```

Sets can take their contents from an iterable and let you iterate over
the set’s elements:

```python
>>> S = {2, 3, 5, 7, 11, 13}
>>> for i in S:
...     print(i)
2
3
5
7
11
13

```

Generator expressions and list comprehensions
=============================================

Two common operations on an iterator’s output are 1) performing some
operation for every element, 2) selecting a subset of elements that
meet some condition. For example, given a list of strings, you might
# EN_PY_077: Functional Programming HOWTO: functools, partial, reduce, and operator

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Functional Programming | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

want to strip off trailing whitespace from each line or extract all
the strings containing a given substring.

List comprehensions and generator expressions (short form: “listcomps”
and “genexps”) are a concise notation for such operations, borrowed
from the functional programming language Haskell
(https://www.haskell.org/).  You can strip all the whitespace from a
stream of strings with the following code:

```python
>>> line_list = ['  line 1\n', 'line 2  \n', ' \n', '']

>>> # Generator expression -- returns iterator
>>> stripped_iter = (line.strip() for line in line_list)

>>> # List comprehension -- returns list
>>> stripped_list = [line.strip() for line in line_list]

```

You can select only certain elements by adding an ""if"" condition:

```python
>>> stripped_list = [line.strip() for line in line_list
...                  if line != ""]

```

With a list comprehension, you get back a Python list; "stripped_list"
is a list containing the resulting lines, not an iterator.  Generator
expressions return an iterator that computes the values as necessary,
not needing to materialize all the values at once.  This means that
list comprehensions aren’t useful if you’re working with iterators
that return an infinite stream or a very large amount of data.
Generator expressions are preferable in these situations.

Generator expressions are surrounded by parentheses (“()”) and list
comprehensions are surrounded by square brackets (“[]”).  Generator
expressions have the form:

```python
( expression for expr in sequence1
             if condition1
             for expr2 in sequence2
             if condition2
             for expr3 in sequence3
             if condition3
             for exprN in sequenceN
             if conditionN )

```

Again, for a list comprehension only the outside brackets are
different (square brackets instead of parentheses).

The elements of the generated output will be the successive values of
"expression".  The "if" clauses are all optional; if present,
"expression" is only evaluated and added to the result when
"condition" is true.

Generator expressions always have to be written inside parentheses,
but the parentheses signalling a function call also count.  If you
want to create an iterator that will be immediately passed to a
function you can write:

```python
obj_total = sum(obj.count for obj in list_all_objects())

```

The "for...in" clauses contain the sequences to be iterated over.  The
sequences do not have to be the same length, because they are iterated
over from left to right, **not** in parallel.  For each element in
"sequence1", "sequence2" is looped over from the beginning.
"sequence3" is then looped over for each resulting pair of elements
from "sequence1" and "sequence2".

To put it another way, a list comprehension or generator expression is
equivalent to the following Python code:

```python
for expr1 in sequence1:
    if not (condition1):
        continue   # Skip this element
    for expr2 in sequence2:
        if not (condition2):
            continue   # Skip this element
        for exprN in sequenceN:
            if not (conditionN):
                continue   # Skip this element

            # Output the value of
            # the expression.

```

This means that when there are multiple "for...in" clauses but no "if"
clauses, the length of the resulting output will be equal to the
product of the lengths of all the sequences.  If you have two lists of
length 3, the output list is 9 elements long:

```python
>>> seq1 = 'abc'
>>> seq2 = (1, 2, 3)
>>> [(x, y) for x in seq1 for y in seq2]
[('a', 1), ('a', 2), ('a', 3),
 ('b', 1), ('b', 2), ('b', 3),
 ('c', 1), ('c', 2), ('c', 3)]
```

To avoid introducing an ambiguity into Python’s grammar, if
"expression" is creating a tuple, it must be surrounded with
parentheses.  The first list comprehension below is a syntax error,
while the second one is correct:

   # Syntax error

```python
[x, y for x in seq1 for y in seq2]
# Correct
[(x, y) for x in seq1 for y in seq2]

```

Generators
==========

Generators are a special class of functions that simplify the task of
writing iterators.  Regular functions compute a value and return it,
but generators return an iterator that returns a stream of values.

You’re doubtless familiar with how regular function calls work in
Python or C. When you call a function, it gets a private namespace
where its local variables are created.  When the function reaches a
"return" statement, the local variables are destroyed and the value is
returned to the caller.  A later call to the same function creates a
new private namespace and a fresh set of local variables. But, what if
the local variables weren’t thrown away on exiting a function?  What
if you could later resume the function where it left off?  This is
what generators provide; they can be thought of as resumable
functions.

Here’s the simplest example of a generator function:

```python
>>> def generate_ints(N):
...    for i in range(N):
...        yield i
```

Any function containing a "yield" keyword is a generator function;
this is detected by Python’s *bytecode* compiler which compiles the
function specially as a result.

When you call a generator function, it doesn’t return a single value;
instead it returns a generator object that supports the iterator
protocol.  On executing the "yield" expression, the generator outputs
the value of "i", similar to a "return" statement.  The big difference
between "yield" and a "return" statement is that on reaching a "yield"
the generator’s state of execution is suspended and local variables
are preserved.  On the next call to the generator’s "__next__()"
method, the function will resume executing.

Here’s a sample usage of the "generate_ints()" generator:

```python
>>> gen = generate_ints(3)
>>> gen
<generator object generate_ints at ...>
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
Traceback (most recent call last):
  File "stdin", line 1, in <module>
  File "stdin", line 2, in generate_ints
StopIteration
```

You could equally write "for i in generate_ints(5)", or "a, b, c =
generate_ints(3)".

Inside a generator function, "return value" causes
"StopIteration(value)" to be raised from the "__next__()" method.
Once this happens, or the bottom of the function is reached, the
procession of values ends and the generator cannot yield any further
values.

You could achieve the effect of generators manually by writing your
own class and storing all the local variables of the generator as

instance variables.  For example, returning a list of integers could
be done by setting "self.count" to 0, and having the "__next__()"
method increment "self.count" and return it. However, for a moderately
complicated generator, writing a corresponding class can be much
messier.

The test suite included with Python’s library,
Lib/test/test_generators.py, contains a number of more interesting
examples.  Here’s one generator that implements an in-order traversal
of a tree using generators recursively.

   # A recursive generator that generates Tree leaves in in-order.

```python
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t.label

        for x in inorder(t.right):
            yield x

```

Two other examples in "test_generators.py" produce solutions for the
N-Queens problem (placing N queens on an NxN chess board so that no
queen threatens another) and the Knight’s Tour (finding a route that
takes a knight to every square of an NxN chessboard without visiting
any square twice).

Passing values into a generator
-------------------------------

In Python 2.4 and earlier, generators only produced output.  Once a
generator’s code was invoked to create an iterator, there was no way
to pass any new information into the function when its execution is
resumed.  You could hack together this ability by making the generator
look at a global variable or by passing in some mutable object that
callers then modify, but these approaches are messy.

In Python 2.5 there’s a simple way to pass values into a generator.
"yield" became an expression, returning a value that can be assigned
to a variable or otherwise operated on:

```python
val = (yield i)

```

I recommend that you **always** put parentheses around a "yield"
expression when you’re doing something with the returned value, as in
the above example. The parentheses aren’t always necessary, but it’s
easier to always add them instead of having to remember when they’re
needed.

(**PEP 342** explains the exact rules, which are that a
"yield"-expression must always be parenthesized except when it occurs
at the top-level expression on the right-hand side of an assignment.
This means you can write "val = yield i" but have to use parentheses
when there’s an operation, as in "val = (yield i) + 12".)

Values are sent into a generator by calling its "send(value)" method.
This method resumes the generator’s code and the "yield" expression
returns the specified value.  If the regular "__next__()" method is
called, the "yield" returns "None".

Here’s a simple counter that increments by 1 and allows changing the
value of the internal counter.

```python
def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

```

And here’s an example of changing the counter:

```python
>>> it = counter(10)
>>> next(it)
0
>>> next(it)
1
>>> it.send(8)
8
```

```python
>>> next(it)
9
>>> next(it)
Traceback (most recent call last):
  File "t.py", line 15, in <module>
    it.next()
StopIteration
```

Because "yield" will often be returning "None", you should always
check for this case.  Don’t just use its value in expressions unless
you’re sure that the "send()" method will be the only method used to
resume your generator function.

In addition to "send()", there are two other methods on generators:

* "throw(value)" is used to raise an exception inside the generator;
  the exception is raised by the "yield" expression where the
  generator’s execution is paused.

* "close()" raises a "GeneratorExit" exception inside the generator to
  terminate the iteration.  On receiving this exception, the
  generator’s code must either raise "GeneratorExit" or
  "StopIteration"; catching the exception and doing anything else is
  illegal and will trigger a "RuntimeError".  "close()" will also be
  called by Python’s garbage collector when the generator is garbage-
  collected.

  If you need to run cleanup code when a "GeneratorExit" occurs, I
  suggest using a "try: ... finally:" suite instead of catching
  "GeneratorExit".

The cumulative effect of these changes is to turn generators from one-
way producers of information into both producers and consumers.

Generators also become **coroutines**, a more generalized form of
subroutines. Subroutines are entered at one point and exited at
another point (the top of the function, and a "return" statement), but
coroutines can be entered, exited, and resumed at many different
points (the "yield" statements).

Built-in functions
==================

Let’s look in more detail at built-in functions often used with

iterators.

Two of Python’s built-in functions, "map()" and "filter()" duplicate
the features of generator expressions:

"map(f, iterA, iterB, ...)" returns an iterator over the sequence
   "f(iterA[0], iterB[0]), f(iterA[1], iterB[1]), f(iterA[2],
   iterB[2]), ...".

```python
>>> def upper(s):
...     return s.upper()

>>> list(map(upper, ['sentence', 'fragment']))
['SENTENCE', 'FRAGMENT']
>>> [upper(s) for s in ['sentence', 'fragment']]
['SENTENCE', 'FRAGMENT']

```

You can of course achieve the same effect with a list comprehension.

"filter(predicate, iter)" returns an iterator over all the sequence
elements that meet a certain condition, and is similarly duplicated by
list comprehensions.  A **predicate** is a function that returns the
truth value of some condition; for use with "filter()", the predicate
must take a single value.

```python
>>> def is_even(x):
...     return (x % 2) == 0
```

```python
>>> list(filter(is_even, range(10)))
[0, 2, 4, 6, 8]
```

This can also be written as a list comprehension:

```python
>>> list(x for x in range(10) if is_even(x))
[0, 2, 4, 6, 8]
```

"enumerate(iter, start=0)" counts off the elements in the iterable
returning 2-tuples containing the count (from *start*) and each
element.

```python
>>> for item in enumerate(['subject', 'verb', 'object']):
...     print(item)
(0, 'subject')
(1, 'verb')
(2, 'object')

```

"enumerate()" is often used when looping through a list and recording
the indexes at which certain conditions are met:

   f = open('data.txt', 'r')

```python
for i, line in enumerate(f):
    if line.strip() == '':
        print('Blank line at line #%i' % i)

```

"sorted(iterable, key=None, reverse=False)" collects all the elements
of the iterable into a list, sorts the list, and returns the sorted
result.  The *key* and *reverse* arguments are passed through to the
constructed list’s "sort()" method.

```python
>>> import random
>>> # Generate 8 random numbers between [0, 10000)
>>> rand_list = random.sample(range(10000), 8)
>>> rand_list
[769, 7953, 9828, 6431, 8442, 9878, 6213, 2207]
>>> sorted(rand_list)
[769, 2207, 6213, 6431, 7953, 8442, 9828, 9878]
>>> sorted(rand_list, reverse=True)
[9878, 9828, 8442, 7953, 6431, 6213, 2207, 769]

```

(For a more detailed discussion of sorting, see the Sorting
Techniques.)

The "any(iter)" and "all(iter)" built-ins look at the truth values of
an iterable’s contents.  "any()" returns "True" if any element in the
iterable is a true value, and "all()" returns "True" if all of the
elements are true values:

```python
>>> any([0, 1, 0])
True
>>> any([0, 0, 0])
False
>>> any([1, 1, 1])
True
>>> all([0, 1, 0])
False
>>> all([0, 0, 0])
False
```

```python
>>> all([1, 1, 1])
True
```

"zip(iterA, iterB, ...)" takes one element from each iterable and
returns them in a tuple:

   zip(['a', 'b', 'c'], (1, 2, 3)) =>
     ('a', 1), ('b', 2), ('c', 3)

It doesn’t construct an in-memory list and exhaust all the input
iterators before returning; instead tuples are constructed and
returned only if they’re requested.  (The technical term for this
behaviour is lazy evaluation.)
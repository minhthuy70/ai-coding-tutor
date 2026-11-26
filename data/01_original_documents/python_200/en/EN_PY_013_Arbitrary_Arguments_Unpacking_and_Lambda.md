<!-- page: 1 -->
# EN_PY_013: Arbitrary Argument Lists (*args, **kwargs), Unpacking, and Lambda Expressions

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Functions | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

4.9.4. Arbitrary Argument Lists
-------------------------------

Finally, the least frequently used option is to specify that a
function can be called with an arbitrary number of arguments.  These
arguments will be wrapped up in a tuple (see Tuples and Sequences).
Before the variable number of arguments, zero or more normal arguments
may occur.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

```
Normally, these *variadic* arguments will be last in the list of
formal parameters, because they scoop up all remaining input arguments
that are passed to the function. Any formal parameters which occur
after the "*args" parameter are ‘keyword-only’ arguments, meaning that
they can only be used as keywords rather than positional arguments.

```python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'


```
4.9.5. Unpacking Argument Lists
-------------------------------


<!-- page: 2 -->

The reverse situation occurs when the arguments are already in a list
or tuple but need to be unpacked for a function call requiring
separate positional arguments.  For instance, the built-in "range()"
function expects separate *start* and *stop* arguments.  If they are
not available separately, write the function call with the
"*"-operator to unpack the arguments out of a list or tuple:

```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

```
In the same fashion, dictionaries can deliver keyword arguments with
the "**"-operator:

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !


```
4.9.6. Lambda Expressions
-------------------------

Small anonymous functions can be created with the "lambda" keyword.
This function returns the sum of its two arguments: "lambda a, b:
a+b". Lambda functions can be used wherever function objects are
required.  They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function
definition.  Like nested function definitions, lambda functions can
reference variables from the containing scope:

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43

```

<!-- page: 3 -->

The above example uses a lambda expression to return a function.
Another use is to pass a small function as an argument:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

```
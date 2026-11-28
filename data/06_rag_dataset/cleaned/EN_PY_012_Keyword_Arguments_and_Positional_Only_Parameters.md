# EN_PY_012: Keyword Arguments, Positional-Only (/) and Keyword-Only (*) Parameters

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Functions | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

4.9.2. Keyword Arguments
------------------------

Functions can also be called using *keyword arguments* of the form
"kwarg=value".  For instance, the following function:

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

```

accepts one required argument ("voltage") and three optional arguments
("state", "action", and "type").  This function can be called in any
of the following ways:

   parrot(1000)                                          # 1 positional argument
   parrot(voltage=1000)                                  # 1 keyword argument
   parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
   parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
   parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
   parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

but all the following calls would be invalid:

   parrot()                     # required argument missing
   parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument

```python
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

```

In a function call, keyword arguments must follow positional
arguments. All the keyword arguments passed must match one of the
arguments accepted by the function (e.g. "actor" is not a valid
argument for the "parrot" function), and their order is not important.
This also includes non-optional arguments (e.g. "parrot(voltage=1000)"
is valid too). No argument may receive a value more than once. Here’s
an example that fails due to this restriction:

```python
>>> def function(a):
...     pass
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'

```

When a final formal parameter of the form "**name" is present, it
receives a dictionary (see Mapping Types — dict) containing all
keyword arguments except for those corresponding to a formal
parameter.  This may be combined with a formal parameter of the form
"*name" (described in the next subsection) which receives a tuple
containing the positional arguments beyond the formal parameter list.
("*name" must occur before "**name".) For example, if we define a
function like this:

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

```

It could be called like this:

   cheeseshop("Limburger", "It's very runny, sir.",
              "It's really very, VERY runny, sir.",
              shopkeeper="Michael Palin",
              client="John Cleese",
              sketch="Cheese Shop Sketch")

and of course it would print:

   -- Do you have any Limburger ?
   -- I'm sorry, we're all out of Limburger
   It's very runny, sir.
   It's really very, VERY runny, sir.
   ----------------------------------------
   shopkeeper : Michael Palin
   client : John Cleese
   sketch : Cheese Shop Sketch

Note that the order in which the keyword arguments are printed is
guaranteed to match the order in which they were provided in the
function call.

4.9.3. Special parameters
-------------------------

By default, arguments may be passed to a Python function either by
position or explicitly by keyword. For readability and performance, it
makes sense to restrict the way arguments can be passed so that a
developer need only look at the function definition to determine if
items are passed by position, by position or keyword, or by keyword.

A function definition may look like:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only

```

where "/" and "*" are optional. If used, these symbols indicate the
kind of parameter by how the arguments may be passed to the function:
positional-only, positional-or-keyword, and keyword-only. Keyword
parameters are also referred to as named parameters.

4.9.3.1. Positional-or-Keyword Arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If "/" and "*" are not present in the function definition, arguments
may be passed to a function by position or by keyword.

4.9.3.2. Positional-Only Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Looking at this in a bit more detail, it is possible to mark certain
parameters as *positional-only*. If *positional-only*, the parameters’
order matters, and the parameters cannot be passed by keyword.
Positional-only parameters are placed before a "/" (forward-slash).
The "/" is used to logically separate the positional-only parameters
from the rest of the parameters. If there is no "/" in the function
definition, there are no positional-only parameters.

Parameters following the "/" may be *positional-or-keyword* or
*keyword-only*.

4.9.3.3. Keyword-Only Arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To mark parameters as *keyword-only*, indicating the parameters must
be passed by keyword argument, place an "*" in the arguments list just
before the first *keyword-only* parameter.

4.9.3.4. Function Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider the following example function definitions paying close
attention to the markers "/" and "*":

```python
>>> def standard_arg(arg):
...     print(arg)
>>> def pos_only_arg(arg, /):
...     print(arg)
>>> def kwd_only_arg(*, arg):
...     print(arg)
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)

```

The first function definition, "standard_arg", the most familiar form,
places no restrictions on the calling convention and arguments may be
passed by position or keyword:

```python
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2

```

The second function "pos_only_arg" is restricted to only use
positional parameters as there is a "/" in the function definition:

```python
>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

```

The third function "kwd_only_arg" only allows keyword arguments as
indicated by a "*" in the function definition:

```python
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3

```

And the last uses all three calling conventions in the same function
definition:

```python
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

```

Finally, consider this function definition which has a potential
collision between the positional argument "name"  and "**kwds" which
has "name" as a key:

```python
def foo(name, **kwds):
    return 'name' in kwds

```

There is no possible call that will make it return "True" as the
keyword "'name'" will always bind to the first parameter. For example:

```python
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>

```

But using "/" (positional only arguments), it is possible since it
allows "name" as a positional argument and "'name'" as a key in the
keyword arguments:

```python
>>> def foo(name, /, **kwds):
...     return 'name' in kwds
>>> foo(1, **{'name': 2})
True

```

In other words, the names of positional-only parameters can be used in
"**kwds" without ambiguity.

4.9.3.5. Recap
~~~~~~~~~~~~~~

The use case will determine which parameters to use in the function
definition:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

```

As guidance:

* Use positional-only if you want the name of the parameters to not be
  available to the user. This is useful when parameter names have no
  real meaning, if you want to enforce the order of the arguments when
  the function is called or if you need to take some positional
  parameters and arbitrary keywords.

* Use keyword-only when names have meaning and the function definition
  is more understandable by being explicit with names or you want to
  prevent users relying on the position of the argument being passed.

* For an API, use positional-only to prevent breaking API changes if
  the parameter’s name is modified in the future.
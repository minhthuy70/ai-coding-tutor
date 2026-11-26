# EN_PY_011: Default Argument Values and the Mutable Default Argument Trap

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Functions | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

4.9. More on Defining Functions
===============================

It is also possible to define functions with a variable number of
arguments. There are three forms, which can be combined.

4.9.1. Default Argument Values
------------------------------

The most useful form is to specify a default value for one or more
arguments. This creates a function that can be called with fewer
arguments than it is defined to allow.  For example:

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

```

This function can be called in several ways:

* giving only the mandatory argument: "ask_ok('Do you really want to
  quit?')"

* giving one of the optional arguments: "ask_ok('OK to overwrite the

  file?', 2)"

* or even giving all arguments: "ask_ok('OK to overwrite the file?',
  2, 'Come on, only yes or no!')"

This example also introduces the "in" keyword. This tests whether or
not a sequence contains a certain value.

The default values are evaluated at the point of function definition
in the *defining* scope, so that

   i = 5

```python
def f(arg=i):
    print(arg)

i = 6
f()

```

will print "5".

**Important warning:**  The default value is evaluated only once. This
makes a difference when the default is a mutable object such as a
list, dictionary, or instances of most classes.  For example, the
following function accumulates the arguments passed to it on
subsequent calls:

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

```

This will print

   [1, 2]
   [1, 2, 3]

If you don’t want the default to be shared between subsequent calls,
you can write the function like this instead:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

```
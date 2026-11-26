# EN_PY_032: Raising Exceptions and Exception Chaining (raise...from Statement)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Exceptions | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

8.4. Raising Exceptions
=======================

The "raise" statement allows the programmer to force a specified
exception to occur. For example:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere

```

The sole argument to "raise" indicates the exception to be raised.
This must be either an exception instance or an exception class (a
class that derives from "BaseException", such as "Exception" or one of
its subclasses).  If an exception class is passed, it will be
implicitly instantiated by calling its constructor with no arguments:

```python
raise ValueError  # shorthand for 'raise ValueError()'

```

If you need to determine whether an exception was raised but don’t
intend to handle it, a simpler form of the "raise" statement allows
you to re-raise the exception:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere

```

8.5. Exception Chaining
=======================

If an unhandled exception occurs inside an "except" section, it will
have the exception being handled attached to it and included in the
error message:

```python
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: unable to handle error

```

To indicate that an exception is a direct consequence of another, the
"raise" statement allows an optional "from" clause:

   # exc must be exception instance or None.

```python
raise RuntimeError from exc

```

This can be useful when you are transforming exceptions. For example:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database

```

It also allows disabling automatic exception chaining using the "from
None" idiom:

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError

```

For more information about chaining mechanics, see Built-in
Exceptions.
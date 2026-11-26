<!-- page: 1 -->
# EN_PY_030: Syntax Errors vs Runtime Exceptions in Python Interpretation

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Exceptions | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

8.1. Syntax Errors
==================

Syntax errors, also known as parsing errors, are perhaps the most
common kind of complaint you get while you are still learning Python:

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax

```
The parser repeats the offending line and displays little arrows
pointing at the token in the line where the error was detected.  The
error may be caused by the absence of a token *before* the indicated
token.  In the example, the error is detected at the function
"print()", since a colon ("':'") is missing before it.  File name and
line number are printed so you know where to look in case the input
came from a script.


8.2. Exceptions
===============

Even if a statement or expression is syntactically correct, it may
cause an error when an attempt is made to execute it. Errors detected
during execution are called *exceptions* and are not unconditionally
fatal: you will soon learn how to handle them in Python programs.
Most exceptions are not handled by programs, however, and result in
error messages as shown here:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

```

<!-- page: 2 -->

The last line of the error message indicates what happened. Exceptions
come in different types, and the type is printed as part of the
message: the types in the example are "ZeroDivisionError", "NameError"
and "TypeError". The string printed as the exception type is the name
of the built-in exception that occurred.  This is true for all built-
in exceptions, but need not be true for user-defined exceptions
(although it is a useful convention). Standard exception names are
built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception
and what caused it.

The preceding part of the error message shows the context where the
exception occurred, in the form of a stack traceback. In general it
contains a stack traceback listing source lines; however, it will not
display lines read from standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

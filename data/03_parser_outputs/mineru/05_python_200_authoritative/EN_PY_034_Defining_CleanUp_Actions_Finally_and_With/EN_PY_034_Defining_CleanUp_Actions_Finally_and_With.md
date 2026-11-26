<!-- page: 1 -->
# EN_PY_034: Defining Clean-up Actions: The finally Clause and Predefined with Statement

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Exceptions | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

8.7. Defining Clean-up Actions
==============================

The "try" statement has another optional clause which is intended to
define clean-up actions that must be executed under all circumstances.
For example:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt

```
If a "finally" clause is present, the "finally" clause will execute as
the last task before the "try" statement completes. The "finally"
clause runs whether or not the "try" statement produces an exception.
The following points discuss more complex cases when an exception
occurs:

* If an exception occurs during execution of the "try" clause, the
  exception may be handled by an "except" clause. If the exception is
  not handled by an "except" clause, the exception is re-raised after
  the "finally" clause has been executed.

* An exception could occur during execution of an "except" or "else"
  clause. Again, the exception is re-raised after the "finally" clause
  has been executed.


<!-- page: 2 -->

* If the "finally" clause executes a "break", "continue" or "return"
  statement, exceptions are not re-raised.

* If the "try" statement reaches a "break", "continue" or "return"
  statement, the "finally" clause will execute just prior to the
  "break", "continue" or "return" statement’s execution.

* If a "finally" clause includes a "return" statement, the returned
  value will be the one from the "finally" clause’s "return"
  statement, not the value from the "try" clause’s "return" statement.

For example:

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

```
A more complicated example:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'

```

<!-- page: 3 -->

As you can see, the "finally" clause is executed in any event.  The
"TypeError" raised by dividing two strings is not handled by the
"except" clause and therefore re-raised after the "finally" clause has
been executed.

In real world applications, the "finally" clause is useful for
releasing external resources (such as files or network connections),
regardless of whether the use of the resource was successful.


8.8. Predefined Clean-up Actions
================================

Some objects define standard clean-up actions to be undertaken when
the object is no longer needed, regardless of whether or not the
operation using the object succeeded or failed. Look at the following
example, which tries to open a file and print its contents to the
screen.

```python
for line in open("myfile.txt"):
    print(line, end="")

```
The problem with this code is that it leaves the file open for an
indeterminate amount of time after this part of the code has finished
executing. This is not an issue in simple scripts, but can be a
problem for larger applications. The "with" statement allows objects
like files to be used in a way that ensures they are always cleaned up
promptly and correctly.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

```
After the statement is executed, the file *f* is always closed, even
if a problem was encountered while processing the lines. Objects
which, like files, provide predefined clean-up actions will indicate
this in their documentation.

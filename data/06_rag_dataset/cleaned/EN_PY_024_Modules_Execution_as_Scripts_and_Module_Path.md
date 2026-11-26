# EN_PY_024: Modules: Python Modules, Executing as Scripts (__name__), and sys.path

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Modules | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

6. Modules
**********

If you quit from the Python interpreter and enter it again, the
definitions you have made (functions and variables) are lost.
Therefore, if you want to write a somewhat longer program, you are
better off using a text editor to prepare the input for the
interpreter and running it with that file as input instead.  This is
known as creating a *script*.  As your program gets longer, you may
want to split it into several files for easier maintenance.  You may
also want to use a handy function that you’ve written in several
programs without copying its definition into each program.

To support this, Python has a way to put definitions in a file and use
them in a script or in an interactive instance of the interpreter.
Such a file is called a *module*; definitions from a module can be
*imported* into other modules or into the *main* module (the
collection of variables that you have access to in a script executed
at the top level and in calculator mode).

A module is a file containing Python definitions and statements.  The
file name is the module name with the suffix ".py" appended.  Within a
module, the module’s name (as a string) is available as the value of
the global variable "__name__".  For instance, use your favorite text
editor to create a file called "fibo.py" in the current directory with
the following contents:

   # Fibonacci numbers module

```python
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

```

Now enter the Python interpreter and import this module with the
following command:

```python
>>> import fibo

```

This does not add the names of the functions defined in "fibo"
directly to the current *namespace* (see Python Scopes and Namespaces
for more details); it only adds the module name "fibo" there. Using
the module name you can access the functions:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

```

If you intend to use a function often you can assign it to a local
name:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

6.1. More on Modules
====================

A module can contain executable statements as well as function
definitions. These statements are intended to initialize the module.
They are executed only the *first* time the module name is encountered
in an import statement. [1] (They are also run if the file is executed
as a script.)

Each module has its own private namespace, which is used as the global
namespace by all functions defined in the module. Thus, the author of
a module can use global variables in the module without worrying about
accidental clashes with a user’s global variables. On the other hand,
if you know what you are doing you can touch a module’s global

variables with the same notation used to refer to its functions,
"modname.itemname".

Modules can import other modules.  It is customary but not required to
place all "import" statements at the beginning of a module (or script,
for that matter).  The imported module names, if placed at the top
level of a module (outside any functions or classes), are added to the
module’s global namespace.

There is a variant of the "import" statement that imports names from a
module directly into the importing module’s namespace.  For example:

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

This does not introduce the module name from which the imports are
taken in the local namespace (so in the example, "fibo" is not
defined).

There is even a variant to import all names that a module defines:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

This imports all names except those beginning with an underscore
("_"). In most cases Python programmers do not use this facility since
it introduces an unknown set of names into the interpreter, possibly
hiding some things you have already defined.

Note that in general the practice of importing "*" from a module or
package is frowned upon, since it often causes poorly readable code.
However, it is okay to use it to save typing in interactive sessions.

If the module name is followed by "as", then the name following "as"
is bound directly to the imported module.

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

This is effectively importing the module in the same way that "import
fibo" will do, with the only difference of it being available as
"fib".

It can also be used when utilising "from" with similar effects:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

Note:

  For efficiency reasons, each module is only imported once per
  interpreter session.  Therefore, if you change your modules, you
  must restart the interpreter – or, if it’s just one module you want
  to test interactively, use "importlib.reload()", e.g. "import
  importlib; importlib.reload(modulename)".

6.1.1. Executing modules as scripts
-----------------------------------

When you run a Python module with

   python fibo.py <arguments>

the code in the module will be executed, just as if you imported it,
but with the "__name__" set to ""__main__"".  That means that by
adding this code at the end of your module:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

```

you can make the file usable as a script as well as an importable
module, because the code that parses the command line only runs if the
module is executed as the “main” file:

   \$ python fibo.py 50
   0 1 1 2 3 5 8 13 21 34

If the module is imported, the code is not run:

```python
>>> import fibo
>>>

```

This is often used either to provide a convenient user interface to a
module, or for testing purposes (running the module as a script
executes a test suite).

6.1.2. The Module Search Path
-----------------------------

When a module named "spam" is imported, the interpreter first searches
for a built-in module with that name. These module names are listed in
"sys.builtin_module_names". If not found, it then searches for a file
named "spam.py" in a list of directories given by the variable
"sys.path".  "sys.path" is initialized from these locations:

* The directory containing the input script (or the current directory
  when no file is specified).

* "PYTHONPATH" (a list of directory names, with the same syntax as the
  shell variable "PATH").

* The installation-dependent default (by convention including a "site-
  packages" directory, handled by the "site" module).

More details are at The initialization of the sys.path module search
path.

Note:

  On file systems which support symlinks, the directory containing the
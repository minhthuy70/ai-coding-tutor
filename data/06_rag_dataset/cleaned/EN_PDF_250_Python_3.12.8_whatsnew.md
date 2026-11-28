# What's New in Python Release 3.12.8

**A. M. Kuchling**

**December 03, 2024**

**Python Software Foundation**

**Email: docs@python.org**

## Contents

- Summary – Release highlights
- New Features
- 2.1 PEP 695: Type Parameter Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 2.2 PEP 701: Syntactic formalization of f-strings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.3 PEP 684: A Per-Interpreter GIL . . . . . . . . . . . . . . . . . . . . . 6
- 2.4 PEP 669: Low impact monitoring for CPython . . . . . . . . . . . . 7
- 2.5 PEP 688: Making the buffer protocol accessible in Python 7
- 2.6 PEP 709: Comprehension inlining 7
- 2.7 Improved Error Messages 8
- New Features Related to Type Hints
- 3.1 PEP 692: Using TypedDict for more precise \*\*kwargs typing 8
- 3.2 PEP 698: Override Decorator for Static Typing 9
- Other Language Changes
- New Modules
- Improved Modules
- 6.1 array 10
- 6.2 asyncio 10
- 6.3 calendar 11
- 6.4 csv 11
- 6.5 dis 11
- 6.6 fractions 11
- 6.7 importlib.resources 11
- 6.8 inspect 11
- 6.9 itertools 12
- 6.**10** math 12
- 6.11 os 12
- 6.12 os.path 12
- 6.13 pathlib 12
- 6.14 pdb 13
- 6.15 random 13
- 6.16 shutil 13
- 6.17 sqlite3 13
- 6.18 statistics 13

- 6.19 sys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 6.20 tempfile . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 6.21 threading . . . . . . . . . . . . . . . . . . 14
- 6.22 tkinter . . . . . . . . . . . . . . 14
- 6.23 tokenize . . . . . . . . . . . . . 14
- 6.24 types . . . . . . . . . . 14
- 6.25 typing 6.26 unicodedata 6.27 unittest 6.28 uuid 16
- **7 Optimizations 16**
- **8 CPython bytecode changes 16**
- **9 Demos and Tools 16**
- **10 Deprecated 17**
- 10.1 Pending Removal in Python 3.13 19
- 10.2 Pending Removal in Python 3.14 20
- 10.3 Pending Removal in Python 3.15 21
- 10.4 Pending Removal in Python 3.16 22
- 10.5 Pending Removal in Future Versions 22
- **11 Removed 24**
- 11.1 asynchat and asyncore 24
- 11.2 configparser 25
- 11.3 distutils 25
- 11.4 ensurepip 25
- 11.5 enum 25
- 11.6 ftplib 25
- 11.7 gzip 25
- 11.8 hashlib 25
- 11.9 importlib 25
- 11.10imp 26
- 11.11io 27
- 11.12locale 27
- 11.13smtpd 27
- 11.14sqlite3 27
- 11.15ssl 27
- 11.16unittest 28
- 11.17webbrowser 28
- 11.18xml.etree.ElementTree 28
- 11.19zipimport 28
- 11.20Others 28
- **12 Porting to Python 3.12 29**
- 12.1 Changes in the Python API 29
- **13 Build Changes 30**
- **14 C API Changes 31**
- 14.1 New Features 31
- 14.2 Porting to Python 3.12 33
- 14.3 Deprecated 34
- 14.4 Removed 37
- **15 Notable changes in 3.12.4 38**
- 15.1 ipaddress 38

- **16 Notable changes in 3.12.5 38**
- 16.1 email 38
- **17 Notable changes in 3.12.6 38**
- 17.1 email 38
- **18 Notable changes in 3.12.8 38**
- 18.1 sys 38
- **Index 39**

## Editor

Adam Turner

This article explains the new features in Python 3.12, compared to 3.11. Python 3.12 was released on October 2, 2023. For full details, see the changelog.

**µ See also**

[**PEP 693**](https://peps.python.org/pep-0693/) – Python 3.12 Release Schedule

## 1 Summary – Release highlights

Python 3.12 is a stable release of the Python programming language, with a mix of changes to the language and the standard library. The library changes focus on cleaning up deprecated APIs, usability, and correctness. Of note, the distutils package has been removed from the standard library. Filesystem support in os and pathlib has seen a number of improvements, and several modules have better performance.

The language changes focus on usability, as f-strings have had many limitations removed and ‘Did you mean …’ suggestions continue to improve. The new type parameter syntax and type statement improve ergonomics for using generic types and type aliases with static type checkers.

This article doesn’t attempt to provide a complete specification of all new features, but instead gives a convenient overview. For full details, you should refer to the documentation, such as the Library Reference and Language Reference. If you want to understand the complete implementation and design rationale for a change, refer to the PEP for a particular new feature; but note that PEPs usually are not kept up-to-date once a feature has been fully implemented.

New syntax features:

• PEP 695, type parameter syntax and the type statement

New grammar features:

• PEP 701, f-strings in the grammar

Interpreter improvements:

• PEP 684, a unique per-interpreter GIL

• PEP 669, low impact monitoring

• Improved ‘Did you mean …’ suggestions for NameError, ImportError, and SyntaxError exceptions Python data model improvements:

• PEP 688, using the buffer protocol from Python

Significant improvements in the standard library:

• The pathlib.Path class now supports subclassing

• The os module received several improvements for Windows support

• A command-line interface has been added to the sqlite3 module

• isinstance() checks against runtime-checkable protocols enjoy a speed up of between two and 20 times

• The asyncio package has had a number of performance improvements, with some benchmarks showing a 75% speed up.

• A command-line interface has been added to the uuid module

• Due to the changes in PEP 701, producing tokens via the tokenize module is up to 64% faster.

## Security improvements:

• Replace the builtin hashlib implementations of SHA1, SHA3, SHA2-384, SHA2-512, and MD5 with formally verified code from the [HACL\*](https://github.com/hacl-star/hacl-star/) project. These builtin implementations remain as fallbacks that are only used when OpenSSL does not provide them.

## C API improvements:

• PEP 697, unstable C API tier

• PEP 683, immortal objects

CPython implementation improvements:

• PEP 709, comprehension inlining

• CPython support for the Linux perf profiler

• Implement stack overflow protection on supported platforms

## New typing features:

• PEP 692, using TypedDict to annotate \*\*kwargs

• PEP 698, typing.override() decorator

Important deprecations, removals or restrictions:

• [**PEP 623**](https://peps.python.org/pep-0623/): Remove wstr from Unicode objects in Python’s C API, reducing the size of every str object by at least 8 bytes.

• [**PEP 632**](https://peps.python.org/pep-0632/): Remove the distutils package. See [**the migration guide**](https://peps.python.org/pep-0632/#migration-advice) for advice replacing the APIs it provided. The third-party [Setuptools](https://setuptools.pypa.io/en/latest/deprecated/distutils-legacy.html) package continues to provide distutils, if you still require it in Python 3.12 and beyond.

• [gh-95299](https://github.com/python/cpython/issues/95299): Do not pre-install setuptools in virtual environments created with venv. This means that distutils, setuptools, pkg\_resources, and easy\_install will no longer available by default; to access these run pip install setuptools in the activated virtual environment.

• The asynchat, asyncore, and imp modules have been removed, along with several unittest.TestCase method aliases.

## 2 New Features

## 2.1 PEP 695: Type Parameter Syntax

Generic classes and functions under [**PEP 484**](https://peps.python.org/pep-0484/) were declared using a verbose syntax that left the scope of type parameters unclear and required explicit declarations of variance.

[**PEP 695**](https://peps.python.org/pep-0695/) introduces a new, more compact and explicit way to create generic classes and functions:

```python
def max[T](args: Iterable[T]) -> T:
```

(continues on next page)

```python
class list[T]:
    def __getitem__(self, index: int, /) -> T:
    def append(self, element: T) -> None:
```

(continued from previous page)

In addition, the PEP introduces a new way to declare type aliases using the type statement, which creates an instance of TypeAliasType:

```txt
type Point = tuple[float, float]
```

Type aliases can also be generic:

```txt
type Point[T] = tuple[T, T]
```

The new syntax allows declaring TypeVarTuple and ParamSpec parameters, as well as TypeVar parameters with bounds or constraints:

```python
type IntFunc[**P] = Callable[P, int]  # ParamSpec
type LabeledTuple[*Ts] = tuple[str, *Ts]  # TypeVarTuple
type HashableSequence[T: Hashable] = Sequence[T]  # TypeVar with bound
type IntOrStrSequence[T: (int, str)] = Sequence[T]  # TypeVar with constraints
```

The value of type aliases and the bound and constraints of type variables created through this syntax are evaluated only on demand (see lazy evaluation). This means type aliases are able to refer to other types defined later in the file.

Type parameters declared through a type parameter list are visible within the scope of the declaration and any nested scopes, but not in the outer scope. For example, they can be used in the type annotations for the methods of a generic class or in the class body. However, they cannot be used in the module scope after the class is defined. See type-params for a detailed description of the runtime semantics of type parameters.

In order to support these scoping semantics, a new kind of scope is introduced, the annotation scope. Annotation scopes behave for the most part like function scopes, but interact differently with enclosing class scopes. In Python 3.13, annotations will also be evaluated in annotation scopes.

See [**PEP 695**](https://peps.python.org/pep-0695/) for more details.

(PEP written by Eric Traut. Implementation by Jelle Zijlstra, Eric Traut, and others in [gh-103764](https://github.com/python/cpython/issues/103764).)

## 2.2 PEP 701: Syntactic formalization of f-strings

[**PEP 701**](https://peps.python.org/pep-0701/) lifts some restrictions on the usage of f-strings. Expression components inside f-strings can now be any valid Python expression, including strings reusing the same quote as the containing f-string, multi-line expressions, comments, backslashes, and unicode escape sequences. Let’s cover these in detail:

• Quote reuse: in Python 3.11, reusing the same quotes as the enclosing f-string raises a SyntaxError, forcing the user to either use other available quotes (like using double quotes or triple quotes if the f-string uses single quotes). In Python 3.12, you can now do things like this:

```python
>>> songs = ['Take me back to Eden', 'Alkaline', 'Ascensionism']
>>> f"This is the playlist: {", ".join(songs)}"
'This is the playlist: Take me back to Eden, Alkaline, Ascensionism'
```

Note that before this change there was no explicit limit in how f-strings can be nested, but the fact that string quotes cannot be reused inside the expression component of f-strings made it impossible to nest f-strings arbitrarily. In fact, this is the most nested f-string that could be written:

```txt
>>> f""" {f''' {f' {f" {1+1}"}'}}'''}'"'"
'2'
```

As now f-strings can contain any valid Python expression inside expression components, it is now possible to nest f-strings arbitrarily:

```txt
>>> f" {f" {f" {f" {f" {f" {f" {1+1}" }"} }"} }"} }
'2'
```

• Multi-line expressions and comments: In Python 3.11, f-string expressions must be defined in a single line, even if the expression within the f-string could normally span multiple lines (like literal lists being defined over multiple lines), making them harder to read. In Python 3.12 you can now define f-strings spanning multiple lines, and add inline comments:

```python
>>> f"This is the playlist: {", ".join([
...     'Take me back to Eden',  # My, my, those eyes like fire
...     'Alkaline',          # Not acid nor alkaline
...     'Ascensionism'      # Take to the broken skies at last
... ])}"
'This is the playlist: Take me back to Eden, Alkaline, Ascensionism'
```

• Backslashes and unicode characters: before Python 3.12 f-string expressions couldn’t contain any \ character. This also affected unicode escape sequences (such as \N{snowman}) as these contain the \N part that previously could not be part of expression components of f-strings. Now, you can define expressions like this:

```python
>>> print(f"This is the playlist: {"\n".join(songs)}")
This is the playlist: Take me back to Eden
Alkaline
Ascensionism
>>> print(f"This is the playlist: {"\N{BLACK HEART SUIT}".join(songs)}")
This is the playlist: Take me back to Eden♥Alkaline♥Ascensionism
```

## See [PEP 701](https://peps.python.org/pep-0701/) for more details.

As a positive side-effect of how this feature has been implemented (by parsing f-strings with [**the PEG parser**](https://peps.python.org/pep-0617/)), now error messages for f-strings are more precise and include the exact location of the error. For example, in Python 3.11, the following f-string raises a SyntaxError:

```txt
>>> my_string = f"{x z y}" + f"{1 + 1}"
    File "<stdin>", line 1
        (x z y)
            ^^^

SyntaxError: f-string: invalid syntax. Perhaps you forgot a comma?
```

but the error message doesn’t include the exact location of the error within the line and also has the expression artificially surrounded by parentheses. In Python 3.12, as f-strings are parsed with the PEG parser, error messages can be more precise and show the entire line:

```txt
>>> my_string = f"{x z y}" + f"{1 + 1}"
  File "<stdin>", line 1
    my_string = f"{x z y}" + f"{1 + 1}"
                                      ^^^

SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

(Contributed by Pablo Galindo, Batuhan Taskaya, Lysandros Nikolaou, Cristián Maureira-Fredes and Marta Gómez in [gh-102856](https://github.com/python/cpython/issues/102856). PEP written by Pablo Galindo, Batuhan Taskaya, Lysandros Nikolaou and Marta Gómez).

## 2.3 PEP 684: A Per-Interpreter GIL

[**PEP 684**](https://peps.python.org/pep-0684/) introduces a per-interpreter GIL, so that sub-interpreters may now be created with a unique GIL per interpreter. This allows Python programs to take full advantage of multiple CPU cores. This is currently only available through the C-API, though a Python API is [**anticipated for 3.13**](https://peps.python.org/pep-0554/).

Use the new Py\_NewInterpreterFromConfig() function to create an interpreter with its own GIL:

```c
PyInterpreterConfig config = {
    .check_multi_interp_extensions = 1,
    .gil = PyInterpreterConfig_OWN_GIL,
};
PyThreadState *tstate = NULL;
PyStatus status = Py_NewInterpreterFromConfig(&tstate, &config);
if (PyStatus_Exception(status)) {
    return -1;
}
/* The new interpreter is now active in the current thread. */
```

For further examples how to use the C-API for sub-interpreters with a per-interpreter GIL, see [Modules/\_xxsubinterpretersmodule.c](https://github.com/python/cpython/tree/3.12/Modules/_xxsubinterpretersmodule.c).

(Contributed by Eric Snow in [gh-104210](https://github.com/python/cpython/issues/104210), etc.)

## 2.4 PEP 669: Low impact monitoring for CPython

[**PEP 669**](https://peps.python.org/pep-0669/) defines a new API for profilers, debuggers, and other tools to monitor events in CPython. It covers a wide range of events, including calls, returns, lines, exceptions, jumps, and more. This means that you only pay for what you use, providing support for near-zero overhead debuggers and coverage tools. See sys.monitoring for details.

(Contributed by Mark Shannon in [gh-103082](https://github.com/python/cpython/issues/103082).)

## 2.5 PEP 688: Making the buffer protocol accessible in Python

[**PEP 688**](https://peps.python.org/pep-0688/) introduces a way to use the buffer protocol from Python code. Classes that implement the \_\_buffer\_\_() method are now usable as buffer types.

The new collections.abc.Buffer ABC provides a standard way to represent buffer objects, for example in type annotations. The new inspect.BufferFlags enum represents the flags that can be used to customize buffer creation. (Contributed by Jelle Zijlstra in [gh-102500](https://github.com/python/cpython/issues/102500).)

## 2.6 PEP 709: Comprehension inlining

Dictionary, list, and set comprehensions are now inlined, rather than creating a new single-use function object for each execution of the comprehension. This speeds up execution of a comprehension by up to two times. See [**PEP 709**](https://peps.python.org/pep-0709/) for further details.

Comprehension iteration variables remain isolated and don’t overwrite a variable of the same name in the outer scope, nor are they visible after the comprehension. Inlining does result in a few visible behavior changes:

• There is no longer a separate frame for the comprehension in tracebacks, and tracing/profiling no longer shows the comprehension as a function call.

• The symtable module will no longer produce child symbol tables for each comprehension; instead, the comprehension’s locals will be included in the parent function’s symbol table.

• Calling locals() inside a comprehension now includes variables from outside the comprehension, and no longer includes the synthetic .0 variable for the comprehension “argument”.

• A comprehension iterating directly over locals() (e.g. [k for k in locals()]) may see “RuntimeError: dictionary changed size during iteration” when run under tracing (e.g. code coverage measurement). This is the same behavior already seen in e.g. for k in locals():. To avoid the error, first create a list of keys to iterate over: keys = list(locals()); [k for k in keys].

(Contributed by Carl Meyer and Vladimir Matveev in [**PEP 709**](https://peps.python.org/pep-0709/).)

## 2.7 Improved Error Messages

• Modules from the standard library are now potentially suggested as part of the error messages displayed by the interpreter when a NameError is raised to the top level. (Contributed by Pablo Galindo in [gh-98254](https://github.com/python/cpython/issues/98254).)

```txt
>>> sys.version_info
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sys' is not defined. Did you forget to import 'sys'?
```

• Improve the error suggestion for NameError exceptions for instances. Now if a NameError is raised in a method and the instance has an attribute that’s exactly equal to the name in the exception, the suggestion will include self.&lt;NAME&gt; instead of the closest match in the method scope. (Contributed by Pablo Galindo in [gh-99139](https://github.com/python/cpython/issues/99139).)

```python
>>> class A:
...     def __init__(self):
...         self.blech = 1
...     def foo(self):
...         somethin = blech
>>> A().foo()
Traceback (most recent call last):
  File "<stdin>", line 1
    somethin = blech
      ^^^^^
NameError: name 'blech' is not defined. Did you mean: 'self.blech'?
```

• Improve the SyntaxError error message when the user types import x from y instead of from y import x. (Contributed by Pablo Galindo in [gh-98931](https://github.com/python/cpython/issues/98931).)

```python
>>> import a.y.z from b.y.z
Traceback (most recent call last):
  File "<stdin>", line 1
    import a.y.z from b.y.z
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^oooooooo
SyntaxError: Did you mean to use 'from ... import ..." instead?
```

• ImportError exceptions raised from failed from &lt;module&gt; import &lt;name&gt; statements now include suggestions for the value of &lt;name&gt; based on the available names in &lt;module&gt;. (Contributed by Pablo Galindo in [gh-91058](https://github.com/python/cpython/issues/91058).)

```python
>>> from collections import chainmap
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'chainmap' from 'collections'. Did you mean:
    'ChainMap'?
```

## 3 New Features Related to Type Hints

This section covers major changes affecting [**type hints**](https://peps.python.org/pep-0484/) and the typing module.

## 3.1 PEP 692: Using TypedDict for more precise \*\*kwargs typing

Typing \*\*kwargs in a function signature as introduced by [**PEP 484**](https://peps.python.org/pep-0484/) allowed for valid annotations only in cases where all of the \*\*kwargs were of the same type.

[**PEP 692**](https://peps.python.org/pep-0692/) specifies a more precise way of typing \*\*kwargs by relying on typed dictionaries:

```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
    name: str
    year: int

def foo(**kwargs: Unpack[Movie]): ...
```

See [**PEP 692**](https://peps.python.org/pep-0692/) for more details.

(Contributed by Franek Magiera in [gh-103629](https://github.com/python/cpython/issues/103629).)

## 3.2 PEP 698: Override Decorator for Static Typing

A new decorator typing.override() has been added to the typing module. It indicates to type checkers that the method is intended to override a method in a superclass. This allows type checkers to catch mistakes where a method that is intended to override something in a base class does not in fact do so.

Example:

```python
from typing import override

class Base:
  def get_color(self) -> str:
    return "blue"

class GoodChild(Base):
  @override  # ok: overrides Base.get_color
  def get_color(self) -> str:
    return "yellow"

class BadChild(Base):
  @override  # type checker error: does not override Base.get_color
  def get_colour(self) -> str:
    return "red"
```

See [**PEP 698**](https://peps.python.org/pep-0698/) for more details.

(Contributed by Steven Troxler in [gh-101561](https://github.com/python/cpython/issues/101561).)

## 4 Other Language Changes

• The parser now raises SyntaxError when parsing source code containing null bytes. (Contributed by Pablo Galindo in [gh-96670](https://github.com/python/cpython/issues/96670).)

• A backslash-character pair that is not a valid escape sequence now generates a SyntaxWarning, instead of DeprecationWarning. For example, re.compile("\d+\.\d+") now emits a SyntaxWarning ("\d" is an invalid escape sequence, use raw strings for regular expression: re.compile(r"\d+\.\d+")). In a future Python version, SyntaxError will eventually be raised, instead of SyntaxWarning. (Contributed by Victor Stinner in [gh-98401](https://github.com/python/cpython/issues/98401).)

• Octal escapes with value larger than 0o377 (ex: "\477"), deprecated in Python 3.11, now produce a SyntaxWarning, instead of DeprecationWarning. In a future Python version they will be eventually a SyntaxError. (Contributed by Victor Stinner in [gh-98401](https://github.com/python/cpython/issues/98401).)

• Variables used in the target part of comprehensions that are not stored to can now be used in assignment expressions (:=). For example, in [(b := 1) for a, b.prop in some\_iter], the assignment to b is now allowed. Note that assigning to variables stored to in the target part of comprehensions (like a) is still disallowed, as per [**PEP 572**](https://peps.python.org/pep-0572/). (Contributed by Nikita Sobolev in [gh-100581](https://github.com/python/cpython/issues/100581).)

• Exceptions raised in a class or type’s \_\_set\_name\_\_ method are no longer wrapped by a RuntimeError. Context information is added to the exception as a [**PEP 678**](https://peps.python.org/pep-0678/) note. (Contributed by Irit Katriel in [gh-77757](https://github.com/python/cpython/issues/77757).)

• When a try-except\* construct handles the entire ExceptionGroup and raises one other exception, that exception is no longer wrapped in an ExceptionGroup. Also changed in version 3.11.4. (Contributed by Irit Katriel in [gh-103590](https://github.com/python/cpython/issues/103590).)

The Garbage Collector now runs only on the eval breaker mechanism of the Python bytecode evaluation loop instead of object allocations. The GC can also run when PyErr\_CheckSignals() is called so C extensions that need to run for a long time without executing any Python code also have a chance to execute the GC periodically. (Contributed by Pablo Galindo in [gh-97922](https://github.com/python/cpython/issues/97922).)

• All builtin and extension callables expecting boolean parameters now accept arguments of any type instead of just bool and int. (Contributed by Serhiy Storchaka in [gh-60203](https://github.com/python/cpython/issues/60203).)

• memoryview now supports the half-float type (the “e” format code). (Contributed by Donghee Na and Antoine Pitrou in [gh-90751](https://github.com/python/cpython/issues/90751).)

• slice objects are now hashable, allowing them to be used as dict keys and set items. (Contributed by Will Bradshaw, Furkan Onder, and Raymond Hettinger in [gh-101264](https://github.com/python/cpython/issues/101264).)

• sum() now uses Neumaier summation to improve accuracy and commutativity when summing floats or mixed ints and floats. (Contributed by Raymond Hettinger in [gh-100425](https://github.com/python/cpython/issues/100425).)

• ast.parse() now raises SyntaxError instead of ValueError when parsing source code containing null bytes. (Contributed by Pablo Galindo in [gh-96670](https://github.com/python/cpython/issues/96670).)

• The extraction methods in tarfile, and shutil.unpack\_archive(), have a new a filter argument that allows limiting tar features than may be surprising or dangerous, such as creating files outside the destination directory. See tarfile extraction filters for details. In Python 3.14, the default will switch to 'data'. (Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)

• types.MappingProxyType instances are now hashable if the underlying mapping is hashable. (Contributed by Serhiy Storchaka in [gh-87995](https://github.com/python/cpython/issues/87995).)

• Add support for the perf profiler through the new environment variable PYTHONPERFSUPPORT and command-line option -X perf, as well as the new sys.activate\_stack\_trampoline(), sys. deactivate\_stack\_trampoline(), and sys.is\_stack\_trampoline\_active() functions. (Design by Pablo Galindo. Contributed by Pablo Galindo and Christian Heimes with contributions from Gregory P. Smith [Google] and Mark Shannon in [gh-96123](https://github.com/python/cpython/issues/96123).)

## 5 New Modules

• None.

## 6 Improved Modules

## 6.1 array

• The array.array class now supports subscripting, making it a generic type. (Contributed by Jelle Zijlstra in [gh-98658](https://github.com/python/cpython/issues/98658).)

## 6.2 asyncio

• The performance of writing to sockets in asyncio has been significantly improved. asyncio now avoids unnecessary copying when writing to sockets and uses sendmsg() if the platform supports it. (Contributed by Kumar Aditya in [gh-91166](https://github.com/python/cpython/issues/91166).)

• Add asyncio.eager\_task\_factory() and asyncio.create\_eager\_task\_factory() functions to allow opting an event loop in to eager task execution, making some use-cases 2x to 5x faster. (Contributed by Jacob Bower & Itamar Oren in [gh-102853](https://github.com/python/cpython/issues/102853), [gh-104140](https://github.com/python/cpython/issues/104140), and [gh-104138](https://github.com/python/cpython/issues/104138))

• On Linux, asyncio uses asyncio.PidfdChildWatcher by default if os.pidfd\_open() is available and functional instead of asyncio.ThreadedChildWatcher. (Contributed by Kumar Aditya in [gh-98024](https://github.com/python/cpython/issues/98024).)

• The event loop now uses the best available child watcher for each platform (asyncio.PidfdChildWatcher if supported and asyncio.ThreadedChildWatcher otherwise), so manually configuring a child watcher is not recommended. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

• Add loop\_factory parameter to asyncio.run() to allow specifying a custom event loop factory. (Contributed by Kumar Aditya in [gh-99388](https://github.com/python/cpython/issues/99388).)

• Add C implementation of asyncio.current\_task() for 4x-6x speedup. (Contributed by Itamar Oren and Pranav Thulasiram Bhat in [gh-100344](https://github.com/python/cpython/issues/100344).)

• asyncio.iscoroutine() now returns False for generators as asyncio does not support legacy generatorbased coroutines. (Contributed by Kumar Aditya in [gh-102748](https://github.com/python/cpython/issues/102748).)

• asyncio.wait() and asyncio.as\_completed() now accepts generators yielding tasks. (Contributed by Kumar Aditya in [gh-78530](https://github.com/python/cpython/issues/78530).)

## 6.3 calendar

• Add enums calendar.Month and calendar.Day defining months of the year and days of the week. (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

## 6.4 csv

• Add csv.QUOTE\_NOTNULL and csv.QUOTE\_STRINGS flags to provide finer grained control of None and empty strings by csv.writer objects.

## 6.5 dis

• Pseudo instruction opcodes (which are used by the compiler but do not appear in executable bytecode) are now exposed in the dis module. HAVE\_ARGUMENT is still relevant to real opcodes, but it is not useful for pseudo instructions. Use the new dis.hasarg collection instead. (Contributed by Irit Katriel in [gh-94216](https://github.com/python/cpython/issues/94216).)

• Add the dis.hasexc collection to signify instructions that set an exception handler. (Contributed by Irit Katriel in [gh-94216](https://github.com/python/cpython/issues/94216).)

## 6.6 fractions

• Objects of type fractions.Fraction now support float-style formatting. (Contributed by Mark Dickinson in [gh-100161](https://github.com/python/cpython/issues/100161).)

## 6.7 importlib.resources

• importlib.resources.as\_file() now supports resource directories. (Contributed by Jason R. Coombs in [gh-97930](https://github.com/python/cpython/issues/97930).)

• Rename first parameter of importlib.resources.files() to anchor. (Contributed by Jason R. Coombs in [gh-100598](https://github.com/python/cpython/issues/100598).)

## 6.8 inspect

• Add inspect.markcoroutinefunction() to mark sync functions that return a coroutine for use with inspect.iscoroutinefunction(). (Contributed by Carlton Gibson in [gh-99247](https://github.com/python/cpython/issues/99247).)

• Add inspect.getasyncgenstate() and inspect.getasyncgenlocals() for determining the current state of asynchronous generators. (Contributed by Thomas Krennwallner in [gh-79940](https://github.com/python/cpython/issues/79940).)

• The performance of inspect.getattr\_static() has been considerably improved. Most calls to the function should be at least 2x faster than they were in Python 3.11. (Contributed by Alex Waygood in [gh-103193](https://github.com/python/cpython/issues/103193).)

## 6.9 itertools

• Add itertools.batched() for collecting into even-sized tuples where the last batch may be shorter than the rest. (Contributed by Raymond Hettinger in [gh-98363](https://github.com/python/cpython/issues/98363).)

## 6.10 math

• Add math.sumprod() for computing a sum of products. (Contributed by Raymond Hettinger in [gh-100485](https://github.com/python/cpython/issues/100485).)

• Extend math.nextafter() to include a steps argument for moving up or down multiple steps at a time. (Contributed by Matthias Goergens, Mark Dickinson, and Raymond Hettinger in [gh-94906](https://github.com/python/cpython/issues/94906).)

## 6.11 os

• Add os.PIDFD\_NONBLOCK to open a file descriptor for a process with os.pidfd\_open() in non-blocking mode. (Contributed by Kumar Aditya in [gh-93312](https://github.com/python/cpython/issues/93312).)

• os.DirEntry now includes an os.DirEntry.is\_junction() method to check if the entry is a junction. (Contributed by Charles Machalow in [gh-99547](https://github.com/python/cpython/issues/99547).)

• Add os.listdrives(), os.listvolumes() and os.listmounts() functions on Windows for enumerating drives, volumes and mount points. (Contributed by Steve Dower in [gh-102519](https://github.com/python/cpython/issues/102519).)

os.stat() and os.lstat() are now more accurate on Windows. The st\_birthtime field will now be filled with the creation time of the file, and st\_ctime is deprecated but still contains the creation time (but in the future will return the last metadata change, for consistency with other platforms). st\_dev may be up to 64 bits and st\_ino up to 128 bits depending on your file system, and st\_rdev is always set to zero rather than incorrect values. Both functions may be significantly faster on newer releases of Windows. (Contributed by Steve Dower in [gh-99726](https://github.com/python/cpython/issues/99726).)

• As of 3.12.4, os.mkdir() and os.makedirs() on Windows now support passing a mode value of 0o700 to apply access control to the new directory. This implicitly affects tempfile.mkdtemp() and is a mitigation for [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030). Other values for mode continue to be ignored. (Contributed by Steve Dower in [gh-118486](https://github.com/python/cpython/issues/118486).)

## 6.12 os.path

• Add os.path.isjunction() to check if a given path is a junction. (Contributed by Charles Machalow in [gh-99547](https://github.com/python/cpython/issues/99547).)

• Add os.path.splitroot() to split a path into a triad (drive, root, tail). (Contributed by Barney Gale in [gh-101000](https://github.com/python/cpython/issues/101000).)

## 6.13 pathlib

• Add support for subclassing pathlib.PurePath and pathlib.Path, plus their Posix- and Windowsspecific variants. Subclasses may override the pathlib.PurePath.with\_segments() method to pass information between path instances.

• Add pathlib.Path.walk() for walking the directory trees and generating all file or directory names within them, similar to os.walk(). (Contributed by Stanislav Zmiev in [gh-90385](https://github.com/python/cpython/issues/90385).)

• Add walk\_up optional parameter to pathlib.PurePath.relative\_to() to allow the insertion of .. entries in the result; this behavior is more consistent with os.path.relpath(). (Contributed by Domenico Ragusa in [gh-84538](https://github.com/python/cpython/issues/84538).)

• Add pathlib.Path.is\_junction() as a proxy to os.path.isjunction(). (Contributed by Charles Machalow in [gh-99547](https://github.com/python/cpython/issues/99547).)

• Add case\_sensitive optional parameter to pathlib.Path.glob(), pathlib.Path.rglob() and pathlib.PurePath.match() for matching the path’s case sensitivity, allowing for more precise control over the matching process.

## 6.14 pdb

• Add convenience variables to hold values temporarily for debug session and provide quick access to values like the current frame or the return value. (Contributed by Tian Gao in [gh-103693](https://github.com/python/cpython/issues/103693).)

## 6.15 random

• Add random.binomialvariate(). (Contributed by Raymond Hettinger in [gh-81620](https://github.com/python/cpython/issues/81620).)

• Add a default of lambd=1.0 to random.expovariate(). (Contributed by Raymond Hettinger in [gh-100234](https://github.com/python/cpython/issues/100234).)

## 6.16 shutil

• shutil.make\_archive() now passes the root\_dir argument to custom archivers which support it. In this case it no longer temporarily changes the current working directory of the process to root\_dir to perform archiving. (Contributed by Serhiy Storchaka in [gh-74696](https://github.com/python/cpython/issues/74696).)

• shutil.rmtree() now accepts a new argument onexc which is an error handler like onerror but which expects an exception instance rather than a (typ, val, tb) triplet. onerror is deprecated. (Contributed by Irit Katriel in [gh-102828](https://github.com/python/cpython/issues/102828).)

• shutil.which() now consults the PATHEXT environment variable to find matches within PATH on Windows even when the given cmd includes a directory component. (Contributed by Charles Machalow in [gh-103179](https://github.com/python/cpython/issues/103179).)

shutil.which() will call NeedCurrentDirectoryForExePathW when querying for executables on Windows to determine if the current working directory should be prepended to the search path. (Contributed by Charles Machalow in [gh-103179](https://github.com/python/cpython/issues/103179).)

shutil.which() will return a path matching the cmd with a component from PATHEXT prior to a direct match elsewhere in the search path on Windows. (Contributed by Charles Machalow in [gh-103179](https://github.com/python/cpython/issues/103179).)

## 6.17 sqlite3

• Add a command-line interface. (Contributed by Erlend E. Aasland in [gh-77617](https://github.com/python/cpython/issues/77617).)

• Add the sqlite3.Connection.autocommit attribute to sqlite3.Connection and the autocommit parameter to sqlite3.connect() to control [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction handling. (Contributed by Erlend E. Aasland in [gh-83638](https://github.com/python/cpython/issues/83638).)

• Add entrypoint keyword-only parameter to sqlite3.Connection.load\_extension(), for overriding the SQLite extension entry point. (Contributed by Erlend E. Aasland in [gh-103015](https://github.com/python/cpython/issues/103015).)

• Add sqlite3.Connection.getconfig() and sqlite3.Connection.setconfig() to sqlite3. Connection to make configuration changes to a database connection. (Contributed by Erlend E. Aasland in [gh-103489](https://github.com/python/cpython/issues/103489).)

## 6.18 statistics

• Extend statistics.correlation() to include as a ranked method for computing the Spearman correlation of ranked data. (Contributed by Raymond Hettinger in [gh-95861](https://github.com/python/cpython/issues/95861).)

## 6.19 sys

• Add the sys.monitoring namespace to expose the new PEP 669 monitoring API. (Contributed by Mark Shannon in [gh-103082](https://github.com/python/cpython/issues/103082).)

• Add sys.activate\_stack\_trampoline() and sys.deactivate\_stack\_trampoline() for activating and deactivating stack profiler trampolines, and sys.is\_stack\_trampoline\_active() for querying if stack profiler trampolines are active. (Contributed by Pablo Galindo and Christian Heimes with contributions from Gregory P. Smith [Google] and Mark Shannon in [gh-96123](https://github.com/python/cpython/issues/96123).)

• Add sys.last\_exc which holds the last unhandled exception that was raised (for post-mortem debugging use cases). Deprecate the three fields that have the same information in its legacy form: sys.last\_type, sys.last\_value and sys.last\_traceback. (Contributed by Irit Katriel in [gh-102778](https://github.com/python/cpython/issues/102778).)

• sys.\_current\_exceptions() now returns a mapping from thread-id to an exception instance, rather than to a (typ, exc, tb) tuple. (Contributed by Irit Katriel in [gh-103176](https://github.com/python/cpython/issues/103176).)

• sys.setrecursionlimit() and sys.getrecursionlimit(). The recursion limit now applies only to Python code. Builtin functions do not use the recursion limit, but are protected by a different mechanism that prevents recursion from causing a virtual machine crash.

## 6.20 tempfile

• The tempfile.NamedTemporaryFile function has a new optional parameter delete\_on\_close (Contributed by Evgeny Zorin in [gh-58451](https://github.com/python/cpython/issues/58451).)

• tempfile.mkdtemp() now always returns an absolute path, even if the argument provided to the dir parameter is a relative path.

• As of 3.12.4 on Windows, the default mode 0o700 used by tempfile.mkdtemp() now limits access to the new directory due to changes to os.mkdir(). This is a mitigation for [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030). (Contributed by Steve Dower in [gh-118486](https://github.com/python/cpython/issues/118486).)

## 6.21 threading

• Add threading.settrace\_all\_threads() and threading.setprofile\_all\_threads() that allow to set tracing and profiling functions in all running threads in addition to the calling one. (Contributed by Pablo Galindo in [gh-93503](https://github.com/python/cpython/issues/93503).)

## 6.22 tkinter

• tkinter.Canvas.coords() now flattens its arguments. It now accepts not only coordinates as separate arguments (x1, y1, x2, y2, ...) and a sequence of coordinates ([x1, y1, x2, y2, ...]), but also coordinates grouped in pairs ((x1, y1), (x2, y2), ... and [(x1, y1), (x2, y2), ...]), like create\_\*() methods. (Contributed by Serhiy Storchaka in [gh-94473](https://github.com/python/cpython/issues/94473).)

## 6.23 tokenize

• The tokenize module includes the changes introduced in [**PEP 701**](https://peps.python.org/pep-0701/). (Contributed by Marta Gómez Macías and Pablo Galindo in [gh-102856](https://github.com/python/cpython/issues/102856).) See Porting to Python 3.12 for more information on the changes to the tokenize module.

## 6.24 types

• Add types.get\_original\_bases() to allow for further introspection of user-defined-generics when subclassed. (Contributed by James Hilton-Balfe and Alex Waygood in [gh-101827](https://github.com/python/cpython/issues/101827).)

## 6.25 typing

• isinstance() checks against runtime-checkable protocols now use inspect. getattr\_static() rather than hasattr() to lookup whether attributes exist. This means that descriptors and \_\_getattr\_\_() methods are no longer unexpectedly evaluated during isinstance() checks against runtime-checkable protocols. However, it may also mean that some objects which used to be considered instances of a runtime-checkable protocol may no longer be considered instances of that protocol on Python 3.12+, and vice versa. Most users are unlikely to be affected by this change. (Contributed by Alex Waygood in [gh-102433](https://github.com/python/cpython/issues/102433).)

• The members of a runtime-checkable protocol are now considered “frozen” at runtime as soon as the class has been created. Monkey-patching attributes onto a runtime-checkable protocol will still work, but will have no impact on isinstance() checks comparing objects to the protocol. For example:

```python
>>> from typing import Protocol, runtime_checkable
>>> @runtime_checkable
... class HasX(Protocol):
...     x = 1
>>> class Foo: ...
>>> f = Foo()
>>> isinstance(f, HasX)
False
>>> f.x = 1
>>> isinstance(f, HasX)
True
>>> HasX.y = 2
>>> isinstance(f, HasX)  # unchanged, even though HasX now also has a "y" attribute
True
```

This change was made in order to speed up isinstance() checks against runtime-checkable protocols.

• The performance profile of isinstance() checks against runtime-checkable protocols has changed significantly. Most isinstance() checks against protocols with only a few members should be at least 2x faster than in 3.11, and some may be 20x faster or more. However, isinstance() checks against protocols with many members may be slower than in Python 3.11. (Contributed by Alex Waygood in [gh-74690](https://github.com/python/cpython/issues/74690) and [gh-103193](https://github.com/python/cpython/issues/103193).)

• All typing.TypedDict and typing.NamedTuple classes now have the \_\_orig\_bases\_\_ attribute. (Contributed by Adrian Garcia Badaracco in [gh-103699](https://github.com/python/cpython/issues/103699).)

• Add frozen\_default parameter to typing.dataclass\_transform(). (Contributed by Erik De Bonte in [gh-99957](https://github.com/python/cpython/issues/99957).)

## 6.26 unicodedata

• The Unicode database has been updated to version 15.0.0. (Contributed by Benjamin Peterson in [gh-96734](https://github.com/python/cpython/issues/96734)).

## 6.27 unittest

Add a --durations command line option, showing the N slowest test cases:

```txt
python3 -m unittest --durations=3 lib.tests.test_threading
Slowest test durations
-----------------------------------
1.210s     test_timeout (Lib.test.test_threading.BarrierTests)
1.003s     test_default_timeout (Lib.test.test_threading.BarrierTests)
0.518s     test_timeout (Lib.test.test_threading.EventTests)

(0.000 durations hidden.  Use -v to show these durations.)
-----------------------------------
Ran 158 tests in 9.869s

OK (skipped=3)
```

(Contributed by Giampaolo Rodola in [gh-48330](https://github.com/python/cpython/issues/48330))

## 6.28 uuid

• Add a command-line interface. (Contributed by Adam Chhina in [gh-88597](https://github.com/python/cpython/issues/88597).)

## 7 Optimizations

• Remove wstr and wstr\_length members from Unicode objects. It reduces object size by 8 or 16 bytes on 64bit platform. ([**PEP 623**](https://peps.python.org/pep-0623/)) (Contributed by Inada Naoki in [gh-92536](https://github.com/python/cpython/issues/92536).)

• Add experimental support for using the BOLT binary optimizer in the build process, which improves performance by 1-5%. (Contributed by Kevin Modzelewski in [gh-90536](https://github.com/python/cpython/issues/90536) and tuned by Donghee Na in [gh-101525](https://github.com/python/cpython/issues/101525))

• Speed up the regular expression substitution (functions re.sub() and re.subn() and corresponding re. Pattern methods) for replacement strings containing group references by 2–3 times. (Contributed by Serhiy Storchaka in [gh-91524](https://github.com/python/cpython/issues/91524).)

• Speed up asyncio.Task creation by deferring expensive string formatting. (Contributed by Itamar Oren in [gh-103793](https://github.com/python/cpython/issues/103793).)

• The tokenize.tokenize() and tokenize.generate\_tokens() functions are up to 64% faster as a side effect of the changes required to cover [**PEP 701**](https://peps.python.org/pep-0701/) in the tokenize module. (Contributed by Marta Gómez Macías and Pablo Galindo in [gh-102856](https://github.com/python/cpython/issues/102856).)

• Speed up super() method calls and attribute loads via the new LOAD\_SUPER\_ATTR instruction. (Contributed by Carl Meyer and Vladimir Matveev in [gh-103497](https://github.com/python/cpython/issues/103497).)

## 8 CPython bytecode changes

• Remove the LOAD\_METHOD instruction. It has been merged into LOAD\_ATTR. LOAD\_ATTR will now behave like the old LOAD\_METHOD instruction if the low bit of its oparg is set. (Contributed by Ken Jin in [gh-93429](https://github.com/python/cpython/issues/93429).)

• Remove the JUMP\_IF\_FALSE\_OR\_POP and JUMP\_IF\_TRUE\_OR\_POP instructions. (Contributed by Irit Katriel in [gh-102859](https://github.com/python/cpython/issues/102859).)

• Remove the PRECALL instruction. (Contributed by Mark Shannon in [gh-92925](https://github.com/python/cpython/issues/92925).)

• Add the BINARY\_SLICE and STORE\_SLICE instructions. (Contributed by Mark Shannon in [gh-94163](https://github.com/python/cpython/issues/94163).)

• Add the CALL\_INTRINSIC\_1 instructions. (Contributed by Mark Shannon in [gh-99005](https://github.com/python/cpython/issues/99005).)

• Add the CALL\_INTRINSIC\_2 instruction. (Contributed by Irit Katriel in [gh-101799](https://github.com/python/cpython/issues/101799).)

• Add the CLEANUP\_THROW instruction. (Contributed by Brandt Bucher in [gh-90997](https://github.com/python/cpython/issues/90997).)

• Add the END\_SEND instruction. (Contributed by Mark Shannon in [gh-103082](https://github.com/python/cpython/issues/103082).)

• Add the LOAD\_FAST\_AND\_CLEAR instruction as part of the implementation of [**PEP 709**](https://peps.python.org/pep-0709/). (Contributed by Carl Meyer in [gh-101441](https://github.com/python/cpython/issues/101441).)

• Add the LOAD\_FAST\_CHECK instruction. (Contributed by Dennis Sweeney in [gh-93143](https://github.com/python/cpython/issues/93143).)

• Add the LOAD\_FROM\_DICT\_OR\_DEREF, LOAD\_FROM\_DICT\_OR\_GLOBALS, and LOAD\_LOCALS opcodes as part of the implementation of [**PEP 695**](https://peps.python.org/pep-0695/). Remove the LOAD\_CLASSDEREF opcode, which can be replaced with LOAD\_LOCALS plus LOAD\_FROM\_DICT\_OR\_DEREF. (Contributed by Jelle Zijlstra in [gh-103764](https://github.com/python/cpython/issues/103764).)

• Add the LOAD\_SUPER\_ATTR instruction. (Contributed by Carl Meyer and Vladimir Matveev in [gh-103497](https://github.com/python/cpython/issues/103497).)

• Add the RETURN\_CONST instruction. (Contributed by Wenyang Wang in [gh-101632](https://github.com/python/cpython/issues/101632).)

## 9 Demos and Tools

• Remove the Tools/demo/ directory which contained old demo scripts. A copy can be found in the [old-demos project](https://github.com/gvanrossum/old-demos). (Contributed by Victor Stinner in [gh-97681](https://github.com/python/cpython/issues/97681).)

• Remove outdated example scripts of the Tools/scripts/ directory. A copy can be found in the [old-demos project](https://github.com/gvanrossum/old-demos). (Contributed by Victor Stinner in [gh-97669](https://github.com/python/cpython/issues/97669).)

## 10 Deprecated

• argparse: The type, choices, and metavar parameters of argparse.BooleanOptionalAction are deprecated and will be removed in 3.14. (Contributed by Nikita Sobolev in [gh-92248](https://github.com/python/cpython/issues/92248).)

• ast: The following ast features have been deprecated in documentation since Python 3.8, now cause a DeprecationWarning to be emitted at runtime when they are accessed or used, and will be removed in Python 3.14:

– ast.Num

– ast.Str

– ast.Bytes

– ast.NameConstant

– ast.Ellipsis

Use ast.Constant instead. (Contributed by Serhiy Storchaka in [gh-90953](https://github.com/python/cpython/issues/90953).)

## • asyncio:

– The child watcher classes asyncio.MultiLoopChildWatcher, asyncio.FastChildWatcher, asyncio.AbstractChildWatcher and asyncio.SafeChildWatcher are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

– asyncio.set\_child\_watcher(), asyncio.get\_child\_watcher(), asyncio.AbstractEventLoopPolicy.set\_child\_watcher() and asyncio. AbstractEventLoopPolicy.get\_child\_watcher() are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

– The get\_event\_loop() method of the default event loop policy now emits a DeprecationWarning if there is no current event loop set and it decides to create one. (Contributed by Serhiy Storchaka and Guido van Rossum in [gh-100160](https://github.com/python/cpython/issues/100160).)

• calendar: calendar.January and calendar.February constants are deprecated and replaced by calendar.JANUARY and calendar.FEBRUARY. (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

• collections.abc: Deprecated collections.abc.ByteString. Prefer Sequence or collections. abc.Buffer. For use in typing, prefer a union, like bytes | bytearray, or collections.abc.Buffer. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

datetime: datetime.datetime’s utcnow() and utcfromtimestamp() are deprecated and will be removed in a future version. Instead, use timezone-aware objects to represent datetimes in UTC: respectively, call now() and fromtimestamp() with the tz parameter set to datetime.UTC. (Contributed by Paul Ganssle in [gh-103857](https://github.com/python/cpython/issues/103857).)

• email: Deprecate the isdst parameter in email.utils.localtime(). (Contributed by Alan Williams in [gh-72346](https://github.com/python/cpython/issues/72346).)

• importlib.abc: Deprecated the following classes, scheduled for removal in Python 3.14:

– importlib.abc.ResourceReader

– importlib.abc.Traversable

– importlib.abc.TraversableResources

Use importlib.resources.abc classes instead:

– importlib.resources.abc.Traversable

– importlib.resources.abc.TraversableResources

(Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963).)

• itertools: Deprecate the support for copy, deepcopy, and pickle operations, which is undocumented, inefficient, historically buggy, and inconsistent. This will be removed in 3.14 for a significant reduction in code volume and maintenance burden. (Contributed by Raymond Hettinger in [gh-101588](https://github.com/python/cpython/issues/101588).)

• multiprocessing: In Python 3.14, the default multiprocessing start method will change to a safer one on Linux, BSDs, and other non-macOS POSIX platforms where 'fork' is currently the default ([gh-84559](https://github.com/python/cpython/issues/84559)). Adding a runtime warning about this was deemed too disruptive as the majority of code is not expected to care. Use the get\_context() or set\_start\_method() APIs to explicitly specify when your code requires 'fork'. See contexts and start methods.

• pkgutil: pkgutil.find\_loader() and pkgutil.get\_loader() are deprecated and will be removed in Python 3.14; use importlib.util.find\_spec() instead. (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850).)

• pty: The module has two undocumented master\_open() and slave\_open() functions that have been deprecated since Python 2 but only gained a proper DeprecationWarning in 3.12. Remove them in 3.14. (Contributed by Soumendra Ganguly and Gregory P. Smith in [gh-85984](https://github.com/python/cpython/issues/85984).)

• os:

– The st\_ctime fields return by os.stat() and os.lstat() on Windows are deprecated. In a future release, they will contain the last metadata change time, consistent with other platforms. For now, they still contain the creation time, which is also available in the new st\_birthtime field. (Contributed by Steve Dower in [gh-99726](https://github.com/python/cpython/issues/99726).)

– On POSIX platforms, os.fork() can now raise a DeprecationWarning when it can detect being called from a multithreaded process. There has always been a fundamental incompatibility with the POSIX platform when doing so. Even if such code appeared to work. We added the warning to raise awareness as issues encountered by code doing this are becoming more frequent. See the os.fork() documentation for more details along with [this discussion on fork being incompatible with threads](https://discuss.python.org/t/concerns-regarding-deprecation-of-fork-with-alive-threads/33555) for why we’re now surfacing this longstanding platform compatibility problem to developers.

When this warning appears due to usage of multiprocessing or concurrent.futures the fix is to use a different multiprocessing start method such as "spawn" or "forkserver".

• shutil: The onerror argument of shutil.rmtree() is deprecated; use onexc instead. (Contributed by Irit Katriel in [gh-102828](https://github.com/python/cpython/issues/102828).)

• sqlite3:

– default adapters and converters are now deprecated. Instead, use the sqlite3-adapter-converter-recipes and tailor them to your needs. (Contributed by Erlend E. Aasland in [gh-90016](https://github.com/python/cpython/issues/90016).)

– In execute(), DeprecationWarning is now emitted when named placeholders are used together with parameters supplied as a sequence instead of as a dict. Starting from Python 3.14, using named placeholders with parameters supplied as a sequence will raise a ProgrammingError. (Contributed by Erlend E. Aasland in [gh-101698](https://github.com/python/cpython/issues/101698).)

• sys: The sys.last\_type, sys.last\_value and sys.last\_traceback fields are deprecated. Use sys. last\_exc instead. (Contributed by Irit Katriel in [gh-102778](https://github.com/python/cpython/issues/102778).)

• tarfile: Extracting tar archives without specifying filter is deprecated until Python 3.14, when 'data' filter will become the default. See tarfile-extraction-filter for details.

• typing:

– typing.Hashable and typing.Sized, aliases for collections.abc.Hashable and collections.abc.Sized respectively, are deprecated. ([gh-94309](https://github.com/python/cpython/issues/94309).)

– typing.ByteString, deprecated since Python 3.9, now causes a DeprecationWarning to be emitted when it is used. (Contributed by Alex Waygood in [gh-91896](https://github.com/python/cpython/issues/91896).)

• xml.etree.ElementTree: The module now emits DeprecationWarning when testing the truth value of an xml.etree.ElementTree.Element. Before, the Python implementation emitted FutureWarning, and the C implementation emitted nothing. (Contributed by Jacob Walls in [gh-83122](https://github.com/python/cpython/issues/83122).)

• The 3-arg signatures (type, value, traceback) of coroutine throw(), generator throw() and async generator throw() are deprecated and may be removed in a future version of Python. Use the single-arg versions of these functions instead. (Contributed by Ofey Chan in [gh-89874](https://github.com/python/cpython/issues/89874).)

• DeprecationWarning is now raised when \_\_package\_\_ on a module differs from \_\_spec\_\_.parent (previously it was ImportWarning). (Contributed by Brett Cannon in [gh-65961](https://github.com/python/cpython/issues/65961).)

• Setting \_\_package\_\_ or \_\_cached\_\_ on a module is deprecated, and will cease to be set or taken into consideration by the import system in Python 3.14. (Contributed by Brett Cannon in [gh-65961](https://github.com/python/cpython/issues/65961).)

• The bitwise inversion operator (\~) on bool is deprecated. It will throw an error in Python 3.16. Use not for logical negation of bools instead. In the rare case that you really need the bitwise inversion of the underlying int, convert to int explicitly: \~int(x). (Contributed by Tim Hoffmann in [gh-103487](https://github.com/python/cpython/issues/103487).)

• Accessing co\_lnotab on code objects was deprecated in Python 3.10 via [**PEP 626**](https://peps.python.org/pep-0626/), but it only got a proper DeprecationWarning in 3.12. May be removed in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)

## 10.1 Pending Removal in Python 3.13

Modules (see [**PEP 594**](https://peps.python.org/pep-0594/)):

• aifc

• audioop

• cgi

• cgitb

• chunk

• crypt

• imghdr

• mailcap

• msilib

• nis

• nntplib

• ossaudiodev

• pipes

• sndhdr

• spwd

• sunau

• telnetlib

• uu

• xdrlib

## Other modules:

• lib2to3, and the **2to3** program ([gh-84540](https://github.com/python/cpython/issues/84540))

## APIs:

• configparser.LegacyInterpolation ([gh-90765](https://github.com/python/cpython/issues/90765))

• locale.resetlocale() ([gh-90817](https://github.com/python/cpython/issues/90817))

• turtle.RawTurtle.settiltangle() ([gh-50096](https://github.com/python/cpython/issues/50096))

• unittest.findTestCases() ([gh-50096](https://github.com/python/cpython/issues/50096))

• unittest.getTestCaseNames() ([gh-50096](https://github.com/python/cpython/issues/50096))

```txt
- unittest.makeSuite() (gh-50096)
txt
- unittest.TestProgram.usageExit() (gh-67048)
txt
- webbrowser.MacOSX (gh-86421)
```

• classmethod descriptor chaining ([gh-89519](https://github.com/python/cpython/issues/89519))

• importlib.resources deprecated methods:

```txt
- contents()
- is_resource()
- open_binary()
- open_text()
- path()
- read_binary()
- read_text()
```

Use importlib.resources.files() instead. Refer to [importlib-resources: Migrating from Legacy](https://importlib-resources.readthedocs.io/en/latest/using.html#migrating-from-legacy) ([gh-106531](https://github.com/python/cpython/issues/106531))

## 10.2 Pending Removal in Python 3.14

• argparse: The type, choices, and metavar parameters of argparse.BooleanOptionalAction are deprecated and will be removed in 3.14. (Contributed by Nikita Sobolev in [gh-92248](https://github.com/python/cpython/issues/92248).)

• ast: The following features have been deprecated in documentation since Python 3.8, now cause a DeprecationWarning to be emitted at runtime when they are accessed or used, and will be removed in Python 3.14:

```yaml
- ast.Num
- ast.Str
- ast.Bytes
- ast.NameConstant
- ast.Ellipsis
```

Use ast.Constant instead. (Contributed by Serhiy Storchaka in [gh-90953](https://github.com/python/cpython/issues/90953).)

## • asyncio:

– The child watcher classes MultiLoopChildWatcher, FastChildWatcher, AbstractChild-Watcher and SafeChildWatcher are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

– asyncio.set\_child\_watcher(), asyncio.get\_child\_watcher(), asyncio.AbstractEventLoopPolicy.set\_child\_watcher() and asyncio. AbstractEventLoopPolicy.get\_child\_watcher() are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

– The get\_event\_loop() method of the default event loop policy now emits a DeprecationWarning if there is no current event loop set and it decides to create one. (Contributed by Serhiy Storchaka and Guido van Rossum in [gh-100160](https://github.com/python/cpython/issues/100160).)

• collections.abc: Deprecated ByteString. Prefer Sequence or Buffer. For use in typing, prefer a union, like bytes | bytearray, or collections.abc.Buffer. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

• email: Deprecated the isdst parameter in email.utils.localtime(). (Contributed by Alan Williams in [gh-72346](https://github.com/python/cpython/issues/72346).)

• importlib: \_\_package\_\_ and \_\_cached\_\_ will cease to be set or taken into consideration by the import system ([gh-97879](https://github.com/python/cpython/issues/97879)).

• importlib.abc deprecated classes:

– importlib.abc.ResourceReader

– importlib.abc.Traversable

– importlib.abc.TraversableResources

Use importlib.resources.abc classes instead:

– importlib.resources.abc.Traversable

– importlib.resources.abc.TraversableResources

(Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963).)

• itertools had undocumented, inefficient, historically buggy, and inconsistent support for copy, deepcopy, and pickle operations. This will be removed in 3.14 for a significant reduction in code volume and maintenance burden. (Contributed by Raymond Hettinger in [gh-101588](https://github.com/python/cpython/issues/101588).)

• multiprocessing: The default start method will change to a safer one on Linux, BSDs, and other non-macOS POSIX platforms where 'fork' is currently the default ([gh-84559](https://github.com/python/cpython/issues/84559)). Adding a runtime warning about this was deemed too disruptive as the majority of code is not expected to care. Use the get\_context() or set\_start\_method() APIs to explicitly specify when your code requires 'fork'. See multiprocessingstart-methods.

• pathlib: is\_relative\_to() and relative\_to(): passing additional arguments is deprecated.

• pkgutil: find\_loader() and get\_loader() now raise DeprecationWarning; use importlib. util.find\_spec() instead. (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850).)

• pty:

– master\_open(): use pty.openpty().

– slave\_open(): use pty.openpty().

• sqlite3:

– version and version\_info.

– execute() and executemany() if named placeholders are used and parameters is a sequence instead of a dict.

• typing: ByteString, deprecated since Python 3.9, now causes a DeprecationWarning to be emitted when it is used.

• urllib: urllib.parse.Quoter is deprecated: it was not intended to be a public API. (Contributed by Gregory P. Smith in [gh-88168](https://github.com/python/cpython/issues/88168).)

## 10.3 Pending Removal in Python 3.15

• http.server.CGIHTTPRequestHandler will be removed along with its related --cgi flag to python -m http.server. It was obsolete and rarely used. No direct replacement exists. Anything is better than CGI to interface a web server with a request handler.

• locale: locale.getdefaultlocale() was deprecated in Python 3.11 and originally planned for removal in Python 3.13 ([gh-90817](https://github.com/python/cpython/issues/90817)), but removal has been postponed to Python 3.15. Use locale.setlocale(), locale.getencoding() and locale.getlocale() instead. (Contributed by Hugo van Kemenade in [gh-111187](https://github.com/python/cpython/issues/111187).)

• pathlib: pathlib.PurePath.is\_reserved() is deprecated and scheduled for removal in Python 3.15. From Python 3.13 onwards, use os.path.isreserved to detect reserved paths on Windows.

• platform: java\_ver() is deprecated and will be removed in 3.15. It was largely untested, had a confusing API, and was only useful for Jython support. (Contributed by Nikita Sobolev in [gh-116349](https://github.com/python/cpython/issues/116349).)

• threading: Passing any arguments to threading.RLock() is now deprecated. C version allows any numbers of args and kwargs, but they are just ignored. Python version does not allow any arguments. All arguments will be removed from threading.RLock() in Python 3.15. (Contributed by Nikita Sobolev in [gh-102029](https://github.com/python/cpython/issues/102029).)

• typing.NamedTuple:

– The undocumented keyword argument syntax for creating NamedTuple classes (NT = NamedTuple("NT", x=int)) is deprecated, and will be disallowed in 3.15. Use the class-based syntax or the functional syntax instead.

• types:

– types.CodeType: Accessing co\_lnotab was deprecated in [**PEP 626**](https://peps.python.org/pep-0626/) since 3.10 and was planned to be removed in 3.12, but it only got a proper DeprecationWarning in 3.12. May be removed in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)

• typing:

When using the functional syntax to create a NamedTuple class, failing to pass a value to the fields parameter (NT = NamedTuple("NT")) is deprecated. Passing None to the fields parameter (NT = NamedTuple("NT", None)) is also deprecated. Both will be disallowed in Python 3.15. To create a NamedTuple class with 0 fields, use class NT(NamedTuple): pass or NT = NamedTuple("NT", []).

typing.TypedDict: When using the functional syntax to create a TypedDict class, failing to pass a value to the fields parameter (TD = TypedDict("TD")) is deprecated. Passing None to the fields parameter (TD = TypedDict("TD", None)) is also deprecated. Both will be disallowed in Python 3.15. To create a TypedDict class with 0 fields, use class TD(TypedDict): pass or TD = TypedDict("TD", {}).

• wave: Deprecate the getmark(), setmark() and getmarkers() methods of the wave.Wave\_read and wave.Wave\_write classes. They will be removed in Python 3.15. (Contributed by Victor Stinner in [gh-105096](https://github.com/python/cpython/issues/105096).)

## 10.4 Pending Removal in Python 3.16

• The import system:

– Setting \_\_loader\_\_ on a module while failing to set \_\_spec\_\_.loader is deprecated. In Python 3.16, \_loader\_\_ will cease to be set or taken into consideration by the import system or the standard library.

• array: array.array 'u' type (wchar\_t): use the 'w' type instead (Py\_UCS4).

• builtins: \~bool, bitwise inversion on bool.

• symtable: Deprecate symtable.Class.get\_methods() due to the lack of interest. (Contributed by Bénédikt Tran in [gh-119698](https://github.com/python/cpython/issues/119698).)

## 10.5 Pending Removal in Future Versions

The following APIs will be removed in the future, although there is currently no date scheduled for their removal.

• argparse: Nesting argument groups and nesting mutually exclusive groups are deprecated.

• array’s 'u' format code ([gh-57281](https://github.com/python/cpython/issues/57281))

• builtins:

– bool(NotImplemented).

– Generators: throw(type, exc, tb) and athrow(type, exc, tb) signature is deprecated: use throw(exc) and athrow(exc) instead, the single argument signature.

– Currently Python accepts numeric literals immediately followed by keywords, for example 0in x, 1or x, 0if 1else 2. It allows confusing and ambiguous expressions like [0x1for x in y] (which can be interpreted as [0x1 for x in y] or [0x1f or x in y]). A syntax warning is raised if the numeric literal is immediately followed by one of keywords and, else, for, if, in, is and or. In a future release it will be changed to a syntax error. ([gh-87999](https://github.com/python/cpython/issues/87999))

– Support for \_\_index\_\_() and \_\_int\_\_() method returning non-int type: these methods will be required to return an instance of a strict subclass of int.

– Support for \_\_float\_\_() method returning a strict subclass of float: these methods will be required to return an instance of float.

– Support for \_\_complex\_\_() method returning a strict subclass of complex: these methods will be required to return an instance of complex.

– Delegation of int() to \_\_trunc\_\_() method.

– Passing a complex number as the real or imag argument in the complex() constructor is now deprecated; it should only be passed as a single positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218).)

• calendar: calendar.January and calendar.February constants are deprecated and replaced by calendar.JANUARY and calendar.FEBRUARY. (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

• codeobject.co\_lnotab: use the codeobject.co\_lines() method instead.

• datetime:

– utcnow(): use datetime.datetime.now(tz=datetime.UTC).

– utcfromtimestamp(): use datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC).

• gettext: Plural value must be an integer.

• importlib:

– load\_module() method: use exec\_module() instead.

– cache\_from\_source() debug\_override parameter is deprecated: use the optimization parameter instead.

• importlib.metadata:

– EntryPoints tuple interface.

– Implicit None on return values.

• mailbox: Use of StringIO input and text mode is deprecated, use BytesIO and binary mode instead.

• os: Calling os.register\_at\_fork() in multi-threaded process.

• pydoc.ErrorDuringImport: A tuple value for exc\_info parameter is deprecated, use an exception instance.

re: More strict rules are now applied for numerical group references and group names in regular expressions. Only sequence of ASCII digits is now accepted as a numerical reference. The group name in bytes patterns and replacement strings can now only contain ASCII letters and digits and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

• sre\_compile, sre\_constants and sre\_parse modules.

• shutil: rmtree()’s onerror parameter is deprecated in Python 3.12; use the onexc parameter instead.

• ssl options and protocols:

– ssl.SSLContext without protocol argument is deprecated.

– ssl.SSLContext: set\_npn\_protocols() and selected\_npn\_protocol() are deprecated: use ALPN instead.

– ssl.OP\_NO\_SSL\* options

– ssl.OP\_NO\_TLS\* options

– ssl.PROTOCOL\_SSLv3

– ssl.PROTOCOL\_TLS

– ssl.PROTOCOL\_TLSv1

– ssl.PROTOCOL\_TLSv1\_1

```yaml
- ssl.PROTOCOL_TLSv1_2
- ssl.TLSVersion.SSLv3
- ssl.TLSVersion.TLSv1
- ssl.TLSVersion.TLSv1_1
```

• sysconfig.is\_python\_build() check\_home parameter is deprecated and ignored.

• threading methods:

```txt
- threading.Condition.notifyAll(): use notify_all().
txt
- threading.Event.isSet(): use is_set().
```

– threading.Thread.isDaemon(), threading.Thread.setDaemon(): use threading. Thread.daemon attribute.

– threading.Thread.getName(), threading.Thread.setName(): use threading.Thread. name attribute.

– threading.currentThread(): use threading.current\_thread().

– threading.activeCount(): use threading.active\_count().

• typing.Text ([gh-92332](https://github.com/python/cpython/issues/92332)).

• unittest.IsolatedAsyncioTestCase: it is deprecated to return a value that is not None from a test case.

• urllib.parse deprecated functions: urlparse() instead

```txt
- splitattr()
- splithost()
- splitnport()
- splitpasswd()
- splitport()
- splitquery()
- splittag()
- splittype()
- splituser()
- splitvalue()
- to_bytes()
```

• urllib.request: URLopener and FancyURLopener style of invoking requests is deprecated. Use newer urlopen() functions and methods.

• wsgiref: SimpleHandler.stdout.write() should not do partial writes.

• xml.etree.ElementTree: Testing the truth value of an Element is deprecated. In a future release it will always return True. Prefer explicit len(elem) or elem is not None tests instead.

• zipimport.zipimporter.load\_module() is deprecated: use exec\_module() instead.

## 11 Removed

## 11.1 asynchat and asyncore

• These two modules have been removed according to the schedule in [**PEP 594**](https://peps.python.org/pep-0594/), having been deprecated in Python 3.6. Use asyncio instead. (Contributed by Nikita Sobolev in [gh-96580](https://github.com/python/cpython/issues/96580).)

## 11.2 configparser

• Several names deprecated in the configparser way back in 3.2 have been removed per [gh-89336](https://github.com/python/cpython/issues/89336):

– configparser.ParsingError no longer has a filename attribute or argument. Use the source attribute and argument instead.

– configparser no longer has a SafeConfigParser class. Use the shorter ConfigParser name instead.

– configparser.ConfigParser no longer has a readfp method. Use read\_file() instead.

## 11.3 distutils

• Remove the distutils package. It was deprecated in Python 3.10 by [**PEP 632**](https://peps.python.org/pep-0632/) “Deprecate distutils module”. For projects still using distutils and cannot be updated to something else, the setuptools project can be installed: it still provides distutils. (Contributed by Victor Stinner in [gh-92584](https://github.com/python/cpython/issues/92584).)

## 11.4 ensurepip

• Remove the bundled setuptools wheel from ensurepip, and stop installing setuptools in environments created by venv.

pip (>= 22.1) does not require setuptools to be installed in the environment. setuptools-based (and distutils-based) packages can still be used with pip install, since pip will provide setuptools in the build environment it uses for building a package.

easy\_install, pkg\_resources, setuptools and distutils are no longer provided by default in environments created with venv or bootstrapped with ensurepip, since they are part of the setuptools package. For projects relying on these at runtime, the setuptools project should be declared as a dependency and installed separately (typically, using pip).

(Contributed by Pradyun Gedam in [gh-95299](https://github.com/python/cpython/issues/95299).)

## 11.5 enum

• Remove enum’s EnumMeta.\_\_getattr\_\_, which is no longer needed for enum attribute access. (Contributed by Ethan Furman in [gh-95083](https://github.com/python/cpython/issues/95083).)

## 11.6 ftplib

• Remove ftplib’s FTP\_TLS.ssl\_version class attribute: use the context parameter instead. (Contributed by Victor Stinner in [gh-94172](https://github.com/python/cpython/issues/94172).)

## 11.7 gzip

• Remove the filename attribute of gzip’s gzip.GzipFile, deprecated since Python 2.6, use the name attribute instead. In write mode, the filename attribute added '.gz' file extension if it was not present. (Contributed by Victor Stinner in [gh-94196](https://github.com/python/cpython/issues/94196).)

## 11.8 hashlib

• Remove the pure Python implementation of hashlib’s hashlib.pbkdf2\_hmac(), deprecated in Python 3.10. Python 3.10 and newer requires OpenSSL 1.1.1 ([**PEP 644**](https://peps.python.org/pep-0644/)): this OpenSSL version provides a C implementation of pbkdf2\_hmac() which is faster. (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

## 11.9 importlib

• Many previously deprecated cleanups in importlib have now been completed:

– References to, and support for module\_repr() has been removed. (Contributed by Barry Warsaw in [gh-97850](https://github.com/python/cpython/issues/97850).)

– importlib.util.set\_package, importlib.util.set\_loader and importlib.util. module\_for\_loader have all been removed. (Contributed by Brett Cannon and Nikita Sobolev in [gh-65961](https://github.com/python/cpython/issues/65961) and [gh-97850](https://github.com/python/cpython/issues/97850).)

– Support for find\_loader() and find\_module() APIs have been removed. (Contributed by Barry Warsaw in [gh-98040](https://github.com/python/cpython/issues/98040).)

– importlib.abc.Finder, pkgutil.ImpImporter, and pkgutil.ImpLoader have been removed. (Contributed by Barry Warsaw in [gh-98040](https://github.com/python/cpython/issues/98040).)

## 11.10 imp

• The imp module has been removed. (Contributed by Barry Warsaw in [gh-98040](https://github.com/python/cpython/issues/98040).)

To migrate, consult the following correspondence table:

```python
imp                  importlib
imp.              Insert None into sys.path_importer_cache
NullImporter
imp.              importlib.util.cache_from_source()
cache_from_s
imp.              importlib.util.find_spec()
find_module(
imp.              importlib.util.MAGIC_NUMBER
get_magic()
imp.              importlib.machinery.SOURCE_SUFFIXES,          importlib.
get_suffixes machinery.EXTENSION_SUFFIXES, and  importlib.machinery.
                          BYTECODE_SUFFIXES
imp.              sys.implementation.cache_tag
get_tag()
imp.              importlib.import_module()
load_module(
imp.              types.ModuleType(name)
new_module(n
imp.              importlib.reload()
reload()
imp.              importlib.util.source_from_cache()
source_from_
imp.              See below
load_source(
```

Replace imp.load\_source() with:

```python
import importlib.util
import importlib.machinery

def load_source(modname, filename):
    loader = importlib.machinery.SourceFileLoader(modname, filename)
    spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
    module = importlib.util.module_from_spec(spec)
    # The module is always executed and not cached in sys.modules.
    # Uncomment the following line to cache the module.
    # sys.modules[module.__name__] = module
    loader.exec_module(module)
    return module
```

• Remove imp functions and attributes with no replacements:

– Undocumented functions:

∗ imp.init\_builtin()

∗ imp.load\_compiled()

∗ imp.load\_dynamic()

∗ imp.load\_package()

– imp.lock\_held(), imp.acquire\_lock(), imp.release\_lock(): the locking scheme has changed in Python 3.3 to per-module locks.

– imp.find\_module() constants: SEARCH\_ERROR, PY\_SOURCE, PY\_COMPILED, C\_EXTENSION, PY\_RESOURCE, PKG\_DIRECTORY, C\_BUILTIN, PY\_FROZEN, PY\_CODERESOURCE, IMP\_HOOK.

## 11.11 io

• Remove io’s io.OpenWrapper and \_pyio.OpenWrapper, deprecated in Python 3.10: just use open() instead. The open() (io.open()) function is a built-in function. Since Python 3.10, \_pyio.open() is also a static method. (Contributed by Victor Stinner in [gh-94169](https://github.com/python/cpython/issues/94169).)

## 11.12 locale

• Remove locale’s locale.format() function, deprecated in Python 3.7: use locale.format\_string() instead. (Contributed by Victor Stinner in [gh-94226](https://github.com/python/cpython/issues/94226).)

## 11.13 smtpd

• The smtpd module has been removed according to the schedule in [**PEP 594**](https://peps.python.org/pep-0594/), having been deprecated in Python 3.4.7 and 3.5.4. Use the [aiosmtpd](https://pypi.org/project/aiosmtpd/) PyPI module or any other asyncio-based server instead. (Contributed by Oleg Iarygin in [gh-93243](https://github.com/python/cpython/issues/93243).)

## 11.14 sqlite3

• The following undocumented sqlite3 features, deprecated in Python 3.10, are now removed:

– sqlite3.enable\_shared\_cache()

– sqlite3.OptimizedUnicode

If a shared cache must be used, open the database in URI mode using the cache=shared query parameter.

The sqlite3.OptimizedUnicode text factory has been an alias for str since Python 3.3. Code that pre-viously set the text factory to OptimizedUnicode can either use str explicitly, or rely on the default value which is also str.

(Contributed by Erlend E. Aasland in [gh-92548](https://github.com/python/cpython/issues/92548).)

## 11.15 ssl

• Remove ssl’s ssl.RAND\_pseudo\_bytes() function, deprecated in Python 3.6: use os.urandom() or ssl.RAND\_bytes() instead. (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

• Remove the ssl.match\_hostname() function. It was deprecated in Python 3.7. OpenSSL performs hostname matching since Python 3.7, Python no longer uses the ssl.match\_hostname() function. (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

• Remove the ssl.wrap\_socket() function, deprecated in Python 3.7: instead, create a ssl.SSLContext object and call its ssl.SSLContext.wrap\_socket method. Any package that still uses ssl. wrap\_socket() is broken and insecure. The function neither sends a SNI TLS extension nor validates the server hostname. Code is subject to [**CWE 295**](https://cwe.mitre.org/data/definitions/295.html) (Improper Certificate Validation). (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

## 11.16 unittest

• Remove many long-deprecated unittest features:

– A number of TestCase method aliases:

| Deprecated alias | Method Name | Deprecated in |
| --- | --- | --- |
| failUnless | assertTrue() | 3.1 |
| failIf | assertFalse() | 3.1 |
| failUnlessEqual | assertEqual() | 3.1 |
| failIfEqual | assertNotEqual() | 3.1 |
| failUnlessAlmostEqual | assertAlmostEqual() | 3.1 |
| failIfAlmostEqual | assertNotAlmostEqual() | 3.1 |
| failUnlessRaises | assertRaises() | 3.1 |
| assert_ | assertTrue() | 3.2 |
| assertEquals | assertEqual() | 3.2 |
| assertNotEquals | assertNotEqual() | 3.2 |
| assertAlmostEquals | assertAlmostEqual() | 3.2 |
| assertNotAlmostEquals | assertNotAlmostEqual() | 3.2 |
| assertRegexpMatches | assertRegex() | 3.2 |
| assertRaisesRegexp | assertRaisesRegex() | 3.2 |
| assertNotRegexpMatches | assertNotRegex() | 3.5 |

You can use [https://github.com/isidentical/teyit](https://github.com/isidentical/teyit) to automatically modernise your unit tests.

– Undocumented and broken TestCase method assertDictContainsSubset (deprecated in Python 3.2).

– Undocumented TestLoader.loadTestsFromModule parameter use\_load\_tests (deprecated and ignored since Python 3.5).

– An alias of the TextTestResult class: \_TextTestResult (deprecated in Python 3.2).

(Contributed by Serhiy Storchaka in [gh-89325](https://github.com/python/cpython/issues/89325).)

## 11.17 webbrowser

• Remove support for obsolete browsers from webbrowser. The removed browsers include: Grail, Mosaic, Netscape, Galeon, Skipstone, Iceape, Firebird, and Firefox versions 35 and below ([gh-102871](https://github.com/python/cpython/issues/102871)).

## 11.18 xml.etree.ElementTree

• Remove the ElementTree.Element.copy() method of the pure Python implementation, deprecated in Python 3.10, use the copy.copy() function instead. The C implementation of xml.etree.ElementTree has no copy() method, only a \_\_copy\_\_() method. (Contributed by Victor Stinner in [gh-94383](https://github.com/python/cpython/issues/94383).)

## 11.19 zipimport

• Remove zipimport’s find\_loader() and find\_module() methods, deprecated in Python 3.10: use the find\_spec() method instead. See [**PEP 451**](https://peps.python.org/pep-0451/) for the rationale. (Contributed by Victor Stinner in [gh-94379](https://github.com/python/cpython/issues/94379).)

## 11.20 Others

• Remove the suspicious rule from the documentation Makefile and Doc/tools/rstlint.py, both in favor of [sphinx-lint](https://github.com/sphinx-contrib/sphinx-lint). (Contributed by Julien Palard in [gh-98179](https://github.com/python/cpython/issues/98179).)

• Remove the keyfile and certfile parameters from the ftplib, imaplib, poplib and smtplib modules, and the key\_file, cert\_file and check\_hostname parameters from the http.client module, all deprecated since Python 3.6. Use the context parameter (ssl\_context in imaplib) instead. (Contributed by Victor Stinner in [gh-94172](https://github.com/python/cpython/issues/94172).)

• Remove Jython compatibility hacks from several stdlib modules and tests. (Contributed by Nikita Sobolev in [gh-99482](https://github.com/python/cpython/issues/99482).)

• Remove \_use\_broken\_old\_ctypes\_structure\_semantics\_ flag from ctypes module. (Contributed by Nikita Sobolev in [gh-99285](https://github.com/python/cpython/issues/99285).)

## 12 Porting to Python 3.12

This section lists previously described changes and other bugfixes that may require changes to your code.

## 12.1 Changes in the Python API

• More strict rules are now applied for numerical group references and group names in regular expressions. Only sequence of ASCII digits is now accepted as a numerical reference. The group name in bytes patterns and replacement strings can now only contain ASCII letters and digits and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

• Remove randrange() functionality deprecated since Python 3.10. Formerly, randrange(10.0) losslessly converted to randrange(10). Now, it raises a TypeError. Also, the exception raised for non-integer values such as randrange(10.5) or randrange('10') has been changed from ValueError to Type-Error. This also prevents bugs where randrange(1e25) would silently select from a larger range than randrange(10\*\*25). (Originally suggested by Serhiy Storchaka [gh-86388](https://github.com/python/cpython/issues/86388).)

argparse.ArgumentParser changed encoding and error handler for reading arguments from file (e.g. fromfile\_prefix\_chars option) from default text encoding (e.g. locale. getpreferredencoding(False)) to filesystem encoding and error handler. Argument files should be encoded in UTF-8 instead of ANSI Codepage on Windows.

• Remove the asyncore-based smtpd module deprecated in Python 3.4.7 and 3.5.4. A recommended replacement is the asyncio-based [aiosmtpd](https://pypi.org/project/aiosmtpd/) PyPI module.

• shlex.split(): Passing None for s argument now raises an exception, rather than reading sys.stdin. The feature was deprecated in Python 3.9. (Contributed by Victor Stinner in [gh-94352](https://github.com/python/cpython/issues/94352).)

• The os module no longer accepts bytes-like paths, like bytearray and memoryview types: only the exact bytes type is accepted for bytes strings. (Contributed by Victor Stinner in [gh-98393](https://github.com/python/cpython/issues/98393).)

• syslog.openlog() and syslog.closelog() now fail if used in subinterpreters. syslog.syslog() may still be used in subinterpreters, but now only if syslog.openlog() has already been called in the main interpreter. These new restrictions do not apply to the main interpreter, so only a very small set of users might be affected. This change helps with interpreter isolation. Furthermore, syslog is a wrapper around process-global resources, which are best managed from the main interpreter. (Contributed by Donghee Na in [gh-99127](https://github.com/python/cpython/issues/99127).)

• The undocumented locking behavior of cached\_property() is removed, because it locked across all instances of the class, leading to high lock contention. This means that a cached property getter function could now run more than once for a single instance, if two threads race. For most simple cached properties (e.g. those that are idempotent and simply calculate a value based on other attributes of the instance) this will be fine. If synchronization is needed, implement locking within the cached property getter function or around multi-threaded access points.

• sys.\_current\_exceptions() now returns a mapping from thread-id to an exception instance, rather than to a (typ, exc, tb) tuple. (Contributed by Irit Katriel in [gh-103176](https://github.com/python/cpython/issues/103176).)

• When extracting tar files using tarfile or shutil.unpack\_archive(), pass the filter argument to limit features that may be surprising or dangerous. See tarfile-extraction-filter for details.

• The output of the tokenize.tokenize() and tokenize.generate\_tokens() functions is now changed due to the changes introduced in [**PEP 701**](https://peps.python.org/pep-0701/). This means that STRING tokens are not emitted any more for fstrings and the tokens described in [**PEP 701**](https://peps.python.org/pep-0701/) are now produced instead: FSTRING\_START, FSTRING\_MIDDLE and FSTRING\_END are now emitted for f-string “string” parts in addition to the appropriate tokens for the tokenization in the expression components. For example for the f-string f"start {1+1} end" the old version of the tokenizer emitted:

| 1,0-1,2: | FSTRING_START | 'f'' |
| --- | --- | --- |
| 1,2-1,8: | FSTRING_MIDDLE | 'start ' |
| 1,8-1,9: | OP | '{' |
| 1,9-1,10: | NUMBER | '1' |
| 1,10-1,11: | OP | '+' |
| 1,11-1,12: | NUMBER | '1' |
| 1,12-1,13: | OP | '}' |
| 1,13-1,17: | FSTRING_MIDDLE | ' end' |
| 1,17-1,18: | FSTRING_END | ''' |

| 1,0-1,18: | STRING | 'f"start {1+1} end"' |
| --- | --- | --- |

while the new version emits:

Additionally, there may be some minor behavioral changes as a consequence of the changes required to support [**PEP 701**](https://peps.python.org/pep-0701/). Some of these changes include:

– The type attribute of the tokens emitted when tokenizing some invalid Python characters such as ! has changed from ERRORTOKEN to OP.

– Incomplete single-line strings now also raise tokenize.TokenError as incomplete multiline strings do.

– Some incomplete or invalid Python code now raises tokenize.TokenError instead of returning arbitrary ERRORTOKEN tokens when tokenizing it.

– Mixing tabs and spaces as indentation in the same file is not supported anymore and will raise a TabError.

• The threading module now expects the \_thread module to have an \_is\_main\_interpreter attribute. It is a function with no arguments that returns True if the current interpreter is the main interpreter.

Any library or application that provides a custom \_thread module should provide \_is\_main\_interpreter(). (See [gh-112826](https://github.com/python/cpython/issues/112826).)

## 13 Build Changes

• Python no longer uses setup.py to build shared C extension modules. Build parameters like headers and libraries are detected in configure script. Extensions are built by Makefile. Most extensions use pkg-config and fall back to manual detection. (Contributed by Christian Heimes in [gh-93939](https://github.com/python/cpython/issues/93939).)

• va\_start() with two parameters, like va\_start(args, format), is now required to build Python. va\_start() is no longer called with a single parameter. (Contributed by Kumar Aditya in [gh-93207](https://github.com/python/cpython/issues/93207).)

• CPython now uses the ThinLTO option as the default link time optimization policy if the Clang compiler accepts the flag. (Contributed by Donghee Na in [gh-89536](https://github.com/python/cpython/issues/89536).)

• Add COMPILEALL\_OPTS variable in Makefile to override compileall options (default: -j0) in make install. Also merged the 3 compileall commands into a single command to build .pyc files for all optimization levels (0, 1, 2) at once. (Contributed by Victor Stinner in [gh-99289](https://github.com/python/cpython/issues/99289).)

• Add platform triplets for 64-bit LoongArch:

– loongarch64-linux-gnusf

– loongarch64-linux-gnuf32

– loongarch64-linux-gnu

(Contributed by Zhang Na in [gh-90656](https://github.com/python/cpython/issues/90656).)

• PYTHON\_FOR\_REGEN now require Python 3.10 or newer.

• Autoconf 2.71 and aclocal 1.16.4 is now required to regenerate !configure. (Contributed by Christian Heimes in [gh-89886](https://github.com/python/cpython/issues/89886).)

• Windows builds and macOS installers from python.org now use OpenSSL 3.0.

## 14 C API Changes

## 14.1 New Features

• [**PEP 697**](https://peps.python.org/pep-0697/): Introduce the Unstable C API tier, intended for low-level tools like debuggers and JIT compilers. This API may change in each minor release of CPython without deprecation warnings. Its contents are marked by the PyUnstable\_ prefix in names.

Code object constructors:

– PyUnstable\_Code\_New() (renamed from PyCode\_New)

– PyUnstable\_Code\_NewWithPosOnlyArgs() (renamed from PyCode\_NewWithPosOnlyArgs)

Extra storage for code objects ([**PEP 523**](https://peps.python.org/pep-0523/)):

– PyUnstable\_Eval\_RequestCodeExtraIndex() (renamed from \_PyEval\_RequestCodeExtraIndex)

– PyUnstable\_Code\_GetExtra() (renamed from \_PyCode\_GetExtra)

– PyUnstable\_Code\_SetExtra() (renamed from \_PyCode\_SetExtra)

The original names will continue to be available until the respective API changes.

(Contributed by Petr Viktorin in [gh-101101](https://github.com/python/cpython/issues/101101).)

• [**PEP 697**](https://peps.python.org/pep-0697/): Add an API for extending types whose instance memory layout is opaque:

– PyType\_Spec.basicsize can be zero or negative to specify inheriting or extending the base class size.

– PyObject\_GetTypeData() and PyType\_GetTypeDataSize() added to allow access to subclassspecific instance data.

– Py\_TPFLAGS\_ITEMS\_AT\_END and PyObject\_GetItemData() added to allow safely extending certain variable-sized types, including PyType\_Type.

– Py\_RELATIVE\_OFFSET added to allow defining members in terms of a subclass-specific struct.

(Contributed by Petr Viktorin in [gh-103509](https://github.com/python/cpython/issues/103509).)

• Add the new limited C API function PyType\_FromMetaclass(), which generalizes the existing Py-Type\_FromModuleAndSpec() using an additional metaclass argument. (Contributed by Wenzel Jakob in [gh-93012](https://github.com/python/cpython/issues/93012).)

• API for creating objects that can be called using the vectorcall protocol was added to the Limited API:

```txt
- Py_TPFLAGS_HAVE_VECTORCALL
```

– PyVectorcall\_NARGS()

– PyVectorcall\_Call()

– vectorcallfunc

The Py\_TPFLAGS\_HAVE\_VECTORCALL flag is now removed from a class when the class’s \_\_call\_\_() method is reassigned. This makes vectorcall safe to use with mutable types (i.e. heap types without the immutable flag, Py\_TPFLAGS\_IMMUTABLETYPE). Mutable types that do not override tp\_call now inherit the Py\_TPFLAGS\_HAVE\_VECTORCALL flag. (Contributed by Petr Viktorin in [gh-93274](https://github.com/python/cpython/issues/93274).)

The Py\_TPFLAGS\_MANAGED\_DICT and Py\_TPFLAGS\_MANAGED\_WEAKREF flags have been added. This allows extensions classes to support object \_\_dict\_\_ and weakrefs with less bookkeeping, using less memory and with faster access.

• API for performing calls using the vectorcall protocol was added to the Limited API:

– PyObject\_Vectorcall()

– PyObject\_VectorcallMethod()

– PY\_VECTORCALL\_ARGUMENTS\_OFFSET

This means that both the incoming and outgoing ends of the vector call protocol are now available in the Limited API. (Contributed by Wenzel Jakob in [gh-98586](https://github.com/python/cpython/issues/98586).)

• Add two new public functions, PyEval\_SetProfileAllThreads() and PyEval\_SetTraceAllThreads(), that allow to set tracing and profiling functions in all running threads in addition to the calling one. (Contributed by Pablo Galindo in [gh-93503](https://github.com/python/cpython/issues/93503).)

• Add new function PyFunction\_SetVectorcall() to the C API which sets the vectorcall field of a given PyFunctionObject. (Contributed by Andrew Frost in [gh-92257](https://github.com/python/cpython/issues/92257).)

• The C API now permits registering callbacks via PyDict\_AddWatcher(), PyDict\_Watch() and related APIs to be called whenever a dictionary is modified. This is intended for use by optimizing interpreters, JIT compilers, or debuggers. (Contributed by Carl Meyer in [gh-91052](https://github.com/python/cpython/issues/91052).)

• Add PyType\_AddWatcher() and PyType\_Watch() API to register callbacks to receive notification on changes to a type. (Contributed by Carl Meyer in [gh-91051](https://github.com/python/cpython/issues/91051).)

• Add PyCode\_AddWatcher() and PyCode\_ClearWatcher() APIs to register callbacks to receive notification on creation and destruction of code objects. (Contributed by Itamar Oren in [gh-91054](https://github.com/python/cpython/issues/91054).)

• Add PyFrame\_GetVar() and PyFrame\_GetVarString() functions to get a frame variable by its name. (Contributed by Victor Stinner in [gh-91248](https://github.com/python/cpython/issues/91248).)

• Add PyErr\_GetRaisedException() and PyErr\_SetRaisedException() for saving and restoring the current exception. These functions return and accept a single exception object, rather than the triple arguments of the now-deprecated PyErr\_Fetch() and PyErr\_Restore(). This is less error prone and a bit more efficient. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

• Add \_PyErr\_ChainExceptions1, which takes an exception instance, to replace the legacy-API \_Py-Err\_ChainExceptions, which is now deprecated. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

• Add PyException\_GetArgs() and PyException\_SetArgs() as convenience functions for retrieving and modifying the args passed to the exception’s constructor. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

• Add PyErr\_DisplayException(), which takes an exception instance, to replace the legacy-api Py-Err\_Display(). (Contributed by Irit Katriel in [gh-102755](https://github.com/python/cpython/issues/102755)).

• [**PEP 683**](https://peps.python.org/pep-0683/): Introduce Immortal Objects, which allows objects to bypass reference counts, and related changes to the C-API:

**– \_Py\_IMMORTAL\_REFCNT: The reference count that defines an object** as immortal.

– \_Py\_IsImmortal Checks if an object has the immortal reference count.

**– PyObject\_HEAD\_INIT This will now initialize reference count to** \_Py\_IMMORTAL\_REFCNT when used with Py\_BUILD\_CORE.

**– SSTATE\_INTERNED\_IMMORTAL An identifier for interned unicode objects** that are immortal.

**– SSTATE\_INTERNED\_IMMORTAL\_STATIC An identifier for interned unicode** objects that are immortal and static

**– sys.getunicodeinternedsize This returns the total number of unicode** objects that have been interned. This is now needed for refleak.py to correctly track reference counts and allocated blocks

(Contributed by Eddie Elizondo in [gh-84436](https://github.com/python/cpython/issues/84436).)

• [**PEP 684**](https://peps.python.org/pep-0684/): Add the new Py\_NewInterpreterFromConfig() function and PyInterpreterConfig, which may be used to create sub-interpreters with their own GILs. (See PEP 684: A Per-Interpreter GIL for more info.) (Contributed by Eric Snow in [gh-104110](https://github.com/python/cpython/issues/104110).)

• In the limited C API version 3.12, Py\_INCREF() and Py\_DECREF() functions are now implemented as opaque function calls to hide implementation details. (Contributed by Victor Stinner in [gh-105387](https://github.com/python/cpython/issues/105387).)

## 14.2 Porting to Python 3.12

• Legacy Unicode APIs based on Py\_UNICODE\* representation has been removed. Please migrate to APIs based on UTF-8 or wchar\_t\*.

• Argument parsing functions like PyArg\_ParseTuple() doesn’t support Py\_UNICODE\* based format (e.g. u, Z) anymore. Please migrate to other formats for Unicode like s, z, es, and U.

tp\_weaklist for all static builtin types is always NULL. This is an internal-only field on PyTypeObject but we’re pointing out the change in case someone happens to be accessing the field directly anyway. To avoid breakage, consider using the existing public C-API instead, or, if necessary, the (internal-only) \_PyObject\_GET\_WEAKREFS\_LISTPTR() macro.

• This internal-only PyTypeObject.tp\_subclasses may now not be a valid object pointer. Its type was changed to void\* to reflect this. We mention this in case someone happens to be accessing the internal-only field directly.

To get a list of subclasses, call the Python method \_\_subclasses\_\_() (using PyObject\_CallMethod(), for example).

• Add support of more formatting options (left aligning, octals, uppercase hexadecimals, intmax\_t, ptrdiff\_t, wchar\_t C strings, variable width and precision) in PyUnicode\_FromFormat() and PyUnicode\_FromFormatV(). (Contributed by Serhiy Storchaka in [gh-98836](https://github.com/python/cpython/issues/98836).)

• An unrecognized format character in PyUnicode\_FromFormat() and PyUnicode\_FromFormatV() now sets a SystemError. In previous versions it caused all the rest of the format string to be copied as-is to the result string, and any extra arguments discarded. (Contributed by Serhiy Storchaka in [gh-95781](https://github.com/python/cpython/issues/95781).)

• Fix wrong sign placement in PyUnicode\_FromFormat() and PyUnicode\_FromFormatV(). (Contributed by Philip Georgi in [gh-95504](https://github.com/python/cpython/issues/95504).)

• Extension classes wanting to add a \_\_dict\_\_ or weak reference slot should use Py\_TPFLAGS\_MANAGED\_DICT and Py\_TPFLAGS\_MANAGED\_WEAKREF instead of tp\_dictoffset and tp\_weaklistoffset, respectively. The use of tp\_dictoffset and tp\_weaklistoffset is still supported, but does not fully support multiple inheritance ([gh-95589](https://github.com/python/cpython/issues/95589)), and performance may be worse. Classes declaring Py\_TPFLAGS\_MANAGED\_DICT should call \_PyObject\_VisitManagedDict() and \_PyObject\_ClearManagedDict() to traverse and clear their instance’s dictionaries. To clear weakrefs, call PyObject\_ClearWeakRefs(), as before.

• The PyUnicode\_FSDecoder() function no longer accepts bytes-like paths, like bytearray and memoryview types: only the exact bytes type is accepted for bytes strings. (Contributed by Victor Stinner in [gh-98393](https://github.com/python/cpython/issues/98393).)

• The Py\_CLEAR, Py\_SETREF and Py\_XSETREF macros now only evaluate their arguments once. If an argument has side effects, these side effects are no longer duplicated. (Contributed by Victor Stinner in [gh-98724](https://github.com/python/cpython/issues/98724).)

• The interpreter’s error indicator is now always normalized. This means that PyErr\_SetObject(), Py-Err\_SetString() and the other functions that set the error indicator now normalize the exception before storing it. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

• \_Py\_RefTotal is no longer authoritative and only kept around for ABI compatibility. Note that it is an internal global and only available on debug builds. If you happen to be using it then you’ll need to start using \_Py\_GetGlobalRefTotal().

• The following functions now select an appropriate metaclass for the newly created type:

– PyType\_FromSpec()

– PyType\_FromSpecWithBases()

– PyType\_FromModuleAndSpec()

Creating classes whose metaclass overrides tp\_new is deprecated, and in Python 3.14+ it will be disallowed. Note that these functions ignore tp\_new of the metaclass, possibly allowing incomplete initialization.

Note that PyType\_FromMetaclass() (added in Python 3.12) already disallows creating classes whose metaclass overrides tp\_new (\_\_new\_\_() in Python).

Since tp\_new overrides almost everything PyType\_From\* functions do, the two are incompatible with each other. The existing behavior – ignoring the metaclass for several steps of type creation – is unsafe in general, since (meta)classes assume that tp\_new was called. There is no simple general workaround. One of the following may work for you:

– If you control the metaclass, avoid using tp\_new in it:

∗ If initialization can be skipped, it can be done in tp\_init instead.

∗ If the metaclass doesn’t need to be instantiated from Python, set its tp\_new to NULL using the Py\_TPFLAGS\_DISALLOW\_INSTANTIATION flag. This makes it acceptable for PyType\_From\* functions.

– Avoid PyType\_From\* functions: if you don’t need C-specific features (slots or setting the instance size), create types by calling the metaclass.

– If you know the tp\_new can be skipped safely, filter the deprecation warning out using warnings. catch\_warnings() from Python.

• PyOS\_InputHook and PyOS\_ReadlineFunctionPointer are no longer called in subinterpreters. This is because clients generally rely on process-wide global state (since these callbacks have no way of recovering extension module state).

This also avoids situations where extensions may find themselves running in a subinterpreter that they don’t support (or haven’t yet been loaded in). See [gh-104668](https://github.com/python/cpython/issues/104668) for more info.

PyLongObject has had its internals changed for better performance. Although the internals of PyLongObject are private, they are used by some extension modules. The internal fields should no longer be accessed directly, instead the API functions beginning PyLong\_... should be used instead. Two new unstable API functions are provided for efficient access to the value of PyLongObjects which fit into a single machine word:

– PyUnstable\_Long\_IsCompact()

– PyUnstable\_Long\_CompactValue()

• Custom allocators, set via PyMem\_SetAllocator(), are now required to be thread-safe, regardless of memory domain. Allocators that don’t have their own state, including “hooks”, are not affected. If your custom allocator is not already thread-safe and you need guidance then please create a new GitHub issue and CC @ericsnowcurrently.

## 14.3 Deprecated

• In accordance with [**PEP 699**](https://peps.python.org/pep-0699/), the ma\_version\_tag field in PyDictObject is deprecated for extension modules. Accessing this field will generate a compiler warning at compile time. This field will be removed in Python 3.14. (Contributed by Ramvikrams and Kumar Aditya in [gh-101193](https://github.com/python/cpython/issues/101193). PEP by Ken Jin.)

• Deprecate global configuration variable:

– Py\_DebugFlag: use PyConfig.parser\_debug

– Py\_VerboseFlag: use PyConfig.verbose

– Py\_QuietFlag: use PyConfig.quiet

– Py\_InteractiveFlag: use PyConfig.interactive

– Py\_InspectFlag: use PyConfig.inspect

– Py\_OptimizeFlag: use PyConfig.optimization\_level

– Py\_NoSiteFlag: use PyConfig.site\_import

– Py\_BytesWarningFlag: use PyConfig.bytes\_warning

– Py\_FrozenFlag: use PyConfig.pathconfig\_warnings

– Py\_IgnoreEnvironmentFlag: use PyConfig.use\_environment

– Py\_DontWriteBytecodeFlag: use PyConfig.write\_bytecode

– Py\_NoUserSiteDirectory: use PyConfig.user\_site\_directory

– Py\_UnbufferedStdioFlag: use PyConfig.buffered\_stdio

– Py\_HashRandomizationFlag: use PyConfig.use\_hash\_seed and PyConfig.hash\_seed

– Py\_IsolatedFlag: use PyConfig.isolated

– Py\_LegacyWindowsFSEncodingFlag: use PyPreConfig.legacy\_windows\_fs\_encoding

– Py\_LegacyWindowsStdioFlag: use PyConfig.legacy\_windows\_stdio

– Py\_FileSystemDefaultEncoding: use PyConfig.filesystem\_encoding

– Py\_HasFileSystemDefaultEncoding: use PyConfig.filesystem\_encoding

– Py\_FileSystemDefaultEncodeErrors: use PyConfig.filesystem\_errors

– Py\_UTF8Mode: use PyPreConfig.utf8\_mode (see Py\_PreInitialize())

The Py\_InitializeFromConfig() API should be used with PyConfig instead. (Contributed by Victor Stinner in [gh-77782](https://github.com/python/cpython/issues/77782).)

• Creating immutable types with mutable bases is deprecated and will be disabled in Python 3.14. ([gh-95388](https://github.com/python/cpython/issues/95388))

• The structmember.h header is deprecated, though it continues to be available and there are no plans to remove it.

Its contents are now available just by including Python.h, with a Py prefix added if it was missing:

– PyMemberDef, PyMember\_GetOne() and PyMember\_SetOne()

– Type macros like Py\_T\_INT, Py\_T\_DOUBLE, etc. (previously T\_INT, T\_DOUBLE, etc.)

– The flags Py\_READONLY (previously READONLY) and Py\_AUDIT\_READ (previously all uppercase)

Several items are not exposed from Python.h:

– T\_OBJECT (use Py\_T\_OBJECT\_EX)

– T\_NONE (previously undocumented, and pretty quirky)

– The macro WRITE\_RESTRICTED which does nothing.

– The macros RESTRICTED and READ\_RESTRICTED, equivalents of Py\_AUDIT\_READ.

– In some configurations, &lt;stddef.h&gt; is not included from Python.h. It should be included manually when using offsetof().

The deprecated header continues to provide its original contents under the original names. Your old code can stay unchanged, unless the extra include and non-namespaced macros bother you greatly.

(Contributed in [gh-47146](https://github.com/python/cpython/issues/47146) by Petr Viktorin, based on earlier work by Alexander Belopolsky and Matthias Braun.)

• PyErr\_Fetch() and PyErr\_Restore() are deprecated. Use PyErr\_GetRaisedException() and Py-Err\_SetRaisedException() instead. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

• PyErr\_Display() is deprecated. Use PyErr\_DisplayException() instead. (Contributed by Irit Katriel in [gh-102755](https://github.com/python/cpython/issues/102755)).

• \_PyErr\_ChainExceptions is deprecated. Use \_PyErr\_ChainExceptions1 instead. (Contributed by Irit Katriel in [gh-102192](https://github.com/python/cpython/issues/102192).)

• Using PyType\_FromSpec(), PyType\_FromSpecWithBases() or PyType\_FromModuleAndSpec() to create a class whose metaclass overrides tp\_new is deprecated. Call the metaclass instead.

## Pending Removal in Python 3.14

• The ma\_version\_tag field in PyDictObject for extension modules ([**PEP 699**](https://peps.python.org/pep-0699/); [gh-101193](https://github.com/python/cpython/issues/101193)).

• Creating immutable types with mutable bases ([gh-95388](https://github.com/python/cpython/issues/95388)).

• Functions to configure Python’s initialization, deprecated in Python 3.11:

– PySys\_SetArgvEx(): Set PyConfig.argv instead.

– PySys\_SetArgv(): Set PyConfig.argv instead.

– Py\_SetProgramName(): Set PyConfig.program\_name instead.

– Py\_SetPythonHome(): Set PyConfig.home instead.

The Py\_InitializeFromConfig() API should be used with PyConfig instead.

## • Global configuration variables:

– Py\_DebugFlag: Use PyConfig.parser\_debug instead.

– Py\_VerboseFlag: Use PyConfig.verbose instead.

– Py\_QuietFlag: Use PyConfig.quiet instead.

– Py\_InteractiveFlag: Use PyConfig.interactive instead.

– Py\_InspectFlag: Use PyConfig.inspect instead.

– Py\_OptimizeFlag: Use PyConfig.optimization\_level instead.

– Py\_NoSiteFlag: Use PyConfig.site\_import instead.

– Py\_BytesWarningFlag: Use PyConfig.bytes\_warning instead.

– Py\_FrozenFlag: Use PyConfig.pathconfig\_warnings instead.

– Py\_IgnoreEnvironmentFlag: Use PyConfig.use\_environment instead.

– Py\_DontWriteBytecodeFlag: Use PyConfig.write\_bytecode instead.

– Py\_NoUserSiteDirectory: Use PyConfig.user\_site\_directory instead.

– Py\_UnbufferedStdioFlag: Use PyConfig.buffered\_stdio instead.

– Py\_HashRandomizationFlag: Use PyConfig.use\_hash\_seed and PyConfig.hash\_seed instead.

– Py\_IsolatedFlag: Use PyConfig.isolated instead.

– Py\_LegacyWindowsFSEncodingFlag: Use PyPreConfig.legacy\_windows\_fs\_encoding instead.

– Py\_LegacyWindowsStdioFlag: Use PyConfig.legacy\_windows\_stdio instead.

– Py\_FileSystemDefaultEncoding: Use PyConfig.filesystem\_encoding instead.

– Py\_HasFileSystemDefaultEncoding: Use PyConfig.filesystem\_encoding instead.

– Py\_FileSystemDefaultEncodeErrors: Use PyConfig.filesystem\_errors instead.

– Py\_UTF8Mode: Use PyPreConfig.utf8\_mode instead. (see Py\_PreInitialize())

The Py\_InitializeFromConfig() API should be used with PyConfig instead.

## Pending Removal in Python 3.15

• The bundled copy of libmpdecimal.

• The PyImport\_ImportModuleNoBlock(): Use PyImport\_ImportModule() instead.

• PyWeakref\_GetObject() and PyWeakref\_GET\_OBJECT(): Use PyWeakref\_GetRef() instead.

• Py\_UNICODE type and the Py\_UNICODE\_WIDE macro: Use wchar\_t instead.

• Python initialization functions:

– PySys\_ResetWarnOptions(): Clear sys.warnoptions and warnings.filters instead.

– Py\_GetExecPrefix(): Get sys.exec\_prefix instead.

– Py\_GetPath(): Get sys.path instead.

– Py\_GetPrefix(): Get sys.prefix instead.

– Py\_GetProgramFullPath(): Get sys.executable instead.

– Py\_GetProgramName(): Get sys.executable instead.

– Py\_GetPythonHome(): Get PyConfig.home or the PYTHONHOME environment variable instead.

## Pending Removal in Future Versions

The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.

• Py\_TPFLAGS\_HAVE\_FINALIZE: Unneeded since Python 3.8.

• PyErr\_Fetch(): Use PyErr\_GetRaisedException() instead.

• PyErr\_NormalizeException(): Use PyErr\_GetRaisedException() instead.

• PyErr\_Restore(): Use PyErr\_SetRaisedException() instead.

• PyModule\_GetFilename(): Use PyModule\_GetFilenameObject() instead.

• PyOS\_AfterFork(): Use PyOS\_AfterFork\_Child() instead.

• PySlice\_GetIndicesEx(): Use PySlice\_Unpack() and PySlice\_AdjustIndices() instead.

• PyUnicode\_AsDecodedObject(): Use PyCodec\_Decode() instead.

• PyUnicode\_AsDecodedUnicode(): Use PyCodec\_Decode() instead.

• PyUnicode\_AsEncodedObject(): Use PyCodec\_Encode() instead.

• PyUnicode\_AsEncodedUnicode(): Use PyCodec\_Encode() instead.

• PyUnicode\_READY(): Unneeded since Python 3.12

• PyErr\_Display(): Use PyErr\_DisplayException() instead.

• \_PyErr\_ChainExceptions(): Use \_PyErr\_ChainExceptions1() instead.

• PyBytesObject.ob\_shash member: call PyObject\_Hash() instead.

• PyDictObject.ma\_version\_tag member.

• Thread Local Storage (TLS) API:

– PyThread\_create\_key(): Use PyThread\_tss\_alloc() instead.

– PyThread\_delete\_key(): Use PyThread\_tss\_free() instead.

– PyThread\_set\_key\_value(): Use PyThread\_tss\_set() instead.

– PyThread\_get\_key\_value(): Use PyThread\_tss\_get() instead.

– PyThread\_delete\_key\_value(): Use PyThread\_tss\_delete() instead.

– PyThread\_ReInitTLS(): Unneeded since Python 3.7.

## 14.4 Removed

• Remove the token.h header file. There was never any public tokenizer C API. The token.h header file was only designed to be used by Python internals. (Contributed by Victor Stinner in [gh-92651](https://github.com/python/cpython/issues/92651).)

• Legacy Unicode APIs have been removed. See [**PEP 623**](https://peps.python.org/pep-0623/) for detail.

– PyUnicode\_WCHAR\_KIND

\- PyUnicode\_AS\_UNICODE()

\- PyUnicode\_AsUnicode()

– PyUnicode\_AsUnicodeAndSize()

– PyUnicode\_AS\_DATA()

– PyUnicode\_FromUnicode()

– PyUnicode\_GET\_SIZE()

– PyUnicode\_GetSize()

– PyUnicode\_GET\_DATA\_SIZE()

• Remove the PyUnicode\_InternImmortal() function macro. (Contributed by Victor Stinner in [gh-85858](https://github.com/python/cpython/issues/85858).)

## 15 Notable changes in 3.12.4

## 15.1 ipaddress

• Fixed is\_global and is\_private behavior in IPv4Address, IPv6Address, IPv4Network and IPv6Network.

## 16 Notable changes in 3.12.5

## 16.1 email

• Headers with embedded newlines are now quoted on output.

The generator will now refuse to serialize (write) headers that are improperly folded or delimited, such that they would be parsed as multiple headers or joined with adjacent data. If you need to turn this safety feature off, set verify\_generated\_headers. (Contributed by Bas Bloemsaat and Petr Viktorin in [gh-121650](https://github.com/python/cpython/issues/121650).)

## 17 Notable changes in 3.12.6

## 17.1 email

• email.utils.getaddresses() and email.utils.parseaddr() now return ('', '') 2-tuples in more situations where invalid email addresses are encountered, instead of potentially inaccurate values. An optional strict parameter was added to these two functions: use strict=False to get the old behavior, accepting malformed inputs. getattr(email.utils, 'supports\_strict\_parsing', False) can be used to check if the strict paramater is available. (Contributed by Thomas Dwyer and Victor Stinner for [gh-102988](https://github.com/python/cpython/issues/102988) to improve the CVE-2023-27043 fix.)

## 18 Notable changes in 3.12.8

## 18.1 sys

• The previously undocumented special function sys.getobjects(), which only exists in specialized builds of Python, may now return objects from other interpreters than the one it’s called in.

## Index

## C

Common Vulnerabilities and Exposures CVE 2024-4030, 12, 14 Common Weakness Enumeration CWE 295, 27

## E

environment variable PYTHONHOME, 37 PYTHONPERFSUPPORT, 10

## P

Python Enhancement Proposals PEP 249, 13 PEP 451, 28 PEP 484, 4, 8 PEP 523, 31 PEP 554, 6 PEP 572, 9 PEP 594, 19, 24, 27 PEP 617, 6 PEP 623, 4, 16, 37 PEP 626, 19, 22 PEP 632, 4, 25 PEP 0632#migration-advice, 4 PEP 644, 25 PEP 669, 7 PEP 678, 10 PEP 683, 32 PEP 684, 6, 32 PEP 688, 7 PEP 692, 8, 9 PEP 693, 3 PEP 695, 4, 5, 16 PEP 697, 31 PEP 698, 9 PEP 699, 34, 36 PEP 701, 5, 6, 14, 16, 29, 30 PEP 706, 10 PEP 709, 7, 16 PYTHONHOME, 37 PYTHONPERFSUPPORT, 10
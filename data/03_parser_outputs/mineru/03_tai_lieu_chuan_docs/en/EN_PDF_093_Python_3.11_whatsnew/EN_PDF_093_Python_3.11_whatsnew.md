<!-- page: 1 -->

# What’s New in Python Release 3.11.10

**A. M. Kuchling**

**September 10, 2024**

**Python Software Foundation**

**Email: docs@python.org**

## Contents

- Summary – Release highlights
- New Features
- 2.1 PEP 657: Fine-grained error locations in tracebacks ..... 4
- 2.2 PEP 654: Exception Groups and except\* ..... 5
- 2.3 PEP 678: Exceptions can be enriched with notes ..... 5
- 2.4 Windows py.exe launcher improvements ..... 5
- New Features Related to Type Hints
- 3.1 PEP 646: Variadic generics ..... 5
- 3.2 PEP 655: Marking individual TypedDict items as required or not-required ..... 6
- 3.3 PEP 673: Self type ..... 6
- 3.4 PEP 675: Arbitrary literal string type ..... 7
- 3.5 PEP 681: Data class transforms ..... 7
- 3.6 PEP 563 may not be the future ..... 8
- Other Language Changes
- Other CPython Implementation Changes
- New Modules
- Improved Modules
- 7.1 asyncio ..... 9
- 7.2 contextlib ..... 10
- 7.3 dataclasses ..... 10
- 7.4 datetime ..... 10
- 7.5 enum ..... 10
- 7.6 fcntl ..... 11
- 7.7 fractions ..... 11
- 7.8 functools ..... 11
- 7.9 gzip ..... 11
- 7.10 hashlib ..... 12
- 7.11 IDLE and idlelib ..... 12
- 7.12 inspect ..... 12
- 7.13 locale ..... 12
- 7.14 logging ..... 12
- 7.15 math ..... 13
- 7.16 operator ..... 13

<!-- page: 2 -->

- 7.17 os . 13
- 7.18 pathlib . 13
- 7.19 re . 13
- 7.20 shutil . 13
- 7.21 socket . 13
- 7.22 sqlite3 . 14
- 7.23 string . 14
- 7.24 sys . 14
- 7.25 sysconfig . 15
- 7.26 tempfile . 15
- 7.27 threading . 15
- 7.28 time . 15
- 7.29 tkinter . 15
- 7.30 traceback . 15
- 7.31 typing . 16
- 7.32 unicodedata . 16
- 7.33 unittest . 17
- 7.34 venv . 17
- 7.35 warnings . 17
- 7.36 zipfile . 17
- **8 Optimizations 17**
- **9 Faster CPython 18**
- 9.1 Faster Startup . 18
- 9.2 Faster Runtime . 18
- 9.3 Misc . 20
- 9.4 FAQ . 21
- 9.5 About . 21
- **10 CPython bytecode changes 21**
- 10.1 New opcodes . 22
- 10.2 Replaced opcodes . 22
- 10.3 Changed/removed opcodes . 23
- **11 Deprecated 23**
- 11.1 Language/Builtins . 23
- 11.2 Modules . 23
- 11.3 Standard Library . 24
- **12 Pending Removal in Python 3.12 25**
- **13 Removed 26**
- **14 Porting to Python 3.11 27**
- **15 Build Changes 28**
- **16 C API Changes 29**
- 16.1 New Features . 29
- 16.2 Porting to Python 3.11 . 30
- 16.3 Deprecated . 34
- 16.4 Pending Removal in Python 3.12 . 35
- 16.5 Removed . 35
- **17 Notable Changes in 3.11.4 36**
- 17.1 tarfile . 36
- **18 Notable Changes in 3.11.5 37**
- 18.1 OpenSSL . 37

<!-- page: 3 -->

- **19 Notable changes in 3.11.10 37**
- 19.1 ipaddress . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
- 19.2 email . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
- **Index 38**

## Editor

Pablo Galindo Salgado

This article explains the new features in Python 3.11, compared to 3.10. Python 3.11 was released on October 24, 2022. For full details, see the changelog.

## 1 Summary – Release highlights

• Python 3.11 is between 10-60% faster than Python 3.10. On average, we measured a 1.25x speedup on the standard benchmark suite. See Faster CPython for details.

New syntax features:

• PEP 654: Exception Groups and except\*

New built-in features:

• PEP 678: Exceptions can be enriched with notes

New standard library modules:

• [**PEP 680**](https://peps.python.org/pep-0680/): tomllib — Support for parsing [TOML](https://toml.io/) in the Standard Library

Interpreter improvements:

• PEP 657: Fine-grained error locations in tracebacks

• New -P command line option and PYTHONSAFEPATH environment variable to disable automatically prepending potentially unsafe paths to sys.path

New typing features:

• PEP 646: Variadic generics

• PEP 655: Marking individual TypedDict items as required or not-required

• PEP 673: Self type

• PEP 675: Arbitrary literal string type

• PEP 681: Data class transforms

Important deprecations, removals and restrictions:

• [**PEP 594**](https://peps.python.org/pep-0594/): Many legacy standard library modules have been deprecated and will be removed in Python 3.13

• [**PEP 624**](https://peps.python.org/pep-0624/): Py\_UNICODE encoder APIs have been removed

• [**PEP 670**](https://peps.python.org/pep-0670/): Macros converted to static inline functions

<!-- page: 4 -->

## 2 New Features

## 2.1 PEP 657: Fine-grained error locations in tracebacks

When printing tracebacks, the interpreter will now point to the exact expression that caused the error, instead of just the line. For example:

```python
Traceback (most recent call last):
  File "distance.py", line 11, in <module>
    print(manhattan_distance(p1, p2))
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "distance.py", line 6, in manhattan_distance
    return abs(point_1.x - point_2.x) + abs(point_1.y - point_2.y)
      ^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'x'
```

Previous versions of the interpreter would point to just the line, making it ambiguous which object was None. These enhanced errors can also be helpful when dealing with deeply nested dict objects and multiple function calls:

```txt
Traceback (most recent call last):
  File "query.py", line 37, in <module>
    magic_arithmetic('foo')
  File "query.py", line 18, in magic_arithmetic
    return add_counts(x) / 25
      ^^^^^^^^^^^
  File "query.py", line 24, in add_counts
    return 25 + query_user(user1) + query_user(user2)
      ^^^^^^^^^^^^^^^
  File "query.py", line 32, in query_user
    return 1 + query_count(db, response['a']['b']['c']['user'], retry=True)
      ^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

As well as complex arithmetic expressions:

```txt
Traceback (most recent call last):
  File "calculation.py", line 54, in <module>
    result = (x / y / z) * (a / b / c)
      ~~~~~~~^~~~
ZeroDivisionError: division by zero
```

Additionally, the information used by the enhanced traceback feature is made available via a general API, that can be used to correlate bytecode instructions with source code location. This information can be retrieved using:

• The codeobject.co\_positions() method in Python.

• The PyCode\_Addr2Location() function in the C API.

See [**PEP 657**](https://peps.python.org/pep-0657/) for more details. (Contributed by Pablo Galindo, Batuhan Taskaya and Ammar Askar in [bpo-43950](https://bugs.python.org/issue?@action=redirect&bpo=43950).)

**Note:** This feature requires storing column positions in codeobjects, which may result in a small increase in interpreter memory usage and disk usage for compiled Python files. To avoid storing the extra information and deactivate printing the extra traceback information, use the -X no\_debug\_ranges command line option or the PYTHONNODEBUGRANGES environment variable.

<!-- page: 5 -->

## 2.2 PEP 654: Exception Groups and except\*

[**PEP 654**](https://peps.python.org/pep-0654/) introduces language features that enable a program to raise and handle multiple unrelated exceptions simultaneously. The builtin types ExceptionGroup and BaseExceptionGroup make it possible to group exceptions and raise them together, and the new except\* syntax generalizes except to match subgroups of exception groups.

See [**PEP 654**](https://peps.python.org/pep-0654/) for more details.

(Contributed by Irit Katriel in [bpo-45292](https://bugs.python.org/issue?@action=redirect&bpo=45292). PEP written by Irit Katriel, Yury Selivanov and Guido van Rossum.)

## 2.3 PEP 678: Exceptions can be enriched with notes

The add\_note() method is added to BaseException. It can be used to enrich exceptions with context information that is not available at the time when the exception is raised. The added notes appear in the default traceback. See [**PEP 678**](https://peps.python.org/pep-0678/) for more details.

(Contributed by Irit Katriel in [bpo-45607](https://bugs.python.org/issue?@action=redirect&bpo=45607). PEP written by Zac Hatfield-Dodds.)

## 2.4 Windows py.exe launcher improvements

The copy of the launcher included with Python 3.11 has been significantly updated. It now supports company/tag syntax as defined in [**PEP 514**](https://peps.python.org/pep-0514/) using the -V:&lt;company&gt;/&lt;tag&gt; argument instead of the limited -&lt;major&gt;. &lt;minor&gt;. This allows launching distributions other than PythonCore, the one hosted on [python.org](https://www.python.org).

When using -V: selectors, either company or tag can be omitted, but all installs will be searched. For example, -V:OtherPython/ will select the “best” tag registered for OtherPython, while -V:3.11 or -V:/3.11 will select the “best” distribution with tag 3.11.

When using the legacy -&lt;major&gt;, -&lt;major&gt;.&lt;minor&gt;, -&lt;major&gt;-&lt;bitness&gt; or -&lt;major&gt;. &lt;minor&gt;-&lt;bitness&gt; arguments, all existing behaviour should be preserved from past versions, and only releases from PythonCore will be selected. However, the -64 suffix now implies “not 32-bit” (not necessarily x86-64), as there are multiple supported 64-bit platforms. 32-bit runtimes are detected by checking the runtime’s tag for a -32 suffix. All releases of Python since 3.5 have included this in their 32-bit builds.

## 3 New Features Related to Type Hints

This section covers major changes affecting [**PEP 484**](https://peps.python.org/pep-0484/) type hints and the typing module.

## 3.1 PEP 646: Variadic generics

[**PEP 484**](https://peps.python.org/pep-0484/) previously introduced TypeVar, enabling creation of generics parameterised with a single type. [**PEP 646**](https://peps.python.org/pep-0646/) adds TypeVarTuple, enabling parameterisation with an arbitrary number of types. In other words, a TypeVarTuple is a variadic type variable, enabling variadic generics.

This enables a wide variety of use cases. In particular, it allows the type of array-like structures in numerical computing libraries such as NumPy and TensorFlow to be parameterised with the array shape. Static type checkers will now be able to catch shape-related bugs in code that uses these libraries.

See [**PEP 646**](https://peps.python.org/pep-0646/) for more details.

(Contributed by Matthew Rahtz in [bpo-43224](https://bugs.python.org/issue?@action=redirect&bpo=43224), with contributions by Serhiy Storchaka and Jelle Zijlstra. PEP written by Mark Mendoza, Matthew Rahtz, Pradeep Kumar Srinivasan, and Vincent Siles.)

<!-- page: 6 -->

## 3.2 PEP 655: Marking individual TypedDict items as required or not-required

Required and NotRequired provide a straightforward way to mark whether individual items in a TypedDict must be present. Previously, this was only possible using inheritance.

All fields are still required by default, unless the total parameter is set to False, in which case all fields are still not-required by default. For example, the following specifies a TypedDict with one required and one not-required key:

```python
class Movie (TypedDict):
    title: str
    year: NotRequired[int]

m1: Movie = {"title": "Black Panther", "year": 2018}  # OK
m2: Movie = {"title": "Star Wars"}  # OK (year is not required)
m3: Movie = {"year": 2022}  # ERROR (missing required field title)
```

The following definition is equivalent:

```python
class Movie(TypedDict, total=False):
  title: Required[str]
  year: int
```

See [**PEP 655**](https://peps.python.org/pep-0655/) for more details.

(Contributed by David Foster and Jelle Zijlstra in [bpo-47087](https://bugs.python.org/issue?@action=redirect&bpo=47087). PEP written by David Foster.)

## 3.3 PEP 673: Self type

The new Self annotation provides a simple and intuitive way to annotate methods that return an instance of their class. This behaves the same as the TypeVar-based approach [**specified in PEP 484**](https://peps.python.org/pep-0484/#annotating-instance-and-class-methods), but is more concise and easier to follow.

Common use cases include alternative constructors provided as classmethods, and \_\_enter\_\_() methods that return self:

```python
class MyLock:
    def __enter__(self) -> Self:
        self.lock()
        return self

    ...

class MyInt:
    @classmethod
    def fromhex(cls, s: str) -> Self:
        return cls(int(s, 16))

    ...
```

Self can also be used to annotate method parameters or attributes of the same type as their enclosing class.

See [**PEP 673**](https://peps.python.org/pep-0673/) for more details.

(Contributed by James Hilton-Balfe in [bpo-46534](https://bugs.python.org/issue?@action=redirect&bpo=46534). PEP written by Pradeep Kumar Srinivasan and James Hilton-Balfe.)

<!-- page: 7 -->

## 3.4 PEP 675: Arbitrary literal string type

The new LiteralString annotation may be used to indicate that a function parameter can be of any literal string type. This allows a function to accept arbitrary literal string types, as well as strings created from other literal strings. Type checkers can then enforce that sensitive functions, such as those that execute SQL statements or shell commands, are called only with static arguments, providing protection against injection attacks.

For example, a SQL query function could be annotated as follows:

```python
def run_query(sql: LiteralString) -> ...
    ...

def caller(
    arbitrary_string: str,
    query_string: LiteralString,
    table_name: LiteralString,
) -> None:
    run_query("SELECT * FROM students")          # ok
    run_query(query_string)                    # ok
    run_query("SELECT * FROM " + table_name)  # ok
    run_query(arbitrary_string)                 # type checker error
    run_query(
        f"SELECT * FROM students WHERE name = {arbitrary_string}"
    )
```

See [**PEP 675**](https://peps.python.org/pep-0675/) for more details.

(Contributed by Jelle Zijlstra in [bpo-47088](https://bugs.python.org/issue?@action=redirect&bpo=47088). PEP written by Pradeep Kumar Srinivasan and Graham Bleaney.)

## 3.5 PEP 681: Data class transforms

dataclass\_transform may be used to decorate a class, metaclass, or a function that is itself a decorator. The presence of @dataclass\_transform() tells a static type checker that the decorated object performs runtime “magic” that transforms a class, giving it dataclass-like behaviors.

For example:

```python
# The create_model decorator is defined by a library.
@typing.dataclass_transform()
def create_model(cls: Type[T]) -> Type[T]:
    cls.__init__ = ...
    cls.__eq__ = ...
    cls.__ne__ = ...
    return cls

# The create_model decorator can now be used to create new model classes:
@create_model
class CustomerModel:
    id: int
    name: str

c = CustomerModel(id=327, name="Eric Idle")
```

See [**PEP 681**](https://peps.python.org/pep-0681/) for more details.

(Contributed by Jelle Zijlstra in [gh-91860](https://github.com/python/cpython/issues/91860). PEP written by Erik De Bonte and Eric Traut.)

<!-- page: 8 -->

## 3.6 PEP 563 may not be the future

[**PEP 563**](https://peps.python.org/pep-0563/) Postponed Evaluation of Annotations (the from \_\_future\_\_ import annotations future statement) that was originally planned for release in Python 3.10 has been put on hold indefinitely. See [this message from the Steering Council](https://mail.python.org/archives/list/python-dev@python.org/message/VIZEBX5EYMSYIJNDBF6DMUMZOCWHARSO/) for more information.

## 4 Other Language Changes

• Starred unpacking expressions can now be used in for statements. (See [bpo-46725](https://bugs.python.org/issue?@action=redirect&bpo=46725) for more details.)

• Asynchronous comprehensions are now allowed inside comprehensions in asynchronous functions. Outer comprehensions implicitly become asynchronous in this case. (Contributed by Serhiy Storchaka in [bpo-33346](https://bugs.python.org/issue?@action=redirect&bpo=33346).)

• A TypeError is now raised instead of an AttributeError in with statements and contextlib. ExitStack.enter\_context() for objects that do not support the context manager protocol, and in async with statements and contextlib.AsyncExitStack.enter\_async\_context() for objects not supporting the asynchronous context manager protocol. (Contributed by Serhiy Storchaka in [bpo-12022](https://bugs.python.org/issue?@action=redirect&bpo=12022) and [bpo-44471](https://bugs.python.org/issue?@action=redirect&bpo=44471).)

• Added object.\_\_getstate\_\_(), which provides the default implementation of the getstate\_\_() method. copying and pickleing instances of subclasses of builtin types bytearray, set, frozenset, collections.OrderedDict, collections.deque, weakref.WeakSet, and datetime.tzinfo now copies and pickles instance attributes implemented as slots. This change has an unintended side effect: It trips up a small minority of existing Python projects not expecting object.\_\_getstate\_\_() to exist. See the later comments on [gh-70766](https://github.com/python/cpython/issues/70766) for discussions of what workarounds such code may need. (Contributed by Serhiy Storchaka in [bpo-26579](https://bugs.python.org/issue?@action=redirect&bpo=26579).)

• Added a -P command line option and a PYTHONSAFEPATH environment variable, which disable the automatic prepending to sys.path of the script’s directory when running a script, or the current directory when using -c and -m. This ensures only stdlib and installed modules are picked up by import, and avoids unintentionally or maliciously shadowing modules with those in a local (and typically user-writable) directory. (Contributed by Victor Stinner in [gh-57684](https://github.com/python/cpython/issues/57684).)

• A "z" option was added to the formatspec that coerces negative to positive zero after rounding to the format precision. See [**PEP 682**](https://peps.python.org/pep-0682/) for more details. (Contributed by John Belmonte in [gh-90153](https://github.com/python/cpython/issues/90153).)

• Bytes are no longer accepted on sys.path. Support broke sometime between Python 3.2 and 3.6, with no one noticing until after Python 3.10.0 was released. In addition, bringing back support would be problematic due to interactions between -b and sys.path\_importer\_cache when there is a mixture of str and bytes keys. (Contributed by Thomas Grainger in [gh-91181](https://github.com/python/cpython/issues/91181).)

## 5 Other CPython Implementation Changes

• The special methods \_\_complex\_\_() for complex and \_\_bytes\_\_() for bytes are implemented to support the typing.SupportsComplex and typing.SupportsBytes protocols. (Contributed by Mark Dickinson and Donghee Na in [bpo-24234](https://bugs.python.org/issue?@action=redirect&bpo=24234).)

• siphash13 is added as a new internal hashing algorithm. It has similar security properties as siphash24, but it is slightly faster for long inputs. str, bytes, and some other types now use it as the default algorithm for hash(). [**PEP 552**](https://peps.python.org/pep-0552/) hash-based .pyc files now use siphash13 too. (Contributed by Inada Naoki in [bpo-29410](https://bugs.python.org/issue?@action=redirect&bpo=29410).)

• When an active exception is re-raised by a raise statement with no parameters, the traceback attached to this exception is now always sys.exc\_info()[1].\_\_traceback\_\_. This means that changes made to the traceback in the current except clause are reflected in the re-raised exception. (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

<!-- page: 9 -->

• The interpreter state’s representation of handled exceptions (aka exc\_info or \_PyErr\_StackItem) now only has the exc\_value field; exc\_type and exc\_traceback have been removed, as they can be derived from exc\_value. (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

• A new command line option, AppendPath, has been added for the Windows installer. It behaves similarly to PrependPath, but appends the install and scripts directories instead of prepending them. (Contributed by Bastian Neuburger in [bpo-44934](https://bugs.python.org/issue?@action=redirect&bpo=44934).)

• The PyConfig.module\_search\_paths\_set field must now be set to 1 for initialization to use PyConfig.module\_search\_paths to initialize sys.path. Otherwise, initialization will recalculate the path and replace any values added to module\_search\_paths.

• The output of the --help option now fits in 50 lines/80 columns. Information about Python environment variables and -X options is now available using the respective --help-env and --help-xoptions flags, and with the new --help-all. (Contributed by É ric Araujo in [bpo-46142](https://bugs.python.org/issue?@action=redirect&bpo=46142).)

• Converting between int and str in bases other than 2 (binary), 4, 8 (octal), 16 (hexadecimal), or 32 such as base 10 (decimal) now raises a ValueError if the number of digits in string form is above a limit to avoid potential denial of service attacks due to the algorithmic complexity. This is a mitigation for [CVE-2020-10735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10735). This limit can be configured or disabled by environment variable, command line flag, or sys APIs. See the integer string conversion length limitation documentation. The default limit is 4300 digits in string form.

## 6 New Modules

• tomllib: For parsing [TOML](https://toml.io/). See [**PEP 680**](https://peps.python.org/pep-0680/) for more details. (Contributed by Taneli Hukkinen in [bpo-40059](https://bugs.python.org/issue?@action=redirect&bpo=40059).)

• wsgiref.types: [**WSGI**](https://peps.python.org/pep-3333/)-specific types for static type checking. (Contributed by Sebastian Rittau in [bpo-42012](https://bugs.python.org/issue?@action=redirect&bpo=42012).)

## 7 Improved Modules

## 7.1 asyncio

• Added the TaskGroup class, an asynchronous context manager holding a group of tasks that will wait for all of them upon exit. For new code this is recommended over using create\_task() and gather() directly. (Contributed by Yury Selivanov and others in [gh-90908](https://github.com/python/cpython/issues/90908).)

• Added timeout(), an asynchronous context manager for setting a timeout on asynchronous operations. For new code this is recommended over using wait\_for() directly. (Contributed by Andrew Svetlov in [gh-90927](https://github.com/python/cpython/issues/90927).)

• Added the Runner class, which exposes the machinery used by run(). (Contributed by Andrew Svetlov in [gh-91218](https://github.com/python/cpython/issues/91218).)

• Added the Barrier class to the synchronization primitives in the asyncio library, and the related BrokenBarrierError exception. (Contributed by Yves Duprat and Andrew Svetlov in [gh-87518](https://github.com/python/cpython/issues/87518).)

• Added keyword argument all\_errors to asyncio.loop.create\_connection() so that multiple connection errors can be raised as an ExceptionGroup.

• Added the asyncio.StreamWriter.start\_tls() method for upgrading existing stream-based connections to TLS. (Contributed by Ian Good in [bpo-34975](https://bugs.python.org/issue?@action=redirect&bpo=34975).)

• Added raw datagram socket functions to the event loop: sock\_sendto(), sock\_recvfrom() and sock\_recvfrom\_into(). These have implementations in SelectorEventLoop and ProactorEventLoop. (Contributed by Alex Grönholm in [bpo-46805](https://bugs.python.org/issue?@action=redirect&bpo=46805).)

<!-- page: 10 -->

• Added cancelling() and uncancel() methods to Task. These are primarily intended for internal use, notably by TaskGroup.

## 7.2 contextlib

• Added non parallel-safe chdir() context manager to change the current working directory and then restore it on exit. Simple wrapper around chdir(). (Contributed by Filipe Laíns in [bpo-25625](https://bugs.python.org/issue?@action=redirect&bpo=25625))

## 7.3 dataclasses

• Change field default mutability check, allowing only defaults which are hashable instead of any object which is not an instance of dict, list or set. (Contributed by Eric V. Smith in [bpo-44674](https://bugs.python.org/issue?@action=redirect&bpo=44674).)

## 7.4 datetime

• Add datetime.UTC, a convenience alias for datetime.timezone.utc. (Contributed by Kabir Kwatra in [gh-91973](https://github.com/python/cpython/issues/91973).)

• datetime.date.fromisoformat(), datetime.time.fromisoformat() and datetime. datetime.fromisoformat() can now be used to parse most ISO 8601 formats (barring only those that support fractional hours and minutes). (Contributed by Paul Ganssle in [gh-80010](https://github.com/python/cpython/issues/80010).)

## 7.5 enum

• Renamed EnumMeta to EnumType (EnumMeta kept as an alias).

• Added StrEnum, with members that can be used as (and must be) strings.

• Added ReprEnum, which only modifies the \_\_repr\_\_() of members while returning their literal values (rather than names) for \_\_str\_\_() and \_\_format\_\_() (used by str(), format() and f-strings).

• Changed Enum.\_\_format\_\_() (the default for format(), str.format() and f-strings) to always produce the same result as Enum.\_\_str\_\_(): for enums inheriting from ReprEnum it will be the member’s value; for all other enums it will be the enum and member name (e.g. Color.RED).

• Added a new boundary class parameter to Flag enums and the FlagBoundary enum with its options, to control how to handle out-of-range flag values.

• Added the verify() enum decorator and the EnumCheck enum with its options, to check enum classes against several specific constraints.

• Added the member() and nonmember() decorators, to ensure the decorated object is/is not converted to an enum member.

• Added the property() decorator, which works like property() except for enums. Use this instead of types.DynamicClassAttribute().

• Added the global\_enum() enum decorator, which adjusts \_\_repr\_\_() and \_\_str\_\_() to show values as members of their module rather than the enum class. For example, 're.ASCII' for the ASCII member of re.RegexFlag rather than 'RegexFlag.ASCII'.

• Enhanced Flag to support len(), iteration and in/not in on its members. For example, the following now works: len(AFlag(3)) == 2 and list(AFlag(3)) == (AFlag.ONE, AFlag.TWO)

• Changed Enum and Flag so that members are now defined before \_\_init\_subclass\_\_() is called; dir() now includes methods, etc., from mixed-in data types.

• Changed Flag to only consider primary values (power of two) canonical while composite values (3, 6, 10, etc.) are considered aliases; inverted flags are coerced to their positive equivalent.

<!-- page: 11 -->

## 7.6 fcntl

• On FreeBSD, the F\_DUP2FD and F\_DUP2FD\_CLOEXEC flags respectively are supported, the former equals to dup2 usage while the latter set the FD\_CLOEXEC flag in addition.

## 7.7 fractions

• Support [**PEP 515**](https://peps.python.org/pep-0515/)-style initialization of Fraction from string. (Contributed by Sergey B Kirpichev in [bpo-44258](https://bugs.python.org/issue?@action=redirect&bpo=44258).)

• Fraction now implements an \_\_int\_\_ method, so that an isinstance(some\_fraction, typing.SupportsInt) check passes. (Contributed by Mark Dickinson in [bpo-44547](https://bugs.python.org/issue?@action=redirect&bpo=44547).)

## 7.8 functools

• functools.singledispatch() now supports types.UnionType and typing.Union as annotations to the dispatch argument.:

```python
>>> from functools import singledispatch
>>> @singledispatch
... def fun(arg, verbose=False):
...     if verbose:
...         print("Let me just say,", end=" ")
...     print(arg)
...
>>> @fun.register
... def _(arg: int | float, verbose=False):
...     if verbose:
...         print("Strength in numbers, eh?", end=" ")
...     print(arg)
...
>>> from typing import Union
>>> @fun.register
... def _(arg: Union[list, set], verbose=False):
...     if verbose:
...         print("Enumerate this:")
...     for i, elem in enumerate(arg):
...         print(i, elem)
...
```

(Contributed by Yurii Karabas in [bpo-46014](https://bugs.python.org/issue?@action=redirect&bpo=46014).)

## 7.9 gzip

• The gzip.compress() function is now faster when used with the **mtime=0** argument as it delegates the compression entirely to a single zlib.compress() operation. There is one side effect of this change: The gzip file header contains an “OS” byte in its header. That was traditionally always set to a value of 255 representing “unknown” by the gzip module. Now, when using compress() with **mtime=0**, it may be set to a different value by the underlying zlib C library Python was linked against. (See [gh-112346](https://github.com/python/cpython/issues/112346) for details on the side effect.)

<!-- page: 12 -->

## 7.10 hashlib

• hashlib.blake2b() and hashlib.blake2s() now prefer [libb2](https://www.blake2.net/) over Python’s vendored copy. (Contributed by Christian Heimes in [bpo-47095](https://bugs.python.org/issue?@action=redirect&bpo=47095).)

• The internal \_sha3 module with SHA3 and SHAKE algorithms now uses tiny\_sha3 instead of the Keccak Code Package to reduce code and binary size. The hashlib module prefers optimized SHA3 and SHAKE implementations from OpenSSL. The change affects only installations without OpenSSL support. (Contributed by Christian Heimes in [bpo-47098](https://bugs.python.org/issue?@action=redirect&bpo=47098).)

• Add hashlib.file\_digest(), a helper function for efficient hashing of files or file-like objects. (Contributed by Christian Heimes in [gh-89313](https://github.com/python/cpython/issues/89313).)

## 7.11 IDLE and idlelib

• Apply syntax highlighting to .pyi files. (Contributed by Alex Waygood and Terry Jan Reedy in [bpo-45447](https://bugs.python.org/issue?@action=redirect&bpo=45447).)

• Include prompts when saving Shell with inputs and outputs. (Contributed by Terry Jan Reedy in [gh-95191](https://github.com/python/cpython/issues/95191).)

## 7.12 inspect

• Add getmembers\_static() to return all members without triggering dynamic lookup via the descriptor protocol. (Contributed by Weipeng Hong in [bpo-30533](https://bugs.python.org/issue?@action=redirect&bpo=30533).)

• Add ismethodwrapper() for checking if the type of an object is a MethodWrapperType. (Contributed by Hakan Çelik in [bpo-29418](https://bugs.python.org/issue?@action=redirect&bpo=29418).)

• Change the frame-related functions in the inspect module to return new FrameInfo and Traceback class instances (backwards compatible with the previous named tuple-like interfaces) that includes the extended [**PEP 657**](https://peps.python.org/pep-0657/) position information (end line number, column and end column). The affected functions are:

– inspect.getframeinfo()

– inspect.getouterframes()

– inspect.getinnerframes(),

– inspect.stack()

– inspect.trace()

(Contributed by Pablo Galindo in [gh-88116](https://github.com/python/cpython/issues/88116).)

## 7.13 locale

• Add locale.getencoding() to get the current locale encoding. It is similar to locale. getpreferredencoding(False) but ignores the Python UTF-8 Mode.

## 7.14 logging

• Added getLevelNamesMapping() to return a mapping from logging level names (e.g. 'CRITICAL') to the values of their corresponding levels (e.g. 50, by default). (Contributed by Andrei Kulakovin in [gh-88024](https://github.com/python/cpython/issues/88024).)

• Added a createSocket() method to SysLogHandler, to match SocketHandler. createSocket(). It is called automatically during handler initialization and when emitting an event, if there is no active socket. (Contributed by Kirill Pinchuk in [gh-88457](https://github.com/python/cpython/issues/88457).)

<!-- page: 13 -->

## 7.15 math

• Add math.exp2(): return 2 raised to the power of x. (Contributed by Gideon Mitchell in [bpo-45917](https://bugs.python.org/issue?@action=redirect&bpo=45917).)

• Add math.cbrt(): return the cube root of x. (Contributed by Ajith Ramachandran in [bpo-44357](https://bugs.python.org/issue?@action=redirect&bpo=44357).)

• The behaviour of two math.pow() corner cases was changed, for consistency with the IEEE 754 specification. The operations math.pow(0.0, -math.inf) and math.pow(-0.0, -math.inf) now return inf. Previously they raised ValueError. (Contributed by Mark Dickinson in [bpo-44339](https://bugs.python.org/issue?@action=redirect&bpo=44339).)

• The math.nan value is now always available. (Contributed by Victor Stinner in [bpo-46917](https://bugs.python.org/issue?@action=redirect&bpo=46917).)

## 7.16 operator

• A new function operator.call has been added, such that operator.call(obj, \*args, \*\*kwargs) == obj(\*args, \*\*kwargs). (Contributed by Antony Lee in [bpo-44019](https://bugs.python.org/issue?@action=redirect&bpo=44019).)

## 7.17 os

• On Windows, os.urandom() now uses BCryptGenRandom(), instead of CryptGenRandom() which is deprecated. (Contributed by Donghee Na in [bpo-44611](https://bugs.python.org/issue?@action=redirect&bpo=44611).)

• As of 3.11.10, os.mkdir() and os.makedirs() on Windows now support passing a mode value of 0o700 to apply access control to the new directory. This implicitly affects tempfile.mkdtemp() and is a mitigation for CVE-2024-4030. Other values for mode continue to be ignored. (Contributed by Steve Dower in [gh-118486](https://github.com/python/cpython/issues/118486).)

## 7.18 pathlib

• glob() and rglob() return only directories if pattern ends with a pathname components separator: sep or altsep. (Contributed by Eisuke Kawasima in [bpo-22276](https://bugs.python.org/issue?@action=redirect&bpo=22276) and [bpo-33392](https://bugs.python.org/issue?@action=redirect&bpo=33392).)

## 7.19 re

• Atomic grouping ((?>...)) and possessive quantifiers (\*+, ++, ?+, {m,n}+) are now supported in regular expressions. (Contributed by Jeffrey C. Jacobs and Serhiy Storchaka in [bpo-433030](https://bugs.python.org/issue?@action=redirect&bpo=433030).)

## 7.20 shutil

• Add optional parameter dir\_fd in shutil.rmtree(). (Contributed by Serhiy Storchaka in [bpo-46245](https://bugs.python.org/issue?@action=redirect&bpo=46245).)

## 7.21 socket

• Add CAN Socket support for NetBSD. (Contributed by Thomas Klausner in [bpo-30512](https://bugs.python.org/issue?@action=redirect&bpo=30512).)

• create\_connection() has an option to raise, in case of failure to connect, an ExceptionGroup containing all errors instead of only raising the last error. (Contributed by Irit Katriel in [bpo-29980](https://bugs.python.org/issue?@action=redirect&bpo=29980).)

<!-- page: 14 -->

## 7.22 sqlite3

• You can now disable the authorizer by passing None to set\_authorizer(). (Contributed by Erlend E. Aasland in [bpo-44491](https://bugs.python.org/issue?@action=redirect&bpo=44491).)

• Collation name create\_collation() can now contain any Unicode character. Collation names with invalid characters now raise UnicodeEncodeError instead of sqlite3.ProgrammingError. (Contributed by Erlend E. Aasland in [bpo-44688](https://bugs.python.org/issue?@action=redirect&bpo=44688).)

• sqlite3 exceptions now include the SQLite extended error code as sqlite\_errorcode and the SQLite error name as sqlite\_errorname. (Contributed by Aviv Palivoda, Daniel Shahaf, and Erlend E. Aasland in [bpo-16379](https://bugs.python.org/issue?@action=redirect&bpo=16379) and [bpo-24139](https://bugs.python.org/issue?@action=redirect&bpo=24139).)

• Add setlimit() and getlimit() to sqlite3.Connection for setting and getting SQLite limits by connection basis. (Contributed by Erlend E. Aasland in [bpo-45243](https://bugs.python.org/issue?@action=redirect&bpo=45243).)

• sqlite3 now sets sqlite3.threadsafety based on the default threading mode the underlying SQLite library has been compiled with. (Contributed by Erlend E. Aasland in [bpo-45613](https://bugs.python.org/issue?@action=redirect&bpo=45613).)

• sqlite3 C callbacks now use unraisable exceptions if callback tracebacks are enabled. Users can now register an unraisable hook handler to improve their debug experience. (Contributed by Erlend E. Aasland in [bpo-45828](https://bugs.python.org/issue?@action=redirect&bpo=45828).)

• Fetch across rollback no longer raises InterfaceError. Instead we leave it to the SQLite library to handle these cases. (Contributed by Erlend E. Aasland in [bpo-44092](https://bugs.python.org/issue?@action=redirect&bpo=44092).)

• Add serialize() and deserialize() to sqlite3.Connection for serializing and deserializing databases. (Contributed by Erlend E. Aasland in [bpo-41930](https://bugs.python.org/issue?@action=redirect&bpo=41930).)

• Add create\_window\_function() to sqlite3.Connection for creating aggregate window functions. (Contributed by Erlend E. Aasland in [bpo-34916](https://bugs.python.org/issue?@action=redirect&bpo=34916).)

• Add blobopen() to sqlite3.Connection. sqlite3.Blob allows incremental I/O operations on blobs. (Contributed by Aviv Palivoda and Erlend E. Aasland in [bpo-24905](https://bugs.python.org/issue?@action=redirect&bpo=24905).)

## 7.23 string

• Add get\_identifiers() and is\_valid() to string.Template, which respectively return all valid placeholders, and whether any invalid placeholders are present. (Contributed by Ben Kehoe in [gh-90465](https://github.com/python/cpython/issues/90465).)

## 7.24 sys

• sys.exc\_info() now derives the type and traceback fields from the value (the exception instance), so when an exception is modified while it is being handled, the changes are reflected in the results of subsequent calls to exc\_info(). (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

• Add sys.exception() which returns the active exception instance (equivalent to sys. exc\_info()[1]). (Contributed by Irit Katriel in [bpo-46328](https://bugs.python.org/issue?@action=redirect&bpo=46328).)

• Add the sys.flags.safe\_path flag. (Contributed by Victor Stinner in [gh-57684](https://github.com/python/cpython/issues/57684).)

<!-- page: 15 -->

## 7.25 sysconfig

• Three new installation schemes (posix\_venv, nt\_venv and venv) were added and are used when Python creates new virtual environments or when it is running from a virtual environment. The first two schemes (posix\_venv and nt\_venv) are OS-specific for non-Windows and Windows, the venv is essentially an alias to one of them according to the OS Python runs on. This is useful for downstream distributors who modify sysconfig. get\_preferred\_scheme(). Third party code that creates new virtual environments should use the new venv installation scheme to determine the paths, as does venv. (Contributed by Miro Hrončok in [bpo-45413](https://bugs.python.org/issue?@action=redirect&bpo=45413).)

## 7.26 tempfile

• SpooledTemporaryFile objects now fully implement the methods of io.BufferedIOBase or io. TextIOBase (depending on file mode). This lets them work correctly with APIs that expect file-like objects, such as compression modules. (Contributed by Carey Metcalfe in [gh-70363](https://github.com/python/cpython/issues/70363).)

• As of 3.11.10 on Windows, the default mode 0o700 used by tempfile.mkdtemp() now limits access to the new directory due to changes to os.mkdir(). This is a mitigation for CVE-2024-4030. (Contributed by Steve Dower in [gh-118486](https://github.com/python/cpython/issues/118486).)

## 7.27 threading

• On Unix, if the sem\_clockwait() function is available in the C library (glibc 2.30 and newer), the threading.Lock.acquire() method now uses the monotonic clock (time.CLOCK\_MONOTONIC) for the timeout, rather than using the system clock (time.CLOCK\_REALTIME), to not be affected by system clock changes. (Contributed by Victor Stinner in [bpo-41710](https://bugs.python.org/issue?@action=redirect&bpo=41710).)

## 7.28 time

• On Unix, time.sleep() now uses the clock\_nanosleep() or nanosleep() function, if available, which has a resolution of 1 nanosecond (10<sup>-9</sup> seconds), rather than using select() which has a resolution of 1 microsecond (10<sup>-6</sup> seconds). (Contributed by Benjamin Szőke and Victor Stinner in [bpo-21302](https://bugs.python.org/issue?@action=redirect&bpo=21302).)

• On Windows 8.1 and newer, time.sleep() now uses a waitable timer based on [high-resolution timers](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/high-resolution-timers) which has a resolution of 100 nanoseconds (10<sup>-7</sup> seconds). Previously, it had a resolution of 1 millisecond (10<sup>-3</sup> seconds). (Contributed by Benjamin Szőke, Donghee Na, Eryk Sun and Victor Stinner in [bpo-21302](https://bugs.python.org/issue?@action=redirect&bpo=21302) and [bpo-45429](https://bugs.python.org/issue?@action=redirect&bpo=45429).)

## 7.29 tkinter

• Added method info\_patchlevel() which returns the exact version of the Tcl library as a named tuple similar to sys.version\_info. (Contributed by Serhiy Storchaka in [gh-91827](https://github.com/python/cpython/issues/91827).)

## 7.30 traceback

• Add traceback.StackSummary.format\_frame\_summary() to allow users to override which frames appear in the traceback, and how they are formatted. (Contributed by Ammar Askar in [bpo-44569](https://bugs.python.org/issue?@action=redirect&bpo=44569).)

• Add traceback.TracebackException.print(), which prints the formatted TracebackException instance to a file. (Contributed by Irit Katriel in [bpo-33809](https://bugs.python.org/issue?@action=redirect&bpo=33809).)

<!-- page: 16 -->

## 7.31 typing

For major changes, see New Features Related to Type Hints.

• Add typing.assert\_never() and typing.Never. typing.assert\_never() is useful for asking a type checker to confirm that a line of code is not reachable. At runtime, it raises an AssertionError. (Contributed by Jelle Zijlstra in [gh-90633](https://github.com/python/cpython/issues/90633).)

• Add typing.reveal\_type(). This is useful for asking a type checker what type it has inferred for a given expression. At runtime it prints the type of the received value. (Contributed by Jelle Zijlstra in [gh-90572](https://github.com/python/cpython/issues/90572).)

• Add typing.assert\_type(). This is useful for asking a type checker to confirm that the type it has inferred for a given expression matches the given type. At runtime it simply returns the received value. (Contributed by Jelle Zijlstra in [gh-90638](https://github.com/python/cpython/issues/90638).)

• typing.TypedDict types can now be generic. (Contributed by Samodya Abeysiriwardane in [gh-89026](https://github.com/python/cpython/issues/89026).)

• NamedTuple types can now be generic. (Contributed by Serhiy Storchaka in [bpo-43923](https://bugs.python.org/issue?@action=redirect&bpo=43923).)

• Allow subclassing of typing.Any. This is useful for avoiding type checker errors related to highly dynamic class, such as mocks. (Contributed by Shantanu Jain in [gh-91154](https://github.com/python/cpython/issues/91154).)

• The typing.final() decorator now sets the \_\_final\_\_ attributed on the decorated object. (Contributed by Jelle Zijlstra in [gh-90500](https://github.com/python/cpython/issues/90500).)

• The typing.get\_overloads() function can be used for introspecting the overloads of a function. typing.clear\_overloads() can be used to clear all registered overloads of a function. (Contributed by Jelle Zijlstra in [gh-89263](https://github.com/python/cpython/issues/89263).)

• The \_\_init\_\_() method of Protocol subclasses is now preserved. (Contributed by Adrian Garcia Badarasco in [gh-88970](https://github.com/python/cpython/issues/88970).)

• The representation of empty tuple types (Tuple[()]) is simplified. This affects introspection, e.g. get\_args(Tuple[()]) now evaluates to () instead of ((),). (Contributed by Serhiy Storchaka in [gh-91137](https://github.com/python/cpython/issues/91137).)

• Loosen runtime requirements for type annotations by removing the callable check in the private typing. \_type\_check function. (Contributed by Gregory Beauregard in [gh-90802](https://github.com/python/cpython/issues/90802).)

• typing.get\_type\_hints() now supports evaluating strings as forward references in PEP 585 generic aliases. (Contributed by Niklas Rosenstein in [gh-85542](https://github.com/python/cpython/issues/85542).)

• typing.get\_type\_hints() no longer adds Optional to parameters with None as a default. (Contributed by Nikita Sobolev in [gh-90353](https://github.com/python/cpython/issues/90353).)

• typing.get\_type\_hints() now supports evaluating bare stringified ClassVar annotations. (Contributed by Gregory Beauregard in [gh-90711](https://github.com/python/cpython/issues/90711).)

• typing.no\_type\_check() no longer modifies external classes and functions. It also now correctly marks classmethods as not to be type checked. (Contributed by Nikita Sobolev in [gh-90729](https://github.com/python/cpython/issues/90729).)

## 7.32 unicodedata

• The Unicode database has been updated to version 14.0.0. (Contributed by Benjamin Peterson in [bpo-45190](https://bugs.python.org/issue?@action=redirect&bpo=45190)).

<!-- page: 17 -->

## 7.33 unittest

• Added methods enterContext() and enterClassContext() of class TestCase, method enterAsyncContext() of class IsolatedAsyncioTestCase and function unittest. enterModuleContext(). (Contributed by Serhiy Storchaka in [bpo-45046](https://bugs.python.org/issue?@action=redirect&bpo=45046).)

## 7.34 venv

When new Python virtual environments are created, the venv sysconfig installation scheme is used to determine the paths inside the environment. When Python runs in a virtual environment, the same installation scheme is the default. That means that downstream distributors can change the default sysconfig install scheme without changing behavior of virtual environments. Third party code that also creates new virtual environments should do the same. (Contributed by Miro Hrončok in [bpo-45413](https://bugs.python.org/issue?@action=redirect&bpo=45413).)

## 7.35 warnings

• warnings.catch\_warnings() now accepts arguments for warnings.simplefilter(), providing a more concise way to locally ignore warnings or convert them to errors. (Contributed by Zac Hatfield-Dodds in [bpo-47074](https://bugs.python.org/issue?@action=redirect&bpo=47074).)

## 7.36 zipfile

• Added support for specifying member name encoding for reading metadata in a ZipFile’s directory and file headers. (Contributed by Stephen J. Turnbull and Serhiy Storchaka in [bpo-28080](https://bugs.python.org/issue?@action=redirect&bpo=28080).)

• Added ZipFile.mkdir() for creating new directories inside ZIP archives. (Contributed by Sam Ezeh in [gh-49083](https://github.com/python/cpython/issues/49083).)

• Added stem, suffix and suffixes to zipfile.Path. (Contributed by Miguel Brito in [gh-88261](https://github.com/python/cpython/issues/88261).)

## 8 Optimizations

This section covers specific optimizations independent of the Faster CPython project, which is covered in its own section.

• The compiler now optimizes simple printf-style % formatting on string literals containing only the format codes%s, %r and %a and makes it as fast as a corresponding f-string expression. (Contributed by Serhiy Storchaka in [bpo-28307](https://bugs.python.org/issue?@action=redirect&bpo=28307).)

• Integer division (//) is better tuned for optimization by compilers. It is now around 20% faster on x86-64 when dividing an int by a value smaller than 2\*\*30. (Contributed by Gregory P. Smith and Tim Peters in [gh-90564](https://github.com/python/cpython/issues/90564).)

• sum() is now nearly 30% faster for integers smaller than 2\*\*30. (Contributed by Stefan Behnel in [gh-68264](https://github.com/python/cpython/issues/68264).)

• Resizing lists is streamlined for the common case, speeding up list.append() by ≈15% and simple list comprehensions by up to 20-30% (Contributed by Dennis Sweeney in [gh-91165](https://github.com/python/cpython/issues/91165).)

• Dictionaries don’t store hash values when all keys are Unicode objects, decreasing dict size. For example, sys.getsizeof(dict.fromkeys("abcdefg")) is reduced from 352 bytes to 272 bytes (23% smaller) on 64-bit platforms. (Contributed by Inada Naoki in [bpo-46845](https://bugs.python.org/issue?@action=redirect&bpo=46845).)

• Using asyncio.DatagramProtocol is now orders of magnitude faster when transferring large files over UDP, with speeds over 100 times higher for a ≈60 MiB file. (Contributed by msoxzw in [gh-91487](https://github.com/python/cpython/issues/91487).)

• math functions comb() and perm() are now ≈10 times faster for large arguments (with a larger speedup for larger k). (Contributed by Serhiy Storchaka in [bpo-37295](https://bugs.python.org/issue?@action=redirect&bpo=37295).)

<!-- page: 18 -->

• The statistics functions mean(), variance() and stdev() now consume iterators in one pass rather than converting them to a list first. This is twice as fast and can save substantial memory. (Contributed by Raymond Hettinger in [gh-90415](https://github.com/python/cpython/issues/90415).)

• unicodedata.normalize() now normalizes pure-ASCII strings in constant time. (Contributed by Donghee Na in [bpo-44987](https://bugs.python.org/issue?@action=redirect&bpo=44987).)

## 9 Faster CPython

CPython 3.11 is an average of [25% faster](https://github.com/faster-cpython/ideas#published-results) than CPython 3.10 as measured with the [pyperformance](https://github.com/python/pyperformance) benchmark suite, when compiled with GCC on Ubuntu Linux. Depending on your workload, the overall speedup could be 10-60%.

This project focuses on two major areas in Python: Faster Startup and Faster Runtime. Optimizations not covered by this project are listed separately under Optimizations.

## 9.1 Faster Startup

**Frozen imports / Static code objects**

Python caches bytecode in the \_\_pycache\_\_ directory to speed up module loading.

Previously in 3.10, Python module execution looked like this:

```txt
Read __pycache__ -> Unmarshal -> Heap allocated code object -> Evaluate
```

In Python 3.11, the core modules essential for Python startup are “frozen”. This means that their codeobjects (and bytecode) are statically allocated by the interpreter. This reduces the steps in module execution process to:

```txt
Statically allocated code object -> Evaluate
```

Interpreter startup is now 10-15% faster in Python 3.11. This has a big impact for short-running programs using Python.

(Contributed by Eric Snow, Guido van Rossum and Kumar Aditya in many issues.)

## 9.2 Faster Runtime

## Cheaper, lazy Python frames

Python frames, holding execution information, are created whenever Python calls a Python function. The following are new frame optimizations:

• Streamlined the frame creation process.

• Avoided memory allocation by generously re-using frame space on the C stack.

• Streamlined the internal frame struct to contain only essential information. Frames previously held extra debugging and memory management information.

Old-style frame objects are now created only when requested by debuggers or by Python introspection functions such as sys.\_getframe() and inspect.currentframe(). For most user code, no frame objects are created at all. As a result, nearly all Python functions calls have sped up significantly. We measured a 3-7% speedup in pyperformance.

(Contributed by Mark Shannon in [bpo-44590](https://bugs.python.org/issue?@action=redirect&bpo=44590).)

<!-- page: 19 -->

## Inlined Python function calls

During a Python function call, Python will call an evaluating C function to interpret that function’s code. This effectively limits pure Python recursion to what’s safe for the C stack.

In 3.11, when CPython detects Python code calling another Python function, it sets up a new frame, and “jumps” to the new code inside the new frame. This avoids calling the C interpreting function altogether.

Most Python function calls now consume no C stack space, speeding them up. In simple recursive functions like fibonacci or factorial, we observed a 1.7x speedup. This also means recursive functions can recurse significantly deeper (if the user increases the recursion limit with sys.setrecursionlimit()). We measured a 1-3% improvement in pyperformance.

(Contributed by Pablo Galindo and Mark Shannon in [bpo-45256](https://bugs.python.org/issue?@action=redirect&bpo=45256).)

## PEP 659: Specializing Adaptive Interpreter

[**PEP 659**](https://peps.python.org/pep-0659/) is one of the key parts of the Faster CPython project. The general idea is that while Python is a dynamic language, most code has regions where objects and types rarely change. This concept is known as type stability.

At runtime, Python will try to look for common patterns and type stability in the executing code. Python will then replace the current operation with a more specialized one. This specialized operation uses fast paths available only to those use cases/types, which generally outperform their generic counterparts. This also brings in another concept called inline caching, where Python caches the results of expensive operations directly in the bytecode.

The specializer will also combine certain common instruction pairs into one superinstruction, reducing the overhead during execution.

Python will only specialize when it sees code that is “hot” (executed multiple times). This prevents Python from wasting time on run-once code. Python can also de-specialize when code is too dynamic or when the use changes. Specialization is attempted periodically, and specialization attempts are not too expensive, allowing specialization to adapt to new circumstances.

(PEP written by Mark Shannon, with ideas inspired by Stefan Brunthaler. See [**PEP 659**](https://peps.python.org/pep-0659/) for more information. Implementation by Mark Shannon and Brandt Bucher, with additional help from Irit Katriel and Dennis Sweeney.)

<!-- page: 20 -->

| Operation | Form | Specialization | Operation speedup (up to) | Contributor(s) |
| --- | --- | --- | --- | --- |
| Binary operations | x + x - x * x | Binary add, multiply and subtract for common types such as int, float and str take custom fast paths for their underlying types. | 10% | Mark Shannon, Donghee Na, Brandt Bucher, Dennis Sweeney |
| Sub-script | a[i] | Subscripting container types such as list, tuple and dict directly index the underlying data structures.Subscripting custom__getitem__() is also inlined similar to Inlined Python function calls. | 10-25% | Irit Katriel, Mark Shannon |
| Store subscript | a[i] = z | Similar to subscripting specialization above. | 10-25% | Dennis Sweeney |
| Calls | f(arg) C(arg) | Calls to common builtin (C) functions and types such as len() and str directly call their underlying C version.This avoids going through the internal calling convention. | 20% | Mark Shannon, Ken Jin |
| Load global variable | print len | The object's index in the globals/builtins namespace is cached. Loading globals and builtins require zero namespace lookups. | 1 | Mark Shannon |
| Load attribute | o.attr | Similar to loading global variables. The attribute's index inside the class/object's namespace is cached. In most cases, attribute loading will require zero namespace lookups. | 2 | Mark Shannon |
| Load methods for call | o.meth() | The actual address of the method is cached. Method loading now has no namespace lookups – even for classes with long inheritance chains. | 10-20% | Ken Jin, Mark Shannon |
| Store attribute | o.attr = z | Similar to load attribute optimization. | 2% in pyper-fornance | Mark Shannon |
| Un-pack Sequence | *seq | Specialized for common containers such as list and tuple. Avoids internal calling convention. | 8% | Brandt Bucher |

## 9.3 Misc

• Objects now require less memory due to lazily created object namespaces. Their namespace dictionaries now also share keys more freely. (Contributed Mark Shannon in [bpo-45340](https://bugs.python.org/issue?@action=redirect&bpo=45340) and [bpo-40116](https://bugs.python.org/issue?@action=redirect&bpo=40116).)

• “Zero-cost” exceptions are implemented, eliminating the cost of try statements when no exception is raised. (Contributed by Mark Shannon in [bpo-40222](https://bugs.python.org/issue?@action=redirect&bpo=40222).)

• A more concise representation of exceptions in the interpreter reduced the time required for catching an exception by about 10%. (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 A similar optimization already existed since Python 3.8. 3.11 specializes for more forms and reduces some overhead.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2 A similar optimization already existed since Python 3.10. 3.11 specializes for more forms. Furthermore, all attribute loads should be sped up by [bpo-45947](https://bugs.python.org/issue?@action=redirect&bpo=45947).</span></small>

<!-- page: 21 -->

• re’s regular expression matching engine has been partially refactored, and now uses computed gotos (or “threaded code”) on supported platforms. As a result, Python 3.11 executes the [pyperformance regular expression benchmarks](https://pyperformance.readthedocs.io/benchmarks.html#regex-dna) up to 10% faster than Python 3.10. (Contributed by Brandt Bucher in [gh-91404](https://github.com/python/cpython/issues/91404).)

## 9.4 FAQ

**How should I write my code to utilize these speedups?**

Write Pythonic code that follows common best practices; you don’t have to change your code. The Faster CPython project optimizes for common code patterns we observe.

## Will CPython 3.11 use more memory?

Maybe not; we don’t expect memory use to exceed 20% higher than 3.10. This is offset by memory optimizations for frame objects and object dictionaries as mentioned above.

## I don’t see any speedups in my workload. Why?

Certain code won’t have noticeable benefits. If your code spends most of its time on I/O operations, or already does most of its computation in a C extension library like NumPy, there won’t be significant speedups. This project currently benefits pure-Python workloads the most.

Furthermore, the pyperformance figures are a geometric mean. Even within the pyperformance benchmarks, certain benchmarks have slowed down slightly, while others have sped up by nearly 2x!

## Is there a JIT compiler?

No. We’re still exploring other optimizations.

## 9.5 About

Faster CPython explores optimizations for CPython. The main team is funded by Microsoft to work on this full-time. Pablo Galindo Salgado is also funded by Bloomberg LP to work on the project part-time. Finally, many contributors are volunteers from the community.

## 10 CPython bytecode changes

The bytecode now contains inline cache entries, which take the form of the newly-added CACHE instructions. Many opcodes expect to be followed by an exact number of caches, and instruct the interpreter to skip over them at runtime. Populated caches can look like arbitrary instructions, so great care should be taken when reading or modifying raw, adaptive bytecode containing quickened data.

<!-- page: 22 -->

## 10.1 New opcodes

• ASYNC\_GEN\_WRAP, RETURN\_GENERATOR and SEND, used in generators and co-routines.

• COPY\_FREE\_VARS, which avoids needing special caller-side code for closures.

• JUMP\_BACKWARD\_NO\_INTERRUPT, for use in certain loops where handling interrupts is undesirable.

• MAKE\_CELL, to create cell-objects.

• CHECK\_EG\_MATCH and PREP\_RERAISE\_STAR, to handle the new exception groups and except\* added in [**PEP 654**](https://peps.python.org/pep-0654/).

• PUSH\_EXC\_INFO, for use in exception handlers.

• RESUME, a no-op, for internal tracing, debugging and optimization checks.

## 10.2 Replaced opcodes

| Replaced Opcode(s) | New Opcode(s) | Notes |
| --- | --- | --- |
| BINARY_*INPLACE_* | BINARY_OP | Replaced all numeric binary/in-place opcodes with a single opcode |
| CALL_FUNCTIONCALL_FUNCTION_KWCALL_METHOD | CALLKW_NAMESPRECALLPUSH_NULL | Decouples argument shifting for methods from handling of keyword arguments; allows better specialization of calls |
| DUP_TOPDUP_TOP_TWO_TWOROTincROT_THREEROT_FOURROT_N | COPYSWAP | Stack manipulation instructions |
| JUMP_IF_NOT_EXC_MATCH | CHECK_EXC_MATCH | Now performs check but doesn't jump |
| JUMP_ABSOLUTEPOP_JUMP_IF_FALSEPOP_JUMP_IF_TRUE | JUMP_BACKWARDPOP_JUMP_BACKWARD_IF_*POP_JUMP_FORWARD_IF_* | See3; TRUE, FALSE, NONE and NOT_NONE variants for each direction |
|  | BEFORE_WITH | with block setup |
| SETUP_WITHSETUP_ASYNC_WITH |  |  |

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3 All jump opcodes are now relative, including the existing JUMP\_IF\_TRUE\_OR\_POP and JUMP\_IF\_FALSE\_OR\_POP. The argument is now an offset from the current instruction rather than an absolute location.</span></small>

<!-- page: 23 -->

## 10.3 Changed/removed opcodes

• Changed MATCH\_CLASS and MATCH\_KEYS to no longer push an additional boolean value to indicate success/failure. Instead, None is pushed on failure in place of the tuple of extracted values.

• Changed opcodes that work with exceptions to reflect them now being represented as one item on the stack instead of three (see [gh-89874](https://github.com/python/cpython/issues/89874)).

• Removed COPY\_DICT\_WITHOUT\_KEYS, GEN\_START, POP\_BLOCK, SETUP\_FINALLY and YIELD\_FROM.

## 11 Deprecated

This section lists Python APIs that have been deprecated in Python 3.11.

Deprecated C APIs are listed separately.

## 11.1 Language/Builtins

• Chaining classmethod descriptors (introduced in [bpo-19072](https://bugs.python.org/issue?@action=redirect&bpo=19072)) is now deprecated. It can no longer be used to wrap other descriptors such as property. The core design of this feature was flawed and caused a number of downstream problems. To “pass-through” a classmethod, consider using the \_\_wrapped\_\_ attribute that was added in Python 3.10. (Contributed by Raymond Hettinger in [gh-89519](https://github.com/python/cpython/issues/89519).)

• Octal escapes in string and bytes literals with values larger than 0o377 (255 in decimal) now produce a DeprecationWarning. In a future Python version, they will raise a SyntaxWarning and eventually a SyntaxError. (Contributed by Serhiy Storchaka in [gh-81548](https://github.com/python/cpython/issues/81548).)

• The delegation of int() to \_\_trunc\_\_() is now deprecated. Calling int(a) when type(a) implements \_\_trunc\_\_() but not \_\_int\_\_() or \_\_index\_\_() now raises a DeprecationWarning. (Contributed by Zackery Spytz in [bpo-44977](https://bugs.python.org/issue?@action=redirect&bpo=44977).)

## 11.2 Modules

• [**PEP 594**](https://peps.python.org/pep-0594/) led to the deprecations of the following modules slated for removal in Python 3.13:

| aifc | chunk | msilib | pipes | telnetlib |
| --- | --- | --- | --- | --- |
| audioop | crypt | nis | sndhdr | uu |
| cgi | imghdr | nntplib | spwd | xdrlib |
| cgitb | mailcap | ossaudiodev | sunau |  |

(Contributed by Brett Cannon in [bpo-47061](https://bugs.python.org/issue?@action=redirect&bpo=47061) and Victor Stinner in [gh-68966](https://github.com/python/cpython/issues/68966).)

• The asynchat, asyncore and smtpd modules have been deprecated since at least Python 3.6. Their documentation and deprecation warnings have now been updated to note they will be removed in Python 3.12. (Contributed by Hugo van Kemenade in [bpo-47022](https://bugs.python.org/issue?@action=redirect&bpo=47022).)

• The lib2to3 package and 2to3 tool are now deprecated and may not be able to parse Python 3.10 or newer. See [**PEP 617**](https://peps.python.org/pep-0617/), introducing the new PEG parser, for details. (Contributed by Victor Stinner in [bpo-40360](https://bugs.python.org/issue?@action=redirect&bpo=40360).)

• Undocumented modules sre\_compile, sre\_constants and sre\_parse are now deprecated. (Contributed by Serhiy Storchaka in [bpo-47152](https://bugs.python.org/issue?@action=redirect&bpo=47152).)

<!-- page: 24 -->

## 11.3 Standard Library

• The following have been deprecated in configparser since Python 3.2. Their deprecation warnings have now been updated to note they will be removed in Python 3.12:

– the configparser.SafeConfigParser class

– the configparser.ParsingError.filename property

– the configparser.RawConfigParser.readfp() method

(Contributed by Hugo van Kemenade in [bpo-45173](https://bugs.python.org/issue?@action=redirect&bpo=45173).)

• configparser.LegacyInterpolation has been deprecated in the docstring since Python 3.2, and is not listed in the configparser documentation. It now emits a DeprecationWarning and will be removed in Python 3.13. Use configparser.BasicInterpolation or configparser. ExtendedInterpolation instead. (Contributed by Hugo van Kemenade in [bpo-46607](https://bugs.python.org/issue?@action=redirect&bpo=46607).)

• The older set of importlib.resources functions were deprecated in favor of the replacements added in Python 3.9 and will be removed in a future Python version, due to not supporting resources located within package subdirectories:

– importlib.resources.contents()

– importlib.resources.is\_resource()

– importlib.resources.open\_binary()

– importlib.resources.open\_text()

– importlib.resources.read\_binary()

– importlib.resources.read\_text()

– importlib.resources.path()

• The locale.getdefaultlocale() function is deprecated and will be removed in Python 3.15. Use locale.setlocale(), locale.getpreferredencoding(False) and locale. getlocale() functions instead. (Contributed by Victor Stinner in [gh-90817](https://github.com/python/cpython/issues/90817).)

• The locale.resetlocale() function is deprecated and will be removed in Python 3.13. Use locale. setlocale(locale.LC\_ALL, "") instead. (Contributed by Victor Stinner in [gh-90817](https://github.com/python/cpython/issues/90817).)

• Stricter rules will now be applied for numerical group references and group names in regular expressions. Only sequences of ASCII digits will now be accepted as a numerical reference, and the group name in bytes patterns and replacement strings can only contain ASCII letters, digits and underscores. For now, a deprecation warning is raised for syntax violating these rules. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

• In the re module, the re.template() function and the corresponding re.TEMPLATE and re.T flags are deprecated, as they were undocumented and lacked an obvious purpose. They will be removed in Python 3.13. (Contributed by Serhiy Storchaka and Miro Hrončok in [gh-92728](https://github.com/python/cpython/issues/92728).)

• turtle.settiltangle() has been deprecated since Python 3.1; it now emits a deprecation warning and will be removed in Python 3.13. Use turtle.tiltangle() instead (it was earlier incorrectly marked as deprecated, and its docstring is now corrected). (Contributed by Hugo van Kemenade in [bpo-45837](https://bugs.python.org/issue?@action=redirect&bpo=45837).)

• typing.Text, which exists solely to provide compatibility support between Python 2 and Python 3 code, is now deprecated. Its removal is currently unplanned, but users are encouraged to use str instead wherever possible. (Contributed by Alex Waygood in [gh-92332](https://github.com/python/cpython/issues/92332).)

• The keyword argument syntax for constructing typing.TypedDict types is now deprecated. Support will be removed in Python 3.13. (Contributed by Jingchen Ye in [gh-90224](https://github.com/python/cpython/issues/90224).)

• webbrowser.MacOSX is deprecated and will be removed in Python 3.13. It is untested, undocumented, and not used by webbrowser itself. (Contributed by Donghee Na in [bpo-42255](https://bugs.python.org/issue?@action=redirect&bpo=42255).)

• The behavior of returning a value from a TestCase and IsolatedAsyncioTestCase test methods (other than the default None value) is now deprecated.

<!-- page: 25 -->

• Deprecated the following not-formally-documented unittest functions, scheduled for removal in Python 3.13:

– unittest.findTestCases()

– unittest.makeSuite()

– unittest.getTestCaseNames()

Use TestLoader methods instead:

– unittest.TestLoader.loadTestsFromModule()

– unittest.TestLoader.loadTestsFromTestCase()

– unittest.TestLoader.getTestCaseNames()

(Contributed by Erlend E. Aasland in [bpo-5846](https://bugs.python.org/issue?@action=redirect&bpo=5846).)

• unittest.TestProgram.usageExit() is marked deprecated, to be removed in 3.13. (Contributed by Carlos Damázio in [gh-67048](https://github.com/python/cpython/issues/67048).)

## 12 Pending Removal in Python 3.12

The following Python APIs have been deprecated in earlier Python releases, and will be removed in Python 3.12.

C APIs pending removal are listed separately.

• The asynchat module

• The asyncore module

• The entire distutils package

• The imp module

• The typing.io namespace

• The typing.re namespace

• cgi.log()

• importlib.find\_loader()

• importlib.abc.Loader.module\_repr()

• importlib.abc.MetaPathFinder.find\_module()

• importlib.abc.PathEntryFinder.find\_loader()

• importlib.abc.PathEntryFinder.find\_module()

• importlib.machinery.BuiltinImporter.find\_module()

• importlib.machinery.BuiltinLoader.module\_repr()

• importlib.machinery.FileFinder.find\_loader()

• importlib.machinery.FileFinder.find\_module()

• importlib.machinery.FrozenImporter.find\_module()

• importlib.machinery.FrozenLoader.module\_repr()

• importlib.machinery.PathFinder.find\_module()

• importlib.machinery.WindowsRegistryFinder.find\_module()

• importlib.util.module\_for\_loader()

• importlib.util.set\_loader\_wrapper()

• importlib.util.set\_package\_wrapper()

<!-- page: 26 -->

• pkgutil.ImpImporter

• pkgutil.ImpLoader

• pathlib.Path.link\_to()

• sqlite3.enable\_shared\_cache()

• sqlite3.OptimizedUnicode()

• PYTHONTHREADDEBUG environment variable

• The following deprecated aliases in unittest:

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

## 13 Removed

This section lists Python APIs that have been removed in Python 3.11.

Removed C APIs are listed separately.

• Removed the @asyncio.coroutine() decorator enabling legacy generator-based coroutines to be compatible with async / await code. The function has been deprecated since Python 3.8 and the removal was initially scheduled for Python 3.10. Use async def instead. (Contributed by Illia Volochii in [bpo-43216](https://bugs.python.org/issue?@action=redirect&bpo=43216).)

• Removed asyncio.coroutines.CoroWrapper used for wrapping legacy generator-based coroutine objects in the debug mode. (Contributed by Illia Volochii in [bpo-43216](https://bugs.python.org/issue?@action=redirect&bpo=43216).)

• Due to significant security concerns, the reuse\_address parameter of asyncio.loop. create\_datagram\_endpoint(), disabled in Python 3.9, is now entirely removed. This is because of the behavior of the socket option SO\_REUSEADDR in UDP. (Contributed by Hugo van Kemenade in [bpo-45129](https://bugs.python.org/issue?@action=redirect&bpo=45129).)

• Removed the binhex module, deprecated in Python 3.9. Also removed the related, similarly-deprecated binascii functions:

– binascii.a2b\_hqx()

– binascii.b2a\_hqx()

– binascii.rlecode\_hqx()

– binascii.rldecode\_hqx()

The binascii.crc\_hqx() function remains available.

(Contributed by Victor Stinner in [bpo-45085](https://bugs.python.org/issue?@action=redirect&bpo=45085).)

<!-- page: 27 -->

• Removed the distutils bdist\_msi command deprecated in Python 3.9. Use bdist\_wheel (wheel packages) instead. (Contributed by Hugo van Kemenade in [bpo-45124](https://bugs.python.org/issue?@action=redirect&bpo=45124).)

• Removed the \_\_getitem\_\_() methods of xml.dom.pulldom.DOMEventStream, wsgiref. util.FileWrapper and fileinput.FileInput, deprecated since Python 3.9. (Contributed by Hugo van Kemenade in [bpo-45132](https://bugs.python.org/issue?@action=redirect&bpo=45132).)

• Removed the deprecated gettext functions lgettext(), ldgettext(), lngettext() and ldngettext(). Also removed the bind\_textdomain\_codeset() function, the NullTranslations.output\_charset() and NullTranslations. set\_output\_charset() methods, and the codeset parameter of translation() and install(), since they are only used for the l\*gettext() functions. (Contributed by Donghee Na and Serhiy Storchaka in [bpo-44235](https://bugs.python.org/issue?@action=redirect&bpo=44235).)

• Removed from the inspect module:

– The getargspec() function, deprecated since Python 3.0; use inspect.signature() or inspect.getfullargspec() instead.

– The formatargspec() function, deprecated since Python 3.5; use the inspect.signature() function or the inspect.Signature object directly.

– The undocumented Signature.from\_builtin() and Signature.from\_function() methods, deprecated since Python 3.5; use the Signature.from\_callable() method instead.

(Contributed by Hugo van Kemenade in [bpo-45320](https://bugs.python.org/issue?@action=redirect&bpo=45320).)

• Removed the \_\_class\_getitem\_\_() method from pathlib.PurePath, because it was not used and added by mistake in previous versions. (Contributed by Nikita Sobolev in [bpo-46483](https://bugs.python.org/issue?@action=redirect&bpo=46483).)

• Removed the MailmanProxy class in the smtpd module, as it is unusable without the external mailman package. (Contributed by Donghee Na in [bpo-35800](https://bugs.python.org/issue?@action=redirect&bpo=35800).)

• Removed the deprecated split() method of \_tkinter.TkappType. (Contributed by Erlend E. Aasland in [bpo-38371](https://bugs.python.org/issue?@action=redirect&bpo=38371).)

• Removed namespace package support from unittest discovery. It was introduced in Python 3.4 but has been broken since Python 3.7. (Contributed by Inada Naoki in [bpo-23882](https://bugs.python.org/issue?@action=redirect&bpo=23882).)

• Removed the undocumented private float.\_\_set\_format\_\_() method, previously known as float. setformat\_\_() in Python 3.7. Its docstring said: “You probably don’t want to use this function. It exists mainly to be used in Python’s test suite.” (Contributed by Victor Stinner in [bpo-46852](https://bugs.python.org/issue?@action=redirect&bpo=46852).)

• The --experimental-isolated-subinterpreters configure flag (and corresponding EXPERIMENTAL\_ISOLATED\_SUBINTERPRETERS macro) have been removed.

• [Pynche](https://pypi.org/project/pynche/) — The Pythonically Natural Color and Hue Editor — has been moved out of Tools/scripts and is [being developed independently](https://gitlab.com/warsaw/pynche/-/tree/main) from the Python source tree.

## 14 Porting to Python 3.11

This section lists previously described changes and other bugfixes in the Python API that may require changes to your Python code.

Porting notes for the C API are listed separately.

• open(), io.open(), codecs.open() and fileinput.FileInput no longer accept 'U' (“universal newline”) in the file mode. In Python 3, “universal newline” mode is used by default whenever a file is opened in text mode, and the 'U' flag has been deprecated since Python 3.3. The newline parameter to these functions controls how universal newlines work. (Contributed by Victor Stinner in [bpo-37330](https://bugs.python.org/issue?@action=redirect&bpo=37330).)

• ast.AST node positions are now validated when provided to compile() and other related functions. If invalid positions are detected, a ValueError will be raised. (Contributed by Pablo Galindo in [gh-93351](https://github.com/python/cpython/issues/93351))

<!-- page: 28 -->

• Prohibited passing non-concurrent.futures.ThreadPoolExecutor executors to asyncio. loop.set\_default\_executor() following a deprecation in Python 3.8. (Contributed by Illia Volochii in [bpo-43234](https://bugs.python.org/issue?@action=redirect&bpo=43234).)

• calendar: The calendar.LocaleTextCalendar and calendar.LocaleHTMLCalendar classes now use locale.getlocale(), instead of using locale.getdefaultlocale(), if no locale is specified. (Contributed by Victor Stinner in [bpo-46659](https://bugs.python.org/issue?@action=redirect&bpo=46659).)

• The pdb module now reads the .pdbrc configuration file with the 'UTF-8' encoding. (Contributed by Srinivas Reddy Thatiparthy (                           ) in [bpo-41137](https://bugs.python.org/issue?@action=redirect&bpo=41137).)

• The population parameter of random.sample() must be a sequence, and automatic conversion of sets to lists is no longer supported. Also, if the sample size is larger than the population size, a ValueError is raised. (Contributed by Raymond Hettinger in [bpo-40465](https://bugs.python.org/issue?@action=redirect&bpo=40465).)

• The random optional parameter of random.shuffle() was removed. It was previously an arbitrary random function to use for the shuffle; now, random.random() (its previous default) will always be used.

• In re re-syntax, global inline flags (e.g. (?i)) can now only be used at the start of regular expressions. Using them elsewhere has been deprecated since Python 3.6. (Contributed by Serhiy Storchaka in [bpo-47066](https://bugs.python.org/issue?@action=redirect&bpo=47066).)

• In the re module, several long-standing bugs where fixed that, in rare cases, could cause capture groups to get the wrong result. Therefore, this could change the captured output in these cases. (Contributed by Ma Lin in [bpo-35859](https://bugs.python.org/issue?@action=redirect&bpo=35859).)

## 15 Build Changes

• CPython now has [**PEP 11**](https://peps.python.org/pep-0011/) [**Tier 3 support**](https://peps.python.org/pep-0011/#tier-3) for cross compiling to the [WebAssembly](https://webassembly.org/) platforms [Emscripten](https://emscripten.org/) (wasm32-unknown-emscripten, i.e. Python in the browser) and [WebAssembly System Interface (WASI)](https://wasi.dev/) (wasm32-unknown-wasi). The effort is inspired by previous work like [Pyodide](https://pyodide.org/). These platforms provide a limited subset of POSIX APIs; Python standard libraries features and modules related to networking, processes, threading, signals, mmap, and users/groups are not available or don’t work. (Emscripten contributed by Christian Heimes and Ethan Smith in [gh-84461](https://github.com/python/cpython/issues/84461) and WASI contributed by Christian Heimes in [gh-90473](https://github.com/python/cpython/issues/90473); platforms promoted in [gh-95085](https://github.com/python/cpython/issues/95085))

• Building CPython now requires:

– A [C11](https://en.cppreference.com/w/c/11) compiler and standard library. [Optional C11 features](https://en.wikipedia.org/wiki/C11_%28C_standard_revision%29#Optional_features) are not required. (Contributed by Victor Stinner in [bpo-46656](https://bugs.python.org/issue?@action=redirect&bpo=46656), [bpo-45440](https://bugs.python.org/issue?@action=redirect&bpo=45440) and [bpo-46640](https://bugs.python.org/issue?@action=redirect&bpo=46640).)

– Support for [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) floating point numbers. (Contributed by Victor Stinner in [bpo-46917](https://bugs.python.org/issue?@action=redirect&bpo=46917).)

• The Py\_NO\_NAN macro has been removed. Since CPython now requires IEEE 754 floats, NaN values are always available. (Contributed by Victor Stinner in [bpo-46656](https://bugs.python.org/issue?@action=redirect&bpo=46656).)

• The tkinter package now requires [Tcl/Tk](https://www.tcl.tk) version 8.5.12 or newer. (Contributed by Serhiy Storchaka in [bpo-46996](https://bugs.python.org/issue?@action=redirect&bpo=46996).)

• Build dependencies, compiler flags, and linker flags for most stdlib extension modules are now detected by **configure**. libffi, libnsl, libsqlite3, zlib, bzip2, liblzma, libcrypt, Tcl/Tk, and uuid flags are detected by [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/) (when available). tkinter now requires a pkg-config command to detect development settings for [Tcl/Tk](https://www.tcl.tk) headers and libraries. (Contributed by Christian Heimes and Erlend Egeberg Aasland in [bpo-45847](https://bugs.python.org/issue?@action=redirect&bpo=45847), [bpo-45747](https://bugs.python.org/issue?@action=redirect&bpo=45747), and [bpo-45763](https://bugs.python.org/issue?@action=redirect&bpo=45763).)

• libpython is no longer linked against libcrypt. (Contributed by Mike Gilbert in [bpo-45433](https://bugs.python.org/issue?@action=redirect&bpo=45433).)

• CPython can now be built with the [ThinLTO](https://clang.llvm.org/docs/ThinLTO.html) option via passing thin to --with-lto, i.e. --with-lto=thin. (Contributed by Donghee Na and Brett Holman in [bpo-44340](https://bugs.python.org/issue?@action=redirect&bpo=44340).)

• Freelists for object structs can now be disabled. A new **configure** option --without-freelists can be used to disable all freelists except empty tuple singleton. (Contributed by Christian Heimes in [bpo-45522](https://bugs.python.org/issue?@action=redirect&bpo=45522).)

• Modules/Setup and Modules/makesetup have been improved and tied up. Extension modules can now be built through makesetup. All except some test modules can be linked statically into a main binary

<!-- page: 29 -->

or library. (Contributed by Brett Cannon and Christian Heimes in [bpo-45548](https://bugs.python.org/issue?@action=redirect&bpo=45548), [bpo-45570](https://bugs.python.org/issue?@action=redirect&bpo=45570), [bpo-45571](https://bugs.python.org/issue?@action=redirect&bpo=45571), and [bpo-43974](https://bugs.python.org/issue?@action=redirect&bpo=43974).)

**Note:** Use the environment variables TCLTK\_CFLAGS and TCLTK\_LIBS to manually specify the location of Tcl/Tk headers and libraries. The **configure** options --with-tcltk-includes and --with-tcltk-libs have been removed.

On RHEL 7 and CentOS 7 the development packages do not provide tcl.pc and tk.pc; use TCLTK\_LIBS="-ltk8.5 -ltkstub8.5 -ltcl8.5". The directory Misc/rhel7 contains .pc files and instructions on how to build Python with RHEL 7’s and CentOS 7’s Tcl/Tk and OpenSSL.

• CPython will now use 30-bit digits by default for the Python int implementation. Previously, the default was to use 30-bit digits on platforms with SIZEOF\_VOID\_P >= 8, and 15-bit digits otherwise. It’s still possible to explicitly request use of 15-bit digits via either the --enable-big-digits option to the configure script or (for Windows) the PYLONG\_BITS\_IN\_DIGIT variable in PC/pyconfig.h, but this option may be removed at some point in the future. (Contributed by Mark Dickinson in [bpo-45569](https://bugs.python.org/issue?@action=redirect&bpo=45569).)

## 16 C API Changes

## 16.1 New Features

• Add a new PyType\_GetName() function to get type’s short name. (Contributed by Hai Shi in [bpo-42035](https://bugs.python.org/issue?@action=redirect&bpo=42035).)

• Add a new PyType\_GetQualName() function to get type’s qualified name. (Contributed by Hai Shi in [bpo-42035](https://bugs.python.org/issue?@action=redirect&bpo=42035).)

• Add new PyThreadState\_EnterTracing() and PyThreadState\_LeaveTracing() functions to the limited C API to suspend and resume tracing and profiling. (Contributed by Victor Stinner in [bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760).)

• Added the Py\_Version constant which bears the same value as PY\_VERSION\_HEX. (Contributed by Gabriele N. Tornetta in [bpo-43931](https://bugs.python.org/issue?@action=redirect&bpo=43931).)

• Py\_buffer and APIs are now part of the limited API and the stable ABI:

– PyObject\_CheckBuffer()

– PyObject\_GetBuffer()

– PyBuffer\_GetPointer()

– PyBuffer\_SizeFromFormat()

– PyBuffer\_ToContiguous()

– PyBuffer\_FromContiguous()

– PyObject\_CopyData()

– PyBuffer\_IsContiguous()

– PyBuffer\_FillContiguousStrides()

– PyBuffer\_FillInfo()

– PyBuffer\_Release()

– PyMemoryView\_FromBuffer()

– bf\_getbuffer and bf\_releasebuffer type slots

(Contributed by Christian Heimes in [bpo-45459](https://bugs.python.org/issue?@action=redirect&bpo=45459).)

<!-- page: 30 -->

• Added the PyType\_GetModuleByDef() function, used to get the module in which a method was defined, in cases where this information is not available directly (via PyCMethod). (Contributed by Petr Viktorin in [bpo-46613](https://bugs.python.org/issue?@action=redirect&bpo=46613).)

• Add new functions to pack and unpack C double (serialize and deserialize): PyFloat\_Pack2(), PyFloat\_Pack4(), PyFloat\_Pack8(), PyFloat\_Unpack2(), PyFloat\_Unpack4() and PyFloat\_Unpack8(). (Contributed by Victor Stinner in [bpo-46906](https://bugs.python.org/issue?@action=redirect&bpo=46906).)

• Add new functions to get frame object attributes: PyFrame\_GetBuiltins(), PyFrame\_GetGenerator(), PyFrame\_GetGlobals(), PyFrame\_GetLasti().

• Added two new functions to get and set the active exception instance: PyErr\_GetHandledException() and PyErr\_SetHandledException(). These are alternatives to PyErr\_SetExcInfo() and PyErr\_GetExcInfo() which work with the legacy 3-tuple representation of exceptions. (Contributed by Irit Katriel in [bpo-46343](https://bugs.python.org/issue?@action=redirect&bpo=46343).)

• Added the PyConfig.safe\_path member. (Contributed by Victor Stinner in [gh-57684](https://github.com/python/cpython/issues/57684).)

## 16.2 Porting to Python 3.11

• Some macros have been converted to static inline functions to avoid [macro pitfalls](https://gcc.gnu.org/onlinedocs/cpp/Macro-Pitfalls.html). The change should be mostly transparent to users, as the replacement functions will cast their arguments to the expected types to avoid compiler warnings due to static type checks. However, when the limited C API is set to >=3.11, these casts are not done, and callers will need to cast arguments to their expected types. See [**PEP 670**](https://peps.python.org/pep-0670/) for more details. (Contributed by Victor Stinner and Erlend E. Aasland in [gh-89653](https://github.com/python/cpython/issues/89653).)

• PyErr\_SetExcInfo() no longer uses the type and traceback arguments, the interpreter now derives those values from the exception instance (the value argument). The function still steals references of all three arguments. (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

• PyErr\_GetExcInfo() now derives the type and traceback fields of the result from the exception instance (the value field). (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

• \_frozen has a new is\_package field to indicate whether or not the frozen module is a package. Previously, a negative value in the size field was the indicator. Now only non-negative values be used for size. (Contributed by Kumar Aditya in [bpo-46608](https://bugs.python.org/issue?@action=redirect&bpo=46608).)

• \_PyFrameEvalFunction() now takes \_PyInterpreterFrame\* as its second parameter, instead of PyFrameObject\*. See [**PEP 523**](https://peps.python.org/pep-0523/) for more details of how to use this function pointer type.

• PyCode\_New() and PyCode\_NewWithPosOnlyArgs() now take an additional exception\_table argument. Using these functions should be avoided, if at all possible. To get a custom code object: create a code object using the compiler, then get a modified version with the replace method.

• PyCodeObject no longer has the co\_code, co\_varnames, co\_cellvars and co\_freevars fields. Instead, use PyCode\_GetCode(), PyCode\_GetVarnames(), PyCode\_GetCellvars() and PyCode\_GetFreevars() respectively to access them via the C API. (Contributed by Brandt Bucher in [bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841) and Ken Jin in [gh-92154](https://github.com/python/cpython/issues/92154) and [gh-94936](https://github.com/python/cpython/issues/94936).)

• The old trashcan macros (Py\_TRASHCAN\_SAFE\_BEGIN/Py\_TRASHCAN\_SAFE\_END) are now deprecated. They should be replaced by the new macros Py\_TRASHCAN\_BEGIN and Py\_TRASHCAN\_END.

A tp\_dealloc function that has the old macros, such as:

```c
static void
mytype_dealloc(mytype *p)
{
    PyObject_GC_UnTrack(p);
    Py_TRASHCAN_SAFE_BEGIN(p);
    ...
    Py_TRASHCAN_SAFE_END
}
```

<!-- page: 31 -->

should migrate to the new macros as follows:

```c
static void
mytype_dealloc(mytype *p)
{
    PyObject_GC_UnTrack(p);
    Py_TRASHCAN_BEGIN(p, mytype_dealloc)
    ...
    Py_TRASHCAN_END
}
```

Note that Py\_TRASHCAN\_BEGIN has a second argument which should be the deallocation function it is in.

To support older Python versions in the same codebase, you can define the following macros and use them throughout the code (credit: these were copied from the mypy codebase):

```m4
#if PY_VERSION_HEX >= 0x03080000
# define CPy_TRASHCAN_BEGIN(op, dealloc) Py_TRASHCAN_BEGIN(op, dealloc)
# define CPy_TRASHCAN_END(op) Py_TRASHCAN_END
#else
# define CPy_TRASHCAN_BEGIN(op, dealloc) Py_TRASHCAN_SAFE_BEGIN(op)
# define CPy_TRASHCAN_END(op) Py_TRASHCAN_SAFE_END(op)
#endif
```

• The PyType\_Ready() function now raises an error if a type is defined with the Py\_TPFLAGS\_HAVE\_GC flag set but has no traverse function (PyTypeObject.tp\_traverse). (Contributed by Victor Stinner in [bpo-44263](https://bugs.python.org/issue?@action=redirect&bpo=44263).)

• Heap types with the Py\_TPFLAGS\_IMMUTABLETYPE flag can now inherit the [**PEP 590**](https://peps.python.org/pep-0590/) vectorcall protocol. Previously, this was only possible for static types. (Contributed by Erlend E. Aasland in [bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908))

• Since Py\_TYPE() is changed to a inline static function, Py\_TYPE(obj) = new\_type must be replaced with Py\_SET\_TYPE(obj, new\_type): see the Py\_SET\_TYPE() function (available since Python 3.9). For backward compatibility, this macro can be used:

```c
#if PY_VERSION_HEX < 0x030900A4 && !defined(Py_SET_TYPE)
static inline void _Py_SET_TYPE(PyObject *ob, PyTypeObject *type)
{ ob->ob_type = type; }
#define Py_SET_TYPE(ob, type) _Py_SET_TYPE((PyObject*)(ob), type)
#endif
```

(Contributed by Victor Stinner in [bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573).)

• Since Py\_SIZE() is changed to a inline static function, Py\_SIZE(obj) = new\_size must be replaced with Py\_SET\_SIZE(obj, new\_size): see the Py\_SET\_SIZE() function (available since Python 3.9). For backward compatibility, this macro can be used:

```c
#if PY_VERSION_HEX < 0x030900A4 && !defined(Py_SET_SIZE)
static inline void _Py_SET_SIZE(PyVarObject *ob, Py_ssize_t size)
{ ob->ob_size = size; }
#define Py_SET_SIZE(ob, size) _Py_SET_SIZE((PyVarObject*)(ob), size)
#endif
```

(Contributed by Victor Stinner in [bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573).)

• &lt;Python.h&gt; no longer includes the header files &lt;stdlib.h&gt;, &lt;stdio.h&gt;, &lt;errno.h&gt; and &lt;string.h&gt; when the Py\_LIMITED\_API macro is set to 0x030b0000 (Python 3.11) or higher. C extensions should explicitly include the header files after #include &lt;Python.h&gt;. (Contributed by Victor Stinner in [bpo-45434](https://bugs.python.org/issue?@action=redirect&bpo=45434).)

• The non-limited API files cellobject.h, classobject.h, code.h, context.h, funcobject. h, genobject.h and longintrepr.h have been moved to the Include/cpython directory. Moreover, the eval.h header file was removed. These files must not be included directly, as they are already

<!-- page: 32 -->

included in Python.h: Include Files. If they have been included directly, consider including Python.h instead. (Contributed by Victor Stinner in [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134).)

• The PyUnicode\_CHECK\_INTERNED() macro has been excluded from the limited C API. It was never usable there, because it used internal structures which are not available in the limited C API. (Contributed by Victor Stinner in [bpo-46007](https://bugs.python.org/issue?@action=redirect&bpo=46007).)

• The following frame functions and type are now directly available with #include &lt;Python.h&gt;, it’s no longer needed to add #include &lt;frameobject.h&gt;:

– PyFrame\_Check()

– PyFrame\_GetBack()

– PyFrame\_GetBuiltins()

– PyFrame\_GetGenerator()

– PyFrame\_GetGlobals()

– PyFrame\_GetLasti()

– PyFrame\_GetLocals()

```txt
- PyFrame_Type
```

(Contributed by Victor Stinner in [gh-93937](https://github.com/python/cpython/issues/93937).)

• The PyFrameObject structure members have been removed from the public C API.

While the documentation notes that the PyFrameObject fields are subject to change at any time, they have been stable for a long time and were used in several popular extensions.

In Python 3.11, the frame struct was reorganized to allow performance optimizations. Some fields were removed entirely, as they were details of the old implementation.

PyFrameObject fields:

– f\_back: use PyFrame\_GetBack().

– f\_blockstack: removed.

– f\_builtins: use PyFrame\_GetBuiltins().

– f\_code: use PyFrame\_GetCode().

– f\_gen: use PyFrame\_GetGenerator().

– f\_globals: use PyFrame\_GetGlobals().

– f\_iblock: removed.

– f\_lasti: use PyFrame\_GetLasti(). Code using f\_lasti with PyCode\_Addr2Line() should use PyFrame\_GetLineNumber() instead; it may be faster.

– f\_lineno: use PyFrame\_GetLineNumber()

– f\_locals: use PyFrame\_GetLocals().

– f\_stackdepth: removed.

– f\_state: no public API (renamed to f\_frame.f\_state).

– f\_trace: no public API.

```txt
- f_trace_lines:        use     PyObject_GetAttrString((PyObject*)frame,
    "f_trace_lines").
```

```prolog
- f_trace_opcodes:      use   PyObject_GetAttrString((PyObject*)frame,
  "f_trace_opcodes").
```

– f\_localsplus: no public API (renamed to f\_frame.localsplus).

– f\_valuestack: removed.

<!-- page: 33 -->

The Python frame object is now created lazily. A side effect is that the f\_back member must not be accessed directly, since its value is now also computed lazily. The PyFrame\_GetBack() function must be called instead.

Debuggers that accessed the f\_locals directly must call PyFrame\_GetLocals() instead. They no longer need to call PyFrame\_FastToLocalsWithError() or PyFrame\_LocalsToFast(), in fact they should not call those functions. The necessary updating of the frame is now managed by the virtual machine.

Code defining PyFrame\_GetCode() on Python 3.8 and older:

```c
#if PY_VERSION_HEX < 0x030900B1
static inline PyCodeObject* PyFrame_GetCode(PyFrameObject *frame)
{
    Py_INCREF(frame->f_code);
    return frame->f_code;
}
#endif
```

Code defining PyFrame\_GetBack() on Python 3.8 and older:

```c
#if PY_VERSION_HEX < 0x030900B1
static inline PyFrameObject* PyFrame_GetBack(PyFrameObject *frame)
{
    Py_XINCREF(frame->f_back);
    return frame->f_back;
}
#endif
```

Or use the [pythoncapi\_compat project](https://github.com/python/pythoncapi-compat) to get these two functions on older Python versions.

• Changes of the PyThreadState structure members:

frame: removed, use PyThreadState\_GetFrame() (function added to Python 3.9 by [bpo-40429](https://bugs.python.org/issue?@action=redirect&bpo=40429)). Warning: the function returns a strong reference, need to call Py\_XDECREF().

– tracing: changed, use PyThreadState\_EnterTracing() and PyThreadState\_LeaveTracing() (functions added to Python 3.11 by [bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760)).

```txt
- recursion_depth: removed, use (tstate->recursion_limit - tstate->recursion_remaining) instead.
```

– stackcheck\_counter: removed.

Code defining PyThreadState\_GetFrame() on Python 3.8 and older:

```c
#if PY_VERSION_HEX < 0x030900B1
static inline PyFrameObject* PyThreadState_GetFrame(PyThreadState *tstate)
{
    Py_XINCREF(tstate->frame);
    return tstate->frame;
}
#endif
```

Code defining PyThreadState\_EnterTracing() and PyThreadState\_LeaveTracing() on Python 3.10 and older:

```c
#if PY_VERSION_HEX < 0x030B00A2
static inline void PyThreadState_EnterTracing(PyThreadState *tstate)
{
    tstate->tracing++;
#if PY_VERSION_HEX >= 0x030A00A1
    tstate->cframe->use_tracing = 0;
#else
    tstate->use_tracing = 0;
```

(continues on next page)

<!-- page: 34 -->

(continued from previous page)

```c
#endif
}

static inline void PyThreadState_LeaveTracing(PyThreadState *tstate)
{
    int use_tracing = (tstate->c_tracefunc != NULL || tstate->c_profilefunc != NULL);
    tstate->tracing--;
#if PY_VERSION_HEX >= 0x030A00A1
    tstate->cframe->use_tracing = use_tracing;
#else
    tstate->use_tracing = use_tracing;
#endif
}
#endif
```

Or use [the pythoncapi-compat project](https://github.com/python/pythoncapi-compat) to get these functions on old Python functions.

• Distributors are encouraged to build Python with the optimized Blake2 library [libb2](https://www.blake2.net/).

• The PyConfig.module\_search\_paths\_set field must now be set to 1 for initialization to use PyConfig.module\_search\_paths to initialize sys.path. Otherwise, initialization will recalculate the path and replace any values added to module\_search\_paths.

• PyConfig\_Read() no longer calculates the initial search path, and will not fill any values into PyConfig. module\_search\_paths. To calculate default paths and then modify them, finish initialization and use PySys\_GetObject() to retrieve sys.path as a Python list object and modify it directly.

## 16.3 Deprecated

• Deprecate the following functions to configure the Python initialization:

– PySys\_AddWarnOptionUnicode()

– PySys\_AddWarnOption()

– PySys\_AddXOption()

– PySys\_HasWarnOptions()

– PySys\_SetArgvEx()

– PySys\_SetArgv()

– PySys\_SetPath()

– Py\_SetPath()

– Py\_SetProgramName()

– Py\_SetPythonHome()

– Py\_SetStandardStreamEncoding()

```txt
- _Py_SetProgramFullPath()
```

Use the new PyConfig API of the Python Initialization Configuration instead ([**PEP 587**](https://peps.python.org/pep-0587/)). (Contributed by Victor Stinner in [gh-88279](https://github.com/python/cpython/issues/88279).)

• Deprecate the ob\_shash member of the PyBytesObject. Use PyObject\_Hash() instead. (Contributed by Inada Naoki in [bpo-46864](https://bugs.python.org/issue?@action=redirect&bpo=46864).)

<!-- page: 35 -->

## 16.4 Pending Removal in Python 3.12

The following C APIs have been deprecated in earlier Python releases, and will be removed in Python 3.12.

• PyUnicode\_AS\_DATA()

• PyUnicode\_AS\_UNICODE()

• PyUnicode\_AsUnicodeAndSize()

• PyUnicode\_AsUnicode()

• PyUnicode\_FromUnicode()

• PyUnicode\_GET\_DATA\_SIZE()

• PyUnicode\_GET\_SIZE()

• PyUnicode\_GetSize()

• PyUnicode\_IS\_COMPACT()

• PyUnicode\_IS\_READY()

• PyUnicode\_READY()

• PyUnicode\_WSTR\_LENGTH()

• \_PyUnicode\_AsUnicode()

• PyUnicode\_WCHAR\_KIND

• PyUnicodeObject

• PyUnicode\_InternImmortal()

## 16.5 Removed

• PyFrame\_BlockSetup() and PyFrame\_BlockPop() have been removed. (Contributed by Mark Shannon in [bpo-40222](https://bugs.python.org/issue?@action=redirect&bpo=40222).)

• Remove the following math macros using the errno variable:

– Py\_ADJUST\_ERANGE1()

– Py\_ADJUST\_ERANGE2()

– Py\_OVERFLOWED()

– Py\_SET\_ERANGE\_IF\_OVERFLOW()

– Py\_SET\_ERRNO\_ON\_MATH\_ERROR()

(Contributed by Victor Stinner in [bpo-45412](https://bugs.python.org/issue?@action=redirect&bpo=45412).)

• Remove Py\_UNICODE\_COPY() and Py\_UNICODE\_FILL() macros, deprecated since Python 3.3. Use PyUnicode\_CopyCharacters() or memcpy() (wchar\_t\* string), and PyUnicode\_Fill() functions instead. (Contributed by Victor Stinner in [bpo-41123](https://bugs.python.org/issue?@action=redirect&bpo=41123).)

• Remove the pystrhex.h header file. It only contains private functions. C extensions should only include the main &lt;Python.h&gt; header file. (Contributed by Victor Stinner in [bpo-45434](https://bugs.python.org/issue?@action=redirect&bpo=45434).)

• Remove the Py\_FORCE\_DOUBLE() macro. It was used by the Py\_IS\_INFINITY() macro. (Contributed by Victor Stinner in [bpo-45440](https://bugs.python.org/issue?@action=redirect&bpo=45440).)

• The following items are no longer available when Py\_LIMITED\_API is defined:

– PyMarshal\_WriteLongToFile()

– PyMarshal\_WriteObjectToFile()

– PyMarshal\_ReadObjectFromString()

<!-- page: 36 -->

– PyMarshal\_WriteObjectToString()

– the Py\_MARSHAL\_VERSION macro

These are not part of the limited API.

(Contributed by Victor Stinner in [bpo-45474](https://bugs.python.org/issue?@action=redirect&bpo=45474).)

• Exclude PyWeakref\_GET\_OBJECT() from the limited C API. It never worked since the PyWeakReference structure is opaque in the limited C API. (Contributed by Victor Stinner in [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134).)

• Remove the PyHeapType\_GET\_MEMBERS() macro. It was exposed in the public C API by mistake, it must only be used by Python internally. Use the PyTypeObject.tp\_members member instead. (Contributed by Victor Stinner in [bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170).)

• Remove the HAVE\_PY\_SET\_53BIT\_PRECISION macro (moved to the internal C API). (Contributed by Victor Stinner in [bpo-45412](https://bugs.python.org/issue?@action=redirect&bpo=45412).)

• Remove the Py\_UNICODE encoder APIs, as they have been deprecated since Python 3.3, are little used and are inefficient relative to the recommended alternatives.

The removed functions are:

– PyUnicode\_Encode()

– PyUnicode\_EncodeASCII()

– PyUnicode\_EncodeLatin1()

– PyUnicode\_EncodeUTF7()

– PyUnicode\_EncodeUTF8()

– PyUnicode\_EncodeUTF16()

– PyUnicode\_EncodeUTF32()

– PyUnicode\_EncodeUnicodeEscape()

– PyUnicode\_EncodeRawUnicodeEscape()

– PyUnicode\_EncodeCharmap()

– PyUnicode\_TranslateCharmap()

– PyUnicode\_EncodeDecimal()

– PyUnicode\_TransformDecimalToASCII()

See [**PEP 624**](https://peps.python.org/pep-0624/) for details and [**migration guidance**](https://peps.python.org/pep-0624/#alternative-apis). (Contributed by Inada Naoki in [bpo-44029](https://bugs.python.org/issue?@action=redirect&bpo=44029).)

## 17 Notable Changes in 3.11.4

## 17.1 tarfile

• The extraction methods in tarfile, and shutil.unpack\_archive(), have a new a filter argument that allows limiting tar features than may be surprising or dangerous, such as creating files outside the destination directory. See tarfile-extraction-filter for details. In Python 3.12, use without the filter argument will show a DeprecationWarning. In Python 3.14, the default will switch to 'data'. (Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)

<!-- page: 37 -->

## 18 Notable Changes in 3.11.5

## 18.1 OpenSSL

• Windows builds and macOS installers from python.org now use OpenSSL 3.0.

## 19 Notable changes in 3.11.10

## 19.1 ipaddress

• Fixed is\_global and is\_private behavior in IPv4Address, IPv6Address, IPv4Network and IPv6Network.

## 19.2 email

• Headers with embedded newlines are now quoted on output.

The generator will now refuse to serialize (write) headers that are improperly folded or delimited, such that they would be parsed as multiple headers or joined with adjacent data. If you need to turn this safety feature off, set verify\_generated\_headers. (Contributed by Bas Bloemsaat and Petr Viktorin in [gh-121650](https://github.com/python/cpython/issues/121650).)

• email.utils.getaddresses() and email.utils.parseaddr() now return ('', '') 2- tuples in more situations where invalid email addresses are encountered, instead of potentially inaccurate values. An optional strict parameter was added to these two functions: use strict=False to get the old behavior, accepting malformed inputs. getattr(email.utils, 'supports\_strict\_parsing', False) can be used to check if the strict paramater is available. (Contributed by Thomas Dwyer and Victor Stinner for [gh-102988](https://github.com/python/cpython/issues/102988) to improve the CVE-2023-27043 fix.)

<!-- page: 38 -->

## Index

## E

## P

environment variable PYTHONNODEBUGRANGES, 4 PYTHONSAFEPATH, 3, 8 PYTHONTHREADDEBUG, 26

Python Enhancement Proposals PEP 11, 28 PEP 11#tier-3, 28 PEP 484, 5 PEP 484#annotating-instance-and-class-methods, 6 PEP 514, 5 PEP 515, 11 PEP 523, 30 PEP 552, 8 PEP 563, 8 PEP 587, 34 PEP 590, 31 PEP 594, 3, 23 PEP 617, 23 PEP 624, 3, 36 PEP 624#alternative-apis, 36 PEP 646, 5 PEP 654, 5, 22 PEP 655, 6 PEP 657, 4, 12 PEP 659, 19 PEP 670, 3, 30 PEP 673, 6 PEP 675, 7 PEP 678, 5 PEP 680, 3, 9 PEP 681, 7 PEP 682, 8 PEP 706, 36 PEP 3333, 9 PYTHONNODEBUGRANGES, 4 PYTHONSAFEPATH, 3, 8 PYTHONTHREADDEBUG, 26

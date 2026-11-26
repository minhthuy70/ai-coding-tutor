<!-- page: 1 -->
# EN_PY_065: Customizing Attribute Access: __getattr__, __getattribute__, __setattr__, __dir__

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Advanced OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

| type.__bases__                                     | A "tuple" containing the class’s bases. In most    |
|                                                    | cases, for a class defined as "class X(A, B, C)",  |
|                                                    | "X.__bases__" will be exactly equal to "(A, B,     |
|                                                    | C)".                                               |
+----------------------------------------------------+----------------------------------------------------+
| type.__doc__                                       | The class’s documentation string, or "None" if     |
|                                                    | undefined. Not inherited by subclasses.            |
+----------------------------------------------------+----------------------------------------------------+
| type.__annotations__                               | A dictionary containing *variable annotations*     |
|                                                    | collected during class body execution. For best    |
|                                                    | practices on working with "__annotations__",       |
|                                                    | please see Annotations Best Practices.  Caution:   |
|                                                    | Accessing the "__annotations__" attribute of a     |
|                                                    | class object directly may yield incorrect results  |
|                                                    | in the presence of metaclasses. In addition, the   |
|                                                    | attribute may not exist for some classes. Use      |
|                                                    | "inspect.get_annotations()" to retrieve class      |
|                                                    | annotations safely.                                |
+----------------------------------------------------+----------------------------------------------------+
| type.__type_params__                               | A "tuple" containing the type parameters of a      |
|                                                    | generic class.  Added in version 3.12.             |
+----------------------------------------------------+----------------------------------------------------+
| type.__mro__                                       | The "tuple" of classes that are considered when    |
|                                                    | looking for base classes during method resolution. |
+----------------------------------------------------+----------------------------------------------------+


3.2.10.2. Special methods
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the special attributes described above, all Python
classes also have the following two methods available:

type.mro()

<!-- page: 2 -->


```python
This method can be overridden by a metaclass to customize the
method resolution order for its instances.  It is called at class
instantiation, and its result is stored in "__mro__".

```
type.__subclasses__()

```python
Each class keeps a list of weak references to its immediate
subclasses. This method returns a list of all those references
still alive. The list is in definition order. Example:

   >>> class A: pass
   >>> class B(A): pass
   >>> A.__subclasses__()
   [<class 'B'>]


```
3.2.11. Class instances
-----------------------

A class instance is created by calling a class object (see above).  A
class instance has a namespace implemented as a dictionary which is
the first place in which attribute references are searched.  When an
attribute is not found there, and the instance’s class has an
attribute by that name, the search continues with the class
attributes.  If a class attribute is found that is a user-defined
function object, it is transformed into an instance method object
whose "__self__" attribute is the instance.  Static method and class
method objects are also transformed; see above under “Classes”.  See
section Implementing Descriptors for another way in which attributes
of a class retrieved via its instances may differ from the objects
actually stored in the class’s "__dict__".  If no class attribute is
found, and the object’s class has a "__getattr__()" method, that is
called to satisfy the lookup.

Attribute assignments and deletions update the instance’s dictionary,
never a class’s dictionary.  If the class has a "__setattr__()" or
"__delattr__()" method, this is called instead of updating the
instance dictionary directly.

Class instances can pretend to be numbers, sequences, or mappings if

<!-- page: 3 -->

they have methods with certain special names.  See section Special
method names.


3.2.11.1. Special attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

object.__class__

```python
The class to which a class instance belongs.

```
object.__dict__

   A dictionary or other mapping object used to store an object’s
   (writable) attributes. Not all instances have a "__dict__"
```python
attribute; see the section on __slots__ for more details.


```
3.2.12. I/O objects (also known as file objects)
------------------------------------------------

A *file object* represents an open file.  Various shortcuts are
available to create file objects: the "open()" built-in function, and
also "os.popen()", "os.fdopen()", and the "makefile()" method of
socket objects (and perhaps by other functions or methods provided by
extension modules).

The objects "sys.stdin", "sys.stdout" and "sys.stderr" are initialized
to file objects corresponding to the interpreter’s standard input,
output and error streams; they are all open in text mode and therefore
follow the interface defined by the "io.TextIOBase" abstract class.


3.2.13. Internal types
----------------------

A few types used internally by the interpreter are exposed to the
user. Their definitions may change with future versions of the
interpreter, but they are mentioned here for completeness.



<!-- page: 4 -->

3.2.13.1. Code objects
~~~~~~~~~~~~~~~~~~~~~~

Code objects represent *byte-compiled* executable Python code, or
*bytecode*. The difference between a code object and a function object
is that the function object contains an explicit reference to the
function’s globals (the module in which it was defined), while a code
object contains no context; also the default argument values are
stored in the function object, not in the code object (because they
represent values calculated at run-time).  Unlike function objects,
code objects are immutable and contain no references (directly or
indirectly) to mutable objects.


3.2.13.1.1. Special read-only attributes
""""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_name                                 | The function name                                  |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_qualname                             | The fully qualified function name  Added in        |
|                                                    | version 3.11.                                      |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_argcount                             | The total number of positional *parameters*        |
|                                                    | (including positional-only parameters and          |
|                                                    | parameters with default values) that the function  |
|                                                    | has                                                |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_posonlyargcount                      | The number of positional-only *parameters*         |
|                                                    | (including arguments with default values) that the |
|                                                    | function has                                       |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_kwonlyargcount                       | The number of keyword-only *parameters* (including |
|                                                    | arguments with default values) that the function   |
|                                                    | has                                                |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_nlocals                              | The number of local variables used by the function |
|                                                    | (including parameters)                             |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_varnames                             | A "tuple" containing the names of the local        |
|                                                    | variables in the function (starting with the       |
|                                                    | parameter names)                                   |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_cellvars                             | A "tuple" containing the names of local variables  |
|                                                    | that are referenced by nested functions inside the |

<!-- page: 5 -->

|                                                    | function                                           |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_freevars                             | A "tuple" containing the names of free variables   |
|                                                    | in the function                                    |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_code                                 | A string representing the sequence of *bytecode*   |
|                                                    | instructions in the function                       |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_consts                               | A "tuple" containing the literals used by the      |
|                                                    | *bytecode* in the function                         |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_names                                | A "tuple" containing the names used by the         |
|                                                    | *bytecode* in the function                         |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_filename                             | The name of the file from which the code was       |
|                                                    | compiled                                           |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_firstlineno                          | The line number of the first line of the function  |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_lnotab                               | A string encoding the mapping from *bytecode*      |
|                                                    | offsets to line numbers. For details, see the      |
|                                                    | source code of the interpreter.  Deprecated since  |
|                                                    | version 3.12: This attribute of code objects is    |
|                                                    | deprecated, and may be removed in Python 3.15.     |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_stacksize                            | The required stack size of the code object         |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_flags                                | An "integer" encoding a number of flags for the    |
|                                                    | interpreter.                                       |
+----------------------------------------------------+----------------------------------------------------+

The following flag bits are defined for "co_flags": bit "0x04" is set
if the function uses the "*arguments" syntax to accept an arbitrary
number of positional arguments; bit "0x08" is set if the function uses
the "**keywords" syntax to accept arbitrary keyword arguments; bit
"0x20" is set if the function is a generator. See Code Objects Bit
Flags for details on the semantics of each flags that might be
present.

Future feature declarations ("from __future__ import division") also
use bits in "co_flags" to indicate whether a code object was compiled
with a particular feature enabled: bit "0x2000" is set if the function
was compiled with future division enabled; bits "0x10" and "0x1000"
were used in earlier versions of Python.


<!-- page: 6 -->

Other bits in "co_flags" are reserved for internal use.

If a code object represents a function, the first item in "co_consts"
is the documentation string of the function, or "None" if undefined.


3.2.13.1.2. Methods on code objects
"""""""""""""""""""""""""""""""""""

codeobject.co_positions()

   Returns an iterable over the source code positions of each
   *bytecode* instruction in the code object.

   The iterator returns "tuple"s containing the "(start_line,
   end_line, start_column, end_column)". The *i-th* tuple corresponds
   to the position of the source code that compiled to the *i-th* code
   unit. Column information is 0-indexed utf-8 byte offsets on the
   given source line.

   This positional information can be missing. A non-exhaustive lists
   of cases where this may happen:

```python
* Running the interpreter with "-X" "no_debug_ranges".

* Loading a pyc file compiled while using "-X" "no_debug_ranges".

* Position tuples corresponding to artificial instructions.

* Line and column numbers that can’t be represented due to
  implementation specific limitations.

When this occurs, some or all of the tuple elements can be "None".

Added in version 3.11.

Note:

  This feature requires storing column positions in code objects
  which may result in a small increase of disk usage of compiled
  Python files or interpreter memory usage. To avoid storing the
  extra information and/or deactivate printing the extra traceback
  information, the "-X" "no_debug_ranges" command line flag or the
  "PYTHONNODEBUGRANGES" environment variable can be used.
```

<!-- page: 7 -->

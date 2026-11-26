# EN_PY_063: Special Method Names (Dunders): __new__, __init__, and __del__ Lifecycle

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Magic Methods | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

|                                                    | function’s global variables – the global namespace |
|                                                    | of the module in which the function was defined.   |
+----------------------------------------------------+----------------------------------------------------+
| function.__closure__                               | "None" or a "tuple" of cells that contain bindings |
|                                                    | for the function’s free variables.  A cell object  |
|                                                    | has the attribute "cell_contents". This can be     |
|                                                    | used to get the value of the cell, as well as set  |
|                                                    | the value.                                         |
+----------------------------------------------------+----------------------------------------------------+

3.2.8.1.2. Special writable attributes
""""""""""""""""""""""""""""""""""""""

Most of these attributes check the type of the assigned value:

+----------------------------------------------------+----------------------------------------------------+
| Attribute                                          | Meaning                                            |
|====================================================|====================================================|
| function.__doc__                                   | The function’s documentation string, or "None" if  |
|                                                    | unavailable.                                       |
+----------------------------------------------------+----------------------------------------------------+
| function.__name__                                  | The function’s name. See also: "__name__           |
|                                                    | attributes".                                       |
+----------------------------------------------------+----------------------------------------------------+
| function.__qualname__                              | The function’s *qualified name*. See also:         |
|                                                    | "__qualname__ attributes".  Added in version 3.3.  |
+----------------------------------------------------+----------------------------------------------------+
| function.__module__                                | The name of the module the function was defined    |
|                                                    | in, or "None" if unavailable.                      |
+----------------------------------------------------+----------------------------------------------------+
| function.__defaults__                              | A "tuple" containing default *parameter* values    |
|                                                    | for those parameters that have defaults, or "None" |
|                                                    | if no parameters have a default value.             |

+----------------------------------------------------+----------------------------------------------------+
| function.__code__                                  | The code object representing the compiled function |
|                                                    | body.                                              |
+----------------------------------------------------+----------------------------------------------------+
| function.__dict__                                  | The namespace supporting arbitrary function        |
|                                                    | attributes. See also: "__dict__ attributes".       |
+----------------------------------------------------+----------------------------------------------------+
| function.__annotations__                           | A "dictionary" containing annotations of           |
|                                                    | *parameters*. The keys of the dictionary are the   |
|                                                    | parameter names, and "'return'" for the return     |
|                                                    | annotation, if provided. See also: Annotations     |
|                                                    | Best Practices.                                    |
+----------------------------------------------------+----------------------------------------------------+
| function.__kwdefaults__                            | A "dictionary" containing defaults for keyword-    |
|                                                    | only *parameters*.                                 |
+----------------------------------------------------+----------------------------------------------------+
| function.__type_params__                           | A "tuple" containing the type parameters of a      |
|                                                    | generic function.  Added in version 3.12.          |
+----------------------------------------------------+----------------------------------------------------+

Function objects also support getting and setting arbitrary
attributes, which can be used, for example, to attach metadata to
functions.  Regular attribute dot-notation is used to get and set such
attributes.

**CPython implementation detail:** CPython’s current implementation
only supports function attributes on user-defined functions. Function
attributes on built-in functions may be supported in the future.

Additional information about a function’s definition can be retrieved
from its code object (accessible via the "__code__" attribute).

3.2.8.2. Instance methods
~~~~~~~~~~~~~~~~~~~~~~~~~

An instance method object combines a class, a class instance and any
callable object (normally a user-defined function).

Special read-only attributes:

+----------------------------------------------------+----------------------------------------------------+
| method.__self__                                    | Refers to the class instance object to which the   |
|                                                    | method is bound                                    |
+----------------------------------------------------+----------------------------------------------------+

| method.__func__                                    | Refers to the original function object             |
+----------------------------------------------------+----------------------------------------------------+
| method.__doc__                                     | The method’s documentation (same as                |
|                                                    | "method.__func__.__doc__"). A "string" if the      |
|                                                    | original function had a docstring, else "None".    |
+----------------------------------------------------+----------------------------------------------------+
| method.__name__                                    | The name of the method (same as                    |
|                                                    | "method.__func__.__name__")                        |
+----------------------------------------------------+----------------------------------------------------+
| method.__module__                                  | The name of the module the method was defined in,  |
|                                                    | or "None" if unavailable.                          |
+----------------------------------------------------+----------------------------------------------------+

Methods also support accessing (but not setting) the arbitrary
function attributes on the underlying function object.

User-defined method objects may be created when getting an attribute
of a class (perhaps via an instance of that class), if that attribute
is a user-defined function object or a "classmethod" object.

When an instance method object is created by retrieving a user-defined
function object from a class via one of its instances, its "__self__"
attribute is the instance, and the method object is said to be
*bound*.  The new method’s "__func__" attribute is the original
function object.

When an instance method object is created by retrieving a
"classmethod" object from a class or instance, its "__self__"
attribute is the class itself, and its "__func__" attribute is the
function object underlying the class method.

When an instance method object is called, the underlying function
("__func__") is called, inserting the class instance ("__self__") in
front of the argument list.  For instance, when "C" is a class which
contains a definition for a function "f()", and "x" is an instance of
"C", calling "x.f(1)" is equivalent to calling "C.f(x, 1)".

When an instance method object is derived from a "classmethod" object,
the “class instance” stored in "__self__" will actually be the class
itself, so that calling either "x.f(1)" or "C.f(1)" is equivalent to
calling "f(C,1)" where "f" is the underlying function.

It is important to note that user-defined functions which are
attributes of a class instance are not converted to bound methods;
this *only* happens when the function is an attribute of the class.

3.2.8.3. Generator functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function or method which uses the "yield" statement (see section The
yield statement) is called a *generator function*.  Such a function,
when called, always returns an *iterator* object which can be used to
execute the body of the function:  calling the iterator’s
"iterator.__next__()" method will cause the function to execute until
it provides a value using the "yield" statement.  When the function
executes a "return" statement or falls off the end, a "StopIteration"
exception is raised and the iterator will have reached the end of the
set of values to be returned.

3.2.8.4. Coroutine functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function or method which is defined using "async def" is called a
*coroutine function*.  Such a function, when called, returns a
*coroutine* object.  It may contain "await" expressions, as well as
"async with" and "async for" statements. See also the Coroutine
Objects section.

3.2.8.5. Asynchronous generator functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function or method which is defined using "async def" and which uses
the "yield" statement is called a *asynchronous generator function*.
Such a function, when called, returns an *asynchronous iterator*
object which can be used in an "async for" statement to execute the
body of the function.

Calling the asynchronous iterator’s "aiterator.__anext__" method will
return an *awaitable* which when awaited will execute until it
provides a value using the "yield" expression.  When the function
executes an empty "return" statement or falls off the end, a
"StopAsyncIteration" exception is raised and the asynchronous iterator
will have reached the end of the set of values to be yielded.

3.2.8.6. Built-in functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A built-in function object is a wrapper around a C function.  Examples
of built-in functions are "len()" and "math.sin()" ("math" is a
standard built-in module). The number and type of the arguments are
determined by the C function. Special read-only attributes:

* "__doc__" is the function’s documentation string, or "None" if
  unavailable. See "function.__doc__".

* "__name__" is the function’s name. See "function.__name__".

* "__self__" is set to "None" (but see the next item).

* "__module__" is the name of the module the function was defined in
  or "None" if unavailable. See "function.__module__".

3.2.8.7. Built-in methods
~~~~~~~~~~~~~~~~~~~~~~~~~

This is really a different disguise of a built-in function, this time
containing an object passed to the C function as an implicit extra
argument.  An example of a built-in method is "alist.append()",
assuming *alist* is a list object. In this case, the special read-only
attribute "__self__" is set to the object denoted by *alist*. (The
attribute has the same semantics as it does with "other instance
methods".)

3.2.8.8. Classes
~~~~~~~~~~~~~~~~

Classes are callable.  These objects normally act as factories for new
instances of themselves, but variations are possible for class types
that override "__new__()".  The arguments of the call are passed to
"__new__()" and, in the typical case, to "__init__()" to initialize
the new instance.

3.2.8.9. Class Instances
~~~~~~~~~~~~~~~~~~~~~~~~

Instances of arbitrary classes can be made callable by defining a
"__call__()" method in their class.

3.2.9. Modules
--------------

Modules are a basic organizational unit of Python code, and are
created by the import system as invoked either by the "import"
statement, or by calling functions such as "importlib.import_module()"
and built-in "__import__()".  A module object has a namespace
implemented by a "dictionary" object (this is the dictionary
referenced by the "__globals__" attribute of functions defined in the
module).  Attribute references are translated to lookups in this
dictionary, e.g., "m.x" is equivalent to "m.__dict__["x"]". A module
object does not contain the code object used to initialize the module
(since it isn’t needed once the initialization is done).

Attribute assignment updates the module’s namespace dictionary, e.g.,
"m.x = 1" is equivalent to "m.__dict__["x"] = 1".

3.2.9.1. Import-related attributes on module objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module objects have the following attributes that relate to the import
system. When a module is created using the machinery associated with
the import system, these attributes are filled in based on the
module’s *spec*, before the *loader* executes and loads the module.

To create a module dynamically rather than using the import system,
it’s recommended to use "importlib.util.module_from_spec()", which
will set the various import-controlled attributes to appropriate
values. It’s also possible to use the "types.ModuleType" constructor
to create modules directly, but this technique is more error-prone, as
most attributes must be manually set on the module object after it has
been created when using this approach.

Caution:

  With the exception of "__name__", it is **strongly** recommended
  that you rely on "__spec__" and its attributes instead of any of the
  other individual attributes listed in this subsection. Note that
  updating an attribute on "__spec__" will not update the
  corresponding attribute on the module itself:

```python
>>> import typing
>>> typing.__name__, typing.__spec__.name
('typing', 'typing')
```
**The Python/C API**

**Release 3.10.15**

**Guido van Rossum**

**and the Python development team**

**September 09, 2024**

**Python Software Foundation Email: docs@python.org**

## CONTENTS

- **1 Introduction** 3
- 1.1 Coding standards 3
- 1.2 Include Files 3
- 1.3 Useful macros 4
- 1.4 Objects, Types and Reference Counts 6
- 1.4.1 Reference Counts 6
- 1.4.2 Types 9
- 1.5 Exceptions 9
- 1.6 Embedding Python 11
- 1.7 Debugging Builds 12
- **2 C API Stability 13**
- 2.1 Stable Application Binary Interface 13
- 2.1.1 Limited API Scope and Performance 14
- 2.1.2 Limited API Caveats 14
- 2.2 Platform Considerations 14
- 2.3 Contents of Limited API 15
- **3 The Very High Level Layer 39**
- **4 Reference Counting 43**
- **5 Exception Handling 45**
- 5.1 Printing and clearing 45
- 5.2 Raising exceptions 46
- 5.3 Issuing warnings 48
- 5.4 Querying the error indicator 49
- 5.5 Signal Handling 51
- 5.6 Exception Classes 52
- 5.7 Exception Objects 52
- 5.8 Unicode Exception Objects 53
- 5.9 Recursion Control 54
- 5.10 Standard Exceptions 55
- 5.11 Standard Warning Categories 56
- 6 **Utilities 57**
- 6.1 Operating System Utilities 57
- 6.2 System Functions 59
- 6.3 Process Control 61
- 6.4 Importing Modules 62
- 6.5 Data marshalling support 65
- 6.6 Parsing arguments and building values 66
- 6.6.1 Parsing arguments 66
- 6.6.2 Building values 72
- 6.7 String conversion and formatting 74

- 6.8 Reflection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
- 6.9 Codec registry and support functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
- 6.9.1 Codec lookup API . . . . . . . . . . . . . . . . . . . . 76
- 6.9.2 Registry API for Unicode encoding error handlers . . . . . . . . . . 77
- 7 **Abstract Objects Layer**
- 7.1 Object Protocol . . . . . . . . . . . . . . . . **79**
- 7.2 Call Protocol
- 7.2.1 The tp\_call Protocol
- 7.2.2 The Vectorcall Protocol
- 7.2.3 Object Calling API
- 7.2.4 Call Support API
- 7.3 Number Protocol
- 7.4 Sequence Protocol
- 7.5 Mapping Protocol
- 7.6 Iterator Protocol
- 7.7 Buffer Protocol
- 7.7.1 Buffer structure
- 7.7.2 Buffer request types
- 7.7.3 Complex arrays
- 7.7.4 Buffer-related functions
- 7.8 Old Buffer Protocol
- **8 Concrete Objects Layer**
- 8.1 Fundamental Objects
- 8.1.1 Type Objects
- 8.1.2 The None Object
- 8.2 Numeric Objects
- 8.2.1 Integer Objects
- 8.2.2 Boolean Objects
- 8.2.3 Floating Point Objects
- 8.2.4 Complex Number Objects
- 8.3 Sequence Objects
- 8.3.1 Bytes Objects
- 8.3.2 Byte Array Objects
- 8.3.3 Unicode Objects and Codecs
- 8.3.4 Tuple Objects
- 8.3.5 Struct Sequence Objects
- 8.3.6 List Objects
- 8.4 Container Objects
- 8.4.1 Dictionary Objects
- 8.4.2 Set Objects
- 8.5 Function Objects
- 8.5.1 Function Objects
- 8.5.2 Instance Method Objects
- 8.5.3 Method Objects
- 8.5.4 Cell Objects
- 8.5.5 Code Objects
- 8.6 Other Objects
- 8.6.1 File Objects
- 8.6.2 Module Objects
- 8.6.3 Iterator Objects
- 8.6.4 Descriptor Objects
- 8.6.5 Slice Objects
- 8.6.6 Ellipsis Object
- 8.6.7 MemoryView objects
- 8.6.8 Weak Reference Objects
- 8.6.9 Capsules

- **9 Initialization, Finalization, and Threads** ..... **165**

- **10 Python Initialization Configuration** ..... **185**

- **11 Memory Management** ..... **205**

- **12 Object Implementation Support** ..... **215**

- 12.2.2 Implementing functions and methods 217
- 12.2.3 Accessing attributes of extension types 220
- 12.3 Type Objects 221
- 12.3.1 Quick Reference 222
- 12.3.2 PyTypeObject Definition 226
- 12.3.3 PyObject Slots 227
- 12.3.4 PyVarObject Slots 228
- 12.3.5 PyTypeObject Slots 228
- 12.3.6 Static Types 245
- 12.3.7 Heap Types 245
- 12.4 Number Object Structures 246
- 12.5 Mapping Object Structures 248
- 12.6 Sequence Object Structures 248
- 12.7 Buffer Object Structures 249
- 12.8 Async Object Structures 250
- 12.9 Slot Type typedefs 251
- 12.10 Examples 252
- 12.11 Supporting Cyclic Garbage Collection 254
- 12.11.1 Controlling the Garbage Collector State 256
- **13 API and ABI Versioning 259**
- **A Glossary 261**
- **B About these documents 275**
- B.1 Contributors to the Python Documentation 275
- **C History and License 277**
- C.1 History of the software 277
- C.2 Terms and conditions for accessing or otherwise using Python 278
- C.2.1 PSF LICENSE AGREEMENT FOR PYTHON 3.10.15 278
- C.2.2 BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0 279
- C.2.3 CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1 280
- C.2.4 CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2 281
- C.2.5 ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON 3.10.15 DOCUMENTATION 281
- C.3 Licenses and Acknowledgements for Incorporated Software 282
- C.3.1 Mersenne Twister 282
- C.3.2 Sockets 283
- C.3.3 Asynchronous socket services 283
- C.3.4 Cookie management 284
- C.3.5 Execution tracing 284
- C.3.6 UUencode and UUdecode functions 285
- C.3.7 XML Remote Procedure Calls 285
- C.3.8 test\_epoll 286
- C.3.9 Select kqueue 286
- C.3.10 SipHash24 287
- C.3.11 strtod and dtoa 287
- C.3.12 OpenSSL 288
- C.3.13 expat 290
- C.3.14 libffi 290
- C.3.15 zlib 291
- C.3.16 cfuhash 291
- C.3.17 libmpdec 292
- C.3.18 W3C C14N test suite 292
- C.3.19 Audioop 293
- **D Copyright 295**

This manual documents the API used by C and C++ programmers who want to write extension modules or embed Python. It is a companion to extending-index, which describes the general principles of extension writing but does not document the API functions in detail.

## INTRODUCTION

The Application Programmer’s Interface to Python gives C and C++ programmers access to the Python interpreter at a variety of levels. The API is equally usable from C++, but for brevity it is generally referred to as the Python/C API. There are two fundamentally different reasons for using the Python/C API. The first reason is to write extension modules for specific purposes; these are C modules that extend the Python interpreter. This is probably the most common use. The second reason is to use Python as a component in a larger application; this technique is generally referred to as embedding Python in an application.

Writing an extension module is a relatively well-understood process, where a “cookbook” approach works well. There are several tools that automate the process to some extent. While people have embedded Python in other applications since its early existence, the process of embedding Python is less straightforward than writing an extension.

Many API functions are useful independent of whether you’re embedding or extending Python; moreover, most applications that embed Python will need to provide a custom extension as well, so it’s probably a good idea to become familiar with writing an extension before attempting to embed Python in a real application.

## 1.1 Coding standards

If you’re writing C code for inclusion in CPython, you **must** follow the guidelines and standards defined in [**PEP 7**](https://www.python.org/dev/peps/pep-0007). These guidelines apply regardless of the version of Python you are contributing to. Following these conventions is not necessary for your own third party extension modules, unless you eventually expect to contribute them to Python.

## 1.2 Include Files

All function, type and macro definitions needed to use the Python/C API are included in your code by the following line:

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```

This implies inclusion of the following standard headers: &lt;stdio.h&gt;, &lt;string.h&gt;, &lt;errno.h&gt;, &lt;limits. h&gt;, &lt;assert.h&gt; and &lt;stdlib.h&gt; (if available).

**Note:** Since Python may define some pre-processor definitions which affect the standard headers on some systems, you must include Python.h before any standard headers are included.

It is recommended to always define PY\_SSIZE\_T\_CLEAN before including Python.h. See Parsing arguments and building values for a description of this macro.

All user visible names defined by Python.h (except those defined by the included standard headers) have one of the prefixes Py or \_Py. Names beginning with \_Py are for internal use by the Python implementation and should not be used by extension writers. Structure member names do not have a reserved prefix.

**Note:** User code should never define names that begin with Py or \_Py. This confuses the reader, and jeopardizes the portability of the user code to future Python versions, which may define additional names beginning with one of these prefixes.

The header files are typically installed with Python. On Unix, these are located in the directories prefix/ include/pythonversion/ and exec\_prefix/include/pythonversion/, where prefix and exec\_prefix are defined by the corresponding parameters to Python’s **configure** script and version is '%d.%d' % sys.version\_info[:2]. On Windows, the headers are installed in prefix/include, where prefix is the installation directory specified to the installer.

To include the headers, place both directories (if different) on your compiler’s search path for includes. Do not place the parent directories on the search path and then use #include &lt;pythonX.Y/Python.h&gt;; this will break on multi-platform builds since the platform independent headers under prefix include the platform specific headers from exec\_prefix.

C++ users should note that although the API is defined entirely using C, the header files properly declare the entry points to be extern "C". As a result, there is no need to do anything special to use the API from C++.

## 1.3 Useful macros

Several useful macros are defined in the Python header files. Many are defined closer to where they are useful (e.g. Py\_RETURN\_NONE). Others of a more general utility are defined here. This is not necessarily a complete listing.

## Py\_UNREACHABLE()

Use this when you have a code path that cannot be reached by design. For example, in the default: clause in a switch statement for which all possible values are covered in case statements. Use this in places where you might be tempted to put an assert(0) or abort() call.

In release mode, the macro helps the compiler to optimize the code, and avoids a warning about unreachable code. For example, the macro is implemented with \_\_builtin\_unreachable() on GCC in release mode.

A use for Py\_UNREACHABLE() is following a call a function that never returns but that is not declared \_Py\_NO\_RETURN.

If a code path is very unlikely code but can be reached under exceptional case, this macro must not be used. For example, under low memory condition or if a system call returns a value out of the expected range. In this case, it’s better to report the error to the caller. If the error cannot be reported to caller, Py\_FatalError() can be used.

New in version 3.7.

## Py\_ABS(x)

Return the absolute value of x.

New in version 3.3.

## Py\_MIN(x, y)

Return the minimum value between x and y.

New in version 3.3.

## Py\_MAX(x, y)

Return the maximum value between x and y.

New in version 3.3.

## Py\_STRINGIFY(x)

Convert x to a C string. E.g. Py\_STRINGIFY(123) returns "123".

New in version 3.4.

**Py\_MEMBER\_SIZE**(type, member) Return the size of a structure (type) member in bytes.

New in version 3.6.

**Py\_CHARMASK**(c) Argument must be a character or an integer in the range [-128, 127] or [0, 255]. This macro returns c cast to an unsigned char.

## Py\_GETENV(s)

Like getenv(s), but returns NULL if -E was passed on the command line (i.e. if Py\_IgnoreEnvironmentFlag is set).

## Py\_UNUSED(arg)

Use this for unused arguments in a function definition to silence compiler warnings. Example: int func(int a, int Py\_UNUSED(b)) { return a; }.

New in version 3.4.

## Py\_DEPRECATED(version)

Use this for deprecated declarations. The macro must be placed before the symbol name.

Example:

```c
Py_DEPRECATED(3.8) PyAPI_FUNC(int) Py_OldFunction(void);
```

Changed in version 3.8: MSVC support was added.

## PyDoc\_STRVAR(name, str)

Creates a variable with name name that can be used in docstrings. If Python is built without docstrings, the value will be empty.

Use PyDoc\_STRVAR for docstrings to support building Python without docstrings, as specified in [**PEP 7**](https://www.python.org/dev/peps/pep-0007).

Example:

```txt
PyDoc_STRVAR(pop_doc, "Remove and return the rightmost element.");
static PyMethodDef deque_methods[] = {
    // ...
    {"pop", (PyCFunction)deque_pop, METH_NOARGS, pop_doc},
    // ...
}
```

## PyDoc\_STR(str)

Creates a docstring for the given input string or an empty string if docstrings are disabled.

Use PyDoc\_STR in specifying docstrings to support building Python without docstrings, as specified in [**PEP** 7](https://www.python.org/dev/peps/pep-0007).

Example:

```txt
static PyMethodDef pysqlite_row_methods[] = {
    {"keys", (PyCFunction) pysqlite_row_keys, METH_NOARGS,
        PyDoc_STR("Returns the keys of the row.")},
    {NULL, NULL}
};
```

## 1.4 Objects, Types and Reference Counts

Most Python/C API functions have one or more arguments as well as a return value of type PyObject\*. This type is a pointer to an opaque data type representing an arbitrary Python object. Since all Python object types are treated the same way by the Python language in most situations (e.g., assignments, scope rules, and argument passing), it is only fitting that they should be represented by a single C type. Almost all Python objects live on the heap: you never declare an automatic or static variable of type PyObject, only pointer variables of type PyObject\* can be declared. The sole exception are the type objects; since these must never be deallocated, they are typically static PyTypeObject objects.

All Python objects (even Python integers) have a type and a reference count. An object’s type determines what kind of object it is (e.g., an integer, a list, or a user-defined function; there are many more as explained in types). For each of the well-known types there is a macro to check whether an object is of that type; for instance, PyList\_Check(a) is true if (and only if) the object pointed to by a is a Python list.

## 1.4.1 Reference Counts

The reference count is important because today’s computers have a finite (and often severely limited) memory size; it counts how many different places there are that have a strong reference to an object. Such a place could be another object, or a global (or static) C variable, or a local variable in some C function. When the last strong reference to an object is released (i.e. its reference count becomes zero), the object is deallocated. If it contains references to other objects, those references are released. Those other objects may be deallocated in turn, if there are no more references to them, and so on. (There’s an obvious problem with objects that reference each other here; for now, the solution is “don’t do that.”)

Reference counts are always manipulated explicitly. The normal way is to use the macro Py\_INCREF() to take a new reference to an object (i.e. increment its reference count by one), and Py\_DECREF() to release that reference (i.e. decrement the reference count by one). The Py\_DECREF() macro is considerably more complex than the incref one, since it must check whether the reference count becomes zero and then cause the object’s deallocator to be called. The deallocator is a function pointer contained in the object’s type structure. The type-specific deallocator takes care of releasing references for other objects contained in the object if this is a compound object type, such as a list, as well as performing any additional finalization that’s needed. There’s no chance that the reference count can overflow; at least as many bits are used to hold the reference count as there are distinct memory locations in virtual memory (assuming sizeof(Py\_ssize\_t) >= sizeof(void\*)). Thus, the reference count increment is a simple operation.

It is not necessary to hold a strong reference (i.e. increment the reference count) for every local variable that contains a pointer to an object. In theory, the object’s reference count goes up by one when the variable is made to point to it and it goes down by one when the variable goes out of scope. However, these two cancel each other out, so at the end the reference count hasn’t changed. The only real reason to use the reference count is to prevent the object from being deallocated as long as our variable is pointing to it. If we know that there is at least one other reference to the object that lives at least as long as our variable, there is no need to take a new strong reference (i.e. increment the reference count) temporarily. An important situation where this arises is in objects that are passed as arguments to C functions in an extension module that are called from Python; the call mechanism guarantees to hold a reference to every argument for the duration of the call.

However, a common pitfall is to extract an object from a list and hold on to it for a while without taking a new reference. Some other operation might conceivably remove the object from the list, releasing that reference, and possibly deallocating it. The real danger is that innocent-looking operations may invoke arbitrary Python code which could do this; there is a code path which allows control to flow back to the user from a Py\_DECREF(), so almost any operation is potentially dangerous.

A safe approach is to always use the generic operations (functions whose name begins with PyObject\_, PyNumber\_, PySequence\_ or PyMapping\_). These operations always create a new strong reference (i.e. increment the reference count) of the object they return. This leaves the caller with the responsibility to call Py\_DECREF() when they are done with the result; this soon becomes second nature.

## Reference Count Details

The reference count behavior of functions in the Python/C API is best explained in terms of ownership of references. Ownership pertains to references, never to objects (objects are not owned: they are always shared). “Owning a reference” means being responsible for calling Py\_DECREF on it when the reference is no longer needed. Ownership can also be transferred, meaning that the code that receives ownership of the reference then becomes responsible for eventually releasing it by calling Py\_DECREF() or Py\_XDECREF() when it’s no longer needed—or passing on this responsibility (usually to its caller). When a function passes ownership of a reference on to its caller, the caller is said to receive a new reference. When no ownership is transferred, the caller is said to borrow the reference. Nothing needs to be done for a borrowed reference.

Conversely, when a calling function passes in a reference to an object, there are two possibilities: the function steals a reference to the object, or it does not. Stealing a reference means that when you pass a reference to a function, that function assumes that it now owns that reference, and you are not responsible for it any longer.

Few functions steal references; the two notable exceptions are PyList\_SetItem() and PyTuple\_SetItem(), which steal a reference to the item (but not to the tuple or list into which the item is put!). These functions were designed to steal a reference because of a common idiom for populating a tuple or list with newly created objects; for example, the code to create the tuple (1, 2, "three") could look like this (forgetting about error handling for the moment; a better way to code this is shown below):

```c
PyObject *t;

t = PyTuple_New(3);
PyTuple_SetItem(t, 0, PyLong_FromLong(1L));
PyTuple_SetItem(t, 1, PyLong_FromLong(2L));
PyTuple_SetItem(t, 2, PyUnicode_FromString("three"));
```

Here, PyLong\_FromLong() returns a new reference which is immediately stolen by PyTuple\_SetItem(). When you want to keep using an object although the reference to it will be stolen, use Py\_INCREF() to grab another reference before calling the reference-stealing function.

Incidentally, PyTuple\_SetItem() is the only way to set tuple items; PySequence\_SetItem() and PyObject\_SetItem() refuse to do this since tuples are an immutable data type. You should only use PyTuple\_SetItem() for tuples that you are creating yourself.

Equivalent code for populating a list can be written using PyList\_New() and PyList\_SetItem().

However, in practice, you will rarely use these ways of creating and populating a tuple or list. There’s a generic function, Py\_BuildValue(), that can create most common objects from C values, directed by a format string. For example, the above two blocks of code could be replaced by the following (which also takes care of the error checking):

```txt
PyObject *tuple, *list;

tuple = Py_BuildValue("(iis)", 1, 2, "three");
list = Py_BuildValue("[iis]", 1, 2, "three");
```

It is much more common to use PyObject\_SetItem() and friends with items whose references you are only borrowing, like arguments that were passed in to the function you are writing. In that case, their behaviour regarding references is much saner, since you don’t have to take a new reference just so you can give that reference away (“have it be stolen”). For example, this function sets all items of a list (actually, any mutable sequence) to a given item:

```c
int
set_all(PyObject *target, PyObject *item)
{
    Py_ssize_t i, n;

    n = PyObject_Length(target);
    if (n < 0)
        return -1;
    for (i = 0; i < n; i++) {
```

(continues on next page)

```c
PyObject *index = PyLong_FromSsize_t(i);
    if (!index)
        return -1;
    if (PyObject_SetItem(target, index, item) < 0) {
        Py_DECREF(index);
        return -1;
    }
    Py_DECREF(index);
}
return 0;
}
```

(continued from previous page)

The situation is slightly different for function return values. While passing a reference to most functions does not change your ownership responsibilities for that reference, many functions that return a reference to an object give you ownership of the reference. The reason is simple: in many cases, the returned object is created on the fly, and the reference you get is the only reference to the object. Therefore, the generic functions that return object references, like PyObject\_GetItem() and PySequence\_GetItem(), always return a new reference (the caller becomes the owner of the reference).

It is important to realize that whether you own a reference returned by a function depends on which function you call only — the plumage (the type of the object passed as an argument to the function) doesn’t enter into it! Thus, if you extract an item from a list using PyList\_GetItem(), you don’t own the reference — but if you obtain the same item from the same list using PySequence\_GetItem() (which happens to take exactly the same arguments), you do own a reference to the returned object.

Here is an example of how you could write a function that computes the sum of the items in a list of integers; once using PyList\_GetItem(), and once using PySequence\_GetItem().

```c
long
sum_list(PyObject *list)
{
    Py_ssize_t i, n;
    long total = 0, value;
    PyObject *item;

    n = PyList_Size(list);
    if (n < 0)
        return -1; /* Not a list */
    for (i = 0; i < n; i++) {
        item = PyList_GetItem(list, i); /* Can't fail */
        if (!PyLong_Check(item)) continue; /* Skip non-integers */
        value = PyLong_AsLong(item);
        if (value == -1 && PyErr_Occurred())
            /* Integer too big to fit in a C long, bail out */
            return -1;
        total += value;
    }
    return total;
}
c
long
sum_sequence(PyObject *sequence)
{
    Py_ssize_t i, n;
    long total = 0, value;
    PyObject *item;
    n = PySequence_Length(sequence);
    if (n < 0)
        return -1; /* Has no length */
    for (i = 0; i < n; i++) {
        item = PySequence_GetItem(sequence, i);
```

(continues on next page)

(continued from previous page)

```c
if (item == NULL)
    return -1; /* Not a sequence, or other failure */
if (PyLong_Check(item)) {
    value = PyLong_AsLong(item);
    Py_DECREF(item);
    if (value == -1 && PyErr_Occurred())
        /* Integer too big to fit in a C long, bail out */
        return -1;
    total += value;
}
else {
    Py_DECREF(item); /* Discard reference ownership */
}
}
return total;
}
```

## 1.4.2 Types

There are few other data types that play a significant role in the Python/C API; most are simple C types such as int, long, double and char\*. A few structure types are used to describe static tables used to list the functions exported by a module or the data attributes of a new object type, and another is used to describe the value of a complex number. These will be discussed together with the functions that use them.

**type Py\_ssize\_t**

Part of the Stable ABI. A signed integral type such that sizeof(Py\_ssize\_t) == sizeof(size\_t). C99 doesn’t define such a thing directly (size\_t is an unsigned integral type). See [**PEP 353**](https://www.python.org/dev/peps/pep-0353) for details. PY\_SSIZE\_T\_MAX is the largest positive value of type Py\_ssize\_t.

## 1.5 Exceptions

The Python programmer only needs to deal with exceptions if specific error handling is required; unhandled exceptions are automatically propagated to the caller, then to the caller’s caller, and so on, until they reach the top-level interpreter, where they are reported to the user accompanied by a stack traceback.

For C programmers, however, error checking always has to be explicit. All functions in the Python/C API can raise exceptions, unless an explicit claim is made otherwise in a function’s documentation. In general, when a function encounters an error, it sets an exception, discards any object references that it owns, and returns an error indicator. If not documented otherwise, this indicator is either NULL or -1, depending on the function’s return type. A few functions return a Boolean true/false result, with false indicating an error. Very few functions return no explicit error indicator or have an ambiguous return value, and require explicit testing for errors with PyErr\_Occurred(). These exceptions are always explicitly documented.

Exception state is maintained in per-thread storage (this is equivalent to using global storage in an unthreaded application). A thread can be in one of two states: an exception has occurred, or not. The function PyErr\_Occurred() can be used to check for this: it returns a borrowed reference to the exception type object when an exception has occurred, and NULL otherwise. There are a number of functions to set the exception state: PyErr\_SetString() is the most common (though not the most general) function to set the exception state, and PyErr\_Clear() clears the exception state.

The full exception state consists of three objects (all of which can be NULL): the exception type, the corresponding exception value, and the traceback. These have the same meanings as the Python result of sys.exc\_info(); however, they are not the same: the Python objects represent the last exception being handled by a Python try … except statement, while the C level exception state only exists while an exception is being passed on between C functions until it reaches the Python bytecode interpreter’s main loop, which takes care of transferring it to sys. exc\_info() and friends.

Note that starting with Python 1.5, the preferred, thread-safe way to access the exception state from Python code is to call the function sys.exc\_info(), which returns the per-thread exception state for Python code. Also, the semantics of both ways to access the exception state have changed so that a function which catches an exception will save and restore its thread’s exception state so as to preserve the exception state of its caller. This prevents common bugs in exception handling code caused by an innocent-looking function overwriting the exception being handled; it also reduces the often unwanted lifetime extension for objects that are referenced by the stack frames in the traceback.

As a general principle, a function that calls another function to perform some task should check whether the called function raised an exception, and if so, pass the exception state on to its caller. It should discard any object references that it owns, and return an error indicator, but it should not set another exception — that would overwrite the exception that was just raised, and lose important information about the exact cause of the error.

A simple example of detecting exceptions and passing them on is shown in the sum\_sequence() example above. It so happens that this example doesn’t need to clean up any owned references when it detects an error. The following example function shows some error cleanup. First, to remind you why you like Python, we show the equivalent Python code:

```python
def incr_item(dict, key):
    try:
        item = dict[key]
    except KeyError:
        item = 0
    dict[key] = item + 1
```

Here is the corresponding C code, in all its glory:

```c
int
incr_item(PyObject *dict, PyObject *key)
{
    /* Objects all initialized to NULL for Py_XDECREF */
    PyObject *item = NULL, *const_one = NULL, *incremented_item = NULL;
    int rv = -1; /* Return value initialized to -1 (failure) */

    item = PyObject_GetItem(dict, key);
    if (item == NULL) {
        /* Handle KeyError only: */
        if (!PyErr_ExceptionMatches(PyExc_KeyError))
            goto error;

        /* Clear the error and use zero: */
        PyErr_Clear();
        item = PyLong_FromLong(0L);
        if (item == NULL)
            goto error;
    }
    const_one = PyLong_FromLong(1L);
    if (const_one == NULL)
        goto error;

    incremented_item = PyNumber_Add(item, const_one);
    if (incremented_item == NULL)
        goto error;

    if (PyObject_SetItem(dict, key, incremented_item) < 0)
        goto error;
    rv = 0; /* Success */
    /* Continue with cleanup code */

error:
    /* Cleanup code, shared by success and failure path */

    /* Use Py_XDECREF() to ignore NULL references */
```

(continues on next page)

```c
(continued from previous page)

    Py_XDECREF(item);
    Py_XDECREF(const_one);
    Py_XDECREF(incremented_item);

    return rv; /* -1 for error, 0 for success */
}
```

This example represents an endorsed use of the goto statement in C! It illustrates the use of PyErr\_ExceptionMatches() and PyErr\_Clear() to handle specific exceptions, and the use of Py\_XDECREF() to dispose of owned references that may be NULL (note the 'X' in the name; Py\_DECREF() would crash when confronted with a NULL reference). It is important that the variables used to hold owned references are initialized to NULL for this to work; likewise, the proposed return value is initialized to -1 (failure) and only set to success after the final call made is successful.

## 1.6 Embedding Python

The one important task that only embedders (as opposed to extension writers) of the Python interpreter have to worry about is the initialization, and possibly the finalization, of the Python interpreter. Most functionality of the interpreter can only be used after the interpreter has been initialized.

The basic initialization function is Py\_Initialize(). This initializes the table of loaded modules, and creates the fundamental modules builtins, \_\_main\_\_, and sys. It also initializes the module search path (sys.path).

Py\_Initialize() does not set the “script argument list” (sys.argv). If this variable is needed by Python code that will be executed later, it must be set explicitly with a call to PySys\_SetArgvEx(argc, argv, updatepath) after the call to Py\_Initialize().

On most systems (in particular, on Unix and Windows, although the details are slightly different), Py\_Initialize() calculates the module search path based upon its best guess for the location of the standard Python interpreter executable, assuming that the Python library is found in a fixed location relative to the Python interpreter executable. In particular, it looks for a directory named lib/pythonX.Y relative to the parent directory where the executable named python is found on the shell command search path (the environment variable PATH).

For instance, if the Python executable is found in /usr/local/bin/python, it will assume that the libraries are in /usr/local/lib/pythonX.Y. (In fact, this particular path is also the “fallback” location, used when no executable file named python is found along PATH.) The user can override this behavior by setting the environment variable PYTHONHOME, or insert additional directories in front of the standard path by setting PYTHONPATH.

The embedding application can steer the search by calling Py\_SetProgramName(file) before calling Py\_Initialize(). Note that PYTHONHOME still overrides this and PYTHONPATH is still inserted in front of the standard path. An application that requires total control has to provide its own implementation of Py\_GetPath(), Py\_GetPrefix(), Py\_GetExecPrefix(), and Py\_GetProgramFullPath() (all defined in Modules/getpath.c).

Sometimes, it is desirable to “uninitialize” Python. For instance, the application may want to start over (make another call to Py\_Initialize()) or the application is simply done with its use of Python and wants to free memory allocated by Python. This can be accomplished by calling Py\_FinalizeEx(). The function Py\_IsInitialized() returns true if Python is currently in the initialized state. More information about these functions is given in a later chapter. Notice that Py\_FinalizeEx() does not free all memory allocated by the Python interpreter, e.g. memory allocated by extension modules currently cannot be released.

## 1.7 Debugging Builds

Python can be built with several macros to enable extra checks of the interpreter and extension modules. These checks tend to add a large amount of overhead to the runtime so they are not enabled by default.

A full list of the various types of debugging builds is in the file Misc/SpecialBuilds.txt in the Python source distribution. Builds are available that support tracing of reference counts, debugging the memory allocator, or lowlevel profiling of the main interpreter loop. Only the most frequently used builds will be described in the remainder of this section.

Compiling the interpreter with the Py\_DEBUG macro defined produces what is generally meant by a debug build of Python. Py\_DEBUG is enabled in the Unix build by adding --with-pydebug to the ./configure command. It is also implied by the presence of the not-Python-specific \_DEBUG macro. When Py\_DEBUG is enabled in the Unix build, compiler optimization is disabled.

In addition to the reference count debugging described below, extra checks are performed, see Python Debug Build.

Defining Py\_TRACE\_REFS enables reference tracing (see the configure --with-trace-refs option). When defined, a circular doubly linked list of active objects is maintained by adding two extra fields to every PyObject. Total allocations are tracked as well. Upon exit, all existing references are printed. (In interactive mode this happens after every statement run by the interpreter.)

Please refer to Misc/SpecialBuilds.txt in the Python source distribution for more detailed information.

# C API STABILITY

Python’s C API is covered by the Backwards Compatibility Policy, [**PEP 387**](https://www.python.org/dev/peps/pep-0387). While the C API will change with every minor release (e.g. from 3.9 to 3.10), most changes will be source-compatible, typically by only adding new API. Changing existing API or removing API is only done after a deprecation period or to fix serious issues.

CPython’s Application Binary Interface (ABI) is forward- and backwards-compatible across a minor release (if these are compiled the same way; see Platform Considerations below). So, code compiled for Python 3.10.0 will work on 3.10.8 and vice versa, but will need to be compiled separately for 3.9.x and 3.10.x.

Names prefixed by an underscore, such as \_Py\_InternalState, are private API that can change without notice even in patch releases.

## 2.1 Stable Application Binary Interface

Python 3.2 introduced the Limited API, a subset of Python’s C API. Extensions that only use the Limited API can be compiled once and work with multiple versions of Python. Contents of the Limited API are listed below.

To enable this, Python provides a Stable ABI: a set of symbols that will remain compatible across Python 3.x versions. The Stable ABI contains symbols exposed in the Limited API, but also other ones – for example, functions necessary to support older versions of the Limited API.

(For simplicity, this document talks about extensions, but the Limited API and Stable ABI work the same way for all uses of the API – for example, embedding Python.)

## Py\_LIMITED\_API

Define this macro before including Python.h to opt in to only use the Limited API, and to select the Limited API version.

Define Py\_LIMITED\_API to the value of PY\_VERSION\_HEX corresponding to the lowest Python version your extension supports. The extension will work without recompilation with all Python 3 releases from the specified one onward, and can use Limited API introduced up to that version.

Rather than using the PY\_VERSION\_HEX macro directly, hardcode a minimum minor version (e.g. 0x030A0000 for Python 3.10) for stability when compiling with future Python versions.

You can also define Py\_LIMITED\_API to 3. This works the same as 0x03020000 (Python 3.2, the version that introduced Limited API).

On Windows, extensions that use the Stable ABI should be linked against python3.dll rather than a versionspecific library such as python39.dll.

On some platforms, Python will look for and load shared library files named with the abi3 tag (e.g. mymodule. abi3.so). It does not check if such extensions conform to a Stable ABI. The user (or their packaging tools) need to ensure that, for example, extensions built with the 3.10+ Limited API are not installed for lower versions of Python.

All functions in the Stable ABI are present as functions in Python’s shared library, not solely as macros. This makes them usable from languages that don’t use the C preprocessor.

## 2.1.1 Limited API Scope and Performance

The goal for the Limited API is to allow everything that is possible with the full C API, but possibly with a performance penalty.

For example, while PyList\_GetItem() is available, its “unsafe” macro variant PyList\_GET\_ITEM() is not. The macro can be faster because it can rely on version-specific implementation details of the list object.

Without Py\_LIMITED\_API defined, some C API functions are inlined or replaced by macros. Defining Py\_LIMITED\_API disables this inlining, allowing stability as Python’s data structures are improved, but possibly reducing performance.

By leaving out the Py\_LIMITED\_API definition, it is possible to compile a Limited API extension with a versionspecific ABI. This can improve performance for that Python version, but will limit compatibility. Compiling with Py\_LIMITED\_API will then yield an extension that can be distributed where a version-specific one is not available – for example, for prereleases of an upcoming Python version.

## 2.1.2 Limited API Caveats

Note that compiling with Py\_LIMITED\_API is not a complete guarantee that code conforms to the Limited API or the Stable ABI. Py\_LIMITED\_API only covers definitions, but an API also includes other issues, such as expected semantics.

One issue that Py\_LIMITED\_API does not guard against is calling a function with arguments that are invalid in a lower Python version. For example, consider a function that starts accepting NULL for an argument. In Python 3.9, NULL now selects a default behavior, but in Python 3.8, the argument will be used directly, causing a NULL dereference and crash. A similar argument works for fields of structs.

Another issue is that some struct fields are currently not hidden when Py\_LIMITED\_API is defined, even though they’re part of the Limited API.

For these reasons, we recommend testing an extension with all minor Python versions it supports, and preferably to build with the lowest such version.

We also recommend reviewing documentation of all used API to check if it is explicitly part of the Limited API. Even with Py\_LIMITED\_API defined, a few private declarations are exposed for technical reasons (or even unintentionally, as bugs).

Also note that the Limited API is not necessarily stable: compiling with Py\_LIMITED\_API with Python 3.8 means that the extension will run with Python 3.12, but it will not necessarily compile with Python 3.12. In particular, parts of the Limited API may be deprecated and removed, provided that the Stable ABI stays stable.

## 2.2 Platform Considerations

ABI stability depends not only on Python, but also on the compiler used, lower-level libraries and compiler options. For the purposes of the Stable ABI, these details define a “platform”. They usually depend on the OS type and processor architecture

It is the responsibility of each particular distributor of Python to ensure that all Python versions on a particular platform are built in a way that does not break the Stable ABI. This is the case with Windows and macOS releases from python.org and many third-party distributors.

## 2.3 Contents of Limited API

Currently, the Limited API includes the following items:

• PyAIter\_Check()

• PyArg\_Parse()

• PyArg\_ParseTuple()

• PyArg\_ParseTupleAndKeywords()

• PyArg\_UnpackTuple()

• PyArg\_VaParse()

• PyArg\_VaParseTupleAndKeywords()

• PyArg\_ValidateKeywordArguments()

• PyBaseObject\_Type

• PyBool\_FromLong()

• PyBool\_Type

• PyByteArrayIter\_Type

• PyByteArray\_AsString()

• PyByteArray\_Concat()

• PyByteArray\_FromObject()

• PyByteArray\_FromStringAndSize()

• PyByteArray\_Resize()

• PyByteArray\_Size()

• PyByteArray\_Type

• PyBytesIter\_Type

• PyBytes\_AsString()

• PyBytes\_AsStringAndSize()

• PyBytes\_Concat()

• PyBytes\_ConcatAndDel()

• PyBytes\_DecodeEscape()

• PyBytes\_FromFormat()

• PyBytes\_FromFormatV()

• PyBytes\_FromObject()

• PyBytes\_FromString()

• PyBytes\_FromStringAndSize()

• PyBytes\_Repr()

• PyBytes\_Size()

• PyBytes\_Type

• PyCFunction

• PyCFunctionWithKeywords

• PyCFunction\_Call()

## The Python/C API, Release 3.10.15

• PyCFunction\_GetFlags()

• PyCFunction\_GetFunction()

• PyCFunction\_GetSelf()

• PyCFunction\_New()

• PyCFunction\_NewEx()

• PyCFunction\_Type

• PyCMethod\_New()

• PyCallIter\_New()

• PyCallIter\_Type

• PyCallable\_Check()

• PyCapsule\_Destructor

• PyCapsule\_GetContext()

• PyCapsule\_GetDestructor()

• PyCapsule\_GetName()

• PyCapsule\_GetPointer()

• PyCapsule\_Import()

• PyCapsule\_IsValid()

• PyCapsule\_New()

• PyCapsule\_SetContext()

• PyCapsule\_SetDestructor()

• PyCapsule\_SetName()

• PyCapsule\_SetPointer()

• PyCapsule\_Type

• PyClassMethodDescr\_Type

• PyCodec\_BackslashReplaceErrors()

• PyCodec\_Decode()

• PyCodec\_Decoder()

• PyCodec\_Encode()

• PyCodec\_Encoder()

• PyCodec\_IgnoreErrors()

• PyCodec\_IncrementalDecoder()

• PyCodec\_IncrementalEncoder()

• PyCodec\_KnownEncoding()

• PyCodec\_LookupError()

• PyCodec\_NameReplaceErrors()

• PyCodec\_Register()

• PyCodec\_RegisterError()

• PyCodec\_ReplaceErrors()

• PyCodec\_StreamReader()

• PyCodec\_StreamWriter()

• PyCodec\_StrictErrors()

• PyCodec\_Unregister()

• PyCodec\_XMLCharRefReplaceErrors()

• PyComplex\_FromDoubles()

• PyComplex\_ImagAsDouble()

• PyComplex\_RealAsDouble()

• PyComplex\_Type

• PyDescr\_NewClassMethod()

• PyDescr\_NewGetSet()

• PyDescr\_NewMember()

• PyDescr\_NewMethod()

• PyDictItems\_Type

• PyDictIterItem\_Type

• PyDictIterKey\_Type

• PyDictIterValue\_Type

• PyDictKeys\_Type

• PyDictProxy\_New()

• PyDictProxy\_Type

• PyDictRevIterItem\_Type

• PyDictRevIterKey\_Type

• PyDictRevIterValue\_Type

• PyDictValues\_Type

• PyDict\_Clear()

• PyDict\_Contains()

• PyDict\_Copy()

• PyDict\_DelItem()

• PyDict\_DelItemString()

• PyDict\_GetItem()

• PyDict\_GetItemString()

• PyDict\_GetItemWithError()

• PyDict\_Items()

• PyDict\_Keys()

• PyDict\_Merge()

• PyDict\_MergeFromSeq2()

• PyDict\_New()

• PyDict\_Next()

• PyDict\_SetItem()

• PyDict\_SetItemString()

## The Python/C API, Release 3.10.15

• PyDict\_Size()

• PyDict\_Type

• PyDict\_Update()

• PyDict\_Values()

• PyEllipsis\_Type

• PyEnum\_Type

• PyErr\_BadArgument()

• PyErr\_BadInternalCall()

• PyErr\_CheckSignals()

• PyErr\_Clear()

• PyErr\_Display()

• PyErr\_ExceptionMatches()

• PyErr\_Fetch()

• PyErr\_Format()

• PyErr\_FormatV()

• PyErr\_GetExcInfo()

• PyErr\_GivenExceptionMatches()

• PyErr\_NewException()

• PyErr\_NewExceptionWithDoc()

• PyErr\_NoMemory()

• PyErr\_NormalizeException()

• PyErr\_Occurred()

• PyErr\_Print()

• PyErr\_PrintEx()

• PyErr\_ProgramText()

• PyErr\_ResourceWarning()

• PyErr\_Restore()

• PyErr\_SetExcFromWindowsErr()

• PyErr\_SetExcFromWindowsErrWithFilename()

• PyErr\_SetExcFromWindowsErrWithFilenameObject()

• PyErr\_SetExcFromWindowsErrWithFilenameObjects()

• PyErr\_SetExcInfo()

• PyErr\_SetFromErrno()

• PyErr\_SetFromErrnoWithFilename()

• PyErr\_SetFromErrnoWithFilenameObject()

• PyErr\_SetFromErrnoWithFilenameObjects()

• PyErr\_SetFromWindowsErr()

• PyErr\_SetFromWindowsErrWithFilename()

• PyErr\_SetImportError()

• PyErr\_SetImportErrorSubclass()

• PyErr\_SetInterrupt()

• PyErr\_SetInterruptEx()

• PyErr\_SetNone()

• PyErr\_SetObject()

• PyErr\_SetString()

• PyErr\_SyntaxLocation()

• PyErr\_SyntaxLocationEx()

• PyErr\_WarnEx()

• PyErr\_WarnExplicit()

• PyErr\_WarnFormat()

• PyErr\_WriteUnraisable()

• PyEval\_AcquireLock()

• PyEval\_AcquireThread()

• PyEval\_CallFunction()

• PyEval\_CallMethod()

• PyEval\_CallObjectWithKeywords()

• PyEval\_EvalCode()

• PyEval\_EvalCodeEx()

• PyEval\_EvalFrame()

• PyEval\_EvalFrameEx()

• PyEval\_GetBuiltins()

• PyEval\_GetFrame()

• PyEval\_GetFuncDesc()

• PyEval\_GetFuncName()

• PyEval\_GetGlobals()

• PyEval\_GetLocals()

• PyEval\_InitThreads()

• PyEval\_ReleaseLock()

• PyEval\_ReleaseThread()

• PyEval\_RestoreThread()

• PyEval\_SaveThread()

• PyEval\_ThreadsInitialized()

• PyExc\_ArithmeticError

• PyExc\_AssertionError

• PyExc\_AttributeError

• PyExc\_BaseException

• PyExc\_BlockingIOError

• PyExc\_BrokenPipeError

## The Python/C API, Release 3.10.15

• PyExc\_BufferError

• PyExc\_BytesWarning

• PyExc\_ChildProcessError

• PyExc\_ConnectionAbortedError

• PyExc\_ConnectionError

• PyExc\_ConnectionRefusedError

• PyExc\_ConnectionResetError

• PyExc\_DeprecationWarning

• PyExc\_EOFError

• PyExc\_EncodingWarning

• PyExc\_EnvironmentError

• PyExc\_Exception

• PyExc\_FileExistsError

• PyExc\_FileNotFoundError

• PyExc\_FloatingPointError

• PyExc\_FutureWarning

• PyExc\_GeneratorExit

• PyExc\_IOError

• PyExc\_ImportError

• PyExc\_ImportWarning

• PyExc\_IndentationError

• PyExc\_IndexError

• PyExc\_InterruptedError

• PyExc\_IsADirectoryError

• PyExc\_KeyError

• PyExc\_KeyboardInterrupt

• PyExc\_LookupError

• PyExc\_MemoryError

• PyExc\_ModuleNotFoundError

• PyExc\_NameError

• PyExc\_NotADirectoryError

• PyExc\_NotImplementedError

• PyExc\_OSError

• PyExc\_OverflowError

• PyExc\_PendingDeprecationWarning

• PyExc\_PermissionError

• PyExc\_ProcessLookupError

• PyExc\_RecursionError

• PyExc\_ReferenceError

• PyExc\_ResourceWarning

• PyExc\_RuntimeError

• PyExc\_RuntimeWarning

• PyExc\_StopAsyncIteration

• PyExc\_StopIteration

• PyExc\_SyntaxError

• PyExc\_SyntaxWarning

• PyExc\_SystemError

• PyExc\_SystemExit

• PyExc\_TabError

• PyExc\_TimeoutError

• PyExc\_TypeError

• PyExc\_UnboundLocalError

• PyExc\_UnicodeDecodeError

• PyExc\_UnicodeEncodeError

• PyExc\_UnicodeError

• PyExc\_UnicodeTranslateError

• PyExc\_UnicodeWarning

• PyExc\_UserWarning

• PyExc\_ValueError

• PyExc\_Warning

• PyExc\_WindowsError

• PyExc\_ZeroDivisionError

• PyExceptionClass\_Name()

• PyException\_GetCause()

• PyException\_GetContext()

• PyException\_GetTraceback()

• PyException\_SetCause()

• PyException\_SetContext()

• PyException\_SetTraceback()

• PyFile\_FromFd()

• PyFile\_GetLine()

• PyFile\_WriteObject()

• PyFile\_WriteString()

• PyFilter\_Type

• PyFloat\_AsDouble()

• PyFloat\_FromDouble()

• PyFloat\_FromString()

• PyFloat\_GetInfo()

## The Python/C API, Release 3.10.15

• PyFloat\_GetMax()

• PyFloat\_GetMin()

• PyFloat\_Type

• PyFrameObject

• PyFrame\_GetCode()

• PyFrame\_GetLineNumber()

• PyFrozenSet\_New()

• PyFrozenSet\_Type

• PyGC\_Collect()

• PyGC\_Disable()

• PyGC\_Enable()

• PyGC\_IsEnabled()

• PyGILState\_Ensure()

• PyGILState\_GetThisThreadState()

• PyGILState\_Release()

• PyGILState\_STATE

• PyGetSetDef

• PyGetSetDescr\_Type

• PyImport\_AddModule()

• PyImport\_AddModuleObject()

• PyImport\_AppendInittab()

• PyImport\_ExecCodeModule()

• PyImport\_ExecCodeModuleEx()

• PyImport\_ExecCodeModuleObject()

• PyImport\_ExecCodeModuleWithPathnames()

• PyImport\_GetImporter()

• PyImport\_GetMagicNumber()

• PyImport\_GetMagicTag()

• PyImport\_GetModule()

• PyImport\_GetModuleDict()

• PyImport\_Import()

• PyImport\_ImportFrozenModule()

• PyImport\_ImportFrozenModuleObject()

• PyImport\_ImportModule()

• PyImport\_ImportModuleLevel()

• PyImport\_ImportModuleLevelObject()

• PyImport\_ImportModuleNoBlock()

• PyImport\_ReloadModule()

• PyIndex\_Check()

• PyInterpreterState

• PyInterpreterState\_Clear()

• PyInterpreterState\_Delete()

• PyInterpreterState\_Get()

• PyInterpreterState\_GetDict()

• PyInterpreterState\_GetID()

• PyInterpreterState\_New()

• PyIter\_Check()

• PyIter\_Next()

• PyIter\_Send()

• PyListIter\_Type

• PyListRevIter\_Type

• PyList\_Append()

• PyList\_AsTuple()

• PyList\_GetItem()

• PyList\_GetSlice()

• PyList\_Insert()

• PyList\_New()

• PyList\_Reverse()

• PyList\_SetItem()

• PyList\_SetSlice()

• PyList\_Size()

• PyList\_Sort()

• PyList\_Type

• PyLongObject

• PyLongRangeIter\_Type

• PyLong\_AsDouble()

• PyLong\_AsLong()

• PyLong\_AsLongAndOverflow()

• PyLong\_AsLongLong()

• PyLong\_AsLongLongAndOverflow()

• PyLong\_AsSize\_t()

• PyLong\_AsSsize\_t()

• PyLong\_AsUnsignedLong()

• PyLong\_AsUnsignedLongLong()

• PyLong\_AsUnsignedLongLongMask()

• PyLong\_AsUnsignedLongMask()

• PyLong\_AsVoidPtr()

• PyLong\_FromDouble()

## The Python/C API, Release 3.10.15

• PyLong\_FromLong()

• PyLong\_FromLongLong()

• PyLong\_FromSize\_t()

• PyLong\_FromSsize\_t()

• PyLong\_FromString()

• PyLong\_FromUnsignedLong()

• PyLong\_FromUnsignedLongLong()

• PyLong\_FromVoidPtr()

• PyLong\_GetInfo()

• PyLong\_Type

• PyMap\_Type

• PyMapping\_Check()

• PyMapping\_GetItemString()

• PyMapping\_HasKey()

• PyMapping\_HasKeyString()

• PyMapping\_Items()

• PyMapping\_Keys()

• PyMapping\_Length()

• PyMapping\_SetItemString()

• PyMapping\_Size()

• PyMapping\_Values()

• PyMem\_Calloc()

• PyMem\_Free()

• PyMem\_Malloc()

• PyMem\_Realloc()

• PyMemberDef

• PyMemberDescr\_Type

• PyMemoryView\_FromMemory()

• PyMemoryView\_FromObject()

• PyMemoryView\_GetContiguous()

• PyMemoryView\_Type

• PyMethodDef

• PyMethodDescr\_Type

• PyModuleDef

• PyModuleDef\_Base

• PyModuleDef\_Init()

• PyModuleDef\_Type

• PyModule\_AddFunctions()

• PyModule\_AddIntConstant()

• PyModule\_AddObject()

• PyModule\_AddObjectRef()

• PyModule\_AddStringConstant()

• PyModule\_AddType()

• PyModule\_Create2()

• PyModule\_ExecDef()

• PyModule\_FromDefAndSpec2()

• PyModule\_GetDef()

• PyModule\_GetDict()

• PyModule\_GetFilename()

• PyModule\_GetFilenameObject()

• PyModule\_GetName()

• PyModule\_GetNameObject()

• PyModule\_GetState()

• PyModule\_New()

• PyModule\_NewObject()

• PyModule\_SetDocString()

• PyModule\_Type

• PyNumber\_Absolute()

• PyNumber\_Add()

• PyNumber\_And()

• PyNumber\_AsSsize\_t()

• PyNumber\_Check()

• PyNumber\_Divmod()

• PyNumber\_Float()

• PyNumber\_FloorDivide()

• PyNumber\_InPlaceAdd()

• PyNumber\_InPlaceAnd()

• PyNumber\_InPlaceFloorDivide()

• PyNumber\_InPlaceLshift()

• PyNumber\_InPlaceMatrixMultiply()

• PyNumber\_InPlaceMultiply()

• PyNumber\_InPlaceOr()

• PyNumber\_InPlacePower()

• PyNumber\_InPlaceRemainder()

• PyNumber\_InPlaceRshift()

• PyNumber\_InPlaceSubtract()

• PyNumber\_InPlaceTrueDivide()

• PyNumber\_InPlaceXor()

## The Python/C API, Release 3.10.15

• PyNumber\_Index()

• PyNumber\_Invert()

• PyNumber\_Long()

• PyNumber\_Lshift()

• PyNumber\_MatrixMultiply()

• PyNumber\_Multiply()

• PyNumber\_Negative()

• PyNumber\_Or()

• PyNumber\_Positive()

• PyNumber\_Power()

• PyNumber\_Remainder()

• PyNumber\_Rshift()

• PyNumber\_Subtract()

• PyNumber\_ToBase()

• PyNumber\_TrueDivide()

• PyNumber\_Xor()

• PyOS\_AfterFork()

• PyOS\_AfterFork\_Child()

• PyOS\_AfterFork\_Parent()

• PyOS\_BeforeFork()

• PyOS\_CheckStack()

• PyOS\_FSPath()

• PyOS\_InputHook

• PyOS\_InterruptOccurred()

• PyOS\_double\_to\_string()

• PyOS\_getsig()

• PyOS\_mystricmp()

• PyOS\_mystrnicmp()

• PyOS\_setsig()

• PyOS\_sighandler\_t

• PyOS\_snprintf()

• PyOS\_string\_to\_double()

• PyOS\_strtol()

• PyOS\_strtoul()

• PyOS\_vsnprintf()

• PyObject

• PyObject.ob\_refcnt

• PyObject.ob\_type

• PyObject\_ASCII()

• PyObject\_AsCharBuffer()

• PyObject\_AsFileDescriptor()

• PyObject\_AsReadBuffer()

• PyObject\_AsWriteBuffer()

• PyObject\_Bytes()

• PyObject\_Call()

• PyObject\_CallFunction()

• PyObject\_CallFunctionObjArgs()

• PyObject\_CallMethod()

• PyObject\_CallMethodObjArgs()

• PyObject\_CallNoArgs()

• PyObject\_CallObject()

• PyObject\_Calloc()

• PyObject\_CheckReadBuffer()

• PyObject\_ClearWeakRefs()

• PyObject\_DelItem()

• PyObject\_DelItemString()

• PyObject\_Dir()

• PyObject\_Format()

• PyObject\_Free()

• PyObject\_GC\_Del()

• PyObject\_GC\_IsFinalized()

• PyObject\_GC\_IsTracked()

• PyObject\_GC\_Track()

• PyObject\_GC\_UnTrack()

• PyObject\_GenericGetAttr()

• PyObject\_GenericGetDict()

• PyObject\_GenericSetAttr()

• PyObject\_GenericSetDict()

• PyObject\_GetAIter()

• PyObject\_GetAttr()

• PyObject\_GetAttrString()

• PyObject\_GetItem()

• PyObject\_GetIter()

• PyObject\_HasAttr()

• PyObject\_HasAttrString()

• PyObject\_Hash()

• PyObject\_HashNotImplemented()

• PyObject\_Init()

## The Python/C API, Release 3.10.15

• PyObject\_InitVar()

• PyObject\_IsInstance()

• PyObject\_IsSubclass()

• PyObject\_IsTrue()

• PyObject\_Length()

• PyObject\_Malloc()

• PyObject\_Not()

• PyObject\_Realloc()

• PyObject\_Repr()

• PyObject\_RichCompare()

• PyObject\_RichCompareBool()

• PyObject\_SelfIter()

• PyObject\_SetAttr()

• PyObject\_SetAttrString()

• PyObject\_SetItem()

• PyObject\_Size()

• PyObject\_Str()

• PyObject\_Type()

• PyProperty\_Type

• PyRangeIter\_Type

• PyRange\_Type

• PyReversed\_Type

• PySeqIter\_New()

• PySeqIter\_Type

• PySequence\_Check()

• PySequence\_Concat()

• PySequence\_Contains()

• PySequence\_Count()

• PySequence\_DelItem()

• PySequence\_DelSlice()

• PySequence\_Fast()

• PySequence\_GetItem()

• PySequence\_GetSlice()

• PySequence\_In()

• PySequence\_InPlaceConcat()

• PySequence\_InPlaceRepeat()

• PySequence\_Index()

• PySequence\_Length()

• PySequence\_List()

• PySequence\_Repeat()

• PySequence\_SetItem()

• PySequence\_SetSlice()

• PySequence\_Size()

• PySequence\_Tuple()

• PySetIter\_Type

• PySet\_Add()

• PySet\_Clear()

• PySet\_Contains()

• PySet\_Discard()

• PySet\_New()

• PySet\_Pop()

• PySet\_Size()

• PySet\_Type

• PySlice\_AdjustIndices()

• PySlice\_GetIndices()

• PySlice\_GetIndicesEx()

• PySlice\_New()

• PySlice\_Type

• PySlice\_Unpack()

• PyState\_AddModule()

• PyState\_FindModule()

• PyState\_RemoveModule()

• PyStructSequence\_Desc

• PyStructSequence\_Field

• PyStructSequence\_GetItem()

• PyStructSequence\_New()

• PyStructSequence\_NewType()

• PyStructSequence\_SetItem()

• PySuper\_Type

• PySys\_AddWarnOption()

• PySys\_AddWarnOptionUnicode()

• PySys\_AddXOption()

• PySys\_FormatStderr()

• PySys\_FormatStdout()

• PySys\_GetObject()

• PySys\_GetXOptions()

• PySys\_HasWarnOptions()

• PySys\_ResetWarnOptions()

## The Python/C API, Release 3.10.15

• PySys\_SetArgv()

• PySys\_SetArgvEx()

• PySys\_SetObject()

• PySys\_SetPath()

• PySys\_WriteStderr()

• PySys\_WriteStdout()

• PyThreadState

• PyThreadState\_Clear()

• PyThreadState\_Delete()

• PyThreadState\_Get()

• PyThreadState\_GetDict()

• PyThreadState\_GetFrame()

• PyThreadState\_GetID()

• PyThreadState\_GetInterpreter()

• PyThreadState\_New()

• PyThreadState\_SetAsyncExc()

• PyThreadState\_Swap()

• PyThread\_GetInfo()

• PyThread\_ReInitTLS()

• PyThread\_acquire\_lock()

• PyThread\_acquire\_lock\_timed()

• PyThread\_allocate\_lock()

• PyThread\_create\_key()

• PyThread\_delete\_key()

• PyThread\_delete\_key\_value()

• PyThread\_exit\_thread()

• PyThread\_free\_lock()

• PyThread\_get\_key\_value()

• PyThread\_get\_stacksize()

• PyThread\_get\_thread\_ident()

• PyThread\_get\_thread\_native\_id()

• PyThread\_init\_thread()

• PyThread\_release\_lock()

• PyThread\_set\_key\_value()

• PyThread\_set\_stacksize()

• PyThread\_start\_new\_thread()

• PyThread\_tss\_alloc()

• PyThread\_tss\_create()

• PyThread\_tss\_delete()

• PyThread\_tss\_free()

• PyThread\_tss\_get()

• PyThread\_tss\_is\_created()

• PyThread\_tss\_set()

• PyTraceBack\_Here()

• PyTraceBack\_Print()

• PyTraceBack\_Type

• PyTupleIter\_Type

• PyTuple\_GetItem()

• PyTuple\_GetSlice()

• PyTuple\_New()

• PyTuple\_Pack()

• PyTuple\_SetItem()

• PyTuple\_Size()

• PyTuple\_Type

• PyTypeObject

• PyType\_ClearCache()

• PyType\_FromModuleAndSpec()

• PyType\_FromSpec()

• PyType\_FromSpecWithBases()

• PyType\_GenericAlloc()

• PyType\_GenericNew()

• PyType\_GetFlags()

• PyType\_GetModule()

• PyType\_GetModuleState()

• PyType\_GetSlot()

• PyType\_IsSubtype()

• PyType\_Modified()

• PyType\_Ready()

• PyType\_Slot

• PyType\_Spec

• PyType\_Type

• PyUnicodeDecodeError\_Create()

• PyUnicodeDecodeError\_GetEncoding()

• PyUnicodeDecodeError\_GetEnd()

• PyUnicodeDecodeError\_GetObject()

• PyUnicodeDecodeError\_GetReason()

• PyUnicodeDecodeError\_GetStart()

• PyUnicodeDecodeError\_SetEnd()

## The Python/C API, Release 3.10.15

• PyUnicodeDecodeError\_SetReason()

• PyUnicodeDecodeError\_SetStart()

• PyUnicodeEncodeError\_GetEncoding()

• PyUnicodeEncodeError\_GetEnd()

• PyUnicodeEncodeError\_GetObject()

• PyUnicodeEncodeError\_GetReason()

• PyUnicodeEncodeError\_GetStart()

• PyUnicodeEncodeError\_SetEnd()

• PyUnicodeEncodeError\_SetReason()

• PyUnicodeEncodeError\_SetStart()

• PyUnicodeIter\_Type

• PyUnicodeTranslateError\_GetEnd()

• PyUnicodeTranslateError\_GetObject()

• PyUnicodeTranslateError\_GetReason()

• PyUnicodeTranslateError\_GetStart()

• PyUnicodeTranslateError\_SetEnd()

• PyUnicodeTranslateError\_SetReason()

• PyUnicodeTranslateError\_SetStart()

• PyUnicode\_Append()

• PyUnicode\_AppendAndDel()

• PyUnicode\_AsASCIIString()

• PyUnicode\_AsCharmapString()

• PyUnicode\_AsDecodedObject()

• PyUnicode\_AsDecodedUnicode()

• PyUnicode\_AsEncodedObject()

• PyUnicode\_AsEncodedString()

• PyUnicode\_AsEncodedUnicode()

• PyUnicode\_AsLatin1String()

• PyUnicode\_AsMBCSString()

• PyUnicode\_AsRawUnicodeEscapeString()

• PyUnicode\_AsUCS4()

• PyUnicode\_AsUCS4Copy()

• PyUnicode\_AsUTF16String()

• PyUnicode\_AsUTF32String()

• PyUnicode\_AsUTF8AndSize()

• PyUnicode\_AsUTF8String()

• PyUnicode\_AsUnicodeEscapeString()

• PyUnicode\_AsWideChar()

• PyUnicode\_AsWideCharString()

• PyUnicode\_BuildEncodingMap()

• PyUnicode\_Compare()

• PyUnicode\_CompareWithASCIIString()

• PyUnicode\_Concat()

• PyUnicode\_Contains()

• PyUnicode\_Count()

• PyUnicode\_Decode()

• PyUnicode\_DecodeASCII()

• PyUnicode\_DecodeCharmap()

• PyUnicode\_DecodeCodePageStateful()

• PyUnicode\_DecodeFSDefault()

• PyUnicode\_DecodeFSDefaultAndSize()

• PyUnicode\_DecodeLatin1()

• PyUnicode\_DecodeLocale()

• PyUnicode\_DecodeLocaleAndSize()

• PyUnicode\_DecodeMBCS()

• PyUnicode\_DecodeMBCSStateful()

• PyUnicode\_DecodeRawUnicodeEscape()

• PyUnicode\_DecodeUTF16()

• PyUnicode\_DecodeUTF16Stateful()

• PyUnicode\_DecodeUTF32()

• PyUnicode\_DecodeUTF32Stateful()

• PyUnicode\_DecodeUTF7()

• PyUnicode\_DecodeUTF7Stateful()

• PyUnicode\_DecodeUTF8()

• PyUnicode\_DecodeUTF8Stateful()

• PyUnicode\_DecodeUnicodeEscape()

• PyUnicode\_EncodeCodePage()

• PyUnicode\_EncodeFSDefault()

• PyUnicode\_EncodeLocale()

• PyUnicode\_FSConverter()

• PyUnicode\_FSDecoder()

• PyUnicode\_Find()

• PyUnicode\_FindChar()

• PyUnicode\_Format()

• PyUnicode\_FromEncodedObject()

• PyUnicode\_FromFormat()

• PyUnicode\_FromFormatV()

• PyUnicode\_FromObject()

## The Python/C API, Release 3.10.15

• PyUnicode\_FromOrdinal()

• PyUnicode\_FromString()

• PyUnicode\_FromStringAndSize()

• PyUnicode\_FromWideChar()

• PyUnicode\_GetDefaultEncoding()

• PyUnicode\_GetLength()

• PyUnicode\_GetSize()

• PyUnicode\_InternFromString()

• PyUnicode\_InternImmortal()

• PyUnicode\_InternInPlace()

• PyUnicode\_IsIdentifier()

• PyUnicode\_Join()

• PyUnicode\_Partition()

• PyUnicode\_RPartition()

• PyUnicode\_RSplit()

• PyUnicode\_ReadChar()

• PyUnicode\_Replace()

• PyUnicode\_Resize()

• PyUnicode\_RichCompare()

• PyUnicode\_Split()

• PyUnicode\_Splitlines()

• PyUnicode\_Substring()

• PyUnicode\_Tailmatch()

• PyUnicode\_Translate()

• PyUnicode\_Type

• PyUnicode\_WriteChar()

• PyVarObject

• PyVarObject.ob\_base

• PyVarObject.ob\_size

• PyWeakReference

• PyWeakref\_GetObject()

• PyWeakref\_NewProxy()

• PyWeakref\_NewRef()

• PyWrapperDescr\_Type

• PyWrapper\_New()

• PyZip\_Type

• Py\_AddPendingCall()

• Py\_AtExit()

• Py\_BEGIN\_ALLOW\_THREADS

• Py\_BLOCK\_THREADS

• Py\_BuildValue()

• Py\_BytesMain()

• Py\_CompileString()

• Py\_DecRef()

• Py\_DecodeLocale()

• Py\_END\_ALLOW\_THREADS

• Py\_EncodeLocale()

• Py\_EndInterpreter()

• Py\_EnterRecursiveCall()

• Py\_Exit()

• Py\_FatalError()

• Py\_FileSystemDefaultEncodeErrors

• Py\_FileSystemDefaultEncoding

• Py\_Finalize()

• Py\_FinalizeEx()

• Py\_GenericAlias()

• Py\_GenericAliasType

• Py\_GetBuildInfo()

• Py\_GetCompiler()

• Py\_GetCopyright()

• Py\_GetExecPrefix()

• Py\_GetPath()

• Py\_GetPlatform()

• Py\_GetPrefix()

• Py\_GetProgramFullPath()

• Py\_GetProgramName()

• Py\_GetPythonHome()

• Py\_GetRecursionLimit()

• Py\_GetVersion()

• Py\_HasFileSystemDefaultEncoding

• Py\_IncRef()

• Py\_Initialize()

• Py\_InitializeEx()

• Py\_Is()

• Py\_IsFalse()

• Py\_IsInitialized()

• Py\_IsNone()

• Py\_IsTrue()

## The Python/C API, Release 3.10.15

• Py\_LeaveRecursiveCall()

• Py\_Main()

• Py\_MakePendingCalls()

• Py\_NewInterpreter()

• Py\_NewRef()

• Py\_ReprEnter()

• Py\_ReprLeave()

• Py\_SetPath()

• Py\_SetProgramName()

• Py\_SetPythonHome()

• Py\_SetRecursionLimit()

• Py\_UCS4

• Py\_UNBLOCK\_THREADS

• Py\_UTF8Mode

• Py\_VaBuildValue()

• Py\_XNewRef()

• Py\_intptr\_t

• Py\_ssize\_t

• Py\_uintptr\_t

• allocfunc

• binaryfunc

• descrgetfunc

• descrsetfunc

• destructor

• getattrfunc

• getattrofunc

• getiterfunc

• getter

• hashfunc

• initproc

• inquiry

• iternextfunc

• lenfunc

• newfunc

• objobjargproc

• objobjproc

• reprfunc

• richcmpfunc

• setattrfunc

• setattrofunc

• setter

• ssizeargfunc

• ssizeobjargproc

• ssizessizeargfunc

• ssizessizeobjargproc

• symtable

• ternaryfunc

• traverseproc

• unaryfunc

• visitproc

## THE VERY HIGH LEVEL LAYER

The functions in this chapter will let you execute Python source code given in a file or a buffer, but they will not let you interact in a more detailed way with the interpreter.

Several of these functions accept a start symbol from the grammar as a parameter. The available start symbols are Py\_eval\_input, Py\_file\_input, and Py\_single\_input. These are described following the functions which accept them as parameters.

Note also that several of these functions take FILE\* parameters. One particular issue which needs to be handled carefully is that the FILE structure for different C libraries can be different and incompatible. Under Windows (at least), it is possible for dynamically linked extensions to actually use different libraries, so care should be taken that FILE\* parameters are only passed to these functions if it is certain that they were created by the same library that the Python runtime is using.

int **Py\_Main**(int argc, wchar\_t \*\*argv)

Part of the Stable ABI. The main program for the standard interpreter. This is made available for programs which embed Python. The argc and argv parameters should be prepared exactly as those which are passed to a C program’s main() function (converted to wchar\_t according to the user’s locale). It is important to note that the argument list may be modified (but the contents of the strings pointed to by the argument list are not). The return value will be 0 if the interpreter exits normally (i.e., without an exception), 1 if the interpreter exits due to an exception, or 2 if the parameter list does not represent a valid Python command line.

Note that if an otherwise unhandled SystemExit is raised, this function will not return 1, but exit the process, as long as Py\_InspectFlag is not set.

int **Py\_BytesMain**(int argc, char \*\*argv)

Part of the Stable ABI since version 3.8. Similar to Py\_Main() but argv is an array of bytes strings.

New in version 3.8.

int **PyRun\_AnyFile**(FILE \*fp, **const** char \*filename) This is a simplified interface to PyRun\_AnyFileExFlags() below, leaving closeit set to 0 and flags set to NULL.

int **PyRun\_AnyFileFlags**(FILE \*fp, **const** char \*filename, PyCompilerFlags \*flags) This is a simplified interface to PyRun\_AnyFileExFlags() below, leaving the closeit argument set to 0.

int **PyRun\_AnyFileEx**(FILE \*fp, **const** char \*filename, int closeit) This is a simplified interface to PyRun\_AnyFileExFlags() below, leaving the flags argument set to NULL.

int **PyRun\_AnyFileExFlags**(FILE \*fp, **const** char \*filename, int closeit, PyCompilerFlags \*flags)

If fp refers to a file associated with an interactive device (console or terminal input or Unix pseudo-terminal), return the value of PyRun\_InteractiveLoop(), otherwise return the result of PyRun\_SimpleFile(). filename is decoded from the filesystem encoding (sys. getfilesystemencoding()). If filename is NULL, this function uses "???" as the filename. If closeit is true, the file is closed before PyRun\_SimpleFileExFlags() returns.

int **PyRun\_SimpleString**(**const** char \*command) This is a simplified interface to PyRun\_SimpleStringFlags() below, leaving the PyCompilerFlags\* argument set to NULL.

int **PyRun\_SimpleStringFlags**(**const** char \*command, PyCompilerFlags \*flags) Executes the Python source code from command in the \_\_main\_\_ module according to the flags argument. If \_\_main\_\_ does not already exist, it is created. Returns 0 on success or -1 if an exception was raised. If there was an error, there is no way to get the exception information. For the meaning of flags, see below. Note that if an otherwise unhandled SystemExit is raised, this function will not return -1, but exit the process, as long as Py\_InspectFlag is not set.

int **PyRun\_SimpleFile**(FILE \*fp, **const** char \*filename) This is a simplified interface to PyRun\_SimpleFileExFlags() below, leaving closeit set to 0 and flags set to NULL.

int **PyRun\_SimpleFileExFlags**(FILE \*fp, **const** char \*filename, int closeit, PyCompilerFlags \*flags) Similar to PyRun\_SimpleStringFlags(), but the Python source code is read from fp instead of an in-memory string. filename should be the name of the file, it is decoded from filesystem encoding and error handler. If closeit is true, the file is closed before PyRun\_SimpleFileExFlags() returns.

**Note:** On Windows, fp should be opened as binary mode (e.g. fopen(filename, "rb")). Otherwise, Python may not handle script file with LF line ending correctly.

int **PyRun\_InteractiveOne**(FILE \*fp, **const** char \*filename) This is a simplified interface to PyRun\_InteractiveOneFlags() below, leaving flags set to NULL.

int **PyRun\_InteractiveOneFlags**(FILE \*fp, **const** char \*filename, PyCompilerFlags \*flags) Read and execute a single statement from a file associated with an interactive device according to the flags argument. The user will be prompted using sys.ps1 and sys.ps2. filename is decoded from the filesystem encoding and error handler.

Returns 0 when the input was executed successfully, -1 if there was an exception, or an error code from the errcode.h include file distributed as part of Python if there was a parse error. (Note that errcode.h is not included by Python.h, so must be included specifically if needed.)

int **PyRun\_InteractiveLoop**(FILE \*fp, **const** char \*filename) This is a simplified interface to PyRun\_InteractiveLoopFlags() below, leaving flags set to NULL.

int **PyRun\_InteractiveLoopFlags**(FILE \*fp, **const** char \*filename, PyCompilerFlags \*flags) Read and execute statements from a file associated with an interactive device until EOF is reached. The user will be prompted using sys.ps1 and sys.ps2. filename is decoded from the filesystem encoding and error handler. Returns 0 at EOF or a negative number upon failure.

int (\***PyOS\_InputHook**)(void) Part of the Stable ABI. Can be set to point to a function with the prototype int func(void). The function will be called when Python’s interpreter prompt is about to become idle and wait for user input from the terminal. The return value is ignored. Overriding this hook can be used to integrate the interpreter’s prompt with other event loops, as done in the Modules/\_tkinter.c in the Python source code.

char \*(\***PyOS\_ReadlineFunctionPointer**)(FILE\*, FILE\*, **const** char\*) Can be set to point to a function with the prototype char \*func(FILE \*stdin, FILE \*stdout, char \*prompt), overriding the default function used to read a single line of input at the interpreter’s prompt. The function is expected to output the string prompt if it’s not NULL, and then read a line of input from the provided standard input file, returning the resulting string. For example, The readline module sets this hook to provide line-editing and tab-completion features.

The result must be a string allocated by PyMem\_RawMalloc() or PyMem\_RawRealloc(), or NULL if an error occurred.

Changed in version 3.4: The result must be allocated by PyMem\_RawMalloc() or PyMem\_RawRealloc(), instead of being allocated by PyMem\_Malloc() or PyMem\_Realloc().

PyObject \***PyRun\_String**(**const** char \*str, int start, PyObject \*globals, PyObject \*locals) Return value: New reference. This is a simplified interface to PyRun\_StringFlags() below, leaving flags set to NULL.

PyObject \***PyRun\_StringFlags**(**const** char \*str, int start, PyObject \*globals, PyObject \*locals, Py-CompilerFlags \*flags)

Return value: New reference. Execute Python source code from str in the context specified by the objects globals and locals with the compiler flags specified by flags. globals must be a dictionary; locals can be any object that implements the mapping protocol. The parameter start specifies the start token that should be used to parse the source code.

Returns the result of executing the code as a Python object, or NULL if an exception was raised.

PyObject \***PyRun\_File**(FILE \*fp, **const** char \*filename, int start, PyObject \*globals, PyObject \*locals) Return value: New reference. This is a simplified interface to PyRun\_FileExFlags() below, leaving closeit set to 0 and flags set to NULL.

PyObject \***PyRun\_FileEx**(FILE \*fp, **const** char \*filename, int start, PyObject \*globals, PyObject \*locals, int closeit)

Return value: New reference. This is a simplified interface to PyRun\_FileExFlags() below, leaving flags set to NULL.

PyObject \***PyRun\_FileFlags**(FILE \*fp, **const** char \*filename, int start, PyObject \*globals, PyObject \*locals, PyCompilerFlags \*flags)

Return value: New reference. This is a simplified interface to PyRun\_FileExFlags() below, leaving closeit set to 0.

PyObject \***PyRun\_FileExFlags**(FILE \*fp, **const** char \*filename, int start, PyObject \*globals, PyObject \*locals, int closeit, PyCompilerFlags \*flags)

Return value: New reference. Similar to PyRun\_StringFlags(), but the Python source code is read from fp instead of an in-memory string. filename should be the name of the file, it is decoded from the filesystem encoding and error handler. If closeit is true, the file is closed before PyRun\_FileExFlags() returns.

PyObject \***Py\_CompileString**(**const** char \*str, **const** char \*filename, int start)

Return value: New reference. Part of the Stable ABI. This is a simplified interface to Py\_CompileStringFlags() below, leaving flags set to NULL.

PyObject \***Py\_CompileStringFlags**(**const** char \*str, **const** char \*filename, int start, PyCompiler-Flags \*flags)

Return value: New reference. This is a simplified interface to Py\_CompileStringExFlags() below, with optimize set to -1.

PyObject \***Py\_CompileStringObject**(**const** char \*str, PyObject \*filename, int start, PyCompiler-

Flags \*flags, int optimize)

Return value: New reference. Parse and compile the Python source code in str, returning the resulting code object. The start token is given by start; this can be used to constrain the code which can be compiled and should be Py\_eval\_input, Py\_file\_input, or Py\_single\_input. The filename specified by filename is used to construct the code object and may appear in tracebacks or SyntaxError exception messages. This returns NULL if the code cannot be parsed or compiled.

The integer optimize specifies the optimization level of the compiler; a value of -1 selects the optimization level of the interpreter as given by -O options. Explicit levels are 0 (no optimization; \_\_debug\_\_ is true), 1 (asserts are removed, \_\_debug\_\_ is false) or 2 (docstrings are removed too).

New in version 3.4.

PyObject \***Py\_CompileStringExFlags**(**const** char \*str, **const** char \*filename, int start, PyCompil-

Return value: New reference. Like Py\_CompileStringObject(), but filename is a byte string decoded from the filesystem encoding and error handler.

New in version 3.2.

PyObject \***PyEval\_EvalCode**(PyObject \*co, PyObject \*globals, PyObject \*locals) Return value: New reference. Part of the Stable ABI. This is a simplified interface to

PyEval\_EvalCodeEx(), with just the code object, and global and local variables. The other arguments are set to NULL.

PyObject \***PyEval\_EvalCodeEx**(PyObject \*co, PyObject \*globals, PyObject \*locals, PyObject \***const**

\*args, int argcount, PyObject \***const** \*kws, int kwcount, PyObject

\***const** \*defs, int defcount, PyObject \*kwdefs, PyObject \*closure)

Return value: New reference. Part of the Stable ABI. Evaluate a precompiled code object, given a particular environment for its evaluation. This environment consists of a dictionary of global variables, a mapping object of local variables, arrays of arguments, keywords and defaults, a dictionary of default values for keyword-only arguments and a closure tuple of cells.

## type PyFrameObject

Part of the Limited API (as an opaque struct). The C structure of the objects used to describe frame objects. The fields of this type are subject to change at any time.

## PyObject \*PyEval\_EvalFrame(PyFrameObject \*f)

Return value: New reference. Part of the Stable ABI. Evaluate an execution frame. This is a simplified interface to PyEval\_EvalFrameEx(), for backward compatibility.

## PyObject \*PyEval\_EvalFrameEx(PyFrameObject \*f, int throwflag)

Return value: New reference. Part of the Stable ABI. This is the main, unvarnished function of Python interpretation. The code object associated with the execution frame f is executed, interpreting bytecode and executing calls as needed. The additional throwflag parameter can mostly be ignored - if true, then it causes an exception to immediately be thrown; this is used for the throw() methods of generator objects.

Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception.

## int PyEval\_MergeCompilerFlags(PyCompilerFlags \*cf)

This function changes the flags of the current evaluation frame, and returns true on success, false on failure.

## int Py\_eval\_input

The start symbol from the Python grammar for isolated expressions; for use with Py\_CompileString().

## int Py\_file\_input

The start symbol from the Python grammar for sequences of statements as read from a file or other source; for use with Py\_CompileString(). This is the symbol to use when compiling arbitrarily long Python source code.

## int Py\_single\_input

The start symbol from the Python grammar for a single statement; for use with Py\_CompileString(). This is the symbol used for the interactive interpreter loop.

## struct PyCompilerFlags

This is the structure used to hold compiler flags. In cases where code is only being compiled, it is passed as int flags, and in cases where code is being executed, it is passed as PyCompilerFlags \*flags. In this case, from \_\_future\_\_ import can modify flags.

Whenever PyCompilerFlags \*flags is NULL, cf\_flags is treated as equal to 0, and any modification due to from \_\_future\_\_ import is discarded.

## int cf\_flags

Compiler flags.

## int cf\_feature\_version

cf\_feature\_version is the minor Python version. It should be initialized to PY\_MINOR\_VERSION.

The field is ignored by default, it is used if and only if PyCF\_ONLY\_AST flag is set in cf\_flags.

Changed in version 3.8: Added cf\_feature\_version field.

## int CO\_FUTURE\_DIVISION

This bit can be set in flags to cause division operator / to be interpreted as “true division” according to [**PEP 238**](https://www.python.org/dev/peps/pep-0238).

## REFERENCE COUNTING

The macros in this section are used for managing reference counts of Python objects.

## void Py\_INCREF(PyObject \*o)

Indicate taking a new strong reference to object o, indicating it is in use and should not be destroyed.

This function is usually used to convert a borrowed reference to a strong reference in-place. The Py\_NewRef() function can be used to create a new strong reference.

When done using the object, release it by calling Py\_DECREF().

The object must not be NULL; if you aren’t sure that it isn’t NULL, use Py\_XINCREF().

Do not expect this function to actually modify o in any way.

## void Py\_XINCREF(PyObject \*o)

Similar to Py\_INCREF(), but the object o can be NULL, in which case this has no effect.

See also Py\_XNewRef().

## PyObject \*Py\_NewRef(PyObject \*o)

Part of the Stable ABI since version 3.10. Create a new strong reference to an object: call Py\_INCREF() on o and return the object o.

When the strong reference is no longer needed, Py\_DECREF() should be called on it to release the reference.

The object o must not be NULL; use Py\_XNewRef() if o can be NULL.

For example:

```txt
Py_INcreF(obj);
self->attr = obj;
```

can be written as:

```txt
self->attr = Py_NewRef(obj);
```

See also Py\_INCREF().

New in version 3.10.

## PyObject \*Py\_XNewRef(PyObject \*o)

Part of the Stable ABI since version 3.10. Similar to Py\_NewRef(), but the object o can be NULL.

If the object o is NULL, the function just returns NULL.

New in version 3.10.

## void Py\_DECREF(PyObject \*o)

Release a strong reference to object o, indicating the reference is no longer used.

Once the last strong reference is released (i.e. the object’s reference count reaches 0), the object’s type’s deallocation function (which must not be NULL) is invoked.

This function is usually used to delete a strong reference before exiting its scope.

The object must not be NULL; if you aren’t sure that it isn’t NULL, use Py\_ \_XDECREF().

Do not expect this function to actually modify o in any way.

**Warning:** The deallocation function can cause arbitrary Python code to be invoked (e.g. when a class instance with a \_\_del\_\_() method is deallocated). While exceptions in such code are not propagated, the executed code has free access to all Python global variables. This means that any object that is reachable from a global variable should be in a consistent state before Py\_DECREF() is invoked. For example, code to delete an object from a list should copy a reference to the deleted object in a temporary variable, update the list data structure, and then call Py\_DECREF() for the temporary variable.

## void Py\_XDECREF (PyObject \*o)

Similar to Py\_DECREF() , but the object o can be NULL, in which case this has no effect. The same warning from Py\_DECREF() applies here as well.

## void Py\_CLEAR (PyObject \*o)

Release a strong reference for object o. The object may be NULL, in which case the macro has no effect; otherwise the effect is the same as for Py\_DECREF(), except that the argument is also set to NULL. The warning for Py\_DECREF() does not apply with respect to the object passed because the macro carefully uses a temporary variable and sets the argument to NULL before releasing the reference.

It is a good idea to use this macro whenever releasing a reference to an object that might be traversed during garbage collection.

## void Py\_IncRef (PyObject \*o)

Part of the Stable ABI. Indicate taking a new strong reference to object o. A function version of Py\_XINCREF(). It can be used for runtime dynamic embedding of Python.

## void Py\_DecRef (PyObject \*o)

Part of the Stable ABI. Release a strong reference to object o. A function version of Py\_XDECREF() . It can be used for runtime dynamic embedding of Python.

The following functions or macros are only for use within the interpreter core: \_Py\_Dealloc(), Py \_ForgetReference(), \_Py\_NewReference(), as well as the global variable \_ \_Py\_ \_RefTotal.

## EXCEPTION HANDLING

The functions described in this chapter will let you handle and raise Python exceptions. It is important to understand some of the basics of Python exception handling. It works somewhat like the POSIX errno variable: there is a global indicator (per thread) of the last error that occurred. Most C API functions don’t clear this on success, but will set it to indicate the cause of the error on failure. Most C API functions also return an error indicator, usually NULL if they are supposed to return a pointer, or -1 if they return an integer (exception: the PyArg\_\* functions return 1 for success and 0 for failure).

Concretely, the error indicator consists of three object pointers: the exception’s type, the exception’s value, and the traceback object. Any of those pointers can be NULL if non-set (although some combinations are forbidden, for example you can’t have a non-NULL traceback if the exception type is NULL).

When a function must fail because some function it called failed, it generally doesn’t set the error indicator; the function it called already set it. It is responsible for either handling the error and clearing the exception or returning after cleaning up any resources it holds (such as object references or memory allocations); it should not continue normally if it is not prepared to handle the error. If returning due to an error, it is important to indicate to the caller that an error has been set. If the error is not handled or carefully propagated, additional calls into the Python/C API may not behave as intended and may fail in mysterious ways.

**Note:** The error indicator is **not** the result of sys.exc\_info(). The former corresponds to an exception that is not yet caught (and is therefore still propagating), while the latter returns an exception after it is caught (and has therefore stopped propagating).

## 5.1 Printing and clearing

void **PyErr\_Clear**()

Part of the Stable ABI. Clear the error indicator. If the error indicator is not set, there is no effect.

void **PyErr\_PrintEx**(int set\_sys\_last\_vars)

Part of the Stable ABI. Print a standard traceback to sys.stderr and clear the error indicator. **Unless** the error is a SystemExit, in that case no traceback is printed and the Python process will exit with the error code specified by the SystemExit instance.

Call this function **only** when the error indicator is set. Otherwise it will cause a fatal error!

If set\_sys\_last\_vars is nonzero, the variables sys.last\_type, sys.last\_value and sys. last\_traceback will be set to the type, value and traceback of the printed exception, respectively.

void **PyErr\_Print**()

Part of the Stable ABI. Alias for PyErr\_PrintEx(1).

void **PyErr\_WriteUnraisable**(PyObject \*obj)

Part of the Stable ABI. Call sys.unraisablehook() using the current exception and obj argument.

This utility function prints a warning message to sys.stderr when an exception has been set but it is impossible for the interpreter to actually raise the exception. It is used, for example, when an exception occurs in an \_\_del\_\_() method.

The function is called with a single argument obj that identifies the context in which the unraisable exception occurred. If possible, the repr of obj will be printed in the warning message.

An exception must be set when calling this function.

## 5.2 Raising exceptions

These functions help you set the current thread’s error indicator. For convenience, some of these functions will always return a NULL pointer for use in a return statement.

## void PyErr\_SetString(PyObject \*type, const char \*message)

Part of the Stable ABI. This is the most common way to set the error indicator. The first argument specifies the exception type; it is normally one of the standard exceptions, e.g. PyExc\_RuntimeError. You need not create a new strong reference to it (e.g. with Py\_INCREF()). The second argument is an error message; it is decoded from 'utf-8'.

## void PyErr\_SetObject(PyObject \*type, PyObject \*value)

Part of the Stable ABI. This function is similar to PyErr\_SetString() but lets you specify an arbitrary Python object for the “value” of the exception.

## PyObject \*PyErr\_Format(PyObject \*exception, const char \*format, ...)

Return value: Always NULL. Part of the Stable ABI. This function sets the error indicator and returns NULL. exception should be a Python exception class. The format and subsequent parameters help format the error message; they have the same meaning and values as in PyUnicode\_FromFormat(). format is an ASCII-encoded string.

## PyObject \*PyErr\_FormatV(PyObject \*exception, const char \*format, va\_list vargs)

Return value: Always NULL. Part of the Stable ABI since version 3.5. Same as PyErr\_Format(), but taking a va\_list argument rather than a variable number of arguments.

New in version 3.5.

## void PyErr\_SetNone(PyObject \*type)

Part of the Stable ABI. This is a shorthand for PyErr\_SetObject(type, Py\_None).

## int PyErr\_BadArgument()

Part of the Stable ABI. This is a shorthand for PyErr\_SetString(PyExc\_TypeError, message), where message indicates that a built-in operation was invoked with an illegal argument. It is mostly for internal use.

## PyObject \*PyErr\_NoMemory()

Return value: Always NULL. Part of the Stable ABI. This is a shorthand for PyErr\_SetNone(PyExc\_MemoryError); it returns NULL so an object allocation function can write return PyErr\_NoMemory(); when it runs out of memory.

## PyObject \*PyErr\_SetFromErrno(PyObject \*type)

Return value: Always NULL. Part of the Stable ABI. This is a convenience function to raise an exception when a C library function has returned an error and set the C variable errno. It constructs a tuple object whose first item is the integer errno value and whose second item is the corresponding error message (gotten from strerror()), and then calls PyErr\_SetObject(type, object). On Unix, when the errno value is EINTR, indicating an interrupted system call, this calls PyErr\_CheckSignals(), and if that set the error indicator, leaves it set to that. The function always returns NULL, so a wrapper function around a system call can write return PyErr\_SetFromErrno(type); when the system call returns an error.

## PyObject \*PyErr\_SetFromErrnoWithFilenameObject(PyObject \*type, PyObject \*filenameOb-

Return value: Always NULL. Part of the Stable ABI. Similar to PyErr\_SetFromErrno(), with the additional behavior that if filenameObject is not NULL, it is passed to the constructor of type as a third parameter. In the case of OSError exception, this is used to define the filename attribute of the exception instance.

## PyObject \*PyErr\_SetFromErrnoWithFilenameObjects(PyObject \*type, PyObject \*filenameOb-

ject, PyObject \*filenameObject2) Return value: Always NULL. Part of the Stable ABI since version 3.7. Similar to

PyErr\_SetFromErrnoWithFilenameObject(), but takes a second filename object, for raising errors when a function that takes two filenames fails.

New in version 3.4.

## PyObject \*PyErr\_SetFromErrnoWithFilename(PyObject \*type, const char \*filename)

Return value: Always NULL. Part of the Stable ABI. Similar to PyErr\_SetFromErrnoWithFilenameObject(), but the filename is given as a C string. filename is decoded from the filesystem encoding and error handler.

## PyObject \*PyErr\_SetFromWindowsErr(int ierr)

Return value: Always NULL. Part of the Stable ABI on Windows since version 3.7. This is a convenience function to raise WindowsError. If called with ierr of 0, the error code returned by a call to GetLastError() is used instead. It calls the Win32 function FormatMessage() to retrieve the Windows description of error code given by ierr or GetLastError(), then it constructs a tuple object whose first item is the ierr value and whose second item is the corresponding error message (gotten from FormatMessage()), and then calls PyErr\_SetObject(PyExc\_WindowsError, object). This function always returns NULL.

Availability: Windows.

PyObject \***PyErr\_SetExcFromWindowsErr**(PyObject \*type, int ierr) Return value: Always NULL. Part of the Stable ABI on Windows since version 3.7. Similar to PyErr\_SetFromWindowsErr(), with an additional parameter specifying the exception type to be raised. Availability: Windows.

## PyObject \*PyErr\_SetFromWindowsErrWithFilename(int ierr, const char \*filename)

Return value: Always NULL. Part of the Stable ABI on Windows since version 3.7. Similar to PyErr\_SetFromWindowsErrWithFilenameObject(), but the filename is given as a C string. filename is decoded from the filesystem encoding (os.fsdecode()).

Availability: Windows.

PyObject \***PyErr\_SetExcFromWindowsErrWithFilenameObject**(PyObject \*type, int ierr, Py-Object \*filename)

Return value: Always NULL. Part of the Stable ABI on Windows since version 3.7. Similar to PyErr\_SetFromWindowsErrWithFilenameObject(), with an additional parameter specifying the exception type to be raised.

Availability: Windows.

PyObject \***PyErr\_SetExcFromWindowsErrWithFilenameObjects**(PyObject \*type, int ierr, Py-Object \*filename, PyObject \*filename2)

Return value: Always NULL. Part of the Stable ABI on Windows since version 3.7. Similar to PyErr\_SetExcFromWindowsErrWithFilenameObject(), but accepts a second filename object.

Availability: Windows.

New in version 3.4.

PyObject \***PyErr\_SetExcFromWindowsErrWithFilename**(PyObject \*type, int ierr, **const** char

Return value: Always NULL. Part of the Stable ABI on Windows since version 3.7. Similar to PyErr\_SetFromWindowsErrWithFilename(), with an additional parameter specifying the exception type to be raised.

Availability: Windows.

## PyObject \*PyErr\_SetImportError(PyObject \*msg, PyObject \*name, PyObject \*path)

Return value: Always NULL. Part of the Stable ABI since version 3.7. This is a convenience function to raise ImportError. msg will be set as the exception’s message string. name and path, both of which can be NULL, will be set as the ImportError’s respective name and path attributes.

New in version 3.3.

PyObject \***PyErr\_SetImportErrorSubclass**(PyObject \*exception, PyObject \*msg, PyObject \*name, PyObject \*path)

Return value: Always NULL. Part of the Stable ABI since version 3.6. Much like PyErr\_SetImportError() but this function allows for specifying a subclass of ImportError to raise.

New in version 3.6.

v id P E \_S t L ti Ob t P Ob t \* l i t li i t l\_ t o y rr yn ax oca on jec ( y jec fi ename, n neno, n co offse )

Set file, line, and offset information for the current exception. If the current exception is not a SyntaxError, then it sets additional attributes, which make the exception printing subsystem think the exception is a SyntaxError.

New in version 3.4.

void **PyErr\_SyntaxLocationEx**(**const** char \*filename, int lineno, int col\_offset) Part of the Stable ABI since version 3.7. Like PyErr\_SyntaxLocationObject(), but filename is a byte string decoded from the filesystem encoding and error handler.

New in version 3.2.

void **PyErr\_SyntaxLocation**(**const** char \*filename, int lineno)

Part of the Stable ABI. Like PyErr\_SyntaxLocationEx(), but the col\_offset parameter is omitted.

void **PyErr\_BadInternalCall**()

Part of the Stable ABI. This is a shorthand for PyErr\_SetString(PyExc\_SystemError, message), where message indicates that an internal operation (e.g. a Python/C API function) was invoked with an illegal argument. It is mostly for internal use.

## 5.3 Issuing warnings

Use these functions to issue warnings from C code. They mirror similar functions exported by the Python warnings module. They normally print a warning message to sys.stderr; however, it is also possible that the user has specified that warnings are to be turned into errors, and in that case they will raise an exception. It is also possible that the functions raise an exception because of a problem with the warning machinery. The return value is 0 if no exception is raised, or -1 if an exception is raised. (It is not possible to determine whether a warning message is actually printed, nor what the reason is for the exception; this is intentional.) If an exception is raised, the caller should do its normal exception handling (for example, Py\_DECREF() owned references and return an error value).

int **PyErr\_WarnEx**(PyObject \*category, **const** char \*message, Py\_ssize\_t stack\_level)

Part of the Stable ABI. Issue a warning message. The category argument is a warning category (see below) or NULL; the message argument is a UTF-8 encoded string. stack\_level is a positive number giving a number of stack frames; the warning will be issued from the currently executing line of code in that stack frame. A stack\_level of 1 is the function calling PyErr\_WarnEx(), 2 is the function above that, and so forth.

Warning categories must be subclasses of PyExc\_Warning; PyExc\_Warning is a subclass of PyExc\_Exception; the default warning category is PyExc\_RuntimeWarning. The standard Python warning categories are available as global variables whose names are enumerated at Standard Warning Categories.

For information about warning control, see the documentation for the warnings module and the -W option in the command line documentation. There is no C API for warning control.

int **PyErr\_WarnExplicitObject**(PyObject \*category, PyObject \*message, PyObject \*filename, int lineno, PyObject \*module, PyObject \*registry)

Issue a warning message with explicit control over all warning attributes. This is a straightforward wrapper around the Python function warnings.warn\_explicit(); see there for more information. The module and registry arguments may be set to NULL to get the default effect described there.

New in version 3.4.

int **PyErr\_WarnExplicit**(PyObject \*category, **const** char \*message, **const** char \*filename, int lineno, **const** char \*module, PyObject \*registry)

Part of the Stable ABI. Similar to PyErr\_WarnExplicitObject() except that message and module are UTF-8 encoded strings, and filename is decoded from the filesystem encoding and error handler.

## int PyErr\_WarnFormat(PyObject \*category, Py\_ssize\_t stack\_level, const char \*format, ...)

Part of the Stable ABI. Function similar to PyErr\_WarnEx(), but use PyUnicode\_FromFormat() to format the warning message. format is an ASCII-encoded string.

New in version 3.2.

int **PyErr\_ResourceWarning**(PyObject \*source, Py\_ssize\_t stack\_level, **const** char \*format, ...) Part of the Stable ABI since version 3.6. Function similar to PyErr\_WarnFormat(), but category is ResourceWarning and it passes source to warnings.WarningMessage(). N i i 3 6 ew n vers on . .

## 5.4 Querying the error indicator

## PyObject \*PyErr\_Occurred()

Return value: Borrowed reference. Part of the Stable ABI. Test whether the error indicator is set. If set, return the exception type (the first argument to the last call to one of the PyErr\_Set\* functions or to PyErr\_Restore()). If not set, return NULL. You do not own a reference to the return value, so you do not need to Py\_DECREF() it.

The caller must hold the GIL.

**Note:** Do not compare the return value to a specific exception; use PyErr\_ExceptionMatches() instead, shown below. (The comparison could easily fail since the exception may be an instance instead of a class, in the case of a class exception, or it may be a subclass of the expected exception.)

## int PyErr\_ExceptionMatches(PyObject \*exc)

Part of the Stable ABI. Equivalent to PyErr\_GivenExceptionMatches(PyErr\_Occurred(), exc). This should only be called when an exception is actually set; a memory access violation will occur if no exception has been raised.

## int PyErr\_GivenExceptionMatches(PyObject \*given, PyObject \*exc)

Part of the Stable ABI. Return true if the given exception matches the exception type in exc. If exc is a class object, this also returns true when given is an instance of a subclass. If exc is a tuple, all exception types in the tuple (and recursively in subtuples) are searched for a match.

## void PyErr\_Fetch(PyObject \*\*ptype, PyObject \*\*pvalue, PyObject \*\*ptraceback)

Part of the Stable ABI. Retrieve the error indicator into three variables whose addresses are passed. If the error indicator is not set, set all three variables to NULL. If it is set, it will be cleared and you own a reference to each object retrieved. The value and traceback object may be NULL even when the type object is not.

**Note:** This function is normally only used by code that needs to catch exceptions or by code that needs to save and restore the error indicator temporarily, e.g.:

```c
{
    PyObject *type, *value, *traceback;
    PyErr_Fetch(&type, &value, &traceback);

    /* ... code that might produce other errors ... */

    PyErr_Restore(type, value, traceback);
}
txt
void PyErr_Restore (PyObject *type, PyObject *value, PyObject *traceback)
```

Part of the Stable ABI. Set the error indicator from the three objects. If the error indicator is already set, it is cleared first. If the objects are NULL, the error indicator is cleared. Do not pass a NULL type and non-NULL value or traceback. The exception type should be a class. Do not pass an invalid exception type or value. (Violating these rules will cause subtle problems later.) This call takes away a reference to each object: you must own a reference to each object before the call and after the call you no longer own these references. (If you don’t understand this, don’t use this function. I warned you.)

**Note:** This function is normally only used by code that needs to save and restore the error indicator temporarily. Use PyErr\_Fetch() to save the current error indicator.

## void PyErr\_NormalizeException(PyObject \*\*exc, PyObject \*\*val, PyObject \*\*tb)

Part of the Stable ABI. Under certain circumstances, the values returned by PyErr\_Fetch() below can be “unnormalized”, meaning that \*exc is a class object but \*val is not an instance of the same class. This function can be used to instantiate the class in that case. If the values are already normalized, nothing happens. The delayed normalization is implemented to improve performance.

**Note:** This function does not implicitly set the \_\_traceback\_\_ attribute on the exception value. If setting the traceback appropriately is desired, the following additional snippet is needed:

```txt
if (tb != NULL) {
    PyException_SetTraceback(val, tb);
}
```

void **PyErr\_GetExcInfo**(PyObject \*\*ptype, PyObject \*\*pvalue, PyObject \*\*ptraceback)

Part of the Stable ABI since version 3.7. Retrieve the exception info, as known from sys.exc\_info(). This refers to an exception that was already caught, not to an exception that was freshly raised. Returns new references for the three objects, any of which may be NULL. Does not modify the exception info state.

**Note:** This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use PyErr\_SetExcInfo() to restore or clear the exception state.

New in version 3.3.

## void PyErr\_SetExcInfo(PyObject \*type, PyObject \*value, PyObject \*traceback)

Part of the Stable ABI since version 3.7. Set the exception info, as known from sys.exc\_info(). This refers to an exception that was already caught, not to an exception that was freshly raised. This function steals the references of the arguments. To clear the exception state, pass NULL for all three arguments. For general rules about the three arguments, see PyErr\_Restore().

**Note:** This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use PyErr\_GetExcInfo() to read the exception state.

New in version 3.3.

## 5.5 Signal Handling

## int PyErr\_CheckSignals()

Part of the Stable ABI. This function interacts with Python’s signal handling.

If the function is called from the main thread and under the main Python interpreter, it checks whether a signal has been sent to the processes and if so, invokes the corresponding signal handler. If the signal module is supported, this can invoke a signal handler written in Python.

The function attempts to handle all pending signals, and then returns 0. However, if a Python signal handler raises an exception, the error indicator is set and the function returns -1 immediately (such that other pending signals may not have been handled yet: they will be on the next PyErr\_CheckSignals() invocation).

If the function is called from a non-main thread, or under a non-main Python interpreter, it does nothing and returns 0.

This function can be called by long-running C code that wants to be interruptible by user requests (such as by pressing Ctrl-C).

**Note:** The default Python signal handler for SIGINT raises the KeyboardInterrupt exception.

## void PyErr\_SetInterrupt()

Part of the Stable ABI. Simulate the effect of a SIGINT signal arriving. This is equivalent to PyErr\_SetInterruptEx(SIGINT).

**Note:** This function is async-signal-safe. It can be called without the GIL and from a C signal handler.

## int PyErr\_SetInterruptEx(int signum)

Part of the Stable ABI since version 3.10. Simulate the effect of a signal arriving. The next time PyErr\_CheckSignals() is called, the Python signal handler for the given signal number will be called.

This function can be called by C code that sets up its own signal handling and wants Python signal handlers to be invoked as expected when an interruption is requested (for example when the user presses Ctrl-C to interrupt an operation).

If the given signal isn’t handled by Python (it was set to signal.SIG\_DFL or signal.SIG\_IGN), it will be ignored.

If signum is outside of the allowed range of signal numbers, -1 is returned. Otherwise, 0 is returned. The error indicator is never changed by this function.

**Note:** This function is async-signal-safe. It can be called without the GIL and from a C signal handler.

New in version 3.10.

## int PySignal\_SetWakeupFd(int fd)

This utility function specifies a file descriptor to which the signal number is written as a single byte whenever a signal is received. fd must be non-blocking. It returns the previous such file descriptor.

The value -1 disables the feature; this is the initial state. This is equivalent to signal.set\_wakeup\_fd() in Python, but without any error checking. fd should be a valid file descriptor. The function should only be called from the main thread.

Changed in version 3.5: On Windows, the function now also supports socket handles.

## 5.6 Exception Classes

PyObject \***PyErr\_NewException**(**const** char \*name, PyObject \*base, PyObject \*dict)

Return value: New reference. Part of the Stable ABI. This utility function creates and returns a new exception class. The name argument must be the name of the new exception, a C string of the form module. classname. The base and dict arguments are normally NULL. This creates a class object derived from Exception (accessible in C as PyExc\_Exception).

The \_\_module\_\_ attribute of the new class is set to the first part (up to the last dot) of the name argument, and the class name is set to the last part (after the last dot). The base argument can be used to specify alternate base classes; it can either be only one class or a tuple of classes. The dict argument can be used to specify a dictionary of class variables and methods.

PyObject \***PyErr\_NewExceptionWithDoc**(**const** char \*name, **const** char \*doc, PyObject \*base,

PyObject \*dict)

Return value: New reference. Part of the Stable ABI. Same as PyErr\_NewException(), except that the new exception class can easily be given a docstring: If doc is non-NULL, it will be used as the docstring for the exception class.

New in version 3.2.

## 5.7 Exception Objects

## PyObject \*PyException\_GetTraceback (PyObject \*ex)

Return value: New reference. Part of the Stable ABI. Return the traceback associated with the exception as a new reference, as accessible from Python through \_\_traceback\_\_. If there is no traceback associated, this returns NULL.

## int PyException\_SetTraceback(PyObject \*ex, PyObject \*tb)

Part of the Stable ABI. Set the traceback associated with the exception to tb. Use Py\_None to clear it.

PyObject \***PyException\_GetContext** (PyObject \*ex)

Return value: New reference. Part of the Stable ABI. Return the context (another exception instance during whose handling ex was raised) associated with the exception as a new reference, as accessible from Python through \_\_context\_\_. If there is no context associated, this returns NULL.

void **PyException\_SetContext** (PyObject \*ex, PyObject \*ctx)

Part of the Stable ABI. Set the context associated with the exception to ctx. Use NULL to clear it. There is no type check to make sure that ctx is an exception instance. This steals a reference to ctx.

PyObject \***PyException\_GetCause**(PyObject \*ex)

Return value: New reference. Part of the Stable ABI. Return the cause (either an exception instance, or None, set by raise ... from ...) associated with the exception as a new reference, as accessible from Python through \_\_cause\_\_.

void **PyException\_SetCause**(PyObject \*ex, PyObject \*cause)

Part of the Stable ABI. Set the cause associated with the exception to cause. Use NULL to clear it. There is no type check to make sure that cause is either an exception instance or None. This steals a reference to cause.

suppress\_context\_\_ is implicitly set to True by this function.

```txt
int PyUnicodeEncodeError_GetEnd (PyObject *exc, Py_ssize_t *end)
c
int PyUnicodeEncodeError_GetStart (PyObject *exc, Py_ssize_t *start)
vba
PyObject *PyUnicodeDecodeError_GetObject(PyObject *exc)
txt
int PyUnicodeDecodeError_SetStart (PyObject *exc, Py_ssize_t start)
txt
int PyUnicodeEncodeError_SetStart (PyObject *exc, Py_ssize_t start)
```

## 5.8 Unicode Exception Objects

The following functions are used to create and modify Unicode exceptions from C.

PyObject \***PyUnicodeDecodeError\_Create**(**const** char \*encoding, **const** char \*object, Py\_ssize\_t length, Py\_ssize\_t start, Py\_ssize\_t end, **const** char \*reason)

Return value: New reference. Part of the Stable ABI. Create a UnicodeDecodeError object with the attributes encoding, object, length, start, end and reason. encoding and reason are UTF-8 encoded strings.

PyObject \***PyUnicodeEncodeError\_Create**(**const** char \*encoding, **const** Py\_UNICODE \*ob-

Return value: New reference. Create a UnicodeEncodeError object with the attributes encoding, object, length, start, end and reason. encoding and reason are UTF-8 encoded strings.

Deprecated since version 3.3: 3.11

Py\_UNICODE is deprecated since Python 3.3. Please migrate to PyObject\_CallFunction(PyExc\_UnicodeEncodeError, "sOnns", ...).

PyObject \***PyUnicodeTranslateError\_Create**(**const** Py\_UNICODE \*object, Py\_ssize\_t length,

Return value: New reference. Create a UnicodeTranslateError object with the attributes object, length, start, end and reason. reason is a UTF-8 encoded string.

Deprecated since version 3.3: 3.11

```txt
Py_UNICODE is deprecated since Python 3.3. Please migrate to PyObject_CallFunction(PyExc_UnicodeTranslateError, "Onns", ...).
```

PyObject \***PyUnicodeDecodeError\_GetEncoding**(PyObject \*exc)

PyObject \***PyUnicodeEncodeError\_GetEncoding**(PyObject \*exc) Return value: New reference. Part of the Stable ABI. Return the encoding attribute of the given exception object.

PyObject \***PyUnicodeTranslateError\_GetObject**(PyObject \*exc) Return value: New reference. Part of the Stable ABI. Return the object attribute of the given exception object.

```c
int PyUnicodeDecodeError_GetStart (PyObject *exc, Py_ssize_t *start)
```

int **PyUnicodeTranslateError\_GetStart**(PyObject \*exc, Py\_ssize\_t \*start) Part of the Stable ABI. Get the start attribute of the given exception object and place it into \*start. start must not be NULL. Return 0 on success, -1 on failure.

int **PyUnicodeTranslateError\_SetStart**(PyObject \*exc, Py\_ssize\_t start) Part of the Stable ABI. Set the start attribute of the given exception object to start. Return 0 on success, -1 on failure.

int **PyUnicodeTranslateError\_GetEnd**(PyObject \*exc, Py\_ssize\_t \*end) Part of the Stable ABI. Get the end attribute of the given exception object and place it into \*end. end must not be NULL. Return 0 on success, -1 on failure.

```txt
int PyUnicodeTranslateError_SetEnd (PyObject *exc, Py_ssize_t end)
    Part of the Stable ABI. Set the end attribute of the given exception object to end. Return 0 on success, -1 on failure.

PyObject *PyUnicodeDecodeError_GetReason (PyObject *exc)
PyObject *PyUnicodeEncodeError_GetReason (PyObject *exc)
PyObject *PyUnicodeTranslateError_GetReason (PyObject *exc)
    Return value: New reference. Part of the Stable ABI. Return the reason attribute of the given exception object.
int PyUnicodeDecodeError_SetReason (PyObject *exc, const char *reason)
int PyUnicodeEncodeError_SetReason (PyObject *exc, const char *reason)
int PyUnicodeTranslateError_SetReason (PyObject *exc, const char *reason)
    Part of the Stable ABI. Set the reason attribute of the given exception object to reason. Return 0 on success, -1 on failure.
```

## 5.9 Recursion Control

These two functions provide a way to perform safe recursive calls at the C level, both in the core and in extension modules. They are needed if the recursive code does not necessarily invoke Python code (which tracks its recursion depth automatically). They are also not needed for tp\_call implementations because the call protocol takes care of recursion handling.

## int Py\_EnterRecursiveCall(const char \*where)

Part of the Stable ABI since version 3.9. Marks a point where a recursive C-level call is about to be performed.

If USE\_STACKCHECK is defined, this function checks if the OS stack overflowed using PyOS\_CheckStack(). In this is the case, it sets a MemoryError and returns a nonzero value.

The function then checks if the recursion limit is reached. If this is the case, a RecursionError is set and a nonzero value is returned. Otherwise, zero is returned.

where should be a UTF-8 encoded string such as " in instance check" to be concatenated to the RecursionError message caused by the recursion depth limit.

Changed in version 3.9: This function is now also available in the limited API.

## void Py\_LeaveRecursiveCall(void)

Part of the Stable ABI since version 3.9. Ends a Py\_EnterRecursiveCall(). Must be called once for each successful invocation of Py\_EnterRecursiveCall().

Changed in version 3.9: This function is now also available in the limited API.

Properly implementing tp\_repr for container types requires special recursion handling. In addition to protecting the stack, tp\_repr also needs to track objects to prevent cycles. The following two functions facilitate this functionality. Effectively, these are the C equivalent to reprlib.recursive\_repr().

## int Py\_ReprEnter(PyObject \*object)

Part of the Stable ABI. Called at the beginning of the tp\_repr implementation to detect cycles.

If the object has already been processed, the function returns a positive integer. In that case the tp\_repr implementation should return a string object indicating a cycle. As examples, dict objects return {...} and list objects return [...].

The function will return a negative integer if the recursion limit is reached. In that case the tp\_repr implementation should typically return NULL.

Otherwise, the function returns zero and the tp\_repr implementation can continue normally.

## void Py\_ReprLeave (PyObject \*object)

Part of the Stable ABI. Ends a Py\_ReprEnter() Must be called once for each invocation of Py\_ReprEnter() that returns zero.

## 5.10 Standard Exceptions

All standard Python exceptions are available as global variables whose names are PyExc\_ followed by the Python exception name. These have the type PyObject\* ; they are all class objects. For completeness, here are all the variables:

| C Name | Python Name | Notes |
| --- | --- | --- |
| PyExc_BaseException | BaseException | 1 |
| PyExc_Exception | Exception | 1 |
| PyExc_ArithmeticError | ArithmeticError | 1 |
| PyExc_AssertionError | AssertionError |  |
| PyExc_AttributeError | AttributeError |  |
| PyExc_BlockingIOError | BlockingIOError |  |
| PyExc_BrokenPipeError | BrokenPipeError |  |
| PyExc_BufferError | BufferError |  |
| PyExc_ChildProcessError | ChildProcessError |  |
| PyExc_ConnectionAbortedE | rrCoornnectionAbortedError |  |
| PyExc_ConnectionError | ConnectionError |  |
| PyExc_ConnectionRefusedE | rrCoornnectionRefusedError |  |
| PyExc_ConnectionResetErr | orConnectionResetError |  |
| PyExc_EOFError | EOFError |  |
| PyExc_FileExistsError | FileExistsError |  |
| PyExc_FileNotFoundError | FileNotFoundError |  |
| PyExc_FloatingPointError | FloatingPointError |  |
| PyExc_GeneratorExit | GeneratorExit |  |
| PyExc_ImportError | ImportError |  |
| PyExc_IndentationError | IndentationError |  |
| PyExc_IndexError | IndexError |  |
| PyExc_InterruptedError | InterruptedError |  |
| PyExc_IsADirectoryError | IsADirectoryError |  |
| PyExc_KeyError | KeyError |  |
| PyExc_KeyboardInterrupt | KeyboardInterrupt |  |
| PyExc_LookupError | LookupError | 1 |
| PyExc_MemoryError | MemoryError |  |
| PyExc_ModuleNotFoundErro | rModuleNotFoundError |  |
| PyExc_NameError | NameError |  |
| PyExc_NotADirectoryError | NotADirectoryError |  |
| PyExc_NotImplementedErro | rNotImplementedError |  |
| PyExc_OSError | OSError | 1 |
| PyExc_OverflowError | OverflowError |  |
| PyExc_PermissionError | PermissionError |  |
| PyExc_ProcessLookupError | ProcessLookupError |  |
| PyExc_RecursionError | RecursionError |  |
| PyExc_ReferenceError | ReferenceError |  |
| PyExc_RuntimeError | RuntimeError |  |
| PyExc_StopAsyncIteration | StopAsyncIteration |  |
| PyExc_StopIteration | StopIteration |  |
| PyExc_SyntaxError | SyntaxError |  |
| PyExc_SystemError | SystemError |  |
| PyExc_SystemExit | SystemExit |  |
| PyExc_TabError | TabError |  |
| PyExc_TimeoutError | TimeoutError |  |
| PyExc_TypeError | TypeError |  |
| PyExc_UnboundLocalError | UnboundLocalError |  |

continues on next page

Table 1 – continued from previous page

| C Name | Python Name | Notes |
| --- | --- | --- |
| PyExc_UnicodeDecodeError | UnicodeDecodeError |  |
| PyExc_UnicodeEncodeError | UnicodeEncodeError |  |
| PyExc_UnicodeError | UnicodeError |  |
| PyExc_UnicodeTranslateEr | roUrnicodeTranslateError |  |
| PyExc_ValueError | ValueError |  |
| PyExc_ZeroDivisionError | ZeroDivisionError |  |

New in version 3.3: PyExc\_BlockingIOError, PyExc\_BrokenPipeError, PyExc\_ChildProcessError, PyExc\_ConnectionError, PyExc\_ConnectionAbortedError, PyExc\_ConnectionRefusedError, PyExc\_ConnectionResetError, PyExc\_FileExistsError, PyExc\_FileNotFoundError, PyExc\_InterruptedError, PyExc\_IsADirectoryError, PyExc\_NotADirectoryError, PyExc\_PermissionError, PyExc\_ProcessLookupError and PyExc\_TimeoutError were introduced following [**PEP 3151**](https://www.python.org/dev/peps/pep-3151).

New in version 3.5: PyExc\_StopAsyncIteration and PyExc\_RecursionError.

New in version 3.6: PyExc\_ModuleNotFoundError.

These are compatibility aliases to PyExc\_OSError:

| C Name | Notes |
| --- | --- |
| PyExc_EnvironmentError |  |
| PyExc_IOError |  |
| PyExc_WindowsError | 2 |

Changed in version 3.3: These aliases used to be separate exception types. Notes:

## 5.11 Standard Warning Categories

All standard Python warning categories are available as global variables whose names are PyExc\_ followed by the Python exception name. These have the type PyObject\*; they are all class objects. For completeness, here are all the variables:

| C Name | Python Name | Notes |
| --- | --- | --- |
| PyExc_Warning | Warning | 3 |
| PyExc_BytesWarning | BytesWarning |  |
| PyExc_DeprecationWarning | DeprecationWarning |  |
| PyExc_FutureWarning | FutureWarning |  |
| PyExc_ImportWarning | ImportWarning |  |
| PyExc_PendingDeprecationWarning | PendingDeprecationWarning |  |
| PyExc_ResourceWarning | ResourceWarning |  |
| PyExc_RuntimeWarning | RuntimeWarning |  |
| PyExc_SyntaxWarning | SyntaxWarning |  |
| PyExc_UnicodeWarning | UnicodeWarning |  |
| PyExc_UserWarning | UserWarning |  |

New in version 3.2: PyExc\_ResourceWarning.

Notes:

  1 This is a base class for other standard exceptions.

  2 Only defined on Windows; protect code that uses this by testing that the preprocessor macro MS\_WINDOWS is defined.

  3 This is a base class for other standard warning categories.

## UTILITIES

The functions in this chapter perform various utility tasks, ranging from helping C code be more portable across platforms, using Python modules from C, and parsing function arguments and constructing Python values from C values.

## 6.1 Operating System Utilities

## PyObject \*PyOS\_FSPath(PyObject \*path)

Return value: New reference. Part of the Stable ABI since version 3.6. Return the file system representation for path. If the object is a str or bytes object, then a new strong reference is returned. If the object implements the os.PathLike interface, then \_\_fspath\_\_() is returned as long as it is a str or bytes object. Otherwise TypeError is raised and NULL is returned.

New in version 3.6.

## int Py\_FdIsInteractive(FILE \*fp, const char \*filename)

Return true (nonzero) if the standard I/O file fp with name filename is deemed interactive. This is the case for files for which isatty(fileno(fp)) is true. If the global flag Py\_InteractiveFlag is true, this function also returns true if the filename pointer is NULL or if the name is equal to one of the strings '&lt;stdin&gt;' or '???'.

## void PyOS\_BeforeFork()

Part of the Stable ABI on platforms with fork() since version 3.7. Function to prepare some internal state before a process fork. This should be called before calling fork() or any similar function that clones the current process. Only available on systems where fork() is defined.

**Warning:** The C fork() call should only be made from the “main” thread (of the “main” interpreter). The same is true for PyOS\_BeforeFork().

## New in version 3.7.

## void PyOS\_AfterFork\_Parent()

Part of the Stable ABI on platforms with fork() since version 3.7. Function to update some internal state after a process fork. This should be called from the parent process after calling fork() or any similar function that clones the current process, regardless of whether process cloning was successful. Only available on systems where fork() is defined.

**Warning:** The C fork() call should only be made from the “main” thread (of the “main” interpreter). The same is true for PyOS\_AfterFork\_Parent().

New in version 3.7.

## void PyOS\_AfterFork\_Child()

Part of the Stable ABI on platforms with fork() since version 3.7. Function to update internal interpreter state

after a process fork. This must be called from the child process after calling fork(), or any similar function that clones the current process, if there is any chance the process will call back into the Python interpreter. Only available on systems where fork() is defined.

**Warning:** The C fork() call should only be made from the “main” thread (of the “main” interpreter). The same is true for PyOS\_AfterFork\_Child().

## New in version 3.7.

os.register\_at\_fork() allows registering custom Python functions to be called by PyOS\_BeforeFork(), PyOS\_AfterFork\_Parent() and PyOS\_AfterFork\_Child().

Part of the Stable ABI on platforms with fork(). Function to update some internal state after a process fork; this should be called in the new process if the Python interpreter will continue to be used. If a new executable is loaded into the new process, this function does not need to be called.

Deprecated since version 3.7: This function is superseded by PyOS\_AfterFork\_Child().

Part of the Stable ABI on platforms with USE\_STACKCHECK since version 3.7. Return true when the interpreter runs out of stack space. This is a reliable check, but is only available when USE\_STACKCHECK is defined (currently on Windows using the Microsoft Visual C++ compiler). USE\_STACKCHECK will be defined automatically; you should never change the definition in your own code.

PyOS\_sighandler\_t **PyOS\_getsig**(int i) Part of the Stable ABI. Return the current signal handler for signal i. This is a thin wrapper around either sigaction() or signal(). Do not call those functions directly! PyOS\_sighandler\_t is a typedef alias for void (\*)int.

PyOS\_sighandler\_t **PyOS\_setsig**(int i, PyOS\_sighandler\_t h) Part of the Stable ABI. Set the signal handler for signal i to be h; return the old signal handler. This is a thin wrapper around either sigaction() or signal(). Do not call those functions directly! PyOS\_sighandler\_t is a typedef alias for void (\*)int.

wchar\_t \***Py\_DecodeLocale**(**const** char \*arg, size\_t \*size) Part of the Stable ABI since version 3.7.

**Warning:** This function should not be called directly: use the PyConfig API with the PyConfig\_SetBytesString() function which ensures that Python is preinitialized. This function must not be called before Python is preinitialized and so that the LC\_CTYPE locale is properly configured: see the Py\_PreInitialize() function.

Decode a byte string from the filesystem encoding and error handler. If the error handler is surrogateescape error handler, undecodable bytes are decoded as characters in range U+DC80..U+DCFF; and if a byte sequence can be decoded as a surrogate character, the bytes are escaped using the surrogateescape error handler instead of decoding them.

Return a pointer to a newly allocated wide character string, use PyMem\_RawFree() to free the memory. If size is not NULL, write the number of wide characters excluding the null character into \*size

Return NULL on decoding error or memory allocation error. If size is not NULL, \*size is set to (size\_t)-1 on memory error or set to (size\_t)-2 on decoding error.

The filesystem encoding and error handler are selected by PyConfig\_Read(): see filesystem\_encoding and filesystem\_errors members of PyConfig.

Decoding errors should never happen, unless there is a bug in the C library.

Use the Py\_EncodeLocale() function to encode the character string back to a byte string.

## See also:

The PyUnicode\_DecodeFSDefaultAndSize() and PyUnicode\_DecodeLocaleAndSize() functions.

New in version 3.5.

Changed in version 3.7: The function now uses the UTF-8 encoding in the Python UTF-8 Mode.

Changed in version 3.8: The function now uses the UTF-8 encoding on Windows if Py\_LegacyWindowsFSEncodingFlag is zero;

char \***Py\_EncodeLocale**(**const** wchar\_t \*text, size\_t \*error\_pos)

Part of the Stable ABI since version 3.7. Encode a wide character string to the filesystem encoding and error handler. If the error handler is surrogateescape error handler, surrogate characters in the range U+DC80..U+DCFF are converted to bytes 0x80..0xFF.

Return a pointer to a newly allocated byte string, use PyMem\_Free() to free the memory. Return NULL on encoding error or memory allocation error.

If error\_pos is not NULL, \*error\_pos is set to (size\_t)-1 on success, or set to the index of the invalid character on encoding error.

The filesystem encoding and error handler are selected by PyConfig\_Read(): see filesystem\_encoding and filesystem\_errors members of PyConfig.

Use the Py\_DecodeLocale() function to decode the bytes string back to a wide character string.

**Warning:** This function must not be called before Python is preinitialized and so that the LC\_CTYPE locale is properly configured: see the Py\_PreInitialize() function.

## See also:

The PyUnicode\_EncodeFSDefault() and PyUnicode\_EncodeLocale() functions.

New in version 3.5.

Changed in version 3.7: The function now uses the UTF-8 encoding in the Python UTF-8 Mode.

Changed in version 3.8: The function now uses the UTF-8 encoding on Windows if Py\_LegacyWindowsFSEncodingFlag is zero.

## 6.2 System Functions

These are utility functions that make functionality from the sys module accessible to C code. They all work with the current interpreter thread’s sys module’s dict, which is contained in the internal thread state structure.

PyObject \***PySys\_GetObject**(**const** char \*name)

Return value: Borrowed reference. Part of the Stable ABI. Return the object name from the sys module or NULL if it does not exist, without setting an exception.

int **PySys\_SetObject**(**const** char \*name, PyObject \*v)

Part of the Stable ABI. Set name in the sys module to v unless v is NULL, in which case name is deleted from the sys module. Returns 0 on success, -1 on error.

void **PySys\_ResetWarnOptions**()

Part of the Stable ABI. Reset sys.warnoptions to an empty list. This function may be called prior to Py\_Initialize().

void **PySys\_AddWarnOption**(**const** wchar\_t \*s)

Part of the Stable ABI. Append s to sys.warnoptions. This function must be called prior to Py\_Initialize() in order to affect the warnings filter list.

## void PySys\_AddWarnOptionUnicode(PyObject \*unicode)

Part of the Stable ABI. Append unicode to sys.warnoptions.

Note: this function is not currently usable from outside the CPython implementation, as it must be called prior to the implicit import of warnings in Py\_Initialize() to be effective, but can’t be called until enough of the runtime has been initialized to permit the creation of Unicode objects.

## void PySys\_SetPath(const wchar\_t \*path)

Part of the Stable ABI. Set sys.path to a list object of paths found in path which should be a list of paths separated with the platform’s search path delimiter (: on Unix, ; on Windows).

## void PySys\_WriteStdout(const char \*format, ...)

Part of the Stable ABI. Write the output string described by format to sys.stdout. No exceptions are raised, even if truncation occurs (see below).

format should limit the total size of the formatted output string to 1000 bytes or less – after 1000 bytes, the output string is truncated. In particular, this means that no unrestricted “%s” formats should occur; these should be limited using “%.&lt;N&gt;s” where &lt;N&gt; is a decimal number calculated so that &lt;N&gt; plus the maximum size of other formatted text does not exceed 1000 bytes. Also watch out for “%f”, which can print hundreds of digits for very large numbers.

If a problem occurs, or sys.stdout is unset, the formatted message is written to the real (C level) stdout.

## void PySys\_WriteStderr(const char \*format, ...)

Part of the Stable ABI. As PySys\_WriteStdout(), but write to sys.stderr or stderr instead.

## void PySys\_FormatStdout(const char \*format, ...)

Part of the Stable ABI. Function similar to PySys\_WriteStdout() but format the message using PyUnicode\_FromFormatV() and don’t truncate the message to an arbitrary length.

New in version 3.2.

## void PySys\_FormatStderr(const char \*format, ...)

Part of the Stable ABI. As PySys\_FormatStdout(), but write to sys.stderr or stderr instead.

New in version 3.2.

## void PySys\_AddXOption(const wchar\_t \*s)

Part of the Stable ABI since version 3.7. Parse s as a set of -X options and add them to the current options mapping as returned by PySys\_GetXOptions(). This function may be called prior to Py\_Initialize(). New in version 3.2.

## PyObject \*PySys\_GetXOptions()

Return value: Borrowed reference. Part of the Stable ABI since version 3.7. Return the current dictionary of -X options, similarly to sys.\_xoptions. On error, NULL is returned and an exception is set.

New in version 3.2.

## int PySys\_Audit(const char \*event, const char \*format, ...)

Raise an auditing event with any active hooks. Return zero for success and non-zero with an exception set on failure.

If any hooks have been added, format and other arguments will be used to construct a tuple to pass. Apart from N, the same format characters as used in Py\_BuildValue() are available. If the built value is not a tuple, it will be added into a single-element tuple. (The N format option consumes a reference, but since there is no way to know whether arguments to this function will be consumed, using it may cause reference leaks.)

Note that # format characters should always be treated as Py\_ssize\_t, regardless of whether PY\_SSIZE\_T\_CLEAN was defined.

sys.audit() performs the same function from Python code.

New in version 3.8.

Changed in version 3.8.2: Require Py\_ssize\_t for # format characters. Previously, an unavoidable deprecation warning was raised.

## int PySys\_AddAuditHook(Py\_AuditHookFunction hook, void \*userData)

Append the callable hook to the list of active auditing hooks. Return zero on success and non-zero on failure. If the runtime has been initialized, also set an error on failure. Hooks added through this API are called for all interpreters created by the runtime.

The userData pointer is passed into the hook function. Since hook functions may be called from different runtimes, this pointer should not refer directly to Python state.

This function is safe to call before Py\_Initialize() When called after runtime initialization, existing audit hooks are notified and may silently abort the operation by raising an error subclassed from Exception (other errors will not be silenced).

The hook function is of type int (\*)**const** char \*event, PyObject \*args, void \*userData, where args is guaranteed to be a PyTupleObject. The hook function is always called with the GIL held by the Python interpreter that raised the event.

See [**PEP 578**](https://www.python.org/dev/peps/pep-0578) for a detailed description of auditing. Functions in the runtime and standard library that raise events are listed in the audit events table. Details are in each function’s documentation.

If the interpreter is initialized, this function raises a auditing event sys.addaudithook with no arguments. If any existing hooks raise an exception derived from Exception, the new hook will not be added and the exception is cleared. As a result, callers cannot assume that their hook has been added unless they control all existing hooks.

New in version 3.8.

## 6.3 Process Control

## void Py\_FatalError(const char \*message)

Part of the Stable ABI. Print a fatal error message and kill the process. No cleanup is performed. This function should only be invoked when a condition is detected that would make it dangerous to continue using the Python interpreter; e.g., when the object administration appears to be corrupted. On Unix, the standard C library function abort() is called which will attempt to produce a core file.

The Py\_FatalError() function is replaced with a macro which logs automatically the name of the current function, unless the Py\_LIMITED\_API macro is defined.

Changed in version 3.9: Log the function name automatically.

## void Py\_Exit(int status)

Part of the Stable ABI. Exit the current process. This calls Py\_FinalizeEx() and then calls the standard C library function exit(status). If Py\_FinalizeEx() indicates an error, the exit status is set to 120.

Changed in version 3.6: Errors from finalization no longer ignored.

## int Py\_AtExit(void (\*func))

Part of the Stable ABI. Register a cleanup function to be called by Py\_FinalizeEx() . The cleanup function will be called with no arguments and should return no value. At most 32 cleanup functions can be registered. When the registration is successful, Py\_AtExit() returns 0; on failure, it returns -1. The cleanup function registered last is called first. Each cleanup function will be called at most once. Since Python’s internal finalization will have completed before the cleanup function, no Python APIs should be called by func.

## 6.4 Importing Modules

PyObject \***PyImport\_ImportModule**(**const** char \*name)

Return value: New reference. Part of the Stable ABI. This is a simplified interface to PyImport\_ImportModuleEx() below, leaving the globals and locals arguments set to NULL and level set to 0. When the name argument contains a dot (when it specifies a submodule of a package), the fromlist argument is set to the list ['\*'] so that the return value is the named module rather than the top-level package containing it as would otherwise be the case. (Unfortunately, this has an additional side effect when name in fact specifies a subpackage instead of a submodule: the submodules specified in the package’s \_\_all\_\_ variable are loaded.) Return a new reference to the imported module, or NULL with an exception set on failure. A failing import of a module doesn’t leave the module in sys.modules.

This function always uses absolute imports.

PyObject \***PyImport\_ImportModuleNoBlock**(**const** char \*name)

Return value: New reference. Part of the Stable ABI. This function is a deprecated alias of PyImport\_ImportModule().

Changed in version 3.3: This function used to fail immediately when the import lock was held by another thread. In Python 3.3 though, the locking scheme switched to per-module locks for most purposes, so this function’s special behaviour isn’t needed anymore.

PyObject \***PyImport\_ImportModuleEx**(**const** char \*name, PyObject \*globals, PyObject \*locals, Py-

Object \*fromlist)

Return value: New reference. Import a module. This is best described by referring to the built-in Python function \_\_import\_\_().

The return value is a new reference to the imported module or top-level package, or NULL with an exception set on failure. Like for \_\_import\_\_(), the return value when a submodule of a package was requested is normally the top-level package, unless a non-empty fromlist was given.

Failing imports remove incomplete module objects, like with PyImport\_ImportModule().

PyObject \***PyImport\_ImportModuleLevelObject**(PyObject \*name, PyObject \*globals, PyObject

\*locals, PyObject \*fromlist, int level)

Return value: New reference. Part of the Stable ABI since version 3.7. Import a module. This is best described by referring to the built-in Python function \_\_import\_\_(), as the standard \_\_import\_\_() function calls this function directly.

The return value is a new reference to the imported module or top-level package, or NULL with an exception set on failure. Like for \_\_import\_\_(), the return value when a submodule of a package was requested is normally the top-level package, unless a non-empty fromlist was given.

New in version 3.3.

PyObject \***PyImport\_ImportModuleLevel**(**const** char \*name, PyObject \*globals, PyObject \*locals,

PyObject \*fromlist, int level Return value: New reference. Part of the Stable ABI. Similar to PyImport\_ImportModuleLevelObject(), but the name is a UTF-8 encoded string instead of a Unicode object.

Changed in version 3.3: Negative values for level are no longer accepted.

PyObject \***PyImport\_Import**(PyObject \*name)

Return value: New reference. Part of the Stable ABI. This is a higher-level interface that calls the current “import hook function” (with an explicit level of 0, meaning absolute import). It invokes the \_\_import\_\_() function from the \_\_builtins\_\_ of the current globals. This means that the import is done using whatever import hooks are installed in the current environment.

This function always uses absolute imports.

PyObject \***PyImport\_ReloadModule**(PyObject \*m)

Return value: New reference. Part of the Stable ABI. Reload a module. Return a new reference to the reloaded module, or NULL with an exception set on failure (the module still exists in this case).

## PyObject \*PyImport\_AddModuleObject(PyObject \*name)

Return value: Borrowed reference. Part of the Stable ABI since version 3.7. Return the module object corresponding to a module name. The name argument may be of the form package.module. First check the modules dictionary if there’s one there, and if not, create a new one and insert it in the modules dictionary. Return NULL with an exception set on failure.

**Note:** This function does not load or import the module; if the module wasn’t already loaded, you will get an empty module object. Use PyImport\_ImportModule() or one of its variants to import a module. Package structures implied by a dotted name for name are not created if not already present.

New in version 3.3.

## PyObject \*PyImport\_AddModule(const char \*name)

Return value: Borrowed reference. Part of the Stable ABI. Similar to PyImport\_AddModuleObject(), but the name is a UTF-8 encoded string instead of a Unicode object.

## PyObject \*PyImport\_ExecCodeModule(const char \*name, PyObject \*co)

Return value: New reference. Part of the Stable ABI. Given a module name (possibly of the form package. module) and a code object read from a Python bytecode file or obtained from the built-in function compile(), load the module. Return a new reference to the module object, or NULL with an exception set if an error occurred. name is removed from sys.modules in error cases, even if name was already in sys.modules on entry to PyImport\_ExecCodeModule(). Leaving incompletely initialized modules in sys.modules is dangerous, as imports of such modules have no way to know that the module object is an unknown (and probably damaged with respect to the module author’s intents) state.

The module’s \_\_spec\_\_ and \_\_loader\_\_ will be set, if not set already, with the appropriate values. The spec’s loader will be set to the module’s \_\_loader\_\_ (if set) and to an instance of SourceFileLoader otherwise.

The module’s \_\_file\_\_ attribute will be set to the code object’s co\_filename. If applicable, \_\_cached\_\_ will also be set.

This function will reload the module if it was already imported. See PyImport\_ReloadModule() for the intended way to reload a module.

If name points to a dotted name of the form package.module, any package structures not already created will still not be created.

See also PyImport\_ExecCodeModuleEx() and PyImport\_ExecCodeModuleWithPathnames().

PyObject \***PyImport\_ExecCodeModuleEx**(**const** char \*name, PyObject \*co, **const** char \*path-

name)

Return value: New reference. Part of the Stable ABI. Like PyImport\_ExecCodeModule(), but the file\_\_ attribute of the module object is set to pathname if it is non-NULL.

See also PyImport\_ExecCodeModuleWithPathnames().

PyObject \***PyImport\_ExecCodeModuleObject**(PyObject \*name, PyObject \*co, PyObject \*pathname,

PyObject \*cpathname)

Return value: New reference. Part of the Stable ABI since version 3.7. Like PyImport\_ExecCodeModuleEx(), but the \_\_cached\_\_ attribute of the module object is set to cpathname if it is non-NULL. Of the three functions, this is the preferred one to use.

New in version 3.3.

PyObject \***PyImport\_ExecCodeModuleWithPathnames**(**const** char \*name, PyObject \*co,

**const** char \*pathname, **const** char

\*cpathname)

Return value: New reference. Part of the Stable ABI. Like PyImport\_ExecCodeModuleObject(), but name, pathname and cpathname are UTF-8 encoded strings. Attempts are also made to figure out what the value for pathname should be from cpathname if the former is set to NULL.

New in version 3.2.

Changed in version 3.3: Uses imp.source\_from\_cache() in calculating the source path if only the bytecode path is provided.

## long PyImport\_GetMagicNumber()

Part of the Stable ABI. Return the magic number for Python bytecode files (a.k.a. .pyc file). The magic number should be present in the first four bytes of the bytecode file, in little-endian byte order. Returns -1 on error.

Changed in version 3.3: Return value of -1 upon failure.

## const char \*PyImport\_GetMagicTag()

Part of the Stable ABI. Return the magic tag string for [**PEP 3147**](https://www.python.org/dev/peps/pep-3147) format Python bytecode file names. Keep in mind that the value at sys.implementation.cache\_tag is authoritative and should be used instead of this function.

New in version 3.2.

## PyObject \*PyImport\_GetModuleDict()

Return value: Borrowed reference. Part of the Stable ABI. Return the dictionary used for the module administration (a.k.a. sys.modules). Note that this is a per-interpreter variable.

## PyObject \*PyImport\_GetModule(PyObject \*name)

Return value: New reference. Part of the Stable ABI since version 3.8. Return the already imported module with the given name. If the module has not been imported yet then returns NULL but does not set an error. Returns NULL and sets an error if the lookup failed.

New in version 3.7.

## PyObject \*PyImport\_GetImporter(PyObject \*path)

Return value: New reference. Part of the Stable ABI. Return a finder object for a sys.path/pkg.\_\_path item path, possibly by fetching it from the sys.path\_importer\_cache dict. If it wasn’t yet cached, traverse sys.path\_hooks until a hook is found that can handle the path item. Return None if no hook could; this tells our caller that the path based finder could not find a finder for this path item. Cache the result in sys.path\_importer\_cache. Return a new reference to the finder object.

## int PyImport\_ImportFrozenModuleObject(PyObject \*name)

Part of the Stable ABI since version 3.7. Load a frozen module named name. Return 1 for success, 0 if the module is not found, and -1 with an exception set if the initialization failed. To access the imported module on a successful load, use PyImport\_ImportModule(). (Note the misnomer — this function would reload the module if it was already imported.)

New in version 3.3.

Changed in version 3.4: The \_\_file\_\_ attribute is no longer set on the module.

## int PyImport\_ImportFrozenModule(const char \*name)

Part of the Stable ABI. Similar to PyImport\_ImportFrozenModuleObject(), but the name is a UTF-8 encoded string instead of a Unicode object.

## struct \_frozen

This is the structure type definition for frozen module descriptors, as generated by the **freeze** utility (see Tools/freeze/ in the Python source distribution). Its definition, found in Include/import.h, is:

```c
struct _frozen {
    const char *name;
    const unsigned char *code;
    int size;
};
```

## const struct \_frozen \*PyImport\_FrozenModules

This pointer is initialized to point to an array of \_frozen records, terminated by one whose members are all NULL or zero. When a frozen module is imported, it is searched in this table. Third-party code could play tricks with this to provide a dynamically created collection of frozen modules.

## int PyImport\_AppendInittab(const char \*name, PyObject \*(\*initfunc))void

Part of the Stable ABI. Add a single module to the existing table of built-in modules. This is a convenience

wrapper around PyImport\_ExtendInittab(), returning -1 if the table could not be extended. The new module can be imported by the name name, and uses the function initfunc as the initialization function called on the first attempted import. This should be called before Py\_Initialize().

## struct \_inittab

Structure describing a single entry in the list of built-in modules. Each of these structures gives the name and initialization function for a module built into the interpreter. The name is an ASCII encoded string. Programs which embed Python may use an array of these structures in conjunction with PyImport\_ExtendInittab() to provide additional built-in modules. The structure is defined in Include/import.h as:

```c
struct _inittab {
    const char *name;                 /* ASCII encoded string */
    PyObject* (*initfunc)(void);
};
```

## int PyImport\_ExtendInittab(struct \_inittab \*newtab)

Add a collection of modules to the table of built-in modules. The newtab array must end with a sentinel entry which contains NULL for the name field; failure to provide the sentinel value can result in a memory fault. Returns 0 on success or -1 if insufficient memory could be allocated to extend the internal table. In the event of failure, no modules are added to the internal table. This must be called before Py\_Initialize().

If Python is initialized multiple times, PyImport\_AppendInittab() or PyImport\_ExtendInittab() must be called before each Python initialization.

## 6.5 Data marshalling support

These routines allow C code to work with serialized objects using the same data format as the marshal module. There are functions to write data into the serialization format, and additional functions that can be used to read the data back. Files used to store marshalled data must be opened in binary mode.

Numeric values are stored with the least significant byte first.

The module supports two versions of the data format: version 0 is the historical version, version 1 shares interned strings in the file, and upon unmarshalling. Version 2 uses a binary format for floating point numbers. Py\_MARSHAL\_VERSION indicates the current file format (currently 2).

## void PyMarshal\_WriteLongToFile(long value, FILE \*file, int version)

Marshal a long integer, value, to file. This will only write the least-significant 32 bits of value; regardless of the size of the native long type. version indicates the file format.

This function can fail, in which case it sets the error indicator. Use PyErr\_Occurred() to check for that.

## void PyMarshal\_WriteObjectToFile(PyObject \*value, FILE \*file, int version)

Marshal a Python object, value, to file. version indicates the file format.

This function can fail, in which case it sets the error indicator. Use PyErr\_Occurred() to check for that.

## PyObject \*PyMarshal\_WriteObjectToString(PyObject \*value, int version)

Return value: New reference. Return a bytes object containing the marshalled representation of value. version indicates the file format.

The following functions allow marshalled values to be read back in.

## long PyMarshal\_ReadLongFromFile(FILE \*file)

Return a C long from the data stream in a FILE\* opened for reading. Only a 32-bit value can be read in using this function, regardless of the native size of long.

On error, sets the appropriate exception (EOFError) and returns -1.

## int PyMarshal\_ReadShortFromFile(FILE \*file)

Return a C short from the data stream in a FILE\* opened for reading. Only a 16-bit value can be read in using this function, regardless of the native size of short.

On error, sets the appropriate exception (EOFError) and returns -1.

PyObject \***PyMarshal\_ReadObjectFromFile**(FILE \*file)

Return value: New reference. Return a Python object from the data stream in a FILE\* opened for reading.

On error, sets the appropriate exception (EOFError, ValueError or TypeError) and returns NULL.

PyObject \***PyMarshal\_ReadLastObjectFromFile**(FILE \*file)

Return value: New reference. Return a Python object from the data stream in a FILE\* opened for reading. Unlike PyMarshal\_ReadObjectFromFile(), this function assumes that no further objects will be read from the file, allowing it to aggressively load file data into memory so that the de-serialization can operate from data in memory rather than reading a byte at a time from the file. Only use these variant if you are certain that you won’t be reading anything else from the file.

On error, sets the appropriate exception (EOFError, ValueError or TypeError) and returns NULL.

PyObject \***PyMarshal\_ReadObjectFromString**(**const** char \*data, Py\_ssize\_t len)

Return value: New reference. Return a Python object from the data stream in a byte buffer containing len bytes pointed to by data.

On error, sets the appropriate exception (EOFError, ValueError or TypeError) and returns NULL.

## 6.6 Parsing arguments and building values

These functions are useful when creating your own extensions functions and methods. Additional information and examples are available in extending-index.

The first three of these functions described, PyArg\_ParseTuple(), PyArg\_ParseTupleAndKeywords(), and PyArg\_Parse(), all use format strings which are used to tell the function about the expected arguments. The format strings use the same syntax for each of these functions.

## 6.6.1 Parsing arguments

A format string consists of zero or more “format units.” A format unit describes one Python object; it is usually a single character or a parenthesized sequence of format units. With a few exceptions, a format unit that is not a parenthesized sequence normally corresponds to a single address argument to these functions. In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that matches the format unit; and the entry in [square] brackets is the type of the C variable(s) whose address should be passed.

## Strings and buffers

These formats allow accessing an object as a contiguous chunk of memory. You don’t have to provide raw storage for the returned unicode or bytes area.

Unless otherwise stated, buffers are not NUL-terminated.

There are three ways strings and buffers can be converted to C:

• Formats such as y\* and s\* fill a Py\_buffer structure. This locks the underlying buffer so that the caller can subsequently use the buffer even inside a Py\_BEGIN\_ALLOW\_THREADS block without the risk of mutable data being resized or destroyed. As a result, **you have to call** PyBuffer\_Release() after you have finished processing the data (or in any early abort case).

• The es, es#, et and et# formats allocate the result buffer. **You have to call** PyMem\_Free() after you have finished processing the data (or in any early abort case).

• Other formats take a str or a read-only bytes-like object, such as bytes, and provide a const char \* pointer to its buffer. In this case the buffer is “borrowed”: it is managed by the corresponding Python object, and shares the lifetime of this object. You won’t have to release any memory yourself.

To ensure that the underlying buffer may be safely borrowed, the object’s PyBufferProcs. bf\_releasebuffer field must be NULL. This disallows common mutable objects such as bytearray, but also some read-only objects such as memoryview of bytes.

Besides this bf\_releasebuffer requirement, there is no check to verify whether the input object is immutable (e.g. whether it would honor a request for a writable buffer, or whether another thread can mutate the data).

**Note:** For all # variants of formats (s#, y#, etc.), the macro PY\_SSIZE\_T\_CLEAN must be defined before including Python.h. On Python 3.9 and older, the type of the length argument is Py\_ssize\_t if the PY\_SSIZE\_T\_CLEAN macro is defined, or int otherwise.

**s (str) [const char \*]** Convert a Unicode object to a C pointer to a character string. A pointer to an existing string is stored in the character pointer variable whose address you pass. The C string is NUL-terminated. The Python string must not contain embedded null code points; if it does, a ValueError exception is raised. Unicode objects are converted to C strings using 'utf-8' encoding. If this conversion fails, a UnicodeError is raised.

**Note:** This format does not accept bytes-like objects. If you want to accept filesystem paths and convert them to C character strings, it is preferable to use the O& format with PyUnicode\_FSConverter() as converter.

Changed in version 3.5: Previously, TypeError was raised when embedded null code points were encountered in the Python string.

**s\* (str or bytes-like object) [Py\_buffer]** This format accepts Unicode objects as well as bytes-like objects. It fills a Py\_buffer structure provided by the caller. In this case the resulting C string may contain embedded NUL bytes. Unicode objects are converted to C strings using 'utf-8' encoding.

**s# (str, read-only bytes-like object) [const char \*, Py\_ssize\_t]** Like s\*, except that it provides a borrowed buffer. The result is stored into two C variables, the first one a pointer to a C string, the second one its length. The string may contain embedded null bytes. Unicode objects are converted to C strings using 'utf-8' encoding.

**z (str or None) [const char \*]** Like s, but the Python object may also be None, in which case the C pointer is set to NULL.

**z\* (str, bytes-like object or None) [Py\_buffer]** Like s\*, but the Python object may also be None, in which case the buf member of the Py\_buffer structure is set to NULL.

**z# (str, read-only bytes-like object or None) [const char \*, Py\_ssize\_t]** Like s#, but the Python object may also be None, in which case the C pointer is set to NULL.

**y (read-only bytes-like object) [const char \*]** This format converts a bytes-like object to a C pointer to a borrowed character string; it does not accept Unicode objects. The bytes buffer must not contain embedded null bytes; if it does, a ValueError exception is raised.

Changed in version 3.5: Previously, TypeError was raised when embedded null bytes were encountered in the bytes buffer.

**y\* (bytes-like object) [Py\_buffer]** This variant on s\* doesn’t accept Unicode objects, only bytes-like objects. **This is the recommended way to accept binary data.**

**y# (read-only bytes-like object) [const char \*, Py\_ssize\_t]** This variant on s# doesn’t accept Unicode objects, only bytes-like objects.

**S (bytes) [PyBytesObject \*]** Requires that the Python object is a bytes object, without attempting any conversion. Raises TypeError if the object is not a bytes object. The C variable may also be declared as PyObject\*.

**Y (bytearray) [PyByteArrayObject \*]** Requires that the Python object is a bytearray object, without attempting any conversion. Raises TypeError if the object is not a bytearray object. The C variable may also be declared as PyObject\*.

**u (str) [const Py\_UNICODE \*]** Convert a Python Unicode object to a C pointer to a NUL-terminated buffer of Unicode characters. You must pass the address of a Py\_UNICODE pointer variable, which will be filled with the pointer to an existing Unicode buffer. Please note that the width of a Py\_UNICODE character depends on compilation options (it is either 16 or 32 bits). The Python string must not contain embedded null code points; if it does, a ValueError exception is raised.

Changed in version 3.5: Previously, TypeError was raised when embedded null code points were encountered in the Python string.

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsWideCharString().

**u# (str) [const Py\_UNICODE \*, Py\_ssize\_t]** This variant on u stores into two C variables, the first one a pointer to a Unicode data buffer, the second one its length. This variant allows null code points.

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsWideCharString().

**Z (str or None) [const Py\_UNICODE \*]** Like u, but the Python object may also be None, in which case the Py\_UNICODE pointer is set to NULL.

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsWideCharString().

**Z# (str or None) [const Py\_UNICODE \*, Py\_ssize\_t]** Like u#, but the Python object may also be None, in which case the Py\_UNICODE pointer is set to NULL.

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsWideCharString().

**U (str) [PyObject \*]** Requires that the Python object is a Unicode object, without attempting any conversion. Raises TypeError if the object is not a Unicode object. The C variable may also be declared as PyObject\*.

**w\* (read-write bytes-like object) [Py\_buffer]** This format accepts any object which implements the read-write buffer interface. It fills a Py\_buffer structure provided by the caller. The buffer may contain embedded null bytes. The caller have to call PyBuffer\_Release() when it is done with the buffer.

**es (str) [const char \*encoding, char \*\*buffer]** This variant on s is used for encoding Unicode into a character buffer. It only works for encoded data without embedded NUL bytes.

This format requires two arguments. The first is only used as input, and must be a **const** char\* which points to the name of an encoding as a NUL-terminated string, or NULL, in which case 'utf-8' encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char\*\*; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text will be encoded in the encoding specified by the first argument.

PyArg\_ParseTuple() will allocate a buffer of the needed size, copy the encoded data into this buffer and adjust \*buffer to reference the newly allocated storage. The caller is responsible for calling PyMem\_Free() to free the allocated buffer after use.

**et (str, bytes or bytearray) [const char \*encoding, char \*\*buffer]** Same as es except that byte string objects are passed through without recoding them. Instead, the implementation assumes that the byte string object uses the encoding passed in as parameter.

**es# (str) [const char \*encoding, char \*\*buffer, Py\_ssize\_t \*buffer\_length]** This variant on s# is used for encoding Unicode into a character buffer. Unlike the es format, this variant allows input data which contains NUL characters.

It requires three arguments. The first is only used as input, and must be a **const** char\* which points to the name of an encoding as a NUL-terminated string, or NULL, in which case 'utf-8' encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char\*\*; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text

will be encoded in the encoding specified by the first argument. The third argument must be a pointer to an integer; the referenced integer will be set to the number of bytes in the output buffer.

There are two modes of operation:

If \*buffer points a NULL pointer, the function will allocate a buffer of the needed size, copy the encoded data into this buffer and set \*buffer to reference the newly allocated storage. The caller is responsible for calling PyMem\_Free() to free the allocated buffer after usage.

If \*buffer points to a non-NULL pointer (an already allocated buffer), PyArg\_ParseTuple() will use this location as the buffer and interpret the initial value of \*buffer\_length as the buffer size. It will then copy the encoded data into the buffer and NUL-terminate it. If the buffer is not large enough, a ValueError will be set.

In both cases, \*buffer\_length is set to the length of the encoded data without the trailing NUL byte.

**et# (str, bytes or bytearray) [const char \*encoding, char \*\*buffer, Py\_ssize\_t \*buffer\_length]** Same as es# except that byte string objects are passed through without recoding them. Instead, the implementation assumes that the byte string object uses the encoding passed in as parameter.

## Numbers

b (int) [unsigned char] Convert a nonnegative Python integer to an unsigned tiny int, stored in a C unsigned char.

B (int) [unsigned char] Convert a Python integer to a tiny int without overflow checking, stored in a C unsigned char.

h (int) [short int] Convert a Python integer to a C short int.

H (int) [unsigned short int] Convert a Python integer to a C unsigned short int, without overflow checking.

i (int) [int] Convert a Python integer to a plain C int.

I (int) [unsigned int] Convert a Python integer to a C unsigned int, without overflow checking.

l (int) [long int] Convert a Python integer to a C long int.

**k (int) [unsigned long]** Convert a Python integer to a C unsigned long without overflow checking.

L (int) [long long] Convert a Python integer to a C long long.

K (int) [unsigned long long] Convert a Python integer to a C unsigned long long without overflow checking.

n (int) [Py\_ssize\_t] Convert a Python integer to a C Py\_ssize\_t.

c (bytes or bytearray of length 1) [char] Convert a Python byte, represented as a bytes or bytearray object of length 1, to a C char.

Changed in version 3.3: Allow bytearray objects.

**C (str of length 1) [int]** Convert a Python character, represented as a str object of length 1, to a C int.

**f (float) [float]** Convert a Python floating point number to a C float.

**d (float) [double]** Convert a Python floating point number to a C double.

**D (complex) [Py\_complex]** Convert a Python complex number to a C Py\_complex structure.

## Other objects

**O (object) [PyObject \*]** Store a Python object (without any conversion) in a C object pointer. The C program thus receives the actual object that was passed. A new strong reference to the object is not created (i.e. its reference count is not increased). The pointer stored is not NULL.

**O! (object) [typeobject, PyObject \*]** Store a Python object in a C object pointer. This is similar to O, but takes two C arguments: the first is the address of a Python type object, the second is the address of the C variable (of type PyObject\*) into which the object pointer is stored. If the Python object does not have the required type, TypeError is raised.

**O& (object) [converter, anything]** Convert a Python object to a C variable through a converter function. This takes two arguments: the first is a function, the second is the address of a C variable (of arbitrary type), converted to void\*. The converter function in turn is called as follows:

```txt
status = converter(object, address);
```

where object is the Python object to be converted and address is the void\* argument that was passed to the PyArg\_Parse\* function. The returned status should be 1 for a successful conversion and 0 if the conversion has failed. When the conversion fails, the converter function should raise an exception and leave the content of address unmodified.

If the converter returns Py\_CLEANUP\_SUPPORTED, it may get called a second time if the argument parsing eventually fails, giving the converter a chance to release any memory that it had already allocated. In this second call, the object parameter will be NULL; address will have the same value as in the original call.

Changed in version 3.1: Py\_CLEANUP\_SUPPORTED was added.

**p (bool) [int]** Tests the value passed in for truth (a boolean predicate) and converts the result to its equivalent C true/false integer value. Sets the int to 1 if the expression was true and 0 if it was false. This accepts any valid Python value. See truth for more information about how Python tests values for truth.

New in version 3.3.

**(items) (tuple) [matching-items]** The object must be a Python sequence whose length is the number of format units in items. The C arguments must correspond to the individual format units in items. Format units for sequences may be nested.

It is possible to pass “long” integers (integers whose value exceeds the platform’s LONG\_MAX) however no proper range checking is done — the most significant bits are silently truncated when the receiving field is too small to receive the value (actually, the semantics are inherited from downcasts in C — your mileage may vary).

A few other characters have a meaning in a format string. These may not occur inside nested parentheses. They are:

| Indicates that the remaining arguments in the Python argument list are optional. The C variables corresponding to optional arguments should be initialized to their default value — when an optional argument is not specified, PyArg\_ParseTuple() does not touch the contents of the corresponding C variable(s).

\$ PyArg\_ParseTupleAndKeywords() only: Indicates that the remaining arguments in the Python argument list are keyword-only. Currently, all keyword-only arguments must also be optional arguments, so | must always be specified before \$ in the format string.

New in version 3.3.

: The list of format units ends here; the string after the colon is used as the function name in error messages (the “associated value” of the exception that PyArg\_ParseTuple() raises).

; The list of format units ends here; the string after the semicolon is used as the error message instead of the default error message. : and ; mutually exclude each other.

Note that any Python object references which are provided to the caller are borrowed references; do not release them (i.e. do not decrement their reference count)!

Additional arguments passed to these functions must be addresses of variables whose type is determined by the format string; these are used to store values from the input tuple. There are a few cases, as described in the list of format units

above, where these parameters are used as input values; they should match what is specified for the corresponding format unit in that case.

For the conversion to succeed, the arg object must match the format and the format must be exhausted. On success, the PyArg\_Parse\* functions return true, otherwise they return false and raise an appropriate exception. When the PyArg\_Parse\* functions fail due to conversion failure in one of the format units, the variables at the addresses corresponding to that and the following format units are left untouched.

## API Functions

int **PyArg\_ParseTuple**(PyObject \*args, **const** char \*format, ...) Part of the Stable ABI. Parse the parameters of a function that takes only positional parameters into local variables. Returns true on success; on failure, it returns false and raises the appropriate exception.

int **PyArg\_VaParse**(PyObject \*args, **const** char \*format, va\_list vargs) Part of the Stable ABI. Identical to PyArg\_ParseTuple(), except that it accepts a va\_list rather than a variable number of arguments.

int **PyArg\_ParseTupleAndKeywords**(PyObject \*args, PyObject \*kw, **const** char \*format, char \*key-

Part of the Stable ABI. Parse the parameters of a function that takes both positional and keyword parameters into local variables. The keywords argument is a NULL-terminated array of keyword parameter names. Empty names denote positional-only parameters. Returns true on success; on failure, it returns false and raises the appropriate exception.

Changed in version 3.6: Added support for positional-only parameters.

int **PyArg\_VaParseTupleAndKeywords**(PyObject \*args, PyObject \*kw, **const** char \*format, char \*keywords[], va\_list vargs)

Part of the Stable ABI. Identical to PyArg\_ParseTupleAndKeywords(), except that it accepts a va\_list rather than a variable number of arguments.

int **PyArg\_ValidateKeywordArguments**(PyObject\*) Part of the Stable ABI. Ensure that the keys in the keywords argument dictionary are strings. This is only needed if PyArg\_ParseTupleAndKeywords() is not used, since the latter already does this check.

New in version 3.2.

int **PyArg\_Parse**(PyObject \*args, **const** char \*format, ...)

Part of the Stable ABI. Function used to deconstruct the argument lists of “old-style” functions — these are functions which use the METH\_OLDARGS parameter parsing method, which has been removed in Python 3. This is not recommended for use in parameter parsing in new code, and most code in the standard interpreter has been modified to no longer use this for that purpose. It does remain a convenient way to decompose other tuples, however, and may continue to be used for that purpose.

npac \_ssize\_t min, Py\_ssize\_ Part of the Stable ABI. A simpler form of parameter retrieval which does not use a format string to specify the types of the arguments. Functions which use this method to retrieve their parameters should be declared as METH\_VARARGS in function or method tables. The tuple containing the actual parameters should be passed as args; it must actually be a tuple. The length of the tuple must be at least min and no more than max; min and max may be equal. Additional arguments must be passed to the function, each of which should be a pointer to a PyObject\* variable; these will be filled in with the values from args; they will contain borrowed references. The variables which correspond to optional parameters not given by args will not be filled in; these should be initialized by the caller. This function returns true on success and false if args is not a tuple or contains the wrong number of elements; an exception will be set if there was a failure.

This is an example of the use of this function, taken from the sources for the \_weakref helper module for weak references:

```txt
static PyObject *
weakref_ref(PyObject *self, PyObject *args)
{
```

(continues on next page)

(continued from previous page)

```c
PyObject *object;
    PyObject *callback = NULL;
    PyObject *result = NULL;

    if (PyArg_UnpackTuple(args, "ref", 1, 2, &object, &callback)) {
        result = PyWeakref_NewRef(object, callback);
    }
    return result;
}
```

The call to PyArg\_UnpackTuple() in this example is entirely equivalent to this call to PyArg\_ParseTuple():

```cpp
PyArg_ParseTuple(args, "O|O:ref", &object, &callback)
```

## 6.6.2 Building values

PyObject \***Py\_BuildValue**(**const** char \*format, ...)

Return value: New reference. Part of the Stable ABI. Create a new value based on a format string similar to those accepted by the PyArg\_Parse\* family of functions and a sequence of values. Returns the value or NULL in the case of an error; an exception will be raised if NULL is returned.

Py\_BuildValue() does not always build a tuple. It builds a tuple only if its format string contains two or more format units. If the format string is empty, it returns None; if it contains exactly one format unit, it returns whatever object is described by that format unit. To force it to return a tuple of size 0 or one, parenthesize the format string.

When memory buffers are passed as parameters to supply data to build objects, as for the s and s# formats, the required data is copied. Buffers provided by the caller are never referenced by the objects created by Py\_BuildValue(). In other words, if your code invokes malloc() and passes the allocated memory to Py\_BuildValue(), your code is responsible for calling free() for that memory once Py\_BuildValue() returns.

In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that the format unit will return; and the entry in [square] brackets is the type of the C value(s) to be passed.

The characters space, tab, colon and comma are ignored in format strings (but not within format units such as s#). This can be used to make long format strings a tad more readable.

**s (str or None) [const char \*]** Convert a null-terminated C string to a Python str object using 'utf-8' encoding. If the C string pointer is NULL, None is used.

**s# (str or None) [const char \*, Py\_ssize\_t]** Convert a C string and its length to a Python str object using 'utf-8' encoding. If the C string pointer is NULL, the length is ignored and None is returned.

**y (bytes) [const char \*]** This converts a C string to a Python bytes object. If the C string pointer is NULL, None is returned.

**y# (bytes) [const char \*, Py\_ssize\_t]** This converts a C string and its lengths to a Python object. If the C string pointer is NULL, None is returned.

**z (str or None) [const char \*]** Same as s.

**z# (str or None) [const char \*, Py\_ssize\_t]** Same as s#.

**u (str) [const wchar\_t \*]** Convert a null-terminated wchar\_t buffer of Unicode (UTF-16 or UCS-4) data to a Python Unicode object. If the Unicode buffer pointer is NULL, None is returned.

**u# (str) [const wchar\_t \*, Py\_ssize\_t]** Convert a Unicode (UTF-16 or UCS-4) data buffer and its length to a Python Unicode object. If the Unicode buffer pointer is NULL, the length is ignored and None is returned.

**U (str or None) [const char \*]** Same as s.

**U# (str or None) [const char \*, Py\_ssize\_t]** Same as s#.

**i (int) [int]** Convert a plain C int to a Python integer object.

**b (int) [char]** Convert a plain C char to a Python integer object.

**h (int) [short int]** Convert a plain C short int to a Python integer object.

**l (int) [long int]** Convert a C long int to a Python integer object.

**B (int) [unsigned char]** Convert a C unsigned char to a Python integer object.

**H (int) [unsigned short int]** Convert a C unsigned short int to a Python integer object.

**I (int) [unsigned int]** Convert a C unsigned int to a Python integer object.

**k (int) [unsigned long]** Convert a C unsigned long to a Python integer object.

**L (int) [long long]** Convert a C long long to a Python integer object.

**K (int) [unsigned long long]** Convert a C unsigned long long to a Python integer object.

**n (int) [Py\_ssize\_t]** Convert a C Py\_ssize\_t to a Python integer.

**c (bytes of length 1) [char]** Convert a C int representing a byte to a Python bytes object of length 1.

**C (str of length 1) [int]** Convert a C int representing a character to Python str object of length 1.

**d (float) [double]** Convert a C double to a Python floating point number.

**f (float) [float]** Convert a C float to a Python floating point number.

**D (complex) [Py\_complex \*]** Convert a C Py\_complex structure to a Python complex number.

**O (object) [PyObject \*]** Pass a Python object untouched but create a new strong reference to it (i.e. its reference count is incremented by one). If the object passed in is a NULL pointer, it is assumed that this was caused because the call producing the argument found an error and set an exception. Therefore, Py\_BuildValue() will return NULL but won’t raise an exception. If no exception has been raised yet, SystemError is set.

**S (object) [PyObject \*]** Same as O.

**N (object) [PyObject \*]** Same as O, except it doesn’t create a new strong reference. Useful when the object is created by a call to an object constructor in the argument list.

**O& (object) [converter, anything]** Convert anything to a Python object through a converter function. The function is called with anything (which should be compatible with void\*) as its argument and should return a “new” Python object, or NULL if an error occurred.

**(items) (tuple) [matching-items]** Convert a sequence of C values to a Python tuple with the same number of items.

**[items] (list) [matching-items]** Convert a sequence of C values to a Python list with the same number of items.

**{items} (dict) [matching-items]** Convert a sequence of C values to a Python dictionary. Each pair of consecutive C values adds one item to the dictionary, serving as key and value, respectively.

If there is an error in the format string, the SystemError exception is set and NULL returned.

PyObject \***Py\_VaBuildValue**(**const** char \*format, va\_list vargs) Return value: New reference. Part of the Stable ABI. Identical to Py\_BuildValue(), except that it accepts a va\_list rather than a variable number of arguments.

## 6.7 String conversion and formatting

Functions for number conversion and formatted string output.

int **PyOS\_snprintf**(char \*str, size\_t size, **const** char \*format, ...)

Part of the Stable ABI. Output not more than size bytes to str according to the format string format and the extra arguments. See the Unix man page snprintf(3).

int **PyOS\_vsnprintf**(char \*str, size\_t size, **const** char \*format, va\_list va)

Part of the Stable ABI. Output not more than size bytes to str according to the format string format and the variable argument list va. Unix man page vsnprintf(3).

PyOS\_snprintf() and PyOS\_vsnprintf() wrap the Standard C library functions snprintf() and vsnprintf(). Their purpose is to guarantee consistent behavior in corner cases, which the Standard C functions do not.

The wrappers ensure that str[size-1] is always '\0' upon return. They never write more than size bytes (including the trailing '\0') into str. Both functions require that str != NULL, size > 0, format != NULL and size < INT\_MAX. Note that this means there is no equivalent to the C99 n = snprintf(NULL, 0, ...) which would determine the necessary buffer size.

The return value (rv) for these functions should be interpreted as follows:

• When 0 <= rv < size, the output conversion was successful and rv characters were written to str (excluding the trailing '\0' byte at str[rv]).

• When rv >= size, the output conversion was truncated and a buffer with rv + 1 bytes would have been needed to succeed. str[size-1] is '\0' in this case.

• When rv < 0, “something bad happened.” str[size-1] is '\0' in this case too, but the rest of str is undefined. The exact cause of the error depends on the underlying platform.

The following functions provide locale-independent string to number conversions.

double **PyOS\_string\_to\_double**(**const** char \*s, char \*\*endptr, PyObject \*overflow\_exception)

Part of the Stable ABI. Convert a string s to a double, raising a Python exception on failure. The set of accepted strings corresponds to the set of strings accepted by Python’s float() constructor, except that s must not have leading or trailing whitespace. The conversion is independent of the current locale.

If endptr is NULL, convert the whole string. Raise ValueError and return -1.0 if the string is not a valid representation of a floating-point number.

If endptr is not NULL, convert as much of the string as possible and set \*endptr to point to the first unconverted character. If no initial segment of the string is the valid representation of a floating-point number, set \*endptr to point to the beginning of the string, raise ValueError, and return -1.0.

If s represents a value that is too large to store in a float (for example, "1e500" is such a string on many platforms) then if overflow\_exception is NULL return Py\_HUGE\_VAL (with an appropriate sign) and don’t set any exception. Otherwise, overflow\_exception must point to a Python exception object; raise that exception and return -1.0. In both cases, set \*endptr to point to the first character after the converted value.

If any other error occurs during the conversion (for example an out-of-memory error), set the appropriate Python exception and return -1.0.

New in version 3.1.

char \***PyOS\_double\_to\_string**(double val, char format\_code, int precision, int flags, int \*ptype) Part of the Stable ABI. Convert a double val to a string using supplied format\_code, precision, and flags.

format\_code must be one of 'e', 'E', 'f', 'F', 'g', 'G' or 'r' . For 'r', the supplied precision must be 0 and is ignored. The 'r' format code specifies the standard repr() format.

flags can be zero or more of the values Py\_DTSF\_SIGN, Py\_DTSF\_ADD\_DOT\_0, or Py\_DTSF\_ALT, or-ed together:

• Py\_DTSF\_SIGN means to always precede the returned string with a sign character, even if val is non-negative.

• Py\_DTSF\_ADD\_DOT\_0 means to ensure that the returned string will not look like an integer.

• Py\_DTSF\_ALT means to apply “alternate” formatting rules. See the documentation for the PyOS\_snprintf() '#' specifier for details.

If ptype is non-NULL, then the value it points to will be set to one of Py\_DTST\_FINITE, Py\_DTST\_INFINITE, or Py\_DTST\_NAN, signifying that val is a finite number, an infinite number, or not a number, respectively.

The return value is a pointer to buffer with the converted string or NULL if the conversion failed. The caller is responsible for freeing the returned string by calling PyMem\_Free().

New in version 3.1.

## int PyOS\_stricmp(const char \*s1, const char \*s2)

Case insensitive comparison of strings. The function works almost identically to strcmp() except that it ignores the case.

## int PyOS\_strnicmp(const char \*s1, const char \*s2, Py\_ssize\_t size)

Case insensitive comparison of strings. The function works almost identically to strncmp() except that it ignores the case.

## 6.8 Reflection

## PyObject \*PyEval\_GetBuiltins(void)

Return value: Borrowed reference. Part of the Stable ABI. Return a dictionary of the builtins in the current execution frame, or the interpreter of the thread state if no frame is currently executing.

## PyObject \*PyEval\_GetLocals(void)

Return value: Borrowed reference. Part of the Stable ABI. Return a dictionary of the local variables in the current execution frame, or NULL if no frame is currently executing.

## PyObject \*PyEval\_GetGlobals(void)

Return value: Borrowed reference. Part of the Stable ABI. Return a dictionary of the global variables in the current execution frame, or NULL if no frame is currently executing.

## PyFrameObject \*PyEval\_GetFrame(void)

Return value: Borrowed reference. Part of the Stable ABI. Return the current thread state’s frame, which is NULL if no frame is currently executing.

See also PyThreadState\_GetFrame().

## PyFrameObject \*PyFrame\_GetBack(PyFrameObject \*frame)

Get the frame next outer frame.

Return a strong reference, or NULL if frame has no outer frame.

frame must not be NULL.

New in version 3.9.

## PyCodeObject \*PyFrame\_GetCode(PyFrameObject \*frame)

Part of the Stable ABI since version 3.10. Get the frame code.

Return a strong reference.

frame must not be NULL. The result (frame code) cannot be NULL.

New in version 3.9.

## int PyFrame\_GetLineNumber(PyFrameObject \*frame)

Part of the Stable ABI since version 3.10. Return the line number that frame is currently executing.

frame must not be NULL.

**const** char \***PyEval\_GetFuncName**(PyObject \*func)

Part of the Stable ABI. Return the name of func if it is a function, class or instance object, else the name of funcs type.

**const** char \***PyEval\_GetFuncDesc**(PyObject \*func)

Part of the Stable ABI. Return a description string, depending on the type of func. Return values include “()” for functions and methods, ” constructor”, ” instance”, and ” object”. Concatenated with the result of PyEval\_GetFuncName(), the result will be a description of func.

## 6.9 Codec registry and support functions

int **PyCodec\_Register**(PyObject \*search\_function)

Part of the Stable ABI. Register a new codec search function.

As side effect, this tries to load the encodings package, if not yet done, to make sure that it is always first in the list of search functions.

int **PyCodec\_Unregister**(PyObject \*search\_function)

Part of the Stable ABI since version 3.10. Unregister a codec search function and clear the registry’s cache. If the search function is not registered, do nothing. Return 0 on success. Raise an exception and return -1 on error.

New in version 3.10.

int **PyCodec\_KnownEncoding**(**const** char \*encoding)

Part of the Stable ABI. Return 1 or 0 depending on whether there is a registered codec for the given encoding. This function always succeeds.

PyObject \***PyCodec\_Encode**(PyObject \*object, **const** char \*encoding, **const** char \*errors) Return value: New reference. Part of the Stable ABI. Generic codec based encoding API.

object is passed through the encoder function found for the given encoding using the error handling method defined by errors. errors may be NULL to use the default method defined for the codec. Raises a LookupError if no encoder can be found.

PyObject \***PyCodec\_Decode**(PyObject \*object, **const** char \*encoding, **const** char \*errors) Return value: New reference. Part of the Stable ABI. Generic codec based decoding API.

object is passed through the decoder function found for the given encoding using the error handling method defined by errors. errors may be NULL to use the default method defined for the codec. Raises a LookupError if no encoder can be found.

## 6.9.1 Codec lookup API

In the following functions, the encoding string is looked up converted to all lower-case characters, which makes encodings looked up through this mechanism effectively case-insensitive. If no codec is found, a KeyError is set and NULL returned.

PyObject \***PyCodec\_Encoder**(**const** char \*encoding)

Return value: New reference. Part of the Stable ABI. Get an encoder function for the given encoding.

PyObject \***PyCodec\_Decoder**(**const** char \*encoding)

Return value: New reference. Part of the Stable ABI. Get a decoder function for the given encoding.

PyObject \***PyCodec\_IncrementalEncoder**(**const** char \*encoding, **const** char \*errors)

Return value: New reference. Part of the Stable ABI. Get an IncrementalEncoder object for the given encoding.

PyObject \***PyCodec\_IncrementalDecoder**(**const** char \*encoding, **const** char \*errors)

Return value: New reference. Part of the Stable ABI. Get an IncrementalDecoder object for the given encoding.

PyObject \***PyCodec\_StreamReader**(**const** char \*encoding, PyObject \*stream, **const** char \*errors) Return value: New reference. Part of the Stable ABI. Get a StreamReader factory function for the given encoding.

PyObject \***PyCodec\_StreamWriter**(**const** char \*encoding, PyObject \*stream, **const** char \*errors) Return value: New reference. Part of the Stable ABI. Get a StreamWriter factory function for the given encoding.

## 6.9.2 Registry API for Unicode encoding error handlers

int **PyCodec\_RegisterError**(**const** char \*name, PyObject \*error)

Part of the Stable ABI. Register the error handling callback function error under the given name. This callback function will be called by a codec when it encounters unencodable characters/undecodable bytes and name is specified as the error parameter in the call to the encode/decode function.

The callback gets a single argument, an instance of UnicodeEncodeError, UnicodeDecodeError or UnicodeTranslateError that holds information about the problematic sequence of characters or bytes and their offset in the original string (see Unicode Exception Objects for functions to extract this information). The callback must either raise the given exception, or return a two-item tuple containing the replacement for the problematic sequence, and an integer giving the offset in the original string at which encoding/decoding should be resumed.

Return 0 on success, -1 on error.

PyObject \***PyCodec\_LookupError**(**const** char \*name)

Return value: New reference. Part of the Stable ABI. Lookup the error handling callback function registered under name. As a special case NULL can be passed, in which case the error handling callback for “strict” will be returned.

PyObject \***PyCodec\_StrictErrors**(PyObject \*exc) Return value: Always NULL. Part of the Stable ABI. Raise exc as an exception.

PyObject \***PyCodec\_IgnoreErrors**(PyObject \*exc)

Return value: New reference. Part of the Stable ABI. Ignore the unicode error, skipping the faulty input.

PyObject \***PyCodec\_ReplaceErrors**(PyObject \*exc)

Return value: New reference. Part of the Stable ABI. Replace the unicode encode error with ? or U+FFFD.

PyObject \***PyCodec\_XMLCharRefReplaceErrors**(PyObject \*exc) Return value: New reference. Part of the Stable ABI. Replace the unicode encode error with XML character references.

PyObject \***PyCodec\_BackslashReplaceErrors**(PyObject \*exc) Return value: New reference. Part of the Stable ABI. Replace the unicode encode error with backslash escapes (\x, \u and \U).

PyObject \***PyCodec\_NameReplaceErrors**(PyObject \*exc) Return value: New reference. Part of the Stable ABI since version 3.7. Replace the unicode encode error with \N{...} escapes. New in version 3.5.

# ABSTRACT OBJECTS LAYER

The functions in this chapter interact with Python objects regardless of their type, or with wide classes of object types (e.g. all numerical types, or all sequence types). When used on object types for which they do not apply, they will raise a Python exception.

It is not possible to use these functions on objects that are not properly initialized, such as a list object that has been created by PyList\_New(), but whose items have not been set to some non-NULL value yet.

## 7.1 Object Protocol

## PyObject \*Py\_NotImplemented

The NotImplemented singleton, used to signal that an operation is not implemented for the given type combination.

## Py\_RETURN\_NOTIMPLEMENTED

Properly handle returning Py\_NotImplemented from within a C function (that is, create a new strong reference to NotImplemented and return it).

## int PyObject\_Print(PyObject \*o, FILE \*fp, int flags)

Print an object o, on file fp. Returns -1 on error. The flags argument is used to enable certain printing options. The only option currently supported is Py\_PRINT\_RAW; if given, the str() of the object is written instead of the repr().

## int PyObject\_HasAttr(PyObject \*o, PyObject \*attr\_name)

Part of the Stable ABI. Returns 1 if o has the attribute attr\_name, and 0 otherwise. This is equivalent to the Python expression hasattr(o, attr\_name). This function always succeeds.

Note that exceptions which occur while calling \_\_getattr\_\_() and \_\_getattribute\_\_() methods will get suppressed. To get error reporting use PyObject\_GetAttr() instead.

## int PyObject\_HasAttrString(PyObject \*o, const char \*attr\_name)

Part of the Stable ABI. Returns 1 if o has the attribute attr\_name, and 0 otherwise. This is equivalent to the Python expression hasattr(o, attr\_name). This function always succeeds.

Note that exceptions which occur while calling \_\_getattr\_\_() and \_\_getattribute\_\_() methods and creating a temporary string object will get suppressed. To get error reporting use PyObject\_GetAttrString() instead.

## PyObject \*PyObject\_GetAttr(PyObject \*o, PyObject \*attr\_name)

Return value: New reference. Part of the Stable ABI. Retrieve an attribute named attr\_name from object o. Returns the attribute value on success, or NULL on failure. This is the equivalent of the Python expression o.attr\_name.

PyObject \***PyObject\_GetAttrString**(PyObject \*o, **const** char \*attr\_name) Return value: New reference. Part of the Stable ABI. Retrieve an attribute named attr\_name from object o. Returns the attribute value on success, or NULL on failure. This is the equivalent of the Python expression o.attr\_name.

PyObject \***PyObject\_GenericGetAttr**(PyObject \*o, PyObject \*name) Return value: New reference. Part of the Stable ABI. Generic attribute getter function that is meant to be put into a type object’s tp\_getattro slot. It looks for a descriptor in the dictionary of classes in the object’s MRO as well as an attribute in the object’s \_\_dict\_\_ (if present). As outlined in descriptors, data descriptors take preference over instance attributes, while non-data descriptors don’t. Otherwise, an AttributeError is raised.

int **PyObject\_SetAttr**(PyObject \*o, PyObject \*attr\_name, PyObject \*v) Part of the Stable ABI. Set the value of the attribute named attr\_name, for object o, to the value v. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o.attr\_name = v. If v is NULL, the attribute is deleted. This behaviour is deprecated in favour of using PyObject\_DelAttr(), but there are currently no plans to remove it.

int **PyObject\_SetAttrString**(PyObject \*o, **const** char \*attr\_name, PyObject \*v) Part of the Stable ABI. Set the value of the attribute named attr\_name, for object o, to the value v. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o.attr\_name = v. If v is NULL, the attribute is deleted, but this feature is deprecated in favour of using PyObject\_DelAttrString().

int **PyObject\_GenericSetAttr**(PyObject \*o, PyObject \*name, PyObject \*value) Part of the Stable ABI. Generic attribute setter and deleter function that is meant to be put into a type object’s tp\_setattro slot. It looks for a data descriptor in the dictionary of classes in the object’s MRO, and if found it takes preference over setting or deleting the attribute in the instance dictionary. Otherwise, the attribute is set or deleted in the object’s \_\_dict\_\_ (if present). On success, 0 is returned, otherwise an AttributeError is raised and -1 is returned.

int **PyObject\_DelAttr**(PyObject \*o, PyObject \*attr\_name) Delete attribute named attr\_name, for object o. Returns -1 on failure. This is the equivalent of the Python statement del o.attr\_name.

int **PyObject\_DelAttrString**(PyObject \*o, **const** char \*attr\_name) Delete attribute named attr\_name, for object o. Returns -1 on failure. This is the equivalent of the Python statement del o.attr\_name.

PyObject \***PyObject\_GenericGetDict**(PyObject \*o, void \*context) Return value: New reference. Part of the Stable ABI since version 3.10. A generic implementation for the getter of a \_\_dict\_\_ descriptor. It creates the dictionary if necessary. New in version 3.3.

int **PyObject\_GenericSetDict**(PyObject \*o, PyObject \*value, void \*context) Part of the Stable ABI since version 3.7. A generic implementation for the setter of a \_\_dict\_\_ descriptor. This implementation does not allow the dictionary to be deleted.

PyObject \***PyObject\_RichCompare**(PyObject \*o1, PyObject \*o2, int opid) Return value: New reference. Part of the Stable ABI. Compare the values of o1 and o2 using the operation specified by opid, which must be one of Py\_LT, Py\_LE, Py\_EQ, Py\_NE, Py\_GT, or Py\_GE, corresponding to <, <=, ==, !=, >, or >= respectively. This is the equivalent of the Python expression o1 op o2, where op is the operator corresponding to opid. Returns the value of the comparison on success, or NULL on failure.

int **PyObject\_RichCompareBool**(PyObject \*o1, PyObject \*o2, int opid) Part of the Stable ABI. Compare the values of o1 and o2 using the operation specified by opid, which must be one of Py\_LT, Py\_LE, Py\_EQ, Py\_NE, Py\_GT, or Py\_GE, corresponding to <, <=, ==, !=, >, or >= respectively. Returns -1 on error, 0 if the result is false, 1 otherwise. This is the equivalent of the Python expression o1 op o2, where op is the operator corresponding to opid.

**Note:** If o1 and o2 are the same object, PyObject\_RichCompareBool() will always return 1 for Py\_EQ

and 0 for Py\_NE.

PyObject \***PyObject\_Format**(PyObject \*obj, PyObject \*format\_spec) Part of the Stable ABI. Format obj using format\_spec. This is equivalent to the Python expression format(obj, format\_spec). format\_spec may be NULL. In this case the call is equivalent to format(obj). Returns the formatted string on success, NULL on failure.

## y ject \*PyObject\_Repr( y ject \*o) PyObject \*PyObject\_Repr (PyObject \*o)

Return value: New reference. Part of the Stable ABI. Compute a string representation of object o. Returns the string representation on success, NULL on failure. This is the equivalent of the Python expression repr(o). Called by the repr() built-in function.

Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception.

PyObject \***PyObject\_ASCII**(PyObject \*o) Return value: New reference. Part of the Stable ABI. As PyObject\_Repr(), compute a string representation of object o, but escape the non-ASCII characters in the string returned by PyObject\_Repr() with \x, \u or \U escapes. This generates a string similar to that returned by PyObject\_Repr() in Python 2. Called by the ascii() built-in function.

PyObject \***PyObject\_Str**(PyObject \*o) Return value: New reference. Part of the Stable ABI. Compute a string representation of object o. Returns the string representation on success, NULL on failure. This is the equivalent of the Python expression str(o). Called by the str() built-in function and, therefore, by the print() function.

Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception.

PyObject \***PyObject\_Bytes**(PyObject \*o) Return value: New reference. Part of the Stable ABI. Compute a bytes representation of object o. NULL is returned on failure and a bytes object on success. This is equivalent to the Python expression bytes(o), when o is not an integer. Unlike bytes(o), a TypeError is raised when o is an integer instead of a zero-initialized bytes object.

## int PyObject\_IsSubclass(PyObject \*derived, PyObject \*cls)

Part of the Stable ABI. Return 1 if the class derived is identical to or derived from the class cls, otherwise return 0. In case of an error, return -1.

If cls is a tuple, the check will be done against every entry in cls. The result will be 1 when at least one of the checks returns 1, otherwise it will be 0.

If cls has a \_\_subclasscheck\_\_() method, it will be called to determine the subclass status as described in [**PEP 3119**](https://www.python.org/dev/peps/pep-3119). Otherwise, derived is a subclass of cls if it is a direct or indirect subclass, i.e. contained in cls.\_\_mro\_\_.

Normally only class objects, i.e. instances of type or a derived class, are considered classes. However, objects can override this by having a \_\_bases\_\_ attribute (which must be a tuple of base classes).

int **PyObject\_IsInstance**(PyObject \*inst, PyObject \*cls)

Part of the Stable ABI. Return 1 if inst is an instance of the class cls or a subclass of cls, or 0 if not. On error, returns -1 and sets an exception.

If cls is a tuple, the check will be done against every entry in cls. The result will be 1 when at least one of the checks returns 1, otherwise it will be 0.

If cls has a \_\_instancecheck\_\_() method, it will be called to determine the subclass status as described in [**PEP 3119**](https://www.python.org/dev/peps/pep-3119). Otherwise, inst is an instance of cls if its class is a subclass of cls.

An instance inst can override what is considered its class by having a \_\_class\_\_ attribute.

An object cls can override if it is considered a class, and what its base classes are, by having a \_\_bases\_\_ attribute (which must be a tuple of base classes).

Py\_hash\_t **PyObject\_Hash**(PyObject \*o) Part of the Stable ABI. Compute and return the hash value of an object o. On failure, return -1. This is the equivalent of the Python expression hash(o). Changed in version 3.2: The return type is now Py\_hash\_t. This is a signed integer the same size as Py\_ssize\_t.

Py\_hash\_t **PyObject\_HashNotImplemented**(PyObject \*o) Part of the Stable ABI. Set a TypeError indicating that type(o) is not hashable and return -1. This function receives special treatment when stored in a tp\_hash slot, allowing a type to explicitly indicate to the interpreter that it is not hashable.

int **PyObject\_IsTrue**(PyObject \*o) Part of the Stable ABI. Returns 1 if the object o is considered to be true, and 0 otherwise. This is equivalent to the Python expression not not o. On failure, return -1.

int **PyObject\_Not**(PyObject \*o) Part of the Stable ABI. Returns 0 if the object o is considered to be true, and 1 otherwise. This is equivalent to the Python expression not o. On failure, return -1.

PyObject \***PyObject\_Type**(PyObject \*o) Return value: New reference. Part of the Stable ABI. When o is non-NULL, returns a type object corresponding to the object type of object o. On failure, raises SystemError and returns NULL. This is equivalent to the Python expression type(o). This function creates a new strong reference to the return value. There’s really no reason to use this function instead of the Py\_TYPE() function, which returns a pointer of type PyTypeObject\*, except when a new strong reference is needed.

int PyObject\_TypeCheck(PyObject \*o, PyTypeObject \*type) Return non-zero if the object o is of type type or a subtype of type, and 0 otherwise. Both parameters must be non-NULL.

Py\_ssize\_t **PyObject\_Length**(PyObject \*o) Part of the Stable ABI. Return the length of object o. If the object o provides either the sequence and mapping protocols, the sequence length is returned. On error, -1 is returned. This is the equivalent to the Python expression len(o).

Py\_ssize\_t **PyObject\_LengthHint**(PyObject \*o, Py\_ssize\_t defaultvalue) Return an estimated length for the object o. First try to return its actual length, then an estimate using length\_hint\_\_(), and finally return the default value. On error return -1. This is the equivalent to the Python expression operator.length\_hint(o, defaultvalue).

PyObject \***PyObject\_GetItem**(PyObject \*o, PyObject \*key) Return value: New reference. Part of the Stable ABI. Return element of o corresponding to the object key or NULL on failure. This is the equivalent of the Python expression o[key].

int **PyObject\_SetItem**(PyObject \*o, PyObject \*key, PyObject \*v) Part of the Stable ABI. Map the object key to the value v. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o[key] = v. This function does not steal a reference to v.

int **PyObject\_DelItem**(PyObject \*o, PyObject \*key) Part of the Stable ABI. Remove the mapping for the object key from the object o. Return -1 on failure. This is equivalent to the Python statement del o[key].

PyObject \***PyObject\_Dir**(PyObject \*o) Return value: New reference. Part of the Stable ABI. This is equivalent to the Python expression dir(o), returning a (possibly empty) list of strings appropriate for the object argument, or NULL if there was an error. If the argument is NULL, this is like the Python dir(), returning the names of the current locals; in this case, if no execution frame is active then NULL is returned but PyErr\_Occurred() will return false.

PyObject \***PyObject\_GetIter**(PyObject \*o) Return value: New reference. Part of the Stable ABI. This is equivalent to the Python expression iter(o).

It returns a new iterator for the object argument, or the object itself if the object is already an iterator. Raises TypeError and returns NULL if the object cannot be iterated.

PyObject \***PyObject\_GetAIter**(PyObject \*o)

Return value: New reference. Part of the Stable ABI since version 3.10. This is the equivalent to the Python expression aiter(o). Takes an AsyncIterable object and returns an AsyncIterator for it. This is typically a new iterator but if the argument is an AsyncIterator, this returns itself. Raises TypeError and returns NULL if the object cannot be iterated.

New in version 3.10.

## 7.2 Call Protocol

CPython supports two different calling protocols: tp\_call and vectorcall.

## 7.2.1 The tp\_call Protocol

Instances of classes that set tp\_call are callable. The signature of the slot is:

```c
PyObject *tp_call(PyObject *callable, PyObject *args, PyObject *kwargs);
```

A call is made using a tuple for the positional arguments and a dict for the keyword arguments, similarly to callable(\*args, \*\*kwargs) in Python code. args must be non-NULL (use an empty tuple if there are no arguments) but kwargs may be NULL if there are no keyword arguments.

This convention is not only used by tp\_call: tp\_new and tp\_init also pass arguments this way.

To call an object, use PyObject\_Call() or another call API.

## 7.2.2 The Vectorcall Protocol

New in version 3.9.

The vectorcall protocol was introduced in [**PEP 590**](https://www.python.org/dev/peps/pep-0590) as an additional protocol for making calls more efficient.

As rule of thumb, CPython will prefer the vectorcall for internal calls if the callable supports it. However, this is not a hard rule. Additionally, some third-party extensions use tp\_call directly (rather than using PyObject\_Call()). Therefore, a class supporting vectorcall must also implement tp\_call. Moreover, the callable must behave the same regardless of which protocol is used. The recommended way to achieve this is by setting tp\_call to PyVectorcall\_Call(). This bears repeating:

**Warning:** A class supporting vectorcall **must** also implement tp\_call with the same semantics.

A class should not implement vectorcall if that would be slower than tp\_call. For example, if the callee needs to convert the arguments to an args tuple and kwargs dict anyway, then there is no point in implementing vectorcall.

Classes can implement the vectorcall protocol by enabling the Py\_TPFLAGS\_HAVE\_VECTORCALL flag and setting tp\_vectorcall\_offset to the offset inside the object structure where a vectorcallfunc appears. This is a pointer to a function with the following signature:

**typedef** PyObject \*(\***vectorcallfunc**)(PyObject \*callable, PyObject \***const** \*args, size\_t nargsf,

• callable is the object being called.

• **args is a C array consisting of the positional arguments followed by the** values of the keyword arguments. This can be NULL if there are no arguments.

• **nargsf is the number of positional arguments plus possibly the** PY\_VECTORCALL\_ARGUMENTS\_OFFSET flag. To get the actual number of positional arguments from nargsf, use PyVectorcall\_NARGS().

• **kwnames is a tuple containing the names of the keyword arguments;** in other words, the keys of the kwargs dict. These names must be strings (instances of str or a subclass) and they must be unique. If there are no keyword arguments, then kwnames can instead be NULL.

## PY\_VECTORCALL\_ARGUMENTS\_OFFSET

If this flag is set in a vectorcall nargsf argument, the callee is allowed to temporarily change args[-1]. In other words, args points to argument 1 (not 0) in the allocated vector. The callee must restore the value of args[-1] before returning.

For PyObject\_VectorcallMethod(), this flag means instead that args[0] may be changed.

Whenever they can do so cheaply (without additional allocation), callers are encouraged to use PY\_VECTORCALL\_ARGUMENTS\_OFFSET. Doing so will allow callables such as bound methods to make their onward calls (which include a prepended self argument) very efficiently.

To call an object that implements vectorcall, use a call API function as with any other callable. PyObject\_Vectorcall() will usually be most efficient.

**Note:** In CPython 3.8, the vectorcall API and related functions were available provisionally under names with a leading underscore: \_PyObject\_Vectorcall, \_Py\_TPFLAGS\_HAVE\_VECTORCALL, \_PyObject\_VectorcallMethod, \_PyVectorcall\_Function, \_PyObject\_CallOneArg, \_PyObject\_CallMethodNoArgs, \_PyObject\_CallMethodOneArg. Additionally, PyObject\_VectorcallDict was available as \_PyObject\_FastCallDict. The old names are still defined as aliases of the new, non-underscored names.

## Recursion Control

When using tp\_call, callees do not need to worry about recursion: CPython uses Py\_EnterRecursiveCall() and Py\_LeaveRecursiveCall() for calls made using tp\_call.

For efficiency, this is not the case for calls done using vectorcall: the callee should use Py\_EnterRecursiveCall and Py\_LeaveRecursiveCall if needed.

## Vectorcall Support API

Py\_ssize\_t **PyVectorcall\_NARGS**(size\_t nargsf) Given a vectorcall nargsf argument, return the actual number of arguments. Currently equivalent to:

```cmake
(Py_ssize_t)(nargsf & ~PY_VECTORCALL_ARGUMENTS_OFFSET)
```

However, the function PyVectorcall\_NARGS should be used to allow for future extensions.

New in version 3.8.

vectorcallfunc **PyVectorcall\_Function**(PyObject \*op)

If op does not support the vectorcall protocol (either because the type does not or because the specific instance does not), return NULL. Otherwise, return the vectorcall function pointer stored in op. This function never raises an exception.

This is mostly useful to check whether or not op supports vectorcall, which can be done by checking PyVectorcall\_Function(op) != NULL.

New in version 3.8.

PyObject \***PyVectorcall\_Call**(PyObject \*callable, PyObject \*tuple, PyObject \*dict) Call callable’s vectorcallfunc with positional and keyword arguments given in a tuple and dict, respectively.

This is a specialized function, intended to be put in the tp\_call slot or be used in an implementation of tp\_call. It does not check the Py\_TPFLAGS\_HAVE\_VECTORCALL flag and it does not fall back to tp\_call.

New in version 3.8.

## 7.2.3 Object Calling API

Various functions are available for calling a Python object. Each converts its arguments to a convention supported by the called object – either tp\_call or vectorcall. In order to do as little conversion as possible, pick one that best fits the format of data you have available.

The following table summarizes the available functions; please see individual documentation for details.

| Function | callable | args | kwargs |
| --- | --- | --- | --- |
| PyObject_Call() | PyObject * | tuple | dict/NULL |
| PyObject_CallNoArgs() | PyObject * | - | - |
| PyObject_CallOneArg() | PyObject * | 1 object | - |
| PyObject_CallObject() | PyObject * | tuple/NULL | - |
| PyObject_CallFunction() | PyObject * | format | - |
| PyObject_CallMethod() | obj + char* | format | - |
| PyObject_CallFunctionObjArgs() | PyObject * | variadic | - |
| PyObject_CallMethodObjArgs() | obj + name | variadic | - |
| PyObject_CallMethodNoArgs() | obj + name | - | - |
| PyObject_CallMethodOneArg() | obj + name | 1 object | - |
| PyObject_Vectorcall() | PyObject * | vectorcall | vectorcall |
| PyObject_VectorcallDict() | PyObject * | vectorcall | dict/NULL |
| PyObject_VectorcallMethod() | arg + name | vectorcall | vectorcall |

## PyObject \*PyObject\_Call(PyObject \*callable, PyObject \*args, PyObject \*kwargs)

Return value: New reference. Part of the Stable ABI. Call a callable Python object callable, with arguments given by the tuple args, and named arguments given by the dictionary kwargs.

args must not be NULL; use an empty tuple if no arguments are needed. If no named arguments are needed, kwargs can be NULL.

Return the result of the call on success, or raise an exception and return NULL on failure.

This is the equivalent of the Python expression: callable(\*args, \*\*kwargs).

## PyObject \*PyObject\_CallNoArgs(PyObject \*callable)

Part of the Stable ABI since version 3.10. Call a callable Python object callable without any arguments. It is the most efficient way to call a callable Python object without any argument. Return the result of the call on success, or raise an exception and return NULL on failure. New in version 3.9.

## PyObject \*PyObject\_CallOneArg(PyObject \*callable, PyObject \*arg)

Call a callable Python object callable with exactly 1 positional argument arg and no keyword arguments.

Return the result of the call on success, or raise an exception and return NULL on failure.

New in version 3.9.

PyObject \***PyObject\_CallObject**(PyObject \*callable, PyObject \*args) Return value: New reference. Part of the Stable ABI. Call a callable Python object callable, with arguments given by the tuple args. If no arguments are needed, then args can be NULL. Return the result of the call on success, or raise an exception and return NULL on failure. This is the equivalent of the Python expression: callable(\*args).

PyObject \***PyObject\_CallFunction**(PyObject \*callable, **const** char \*format, ...) Return value: New reference. Part of the Stable ABI. Call a callable Python object callable, with a variable number of C arguments. The C arguments are described using a Py\_BuildValue() style format string. The format can be NULL, indicating that no arguments are provided. Return the result of the call on success, or raise an exception and return NULL on failure. This is the equivalent of the Python expression: callable(\*args). Note that if you only pass PyObject\* args, PyObject\_CallFunctionObjArgs() is a faster alternative. Changed in version 3.4: The type of format was changed from char \*.

PyObject \***PyObject\_CallMethod**(PyObject \*obj, **const** char \*name, **const** char \*format, ...) Return value: New reference. Part of the Stable ABI. Call the method named name of object obj with a variable number of C arguments. The C arguments are described by a Py\_BuildValue() format string that should produce a tuple. The format can be NULL, indicating that no arguments are provided. Return the result of the call on success, or raise an exception and return NULL on failure. This is the equivalent of the Python expression: obj.name(arg1, arg2, ...). Note that if you only pass PyObject\* args, PyObject\_CallMethodObjArgs() is a faster alternative. Changed in version 3.4: The types of name and format were changed from char \*.

Return the result of the call on success, or raise an exception and return NULL on failure.

This is the equivalent of the Python expression: callable(arg1, arg2, ...).

PyObject \***PyObject\_CallMethodObjArgs**(PyObject \*obj, PyObject \*name, ...) Return value: New reference. Part of the Stable ABI. Call a method of the Python object obj, where the name of the method is given as a Python string object in name. It is called with a variable number of PyObject\* arguments. The arguments are provided as a variable number of parameters followed by NULL. Return the result of the call on success, or raise an exception and return NULL on failure.

PyObject \***PyObject\_CallMethodNoArgs**(PyObject \*obj, PyObject \*name) Call a method of the Python object obj without arguments, where the name of the method is given as a Python string object in name. Return the result of the call on success, or raise an exception and return NULL on failure. New in version 3.9.

PyObject \***PyObject\_CallMethodOneArg**(PyObject \*obj, PyObject \*name, PyObject \*arg) Call a method of the Python object obj with a single positional argument arg, where the name of the method is given as a Python string object in name. Return the result of the call on success, or raise an exception and return NULL on failure.

New in version 3.9.

PyObject \***PyObject\_Vectorcall**(PyObject \*callable, PyObject \***const** \*args, size\_t nargsf, PyObject \*kwnames) Call a callable Python object callable. The arguments are the same as for vectorcallfunc. If callable supports vectorcall, this directly calls the vectorcall function stored in callable. Return the result of the call on success, or raise an exception and return NULL on failure. New in version 3.9.

PyObject \***PyObject\_VectorcallDict**(PyObject \*callable, PyObject \***const** \*args, size\_t nargsf, PyObject \*kwdict)

Call callable with positional arguments passed exactly as in the vectorcall protocol, but with keyword arguments passed as a dictionary kwdict. The args array contains only the positional arguments.

Regardless of which protocol is used internally, a conversion of arguments needs to be done. Therefore, this function should only be used if the caller already has a dictionary ready to use for the keyword arguments, but not a tuple for the positional arguments.

New in version 3.9.

## PyObject \*PyObject\_VectorcallMethod(PyObject \*name, PyObject \*const \*args, size\_t nargsf,

PyObject \*kwnames)

Call a method using the vectorcall calling convention. The name of the method is given as a Python string name. The object whose method is called is args[0], and the args array starting at args[1] represents the arguments of the call. There must be at least one positional argument. nargsf is the number of positional arguments including args[0], plus PY\_VECTORCALL\_ARGUMENTS\_OFFSET if the value of args[0] may temporarily be changed. Keyword arguments can be passed just like in PyObject\_Vectorcall().

If the object has the Py\_TPFLAGS\_METHOD\_DESCRIPTOR feature, this will call the unbound method object with the full args vector as arguments.

Return the result of the call on success, or raise an exception and return NULL on failure.

New in version 3.9.

## 7.2.4 Call Support API

int **PyCallable\_Check**(PyObject \*o)

Part of the Stable ABI. Determine if the object o is callable. Return 1 if the object is callable and 0 otherwise. This function always succeeds.

## 7.3 Number Protocol

## int PyNumber\_Check(PyObject \*o)

Part of the Stable ABI. Returns 1 if the object o provides numeric protocols, and false otherwise. This function always succeeds.

Changed in version 3.8: Returns 1 if o is an index integer.

## PyObject \*PyNumber\_Add(PyObject \*o1, PyObject \*o2)

Return value: New reference. Part of the Stable ABI. Returns the result of adding o1 and o2, or NULL on failure. This is the equivalent of the Python expression o1 + o2.

## PyObject \*PyNumber\_Subtract(PyObject \*o1, PyObject \*o2)

Return value: New reference. Part of the Stable ABI. Returns the result of subtracting o2 from o1, or NULL on failure. This is the equivalent of the Python expression o1 - o2.

## PyObject \*PyNumber\_Multiply(PyObject \*o1, PyObject \*o2)

Return value: New reference. Part of the Stable ABI. Returns the result of multiplying o1 and o2, or NULL on failure. This is the equivalent of the Python expression o1 \* o2.

PyObject \***PyNumber\_MatrixMultiply**(PyObject \*o1, PyObject \*o2)

Return value: New reference. Part of the Stable ABI since version 3.7. Returns the result of matrix multiplication on o1 and o2, or NULL on failure. This is the equivalent of the Python expression o1 @ o2.

New in version 3.5.

PyObject \***PyNumber\_FloorDivide**(PyObject \*o1, PyObject \*o2)

Return value: New reference. Part of the Stable ABI. Return the floor of o1 divided by o2, or NULL on failure. This is the equivalent of the Python expression o1 // o2.

PyObject \*PyNumber\_TrueDivide(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Return a reasonable approximation for the mathematical value of o1 divided by o2, or NULL on failure. The return value is “approximate” because binary floating point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating point value when passed two integers. This is the equivalent of the Python expression o1 / o2.

PyObject \*PyNumber\_Remainder(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the remainder of dividing o1 by o2, or NULL on failure. This is the equivalent of the Python expression o1 % o2.

PyObject \*PyNumber\_Divmod(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. See the built-in function divmod(). Returns NULL on failure. This is the equivalent of the Python expression divmod(o1, o2).

PyObject \*PyNumber\_Power(PyObject \*o1, PyObject \*o2, PyObject \*o3) Return value: New reference. Part of the Stable ABI. See the built-in function pow(). Returns NULL on failure. This is the equivalent of the Python expression pow(o1, o2, o3), where o3 is optional. If o3 is to be ignored, pass Py\_None in its place (passing NULL for o3 would cause an illegal memory access).

PyObject \*PyNumber\_Negative(PyObject \*o) Return value: New reference. Part of the Stable ABI. Returns the negation of o on success, or NULL on failure. This is the equivalent of the Python expression -o.

PyObject \*PyNumber\_Positive(PyObject \*o) Return value: New reference. Part of the Stable ABI. Returns o on success, or NULL on failure. This is the equivalent of the Python expression +o.

PyObject \*PyNumber\_Absolute(PyObject \*o) Return value: New reference. Part of the Stable ABI. Returns the absolute value of o, or NULL on failure. This is the equivalent of the Python expression abs(o).

PyObject \*PyNumber\_Invert(PyObject \*o) Return value: New reference. Part of the Stable ABI. Returns the bitwise negation of o on success, or NULL on failure. This is the equivalent of the Python expression \~o.

PyObject \*PyNumber\_Lshift(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the result of left shifting o1 by o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 << o2.

PyObject \*PyNumber\_Rshift(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the result of right shifting o1 by o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 >> o2.

PyObject \*PyNumber\_And(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the “bitwise and” of o1 and o2 on success and NULL on failure. This is the equivalent of the Python expression o1 & o2.

PyObject \*PyNumber\_Xor(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the “bitwise exclusive or” of o1 by o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 ^ o2.

PyObject \*PyNumber\_Or(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the “bitwise or” of o1 and o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 | o2.

PyObject \*PyNumber\_InPlaceAdd(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the result of adding o1 and o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 += o2.

PyObject \*PyNumber\_InPlaceSubtract(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the result of subtracting o2 from o1, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 -= o2.

PyObject \*PyNumber\_InPlaceMultiply(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the result of multiplying o1 and o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 \*= o2.

PyObject \*PyNumber\_InPlaceMatrixMultiply(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI since version 3.7. Returns the result of matrix multiplication on o1 and o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 @= o2.

PyObject \*PyNumber\_InPlaceFloorDivide(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the mathematical floor of dividing o1 by o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 //= o2.

PyObject \*PyNumber\_InPlaceTrueDivide(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Return a reasonable approximation for the mathematical value of o1 divided by o2, or NULL on failure. The return value is “approximate” because binary floating point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating point value when passed two integers. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 /= o2.

PyObject \*PyNumber\_InPlaceRemainder(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the remainder of dividing o1 by o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1%= o2.

PyObject \*PyNumber\_InPlacePower(PyObject \*o1, PyObject \*o2, PyObject \*o3) Return value: New reference. Part of the Stable ABI. See the built-in function pow(). Returns NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 \*\*= o2 when o3 is Py\_None, or an in-place variant of pow(o1, o2, o3) otherwise. If o3 is to be ignored, pass Py\_None in its place (passing NULL for o3 would cause an illegal memory access).

PyObject \*PyNumber\_InPlaceLshift(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the result of left shifting o1 by o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 <<= o2.

PyObject \*PyNumber\_InPlaceRshift(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the result of right shifting o1 by o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 >>= o2.

PyObject \*PyNumber\_InPlaceAnd(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the “bitwise and” of o1 and o2 on success and NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 &= o2.

PyObject \*PyNumber\_InPlaceXor(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the “bitwise exclusive or” of o1 by o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 ^= o2.

PyObject \*PyNumber\_InPlaceOr(PyObject \*o1, PyObject \*o2) Return value: New reference. Part of the Stable ABI. Returns the “bitwise or” of o1 and o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 |= o2.

PyObject \*PyNumber\_Long(PyObject \*o) Return value: New reference. Part of the Stable ABI. Returns the o converted to an integer object on success, or NULL on failure. This is the equivalent of the Python expression int(o).

## PyObject \*PyNumber\_Float(PyObject \*o)

Return value: New reference. Part of the Stable ABI. Returns the o converted to a float object on success, or NULL on failure. This is the equivalent of the Python expression float(o).

## PyObject \*PyNumber\_Index(PyObject \*o)

Return value: New reference. Part of the Stable ABI. Returns the o converted to a Python int on success or NULL with a TypeError exception raised on failure.

Changed in version 3.10: The result always has exact type int. Previously, the result could have been an instance of a subclass of int.

## PyObject \*PyNumber\_ToBase(PyObject \*n, int base)

Return value: New reference. Part of the Stable ABI. Returns the integer n converted to base base as a string. The base argument must be one of 2, 8, 10, or 16. For base 2, 8, or 16, the returned string is prefixed with a base marker of '0b', '0o', or '0x', respectively. If n is not a Python int, it is converted with PyNumber\_Index() first.

## Py\_ssize\_t PyNumber\_AsSsize\_t(PyObject \*o, PyObject \*exc)

Part of the Stable ABI. Returns o converted to a Py\_ssize\_t value if o can be interpreted as an integer. If the call fails, an exception is raised and -1 is returned.

If o can be converted to a Python int but the attempt to convert to a Py\_ssize\_t value would raise an OverflowError, then the exc argument is the type of exception that will be raised (usually IndexError or OverflowError). If exc is NULL, then the exception is cleared and the value is clipped to PY\_SSIZE\_T\_MIN for a negative integer or PY\_SSIZE\_T\_MAX for a positive integer.

## int PyIndex\_Check(PyObject \*o)

Part of the Stable ABI since version 3.8. Returns 1 if o is an index integer (has the nb\_index slot of the tp\_as\_number structure filled in), and 0 otherwise. This function always succeeds.

## 7.4 Sequence Protocol

## int PySequence\_Check(PyObject \*o)

Part of the Stable ABI. Return 1 if the object provides the sequence protocol, and 0 otherwise. Note that it returns 1 for Python classes with a \_\_getitem\_\_() method, unless they are dict subclasses, since in general it is impossible to determine what type of keys the class supports. This function always succeeds.

## Py\_ssize\_t PySequence\_Size(PyObject \*o)

## Py\_ssize\_t PySequence\_Length(PyObject \*o)

Part of the Stable ABI. Returns the number of objects in sequence o on success, and -1 on failure. This is equivalent to the Python expression len(o).

## PyObject \*PySequence\_Concat(PyObject \*o1, PyObject \*o2)

Return value: New reference. Part of the Stable ABI. Return the concatenation of o1 and o2 on success, and NULL on failure. This is the equivalent of the Python expression o1 + o2.

## PyObject \*PySequence\_Repeat(PyObject \*o, Py\_ssize\_t count)

Return value: New reference. Part of the Stable ABI. Return the result of repeating sequence object o count times, or NULL on failure. This is the equivalent of the Python expression o \* count.

## PyObject \*PySequence\_InPlaceConcat(PyObject \*o1, PyObject \*o2)

Return value: New reference. Part of the Stable ABI. Return the concatenation of o1 and o2 on success, and NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python expression o1 += o2.

## PyObject \*PySequence\_InPlaceRepeat(PyObject \*o, Py\_ssize\_t count)

Return value: New reference. Part of the Stable ABI. Return the result of repeating sequence object o count times, or NULL on failure. The operation is done in-place when o supports it. This is the equivalent of the Python expression o \*= count.

PyObject \*PySequence\_GetItem(PyObject \*o, Py\_ssize\_t i) Return value: New reference. Part of the Stable ABI. Return the ith element of o, or NULL on failure. This is the equivalent of the Python expression o[i].

PyObject \*PySequence\_GetSlice(PyObject \*o, Py\_ssize\_t i1, Py\_ssize\_t i2) Return value: New reference. Part of the Stable ABI. Return the slice of sequence object o between i1 and i2, or NULL on failure. This is the equivalent of the Python expression o[i1:i2].

int PySequence\_SetItem(PyObject \*o, Py\_ssize\_t i, PyObject \*v) Part of the Stable ABI. Assign object v to the ith element of o. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o[i] = v. This function does not steal a reference to v.

int PySequence\_DelItem(PyObject \*o, Py\_ssize\_t i) Part of the Stable ABI. Delete the ith element of object o. Returns -1 on failure. This is the equivalent of the Python statement del o[i].

int PySequence\_SetSlice(PyObject \*o, Py\_ssize\_t i1, Py\_ssize\_t i2, PyObject \*v) Part of the Stable ABI. Assign the sequence object v to the slice in sequence object o from i1 to i2. This is the equivalent of the Python statement o[i1:i2] = v.

int PySequence\_DelSlice(PyObject \*o, Py\_ssize\_t i1, Py\_ssize\_t i2) Part of the Stable ABI. Delete the slice in sequence object o from i1 to i2. Returns -1 on failure. This is the equivalent of the Python statement del o[i1:i2].

Py\_ssize\_t PySequence\_Count(PyObject \*o, PyObject \*value) Part of the Stable ABI. Return the number of occurrences of value in o, that is, return the number of keys for which o[key] == value. On failure, return -1. This is equivalent to the Python expression o. count(value).

int PySequence\_Contains(PyObject \*o, PyObject \*value) Part of the Stable ABI. Determine if o contains value. If an item in o is equal to value, return 1, otherwise return 0. On error, return -1. This is equivalent to the Python expression value in o.

Py\_ssize\_t PySequence\_Index(PyObject \*o, PyObject \*value) Part of the Stable ABI. Return the first index i for which o[i] == value. On error, return -1. This is equivalent to the Python expression o.index(value).

PyObject \*PySequence\_List(PyObject \*o) Return value: New reference. Part of the Stable ABI. Return a list object with the same contents as the sequence or iterable o, or NULL on failure. The returned list is guaranteed to be new. This is equivalent to the Python expression list(o).

PyObject \*PySequence\_Tuple(PyObject \*o) Return value: New reference. Part of the Stable ABI. Return a tuple object with the same contents as the sequence or iterable o, or NULL on failure. If o is a tuple, a new reference will be returned, otherwise a tuple will be constructed with the appropriate contents. This is equivalent to the Python expression tuple(o).

## PyObject \*PySequence\_Fast(PyObject \*o, const char \*m)

Return value: New reference. Part of the Stable ABI. Return the sequence or iterable o as an object usable by the other PySequence\_Fast\* family of functions. If the object is not a sequence or iterable, raises TypeError with m as the message text. Returns NULL on failure.

The PySequence\_Fast\* functions are thus named because they assume o is a PyTupleObject or a PyListObject and access the data fields of o directly.

As a CPython implementation detail, if o is already a sequence or list, it will be returned.

Py\_ssize\_t **PySequence\_Fast\_GET\_SIZE**(PyObject \*o) Returns the length of o, assuming that o was returned by PySequence\_Fast() and that o is not NULL. The size can also be retrieved by calling PySequence\_Size() on o, but PySequence\_Fast\_GET\_SIZE() is faster because it can assume o is a list or tuple.

## PyObject \*PySequence\_Fast\_GET\_ITEM(PyObject \*o, Py\_ssize\_t i)

Return value: Borrowed reference. Return the ith element of o, assuming that o was returned by PySequence\_Fast(), o is not NULL, and that i is within bounds.

## PyObject \*\*PySequence\_Fast\_ITEMS(PyObject \*o)

Return the underlying array of PyObject pointers. Assumes that o was returned by PySequence\_Fast() and o is not NULL.

Note, if a list gets resized, the reallocation may relocate the items array. So, only use the underlying array pointer in contexts where the sequence cannot change.

## PyObject \*PySequence\_ITEM(PyObject \*o, Py\_ssize\_t i)

Return value: New reference. Return the ith element of o or NULL on failure. Faster form of PySequence\_GetItem() but without checking that PySequence\_Check() on o is true and without adjustment for negative indices.

## 7.5 Mapping Protocol

See also PyObject\_GetItem(), PyObject\_SetItem() and PyObject\_DelItem().

## int PyMapping\_Check(PyObject \*o)

Part of the Stable ABI. Return 1 if the object provides the mapping protocol or supports slicing, and 0 otherwise. Note that it returns 1 for Python classes with a \_\_getitem\_\_() method, since in general it is impossible to determine what type of keys the class supports. This function always succeeds.

## Py\_ssize\_t PyMapping\_Size(PyObject \*o)

## Py\_ssize\_t PyMapping\_Length(PyObject \*o)

Part of the Stable ABI. Returns the number of keys in object o on success, and -1 on failure. This is equivalent to the Python expression len(o).

PyObject \***PyMapping\_GetItemString**(PyObject \*o, **const** char \*key) Return value: New reference. Part of the Stable ABI. Return element of o corresponding to the string key or NULL on failure. This is the equivalent of the Python expression o[key]. See also PyObject\_GetItem().

## int PyMapping\_SetItemString(PyObject \*o, const char \*key, PyObject \*v)

Part of the Stable ABI. Map the string key to the value v in object o. Returns -1 on failure. This is the equivalent of the Python statement o[key] = v. See also PyObject\_SetItem(). This function does not steal a reference to v.

int **PyMapping\_DelItem**(PyObject \*o, PyObject \*key) Remove the mapping for the object key from the object o. Return -1 on failure. This is equivalent to the Python statement del o[key]. This is an alias of PyObject\_DelItem().

## int PyMapping\_DelItemString(PyObject \*o, const char \*key)

Remove the mapping for the string key from the object o. Return -1 on failure. This is equivalent to the Python statement del o[key].

## int PyMapping\_HasKey(PyObject \*o, PyObject \*key)

Part of the Stable ABI. Return 1 if the mapping object has the key key and 0 otherwise. This is equivalent to the Python expression key in o. This function always succeeds.

Note that exceptions which occur while calling the \_\_getitem\_\_() method will get suppressed. To get error reporting use PyObject\_GetItem() instead.

## int PyMapping\_HasKeyString(PyObject \*o, const char \*key)

Part of the Stable ABI. Return 1 if the mapping object has the key key and 0 otherwise. This is equivalent to the Python expression key in o. This function always succeeds.

Note that exceptions which occur while calling the \_\_getitem\_\_() method and creating a temporary string object will get suppressed. To get error reporting use PyMapping\_GetItemString() instead.

PyObject \***PyMapping\_Keys**(PyObject \*o) Return value: New reference. Part of the Stable ABI. On success, return a list of the keys in object o. On failure, return NULL.

Changed in version 3.7: Previously, the function returned a list or a tuple.

## PyObject \*PyMapping\_Values(PyObject \*o) PP

Return value: New reference. Part of the Stable ABI. On success, return a list of the values in object o. On failure, return NULL.

Changed in version 3.7: Previously, the function returned a list or a tuple.

## PyObject \*PyMapping\_Items(PyObject \*o)

Return value: New reference. Part of the Stable ABI. On success, return a list of the items in object o, where each item is a tuple containing a key-value pair. On failure, return NULL.

Changed in version 3.7: Previously, the function returned a list or a tuple.

## 7.6 Iterator Protocol

There are two functions specifically for working with iterators.

## int PyIter\_Check(PyObject \*o)

Part of the Stable ABI since version 3.8. Return non-zero if the object o can be safely passed to PyIter\_Next(), and 0 otherwise. This function always succeeds.

## int PyAIter\_Check(PyObject \*o)

Part of the Stable ABI since version 3.10. Return non-zero if the object o provides the AsyncIterator protocol, and 0 otherwise. This function always succeeds.

New in version 3.10.

## PyObject \*PyIter\_Next(PyObject \*o)

Return value: New reference. Part of the Stable ABI. Return the next value from the iterator o. The object must be an iterator according to PyIter\_Check() (it is up to the caller to check this). If there are no remaining values, returns NULL with no exception set. If an error occurs while retrieving the item, returns NULL and passes along the exception.

To write a loop which iterates over an iterator, the C code should look something like this:

```c
PyObject *iterator = PyObject_GetIter(obj);
PyObject *item;

if (iterator == NULL) {
    /* propagate error */
}

while ((item = PyIter_Next(iterator))) {
    /* do something with item */
    /* release reference when done */
    Py_DECREF(item);
}

Py_DECREF(iterator);

if (PyErr_Occurred()) {
    /* propagate error */
}
else {
    /* continue doing useful work */
}
```

## type PySendResult

The enum value used to represent different results of PyIter\_Send().

New in version 3.10.

PySendResult **PyIter\_Send**(PyObject \*iter, PyObject \*arg, PyObject \*\*presult)

Part of the Stable ABI since version 3.10. Sends the arg value into the iterator iter. Returns:

• PYGEN\_RETURN if iterator returns. Return value is returned via presult.

• PYGEN\_NEXT if iterator yields. Yielded value is returned via presult.

• PYGEN\_ERROR if iterator has raised and exception. presult is set to NULL.

New in version 3.10.

## 7.7 Buffer Protocol

Certain objects available in Python wrap access to an underlying memory array or buffer. Such objects include the built-in bytes and bytearray, and some extension types like array.array. Third-party libraries may define their own types for special purposes, such as image processing or numeric analysis.

While each of these types have their own semantics, they share the common characteristic of being backed by a possibly large memory buffer. It is then desirable, in some situations, to access that buffer directly and without intermediate copying.

Python provides such a facility at the C level in the form of the buffer protocol. This protocol has two sides:

• on the producer side, a type can export a “buffer interface” which allows objects of that type to expose information about their underlying buffer. This interface is described in the section Buffer Object Structures;

• on the consumer side, several means are available to obtain a pointer to the raw underlying data of an object (for example a method parameter).

Simple objects such as bytes and bytearray expose their underlying buffer in byte-oriented form. Other forms are possible; for example, the elements exposed by an array.array can be multi-byte values.

An example consumer of the buffer interface is the write() method of file objects: any object that can export a series of bytes through the buffer interface can be written to a file. While write() only needs read-only access to the internal contents of the object passed to it, other methods such as readinto() need write access to the contents of their argument. The buffer interface allows objects to selectively allow or reject exporting of read-write and read-only buffers.

There are two ways for a consumer of the buffer interface to acquire a buffer over a target object:

• call PyObject\_GetBuffer() with the right parameters;

• call PyArg\_ParseTuple() (or one of its siblings) with one of the y\*, w\* or s\* format codes.

In both cases, PyBuffer\_Release() must be called when the buffer isn’t needed anymore. Failure to do so could lead to various issues such as resource leaks.

## 7.7.1 Buffer structure

Buffer structures (or simply “buffers”) are useful as a way to expose the binary data from another object to the Python programmer. They can also be used as a zero-copy slicing mechanism. Using their ability to reference a block of memory, it is possible to expose any data to the Python programmer quite easily. The memory could be a large, constant array in a C extension, it could be a raw block of memory for manipulation before passing to an operating system library, or it could be used to pass around structured data in its native, in-memory format.

Contrary to most data types exposed by the Python interpreter, buffers are not PyObject pointers but rather simple C structures. This allows them to be created and copied very simply. When a generic wrapper around a buffer is needed, a memoryview object can be created.

For short instructions how to write an exporting object, see Buffer Object Structures. For obtaining a buffer, see PyObject\_GetBuffer().

## type Py\_buffer

## void \*buf

A pointer to the start of the logical structure described by the buffer fields. This can be any location within the underlying physical memory block of the exporter. For example, with negative strides the value may point to the end of the memory block.

For contiguous arrays, the value points to the beginning of the memory block.

## PyObject \*obj

A new reference to the exporting object. The reference is owned by the consumer and automatically released (i.e. reference count decremented) and set to NULL by PyBuffer\_Release(). The field is the equivalent of the return value of any standard C-API function.

As a special case, for temporary buffers that are wrapped by PyMemoryView\_FromBuffer() or PyBuffer\_FillInfo() this field is NULL. In general, exporting objects MUST NOT use this scheme.

## Py\_ssize\_t len

product(shape) \* itemsize. For contiguous arrays, this is the length of the underlying memory block. For non-contiguous arrays, it is the length that the logical structure would have if it were copied to a contiguous representation.

Accessing ((char \*)buf)[0] up to ((char \*)buf)[len-1] is only valid if the buffer has been obtained by a request that guarantees contiguity. In most cases such a request will be PyBUF\_SIMPLE or PyBUF\_WRITABLE.

## int readonly

An indicator of whether the buffer is read-only. This field is controlled by the PyBUF\_WRITABLE flag.

## Py\_ssize\_t itemsize

Item size in bytes of a single element. Same as the value of struct.calcsize() called on non-NULL format values.

Important exception: If a consumer requests a buffer without the PyBUF\_FORMAT flag, format will be set to NULL, but itemsize still has the value for the original format.

If shape is present, the equality product(shape) \* itemsize == len still holds and the consumer can use itemsize to navigate the buffer.

If shape is NULL as a result of a PyBUF\_SIMPLE or a PyBUF\_WRITABLE request, the consumer must disregard itemsize and assume itemsize == 1.

## const char \*format

A NUL terminated string in struct module style syntax describing the contents of a single item. If this is NULL, "B" (unsigned bytes) is assumed.

This field is controlled by the PyBUF\_FORMAT flag.

## int ndim

The number of dimensions the memory represents as an n-dimensional array. If it is 0, buf points to a single item representing a scalar. In this case, shape, strides and suboffsets MUST be NULL.

The macro PyBUF\_MAX\_NDIM limits the maximum number of dimensions to 64. Exporters MUST respect this limit, consumers of multi-dimensional buffers SHOULD be able to handle up to PyBUF\_MAX\_NDIM dimensions.

## Py\_ssize\_t \*shape

An array of Py\_ssize\_t of length ndim indicating the shape of the memory as an n-dimensional array. Note that shape[0] \* ... \* shape[ndim-1] \* itemsize MUST be equal to len.

Shape values are restricted to shape[n] >= 0. The case shape[n] == 0 requires special attention. See complex arrays for further information.

The shape array is read-only for the consumer.

## Py\_ssize\_t \*strides

An array of Py\_ssize\_t of length ndim giving the number of bytes to skip to get to a new element in each dimension.

Stride values can be any integer. For regular arrays, strides are usually positive, but a consumer MUST be able to handle the case strides[n] <= 0. See complex arrays for further information.

The strides array is read-only for the consumer.

## Py\_ssize\_t \*suboffsets

An array of Py\_ssize\_t of length ndim. If suboffsets[n] >= 0, the values stored along the nth dimension are pointers and the suboffset value dictates how many bytes to add to each pointer after de-referencing. A suboffset value that is negative indicates that no de-referencing should occur (striding in a contiguous memory block).

If all suboffsets are negative (i.e. no de-referencing is needed), then this field must be NULL (the default value).

This type of array representation is used by the Python Imaging Library (PIL). See complex arrays for further information how to access elements of such an array.

The suboffsets array is read-only for the consumer.

## void \*internal

This is for use internally by the exporting object. For example, this might be re-cast as an integer by the exporter and used to store flags about whether or not the shape, strides, and suboffsets arrays must be freed when the buffer is released. The consumer MUST NOT alter this value.

## 7.7.2 Buffer request types

Buffers are usually obtained by sending a buffer request to an exporting object via PyObject\_GetBuffer(). Since the complexity of the logical structure of the memory can vary drastically, the consumer uses the flags argument to specify the exact buffer type it can handle.

All Py\_buffer fields are unambiguously defined by the request type.

## request-independent fields

The following fields are not influenced by flags and must always be filled in with the correct values: obj, buf, len, itemsize, ndim.

## readonly, format

## PyBUF\_WRITABLE

Controls the readonly field. If set, the exporter MUST provide a writable buffer or else report failure. Otherwise, the exporter MAY provide either a read-only or writable buffer, but the choice MUST be consistent for all consumers.

## PyBUF\_FORMAT

Controls the format field. If set, this field MUST be filled in correctly. Otherwise, this field MUST be NULL.

PyBUF\_WRITABLE can be |’d to any of the flags in the next section. Since PyBUF\_SIMPLE is defined as 0, PyBUF\_WRITABLE can be used as a stand-alone flag to request a simple writable buffer.

PyBUF\_FORMAT can be |’d to any of the flags except PyBUF\_SIMPLE. The latter already implies format B (unsigned bytes).

## shape, strides, suboffsets

The flags that control the logical structure of the memory are listed in decreasing order of complexity. Note that each flag contains all bits of the flags below it.

| Request | shape | strides | suboffsets |
| --- | --- | --- | --- |
| PyBUF_INDIRECT | yes | yes | if needed |
| PyBUF_STRIDES | yes | yes | NULL |
| PyBUF_ND | yes | NULL | NULL |
| PyBUF_SIMPLE | NULL | NULL | NULL |

## contiguity requests

C or Fortran contiguity can be explicitly requested, with and without stride information. Without stride information, the buffer must be C-contiguous.

| Request | shape | strides | suboffsets | contig |
| --- | --- | --- | --- | --- |
| PyBUF_C_CONTIGUOUS | yes | yes | NULL | C |
| PyBUF_F_CONTIGUOUS | yes | yes | NULL | F |
| PyBUF_ANY_CONTIGUOUS | yes | yes | NULL | C or F |
| PyBUF_ND | yes | NULL | NULL | C |

## compound requests

All possible requests are fully defined by some combination of the flags in the previous section. For convenience, the buffer protocol provides frequently used combinations as single flags.

In the following table U stands for undefined contiguity. The consumer would have to call PyBuffer\_IsContiguous() to determine contiguity.

| Request | shape | strides | suboffsets | contig | readonly | format |
| --- | --- | --- | --- | --- | --- | --- |
| PyBUF_FULL | yes | yes | if needed | U | 0 | yes |
| PyBUF_FULL_RO | yes | yes | if needed | U | 1 or 0 | yes |
| PyBUF_RECORDS | yes | yes | NULL | U | 0 | yes |
| PyBUF_RECORDS_RO | yes | yes | NULL | U | 1 or 0 | yes |
| PyBUF_STRIDED | yes | yes | NULL | U | 0 | NULL |
| PyBUF_STRIDED_RO | yes | yes | NULL | U | 1 or 0 | NULL |
| PyBUF_CONTIG | yes | NULL | NULL | C | 0 | NULL |
| PyBUF_CONTIG_RO | yes | NULL | NULL | C | 1 or 0 | NULL |

## 7.7.3 Complex arrays

## NumPy-style: shape and strides

The logical structure of NumPy-style arrays is defined by itemsize, ndim, shape and strides.

If ndim == 0, the memory location pointed to by buf is interpreted as a scalar of size itemsize. In that case, both shape and strides are NULL.

If strides is NULL, the array is interpreted as a standard n-dimensional C-array. Otherwise, the consumer must access an n-dimensional array as follows:

```c
ptr = (char *)buf + indices[0] * strides[0] + ... + indices[n-1] * strides[n-1];
item = *((typeof(item) *)ptr);
```

As noted above, buf can point to any location within the actual memory block. An exporter can check the validity of a buffer with this function:

```python
def verify_structure(memlen, itemsize, ndim, shape, strides, offset):
    """Verify that the parameters represent a valid array within
    the bounds of the allocated memory:
        char *mem: start of the physical memory block
        memlen: length of the physical memory block
        offset: (char *)buf - mem
    """
    if offset % itemsize:
        return False
    if offset < 0 or offset+itemsize > memlen:
        return False
    if any(v % itemsize for v in strides):
        return False

    if ndim <= 0:
        return ndim == 0 and not shape and not strides
    if 0 in shape:
        return True
```

(continues on next page)

```python
imin = sum(strides[j]*(shape[j]-1) for j in range(ndim)
        if strides[j] <= 0)
imax = sum(strides[j]*(shape[j]-1) for j in range(ndim)
        if strides[j] > 0)

return 0 <= offset+imin and offset+imax+itemsize <= memlen
```

(continued from previous page)

## PIL-style: shape, strides and suboffsets

In addition to the regular items, PIL-style arrays can contain pointers that must be followed in order to get to the next element in a dimension. For example, the regular three-dimensional C-array char v[2][2][3] can also be viewed as an array of 2 pointers to 2 two-dimensional arrays: char (\*v[2])[2][3]. In suboffsets representation, those two pointers can be embedded at the start of buf, pointing to two char x[2][3] arrays that can be located anywhere in memory.

Here is a function that returns a pointer to the element in an N-D array pointed to by an N-dimensional index when there are both non-NULL strides and suboffsets:

```c
void *get_item_pointer(int ndim, void *buf, Py_ssize_t *strides,
                      Py_ssize_t *suboffsets, Py_ssize_t *indices) {
    char *pointer = (char*)buf;
    int i;
    for (i = 0; i < ndim; i++) {
        pointer += strides[i] * indices[i];
        if (suboffsets[i] >=0 ) {
            pointer = *((char**)pointer) + suboffsets[i];
        }
    }
    return (void*)pointer;
}
```

## 7.7.4 Buffer-related functions

## int PyObject\_CheckBuffer(PyObject \*obj)

Return 1 if obj supports the buffer interface otherwise 0. When 1 is returned, it doesn’t guarantee that PyObject\_GetBuffer() will succeed. This function always succeeds.

## int PyObject\_GetBuffer(PyObject \*exporter, Py\_buffer \*view, int flags)

Send a request to exporter to fill in view as specified by flags. If the exporter cannot provide a buffer of the exact type, it MUST raise PyExc\_BufferError, set view->obj to NULL and return -1.

On success, fill in view, set view->obj to a new reference to exporter and return 0. In the case of chained buffer providers that redirect requests to a single object, view->obj MAY refer to this object instead of exporter (See Buffer Object Structures).

Successful calls to PyObject\_GetBuffer() must be paired with calls to PyBuffer\_Release(), similar to malloc() and free(). Thus, after the consumer is done with the buffer, PyBuffer\_Release() must be called exactly once.

## void PyBuffer\_Release(Py\_buffer \*view)

Release the buffer view and release the strong reference (i.e. decrement the reference count) to the view’s supporting object, view->obj. This function MUST be called when the buffer is no longer being used, otherwise reference leaks may occur.

It is an error to call this function on a buffer that was not obtained via PyObject\_GetBuffer().

## Py\_ssize\_t PyBuffer\_SizeFromFormat(const char \*format)

Return the implied itemsize from format. On error, raise an exception and return -1.

New in version 3.9.

int **PyBuffer\_IsContiguous**(Py\_buffer \*view, char order) Return 1 if the memory defined by the view is C-style (order is 'C') or Fortran-style (order is 'F') contiguous or either one (order is 'A'). Return 0 otherwise. This function always succeeds.

void \***PyBuffer\_GetPointer**(Py\_buffer \*view, Py\_ssize\_t \*indices)

Get the memory area pointed to by the indices inside the given view. indices must point to an array of view->ndim indices.

int **PyBuffer\_FromContiguous**(Py\_buffer \*view, void \*buf, Py\_ssize\_t len, char fort) Copy contiguous len bytes from buf to view. fort can be 'C' or 'F' (for C-style or Fortran-style ordering). 0 is returned on success, -1 on error.

int **PyBuffer\_ToContiguous**(void \*buf, Py\_buffer \*src, Py\_ssize\_t len, char order)

Copy len bytes from src to its contiguous representation in buf. order can be 'C' or 'F' or 'A' (for C-style or Fortran-style ordering or either one). 0 is returned on success, -1 on error.

This function fails if len != src->len.

void **PyBuffer\_FillContiguousStrides**(int ndims, Py\_ssize\_t \*shape, Py\_ssize\_t \*strides, int itemsize, char order)

Fill the strides array with byte-strides of a contiguous (C-style if order is 'C' or Fortran-style if order is 'F') array of the given shape with the given number of bytes per element.

int **PyBuffer\_FillInfo**(Py\_buffer \*view, PyObject \*exporter, void \*buf, Py\_ssize\_t len, int readonly, int flags)

Handle buffer requests for an exporter that wants to expose buf of size len with writability set according to readonly. buf is interpreted as a sequence of unsigned bytes.

The flags argument indicates the request type. This function always fills in view as specified by flags, unless buf has been designated as read-only and PyBUF\_WRITABLE is set in flags.

On success, set view->obj to a new reference to exporter and return 0. Otherwise, raise PyExc\_BufferError, set view->obj to NULL and return -1;

If this function is used as part of a getbufferproc, exporter MUST be set to the exporting object and flags must be passed unmodified. Otherwise, exporter MUST be NULL.

## 7.8 Old Buffer Protocol

## Deprecated since version 3.0.

These functions were part of the “old buffer protocol” API in Python 2. In Python 3, this protocol doesn’t exist anymore but the functions are still exposed to ease porting 2.x code. They act as a compatibility wrapper around the new buffer protocol, but they don’t give you control over the lifetime of the resources acquired when a buffer is exported.

Therefore, it is recommended that you call PyObject\_GetBuffer() (or the y\* or w\* format codes with the PyArg\_ParseTuple() family of functions) to get a buffer view over an object, and PyBuffer\_Release() when the buffer view can be released.

int **PyObject\_AsCharBuffer**(PyObject \*obj, **const** char \*\*buffer, Py\_ssize\_t \*buffer\_len)

Part of the Stable ABI. Returns a pointer to a read-only memory location usable as character-based input. The obj argument must support the single-segment character buffer interface. On success, returns 0, sets buffer to the memory location and buffer\_len to the buffer length. Returns -1 and sets a TypeError on error.

int **PyObject\_AsReadBuffer**(PyObject \*obj, **const** void \*\*buffer, Py\_ssize\_t \*buffer\_len)

Part of the Stable ABI. Returns a pointer to a read-only memory location containing arbitrary data. The obj argument must support the single-segment readable buffer interface. On success, returns 0, sets buffer to the memory location and buffer\_len to the buffer length. Returns -1 and sets a TypeError on error.

## int PyObject\_CheckReadBuffer (PyObject \*o)

Part of the Stable ABI. Returns 1 if o supports the single-segment readable buffer interface. Otherwise returns 0. This function always succeeds.

Note that this function tries to get and release a buffer, and exceptions which occur while calling corresponding functions will get suppressed. To get error reporting use PyObject\_GetBuffer() instead.

int **PyObject\_AsWriteBuffer**(PyObject \*obj, void \*\*buffer, Py\_ssize\_t \*buffer\_len) Part of the Stable ABI. Returns a pointer to a writable memory location. The obj argument must support the single-segment, character buffer interface. On success, returns 0, sets buffer to the memory location and buffer\_len to the buffer length. Returns -1 and sets a TypeError on error.

# CONCRETE OBJECTS LAYER

The functions in this chapter are specific to certain Python object types. Passing them an object of the wrong type is not a good idea; if you receive an object from a Python program and you are not sure that it has the right type, you must perform a type check first; for example, to check that an object is a dictionary, use PyDict\_Check(). The chapter is structured like the “family tree” of Python object types.

**Warning:** While the functions described in this chapter carefully check the type of the objects which are passed in, many of them do not check for NULL being passed instead of a valid object. Allowing NULL to be passed in can cause memory access violations and immediate termination of the interpreter.

## 8.1 Fundamental Objects

This section describes Python type objects and the singleton object None.

## 8.1.1 Type Objects

## type PyTypeObject

Part of the Limited API (as an opaque struct). The C structure of the objects used to describe built-in types.

## PyTypeObject PyType\_Type

Part of the Stable ABI. This is the type object for type objects; it is the same object as type in the Python layer.

## int PyType\_Check(PyObject \*o)

Return non-zero if the object o is a type object, including instances of types derived from the standard type object. Return 0 in all other cases. This function always succeeds.

## int PyType\_CheckExact(PyObject \*o)

Return non-zero if the object o is a type object, but not a subtype of the standard type object. Return 0 in all other cases. This function always succeeds.

## unsigned int PyType\_ClearCache()

Part of the Stable ABI. Clear the internal lookup cache. Return the current version tag.

## unsigned long PyType\_GetFlags(PyTypeObject \*type)

Part of the Stable ABI. Return the tp\_flags member of type. This function is primarily meant for use with Py\_LIMITED\_API; the individual flag bits are guaranteed to be stable across Python releases, but access to tp\_flags itself is not part of the limited API.

## New in version 3.2.

Changed in version 3.4: The return type is now unsigned long rather than long.

## void PyType\_Modified(PyTypeObject \*type)

Part of the Stable ABI. Invalidate the internal lookup cache for the type and all of its subtypes. This function must be called after any manual modification of the attributes or base classes of the type.

```txt
int PyType_HasFeature (PyTypeObject *o, int feature)
    Return non-zero if the type object o sets the feature feature. Type features are denoted by single bit flags.
int PyType_IS_GC (PyTypeObject *o)
    Return true if the type object includes support for the cycle detector; this tests the type flag
    Py_TPFLAGS_HAVE_GC.
int PyType_IsSubtype (PyTypeObject *a, PyTypeObject *b)
    Part of the Stable ABI. Return true if a is a subtype of b.
    This function only checks for actual subtypes, which means that __subclasscheck__() is not called on
    b. Call PyObject_IsSubclass() to do the same check that issubclass() would do.
PyObject *PyType_GenericAlloc (PyTypeObject *type, Py_ssize_t nitems)
    Return value: New reference. Part of the Stable ABI. Generic handler for the tp_alloc slot of a type object.
    Use Python's default memory allocation mechanism to allocate a new instance and initialize all its contents to
    NULL.
PyObject *PyType_GenericNew (PyTypeObject *type, PyObject *args, PyObject *kwds)
    Return value: New reference. Part of the Stable ABI. Generic handler for the tp_new slot of a type object.
    Create a new instance using the type's tp_alloc slot.
int PyType_Ready (PyTypeObject *type)
    Part of the Stable ABI. Finalize a type object. This should be called on all type objects to finish their initial-
    ization. This function is responsible for adding inherited slots from a type's base class. Return 0 on success,
    or return -1 and sets an exception on error.
```

**Note:** If some of the base classes implements the GC protocol and the provided type does not include the Py\_TPFLAGS\_HAVE\_GC in its flags, then the GC protocol will be automatically implemented from its parents. On the contrary, if the type being created does include Py\_TPFLAGS\_HAVE\_GC in its flags then it **must** implement the GC protocol itself by at least implementing the tp\_traverse handle.

```python
void *PyType_GetSlot (PyTypeObject *type, int slot)
    Part of the Stable ABI since version 3.4. Return the function pointer stored in the given slot. If the result is NULL, this indicates that either the slot is NULL, or that the function was called with invalid parameters. Callers will typically cast the result pointer into the appropriate function type.
    See PyType_Slot Developed for possible values of the slot argument.
    New in version 3.4.
    Changed in version 3.10: PyType_GetSlot() can now accept all types. Previously, it was limited to heap types.
PyObject *PyType_GetModule (PyTypeObject *type)
    Part of the Stable ABI since version 3.10. Return the module object associated with the given type when the type was created using PyType_FromModuleAndSpec().
    If no module is associated with the given type, sets TypeError and returns NULL.
    This function is usually used to get the module in which a method is defined. Note that in such a method, PyType_GetModule(Py_TYPE(self)) may not return the intended result. Py_TYPE(self) may be a subclass of the intended class, and subclasses are not necessarily defined in the same module as their superclass. See PyCMethod to get the class that defines the method.
    New in version 3.9.
void *PyType_GetModuleState (PyTypeObject *type)
    Part of the Stable ABI since version 3.10. Return the state of the module object associated with the given type. This is a shortcut for calling PyModule_GetState() on the result of PyType_GetModule().
    If no module is associated with the given type, sets TypeError and returns NULL.
    If the type has an associated module but its state is NULL, returns NULL without setting an exception.
    New in version 3.9.
```

## Creating Heap-Allocated Types

The following functions and structs are used to create heap types.

PyObject \***PyType\_FromModuleAndSpec**(PyObject \*module, PyType\_Spec \*spec, PyObject \*bases) Return value: New reference. Part of the Stable ABI since version 3.10. Creates and returns a heap type from the spec (Py\_TPFLAGS\_HEAPTYPE).

The bases argument can be used to specify base classes; it can either be only one class or a tuple of classes. If bases is NULL, the Py\_tp\_bases slot is used instead. If that also is NULL, the Py\_tp\_base slot is used instead. If that also is NULL, the new type derives from object.

The module argument can be used to record the module in which the new class is defined. It must be a module object or NULL. If not NULL, the module is associated with the new type and can later be retrieved with PyType\_GetModule(). The associated module is not inherited by subclasses; it must be specified for each class individually.

This function calls PyType\_Ready() on the new type.

New in version 3.9.

Changed in version 3.10: The function now accepts a single class as the bases argument and NULL as the tp\_doc slot.

## PyObject \*PyType\_FromSpecWithBases(PyType\_Spec \*spec, PyObject \*bases)

Return value: New reference. Part of the Stable ABI since version 3.3. Equivalent to PyType\_FromModuleAndSpec(NULL, spec, bases).

New in version 3.3.

PyObject \***PyType\_FromSpec**(PyType\_Spec \*spec) Return value: New reference. Part of the Stable ABI. Equivalent to PyType\_FromSpecWithBases(spec, NULL).

## type PyType\_Spec

Part of the Stable ABI (including all members). Structure defining a type’s behavior.

**const** char \*PyType\_Spec.**name** Name of the type, used to set PyTypeObject.tp\_name.

int PyType\_Spec.**basicsize**

int PyType\_Spec.**itemsize** Size of the instance in bytes, used to set PyTypeObject.tp\_basicsize and PyTypeObject. tp\_itemsize.

int PyType\_Spec.**flags** Type flags, used to set PyTypeObject.tp\_flags. If the Py\_TPFLAGS\_HEAPTYPE flag is not set, PyType\_FromSpecWithBases() sets it automatically.

PyType\_Slot \*PyType\_Spec.**slots** Array of PyType\_Slot structures. Terminated by the special slot value {0, NULL}.

## type PyType\_Slot

Part of the Stable ABI (including all members). Structure defining optional functionality of a type, containing a slot ID and a value pointer.

int PyType\_Slot.**slot**

A slot ID.

Slot IDs are named like the field names of the structures PyTypeObject, PyNumberMethods, PySequenceMethods, PyMappingMethods and PyAsyncMethods with an added Py\_ prefix. For example, use:

• Py\_tp\_dealloc to set PyTypeObject.tp\_dealloc

• Py\_nb\_add to set PyNumberMethods.nb\_add

• Py\_sq\_length to set PySequenceMethods.sq\_length

The following fields cannot be set at all using PyType\_Spec and PyType\_Slot:

• tp\_dict

• tp\_mro

• tp\_cache

• tp\_subclasses

• tp\_weaklist

• tp\_vectorcall

• tp\_weaklistoffset (see PyMemberDef)

• tp\_dictoffset (see PyMemberDef)

• tp\_vectorcall\_offset (see PyMemberDef)

The following fields cannot be set using PyType\_Spec and PyType\_Slot under the limited API:

• bf\_getbuffer

```txt
- bf_releasebuffer
```

Setting Py\_tp\_bases or Py\_tp\_base may be problematic on some platforms. To avoid issues, use the bases argument of PyType\_FromSpecWithBases() instead.

Changed in version 3.9: Slots in PyBufferProcs may be set in the unlimited API.

## void \*PyType\_Slot.pfunc

The desired value of the slot. In most cases, this is a pointer to a function.

Slots other than Py\_tp\_doc may not be NULL.

## 8.1.2 The None Object

Note that the PyTypeObject for None is not directly exposed in the Python/C API. Since None is a singleton, testing for object identity (using == in C) is sufficient. There is no PyNone\_Check() function for the same reason.

## PyObject \*Py\_None

The Python None object, denoting lack of value. This object has no methods. It needs to be treated just like any other object with respect to reference counts.

## Py\_RETURN\_NONE

Properly handle returning Py\_None from within a C function (that is, increment the reference count of None and return it.)

## 8.2 Numeric Objects

## 8.2.1 Integer Objects

All integers are implemented as “long” integer objects of arbitrary size.

On error, most PyLong\_As\* APIs return (return type)-1 which cannot be distinguished from a number. Use PyErr\_Occurred() to disambiguate.

## type PyLongObject

Part of the Limited API (as an opaque struct). This subtype of PyObject represents a Python integer object.

PyTypeObject **PyLong\_Type** Part of the Stable ABI. This instance of PyTypeObject represents the Python integer type. This is the same object as int in the Python layer.

int **PyLong\_Check**(PyObject \*p) Return true if its argument is a PyLongObject or a subtype of PyLongObject. This function always succeeds.

int **PyLong\_CheckExact**(PyObject \*p) Return true if its argument is a PyLongObject, but not a subtype of PyLongObject. This function always succeeds.

PyObject \***PyLong\_FromLong**(long v) Return value: New reference. Part of the Stable ABI. Return a new PyLongObject object from v, or NULL on failure. The current implementation keeps an array of integer objects for all integers between -5 and 256. When you create an int in that range you actually just get back a reference to the existing object.

PyObject \***PyLong\_FromUnsignedLong**(unsigned long v) Return value: New reference. Part of the Stable ABI. Return a new PyLongObject object from a C unsigned long, or NULL on failure.

PyObject \***PyLong\_FromSsize\_t**(Py\_ssize\_t v) Return value: New reference. Part of the Stable ABI. Return a new PyLongObject object from a C Py\_ssize\_t, or NULL on failure.

PyObject \***PyLong\_FromSize\_t**(size\_t v) Return value: New reference. Part of the Stable ABI. Return a new PyLongObject object from a C size\_t, or NULL on failure.

PyObject \***PyLong\_FromLongLong**(long long v) Return value: New reference. Part of the Stable ABI. Return a new PyLongObject object from a C long long, or NULL on failure.

PyObject \***PyLong\_FromUnsignedLongLong**(unsigned long long v) Return value: New reference. Part of the Stable ABI. Return a new PyLongObject object from a C unsigned long long, or NULL on failure.

PyObject \***PyLong\_FromDouble**(double v) Return value: New reference. Part of the Stable ABI. Return a new PyLongObject object from the integer part of v, or NULL on failure.

## PyObject \*PyLong\_FromString(const char \*str, char \*\*pend, int base)

Return value: New reference. Part of the Stable ABI. Return a new PyLongObject based on the string value in str, which is interpreted according to the radix in base. If pend is non-NULL, \*pend will point to the first character in str which follows the representation of the number. If base is 0, str is interpreted using the integers definition; in this case, leading zeros in a non-zero decimal number raises a ValueError. If base is not 0, it must be between 2 and 36, inclusive. Leading spaces and single underscores after a base specifier and between digits are ignored. If there are no digits, ValueError will be raised.

## See also:

Python methods int.to\_bytes() and int.from\_bytes() to convert a PyLongObject to/from an array of bytes in base 256. You can call those from C using PyObject\_CallMethod().

PyObject \***PyLong\_FromUnicodeObject**(PyObject \*u, int base)

Return value: New reference. Convert a sequence of Unicode digits in the string u to a Python integer value.

New in version 3.3.

PyObject \***PyLong\_FromVoidPtr**(void \*p)

Return value: New reference. Part of the Stable ABI. Create a Python integer from the pointer p. The pointer value can be retrieved from the resulting value using PyLong\_AsVoidPtr().

## long PyLong\_AsLong(PyObject \*obj)

Part of the Stable ABI. Return a C long representation of obj. If obj is not an instance of PyLongObject, first call its \_\_index\_\_() method (if present) to convert it to a PyLongObject.

Raise OverflowError if the value of obj is out of range for a long.

Returns -1 on error. Use PyErr\_Occurred() to disambiguate.

Changed in version 3.8: Use \_\_index\_\_() if available.

Changed in version 3.10: This function will no longer use \_\_int\_\_().

## long PyLong\_AsLongAndOverflow(PyObject \*obj, int \*overflow)

Part of the Stable ABI. Return a C long representation of obj. If obj is not an instance of PyLongObject, first call its \_\_index\_\_() method (if present) to convert it to a PyLongObject.

If the value of obj is greater than LONG\_MAX or less than LONG\_MIN, set \*overflow to 1 or -1, respectively, and return -1; otherwise, set \*overflow to 0. If any other exception occurs set \*overflow to 0 and return -1 as usual.

Returns -1 on error. Use PyErr\_Occurred() to disambiguate.

Changed in version 3.8: Use \_\_index\_\_() if available.

Changed in version 3.10: This function will no longer use \_\_int\_\_().

## long long PyLong\_AsLongLong(PyObject \*obj)

Part of the Stable ABI. Return a C long long representation of obj. If obj is not an instance of PyLongObject, first call its \_\_index\_\_() method (if present) to convert it to a PyLongObject.

Raise OverflowError if the value of obj is out of range for a long long.

Returns -1 on error. Use PyErr\_Occurred() to disambiguate.

Changed in version 3.8: Use \_\_index\_\_() if available.

Changed in version 3.10: This function will no longer use \_\_int\_\_().

## long long PyLong\_AsLongLongAndOverflow(PyObject \*obj, int \*overflow)

Part of the Stable ABI. Return a C long long representation of obj. If obj is not an instance of PyLongObject, first call its \_\_index\_\_() method (if present) to convert it to a PyLongObject.

If the value of obj is greater than LLONG\_MAX or less than LLONG\_MIN, set \*overflow to 1 or -1, respectively, and return -1; otherwise, set \*overflow to 0. If any other exception occurs set \*overflow to 0 and return -1 as usual.

Returns -1 on error. Use PyErr\_Occurred() to disambiguate.

New in version 3.2.

Changed in version 3.8: Use \_\_index\_\_() if available.

Changed in version 3.10: This function will no longer use \_\_int\_\_().

## Py\_ssize\_t PyLong\_AsSsize\_t(PyObject \*pylong)

Part of the Stable ABI. Return a C Py\_ssize\_t representation of pylong. pylong must be an instance of PyLongObject.

Raise OverflowError if the value of pylong is out of range for a Py\_ssize\_t.

Returns -1 on error. Use PyErr\_Occurred() to disambiguate.

## unsigned long PyLong\_AsUnsignedLong(PyObject \*pylong)

Part of the Stable ABI. Return a C unsigned long representation of pylong. pylong must be an instance of PyLongObject.

Raise OverflowError if the value of pylong is out of range for a unsigned long.

Returns (unsigned long)-1 on error. Use PyErr\_Occurred() to disambiguate.

size\_t **PyLong\_AsSize\_t**(PyObject \*pylong) Part of the Stable ABI. Return a C size\_t representation of pylong. pylong must be an instance of PyLongObject. Raise OverflowError if the value of pylong is out of range for a size\_t. Returns (size\_t)-1 on error. Use PyErr\_Occurred() to disambiguate.

unsigned long long **PyLong\_AsUnsignedLongLong**(PyObject \*pylong) Part of the Stable ABI. Return a C unsigned long long representation of pylong. pylong must be an instance of PyLongObject. Raise OverflowError if the value of pylong is out of range for an unsigned long long. Returns (unsigned long long)-1 on error. Use PyErr\_Occurred() to disambiguate. Changed in version 3.1: A negative pylong now raises OverflowError, not TypeError.

unsigned long **PyLong\_AsUnsignedLongMask**(PyObject \*obj) Part of the Stable ABI. Return a C unsigned long representation of obj. If obj is not an instance of PyLongObject, first call its \_\_index\_\_() method (if present) to convert it to a PyLongObject. If the value of obj is out of range for an unsigned long, return the reduction of that value modulo ULONG\_MAX + 1. Returns (unsigned long)-1 on error. Use PyErr\_Occurred() to disambiguate. Changed in version 3.8: Use \_\_index\_\_() if available. Changed in version 3.10: This function will no longer use \_\_int\_\_().

unsigned long long **PyLong\_AsUnsignedLongLongMask**(PyObject \*obj) Part of the Stable ABI. Return a C unsigned long long representation of obj. If obj is not an instance of PyLongObject, first call its \_\_index\_\_() method (if present) to convert it to a PyLongObject. If the value of obj is out of range for an unsigned long long, return the reduction of that value modulo ULLONG\_MAX + 1. Returns (unsigned long long)-1 on error. Use PyErr\_Occurred() to disambiguate. Changed in version 3.8: Use \_\_index\_\_() if available. Changed in version 3.10: This function will no longer use \_\_int\_\_().

double **PyLong\_AsDouble**(PyObject \*pylong) Part of the Stable ABI. Return a C double representation of pylong. pylong must be an instance of PyLongObject. Raise OverflowError if the value of pylong is out of range for a double. Returns -1.0 on error. Use PyErr\_Occurred() to disambiguate.

void \***PyLong\_AsVoidPtr**(PyObject \*pylong) Part of the Stable ABI. Convert a Python integer pylong to a C void pointer. If pylong cannot be converted, an OverflowError will be raised. This is only assured to produce a usable void pointer for values created with PyLong\_FromVoidPtr(). Returns NULL on error. Use PyErr\_Occurred() to disambiguate.

## 8.2.2 Boolean Objects

Booleans in Python are implemented as a subclass of integers. There are only two booleans, Py\_False and Py\_True. As such, the normal creation and deletion functions don’t apply to booleans. The following macros are available, however.

## int PyBool\_Check(PyObject \*o)

Return true if o is of type PyBool\_Type. This function always succeeds.

## PyObject \*Py\_False

The Python False object. This object has no methods. It needs to be treated just like any other object with respect to reference counts.

## PyObject \*Py\_True

The Python True object. This object has no methods. It needs to be treated just like any other object with respect to reference counts.

## Py\_RETURN\_FALSE

Return Py\_False from a function, properly incrementing its reference count.

## Py\_RETURN\_TRUE

Return Py\_True from a function, properly incrementing its reference count.

## PyObject \*PyBool\_FromLong(long v)

Return value: New reference. Part of the Stable ABI. Return a new reference to Py\_True or Py\_False depending on the truth value of v.

## 8.2.3 Floating Point Objects

## type PyFloatObject

This subtype of PyObject represents a Python floating point object.

## PyTypeObject PyFloat\_Type

Part of the Stable ABI. This instance of PyTypeObject represents the Python floating point type. This is the same object as float in the Python layer.

## int PyFloat\_Check(PyObject \*p)

Return true if its argument is a PyFloatObject or a subtype of PyFloatObject. This function always succeeds.

## int PyFloat\_CheckExact(PyObject \*p)

Return true if its argument is a PyFloatObject, but not a subtype of PyFloatObject. This function always succeeds.

## PyObject \*PyFloat\_FromString(PyObject \*str)

Return value: New reference. Part of the Stable ABI. Create a PyFloatObject object based on the string value in str, or NULL on failure.

## PyObject \*PyFloat\_FromDouble(double v)

Return value: New reference. Part of the Stable ABI. Create a PyFloatObject object from v, or NULL on failure.

## double PyFloat\_AsDouble(PyObject \*pyfloat)

Part of the Stable ABI. Return a C double representation of the contents of pyfloat. If pyfloat is not a Python floating point object but has a \_\_float\_\_() method, this method will first be called to convert pyfloat into a float. If \_\_float\_\_() is not defined then it falls back to \_\_index\_\_(). This method returns -1.0 upon failure, so one should call PyErr\_Occurred() to check for errors.

Changed in version 3.8: Use \_\_index\_\_() if available.

## double PyFloat\_AS\_DOUBLE(PyObject \*pyfloat)

Return a C double representation of the contents of pyfloat, but without error checking.

## PyObject \*PyFloat\_GetInfo(void)

Return value: New reference. Part of the Stable ABI. Return a structseq instance which contains information about the precision, minimum and maximum values of a float. It’s a thin wrapper around the header file float.h.

```txt
double PyFloat_GetMax()
```

Part of the Stable ABI. Return the maximum representable finite float DBL\_MAX as C double.

double **PyFloat\_GetMin**()

Part of the Stable ABI. Return the minimum normalized positive float DBL\_MIN as C double.

## 8.2.4 Complex Number Objects

Python’s complex number objects are implemented as two distinct types when viewed from the C API: one is the Python object exposed to Python programs, and the other is a C structure which represents the actual complex number value. The API provides functions for working with both.

## Complex Numbers as C Structures

Note that the functions which accept these structures as parameters and return them as results do so by value rather than dereferencing them through pointers. This is consistent throughout the API.

## type Py\_complex

The C structure which corresponds to the value portion of a Python complex number object. Most of the functions for dealing with complex number objects use structures of this type as input or output values, as appropriate. It is defined as:

```txt
typedef struct {
    double real;
    double imag;
} Py_complex;
```

Py\_complex **\_Py\_c\_sum**(Py\_complex left, Py\_complex right) Return the sum of two complex numbers, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_diff**(Py\_complex left, Py\_complex right) Return the difference between two complex numbers, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_neg**(Py\_complex num) Return the negation of the complex number num, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_prod**(Py\_complex left, Py\_complex right) Return the product of two complex numbers, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_quot**(Py\_complex dividend, Py\_complex divisor) Return the quotient of two complex numbers, using the C Py\_complex representation.

If divisor is null, this method returns zero and sets errno to EDOM.

Py\_complex **\_Py\_c\_pow**(Py\_complex num, Py\_complex exp) Return the exponentiation of num by exp, using the C Py\_complex representation.

If num is null and exp is not a positive real number, this method returns zero and sets errno to EDOM.

## Complex Numbers as Python Objects

## type PyComplexObject

This subtype of PyObject represents a Python complex number object.

## PyTypeObject PyComplex\_Type

Part of the Stable ABI. This instance of PyTypeObject represents the Python complex number type. It is the same object as complex in the Python layer.

## int PyComplex\_Check(PyObject \*p)

Return true if its argument is a PyComplexObject or a subtype of PyComplexObject. This function always succeeds.

## int PyComplex\_CheckExact(PyObject \*p)

Return true if its argument is a PyComplexObject , but not a subtype of PyComplexObject. This function always succeeds.

## PyObject \*PyComplex\_FromCComplex(Py\_complex v)

Return value: New reference. Create a new Python complex number object from a C Py\_complex value.

## PyObject \*PyComplex\_FromDoubles(double real, double imag)

Return value: New reference. Part of the Stable ABI. Return a new PyComplexObject object from real and imag.

## double PyComplex\_RealAsDouble(PyObject \*op)

Part of the Stable ABI. Return the real part of op as a C double.

## double PyComplex\_ImagAsDouble(PyObject \*op)

Part of the Stable ABI. Return the imaginary part of op as a C double.

## Py\_complex PyComplex\_AsCComplex(PyObject \*op)

Return the Py\_complex value of the complex number op.

If op is not a Python complex number object but has a \_\_complex\_\_() method, this method will first be called to convert op to a Python complex number object. If \_\_complex\_\_() is not defined then it falls back to \_\_float\_\_(). If \_\_float\_\_() is not defined then it falls back to \_\_index\_\_(). Upon failure, this method returns -1.0 as a real value.

Changed in version 3.8: Use \_\_index\_\_() if available.

## 8.3 Sequence Objects

Generic operations on sequence objects were discussed in the previous chapter; this section deals with the specific kinds of sequence objects that are intrinsic to the Python language.

## 8.3.1 Bytes Objects

These functions raise TypeError when expecting a bytes parameter and called with a non-bytes parameter.

## type PyBytesObject

This subtype of PyObject represents a Python bytes object.

## PyTypeObject PyBytes\_Type

Part of the Stable ABI. This instance of PyTypeObject represents the Python bytes type; it is the same object as bytes in the Python layer.

## int PyBytes\_Check(PyObject \*o)

Return true if the object o is a bytes object or an instance of a subtype of the bytes type. This function always succeeds.

int **PyBytes\_CheckExact** (PyObject \*o)

Return true if the object o is a bytes object, but not an instance of a subtype of the bytes type. This function always succeeds.

PyObject \***PyBytes\_FromString**(**const** char \*v)

Return value: New reference. Part of the Stable ABI. Return a new bytes object with a copy of the string v as value on success, and NULL on failure. The parameter v must not be NULL; it will not be checked.

PyObject \***PyBytes\_FromStringAndSize**(**const** char \*v, Py\_ssize\_t len)

Return value: New reference. Part of the Stable ABI. Return a new bytes object with a copy of the string v as value and length len on success, and NULL on failure. If v is NULL, the contents of the bytes object are uninitialized.

PyObject \***PyBytes\_FromFormat**(**const** char \*format, ...)

Return value: New reference. Part of the Stable ABI. Take a C printf()-style format string and a variable number of arguments, calculate the size of the resulting Python bytes object and return a bytes object with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the format string. The following format characters are allowed:

| Format Characters | Type | Comment |
| --- | --- | --- |
| %% | n/a | The literal % character. |
| %c | int | A single byte, represented as a C int. |
| %d | int | Equivalent to printf("%d").<sup>1</sup> |
| %u | unsigned int | Equivalent to printf("%u").<sup>1</sup> |
| %ld | long | Equivalent to printf("%ld").<sup>1</sup> |
| %lu | unsigned long | Equivalent to printf("%lu").<sup>1</sup> |
| %zd | Py_ssize_t | Equivalent to printf("%zd").<sup>1</sup> |
| %zu | size_t | Equivalent to printf("%zu").<sup>1</sup> |
| %i | int | Equivalent to printf("%i").<sup>1</sup> |
| %x | int | Equivalent to printf("%x").<sup>1</sup> |
| %s | const char* | A null-terminated C character array. |
| %p | const void* | The hex representation of a C pointer. Mostly equivalent to printf("%p") except that it is guaranteed to start with the literal 0x regardless of what the platform's printf yields. |

An unrecognized format character causes all the rest of the format string to be copied as-is to the result object, and any extra arguments discarded.

PyObject \***PyBytes\_FromFormatV**(**const** char \*format, va\_list vargs)

Return value: New reference. Part of the Stable ABI. Identical to PyBytes\_FromFormat() except that it takes exactly two arguments.

PyObject \***PyBytes\_FromObject** (PyObject \*o)

Return value: New reference. Part of the Stable ABI. Return the bytes representation of object o that implements the buffer protocol.

Py\_ssize\_t **PyBytes\_Size**(PyObject \*o)

Part of the Stable ABI. Return the length of the bytes in bytes object o.

Py\_ssize\_t **PyBytes\_GET\_SIZE**(PyObject \*o) Macro form of PyBytes\_Size() but without error checking.

char \***PyBytes\_AsString** (PyObject \*o)

Part of the Stable ABI. Return a pointer to the contents of o. The pointer refers to the internal buffer of o, which consists of len(o) + 1 bytes. The last byte in the buffer is always null, regardless of whether there are any other null bytes. The data must not be modified in any way, unless the object was just created using PyBytes\_FromStringAndSize(NULL, size). It must not be deallocated. If o is not a bytes object at all, PyBytes\_AsString() returns NULL and raises TypeError.

  1 For integer specifiers (d, u, ld, lu, zd, zu, i, x): the 0-conversion flag has effect even when a precision is given.

## char \*PyBytes\_AS\_STRING(PyObject \*string)

Macro form of PyBytes\_AsString() but without error checking.

## int PyBytes\_AsStringAndSize(PyObject \*obj, char \*\*buffer, Py\_ssize\_t \*length)

Part of the Stable ABI. Return the null-terminated contents of the object obj through the output variables buffer and length.

If length is NULL, the bytes object may not contain embedded null bytes; if it does, the function returns -1 and a ValueError is raised.

The buffer refers to an internal buffer of obj, which includes an additional null byte at the end (not counted in length). The data must not be modified in any way, unless the object was just created using PyBytes\_FromStringAndSize(NULL, size). It must not be deallocated. If obj is not a bytes object at all, PyBytes\_AsStringAndSize() returns -1 and raises TypeError.

Changed in version 3.5: Previously, TypeError was raised when embedded null bytes were encountered in the bytes object.

## void PyBytes\_Concat(PyObject \*\*bytes, PyObject \*newpart)

Part of the Stable ABI. Create a new bytes object in \*bytes containing the contents of newpart appended to bytes; the caller will own the new reference. The reference to the old value of bytes will be stolen. If the new object cannot be created, the old reference to bytes will still be discarded and the value of \*bytes will be set to NULL; the appropriate exception will be set.

## void PyBytes\_ConcatAndDel(PyObject \*\*bytes, PyObject \*newpart)

Part of the Stable ABI. Create a new bytes object in \*bytes containing the contents of newpart appended to bytes. This version releases the strong reference to newpart (i.e. decrements its reference count).

## int \_PyBytes\_Resize(PyObject \*\*bytes, Py\_ssize\_t newsize)

A way to resize a bytes object even though it is “immutable”. Only use this to build up a brand new bytes object; don’t use this if the bytes may already be known in other parts of the code. It is an error to call this function if the refcount on the input bytes object is not one. Pass the address of an existing bytes object as an lvalue (it may be written into), and the new size desired. On success, \*bytes holds the resized bytes object and 0 is returned; the address in \*bytes may differ from its input value. If the reallocation fails, the original bytes object at \*bytes is deallocated, \*bytes is set to NULL, MemoryError is set, and -1 is returned.

## 8.3.2 Byte Array Objects

## type PyByteArrayObject

This subtype of PyObject represents a Python bytearray object.

## PyTypeObject PyByteArray\_Type

Part of the Stable ABI. This instance of PyTypeObject represents the Python bytearray type; it is the same object as bytearray in the Python layer.

## Type check macros

## int PyByteArray\_Check(PyObject \*o)

Return true if the object o is a bytearray object or an instance of a subtype of the bytearray type. This function always succeeds.

## int PyByteArray\_CheckExact(PyObject \*o)

Return true if the object o is a bytearray object, but not an instance of a subtype of the bytearray type. This function always succeeds.

## Direct API functions

PyObject \***PyByteArray\_FromObject**(PyObject \*o) Return value: New reference. Part of the Stable ABI. Return a new bytearray object from any object, o, that implements the buffer protocol.

PyObject \***PyByteArray\_FromStringAndSize**(**const** char \*string, Py\_ssize\_t len) Return value: New reference. Part of the Stable ABI. Create a new bytearray object from string and its length, len. On failure, NULL is returned.

PyObject \***PyByteArray\_Concat**(PyObject \*a, PyObject \*b) Return value: New reference. Part of the Stable ABI. Concat bytearrays a and b and return a new bytearray with the result.

Py\_ssize\_t **PyByteArray\_Size**(PyObject \*bytearray) Part of the Stable ABI. Return the size of bytearray after checking for a NULL pointer.

char \***PyByteArray\_AsString**(PyObject \*bytearray) Part of the Stable ABI. Return the contents of bytearray as a char array after checking for a NULL pointer. The returned array always has an extra null byte appended.

int **PyByteArray\_Resize**(PyObject \*bytearray, Py\_ssize\_t len) Part of the Stable ABI. Resize the internal buffer of bytearray to len.

## Macros

These macros trade safety for speed and they don’t check pointers.

char \***PyByteArray\_AS\_STRING**(PyObject \*bytearray) Macro version of PyByteArray\_AsString().

Py\_ssize\_t **PyByteArray\_GET\_SIZE**(PyObject \*bytearray) Macro version of PyByteArray\_Size().

## 8.3.3 Unicode Objects and Codecs

## Unicode Objects

Since the implementation of [**PEP 393**](https://www.python.org/dev/peps/pep-0393) in Python 3.3, Unicode objects internally use a variety of representations, in order to allow handling the complete range of Unicode characters while staying memory efficient. There are special cases for strings where all code points are below 128, 256, or 65536; otherwise, code points must be below 1114112 (which is the full Unicode range).

Py\_UNICODE\* and UTF-8 representations are created on demand and cached in the Unicode object. The Py\_UNICODE\* representation is deprecated and inefficient.

Due to the transition between the old APIs and the new APIs, Unicode objects can internally be in two states depending on how they were created:

• “canonical” Unicode objects are all objects created by a non-deprecated Unicode API. They use the most efficient representation allowed by the implementation.

• “legacy” Unicode objects have been created through one of the deprecated APIs (typically PyUnicode\_FromUnicode()) and only bear the Py\_UNICODE\* representation; you will have to call PyUnicode\_READY() on them before calling any other API.

**Note:** The “legacy” Unicode object will be removed in Python 3.12 with deprecated APIs. All Unicode objects will be “canonical” since then. See [**PEP 623**](https://www.python.org/dev/peps/pep-0623) for more information.

## Unicode Type

These are the basic Unicode object types used for the Unicode implementation in Python:

## type Py\_UCS4

**type Py\_UCS2**

**type Py\_UCS1** Part of the Stable ABI. These types are typedefs for unsigned integer types wide enough to contain characters of 32 bits, 16 bits and 8 bits, respectively. When dealing with single Unicode characters, use Py\_UCS4. New in version 3.3.

## type Py\_UNICODE

This is a typedef of wchar\_t, which is a 16-bit type or 32-bit type depending on the platform.

Changed in version 3.3: In previous versions, this was a 16-bit type or a 32-bit type depending on whether you selected a “narrow” or “wide” Unicode version of Python at build time.

## type PyASCIIObject

## type PyCompactUnicodeObject

## type PyUnicodeObject

These subtypes of PyObject represent a Python Unicode object. In almost all cases, they shouldn’t be used directly, since all API functions that deal with Unicode objects take and return PyObject pointers.

New in version 3.3.

## PyTypeObject PyUnicode\_Type

Part of the Stable ABI. This instance of PyTypeObject represents the Python Unicode type. It is exposed to Python code as str.

The following APIs are really C macros and can be used to do fast checks and to access internal read-only data of Unicode objects:

## int PyUnicode\_Check(PyObject \*o)

Return true if the object o is a Unicode object or an instance of a Unicode subtype. This function always succeeds.

## int PyUnicode\_CheckExact(PyObject \*o)

Return true if the object o is a Unicode object, but not an instance of a subtype. This function always succeeds.

## int PyUnicode\_READY(PyObject \*o)

Ensure the string object o is in the “canonical” representation. This is required before using any of the access macros described below.

Returns 0 on success and -1 with an exception set on failure, which in particular happens if memory allocation fails.

New in version 3.3.

Deprecated since version 3.10, will be removed in version 3.12: This API will be removed with PyUnicode\_FromUnicode().

## Py\_ssize\_t PyUnicode\_GET\_LENGTH(PyObject \*o)

Return the length of the Unicode string, in code points. o has to be a Unicode object in the “canonical” representation (not checked).

New in version 3.3.

## Py\_UCS1 \*PyUnicode\_1BYTE\_DATA(PyObject \*o)

Py\_UCS2 \***PyUnicode\_2BYTE\_DATA**(PyObject \*o)

## Py\_UCS4 \*PyUnicode\_4BYTE\_DATA(PyObject \*o)

Return a pointer to the canonical representation cast to UCS1, UCS2 or UCS4 integer types for direct character access. No checks are performed if the canonical representation has the correct character size; use PyUnicode\_KIND() to select the right macro. Make sure PyUnicode\_READY() has been called before accessing this.

**PyUnicode\_4BYTE\_KIND** Return values of the PyUnicode\_KIND() macro. New in version 3.3. Deprecated since version 3.10, will be removed in version 3.12: PyUnicode\_WCHAR\_KIND is deprecated.

unsigned int **PyUnicode\_KIND**(PyObject \*o) Return one of the PyUnicode kind constants (see above) that indicate how many bytes per character this Unicode object uses to store its data. o has to be a Unicode object in the “canonical” representation (not checked).

void \***PyUnicode\_DATA**(PyObject \*o) Return a void pointer to the raw Unicode buffer. o has to be a Unicode object in the “canonical” representation (not checked). New in version 3.3.

void **PyUnicode\_WRITE**(int kind, void \*data, Py\_ssize\_t index, Py\_UCS4 value) Write into a canonical representation data (as obtained with PyUnicode\_DATA()). This macro does not do any sanity checks and is intended for usage in loops. The caller should cache the kind value and data pointer as obtained from other macro calls. index is the index in the string (starts at 0) and value is the new code point value which should be written to that location.

Py\_UCS4 **PyUnicode\_READ**(int kind, void \*data, Py\_ssize\_t index) Read a code point from a canonical representation data (as obtained with PyUnicode\_DATA()). No checks or ready calls are performed. New in version 3.3.

Py\_UCS4 **PyUnicode\_READ\_CHAR**(PyObject \*o, Py\_ssize\_t index) Read a character from a Unicode object o, which must be in the “canonical” representation. This is less efficient than PyUnicode\_READ() if you do multiple consecutive reads. New in version 3.3.

**PyUnicode\_MAX\_CHAR\_VALUE**(o) Return the maximum code point that is suitable for creating another string based on o, which must be in the “canonical” representation. This is always an approximation but more efficient than iterating over the string. New in version 3.3.

Py\_ssize\_t **PyUnicode\_GET\_SIZE**(PyObject \*o) Return the size of the deprecated Py\_UNICODE representation, in code units (this includes surrogate pairs as 2 units). o has to be a Unicode object (not checked). Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Unicode API, please migrate to using PyUnicode\_GET\_LENGTH().

Py\_ssize\_t **PyUnicode\_GET\_DATA\_SIZE**(PyObject \*o) Return the size of the deprecated Py\_UNICODE representation in bytes. o has to be a Unicode object (not checked). Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Unicode API, please migrate to using PyUnicode\_GET\_LENGTH().

Py\_UNICODE \***PyUnicode\_AS\_UNICODE**(PyObject \*o)

## const char \*PyUnicode\_AS\_DATA(PyObject \*o)

Return a pointer to a Py\_UNICODE representation of the object. The returned buffer is always terminated with an extra null code point. It may also contain embedded null code points, which would cause the string to be truncated when used in most C functions. The AS\_DATA form casts the pointer to **const** char\*. The o argument has to be a Unicode object (not checked).

Changed in version 3.3: This macro is now inefficient – because in many cases the Py\_UNICODE representation does not exist and needs to be created – and can fail (return NULL with an exception set). Try to port the code to use the new PyUnicode\_nBYTE\_DATA() macros or use PyUnicode\_WRITE() or PyUnicode\_READ().

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Unicode API, please migrate to using the PyUnicode\_nBYTE\_DATA() family of macros.

## int PyUnicode\_IsIdentifier(PyObject \*o)

Part of the Stable ABI. Return 1 if the string is a valid identifier according to the language definition, section identifiers. Return 0 otherwise.

Changed in version 3.9: The function does not call Py\_FatalError() anymore if the string is not ready.

## Unicode Character Properties

Unicode provides many different character properties. The most often needed ones are available through these macros which are mapped to C functions depending on the Python configuration.

int **Py\_UNICODE\_ISSPACE**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is a whitespace character.

int **Py\_UNICODE\_ISLOWER**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is a lowercase character.

int **Py\_UNICODE\_ISUPPER**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is an uppercase character.

int **Py\_UNICODE\_ISTITLE**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is a titlecase character.

int **Py\_UNICODE\_ISLINEBREAK**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is a linebreak character.

int **Py\_UNICODE\_ISDECIMAL**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is a decimal character.

int **Py\_UNICODE\_ISDIGIT**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is a digit character.

int **Py\_UNICODE\_ISNUMERIC**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is a numeric character.

int **Py\_UNICODE\_ISALPHA**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is an alphabetic character.

int **Py\_UNICODE\_ISALNUM**(Py\_UCS4 ch) Return 1 or 0 depending on whether ch is an alphanumeric character.

## int Py\_UNICODE\_ISPRINTABLE(Py\_UCS4 ch)

Return 1 or 0 depending on whether ch is a printable character. Nonprintable characters are those characters defined in the Unicode character database as “Other” or “Separator”, excepting the ASCII space (0x20) which is considered printable. (Note that printable characters in this context are those which should not be escaped when repr() is invoked on a string. It has no bearing on the handling of strings written to sys.stdout or sys.stderr.)

These APIs can be used for fast direct character conversions:

Py\_UCS4 **Py\_UNICODE\_TOLOWER**(Py\_UCS4 ch) Return the character ch converted to lower case. Deprecated since version 3.3: This function uses simple case mappings.

Py\_UCS4 **Py\_UNICODE\_TOUPPER**(Py\_UCS4 ch) Return the character ch converted to upper case.

Deprecated since version 3.3: This function uses simple case mappings.

Py\_UCS4 **Py\_UNICODE\_TOTITLE**(Py\_UCS4 ch) Return the character ch converted to title case.

Deprecated since version 3.3: This function uses simple case mappings.

int **Py\_UNICODE\_TODECIMAL**(Py\_UCS4 ch) Return the character ch converted to a decimal positive integer. Return -1 if this is not possible. This macro does not raise exceptions.

int **Py\_UNICODE\_TODIGIT**(Py\_UCS4 ch) Return the character ch converted to a single digit integer. Return -1 if this is not possible. This macro does not raise exceptions.

double **Py\_UNICODE\_TONUMERIC**(Py\_UCS4 ch) Return the character ch converted to a double. Return -1.0 if this is not possible. This macro does not raise exceptions.

These APIs can be used to work with surrogates:

```txt
Py_UNICODE_IS_SURROGATE (ch)
    Check if ch is a surrogate (0xD800 <= ch <= 0xDFFF).
txt
Py_UNICODE_IS_HIGH_SURROGATE (ch)
    Check if ch is a high surrogate (0xD800 <= ch <= 0xDBFF).
txt
Py_UNICODE_IS_LOW_SURROGATE (ch)
    Check if ch is a low surrogate (0xDC00 <= ch <= 0xDFFF).
```

## P \_UNICODE\_JOIN\_SURROGATES(hi h l ) Py\_UNICODE\_JOIN\_SURROGATES (high, low)

Join two surrogate characters and return a single Py\_UCS4 value. high and low are respectively the leading and trailing surrogates in a surrogate pair.

## Creating and accessing Unicode strings

To create Unicode objects and access their basic sequence properties, use these APIs:

PyObject \***PyUnicode\_New**(Py\_ssize\_t size, Py\_UCS4 maxchar)

Return value: New reference. Create a new Unicode object. maxchar should be the true maximum code point to be placed in the string. As an approximation, it can be rounded up to the nearest value in the sequence 127, 255, 65535, 1114111.

This is the recommended way to allocate a new Unicode object. Objects created using this function are not resizable.

New in version 3.3.

PyObject \***PyUnicode\_FromKindAndData**(int kind, **const** void \*buffer, Py\_ssize\_t size)

Return value: New reference. Create a new Unicode object with the given kind (possible values are PyUnicode\_1BYTE\_KIND etc., as returned by PyUnicode\_KIND()). The buffer must point to an array of size units of 1, 2 or 4 bytes per character, as given by the kind.

New in version 3.3.

PyObject \***PyUnicode\_FromStringAndSize**(**const** char \*u, Py\_ssize\_t size)

Return value: New reference. Part of the Stable ABI. Create a Unicode object from the char buffer u. The bytes will be interpreted as being UTF-8 encoded. The buffer is copied into the new object. If the buffer is not NULL, the return value might be a shared object, i.e. modification of the data is not allowed.

If u is NULL, this function behaves like PyUnicode\_FromUnicode() with the buffer set to NULL. This usage is deprecated in favor of PyUnicode\_New(), and will be removed in Python 3.12.

## PyObject \*PyUnicode\_FromString(const char \*u)

Return value: New reference. Part of the Stable ABI. Create a Unicode object from a UTF-8 encoded nullterminated char buffer u.

## PyObject \*PyUnicode\_FromFormat(const char \*format, ...)

Return value: New reference. Part of the Stable ABI. Take a C printf()-style format string and a variable number of arguments, calculate the size of the resulting Python Unicode string and return a string with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the format ASCII-encoded string. The following format characters are allowed:

| Format Characters | Type | Comment |
| --- | --- | --- |
| %% | n/a | The literal % character. |
| %c | int | A single character, represented as a C int. |
| %d | int | Equivalent to printf("%d").<sup>1</sup> |
| %u | unsigned int | Equivalent to printf("%u").<sup>1</sup> |
| %ld | long | Equivalent to printf("%ld").<sup>1</sup> |
| %li | long | Equivalent to printf("%li").<sup>1</sup> |
| %lu | unsigned long | Equivalent to printf("%lu").<sup>1</sup> |
| %lld | long long | Equivalent to printf("%lld").<sup>1</sup> |
| %lli | long long | Equivalent to printf("%lli").<sup>1</sup> |
| %llu | unsigned long long | Equivalent to printf("%llu").<sup>1</sup> |
| %zd | Py_ssize_t | Equivalent to printf("%zd").<sup>1</sup> |
| %zi | Py_ssize_t | Equivalent to printf("%zi").<sup>1</sup> |
| %zu | size_t | Equivalent to printf("%zu").<sup>1</sup> |
| %i | int | Equivalent to printf("%i").<sup>1</sup> |
| %x | int | Equivalent to printf("%x").<sup>1</sup> |
| %s | const char* | A null-terminated C character array. |
| %p | const void* | The hex representation of a C pointer. Mostly equivalent to printf("%p") except that it is guaranteed to start with the literal 0x regardless of what the platform's printf yields. |
| %A | PyObject* | The result of calling ascii(). |
| %U | PyObject* | A Unicode object. |
| %V | PyObject*, const char* | A Unicode object (which may be NULL) and a null-terminated C character array as a second parameter (which will be used, if the first parameter is NULL). |
| %S | PyObject* | The result of calling PyObject_Str(). |
| %R | PyObject* | The result of calling PyObject_Repr(). |

An unrecognized format character causes all the rest of the format string to be copied as-is to the result string, and any extra arguments discarded.

**Note:** The width formatter unit is number of characters rather than bytes. The precision formatter unit is number of bytes for "%s" and "%V" (if the PyObject\* argument is NULL), and a number of characters for "%A", "%U", "%S", "%R" and "%V" (if the PyObject\* argument is not NULL).

Changed in version 3.2: Support for "%lld" and "%llu" added.

Changed in version 3.3: Support for "%li", "%lli" and "%zi" added.

Changed in version 3.4: Support width and precision formatter for "%s", "%A", "%U", "%V", "%S", "%R" added.

  1 For integer specifiers (d, u, ld, li, lu, lld, lli, llu, zd, zi, zu, i, x): the 0-conversion flag has effect even when a precision is given.

PyObject \*PyUnicode\_Substring(PyObject \*str, Py\_ssize\_t start, Py\_ssize\_t end) Return value: New reference. Part of the Stable ABI since version 3.7. Return a substring of str, from character index start (included) to character index end (excluded). Negative indices are not supported. New in version 3.3.

PyObject \*PyUnicode\_FromFormatV(const char \*format, va\_list vargs) Return value: New reference. Part of the Stable ABI. Identical to PyUnicode\_FromFormat() except that it takes exactly two arguments.

PyObject \*PyUnicode\_FromEncodedObject(PyObject \*obj, const char \*encoding, const char \*errors) Return value: New reference. Part of the Stable ABI. Decode an encoded object obj to a Unicode object.

Py\_ssize\_t PyUnicode\_GetLength(PyObject \*unicode) Part of the Stable ABI since version 3.7. Return the length of the Unicode object, in code points. New in version 3.3.

Py\_ssize\_t PyUnicode\_CopyCharacters(PyObject \*to, Py\_ssize\_t to\_start, PyObject \*from, Py\_ssize\_t from\_start, Py\_ssize\_t how\_many) Copy characters from one Unicode object into another. This function performs character conversion when necessary and falls back to memcpy() if possible. Returns -1 and sets an exception on error, otherwise returns the number of copied characters.

Py\_ssize\_t PyUnicode\_Fill(PyObject \*unicode, Py\_ssize\_t start, Py\_ssize\_t length, Py\_UCS4 fill\_char) Fill a string with a character: write fill\_char into unicode[start:start+length]. Fail if fill\_char is bigger than the string maximum character, or if the string has more than 1 reference. Return the number of written character, or return -1 and raise an exception on error. New in version 3.3.

int PyUnicode\_WriteChar(PyObject \*unicode, Py\_ssize\_t index, Py\_UCS4 character) Part of the Stable ABI since version 3.7. Write a character to a string. The string must have been created through PyUnicode\_New(). Since Unicode strings are supposed to be immutable, the string must not be shared, or have been hashed yet. This function checks that unicode is a Unicode object, that the index is not out of bounds, and that the object can be modified safely (i.e. that it its reference count is one). New in version 3.3.

Py\_UCS4 **PyUnicode\_ReadChar**(PyObject \*unicode, Py\_ssize\_t index) Part of the Stable ABI since version 3.7. Read a character from a string. This function checks that unicode is a Unicode object and the index is not out of bounds, in contrast to the macro version PyUnicode\_READ\_CHAR().

Py\_UCS4 \*PyUnicode\_AsUCS4(PyObject \*u, Py\_UCS4 \*buffer, Py\_ssize\_t buflen, int copy\_null) Part of the Stable ABI since version 3.7. Copy the string u into a UCS4 buffer, including a null character, if copy\_null is set. Returns NULL and sets an exception on error (in particular, a SystemError if buflen is smaller than the length of u). buffer is returned on success. New in version 3.3.

## Py\_UCS4 \*PyUnicode\_AsUCS4Copy(PyObject \*u)

Part of the Stable ABI since version 3.7. Copy the string u into a new UCS4 buffer that is allocated using PyMem\_Malloc(). If this fails, NULL is returned with a MemoryError set. The returned buffer always has an extra null code point appended.

New in version 3.3.

## Deprecated Py\_UNICODE APIs

Deprecated since version 3.3, will be removed in version 3.12.

These API functions are deprecated with the implementation of [**PEP 393**](https://www.python.org/dev/peps/pep-0393). Extension modules can continue using them, as they will not be removed in Python 3.x, but need to be aware that their use can now cause performance and memory hits.

## PyObject \*PyUnicode\_FromUnicode(const Py\_UNICODE \*u, Py\_ssize\_t size)

Return value: New reference. Create a Unicode object from the Py\_UNICODE buffer u of the given size. u may be NULL which causes the contents to be undefined. It is the user’s responsibility to fill in the needed data. The buffer is copied into the new object.

If the buffer is not NULL, the return value might be a shared object. Therefore, modification of the resulting Unicode object is only allowed when u is NULL.

If the buffer is NULL, PyUnicode\_READY() must be called once the string content has been filled before using any of the access macros such as PyUnicode\_KIND().

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Unicode API, please migrate to using PyUnicode\_FromKindAndData(), PyUnicode\_FromWideChar(), or PyUnicode\_New().

## Py\_UNICODE \*PyUnicode\_AsUnicode(PyObject \*unicode)

Return a read-only pointer to the Unicode object’s internal Py\_UNICODE buffer, or NULL on error. This will create the Py\_UNICODE\* representation of the object if it is not yet available. The buffer is always terminated with an extra null code point. Note that the resulting Py\_UNICODE string may also contain embedded null code points, which would cause the string to be truncated when used in most C functions.

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Unicode API, please migrate to using PyUnicode\_AsUCS4(), PyUnicode\_AsWideChar(), PyUnicode\_ReadChar() or similar new APIs.

## PyObject \*PyUnicode\_TransformDecimalToASCII(Py\_UNICODE \*s, Py\_ssize\_t size)

Return value: New reference. Create a Unicode object by replacing all decimal digits in Py\_UNICODE buffer of the given size by ASCII digits 0–9 according to their decimal value. Return NULL if an exception occurs.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using Py\_UNICODE\_TODECIMAL().

## Py\_UNICODE \*PyUnicode\_AsUnicodeAndSize(PyObject \*unicode, Py\_ssize\_t \*size)

Like PyUnicode\_AsUnicode(), but also saves the Py\_UNICODE() array length (excluding the extra null terminator) in size. Note that the resulting Py\_UNICODE\* string may contain embedded null code points, which would cause the string to be truncated when used in most C functions.

New in version 3.3.

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Unicode API, please migrate to using PyUnicode\_AsUCS4(), PyUnicode\_AsWideChar(), PyUnicode\_ReadChar() or similar new APIs.

## Py\_ssize\_t PyUnicode\_GetSize(PyObject \*unicode)

Part of the Stable ABI. Return the size of the deprecated Py\_UNICODE representation, in code units (this includes surrogate pairs as 2 units).

Deprecated since version 3.3, will be removed in version 3.12: Part of the old-style Unicode API, please migrate to using PyUnicode\_GET\_LENGTH().

## PyObject \*PyUnicode\_FromObject(PyObject \*obj)

Return value: New reference. Part of the Stable ABI. Copy an instance of a Unicode subtype to a new true Unicode object if necessary. If obj is already a true Unicode object (not a subtype), return the reference with incremented refcount.

Objects other than Unicode or its subtypes will cause a TypeError.

## Locale Encoding

The current locale encoding can be used to decode text from the operating system.

PyObject \***PyUnicode\_DecodeLocaleAndSize**(**const** char \*str, Py\_ssize\_t len, **const** char \*er-

Return value: New reference. Part of the Stable ABI since version 3.7. Decode a string from UTF-8 on Android and VxWorks, or from the current locale encoding on other platforms. The supported error handlers are "strict" and "surrogateescape" ([**PEP 383**](https://www.python.org/dev/peps/pep-0383)). The decoder uses "strict" error handler if errors is NULL. str must end with a null character but cannot contain embedded null characters.

Use PyUnicode\_DecodeFSDefaultAndSize() to decode string from Py\_FileSystemDefaultEncoding (the locale encoding read at Python startup).

This function ignores the Python UTF-8 Mode.

## See also:

The Py\_DecodeLocale() function.

New in version 3.3.

Changed in version 3.7: The function now also uses the current locale encoding for the surrogateescape error handler, except on Android. Previously, Py\_DecodeLocale() was used for the surrogateescape, and the current locale encoding was used for strict.

## PyObject \*PyUnicode\_DecodeLocale(const char \*str, const char \*errors)

Return value: New reference. Part of the Stable ABI since version 3.7. Similar to PyUnicode\_DecodeLocaleAndSize(), but compute the string length using strlen().

New in version 3.3.

## PyObject \*PyUnicode\_EncodeLocale(PyObject \*unicode, const char \*errors)

Return value: New reference. Part of the Stable ABI since version 3.7. Encode a Unicode object to UTF-8 on Android and VxWorks, or to the current locale encoding on other platforms. The supported error handlers are "strict" and "surrogateescape" ([**PEP 383**](https://www.python.org/dev/peps/pep-0383)). The encoder uses "strict" error handler if errors is NULL. Return a bytes object. unicode cannot contain embedded null characters.

Use PyUnicode\_EncodeFSDefault() to encode a string to Py\_FileSystemDefaultEncoding (the locale encoding read at Python startup).

This function ignores the Python UTF-8 Mode.

## See also:

The Py\_EncodeLocale() function.

New in version 3.3.

Changed in version 3.7: The function now also uses the current locale encoding for the surrogateescape error handler, except on Android. Previously, Py\_EncodeLocale() was used for the surrogateescape, and the current locale encoding was used for strict.

## File System Encoding

To encode and decode file names and other environment strings, Py\_FileSystemDefaultEncoding should be used as the encoding, and Py\_FileSystemDefaultEncodeErrors should be used as the error handler ([**PEP 383**](https://www.python.org/dev/peps/pep-0383) and [**PEP 529**](https://www.python.org/dev/peps/pep-0529)). To encode file names to bytes during argument parsing, the "O&" converter should be used, passing PyUnicode\_FSConverter() as the conversion function:

## int PyUnicode\_FSConverter(PyObject \*obj, void \*result)

Part of the Stable ABI. ParseTuple converter: encode str objects – obtained directly or through the os. PathLike interface – to bytes using PyUnicode\_EncodeFSDefault(); bytes objects are output as-is. result must be a PyBytesObject\* which must be released when it is no longer used.

New in version 3.1.

Changed in version 3.6: Accepts a path-like object.

To decode file names to str during argument parsing, the "O&" converter should be used, passing PyUnicode\_FSDecoder() as the conversion function:

## int PyUnicode\_FSDecoder(PyObject \*obj, void \*result)

Part of the Stable ABI. ParseTuple converter: decode bytes objects – obtained either directly or indirectly through the os.PathLike interface – to str using PyUnicode\_DecodeFSDefaultAndSize(); str objects are output as-is. result must be a PyUnicodeObject\* which must be released when it is no longer used.

New in version 3.2.

Changed in version 3.6: Accepts a path-like object.

## PyObject \*PyUnicode\_DecodeFSDefaultAndSize(const char \*s, Py\_ssize\_t size)

Return value: New reference. Part of the Stable ABI. Decode a string from the filesystem encoding and error handler.

If Py\_FileSystemDefaultEncoding is not set, fall back to the locale encoding.

Py\_FileSystemDefaultEncoding is initialized at startup from the locale encoding and cannot be modified later. If you need to decode a string from the current locale encoding, use PyUnicode\_DecodeLocaleAndSize().

## See also:

The Py\_DecodeLocale() function.

Changed in version 3.6: Use Py\_FileSystemDefaultEncodeErrors error handler.

## PyObject \*PyUnicode\_DecodeFSDefault(const char \*s)

Return value: New reference. Part of the Stable ABI. Decode a null-terminated string from the filesystem encoding and error handler.

If Py\_FileSystemDefaultEncoding is not set, fall back to the locale encoding.

Use PyUnicode\_DecodeFSDefaultAndSize() if you know the string length.

Changed in version 3.6: Use Py\_FileSystemDefaultEncodeErrors error handler.

## PyObject \*PyUnicode\_EncodeFSDefault(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object to Py\_FileSystemDefaultEncoding with the Py\_FileSystemDefaultEncodeErrors error handler, and return bytes. Note that the resulting bytes object may contain null bytes.

If Py\_FileSystemDefaultEncoding is not set, fall back to the locale encoding.

Py\_FileSystemDefaultEncoding is initialized at startup from the locale encoding and cannot be modified later. If you need to encode a string to the current locale encoding, use PyUnicode\_EncodeLocale().

## See also:

The Py\_EncodeLocale() function.

New in version 3.2.

Changed in version 3.6: Use Py\_FileSystemDefaultEncodeErrors error handler.

## wchar\_t Support

wchar\_t support for platforms which support it:

## PyObject \*PyUnicode\_FromWideChar(const wchar\_t \*w, Py\_ssize\_t size)

Return value: New reference. Part of the Stable ABI. Create a Unicode object from the wchar\_t buffer w of the given size. Passing -1 as the size indicates that the function must itself compute the length, using wcslen. Return NULL on failure.

## Py\_ssize\_t PyUnicode\_AsWideChar(PyObject \*unicode, wchar\_t \*w, Py\_ssize\_t size)

Part of the Stable ABI. Copy the Unicode object contents into the wchar\_t buffer w. At most size wchar\_t characters are copied (excluding a possibly trailing null termination character). Return the number of wchar\_t characters copied or -1 in case of an error. Note that the resulting wchar\_t\* string may or may not be null-terminated. It is the responsibility of the caller to make sure that the wchar\_t\* string is null-terminated in case this is required by the application. Also, note that the wchar\_t\* string might contain null characters, which would cause the string to be truncated when used with most C functions.

## wchar\_t \*PyUnicode\_AsWideCharString(PyObject \*unicode, Py\_ssize\_t \*size)

Part of the Stable ABI since version 3.7. Convert the Unicode object to a wide character string. The output string always ends with a null character. If size is not NULL, write the number of wide characters (excluding the trailing null termination character) into \*size. Note that the resulting wchar\_t string might contain null characters, which would cause the string to be truncated when used with most C functions. If size is NULL and the wchar\_t\* string contains null characters a ValueError is raised.

Returns a buffer allocated by PyMem\_Alloc() (use PyMem\_Free() to free it) on success. On error, returns NULL and \*size is undefined. Raises a MemoryError if memory allocation is failed.

New in version 3.2.

Changed in version 3.7: Raises a ValueError if size is NULL and the wchar\_t\* string contains null characters.

## Built-in Codecs

Python provides a set of built-in codecs which are written in C for speed. All of these codecs are directly usable via the following functions.

Many of the following APIs take two arguments encoding and errors, and they have the same semantics as the ones of the built-in str() string object constructor.

Setting encoding to NULL causes the default encoding to be used which is UTF-8. The file system calls should use PyUnicode\_FSConverter() for encoding file names. This uses the variable Py\_FileSystemDefaultEncoding internally. This variable should be treated as read-only: on some systems, it will be a pointer to a static string, on others, it will change at run-time (such as when the application invokes setlocale).

Error handling is set by errors which may also be set to NULL meaning to use the default handling defined for the codec. Default error handling for all built-in codecs is “strict” (ValueError is raised).

The codecs all use a similar interface. Only deviations from the following generic ones are documented for simplicity.

## Generic Codecs

These are the generic codec APIs:

PyObject \***PyUnicode\_Decode**(**const** char \*s, Py\_ssize\_t size, **const** char \*encoding, **const** char

\*errors)

Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the encoded string s. encoding and errors have the same meaning as the parameters of the same name in the str() built-in function. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_AsEncodedString**(PyObject \*unicode, **const** char \*encoding, **const** char

\*errors)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object and return the result as Python bytes object. encoding and errors have the same meaning as the parameters of the same name in the Unicode encode() method. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_Encode**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, **const** char \*encoding,

**const** char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer s of the given size and return a Python bytes object. encoding and errors have the same meaning as the parameters of the same name in the Unicode encode() method. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsEncodedString().

## UTF-8 Codecs

These are the UTF-8 codec APIs:

PyObject \***PyUnicode\_DecodeUTF8**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the UTF-8 encoded string s. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_DecodeUTF8Stateful**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors,

Py\_ssize\_t \*consumed)

Return value: New reference. Part of the Stable ABI. If consumed is NULL, behave like PyUnicode\_DecodeUTF8(). If consumed is not NULL, trailing incomplete UTF-8 byte sequences will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

PyObject \***PyUnicode\_AsUTF8String**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object using UTF-8 and return the result as Python bytes object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

**const** char \***PyUnicode\_AsUTF8AndSize**(PyObject \*unicode, Py\_ssize\_t \*size)

Part of the Stable ABI since version 3.10. Return a pointer to the UTF-8 encoding of the Unicode object, and store the size of the encoded representation (in bytes) in size. The size argument can be NULL; in this case no size will be stored. The returned buffer always has an extra null byte appended (not included in size), regardless of whether there are any other null code points.

In the case of an error, NULL is returned with an exception set and no size is stored.

This caches the UTF-8 representation of the string in the Unicode object, and subsequent calls will return a pointer to the same buffer. The caller is not responsible for deallocating the buffer. The buffer is deallocated and pointers to it become invalid when the Unicode object is garbage collected.

New in version 3.3.

Changed in version 3.7: The return type is now const char \* rather of char \*.

Changed in version 3.10: This function is a part of the limited API.

**const** char \***PyUnicode\_AsUTF8**(PyObject \*unicode)

As PyUnicode\_AsUTF8AndSize(), but does not store the size.

New in version 3.3.

Changed in version 3.7: The return type is now const char \* rather of char \*.

PyObject \***PyUnicode\_EncodeUTF8**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer s of the given size using UTF-8 and return a Python bytes object. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsUTF8String(), PyUnicode\_AsUTF8AndSize() or PyUnicode\_AsEncodedString().

## UTF-32 Codecs

These are the UTF-32 codec APIs:

PyObject \***PyUnicode\_DecodeUTF32**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors, int \*byte-

Return value: New reference. Part of the Stable ABI. Decode size bytes from a UTF-32 encoded buffer string and return the corresponding Unicode object. errors (if non-NULL) defines the error handling. It defaults to “strict”.

If byteorder is non-NULL, the decoder starts decoding using the given byte order:

```txt
*byteorder == -1: little endian
*byteorder == 0: native order
*byteorder == 1: big endian
```

If \*byteorder is zero, and the first four bytes of the input data are a byte order mark (BOM), the decoder switches to this byte order and the BOM is not copied into the resulting Unicode string. If \*byteorder is -1 or 1, any byte order mark is copied to the output.

After completion, \*byteorder is set to the current byte order at the end of input data.

If byteorder is NULL, the codec starts in native order mode.

Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_DecodeUTF32Stateful**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors,

y eor onsumed) Return value: New reference. Part of the Stable ABI. If consumed is NULL, behave like PyUnicode\_DecodeUTF32(). If consumed is not NULL, PyUnicode\_DecodeUTF32Stateful() will not treat trailing incomplete UTF-32 byte sequences (such as a number of bytes not divisible by four) as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

PyObject \***PyUnicode\_AsUTF32String**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Return a Python byte string using the UTF-32 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_EncodeUTF32**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, **const** char \*errors,

Return value: New reference. Return a Python bytes object holding the UTF-32 encoded value of the Unicode data in s. Output is written according to the following byte order:

```txt
byteorder == -1: little endian
byteorder == 0: native byte order (writes a BOM mark)
byteorder == 1: big endian
```

If byteorder is 0, the output string will always start with the Unicode BOM mark (U+FEFF). In the other two modes, no BOM mark is prepended.

If Py\_UNICODE\_WIDE is not defined, surrogate pairs will be output as a single code point.

Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsUTF32String() or PyUnicode\_AsEncodedString().

## UTF-16 Codecs

These are the UTF-16 codec APIs:

PyObject \***PyUnicode\_DecodeUTF16**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors, int \*byte-

Return value: New reference. Part of the Stable ABI. Decode size bytes from a UTF-16 encoded buffer string and return the corresponding Unicode object. errors (if non-NULL) defines the error handling. It defaults to “strict”.

If byteorder is non-NULL, the decoder starts decoding using the given byte order:

```txt
*byteorder == -1: little endian
*byteorder == 0: native order
*byteorder == 1: big endian
```

If \*byteorder is zero, and the first two bytes of the input data are a byte order mark (BOM), the decoder switches to this byte order and the BOM is not copied into the resulting Unicode string. If \*byteorder is -1 or 1, any byte order mark is copied to the output (where it will result in either a \ufeff or a \ufffe character).

After completion, \*byteorder is set to the current byte order at the end of input data.

If byteorder is NULL, the codec starts in native order mode.

Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_DecodeUTF16Stateful**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors,

Return value: New reference. Part of the Stable ABI. If consumed is NULL, behave like PyUnicode\_DecodeUTF16(). If consumed is not NULL, PyUnicode\_DecodeUTF16Stateful() will not treat trailing incomplete UTF-16 byte sequences (such as an odd number of bytes or a split surrogate pair) as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

PyObject \***PyUnicode\_AsUTF16String**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Return a Python byte string using the UTF-16 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_EncodeUTF16**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, **const** char \*errors,

Return value: New reference. Return a Python bytes object holding the UTF-16 encoded value of the Unicode data in s. Output is written according to the following byte order:

```txt
byteorder == -1: little endian
byteorder == 0: native byte order (writes a BOM mark)
byteorder == 1: big endian
```

If byteorder is 0, the output string will always start with the Unicode BOM mark (U+FEFF). In the other two modes, no BOM mark is prepended.

If Py\_UNICODE\_WIDE is defined, a single Py\_UNICODE value may get represented as a surrogate pair. If it is not defined, each Py\_UNICODE values is interpreted as a UCS-2 character.

Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsUTF16String() or PyUnicode\_AsEncodedString().

## UTF-7 Codecs

These are the UTF-7 codec APIs:

PyObject \***PyUnicode\_DecodeUTF7**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the UTF-7 encoded string s. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_DecodeUTF7Stateful**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors,

Py\_ssize\_t \*consumed)

Return value: New reference. Part of the Stable ABI. If consumed is NULL, behave like PyUnicode\_DecodeUTF7(). If consumed is not NULL, trailing incomplete UTF-7 base-64 sections will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

PyObject \***PyUnicode\_EncodeUTF7**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, int base64SetO, int

base64WhiteSpace, **const** char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using UTF-7 and return a Python bytes object. Return NULL if an exception was raised by the codec.

If base64SetO is nonzero, “Set O” (punctuation that has no otherwise special meaning) will be encoded in base-64. If base64WhiteSpace is nonzero, whitespace will be encoded in base-64. Both are set to zero for the Python “utf-7” codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsEncodedString().

## Unicode-Escape Codecs

These are the “Unicode Escape” codec APIs:

PyObject \***PyUnicode\_DecodeUnicodeEscape**(**const** char \*s, Py\_ssize\_t size, **const** char \*er-

rors)

Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the Unicode-Escape encoded string s. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_AsUnicodeEscapeString**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object using Unicode-Escape and return the result as a bytes object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_EncodeUnicodeEscape**(**const** Py\_UNICODE \*s, Py\_ssize\_t size)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using Unicode-Escape and return a bytes object. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsUnicodeEscapeString().

## Raw-Unicode-Escape Codecs

These are the “Raw Unicode Escape” codec APIs:

PyObject \***PyUnicode\_DecodeRawUnicodeEscape**(**const** char \*s, Py\_ssize\_t size, **const** char

Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the Raw-Unicode-Escape encoded string s. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_AsRawUnicodeEscapeString**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object using Raw-Unicode-Escape and return the result as a bytes object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_EncodeRawUnicodeEscape**(**const** Py\_UNICODE \*s, Py\_ssize\_t size)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using Raw-Unicode-Escape and return a bytes object. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsRawUnicodeEscapeString() or PyUnicode\_AsEncodedString().

## Latin-1 Codecs

These are the Latin-1 codec APIs: Latin-1 corresponds to the first 256 Unicode ordinals and only these are accepted by the codecs during encoding.

PyObject \***PyUnicode\_DecodeLatin1**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the Latin-1 encoded string s. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_AsLatin1String**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object using Latin-1 and return the result as Python bytes object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_EncodeLatin1**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using Latin-1 and return a Python bytes object. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsLatin1String() or PyUnicode\_AsEncodedString().

## ASCII Codecs

These are the ASCII codec APIs. Only 7-bit ASCII data is accepted. All other codes generate errors.

PyObject \***PyUnicode\_DecodeASCII**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors) Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the ASCII encoded string s. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_AsASCIIString**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object using ASCII and return the result as Python bytes object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_EncodeASCII**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using ASCII and return a Python bytes object. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsASCIIString() or PyUnicode\_AsEncodedString().

## Character Map Codecs

This codec is special in that it can be used to implement many different codecs (and this is in fact what was done to obtain most of the standard codecs included in the encodings package). The codec uses mappings to encode and decode characters. The mapping objects provided must support the \_\_getitem\_\_() mapping interface; dictionaries and sequences work well.

These are the mapping codec APIs:

PyObject \***PyUnicode\_DecodeCharmap**(**const** char \*data, Py\_ssize\_t size, PyObject \*mapping,

**const** char \*errors)

Return value: New reference. Part of the Stable ABI. Create a Unicode object by decoding size bytes of the encoded string s using the given mapping object. Return NULL if an exception was raised by the codec.

If mapping is NULL, Latin-1 decoding will be applied. Else mapping must map bytes ordinals (integers in the range from 0 to 255) to Unicode strings, integers (which are then interpreted as Unicode ordinals) or None. Unmapped data bytes – ones which cause a LookupError, as well as ones which get mapped to None, 0xFFFE or '\ufffe', are treated as undefined mappings and cause an error.

PyObject \***PyUnicode\_AsCharmapString**(PyObject \*unicode, PyObject \*mapping)

Return value: New reference. Part of the Stable ABI. Encode a Unicode object using the given mapping object and return the result as a bytes object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

The mapping object must map Unicode ordinal integers to bytes objects, integers in the range from 0 to 255 or None. Unmapped character ordinals (ones which cause a LookupError) as well as mapped to None are treated as “undefined mapping” and cause an error.

PyObject \***PyUnicode\_EncodeCharmap**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, PyObject \*mapping,

**const** char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using the given mapping object and return the result as a bytes object. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsCharmapString() or PyUnicode\_AsEncodedString().

The following codec API is special in that maps Unicode to Unicode.

PyObject \***PyUnicode\_Translate**(PyObject \*str, PyObject \*table, **const** char \*errors)

Return value: New reference. Part of the Stable ABI. Translate a string by applying a character mapping table to it and return the resulting Unicode object. Return NULL if an exception was raised by the codec.

The mapping table must map Unicode ordinal integers to Unicode ordinal integers or None (causing deletion of the character).

Mapping tables need only provide the \_\_getitem\_\_() interface; dictionaries and sequences work well. Unmapped character ordinals (ones which cause a LookupError) are left untouched and are copied as-is.

errors has the usual meaning for codecs. It may be NULL which indicates to use the default error handling.

PyObject \***PyUnicode\_TranslateCharmap**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, PyObject

\*mapping, **const** char \*errors)

Return value: New reference. Translate a Py\_UNICODE buffer of the given size by applying a character mapping table to it and return the resulting Unicode object. Return NULL when an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 3.11: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_Translate(). or generic codec based API

## MBCS codecs for Windows

These are the MBCS codec APIs. They are currently only available on Windows and use the Win32 MBCS converters to implement the conversions. Note that MBCS (or DBCS) is a class of encodings, not just one. The target encoding is defined by the user settings on the machine running the codec.

PyObject \***PyUnicode\_DecodeMBCS**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Part of the Stable ABI on Windows since version 3.7. Create a Unicode object by decoding size bytes of the MBCS encoded string s. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_DecodeMBCSStateful**(**const** char \*s, Py\_ssize\_t size, **const** char \*errors,

Py\_ssize\_t \*consumed)

Return value: New reference. Part of the Stable ABI on Windows since version 3.7. If consumed is NULL, behave like PyUnicode\_DecodeMBCS(). If consumed is not NULL, PyUnicode\_DecodeMBCSStateful() will not decode trailing lead byte and the number of bytes that have been decoded will be stored in consumed.

PyObject \***PyUnicode\_AsMBCSString**(PyObject \*unicode)

Return value: New reference. Part of the Stable ABI on Windows since version 3.7. Encode a Unicode object using MBCS and return the result as Python bytes object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

PyObject \***PyUnicode\_EncodeCodePage**(int code\_page, PyObject \*unicode, **const** char \*errors)

Return value: New reference. Part of the Stable ABI on Windows since version 3.7. Encode the Unicode object using the specified code page and return a Python bytes object. Return NULL if an exception was raised by the codec. Use CP\_ACP code page to get the MBCS encoder.

New in version 3.3.

PyObject \***PyUnicode\_EncodeMBCS**(**const** Py\_UNICODE \*s, Py\_ssize\_t size, **const** char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using MBCS and return a Python bytes object. Return NULL if an exception was raised by the codec.

Deprecated since version 3.3, will be removed in version 4.0: Part of the old-style Py\_UNICODE API; please migrate to using PyUnicode\_AsMBCSString(), PyUnicode\_EncodeCodePage() or PyUnicode\_AsEncodedString().

## Methods & Slots

## Methods and Slot Functions

The following APIs are capable of handling Unicode objects and strings on input (we refer to them as strings in the descriptions) and return Unicode objects or integers as appropriate.

They all return NULL or -1 if an exception occurs.

PyObject \***PyUnicode\_Concat**(PyObject \*left, PyObject \*right)

Return value: New reference. Part of the Stable ABI. Concat two strings giving a new Unicode string.

PyObject \***PyUnicode\_Split**(PyObject \*s, PyObject \*sep, Py\_ssize\_t maxsplit)

Return value: New reference. Part of the Stable ABI. Split a string giving a list of Unicode strings. If sep is NULL, splitting will be done at all whitespace substrings. Otherwise, splits occur at the given separator. At most maxsplit splits will be done. If negative, no limit is set. Separators are not included in the resulting list.

PyObject \***PyUnicode\_Splitlines**(PyObject \*s, int keepend)

Return value: New reference. Part of the Stable ABI. Split a Unicode string at line breaks, returning a list of Unicode strings. CRLF is considered to be one line break. If keepend is 0, the line break characters are not included in the resulting strings.

PyObject \***PyUnicode\_Join**(PyObject \*separator, PyObject \*seq)

Return value: New reference. Part of the Stable ABI. Join a sequence of strings using the given separator and return the resulting Unicode string.

Py\_ssize\_t **PyUnicode\_Tailmatch**(PyObject \*str, PyObject \*substr, Py\_ssize\_t start, Py\_ssize\_t end, int direction)

Part of the Stable ABI. Return 1 if substr matches str[start:end] at the given tail end (direction == -1 means to do a prefix match, direction == 1 a suffix match), 0 otherwise. Return -1 if an error occurred.

## Py\_ssize\_t PyUnicode\_Find(PyObject \*str, PyObject \*substr, Py\_ssize\_t start, Py\_ssize\_t end, int direction)

Part of the Stable ABI. Return the first position of substr in str[start:end] using the given direction (direction == 1 means to do a forward search, direction == -1 a backward search). The return value is the index of the first match; a value of -1 indicates that no match was found, and -2 indicates that an error occurred and an exception has been set.

## Py\_ssize\_t PyUnicode\_FindChar(PyObject \*str, Py\_UCS4 ch, Py\_ssize\_t start, Py\_ssize\_t end, int direc-

Part of the Stable ABI since version 3.7. Return the first position of the character ch in str[start:end] using the given direction (direction == 1 means to do a forward search, direction == -1 a backward search). The return value is the index of the first match; a value of -1 indicates that no match was found, and -2 indicates that an error occurred and an exception has been set.

New in version 3.3.

Changed in version 3.7: start and end are now adjusted to behave like str[start:end].

## Py\_ssize\_t PyUnicode\_Count(PyObject \*str, PyObject \*substr, Py\_ssize\_t start, Py\_ssize\_t end)

Part of the Stable ABI. Return the number of non-overlapping occurrences of substr in str[start:end]. Return -1 if an error occurred.

## PyObject \*PyUnicode\_Replace(PyObject \*str, PyObject \*substr, PyObject \*replstr, Py\_ssize\_t max-

Return value: New reference. Part of the Stable ABI. Replace at most maxcount occurrences of substr in str with replstr and return the resulting Unicode object. maxcount == -1 means replace all occurrences.

## int PyUnicode\_Compare(PyObject \*left, PyObject \*right)

Part of the Stable ABI. Compare two strings and return -1, 0, 1 for less than, equal, and greater than, respectively.

This function returns -1 upon failure, so one should call PyErr\_Occurred() to check for errors.

## int PyUnicode\_CompareWithASCIIString(PyObject \*uni, const char \*string)

Part of the Stable ABI. Compare a Unicode object, uni, with string and return -1, 0, 1 for less than, equal, and greater than, respectively. It is best to pass only ASCII-encoded strings, but the function interprets the input string as ISO-8859-1 if it contains non-ASCII characters.

This function does not raise exceptions.

## PyObject \*PyUnicode\_RichCompare(PyObject \*left, PyObject \*right, int op)

Return value: New reference. Part of the Stable ABI. Rich compare two Unicode strings and return one of the following:

• NULL in case an exception was raised

• Py\_True or Py\_False for successful comparisons

• Py\_NotImplemented in case the type combination is unknown

Possible values for op are Py\_GT, Py\_GE, Py\_EQ, Py\_NE, Py\_LT, and Py\_LE.

## PyObject \*PyUnicode\_Format(PyObject \*format, PyObject \*args)

Return value: New reference. Part of the Stable ABI. Return a new string object from format and args; this is analogous to format % args.

## int PyUnicode\_Contains(PyObject \*container, PyObject \*element)

Part of the Stable ABI. Check whether element is contained in container and return true or false accordingly.

element has to coerce to a one element Unicode string. -1 is returned if there was an error.

## void PyUnicode\_InternInPlace(PyObject \*\*string)

Part of the Stable ABI. Intern the argument \*string in place. The argument must be the address of a pointer variable pointing to a Python Unicode string object. If there is an existing interned string that is the same as

\*string, it sets \*string to it (releasing the reference to the old string object and creating a new strong reference to the interned string object), otherwise it leaves \*string alone and interns it (creating a new strong reference). (Clarification: even though there is a lot of talk about references, think of this function as reference-neutral; you own the object after the call if and only if you owned it before the call.)

## PyObject \*PyUnicode\_InternFromString(const char \*v)

Return value: New reference. Part of the Stable ABI. A combination of PyUnicode\_FromString() and PyUnicode\_InternInPlace(), returning either a new Unicode string object that has been interned, or a new (“owned”) reference to an earlier interned string object with the same value.

## 8.3.4 Tuple Objects

## type PyTupleObject

This subtype of PyObject represents a Python tuple object.

PyTypeObject **PyTuple\_Type** Part of the Stable ABI. This instance of PyTypeObject represents the Python tuple type; it is the same object as tuple in the Python layer.

## int PyTuple\_Check(PyObject \*p)

Return true if p is a tuple object or an instance of a subtype of the tuple type. This function always succeeds.

## int PyTuple\_CheckExact(PyObject \*p)

Return true if p is a tuple object, but not an instance of a subtype of the tuple type. This function always succeeds.

## PyObject \*PyTuple\_New(Py\_ssize\_t len)

Return value: New reference. Part of the Stable ABI. Return a new tuple object of size len, or NULL on failure.

## PyObject \*PyTuple\_Pack(Py\_ssize\_t n, ...)

Return value: New reference. Part of the Stable ABI. Return a new tuple object of size n, or NULL on failure. The tuple values are initialized to the subsequent n C arguments pointing to Python objects. PyTuple\_Pack(2, a, b) is equivalent to Py\_BuildValue("(OO)", a, b).

## Py\_ssize\_t PyTuple\_Size(PyObject \*p)

Part of the Stable ABI. Take a pointer to a tuple object, and return the size of that tuple.

## Py\_ssize\_t PyTuple\_GET\_SIZE(PyObject \*p)

Return the size of the tuple p, which must be non-NULL and point to a tuple; no error checking is performed.

PyObject \***PyTuple\_GetItem**(PyObject \*p, Py\_ssize\_t pos) Return value: Borrowed reference. Part of the Stable ABI. Return the object at position pos in the tuple pointed to by p. If pos is negative or out of bounds, return NULL and set an IndexError exception.

PyObject \***PyTuple\_GET\_ITEM**(PyObject \*p, Py\_ssize\_t pos) Return value: Borrowed reference. Like PyTuple\_GetItem(), but does no checking of its arguments.

PyObject \***PyTuple\_GetSlice**(PyObject \*p, Py\_ssize\_t low, Py\_ssize\_t high) Return value: New reference. Part of the Stable ABI. Return the slice of the tuple pointed to by p between low and high, or NULL on failure. This is the equivalent of the Python expression p[low:high]. Indexing from the end of the list is not supported.

## int PyTuple\_SetItem(PyObject \*p, Py\_ssize\_t pos, PyObject \*o)

Part of the Stable ABI. Insert a reference to object o at position pos of the tuple pointed to by p. Return 0 on success. If pos is out of bounds, return -1 and set an IndexError exception.

**Note:** This function “steals” a reference to o and discards a reference to an item already in the tuple at the affected position.

void **PyTuple\_SET\_ITEM**(PyObject \*p, Py\_ssize\_t pos, PyObject \*o) Like PyTuple\_SetItem(), but does no error checking, and should only be used to fill in brand new tuples.

**Note:** This macro “steals” a reference to o, and, unlike PyTuple\_SetItem(), does not discard a reference to any item that is being replaced; any reference in the tuple at position pos will be leaked.

## int \_PyTuple\_Resize(PyObject \*\*p, Py\_ssize\_t newsize)

Can be used to resize a tuple. newsize will be the new length of the tuple. Because tuples are supposed to be immutable, this should only be used if there is only one reference to the object. Do not use this if the tuple may already be known to some other part of the code. The tuple will always grow or shrink at the end. Think of this as destroying the old tuple and creating a new one, only more efficiently. Returns 0 on success. Client code should never assume that the resulting value of \*p will be the same as before calling this function. If the object referenced by \*p is replaced, the original \*p is destroyed. On failure, returns -1 and sets \*p to NULL, and raises MemoryError or SystemError.

## 8.3.5 Struct Sequence Objects

Struct sequence objects are the C equivalent of namedtuple() objects, i.e. a sequence whose items can also be accessed through attributes. To create a struct sequence, you first have to create a specific struct sequence type.

## PyTypeObject \*PyStructSequence\_NewType(PyStructSequence\_Desc \*desc)

Return value: New reference. Part of the Stable ABI. Create a new struct sequence type from the data in desc, described below. Instances of the resulting type can be created with PyStructSequence\_New().

void **PyStructSequence\_InitType**(PyTypeObject \*type, PyStructSequence\_Desc \*desc) Initializes a struct sequence type type from desc in place.

int **PyStructSequence\_InitType2**(PyTypeObject \*type, PyStructSequence\_Desc \*desc) The same as PyStructSequence\_InitType, but returns 0 on success and -1 on failure.

New in version 3.4.

## type PyStructSequence\_Desc

Part of the Stable ABI (including all members). Contains the meta information of a struct sequence type to create.

| Field | C Type | Meaning |
| --- | --- | --- |
| name | const char * | name of the struct sequence type |
| doc | const char * | pointer to docstring for the type or NULL to omit |
| fields | PyStructSequence_Fie* | ldpointer to NULL-terminated array with field names of the new type |
| n_in_sequenc | eint | number of fields visible to the Python side (if used as tuple) |

## type PyStructSequence\_Field

Part of the Stable ABI (including all members). Describes a field of a struct sequence. As a struct sequence is modeled as a tuple, all fields are typed as PyObject\*. The index in the fields array of the PyStructSequence\_Desc determines which field of the struct sequence is described.

| Field | C Type | Meaning |
| --- | --- | --- |
| name | constchar * | name for the field or NULL to end the list of named fields, set toPyStructSequence_UnnamedField to leave unnamed |
| doc | constchar * | field docstring or NULL to omit |

## const char \*const PyStructSequence\_UnnamedField

Special value for a field name to leave it unnamed.

Changed in version 3.9: The type was changed from char \*.

```txt
Py_ssize_t PyList_GET_SIZE (PyObject *list)
txt
PyObject *PyList_GET_ITEM(PyObject *list, Py_ssize_t i)
    Return value: Borrowed reference. Macro form of PyList_GetItem() without error checking.
txt
type PylistObject
    This subtype of PyObject represents a Python list object.

PyTypeObject PyList_Type
    Part of the Stable ABI. This instance of PyTypeObject represents the Python list type. This is the same object as list in the Python layer.

int PyList_Check(PyObject *p)
    Return true if p is a list object or an instance of a subtype of the list type. This function always succeeds.

int PyList_CheckExact(PyObject *p)
    Return true if p is a list object, but not an instance of a subtype of the list type. This function always succeeds.

PyObject *PyList_New(Py_ssize_t len)
    Return value: New reference. Part of the Stable ABI. Return a new list of length len on success, or NULL on failure.
```

PyObject \***PyStructSequence\_New**(PyTypeObject \*type) Return value: New reference. Part of the Stable ABI. Creates an instance of type, which must have been created with PyStructSequence\_NewType().

void **PyStructSequence\_SetItem**(PyObject \*p, Py\_ssize\_t pos, PyObject \*o) Part of the Stable ABI. Sets the field at index pos of the struct sequence p to value o. Like PyTuple\_SET\_ITEM(), this should only be used to fill in brand new instances.

void **PyStructSequence\_SET\_ITEM**(PyObject \*p, Py\_ssize\_t \*pos, PyObject \*o) Macro equivalent of PyStructSequence\_SetItem().

```txt
Note: This function “steals” a reference to o.
```

## 8.3.6 List Objects

**Note:** If len is greater than zero, the returned list object’s items are set to NULL. Thus you cannot use abstract API functions such as PySequence\_SetItem() or expose the object to Python code before setting all items to a real object with PyList\_SetItem().

Py\_ssize\_t **PyList\_Size**(PyObject \*list) Part of the Stable ABI. Return the length of the list object in list; this is equivalent to len(list) on a list object.

PyObject \***PyList\_GetItem**(PyObject \*list, Py\_ssize\_t index) Return value: Borrowed reference. Part of the Stable ABI. Return the object at position index in the list pointed to by list. The position must be non-negative; indexing from the end of the list is not supported. If index is out of bounds (<0 or >=len(list)), return NULL and set an IndexError exception.

int **PyList\_SetItem**(PyObject \*list, Py\_ssize\_t index, PyObject \*item) Part of the Stable ABI. Set the item at index index in list to item. Return 0 on success. If index is out of bounds, return -1 and set an IndexError exception.

**Note:** This function “steals” a reference to item and discards a reference to an item already in the list at the affected position.

void **PyList\_SET\_ITEM**(PyObject \*list, Py\_ssize\_t i, PyObject \*o) Macro form of PyList\_SetItem() without error checking. This is normally only used to fill in new lists where there is no previous content.

**Note:** This macro “steals” a reference to item, and, unlike PyList\_SetItem(), does not discard a reference to any item that is being replaced; any reference in list at position i will be leaked.

## int PyList\_Insert(PyObject \*list, Py\_ssize\_t index, PyObject \*item)

Part of the Stable ABI. Insert the item item into list list in front of index index. Return 0 if successful; return -1 and set an exception if unsuccessful. Analogous to list.insert(index, item).

## int PyList\_Append(PyObject \*list, PyObject \*item)

Part of the Stable ABI. Append the object item at the end of list list. Return 0 if successful; return -1 and set an exception if unsuccessful. Analogous to list.append(item).

## PyObject \*PyList\_GetSlice(PyObject \*list, Py\_ssize\_t low, Py\_ssize\_t high)

Return value: New reference. Part of the Stable ABI. Return a list of the objects in list containing the objects between low and high. Return NULL and set an exception if unsuccessful. Analogous to list[low:high]. Indexing from the end of the list is not supported.

## int PyList\_SetSlice(PyObject \*list, Py\_ssize\_t low, Py\_ssize\_t high, PyObject \*itemlist)

Part of the Stable ABI. Set the slice of list between low and high to the contents of itemlist. Analogous to list[low:high] = itemlist. The itemlist may be NULL, indicating the assignment of an empty list (slice deletion). Return 0 on success, -1 on failure. Indexing from the end of the list is not supported.

## int PyList\_Sort(PyObject \*list)

Part of the Stable ABI. Sort the items of list in place. Return 0 on success, -1 on failure. This is equivalent to list.sort().

## int PyList\_Reverse(PyObject \*list)

Part of the Stable ABI. Reverse the items of list in place. Return 0 on success, -1 on failure. This is the equivalent of list.reverse().

PyObject \***PyList\_AsTuple**(PyObject \*list) Return value: New reference. Part of the Stable ABI. Return a new tuple object containing the contents of list; equivalent to tuple(list).

## 8.4 Container Objects

## 8.4.1 Dictionary Objects

## type PyDictObject

This subtype of PyObject represents a Python dictionary object.

## PyTypeObject PyDict\_Type

Part of the Stable ABI. This instance of PyTypeObject represents the Python dictionary type. This is the same object as dict in the Python layer.

## int PyDict\_Check(PyObject \*p)

Return true if p is a dict object or an instance of a subtype of the dict type. This function always succeeds.

Note that exceptions which occur while calling \_\_hash\_\_() and \_\_eq\_\_() methods and creating a temporary string object will get suppressed. To get error reporting use PyDict\_GetItemWithError() instead.

int PyDict\_CheckExact(PyObject \*p) Return true if p is a dict object, but not an instance of a subtype of the dict type. This function always succeeds.

PyObject \*PyDictProxy\_New(PyObject \*mapping) Return value: New reference. Part of the Stable ABI. Return a types.MappingProxyType object for a mapping which enforces read-only behavior. This is normally used to create a view to prevent modification of the dictionary for non-dynamic class types.

void PyDict\_Clear(PyObject \*p) Part of the Stable ABI. Empty an existing dictionary of all key-value pairs.

int PyDict\_Contains(PyObject \*p, PyObject \*key) Part of the Stable ABI. Determine if dictionary p contains key. If an item in p is matches key, return 1, otherwise return 0. On error, return -1. This is equivalent to the Python expression key in p.

PyObject \*PyDict\_Copy(PyObject \*p) Return value: New reference. Part of the Stable ABI. Return a new dictionary that contains the same key-value pairs as p.

int PyDict\_SetItem(PyObject \*p, PyObject \*key, PyObject \*val) Part of the Stable ABI. Insert val into the dictionary p with a key of key. key must be hashable; if it isn’t, TypeError will be raised. Return 0 on success or -1 on failure. This function does not steal a reference to val.

int PyDict\_SetItemString(PyObject \*p, const char \*key, PyObject \*val) Part of the Stable ABI. Insert val into the dictionary p using key as a key. key should be a const char\*. The key object is created using PyUnicode\_FromString(key). Return 0 on success or -1 on failure. This function does not steal a reference to val.

int PyDict\_DelItem(PyObject \*p, PyObject \*key) Part of the Stable ABI. Remove the entry in dictionary p with key key. key must be hashable; if it isn’t, TypeError is raised. If key is not in the dictionary, KeyError is raised. Return 0 on success or -1 on failure.

int PyDict\_DelItemString(PyObject \*p, const char \*key) Part of the Stable ABI. Remove the entry in dictionary p which has a key specified by the string key. If key is not in the dictionary, KeyError is raised. Return 0 on success or -1 on failure.

PyObject \*PyDict\_GetItem(PyObject \*p, PyObject \*key) Return value: Borrowed reference. Part of the Stable ABI. Return the object from dictionary p which has a key key. Return NULL if the key key is not present, but without setting an exception.

PyObject \*PyDict\_GetItemWithError(PyObject \*p, PyObject \*key) Return value: Borrowed reference. Part of the Stable ABI. Variant of PyDict\_GetItem() that does not suppress exceptions. Return NULL with an exception set if an exception occurred. Return NULL without an exception set if the key wasn’t present.

PyObject \*PyDict\_GetItemString(PyObject \*p, const char \*key) Return value: Borrowed reference. Part of the Stable ABI. This is the same as PyDict\_GetItem(), but key is specified as a const char\*, rather than a PyObject\*.

PyObject \*PyDict\_SetDefault(PyObject \*p, PyObject \*key, PyObject \*defaultobj) Return value: Borrowed reference. This is the same as the Python-level dict.setdefault(). If present,

it returns the value corresponding to key from the dictionary p. If the key is not in the dict, it is inserted with value defaultobj and defaultobj is returned. This function evaluates the hash function of key only once, instead of evaluating it independently for the lookup and the insertion.

New in version 3.4.

PyObject \***PyDict\_Items**(PyObject \*p) Return value: New reference. Part of the Stable ABI. Return a PyListObject containing all the items from the dictionary.

PyObject \***PyDict\_Keys**(PyObject \*p) Return value: New reference. Part of the Stable ABI. Return a PyListObject containing all the keys from the dictionary.

PyObject \***PyDict\_Values**(PyObject \*p) Return value: New reference. Part of the Stable ABI. Return a PyListObject containing all the values from the dictionary p.

## Py\_ssize\_t PyDict\_Size(PyObject \*p)

Part of the Stable ABI. Return the number of items in the dictionary. This is equivalent to len(p) on a dictionary.

## int PyDict\_Next(PyObject \*p, Py\_ssize\_t \*ppos, PyObject \*\*pkey, PyObject \*\*pvalue)

Part of the Stable ABI. Iterate over all key-value pairs in the dictionary p. The Py\_ssize\_t referred to by ppos must be initialized to 0 prior to the first call to this function to start the iteration; the function returns true for each pair in the dictionary, and false once all pairs have been reported. The parameters pkey and pvalue should either point to PyObject\* variables that will be filled in with each key and value, respectively, or may be NULL. Any references returned through them are borrowed. ppos should not be altered during iteration. Its value represents offsets within the internal dictionary structure, and since the structure is sparse, the offsets are not consecutive.

For example:

```c
PyObject *key, *value;
Py_ssize_t pos = 0;

while (PyDict_Next(self->dict, &pos, &key, &value)) {
    /* do something interesting with the values... */
}
```

The dictionary p should not be mutated during iteration. It is safe to modify the values of the keys as you iterate over the dictionary, but only so long as the set of keys does not change. For example:

```c
PyObject *key, *value;
Py_ssize_t pos = 0;

while (PyDict_Next(self->dict, &pos, &key, &value)) {
    long i = PyLong_AsLong(value);
    if (i == -1 && PyErr_Occurred()) {
        return -1;
    }
    PyObject *o = PyLong_FromLong(i + 1);
    if (o == NULL)
        return -1;
    if (PyDict_SetItem(self->dict, key, o) < 0) {
        Py_DECREF(o);
        return -1;
    }
    Py_DECREF(o);
}
```

int **PyDict\_Merge**(PyObject \*a, PyObject \*b, int override)

Part of the Stable ABI. Iterate over mapping object b adding key-value pairs to dictionary a. b may be a

dictionary, or any object supporting PyMapping\_Keys() and PyObject\_GetItem(). If override is true, existing pairs in a will be replaced if a matching key is found in b, otherwise pairs will only be added if there is not a matching key in a. Return 0 on success or -1 if an exception was raised.

## int PyDict\_Update(PyObject \*a, PyObject \*b)

Part of the Stable ABI. This is the same as PyDict\_Merge(a, b, 1) in C, and is similar to a. update(b) in Python except that PyDict\_Update() doesn’t fall back to the iterating over a sequence of key value pairs if the second argument has no “keys” attribute. Return 0 on success or -1 if an exception was raised.

## int PyDict\_MergeFromSeq2(PyObject \*a, PyObject \*seq2, int override)

Part of the Stable ABI. Update or merge into dictionary a, from the key-value pairs in seq2. seq2 must be an iterable object producing iterable objects of length 2, viewed as key-value pairs. In case of duplicate keys, the last wins if override is true, else the first wins. Return 0 on success or -1 if an exception was raised. Equivalent Python (except for the return value):

```python
def PyDict_MergeFromSeq2(a, seq2, override):
    for key, value in seq2:
        if override or key not in a:
            a[key] = value
```

## 8.4.2 Set Objects

This section details the public API for set and frozenset objects. Any functionality not listed below is best accessed using either the abstract object protocol (including PyObject\_CallMethod(), PyObject\_RichCompareBool(), PyObject\_Hash(), PyObject\_Repr(), PyObject\_IsTrue(), PyObject\_Print(), and PyObject\_GetIter()) or the abstract number protocol (including PyNumber\_And(), PyNumber\_Subtract(), PyNumber\_Or(), PyNumber\_Xor(), PyNumber\_InPlaceAnd(), PyNumber\_InPlaceSubtract(), PyNumber\_InPlaceOr(), and PyNumber\_InPlaceXor()).

## type PySetObject

This subtype of PyObject is used to hold the internal data for both set and frozenset objects. It is like a PyDictObject in that it is a fixed size for small sets (much like tuple storage) and will point to a separate, variable sized block of memory for medium and large sized sets (much like list storage). None of the fields of this structure should be considered public and all are subject to change. All access should be done through the documented API rather than by manipulating the values in the structure.

## PyTypeObject PySet\_Type

Part of the Stable ABI. This is an instance of PyTypeObject representing the Python set type.

## PyTypeObject PyFrozenSet\_Type

Part of the Stable ABI. This is an instance of PyTypeObject representing the Python frozenset type.

The following type check macros work on pointers to any Python object. Likewise, the constructor functions work with any iterable Python object.

## int PySet\_Check(PyObject \*p)

Return true if p is a set object or an instance of a subtype. This function always succeeds.

## int PyFrozenSet\_Check(PyObject \*p)

Return true if p is a frozenset object or an instance of a subtype. This function always succeeds.

## int PyAnySet\_Check(PyObject \*p)

Return true if p is a set object, a frozenset object, or an instance of a subtype. This function always succeeds.

## int PySet\_CheckExact(PyObject \*p)

Return true if p is a set object but not an instance of a subtype. This function always succeeds.

New in version 3.10.

int **PyAnySet\_CheckExact**(PyObject \*p) Return true if p is a set object or a frozenset object but not an instance of a subtype. This function always succeeds.

int **PyFrozenSet\_CheckExact**(PyObject \*p) Return true if p is a frozenset object but not an instance of a subtype. This function always succeeds.

PyObject \***PySet\_New**(PyObject \*iterable) Return value: New reference. Part of the Stable ABI. Return a new set containing objects returned by the iterable. The iterable may be NULL to create a new empty set. Return the new set on success or NULL on failure. Raise TypeError if iterable is not actually iterable. The constructor is also useful for copying a set (c=set(s)).

PyObject \***PyFrozenSet\_New**(PyObject \*iterable) Return value: New reference. Part of the Stable ABI. Return a new frozenset containing objects returned by the iterable. The iterable may be NULL to create a new empty frozenset. Return the new set on success or NULL on failure. Raise TypeError if iterable is not actually iterable.

The following functions and macros are available for instances of set or frozenset or instances of their subtypes.

Py\_ssize\_t **PySet\_Size**(PyObject \*anyset) Part of the Stable ABI. Return the length of a set or frozenset object. Equivalent to len(anyset). Raises a PyExc\_SystemError if anyset is not a set, frozenset, or an instance of a subtype.

Py\_ssize\_t **PySet\_GET\_SIZE**(PyObject \*anyset) Macro form of PySet\_Size() without error checking.

nt **PySet\_Contains**(PyObject \*anyset, PyObject \*key) Part of the Stable ABI. Return 1 if found, 0 if not found, and -1 if an error is encountered. Unlike the Python contains\_\_() method, this function does not automatically convert unhashable sets into temporary frozensets. Raise a TypeError if the key is unhashable. Raise PyExc\_SystemError if anyset is not a set, frozenset, or an instance of a subtype.

nt **PySet\_Add**(PyObject \*set, PyObject \*key) Part of the Stable ABI. Add key to a set instance. Also works with frozenset instances (like PyTuple\_SetItem() it can be used to fill in the values of brand new frozensets before they are exposed to other code). Return 0 on success or -1 on failure. Raise a TypeError if the key is unhashable. Raise a MemoryError if there is no room to grow. Raise a SystemError if set is not an instance of set or its subtype.

The following functions are available for instances of set or its subtypes but not for instances of frozenset or its subtypes.

int **PySet\_Discard**(PyObject \*set, PyObject \*key) Part of the Stable ABI. Return 1 if found and removed, 0 if not found (no action taken), and -1 if an error is encountered. Does not raise KeyError for missing keys. Raise a TypeError if the key is unhashable. Unlike the Python discard() method, this function does not automatically convert unhashable sets into temporary frozensets. Raise PyExc\_SystemError if set is not an instance of set or its subtype.

PyObject \***PySet\_Pop**(PyObject \*set) Return value: New reference. Part of the Stable ABI. Return a new reference to an arbitrary object in the set, and removes the object from the set. Return NULL on failure. Raise KeyError if the set is empty. Raise a SystemError if set is not an instance of set or its subtype.

int **PySet\_Clear**(PyObject \*set) Part of the Stable ABI. Empty an existing set of all elements.

## 8.5 Function Objects

## 8.5.1 Function Objects

There are a few functions specific to Python functions.

## type PyFunctionObject

The C structure used for functions.

## PyTypeObject PyFunction\_Type

This is an instance of PyTypeObject and represents the Python function type. It is exposed to Python programmers as types.FunctionType.

## int PyFunction\_Check(PyObject \*o)

Return true if o is a function object (has type PyFunction\_Type). The parameter must not be NULL. This function always succeeds.

## PyObject \*PyFunction\_New(PyObject \*code, PyObject \*globals)

Return value: New reference. Return a new function object associated with the code object code. globals must be a dictionary with the global variables accessible to the function.

The function’s docstring and name are retrieved from the code object. \_\_module\_\_ is retrieved from globals. The argument defaults, annotations and closure are set to NULL. \_\_qualname\_\_ is set to the same value as the function’s name.

## PyObject \*PyFunction\_NewWithQualName(PyObject \*code, PyObject \*globals, PyObject \*qualname)

Return value: New reference. As PyFunction\_New(), but also allows setting the function object’s qualname\_\_ attribute. qualname should be a unicode object or NULL; if NULL, the \_\_qualname attribute is set to the same value as its \_\_name\_\_ attribute.

New in version 3.3.

## PyObject \*PyFunction\_GetCode(PyObject \*op)

Return value: Borrowed reference. Return the code object associated with the function object op.

## PyObject \*PyFunction\_GetGlobals(PyObject \*op)

Return value: Borrowed reference. Return the globals dictionary associated with the function object op.

## PyObject \*PyFunction\_GetModule(PyObject \*op)

Return value: Borrowed reference. Return a borrowed reference to the \_\_module\_\_ attribute of the function object op. It can be NULL.

This is normally a string containing the module name, but can be set to any other object by Python code.

## PyObject \*PyFunction\_GetDefaults(PyObject \*op)

Return value: Borrowed reference. Return the argument default values of the function object op. This can be a tuple of arguments or NULL.

## int PyFunction\_SetDefaults(PyObject \*op, PyObject \*defaults)

Set the argument default values for the function object op. defaults must be Py\_None or a tuple.

Raises SystemError and returns -1 on failure.

## PyObject \*PyFunction\_GetClosure(PyObject \*op)

Return value: Borrowed reference. Return the closure associated with the function object op. This can be NULL or a tuple of cell objects.

## int PyFunction\_SetClosure(PyObject \*op, PyObject \*closure)

Set the closure associated with the function object op. closure must be Py\_None or a tuple of cell objects.

Raises SystemError and returns -1 on failure.

## PyObject \*PyFunction\_GetAnnotations(PyObject \*op)

Return value: Borrowed reference. Return the annotations of the function object op. This can be a mutable dictionary or NULL.

## int PyFunction\_SetAnnotations(PyObject \*op, PyObject \*annotations)

Set the annotations for the function object op. annotations must be a dictionary or Py\_None.

Raises SystemError and returns -1 on failure.

## 8.5.2 Instance Method Objects

An instance method is a wrapper for a PyCFunction and the new way to bind a PyCFunction to a class object. It replaces the former call PyMethod\_New(func, NULL, class).

## PyTypeObject PyInstanceMethod\_Type

This instance of PyTypeObject represents the Python instance method type. It is not exposed to Python programs.

## int PyInstanceMethod\_Check(PyObject \*o)

Return true if o is an instance method object (has type PyInstanceMethod\_Type). The parameter must not be NULL. This function always succeeds.

## PyObject \*PyInstanceMethod\_New(PyObject \*func)

Return value: New reference. Return a new instance method object, with func being any callable object. func is the function that will be called when the instance method is called.

## PyObject \*PyInstanceMethod\_Function(PyObject \*im)

Return value: Borrowed reference. Return the function object associated with the instance method im.

## PyObject \*PyInstanceMethod\_GET\_FUNCTION(PyObject \*im)

Return value: Borrowed reference. Macro version of PyInstanceMethod\_Function() which avoids error checking.

## 8.5.3 Method Objects

Methods are bound function objects. Methods are always bound to an instance of a user-defined class. Unbound methods (methods bound to a class object) are no longer available.

## PyTypeObject PyMethod\_Type

This instance of PyTypeObject represents the Python method type. This is exposed to Python programs as types.MethodType.

## int PyMethod\_Check(PyObject \*o)

Return true if o is a method object (has type PyMethod\_Type). The parameter must not be NULL. This function always succeeds.

## PyObject \*PyMethod\_New(PyObject \*func, PyObject \*self)

Return value: New reference. Return a new method object, with func being any callable object and self the instance the method should be bound. func is the function that will be called when the method is called. self must not be NULL.

## PyObject \*PyMethod\_Function(PyObject \*meth)

Return value: Borrowed reference. Return the function object associated with the method meth.

## PyObject \*PyMethod\_GET\_FUNCTION(PyObject \*meth)

Return value: Borrowed reference. Macro version of PyMethod\_Function() which avoids error checking.

## PyObject \*PyMethod\_Self(PyObject \*meth)

Return value: Borrowed reference. Return the instance associated with the method meth.

PyObject \***PyMethod\_GET\_SELF**(PyObject \*meth) Return value: Borrowed reference. Macro version of PyMethod\_Self() which avoids error checking.

## 8.5.4 Cell Objects

“Cell” objects are used to implement variables referenced by multiple scopes. For each such variable, a cell object is created to store the value; the local variables of each stack frame that references the value contains a reference to the cells from outer scopes which also use that variable. When the value is accessed, the value contained in the cell is used instead of the cell object itself. This de-referencing of the cell object requires support from the generated byte-code; these are not automatically de-referenced when accessed. Cell objects are not likely to be useful elsewhere.

**type PyCellObject**

The C structure used for cell objects.

PyTypeObject **PyCell\_Type**

The type object corresponding to cell objects.

int **PyCell\_Check**(ob)

Return true if ob is a cell object; ob must not be NULL. This function always succeeds.

PyObject \***PyCell\_New**(PyObject \*ob)

Return value: New reference. Create and return a new cell object containing the value ob. The parameter may be NULL.

PyObject \***PyCell\_Get**(PyObject \*cell)

Return value: New reference. Return the contents of the cell cell.

PyObject \***PyCell\_GET**(PyObject \*cell)

Return value: Borrowed reference. Return the contents of the cell cell, but without checking that cell is non-NULL and a cell object.

int **PyCell\_Set**(PyObject \*cell, PyObject \*value)

Set the contents of the cell object cell to value. This releases the reference to any current content of the cell. value may be NULL. cell must be non-NULL; if it is not a cell object, -1 will be returned. On success, 0 will be returned.

void **PyCell\_SET**(PyObject \*cell, PyObject \*value)

Sets the value of the cell object cell to value. No reference counts are adjusted, and no checks are made for safety; cell must be non-NULL and must be a cell object.

## 8.5.5 Code Objects

Code objects are a low-level detail of the CPython implementation. Each one represents a chunk of executable code that hasn’t yet been bound into a function.

**type PyCodeObject**

The C structure of the objects used to describe code objects. The fields of this type are subject to change at any time.

PyTypeObject **PyCode\_Type**

This is an instance of PyTypeObject representing the Python code type.

int **PyCode\_Check**(PyObject \*co)

Return true if co is a code object. This function always succeeds.

int **PyCode\_GetNumFree**(PyCodeObject \*co)

Return the number of free variables in co.

PyCodeObject \***PyCode\_New**(int argcount, int kwonlyargcount, int nlocals, int stacksize, int flags, PyObjec \*code, PyObject \*consts, PyObject \*names, PyObject \*varnames, PyObject \*freevars, PyObject \*cellvars, PyObject \*filename, PyObject \*name, int firstlineno, PyObject \*lnotab)

Return value: New reference. Return a new code object. If you need a dummy code object to create a frame, use PyCode\_NewEmpty() instead. Calling PyCode\_New() directly can bind you to a precise Python version since the definition of the bytecode changes often.

PyCodeObject \***PyCode\_NewWithPosOnlyArgs**(int argcount, int posonlyargcount, int kwonlyargcount, int nlocals, int stacksize, int flags, PyObject \*code, PyObject \*consts, PyObject \*names, PyObject \*varnames, PyObject \*freevars, PyObject \*cellvars, PyObject \*filename, PyObject \*name, int firstlineno, PyObject \*lnotab)

Return value: New reference. Similar to PyCode\_New(), but with an extra “posonlyargcount” for positionalonly arguments.

New in version 3.8.

PyCodeObject \***PyCode\_NewEmpty**(**const** char \*filename, **const** char \*funcname, int firstlineno)

Return value: New reference. Return a new empty code object with the specified filename, function name, and first line number. It is illegal to exec() or eval() the resulting code object.

int **PyCode\_Addr2Line**(PyCodeObject \*co, int byte\_offset)

Return the line number of the instruction that occurs on or before byte\_offset and ends after it. If you just need the line number of a frame, use PyFrame\_GetLineNumber() instead.

For efficiently iterating over the line numbers in a code object, use [the API described in PEP 626](https://www.python.org/dev/peps/pep-0626/#out-of-process-debuggers-and-profilers).

## 8.6 Other Objects

## 8.6.1 File Objects

These APIs are a minimal emulation of the Python 2 C API for built-in file objects, which used to rely on the buffered I/O (FILE\*) support from the C standard library. In Python 3, files and streams use the new io module, which defines several layers over the low-level unbuffered I/O of the operating system. The functions described below are convenience C wrappers over these new APIs, and meant mostly for internal error reporting in the interpreter; third-party code is advised to access the io APIs instead.

PyObject \***PyFile\_FromFd**(int fd, **const** char \*name, **const** char \*mode, int buffering, **const** char

\*encoding, **const** char \*errors, **const** char \*newline, int closefd)

Return value: New reference. Part of the Stable ABI. Create a Python file object from the file descriptor of an already opened file fd. The arguments name, encoding, errors and newline can be NULL to use the defaults; buffering can be -1 to use the default. name is ignored and kept for backward compatibility. Return NULL on failure. For a more comprehensive description of the arguments, please refer to the io.open() function documentation.

**Warning:** Since Python streams have their own buffering layer, mixing them with OS-level file descriptors can produce various issues (such as unexpected ordering of data).

Changed in version 3.2: Ignore name attribute.

int **PyObject\_AsFileDescriptor**(PyObject \*p)

Part of the Stable ABI. Return the file descriptor associated with p as an int. If the object is an integer, its value is returned. If not, the object’s fileno() method is called if it exists; the method must return an integer, which is returned as the file descriptor value. Sets an exception and returns -1 on failure.

PyObject \***PyFile\_GetLine**(PyObject \*p, int n)

Return value: New reference. Part of the Stable ABI. Equivalent to p.readline([n]), this function reads one line from the object p. p may be a file object or any object with a readline() method. If n is 0, exactly one line is read, regardless of the length of the line. If n is greater than 0, no more than n bytes will be read from the file; a partial line can be returned. In both cases, an empty string is returned if the end of the file is reached immediately. If n is less than 0, however, one line is read regardless of length, but EOFError is raised if the end of the file is reached immediately.

int **PyFile\_SetOpenCodeHook**(Py\_OpenCodeHookFunction handler)

Overrides the normal behavior of io.open\_code() to pass its parameter through the provided handler.

The handler is a function of type PyObject \*(\*)PyObject \*path, void \*userData, where path is guaranteed to be PyUnicodeObject.

The userData pointer is passed into the hook function. Since hook functions may be called from different runtimes, this pointer should not refer directly to Python state.

As this hook is intentionally used during import, avoid importing new modules during its execution unless they are known to be frozen or available in sys.modules.

Once a hook has been set, it cannot be removed or replaced, and later calls to PyFile\_SetOpenCodeHook() will fail. On failure, the function returns -1 and sets an exception if the interpreter has been initialized.

This function is safe to call before Py\_Initialize().

Raises an auditing event setopencodehook with no arguments.

New in version 3.8.

## int PyFile\_WriteObject(PyObject \*obj, PyObject \*p, int flags)

Part of the Stable ABI. Write object obj to file object p. The only supported flag for flags is Py\_PRINT\_RAW; if given, the str() of the object is written instead of the repr(). Return 0 on success or -1 on failure; the appropriate exception will be set.

## int PyFile\_WriteString(const char \*s, PyObject \*p)

Part of the Stable ABI. Write string s to file object p. Return 0 on success or -1 on failure; the appropriate exception will be set.

## 8.6.2 Module Objects

## PyTypeObject PyModule\_Type

Part of the Stable ABI. This instance of PyTypeObject represents the Python module type. This is exposed to Python programs as types.ModuleType.

## int PyModule\_Check(PyObject \*p)

Return true if p is a module object, or a subtype of a module object. This function always succeeds.

## int PyModule\_CheckExact(PyObject \*p)

Return true if p is a module object, but not a subtype of PyModule\_Type. This function always succeeds.

## PyObject \*PyModule\_NewObject(PyObject \*name)

Return value: New reference. Part of the Stable ABI since version 3.7. Return a new module object with the \_\_name\_\_ attribute set to name. The module’s \_\_name\_\_, \_\_doc\_\_, \_\_package\_\_, and loader\_\_ attributes are filled in (all but \_\_name\_\_ are set to None); the caller is responsible for providing a \_\_file\_\_ attribute.

New in version 3.3.

Changed in version 3.4: \_\_package\_\_ and \_\_loader\_\_ are set to None.

## PyObject \*PyModule\_New(const char \*name)

Return value: New reference. Part of the Stable ABI. Similar to PyModule\_NewObject(), but the name is a UTF-8 encoded string instead of a Unicode object.

## PyObject \*PyModule\_GetDict(PyObject \*module)

Return value: Borrowed reference. Part of the Stable ABI. Return the dictionary object that implements module’s namespace; this object is the same as the \_\_dict\_\_ attribute of the module object. If module is not a module object (or a subtype of a module object), SystemError is raised and NULL is returned.

It is recommended extensions use other PyModule\_\* and PyObject\_\* functions rather than directly manipulate a module’s \_\_dict\_\_.

## PyObject \*PyModule\_GetNameObject(PyObject \*module)

Return value: New reference. Part of the Stable ABI since version 3.7. Return module’s \_\_name\_\_ value. If the module does not provide one, or if it is not a string, SystemError is raised and NULL is returned.

New in version 3.3.

**const** char \***PyModule\_GetName**(PyObject \*module) Part of the Stable ABI. Similar to PyModule\_GetNameObject() but return the name encoded to 'utf-8'.

## void \*PyModule\_GetState(PyObject \*module)

Part of the Stable ABI. Return the “state” of the module, that is, a pointer to the block of memory allocated at module creation time, or NULL. See PyModuleDef.m\_size.

## PyModuleDef \*PyModule\_GetDef(PyObject \*module)

Part of the Stable ABI. Return a pointer to the PyModuleDef struct from which the module was created, or NULL if the module wasn’t created from a definition.

## PyObject \*PyModule\_GetFilenameObject(PyObject \*module)

Return value: New reference. Part of the Stable ABI. Return the name of the file from which module was loaded using module’s \_\_file\_\_ attribute. If this is not defined, or if it is not a unicode string, raise SystemError and return NULL; otherwise return a reference to a Unicode object.

New in version 3.2.

## const char \*PyModule\_GetFilename(PyObject \*module)

Part of the Stable ABI. Similar to PyModule\_GetFilenameObject() but return the filename encoded to ‘utf-8’.

Deprecated since version 3.2: PyModule\_GetFilename() raises UnicodeEncodeError on unencodable filenames, use PyModule\_GetFilenameObject() instead.

## Initializing C modules

Modules objects are usually created from extension modules (shared libraries which export an initialization function), or compiled-in modules (where the initialization function is added using PyImport\_AppendInittab()). See building or extending-with-embedding for details.

The initialization function can either pass a module definition instance to PyModule\_Create(), and return the resulting module object, or request “multi-phase initialization” by returning the definition struct itself.

## type PyModuleDef

Part of the Stable ABI (including all members). The module definition struct, which holds all information needed to create a module object. There is usually only one statically initialized variable of this type for each module.

## PyModuleDef\_Base m\_base

Always initialize this member to PyModuleDef\_HEAD\_INIT.

**const** char \***m\_name**

Name for the new module.

## const char \*m\_doc

Docstring for the module; usually a docstring variable created with PyDoc\_STRVAR is used.

## Py\_ssize\_t m\_size

Module state may be kept in a per-module memory area that can be retrieved with PyModule\_GetState(), rather than in static globals. This makes modules safe for use in multiple sub-interpreters.

This memory area is allocated based on m\_size on module creation, and freed when the module object is deallocated, after the m\_free function has been called, if present.

Setting m\_size to -1 means that the module does not support sub-interpreters, because it has global state.

Setting it to a non-negative value means that the module can be re-initialized and specifies the additional amount of memory it requires for its state. Non-negative m\_size is required for multi-phase initialization.

See [**PEP 3121**](https://www.python.org/dev/peps/pep-3121) for more details.

## PyMethodDef \*m\_methods

A pointer to a table of module-level functions, described by PyMethodDef values. Can be NULL if no functions are present.

## PyModuleDef\_Slot \*m\_slots

An array of slot definitions for multi-phase initialization, terminated by a {0, NULL} entry. When using single-phase initialization, m\_slots must be NULL.

Changed in version 3.5: Prior to version 3.5, this member was always set to NULL, and was defined as:

## inquiry m\_reload

## traverseproc m\_traverse

A traversal function to call during GC traversal of the module object, or NULL if not needed.

This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed (Py\_mod\_exec function). More precisely, this function is not called if m\_size is greater than 0 and the module state (as returned by PyModule\_GetState()) is NULL.

Changed in version 3.9: No longer called before the module state is allocated.

## inquiry m\_clear

A clear function to call during GC clearing of the module object, or NULL if not needed.

This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed (Py\_mod\_exec function). More precisely, this function is not called if m\_size is greater than 0 and the module state (as returned by PyModule\_GetState()) is NULL.

Like PyTypeObject.tp\_clear, this function is not always called before a module is deallocated. For example, when reference counting is enough to determine that an object is no longer used, the cyclic garbage collector is not involved and m\_free is called directly.

Changed in version 3.9: No longer called before the module state is allocated.

## freefunc m\_free

A function to call during deallocation of the module object, or NULL if not needed.

This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed (Py\_mod\_exec function). More precisely, this function is not called if m\_size is greater than 0 and the module state (as returned by PyModule\_GetState()) is NULL.

Changed in version 3.9: No longer called before the module state is allocated.

## Single-phase initialization

The module initialization function may create and return the module object directly. This is referred to as “singlephase initialization”, and uses one of the following two module creation functions:

## PyObject \*PyModule\_Create(PyModuleDef \*def)

Return value: New reference. Create a new module object, given the definition in def. This behaves like PyModule\_Create2() with module\_api\_version set to PYTHON\_API\_VERSION.

## PyObject \*PyModule\_Create2(PyModuleDef \*def, int module\_api\_version)

Return value: New reference. Part of the Stable ABI. Create a new module object, given the definition in def, assuming the API version module\_api\_version. If that version does not match the version of the running interpreter, a RuntimeWarning is emitted.

**Note:** Most uses of this function should be using PyModule\_Create() instead; only use this if you are sure you need it.

Before it is returned from in the initialization function, the resulting module object is typically populated using functions like PyModule\_AddObjectRef().

## Multi-phase initialization

An alternate way to specify extensions is to request “multi-phase initialization”. Extension modules created this way behave more like Python modules: the initialization is split between the creation phase, when the module object is created, and the execution phase, when it is populated. The distinction is similar to the \_\_new\_\_() and \_init\_\_() methods of classes.

Unlike modules created using single-phase initialization, these modules are not singletons: if the sys.modules entry is removed and the module is re-imported, a new module object is created, and the old module is subject to normal garbage collection – as with Python modules. By default, multiple modules created from the same definition should be independent: changes to one should not affect the others. This means that all state should be specific to the module object (using e.g. using PyModule\_GetState()), or its contents (such as the module’s \_\_dict\_\_ or individual classes created with PyType\_FromSpec()).

All modules created using multi-phase initialization are expected to support sub-interpreters. Making sure multiple modules are independent is typically enough to achieve this.

To request multi-phase initialization, the initialization function (PyInit\_modulename) returns a PyModuleDef instance with non-empty m\_slots. Before it is returned, the PyModuleDef instance must be initialized with the following function:

## PyObject \*PyModuleDef\_Init(PyModuleDef \*def)

Return value: Borrowed reference. Part of the Stable ABI since version 3.5. Ensures a module definition is a properly initialized Python object that correctly reports its type and reference count.

Returns def cast to PyObject\*, or NULL if an error occurred.

New in version 3.5.

The m\_slots member of the module definition must point to an array of PyModuleDef\_Slot structures:

**type PyModuleDef\_Slot**

int **slot**

A slot ID, chosen from the available values explained below.

void \***value**

Value of the slot, whose meaning depends on the slot ID.

New in version 3.5.

The m\_slots array must be terminated by a slot with id 0.

The available slot types are:

## Py\_mod\_create

Specifies a function that is called to create the module object itself. The value pointer of this slot must point to a function of the signature:

PyObject \***create\_module**(PyObject \*spec, PyModuleDef \*def)

The function receives a ModuleSpec instance, as defined in [**PEP 451**](https://www.python.org/dev/peps/pep-0451), and the module definition. It should return a new module object, or set an error and return NULL.

This function should be kept minimal. In particular, it should not call arbitrary Python code, as trying to import the same module again may result in an infinite loop.

Multiple Py\_mod\_create slots may not be specified in one module definition.

If Py\_mod\_create is not specified, the import machinery will create a normal module object using PyModule\_New(). The name is taken from spec, not the definition, to allow extension modules to dynamically adjust to their place in the module hierarchy and be imported under different names through symlinks, all while sharing a single module definition.

There is no requirement for the returned object to be an instance of PyModule\_Type. Any type can be used, as long as it supports setting and getting import-related attributes. However, only PyModule\_Type instances may be returned if the PyModuleDef has non-NULL m\_traverse, m\_clear, m\_free; non-zero m\_size; or slots other than Py\_mod\_create.

## Py\_mod\_exec

Specifies a function that is called to execute the module. This is equivalent to executing the code of a Python module: typically, this function adds classes and constants to the module. The signature of the function is:

int **exec\_module**(PyObject \*module)

If multiple Py\_mod\_exec slots are specified, they are processed in the order they appear in the m\_slots array. See [**PEP 489**](https://www.python.org/dev/peps/pep-0489) for more details on multi-phase initialization.

## Low-level module creation functions

The following functions are called under the hood when using multi-phase initialization. They can be used directly, for example when creating module objects dynamically. Note that both PyModule\_FromDefAndSpec and PyModule\_ExecDef must be called to fully initialize a module.

PyObject \***PyModule\_FromDefAndSpec**(PyModuleDef \*def, PyObject \*spec)

Return value: New reference. Create a new module object, given the definition in def and the ModuleSpec spec. This behaves like PyModule\_FromDefAndSpec2() with module\_api\_version set to PYTHON\_API\_VERSION.

New in version 3.5.

PyObject \***PyModule\_FromDefAndSpec2**(PyModuleDef \*def, PyObject \*spec, int module\_api\_version)

Return value: New reference. Part of the Stable ABI since version 3.7. Create a new module object, given the definition in def and the ModuleSpec spec, assuming the API version module\_api\_version. If that version does not match the version of the running interpreter, a RuntimeWarning is emitted.

**Note:** Most uses of this function should be using PyModule\_FromDefAndSpec() instead; only use this if you are sure you need it.

New in version 3.5.

int **PyModule\_ExecDef**(PyObject \*module, PyModuleDef \*def) Part of the Stable ABI since version 3.7. Process any execution slots (Py\_mod\_exec) given in def.

New in version 3.5.

int **PyModule\_SetDocString**(PyObject \*module, **const** char \*docstring) Part of the Stable ABI since version 3.7. Set the docstring for module to docstring. This function is called automatically when creating a module from PyModuleDef, using either PyModule\_Create or PyModule\_FromDefAndSpec.

New in version 3.5.

int **PyModule\_AddFunctions**(PyObject \*module, PyMethodDef \*functions) Part of the Stable ABI since version 3.7. Add the functions from the NULL terminated functions array to module. Refer to the PyMethodDef documentation for details on individual entries (due to the lack of a shared module namespace, module level “functions” implemented in C typically receive the module as their first parameter, making them similar to instance methods on Python classes). This function is called automatically when creating a module from PyModuleDef, using either PyModule\_Create or PyModule\_FromDefAndSpec.

New in version 3.5.

## Support functions

The module initialization function (if using single phase initialization) or a function called from a module execution slot (if using multi-phase initialization), can use the following functions to help initialize the module state:

int **PyModule\_AddObjectRef**(PyObject \*module, **const** char \*name, PyObject \*value)

Part of the Stable ABI since version 3.10. Add an object to module as name. This is a convenience function which can be used from the module’s initialization function.

On success, return 0. On error, raise an exception and return -1.

Return NULL if value is NULL. It must be called with an exception raised in this case.

Example usage:

```c
static int
add_spam(PyObject *module, int value)
{
    PyObject *obj = PyLong_FromLong(value);
    if (obj == NULL) {
        return -1;
    }
    int res = PyModule_AddObjectRef(module, "spam", obj);
    Py_DECREF(obj);
    return res;
}
```

The example can also be written without checking explicitly if obj is NULL:

```c
static int
add_spam(PyObject *module, int value)
{
    PyObject *obj = PyLong_FromLong(value);
    int res = PyModule_AddObjectRef(module, "spam", obj);
    Py_XDEcref(obj);
    return res;
}
```

Note that Py\_XDECREF() should be used instead of Py\_DECREF() in this case, since obj can be NULL.

New in version 3.10.

int **PyModule\_AddObject**(PyObject \*module, **const** char \*name, PyObject \*value)

Part of the Stable ABI. Similar to PyModule\_AddObjectRef(), but steals a reference to value on success (if it returns 0).

The new PyModule\_AddObjectRef() function is recommended, since it is easy to introduce reference leaks by misusing the PyModule\_AddObject() function.

**Note:** Unlike other functions that steal references, PyModule\_AddObject() only releases the reference to value **on success**.

This means that its return value must be checked, and calling code must Py\_DECREF() value manually on error.

Example usage:

```txt
static int
add_spam(PyObject *module, int value)
{
```

(continues on next page)

(continued from previous page)

```c
PyObject *obj = PyLong_FromLong(value);
if (obj == NULL) {
    return -1;
}
if (PyModule_AddObject(module, "spam", obj) < 0) {
    Py_DECREF(obj);
    return -1;
}
// PyModule_AddObject() stole a reference to obj:
// Py_DECREF(obj) is not needed here
return 0;
}
```

The example can also be written without checking explicitly if obj is NULL:

```c
static int
add_spam(PyObject *module, int value)
{
    PyObject *obj = PyLong_FromLong(value);
    if (PyModule_AddObject(module, "spam", obj) < 0) {
        Py_XDECREF(obj);
        return -1;
    }
    // PyModule_AddObject() stole a reference to obj:
    // Py_DECREF(obj) is not needed here
    return 0;
}
```

Note that Py\_XDECREF() should be used instead of Py\_DECREF() in this case, since obj can be NULL.

## int PyModule\_AddIntConstant(PyObject \*module, const char \*name, long value)

Part of the Stable ABI. Add an integer constant to module as name. This convenience function can be used from the module’s initialization function. Return -1 on error, 0 on success.

## int PyModule\_AddStringConstant(PyObject \*module, const char \*name, const char \*value)

Part of the Stable ABI. Add a string constant to module as name. This convenience function can be used from the module’s initialization function. The string value must be NULL-terminated. Return -1 on error, 0 on success.

## int PyModule\_AddIntMacro(PyObject \*module, macro)

Add an int constant to module. The name and the value are taken from macro. For example PyModule\_AddIntMacro(module, AF\_INET) adds the int constant AF\_INET with the value of AF\_INET to module. Return -1 on error, 0 on success.

int **PyModule\_AddStringMacro**(PyObject \*module, macro) Add a string constant to module.

## int PyModule\_AddType(PyObject \*module, PyTypeObject \*type)

Part of the Stable ABI since version 3.10. Add a type object to module. The type object is finalized by calling internally PyType\_Ready(). The name of the type object is taken from the last component of tp\_name after dot. Return -1 on error, 0 on success.

New in version 3.9.

## Module lookup

Single-phase initialization creates singleton modules that can be looked up in the context of the current interpreter. This allows the module object to be retrieved later with only a reference to the module definition.

These functions will not work on modules created using multi-phase initialization, since multiple such modules can be created from a single definition.

## PyObject \*PyState\_FindModule(PyModuleDef \*def)

Return value: Borrowed reference. Part of the Stable ABI. Returns the module object that was created from def for the current interpreter. This method requires that the module object has been attached to the interpreter state with PyState\_AddModule() beforehand. In case the corresponding module object is not found or has not been attached to the interpreter state yet, it returns NULL.

## int PyState\_AddModule(PyObject \*module, PyModuleDef \*def)

Part of the Stable ABI since version 3.3. Attaches the module object passed to the function to the interpreter state. This allows the module object to be accessible via PyState\_FindModule().

Only effective on modules created using single-phase initialization.

Python calls PyState\_AddModule automatically after importing a module, so it is unnecessary (but harmless) to call it from module initialization code. An explicit call is needed only if the module’s own init code subsequently calls PyState\_FindModule. The function is mainly intended for implementing alternative import mechanisms (either by calling it directly, or by referring to its implementation for details of the required state updates).

The caller must hold the GIL.

Return 0 on success or -1 on failure.

New in version 3.3.

## int PyState\_RemoveModule(PyModuleDef \*def)

Part of the Stable ABI since version 3.3. Removes the module object created from def from the interpreter state. Return 0 on success or -1 on failure.

The caller must hold the GIL.

New in version 3.3.

## 8.6.3 Iterator Objects

Python provides two general-purpose iterator objects. The first, a sequence iterator, works with an arbitrary sequence supporting the \_\_getitem\_\_() method. The second works with a callable object and a sentinel value, calling the callable for each item in the sequence, and ending the iteration when the sentinel value is returned.

## PyTypeObject PySeqIter\_Type

Part of the Stable ABI. Type object for iterator objects returned by PySeqIter\_New() and the oneargument form of the iter() built-in function for built-in sequence types.

## int PySeqIter\_Check(op)

Return true if the type of op is PySeqIter\_Type. This function always succeeds.

## PyObject \*PySeqIter\_New(PyObject \*seq)

Return value: New reference. Part of the Stable ABI. Return an iterator that works with a general sequence object, seq. The iteration ends when the sequence raises IndexError for the subscripting operation.

## PyTypeObject PyCallIter\_Type

Part of the Stable ABI. Type object for iterator objects returned by PyCallIter\_New() and the twoargument form of the iter() built-in function.

## int PyCallIter\_Check(op)

Return true if the type of op is PyCallIter\_Type. This function always succeeds.

PyObject \***PyCallIter\_New**(PyObject \*callable, PyObject \*sentinel)

Return value: New reference. Part of the Stable ABI. Return a new iterator. The first parameter, callable, can be any Python callable object that can be called with no parameters; each call to it should return the next item in the iteration. When callable returns a value equal to sentinel, the iteration will be terminated.

## 8.6.4 Descriptor Objects

“Descriptors” are objects that describe some attribute of an object. They are found in the dictionary of type objects.

PyTypeObject **PyProperty\_Type**

Part of the Stable ABI. The type object for the built-in descriptor types.

PyObject \***PyDescr\_NewGetSet**(PyTypeObject \*type, **struct** PyGetSetDef \*getset) Return value: New reference. Part of the Stable ABI.

PyObject \***PyDescr\_NewMember**(PyTypeObject \*type, **struct** PyMemberDef \*meth) Return value: New reference. Part of the Stable ABI.

PyObject \***PyDescr\_NewMethod**(PyTypeObject \*type, **struct** PyMethodDef \*meth) Return value: New reference. Part of the Stable ABI.

PyObject \***PyDescr\_NewWrapper**(PyTypeObject \*type, **struct** wrapperbase \*wrapper, void \*wrapped)

Return value: New reference.

PyObject \***PyDescr\_NewClassMethod**(PyTypeObject \*type, PyMethodDef \*method) Return value: New reference. Part of the Stable ABI.

int **PyDescr\_IsData**(PyObject \*descr)

Return non-zero if the descriptor objects descr describes a data attribute, or 0 if it describes a method. descr must be a descriptor object; there is no error checking.

PyObject \***PyWrapper\_New**(PyObject\*, PyObject\*)

Return value: New reference. Part of the Stable ABI.

## 8.6.5 Slice Objects

PyTypeObject **PySlice\_Type**

Part of the Stable ABI. The type object for slice objects. This is the same as slice in the Python layer.

int **PySlice\_Check**(PyObject \*ob)

Return true if ob is a slice object; ob must not be NULL. This function always succeeds.

PyObject \***PySlice\_New**(PyObject \*start, PyObject \*stop, PyObject \*step)

Return value: New reference. Part of the Stable ABI. Return a new slice object with the given values. The start, stop, and step parameters are used as the values of the slice object attributes of the same names. Any of the values may be NULL, in which case the None will be used for the corresponding attribute. Return NULL if the new object could not be allocated.

int **PySlice\_GetIndices**(PyObject \*slice, Py\_ssize\_t length, Py\_ssize\_t \*start, Py\_ssize\_t \*stop, P i \* y\_ss ze\_t step)

Part of the Stable ABI. Retrieve the start, stop and step indices from the slice object slice, assuming a sequence of length length. Treats indices greater than length as errors.

Returns 0 on success and -1 on error with no exception set (unless one of the indices was not None and failed to be converted to an integer, in which case -1 is returned with an exception set).

You probably do not want to use this function.

Changed in version 3.2: The parameter type for the slice parameter was PySliceObject\* before.

int **PySlice\_GetIndicesEx**(PyObject \*slice, Py\_ssize\_t length, Py\_ssize\_t \*start, Py\_ssize\_t \*stop,

Py\_ssize\_t \*step, Py\_ssize\_t \*slicelength)

Part of the Stable ABI. Usable replacement for PySlice\_GetIndices(). Retrieve the start, stop, and

step indices from the slice object slice assuming a sequence of length length, and store the length of the slice in slicelength. Out of bounds indices are clipped in a manner consistent with the handling of normal slices.

Returns 0 on success and -1 on error with exception set.

**Note:** This function is considered not safe for resizable sequences. Its invocation should be replaced by a combination of PySlice\_Unpack() and PySlice\_AdjustIndices() where

```txt
if (PySlice_GetIndicesEx(slice, length, &start, &stop, &step, &slicelength) <0) {
    // return error
}
```

is replaced by

```c
if (PySlice_Unpack(slice, &start, &stop, &step) < 0) {
    // return error
}
slicelength = PySlice_AdjustIndices(length, &start, &stop, step);
```

Changed in version 3.2: The parameter type for the slice parameter was PySliceObject\* before.

Changed in version 3.6.1: If Py\_LIMITED\_API is not set or set to the value between 0x03050400 and 0x03060000 (not including) or 0x03060100 or higher PySlice\_GetIndicesEx() is implemented as a macro using PySlice\_Unpack() and PySlice\_AdjustIndices(). Arguments start, stop and step are evaluated more than once.

Deprecated since version 3.6.1: If Py\_LIMITED\_API is set to the value less than 0x03050400 or between 0x03060000 and 0x03060100 (not including) PySlice\_GetIndicesEx() is a deprecated function.

## int PySlice\_Unpack(PyObject \*slice, Py\_ssize\_t \*start, Py\_ssize\_t \*stop, Py\_ssize\_t \*step)

Part of the Stable ABI since version 3.7. Extract the start, stop and step data members from a slice object as C integers. Silently reduce values larger than PY\_SSIZE\_T\_MAX to PY\_SSIZE\_T\_MAX, silently boost the start and stop values less than PY\_SSIZE\_T\_MIN to PY\_SSIZE\_T\_MIN, and silently boost the step values less than -PY\_SSIZE\_T\_MAX to -PY\_SSIZE\_T\_MAX.

Return -1 on error, 0 on success.

New in version 3.6.1.

Py\_ssize\_t **PySlice\_AdjustIndices**(Py\_ssize\_t length, Py\_ssize\_t \*start, Py\_ssize\_t \*stop, Py\_ssize\_t

Part of the Stable ABI since version 3.7. Adjust start/end slice indices assuming a sequence of the specified length. Out of bounds indices are clipped in a manner consistent with the handling of normal slices.

Return the length of the slice. Always successful. Doesn’t call Python code.

New in version 3.6.1.

## 8.6.6 Ellipsis Object

## PyObject \*Py\_Ellipsis

The Python Ellipsis object. This object has no methods. It needs to be treated just like any other object with respect to reference counts. Like Py\_None it is a singleton object.

## 8.6.7 MemoryView objects

A memoryview object exposes the C level buffer interface as a Python object which can then be passed around like any other object.

## PyObject \*PyMemoryView\_FromObject(PyObject \*obj)

Return value: New reference. Part of the Stable ABI. Create a memoryview object from an object that provides the buffer interface. If obj supports writable buffer exports, the memoryview object will be read/write, otherwise it may be either read-only or read/write at the discretion of the exporter.

## PyObject \*PyMemoryView\_FromMemory(char \*mem, Py\_ssize\_t size, int flags)

Return value: New reference. Part of the Stable ABI since version 3.7. Create a memoryview object using mem as the underlying buffer. flags can be one of PyBUF\_READ or PyBUF\_WRITE.

New in version 3.3.

## PyObject \*PyMemoryView\_FromBuffer(Py\_buffer \*view)

Return value: New reference. Create a memoryview object wrapping the given buffer structure view. For simple byte buffers, PyMemoryView\_FromMemory() is the preferred function.

## PyObject \*PyMemoryView\_GetContiguous(PyObject \*obj, int buffertype, char order)

Return value: New reference. Part of the Stable ABI. Create a memoryview object to a contiguous chunk of memory (in either ‘C’ or ‘F’ortran order) from an object that defines the buffer interface. If memory is contiguous, the memoryview object points to the original memory. Otherwise, a copy is made and the memoryview points to a new bytes object.

## int PyMemoryView\_Check(PyObject \*obj)

Return true if the object obj is a memoryview object. It is not currently allowed to create subclasses of memoryview. This function always succeeds.

## Py\_buffer \*PyMemoryView\_GET\_BUFFER(PyObject \*mview)

Return a pointer to the memoryview’s private copy of the exporter’s buffer. mview **must** be a memoryview instance; this macro doesn’t check its type, you must do it yourself or you will risk crashes.

## PyObject \*PyMemoryView\_GET\_BASE(PyObject \*mview)

Return either a pointer to the exporting object that the memoryview is based on or NULL if the memoryview has been created by one of the functions PyMemoryView\_FromMemory() or PyMemoryView\_FromBuffer(). mview **must** be a memoryview instance.

## 8.6.8 Weak Reference Objects

Python supports weak references as first-class objects. There are two specific object types which directly implement weak references. The first is a simple reference object, and the second acts as a proxy for the original object as much as it can.

## int PyWeakref\_Check(ob)

Return true if ob is either a reference or proxy object. This function always succeeds.

## int PyWeakref\_CheckRef(ob)

Return true if ob is a reference object. This function always succeeds.

## int PyWeakref\_CheckProxy(ob)

Return true if ob is a proxy object. This function always succeeds.

## PyObject \*PyWeakref\_NewRef(PyObject \*ob, PyObject \*callback)

Return value: New reference. Part of the Stable ABI. Return a weak reference object for the object ob. This will always return a new reference, but is not guaranteed to create a new object; an existing reference object may be returned. The second parameter, callback, can be a callable object that receives notification when ob is garbage collected; it should accept a single parameter, which will be the weak reference object itself. callback may also be None or NULL. If ob is not a weakly referencable object, or if callback is not callable, None, or NULL, this will return NULL and raise TypeError.

## PyObject \*PyWeakref\_NewProxy(PyObject \*ob, PyObject \*callback)

Return value: New reference. Part of the Stable ABI. Return a weak reference proxy object for the object ob. This will always return a new reference, but is not guaranteed to create a new object; an existing proxy object may be returned. The second parameter, callback, can be a callable object that receives notification when ob is garbage collected; it should accept a single parameter, which will be the weak reference object itself. callback may also be None or NULL. If ob is not a weakly referencable object, or if callback is not callable, None, or NULL, this will return NULL and raise TypeError.

## PyObject \*PyWeakref\_GetObject(PyObject \*ref)

Return value: Borrowed reference. Part of the Stable ABI. Return the referenced object from a weak reference, ref. If the referent is no longer live, returns Py\_None.

**Note:** This function returns a borrowed reference to the referenced object. This means that you should always call Py\_INCREF() on the object except when it cannot be destroyed before the last usage of the borrowed reference.

## PyObject \*PyWeakref\_GET\_OBJECT(PyObject \*ref)

Return value: Borrowed reference. Similar to PyWeakref\_GetObject(), but implemented as a macro that does no error checking.

## void PyObject\_ClearWeakRefs(PyObject \*object)

Part of the Stable ABI. This function is called by the tp\_dealloc handler to clear weak references.

This iterates through the weak references for object and calls callbacks for those references which have one. It returns when all callbacks have been attempted.

## 8.6.9 Capsules

Refer to using-capsules for more information on using these objects.

New in version 3.1.

## type PyCapsule

This subtype of PyObject represents an opaque value, useful for C extension modules who need to pass an opaque value (as a void\* pointer) through Python code to other C code. It is often used to make a C function pointer defined in one module available to other modules, so the regular import mechanism can be used to access C APIs defined in dynamically loaded modules.

## type PyCapsule\_Destructor

Part of the Stable ABI. The type of a destructor callback for a capsule. Defined as:

```txt
typedef void (*PyCapsule_Destructor) (PyObject *);
```

See PyCapsule\_New() for the semantics of PyCapsule\_Destructor callbacks.

## int PyCapsule\_CheckExact(PyObject \*p)

Return true if its argument is a PyCapsule. This function always succeeds.

## PyObject \*PyCapsule\_New(void \*pointer, const char \*name, PyCapsule\_Destructor destructor)

Return value: New reference. Part of the Stable ABI. Create a PyCapsule encapsulating the pointer. The pointer argument may not be NULL.

On failure, set an exception and return NULL.

The name string may either be NULL or a pointer to a valid C string. If non-NULL, this string must outlive the capsule. (Though it is permitted to free it inside the destructor.)

If the destructor argument is not NULL, it will be called with the capsule as its argument when it is destroyed.

If this capsule will be stored as an attribute of a module, the name should be specified as modulename. attributename. This will enable other modules to import the capsule using PyCapsule\_Import().

int PyCapsule\_SetPointer(PyObject \*capsule, void \*pointer) Part of the Stable ABI. Set the void pointer inside capsule to pointer. The pointer may not be NULL.

void \*PyCapsule\_Import(const char \*name, int no\_block) Part of the Stable ABI. Import a pointer to a C object from a capsule attribute in a module. The name parameter should specify the full name to the attribute, as in module.attribute. The name stored in the capsule must match this string exactly. If no\_block is true, import the module without blocking (using PyImport\_ImportModuleNoBlock()). If no\_block is false, import the module conventionally (using PyImport\_ImportModule()).

void \*PyCapsule\_GetPointer(PyObject \*capsule, const char \*name) Part of the Stable ABI. Retrieve the pointer stored in the capsule. On failure, set an exception and return NULL. The name parameter must compare exactly to the name stored in the capsule. If the name stored in the capsule is NULL, the name passed in must also be NULL. Python uses the C function strcmp() to compare capsule names.

PyCapsule\_Destructor PyCapsule\_GetDestructor(PyObject \*capsule) Part of the Stable ABI. Return the current destructor stored in the capsule. On failure, set an exception and return NULL. It is legal for a capsule to have a NULL destructor. This makes a NULL return code somewhat ambiguous; use PyCapsule\_IsValid() or PyErr\_Occurred() to disambiguate.

void \*PyCapsule\_GetContext(PyObject \*capsule) Part of the Stable ABI. Return the current context stored in the capsule. On failure, set an exception and return NULL. It is legal for a capsule to have a NULL context. This makes a NULL return code somewhat ambiguous; use PyCapsule\_IsValid() or PyErr\_Occurred() to disambiguate.

const char \*PyCapsule\_GetName(PyObject \*capsule) Part of the Stable ABI. Return the current name stored in the capsule. On failure, set an exception and return NULL. It is legal for a capsule to have a NULL name. This makes a NULL return code somewhat ambiguous; use PyCapsule\_IsValid() or PyErr\_Occurred() to disambiguate.

int PyCapsule\_IsValid(PyObject \*capsule, const char \*name) Part of the Stable ABI. Determines whether or not capsule is a valid capsule. A valid capsule is non-NULL, passes PyCapsule\_CheckExact(), has a non-NULL pointer stored in it, and its internal name matches the name parameter. (See PyCapsule\_GetPointer() for information on how capsule names are compared.) In other words, if PyCapsule\_IsValid() returns a true value, calls to any of the accessors (any function starting with PyCapsule\_Get()) are guaranteed to succeed. Return a nonzero value if the object is valid and matches the name passed in. Return 0 otherwise. This function will not fail.

int **PyCapsule\_SetContext**(PyObject \*capsule, void \*context) Part of the Stable ABI. Set the context pointer inside capsule to context.

int **PyCapsule\_SetDestructor**(PyObject \*capsule, PyCapsule\_Destructor destructor) Part of the Stable ABI. Set the destructor inside capsule to destructor.

Return 0 on success. Return nonzero and set an exception on failure.

Return 0 on success. Return nonzero and set an exception on failure.

## 8.6.10 Generator Objects

Generator objects are what Python uses to implement generator iterators. They are normally created by iterating over a function that yields values, rather than explicitly calling PyGen\_New() or PyGen\_NewWithQualName().

**type PyGenObject**

The C structure used for generator objects.

PyTypeObject **PyGen\_Type**

The type object corresponding to generator objects.

```txt
int PyGen_Check (PyObject *ob)
```

Return true if ob is a generator object; ob must not be NULL. This function always succeeds.

int **PyGen\_CheckExact**(PyObject \*ob)

Return true if ob’s type is PyGen\_Type; ob must not be NULL. This function always succeeds.

```txt
PyObject *PyGen_New (PyFrameObject *frame)
```

Return value: New reference. Create and return a new generator object based on the frame object. A reference to frame is stolen by this function. The argument must not be NULL.

PyObject \***PyGen\_NewWithQualName**(PyFrameObject \*frame, PyObject \*name, PyObject \*qualname)

Return value: New reference. Create and return a new generator object based on the frame object, with name\_\_ and \_\_qualname\_\_ set to name and qualname. A reference to frame is stolen by this function. The frame argument must not be NULL.

## 8.6.11 Coroutine Objects

New in version 3.5.

Coroutine objects are what functions declared with an async keyword return.

**type PyCoroObject**

The C structure used for coroutine objects.

PyTypeObject **PyCoro\_Type**

The type object corresponding to coroutine objects.

int **PyCoro\_CheckExact**(PyObject \*ob)

Return true if ob’s type is PyCoro\_Type; ob must not be NULL. This function always succeeds.

PyObject \***PyCoro\_New**(PyFrameObject \*frame, PyObject \*name, PyObject \*qualname)

Return value: New reference. Create and return a new coroutine object based on the frame object, with name\_\_ and \_\_qualname\_\_ set to name and qualname. A reference to frame is stolen by this function. The frame argument must not be NULL.

## 8.6.12 Context Variables Objects

**Note:** Changed in version 3.7.1: In Python 3.7.1 the signatures of all context variables C APIs were **changed** to use PyObject pointers instead of PyContext, PyContextVar, and PyContextToken, e.g.:

```c
// in 3.7.0:
PyContext *PyContext_New(void);

// in 3.7.1+:
PyObject *PyContext_New(void);
```

See [bpo-34762](https://bugs.python.org/issue?@action=redirect&bpo=34762) for more details.

New in version 3.7. This section details the public C API for the contextvars module. **type PyContext** The C structure used to represent a contextvars.Context object. **type PyContextVar** The C structure used to represent a contextvars.ContextVar object. **type PyContextToken** The C structure used to represent a contextvars.Token object. PyTypeObject **PyContext\_Type** The type object representing the context type. PyTypeObject **PyContextVar\_Type** The type object representing the context variable type. PyTypeObject **PyContextToken\_Type** The type object representing the context variable token type. Type-check macros: int **PyContext\_CheckExact**(PyObject \*o) Return true if o is of type PyContext\_Type. o must not be NULL. This function always succeeds. int **PyContextVar\_CheckExact**(PyObject \*o) Return true if o is of type PyContextVar\_Type. o must not be NULL. This function always succeeds. int **PyContextToken\_CheckExact**(PyObject \*o) Return true if o is of type PyContextToken\_Type. o must not be NULL. This function always succeeds. Context object management functions: PyObject \***PyContext\_New**(void) Return value: New reference. Create a new empty context object. Returns NULL if an error has occurred. PyObject \***PyContext\_Copy**(PyObject \*ctx) Return value: New reference. Create a shallow copy of the passed ctx context object. Returns NULL if an error has occurred. PyObject \***PyContext\_CopyCurrent**(void) Return value: New reference. Create a shallow copy of the current thread context. Returns NULL if an error has occurred. int **PyContext\_Enter**(PyObject \*ctx) Set ctx as the current context for the current thread. Returns 0 on success, and -1 on error. int **PyContext\_Exit**(PyObject \*ctx) Deactivate the ctx context and restore the previous context as the current context for the current thread. Returns 0 on success, and -1 on error. Context variable functions: PyObject \***PyContextVar\_New**(**const** char \*name, PyObject \*def) Return value: New reference. Create a new ContextVar object. The name parameter is used for introspection and debug purposes. The def parameter specifies a default value for the context variable, or NULL for no default. If an error has occurred, this function returns NULL. int **PyContextVar\_Get**(PyObject \*var, PyObject \*default\_value, PyObject \*\*value) Get the value of a context variable. Returns -1 if an error has occurred during lookup, and 0 if no error occurred, whether or not a value was found. If the context variable was found, value will be a pointer to it. If the context variable was not found, value will point to:

• default\_value, if not NULL;

• the default value of var, if not NULL;

• NULL

Except for NULL, the function returns a new reference.

PyObject \***PyContextVar\_Set**(PyObject \*var, PyObject \*value)

Return value: New reference. Set the value of var to value in the current context. Returns a new token object for this change, or NULL if an error has occurred.

int **PyContextVar\_Reset**(PyObject \*var, PyObject \*token)

Reset the state of the var context variable to that it was in before PyContextVar\_Set() that returned the token was called. This function returns 0 on success and -1 on error.

## 8.6.13 DateTime Objects

Various date and time objects are supplied by the datetime module. Before using any of these functions, the header file datetime.h must be included in your source (note that this is not included by Python.h), and the macro PyDateTime\_IMPORT must be invoked, usually as part of the module initialisation function. The macro puts a pointer to a C structure into a static variable, PyDateTimeAPI, that is used by the following macros.

Macro for access to the UTC singleton:

PyObject \***PyDateTime\_TimeZone\_UTC** Returns the time zone singleton representing UTC, the same object as datetime.timezone.utc. New in version 3.7.

Type-check macros:

int **PyDate\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateType or a subtype of PyDateTime\_DateType. ob must not be NULL. This function always succeeds.

int **PyDate\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateType. ob must not be NULL. This function always succeeds.

int **PyDateTime\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateTimeType or a subtype of PyDateTime\_DateTimeType. ob must not be NULL. This function always succeeds.

int **PyDateTime\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateTimeType. ob must not be NULL. This function always succeeds.

int **PyTime\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_TimeType or a subtype of PyDateTime\_TimeType. ob must not be NULL. This function always succeeds.

int **PyTime\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_TimeType. ob must not be NULL. This function always succeeds.

int **PyDelta\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_DeltaType or a subtype of PyDateTime\_DeltaType. ob must not be NULL. This function always succeeds.

int **PyDelta\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_DeltaType. ob must not be NULL. This function always succeeds.

int **PyTZInfo\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_TZInfoType or a subtype of PyDateTime\_TZInfoType. ob must not be NULL. This function always succeeds.

int PyTZInfo\_CheckExact(PyObject \*ob) Return true if ob is of type PyDateTime\_TZInfoType. ob must not be NULL. This function always succeeds.

PyObject \*PyDateTime\_FromDateAndTime(int year, int month, int day, int hour, int minute, int second, int usecond) Return value: New reference. Return a datetime.datetime object with the specified year, month, day, hour, minute, second and microsecond.

PyObject \*PyDate\_FromDate(int year, int month, int day) Return value: New reference. Return a datetime.date object with the specified year, month and day.

PyObject \*PyDateTime\_FromDateAndTimeAndFold(int year, int month, int day, int hour, int minute, int second, int usecond, int fold) Return value: New reference. Return a datetime.datetime object with the specified year, month, day, hour, minute, second, microsecond and fold. New in version 3.6.

PyObject \*PyTime\_FromTime(int hour, int minute, int second, int usecond) Return value: New reference. Return a datetime.time object with the specified hour, minute, second and microsecond.

int **PyDateTime\_DATE\_GET\_SECOND**(PyDateTime\_DateTime \*o) Return the second, as an int from 0 through 59. int **PyDateTime\_DATE\_GET\_MICROSECOND**(PyDateTime\_DateTime \*o) Return the microsecond, as an int from 0 through 999999. int **PyDateTime\_DATE\_GET\_FOLD**(PyDateTime\_DateTime \*o) Return the fold, as an int from 0 through 1. New in version 3.6. PyObject \***PyDateTime\_DATE\_GET\_TZINFO**(PyDateTime\_DateTime \*o) Return the tzinfo (which may be None). New in version 3.10. Macros to extract fields from time objects. The argument must be an instance of PyDateTime\_Time, including subclasses. The argument must not be NULL, and the type is not checked: int **PyDateTime\_TIME\_GET\_HOUR**(PyDateTime\_Time \*o) Return the hour, as an int from 0 through 23. int **PyDateTime\_TIME\_GET\_MINUTE**(PyDateTime\_Time \*o) Return the minute, as an int from 0 through 59. int **PyDateTime\_TIME\_GET\_SECOND**(PyDateTime\_Time \*o) Return the second, as an int from 0 through 59. int **PyDateTime\_TIME\_GET\_MICROSECOND**(PyDateTime\_Time \*o) Return the microsecond, as an int from 0 through 999999. int **PyDateTime\_TIME\_GET\_FOLD**(PyDateTime\_Time \*o) Return the fold, as an int from 0 through 1. New in version 3.6. PyObject \***PyDateTime\_TIME\_GET\_TZINFO**(PyDateTime\_Time \*o) Return the tzinfo (which may be None). New in version 3.10. Macros to extract fields from time delta objects. The argument must be an instance of PyDateTime\_Delta, including subclasses. The argument must not be NULL, and the type is not checked: int **PyDateTime\_DELTA\_GET\_DAYS**(PyDateTime\_Delta \*o) Return the number of days, as an int from -999999999 to 999999999. New in version 3.3. int **PyDateTime\_DELTA\_GET\_SECONDS**(PyDateTime\_Delta \*o) Return the number of seconds, as an int from 0 through 86399. New in version 3.3. int **PyDateTime\_DELTA\_GET\_MICROSECONDS**(PyDateTime\_Delta \*o) Return the number of microseconds, as an int from 0 through 999999. New in version 3.3. Macros for the convenience of modules implementing the DB API: PyObject \***PyDateTime\_FromTimestamp**(PyObject \*args) Return value: New reference. Create and return a new datetime.datetime object given an argument tuple suitable for passing to datetime.datetime.fromtimestamp(). PyObject \***PyDate\_FromTimestamp**(PyObject \*args) Return value: New reference. Create and return a new datetime.date object given an argument tuple suitable for passing to datetime.date.fromtimestamp().

## 8.6.14 Objects for Type Hinting

Various built-in types for type hinting are provided. Currently, two types exist – GenericAlias and Union. Only GenericAlias is exposed to C.

## PyObject \*Py\_GenericAlias(PyObject \*origin, PyObject \*args)

Part of the Stable ABI since version 3.9. Create a GenericAlias object. Equivalent to calling the Python class types.GenericAlias. The origin and args arguments set the GenericAlias‘s \_\_origin and \_\_args\_\_ attributes respectively. origin should be a PyTypeObject\*, and args can be a PyTupleObject\* or any PyObject\*. If args passed is not a tuple, a 1-tuple is automatically constructed and \_\_args\_\_ is set to (args,). Minimal checking is done for the arguments, so the function will succeed even if origin is not a type. The GenericAlias‘s \_\_parameters\_\_ attribute is constructed lazily from \_args\_\_. On failure, an exception is raised and NULL is returned.

Here’s an example of how to make an extension type generic:

```c
static PyMethodDef my_obj_methods[] = {
    // Other methods.
    {"__class_getitem__", (PyCFunction)Py_GenericAlias, METH_O|METH_CLASS,
    "See PEP 585"}
}
```

## See also:

The data model method \_\_class\_getitem\_\_().

New in version 3.9.

## PyTypeObject Py\_GenericAliasType

Part of the Stable ABI since version 3.9. The C type of the object returned by Py\_GenericAlias(). Equivalent to types.GenericAlias in Python.

New in version 3.9.

# INITIALIZATION, FINALIZATION, AND THREADS

See also Python Initialization Configuration.

## 9.1 Before Python Initialization

In an application embedding Python, the Py\_Initialize() function must be called before using any other Python/C API functions; with the exception of a few functions and the global configuration variables.

The following functions can be safely called before Python is initialized:

• Configuration functions:

– PyImport\_AppendInittab()

– PyImport\_ExtendInittab()

– PyInitFrozenExtensions()

– PyMem\_SetAllocator()

– PyMem\_SetupDebugHooks()

– PyObject\_SetArenaAllocator()

– Py\_SetPath()

– Py\_SetProgramName()

– Py\_SetPythonHome()

– Py\_SetStandardStreamEncoding()

– PySys\_AddWarnOption()

– PySys\_AddXOption()

– PySys\_ResetWarnOptions()

• Informative functions:

– Py\_IsInitialized()

– PyMem\_GetAllocator()

– PyObject\_GetArenaAllocator()

– Py\_GetBuildInfo()

– Py\_GetCompiler()

– Py\_GetCopyright()

– Py\_GetPlatform()

– Py\_GetVersion()

• Utilities:

## The Python/C API, Release 3.10.15

– Py\_DecodeLocale()

• Memory allocators:

– PyMem\_RawMalloc()

– PyMem\_RawRealloc()

– PyMem\_RawCalloc()

– PyMem\_RawFree()

**Note:** The following functions **should not be called** before Py\_Initialize(): Py\_EncodeLocale(), Py\_GetPath(), Py\_GetPrefix(), Py\_GetExecPrefix(), Py\_GetProgramFullPath(), Py\_GetPythonHome(), Py\_GetProgramName() and PyEval\_InitThreads().

## 9.2 Global configuration variables

Python has variables for the global configuration to control different features and options. By default, these flags are controlled by command line options.

When a flag is set by an option, the value of the flag is the number of times that the option was set. For example, -b sets Py\_BytesWarningFlag to 1 and -bb sets Py\_BytesWarningFlag to 2.

## int Py\_BytesWarningFlag

Issue a warning when comparing bytes or bytearray with str or bytes with int. Issue an error if greater or equal to 2.

Set by the -b option.

## int Py\_DebugFlag

Turn on parser debugging output (for expert only, depending on compilation options).

Set by the -d option and the PYTHONDEBUG environment variable.

## int Py\_DontWriteBytecodeFlag

If set to non-zero, Python won’t try to write .pyc files on the import of source modules.

Set by the -B option and the PYTHONDONTWRITEBYTECODE environment variable.

## int Py\_FrozenFlag

Suppress error messages when calculating the module search path in Py\_GetPath().

Private flag used by \_freeze\_importlib and frozenmain programs.

## int Py\_HashRandomizationFlag

Set to 1 if the PYTHONHASHSEED environment variable is set to a non-empty string.

If the flag is non-zero, read the PYTHONHASHSEED environment variable to initialize the secret hash seed.

## int Py\_IgnoreEnvironmentFlag

Ignore all PYTHON\* environment variables, e.g. PYTHONPATH and PYTHONHOME, that might be set.

Set by the -E and -I options.

## int Py\_InspectFlag

When a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command, even when sys.stdin does not appear to be a terminal.

Set by the -i option and the PYTHONINSPECT environment variable.

## int Py\_InteractiveFlag

Set by the -i option.

## int Py\_IsolatedFlag

Run Python in isolated mode. In isolated mode sys.path contains neither the script’s directory nor the user’s site-packages directory. Set by the -I option. New in version 3.4.

## int Py\_LegacyWindowsFSEncodingFlag

If the flag is non-zero, use the mbcs encoding with replace error handler, instead of the UTF-8 encoding with surrogatepass error handler, for the filesystem encoding and error handler. Set to 1 if the PYTHONLEGACYWINDOWSFSENCODING environment variable is set to a non-empty string. See [**PEP 529**](https://www.python.org/dev/peps/pep-0529) for more details. Availability: Windows.

## int Py\_LegacyWindowsStdioFlag

If the flag is non-zero, use io.FileIO instead of WindowsConsoleIO for sys standard streams. Set to 1 if the PYTHONLEGACYWINDOWSSTDIO environment variable is set to a non-empty string. See [**PEP 528**](https://www.python.org/dev/peps/pep-0528) for more details. Availability: Windows.

## int Py\_NoSiteFlag

Disable the import of the module site and the site-dependent manipulations of sys.path that it entails. Also disable these manipulations if site is explicitly imported later (call site.main() if you want them to be triggered). Set by the -S option.

## int Py\_NoUserSiteDirectory

Don’t add the user site-packages directory to sys.path.

Set by the -s and -I options, and the PYTHONNOUSERSITE environment variable.

## int Py\_OptimizeFlag

Set by the -O option and the PYTHONOPTIMIZE environment variable.

## int Py\_QuietFlag

Don’t display the copyright and version messages even in interactive mode. Set by the -q option. New in version 3.2.

## int Py\_UnbufferedStdioFlag

Force the stdout and stderr streams to be unbuffered.

Set by the -u option and the PYTHONUNBUFFERED environment variable.

## int Py\_VerboseFlag

Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. If greater or equal to 2, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit. Set by the -v option and the PYTHONVERBOSE environment variable.

## 9.3 Initializing and finalizing the interpreter

## void Py\_Initialize()

Part of the Stable ABI. Initialize the Python interpreter. In an application embedding Python, this should be called before using any other Python/C API functions; see Before Python Initialization for the few exceptions.

This initializes the table of loaded modules (sys.modules), and creates the fundamental modules builtins, \_\_main\_\_ and sys. It also initializes the module search path (sys.path). It does not set sys.argv; use PySys\_SetArgvEx() for that. This is a no-op when called for a second time (without calling Py\_FinalizeEx() first). There is no return value; it is a fatal error if the initialization fails.

**Note:** On Windows, changes the console mode from O\_TEXT to O\_BINARY, which will also affect non-Python uses of the console using the C Runtime.

## void Py\_InitializeEx(int initsigs)

Part of the Stable ABI. This function works like Py\_Initialize() if initsigs is 1. If initsigs is 0, it skips initialization registration of signal handlers, which might be useful when Python is embedded.

## int Py\_IsInitialized()

Part of the Stable ABI. Return true (nonzero) when the Python interpreter has been initialized, false (zero) if not. After Py\_FinalizeEx() is called, this returns false until Py\_Initialize() is called again.

## int Py\_FinalizeEx()

Part of the Stable ABI since version 3.6. Undo all initializations made by Py\_Initialize() and subsequent use of Python/C API functions, and destroy all sub-interpreters (see Py\_NewInterpreter() below) that were created and not yet destroyed since the last call to Py\_Initialize(). Ideally, this frees all memory allocated by the Python interpreter. This is a no-op when called for a second time (without calling Py\_Initialize() again first). Normally the return value is 0. If there were errors during finalization (flushing buffered data), -1 is returned.

This function is provided for a number of reasons. An embedding application might want to restart Python without having to restart the application itself. An application that has loaded the Python interpreter from a dynamically loadable library (or DLL) might want to free all memory allocated by Python before unloading the DLL. During a hunt for memory leaks in an application a developer might want to free all memory allocated by Python before exiting from the application.

**Bugs and caveats:** The destruction of modules and objects in modules is done in random order; this may cause destructors (\_\_del\_\_() methods) to fail when they depend on other objects (even functions) or modules. Dynamically loaded extension modules loaded by Python are not unloaded. Small amounts of memory allocated by the Python interpreter may not be freed (if you find a leak, please report it). Memory tied up in circular references between objects is not freed. Some memory allocated by extension modules may not be freed. Some extensions may not work properly if their initialization routine is called more than once; this can happen if an application calls Py\_Initialize() and Py\_FinalizeEx() more than once.

Raises an auditing event cpython.\_PySys\_ClearAuditHooks with no arguments.

New in version 3.6.

## void Py\_Finalize()

Part of the Stable ABI. This is a backwards-compatible version of Py\_FinalizeEx() that disregards the return value.

## 9.4 Process-wide parameters

## int Py\_SetStandardStreamEncoding(const char \*encoding, const char \*errors)

This function should be called before Py\_Initialize() , if it is called at all. It specifies which encoding and error handling to use with standard IO, with the same meanings as in str.encode().

It overrides PYTHONIOENCODING values, and allows embedding code to control IO encoding when the environment variable does not work.

encoding and/or errors may be NULL to use PYTHONIOENCODING and/or default values (depending on other settings).

Note that sys.stderr always uses the “backslashreplace” error handler, regardless of this (or any other) setting.

If Py\_FinalizeEx() is called, this function will need to be called again in order to affect subsequent calls to Py\_Initialize()

Returns 0 if successful, a nonzero value on error (e.g. calling after the interpreter has already been initialized).

New in version 3.4.

## void Py\_SetProgramName(const wchar\_t \*name)

Part of the Stable ABI. This function should be called before Py\_Initialize() is called for the first time, if it is called at all. It tells the interpreter the value of the argv[0] argument to the main() function of the program (converted to wide characters). This is used by Py\_GetPath() and some other functions below to find the Python run-time libraries relative to the interpreter executable. The default value is 'python'. The argument should point to a zero-terminated wide character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage.

Use Py\_DecodeLocale() to decode a bytes string to get a wchar\_\* string.

## wchar \*Py\_GetProgramName()

Part of the Stable ABI. Return the program name set with Py\_SetProgramName(), or the default. The returned string points into static storage; the caller should not modify its value.

This function should not be called before Py\_Initialize(), otherwise it returns NULL.

Changed in version 3.10: It now returns NULL if called before Py\_Initialize()

## wchar\_t \*Py\_GetPrefix()

Part of the Stable ABI. Return the prefix for installed platform-independent files. This is derived through a number of complicated rules from the program name set with Py\_SetProgramName() and some environment variables; for example, if the program name is '/usr/local/bin/python', the prefix is '/usr/ local'. The returned string points into static storage; the caller should not modify its value. This corresponds to the **prefix** variable in the top-level Makefile and the --prefix argument to the **configure** script at build time. The value is available to Python code as sys.prefix. It is only useful on Unix. See also the next function.

This function should not be called before Py\_Initialize() , otherwise it returns NULL.

Changed in version 3.10: It now returns NULL if called before Py\_Initialize()

## wchar\_t \*Py\_GetExecPrefix()

Part of the Stable ABI. Return the exec-prefix for installed platform-dependent files. This is derived through a number of complicated rules from the program name set with Py\_SetProgramName() and some environment variables; for example, if the program name is '/usr/local/bin/python', the exec-prefix is '/usr/local' . The returned string points into static storage; the caller should not modify its value. This corresponds to the **exec\_prefix** variable in the top-level Makefile and the --exec-prefix argument to the **configure** script at build time. The value is available to Python code as sys.exec\_prefix. It is only useful on Unix.

Background: The exec-prefix differs from the prefix when platform dependent files (such as executables and shared libraries) are installed in a different directory tree. In a typical installation, platform dependent files

may be installed in the /usr/local/plat subtree while platform independent may be installed in /usr/ local.

Generally speaking, a platform is a combination of hardware and software families, e.g. Sparc machines running the Solaris 2.x operating system are considered the same platform, but Intel machines running Solaris 2.x are another platform, and Intel machines running Linux are yet another platform. Different major revisions of the same operating system generally also form different platforms. Non-Unix operating systems are a different story; the installation strategies on those systems are so different that the prefix and exec-prefix are meaningless, and set to the empty string. Note that compiled Python bytecode files are platform independent (but not independent from the Python version by which they were compiled!).

System administrators will know how to configure the **mount** or **automount** programs to share /usr/ local between platforms while having /usr/local/plat be a different filesystem for each platform.

This function should not be called before Py\_Initialize(), otherwise it returns NULL.

Changed in version 3.10: It now returns NULL if called before Py\_Initialize().

## wchar\_t \*Py\_GetProgramFullPath()

Part of the Stable ABI. Return the full program name of the Python executable; this is computed as a sideeffect of deriving the default module search path from the program name (set by Py\_SetProgramName() above). The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys.executable.

This function should not be called before Py\_Initialize(), otherwise it returns NULL.

Changed in version 3.10: It now returns NULL if called before Py\_Initialize().

## wchar\_t \*Py\_GetPath()

Part of the Stable ABI. Return the default module search path; this is computed from the program name (set by Py\_SetProgramName() above) and some environment variables. The returned string consists of a series of directory names separated by a platform dependent delimiter character. The delimiter character is ':' on Unix and macOS, ';' on Windows. The returned string points into static storage; the caller should not modify its value. The list sys.path is initialized with this value on interpreter startup; it can be (and usually is) modified later to change the search path for loading modules.

This function should not be called before Py\_Initialize(), otherwise it returns NULL.

Changed in version 3.10: It now returns NULL if called before Py\_Initialize().

## void Py\_SetPath(const wchar\_t\*)

Part of the Stable ABI since version 3.7. Set the default module search path. If this function is called before Py\_Initialize(), then Py\_GetPath() won’t attempt to compute a default search path but uses the one provided instead. This is useful if Python is embedded by an application that has full knowledge of the location of all modules. The path components should be separated by the platform dependent delimiter character, which is ':' on Unix and macOS, ';' on Windows.

This also causes sys.executable to be set to the program full path (see Py\_GetProgramFullPath()) and for sys.prefix and sys.exec\_prefix to be empty. It is up to the caller to modify these if required after calling Py\_Initialize().

Use Py\_DecodeLocale() to decode a bytes string to get a wchar\_\* string.

The path argument is copied internally, so the caller may free it after the call completes.

Changed in version 3.8: The program full path is now used for sys.executable, instead of the program name.

## const char \*Py\_GetVersion()

Part of the Stable ABI. Return the version of this Python interpreter. This is a string that looks something like

```txt
"3.0a5+ (py3k:63103M, May 12 2008, 00:53:55) \n[GCC 4.2.3]"
```

The first word (up to the first space character) is the current Python version; the first characters are the major and minor version separated by a period. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys.version.

## const char \*Py\_GetPlatform()

Part of the Stable ABI. Return the platform identifier for the current platform. On Unix, this is formed from the “official” name of the operating system, converted to lower case, followed by the major revision number; e.g., for Solaris 2.x, which is also known as SunOS 5.x, the value is 'sunos5'. On macOS, it is 'darwin'. On Windows, it is 'win'. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys.platform.

## const char \*Py\_GetCopyright()

Part of the Stable ABI. Return the official copyright string for the current Python version, for example

'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam'

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys.copyright.

## const char \*Py\_GetCompiler()

Part of the Stable ABI. Return an indication of the compiler used to build the current Python version, in square brackets, for example:

```txt
"[GCC 2.7.2.2]"
```

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable sys.version.

## const char \*Py\_GetBuildInfo()

Part of the Stable ABI. Return information about the sequence number and build date and time of the current Python interpreter instance, for example

```txt
"#67, Aug 1 1997, 22:34:28"
```

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable sys.version.

## void PySys\_SetArgvEx(int argc, wchar\_t \*\*argv, int updatepath)

Part of the Stable ABI. Set sys.argv based on argc and argv. These parameters are similar to those passed to the program’s main() function with the difference that the first entry should refer to the script file to be executed rather than the executable hosting the Python interpreter. If there isn’t a script that will be run, the first entry in argv can be an empty string. If this function fails to initialize sys.argv, a fatal condition is signalled using Py\_FatalError().

If updatepath is zero, this is all the function does. If updatepath is non-zero, the function also modifies sys. path according to the following algorithm:

• If the name of an existing script is passed in argv[0], the absolute path of the directory where the script is located is prepended to sys.path.

• Otherwise (that is, if argc is 0 or argv[0] doesn’t point to an existing file name), an empty string is prepended to sys.path, which is the same as prepending the current working directory (".").

Use Py\_DecodeLocale() to decode a bytes string to get a wchar\_\* string.

**Note:** It is recommended that applications embedding the Python interpreter for purposes other than executing a single script pass 0 as updatepath, and update sys.path themselves if desired. See [CVE-2008-5983](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-5983).

On versions before 3.1.3, you can achieve the same effect by manually popping the first sys.path element after having called PySys\_SetArgv(), for example using:

```javascript
PyRun_SimpleString("import sys; sys.path.pop(0)\n");
```

New in version 3.1.3.

## void PySys\_SetArgv(int argc, wchar\_t \*\*argv)

Part of the Stable ABI. This function works like PySys\_SetArgvEx() with updatepath set to 1 unless the **python** interpreter was started with the -I.

Use Py\_DecodeLocale() to decode a bytes string to get a wchar\_\* string.

Changed in version 3.4: The updatepath value depends on -I.

## void Py\_SetPythonHome(const wchar\_t \*home)

Part of the Stable ABI. Set the default “home” directory, that is, the location of the standard Python libraries. See PYTHONHOME for the meaning of the argument string.

The argument should point to a zero-terminated character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage.

Use Py\_DecodeLocale() to decode a bytes string to get a wchar\_\* string.

## wchar\_t \*Py\_GetPythonHome()

Part of the Stable ABI. Return the default “home”, that is, the value set by a previous call to Py\_SetPythonHome(), or the value of the PYTHONHOME environment variable if it is set.

This function should not be called before Py\_Initialize(), otherwise it returns NULL.

Changed in version 3.10: It now returns NULL if called before Py\_Initialize().

## 9.5 Thread State and the Global Interpreter Lock

The Python interpreter is not fully thread-safe. In order to support multi-threaded Python programs, there’s a global lock, called the global interpreter lock or GIL, that must be held by the current thread before it can safely access Python objects. Without the lock, even the simplest operations could cause problems in a multi-threaded program: for example, when two threads simultaneously increment the reference count of the same object, the reference count could end up being incremented only once instead of twice.

Therefore, the rule exists that only the thread that has acquired the GIL may operate on Python objects or call Python/C API functions. In order to emulate concurrency of execution, the interpreter regularly tries to switch threads (see sys.setswitchinterval()). The lock is also released around potentially blocking I/O operations like reading or writing a file, so that other Python threads can run in the meantime.

The Python interpreter keeps some thread-specific bookkeeping information inside a data structure called PyThreadState. There’s also one global variable pointing to the current PyThreadState: it can be retrieved using PyThreadState\_Get().

## 9.5.1 Releasing the GIL from extension code

Most extension code manipulating the GIL has the following simple structure:

```txt
Save the thread state in a local variable.
Release the global interpreter lock.
... Do some blocking I/O operation ...
Reacquire the global interpreter lock.
Restore the thread state from the local variable.
```

This is so common that a pair of macros exists to simplify it:

```txt
Py_BEGIN_ALLOW_THREADS
... Do some blocking I/O operation ...
Py_END_ALLOW_THREADS
```

The Py\_BEGIN\_ALLOW\_THREADS macro opens a new block and declares a hidden local variable; the Py\_END\_ALLOW\_THREADS macro closes the block.

The block above expands to the following code:

```matlab
PyThreadState *_save;

_save = PyEval_SaveThread();
... Do some blocking I/O operation ...
PyEval_RestoreThread(_save);
```

Here is how these functions work: the global interpreter lock is used to protect the pointer to the current thread state. When releasing the lock and saving the thread state, the current thread state pointer must be retrieved before the lock is released (since another thread could immediately acquire the lock and store its own thread state in the global variable). Conversely, when acquiring the lock and restoring the thread state, the lock must be acquired before storing the thread state pointer.

**Note:** Calling system I/O functions is the most common use case for releasing the GIL, but it can also be useful before calling long-running computations which don’t need access to Python objects, such as compression or cryptographic functions operating over memory buffers. For example, the standard zlib and hashlib modules release the GIL when compressing or hashing data.

## 9.5.2 Non-Python created threads

When threads are created using the dedicated Python APIs (such as the threading module), a thread state is automatically associated to them and the code showed above is therefore correct. However, when threads are created from C (for example by a third-party library with its own thread management), they don’t hold the GIL, nor is there a thread state structure for them.

If you need to call Python code from these threads (often this will be part of a callback API provided by the aforementioned third-party library), you must first register these threads with the interpreter by creating a thread state data structure, then acquiring the GIL, and finally storing their thread state pointer, before you can start using the Python/C API. When you are done, you should reset the thread state pointer, release the GIL, and finally free the thread state data structure.

The PyGILState\_Ensure() and PyGILState\_Release() functions do all of the above automatically. The typical idiom for calling into Python from a C thread is:

```c
PyGILState_STATE gstate;
gstate = PyGILState_Ensure();

/* Perform Python actions here. */
result = CallSomeFunction();
/* evaluate result or handle exception */

/* Release the thread. No Python API allowed beyond this point. */
PyGILState_Release(gstate);
```

Note that the PyGILState\_\* functions assume there is only one global interpreter (created automatically by Py\_Initialize()). Python supports the creation of additional interpreters (using Py\_NewInterpreter()), but mixing multiple interpreters and the PyGILState\_\* API is unsupported.

## 9.5.3 Cautions about fork()

Another important thing to note about threads is their behaviour in the face of the C fork() call. On most systems with fork(), after a process forks only the thread that issued the fork will exist. This has a concrete impact both on how locks must be handled and on all stored state in CPython’s runtime.

The fact that only the “current” thread remains means any locks held by other threads will never be released. Python solves this for os.fork() by acquiring the locks it uses internally before the fork, and releasing them afterwards. In addition, it resets any lock-objects in the child. When extending or embedding Python, there is no way to inform Python of additional (non-Python) locks that need to be acquired before or reset after a fork. OS facilities such as pthread\_atfork() would need to be used to accomplish the same thing. Additionally, when extending or embedding Python, calling fork() directly rather than through os.fork() (and returning to or calling into Python) may result in a deadlock by one of Python’s internal locks being held by a thread that is defunct after the fork. PyOS\_AfterFork\_Child() tries to reset the necessary locks, but is not always able to.

The fact that all other threads go away also means that CPython’s runtime state there must be cleaned up properly, which os.fork() does. This means finalizing all other PyThreadState objects belonging to the current interpreter and all other PyInterpreterState objects. Due to this and the special nature of the “main” interpreter, fork() should only be called in that interpreter’s “main” thread, where the CPython global runtime was originally initialized. The only exception is if exec() will be called immediately after.

## 9.5.4 High-level API

These are the most commonly used types and functions when writing C extension code, or when embedding the Python interpreter:

## type PyInterpreterState

Part of the Limited API (as an opaque struct). This data structure represents the state shared by a number of cooperating threads. Threads belonging to the same interpreter share their module administration and a few other internal items. There are no public members in this structure.

Threads belonging to different interpreters initially share nothing, except process state like available memory, open file descriptors and such. The global interpreter lock is also shared by all threads, regardless of to which interpreter they belong.

## type PyThreadState

Part of the Limited API (as an opaque struct). This data structure represents the state of a single thread. The only public data member is interp (PyInterpreterState\*), which points to this thread’s interpreter state.

## void PyEval\_InitThreads()

Part of the Stable ABI. Deprecated function which does nothing.

In Python 3.6 and older, this function created the GIL if it didn’t exist.

Changed in version 3.9: The function now does nothing.

Changed in version 3.7: This function is now called by Py\_Initialize(), so you don’t have to call it yourself anymore.

Changed in version 3.2: This function cannot be called before Py\_Initialize() anymore.

Deprecated since version 3.9, will be removed in version 3.11.

## int PyEval\_ThreadsInitialized()

Part of the Stable ABI. Returns a non-zero value if PyEval\_InitThreads() has been called. This function can be called without holding the GIL, and therefore can be used to avoid calls to the locking API when running single-threaded.

Changed in version 3.7: The GIL is now initialized by Py\_Initialize()

Deprecated since version 3.9, will be removed in version 3.11.

## PyThreadState \*PyEval\_SaveThread()

Part of the Stable ABI. Release the global interpreter lock (if it has been created) and reset the thread state to NULL, returning the previous thread state (which is not NULL). If the lock has been created, the current thread must have acquired it.

## void PyEval\_RestoreThread(PyThreadState \*tstate)

Part of the Stable ABI. Acquire the global interpreter lock (if it has been created) and set the thread state to tstate, which must not be NULL. If the lock has been created, the current thread must not have acquired it, otherwise deadlock ensues.

**Note:** Calling this function from a thread when the runtime is finalizing will terminate the thread, even if the thread was not created by Python. You can use \_Py\_IsFinalizing() or sys.is\_finalizing() to check if the interpreter is in process of being finalized before calling this function to avoid unwanted termination.

## PyThreadState \*PyThreadState\_Get()

Part of the Stable ABI. Return the current thread state. The global interpreter lock must be held. When the current thread state is NULL, this issues a fatal error (so that the caller needn’t check for NULL).

## PyThreadState \*PyThreadState\_Swap(PyThreadState \*tstate)

Part of the Stable ABI. Swap the current thread state with the thread state given by the argument tstate, which may be NULL. The global interpreter lock must be held and is not released.

The following functions use thread-local storage, and are not compatible with sub-interpreters:

## PyGILState\_STATE PyGILState\_Ensure()

Part of the Stable ABI. Ensure that the current thread is ready to call the Python C API regardless of the current state of Python, or of the global interpreter lock. This may be called as many times as desired by a thread as long as each call is matched with a call to PyGILState\_Release(). In general, other threadrelated APIs may be used between PyGILState\_Ensure() and PyGILState\_Release() calls as long as the thread state is restored to its previous state before the Release(). For example, normal usage of the Py\_BEGIN\_ALLOW\_THREADS and Py\_END\_ALLOW\_THREADS macros is acceptable.

The return value is an opaque “handle” to the thread state when PyGILState\_Ensure() was called, and must be passed to PyGILState\_Release() to ensure Python is left in the same state. Even though recursive calls are allowed, these handles cannot be shared - each unique call to PyGILState\_Ensure() must save the handle for its call to PyGILState\_Release().

When the function returns, the current thread will hold the GIL and be able to call arbitrary Python code. Failure is a fatal error.

**Note:** Calling this function from a thread when the runtime is finalizing will terminate the thread, even if the thread was not created by Python. You can use \_Py\_IsFinalizing() or sys.is\_finalizing() to check if the interpreter is in process of being finalized before calling this function to avoid unwanted termination.

## void PyGILState\_Release(PyGILState\_STATE)

Part of the Stable ABI. Release any resources previously acquired. After this call, Python’s state will be the same as it was prior to the corresponding PyGILState\_Ensure() call (but generally this state will be unknown to the caller, hence the use of the GILState API).

Every call to PyGILState\_Ensure() must be matched by a call to PyGILState\_Release() on the same thread.

## PyThreadState \*PyGILState\_GetThisThreadState()

Part of the Stable ABI. Get the current thread state for this thread. May return NULL if no GILState API has been used on the current thread. Note that the main thread always has such a thread-state, even if no auto-thread-state call has been made on the main thread. This is mainly a helper/diagnostic function.

## int PyGILState\_Check()

Return 1 if the current thread is holding the GIL and 0 otherwise. This function can be called from any thread

at any time. Only if it has had its Python thread state initialized and currently is holding the GIL will it return 1. This is mainly a helper/diagnostic function. It can be useful for example in callback contexts or memory allocation functions when knowing that the GIL is locked can allow the caller to perform sensitive actions or otherwise behave differently.

New in version 3.4.

The following macros are normally used without a trailing semicolon; look for example usage in the Python source distribution.

## Py\_BEGIN\_ALLOW\_THREADS

Part of the Stable ABI. This macro expands to { PyThreadState \*\_save; \_save = PyEval\_SaveThread();. Note that it contains an opening brace; it must be matched with a following Py\_END\_ALLOW\_THREADS macro. See above for further discussion of this macro.

## Py\_END\_ALLOW\_THREADS

Part of the Stable ABI. This macro expands to PyEval\_RestoreThread(\_save); }. Note that it contains a closing brace; it must be matched with an earlier Py\_BEGIN\_ALLOW\_THREADS macro. See above for further discussion of this macro.

## Py\_BLOCK\_THREADS

Part of the Stable ABI. This macro expands to PyEval\_RestoreThread(\_save);: it is equivalent to Py\_END\_ALLOW\_THREADS without the closing brace.

## Py\_UNBLOCK\_THREADS

Part of the Stable ABI. This macro expands to \_save = PyEval\_SaveThread();: it is equivalent to Py\_BEGIN\_ALLOW\_THREADS without the opening brace and variable declaration.

## 9.5.5 Low-level API

All of the following functions must be called after Py\_Initialize().

Changed in version 3.7: Py\_Initialize() now initializes the GIL.

## PyInterpreterState \*PyInterpreterState\_New()

Part of the Stable ABI. Create a new interpreter state object. The global interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function.

Raises an auditing event cpython.PyInterpreterState\_New with no arguments.

## void PyInterpreterState\_Clear(PyInterpreterState \*interp)

Part of the Stable ABI. Reset all information in an interpreter state object. The global interpreter lock must be held.

Raises an auditing event cpython.PyInterpreterState\_Clear with no arguments.

## void PyInterpreterState\_Delete(PyInterpreterState \*interp)

Part of the Stable ABI. Destroy an interpreter state object. The global interpreter lock need not be held. The interpreter state must have been reset with a previous call to PyInterpreterState\_Clear().

## PyThreadState \*PyThreadState\_New(PyInterpreterState \*interp)

Part of the Stable ABI. Create a new thread state object belonging to the given interpreter object. The global interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function.

## void PyThreadState\_Clear(PyThreadState \*tstate)

Part of the Stable ABI. Reset all information in a thread state object. The global interpreter lock must be held.

Changed in version 3.9: This function now calls the PyThreadState.on\_delete callback. Previously, that happened in PyThreadState\_Delete().

## void PyThreadState\_Delete(PyThreadState \*tstate)

Part of the Stable ABI. Destroy a thread state object. The global interpreter lock need not be held. The thread state must have been reset with a previous call to PyThreadState\_Clear().

void **PyThreadState\_DeleteCurrent**(void) Destroy the current thread state and release the global interpreter lock. Like PyThreadState\_Delete(), the global interpreter lock need not be held. The thread state must have been reset with a previous call to PyThreadState\_Clear().

PyFrameObject \***PyThreadState\_GetFrame**(PyThreadState \*tstate) Part of the Stable ABI since version 3.10. Get the current frame of the Python thread state tstate. Return a strong reference. Return NULL if no frame is currently executing. See also PyEval\_GetFrame(). tstate must not be NULL. New in version 3.9.

uint64\_t **PyThreadState\_GetID**(PyThreadState \*tstate) Part of the Stable ABI since version 3.10. Get the unique thread state identifier of the Python thread state tstate. tstate must not be NULL. New in version 3.9.

PyInterpreterState \***PyThreadState\_GetInterpreter**(PyThreadState \*tstate) Part of the Stable ABI since version 3.10. Get the interpreter of the Python thread state tstate. tstate must not be NULL. New in version 3.9.

PyInterpreterState \***PyInterpreterState\_Get**(void) Part of the Stable ABI since version 3.9. Get the current interpreter. Issue a fatal error if there no current Python thread state or no current interpreter. It cannot return NULL. The caller must hold the GIL. New in version 3.9.

int64\_t **PyInterpreterState\_GetID**(PyInterpreterState \*interp) Part of the Stable ABI since version 3.7. Return the interpreter’s unique ID. If there was any error in doing so then -1 is returned and an error is set. The caller must hold the GIL. New in version 3.7.

PyObject \***PyInterpreterState\_GetDict**(PyInterpreterState \*interp) Part of the Stable ABI since version 3.8. Return a dictionary in which interpreter-specific data may be stored. If this function returns NULL then no exception has been raised and the caller should assume no interpreterspecific dict is available. This is not a replacement for PyModule\_GetState(), which extensions should use to store interpreterspecific state information. New in version 3.8.

**typedef** PyObject \*(\***\_PyFrameEvalFunction**)(PyThreadState \*tstate, PyFrameObject \*frame, int throwflag) Type of a frame evaluation function. The throwflag parameter is used by the throw() method of generators: if non-zero, handle the current exception. Changed in version 3.9: The function now takes a tstate parameter.

\_PyFrameEvalFunction **\_PyInterpreterState\_GetEvalFrameFunc**(PyInterpreterState \*interp) Get the frame evaluation function. See the [**PEP 523**](https://www.python.org/dev/peps/pep-0523) “Adding a frame evaluation API to CPython”. New in version 3.9.

void **\_PyInterpreterState\_SetEvalFrameFunc**(PyInterpreterState \*interp, \_PyFrameEvalFunction eval\_frame)

Set the frame evaluation function.

See the [**PEP 523**](https://www.python.org/dev/peps/pep-0523) “Adding a frame evaluation API to CPython”.

New in version 3.9.

## PyObject \*PyThreadState\_GetDict()

Return value: Borrowed reference. Part of the Stable ABI. Return a dictionary in which extensions can store thread-specific state information. Each extension should use a unique key to use to store state in the dictionary. It is okay to call this function when no current thread state is available. If this function returns NULL, no exception has been raised and the caller should assume no current thread state is available.

## int PyThreadState\_SetAsyncExc(unsigned long id, PyObject \*exc)

Part of the Stable ABI. Asynchronously raise an exception in a thread. The id argument is the thread id of the target thread; exc is the exception object to be raised. This function does not steal any references to exc. To prevent naive misuse, you must write your own C extension to call this. Must be called with the GIL held. Returns the number of thread states modified; this is normally one, but will be zero if the thread id isn’t found. If exc is NULL, the pending exception (if any) for the thread is cleared. This raises no exceptions.

Changed in version 3.7: The type of the id parameter changed from long to unsigned long.

## void PyEval\_AcquireThread(PyThreadState \*tstate)

Part of the Stable ABI. Acquire the global interpreter lock and set the current thread state to tstate, which must not be NULL. The lock must have been created earlier. If this thread already has the lock, deadlock ensues.

**Note:** Calling this function from a thread when the runtime is finalizing will terminate the thread, even if the thread was not created by Python. You can use \_Py\_IsFinalizing() or sys.is\_finalizing() to check if the interpreter is in process of being finalized before calling this function to avoid unwanted termination.

Changed in version 3.8: Updated to be consistent with PyEval\_RestoreThread(), Py\_END\_ALLOW\_THREADS(), and PyGILState\_Ensure(), and terminate the current thread if called while the interpreter is finalizing.

PyEval\_RestoreThread() is a higher-level function which is always available (even when threads have not been initialized).

## void PyEval\_ReleaseThread(PyThreadState \*tstate)

Part of the Stable ABI. Reset the current thread state to NULL and release the global interpreter lock. The lock must have been created earlier and must be held by the current thread. The tstate argument, which must not be NULL, is only used to check that it represents the current thread state — if it isn’t, a fatal error is reported.

PyEval\_SaveThread() is a higher-level function which is always available (even when threads have not been initialized).

## void PyEval\_AcquireLock()

Part of the Stable ABI. Acquire the global interpreter lock. The lock must have been created earlier. If this thread already has the lock, a deadlock ensues.

Deprecated since version 3.2: This function does not update the current thread state. Please use PyEval\_RestoreThread() or PyEval\_AcquireThread() instead.

**Note:** Calling this function from a thread when the runtime is finalizing will terminate the thread, even if the thread was not created by Python. You can use \_Py\_IsFinalizing() or sys.is\_finalizing() to check if the interpreter is in process of being finalized before calling this function to avoid unwanted termination.

Changed in version 3.8: Updated to be consistent with PyEval\_RestoreThread(), Py\_END\_ALLOW\_THREADS(), and PyGILState\_Ensure(), and terminate the current thread if called while the interpreter is finalizing.

## void PyEval\_ReleaseLock()

Part of the Stable ABI. Release the global interpreter lock. The lock must have been created earlier.

Deprecated since version 3.2: This function does not update the current thread state. Please use PyEval\_SaveThread() or PyEval\_ReleaseThread() instead.

## 9.6 Sub-interpreter support

While in most uses, you will only embed a single Python interpreter, there are cases where you need to create several independent interpreters in the same process and perhaps even in the same thread. Sub-interpreters allow you to do that.

The “main” interpreter is the first one created when the runtime initializes. It is usually the only Python interpreter in a process. Unlike sub-interpreters, the main interpreter has unique process-global responsibilities like signal handling. It is also responsible for execution during runtime initialization and is usually the active interpreter during runtime finalization. The PyInterpreterState\_Main() function returns a pointer to its state.

You can switch between sub-interpreters using the PyThreadState\_Swap() function. You can create and destroy them using the following functions:

## PyThreadState \*Py\_NewInterpreter()

Part of the Stable ABI. Create a new sub-interpreter. This is an (almost) totally separate environment for the execution of Python code. In particular, the new interpreter has separate, independent versions of all imported modules, including the fundamental modules builtins, \_\_main\_\_ and sys. The table of loaded modules (sys.modules) and the module search path (sys.path) are also separate. The new environment has no sys.argv variable. It has new standard I/O stream file objects sys.stdin, sys.stdout and sys. stderr (however these refer to the same underlying file descriptors).

The return value points to the first thread state created in the new sub-interpreter. This thread state is made in the current thread state. Note that no actual thread is created; see the discussion of thread states below. If creation of the new interpreter is unsuccessful, NULL is returned; no exception is set since the exception state is stored in the current thread state and there may not be a current thread state. (Like all other Python/C API functions, the global interpreter lock must be held before calling this function and is still held when it returns; however, unlike most other Python/C API functions, there needn’t be a current thread state on entry.)

Extension modules are shared between (sub-)interpreters as follows:

• For modules using multi-phase initialization, e.g. PyModule\_FromDefAndSpec(), a separate module object is created and initialized for each interpreter. Only C-level static and global variables are shared between these module objects.

• For modules using single-phase initialization, e.g. PyModule\_Create(), the first time a particular extension is imported, it is initialized normally, and a (shallow) copy of its module’s dictionary is squirreled away. When the same extension is imported by another (sub-)interpreter, a new module is initialized and filled with the contents of this copy; the extension’s init function is not called. Objects in the module’s dictionary thus end up shared across (sub-)interpreters, which might cause unwanted behavior (see Bugs and caveats below).

Note that this is different from what happens when an extension is imported after the interpreter has been completely re-initialized by calling Py\_FinalizeEx() and Py\_Initialize(); in that case, the extension’s initmodule function is called again. As with multi-phase initialization, this means that only C-level static and global variables are shared between these modules.

## void Py\_EndInterpreter(PyThreadState \*tstate)

Part of the Stable ABI. Destroy the (sub-)interpreter represented by the given thread state. The given thread state must be the current thread state. See the discussion of thread states below. When the call returns, the current thread state is NULL. All thread states associated with this interpreter are destroyed. (The global interpreter lock must be held before calling this function and is still held when it returns.) Py\_FinalizeEx() will destroy all sub-interpreters that haven’t been explicitly destroyed at that point.

## 9.6.1 Bugs and caveats

Because sub-interpreters (and the main interpreter) are part of the same process, the insulation between them isn’t perfect — for example, using low-level file operations like os.close() they can (accidentally or maliciously) affect each other’s open files. Because of the way extensions are shared between (sub-)interpreters, some extensions may not work properly; this is especially likely when using single-phase initialization or (static) global variables. It is possible to insert objects created in one sub-interpreter into a namespace of another (sub-)interpreter; this should be avoided if possible.

Special care should be taken to avoid sharing user-defined functions, methods, instances or classes between subinterpreters, since import operations executed by such objects may affect the wrong (sub-)interpreter’s dictionary of loaded modules. It is equally important to avoid sharing objects from which the above are reachable.

Also note that combining this functionality with PyGILState\_\* APIs is delicate, because these APIs assume a bijection between Python thread states and OS-level threads, an assumption broken by the presence of sub-interpreters. It is highly recommended that you don’t switch sub-interpreters between a pair of matching PyGILState\_Ensure() and PyGILState\_Release() calls. Furthermore, extensions (such as ctypes) using these APIs to allow calling of Python code from non-Python created threads will probably be broken when using sub-interpreters.

## 9.7 Asynchronous Notifications

A mechanism is provided to make asynchronous notifications to the main interpreter thread. These notifications take the form of a function pointer and a void pointer argument.

int **Py\_AddPendingCall**(int (\*func))void\*

, void \*arg Part of the Stable ABI. Schedule a function to be called from the main interpreter thread. On success, 0 is returned and func is queued for being called in the main thread. On failure, -1 is returned without setting any exception.

When successfully queued, func will be eventually called from the main interpreter thread with the argument arg. It will be called asynchronously with respect to normally running Python code, but with both these conditions met:

• on a bytecode boundary;

• with the main thread holding the global interpreter lock (func can therefore use the full C API).

func must return 0 on success, or -1 on failure with an exception set. func won’t be interrupted to perform another asynchronous notification recursively, but it can still be interrupted to switch threads if the global interpreter lock is released.

This function doesn’t need a current thread state to run, and it doesn’t need the global interpreter lock.

To call this function in a subinterpreter, the caller must hold the GIL. Otherwise, the function func can be scheduled to be called from the wrong interpreter.

**Warning:** This is a low-level function, only useful for very special cases. There is no guarantee that func will be called as quick as possible. If the main thread is busy executing a system call, func won’t be called before the system call returns. This function is generally **not** suitable for calling Python code from arbitrary C threads. Instead, use the PyGILState API.

Changed in version 3.9: If this function is called in a subinterpreter, the function func is now scheduled to be called from the subinterpreter, rather than being called from the main interpreter. Each subinterpreter now has its own list of scheduled calls.

New in version 3.1.

## 9.8 Profiling and Tracing

The Python interpreter provides some low-level support for attaching profiling and execution tracing facilities. These are used for profiling, debugging, and coverage analysis tools.

This C interface allows the profiling or tracing code to avoid the overhead of calling through Python-level callable objects, making a direct C function call instead. The essential attributes of the facility have not changed; the interface allows trace functions to be installed per-thread, and the basic events reported to the trace function are the same as had been reported to the Python-level trace functions in previous versions.

## typedef int (\*Py\_tracefunc)(PyObject \*obj, PyFrameObject \*frame, int what, PyObject \*arg)

The type of the trace function registered using PyEval\_SetProfile() and PyEval\_SetTrace(). The first parameter is the object passed to the registration function as obj, frame is the frame object to which the event pertains, what is one of the constants PyTrace\_CALL, PyTrace\_EXCEPTION, PyTrace\_LINE, PyTrace\_RETURN, PyTrace\_C\_CALL, PyTrace\_C\_EXCEPTION, PyTrace\_C\_RETURN, or PyTrace\_OPCODE, and arg depends on the value of what:

| Value of what | Meaning of arg |
| --- | --- |
| PyTrace_CALL | Always Py_None. |
| PyTrace_EXCEPTION | Exception information as returned by sys.exc_info(). |
| PyTrace_LINE | Always Py_None. |
| PyTrace_RETURN | Value being returned to the caller, or NULL if caused by an exception. |
| PyTrace_C_CALL | Function object being called. |
| PyTrace_C_EXCEPTION | Function object being called. |
| PyTrace_C_RETURN | Function object being called. |
| PyTrace_OPCODE | Always Py_None. |

## int PyTrace\_CALL

The value of the what parameter to a Py\_tracefunc function when a new call to a function or method is being reported, or a new entry into a generator. Note that the creation of the iterator for a generator function is not reported as there is no control transfer to the Python bytecode in the corresponding frame.

## int PyTrace\_EXCEPTION

The value of the what parameter to a Py\_tracefunc function when an exception has been raised. The callback function is called with this value for what when after any bytecode is processed after which the exception becomes set within the frame being executed. The effect of this is that as exception propagation causes the Python stack to unwind, the callback is called upon return to each frame as the exception propagates. Only trace functions receives these events; they are not needed by the profiler.

## int PyTrace\_LINE

The value passed as the what parameter to a Py\_tracefunc function (but not a profiling function) when a line-number event is being reported. It may be disabled for a frame by setting f\_trace\_lines to 0 on that frame.

## int PyTrace\_RETURN

The value for the what parameter to Py\_tracefunc functions when a call is about to return.

## int PyTrace\_C\_CALL

The value for the what parameter to Py\_tracefunc functions when a C function is about to be called.

## int PyTrace\_C\_EXCEPTION

The value for the what parameter to Py\_tracefunc functions when a C function has raised an exception.

## int PyTrace\_C\_RETURN

The value for the what parameter to Py\_tracefunc functions when a C function has returned.

## int PyTrace\_OPCODE

The value for the what parameter to Py\_tracefunc functions (but not profiling functions) when a new opcode is about to be executed. This event is not emitted by default: it must be explicitly requested by setting f\_trace\_opcodes to 1 on the frame.

void **PyEval\_SetProfile**(Py\_tracefunc func, PyObject \*obj)

Set the profiler function to func. The obj parameter is passed to the function as its first parameter, and may be any Python object, or NULL. If the profile function needs to maintain state, using a different value for obj for each thread provides a convenient and thread-safe place to store it. The profile function is called for all monitored events except PyTrace\_LINE PyTrace\_OPCODE and PyTrace\_EXCEPTION.

The caller must hold the GIL.

void **PyEval\_SetTrace**(Py\_tracefunc func, PyObject \*obj)

Set the tracing function to func. This is similar to PyEval\_SetProfile(), except the tracing function does receive line-number events and per-opcode events, but does not receive any event related to C function objects being called. Any trace function registered using PyEval\_SetTrace() will not receive PyTrace\_C\_CALL, PyTrace\_C\_EXCEPTION or PyTrace\_C\_RETURN as a value for the what parameter.

The caller must hold the GIL.

## 9.9 Advanced Debugger Support

These functions are only intended to be used by advanced debugging tools.

PyInterpreterState \***PyInterpreterState\_Head**()

Return the interpreter state object at the head of the list of all such objects.

PyInterpreterState \***PyInterpreterState\_Main**()

Return the main interpreter state object.

PyInterpreterState \***PyInterpreterState\_Next**(PyInterpreterState \*interp) Return the next interpreter state object after interp from the list of all such objects.

PyThreadState \***PyInterpreterState\_ThreadHead**(PyInterpreterState \*interp)

Return the pointer to the first PyThreadState object in the list of threads associated with the interpreter interp.

PyThreadState \***PyThreadState\_Next**(PyThreadState \*tstate)

Return the next thread state object after tstate from the list of all such objects belonging to the same PyInterpreterState object.

## 9.10 Thread Local Storage Support

The Python interpreter provides low-level support for thread-local storage (TLS) which wraps the underlying native TLS implementation to support the Python-level thread local storage API (threading.local). The CPython C level APIs are similar to those offered by pthreads and Windows: use a thread key and functions to associate a void\* value per thread.

The GIL does not need to be held when calling these functions; they supply their own locking.

Note that Python.h does not include the declaration of the TLS APIs, you need to include pythread.h to use thread-local storage.

**Note:** None of these API functions handle memory management on behalf of the void\* values. You need to allocate and deallocate them yourself. If the void\* values happen to be PyObject\*, these functions don’t do refcount operations on them either.

## 9.10.1 Thread Specific Storage (TSS) API

TSS API is introduced to supersede the use of the existing TLS API within the CPython interpreter. This API uses a new type Py\_tss\_t instead of int to represent thread keys.

New in version 3.7.

## See also:

“A New C-API for Thread-Local Storage in CPython” ([**PEP 539**](https://www.python.org/dev/peps/pep-0539))

## type Py\_tss\_t

This data structure represents the state of a thread key, the definition of which may depend on the underlying TLS implementation, and it has an internal field representing the key’s initialization state. There are no public members in this structure.

When Py \_LIMITED\_API is not defined, static allocation of this type by Py\_tss\_NEEDS\_INIT is allowed.

## Py\_tss\_NEEDS\_INIT

This macro expands to the initializer for Py\_tss\_t variables. Note that this macro won’t be defined with Py\_ \_LIMITED\_API.

## Dynamic Allocation

Dynamic allocation of the Py\_tss\_t, required in extension modules built with Py \_LIMITED\_API, where static allocation of this type is not possible due to its implementation being opaque at build time.

## Py\_tss\_t \*PyThread\_tss\_alloc()

Part of the Stable ABI since version 3.7. Return a value which is the same state as a value initialized with Py\_tss\_NEEDS\_INIT, or NULL in the case of dynamic allocation failure.

## void PyThread\_tss\_free(Py\_tss\_t \*key)

Part of the Stable ABI since version 3.7. Free the given key allocated by PyThread\_tss\_alloc(), after first calling PyThread\_tss\_delete() to ensure any associated thread locals have been unassigned. This is a no-op if the key argument is NULL.

**Note:** A freed key becomes a dangling pointer. You should reset the key to NULL.

## Methods

The parameter key of these functions must not be NULL. Moreover, the behaviors of PyThread\_tss\_set() and PyThread\_tss\_get() are undefined if the given Py\_tss\_t has not been initialized by PyThread\_tss\_create().

int **PyThread\_tss\_is\_created** (Py\_tss\_t \*key)

Part of the Stable ABI since version 3.7. Return a non-zero value if the given Py\_tss\_t has been initialized by PyThread\_tss\_create().

## int PyThread\_tss\_create (Py\_ \_tss\_ \_t \*key)

Part of the Stable ABI since version 3.7. Return a zero value on successful initialization of a TSS key. The behavior is undefined if the value pointed to by the key argument is not initialized by Py\_tss\_NEEDS\_INIT. This function can be called repeatedly on the same key – calling it on an already initialized key is a no-op and immediately returns success.

## void PyThread\_tss\_delete (Py\_tss\_t \*key)

Part of the Stable ABI since version 3.7. Destroy a TSS key to forget the values associated with the key across all threads, and change the key’s initialization state to uninitialized. A destroyed key is able to be initialized again by PyThread\_tss\_create(). This function can be called repeatedly on the same key – calling it on an already destroyed key is a no-op.

int **PyThread\_tss\_set**(Py\_tss\_t \*key, void \*value) Part of the Stable ABI since version 3.7. Return a zero value to indicate successfully associating a void\* value with a TSS key in the current thread. Each thread has a distinct mapping of the key to a void\* value.

void \***PyThread\_tss\_get**(Py\_tss\_t \*key)

Part of the Stable ABI since version 3.7. Return the void\* value associated with a TSS key in the current thread. This returns NULL if no value is associated with the key in the current thread.

## 9.10.2 Thread Local Storage (TLS) API

Deprecated since version 3.7: This API is superseded by Thread Specific Storage (TSS) API.

**Note:** This version of the API does not support platforms where the native TLS key is defined in a way that cannot be safely cast to int. On such platforms, PyThread\_create\_key() will return immediately with a failure status, and the other TLS functions will all be no-ops on such platforms.

Due to the compatibility problem noted above, this version of the API should not be used in new code.

int **PyThread\_create\_key**() Part of the Stable ABI.

void **PyThread\_delete\_key**(int key) Part of the Stable ABI.

int **PyThread\_set\_key\_value**(int key, void \*value) Part of the Stable ABI.

void \***PyThread\_get\_key\_value**(int key) Part of the Stable ABI.

void **PyThread\_delete\_key\_value**(int key) Part of the Stable ABI.

void **PyThread\_ReInitTLS**() Part of the Stable ABI.

# PYTHON INITIALIZATION CONFIGURATION

## New in version 3.8.

Python can be initialized with Py\_InitializeFromConfig() and the PyConfig structure. It can be preinitialized with Py\_PreInitialize() and the PyPreConfig structure.

There are two kinds of configuration:

• The Python Configuration can be used to build a customized Python which behaves as the regular Python. For example, environment variables and command line arguments are used to configure Python.

• The Isolated Configuration can be used to embed Python into an application. It isolates Python from the system. For example, environment variables are ignored, the LC\_CTYPE locale is left unchanged and no signal handler is registered.

The Py\_RunMain() function can be used to write a customized Python program.

See also Initialization, Finalization, and Threads.

## See also:

[**PEP 587**](https://www.python.org/dev/peps/pep-0587) “Python Initialization Configuration”.

## 10.1 Example

Example of customized Python always running in isolated mode:

```c
int main(int argc, char **argv)
{
    PyStatus status;

    PyConfig config;
    PyConfig_InitPythonConfig(&config);
    config.isolated = 1;

    /* Decode command line arguments.
        Implicitly preinitialize Python (in isolated mode). */
    status = PyConfig_SetBytesArgv(&config, argc, argv);
    if (PyStatus_Exception(status)) {
        goto exception;
    }

    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    PyConfig_Clear(&config);

    return Py_RunMain();
```

(continues on next page)

(continued from previous page)

```txt
exception:
    PyConfig_Clear(&config);
    if (PyStatus_IsExit(status)) {
        return status.exitcode;
    }
    /* Display the error message and exit the process with
       non-zero exit code */
    Py_ExitStatusException(status);
}
```

## 10.2 PyWideStringList

## type PyWideStringList

List of wchar\_t\* strings.

If length is non-zero, items must be non-NULL and all strings must be non-NULL.

Methods:

PyStatus **PyWideStringList\_Append**(PyWideStringList \*list, **const** wchar\_t \*item) Append item to list.

Python must be preinitialized to call this function.

PyStatus **PyWideStringList\_Insert**(PyWideStringList \*list, Py\_ssize\_t index, **const** wchar\_t

Insert item into list at index.

If index is greater than or equal to list length, append item to list.

index must be greater than or equal to 0.

Python must be preinitialized to call this function.

Structure fields:

```txt
Py_ssize_t length
    List length.
wchar_t **items
    List items.
```

## 10.3 PyStatus

## type PyStatus

Structure to store an initialization function status: success, error or exit.

For an error, it can store the C function name which created the error.

Structure fields:

int **exitcode** Exit code. Argument passed to exit().

**const** char \***err\_msg** Error message.

**const** char \***func** Name of the function which created an error, can be NULL.

Functions to create a status:

```txt
PyStatus PyStatus_Ok (void)
    Success.

PyStatus PyStatus_Error (const char *err_msg)
    Initialization error with a message.
    err_msg must not be NULL.

PyStatus PyStatus_NoMemory (void)
    Memory allocation failure (out of memory).

PyStatus PyStatus_Exit (int exitcode)
    Exit Python with the specified exit code.

Functions to handle a status:
int PyStatus_Exception (PyStatus status)
    Is the status an error or an exit?   If true, the exception must be handled; by calling
    Py_ExitStatusException() for example.

int PyStatus_IsError (PyStatus status)
    Is the result an error?

int PyStatus_IsExit (PyStatus status)
    Is the result an exit?

void Py_ExitStatusException (PyStatus status)
    Call exit (exitcode) if status is an exit. Print the error message and exit with a non-zero exit code
    if status is an error. Must only be called if PyStatus_Exception(status) is non-zero.
```

**Note:** Internally, Python uses macros which set PyStatus.func, whereas functions to create a status set func to NULL.

Example:

```c
PyStatus alloc(void **ptr, size_t size)
{
    *ptr = PyMem_RawMalloc(size);
    if (*ptr == NULL) {
        return PyStatus_NoMemory();
    }
    return PyStatus_Ok();
}

int main(int argc, char **argv)
{
    void *ptr;
    PyStatus status = alloc(&ptr, 16);
    if (PyStatus_Exception(status)) {
        Py_ExitStatusException(status);
    }
    PyMem_Free(ptr);
    return 0;
}
```

## 10.4 PyPreConfig

## type PyPreConfig

Structure used to preinitialize Python.

Function to initialize a preconfiguration:

void **PyPreConfig\_InitPythonConfig**(PyPreConfig \*preconfig)

Initialize the preconfiguration with Python Configuration.

void **PyPreConfig\_InitIsolatedConfig**(PyPreConfig \*preconfig) Initialize the preconfiguration with Isolated Configuration.

Structure fields:

## int allocator

Name of the Python memory allocators:

• PYMEM\_ALLOCATOR\_NOT\_SET (0): don’t change memory allocators (use defaults).

• PYMEM\_ALLOCATOR\_DEFAULT (1): default memory allocators.

• PYMEM\_ALLOCATOR\_DEBUG (2): default memory allocators with debug hooks.

• PYMEM\_ALLOCATOR\_MALLOC (3): use malloc() of the C library.

• PYMEM\_ALLOCATOR\_MALLOC\_DEBUG (4): force usage of malloc() with debug hooks.

• PYMEM\_ALLOCATOR\_PYMALLOC (5): Python pymalloc memory allocator.

• PYMEM\_ALLOCATOR\_PYMALLOC\_DEBUG (6): Python pymalloc memory allocator with debug hooks.

PYMEM\_ALLOCATOR\_PYMALLOC and PYMEM\_ALLOCATOR\_PYMALLOC\_DEBUG are not supported if Python is configured using --without-pymalloc.

See Memory Management.

Default: PYMEM\_ALLOCATOR\_NOT\_SET.

## int configure\_locale

Set the LC\_CTYPE locale to the user preferred locale.

If equals to 0, set coerce\_c\_locale and coerce\_c\_locale\_warn members to 0.

See the locale encoding.

Default: 1 in Python config, 0 in isolated config.

## int coerce\_c\_locale

If equals to 2, coerce the C locale.

If equals to 1, read the LC\_CTYPE locale to decide if it should be coerced.

See the locale encoding.

Default: -1 in Python config, 0 in isolated config.

## int coerce\_c\_locale\_warn

If non-zero, emit a warning if the C locale is coerced.

Default: -1 in Python config, 0 in isolated config.

## int dev\_mode

If non-zero, enables the Python Development Mode: see PyConfig.dev\_mode.

Default: -1 in Python mode, 0 in isolated mode.

## int isolated

Isolated mode: see PyConfig.isolated.

Default: 0 in Python mode, 1 in isolated mode.

## int legacy\_windows\_fs\_encoding

## If non-zero:

• Set PyPreConfig.utf8\_mode to 0,

• Set PyConfig.filesystem\_encoding to "mbcs",

• Set PyConfig.filesystem\_errors to "replace".

Initialized the from PYTHONLEGACYWINDOWSFSENCODING environment variable value.

Only available on Windows. #ifdef MS\_WINDOWS macro can be used for Windows specific code.

Default: 0.

## int parse\_argv

If non-zero, Py\_PreInitializeFromArgs() and Py\_PreInitializeFromBytesArgs() parse their argv argument the same way the regular Python parses command line arguments: see Command Line Arguments.

Default: 1 in Python config, 0 in isolated config.

## int use\_environment

Use environment variables? See PyConfig.use\_environment.

Default: 1 in Python config and 0 in isolated config.

## int utf8\_mode

If non-zero, enable the Python UTF-8 Mode.

Set by the -X utf8 command line option and the PYTHONUTF8 environment variable.

Default: -1 in Python config and 0 in isolated config.

## 10.5 Preinitialize Python with PyPreConfig

The preinitialization of Python:

• Set the Python memory allocators (PyPreConfig.allocator)

• Configure the LC\_CTYPE locale (locale encoding)

• Set the Python UTF-8 Mode (PyPreConfig.utf8\_mode)

The current preconfiguration (PyPreConfig type) is stored in \_PyRuntime.preconfig.

Functions to preinitialize Python:

## PyStatus Py\_PreInitialize(const PyPreConfig \*preconfig)

Preinitialize Python from preconfig preconfiguration.

preconfig must not be NULL.

PyStatus **Py\_PreInitializeFromBytesArgs**(**const** PyPreConfig \*preconfig, int argc, char \***const** \*argv)

Preinitialize Python from preconfig preconfiguration.

Parse argv command line arguments (bytes strings) if parse\_argv of preconfig is non-zero.

preconfig must not be NULL.

## PyStatus Py\_PreInitializeFromArgs(const PyPreConfig \*preconfig, int argc, wchar\_t \*const

Preinitialize Python from preconfig preconfiguration.

Parse argv command line arguments (wide strings) if parse\_argv of preconfig is non-zero.

preconfig must not be NULL.

The caller is responsible to handle exceptions (error or exit) using PyStatus\_Exception() and Py\_ExitStatusException().

For Python Configuration (PyPreConfig\_InitPythonConfig()), if Python is initialized with command line arguments, the command line arguments must also be passed to preinitialize Python, since they have an effect on the pre-configuration like encodings. For example, the -X utf8 command line option enables the Python UTF-8 Mode.

PyMem\_SetAllocator() can be called after Py\_PreInitialize() and before Py\_InitializeFromConfig() to install a custom memory allocator. It can be called before Py\_PreInitialize() if PyPreConfig.allocator is set to PYMEM\_ALLOCATOR\_NOT\_SET.

Python memory allocation functions like PyMem\_RawMalloc() must not be used before the Python preinitialization, whereas calling directly malloc() and free() is always safe. Py\_DecodeLocale() must not be called before the Python preinitialization.

Example using the preinitialization to enable the Python UTF-8 Mode:

```c
PyStatus status;
PyPreConfig preconfig;
PyPreConfig_InitPythonConfig(&preconfig);

preconfig.utf8_mode = 1;

status = Py_PreInitialize(&preconfig);
if (PyStatus_Exception(status)) {
    Py_ExitStatusException(status);
}

/* at this point, Python speaks UTF-8 */

Py_Initialize();
/* ... use Python API here ... */
Py_Finalize();
```

## 10.6 PyConfig

## type PyConfig

```txt
e PyConfig
Structure containing most parameters to configure Python.
When done, the PyConfig_Clear() function must be used to release the configuration memory.
Structure methods:
void PyConfig_InitPythonConfig (PyConfig *config)
    Initialize configuration with the Python Configuration.
void PyConfig_InitIsolatedConfig (PyConfig *config)
    Initialize configuration with the Isolated Configuration.
PyStatus PyConfig_SetString (PyConfig *config, wchar_t *const *config_str, const wchar_t *str)
    Copy the wide character string str into *config_str.
    Preinitialize Python if needed.
PyStatus PyConfig_SetBytesString (PyConfig *config, wchar_t *const *config_str, const char *str)
    Decode str using Py_DecodeLocale() and set the result into *config_str.
    Preinitialize Python if needed.
PyStatus PyConfig_SetArgv (PyConfig *config, int argc, wchar_t *const *argv)
    Set command line arguments (argv member of config) from the argv list of wide character strings.
    Preinitialize Python if needed.
```

PyStatus **PyConfig\_SetBytesArgv**(PyConfig \*config, int argc, char \***const** \*argv) Set command line arguments (argv member of config) from the argv list of bytes strings. Decode bytes using Py\_DecodeLocale().

Preinitialize Python if needed.

## PyStatus PyConfig\_SetWideStringList(PyConfig \*config, PyWideStringList \*list, Py\_ssize\_t

Set the list of wide strings list to length and items.

Preinitialize Python if needed.

PyStatus **PyConfig\_Read**(PyConfig \*config) Read all Python configuration.

Fields which are already initialized are left unchanged.

The PyConfig\_Read() function only parses PyConfig.argv arguments once: PyConfig. parse\_argv is set to 2 after arguments are parsed. Since Python arguments are strippped from PyConfig.argv, parsing arguments twice would parse the application options as Python options.

Preinitialize Python if needed.

Changed in version 3.10: The PyConfig.argv arguments are now only parsed once, PyConfig. parse\_argv is set to 2 after arguments are parsed, and arguments are only parsed if PyConfig. parse\_argv equals 1.

## void PyConfig\_Clear(PyConfig \*config) Release configuration memory.

Most PyConfig methods preinitialize Python if needed. In that case, the Python preinitialization configuration (PyPreConfig) in based on the PyConfig. If configuration fields which are in common with PyPreConfig are tuned, they must be set before calling a PyConfig method:

• PyConfig.dev\_mode

• PyConfig.isolated

• PyConfig.parse\_argv

• PyConfig.use\_environment

Moreover, if PyConfig\_SetArgv() or PyConfig\_SetBytesArgv() is used, this method must be called before other methods, since the preinitialization configuration depends on command line arguments (if parse\_argv is non-zero).

The caller of these methods is responsible to handle exceptions (error or exit) using PyStatus\_Exception() and Py\_ExitStatusException().

Structure fields:

## PyWideStringList argv

Command line arguments: sys.argv.

Set parse\_argv to 1 to parse argv the same way the regular Python parses Python command line arguments and then to strip Python arguments from argv.

If argv is empty, an empty string is added to ensure that sys.argv always exists and is never empty.

Default: NULL.

See also the orig\_argv member.

## wchar\_t \*base\_exec\_prefix

sys.base\_exec\_prefix.

Default: NULL.

Part of the Python Path Configuration output.

## wchar\_t \*base\_executable

Python base executable: sys.\_base\_executable.

Set by the \_\_PYVENV\_LAUNCHER\_\_ environment variable.

Set from PyConfig.executable if NULL.

Default: NULL.

Part of the Python Path Configuration output.

## wchar\_t \*base\_prefix

sys.base\_prefix.

Default: NULL.

Part of the Python Path Configuration output.

## int buffered\_stdio

If equals to 0 and configure\_c\_stdio is non-zero, disable buffering on the C streams stdout and stderr.

Set to 0 by the -u command line option and the PYTHONUNBUFFERED environment variable.

stdin is always opened in buffered mode.

Default: 1.

## int bytes\_warning

If equals to 1, issue a warning when comparing bytes or bytearray with str, or comparing bytes with int.

If equal or greater to 2, raise a BytesWarning exception in these cases.

Incremented by the -b command line option.

Default: 0.

## int warn\_default\_encoding

If non-zero, emit a EncodingWarning warning when io.TextIOWrapper uses its default encoding. See io-encoding-warning for details.

Default: 0.

New in version 3.10.

## wchar\_t \*check\_hash\_pycs\_mode

Control the validation behavior of hash-based .pyc files: value of the --check-hash-based-pycs command line option.

Valid values:

• L"always": Hash the source file for invalidation regardless of value of the ‘check\_source’ flag.

• L"never": Assume that hash-based pycs always are valid.

• L"default": The ‘check\_source’ flag in hash-based pycs determines invalidation.

Default: L"default".

See also [**PEP 552**](https://www.python.org/dev/peps/pep-0552) “Deterministic pycs”.

## int configure\_c\_stdio

If non-zero, configure C standard streams:

• On Windows, set the binary mode (O\_BINARY) on stdin, stdout and stderr.

• If buffered\_stdio equals zero, disable buffering of stdin, stdout and stderr streams.

• If interactive is non-zero, enable stream buffering on stdin and stdout (only stdout on Windows).

Default: 1 in Python config, 0 in isolated config.

## int dev\_mode

If non-zero, enable the Python Development Mode.

Default: -1 in Python mode, 0 in isolated mode.

## int dump\_refs

Dump Python references?

If non-zero, dump all objects which are still alive at exit.

Set to 1 by the PYTHONDUMPREFS environment variable.

Need a special build of Python with the Py\_TRACE\_REFS macro defined: see the configure --with-trace-refs option.

Default: 0.

## wchar\_t \*exec\_prefix

The site-specific directory prefix where the platform-dependent Python files are installed: sys. exec\_prefix.

Default: NULL.

Part of the Python Path Configuration output.

## wchar\_t \*executable

The absolute path of the executable binary for the Python interpreter: sys.executable.

Default: NULL.

Part of the Python Path Configuration output.

## int faulthandler

Enable faulthandler?

If non-zero, call faulthandler.enable() at startup.

Set to 1 by -X faulthandler and the PYTHONFAULTHANDLER environment variable.

Default: -1 in Python mode, 0 in isolated mode.

## wchar\_t \*filesystem\_encoding

Filesystem encoding: sys.getfilesystemencoding().

On macOS, Android and VxWorks: use "utf-8" by default.

On Windows: use "utf-8" by default, or "mbcs" if legacy\_windows\_fs\_encoding of PyPreConfig is non-zero.

Default encoding on other platforms:

• "utf-8" if PyPreConfig.utf8\_mode is non-zero.

• "ascii" if Python detects that nl\_langinfo(CODESET) announces the ASCII encoding, whereas the mbstowcs() function decodes from a different encoding (usually Latin1).

• "utf-8" if nl\_langinfo(CODESET) returns an empty string.

• Otherwise, use the locale encoding: nl\_langinfo(CODESET) result.

At Python startup, the encoding name is normalized to the Python codec name. For example, "ANSI\_X3.4-1968" is replaced with "ascii".

See also the filesystem\_errors member.

## wchar\_t \*filesystem\_errors

Filesystem error handler: sys.getfilesystemencodeerrors().

On Windows: use "surrogatepass" by default, or "replace" if legacy\_windows\_fs\_encoding of PyPreConfig is non-zero.

On other platforms: use "surrogateescape" by default.

Supported error handlers:

• "strict"

• "surrogateescape"

• "surrogatepass" (only supported with the UTF-8 encoding)

See also the filesystem\_encoding member.

## unsigned long hash\_seed

## int use\_hash\_seed

Randomized hash function seed.

If use\_hash\_seed is zero, a seed is chosen randomly at Python startup, and hash\_seed is ignored.

Set by the PYTHONHASHSEED environment variable.

Default use\_hash\_seed value: -1 in Python mode, 0 in isolated mode.

## wchar\_t \*home

Python home directory.

If Py\_SetPythonHome() has been called, use its argument if it is not NULL.

Set by the PYTHONHOME environment variable.

Default: NULL.

Part of the Python Path Configuration input.

## int import\_time

If non-zero, profile import time.

Set the 1 by the -X importtime option and the PYTHONPROFILEIMPORTTIME environment variable.

Default: 0.

## int inspect

Enter interactive mode after executing a script or a command.

If greater than 0, enable inspect: when a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command, even when sys.stdin does not appear to be a terminal.

Incremented by the -i command line option. Set to 1 if the PYTHONINSPECT environment variable is non-empty.

Default: 0.

## int install\_signal\_handlers

Install Python signal handlers?

Default: 1 in Python mode, 0 in isolated mode.

## int interactive

If greater than 0, enable the interactive mode (REPL).

Incremented by the -i command line option.

Default: 0.

## int isolated

If greater than 0, enable isolated mode:

• sys.path contains neither the script’s directory (computed from argv[0] or the current directory) nor the user’s site-packages directory.

• Python REPL doesn’t import readline nor enable default readline configuration on interactive prompts.

• Set use\_environment and user\_site\_directory to 0.

Default: 0 in Python mode, 1 in isolated mode.

See also PyPreConfig.isolated.

## int legacy\_windows\_stdio

If non-zero, use io.FileIO instead of io.WindowsConsoleIO for sys.stdin, sys.stdout and sys.stderr.

Set to 1 if the PYTHONLEGACYWINDOWSSTDIO environment variable is set to a non-empty string.

Only available on Windows. #ifdef MS\_WINDOWS macro can be used for Windows specific code.

Default: 0.

See also the [**PEP 528**](https://www.python.org/dev/peps/pep-0528) (Change Windows console encoding to UTF-8).

## int malloc\_stats

If non-zero, dump statistics on Python pymalloc memory allocator at exit.

Set to 1 by the PYTHONMALLOCSTATS environment variable.

The option is ignored if Python is configured using the --without-pymalloc option.

Default: 0.

## wchar\_t \*platlibdir

Platform library directory name: sys.platlibdir.

Set by the PYTHONPLATLIBDIR environment variable.

Default: value of the PLATLIBDIR macro which is set by the configure --with-platlibdir option (default: "lib").

Part of the Python Path Configuration input.

New in version 3.9.

## wchar\_t \*pythonpath\_env

Module search paths (sys.path) as a string separated by DELIM (os.path.pathsep).

Set by the PYTHONPATH environment variable.

Default: NULL.

Part of the Python Path Configuration input.

## PyWideStringList module\_search\_paths

## int module\_search\_paths\_set

Module search paths: sys.path.

If module\_search\_paths\_set is equal to 0, the function calculating the Python Path Configuration overrides the module\_search\_paths and sets module\_search\_paths\_set to 1.

Default: empty list (module\_search\_paths) and 0 (module\_search\_paths\_set).

Part of the Python Path Configuration output.

## int optimization\_level

Compilation optimization level:

• 0: Peephole optimizer, set \_\_debug\_\_ to True.

• 1: Level 0, remove assertions, set \_\_debug\_\_ to False.

• 2: Level 1, strip docstrings.

Incremented by the -O command line option. Set to the PYTHONOPTIMIZE environment variable value.

Default: 0.

## PyWideStringList orig\_argv

The list of the original command line arguments passed to the Python executable: sys.orig\_argv.

If orig\_argv list is empty and argv is not a list only containing an empty string, PyConfig\_Read() copies argv into orig\_argv before modifying argv (if parse\_argv is non-zero).

See also the argv member and the Py\_GetArgcArgv() function.

Default: empty list.

New in version 3.10.

## int parse\_argv

## Parse command line arguments?

If equals to 1, parse argv the same way the regular Python parses command line arguments, and strip Python arguments from argv.

The PyConfig\_Read() function only parses PyConfig.argv arguments once: PyConfig. parse\_argv is set to 2 after arguments are parsed. Since Python arguments are strippped from PyConfig.argv, parsing arguments twice would parse the application options as Python options.

Default: 1 in Python mode, 0 in isolated mode.

Changed in version 3.10: The PyConfig.argv arguments are now only parsed if PyConfig. parse\_argv equals to 1.

## int parser\_debug

Parser debug mode. If greater than 0, turn on parser debugging output (for expert only, depending on compilation options).

Incremented by the -d command line option. Set to the PYTHONDEBUG environment variable value.

Default: 0.

## int pathconfig\_warnings

On Unix, if non-zero, calculating the Python Path Configuration can log warnings into stderr. If equals to 0, suppress these warnings.

It has no effect on Windows.

Default: 1 in Python mode, 0 in isolated mode.

Part of the Python Path Configuration input.

## wchar\_t \*prefix

The site-specific directory prefix where the platform independent Python files are installed: sys. prefix.

Default: NULL.

Part of the Python Path Configuration output.

## wchar\_t \*program\_name

Program name used to initialize executable and in early error messages during Python initialization.

• If Py\_SetProgramName() has been called, use its argument.

• On macOS, use PYTHONEXECUTABLE environment variable if set.

• If the WITH\_NEXT\_FRAMEWORK macro is defined, use \_\_PYVENV\_LAUNCHER\_\_ environment variable if set.

• Use argv[0] of argv if available and non-empty.

• Otherwise, use L"python" on Windows, or L"python3" on other platforms.

Default: NULL.

Part of the Python Path Configuration input.

wchar\_t \***pycache\_prefix** Directory where cached .pyc files are written: sys.pycache\_prefix. Set by the -X pycache\_prefix=PATH command line option and the PYTHONPYCACHEPREFIX environment variable. If NULL, sys.pycache\_prefix is set to None. Default: NULL. int **quiet** Quiet mode. If greater than 0, don’t display the copyright and version at Python startup in interactive mode. Incremented by the -q command line option. Default: 0. wchar\_t \***run\_command** Value of the -c command line option. Used by Py\_RunMain(). Default: NULL. wchar\_t \***run\_filename** Filename passed on the command line: trailing command line argument without -c or -m. For example, it is set to script.py by the python3 script.py arg command. Used by Py\_RunMain(). Default: NULL. wchar\_t \***run\_module** Value of the -m command line option. Used by Py\_RunMain(). Default: NULL. int **show\_ref\_count** Show total reference count at exit? Set to 1 by -X showrefcount command line option. Need a debug build of Python (the Py\_REF\_DEBUG macro must be defined). Default: 0. int **site\_import** Import the site module at startup? If equal to zero, disable the import of the module site and the site-dependent manipulations of sys. path that it entails. Also disable these manipulations if the site module is explicitly imported later (call site.main() if you want them to be triggered). Set to 0 by the -S command line option. sys.flags.no\_site is set to the inverted value of site\_import. Default: 1. int **skip\_source\_first\_line** If non-zero, skip the first line of the PyConfig.run\_filename source. It allows the usage of non-Unix forms of #!cmd. This is intended for a DOS specific hack only. Set to 1 by the -x command line option. Default: 0.

## wchar\_t \*stdio\_encoding

## wchar\_t \*stdio\_errors

Encoding and encoding errors of sys.stdin, sys.stdout and sys.stderr (but sys.stderr always uses "backslashreplace" error handler).

If Py\_SetStandardStreamEncoding() has been called, use its error and errors arguments if they are not NULL.

Use the PYTHONIOENCODING environment variable if it is non-empty.

Default encoding:

• "UTF-8" if PyPreConfig.utf8\_mode is non-zero.

• Otherwise, use the locale encoding.

Default error handler:

• On Windows: use "surrogateescape".

• "surrogateescape" if PyPreConfig.utf8\_mode is non-zero, or if the LC\_CTYPE locale is “C” or “POSIX”.

• "strict" otherwise.

## int tracemalloc

Enable tracemalloc?

If non-zero, call tracemalloc.start() at startup.

Set by -X tracemalloc=N command line option and by the PYTHONTRACEMALLOC environment variable.

Default: -1 in Python mode, 0 in isolated mode.

## int use\_environment

Use environment variables?

If equals to zero, ignore the environment variables.

Default: 1 in Python config and 0 in isolated config.

## int user\_site\_directory

If non-zero, add the user site directory to sys.path.

Set to 0 by the -s and -I command line options.

Set to 0 by the PYTHONNOUSERSITE environment variable.

Default: 1 in Python mode, 0 in isolated mode.

## int verbose

Verbose mode. If greater than 0, print a message each time a module is imported, showing the place (filename or built-in module) from which it is loaded.

If greater or equal to 2, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.

Incremented by the -v command line option.

Set to the PYTHONVERBOSE environment variable value.

Default: 0.

## PyWideStringList warnoptions

Options of the warnings module to build warnings filters, lowest to highest priority: sys. warnoptions.

The warnings module adds sys.warnoptions in the reverse order: the last PyConfig. warnoptions item becomes the first item of warnings.filters which is checked first (highest priority).

The -W command line options adds its value to warnoptions, it can be used multiple times.

The PYTHONWARNINGS environment variable can also be used to add warning options. Multiple options can be specified, separated by commas (,).

Default: empty list.

## int write\_bytecode

If equal to 0, Python won’t try to write .pyc files on the import of source modules.

Set to 0 by the -B command line option and the PYTHONDONTWRITEBYTECODE environment variable.

sys.dont\_write\_bytecode is initialized to the inverted value of write\_bytecode.

Default: 1.

## PyWideStringList xoptions

Values of the -X command line options: sys.\_xoptions.

Default: empty list.

If parse\_argv is non-zero, argv arguments are parsed the same way the regular Python parses command line arguments, and Python arguments are stripped from argv.

The xoptions options are parsed to set other options: see the -X command line option.

Changed in version 3.9: The show\_alloc\_count field has been removed.

## 10.7 Initialization with PyConfig

Function to initialize Python:

PyStatus **Py\_InitializeFromConfig**(**const** PyConfig \*config) Initialize Python from config configuration.

The caller is responsible to handle exceptions (error or exit) using PyStatus\_Exception() and Py\_ExitStatusException().

If PyImport\_FrozenModules(), PyImport\_AppendInittab() or PyImport\_ExtendInittab() are used, they must be set or called after Python preinitialization and before the Python initialization. If Python is initialized multiple times, PyImport\_AppendInittab() or PyImport\_ExtendInittab() must be called before each Python initialization.

The current configuration (PyConfig type) is stored in PyInterpreterState.config.

Example setting the program name:

```c
void init_python(void)
{
    PyStatus status;

    PyConfig config;
    PyConfig_InitPythonConfig(&config);

    /* Set the program name. Implicitly preinitialize Python. */
    status = PyConfig_SetString(&config, &config.program_name,
                          L"/path/to/my_program");
    if (PyStatus_Exception(status)) {
        goto exception;
    }

    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto exception;
```

(continues on next page)

```c
}
    PyConfig_Clear(&config);
    return;

exception:
    PyConfig_Clear(&config);
    Py_ExitStatusException(status);
}
```

(continued from previous page)

More complete example modifying the default configuration, read the configuration, and then override some parameters:

```txt
PyStatus init_python(const char *program_name)
{
    PyStatus status;

    PyConfig config;
    PyConfig_InitPythonConfig(&config);

    /* Set the program name before reading the configuration
        (decode byte string from the locale encoding).

        Implicitly preinitialize Python. */
    status = PyConfig_SetBytesString(&config, &config.program_name,
                               program_name);
    if (PyStatus_Exception(status)) {
        goto done;
    }

    /* Read all configuration at once */
    status = PyConfig_Read(&config);
    if (PyStatus_Exception(status)) {
        goto done;
    }

    /* Append our custom search path to sys.path */
    status = PyWideStringList_Append(&config.module_search_paths,
                               L"/path/to/more/modules");
    if (PyStatus_Exception(status)) {
        goto done;
    }

    /* Override executable computed by PyConfig_Read() */
    status = PyConfig_SetString(&config, &config.executable,
                               L"/path/to/my_executable");
    if (PyStatus_Exception(status)) {
        goto done;
    }

    status = Py_InitializeFromConfig(&config);

done:
    PyConfig_Clear(&config);
    return status;
}
```

## 10.8 Isolated Configuration

PyPreConfig\_InitIsolatedConfig() and PyConfig\_InitIsolatedConfig() functions create a configuration to isolate Python from the system. For example, to embed Python into an application.

This configuration ignores global configuration variables, environment variables, command line arguments (PyConfig.argv is not parsed) and user site directory. The C standard streams (ex: stdout) and the LC\_CTYPE locale are left unchanged. Signal handlers are not installed.

Configuration files are still used with this configuration. Set the Python Path Configuration (“output fields”) to ignore these configuration files and avoid the function computing the default path configuration.

## 10.9 Python Configuration

PyPreConfig\_InitPythonConfig() and PyConfig\_InitPythonConfig() functions create a configuration to build a customized Python which behaves as the regular Python.

Environments variables and command line arguments are used to configure Python, whereas global configuration variables are ignored.

This function enables C locale coercion ([**PEP 538**](https://www.python.org/dev/peps/pep-0538)) and Python UTF-8 Mode ([**PEP 540**](https://www.python.org/dev/peps/pep-0540)) depending on the LC\_CTYPE locale, PYTHONUTF8 and PYTHONCOERCECLOCALE environment variables.

## 10.10 Python Path Configuration

PyConfig contains multiple fields for the path configuration:

• Path configuration inputs:

– PyConfig.home

– PyConfig.platlibdir

– PyConfig.pathconfig\_warnings

– PyConfig.program\_name

– PyConfig.pythonpath\_env

– current working directory: to get absolute paths

– PATH environment variable to get the program full path (from PyConfig.program\_name)

– \_ PYVENV\_LAUNCHER\_\_ environment variable

(Windows only) Application paths in the registry under “SoftwarePythonPythonCoreX.YPythonPath” of HKEY\_CURRENT\_USER and HKEY\_LOCAL\_MACHINE (where X.Y is the Python version).

• Path configuration output fields:

– PyConfig.base\_exec\_prefix

– PyConfig.base\_executable

– PyConfig.base\_prefix

– PyConfig.exec\_prefix

– PyConfig.executable

– PyConfig.module\_search\_paths\_set, PyConfig.module\_search\_paths

– PyConfig.prefix

If at least one “output field” is not set, Python calculates the path configuration to fill unset fields. If module\_search\_paths\_set is equal to 0, module\_search\_paths is overridden and module\_search\_paths\_set is set to 1.

It is possible to completely ignore the function calculating the default path configuration by setting explicitly all path configuration output fields listed above. A string is considered as set even if it is non-empty. module\_search\_paths is considered as set if module\_search\_paths\_set is set to 1. In this case, path configuration input fields are ignored as well.

Set pathconfig\_warnings to 0 to suppress warnings when calculating the path configuration (Unix only, Windows does not log any warning).

If base\_prefix or base\_exec\_prefix fields are not set, they inherit their value from prefix and exec\_prefix respectively.

Py\_RunMain() and Py\_Main() modify sys.path:

• If run\_filename is set and is a directory which contains a \_\_main\_\_.py script, prepend run\_filename to sys.path.

• If isolated is zero:

– If run\_module is set, prepend the current directory to sys.path. Do nothing if the current directory cannot be read.

– If run\_filename is set, prepend the directory of the filename to sys.path.

– Otherwise, prepend an empty string to sys.path.

If site\_import is non-zero, sys.path can be modified by the site module. If user\_site\_directory is non-zero and the user’s site-package directory exists, the site module appends the user’s site-package directory to sys.path.

The following configuration files are used by the path configuration:

• pyvenv.cfg

• python.\_pth (Windows only)

• pybuilddir.txt (Unix only)

The \_\_PYVENV\_LAUNCHER\_\_ environment variable is used to set PyConfig.base\_executable

## 10.11 Py\_RunMain()

## int Py\_RunMain(void)

Execute the command (PyConfig.run\_command), the script (PyConfig.run\_filename) or the module (PyConfig.run\_module) specified on the command line or in the configuration.

By default and when if -i option is used, run the REPL.

Finally, finalizes Python and returns an exit status that can be passed to the exit() function.

See Python Configuration for an example of customized Python always running in isolated mode using Py\_RunMain().

## 10.12 Py\_GetArgcArgv()

void **Py\_GetArgcArgv**(int \*argc, wchar\_t \*\*\*argv)

Get the original command line arguments, before Python modified them.

See also PyConfig.orig\_argv member.

## 10.13 Multi-Phase Initialization Private Provisional API

This section is a private provisional API introducing multi-phase initialization, the core feature of [**PEP 432**](https://www.python.org/dev/peps/pep-0432):

• “Core” initialization phase, “bare minimum Python”:

– Builtin types;

– Builtin exceptions;

– Builtin and frozen modules;

– The sys module is only partially initialized (ex: sys.path doesn’t exist yet).

• “Main” initialization phase, Python is fully initialized:

– Install and configure importlib;

– Apply the Path Configuration;

– Install signal handlers;

– Finish sys module initialization (ex: create sys.stdout and sys.path);

– Enable optional features like faulthandler and tracemalloc;

– Import the site module;

```txt
- etc.
```

Private provisional API:

• PyConfig.\_init\_main: if set to 0, Py\_InitializeFromConfig() stops at the “Core” initialization phase.

• PyConfig.\_isolated\_interpreter: if non-zero, disallow threads, subprocesses and fork.

PyStatus **\_Py\_InitializeMain**(void)

Move to the “Main” initialization phase, finish the Python initialization.

No module is imported during the “Core” phase and the importlib module is not configured: the Path Configuration is only applied during the “Main” phase. It may allow to customize Python in Python to override or tune the Path Configuration, maybe install a custom sys.meta\_path importer or an import hook, etc.

It may become possible to calculatin the Path Configuration in Python, after the Core phase and before the Main phase, which is one of the [**PEP 432**](https://www.python.org/dev/peps/pep-0432) motivation.

The “Core” phase is not properly defined: what should be and what should not be available at this phase is not specified yet. The API is marked as private and provisional: the API can be modified or even be removed anytime until a proper public API is designed.

Example running Python code between “Core” and “Main” initialization phases:

```c
void init_python(void)
{
    PyStatus status;

    PyConfig config;
    PyConfig_InitPythonConfig(&config);
    config._init_main = 0;
```

(continues on next page)

(continued from previous page)

```c
/* ... customize 'config' configuration ... */

status = Py_InitializeFromConfig(&config);
PyConfig_Clear(&config);
if (PyStatus_Exception(status)) {
    Py_ExitStatusException(status);
}

/* Use sys.stderr because sys.stdout is only created
    by _Py_InitializeMain() */
int res = PyRun_SimpleString(
    "import sys; "
    "print('Run Python code before _Py_InitializeMain', "
        "file=sys.stderr)");
if (res < 0) {
    exit(1);
}

/* ... put more configuration code here ... */

status = _Py_InitializeMain();
if (PyStatus_Exception(status)) {
    Py_ExitStatusException(status);
}
```

## MEMORY MANAGEMENT

## 11.1 Overview

Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.

At the lowest level, a raw memory allocator ensures that there is enough room in the private heap for storing all Python-related data by interacting with the memory manager of the operating system. On top of the raw memory allocator, several object-specific allocators operate on the same heap and implement distinct memory management policies adapted to the peculiarities of every object type. For example, integer objects are managed differently within the heap than strings, tuples or dictionaries because integers imply different storage requirements and speed/space tradeoffs. The Python memory manager thus delegates some of the work to the object-specific allocators, but ensures that the latter operate within the bounds of the private heap.

It is important to understand that the management of the Python heap is performed by the interpreter itself and that the user has no control over it, even if they regularly manipulate object pointers to memory blocks inside that heap. The allocation of heap space for Python objects and other internal buffers is performed on demand by the Python memory manager through the Python/C API functions listed in this document.

To avoid memory corruption, extension writers should never try to operate on Python objects with the functions exported by the C library: malloc(), calloc(), realloc() and free(). This will result in mixed calls between the C allocator and the Python memory manager with fatal consequences, because they implement different algorithms and operate on different heaps. However, one may safely allocate and release memory blocks with the C library allocator for individual purposes, as shown in the following example:

```c
PyObject *res;
char *buf = (char *) malloc(BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
...Do some I/O operation involving buf...
res = PyBytes_FromString(buf);
free(buf); /* malloc'ed */
return res;
```

In this example, the memory request for the I/O buffer is handled by the C library allocator. The Python memory manager is involved only in the allocation of the bytes object returned as a result.

In most situations, however, it is recommended to allocate memory from the Python heap specifically because the latter is under control of the Python memory manager. For example, this is required when the interpreter is extended with new object types written in C. Another reason for using the Python heap is the desire to inform the Python memory manager about the memory needs of the extension module. Even when the requested memory is used exclusively for internal, highly specific purposes, delegating all memory requests to the Python memory manager causes the interpreter to have a more accurate image of its memory footprint as a whole. Consequently, under certain circumstances, the Python memory manager may or may not trigger appropriate actions, like garbage collection,

memory compaction or other preventive procedures. Note that by using the C library allocator as shown in the previous example, the allocated memory for the I/O buffer escapes completely the Python memory manager.

## See also:

The PYTHONMALLOC environment variable can be used to configure the memory allocators used by Python.

The PYTHONMALLOCSTATS environment variable can be used to print statistics of the pymalloc memory allocator every time a new pymalloc object arena is created, and on shutdown.

## 11.2 Allocator Domains

All allocating functions belong to one of three different “domains” (see also PyMemAllocatorDomain). These domains represent different allocation strategies and are optimized for different purposes. The specific details on how every domain allocates memory or what internal functions each domain calls is considered an implementation detail, but for debugging purposes a simplified table can be found at here. There is no hard requirement to use the memory returned by the allocation functions belonging to a given domain for only the purposes hinted by that domain (although this is the recommended practice). For example, one could use the memory returned by PyMem\_RawMalloc() for allocating Python objects or the memory returned by PyObject\_Malloc() for allocating memory for buffers.

The three allocation domains are:

• Raw domain: intended for allocating memory for general-purpose memory buffers where the allocation must go to the system allocator or where the allocator can operate without the GIL. The memory is requested directly to the system.

• “Mem” domain: intended for allocating memory for Python buffers and general-purpose memory buffers where the allocation must be performed with the GIL held. The memory is taken from the Python private heap.

• Object domain: intended for allocating memory belonging to Python objects. The memory is taken from the Python private heap.

When freeing memory previously allocated by the allocating functions belonging to a given domain,the matching specific deallocating functions must be used. For example, PyMem\_Free() must be used to free memory allocated using PyMem\_Malloc().

## 11.3 Raw Memory Interface

The following function sets are wrappers to the system allocator. These functions are thread-safe, the GIL does not need to be held.

The default raw memory allocator uses the following functions: malloc(), calloc(), realloc() and free(); call malloc(1) (or calloc(1, 1)) when requesting zero bytes.

New in version 3.4.

## void \*PyMem\_RawMalloc(size\_t n)

Allocates n bytes and returns a pointer of type void\* to the allocated memory, or NULL if the request fails.

Requesting zero bytes returns a distinct non-NULL pointer if possible, as if PyMem\_RawMalloc(1) had been called instead. The memory will not have been initialized in any way.

## void \*PyMem\_RawCalloc(size\_t nelem, size\_t elsize)

Allocates nelem elements each whose size in bytes is elsize and returns a pointer of type void\* to the allocated memory, or NULL if the request fails. The memory is initialized to zeros.

Requesting zero elements or elements of size zero bytes returns a distinct non-NULL pointer if possible, as if PyMem\_RawCalloc(1, 1) had been called instead.

New in version 3.5.

void \***PyMem\_RawRealloc**(void \*p, size\_t n)

Resizes the memory block pointed to by p to n bytes. The contents will be unchanged to the minimum of the old and the new sizes.

If p is NULL, the call is equivalent to PyMem\_RawMalloc(n); else if n is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-NULL.

Unless p is NULL, it must have been returned by a previous call to PyMem\_RawMalloc(), PyMem\_RawRealloc() or PyMem\_RawCalloc().

If the request fails, PyMem\_RawRealloc() returns NULL and p remains a valid pointer to the previous memory area.

## void PyMem\_RawFree(void \*p)

Frees the memory block pointed to by p, which must have been returned by a previous call to PyMem\_RawMalloc(), PyMem\_RawRealloc() or PyMem\_RawCalloc(). Otherwise, or if PyMem\_RawFree(p) has been called before, undefined behavior occurs.

If p is NULL, no operation is performed.

## 11.4 Memory Interface

The following function sets, modeled after the ANSI C standard, but specifying behavior when requesting zero bytes, are available for allocating and releasing memory from the Python heap.

The default memory allocator uses the pymalloc memory allocator.

**Warning:** The GIL must be held when using these functions.

Changed in version 3.6: The default allocator is now pymalloc instead of system malloc().

## void \*PyMem\_Malloc(size\_t n)

Part of the Stable ABI. Allocates n bytes and returns a pointer of type void\* to the allocated memory, or NULL if the request fails.

Requesting zero bytes returns a distinct non-NULL pointer if possible, as if PyMem\_Malloc(1) had been called instead. The memory will not have been initialized in any way.

void \***PyMem\_Calloc**(size\_t nelem, size\_t elsize)

Part of the Stable ABI since version 3.7. Allocates nelem elements each whose size in bytes is elsize and returns a pointer of type void\* to the allocated memory, or NULL if the request fails. The memory is initialized to zeros.

Requesting zero elements or elements of size zero bytes returns a distinct non-NULL pointer if possible, as if PyMem\_Calloc(1, 1) had been called instead.

New in version 3.5.

void \***PyMem\_Realloc**(void \*p, size\_t n) Part of the Stable ABI. Resizes the memory block pointed to by p to n bytes. The contents will be unchanged to the minimum of the old and the new sizes.

If p is NULL, the call is equivalent to PyMem\_Malloc(n); else if n is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-NULL.

Unless p is NULL, it must have been returned by a previous call to PyMem\_Malloc(), PyMem\_Realloc() or PyMem\_Calloc().

If the request fails, PyMem\_Realloc() returns NULL and p remains a valid pointer to the previous memory area.

Part of the Stable ABI. Frees the memory block pointed to by p, which must have been returned by a

previous call to PyMem\_Malloc(), PyMem\_Realloc() or PyMem\_Calloc(). Otherwise, or if PyMem\_Free(p) has been called before, undefined behavior occurs.

If p is NULL, no operation is performed.

The following type-oriented macros are provided for convenience. Note that TYPE refers to any C type.

TYPE \***PyMem\_New**(TYPE, size\_t n)

Same as PyMem\_Malloc(), but allocates (n \* sizeof(TYPE)) bytes of memory. Returns a pointer cast to TYPE\*. The memory will not have been initialized in any way.

TYPE \***PyMem\_Resize**(void \*p, TYPE, size\_t n)

Same as PyMem\_Realloc(), but the memory block is resized to (n \* sizeof(TYPE)) bytes. Returns a pointer cast to TYPE\*. On return, p will be a pointer to the new memory area, or NULL in the event of failure.

This is a C preprocessor macro; p is always reassigned. Save the original value of p to avoid losing memory when handling errors.

```txt
void PyMem_Del (void *p)
    Same as PyMem_Free().
```

In addition, the following macro sets are provided for calling the Python memory allocator directly, without involving the C API functions listed above. However, note that their use does not preserve binary compatibility across Python versions and is therefore deprecated in extension modules.

• PyMem\_MALLOC(size)

• PyMem\_NEW(type, size)

• PyMem\_REALLOC(ptr, size)

• PyMem\_RESIZE(ptr, type, size)

• PyMem\_FREE(ptr)

• PyMem\_DEL(ptr)

## 11.5 Object allocators

The following function sets, modeled after the ANSI C standard, but specifying behavior when requesting zero bytes, are available for allocating and releasing memory from the Python heap.

**Note:** There is no guarantee that the memory returned by these allocators can be successfully cast to a Python object when intercepting the allocating functions in this domain by the methods described in the Customize Memory Allocators section.

The default object allocator uses the pymalloc memory allocator.

**Warning:** The GIL must be held when using these functions.

void \***PyObject\_Malloc**(size\_t n)

Part of the Stable ABI. Allocates n bytes and returns a pointer of type void\* to the allocated memory, or NULL if the request fails.

Requesting zero bytes returns a distinct non-NULL pointer if possible, as if PyObject\_Malloc(1) had been called instead. The memory will not have been initialized in any way.

void \***PyObject\_Calloc**(size\_t nelem, size\_t elsize)

Part of the Stable ABI since version 3.7. Allocates nelem elements each whose size in bytes is elsize and returns a pointer of type void\* to the allocated memory, or NULL if the request fails. The memory is initialized to zeros.

Requesting zero elements or elements of size zero bytes returns a distinct non-NULL pointer if possible, as if PyObject\_Calloc(1, 1) had been called instead.

New in version 3.5.

## void \*PyObject\_Realloc(void \*p, size\_t n)

Part of the Stable ABI. Resizes the memory block pointed to by p to n bytes. The contents will be unchanged to the minimum of the old and the new sizes.

If p is NULL, the call is equivalent to PyObject\_Malloc(n); else if n is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-NULL.

Unless p is NULL, it must have been returned by a previous call to PyObject\_Malloc(), PyObject\_Realloc() or PyObject\_Calloc().

If the request fails, PyObject\_Realloc() returns NULL and p remains a valid pointer to the previous memory area.

## void PyObject\_Free(void \*p)

Part of the Stable ABI. Frees the memory block pointed to by p, which must have been returned by a previous call to PyObject\_Malloc(), PyObject\_Realloc() or PyObject\_Calloc(). Otherwise, or if PyObject\_Free(p) has been called before, undefined behavior occurs.

If p is NULL, no operation is performed.

## 11.6 Default Memory Allocators

Default memory allocators:

| Configuration | Name | PyMem_RawMall | ocPyMem_Malloc | PyOb-ject_Malloc |
| --- | --- | --- | --- | --- |
| Release build | "pymalloc" | malloc | pymalloc | pymalloc |
| Debug build | "pymalloc_debu | g"malloc + debug | pymalloc + debug | pymalloc + debug |
| Release build, without py-malloc | "malloc" | malloc | malloc | malloc |
| Debug build, without py-malloc | "malloc_debug" | malloc + debug | malloc + de-bug | malloc + de-bug |

## Legend:

• Name: value for PYTHONMALLOC environment variable.

• malloc: system allocators from the standard C library, C functions: malloc(), calloc(), realloc() and free().

• pymalloc: pymalloc memory allocator.

• “+ debug”: with debug hooks on the Python memory allocators.

• “Debug build”: Python build in debug mode.

## 11.7 Customize Memory Allocators

New in version 3.4.

## type PyMemAllocatorEx

Structure used to describe a memory block allocator. The structure has the following fields:

| Field | Meaning |
| --- | --- |
| void *ctx | user context passed as first argument |
| void* malloc(void *ctx, size_t size) | allocate a memory block |
| void* calloc(void *ctx, size_t nelem, | allocate a memory block initialized |
| size_t elsize) | with zeros |
| void* realloc(void *ctx, void *ptr, size_t | allocate or resize a memory block |
| new_size) |  |
| void free(void *ctx, void *ptr) | free a memory block |

Changed in version 3.5: The PyMemAllocator structure was renamed to PyMemAllocatorEx and a new calloc field was added.

## type PyMemAllocatorDomain

Enum used to identify an allocator domain. Domains:

## PYMEM\_DOMAIN\_RAW

Functions:

• PyMem\_RawMalloc()

• PyMem\_RawRealloc()

• PyMem\_RawCalloc()

• PyMem\_RawFree()

## PYMEM\_DOMAIN\_MEM

Functions:

• PyMem\_Malloc(),

• PyMem\_Realloc()

• PyMem\_Calloc()

• PyMem\_Free()

**PYMEM\_DOMAIN\_OBJ**

Functions:

• PyObject\_Malloc()

• PyObject\_Realloc()

• PyObject\_Calloc()

• PyObject\_Free()

void **PyMem\_GetAllocator**(PyMemAllocatorDomain domain, PyMemAllocatorEx \*allocator)

Get the memory block allocator of the specified domain.

void **PyMem\_SetAllocator**(PyMemAllocatorDomain domain, PyMemAllocatorEx \*allocator)

Set the memory block allocator of the specified domain.

The new allocator must return a distinct non-NULL pointer when requesting zero bytes.

For the PYMEM\_DOMAIN\_RAW domain, the allocator must be thread-safe: the GIL is not held when the allocator is called.

If the new allocator is not a hook (does not call the previous allocator), the PyMem\_SetupDebugHooks() function must be called to reinstall the debug hooks on top on the new allocator.

**Warning:** PyMem\_SetAllocator() does have the following contract:

• It can be called after Py\_PreInitialize() and before Py\_InitializeFromConfig() to install a custom memory allocator. There are no restrictions over the installed allocator other than the ones imposed by the domain (for instance, the Raw Domain allows the allocator to be called without the GIL held). See the section on allocator domains for more information.

• If called after Python has finish initializing (after Py\_InitializeFromConfig() has been called) the allocator **must** wrap the existing allocator. Substituting the current allocator for some other arbitrary one is **not supported**.

## void PyMem\_SetupDebugHooks(void)

Setup debug hooks in the Python memory allocators to detect memory errors.

## 11.8 Debug hooks on the Python memory allocators

When Python is built in debug mode, the PyMem\_SetupDebugHooks() function is called at the Python preinitialization to setup debug hooks on Python memory allocators to detect memory errors.

The PYTHONMALLOC environment variable can be used to install debug hooks on a Python compiled in release mode (ex: PYTHONMALLOC=debug).

The PyMem\_SetupDebugHooks() function can be used to set debug hooks after calling PyMem\_SetAllocator().

These debug hooks fill dynamically allocated memory blocks with special, recognizable bit patterns. Newly allocated memory is filled with the byte 0xCD (PYMEM\_CLEANBYTE), freed memory is filled with the byte 0xDD (PYMEM\_DEADBYTE). Memory blocks are surrounded by “forbidden bytes” filled with the byte 0xFD (PYMEM\_FORBIDDENBYTE). Strings of these bytes are unlikely to be valid addresses, floats, or ASCII strings.

## Runtime checks:

• Detect API violations. For example, detect if PyObject\_Free() is called on a memory block allocated by PyMem\_Malloc().

• Detect write before the start of the buffer (buffer underflow).

• Detect write after the end of the buffer (buffer overflow).

• Check that the GIL is held when allocator functions of PYMEM\_DOMAIN\_OBJ (ex: PyObject\_Malloc()) and PYMEM\_DOMAIN\_MEM (ex: PyMem\_Malloc()) domains are called.

On error, the debug hooks use the tracemalloc module to get the traceback where a memory block was allocated. The traceback is only displayed if tracemalloc is tracing Python memory allocations and the memory block was traced.

Let S = sizeof(size\_t). 2\*S bytes are added at each end of each block of N bytes requested. The memory layout is like so, where p represents the address returned by a malloc-like or realloc-like function (p[i:j] means the slice of bytes from \*(p+i) inclusive up to \*(p+j) exclusive; note that the treatment of negative indices differs from a Python slice):

**p[-2\*S:-S]** Number of bytes originally asked for. This is a size\_t, big-endian (easier to read in a memory dump).

**p[-S]** API identifier (ASCII character):

• 'r' for PYMEM\_DOMAIN\_RAW.

• 'm' for PYMEM\_DOMAIN\_MEM.

• 'o' for PYMEM\_DOMAIN\_OBJ.

**p[-S+1:0]** Copies of PYMEM\_FORBIDDENBYTE. Used to catch under- writes and reads.

**p[0:N]** The requested memory, filled with copies of PYMEM\_CLEANBYTE, used to catch reference to uninitialized memory. When a realloc-like function is called requesting a larger memory block, the new excess bytes are also filled with PYMEM\_CLEANBYTE. When a free-like function is called, these are overwritten with PYMEM\_DEADBYTE, to catch reference to freed memory. When a realloc- like function is called requesting a smaller memory block, the excess old bytes are also filled with PYMEM\_DEADBYTE.

**p[N:N+S]** Copies of PYMEM\_FORBIDDENBYTE. Used to catch over- writes and reads.

**p[N+S:N+2\*S]** Only used if the PYMEM\_DEBUG\_SERIALNO macro is defined (not defined by default).

A serial number, incremented by 1 on each call to a malloc-like or realloc-like function. Big-endian size\_t. If “bad memory” is detected later, the serial number gives an excellent way to set a breakpoint on the next run, to capture the instant at which this block was passed out. The static function bumpserialno() in obmalloc.c is the only place the serial number is incremented, and exists so you can set such a breakpoint easily.

A realloc-like or free-like function first checks that the PYMEM\_FORBIDDENBYTE bytes at each end are intact. If they’ve been altered, diagnostic output is written to stderr, and the program is aborted via Py\_FatalError(). The other main failure mode is provoking a memory error when a program reads up one of the special bit patterns and tries to use it as an address. If you get in a debugger then and look at the object, you’re likely to see that it’s entirely filled with PYMEM\_DEADBYTE (meaning freed memory is getting used) or PYMEM\_CLEANBYTE (meaning uninitialized memory is getting used).

Changed in version 3.6: The PyMem\_SetupDebugHooks() function now also works on Python compiled in release mode. On error, the debug hooks now use tracemalloc to get the traceback where a memory block was allocated. The debug hooks now also check if the GIL is held when functions of PYMEM\_DOMAIN\_OBJ and PYMEM\_DOMAIN\_MEM domains are called.

Changed in version 3.8: Byte patterns 0xCB (PYMEM\_CLEANBYTE), 0xDB (PYMEM\_DEADBYTE) and 0xFB (PYMEM\_FORBIDDENBYTE) have been replaced with 0xCD, 0xDD and 0xFD to use the same values than Windows CRT debug malloc() and free().

## 11.9 The pymalloc allocator

Python has a pymalloc allocator optimized for small objects (smaller or equal to 512 bytes) with a short lifetime. It uses memory mappings called “arenas” with a fixed size of 256 KiB. It falls back to PyMem\_RawMalloc() and PyMem\_RawRealloc() for allocations larger than 512 bytes.

pymalloc is the default allocator of the PYMEM\_DOMAIN\_MEM (ex: PyMem\_Malloc()) and PYMEM\_DOMAIN\_OBJ (ex: PyObject\_Malloc()) domains.

The arena allocator uses the following functions:

• VirtualAlloc() and VirtualFree() on Windows,

• mmap() and munmap() if available,

• malloc() and free() otherwise.

This allocator is disabled if Python is configured with the --without-pymalloc option. It can also be disabled at runtime using the PYTHONMALLOC environment variable (ex: PYTHONMALLOC=malloc).

## 11.9.1 Customize pymalloc Arena Allocator

New in version 3.4.

## type PyObjectArenaAllocator

Structure used to describe an arena allocator. The structure has three fields:

| Field | Meaning |
| --- | --- |
| void *ctx | user context passed as first argument |
| void* alloc(void *ctx, size_t size) | allocate an arena of size bytes |
| void free(void *ctx, void *ptr, size_t size) | free an arena |

void **PyObject\_GetArenaAllocator**(PyObjectArenaAllocator \*allocator) Get the arena allocator.

void **PyObject\_SetArenaAllocator**(PyObjectArenaAllocator \*allocator)

Set the arena allocator.

## 11.10 tracemalloc C API

New in version 3.7.

int **PyTraceMalloc\_Track**(unsigned int domain, uintptr\_t ptr, size\_t size) Track an allocated memory block in the tracemalloc module.

Return 0 on success, return -1 on error (failed to allocate memory to store the trace). Return -2 if tracemalloc is disabled.

If memory block is already tracked, update the existing trace.

int **PyTraceMalloc\_Untrack**(unsigned int domain, uintptr\_t ptr)

Untrack an allocated memory block in the tracemalloc module. Do nothing if the block was not tracked.

Return -2 if tracemalloc is disabled, otherwise return 0.

## 11.11 Examples

Here is the example from section Overview, rewritten so that the I/O buffer is allocated from the Python heap by using the first function set:

```c
PyObject *res;
char *buf = (char *) PyMem_Malloc(BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
/* ...Do some I/O operation involving buf... */
res = PyBytes_FromString(buf);
PyMem_Free(buf); /* allocated with PyMem_Malloc */
return res;
```

The same code using the type-oriented function set:

```c
PyObject *res;
char *buf = PyMem_New(char, BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
```

(continues on next page)

```c
/* ...Do some I/O operation involving buf... */
res = PyBytes_FromString(buf);
PyMem_Del(buf); /* allocated with PyMem_New */
return res;
```

(continued from previous page)

Note that in the two examples above, the buffer is always manipulated via functions belonging to the same set. Indeed, it is required to use the same memory API family for a given memory block, so that the risk of mixing different allocators is reduced to a minimum. The following code sequence contains two errors, one of which is labeled as fatal because it mixes two different allocators operating on different heaps.

```c
char *buf1 = PyMem_New(char, BUFSIZ);
char *buf2 = (char *) malloc(BUFSIZ);
char *buf3 = (char *) PyMem_Malloc(BUFSIZ);
PyMem_Del(buf3); /* Wrong -- should be PyMem_Free() */
free(buf2); /* Right -- allocated via malloc() */
free(buf1); /* Fatal -- should be PyMem_Del() */
```

In addition to the functions aimed at handling raw memory blocks from the Python heap, objects in Python are allocated and released with PyObject\_New(), PyObject\_NewVar() and PyObject\_Del()

These will be explained in the next chapter on defining and implementing new object types in C.

# OBJECT IMPLEMENTATION SUPPORT

This chapter describes the functions, types, and macros used when defining new object types.

## 12.1 Allocating Objects on the Heap

PyObject \***\_PyObject\_New**(PyTypeObject \*type) Return value: New reference.

PyVarObject \***\_PyObject\_NewVar**(PyTypeObject \*type, Py\_ssize\_t size) Return value: New reference.

PyObject \***PyObject\_Init**(PyObject \*op, PyTypeObject \*type) Return value: Borrowed reference. Part of the Stable ABI. Initialize a newly allocated object op with its type and initial reference. Returns the initialized object. If type indicates that the object participates in the cyclic garbage detector, it is added to the detector’s set of observed objects. Other fields of the object are not affected.

PyVarObject \***PyObject\_InitVar**(PyVarObject \*op, PyTypeObject \*type, Py\_ssize\_t size) Return value: Borrowed reference. Part of the Stable ABI. This does everything PyObject\_Init() does, and also initializes the length information for a variable-size object.

## TYPE \*PyObject\_New(TYPE, PyTypeObject \*type)

Return value: New reference. Allocate a new Python object using the C structure type TYPE and the Python type object type. Fields not defined by the Python object header are not initialized. The caller will own the only reference to the object (i.e. its reference count will be one). The size of the memory allocation is determined from the tp\_basicsize field of the type object.

## TYPE \*PyObject\_NewVar(TYPE, PyTypeObject \*type, Py\_ssize\_t size)

Return value: New reference. Allocate a new Python object using the C structure type TYPE and the Python type object type. Fields not defined by the Python object header are not initialized. The allocated memory allows for the TYPE structure plus size fields of the size given by the tp\_itemsize field of type. This is useful for implementing objects like tuples, which are able to determine their size at construction time. Embedding the array of fields into the same allocation decreases the number of allocations, improving the memory management efficiency.

## void PyObject\_Del(void \*op)

Releases memory allocated to an object using PyObject\_New() or PyObject\_NewVar(). This is normally called from the tp\_dealloc handler specified in the object’s type. The fields of the object should not be accessed after this call as the memory is no longer a valid Python object.

## PyObject \_Py\_NoneStruct

Object which is visible in Python as None. This should only be accessed using the Py\_None macro, which evaluates to a pointer to this object.

## See also:

**PyModule\_Create()** To allocate and create extension modules.

## 12.2 Common Object Structures

There are a large number of structures which are used in the definition of object types for Python. This section describes these structures and how they are used.

## 12.2.1 Base object types and macros

All Python objects ultimately share a small number of fields at the beginning of the object’s representation in memory. These are represented by the PyObject and PyVarObject types, which are defined, in turn, by the expansions of some macros also used, whether directly or indirectly, in the definition of all other Python objects.

## type PyObject

Part of the Limited API. (Only some members are part of the stable ABI.) All object types are extensions of this type. This is a type which contains the information Python needs to treat a pointer to an object as an object. In a normal “release” build, it contains only the object’s reference count and a pointer to the corresponding type object. Nothing is actually declared to be a PyObject, but every pointer to a Python object can be cast to a PyObject\*. Access to the members must be done by using the macros Py\_REFCNT and Py\_TYPE.

## type PyVarObject

Part of the Limited API. (Only some members are part of the stable ABI.) This is an extension of PyObject that adds the ob\_size field. This is only used for objects that have some notion of length. This type does not often appear in the Python/C API. Access to the members must be done by using the macros Py\_REFCNT, Py\_TYPE, and Py\_SIZE.

## PyObject\_HEAD

This is a macro used when declaring new types which represent objects without a varying length. The PyObject\_HEAD macro expands to:

```txt
PyObject ob_base;
```

See documentation of PyObject above.

## PyObject\_VAR\_HEAD

This is a macro used when declaring new types which represent objects with a length that varies from instance to instance. The PyObject\_VAR\_HEAD macro expands to:

```txt
PyVarObject ob_base;
```

See documentation of PyVarObject above.

## int Py\_Is(const PyObject \*x, const PyObject \*y)

Part of the Stable ABI since version 3.10. Test if the x object is the y object, the same as x is y in Python.

New in version 3.10.

## int Py\_IsNone(const PyObject \*x)

Part of the Stable ABI since version 3.10. Test if an object is the None singleton, the same as x is None in Python.

New in version 3.10.

## int Py\_IsTrue(const PyObject \*x)

Part of the Stable ABI since version 3.10. Test if an object is the True singleton, the same as x is True in Python.

New in version 3.10.

## int Py\_IsFalse(const PyObject \*x)

Part of the Stable ABI since version 3.10. Test if an object is the False singleton, the same as x is False in Python.

New in version 3.10.

```txt
PyTypeObject *Py_TYPE (const PyObject *o)
    Get the type of the Python object o.
txt
Return a borrowed reference.
```

Use the Py\_SET\_TYPE() function to set an object type.

```python
int Py_IS_TYPE (PyObject *o, PyTypeObject *type)
    Return non-zero if the object o type is type. Return zero otherwise. Equivalent to: Py_TYPE(o) == type.
    New in version 3.9.
txt
void Py_SET_TYPE (PyObject *o, PyTypeObject *type)
    Set the object o type to type.
```

New in version 3.9.

```txt
Py_ssize_t Py_REFCNT (const PyObject *o)
    Get the reference count of the Python object o.
```

Changed in version 3.10: Py\_REFCNT() is changed to the inline static function. Use Py\_SET\_REFCNT() to set an object reference count.

```txt
void Py_SET_REFCNT (PyObject *o, Py_ssize_t refcnt)
    Set the object o reference counter to refcnt.
```

New in version 3.9.

```txt
Py_ssize_t Py_SIZE (const PyVarObject *o)
    Get the size of the Python object o.
```

Use the Py\_SET\_SIZE() function to set an object size.

```txt
void Py_SET_SIZE (PyVarObject *o, Py_ssize_t size)
    Set the object o size to size.
```

New in version 3.9.

**PyObject\_HEAD\_INIT**(type) This is a macro which expands to initialization values for a new PyObject type. This macro expands to:

```csv
_PyObject_EXTRA_INIT
1, type,
```

## PyVarObject\_HEAD\_INIT(type, size)

This is a macro which expands to initialization values for a new PyVarObject type, including the ob\_size field. This macro expands to:

```csv
_PyObject_EXTRA_INIT
1, type, size,
```

## 12.2.2 Implementing functions and methods

## type PyCFunction

Part of the Stable ABI. Type of the functions used to implement most Python callables in C. Functions of this type take two PyObject\* parameters and return one such value. If the return value is NULL, an exception shall have been set. If not NULL, the return value is interpreted as the return value of the function as exposed in Python. The function must return a new reference.

The function signature is:

```c
PyObject *PyCFunction(PyObject *self,
                            PyObject *args);
```

## type PyCFunctionWithKeywords

Part of the Stable ABI. Type of the functions used to implement Python callables in C with signature METH\_VARARGS | METH\_KEYWORDS. The function signature is:

```txt
PyObject *PyCFunctionWithKeywords(PyObject *self,
                            PyObject *args,
                            PyObject *kwargs);
```

## type \_PyCFunctionFast

Type of the functions used to implement Python callables in C with signature METH\_FASTCALL. The function signature is:

```c
PyObject *_PyCFunctionFast(PyObject *self,
                            PyObject *const *args,
                            Py_ssize_t nargs);
```

## type \_PyCFunctionFastWithKeywords

Type of the functions used to implement Python callables in C with signature METH\_FASTCALL | METH\_KEYWORDS. The function signature is:

```c
PyObject *_PyCFunctionFastWithKeywords(PyObject *self,
                            PyObject *const *args,
                            Py_ssize_t nargs,
                            PyObject *kwnames);
```

## type PyCMethod

Type of the functions used to implement Python callables in C with signature METH\_METHOD | METH\_FASTCALL | METH\_KEYWORDS. The function signature is:

```c
PyObject *PyCMethod(PyObject *self,
                      PyTypeObject *defining_class,
                      PyObject *const *args,
                      Py_ssize_t nargs,
                      PyObject *kwnames)
```

New in version 3.9.

## type PyMethodDef

Part of the Stable ABI (including all members). Structure used to describe a method of an extension type. This structure has four fields:

```txt
const char *ml_name
    name of the method
python
PyCFunction ml_meth
    pointer to the C implementation
```

## int ml\_flags

flags bits indicating how the call should be constructed

```txt
const char *ml_doc
    points to the contents of the docstring
```

The ml\_meth is a C function pointer. The functions may be of different types, but they always return PyObject\*. If the function is not of the PyCFunction, the compiler will require a cast in the method table. Even though PyCFunction defines the first parameter as PyObject\*, it is common that the method implementation uses the specific C type of the self object.

The ml\_flags field is a bitfield which can include the following flags. The individual flags indicate either a calling convention or a binding convention.

There are these calling conventions:

## METH\_VARARGS

This is the typical calling convention, where the methods have the type PyCFunction. The function expects

two PyObject\* values. The first one is the self object for methods; for module functions, it is the module object. The second parameter (often called args) is a tuple object representing all arguments. This parameter is typically processed using PyArg\_ParseTuple() or PyArg\_UnpackTuple().

## METH\_VARARGS | METH\_KEYWORDS

Methods with these flags must be of type PyCFunctionWithKeywords. The function expects three parameters: self, args, kwargs where kwargs is a dictionary of all the keyword arguments or possibly NULL if there are no keyword arguments. The parameters are typically processed using PyArg\_ParseTupleAndKeywords().

## METH\_FASTCALL

Fast calling convention supporting only positional arguments. The methods have the type \_PyCFunctionFast. The first parameter is self, the second parameter is a C array of PyObject\* values indicating the arguments and the third parameter is the number of arguments (the length of the array).

New in version 3.7.

Changed in version 3.10: METH\_FASTCALL is now part of the stable ABI.

## METH\_FASTCALL | METH\_KEYWORDS

Extension of METH\_FASTCALL supporting also keyword arguments, with methods of type \_PyCFunctionFastWithKeywords. Keyword arguments are passed the same way as in the vectorcall protocol: there is an additional fourth PyObject\* parameter which is a tuple representing the names of the keyword arguments (which are guaranteed to be strings) or possibly NULL if there are no keywords. The values of the keyword arguments are stored in the args array, after the positional arguments.

New in version 3.7.

## METH\_METHOD | METH\_FASTCALL | METH\_KEYWORDS

Extension of METH\_FASTCALL | METH\_KEYWORDS supporting the defining class, that is, the class that contains the method in question. The defining class might be a superclass of Py\_TYPE(self).

The method needs to be of type PyCMethod, the same as for METH\_FASTCALL | METH\_KEYWORDS with defining\_class argument added after self.

New in version 3.9.

## METH\_NOARGS

Methods without parameters don’t need to check whether arguments are given if they are listed with the METH\_NOARGS flag. They need to be of type PyCFunction. The first parameter is typically named self and will hold a reference to the module or object instance. In all cases the second parameter will be NULL.

## METH\_O

Methods with a single object argument can be listed with the METH\_O flag, instead of invoking PyArg\_ParseTuple() with a "O" argument. They have the type PyCFunction, with the self parameter, and a PyObject\* parameter representing the single argument.

These two constants are not used to indicate the calling convention but the binding when use with methods of classes. These may not be used for functions defined for modules. At most one of these flags may be set for any given method.

## METH\_CLASS

The method will be passed the type object as the first parameter rather than an instance of the type. This is used to create class methods, similar to what is created when using the classmethod() built-in function.

## METH\_STATIC

The method will be passed NULL as the first parameter rather than an instance of the type. This is used to create static methods, similar to what is created when using the staticmethod() built-in function.

One other constant controls whether a method is loaded in place of another definition with the same method name.

## METH\_COEXIST

The method will be loaded in place of existing definitions. Without METH\_COEXIST, the default is to skip repeated definitions. Since slot wrappers are loaded before the method table, the existence of a sq\_contains slot, for example, would generate a wrapped method named \_\_contains\_\_() and preclude the loading of a corresponding PyCFunction with the same name. With the flag defined, the PyCFunction will be loaded in

place of the wrapper object and will co-exist with the slot. This is helpful because calls to PyCFunctions are optimized more than wrapper object calls.

## 12.2.3 Accessing attributes of extension types

## type PyMemberDef

Part of the Stable ABI (including all members). Structure which describes an attribute of a type which corresponds to a C struct member. Its fields are:

| Field | C Type | Meaning |
| --- | --- | --- |
| name | const char * | name of the member |
| type | int | the type of the member in the C struct |
| offset | Py_ssize_t | the offset in bytes that the member is located on the type's object struct |
| flags | int | flag bits indicating if the field should be read-only or writable |
| doc | const char * | points to the contents of the docstring |

type can be one of many T\_ macros corresponding to various C types. When the member is accessed in Python, it will be converted to the equivalent Python type.

| Macro name | C type |
| --- | --- |
| T_SHORT | short |
| T_INT | int |
| T_LONG | long |
| T_FLOAT | float |
| T_DOUBLE | double |
| T_STRING | const char * |
| T_OBJECT | PyObject * |
| T_OBJECT_EX | PyObject * |
| T_CHAR | char |
| T_BYTE | char |
| T_UBYTE | unsigned char |
| T_UINT | unsigned int |
| T_USHORT | unsigned short |
| T_ULONG | unsigned long |
| T_BOOL | char |
| T_LONGLONG | long long |
| T_ULONGLONG | unsigned long long |
| T_PYSSIZET | Py_ssize_t |

T\_OBJECT and T\_OBJECT\_EX differ in that T\_OBJECT returns None if the member is NULL and T\_OBJECT\_EX raises an AttributeError. Try to use T\_OBJECT\_EX over T\_OBJECT because T\_OBJECT\_EX handles use of the del statement on that attribute more correctly than T\_OBJECT.

flags can be 0 for write and read access or READONLY for read-only access. Using T\_STRING for type implies READONLY. T\_STRING data is interpreted as UTF-8. Only T\_OBJECT and T\_OBJECT\_EX members can be deleted. (They are set to NULL).

Heap allocated types (created using PyType\_FromSpec() or similar), PyMemberDef may contain definitions for the special members \_\_dictoffset\_\_, \_\_weaklistoffset\_\_ and \_vectorcalloffset\_\_, corresponding to tp\_dictoffset, tp\_weaklistoffset and tp\_vectorcall\_offset in type objects. These must be defined with T\_PYSSIZET and READONLY, for example:

```c
static PyMemberDef spam_type_members[] = {
    {"__dictoffset__", T_PYSSIZET, offsetof(Spam_object, dict), READONLY},
    {NULL}  /* Sentinel */
};
```

PyObject \***PyMember\_GetOne**(**const** char \*obj\_addr, **struct** PyMemberDef \*m) Get an attribute belonging to the object at address obj\_addr. The attribute is described by PyMemberDef m. Returns NULL on error.

int **PyMember\_SetOne**(char \*obj\_addr, **struct** PyMemberDef \*m, PyObject \*o)

Set an attribute belonging to the object at address obj\_addr to object o. The attribute to set is described by PyMemberDef m. Returns 0 if successful and a negative value on failure.

## type PyGetSetDef

Part of the Stable ABI (including all members). Structure to define property-like access for a type. See also description of the PyTypeObject.tp\_getset slot.

| Field | C Type | Meaning |
| --- | --- | --- |
| name | constchar* | attribute name |
| get | getter | C function to get the attribute |
| set | setter | optionalCfunctiontosetordeletetheattribute,ifomittedtheattributeisreadonly |
| doc | constchar* | optional docstring |
| clo-sure | void * | optional function pointer, providing additional data for getter and setter |

The get function takes one PyObject\* parameter (the instance) and a function pointer (the associated closure):

```txt
typedef PyObject *(*getter)(PyObject *, void *);
```

It should return a new reference on success or NULL with a set exception on failure.

set functions take two PyObject\* parameters (the instance and the value to be set) and a function pointer (the associated closure):

```txt
typedef int (*setter)(PyObject *, PyObject *, void *);
```

In case the attribute should be deleted the second parameter is NULL. Should return 0 on success or -1 with a set exception on failure.

## 12.3 Type Objects

Perhaps one of the most important structures of the Python object system is the structure that defines a new type: the PyTypeObject structure. Type objects can be handled using any of the PyObject\_\* or PyType\_\* functions, but do not offer much that’s interesting to most Python applications. These objects are fundamental to how objects behave, so they are very important to the interpreter itself and to any extension module that implements new types.

Type objects are fairly large compared to most of the standard types. The reason for the size is that each type object stores a large number of values, mostly C function pointers, each of which implements a small part of the type’s functionality. The fields of the type object are examined in detail in this section. The fields will be described in the order in which they occur in the structure.

In addition to the following quick reference, the Examples section provides at-a-glance insight into the meaning and use of PyTypeObject.

## 12.3.1 Quick Reference

**“tp slots”**

<table><tbody><tr><td rowspan="2">PyTypeObject Slot<sup>1</sup></td><td rowspan="2">Type</td><td rowspan="2">special methods/attrs</td><td colspan="4">Info<sup>2</sup></td></tr><tr><td>O</td><td>T</td><td>D</td><td>I</td></tr><tr><td>&lt;R&gt; tp_name</td><td>const char *</td><td>__name__</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>tp_basicsize</td><td>Py_ssize_t</td><td></td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>tp_itemsize</td><td>Py_ssize_t</td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>tp_dealloc</td><td>destructor</td><td></td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>tp_vectorcall_offset</td><td>Py_ssize_t</td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>(tp_getattr)</td><td>getattrfunc</td><td>__getattribute__, __getattr__</td><td></td><td></td><td></td><td>G</td></tr><tr><td>(tp_setattr)</td><td>setattrfunc</td><td>__setattr__, __delattr__</td><td></td><td></td><td></td><td>G</td></tr><tr><td>tp_as_async</td><td>PyAsyncMethods *</td><td>sub-slots</td><td></td><td></td><td></td><td>%</td></tr><tr><td>tp_repr</td><td>reprfunc</td><td>__repr__</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>tp_as_number</td><td>PyNumberMethods *</td><td>sub-slots</td><td></td><td></td><td></td><td>%</td></tr><tr><td>tp_as_sequence</td><td>PySequenceMethods *</td><td>sub-slots</td><td></td><td></td><td></td><td>%</td></tr><tr><td>tp_as_mapping</td><td>PyMappingMethods *</td><td>sub-slots</td><td></td><td></td><td></td><td>%</td></tr><tr><td>tp_hash</td><td>hashfunc</td><td>__hash__</td><td>X</td><td></td><td></td><td>G</td></tr><tr><td>tp_call</td><td>ternaryfunc</td><td>__call__</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>tp_str</td><td>reprfunc</td><td>__str__</td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>tp_getattro</td><td>getattrofunc</td><td>__getattribute__, __getattr__</td><td>X</td><td>X</td><td></td><td>G</td></tr><tr><td>tp_setattro</td><td>setattrofunc</td><td>__setattr__, __delattr__</td><td>X</td><td>X</td><td></td><td>G</td></tr><tr><td>tp_as_buffer</td><td>PyBufferProcs *</td><td></td><td></td><td></td><td></td><td>%</td></tr><tr><td>tp_flags</td><td>unsigned long</td><td></td><td>X</td><td>X</td><td></td><td>?</td></tr><tr><td>tp_doc</td><td>const char *</td><td>__doc__</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>tp_traverse</td><td>traverseproc</td><td></td><td></td><td>X</td><td></td><td>G</td></tr><tr><td>tp_clear</td><td>inquiry</td><td></td><td></td><td>X</td><td></td><td>G</td></tr><tr><td>tp_richcompare</td><td>richcmpfunc</td><td>__lt__, __le__, __eq__, __ne__, __gt__, __ge__</td><td>X</td><td></td><td></td><td>G</td></tr><tr><td>tp_weaklistoffset</td><td>Py_ssize_t</td><td></td><td></td><td>X</td><td></td><td>?</td></tr><tr><td>tp_iter</td><td>getiterfunc</td><td>__iter__</td><td></td><td></td><td></td><td>X</td></tr><tr><td>tp_iternext</td><td>iternextfunc</td><td>__next__</td><td></td><td></td><td></td><td>X</td></tr><tr><td>tp_methods</td><td>PyMethodDef []</td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>tp_members</td><td>PyMemberDef []</td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>tp_getset</td><td>PyGetSetDef []</td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>tp_base</td><td>PyTypeObject *</td><td>__base__</td><td></td><td></td><td>X</td><td></td></tr><tr><td>tp_dict</td><td>PyObject *</td><td>__dict__</td><td></td><td></td><td>?</td><td></td></tr><tr><td>tp_descr_get</td><td>descrgetfunc</td><td>__get__</td><td></td><td></td><td></td><td>X</td></tr><tr><td>tp_descr_set</td><td>descrsetfunc</td><td>__set__, __delete__</td><td></td><td></td><td></td><td>X</td></tr><tr><td>tp_dictoffset</td><td>Py_ssize_t</td><td></td><td></td><td>X</td><td></td><td>?</td></tr><tr><td>tp_init</td><td>initproc</td><td>__init__</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>tp_alloc</td><td>allocfunc</td><td></td><td>X</td><td></td><td>?</td><td>?</td></tr><tr><td>tp_new</td><td>newfunc</td><td>__new__</td><td>X</td><td>X</td><td>?</td><td>?</td></tr><tr><td>tp_free</td><td>freefunc</td><td></td><td>X</td><td>X</td><td>?</td><td>?</td></tr><tr><td>tp_is_gc</td><td>inquiry</td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>&lt;tp_bases&gt;</td><td>PyObject *</td><td>__bases__</td><td></td><td></td><td>~</td><td></td></tr><tr><td>&lt;tp_mro&gt;</td><td>PyObject *</td><td>__mro__</td><td></td><td></td><td>~</td><td></td></tr><tr><td>[tp_cache]</td><td>PyObject *</td><td></td><td></td><td></td><td colspan="2"></td></tr><tr><td>[tp_subclasses]</td><td>PyObject *</td><td>__subclasses__</td><td></td><td></td><td colspan="2"></td></tr><tr><td>[tp_weaklist]</td><td>PyObject *</td><td></td><td></td><td></td><td colspan="2"></td></tr><tr><td>(tp_del)</td><td>destructor</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[tp_version_tag]</td><td>unsigned int</td><td></td><td></td><td></td><td colspan="2"></td></tr><tr><td>tp_finalize</td><td>destructor</td><td>__del__</td><td></td><td></td><td></td><td>X</td></tr></tbody></table>

continues on next page

Table 1 – continued from previous page

<table><tbody><tr><td rowspan="2">PyTypeObject Slot<sup>1</sup></td><td rowspan="2">Type</td><td rowspan="2">special methods/attrs</td><td colspan="4">Info<sup>2</sup></td></tr><tr><td>O</td><td>T</td><td>D</td><td>I</td></tr><tr><td>tp_vectorcall</td><td>vectorcallfunc</td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

## sub-slots

<table><tbody><tr><td>Slot</td><td>Type</td><td>special methods</td></tr><tr><td>am_await</td><td>unaryfunc</td><td>__await__</td></tr><tr><td>am_aiter</td><td>unaryfunc</td><td>__aiter__</td></tr><tr><td>am_anext</td><td>unaryfunc</td><td>__anext__</td></tr><tr><td>am_send</td><td>sendfunc</td><td></td></tr><tr><td colspan="3"></td></tr><tr><td>nb_add</td><td>binaryfunc</td><td>__add__ __radd__</td></tr><tr><td>nb_inplace_add</td><td>binaryfunc</td><td>__iadd__</td></tr><tr><td>nb_subtract</td><td>binaryfunc</td><td>__sub__ __rsub__</td></tr><tr><td>nb_inplace_subtract</td><td>binaryfunc</td><td>__isub__</td></tr><tr><td>nb_multiply</td><td>binaryfunc</td><td>__mul__ __rmul__</td></tr><tr><td>nb_inplace_multiply</td><td>binaryfunc</td><td>__imul__</td></tr><tr><td>nb_remainder</td><td>binaryfunc</td><td>__mod__ __rmod__</td></tr><tr><td>nb_inplace_remainder</td><td>binaryfunc</td><td>__imod__</td></tr><tr><td>nb_divmod</td><td>binaryfunc</td><td>__divmod__ __rdiv-mod__</td></tr><tr><td>nb_power</td><td>ternaryfunc</td><td>__pow__ __rpow__</td></tr><tr><td>nb_inplace_power</td><td>ternaryfunc</td><td>__ipow__</td></tr><tr><td>nb_negative</td><td>unaryfunc</td><td>__neg__</td></tr><tr><td>nb_positive</td><td>unaryfunc</td><td>__pos__</td></tr><tr><td>nb_absolute</td><td>unaryfunc</td><td>__abs__</td></tr><tr><td>nb_bool</td><td>inquiry</td><td>__bool__</td></tr><tr><td>nb_invert</td><td>unaryfunc</td><td>__invert__</td></tr><tr><td>nb_lshift</td><td>binaryfunc</td><td>__lshift__ __rlshift__</td></tr><tr><td>nb_inplace_lshift</td><td>binaryfunc</td><td>__ilshift__</td></tr><tr><td>nb_rshift</td><td>binaryfunc</td><td>__rshift____rrshift__</td></tr><tr><td>nb_inplace_rshift</td><td>binaryfunc</td><td>__irshift__</td></tr><tr><td>nb_and</td><td>binaryfunc</td><td>__and__ __rand__</td></tr></tbody></table>

continues on next page

```txt
¹(): A slot name in parentheses indicates it is (effectively) deprecated.
<>: Names in angle brackets should be initially set to NULL and treated as read-only.
[]: Names in square brackets are for internal use only.
<R> (as a prefix) means the field is required (must be non-NULL).
² Columns:
“O”: set on PyBaseObject_Type
“T”: set on PyType_Type
“D”: default (if slot is set to NULL)

X - PyType_Ready sets this value if it is NULL
~ - PyType_Ready always sets this value (it should be NULL)
? - PyType_Ready may set this value depending on other slots

Also see the inheritance column ("I").
“T”: inheritance

X - type slot is inherited via *PyType_Ready* if defined with a *NULL* value
% - the slots of the sub-struct are inherited individually
G - inherited, but only in combination with other slots; see the slot's description
? - it's complicated; see the slot's description
Note that some slots are effectively inherited through the normal attribute lookup chain.
```

Table 2 – continued from previous page

<table><tbody><tr><td>Slot</td><td>Type</td><td>special methods</td></tr><tr><td>nb_inplace_and</td><td>binaryfunc</td><td>__iand__</td></tr><tr><td>nb_xor</td><td>binaryfunc</td><td>__xor__ __rxor__</td></tr><tr><td>nb_inplace_xor</td><td>binaryfunc</td><td>__ixor__</td></tr><tr><td>nb_or</td><td>binaryfunc</td><td>__or__ __ror__</td></tr><tr><td>nb_inplace_or</td><td>binaryfunc</td><td>__ior__</td></tr><tr><td>nb_int</td><td>unaryfunc</td><td>__int__</td></tr><tr><td>nb_reserved</td><td>void *</td><td></td></tr><tr><td>nb_float</td><td>unaryfunc</td><td>__float__</td></tr><tr><td>nb_floor_divide</td><td>binaryfunc</td><td>__floordiv__</td></tr><tr><td>nb_inplace_floor_divide</td><td>binaryfunc</td><td>__ifloordiv__</td></tr><tr><td>nb_true_divide</td><td>binaryfunc</td><td>__truediv__</td></tr><tr><td>nb_inplace_true_divide</td><td>binaryfunc</td><td>__itruediv__</td></tr><tr><td>nb_index</td><td>unaryfunc</td><td>__index__</td></tr><tr><td>nb_matrix_multiply</td><td>binaryfunc</td><td>__matmul__ __rmat-mul__</td></tr><tr><td>nb_inplace_matrix_multiply</td><td>binaryfunc</td><td>__imatmul__</td></tr><tr><td colspan="3"></td></tr><tr><td>mp_length</td><td>lenfunc</td><td>__len__</td></tr><tr><td>mp_subscript</td><td>binaryfunc</td><td>__getitem__</td></tr><tr><td>mp_ass_subscript</td><td>objobjargproc</td><td>__setitem__,__delitem__</td></tr><tr><td colspan="3"></td></tr><tr><td>sq_length</td><td>lenfunc</td><td>__len__</td></tr><tr><td>sq_concat</td><td>binaryfunc</td><td>__add__</td></tr><tr><td>sq_repeat</td><td>ssizeargfunc</td><td>__mul__</td></tr><tr><td>sq_item</td><td>ssizeargfunc</td><td>__getitem__</td></tr><tr><td>sq_ass_item</td><td>ssizeobjargproc</td><td>__setitem____delitem__</td></tr><tr><td>sq_contains</td><td>objobjproc</td><td>__contains__</td></tr><tr><td>sq_inplace_concat</td><td>binaryfunc</td><td>__iadd__</td></tr><tr><td>sq_inplace_repeat</td><td>ssizeargfunc</td><td>__imul__</td></tr><tr><td colspan="3"></td></tr><tr><td>bf_getbuffer</td><td>getbufferproc()</td><td></td></tr><tr><td>bf_releasebuffer</td><td>releasebufferproc()</td><td></td></tr></tbody></table>

## slot typedefs

| typedef | Parameter Types | Return Type |
| --- | --- | --- |
| allocfunc | PyTypeObject * Py_ssize_t | PyObject * |
| destructor | void * | void |
| freefunc | void * | void |
| traverseproc | void * visitproc void * | int |
| newfunc | PyObject * PyObject * PyObject * | PyObject * |
| initproc | PyObject * PyObject * PyObject * | int |
| reprfunc | PyObject * | PyObject * |
| getattrfunc | PyObject * const char * | PyObject * |
| setattrfunc | PyObject * const char * PyObject * | int |
| getattrofunc | PyObject * PyObject * | PyObject * |
| setattrofunc | PyObject * PyObject * PyObject * | int |
| descrgetfunc | PyObject * PyObject * PyObject * | PyObject * |
| descrsetfunc | PyObject * PyObject * | int |
| 12.3. Type Objects | PyObject * | 225 |
| hashfunc | PyObject * | Py_hash_t |
| richcmpfunc |  | PyObject * |

See Slot Type typedefs below for more detail.

## 12.3.2 PyTypeObject Definition

The structure definition for PyTypeObject can be found in Include/object.h. For convenience of reference, this repeats the definition found there:

```c
typedef struct _typeobject {
    PyObject_VAR_HEAD
    const char *tp_name; /* For printing, in format "<module>.<name>" */
    Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */

    /* Methods to implement standard operations */

    destructor tp_dealloc;
    Py_ssize_t tp_vectorcall_offset;
    getattrfunc tp_getattr;
    setattrfunc tp_setattr;
    PyAsyncMethods *tp_as_async; /* formerly known as tp_compare (Python 2)
                             or tp_reserved (Python 3) */
    refrunc tp_repr;

    /* Method suites for standard classes */

    PyNumberMethods *tp_as_number;
    PySequenceMethods *tp_as_sequence;
    PyMappingMethods *tp_as_mapping;

    /* More standard operations (here for binary compatibility) */

    hashfunc tp_hash;
    ternaryfunc tp_call;
    refrunc tp_str;
    getattrofunc tp_getattro;
    setattrofunc tp_setattro;

    /* Functions to access object as input/output buffer */
    PyBufferProcs *tp_as_buffer;

    /* Flags to define presence of optional/expanded features */
    unsigned long tp_flags;

    const char *tp_doc; /* Documentation string */

    /* Assigned meaning in release 2.0 */
    /* call function for all accessible objects */
    traverseproc tp_traverse;

    /* delete references to contained objects */
    inquiry tp_clear;

    /* Assigned meaning in release 2.1 */
    /* rich comparisons */
    richcmpfunc tp_richcompare;

    /* weak reference enabler */
    Py_ssize_t tp_weaklistoffset;

    /* Iterators */
    getiterfunc tp_iter;
    iternextfunc tp_iternext;
```

(continues on next page)

(continued from previous page)

```c
/* Attribute descriptor and subclassing stuff */
struct PyMethodDef *tp_methods;
struct PyMemberDef *tp_members;
struct PyGetSetDef *tp_getset;
// Strong reference on a heap type, borrowed reference on a static type
struct _typeobject *tp_base;
PyObject *tp_dict;
descrgetfunc tp_descr_get;
descrsetfunc tp_descr_set;
Py_ssize_t tp_dictoffset;
initproc tp_init;
allocfunc tp_alloc;
newfunc tp_new;
freefunc tp_free; /* Low-level free-memory routine */
inquiry tp_is_gc; /* For PyObject_IS_GC */
PyObject *tp_bases;
PyObject *tp_mro; /* method resolution order */
PyObject *tp_cache;
PyObject *tp_subclasses;
PyObject *tp_weaklist;
destructor tp_del;

/* Type attribute cache version tag. Added in version 2.6 */
unsigned int tp_version_tag;

destructor tp_finalize;
vectorcallfunc tp_vectorcall;
} PyTypeObject;
```

## 12.3.3 PyObject Slots

The type object structure extends the PyVarObject structure. The ob\_size field is used for dynamic types (created by type\_new(), usually called from a class statement). Note that PyType\_Type (the metatype) initializes tp\_itemsize, which means that its instances (i.e. type objects) must have the ob\_size field.

## Py\_ssize\_t PyObject.ob\_refcnt

Part of the Stable ABI. This is the type object’s reference count, initialized to 1 by the PyObject\_HEAD\_INIT macro. Note that for statically allocated type objects, the type’s instances (objects whose ob\_type points back to the type) do not count as references. But for dynamically allocated type objects, the instances do count as references.

## Inheritance:

This field is not inherited by subtypes.

## PyTypeObject \*PyObject.ob\_type

Part of the Stable ABI. This is the type’s type, in other words its metatype. It is initialized by the argument to the PyObject\_HEAD\_INIT macro, and its value should normally be &PyType\_Type. However, for dynamically loadable extension modules that must be usable on Windows (at least), the compiler complains that this is not a valid initializer. Therefore, the convention is to pass NULL to the PyObject\_HEAD\_INIT macro and to initialize this field explicitly at the start of the module’s initialization function, before doing anything else. This is typically done like this:

```txt
Foo_Type.ob_type = &PyType_Type;
```

This should be done before any instances of the type are created. PyType\_Ready() checks if ob\_type is NULL, and if so, initializes it to the ob\_type field of the base class. PyType\_Ready() will not change this field if it is non-zero.

## Inheritance:

This field is inherited by subtypes.

```txt
PyObject *PyObject._ob_next
txt
PyObject *PyObject._ob_prev
```

These fields are only present when the macro Py\_TRACE\_REFS is defined (see the configure --with-trace-refs option).

Their initialization to NULL is taken care of by the PyObject\_HEAD\_INIT macro. For statically allocated objects, these fields always remain NULL. For dynamically allocated objects, these two fields are used to link the object into a doubly linked list of all live objects on the heap.

This could be used for various debugging purposes; currently the only uses are the sys.getobjects() function and to print the objects that are still alive at the end of a run when the environment variable PYTHONDUMPREFS is set.

## Inheritance:

These fields are not inherited by subtypes.

## 12.3.4 PyVarObject Slots

## Py\_ssize\_t PyVarObject.ob\_size

Part of the Stable ABI. For statically allocated type objects, this should be initialized to zero. For dynamically allocated type objects, this field has a special internal meaning.

## Inheritance:

This field is not inherited by subtypes.

## 12.3.5 PyTypeObject Slots

Each slot has a section describing inheritance. If PyType\_Ready() may set a value when the field is set to NULL then there will also be a “Default” section. (Note that many fields set on PyBaseObject\_Type and PyType\_Type effectively act as defaults.)

## const char \*PyTypeObject.tp\_name

Pointer to a NUL-terminated string containing the name of the type. For types that are accessible as module globals, the string should be the full module name, followed by a dot, followed by the type name; for built-in types, it should be just the type name. If the module is a submodule of a package, the full package name is part of the full module name. For example, a type named T defined in module M in subpackage Q in package P should have the tp\_name initializer "P.Q.M.T".

For dynamically allocated type objects, this should just be the type name, and the module name explicitly stored in the type dict as the value for key '\_\_module\_\_'.

For statically allocated type objects, the tp\_name field should contain a dot. Everything before the last dot is made accessible as the \_\_module\_\_ attribute, and everything after the last dot is made accessible as the name\_\_ attribute.

If no dot is present, the entire tp\_name field is made accessible as the \_\_name\_\_ attribute, and the module\_\_ attribute is undefined (unless explicitly set in the dictionary, as explained above). This means your type will be impossible to pickle. Additionally, it will not be listed in module documentations created with pydoc.

This field must not be NULL. It is the only required field in PyTypeObject() (other than potentially tp\_itemsize).

## Inheritance:

This field is not inherited by subtypes.

Py\_ssize\_t PyTypeObject.**tp\_basicsize**

## Py\_ssize\_t PyTypeObject.tp\_itemsize

These fields allow calculating the size in bytes of instances of the type.

There are two kinds of types: types with fixed-length instances have a zero tp\_itemsize field, types with variable-length instances have a non-zero tp\_itemsize field. For a type with fixed-length instances, all instances have the same size, given in tp\_basicsize.

For a type with variable-length instances, the instances must have an ob\_size field, and the instance size is tp\_basicsize plus N times tp\_itemsize, where N is the “length” of the object. The value of N is typically stored in the instance’s ob\_size field. There are exceptions: for example, ints use a negative ob\_size to indicate a negative number, and N is abs(ob\_size) there. Also, the presence of an ob\_size field in the instance layout doesn’t mean that the instance structure is variable-length (for example, the structure for the list type has fixed-length instances, yet those instances have a meaningful ob\_size field).

The basic size includes the fields in the instance declared by the macro PyObject\_HEAD or PyObject\_VAR\_HEAD (whichever is used to declare the instance struct) and this in turn includes the \_ob\_prev and \_ob\_next fields if they are present. This means that the only correct way to get an initializer for the tp\_basicsize is to use the sizeof operator on the struct used to declare the instance layout. The basic size does not include the GC header size.

A note about alignment: if the variable items require a particular alignment, this should be taken care of by the value of tp\_basicsize. Example: suppose a type implements an array of double. tp\_itemsize is sizeof(double). It is the programmer’s responsibility that tp\_basicsize is a multiple of sizeof(double) (assuming this is the alignment requirement for double).

For any type with variable-length instances, this field must not be NULL.

## Inheritance:

These fields are inherited separately by subtypes. If the base type has a non-zero tp\_itemsize, it is generally not safe to set tp\_itemsize to a different non-zero value in a subtype (though this depends on the implementation of the base type).

## destructor PyTypeObject.tp\_dealloc

A pointer to the instance destructor function. This function must be defined unless the type guarantees that its instances will never be deallocated (as is the case for the singletons None and Ellipsis). The function signature is:

```c
void tp_dealloc(PyObject *self);
```

The destructor function is called by the Py\_DECREF() and Py\_XDECREF() macros when the new reference count is zero. At this point, the instance is still in existence, but there are no references to it. The destructor function should free all references which the instance owns, free all memory buffers owned by the instance (using the freeing function corresponding to the allocation function used to allocate the buffer), and call the type’s tp\_free function. If the type is not subtypable (doesn’t have the Py\_TPFLAGS\_BASETYPE flag bit set), it is permissible to call the object deallocator directly instead of via tp\_free. The object deallocator should be the one used to allocate the instance; this is normally PyObject\_Del() if the instance was allocated using PyObject\_New() or PyObject\_VarNew(), or PyObject\_GC\_Del() if the instance was allocated using PyObject\_GC\_New() or PyObject\_GC\_NewVar().

If the type supports garbage collection (has the Py\_TPFLAGS\_HAVE\_GC flag bit set), the destructor should call PyObject\_GC\_UnTrack() before clearing any member fields.

```c
static void foo_dealloc(foo_object *self) {
    PyObject_GC_UnTrack(self);
    Py_CLEAR(self->ref);
    Py_TYPE(self)->tp_free((PyObject *)self);
}
```

Finally, if the type is heap allocated (Py\_TPFLAGS\_HEAPTYPE), the deallocator should release the owned reference to its type object (via Py\_DECREF()) after calling the type deallocator. In order to avoid dangling pointers, the recommended way to achieve this is:

```c
static void foo_dealloc(foo_object *self) {
    PyTypeObject *tp = Py_TYPE(self);
    // free references and buffers here
    tp->tp_free(self);
    Py_DECREF(tp);
}
```

## Inheritance:

This field is inherited by subtypes.

## Py\_ssize\_t PyTypeObject.tp\_vectorcall\_offset

An optional offset to a per-instance function that implements calling the object using the vectorcall protocol, a more efficient alternative of the simpler tp\_call.

This field is only used if the flag Py\_TPFLAGS\_HAVE\_VECTORCALL is set. If so, this must be a positive integer containing the offset in the instance of a vectorcallfunc pointer.

The vectorcallfunc pointer may be NULL, in which case the instance behaves as if Py\_TPFLAGS\_HAVE\_VECTORCALL was not set: calling the instance falls back to tp\_call.

Any class that sets Py\_TPFLAGS\_HAVE\_VECTORCALL must also set tp\_call and make sure its behaviour is consistent with the vectorcallfunc function. This can be done by setting tp\_call to PyVectorcall\_Call().

**Warning:** It is not recommended for heap types to implement the vectorcall protocol. When a user sets \_\_call\_\_ in Python code, only tp\_call is updated, likely making it inconsistent with the vectorcall function.

Changed in version 3.8: Before version 3.8, this slot was named tp\_print. In Python 2.x, it was used for printing to a file. In Python 3.0 to 3.7, it was unused.

## Inheritance:

This field is always inherited. However, the Py\_TPFLAGS\_HAVE\_VECTORCALL flag is not always inherited. If it’s not, then the subclass won’t use vectorcall, except when PyVectorcall\_Call() is explicitly called. This is in particular the case for heap types (including subclasses defined in Python).

## getattrfunc PyTypeObject.tp\_getattr

An optional pointer to the get-attribute-string function.

This field is deprecated. When it is defined, it should point to a function that acts the same as the tp\_getattro function, but taking a C string instead of a Python string object to give the attribute name.

## Inheritance:

Group: tp\_getattr, tp\_getattro

This field is inherited by subtypes together with tp\_getattro: a subtype inherits both tp\_getattr and tp\_getattro from its base type when the subtype’s tp\_getattr and tp\_getattro are both NULL.

## setattrfunc PyTypeObject.tp\_setattr

An optional pointer to the function for setting and deleting attributes.

This field is deprecated. When it is defined, it should point to a function that acts the same as the tp\_setattro function, but taking a C string instead of a Python string object to give the attribute name.

## Inheritance:

Group: tp\_setattr, tp\_setattro

This field is inherited by subtypes together with tp\_setattro: a subtype inherits both tp\_setattr and tp\_setattro from its base type when the subtype’s tp\_setattr and tp\_setattro are both NULL.

## PyAsyncMethods \*PyTypeObject.tp\_as\_async

Pointer to an additional structure that contains fields relevant only to objects which implement awaitable and asynchronous iterator protocols at the C-level. See Async Object Structures for details.

New in version 3.5: Formerly known as tp\_compare and tp\_reserved.

## Inheritance:

The tp\_as\_async field is not inherited, but the contained fields are inherited individually.

## reprfunc PyTypeObject.tp\_repr

An optional pointer to a function that implements the built-in function repr().

The signature is the same as for PyObject\_Repr():

```txt
PyObject *tp_repr(PyObject *self);
```

The function must return a string or a Unicode object. Ideally, this function should return a string that, when passed to eval(), given a suitable environment, returns an object with the same value. If this is not feasible, it should return a string starting with '<' and ending with '>' from which both the type and the value of the object can be deduced.

## Inheritance:

This field is inherited by subtypes.

## Default:

When this field is not set, a string of the form <%s object at %p> is returned, where %s is replaced by the type name, and %p by the object’s memory address.

## PyNumberMethods \*PyTypeObject.tp\_as\_number

Pointer to an additional structure that contains fields relevant only to objects which implement the number protocol. These fields are documented in Number Object Structures.

## Inheritance:

The tp\_as\_number field is not inherited, but the contained fields are inherited individually.

## PySequenceMethods \*PyTypeObject.tp\_as\_sequence

Pointer to an additional structure that contains fields relevant only to objects which implement the sequence protocol. These fields are documented in Sequence Object Structures.

## Inheritance:

The tp\_as\_sequence field is not inherited, but the contained fields are inherited individually.

## PyMappingMethods \*PyTypeObject.tp\_as\_mapping

Pointer to an additional structure that contains fields relevant only to objects which implement the mapping protocol. These fields are documented in Mapping Object Structures.

## Inheritance:

The tp\_as\_mapping field is not inherited, but the contained fields are inherited individually.

## hashfunc PyTypeObject.tp\_hash

An optional pointer to a function that implements the built-in function hash().

The signature is the same as for PyObject\_Hash():

```c
Py_hash_t tp_hash(PyObject *);
```

The value -1 should not be returned as a normal return value; when an error occurs during the computation of the hash value, the function should set an exception and return -1.

When this field is not set (and tp\_richcompare is not set), an attempt to take the hash of the object raises TypeError. This is the same as setting it to PyObject\_HashNotImplemented().

This field can be set explicitly to PyObject\_HashNotImplemented() to block inheritance of the hash method from a parent type. This is interpreted as the equivalent of \_\_hash\_\_ = None at the Python

level, causing isinstance(o, collections.Hashable) to correctly return False. Note that the converse is also true - setting \_\_hash\_\_ = None on a class at the Python level will result in the tp\_hash slot being set to PyObject\_HashNotImplemented().

## Inheritance:

Group: tp\_hash, tp\_richcompare

This field is inherited by subtypes together with tp\_richcompare: a subtype inherits both of tp\_richcompare and tp\_hash, when the subtype’s tp\_richcompare and tp\_hash are both NULL.

## ternaryfunc PyTypeObject.tp\_call

An optional pointer to a function that implements calling the object. This should be NULL if the object is not callable. The signature is the same as for PyObject\_Call():

```c
PyObject *tp_call(PyObject *self, PyObject *args, PyObject *kwargs);
```

## Inheritance:

This field is inherited by subtypes.

## reprfunc PyTypeObject.tp\_str

An optional pointer to a function that implements the built-in operation str(). (Note that str is a type now, and str() calls the constructor for that type. This constructor calls PyObject\_Str() to do the actual work, and PyObject\_Str() will call this handler.)

The signature is the same as for PyObject\_Str():

```c
PyObject *tp_str(PyObject *self);
```

The function must return a string or a Unicode object. It should be a “friendly” string representation of the object, as this is the representation that will be used, among other things, by the print() function.

## Inheritance:

This field is inherited by subtypes.

## Default:

When this field is not set, PyObject\_Repr() is called to return a string representation.

getattrofunc PyTypeObject.**tp\_getattro**

An optional pointer to the get-attribute function.

The signature is the same as for PyObject\_GetAttr():

```txt
PyObject *tp_getattro(PyObject *self, PyObject *attr);
```

It is usually convenient to set this field to PyObject\_GenericGetAttr(), which implements the normal way of looking for object attributes.

## Inheritance:

Group: tp\_getattr, tp\_getattro

This field is inherited by subtypes together with tp\_getattr: a subtype inherits both tp\_getattr and tp\_getattro from its base type when the subtype’s tp\_getattr and tp\_getattro are both NULL.

## Default:

PyBaseObject\_Type uses PyObject\_GenericGetAttr().

```txt
setattrofunc PyTypeObject.tp_setattro
```

An optional pointer to the function for setting and deleting attributes.

The signature is the same as for PyObject\_SetAttr():

```c
int tp_setattro(PyObject *self, PyObject *attr, PyObject *value);
```

In addition, setting value to NULL to delete an attribute must be supported. It is usually convenient to set this field to PyObject\_GenericSetAttr(), which implements the normal way of setting object attributes.

## Inheritance:

Group: tp\_setattr, tp\_setattro

This field is inherited by subtypes together with tp\_setattr: a subtype inherits both tp\_setattr and tp\_setattro from its base type when the subtype’s tp\_setattr and tp\_setattro are both NULL.

## Default:

PyBaseObject\_Type uses PyObject\_GenericSetAttr().

## PyBufferProcs \*PyTypeObject.tp\_as\_buffer

Pointer to an additional structure that contains fields relevant only to objects which implement the buffer interface. These fields are documented in Buffer Object Structures.

## Inheritance:

The tp\_as\_buffer field is not inherited, but the contained fields are inherited individually.

## unsigned long PyTypeObject.tp\_flags

This field is a bit mask of various flags. Some flags indicate variant semantics for certain situations; others are used to indicate that certain fields in the type object (or in the extension structures referenced via tp\_as\_number, tp\_as\_sequence, tp\_as\_mapping, and tp\_as\_buffer) that were historically not always present are valid; if such a flag bit is clear, the type fields it guards must not be accessed and must be considered to have a zero or NULL value instead.

## Inheritance:

Inheritance of this field is complicated. Most flag bits are inherited individually, i.e. if the base type has a flag bit set, the subtype inherits this flag bit. The flag bits that pertain to extension structures are strictly inherited if the extension structure is inherited, i.e. the base type’s value of the flag bit is copied into the subtype together with a pointer to the extension structure. The Py\_TPFLAGS\_HAVE\_GC flag bit is inherited together with the tp\_traverse and tp\_clear fields, i.e. if the Py\_TPFLAGS\_HAVE\_GC flag bit is clear in the subtype and the tp\_traverse and tp\_clear fields in the subtype exist and have NULL values.

## Default:

PyBaseObject\_Type uses Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE.

## Bit Masks:

The following bit masks are currently defined; these can be ORed together using the | operator to form the value of the tp\_flags field. The macro PyType\_HasFeature() takes a type and a flags value, tp and f, and checks whether tp->tp\_flags & f is non-zero.

## Py\_TPFLAGS\_HEAPTYPE

This bit is set when the type object itself is allocated on the heap, for example, types created dynamically using PyType\_FromSpec(). In this case, the ob\_type field of its instances is considered a reference to the type, and the type object is INCREF’ed when a new instance is created, and DECREF’ed when an instance is destroyed (this does not apply to instances of subtypes; only the type referenced by the instance’s ob\_type gets INCREF’ed or DECREF’ed).

## Inheritance:

???

## Py\_TPFLAGS\_BASETYPE

This bit is set when the type can be used as the base type of another type. If this bit is clear, the type cannot be subtyped (similar to a “final” class in Java).

**Inheritance:**

???

## Py\_TPFLAGS\_READY

This bit is set when the type object has been fully initialized by PyType\_Ready().

## Inheritance:

???

## Py\_TPFLAGS\_READYING

This bit is set while PyType\_Ready() is in the process of initializing the type object.

## Inheritance:

```txt
???
```

## Py\_TPFLAGS\_HAVE\_GC

This bit is set when the object supports garbage collection. If this bit is set, instances must be created using PyObject\_GC\_New() and destroyed using PyObject\_GC\_Del(). More information in section Supporting Cyclic Garbage Collection. This bit also implies that the GC-related fields tp\_traverse and tp\_clear are present in the type object.

## Inheritance:

```txt
Group: Py_TPFLAGS_HAVE_GC, tp_traverse, tp_clear
```

The Py\_TPFLAGS\_HAVE\_GC flag bit is inherited together with the tp\_traverse and tp\_clear fields, i.e. if the Py\_TPFLAGS\_HAVE\_GC flag bit is clear in the subtype and the tp\_traverse and tp\_clear fields in the subtype exist and have NULL values.

## Py\_TPFLAGS\_DEFAULT

This is a bitmask of all the bits that pertain to the existence of certain fields in the type object and its extension structures. Currently, it includes the following bits: Py\_TPFLAGS\_HAVE\_STACKLESS\_EXTENSION.

## Inheritance:

???

## Py\_TPFLAGS\_METHOD\_DESCRIPTOR

This bit indicates that objects behave like unbound methods.

If this flag is set for type(meth), then:

• meth.\_\_get\_\_(obj, cls)(\*args, \*\*kwds) (with obj not None) must be equivalent to meth(obj, \*args, \*\*kwds).

• meth.\_\_get\_\_(None, cls)(\*args, \*\*kwds) must be equivalent to meth(\*args, \*\*kwds).

This flag enables an optimization for typical method calls like obj.meth(): it avoids creating a temporary “bound method” object for obj.meth.

New in version 3.8.

## Inheritance:

This flag is never inherited by heap types. For extension types, it is inherited whenever tp\_descr\_get is inherited.

```csv
Py_TPFLAGS_LONG_SUBCLASS
Py_TPFLAGS_LIST_SUBCLASS
Py_TPFLAGS_TUPLE_SUBCLASS
Py_TPFLAGS_BYTES_SUBCLASS
Py_TPFLAGS_UNICODE_SUBCLASS
Py_TPFLAGS_DICT_SUBCLASS
Py_TPFLAGS_BASE_EXC_SUBCLASS
```

## Py\_TPFLAGS\_TYPE\_SUBCLASS

These flags are used by functions such as PyLong\_Check() to quickly determine if a type is a subclass of a built-in type; such specific checks are faster than a generic check, like PyObject\_IsInstance(). Custom types that inherit from built-ins should have their tp\_flags set appropriately, or the code that interacts with such types will behave differently depending on what kind of check is used.

## Py\_TPFLAGS\_HAVE\_FINALIZE

This bit is set when the tp\_finalize slot is present in the type structure.

New in version 3.4.

Deprecated since version 3.8: This flag isn’t necessary anymore, as the interpreter assumes the tp\_finalize slot is always present in the type structure.

## Py\_TPFLAGS\_HAVE\_VECTORCALL

This bit is set when the class implements the vectorcall protocol. See tp\_vectorcall\_offset for details.

## Inheritance:

This bit is inherited for static subtypes if tp\_call is also inherited. Heap types do not inherit Py\_TPFLAGS\_HAVE\_VECTORCALL.

New in version 3.9.

## Py\_TPFLAGS\_IMMUTABLETYPE

This bit is set for type objects that are immutable: type attributes cannot be set nor deleted.

PyType\_Ready() automatically applies this flag to static types.

## Inheritance:

This flag is not inherited.

New in version 3.10.

## Py\_TPFLAGS\_DISALLOW\_INSTANTIATION

Disallow creating instances of the type: set tp\_new to NULL and don’t create the \_\_new\_\_ key in the type dictionary.

The flag must be set before creating the type, not after. For example, it must be set before PyType\_Ready() is called on the type.

The flag is set automatically on static types if tp\_base is NULL or &PyBaseObject\_Type and tp\_new is NULL.

## Inheritance:

This flag is not inherited. However, subclasses will not be instantiable unless they provide a non-NULL tp\_new (which is only possible via the C API).

**Note:** To disallow instantiating a class directly but allow instantiating its subclasses (e.g. for an abstract base class), do not use this flag. Instead, make tp\_new only succeed for subclasses.

New in version 3.10.

## Py\_TPFLAGS\_MAPPING

This bit indicates that instances of the class may match mapping patterns when used as the subject of a match block. It is automatically set when registering or subclassing collections.abc.Mapping, and unset when registering collections.abc.Sequence.

**Note:** Py\_TPFLAGS\_MAPPING and Py\_TPFLAGS\_SEQUENCE are mutually exclusive; it is an error to enable both flags simultaneously.

## Inheritance:

This flag is inherited by types that do not already set Py\_TPFLAGS\_SEQUENCE.

## See also:

[**PEP 634**](https://www.python.org/dev/peps/pep-0634) – Structural Pattern Matching: Specification

New in version 3.10.

## Py\_TPFLAGS\_SEQUENCE

This bit indicates that instances of the class may match sequence patterns when used as the subject of a match block. It is automatically set when registering or subclassing collections.abc. Sequence, and unset when registering collections.abc.Mapping.

**Note:** Py\_TPFLAGS\_MAPPING and Py\_TPFLAGS\_SEQUENCE are mutually exclusive; it is an error to enable both flags simultaneously.

## Inheritance:

This flag is inherited by types that do not already set Py\_TPFLAGS\_MAPPING.

## See also:

[**PEP 634**](https://www.python.org/dev/peps/pep-0634) – Structural Pattern Matching: Specification

New in version 3.10.

## const char \*PyTypeObject.tp\_doc

An optional pointer to a NUL-terminated C string giving the docstring for this type object. This is exposed as the \_\_doc\_\_ attribute on the type and instances of the type.

## Inheritance:

This field is not inherited by subtypes.

## traverseproc PyTypeObject.tp\_traverse

An optional pointer to a traversal function for the garbage collector. This is only used if the Py\_TPFLAGS\_HAVE\_GC flag bit is set. The signature is:

```c
int tp_traverse(PyObject *self, visitproc visit, void *arg);
```

More information about Python’s garbage collection scheme can be found in section Supporting Cyclic Garbage Collection.

The tp\_traverse pointer is used by the garbage collector to detect reference cycles. A typical implementation of a tp\_traverse function simply calls Py\_VISIT() on each of the instance’s members that are Python objects that the instance owns. For example, this is function local\_traverse() from the \_thread extension module:

```c
static int
local_traverse(localobject *self, visitproc visit, void *arg)
{
    Py_VISIT(self->args);
    Py_VISIT(self->kw);
    Py_VISIT(self->dict);
    return 0;
}
```

Note that Py\_VISIT() is called only on those members that can participate in reference cycles. Although there is also a self->key member, it can only be NULL or a Python string and therefore cannot be part of a reference cycle.

On the other hand, even if you know a member can never be part of a cycle, as a debugging aid you may want to visit it anyway just so the gc module’s get\_referents() function will include it.

**Warning:** When implementing tp\_traverse, only the members that the instance owns (by having strong references to them) must be visited. For instance, if an object supports weak references via the tp\_weaklist slot, the pointer supporting the linked list (what tp\_weaklist points to) must **not** be visited as the instance does not directly own the weak references to itself (the weakreference list is there to support the weak reference machinery, but the instance has no strong reference to the elements inside it, as they are allowed to be removed even if the instance is still alive).

Note that Py\_VISIT() requires the visit and arg parameters to local\_traverse() to have these specific names; don’t name them just anything.

Instances of heap-allocated types hold a reference to their type. Their traversal function must therefore either visit Py\_TYPE(self), or delegate this responsibility by calling tp\_traverse of another heap-allocated type (such as a heap-allocated superclass). If they do not, the type object may not be garbage-collected.

Changed in version 3.9: Heap-allocated types are expected to visit Py\_TYPE(self) in tp\_traverse. In earlier versions of Python, due to [bug 40217](https://bugs.python.org/issue40217), doing this may lead to crashes in subclasses.

## Inheritance:

Group: Py\_TPFLAGS\_HAVE\_GC, tp\_traverse, tp\_clear

This field is inherited by subtypes together with tp\_clear and the Py\_TPFLAGS\_HAVE\_GC flag bit: the flag bit, tp\_traverse, and tp\_clear are all inherited from the base type if they are all zero in the subtype.

inquiry PyTypeObject.**tp\_clear**

An optional pointer to a clear function for the garbage collector. This is only used if the Py\_TPFLAGS\_HAVE\_GC flag bit is set. The signature is:

```txt
int tp_clear(PyObject *);
```

The tp\_clear member function is used to break reference cycles in cyclic garbage detected by the garbage collector. Taken together, all tp\_clear functions in the system must combine to break all reference cycles. This is subtle, and if in any doubt supply a tp\_clear function. For example, the tuple type does not implement a tp\_clear function, because it’s possible to prove that no reference cycle can be composed entirely of tuples. Therefore the tp\_clear functions of other types must be sufficient to break any cycle containing a tuple. This isn’t immediately obvious, and there’s rarely a good reason to avoid implementing tp\_clear.

Implementations of tp\_clear should drop the instance’s references to those of its members that may be Python objects, and set its pointers to those members to NULL, as in the following example:

```c
static int
local_clear(localobject *self)
{
    Py_CLEAR(self->key);
    Py_CLEAR(self->args);
    Py_CLEAR(self->kw);
    Py_CLEAR(self->dict);
    return 0;
}
```

The Py\_CLEAR() macro should be used, because clearing references is delicate: the reference to the contained object must not be released (via Py\_DECREF()) until after the pointer to the contained object is set to NULL. This is because releasing the reference may cause the contained object to become trash, triggering a chain of reclamation activity that may include invoking arbitrary Python code (due to finalizers, or weakref callbacks, associated with the contained object). If it’s possible for such code to reference self again, it’s important that the pointer to the contained object be NULL at that time, so that self knows the contained object can no longer be used. The Py\_CLEAR() macro performs the operations in a safe order.

Note that tp\_clear is not always called before an instance is deallocated. For example, when reference counting is enough to determine that an object is no longer used, the cyclic garbage collector is not involved and tp\_dealloc is called directly.

Because the goal of tp\_clear functions is to break reference cycles, it’s not necessary to clear contained objects like Python strings or Python integers, which can’t participate in reference cycles. On the other hand, it may be convenient to clear all contained Python objects, and write the type’s tp\_dealloc function to invoke tp\_clear.

More information about Python’s garbage collection scheme can be found in section Supporting Cyclic Garbage Collection.

## Inheritance:

Group: Py\_TPFLAGS\_HAVE\_GC, tp\_traverse, tp\_clear

This field is inherited by subtypes together with tp\_traverse and the Py\_TPFLAGS\_HAVE\_GC flag bit: the flag bit, tp\_traverse, and tp\_clear are all inherited from the base type if they are all zero in the subtype.

## richcmpfunc PyTypeObject.tp\_richcompare

An optional pointer to the rich comparison function, whose signature is:

```c
PyObject *tp_richcompare(PyObject *self, PyObject *other, int op);
```

The first parameter is guaranteed to be an instance of the type that is defined by PyTypeObject.

The function should return the result of the comparison (usually Py\_True or Py\_False). If the comparison is undefined, it must return Py\_NotImplemented, if another error occurred it must return NULL and set an exception condition.

The following constants are defined to be used as the third argument for tp\_richcompare and for PyObject\_RichCompare():

| Constant | Comparison |
| --- | --- |
| Py_LT | &lt; |
| Py_LE | &lt;= |
| Py_EQ | == |
| Py_NE | != |
| Py_GT | > |
| Py_GE | >= |

The following macro is defined to ease writing rich comparison functions:

## Py\_RETURN\_RICHCOMPARE(VAL\_A, VAL\_B, op)

Return Py\_True or Py\_False from the function, depending on the result of a comparison. VAL\_A and VAL\_B must be orderable by C comparison operators (for example, they may be C ints or floats). The third argument specifies the requested operation, as for PyObject\_RichCompare().

The returned value is a new strong reference.

On error, sets an exception and returns NULL from the function.

New in version 3.7.

## Inheritance:

Group: tp\_hash, tp\_richcompare

This field is inherited by subtypes together with tp\_hash: a subtype inherits tp\_richcompare and tp\_hash when the subtype’s tp\_richcompare and tp\_hash are both NULL.

## Default:

PyBaseObject\_Type provides a tp\_richcompare implementation, which may be inherited. However, if only tp\_hash is defined, not even the inherited function is used and instances of the type will not be able to participate in any comparisons.

## Py\_ssize\_t PyTypeObject.tp\_weaklistoffset

If the instances of this type are weakly referenceable, this field is greater than zero and contains the offset in

the instance structure of the weak reference list head (ignoring the GC header, if present); this offset is used by PyObject\_ClearWeakRefs() and the PyWeakref\_\* functions. The instance structure needs to include a field of type PyObject\* which is initialized to NULL.

Do not confuse this field with tp\_weaklist; that is the list head for weak references to the type object itself.

## Inheritance:

This field is inherited by subtypes, but see the rules listed below. A subtype may override this offset; this means that the subtype uses a different weak reference list head than the base type. Since the list head is always found via tp\_weaklistoffset, this should not be a problem.

When a type defined by a class statement has no \_\_slots\_\_ declaration, and none of its base types are weakly referenceable, the type is made weakly referenceable by adding a weak reference list head slot to the instance layout and setting the tp\_weaklistoffset of that slot’s offset.

When a type’s \_\_slots\_\_ declaration contains a slot named \_\_weakref\_\_, that slot becomes the weak reference list head for instances of the type, and the slot’s offset is stored in the type’s tp\_weaklistoffset.

When a type’s \_\_slots\_\_ declaration does not contain a slot named \_\_weakref\_\_, the type inherits its tp\_weaklistoffset from its base type.

## getiterfunc PyTypeObject.tp\_iter

An optional pointer to a function that returns an iterator for the object. Its presence normally signals that the instances of this type are iterable (although sequences may be iterable without this function).

This function has the same signature as PyObject\_GetIter():

```c
PyObject *tp_iter(PyObject *self);
```

## Inheritance:

This field is inherited by subtypes.

iternextfunc PyTypeObject.**tp\_iternext**

An optional pointer to a function that returns the next item in an iterator. The signature is:

```c
PyObject *tp_iternext(PyObject *self);
```

When the iterator is exhausted, it must return NULL; a StopIteration exception may or may not be set. When another error occurs, it must return NULL too. Its presence signals that the instances of this type are iterators.

Iterator types should also define the tp\_iter function, and that function should return the iterator instance itself (not a new iterator instance).

This function has the same signature as PyIter\_Next().

## Inheritance:

This field is inherited by subtypes.

## struct PyMethodDef \*PyTypeObject.tp\_methods

An optional pointer to a static NULL-terminated array of PyMethodDef structures, declaring regular methods of this type.

For each entry in the array, an entry is added to the type’s dictionary (see tp\_dict below) containing a method descriptor.

## Inheritance:

This field is not inherited by subtypes (methods are inherited through a different mechanism).

## struct PyMemberDef \*PyTypeObject.tp\_members

An optional pointer to a static NULL-terminated array of PyMemberDef structures, declaring regular data members (fields or slots) of instances of this type.

For each entry in the array, an entry is added to the type’s dictionary (see tp\_dict below) containing a member descriptor.

## Inheritance:

This field is not inherited by subtypes (members are inherited through a different mechanism).

## struct PyGetSetDef \*PyTypeObject.tp\_getset

An optional pointer to a static NULL-terminated array of PyGetSetDef structures, declaring computed attributes of instances of this type.

For each entry in the array, an entry is added to the type’s dictionary (see tp\_dict below) containing a getset descriptor.

## Inheritance:

This field is not inherited by subtypes (computed attributes are inherited through a different mechanism).

## PyTypeObject \*PyTypeObject.tp\_base

An optional pointer to a base type from which type properties are inherited. At this level, only single inheritance is supported; multiple inheritance require dynamically creating a type object by calling the metatype.

**Note:** Slot initialization is subject to the rules of initializing globals. C99 requires the initializers to be “address constants”. Function designators like PyType\_GenericNew(), with implicit conversion to a pointer, are valid C99 address constants.

However, the unary ‘&’ operator applied to a non-static variable like PyBaseObject\_Type() is not required to produce an address constant. Compilers may support this (gcc does), MSVC does not. Both compilers are strictly standard conforming in this particular behavior.

Consequently, tp\_base should be set in the extension module’s init function.

## Inheritance:

This field is not inherited by subtypes (obviously).

## Default:

This field defaults to &PyBaseObject\_Type (which to Python programmers is known as the type object).

## PyObject \*PyTypeObject.tp\_dict

The type’s dictionary is stored here by PyType\_Ready().

This field should normally be initialized to NULL before PyType\_Ready is called; it may also be initialized to a dictionary containing initial attributes for the type. Once PyType\_Ready() has initialized the type, extra attributes for the type may be added to this dictionary only if they don’t correspond to overloaded operations (like \_\_add\_\_()).

## Inheritance:

This field is not inherited by subtypes (though the attributes defined in here are inherited through a different mechanism).

## Default:

If this field is NULL, PyType\_Ready() will assign a new dictionary to it.

**Warning:** It is not safe to use PyDict\_SetItem() on or otherwise modify tp\_dict with the dictionary C-API.

## descrgetfunc PyTypeObject.tp\_descr\_get

An optional pointer to a “descriptor get” function.

The function signature is:

```c
PyObject * tp_descr_get(PyObject *self, PyObject *obj, PyObject *type);
txt
descrsetfunc PyTypeObject.tp_descr_set
```

## Inheritance:

This field is inherited by subtypes.

An optional pointer to a function for setting and deleting a descriptor’s value.

The function signature is:

```c
int tp_descr_set(PyObject *self, PyObject *obj, PyObject *value);
```

The value argument is set to NULL to delete the value.

## Inheritance:

This field is inherited by subtypes.

## Py\_ssize\_t PyTypeObject.tp\_dictoffset

If the instances of this type have a dictionary containing instance variables, this field is non-zero and contains the offset in the instances of the type of the instance variable dictionary; this offset is used by PyObject\_GenericGetAttr().

Do not confuse this field with tp\_dict; that is the dictionary for attributes of the type object itself.

If the value of this field is greater than zero, it specifies the offset from the start of the instance structure. If the value is less than zero, it specifies the offset from the end of the instance structure. A negative offset is more expensive to use, and should only be used when the instance structure contains a variable-length part. This is used for example to add an instance variable dictionary to subtypes of str or tuple. Note that the tp\_basicsize field should account for the dictionary added to the end in that case, even though the dictionary is not included in the basic object layout. On a system with a pointer size of 4 bytes, tp\_dictoffset should be set to -4 to indicate that the dictionary is at the very end of the structure.

The real dictionary offset in an instance can be computed from a negative tp\_dictoffset as follows:

```python
dictoffset = tp_basicsize + abs(ob_size)*tp_itemsize + tp_dictoffset
if dictoffset is not aligned on sizeof(void*):
    round up to sizeof(void*)
```

where tp\_basicsize, tp\_itemsize and tp\_dictoffset are taken from the type object, and ob\_size is taken from the instance. The absolute value is taken because ints use the sign of ob\_size to store the sign of the number. (There’s never a need to do this calculation yourself; it is done for you by \_PyObject\_GetDictPtr().)

## Inheritance:

This field is inherited by subtypes, but see the rules listed below. A subtype may override this offset; this means that the subtype instances store the dictionary at a difference offset than the base type. Since the dictionary is always found via tp\_dictoffset, this should not be a problem.

When a type defined by a class statement has no \_\_slots\_\_ declaration, and none of its base types has an instance variable dictionary, a dictionary slot is added to the instance layout and the tp\_dictoffset is set to that slot’s offset.

When a type defined by a class statement has a \_\_slots\_\_ declaration, the type inherits its tp\_dictoffset from its base type.

(Adding a slot named \_\_dict\_\_ to the \_\_slots\_\_ declaration does not have the expected effect, it just causes confusion. Maybe this should be added as a feature just like \_\_weakref\_\_ though.)

## Default:

This slot has no default. For static types, if the field is NULL then no \_\_dict\_\_ gets created for instances.

initproc PyTypeObject.**tp\_init**

An optional pointer to an instance initialization function.

This function corresponds to the \_\_init\_\_() method of classes. Like \_\_init\_\_(), it is possible to create an instance without calling \_\_init\_\_(), and it is possible to reinitialize an instance by calling its init\_\_() method again.

The function signature is:

```c
int tp_init(PyObject *self, PyObject *args, PyObject *kwds);
```

The self argument is the instance to be initialized; the args and kwds arguments represent positional and keyword arguments of the call to \_\_init\_\_().

The tp\_init function, if not NULL, is called when an instance is created normally by calling its type, after the type’s tp\_new function has returned an instance of the type. If the tp\_new function returns an instance of some other type that is not a subtype of the original type, no tp\_init function is called; if tp\_new returns an instance of a subtype of the original type, the subtype’s tp\_init is called.

Returns 0 on success, -1 and sets an exception on error.

## Inheritance:

This field is inherited by subtypes.

## Default:

For static types this field does not have a default.

allocfunc PyTypeObject.**tp\_alloc**

An optional pointer to an instance allocation function.

The function signature is:

```txt
PyObject *tp_alloc(PyTypeObject *self, Py_ssize_t nitems);
```

## Inheritance:

This field is inherited by static subtypes, but not by dynamic subtypes (subtypes created by a class statement).

## Default:

For dynamic subtypes, this field is always set to PyType\_GenericAlloc(), to force a standard heap allocation strategy.

For static subtypes, PyBaseObject\_Type uses PyType\_GenericAlloc(). That is the recommended value for all statically defined types.

## newfunc PyTypeObject.tp\_new

An optional pointer to an instance creation function.

The function signature is:

```c
PyObject *tp_new(PyTypeObject *subtype, PyObject *args, PyObject *kwds);
```

The subtype argument is the type of the object being created; the args and kwds arguments represent positional and keyword arguments of the call to the type. Note that subtype doesn’t have to equal the type whose tp\_new function is called; it may be a subtype of that type (but not an unrelated type).

The tp\_new function should call subtype->tp\_alloc(subtype, nitems) to allocate space for the object, and then do only as much further initialization as is absolutely necessary. Initialization that can safely be ignored or repeated should be placed in the tp\_init handler. A good rule of thumb is that for immutable types, all initialization should take place in tp\_new, while for mutable types, most initialization should be deferred to tp\_init.

Set the Py\_TPFLAGS\_DISALLOW\_INSTANTIATION flag to disallow creating instances of the type in Python.

## Inheritance:

This field is inherited by subtypes, except it is not inherited by static types whose tp\_base is NULL or &PyBaseObject\_Type.

## Default:

For static types this field has no default. This means if the slot is defined as NULL, the type cannot be called to create new instances; presumably there is some other way to create instances, like a factory function.

## freefunc PyTypeObject.tp\_free

An optional pointer to an instance deallocation function. Its signature is:

```c
void tp_free(void *self);
```

An initializer that is compatible with this signature is PyObject\_Free().

## Inheritance:

This field is inherited by static subtypes, but not by dynamic subtypes (subtypes created by a class statement)

## Default:

In dynamic subtypes, this field is set to a deallocator suitable to match PyType\_GenericAlloc() and the value of the Py\_TPFLAGS\_HAVE\_GC flag bit.

For static subtypes, PyBaseObject\_Type uses PyObject\_Del.

## inquiry PyTypeObject.tp\_is\_gc

An optional pointer to a function called by the garbage collector.

The garbage collector needs to know whether a particular object is collectible or not. Normally, it is sufficient to look at the object’s type’s tp\_flags field, and check the Py\_TPFLAGS\_HAVE\_GC flag bit. But some types have a mixture of statically and dynamically allocated instances, and the statically allocated instances are not collectible. Such types should define this function; it should return 1 for a collectible instance, and 0 for a non-collectible instance. The signature is:

```txt
int tp_is_gc(PyObject *self);
```

(The only example of this are types themselves. The metatype, PyType\_Type, defines this function to distinguish between statically and dynamically allocated types.)

## Inheritance:

This field is inherited by subtypes.

## Default:

This slot has no default. If this field is NULL, Py\_TPFLAGS\_HAVE\_GC is used as the functional equivalent.

## PyObject \*PyTypeObject.tp\_bases

```txt
Tuple of base types.
```

This field should be set to NULL and treated as read-only. Python will fill it in when the type is initialized.

For dynamically created classes, the Py\_tp\_bases slot can be used instead of the bases argument of PyType\_FromSpecWithBases(). The argument form is preferred.

**Warning:** Multiple inheritance does not work well for statically defined types. If you set tp\_bases to a tuple, Python will not raise an error, but some slots will only be inherited from the first base.

## Inheritance:

This field is not inherited.

PyObject \*PyTypeObject.**tp\_mro**

Tuple containing the expanded set of base types, starting with the type itself and ending with object, in Method Resolution Order.

This field should be set to NULL and treated as read-only. Python will fill it in when the type is initialized.

## Inheritance:

This field is not inherited; it is calculated fresh by PyType\_Ready().

```txt
PyObject *PyTypeObject.tp_cache
Unused. Internal use only.
```

**Inheritance:**

This field is not inherited.

PyObject \*PyTypeObject.**tp\_subclasses** List of weak references to subclasses. Internal use only.

## Inheritance:

This field is not inherited.

PyObject \*PyTypeObject.**tp\_weaklist** Weak reference list head, for weak references to this type object. Not inherited. Internal use only.

## Inheritance:

This field is not inherited.

```txt
destructor PyTypeObject.tp_del
    This field is deprecated. Use tp_finalize instead.
```

unsigned int PyTypeObject.**tp\_version\_tag** Used to index into the method cache. Internal use only.

## Inheritance:

This field is not inherited.

destructor PyTypeObject.**tp\_finalize** An optional pointer to an instance finalization function. Its signature is:

```c
void tp_finalize(PyObject *self);
```

If tp\_finalize is set, the interpreter calls it once when finalizing an instance. It is called either from the garbage collector (if the instance is part of an isolated reference cycle) or just before the object is deallocated. Either way, it is guaranteed to be called before attempting to break reference cycles, ensuring that it finds the object in a sane state.

tp\_finalize should not mutate the current exception status; therefore, a recommended way to write a non-trivial finalizer is:

```c
static void
local_finalize(PyObject *self)
{
    PyObject *error_type, *error_value, *error_traceback;

    /* Save the current exception, if any. */
    PyErr_Fetch(&error_type, &error_value, &error_traceback);

    /* ... */

    /* Restore the saved exception. */
    PyErr_Restore(error_type, error_value, error_traceback);
}
```

Also, note that, in a garbage collected Python, tp\_dealloc may be called from any Python thread, not just the thread which created the object (if the object becomes part of a refcount cycle, that cycle might be collected by a garbage collection on any thread). This is not a problem for Python API calls, since the thread on which tp\_dealloc is called will own the Global Interpreter Lock (GIL). However, if the object being destroyed in turn

destroys objects from some other C or C++ library, care should be taken to ensure that destroying those objects on the thread which called tp\_dealloc will not violate any assumptions of the library.

## Inheritance:

This field is inherited by subtypes.

New in version 3.4.

Changed in version 3.8: Before version 3.8 it was necessary to set the Py\_TPFLAGS\_HAVE\_FINALIZE flags bit in order for this field to be used. This is no longer required.

## See also:

“Safe object finalization” ([**PEP 442**](https://www.python.org/dev/peps/pep-0442))

## vectorcallfunc PyTypeObject.tp\_vectorcall

Vectorcall function to use for calls of this type object. In other words, it is used to implement vectorcall for type.\_\_call\_\_. If tp\_vectorcall is NULL, the default call implementation using \_\_new\_\_ and init\_\_ is used.

## Inheritance:

This field is never inherited.

New in version 3.9: (the field exists since 3.8 but it’s only used since 3.9)

## 12.3.6 Static Types

Traditionally, types defined in C code are static, that is, a static PyTypeObject structure is defined directly in code and initialized using PyType\_Ready().

This results in types that are limited relative to types defined in Python:

• Static types are limited to one base, i.e. they cannot use multiple inheritance.

• Static type objects (but not necessarily their instances) are immutable. It is not possible to add or modify the type object’s attributes from Python.

• Static type objects are shared across sub-interpreters, so they should not include any subinterpreter-specific state.

Also, since PyTypeObject is only part of the Limited API as an opaque struct, any extension modules using static types must be compiled for a specific Python minor version.

## 12.3.7 Heap Types

An alternative to static types is heap-allocated types, or heap types for short, which correspond closely to classes created by Python’s class statement. Heap types have the Py\_TPFLAGS\_HEAPTYPE flag set.

This is done by filling a PyType\_Spec structure and calling PyType\_FromSpec(), PyType\_FromSpecWithBases(), or PyType\_FromModuleAndSpec().

## 12.4 Number Object Structures

## type PyNumberMethods

This structure holds pointers to the functions which an object uses to implement the number protocol. Each function is used by the function of similar name documented in the Number Protocol section.

Here is the structure definition:

```cpp
typedef struct {
    binaryfunc nb_add;
    binaryfunc nb_subtract;
    binaryfunc nb_multiply;
    binaryfunc nb_remainder;
    binaryfunc nb_divmod;
    ternaryfunc nb_power;
    unaryfunc nb_negative;
    unaryfunc nb_positive;
    unaryfunc nb_absolute;
    inquiry nb_bool;
    unaryfunc nb_invert;
    binaryfunc nb_lshift;
    binaryfunc nb_rshift;
    binaryfunc nb_and;
    binaryfunc nb_xor;
    binaryfunc nb_or;
    unaryfunc nb_int;
    void *nb_reserved;
    unaryfunc nb_float;

    binaryfunc nb_inplace_add;
    binaryfunc nb_inplace_subtract;
    binaryfunc nb_inplace_multiply;
    binaryfunc nb_inplace_remainder;
    ternaryfunc nb_inplace_power;
    binaryfunc nb_inplace_lshift;
    binaryfunc nb_inplace_rshift;
    binaryfunc nb_inplace_and;
    binaryfunc nb_inplace_xor;
    binaryfunc nb_inplace_or;

    binaryfunc nb_floor_divide;
    binaryfunc nb_true_divide;
    binaryfunc nb_inplace_floor_divide;
    binaryfunc nb_inplace_true_divide;

    unaryfunc nb_index;

    binaryfunc nb_matrix_multiply;
    binaryfunc nb_inplace_matrix_multiply;
} PyNumberMethods;
```

**Note:** Binary and ternary functions must check the type of all their operands, and implement the necessary conversions (at least one of the operands is an instance of the defined type). If the operation is not defined for the given operands, binary and ternary functions must return Py\_NotImplemented, if another error occurred they must return NULL and set an exception.

**Note:** The nb\_reserved field should always be NULL. It was previously called nb\_long, and was renamed in Python 3.0.1.

binaryfunc PyNumberMethods.**nb\_add**

binaryfunc PyNumberMethods.**nb\_subtract**

binaryfunc PyNumberMethods.**nb\_multiply**

binaryfunc PyNumberMethods.**nb\_remainder**

binaryfunc PyNumberMethods.**nb\_divmod**

ternaryfunc PyNumberMethods.**nb\_power**

unaryfunc PyNumberMethods.**nb\_negative**

unaryfunc PyNumberMethods.**nb\_positive**

unaryfunc PyNumberMethods.**nb\_absolute**

inquiry PyNumberMethods.**nb\_bool**

unaryfunc PyNumberMethods.**nb\_invert**

binaryfunc PyNumberMethods.**nb\_lshift**

binaryfunc PyNumberMethods.**nb\_rshift**

binaryfunc PyNumberMethods.**nb\_and**

binaryfunc PyNumberMethods.**nb\_xor**

binaryfunc PyNumberMethods.**nb\_or**

unaryfunc PyNumberMethods.**nb\_int**

void \*PyNumberMethods.**nb\_reserved**

unaryfunc PyNumberMethods.**nb\_float**

binaryfunc PyNumberMethods.**nb\_inplace\_add**

binaryfunc PyNumberMethods.**nb\_inplace\_subtract**

binaryfunc PyNumberMethods.**nb\_inplace\_multiply**

binaryfunc PyNumberMethods.**nb\_inplace\_remainder**

ternaryfunc PyNumberMethods.**nb\_inplace\_power**

binaryfunc PyNumberMethods.**nb\_inplace\_lshift**

binaryfunc PyNumberMethods.**nb\_inplace\_rshift**

binaryfunc PyNumberMethods.**nb\_inplace\_and**

binaryfunc PyNumberMethods.**nb\_inplace\_xor**

binaryfunc PyNumberMethods.**nb\_inplace\_or**

binaryfunc PyNumberMethods.**nb\_floor\_divide**

binaryfunc PyNumberMethods.**nb\_true\_divide**

binaryfunc PyNumberMethods.**nb\_inplace\_floor\_divide**

binaryfunc PyNumberMethods.**nb\_inplace\_true\_divide**

unaryfunc PyNumberMethods.**nb\_index**

binaryfunc PyNumberMethods.**nb\_matrix\_multiply**

binaryfunc PyNumberMethods.**nb\_inplace\_matrix\_multiply**

## 12.5 Mapping Object Structures

## type PyMappingMethods

This structure holds pointers to the functions which an object uses to implement the mapping protocol. It has three members:

## lenfunc PyMappingMethods.mp\_length

This function is used by PyMapping\_Size() and PyObject\_Size(), and has the same signature. This slot may be set to NULL if the object has no defined length.

## binaryfunc PyMappingMethods.mp\_subscript

This function is used by PyObject\_GetItem() and PySequence\_GetSlice(), and has the same signature as PyObject\_GetItem(). This slot must be filled for the PyMapping\_Check() function to return 1, it can be NULL otherwise.

## objobjargproc PyMappingMethods.mp\_ass\_subscript

This function is used by PyObject\_SetItem(), PyObject\_DelItem(), PyObject\_SetSlice() and PyObject\_DelSlice(). It has the same signature as PyObject\_SetItem(), but v can also be set to NULL to delete an item. If this slot is NULL, the object does not support item assignment and deletion.

## 12.6 Sequence Object Structures

## type PySequenceMethods

This structure holds pointers to the functions which an object uses to implement the sequence protocol.

## lenfunc PySequenceMethods.sq\_length

This function is used by PySequence\_Size() and PyObject\_Size(), and has the same signature. It is also used for handling negative indices via the sq\_item and the sq\_ass\_item slots.

## binaryfunc PySequenceMethods.sq\_concat

This function is used by PySequence\_Concat() and has the same signature. It is also used by the + operator, after trying the numeric addition via the nb\_add slot.

## ssizeargfunc PySequenceMethods.sq\_repeat

This function is used by PySequence\_Repeat() and has the same signature. It is also used by the \* operator, after trying numeric multiplication via the nb\_multiply slot.

## ssizeargfunc PySequenceMethods.sq\_item

This function is used by PySequence\_GetItem() and has the same signature. It is also used by PyObject\_GetItem(), after trying the subscription via the mp\_subscript slot. This slot must be filled for the PySequence\_Check() function to return 1, it can be NULL otherwise.

Negative indexes are handled as follows: if the sq\_length slot is filled, it is called and the sequence length is used to compute a positive index which is passed to sq\_item. If sq\_length is NULL, the index is passed as is to the function.

## ssizeobjargproc PySequenceMethods.sq\_ass\_item

This function is used by PySequence\_SetItem() and has the same signature. It is also used by PyObject\_SetItem() and PyObject\_DelItem(), after trying the item assignment and deletion via the mp\_ass\_subscript slot. This slot may be left to NULL if the object does not support item assignment and deletion.

## objobjproc PySequenceMethods.sq\_contains

This function may be used by PySequence\_Contains() and has the same signature. This slot may be left to NULL, in this case PySequence\_Contains() simply traverses the sequence until it finds a match.

## binaryfunc PySequenceMethods.sq\_inplace\_concat

This function is used by PySequence\_InPlaceConcat() and has the same signature. It should modify its first operand, and return it. This slot may be left to NULL, in this case

PySequence\_InPlaceConcat() will fall back to PySequence\_Concat(). It is also used by the augmented assignment +=, after trying numeric in-place addition via the nb\_inplace\_add slot.

ssizeargfunc PySequenceMethods.**sq\_inplace\_repeat**

This function is used by PySequence\_InPlaceRepeat() and has the same signature. It should modify its first operand, and return it. This slot may be left to NULL, in this case PySequence\_InPlaceRepeat() will fall back to PySequence\_Repeat(). It is also used by the augmented assignment \*=, after trying numeric in-place multiplication via the nb\_inplace\_multiply slot.

## 12.7 Buffer Object Structures

## type PyBufferProcs

This structure holds pointers to the functions required by the Buffer protocol. The protocol defines how an exporter object can expose its internal data to consumer objects.

getbufferproc PyBufferProcs.**bf\_getbuffer** The signature of this function is:

```txt
int (PyObject *exporter, Py_buffer *view, int flags);
```

Handle a request to exporter to fill in view as specified by flags. Except for point (3), an implementation of this function MUST take these steps:

(1) Check if the request can be met. If not, raise PyExc\_BufferError, set view->obj to NULL and return -1.

(2) Fill in the requested fields.

(3) Increment an internal counter for the number of exports.

(4) Set view->obj to exporter and increment view->obj.

(5) Return 0.

If exporter is part of a chain or tree of buffer providers, two main schemes can be used:

• Re-export: Each member of the tree acts as the exporting object and sets view->obj to a new reference to itself.

• Redirect: The buffer request is redirected to the root object of the tree. Here, view->obj will be a new reference to the root object.

The individual fields of view are described in section Buffer structure, the rules how an exporter must react to specific requests are in section Buffer request types.

All memory pointed to in the Py\_buffer structure belongs to the exporter and must remain valid until there are no consumers left. format, shape, strides, suboffsets and internal are read-only for the consumer.

PyBuffer\_FillInfo() provides an easy way of exposing a simple bytes buffer while dealing correctly with all request types.

PyObject\_GetBuffer() is the interface for the consumer that wraps this function.

releasebufferproc PyBufferProcs.**bf\_releasebuffer**

The signature of this function is:

```txt
void (PyObject *exporter, Py_buffer *view);
```

Handle a request to release the resources of the buffer. If no resources need to be released, PyBufferProcs.bf\_releasebuffer may be NULL. Otherwise, a standard implementation of this function will take these optional steps:

(1) Decrement an internal counter for the number of exports.

(2) If the counter is 0, free all memory associated with view.

The exporter MUST use the internal field to keep track of buffer-specific resources. This field is guaranteed to remain constant, while a consumer MAY pass a copy of the original buffer as the view argument.

This function MUST NOT decrement view->obj, since that is done automatically in PyBuffer\_Release() (this scheme is useful for breaking reference cycles).

PyBuffer\_Release() is the interface for the consumer that wraps this function.

## 12.8 Async Object Structures

New in version 3.5.

## type PyAsyncMethods

This structure holds pointers to the functions required to implement awaitable and asynchronous iterator objects.

Here is the structure definition:

```txt
typedef struct {
    unaryfunc am_await;
    unaryfunc am_aiter;
    unaryfunc am_anext;
    sendfunc am_send;
} PyAsyncMethods;
```

unaryfunc PyAsyncMethods.**am\_await**

The signature of this function is:

```txt
PyObject *am_await(PyObject *self);
```

The returned object must be an iterator, i.e. PyIter\_Check() must return 1 for it.

This slot may be set to NULL if an object is not an awaitable.

unaryfunc PyAsyncMethods.**am\_aiter**

The signature of this function is:

```c
PyObject *am_aiter(PyObject *self);
```

Must return an asynchronous iterator object. See \_\_anext\_\_() for details.

This slot may be set to NULL if an object does not implement asynchronous iteration protocol.

unaryfunc PyAsyncMethods.**am\_anext**

The signature of this function is:

```c
PyObject *am_anext(PyObject *self);
```

Must return an awaitable object. See \_\_anext\_\_() for details. This slot may be set to NULL.

sendfunc PyAsyncMethods.**am\_send**

The signature of this function is:

```c
PySendResult am_send(PyObject *self, PyObject *arg, PyObject **result);
```

See PyIter\_Send() for details. This slot may be set to NULL.

New in version 3.10.

## 12.9 Slot Type typedefs

**typedef** PyObject \*(\***allocfunc**)(PyTypeObject \*cls, Py\_ssize\_t nitems)

Part of the Stable ABI. The purpose of this function is to separate memory allocation from memory initialization. It should return a pointer to a block of memory of adequate length for the instance, suitably aligned, and initialized to zeros, but with ob\_refcnt set to 1 and ob\_type set to the type argument. If the type’s tp\_itemsize is non-zero, the object’s ob\_size field should be initialized to nitems and the length of the allocated memory block should be tp\_basicsize + nitems\*tp\_itemsize, rounded up to a multiple of sizeof(void\*); otherwise, nitems is not used and the length of the block should be tp\_basicsize.

This function should not do any other instance initialization, not even to allocate additional memory; that should be done by tp\_new.

**typedef** void (\***destructor**)(PyObject\*) Part of the Stable ABI.

**typedef** void (\***freefunc**)(void\*) See tp\_free.

**typedef** PyObject \*(\***newfunc**)(PyObject\*, PyObject\*, PyObject\*) Part of the Stable ABI. See tp\_new.

**typedef** int (\***initproc**)(PyObject\*, PyObject\*, PyObject\*) Part of the Stable ABI. See tp\_init.

**typedef** PyObject \*(\***reprfunc**)(PyObject\*) Part of the Stable ABI. See tp\_repr.

**typedef** PyObject \*(\***getattrfunc**)(PyObject \*self, char \*attr) Part of the Stable ABI. Return the value of the named attribute for the object.

**typedef** int (\***setattrfunc**)(PyObject \*self, char \*attr, PyObject \*value) Part of the Stable ABI. Set the value of the named attribute for the object. The value argument is set to NULL to delete the attribute.

**typedef** PyObject \*(\***getattrofunc**)(PyObject \*self, PyObject \*attr) Part of the Stable ABI. Return the value of the named attribute for the object. See tp\_getattro.

**typedef** int (\***setattrofunc**)(PyObject \*self, PyObject \*attr, PyObject \*value) Part of the Stable ABI. Set the value of the named attribute for the object. The value argument is set to NULL to delete the attribute. See tp\_setattro.

**typedef** PyObject \*(\***descrgetfunc**)(PyObject\*, PyObject\*, PyObject\*) Part of the Stable ABI. See tp\_descr\_get.

**typedef** int (\***descrsetfunc**)(PyObject\*, PyObject\*, PyObject\*) Part of the Stable ABI. See tp\_descr\_set.

**typedef** Py\_hash\_t (\***hashfunc**)(PyObject\*) Part of the Stable ABI. See tp\_hash.

**typedef** PyObject \*(\***richcmpfunc**)(PyObject\*, PyObject\*, int) Part of the Stable ABI. See tp\_richcompare.

**typedef** PyObject \*(\***getiterfunc**)(PyObject\*) Part of the Stable ABI. See tp\_iter.

**typedef** PyObject \*(\***iternextfunc**)(PyObject\*) Part of the Stable ABI. See tp\_iternext.

**typedef** Py\_ssize\_t (\***lenfunc**)(PyObject\*) Part of the Stable ABI.

```txt
typedef int (*getbufferproc)(PyObject*, Py_buffer*, int)
typedef void (*releasebufferproc)(PyObject*, Py_buffer*)
typedef PyObject *(*unaryfunc)(PyObject*)
    Part of the Stable ABI.
typedef PyObject *(*binaryfunc)(PyObject*, PyObject*)
    Part of the Stable ABI.
typedef PySendResult (*sendfunc)(PyObject*, PyObject*, PyObject**
    See am_send.
typedef PyObject *(*ternaryfunc)(PyObject*, PyObject*, PyObject*)
    Part of the Stable ABI.
typedef PyObject *(*ssizeargfunc)(PyObject*, Py_ssize_t)
    Part of the Stable ABI.
typedef int (*ssizeobjargproc)(PyObject*, Py_ssize_t, PyObject*)
    Part of the Stable ABI.
typedef int (*objobjproc)(PyObject*, PyObject*)
    Part of the Stable ABI.
typedef int (*objobjargproc)(PyObject*, PyObject*, PyObject*)
    Part of the Stable ABI.
```

## 12.10 Examples

The following are simple examples of Python type definitions. They include common usage you may encounter. Some demonstrate tricky corner cases. For more examples, practical info, and a tutorial, see defining-new-types and new-types-topics.

A basic static type:

```txt
typedef struct {
    PyObject_HEAD
    const char *data;
} MyObject;

static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
    .tp_basicsize = sizeof(MyObject),
    .tp_doc = PyDoc_STR("My objects"),
    .tp_new = myobj_new,
    .tp_dealloc = (destructor)myobj_dealloc,
    .tp_repr = (reprfunc)myobj_repr,
};
```

You may also find older code (especially in the CPython code base) with a more verbose initializer:

```c
static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "mymod.MyObject",          /* tp_name */
    sizeof(MyObject),            /* tp_basicsize */
    0,                       /* tp_itemsize */
    (destructor)myobj_dealloc,      /* tp_dealloc */
    0,                       /* tp_vectorcall_offset */
    0,                       /* tp_getattr */
    0,                       /* tp_setattr */
    0,                       /* tp_as_async */
```

(continues on next page)

(continued from previous page)

```c
(reprfunc)myobj_repr,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
PyDoc_STR("My objects"),
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0, myobj_new,
};
/* tp_repr */
/* tp_as_number */
/* tp_as_sequence */
/* tp_as_mapping */
/* tp_hash */
/* tp_call */
/* tp_str */
/* tp_getattro */
/* tp_setattro */
/* tp_as_buffer */
/* tp_flags */
/* tp_doc */
/* tp_traverse */
/* tp_clear */
/* tp_richcompare */
/* tp_weaklistoffset */
/* tp_iter */
/* tp_iternext */
/* tp_methods */
/* tp_members */
/* tp_getset */
/* tp_base */
/* tp_dict */
/* tp_descr_get */
/* tp_descr_set */
/* tp_dictoffset */
/* tp_init */
/* tp_alloc */
/* tp_new */
};
```

A type that supports weakrefs, instance dicts, and hashing:

```txt
typedef struct {
    PyObject_HEAD
    const char *data;
    PyObject *inst_dict;
    PyObject *weakreflist;
} MyObject;

static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
    .tp_basicsize = sizeof(MyObject),
    .tp_doc = PyDoc_STR("My objects"),
    .tp_weaklistoffset = offsetof(MyObject, weakreflist),
    .tp_dictoffset = offsetof(MyObject, inst_dict),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
    .tp_new = myobj_new,
    .tp_traverse = (traverseproc)myobj_traverse,
    .tp_clear = (inquiry)myobj_clear,
    .tp_alloc = PyType_GenericNew,
    .tp_dealloc = (destructor)myobj_dealloc,
    .tp_repr = (reprfunc)myobj_repr,
    .tp_hash = (hashfunc)myobj_hash,
    .tp_richcompare = PyBaseObject_Type.tp_richcompare,
};
```

A str subclass that cannot be subclassed and cannot be called to create instances (e.g. uses a separate factory func) using Py\_TPFLAGS\_DISALLOW\_INSTANTIATION flag:

```txt
typedef struct {
    PyUnicodeObject raw;
    char *extra;
} MyStr;

static PyTypeObject MyStr_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyStr",
    .tp_basicsize = sizeof(MyStr),
    .tp_base = NULL,  // set to &PyUnicode_Type in module init
    .tp_doc = PyDoc_STR("my custom str"),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .tp_repr = (reprfunc)myobj_repr,
};
```

The simplest static type with fixed-length instances:

```c
typedef struct {
    PyObject_HEAD
} MyObject;

static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
};
```

The simplest static type with variable-length instances:

```txt
typedef struct {
    PyObject_VAR_HEAD
    const char *data[1];
} MyObject;

static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
    .tp_basicsize = sizeof(MyObject) - sizeof(char *),
    .tp_itemsize = sizeof(char *),
};
```

## 12.11 Supporting Cyclic Garbage Collection

Python’s support for detecting and collecting garbage which involves circular references requires support from object types which are “containers” for other objects which may also be containers. Types which do not store references to other objects, or which only store references to atomic types (such as numbers or strings), do not need to provide any explicit support for garbage collection.

To create a container type, the tp\_flags field of the type object must include the Py\_TPFLAGS\_HAVE\_GC and provide an implementation of the tp\_traverse handler. If instances of the type are mutable, a tp\_cl ear implementation must also be provided.

## Py\_TPFLAGS\_HAVE\_GC

Objects with a type with this flag set must conform with the rules documented here. For convenience these objects will be referred to as container objects.

Constructors for container types must conform to two rules:

1. The memory for the object must be allocated using PyObject\_GC\_New() PyObject\_GC\_NewVar().

2. Once all the fields which may contain references to other containers are initialized, it must call PyObject\_GC\_Track().

Similarly, the deallocator for the object must conform to a similar pair of rules:

1. Before fields which refer to other containers are invalidated, PyObject\_GC\_UnTrack() must be called.

2. The object’s memory must be deallocated using PyObject\_GC\_Del().

```python
Warning: If a type adds the Py_TPFLAGS_HAVE_GC, then it must implement at least a tp_traverse handler or explicitly use one from its subclass or subclasses.
When calling PyType_Ready() or some of the APIs that indirectly call it like PyType_FromSpecWithBases() or PyType_FromSpec() the interpreter will automatically populate the tp_flags, tp_traverse and tp_clear fields if the type inherits from a class that implements the garbage collector protocol and the child class does not include the Py_TPFLAGS_HAVE_GC flag.

TYPE *PyObject_GC_New (TYPE, PyTypeObject *type)
Analogous to PyObject_New() but for container objects with the Py_TPFLAGS_HAVE_GC flag set.

TYPE *PyObject_GC_NewVar (TYPE, PyTypeObject *type, Py_ssize_t size)
Analogous to PyObject_NewVar() but for container objects with the Py_TPFLAGS_HAVE_GC flag set.

TYPE *PyObject_GC_Resize (TYPE, PyVarObject *op, Py_ssize_t newsize)
Resize an object allocated by PyObject_NewVar(). Returns the resized object or NULL on failure. op must not be tracked by the collector yet.

void PyObject_GC_Track (PyObject *op)
Part of the Stable ABI. Adds the object op to the set of container objects tracked by the collector. The collector can run at unexpected times so objects must be valid while being tracked. This should be called once all the fields followed by the tp_traverse handler become valid, usually near the end of the constructor.

int PyObject_IS_GC (PyObject *obj)
Returns non-zero if the object implements the garbage collector protocol, otherwise returns 0.
The object cannot be tracked by the garbage collector if this function returns 0.

int PyObject_GC_IsTracked (PyObject *op)
Part of the Stable ABI since version 3.9. Returns 1 if the object type of op implements the GC protocol and op is being currently tracked by the garbage collector and 0 otherwise.
This is analogous to the Python function gc.is_tracked().
New in version 3.9.

int PyObject_GC_IsFinalized (PyObject *op)
Part of the Stable ABI since version 3.9. Returns 1 if the object type of op implements the GC protocol and op has been already finalized by the garbage collector and 0 otherwise.
This is analogous to the Python function gc.is_finalized().
New in version 3.9.

void PyObject_GC_Del (void *op)
Part of the Stable ABI. Releases memory allocated to an object using PyObject_GC_New() or PyObject_GC_NewVar().
void PyObject_GC_UnTrack (void *op)
Part of the Stable ABI. Remove the object op from the set of container objects tracked by the collector. Note that PyObject_GC_Track() can be called again on this object to add it back to the set of tracked objects. The deallocator (tp_dealloc handler) should call this for the object before any of the fields used by the tp_traverse handler become invalid.

Changed in version 3.8: The _PyObject_GC_TRACK() and _PyObject_GC_UNTRACK() macros have been removed from the public C API.
```

The tp\_traverse handler accepts a function parameter of this type:

## typedef int (\*visitproc)(PyObject \*object, void \*arg)

Part of the Stable ABI. Type of the visitor function passed to the tp\_traverse handler. The function should be called with an object to traverse as object and the third parameter to the tp\_traverse handler as arg. The Python core uses several visitor functions to implement cyclic garbage detection; it’s not expected that users will need to write their own visitor functions.

The tp\_traverse handler must have the following type:

## typedef int (\*traverseproc)(PyObject \*self, visitproc visit, void \*arg)

Part of the Stable ABI. Traversal function for a container object. Implementations must call the visit function for each object directly contained by self, with the parameters to visit being the contained object and the arg value passed to the handler. The visit function must not be called with a NULL object argument. If visit returns a non-zero value that value should be returned immediately.

To simplify writing tp\_traverse handlers, a Py\_VISIT() macro is provided. In order to use this macro, the tp\_traverse implementation must name its arguments exactly visit and arg:

## void Py\_VISIT(PyObject \*o)

If o is not NULL, call the visit callback, with arguments o and arg. If visit returns a non-zero value, then return it. Using this macro, tp\_traverse handlers look like:

```c
static int
my_traverse(Noddy *self, visitproc visit, void *arg)
{
    Py_VISIT(self->foo);
    Py_VISIT(self->bar);
    return 0;
}
```

The tp\_clear handler must be of the inquiry type, or NULL if the object is immutable.

## typedef int (\*inquiry)(PyObject \*self)

Part of the Stable ABI. Drop references that may have created reference cycles. Immutable objects do not have to define this method since they can never directly create reference cycles. Note that the object must still be valid after calling this method (don’t just call Py\_DECREF() on a reference). The collector will call this method if it detects that this object is involved in a reference cycle.

## 12.11.1 Controlling the Garbage Collector State

The C-API provides the following functions for controlling garbage collection runs.

## Py\_ssize\_t PyGC\_Collect(void)

Part of the Stable ABI. Perform a full garbage collection, if the garbage collector is enabled. (Note that gc. collect() runs it unconditionally.)

Returns the number of collected + unreachable objects which cannot be collected. If the garbage collector is disabled or already collecting, returns 0 immediately. Errors during garbage collection are passed to sys. unraisablehook. This function does not raise exceptions.

## int PyGC\_Enable(void)

Part of the Stable ABI since version 3.10. Enable the garbage collector: similar to gc.enable(). Returns the previous state, 0 for disabled and 1 for enabled.

New in version 3.10.

## int PyGC\_Disable(void)

Part of the Stable ABI since version 3.10. Disable the garbage collector: similar to gc.disable(). Returns the previous state, 0 for disabled and 1 for enabled.

New in version 3.10.

## int PyGC\_IsEnabled(void)

Part of the Stable ABI since version 3.10. Query the state of the garbage collector: similar to gc. isenabled(). Returns the current state, 0 for disabled and 1 for enabled.

New in version 3.10.

## API AND ABI VERSIONING

CPython exposes its version number in the following macros. Note that these correspond to the version code is **built** with, not necessarily the version used at **run time**.

See C API Stability for a discussion of API and ABI stability across versions.

**PY\_MAJOR\_VERSION** The 3 in 3.4.1a2.

**PY\_MINOR\_VERSION** The 4 in 3.4.1a2.

**PY\_MICRO\_VERSION** The 1 in 3.4.1a2.

**PY\_RELEASE\_LEVEL** The a in 3.4.1a2. This can be 0xA for alpha, 0xB for beta, 0xC for release candidate or 0xF for final.

**PY\_RELEASE\_SERIAL** The 2 in 3.4.1a2. Zero for final releases.

**PY\_VERSION\_HEX** The Python version number encoded in a single integer.

The underlying version information can be found by treating it as a 32 bit number in the following manner:

<table><tbody><tr><td>Bytes</td><td>Bits (big endian order)</td><td>Meaning</td><td>Value for 3.4.1a2</td></tr><tr><td>1</td><td>1-8</td><td>PY_MAJOR_VERSION</td><td>0x03</td></tr><tr><td>2</td><td>9-16</td><td>PY_MINOR_VERSION</td><td>0x04</td></tr><tr><td>3</td><td>17-24</td><td>PY_MICRO_VERSION</td><td>0x01</td></tr><tr><td rowspan="2">4</td><td>25-28</td><td>PY_RELEASE_LEVEL</td><td>0xA</td></tr><tr><td>29-32</td><td>PY_RELEASE_SERIAL</td><td>0x2</td></tr></tbody></table>

Thus 3.4.1a2 is hexversion 0x030401a2 and 3.10.0 is hexversion 0x030a00f0. All the given macros are defined in [Include/patchlevel.h](https://github.com/python/cpython/tree/3.10/Include/patchlevel.h).

# GLOSSARY

**>>>** The default Python prompt of the interactive shell. Often seen for code examples which can be executed interactively in the interpreter.

**...** Can refer to:

• The default Python prompt of the interactive shell when entering the code for an indented code block, when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator.

• The Ellipsis built-in constant.

**2to3** A tool that tries to convert Python 2.x code to Python 3.x code by handling most of the incompatibilities which can be detected by parsing the source and traversing the parse tree.

2to3 is available in the standard library as lib2to3; a standalone entry point is provided as Tools/ scripts/2to3. See 2to3-reference.

**abstract base class** Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like hasattr() would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and issubclass(); see the abc module documentation. Python comes with many built-in ABCs for data structures (in the collections.abc module), numbers (in the numbers module), streams (in the io module), import finders and loaders (in the importlib.abc module). You can create your own ABCs with the abc module.

**annotation** A label associated with a variable, a class attribute or a function parameter or return value, used by convention as a type hint.

Annotations of local variables cannot be accessed at runtime, but annotations of global variables, class attributes, and functions are stored in the \_\_annotations\_\_ special attribute of modules, classes, and functions, respectively.

See variable annotation, function annotation, [**PEP 484**](https://www.python.org/dev/peps/pep-0484) and [**PEP 526**](https://www.python.org/dev/peps/pep-0526), which describe this functionality. Also see annotations-howto for best practices on working with annotations.

**argument** A value passed to a function (or method) when calling the function. There are two kinds of argument:

• keyword argument: an argument preceded by an identifier (e.g. name=) in a function call or passed as a value in a dictionary preceded by \*\*. For example, 3 and 5 are both keyword arguments in the following calls to complex():

```python
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
```

• positional argument: an argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list and/or be passed as elements of an iterable preceded by \*. For example, 3 and 5 are both positional arguments in the following calls:

```txt
complex(3, 5)
complex(*(3, 5))
```

Arguments are assigned to the named local variables in a function body. See the calls section for the rules governing this assignment. Syntactically, any expression can be used to represent an argument; the evaluated value is assigned to the local variable.

See also the parameter glossary entry, the FAQ question on the difference between arguments and parameters, and [**PEP 362**](https://www.python.org/dev/peps/pep-0362).

**asynchronous context manager** An object which controls the environment seen in an async with statement by defining \_\_aenter\_\_() and \_\_aexit\_\_() methods. Introduced by [**PEP 492**](https://www.python.org/dev/peps/pep-0492).

**asynchronous generator** A function which returns an asynchronous generator iterator. It looks like a coroutine function defined with async def except that it contains yield expressions for producing a series of values usable in an async for loop.

Usually refers to an asynchronous generator function, but may refer to an asynchronous generator iterator in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

An asynchronous generator function may contain await expressions as well as async for, and async with statements.

**asynchronous generator iterator** An object created by a asynchronous generator function.

This is an asynchronous iterator which when called using the \_\_anext\_\_() method returns an awaitable object which will execute the body of the asynchronous generator function until the next yield expression.

Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the asynchronous generator iterator effectively resumes with another awaitable returned by \_\_anext\_\_(), it picks up where it left off. See [**PEP 492**](https://www.python.org/dev/peps/pep-0492) and [**PEP 525**](https://www.python.org/dev/peps/pep-0525).

**asynchronous iterable** An object, that can be used in an async for statement. Must return an asynchronous iterator from its \_\_aiter\_\_() method. Introduced by [**PEP 492**](https://www.python.org/dev/peps/pep-0492).

**asynchronous iterator** An object that implements the \_\_aiter\_\_() and \_\_anext\_\_() methods. \_anext\_\_ must return an awaitable object. async for resolves the awaitables returned by an asynchronous iterator’s \_\_anext\_\_() method until it raises a StopAsyncIteration exception. Introduced by [**PEP 492**](https://www.python.org/dev/peps/pep-0492).

**attribute** A value associated with an object which is usually referenced by name using dotted expressions. For example, if an object o has an attribute a it would be referenced as o.a.

It is possible to give an object an attribute whose name is not an identifier as defined by identifiers, for example using setattr(), if the object allows it. Such an attribute will not be accessible using a dotted expression, and would instead need to be retrieved with getattr().

**awaitable** An object that can be used in an await expression. Can be a coroutine or an object with an \_await\_\_() method. See also [**PEP 492**](https://www.python.org/dev/peps/pep-0492).

**BDFL** Benevolent Dictator For Life, a.k.a. [Guido van Rossum](https://gvanrossum.github.io/), Python’s creator.

**binary file** A file object able to read and write bytes-like objects. Examples of binary files are files opened in binary mode ('rb', 'wb' or 'rb+'), sys.stdin.buffer, sys.stdout.buffer, and instances of io. BytesIO and gzip.GzipFile.

See also text file for a file object able to read and write str objects.

**borrowed reference** In Python’s C API, a borrowed reference is a reference to an object, where the code using the object does not own the reference. It becomes a dangling pointer if the object is destroyed. For example, a garbage collection can remove the last strong reference to the object and so destroy it.

Calling Py\_INCREF() on the borrowed reference is recommended to convert it to a strong reference inplace, except when the object cannot be destroyed before the last usage of the borrowed reference. The Py\_NewRef() function can be used to create a new strong reference.

**bytes-like object** An object that supports the Buffer Protocol and can export a C-contiguous buffer. This includes all bytes, bytearray, and array.array objects, as well as many common memoryview objects. Bytes-like objects can be used for various operations that work with binary data; these include compression, saving to a binary file, and sending over a socket.

Some operations need the binary data to be mutable. The documentation often refers to these as “readwrite bytes-like objects”. Example mutable buffer objects include bytearray and a memoryview of a bytearray. Other operations require the binary data to be stored in immutable objects (“read-only byteslike objects”); examples of these include bytes and a memoryview of a bytes object.

**bytecode** Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter. The bytecode is also cached in .pyc files so that executing the same file is faster the second time (recompilation from source to bytecode can be avoided). This “intermediate language” is said to run on a virtual machine that executes the machine code corresponding to each bytecode. Do note that bytecodes are not expected to work between different Python virtual machines, nor to be stable between Python releases.

A list of bytecode instructions can be found in the documentation for the dis module.

**callable** A callable is an object that can be called, possibly with a set of arguments (see argument), with the following syntax:

```txt
callable(argument1, argument2, ...)
```

A function, and by extension a method, is a callable. An instance of a class that implements the \_\_call\_\_() method is also a callable.

**callback** A subroutine function which is passed as an argument to be executed at some point in the future.

**class** A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

**class variable** A variable defined in a class and intended to be modified only at class level (i.e., not in an instance of the class).

**coercion** The implicit conversion of an instance of one type to another during an operation which involves two arguments of the same type. For example, int(3.15) converts the floating point number to the integer 3, but in 3+4.5, each argument is of a different type (one int, one float), and both must be converted to the same type before they can be added or it will raise a TypeError. Without coercion, all arguments of even compatible types would have to be normalized to the same value by the programmer, e.g., float(3)+4.5 rather than just 3+4.5.

**complex number** An extension of the familiar real number system in which all numbers are expressed as a sum of a real part and an imaginary part. Imaginary numbers are real multiples of the imaginary unit (the square root of -1), often written i in mathematics or j in engineering. Python has built-in support for complex numbers, which are written with this latter notation; the imaginary part is written with a j suffix, e.g., 3+1j. To get access to complex equivalents of the math module, use cmath. Use of complex numbers is a fairly advanced mathematical feature. If you’re not aware of a need for them, it’s almost certain you can safely ignore them.

**context manager** An object which controls the environment seen in a with statement by defining \_\_enter\_\_() and \_\_exit\_\_() methods. See [**PEP 343**](https://www.python.org/dev/peps/pep-0343).

**context variable** A variable which can have different values depending on its context. This is similar to Thread-Local Storage in which each execution thread may have a different value for a variable. However, with context variables, there may be several contexts in one execution thread and the main usage for context variables is to keep track of variables in concurrent asynchronous tasks. See contextvars.

**contiguous** A buffer is considered contiguous exactly if it is either C-contiguous or Fortran contiguous. Zerodimensional buffers are C and Fortran contiguous. In one-dimensional arrays, the items must be laid out in memory next to each other, in order of increasing indexes starting from zero. In multidimensional Ccontiguous arrays, the last index varies the fastest when visiting items in order of memory address. However, in Fortran contiguous arrays, the first index varies the fastest.

**coroutine** Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points. They can be implemented with the async def statement. See also [**PEP 492**](https://www.python.org/dev/peps/pep-0492).

**coroutine function** A function which returns a coroutine object. A coroutine function may be defined with the async def statement, and may contain await, async for, and async with keywords. These were introduced by [**PEP 492**](https://www.python.org/dev/peps/pep-0492).

**CPython** The canonical implementation of the Python programming language, as distributed on [python.org](https://www.python.org). The term “CPython” is used when necessary to distinguish this implementation from others such as Jython or IronPython.

**decorator** A function returning another function, usually applied as a function transformation using the @wrapper syntax. Common examples for decorators are classmethod() and staticmethod().

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:

```python
def f(arg):
f = staticmethod(f)

@staticmethod
def f(arg):
```

The same concept exists for classes, but is less commonly used there. See the documentation for function definitions and class definitions for more about decorators.

**descriptor** Any object which defines the methods \_\_get\_\_(), \_\_set\_\_(), or \_\_delete\_\_(). When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using a.b to get, set or delete an attribute looks up the object named b in the class dictionary for a, but if b is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python because they are the basis for many features including functions, methods, properties, class methods, static methods, and reference to super classes.

For more information about descriptors’ methods, see descriptors or the Descriptor How To Guide.

**dictionary** An associative array, where arbitrary keys are mapped to values. The keys can be any object with \_\_hash\_\_() and \_\_eq\_\_() methods. Called a hash in Perl.

**dictionary comprehension** A compact way to process all or part of the elements in an iterable and return a dictionary with the results. results = {n: n \*\* 2 for n in range(10)} generates a dictionary containing key n mapped to value n \*\* 2. See comprehensions.

**dictionary view** The objects returned from dict.keys(), dict.values(), and dict.items() are called dictionary views. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes. To force the dictionary view to become a full list use list(dictview). See dict-views.

**docstring** A string literal which appears as the first expression in a class, function or module. While ignored when the suite is executed, it is recognized by the compiler and put into the \_\_doc\_\_ attribute of the enclosing class, function or module. Since it is available via introspection, it is the canonical place for documentation of the object.

**duck-typing** A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitution. Duck-typing avoids tests using type() or isinstance(). (Note, however, that duck-typing can be complemented with abstract base classes.) Instead, it typically employs hasattr() tests or EAFP programming.

**EAFP** Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.

**expression** A piece of syntax which can be evaluated to some value. In other words, an expression is an accumulation of expression elements like literals, names, attribute access, operators or function calls which all return a value. In contrast to many other languages, not all language constructs are expressions. There are also statements which cannot be used as expressions, such as while. Assignments are also statements, not expressions.

**extension module** A module written in C or C++, using Python’s C API to interact with the core and with user code.

**f-string** String literals prefixed with 'f' or 'F' are commonly called “f-strings” which is short for formatted string literals. See also [**PEP 498**](https://www.python.org/dev/peps/pep-0498).

**file object** An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource. Depending on the way it was created, a file object can mediate access to a real on-disk file or to another type of storage or communication device (for example standard input/output, in-memory buffers, sockets, pipes, etc.). File objects are also called file-like objects or streams.

There are actually three categories of file objects: raw binary files, buffered binary files and text files. Their interfaces are defined in the io module. The canonical way to create a file object is by using the open() function.

**file-like object** A synonym for file object.

**filesystem encoding and error handler** Encoding and error handler used by Python to decode bytes from the operating system and encode Unicode to the operating system.

The filesystem encoding must guarantee to successfully decode all bytes below 128. If the file system encoding fails to provide this guarantee, API functions can raise UnicodeError.

The sys.getfilesystemencoding() and sys.getfilesystemencodeerrors() functions can be used to get the filesystem encoding and error handler.

The filesystem encoding and error handler are configured at Python startup by the PyConfig\_Read() function: see filesystem\_encoding and filesystem\_errors members of PyConfig.

See also the locale encoding.

**finder** An object that tries to find the loader for a module that is being imported.

Since Python 3.3, there are two types of finder: meta path finders for use with sys.meta\_path, and path entry finders for use with sys.path\_hooks.

See [**PEP 302**](https://www.python.org/dev/peps/pep-0302), [**PEP 420**](https://www.python.org/dev/peps/pep-0420) and [**PEP 451**](https://www.python.org/dev/peps/pep-0451) for much more detail.

**floor division** Mathematical division that rounds down to nearest integer. The floor division operator is //. For example, the expression 11 // 4 evaluates to 2 in contrast to the 2.75 returned by float true division. Note that (-11) // 4 is -3 because that is -2.75 rounded downward. See [**PEP 238**](https://www.python.org/dev/peps/pep-0238).

**function** A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body. See also parameter, method, and the function section.

**function annotation** An annotation of a function parameter or return value.

Function annotations are usually used for type hints: for example, this function is expected to take two int arguments and is also expected to have an int return value:

```python
def sum_two_numbers(a: int, b: int) -> int:
    return a + b
```

Function annotation syntax is explained in section function.

See variable annotation and [**PEP 484**](https://www.python.org/dev/peps/pep-0484), which describe this functionality. Also see annotations-howto for best practices on working with annotations.

future\_\_ A future statement, from **\_\_future\_\_** import &lt;feature&gt;, directs the compiler to compile the current module using syntax or semantics that will become standard in a future release of Python. The future\_\_ module documents the possible values of feature. By importing this module and evaluating its variables, you can see when a new feature was first added to the language and when it will (or did) become the default:

```python
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
```

**garbage collection** The process of freeing memory when it is not used anymore. Python performs garbage collection via reference counting and a cyclic garbage collector that is able to detect and break reference cycles. The garbage collector can be controlled using the gc module.

**generator** A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

Usually refers to a generator function, but may refer to a generator iterator in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

**generator iterator** An object created by a generator function.

Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

**generator expression** An expression that returns an iterator. It looks like a normal expression followed by a for clause defining a loop variable, range, and an optional if clause. The combined expression generates values for an enclosing function:

```python
>>> sum(i*i for i in range(10))          # sum of squares 0, 1, 4, ... 81
285
```

**generic function** A function composed of multiple functions implementing the same operation for different types. Which implementation should be used during a call is determined by the dispatch algorithm.

See also the single dispatch glossary entry, the functools.singledispatch() decorator, and [**PEP 443**](https://www.python.org/dev/peps/pep-0443).

**generic type** A type that can be parameterized; typically a container class such as list or dict. Used for type hints and annotations.

For more details, see generic alias types, [**PEP 483**](https://www.python.org/dev/peps/pep-0483), [**PEP 484**](https://www.python.org/dev/peps/pep-0484), [**PEP 585**](https://www.python.org/dev/peps/pep-0585), and the typing module.

**GIL** See global interpreter lock.

**global interpreter lock** The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This simplifies the CPython implementation by making the object model (including critical built-in types such as dict) implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

However, some extension modules, either standard or third-party, are designed so as to release the GIL when doing computationally intensive tasks such as compression or hashing. Also, the GIL is always released when doing I/O.

Past efforts to create a “free-threaded” interpreter (one which locks shared data at a much finer granularity) have not been successful because performance suffered in the common single-processor case. It is believed that overcoming this performance issue would make the implementation much more complicated and therefore costlier to maintain.

**hash-based pyc** A bytecode cache file that uses the hash rather than the last-modified time of the corresponding source file to determine its validity. See pyc-invalidation.

**hashable** An object is hashable if it has a hash value which never changes during its lifetime (it needs a \_hash\_\_() method), and can be compared to other objects (it needs an \_\_eq\_\_() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

Most of Python’s immutable built-in objects are hashable; mutable containers (such as lists or dictionaries) are not; immutable containers (such as tuples and frozensets) are only hashable if their elements are hashable. Objects which are instances of user-defined classes are hashable by default. They all compare unequal (except with themselves), and their hash value is derived from their id().

**IDLE** An Integrated Development and Learning Environment for Python. idle is a basic editor and interpreter environment which ships with the standard distribution of Python.

**immutable** An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.

**import path** A list of locations (or path entries) that are searched by the path based finder for modules to import. During import, this list of locations usually comes from sys.path, but for subpackages it may also come from the parent package’s \_\_path\_\_ attribute.

**importing** The process by which Python code in one module is made available to Python code in another module.

**importer** An object that both finds and loads a module; both a finder and loader object.

**interactive** Python has an interactive interpreter which means you can enter statements and expressions at the interpreter prompt, immediately execute them and see their results. Just launch python with no arguments (possibly by selecting it from your computer’s main menu). It is a very powerful way to test out new ideas or inspect modules and packages (remember help(x)).

**interpreted** Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. This means that source files can be run directly without explicitly creating an executable which is then run. Interpreted languages typically have a shorter development/debug cycle than compiled ones, though their programs generally also run more slowly. See also interactive.

**interpreter shutdown** When asked to shut down, the Python interpreter enters a special phase where it gradually releases all allocated resources, such as modules and various critical internal structures. It also makes several calls to the garbage collector. This can trigger the execution of code in user-defined destructors or weakref callbacks. Code executed during the shutdown phase can encounter various exceptions as the resources it relies on may not function anymore (common examples are library modules or the warnings machinery).

The main reason for interpreter shutdown is that the \_\_main\_\_ module or the script being run has finished executing.

**iterable** An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an \_\_iter\_\_() method or with a \_\_getitem\_\_() method that implements Sequence semantics.

Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.

**iterator** An object representing a stream of data. Repeated calls to the iterator’s \_\_next\_\_() method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its \_\_next\_\_() method just raise StopIteration again. Iterators are required to have an iter\_\_() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

More information can be found in typeiter.

**CPython implementation detail:** CPython does not consistently apply the requirement that an iterator define iter\_\_().

**key function** A key function or collation function is a callable that returns a value used for sorting or ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale specific sort conventions.

A number of tools in Python accept key functions to control how elements are ordered or grouped. They include min(), max(), sorted(), list.sort(), heapq.merge(), heapq.nsmallest(), heapq. nlargest(), and itertools.groupby().

There are several ways to create a key function. For example. the str.lower() method can serve as a key function for case insensitive sorts. Alternatively, a key function can be built from a lambda expression such as lambda r: (r[0], r[2]). Also, the operator module provides three key function constructors: attrgetter(), itemgetter(), and methodcaller(). See the Sorting HOW TO for examples of how to create and use key functions.

## keyword argument See argument.

**lambda** An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [parameters]: expression

**LBYL** Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the EAFP approach and is characterized by the presence of many if statements.

In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the looking” and “the leaping”. For example, the code, if key in mapping: return mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. This issue can be solved with locks or by using the EAFP approach.

**locale encoding** On Unix, it is the encoding of the LC\_CTYPE locale. It can be set with locale. setlocale(locale.LC\_CTYPE, new\_locale).

On Windows, it is the ANSI code page (ex: cp1252).

locale.getpreferredencoding(False) can be used to get the locale encoding.

Python uses the filesystem encoding and error handler to convert between Unicode filenames and bytes filenames.

**list** A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).

**list comprehension** A compact way to process all or part of the elements in a sequence and return a list with the results. result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0] generates a list of strings containing even hex numbers (0x..) in the range from 0 to 255. The if clause is optional. If omitted, all elements in range(256) are processed.

**loader** An object that loads a module. It must define a method named load\_module(). A loader is typically returned by a finder. See [**PEP 302**](https://www.python.org/dev/peps/pep-0302) for details and importlib.abc.Loader for an abstract base class.

**magic method** An informal synonym for special method.

**mapping** A container object that supports arbitrary key lookups and implements the methods specified in the Mapping or MutableMapping abstract base classes. Examples include dict, collections. defaultdict, collections.OrderedDict and collections.Counter.

**meta path finder** A finder returned by a search of sys.meta\_path. Meta path finders are related to, but different from path entry finders.

See importlib.abc.MetaPathFinder for the methods that meta path finders implement.

**metaclass** The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses. Most users never need this tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have been used for logging attribute access, adding thread-safety, tracking object creation, implementing singletons, and many other tasks.

More information can be found in metaclasses.

**method** A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self). See function and nested scope.

**method resolution order** Method Resolution Order is the order in which base classes are searched for a member during lookup. See [The Python 2.3 Method Resolution Order](https://www.python.org/download/releases/2.3/mro/) for details of the algorithm used by the Python interpreter since the 2.3 release.

**module** An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

See also package.

**module spec** A namespace containing the import-related information used to load a module. An instance of importlib.machinery.ModuleSpec.

**MRO** See method resolution order.

**mutable** Mutable objects can change their value but keep their id(). See also immutable.

**named tuple** The term “named tuple” applies to any type or class that inherits from tuple and whose indexable elements are also accessible using named attributes. The type or class may have other features as well.

Several built-in types are named tuples, including the values returned by time.localtime() and os. stat(). Another example is sys.float\_info:

```python
>>> sys.float_info[1]                      # indexed access
1024
>>> sys.float_info.max_exp                 # named field access
1024
>>> isinstance(sys.float_info, tuple)   # kind of tuple
True
```

Some named tuples are built-in types (such as the above examples). Alternatively, a named tuple can be created from a regular class definition that inherits from tuple and that defines named fields. Such a class can be written by hand or it can be created with the factory function collections.namedtuple(). The latter technique also adds some extra methods that may not be found in hand-written or built-in named tuples.

**namespace** The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions builtins.open and os.open() are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.islice() makes it clear that those functions are implemented by the random and itertools modules, respectively.

**namespace package** A [**PEP 420**](https://www.python.org/dev/peps/pep-0420) package which serves only as a container for subpackages. Namespace packages may have no physical representation, and specifically are not like a regular package because they have no init\_\_.py file.

See also module.

**nested scope** The ability to refer to a variable in an enclosing definition. For instance, a function defined inside another function can refer to variables in the outer function. Note that nested scopes by default work only for reference and not for assignment. Local variables both read and write in the innermost scope. Likewise, global variables read and write to the global namespace. The nonlocal allows writing to outer scopes.

**new-style class** Old name for the flavor of classes now used for all class objects. In earlier Python versions, only new-style classes could use Python’s newer, versatile features like \_\_slots\_\_, descriptors, properties, getattribute\_\_(), class methods, and static methods.

**object** Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.

**package** A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with a \_\_path\_\_ attribute.

See also regular package and namespace package.

**parameter** A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept. There are five kinds of parameter:

• positional-or-keyword: specifies an argument that can be passed either positionally or as a keyword argument. This is the default kind of parameter, for example foo and bar in the following:

```python
def func(foo, bar=None): ...
```

• positional-only: specifies an argument that can be supplied only by position. Positional-only parameters can be defined by including a / character in the parameter list of the function definition after them, for example posonly1 and posonly2 in the following:

```python
def func(posonly1, posonly2, /, positional_or_keyword): ...
```

• keyword-only: specifies an argument that can be supplied only by keyword. Keyword-only parameters can be defined by including a single var-positional parameter or bare \* in the parameter list of the function definition before them, for example kw\_only1 and kw\_only2 in the following:

```python
def func(arg, *, kw_only1, kw_only2): ...
```

• var-positional: specifies that an arbitrary sequence of positional arguments can be provided (in addition to any positional arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with \*, for example args in the following:

```python
def func(*args, **kwargs): ...
```

• var-keyword: specifies that arbitrarily many keyword arguments can be provided (in addition to any keyword arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with \*\*, for example kwargs in the example above.

Parameters can specify both optional and required arguments, as well as default values for some optional arguments.

See also the argument glossary entry, the FAQ question on the difference between arguments and parameters, the inspect.Parameter class, the function section, and [**PEP 362**](https://www.python.org/dev/peps/pep-0362).

**path entry** A single location on the import path which the path based finder consults to find modules for importing.

**path entry finder** A finder returned by a callable on sys.path\_hooks (i.e. a path entry hook) which knows how to locate modules given a path entry.

See importlib.abc.PathEntryFinder for the methods that path entry finders implement.

**path entry hook** A callable on the sys.path\_hook list which returns a path entry finder if it knows how to find modules on a specific path entry.

**path based finder** One of the default meta path finders which searches an import path for modules.

**path-like object** An object representing a file system path. A path-like object is either a str or bytes object representing a path, or an object implementing the os.PathLike protocol. An object that supports the os. PathLike protocol can be converted to a str or bytes file system path by calling the os.fspath() function; os.fsdecode() and os.fsencode() can be used to guarantee a str or bytes result instead, respectively. Introduced by [**PEP 519**](https://www.python.org/dev/peps/pep-0519).

**PEP** Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. PEPs should provide a concise technical specification and a rationale for proposed features.

PEPs are intended to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.

**portion** A set of files in a single directory (possibly stored in a zip file) that contribute to a namespace package, as defined in [**PEP 420**](https://www.python.org/dev/peps/pep-0420).

**positional argument** See argument.

**provisional API** A provisional API is one which has been deliberately excluded from the standard library’s backwards compatibility guarantees. While major changes to such interfaces are not expected, as long as they are marked provisional, backwards incompatible changes (up to and including removal of the interface) may occur if deemed necessary by core developers. Such changes will not be made gratuitously – they will occur only if serious fundamental flaws are uncovered that were missed prior to the inclusion of the API.

Even for provisional APIs, backwards incompatible changes are seen as a “solution of last resort” - every attempt will still be made to find a backwards compatible resolution to any identified problems.

This process allows the standard library to continue to evolve over time, without locking in problematic design errors for extended periods of time. See [**PEP 411**](https://www.python.org/dev/peps/pep-0411) for more details.

**provisional package** See provisional API.

**Python 3000** Nickname for the Python 3.x release line (coined long ago when the release of version 3 was something in the distant future.) This is also abbreviated “Py3k”.

**Pythonic** An idea or piece of code which closely follows the most common idioms of the Python language, rather than implementing code using concepts common to other languages. For example, a common idiom in Python is to loop over all elements of an iterable using a for statement. Many other languages don’t have this type of construct, so people unfamiliar with Python sometimes use a numerical counter instead:

```python
for i in range(len(food)):
    print(food[i])
```

As opposed to the cleaner, Pythonic method:

```python
for piece in food:
    print(piece)
```

**qualified name** A dotted name showing the “path” from a module’s global scope to a class, function or method defined in that module, as defined in [**PEP 3155**](https://www.python.org/dev/peps/pep-3155). For top-level functions and classes, the qualified name is the same as the object’s name:

```python
>>> class C:
...     class D:
...         def meth(self):
...             pass
>>> C.__qualname__
'C'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__qualname__
'C.D.meth'
```

When used to refer to modules, the fully qualified name means the entire dotted path to the module, including any parent packages, e.g. email.mime.text:

```python
>>> import email.mime.text
>>> email.mime.text.__name'
'Semail.mime.text'
```

**reference count** The number of references to an object. When the reference count of an object drops to zero, it is deallocated. Reference counting is generally not visible to Python code, but it is a key element of the CPython implementation. The sys module defines a getrefcount() function that programmers can call to return the reference count for a particular object.

**regular package** A traditional package, such as a directory containing an \_\_init\_\_.py file.

See also namespace package.

slots\_\_ A declaration inside a class that saves memory by pre-declaring space for instance attributes and eliminating instance dictionaries. Though popular, the technique is somewhat tricky to get right and is best reserved for rare cases where there are large numbers of instances in a memory-critical application.

**sequence** An iterable which supports efficient element access using integer indices via the \_\_getitem\_\_() special method and defines a \_\_len\_\_() method that returns the length of the sequence. Some built-in sequence types are list, str, tuple, and bytes. Note that dict also supports \_\_getitem\_\_() and \_len\_\_(), but is considered a mapping rather than a sequence because the lookups use arbitrary immutable keys rather than integers.

The collections.abc.Sequence abstract base class defines a much richer interface that goes beyond just \_\_getitem\_\_() and \_\_len\_\_(), adding count(), index(), \_\_contains\_\_(), and reversed\_\_(). Types that implement this expanded interface can be registered explicitly using register().

**set comprehension** A compact way to process all or part of the elements in an iterable and return a set with the results. results = {c for c in 'abracadabra' if c not in 'abc'} generates the set of strings {'r', 'd'}. See comprehensions.

**single dispatch** A form of generic function dispatch where the implementation is chosen based on the type of a single argument.

**slice** An object usually containing a portion of a sequence. A slice is created using the subscript notation, [] with colons between numbers when several are given, such as in variable\_name[1:3:5]. The bracket (subscript) notation uses slice objects internally.

**special method** A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. Special methods are documented in specialnames.

**statement** A statement is part of a suite (a “block” of code). A statement is either an expression or one of several constructs with a keyword, such as if, while or for.

**strong reference** In Python’s C API, a strong reference is a reference to an object which is owned by the code holding the reference. The strong reference is taken by calling Py\_INCREF() when the reference is created and released with Py\_DECREF() when the reference is deleted.

The Py\_NewRef() function can be used to create a strong reference to an object. Usually, the Py\_DECREF() function must be called on the strong reference before exiting the scope of the strong reference, to avoid leaking one reference.

See also borrowed reference.

**text encoding** A string in Python is a sequence of Unicode code points (in range U+0000–U+10FFFF). To store or transfer a string, it needs to be serialized as a sequence of bytes.

Serializing a string into a sequence of bytes is known as “encoding”, and recreating the string from the sequence of bytes is known as “decoding”.

There are a variety of different text serialization codecs, which are collectively referred to as “text encodings”.

**text file** A file object able to read and write str objects. Often, a text file actually accesses a byte-oriented datastream and handles the text encoding automatically. Examples of text files are files opened in text mode ('r' or 'w'), sys.stdin, sys.stdout, and instances of io.StringIO.

See also binary file for a file object able to read and write bytes-like objects.

**triple-quoted string** A string which is bound by three instances of either a quotation mark (”) or an apostrophe (‘). While they don’t provide any functionality not available with single-quoted strings, they are useful for a number of reasons. They allow you to include unescaped single and double quotes within a string and they can span multiple lines without the use of the continuation character, making them especially useful when writing docstrings.

**type** The type of a Python object determines what kind of object it is; every object has a type. An object’s type is accessible as its \_\_class\_\_ attribute or can be retrieved with type(obj).

**type alias** A synonym for a type, created by assigning the type to an identifier.

Type aliases are useful for simplifying type hints. For example:

```python
def remove_gray_shades(
    colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    pass
```

could be made more readable like this:

```python
Color = tuple[int, int, int]

def remove_gray_shades(colors: list[Color]) -> list[Color]:
    pass
```

See typing and [**PEP 484**](https://www.python.org/dev/peps/pep-0484), which describe this functionality.

**type hint** An annotation that specifies the expected type for a variable, a class attribute, or a function parameter or return value.

Type hints are optional and are not enforced by Python but they are useful to static type analysis tools, and aid IDEs with code completion and refactoring.

Type hints of global variables, class attributes, and functions, but not local variables, can be accessed using typing.get\_type\_hints().

See typing and [**PEP 484**](https://www.python.org/dev/peps/pep-0484), which describe this functionality.

**universal newlines** A manner of interpreting text streams in which all of the following are recognized as ending a line: the Unix end-of-line convention '\n', the Windows convention '\r\n', and the old Macintosh convention '\r'. See [**PEP 278**](https://www.python.org/dev/peps/pep-0278) and [**PEP 3116**](https://www.python.org/dev/peps/pep-3116), as well as bytes.splitlines() for an additional use.

**variable annotation** An annotation of a variable or a class attribute.

When annotating a variable or a class attribute, assignment is optional:

```python
class C:
    field: 'annotation'
```

Variable annotations are usually used for type hints: for example this variable is expected to take int values:

```txt
count: int = 0
```

Variable annotation syntax is explained in section annassign.

See function annotation, [**PEP 484**](https://www.python.org/dev/peps/pep-0484) and [**PEP 526**](https://www.python.org/dev/peps/pep-0526), which describe this functionality. Also see annotations-howto for best practices on working with annotations.

**virtual environment** A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.

See also venv.

**virtual machine** A computer defined entirely in software. Python’s virtual machine executes the bytecode emitted by the bytecode compiler.

**Zen of Python** Listing of Python design principles and philosophies that are helpful in understanding and using the language. The listing can be found by typing “import this” at the interactive prompt.

## ABOUT THESE DOCUMENTS

These documents are generated from [reStructuredText](https://docutils.sourceforge.io/rst.html) sources by [Sphinx](https://www.sphinx-doc.org/), a document processor specifically written for the Python documentation.

Development of the documentation and its toolchain is an entirely volunteer effort, just like Python itself. If you want to contribute, please take a look at the reporting-bugs page for information on how to do so. New volunteers are always welcome!

## Many thanks go to:

• Fred L. Drake, Jr., the creator of the original Python documentation toolset and writer of much of the content;

• the [Docutils](https://docutils.sourceforge.io/) project for creating reStructuredText and the Docutils suite;

• Fredrik Lundh for his Alternative Python Reference project from which Sphinx got many good ideas.

## B.1 Contributors to the Python Documentation

Many people have contributed to the Python language, the Python standard library, and the Python documentation. See [Misc/ACKS](https://github.com/python/cpython/tree/3.10/Misc/ACKS) in the Python source distribution for a partial list of contributors.

It is only with the input and contributions of the Python community that Python has such wonderful documentation – Thank You!

## HISTORY AND LICENSE

## C.1 History of the software

Python was created in the early 1990s by Guido van Rossum at Stichting Mathematisch Centrum (CWI, see [https://www.cwi.nl/](https://www.cwi.nl/)) in the Netherlands as a successor of a language called ABC. Guido remains Python’s principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for National Research Initiatives (CNRI, see [https://www.cnri.reston.va.us/](https://www.cnri.reston.va.us/)) in Reston, Virginia where he released several versions of the software.

In May 2000, Guido and the Python core development team moved to BeOpen.com to form the BeOpen Python-Labs team. In October of the same year, the PythonLabs team moved to Digital Creations (now Zope Corporation; see [https://www.zope.org/](https://www.zope.org/)). In 2001, the Python Software Foundation (PSF, see [https://www.python.org/psf/](https://www.python.org/psf/)) was formed, a non-profit organization created specifically to own Python-related Intellectual Property. Zope Corporation is a sponsoring member of the PSF.

All Python releases are Open Source (see [https://opensource.org/](https://opensource.org/) for the Open Source Definition). Historically, most, but not all, Python releases have also been GPL-compatible; the table below summarizes the various releases.

| Release | Derived from | Year | Owner | GPL compatible? |
| --- | --- | --- | --- | --- |
| 0.9.0 thru 1.2 | n/a | 1991-1995 | CWI | yes |
| 1.3 thru 1.5.2 | 1.2 | 1995-1999 | CNRI | yes |
| 1.6 | 1.5.2 | 2000 | CNRI | no |
| 2.0 | 1.6 | 2000 | BeOpen.com | no |
| 1.6.1 | 1.6 | 2001 | CNRI | no |
| 2.1 | 2.0+1.6.1 | 2001 | PSF | no |
| 2.0.1 | 2.0+1.6.1 | 2001 | PSF | yes |
| 2.1.1 | 2.1+2.0.1 | 2001 | PSF | yes |
| 2.1.2 | 2.1.1 | 2002 | PSF | yes |
| 2.1.3 | 2.1.2 | 2002 | PSF | yes |
| 2.2 and above | 2.1.1 | 2001-now | PSF | yes |

**Note:** GPL-compatible doesn’t mean that we’re distributing Python under the GPL. All Python licenses, unlike the GPL, let you distribute a modified version without making your changes open source. The GPL-compatible licenses make it possible to combine Python with other software that is released under the GPL; the others don’t.

## C.2 Terms and conditions for accessing or otherwise using Python

Python software and documentation are licensed under the PSF License Agreement.

Starting with Python 3.8.6, examples, recipes, and other code in the documentation are dual licensed under the PSF License Agreement and the Zero-Clause BSD license.

Some software incorporated into Python is under different licenses. The licenses are listed with code falling under that license. See Licenses and Acknowledgements for Incorporated Software for an incomplete list of these licenses.

## C.2.1 PSF LICENSE AGREEMENT FOR PYTHON 3.10.15

```txt
1. This LICENSE AGREEMENT is between the Python Software Foundation
  ( "PSF"), and
    the Individual or Organization ("Licensee") accessing and otherwise
  using Python
    3.10.15 software in source or binary form and its associated
  documentation.
txt
2. Subject to the terms and conditions of this License Agreement, PSF
→ hereby
  grants Licensee a nonexclusive, royalty-free, world-wide license to
→ reproduce,
  analyze, test, perform and/or display publicly, prepare derivative
→ works,
  distribute, and otherwise use Python 3.10.15 alone or in any derivative
  version, provided, however, that PSF's License Agreement and PSF's
→ notice of
  copyright, i.e., "Copyright © 2001-2023 Python Software Foundation; All
→ Rights
  Reserved" are retained in Python 3.10.15 alone or in any derivative
→ version
  prepared by Licensee.
txt
3. In the event Licensee prepares a derivative work that is based on or incorporates Python 3.10.15 or any part thereof, and wants to make the derivative work available to others as provided herein, then Licensee hereby agrees to include in any such work a brief summary of the changes made to Python 3.10.15.
txt
4. PSF is making Python 3.10.15 available to Licensee on an "AS IS" basis.
    PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF
    EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
    WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
    USE OF PYTHON 3.10.15 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
txt
5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 3.10.15
    FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A
→RESULT OF
MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 3.10.15, OR ANY
→DERIVATIVE
THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.
txt
6. This License Agreement will automatically terminate upon a material
    breach of
        its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
    relationship
        of agency, partnership, or joint venture between PSF and Licensee.
    This License
        Agreement does not grant permission to use PSF trademarks or trade name
    in a
        trademark sense to endorse or promote products or services of Licensee,
    or any
        third party.

8. By copying, installing or otherwise using Python 3.10.15, Licensee
    agrees
        to be bound by the terms and conditions of this License Agreement.
```

## C.2.2 BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0

## BEOPEN PYTHON OPEN SOURCE LICENSE AGREEMENT VERSION 1

```txt
This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an office at 160 Saratoga Avenue, Santa Clara, CA 95051, and the Individual or Organization ("Licensee") accessing and otherwise using this software in source or binary form and its associated documentation ("the Software").
Subject to the terms and conditions of this BeOpen Python License Agreement, BeOpen hereby grants Licensee a non-exclusive, royalty-free, world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use the Software alone or in any derivative version, provided, however, that the BeOpen Python License is retained in the Software, alone or in any derivative version prepared by Licensee.
BeOpen is making the Software available to Licensee on an "AS IS" basis. BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE SOFTWARE WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE SOFTWARE FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THE SOFTWARE, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.
This License Agreement will automatically terminate upon a material breach of its terms and conditions.
This License Agreement shall be governed by and interpreted in all respects by the law of the State of California, excluding conflict of law provisions. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between BeOpen and Licensee. This License Agreement does not grant permission to use BeOpen trademarks or trade names in a trademark sense to endorse or promote products or services of Licensee, or any third party. As an exception, the "BeOpen Python" logos available at http://www.pythonlabs.com/logos.html may be used according to the permissions granted on that web page.
```

(continues on next page)

(continued from previous page)

7. By copying, installing or otherwise using the software, Licensee agrees to be bound by the terms and conditions of this License Agreement.

## C.2.3 CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1

1. This LICENSE AGREEMENT is between the Corporation for National Research Initiatives, having an office at 1895 Preston White Drive, Reston, VA 20191 ("CNRI"), and the Individual or Organization ("Licensee") accessing and otherwise using Python 1.6.1 software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, CNRI hereby grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use Python 1.6.1 alone or in any derivative version, provided, however, that CNRI's License Agreement and CNRI's notice of copyright, i.e., "Copyright © 1995-2001 Corporation for National Research Initiatives; All Rights Reserved" are retained in Python 1.6.1 alone or in any derivative version prepared by Licensee. Alternately, in lieu of CNRI's License Agreement, Licensee may substitute the following text (omitting the quotes): "Python 1.6.1 is made available subject to the terms and conditions in CNRI's License Agreement. This Agreement together with Python 1.6.1 may be located on the internet using the following unique, persistent identifier (known as a handle): 1895.22/1013. This Agreement may also be obtained from a proxy server on the internet using the following URL: http://hdl.handle.net/1895.22/1013."

3. In the event Licensee prepares a derivative work that is based on or incorporates Python 1.6.1 or any part thereof, and wants to make the derivative work available to others as provided herein, then Licensee hereby agrees to include in any such work a brief summary of the changes made to Python 1.6.1.

4. CNRI is making Python 1.6.1 available to Licensee on an "AS IS" basis. CNRI MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, CNRI MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON 1.6.1 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. CNRI SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 1.6.1 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 1.6.1, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of its terms and conditions.

7. This License Agreement shall be governed by the federal intellectual property law of the United States, including without limitation the federal copyright law, and, to the extent such U.S. federal law does not apply, by the law of the Commonwealth of Virginia, excluding Virginia's conflict of law provisions. Notwithstanding the foregoing, with regard to derivative works based on Python 1.6.1 that incorporate non-separable material that was previously distributed under the GNU General Public License (GPL), the law of the Commonwealth of Virginia shall govern this License Agreement only as to issues arising under or with respect to Paragraphs 4, 5, and 7 of this License Agreement. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between CNRI and Licensee. This License Agreement does not grant permission to use CNRI trademarks or trade name in a trademark sense to endorse or promote products or services of Licensee, or any third party.

(continues on next page)

```txt
(continued from previous page)

8. By clicking on the "ACCEPT" button where indicated, or by copying, installing or otherwise using Python 1.6.1, Licensee agrees to be bound by the terms and conditions of this License Agreement.
```

## C.2.4 CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2

```txt
Copyright © 1991 - 1995, Stichting Mathematisch Centrum Amsterdam, The Netherlands. All rights reserved.

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Stichting Mathematisch Centrum or CWI not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

STICHTING MATHEMATISCH CENTRUM DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL STICHTING MATHEMATISCH CENTRUM BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.2.5 ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON 3.10.15 DOCU-MENTATION

```txt
Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3 Licenses and Acknowledgements for Incorporated Software

This section is an incomplete, but growing list of licenses and acknowledgements for third-party software incorporated in the Python distribution.

## C.3.1 Mersenne Twister

The \_random module includes code based on a download from [http://www.math.sci.hiroshima-u.ac.jp/\~m-mat/MT/MT2002/emt19937ar.html](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/emt19937ar.html). The following are the verbatim comments from the original code:

```txt
A C-program for MT19937, with initialization improved 2002/1/26.
Coded by Takuji Nishimura and Makoto Matsumoto.

Before using, initialize the state by using init_genrand(seed)
or init_by_array(init_key, key_length).

Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
    1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

    3. The names of its contributors may not be used to endorse or promote
    products derived from this software without specific prior written
    permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Any feedback is very welcome.
http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
email: m-mat @ math.sci.hiroshima-u.ac.jp (remove space)
```

## C.3.2 Sockets

The socket module uses the functions, getaddrinfo(), and getnameinfo(), which are coded in separate source files from the WIDE Project, [https://www.wide.ad.jp/](https://www.wide.ad.jp/).

```txt
Copyright (C) 1995, 1996, 1997, and 1998 WIDE Project.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the project nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.3 Asynchronous socket services

The asynchat and asyncore modules contain the following notice:

```txt
Copyright 1996 by Sam Rushing
All Rights Reserved
Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Sam Rushing not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.
SAM RUSHING DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL SAM RUSHING BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.4 Cookie management

The http.cookies module contains the following notice:

```txt
Copyright 2000 by Timothy O'Malley <timo@alum.mit.edu>

All Rights Reserved

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Timothy O'Malley not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

Timothy O'Malley DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL Timothy O'Malley BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.5 Execution tracing

The trace module contains the following notice:

```txt
portions copyright 2001, Autonomous Zones Industries, Inc., all rights...
err... reserved and offered to the public under the terms of the
Python 2.2 license.
Author: Zooko O'Whielacronx
http://zooko.com/
mailto:zooko@zooko.com

Copyright 2000, Mojam Media, Inc., all rights reserved.
Author: Skip Montanaro

Copyright 1999, Bioreason, Inc., all rights reserved.
Author: Andrew Dalke

Copyright 1995-1997, Automatrix, Inc., all rights reserved.
Author: Skip Montanaro

Copyright 1991-1995, Stichting Mathematisch Centrum, all rights reserved.

Permission to use, copy, modify, and distribute this Python software and
its associated documentation for any purpose without fee is hereby
granted, provided that the above copyright notice appears in all copies,
and that both that copyright notice and this permission notice appear in
supporting documentation, and that the name of neither Automatrix,
Bioreason or Mojam Media be used in advertising or publicity pertaining to
distribution of the software without specific, written prior permission.
```

## C.3.6 UUencode and UUdecode functions

The uu module contains the following notice:

```txt
Copyright 1994 by Lance Ellinghouse
Cathedral City, California Republic, United States of America.
All Rights Reserved
Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Lance Ellinghouse not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.
LANCE ELLINGHOUSE DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL LANCE ELLINGHOUSE CENTRUM BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Modified by Jack Jansen, CWI, July 1995:
- Use binascii module to do the actual line-by-line conversion between ascii and binary. This results in a 1000-fold speedup. The C version is still 5 times faster, though.
- Arguments more compliant with Python standard
```

## C.3.7 XML Remote Procedure Calls

The xmlrpc.client module contains the following notice:

```txt
The XML-RPC client interface is

Copyright (c) 1999-2002 by Secret Labs AB
Copyright (c) 1999-2002 by Fredrik Lundh

By obtaining, using, and/or copying this software and/or its associated documentation, you agree that you have read, understood, and will comply with the following terms and conditions:

Permission to use, copy, modify, and distribute this software and its associated documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Secret Labs AB or the author not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.8 test\_epoll

The test\_epoll module contains the following notice:

```txt
Copyright (c) 2001-2006 Twisted Matrix Laboratories.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## C.3.9 Select kqueue

The select module contains the following notice for the kqueue interface:

```txt
Copyright (c) 2000 Doug White, 2006 James Knight, 2007 Christian Heimes All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.10 SipHash24

The file Python/pyhash.c contains Marek Majkowski’ implementation of Dan Bernstein’s SipHash24 algorithm. It contains the following note:

```txt
<MIT License>
Copyright (c) 2013 Marek Majkowski <marek@popcount.org>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
</MIT License>

Original location:
https://github.com/majek/csiphash/

Solution inspired by code from:
Samuel Neves (supercop/crypto_auth/siphash24/little)
djb (supercop/crypto_auth/siphash24/little2)
Jean-Philippe Aumasson (https://131002.net/siphash/siphash24.c)
```

## C.3.11 strtod and dtoa

The file Python/dtoa.c, which supplies C functions dtoa and strtod for conversion of C doubles to and from strings, is derived from the file of the same name by David M. Gay, currently available from [https://web.archive.org/web/20220517033456/http://www.netlib.org/fp/dtoa.c](https://web.archive.org/web/20220517033456/http://www.netlib.org/fp/dtoa.c). The original file, as retrieved on March 16, 2009, contains the following copyright and licensing notice:

```c
/******************************************************************
*
* The author of this software is David M. Gay.
*
* Copyright (c) 1991, 2000, 2001 by Lucent Technologies.
*
* Permission to use, copy, modify, and distribute this software for any
* purpose without fee is hereby granted, provided that this entire notice
* is included in all copies of any software which is or includes a copy
* or modification of this software and in all copies of the supporting
* documentation for such software.
*
* THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
* WARRANTY. IN PARTICULAR, NEITHER THE AUTHOR NOR LUCENT MAKES ANY
* REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY
* OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.
*
**********************************************************************/
```

## C.3.12 OpenSSL

The modules hashlib, posix, ssl, crypt use the OpenSSL library for added performance if made available by the operating system. Additionally, the Windows and macOS installers for Python may include a copy of the OpenSSL libraries, so we include a copy of the OpenSSL license here:

```python
LICENSE ISSUES
==============================

The OpenSSL toolkit stays under a dual license, i.e. both the conditions of the OpenSSL License and the original SSLeay license apply to the toolkit.
See below for the actual license texts. Actually both licenses are BSD-style Open Source licenses. In case of any license issues related to OpenSSL please contact openssl-core@openssl.org.

OpenSSL License
---------------------------------------------------
/* =================……
* Copyright (c) 1998-2008 The OpenSSL Project. All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
*
* 1. Redistributions of source code must retain the above copyright
* notice, this list of conditions and the following disclaimer.
*
* 2. Redistributions in binary form must reproduce the above copyright
* notice, this list of conditions and the following disclaimer in
* the documentation and/or other materials provided with the
* distribution.
*
* 3. All advertising materials mentioning features or use of this
* software must display the following acknowledgment:
* "This product includes software developed by the OpenSSL Project
* for use in the OpenSSL Toolkit. (http://www.openssl.org/)"
*
* 4. The names "OpenSSL Toolkit" and "OpenSSL Project" must not be used to
* endorse or promote products derived from this software without
* prior written permission. For written permission, please contact
* openssl-core@openssl.org.
*
* 5. Products derived from this software may not be called "OpenSSL"
* nor may "OpenSSL" appear in their names without prior written
* permission of the OpenSSL Project.
*
* 6. Redistributions of any form whatsoever must retain the following
* acknowledgment:
* "This product includes software developed by the OpenSSL Project
* for use in the OpenSSL Toolkit (http://www.openssl.org/)"
*
* THIS SOFTWARE IS PROVIDED BY THE OpenSSL PROJECT ``AS IS'' AND ANY
* EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
* PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE OpenSSL PROJECT OR
* ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
* SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
* NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
* STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
```

(continues on next page)

(continued from previous page)

```txt
* ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
* OF THE POSSIBILITY OF SUCH DAMAGE.
* ====================
*
* This product includes cryptographic software written by Eric Young
* (eay@cryptsoft.com).  This product includes software written by Tim
* Hudson (tjh@cryptsoft.com).
*
*/

Original SSLeay License
-------------------------------------------------------------------

/* Copyright (C) 1995-1998 Eric Young (eay@cryptsoft.com)
* All rights reserved.
*
* This package is an SSL implementation written
* by Eric Young (eay@cryptsoft.com).
* The implementation was written so as to conform with Netscapes SSL.
*
* This library is free for commercial and non-commercial use as long as
* the following conditions are aheaded to.  The following conditions
* apply to all code found in this distribution, be it the RC4, RSA,
* lhash, DES, etc., code; not just the SSL code.  The SSL documentation
* included with this distribution is covered by the same copyright terms
* except that the holder is Tim Hudson (tjh@cryptsoft.com).
*
* Copyright remains Eric Young's, and as such any Copyright notices in
* the code are not to be removed.
* If this package is used in a product, Eric Young should be given attribution
* as the author of the parts of the library used.
* This can be in the form of a textual message at program startup or
* in documentation (online or textual) provided with the package.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
* 1. Redistributions of source code must retain the copyright
*    notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
*    notice, this list of conditions and the following disclaimer in the
*    documentation and/or other materials provided with the distribution.
* 3. All advertising materials mentioning features or use of this software
*    must display the following acknowledgement:
*    "This product includes cryptographic software written by
*    Eric Young (eay@cryptsoft.com)"
*    The word 'cryptographic' can be left out if the routines from the library
*    being used are not cryptographic related :-).
* 4. If you include any Windows specific code (or a derivative thereof) from
*    the apps directory (application code) you must include an acknowledgement:
*    "This product includes software written by Tim Hudson (tjh@cryptsoft.com)"
*
* THIS SOFTWARE IS PROVIDED BY ERIC YOUNG ``AS IS'' AND
* ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
* ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
* OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
```

(continues on next page)

(continued from previous page)

```c
* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
* SUCH DAMAGE.
*
* The licence and distribution terms for any publically available version or
* derivative of this code cannot be changed. i.e. this code cannot simply be
* copied and put under another distribution licence
* [including the GNU Public Licence.]
*/
```

## C.3.13 expat

The pyexpat extension is built using an included copy of the expat sources unless the build is configured --with-system-expat:

```txt
Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd and Clark Cooper

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## C.3.14 libffi

The \_ctypes extension is built using an included copy of the libffi sources unless the build is configured --with-system-libffi:

```txt
Copyright (c) 1996-2008 Red Hat, Inc and others.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ``Software''), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ``AS IS'', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
```

(continues on next page)

```txt
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

(continued from previous page)

## C.3.15 zlib

The zlib extension is built using an included copy of the zlib sources if the zlib version found on the system is too old to be used for the build:

```txt
Copyright (C) 1995-2011 Jean-loup Gailly and Mark Adler

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source distribution.

Jean-loup Gailly          Mark Adler
jloup@gzip.org           madler@alumni.caltech.edu
```

## C.3.16 cfuhash

The implementation of the hash table used by the tracemalloc is based on the cfuhash project:

```txt
Copyright (c) 2005 Don Owens
All rights reserved.

This code is released under the BSD license:

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* Neither the name of the author nor the names of its contributors may be used to endorse or promote products derived
```

(continues on next page)

(continued from previous page)

```txt
from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.17 libmpdec

The \_decimal module is built using an included copy of the libmpdec library unless the build is configured --with-system-libmpdec:

```txt
Copyright (c) 2008-2020 Stefan Krah. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.18 W3C C14N test suite

The C14N 2.0 test suite in the test package (Lib/test/xmltestdata/c14n-20/) was retrieved from the W3C website at [https://www.w3.org/TR/xml-c14n2-testcases/](https://www.w3.org/TR/xml-c14n2-testcases/) and is distributed under the 3-clause BSD license:

```txt
Copyright (c) 2013 W3C(R) (MIT, ERCIM, Keio, Beihang), All Rights Reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
```

(continues on next page)

(continued from previous page)

```txt
* Redistributions of works must retain the original copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the W3C nor the names of its contributors may be used to endorse or promote products derived from this work without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.19 Audioop

The audioop module uses the code base in g771.c file of the SoX project. [https://sourceforge.net/projects/sox/files/sox/12.17.7/sox-12.17.7.tar.gz](https://sourceforge.net/projects/sox/files/sox/12.17.7/sox-12.17.7.tar.gz)

This source code is a product of Sun Microsystems, Inc. and is provided for unrestricted use. Users may copy or modify this source code without charge.

SUN SOURCE CODE IS PROVIDED AS IS WITH NO WARRANTIES OF ANY KIND INCLUD-ING THE WARRANTIES OF DESIGN, MERCHANTIBILITY AND FITNESS FOR A PARTICU-LAR PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE OR TRADE PRAC-TICE.

Sun source code is provided with no support and without any obligation on the part of Sun Microsystems, Inc. to assist in its use, correction, modification or enhancement.

SUN MICROSYSTEMS, INC. SHALL HAVE NO LIABILITY WITH RESPECT TO THE IN-FRINGEMENT OF COPYRIGHTS, TRADE SECRETS OR ANY PATENTS BY THIS SOFTWARE OR ANY PART THEREOF.

In no event will Sun Microsystems, Inc. be liable for any lost revenue or profits or other special, indirect and consequential damages, even if Sun has been advised of the possibility of such damages.

Sun Microsystems, Inc. 2550 Garcia Avenue Mountain View, California 94043

## COPYRIGHT

Python and this documentation is:

Copyright © 2001-2023 Python Software Foundation. All rights reserved.

Copyright © 2000 BeOpen.com. All rights reserved.

Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.

Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.

See History and License for complete license and permissions information.

## Non-alphabetical

```python
..., **261** 2to3, **261** >>>, **261** all\_\_ (package variable), 62 dict\_\_ (module attribute), 146 doc\_\_ (module attribute), 146 file\_\_ (module attribute), 146, 147 future\_\_, **265** import built-in function, 62 loader\_\_ (module attribute), 146 main module, 11, 168, 179 name\_\_ (module attribute), 146 package\_\_ (module attribute), 146 PYVENV\_LAUNCHER\_\_, 192, 196 slots\_\_, **271** \_frozen (C struct), 64 \_inittab (C struct), 65 \_Py\_c\_diff (C function), 111 \_Py\_c\_neg (C function), 111 \_Py\_c\_pow (C function), 111 \_Py\_c\_prod (C function), 111 \_Py\_c\_quot (C function), 111 \_Py\_c\_sum (C function), 111 \_Py\_InitializeMain (C function), 203 \_Py\_NoneStruct (C var), 215 \_PyBytes\_Resize (C function), 114 \_PyCFunctionFast (C type), 218 \_PyCFunctionFastWithKeywords (C type), 218 \_PyFrameEvalFunction (C type), 177 \_PyInterpreterState\_GetEvalFrameFunc (C function), 177 \_PyInterpreterState\_SetEvalFrameFunc (C function), 177 \_PyObject\_New (C function), 215 \_PyObject\_NewVar (C function), 215 \_PyTuple\_Resize (C function), 135 \_thread module, 174 A abort(), 61 abs built-in function, 88
```

abstract base class, **261** allocfunc (C type), 251 annotation, **261** argument, **261** argv (in module sys), 171 ascii built-in function, 81 asynchronous context manager, **262** asynchronous generator, **262** asynchronous generator iterator, **262** asynchronous iterable, **262** asynchronous iterator, **262** attribute, **262** awaitable, **262**

## B

BDFL, **262** binary file, **262** binaryfunc (C type), 252 borrowed reference, **262** buffer interface (see buffer protocol), 94 buffer object (see buffer protocol), 94 buffer protocol, 94 built-in function import\_\_, 62 abs, 88 ascii, 81 bytes, 81 classmethod, 219 compile, 63 divmod, 88 float, 90 hash, 82, 231 int, 89 len, 82, 90, 92, 136, 139, 141 pow, 88, 89 repr, 81, 231 staticmethod, 219 tuple, 91, 137 type, 82 builtins module, 11, 168, 179 bytearray object, 114

bytecode, **263** bytes built-in function, 81 object, 112 bytes-like object, **262**

## C

callable, **263** callback, **263** calloc(), 205 Capsule object, 157 C-contiguous, 97, 263 class, **263** class variable, **263** classmethod built-in function, 219 cleanup functions, 61 close() (in module os), 179 CO\_FUTURE\_DIVISION (C var), 42 code object, 144 coercion, **263** compile built-in function, 63 complex number, **263** object, 111 context manager, **263** context variable, **263** contiguous, 97, **263** copyright (in module sys), 171 coroutine, **263** coroutine function, **263** CPython, **264**

## D

decorator, **264** descrgetfunc (C type), 251 descriptor, **264** descrsetfunc (C type), 251 destructor (C type), 251 dictionary, **264** object, 137 dictionary comprehension, **264** dictionary view, **264** divmod built-in function, 88 docstring, **264** duck-typing, **264**

## E

EAFP, **264** environment variable PYVENV\_LAUNCHER\_\_, 192, 196 PATH, 11 PYTHON\*, 166 PYTHONCOERCECLOCALE, 201 PYTHONDEBUG, 166, 196 PYTHONDONTWRITEBYTECODE, 166, 199

PYTHONDUMPREFS, 193, 228 PYTHONEXECUTABLE, 196 PYTHONFAULTHANDLER, 193 PYTHONHASHSEED, 166, 194 PYTHONHOME, 11, 166, 172, 194 PYTHONINSPECT, 166, 194 PYTHONIOENCODING, 169, 198 PYTHONLEGACYWINDOWSFSENCODING, 167, 189 PYTHONLEGACYWINDOWSSTDIO, 167, 195 PYTHONMALLOC, 206, 209, 211, 212 PYTHONMALLOCSTATS, 195, 206 PYTHONNOUSERSITE, 167, 198 PYTHONOPTIMIZE, 167, 195 PYTHONPATH, 11, 166, 195 PYTHONPLATLIBDIR, 195 PYTHONPROFILEIMPORTTIME, 194 PYTHONPYCACHEPREFIX, 197 PYTHONTRACEMALLOC, 198 PYTHONUNBUFFERED, 167, 192 PYTHONUTF8, 189, 201 PYTHONVERBOSE, 167, 198 PYTHONWARNINGS, 199 EOFError (built-in exception), 145 exc\_info() (in module sys), 9 executable (in module sys), 170 exit(), 61 expression, **264** extension module, **264**

## F

f-string, **265** file object, 145 file object, **265** file-like object, **265** filesystem encoding and error handler, **265** finder, **265** float built-in function, 90 floating point object, 110 floor division, **265** Fortran contiguous, 97, 263 free(), 205 freefunc (C type), 251 freeze utility, 64 frozenset object, 140 function, **265** object, 142 function annotation, **265**

## G

garbage collection, **266** generator, **266** generator expression, **266**

generator iterator, **266** generic function, **266** generic type, **266** getattrfunc (C type), 251 getattrofunc (C type), 251 getbufferproc (C type), 251 getiterfunc (C type), 251 GIL, **266** global interpreter lock, 172, **266**

## H

hash built-in function, 82, 231 hash-based pyc, **266** hashable, **266** hashfunc (C type), 251

## I

IDLE, **267** immutable, **267** import path, **267** importer, **267** importing, **267** incr\_item(), 10, 11 initproc (C type), 251 inquiry (C type), 256 instancemethod object, 143 int built-in function, 89 integer object, 106 interactive, **267** interpreted, **267** interpreter lock, 172 interpreter shutdown, **267** iterable, **267** iterator, **267** iternextfunc (C type), 251

## K

key function, **267** KeyboardInterrupt (built-in exception), 51 keyword argument, **268**

lambda, **268** LBYL, **268** len built-in function, 82, 90, 92, 136, 139, 141 lenfunc (C type), 251 list, **268** object, 136 list comprehension, **268** loader, **268** locale encoding, **268** lock, interpreter, 172

long integer object, 106 LONG\_MAX, 108

## M

magic method, 268 magic method, **268** main(), 169, 171 malloc(), 205 mapping, **268** object, 137 memoryview object, 155 meta path finder, **268** metaclass, **268** METH\_CLASS (built-in variable), 219 METH\_COEXIST (built-in variable), 219 METH\_FASTCALL (built-in variable), 219 METH\_NOARGS (built-in variable), 219 METH\_O (built-in variable), 219 METH\_STATIC (built-in variable), 219 METH\_VARARGS (built-in variable), 218 method, **268** magic, 268 object, 143 special, 272 method resolution order, **269** MethodType (in module types), 142, 143 module, **269** main\_\_, 11, 168, 179 \_thread, 174 builtins, 11, 168, 179 object, 146 search path, 11, 168, 170 signal, 51 sys, 11, 168, 179 module spec, **269** modules (in module sys), 62, 168 ModuleType (in module types), 146 MRO, **269** mutable, **269**

## N

named tuple, **269** namespace, **269** namespace package, **269** nested scope, **269** new-style class, **269** newfunc (C type), 251 None object, 106 numeric object, 106

object, **269** bytearray, 114

bytes, 112 Capsule, 157 code, 144 complex number, 111 dictionary, 137 file, 145 floating point, 110 frozenset, 140 function, 142 instancemethod, 143 integer, 106 list, 136 long integer, 106 mapping, 137 memoryview, 155 method, 143 module, 146 None, 106 numeric, 106 sequence, 112 set, 140 tuple, 134 type, 6, 103 objobjargproc (C type), 252 objobjproc (C type), 252 OverflowError (built-in exception), 108, 109

## P

package, **269** package variable all\_\_, 62 parameter, **269** PATH, 11 path module search, 11, 168, 170 path (in module sys), 11, 168, 170 path based finder, **270** path entry, **270** path entry finder, **270** path entry hook, **270** path-like object, **270** PEP, **270** platform (in module sys), 171 portion, **270** positional argument, **270** pow built-in function, 88, 89 provisional API, **271** provisional package, **271** Py\_ABS (C macro), 4 Py\_AddPendingCall (C function), 180 Py\_AddPendingCall(), 180 Py\_AtExit (C function), 61 Py\_BEGIN\_ALLOW\_THREADS, 172 Py\_BEGIN\_ALLOW\_THREADS (C macro), 176 Py\_BLOCK\_THREADS (C macro), 176 Py\_buffer (C type), 95 Py\_buffer.buf (C member), 95

Py\_buffer.format (C member), 95 Py\_buffer.internal (C member), 96 Py\_buffer.itemsize (C member), 95 Py\_buffer.len (C member), 95 Py\_buffer.ndim (C member), 95 Py\_buffer.obj (C member), 95 Py\_buffer.readonly (C member), 95 Py\_buffer.shape (C member), 95 Py\_buffer.strides (C member), 96 Py\_buffer.suboffsets (C member), 96 Py\_BuildValue (C function), 72 Py\_BytesMain (C function), 39 Py\_BytesWarningFlag (C var), 166 Py\_CHARMASK (C macro), 5 Py\_CLEAR (C function), 44 Py\_CompileString (C function), 41 Py\_CompileString(), 42 Py\_CompileStringExFlags (C function), 41 Py\_CompileStringFlags (C function), 41 Py\_CompileStringObject (C function), 41 Py\_complex (C type), 111 Py\_DebugFlag (C var), 166 Py\_DecodeLocale (C function), 58 Py\_DECREF (C function), 43 Py\_DecRef (C function), 44 Py\_DECREF(), 6 Py\_DEPRECATED (C macro), 5 Py\_DontWriteBytecodeFlag (C var), 166 Py\_Ellipsis (C var), 155 Py\_EncodeLocale (C function), 59 Py\_END\_ALLOW\_THREADS, 172 Py\_END\_ALLOW\_THREADS (C macro), 176 Py\_EndInterpreter (C function), 179 Py\_EnterRecursiveCall (C function), 54 Py\_eval\_input (C var), 42 Py\_Exit (C function), 61 Py\_False (C var), 110 Py\_FatalError (C function), 61 Py\_FatalError(), 171 Py\_FdIsInteractive (C function), 57 Py\_file\_input (C var), 42 Py\_Finalize (C function), 168 Py\_FinalizeEx (C function), 168 Py\_FinalizeEx(), 61, 168, 179 Py\_FrozenFlag (C var), 166 Py\_GenericAlias (C function), 164 Py\_GenericAliasType (C var), 164 Py\_GetArgcArgv (C function), 203 Py\_GetBuildInfo (C function), 171 Py\_GetCompiler (C function), 171 Py\_GetCopyright (C function), 171 Py\_GETENV (C macro), 5 Py\_GetExecPrefix (C function), 169 Py\_GetExecPrefix(), 11 Py\_GetPath (C function), 170 Py\_GetPath(), 11, 169, 170 Py\_GetPlatform (C function), 170 Py\_GetPrefix (C function), 169

Py\_GetPrefix(), 11 Py\_GetProgramFullPath (C function), 170 Py\_GetProgramFullPath(), 11 Py\_GetProgramName (C function), 169 Py\_GetPythonHome (C function), 172 Py\_GetVersion (C function), 170 Py\_HashRandomizationFlag (C var), 166 Py\_IgnoreEnvironmentFlag (C var), 166 Py\_INCREF (C function), 43 Py\_IncRef (C function), 44 Py\_INCREF(), 6 Py\_Initialize (C function), 168 Py\_Initialize(), 11, 169, 179 Py\_InitializeEx (C function), 168 Py\_InitializeFromConfig (C function), 199 Py\_InspectFlag (C var), 166 Py\_InteractiveFlag (C var), 166 Py\_Is (C function), 216 Py\_IS\_TYPE (C function), 217 Py\_IsFalse (C function), 216 Py\_IsInitialized (C function), 168 Py\_IsInitialized(), 11 Py\_IsNone (C function), 216 Py\_IsolatedFlag (C var), 166 Py\_IsTrue (C function), 216 Py\_LeaveRecursiveCall (C function), 54 Py\_LegacyWindowsFSEncodingFlag (C var), 167 Py\_LegacyWindowsStdioFlag (C var), 167 Py\_LIMITED\_API (C macro), 13 Py\_Main (C function), 39 PY\_MAJOR\_VERSION (C macro), 259 Py\_MAX (C macro), 4 Py\_MEMBER\_SIZE (C macro), 4 PY\_MICRO\_VERSION (C macro), 259 Py\_MIN (C macro), 4 PY\_MINOR\_VERSION (C macro), 259 Py\_mod\_create (C macro), 149 Py\_mod\_create.create\_module (C function), 149 Py\_mod\_exec (C macro), 150 Py\_mod\_exec.exec\_module (C function), 150 Py\_NewInterpreter (C function), 179 Py\_NewRef (C function), 43 Py\_None (C var), 106 Py\_NoSiteFlag (C var), 167 Py\_NotImplemented (C var), 79 Py\_NoUserSiteDirectory (C var), 167 Py\_OptimizeFlag (C var), 167 Py\_PreInitialize (C function), 189 Py\_PreInitializeFromArgs (C function), 189 Py\_PreInitializeFromBytesArgs (C function), 189 Py\_PRINT\_RAW, 146 Py\_QuietFlag (C var), 167 Py\_REFCNT (C function), 217 PY\_RELEASE\_LEVEL (C macro), 259 PY\_RELEASE\_SERIAL (C macro), 259

Py\_ReprEnter (C function), 54 Py\_ReprLeave (C function), 54 Py\_RETURN\_FALSE (C macro), 110 Py\_RETURN\_NONE (C macro), 106 Py\_RETURN\_NOTIMPLEMENTED (C macro), 79 Py\_RETURN\_TRUE (C macro), 110 Py\_RunMain (C function), 202 Py\_SET\_REFCNT (C function), 217 Py\_SET\_SIZE (C function), 217 Py\_SET\_TYPE (C function), 217 Py\_SetPath (C function), 170 Py\_SetPath(), 170 Py\_SetProgramName (C function), 169 Py\_SetProgramName(), 11, 168170 Py\_SetPythonHome (C function), 172 Py\_SetStandardStreamEncoding (C function), 169 Py\_single\_input (C var), 42 Py\_SIZE (C function), 217 Py\_ssize\_t (C type), 9 PY\_SSIZE\_T\_MAX, 108 Py\_STRINGIFY (C macro), 4 Py\_TPFLAGS\_BASE\_EXC\_SUBCLASS (built-in variable), 234 Py\_TPFLAGS\_BASETYPE (built-in variable), 233 Py\_TPFLAGS\_BYTES\_SUBCLASS (built-in variable), 234 Py\_TPFLAGS\_DEFAULT (built-in variable), 234 Py\_TPFLAGS\_DICT\_SUBCLASS (built-in variable), 234 Py\_TPFLAGS\_DISALLOW\_INSTANTIATION (built-in variable), 235 Py\_TPFLAGS\_HAVE\_FINALIZE (built-in variable), 235 Py\_TPFLAGS\_HAVE\_GC (built-in variable), 234 Py\_TPFLAGS\_HAVE\_VECTORCALL (built-in variable), 235 Py\_TPFLAGS\_HEAPTYPE (built-in variable), 233 Py\_TPFLAGS\_IMMUTABLETYPE (built-in variable), 235 Py\_TPFLAGS\_LIST\_SUBCLASS (built-in variable), 234 Py\_TPFLAGS\_LONG\_SUBCLASS (built-in variable), 234 Py\_TPFLAGS\_MAPPING (built-in variable), 235 Py\_TPFLAGS\_METHOD\_DESCRIPTOR (built-in variable), 234 Py\_TPFLAGS\_READY (built-in variable), 233 Py\_TPFLAGS\_READYING (built-in variable), 234 Py\_TPFLAGS\_SEQUENCE (built-in variable), 236 Py\_TPFLAGS\_TUPLE\_SUBCLASS (built-in variable), 234 Py\_TPFLAGS\_TYPE\_SUBCLASS (built-in variable), 234 Py\_TPFLAGS\_UNICODE\_SUBCLASS (built-in variable), 234 Py\_tracefunc (C type), 181 Py\_True (C var), 110

```csv
Py_tss_NEEDS_INIT (C macro), 183
Py_tss_t (C type), 183
Py_TYPE (C function), 216
Py_UCS1 (C type), 116
Py_UCS2 (C type), 116
Py_UCS4 (C type), 116
Py_UNBLOCK_THREADS (C macro), 176
Py_UnbufferedStdioFlag (C var), 167
Py_UNICODE (C type), 116
Py_UNICODE_IS_HIGH_SURROGATE (C macro), 119
Py_UNICODE_IS_LOW_SURROGATE (C macro), 119
Py_UNICODE_IS_SURROGATE (C macro), 119
Py_UNICODE_ISALNUM (C function), 118
Py_UNICODE_ISALPHA (C function), 118
Py_UNICODE_ISDECIMAL (C function), 118
Py_UNICODE_ISDIGIT (C function), 118
Py_UNICODE_ISLINEBREAK (C function), 118
Py_UNICODE_ISLOWER (C function), 118
Py_UNICODE_ISNUMERIC (C function), 118
Py_UNICODE_ISPRINTABLE (C function), 118
Py_UNICODE_ISSPACE (C function), 118
Py_UNICODE_ISTITLE (C function), 118
Py_UNICODE_ISUPPER (C function), 118
Py_UNICODE_JOIN_SURROGATES (C macro), 119
Py_UNICODE_TODECIMAL (C function), 119
Py_UNICODE_TODIGIT (C function), 119
Py_UNICODE_TOLOWER (C function), 118
Py_UNICODE_TONUMERIC (C function), 119
Py_UNICODE_TOTITLE (C function), 119
Py_UNICODE_TOUPPER (C function), 119
Py_UNREACHABLE (C macro), 4
Py_UNUSED (C macro), 5
Py_VaBuildValue (C function), 73
PY_VECTORCALL_ARGUMENTS_OFFSET (C macro), 84
Py_VerboseFlag (C var), 167
PY_VERSION_HEX (C macro), 259
Py_VISIT (C function), 256
Py_XDECREF (C function), 44
Py_XDECREF (), 11
Py_XINCREF (C function), 43
Py_XNewRef (C function), 43
PyAIter_Check (C function), 93
PyAnySet_Check (C function), 140
PyAnySet_CheckExact (C function), 140
PyArg_Parse (C function), 71
PyArg_ParseTuple (C function), 71
PyArg_ParseTupleAndKeywords (C function), 71
PyArg_UnpackTuple (C function), 71
PyArg_ValidateKeywordArguments (C function), 71
PyArg_VaParse (C function), 71
PyArg_VaParseTupleAndKeywords (C function), 71
PyASCIIObject (C type), 116
```

PyBytes\_ConcatAndDel (C function), 114

PyBytes\_FromFormat (C function), 113

PyBytes\_FromFormatV (C function), 113

PyBytes\_FromObject (C function), 113

PyBytes\_FromString (C function), 113

PyBytes\_FromStringAndSize (C function), 113

PyBytes\_GET\_SIZE (C function), 113

PyBytes\_Size (C function), 113

PyBytes\_Type (C var), 112

PyBytesObject (C type), 112

PyCallable\_Check (C function), 87

PyCallIter\_Check (C function), 153

PyCallIter\_New (C function), 153

PyCallIter\_Type (C var), 153

PyCapsule (C type), 157

PyCapsule\_CheckExact (C function), 157

PyCapsule\_Destructor (C type), 157

PyCapsule\_GetContext (C function), 158

PyCapsule\_GetDestructor (C function), 158

PyCapsule\_GetName (C function), 158

PyCapsule\_GetPointer (C function), 157

PyCapsule\_Import (C function), 158

PyCapsule\_IsValid (C function), 158

PyCapsule\_New (C function), 157

PyCapsule\_SetContext (C function), 158

PyCapsule\_SetDestructor (C function), 158

PyCapsule\_SetName (C function), 158

PyCapsule\_SetPointer (C function), 158

PyCell\_Check (C function), 144

PyCell\_GET (C function), 144

PyCell\_Get (C function), 144

PyCell\_New (C function), 144

PyCell\_SET (C function), 144

PyCell\_Set (C function), 144

PyCell\_Type (C var), 144

PyCellObject (C type), 144

PyCFunction (C type), 217

PyCFunctionWithKeywords (C type), 217

PyCMethod (C type), 218

PyCode\_Addr2Line (C function), 145

PyCode\_Check (C function), 144

PyCode\_GetNumFree (C function), 144

PyCode\_New (C function), 144

PyCode\_NewEmpty (C function), 145

PyCode\_NewWithPosOnlyArgs (C function), 144

PyCode\_Type (C var), 144

PyCodec\_BackslashReplaceErrors (C function), 77

PyCodec\_Decode (C function), 76

PyCodec\_Decoder (C function), 76

PyCodec\_Encode (C function), 76

PyCodec\_Encoder (C function), 76

PyCodec\_IgnoreErrors (C function), 77

PyCodec\_IncrementalDecoder (C function), 76

PyCodec\_IncrementalEncoder (C function), 76

PyCodec\_KnownEncoding (C function), 76

PyCodec\_LookupError (C function), 77

PyCodec\_NameReplaceErrors (C function), 77

PyCodec\_Register (C function), 76

PyCodec\_RegisterError (C function), 77

PyCodec\_ReplaceErrors (C function), 77

PyCodec\_StreamReader (C function), 76

PyCodec\_StreamWriter (C function), 77

PyCodec\_StrictErrors (C function), 77

PyCodec\_Unregister (C function), 76

PyCodec\_XMLCharRefReplaceErrors (C func-

tion), 77

PyCodeObject (C type), 144

PyCompactUnicodeObject (C type), 116

PyCompilerFlags (C struct), 42

PyCompilerFlags.cf\_feature\_version (C

member), 42

PyCompilerFlags.cf\_flags (C member), 42

PyComplex\_AsCComplex (C function), 112

PyComplex\_Check (C function), 112

PyComplex\_CheckExact (C function), 112

PyComplex\_FromCComplex (C function), 112

PyComplex\_FromDoubles (C function), 112

PyComplex\_ImagAsDouble (C function), 112

PyComplex\_RealAsDouble (C function), 112

PyComplex\_Type (C var), 112

PyComplexObject (C type), 112

PyConfig (C type), 190

PyConfig.argv (C member), 191

PyConfig.base\_exec\_prefix (C member), 191

PyConfig.base\_executable (C member), 191

PyConfig.base\_prefix (C member), 192

PyConfig.buffered\_stdio (C member), 192

PyConfig.bytes\_warning (C member), 192

PyConfig.check\_hash\_pycs\_mode (C member), 192

PyConfig.configure\_c\_stdio (C member), 192

PyConfig.dev\_mode (C member), 192

PyConfig.dump\_refs (C member), 193

PyConfig.exec\_prefix (C member), 193

PyConfig.executable (C member), 193

PyConfig.faulthandler (C member), 193

PyConfig.filesystem\_encoding (C member),

PyConfig.filesystem\_errors (C member), 193

PyConfig.hash\_seed (C member), 194

PyConfig.home (C member), 194

PyConfig.import\_time (C member), 194

PyConfig.inspect (C member), 194

PyConfig.install\_signal\_handlers (C member), 194

PyConfig.interactive (C member), 194

PyConfig.isolated (C member), 194

PyConfig.legacy\_windows\_stdio (C mem-

PyConfig.malloc\_stats (C member), 195

PyConfig.module\_search\_paths (C member), 195

PyConfig.module\_search\_paths\_set (C member), 195

PyConfig.optimization\_level (C member), 195

PyConfig.orig\_argv (C member), 195

PyConfig.parse\_argv (C member), 196

PyConfig.parser\_debug (C member), 196

PyConfig.pathconfig\_warnings (C member), 196

PyConfig.platlibdir (C member), 195

PyConfig.prefix (C member), 196

PyConfig.program\_name (C member), 196

PyConfig.pycache\_prefix (C member), 196

PyConfig.PyConfig\_Clear (C function), 191

PyConfig.PyConfig\_InitIsolatedConfig (C function), 190

PyConfig.PyConfig\_InitPythonConfig (C function), 190

PyConfig.PyConfig\_Read (C function), 191

PyConfig.PyConfig\_SetArgv (C function), 190

PyConfig.PyConfig\_SetBytesArgv (C function), 190

PyConfig.PyConfig\_SetBytesString (C function), 190

PyConfig.PyConfig\_SetString (C function), 190

PyConfig.PyConfig\_SetWideStringList (C function), 191

PyConfig.pythonpath\_env (C member), 195

PyConfig.quiet (C member), 197

PyConfig.run\_command (C member), 197

PyConfig.run\_filename (C member), 197

PyConfig.run\_module (C member), 197

PyConfig.show\_ref\_count (C member), 197

PyConfig.site\_import (C member), 197

PyConfig.skip\_source\_first\_line (C member), 197

PyConfig.stdio\_encoding (C member), 197

PyConfig.stdio\_errors (C member), 198

PyConfig.tracemalloc (C member), 198

PyConfig.use\_environment (C member), 198

PyConfig.use\_hash\_seed (C member), 194

PyConfig.user\_site\_directory (C member), 198

PyConfig.verbose (C member), 198

PyConfig.warn\_default\_encoding (C member), 192

PyConfig.warnoptions (C member), 198

PyConfig.write\_bytecode (C member), 199

PyConfig.xoptions (C member), 199

PyContext (C type), 160

PyContext\_CheckExact (C function), 160

PyContext\_Copy (C function), 160

PyContext\_CopyCurrent (C function), 160

PyContext\_Enter (C function), 160

PyContext\_Exit (C function), 160

PyContext\_New (C function), 160

PyContext\_Type (C var), 160

PyContextToken (C type), 160

PyContextToken\_CheckExact (C function), 160

PyContextToken\_Type (C var), 160

PyContextVar (C type), 160

PyContextVar\_CheckExact (C function), 160

PyContextVar\_Get (C function), 160

PyContextVar\_New (C function), 160

PyContextVar\_Reset (C function), 161

PyContextVar\_Set (C function), 161

PyContextVar\_Type (C var), 160

PyCoro\_CheckExact (C function), 159

PyCoro\_New (C function), 159

PyCoro\_Type (C var), 159

PyCoroObject (C type), 159

PyDate\_Check (C function), 161

PyDate\_CheckExact (C function), 161

PyDate\_FromDate (C function), 162

PyDate\_FromTimestamp (C function), 163

PyDateTime\_Check (C function), 161

PyDateTime\_CheckExact (C function), 161

PyDateTime\_DATE\_GET\_FOLD (C function), 163

PyDateTime\_DATE\_GET\_HOUR (C function), 162

PyDateTime\_DATE\_GET\_MICROSECOND (C function), 163

PyDateTime\_DATE\_GET\_MINUTE (C function), 162

PyDateTime\_DATE\_GET\_SECOND (C function), 162

PyDateTime\_DATE\_GET\_TZINFO (C function), 163

PyDateTime\_DELTA\_GET\_DAYS (C function), 163

PyDateTime\_DELTA\_GET\_MICROSECONDS (C function), 163

PyDateTime\_DELTA\_GET\_SECONDS (C function), 163

PyDateTime\_FromDateAndTime (C function), 162

PyDateTime\_FromDateAndTimeAndFold (C function), 162

PyDateTime\_FromTimestamp (C function), 163

PyDateTime\_GET\_DAY (C function), 162

PyDateTime\_GET\_MONTH (C function), 162

PyDateTime\_GET\_YEAR (C function), 162

PyDateTime\_TIME\_GET\_FOLD (C function), 163

PyDateTime\_TIME\_GET\_HOUR (C function), 163

PyDateTime\_TIME\_GET\_MICROSECOND (C function), 163

PyDateTime\_TIME\_GET\_MINUTE (C function), 163

PyDateTime\_TIME\_GET\_SECOND (C function), 163

PyDateTime\_TIME\_GET\_TZINFO (C function), 163

PyDateTime\_TimeZone\_UTC (C var), 161

PyDelta\_Check (C function), 161

PyDelta\_CheckExact (C function), 161

PyDelta\_FromDSU (C function), 162

PyDescr\_IsData (C function), 154

PyDescr\_NewClassMethod (C function), 154

PyDescr\_NewGetSet (C function), 154

PyDescr\_NewMember (C function), 154

PyDescr\_NewMethod (C function), 154

PyDescr\_NewWrapper (C function), 154

PyDict\_Check (C function), 137

PyDict\_CheckExact (C function), 137

PyDict\_Clear (C function), 138

PyDict\_Contains (C function), 138

PyDict\_Copy (C function), 138

PyDict\_DelItem (C function), 138

PyDict\_DelItemString (C function), 138

PyDict\_GetItem (C function), 138

PyDict\_GetItemString (C function), 138

PyDict\_GetItemWithError (C function), 138

PyDict\_Items (C function), 139

PyDict\_Keys (C function), 139

PyDict\_Merge (C function), 139

PyDict\_MergeFromSeq2 (C function), 140

PyDict\_New (C function), 138

PyDict\_Next (C function), 139

PyDict\_SetDefault (C function), 138

PyDict\_SetItem (C function), 138

PyDict\_SetItemString (C function), 138

PyDict\_Size (C function), 139

PyDict\_Type (C var), 137

PyDict\_Update (C function), 140

PyDict\_Values (C function), 139

PyDictObject (C type), 137

PyDictProxy\_New (C function), 138

PyDoc\_STR (C macro), 5

PyDoc\_STRVAR (C macro), 5

PyErr\_BadArgument (C function), 46

PyErr\_BadInternalCall (C function), 48

PyErr\_CheckSignals (C function), 51

PyErr\_Clear (C function), 45

PyErr\_Clear(), 9, 11

PyErr\_ExceptionMatches (C function), 49

PyErr\_ExceptionMatches(), 11

PyErr\_Fetch (C function), 49

PyErr\_Format (C function), 46

PyErr\_FormatV (C function), 46

PyErr\_GetExcInfo (C function), 50

PyErr\_GivenExceptionMatches (C function), 49

PyErr\_NewException (C function), 52

PyErr\_NewExceptionWithDoc (C function), 52

PyErr\_NoMemory (C function), 46

PyErr\_NormalizeException (C function), 50

PyErr\_Occurred (C function), 49

PyErr\_Occurred(), 9

PyErr\_Print (C function), 45

PyErr\_PrintEx (C function), 45

PyErr\_ResourceWarning (C function), 49

PyErr\_Restore (C function), 49

PyErr\_SetExcFromWindowsErr (C function), 47

PyErr\_SetExcFromWindowsErrWithFilename (C function), 47

PyErr\_SetExcFromWindowsErrWithFilenameObject (C function), 47

PyErr\_SetExcFromWindowsErrWithFilenameObjects (C function), 47

PyErr\_SetExcInfo (C function), 50

PyErr\_SetFromErrno (C function), 46

PyErr\_SetFromErrnoWithFilename (C function), 47

PyErr\_SetFromErrnoWithFilenameObject (C function), 46

PyErr\_SetFromErrnoWithFilenameObjects (C function), 46

PyErr\_SetFromWindowsErr (C function), 47

PyErr\_SetFromWindowsErrWithFilename (C function), 47

PyErr\_SetImportError (C function), 47

PyErr\_SetImportErrorSubclass (C function), 47

PyErr\_SetInterrupt (C function), 51

PyErr\_SetInterruptEx (C function), 51

PyErr\_SetNone (C function), 46

PyErr\_SetObject (C function), 46

PyErr\_SetString (C function), 46

PyErr\_SetString(), 9

PyErr\_SyntaxLocation (C function), 48

PyErr\_SyntaxLocationEx (C function), 48

PyErr\_SyntaxLocationObject (C function), 48

PyErr\_WarnEx (C function), 48

PyErr\_WarnExplicit (C function), 48

PyErr\_WarnExplicitObject (C function), 48

PyErr\_WarnFormat (C function), 49

PyErr\_WriteUnraisable (C function), 45

PyEval\_AcquireLock (C function), 178

PyEval\_AcquireThread (C function), 178

PyEval\_AcquireThread(), 174

PyEval\_EvalCode (C function), 41

PyEval\_EvalCodeEx (C function), 42

PyEval\_EvalFrame (C function), 42

PyEval\_EvalFrameEx (C function), 42

PyEval\_GetBuiltins (C function), 75

PyEval\_GetFrame (C function), 75

PyEval\_GetFuncDesc (C function), 76

PyEval\_GetFuncName (C function), 75

PyEval\_GetGlobals (C function), 75

PyEval\_GetLocals (C function), 75

PyEval\_InitThreads (C function), 174

PyEval\_InitThreads(), 168

PyEval\_MergeCompilerFlags (C function), 42

PyEval\_ReleaseLock (C function), 178

PyEval\_ReleaseThread (C function), 178

PyEval\_ReleaseThread(), 174

PyEval\_RestoreThread (C function), 175

PyEval\_RestoreThread(), 173, 174

PyEval\_SaveThread (C function), 174

PyEval\_SaveThread(), 173, 174

PyEval\_SetProfile (C function), 181

PyEval\_SetTrace (C function), 182

PyEval\_ThreadsInitialized (C function), 174

PyExc\_ArithmeticError, 55 PyExc\_AssertionError, 55 PyExc\_AttributeError, 55 PyExc\_BaseException, 55 PyExc\_BlockingIOError, 55 PyExc\_BrokenPipeError, 55 PyExc\_BufferError, 55 PyExc\_BytesWarning, 56 PyExc\_ChildProcessError, 55 PyExc\_ConnectionAbortedError, 55 PyExc\_ConnectionError, 55 PyExc\_ConnectionRefusedError, 55 PyExc\_ConnectionResetError, 55 PyExc\_DeprecationWarning, 56 PyExc\_EnvironmentError, 56 PyExc\_EOFError, 55 PyExc\_Exception, 55 PyExc\_FileExistsError, 55 PyExc\_FileNotFoundError, 55 PyExc\_FloatingPointError, 55 PyExc\_FutureWarning, 56 PyExc\_GeneratorExit, 55 PyExc\_ImportError, 55 PyExc\_ImportWarning, 56 PyExc\_IndentationError, 55 PyExc\_IndexError, 55 PyExc\_InterruptedError, 55 PyExc\_IOError, 56 PyExc\_IsADirectoryError, 55 PyExc\_KeyboardInterrupt, 55 PyExc\_KeyError, 55 PyExc\_LookupError, 55 PyExc\_MemoryError, 55 PyExc\_ModuleNotFoundError, 55 PyExc\_NameError, 55 PyExc\_NotADirectoryError, 55 PyExc\_NotImplementedError, 55 PyExc\_OSError, 55 PyExc\_OverflowError, 55 PyExc\_PendingDeprecationWarning, 56 PyExc\_PermissionError, 55 PyExc\_ProcessLookupError, 55 PyExc\_RecursionError, 55 PyExc\_ReferenceError, 55 PyExc\_ResourceWarning, 56 PyExc\_RuntimeError, 55 PyExc\_RuntimeWarning, 56 PyExc\_StopAsyncIteration, 55 PyExc\_StopIteration, 55 PyExc\_SyntaxError, 55 PyExc\_SyntaxWarning, 56 PyExc\_SystemError, 55 PyExc\_SystemExit, 55 PyExc\_TabError, 55 PyExc\_TimeoutError, 55 PyExc\_TypeError, 55 PyExc\_UnboundLocalError, 55 PyExc\_UnicodeDecodeError, 55

PyExc\_UnicodeEncodeError, 55 PyExc\_UnicodeError, 55 PyExc\_UnicodeTranslateError, 55 PyExc\_UnicodeWarning, 56 PyExc\_UserWarning, 56 PyExc\_ValueError, 55 PyExc\_Warning, 56 PyExc\_WindowsError, 56 PyExc\_ZeroDivisionError, 55 PyException\_GetCause (C function), 52 PyException\_GetContext (C function), 52 PyException\_GetTraceback (C function), 52 PyException\_SetCause (C function), 52 PyException\_SetContext (C function), 52 PyException\_SetTraceback (C function), 52 PyFile\_FromFd (C function), 145 PyFile\_GetLine (C function), 145 PyFile\_SetOpenCodeHook (C function), 145 PyFile\_WriteObject (C function), 146 PyFile\_WriteString (C function), 146 PyFloat\_AS\_DOUBLE (C function), 110 PyFloat\_AsDouble (C function), 110 PyFloat\_Check (C function), 110 PyFloat\_CheckExact (C function), 110 PyFloat\_FromDouble (C function), 110 PyFloat\_FromString (C function), 110 PyFloat\_GetInfo (C function), 110 PyFloat\_GetMax (C function), 111 PyFloat\_GetMin (C function), 111 PyFloat\_Type (C var), 110 PyFloatObject (C type), 110 PyFrame\_GetBack (C function), 75 PyFrame\_GetCode (C function), 75 PyFrame\_GetLineNumber (C function), 75 PyFrameObject (C type), 42 PyFrozenSet\_Check (C function), 140 PyFrozenSet\_CheckExact (C function), 141 PyFrozenSet\_New (C function), 141 PyFrozenSet\_Type (C var), 140 PyFunction\_Check (C function), 142 PyFunction\_GetAnnotations (C function), 142 PyFunction\_GetClosure (C function), 142 PyFunction\_GetCode (C function), 142 PyFunction\_GetDefaults (C function), 142 PyFunction\_GetGlobals (C function), 142 PyFunction\_GetModule (C function), 142 PyFunction\_New (C function), 142 PyFunction\_NewWithQualName (C function), 142 PyFunction\_SetAnnotations (C function), 142 PyFunction\_SetClosure (C function), 142 PyFunction\_SetDefaults (C function), 142 PyFunction\_Type (C var), 142 PyFunctionObject (C type), 142 PyGC\_Collect (C function), 256 PyGC\_Disable (C function), 256 PyGC\_Enable (C function), 256 PyGC\_IsEnabled (C function), 256

| PyGen_Check (C function), 159 | PyInterpreterState_Next (C function), 182 |
| --- | --- |
| PyGen_CheckExact (C function), 159 | PyInterpreterState_ThreadHead (C function), 182 |
| PyGen_New (C function), 159 | PyIter_Check (C function), 93 |
| PyGen_NewWithQualName (C function), 159 | PyIter_Next (C function), 93 |
| PyGen_Type (C var), 159 | PyIter_Send (C function), 94 |
| PyGenObject (C type), 159 | PyList_Append (C function), 137 |
| PyGetSetDef (C type), 221 | PyList_AsTuple (C function), 137 |
| PyGILState_Check (C function), 175 | PyList_Check (C function), 136 |
| PyGILState_Ensure (C function), 175 | PyList_CheckExact (C function), 136 |
| PyGILState_GetThisThreadState (C function), 175 | PyList_GET_ITEM (C function), 136 |
| PyGILState_Release (C function), 175 | PyList_GET_SIZE (C function), 136 |
| PyImport_AddModule (C function), 63 | PyList_GetItem (C function), 136 |
| PyImport_AddModuleObject (C function), 62 | PyList_GetItem(), 8 |
| PyImport_AppendInittab (C function), 64 | PyList_GetSlice (C function), 137 |
| PyImport_ExecCodeModule (C function), 63 | PyList_Insert (C function), 137 |
| PyImport_ExecCodeModuleEx (C function), 63 | PyList_New (C function), 136 |
| PyImport_ExecCodeModuleObject (C function), 63 | PyList_Reverse (C function), 137 |
| PyImport_ExecCodeModuleWithPathnames (C function), 63 | PyList_SET_ITEM (C function), 137 |
| PyImport_ExtendInittab (C function), 65 | PyList_SetItem (C function), 137 |
| PyImport_FrozenModules (C var), 64 | PyList_SetItem(), 7 |
| PyImport_GetImporter (C function), 64 | PyList_SetSlice (C function), 137 |
| PyImport_GetMagicNumber (C function), 64 | PyList_Size (C function), 136 |
| PyImport_GetMagicTag (C function), 64 | PyList_Sort (C function), 137 |
| PyImport_GetModule (C function), 64 | PyList_Type (C var), 136 |
| PyImport_GetModuleDict (C function), 64 | PyListObject (C type), 136 |
| PyImport_Import (C function), 62 | PyLong_AsDouble (C function), 109 |
| PyImport_ImportFrozenModule (C function), 64 | PyLong_AsLong (C function), 107 |
| PyImport_ImportFrozenModuleObject (C function), 64 | PyLong_AsLongAndOverflow (C function), 108 |
| PyImport_ImportModuleNoBlock (C function), 62 | PyLong_AsLongLong (C function), 108 |
| PyImport_ReloadModule (C function), 62 | PyLong_AsLongLongAndOverflow (C function), 108 |
| PyIndex_Check (C function), 90 | PyLong_AsSize_t (C function), 108 |
| PyInstanceMethod_Check (C function), 143 | PyLong_AsSsize_t (C function), 108 |
| PyInstanceMethod_Function (C function), 143 | PyLong_AsUnsignedLong (C function), 108 |
| PyInstanceMethod_GET_FUNCTION (C function), 143 | PyLong_AsUnsignedLongLongMask (C function), 109 |
| PyInstanceMethod_New (C function), 143 | PyLong_AsUnsignedLongMask (C function), 109 |
| PyInstanceMethod_Type (C var), 143 | PyLong_AsVoidPtr (C function), 109 |
| PyInterpreterState (C type), 174 | PyLong_Check (C function), 107 |
| PyInterpreterState_Clear (C function), 176 | PyLong_CheckExact (C function), 107 |
| PyInterpreterState_Delete (C function), 176 | PyLong_FromDouble (C function), 107 |
| PyInterpreterState_Get (C function), 177 | PyLong_FromLong (C function), 107 |
| PyInterpreterState_GetDict (C function), 177 | PyLong_FromSize_t (C function), 107 |
| PyInterpreterState_GetID (C function), 177 | PyLong_FromSsize_t (C function), 107 |
| PyInterpreterState_Head (C function), 182 | PyLong_FromString (C function), 107 |
| PyInterpreterState_Main (C function), 182 | PyLong_FromUnicodeObject (C function), 107 |
| PyInterpreterState_New (C function), 176 | PyLong_FromUnsignedLong (C function), 107 |
|  | PyLong_FromUnsignedLongLong (C function), 107 |
|  | PyLong_FromVoidPtr (C function), 107 |
|  | PyLong_Type (C var), 106 |
|  | PyLongObject (C type), 106 |
|  | PyMapping_Check (C function), 92 |
|  | PyMapping_DelItem (C function), 92 |
|  | PyMapping_DelItemString (C function), 92 |

PyMapping\_GetItemString (C function), 92

PyMapping\_HasKey (C function), 92

PyMapping\_HasKeyString (C function), 92

PyMapping\_Items (C function), 93

PyMapping\_Keys (C function), 92

PyMapping\_Length (C function), 92

PyMapping\_SetItemString (C function), 92

PyMapping\_Size (C function), 92

PyMapping\_Values (C function), 93

PyMappingMethods (C type), 248

PyMappingMethods.mp\_ass\_subscript (C member), 248

PyMappingMethods.mp\_length (C member), 248

PyMappingMethods.mp\_subscript (C member), 248

PyMarshal\_ReadLastObjectFromFil e (C function), 66

PyMarshal\_ReadLongFromFile (C function), 65

PyMarshal\_ReadObjectFromFile (C function), 66

PyMarshal\_ReadObjectFromString (C function), 66

PyMarshal\_ReadShortFromFile (C function), 65

PyMarshal\_WriteLongToFile (C function), 65

PyMarshal\_WriteObjectToFile (C function), 65

PyMarshal\_WriteObjectToString (C function), 65

PyMem\_Calloc (C function), 207

PyMem\_Del (C function), 208

PyMem\_Free (C function), 207

PyMem\_GetAllocator (C function), 210

PyMem\_Malloc (C function), 207

PyMem\_New (C function), 208

PyMem\_RawCalloc (C function), 206

PyMem\_RawFree (C function), 207

PyMem\_RawMalloc (C function), 206

PyMem\_RawRealloc (C function), 206

PyMem\_Realloc (C function), 207

PyMem\_Resize (C function), 208

PyMem\_SetAllocator (C function), 210

PyMem\_SetupDebugHooks (C function), 211

PyMemAllocatorDomain (C type), 210

PyMemAllocatorDomain.PYMEM\_DOMAIN\_MEM (C macro), 210

PyMemAllocatorDomain.PYMEM\_DOMAIN\_OBJ (C macro), 210

PyMemAllocatorDomain.PYMEM\_DOMAIN\_RAW (C macro), 210

PyMemAllocatorEx (C type), 210

PyMember\_GetOne (C function), 220

PyMember\_SetOne (C function), 221

PyMemberDef (C type), 220

PyMemoryView\_Check (C function), 156

PyMemoryView\_FromBuffer (C function), 156

PyMemoryView\_FromMemory (C function), 156

PyMemoryView\_FromObject (C function), 156

PyMemoryView\_GET\_BASE (C function), 156

PyMemoryView\_GET\_BUFFER (C function), 156

PyMemoryView\_GetContiguous (C function), 156

PyMethod\_Check (C function), 143

PyMethod\_Function (C function), 143

PyMethod\_GET\_FUNCTION (C function), 143

PyMethod\_GET\_SELF (C function), 143

PyMethod\_New (C function), 143

PyMethod\_Self (C function), 143

PyMethod\_Type (C var), 143

PyMethodDef (C type), 218

PyMethodDef.ml\_doc (C member), 218

PyMethodDef.ml\_flags (C member), 218

PyMethodDef.ml\_meth (C member), 218

PyMethodDef.ml\_name (C member), 218

PyModule\_AddFunctions (C function), 150

PyModule\_AddIntConstant (C function), 152

PyModule\_AddIntMacro (C function), 152

PyModule\_AddObject (C function), 151

PyModule\_AddObjectRef (C function), 151

PyModule\_AddStringConstant (C function), 152

PyModule\_AddStringMacro (C function), 152

PyModule\_AddType (C function), 152

PyModule\_Check (C function), 146

PyModule\_CheckExact (C function), 146

PyModule\_Create (C function), 148

PyModule\_Create2 (C function), 148

PyModule\_ExecDef (C function), 150

PyModule\_FromDefAndSpec (C function), 150

PyModule\_FromDefAndSpec2 (C function), 150

PyModule\_GetDef (C function), 147

PyModule\_GetDict (C function), 146

PyModule\_GetFilename (C function), 147

PyModule\_GetFilenameObject (C function),

147

PyModule\_GetName (C function), 147

PyModule\_GetNameObject (C function), 146

PyModule\_GetState (C function), 147

PyModule\_New (C function), 146

PyModule\_NewObject (C function), 146

PyModule\_SetDocString (C function), 150

PyModule\_Type (C var), 146

PyModuleDef (C type), 147

PyModuleDef\_Init (C function), 149

PyModuleDef\_Slot (C type), 149

PyModuleDef\_Slot.slot (C member), 149

PyModuleDef\_Slot.value (C member), 149

PyModuleDef.m\_base (C member), 147

PyModuleDef.m\_clear (C member), 148

PyModuleDef.m\_doc (C member), 147

PyModuleDef.m\_free (C member), 148

PyModuleDef.m\_methods (C member), 148

PyModuleDef.m\_name (C member), 147

PyModuleDef.m\_size (C member), 147

PyModuleDef.m\_slots (C member), 148

PyModuleDef.m\_slots.m\_reload (C member), 148

PyModuleDef.m\_traverse (C member), 148

PyNumber\_Absolute (C function), 88

PyNumber\_Add (C function), 87

PyNumber\_And (C function), 88

PyNumber\_AsSsize\_t (C function), 90

PyNumber\_Check (C function), 87

PyNumber\_Divmod (C function), 88

PyNumber\_Float (C function), 89

PyNumber\_FloorDivide (C function), 87

PyNumber\_Index (C function), 90

PyNumber\_InPlaceAdd (C function), 88

PyNumber\_InPlaceAnd (C function), 89

PyNumber\_InPlaceFloorDivide (C function), 89

PyNumber\_InPlaceLshift (C function), 89

PyNumber\_InPlaceMatrixMultiply (C function), 89

PyNumber\_InPlaceMultiply (C function), 88

PyNumber\_InPlaceOr (C function), 89

PyNumber\_InPlacePower (C function), 89

PyNumber\_InPlaceRemainder (C function), 89

PyNumber\_InPlaceRshift (C function), 89

PyNumber\_InPlaceSubtract (C function), 88

PyNumber\_InPlaceTrueDivide (C function), 89

PyNumber\_InPlaceXor (C function), 89

PyNumber\_Invert (C function), 88

PyNumber\_Long (C function), 89

PyNumber\_Lshift (C function), 88

PyNumber\_MatrixMultiply (C function), 87

PyNumber\_Multiply (C function), 87

PyNumber\_Negative (C function), 88

PyNumber\_Or (C function), 88

PyNumber\_Positive (C function), 88

PyNumber\_Power (C function), 88

PyNumber\_Remainder (C function), 88

PyNumber\_Rshift (C function), 88

PyNumber\_Subtract (C function), 87

PyNumber\_ToBase (C function), 90

PyNumber\_TrueDivide (C function), 87

PyNumber\_Xor (C function), 88

PyNumberMethods (C type), 246

PyNumberMethods.nb\_absolute (C member), 247

PyNumberMethods.nb\_add (C member), 246

PyNumberMethods.nb\_and (C member), 247

PyNumberMethods.nb\_bool (C member), 247

PyNumberMethods.nb\_divmod (C member), 247

PyNumberMethods.nb\_float (C member), 247

PyNumberMethods.nb\_floor\_divide (C member), 247

PyNumberMethods.nb\_index (C member), 247

PyNumberMethods.nb\_inplace\_add (C member), 247

PyNumberMethods.nb\_inplace\_and (C member), 247

PyNumberMethods.nb\_inplace\_floor\_divide (C member), 247

PyNumberMethods.nb\_inplace\_lshift (C member), 247

PyNumberMethods.nb\_inplace\_matrix\_multiply (C member), 247

PyNumberMethods.nb\_inplace\_multiply (C member), 247

PyNumberMethods.nb\_inplace\_or (C member), 247

PyNumberMethods.nb\_inplace\_power (C member), 247

PyNumberMethods.nb\_inplace\_remainder (C member), 247

PyNumberMethods.nb\_inplace\_rshift (C member), 247

PyNumberMethods.nb\_inplace\_subtract (C member), 247

PyNumberMethods.nb\_inplace\_true\_divide (C member), 247

PyNumberMethods.nb\_inplace\_xor (C member), 247

PyNumberMethods.nb\_int (C member), 247

PyNumberMethods.nb\_invert (C member), 247

PyNumberMethods.nb\_lshift (C member), 247

PyNumberMethods.nb\_matrix\_multiply (C member), 247

PyNumberMethods.nb\_multiply (C member), 247

PyNumberMethods.nb\_negative (C member), 247

PyNumberMethods.nb\_or (C member), 247

PyNumberMethods.nb\_positive (C member), 247

PyNumberMethods.nb\_power (C member), 247

PyNumberMethods.nb\_remainder (C member), 247

PyNumberMethods.nb\_reserved (C member), 247

PyNumberMethods.nb\_rshift (C member), 247

PyNumberMethods.nb\_subtract (C member), 247

PyNumberMethods.nb\_true\_divide (C member), 247

PyNumberMethods.nb\_xor (C member), 247

PyObject (C type), 216

PyObject\_AsCharBuffer (C function), 100

PyObject\_ASCII (C function), 81

PyObject\_AsFileDescriptor (C function), 145

PyObject\_AsReadBuffer (C function), 100

PyObject\_AsWriteBuffer (C function), 101

PyObject\_Bytes (C function), 81

PyObject\_Call (C function), 85

PyObject\_CallFunction (C function), 85

PyObject\_CallFunctionObjArgs (C function), 86

PyObject\_CallMethod (C function), 86

PyObject\_CallMethodNoArgs (C function), 86

PyObject\_CallMethodObjArgs (C function), 86 PyObject\_CallMethodOneArg (C function), 86 PyObject\_CallNoArgs (C function), 85 PyObject\_CallObject (C function), 85 PyObject\_Calloc (C function), 208 PyObject\_CallOneArg (C function), 85 PyObject\_CheckBuffer (C function), 99 PyObject\_CheckReadBuffer (C function), 100 PyObject\_ClearWeakRefs (C function), 157 PyObject\_Del (C function), 215 PyObject\_DelAttr (C function), 80 PyObject\_DelAttrString (C function), 80 PyObject\_DelItem (C function), 82 PyObject\_Dir (C function), 82 PyObject\_Format (C function), 81 PyObject\_Free (C function), 209 PyObject\_GC\_Del (C function), 255 PyObject\_GC\_IsFinalized (C function), 255 PyObject\_GC\_IsTracked (C function), 255 PyObject\_GC\_New (C function), 255 PyObject\_GC\_NewVar (C function), 255 PyObject\_GC\_Resize (C function), 255 PyObject\_GC\_Track (C function), 255 PyObject\_GC\_UnTrack (C function), 255 PyObject\_GenericGetAttr (C function), 79 PyObject\_GenericGetDict (C function), 80 PyObject\_GenericSetAttr (C function), 80 PyObject\_GenericSetDict (C function), 80 PyObject\_GetAIter (C function), 83 PyObject\_GetArenaAllocator (C function), 213 PyObject\_GetAttr (C function), 79 PyObject\_GetAttrString (C function), 79 PyObject\_GetBuffer (C function), 99 PyObject\_GetItem (C function), 82 PyObject\_GetIter (C function), 82 PyObject\_HasAttr (C function), 79 PyObject\_HasAttrString (C function), 79 PyObject\_Hash (C function), 81 PyObject\_HashNotImplemented (C function), 82 PyObject\_HEAD (C macro), 216 PyObject\_HEAD\_INIT (C macro), 217 PyObject\_Init (C function), 215 PyObject\_InitVar (C function), 215 PyObject\_IS\_GC (C function), 255 PyObject\_IsInstance (C function), 81 PyObject\_IsSubclass (C function), 81 PyObject\_IsTrue (C function), 82 PyObject\_Length (C function), 82 PyObject\_LengthHint (C function), 82 PyObject\_Malloc (C function), 208 PyObject\_New (C function), 215 PyObject\_NewVar (C function), 215 PyObject\_Not (C function), 82 PyObject.\_ob\_next (C member), 228 PyObject.\_ob\_prev (C member), 228 PyObject\_Print (C function), 79

PyObject\_Realloc (C function), 209 PyObject\_Repr (C function), 81 PyObject\_RichCompare (C function), 80 PyObject\_RichCompareBool (C function), 80 PyObject\_SetArenaAllocator (C function), 213 PyObject\_SetAttr (C function), 80 PyObject\_SetAttrString (C function), 80 PyObject\_SetItem (C function), 82 PyObject\_Size (C function), 82 PyObject\_Str (C function), 81 PyObject\_Type (C function), 82 PyObject\_TypeCheck (C function), 82 PyObject\_VAR\_HEAD (C macro), 216 PyObject\_Vectorcall (C function), 86 PyObject\_VectorcallDict (C function), 86 PyObject\_VectorcallMethod (C function), 87 PyObjectArenaAllocator (C type), 213 PyObject.ob\_refcnt (C member), 227 PyObject.ob\_type (C member), 227 PyOS\_AfterFork (C function), 58 PyOS\_AfterFork\_Child (C function), 57 PyOS\_AfterFork\_Parent (C function), 57 PyOS\_BeforeFork (C function), 57 PyOS\_CheckStack (C function), 58 PyOS\_double\_to\_string (C function), 74 PyOS\_FSPath (C function), 57 PyOS\_getsig (C function), 58 PyOS\_InputHook (C var), 40 PyOS\_ReadlineFunctionPointer (C var), 40 PyOS\_setsig (C function), 58 PyOS\_snprintf (C function), 74 PyOS\_stricmp (C function), 75 PyOS\_string\_to\_double (C function), 74 PyOS\_strnicmp (C function), 75 PyOS\_vsnprintf (C function), 74 PyPreConfig (C type), 188 PyPreConfig.allocator (C member), 188 PyPreConfig.coerce\_c\_locale (C member), 188 PyPreConfig.coerce\_c\_locale\_warn (C member), 188 PyPreConfig.configure\_locale (C member), 188 PyPreConfig.dev\_mode (C member), 188 PyPreConfig.isolated (C member), 188 PyPreConfig.legacy\_windows\_fs\_encoding (C member), 188 PyPreConfig.parse\_argv (C member), 189 PyPreConfig.PyPreConfig\_InitIsolatedConfi (C function), 188 PyPreConfig.PyPreConfig\_InitPythonConfig (C function), 188 PyPreConfig.use\_environment (C member), 189 PyPreConfig.utf8\_mode (C member), 189 PyProperty\_Type (C var), 154 PyRun\_AnyFile (C function), 39

PyRun\_AnyFileEx (C function), 39

PyRun\_AnyFileExFlags (C function), 39

PyRun\_AnyFileFlags (C function), 39

PyRun\_File (C function), 41

PyRun\_FileEx (C function), 41

PyRun\_FileExFlags (C function), 41

PyRun\_FileFlags (C function), 41

PyRun\_InteractiveLoop (C function), 40

PyRun\_InteractiveLoopFlags (C function), 40

PyRun\_InteractiveOne (C function), 40

PyRun\_InteractiveOneFlags (C function), 40

PyRun\_SimpleFile (C function), 40

PyRun\_SimpleFileEx (C function), 40

PyRun\_SimpleFileExFlags (C function), 40

PyRun\_SimpleString (C function), 39

PyRun\_SimpleStringFlags (C function), 39

PyRun\_String (C function), 40

PyRun\_StringFlags (C function), 41

PySendResult (C type), 93

PySeqIter\_Check (C function), 153

PySeqIter\_New (C function), 153

PySeqIter\_Type (C var), 153

PySequence\_Check (C function), 90

PySequence\_Concat (C function), 90

PySequence\_Contains (C function), 91

PySequence\_Count (C function), 91

PySequence\_DelItem (C function), 91

PySequence\_DelSlice (C function), 91

PySequence\_Fast (C function), 91

PySequence\_Fast\_GET\_ITEM (C function), 91

PySequence\_Fast\_GET\_SIZE (C function), 91

PySequence\_Fast\_ITEMS (C function), 92

PySequence\_GetItem (C function), 90

PySequence\_GetItem(), 8

PySequence\_GetSlice (C function), 91

PySequence\_Index (C function), 91

PySequence\_InPlaceConcat (C function), 90

PySequence\_InPlaceRepeat (C function), 90

PySequence\_ITEM (C function), 92

PySequence\_Length (C function), 90

PySequence\_List (C function), 91

PySequence\_Repeat (C function), 90

PySequence\_SetItem (C function), 91

PySequence\_SetSlice (C function), 91

PySequence\_Size (C function), 90

PySequence\_Tuple (C function), 91

PySequenceMethods (C type), 248

PySequenceMethods.sq\_ass\_item (C member), 248

PySequenceMethods.sq\_concat (C member), 248

PySequenceMethods.sq\_contains (C member), 248

PySequenceMethods.sq\_inplace\_concat (C member), 248

PySequenceMethods.sq\_inplace\_repeat (C member), 249

PySequenceMethods.sq\_item (C member), 248

PySequenceMethods.sq\_length (C member), 248

PySequenceMethods.sq\_repeat (C member), 248

PySet\_Add (C function), 141

PySet\_Check (C function), 140

PySet\_CheckExact (C function), 140

PySet\_Clear (C function), 141

PySet\_Contains (C function), 141

PySet\_Discard (C function), 141

PySet\_GET\_SIZE (C function), 141

PySet\_New (C function), 141

PySet\_Pop (C function), 141

PySet\_Size (C function), 141

PySet\_Type (C var), 140

PySetObject (C type), 140

PySignal\_SetWakeupFd (C function), 51

PySlice\_AdjustIndices (C function), 155

PySlice\_Check (C function), 154

PySlice\_GetIndices (C function), 154

PySlice\_GetIndicesEx (C function), 154

PySlice\_New (C function), 154

PySlice\_Type (C var), 154

PySlice\_Unpack (C function), 155

PyState\_AddModule (C function), 153

PyState\_FindModule (C function), 153

PyState\_RemoveModule (C function), 153

PyStatus (C type), 186

PyStatus.err\_msg (C member), 186

PyStatus.exitcode (C member), 186

PyStatus.func (C member), 186

PyStatus.Py\_ExitStatusException (C function), 187

PyStatus.PyStatus\_Error (C function), 187

PyStatus.PyStatus\_Exception (C function), 187

PyStatus.PyStatus\_Exit (C function), 187

PyStatus.PyStatus\_IsError (C function), 187

PyStatus.PyStatus\_IsExit (C function), 187

PyStatus.PyStatus\_NoMemory (C function), 187

PyStatus.PyStatus\_Ok (C function), 186

PyStructSequence\_Desc (C type), 135

PyStructSequence\_Field (C type), 135

PyStructSequence\_GET\_ITEM (C function), 136

PyStructSequence\_GetItem (C function), 136

PyStructSequence\_InitType (C function), 135

PyStructSequence\_InitType2 (C function), 135

PyStructSequence\_New (C function), 135

PyStructSequence\_NewType (C function), 135

PyStructSequence\_SET\_ITEM (C function), 136

PyStructSequence\_SetItem (C function), 136

PyStructSequence\_UnnamedField (C var), 135

PySys\_AddAuditHook (C function), 60

PySys\_AddWarnOption (C function), 59

PySys\_AddWarnOptionUnicode (C function), 59

| PySys_AddXOption (C function), 60 | PEP 3147, 64 |
| --- | --- |
| PySys_Audit (C function), 60 | PEP 3151, 56 |
| PySys_FormatStderr (C function), 60 | PEP 3155, 271 |
| PySys_FormatStdout (C function), 60 | PYTHON*, 166 |
| PySys_GetObject (C function), 59 | PYTHONCOERCECLOCALE, 201 |
| PySys_GetXOptions (C function), 60 | PYTHONDEBUG, 166, 196 |
| PySys_ResetWarnOptions (C function), 59 | PYTHONDONTWRITEBYTECODE, 166, 199 |
| PySys_SetArgv (C function), 171 | PYTHONDUMPREFS, 193, 228 |
| PySys_SetArgv(), 168 | PYTHONEXECUTABLE, 196 |
| PySys_SetArgvEx (C function), 171 | PYTHONFAULTHANDLER, 193 |
| PySys_SetArgvEx(), 11, 168 | PYTHONHASHSEED, 166, 194 |
| PySys_SetObject (C function), 59 | PYTHONHOME, 11, 166, 172, 194 |
| PySys_SetPath (C function), 60 | Pythonic, 271 |
| PySys_WriteStderr (C function), 60 | PYTHONINSPECT, 166, 194 |
| PySys_WriteStdout (C function), 60 | PYTHONIOENCODING, 169, 198 |
| Python 3000, 271 | PYTHONLEGACYWINDOWSFSENCODING, 167, 189 |
| Python Enhancement Proposals | PYTHONLEGACYWINDOWSSTDIO, 167, 195 |
| PEP 1, 270 | PYTHONMALLOC, 206, 209, 211, 212 |
| PEP 7, 3, 5 | PYTHONMALLOCSTATS, 195, 206 |
| PEP 238, 42, 265 | PYTHONNOUSERSITE, 167, 198 |
| PEP 278, 273 | PYTHONOPTIMIZE, 167, 195 |
| PEP 302, 265, 268 | PYTHONPATH, 11, 166, 195 |
| PEP 343, 263 | PYTHONPLATLIBDIR, 195 |
| PEP 353, 9 | PYTHONPROFILEIMPORTTIME, 194 |
| PEP 362, 262, 270 | PYTHONPYCACHEPREFIX, 197 |
| PEP 383, 123, 124 | PYTHONTRACEMALLOC, 198 |
| PEP 387, 13 | PYTHONUNBUFFERED, 167, 192 |
| PEP 393, 115, 122 | PYTHONUTF8, 189, 201 |
| PEP 411, 271 | PYTHONVERBOSE, 167, 198 |
| PEP 420, 265, 269, 270 | PYTHONWARNINGS, 199 |
| PEP 432, 203 | PyThread_create_key (C function), 184 |
| PEP 442, 245 | PyThread_delete_key (C function), 184 |
| PEP 443, 266 | PyThread_delete_key_value (C function), 184 |
| PEP 451, 149, 265 | PyThread_get_key_value (C function), 184 |
| PEP 483, 266 | PyThread_ReInitTLS (C function), 184 |
| PEP 484, 261, 265, 266, 273 | PyThread_set_key_value (C function), 184 |
| PEP 489, 150 | PyThread_tss_alloc (C function), 183 |
| PEP 492, 262, 263 | PyThread_tss_create (C function), 183 |
| PEP 498, 265 | PyThread_tss_delete (C function), 183 |
| PEP 519, 270 | PyThread_tss_free (C function), 183 |
| PEP 523, 177, 178 | PyThread_tss_get (C function), 184 |
| PEP 525, 262 | PyThread_tss_is_created (C function), 183 |
| PEP 526, 261, 273 | PyThread_tss_set (C function), 183 |
| PEP 528, 167, 195 | PyThreadState, 172 |
| PEP 529, 124, 167 | PyThreadState (C type), 174 |
| PEP 538, 201 | PyThreadState_Clear (C function), 176 |
| PEP 539, 183 | PyThreadState_Delete (C function), 176 |
| PEP 540, 201 | PyThreadState_DeleteCurrent (C function), 176 |
| PEP 552, 192 |  |
| PEP 578, 61 | PyThreadState_Get (C function), 175 |
| PEP 585, 266 | PyThreadState_GetDict (C function), 178 |
| PEP 587, 185 | PyThreadState_GetFrame (C function), 177 |
| PEP 590, 83 | PyThreadState_GetID (C function), 177 |
| PEP 623, 115 | PyThreadState_GetInterpreter (C function), 177 |
| PEP 634, 236 |  |
| PEP 3116, 273 | PyThreadState_New (C function), 176 |
| PEP 3119, 81 | PyThreadState_Next (C function), 182 |
| PEP 3121, 148 | PyThreadState_SetAsyncExc (C function), 178 |

PyThreadState\_Swap (C function), 175

PyTime\_Check (C function), 161

PyTime\_CheckExact (C function), 161

PyTime\_FromTime (C function), 162

PyTime\_FromTimeAndFold (C function), 162

PyTimeZone\_FromOffset (C function), 162

PyTimeZone\_FromOffsetAndName (C function), 162

PyTrace\_C\_CALL (C var), 181

PyTrace\_C\_EXCEPTION (C var), 181

PyTrace\_C\_RETURN (C var), 181

PyTrace\_CALL (C var), 181

PyTrace\_EXCEPTION (C var), 181

PyTrace\_LINE (C var), 181

PyTrace\_OPCODE (C var), 181

PyTrace\_RETURN (C var), 181

PyTraceMalloc\_Track (C function), 213

PyTraceMalloc\_Untrack (C function), 213

PyTuple\_Check (C function), 134

PyTuple\_CheckExact (C function), 134

PyTuple\_GET\_ITEM (C function), 134

PyTuple\_GET\_SIZE (C function), 134

PyTuple\_GetItem (C function), 134

PyTuple\_GetSlice (C function), 134

PyTuple\_New (C function), 134

PyTuple\_Pack (C function), 134

PyTuple\_SET\_ITEM (C function), 134

PyTuple\_SetItem (C function), 134

PyTuple\_SetItem(), 7

PyTuple\_Size (C function), 134

PyTuple\_Type (C var), 134

PyTupleObject (C type), 134

PyType\_Check (C function), 103

PyType\_CheckExact (C function), 103

PyType\_ClearCache (C function), 103

PyType\_FromModuleAndSpec (C function), 105

PyType\_FromSpec (C function), 105

PyType\_FromSpecWithBases (C function), 105

PyType\_GenericAlloc (C function), 104

PyType\_GenericNew (C function), 104

PyType\_GetFlags (C function), 103

PyType\_GetModule (C function), 104

PyType\_GetModuleState (C function), 104

PyType\_GetSlot (C function), 104

PyType\_HasFeature (C function), 103

PyType\_IS\_GC (C function), 104

PyType\_IsSubtype (C function), 104

PyType\_Modified (C function), 103

PyType\_Ready (C function), 104

PyType\_Slot (C type), 105

PyType\_Slot.PyType\_Slot.pfunc (C member), 106

PyType\_Slot.PyType\_Slot.slot (C member), 105

PyType\_Spec (C type), 105

PyType\_Spec.PyType\_Spec.basicsize (C member), 105

PyType\_Spec.PyType\_Spec.flags (C member), 105

PyType\_Spec.PyType\_Spec.itemsize (C member), 105

PyType\_Spec.PyType\_Spec.name (C member), 105

PyType\_Spec.PyType\_Spec.slots (C member), 105

PyType\_Type (C var), 103

PyTypeObject (C type), 103

PyTypeObject.tp\_alloc (C member), 242

PyTypeObject.tp\_as\_async (C member), 230

PyTypeObject.tp\_as\_buffer (C member), 233

PyTypeObject.tp\_as\_mapping (C member), 231

PyTypeObject.tp\_as\_number (C member), 231

PyTypeObject.tp\_as\_sequence (C member), 231

PyTypeObject.tp\_base (C member), 240

PyTypeObject.tp\_bases (C member), 243

PyTypeObject.tp\_basicsize (C member), 228

PyTypeObject.tp\_cache (C member), 244

PyTypeObject.tp\_call (C member), 232

PyTypeObject.tp\_clear (C member), 237

PyTypeObject.tp\_dealloc (C member), 229

PyTypeObject.tp\_del (C member), 244

PyTypeObject.tp\_descr\_get (C member), 240

PyTypeObject.tp\_descr\_set (C member), 241

PyTypeObject.tp\_dict (C member), 240

PyTypeObject.tp\_dictoffset (C member), 241

PyTypeObject.tp\_doc (C member), 236

PyTypeObject.tp\_finalize (C member), 244

PyTypeObject.tp\_flags (C member), 233

PyTypeObject.tp\_free (C member), 243

PyTypeObject.tp\_getattr (C member), 230

PyTypeObject.tp\_getattro (C member), 232

PyTypeObject.tp\_getset (C member), 240

PyTypeObject.tp\_hash (C member), 231

PyTypeObject.tp\_init (C member), 241

PyTypeObject.tp\_is\_gc (C member), 243

PyTypeObject.tp\_itemsize (C member), 228

PyTypeObject.tp\_iter (C member), 239

PyTypeObject.tp\_iternext (C member), 239

PyTypeObject.tp\_members (C member), 239

PyTypeObject.tp\_methods (C member), 239

PyTypeObject.tp\_mro (C member), 243

PyTypeObject.tp\_name (C member), 228

PyTypeObject.tp\_new (C member), 242

PyTypeObject.tp\_repr (C member), 231

PyTypeObject.tp\_richcompare (C member), 238

PyTypeObject.tp\_richcompare.Py\_RETURN\_RICHCOMPARE (C macro), 238

PyTypeObject.tp\_setattr (C member), 230

PyTypeObject.tp\_setattro (C member), 232

PyTypeObject.tp\_str (C member), 232

PyTypeObject.tp\_subclasses (C member), 244

PyTypeObject.tp\_traverse (C member), 236

PyTypeObject.tp\_vectorcall (C member), 245

PyTypeObject.tp\_vectorcall\_offset (C member), 230

PyTypeObject.tp\_version\_tag (C member), 244

PyTypeObject.tp\_weaklist (C member), 244

PyTypeObject.tp\_weaklistoffset (C member), 238

PyTZInfo\_Check (C function), 161

PyTZInfo\_CheckExact (C function), 161

PyUnicode\_1BYTE\_DATA (C function), 116

PyUnicode\_1BYTE\_KIND (C macro), 117

PyUnicode\_2BYTE\_DATA (C function), 116

PyUnicode\_2BYTE\_KIND (C macro), 117

PyUnicode\_4BYTE\_DATA (C function), 116

PyUnicode\_4BYTE\_KIND (C macro), 117

PyUnicode\_AS\_DATA (C function), 117

PyUnicode\_AS\_UNICODE (C function), 117

PyUnicode\_AsASCIIString (C function), 130

PyUnicode\_AsCharmapString (C function), 131

PyUnicode\_AsEncodedString (C function), 126

PyUnicode\_AsLatin1String (C function), 130

PyUnicode\_AsMBCSString (C function), 132

PyUnicode\_AsRawUnicodeEscapeString (C function), 130

PyUnicode\_AsUCS4 (C function), 121

PyUnicode\_AsUCS4Copy (C function), 121

PyUnicode\_AsUnicode (C function), 122

PyUnicode\_AsUnicodeAndSize (C function), 122

PyUnicode\_AsUnicodeEscapeString (C function), 129

PyUnicode\_AsUTF8 (C function), 126

PyUnicode\_AsUTF8AndSize (C function), 126

PyUnicode\_AsUTF8String (C function), 126

PyUnicode\_AsUTF16String (C function), 128

PyUnicode\_AsUTF32String (C function), 127

PyUnicode\_AsWideChar (C function), 125

PyUnicode\_AsWideCharString (C function), 125

PyUnicode\_Check (C function), 116

PyUnicode\_CheckExact (C function), 116

PyUnicode\_Compare (C function), 133

PyUnicode\_CompareWithASCIIString (C function), 133

PyUnicode\_Concat (C function), 132

PyUnicode\_Contains (C function), 133

PyUnicode\_CopyCharacters (C function), 121

PyUnicode\_Count (C function), 133

PyUnicode\_DATA (C function), 117

PyUnicode\_Decode (C function), 126

PyUnicode\_DecodeASCII (C function), 130

PyUnicode\_DecodeCharmap (C function), 131

PyUnicode\_DecodeFSDefault (C function), 124

PyUnicode\_DecodeFSDefaultAndSize (C function), 124

PyUnicode\_DecodeLatin1 (C function), 130

PyUnicode\_DecodeLocale (C function), 123

PyUnicode\_DecodeLocaleAndSize (C function), 123

PyUnicode\_DecodeMBCS (C function), 132

PyUnicode\_DecodeMBCSStateful (C function), 132

PyUnicode\_DecodeRawUnicodeEscape (C function), 130

PyUnicode\_DecodeUnicodeEscape (C function), 129

PyUnicode\_DecodeUTF7 (C function), 129

PyUnicode\_DecodeUTF7Stateful (C function), 129

PyUnicode\_DecodeUTF8 (C function), 126

PyUnicode\_DecodeUTF8Stateful (C function), 126

PyUnicode\_DecodeUTF16 (C function), 128

PyUnicode\_DecodeUTF16Stateful (C function), 128

PyUnicode\_DecodeUTF32 (C function), 127

PyUnicode\_DecodeUTF32Stateful (C function), 127

PyUnicode\_Encode (C function), 126

PyUnicode\_EncodeASCII (C function), 130

PyUnicode\_EncodeCharmap (C function), 131

PyUnicode\_EncodeCodePage (C function), 132

PyUnicode\_EncodeFSDefault (C function), 124

PyUnicode\_EncodeLatin1 (C function), 130

PyUnicode\_EncodeLocale (C function), 123

PyUnicode\_EncodeMBCS (C function), 132

PyUnicode\_EncodeRawUnicodeEscape (C function), 130

PyUnicode\_EncodeUnicodeEscape (C function), 129

PyUnicode\_EncodeUTF7 (C function), 129

PyUnicode\_EncodeUTF8 (C function), 127

PyUnicode\_EncodeUTF16 (C function), 128

PyUnicode\_EncodeUTF32 (C function), 127

PyUnicode\_Fill (C function), 121

PyUnicode\_Find (C function), 133

PyUnicode\_FindChar (C function), 133

PyUnicode\_Format (C function), 133

PyUnicode\_FromEncodedObject (C function), 121

PyUnicode\_FromFormat (C function), 120

PyUnicode\_FromFormatV (C function), 120

PyUnicode\_FromKindAndData (C function), 119

PyUnicode\_FromObject (C function), 122

PyUnicode\_FromString (C function), 120

PyUnicode\_FromString(), 138

PyUnicode\_FromStringAndSize (C function), 119

PyUnicode\_FromUnicode (C function), 122

PyUnicode\_FromWideChar (C function), 125

PyUnicode\_FSConverter (C function), 124

PyUnicode\_FSDecoder (C function), 124

PyUnicode\_GET\_DATA\_SIZE (C function), 117

PyUnicode\_GET\_LENGTH (C function), 116

PyUnicode\_GET\_SIZE (C function), 117

PyUnicode\_GetLength (C function), 121

PyUnicode\_GetSize (C function), 122

PyUnicode\_InternFromString (C function), 134

PyUnicode\_InternInPlace (C function), 133

PyUnicode\_IsIdentifier (C function), 118

PyUnicode\_Join (C function), 132

PyUnicode\_KIND (C function), 117

PyUnicode\_MAX\_CHAR\_VALUE (C macro), 117

PyUnicode\_New (C function), 119

PyUnicode\_READ (C function), 117

PyUnicode\_READ\_CHAR (C function), 117

PyUnicode\_ReadChar (C function), 121

PyUnicode\_READY (C function), 116

PyUnicode\_Replace (C function), 133

PyUnicode\_RichCompare (C function), 133

PyUnicode\_Split (C function), 132

PyUnicode\_Splitlines (C function), 132

PyUnicode\_Substring (C function), 121

PyUnicode\_Tailmatch (C function), 132

PyUnicode\_TransformDecimalToASCII (C function), 122

PyUnicode\_Translate (C function), 131

PyUnicode\_TranslateCharmap (C function), 131

PyUnicode\_Type (C var), 116

PyUnicode\_WCHAR\_KIND (C macro), 117

PyUnicode\_WRITE (C function), 117

PyUnicode\_WriteChar (C function), 121

PyUnicodeDecodeError\_Create (C function), 53

PyUnicodeDecodeError\_GetEncoding (C function), 53

PyUnicodeDecodeError\_GetEnd (C function), 53

PyUnicodeDecodeError\_GetObject (C function), 53

PyUnicodeDecodeError\_GetReason (C function), 54

PyUnicodeDecodeError\_GetStart (C function), 53

PyUnicodeDecodeError\_SetEnd (C function), 53

PyUnicodeDecodeError\_SetReason (C function), 54

PyUnicodeDecodeError\_SetStart (C function), 53

PyUnicodeEncodeError\_Create (C function), 53

PyUnicodeEncodeError\_GetEncoding (C function), 53

PyUnicodeEncodeError\_GetEnd (C function), 53

PyUnicodeEncodeError\_GetObject (C function), 53

PyUnicodeEncodeError\_GetReason (C function), 54

PyUnicodeEncodeError\_GetStart (C function), 53

PyUnicodeEncodeError\_SetEnd (C function), 53

PyUnicodeEncodeError\_SetReason (C function), 54

PyUnicodeEncodeError\_SetStart (C function), 53

PyUnicodeObject (C type), 116

PyUnicodeTranslateError\_Create (C function), 53

PyUnicodeTranslateError\_GetEnd (C function), 53

PyUnicodeTranslateError\_GetObject (C function), 53

PyUnicodeTranslateError\_GetReason (C function), 54

PyUnicodeTranslateError\_GetStart (C function), 53

PyUnicodeTranslateError\_SetEnd (C function), 53

PyUnicodeTranslateError\_SetReason (C function), 54

PyUnicodeTranslateError\_SetStart (C function), 53

PyVarObject (C type), 216

PyVarObject\_HEAD\_INIT (C macro), 217

PyVarObject.ob\_size (C member), 228

PyVectorcall\_Call (C function), 84

PyVectorcall\_Function (C function), 84

PyVectorcall\_NARGS (C function), 84

PyWeakref\_Check (C function), 156

PyWeakref\_CheckProxy (C function), 156

PyWeakref\_CheckRef (C function), 156

PyWeakref\_GET\_OBJECT (C function), 157

PyWeakref\_GetObject (C function), 157

PyWeakref\_NewProxy (C function), 156

PyWeakref\_NewRef (C function), 156

PyWideStringList (C type), 186

PyWideStringList.items (C member), 186

PyWideStringList.length (C member), 186

PyWideStringList.PyWideStringList\_Append (C function), 186

PyWideStringList.PyWideStringList\_Insert (C function), 186

PyWrapper\_New (C function), 154

## Q

qualified name, **271**

## R

realloc(), 205 reference count, **271** regular package, **271**

releasebufferproc (C type), 252 repr built-in function, 81, 231 reprfunc (C type), 251 richcmpfunc (C type), 251

## S

sdterr stdin stdout, 169 search path, module, 11, 168, 170 sendfunc (C type), 252 sequence, **272** object, 112 set object, 140 set comprehension, **272** set\_all(), 8 setattrfunc (C type), 251 setattrofunc (C type), 251 setswitchinterval() (in module sys), 172 SIGINT, 51 signal module, 51 single dispatch, **272** SIZE\_MAX, 109 slice, **272** special method, 272 special method, **272** ssizeargfunc (C type), 252 ssizeobjargproc (C type), 252 statement, **272** staticmethod built-in function, 219 stderr (in module sys), 179 stdin stdout sdterr, 169 stdin (in module sys), 179 stdout sdterr, stdin, 169 stdout (in module sys), 179 strerror(), 46 string PyObject\_Str (C function), 81 strong reference, **272** sum\_list(), 8 sum\_sequence(), 9, 10 sys module, 11, 168, 179 SystemError (built-in exception), 146, 147

## T

ternaryfunc (C type), 252 text encoding, **272** text file, **272** traverseproc (C type), 256 triple-quoted string, **272** tuple built-in function, 91, 137 object, 134 type, **272** built-in function, 82 object, 6, 103 type alias, **272** type hint, **273**

ULONG\_MAX, 108 unaryfunc (C type), 252 universal newlines, **273**

## V

variable annotation, **273** vectorcallfunc (C type), 83 version (in module sys), 170, 171 virtual environment, **273** virtual machine, **273** visitproc (C type), 256

## Z

Zen of Python, **273**
<!-- page: 1 -->

**The Python/C API**

**Release 2.7.18**

**Guido van Rossum**

**and the Python development team**

**May 20, 2020**

**Python Software Foundation Email: docs@python.org**

<!-- page: 2 -->

<!-- page: 3 -->

## CONTENTS

- **1 Introduction** 3
- 1.1 Include Files 3
- 1.2 Objects, Types and Reference Counts 4
- 1.3 Exceptions 7
- 1.4 Embedding Python 9
- 1.5 Debugging Builds 10
- **2 The Very High Level Layer 11**
- **3 Reference Counting 15**
- **4 Exception Handling 17**
- 4.1 Unicode Exception Objects 21
- 4.2 Recursion Control 22
- 4.3 Standard Exceptions 22
- 4.4 Standard Warning Categories 24
- 4.5 String Exceptions 24
- 5 **Utilities 25**
- 5.1 Operating System Utilities 25
- 5.2 System Functions 25
- 5.3 Process Control 26
- 5.4 Importing Modules 27
- 5.5 Data marshalling support 30
- 5.6 Parsing arguments and building values 31
- 5.7 String conversion and formatting 37
- 5.8 Reflection 39
- 5.9 Codec registry and support functions 40
- 6 **Abstract Objects Layer 43**
- 6.1 Object Protocol 43
- 6.2 Number Protocol 47
- 6.3 Sequence Protocol 50
- 6.4 Mapping Protocol 53
- 6.5 Iterator Protocol 54
- 6.6 Old Buffer Protocol 54
- 7 **Concrete Objects Layer 57**
- 7.1 Fundamental Objects 57
- 7.2 Numeric Objects 58
- 7.3 Sequence Objects 65

<!-- page: 4 -->

- 7.4 Mapping Objects 91
- 7.5 Other Objects 94
- **8 Initialization, Finalization, and Threads 111**
- 8.1 Initializing and finalizing the interpreter 111
- 8.2 Process-wide parameters 112
- 8.3 Thread State and the Global Interpreter Lock 114
- 8.4 Sub-interpreter support 119
- 8.5 Asynchronous Notifications 120
- 8.6 Profiling and Tracing 121
- 8.7 Advanced Debugger Support 122
- **9 Memory Management 125**
- 9.1 Overview 125
- 9.2 Memory Interface 126
- 9.3 Object allocators 127
- 9.4 The pymalloc allocator 127
- 9.5 Examples 128
- **10 Object Implementation Support 129**
- 10.1 Allocating Objects on the Heap 129
- 10.2 Common Object Structures 130
- 10.3 Type Objects 134
- 10.4 Number Object Structures 149
- 10.5 Mapping Object Structures 150
- 10.6 Sequence Object Structures 150
- 10.7 Buffer Object Structures 151
- 10.8 Supporting Cyclic Garbage Collection 152
- **A Glossary 155**
- **B About these documents 163**
- B.1 Contributors to the Python Documentation 163
- **C History and License 165**
- C.1 History of the software 165
- C.2 Terms and conditions for accessing or otherwise using Python 166
- C.3 Licenses and Acknowledgements for Incorporated Software 169
- **D Copyright 181**
- **Index 183**

<!-- page: 5 -->

This manual documents the API used by C and C++ programmers who want to write extension modules or embed Python. It is a companion to extending-index, which describes the general principles of extension writing but does not document the API functions in detail.

<!-- page: 6 -->

<!-- page: 7 -->

## INTRODUCTION

The Application Programmer’s Interface to Python gives C and C++ programmers access to the Python interpreter at a variety of levels. The API is equally usable from C++, but for brevity it is generally referred to as the Python/C API. There are two fundamentally different reasons for using the Python/C API. The first reason is to write extension modules for specific purposes; these are C modules that extend the Python interpreter. This is probably the most common use. The second reason is to use Python as a component in a larger application; this technique is generally referred to as embedding Python in an application.

Writing an extension module is a relatively well-understood process, where a “cookbook” approach works well. There are several tools that automate the process to some extent. While people have embedded Python in other applications since its early existence, the process of embedding Python is less straightforward than writing an extension.

Many API functions are useful independent of whether you’re embedding or extending Python; moreover, most applications that embed Python will need to provide a custom extension as well, so it’s probably a good idea to become familiar with writing an extension before attempting to embed Python in a real application.

## 1.1 Include Files

All function, type and macro definitions needed to use the Python/C API are included in your code by the following line:

```c
#include "Python.h"
```

This implies inclusion of the following standard headers: &lt;stdio.h&gt;, &lt;string.h&gt;, &lt;errno.h&gt;, &lt;limits.h&gt;, &lt;assert.h&gt; and &lt;stdlib.h&gt; (if available).

**Note:** Since Python may define some pre-processor definitions which affect the standard headers on some systems, you must include Python.h before any standard headers are included.

All user visible names defined by Python.h (except those defined by the included standard headers) have one of the prefixes Py or \_Py. Names beginning with \_Py are for internal use by the Python implementation and should not be used by extension writers. Structure member names do not have a reserved prefix.

**Important:** user code should never define names that begin with Py or \_Py. This confuses the reader, and jeopardizes the portability of the user code to future Python versions, which may define additional names beginning with one of these prefixes.

The header files are typically installed with Python. On Unix, these are located in the directories prefix/include/ pythonversion/ and exec\_prefix/include/pythonversion/, where prefix and exec\_prefix are defined by the corresponding parameters to Python’s **configure** script and version is sys.version[:3]. On Windows, the headers are installed in prefix/include, where prefix is the installation directory specified to the installer.

<!-- page: 8 -->

To include the headers, place both directories (if different) on your compiler’s search path for includes. Do not place the parent directories on the search path and then use #include &lt;pythonX.Y/Python.h&gt;; this will break on multi-platform builds since the platform independent headers under prefix include the platform specific headers from exec\_prefix.

C++ users should note that though the API is defined entirely using C, the header files do properly declare the entry points to be extern "C", so there is no need to do anything special to use the API from C++.

## 1.2 Objects, Types and Reference Counts

Most Python/C API functions have one or more arguments as well as a return value of type PyObject\*. This type is a pointer to an opaque data type representing an arbitrary Python object. Since all Python object types are treated the same way by the Python language in most situations (e.g., assignments, scope rules, and argument passing), it is only fitting that they should be represented by a single C type. Almost all Python objects live on the heap: you never declare an automatic or static variable of type PyObject, only pointer variables of type PyObject\* can be declared. The sole exception are the type objects; since these must never be deallocated, they are typically static PyTypeObject objects.

All Python objects (even Python integers) have a type and a reference count. An object’s type determines what kind of object it is (e.g., an integer, a list, or a user-defined function; there are many more as explained in types). For each of the well-known types there is a macro to check whether an object is of that type; for instance, PyList\_Check(a) is true if (and only if) the object pointed to by a is a Python list.

## 1.2.1 Reference Counts

The reference count is important because today’s computers have a finite (and often severely limited) memory size; it counts how many different places there are that have a reference to an object. Such a place could be another object, or a global (or static) C variable, or a local variable in some C function. When an object’s reference count becomes zero, the object is deallocated. If it contains references to other objects, their reference count is decremented. Those other objects may be deallocated in turn, if this decrement makes their reference count become zero, and so on. (There’s an obvious problem with objects that reference each other here; for now, the solution is “don’t do that.”)

Reference counts are always manipulated explicitly. The normal way is to use the macro Py\_INCREF() to increment an object’s reference count by one, and Py\_DECREF() to decrement it by one. The Py\_DECREF() macro is considerably more complex than the incref one, since it must check whether the reference count becomes zero and then cause the object’s deallocator to be called. The deallocator is a function pointer contained in the object’s type structure. The typespecific deallocator takes care of decrementing the reference counts for other objects contained in the object if this is a compound object type, such as a list, as well as performing any additional finalization that’s needed. There’s no chance that the reference count can overflow; at least as many bits are used to hold the reference count as there are distinct memory locations in virtual memory (assuming sizeof(Py\_ssize\_t) >= sizeof(void\*)). Thus, the reference count increment is a simple operation.

It is not necessary to increment an object’s reference count for every local variable that contains a pointer to an object. In theory, the object’s reference count goes up by one when the variable is made to point to it and it goes down by one when the variable goes out of scope. However, these two cancel each other out, so at the end the reference count hasn’t changed. The only real reason to use the reference count is to prevent the object from being deallocated as long as our variable is pointing to it. If we know that there is at least one other reference to the object that lives at least as long as our variable, there is no need to increment the reference count temporarily. An important situation where this arises is in objects that are passed as arguments to C functions in an extension module that are called from Python; the call mechanism guarantees to hold a reference to every argument for the duration of the call.

However, a common pitfall is to extract an object from a list and hold on to it for a while without incrementing its reference count. Some other operation might conceivably remove the object from the list, decrementing its reference count and possible deallocating it. The real danger is that innocent-looking operations may invoke arbitrary Python code

<!-- page: 9 -->

which could do this; there is a code path which allows control to flow back to the user from a Py\_DECREF(), so almost any operation is potentially dangerous.

A safe approach is to always use the generic operations (functions whose name begins with PyObject\_, PyNumber\_, PySequence\_ or PyMapping\_). These operations always increment the reference count of the object they return. This leaves the caller with the responsibility to call Py\_DECREF() when they are done with the result; this soon becomes second nature.

## Reference Count Details

The reference count behavior of functions in the Python/C API is best explained in terms of ownership of references. Ownership pertains to references, never to objects (objects are not owned: they are always shared). “Owning a reference” means being responsible for calling Py\_DECREF on it when the reference is no longer needed. Ownership can also be transferred, meaning that the code that receives ownership of the reference then becomes responsible for eventually decref’ing it by calling Py\_DECREF() or Py\_XDECREF() when it’s no longer needed—or passing on this responsibility (usually to its caller). When a function passes ownership of a reference on to its caller, the caller is said to receive a new reference. When no ownership is transferred, the caller is said to borrow the reference. Nothing needs to be done for a borrowed reference.

Conversely, when a calling function passes in a reference to an object, there are two possibilities: the function steals a reference to the object, or it does not. Stealing a reference means that when you pass a reference to a function, that function assumes that it now owns that reference, and you are not responsible for it any longer.

Few functions steal references; the two notable exceptions are PyList\_SetItem() and PyTuple\_SetItem(), which steal a reference to the item (but not to the tuple or list into which the item is put!). These functions were designed to steal a reference because of a common idiom for populating a tuple or list with newly created objects; for example, the code to create the tuple (1, 2, "three") could look like this (forgetting about error handling for the moment; a better way to code this is shown below):

```c
PyObject *t;

t = PyTuple_New(3);
PyTuple_SetItem(t, 0, PyInt_FromLong(1L));
PyTuple_SetItem(t, 1, PyInt_FromLong(2L));
PyTuple_SetItem(t, 2, PyString_FromString("three"));
```

Here, PyInt\_FromLong() returns a new reference which is immediately stolen by PyTuple\_SetItem(). When you want to keep using an object although the reference to it will be stolen, use Py\_INCREF() to grab another reference before calling the reference-stealing function.

Incidentally, PyTuple\_SetItem() is the only way to set tuple items; PySequence\_SetItem() and PyObject\_SetItem() refuse to do this since tuples are an immutable data type. You should only use PyTuple\_SetItem() for tuples that you are creating yourself.

Equivalent code for populating a list can be written using PyList\_New() and PyList\_SetItem().

However, in practice, you will rarely use these ways of creating and populating a tuple or list. There’s a generic function, Py\_BuildValue(), that can create most common objects from C values, directed by a format string. For example, the above two blocks of code could be replaced by the following (which also takes care of the error checking):

```txt
PyObject *tuple, *list;

tuple = Py_BuildValue("(iis)", 1, 2, "three");
list = Py_BuildValue("[iis]", 1, 2, "three");
```

It is much more common to use PyObject\_SetItem() and friends with items whose references you are only borrowing, like arguments that were passed in to the function you are writing. In that case, their behaviour regarding reference

<!-- page: 10 -->

counts is much saner, since you don’t have to increment a reference count so you can give a reference away (“have it be stolen”). For example, this function sets all items of a list (actually, any mutable sequence) to a given item:

```c
int
set_all(PyObject *target, PyObject *item)
{
    int i, n;

    n = PyObject_Length(target);
    if (n < 0)
        return -1;
    for (i = 0; i < n; i++) {
        PyObject *index = PyInt_FromLong(i);
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

The situation is slightly different for function return values. While passing a reference to most functions does not change your ownership responsibilities for that reference, many functions that return a reference to an object give you ownership of the reference. The reason is simple: in many cases, the returned object is created on the fly, and the reference you get is the only reference to the object. Therefore, the generic functions that return object references, like PyObject\_GetItem() and PySequence\_GetItem(), always return a new reference (the caller becomes the owner of the reference).

It is important to realize that whether you own a reference returned by a function depends on which function you call only — the plumage (the type of the object passed as an argument to the function) doesn’t enter into it! Thus, if you extract an item from a list using PyList\_GetItem(), you don’t own the reference — but if you obtain the same item from the same list using PySequence\_GetItem() (which happens to take exactly the same arguments), you do own a reference to the returned object.

Here is an example of how you could write a function that computes the sum of the items in a list of integers; once using PyList\_GetItem(), and once using PySequence\_GetItem().

```c
long
sum_list(PyObject *list)
{
    int i, n;
    long total = 0;
    PyObject *item;

    n = PyList_Size(list);
    if (n < 0)
        return -1; /* Not a list */
    for (i = 0; i < n; i++) {
        item = PyList_GetItem(list, i); /* Can't fail */
        if (!PyInt_Check(item)) continue; /* Skip non-integers */
        total += PyInt_AsLong(item);
    }
    return total;
}
```

<!-- page: 11 -->

```c
long
sum_sequence(PyObject *sequence)
{
    int i, n;
    long total = 0;
    PyObject *item;
    n = PySequence_Length(sequence);
    if (n < 0)
        return -1; /* Has no length */
    for (i = 0; i < n; i++) {
        item = PySequence_GetItem(sequence, i);
        if (item == NULL)
            return -1; /* Not a sequence, or other failure */
        if (PyInt_Check(item))
            total += PyInt_AsLong(item);
        Py_DECREF(item); /* Discard reference ownership */
    }
    return total;
}
```

## 1.2.2 Types

There are few other data types that play a significant role in the Python/C API; most are simple C types such as int, long, double and char\*. A few structure types are used to describe static tables used to list the functions exported by a module or the data attributes of a new object type, and another is used to describe the value of a complex number. These will be discussed together with the functions that use them.

## 1.3 Exceptions

The Python programmer only needs to deal with exceptions if specific error handling is required; unhandled exceptions are automatically propagated to the caller, then to the caller’s caller, and so on, until they reach the top-level interpreter, where they are reported to the user accompanied by a stack traceback.

For C programmers, however, error checking always has to be explicit. All functions in the Python/C API can raise exceptions, unless an explicit claim is made otherwise in a function’s documentation. In general, when a function encounters an error, it sets an exception, discards any object references that it owns, and returns an error indicator. If not documented otherwise, this indicator is either NULL or -1, depending on the function’s return type. A few functions return a Boolean true/false result, with false indicating an error. Very few functions return no explicit error indicator or have an ambiguous return value, and require explicit testing for errors with PyErr\_Occurred(). These exceptions are always explicitly documented.

Exception state is maintained in per-thread storage (this is equivalent to using global storage in an unthreaded application). A thread can be in one of two states: an exception has occurred, or not. The function PyErr\_Occurred() can be used to check for this: it returns a borrowed reference to the exception type object when an exception has occurred, and NULL otherwise. There are a number of functions to set the exception state: PyErr\_SetString() is the most common (though not the most general) function to set the exception state, and PyErr\_Clear() clears the exception state.

The full exception state consists of three objects (all of which can be NULL): the exception type, the corresponding exception value, and the traceback. These have the same meanings as the Python objects sys.exc\_type, sys. exc\_value, and sys.exc\_traceback; however, they are not the same: the Python objects represent the last exception being handled by a Python try … except statement, while the C level exception state only exists while an exception is being passed on between C functions until it reaches the Python bytecode interpreter’s main loop, which takes care of transferring it to sys.exc\_type and friends.

<!-- page: 12 -->

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
        item = PyInt_FromLong(0L);
        if (item == NULL)
            goto error;
    }
    const_one = PyInt_FromLong(1L);
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
```

(continues on next page)

<!-- page: 13 -->

(continued from previous page)

```c
/* Cleanup code, shared by success and failure path */

    /* Use Py_XDECREF() to ignore NULL references */
    Py_XDECREF(item);
    Py_XDECREF(const_one);
    Py_XDECREF(incremented_item);

    return rv; /* -1 for error, 0 for success */
}
```

This example represents an endorsed use of the goto statement in C! It illustrates the use of PyErr\_ExceptionMatches() and PyErr\_Clear() to handle specific exceptions, and the use of Py\_XDECREF() to dispose of owned references that may be NULL (note the 'X' in the name; Py\_DECREF() would crash when confronted with a NULL reference). It is important that the variables used to hold owned references are initialized to NULL for this to work; likewise, the proposed return value is initialized to -1 (failure) and only set to success after the final call made is successful.

## 1.4 Embedding Python

The one important task that only embedders (as opposed to extension writers) of the Python interpreter have to worry about is the initialization, and possibly the finalization, of the Python interpreter. Most functionality of the interpreter can only be used after the interpreter has been initialized.

The basic initialization function is Py\_Initialize(). This initializes the table of loaded modules, and creates the fundamental modules \_\_builtin\_\_, \_\_main\_\_, sys, and exceptions. It also initializes the module search path (sys.path).

Py\_Initialize() does not set the “script argument list” (sys.argv). If this variable is needed by Python code that will be executed later, it must be set explicitly with a call to PySys\_SetArgvEx(argc, argv, updatepath) after the call to Py\_Initialize().

On most systems (in particular, on Unix and Windows, although the details are slightly different), Py\_Initialize() calculates the module search path based upon its best guess for the location of the standard Python interpreter executable, assuming that the Python library is found in a fixed location relative to the Python interpreter executable. In particular, it looks for a directory named lib/pythonX.Y relative to the parent directory where the executable named python is found on the shell command search path (the environment variable PATH).

For instance, if the Python executable is found in /usr/local/bin/python, it will assume that the libraries are in / usr/local/lib/pythonX.Y. (In fact, this particular path is also the “fallback” location, used when no executable file named python is found along PATH.) The user can override this behavior by setting the environment variable PYTHONHOME, or insert additional directories in front of the standard path by setting PYTHONPATH.

The embedding application can steer the search by calling Py\_SetProgramName(file) before calling Py\_Initialize(). Note that PYTHONHOME still overrides this and PYTHONPATH is still inserted in front of the standard path. An application that requires total control has to provide its own implementation of Py\_GetPath() Py\_GetPrefix(), Py\_GetExecPrefix(), and Py\_GetProgramFullPath() (all defined in Modules/ getpath.c).

Sometimes, it is desirable to “uninitialize” Python. For instance, the application may want to start over (make another call to Py\_Initialize()) or the application is simply done with its use of Python and wants to free memory allocated by Python. This can be accomplished by calling Py\_Finalize(). The function Py\_IsInitialized() returns true if Python is currently in the initialized state. More information about these functions is given in a later chapter. Notice that Py\_Finalize() does not free all memory allocated by the Python interpreter, e.g. memory allocated by extension modules currently cannot be released.

<!-- page: 14 -->

## 1.5 Debugging Builds

Python can be built with several macros to enable extra checks of the interpreter and extension modules. These checks tend to add a large amount of overhead to the runtime so they are not enabled by default.

A full list of the various types of debugging builds is in the file Misc/SpecialBuilds.txt in the Python source distribution. Builds are available that support tracing of reference counts, debugging the memory allocator, or low-level profiling of the main interpreter loop. Only the most frequently-used builds will be described in the remainder of this section.

Compiling the interpreter with the Py\_DEBUG macro defined produces what is generally meant by “a debug build” of Python. Py\_DEBUG is enabled in the Unix build by adding --with-pydebug to the ./configure command. It is also implied by the presence of the not-Python-specific \_DEBUG macro. When Py\_DEBUG is enabled in the Unix build, compiler optimization is disabled.

In addition to the reference count debugging described below, the following extra checks are performed:

• Extra checks are added to the object allocator.

• Extra checks are added to the parser and compiler.

• Downcasts from wide types to narrow types are checked for loss of information.

• A number of assertions are added to the dictionary and set implementations. In addition, the set object acquires a test\_c\_api() method.

• Sanity checks of the input arguments are added to frame creation.

• The storage for long ints is initialized with a known invalid pattern to catch reference to uninitialized digits.

• Low-level tracing and extra exception checking are added to the runtime virtual machine.

• Extra checks are added to the memory arena implementation.

• Extra debugging is added to the thread module.

There may be additional checks not mentioned here.

Defining Py\_TRACE\_REFS enables reference tracing. When defined, a circular doubly linked list of active objects is maintained by adding two extra fields to every PyObject. Total allocations are tracked as well. Upon exit, all existing references are printed. (In interactive mode this happens after every statement run by the interpreter.) Implied by Py\_DEBUG.

Please refer to Misc/SpecialBuilds.txt in the Python source distribution for more detailed information.

<!-- page: 15 -->

## THE VERY HIGH LEVEL LAYER

The functions in this chapter will let you execute Python source code given in a file or a buffer, but they will not let you interact in a more detailed way with the interpreter.

Several of these functions accept a start symbol from the grammar as a parameter. The available start symbols are Py\_eval\_input, Py\_file\_input, and Py\_single\_input. These are described following the functions which accept them as parameters.

Note also that several of these functions take FILE\* parameters. One particular issue which needs to be handled carefully is that the FILE structure for different C libraries can be different and incompatible. Under Windows (at least), it is possible for dynamically linked extensions to actually use different libraries, so care should be taken that FILE\* parameters are only passed to these functions if it is certain that they were created by the same library that the Python runtime is using.

## int Py\_Main(int argc, char \*\*argv)

The main program for the standard interpreter. This is made available for programs which embed Python. The argc and argv parameters should be prepared exactly as those which are passed to a C program’s main() function. It is important to note that the argument list may be modified (but the contents of the strings pointed to by the argument list are not). The return value will be 0 if the interpreter exits normally (ie, without an exception), 1 if the interpreter exits due to an exception, or 2 if the parameter list does not represent a valid Python command line.

Note that if an otherwise unhandled SystemExit is raised, this function will not return 1, but exit the process, as long as Py\_InspectFlag is not set.

int **PyRun\_AnyFile**(FILE \*fp, const char \*filename) This is a simplified interface to PyRun\_AnyFileExFlags() below, leaving closeit set to 0 and flags set to NULL.

int **PyRun\_AnyFileFlags**(FILE \*fp, const char \*filename, PyCompilerFlags \*flags) This is a simplified interface to PyRun\_AnyFileExFlags() below, leaving the closeit argument set to 0.

int **PyRun\_AnyFileEx**(FILE \*fp, const char \*filename, int closeit) This is a simplified interface to PyRun\_AnyFileExFlags() below, leaving the flags argument set to NULL.

int **PyRun\_AnyFileExFlags**(FILE \*fp, const char \*filename, int closeit, PyCompilerFlags \*flags) If fp refers to a file associated with an interactive device (console or terminal input or Unix pseudo-terminal), return the value of PyRun\_InteractiveLoop(), otherwise return the result of PyRun\_SimpleFile(). If filename is NULL, this function uses "???" as the filename.

int **PyRun\_SimpleString**(const char \*command) This is a simplified interface to PyRun\_SimpleStringFlags() below, leaving the PyCompilerFlags\* argument set to NULL.

int **PyRun\_SimpleStringFlags**(const char \*command, PyCompilerFlags \*flags) Executes the Python source code from command in the \_\_main\_\_ module according to the flags argument. If \_main\_\_ does not already exist, it is created. Returns 0 on success or -1 if an exception was raised. If there was an error, there is no way to get the exception information. For the meaning of flags, see below.

<!-- page: 16 -->

Note that if an otherwise unhandled SystemExit is raised, this function will not return -1, but exit the process, as long as Py\_InspectFlag is not set.

int PyRun\_SimpleFile(FILE \*fp, const char \*filename) This is a simplified interface to PyRun\_SimpleFileExFlags() below, leaving closeit set to 0 and flags set to NULL.

int PyRun\_SimpleFileFlags(FILE \*fp, const char \*filename, PyCompilerFlags \*flags) This is a simplified interface to PyRun\_SimpleFileExFlags() below, leaving closeit set to 0.

int PyRun\_SimpleFileEx(FILE \*fp, const char \*filename, int closeit) This is a simplified interface to PyRun\_SimpleFileExFlags() below, leaving flags set to NULL.

int PyRun\_SimpleFileExFlags(FILE \*fp, const char \*filename, int closeit, PyCompilerFlags \*flags) Similar to PyRun\_SimpleStringFlags(), but the Python source code is read from fp instead of an in-memory string. filename should be the name of the file. If closeit is true, the file is closed before PyRun\_SimpleFileExFlags returns.

int PyRun\_InteractiveOne(FILE \*fp, const char \*filename) This is a simplified interface to PyRun\_InteractiveOneFlags() below, leaving flags set to NULL.

int PyRun\_InteractiveOneFlags(FILE \*fp, const char \*filename, PyCompilerFlags \*flags) Read and execute a single statement from a file associated with an interactive device according to the flags argument. The user will be prompted using sys.ps1 and sys.ps2. Returns 0 when the input was executed successfully, -1 if there was an exception, or an error code from the errcode.h include file distributed as part of Python if there was a parse error. (Note that errcode.h is not included by Python.h, so must be included specifically if needed.)

int PyRun\_InteractiveLoop(FILE \*fp, const char \*filename) This is a simplified interface to PyRun\_InteractiveLoopFlags() below, leaving flags set to NULL.

int PyRun\_InteractiveLoopFlags(FILE \*fp, const char \*filename, PyCompilerFlags \*flags) Read and execute statements from a file associated with an interactive device until EOF is reached. The user will be prompted using sys.ps1 and sys.ps2. Returns 0 at EOF.

struct \_node\* PyParser\_SimpleParseString(const char \*str, int start) This is a simplified interface to PyParser\_SimpleParseStringFlagsFilename() below, leaving filename set to NULL and flags set to 0.

struct \_node\* PyParser\_SimpleParseStringFlags(const char \*str, int start, int flags) This is a simplified interface to PyParser\_SimpleParseStringFlagsFilename() below, leaving filename set to NULL.

struct \_node\* PyParser\_SimpleParseStringFlagsFilename(const char \*str, const char \*filename, int start, int flags) Parse Python source code from str using the start token start according to the flags argument. The result can be used to create a code object which can be evaluated efficiently. This is useful if a code fragment must be evaluated many times.

struct \_node\* PyParser\_SimpleParseFile(FILE \*fp, const char \*filename, int start) This is a simplified interface to PyParser\_SimpleParseFileFlags() below, leaving flags set to 0.

struct \_node\* PyParser\_SimpleParseFileFlags(FILE \*fp, const char \*filename, int start, int flags) Similar to PyParser\_SimpleParseStringFlagsFilename(), but the Python source code is read from fp instead of an in-memory string.

PyObject\* PyRun\_String(const char \*str, int start, PyObject \*globals, PyObject \*locals) Return value: New reference. This is a simplified interface to PyRun\_StringFlags() below, leaving flags set to NULL.

<!-- page: 17 -->

PyObject\* PyRun\_StringFlags(const char \*str, int start, PyObject \*globals, PyObject \*locals, PyCompiler-Flags \*flags)

Return value: New reference. Execute Python source code from str in the context specified by the dictionaries globals and locals with the compiler flags specified by flags. The parameter start specifies the start token that should be used to parse the source code.

Returns the result of executing the code as a Python object, or NULL if an exception was raised.

PyObject\* PyRun\_File(FILE \*fp, const char \*filename, int start, PyObject \*globals, PyObject \*locals) Return value: New reference. This is a simplified interface to PyRun\_FileExFlags() below, leaving closeit set to 0 and flags set to NULL.

PyObject\* PyRun\_FileEx(FILE \*fp, const char \*filename, int start, PyObject \*globals, PyObject \*locals, int closeit) Return value: New reference. This is a simplified interface to PyRun\_FileExFlags() below, leaving flags set to NULL.

PyObject\* PyRun\_FileFlags(FILE \*fp, const char \*filename, int start, PyObject \*globals, PyObject \*locals, PyCompilerFlags \*flags)

Return value: New reference. This is a simplified interface to PyRun\_FileExFlags() below, leaving closeit set to 0.

PyObject\* PyRun\_FileExFlags(FILE \*fp, const char \*filename, int start, PyObject \*globals, PyObject \*locals, int closeit, PyCompilerFlags \*flags) Return value: New reference. Similar to PyRun\_StringFlags(), but the Python source code is read from fp instead of an in-memory string. filename should be the name of the file. If closeit is true, the file is closed before PyRun\_FileExFlags() returns.

PyObject\* Py\_CompileString(const char \*str, const char \*filename, int start) Return value: New reference. This is a simplified interface to Py\_CompileStringFlags() below, leaving flags set to NULL.

PyObject\* Py\_CompileStringFlags(const char \*str, const char \*filename, int start, PyCompiler-Flags \*flags)

Return value: New reference. Parse and compile the Python source code in str, returning the resulting code object. The start token is given by start; this can be used to constrain the code which can be compiled and should be Py\_eval\_input, Py\_file\_input, or Py\_single\_input. The filename specified by filename is used to construct the code object and may appear in tracebacks or SyntaxError exception messages. This returns NULL if the code cannot be parsed or compiled.

PyObject\* PyEval\_EvalCode(PyCodeObject \*co, PyObject \*globals, PyObject \*locals) Return value: New reference. This is a simplified interface to PyEval\_EvalCodeEx(), with just the code object, and the dictionaries of global and local variables. The other arguments are set to NULL.

PyObject\* PyEval\_EvalCodeEx(PyCodeObject \*co, PyObject \*globals, PyObject \*locals, PyObject \*\*args, int argcount, PyObject \*\*kws, int kwcount, PyObject \*\*defs, int defcount, PyObject \*closure)

PyObject\* PyEval\_EvalFrame(PyFrameObject \*f) Evaluate an execution frame. This is a simplified interface to PyEval\_EvalFrameEx, for backward compatibility.

PyObject\* PyEval\_EvalFrameEx(PyFrameObject \*f, int throwflag) This is the main, unvarnished function of Python interpretation. It is literally 2000 lines long. The code object associated with the execution frame f is executed, interpreting bytecode and executing calls as needed. The additional throwflag parameter can mostly be ignored - if true, then it causes an exception to immediately be thrown; this is used for the throw() methods of generator objects.

int PyEval\_MergeCompilerFlags(PyCompilerFlags \*cf) This function changes the flags of the current evaluation frame, and returns true on success, false on failure.

<!-- page: 18 -->

## int Py\_eval\_input

The start symbol from the Python grammar for isolated expressions; for use with Py\_CompileString().

## int Py\_file\_input

The start symbol from the Python grammar for sequences of statements as read from a file or other source; for use with Py\_CompileString(). This is the symbol to use when compiling arbitrarily long Python source code.

## int Py\_single\_input

The start symbol from the Python grammar for a single statement; for use with Py\_CompileString(). This is the symbol used for the interactive interpreter loop.

## struct PyCompilerFlags

This is the structure used to hold compiler flags. In cases where code is only being compiled, it is passed as int flags, and in cases where code is being executed, it is passed as PyCompilerFlags \*flags. In this case, from \_\_future\_\_ import can modify flags.

Whenever PyCompilerFlags \*flags is NULL, cf\_flags is treated as equal to 0, and any modification due to from \_\_future\_\_ import is discarded.

```solidity
struct PyCompilerFlags {
    int cf_flags;
}
```

## int CO\_FUTURE\_DIVISION

This bit can be set in flags to cause division operator / to be interpreted as “true division” according to [**PEP 238**](https://www.python.org/dev/peps/pep-0238).

<!-- page: 19 -->

## REFERENCE COUNTING

The macros in this section are used for managing reference counts of Python objects.

Increment the reference count for object o. The object must not be NULL; if you aren’t sure that it isn’t NULL, use Py\_XINCREF().

void **Py\_XINCREF**(PyObject \*o) Increment the reference count for object o. The object may be NULL, in which case the macro has no effect.

## void Py\_DECREF(PyObject \*o)

Decrement the reference count for object o. The object must not be NULL; if you aren’t sure that it isn’t NULL, use Py\_XDECREF(). If the reference count reaches zero, the object’s type’s deallocation function (which must not be NULL) is invoked.

**Warning:** The deallocation function can cause arbitrary Python code to be invoked (e.g. when a class instance with a \_\_del\_\_() method is deallocated). While exceptions in such code are not propagated, the executed code has free access to all Python global variables. This means that any object that is reachable from a global variable should be in a consistent state before Py\_DECREF() is invoked. For example, code to delete an object from a list should copy a reference to the deleted object in a temporary variable, update the list data structure, and then call Py\_DECREF() for the temporary variable.

## void Py\_XDECREF(PyObject \*o)

Decrement the reference count for object o. The object may be NULL, in which case the macro has no effect; otherwise the effect is the same as for Py\_DECREF(), and the same warning applies.

## void Py\_CLEAR(PyObject \*o)

Decrement the reference count for object o. The object may be NULL, in which case the macro has no effect; otherwise the effect is the same as for Py\_DECREF(), except that the argument is also set to NULL. The warning for Py\_DECREF() does not apply with respect to the object passed because the macro carefully uses a temporary variable and sets the argument to NULL before decrementing its reference count.

It is a good idea to use this macro whenever decrementing the value of a variable that might be traversed during garbage collection.

## New in version 2.4.

The following functions are for runtime dynamic embedding of Python: Py\_IncRef(PyObject \*o), Py\_DecRef(PyObject \*o). They are simply exported function versions of Py\_XINCREF() and Py\_XDECREF(), respectively.

The following functions or macros are only for use within the interpreter core: \_Py\_Dealloc(), \_Py\_ForgetReference(), \_Py\_NewReference(), as well as the global variable \_Py\_RefTotal.

<!-- page: 20 -->

<!-- page: 21 -->

## EXCEPTION HANDLING

The functions described in this chapter will let you handle and raise Python exceptions. It is important to understand some of the basics of Python exception handling. It works somewhat like the Unix errno variable: there is a global indicator (per thread) of the last error that occurred. Most functions don’t clear this on success, but will set it to indicate the cause of the error on failure. Most functions also return an error indicator, usually NULL if they are supposed to return a pointer, or -1 if they return an integer (exception: the PyArg\_\*() functions return 1 for success and 0 for failure).

When a function must fail because some function it called failed, it generally doesn’t set the error indicator; the function it called already set it. It is responsible for either handling the error and clearing the exception or returning after cleaning up any resources it holds (such as object references or memory allocations); it should not continue normally if it is not prepared to handle the error. If returning due to an error, it is important to indicate to the caller that an error has been set. If the error is not handled or carefully propagated, additional calls into the Python/C API may not behave as intended and may fail in mysterious ways.

The error indicator consists of three Python objects corresponding to the Python variables sys.exc\_type, sys. exc\_value and sys.exc\_traceback. API functions exist to interact with the error indicator in various ways. There is a separate error indicator for each thread.

void **PyErr\_PrintEx**(int set\_sys\_last\_vars)

Print a standard traceback to sys.stderr and clear the error indicator. **Unless** the error is a SystemExit. In that case the no traceback is printed and Python process will exit with the error code specified by the SystemExit instance.

Call this function **only** when the error indicator is set. Otherwise it will cause a fatal error!

If set\_sys\_last\_vars is nonzero, the variables sys.last\_type, sys.last\_value and sys. last\_traceback will be set to the type, value and traceback of the printed exception, respectively.

## void PyErr\_Print()

Alias for PyErr\_PrintEx(1).

## PyObject\* PyErr\_Occurred()

Return value: Borrowed reference. Test whether the error indicator is set. If set, return the exception type (the first argument to the last call to one of the PyErr\_Set\*() functions or to PyErr\_Restore()). If not set, return NULL. You do not own a reference to the return value, so you do not need to Py\_DECREF() it.

**Note:** Do not compare the return value to a specific exception; use PyErr\_ExceptionMatches() instead, shown below. (The comparison could easily fail since the exception may be an instance instead of a class, in the case of a class exception, or it may be a subclass of the expected exception.)

## int PyErr\_ExceptionMatches(PyObject \*exc)

Equivalent to PyErr\_GivenExceptionMatches(PyErr\_Occurred(), exc). This should only be called when an exception is actually set; a memory access violation will occur if no exception has been raised.

<!-- page: 22 -->

| int PyErr_GivenExceptionMatches (PyObject *given, PyObject *exc)Return true if the given exception matches the exception in exc. If exc is a class object, this also returns true when given is an instance of a subclass. If exc is a tuple, all exceptions in the tuple (and recursively in subtuples) are searched for a match. |
| --- |
| void PyErr_NormalizeException (PyObject**exc, PyObject**val, PyObject**tb)Under certain circumstances, the values returned by PyErr_Fetch() below can be “unnormalized”, meaning that *exc is a class object but *val is not an instance of the same class. This function can be used to instantiate the class in that case. If the values are already normalized, nothing happens. The delayed normalization is implemented to improve performance. |
| void PyErr_Clear()Clear the error indicator. If the error indicator is not set, there is no effect. |
| void PyErr_Fetch (PyObject **ptype, PyObject **pvalue, PyObject **ptraceback)Retrieve the error indicator into three variables whose addresses are passed. If the error indicator is not set, set all three variables to NULL. If it is set, it will be cleared and you own a reference to each object retrieved. The value and traceback object may be NULL even when the type object is not. |
| Note: This function is normally only used by code that needs to handle exceptions or by code that needs to save and restore the error indicator temporarily. |
| void PyErr_Restore (PyObject *type, PyObject *value, PyObject *traceback)Set the error indicator from the three objects. If the error indicator is already set, it is cleared first. If the objects are NULL, the error indicator is cleared. Do not pass a NULL type and non-NULL value or traceback. The exception type should be a class. Do not pass an invalid exception type or value. (Violating these rules will cause subtle problems later.) This call takes away a reference to each object: you must own a reference to each object before the call and after the call you no longer own these references. (If you don’t understand this, don’t use this function. I warned you.) |
| Note: This function is normally only used by code that needs to save and restore the error indicator temporarily; use PyErr_Fetch() to save the current exception state. |
| void PyErr_SetString (PyObject *type, const char *message)This is the most common way to set the error indicator. The first argument specifies the exception type; it is normally one of the standard exceptions, e.g. PyExc_RuntimeError. You need not increment its reference count. The second argument is an error message; it is converted to a string object. |
| void PyErr_SetObject (PyObject *type, PyObject *value)This function is similar to PyErr_SetString() but lets you specify an arbitrary Python object for the “value” of the exception. |
| PyObject* PyErr_Format (PyObject *exception, const char *format, ...)Return value: Always NULL. This function sets the error indicator and returns NULL. exception should be a Python exception class. The format and subsequent parameters help format the error message; they have the same meaning and values as in PyString_FromFormat(). |
| void PyErr_SetNone (PyObject *type)This is a shorthand for PyErr_SetObject(type, Py_None). |
| int PyErr_BadArgument()This is a shorthand for PyErr_SetString(PyExc_TypeError, message), where message indicates that a built-in operation was invoked with an illegal argument. It is mostly for internal use. |
| PyObject* PyErr_NoMemory()Return value: Always NULL. This is a shorthand for PyErr_SetNone(PyExc_MemoryError); it returns |

<!-- page: 23 -->

NULL so an object allocation function can write return PyErr\_NoMemory(); when it runs out of memory.

## PyObject\* PyErr\_SetFromErrno(PyObject \*type)

Return value: Always NULL. This is a convenience function to raise an exception when a C library function has returned an error and set the C variable errno. It constructs a tuple object whose first item is the integer errno value and whose second item is the corresponding error message (gotten from strerror()), and then calls PyErr\_SetObject(type, object). On Unix, when the errno value is EINTR, indicating an interrupted system call, this calls PyErr\_CheckSignals(), and if that set the error indicator, leaves it set to that. The function always returns NULL, so a wrapper function around a system call can write return PyErr\_SetFromErrno(type); when the system call returns an error.

## PyObject\* PyErr\_SetFromErrnoWithFilenameObject(PyObject \*type, PyObject \*filenameObject)

Similar to PyErr\_SetFromErrno(), with the additional behavior that if filenameObject is not NULL, it is passed to the constructor of type as a third parameter. In the case of exceptions such as IOError and OSError, this is used to define the filename attribute of the exception instance.

## PyObject\* PyErr\_SetFromErrnoWithFilename(PyObject \*type, const char \*filename)

Return value: Always NULL. Similar to PyErr\_SetFromErrnoWithFilenameObject(), but the filename is given as a C string.

## PyObject\* PyErr\_SetFromWindowsErr(int ierr)

Return value: Always NULL. This is a convenience function to raise WindowsError. If called with ierr of 0, the error code returned by a call to GetLastError() is used instead. It calls the Win32 function FormatMessage() to retrieve the Windows description of error code given by ierr or GetLastError(), then it constructs a tuple object whose first item is the ierr value and whose second item is the corresponding error message (gotten from FormatMessage()), and then calls PyErr\_SetObject(PyExc\_WindowsError, object). This function always returns NULL. Availability: Windows.

## PyObject\* PyErr\_SetExcFromWindowsErr(PyObject \*type, int ierr)

Return value: Always NULL. Similar to PyErr\_SetFromWindowsErr(), with an additional parameter specifying the exception type to be raised. Availability: Windows.

New in version 2.3.

PyObject\* **PyErr\_SetFromWindowsErrWithFilenameObject**(int ierr, PyObject \*filenameObject) Similar to PyErr\_SetFromWindowsErr(), with the additional behavior that if filenameObject is not NULL, it is passed to the constructor of WindowsError as a third parameter. Availability: Windows.

PyObject\* **PyErr\_SetFromWindowsErrWithFilename**(int ierr, const char \*filename) Return value: Always NULL. Similar to PyErr\_SetFromWindowsErrWithFilenameObject(), but the filename is given as a C string. Availability: Windows.

## PyObject\* PyErr\_SetExcFromWindowsErrWithFilenameObject(PyObject \*type, int ierr, PyOb-

Similar to PyErr\_SetFromWindowsErrWithFilenameObject(), with an additional parameter specifying the exception type to be raised. Availability: Windows.

New in version 2.3.

## PyObject\* PyErr\_SetExcFromWindowsErrWithFilename(PyObject \*type, int ierr, const char \*file-

Return value: Always NULL. Similar to PyErr\_SetFromWindowsErrWithFilename(), with an additional parameter specifying the exception type to be raised. Availability: Windows.

New in version 2.3.

void **PyErr\_BadInternalCall**() This is a shorthand for PyErr\_SetString(PyExc\_SystemError, message), where message indicates that an internal operation (e.g. a Python/C API function) was invoked with an illegal argument. It is mostly for internal use.

<!-- page: 24 -->

## int PyErr\_WarnEx(PyObject \*category, char \*message, int stacklevel)

Issue a warning message. The category argument is a warning category (see below) or NULL; the message argument is a message string. stacklevel is a positive number giving a number of stack frames; the warning will be issued from the currently executing line of code in that stack frame. A stacklevel of 1 is the function calling PyErr\_WarnEx(), 2 is the function above that, and so forth.

This function normally prints a warning message to sys.stderr; however, it is also possible that the user has specified that warnings are to be turned into errors, and in that case this will raise an exception. It is also possible that the function raises an exception because of a problem with the warning machinery (the implementation imports the warnings module to do the heavy lifting). The return value is 0 if no exception is raised, or -1 if an exception is raised. (It is not possible to determine whether a warning message is actually printed, nor what the reason is for the exception; this is intentional.) If an exception is raised, the caller should do its normal exception handling (for example, Py\_DECREF() owned references and return an error value).

Warning categories must be subclasses of PyExc\_Warning; PyExc\_Warning is a subclass of PyExc\_Exception; the default warning category is PyExc\_RuntimeWarning. The standard Python warning categories are available as global variables whose names are enumerated at Standard Warning Categories.

For information about warning control, see the documentation for the warnings module and the -W option in the command line documentation. There is no C API for warning control.

## int PyErr\_Warn(PyObject \*category, char \*message)

Issue a warning message. The category argument is a warning category (see below) or NULL; the message argument is a message string. The warning will appear to be issued from the function calling PyErr\_Warn(), equivalent to calling PyErr\_WarnEx() with a stacklevel of 1.

Deprecated; use PyErr\_WarnEx() instead.

## int PyErr\_WarnExplicit(PyObject \*category, const char \*message, const char \*filename, int lineno, const char \*module, PyObject \*registry)

Issue a warning message with explicit control over all warning attributes. This is a straightforward wrapper around the Python function warnings.warn\_explicit(), see there for more information. The module and registry arguments may be set to NULL to get the default effect described there.

## int PyErr\_WarnPy3k(char \*message, int stacklevel)

Issue a DeprecationWarning with the given message and stacklevel if the Py\_Py3kWarningFlag flag is enabled.

New in version 2.6.

## int PyErr\_CheckSignals()

This function interacts with Python’s signal handling. It checks whether a signal has been sent to the processes and if so, invokes the corresponding signal handler. If the signal module is supported, this can invoke a signal handler written in Python. In all cases, the default effect for SIGINT is to raise the KeyboardInterrupt exception. If an exception is raised the error indicator is set and the function returns -1; otherwise the function returns 0. The error indicator may or may not be cleared if it was previously set.

## void PyErr\_SetInterrupt()

This function simulates the effect of a SIGINT signal arriving — the next time PyErr\_CheckSignals() is called, KeyboardInterrupt will be raised. It may be called without holding the interpreter lock.

## int PySignal\_SetWakeupFd(int fd)

This utility function specifies a file descriptor to which a '\0' byte will be written whenever a signal is received. It returns the previous such file descriptor. The value -1 disables the feature; this is the initial state. This is equivalent to signal.set\_wakeup\_fd() in Python, but without any error checking. fd should be a valid file descriptor. The function should only be called from the main thread.

New in version 2.6.

## PyObject\* PyErr\_NewException(char \*name, PyObject \*base, PyObject \*dict)

Return value: New reference. This utility function creates and returns a new exception class. The name argu-

<!-- page: 25 -->

```c
int PyUnicodeDecodeError_GetStart (PyObject *exc, Py_ssize_t *start)
```

```txt
Py_ssize_t length, Py_ssize_t start, Py_ssize_t end, const char *reason)
```

ment must be the name of the new exception, a C string of the form module.classname. The base and dict arguments are normally NULL. This creates a class object derived from Exception (accessible in C as PyExc\_Exception).

The \_\_module\_\_ attribute of the new class is set to the first part (up to the last dot) of the name argument, and the class name is set to the last part (after the last dot). The base argument can be used to specify alternate base classes; it can either be only one class or a tuple of classes. The dict argument can be used to specify a dictionary of class variables and methods.

PyObject\* **PyErr\_NewExceptionWithDoc**(char \*name, char \*doc, PyObject \*base, PyObject \*dict)

Return value: New reference. Same as PyErr\_NewException(), except that the new exception class can easily be given a docstring: If doc is non-NULL, it will be used as the docstring for the exception class.

New in version 2.7.

## void PyErr\_WriteUnraisable(PyObject \*obj)

This utility function prints a warning message to sys.stderr when an exception has been set but it is impossible for the interpreter to actually raise the exception. It is used, for example, when an exception occurs in an del\_\_() method.

The function is called with a single argument obj that identifies the context in which the unraisable exception occurred. If possible, the repr of obj will be printed in the warning message.

## 4.1 Unicode Exception Objects

The following functions are used to create and modify Unicode exceptions from C.

PyObject\* **PyUnicodeDecodeError\_Create**(const char \*encoding, const char \*object, Py\_ssize\_t length,

Py\_ssize\_t start, Py\_ssize\_t end, const char \*reason)

```txt
Create a UnicodeDecodeError object with the attributes encoding, object, length, start, end and reason.
```

```txt
PyObject* PyUnicodeEncodeError_Create (const char *encoding, const Py_UNICODE *object,
```

Create a UnicodeEncodeError object with the attributes encoding, object, length, start, end and reason.

```txt
PyObject* PyUnicodeTranslateError_Create (const Py_UNICODE *object, Py_ssize_t length,
```

Py\_ssize\_t start, Py\_ssize\_t end, const char \*reason)

```txt
Create a UnicodeTranslateError object with the attributes object, length, start, end and reason.
```

PyObject\* **PyUnicodeDecodeError\_GetEncoding**(PyObject \*exc)

```txt
PyObject* PyUnicodeEncodeError_GetEncoding (PyObject *exc)
```

Return the encoding attribute of the given exception object.

```vba
PyObject* PyUnicodeDecodeError_GetObject(PyObject *exc)
```

```txt
PyObject* PyUnicodeEncodeError_GetObject(PyObject *exc)
```

```txt
PyObject* PyUnicodeTranslateError_GetObject(PyObject *exc)
```

Return the object attribute of the given exception object.

```c
int PyUnicodeEncodeError_GetStart (PyObject *exc, Py_ssize_t *start)
```

```txt
int PyUnicodeTranslateError_GetStart (PyObject *exc, Py_ssize_t *start)
```

Get the start attribute of the given exception object and place it into \*start. start must not be NULL. Return 0 on success, -1 on failure.

```txt
int PyUnicodeDecodeError_SetStart (PyObject *exc, Py_ssize_t start)
```

```txt
int PyUnicodeEncodeError_SetStart (PyObject *exc, Py_ssize_t start)
```

```txt
int PyUnicodeTranslateError_SetStart (PyObject *exc, Py_ssize_t start)
```

Set the start attribute of the given exception object to start. Return 0 on success, -1 on failure.

<!-- page: 26 -->

```verilog
int PyUnicodeDecodeError_GetEnd (PyObject *exc, Py_ssize_t *end)
int PyUnicodeEncodeError_GetEnd (PyObject *exc, Py_ssize_t *end)
int PyUnicodeTranslateError_GetEnd (PyObject *exc, Py_ssize_t *end)
    Get the end attribute of the given exception object and place it into *end. end must not be NULL. Return 0 on success, -1 on failure.
int PyUnicodeDecodeError_SetEnd (PyObject *exc, Py_ssize_t end)
int PyUnicodeEncodeError_SetEnd (PyObject *exc, Py_ssize_t end)
int PyUnicodeTranslateError_SetEnd (PyObject *exc, Py_ssize_t end)
    Set the end attribute of the given exception object to end. Return 0 on success, -1 on failure.
PyObject* PyUnicodeDecodeError_GetReason (PyObject *exc)
PyObject* PyUnicodeEncodeError_GetReason (PyObject *exc)
PyObject* PyUnicodeTranslateError_GetReason (PyObject *exc)
    Return the reason attribute of the given exception object.
int PyUnicodeDecodeError_SetReason (PyObject *exc, const char *reason)
int PyUnicodeEncodeError_SetReason (PyObject *exc, const char *reason)
int PyUnicodeTranslateError_SetReason (PyObject *exc, const char *reason)
    Set the reason attribute of the given exception object to reason. Return 0 on success, -1 on failure.
```

## 4.2 Recursion Control

These two functions provide a way to perform safe recursive calls at the C level, both in the core and in extension modules. They are needed if the recursive code does not necessarily invoke Python code (which tracks its recursion depth automatically).

## int Py\_EnterRecursiveCall(const char \*where)

Marks a point where a recursive C-level call is about to be performed.

If USE\_STACKCHECK is defined, this function checks if the OS stack overflowed using PyOS\_CheckStack(). In this is the case, it sets a MemoryError and returns a nonzero value.

The function then checks if the recursion limit is reached. If this is the case, a RuntimeError is set and a nonzero value is returned. Otherwise, zero is returned.

where should be a string such as " in instance check" to be concatenated to the RuntimeError message caused by the recursion depth limit.

## void Py\_LeaveRecursiveCall()

Ends a Py\_EnterRecursiveCall(). Must be called once for each successful invocation of Py\_EnterRecursiveCall().

## 4.3 Standard Exceptions

All standard Python exceptions are available as global variables whose names are PyExc\_ followed by the Python exception name. These have the type PyObject\*; they are all class objects. For completeness, here are all the variables:

| C Name | Python Name | Notes |
| --- | --- | --- |
| PyExc_BaseException | BaseException | (1), (4) |
| PyExc_Exception | Exception | (1) |
| PyExc_StandardError | StandardError | (1) |
| PyExc_ArithmeticError | ArithmeticError | (1) |

Continued on next page

<!-- page: 27 -->

Table 1 – continued from previous page

| C Name | Python Name | Notes |
| --- | --- | --- |
| PyExc_AssertionError | AssertionError |  |
| PyExc_AttributeError | AttributeError |  |
| PyExc_BufferError | BufferError |  |
| PyExc_EnvironmentError | EnvironmentError | (1) |
| PyExc_EOFError | EOFError |  |
| PyExc_FloatingPointError | FloatingPointError |  |
| PyExc_GeneratorExit | GeneratorExit |  |
| PyExc_ImportError | ImportError |  |
| PyExc_IndentationError | IndentationError |  |
| PyExc_IndexError | IndexError |  |
| PyExc_IOError | IOError |  |
| PyExc_KeyError | KeyError |  |
| PyExc_KeyboardInterrupt | KeyboardInterrupt |  |
| PyExc_LookupError | LookupError | (1) |
| PyExc_MemoryError | MemoryError |  |
| PyExc_NameError | NameError |  |
| PyExc_NotImplementedError | NotImplementedError |  |
| PyExc_OSError | OSError |  |
| PyExc_OverflowError | OverflowError |  |
| PyExc_ReferenceError | ReferenceError | (2) |
| PyExc_RuntimeError | RuntimeError |  |
| PyExc_StopIteration | StopIteration |  |
| PyExc_SyntaxError | SyntaxError |  |
| PyExc_SystemError | SystemError |  |
| PyExc_SystemExit | SystemExit |  |
| PyExc_TabError | TabError |  |
| PyExc_TypeError | TypeError |  |
| PyExc_UnboundLocalError | UnboundLocalError |  |
| PyExc_UnicodeDecodeError | UnicodeDecodeError |  |
| PyExc_UnicodeEncodeError | UnicodeEncodeError |  |
| PyExc_UnicodeError | UnicodeError |  |
| PyExc_UnicodeTranslateError | UnicodeTranslateError |  |
| PyExc_VMSError | VMSError | (5) |
| PyExc_ValueError | ValueError |  |
| PyExc_WindowsError | WindowsError | (3) |
| PyExc_ZeroDivisionError | ZeroDivisionError |  |

Notes:

(1) This is a base class for other standard exceptions.

(2) This is the same as weakref.ReferenceError.

(3) Only defined on Windows; protect code that uses this by testing that the preprocessor macro MS\_WINDOWS is defined.

(4) New in version 2.5.

(5) Only defined on VMS; protect code that uses this by testing that the preprocessor macro \_\_VMS is defined.

<!-- page: 28 -->

## 4.4 Standard Warning Categories

All standard Python warning categories are available as global variables whose names are PyExc\_ followed by the Python exception name. These have the type PyObject\*; they are all class objects. For completeness, here are all the variables:

| C Name | Python Name | Notes |
| --- | --- | --- |
| PyExc_Warning | Warning | (1) |
| PyExc_BytesWarning | BytesWarning |  |
| PyExc_DeprecationWarning | DeprecationWarning |  |
| PyExc_FutureWarning | FutureWarning |  |
| PyExc_ImportWarning | ImportWarning |  |
| PyExc_PendingDeprecationWarning | PendingDeprecationWarning |  |
| PyExc_RuntimeWarning | RuntimeWarning |  |
| PyExc_SyntaxWarning | SyntaxWarning |  |
| PyExc_UnicodeWarning | UnicodeWarning |  |
| PyExc_UserWarning | UserWarning |  |

Notes:

(1) This is a base class for other standard warning categories.

## 4.5 String Exceptions

Changed in version 2.6: All exceptions to be raised or caught must be derived from BaseException. Trying to raise a string exception now raises TypeError.

<!-- page: 29 -->

# UTILITIES

The functions in this chapter perform various utility tasks, ranging from helping C code be more portable across platforms, using Python modules from C, and parsing function arguments and constructing Python values from C values.

## 5.1 Operating System Utilities

## int Py\_FdIsInteractive(FILE \*fp, const char \*filename)

Return true (nonzero) if the standard I/O file fp with name filename is deemed interactive. This is the case for files for which isatty(fileno(fp)) is true. If the global flag Py\_InteractiveFlag is true, this function also returns true if the filename pointer is NULL or if the name is equal to one of the strings '&lt;stdin&gt;' or '???'.

## void PyOS\_AfterFork()

Function to update some internal state after a process fork; this should be called in the new process if the Python interpreter will continue to be used. If a new executable is loaded into the new process, this function does not need to be called.

## int PyOS\_CheckStack()

Return true when the interpreter runs out of stack space. This is a reliable check, but is only available when USE\_STACKCHECK is defined (currently on Windows using the Microsoft Visual C++ compiler). USE\_STACKCHECK will be defined automatically; you should never change the definition in your own code.

## PyOS\_sighandler\_t PyOS\_getsig(int i)

Return the current signal handler for signal i. This is a thin wrapper around either sigaction() or signal(). Do not call those functions directly! PyOS\_sighandler\_t is a typedef alias for void (\*)(int).

## PyOS\_sighandler\_t PyOS\_setsig(int i, PyOS\_sighandler\_t h)

Set the signal handler for signal i to be h; return the old signal handler. This is a thin wrapper around either sigaction() or signal(). Do not call those functions directly! PyOS\_sighandler\_t is a typedef alias for void (\*)(int).

## 5.2 System Functions

These are utility functions that make functionality from the sys module accessible to C code. They all work with the current interpreter thread’s sys module’s dict, which is contained in the internal thread state structure.

## PyObject \*PySys\_GetObject(char \*name)

Return value: Borrowed reference. Return the object name from the sys module or NULL if it does not exist, without setting an exception.

<!-- page: 30 -->

FILE \***PySys\_GetFile**(char \*name, FILE \*def) Return the FILE\* associated with the object name in the sys module, or def if name is not in the module or is not associated with a FILE\*.

int **PySys\_SetObject**(char \*name, PyObject \*v) Set name in the sys module to v unless v is NULL, in which case name is deleted from the sys module. Returns 0 on success, -1 on error.

void **PySys\_ResetWarnOptions**() Reset sys.warnoptions to an empty list.

void **PySys\_AddWarnOption**(char \*s) Append s to sys.warnoptions.

## void PySys\_SetPath(char \*path)

Set sys.path to a list object of paths found in path which should be a list of paths separated with the platform’s search path delimiter (: on Unix, ; on Windows).

## void PySys\_WriteStdout(const char \*format, ...)

Write the output string described by format to sys.stdout. No exceptions are raised, even if truncation occurs (see below).

format should limit the total size of the formatted output string to 1000 bytes or less – after 1000 bytes, the output string is truncated. In particular, this means that no unrestricted “%s” formats should occur; these should be limited using “%.&lt;N&gt;s” where &lt;N&gt; is a decimal number calculated so that &lt;N&gt; plus the maximum size of other formatted text does not exceed 1000 bytes. Also watch out for “%f”, which can print hundreds of digits for very large numbers.

If a problem occurs, or sys.stdout is unset, the formatted message is written to the real (C level) stdout.

void **PySys\_WriteStderr**(const char \*format, ...)

As above, but write to sys.stderr or stderr instead.

## 5.3 Process Control

## void Py\_FatalError(const char \*message)

Print a fatal error message and kill the process. No cleanup is performed. This function should only be invoked when a condition is detected that would make it dangerous to continue using the Python interpreter; e.g., when the object administration appears to be corrupted. On Unix, the standard C library function abort() is called which will attempt to produce a core file.

## void Py\_Exit(int status)

Exit the current process. This calls Py\_Finalize() and then calls the standard C library function exit(status).

## int Py\_AtExit(void (\*func)())

Register a cleanup function to be called by Py\_Finalize(). The cleanup function will be called with no arguments and should return no value. At most 32 cleanup functions can be registered. When the registration is successful, Py\_AtExit() returns 0; on failure, it returns -1. The cleanup function registered last is called first. Each cleanup function will be called at most once. Since Python’s internal finalization will have completed before the cleanup function, no Python APIs should be called by func.

<!-- page: 31 -->

## 5.4 Importing Modules

PyObject\* **PyImport\_ImportModule**(const char \*name)

Return value: New reference. This is a simplified interface to PyImport\_ImportModuleEx() below, leaving the globals and locals arguments set to NULL and level set to 0. When the name argument contains a dot (when it specifies a submodule of a package), the fromlist argument is set to the list ['\*'] so that the return value is the named module rather than the top-level package containing it as would otherwise be the case. (Unfortunately, this has an additional side effect when name in fact specifies a subpackage instead of a submodule: the submodules specified in the package’s \_\_all\_\_ variable are loaded.) Return a new reference to the imported module, or NULL with an exception set on failure. Before Python 2.4, the module may still be created in the failure case — examine sys.modules to find out. Starting with Python 2.4, a failing import of a module no longer leaves the module in sys.modules.

Changed in version 2.4: Failing imports remove incomplete module objects.

Changed in version 2.6: Always uses absolute imports.

PyObject\* **PyImport\_ImportModuleNoBlock**(const char \*name)

This version of PyImport\_ImportModule() does not block. It’s intended to be used in C functions that import other modules to execute a function. The import may block if another thread holds the import lock. The function PyImport\_ImportModuleNoBlock() never blocks. It first tries to fetch the module from sys.modules and falls back to PyImport\_ImportModule() unless the lock is held, in which case the function will raise an ImportError.

New in version 2.6.

PyObject\* **PyImport\_ImportModuleEx**(char \*name, PyObject \*globals, PyObject \*locals, PyObject \*from-

Return value: New reference. Import a module. This is best described by referring to the built-in Python function \_\_import\_\_(), as the standard \_\_import\_\_() function calls this function directly.

The return value is a new reference to the imported module or top-level package, or NULL with an exception set on failure (before Python 2.4, the module may still be created in this case). Like for \_\_import\_\_(), the return value when a submodule of a package was requested is normally the top-level package, unless a non-empty fromlist was given.

Changed in version 2.4: Failing imports remove incomplete module objects.

Changed in version 2.6: The function is an alias for PyImport\_ImportModuleLevel() with -1 as level, meaning relative import.

PyObject\* **PyImport\_ImportModuleLevel**(char \*name, PyObject \*globals, PyObject \*locals, PyOb-

ject \*fromlist, int level)

Return value: New reference. Import a module. This is best described by referring to the built-in Python function import\_\_(), as the standard \_\_import\_\_() function calls this function directly.

The return value is a new reference to the imported module or top-level package, or NULL with an exception set on failure. Like for \_\_import\_\_(), the return value when a submodule of a package was requested is normally the top-level package, unless a non-empty fromlist was given.

New in version 2.5.

PyObject\* **PyImport\_Import**(PyObject \*name)

Return value: New reference. This is a higher-level interface that calls the current “import hook function”. It invokes the \_\_import\_\_() function from the \_\_builtins\_\_ of the current globals. This means that the import is done using whatever import hooks are installed in the current environment, e.g. by rexec or ihooks.

Changed in version 2.6: Always uses absolute imports.

<!-- page: 32 -->

## PyObject\* PyImport\_ReloadModule(PyObject \*m)

Return value: New reference. Reload a module. This is best described by referring to the built-in Python function reload(), as the standard reload() function calls this function directly. Return a new reference to the reloaded module, or NULL with an exception set on failure (the module still exists in this case).

## PyObject\* PyImport\_AddModule(const char \*name)

Return value: Borrowed reference. Return the module object corresponding to a module name. The name argument may be of the form package.module. First check the modules dictionary if there’s one there, and if not, create a new one and insert it in the modules dictionary. Return NULL with an exception set on failure.

**Note:** This function does not load or import the module; if the module wasn’t already loaded, you will get an empty module object. Use PyImport\_ImportModule() or one of its variants to import a module. Package structures implied by a dotted name for name are not created if not already present.

## PyObject\* PyImport\_ExecCodeModule(char \*name, PyObject \*co)

Return value: New reference. Given a module name (possibly of the form package.module) and a code object read from a Python bytecode file or obtained from the built-in function compile(), load the module. Return a new reference to the module object, or NULL with an exception set if an error occurred. Before Python 2.4, the module could still be created in error cases. Starting with Python 2.4, name is removed from sys.modules in error cases, and even if name was already in sys.modules on entry to PyImport\_ExecCodeModule(). Leaving incompletely initialized modules in sys.modules is dangerous, as imports of such modules have no way to know that the module object is an unknown (and probably damaged with respect to the module author’s intents) state.

The module’s \_\_file\_\_ attribute will be set to the code object’s co\_filename.

This function will reload the module if it was already imported. See PyImport\_ReloadModule() for the intended way to reload a module.

If name points to a dotted name of the form package.module, any package structures not already created will still not be created.

Changed in version 2.4: name is removed from sys.modules in error cases.

## PyObject\* PyImport\_ExecCodeModuleEx(char \*name, PyObject \*co, char \*pathname)

Return value: New reference. Like PyImport\_ExecCodeModule(), but the \_\_file\_\_ attribute of the module object is set to pathname if it is non-NULL.

## long PyImport\_GetMagicNumber()

Return the magic number for Python bytecode files (a.k.a. .pyc and .pyo files). The magic number should be present in the first four bytes of the bytecode file, in little-endian byte order.

## PyObject\* PyImport\_GetModuleDict()

Return value: Borrowed reference. Return the dictionary used for the module administration (a.k.a. sys. modules). Note that this is a per-interpreter variable.

## PyObject\* PyImport\_GetImporter(PyObject \*path)

Return an importer object for a sys.path/pkg.\_\_path\_\_ item path, possibly by fetching it from the sys. path\_importer\_cache dict. If it wasn’t yet cached, traverse sys.path\_hooks until a hook is found that can handle the path item. Return None if no hook could; this tells our caller it should fall back to the built-in import mechanism. Cache the result in sys.path\_importer\_cache. Return a new reference to the importer object.

New in version 2.6.

## void \_PyImport\_Init()

Initialize the import mechanism. For internal use only.

## void PyImport\_Cleanup()

Empty the module table. For internal use only.

<!-- page: 33 -->

```python
void _PyImport_Fini()
    Finalize the import mechanism. For internal use only.
```

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$PyObject^*\_\text{PyImport\_FindExtension (char *, char *)}$
For internal use only.
</div>

```txt
PyObject* _PyImport_FixupExtension (char *, char *)
    For internal use only.
```

## int PyImport\_ImportFrozenModule(char \*name)

Load a frozen module named name. Return 1 for success, 0 if the module is not found, and -1 with an exception set if the initialization failed. To access the imported module on a successful load, use PyImport\_ImportModule(). (Note the misnomer — this function would reload the module if it was already imported.)

## struct \_frozen

This is the structure type definition for frozen module descriptors, as generated by the **freeze** utility (see Tools/ freeze/ in the Python source distribution). Its definition, found in Include/import.h, is:

```c
struct _frozen {
    char *name;
    unsigned char *code;
    int size;
};
```

## struct \_frozen\* PyImport\_FrozenModules

This pointer is initialized to point to an array of struct \_frozen records, terminated by one whose members are all NULL or zero. When a frozen module is imported, it is searched in this table. Third-party code could play tricks with this to provide a dynamically created collection of frozen modules.

## int PyImport\_AppendInittab(const char \*name, void (\*initfunc)(void))

Add a single module to the existing table of built-in modules. This is a convenience wrapper around PyImport\_ExtendInittab(), returning -1 if the table could not be extended. The new module can be imported by the name name, and uses the function initfunc as the initialization function called on the first attempted import. This should be called before Py\_Initialize().

## struct \_inittab

Structure describing a single entry in the list of built-in modules. Each of these structures gives the name and initialization function for a module built into the interpreter. Programs which embed Python may use an array of these structures in conjunction with PyImport\_ExtendInittab() to provide additional built-in modules. The structure is defined in Include/import.h as:

```txt
struct _inittab {
    char *name;
    void (*initfunc)(void);
};
```

## int PyImport\_ExtendInittab(struct \_inittab \*newtab)

Add a collection of modules to the table of built-in modules. The newtab array must end with a sentinel entry which contains NULL for the name field; failure to provide the sentinel value can result in a memory fault. Returns 0 on success or -1 if insufficient memory could be allocated to extend the internal table. In the event of failure, no modules are added to the internal table. This should be called before Py\_Initialize().

<!-- page: 34 -->

## 5.5 Data marshalling support

These routines allow C code to work with serialized objects using the same data format as the marshal module. There are functions to write data into the serialization format, and additional functions that can be used to read the data back. Files used to store marshalled data must be opened in binary mode.

Numeric values are stored with the least significant byte first.

The module supports two versions of the data format: version 0 is the historical version, version 1 (new in Python 2.4) shares interned strings in the file, and upon unmarshalling. Version 2 (new in Python 2.5) uses a binary format for floating point numbers. Py\_MARSHAL\_VERSION indicates the current file format (currently 2).

## void PyMarshal\_WriteLongToFile(long value, FILE \*file, int version)

Marshal a long integer, value, to file. This will only write the least-significant 32 bits of value; regardless of the size of the native long type.

Changed in version 2.4: version indicates the file format.

## void PyMarshal\_WriteObjectToFile(PyObject \*value, FILE \*file, int version)

Marshal a Python object, value, to file.

Changed in version 2.4: version indicates the file format.

## PyObject\* PyMarshal\_WriteObjectToString(PyObject \*value, int version)

Return value: New reference. Return a string object containing the marshalled representation of value.

Changed in version 2.4: version indicates the file format.

The following functions allow marshalled values to be read back in.

XXX What about error detection? It appears that reading past the end of the file will always result in a negative numeric value (where that’s relevant), but it’s not clear that negative values won’t be handled properly when there’s no error. What’s the right way to tell? Should only non-negative values be written using these routines?

## long PyMarshal\_ReadLongFromFile(FILE \*file)

Return a C long from the data stream in a FILE\* opened for reading. Only a 32-bit value can be read in using this function, regardless of the native size of long.

## int PyMarshal\_ReadShortFromFile(FILE \*file)

Return a C short from the data stream in a FILE\* opened for reading. Only a 16-bit value can be read in using this function, regardless of the native size of short.

## PyObject\* PyMarshal\_ReadObjectFromFile(FILE \*file)

Return value: New reference. Return a Python object from the data stream in a FILE\* opened for reading. On error, sets the appropriate exception (EOFError or TypeError) and returns NULL.

## PyObject\* PyMarshal\_ReadLastObjectFromFile(FILE \*file)

Return value: New reference. Return a Python object from the data stream in a FILE\* opened for reading. Unlike PyMarshal\_ReadObjectFromFile(), this function assumes that no further objects will be read from the file, allowing it to aggressively load file data into memory so that the de-serialization can operate from data in memory rather than reading a byte at a time from the file. Only use these variant if you are certain that you won’t be reading anything else from the file. On error, sets the appropriate exception (EOFError or TypeError) and returns NULL.

## PyObject\* PyMarshal\_ReadObjectFromString(char \*string, Py\_ssize\_t len)

Return value: New reference. Return a Python object from the data stream in a character buffer containing len bytes pointed to by string. On error, sets the appropriate exception (EOFError or TypeError) and returns NULL.

Changed in version 2.5: This function used an int type for len. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 35 -->

## 5.6 Parsing arguments and building values

These functions are useful when creating your own extensions functions and methods. Additional information and examples are available in extending-index.

The first three of these functions described, PyArg\_ParseTuple(), PyArg\_ParseTupleAndKeywords(), and PyArg\_Parse(), all use format strings which are used to tell the function about the expected arguments. The format strings use the same syntax for each of these functions.

A format string consists of zero or more “format units.” A format unit describes one Python object; it is usually a single character or a parenthesized sequence of format units. With a few exceptions, a format unit that is not a parenthesized sequence normally corresponds to a single address argument to these functions. In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that matches the format unit; and the entry in [square] brackets is the type of the C variable(s) whose address should be passed.

These formats allow accessing an object as a contiguous chunk of memory. You don’t have to provide raw storage for the returned unicode or bytes area. Also, you won’t have to release any memory yourself, except with the es, es#, et and et# formats.

**s (string or Unicode) [const char \*]** Convert a Python string or Unicode object to a C pointer to a character string. You must not provide storage for the string itself; a pointer to an existing string is stored into the character pointer variable whose address you pass. The C string is NUL-terminated. The Python string must not contain embedded NUL bytes; if it does, a TypeError exception is raised. Unicode objects are converted to C strings using the default encoding. If this conversion fails, a UnicodeError is raised.

**s# (string, Unicode or any read buffer compatible object) [const char \*, int (or Py\_ssize\_t, see below)]** This variant on s stores into two C variables, the first one a pointer to a character string, the second one its length. In this case the Python string may contain embedded null bytes. Unicode objects pass back a pointer to the default encoded string version of the object if such a conversion is possible. All other read-buffer compatible objects pass back a reference to the raw internal data representation.

Starting with Python 2.5 the type of the length argument can be controlled by defining the macro PY\_SSIZE\_T\_CLEAN before including Python.h. If the macro is defined, length is a Py\_ssize\_t rather than an int.

**s\* (string, Unicode, or any buffer compatible object) [Py\_buffer]** Similar to s#, this code fills a Py\_buffer structure provided by the caller. The buffer gets locked, so that the caller can subsequently use the buffer even inside a Py\_BEGIN\_ALLOW\_THREADS block; the caller is responsible for calling PyBuffer\_Release with the structure after it has processed the data.

New in version 2.6.

**z (string, Unicode or None) [const char \*]** Like s, but the Python object may also be None, in which case the C pointer is set to NULL.

**z# (string, Unicode, None or any read buffer compatible object) [const char \*, int]** This is to s# as z is to s.

**z\* (string, Unicode, None or any buffer compatible object) [Py\_buffer]** This is to s\* as z is to s.

New in version 2.6.

**u (Unicode) [Py\_UNICODE \*]** Convert a Python Unicode object to a C pointer to a NUL-terminated buffer of 16-bit Unicode (UTF-16) data. As with s, there is no need to provide storage for the Unicode data buffer; a pointer to the existing Unicode data is stored into the Py\_UNICODE pointer variable whose address you pass.

**u# (Unicode) [Py\_UNICODE \*, int]** This variant on u stores into two C variables, the first one a pointer to a Unicode data buffer, the second one its length. Non-Unicode objects are handled by interpreting their read-buffer pointer as pointer to a Py\_UNICODE array.

<!-- page: 36 -->

**es (string, Unicode or character buffer compatible object) [const char \*encoding, char \*\*buffer]** This variant on s is used for encoding Unicode and objects convertible to Unicode into a character buffer. It only works for encoded data without embedded NUL bytes.

This format requires two arguments. The first is only used as input, and must be a const char\* which points to the name of an encoding as a NUL-terminated string, or NULL, in which case the default encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char\*\*; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text will be encoded in the encoding specified by the first argument.

PyArg\_ParseTuple() will allocate a buffer of the needed size, copy the encoded data into this buffer and adjust \*buffer to reference the newly allocated storage. The caller is responsible for calling PyMem\_Free() to free the allocated buffer after use.

**et (string, Unicode or character buffer compatible object) [const char \*encoding, char \*\*buffer]** Same as es except that 8-bit string objects are passed through without recoding them. Instead, the implementation assumes that the string object uses the encoding passed in as parameter.

**es# (string, Unicode or character buffer compatible object) [const char \*encoding, char \*\*buffer, int \*buffer\_length]** This variant on s# is used for encoding Unicode and objects convertible to Unicode into a character buffer. Unlike the es format, this variant allows input data which contains NUL characters.

It requires three arguments. The first is only used as input, and must be a const char\* which points to the name of an encoding as a NUL-terminated string, or NULL, in which case the default encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char\*\*; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text will be encoded in the encoding specified by the first argument. The third argument must be a pointer to an integer; the referenced integer will be set to the number of bytes in the output buffer.

There are two modes of operation:

If \*buffer points a NULL pointer, the function will allocate a buffer of the needed size, copy the encoded data into this buffer and set \*buffer to reference the newly allocated storage. The caller is responsible for calling PyMem\_Free() to free the allocated buffer after usage.

If \*buffer points to a non-NULL pointer (an already allocated buffer), PyArg\_ParseTuple() will use this location as the buffer and interpret the initial value of \*buffer\_length as the buffer size. It will then copy the encoded data into the buffer and NUL-terminate it. If the buffer is not large enough, a TypeError will be set. Note: starting from Python 3.6 a ValueError will be set.

In both cases, \*buffer\_length is set to the length of the encoded data without the trailing NUL byte.

**et# (string, Unicode or character buffer compatible object) [const char \*encoding, char \*\*buffer, int \*buffer\_length]** Same as es# except that string objects are passed through without recoding them. Instead, the implementation assumes that the string object uses the encoding passed in as parameter.

**b (integer) [unsigned char]** Convert a nonnegative Python integer to an unsigned tiny int, stored in a C unsigned char.

**B (integer) [unsigned char]** Convert a Python integer to a tiny int without overflow checking, stored in a C unsigned char.

New in version 2.3.

**h (integer) [short int]** Convert a Python integer to a C short int.

**H (integer) [unsigned short int]** Convert a Python integer to a C unsigned short int, without overflow checking.

New in version 2.3.

**i (integer) [int]** Convert a Python integer to a plain C int.

<!-- page: 37 -->

**I (integer) [unsigned int]** Convert a Python integer to a C unsigned int, without overflow checking. New in version 2.3.

**l (integer) [long int]** Convert a Python integer to a C long int.

**k (integer) [unsigned long]** Convert a Python integer or long integer to a C unsigned long without overflow checking.

New in version 2.3.

**L (integer) [PY\_LONG\_LONG]** Convert a Python integer to a C long long. This format is only available on platforms that support long long (or \_int64 on Windows).

**K (integer) [unsigned PY\_LONG\_LONG]** Convert a Python integer or long integer to a C unsigned long long without overflow checking. This format is only available on platforms that support unsigned long long (or unsigned \_int64 on Windows).

New in version 2.3.

**n (integer) [Py\_ssize\_t]** Convert a Python integer or long integer to a C Py\_ssize\_t.

**c (string of length 1) [char]** Convert a Python character, represented as a string of length 1, to a C char.

**f (float) [float]** Convert a Python floating point number to a C float.

**d (float) [double]** Convert a Python floating point number to a C double.

**D (complex) [Py\_complex]** Convert a Python complex number to a C Py\_complex structure.

**O (object) [PyObject \*]** Store a Python object (without any conversion) in a C object pointer. The C program thus receives the actual object that was passed. The object’s reference count is not increased. The pointer stored is not NULL.

**O! (object) [typeobject, PyObject \*]** Store a Python object in a C object pointer. This is similar to O, but takes two C arguments: the first is the address of a Python type object, the second is the address of the C variable (of type PyObject\*) into which the object pointer is stored. If the Python object does not have the required type, TypeError is raised.

**O& (object) [converter, anything]** Convert a Python object to a C variable through a converter function. This takes two arguments: the first is a function, the second is the address of a C variable (of arbitrary type), converted to void \*. The converter function in turn is called as follows:

status = converter(object, address);

where object is the Python object to be converted and address is the void\* argument that was passed to the PyArg\_Parse\*() function. The returned status should be 1 for a successful conversion and 0 if the conversion has failed. When the conversion fails, the converter function should raise an exception and leave the content of address unmodified.

**S (string) [PyStringObject \*]** Like O but requires that the Python object is a string object. Raises TypeError if the object is not a string object. The C variable may also be declared as PyObject\*.

**U (Unicode string) [PyUnicodeObject \*]** Like O but requires that the Python object is a Unicode object. Raises TypeError if the object is not a Unicode object. The C variable may also be declared as PyObject\*.

**t# (read-only character buffer) [char \*, int]** Like s#, but accepts any object which implements the read-only buffer interface. The char\* variable is set to point to the first byte of the buffer, and the int is set to the length of the buffer. Only single-segment buffer objects are accepted; TypeError is raised for all others.

<!-- page: 38 -->

**w (read-write character buffer) [char \*]** Similar to s, but accepts any object which implements the read-write buffer interface. The caller must determine the length of the buffer by other means, or use w# instead. Only single-segment buffer objects are accepted; TypeError is raised for all others.

**w# (read-write character buffer) [char \*, Py\_ssize\_t]** Like s#, but accepts any object which implements the readwrite buffer interface. The char \* variable is set to point to the first byte of the buffer, and the Py\_ssize\_t is set to the length of the buffer. Only single-segment buffer objects are accepted; TypeError is raised for all others.

**w\* (read-write byte-oriented buffer) [Py\_buffer]** This is to w what s\* is to s.

New in version 2.6.

**(items) (tuple) [matching-items]** The object must be a Python sequence whose length is the number of format units in items. The C arguments must correspond to the individual format units in items. Format units for sequences may be nested.

**Note:** Prior to Python version 1.5.2, this format specifier only accepted a tuple containing the individual parameters, not an arbitrary sequence. Code which previously caused TypeError to be raised here may now proceed without an exception. This is not expected to be a problem for existing code.

It is possible to pass Python long integers where integers are requested; however no proper range checking is done — the most significant bits are silently truncated when the receiving field is too small to receive the value (actually, the semantics are inherited from downcasts in C — your mileage may vary).

A few other characters have a meaning in a format string. These may not occur inside nested parentheses. They are:

| Indicates that the remaining arguments in the Python argument list are optional. The C variables corresponding to optional arguments should be initialized to their default value — when an optional argument is not specified, PyArg\_ParseTuple() does not touch the contents of the corresponding C variable(s).

: The list of format units ends here; the string after the colon is used as the function name in error messages (the “associated value” of the exception that PyArg\_ParseTuple() raises).

; The list of format units ends here; the string after the semicolon is used as the error message instead of the default error message. : and ; mutually exclude each other.

Note that any Python object references which are provided to the caller are borrowed references; do not decrement their reference count!

Additional arguments passed to these functions must be addresses of variables whose type is determined by the format string; these are used to store values from the input tuple. There are a few cases, as described in the list of format units above, where these parameters are used as input values; they should match what is specified for the corresponding format unit in that case.

For the conversion to succeed, the arg object must match the format and the format must be exhausted. On success, the PyArg\_Parse\*() functions return true, otherwise they return false and raise an appropriate exception. When the PyArg\_Parse\*() functions fail due to conversion failure in one of the format units, the variables at the addresses corresponding to that and the following format units are left untouched.

int **PyArg\_ParseTuple**(PyObject \*args, const char \*format, ...)

Parse the parameters of a function that takes only positional parameters into local variables. Returns true on success; on failure, it returns false and raises the appropriate exception.

int **PyArg\_VaParse**(PyObject \*args, const char \*format, va\_list vargs)

Identical to PyArg\_ParseTuple(), except that it accepts a va\_list rather than a variable number of arguments.

int **PyArg\_ParseTupleAndKeywords**(PyObject \*args, PyObject \*kw, const char \*format, char \*keywords[], ...)

Parse the parameters of a function that takes both positional and keyword parameters into local variables. Returns

<!-- page: 39 -->

true on success; on failure, it returns false and raises the appropriate exception.

## int PyArg\_VaParseTupleAndKeywords(PyObject \*args, PyObject \*kw, const char \*format, char \*key-

Identical to PyArg\_ParseTupleAndKeywords(), except that it accepts a va\_list rather than a variable number of arguments.

## int PyArg\_Parse(PyObject \*args, const char \*format, ...)

Function used to deconstruct the argument lists of “old-style” functions — these are functions which use the METH\_OLDARGS parameter parsing method. This is not recommended for use in parameter parsing in new code, and most code in the standard interpreter has been modified to no longer use this for that purpose. It does remain a convenient way to decompose other tuples, however, and may continue to be used for that purpose.

## int PyArg\_UnpackTuple(PyObject \*args, const char \*name, Py\_ssize\_t min, Py\_ssize\_t max, ...)

A simpler form of parameter retrieval which does not use a format string to specify the types of the arguments. Functions which use this method to retrieve their parameters should be declared as METH\_VARARGS in function or method tables. The tuple containing the actual parameters should be passed as args; it must actually be a tuple. The length of the tuple must be at least min and no more than max; min and max may be equal. Additional arguments must be passed to the function, each of which should be a pointer to a PyObject\* variable; these will be filled in with the values from args; they will contain borrowed references. The variables which correspond to optional parameters not given by args will not be filled in; these should be initialized by the caller. This function returns true on success and false if args is not a tuple or contains the wrong number of elements; an exception will be set if there was a failure.

This is an example of the use of this function, taken from the sources for the \_weakref helper module for weak references:

```c
static PyObject *
weakref_ref(PyObject *self, PyObject *args)
{
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

## New in version 2.2.

Changed in version 2.5: This function used an int type for min and max. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* Py\_BuildValue(const char \*format, ...)

Return value: New reference. Create a new value based on a format string similar to those accepted by the PyArg\_Parse\*() family of functions and a sequence of values. Returns the value or NULL in the case of an error; an exception will be raised if NULL is returned.

Py\_BuildValue() does not always build a tuple. It builds a tuple only if its format string contains two or more format units. If the format string is empty, it returns None; if it contains exactly one format unit, it returns whatever object is described by that format unit. To force it to return a tuple of size 0 or one, parenthesize the format string.

<!-- page: 40 -->

When memory buffers are passed as parameters to supply data to build objects, as for the s and s# formats, the required data is copied. Buffers provided by the caller are never referenced by the objects created by Py\_BuildValue(). In other words, if your code invokes malloc() and passes the allocated memory to Py\_BuildValue(), your code is responsible for calling free() for that memory once Py\_BuildValue() returns.

In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that the format unit will return; and the entry in [square] brackets is the type of the C value(s) to be passed.

The characters space, tab, colon and comma are ignored in format strings (but not within format units such as s#). This can be used to make long format strings a tad more readable.

**s (string) [char \*]** Convert a null-terminated C string to a Python object. If the C string pointer is NULL, None is used.

**s# (string) [char \*, int]** Convert a C string and its length to a Python object. If the C string pointer is NULL, the length is ignored and None is returned.

**z (string or None) [char \*]** Same as s.

**z# (string or None) [char \*, int]** Same as s#.

**u (Unicode string) [Py\_UNICODE \*]** Convert a null-terminated buffer of Unicode (UCS-2 or UCS-4) data to a Python Unicode object. If the Unicode buffer pointer is NULL, None is returned.

**u# (Unicode string) [Py\_UNICODE \*, int]** Convert a Unicode (UCS-2 or UCS-4) data buffer and its length to a Python Unicode object. If the Unicode buffer pointer is NULL, the length is ignored and None is returned.

**i (integer) [int]** Convert a plain C int to a Python integer object.

**b (integer) [char]** Convert a plain C char to a Python integer object.

**h (integer) [short int]** Convert a plain C short int to a Python integer object.

**l (integer) [long int]** Convert a C long int to a Python integer object.

**B (integer) [unsigned char]** Convert a C unsigned char to a Python integer object.

**H (integer) [unsigned short int]** Convert a C unsigned short int to a Python integer object.

**I (integer/long) [unsigned int]** Convert a C unsigned int to a Python integer object or a Python long integer object, if it is larger than sys.maxint.

**k (integer/long) [unsigned long]** Convert a C unsigned long to a Python integer object or a Python long integer object, if it is larger than sys.maxint.

**L (long) [PY\_LONG\_LONG]** Convert a C long long to a Python long integer object. Only available on platforms that support long long.

**K (long) [unsigned PY\_LONG\_LONG]** Convert a C unsigned long long to a Python long integer object. Only available on platforms that support unsigned long long.

**n (int) [Py\_ssize\_t]** Convert a C Py\_ssize\_t to a Python integer or long integer. New in version 2.5.

**c (string of length 1) [char]** Convert a C int representing a character to a Python string of length 1.

**d (float) [double]** Convert a C double to a Python floating point number.

**f (float) [float]** Same as d.

**D (complex) [Py\_complex \*]** Convert a C Py\_complex structure to a Python complex number.

<!-- page: 41 -->

**O (object) [PyObject \*]** Pass a Python object untouched (except for its reference count, which is incremented by one). If the object passed in is a NULL pointer, it is assumed that this was caused because the call producing the argument found an error and set an exception. Therefore, Py\_BuildValue() will return NULL but won’t raise an exception. If no exception has been raised yet, SystemError is set.

**S (object) [PyObject \*]** Same as O.

**N (object) [PyObject \*]** Same as O, except it doesn’t increment the reference count on the object. Useful when the object is created by a call to an object constructor in the argument list.

**O& (object) [converter, anything]** Convert anything to a Python object through a converter function. The function is called with anything (which should be compatible with void \*) as its argument and should return a “new” Python object, or NULL if an error occurred.

**(items) (tuple) [matching-items]** Convert a sequence of C values to a Python tuple with the same number of items.

**[items] (list) [matching-items]** Convert a sequence of C values to a Python list with the same number of items.

**{items} (dictionary) [matching-items]** Convert a sequence of C values to a Python dictionary. Each pair of consecutive C values adds one item to the dictionary, serving as key and value, respectively.

If there is an error in the format string, the SystemError exception is set and NULL returned.

PyObject\* **Py\_VaBuildValue**(const char \*format, va\_list vargs)

Identical to Py\_BuildValue(), except that it accepts a va\_list rather than a variable number of arguments.

## 5.7 String conversion and formatting

Functions for number conversion and formatted string output.

int **PyOS\_snprintf**(char \*str, size\_t size, const char \*format, ...)

Output not more than size bytes to str according to the format string format and the extra arguments. See the Unix man page snprintf(2).

int **PyOS\_vsnprintf**(char \*str, size\_t size, const char \*format, va\_list va)

Output not more than size bytes to str according to the format string format and the variable argument list va. Unix man page vsnprintf(2).

PyOS\_snprintf() and PyOS\_vsnprintf() wrap the Standard C library functions snprintf() and vsnprintf(). Their purpose is to guarantee consistent behavior in corner cases, which the Standard C functions do not.

The wrappers ensure that str\*[\*size-1] is always '\0' upon return. They never write more than size bytes (including the trailing '\0' into str. Both functions require that str != NULL, size > 0 and format != NULL.

If the platform doesn’t have vsnprintf() and the buffer size needed to avoid truncation exceeds size by more than 512 bytes, Python aborts with a Py\_FatalError.

The return value (rv) for these functions should be interpreted as follows:

• When 0 <= rv < size, the output conversion was successful and rv characters were written to str (excluding the trailing '\0' byte at str\*[\*rv]).

• When rv >= size, the output conversion was truncated and a buffer with rv + 1 bytes would have been needed to succeed. str\*[\*size-1] is '\0' in this case.

• When rv < 0, “something bad happened.” str\*[\*size-1] is '\0' in this case too, but the rest of str is undefined. The exact cause of the error depends on the underlying platform.

The following functions provide locale-independent string to number conversions.

<!-- page: 42 -->

## double PyOS\_string\_to\_double(const char \*s, char \*\*endptr, PyObject \*overflow\_exception)

Convert a string s to a double, raising a Python exception on failure. The set of accepted strings corresponds to the set of strings accepted by Python’s float() constructor, except that s must not have leading or trailing whitespace. The conversion is independent of the current locale.

If endptr is NULL, convert the whole string. Raise ValueError and return -1.0 if the string is not a valid representation of a floating-point number.

If endptr is not NULL, convert as much of the string as possible and set \*endptr to point to the first unconverted character. If no initial segment of the string is the valid representation of a floating-point number, set \*endptr to point to the beginning of the string, raise ValueError, and return -1.0.

If s represents a value that is too large to store in a float (for example, "1e500" is such a string on many platforms) then if overflow\_exception is NULL return Py\_HUGE\_VAL (with an appropriate sign) and don’t set any exception. Otherwise, overflow\_exception must point to a Python exception object; raise that exception and return -1.0. In both cases, set \*endptr to point to the first character after the converted value.

If any other error occurs during the conversion (for example an out-of-memory error), set the appropriate Python exception and return -1.0.

New in version 2.7.

## double PyOS\_ascii\_strtod(const char \*nptr, char \*\*endptr)

Convert a string to a double. This function behaves like the Standard C function strtod() does in the C locale. It does this without changing the current locale, since that would not be thread-safe.

PyOS\_ascii\_strtod() should typically be used for reading configuration files or other non-user input that should be locale independent.

See the Unix man page strtod(2) for details.

New in version 2.4.

Deprecated since version 2.7: Use PyOS\_string\_to\_double() instead.

## char\* PyOS\_ascii\_formatd(char \*buffer, size\_t buf\_len, const char \*format, double d)

Convert a double to a string using the '.' as the decimal separator. format is a printf()-style format string specifying the number format. Allowed conversion characters are 'e', 'E', 'f', 'F', 'g' and 'G'.

The return value is a pointer to buffer with the converted string or NULL if the conversion failed.

New in version 2.4.

Deprecated since version 2.7: This function is removed in Python 2.7 and 3.1. Use PyOS\_double\_to\_string() instead.

char\* **PyOS\_double\_to\_string**(double val, char format\_code, int precision, int flags, int \*ptype) Convert a double val to a string using supplied format\_code, precision, and flags.

format\_code must be one of 'e', 'E', 'f', 'F', 'g', 'G' or 'r'. For 'r', the supplied precision must be 0 and is ignored. The 'r' format code specifies the standard repr() format.

flags can be zero or more of the values Py\_DTSF\_SIGN, Py\_DTSF\_ADD\_DOT\_0, or Py\_DTSF\_ALT, or-ed together:

• Py\_DTSF\_SIGN means to always precede the returned string with a sign character, even if val is non-negative.

• Py\_DTSF\_ADD\_DOT\_0 means to ensure that the returned string will not look like an integer.

• Py\_DTSF\_ALT means to apply “alternate” formatting rules. See the documentation for the PyOS\_snprintf() '#' specifier for details.

If ptype is non-NULL, then the value it points to will be set to one of Py\_DTST\_FINITE, Py\_DTST\_INFINITE, or Py\_DTST\_NAN, signifying that val is a finite number, an infinite number, or not a number, respectively.

<!-- page: 43 -->

The return value is a pointer to buffer with the converted string or NULL if the conversion failed. The caller is responsible for freeing the returned string by calling PyMem\_Free().

New in version 2.7.

double **PyOS\_ascii\_atof**(const char \*nptr)

Convert a string to a double in a locale-independent way.

See the Unix man page atof(2) for details.

New in version 2.4.

Deprecated since version 3.1: Use PyOS\_string\_to\_double() instead.

## char\* PyOS\_stricmp(char \*s1, char \*s2)

Case insensitive comparison of strings. The function works almost identically to strcmp() except that it ignores the case.

New in version 2.6.

char\* **PyOS\_strnicmp**(char \*s1, char \*s2, Py\_ssize\_t size)

Case insensitive comparison of strings. The function works almost identically to strncmp() except that it ignores the case.

New in version 2.6.

## 5.8 Reflection

## PyObject\* PyEval\_GetBuiltins()

Return value: Borrowed reference. Return a dictionary of the builtins in the current execution frame, or the interpreter of the thread state if no frame is currently executing.

## PyObject\* PyEval\_GetLocals()

Return value: Borrowed reference. Return a dictionary of the local variables in the current execution frame, or NULL if no frame is currently executing.

## P Ob \* P E l\_G tGl b l y ject y va e o a s()

Return value: Borrowed reference. Return a dictionary of the global variables in the current execution frame, or NULL if no frame is currently executing.

PyFrameObject\* **PyEval\_GetFrame**() Return value: Borrowed reference. Return the current thread state’s frame, which is NULL if no frame is currently executing.

int **PyFrame\_GetLineNumber**(PyFrameObject \*frame) Return the line number that frame is currently executing.

## int PyEval\_GetRestricted()

If there is a current frame and it is executing in restricted mode, return true, otherwise false.

const char\* **PyEval\_GetFuncName**(PyObject \*func) Return the name of func if it is a function, class or instance object, else the name of funcs type.

const char\* **PyEval\_GetFuncDesc**(PyObject \*func) Return a description string, depending on the type of func. Return values include “()” for functions and methods, ” constructor”, ” instance”, and ” object”. Concatenated with the result of PyEval\_GetFuncName(), the result will be a description of func.

<!-- page: 44 -->

## 5.9 Codec registry and support functions

int **PyCodec\_Register**(PyObject \*search\_function)

Register a new codec search function.

As side effect, this tries to load the encodings package, if not yet done, to make sure that it is always first in the list of search functions.

int **PyCodec\_KnownEncoding**(const char \*encoding)

Return 1 or 0 depending on whether there is a registered codec for the given encoding.

PyObject\* **PyCodec\_Encode**(PyObject \*object, const char \*encoding, const char \*errors)

Generic codec based encoding API.

object is passed through the encoder function found for the given encoding using the error handling method defined by errors. errors may be NULL to use the default method defined for the codec. Raises a LookupError if no encoder can be found.

PyObject\* **PyCodec\_Decode**(PyObject \*object, const char \*encoding, const char \*errors)

Generic codec based decoding API.

object is passed through the decoder function found for the given encoding using the error handling method defined by errors. errors may be NULL to use the default method defined for the codec. Raises a LookupError if no encoder can be found.

## 5.9.1 Codec lookup API

In the following functions, the encoding string is looked up converted to all lower-case characters, which makes encodings looked up through this mechanism effectively case-insensitive. If no codec is found, a KeyError is set and NULL returned.

PyObject\* **PyCodec\_Encoder**(const char \*encoding)

Get an encoder function for the given encoding.

PyObject\* **PyCodec\_Decoder**(const char \*encoding)

Get a decoder function for the given encoding.

PyObject\* **PyCodec\_IncrementalEncoder**(const char \*encoding, const char \*errors) Get an IncrementalEncoder object for the given encoding.

PyObject\* **PyCodec\_IncrementalDecoder**(const char \*encoding, const char \*errors) Get an IncrementalDecoder object for the given encoding.

PyObject\* **PyCodec\_StreamReader**(const char \*encoding, PyObject \*stream, const char \*errors) Get a StreamReader factory function for the given encoding.

PyObject\* **PyCodec\_StreamWriter**(const char \*encoding, PyObject \*stream, const char \*errors) Get a StreamWriter factory function for the given encoding.

<!-- page: 45 -->

## 5.9.2 Registry API for Unicode encoding error handlers

int **PyCodec\_RegisterError**(const char \*name, PyObject \*error)

Register the error handling callback function error under the given name. This callback function will be called by a codec when it encounters unencodable characters/undecodable bytes and name is specified as the error parameter in the call to the encode/decode function.

The callback gets a single argument, an instance of UnicodeEncodeError, UnicodeDecodeError or UnicodeTranslateError that holds information about the problematic sequence of characters or bytes and their offset in the original string (see Unicode Exception Objects for functions to extract this information). The callback must either raise the given exception, or return a two-item tuple containing the replacement for the problematic sequence, and an integer giving the offset in the original string at which encoding/decoding should be resumed.

Return 0 on success, -1 on error.

PyObject\* **PyCodec\_LookupError**(const char \*name)

Lookup the error handling callback function registered under name. As a special case NULL can be passed, in which case the error handling callback for “strict” will be returned.

PyObject\* **PyCodec\_StrictErrors** (PyObject \*exc)

Raise exc as an exception.

PyObject\* **PyCodec\_IgnoreErrors** (PyObject \*exc)

Ignore the unicode error, skipping the faulty input.

PyObject\* **PyCodec\_ReplaceErrors** (PyObject \*exc)

Replace the unicode encode error with ? or U+FFFD.

PyObject\* **PyCodec\_XMLCharRefReplaceErrors** (PyObject \*exc)

Replace the unicode encode error with XML character references.

PyObject\* **PyCodec\_BackslashReplaceErrors** (PyObject \*exc)

Replace the unicode encode error with backslash escapes (\x, \u and \U).

<!-- page: 46 -->

<!-- page: 47 -->

# ABSTRACT OBJECTS LAYER

The functions in this chapter interact with Python objects regardless of their type, or with wide classes of object types (e.g. all numerical types, or all sequence types). When used on object types for which they do not apply, they will raise a Python exception.

It is not possible to use these functions on objects that are not properly initialized, such as a list object that has been created by PyList\_New(), but whose items have not been set to some non-NULL value yet.

## 6.1 Object Protocol

int **PyObject\_Print**(PyObject \*o, FILE \*fp, int flags) Print an object o, on file fp. Returns -1 on error. The flags argument is used to enable certain printing options. The only option currently supported is Py\_PRINT\_RAW; if given, the str() of the object is written instead of the repr().

int **PyObject\_HasAttr**(PyObject \*o, PyObject \*attr\_name) Returns 1 if o has the attribute attr\_name, and 0 otherwise. This is equivalent to the Python expression hasattr(o, attr\_name). This function always succeeds.

int **PyObject\_HasAttrString**(PyObject \*o, const char \*attr\_name) Returns 1 if o has the attribute attr\_name, and 0 otherwise. This is equivalent to the Python expression hasattr(o, attr\_name). This function always succeeds.

PyObject\* **PyObject\_GetAttr**(PyObject \*o, PyObject \*attr\_name) Return value: New reference. Retrieve an attribute named attr\_name from object o. Returns the attribute value on success, or NULL on failure. This is the equivalent of the Python expression o.attr\_name.

PyObject\* **PyObject\_GetAttrString**(PyObject \*o, const char \*attr\_name) Return value: New reference. Retrieve an attribute named attr\_name from object o. Returns the attribute value on success, or NULL on failure. This is the equivalent of the Python expression o.attr\_name.

PyObject\* **PyObject\_GenericGetAttr**(PyObject \*o, PyObject \*name) Generic attribute getter function that is meant to be put into a type object’s tp\_getattro slot. It looks for a descriptor in the dictionary of classes in the object’s MRO as well as an attribute in the object’s \_\_dict (if present). As outlined in descriptors, data descriptors take preference over instance attributes, while non-data descriptors don’t. Otherwise, an AttributeError is raised.

int **PyObject\_SetAttr**(PyObject \*o, PyObject \*attr\_name, PyObject \*v) Set the value of the attribute named attr\_name, for object o, to the value v. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o.attr\_name = v.

If v is NULL, the attribute is deleted, however this feature is deprecated in favour of using PyObject\_DelAttr().

<!-- page: 48 -->

int **PyObject\_SetAttrString**(PyObject \*o, const char \*attr\_name, PyObject \*v) Set the value of the attribute named attr\_name, for object o, to the value v. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o.attr\_name = v. If v is NULL, the attribute is deleted, however this feature is deprecated in favour of using PyObject\_DelAttrString(). int **PyObject\_GenericSetAttr**(PyObject \*o, PyObject \*name, PyObject \*value) Generic attribute setter and deleter function that is meant to be put into a type object’s tp\_setattro slot. It looks for a data descriptor in the dictionary of classes in the object’s MRO, and if found it takes preference over setting or deleting the attribute in the instance dictionary. Otherwise, the attribute is set or deleted in the object’s dict\_\_ (if present). On success, 0 is returned, otherwise an AttributeError is raised and -1 is returned. int **PyObject\_DelAttr**(PyObject \*o, PyObject \*attr\_name) Delete attribute named attr\_name, for object o. Returns -1 on failure. This is the equivalent of the Python statement del o.attr\_name. int **PyObject\_DelAttrString**(PyObject \*o, const char \*attr\_name) Delete attribute named attr\_name, for object o. Returns -1 on failure. This is the equivalent of the Python statement del o.attr\_name. PyObject\* **PyObject\_RichCompare**(PyObject \*o1, PyObject \*o2, int opid) Return value: New reference. Compare the values of o1 and o2 using the operation specified by opid, which must be one of Py\_LT, Py\_LE, Py\_EQ, Py\_NE, Py\_GT, or Py\_GE, corresponding to <, <=, ==, !=, >, or >= respectively. This is the equivalent of the Python expression o1 op o2, where op is the operator corresponding to opid. Returns the value of the comparison on success, or NULL on failure. int **PyObject\_RichCompareBool**(PyObject \*o1, PyObject \*o2, int opid) Compare the values of o1 and o2 using the operation specified by opid, which must be one of Py\_LT, Py\_LE, Py\_EQ, Py\_NE, Py\_GT, or Py\_GE, corresponding to <, <=, ==, !=, >, or >= respectively. Returns -1 on error, 0 if the result is false, 1 otherwise. This is the equivalent of the Python expression o1 op o2, where op is the operator corresponding to opid.

**Note:** If o1 and o2 are the same object, PyObject\_RichCompareBool() will always return 1 for Py\_EQ and 0 for Py\_NE.

int **PyObject\_Cmp**(PyObject \*o1, PyObject \*o2, int \*result) Compare the values of o1 and o2 using a routine provided by o1, if one exists, otherwise with a routine provided by o2. The result of the comparison is returned in result. Returns -1 on failure. This is the equivalent of the Python statement result = cmp(o1, o2).

int **PyObject\_Compare**(PyObject \*o1, PyObject \*o2) Compare the values of o1 and o2 using a routine provided by o1, if one exists, otherwise with a routine provided by o2. Returns the result of the comparison on success. On error, the value returned is undefined; use PyErr\_Occurred() to detect an error. This is equivalent to the Python expression cmp(o1, o2).

PyObject\* **PyObject\_Repr**(PyObject \*o) Return value: New reference. Compute a string representation of object o. Returns the string representation on success, NULL on failure. This is the equivalent of the Python expression repr(o). Called by the repr() built-in function and by reverse quotes.

PyObject\* **PyObject\_Str**(PyObject \*o) Return value: New reference. Compute a string representation of object o. Returns the string representation on success, NULL on failure. This is the equivalent of the Python expression str(o). Called by the str() built-in function and by the print statement.

PyObject\* **PyObject\_Bytes**(PyObject \*o) Compute a bytes representation of object o. In 2.x, this is just an alias for PyObject\_Str().

<!-- page: 49 -->

## PyObject\* PyObject\_Unicode(PyObject \*o)

Return value: New reference. Compute a Unicode string representation of object o. Returns the Unicode string representation on success, NULL on failure. This is the equivalent of the Python expression unicode(o). Called by the unicode() built-in function.

## int PyObject\_IsInstance(PyObject \*inst, PyObject \*cls)

Returns 1 if inst is an instance of the class cls or a subclass of cls, or 0 if not. On error, returns -1 and sets an exception. If cls is a type object rather than a class object, PyObject\_IsInstance() returns 1 if inst is of type cls. If cls is a tuple, the check will be done against every entry in cls. The result will be 1 when at least one of the checks returns 1, otherwise it will be 0. If inst is not a class instance and cls is neither a type object, nor a class object, nor a tuple, inst must have a \_\_class\_\_ attribute — the class relationship of the value of that attribute with cls will be used to determine the result of this function.

New in version 2.1.

Changed in version 2.2: Support for a tuple as the second argument added.

Subclass determination is done in a fairly straightforward way, but includes a wrinkle that implementors of extensions to the class system may want to be aware of. If A and B are class objects, B is a subclass of A if it inherits from A either directly or indirectly. If either is not a class object, a more general mechanism is used to determine the class relationship of the two objects. When testing if B is a subclass of A, if A is B, PyObject\_IsSubclass() returns true. If A and B are different objects, B’s \_\_bases\_\_ attribute is searched in a depth-first fashion for A — the presence of the \_bases\_\_ attribute is considered sufficient for this determination.

## int PyObject\_IsSubclass(PyObject \*derived, PyObject \*cls)

Returns 1 if the class derived is identical to or derived from the class cls, otherwise returns 0. In case of an error, returns -1. If cls is a tuple, the check will be done against every entry in cls. The result will be 1 when at least one of the checks returns 1, otherwise it will be 0. If either derived or cls is not an actual class object (or tuple), this function uses the generic algorithm described above.

New in version 2.1.

Changed in version 2.3: Older versions of Python did not support a tuple as the second argument.

## int PyCallable\_Check(PyObject \*o)

Determine if the object o is callable. Return 1 if the object is callable and 0 otherwise. This function always succeeds.

## PyObject\* PyObject\_Call(PyObject \*callable\_object, PyObject \*args, PyObject \*kw)

Return value: New reference. Call a callable Python object callable\_object, with arguments given by the tuple args, and named arguments given by the dictionary kw. If no named arguments are needed, kw may be NULL. args must not be NULL, use an empty tuple if no arguments are needed. Returns the result of the call on success, or NULL on failure. This is the equivalent of the Python expression apply(callable\_object, args, kw) or callable\_object(\*args, \*\*kw).

New in version 2.2.

## PyObject\* PyObject\_CallObject(PyObject \*callable\_object, PyObject \*args)

Return value: New reference. Call a callable Python object callable\_object, with arguments given by the tuple args. If no arguments are needed, then args may be NULL. Returns the result of the call on success, or NULL on failure. This is the equivalent of the Python expression apply(callable\_object, args) or callable\_object(\*args).

## PyObject\* PyObject\_CallFunction(PyObject \*callable, char \*format, ...)

Return value: New reference. Call a callable Python object callable, with a variable number of C arguments. The C arguments are described using a Py\_BuildValue() style format string. The format may be NULL, indicating that no arguments are provided. Returns the result of the call on success, or NULL on failure. This is the equivalent of the Python expression apply(callable, args) or callable(\*args). Note that if you only pass PyObject \* args, PyObject\_CallFunctionObjArgs() is a faster alternative.

<!-- page: 50 -->

PyObject\* **PyObject\_CallMethod**(PyObject \*o, char \*method, char \*format, ...) Return value: New reference. Call the method named method of object o with a variable number of C arguments. The C arguments are described by a Py\_BuildValue() format string that should produce a tuple. The format may be NULL, indicating that no arguments are provided. Returns the result of the call on success, or NULL on failure. This is the equivalent of the Python expression o.method(args). Note that if you only pass PyObject \* args, PyObject\_CallMethodObjArgs() is a faster alternative.

PyObject\* **PyObject\_CallFunctionObjArgs**(PyObject \*callable, ..., NULL) Return value: New reference. Call a callable Python object callable, with a variable number of PyObject\* arguments. The arguments are provided as a variable number of parameters followed by NULL. Returns the result of the call on success, or NULL on failure.

New in version 2.2.

PyObject\* **PyObject\_CallMethodObjArgs**(PyObject \*o, PyObject \*name, ..., NULL) Return value: New reference. Calls a method of the object o, where the name of the method is given as a Python string object in name. It is called with a variable number of PyObject\* arguments. The arguments are provided as a variable number of parameters followed by NULL. Returns the result of the call on success, or NULL on failure. New in version 2.2.

long **PyObject\_Hash**(PyObject \*o) Compute and return the hash value of an object o. On failure, return -1. This is the equivalent of the Python expression hash(o).

long **PyObject\_HashNotImplemented**(PyObject \*o) Set a TypeError indicating that type(o) is not hashable and return -1. This function receives special treatment when stored in a tp\_hash slot, allowing a type to explicitly indicate to the interpreter that it is not hashable.

int **PyObject\_IsTrue**(PyObject \*o) Returns 1 if the object o is considered to be true, and 0 otherwise. This is equivalent to the Python expression not not o. On failure, return -1.

int **PyObject\_Not**(PyObject \*o) Returns 0 if the object o is considered to be true, and 1 otherwise. This is equivalent to the Python expression not o. On failure, return -1.

PyObject\* **PyObject\_Type**(PyObject \*o) Return value: New reference. When o is non-NULL, returns a type object corresponding to the object type of object o. On failure, raises SystemError and returns NULL. This is equivalent to the Python expression type(o). This function increments the reference count of the return value. There’s really no reason to use this function instead of the common expression o->ob\_type, which returns a pointer of type PyTypeObject\*, except when the incremented reference count is needed.

int **PyObject\_TypeCheck**(PyObject \*o, PyTypeObject \*type) Return true if the object o is of type type or a subtype of type. Both parameters must be non-NULL.

New in version 2.2.

Py\_ssize\_t **PyObject\_Length**(PyObject \*o)

Py\_ssize\_t **PyObject\_Size**(PyObject \*o) Return the length of object o. If the object o provides either the sequence and mapping protocols, the sequence length is returned. On error, -1 is returned. This is the equivalent to the Python expression len(o). Changed in version 2.5: These functions returned an int type. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyObject\_GetItem**(PyObject \*o, PyObject \*key) Return value: New reference. Return element of o corresponding to the object key or NULL on failure. This is the

<!-- page: 51 -->

equivalent of the Python expression o[key].

## int PyObject\_SetItem(PyObject \*o, PyObject \*key, PyObject \*v)

Map the object key to the value v. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o[key] = v.

## int PyObject\_DelItem(PyObject \*o, PyObject \*key)

Delete the mapping for key from o. Returns -1 on failure. This is the equivalent of the Python statement del o[key].

## int PyObject\_AsFileDescriptor(PyObject \*o)

Derives a file descriptor from a Python object. If the object is an integer or long integer, its value is returned. If not, the object’s fileno() method is called if it exists; the method must return an integer or long integer, which is returned as the file descriptor value. Returns -1 on failure.

## PyObject\* PyObject\_Dir(PyObject \*o)

Return value: New reference. This is equivalent to the Python expression dir(o), returning a (possibly empty) list of strings appropriate for the object argument, or NULL if there was an error. If the argument is NULL, this is like the Python dir(), returning the names of the current locals; in this case, if no execution frame is active then NULL is returned but PyErr\_Occurred() will return false.

## PyObject\* PyObject\_GetIter(PyObject \*o)

Return value: New reference. This is equivalent to the Python expression iter(o). It returns a new iterator for the object argument, or the object itself if the object is already an iterator. Raises TypeError and returns NULL if the object cannot be iterated.

## 6.2 Number Protocol

## int PyNumber\_Check(PyObject \*o)

Returns 1 if the object o provides numeric protocols, and false otherwise. This function always succeeds.

## PyObject\* PyNumber\_Add(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the result of adding o1 and o2, or NULL on failure. This is the equivalent of the Python expression o1 + o2.

## PyObject\* PyNumber\_Subtract(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the result of subtracting o2 from o1, or NULL on failure. This is the equivalent of the Python expression o1 - o2.

## PyObject\* PyNumber\_Multiply(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the result of multiplying o1 and o2, or NULL on failure. This is the equivalent of the Python expression o1 \* o2.

## PyObject\* PyNumber\_Divide(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the result of dividing o1 by o2, or NULL on failure. This is the equivalent of the Python expression o1 / o2.

## PyObject\* PyNumber\_FloorDivide(PyObject \*o1, PyObject \*o2)

Return value: New reference. Return the floor of o1 divided by o2, or NULL on failure. This is equivalent to the “classic” division of integers.

New in version 2.2.

## PyObject\* PyNumber\_TrueDivide(PyObject \*o1, PyObject \*o2)

Return value: New reference. Return a reasonable approximation for the mathematical value of o1 divided by o2, or NULL on failure. The return value is “approximate” because binary floating point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating point value when passed two integers.

<!-- page: 52 -->

New in version 2.2.

PyObject\* PyNumber\_Remainder(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the remainder of dividing o1 by o2, or NULL on failure. This is the equivalent of the Python expression o1 % o2.

PyObject\* PyNumber\_Divmod(PyObject \*o1, PyObject \*o2) Return value: New reference. See the built-in function divmod(). Returns NULL on failure. This is the equivalent of the Python expression divmod(o1, o2).

PyObject\* PyNumber\_Power(PyObject \*o1, PyObject \*o2, PyObject \*o3) Return value: New reference. See the built-in function pow(). Returns NULL on failure. This is the equivalent of the Python expression pow(o1, o2, o3), where o3 is optional. If o3 is to be ignored, pass Py\_None in its place (passing NULL for o3 would cause an illegal memory access).

PyObject\* PyNumber\_Negative(PyObject \*o) Return value: New reference. Returns the negation of o on success, or NULL on failure. This is the equivalent of the Python expression -o.

PyObject\* PyNumber\_Positive(PyObject \*o) Return value: New reference. Returns o on success, or NULL on failure. This is the equivalent of the Python expression +o.

PyObject\* PyNumber\_Absolute(PyObject \*o) Return value: New reference. Returns the absolute value of o, or NULL on failure. This is the equivalent of the Python expression abs(o).

PyObject\* PyNumber\_Invert(PyObject \*o) Return value: New reference. Returns the bitwise negation of o on success, or NULL on failure. This is the equivalent of the Python expression \~o.

PyObject\* PyNumber\_Lshift(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the result of left shifting o1 by o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 << o2.

PyObject\* PyNumber\_Rshift(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the result of right shifting o1 by o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 >> o2.

PyObject\* PyNumber\_And(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the “bitwise and” of o1 and o2 on success and NULL on failure. This is the equivalent of the Python expression o1 & o2.

PyObject\* PyNumber\_Xor(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the “bitwise exclusive or” of o1 by o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 ^ o2.

PyObject\* PyNumber\_Or(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the “bitwise or” of o1 and o2 on success, or NULL on failure. This is the equivalent of the Python expression o1 | o2.

PyObject\* PyNumber\_InPlaceAdd(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the result of adding o1 and o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 += o2.

PyObject\* PyNumber\_InPlaceSubtract(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the result of subtracting o2 from o1, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 -= o2.

PyObject\* PyNumber\_InPlaceMultiply(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the result of multiplying o1 and o2, or NULL on failure. The operation is

<!-- page: 53 -->

done in-place when o1 supports it. This is the equivalent of the Python statement o1 \*= o2.

## PyObject\* PyNumber\_InPlaceDivide(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the result of dividing o1 by o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 /= o2.

## PyObject\* PyNumber\_InPlaceFloorDivide(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the mathematical floor of dividing o1 by o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 //= o2.

New in version 2.2.

## PyObject\* PyNumber\_InPlaceTrueDivide(PyObject \*o1, PyObject \*o2)

Return value: New reference. Return a reasonable approximation for the mathematical value of o1 divided by o2, or NULL on failure. The return value is “approximate” because binary floating point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating point value when passed two integers. The operation is done in-place when o1 supports it.

New in version 2.2.

PyObject\* **PyNumber\_InPlaceRemainder**(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the remainder of dividing o1 by o2, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 %= o2.

## PyObject\* PyNumber\_InPlacePower(PyObject \*o1, PyObject \*o2, PyObject \*o3)

Return value: New reference. See the built-in function pow(). Returns NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 \*\*= o2 when o3 is Py\_None, or an in-place variant of pow(o1, o2, o3) otherwise. If o3 is to be ignored, pass Py\_None in its place (passing NULL for o3 would cause an illegal memory access).

## PyObject\* PyNumber\_InPlaceLshift(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the result of left shifting o1 by o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 <<= o2.

## PyObject\* PyNumber\_InPlaceRshift(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the result of right shifting o1 by o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 >>= o2.

## PyObject\* PyNumber\_InPlaceAnd(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the “bitwise and” of o1 and o2 on success and NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 &= o2.

PyObject\* **PyNumber\_InPlaceXor**(PyObject \*o1, PyObject \*o2) Return value: New reference. Returns the “bitwise exclusive or” of o1 by o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 ^= o2.

## PyObject\* PyNumber\_InPlaceOr(PyObject \*o1, PyObject \*o2)

Return value: New reference. Returns the “bitwise or” of o1 and o2 on success, or NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python statement o1 |= o2.

## int PyNumber\_Coerce(PyObject \*\*p1, PyObject \*\*p2)

This function takes the addresses of two variables of type PyObject\*. If the objects pointed to by \*p1 and \*p2 have the same type, increment their reference count and return 0 (success). If the objects can be converted to a common numeric type, replace \*p1 and \*p2 by their converted value (with ‘new’ reference counts), and return 0. If no conversion is possible, or if some other error occurs, return -1 (failure) and don’t increment the reference counts. The call PyNumber\_Coerce(&o1, &o2) is equivalent to the Python statement o1, o2 = coerce(o1, o2).

## int PyNumber\_CoerceEx(PyObject \*\*p1, PyObject \*\*p2)

This function is similar to PyNumber\_Coerce(), except that it returns 1 when the conversion is not possible and when no error is raised. Reference counts are still not increased in this case.

<!-- page: 54 -->

## PyObject\* PyNumber\_Int(PyObject \*o)

Return value: New reference. Returns the o converted to an integer object on success, or NULL on failure. If the argument is outside the integer range a long object will be returned instead. This is the equivalent of the Python expression int(o).

## PyObject\* PyNumber\_Long(PyObject \*o)

Return value: New reference. Returns the o converted to a long integer object on success, or NULL on failure. This is the equivalent of the Python expression long(o).

## PyObject\* PyNumber\_Float(PyObject \*o)

Return value: New reference. Returns the o converted to a float object on success, or NULL on failure. This is the equivalent of the Python expression float(o).

## PyObject\* PyNumber\_Index(PyObject \*o)

New in version 2.5.

## PyObject\* PyNumber\_ToBase(PyObject \*n, int base)

Returns the integer n converted to base as a string with a base marker of '0b', '0o', or '0x' if applicable. When base is not 2, 8, 10, or 16, the format is 'x#num' where x is the base. If n is not an int object, it is converted with PyNumber\_Index() first.

New in version 2.6.

## Py\_ssize\_t PyNumber\_AsSsize\_t(PyObject \*o, PyObject \*exc)

Returns o converted to a Py\_ssize\_t value if o can be interpreted as an integer. If o can be converted to a Python int or long but the attempt to convert to a Py\_ssize\_t value would raise an OverflowError, then the exc argument is the type of exception that will be raised (usually IndexError or OverflowError). If exc is NULL, then the exception is cleared and the value is clipped to PY\_SSIZE\_T\_MIN for a negative integer or PY\_SSIZE\_T\_MAX for a positive integer.

New in version 2.5.

## int PyIndex\_Check(PyObject \*o)

Returns 1 if o is an index integer (has the nb\_index slot of the tp\_as\_number structure filled in), and 0 otherwise.

New in version 2.5.

## 6.3 Sequence Protocol

## int PySequence\_Check(PyObject \*o)

Return 1 if the object provides sequence protocol, and 0 otherwise. This function always succeeds.

## Py\_ssize\_t PySequence\_Size(PyObject \*o)

## Py\_ssize\_t PySequence\_Length(PyObject \*o)

Returns the number of objects in sequence o on success, and -1 on failure. This is equivalent to the Python expression len(o).

Changed in version 2.5: These functions returned an int type. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PySequence\_Concat(PyObject \*o1, PyObject \*o2)

Return value: New reference. Return the concatenation of o1 and o2 on success, and NULL on failure. This is the equivalent of the Python expression o1 + o2.

## PyObject\* PySequence\_Repeat(PyObject \*o, Py\_ssize\_t count)

Return value: New reference. Return the result of repeating sequence object o count times, or NULL on failure. This is the equivalent of the Python expression o \* count.

<!-- page: 55 -->

Changed in version 2.5: This function used an int type for count. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PySequence\_InPlaceConcat(PyObject \*o1, PyObject \*o2) Return value: New reference. Return the concatenation of o1 and o2 on success, and NULL on failure. The operation is done in-place when o1 supports it. This is the equivalent of the Python expression o1 += o2.

PyObject\* PySequence\_InPlaceRepeat(PyObject \*o, Py\_ssize\_t count) Return value: New reference. Return the result of repeating sequence object o count times, or NULL on failure. The operation is done in-place when o supports it. This is the equivalent of the Python expression o \*= count. Changed in version 2.5: This function used an int type for count. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PySequence\_GetItem(PyObject \*o, Py\_ssize\_t i) Return value: New reference. Return the ith element of o, or NULL on failure. This is the equivalent of the Python expression o[i]. Changed in version 2.5: This function used an int type for i. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PySequence\_GetSlice(PyObject \*o, Py\_ssize\_t i1, Py\_ssize\_t i2) Return value: New reference. Return the slice of sequence object o between i1 and i2, or NULL on failure. This is the equivalent of the Python expression o[i1:i2]. Changed in version 2.5: This function used an int type for i1 and i2. This might require changes in your code for properly supporting 64-bit systems.

int PySequence\_SetItem(PyObject \*o, Py\_ssize\_t i, PyObject \*v) Assign object v to the ith element of o. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o[i] = v. This function does not steal a reference to v.

int PySequence\_DelItem(PyObject \*o, Py\_ssize\_t i) Delete the ith element of object o. Returns -1 on failure. This is the equivalent of the Python statement del o[i]. Changed in version 2.5: This function used an int type for i. This might require changes in your code for properly supporting 64-bit systems.

int PySequence\_SetSlice(PyObject \*o, Py\_ssize\_t i1, Py\_ssize\_t i2, PyObject \*v) Assign the sequence object v to the slice in sequence object o from i1 to i2. Raise an exception and return -1 on failure; return 0 on success. This is the equivalent of the Python statement o[i1:i2] = v. If v is NULL, the slice is deleted, however this feature is deprecated in favour of using PySequence\_DelSlice(). Changed in version 2.5: This function used an int type for i1 and i2. This might require changes in your code for properly supporting 64-bit systems.

int PySequence\_DelSlice(PyObject \*o, Py\_ssize\_t i1, Py\_ssize\_t i2) Delete the slice in sequence object o from i1 to i2. Returns -1 on failure. This is the equivalent of the Python statement del o[i1:i2]. Changed in version 2.5: This function used an int type for i1 and i2. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 56 -->

Py\_ssize\_t PySequence\_Count(PyObject \*o, PyObject \*value) Return the number of occurrences of value in o, that is, return the number of keys for which o[key] == value. On failure, return -1. This is equivalent to the Python expression o.count(value). Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

int PySequence\_Contains(PyObject \*o, PyObject \*value) Determine if o contains value. If an item in o is equal to value, return 1, otherwise return 0. On error, return -1. This is equivalent to the Python expression value in o.

Py\_ssize\_t PySequence\_Index(PyObject \*o, PyObject \*value) Return the first index i for which o[i] == value. On error, return -1. This is equivalent to the Python expression o.index(value). Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PySequence\_List(PyObject \*o) Return value: New reference. Return a list object with the same contents as the arbitrary sequence o. The returned list is guaranteed to be new.

PyObject\* PySequence\_Tuple(PyObject \*o) Return value: New reference. Return a tuple object with the same contents as the arbitrary sequence o or NULL on failure. If o is a tuple, a new reference will be returned, otherwise a tuple will be constructed with the appropriate contents. This is equivalent to the Python expression tuple(o).

PyObject\* PySequence\_Fast(PyObject \*o, const char \*m) Return value: New reference. Return the sequence o as a list, unless it is already a tuple or list, in which case o is returned. Use PySequence\_Fast\_GET\_ITEM() to access the members of the result. Returns NULL on failure. If the object is not a sequence, raises TypeError with m as the message text.

PyObject\* PySequence\_Fast\_GET\_ITEM(PyObject \*o, Py\_ssize\_t i) Return value: Borrowed reference. Return the ith element of o, assuming that o was returned by PySequence\_Fast(), o is not NULL, and that i is within bounds. Changed in version 2.5: This function used an int type for i. This might require changes in your code for properly supporting 64-bit systems.

PyObject\*\* PySequence\_Fast\_ITEMS(PyObject \*o) Return the underlying array of PyObject pointers. Assumes that o was returned by PySequence\_Fast() and o is not NULL. Note, if a list gets resized, the reallocation may relocate the items array. So, only use the underlying array pointer in contexts where the sequence cannot change.

PyObject\* PySequence\_ITEM(PyObject \*o, Py\_ssize\_t i) Return value: New reference. Return the ith element of o or NULL on failure. Macro form of PySequence\_GetItem() but without checking that PySequence\_Check() on o is true and without adjustment for negative indices. New in version 2.3. Changed in version 2.5: This function used an int type for i. This might require changes in your code for properly supporting 64-bit systems.

Py\_ssize\_t PySequence\_Fast\_GET\_SIZE(PyObject \*o) Returns the length of o, assuming that o was returned by PySequence\_Fast() and that o is not NULL. The size can also be gotten by calling PySequence\_Size() on o, but PySequence\_Fast\_GET\_SIZE() is faster because it can assume o is a list or tuple.

<!-- page: 57 -->

## 6.4 Mapping Protocol

int **PyMapping\_Check**(PyObject \*o) Return 1 if the object provides mapping protocol, and 0 otherwise. This function always succeeds.

Py\_ssize\_t **PyMapping\_Size**(PyObject \*o)

Py\_ssize\_t **PyMapping\_Length**(PyObject \*o) Returns the number of keys in object o on success, and -1 on failure. For objects that do not provide mapping protocol, this is equivalent to the Python expression len(o). Changed in version 2.5: These functions returned an int type. This might require changes in your code for properly supporting 64-bit systems.

int **PyMapping\_DelItemString**(PyObject \*o, char \*key) Remove the mapping for object key from the object o. Return -1 on failure. This is equivalent to the Python statement del o[key].

int **PyMapping\_DelItem**(PyObject \*o, PyObject \*key) Remove the mapping for object key from the object o. Return -1 on failure. This is equivalent to the Python statement del o[key].

int **PyMapping\_HasKeyString**(PyObject \*o, char \*key) On success, return 1 if the mapping object has the key key and 0 otherwise. This is equivalent to o[key], returning True on success and False on an exception. This function always succeeds.

int **PyMapping\_HasKey**(PyObject \*o, PyObject \*key) Return 1 if the mapping object has the key key and 0 otherwise. This is equivalent to o[key], returning True on success and False on an exception. This function always succeeds.

PyObject\* **PyMapping\_Keys**(PyObject \*o) Return value: New reference. On success, return a list of the keys in object o. On failure, return NULL. This is equivalent to the Python expression o.keys().

PyObject\* **PyMapping\_Values**(PyObject \*o) Return value: New reference. On success, return a list of the values in object o. On failure, return NULL. This is equivalent to the Python expression o.values().

PyObject\* **PyMapping\_Items**(PyObject \*o) Return value: New reference. On success, return a list of the items in object o, where each item is a tuple containing a key-value pair. On failure, return NULL. This is equivalent to the Python expression o.items().

PyObject\* **PyMapping\_GetItemString**(PyObject \*o, char \*key) Return value: New reference. Return element of o corresponding to the object key or NULL on failure. This is the equivalent of the Python expression o[key].

int **PyMapping\_SetItemString**(PyObject \*o, char \*key, PyObject \*v) Map the object key to the value v in object o. Returns -1 on failure. This is the equivalent of the Python statement o[key] = v.

<!-- page: 58 -->

## 6.5 Iterator Protocol

## New in version 2.2.

There are two functions specifically for working with iterators.

## int PyIter\_Check(PyObject \*o)

Return true if the object o supports the iterator protocol.

This function can return a false positive in the case of old-style classes because those classes always define a tp\_iternext slot with logic that either invokes a next() method or raises a TypeError.

## PyObject\* PyIter\_Next(PyObject \*o)

Return value: New reference. Return the next value from the iteration o. The object must be an iterator (it is up to the caller to check this). If there are no remaining values, returns NULL with no exception set. If an error occurs while retrieving the item, returns NULL and passes along the exception.

To write a loop which iterates over an iterator, the C code should look something like this:

```c
PyObject *iterator = PyObject_GetIter(obj);
PyObject *item;

if (iterator == NULL) {
    /* propagate error */
}

while ((item = PyIter_Next(iterator))) {
    /* do something with item */
    ...
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

## 6.6 Old Buffer Protocol

This section describes the legacy buffer protocol, which has been introduced in Python 1.6. It is still supported but deprecated in the Python 2.x series. Python 3 introduces a new buffer protocol which fixes weaknesses and shortcomings of the protocol, and has been backported to Python 2.6. See Buffers and Memoryview Objects for more information.

## int PyObject\_AsCharBuffer(PyObject \*obj, const char \*\*buffer, Py\_ssize\_t \*buffer\_len)

Returns a pointer to a read-only memory location usable as character-based input. The obj argument must support the single-segment character buffer interface. On success, returns 0, sets buffer to the memory location and buffer\_len to the buffer length. Returns -1 and sets a TypeError on error.

New in version 1.6.

Changed in version 2.5: This function used an int \* type for buffer\_len. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 59 -->

int **PyObject\_AsReadBuffer**(PyObject \*obj, const void \*\*buffer, Py\_ssize\_t \*buffer\_len) Returns a pointer to a read-only memory location containing arbitrary data. The obj argument must support the single-segment readable buffer interface. On success, returns 0, sets buffer to the memory location and buffer\_len to the buffer length. Returns -1 and sets a TypeError on error.

New in version 1.6.

Changed in version 2.5: This function used an int \* type for buffer\_len. This might require changes in your code for properly supporting 64-bit systems.

int **PyObject\_CheckReadBuffer**(PyObject \*o) Returns 1 if o supports the single-segment readable buffer interface. Otherwise returns 0.

New in version 2.2.

int **PyObject\_AsWriteBuffer**(PyObject \*obj, void \*\*buffer, Py\_ssize\_t \*buffer\_len) Returns a pointer to a writeable memory location. The obj argument must support the single-segment, character buffer interface. On success, returns 0, sets buffer to the memory location and buffer\_len to the buffer length. Returns -1 and sets a TypeError on error.

New in version 1.6.

Changed in version 2.5: This function used an int \* type for buffer\_len. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 60 -->

<!-- page: 61 -->

# CONCRETE OBJECTS LAYER

The functions in this chapter are specific to certain Python object types. Passing them an object of the wrong type is not a good idea; if you receive an object from a Python program and you are not sure that it has the right type, you must perform a type check first; for example, to check that an object is a dictionary, use PyDict\_Check(). The chapter is structured like the “family tree” of Python object types.

**Warning:** While the functions described in this chapter carefully check the type of the objects which are passed in, many of them do not check for NULL being passed instead of a valid object. Allowing NULL to be passed in can cause memory access violations and immediate termination of the interpreter.

## 7.1 Fundamental Objects

This section describes Python type objects and the singleton object None.

## 7.1.1 Type Objects

## PyTypeObject

The C structure of the objects used to describe built-in types.

## PyObject\* PyType\_Type

This is the type object for type objects; it is the same object as type and types.TypeType in the Python layer.

## int PyType\_Check(PyObject \*o)

Return true if the object o is a type object, including instances of types derived from the standard type object. Return false in all other cases.

## int PyType\_CheckExact (PyObject \*o)

Return true if the object o is a type object, but not a subtype of the standard type object. Return false in all other cases.

New in version 2.2.

## unsigned int PyType\_ClearCache()

Clear the internal lookup cache. Return the current version tag.

New in version 2.6.

## void PyType\_Modified(PyTypeObject \*type)

Invalidate the internal lookup cache for the type and all of its subtypes. This function must be called after any manual modification of the attributes or base classes of the type.

New in version 2.6.

<!-- page: 62 -->

## int PyType\_HasFeature(PyObject \*o, int feature)

Return true if the type object o sets the feature feature. Type features are denoted by single bit flags.

## int PyType\_IS\_GC(PyObject \*o)

Return true if the type object includes support for the cycle detector; this tests the type flag Py\_TPFLAGS\_HAVE\_GC.

New in version 2.0.

## int PyType\_IsSubtype(PyTypeObject \*a, PyTypeObject \*b)

Return true if a is a subtype of b.

New in version 2.2.

This function only checks for actual subtypes, which means that \_\_subclasscheck\_\_() is not called on b. Call PyObject\_IsSubclass() to do the same check that issubclass() would do.

## PyObject\* PyType\_GenericAlloc(PyTypeObject \*type, Py\_ssize\_t nitems)

Return value: New reference. New in version 2.2.

Changed in version 2.5: This function used an int type for nitems. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyType\_GenericNew(PyTypeObject \*type, PyObject \*args, PyObject \*kwds)

Return value: New reference. New in version 2.2.

## int PyType\_Ready(PyTypeObject \*type)

Finalize a type object. This should be called on all type objects to finish their initialization. This function is responsible for adding inherited slots from a type’s base class. Return 0 on success, or return -1 and sets an exception on error.

New in version 2.2.

## 7.1.2 The None Object

Note that the PyTypeObject for None is not directly exposed in the Python/C API. Since None is a singleton, testing for object identity (using == in C) is sufficient. There is no PyNone\_Check() function for the same reason.

## PyObject\* Py\_None

The Python None object, denoting lack of value. This object has no methods. It needs to be treated just like any other object with respect to reference counts.

## Py\_RETURN\_NONE

Properly handle returning Py\_None from within a C function.

New in version 2.4.

## 7.2 Numeric Objects

## 7.2.1 Plain Integer Objects

## PyIntObject

This subtype of PyObject represents a Python integer object.

## PyTypeObject PyInt\_Type

This instance of PyTypeObject represents the Python plain integer type. This is the same object as int and types.IntType.

<!-- page: 63 -->

int **PyInt\_Check**(PyObject \*o)

Return true if o is of type PyInt\_Type or a subtype of PyInt\_Type.

Changed in version 2.2: Allowed subtypes to be accepted.

int **PyInt\_CheckExact**(PyObject \*o)

Return true if o is of type PyInt\_Type, but not a subtype of PyInt\_Type.

New in version 2.2.

## PyObject\* PyInt\_FromString(char \*str, char \*\*pend, int base)

Return value: New reference. Return a new PyIntObject or PyLongObject based on the string value in str, which is interpreted according to the radix in base. If pend is non-NULL, \*pend will point to the first character in str which follows the representation of the number. If base is 0, the radix will be determined based on the leading characters of str: if str starts with '0x' or '0X', radix 16 will be used; if str starts with '0', radix 8 will be used; otherwise radix 10 will be used. If base is not 0, it must be between 2 and 36, inclusive. Leading spaces are ignored. If there are no digits, ValueError will be raised. If the string represents a number too large to be contained within the machine’s long int type and overflow warnings are being suppressed, a PyLongObject will be returned. If overflow warnings are not being suppressed, NULL will be returned in this case.

## PyObject\* PyInt\_FromLong(long ival)

Return value: New reference. Create a new integer object with a value of ival.

The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object. So it should be possible to change the value of 1. I suspect the behaviour of Python in this case is undefined. :-)

## PyObject\* PyInt\_FromSsize\_t(Py\_ssize\_t ival)

Return value: New reference. Create a new integer object with a value of ival. If the value is larger than LONG\_MAX or smaller than LONG\_MIN, a long integer object is returned.

New in version 2.5.

PyObject\* **PyInt\_FromSize\_t**(size\_t ival) Create a new integer object with a value of ival. If the value exceeds LONG\_MAX, a long integer object is returned. New in version 2.5.

long **PyInt\_AsLong**(PyObject \*io) Will first attempt to cast the object to a PyIntObject, if it is not already one, and then return its value. If there is an error, -1 is returned, and the caller should check PyErr\_Occurred() to find out whether there was an error, or whether the value just happened to be -1.

long **PyInt\_AS\_LONG**(PyObject \*io) Return the value of the object io. No error checking is performed.

unsigned long **PyInt\_AsUnsignedLongMask**(PyObject \*io) Will first attempt to cast the object to a PyIntObject or PyLongObject, if it is not already one, and then return its value as unsigned long. This function does not check for overflow. New in version 2.3.

unsigned PY\_LONG\_LONG **PyInt\_AsUnsignedLongLongMask**(PyObject \*io) Will first attempt to cast the object to a PyIntObject or PyLongObject, if it is not already one, and then return its value as unsigned long long, without checking for overflow.

New in version 2.3.

Py\_ssize\_t **PyInt\_AsSsize\_t**(PyObject \*io) Will first attempt to cast the object to a PyIntObject or PyLongObject, if it is not already one, and then return its value as Py\_ssize\_t. New in version 2.5.

<!-- page: 64 -->

## long PyInt\_GetMax()

Return the system’s idea of the largest integer it can handle (LONG\_MAX, as defined in the system header files).

## int PyInt\_ClearFreeList()

Clear the integer free list. Return the number of items that could not be freed.

New in version 2.6.

## 7.2.2 Boolean Objects

Booleans in Python are implemented as a subclass of integers. There are only two booleans, Py\_False and Py\_True. As such, the normal creation and deletion functions don’t apply to booleans. The following macros are available, however.

## int PyBool\_Check(PyObject \*o)

Return true if o is of type PyBool\_Type.

New in version 2.3.

## PyObject\* Py\_False

The Python False object. This object has no methods. It needs to be treated just like any other object with respect to reference counts.

## PyObject\* Py\_True

The Python True object. This object has no methods. It needs to be treated just like any other object with respect to reference counts.

## Py\_RETURN\_FALSE

Return Py\_False from a function, properly incrementing its reference count.

New in version 2.4.

## Py\_RETURN\_TRUE

Return Py\_True from a function, properly incrementing its reference count.

New in version 2.4.

## PyObject\* PyBool\_FromLong(long v)

Return value: New reference. Return a new reference to Py\_True or Py\_False depending on the truth value of v.

New in version 2.3.

## 7.2.3 Long Integer Objects

## PyLongObject

This subtype of PyObject represents a Python long integer object.

## PyTypeObject PyLong\_Type

This instance of PyTypeObject represents the Python long integer type. This is the same object as long and types.LongType.

## int PyLong\_Check(PyObject \*p)

Return true if its argument is a PyLongObject or a subtype of PyLongObject.

Changed in version 2.2: Allowed subtypes to be accepted.

## int PyLong\_CheckExact(PyObject \*p)

Return true if its argument is a PyLongObject, but not a subtype of PyLongObject.

New in version 2.2.

<!-- page: 65 -->

PyObject\* PyLong\_FromLong(long v) Return value: New reference. Return a new PyLongObject object from v, or NULL on failure.

PyObject\* PyLong\_FromUnsignedLong(unsigned long v) Return value: New reference. Return a new PyLongObject object from a C unsigned long, or NULL on failure.

PyObject\* PyLong\_FromSsize\_t(Py\_ssize\_t v) Return value: New reference. Return a new PyLongObject object from a C Py\_ssize\_t, or NULL on failure. New in version 2.6.

PyObject\* PyLong\_FromSize\_t(size\_t v) Return value: New reference. Return a new PyLongObject object from a C size\_t, or NULL on failure. New in version 2.6.

PyObject\* PyLong\_FromLongLong(PY\_LONG\_LONG v) Return value: New reference. Return a new PyLongObject object from a C long long, or NULL on failure.

PyObject\* PyLong\_FromUnsignedLongLong(unsigned PY\_LONG\_LONG v) Return value: New reference. Return a new PyLongObject object from a C unsigned long long, or NULL on failure.

PyObject\* PyLong\_FromDouble(double v) Return value: New reference. Return a new PyLongObject object from the integer part of v, or NULL on failure.

PyObject\* PyLong\_FromString(char \*str, char \*\*pend, int base) Return value: New reference. Return a new PyLongObject based on the string value in str, which is interpreted according to the radix in base. If pend is non-NULL, \*pend will point to the first character in str which follows the representation of the number. If base is 0, the radix will be determined based on the leading characters of str: if str starts with '0x' or '0X', radix 16 will be used; if str starts with '0', radix 8 will be used; otherwise radix 10 will be used. If base is not 0, it must be between 2 and 36, inclusive. Leading spaces are ignored. If there are no digits, ValueError will be raised.

PyObject\* PyLong\_FromUnicode(Py\_UNICODE \*u, Py\_ssize\_t length, int base) Return value: New reference. Convert a sequence of Unicode digits to a Python long integer value. The first parameter, u, points to the first character of the Unicode string, length gives the number of characters, and base is the radix for the conversion. The radix must be in the range [2, 36]; if it is out of range, ValueError will be raised.

New in version 1.6. Changed in version 2.5: This function used an int for length. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PyLong\_FromVoidPtr(void \*p) Return value: New reference. Create a Python integer or long integer from the pointer p. The pointer value can be retrieved from the resulting value using PyLong\_AsVoidPtr(). New in version 1.5.2.

long PyLong\_AsLong(PyObject \*pylong) Return a C long representation of the contents of pylong. If pylong is greater than LONG\_MAX, an OverflowError is raised and -1 will be returned.

long PyLong\_AsLongAndOverflow(PyObject \*pylong, int \*overflow) Return a C long representation of the contents of pylong. If pylong is greater than LONG\_MAX or less than LONG\_MIN, set \*overflow to 1 or -1, respectively, and return -1; otherwise, set \*overflow to 0. If any other exception occurs (for example a TypeError or MemoryError), then -1 will be returned and \*overflow will be 0.

<!-- page: 66 -->

PY\_LONG\_LONG PyLong\_AsLongLongAndOverflow(PyObject \*pylong, int \*overflow) Return a C long long representation of the contents of pylong. If pylong is greater than PY\_LLONG\_MAX or less than PY\_LLONG\_MIN, set \*overflow to 1 or -1, respectively, and return -1; otherwise, set \*overflow to 0. If any other exception occurs (for example a TypeError or MemoryError), then -1 will be returned and \*overflow will be 0.

Py\_ssize\_t PyLong\_AsSsize\_t(PyObject \*pylong) Return a C Py\_ssize\_t representation of the contents of pylong. If pylong is greater than PY\_SSIZE\_T\_MAX, an OverflowError is raised and -1 will be returned. New in version 2.6.

unsigned long PyLong\_AsUnsignedLong(PyObject \*pylong) Return a C unsigned long representation of the contents of pylong. If pylong is greater than ULONG\_MAX, an OverflowError is raised.

PY\_LONG\_LONG PyLong\_AsLongLong(PyObject \*pylong) Return a C long long from a Python long integer. If pylong cannot be represented as a long long, an OverflowError is raised and -1 is returned. New in version 2.2.

unsigned PY\_LONG\_LONG PyLong\_AsUnsignedLongLong(PyObject \*pylong) Return a C unsigned long long from a Python long integer. If pylong cannot be represented as an unsigned long long, an OverflowError is raised and (unsigned long long)-1 is returned. New in version 2.2. Changed in version 2.7: A negative pylong now raises OverflowError, not TypeError.

unsigned long PyLong\_AsUnsignedLongMask(PyObject \*io) Return a C unsigned long from a Python long integer, without checking for overflow. Returns (unsigned long)-1 on error. Use PyErr\_Occurred() to disambiguate. New in version 2.3.

unsigned PY\_LONG\_LONG PyLong\_AsUnsignedLongLongMask(PyObject \*io) Return a C unsigned long long from a Python long integer, without checking for overflow. Returns (unsigned PY\_LONG\_LONG)-1 on error. Use PyErr\_Occurred() to disambiguate. New in version 2.3.

double PyLong\_AsDouble(PyObject \*pylong) Return a C double representation of the contents of pylong. If pylong cannot be approximately represented as a double, an OverflowError exception is raised and -1.0 will be returned.

void\* **PyLong\_AsVoidPtr**(PyObject \*pylong) Convert a Python integer or long integer pylong to a C void pointer. If pylong cannot be converted, an OverflowError will be raised. This is only assured to produce a usable void pointer for values created with PyLong\_FromVoidPtr(). New in version 1.5.2. Changed in version 2.5: For values outside 0..LONG\_MAX, both signed and unsigned integers are accepted.

<!-- page: 67 -->

## 7.2.4 Floating Point Objects

**PyFloatObject** This subtype of PyObject represents a Python floating point object. PyTypeObject **PyFloat\_Type** This instance of PyTypeObject represents the Python floating point type. This is the same object as float and types.FloatType. int **PyFloat\_Check**(PyObject \*p) Return true if its argument is a PyFloatObject or a subtype of PyFloatObject. Changed in version 2.2: Allowed subtypes to be accepted. int **PyFloat\_CheckExact**(PyObject \*p) Return true if its argument is a PyFloatObject, but not a subtype of PyFloatObject. New in version 2.2. PyObject\* **PyFloat\_FromString**(PyObject \*str, char \*\*pend) Return value: New reference. Create a PyFloatObject object based on the string value in str, or NULL on failure. The pend argument is ignored. It remains only for backward compatibility. PyObject\* **PyFloat\_FromDouble**(double v) Return value: New reference. Create a PyFloatObject object from v, or NULL on failure. double **PyFloat\_AsDouble**(PyObject \*pyfloat) Return a C double representation of the contents of pyfloat. If pyfloat is not a Python floating point object but has a \_\_float\_\_() method, this method will first be called to convert pyfloat into a float. This method returns -1.0 upon failure, so one should call PyErr\_Occurred() to check for errors. double **PyFloat\_AS\_DOUBLE**(PyObject \*pyfloat) Return a C double representation of the contents of pyfloat, but without error checking. PyObject\* **PyFloat\_GetInfo**(void) Return a structseq instance which contains information about the precision, minimum and maximum values of a float. It’s a thin wrapper around the header file float.h. New in version 2.6. double **PyFloat\_GetMax**() Return the maximum representable finite float DBL\_MAX as C double. New in version 2.6. double **PyFloat\_GetMin**() Return the minimum normalized positive float DBL\_MIN as C double. New in version 2.6. int **PyFloat\_ClearFreeList**() Clear the float free list. Return the number of items that could not be freed. New in version 2.6. void **PyFloat\_AsString**(char \*buf, PyFloatObject \*v) Convert the argument v to a string, using the same rules as str(). The length of buf should be at least 100. This function is unsafe to call because it writes to a buffer whose length it does not know. Deprecated since version 2.7: Use PyObject\_Str() or PyOS\_double\_to\_string() instead. void **PyFloat\_AsReprString**(char \*buf, PyFloatObject \*v) Same as PyFloat\_AsString, except uses the same rules as repr(). The length of buf should be at least 100.

<!-- page: 68 -->

This function is unsafe to call because it writes to a buffer whose length it does not know.

Deprecated since version 2.7: Use PyObject\_Repr() or PyOS\_double\_to\_string() instead.

## 7.2.5 Complex Number Objects

Python’s complex number objects are implemented as two distinct types when viewed from the C API: one is the Python object exposed to Python programs, and the other is a C structure which represents the actual complex number value. The API provides functions for working with both.

## Complex Numbers as C Structures

Note that the functions which accept these structures as parameters and return them as results do so by value rather than dereferencing them through pointers. This is consistent throughout the API.

## Py\_complex

The C structure which corresponds to the value portion of a Python complex number object. Most of the functions for dealing with complex number objects use structures of this type as input or output values, as appropriate. It is defined as:

```txt
typedef struct {
    double real;
    double imag;
} Py_complex;
```

Py\_complex **\_Py\_c\_sum**(Py\_complex left, Py\_complex right) Return the sum of two complex numbers, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_diff**(Py\_complex left, Py\_complex right) Return the difference between two complex numbers, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_neg**(Py\_complex complex) Return the negation of the complex number complex, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_prod**(Py\_complex left, Py\_complex right) Return the product of two complex numbers, using the C Py\_complex representation.

Py\_complex **\_Py\_c\_quot**(Py\_complex dividend, Py\_complex divisor) Return the quotient of two complex numbers, using the C Py\_complex representation.

If divisor is null, this method returns zero and sets errno to EDOM.

Py\_complex **\_Py\_c\_pow**(Py\_complex num, Py\_complex exp) Return the exponentiation of num by exp, using the C Py\_complex representation. If num is null and exp is not a positive real number, this method returns zero and sets errno to EDOM.

<!-- page: 69 -->

## Complex Numbers as Python Objects

## PyComplexObject

This subtype of PyObject represents a Python complex number object.

## PyTypeObject PyComplex\_Type

This instance of PyTypeObject represents the Python complex number type. It is the same object as complex and types.ComplexType.

## int PyComplex\_Check(PyObject \*p)

Return true if its argument is a PyComplexObject or a subtype of PyComplexObject.

Changed in version 2.2: Allowed subtypes to be accepted.

## int PyComplex\_CheckExact(PyObject \*p)

Return true if its argument is a PyComplexObject, but not a subtype of PyComplexObject.

New in version 2.2.

## PyObject\* PyComplex\_FromCComplex(Py\_complex v)

Return value: New reference. Create a new Python complex number object from a C Py\_complex value.

## PyObject\* PyComplex\_FromDoubles(double real, double imag)

Return value: New reference. Return a new PyComplexObject object from real and imag.

double **PyComplex\_RealAsDouble**(PyObject \*op)

Return the real part of op as a C double.

double **PyComplex\_ImagAsDouble**(PyObject \*op)

Return the imaginary part of op as a C double.

## Py\_complex PyComplex\_AsCComplex(PyObject \*op)

Return the Py\_complex value of the complex number op. Upon failure, this method returns -1.0 as a real value.

Changed in version 2.6: If op is not a Python complex number object but has a \_\_complex\_\_() method, this method will first be called to convert op to a Python complex number object.

## 7.3 Sequence Objects

Generic operations on sequence objects were discussed in the previous chapter; this section deals with the specific kinds of sequence objects that are intrinsic to the Python language.

## 7.3.1 Byte Array Objects

New in version 2.6.

## PyByteArrayObject

This subtype of PyObject represents a Python bytearray object.

## PyTypeObject PyByteArray\_Type

This instance of PyTypeObject represents the Python bytearray type; it is the same object as bytearray in the Python layer.

<!-- page: 70 -->

```txt
PyObject* PyByteArray_FromObject (PyObject *o)
    Return a new bytearray object from any object, o, that implements the buffer protocol.
PyObject* PyByteArray_FromStringAndSize (const char *string, Py_ssize_t len)
    Create a new bytearray object from string and its length, len. On failure, NULL is returned.
PyObject* PyByteArray_Concat (PyObject *a, PyObject *b)
    Concat bytearrays a and b and return a new bytearray with the result.
Py_ssize_t PyByteArray_Size (PyObject *bytearray)
    Return the size of bytearray after checking for a NULL pointer.
char* PyByteArray_AsString (PyObject *bytearray)
    Return the contents of bytearray as a char array after checking for a NULL pointer.
int PyByteArray_Resize (PyObject *bytearray, Py_ssize_t len)
    Resize the internal buffer of bytearray to len.
```

## Type check macros

Return true if the object o is a bytearray object or an instance of a subtype of the bytearray type.

int **PyByteArray\_CheckExact**(PyObject \*o)

Return true if the object o is a bytearray object, but not an instance of a subtype of the bytearray type.

## Direct API functions

## Macros

These macros trade safety for speed and they don’t check pointers.

char\* **PyByteArray\_AS\_STRING**(PyObject \*bytearray)

Py\_ssize\_t **PyByteArray\_GET\_SIZE**(PyObject \*bytearray)

## 7.3.2 String/Bytes Objects

These functions raise TypeError when expecting a string parameter and are called with a non-string parameter.

**Note:** These functions have been renamed to PyBytes\_\* in Python 3.x. Unless otherwise noted, the PyBytes functions available in 3.x are aliased to their PyString\_\* equivalents to help porting.

**PyStringObject** This subtype of PyObject represents a Python string object.

PyTypeObject **PyString\_Type** This instance of PyTypeObject represents the Python string type; it is the same object as str and types. StringType in the Python layer. .

Changed in version 2.2: Allowed subtypes to be accepted.

<!-- page: 71 -->

int **PyString\_CheckExact**(PyObject \*o)

Return true if the object o is a string object, but not an instance of a subtype of the string type.

New in version 2.2.

PyObject\* **PyString\_FromString**(const char \*v)

Return value: New reference. Return a new string object with a copy of the string v as value on success, and NULL on failure. The parameter v must not be NULL; it will not be checked.

PyObject\* **PyString\_FromStringAndSize**(const char \*v, Py\_ssize\_t len)

Return value: New reference. Return a new string object with a copy of the string v as value and length len on success, and NULL on failure. If v is NULL, the contents of the string are uninitialized.

Changed in version 2.5: This function used an int type for len. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyString\_FromFormat**(const char \*format, ...)

Return value: New reference. Take a C printf()-style format string and a variable number of arguments, calculate the size of the resulting Python string and return a string with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the format string. The following format characters are allowed:

| Format Charac-ters | Type | Comment |
| --- | --- | --- |
| %% | n/a | The literal % character. |
| %c | int | A single character, represented as a C int. |
| %d | int | Exactly equivalent to printf("%d"). |
| %u | un-signed int | Exactly equivalent to printf("%u"). |
| %ld | long | Exactly equivalent to printf("%ld"). |
| %lu | un-signed long | Exactly equivalent to printf("%lu"). |
| %lld | long long | Exactly equivalent to printf("%lld"). |
| %llu | un-signed long long | Exactly equivalent to printf("%llu"). |
| %zd | Py_ssize_t | Exactly equivalent to printf("%zd"). |
| %zu | size_t | Exactly equivalent to printf("%zu"). |
| %i | int | Exactly equivalent to printf("%i"). |
| %x | int | Exactly equivalent to printf("%x"). |
| %s | char* | A null-terminated C character array. |
| %p | void* | The hex representation of a C pointer. Mostly equivalent to printf("%p") ex-cept that it is guaranteed to start with the literal 0x regardless of what the platform's printf yields. |

An unrecognized format character causes all the rest of the format string to be copied as-is to the result string, and any extra arguments discarded.

**Note:** The “%lld” and “%llu” format specifiers are only available when HAVE\_LONG\_LONG is defined.

<!-- page: 72 -->

Changed in version 2.7: Support for “%lld” and “%llu” added.

PyObject\* **PyString\_FromFormatV**(const char \*format, va\_list vargs) Return value: New reference. Identical to PyString\_FromFormat() except that it takes exactly two arguments.

Py\_ssize\_t **PyString\_Size**(PyObject \*string) Return the length of the string in string object string. Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

## Py\_ssize\_t PyString\_GET\_SIZE(PyObject \*string) Macro form of PyString\_Size() but without error checking.

Changed in version 2.5: This macro returned an int type. This might require changes in your code for properly supporting 64-bit systems.

char\* **PyString\_AsString**(PyObject \*string) Return a NUL-terminated representation of the contents of string. The pointer refers to the internal buffer of string, not a copy. The data must not be modified in any way, unless the string was just created using PyString\_FromStringAndSize(NULL, size). It must not be deallocated. If string is a Unicode object, this function computes the default encoding of string and operates on that. If string is not a string object at all, PyString\_AsString() returns NULL and raises TypeError.

char\* **PyString\_AS\_STRING**(PyObject \*string) Macro form of PyString\_AsString() but without error checking. Only string objects are supported; no Unicode objects should be passed.

int **PyString\_AsStringAndSize**(PyObject \*obj, char \*\*buffer, Py\_ssize\_t \*length) Return a NUL-terminated representation of the contents of the object obj through the output variables buffer and length.

The function accepts both string and Unicode objects as input. For Unicode objects it returns the default encoded version of the object. If length is NULL, the resulting buffer may not contain NUL characters; if it does, the function returns -1 and a TypeError is raised.

The buffer refers to an internal string buffer of obj, not a copy. The data must not be modified in any way, unless the string was just created using PyString\_FromStringAndSize(NULL, size). It must not be deallocated. If string is a Unicode object, this function computes the default encoding of string and operates on that. If string is not a string object at all, PyString\_AsStringAndSize() returns -1 and raises TypeError.

Changed in version 2.5: This function used an int \* type for length. This might require changes in your code for properly supporting 64-bit systems.

## void PyString\_Concat(PyObject \*\*string, PyObject \*newpart)

Create a new string object in \*string containing the contents of newpart appended to string; the caller will own the new reference. The reference to the old value of string will be stolen. If the new string cannot be created, the old reference to string will still be discarded and the value of \*string will be set to NULL; the appropriate exception will be set.

## void PyString\_ConcatAndDel(PyObject \*\*string, PyObject \*newpart)

Create a new string object in \*string containing the contents of newpart appended to string. This version decrements the reference count of newpart.

## int \_PyString\_Resize(PyObject \*\*string, Py\_ssize\_t newsize)

A way to resize a string object even though it is “immutable”. Only use this to build up a brand new string object; don’t use this if the string may already be known in other parts of the code. It is an error to call this function if the refcount on the input string object is not one. Pass the address of an existing string object as an lvalue (it may be written into), and the new size desired. On success, \*string holds the resized string object and 0 is returned;

<!-- page: 73 -->

the address in \*string may differ from its input value. If the reallocation fails, the original string object at \*string is deallocated, \*string is set to NULL, a memory exception is set, and -1 is returned.

Changed in version 2.5: This function used an int type for newsize. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyString\_Format**(PyObject \*format, PyObject \*args)

Return value: New reference. Return a new string object from format and args. Analogous to format % args. The args argument must be a tuple or dict.

void **PyString\_InternInPlace**(PyObject \*\*string)

Intern the argument \*string in place. The argument must be the address of a pointer variable pointing to a Python string object. If there is an existing interned string that is the same as \*string, it sets \*string to it (decrementing the reference count of the old string object and incrementing the reference count of the interned string object), otherwise it leaves \*string alone and interns it (incrementing its reference count). (Clarification: even though there is a lot of talk about reference counts, think of this function as reference-count-neutral; you own the object after the call if and only if you owned it before the call.)

**Note:** This function is not available in 3.x and does not have a PyBytes alias.

PyObject\* **PyString\_InternFromString**(const char \*v) Return value: New reference. A combination of PyString\_FromString() and PyString\_InternInPlace(), returning either a new string object that has been interned, or a new (“owned”) reference to an earlier interned string object with the same value.

**Note:** This function is not available in 3.x and does not have a PyBytes alias.

PyObject\* **PyString\_Decode**(const char \*s, Py\_ssize\_t size, const char \*encoding, const char \*errors) Return value: New reference. Create an object by decoding size bytes of the encoded buffer s using the codec registered for encoding. encoding and errors have the same meaning as the parameters of the same name in the unicode() built-in function. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

**Note:** This function is not available in 3.x and does not have a PyBytes alias.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyString\_AsDecodedObject**(PyObject \*str, const char \*encoding, const char \*errors)

Return value: New reference. Decode a string object by passing it to the codec registered for encoding and return the result as Python object. encoding and errors have the same meaning as the parameters of the same name in the string encode() method. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

**Note:** This function is not available in 3.x and does not have a PyBytes alias.

PyObject\* **PyString\_Encode**(const char \*s, Py\_ssize\_t size, const char \*encoding, const char \*errors)

Return value: New reference. Encode the char buffer of the given size by passing it to the codec registered for encoding and return a Python object. encoding and errors have the same meaning as the parameters of the same name in the string encode() method. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

<!-- page: 74 -->

**Note:** This function is not available in 3.x and does not have a PyBytes alias.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyString\_AsEncodedObject(PyObject \*str, const char \*encoding, const char \*errors)

Return value: New reference. Encode a string object using the codec registered for encoding and return the result as Python object. encoding and errors have the same meaning as the parameters of the same name in the string encode() method. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

**Note:** This function is not available in 3.x and does not have a PyBytes alias.

## 7.3.3 Unicode Objects and Codecs

## Unicode Objects

## Unicode Type

These are the basic Unicode object types used for the Unicode implementation in Python:

## Py\_UNICODE

This type represents the storage type which is used by Python internally as basis for holding Unicode ordinals. Python’s default builds use a 16-bit type for Py\_UNICODE and store Unicode values internally as UCS2. It is also possible to build a UCS4 version of Python (most recent Linux distributions come with UCS4 builds of Python). These builds then use a 32-bit type for Py\_UNICODE and store Unicode data internally as UCS4. On platforms where wchar\_t is available and compatible with the chosen Python Unicode build variant, Py\_UNICODE is a typedef alias for wchar\_t to enhance native platform compatibility. On all other platforms, Py\_UNICODE is a typedef alias for either unsigned short (UCS2) or unsigned long (UCS4).

Note that UCS2 and UCS4 Python builds are not binary compatible. Please keep this in mind when writing extensions or interfaces.

## PyUnicodeObject

This subtype of PyObject represents a Python Unicode object.

## PyTypeObject PyUnicode\_Type

This instance of PyTypeObject represents the Python Unicode type. It is exposed to Python code as unicode and types.UnicodeType.

The following APIs are really C macros and can be used to do fast checks and to access internal read-only data of Unicode objects:

## int PyUnicode\_Check(PyObject \*o)

Return true if the object o is a Unicode object or an instance of a Unicode subtype.

Changed in version 2.2: Allowed subtypes to be accepted.

## int PyUnicode\_CheckExact(PyObject \*o)

Return true if the object o is a Unicode object, but not an instance of a subtype.

New in version 2.2.

## Py\_ssize\_t PyUnicode\_GET\_SIZE(PyObject \*o)

Return the size of the object. o has to be a PyUnicodeObject (not checked).

<!-- page: 75 -->

Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

Py\_ssize\_t **PyUnicode\_GET\_DATA\_SIZE**(PyObject \*o)

Return the size of the object’s internal buffer in bytes. o has to be a PyUnicodeObject (not checked).

Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

Py\_UNICODE\* **PyUnicode\_AS\_UNICODE**(PyObject \*o) Return a pointer to the internal Py\_UNICODE buffer of the object. o has to be a PyUnicodeObject (not checked).

const char\* **PyUnicode\_AS\_DATA**(PyObject \*o)

Return a pointer to the internal buffer of the object. o has to be a PyUnicodeObject (not checked).

int **PyUnicode\_ClearFreeList**()

Clear the free list. Return the total number of freed items.

New in version 2.6.

## Unicode Character Properties

Unicode provides many different character properties. The most often needed ones are available through these macros which are mapped to C functions depending on the Python configuration.

int **Py\_UNICODE\_ISSPACE**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is a whitespace character.

int **Py\_UNICODE\_ISLOWER**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is a lowercase character.

int **Py\_UNICODE\_ISUPPER**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is an uppercase character.

int **Py\_UNICODE\_ISTITLE**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is a titlecase character.

int **Py\_UNICODE\_ISLINEBREAK**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is a linebreak character.

int **Py\_UNICODE\_ISDECIMAL**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is a decimal character.

int **Py\_UNICODE\_ISDIGIT**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is a digit character.

int **Py\_UNICODE\_ISNUMERIC**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is a numeric character.

int **Py\_UNICODE\_ISALPHA**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is an alphabetic character.

int **Py\_UNICODE\_ISALNUM**(Py\_UNICODE ch) Return 1 or 0 depending on whether ch is an alphanumeric character.

These APIs can be used for fast direct character conversions:

Py\_UNICODE **Py\_UNICODE\_TOLOWER**(Py\_UNICODE ch) Return the character ch converted to lower case.

<!-- page: 76 -->

Py\_UNICODE **Py\_UNICODE\_TOUPPER**(Py\_UNICODE ch) Return the character ch converted to upper case.

Py\_UNICODE **Py\_UNICODE\_TOTITLE**(Py\_UNICODE ch) Return the character ch converted to title case.

int **Py\_UNICODE\_TODECIMAL**(Py\_UNICODE ch)

Return the character ch converted to a decimal positive integer. Return -1 if this is not possible. This macro does not raise exceptions.

int **Py\_UNICODE\_TODIGIT**(Py\_UNICODE ch) Return the character ch converted to a single digit integer. Return -1 if this is not possible. This macro does not raise exceptions.

double **Py\_UNICODE\_TONUMERIC**(Py\_UNICODE ch)

Return the character ch converted to a double. Return -1.0 if this is not possible. This macro does not raise exceptions.

## Plain Py\_UNICODE

To create Unicode objects and access their basic sequence properties, use these APIs:

PyObject\* **PyUnicode\_FromUnicode**(const Py\_UNICODE \*u, Py\_ssize\_t size)

Return value: New reference. Create a Unicode object from the Py\_UNICODE buffer u of the given size. u may be NULL which causes the contents to be undefined. It is the user’s responsibility to fill in the needed data. The buffer is copied into the new object. If the buffer is not NULL, the return value might be a shared object. Therefore, modification of the resulting Unicode object is only allowed when u is NULL.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_FromStringAndSize**(const char \*u, Py\_ssize\_t size)

Return value: New reference. Create a Unicode object from the char buffer u. The bytes will be interpreted as being UTF-8 encoded. u may also be NULL which causes the contents to be undefined. It is the user’s responsibility to fill in the needed data. The buffer is copied into the new object. If the buffer is not NULL, the return value might be a shared object. Therefore, modification of the resulting Unicode object is only allowed when u is NULL.

New in version 2.6.

PyObject \***PyUnicode\_FromString**(const char \*u)

Return value: New reference. Create a Unicode object from a UTF-8 encoded null-terminated char buffer u.

New in version 2.6.

PyObject\* **PyUnicode\_FromFormat**(const char \*format, ...)

Return value: New reference. Take a C printf()-style format string and a variable number of arguments, calculate the size of the resulting Python unicode string and return a string with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the format string. The following format characters are allowed:

<!-- page: 77 -->

| Format Characters | Type | Comment |
| --- | --- | --- |
| %% | n/a | The literal % character. |
| %c | int | A single character, represented as a C int. |
| %d | int | Exactly equivalent to printf("%d"). |
| %u | unsigned int | Exactly equivalent to printf("%u"). |
| %ld | long | Exactly equivalent to printf("%ld"). |
| %lu | unsigned long | Exactly equivalent to printf("%lu"). |
| %zd | Py_ssize_t | Exactly equivalent to printf("%zd"). |
| %zu | size_t | Exactly equivalent to printf("%zu"). |
| %i | int | Exactly equivalent to printf("%i"). |
| %x | int | Exactly equivalent to printf("%x"). |
| %s | char* | A null-terminated C character array. |
| %p | void* | The hex representation of a C pointer. Mostly equivalent to printf("%p") except that it is guaranteed to start with the literal 0x regardless of what the platform's printf yields. |
| %U | PyObject* | A unicode object. |
| %V | PyObject*, char * | A unicode object (which may be NULL) and a null-terminated C character array as a second parameter (which will be used, if the first parameter is NULL). |
| %S | PyObject* | The result of calling PyObject_Unicode(). |
| %R | PyObject* | The result of calling PyObject_Repr(). |

An unrecognized format character causes all the rest of the format string to be copied as-is to the result string, and any extra arguments discarded.

New in version 2.6.

PyObject\* **PyUnicode\_FromFormatV**(const char \*format, va\_list vargs) Return value: New reference. Identical to PyUnicode\_FromFormat() except that it takes exactly two arguments.

New in version 2.6.

## Py\_UNICODE\* PyUnicode\_AsUnicode(PyObject \*unicode)

Return a read-only pointer to the Unicode object’s internal Py\_UNICODE buffer, NULL if unicode is not a Unicode object. Note that the resulting Py\_UNICODE\* string may contain embedded null characters, which would cause the string to be truncated when used in most C functions.

## Py\_ssize\_t PyUnicode\_GetSize(PyObject \*unicode)

Return the length of the Unicode object.

Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyUnicode\_FromEncodedObject(PyObject \*obj, const char \*encoding, const char \*errors)

Return value: New reference. Coerce an encoded object obj to a Unicode object and return a reference with incremented refcount.

String and other char buffer compatible objects are decoded according to the given encoding and using the error handling defined by errors. Both can be NULL to have the interface use the default values (see the next section for details).

All other objects, including Unicode objects, cause a TypeError to be set.

The API returns NULL if there was an error. The caller is responsible for decref’ing the returned objects.

## PyObject\* PyUnicode\_FromObject(PyObject \*obj)

Return value: New reference. Shortcut for PyUnicode\_FromEncodedObject(obj, NULL,

<!-- page: 78 -->

"strict") which is used throughout the interpreter whenever coercion to Unicode is needed.

If the platform supports wchar\_t and provides a header file wchar.h, Python can interface directly to this type using the following functions. Support is optimized if Python’s own Py\_UNICODE type is identical to the system’s wchar\_t.

## wchar\_t Support

wchar\_t support for platforms which support it:

PyObject\* **PyUnicode\_FromWideChar**(const wchar\_t \*w, Py\_ssize\_t size)

Return value: New reference. Create a Unicode object from the wchar\_t buffer w of the given size. Return NULL on failure.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

Py\_ssize\_t **PyUnicode\_AsWideChar**(PyUnicodeObject \*unicode, wchar\_t \*w, Py\_ssize\_t size)

Copy the Unicode object contents into the wchar\_t buffer w. At most size wchar\_t characters are copied (excluding a possibly trailing 0-termination character). Return the number of wchar\_t characters copied or -1 in case of an error. Note that the resulting wchar\_t string may or may not be 0-terminated. It is the responsibility of the caller to make sure that the wchar\_t string is 0-terminated in case this is required by the application. Also, note that the wchar\_t\* string might contain null characters, which would cause the string to be truncated when used with most C functions.

Changed in version 2.5: This function returned an int type and used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

## Built-in Codecs

Python provides a set of built-in codecs which are written in C for speed. All of these codecs are directly usable via the following functions.

Many of the following APIs take two arguments encoding and errors, and they have the same semantics as the ones of the built-in unicode() Unicode object constructor.

Setting encoding to NULL causes the default encoding to be used which is ASCII. The file system calls should use Py\_FileSystemDefaultEncoding as the encoding for file names. This variable should be treated as read-only: on some systems, it will be a pointer to a static string, on others, it will change at run-time (such as when the application invokes setlocale).

Error handling is set by errors which may also be set to NULL meaning to use the default handling defined for the codec. Default error handling for all built-in codecs is “strict” (ValueError is raised).

The codecs all use a similar interface. Only deviation from the following generic ones are documented for simplicity.

## Generic Codecs

These are the generic codec APIs:

PyObject\* **PyUnicode\_Decode**(const char \*s, Py\_ssize\_t size, const char \*encoding, const char \*errors)

Return value: New reference. Create a Unicode object by decoding size bytes of the encoded string s. encoding and errors have the same meaning as the parameters of the same name in the unicode() built-in function. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 79 -->

PyObject\* **PyUnicode\_Encode**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*encoding, const char \*er-

Return value: New reference. Encode the Py\_UNICODE buffer s of the given size and return a Python string object. encoding and errors have the same meaning as the parameters of the same name in the Unicode encode() method. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsEncodedString**(PyObject \*unicode, const char \*encoding, const char \*errors)

Return value: New reference. Encode a Unicode object and return the result as Python string object. encoding and errors have the same meaning as the parameters of the same name in the Unicode encode() method. The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec.

## UTF-8 Codecs

These are the UTF-8 codec APIs:

PyObject\* **PyUnicode\_DecodeUTF8**(const char \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Create a Unicode object by decoding size bytes of the UTF-8 encoded string s. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_DecodeUTF8Stateful**(const char \*s, Py\_ssize\_t size, const char \*errors, Py\_ssize\_t \*consumed)

Return value: New reference. If consumed is NULL, behave like PyUnicode\_DecodeUTF8(). If consumed is not NULL, trailing incomplete UTF-8 byte sequences will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

New in version 2.4.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_EncodeUTF8**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer s of the given size using UTF-8 and return a Python string object. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsUTF8String**(PyObject \*unicode)

Return value: New reference. Encode a Unicode object using UTF-8 and return the result as Python string object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

<!-- page: 80 -->

## UTF-32 Codecs

These are the UTF-32 codec APIs:

PyObject\* **PyUnicode\_DecodeUTF32**(const char \*s, Py\_ssize\_t size, const char \*errors, int \*byteorder) Decode size bytes from a UTF-32 encoded buffer string and return the corresponding Unicode object. errors (if non-NULL) defines the error handling. It defaults to “strict”.

If byteorder is non-NULL, the decoder starts decoding using the given byte order:

```txt
*byteorder == -1: little endian
*byteorder == 0: native order
*byteorder == 1: big endian
```

If \*byteorder is zero, and the first four bytes of the input data are a byte order mark (BOM), the decoder switches to this byte order and the BOM is not copied into the resulting Unicode string. If \*byteorder is -1 or 1, any byte order mark is copied to the output.

After completion, \*byteorder is set to the current byte order at the end of input data.

In a narrow build code points outside the BMP will be decoded as surrogate pairs.

If byteorder is NULL, the codec starts in native order mode.

Return NULL if an exception was raised by the codec.

New in version 2.6.

PyObject\* **PyUnicode\_DecodeUTF32Stateful**(const char \*s, Py\_ssize\_t size, const char \*errors, int \*by-

If consumed is NULL, behave like PyUnicode\_DecodeUTF32(). If consumed is not NULL, PyUnicode\_DecodeUTF32Stateful() will not treat trailing incomplete UTF-32 byte sequences (such as a number of bytes not divisible by four) as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

New in version 2.6.

PyObject\* **PyUnicode\_EncodeUTF32**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*errors, int byteorder)

Return a Python bytes object holding the UTF-32 encoded value of the Unicode data in s. Output is written according to the following byte order:

```txt
byteorder == -1: little endian
byteorder == 0: native byte order (writes a BOM mark)
byteorder == 1: big endian
```

If byteorder is 0, the output string will always start with the Unicode BOM mark (U+FEFF). In the other two modes, no BOM mark is prepended.

If Py\_UNICODE\_WIDE is not defined, surrogate pairs will be output as a single code point.

Return NULL if an exception was raised by the codec.

New in version 2.6.

PyObject\* **PyUnicode\_AsUTF32String**(PyObject \*unicode)

Return a Python string using the UTF-32 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return NULL if an exception was raised by the codec.

New in version 2.6.

<!-- page: 81 -->

## UTF-16 Codecs

These are the UTF-16 codec APIs:

PyObject\* **PyUnicode\_DecodeUTF16**(const char \*s, Py\_ssize\_t size, const char \*errors, int \*byteorder) Return value: New reference. Decode size bytes from a UTF-16 encoded buffer string and return the corresponding Unicode object. errors (if non-NULL) defines the error handling. It defaults to “strict”.

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

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_DecodeUTF16Stateful**(const char \*s, Py\_ssize\_t size, const char \*errors, int \*by-

Return value: New reference. If consumed is NULL, behave like PyUnicode\_DecodeUTF16(). If consumed is not NULL, PyUnicode\_DecodeUTF16Stateful() will not treat trailing incomplete UTF-16 byte sequences (such as an odd number of bytes or a split surrogate pair) as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

New in version 2.4.

Changed in version 2.5: This function used an int type for size and an int \* type for consumed. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_EncodeUTF16**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*errors, int byte-

Return value: New reference. Return a Python string object holding the UTF-16 encoded value of the Unicode data in s. Output is written according to the following byte order:

```txt
byteorder == -1: little endian
byteorder == 0: native byte order (writes a BOM mark)
byteorder == 1: big endian
```

If byteorder is 0, the output string will always start with the Unicode BOM mark (U+FEFF). In the other two modes, no BOM mark is prepended.

If Py\_UNICODE\_WIDE is defined, a single Py\_UNICODE value may get represented as a surrogate pair. If it is not defined, each Py\_UNICODE values is interpreted as a UCS-2 character.

Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsUTF16String**(PyObject \*unicode)

Return value: New reference. Return a Python string using the UTF-16 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return NULL if an exception was raised by the codec.

<!-- page: 82 -->

## UTF-7 Codecs

These are the UTF-7 codec APIs:

PyObject\* **PyUnicode\_DecodeUTF7**(const char \*s, Py\_ssize\_t size, const char \*errors)

Create a Unicode object by decoding size bytes of the UTF-7 encoded string s. Return NULL if an exception was raised by the codec.

PyObject\* **PyUnicode\_DecodeUTF7Stateful**(const char \*s, Py\_ssize\_t size, const char \*errors,

Py\_ssize\_t \*consumed)

If consumed is NULL, behave like PyUnicode\_DecodeUTF7(). If consumed is not NULL, trailing incomplete UTF-7 base-64 sections will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in consumed.

PyObject\* **PyUnicode\_EncodeUTF7**(const Py\_UNICODE \*s, Py\_ssize\_t size, int base64SetO,

int base64WhiteSpace, const char \*errors)

Encode the Py\_UNICODE buffer of the given size using UTF-7 and return a Python bytes object. Return NULL if an exception was raised by the codec.

If base64SetO is nonzero, “Set O” (punctuation that has no otherwise special meaning) will be encoded in base-64. If base64WhiteSpace is nonzero, whitespace will be encoded in base-64. Both are set to zero for the Python “utf-7” codec.

## Unicode-Escape Codecs

These are the “Unicode Escape” codec APIs:

PyObject\* **PyUnicode\_DecodeUnicodeEscape**(const char \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Create a Unicode object by decoding size bytes of the Unicode-Escape encoded string s. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_EncodeUnicodeEscape**(const Py\_UNICODE \*s, Py\_ssize\_t size)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using Unicode-Escape and return a Python string object. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsUnicodeEscapeString**(PyObject \*unicode)

Return value: New reference. Encode a Unicode object using Unicode-Escape and return the result as Python string object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

## Raw-Unicode-Escape Codecs

These are the “Raw Unicode Escape” codec APIs:

PyObject\* **PyUnicode\_DecodeRawUnicodeEscape**(const char \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Create a Unicode object by decoding size bytes of the Raw-Unicode-Escape encoded string s. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 83 -->

PyObject\* **PyUnicode\_EncodeRawUnicodeEscape**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Encode the Py\_ \_UNICODE buffer of the given size using Raw-Unicode-Escape and return a Python string object. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsRawUnicodeEscapeString**(PyObject \*unicode)

Return value: New reference. Encode a Unicode object using Raw-Unicode-Escape and return the result as Python string object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

## Latin-1 Codecs

These are the Latin-1 codec APIs: Latin-1 corresponds to the first 256 Unicode ordinals and only these are accepted by the codecs during encoding.

PyObject\* **PyUnicode\_DecodeLatin1**(const char \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Create a Unicode object by decoding size bytes of the Latin-1 encoded string s. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_EncodeLatin1**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using Latin-1 and return a Python string object. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsLatin1String**(PyObject \*unicode)

Return value: New reference. Encode a Unicode object using Latin-1 and return the result as Python string object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

## ASCII Codecs

These are the ASCII codec APIs. Only 7-bit ASCII data is accepted. All other codes generate errors.

PyObject\* **PyUnicode\_DecodeASCII**(const char \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Create a Unicode object by decoding size bytes of the ASCII encoded string s. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_EncodeASCII**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using ASCII and return a Python string object. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsASCIIString**(PyObject \*unicode)

Return value: New reference. Encode a Unicode object using ASCII and return the result as Python string object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

<!-- page: 84 -->

## Character Map Codecs

This codec is special in that it can be used to implement many different codecs (and this is in fact what was done to obtain most of the standard codecs included in the encodings package). The codec uses mapping to encode and decode characters.

Decoding mappings must map single string characters to single Unicode characters, integers (which are then interpreted as Unicode ordinals) or None (meaning “undefined mapping” and causing an error).

Encoding mappings must map single Unicode characters to single string characters, integers (which are then interpreted as Latin-1 ordinals) or None (meaning “undefined mapping” and causing an error).

The mapping objects provided must only support the \_\_getitem\_\_ mapping interface.

If a character lookup fails with a LookupError, the character is copied as-is meaning that its ordinal value will be interpreted as Unicode or Latin-1 ordinal resp. Because of this, mappings only need to contain those mappings which map characters to different code points.

These are the mapping codec APIs:

PyObject\* **PyUnicode\_DecodeCharmap**(const char \*s, Py\_ssize\_t size, PyObject \*mapping, const char \*er-

rors)

Return value: New reference. Create a Unicode object by decoding size bytes of the encoded string s using the given mapping object. Return NULL if an exception was raised by the codec. If mapping is NULL latin-1 decoding will be done. Else it can be a dictionary mapping byte or a unicode string, which is treated as a lookup table. Byte values greater that the length of the string and U+FFFE “characters” are treated as “undefined mapping”.

Changed in version 2.4: Allowed unicode string as mapping argument.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_EncodeCharmap**(const Py\_UNICODE \*s, Py\_ssize\_t size, PyObject \*mapping, const char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using the given mapping object and return a Python string object. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsCharmapString**(PyObject \*unicode, PyObject \*mapping)

Return value: New reference. Encode a Unicode object using the given mapping object and return the result as Python string object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

The following codec API is special in that maps Unicode to Unicode.

PyObject\* **PyUnicode\_TranslateCharmap**(const Py\_UNICODE \*s, Py\_ssize\_t size, PyObject \*table, const char \*errors)

Return value: New reference. Translate a Py\_UNICODE buffer of the given size by applying a character mapping table to it and return the resulting Unicode object. Return NULL when an exception was raised by the codec.

The mapping table must map Unicode ordinal integers to Unicode ordinal integers or None (causing deletion of the character).

Mapping tables need only provide the \_\_getitem\_\_() interface; dictionaries and sequences work well. Unmapped character ordinals (ones which cause a LookupError) are left untouched and are copied as-is.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 85 -->

## MBCS codecs for Windows

These are the MBCS codec APIs. They are currently only available on Windows and use the Win32 MBCS converters to implement the conversions. Note that MBCS (or DBCS) is a class of encodings, not just one. The target encoding is defined by the user settings on the machine running the codec.

PyObject\* **PyUnicode\_DecodeMBCS**(const char \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Create a Unicode object by decoding size bytes of the MBCS encoded string s. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_DecodeMBCSStateful**(const char \*s, int size, const char \*errors, int \*consumed)

If consumed is NULL, behave like PyUnicode\_DecodeMBCS(). If consumed is not NULL, PyUnicode\_DecodeMBCSStateful() will not decode trailing lead byte and the number of bytes that have been decoded will be stored in consumed.

New in version 2.5.

PyObject\* **PyUnicode\_EncodeMBCS**(const Py\_UNICODE \*s, Py\_ssize\_t size, const char \*errors)

Return value: New reference. Encode the Py\_UNICODE buffer of the given size using MBCS and return a Python string object. Return NULL if an exception was raised by the codec.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_AsMBCSString**(PyObject \*unicode)

Return value: New reference. Encode a Unicode object using MBCS and return the result as Python string object. Error handling is “strict”. Return NULL if an exception was raised by the codec.

## Methods & Slots

## Methods and Slot Functions

The following APIs are capable of handling Unicode objects and strings on input (we refer to them as strings in the descriptions) and return Unicode objects or integers as appropriate.

They all return NULL or -1 if an exception occurs.

PyObject\* **PyUnicode\_Concat**(PyObject \*left, PyObject \*right)

Return value: New reference. Concat two strings giving a new Unicode string.

PyObject\* **PyUnicode\_Split**(PyObject \*s, PyObject \*sep, Py\_ssize\_t maxsplit)

Return value: New reference. Split a string giving a list of Unicode strings. If sep is NULL, splitting will be done at all whitespace substrings. Otherwise, splits occur at the given separator. At most maxsplit splits will be done. If negative, no limit is set. Separators are not included in the resulting list.

Changed in version 2.5: This function used an int type for maxsplit. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyUnicode\_Splitlines**(PyObject \*s, int keepend)

Return value: New reference. Split a Unicode string at line breaks, returning a list of Unicode strings. CRLF is considered to be one line break. If keepend is 0, the Line break characters are not included in the resulting strings.

PyObject\* **PyUnicode\_Translate**(PyObject \*str, PyObject \*table, const char \*errors)

Return value: New reference. Translate a string by applying a character mapping table to it and return the resulting Unicode object.

<!-- page: 86 -->

The mapping table must map Unicode ordinal integers to Unicode ordinal integers or None (causing deletion of the character).

Mapping tables need only provide the \_\_getitem\_\_() interface; dictionaries and sequences work well. Unmapped character ordinals (ones which cause a LookupError) are left untouched and are copied as-is.

errors has the usual meaning for codecs. It may be NULL which indicates to use the default error handling.

## PyObject\* PyUnicode\_Join(PyObject \*separator, PyObject \*seq)

Return value: New reference. Join a sequence of strings using the given separator and return the resulting Unicode string.

Py\_ssize\_t **PyUnicode\_Tailmatch**(PyObject \*str, PyObject \*substr, Py\_ssize\_t start, Py\_ssize\_t end, int di-

Return 1 if substr matches str[start:end] at the given tail end (direction == -1 means to do a prefix match, direction == 1 a suffix match), 0 otherwise. Return -1 if an error occurred.

Changed in version 2.5: This function used an int type for start and end. This might require changes in your code for properly supporting 64-bit systems.

## Py\_ssize\_t PyUnicode\_Find(PyObject \*str, PyObject \*substr, Py\_ssize\_t start, Py\_ssize\_t end, int direction)

Return the first position of substr in str[start:end] using the given direction (direction == 1 means to do a forward search, direction == -1 a backward search). The return value is the index of the first match; a value of -1 indicates that no match was found, and -2 indicates that an error occurred and an exception has been set.

Changed in version 2.5: This function used an int type for start and end. This might require changes in your code for properly supporting 64-bit systems.

## Py\_ssize\_t PyUnicode\_Count(PyObject \*str, PyObject \*substr, Py\_ssize\_t start, Py\_ssize\_t end)

Return the number of non-overlapping occurrences of substr in str[start:end]. Return -1 if an error occurred.

Changed in version 2.5: This function returned an int type and used an int type for start and end. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyUnicode\_Replace(PyObject \*str, PyObject \*substr, PyObject \*replstr, Py\_ssize\_t maxcount)

Return value: New reference. Replace at most maxcount occurrences of substr in str with replstr and return the resulting Unicode object. maxcount == -1 means replace all occurrences.

Changed in version 2.5: This function used an int type for maxcount. This might require changes in your code for properly supporting 64-bit systems.

## int PyUnicode\_Compare(PyObject \*left, PyObject \*right)

Compare two strings and return -1, 0, 1 for less than, equal, and greater than, respectively.

## int PyUnicode\_RichCompare(PyObject \*left, PyObject \*right, int op)

Rich compare two unicode strings and return one of the following:

• NULL in case an exception was raised

• Py\_True or Py\_False for successful comparisons

• Py\_NotImplemented in case the type combination is unknown

Note that Py\_EQ and Py\_NE comparisons can cause a UnicodeWarning in case the conversion of the arguments to Unicode fails with a UnicodeDecodeError.

Possible values for op are Py\_GT, Py\_GE, Py\_EQ, Py\_NE, Py\_LT, and Py\_LE.

## PyObject\* PyUnicode\_Format(PyObject \*format, PyObject \*args)

Return value: New reference. Return a new string object from format and args; this is analogous to format % args.

<!-- page: 87 -->

int **PyUnicode\_Contains**(PyObject \*container, PyObject \*element)

Check whether element is contained in container and return true or false accordingly.

element has to coerce to a one element Unicode string. -1 is returned if there was an error.

## 7.3.4 Buffers and Memoryview Objects

Python objects implemented in C can export a group of functions called the “buffer interface.” These functions can be used by an object to expose its data in a raw, byte-oriented format. Clients of the object can use the buffer interface to access the object data directly, without needing to copy it first.

Two examples of objects that support the buffer interface are strings and arrays. The string object exposes the character contents in the buffer interface’s byte-oriented form. An array can only expose its contents via the old-style buffer interface. This limitation does not apply to Python 3, where memoryview objects can be constructed from arrays, too. Array elements may be multi-byte values.

An example user of the buffer interface is the file object’s write() method. Any object that can export a series of bytes through the buffer interface can be written to a file. There are a number of format codes to PyArg\_ParseTuple() that operate against an object’s buffer interface, returning data from the target object.

Starting from version 1.6, Python has been providing Python-level buffer objects and a C-level buffer API so that any built-in or used-defined type can expose its characteristics. Both, however, have been deprecated because of various shortcomings, and have been officially removed in Python 3 in favour of a new C-level buffer API and a new Python-level object named memoryview.

The new buffer API has been backported to Python 2.6, and the memoryview object has been backported to Python 2.7. It is strongly advised to use them rather than the old APIs, unless you are blocked from doing so for compatibility reasons.

## The new-style Py\_buffer struct

## Py\_buffer

void \***buf** A pointer to the start of the memory for the object.

Py\_ssize\_t **len** The total length of the memory in bytes.

int **readonly** An indicator of whether the buffer is read only.

A NULL terminated string in struct module style syntax giving the contents of the elements available through the buffer. If this is NULL, "B" (unsigned bytes) is assumed.

The number of dimensions the memory represents as a multi-dimensional array. If it is 0, strides and suboffsets must be NULL.

\_ssize\_t \*shape An array of Py\_ssize\_ts the length of ndim giving the shape of the memory as a multi-dimensional array. Note that ((\*shape)[0] \* ... \* (\*shape)[ndims-1])\*itemsize should be equal to len.

An array of Py\_ssize\_ts the length of ndim giving the number of bytes to skip to get to a new element in each dimension.

<!-- page: 88 -->

## Py\_ssize\_t \*suboffsets

An array of Py\_ssize\_ts the length of ndim. If these suboffset numbers are greater than or equal to 0, then the value stored along the indicated dimension is a pointer and the suboffset value dictates how many bytes to add to the pointer after de-referencing. A suboffset value that it negative indicates that no de-referencing should occur (striding in a contiguous memory block).

If all suboffsets are negative (i.e. no de-referencing is needed), then this field must be NULL (the default value).

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

## Py\_ssize\_t itemsize

This is a storage for the itemsize (in bytes) of each element of the shared memory. It is technically unnecessary as it can be obtained using PyBuffer\_SizeFromFormat(), however an exporter may know this information without parsing the format string and it is necessary to know the itemsize for proper interpretation of striding. Therefore, storing it is more convenient and faster.

## void \*internal

This is for use internally by the exporting object. For example, this might be re-cast as an integer by the exporter and used to store flags about whether or not the shape, strides, and suboffsets arrays must be freed when the buffer is released. The consumer should never alter this value.

## Buffer related functions

## int PyObject\_CheckBuffer(PyObject \*obj)

Return 1 if obj supports the buffer interface otherwise 0.

## int PyObject\_GetBuffer(PyObject \*obj, Py\_buffer \*view, int flags)

Export obj into a Py\_buffer, view. These arguments must never be NULL. The flags argument is a bit field indicating what kind of buffer the caller is prepared to deal with and therefore what kind of buffer the exporter is allowed to return. The buffer interface allows for complicated memory sharing possibilities, but some caller may not be able to handle all the complexity but may want to see if the exporter will let them take a simpler view to its memory.

Some exporters may not be able to share memory in every possible way and may need to raise errors to signal to some consumers that something is just not possible. These errors should be a BufferError unless there is another error that is actually causing the problem. The exporter can use flags information to simplify how much of the Py\_buffer structure is filled in with non-default values and/or raise an error if the object can’t support a simpler view of its memory.

0 is returned on success and -1 on error.

The following table gives possible values to the flags arguments.

<!-- page: 89 -->

| Flag | Description |
| --- | --- |
| PyBUF_SIMPLE | This is the default flag state. The returned buffer may or may not have writable memory. The format of the data will be assumed to be unsigned bytes. This is a "stand-alone" flag constant. It never needs to be '\|'d to the others. The exporter will raise an error if it cannot provide such a contiguous buffer of bytes. |
| PyBUF_WRITABLE | The returned buffer must be writable. If it is not writable, then raise an error. |
| PyBUF_STRIDES | This implies PyBUF_ND. The returned buffer must provide strides information (i.e. the strides cannot be NULL). This would be used when the consumer can handle strided, discontiguous arrays. Handling strides automatically assumes you can handle shape. The exporter can raise an error if a strided representation of the data is not possible (i.e. without the suboffsets). |
| PyBUF_ND | The returned buffer must provide shape information. The memory will be assumed C-style contiguous (last dimension varies the fastest). The exporter may raise an error if it cannot provide this kind of contiguous buffer. If this is not given then shape will be NULL. |
| PyBUF_C_CONTIGPyBUF_F_CONTIGPyBUF_ANY_CONT | UOTUhSese flags indicate that the contiguity returned buffer must be respectively, C-UOcoUnStiguous (last dimension varies the fastest), Fortran contiguous (first dimension varies IGthUeOfUasStest)oreitherone. All ofthese flagsimply PyBUF_STRIDES andguarantee that the strides buffer info structure will be filled in correctly. |
| PyBUF_INDIRECT | This flag indicates the returned buffer must have suboffsets information (which can be NULL if no suboffsets are needed). This can be used when the consumer can handle indirect array referencing implied by these suboffsets. This implies PyBUF_STRIDES. |
| PyBUF_FORMAT | Thereturnedbuffermusthavetrueformatinformationifthisflagisprovided. Thiswould be used when the consumer is going to be checking for what 'kind' of data is actually stored. An exporter should always be able to provide this information if requested. If format is not explicitly requested then the format must be returned as NULL (which means 'B', or unsigned bytes) |
| PyBUF_STRIDED | This is equivalent to (PyBUF_STRIDES \| PyBUF_WRITABLE). |
| PyBUF_STRIDED_ | ROThis is equivalent to (PyBUF_STRIDES). |
| PyBUF_RECORDS | This is equivalent to (PyBUF_STRIDES \| PyBUF_FORMAT \| PyBUF_WRITABLE). |
| PyBUF_RECORDS_ | ROThis is equivalent to (PyBUF_STRIDES \| PyBUF_FORMAT). |
| PyBUF_FULL | This is equivalent to (PyBUF_INDIRECT \| PyBUF_FORMAT \| PyBUF_WRITABLE). |
| PyBUF_FULL_RO | This is equivalent to (PyBUF_INDIRECT \| PyBUF_FORMAT). |
| PyBUF_CONTIG | This is equivalent to (PyBUF_ND \| PyBUF_WRITABLE). |
| PyBUF_CONTIG_R | OThis is equivalent to (PyBUF_ND). |

## void PyBuffer\_Release(Py\_buffer \*view)

Release the buffer view. This should be called when the buffer is no longer being used as it may free memory from it.

## Py\_ssize\_t PyBuffer\_SizeFromFormat(const char \*)

Return the implied itemsize from the struct-stype format.

## int PyBuffer\_IsContiguous(Py\_buffer \*view, char fortran)

Return 1 if the memory defined by the view is C-style (fortran is 'C') or Fortran-style (fortran is 'F') contiguous or either one (fortran is 'A'). Return 0 otherwise.

## void PyBuffer\_FillContiguousStrides(int ndims, Py\_ssize\_t \*shape, Py\_ssize\_t \*strides, int itemsize, char fortran)

Fill the strides array with byte-strides of a contiguous (C-style if fortran is 'C' or Fortran-style if fortran is 'F') array of the given shape with the given number of bytes per element.

<!-- page: 90 -->

int **PyBuffer\_FillInfo**(Py\_buffer \*view, PyObject \*obj, void \*buf, Py\_ssize\_t len, int readonly, int infoflags)

Fill in a buffer-info structure, view, correctly for an exporter that can only share a contiguous chunk of memory of “unsigned bytes” of the given length. Return 0 on success and -1 (with raising an error) on error.

## MemoryView objects

## New in version 2.7.

A memoryview object exposes the new C level buffer interface as a Python object which can then be passed around like any other object.

## PyObject \*PyMemoryView\_FromObject(PyObject \*obj)

Create a memoryview object from an object that defines the new buffer interface.

## PyObject \*PyMemoryView\_FromBuffer(Py\_buffer \*view)

Create a memoryview object wrapping the given buffer-info structure view. The memoryview object then owns the buffer, which means you shouldn’t try to release it yourself: it will be released on deallocation of the memoryview object.

## PyObject \*PyMemoryView\_GetContiguous(PyObject \*obj, int buffertype, char order)

Create a memoryview object to a contiguous chunk of memory (in either ‘C’ or ‘F’ortran order) from an object that defines the buffer interface. If memory is contiguous, the memoryview object points to the original memory. Otherwise copy is made and the memoryview points to a new bytes object.

## int PyMemoryView\_Check(PyObject \*obj)

Return true if the object obj is a memoryview object. It is not currently allowed to create subclasses of memoryview.

## Py\_buffer \*PyMemoryView\_GET\_BUFFER(PyObject \*obj)

Return a pointer to the buffer-info structure wrapped by the given object. The object **must** be a memoryview instance; this macro doesn’t check its type, you must do it yourself or you will risk crashes.

## Old-style buffer objects

More information on the old buffer interface is provided in the section Buffer Object Structures, under the description for PyBufferProcs.

A “buffer object” is defined in the bufferobject.h header (included by Python.h). These objects look very similar to string objects at the Python programming level: they support slicing, indexing, concatenation, and some other standard string operations. However, their data can come from one of two sources: from a block of memory, or from another object which exports the buffer interface.

Buffer objects are useful as a way to expose the data from another object’s buffer interface to the Python programmer. They can also be used as a zero-copy slicing mechanism. Using their ability to reference a block of memory, it is possible to expose any data to the Python programmer quite easily. The memory could be a large, constant array in a C extension, it could be a raw block of memory for manipulation before passing to an operating system library, or it could be used to pass around structured data in its native, in-memory format.

## PyBufferObject

This subtype of PyObject represents a buffer object.

## PyTypeObject PyBuffer\_Type

The instance of PyTypeObject which represents the Python buffer type; it is the same object as buffer and types.BufferType in the Python layer. .

## int Py\_END\_OF\_BUFFER

This constant may be passed as the size parameter to PyBuffer\_FromObject() or

<!-- page: 91 -->

PyBuffer\_FromReadWriteObject(). It indicates that the new PyBufferObject should refer to base object from the specified offset to the end of its exported buffer. Using this enables the caller to avoid querying the base object for its length.

## int PyBuffer\_Check(PyObject \*p)

Return true if the argument has type PyBuffer\_Type.

## PyObject\* PyBuffer\_FromObject(PyObject \*base, Py\_ssize\_t offset, Py\_ssize\_t size)

Return value: New reference. Return a new read-only buffer object. This raises TypeError if base doesn’t support the read-only buffer protocol or doesn’t provide exactly one buffer segment, or it raises ValueError if offset is less than zero. The buffer will hold a reference to the base object, and the buffer’s contents will refer to the base object’s buffer interface, starting as position offset and extending for size bytes. If size is Py\_END\_OF\_BUFFER, then the new buffer’s contents extend to the length of the base object’s exported buffer data.

Changed in version 2.5: This function used an int type for offset and size. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyBuffer\_FromReadWriteObject(PyObject \*base, Py\_ssize\_t offset, Py\_ssize\_t size)

Return value: New reference. Return a new writable buffer object. Parameters and exceptions are similar to those for PyBuffer\_FromObject(). If the base object does not export the writeable buffer protocol, then TypeError is raised.

Changed in version 2.5: This function used an int type for offset and size. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyBuffer\_FromMemory(void \*ptr, Py\_ssize\_t size)

Return value: New reference. Return a new read-only buffer object that reads from a specified location in memory, with a specified size. The caller is responsible for ensuring that the memory buffer, passed in as ptr, is not deallocated while the returned buffer object exists. Raises ValueError if size is less than zero. Note that Py\_END\_OF\_BUFFER may not be passed for the size parameter; ValueError will be raised in that case.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyBuffer\_FromReadWriteMemory(void \*ptr, Py\_ssize\_t size)

Return value: New reference. Similar to PyBuffer\_FromMemory(), but the returned buffer is writable.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

## PyObject\* PyBuffer\_New(Py\_ssize\_t size)

Return value: New reference. Return a new writable buffer object that maintains its own memory buffer of size bytes. ValueError is returned if size is not zero or positive. Note that the memory buffer (as returned by PyObject\_AsWriteBuffer()) is not specifically aligned.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

## 7.3.5 Tuple Objects

## PyTupleObject

This subtype of PyObject represents a Python tuple object.

## PyTypeObject PyTuple\_Type

This instance of PyTypeObject represents the Python tuple type; it is the same object as tuple and types. TupleType in the Python layer..

## int PyTuple\_Check(PyObject \*p)

Return true if p is a tuple object or an instance of a subtype of the tuple type.

<!-- page: 92 -->

Changed in version 2.2: Allowed subtypes to be accepted.

int PyTuple\_CheckExact(PyObject \*p) Return true if p is a tuple object, but not an instance of a subtype of the tuple type. New in version 2.2.

PyObject\* PyTuple\_New(Py\_ssize\_t len) Return value: New reference. Return a new tuple object of size len, or NULL on failure. Changed in version 2.5: This function used an int type for len. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PyTuple\_Pack(Py\_ssize\_t n, ...) Return value: New reference. Return a new tuple object of size n, or NULL on failure. The tuple values are initialized to the subsequent n C arguments pointing to Python objects. PyTuple\_Pack(2, a, b) is equivalent to Py\_BuildValue("(OO)", a, b). New in version 2.4. Changed in version 2.5: This function used an int type for n. This might require changes in your code for properly supporting 64-bit systems.

Py\_ssize\_t PyTuple\_Size(PyObject \*p) Take a pointer to a tuple object, and return the size of that tuple. Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

Py\_ssize\_t PyTuple\_GET\_SIZE(PyObject \*p) Return the size of the tuple p, which must be non-NULL and point to a tuple; no error checking is performed. Changed in version 2.5: This function returned an int type. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PyTuple\_GetItem(PyObject \*p, Py\_ssize\_t pos) Return value: Borrowed reference. Return the object at position pos in the tuple pointed to by p. If pos is out of bounds, return NULL and set an IndexError exception. Changed in version 2.5: This function used an int type for pos. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PyTuple\_GET\_ITEM(PyObject \*p, Py\_ssize\_t pos) Return value: Borrowed reference. Like PyTuple\_GetItem(), but does no checking of its arguments. Changed in version 2.5: This function used an int type for pos. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* PyTuple\_GetSlice(PyObject \*p, Py\_ssize\_t low, Py\_ssize\_t high) Return value: New reference. Return the slice of the tuple pointed to by p between low and high, or NULL on failure. This is the equivalent of the Python expression p[low:high]. Indexing from the end of the list is not supported. Changed in version 2.5: This function used an int type for low and high. This might require changes in your code for properly supporting 64-bit systems.

int PyTuple\_SetItem(PyObject \*p, Py\_ssize\_t pos, PyObject \*o) Insert a reference to object o at position pos of the tuple pointed to by p. Return 0 on success. If pos is out of bounds, return -1 and set an IndexError exception.

<!-- page: 93 -->

**Note:** This function “steals” a reference to o and discards a reference to an item already in the tuple at the affected position.

Changed in version 2.5: This function used an int type for pos. This might require changes in your code for properly supporting 64-bit systems.

## void PyTuple\_SET\_ITEM(PyObject \*p, Py\_ssize\_t pos, PyObject \*o)

Like PyTuple\_SetItem(), but does no error checking, and should only be used to fill in brand new tuples.

**Note:** This macro “steals” a reference to o, and, unlike PyTuple\_SetItem(), does not discard a reference to any item that is being replaced; any reference in the tuple at position pos will be leaked.

Changed in version 2.5: This function used an int type for pos. This might require changes in your code for properly supporting 64-bit systems.

## int \_PyTuple\_Resize(PyObject \*\*p, Py\_ssize\_t newsize)

Can be used to resize a tuple. newsize will be the new length of the tuple. Because tuples are supposed to be immutable, this should only be used if there is only one reference to the object. Do not use this if the tuple may already be known to some other part of the code. The tuple will always grow or shrink at the end. Think of this as destroying the old tuple and creating a new one, only more efficiently. Returns 0 on success. Client code should never assume that the resulting value of \*p will be the same as before calling this function. If the object referenced by \*p is replaced, the original \*p is destroyed. On failure, returns -1 and sets \*p to NULL, and raises MemoryError or SystemError.

Changed in version 2.2: Removed unused third parameter, last\_is\_sticky.

Changed in version 2.5: This function used an int type for newsize. This might require changes in your code for properly supporting 64-bit systems.

## int PyTuple\_ClearFreeList()

Clear the free list. Return the total number of freed items.

New in version 2.6.

## 7.3.6 List Objects

## PyListObject

This subtype of PyObject represents a Python list object.

## PyTypeObject PyList\_Type

This instance of PyTypeObject represents the Python list type. This is the same object as list in the Python layer.

## int PyList\_Check(PyObject \*p)

Return true if p is a list object or an instance of a subtype of the list type.

Changed in version 2.2: Allowed subtypes to be accepted.

## int PyList\_CheckExact(PyObject \*p)

Return true if p is a list object, but not an instance of a subtype of the list type.

New in version 2.2.

## PyObject\* PyList\_New(Py\_ssize\_t len)

Return value: New reference. Return a new list of length len on success, or NULL on failure.

<!-- page: 94 -->

**Note:** If len is greater than zero, the returned list object’s items are set to NULL. Thus you cannot use abstract API functions such as PySequence\_SetItem() or expose the object to Python code before setting all items to a real object with PyList\_SetItem().

Changed in version 2.5: This function used an int for size. This might require changes in your code for properly supporting 64-bit systems.

Py\_ssize\_t **PyList\_Size**(PyObject \*list) Return the length of the list object in list; this is equivalent to len(list) on a list object. Changed in version 2.5: This function returned an int. This might require changes in your code for properly supporting 64-bit systems.

Py\_ssize\_t **PyList\_GET\_SIZE**(PyObject \*list) Macro form of PyList\_Size() without error checking. Changed in version 2.5: This macro returned an int. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyList\_GetItem**(PyObject \*list, Py\_ssize\_t index) Return value: Borrowed reference. Return the object at position index in the list pointed to by list. The position must be non-negative; indexing from the end of the list is not supported. If index is out of bounds (<0 or >=len(list)), return NULL and set an IndexError exception. Changed in version 2.5: This function used an int for index. This might require changes in your code for properly supporting 64-bit systems.

PyObject\* **PyList\_GET\_ITEM**(PyObject \*list, Py\_ssize\_t i) Return value: Borrowed reference. Macro form of PyList\_GetItem() without error checking.

Changed in version 2.5: This macro used an int for i. This might require changes in your code for properly supporting 64-bit systems.

int **PyList\_SetItem**(PyObject \*list, Py\_ssize\_t index, PyObject \*item) Set the item at index index in list to item. Return 0 on success. If index is out of bounds, return -1 and set an IndexError exception.

**Note:** This function “steals” a reference to item and discards a reference to an item already in the list at the affected position.

Changed in version 2.5: This function used an int for index. This might require changes in your code for properly supporting 64-bit systems.

void **PyList\_SET\_ITEM**(PyObject \*list, Py\_ssize\_t i, PyObject \*o) Macro form of PyList\_SetItem() without error checking. This is normally only used to fill in new lists where there is no previous content.

**Note:** This macro “steals” a reference to item, and, unlike PyList\_SetItem(), does not discard a reference to any item that it being replaced; any reference in list at position i will be leaked.

Changed in version 2.5: This macro used an int for i. This might require changes in your code for properly supporting 64-bit systems.

int **PyList\_Insert**(PyObject \*list, Py\_ssize\_t index, PyObject \*item) Insert the item item into list list in front of index index. Return 0 if successful; return -1 and set an exception if unsuccessful. Analogous to list.insert(index, item).

<!-- page: 95 -->

Changed in version 2.5: This function used an int for index. This might require changes in your code for properly supporting 64-bit systems.

## int PyList\_Append(PyObject \*list, PyObject \*item)

Append the object item at the end of list list. Return 0 if successful; return -1 and set an exception if unsuccessful. Analogous to list.append(item).

## PyObject\* PyList\_GetSlice(PyObject \*list, Py\_ssize\_t low, Py\_ssize\_t high)

Return value: New reference. Return a list of the objects in list containing the objects between low and high. Return NULL and set an exception if unsuccessful. Analogous to list[low:high]. Indexing from the end of the list is not supported.

Changed in version 2.5: This function used an int for low and high. This might require changes in your code for properly supporting 64-bit systems.

## int PyList\_SetSlice(PyObject \*list, Py\_ssize\_t low, Py\_ssize\_t high, PyObject \*itemlist)

Set the slice of list between low and high to the contents of itemlist. Analogous to list[low:high] = itemlist. The itemlist may be NULL, indicating the assignment of an empty list (slice deletion). Return 0 on success, -1 on failure. Indexing from the end of the list is not supported.

Changed in version 2.5: This function used an int for low and high. This might require changes in your code for properly supporting 64-bit systems.

## int PyList\_Sort(PyObject \*list)

Sort the items of list in place. Return 0 on success, -1 on failure. This is equivalent to list.sort().

## int PyList\_Reverse(PyObject \*list)

Reverse the items of list in place. Return 0 on success, -1 on failure. This is the equivalent of list.reverse().

## PyObject\* PyList\_AsTuple(PyObject \*list)

Return value: New reference. Return a new tuple object containing the contents of list; equivalent to tuple(list).

## 7.4 Mapping Objects

## 7.4.1 Dictionary Objects

## PyDictObject

This subtype of PyObject represents a Python dictionary object.

## PyTypeObject PyDict\_Type

This instance of PyTypeObject represents the Python dictionary type. This is exposed to Python programs as dict and types.DictType.

## int PyDict\_Check(PyObject \*p)

Return true if p is a dict object or an instance of a subtype of the dict type.

Changed in version 2.2: Allowed subtypes to be accepted.

## int PyDict\_CheckExact(PyObject \*p)

Return true if p is a dict object, but not an instance of a subtype of the dict type.

New in version 2.4.

## PyObject\* PyDict\_New()

Return value: New reference. Return a new empty dictionary, or NULL on failure.

<!-- page: 96 -->

PyObject\* PyDictProxy\_New(PyObject \*dict) Return value: New reference. Return a proxy object for a mapping which enforces read-only behavior. This is normally used to create a proxy to prevent modification of the dictionary for non-dynamic class types. New in version 2.2.

void PyDict\_Clear(PyObject \*p) Empty an existing dictionary of all key-value pairs.

int PyDict\_Contains(PyObject \*p, PyObject \*key) Determine if dictionary p contains key. If an item in p is matches key, return 1, otherwise return 0. On error, return -1. This is equivalent to the Python expression key in p.

PyObject\* PyDict\_Copy(PyObject \*p) Return value: New reference. Return a new dictionary that contains the same key-value pairs as p. New in version 1.6.

int PyDict\_SetItem(PyObject \*p, PyObject \*key, PyObject \*val) Insert value into the dictionary p with a key of key. key must be hashable; if it isn’t, TypeError will be raised. Return 0 on success or -1 on failure.

int PyDict\_SetItemString(PyObject \*p, const char \*key, PyObject \*val) Insert value into the dictionary p using key as a key. key should be a char\*. The key object is created using PyString\_FromString(key). Return 0 on success or -1 on failure.

int PyDict\_DelItem(PyObject \*p, PyObject \*key) Remove the entry in dictionary p with key key. key must be hashable; if it isn’t, TypeError is raised. Return 0 on success or -1 on failure.

int PyDict\_DelItemString(PyObject \*p, char \*key) Remove the entry in dictionary p which has a key specified by the string key. Return 0 on success or -1 on failure.

PyObject\* PyDict\_GetItem(PyObject \*p, PyObject \*key) Return value: Borrowed reference. Return the object from dictionary p which has a key key. Return NULL if the key key is not present, but without setting an exception.

PyObject\* PyDict\_GetItemString(PyObject \*p, const char \*key) Return value: Borrowed reference. This is the same as PyDict\_GetItem(), but key is specified as a char\*, rather than a PyObject\*.

PyObject\* PyDict\_Items(PyObject \*p) Return value: New reference. Return a PyListObject containing all the items from the dictionary, as in the dictionary method dict.items().

PyObject\* PyDict\_Keys(PyObject \*p) Return value: New reference. Return a PyListObject containing all the keys from the dictionary, as in the dictionary method dict.keys().

PyObject\* PyDict\_Values(PyObject \*p) Return value: New reference. Return a PyListObject containing all the values from the dictionary p, as in the dictionary method dict.values().

Py\_ssize\_t PyDict\_Size(PyObject \*p) Return the number of items in the dictionary. This is equivalent to len(p) on a dictionary.

int PyDict\_Next(PyObject \*p, Py\_ssize\_t \*ppos, PyObject \*\*pkey, PyObject \*\*pvalue) Iterate over all key-value pairs in the dictionary p. The Py\_ssize\_t referred to by ppos must be initialized to 0

<!-- page: 97 -->

prior to the first call to this function to start the iteration; the function returns true for each pair in the dictionary, and false once all pairs have been reported. The parameters pkey and pvalue should either point to PyObject\* variables that will be filled in with each key and value, respectively, or may be NULL. Any references returned through them are borrowed. ppos should not be altered during iteration. Its value represents offsets within the internal dictionary structure, and since the structure is sparse, the offsets are not consecutive.

For example:

```c
PyObject *key, *value;
Py_ssize_t pos = 0;

while (PyDict_Next(self->dict, &pos, &key, &value)) {
    /* do something interesting with the values... */
    ...
}
```

The dictionary p should not be mutated during iteration. It is safe (since Python 2.1) to modify the values of the keys as you iterate over the dictionary, but only so long as the set of keys does not change. For example:

```c
PyObject *key, *value;
Py_ssize_t pos = 0;

while (PyDict_Next(self->dict, &pos, &key, &value)) {
    int i = PyInt_AS_LONG(value) + 1;
    PyObject *o = PyInt_FromLong(i);
    if (o == NULL)
        return -1;
    if (PyDict_SetItem(self->dict, key, o) < 0) {
        Py_DECREF(o);
        return -1;
    }
    Py_DECREF(o);
}
```

Changed in version 2.5: This function used an int \* type for ppos. This might require changes in your code for properly supporting 64-bit systems.

## int PyDict\_Merge(PyObject \*a, PyObject \*b, int override)

Iterate over mapping object b adding key-value pairs to dictionary a. b may be a dictionary, or any object supporting PyMapping\_Keys() and PyObject\_GetItem(). If override is true, existing pairs in a will be replaced if a matching key is found in b, otherwise pairs will only be added if there is not a matching key in a. Return 0 on success or -1 if an exception was raised.

New in version 2.2.

## int PyDict\_Update(PyObject \*a, PyObject \*b)

This is the same as PyDict\_Merge(a, b, 1) in C, and is similar to a.update(b) in Python except that PyDict\_Update() doesn’t fall back to the iterating over a sequence of key value pairs if the second argument has no “keys” attribute. Return 0 on success or -1 if an exception was raised.

New in version 2.2.

## int PyDict\_MergeFromSeq2(PyObject \*a, PyObject \*seq2, int override)

Update or merge into dictionary a, from the key-value pairs in seq2. seq2 must be an iterable object producing iterable objects of length 2, viewed as key-value pairs. In case of duplicate keys, the last wins if override is true, else the first wins. Return 0 on success or -1 if an exception was raised. Equivalent Python (except for the return value):

<!-- page: 98 -->

```python
def PyDict_MergeFromSeq2(a, seq2, override):
    for key, value in seq2:
        if override or key not in a:
            a[key] = value
```

New in version 2.2.

## 7.5 Other Objects

## 7.5.1 Class and Instance Objects

Note that the class objects described here represent old-style classes, which will go away in Python 3. When creating new types for extension modules, you will want to work with type objects (section Type Objects).

## PyClassObject

The C structure of the objects used to describe built-in classes.

## PyObject\* PyClass\_Type

This is the type object for class objects; it is the same object as types.ClassType in the Python layer.

## int PyClass\_Check(PyObject \*o)

Return true if the object o is a class object, including instances of types derived from the standard class object. Return false in all other cases.

## int PyClass\_IsSubclass(PyObject \*klass, PyObject \*base)

Return true if klass is a subclass of base. Return false in all other cases.

There are very few functions specific to instance objects.

## PyTypeObject PyInstance\_Type

Type object for class instances.

## int PyInstance\_Check(PyObject \*obj)

Return true if obj is an instance.

## PyObject\* PyInstance\_New(PyObject \*class, PyObject \*arg, PyObject \*kw)

Return value: New reference. Create a new instance of a specific class. The parameters arg and kw are used as the positional and keyword parameters to the object’s constructor.

## PyObject\* PyInstance\_NewRaw(PyObject \*class, PyObject \*dict)

Return value: New reference. Create a new instance of a specific class without calling its constructor. class is the class of new object. The dict parameter will be used as the object’s \_\_dict\_\_; if NULL, a new dictionary will be created for the instance.

## 7.5.2 Function Objects

There are a few functions specific to Python functions.

## PyFunctionObject

The C structure used for functions.

## PyTypeObject PyFunction\_Type

This is an instance of PyTypeObject and represents the Python function type. It is exposed to Python programmers as types.FunctionType.

## int PyFunction\_Check(PyObject \*o)

Return true if o is a function object (has type PyFunction\_Type). The parameter must not be NULL.

<!-- page: 99 -->

## PyObject\* PyFunction\_New(PyObject \*code, PyObject \*globals)

Return value: New reference. Return a new function object associated with the code object code. globals must be a dictionary with the global variables accessible to the function.

The function’s docstring, name and \_\_module\_\_ are retrieved from the code object, the argument defaults and closure are set to NULL.

## PyObject\* PyFunction\_GetCode(PyObject \*op)

Return value: Borrowed reference. Return the code object associated with the function object op.

## PyObject\* PyFunction\_GetGlobals(PyObject \*op)

Return value: Borrowed reference. Return the globals dictionary associated with the function object op.

## PyObject\* PyFunction\_GetModule(PyObject \*op)

Return value: Borrowed reference. Return the \_\_module\_\_ attribute of the function object op. This is normally a string containing the module name, but can be set to any other object by Python code.

## PyObject\* PyFunction\_GetDefaults(PyObject \*op)

Return value: Borrowed reference. Return the argument default values of the function object op. This can be a tuple of arguments or NULL.

## int PyFunction\_SetDefaults(PyObject \*op, PyObject \*defaults)

Set the argument default values for the function object op. defaults must be Py\_None or a tuple.

Raises SystemError and returns -1 on failure.

## PyObject\* PyFunction\_GetClosure(PyObject \*op)

Return value: Borrowed reference. Return the closure associated with the function object op. This can be NULL or a tuple of cell objects.

## int PyFunction\_SetClosure(PyObject \*op, PyObject \*closure)

Set the closure associated with the function object op. closure must be Py\_None or a tuple of cell objects.

Raises SystemError and returns -1 on failure.

## 7.5.3 Method Objects

There are some useful functions that are useful for working with method objects.

## PyTypeObject PyMethod\_Type

This instance of PyTypeObject represents the Python method type. This is exposed to Python programs as types.MethodType.

## int PyMethod\_Check(PyObject \*o)

Return true if o is a method object (has type PyMethod\_Type). The parameter must not be NULL.

## PyObject\* PyMethod\_New(PyObject \*func, PyObject \*self, PyObject \*class)

Return value: New reference. Return a new method object, with func being any callable object; this is the function that will be called when the method is called. If this method should be bound to an instance, self should be the instance and class should be the class of self, otherwise self should be NULL and class should be the class which provides the unbound method..

## PyObject\* PyMethod\_Class(PyObject \*meth)

Return value: Borrowed reference. Return the class object from which the method meth was created; if this was created from an instance, it will be the class of the instance.

## PyObject\* PyMethod\_GET\_CLASS(PyObject \*meth)

Return value: Borrowed reference. Macro version of PyMethod\_Class() which avoids error checking.

## PyObject\* PyMethod\_Function(PyObject \*meth)

Return value: Borrowed reference. Return the function object associated with the method meth.

<!-- page: 100 -->

## PyObject\* PyMethod\_GET\_FUNCTION(PyObject \*meth)

Return value: Borrowed reference. Macro version of PyMethod\_Function() which avoids error checking.

## PyObject\* PyMethod\_Self(PyObject \*meth)

Return value: Borrowed reference. Return the instance associated with the method meth if it is bound, otherwise return NULL.

## PyObject\* PyMethod\_GET\_SELF(PyObject \*meth)

Return value: Borrowed reference. Macro version of PyMethod\_Self() which avoids error checking.

## int PyMethod\_ClearFreeList()

Clear the free list. Return the total number of freed items.

New in version 2.6.

## 7.5.4 File Objects

Python’s built-in file objects are implemented entirely on the FILE\* support from the C standard library. This is an implementation detail and may change in future releases of Python.

## PyFileObject

This subtype of PyObject represents a Python file object.

## PyTypeObject PyFile\_Type

This instance of PyTypeObject represents the Python file type. This is exposed to Python programs as file and types.FileType.

## int PyFile\_Check(PyObject \*p)

Return true if its argument is a PyFileObject or a subtype of PyFileObject.

Changed in version 2.2: Allowed subtypes to be accepted.

## int PyFile\_CheckExact(PyObject \*p)

Return true if its argument is a PyFileObject, but not a subtype of PyFileObject.

New in version 2.2.

## PyObject\* PyFile\_FromString(char \*filename, char \*mode)

Return value: New reference. On success, return a new file object that is opened on the file given by filename, with a file mode given by mode, where mode has the same semantics as the standard C routine fopen(). On failure, return NULL.

## PyObject\* PyFile\_FromFile(FILE \*fp, char \*name, char \*mode, int (\*close)(FILE\*))

Return value: New reference. Create a new PyFileObject from the already-open standard C file pointer, fp. The function close will be called when the file should be closed. Return NULL and close the file using close on failure. close is optional and can be set to NULL.

## FILE\* PyFile\_AsFile(PyObject \*p)

Return the file object associated with p as a FILE\*.

If the caller will ever use the returned FILE\* object while the GIL is released it must also call the PyFile\_IncUseCount() and PyFile\_DecUseCount() functions described below as appropriate.

## void PyFile\_IncUseCount(PyFileObject \*p)

Increments the PyFileObject’s internal use count to indicate that the underlying FILE\* is being used. This prevents Python from calling f\_close() on it from another thread. Callers of this must call PyFile\_DecUseCount() when they are finished with the FILE\*. Otherwise the file object will never be closed by Python.

The GIL must be held while calling this function.

The suggested use is to call this after PyFile\_AsFile() and before you release the GIL:

<!-- page: 101 -->

```txt
FILE *fp = PyFile_AsFile(p);
PyFile_IncUseCount(p);
/* ... */
Py_BEGIN_ALLOW_THREADS
do_something(fp);
Py_END_ALLOW_THREADS
/* ... */
PyFile_DecUseCount(p);
```

New in version 2.6.

## void PyFile\_DecUseCount(PyFileObject \*p)

Decrements the PyFileObject’s internal unlocked\_count member to indicate that the caller is done with its own use of the FILE\*. This may only be called to undo a prior call to PyFile\_IncUseCount().

The GIL must be held while calling this function (see the example above).

New in version 2.6.

## PyObject\* PyFile\_GetLine(PyObject \*p, int n)

Return value: New reference. Equivalent to p.readline([n]), this function reads one line from the object p. p may be a file object or any object with a readline() method. If n is 0, exactly one line is read, regardless of the length of the line. If n is greater than 0, no more than n bytes will be read from the file; a partial line can be returned. In both cases, an empty string is returned if the end of the file is reached immediately. If n is less than 0, however, one line is read regardless of length, but EOFError is raised if the end of the file is reached immediately.

## PyObject\* PyFile\_Name(PyObject \*p)

Return value: Borrowed reference. Return the name of the file specified by p as a string object.

## void PyFile\_SetBufSize(PyFileObject \*p, int n)

Available on systems with setvbuf() only. This should only be called immediately after file object creation.

## int PyFile\_SetEncoding(PyFileObject \*p, const char \*enc)

Set the file’s encoding for Unicode output to enc. Return 1 on success and 0 on failure.

New in version 2.3.

## int PyFile\_SetEncodingAndErrors(PyFileObject \*p, const char \*enc, \*errors)

Set the file’s encoding for Unicode output to enc, and its error mode to err. Return 1 on success and 0 on failure.

New in version 2.6.

## int PyFile\_SoftSpace(PyObject \*p, int newflag)

This function exists for internal use by the interpreter. Set the softspace attribute of p to newflag and return the previous value. p does not have to be a file object for this function to work properly; any object is supported (thought its only interesting if the softspace attribute can be set). This function clears any errors, and will return 0 as the previous value if the attribute either does not exist or if there were errors in retrieving it. There is no way to detect errors from this function, but doing so should not be needed.

## int PyFile\_WriteObject(PyObject \*obj, PyObject \*p, int flags)

Write object obj to file object p. The only supported flag for flags is Py\_PRINT\_RAW; if given, the str() of the object is written instead of the repr(). Return 0 on success or -1 on failure; the appropriate exception will be set.

## int PyFile\_WriteString(const char \*s, PyObject \*p)

Write string s to file object p. Return 0 on success or -1 on failure; the appropriate exception will be set.

<!-- page: 102 -->

## 7.5.5 Module Objects

There are only a few functions special to module objects.

PyTypeObject **PyModule\_Type** This instance of PyTypeObject represents the Python module type. This is exposed to Python programs as types.ModuleType.

int **PyModule\_Check**(PyObject \*p) Return true if p is a module object, or a subtype of a module object. Changed in version 2.2: Allowed subtypes to be accepted.

## int PyModule\_CheckExact(PyObject \*p)

Return true if p is a module object, but not a subtype of PyModule\_Type.

New in version 2.2.

## PyObject\* PyModule\_New(const char \*name)

Return value: New reference. Return a new module object with the \_\_name\_\_ attribute set to name. Only the module’s \_\_doc\_\_ and \_\_name\_\_ attributes are filled in; the caller is responsible for providing a \_\_file\_\_ attribute.

## PyObject\* PyModule\_GetDict(PyObject \*module)

Return value: Borrowed reference. Return the dictionary object that implements module’s namespace; this object is the same as the \_\_dict\_\_ attribute of the module object. This function never fails. It is recommended extensions use other PyModule\_\*() and PyObject\_\*() functions rather than directly manipulate a module’s dict\_\_.

## char\* PyModule\_GetName(PyObject \*module)

Return module’s \_\_name\_\_ value. If the module does not provide one, or if it is not a string, SystemError is raised and NULL is returned.

## char\* PyModule\_GetFilename(PyObject \*module)

Return the name of the file from which module was loaded using module’s \_\_file\_\_ attribute. If this is not defined, or if it is not a string, raise SystemError and return NULL.

int **PyModule\_AddObject**(PyObject \*module, const char \*name, PyObject \*value) Add an object to module as name. This is a convenience function which can be used from the module’s initialization function. This steals a reference to value. Return -1 on error, 0 on success. New in version 2.0.

int **PyModule\_AddIntConstant**(PyObject \*module, const char \*name, long value) Add an integer constant to module as name. This convenience function can be used from the module’s initialization function. Return -1 on error, 0 on success. New in version 2.0.

int **PyModule\_AddStringConstant**(PyObject \*module, const char \*name, const char \*value) Add a string constant to module as name. This convenience function can be used from the module’s initialization function. The string value must be null-terminated. Return -1 on error, 0 on success.

New in version 2.0.

## int PyModule\_AddIntMacro(PyObject \*module, macro)

Add an int constant to module. The name and the value are taken from macro. For example PyModule\_AddIntMacro(module, AF\_INET) adds the int constant AF\_INET with the value of AF\_INET to module. Return -1 on error, 0 on success.

New in version 2.6.

int **PyModule\_AddStringMacro**(PyObject \*module, macro)

<!-- page: 103 -->

Add a string constant to module.

New in version 2.6.

## 7.5.6 Iterator Objects

Python provides two general-purpose iterator objects. The first, a sequence iterator, works with an arbitrary sequence supporting the \_\_getitem\_\_() method. The second works with a callable object and a sentinel value, calling the callable for each item in the sequence, and ending the iteration when the sentinel value is returned.

## PyTypeObject PySeqIter\_Type

Type object for iterator objects returned by PySeqIter\_New() and the one-argument form of the iter() built-in function for built-in sequence types.

New in version 2.2.

## int PySeqIter\_Check(op)

Return true if the type of op is PySeqIter\_Type.

New in version 2.2.

## PyObject\* PySeqIter\_New(PyObject \*seq)

Return value: New reference. Return an iterator that works with a general sequence object, seq. The iteration ends when the sequence raises IndexError for the subscripting operation.

New in version 2.2.

## PyTypeObject PyCallIter\_Type

Type object for iterator objects returned by PyCallIter\_New() and the two-argument form of the iter() built-in function.

New in version 2.2.

## int PyCallIter\_Check(op)

Return true if the type of op is PyCallIter\_Type.

New in version 2.2.

## PyObject\* PyCallIter\_New(PyObject \*callable, PyObject \*sentinel)

Return value: New reference. Return a new iterator. The first parameter, callable, can be any Python callable object that can be called with no parameters; each call to it should return the next item in the iteration. When callable returns a value equal to sentinel, the iteration will be terminated.

New in version 2.2.

## 7.5.7 Descriptor Objects

“Descriptors” are objects that describe some attribute of an object. They are found in the dictionary of type objects.

## PyTypeObject PyProperty\_Type

The type object for the built-in descriptor types.

New in version 2.2.

PyObject\* **PyDescr\_NewGetSet**(PyTypeObject \*type, struct PyGetSetDef \*getset) Return value: New reference. New in version 2.2.

PyObject\* **PyDescr\_NewMember**(PyTypeObject \*type, struct PyMemberDef \*meth) Return value: New reference. New in version 2.2.

<!-- page: 104 -->

PyObject\* **PyDescr\_NewMethod**(PyTypeObject \*type, struct PyMethodDef \*meth)

Return value: New reference. New in version 2.2.

PyObject\* **PyDescr\_NewWrapper**(PyTypeObject \*type, struct wrapperbase \*wrapper, void \*wrapped) Return value: New reference. New in version 2.2.

PyObject\* **PyDescr\_NewClassMethod**(PyTypeObject \*type, PyMethodDef \*method)

Return value: New reference. New in version 2.3.

int **PyDescr\_IsData**(PyObject \*descr)

Return true if the descriptor objects descr describes a data attribute, or false if it describes a method. descr must be a descriptor object; there is no error checking.

New in version 2.2.

PyObject\* **PyWrapper\_New**(PyObject \*, PyObject \*)

Return value: New reference. New in version 2.2.

## 7.5.8 Slice Objects

PyTypeObject **PySlice\_Type**

The type object for slice objects. This is the same as slice and types.SliceType.

int **PySlice\_Check**(PyObject \*ob)

Return true if ob is a slice object; ob must not be NULL.

PyObject\* **PySlice\_New**(PyObject \*start, PyObject \*stop, PyObject \*step)

Return value: New reference. Return a new slice object with the given values. The start, stop, and step parameters are used as the values of the slice object attributes of the same names. Any of the values may be NULL, in which case the None will be used for the corresponding attribute. Return NULL if the new object could not be allocated.

int **PySlice\_GetIndices**(PySliceObject \*slice, Py\_ssize\_t length, Py\_ssize\_t \*start, Py\_ssize\_t \*stop,

Py\_ssize\_t \*step)

Retrieve the start, stop and step indices from the slice object slice, assuming a sequence of length length. Treats indices greater than length as errors.

Returns 0 on success and -1 on error with no exception set (unless one of the indices was not None and failed to be converted to an integer, in which case -1 is returned with an exception set).

You probably do not want to use this function. If you want to use slice objects in versions of Python prior to 2.3, you would probably do well to incorporate the source of PySlice\_GetIndicesEx(), suitably renamed, in the source of your extension.

Changed in version 2.5: This function used an int type for length and an int \* type for start, stop, and step. This might require changes in your code for properly supporting 64-bit systems.

int **PySlice\_GetIndicesEx**(PySliceObject \*slice, Py\_ssize\_t length, Py\_ssize\_t \*start, Py\_ssize\_t \*stop,

Py\_ssize\_t \*step, Py\_ssize\_t \*slicelength)

Usable replacement for PySlice\_GetIndices(). Retrieve the start, stop, and step indices from the slice object slice assuming a sequence of length length, and store the length of the slice in slicelength. Out of bounds indices are clipped in a manner consistent with the handling of normal slices.

Returns 0 on success and -1 on error with exception set.

New in version 2.3.

Changed in version 2.5: This function used an int type for length and an int \* type for start, stop, step, and slicelength. This might require changes in your code for properly supporting 64-bit systems.

<!-- page: 105 -->

## 7.5.9 Ellipsis Object

## PyObject \*Py\_Ellipsis

The Python Ellipsis object. This object has no methods. It needs to be treated just like any other object with respect to reference counts. Like Py\_None it is a singleton object.

## 7.5.10 Weak Reference Objects

Python supports weak references as first-class objects. There are two specific object types which directly implement weak references. The first is a simple reference object, and the second acts as a proxy for the original object as much as it can.

int **PyWeakref\_Check**(ob) Return true if ob is either a reference or proxy object.

New in version 2.2.

int **PyWeakref\_CheckRef**(ob) Return true if ob is a reference object.

New in version 2.2.

int **PyWeakref\_CheckProxy**(ob)

Return true if ob is a proxy object.

New in version 2.2.

## PyObject\* PyWeakref\_NewRef(PyObject \*ob, PyObject \*callback)

Return value: New reference. Return a weak reference object for the object ob. This will always return a new reference, but is not guaranteed to create a new object; an existing reference object may be returned. The second parameter, callback, can be a callable object that receives notification when ob is garbage collected; it should accept a single parameter, which will be the weak reference object itself. callback may also be None or NULL. If ob is not a weakly-referencable object, or if callback is not callable, None, or NULL, this will return NULL and raise TypeError.

New in version 2.2.

## PyObject\* PyWeakref\_NewProxy(PyObject \*ob, PyObject \*callback)

Return value: New reference. Return a weak reference proxy object for the object ob. This will always return a new reference, but is not guaranteed to create a new object; an existing proxy object may be returned. The second parameter, callback, can be a callable object that receives notification when ob is garbage collected; it should accept a single parameter, which will be the weak reference object itself. callback may also be None or NULL. If ob is not a weakly-referencable object, or if callback is not callable, None, or NULL, this will return NULL and raise TypeError.

New in version 2.2.

## PyObject\* PyWeakref\_GetObject(PyObject \*ref)

Return value: Borrowed reference. Return the referenced object from a weak reference, ref. If the referent is no longer live, returns Py\_None.

New in version 2.2.

**Warning:** This function returns a **borrowed reference** to the referenced object. This means that you should always call Py\_INCREF() on the object except if you know that it cannot be destroyed while you are still using it.

<!-- page: 106 -->

PyObject\* **PyWeakref\_GET\_OBJECT**(PyObject \*ref)

Return value: Borrowed reference. Similar to PyWeakref\_GetObject(), but implemented as a macro that does no error checking.

New in version 2.2.

## 7.5.11 Capsules

Refer to using-capsules for more information on using these objects.

New in version 2.7.

## PyCapsule

This subtype of PyObject represents an opaque value, useful for C extension modules who need to pass an opaque value (as a void\* pointer) through Python code to other C code. It is often used to make a C function pointer defined in one module available to other modules, so the regular import mechanism can be used to access C APIs defined in dynamically loaded modules.

## PyCapsule\_Destructor

The type of a destructor callback for a capsule. Defined as:

```txt
typedef void (*PyCapsule_Destructor)(PyObject *);
```

See PyCapsule\_New() for the semantics of PyCapsule\_Destructor callbacks.

int **PyCapsule\_CheckExact**(PyObject \*p)

Return true if its argument is a PyCapsule.

PyObject\* **PyCapsule\_New**(void \*pointer, const char \*name, PyCapsule\_Destructor destructor)

Return value: New reference. Create a PyCapsule encapsulating the pointer. The pointer argument may not be NULL.

On failure, set an exception and return NULL.

The name string may either be NULL or a pointer to a valid C string. If non-NULL, this string must outlive the capsule. (Though it is permitted to free it inside the destructor.)

If the destructor argument is not NULL, it will be called with the capsule as its argument when it is destroyed.

If this capsule will be stored as an attribute of a module, the name should be specified as modulename. attributename. This will enable other modules to import the capsule using PyCapsule\_Import().

void\* **PyCapsule\_GetPointer**(PyObject \*capsule, const char \*name)

Retrieve the pointer stored in the capsule. On failure, set an exception and return NULL.

The name parameter must compare exactly to the name stored in the capsule. If the name stored in the capsule is NULL, the name passed in must also be NULL. Python uses the C function strcmp() to compare capsule names.

PyCapsule\_Destructor **PyCapsule\_GetDestructor**(PyObject \*capsule)

Return the current destructor stored in the capsule. On failure, set an exception and return NULL.

It is legal for a capsule to have a NULL destructor. This makes a NULL return code somewhat ambiguous; use PyCapsule\_IsValid() or PyErr\_Occurred() to disambiguate.

void\* **PyCapsule\_GetContext**(PyObject \*capsule)

Return the current context stored in the capsule. On failure, set an exception and return NULL.

It is legal for a capsule to have a NULL context. This makes a NULL return code somewhat ambiguous; use PyCapsule\_IsValid() or PyErr\_Occurred() to disambiguate.

<!-- page: 107 -->

const char\* **PyCapsule\_GetName**(PyObject \*capsule) Return the current name stored in the capsule. On failure, set an exception and return NULL.

It is legal for a capsule to have a NULL name. This makes a NULL return code somewhat ambiguous; use PyCapsule\_IsValid() or PyErr\_Occurred() to disambiguate.

void\* **PyCapsule\_Import**(const char \*name, int no\_block)

Import a pointer to a C object from a capsule attribute in a module. The name parameter should specify the full name to the attribute, as in module.attribute. The name stored in the capsule must match this string exactly. If no\_block is true, import the module without blocking (using PyImport\_ImportModuleNoBlock()). If no\_block is false, import the module conventionally (using PyImport\_ImportModule()).

Return the capsule’s internal pointer on success. On failure, set an exception and return NULL.

int **PyCapsule\_IsValid**(PyObject \*capsule, const char \*name)

Determines whether or not capsule is a valid capsule. A valid capsule is non-NULL, passes PyCapsule\_CheckExact(), has a non-NULL pointer stored in it, and its internal name matches the name parameter. (See PyCapsule\_GetPointer() for information on how capsule names are compared.)

In other words, if PyCapsule\_IsValid() returns a true value, calls to any of the accessors (any function starting with PyCapsule\_Get()) are guaranteed to succeed.

Return a nonzero value if the object is valid and matches the name passed in. Return 0 otherwise. This function will not fail.

int **PyCapsule\_SetContext**(PyObject \*capsule, void \*context)

Set the context pointer inside capsule to context.

Return 0 on success. Return nonzero and set an exception on failure.

int **PyCapsule\_SetDestructor**(PyObject \*capsule, PyCapsule\_Destructor destructor) Set the destructor inside capsule to destructor.

Return 0 on success. Return nonzero and set an exception on failure.

int **PyCapsule\_SetName**(PyObject \*capsule, const char \*name) Set the name inside capsule to name. If non-NULL, the name must outlive the capsule. If the previous name stored in the capsule was not NULL, no attempt is made to free it.

Return 0 on success. Return nonzero and set an exception on failure.

int **PyCapsule\_SetPointer**(PyObject \*capsule, void \*pointer)

Set the void pointer inside capsule to pointer. The pointer may not be NULL.

Return 0 on success. Return nonzero and set an exception on failure.

## 7.5.12 CObjects

**Warning:** The CObject API is deprecated as of Python 2.7. Please switch to the new Capsules API.

## PyCObject

This subtype of PyObject represents an opaque value, useful for C extension modules who need to pass an opaque value (as a void\* pointer) through Python code to other C code. It is often used to make a C function pointer defined in one module available to other modules, so the regular import mechanism can be used to access C APIs defined in dynamically loaded modules.

int **PyCObject\_Check**(PyObject \*p)

Return true if its argument is a PyCObject.

<!-- page: 108 -->

PyObject\* **PyCObject\_FromVoidPtr**(void\* cobj, void (\*destr)(void \*))

Return value: New reference. Create a PyCObject from the void \* cobj. The destr function will be called when the object is reclaimed, unless it is NULL.

PyObject\* **PyCObject\_FromVoidPtrAndDesc**(void\* cobj, void\* desc, void (\*destr)(void \*, void \*))

Return value: New reference. Create a PyCObject from the void \* cobj. The destr function will be called when the object is reclaimed. The desc argument can be used to pass extra callback data for the destructor function.

void\* **PyCObject\_AsVoidPtr**(PyObject\* self)

Return the object void \* that the PyCObject self was created with.

void\* **PyCObject\_GetDesc**(PyObject\* self)

Return the description void \* that the PyCObject self was created with.

int **PyCObject\_SetVoidPtr**(PyObject\* self, void\* cobj)

Set the void pointer inside self to cobj. The PyCObject must not have an associated destructor. Return true on success, false on failure.

## 7.5.13 Cell Objects

“Cell” objects are used to implement variables referenced by multiple scopes. For each such variable, a cell object is created to store the value; the local variables of each stack frame that references the value contains a reference to the cells from outer scopes which also use that variable. When the value is accessed, the value contained in the cell is used instead of the cell object itself. This de-referencing of the cell object requires support from the generated byte-code; these are not automatically de-referenced when accessed. Cell objects are not likely to be useful elsewhere.

**PyCellObject**

The C structure used for cell objects.

PyTypeObject **PyCell\_Type** The type object corresponding to cell objects.

int **PyCell\_Check**(ob)

Return true if ob is a cell object; ob must not be NULL.

PyObject\* **PyCell\_New**(PyObject \*ob) (1

Return value: New reference. Create and return a new cell object containing the value ob. The parameter may be NULL.

PyObject\* **PyCell\_Get**(PyObject \*cell) Return value: New reference. Return the contents of the cell cell.

PyObject\* **PyCell\_GET**(PyObject \*cell) Return value: Borrowed reference. Return the contents of the cell cell, but without checking that cell is non-NULL and a cell object.

int **PyCell\_Set**(PyObject \*cell, PyObject \*value) Set the contents of the cell object cell to value. This releases the reference to any current content of the cell. value may be NULL. cell must be non-NULL; if it is not a cell object, -1 will be returned. On success, 0 will be returned.

void **PyCell\_SET**(PyObject \*cell, PyObject \*value) Sets the value of the cell object cell to value. No reference counts are adjusted, and no checks are made for safety; cell must be non-NULL and must be a cell object.

<!-- page: 109 -->

## 7.5.14 Generator Objects

Generator objects are what Python uses to implement generator iterators. They are normally created by iterating over a function that yields values, rather than explicitly calling PyGen\_New().

## PyGenObject

The C structure used for generator objects.

PyTypeObject **PyGen\_Type**

The type object corresponding to generator objects.

int **PyGen\_Check**(ob)

Return true if ob is a generator object; ob must not be NULL.

int **PyGen\_CheckExact**(ob)

Return true if ob’s type is PyGen\_Type is a generator object; ob must not be NULL.

PyObject\* **PyGen\_New**(PyFrameObject \*frame)

Return value: New reference. Create and return a new generator object based on the frame object. A reference to frame is stolen by this function. The parameter must not be NULL.

## 7.5.15 DateTime Objects

Various date and time objects are supplied by the datetime module. Before using any of these functions, the header file datetime.h must be included in your source (note that this is not included by Python.h), and the macro PyDateTime\_IMPORT must be invoked, usually as part of the module initialisation function. The macro puts a pointer to a C structure into a static variable, PyDateTimeAPI, that is used by the following macros.

Type-check macros:

int **PyDate\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateType or a subtype of PyDateTime\_DateType. ob must not be NULL. New in version 2.4.

int **PyDate\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateType. ob must not be NULL. New in version 2.4.

int **PyDateTime\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateTimeType or a subtype of PyDateTime\_DateTimeType. ob must not be NULL. New in version 2.4.

int **PyDateTime\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_DateTimeType. ob must not be NULL. New in version 2.4.

int **PyTime\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_TimeType or a subtype of PyDateTime\_TimeType. ob must not be NULL. New in version 2.4.

int **PyTime\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_TimeType. ob must not be NULL. New in version 2.4.

<!-- page: 110 -->

int **PyDelta\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_DeltaType or a subtype of PyDateTime\_DeltaType. ob must not be NULL. New in version 2.4.

int **PyDelta\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_DeltaType. ob must not be NULL. New in version 2.4.

int **PyTZInfo\_Check**(PyObject \*ob) Return true if ob is of type PyDateTime\_TZInfoType or a subtype of PyDateTime\_TZInfoType. ob must not be NULL. New in version 2.4.

int **PyTZInfo\_CheckExact**(PyObject \*ob) Return true if ob is of type PyDateTime\_TZInfoType. ob must not be NULL. New in version 2.4.

Macros to create objects:

PyObject\* **PyDate\_FromDate**(int year, int month, int day) Return value: New reference. Return a datetime.date object with the specified year, month and day. New in version 2.4.

PyObject\* **PyDateTime\_FromDateAndTime**(int year, int month, int day, int hour, int minute, int second, int usecond) Return value: New reference. Return a datetime.datetime object with the specified year, month, day, hour, minute, second and microsecond. New in version 2.4.

PyObject\* **PyTime\_FromTime**(int hour, int minute, int second, int usecond) Return value: New reference. Return a datetime.time object with the specified hour, minute, second and microsecond. New in version 2.4.

PyObject\* **PyDelta\_FromDSU**(int days, int seconds, int useconds) Return value: New reference. Return a datetime.timedelta object representing the given number of days, seconds and microseconds. Normalization is performed so that the resulting number of microseconds and seconds lie in the ranges documented for datetime.timedelta objects.

Macros to extract fields from date objects. The argument must be an instance of PyDateTime\_Date, including subclasses (such as PyDateTime\_DateTime). The argument must not be NULL, and the type is not checked:

int **PyDateTime\_GET\_YEAR**(PyDateTime\_Date \*o) Return the year, as a positive int. New in version 2.4.

int **PyDateTime\_GET\_MONTH**(PyDateTime\_Date \*o) Return the month, as an int from 1 through 12. New in version 2.4.

int **PyDateTime\_GET\_DAY**(PyDateTime\_Date \*o) Return the day, as an int from 1 through 31. New in version 2.4.

<!-- page: 111 -->

Macros to extract fields from datetime objects. The argument must be an instance of PyDateTime\_DateTime, including subclasses. The argument must not be NULL, and the type is not checked:

int **PyDateTime\_DATE\_GET\_HOUR**(PyDateTime\_DateTime \*o) Return the hour, as an int from 0 through 23. New in version 2.4.

int **PyDateTime\_DATE\_GET\_MINUTE**(PyDateTime\_DateTime \*o) Return the minute, as an int from 0 through 59. New in version 2.4.

int **PyDateTime\_DATE\_GET\_SECOND**(PyDateTime\_DateTime \*o) Return the second, as an int from 0 through 59. New in version 2.4.

int **PyDateTime\_DATE\_GET\_MICROSECOND**(PyDateTime\_DateTime \*o) Return the microsecond, as an int from 0 through 999999. New in version 2.4.

Macros to extract fields from time objects. The argument must be an instance of PyDateTime\_Time, including subclasses. The argument must not be NULL, and the type is not checked:

int **PyDateTime\_TIME\_GET\_HOUR**(PyDateTime\_Time \*o) Return the hour, as an int from 0 through 23. New in version 2.4.

int **PyDateTime\_TIME\_GET\_MINUTE**(PyDateTime\_Time \*o) Return the minute, as an int from 0 through 59. New in version 2.4.

int **PyDateTime\_TIME\_GET\_SECOND**(PyDateTime\_Time \*o) Return the second, as an int from 0 through 59. New in version 2.4.

int **PyDateTime\_TIME\_GET\_MICROSECOND**(PyDateTime\_Time \*o) Return the microsecond, as an int from 0 through 999999. New in version 2.4.

Macros for the convenience of modules implementing the DB API:

PyObject\* **PyDateTime\_FromTimestamp**(PyObject \*args) Return value: New reference. Create and return a new datetime.datetime object given an argument tuple suitable for passing to datetime.datetime.fromtimestamp(). New in version 2.4.

PyObject\* **PyDate\_FromTimestamp**(PyObject \*args) Return value: New reference. Create and return a new datetime.date object given an argument tuple suitable for passing to datetime.date.fromtimestamp(). New in version 2.4.

<!-- page: 112 -->

## 7.5.16 Set Objects

## New in version 2.5.

This section details the public API for set and frozenset objects. Any functionality not listed below is best accessed using the either the abstract object protocol (including PyObject\_CallMethod(), PyObject\_RichCompareBool(), PyObject\_Hash(), PyObject\_Repr(), PyObject\_IsTrue(), PyObject\_Print(), and PyObject\_GetIter()) or the abstract number protocol (including PyNumber\_And(), PyNumber\_Subtract(), PyNumber\_Or(), PyNumber\_Xor(), PyNumber\_InPlaceAnd(), PyNumber\_InPlaceSubtract(), PyNumber\_InPlaceOr(), and PyNumber\_InPlaceXor()).

## PySetObject

This subtype of PyObject is used to hold the internal data for both set and frozenset objects. It is like a PyDictObject in that it is a fixed size for small sets (much like tuple storage) and will point to a separate, variable sized block of memory for medium and large sized sets (much like list storage). None of the fields of this structure should be considered public and are subject to change. All access should be done through the documented API rather than by manipulating the values in the structure.

## PyTypeObject PySet\_Type

This is an instance of PyTypeObject representing the Python set type.

## PyTypeObject PyFrozenSet\_Type

This is an instance of PyTypeObject representing the Python frozenset type.

The following type check macros work on pointers to any Python object. Likewise, the constructor functions work with any iterable Python object.

## int PySet\_Check(PyObject \*p)

Return true if p is a set object or an instance of a subtype.

New in version 2.6.

## int PyFrozenSet\_Check(PyObject \*p)

Return true if p is a frozenset object or an instance of a subtype.

New in version 2.6.

## int PyAnySet\_Check(PyObject \*p)

Return true if p is a set object, a frozenset object, or an instance of a subtype.

## int PyAnySet\_CheckExact(PyObject \*p)

Return true if p is a set object or a frozenset object but not an instance of a subtype.

## int PyFrozenSet\_CheckExact(PyObject \*p)

Return true if p is a frozenset object but not an instance of a subtype.

## PyObject\* PySet\_New(PyObject \*iterable)

Return value: New reference. Return a new set containing objects returned by the iterable. The iterable may be NULL to create a new empty set. Return the new set on success or NULL on failure. Raise TypeError if iterable is not actually iterable. The constructor is also useful for copying a set (c=set(s)).

## PyObject\* PyFrozenSet\_New(PyObject \*iterable)

Return value: New reference. Return a new frozenset containing objects returned by the iterable. The iterable may be NULL to create a new empty frozenset. Return the new set on success or NULL on failure. Raise TypeError if iterable is not actually iterable.

Changed in version 2.6: Now guaranteed to return a brand-new frozenset. Formerly, frozensets of zero-length were a singleton. This got in the way of building-up new frozensets with PySet\_Add().

The following functions and macros are available for instances of set or frozenset or instances of their subtypes.

<!-- page: 113 -->

## Py\_ssize\_t PySet\_Size(PyObject \*anyset)

Return the length of a set or frozenset object. Equivalent to len(anyset). Raises a PyExc\_SystemError if anyset is not a set, frozenset, or an instance of a subtype.

Changed in version 2.5: This function returned an int. This might require changes in your code for properly supporting 64-bit systems.

## Py\_ssize\_t PySet\_GET\_SIZE(PyObject \*anyset)

Macro form of PySet\_Size() without error checking.

## int PySet\_Contains(PyObject \*anyset, PyObject \*key)

Return 1 if found, 0 if not found, and -1 if an error is encountered. Unlike the Python \_\_contains\_\_() method, this function does not automatically convert unhashable sets into temporary frozensets. Raise a TypeError if the key is unhashable. Raise PyExc\_SystemError if anyset is not a set, frozenset, or an instance of a subtype.

## int PySet\_Add(PyObject \*set, PyObject \*key)

Add key to a set instance. Does not apply to frozenset instances. Return 0 on success or -1 on failure. Raise a TypeError if the key is unhashable. Raise a MemoryError if there is no room to grow. Raise a SystemError if set is not an instance of set or its subtype.

Changed in version 2.6: Now works with instances of frozenset or its subtypes. Like PyTuple\_SetItem() in that it can be used to fill-in the values of brand new frozensets before they are exposed to other code.

The following functions are available for instances of set or its subtypes but not for instances of frozenset or its subtypes.

## int PySet\_Discard(PyObject \*set, PyObject \*key)

Return 1 if found and removed, 0 if not found (no action taken), and -1 if an error is encountered. Does not raise KeyError for missing keys. Raise a TypeError if the key is unhashable. Unlike the Python discard() method, this function does not automatically convert unhashable sets into temporary frozensets. Raise PyExc\_SystemError if set is not an instance of set or its subtype.

## PyObject\* PySet\_Pop(PyObject \*set)

Return value: New reference. Return a new reference to an arbitrary object in the set, and removes the object from the set. Return NULL on failure. Raise KeyError if the set is empty. Raise a SystemError if set is not an instance of set or its subtype.

## int PySet\_Clear(PyObject \*set)

Empty an existing set of all elements.

## 7.5.17 Code Objects

Code objects are a low-level detail of the CPython implementation. Each one represents a chunk of executable code that hasn’t yet been bound into a function.

## PyCodeObject

The C structure of the objects used to describe code objects. The fields of this type are subject to change at any time.

## PyTypeObject PyCode\_Type

This is an instance of PyTypeObject representing the Python code type.

## int PyCode\_Check(PyObject \*co)

Return true if co is a code object.

## int PyCode\_GetNumFree(PyObject \*co)

Return the number of free variables in co.

<!-- page: 114 -->

PyCodeObject \***PyCode\_New**(int argcount, int nlocals, int stacksize, int flags, PyObject \*code, PyObject \*consts, PyObject \*names, PyObject \*varnames, PyObject \*freevars, PyObject \*cellvars, PyObject \*filename, PyObject \*name, int firstlineno, PyObject \*lnotab)

Return a new code object. If you need a dummy code object to create a frame, use PyCode\_NewEmpty() instead. Calling PyCode\_New() directly can bind you to a precise Python version since the definition of the bytecode changes often.

int **PyCode\_NewEmpty**(const char \*filename, const char \*funcname, int firstlineno) Return a new empty code object with the specified filename, function name, and first line number. It is illegal to exec or eval() the resulting code object.

<!-- page: 115 -->

## INITIALIZATION, FINALIZATION, AND THREADS

## 8.1 Initializing and finalizing the interpreter

## void Py\_Initialize()

Initialize the Python interpreter. In an application embedding Python, this should be called before using any other Python/C API functions; with the exception of Py\_SetProgramName(), Py\_SetPythonHome(), PyEval\_InitThreads(), PyEval\_ReleaseLock(), and PyEval\_AcquireLock(). This initializes the table of loaded modules (sys.modules), and creates the fundamental modules \_\_builtin\_\_, \_main\_\_ and sys. It also initializes the module search path (sys.path). It does not set sys. argv; use PySys\_SetArgvEx() for that. This is a no-op when called for a second time (without calling Py\_Finalize() first). There is no return value; it is a fatal error if the initialization fails.

## void Py\_InitializeEx(int initsigs)

This function works like Py\_Initialize() if initsigs is 1. If initsigs is 0, it skips initialization registration of signal handlers, which might be useful when Python is embedded.

New in version 2.4.

## int Py\_IsInitialized()

Return true (nonzero) when the Python interpreter has been initialized, false (zero) if not. After Py\_Finalize() is called, this returns false until Py\_Initialize() is called again.

## void Py\_Finalize()

Undo all initializations made by Py\_Initialize() and subsequent use of Python/C API functions, and destroy all sub-interpreters (see Py\_NewInterpreter() below) that were created and not yet destroyed since the last call to Py\_Initialize(). Ideally, this frees all memory allocated by the Python interpreter. This is a no-op when called for a second time (without calling Py\_Initialize() again first). There is no return value; errors during finalization are ignored.

This function is provided for a number of reasons. An embedding application might want to restart Python without having to restart the application itself. An application that has loaded the Python interpreter from a dynamically loadable library (or DLL) might want to free all memory allocated by Python before unloading the DLL. During a hunt for memory leaks in an application a developer might want to free all memory allocated by Python before exiting from the application.

**Bugs and caveats:** The destruction of modules and objects in modules is done in random order; this may cause destructors (\_\_del\_\_() methods) to fail when they depend on other objects (even functions) or modules. Dynamically loaded extension modules loaded by Python are not unloaded. Small amounts of memory allocated by the Python interpreter may not be freed (if you find a leak, please report it). Memory tied up in circular references between objects is not freed. Some memory allocated by extension modules may not be freed. Some extensions may not work properly if their initialization routine is called more than once; this can happen if an application calls Py\_Initialize() and Py\_Finalize() more than once.

<!-- page: 116 -->

## 8.2 Process-wide parameters

## void Py\_SetProgramName(char \*name)

This function should be called before Py\_Initialize() is called for the first time, if it is called at all. It tells the interpreter the value of the argv[0] argument to the main() function of the program. This is used by Py\_GetPath() and some other functions below to find the Python run-time libraries relative to the interpreter executable. The default value is 'python'. The argument should point to a zero-terminated character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage.

## char\* Py\_GetProgramName()

Return the program name set with Py\_SetProgramName(), or the default. The returned string points into static storage; the caller should not modify its value.

## char\* Py\_GetPrefix()

Return the prefix for installed platform-independent files. This is derived through a number of complicated rules from the program name set with Py\_SetProgramName() and some environment variables; for example, if the program name is '/usr/local/bin/python', the prefix is '/usr/local'. The returned string points into static storage; the caller should not modify its value. This corresponds to the **prefix** variable in the toplevel Makefile and the --prefix argument to the **configure** script at build time. The value is available to Python code as sys.prefix. It is only useful on Unix. See also the next function.

## char\* Py\_GetExecPrefix()

Return the exec-prefix for installed platform-dependent files. This is derived through a number of complicated rules from the program name set with Py\_SetProgramName() and some environment variables; for example, if the program name is '/usr/local/bin/python', the exec-prefix is '/usr/local'. The returned string points into static storage; the caller should not modify its value. This corresponds to the **exec\_prefix** variable in the top-level Makefile and the --exec-prefix argument to the **configure** script at build time. The value is available to Python code as sys.exec\_prefix. It is only useful on Unix.

Background: The exec-prefix differs from the prefix when platform dependent files (such as executables and shared libraries) are installed in a different directory tree. In a typical installation, platform dependent files may be installed in the /usr/local/plat subtree while platform independent may be installed in /usr/local.

Generally speaking, a platform is a combination of hardware and software families, e.g. Sparc machines running the Solaris 2.x operating system are considered the same platform, but Intel machines running Solaris 2.x are another platform, and Intel machines running Linux are yet another platform. Different major revisions of the same operating system generally also form different platforms. Non-Unix operating systems are a different story; the installation strategies on those systems are so different that the prefix and exec-prefix are meaningless, and set to the empty string. Note that compiled Python bytecode files are platform independent (but not independent from the Python version by which they were compiled!).

System administrators will know how to configure the **mount** or **automount** programs to share /usr/local between platforms while having /usr/local/plat be a different filesystem for each platform.

## char\* Py\_GetProgramFullPath()

Return the full program name of the Python executable; this is computed as a side-effect of deriving the default module search path from the program name (set by Py\_SetProgramName() above). The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys. executable.

## char\* Py\_GetPath()

Return the default module search path; this is computed from the program name (set by Py\_SetProgramName() above) and some environment variables. The returned string consists of a series of directory names separated by a platform dependent delimiter character. The delimiter character is ':' on Unix and Mac OS X, ';' on Windows. The returned string points into static storage; the caller should not

<!-- page: 117 -->

modify its value. The list sys.path is initialized with this value on interpreter startup; it can be (and usually is) modified later to change the search path for loading modules.

## const char\* Py\_GetVersion()

Return the version of this Python interpreter. This is a string that looks something like

```txt
"1.5 (#67, Dec 31 1997, 22:34:28) [GCC 2.7.2.2]"
```

The first word (up to the first space character) is the current Python version; the first three characters are the major and minor version separated by a period. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys.version.

## const char\* Py\_GetPlatform()

Return the platform identifier for the current platform. On Unix, this is formed from the “official” name of the operating system, converted to lower case, followed by the major revision number; e.g., for Solaris 2.x, which is also known as SunOS 5.x, the value is 'sunos5'. On Mac OS X, it is 'darwin'. On Windows, it is 'win'. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys.platform.

## const char\* Py\_GetCopyright()

Return the official copyright string for the current Python version, for example

'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam'

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as sys.copyright.

## const char\* Py\_GetCompiler()

Return an indication of the compiler used to build the current Python version, in square brackets, for example:

```txt
"[GCC 2.7.2.2]"
```

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable sys.version.

## const char\* Py\_GetBuildInfo()

Return information about the sequence number and build date and time of the current Python interpreter instance, for example

```txt
"#67, Aug 1 1997, 22:34:28"
```

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable sys.version.

## void PySys\_SetArgvEx(int argc, char \*\*argv, int updatepath)

Set sys.argv based on argc and argv. These parameters are similar to those passed to the program’s main() function with the difference that the first entry should refer to the script file to be executed rather than the executable hosting the Python interpreter. If there isn’t a script that will be run, the first entry in argv can be an empty string. If this function fails to initialize sys.argv, a fatal condition is signalled using Py\_FatalError().

If updatepath is zero, this is all the function does. If updatepath is non-zero, the function also modifies sys.path according to the following algorithm:

• If the name of an existing script is passed in argv[0], the absolute path of the directory where the script is located is prepended to sys.path.

• Otherwise (that is, if argc is 0 or argv[0] doesn’t point to an existing file name), an empty string is prepended to sys.path, which is the same as prepending the current working directory (".").

<!-- page: 118 -->

**Note:** It is recommended that applications embedding the Python interpreter for purposes other than executing a single script pass 0 as updatepath, and update sys.path themselves if desired. See [CVE-2008-5983](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-5983).

On versions before 2.6.6, you can achieve the same effect by manually popping the first sys.path element after having called PySys\_SetArgv(), for example using:

```javascript
Python_SimpleString("import sys; sys.path.pop(0)\n");
```

New in version 2.6.6.

## void PySys\_SetArgv(int argc, char \*\*argv)

This function works like PySys\_SetArgvEx() with updatepath set to 1.

## void Py\_SetPythonHome(char \*home)

Set the default “home” directory, that is, the location of the standard Python libraries. See PYTHONHOME for the meaning of the argument string.

The argument should point to a zero-terminated character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage.

## char\* Py\_GetPythonHome()

Return the default “home”, that is, the value set by a previous call to Py\_SetPythonHome(), or the value of the PYTHONHOME environment variable if it is set.

## 8.3 Thread State and the Global Interpreter Lock

The Python interpreter is not fully thread-safe. In order to support multi-threaded Python programs, there’s a global lock, called the global interpreter lock or GIL, that must be held by the current thread before it can safely access Python objects. Without the lock, even the simplest operations could cause problems in a multi-threaded program: for example, when two threads simultaneously increment the reference count of the same object, the reference count could end up being incremented only once instead of twice.

Therefore, the rule exists that only the thread that has acquired the GIL may operate on Python objects or call Python/C API functions. In order to emulate concurrency of execution, the interpreter regularly tries to switch threads (see sys. setcheckinterval()). The lock is also released around potentially blocking I/O operations like reading or writing a file, so that other Python threads can run in the meantime.

The Python interpreter keeps some thread-specific bookkeeping information inside a data structure called PyThreadState. There’s also one global variable pointing to the current PyThreadState: it can be retrieved using PyThreadState\_Get().

## 8.3.1 Releasing the GIL from extension code

Most extension code manipulating the GIL has the following simple structure:

```txt
Save the thread state in a local variable.
Release the global interpreter lock.
... Do some blocking I/O operation ...
Reacquire the global interpreter lock.
Restore the thread state from the local variable.
```

This is so common that a pair of macros exists to simplify it:

<!-- page: 119 -->

```txt
Py_BEGIN_ALLOW_THREADS
... Do some blocking I/O operation ...
Py_END_ALLOW_THREADS
```

The Py\_BEGIN\_ALLOW\_THREADS macro opens a new block and declares a hidden local variable; the Py\_END\_ALLOW\_THREADS macro closes the block. These two macros are still available when Python is compiled without thread support (they simply have an empty expansion).

When thread support is enabled, the block above expands to the following code:

```txt
PyThreadState *_save;

_save = PyEval_SaveThread();
...Do some blocking I/O operation...
PyEval_RestoreThread(_save);
```

Here is how these functions work: the global interpreter lock is used to protect the pointer to the current thread state. When releasing the lock and saving the thread state, the current thread state pointer must be retrieved before the lock is released (since another thread could immediately acquire the lock and store its own thread state in the global variable). Conversely, when acquiring the lock and restoring the thread state, the lock must be acquired before storing the thread state pointer.

**Note:** Calling system I/O functions is the most common use case for releasing the GIL, but it can also be useful before calling long-running computations which don’t need access to Python objects, such as compression or cryptographic functions operating over memory buffers. For example, the standard zlib and hashlib modules release the GIL when compressing or hashing data.

## 8.3.2 Non-Python created threads

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

Note that the PyGILState\_\*() functions assume there is only one global interpreter (created automatically by Py\_Initialize()). Python supports the creation of additional interpreters (using Py\_NewInterpreter()),

<!-- page: 120 -->

but mixing multiple interpreters and the PyGILState\_\*() API is unsupported.

Another important thing to note about threads is their behaviour in the face of the C fork() call. On most systems with fork(), after a process forks only the thread that issued the fork will exist. That also means any locks held by other threads will never be released. Python solves this for os.fork() by acquiring the locks it uses internally before the fork, and releasing them afterwards. In addition, it resets any lock-objects in the child. When extending or embedding Python, there is no way to inform Python of additional (non-Python) locks that need to be acquired before or reset after a fork. OS facilities such as pthread\_atfork() would need to be used to accomplish the same thing. Additionally, when extending or embedding Python, calling fork() directly rather than through os.fork() (and returning to or calling into Python) may result in a deadlock by one of Python’s internal locks being held by a thread that is defunct after the fork. PyOS\_AfterFork() tries to reset the necessary locks, but is not always able to.

## 8.3.3 High-level API

These are the most commonly used types and functions when writing C extension code, or when embedding the Python interpreter:

## PyInterpreterState

This data structure represents the state shared by a number of cooperating threads. Threads belonging to the same interpreter share their module administration and a few other internal items. There are no public members in this structure.

Threads belonging to different interpreters initially share nothing, except process state like available memory, open file descriptors and such. The global interpreter lock is also shared by all threads, regardless of to which interpreter they belong.

## PyThreadState

This data structure represents the state of a single thread. The only public data member is PyInterpreterState \*interp, which points to this thread’s interpreter state.

## void PyEval\_InitThreads()

Initialize and acquire the global interpreter lock. It should be called in the main thread before creating a second thread or engaging in any other thread operations such as PyEval\_ReleaseLock() or PyEval\_ReleaseThread(tstate). It is not needed before calling PyEval\_SaveThread() or PyEval\_RestoreThread().

This is a no-op when called for a second time. It is safe to call this function before calling Py\_Initialize().

**Note:** When only the main thread exists, no GIL operations are needed. This is a common situation (most Python programs do not use threads), and the lock operations slow the interpreter down a bit. Therefore, the lock is not created initially. This situation is equivalent to having acquired the lock: when there is only a single thread, all object accesses are safe. Therefore, when this function initializes the global interpreter lock, it also acquires it. Before the Python \_thread module creates a new thread, knowing that either it has the lock or the lock hasn’t been created yet, it calls PyEval\_InitThreads(). When this call returns, it is guaranteed that the lock has been created and that the calling thread has acquired it.

It is **not** safe to call this function when it is unknown which thread (if any) currently has the global interpreter lock.

This function is not available when thread support is disabled at compile time.

## int PyEval\_ThreadsInitialized()

Returns a non-zero value if PyEval\_InitThreads() has been called. This function can be called without holding the GIL, and therefore can be used to avoid calls to the locking API when running single-threaded. This function is not available when thread support is disabled at compile time.

New in version 2.4.

<!-- page: 121 -->

## PyThreadState\* PyEval\_SaveThread()

Release the global interpreter lock (if it has been created and thread support is enabled) and reset the thread state to NULL, returning the previous thread state (which is not NULL). If the lock has been created, the current thread must have acquired it. (This function is available even when thread support is disabled at compile time.)

## void PyEval\_RestoreThread(PyThreadState \*tstate)

Acquire the global interpreter lock (if it has been created and thread support is enabled) and set the thread state to tstate, which must not be NULL. If the lock has been created, the current thread must not have acquired it, otherwise deadlock ensues. (This function is available even when thread support is disabled at compile time.)

## PyThreadState\* PyThreadState\_Get()

Return the current thread state. The global interpreter lock must be held. When the current thread state is NULL, this issues a fatal error (so that the caller needn’t check for NULL).

## PyThreadState\* PyThreadState\_Swap(PyThreadState \*tstate)

Swap the current thread state with the thread state given by the argument tstate, which may be NULL. The global interpreter lock must be held and is not released.

## void PyEval\_ReInitThreads()

This function is called from PyOS\_AfterFork() to ensure that newly created child processes don’t hold locks referring to threads which are not running in the child process.

The following functions use thread-local storage, and are not compatible with sub-interpreters:

## PyGILState\_STATE PyGILState\_Ensure()

Ensure that the current thread is ready to call the Python C API regardless of the current state of Python, or of the global interpreter lock. This may be called as many times as desired by a thread as long as each call is matched with a call to PyGILState\_Release(). In general, other thread-related APIs may be used between PyGILState\_Ensure() and PyGILState\_Release() calls as long as the thread state is restored to its previous state before the Release(). For example, normal usage of the Py\_BEGIN\_ALLOW\_THREADS and Py\_END\_ALLOW\_THREADS macros is acceptable.

The return value is an opaque “handle” to the thread state when PyGILState\_Ensure() was called, and must be passed to PyGILState\_Release() to ensure Python is left in the same state. Even though recursive calls are allowed, these handles cannot be shared - each unique call to PyGILState\_Ensure() must save the handle for its call to PyGILState\_Release().

When the function returns, the current thread will hold the GIL and be able to call arbitrary Python code. Failure is a fatal error.

New in version 2.3.

## void PyGILState\_Release(PyGILState\_STATE)

Release any resources previously acquired. After this call, Python’s state will be the same as it was prior to the corresponding PyGILState\_Ensure() call (but generally this state will be unknown to the caller, hence the use of the GILState API).

Every call to PyGILState\_Ensure() must be matched by a call to PyGILState\_Release() on the same thread.

New in version 2.3.

## PyThreadState\* PyGILState\_GetThisThreadState()

Get the current thread state for this thread. May return NULL if no GILState API has been used on the current thread. Note that the main thread always has such a thread-state, even if no auto-thread-state call has been made on the main thread. This is mainly a helper/diagnostic function.

New in version 2.3.

The following macros are normally used without a trailing semicolon; look for example usage in the Python source distribution.

<!-- page: 122 -->

## Py\_BEGIN\_ALLOW\_THREADS

This macro expands to { PyThreadState \*\_save; \_save = PyEval\_SaveThread();. Note that it contains an opening brace; it must be matched with a following Py\_END\_ALLOW\_THREADS macro. See above for further discussion of this macro. It is a no-op when thread support is disabled at compile time.

## Py\_END\_ALLOW\_THREADS

This macro expands to PyEval\_RestoreThread(\_save); }. Note that it contains a closing brace; it must be matched with an earlier Py\_BEGIN\_ALLOW\_THREADS macro. See above for further discussion of this macro. It is a no-op when thread support is disabled at compile time.

## Py\_BLOCK\_THREADS

This macro expands to PyEval\_RestoreThread(\_save);: it is equivalent to Py\_END\_ALLOW\_THREADS without the closing brace. It is a no-op when thread support is disabled at compile time.

## Py\_UNBLOCK\_THREADS

This macro expands to \_save = PyEval\_SaveThread();: it is equivalent to Py\_BEGIN\_ALLOW\_THREADS without the opening brace and variable declaration. It is a no-op when thread support is disabled at compile time.

## 8.3.4 Low-level API

All of the following functions are only available when thread support is enabled at compile time, and must be called only when the global interpreter lock has been created.

## PyInterpreterState\* PyInterpreterState\_New()

Create a new interpreter state object. The global interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function.

## void PyInterpreterState\_Clear(PyInterpreterState \*interp)

Reset all information in an interpreter state object. The global interpreter lock must be held.

## void PyInterpreterState\_Delete(PyInterpreterState \*interp)

Destroy an interpreter state object. The global interpreter lock need not be held. The interpreter state must have been reset with a previous call to PyInterpreterState\_Clear().

## PyThreadState\* PyThreadState\_New(PyInterpreterState \*interp)

Create a new thread state object belonging to the given interpreter object. The global interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function.

## void PyThreadState\_Clear(PyThreadState \*tstate)

Reset all information in a thread state object. The global interpreter lock must be held.

## void PyThreadState\_Delete(PyThreadState \*tstate)

Destroy a thread state object. The global interpreter lock need not be held. The thread state must have been reset with a previous call to PyThreadState\_Clear().

## PyObject\* PyThreadState\_GetDict()

Return value: Borrowed reference. Return a dictionary in which extensions can store thread-specific state information. Each extension should use a unique key to use to store state in the dictionary. It is okay to call this function when no current thread state is available. If this function returns NULL, no exception has been raised and the caller should assume no current thread state is available.

Changed in version 2.3: Previously this could only be called when a current thread is active, and NULL meant that an exception was raised.

## int PyThreadState\_SetAsyncExc(long id, PyObject \*exc)

Asynchronously raise an exception in a thread. The id argument is the thread id of the target thread; exc is the exception object to be raised. This function does not steal any references to exc. To prevent naive misuse, you must

<!-- page: 123 -->

write your own C extension to call this. Must be called with the GIL held. Returns the number of thread states modified; this is normally one, but will be zero if the thread id isn’t found. If exc is NULL, the pending exception (if any) for the thread is cleared. This raises no exceptions.

New in version 2.3.

## void PyEval\_AcquireThread(PyThreadState \*tstate)

Acquire the global interpreter lock and set the current thread state to tstate, which should not be NULL. The lock must have been created earlier. If this thread already has the lock, deadlock ensues.

PyEval\_RestoreThread() is a higher-level function which is always available (even when thread support isn’t enabled or when threads have not been initialized).

## void PyEval\_ReleaseThread(PyThreadState \*tstate)

Reset the current thread state to NULL and release the global interpreter lock. The lock must have been created earlier and must be held by the current thread. The tstate argument, which must not be NULL, is only used to check that it represents the current thread state — if it isn’t, a fatal error is reported.

PyEval\_SaveThread() is a higher-level function which is always available (even when thread support isn’t enabled or when threads have not been initialized).

## void PyEval\_AcquireLock()

Acquire the global interpreter lock. The lock must have been created earlier. If this thread already has the lock, a deadlock ensues.

**Warning:** This function does not change the current thread state. Please use PyEval\_RestoreThread() or PyEval\_AcquireThread() instead.

## void PyEval\_ReleaseLock()

Release the global interpreter lock. The lock must have been created earlier.

**Warning:** This function does not change the current thread state. Please use PyEval\_SaveThread() or PyEval\_ReleaseThread() instead.

## 8.4 Sub-interpreter support

While in most uses, you will only embed a single Python interpreter, there are cases where you need to create several independent interpreters in the same process and perhaps even in the same thread. Sub-interpreters allow you to do that. You can switch between sub-interpreters using the PyThreadState\_Swap() function. You can create and destroy them using the following functions:

## PyThreadState\* Py\_NewInterpreter()

Create a new sub-interpreter. This is an (almost) totally separate environment for the execution of Python code. In particular, the new interpreter has separate, independent versions of all imported modules, including the fundamental modules builtins, \_\_main\_\_ and sys. The table of loaded modules (sys.modules) and the module search path (sys.path) are also separate. The new environment has no sys.argv variable. It has new standard I/O stream file objects sys.stdin, sys.stdout and sys.stderr (however these refer to the same underlying file descriptors).

The return value points to the first thread state created in the new sub-interpreter. This thread state is made in the current thread state. Note that no actual thread is created; see the discussion of thread states below. If creation of the new interpreter is unsuccessful, NULL is returned; no exception is set since the exception state is stored in the current thread state and there may not be a current thread state. (Like all other Python/C API functions, the

<!-- page: 124 -->

global interpreter lock must be held before calling this function and is still held when it returns; however, unlike most other Python/C API functions, there needn’t be a current thread state on entry.)

Extension modules are shared between (sub-)interpreters as follows: the first time a particular extension is imported, it is initialized normally, and a (shallow) copy of its module’s dictionary is squirreled away. When the same extension is imported by another (sub-)interpreter, a new module is initialized and filled with the contents of this copy; the extension’s init function is not called. Note that this is different from what happens when an extension is imported after the interpreter has been completely re-initialized by calling Py\_Finalize() and Py\_Initialize() in that case, the extension’s initmodule function is called again.

## void Py\_EndInterpreter(PyThreadState \*tstate)

Destroy the (sub-)interpreter represented by the given thread state. The given thread state must be the current thread state. See the discussion of thread states below. When the call returns, the current thread state is NULL. All thread states associated with this interpreter are destroyed. (The global interpreter lock must be held before calling this function and is still held when it returns.) Py\_Finalize() will destroy all sub-interpreters that haven’t been explicitly destroyed at that point.

## 8.4.1 Bugs and caveats

Because sub-interpreters (and the main interpreter) are part of the same process, the insulation between them isn’t perfect — for example, using low-level file operations like os.close() they can (accidentally or maliciously) affect each other’s open files. Because of the way extensions are shared between (sub-)interpreters, some extensions may not work properly; this is especially likely when the extension makes use of (static) global variables, or when the extension manipulates its module’s dictionary after its initialization. It is possible to insert objects created in one sub-interpreter into a namespace of another sub-interpreter; this should be done with great care to avoid sharing user-defined functions, methods, instances or classes between sub-interpreters, since import operations executed by such objects may affect the wrong (sub-)interpreter’s dictionary of loaded modules.

Also note that combining this functionality with PyGILState\_\*() APIs is delicate, because these APIs assume a bijection between Python thread states and OS-level threads, an assumption broken by the presence of sub-interpreters. It is highly recommended that you don’t switch sub-interpreters between a pair of matching PyGILState\_Ensure() and PyGILState\_Release() calls. Furthermore, extensions (such as ctypes) using these APIs to allow calling of Python code from non-Python created threads will probably be broken when using sub-interpreters.

## 8.5 Asynchronous Notifications

A mechanism is provided to make asynchronous notifications to the main interpreter thread. These notifications take the form of a function pointer and a void pointer argument.

## int Py\_AddPendingCall(int (\*func)(void \*), void \*arg)

Schedule a function to be called from the main interpreter thread. On success, 0 is returned and func is queued for being called in the main thread. On failure, -1 is returned without setting any exception.

When successfully queued, func will be eventually called from the main interpreter thread with the argument arg. It will be called asynchronously with respect to normally running Python code, but with both these conditions met:

• on a bytecode boundary;

• with the main thread holding the global interpreter lock (func can therefore use the full C API).

func must return 0 on success, or -1 on failure with an exception set. func won’t be interrupted to perform another asynchronous notification recursively, but it can still be interrupted to switch threads if the global interpreter lock is released.

This function doesn’t need a current thread state to run, and it doesn’t need the global interpreter lock.

<!-- page: 125 -->

**Warning:** This is a low-level function, only useful for very special cases. There is no guarantee that func will be called as quick as possible. If the main thread is busy executing a system call, func won’t be called before the system call returns. This function is generally **not** suitable for calling Python code from arbitrary C threads. Instead, use the PyGILState API.

New in version 2.7.

## 8.6 Profiling and Tracing

The Python interpreter provides some low-level support for attaching profiling and execution tracing facilities. These are used for profiling, debugging, and coverage analysis tools.

Starting with Python 2.2, the implementation of this facility was substantially revised, and an interface from C was added. This C interface allows the profiling or tracing code to avoid the overhead of calling through Python-level callable objects, making a direct C function call instead. The essential attributes of the facility have not changed; the interface allows trace functions to be installed per-thread, and the basic events reported to the trace function are the same as had been reported to the Python-level trace functions in previous versions.

## int (\*Py\_tracefunc)(PyObject \*obj, PyFrameObject \*frame, int what, PyObject \*arg)

The type of the trace function registered using PyEval\_SetProfile() and PyEval\_SetTrace(). The first parameter is the object passed to the registration function as obj, frame is the frame object to which the event pertains, what is one of the constants PyTrace\_CALL, PyTrace\_EXCEPTION, PyTrace\_LINE, PyTrace\_RETURN, PyTrace\_C\_CALL, PyTrace\_C\_EXCEPTION, or PyTrace\_C\_RETURN, and arg depends on the value of what:

| Value of what | Meaning of arg |
| --- | --- |
| PyTrace_CALL | Always Py_None. |
| PyTrace_EXCEPTION | Exception information as returned by sys.exc_info(). |
| PyTrace_LINE | Always Py_None. |
| PyTrace_RETURN | Value being returned to the caller, or NULL if caused by an exception. |
| PyTrace_C_CALL | Function object being called. |
| PyTrace_C_EXCEPTION | Function object being called. |
| PyTrace_C_RETURN | Function object being called. |

## int PyTrace\_CALL

The value of the what parameter to a Py\_tracefunc function when a new call to a function or method is being reported, or a new entry into a generator. Note that the creation of the iterator for a generator function is not reported as there is no control transfer to the Python bytecode in the corresponding frame.

## int PyTrace\_EXCEPTION

The value of the what parameter to a Py\_tracefunc function when an exception has been raised. The callback function is called with this value for what when after any bytecode is processed after which the exception becomes set within the frame being executed. The effect of this is that as exception propagation causes the Python stack to unwind, the callback is called upon return to each frame as the exception propagates. Only trace functions receives these events; they are not needed by the profiler.

## int PyTrace\_LINE

The value passed as the what parameter to a trace function (but not a profiling function) when a line-number event is being reported.

## int PyTrace\_RETURN

The value for the what parameter to Py\_tracefunc functions when a call is about to return.

<!-- page: 126 -->

int **PyTrace\_C\_CALL**

The value for the what parameter to Py\_tracefunc functions when a C function is about to be called.

int **PyTrace\_C\_EXCEPTION**

The value for the what parameter to Py\_tracefunc functions when a C function has raised an exception.

int **PyTrace\_C\_RETURN**

The value for the what parameter to Py\_tracefunc functions when a C function has returned.

void **PyEval\_SetProfile**(Py\_tracefunc func, PyObject \*obj)

Set the profiler function to func. The obj parameter is passed to the function as its first parameter, and may be any Python object, or NULL. If the profile function needs to maintain state, using a different value for obj for each thread provides a convenient and thread-safe place to store it. The profile function is called for all monitored events except PyTrace\_LINE and PyTrace\_EXCEPTION.

void **PyEval\_SetTrace**(Py\_tracefunc func, PyObject \*obj)

Set the tracing function to func. This is similar to PyEval\_SetProfile(), except the tracing function does receive line-number events and does not receive any event related to C function objects being called. Any trace function registered using PyEval\_SetTrace() will not receive PyTrace\_C\_CALL, PyTrace\_C\_EXCEPTION or PyTrace\_C\_RETURN as a value for the what parameter.

PyObject\* **PyEval\_GetCallStats**(PyObject \*self)

Return a tuple of function call counts. There are constants defined for the positions within the tuple:

| Name | Value |
| --- | --- |
| PCALL_ALL | 0 |
| PCALL_FUNCTION | 1 |
| PCALL_FAST_FUNCTION | 2 |
| PCALL_FASTER_FUNCTION | 3 |
| PCALL_METHOD | 4 |
| PCALL_BOUND_METHOD | 5 |
| PCALL_CFUNCTION | 6 |
| PCALL_TYPE | 7 |
| PCALL_GENERATOR | 8 |
| PCALL_OTHER | 9 |
| PCALL_POP | 10 |

PCALL\_FAST\_FUNCTION means no argument tuple needs to be created. PCALL\_FASTER\_FUNCTION means that the fast-path frame setup code is used.

If there is a method call where the call can be optimized by changing the argument tuple and calling the function directly, it gets recorded twice.

This function is only present if Python is compiled with CALL\_PROFILE defined.

## 8.7 Advanced Debugger Support

These functions are only intended to be used by advanced debugging tools.

PyInterpreterState\* **PyInterpreterState\_Head**()

Return the interpreter state object at the head of the list of all such objects.

New in version 2.2.

PyInterpreterState\* **PyInterpreterState\_Next**(PyInterpreterState \*interp)

Return the next interpreter state object after interp from the list of all such objects.

<!-- page: 127 -->

New in version 2.2.

PyThreadState \* **PyInterpreterState\_ThreadHead**(PyInterpreterState \*interp) Return the pointer to the first PyThreadState object in the list of threads associated with the interpreter interp. New in version 2.2.

PyThreadState\* **PyThreadState\_Next**(PyThreadState \*tstate) Return the next thread state object after tstate from the list of all such objects belonging to the same PyInterpreterState object. New in version 2.2.

<!-- page: 128 -->

<!-- page: 129 -->

# MEMORY MANAGEMENT

## 9.1 Overview

Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.

At the lowest level, a raw memory allocator ensures that there is enough room in the private heap for storing all Pythonrelated data by interacting with the memory manager of the operating system. On top of the raw memory allocator, several object-specific allocators operate on the same heap and implement distinct memory management policies adapted to the peculiarities of every object type. For example, integer objects are managed differently within the heap than strings, tuples or dictionaries because integers imply different storage requirements and speed/space tradeoffs. The Python memory manager thus delegates some of the work to the object-specific allocators, but ensures that the latter operate within the bounds of the private heap.

It is important to understand that the management of the Python heap is performed by the interpreter itself and that the user has no control over it, even if they regularly manipulate object pointers to memory blocks inside that heap. The allocation of heap space for Python objects and other internal buffers is performed on demand by the Python memory manager through the Python/C API functions listed in this document.

To avoid memory corruption, extension writers should never try to operate on Python objects with the functions exported by the C library: malloc(), calloc(), realloc() and free(). This will result in mixed calls between the C allocator and the Python memory manager with fatal consequences, because they implement different algorithms and operate on different heaps. However, one may safely allocate and release memory blocks with the C library allocator for individual purposes, as shown in the following example:

```c
PyObject *res;
char *buf = (char *) malloc(BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
...Do some I/O operation involving buf...
res = PyString_FromString(buf);
free(buf); /* malloc'ed */
return res;
```

In this example, the memory request for the I/O buffer is handled by the C library allocator. The Python memory manager is involved only in the allocation of the string object returned as a result.

In most situations, however, it is recommended to allocate memory from the Python heap specifically because the latter is under control of the Python memory manager. For example, this is required when the interpreter is extended with new object types written in C. Another reason for using the Python heap is the desire to inform the Python memory manager about the memory needs of the extension module. Even when the requested memory is used exclusively for internal,

<!-- page: 130 -->

highly-specific purposes, delegating all memory requests to the Python memory manager causes the interpreter to have a more accurate image of its memory footprint as a whole. Consequently, under certain circumstances, the Python memory manager may or may not trigger appropriate actions, like garbage collection, memory compaction or other preventive procedures. Note that by using the C library allocator as shown in the previous example, the allocated memory for the I/O buffer escapes completely the Python memory manager.

## 9.2 Memory Interface

The following function sets, modeled after the ANSI C standard, but specifying behavior when requesting zero bytes, are available for allocating and releasing memory from the Python heap:

## void\* PyMem\_Malloc(size\_t n)

Allocates n bytes and returns a pointer of type void\* to the allocated memory, or NULL if the request fails. Requesting zero bytes returns a distinct non-NULL pointer if possible, as if PyMem\_Malloc(1) had been called instead. The memory will not have been initialized in any way.

## void\* PyMem\_Realloc(void \*p, size\_t n)

Resizes the memory block pointed to by p to n bytes. The contents will be unchanged to the minimum of the old and the new sizes. If p is NULL, the call is equivalent to PyMem\_Malloc(n); else if n is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-NULL. Unless p is NULL, it must have been returned by a previous call to PyMem\_Malloc() or PyMem\_Realloc(). If the request fails, PyMem\_Realloc() returns NULL and p remains a valid pointer to the previous memory area.

## void PyMem\_Free(void \*p)

Frees the memory block pointed to by p, which must have been returned by a previous call to PyMem\_Malloc() or PyMem\_Realloc(). Otherwise, or if PyMem\_Free(p) has been called before, undefined behavior occurs. If p is NULL, no operation is performed.

The following type-oriented macros are provided for convenience. Note that TYPE refers to any C type.

## TYPE\* PyMem\_New(TYPE, size\_t n)

Same as PyMem\_Malloc(), but allocates (n \* sizeof(TYPE)) bytes of memory. Returns a pointer cast to TYPE\*. The memory will not have been initialized in any way.

## TYPE\* PyMem\_Resize(void \*p, TYPE, size\_t n)

Same as PyMem\_Realloc(), but the memory block is resized to (n \* sizeof(TYPE)) bytes. Returns a pointer cast to TYPE\*. On return, p will be a pointer to the new memory area, or NULL in the event of failure. This is a C preprocessor macro; p is always reassigned. Save the original value of p to avoid losing memory when handling errors.

## void PyMem\_Del(void \*p)

Same as PyMem\_Free().

In addition, the following macro sets are provided for calling the Python memory allocator directly, without involving the C API functions listed above. However, note that their use does not preserve binary compatibility across Python versions and is therefore deprecated in extension modules.

PyMem\_MALLOC(), PyMem\_REALLOC(), PyMem\_FREE().

PyMem\_NEW(), PyMem\_RESIZE(), PyMem\_DEL().

<!-- page: 131 -->

## 9.3 Object allocators

The following function sets, modeled after the ANSI C standard, but specifying behavior when requesting zero bytes, are available for allocating and releasing memory from the Python heap.

By default, these functions use pymalloc memory allocator.

**Warning:** The GIL must be held when using these functions.

## void\* PyObject\_Malloc(size\_t n)

Allocates n bytes and returns a pointer of type void\* to the allocated memory, or NULL if the request fails.

Requesting zero bytes returns a distinct non-NULL pointer if possible, as if PyObject\_Malloc(1) had been called instead. The memory will not have been initialized in any way.

## void\* PyObject\_Realloc(void \*p, size\_t n)

Resizes the memory block pointed to by p to n bytes. The contents will be unchanged to the minimum of the old and the new sizes.

If p is NULL, the call is equivalent to PyObject\_Malloc(n); else if n is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-NULL.

Unless p is NULL, it must have been returned by a previous call to PyObject\_Malloc(), PyObject\_Realloc() or PyObject\_Calloc().

If the request fails, PyObject\_Realloc() returns NULL and p remains a valid pointer to the previous memory area.

## void PyObject\_Free(void \*p)

Frees the memory block pointed to by p, which must have been returned by a previous call to PyObject\_Malloc(), PyObject\_Realloc() or PyObject\_Calloc(). Otherwise, or if PyObject\_Free(p) has been called before, undefined behavior occurs.

If p is NULL, no operation is performed.

In addition, the following macro sets are provided:

• PyObject\_MALLOC(): alias to PyObject\_Malloc()

• PyObject\_REALLOC(): alias to PyObject\_Realloc()

• PyObject\_FREE(): alias to PyObject\_Free()

• PyObject\_Del(): alias to PyObject\_Free()

• PyObject\_DEL(): alias to PyObject\_FREE() (so finally an alias to PyObject\_Free())

## 9.4 The pymalloc allocator

Python has a pymalloc allocator optimized for small objects (smaller or equal to 512 bytes) with a short lifetime. It uses memory mappings called “arenas” with a fixed size of 256 KiB. It falls back to malloc() and realloc() for allocations larger than 512 bytes.

pymalloc is the default allocator of PyObject\_Malloc().

The arena allocator uses the following functions:

• mmap() and munmap() if available,

<!-- page: 132 -->

```txt
- malloc() and free() otherwise.
```

Changed in version 2.7.7: The threshold changed from 256 to 512 bytes. The arena allocator now uses mmap() if available.

## 9.5 Examples

Here is the example from section Overview, rewritten so that the I/O buffer is allocated from the Python heap by using the first function set:

```c
PyObject *res;
char *buf = (char *) PyMem_Malloc(BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
/* ...Do some I/O operation involving buf... */
res = PyString_FromString(buf);
PyMem_Free(buf); /* allocated with PyMem_Malloc */
return res;
```

The same code using the type-oriented function set:

```c
PyObject *res;
char *buf = PyMem_New(char, BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
/* ...Do some I/O operation involving buf... */
res = PyString_FromString(buf);
PyMem_Del(buf); /* allocated with PyMem_New */
return res;
```

Note that in the two examples above, the buffer is always manipulated via functions belonging to the same set. Indeed, it is required to use the same memory API family for a given memory block, so that the risk of mixing different allocators is reduced to a minimum. The following code sequence contains two errors, one of which is labeled as fatal because it mixes two different allocators operating on different heaps.

```c
char *buf1 = PyMem_New(char, BUFSIZ);
char *buf2 = (char *) malloc(BUFSIZ);
char *buf3 = (char *) PyMem_Malloc(BUFSIZ);
...
PyMem_Del(buf3); /* Wrong -- should be PyMem_Free() */
free(buf2); /* Right -- allocated via malloc() */
free(buf1); /* Fatal -- should be PyMem_Del() */
```

In addition to the functions aimed at handling raw memory blocks from the Python heap, objects in Python are allocated and released with PyObject\_New(), PyObject\_NewVar() and PyObject\_Del().

These will be explained in the next chapter on defining and implementing new object types in C.

<!-- page: 133 -->

# OBJECT IMPLEMENTATION SUPPORT

This chapter describes the functions, types, and macros used when defining new object types.

## 10.1 Allocating Objects on the Heap

PyObject\* **\_PyObject\_New**(PyTypeObject \*type) Return value: New reference.

PyVarObject\* **\_PyObject\_NewVar**(PyTypeObject \*type, Py\_ssize\_t size) Return value: New reference. Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

void **\_PyObject\_Del**(PyObject \*op)

PyObject\* **PyObject\_Init**(PyObject \*op, PyTypeObject \*type) Return value: Borrowed reference. Initialize a newly-allocated object op with its type and initial reference. Returns the initialized object. If type indicates that the object participates in the cyclic garbage detector, it is added to the detector’s set of observed objects. Other fields of the object are not affected.

PyVarObject\* **PyObject\_InitVar**(PyVarObject \*op, PyTypeObject \*type, Py\_ssize\_t size)

Return value: Borrowed reference. This does everything PyObject\_Init() does, and also initializes the length information for a variable-size object.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

TYPE\* **PyObject\_New**(TYPE, PyTypeObject \*type)

Return value: New reference. Allocate a new Python object using the C structure type TYPE and the Python type object type. Fields not defined by the Python object header are not initialized; the object’s reference count will be one. The size of the memory allocation is determined from the tp\_basicsize field of the type object.

TYPE\* **PyObject\_NewVar**(TYPE, PyTypeObject \*type, Py\_ssize\_t size)

Return value: New reference. Allocate a new Python object using the C structure type TYPE and the Python type object type. Fields not defined by the Python object header are not initialized. The allocated memory allows for the TYPE structure plus size fields of the size given by the tp\_itemsize field of type. This is useful for implementing objects like tuples, which are able to determine their size at construction time. Embedding the array of fields into the same allocation decreases the number of allocations, improving the memory management efficiency.

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

## void PyObject\_Del(PyObject \*op)

Releases memory allocated to an object using PyObject\_New() or PyObject\_NewVar(). This is normally called from the tp\_dealloc handler specified in the object’s type. The fields of the object should not be accessed after this call as the memory is no longer a valid Python object.

<!-- page: 134 -->

PyObject\* **Py\_InitModule**(char \*name, PyMethodDef \*methods)

Return value: Borrowed reference. Create a new module object based on a name and table of functions, returning the new module object.

Changed in version 2.3: Older versions of Python did not support NULL as the value for the methods argument.

PyObject\* **Py\_InitModule3**(char \*name, PyMethodDef \*methods, char \*doc)

Return value: Borrowed reference. Create a new module object based on a name and table of functions, returning the new module object. If doc is non-NULL, it will be used to define the docstring for the module.

Changed in version 2.3: Older versions of Python did not support NULL as the value for the methods argument.

PyObject\* **Py\_InitModule4**(char \*name, PyMethodDef \*methods, char \*doc, PyObject \*self, int apiver)

Return value: Borrowed reference. Create a new module object based on a name and table of functions, returning the new module object. If doc is non-NULL, it will be used to define the docstring for the module. If self is non-NULL, it will be passed to the functions of the module as their (otherwise NULL) first parameter. (This was added as an experimental feature, and there are no known uses in the current version of Python.) For apiver, the only value which should be passed is defined by the constant PYTHON\_API\_VERSION.

**Note:** Most uses of this function should probably be using the Py\_InitModule3() instead; only use this if you are sure you need it.

Changed in version 2.3: Older versions of Python did not support NULL as the value for the methods argument.

## PyObject \_Py\_NoneStruct

Object which is visible in Python as None. This should only be accessed using the Py\_None macro, which evaluates to a pointer to this object.

## 10.2 Common Object Structures

There are a large number of structures which are used in the definition of object types for Python. This section describes these structures and how they are used.

All Python objects ultimately share a small number of fields at the beginning of the object’s representation in memory. These are represented by the PyObject and PyVarObject types, which are defined, in turn, by the expansions of some macros also used, whether directly or indirectly, in the definition of all other Python objects.

## PyObject

All object types are extensions of this type. This is a type which contains the information Python needs to treat a pointer to an object as an object. In a normal “release” build, it contains only the object’s reference count and a pointer to the corresponding type object. It corresponds to the fields defined by the expansion of the PyObject\_HEAD macro.

## PyVarObject

This is an extension of PyObject that adds the ob\_size field. This is only used for objects that have some notion of length. This type does not often appear in the Python/C API. It corresponds to the fields defined by the expansion of the PyObject\_VAR\_HEAD macro.

These macros are used in the definition of PyObject and PyVarObject:

## PyObject\_HEAD

This is a macro which expands to the declarations of the fields of the PyObject type; it is used when declaring new types which represent objects without a varying length. The specific fields it expands to depend on the definition of Py\_TRACE\_REFS. By default, that macro is not defined, and PyObject\_HEAD expands to:

<!-- page: 135 -->

```txt
Py_ssize_t ob_refcnt;
PyTypeObject *ob_type;
```

When Py\_TRACE\_REFS is defined, it expands to:

```c
PyObject *_ob_next, *_ob_prev;
Py_ssize_t ob_refcnt;
PyTypeObject *ob_type;
```

## PyObject\_VAR\_HEAD

This is a macro which expands to the declarations of the fields of the PyVarObject type; it is used when declaring new types which represent objects with a length that varies from instance to instance. This macro always expands to:

```c
PyObject_HEAD
Py_ssize_t ob_size;
```

Note that PyObject\_HEAD is part of the expansion, and that its own expansion varies depending on the definition of Py\_TRACE\_REFS.

## Py\_TYPE(o)

This macro is used to access the ob\_type member of a Python object. It expands to:

```txt
(((PyObject*) (o)) ->ob_type)
```

New in version 2.6.

## Py\_REFCNT(o)

This macro is used to access the ob\_refcnt member of a Python object. It expands to:

```lisp
(((PyObject*) (o)) ->ob_refcnt)
```

New in version 2.6.

## Py\_SIZE(o)

This macro is used to access the ob\_size member of a Python object. It expands to:

```c
(((PyVarObject*) (o)) ->ob_size)
```

New in version 2.6.

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

## PyCFunction

Type of the functions used to implement most Python callables in C. Functions of this type take two PyObject\* parameters and return one such value. If the return value is NULL, an exception shall have been set. If not NULL,

<!-- page: 136 -->

the return value is interpreted as the return value of the function as exposed in Python. The function must return a new reference.

## PyMethodDef

Structure used to describe a method of an extension type. This structure has four fields:

| Field | C Type | Meaning |
| --- | --- | --- |
| ml_name | char * | name of the method |
| ml_meth | PyCFunction | pointer to the C implementation |
| ml_flags | int | flag bits indicating how the call should be constructed |
| ml_doc | char * | points to the contents of the docstring |

The ml\_meth is a C function pointer. The functions may be of different types, but they always return PyObject\*. If the function is not of the PyCFunction, the compiler will require a cast in the method table. Even though PyCFunction defines the first parameter as PyObject\*, it is common that the method implementation uses the specific C type of the self object.

The ml\_flags field is a bitfield which can include the following flags. The individual flags indicate either a calling convention or a binding convention. Of the calling convention flags, only METH\_VARARGS and METH\_KEYWORDS can be combined. Any of the calling convention flags can be combined with a binding flag.

## METH\_VARARGS

This is the typical calling convention, where the methods have the type PyCFunction. The function expects two PyObject\* values. The first one is the self object for methods; for module functions, it is the module object. The second parameter (often called args) is a tuple object representing all arguments. This parameter is typically processed using PyArg\_ParseTuple() or PyArg\_UnpackTuple().

## METH\_KEYWORDS

Methods with these flags must be of type PyCFunctionWithKeywords. The function expects three parameters: self, args, and a dictionary of all the keyword arguments. The flag is typically combined with METH\_VARARGS, and the parameters are typically processed using PyArg\_ParseTupleAndKeywords().

## METH\_NOARGS

Methods without parameters don’t need to check whether arguments are given if they are listed with the METH\_NOARGS flag. They need to be of type PyCFunction. The first parameter is typically named self and will hold a reference to the module or object instance. In all cases the second parameter will be NULL.

## METH\_O

Methods with a single object argument can be listed with the METH\_O flag, instead of invoking PyArg\_ParseTuple() with a "O" argument. They have the type PyCFunction, with the self parameter, and a PyObject\* parameter representing the single argument.

## METH\_OLDARGS

This calling convention is deprecated. The method must be of type PyCFunction. The second argument is NULL if no arguments are given, a single object if exactly one argument is given, and a tuple of objects if more than one argument is given. There is no way for a function using this convention to distinguish between a call with multiple arguments and a call with a tuple as the only argument.

These two constants are not used to indicate the calling convention but the binding when use with methods of classes. These may not be used for functions defined for modules. At most one of these flags may be set for any given method.

## METH\_CLASS

The method will be passed the type object as the first parameter rather than an instance of the type. This is used to create class methods, similar to what is created when using the classmethod() built-in function.

New in version 2.3.

<!-- page: 137 -->

## METH\_STATIC

The method will be passed NULL as the first parameter rather than an instance of the type. This is used to create static methods, similar to what is created when using the staticmethod() built-in function.

New in version 2.3.

One other constant controls whether a method is loaded in place of another definition with the same method name.

## METH\_COEXIST

The method will be loaded in place of existing definitions. Without METH\_COEXIST, the default is to skip repeated definitions. Since slot wrappers are loaded before the method table, the existence of a sq\_contains slot, for example, would generate a wrapped method named \_\_contains\_\_() and preclude the loading of a corresponding PyCFunction with the same name. With the flag defined, the PyCFunction will be loaded in place of the wrapper object and will co-exist with the slot. This is helpful because calls to PyCFunctions are optimized more than wrapper object calls.

New in version 2.4.

## PyMemberDef

Structure which describes an attribute of a type which corresponds to a C struct member. Its fields are:

| Field | C Type | Meaning |
| --- | --- | --- |
| name | char * | name of the member |
| type | int | the type of the member in the C struct |
| offset | Py_ssize_t | the offset in bytes that the member is located on the type's object struct |
| flags | int | flag bits indicating if the field should be read-only or writable |
| doc | char * | points to the contents of the docstring |

type can be one of many T\_ macros corresponding to various C types. When the member is accessed in Python, it will be converted to the equivalent Python type.

| Macro name | C type |
| --- | --- |
| T_SHORT | short |
| T_INT | int |
| T_LONG | long |
| T_FLOAT | float |
| T_DOUBLE | double |
| T_STRING | char * |
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

<!-- page: 138 -->

flags can be 0 for write and read access or READONLY for read-only access. Using T\_STRING for type implies READONLY. Only T\_OBJECT and T\_OBJECT\_EX members can be deleted. (They are set to NULL).

## PyGetSetDef

Structure to define property-like access for a type. See also description of the PyTypeObject.tp\_getset slot.

| Field | C Type | Meaning |
| --- | --- | --- |
| name | char * | attribute name |
| get | getter | C Function to get the attribute |
| set | setter | optional C function to set or delete the attribute, if omitted the attribute is readonly |
| doc | char * | optional docstring |
| closure | void * | optional function pointer, providing additional data for getter and setter |

The get function takes one PyObject\* parameter (the instance) and a function pointer (the associated closure):

```txt
typedef PyObject *(*getter)(PyObject *, void *);
```

It should return a new reference on success or NULL with a set exception on failure.

set functions take two PyObject\* parameters (the instance and the value to be set) and a function pointer (the associated closure):

```txt
typedef int (*setter) (PyObject *, PyObject *, void *);
```

In case the attribute should be deleted the second parameter is NULL. Should return 0 on success or -1 with a set exception on failure.

PyObject\* **Py\_FindMethod**(PyMethodDef table[], PyObject \*ob, char \*name)

Return value: New reference. Return a bound method object for an extension type implemented in C. This can be useful in the implementation of a tp\_getattro or tp\_getattr handler that does not use the PyObject\_GenericGetAttr() function.

## 10.3 Type Objects

Perhaps one of the most important structures of the Python object system is the structure that defines a new type: the PyTypeObject structure. Type objects can be handled using any of the PyObject\_\*() or PyType\_\*() functions, but do not offer much that’s interesting to most Python applications. These objects are fundamental to how objects behave, so they are very important to the interpreter itself and to any extension module that implements new types.

Type objects are fairly large compared to most of the standard types. The reason for the size is that each type object stores a large number of values, mostly C function pointers, each of which implements a small part of the type’s functionality. The fields of the type object are examined in detail in this section. The fields will be described in the order in which they occur in the structure.

Typedefs: unaryfunc, binaryfunc, ternaryfunc, inquiry, coercion, intargfunc, intintargfunc, intobjargproc, intintobjargproc, objobjargproc, destructor, freefunc, printfunc, getattrfunc, getattrofunc, setattrfunc, setattrofunc, cmpfunc, reprfunc, hashfunc

The structure definition for PyTypeObject can be found in Include/object.h. For convenience of reference, this repeats the definition found there:

<!-- page: 139 -->

```c
typedef struct _typeobject {
    PyObject_VAR_HEAD
    char *tp_name; /* For printing, in format "<module>.<name>" */
    int tp_basicsize, tp_itemsize; /* For allocation */

    /* Methods to implement standard operations */

    destructor tp_dealloc;
    printfunc tp_print;
    getattrfunc tp_getattr;
    setattrfunc tp_setattr;
    cmpfunc tp_compare;
    reprfunc tp_repr;

    /* Method suites for standard classes */

    PyNumberMethods *tp_as_number;
    PySequenceMethods *tp_as_sequence;
    PyMappingMethods *tp_as_mapping;

    /* More standard operations (here for binary compatibility) */

    hashfunc tp_hash;
    ternaryfunc tp_call;
    reprfunc tp_str;
    getattrofunc tp_getattro;
    setattrofunc tp_setattro;

    /* Functions to access object as input/output buffer */
    PyBufferProcs *tp_as_buffer;

    /* Flags to define presence of optional/expanded features */
    long tp_flags;

    char *tp_doc; /* Documentation string */

    /* Assigned meaning in release 2.0 */
    /* call function for all accessible objects */
    traverseproc tp_traverse;

    /* delete references to contained objects */
    inquiry tp_clear;

    /* Assigned meaning in release 2.1 */
    /* rich comparisons */
    richcmpfunc tp_richcompare;

    /* weak reference enabler */
    long tp_weaklistoffset;

    /* Added in release 2.2 */
    /* Iterators */
    getiterfunc tp_iter;
    iternextfunc tp_iternext;

    /* Attribute descriptor and subclassing stuff */
    struct PyMethodDef *tp_methods;
```

(continues on next page)

<!-- page: 140 -->

(continued from previous page)

```c
struct PyMemberDef *tp_members;
struct PyGetSetDef *tp_getset;
struct _typeobject *tp_base;
PyObject *tp_dict;
descrgetfunc tp_descr_get;
descrsetfunc tp_descr_set;
long tp_dictoffset;
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

} PyTypeObject;
```

The type object structure extends the PyVarObject structure. The ob\_size field is used for dynamic types (created by type\_new(), usually called from a class statement). Note that PyType\_Type (the metatype) initializes tp\_itemsize, which means that its instances (i.e. type objects) must have the ob\_size field.

## PyObject\* PyObject.\_ob\_next

## PyObject\* PyObject.\_ob\_prev

These fields are only present when the macro Py\_TRACE\_REFS is defined. Their initialization to NULL is taken care of by the PyObject\_HEAD\_INIT macro. For statically allocated objects, these fields always remain NULL. For dynamically allocated objects, these two fields are used to link the object into a doubly-linked list of all live objects on the heap. This could be used for various debugging purposes; currently the only use is to print the objects that are still alive at the end of a run when the environment variable PYTHONDUMPREFS is set.

These fields are not inherited by subtypes.

## Py\_ssize\_t PyObject.ob\_refcnt

This is the type object’s reference count, initialized to 1 by the PyObject\_HEAD\_INIT macro. Note that for statically allocated type objects, the type’s instances (objects whose ob\_type points back to the type) do not count as references. But for dynamically allocated type objects, the instances do count as references.

This field is not inherited by subtypes.

Changed in version 2.5: This field used to be an int type. This might require changes in your code for properly supporting 64-bit systems.

## PyTypeObject\* PyObject.ob\_type

This is the type’s type, in other words its metatype. It is initialized by the argument to the PyObject\_HEAD\_INIT macro, and its value should normally be &PyType\_Type. However, for dynamically loadable extension modules that must be usable on Windows (at least), the compiler complains that this is not a valid initializer. Therefore, the convention is to pass NULL to the PyObject\_HEAD\_INIT macro and to initialize this field explicitly at the start of the module’s initialization function, before doing anything else. This is typically done like this:

```txt
Foo_Type.ob_type = &PyType_Type;
```

This should be done before any instances of the type are created. PyType\_Ready() checks if ob\_type is NULL, and if so, initializes it: in Python 2.2, it is set to &PyType\_Type; in Python 2.2.1 and later it is initialized to the ob\_type field of the base class. PyType\_Ready() will not change this field if it is non-zero.

<!-- page: 141 -->

In Python 2.2, this field is not inherited by subtypes. In 2.2.1, and in 2.3 and beyond, it is inherited by subtypes.

## Py\_ssize\_t PyVarObject.ob\_size

For statically allocated type objects, this should be initialized to zero. For dynamically allocated type objects, this field has a special internal meaning.

This field is not inherited by subtypes.

## char\* PyTypeObject.tp\_name

Pointer to a NUL-terminated string containing the name of the type. For types that are accessible as module globals, the string should be the full module name, followed by a dot, followed by the type name; for built-in types, it should be just the type name. If the module is a submodule of a package, the full package name is part of the full module name. For example, a type named T defined in module M in subpackage Q in package P should have the tp\_name initializer "P.Q.M.T".

For dynamically allocated type objects, this should just be the type name, and the module name explicitly stored in the type dict as the value for key '\_\_module\_\_'.

For statically allocated type objects, the tp\_name field should contain a dot. Everything before the last dot is made accessible as the \_\_module\_\_ attribute, and everything after the last dot is made accessible as the \_\_name\_\_ attribute.

If no dot is present, the entire tp\_name field is made accessible as the \_\_name\_\_ attribute, and the \_\_module\_\_ attribute is undefined (unless explicitly set in the dictionary, as explained above). This means your type will be impossible to pickle. Additionally, it will not be listed in module documentations created with pydoc.

This field is not inherited by subtypes.

## Py\_ssize\_t PyTypeObject.tp\_basicsize

## Py\_ssize\_t PyTypeObject.tp\_itemsize

These fields allow calculating the size in bytes of instances of the type.

There are two kinds of types: types with fixed-length instances have a zero tp\_itemsize field, types with variable-length instances have a non-zero tp\_itemsize field. For a type with fixed-length instances, all instances have the same size, given in tp\_basicsize.

For a type with variable-length instances, the instances must have an ob\_size field, and the instance size is tp\_basicsize plus N times tp\_itemsize, where N is the “length” of the object. The value of N is typically stored in the instance’s ob\_size field. There are exceptions: for example, long ints use a negative ob\_size to indicate a negative number, and N is abs(ob\_size) there. Also, the presence of an ob\_size field in the instance layout doesn’t mean that the instance structure is variable-length (for example, the structure for the list type has fixed-length instances, yet those instances have a meaningful ob\_size field).

The basic size includes the fields in the instance declared by the macro PyObject\_HEAD or PyObject\_VAR\_HEAD (whichever is used to declare the instance struct) and this in turn includes the \_ob\_prev and \_ob\_next fields if they are present. This means that the only correct way to get an initializer for the tp\_basicsize is to use the sizeof operator on the struct used to declare the instance layout. The basic size does not include the GC header size (this is new in Python 2.2; in 2.1 and 2.0, the GC header size was included in tp\_basicsize).

These fields are inherited separately by subtypes. If the base type has a non-zero tp\_itemsize, it is generally not safe to set tp\_itemsize to a different non-zero value in a subtype (though this depends on the implementation of the base type).

A note about alignment: if the variable items require a particular alignment, this should be taken care of by the value of tp\_basicsize. Example: suppose a type implements an array of double. tp\_itemsize is sizeof(double). It is the programmer’s responsibility that tp\_basicsize is a multiple of sizeof(double) (assuming this is the alignment requirement for double).

<!-- page: 142 -->

## destructor PyTypeObject.tp\_dealloc

A pointer to the instance destructor function. This function must be defined unless the type guarantees that its instances will never be deallocated (as is the case for the singletons None and Ellipsis).

The destructor function is called by the Py\_DECREF() and Py\_XDECREF() macros when the new reference count is zero. At this point, the instance is still in existence, but there are no references to it. The destructor function should free all references which the instance owns, free all memory buffers owned by the instance (using the freeing function corresponding to the allocation function used to allocate the buffer), and finally (as its last action) call the type’s tp\_free function. If the type is not subtypable (doesn’t have the Py\_TPFLAGS\_BASETYPE flag bit set), it is permissible to call the object deallocator directly instead of via tp\_free. The object deallocator should be the one used to allocate the instance; this is normally PyObject\_Del() if the instance was allocated using PyObject\_New() or PyObject\_VarNew(), or PyObject\_GC\_Del() if the instance was allocated using PyObject\_GC\_New() or PyObject\_GC\_NewVar().

This field is inherited by subtypes.

## printfunc PyTypeObject.tp\_print

An optional pointer to the instance print function.

The print function is only called when the instance is printed to a real file; when it is printed to a pseudo-file (like a StringIO instance), the instance’s tp\_repr or tp\_str function is called to convert it to a string. These are also called when the type’s tp\_ print field is NULL. A type should never implement tp\_print in a way that produces different output than tp\_repr or tp\_str would.

The print function is called with the same signature as PyObject\_Print(): int tp\_print(PyObject \*self, FILE \*file, int flags). The self argument is the instance to be printed. The file argument is the stdio file to which it is to be printed. The flags argument is composed of flag bits. The only flag bit currently defined is Py\_PRINT\_RAW. When the Py\_PRINT\_RAW flag bit is set, the instance should be printed the same way as tp\_str would format it; when the Py\_PRINT\_RAW flag bit is clear, the instance should be printed the same was as tp\_repr would format it. It should return -1 and set an exception condition when an error occurred during the comparison.

It is possible that the tp\_print field will be deprecated. In any case, it is recommended not to define tp\_print, but instead to rely on tp\_repr and tp\_str for printing.

This field is inherited by subtypes.

## getattrfunc PyTypeObject.tp\_getattr

An optional pointer to the get-attribute-string function.

This field is deprecated. When it is defined, it should point to a function that acts the same as the tp\_getattro function, but taking a C string instead of a Python string object to give the attribute name. The signature is

```txt
PyObject * tp_getattr(PyObject *o, char *attr_name);
```

This field is inherited by subtypes together with tp\_getattro: a subtype inherits both tp\_getattr and tp\_getattro from its base type when the subtype’s tp\_getattr and tp\_getattro are both NULL.

## setattrfunc PyTypeObject.tp\_setattr

An optional pointer to the function for setting and deleting attributes.

This field is deprecated. When it is defined, it should point to a function that acts the same as the tp\_ \_setattro function, but taking a C string instead of a Python string object to give the attribute name. The signature is

```txt
PyObject * tp_setattr(PyObject *o, char *attr_name, PyObject *v);
```

The v argument is set to NULL to delete the attribute. This field is inherited by subtypes together with tp\_setattro: a subtype inherits both tp\_ setattr and tp\_setattro from its base type when the subtype’s tp\_setattr and tp\_ setattro are both NULL.

<!-- page: 143 -->

## cmpfunc PyTypeObject.tp\_compare

An optional pointer to the three-way comparison function.

The signature is the same as for PyObject\_Compare(). The function should return 1 if self greater than other, 0 if self is equal to other, and -1 if self less than other. It should return -1 and set an exception condition when an error occurred during the comparison.

This field is inherited by subtypes together with tp\_richcompare and tp\_hash: a subtypes inherits all three of tp\_compare, tp\_richcompare, and tp\_hash when the subtype’s tp\_compare, tp\_richcompare, and tp\_hash are all NULL.

## reprfunc PyTypeObject.tp\_repr

An optional pointer to a function that implements the built-in function repr().

The signature is the same as for PyObject\_Repr(); it must return a string or a Unicode object. Ideally, this function should return a string that, when passed to eval(), given a suitable environment, returns an object with the same value. If this is not feasible, it should return a string starting with '<' and ending with '>' from which both the type and the value of the object can be deduced.

When this field is not set, a string of the form <%s object at %p> is returned, where %s is replaced by the type name, and %p by the object’s memory address.

This field is inherited by subtypes.

## PyNumberMethods\* tp\_as\_number

Pointer to an additional structure that contains fields relevant only to objects which implement the number protocol. These fields are documented in Number Object Structures.

The tp\_as\_number field is not inherited, but the contained fields are inherited individually.

## PySequenceMethods\* tp\_as\_sequence

Pointer to an additional structure that contains fields relevant only to objects which implement the sequence protocol. These fields are documented in Sequence Object Structures.

The tp\_as\_sequence field is not inherited, but the contained fields are inherited individually.

## PyMappingMethods\* tp\_as\_mapping

Pointer to an additional structure that contains fields relevant only to objects which implement the mapping protocol. These fields are documented in Mapping Object Structures.

The tp\_as\_mapping field is not inherited, but the contained fields are inherited individually.

## hashfunc PyTypeObject.tp\_hash

An optional pointer to a function that implements the built-in function hash().

The signature is the same as for PyObject\_Hash(); it must return a C long. The value -1 should not be returned as a normal return value; when an error occurs during the computation of the hash value, the function should set an exception and return -1.

This field can be set explicitly to PyObject\_HashNotImplemented() to block inheritance of the hash method from a parent type. This is interpreted as the equivalent of \_\_hash\_\_ = None at the Python level, causing isinstance(o, collections.Hashable) to correctly return False. Note that the converse is also true - setting \_\_hash\_\_ = None on a class at the Python level will result in the tp\_hash slot being set to PyObject\_HashNotImplemented().

When this field is not set, two possibilities exist: if the tp\_compare and tp\_richcompare fields are both NULL, a default hash value based on the object’s address is returned; otherwise, a TypeError is raised.

This field is inherited by subtypes together with tp\_richcompare and tp\_compare: a subtypes inherits all three of tp\_compare, tp\_richcompare, and tp\_hash, when the subtype’s tp\_compare, tp\_richcompare and tp\_hash are all NULL.

<!-- page: 144 -->

## ternaryfunc PyTypeObject.tp\_call

An optional pointer to a function that implements calling the object. This should be NULL if the object is not callable. The signature is the same as for PyObject\_Call().

This field is inherited by subtypes.

## reprfunc PyTypeObject.tp\_str

An optional pointer to a function that implements the built-in operation str(). (Note that str is a type now, and str() calls the constructor for that type. This constructor calls PyObject\_Str() to do the actual work, and PyObject\_Str() will call this handler.)

The signature is the same as for PyObject\_Str(); it must return a string or a Unicode object. This function should return a “friendly” string representation of the object, as this is the representation that will be used by the print statement.

When this field is not set, PyObject\_Repr() is called to return a string representation.

This field is inherited by subtypes.

## getattrofunc PyTypeObject.tp\_getattro

An optional pointer to the get-attribute function.

The signature is the same as for PyObject\_GetAttr(). It is usually convenient to set this field to PyObject\_GenericGetAttr(), which implements the normal way of looking for object attributes.

This field is inherited by subtypes together with tp\_getattr: a subtype inherits both tp\_getattr and tp\_getattro from its base type when the subtype’s tp\_getattr and tp\_getattro are both NULL.

## setattrofunc PyTypeObject.tp\_setattro

An optional pointer to the function for setting and deleting attributes.

The signature is the same as for PyObject\_SetAttr(), but setting v to NULL to delete an attribute must be supported. It is usually convenient to set this field to PyObject\_GenericSetAttr(), which implements the normal way of setting object attributes.

This field is inherited by subtypes together with tp\_setattr: a subtype inherits both tp\_setattr and tp\_setattro from its base type when the subtype’s tp\_setattr and tp\_setattro are both NULL.

## PyBufferProcs\* PyTypeObject.tp\_as\_buffer

Pointer to an additional structure that contains fields relevant only to objects which implement the buffer interface. These fields are documented in Buffer Object Structures.

The tp\_as\_buffer field is not inherited, but the contained fields are inherited individually.

## long PyTypeObject.tp\_flags

This field is a bit mask of various flags. Some flags indicate variant semantics for certain situations; others are used to indicate that certain fields in the type object (or in the extension structures referenced via tp\_as\_number, tp\_as\_sequence, tp\_as\_mapping, and tp\_as\_buffer) that were historically not always present are valid; if such a flag bit is clear, the type fields it guards must not be accessed and must be considered to have a zero or NULL value instead.

Inheritance of this field is complicated. Most flag bits are inherited individually, i.e. if the base type has a flag bit set, the subtype inherits this flag bit. The flag bits that pertain to extension structures are strictly inherited if the extension structure is inherited, i.e. the base type’s value of the flag bit is copied into the subtype together with a pointer to the extension structure. The Py\_TPFLAGS\_HAVE\_GC flag bit is inherited together with the tp\_traverse and tp\_clear fields, i.e. if the Py\_TPFLAGS\_HAVE\_GC flag bit is clear in the subtype and the tp\_traverse and tp\_clear fields in the subtype exist (as indicated by the Py\_TPFLAGS\_HAVE\_RICHCOMPARE flag bit) and have NULL values.

The following bit masks are currently defined; these can be ORed together using the | operator to form the value of the tp\_flags field. The macro PyType\_HasFeature() takes a type and a flags value, tp and f, and checks whether tp->tp\_flags & f is non-zero.

<!-- page: 145 -->

## Py\_TPFLAGS\_HAVE\_GETCHARBUFFER

If this bit is set, the PyBufferProcs struct referenced by tp\_as\_buffer has the bf\_getcharbuffer field.

## Py\_TPFLAGS\_HAVE\_SEQUENCE\_IN

If this bit is set, the PySequenceMethods struct referenced by tp\_as\_sequence has the sq\_contains field.

## Py\_TPFLAGS\_GC

This bit is obsolete. The bit it used to name is no longer in use. The symbol is now defined as zero.

## Py\_TPFLAGS\_HAVE\_INPLACEOPS

If this bit is set, the PySequenceMethods struct referenced by tp\_as\_sequence and the PyNumberMethods structure referenced by tp\_as\_number contain the fields for in-place operators. In particular, this means that the PyNumberMethods structure has the fields nb\_inplace\_add, nb\_inplace\_subtract, nb\_inplace\_multiply, nb\_inplace\_divide, nb\_inplace\_remainder, nb\_inplace\_power, nb\_inplace\_lshift, nb\_inplace\_rshift, nb\_inplace\_and, nb\_inplace\_xor, and nb\_inplace\_or; and the PySequenceMethods struct has the fields sq\_inplace\_concat and sq\_inplace\_repeat.

## Py\_TPFLAGS\_CHECKTYPES

If this bit is set, the binary and ternary operations in the PyNumberMethods structure referenced by tp\_as\_number accept arguments of arbitrary object types, and do their own type conversions if needed. If this bit is clear, those operations require that all arguments have the current type as their type, and the caller is supposed to perform a coercion operation first. This applies to nb\_add, nb\_subtract, nb\_multiply, nb\_divide, nb\_remainder, nb\_divmod, nb\_power, nb\_lshift, nb\_rshift, nb\_and, nb\_xor, and nb\_or.

## Py\_TPFLAGS\_HAVE\_RICHCOMPARE

If this bit is set, the type object has the tp\_richcompare field, as well as the tp\_traverse and the tp\_clear fields.

## Py\_TPFLAGS\_HAVE\_WEAKREFS

If this bit is set, the tp\_weaklistoffset field is defined. Instances of a type are weakly referenceable if the type’s tp\_weaklistoffset field has a value greater than zero.

## Py\_TPFLAGS\_HAVE\_ITER

If this bit is set, the type object has the tp\_iter and tp\_iternext fields.

## Py\_TPFLAGS\_HAVE\_CLASS

If this bit is set, the type object has several new fields defined starting in Python 2.2: tp\_methods, tp\_members, tp\_getset, tp\_base, tp\_dict, tp\_descr\_get, tp\_descr\_set, tp\_dictoffset, tp\_init, tp\_alloc, tp\_new, tp\_free, tp\_is\_gc, tp\_bases, tp\_mro, tp\_cache, tp\_subclasses, and tp\_weaklist.

## Py\_TPFLAGS\_HEAPTYPE

This bit is set when the type object itself is allocated on the heap. In this case, the ob\_type field of its instances is considered a reference to the type, and the type object is INCREF’ed when a new instance is created, and DECREF’ed when an instance is destroyed (this does not apply to instances of subtypes; only the type referenced by the instance’s ob\_type gets INCREF’ed or DECREF’ed).

## Py\_TPFLAGS\_BASETYPE

This bit is set when the type can be used as the base type of another type. If this bit is clear, the type cannot be subtyped (similar to a “final” class in Java).

## Py\_TPFLAGS\_READY

This bit is set when the type object has been fully initialized by PyType\_Ready().

<!-- page: 146 -->

## Py\_TPFLAGS\_READYING

This bit is set while PyType\_Ready() is in the process of initializing the type object.

## Py\_TPFLAGS\_HAVE\_GC

This bit is set when the object supports garbage collection. If this bit is set, instances must be created using PyObject\_GC\_New() and destroyed using PyObject\_GC\_Del(). More information in section Supporting Cyclic Garbage Collection. This bit also implies that the GC-related fields tp\_traverse and tp\_clear are present in the type object; but those fields also exist when Py\_TPFLAGS\_HAVE\_GC is clear but Py\_TPFLAGS\_HAVE\_RICHCOMPARE is set.

## Py\_TPFLAGS\_DEFAULT

This is a bitmask of all the bits that pertain to the existence of certain fields in the type object and its extension structures. Currently, it includes the following bits: Py\_TPFLAGS\_HAVE\_GETCHARBUFFER, Py\_TPFLAGS\_HAVE\_SEQUENCE\_IN, Py\_TPFLAGS\_HAVE\_INPLACEOPS, Py\_TPFLAGS\_HAVE\_RICHCOMPARE, Py\_TPFLAGS\_HAVE\_WEAKREFS, Py\_TPFLAGS\_HAVE\_ITER, and Py\_TPFLAGS\_HAVE\_CLASS.

## char\* PyTypeObject.tp\_doc

An optional pointer to a NUL-terminated C string giving the docstring for this type object. This is exposed as the \_\_doc\_\_ attribute on the type and instances of the type.

This field is not inherited by subtypes.

The following three fields only exist if the Py\_TPFLAGS\_HAVE\_RICHCOMPARE flag bit is set.

## traverseproc PyTypeObject.tp\_traverse

An optional pointer to a traversal function for the garbage collector. This is only used if the Py\_TPFLAGS\_HAVE\_GC flag bit is set. More information about Python’s garbage collection scheme can be found in section Supporting Cyclic Garbage Collection.

The tp\_traverse pointer is used by the garbage collector to detect reference cycles. A typical implementation of a tp\_traverse function simply calls Py\_VISIT() on each of the instance’s members that are Python objects. For example, this is function local\_traverse() from the thread extension module:

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

Note that Py\_VISIT() requires the visit and arg parameters to local\_traverse() to have these specific names; don’t name them just anything.

This field is inherited by subtypes together with tp\_clear and the Py\_TPFLAGS\_HAVE\_GC flag bit: the flag bit, tp\_traverse, and tp\_clear are all inherited from the base type if they are all zero in the subtype and the subtype has the Py\_TPFLAGS\_HAVE\_RICHCOMPARE flag bit set.

## inquiry PyTypeObject.tp\_clear

An optional pointer to a clear function for the garbage collector. This is only used if the Py\_TPFLAGS\_HAVE\_GC flag bit is set.

<!-- page: 147 -->

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

The tp\_ \_clear member function is used to break reference cycles in cyclic garbage detected by the garbage collector. Taken together, all tp\_ \_clear functions in the system must combine to break all reference cycles. This is subtle, and if in any doubt supply a tp\_clear function. For example, the tuple type does not implement a tp\_clear function, because it’s possible to prove that no reference cycle can be composed entirely of tuples. Therefore the tp\_clear functions of other types must be sufficient to break any cycle containing a tuple. This isn’t immediately obvious, and there’s rarely a good reason to avoid implementing tp\_cl ear.

Implementations of tp\_clear should drop the instance’s references to those of its members that may be Python objects, and set its pointers to those members to NULL, as in the following example:

The Py\_ \_CLEAR() macro should be used, because clearing references is delicate: the reference to the contained object must not be decremented until after the pointer to the contained object is set to NULL. This is because decrementing the reference count may cause the contained object to become trash, triggering a chain of reclamation activity that may include invoking arbitrary Python code (due to finalizers, or weakref callbacks, associated with the contained object). If it’s possible for such code to reference self again, it’s important that the pointer to the contained object be NULL at that time, so that self knows the contained object can no longer be used. The Py\_CLEAR() macro performs the operations in a safe order.

Because the goal of tp\_clear functions is to break reference cycles, it’s not necessary to clear contained objects like Python strings or Python integers, which can’t participate in reference cycles. On the other hand, it may be convenient to clear all contained Python objects, and write the type’s tp\_dealloc function to invoke tp\_clear.

More information about Python’s garbage collection scheme can be found in section Supporting Cyclic Garbage Collection.

This field is inherited by subtypes together with tp\_traverse and the Py\_TPFLAGS\_HAVE\_GC flag bit: the flag bit, tp\_traverse, and tp\_clear are all inherited from the base type if they are all zero in the subtype and the subtype has the Py\_TPFLAGS\_HAVE\_RICHCOMPARE flag bit set.

## richcmpfunc PyTypeObject.tp\_richcompare

An optional pointer to the rich comparison function, whose signature is PyObject \*tp\_richcompare(PyObject \*a, PyObject \*b, int op).

The function should return the result of the comparison (usually Py\_True or Py\_False). If the comparison is undefined, it must return Py\_NotImplemented, if another error occurred it must return NULL and set an exception condition.

**Note:** If you want to implement a type for which only a limited set of comparisons makes sense (e.g. == and !=, but not < and friends), directly raise TypeError in the rich comparison function.

This field is inherited by subtypes together with tp\_ compare and tp\_ \_hash: a subtype inherits all three of tp\_compare, tp\_rich compare, and tp\_hash , when the subtype’s tp\_compare, tp\_richcompare, and tp\_ hash are all NULL

The following constants are defined to be used as the third argument for tp\_ richcompare and for PyObject\_RichCompare():

<!-- page: 148 -->

| Constant | Comparison |
| --- | --- |
| Py_LT | &lt; |
| Py_LE | &lt;= |
| Py_EQ | == |
| Py_NE | != |
| Py_GT | > |
| Py_GE | >= |

The next field only exists if the Py\_TPFLAGS\_HAVE\_WEAKREFS flag bit is set.

## long PyTypeObject.tp\_weaklistoffset

If the instances of this type are weakly referenceable, this field is greater than zero and contains the offset in the instance structure of the weak reference list head (ignoring the GC header, if present); this offset is used by PyObject\_ClearWeakRefs() and the PyWeakref\_\*() functions. The instance structure needs to include a field of type PyObject\* which is initialized to NULL.

Do not confuse this field with tp\_weaklist; that is the list head for weak references to the type object itself.

This field is inherited by subtypes, but see the rules listed below. A subtype may override this offset; this means that the subtype uses a different weak reference list head than the base type. Since the list head is always found via tp\_weaklistoffset, this should not be a problem.

When a type defined by a class statement has no \_\_slots\_\_ declaration, and none of its base types are weakly referenceable, the type is made weakly referenceable by adding a weak reference list head slot to the instance layout and setting the tp\_weaklistoffset of that slot’s offset.

When a type’s \_\_slots\_\_ declaration contains a slot named \_\_weakref\_\_, that slot becomes the weak reference list head for instances of the type, and the slot’s offset is stored in the type’s tp\_weaklistoffset.

When a type’s \_\_slots\_\_ declaration does not contain a slot named \_\_weakref\_\_, the type inherits its tp\_weaklistoffset from its base type.

The next two fields only exist if the Py\_TPFLAGS\_HAVE\_ITER flag bit is set.

## getiterfunc PyTypeObject.tp\_iter

An optional pointer to a function that returns an iterator for the object. Its presence normally signals that the instances of this type are iterable (although sequences may be iterable without this function, and classic instances always have this function, even if they don’t define an \_\_iter\_\_() method).

This function has the same signature as PyObject\_GetIter().

This field is inherited by subtypes.

## iternextfunc PyTypeObject.tp\_iternext

An optional pointer to a function that returns the next item in an iterator. When the iterator is exhausted, it must return NULL; a StopIteration exception may or may not be set. When another error occurs, it must return NULL too. Its presence normally signals that the instances of this type are iterators (although classic instances always have this function, even if they don’t define a next() method).

Iterator types should also define the tp\_iter function, and that function should return the iterator instance itself (not a new iterator instance).

This function has the same signature as PyIter\_Next().

This field is inherited by subtypes.

The next fields, up to and including tp\_weaklist, only exist if the Py\_TPFLAGS\_HAVE\_CLASS flag bit is set.

## struct PyMethodDef\* PyTypeObject.tp\_methods

An optional pointer to a static NULL-terminated array of PyMethodDef structures, declaring regular methods of this type.

<!-- page: 149 -->

For each entry in the array, an entry is added to the type’s dictionary (see tp\_dict below) containing a method descriptor.

This field is not inherited by subtypes (methods are inherited through a different mechanism).

## struct PyMemberDef\* PyTypeObject.tp\_members

An optional pointer to a static NULL-terminated array of PyMemberDef structures, declaring regular data members (fields or slots) of instances of this type.

For each entry in the array, an entry is added to the type’s dictionary (see tp\_dict below) containing a member descriptor.

This field is not inherited by subtypes (members are inherited through a different mechanism).

## struct PyGetSetDef\* PyTypeObject.tp\_getset

An optional pointer to a static NULL-terminated array of PyGetSetDef structures, declaring computed attributes of instances of this type.

For each entry in the array, an entry is added to the type’s dictionary (see tp\_dict below) containing a getset descriptor.

This field is not inherited by subtypes (computed attributes are inherited through a different mechanism).

## PyTypeObject\* PyTypeObject.tp\_base

An optional pointer to a base type from which type properties are inherited. At this level, only single inheritance is supported; multiple inheritance require dynamically creating a type object by calling the metatype.

This field is not inherited by subtypes (obviously), but it defaults to &PyBaseObject\_Type (which to Python programmers is known as the type object).

## PyObject\* PyTypeObject.tp\_dict

The type’s dictionary is stored here by PyType\_Ready().

This field should normally be initialized to NULL before PyType\_Ready is called; it may also be initialized to a dictionary containing initial attributes for the type. Once PyType\_Ready() has initialized the type, extra attributes for the type may be added to this dictionary only if they don’t correspond to overloaded operations (like add\_\_()).

This field is not inherited by subtypes (though the attributes defined in here are inherited through a different mechanism).

## descrgetfunc PyTypeObject.tp\_descr\_get

An optional pointer to a “descriptor get” function.

The function signature is

```c
PyObject * tp_descr_get(PyObject *self, PyObject *obj, PyObject *type);
```

This field is inherited by subtypes.

## descrsetfunc PyTypeObject.tp\_descr\_set

An optional pointer to a function for setting and deleting a descriptor’s value.

The function signature is

```c
int tp_descr_set(PyObject *self, PyObject *obj, PyObject *value);
```

The value argument is set to NULL to delete the value. This field is inherited by subtypes.

## long PyTypeObject.tp\_dictoffset

If the instances of this type have a dictionary containing instance variables, this field is non-zero and contains the offset in the instances of the type of the instance variable dictionary; this offset is used by PyObject\_GenericGetAttr().

<!-- page: 150 -->

Do not confuse this field with tp\_dict; that is the dictionary for attributes of the type object itself.

If the value of this field is greater than zero, it specifies the offset from the start of the instance structure. If the value is less than zero, it specifies the offset from the end of the instance structure. A negative offset is more expensive to use, and should only be used when the instance structure contains a variable-length part. This is used for example to add an instance variable dictionary to subtypes of str or tuple. Note that the tp\_basicsize field should account for the dictionary added to the end in that case, even though the dictionary is not included in the basic object layout. On a system with a pointer size of 4 bytes, tp\_dictoffset should be set to -4 to indicate that the dictionary is at the very end of the structure.

The real dictionary offset in an instance can be computed from a negative tp\_dictoffset as follows:

```python
dictoffset = tp_basicsize + abs(ob_size)*tp_itemsize + tp_dictoffset
if dictoffset is not aligned on sizeof(void*):
    round up to sizeof(void*)
```

where tp\_basicsize, tp\_itemsize and tp\_dictoffset are taken from the type object, and ob\_size is taken from the instance. The absolute value is taken because long ints use the sign of ob\_size to store the sign of the number. (There’s never a need to do this calculation yourself; it is done for you by \_PyObject\_GetDictPtr().)

This field is inherited by subtypes, but see the rules listed below. A subtype may override this offset; this means that the subtype instances store the dictionary at a difference offset than the base type. Since the dictionary is always found via tp\_dictoffset, this should not be a problem.

When a type defined by a class statement has no \_\_slots\_\_ declaration, and none of its base types has an instance variable dictionary, a dictionary slot is added to the instance layout and the tp\_dictoffset is set to that slot’s offset.

When a type defined by a class statement has a \_\_slots\_\_ declaration, the type inherits its tp\_dictoffset from its base type.

(Adding a slot named \_\_dict\_\_ to the \_\_slots\_\_ declaration does not have the expected effect, it just causes confusion. Maybe this should be added as a feature just like \_\_weakref\_\_ though.)

## initproc PyTypeObject.tp\_init

An optional pointer to an instance initialization function.

This function corresponds to the \_\_init\_\_() method of classes. Like \_\_init\_\_(), it is possible to create an instance without calling \_\_init\_\_(), and it is possible to reinitialize an instance by calling its \_\_init\_\_() method again.

The function signature is

```c
int tp_init(PyObject *self, PyObject *args, PyObject *kwds)
```

The self argument is the instance to be initialized; the args and kwds arguments represent positional and keyword arguments of the call to \_\_init\_\_().

The tp\_init function, if not NULL, is called when an instance is created normally by calling its type, after the type’s tp\_new function has returned an instance of the type. If the tp\_new function returns an instance of some other type that is not a subtype of the original type, no tp\_init function is called; if tp\_new returns an instance of a subtype of the original type, the subtype’s tp\_init is called. (VERSION NOTE: described here is what is implemented in Python 2.2.1 and later. In Python 2.2, the tp\_init of the type of the object returned by tp\_new was always called, if not NULL.)

This field is inherited by subtypes.

## allocfunc PyTypeObject.tp\_alloc

An optional pointer to an instance allocation function.

<!-- page: 151 -->

The function signature is

```c
PyObject *tp_alloc(PyTypeObject *self, Py_ssize_t nitems)
```

The purpose of this function is to separate memory allocation from memory initialization. It should return a pointer to a block of memory of adequate length for the instance, suitably aligned, and initialized to zeros, but with ob\_refcnt set to 1 and ob\_type set to the type argument. If the type’s tp\_itemsize is non-zero, the object’s ob\_size field should be initialized to nitems and the length of the allocated memory block should be tp\_basicsize + nitems\*tp\_itemsize, rounded up to a multiple of sizeof(void\*); otherwise, nitems is not used and the length of the block should be tp\_basicsize.

Do not use this function to do any other instance initialization, not even to allocate additional memory; that should be done by tp\_new.

This field is inherited by static subtypes, but not by dynamic subtypes (subtypes created by a class statement); in the latter, this field is always set to PyType\_GenericAlloc(), to force a standard heap allocation strategy. That is also the recommended value for statically defined types.

## newfunc PyTypeObject.tp\_new

An optional pointer to an instance creation function.

If this function is NULL for a particular type, that type cannot be called to create new instances; presumably there is some other way to create instances, like a factory function.

The function signature is

```c
PyObject *tp_new(PyTypeObject *subtype, PyObject *args, PyObject *kwds)
```

The subtype argument is the type of the object being created; the args and kwds arguments represent positional and keyword arguments of the call to the type. Note that subtype doesn’t have to equal the type whose tp\_new function is called; it may be a subtype of that type (but not an unrelated type).

The tp\_new function should call subtype->tp\_alloc(subtype, nitems) to allocate space for the object, and then do only as much further initialization as is absolutely necessary. Initialization that can safely be ignored or repeated should be placed in the tp\_init handler. A good rule of thumb is that for immutable types, all initialization should take place in tp\_new, while for mutable types, most initialization should be deferred to tp\_init.

This field is inherited by subtypes, except it is not inherited by static types whose tp\_base is NULL or &PyBaseObject\_Type. The latter exception is a precaution so that old extension types don’t become callable simply by being linked with Python 2.2.

## destructor PyTypeObject.tp\_free

An optional pointer to an instance deallocation function.

The signature of this function has changed slightly: in Python 2.2 and 2.2.1, its signature is destructor:

```txt
void tp_free(PyObject *)
```

In Python 2.3 and beyond, its signature is freefunc:

```txt
void tp_free(void *)
```

The only initializer that is compatible with both versions is \_PyObject\_Del, whose definition has suitably adapted in Python 2.3.

This field is inherited by static subtypes, but not by dynamic subtypes (subtypes created by a class statement); in the latter, this field is set to a deallocator suitable to match PyType\_GenericAlloc() and the value of the Py\_TPFLAGS\_HAVE\_GC flag bit.

<!-- page: 152 -->

## inquiry PyTypeObject.tp\_is\_gc

An optional pointer to a function called by the garbage collector.

The garbage collector needs to know whether a particular object is collectible or not. Normally, it is sufficient to look at the object’s type’s tp\_flags field, and check the Py\_TPFLAGS\_HAVE\_GC flag bit. But some types have a mixture of statically and dynamically allocated instances, and the statically allocated instances are not collectible. Such types should define this function; it should return 1 for a collectible instance, and 0 for a non-collectible instance. The signature is

```lisp
int tp_is_gc(PyObject *self)
```

(The only example of this are types themselves. The metatype, PyType\_Type, defines this function to distinguish between statically and dynamically allocated types.)

This field is inherited by subtypes. (VERSION NOTE: in Python 2.2, it was not inherited. It is inherited in 2.2.1 and later versions.)

## PyObject\* PyTypeObject.tp\_bases

Tuple of base types.

This is set for types created by a class statement. It should be NULL for statically defined types.

This field is not inherited.

## PyObject\* PyTypeObject.tp\_mro

Tuple containing the expanded set of base types, starting with the type itself and ending with object, in Method Resolution Order.

This field is not inherited; it is calculated fresh by PyType\_Ready().

PyObject\* **PyTypeObject.tp\_cache** Unused. Not inherited. Internal use only.

## PyObject\* PyTypeObject.tp\_subclasses

List of weak references to subclasses. Not inherited. Internal use only.

## PyObject\* PyTypeObject.tp\_weaklist

Weak reference list head, for weak references to this type object. Not inherited. Internal use only.

The remaining fields are only defined if the feature test macro COUNT\_ALLOCS is defined, and are for internal use only. They are documented here for completeness. None of these fields are inherited by subtypes. See the PYTHONSHOWALLOCCOUNT environment variable.

Py\_ssize\_t **PyTypeObject.tp\_allocs** Number of allocations.

Py\_ssize\_t **PyTypeObject.tp\_frees** Number of frees.

Py\_ssize\_t **PyTypeObject.tp\_maxalloc** Maximum simultaneously allocated objects.

PyTypeObject\* **PyTypeObject.tp\_next** Pointer to the next type object with a non-zero tp\_allocs field.

Also, note that, in a garbage collected Python, tp\_dealloc may be called from any Python thread, not just the thread which created the object (if the object becomes part of a refcount cycle, that cycle might be collected by a garbage collection on any thread). This is not a problem for Python API calls, since the thread on which tp\_dealloc is called will own the Global Interpreter Lock (GIL). However, if the object being destroyed in turn destroys objects from some other C or C++ library, care should be taken to ensure that destroying those objects on the thread which called tp\_dealloc will not violate any assumptions of the library.

<!-- page: 153 -->

## 10.4 Number Object Structures

## PyNumberMethods

This structure holds pointers to the functions which an object uses to implement the number protocol. Almost every function below is used by the function of similar name documented in the Number Protocol section.

Here is the structure definition:

```txt
typedef struct {
    binaryfunc nb_add;
    binaryfunc nb_subtract;
    binaryfunc nb_multiply;
    binaryfunc nb_divide;
    binaryfunc nb_remainder;
    binaryfunc nb_divmod;
    ternaryfunc nb_power;
    unaryfunc nb_negative;
    unaryfunc nb_positive;
    unaryfunc nb_absolute;
    inquiry nb_nonzero;          /* Used by PyObject_IsTrue */
    unaryfunc nb_invert;
    binaryfunc nb_lshift;
    binaryfunc nb_rshift;
    binaryfunc nb_and;
    binaryfunc nb_xor;
    binaryfunc nb_or;
    coercion nb_coerce;         /* Used by the coerce() function */
    unaryfunc nb_int;
    unaryfunc nb_long;
    unaryfunc nb_float;
    unaryfunc nb_oct;
    unaryfunc nb_hex;

    /* Added in release 2.0 */
    binaryfunc nb_inplace_add;
    binaryfunc nb_inplace_subtract;
    binaryfunc nb_inplace_multiply;
    binaryfunc nb_inplace_divide;
    binaryfunc nb_inplace_remainder;
    ternaryfunc nb_inplace_power;
    binaryfunc nb_inplace_lshift;
    binaryfunc nb_inplace_rshift;
    binaryfunc nb_inplace_and;
    binaryfunc nb_inplace_xor;
    binaryfunc nb_inplace_or;

    /* Added in release 2.2 */
    binaryfunc nb_floor_divide;
    binaryfunc nb_true_divide;
    binaryfunc nb_inplace_floor_divide;
    binaryfunc nb_inplace_true_divide;

    /* Added in release 2.5 */
    unaryfunc nb_index;
} PyNumberMethods;
```

Binary and ternary functions may receive different kinds of arguments, depending on the flag bit Py\_TPFLAGS\_CHECKTYPES:

<!-- page: 154 -->

• If Py\_TPFLAGS\_CHECKTYPES is not set, the function arguments are guaranteed to be of the object’s type; the caller is responsible for calling the coercion method specified by the nb\_coerce member to convert the arguments:

## coercion PyNumberMethods.nb\_coerce

This function is used by PyNumber\_CoerceEx() and has the same signature. The first argument is always a pointer to an object of the defined type. If the conversion to a common “larger” type is possible, the function replaces the pointers with new references to the converted objects and returns 0. If the conversion is not possible, the function returns 1. If an error condition is set, it will return -1.

• If the Py\_TPFLAGS\_CHECKTYPES flag is set, binary and ternary functions must check the type of all their operands, and implement the necessary conversions (at least one of the operands is an instance of the defined type). This is the recommended way; with Python 3 coercion will disappear completely.

If the operation is not defined for the given operands, binary and ternary functions must return Py\_NotImplemented, if another error occurred they must return NULL and set an exception.

## 10.5 Mapping Object Structures

## PyMappingMethods

This structure holds pointers to the functions which an object uses to implement the mapping protocol. It has three members:

## lenfunc PyMappingMethods.mp\_length

This function is used by PyMapping\_Length() and PyObject\_Size(), and has the same signature. This slot may be set to NULL if the object has no defined length.

## binaryfunc PyMappingMethods.mp\_subscript

This function is used by PyObject\_GetItem() and has the same signature. This slot must be filled for the PyMapping\_Check() function to return 1, it can be NULL otherwise.

## objobjargproc PyMappingMethods.mp\_ass\_subscript

This function is used by PyObject\_SetItem() and PyObject\_DelItem(). It has the same signature as PyObject\_SetItem(), but v can also be set to NULL to delete an item. If this slot is NULL, the object does not support item assignment and deletion.

## 10.6 Sequence Object Structures

## PySequenceMethods

This structure holds pointers to the functions which an object uses to implement the sequence protocol.

## lenfunc PySequenceMethods.sq\_length

This function is used by PySequence\_Size() and PyObject\_Size(), and has the same signature.

## binaryfunc PySequenceMethods.sq\_concat

This function is used by PySequence\_Concat() and has the same signature. It is also used by the + operator, after trying the numeric addition via the nb\_add slot.

## ssizeargfunc PySequenceMethods.sq\_repeat

This function is used by PySequence\_Repeat() and has the same signature. It is also used by the \* operator, after trying numeric multiplication via the nb\_multiply slot.

## ssizeargfunc PySequenceMethods.sq\_item

This function is used by PySequence\_GetItem() and has the same signature. This slot must be filled for the PySequence\_Check() function to return 1, it can be NULL otherwise.

<!-- page: 155 -->

Negative indexes are handled as follows: if the sq\_length slot is filled, it is called and the sequence length is used to compute a positive index which is passed to sq\_item. If sq\_length is NULL, the index is passed as is to the function.

## ssizeobjargproc PySequenceMethods.sq\_ass\_item

This function is used by PySequence\_SetItem() and has the same signature. This slot may be left to NULL if the object does not support item assignment and deletion.

## objobjproc PySequenceMethods.sq\_contains

This function may be used by PySequence\_Contains() and has the same signature. This slot may be left to NULL, in this case PySequence\_Contains() simply traverses the sequence until it finds a match.

## binaryfunc PySequenceMethods.sq\_inplace\_concat

This function is used by PySequence\_InPlaceConcat() and has the same signature. It should modify its first operand, and return it.

## ssizeargfunc PySequenceMethods.sq\_inplace\_repeat

This function is used by PySequence\_InPlaceRepeat() and has the same signature. It should modify its first operand, and return it.

## 10.7 Buffer Object Structures

The buffer interface exports a model where an object can expose its internal data as a set of chunks of data, where each chunk is specified as a pointer/length pair. These chunks are called segments and are presumed to be non-contiguous in memory.

If an object does not export the buffer interface, then its tp\_as\_buffer member in the PyTypeObject structure should be NULL. Otherwise, the tp\_as\_buffer will point to a PyBufferProcs structure.

**Note:** It is very important that your PyTypeObject structure uses Py\_TPFLAGS\_DEFAULT for the value of the tp\_flags member rather than 0. This tells the Python runtime that your PyBufferProcs structure contains the bf\_getcharbuffer slot. Older versions of Python did not have this member, so a new Python interpreter using an old extension needs to be able to test for its presence before using it.

## PyBufferProcs

Structure used to hold the function pointers which define an implementation of the buffer protocol.

The first slot is bf\_getreadbuffer, of type readbufferproc. If this slot is NULL, then the object does not support reading from the internal data. This is non-sensical, so implementors should fill this in, but callers should test that the slot contains a non-NULL value.

The next slot is bf\_getwritebuffer having type writebufferproc. This slot may be NULL if the object does not allow writing into its returned buffers.

The third slot is bf\_getsegcount, with type segcountproc. This slot must not be NULL and is used to inform the caller how many segments the object contains. Simple objects such as PyString\_Type and PyBuffer\_Type objects contain a single segment.

The last slot is bf\_getcharbuffer, of type charbufferproc. This slot will only be present if the Py\_TPFLAGS\_HAVE\_GETCHARBUFFER flag is present in the tp\_flags field of the object’s PyTypeObject. Before using this slot, the caller should test whether it is present by using the PyType\_HasFeature() function. If the flag is present, bf\_getcharbuffer may be NULL, indicating that the object’s contents cannot be used as 8-bit characters. The slot function may also raise an error if the object’s contents cannot be interpreted as 8-bit characters. For example, if the object is an array which is configured to hold floating point values, an exception may be raised if a caller attempts to use bf\_getcharbuffer to fetch a

<!-- page: 156 -->

sequence of 8-bit characters. This notion of exporting the internal buffers as “text” is used to distinguish between objects that are binary in nature, and those which have character-based content.

**Note:** The current policy seems to state that these characters may be multi-byte characters. This implies that a buffer size of N does not mean there are N characters present.

## Py\_TPFLAGS\_HAVE\_GETCHARBUFFER

Flag bit set in the type structure to indicate that the bf\_getcharbuffer slot is known. This being set does not indicate that the object supports the buffer interface or that the bf\_getcharbuffer slot is non-NULL.

Py\_ssize\_t **(\*readbufferproc)**(PyObject \*self, Py\_ssize\_t segment, void \*\*ptrptr)

Return a pointer to a readable segment of the buffer in \*ptrptr. This function is allowed to raise an exception, in which case it must return -1. The segment which is specified must be zero or positive, and strictly less than the number of segments returned by the bf\_getsegcount slot function. On success, it returns the length of the segment, and sets \*ptrptr to a pointer to that memory.

Py\_ssize\_t **(\*writebufferproc)**(PyObject \*self, Py\_ssize\_t segment, void \*\*ptrptr)

Return a pointer to a writable memory buffer in \*ptrptr, and the length of that segment as the function return value. The memory buffer must correspond to buffer segment segment. Must return -1 and set an exception on error. TypeError should be raised if the object only supports read-only buffers, and SystemError should be raised when segment specifies a segment that doesn’t exist.

Py\_ssize\_t **(\*segcountproc)**(PyObject \*self, Py\_ssize\_t \*lenp)

Return the number of memory segments which comprise the buffer. If lenp is not NULL, the implementation must report the sum of the sizes (in bytes) of all segments in \*lenp. The function cannot fail.

Py\_ssize\_t **(\*charbufferproc)**(PyObject \*self, Py\_ssize\_t segment, char \*\*ptrptr)

Return the size of the segment segment that ptrptr is set to. \*ptrptr is set to the memory buffer. Returns -1 on error.

## 10.8 Supporting Cyclic Garbage Collection

Python’s support for detecting and collecting garbage which involves circular references requires support from object types which are “containers” for other objects which may also be containers. Types which do not store references to other objects, or which only store references to atomic types (such as numbers or strings), do not need to provide any explicit support for garbage collection.

To create a container type, the tp\_flags field of the type object must include the Py\_TPFLAGS\_HAVE\_GC and provide an implementation of the tp\_traverse handler. If instances of the type are mutable, a tp\_clear implementation must also be provided.

## Py\_TPFLAGS\_HAVE\_GC

Objects with a type with this flag set must conform with the rules documented here. For convenience these objects will be referred to as container objects.

Constructors for container types must conform to two rules:

1. The memory for the object must be allocated using PyObject\_GC\_New() or PyObject\_GC\_NewVar().

2. Once all the fields which may contain references to other containers are initialized, it must call PyObject\_GC\_Track().

TYPE\* **PyObject\_GC\_New**(TYPE, PyTypeObject \*type)

Analogous to PyObject\_New() but for container objects with the Py\_TPFLAGS\_HAVE\_GC flag set.

## TYPE\* PyObject\_GC\_NewVar(TYPE, PyTypeObject \*type, Py\_ssize\_t size)

Analogous to PyObject\_NewVar() but for container objects with the Py\_TPFLAGS\_HAVE\_GC flag set.

<!-- page: 157 -->

void **\_PyObject\_GC\_TRACK**(PyObject \*op)

```txt
void PyObject_GC_Del (void *op)
    Releases memory allocated to an object using PyObject_GC_New() or PyObject_GC_NewVar().
```

Changed in version 2.5: This function used an int type for size. This might require changes in your code for properly supporting 64-bit systems.

TYPE\* **PyObject\_GC\_Resize**(TYPE, PyVarObject \*op, Py\_ssize\_t newsize) Resize an object allocated by PyObject\_NewVar(). Returns the resized object or NULL on failure. op must not be tracked by the collector yet.

Changed in version 2.5: This function used an int type for newsize. This might require changes in your code for properly supporting 64-bit systems.

## void PyObject\_GC\_Track(PyObject \*op)

Adds the object op to the set of container objects tracked by the collector. The collector can run at unexpected times so objects must be valid while being tracked. This should be called once all the fields followed by the tp\_traverse handler become valid, usually near the end of the constructor.

A macro version of PyObject\_GC\_Track(). It should not be used for extension modules.

Similarly, the deallocator for the object must conform to a similar pair of rules:

1. Before fields which refer to other containers are invalidated, PyObject\_GC\_UnTrack() must be called.

2. The object’s memory must be deallocated using PyObject\_GC\_Del().

## void PyObject\_GC\_UnTrack(void \*op)

Remove the object op from the set of container objects tracked by the collector. Note that PyObject\_GC\_Track() can be called again on this object to add it back to the set of tracked objects. The deallocator (tp\_dealloc handler) should call this for the object before any of the fields used by the tp\_traverse handler become invalid.

```txt
void _PyObject_GC_UNTRACK(PyObject *op)
    A macro version of PyObject_GC_UnTrack(). It should not be used for extension modules.
```

The tp\_traverse handler accepts a function parameter of this type:

## int (\*visitproc)(PyObject \*object, void \*arg)

Type of the visitor function passed to the tp\_traverse handler. The function should be called with an object to traverse as object and the third parameter to the tp\_traverse handler as arg. The Python core uses several visitor functions to implement cyclic garbage detection; it’s not expected that users will need to write their own visitor functions.

The tp\_traverse handler must have the following type:

int **(\*traverseproc)**(PyObject \*self, visitproc visit, void \*arg) Traversal function for a container object. Implementations must call the visit function for each object directly contained by self, with the parameters to visit being the contained object and the arg value passed to the handler. The visit function must not be called with a NULL object argument. If visit returns a non-zero value that value should be returned immediately.

To simplify writing tp\_traverse handlers, a Py\_VISIT() macro is provided. In order to use this macro, the tp\_traverse implementation must name its arguments exactly visit and arg:

If o is not NULL, call the visit callback, with arguments o and arg. If visit returns a non-zero value, then return it. Using this macro, tp\_traverse handlers look like:

```c
static int
my_traverse(Noddy *self, visitproc visit, void *arg)
```

(continues on next page)

<!-- page: 158 -->

```c
{
    Py_VISIT(self->foo);
    Py_VISIT(self->bar);
    return 0;
}
```

(continued from previous page)

## New in version 2.4.

The tp\_cl ear handler must be of the inquiry type, or NULL if the object is immutable.

## int (\*inquiry)(PyObject \*self)

Drop references that may have created reference cycles. Immutable objects do not have to define this method since they can never directly create reference cycles. Note that the object must still be valid after calling this method (don’t just call Py\_DECREF() on a reference). The collector will call this method if it detects that this object is involved in a reference cycle.

<!-- page: 159 -->

# GLOSSARY

**>>>** The default Python prompt of the interactive shell. Often seen for code examples which can be executed interactively in the interpreter.

The default Python prompt of the interactive shell when entering code for an indented code block, when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator.

**2to3** A tool that tries to convert Python 2.x code to Python 3.x code by handling most of the incompatibilities which can be detected by parsing the source and traversing the parse tree.

2to3 is available in the standard library as lib2to3; a standalone entry point is provided as Tools/scripts/ 2to3. See 2to3-reference.

**abstract base class** Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like hasattr() would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and issubclass(); see the abc module documentation. Python comes with many built-in ABCs for data structures (in the collections module), numbers (in the numbers module), and streams (in the io module). You can create your own ABCs with the abc module.

**argument** A value passed to a function (or method) when calling the function. There are two types of arguments:

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

See also the parameter glossary entry and the FAQ question on the difference between arguments and parameters.

**attribute** A value associated with an object which is referenced by name using dotted expressions. For example, if an object o has an attribute a it would be referenced as o.a.

**BDFL** Benevolent Dictator For Life, a.k.a. [Guido van Rossum](https://www.python.org/~guido/), Python’s creator.

<!-- page: 160 -->

**bytes-like object** An object that supports the buffer protocol, like str, bytearray or memoryview. Bytes-like objects can be used for various operations that expect binary data, such as compression, saving to a binary file or sending over a socket. Some operations need the binary data to be mutable, in which case not all bytes-like objects can apply.

**bytecode** Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter. The bytecode is also cached in .pyc and .pyo files so that executing the same file is faster the second time (recompilation from source to bytecode can be avoided). This “intermediate language” is said to run on a virtual machine that executes the machine code corresponding to each bytecode. Do note that bytecodes are not expected to work between different Python virtual machines, nor to be stable between Python releases.

A list of bytecode instructions can be found in the documentation for the dis module.

**class** A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

**classic class** Any class which does not inherit from object. See new-style class. Classic classes have been removed in Python 3.

**coercion** The implicit conversion of an instance of one type to another during an operation which involves two arguments of the same type. For example, int(3.15) converts the floating point number to the integer 3, but in 3+4.5, each argument is of a different type (one int, one float), and both must be converted to the same type before they can be added or it will raise a TypeError. Coercion between two operands can be performed with the coerce built-in function; thus, 3+4.5 is equivalent to calling operator.add(\*coerce(3, 4.5)) and results in operator.add(3.0, 4.5). Without coercion, all arguments of even compatible types would have to be normalized to the same value by the programmer, e.g., float(3)+4.5 rather than just 3+4.5.

**complex number** An extension of the familiar real number system in which all numbers are expressed as a sum of a real part and an imaginary part. Imaginary numbers are real multiples of the imaginary unit (the square root of -1), often written i in mathematics or j in engineering. Python has built-in support for complex numbers, which are written with this latter notation; the imaginary part is written with a j suffix, e.g., 3+1j. To get access to complex equivalents of the math module, use cmath. Use of complex numbers is a fairly advanced mathematical feature. If you’re not aware of a need for them, it’s almost certain you can safely ignore them.

**context manager** An object which controls the environment seen in a with statement by defining \_\_enter\_\_() and exit\_\_() methods. See [**PEP 343**](https://www.python.org/dev/peps/pep-0343).

**CPython** The canonical implementation of the Python programming language, as distributed on [python.org](https://www.python.org). The term “CPython” is used when necessary to distinguish this implementation from others such as Jython or IronPython.

**decorator** A function returning another function, usually applied as a function transformation using the @wrapper syntax. Common examples for decorators are classmethod() and staticmethod().

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:

```python
def f(...):
    ...
f = staticmethod(f)

@staticmethod
def f(...):
    ...
```

The same concept exists for classes, but is less commonly used there. See the documentation for function definitions and class definitions for more about decorators.

**descriptor** Any new-style object which defines the methods \_\_get\_\_(), \_\_set\_\_(), or \_\_delete\_\_(). When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using a.b to get, set or delete an attribute looks up the object named b in the class dictionary for a, but if b is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python

<!-- page: 161 -->

because they are the basis for many features including functions, methods, properties, class methods, static methods, and reference to super classes.

For more information about descriptors’ methods, see descriptors.

**dictionary** An associative array, where arbitrary keys are mapped to values. The keys can be any object with \_\_hash\_\_() and \_\_eq\_\_() methods. Called a hash in Perl.

**dictionary view** The objects returned from dict.viewkeys(), dict.viewvalues(), and dict. viewitems() are called dictionary views. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes. To force the dictionary view to become a full list use list(dictview). See dict-views.

**docstring** A string literal which appears as the first expression in a class, function or module. While ignored when the suite is executed, it is recognized by the compiler and put into the \_\_doc\_\_ attribute of the enclosing class, function or module. Since it is available via introspection, it is the canonical place for documentation of the object.

**duck-typing** A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitution. Duck-typing avoids tests using type() or isinstance(). (Note, however, that duck-typing can be complemented with abstract base classes.) Instead, it typically employs hasattr() tests or EAFP programming.

**EAFP** Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.

**expression** A piece of syntax which can be evaluated to some value. In other words, an expression is an accumulation of expression elements like literals, names, attribute access, operators or function calls which all return a value. In contrast to many other languages, not all language constructs are expressions. There are also statements which cannot be used as expressions, such as print or if. Assignments are also statements, not expressions.

**extension module** A module written in C or C++, using Python’s C API to interact with the core and with user code.

**file object** An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource. Depending on the way it was created, a file object can mediate access to a real on-disk file or to another type of storage or communication device (for example standard input/output, in-memory buffers, sockets, pipes, etc.). File objects are also called file-like objects or streams.

There are actually three categories of file objects: raw binary files, buffered binary files and text files. Their interfaces are defined in the io module. The canonical way to create a file object is by using the open() function.

**file-like object** A synonym for file object.

**finder** An object that tries to find the loader for a module. It must implement a method named find\_module(). See [**PEP 302**](https://www.python.org/dev/peps/pep-0302) for details.

**floor division** Mathematical division that rounds down to nearest integer. The floor division operator is //. For example, the expression 11 // 4 evaluates to 2 in contrast to the 2.75 returned by float true division. Note that (-11) // 4 is -3 because that is -2.75 rounded downward. See [**PEP 238**](https://www.python.org/dev/peps/pep-0238).

**function** A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body. See also parameter, method, and the function section.

future\_\_ A pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter. For example, the expression 11/4 currently evaluates to 2. If the module in which it is executed had enabled true division by executing:

<!-- page: 162 -->

```python
from __future__ import division
```

the expression 11/4 would evaluate to 2.75. By importing the \_\_future\_\_ module and evaluating its variables, you can see when a new feature was first added to the language and when it will become the default:

```python
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
```

**garbage collection** The process of freeing memory when it is not used anymore. Python performs garbage collection via reference counting and a cyclic garbage collector that is able to detect and break reference cycles.

**generator** A function which returns an iterator. It looks like a normal function except that it contains yield statements for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function. Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the generator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

**generator expression** An expression that returns an iterator. It looks like a normal expression followed by a for expression defining a loop variable, range, and an optional if expression. The combined expression generates values for an enclosing function:

```txt
>>> sum(i*i for i in range(10))
285
```

```txt
# sum of squares 0, 1, 4, ... 81
```

**GIL** See global interpreter lock.

**global interpreter lock** The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This simplifies the CPython implementation by making the object model (including critical built-in types such as dict) implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

However, some extension modules, either standard or third-party, are designed so as to release the GIL when doing computationally-intensive tasks such as compression or hashing. Also, the GIL is always released when doing I/O.

Past efforts to create a “free-threaded” interpreter (one which locks shared data at a much finer granularity) have not been successful because performance suffered in the common single-processor case. It is believed that overcoming this performance issue would make the implementation much more complicated and therefore costlier to maintain.

**hashable** An object is hashable if it has a hash value which never changes during its lifetime (it needs a \_\_hash\_\_() method), and can be compared to other objects (it needs an \_\_eq\_\_() or \_\_cmp\_\_() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal (except with themselves), and their hash value is derived from their id().

**IDLE** An Integrated Development Environment for Python. IDLE is a basic editor and interpreter environment which ships with the standard distribution of Python.

**immutable** An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.

**integer division** Mathematical division discarding any remainder. For example, the expression 11/4 currently evaluates to 2 in contrast to the 2.75 returned by float division. Also called floor division. When dividing two integers the

<!-- page: 163 -->

outcome will always be another integer (having the floor function applied to it). However, if one of the operands is another numeric type (such as a float), the result will be coerced (see coercion) to a common type. For example, an integer divided by a float will result in a float value, possibly with a decimal fraction. Integer division can be forced by using the // operator instead of the / operator. See also \_\_future\_\_.

**importing** The process by which Python code in one module is made available to Python code in another module.

**importer** An object that both finds and loads a module; both a finder and loader object.

**interactive** Python has an interactive interpreter which means you can enter statements and expressions at the interpreter prompt, immediately execute them and see their results. Just launch python with no arguments (possibly by selecting it from your computer’s main menu). It is a very powerful way to test out new ideas or inspect modules and packages (remember help(x)).

**interpreted** Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. This means that source files can be run directly without explicitly creating an executable which is then run. Interpreted languages typically have a shorter development/debug cycle than compiled ones, though their programs generally also run more slowly. See also interactive.

**iterable** An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict and file and objects of any classes you define with an \_\_iter\_\_() or \_\_getitem\_\_() method. Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.

**iterator** An object representing a stream of data. Repeated calls to the iterator’s next() method return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its next() method just raise StopIteration again. Iterators are required to have an \_\_iter\_\_() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

More information can be found in typeiter.

**key function** A key function or collation function is a callable that returns a value used for sorting or ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale specific sort conventions.

A number of tools in Python accept key functions to control how elements are ordered or grouped. They include min(), max(), sorted(), list.sort(), heapq.nsmallest(), heapq.nlargest(), and itertools.groupby().

There are several ways to create a key function. For example. the str.lower() method can serve as a key function for case insensitive sorts. Alternatively, an ad-hoc key function can be built from a lambda expression such as lambda r: (r[0], r[2]). Also, the operator module provides three key function constructors: attrgetter(), itemgetter(), and methodcaller(). See the Sorting HOW TO for examples of how to create and use key functions.

## keyword argument See argument.

**lambda** An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [parameters]: expression

**LBYL** Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the EAFP approach and is characterized by the presence of many if statements.

<!-- page: 164 -->

In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the looking” and “the leaping”. For example, the code, if key in mapping: return mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. This issue can be solved with locks or by using the EAFP approach.

**list** A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).

**list comprehension** A compact way to process all or part of the elements in a sequence and return a list with the results. result = ["0x%02x" % x for x in range(256) if x % 2 == 0] generates a list of strings containing even hex numbers (0x..) in the range from 0 to 255. The if clause is optional. If omitted, all elements in range(256) are processed.

**loader** An object that loads a module. It must define a method named load\_module(). A loader is typically returned by a finder. See [**PEP 302**](https://www.python.org/dev/peps/pep-0302) for details.

**magic method** An informal synonym for special method.

**mapping** A container object that supports arbitrary key lookups and implements the methods specified in the Mapping or MutableMapping abstract base classes. Examples include dict, collections.defaultdict, collections.OrderedDict and collections.Counter.

**metaclass** The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses. Most users never need this tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have been used for logging attribute access, adding thread-safety, tracking object creation, implementing singletons, and many other tasks.

More information can be found in metaclasses.

**method** A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self). See function and nested scope.

**method resolution order** Method Resolution Order is the order in which base classes are searched for a member during lookup. See [The Python 2.3 Method Resolution Order](https://www.python.org/download/releases/2.3/mro/) for details of the algorithm used by the Python interpreter since the 2.3 release.

**module** An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

See also package.

**MRO** See method resolution order.

**mutable** Mutable objects can change their value but keep their id(). See also immutable.

**named tuple** Any tuple-like class whose indexable elements are also accessible using named attributes (for example, time.localtime() returns a tuple-like object where the year is accessible either with an index such as t[0] or with a named attribute like t.tm\_year).

A named tuple can be a built-in type such as time.struct\_time, or it can be created with a regular class definition. A full featured named tuple can also be created with the factory function collections. namedtuple(). The latter approach automatically provides extra features such as a self-documenting representation like Employee(name='jones', title='programmer').

**namespace** The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions \_\_builtin\_\_.open() and os.open() are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.izip() makes it clear that those functions are implemented by the random and itertools modules, respectively.

<!-- page: 165 -->

**nested scope** The ability to refer to a variable in an enclosing definition. For instance, a function defined inside another function can refer to variables in the outer function. Note that nested scopes work only for reference and not for assignment which will always write to the innermost scope. In contrast, local variables both read and write in the innermost scope. Likewise, global variables read and write to the global namespace.

**new-style class** Any class which inherits from object. This includes all built-in types like list and dict. Only new-style classes can use Python’s newer, versatile features like \_\_slots\_\_, descriptors, properties, and \_getattribute\_\_().

More information can be found in newstyle.

**object** Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.

**package** A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an \_\_path\_\_ attribute.

**parameter** A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept. There are four types of parameters:

• positional-or-keyword: specifies an argument that can be passed either positionally or as a keyword argument. This is the default kind of parameter, for example foo and bar in the following:

```txt
def func(foo, bar=None): ...
```

• positional-only: specifies an argument that can be supplied only by position. Python has no syntax for defining positional-only parameters. However, some built-in functions have positional-only parameters (e.g. abs()).

• var-positional: specifies that an arbitrary sequence of positional arguments can be provided (in addition to any positional arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with \*, for example args in the following:

```txt
def func(*args, **kwargs): ...
```

• var-keyword: specifies that arbitrarily many keyword arguments can be provided (in addition to any keyword arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with \*\*, for example kwargs in the example above.

Parameters can specify both optional and required arguments, as well as default values for some optional arguments.

See also the argument glossary entry, the FAQ question on the difference between arguments and parameters, and the function section.

**PEP** Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. PEPs should provide a concise technical specification and a rationale for proposed features.

PEPs are intended to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.

See [**PEP 1**](https://www.python.org/dev/peps/pep-0001).

**positional argument** See argument.

**Python 3000** Nickname for the Python 3.x release line (coined long ago when the release of version 3 was something in the distant future.) This is also abbreviated “Py3k”.

**Pythonic** An idea or piece of code which closely follows the most common idioms of the Python language, rather than implementing code using concepts common to other languages. For example, a common idiom in Python is to loop over all elements of an iterable using a for statement. Many other languages don’t have this type of construct, so people unfamiliar with Python sometimes use a numerical counter instead:

<!-- page: 166 -->

```python
for i in range(len(food)):
    print food[i]
```

As opposed to the cleaner, Pythonic method:

```python
for piece in food:
    print piece
```

**reference count** The number of references to an object. When the reference count of an object drops to zero, it is deallocated. Reference counting is generally not visible to Python code, but it is a key element of the CPython implementation. The sys module defines a getrefcount() function that programmers can call to return the reference count for a particular object.

\_slots\_\_ A declaration inside a new-style class that saves memory by pre-declaring space for instance attributes and eliminating instance dictionaries. Though popular, the technique is somewhat tricky to get right and is best reserved for rare cases where there are large numbers of instances in a memory-critical application.

**sequence** An iterable which supports efficient element access using integer indices via the \_\_getitem\_\_() special method and defines a len() method that returns the length of the sequence. Some built-in sequence types are list, str, tuple, and unicode. Note that dict also supports \_\_getitem\_\_() and \_\_len\_\_(), but is considered a mapping rather than a sequence because the lookups use arbitrary immutable keys rather than integers.

**slice** An object usually containing a portion of a sequence. A slice is created using the subscript notation, [] with colons between numbers when several are given, such as in variable\_name[1:3:5]. The bracket (subscript) notation uses slice objects internally (or in older versions, \_\_getslice\_\_() and \_\_setslice\_\_()).

**special method** A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. Special methods are documented in specialnames.

**statement** A statement is part of a suite (a “block” of code). A statement is either an expression or one of several constructs with a keyword, such as if, while or for.

**struct sequence** A tuple with named elements. Struct sequences expose an interface similiar to named tuple in that elements can be accessed either by index or as an attribute. However, they do not have any of the named tuple methods like \_make() or \_asdict(). Examples of struct sequences include sys.float\_info and the return value of os.stat().

**triple-quoted string** A string which is bound by three instances of either a quotation mark (“) or an apostrophe (‘). While they don’t provide any functionality not available with single-quoted strings, they are useful for a number of reasons. They allow you to include unescaped single and double quotes within a string and they can span multiple lines without the use of the continuation character, making them especially useful when writing docstrings.

**type** The type of a Python object determines what kind of object it is; every object has a type. An object’s type is accessible as its \_\_class\_\_ attribute or can be retrieved with type(obj).

**universal newlines** A manner of interpreting text streams in which all of the following are recognized as ending a line: the Unix end-of-line convention '\n', the Windows convention '\r\n', and the old Macintosh convention '\ r'. See [**PEP 278**](https://www.python.org/dev/peps/pep-0278) and [**PEP 3116**](https://www.python.org/dev/peps/pep-3116), as well as str.splitlines() for an additional use.

**virtual environment** A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.

**virtual machine** A computer defined entirely in software. Python’s virtual machine executes the bytecode emitted by the bytecode compiler.

**Zen of Python** Listing of Python design principles and philosophies that are helpful in understanding and using the language. The listing can be found by typing “import this” at the interactive prompt.

<!-- page: 167 -->

## ABOUT THESE DOCUMENTS

These documents are generated from [reStructuredText](http://docutils.sourceforge.net/rst.html) sources by [Sphinx](http://sphinx-doc.org/), a document processor specifically written for the Python documentation.

Development of the documentation and its toolchain is an entirely volunteer effort, just like Python itself. If you want to contribute, please take a look at the reporting-bugs page for information on how to do so. New volunteers are always welcome!

Many thanks go to:

• Fred L. Drake, Jr., the creator of the original Python documentation toolset and writer of much of the content;

• the [Docutils](http://docutils.sourceforge.net/) project for creating reStructuredText and the Docutils suite;

• Fredrik Lundh for his [Alternative Python Reference](http://effbot.org/zone/pyref.htm) project from which Sphinx got many good ideas.

## B.1 Contributors to the Python Documentation

Many people have contributed to the Python language, the Python standard library, and the Python documentation. See [Misc/ACKS](https://github.com/python/cpython/tree/2.7/Misc/ACKS) in the Python source distribution for a partial list of contributors.

It is only with the input and contributions of the Python community that Python has such wonderful documentation – Thank You!

<!-- page: 168 -->

<!-- page: 169 -->

# HISTORY AND LICENSE

## C.1 History of the software

Python was created in the early 1990s by Guido van Rossum at Stichting Mathematisch Centrum (CWI, see [https://www.cwi.nl/](https://www.cwi.nl/)) in the Netherlands as a successor of a language called ABC. Guido remains Python’s principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for National Research Initiatives (CNRI, see [https://www.cnri.reston.va.us/](https://www.cnri.reston.va.us/)) in Reston, Virginia where he released several versions of the software.

In May 2000, Guido and the Python core development team moved to BeOpen.com to form the BeOpen PythonLabs team. In October of the same year, the PythonLabs team moved to Digital Creations (now Zope Corporation; see [https://www.zope.org/](https://www.zope.org/)). In 2001, the Python Software Foundation (PSF, see [https://www.python.org/psf/](https://www.python.org/psf/)) was formed, a non-profit organization created specifically to own Python-related Intellectual Property. Zope Corporation is a sponsoring member of the PSF.

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

<!-- page: 170 -->

# C.2 Terms and conditions for accessing or otherwise using Python

## C.2.1 PSF LICENSE AGREEMENT FOR PYTHON 2.7.18

1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"),␣,→and the Individual or Organization ("Licensee") accessing and otherwise using␣,→Python 2.7.18 software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, PSF hereby grants Licensee a nonexclusive, royalty-free, world-wide license to␣,→reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use Python 2.7.18 alone or in any derivative version, provided, however, that PSF's License Agreement and PSF's notice␣,→of copyright, i.e., "Copyright © 2001-2020 Python Software Foundation; All␣,→Rights Reserved" are retained in Python 2.7.18 alone or in any derivative version prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on or incorporates Python 2.7.18 or any part thereof, and wants to make the derivative work available to others as provided herein, then Licensee␣,→hereby agrees to include in any such work a brief summary of the changes made to␣,→Python 2.7.18.

4. PSF is making Python 2.7.18 available to Licensee on an "AS IS" basis. PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION␣,→OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT␣,→THE USE OF PYTHON 2.7.18 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 2.7.18 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT␣,→OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 2.7.18, OR ANY␣,→DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach␣,→of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any␣,→relationship of agency, partnership, or joint venture between PSF and Licensee. This␣,→License

<!-- page: 171 -->

```txt
Agreement does not grant permission to use PSF trademarks or trade name in a trademark sense to endorse or promote products or services of Licensee, or any third party.
```

8. By copying, installing or otherwise using Python 2.7.18, Licensee agrees to be bound by the terms and conditions of this License Agreement.

## C.2.2 BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0

## BEOPEN PYTHON OPEN SOURCE LICENSE AGREEMENT VERSION 1

```txt
This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an office at 160 Saratoga Avenue, Santa Clara, CA 95051, and the Individual or Organization ("Licensee") accessing and otherwise using this software in source or binary form and its associated documentation ("the Software").
Subject to the terms and conditions of this BeOpen Python License Agreement, BeOpen hereby grants Licensee a non-exclusive, royalty-free, world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use the Software alone or in any derivative version, provided, however, that the BeOpen Python License is retained in the Software, alone or in any derivative version prepared by Licensee.
BeOpen is making the Software available to Licensee on an "AS IS" basis. BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE SOFTWARE WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE SOFTWARE FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THE SOFTWARE, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.
This License Agreement will automatically terminate upon a material breach of its terms and conditions.
This License Agreement shall be governed by and interpreted in all respects by the law of the State of California, excluding conflict of law provisions. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between BeOpen and Licensee. This License Agreement does not grant permission to use BeOpen trademarks or trade names in a trademark sense to endorse or promote products or services of Licensee, or any third party. As an exception, the "BeOpen Python" logos available at http://www.pythonlabs.com/logos.html may be used according to the permissions granted on that web page.
By copying, installing or otherwise using the software, Licensee agrees to be bound by the terms and conditions of this License Agreement.
```

<!-- page: 172 -->

## C.2.3 CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1

1. This LICENSE AGREEMENT is between the Corporation for National Research Initiatives, having an office at 1895 Preston White Drive, Reston, VA 20191 ("CNRI"), and the Individual or Organization ("Licensee") accessing and otherwise using Python 1.6.1 software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, CNRI hereby grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use Python 1.6.1 alone or in any derivative version, provided, however, that CNRI's License Agreement and CNRI's notice of copyright, i.e., "Copyright © 1995-2001 Corporation for National Research Initiatives; All Rights Reserved" are retained in Python 1.6.1 alone or in any derivative version prepared by Licensee. Alternately, in lieu of CNRI's License Agreement, Licensee may substitute the following text (omitting the quotes): "Python 1.6.1 is made available subject to the terms and conditions in CNRI's License Agreement. This Agreement together with Python 1.6.1 may be located on the Internet using the following unique, persistent identifier (known as a handle): 1895.22/1013. This Agreement may also be obtained from a proxy server on the Internet using the following URL: http://hdl.handle.net/1895.22/1013."

3. In the event Licensee prepares a derivative work that is based on or incorporates Python 1.6.1 or any part thereof, and wants to make the derivative work available to others as provided herein, then Licensee hereby agrees to include in any such work a brief summary of the changes made to Python 1.6.1.

4. CNRI is making Python 1.6.1 available to Licensee on an "AS IS" basis. CNRI MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, CNRI MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON 1.6.1 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. CNRI SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 1.6.1 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 1.6.1, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of its terms and conditions.

7. This License Agreement shall be governed by the federal intellectual property law of the United States, including without limitation the federal copyright law, and, to the extent such U.S. federal law does not apply, by the law of the Commonwealth of Virginia, excluding Virginia's conflict of law provisions. Notwithstanding the foregoing, with regard to derivative works based on Python 1.6.1 that incorporate non-separable material that was previously distributed under the GNU General Public License (GPL), the law of the Commonwealth of Virginia shall govern this License Agreement only as to issues arising under or with respect to Paragraphs 4, 5, and 7 of this License Agreement. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between CNRI and Licensee. This License Agreement does not grant permission to use CNRI trademarks or trade name in a trademark sense to endorse or promote products or services of Licensee, or any third party.

(continues on next page)

<!-- page: 173 -->

(continued from previous page)

```txt
8. By clicking on the "ACCEPT" button where indicated, or by copying, installing or otherwise using Python 1.6.1, Licensee agrees to be bound by the terms and conditions of this License Agreement.
```

## C.2.4 CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2

```txt
Copyright © 1991 - 1995, Stichting Mathematisch Centrum Amsterdam, The Netherlands. All rights reserved.

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Stichting Mathematisch Centrum or CWI not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

STICHTING MATHEMATISCH CENTRUM DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL STICHTING MATHEMATISCH CENTRUM BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
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
```

(continues on next page)

<!-- page: 174 -->

(continued from previous page)

```txt
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. The names of its contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Any feedback is very welcome.
http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
email: m-mat @ math.sci.hiroshima-u.ac.jp (remove space)
```

## C.3.2 Sockets

The socket module uses the functions, getaddrinfo(), and getnameinfo(), which are coded in separate source files from the WIDE Project, [http://www.wide.ad.jp/](http://www.wide.ad.jp/).

```txt
Copyright (C) 1995, 1996, 1997, and 1998 WIDE Project.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the project nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
```

(continues on next page)

<!-- page: 175 -->

```txt
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

(continued from previous page)

## C.3.3 Floating point exception control

The source for the fpectl module includes the following notice:

```txt
Copyright (c) 1996.
The Regents of the University of California.
All rights reserved.

Permission to use, copy, modify, and distribute this software for any purpose without fee is hereby granted, provided that this entire notice is included in all copies of any software which is or includes a copy or modification of this software and in all copies of the supporting documentation for such software.

This work was produced at the University of California, Lawrence Livermore National Laboratory under contract no. W-7405-ENG-48 between the U.S. Department of Energy and The Regents of the University of California for the operation of UC LLNL.
```

## DISCLAIMER

```txt
This software was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor the University of California nor any of their employees, makes any warranty, express or implied, or assumes any liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately-owned rights. Reference herein to any specific commercial products, process, or service by trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or the University of California. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or the University of California, and shall not be used for advertising or product endorsement purposes.
```

## C.3.4 MD5 message digest algorithm

The source code for the md5 module contains the following notice:

```txt
Copyright (C) 1999, 2002 Aladdin Enterprises. All rights reserved.
This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.
```

(continues on next page)

<!-- page: 176 -->

(continued from previous page)

```txt
Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.

L. Peter Deutsch
ghost@aladdin.com

Independent implementation of MD5 (RFC 1321).

This code implements the MD5 Algorithm defined in RFC 1321, whose text is available at
    http://www.ietf.org/rfc/rfc1321.txt
The code is derived from the text of the RFC, including the test suite (section A.5) but excluding the rest of Appendix A. It does not include any code or documentation that is identified in the RFC as being copyrighted.

The original and principal author of md5.h is L. Peter Deutsch <ghost@aladdin.com>. Other authors are noted in the change history that follows (in reverse chronological order):

2002-04-13 lpd Removed support for non-ANSI compilers; removed references to Ghostscript; clarified derivation from RFC 1321; now handles byte order either statically or dynamically.
1999-11-04 lpd Edited comments slightly for automatic TOC extraction.
1999-10-18 lpd Fixed typo in header comment (ansi2knr rather than md5); added conditionalization for C++ compilation from Martin Purschke <purschke@bnl.gov>.
1999-05-03 lpd Original version.
```

## C.3.5 Asynchronous socket services

The asynchat and asyncore modules contain the following notice:

```txt
Copyright 1996 by Sam Rushing

All Rights Reserved

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Sam Rushing not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.
```

(continues on next page)

<!-- page: 177 -->

```txt
SAM RUSHING DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL SAM RUSHING BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

(continued from previous page)

## C.3.6 Cookie management

The Cookie module contains the following notice:

```txt
Copyright 2000 by Timothy O'Malley <timo@alum.mit.edu>

All Rights Reserved

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Timothy O'Malley not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

Timothy O'Malley DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL Timothy O'Malley BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.7 Execution tracing

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
```

(continues on next page)

<!-- page: 178 -->

(continued from previous page)

```txt
Copyright 1991-1995, Stichting Mathematisch Centrum, all rights reserved.

Permission to use, copy, modify, and distribute this Python software and its associated documentation for any purpose without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of neither Automatrix, Bioreason or Mojam Media be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.
```

## C.3.8 UUencode and UUdecode functions

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

## C.3.9 XML Remote Procedure Calls

The xmlrpclib module contains the following notice:

```txt
The XML-RPC client interface is

Copyright (c) 1999-2002 by Secret Labs AB
Copyright (c) 1999-2002 by Fredrik Lundh

By obtaining, using, and/or copying this software and/or its associated documentation, you agree that you have read, understood, and will comply with the following terms and conditions:
```

(continues on next page)

<!-- page: 179 -->

(continued from previous page)

```txt
Permission to use, copy, modify, and distribute this software and its associated documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Secret Labs AB or the author not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.10 test\_epoll

The test\_epoll contains the following notice:

```txt
Copyright (c) 2001-2006 Twisted Matrix Laboratories.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## C.3.11 Select kqueue

The select and contains the following notice for the kqueue interface:

```txt
Copyright (c) 2000 Doug White, 2006 James Knight, 2007 Christian Heimes All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
```

(continues on next page)

<!-- page: 180 -->

(continued from previous page)

```txt
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.12 strtod and dtoa

The file Python/dtoa.c, which supplies C functions dtoa and strtod for conversion of C doubles to and from strings, is derived from the file of the same name by David M. Gay, currently available from [http://www.netlib.org/fp/](http://www.netlib.org/fp/). The original file, as retrieved on March 16, 2009, contains the following copyright and licensing notice:

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

## C.3.13 OpenSSL

The modules hashlib, posix, ssl, crypt use the OpenSSL library for added performance if made available by the operating system. Additionally, the Windows and Mac OS X installers for Python may include a copy of the OpenSSL libraries, so we include a copy of the OpenSSL license here:

```txt
LICENSE ISSUES
================

The OpenSSL toolkit stays under a dual license, i.e. both the conditions of
```

(continues on next page)

<!-- page: 181 -->

(continued from previous page)

```txt
the OpenSSL License and the original SSLeay license apply to the toolkit.
See below for the actual license texts. Actually both licenses are BSD-style
Open Source licenses. In case of any license issues related to OpenSSL
please contact openssl-core@openssl.org.

OpenSSL License
-----------------------------------
/* ====================
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
* ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
* OF THE POSSIBILITY OF SUCH DAMAGE.
* ====================
*
* This product includes cryptographic software written by Eric Young
```

(continues on next page)

<!-- page: 182 -->

(continued from previous page)

```txt
*(eay@cryptsoft.com). This product includes software written by Tim
* Hudson (tjh@cryptsoft.com).
*
*/

Original SSLay License
------------------------------------------------------------------

/* Copyright (C) 1995-1998 Eric Young (eay@cryptsoft.com)
* All rights reserved.
*
* This package is an SSL implementation written
* by Eric Young (eay@cryptsoft.com).
* The implementation was written so as to conform with Netscapes SSL.
*
* This library is free for commercial and non-commercial use as long as
* the following conditions are aheaded to. The following conditions
* apply to all code found in this distribution, be it the RC4, RSA,
* lhash, DES, etc., code; not just the SSL code. The SSL documentation
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
* notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
* notice, this list of conditions and the following disclaimer in the
* documentation and/or other materials provided with the distribution.
* 3. All advertising materials mentioning features or use of this software
* must display the following acknowledgement:
* "This product includes cryptographic software written by
* Eric Young (eay@cryptsoft.com)"
* The word 'cryptographic' can be left out if the routines from the library
* being used are not cryptographic related :-).
* 4. If you include any Windows specific code (or a derivative thereof) from
* the apps directory (application code) you must include an acknowledgement:
* "This product includes software written by Tim Hudson (tjh@cryptsoft.com)"
*
* THIS SOFTWARE IS PROVIDED BY ERIC YOUNG ``AS IS'' AND
* ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
* ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
* OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
```

(continues on next page)

<!-- page: 183 -->

(continued from previous page)

```txt
* SUCH DAMAGE.
*
* The licence and distribution terms for any publically available version or
* derivative of this code cannot be changed. i.e. this code cannot simply be
* copied and put under another distribution licence
* [including the GNU Public Licence.]
*/
```

## C.3.14 expat

The pyexpat extension is built using an included copy of the expat sources unless the build is configured --with-system-expat:

```txt
Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd and Clark Cooper

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## C.3.15 libffi

The \_ctypes extension is built using an included copy of the libffi sources unless the build is configured --with-system-libffi:

```txt
Copyright (c) 1996-2008 Red Hat, Inc and others.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ``Software''), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```

(continues on next page)

<!-- page: 184 -->

```txt
THE SOFTWARE IS PROVIDED ``AS IS'', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

(continued from previous page)

## C.3.16 zlib

The zlib extension is built using an included copy of the zlib sources if the zlib version found on the system is too old to be used for the build:

```txt
Copyright (C) 1995-2010 Jean-loup Gailly and Mark Adler

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source distribution.

Jean-loup Gailly          Mark Adler
jloup@gzip.org           madler@alumni.caltech.edu
```

<!-- page: 185 -->

## COPYRIGHT

Python and this documentation is:

Copyright © 2001-2020 Python Software Foundation. All rights reserved.

Copyright © 2000 BeOpen.com. All rights reserved.

Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.

Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.

See History and License for complete license and permissions information.

<!-- page: 186 -->

<!-- page: 187 -->

## Non-alphabetical

..., **155** 2to3, **155** >>>, **155** all\_\_ (package variable), 27 builtin module, 9, 111 dict\_\_ (module attribute), 98 doc\_\_ (module attribute), 98 file\_\_ (module attribute), 98 future\_\_, **157** import built-in function, 27 main module, 9, 111, 119 name\_\_ (module attribute), 98 slots\_\_, **162** frozen (C type), 29 \_inittab (C type), 29 \_Py\_c\_diff (C function), 64 \_Py\_c\_neg (C function), 64 \_Py\_c\_pow (C function), 64 \_Py\_c\_prod (C function), 64 \_Py\_c\_quot (C function), 64 \_Py\_c\_sum (C function), 64 \_Py\_NoneStruct (C variable), 130 \_PyImport\_FindExtension (C function), 29 \_PyImport\_Fini (C function), 28 \_PyImport\_FixupExtension (C function), 29 \_PyImport\_Init (C function), 28 \_PyObject\_Del (C function), 129 \_PyObject\_GC\_TRACK (C function), 153 \_PyObject\_GC\_UNTRACK (C function), 153 \_PyObject\_New (C function), 129 \_PyObject\_NewVar (C function), 129 \_PyString\_Resize (C function), 68 \_PyTuple\_Resize (C function), 89

## A

abort(), 26 abs built-in function, 48 abstract base class, **155** apply built-in function, 45 argument, **155** argv (in module sys), 113 attribute, **155**

## B

BDFL, **155** buffer object, 83 buffer interface, 83 BufferType (in module types), 86 built-in function import\_\_, 27 abs, 48 apply, 45 bytes, 44 classmethod, 132 cmp, 44 coerce, 49 compile, 28 divmod, 48 float, 50 hash, 46, 139 int, 50 len, 46, 50, 53, 90, 92, 109 long, 50 pow, 48, 49 reload, 28 repr, 44, 139 staticmethod, 133 str, 44 tuple, 52, 91 type, 46 unicode, 45 builtins module, 119 bytearray object, 65 bytecode, **156** bytes

<!-- page: 188 -->

built-in function, 44 bytes-like object, **156**

## C

calloc(), 125 Capsule object, 102 charbufferproc (C type), 152 class, **156** object, 94 classic class, **156** classmethod built-in function, 132 ClassType (in module types), 94 cleanup functions, 26 close() (in module os), 120 cmp built-in function, 44 CO\_FUTURE\_DIVISION (C variable), 14 CObject object, 103 code object, 109 coerce built-in function, 49 coercion, **156** compile built-in function, 28 complex number, **156** object, 64 context manager, **156** copyright (in module sys), 113 CPython, **156**

## D

decorator, **156** descriptor, **156** dictionary, **157** object, 91 dictionary view, **157** DictionaryType (in module types), 91 DictType (in module types), 91 divmod built-in function, 48 docstring, **157** duck-typing, **157**

## E

EAFP, **157** environment variable exec\_prefix, 3, 4 PATH, 9 prefix, 3, 4 PYTHONDUMPREFS, 136 PYTHONHOME, 9, 114

PYTHONPATH, 9 PYTHONSHOWALLOCCOUNT, 148 EOFError (built-in exception), 97 exc\_info() (in module sys), 7 exc\_traceback (in module sys), 7, 17 exc\_type (in module sys), 7, 17 exc\_value (in module sys), 7, 17 exceptions module, 9 exec\_prefix, 3, 4 executable (in module sys), 112 exit(), 26 expression, **157** extension module, **157**

## F

file object, 96 file object, **157** file-like object, **157** FileType (in module types), 96 finder, **157** float built-in function, 50 floating point object, 63 FloatType (in modules types), 63 floor division, **157** fopen(), 96 free(), 125 freeze utility, 29 frozenset object, 108 function, **157** object, 94

## G

garbage collection, **158** generator, **158** generator expression, **158** GIL, 114, **158** global interpreter lock, 114, **158**

## H

hash built-in function, 46, 139 hashable, **158**

## I

IDLE, **158** ihooks module, 27 immutable, **158** importer, **159**

<!-- page: 189 -->

importing, **159** incr\_item(), 8, 9 inquiry (C type), 154 instance object, 94 int built-in function, 50 integer object, 58 integer division, **158** interactive, **159** interpreted, **159** interpreter lock, 114 IntType (in modules types), 58 iterable, **159** iterator, **159**

## K

key function, **159** KeyboardInterrupt (built-in exception), 20 keyword argument, **159**

## L

lambda, **159** LBYL, **159** len built-in function, 46, 50, 53, 90, 92, 109 list, **160** object, 89 list comprehension, **160** loader, **160** lock, interpreter, 114 long built-in function, 50 long integer object, 60 LONG\_MAX, 60, 61 LongType (in modules types), 60

## M

magic method, 160 magic method, **160** main(), 112, 113 malloc(), 125 mapping, **160** object, 91 metaclass, **160** METH\_CLASS (built-in variable), 132 METH\_COEXIST (built-in variable), 133 METH\_KEYWORDS (built-in variable), 132 METH\_NOARGS (built-in variable), 132 METH\_O (built-in variable), 132 METH\_OLDARGS (built-in variable), 132

METH\_STATIC (built-in variable), 132 METH\_VARARGS (built-in variable), 132 method, **160** magic, 160 object, 95 special, 162 method resolution order, **160** MethodType (in module types), 94, 95 module, **160** \_builtin\_\_, 9, 111 main\_\_, 9, 111, 119 builtins, 119 exceptions, 9 ihooks, 27 object, 98 rexec, 27 search path, 9, 111, 112 signal, 20 sys, 9, 111, 119 thread, 116 modules (in module sys), 27, 111 ModuleType (in module types), 98 MRO, **160** mutable, **160**

## N

named tuple, **160** namespace, **160** nested scope, **161** new-style class, **161** None object, 58 numeric object, 58

object, **161** buffer, 83 bytearray, 65 Capsule, 102 class, 94 CObject, 103 code, 109 complex number, 64 dictionary, 91 file, 96 floating point, 63 frozenset, 108 function, 94 instance, 94 integer, 58 list, 89 long integer, 60 mapping, 91

<!-- page: 190 -->

```csv
method, 95
module, 98
None, 58
numeric, 58
sequence, 65
set, 108
string, 66
tuple, 87
type, 4, 57
OverflowError (built-in exception), 61, 62
```

## P

package, **161** package variable all\_\_, 27 parameter, **161** PATH, 9 path module search, 9, 111, 112 path (in module sys), 9, 111, 112 PEP, **161** platform (in module sys), 113 positional argument, **161** pow built-in function, 48, 49 prefix, 3, 4 Py\_AddPendingCall (C function), 120 Py\_AddPendingCall(), 120 Py\_AtExit (C function), 26 Py\_BEGIN\_ALLOW\_THREADS, 115 Py\_BEGIN\_ALLOW\_THREADS (C macro), 117 Py\_BLOCK\_THREADS (C macro), 118 Py\_buffer (C type), 83 Py\_buffer.buf (C member), 83 Py\_buffer.internal (C member), 84 Py\_buffer.itemsize (C member), 84 Py\_buffer.ndim (C member), 83 Py\_buffer.readonly (C member), 83 Py\_buffer.shape (C member), 83 Py\_buffer.strides (C member), 83 Py\_buffer.suboffsets (C member), 83 Py\_BuildValue (C function), 35 Py\_CLEAR (C function), 15 Py\_CompileString (C function), 13 Py\_CompileString(), 14 Py\_CompileStringFlags (C function), 13 Py\_complex (C type), 64 Py\_DECREF (C function), 15 Py\_DECREF(), 4 Py\_Ellipsis (C variable), 101 Py\_END\_ALLOW\_THREADS, 115 Py\_END\_ALLOW\_THREADS (C macro), 118 Py\_END\_OF\_BUFFER (C variable), 86 Py\_EndInterpreter (C function), 120

Py\_EnterRecursiveCall (C function), 22 Py\_eval\_input (C variable), 13 Py\_Exit (C function), 26 Py\_False (C variable), 60 Py\_FatalError (C function), 26 Py\_FatalError(), 113 Py\_FdIsInteractive (C function), 25 Py\_file\_input (C variable), 14 Py\_Finalize (C function), 111 Py\_Finalize(), 26, 111, 120 Py\_FindMethod (C function), 134 Py\_GetBuildInfo (C function), 113 Py\_GetCompiler (C function), 113 Py\_GetCopyright (C function), 113 Py\_GetExecPrefix (C function), 112 Py\_GetExecPrefix(), 9 Py\_GetPath (C function), 112 Py\_GetPath(), 9, 112 Py\_GetPlatform (C function), 113 Py\_GetPrefix (C function), 112 Py\_GetPrefix(), 9 Py\_GetProgramFullPath (C function), 112 Py\_GetProgramFullPath(), 9 Py\_GetProgramName (C function), 112 Py\_GetPythonHome (C function), 114 Py\_GetVersion (C function), 113 Py\_INCREF (C function), 15 Py\_INCREF(), 4 Py\_Initialize (C function), 111 Py\_Initialize(), 9, 112, 116, 120 Py\_InitializeEx (C function), 111 Py\_InitModule (C function), 129 Py\_InitModule3 (C function), 130 Py\_InitModule4 (C function), 130 Py\_IsInitialized (C function), 111 Py\_IsInitialized(), 9 Py\_LeaveRecursiveCall (C function), 22 Py\_Main (C function), 11 Py\_NewInterpreter (C function), 119 Py\_None (C variable), 58 Py\_PRINT\_RAW, 97 Py\_REFCNT (C macro), 131 Py\_RETURN\_FALSE (C macro), 60 Py\_RETURN\_NONE (C macro), 58 Py\_RETURN\_TRUE (C macro), 60 Py\_SetProgramName (C function), 112 Py\_SetProgramName(), 9, 111, 112 Py\_SetPythonHome (C function), 114 Py\_single\_input (C variable), 14 Py\_SIZE (C macro), 131 PY\_SSIZE\_T\_MAX, 62 Py\_TPFLAGS\_BASETYPE (built-in variable), 141 Py\_TPFLAGS\_CHECKTYPES (built-in variable), 141 Py\_TPFLAGS\_DEFAULT (built-in variable), 142

<!-- page: 191 -->

Py\_TPFLAGS\_GC (built-in variable), 141

Py\_TPFLAGS\_HAVE\_CLASS (built-in variable), 141

Py\_TPFLAGS\_HAVE\_GC (built-in variable), 142

Py\_TPFLAGS\_HAVE\_GETCHARBUFFER (built-in variable), 140, 152

Py\_TPFLAGS\_HAVE\_INPLACEOPS (built-in variable), 141

Py\_TPFLAGS\_HAVE\_ITER (built-in variable), 141

Py\_TPFLAGS\_HAVE\_RICHCOMPARE (built-in variable), 141

Py\_TPFLAGS\_HAVE\_SEQUENCE\_IN (built-in variable), 141

Py\_TPFLAGS\_HAVE\_WEAKREFS (built-in variable), 141

Py\_TPFLAGS\_HEAPTYPE (built-in variable), 141

Py\_TPFLAGS\_READY (built-in variable), 141

Py\_TPFLAGS\_READYING (built-in variable), 141

Py\_tracefunc (C type), 121

Py\_True (C variable), 60

Py\_TYPE (C macro), 131

Py\_UNBLOCK\_THREADS (C macro), 118

Py\_UNICODE (C type), 70

Py\_UNICODE\_ISALNUM (C function), 71

Py\_UNICODE\_ISALPHA (C function), 71

Py\_UNICODE\_ISDECIMAL (C function), 71

Py\_UNICODE\_ISDIGIT (C function), 71

Py\_UNICODE\_ISLINEBREAK (C function), 71

Py\_UNICODE\_ISLOWER (C function), 71

Py\_UNICODE\_ISNUMERIC (C function), 71

Py\_UNICODE\_ISSPACE (C function), 71

Py\_UNICODE\_ISTITLE (C function), 71

Py\_UNICODE\_ISUPPER (C function), 71

Py\_UNICODE\_TODECIMAL (C function), 72

Py\_UNICODE\_TODIGIT (C function), 72

Py\_UNICODE\_TOLOWER (C function), 71

Py\_UNICODE\_TONUMERIC (C function), 72

Py\_UNICODE\_TOTITLE (C function), 72

Py\_UNICODE\_TOUPPER (C function), 71

Py\_VaBuildValue (C function), 37

Py\_VISIT (C function), 153

Py\_XDECREF (C function), 15

Py\_XDECREF(), 9

Py\_XINCREF (C function), 15

PyAnySet\_Check (C function), 108

PyAnySet\_CheckExact (C function), 108

PyArg\_Parse (C function), 35

PyArg\_ParseTuple (C function), 34

PyArg\_ParseTupleAndKeywords (C function), 34

PyArg\_UnpackTuple (C function), 35

PyArg\_VaParse (C function), 34

PyBuffer\_Check (C function), 87

PyBuffer\_FillContiguousStrides (C function), 85

PyBuffer\_FillInfo (C function), 85

PyBuffer\_FromMemory (C function), 87

PyBuffer\_FromObject (C function), 87

PyBuffer\_FromReadWriteMemory (C function), 87

PyBuffer\_FromReadWriteObject (C function), 87

PyBuffer\_IsContiguous (C function), 85

PyBuffer\_New (C function), 87

PyBuffer\_Release (C function), 85

PyBuffer\_SizeFromFormat (C function), 85

PyBuffer\_Type (C variable), 86

PyBufferObject (C type), 86

PyBufferProcs, 86

PyBufferProcs (C type), 151

PyByteArray\_AS\_STRING (C function), 66

PyByteArray\_AsString (C function), 66

PyByteArray\_Check (C function), 66

PyByteArray\_CheckExact (C function), 66

PyByteArray\_Concat (C function), 66

ywords (C function),PyCell\_GET (C function), 104 PyArg\_VaParseTupleAndKe 35

PyByteArray\_FromObject (C function), 66

PyByteArray\_FromStringAndSize (C function), 66

PyByteArray\_GET\_SIZE (C function), 66

PyByteArray\_Resize (C function), 66

PyByteArray\_Size (C function), 66

PyByteArray\_Type (C variable), 65

PyByteArrayObject (C type), 65

PyCallable\_Check (C function), 45

PyCallIter\_Check (C function), 99

PyCallIter\_New (C function), 99

PyCallIter\_Type (C variable), 99

PyCapsule (C type), 102

PyCapsule\_CheckExact (C function), 102

PyCapsule\_Destructor (C type), 102

PyCapsule\_GetContext (C function), 102

PyCapsule\_GetDestructor (C function), 102

PyCapsule\_GetName (C function), 102

PyCapsule\_GetPointer (C function), 102

PyCapsule\_Import (C function), 103

PyCapsule\_IsValid (C function), 103

PyCapsule\_New (C function), 102

PyCapsule\_SetContext (C function), 103

PyCapsule\_SetDestructor (C function), 103

PyCapsule\_SetName (C function), 103

PyCapsule\_SetPointer (C function), 103

PyBool\_Check (C function), 60

PyCell\_Check (C function), 104

PyCell\_Get (C function), 104

PyBool\_FromLong (C function), 60

PyCell\_New (C function), 104

PyCell\_SET (C function), 104

<!-- page: 192 -->

PyCell\_Set (C function), 104 PyDate\_FromTimestamp (C function), 107 PyCell\_Type (C variable), 104 PyDateTime\_Check (C function), 105 PyCellObject (C type), 104 PyDateTime\_CheckExact (C function), 105 PyCFunction (C type), 131 PyDateTime\_DATE\_GET\_HOUR (C function), 107 PyClass\_Check (C function), 94 PyDateTime\_DATE\_GET\_MICROSECOND (C func-PyClass\_IsSubclass (C function), 94 tion), 107 PyClass\_Type (C variable), 94 PyDateTime\_DATE\_GET\_MINUTE (C function), 107 PyClassObject (C type), 94 PyDateTime\_DATE\_GET\_SECOND (C function), 107 PyCObject (C type), 103 PyDateTime\_FromDateAndTime (C function), 106 PyCObject\_AsVoidPtr (C function), 104 PyDateTime\_FromTimestamp (C function), 107 PyCObject\_Check (C function), 103 PyDateTime\_GET\_DAY (C function), 106 PyCObject\_FromVoidPtr (C function), 103 PyDateTime\_GET\_MONTH (C function), 106 PyCObject\_FromVoidPtrAndDesc (C function), PyDateTime\_GET\_YEAR (C function), 106 104 PyDateTime\_TIME\_GET\_HOUR (C function), 107 PyCObject\_GetDesc (C function), 104 PyDateTime\_TIME\_GET\_MICROSECOND (C func-PyCObject\_SetVoidPtr (C function), 104 tion), 107 PyCode\_Check (C function), 109 PyDateTime\_TIME\_GET\_MINUTE (C function), 107 PyCode\_GetNumFree (C function), 109 PyDateTime\_TIME\_GET\_SECOND (C function), 107 PyCode\_New (C function), 109 PyDelta\_Check (C function), 105 PyCode\_NewEmpty (C function), 110 PyDelta\_CheckExact (C function), 106 PyCode\_Type (C variable), 109 PyDelta\_FromDSU (C function), 106 PyCodec\_BackslashReplaceErrors (C func- PyDescr\_IsData (C function), 100 tion), 41 PyDescr\_NewClassMethod (C function), 100 PyCodec\_Decode (C function), 40 PyDescr\_NewGetSet (C function), 99 PyCodec\_Decoder (C function), 40 PyDescr\_NewMember (C function), 99 PyCodec\_Encode (C function), 40 PyDescr\_NewMethod (C function), 99 PyCodec\_Encoder (C function), 40 PyDescr\_NewWrapper (C function), 100 PyCodec\_IgnoreErrors (C function), 41 PyDict\_Check (C function), 91 PyCodec\_IncrementalDecoder (C function), 40 PyDict\_CheckExact (C function), 91 PyCodec\_IncrementalEncoder (C function), 40 PyDict\_Clear (C function), 92 PyCodec\_KnownEncoding (C function), 40 PyDict\_Contains (C function), 92 PyCodec\_LookupError (C function), 41 PyDict\_Copy (C function), 92 PyCodec\_Register (C function), 40 PyDict\_DelItem (C function), 92 PyCodec\_RegisterError (C function), 41 PyDict\_DelItemString (C function), 92 PyCodec\_ReplaceErrors (C function), 41 PyDict\_GetItem (C function), 92 PyCodec\_StreamReader (C function), 40 PyDict\_GetItemString (C function), 92 PyCodec\_StreamWriter (C function), 40 PyDict\_Items (C function), 92 PyCodec\_StrictErrors (C function), 41 PyDict\_Keys (C function), 92 PyCodec\_XMLCharRefReplaceErrors (C func- PyDict\_Merge (C function), 93 tion), 41 PyDict\_MergeFromSeq2 (C function), 93 PyCodeObject (C type), 109 PyDict\_New (C function), 91 PyCompilerFlags (C type), 14 PyDict\_Next (C function), 92 PyComplex\_AsCComplex (C function), 65 PyDict\_SetItem (C function), 92 PyComplex\_Check (C function), 65 PyDict\_SetItemString (C function), 92 PyComplex\_CheckExact (C function), 65 PyDict\_Size (C function), 92 PyComplex\_FromCComplex (C function), 65 PyDict\_Type (C variable), 91 PyComplex\_FromDoubles (C function), 65 PyDict\_Update (C function), 93 PyComplex\_ImagAsDouble (C function), 65 PyDict\_Values (C function), 92 PyComplex\_RealAsDouble (C function), 65 PyDictObject (C type), 91 PyComplex\_Type (C variable), 65 PyDictProxy\_New (C function), 91 PyComplexObject (C type), 65 PyErr\_BadArgument (C function), 18 PyDate\_Check (C function), 105 PyErr\_BadInternalCall (C function), 19 PyDate\_CheckExact (C function), 105 PyErr\_CheckSignals (C function), 20 PyDate\_FromDate (C function), 106 PyErr\_Clear (C function), 18

<!-- page: 193 -->

PyErr\_Clear(), 7, 9 PyEval\_GetRestricted (C function), 39 PyErr\_ExceptionMatches (C function), 17 PyEval\_InitThreads (C function), 116 PyErr\_ExceptionMatches(), 9 PyEval\_InitThreads(), 111 PyErr\_Fetch (C function), 18 PyEval\_MergeCompilerFlags (C function), 13 PyErr\_Format (C function), 18 PyEval\_ReInitThreads (C function), 117 PyErr\_GivenExceptionMatches (C function), 17 PyEval\_ReleaseLock (C function), 119 PyErr\_NewException (C function), 20 PyEval\_ReleaseLock(), 111, 116 PyErr\_NewExceptionWithDoc (C function), 21 PyEval\_ReleaseThread (C function), 119 PyErr\_NoMemory (C function), 18 PyEval\_ReleaseThread(), 116 PyErr\_NormalizeException (C function), 18 PyEval\_RestoreThread (C function), 117 PyErr\_Occurred (C function), 17 PyEval\_RestoreThread(), 115, 116 PyErr\_Occurred(), 7 PyEval\_SaveThread (C function), 116 PyErr\_Print (C function), 17 PyEval\_SaveThread(), 115, 116 PyErr\_PrintEx (C function), 17 PyEval\_SetProfile (C function), 122 PyErr\_Restore (C function), 18 PyEval\_SetTrace (C function), 122 PyErr\_SetExcFromWindowsErr (C function), 19 PyEval\_ThreadsInitialized (C function), 116 PyErr\_SetExcFromWindowsErrWithFilename PyExc\_ArithmeticError, 22 (C function), 19 PyExc\_AssertionError, 22 PyErr\_SetExcFromWindowsErrWithFilenameObjectPyExc\_AttributeError, 22 (C function), 19 PyExc\_BaseException, 22 PyErr\_SetFromErrno (C function), 19 PyExc\_BufferError, 22 PyErr\_SetFromErrnoWithFilename (C func- PyExc\_BytesWarning, 24 tion), 19 PyExc\_DeprecationWarning, 24 PyErr\_SetFromErrnoWithFilenameObject (C PyExc\_EnvironmentError, 22 function), 19 PyExc\_EOFError, 22 PyErr\_SetFromWindowsErr (C function), 19 PyExc\_Exception, 22 PyErr\_SetFromWindowsErrWithFilename (C PyExc\_FloatingPointError, 22 function), 19 PyExc\_FutureWarning, 24 PyErr\_SetFromWindowsErrWithFilenameObjectPyExc\_GeneratorExit, 22 (C function), 19 PyExc\_ImportError, 22 PyErr\_SetInterrupt (C function), 20 PyExc\_ImportWarning, 24 PyErr\_SetNone (C function), 18 PyExc\_IndentationError, 22 PyErr\_SetObject (C function), 18 PyExc\_IndexError, 22 PyErr\_SetString (C function), 18 PyExc\_IOError, 22 PyErr\_SetString(), 7 PyExc\_KeyboardInterrupt, 22 PyErr\_Warn (C function), 20 PyExc\_KeyError, 22 PyErr\_WarnEx (C function), 19 PyExc\_LookupError, 22 PyErr\_WarnExplicit (C function), 20 PyExc\_MemoryError, 22 PyErr\_WarnPy3k (C function), 20 PyExc\_NameError, 22 PyErr\_WriteUnraisable (C function), 21 PyExc\_NotImplementedError, 22 PyEval\_AcquireLock (C function), 119 PyExc\_OSError, 22 PyEval\_AcquireLock(), 111 PyExc\_OverflowError, 22 PyEval\_AcquireThread (C function), 119 PyExc\_PendingDeprecationWarning, 24 PyEval\_EvalCode (C function), 13 PyExc\_ReferenceError, 22 PyEval\_EvalCodeEx (C function), 13 PyExc\_RuntimeError, 22 PyEval\_EvalFrame (C function), 13 PyExc\_RuntimeWarning, 24 PyEval\_EvalFrameEx (C function), 13 PyExc\_StandardError, 22 PyEval\_GetBuiltins (C function), 39 PyExc\_StopIteration, 22 PyEval\_GetCallStats (C function), 122 PyExc\_SyntaxError, 22 PyEval\_GetFrame (C function), 39 PyExc\_SyntaxWarning, 24 PyEval\_GetFuncDesc (C function), 39 PyExc\_SystemError, 22 PyEval\_GetFuncName (C function), 39 PyExc\_SystemExit, 22 PyEval\_GetGlobals (C function), 39 PyExc\_TabError, 22 PyEval\_GetLocals (C function), 39 PyExc\_TypeError, 22

<!-- page: 194 -->

PyExc\_UnboundLocalError, 22 PyExc\_UnicodeDecodeError, 22 PyExc\_UnicodeEncodeError, 22 PyExc\_UnicodeError, 22 PyExc\_UnicodeTranslateError, 22 PyExc\_UnicodeWarning, 24 PyExc\_UserWarning, 24 PyExc\_ValueError, 22 PyExc\_VMSError, 22 PyExc\_Warning, 24 PyExc\_WindowsError, 22 PyExc\_ZeroDivisionError, 22 PyFile\_AsFile (C function), 96 PyFile\_Check (C function), 96 PyFile\_CheckExact (C function), 96 PyFile\_DecUseCount (C function), 97 PyFile\_FromFile (C function), 96 PyFile\_FromString (C function), 96 PyFile\_GetLine (C function), 97 PyFile\_IncUseCount (C function), 96 PyFile\_Name (C function), 97 PyFile\_SetBufSize (C function), 97 PyFile\_SetEncoding (C function), 97 PyFile\_SetEncodingAndErrors (C function), 9 PyFile\_SoftSpace (C function), 97 PyFile\_Type (C variable), 96 PyFile\_WriteObject (C function), 97 PyFile\_WriteString (C function), 97 PyFileObject (C type), 96 PyFloat\_AS\_DOUBLE (C function), 63 PyFloat\_AsDouble (C function), 63 PyFloat\_AsReprString (C function), 63 PyFloat\_AsString (C function), 63 PyFloat\_Check (C function), 63 PyFloat\_CheckExact (C function), 63 PyFloat\_ClearFreeList (C function), 63 PyFloat\_FromDouble (C function), 63 PyFloat\_FromString (C function), 63 PyFloat\_GetInfo (C function), 63 PyFloat\_GetMax (C function), 63 PyFloat\_GetMin (C function), 63 PyFloat\_Type (C variable), 63 PyFloatObject (C type), 63 PyFrame\_GetLineNumber (C function), 39 PyFrozenSet\_Check (C function), 108 PyFrozenSet\_CheckExact (C function), 108 PyFrozenSet\_New (C function), 108 PyFrozenSet\_Type (C variable), 108 PyFunction\_Check (C function), 94 PyFunction\_GetClosure (C function), 95 PyFunction\_GetCode (C function), 95 PyFunction\_GetDefaults (C function), 95 PyFunction\_GetGlobals (C function), 95 PyFunction\_GetModule (C function), 95

PyFunction\_New (C function), 95 PyFunction\_SetClosure (C function), 95 PyFunction\_SetDefaults (C function), 95 PyFunction\_Type (C variable), 94 PyFunctionObject (C type), 94 PyGen\_Check (C function), 105 PyGen\_CheckExact (C function), 105 PyGen\_New (C function), 105 PyGen\_Type (C variable), 105 PyGenObject (C type), 105 PyGetSetDef (C type), 134 PyGILState\_Ensure (C function), 117 PyGILState\_GetThisThreadState (C function), 117 PyGILState\_Release (C function), 117 PyImport\_AddModule (C function), 28 PyImport\_AppendInittab (C function), 29 PyImport\_Cleanup (C function), 28 PyImport\_ExecCodeModule (C function), 28 PyImport\_ExecCodeModuleEx (C function), 28 PyImport\_ExtendInittab (C function), 29 PyImport\_FrozenModules (C variable), 29 PyImport\_GetImporter (C function), 28 PyImport\_GetMagicNumber (C function), 28 PyImport\_GetModuleDict (C function), 28 PyImport\_Import (C function), 27 PyImport\_ImportFrozenModule (C function), 29 PyImport\_ImportModule (C function), 27 PyImport\_ImportModuleEx (C function), 27 PyImport\_ImportModuleLevel (C function), 27 PyImport\_ImportModuleNoBlock (C function), 27 PyImport\_ReloadModule (C function), 27 PyIndex\_Check (C function), 50 PyInstance\_Check (C function), 94 PyInstance\_New (C function), 94 PyInstance\_NewRaw (C function), 94 PyInstance\_Type (C variable), 94 PyInt\_AS\_LONG (C function), 59 PyInt\_AsLong (C function), 59 PyInt\_AsSsize\_t (C function), 59 PyInt\_AsUnsignedLongLongMask (C function), 59 PyInt\_AsUnsignedLongMask (C function), 59 PyInt\_Check (C function), 58 PyInt\_CheckExact (C function), 59 PyInt\_ClearFreeList (C function), 60 PyInt\_FromLong (C function), 59 PyInt\_FromSize\_t (C function), 59 PyInt\_FromSsize\_t (C function), 59 PyInt\_FromString (C function), 59 PyInt\_GetMax (C function), 59 PyInt\_Type (C variable), 58 PyInterpreterState (C type), 116

<!-- page: 195 -->

PyInterpreterState\_Clear (C function), 118

PyInterpreterState\_Delete (C function), 118

PyInterpreterState\_Head (C function), 122

PyInterpreterState\_New (C function), 118

PyInterpreterState\_Next (C function), 122

PyInterpreterState\_ThreadHead (C function), 123

PyIntObject (C type), 58

PyIter\_Check (C function), 54

PyIter\_Next (C function), 54

PyList\_Append (C function), 91

PyList\_AsTuple (C function), 91

PyList\_Check (C function), 89

PyList\_CheckExact (C function), 89

PyList\_GET\_ITEM (C function), 90

PyList\_GET\_SIZE (C function), 90

PyList\_GetItem (C function), 90

PyList\_GetItem(), 6

PyList\_GetSlice (C function), 91

PyList\_Insert (C function), 90

PyList\_New (C function), 89

PyList\_Reverse (C function), 91

PyList\_SET\_ITEM (C function), 90

PyList\_SetItem (C function), 90

PyList\_SetItem(), 5

PyList\_SetSlice (C function), 91

PyList\_Size (C function), 90

PyList\_Sort (C function), 91

PyList\_Type (C variable), 89

PyListObject (C type), 89

PyLong\_AsDouble (C function), 62

PyLong\_AsLong (C function), 61

PyLong\_AsLongAndOverflow (C function), 61

PyLong\_AsLongLong (C function), 62

PyLong\_AsLongLongAndOverflow (C function), 62

PyLong\_AsSsize\_t (C function), 62

PyLong\_AsUnsignedLong (C function), 62

PyLong\_AsUnsignedLongLong (C function), 62

PyLong\_AsUnsignedLongLongMask (C function), PyMemberDef (C type), 133 62

PyLong\_AsUnsignedLongMask (C function), 62

PyLong\_AsVoidPtr (C function), 62

PyLong\_FromLongLong (C function), 61

PyLong\_Check (C function), 60

PyLong\_FromSize\_t (C function), 61

PyLong\_FromSsize\_t (C function), 61

PyLong\_FromString (C function), 61

PyLong\_FromUnicode (C function), 61

PyLong\_FromLong (C function), 61

PyLong\_FromUnsignedLong (C function), 61

PyLong\_FromDouble (C function), 61

PyLong\_FromVoidPtr (C function), 61

PyLong\_CheckExact (C function), 60

PyLong\_Type (C variable), 60

PyLongObject (C type), 60

PyLong\_FromUnsignedLongLong (C function), 61

PyMapping\_Check (C function), 53

PyMapping\_DelItem (C function), 53

PyMapping\_DelItemString (C function), 53

PyMapping\_GetItemString (C function), 53

PyMapping\_HasKey (C function), 53

PyMapping\_HasKeyString (C function), 53

PyMapping\_Items (C function), 53

PyMapping\_Keys (C function), 53

PyMapping\_Length (C function), 53

PyMapping\_SetItemString (C function), 53

PyMapping\_Size (C function), 53

PyMapping\_Values (C function), 53

PyMappingMethods (C type), 150

PyMappingMethods.mp\_ass\_subscript (C member), 150

PyMappingMethods.mp\_length (C member), 150

PyMarshal\_ReadObjectFromFile (C function), 30

PyMappingMethods.mp\_subscript (C member), 150

PyMarshal\_ReadLongFromFile (C function), 30

PyMarshal\_ReadLastObjectFromFile (C function), 30

PyMarshal\_ReadObjectFromString (C function), 30

PyMarshal\_ReadShortFromFile (C function), 30

PyMarshal\_WriteLongToFile (C function), 30

PyMarshal\_WriteObjectToFile (C function), 30

PyMarshal\_WriteObjectToString (C function), 30

PyMem\_Free (C function), 126

PyMem\_Del (C function), 126

PyMem\_Malloc (C function), 126

PyMem\_New (C function), 126

PyMem\_Realloc (C function), 126

PyMem\_Resize (C function), 126

PyMemoryView\_Check (C function), 86

PyMemoryView\_FromBuffer (C function), 86

PyMemoryView\_FromObject (C function), 86

PyMemoryView\_GET\_BUFFER (C function), 86

PyMemoryView\_GetContiguous (C function), 86

PyMethod\_Check (C function), 95

PyMethod\_Class (C function), 95

PyMethod\_ClearFreeList (C function), 96

PyMethod\_Function (C function), 95

PyMethod\_GET\_CLASS (C function), 95

PyMethod\_GET\_FUNCTION (C function), 95

PyMethod\_GET\_SELF (C function), 96

PyMethod\_New (C function), 95

PyMethod\_Self (C function), 96

<!-- page: 196 -->

PyMethod\_Type (C variable), 95

PyMethodDef (C type), 132

PyModule\_AddIntConstant (C function), 98

PyModule\_AddIntMacro (C function), 98

PyModule\_AddObject (C function), 98

PyModule\_AddStringConstant (C function), 98

PyModule\_AddStringMacro (C function), 98

PyModule\_Check (C function), 98

PyModule\_CheckExact (C function), 98

PyModule\_GetDict (C function), 98

PyModule\_GetFilename (C function), 98

PyModule\_GetName (C function), 98

PyModule\_New (C function), 98

PyModule\_Type (C variable), 98

PyNumber\_Absolute (C function), 48

PyNumber\_Add (C function), 47

PyNumber\_And (C function), 48

PyNumber\_AsSsize\_t (C function), 50

PyNumber\_Check (C function), 47

PyNumber\_Coerce (C function), 49

PyNumber\_CoerceEx (C function), 49

PyNumber\_Divide (C function), 47

PyNumber\_Divmod (C function), 48

PyNumber\_Float (C function), 50

PyNumber\_FloorDivide (C function), 47

PyNumber\_InPlaceAdd (C function), 48

PyNumber\_InPlaceAnd (C function), 49

PyNumber\_InPlaceDivide (C function), 49

PyNumber\_InPlaceFloorDivide (C function), 49

PyNumber\_InPlaceLshift (C function), 49

PyNumber\_InPlaceMultiply (C function), 48

PyNumber\_InPlaceOr (C function), 49

PyNumber\_InPlacePower (C function), 49

PyNumber\_InPlaceRemainder (C function), 49

PyNumber\_InPlaceRshift (C function), 49

PyNumber\_InPlaceSubtract (C function), 48

PyNumber\_InPlaceTrueDivide (C function), 49

PyNumber\_InPlaceXor (C function), 49

PyNumber\_Int (C function), 49

PyNumber\_Invert (C function), 48

PyNumber\_Long (C function), 50

PyNumber\_Lshift (C function), 48

PyNumber\_Multiply (C function), 47

PyNumber\_Negative (C function), 48

PyNumber\_Or (C function), 48

PyNumber\_Positive (C function), 48

PyNumber\_Power (C function), 48

PyNumber\_Remainder (C function), 48

PyNumber\_Rshift (C function), 48

PyNumber\_Subtract (C function), 47

PyNumber\_ToBase (C function), 50

PyNumber\_TrueDivide (C function), 47

PyNumber\_Xor (C function), 48

PyNumberMethods (C type), 149

PyNumberMethods.nb\_coerce (C member), 150

PyObject (C type), 130

PyObject\_AsCharBuffer (C function), 54

PyObject\_AsFileDescriptor (C function), 47

PyObject\_AsReadBuffer (C function), 54

PyObject\_AsWriteBuffer (C function), 55

PyObject\_Bytes (C function), 44

PyObject\_Call (C function), 45

PyObject\_CallFunction (C function), 45

PyObject\_CallFunctionObjArgs (C function),

46

PyObject\_CallMethod (C function), 45

PyObject\_CallMethodObjArgs (C function), 46

PyObject\_CallObject (C function), 45

PyObject\_CheckBuffer (C function), 84

PyObject\_CheckReadBuffer (C function), 55

PyObject\_Cmp (C function), 44

PyObject\_Compare (C function), 44

PyObject\_Del (C function), 129

PyObject\_DelAttr (C function), 44

PyObject\_DelAttrString (C function), 44

PyObject\_DelItem (C function), 47

PyObject\_Dir (C function), 47

PyObject\_Free (C function), 127

PyObject\_GC\_Del (C function), 153

PyObject\_GC\_New (C function), 152

PyObject\_GC\_NewVar (C function), 152

PyObject\_GC\_Resize (C function), 153

PyObject\_GC\_Track (C function), 153

PyObject\_GC\_UnTrack (C function), 153

PyObject\_GenericGetAttr (C function), 43

PyObject\_GenericSetAttr (C function), 44

PyObject\_GetAttr (C function), 43

PyObject\_GetAttrString (C function), 43

PyObject\_GetBuffer (C function), 84

PyObject\_GetItem (C function), 46

PyObject\_GetIter (C function), 47

PyObject\_HasAttr (C function), 43

PyObject\_HasAttrString (C function), 43

PyObject\_Hash (C function), 46

PyObject\_HashNotImplemented (C function), 46

PyObject\_HEAD (C macro), 130

PyObject\_HEAD\_INIT (C macro), 131

PyObject\_Init (C function), 129

PyObject\_InitVar (C function), 129

PyObject\_IsInstance (C function), 45

PyObject\_IsSubclass (C function), 45

PyObject\_IsTrue (C function), 46

PyObject\_Length (C function), 46

PyObject\_Malloc (C function), 127

PyObject\_New (C function), 129

PyObject\_NewVar (C function), 129

PyObject\_Not (C function), 46

<!-- page: 197 -->

PyObject.\_ob\_next (C member), 136

PyObject.\_ob\_prev (C member), 136

PyObject\_Print (C function), 43

PyObject\_Realloc (C function), 127

PyObject\_Repr (C function), 44

PyObject\_RichCompare (C function), 44

PyObject\_RichCompareBool (C function), 44

PyObject\_SetAttr (C function), 43

PyObject\_SetAttrString (C function), 43

PyObject\_SetItem (C function), 47

PyObject\_Size (C function), 46

PyObject\_Str (C function), 44

PyObject\_Type (C function), 46

PyObject\_TypeCheck (C function), 46

PyObject\_Unicode (C function), 44

PyObject\_VAR\_HEAD (C macro), 131

PyObject.ob\_refcnt (C member), 136

PyObject.ob\_type (C member), 136

PyOS\_AfterFork (C function), 25

PyOS\_ascii\_atof (C function), 39

PyOS\_ascii\_formatd (C function), 38

PyOS\_ascii\_strtod (C function), 38

PyOS\_CheckStack (C function), 25

PyOS\_double\_to\_string (C function), 38

PyOS\_getsig (C function), 25

PyOS\_setsig (C function), 25

PyOS\_snprintf (C function), 37

PyOS\_stricmp (C function), 39

PyOS\_string\_to\_double (C function), 37

PyOS\_strnicmp (C function), 39

PyOS\_vsnprintf (C function), 37

PyParser\_SimpleParseFile (C function), 12

PyParser\_SimpleParseFileFlags (C function), 12

PyParser\_SimpleParseString (C function), 12

PyParser\_SimpleParseStringFlags (C function), 12

PyParser\_SimpleParseStringFlagsFilename (C function), 12

PyProperty\_Type (C variable), 99

PyRun\_AnyFile (C function), 11

PyRun\_AnyFileEx (C function), 11

PyRun\_AnyFileExFlags (C function), 11

PyRun\_AnyFileFlags (C function), 11

PyRun\_File (C function), 13

PyRun\_FileEx (C function), 13

PyRun\_FileExFlags (C function), 13

PyRun\_FileFlags (C function), 13

PyRun\_InteractiveLoop (C function), 12

PyRun\_InteractiveLoopFlags (C function), 12

PyRun\_InteractiveOne (C function), 12

PyRun\_InteractiveOneFlags (C function), 12

PyRun\_SimpleFile (C function), 12

PyRun\_SimpleFileEx (C function), 12

PyRun\_SimpleFileExFlags (C function), 12

PyRun\_SimpleFileFlags (C function), 12

PyRun\_SimpleString (C function), 11

PyRun\_SimpleStringFlags (C function), 11

PyRun\_String (C function), 12

PyRun\_StringFlags (C function), 12

PySeqIter\_Check (C function), 99

PySeqIter\_New (C function), 99

PySeqIter\_Type (C variable), 99

PySequence\_Check (C function), 50

PySequence\_Concat (C function), 50

PySequence\_Contains (C function), 52

PySequence\_Count (C function), 51

PySequence\_DelItem (C function), 51

PySequence\_DelSlice (C function), 51

PySequence\_Fast (C function), 52

PySequence\_Fast\_GET\_ITEM (C function), 52

PySequence\_Fast\_GET\_SIZE (C function), 52

PySequence\_Fast\_ITEMS (C function), 52

PySequence\_GetItem (C function), 51

PySequence\_GetItem(), 6

PySequence\_GetSlice (C function), 51

PySequence\_Index (C function), 52

PySequence\_InPlaceConcat (C function), 51

PySequence\_InPlaceRepeat (C function), 51

PySequence\_ITEM (C function), 52

PySequence\_Length (C function), 50

PySequence\_List (C function), 52

PySequence\_Repeat (C function), 50

PySequence\_SetItem (C function), 51

PySequence\_SetSlice (C function), 51

PySequence\_Size (C function), 50

PySequence\_Tuple (C function), 52

PySequenceMethods (C type), 150

PySequenceMethods.sq\_ass\_item (C member), 151

PySequenceMethods.sq\_concat (C member), 150

PySequenceMethods.sq\_contains (C member), 151

PySequenceMethods.sq\_inplace\_concat (C

PySequenceMethods.sq\_inplace\_repeat (C member), 151

PySequenceMethods.sq\_item (C member), 150

PySequenceMethods.sq\_length (C member), 150

PySequenceMethods.sq\_repeat (C member), 150

PySet\_Add (C function), 109

PySet\_Check (C function), 108

PySet\_Clear (C function), 109

PySet\_Contains (C function), 109

PySet\_Discard (C function), 109

PySet\_GET\_SIZE (C function), 109

PySet\_New (C function), 108

PySet\_Pop (C function), 109

<!-- page: 198 -->

PySet\_Size (C function), 108 PySet\_Type (C variable), 108 PySetObject (C type), 108 PySignal\_SetWakeupFd (C function), 20 PySlice\_Check (C function), 100 PySlice\_GetIndices (C function), 100 PySlice\_GetIndicesEx (C function), 100 PySlice\_New (C function), 100 PySlice\_Type (C variable), 100 PyString\_AS\_STRING (C function), 68 PyString\_AsDecodedObject (C function), 69 PyString\_AsEncodedObject (C function), 70 PyString\_AsString (C function), 68 PyString\_AsStringAndSize (C function), 68 PyString\_Check (C function), 66 PyString\_CheckExact (C function), 66 PyString\_Concat (C function), 68 PyString\_ConcatAndDel (C function), 68 PyString\_Decode (C function), 69 PyString\_Encode (C function), 69 PyString\_Format (C function), 69 PyString\_FromFormat (C function), 67 PyString\_FromFormatV (C function), 68 PyString\_FromString (C function), 67 PyString\_FromString(), 92 PyString\_FromStringAndSize (C function), 67 PyString\_GET\_SIZE (C function), 68 PyString\_InternFromString (C function), 69 PyString\_InternInPlace (C function), 69 PyString\_Size (C function), 68 PyString\_Type (C variable), 66 PyStringObject (C type), 66 PySys\_AddWarnOption (C function), 26 PySys\_GetFile (C function), 25 PySys\_GetObject (C function), 25 PySys\_ResetWarnOptions (C function), 26 PySys\_SetArgv (C function), 114 PySys\_SetArgv(), 111 PySys\_SetArgvEx (C function), 113 PySys\_SetArgvEx(), 9, 111 PySys\_SetObject (C function), 26 PySys\_SetPath (C function), 26 PySys\_WriteStderr (C function), 26 PySys\_WriteStdout (C function), 26 Python 3000, **161** Python Enhancement Proposals PEP 1, 161 PEP 238, 14, 157 PEP 278, 162 PEP 302, 157, 160 PEP 343, 156 PEP 3116, 162 PYTHONDUMPREFS, 136 PYTHONHOME, 9, 114

Pythonic, **161** PYTHONPATH, 9 PYTHONSHOWALLOCCOUNT, 148 PyThreadState, 114 PyThreadState (C type), 116 PyThreadState\_Clear (C function), 118 PyThreadState\_Delete (C function), 118 PyThreadState\_Get (C function), 117 PyThreadState\_GetDict (C function), 118 PyThreadState\_New (C function), 118 PyThreadState\_Next (C function), 123 PyThreadState\_SetAsyncExc (C function), 118 PyThreadState\_Swap (C function), 117 PyTime\_Check (C function), 105 PyTime\_CheckExact (C function), 105 PyTime\_FromTime (C function), 106 PyTrace\_C\_CALL (C variable), 121 PyTrace\_C\_EXCEPTION (C variable), 122 PyTrace\_C\_RETURN (C variable), 122 PyTrace\_CALL (C variable), 121 PyTrace\_EXCEPTION (C variable), 121 PyTrace\_LINE (C variable), 121 PyTrace\_RETURN (C variable), 121 PyTuple\_Check (C function), 87 PyTuple\_CheckExact (C function), 88 PyTuple\_ClearFreeList (C function), 89 PyTuple\_GET\_ITEM (C function), 88 PyTuple\_GET\_SIZE (C function), 88 PyTuple\_GetItem (C function), 88 PyTuple\_GetSlice (C function), 88 PyTuple\_New (C function), 88 PyTuple\_Pack (C function), 88 PyTuple\_SET\_ITEM (C function), 89 PyTuple\_SetItem (C function), 88 PyTuple\_SetItem(), 5 PyTuple\_Size (C function), 88 PyTuple\_Type (C variable), 87 PyTupleObject (C type), 87 PyType\_Check (C function), 57 PyType\_CheckExact (C function), 57 PyType\_ClearCache (C function), 57 PyType\_GenericAlloc (C function), 58 PyType\_GenericNew (C function), 58 PyType\_HasFeature (C function), 57 PyType\_HasFeature(), 151 PyType\_IS\_GC (C function), 58 PyType\_IsSubtype (C function), 58 PyType\_Modified (C function), 57 PyType\_Ready (C function), 58 PyType\_Type (C variable), 57 PyTypeObject (C type), 57 PyTypeObject.tp\_alloc (C member), 146 PyTypeObject.tp\_allocs (C member), 148 PyTypeObject.tp\_as\_buffer (C member), 140

<!-- page: 199 -->

PyTypeObject.tp\_base (C member), 145

PyTypeObject.tp\_bases (C member), 148

PyTypeObject.tp\_basicsize (C member), 137

PyTypeObject.tp\_cache (C member), 148

PyTypeObject.tp\_call (C member), 139

PyTypeObject.tp\_clear (C member), 142

PyTypeObject.tp\_compare (C member), 138

PyTypeObject.tp\_dealloc (C member), 137

PyTypeObject.tp\_descr\_get (C member), 145

PyTypeObject.tp\_descr\_set (C member), 145

PyTypeObject.tp\_dict (C member), 145

PyTypeObject.tp\_dictoffset (C member), 145

PyTypeObject.tp\_doc (C member), 142

PyTypeObject.tp\_free (C member), 147

PyTypeObject.tp\_frees (C member), 148

PyTypeObject.tp\_getattro (C member), 140

PyTypeObject.tp\_getset (C member), 145

PyTypeObject.tp\_hash (C member), 139

PyTypeObject.tp\_init (C member), 146

PyTypeObject.tp\_itemsize (C member), 137

PyTypeObject.tp\_iter (C member), 144

PyTypeObject.tp\_iternext (C member), 144

PyTypeObject.tp\_maxalloc (C member), 148

PyTypeObject.tp\_members (C member), 145

PyTypeObject.tp\_methods (C member), 144

PyTypeObject.tp\_mro (C member), 148

PyTypeObject.tp\_name (C member), 137

PyTypeObject.tp\_new (C member), 147

PyTypeObject.tp\_next (C member), 148

PyTypeObject.tp\_print (C member), 138

PyTypeObject.tp\_repr (C member), 139

PyTypeObject.tp\_richcompare (C member), 143

PyTypeObject.tp\_setattr (C member), 138

PyTypeObject.tp\_setattro (C member), 140

PyTypeObject.tp\_str (C member), 140

PyTypeObject.tp\_subclasses (C member), 148

PyTypeObject.tp\_traverse (C member), 142

PyTypeObject.tp\_weaklist (C member), 148

PyTypeObject.tp\_weaklistoffset (C member), 144

PyTZInfo\_Check (C function), 106

PyTZInfo\_CheckExact (C function), 106

PyUnicode\_AS\_DATA (C function), 71

PyUnicode\_AS\_UNICODE (C function), 71

PyUnicode\_AsASCIIString (C function), 79

PyUnicode\_AsCharmapString (C function), 80

PyUnicode\_AsEncodedString (C function), 75

PyUnicode\_AsLatin1String (C function), 79

PyUnicode\_AsMBCSString (C function), 81

PyUnicode\_AsRawUnicodeEscapeString C function), 79

PyUnicode\_AsUnicode (C function), 73

PyUnicode\_AsUnicodeEscapeString (C function), 78

PyUnicode\_AsUTF8String (C function), 75

PyUnicode\_AsUTF16String (C function), 77

PyUnicode\_AsUTF32String (C function), 76

PyUnicode\_AsWideChar (C function), 74

PyUnicode\_Check (C function), 70

PyUnicode\_CheckExact (C function), 70

PyUnicode\_ClearFreeList (C function), 71

PyUnicode\_Compare (C function), 82

PyUnicode\_Concat (C function), 81

PyUnicode\_Contains (C function), 82

PyUnicode\_Count (C function), 82

PyUnicode\_Decode (C function), 74

PyUnicode\_DecodeASCII (C function), 79

PyUnicode\_DecodeCharmap (C function), 80

PyUnicode\_DecodeLatin1 (C function), 79

PyUnicode\_DecodeMBCS (C function), 81

PyUnicode\_DecodeMBCSStateful (C function), 81

PyUnicode\_DecodeRawUnicodeEscape (C function), 78

PyUnicode\_DecodeUnicodeEscape (C function), 78

PyUnicode\_DecodeUTF7 (C function), 78

PyUnicode\_DecodeUTF7Stateful (C function), 78

PyUnicode\_DecodeUTF8 (C function), 75

PyUnicode\_DecodeUTF8Stateful (C function), 75

PyUnicode\_DecodeUTF16 (C function), 77

PyUnicode\_DecodeUTF16Stateful (C function), 77

PyUnicode\_DecodeUTF32 (C function), 76

PyUnicode\_DecodeUTF32Stateful (C function),

PyUnicode\_Encode (C function), 75

PyUnicode\_EncodeASCII (C function), 79

PyUnicode\_EncodeCharmap (C function), 80

PyUnicode\_EncodeLatin1 (C function), 79

PyUnicode\_EncodeMBCS (C function), 81

PyUnicode\_EncodeRawUnicodeEscape (C function), 78

PyUnicode\_EncodeUnicodeEscape (C function), 78

PyUnicode\_EncodeUTF7 (C function), 78

PyUnicode\_EncodeUTF8 (C function), 75

PyUnicode\_EncodeUTF16 (C function), 77

PyUnicode\_EncodeUTF32 (C function), 76

PyUnicode\_Find (C function), 82

PyUnicode\_Format (C function), 82

( PyUnicode\_FromEncodedObject (C function), 73

PyUnicode\_FromFormat (C function), 72

<!-- page: 200 -->

PyUnicode\_FromFormatV (C function), 73 PyUnicode\_FromObject (C function), 73 PyUnicode\_FromString (C function), 72 PyUnicode\_FromStringAndSize (C function), 72 PyUnicode\_FromUnicode (C function), 72 PyUnicode\_FromWideChar (C function), 74 PyUnicode\_GET\_DATA\_SIZE (C function), 71 PyUnicode\_GET\_SIZE (C function), 70 PyUnicode\_GetSize (C function), 73 PyUnicode\_Join (C function), 82 PyUnicode\_Replace (C function), 82 PyUnicode\_RichCompare (C function), 82 PyUnicode\_Split (C function), 81 PyUnicode\_Splitlines (C function), 81 PyUnicode\_Tailmatch (C function), 82 PyUnicode\_Translate (C function), 81 PyUnicode\_TranslateCharmap (C function), 80 PyUnicode\_Type (C variable), 70 PyUnicodeDecodeError\_Create (C function), 21 PyUnicodeDecodeError\_GetEncoding (C function), 21 PyUnicodeDecodeError\_GetEnd (C function), 22 PyUnicodeDecodeError\_GetObject (C function), 21 PyUnicodeDecodeError\_GetReason (C function), 22 PyUnicodeDecodeError\_GetStart (C function), 21 PyUnicodeDecodeError\_SetEnd (C function), 22 PyUnicodeDecodeError\_SetReason (C function), 22 PyUnicodeDecodeError\_SetStart (C function), 21 PyUnicodeEncodeError\_Create (C function), 21 PyUnicodeEncodeError\_GetEncoding (C function), 21 PyUnicodeEncodeError\_GetEnd (C function), 22 PyUnicodeEncodeError\_GetObject (C function), 21 PyUnicodeEncodeError\_GetReason (C function), 22 PyUnicodeEncodeError\_GetStart (C function), 21 PyUnicodeEncodeError\_SetEnd (C function), 22 PyUnicodeEncodeError\_SetReason (C function), 22 PyUnicodeEncodeError\_SetStart (C function), 21 PyUnicodeObject (C type), 70 PyUnicodeTranslateError\_Create (C function), 21 PyUnicodeTranslateError\_GetEnd (C function), 22

PyUnicodeTranslateError\_GetObject (C function), 21 PyUnicodeTranslateError\_GetReason (C function), 22 PyUnicodeTranslateError\_GetStart (C function), 21 PyUnicodeTranslateError\_SetEnd (C function), 22 PyUnicodeTranslateError\_SetReason (C function), 22 PyUnicodeTranslateError\_SetStart (C function), 21 PyVarObject (C type), 130 PyVarObject\_HEAD\_INIT (C macro), 131 PyVarObject.ob\_size (C member), 137 PyWeakref\_Check (C function), 101 PyWeakref\_CheckProxy (C function), 101 PyWeakref\_CheckRef (C function), 101 PyWeakref\_GET\_OBJECT (C function), 101 PyWeakref\_GetObject (C function), 101 PyWeakref\_NewProxy (C function), 101 PyWeakref\_NewRef (C function), 101 PyWrapper\_New (C function), 100

## R

readbufferproc (C type), 152 realloc(), 125 reference count, **162** reload built-in function, 28 repr built-in function, 44, 139 rexec module, 27

## S

search path, module, 9, 111, 112 segcountproc (C type), 152 sequence, **162** object, 65 set object, 108 set\_all(), 6 setcheckinterval() (in module sys), 114 setvbuf(), 97 SIGINT, 20 signal module, 20 slice, **162** SliceType (in module types), 100 softspace (file attribute), 97 special method, 162

<!-- page: 201 -->

special method, **162** statement, **162** staticmethod built-in function, 133 stderr (in module sys), 119 stdin (in module sys), 119 stdout (in module sys), 119 str built-in function, 44 strerror(), 19 string object, 66 StringType (in module types), 66 struct sequence, **162** sum\_list(), 6 sum\_sequence(), 7, 8 sys module, 9, 111, 119 SystemError (built-in exception), 98

## T

thread module, 116 tp\_as\_mapping (C member), 139 tp\_as\_number (C member), 139 tp\_as\_sequence (C member), 139 traverseproc (C type), 153 triple-quoted string, **162** tuple built-in function, 52, 91 object, 87 TupleType (in module types), 87 type, **162** built-in function, 46 object, 4, 57 TypeType (in module types), 57

ULONG\_MAX, 62 unicode built-in function, 45 universal newlines, **162**

version (in module sys), 113 virtual environment, **162** virtual machine, **162** visitproc (C type), 153

## W

writebufferproc (C type), 152

## Z

Zen of Python, **162**

## Index

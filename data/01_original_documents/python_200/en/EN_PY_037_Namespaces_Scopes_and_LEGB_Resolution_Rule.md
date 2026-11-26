<!-- page: 1 -->
# EN_PY_037: Python Scopes and Namespaces: The LEGB Rule and global/nonlocal Statements

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

9.1. A Word About Names and Objects
===================================

Objects have individuality, and multiple names (in multiple scopes)
can be bound to the same object.  This is known as aliasing in other
languages.  This is usually not appreciated on a first glance at
Python, and can be safely ignored when dealing with immutable basic
types (numbers, strings, tuples).  However, aliasing has a possibly
surprising effect on the semantics of Python code involving mutable
objects such as lists, dictionaries, and most other types. This is
usually used to the benefit of the program, since aliases behave like
pointers in some respects.  For example, passing an object is cheap
since only a pointer is passed by the implementation; and if a
function modifies an object passed as an argument, the caller will see
the change — this eliminates the need for two different argument
passing mechanisms as in Pascal.


9.2. Python Scopes and Namespaces
=================================

Before introducing classes, I first have to tell you something about
Python’s scope rules.  Class definitions play some neat tricks with
namespaces, and you need to know how scopes and namespaces work to
fully understand what’s going on. Incidentally, knowledge about this
subject is useful for any advanced Python programmer.

Let’s begin with some definitions.

A *namespace* is a mapping from names to objects.  Most namespaces are
currently implemented as Python dictionaries, but that’s normally not
noticeable in any way (except for performance), and it may change in
the future.  Examples of namespaces are: the set of built-in names
(containing functions such as "abs()", and built-in exception names);

<!-- page: 2 -->

the global names in a module; and the local names in a function
invocation.  In a sense the set of attributes of an object also form a
namespace.  The important thing to know about namespaces is that there
is absolutely no relation between names in different namespaces; for
instance, two different modules may both define a function "maximize"
without confusion — users of the modules must prefix it with the
module name.

By the way, I use the word *attribute* for any name following a dot —
for example, in the expression "z.real", "real" is an attribute of the
object "z".  Strictly speaking, references to names in modules are
attribute references: in the expression "modname.funcname", "modname"
is a module object and "funcname" is an attribute of it.  In this case
there happens to be a straightforward mapping between the module’s
attributes and the global names defined in the module: they share the
same namespace!  [1]

Attributes may be read-only or writable.  In the latter case,
assignment to attributes is possible.  Module attributes are writable:
you can write "modname.the_answer = 42".  Writable attributes may also
be deleted with the "del" statement.  For example, "del
modname.the_answer" will remove the attribute "the_answer" from the
object named by "modname".

Namespaces are created at different moments and have different
lifetimes.  The namespace containing the built-in names is created
when the Python interpreter starts up, and is never deleted.  The
global namespace for a module is created when the module definition is
read in; normally, module namespaces also last until the interpreter
quits.  The statements executed by the top-level invocation of the
interpreter, either read from a script file or interactively, are
considered part of a module called "__main__", so they have their own
global namespace.  (The built-in names actually also live in a module;
this is called "builtins".)

The local namespace for a function is created when the function is
called, and deleted when the function returns or raises an exception
that is not handled within the function.  (Actually, forgetting would
be a better way to describe what actually happens.)  Of course,
recursive invocations each have their own local namespace.

A *scope* is a textual region of a Python program where a namespace is
directly accessible.  “Directly accessible” here means that an
unqualified reference to a name attempts to find the name in the
namespace.

<!-- page: 3 -->


Although scopes are determined statically, they are used dynamically.
At any time during execution, there are 3 or 4 nested scopes whose
namespaces are directly accessible:

* the innermost scope, which is searched first, contains the local
  names

* the scopes of any enclosing functions, which are searched starting
  with the nearest enclosing scope, contain non-local, but also non-
  global names

* the next-to-last scope contains the current module’s global names

* the outermost scope (searched last) is the namespace containing
  built-in names

If a name is declared global, then all references and assignments go
directly to the next-to-last scope containing the module’s global
names.  To rebind variables found outside of the innermost scope, the
"nonlocal" statement can be used; if not declared nonlocal, those
variables are read-only (an attempt to write to such a variable will
simply create a *new* local variable in the innermost scope, leaving
the identically named outer variable unchanged).

Usually, the local scope references the local names of the (textually)
current function.  Outside functions, the local scope references the
same namespace as the global scope: the module’s namespace. Class
definitions place yet another namespace in the local scope.

It is important to realize that scopes are determined textually: the
global scope of a function defined in a module is that module’s
namespace, no matter from where or by what alias the function is
called.  On the other hand, the actual search for names is done
dynamically, at run time — however, the language definition is
evolving towards static name resolution, at “compile” time, so don’t
rely on dynamic name resolution!  (In fact, local variables are
already determined statically.)

A special quirk of Python is that – if no "global" or "nonlocal"
statement is in effect – assignments to names always go into the
innermost scope. Assignments do not copy data — they just bind names
to objects.  The same is true for deletions: the statement "del x"
removes the binding of "x" from the namespace referenced by the local
scope.  In fact, all operations that introduce new names use the local

<!-- page: 4 -->

scope: in particular, "import" statements and function definitions
bind the module or function name in the local scope.

The "global" statement can be used to indicate that particular
variables live in the global scope and should be rebound there; the
"nonlocal" statement indicates that particular variables live in an
enclosing scope and should be rebound there.


9.2.1. Scopes and Namespaces Example
------------------------------------

This is an example demonstrating how to reference the different scopes
and namespaces, and how "global" and "nonlocal" affect variable
binding:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

```
The output of the example code is:

   After local assignment: test spam
   After nonlocal assignment: nonlocal spam

<!-- page: 5 -->

   After global assignment: nonlocal spam
   In global scope: global spam

Note how the *local* assignment (which is default) didn’t change
*scope_test*'s binding of *spam*.  The "nonlocal" assignment changed
*scope_test*'s binding of *spam*, and the "global" assignment changed
the module-level binding.

You can also see that there was no previous binding for *spam* before
the "global" assignment.

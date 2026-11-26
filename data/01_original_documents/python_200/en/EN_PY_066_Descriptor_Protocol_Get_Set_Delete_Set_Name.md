<!-- page: 1 -->
# EN_PY_066: Implementing Descriptors: The Descriptor Protocol (__get__, __set__, __delete__)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Advanced OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification


codeobject.co_lines()

   Returns an iterator that yields information about successive ranges
   of *bytecode*s. Each item yielded is a "(start, end, lineno)"
   "tuple":

   * "start" (an "int") represents the offset (inclusive) of the start
     of the *bytecode* range

   * "end" (an "int") represents the offset (exclusive) of the end of
     the *bytecode* range

   * "lineno" is an "int" representing the line number of the
```python
  *bytecode* range, or "None" if the bytecodes in the given range
  have no line number

The items yielded will have the following properties:

* The first range yielded will have a "start" of 0.

* The "(start, end)" ranges will be non-decreasing and consecutive.
  That is, for any pair of "tuple"s, the "start" of the second will
  be equal to the "end" of the first.

* No range will be backwards: "end >= start" for all triples.

* The last "tuple" yielded will have "end" equal to the size of the
  *bytecode*.

Zero-width ranges, where "start == end", are allowed. Zero-width
ranges are used for lines that are present in the source code, but
have been eliminated by the *bytecode* compiler.

Added in version 3.10.

See also:

  **PEP 626** - Precise line numbers for debugging and other tools.
     The PEP that introduced the "co_lines()" method.

```

<!-- page: 2 -->

codeobject.replace(**kwargs)

```python
Return a copy of the code object with new values for the specified
fields.

Added in version 3.8.


```
3.2.13.2. Frame objects
~~~~~~~~~~~~~~~~~~~~~~~

Frame objects represent execution frames.  They may occur in traceback
objects, and are also passed to registered trace functions.


3.2.13.2.1. Special read-only attributes
""""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| frame.f_back                                       | Points to the previous stack frame (towards the    |
|                                                    | caller), or "None" if this is the bottom stack     |
|                                                    | frame                                              |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_code                                       | The code object being executed in this frame.      |
|                                                    | Accessing this attribute raises an auditing event  |
|                                                    | "object.__getattr__" with arguments "obj" and      |
|                                                    | ""f_code"".                                        |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_locals                                     | The dictionary used by the frame to look up local  |
|                                                    | variables                                          |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_globals                                    | The dictionary used by the frame to look up global |
|                                                    | variables                                          |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_builtins                                   | The dictionary used by the frame to look up built- |
|                                                    | in (intrinsic) names                               |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_lasti                                      | The “precise instruction” of the frame object      |
|                                                    | (this is an index into the *bytecode* string of    |
|                                                    | the code object)                                   |
+----------------------------------------------------+----------------------------------------------------+



<!-- page: 3 -->

3.2.13.2.2. Special writable attributes
"""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| frame.f_trace                                      | If not "None", this is a function called for       |
|                                                    | various events during code execution (this is used |
|                                                    | by debuggers). Normally an event is triggered for  |
|                                                    | each new source line (see "f_trace_lines").        |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_trace_lines                                | Set this attribute to "False" to disable           |
|                                                    | triggering a tracing event for each source line.   |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_trace_opcodes                              | Set this attribute to "True" to allow per-opcode   |
|                                                    | events to be requested. Note that this may lead to |
|                                                    | undefined interpreter behaviour if exceptions      |
|                                                    | raised by the trace function escape to the         |
|                                                    | function being traced.                             |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_lineno                                     | The current line number of the frame – writing to  |
|                                                    | this from within a trace function jumps to the     |
|                                                    | given line (only for the bottom-most frame).  A    |
|                                                    | debugger can implement a Jump command (aka Set     |
|                                                    | Next Statement) by writing to this attribute.      |
+----------------------------------------------------+----------------------------------------------------+


3.2.13.2.3. Frame object methods
""""""""""""""""""""""""""""""""

Frame objects support one method:

frame.clear()

   This method clears all references to local variables held by the
```python
frame.  Also, if the frame belonged to a *generator*, the generator
is finalized.  This helps break reference cycles involving frame
objects (for example when catching an exception and storing its
traceback for later use).

"RuntimeError" is raised if the frame is currently executing.

Added in version 3.4.


```

<!-- page: 4 -->

3.2.13.3. Traceback objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Traceback objects represent the stack trace of an exception. A
traceback object is implicitly created when an exception occurs, and
may also be explicitly created by calling "types.TracebackType".

Changed in version 3.7: Traceback objects can now be explicitly
instantiated from Python code.

For implicitly created tracebacks, when the search for an exception
handler unwinds the execution stack, at each unwound level a traceback
object is inserted in front of the current traceback.  When an
exception handler is entered, the stack trace is made available to the
program. (See section The try statement.) It is accessible as the
third item of the tuple returned by "sys.exc_info()", and as the
"__traceback__" attribute of the caught exception.

When the program contains no suitable handler, the stack trace is
written (nicely formatted) to the standard error stream; if the
interpreter is interactive, it is also made available to the user as
"sys.last_traceback".

For explicitly created tracebacks, it is up to the creator of the
traceback to determine how the "tb_next" attributes should be linked
to form a full stack trace.

Special read-only attributes:

+----------------------------------------------------+----------------------------------------------------+
| traceback.tb_frame                                 | Points to the execution frame of the current       |
|                                                    | level.  Accessing this attribute raises an         |
|                                                    | auditing event "object.__getattr__" with arguments |
|                                                    | "obj" and ""tb_frame"".                            |
+----------------------------------------------------+----------------------------------------------------+
| traceback.tb_lineno                                | Gives the line number where the exception occurred |
+----------------------------------------------------+----------------------------------------------------+
| traceback.tb_lasti                                 | Indicates the “precise instruction”.               |
+----------------------------------------------------+----------------------------------------------------+

The line number and last instruction in the traceback may differ from
the line number of its frame object if the exception occurred in a
"try" statement with no matching except clause or with a "finally"
clause.


<!-- page: 5 -->

traceback.tb_next

   The special writable attribute "tb_next" is the next level in the
   stack trace (towards the frame where the exception occurred), or
```python
"None" if there is no next level.

Changed in version 3.7: This attribute is now writable


```
3.2.13.4. Slice objects
~~~~~~~~~~~~~~~~~~~~~~~

Slice objects are used to represent slices for "__getitem__()"
methods.  They are also created by the built-in "slice()" function.

Special read-only attributes: "start" is the lower bound; "stop" is
the upper bound; "step" is the step value; each is "None" if omitted.
These attributes can have any type.

Slice objects support one method:

slice.indices(self, length)

   This method takes a single integer argument *length* and computes
   information about the slice that the slice object would describe if
   applied to a sequence of *length* items.  It returns a tuple of
   three integers; respectively these are the *start* and *stop*
   indices and the *step* or stride length of the slice. Missing or
   out-of-bounds indices are handled in a manner consistent with
   regular slices.


3.2.13.5. Static method objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Static method objects provide a way of defeating the transformation of
function objects to method objects described above. A static method
object is a wrapper around any other object, usually a user-defined
method object. When a static method object is retrieved from a class
or a class instance, the object actually returned is the wrapped
object, which is not subject to any further transformation. Static
method objects are also callable. Static method objects are created by
the built-in "staticmethod()" constructor.

<!-- page: 6 -->



3.2.13.6. Class method objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A class method object, like a static method object, is a wrapper
around another object that alters the way in which that object is
retrieved from classes and class instances. The behaviour of class
method objects upon such retrieval is described above, under “instance
methods”. Class method objects are created by the built-in
"classmethod()" constructor.


3.3. Special method names
=========================

A class can implement certain operations that are invoked by special
syntax (such as arithmetic operations or subscripting and slicing) by
defining methods with special names. This is Python’s approach to
*operator overloading*, allowing classes to define their own behavior
with respect to language operators.  For instance, if a class defines
a method named "__getitem__()", and "x" is an instance of this class,
then "x[i]" is roughly equivalent to "type(x).__getitem__(x, i)".
Except where mentioned, attempts to execute an operation raise an
exception when no appropriate method is defined (typically
"AttributeError" or "TypeError").

Setting a special method to "None" indicates that the corresponding
operation is not available.  For example, if a class sets "__iter__()"
to "None", the class is not iterable, so calling "iter()" on its
instances will raise a "TypeError" (without falling back to
"__getitem__()"). [2]

When implementing a class that emulates any built-in type, it is
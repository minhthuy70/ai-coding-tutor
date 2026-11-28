# EN_PY_074: Yield Expressions, yield from Delegations, and Coroutine Suspension

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Generators | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

A generator expression yields a new generator object.  Its syntax is
the same as for comprehensions, except that it is enclosed in
parentheses instead of brackets or curly braces.

Variables used in the generator expression are evaluated lazily when
the "__next__()" method is called for the generator object (in the
same fashion as normal generators).  However, the iterable expression
in the leftmost "for" clause is immediately evaluated, so that an
error produced by it will be emitted at the point where the generator
expression is defined, rather than at the point where the first value
is retrieved. Subsequent "for" clauses and any filter condition in the
leftmost "for" clause cannot be evaluated in the enclosing scope as
they may depend on the values obtained from the leftmost iterable. For
example: "(x*y for x in range(10) for y in range(x, x+10))".

The parentheses can be omitted on calls with only one argument.  See
section Calls for details.

To avoid interfering with the expected operation of the generator
expression itself, "yield" and "yield from" expressions are prohibited
in the implicitly defined generator.

If a generator expression contains either "async for" clauses or
"await" expressions it is called an *asynchronous generator
expression*.  An asynchronous generator expression returns a new
asynchronous generator object, which is an asynchronous iterator (see
Asynchronous Iterators).

Added in version 3.6: Asynchronous generator expressions were
introduced.

Changed in version 3.7: Prior to Python 3.7, asynchronous generator
expressions could only appear in "async def" coroutines.  Starting

with 3.7, any function can use asynchronous generator expressions.

Changed in version 3.8: "yield" and "yield from" prohibited in the
implicitly nested scope.

6.2.9. Yield expressions
------------------------

   yield_atom       ::= "(" yield_expression ")"

```python
yield_from       ::= "yield" "from" expression
yield_expression ::= "yield" yield_list | yield_from

```

The yield expression is used when defining a *generator* function or
an *asynchronous generator* function and thus can only be used in the
body of a function definition.  Using a yield expression in a
function’s body causes that function to be a generator function, and
using it in an "async def" function’s body causes that coroutine
function to be an asynchronous generator function. For example:

```python
def gen():  # defines a generator function
    yield 123

async def agen(): # defines an asynchronous generator function
    yield 123

```

Due to their side effects on the containing scope, "yield" expressions
are not permitted as part of the implicitly defined scopes used to
implement comprehensions and generator expressions.

Changed in version 3.8: Yield expressions prohibited in the implicitly
nested scopes used to implement comprehensions and generator
expressions.

Generator functions are described below, while asynchronous generator
functions are described separately in section Asynchronous generator
functions.

When a generator function is called, it returns an iterator known as a
generator.  That generator then controls the execution of the
generator function.  The execution starts when one of the generator’s

methods is called. At that time, the execution proceeds to the first
yield expression, where it is suspended again, returning the value of
"yield_list" to the generator’s caller, or "None" if "yield_list" is
omitted. By suspended, we mean that all local state is retained,
including the current bindings of local variables, the instruction
pointer, the internal evaluation stack, and the state of any exception
handling. When the execution is resumed by calling one of the
generator’s methods, the function can proceed exactly as if the yield
expression were just another external call.  The value of the yield
expression after resuming depends on the method which resumed the
execution.  If "__next__()" is used (typically via either a "for" or
the "next()" builtin) then the result is "None".  Otherwise, if
"send()" is used, then the result will be the value passed in to that
method.

All of this makes generator functions quite similar to coroutines;
they yield multiple times, they have more than one entry point and
their execution can be suspended.  The only difference is that a
generator function cannot control where the execution should continue
after it yields; the control is always transferred to the generator’s
caller.

Yield expressions are allowed anywhere in a "try" construct.  If the
generator is not resumed before it is finalized (by reaching a zero
reference count or by being garbage collected), the generator-
iterator’s "close()" method will be called, allowing any pending
"finally" clauses to execute.

When "yield from <expr>" is used, the supplied expression must be an
iterable. The values produced by iterating that iterable are passed
directly to the caller of the current generator’s methods. Any values
passed in with "send()" and any exceptions passed in with "throw()"
are passed to the underlying iterator if it has the appropriate
methods.  If this is not the case, then "send()" will raise
"AttributeError" or "TypeError", while "throw()" will just raise the
passed in exception immediately.

When the underlying iterator is complete, the "value" attribute of the
raised "StopIteration" instance becomes the value of the yield
expression. It can be either set explicitly when raising
"StopIteration", or automatically when the subiterator is a generator
(by returning a value from the subgenerator).

Changed in version 3.3: Added "yield from <expr>" to delegate control
flow to a subiterator.

The parentheses may be omitted when the yield expression is the sole
expression on the right hand side of an assignment statement.

See also:

  **PEP 255** - Simple Generators

```python
The proposal for adding generators and the "yield" statement to
Python.

```

  **PEP 342** - Coroutines via Enhanced Generators
     The proposal to enhance the API and syntax of generators, making
     them usable as simple coroutines.

  **PEP 380** - Syntax for Delegating to a Subgenerator
     The proposal to introduce the "yield_from" syntax, making
     delegation to subgenerators easy.

  **PEP 525** - Asynchronous Generators
     The proposal that expanded on **PEP 492** by adding generator
     capabilities to coroutine functions.

6.2.9.1. Generator-iterator methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This subsection describes the methods of a generator iterator.  They
can be used to control the execution of a generator function.

Note that calling any of the generator methods below when the
generator is already executing raises a "ValueError" exception.

generator.__next__()

   Starts the execution of a generator function or resumes it at the

```python
last executed yield expression.  When a generator function is
resumed with a "__next__()" method, the current yield expression
always evaluates to "None".  The execution then continues to the
next yield expression, where the generator is suspended again, and
the value of the "yield_list" is returned to "__next__()"’s caller.
If the generator exits without yielding another value, a
"StopIteration" exception is raised.

This method is normally called implicitly, e.g. by a "for" loop, or
by the built-in "next()" function.

```

generator.send(value)

   Resumes the execution and “sends” a value into the generator
   function.  The *value* argument becomes the result of the current

```python
yield expression.  The "send()" method returns the next value
yielded by the generator, or raises "StopIteration" if the
generator exits without yielding another value.  When "send()" is
called to start the generator, it must be called with "None" as the
argument, because there is no yield expression that could receive
the value.

```

generator.throw(value)
generator.throw(type[, value[, traceback]])

   Raises an exception at the point where the generator was paused,
   and returns the next value yielded by the generator function.  If
   the generator exits without yielding another value, a
   "StopIteration" exception is raised.  If the generator function
   does not catch the passed-in exception, or raises a different
   exception, then that exception propagates to the caller.

```python
In typical use, this is called with a single exception instance
similar to the way the "raise" keyword is used.

For backwards compatibility, however, the second signature is
supported, following a convention from older versions of Python.
The *type* argument should be an exception class, and *value*
should be an exception instance. If the *value* is not provided,
the *type* constructor is called to get an instance. If *traceback*
is provided, it is set on the exception, otherwise any existing
"__traceback__" attribute stored in *value* may be cleared.

Changed in version 3.12: The second signature (type[, value[,
traceback]]) is deprecated and may be removed in a future version
of Python.

```

generator.close()

   Raises a "GeneratorExit" at the point where the generator function
   was paused.  If the generator function then exits gracefully, is
   already closed, or raises "GeneratorExit" (by not catching the

   exception), close returns to its caller.  If the generator yields a
   value, a "RuntimeError" is raised.  If the generator raises any
   other exception, it is propagated to the caller.  "close()" does

```python
nothing if the generator has already exited due to an exception or
normal exit.

```

6.2.9.2. Examples
~~~~~~~~~~~~~~~~~

Here is a simple example that demonstrates the behavior of generators
and generator functions:

```python
>>> def echo(value=None):
...     print("Execution starts when 'next()' is called for the first time.")
...     try:
...         while True:
...             try:
...                 value = (yield value)
...             except Exception as e:
...                 value = e
...     finally:
...         print("Don't forget to clean up when 'close()' is called.")
>>> generator = echo(1)
>>> print(next(generator))
Execution starts when 'next()' is called for the first time.
1
>>> print(next(generator))
None
>>> print(generator.send(2))
2
>>> generator.throw(TypeError, "spam")
TypeError('spam',)
>>> generator.close()
Don't forget to clean up when 'close()' is called.

```

For examples using "yield from", see PEP 380: Syntax for Delegating to
a Subgenerator in “What’s New in Python.”

6.2.9.3. Asynchronous generator functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The presence of a yield expression in a function or method defined
using "async def" further defines the function as an *asynchronous
generator* function.

When an asynchronous generator function is called, it returns an
asynchronous iterator known as an asynchronous generator object. That
object then controls the execution of the generator function. An
asynchronous generator object is typically used in an "async for"
statement in a coroutine function analogously to how a generator
object would be used in a "for" statement.

Calling one of the asynchronous generator’s methods returns an
*awaitable* object, and the execution starts when this object is
awaited on. At that time, the execution proceeds to the first yield
expression, where it is suspended again, returning the value of
"yield_list" to the awaiting coroutine. As with a generator,
suspension means that all local state is retained, including the
current bindings of local variables, the instruction pointer, the
internal evaluation stack, and the state of any exception handling.
When the execution is resumed by awaiting on the next object returned
by the asynchronous generator’s methods, the function can proceed
exactly as if the yield expression were just another external call.
The value of the yield expression after resuming depends on the method
which resumed the execution.  If "__anext__()" is used then the result
is "None". Otherwise, if "asend()" is used, then the result will be
the value passed in to that method.

If an asynchronous generator happens to exit early by "break", the
caller task being cancelled, or other exceptions, the generator’s
async cleanup code will run and possibly raise exceptions or access
context variables in an unexpected context–perhaps after the lifetime
of tasks it depends, or during the event loop shutdown when the async-
generator garbage collection hook is called. To prevent this, the
caller must explicitly close the async generator by calling "aclose()"
method to finalize the generator and ultimately detach it from the
event loop.

In an asynchronous generator function, yield expressions are allowed
anywhere in a "try" construct. However, if an asynchronous generator
is not resumed before it is finalized (by reaching a zero reference
count or by being garbage collected), then a yield expression within a
"try" construct could result in a failure to execute pending "finally"

clauses.  In this case, it is the responsibility of the event loop or
scheduler running the asynchronous generator to call the asynchronous
generator-iterator’s "aclose()" method and run the resulting coroutine
object, thus allowing any pending "finally" clauses to execute.

To take care of finalization upon event loop termination, an event
loop should define a *finalizer* function which takes an asynchronous
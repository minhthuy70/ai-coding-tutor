# Official Python Documentation: Built-in Functions and Standard Types

## Built-in functions

The Python interpreter has a number of functions and types built into it that
are always available.  They are listed here in alphabetical order.

+---------------------------------------------------------------------------------------------------+
|                                        Built-in Functions                                         |
+=========================+=======================+=======================+=========================+
| |  **A**                | |  **E**              | |  **L**              | |  **R**                |
| |  `abs()`          | |  `enumerate()`  | |  `len()`        | |  |func-range|_        |
| |  `aiter()`        | |  `eval()`       | |  |func-list|_       | |  `repr()`         |
| |  `all()`          | |  `exec()`       | |  `locals()`     | |  `reversed()`     |
| |  `anext()`        | |                     | |                     | |  `round()`        |
| |  `any()`          | |  **F**              | |  **M**              | |                       |
| |  `ascii()`        | |  `filter()`     | |  `map()`        | |  **S**                |
| |                       | |  `float()`      | |  `max()`        | |  |func-set|_          |
| |  **B**                | |  `format()`     | |  |func-memoryview|_ | |  `setattr()`      |
| |  `bin()`          | |  |func-frozendict|_ | |  `min()`        | |  `sentinel()`     |
| |  `bool()`         | |  |func-frozenset|_  | |                     | |  `slice()`        |
| |  `breakpoint()`   | |                     | |  **N**              | |  `sorted()`       |
| |  |func-bytearray|_    | |  **G**              | |  `next()`       | |  `staticmethod()` |
| |  |func-bytes|_        | |  `getattr()`    | |                     | |  |func-str|_          |
| |                       | |  `globals()`    | |  **O**              | |  `sum()`          |
| |  **C**                | |                     | |  `object()`     | |  `super()`        |
| |  `callable()`     | |  **H**              | |  `oct()`        | |                       |
| |  `chr()`          | |  `hasattr()`    | |  `open()`       | |  **T**                |
| |  `classmethod()`  | |  `hash()`       | |  `ord()`        | |  |func-tuple|_        |
| |  `compile()`      | |  `help()`       | |                     | |  `type()`         |
| |  `complex()`      | |  `hex()`        | |  **P**              | |                       |
| |                       | |                     | |  `pow()`        | |  **V**                |
| |  **D**                | |  **I**              | |  `print()`      | |  `vars()`         |
| |  `delattr()`      | |  `id()`         | |  `property()`   | |                       |
| |  |func-dict|_         | |  `input()`      | |                     | |  **Z**                |
| |  `dir()`          | |  `int()`        | |                     | |  `zip()`          |
| |  `divmod()`       | |  `isinstance()` | |                     | |                       |
| |                       | |  `issubclass()` | |                     | |  **_**                |
| |                       | |  `iter()`       | |                     | |  `__import__()`   |
+-------------------------+-----------------------+-----------------------+-------------------------+

   used, with replacement texts to make the output in the table consistent

### Function: `abs(number, /)`

   Return the absolute value of a number.  The argument may be an
   integer, a floating-point number, or an object implementing
   `object.__abs__()`.
   If the argument is a complex number, its magnitude is returned.

### Function: `aiter(async_iterable, /)`

              aiter(callable, /, stop_value, *, stop_exception=StopAsyncIteration)
              aiter(callable, /, *, stop_exception)

   Return an `term` object.
   The first argument is interpreted very differently
   depending on the presence of the other arguments.
   Without other arguments,
   the single argument must be an `term`,
   and the result is equivalent to calling `x.__aiter__()`.

   If *stop_value* or *stop_exception* is given,
   then the first argument must be a callable object.
   The asynchronous iterator created in this case
   calls *callable* with no arguments and awaits the result
   for each call to its `object.__anext__()` method;
   if the awaited value is equal to *stop_value*,
   or if the call raises an exception matching *stop_exception*,
   `exc` will be raised,
   otherwise the value will be returned.
   The callable is only called when the result of `object.__anext__()`
   is awaited.

   *stop_exception* is an exception class or a tuple of exception classes.
   If *stop_value* is not specified,
   the iteration stops only when the callable raises an exception.
   If the callable raises `exc`
   which does not match *stop_exception*,
   it is replaced with a `exc`,
   as for asynchronous generators (see `pep`).

   For example, reading fixed-size chunks from an asynchronous stream
until the end of file is reached

```python

   from functools import partial
   async for chunk in aiter(partial(reader.read, 1024), b''):
       process_chunk(chunk)

Or consuming an :class:`asyncio.Queue` until it is shut down::

   from asyncio import QueueShutDown
   async for item in aiter(queue.get, stop_exception=QueueShutDown):
       process_item(item)

.. versionadded:: 3.10

.. versionchanged:: 3.16
   Added the *stop_value* and *stop_exception* parameters.

```

### Function: `all(iterable, /)`

   Return `True` if all elements of the *iterable* are true (or if the iterable
is empty).  Equivalent to

```python

   def all(iterable):
       for element in iterable:
           if not element:
               return False
       return True

```

                       anext(async_iterator, default, /)

   When awaited, return the next item from the given :term:`asynchronous
   iterator`, or *default* if given and the iterator is `term`.

   This is the async variant of the `next()` builtin, and behaves
   similarly.

   This calls the `object.__anext__()` method of *async_iterator*,
   returning an `term`. Awaiting this returns the next value of the
   iterator. If *default* is given, it is returned if the iterator is exhausted,
   otherwise `exc` is raised.

   .. versionadded:: 3.10

### Function: `any(iterable, /)`

   Return `True` if any element of the *iterable* is true.  If the iterable
is empty, return ``False``.  Equivalent to

```python

   def any(iterable):
       for element in iterable:
           if element:
               return True
       return False

```

### Function: `ascii(object, /)`

   As `repr()`, return a string containing a printable representation of an
   object, but escape the non-ASCII characters in the string returned by
   `repr()` using `\x`, `\u`, or `\U` escapes.  This generates a string
   similar to that returned by `repr()` in Python 2.

### Function: `bin(integer, /)`

   Convert an integer number to a binary string prefixed with "0b". The result
   is a valid Python expression. If *integer* is not a Python `class` object, it
   has to define an `object.__index__()` method that returns an integer. Some
   examples:

      >>> bin(3)
      '0b11'
      >>> bin(-10)
      '-0b1010'

   If the prefix "0b" is desired or not, you can use either of the following ways.

      >>> format(14, '#b'), format(14, 'b')
      ('0b1110', '1110')
      >>> f'{14:#b}', f'{14:b}'
      ('0b1110', '1110')

   See also `enum.bin()` to represent negative values as twos-complement.

   See also `format()` for more information.

### Class: `bool(object=False, /)`

   Return a Boolean value, i.e. one of `True` or `False`.  The argument
   is converted using the standard `ref`.
   If the argument is false
   or omitted, this returns `False`; otherwise, it returns `True`.  The
   `class` class is a subclass of `class` (see `ref`).
   It cannot be subclassed further.  Its only instances are `False` and
   `True` (see `ref`).

   .. index:: pair: Boolean; type

   .. versionchanged:: 3.7
      The parameter is now positional-only.

### Function: `breakpoint(*args, **kws)`

   This function drops you into the debugger at the call site.  Specifically,
   it calls `sys.breakpointhook()`, passing `args` and `kws` straight
   through.  By default, `sys.breakpointhook()` calls
   `pdb.set_trace()` expecting no arguments.  In this case, it is
   purely a convenience function so you don't have to explicitly import
   `mod` or type as much code to enter the debugger.  However,
   `sys.breakpointhook()` can be set to some other function and
   `breakpoint()` will automatically call that, allowing you to drop into
   the debugger of choice.
   If `sys.breakpointhook()` is not accessible, this function will
   raise `exc`.

   By default, the behavior of `breakpoint()` can be changed with
   the :envvar:`PYTHONBREAKPOINT` environment variable.
   See `sys.breakpointhook()` for usage details.

   Note that this is not guaranteed if `sys.breakpointhook()`
   has been replaced.

   .. audit-event:: builtins.breakpoint breakpointhook breakpoint

   .. versionadded:: 3.7

### Class: `bytearray(source=b'')`

           bytearray(source, encoding, errors='strict')

   Return a new array of bytes.  The `class` class is a mutable
   sequence of integers in the range 0 <= x < 256.  It has most of the usual
   methods of mutable sequences, described in `ref`, as well
   as most methods that the `class` type has, see `ref`.

   The optional *source* parameter can be used to initialize the array in a few
   different ways:

   * If it is a *string*, you must also give the *encoding* (and optionally,
     *errors*) parameters; `bytearray()` then converts the string to
     bytes using `str.encode()`.

   * If it is an *integer*, the array will have that size and will be
     initialized with null bytes.

   * If it is an object conforming to the `ref`,
     a read-only buffer of the object will be used to initialize the bytes array.

   * If it is an *iterable*, it must be an iterable of integers in the range
     `0 <= x < 256`, which are used as the initial contents of the array.

   Without an argument, an array of size 0 is created.

   See also `ref` and `ref`.

### Class: `bytes(source=b'')`

           bytes(source, encoding, errors='strict')

   Return a new "bytes" object which is an immutable sequence of integers in
   the range `0 <= x < 256`.  `class` is an immutable version of
   `class` -- it has the same non-mutating methods and the same
   indexing and slicing behavior.

   Accordingly, constructor arguments are interpreted as for `bytearray()`.

   Bytes objects can also be created with literals, see `ref`.

   See also `ref`, `ref`, and `ref`.

### Function: `callable(object, /)`

   Return `const` if the *object* argument appears callable,
   `const` if not.  If this returns `True`, it is still possible that a
   call fails, but if it is `False`, calling *object* will never succeed.
   Note that classes are callable (calling a class returns a new instance);
   instances are callable if their class has a `object.__call__()` method.

   .. versionadded:: 3.2
      This function was first removed in Python 3.0 and then brought back
      in Python 3.2.

### Function: `chr(codepoint, /)`

   Return the string representing a character with the specified Unicode code point.
   For example, `chr(97)` returns the string `'a'`, while
   `chr(8364)` returns the string `'€'`. This is the inverse of `ord()`.

   The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in
   base 16).  `exc` will be raised if it is outside that range.

   Transform a method into a class method.

   A class method receives the class as an implicit first argument, just like an
   instance method receives the instance. To declare a class method, use this
idiom

```python

   class C:
       @classmethod
       def f(cls, arg1, arg2): ...

The ``@classmethod`` form is a function :term:`decorator` -- see
:ref:`function` for details.

A class method can be called either on the class (such as ``C.f()``) or on an instance (such
as ``C().f()``).  The instance is ignored except for its class. If a class
method is called for a derived class, the derived class object is passed as the
implied first argument.

Class methods are different than C++ or Java static methods. If you want those,
see :func:`staticmethod` in this section.
For more information on class methods, see :ref:`types`.

.. versionchanged:: 3.9
   Class methods can now wrap other :term:`descriptors <descriptor>` such as
   :func:`property`.

.. versionchanged:: 3.10
   Class methods now inherit the method attributes
   (:attr:`~function.__module__`, :attr:`~function.__name__`,
   :attr:`~function.__qualname__`, :attr:`~function.__doc__` and
   :attr:`~function.__annotations__`) and have a new ``__wrapped__``
   attribute.

.. deprecated-removed:: 3.11 3.13
   Class methods can no longer wrap other :term:`descriptors <descriptor>` such as
   :func:`property`.

```

### Function: `compile(source, filename, mode, flags=0, \`

                      dont_inherit=False, optimize=-1, \
                      *, module=None)

   Compile the *source* into a code or AST object.  Code objects can be executed
   by `exec()` or `eval()`.  *source* can either be a normal string, a
   byte string, or an AST object.  Refer to the `mod` module documentation
   for information on how to work with AST objects.

   The *filename* argument should give the file from which the code was read;
   pass some recognizable value if it wasn't read from a file (`'<string>'` is
   commonly used).

   The *mode* argument specifies what kind of code must be compiled; it can be
   `'exec'` if *source* consists of a sequence of statements, `'eval'` if it
   consists of a single expression, or `'single'` if it consists of a single
   interactive statement (in the latter case, expression statements that
   evaluate to something other than `None` will be printed).
   It can also be `'func_type'` if *source* consists of a
   function type signature, for example `(int) -> str`; see
   `ast.parse()` for more information. This mode requires passing
   `data` in *flags*.

   The optional arguments *flags* and *dont_inherit* control which
   `ref` should be activated
   and which `ref` should be allowed. If neither
   is present (or both are zero) the code is compiled with the same flags that
   affect the code that is calling `compile()`. If the *flags*
   argument is given and *dont_inherit* is not (or is zero) then the compiler
   options and the future statements specified by the *flags* argument are used
   in addition to those that would be used anyway. If *dont_inherit* is a
   non-zero integer then the *flags* argument is it -- the flags (future
   features and compiler options) in the surrounding code are ignored.

   Compiler options and future statements are specified by bits which can be
   bitwise ORed together to specify multiple options. The bitfield required to
   specify a given future feature can be found as the
   :attr:`~__future__._Feature.compiler_flag` attribute on the
   `class` instance in the `mod` module.
   `ref` can be found in `mod`
   module, with `PyCF_` prefix.

   The argument *optimize* specifies the optimization level of the compiler; the
   default value of `-1` selects the optimization level of the interpreter as
   given by :option:`-O` options.  Explicit levels are `0` (no optimization;
   `__debug__` is true), `1` (asserts are removed, `__debug__` is false)
   or `2` (docstrings are removed too).

   The optional argument *module* specifies the module name.
   It is needed to unambiguous `ref` syntax warnings
   by module name.

   This function raises `exc` if the compiled source is invalid,
   including a *source* containing a null character or that cannot be decoded;
   `exc` if *mode* or *flags* is invalid,
   or if a string *source* contains surrogate characters;
   `exc` or `exc` if *source* is too complex
   to parse or compile,
   for example an expression with many thousands of nested operators;
   and `exc` if *source* is too large.

   If you want to parse Python code into its AST representation, see
   `ast.parse()`.

   .. audit-event:: compile source,filename compile

      Raises an `ref` `compile` with arguments
      `source` and `filename`. This event may also be raised by implicit
      compilation.

.. note

```python

   When compiling a string with multi-line code in ``'single'`` or
   ``'eval'`` mode, input must be terminated by at least one newline
   character.  This is to facilitate detection of incomplete and complete
   statements in the :mod:`code` module.

.. warning::

   It is possible to crash the Python interpreter with a
   sufficiently large/complex string when compiling to an AST
   object due to stack depth limitations in Python's AST compiler.

.. versionchanged:: 3.2
   Allowed use of Windows and Mac newlines.  Also, input in ``'exec'`` mode
   does not have to end in a newline anymore.  Added the *optimize* parameter.

.. versionchanged:: 3.5
   Previously, :exc:`TypeError` was raised when null bytes were encountered
   in *source*.

.. versionchanged:: 3.8
   ``ast.PyCF_ALLOW_TOP_LEVEL_AWAIT`` can now be passed in flags to enable
   support for top-level ``await``, ``async for``, and ``async with``.

.. versionchanged:: 3.8
   Added support for ``mode='func_type'``.

.. versionchanged:: 3.12
   :exc:`SyntaxError` is raised instead of :exc:`ValueError` when null bytes
   are encountered in *source*.

.. versionchanged:: 3.15
   Added the *module* parameter.

```

### Class: `complex(number=0, /)`

           complex(string, /)
           complex(real=0, imag=0)

   Convert a single string or number to a complex number, or create a
   complex number from real and imaginary parts.

   Examples:

.. doctest

```python

   >>> complex('+1.23')
   (1.23+0j)
   >>> complex('-4.5j')
   -4.5j
   >>> complex('-1.23+4.5j')
   (-1.23+4.5j)
   >>> complex('\t( -1.23+4.5J )\n')
   (-1.23+4.5j)
   >>> complex('-Infinity+NaNj')
   (-inf+nanj)
   >>> complex(1.23)
   (1.23+0j)
   >>> complex(imag=-4.5)
   -4.5j
   >>> complex(-1.23, 4.5)
   (-1.23+4.5j)

If the argument is a string, it must contain either a real part (in the
same format as for :func:`float`) or an imaginary part (in the same
format but with a ``'j'`` or ``'J'`` suffix), or both real and imaginary
parts (the sign of the imaginary part is mandatory in this case).
The string can optionally be surrounded by whitespaces and the round
parentheses ``'('`` and ``')'``, which are ignored.
The string must not contain whitespace between ``'+'``, ``'-'``, the
``'j'`` or ``'J'`` suffix, and the decimal number.
For example, ``complex('1+2j')`` is fine, but ``complex('1 + 2j')`` raises
:exc:`ValueError`.
More precisely, the input must conform to the :token:`~float:complexvalue`
production rule in the following grammar, after parentheses and leading and
trailing whitespace characters are removed:

.. productionlist:: float
   complexvalue: `floatvalue` |
               : `floatvalue` ("j" | "J") |
               : `floatvalue` `sign` `absfloatvalue` ("j" | "J")

If the argument is a number, the constructor serves as a numeric
conversion like :class:`int` and :class:`float`.
For a general Python object ``x``, ``complex(x)`` delegates to
``x.__complex__()``.
If :meth:`~object.__complex__` is not defined then it falls back
to :meth:`~object.__float__`.
If :meth:`!__float__` is not defined then it falls back
to :meth:`~object.__index__`.

If two arguments are provided or keyword arguments are used, each argument
may be any numeric type (including complex).
If both arguments are real numbers, return a complex number with the real
component *real* and the imaginary component *imag*.
If both arguments are complex numbers, return a complex number with the real
component ``real.real-imag.imag`` and the imaginary component
``real.imag+imag.real``.
If one of arguments is a real number, only its real component is used in
the above expressions.

See also :meth:`complex.from_number` which only accepts a single numeric argument.

If all arguments are omitted, returns ``0j``.

The complex type is described in :ref:`typesnumeric`.

.. versionchanged:: 3.6
   Grouping digits with underscores as in code literals is allowed.

.. versionchanged:: 3.8
   Falls back to :meth:`~object.__index__` if :meth:`~object.__complex__` and
   :meth:`~object.__float__` are not defined.

.. deprecated:: 3.14
   Passing a complex number as the *real* or *imag* argument is now
   deprecated; it should only be passed as a single positional argument.

```

### Function: `delattr(object, name, /)`

   This is a relative of `setattr()`.  The arguments are an object and a
   string.  The string must be the name of one of the object's attributes.  The
   function deletes the named attribute, provided the object allows it.  For
   example, `delattr(x, 'foobar')` is equivalent to `del x.foobar`.
   *name* need not be a Python identifier (see `setattr()`).

### Class: `dict(**kwargs)`

           dict(mapping, /, **kwargs)
           dict(iterable, /, **kwargs)

   Create a new dictionary.  The `class` object is the dictionary class.
   See also `ref` for documentation about this class.

   For other containers see the built-in `class`, `class`,
   `class`, and `class` classes, as well as the `mod` module.

### Function: `dir()`

              dir(object, /)

   Without arguments, return the list of names in the current local scope.  With an
   argument, attempt to return a list of valid attributes for that object.

   If the object has a method named `object.__dir__()`,
   this method will be called and
   must return the list of attributes. This allows objects that implement a custom
   `object.__getattr__()` or `object.__getattribute__()` function
   to customize the way
   `dir()` reports their attributes.

   If the object does not provide `object.__dir__()`,
   the function tries its best to gather information from the object's
   :attr:`~object.__dict__` attribute, if defined, and
   from its type object.  The resulting list is not necessarily complete and may
   be inaccurate when the object has a custom `object.__getattr__()`.

   The default `dir()` mechanism behaves differently with different types of
   objects, as it attempts to produce the most relevant, rather than complete,
   information:

   * If the object is a module object, the list contains the names of the module's
     attributes.

   * If the object is a type or class object, the list contains the names of its
     attributes, and recursively of the attributes of its bases.

   * Otherwise, the list contains the object's attributes' names, the names of its
     class's attributes, and recursively of the attributes of its class's base
     classes.

   The resulting list is sorted alphabetically.  For example:

      >>> import struct
      >>> dir()   # show the names in the module namespace  # doctest: +SKIP
      ['__builtins__', '__name__', 'struct']
      >>> dir(struct)   # show the names in the struct module # doctest: +SKIP
      ['Struct', '__all__', '__builtins__', '__doc__', '__file__',
       '__initializing__', '__loader__', '__name__', '__package__',
       '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
       'unpack', 'unpack_from']
      >>> class Shape:
      ...     def __dir__(self):
      ...         return ['area', 'perimeter', 'location']
      ...
      >>> s = Shape()
      >>> dir(s)
      ['area', 'location', 'perimeter']

.. note

```python

   Because :func:`dir` is supplied primarily as a convenience for use at an
   interactive prompt, it tries to supply an interesting set of names more
   than it tries to supply a rigorously or consistently defined set of names,
   and its detailed behavior may change across releases.  For example,
   metaclass attributes are not in the result list when the argument is a
   class.

```

### Function: `divmod(a, b, /)`

   Take two (non-complex) numbers as arguments and return a pair of numbers
   consisting of their quotient and remainder when using integer division.  With
   mixed operand types, the rules for binary arithmetic operators apply.  For
   integers, the result is the same as `(a // b, a % b)`. For floating-point
   numbers the result is `(q, a % b)`, where *q* is usually ``math.floor(a /
   b)` but may be 1 less than that.  In any case `q * b + a % b`` is very
   close to *a*, if `a % b` is non-zero it has the same sign as *b*, and ``0
   <= abs(a % b) < abs(b)``.

### Function: `enumerate(iterable, start=0)`

   Return an enumerate object. *iterable* must be a sequence, an
   `term`, or some other object which supports iteration.
   The `iterator.__next__()` method of the iterator returned by
   `enumerate()` returns a tuple containing a count (from *start* which
   defaults to 0) and the values obtained from iterating over *iterable*.

      >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
      >>> list(enumerate(seasons))
      [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
      >>> list(enumerate(seasons, start=1))
      [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

Equivalent to

```python

   def enumerate(iterable, start=0):
       n = start
       for elem in iterable:
           yield n, elem
           n += 1

```

### Function: `eval(source, /, globals=None, locals=None)`

   :param source:
      A Python expression.
   :type source: `class` | `ref`

   :param globals:
      The global namespace (default: `None`).
   :type globals: `class` | `class` | `None`

   :param locals:
      The local namespace (default: `None`).
   :type locals: `term` | `None`

   :returns: The result of the evaluated expression.
   :raises: Syntax errors are reported as exceptions.

.. warning

```python

   This function executes arbitrary code. Calling it with
   untrusted user-supplied input will lead to security vulnerabilities.

The *source* argument is parsed and evaluated as a Python expression
(technically speaking, an :ref:`expression list <exprlists>`)
using the *globals* and *locals* mappings as global and local namespace.
If the *globals* dictionary is present and does not contain a value for the
key ``__builtins__``, a
reference to the dictionary of the built-in module :mod:`builtins` is
inserted under that key before *source* is parsed.
Overriding ``__builtins__`` can be used to restrict or change the available
names, but this is **not** a security mechanism: the executed code can
still access all builtins.
If the *locals* mapping is omitted it defaults to the
*globals* dictionary.  If both mappings are omitted, the source is
executed with the *globals* and *locals* in the environment where
:func:`eval` is called.  Note, *eval()* will only have access to the
:term:`nested scopes <nested scope>` (non-locals) in the enclosing
environment if they are already referenced in the scope that is calling
:func:`eval` (e.g. via a :keyword:`nonlocal` statement).

Example:

   >>> x = 1
   >>> eval('x+1')
   2

   >>> eval("1, 2")
   (1, 2)

This function can also be used to execute arbitrary code objects (such as
those created by :func:`compile`).  In this case, pass a code object instead
of a string.  If the code object has been compiled with ``'exec'`` as the
*mode* argument, :func:`eval`\'s return value will be ``None``.

Hints: dynamic execution of statements is supported by the :func:`exec`
function.  The :func:`globals` and :func:`locals` functions
return the current global and local dictionary, respectively, which may be
useful to pass around for use by :func:`eval` or :func:`exec`.

If the given source is a string, then leading and trailing spaces and tabs
are stripped.

See :func:`ast.literal_eval` for a function to evaluate strings
with expressions containing only literals.

.. audit-event:: exec code_object eval

   Raises an :ref:`auditing event <auditing>` ``exec`` with the code object
   as the argument. Code compilation events may also be raised.

.. versionchanged:: 3.13

   The *globals* and *locals* arguments can now be passed as keywords.

.. versionchanged:: 3.13

   The semantics of the default *locals* namespace have been adjusted as
   described for the :func:`locals` builtin.

.. versionchanged:: 3.15

   *globals* can now be a :class:`frozendict`.

```

### Function: `exec(source, /, globals=None, locals=None, *, closure=None)`

.. warning

```python

   This function executes arbitrary code. Calling it with
   untrusted user-supplied input will lead to security vulnerabilities.

This function supports dynamic execution of Python code. *source* must be
either a string or a code object.  If it is a string, the string is parsed as
a suite of Python statements which is then executed (unless a syntax error
occurs). If it is a code object, it is simply executed.  In all cases,
the code that's executed is expected to be valid as file input (see the
section :ref:`file-input` in the Reference Manual). Be aware that the
:keyword:`nonlocal`, :keyword:`yield`,  and :keyword:`return`
statements may not be used outside of
function definitions even within the context of code passed to the
:func:`exec` function. The return value is ``None``.

In all cases, if the optional parts are omitted, the code is executed in the
current scope.  If only *globals* is provided, it must be a dictionary
(and not a subclass of dictionary), which
will be used for both the global and the local variables.  If *globals* and
*locals* are given, they are used for the global and local variables,
respectively.  If provided, *locals* can be any mapping object.  Remember
that at the module level, globals and locals are the same dictionary.

.. note::

   When ``exec`` gets two separate objects as *globals* and *locals*, the
   code will be executed as if it were embedded in a class definition. This
   means functions and classes defined in the executed code will not be able
   to access variables assigned at the top level (as the "top level"
   variables are treated as class variables in a class definition).

If the *globals* dictionary does not contain a value for the key
``__builtins__``, a reference to the dictionary of the built-in module
:mod:`builtins` is inserted under that key.
Overriding ``__builtins__`` can be used to restrict or change the available
names, but this is **not** a security mechanism: the executed code can
still access all builtins.

The *closure* argument specifies a closure--a tuple of cellvars.
It's only valid when *source* is a code object containing
:term:`free (closure) variables <closure variable>`.
The length of the tuple must exactly match the length of the code object's
:attr:`~codeobject.co_freevars` attribute.

.. audit-event:: exec code_object exec

   Raises an :ref:`auditing event <auditing>` ``exec`` with the code object
   as the argument. Code compilation events may also be raised.

.. note::

   The built-in functions :func:`globals` and :func:`locals` return the current
   global and local namespace, respectively, which may be useful to pass around
   for use as the second and third argument to :func:`exec`.

.. note::

   The default *locals* act as described for function :func:`locals` below.
   Pass an explicit *locals* dictionary if you need to see effects of the
   code on *locals* after function :func:`exec` returns.

.. versionchanged:: 3.11
   Added the *closure* parameter.

.. versionchanged:: 3.13

   The *globals* and *locals* arguments can now be passed as keywords.

.. versionchanged:: 3.13

   The semantics of the default *locals* namespace have been adjusted as
   described for the :func:`locals` builtin.

.. versionchanged:: 3.15

   *globals* can now be a :class:`frozendict`.

```

### Function: `filter(function, iterable, /)`

   Construct an iterator from those elements of *iterable* for which *function*
   is true.  *iterable* may be either a sequence, a container which
   supports iteration, or an iterator.  If *function* is `None`, the identity
   function is assumed, that is, all elements of *iterable* that are false are
   removed.

   Note that `filter(function, iterable)` is equivalent to the generator
   expression `(item for item in iterable if function(item))` if function is
   not `None` and `(item for item in iterable if item)` if function is
   `None`.

   See `itertools.filterfalse()` for the complementary function that returns
   elements of *iterable* for which *function* is false.

### Class: `float(number=0.0, /)`

           float(string, /)

.. index

```python
   single: NaN
   single: Infinity

Return a floating-point number constructed from a number or a string.

Examples:

.. doctest::

   >>> float('+1.23')
   1.23
   >>> float('   -12345\n')
   -12345.0
   >>> float('1e-003')
   0.001
   >>> float('+1E6')
   1000000.0
   >>> float('-Infinity')
   -inf

If the argument is a string, it should contain a decimal number, optionally
preceded by a sign, and optionally embedded in whitespace.  The optional
sign may be ``'+'`` or ``'-'``; a ``'+'`` sign has no effect on the value
produced.  The argument may also be a string representing a NaN
(not-a-number), or positive or negative infinity.
More precisely, the input must conform to the :token:`~float:floatvalue`
production rule in the following grammar, after leading and trailing
whitespace characters are removed:

.. productionlist:: float
   sign: "+" | "-"
   infinity: "Infinity" | "inf"
   nan: "nan"
   digit: <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
   digitpart: `digit` (["_"] `digit`)*
   number: [`digitpart`] "." `digitpart` | `digitpart` ["."]
   exponent: ("e" | "E") [`sign`] `digitpart`
   floatnumber: `number` [`exponent`]
   absfloatvalue: `floatnumber` | `infinity` | `nan`
   floatvalue: [`sign`] `absfloatvalue`

Case is not significant, so, for example, "inf", "Inf", "INFINITY", and
"iNfINity" are all acceptable spellings for positive infinity.

Otherwise, if the argument is an integer or a floating-point number, a
floating-point number with the same value (within Python's floating-point
precision) is returned.  If the argument is outside the range of a Python
float, an :exc:`OverflowError` will be raised.

For a general Python object ``x``, ``float(x)`` delegates to
``x.__float__()``.  If :meth:`~object.__float__` is not defined then it falls back
to :meth:`~object.__index__`.

See also :meth:`float.from_number` which only accepts a numeric argument.

If no argument is given, ``0.0`` is returned.

The float type is described in :ref:`typesnumeric`.

.. versionchanged:: 3.6
   Grouping digits with underscores as in code literals is allowed.

.. versionchanged:: 3.7
   The parameter is now positional-only.

.. versionchanged:: 3.8
   Falls back to :meth:`~object.__index__` if :meth:`~object.__float__` is not defined.

```

.. index

```python
single: __format__
single: string; format() (built-in function)

```

### Function: `format(value, format_spec="", /)`

   Convert a *value* to a "formatted" representation, as controlled by
   *format_spec*.  The interpretation of *format_spec* will depend on the type
   of the *value* argument; however, there is a standard formatting syntax that
   is used by most built-in types: `ref`.

   The default *format_spec* is an empty string which usually gives the same
   effect as calling `str(value) <str>()`.

   A call to `format(value, format_spec)` is translated to
   `type(value).__format__(value, format_spec)` which bypasses the instance
   dictionary when searching for the value's `object.__format__()` method.
   A `exc` exception is raised if the method search reaches
   `mod` and the *format_spec* is non-empty, or if either the
   *format_spec* or the return value are not strings.

   .. versionchanged:: 3.4
      `object().__format__(format_spec)` raises `exc`
      if *format_spec* is not an empty string.

### Class: `frozendict(**kwargs)`

           frozendict(mapping, /, **kwargs)
           frozendict(iterable, /, **kwargs)

   Create a new frozen dictionary.  The `class` object is a built-in class.
   See also `ref` for documentation about this class.

   For other containers see the built-in `class`, `class`, `class`,
   and `class` classes, as well as the `mod` module.

   .. versionadded:: 3.15

### Class: `frozenset(iterable=(), /)`

   Return a new `class` object, optionally with elements taken from
   *iterable*.  `class` is a built-in class.  See also
   `ref` for documentation about this class.

   For other containers see the built-in `class`, `class`,
   `class`, and `class` classes, as well as the `mod`
   module.

### Function: `getattr(object, name, /)`

              getattr(object, name, default, /)

   Return the value of the named attribute of *object*.  *name* must be a string.
   If the string is the name of one of the object's attributes, the result is the
   value of that attribute.  For example, `getattr(x, 'foobar')` is equivalent to
   `x.foobar`.  If the named attribute does not exist, *default* is returned if
   provided, otherwise `exc` is raised.
   *name* need not be a Python identifier (see `setattr()`).

.. note

```python

   Since :ref:`private name mangling <private-name-mangling>` happens at
   compilation time, one must manually mangle a private attribute's
   (attributes with two leading underscores) name in order to retrieve it with
   :func:`getattr`.

```

### Function: `globals()`

   Return the dictionary implementing the current module namespace. For code within
   functions, this is set when the function is defined and remains the same
   regardless of where the function is called.

### Function: `hasattr(object, name, /)`

   The arguments are an object and a string.  The result is `True` if the
   string is the name of one of the object's attributes, `False` if not. (This
   is implemented by calling `getattr(object, name)` and seeing whether it
   raises an `exc` or not.)

### Function: `hash(object, /)`

   Return the hash value of the object (if it has one).  Hash values are
   integers.  They are used to quickly compare dictionary keys during a
   dictionary lookup.  Numeric values that compare equal have the same hash
   value (even if they are of different types, as is the case for 1 and 1.0).

.. note

```python

   For objects with custom :meth:`~object.__hash__` methods,
   note that :func:`hash`
   truncates the return value based on the bit width of the host machine.

```

### Function: `help()`

              help(request)

   Invoke the built-in help system.  (This function is intended for interactive
   use.)  If no argument is given, the interactive help system starts on the
   interpreter console.  If the argument is a string, then the string is looked up
   as the name of a module, function, class, method, keyword, or documentation
   topic, and a help page is printed on the console.  If the argument is any other
   kind of object, a help page on the object is generated.

   Note that if a slash(/) appears in the parameter list of a function when
   invoking `help()`, it means that the parameters prior to the slash are
   positional-only. For more info, see
   `ref`.

   This function is added to the built-in namespace by the `mod` module.

   .. versionchanged:: 3.4
      Changes to `mod` and `mod` mean that the reported
      signatures for callables are now more comprehensive and consistent.

### Function: `hex(integer, /)`

   Convert an integer number to a lowercase hexadecimal string prefixed with
   "0x". If *integer* is not a Python `class` object, it has to define an
   `object.__index__()` method that returns an integer. Some examples:

      >>> hex(255)
      '0xff'
      >>> hex(-42)
      '-0x2a'

   If you want to convert an integer number to an uppercase or lower hexadecimal
   string with prefix or not, you can use either of the following ways:

     >>> '%#x' % 255, '%x' % 255, '%X' % 255
     ('0xff', 'ff', 'FF')
     >>> format(255, '#x'), format(255, 'x'), format(255, 'X')
     ('0xff', 'ff', 'FF')
     >>> f'{255:#x}', f'{255:x}', f'{255:X}'
     ('0xff', 'ff', 'FF')

   See also `format()` for more information.

   See also `int()` for converting a hexadecimal string to an
   integer using a base of 16.

.. note

```python

   To obtain a hexadecimal string representation for a float, use the
   :meth:`float.hex` method.

```

### Function: `id(object, /)`

   Return the "identity" of an object.  This is an integer which
   is guaranteed to be unique and constant for this object during its lifetime.
   Two objects with non-overlapping lifetimes may have the same `id()`
   value.

   .. impl-detail:: This is the address of the object in memory.

   .. audit-event:: builtins.id id id

### Function: `input()`

              input(prompt, /)

   If the *prompt* argument is present, it is written to standard output without
   a trailing newline.  The function then reads a line from input, converts it
   to a string (stripping a trailing newline), and returns that.  When EOF is
read, :exc:`EOFError` is raised.  Example

```python

   >>> s = input('--> ')  # doctest: +SKIP
   --> Monty Python's Flying Circus
   >>> s  # doctest: +SKIP
   "Monty Python's Flying Circus"

If the :mod:`readline` module was loaded, then :func:`input` will use it
to provide elaborate line editing and history features.

.. audit-event:: builtins.input prompt input

   Raises an :ref:`auditing event <auditing>` ``builtins.input`` with
   argument ``prompt`` before reading input

.. audit-event:: builtins.input/result result input

   Raises an :ref:`auditing event <auditing>` ``builtins.input/result``
   with the result after successfully reading input.

```

### Class: `int(number=0, /)`

           int(string, /, base=10)

   Return an integer object constructed from a number or a string, or return
   `0` if no arguments are given.

   Examples:

.. doctest

```python

   >>> int(123.45)
   123
   >>> int('123')
   123
   >>> int('   -12_345\n')
   -12345
   >>> int('FACE', 16)
   64206
   >>> int('0xface', 0)
   64206
   >>> int('01110011', base=2)
   115

If the argument defines :meth:`~object.__int__`,
``int(x)`` returns ``x.__int__()``.  If the argument defines
:meth:`~object.__index__`, it returns ``x.__index__()``.
For floating-point numbers, this truncates towards zero.

If the argument is not a number or if *base* is given, then it must be a string,
:class:`bytes`, or :class:`bytearray` instance representing an integer
in radix *base*.  Optionally, the string can be preceded by ``+`` or ``-``
(with no space in between), have leading zeros, be surrounded by whitespace,
and have single underscores interspersed between digits.

A base-n integer string contains digits, each representing a value from 0 to
n-1. The values 0--9 can be represented by any Unicode decimal digit. The
values 10--35 can be represented by ``a`` to ``z`` (or ``A`` to ``Z``). The
default *base* is 10. The allowed bases are 0 and 2--36. Base-2, -8, and -16
strings can be optionally prefixed with ``0b``/``0B``, ``0o``/``0O``, or
``0x``/``0X``, as with integer literals in code.  For base 0, the string is
interpreted in a similar way to an :ref:`integer literal in code <integers>`,
in that the actual base is 2, 8, 10, or 16 as determined by the prefix. Base
0 also disallows leading zeros: ``int('010', 0)`` is not legal, while
``int('010')`` and ``int('010', 8)`` are.

The integer type is described in :ref:`typesnumeric`.

.. versionchanged:: 3.4
   If *base* is not an instance of :class:`int` and the *base* object has a
   :meth:`base.__index__ <object.__index__>` method, that method is called
   to obtain an integer for the base.  Previous versions used
   :meth:`base.__int__ <object.__int__>` instead of :meth:`base.__index__
   <object.__index__>`.

.. versionchanged:: 3.6
   Grouping digits with underscores as in code literals is allowed.

.. versionchanged:: 3.7
   The first parameter is now positional-only.

.. versionchanged:: 3.8
   Falls back to :meth:`~object.__index__` if :meth:`~object.__int__` is not defined.

.. versionchanged:: 3.11
   :class:`int` string inputs and string representations can be limited to
   help avoid denial of service attacks. A :exc:`ValueError` is raised when
   the limit is exceeded while converting a string to an :class:`int` or
   when converting an :class:`int` into a string would exceed the limit.
   See the :ref:`integer string conversion length limitation
   <int_max_str_digits>` documentation.

.. versionchanged:: 3.14
   :func:`int` no longer delegates to the :meth:`~object.__trunc__` method.

```

### Function: `isinstance(object, classinfo, /)`

   Return `True` if the *object* argument is an instance of the *classinfo*
   argument, or of a (direct, indirect, or :term:`virtual <abstract base
   class>`) subclass thereof.  If *object* is not
   an object of the given type, the function always returns `False`.
   If *classinfo* is a tuple of type objects (or recursively, other such
   tuples) or a `ref` of multiple types, return `True` if
   *object* is an instance of any of the types.
   If *classinfo* is not a type or tuple of types and such tuples,
   a `exc` exception is raised. `exc` may not be
   raised for an invalid type if an earlier check succeeds.

   .. versionchanged:: 3.10
      *classinfo* can be a `ref`.

### Function: `issubclass(cls, classinfo, /)`

   Return `True` if *cls* is a subclass (direct, indirect, or :term:`virtual
   <abstract base class>`) of *classinfo*.  A
   class is considered a subclass of itself. *classinfo* may be a tuple of class
   objects (or recursively, other such tuples)
   or a `ref`, in which case return `True` if *cls* is a
   subclass of any entry in *classinfo*.  In any other case, a `exc`
   exception is raised.

   .. versionchanged:: 3.10
      *classinfo* can be a `ref`.

### Function: `iter(iterable, /)`

              iter(callable, /, stop_value, *, stop_exception=StopIteration)
              iter(callable, /, *, stop_exception)

   Return an `term` object.  The first argument is interpreted very
   differently depending on the presence of the other arguments. Without other
   arguments, the single argument must be a collection object which supports the
   `term` protocol (the `object.__iter__()` method),
   or it must support
   the sequence protocol (the `object.__getitem__()` method with integer arguments
   starting at `0`).  If it does not support either of those protocols,
   `exc` is raised.

   If *stop_value* or *stop_exception* is given,
   then the first argument must be a callable object.  The iterator created in this case
   will call *callable* with no arguments for each call to its
   `iterator.__next__()` method; if the value returned is equal to
   *stop_value*, or if the call raises an exception matching *stop_exception*,
   `exc` will be raised, otherwise the value will
   be returned.

   *stop_exception* is an exception class or a tuple of exception classes.
   If *stop_value* is not specified,
   the iteration stops only when the callable raises an exception.
   If the callable raises `exc`
   which does not match *stop_exception*,
   it is replaced with a `exc`,
   as for generators (see `pep`).

   See also `ref`.

   One useful application of the second form of `iter()` is to build a
   block-reader. For example, reading fixed-width blocks from a binary
database file until the end of file is reached

```python

   from functools import partial
   with open('mydata.db', 'rb') as f:
       for block in iter(partial(f.read, 64), b''):
           process_block(block)

*stop_exception* is useful for callables
which report :term:`exhaustion <exhausted>` by raising an exception
instead of returning a special value.
For example, draining a queue::

   import queue
   for item in iter(input_queue.get_nowait, stop_exception=queue.Empty):
       process_item(item)

.. versionchanged:: 3.16
   Added the *stop_exception* parameter
   and allowed passing *stop_value* by keyword.

```

### Function: `len(object, /)`

   Return the length (the number of items) of an object.  The argument may be a
   sequence (such as a string, bytes, tuple, list, or range) or a collection
   (such as a dictionary, set, or frozen set).

.. impl-detail

```python

   ``len`` raises :exc:`OverflowError` on lengths larger than
   :data:`sys.maxsize`, such as :class:`range(2 ** 100) <range>`.

```

### Class: `list(iterable=(), /)`

   Rather than being a function, `class` is actually a mutable
   sequence type, as documented in `ref` and `ref`.

### Function: `locals()`

   Return a mapping object representing the current local symbol table, with
   variable names as the keys, and their currently bound references as the
   values.

   At module scope, as well as when using `exec()` or `eval()` with
   a single namespace, this function returns the same namespace as
   `globals()`.

   At class scope, it returns the namespace that will be passed to the
   metaclass constructor.

   When using `exec()` or `eval()` with separate local and global
   arguments, it returns the local namespace passed in to the function call.

   In all of the above cases, each call to `locals()` in a given frame of
   execution will return the *same* mapping object. Changes made through
   the mapping object returned from `locals()` will be visible as assigned,
   reassigned, or deleted local variables, and assigning, reassigning, or
   deleting local variables will immediately affect the contents of the
   returned mapping object.

   In an `term` (including functions, generators, and
   coroutines), each call to `locals()` instead returns a fresh dictionary
   containing the current bindings of the function's local variables and any
   nonlocal cell references. In this case, name binding changes made via the
   returned dict are *not* written back to the corresponding local variables
   or nonlocal cell references, and assigning, reassigning, or deleting local
   variables and nonlocal cell references does *not* affect the contents
   of previously returned dictionaries.

   Calling `locals()` as part of a comprehension in a function, generator, or
   coroutine is equivalent to calling it in the containing scope, except that
   the comprehension's initialised iteration variables will be included. In
   other scopes, it behaves as if the comprehension were running as a nested
   function.

   Calling `locals()` as part of a generator expression is equivalent to
   calling it in a nested generator function.

   .. versionchanged:: 3.12
      The behaviour of `locals()` in a comprehension has been updated as
      described in `pep`.

   .. versionchanged:: 3.13
      As part of `pep`, the semantics of mutating the mapping objects
      returned from this function are now defined. The behavior in
      `term` is now as described above.
      Aside from being defined, the behaviour in other scopes remains
      unchanged from previous versions.

### Function: `map(function, iterable, /, *iterables, strict=False)`

   Return an iterator that applies *function* to every item of *iterable*,
   yielding the results.  If additional *iterables* arguments are passed,
   *function* must take that many arguments and is applied to the items from all
   iterables in parallel.  With multiple iterables, the iterator stops when the
   shortest iterable is `term`.  If *strict* is `True` and one of the
   iterables is exhausted before the others, a `exc` is raised. For
   cases where the function inputs are already arranged into argument tuples,
   see `itertools.starmap()`.

   .. versionchanged:: 3.14
      Added the *strict* parameter.

### Function: `max(iterable, /, *, key=None)`

              max(iterable, /, *, default, key=None)
              max(arg1, arg2, /, *args, key=None)

   Return the largest item in an iterable or the largest of two or more
   arguments.

   If one positional argument is provided, it should be an `term`.
   The largest item in the iterable is returned.  If two or more positional
   arguments are provided, the largest of the positional arguments is
   returned.

   There are two optional keyword-only arguments. The *key* argument specifies
   a one-argument ordering function like that used for `list.sort()`. The
   *default* argument specifies an object to return if the provided iterable is
   empty. If the iterable is empty and *default* is not provided, a
   `exc` is raised.

   If multiple items are maximal, the function returns the first one
   encountered.  This is consistent with other sort-stability preserving tools
   such as `sorted(iterable, key=keyfunc, reverse=True)[0]` and
   `heapq.nlargest(1, iterable, key=keyfunc)`.

   .. versionchanged:: 3.4
      Added the *default* keyword-only parameter.

   .. versionchanged:: 3.8
      The *key* can be `None`.

### Class: `memoryview(object)`

   Return a "memory view" object created from the given argument.  See
   `ref` for more information.

### Function: `min(iterable, /, *, key=None)`

              min(iterable, /, *, default, key=None)
              min(arg1, arg2, /, *args, key=None)

   Return the smallest item in an iterable or the smallest of two or more
   arguments.

   If one positional argument is provided, it should be an `term`.
   The smallest item in the iterable is returned.  If two or more positional
   arguments are provided, the smallest of the positional arguments is
   returned.

   There are two optional keyword-only arguments. The *key* argument specifies
   a one-argument ordering function like that used for `list.sort()`. The
   *default* argument specifies an object to return if the provided iterable is
   empty. If the iterable is empty and *default* is not provided, a
   `exc` is raised.

   If multiple items are minimal, the function returns the first one
   encountered.  This is consistent with other sort-stability preserving tools
   such as `sorted(iterable, key=keyfunc)[0]` and ``heapq.nsmallest(1,
   iterable, key=keyfunc)``.

   .. versionchanged:: 3.4
      Added the *default* keyword-only parameter.

   .. versionchanged:: 3.8
      The *key* can be `None`.

### Function: `next(iterator, /)`

              next(iterator, default, /)

   Retrieve the next item from the `term` by calling its
   `iterator.__next__()` method.  If *default* is given, it is returned
   if the iterator is `term`, otherwise `exc` is raised.

### Class: `object()`

   This is the ultimate base class of all other classes. It has methods
   that are common to all instances of Python classes. When the constructor
   is called, it returns a new featureless object. The constructor does not
   accept any arguments.

.. note

```python

   :class:`object` instances do *not* have :attr:`~object.__dict__`
   attributes, so you can't assign arbitrary attributes to an instance of
   :class:`object`.

```

### Function: `oct(integer, /)`

  Convert an integer number to an octal string prefixed with "0o".  The result
  is a valid Python expression. If *integer* is not a Python `class` object, it
  has to define an `object.__index__()` method that returns an integer. For
  example:

      >>> oct(8)
      '0o10'
      >>> oct(-56)
      '-0o70'

  If you want to convert an integer number to an octal string either with the prefix
  "0o" or not, you can use either of the following ways.

      >>> '%#o' % 10, '%o' % 10
      ('0o12', '12')
      >>> format(10, '#o'), format(10, 'o')
      ('0o12', '12')
      >>> f'{10:#o}', f'{10:o}'
      ('0o12', '12')

  See also `format()` for more information.

.. index

```python
single: file object; open() built-in function

```

### Function: `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`

   Open *file* and return a corresponding `term`.  If the file
   cannot be opened, an `exc` is raised. See
   `ref` for more examples of how to use this function.

   *file* is a `term` giving the pathname (absolute or
   relative to the current working directory) of the file to be opened or an
   integer file descriptor of the file to be wrapped.  (If a file descriptor is
   given, it is closed when the returned I/O object is closed unless *closefd*
   is set to `False`.)

   *mode* is an optional string that specifies the mode in which the file is
   opened.  It defaults to `'r'` which means open for reading in text mode.
   Other common values are `'w'` for writing (truncating the file if it
   already exists), `'x'` for exclusive creation, and `'a'` for appending
   (which on *some* Unix systems, means that *all* writes append to the end of
   the file regardless of the current seek position).  In text mode, if
   *encoding* is not specified, UTF-8 is used by default; if
   `ref` is disabled,
   `locale.getencoding()` is called to get the current locale encoding.
   (For reading and writing raw bytes use binary mode and leave
   *encoding* unspecified.)  The available modes are:

   .. _filemodes:

.. index

```python
   pair: file; modes

========= ===============================================================
Character Meaning
========= ===============================================================
``'r'``   open for reading (default)
``'w'``   open for writing, truncating the file first
``'x'``   open for exclusive creation, failing if the file already exists
``'a'``   open for writing, appending to the end of file if it exists
``'b'``   binary mode
``'t'``   text mode (default)
``'+'``   open for updating (reading and writing)
========= ===============================================================

The default mode is ``'r'`` (open for reading text, a synonym of ``'rt'``).
Modes ``'w+'`` and ``'w+b'`` open and truncate the file.  Modes ``'r+'``
and ``'r+b'`` open the file with no truncation.

As mentioned in the :ref:`io-overview`, Python distinguishes between binary
and text I/O.  Files opened in binary mode (including ``'b'`` in the *mode*
argument) return contents as :class:`bytes` objects without any decoding.  In
text mode (the default, or when ``'t'`` is included in the *mode* argument),
the contents of the file are returned as :class:`str`, the bytes having been
first decoded using the default encoding or using the specified
*encoding* if given.

.. note::

   Python doesn't depend on the underlying operating system's notion of text
   files; all the processing is done by Python itself, and is therefore
   platform-independent.

*buffering* is an optional integer used to set the buffering policy.  Pass 0
to switch buffering off (only allowed in binary mode), 1 to select line
buffering (only usable when writing in text mode), and an integer > 1 to indicate the size
in bytes of a fixed-size chunk buffer. Note that specifying a buffer size this
way applies for binary buffered I/O, but ``TextIOWrapper`` (i.e., files opened
with ``mode='r+'``) would have another buffering. To disable buffering in
``TextIOWrapper``, consider using the ``write_through`` flag for
:func:`io.TextIOWrapper.reconfigure`. When no *buffering* argument is
given, the default buffering policy works as follows:

* Binary files are buffered in fixed-size chunks; the size of the buffer
  is ``max(min(blocksize, 8 MiB), DEFAULT_BUFFER_SIZE)``
  when the device block size is available.
  On most systems, the buffer will typically be 128 kilobytes long.

* "Interactive" text files (files for which :meth:`~io.IOBase.isatty`
  returns ``True``) use line buffering.  Other text files use the policy
  described above for binary files.

*encoding* is the name of the encoding used to decode or encode the file.
This should only be used in text mode.  The default encoding is UTF-8;
if :ref:`Python UTF-8 Mode <utf8-mode>` is disabled, the default is
platform-dependent (whatever :func:`locale.getencoding` returns).
Any :term:`text encoding` supported by Python can be used, and
``encoding="locale"`` specifies the current locale encoding explicitly.
See the :mod:`codecs` module for the list of supported encodings.

*errors* is an optional string that specifies how encoding and decoding
errors are to be handled—this cannot be used in binary mode.
A variety of standard error handlers are available,
though any error handling name that has been registered with
:func:`codecs.register_error` is also valid.  The standard names
can be found in :ref:`error-handlers`.

.. index::
   single: universal newlines; open() built-in function

.. _open-newline-parameter:

*newline* determines how to parse newline characters from the stream.
It can be ``None``, ``''``, ``'\n'``, ``'\r'``, and
``'\r\n'``.  It works as follows:

* When reading input from the stream, if *newline* is ``None``, universal
  newlines mode is enabled.  Lines in the input can end in ``'\n'``,
  ``'\r'``, or ``'\r\n'``, and these are translated into ``'\n'`` before
  being returned to the caller.  If it is ``''``, universal newlines mode is
  enabled, but line endings are returned to the caller untranslated.  If it
  has any of the other legal values, input lines are only terminated by the
  given string, and the line ending is returned to the caller untranslated.

* When writing output to the stream, if *newline* is ``None``, any ``'\n'``
  characters written are translated to the system default line separator,
  :data:`os.linesep`.  If *newline* is ``''`` or ``'\n'``, no translation
  takes place.  If *newline* is any of the other legal values, any ``'\n'``
  characters written are translated to the given string.

If *closefd* is ``False`` and a file descriptor rather than a filename was
given, the underlying file descriptor will be kept open when the file is
closed.  If a filename is given *closefd* must be ``True`` (the default);
otherwise, an error will be raised.

A custom opener can be used by passing a callable as *opener*. The underlying
file descriptor for the file object is then obtained by calling *opener* with
(*file*, *flags*). *opener* must return an open file descriptor (passing
:mod:`os.open` as *opener* results in functionality similar to passing
``None``).

The newly created file is :ref:`non-inheritable <fd_inheritance>`.

The following example uses the :ref:`dir_fd <dir_fd>` parameter of the
:func:`os.open` function to open a file relative to a given directory::

   >>> import os
   >>> dir_fd = os.open('somedir', os.O_RDONLY)
   >>> def opener(path, flags):
   ...     return os.open(path, flags, dir_fd=dir_fd)
   ...
   >>> with open('spamspam.txt', 'w', opener=opener) as f:
   ...     print('This will be written to somedir/spamspam.txt', file=f)
   ...
   >>> os.close(dir_fd)  # don't leak a file descriptor

The type of :term:`file object` returned by the :func:`open` function
depends on the mode.  When :func:`open` is used to open a file in a text
mode (``'w'``, ``'r'``, ``'wt'``, ``'rt'``, etc.), it returns a subclass of
:class:`io.TextIOBase` (specifically :class:`io.TextIOWrapper`).  When used
to open a file in a binary mode with buffering, the returned class is a
subclass of :class:`io.BufferedIOBase`.  The exact class varies: in read
binary mode, it returns an :class:`io.BufferedReader`; in write binary and
append binary modes, it returns an :class:`io.BufferedWriter`, and in
read/write mode, it returns an :class:`io.BufferedRandom`.  When buffering is
disabled, the raw stream, a subclass of :class:`io.RawIOBase`,
:class:`io.FileIO`, is returned.

.. index::
   single: line-buffered I/O
   single: unbuffered I/O
   single: buffer size, I/O
   single: I/O control; buffering
   single: binary mode
   single: text mode
   pair: module; sys

See also the file handling modules, such as :mod:`fileinput`, :mod:`io`
(where :func:`open` is declared), :mod:`os`, :mod:`os.path`, :mod:`tempfile`,
and :mod:`shutil`.

.. audit-event:: open path,mode,flags open

The ``mode`` and ``flags`` arguments may have been modified or inferred from
the original call.

.. versionchanged:: 3.3

   * The *opener* parameter was added.
   * The ``'x'`` mode was added.
   * :exc:`IOError` used to be raised, it is now an alias of :exc:`OSError`.
   * :exc:`FileExistsError` is now raised if the file opened in exclusive
     creation mode (``'x'``) already exists.

.. versionchanged:: 3.4

   * The file is now non-inheritable.

.. versionchanged:: 3.5

   * If the system call is interrupted and the signal handler does not raise an
     exception, the function now retries the system call instead of raising an
     :exc:`InterruptedError` exception (see :pep:`475` for the rationale).
   * The ``'namereplace'`` error handler was added.

.. versionchanged:: 3.6

   * Support added to accept objects implementing :class:`os.PathLike`.
   * On Windows, opening a console buffer may return a subclass of
     :class:`io.RawIOBase` other than :class:`io.FileIO`.

.. versionchanged:: 3.11
   The ``'U'`` mode has been removed.

.. versionchanged:: 3.15
   UTF-8 is now the default encoding, instead of the
   platform-dependent locale encoding (:pep:`686`).

```

### Function: `ord(character, /)`

   Return the ordinal value of a character.

   If the argument is a one-character string, return the Unicode code point
   of that character.  For example,
   `ord('a')` returns the integer `97` and `ord('€')` (Euro sign)
   returns `8364`.  This is the inverse of `chr()`.

   If the argument is a `class` or `class` object of
   length 1, return its single byte value.
   For example, `ord(b'a')` returns the integer `97`.

### Function: `pow(base, exp, mod=None)`

   Return *base* to the power *exp*; if *mod* is present, return *base* to the
   power *exp*, modulo *mod* (computed more efficiently than
   `pow(base, exp) % mod`). The two-argument form `pow(base, exp)` is
   equivalent to using the power operator: `base**exp`.

   When arguments are builtin numeric types with mixed operand types, the
   coercion rules for binary arithmetic operators apply.  For `class`
   operands, the result has the same type as the operands (after coercion)
   unless the second argument is negative; in that case, all arguments are
   converted to float and a float result is delivered.  For example, `pow(10, 2)`
   returns `100`, but `pow(10, -2)` returns `0.01`.  For a negative base of
   type `class` or `class` and a non-integral exponent, a complex
   result is delivered.  For example, `pow(-9, 0.5)` returns a value close
   to `3j`. Whereas, for a negative base of type `class` or `class`
   with an integral exponent, a float result is delivered. For example,
   `pow(-9, 2.0)` returns `81.0`.

   For `class` operands *base* and *exp*, if *mod* is present, *mod* must
   also be of integer type and *mod* must be nonzero. If *mod* is present and
   *exp* is negative, *base* must be relatively prime to *mod*. In that case,
   `pow(inv_base, -exp, mod)` is returned, where *inv_base* is an inverse to
   *base* modulo *mod*.

Here's an example of computing an inverse for ``38`` modulo ``97``

```python

   >>> pow(38, -1, mod=97)
   23
   >>> 23 * 38 % 97 == 1
   True

.. versionchanged:: 3.8
   For :class:`int` operands, the three-argument form of ``pow`` now allows
   the second argument to be negative, permitting computation of modular
   inverses.

.. versionchanged:: 3.8
   Allow keyword arguments.  Formerly, only positional arguments were
   supported.

```

### Function: `print(*objects, sep=' ', end='\n', file=None, flush=False)`

   Print *objects* to the text stream *file*, separated by *sep* and followed
   by *end*.  *sep*, *end*, *file*, and *flush*, if present, must be given as keyword
   arguments.

   All non-keyword arguments are converted to strings like `str()` does and
   written to the stream, separated by *sep* and followed by *end*.  Both *sep*
   and *end* must be strings; they can also be `None`, which means to use the
   default values.  If no *objects* are given, `print()` will just write
   *end*.

   The *file* argument must be an object with a `write(string)` method; if it
   is not present or `None`, `data` will be used.  Since printed
   arguments are converted to text strings, `print()` cannot be used with
   binary mode file objects.  For these, use `file.write(...)` instead.

   Output buffering is usually determined by *file*.
   However, if *flush* is true, the stream is forcibly flushed.

   .. versionchanged:: 3.3
      Added the *flush* keyword argument.

### Class: `property(fget=None, fset=None, fdel=None, doc=None)`

   Return a property attribute.

   *fget* is a function for getting an attribute value.  *fset* is a function
   for setting an attribute value. *fdel* is a function for deleting an attribute
   value.  And *doc* creates a docstring for the attribute.

A typical use is to define a managed attribute ``x``

```python

   class C:
       def __init__(self):
           self._x = None

       def getx(self):
           return self._x

       def setx(self, value):
           self._x = value

       def delx(self):
           del self._x

       x = property(getx, setx, delx, "I'm the 'x' property.")

If *c* is an instance of *C*, ``c.x`` will invoke the getter,
``c.x = value`` will invoke the setter, and ``del c.x`` the deleter.

If given, *doc* will be the docstring of the property attribute. Otherwise, the
property will copy *fget*'s docstring (if it exists).  This makes it possible to
create read-only properties easily using :deco:`property` as a :term:`decorator`::

   class Parrot:
       def __init__(self):
           self._voltage = 100000

       @property
       def voltage(self):
           """Get the current voltage."""
           return self._voltage

The ``@property`` decorator turns the :meth:`!voltage` method into a "getter"
for a read-only attribute with the same name, and it sets the docstring for
*voltage* to "Get the current voltage."

.. decorator:: property.getter
.. decorator:: property.setter
.. decorator:: property.deleter

   A property object has ``getter``, ``setter``,
   and ``deleter`` methods usable as decorators that create a
   copy of the property with the corresponding accessor function set to the
   decorated function.  This is best explained with an example:

   .. testcode::

      class C:
          def __init__(self):
              self._x = None

          @property
          def x(self):
              """I'm the 'x' property."""
              return self._x

          @x.setter
          def x(self, value):
              self._x = value

          @x.deleter
          def x(self):
              del self._x

   This code is exactly equivalent to the first example.  Be sure to give the
   additional functions the same name as the original property (``x`` in this
   case.)

   The returned property object also has the attributes ``fget``, ``fset``, and
   ``fdel`` corresponding to the constructor arguments.

.. versionchanged:: 3.5
   The docstrings of property objects are now writeable.

.. attribute:: __name__

   Attribute holding the name of the property. The name of the property
   can be changed at runtime.

   .. versionadded:: 3.13

```

### Class: `range(stop, /)`

           range(start, stop, step=1, /)

   Rather than being a function, `class` is actually an immutable
   sequence type, as documented in `ref` and `ref`.

### Function: `repr(object, /)`

   Return a string containing a printable representation of an object.  For many
   types, this function makes an attempt to return a string that would yield an
   object with the same value when passed to `eval()`; otherwise, the
   representation is a string enclosed in angle brackets that contains the name
   of the type of the object together with additional information often
   including the name and address of the object.  A class can control what this
   function returns for its instances
   by defining a `object.__repr__()` method.

This class has a custom representation that can be evaluated

```python

   class Person:
      def __init__(self, name, age):
         self.name = name
         self.age = age

      def __repr__(self):
         return f"Person({self.name!r}, {self.age!r})"

```

### Function: `reversed(object, /)`

   Return a reverse `term`.  The argument must be an object which has
   a `object.__reversed__()` method or supports the sequence protocol (the
   `object.__len__()` method and the `object.__getitem__()` method
   with integer arguments starting at `0`).

### Function: `round(number, ndigits=None)`

   Return *number* rounded to *ndigits* precision after the decimal
   point.  If *ndigits* is omitted or is `None`, it returns the
   nearest integer to its input.

   For the built-in types supporting `round()`, values are rounded to the
   closest multiple of 10 to the power minus *ndigits*; if two multiples are
   equally close, rounding is done toward the even choice (so, for example,
   both `round(0.5)` and `round(-0.5)` are `0`, and `round(1.5)` is
   `2`).  Any integer value is valid for *ndigits* (positive, zero, or
   negative).  The return value is an integer if *ndigits* is omitted or
   `None`.
   Otherwise, the return value has the same type as *number*.

   For a general Python object `number`, `round` delegates to
   `number.__round__`.

.. note

```python

   The behavior of :func:`round` for floats can be surprising: for example,
   ``round(2.675, 2)`` gives ``2.67`` instead of the expected ``2.68``.
   This is not a bug: it's a result of the fact that most decimal fractions
   can't be represented exactly as a float.  See :ref:`tut-fp-issues` for
   more information.

```

### Class: `set(iterable=(), /)`

   Return a new `class` object, optionally with elements taken from
   *iterable*.  `class` is a built-in class.  See also
   `ref` for documentation about this class.

   For other containers see the built-in `class`, `class`,
   `class`, and `class` classes, as well as the `mod`
   module.

### Function: `setattr(object, name, value, /)`

   This is the counterpart of `getattr()`.  The arguments are an object, a
   string, and an arbitrary value.  The string may name an existing attribute or a
   new attribute.  The function assigns the value to the attribute, provided the
   object allows it.  For example, `setattr(x, 'foobar', 123)` is equivalent to
   `x.foobar = 123`.

   *name* need not be a Python identifier as defined in `ref`
   unless the object chooses to enforce that, for example in a custom
   `object.__getattribute__()` or via :attr:`~object.__slots__`.
   An attribute whose name is not an identifier will not be accessible using
   the dot notation, but is accessible through `getattr()` etc..

.. note

```python

   Since :ref:`private name mangling <private-name-mangling>` happens at
   compilation time, one must manually mangle a private attribute's
   (attributes with two leading underscores) name in order to set it with
   :func:`setattr`.

```

### Class: `sentinel(name, /, *, repr=None)`

   Return a new unique sentinel object.  *name* must be a `class`, and is
used by default as the returned object's representation

```python

   >>> MISSING = sentinel("MISSING")
   >>> MISSING
   MISSING

The optional *repr* argument can be used to specify a different representation::

   >>> MISSING = sentinel("MISSING", repr="<MISSING>")
   >>> MISSING
   <MISSING>

Sentinel objects are true and compare equal only to themselves.  They are
intended to be compared with the :keyword:`is` operator.

``sentinel`` does not support subclassing.

Shallow and deep copies of a sentinel object return the object itself.

Sentinels are conventionally assigned to a variable with a matching name.
Sentinels defined in this way can be used in :term:`type hints <type hint>`::

   MISSING = sentinel("MISSING")

   def next_value(default: int | MISSING = MISSING):
       ...

Sentinel objects support the :ref:`| <bitwise>` operator for use in type expressions.

:mod:`Pickling <pickle>` is supported for sentinel objects that are
placed in the global scope of a module under a name matching the sentinel's
name, and for sentinels placed in class scopes with a name matching the
:term:`qualified name` of the sentinel. Other sentinels, such as those
defined in a function scope, are not picklable. The identity of the sentinel is preserved
after pickling::

   import pickle

   PICKLABLE = sentinel("PICKLABLE")

   assert pickle.loads(pickle.dumps(PICKLABLE)) is PICKLABLE

   class Cls:
       PICKLABLE = sentinel("Cls.PICKLABLE")

   assert pickle.loads(pickle.dumps(Cls.PICKLABLE)) is Cls.PICKLABLE

Sentinel objects have the following attributes:

.. attribute:: __name__

   The sentinel's name.

.. attribute:: __module__

   The name of the module where the sentinel was created. This attribute is writable.

.. versionadded:: 3.15

```

### Class: `slice(stop, /)`

           slice(start, stop, step=None, /)

   Return a `term` object representing the set of indices specified by
   `range(start, stop, step)`.  The *start* and *step* arguments default to
   `None`.

   Slice objects are also generated when `ref`
   is used.  For example: `a[start:stop:step]` or `a[start:stop, i]`.

   See `itertools.islice()` for an alternate version that returns an
   `term`.

   .. attribute:: slice.start
                  slice.stop
                  slice.step

      These read-only attributes are set to the argument values
      (or their default).  They have no other explicit functionality;
      however, they are used by NumPy and other third-party packages.

   .. versionchanged:: 3.12
      Slice objects are now `term` (provided :attr:`~slice.start`,
      :attr:`~slice.stop`, and :attr:`~slice.step` are hashable).

### Function: `sorted(iterable, /, *, key=None, reverse=False)`

   Return a new sorted list from the items in *iterable*.

   Has two optional arguments which must be specified as keyword arguments.

   *key* specifies a function of one argument that is used to extract a comparison
   key from each element in *iterable* (for example, `key=str.lower`).  The
   default value is `None` (compare the elements directly).

   *reverse* is a boolean value.  If set to `True`, then the list elements are
   sorted as if each comparison were reversed.

   Use `functools.cmp_to_key()` to convert an old-style *cmp* function to a
   *key* function.

   The built-in `sorted()` function is guaranteed to be stable. A sort is
   stable if it guarantees not to change the relative order of elements that
   compare equal --- this is helpful for sorting in multiple passes (for
   example, sort by department, then by salary grade).

   The sort algorithm uses only `<` comparisons between items.  While
   defining an `object.__lt__()` method will suffice for sorting,
   :PEP:`8` recommends that all six :ref:`rich comparisons
   <comparisons>` be implemented.  This will help avoid bugs when using
   the same data with other ordering tools such as `max()` that rely
   on a different underlying method.  Implementing all six comparisons
   also helps avoid confusion for mixed type comparisons which can call
   the reflected `object.__gt__()` method.

   For sorting examples and a brief sorting tutorial, see `ref`.

   Transform a method into a static method.

   A static method does not receive an implicit first argument. To declare a static
method, use this idiom

```python

   class C:
       @staticmethod
       def f(arg1, arg2, argN): ...

The ``@staticmethod`` form is a function :term:`decorator` -- see
:ref:`function` for details.

A static method can be called either on the class (such as ``C.f()``) or on
an instance (such as ``C().f()``).
Moreover, the static method :term:`descriptor` is also callable, so it can
be used in the class definition (such as ``f()``).

Static methods in Python are similar to those found in Java or C++. Also, see
:deco:`classmethod` for a variant that is useful for creating alternate class
constructors.

Like all decorators, it is also possible to call ``staticmethod`` as
a regular function and do something with its result.  This is needed
in some cases where you need a reference to a function from a class
body and you want to avoid the automatic transformation to instance
method.  For these cases, use this idiom::

   def regular_function():
       ...

   class C:
       method = staticmethod(regular_function)

For more information on static methods, see :ref:`types`.

.. versionchanged:: 3.10
   Static methods now inherit the method attributes
   (:attr:`~function.__module__`, :attr:`~function.__name__`,
   :attr:`~function.__qualname__`, :attr:`~function.__doc__` and
   :attr:`~function.__annotations__`), have a new ``__wrapped__`` attribute,
   and are now callable as regular functions.

```

.. index

```python
single: string; str() (built-in function)

```

### Class: `str(*, encoding='utf-8', errors='strict')`

           str(object)
           str(object, encoding, errors='strict')
           str(object, *, errors)

   Return a `class` version of *object*.  See `str()` for details.

   `str` is the built-in string `term`.  For general information
   about strings, see `ref`.

### Function: `sum(iterable, /, start=0)`

   Sums *start* and the items of an *iterable* from left to right and returns the
   total.  The *iterable*'s items are normally numbers, and the start value is not
   allowed to be a string.

   For some use cases, there are good alternatives to `sum()`.
   The preferred, fast way to concatenate a sequence of strings is by calling
   `''.join(sequence)`.  To add floating-point values with extended precision,
   see `math.fsum()`\.  To concatenate a series of iterables, consider using
   `itertools.chain()`.

   .. versionchanged:: 3.8
      The *start* parameter can be specified as a keyword argument.

   .. versionchanged:: 3.12 Summation of floats switched to an algorithm
      that gives higher accuracy and better commutativity on most builds.

   .. versionchanged:: 3.14
      Added specialization for summation of complexes,
      using same algorithm as for summation of floats.

### Class: `super()`

           super(type, object_or_type=None, /)

   Return a proxy object that delegates method calls to a parent or sibling
   class of *type*.  This is useful for accessing inherited methods that have
   been overridden in a class.

   The *object_or_type* determines the `term`
   to be searched.  The search starts from the class right after the
   *type*.

   For example, if :attr:`~type.__mro__` of *object_or_type* is
   `D -> B -> C -> A -> object` and the value of *type* is `B`,
   then `super()` searches `C -> A -> object`.

   The :attr:`~type.__mro__` attribute of the class corresponding to
   *object_or_type* lists the method resolution search order used by both
   `getattr()` and `super()`.  The attribute is dynamic and can change
   whenever the inheritance hierarchy is updated.

   If the second argument is omitted, the super object returned is unbound.  If
   the second argument is an object, `isinstance(obj, type)` must be true.  If
   the second argument is a type, `issubclass(type2, type)` must be true (this
   is useful for classmethods).

   When called directly within an ordinary method of a class, both arguments may
   be omitted ("zero-argument `!super()`"). In this case, *type* will be the
   enclosing class, and *object_or_type* will be the first argument of the
   immediately enclosing function (typically `self`). Zero-argument
   `!super()` will not work as expected within nested functions, including
   generator expressions, which implicitly create nested functions.

   There are two typical use cases for *super*.  In a class hierarchy with
   single inheritance, *super* can be used to refer to parent classes without
   naming them explicitly, thus making the code more maintainable.  This use
   closely parallels the use of *super* in other programming languages.

   The second use case is to support cooperative multiple inheritance in a
   dynamic execution environment.  This use case is unique to Python and is
   not found in statically compiled languages or languages that only support
   single inheritance.  This makes it possible to implement "diamond diagrams"
   where multiple base classes implement the same method.  Good design dictates
   that such implementations have the same calling signature in every case (because the
   order of calls is determined at runtime, because that order adapts
   to changes in the class hierarchy, and because that order can include
   sibling classes that are unknown prior to runtime).

For both use cases, a typical superclass call looks like this

```python

   class C(B):
       def method(self, arg):
           super().method(arg)    # This does the same thing as:
                                  # super(C, self).method(arg)

In addition to method lookups, :func:`super` also works for attribute
lookups.  One possible use case for this is calling :term:`descriptors <descriptor>`
in a parent or sibling class.

Note that :func:`super` is implemented as part of the binding process for
explicit dotted attribute lookups such as ``super().__getitem__(name)``.
It does so by implementing its own :meth:`~object.__getattribute__` method
for searching
classes in a predictable order that supports cooperative multiple inheritance.
Accordingly, :func:`super` is undefined for implicit lookups using statements or
operators such as ``super()[name]``.

Also note that, aside from the zero argument form, :func:`super` is not
limited to use inside methods.  The two argument form specifies the
arguments exactly and makes the appropriate references.  The zero
argument form only works inside a class definition, as the compiler fills
in the necessary details to correctly retrieve the class being defined,
as well as accessing the current instance for ordinary methods.

For practical suggestions on how to design cooperative classes using
:func:`super`, see `guide to using super()
<https://rhettinger.wordpress.com/2011/05/26/super-considered-super/>`_.

.. versionchanged:: 3.14
  :class:`super` objects are now :mod:`pickleable <pickle>` and
   :mod:`copyable <copy>`.

```

### Class: `tuple(iterable=(), /)`

   Rather than being a function, `class` is actually an immutable
   sequence type, as documented in `ref` and `ref`.

### Class: `type(object, /)`

           type(name, bases, dict, /, **kwargs)

   .. index:: pair: object; type

   With one argument, return the type of an *object*.  The return value is a
   type object and generally the same object as returned by
   :attr:`object.__class__`.

   The `isinstance()` built-in function is recommended for testing the type
   of an object, because it takes subclasses into account.

   With three arguments, return a new type object.  This is essentially a
   dynamic form of the :keyword:`class` statement. The *name* string is
   the class name and becomes the :attr:`~type.__name__` attribute.
   The *bases* tuple contains the base classes and becomes the
   :attr:`~type.__bases__` attribute; if empty, `class`, the
   ultimate base of all classes, is added.  The *dict* dictionary contains
   attribute and method definitions for the class body; it may be copied
   or wrapped before becoming the :attr:`~type.__dict__` attribute.
   The following two statements create identical `class` objects:

      >>> class X:
      ...     a = 1
      ...
      >>> X = type('X', (), dict(a=1))

   See also:

   * `ref`.
   * `ref`

   Keyword arguments provided to the three argument form are passed to the
   appropriate metaclass machinery (usually `object.__init_subclass__()`)
   in the same way that keywords in a class
   definition (besides *metaclass*) would.

   Unlike a :keyword:`class` statement, the three argument form does not
   call the metaclass `__prepare__` method (see `ref`).  Use
   `types.new_class()` to dynamically create a class using the
   appropriate metaclass.

   See also `ref`.

   .. versionchanged:: 3.6
      Subclasses of `class` which don't override `type.__new__` may no
      longer use the one-argument form to get the type of an object.

   .. versionchanged:: 3.15

      *dict* can now be a `class`.

### Function: `vars()`

              vars(object, /)

   Return the :attr:`~object.__dict__` attribute for a module, class, instance,
   or any other object with a :attr:`!__dict__` attribute.

   Objects such as modules and instances have an updateable :attr:`~object.__dict__`
   attribute; however, other objects may have write restrictions on their
   :attr:`!__dict__` attributes (for example, classes use a
   `class` to prevent direct dictionary updates).

   Without an argument, `vars()` acts like `locals()`.

   A `exc` exception is raised if an object is specified but
   it doesn't have a :attr:`~object.__dict__` attribute (for example, if
   its class defines the :attr:`~object.__slots__` attribute).

   .. versionchanged:: 3.13

      The result of calling this function without an argument has been
      updated as described for the `locals()` builtin.

### Function: `zip(*iterables, strict=False)`

   Iterate over several iterables in parallel, producing tuples with an item
   from each one.

Example

```python

   >>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
   ...     print(item)
   ...
   (1, 'sugar')
   (2, 'spice')
   (3, 'everything nice')

More formally: :func:`zip` returns an iterator of tuples, where the *i*-th
tuple contains the *i*-th element from each of the argument iterables.

Another way to think of :func:`zip` is that it turns rows into columns, and
columns into rows.  This is similar to `transposing a matrix
<https://en.wikipedia.org/wiki/Transpose>`_.

:func:`zip` is lazy: The elements won't be processed until the iterable is
iterated on, e.g. by a :keyword:`!for` loop or by wrapping in a
:class:`list`.

One thing to consider is that the iterables passed to :func:`zip` could have
different lengths; sometimes by design, and sometimes because of a bug in
the code that prepared these iterables.  Python offers three different
approaches to dealing with this issue:

* By default, :func:`zip` stops when the shortest iterable is :term:`exhausted`.
  It will ignore the remaining items in the longer iterables, cutting off
  the result to the length of the shortest iterable::

     >>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
     [(0, 'fee'), (1, 'fi'), (2, 'fo')]

* :func:`zip` is often used in cases where the iterables are assumed to be
  of equal length.  In such cases, it's recommended to use the ``strict=True``
  option. Its output is the same as regular :func:`zip`::

     >>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
     [('a', 1), ('b', 2), ('c', 3)]

  Unlike the default behavior, it raises a :exc:`ValueError` if one iterable
  is :term:`exhausted` before the others:

     >>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):  # doctest: +SKIP
     ...     print(item)
     ...
     (0, 'fee')
     (1, 'fi')
     (2, 'fo')
     Traceback (most recent call last):
       ...
     ValueError: zip() argument 2 is longer than argument 1

  ..
     This doctest is disabled because doctest does not support capturing
     output and exceptions in the same code unit.
     https://github.com/python/cpython/issues/65382

  Without the ``strict=True`` argument, any bug that results in iterables of
  different lengths will be silenced, possibly manifesting as a hard-to-find
  bug in another part of the program.

* Shorter iterables can be padded with a constant value to make all the
  iterables have the same length.  This is done by
  :func:`itertools.zip_longest`.

Edge cases: With a single iterable argument, :func:`zip` returns an
iterator of 1-tuples.  With no arguments, it returns an empty iterator.

Tips and tricks:

* The left-to-right evaluation order of the iterables is guaranteed. This
  makes possible an idiom for clustering a data series into n-length groups
  using ``zip(*[iter(s)]*n, strict=True)``.  This repeats the *same* iterator
  ``n`` times so that each output tuple has the result of ``n`` calls to the
  iterator. This has the effect of dividing the input into n-length chunks.

* :func:`zip` in conjunction with the ``*`` operator can be used to unzip a
  list::

     >>> x = [1, 2, 3]
     >>> y = [4, 5, 6]
     >>> list(zip(x, y))
     [(1, 4), (2, 5), (3, 6)]
     >>> x2, y2 = zip(*zip(x, y))
     >>> x == list(x2) and y == list(y2)
     True

.. versionchanged:: 3.10
   Added the ``strict`` argument.

```

### Function: `__import__(name, globals=None, locals=None, fromlist=(), level=0)`

.. index

```python
   pair: statement; import
   pair: module; builtins

.. note::

   This is an advanced function that is not needed in everyday Python
   programming, unlike :func:`importlib.import_module`.

This function is invoked by the :keyword:`import` statement.  It can be
replaced (by importing the :mod:`builtins` module and assigning to
``builtins.__import__``) in order to change semantics of the
:keyword:`!import` statement, but doing so is **strongly** discouraged as it
is usually simpler to use import hooks (see :pep:`302`) to attain the same
goals and does not cause issues with code which assumes the default import
implementation is in use.  Direct use of :func:`__import__` is also
discouraged in favor of :func:`importlib.import_module`.

The function imports the module *name*, potentially using the given *globals*
and *locals* to determine how to interpret the name in a package context.
The *fromlist* gives the names of objects or submodules that should be
imported from the module given by *name*.  The standard implementation does
not use its *locals* argument at all and uses its *globals* only to
determine the package context of the :keyword:`import` statement.

*level* specifies whether to use absolute or relative imports. ``0`` (the
default) means only perform absolute imports.  For relative imports,
``1`` refers to the current package, ``2`` to its parent package, and so on
(see :pep:`328` for details).

When the *name* variable is of the form ``package.module``, normally, the
top-level package (the name up till the first dot) is returned, *not* the
module named by *name*.  However, when a non-empty *fromlist* argument is
given, the module named by *name* is returned.

For example, the statement ``import spam`` results in bytecode resembling the
following code::

   spam = __import__('spam', globals(), locals(), [], 0)

The statement ``import spam.ham`` results in this call::

   spam = __import__('spam.ham', globals(), locals(), [], 0)

Note how :func:`__import__` returns the toplevel module here because this is
the object that is bound to a name by the :keyword:`import` statement.

On the other hand, the statement ``from spam.ham import eggs, sausage as
saus`` results in ::

   _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
   eggs = _temp.eggs
   saus = _temp.sausage

Here, the ``spam.ham`` module is returned from :func:`__import__`.  From this
object, the names to import are retrieved and assigned to their respective
names.

If you simply want to import a module (potentially within a package) by name,
use :func:`importlib.import_module`.

.. versionchanged:: 3.3
   Negative values for *level* are no longer supported (which also changes
   the default value to 0).

.. versionchanged:: 3.9
   When the command line options :option:`-E` or :option:`-I` are being used,
   the environment variable :envvar:`PYTHONCASEOK` is now ignored.

```

**************

## Built-in Types

The following sections describe the standard types that are built into the
interpreter.

The principal built-in types are numerics, sequences, mappings, classes,
instances and exceptions.

Some collection classes are mutable.  The methods that add, subtract, or
rearrange their members in place, and don't return a specific item, never return
the collection instance itself but `None`.

Some operations are supported by several object types; in particular,
practically all objects can be compared for equality, tested for truth
value, and converted to a string (with the `repr()` function or the
slightly different `str()` function).  The latter function is implicitly
used when an object is written by the `print()` function.

## Truth Value Testing

.. index

```python
pair: statement; if
pair: statement; while
pair: truth; value
pair: Boolean; operations
single: false

```

Any object can be tested for truth value, for use in an :keyword:`if` or
:keyword:`while` condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a
`object.__bool__()` method that returns `False` or a
`object.__len__()` method that
returns zero, when called with the object. [1]_ If one of the methods raises an
exception when called, the exception is propagated and the object does
not have a truth value (for example, `data`).
Here are most of the built-in objects considered false:

.. index

```python
single: None (Built-in object)
single: False (Built-in object)

```

* constants defined to be false: `None` and `False`

* zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`,
  `Fraction(0, 1)`

* empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`,
  `range(0)`

.. index

```python
pair: operator; or
pair: operator; and
single: False
single: True

```

Operations and built-in functions that have a Boolean result always return `0`
or `False` for false and `1` or `True` for true, unless otherwise stated.
(Important exception: the Boolean operations `or` and `and` always return
one of their operands.)

## Boolean Operations --- :keyword:`!and`, :keyword:`!or`, :keyword:`!not`

These are the Boolean operations, ordered by ascending priority:

+-------------+---------------------------------+-------+
| Operation   | Result                          | Notes |
+=============+=================================+=======+
| `x or y`  | if *x* is true, then *x*, else  | \(1)  |
|             | *y*                             |       |
+-------------+---------------------------------+-------+
| `x and y` | if *x* is false, then *x*, else | \(2)  |
|             | *y*                             |       |
+-------------+---------------------------------+-------+
| `not x`   | if *x* is false, then `True`, | \(3)  |
|             | else `False`                  |       |
+-------------+---------------------------------+-------+

.. index

```python
pair: operator; and
pair: operator; or
pair: operator; not

```

Notes:

(1)
   This is a short-circuit operator, so it only evaluates the second
   argument if the first one is false.

(2)
   This is a short-circuit operator, so it only evaluates the second
   argument if the first one is true.

(3)
   `not` has a lower priority than non-Boolean operators, so `not a == b` is
   interpreted as `not (a == b)`, and `a == not b` is a syntax error.

## Comparisons

.. index

```python
pair: chaining; comparisons
pair: operator; comparison
pair: operator; ==
pair: operator; < (less)
pair: operator; <=
pair: operator; > (greater)
pair: operator; >=
pair: operator; !=
pair: operator; is
pair: operator; is not

```

There are eight comparison operations in Python.  They all have the same
priority (which is higher than that of the Boolean operations).  Comparisons can
be chained arbitrarily; for example, `x < y <= z` is equivalent to ``x < y and
y <= z``, except that *y* is evaluated only once (but in both cases *z* is not
evaluated at all when `x < y` is found to be false).

This table summarizes the comparison operations:

+------------+-------------------------+
| Operation  | Meaning                 |
+============+=========================+
| `<`      | strictly less than      |
+------------+-------------------------+
| `<=`     | less than or equal      |
+------------+-------------------------+
| `>`      | strictly greater than   |
+------------+-------------------------+
| `>=`     | greater than or equal   |
+------------+-------------------------+
| `==`     | equal                   |
+------------+-------------------------+
| `!=`     | not equal               |
+------------+-------------------------+
| `is`     | object identity         |
+------------+-------------------------+
| `is not` | negated object identity |
+------------+-------------------------+

.. index

```python
pair: object; numeric
pair: objects; comparing

```

Unless stated otherwise, objects of different types never compare equal.
The `==` operator is always defined but for some object types (for example,
class objects) is equivalent to :keyword:`is`. The `<`, `<=`, `>` and `>=`
operators are only defined where they make sense; for example, they raise a
`exc` exception when one of the arguments is a complex number.

.. index

```python
single: __eq__() (instance method)
single: __ne__() (instance method)
single: __lt__() (instance method)
single: __le__() (instance method)
single: __gt__() (instance method)
single: __ge__() (instance method)

```

Non-identical instances of a class normally compare as non-equal unless the
class defines the `object.__eq__()` method.

Instances of a class cannot be ordered with respect to other instances of the
same class, or other types of object, unless the class defines enough of the
methods `object.__lt__()`, `object.__le__()`, `object.__gt__()`, and
`object.__ge__()` (in general, `object.__lt__()` and
`object.__eq__()` are sufficient, if you want the conventional meanings of the
comparison operators).

The behavior of the :keyword:`is` and :keyword:`is not` operators cannot be
customized; also they can be applied to any two objects and never raise an
exception.

.. index

```python
pair: operator; in
pair: operator; not in

```

Two more operations with the same syntactic priority, :keyword:`in` and
:keyword:`not in`, are supported by types that are `term` or
implement the `object.__contains__()` method.

## Numeric Types --- :class:`int`, :class:`float`, :class:`complex`

.. index

```python
pair: object; numeric
pair: object; Boolean
pair: object; integer
pair: object; floating-point
pair: object; complex number
pair: C; language

```

There are three distinct numeric types: :dfn:`integers`, :dfn:`floating-point
numbers`, and :dfn:`complex numbers`.  In addition, Booleans are a
subtype of integers.  Integers have unlimited precision.  Floating-point
numbers are usually implemented using :c:expr:`double` in C; information
about the precision and internal representation of floating-point
numbers for the machine on which your program is running is available
in `data`.  Complex numbers have a real and imaginary
part, which are each a floating-point number.  To extract these parts
from a complex number *z*, use `z.real` and `z.imag`. (The standard
library includes the additional numeric types `mod`, for
rationals, and `mod`, for floating-point numbers with
user-definable precision.)

.. index

```python
pair: numeric; literals
pair: integer; literals
pair: floating-point; literals
pair: complex number; literals
pair: hexadecimal; literals
pair: octal; literals
pair: binary; literals

```

Numbers are created by numeric literals or as the result of built-in functions
and operators.  Unadorned integer literals (including hex, octal and binary
numbers) yield integers.  Numeric literals containing a decimal point or an
exponent sign yield floating-point numbers.  Appending `'j'` or `'J'` to a
numeric literal yields an imaginary number (a complex number with a zero real
part) which you can add to an integer or float to get a complex number with real
and imaginary parts.

The constructors `int()`, `float()`, and
`complex()` can be used to produce numbers of a specific type.

.. index

```python
single: arithmetic
pair: built-in function; int
pair: built-in function; float
pair: built-in function; complex
single: operator; + (plus)
single: + (plus); unary operator
single: + (plus); binary operator
single: operator; - (minus)
single: - (minus); unary operator
single: - (minus); binary operator
pair: operator; * (asterisk)
pair: operator; / (slash)
pair: operator; //
pair: operator; % (percent)
pair: operator; **

```

Python fully supports mixed arithmetic: when a binary arithmetic operator has
operands of different built-in numeric types, the operand with the "narrower"
type is widened to that of the other:

* If both arguments are complex numbers, no conversion is performed;
* if either argument is a complex or a floating-point number, the other is
  converted to a floating-point number;
* otherwise, both must be integers and no conversion is necessary.

Arithmetic with complex and real operands is defined by the usual mathematical
formula, for example

```python

 x + complex(u, v) = complex(x + u, v)
 x * complex(u, v) = complex(x * u, x * v)

```

A comparison between numbers of different types behaves as though the exact
values of those numbers were being compared. [2]_

All numeric types (except complex) support the following operations (for priorities of
the operations, see `ref`):

+---------------------+---------------------------------+---------+--------------------+
| Operation           | Result                          | Notes   | Full documentation |
+=====================+=================================+=========+====================+
| `x + y`           | sum of *x* and *y*              |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `x - y`           | difference of *x* and *y*       |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `x * y`           | product of *x* and *y*          |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `x / y`           | quotient of *x* and *y*         |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `x // y`          | floored quotient of *x* and     | \(1)\(2)|                    |
|                     | *y*                             |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `x % y`           | remainder of `x / y`          | \(2)    |                    |
+---------------------+---------------------------------+---------+--------------------+
| `-x`              | *x* negated                     |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `+x`              | *x* unchanged                   |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `abs(x)`          | absolute value or magnitude of  |         | `abs()`        |
|                     | *x*                             |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `int(x)`          | *x* converted to integer        | \(3)\(6)| `int()`        |
+---------------------+---------------------------------+---------+--------------------+
| `float(x)`        | *x* converted to floating point | \(4)\(6)| `float()`      |
+---------------------+---------------------------------+---------+--------------------+
| `complex(re, im)` | a complex number with real part | \(6)    | `complex()`    |
|                     | *re*, imaginary part *im*.      |         |                    |
|                     | *im* defaults to zero.          |         |                    |
+---------------------+---------------------------------+---------+--------------------+
|  `c.conjugate()`  | conjugate of the complex number |         |                    |
|                     | *c*                             |         |                    |
+---------------------+---------------------------------+---------+--------------------+
| `divmod(x, y)`    | the pair `(x // y, x % y)`    | \(2)    | `divmod()`     |
+---------------------+---------------------------------+---------+--------------------+
| `pow(x, y)`       | *x* to the power *y*            | \(5)    | `pow()`        |
+---------------------+---------------------------------+---------+--------------------+
| `x ** y`          | *x* to the power *y*            | \(5)    |                    |
+---------------------+---------------------------------+---------+--------------------+

.. index

```python
triple: operations on; numeric; types
single: conjugate() (complex number method)

```

Notes:

(1)
   Also referred to as integer division.  For operands of type `class`,
   the result has type `class`.  For operands of type `class`,
   the result has type `class`.  In general, the result is a whole
   integer, though the result's type is not necessarily `class`.  The result is
   always rounded towards minus infinity: `1//2` is `0`, `(-1)//2` is
   `-1`, `1//(-2)` is `-1`, and `(-1)//(-2)` is `0`.

(2)
   Not for complex numbers.  Instead convert to floats using `abs()` if
   appropriate.

(3)
.. index

```python
   pair: module; math
   single: floor() (in module math)
   single: ceil() (in module math)
   single: trunc() (in module math)
   pair: numeric; conversions

Conversion from :class:`float` to :class:`int` truncates, discarding the
fractional part. See functions :func:`math.floor` and :func:`math.ceil` for
alternative conversions.

```

(4)
   float also accepts the strings "nan" and "inf" with an optional prefix "+"
   or "-" for Not a Number (NaN) and positive or negative infinity.

(5)
   Python defines `pow(0, 0)` and `0 ** 0` to be `1`, as is common for
   programming languages.

(6)
   The numeric literals accepted include the digits `0` to `9` or any
   Unicode equivalent (code points with the `Nd` property).

   See `the Unicode Standard <https://unicode.org/Public/UNIDATA/extracted/DerivedNumericType.txt>`_
   for a complete list of code points with the `Nd` property.

All `class` types (`class` and `class`) also include
the following operations:

+--------------------+---------------------------------------------+
| Operation          | Result                                      |
+====================+=============================================+
| `math.trunc(\| *x* truncated to :class:()`~numbers.Integral` |
| x) <math.trunc>`   |                                             |
+--------------------+---------------------------------------------+
| :func:`round(x[,   | *x* rounded to *n* digits,                  |
| n]) <round>`       | rounding half to even. If *n* is            |
|                    | omitted, it defaults to 0.                  |
+--------------------+---------------------------------------------+
| `math.floor(\| the greatest :class:()`~numbers.Integral`     |
| x) <math.floor>`   | <= *x*                                      |
+--------------------+---------------------------------------------+
| `math.ceil(x)| the least :class:()`~numbers.Integral` >= *x* |
| <math.ceil>`       |                                             |
+--------------------+---------------------------------------------+

For additional numeric operations see the `mod` and `mod`
modules.

### Bitwise Operations on Integer Types

.. index

```python
triple: operations on; integer; types
pair: bitwise; operations
pair: shifting; operations
pair: masking; operations
pair: operator; | (vertical bar)
pair: operator; ^ (caret)
pair: operator; & (ampersand)
pair: operator; <<
pair: operator; >>
pair: operator; ~ (tilde)

```

Bitwise operations only make sense for integers. The result of bitwise
operations is calculated as though carried out in two's complement with an
infinite number of sign bits.

The priorities of the binary bitwise operations are all lower than the numeric
operations and higher than the comparisons; the unary operation `~` has the
same priority as the other unary numeric operations (`+` and `-`).

This table lists the bitwise operations sorted in ascending priority:

+------------+--------------------------------+----------+
| Operation  | Result                         | Notes    |
+============+================================+==========+
| `x | y`  | bitwise :dfn:`or` of *x* and   | \(4)     |
|            | *y*                            |          |
+------------+--------------------------------+----------+
| `x ^ y`  | bitwise :dfn:`exclusive or` of | \(4)     |
|            | *x* and *y*                    |          |
+------------+--------------------------------+----------+
| `x & y`  | bitwise :dfn:`and` of *x* and  | \(4)     |
|            | *y*                            |          |
+------------+--------------------------------+----------+
| `x << n` | *x* shifted left by *n* bits   | (1)(2)   |
+------------+--------------------------------+----------+
| `x >> n` | *x* shifted right by *n* bits  | (1)(3)   |
+------------+--------------------------------+----------+
| `~x`     | the bits of *x* inverted       |          |
+------------+--------------------------------+----------+

Notes:

(1)
   Negative shift counts are illegal and cause a `exc` to be raised.

(2)
   A left shift by *n* bits is equivalent to multiplication by `pow(2, n)`.

(3)
   A right shift by *n* bits is equivalent to floor division by `pow(2, n)`.

(4)
   Performing these calculations with at least one extra sign extension bit in
   a finite two's complement representation (a working bit-width of
   `1 + max(x.bit_length(), y.bit_length())` or more) is sufficient to get the
   same result as if there were an infinite number of sign bits.

### Additional Methods on Integer Types

The int type implements the `class` :term:`abstract base
class`. In addition, it provides a few more methods:

### Method: `int.bit_length()`

    Return the number of bits necessary to represent an integer in binary,
excluding the sign and leading zeros

```python

     >>> n = -37
     >>> bin(n)
     '-0b100101'
     >>> n.bit_length()
     6

 More precisely, if ``x`` is nonzero, then ``x.bit_length()`` is the
 unique positive integer ``k`` such that ``2**(k-1) <= abs(x) < 2**k``.
 Equivalently, when ``abs(x)`` is small enough to have a correctly
 rounded logarithm, then ``k = 1 + int(log(abs(x), 2))``.
 If ``x`` is zero, then ``x.bit_length()`` returns ``0``.

 Equivalent to::

     def bit_length(self):
         s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
         s = s.lstrip('-0b') # remove leading zeros and minus sign
         return len(s)       # len('100101') --> 6

 .. versionadded:: 3.1

```

### Method: `int.bit_count()`

    Return the number of ones in the binary representation of the absolute
    value of the integer. This is also known as the population count.
Example

```python

     >>> n = 19
     >>> bin(n)
     '0b10011'
     >>> n.bit_count()
     3
     >>> (-n).bit_count()
     3

 Equivalent to::

     def bit_count(self):
         return bin(self).count("1")

 .. versionadded:: 3.10

```

### Method: `int.to_bytes(length=1, byteorder='big', *, signed=False)`

    Return an array of bytes representing an integer.

        >>> (1024).to_bytes(2, byteorder='big')
        b'\x04\x00'
        >>> (1024).to_bytes(10, byteorder='big')
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
        >>> (-1024).to_bytes(10, byteorder='big', signed=True)
        b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
        >>> x = 1000
        >>> x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
        b'\xe8\x03'

    The integer is represented using *length* bytes, and defaults to 1.  An
    `exc` is raised if the integer is not representable with
    the given number of bytes.

    The *byteorder* argument determines the byte order used to represent the
    integer, and defaults to `"big"`.  If *byteorder* is
    `"big"`, the most significant byte is at the beginning of the byte
    array.  If *byteorder* is `"little"`, the most significant byte is at
    the end of the byte array.

    The *signed* argument determines whether two's complement is used to
    represent the integer.  If *signed* is `False` and a negative integer is
    given, an `exc` is raised. The default value for *signed*
    is `False`.

    The default values can be used to conveniently turn an integer into a
single byte object

```python

     >>> (65).to_bytes()
     b'A'

 However, when using the default arguments, don't try
 to convert a value greater than 255 or you'll get an :exc:`OverflowError`.

 Equivalent to::

     def to_bytes(n, length=1, byteorder='big', signed=False):
         if byteorder == 'little':
             order = range(length)
         elif byteorder == 'big':
             order = reversed(range(length))
         else:
             raise ValueError("byteorder must be either 'little' or 'big'")

         return bytes((n >> i*8) & 0xff for i in order)

 .. versionadded:: 3.2
 .. versionchanged:: 3.11
    Added default argument values for ``length`` and ``byteorder``.

```

    Return the integer represented by the given array of bytes.

        >>> int.from_bytes(b'\x00\x10', byteorder='big')
        16
        >>> int.from_bytes(b'\x00\x10', byteorder='little')
        4096
        >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
        -1024
        >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
        64512
        >>> int.from_bytes([255, 0, 0], byteorder='big')
        16711680

    The argument *bytes* must either be a `term` or an
    iterable producing bytes.

    The *byteorder* argument determines the byte order used to represent the
    integer, and defaults to `"big"`.  If *byteorder* is
    `"big"`, the most significant byte is at the beginning of the byte
    array.  If *byteorder* is `"little"`, the most significant byte is at
    the end of the byte array.  To request the native byte order of the host
    system, use `data` as the byte order value.

    The *signed* argument indicates whether two's complement is used to
    represent the integer.

Equivalent to

```python

     def from_bytes(bytes, byteorder='big', signed=False):
         if byteorder == 'little':
             little_ordered = list(bytes)
         elif byteorder == 'big':
             little_ordered = list(reversed(bytes))
         else:
             raise ValueError("byteorder must be either 'little' or 'big'")

         n = sum(b << i*8 for i, b in enumerate(little_ordered))
         if signed and little_ordered and (little_ordered[-1] & 0x80):
             n -= 1 << 8*len(little_ordered)

         return n

 .. versionadded:: 3.2
 .. versionchanged:: 3.11
    Added default argument value for ``byteorder``.

```

### Method: `int.as_integer_ratio()`

   Return a pair of integers whose ratio is equal to the original
   integer and has a positive denominator.  The integer ratio of integers
   (whole numbers) is always the integer as the numerator and `1` as the
   denominator.

   .. versionadded:: 3.8

### Method: `int.is_integer()`

   Returns `True`. Exists for duck type compatibility with `float.is_integer()`.

   .. versionadded:: 3.12

### Additional Methods on Float

The float type implements the `class` :term:`abstract base
class`. float also has the following additional methods.

   Class method to return a floating-point number constructed from a number *x*.

   If the argument is an integer or a floating-point number, a
   floating-point number with the same value (within Python's floating-point
   precision) is returned.  If the argument is outside the range of a Python
   float, an `exc` will be raised.

   For a general Python object `x`, `float.from_number(x)` delegates to
   `x.__float__()`.
   If `object.__float__()` is not defined then it falls back
   to `object.__index__()`.

   .. versionadded:: 3.14

### Method: `float.as_integer_ratio()`

   Return a pair of integers whose ratio is exactly equal to the
   original float. The ratio is in lowest terms and has a positive denominator.  Raises
   `exc` on infinities and a `exc` on
   NaNs.

### Method: `float.is_integer()`

   Return `True` if the float instance is finite with integral
value, and ``False`` otherwise

```python

   >>> (-2.0).is_integer()
   True
   >>> (3.2).is_integer()
   False

```

Two methods support conversion to
and from hexadecimal strings.  Since Python's floats are stored
internally as binary numbers, converting a float to or from a
*decimal* string usually involves a small rounding error.  In
contrast, hexadecimal strings allow exact representation and
specification of floating-point numbers.  This can be useful when
debugging, and in numerical work.

### Method: `float.hex()`

   Return a representation of a floating-point number as a hexadecimal
   string.  For finite floating-point numbers, this representation
   will always include a leading `0x` and a trailing `p` and
   exponent.

   Class method to return the float represented by a hexadecimal
   string *s*.  The string *s* may have leading and trailing
   whitespace.

Note that `float.hex()` is an instance method, while
`float.fromhex()` is a class method.

A hexadecimal string takes the form

```python

[sign] ['0x'] integer ['.' fraction] ['p' exponent]

```

where the optional `sign` may be either `+` or `-`, `integer`
and `fraction` are strings of hexadecimal digits, and `exponent`
is a decimal integer with an optional leading sign.  Case is not
significant, and there must be at least one hexadecimal digit in
either the integer or the fraction.  This syntax is similar to the
syntax specified in section 6.4.4.2 of the C99 standard, and also to
the syntax used in Java 1.5 onwards.  In particular, the output of
`float.hex()` is usable as a hexadecimal floating-point literal in
C or Java code, and hexadecimal strings produced by C's `%a` format
character or Java's `Double.toHexString` are accepted by
`float.fromhex()`.

Note that the exponent is written in decimal rather than hexadecimal,
and that it gives the power of 2 by which to multiply the coefficient.
For example, the hexadecimal string `0x3.a7p10` represents the
floating-point number `(3 + 10./16 + 7./16**2) * 2.0**10`, or
``3740.0``

```python

>>> float.fromhex('0x3.a7p10')
3740.0

```

Applying the reverse conversion to `3740.0` gives a different
hexadecimal string representing the same number

```python

>>> float.hex(3740.0)
'0x1.d380000000000p+11'

```

### Additional Methods on Complex

The `class` type implements the `class`
`term`.
`class` also has the following additional methods.

   Class method to convert a number to a complex number.

   For a general Python object `x`, `complex.from_number(x)` delegates to
   `x.__complex__()`.  If `object.__complex__()` is not defined then it falls back
   to `object.__float__()`.  If `!__float__()` is not defined then it falls back
   to `object.__index__()`.

   .. versionadded:: 3.14

### Hashing of numeric types

For numbers `x` and `y`, possibly of different types, it's a requirement
that `hash(x) == hash(y)` whenever `x == y` (see the `object.__hash__()`
method documentation for more details).  For ease of implementation and
efficiency across a variety of numeric types (including `class`,
`class`, `class` and `class`)
Python's hash for numeric types is based on a single mathematical function
that's defined for any rational number, and hence applies to all instances of
`class` and `class`, and all finite instances of
`class` and `class`.  Essentially, this function is
given by reduction modulo `P` for a fixed prime `P`.  The value of `P` is
made available to Python as the :attr:`~sys.hash_info.modulus` attribute of
`data`.

.. impl-detail

```python

Currently, the prime used is ``P = 2**31 - 1`` on machines with 32-bit C
longs and ``P = 2**61 - 1`` on machines with 64-bit C longs.

```

Here are the rules in detail:

- If `x = m / n` is a nonnegative rational number and `n` is not divisible
  by `P`, define `hash(x)` as `m * invmod(n, P) % P`, where ``invmod(n,
  P)` gives the inverse of `n` modulo `P``.

- If `x = m / n` is a nonnegative rational number and `n` is
  divisible by `P` (but `m` is not) then `n` has no inverse
  modulo `P` and the rule above doesn't apply; in this case define
  `hash(x)` to be the constant value `sys.hash_info.inf`.

- If `x = m / n` is a negative rational number define `hash(x)`
  as `-hash(-x)`.  If the resulting hash is `-1`, replace it with
  `-2`.

- The particular values `sys.hash_info.inf` and `-sys.hash_info.inf`
  are used as hash values for positive
  infinity or negative infinity (respectively).

- For a `class` number `z`, the hash values of the real
  and imaginary parts are combined by computing ``hash(z.real) +
  sys.hash_info.imag * hash(z.imag)``, reduced modulo
  `2**sys.hash_info.width` so that it lies in
  ``range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width -
  1))`.  Again, if the result is `-1`, it's replaced with `-2``.

To clarify the above rules, here's some example Python code,
equivalent to the built-in hash, for computing the hash of a rational
number, :class:`float`, or :class:`complex`

```python

import sys, math

def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return object.__hash__(x)
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value

```

## Boolean Type - :class:`bool`

Booleans represent truth values. The `class` type has exactly two
constant instances: `True` and `False`.

.. index

```python
single: False
single: True
pair: Boolean; values

```

The built-in function `bool()`  converts any value to a boolean, if the
value can be interpreted as a truth value (see section `ref` above).

For logical operations, use the `ref` `and`,
`or` and `not`.
When applying the bitwise operators `&`, `|`, `^` to two booleans, they
return a bool equivalent to the logical operations "and", "or", "xor". However,
the logical operators `and`, `or` and `!=` should be preferred
over `&`, `|` and `^`.

   The use of the bitwise inversion operator `~` is deprecated and will
   raise an error in Python 3.16.

`class` is a subclass of `class` (see `ref`). In
many numeric contexts, `False` and `True` behave like the integers 0 and 1, respectively.
However, relying on this is discouraged; explicitly convert using `int()`
instead.

## Iteration-related types

.. index

```python
single: iterator protocol
single: protocol; iterator
single: sequence; iteration
single: container; iteration over

```

Python supports a concept of iteration over containers.  This is implemented
using two distinct methods; these are used to allow user-defined classes to
support iteration.  Sequences, described below in more detail, always support
the iteration methods.

### Iterables

One method needs to be defined for container objects to provide `term`
support:

### Method: `container.__iter__()`

   Return an `term` object.  The object is required to support the
   iterator protocol described below.  If a container supports different types
   of iteration, additional methods can be provided to specifically request
   iterators for those iteration types.  (An example of an object supporting
   multiple forms of iteration would be a tree structure which supports both
   breadth-first and depth-first traversal.)  This method corresponds to the
   :c:member:`~PyTypeObject.tp_iter` slot of the type structure for Python
   objects in the Python/C API.

### Iterators

The iterator objects themselves are required to support the following two
methods, which together form the :dfn:`iterator protocol`:

### Method: `iterator.__iter__()`

   Return the `term` object itself.  This is required to allow both
   containers and iterators to be used with the :keyword:`for` and
   :keyword:`in` statements.  This method corresponds to the
   :c:member:`~PyTypeObject.tp_iter` slot of the type structure for Python
   objects in the Python/C API.

### Method: `iterator.__next__()`

   Return the next item from the `term`.  If there are no further
   items, raise the `exc` exception.  This method corresponds to
   the :c:member:`~PyTypeObject.tp_iternext` slot of the type structure for
   Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and
specific sequence types, dictionaries, and other more specialized forms.  The
specific types are not important beyond their implementation of the iterator
protocol.

Once an iterator's `iterator.__next__()` method raises
`exc`, it must continue to do so on subsequent calls.
Implementations that do not obey this property are deemed broken.

### Generator types

Python's `term` -- or more precisely,
`term` and
`term` -- provide a convenient way
to implement the iterator protocol.

A function that contains one or more `ref`
is a `term`.
For example

```python

>>> def count_to_three():
...     yield 0
...     yield 1
...     yield 2
...     yield 3

```

Generator functions behave as regular
`ref`
(for example, they have the same attributes), except that calling a generator
function returns a :ref:`generator iterator <generator-methods>`

```python

>>> count_to_three()
<generator object count_to_three at 0x7f33a2305000>

```

Iterating a generator iterator executes code of the underlying
generator function, producing each :keyword:`yield`\ed value in turn

```python

>>> for number in count_to_three():
...     print(number)
0
1
2
3

>>> list(count_to_three())
[0, 1, 2, 3]

```

One common use for generator functions is implementing the
`object.__iter__()` method of custom iterable objects.
For example

```python

>>> class CardDeck:
...     def __iter__(self):
...         yield 'three of clubs'
...         yield 'ace of hearts'

>>> list(CardDeck())
['three of clubs', 'ace of hearts']

```

### Generator iterators

Generator iterators implement the
`ref`.
Iterating them drives execution of the underlying generator function.

### Method: `generator.__next__()`

   Starts the execution of a generator function or resumes it at the
   `ref` where the function is currently suspended.
   When a generator function is resumed with a `generator.__next__()`
   method, the current yield expression always evaluates to `const`.
   The execution then continues to the next yield expression, where the
   generator is suspended again, and the value of the expression after the
   :keyword:`yield` keyword is returned to `generator.__next__()`'s
   caller.
   If the generator exits without yielding another value,
   `generator.__next__()` raises a `exc` exception,
   signalling that iteration has completed.

   This method is normally called implicitly, for example by a :keyword:`for`
   loop, or by the built-in `next()` function.

Generator iterators have a few more methods than generic iterators, which
can be used to control the execution of the underlying generator function:

### Method: `generator.send(value)`

   "Sends" a value into the generator function: the *value* argument becomes
   the result of the current yield expression.

   Otherwise, this method behaves like `generator.__next__()`: it resumes
   the underlying function and either returns the next yielded value or raises
   `exc`.

   When `send()` is called to start the generator, it must be called
   with `const` as the argument, because there is no current yield
   expression that could receive the value.

### Method: `generator.throw(value)`

            generator.throw(type[, value[, traceback]])

   Raises an exception at the point where the generator is currently suspended.

   Otherwise, this method behaves like `generator.__next__()`: it resumes
   the underlying function and either returns the next yielded value or raises
   `exc`.
   If the generator function does not catch the passed-in exception, or
   raises a different exception, then that exception propagates to the caller.

   When `throw()` is called to start the generator, the generator
   immediately exits (that is, subsequent calls to `generator.__next__()`
   will raise `exc`) and the thrown exception is propagated to
   `throw()`'s caller.

   In typical use, this is called with a single argument, an exception instance,
   similar to the way the :keyword:`raise` keyword is used.

   For backwards compatibility, however, the second signature is
   supported, following a convention from older versions of Python.
   The *type* argument should be an exception class, and *value*
   should be an exception instance. If the *value* is not provided, the
   *type* constructor is called to get an instance. If *traceback*
   is provided, it is set on the exception, otherwise any existing
   :attr:`~BaseException.__traceback__` attribute stored in *value* may
   be cleared.

   .. versionchanged:: 3.12

      The second signature \(type\[, value\[, traceback\]\]\) is deprecated and
      may be removed in a future version of Python.

### Method: `generator.close()`

   Raises a `exc` exception at the point where the generator
   function is currently suspended (equivalent to calling `throw(GeneratorExit)`).

   If the generator function has already exited (due to an exception or
   normal return), or raises `exc` (by not catching the
   exception), `close()` returns `const`.
   If the generator yields a value, a `exc` is raised.
   If the generator raises any other exception, it is propagated to the caller.
   If a generator returns a value upon being closed, that value is returned
   by `close()`.

   When a generator iterator is garbage collected before it has exited,
   `generator.close()` is called automatically.

   .. versionchanged:: 3.13

      If a generator returns a value upon being closed, the value is returned
      by `close()`.
      Previously, it returned `None`.

Calling any of the generator methods (`generator.__next__()`,
`generator.send()`, `generator.throw()`, `generator.close()`)
while one of these methods is already executing
raises a `exc` exception.

### Asynchronous generator iterators

This subsection describes the methods of an asynchronous generator iterator,
which are used to control the execution of an asynchronous generator function.

### Method: `agen.__anext__()`

   Returns an `term` which when run starts to execute the
   asynchronous generator function or resumes it at the
   `ref` where the function is currently suspended.
   When an asynchronous generator function is resumed with an
   `agen.__anext__()` method, the current yield expression always
   evaluates to `const` in the returned awaitable, which when run will
   continue to the next yield expression.
   The value of the expression after the :keyword:`yield` keyword is the value
   of the `exc` exception raised by the completing coroutine.
   If the asynchronous generator exits without yielding another value, the
   awaitable instead raises a `exc` exception,
   signalling that the asynchronous iteration has completed.

   This method is normally called implicitly by an :keyword:`async for` loop,
   or by the built-in `anext()` function.

Asynchronous generator-iterators have a few more methods than generic
asynchronous iterators, which can be used to control the execution of
the underlying generator function:

### Method: `agen.asend(value)`

   Returns an awaitable which, when run, "sends" a value into the underlying
   asynchronous generator function: the *value* argument becomes
   the result of the current yield expression.

   Otherwise, this method behaves like `agen.__anext__()`: when the
   returned awaitable runs, it resumes the underlying function and either
   returns the next yielded value as the value of the raised
   `exc`, or raises `exc`.

   When `asend()` is called to start the asynchronous
   generator, it must be called with `const` as the argument,
   because there is no yield expression that could receive the value.

### Method: `agen.athrow(value)`

            agen.athrow(type[, value[, traceback]])

   Returns an awaitable that, when run, raises an exception at the point where
   the underlying asynchronous generator function is currently suspended.

   Otherwise, this method behaves like `agen.__anext__()`: when the
   returned awaitable runs, it resumes the underlying function (with an
   exception raised) and either returns the next yielded value as the value of
   the raised `exc`, or raises `exc`.
   If the underlying function does not catch the passed-in exception, or
   raises a different exception, then when the awaitable is run, that
   exception propagates to the caller of the awaitable.

   When `agen.athrow()` is called to start the generator, the generator
   exits when the awaitable runs (that is, subsequent results from
   `agen.__anext__()` will raise `exc` when run)
   and the thrown exception is propagated to the awaitable's caller.

   In typical use, this is called with a single argument, an exception instance,
   similar to the way the :keyword:`raise` keyword is used.

   For backwards compatibility, however, the second signature is
   supported.
   An exception instance is created from three arguments in the same way as in
   `generator.throw()`.

   .. versionchanged:: 3.12

      The second signature \(type\[, value\[, traceback\]\]\) is deprecated and
      may be removed in a future version of Python.

### Method: `agen.aclose()`

   Returns an awaitable that when run will throw a `exc` into
   the underlying asynchronous generator function at the point where it is
   currently suspended (equivalent to calling `athrow(GeneratorExit)`).

   If the asynchronous generator function then exits gracefully, is already
   closed, or raises `exc` (by not catching the exception),
   then the returned awaitable will raise a `exc` exception.
   Awaitables returned by subsequent calls to `agen.__anext__()`
   or `agen.asend()` will raise a `exc` exception.

   If the asynchronous generator yields a value, a `exc` is
   raised by the awaitable.
   If the asynchronous generator raises any other exception, that exception
   is propagated to the caller of the awaitable.

   If the asynchronous generator has already exited due to an exception or
   normal exit, then further calls to `aclose()` will return an awaitable
   that does nothing.

## Sequence Types --- :class:`list`, :class:`tuple`, :class:`range`

There are three basic sequence types: lists, tuples, and range objects.
Additional sequence types tailored for processing of
`ref` and `ref` are
described in dedicated sections.

### Common Sequence Operations

The operations in the following table are supported by most sequence types,
both mutable and immutable. The `class` ABC is
provided to make it easier to correctly implement these operations on
custom sequence types.

This table lists the sequence operations sorted in ascending priority.  In the
table, *s* and *t* are sequences of the same type, *n*, *i*, *j* and *k* are
integers and *x* is an arbitrary object that meets any type and value
restrictions imposed by *s*.

The `in` and `not in` operations have the same priorities as the
comparison operations. The `+` (concatenation) and `*` (repetition)
operations have the same priority as the corresponding numeric operations. [3]_

See `ref` for the costs of the various sequence
operations.

.. index

```python
triple: operations on; sequence; types
pair: built-in function; len
pair: built-in function; min
pair: built-in function; max
pair: concatenation; operation
pair: repetition; operation
pair: subscript; operation
pair: slice; operation
pair: operator; in
pair: operator; not in

```

+--------------------------+--------------------------------+----------+
| Operation                | Result                         | Notes    |
+==========================+================================+==========+
| `x in s`               | `True` if an item of *s* is  | \(1)     |
|                          | equal to *x*, else `False`   |          |
+--------------------------+--------------------------------+----------+
| `x not in s`           | `False` if an item of *s* is | \(1)     |
|                          | equal to *x*, else `True`    |          |
+--------------------------+--------------------------------+----------+
| `s + t`                | the concatenation of *s* and   | (6)(7)   |
|                          | *t*                            |          |
+--------------------------+--------------------------------+----------+
| `s * n` or             | equivalent to adding *s* to    | (2)(7)   |
| `n * s`                | itself *n* times               |          |
+--------------------------+--------------------------------+----------+
| `s[i]`                 | *i*\ th item of *s*, origin 0  | (3)(8)   |
+--------------------------+--------------------------------+----------+
| `s[i:j]`               | slice of *s* from *i* to *j*   | (3)(4)   |
+--------------------------+--------------------------------+----------+
| `s[i:j:k]`             | slice of *s* from *i* to *j*   | (3)(5)   |
|                          | with step *k*                  |          |
+--------------------------+--------------------------------+----------+
| `len(s)`               | length of *s*                  |          |
+--------------------------+--------------------------------+----------+
| `min(s)`               | smallest item of *s*           |          |
+--------------------------+--------------------------------+----------+
| `max(s)`               | largest item of *s*            |          |
+--------------------------+--------------------------------+----------+

Sequences of the same type also support comparisons.  In particular, tuples
and lists are compared lexicographically by comparing corresponding elements.
This means that to compare equal, every element must compare equal and the
two sequences must be of the same type and have the same length.  (For full
details see `ref` in the language reference.)

.. index

```python
single: loop; over mutable sequence
single: mutable sequence; loop over

```

Forward and reversed iterators over mutable sequences access values using an
index.  That index will continue to march forward (or backward) even if the
underlying sequence is mutated.  The iterator terminates only when an
`exc` or a `exc` is encountered (or when the index
drops below zero).

Notes:

(1)
   While the `in` and `not in` operations are used only for simple
   containment testing in the general case, some specialised sequences
   (such as `class`, `class` and `class`) also use
them for subsequence testing

```python

   >>> "gg" in "eggs"
   True

```

(2)
   Values of *n* less than `0` are treated as `0` (which yields an empty
   sequence of the same type as *s*).  Note that items in the sequence *s*
   are not copied; they are referenced multiple times.  This often haunts
new Python programmers; consider

```python

   >>> lists = [[]] * 3
   >>> lists
   [[], [], []]
   >>> lists[0].append(3)
   >>> lists
   [[3], [3], [3]]

What has happened is that ``[[]]`` is a one-element list containing an empty
list, so all three elements of ``[[]] * 3`` are references to this single empty
list.  Modifying any of the elements of ``lists`` modifies this single list.
You can create a list of different lists this way::

   >>> lists = [[] for i in range(3)]
   >>> lists[0].append(3)
   >>> lists[1].append(5)
   >>> lists[2].append(7)
   >>> lists
   [[3], [5], [7]]

Further explanation is available in the FAQ entry
:ref:`faq-multidimensional-list`.

```

(3)
   If *i* or *j* is negative, the index is relative to the end of sequence *s*:
   `len(s) + i` or `len(s) + j` is substituted.  But note that `-0` is
   still `0`.

(4)
   The slice of *s* from *i* to *j* is defined as the sequence of items with
   index *k* such that `i <= k < j`.

   * If *i* is omitted or `None`, use `0`.
   * If *j* is omitted or `None`, use `len(s)`.
   * If *i* or *j* is less than `-len(s)`, use `0`.
   * If *i* or *j* is greater than `len(s)`, use `len(s)`.
   * If *i* is greater than or equal to *j*, the slice is empty.

(5)
   The slice of *s* from *i* to *j* with step *k* is defined as the sequence of
   items with index  `x = i + n*k` such that `0 <= n < (j-i)/k`.  In other words,
   the indices are `i`, `i+k`, `i+2*k`, `i+3*k` and so on, stopping when
   *j* is reached (but never including *j*).  When *k* is positive,
   *i* and *j* are reduced to `len(s)` if they are greater.
   When *k* is negative, *i* and *j* are reduced to `len(s) - 1` if
   they are greater.  If *i* or *j* are omitted or `None`, they become
   "end" values (which end depends on the sign of *k*).  Note, *k* cannot be zero.
   If *k* is `None`, it is treated like `1`.

(6)
   Concatenating immutable sequences always results in a new object.  This
   means that building up a sequence by repeated concatenation will have a
   quadratic runtime cost in the total sequence length.  To get a linear
   runtime cost, you must switch to one of the alternatives below:

   * if concatenating `class` objects, you can build a list and use
     `str.join()` at the end or else write to an `class`
     instance and retrieve its value when complete

   * if concatenating `class` objects, you can similarly use
     `bytes.join()` or `class`, or you can do in-place
     concatenation with a `class` object.  `class`
     objects are mutable and have an efficient overallocation mechanism

   * if concatenating `class` objects, extend a `class` instead

   * for other types, investigate the relevant class documentation

(7)
  Some sequence types (such as `class`) only support item sequences
  that follow specific patterns, and hence don't support sequence
  concatenation or repetition.

(8)
   An `exc` is raised if *i* is outside the sequence range.

Sequence types also support the following methods:

### Method: `list.count(value, /)`

            range.count(value, /)
            tuple.count(value, /)
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.count(value, /)`

   Return the total number of occurrences of *value* in *sequence*.

### Method: `list.index(value[, start[, stop]])`

            range.index(value[, start[, stop]])
            tuple.index(value[, start[, stop]])
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.index(value[, start[, stop]])`

   Return the index of the first occurrence of *value* in *sequence*.

   Raises `exc` if *value* is not found in *sequence*.

   The *start* or *stop* arguments allow for efficient searching
   of subsections of the sequence, beginning at *start* and ending at *stop*.
   This is roughly equivalent to `start + sequence[start:stop].index(value)`,
   only without copying any data.

.. caution

```python
   Not all sequence types support passing the *start* and *stop* arguments.

```

### Immutable Sequence Types

.. index

```python
triple: immutable; sequence; types
pair: object; tuple
pair: built-in function; hash

```

The only operation that immutable sequence types generally implement that is
not also implemented by mutable sequence types is support for the `hash()`
built-in.

This support allows immutable sequences, such as `class` instances, to
be used as `class` keys and stored in `class` and `class`
instances.

Attempting to hash an immutable sequence that contains unhashable values will
result in `exc`.

### Mutable Sequence Types

.. index

```python
triple: mutable; sequence; types
pair: object; list
pair: object; bytearray

```

The operations in the following table are defined on mutable sequence types.
The `class` ABC is provided to make it
easier to correctly implement these operations on custom sequence types.

In the table *s* is an instance of a mutable sequence type, *t* is any
iterable object and *x* is an arbitrary object that meets any type
and value restrictions imposed by *s* (for example, `class` only
accepts integers that meet the value restriction `0 <= x <= 255`).

.. index

```python
triple: operations on; sequence; types
triple: operations on; list; type
pair: subscript; assignment
pair: slice; assignment
pair: statement; del

```

+------------------------------+--------------------------------+---------------------+
| Operation                    | Result                         | Notes               |
+==============================+================================+=====================+
| `s[i] = x`                 | item *i* of *s* is replaced by |                     |
|                              | *x*                            |                     |
+------------------------------+--------------------------------+---------------------+
| `del s[i]`                 | removes item *i* of *s*        |                     |
+------------------------------+--------------------------------+---------------------+
| `s[i:j] = t`               | slice of *s* from *i* to *j*   |                     |
|                              | is replaced by the contents of |                     |
|                              | the iterable *t*               |                     |
+------------------------------+--------------------------------+---------------------+
| `del s[i:j]`               | removes the elements of        |                     |
|                              | `s[i:j]` from the list       |                     |
|                              | (same as `s[i:j] = []`)      |                     |
+------------------------------+--------------------------------+---------------------+
| `s[i:j:k] = t`             | the elements of `s[i:j:k]`   | \(1)                |
|                              | are replaced by those of *t*   |                     |
+------------------------------+--------------------------------+---------------------+
| `del s[i:j:k]`             | removes the elements of        |                     |
|                              | `s[i:j:k]` from the list     |                     |
+------------------------------+--------------------------------+---------------------+
| `s += t`                   | extends *s* with the           |                     |
|                              | contents of *t* (for the       |                     |
|                              | most part the same as          |                     |
|                              | `s[len(s):len(s)] = t`)      |                     |
+------------------------------+--------------------------------+---------------------+
| `s *= n`                   | updates *s* with its contents  | \(2)                |
|                              | repeated *n* times             |                     |
+------------------------------+--------------------------------+---------------------+

Notes:

(1)
   If *k* is not equal to `1`, *t* must have the same length as the slice it is replacing.

(2)
   The value *n* is an integer, or an object implementing
   `object.__index__()`.  Zero and negative values of *n* clear
   the sequence.  Items in the sequence are not copied; they are referenced
   multiple times, as explained for `s * n` under `ref`.

Mutable sequence types also support the following methods:

### Method: `bytearray.append(value, /)`

            list.append(value, /)
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.append(value, /)`

   Append *value* to the end of the sequence.
   This is equivalent to writing `seq[len(seq):len(seq)] = [value]`.

### Method: `bytearray.clear()`

            list.clear()
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.clear()`

   .. versionadded:: 3.3

   Remove all items from *sequence*.
   This is equivalent to writing `del sequence[:]`.

### Method: `bytearray.copy()`

            list.copy()
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.copy()`

   .. versionadded:: 3.3

   Create a shallow copy of *sequence*.
   This is equivalent to writing `sequence[:]`.

   .. hint:: The `!copy()` method is not part of the
             `class` `class`,
             but most concrete mutable sequence types provide it.

### Method: `bytearray.extend(iterable, /)`

            list.extend(iterable, /)
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.extend(iterable, /)`

   Extend *sequence* with the contents of *iterable*.
   For the most part, this is the same as writing
   `seq[len(seq):len(seq)] = iterable`.

### Method: `bytearray.insert(index, value, /)`

            list.insert(index, value, /)
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.insert(index, value, /)`

   Insert *value* into *sequence* at the given *index*.
   This is equivalent to writing `sequence[index:index] = [value]`.

### Method: `bytearray.pop(index=-1, /)`

            list.pop(index=-1, /)
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.pop(index=-1, /)`

   Retrieve the item at *index* and also remove it from *sequence*.
   By default, the last item in *sequence* is removed and returned.

### Method: `bytearray.remove(value, /)`

            list.remove(value, /)
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.remove(value, /)`

   Remove the first item from *sequence* where `sequence[i] == value`.

   Raises `exc` if *value* is not found in *sequence*.

### Method: `bytearray.reverse()`

            list.reverse()
   :no-contents-entry:
   :no-index-entry:
   :no-typesetting:

### Method: `sequence.reverse()`

   Reverse the items of *sequence* in place.
   This method maintains economy of space when reversing a large sequence.
   To remind users that it operates by side-effect, it returns `None`.

### Lists

Lists are mutable sequences, typically used to store collections of
homogeneous items (where the precise degree of similarity will vary by
application).

### Class: `list(iterable=(), /)`

   Lists may be constructed in several ways:

   * Using a pair of square brackets to denote the empty list: `[]`
   * Using square brackets, separating items with commas: `[a]`, `[a, b, c]`
   * Using a list comprehension: `[x for x in iterable]`
   * Using the type constructor: `list()` or `list(iterable)`

   The constructor builds a list whose items are the same and in the same
   order as *iterable*'s items.  *iterable* may be either a sequence, a
   container that supports iteration, or an iterator object.  If *iterable*
   is already a list, a copy is made and returned, similar to `iterable[:]`.
   For example, `list('abc')` returns `['a', 'b', 'c']` and
   `list( (1, 2, 3) )` returns `[1, 2, 3]`.
   If no argument is given, the constructor creates a new empty list, `[]`.

   Many other operations also produce lists, including the `sorted()`
   built-in.

   Lists are `ref` over the types of their items.

   Lists implement all of the `ref` and
   `ref` sequence operations. Lists also provide the
   following additional method:

   .. method:: list.sort(*, key=None, reverse=False)

      This method sorts the list in place, using only `<` comparisons
      between items. Exceptions are not suppressed - if any comparison operations
      fail, the entire sort operation will fail (and the list will likely be left
      in a partially modified state).

      `sort()` accepts two arguments that can only be passed by keyword
      (`ref`):

      *key* specifies a function of one argument that is used to extract a
      comparison key from each list element (for example, `key=str.lower`).
      The key corresponding to each item in the list is calculated once and
      then used for the entire sorting process. The default value of `None`
      means that list items are sorted directly without calculating a separate
      key value.

      The `functools.cmp_to_key()` utility is available to convert a 2.x
      style *cmp* function to a *key* function.

      *reverse* is a boolean value.  If set to `True`, then the list elements
      are sorted as if each comparison were reversed.

      This method modifies the sequence in place for economy of space when
      sorting a large sequence.  To remind users that it operates by side
      effect, it does not return the sorted sequence (use `sorted()` to
      explicitly request a new sorted list instance).

      The `sort()` method is guaranteed to be stable.  A sort is stable if it
      guarantees not to change the relative order of elements that compare equal
      --- this is helpful for sorting in multiple passes (for example, sort by
      department, then by salary grade).

      For sorting examples and a brief sorting tutorial, see `ref`.

.. impl-detail

```python

      While a list is being sorted, the effect of attempting to mutate, or even
      inspect, the list is undefined.  The C implementation of Python makes the
      list appear empty for the duration, and raises :exc:`ValueError` if it can
      detect that the list has been mutated during a sort.

```

.. seealso

```python

For detailed information on thread-safety guarantees for :class:`list`
objects, see :ref:`thread-safety-list`.

```

### Tuples

Tuples are immutable sequences, typically used to store collections of
heterogeneous data (such as the 2-tuples produced by the `enumerate()`
built-in). Tuples are also used for cases where an immutable sequence of
homogeneous data is needed (such as allowing storage in a `class` or
`class` instance).

### Class: `tuple(iterable=(), /)`

   Tuples may be constructed in a number of ways:

   * Using a pair of parentheses to denote the empty tuple: `()`
   * Using a trailing comma for a singleton tuple: `a,` or `(a,)`
   * Separating items with commas: `a, b, c` or `(a, b, c)`
   * Using the `tuple()` built-in: `tuple()` or `tuple(iterable)`

   The constructor builds a tuple whose items are the same and in the same
   order as *iterable*'s items.  *iterable* may be either a sequence, a
   container that supports iteration, or an iterator object.  If *iterable*
   is already a tuple, it is returned unchanged. For example,
   `tuple('abc')` returns `('a', 'b', 'c')` and
   `tuple( [1, 2, 3] )` returns `(1, 2, 3)`.
   If no argument is given, the constructor creates a new empty tuple, `()`.

   Note that it is actually the comma which makes a tuple, not the parentheses.
   The parentheses are optional, except in the empty tuple case, or
   when they are needed to avoid syntactic ambiguity. For example,
   `f(a, b, c)` is a function call with three arguments, while
   `f((a, b, c))` is a function call with a 3-tuple as the sole argument.

   Tuples implement all of the `ref` sequence
   operations.

   Tuples are `ref` over the types of their contents.
   For more information, refer to
   `ref`.

For heterogeneous collections of data where access by name is clearer than
access by index, `collections.namedtuple()` may be a more appropriate
choice than a simple tuple object.

### Ranges

The `class` type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in :keyword:`for`
loops.

### Class: `range(stop, /)`

           range(start, stop, step=1, /)

   The arguments to the range constructor must be integers (either built-in
   `class` or any object that implements the `object.__index__()` special
   method).  If the *step* argument is omitted, it defaults to `1`.
   If the *start* argument is omitted, it defaults to `0`.
   If *step* is zero, `exc` is raised.

   For a positive *step*, the contents of a range `r` are determined by the
   formula `r[i] = start + step*i` where `i >= 0` and
   `r[i] < stop`.

   For a negative *step*, the contents of the range are still determined by
   the formula `r[i] = start + step*i`, but the constraints are `i >= 0`
   and `r[i] > stop`.

   A range object will be empty if `r[0]` does not meet the value
   constraint. Ranges do support negative indices, but these are interpreted
   as indexing from the end of the sequence determined by the positive
   indices.

   Ranges containing absolute values larger than `data` are
   permitted but some features (such as `len()`) may raise
   `exc`.

Range examples

```python

   >>> list(range(10))
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   >>> list(range(1, 11))
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   >>> list(range(0, 30, 5))
   [0, 5, 10, 15, 20, 25]
   >>> list(range(0, 10, 3))
   [0, 3, 6, 9]
   >>> list(range(0, -10, -1))
   [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
   >>> list(range(0))
   []
   >>> list(range(1, 0))
   []

Ranges implement all of the :ref:`common <typesseq-common>` sequence operations
except concatenation and repetition (due to the fact that range objects can
only represent sequences that follow a strict pattern and repetition and
concatenation will usually violate that pattern).

.. attribute:: start

   The value of the *start* parameter (or ``0`` if the parameter was
   not supplied)

.. attribute:: stop

   The value of the *stop* parameter

.. attribute:: step

   The value of the *step* parameter (or ``1`` if the parameter was
   not supplied)

```

The advantage of the `class` type over a regular `class` or
`class` is that a `class` object will always take the same
(small) amount of memory, no matter the size of the range it represents (as it
only stores the `start`, `stop` and `step` values, calculating individual
items and subranges as needed).

Range objects implement the `class` ABC, and provide
features such as containment tests, element index lookup, slicing and
support for negative indices (see `ref`):

   >>> r = range(0, 20, 2)
   >>> r
   range(0, 20, 2)
   >>> 11 in r
   False
   >>> 10 in r
   True
   >>> r.index(10)
   5
   >>> r[5]
   10
   >>> r[:5]
   range(0, 10, 2)
   >>> r[-1]
   18

Testing range objects for equality with `==` and `!=` compares
them as sequences.  That is, two range objects are considered equal if
they represent the same sequence of values.  (Note that two range
objects that compare equal might have different :attr:`~range.start`,
:attr:`~range.stop` and :attr:`~range.step` attributes, for example
`range(0) == range(2, 1, 3)` or `range(0, 3, 2) == range(0, 4, 2)`.)

   Implement the Sequence ABC.
   Support slicing and negative indices.
   Test `class` objects for membership in constant time instead of
   iterating through all items.

   Define '==' and '!=' to compare range objects based on the
   sequence of values they define (instead of comparing based on
   object identity).

   Added the :attr:`~range.start`, :attr:`~range.stop` and :attr:`~range.step`
   attributes.

.. seealso

```python

* The `linspace recipe <https://code.activestate.com/recipes/579000-equally-spaced-numbers-linspace/>`_
  shows how to implement a lazy version of range suitable for floating-point
  applications.

```

.. index

```python
single: string; text sequence type
single: str (built-in class); (see also string)
pair: object; string

```

## Text and Binary Sequence Type Methods Summary

The following table summarizes the text and binary sequence types methods by
category.

+--------------------------+-------------------------------------------+---------------------------------------------------+
| Category                 |  `class` methods                     |   `class` and `class` methods   |
+==========================+===========================================+===================================================+
| Formatting               |  `str.format()`                       |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.format_map()`                   |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `ref`                         |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `ref`             |  `ref`                          |
+--------------------------+------------------+------------------------+--------------------+------------------------------+
| Searching and Replacing  | `str.find()` | `str.rfind()`      | `bytes.find()` | `bytes.rfind()`          |
|                          +------------------+------------------------+--------------------+------------------------------+
|                          | `str.index()`| `str.rindex()`     | `bytes.index()`| `bytes.rindex()`         |
|                          +------------------+------------------------+--------------------+------------------------------+
|                          |  `str.startswith()`                   |  `bytes.startswith()`                         |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.endswith()`                     |  `bytes.endswith()`                           |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.count()`                        |  `bytes.count()`                              |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.replace()`                      |  `bytes.replace()`                            |
+--------------------------+-------------------+-----------------------+---------------------+-----------------------------+
| Splitting and Joining    | `str.split()` | `str.rsplit()`    | `bytes.split()` | `bytes.rsplit()`        |
|                          +-------------------+-----------------------+---------------------+-----------------------------+
|                          |  `str.splitlines()`                   |  `bytes.splitlines()`                         |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.partition()`                    |  `bytes.partition()`                          |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.rpartition()`                   |  `bytes.rpartition()`                         |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.join()`                         |  `bytes.join()`                               |
+--------------------------+-------------------------------------------+---------------------------------------------------+
| String Classification    |  `str.isalpha()`                      |  `bytes.isalpha()`                            |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isdecimal()`                    |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isdigit()`                      |  `bytes.isdigit()`                            |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isnumeric()`                    |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isalnum()`                      |  `bytes.isalnum()`                            |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isidentifier()`                 |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.islower()`                      |  `bytes.islower()`                            |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isupper()`                      |  `bytes.isupper()`                            |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.istitle()`                      |  `bytes.istitle()`                            |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isspace()`                      |  `bytes.isspace()`                            |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.isprintable()`                  |                                                   |
+--------------------------+-------------------------------------------+---------------------------------------------------+
| Case Manipulation        |  `str.lower()`                        |  `bytes.lower()`                              |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.upper()`                        |  `bytes.upper()`                              |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.casefold()`                     |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.capitalize()`                   |  `bytes.capitalize()`                         |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.title()`                        |  `bytes.title()`                              |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.swapcase()`                     |  `bytes.swapcase()`                           |
+--------------------------+-------------------+-----------------------+---------------------+-----------------------------+
| Padding and Stripping    | `str.ljust()` | `str.rjust()`     | `bytes.ljust()` | `bytes.rjust()`         |
|                          +-------------------+-----------------------+---------------------+-----------------------------+
|                          |  `str.center()`                       |  `bytes.center()`                             |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.expandtabs()`                   |  `bytes.expandtabs()`                         |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.strip()`                        |  `bytes.strip()`                              |
|                          +--------------------+----------------------+----------------------+----------------------------+
|                          | `str.lstrip()` | `str.rstrip()`   | `bytes.lstrip()` | `bytes.rstrip()`       |
|                          +--------------------+----------------------+----------------------+----------------------------+
|                          |  `str.removeprefix()`                 |  `bytes.removeprefix()`                       |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.removesuffix()`                 |  `bytes.removesuffix()`                       |
+--------------------------+-------------------------------------------+---------------------------------------------------+
| Translation and Encoding |  `str.translate()`                    |  `bytes.translate()`                          |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.maketrans()`                    |  `bytes.maketrans()`                          |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |  `str.encode()`                       |                                                   |
|                          +-------------------------------------------+---------------------------------------------------+
|                          |                                           |  `bytes.decode()`                             |
+--------------------------+-------------------------------------------+---------------------------------------------------+

## Text Sequence Type --- :class:`str`

Textual data in Python is handled with `class` objects, or :dfn:`strings`.
Strings are immutable
`ref` of Unicode code points.  String literals are
written in a variety of ways:

* Single quotes: `'allows embedded "double" quotes'`
* Double quotes: `"allows embedded 'single' quotes"`
* Triple quoted: `'''Three single quotes'''`, `"""Three double quotes"""`

Triple quoted strings may span multiple lines - all associated whitespace will
be included in the string literal.

String literals that are part of a single expression and have only whitespace
between them will be implicitly converted to a single string literal. That
is, `("spam " "eggs") == "spam eggs"`.

See `ref` for more about the various forms of string literal,
including supported `ref`, and the `r` ("raw") prefix that
disables most escape sequence processing.

Strings may also be created from other objects using the `class`
constructor.

Since there is no separate "character" type, indexing a string produces
strings of length 1. That is, for a non-empty string *s*, `s[0] == s[0:1]`.

.. index

```python
pair: object; io.StringIO

```

There is also no mutable string type, but `str.join()` or
`class` can be used to efficiently construct strings from
multiple fragments.

   For backwards compatibility with the Python 2 series, the `u` prefix is
   once again permitted on string literals. It has no effect on the meaning
   of string literals and cannot be combined with the `r` prefix.

.. index

```python
single: string; str (built-in class)

```

### Class: `str(*, encoding='utf-8', errors='strict')`

           str(object)
           str(object, encoding, errors='strict')
           str(object, *, errors)

   Return a `ref` version of *object*.  If *object* is not
   provided, returns the empty string.  Otherwise, the behavior of `str()`
   depends on whether *encoding* or *errors* is given, as follows.

   If neither *encoding* nor *errors* is given, `str(object)` returns
   `type(object).__str__(object) <object.__str__>()`,
   which is the "informal" or nicely
   printable string representation of *object*.  For string objects, this is
   the string itself.  If *object* does not have a `object.__str__()`
   method, then `str()` falls back to returning
   `repr(object) <repr>()`.

.. index

```python
   single: buffer protocol; str (built-in class)
   single: bytes; str (built-in class)

If at least one of *encoding* or *errors* is given, *object* should be a
:term:`bytes-like object` (e.g. :class:`bytes` or :class:`bytearray`).  In
this case, if *object* is a :class:`bytes` (or :class:`bytearray`) object,
then ``str(bytes, encoding, errors)`` is equivalent to
:meth:`bytes.decode(encoding, errors) <bytes.decode>`.  Otherwise, the bytes
object underlying the buffer object is obtained before calling
:meth:`bytes.decode`.  See :ref:`binaryseq` and
:ref:`bufferobjects` for information on buffer objects.

Passing a :class:`bytes` object to :func:`str` without the *encoding*
or *errors* arguments falls under the first case of returning the informal
string representation (see also the :option:`-b` command-line option to
Python).  For example::

   >>> str(b'Zoot!')
   "b'Zoot!'"

For more information on the ``str`` class and its methods, see
:ref:`textseq` and the :ref:`string-methods` section below.  To output
formatted strings, see the :ref:`f-strings` and :ref:`formatstrings`
sections.  In addition, see the :ref:`stringservices` section.

```

.. index

```python
pair: string; methods

```

### String Methods

.. index

```python
pair: module; re

```

Strings implement all of the `ref` sequence
operations, along with the additional methods described below.

Strings also support two styles of string formatting, one providing a large
degree of flexibility and customization (see `str.format()`,
`ref` and `ref`) and the other based on C
`printf` style formatting that handles a narrower range of types and is
slightly harder to use correctly, but is often faster for the cases it can
handle (`ref`).

The `ref` section of the standard library covers a number of
other modules that provide various text related utilities (including regular
expression support in the `mod` module).

### Method: `str.capitalize()`

   Return a copy of the string with its first character capitalized and the
   rest lowercased. For example:

.. doctest

```python

   >>> 'PYTHON IS AMAZING'.capitalize()
   'Python is amazing'
   >>> 'ǋemačka starts With a non-ASCII digraph'.capitalize()
   'ǋemačka starts with a non-ascii digraph'

See also :meth:`title`.

.. versionchanged:: 3.8
   The first character is now put into titlecase rather than uppercase.
   This means that characters like digraphs will only have their first
   letter capitalized, instead of the full character.

```

### Method: `str.casefold()`

   Return a casefolded copy of the string. Casefolded strings may be used for
   caseless matching.

   Casefolding is similar to lowercasing but more aggressive because it is
   intended to remove all case distinctions in a string. For example, the German
   lowercase letter `'ß'` is equivalent to `"ss"`. Since it is already
   lowercase, `lower()` would do nothing to `'ß'`; `casefold()`
   converts it to `"ss"`.
   For example:

.. doctest

```python

   >>> 'straße'.lower()
   'straße'
   >>> 'straße'.casefold()
   'strasse'

The casefolding algorithm is `described in section 3.13.3 'Default Case
Folding' of the Unicode Standard
<https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G53253>`__.

.. versionadded:: 3.3

```

### Method: `str.center(width, fillchar=' ', /)`

   Return centered in a string of length *width*. Padding is done using the
   specified *fillchar* (default is an ASCII space). The original string is
returned if *width* is less than or equal to ``len(s)``.  For example

```python

   >>> 'Python'.center(10)
   '  Python  '
   >>> 'Python'.center(10, '-')
   '--Python--'
   >>> 'Python'.center(4)
   'Python'

```

### Method: `str.count(sub[, start[, end]])`

   Return the number of non-overlapping occurrences of substring *sub* in the
   range [*start*, *end*].  Optional arguments *start* and *end* are
   interpreted as in slice notation.

   If *sub* is empty, returns the number of empty strings between characters
which is the length of the string plus one. For example

```python

   >>> 'spam, spam, spam'.count('spam')
   3
   >>> 'spam, spam, spam'.count('spam', 5)
   2
   >>> 'spam, spam, spam'.count('spam', 5, 10)
   1
   >>> 'spam, spam, spam'.count('eggs')
   0
   >>> 'spam, spam, spam'.count('')
   17

```

### Method: `str.encode(encoding="utf-8", errors="strict")`

   Return the string encoded to `class`.

   *encoding* defaults to `'utf-8'`;
   see `ref` for possible values.

   *errors* controls how encoding errors are handled.
   If `'strict'` (the default), a `exc` exception is raised.
   Other possible values are `'ignore'`,
   `'replace'`, `'xmlcharrefreplace'`, `'backslashreplace'` and any
   other name registered via `codecs.register_error()`.
   See `ref` for details.

   For performance reasons, the value of *errors* is not checked for validity
   unless an encoding error actually occurs,
   `ref` is enabled
   or a `ref` is used.
For example

```python

   >>> encoded_str_to_bytes = 'Python'.encode()
   >>> type(encoded_str_to_bytes)
   <class 'bytes'>
   >>> encoded_str_to_bytes
   b'Python'

.. versionchanged:: 3.1
   Added support for keyword arguments.

.. versionchanged:: 3.9
   The value of the *errors* argument is now checked in :ref:`devmode` and
   in :ref:`debug mode <debug-build>`.

```

### Method: `str.endswith(suffix[, start[, end]])`

   Return `True` if the string ends with the specified *suffix*, otherwise return
   `False`.  *suffix* can also be a tuple of suffixes to look for.  With optional
   *start*, test beginning at that position.  With optional *end*, stop comparing
   at that position. Using *start* and *end* is equivalent to
``str[start:end].endswith(suffix)``. For example

```python

   >>> 'Python'.endswith('on')
   True
   >>> 'a tuple of suffixes'.endswith(('at', 'in'))
   False
   >>> 'a tuple of suffixes'.endswith(('at', 'es'))
   True
   >>> 'Python is amazing'.endswith('is', 0, 9)
   True

See also :meth:`startswith` and :meth:`removesuffix`.

```

### Method: `str.expandtabs(tabsize=8)`

   Return a copy of the string where all tab characters are replaced by one or
   more spaces, depending on the current column and the given tab size.  Tab
   positions occur every *tabsize* characters (default is 8, giving tab
   positions at columns 0, 8, 16 and so on).  To expand the string, the current
   column is set to zero and the string is examined character by character.  If
   the character is a tab (`\t`), one or more space characters are inserted
   in the result until the current column is equal to the next tab position.
   (The tab character itself is not copied.)  If the character is a newline
   (`\n`) or return (`\r`), it is copied and the current column is reset to
   zero.  Any other character is copied unchanged and the current column is
   incremented by one regardless of how the character is represented when
printed. For example

```python

   >>> '01\t012\t0123\t01234'.expandtabs()
   '01      012     0123    01234'
   >>> '01\t012\t0123\t01234'.expandtabs(4)
   '01  012 0123    01234'
   >>> print('01\t012\n0123\t01234'.expandtabs(4))
   01  012
   0123    01234

```

### Method: `str.find(sub[, start[, end]])`

   Return the lowest index in the string where substring *sub* is found within
   the slice `s[start:end]`.  Optional arguments *start* and *end* are
   interpreted as in slice notation.  Return `-1` if *sub* is not found.
For example

```python

   >>> 'spam, spam, spam'.find('sp')
   0
   >>> 'spam, spam, spam'.find('sp', 5)
   6

See also :meth:`rfind` and :meth:`index`.

.. note::

   The :meth:`~str.find` method should be used only if you need to know the
   position of *sub*.  To check if *sub* is a substring or not, use the
   :keyword:`in` operator::

      >>> 'Py' in 'Python'
      True

```

### Method: `str.format(*args, **kwargs)`

   Perform a string formatting operation.  The string on which this method is
   called can contain literal text or replacement fields delimited by braces
   `{}`.  Each replacement field refers to a positional argument (numbered
   explicitly or automatically) or a keyword argument.  Returns a copy of
   the string where each replacement field is replaced with the string value of
   the corresponding argument. For example:

.. doctest

```python

   >>> "The sum of {} + {} is {}".format(1, 2, 1+2)
   'The sum of 1 + 2 is 3'
   >>> "{1} expects the {0} Inquisition!".format("Spanish", "Nobody")
   'Nobody expects the Spanish Inquisition!'
   >>> "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)
   'The sum of 1 + 2 is 3'

See :ref:`formatstrings` for a description of the various formatting options
that can be specified in format strings.

.. note::
   When formatting a number (:class:`int`, :class:`float`, :class:`complex`,
   :class:`decimal.Decimal` and subclasses) with the ``n`` type
   (ex: ``'{:n}'.format(1234)``), the function temporarily sets the
   ``LC_CTYPE`` locale to the ``LC_NUMERIC`` locale to decode
   ``decimal_point`` and ``thousands_sep`` fields of :c:func:`localeconv` if
   they are non-ASCII or longer than 1 byte, and the ``LC_NUMERIC`` locale is
   different than the ``LC_CTYPE`` locale.  This temporary change affects
   other threads.

.. versionchanged:: 3.7
   When formatting a number with the ``n`` type, the function sets
   temporarily the ``LC_CTYPE`` locale to the ``LC_NUMERIC`` locale in some
   cases.

```

### Method: `str.format_map(mapping, /)`

   Similar to `str.format(**mapping)`, except that `mapping` is
   used directly and not copied to a `class`.  This is useful
   if for example `mapping` is a dict subclass:

   >>> class Default(dict):
   ...     def __missing__(self, key):
   ...         return key
   ...
   >>> '{name} was born in {country}'.format_map(Default(name='Guido'))
   'Guido was born in country'

   .. versionadded:: 3.2

### Method: `str.index(sub[, start[, end]])`

   Like `str.find()`, but raise `exc` when the substring is
   not found. For example:

.. doctest

```python

   >>> 'spam, spam, spam'.index('spam')
   0
   >>> 'spam, spam, spam'.index('eggs')
   Traceback (most recent call last):
     File "<python-input-0>", line 1, in <module>
       'spam, spam, spam'.index('eggs')
       ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
   ValueError: substring not found

See also :meth:`rindex`.

```

### Method: `str.isalnum()`

   Return `True` if all characters in the string are alphanumeric and there is at
   least one character, `False` otherwise.  A character `c` is alphanumeric if one
   of the following returns `True`: `c.isalpha()`, `c.isdecimal()`,
   `c.isdigit()`, or `c.isnumeric()`. For example:

.. doctest

```python

   >>> 'abc123'.isalnum()
   True
   >>> 'abc123!@#'.isalnum()
   False
   >>> ''.isalnum()
   False
   >>> ' '.isalnum()
   False

```

### Method: `str.isalpha()`

   Return `True` if all characters in the string are alphabetic and there is at least
   one character, `False` otherwise.  Alphabetic characters are those characters defined
   in the Unicode character database as "Letter", i.e., those with general category
   property being one of "Lm", "Lt", "Lu", "Ll", or "Lo".  Note that this is different
   from the `Alphabetic property defined in section 4.10 'Letters, Alphabetic, and
   Ideographic' of the Unicode Standard
   <https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G91002>`__.
   For example:

.. doctest

```python

   >>> 'Letters and spaces'.isalpha()
   False
   >>> 'LettersOnly'.isalpha()
   True
   >>> 'µ'.isalpha()  # non-ASCII characters can be considered alphabetical too
   True

See :ref:`unicode-properties`.

```

### Method: `str.isascii()`

   Return `True` if the string is empty or all characters in the string are ASCII,
   `False` otherwise.
   ASCII characters have code points in the range U+0000-U+007F. For example:

.. doctest

```python

   >>> 'ASCII characters'.isascii()
   True
   >>> 'µ'.isascii()
   False

.. versionadded:: 3.7

```

### Method: `str.isdecimal()`

   Return `True` if all characters in the string are decimal
   characters and there is at least one character, `False`
   otherwise. Decimal characters are those that can be used to form
   numbers in base 10, such as U+0660, ARABIC-INDIC DIGIT
   ZERO.  Formally a decimal character is a character in the Unicode
   General Category "Nd". For example:

.. doctest

```python

   >>> '0123456789'.isdecimal()
   True
   >>> '٠١٢٣٤٥٦٧٨٩'.isdecimal()  # Arabic-Indic digits zero to nine
   True
   >>> 'alphabetic'.isdecimal()
   False

```

### Method: `str.isdigit()`

   Return `True` if all characters in the string are digits and there is at least one
   character, `False` otherwise.  Digits include decimal characters and digits that need
   special handling, such as the compatibility superscript digits.
   This covers digits which cannot be used to form numbers in base 10,
   like the `Kharosthi numbers <https://en.wikipedia.org/wiki/Kharosthi#Numerals>`__.
   Formally, a digit is a character that has the
   property value Numeric_Type=Digit or Numeric_Type=Decimal.

   For example:

.. doctest

```python

   >>> '0123456789'.isdigit()
   True
   >>> '٠١٢٣٤٥٦٧٨٩'.isdigit()  # Arabic-Indic digits zero to nine
   True
   >>> '⅕'.isdigit()  # Vulgar fraction one fifth
   False
   >>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
   (False, True, True)

See also :meth:`isdecimal` and :meth:`isnumeric`.

```

### Method: `str.isidentifier()`

   Return `True` if the string is a valid identifier according to the language
   definition, section `ref`.

   `keyword.iskeyword()` can be used to test whether string `s` is a reserved
   identifier, such as :keyword:`def` and :keyword:`class`.

   Example:

```python

   >>> from keyword import iskeyword

   >>> 'hello'.isidentifier(), iskeyword('hello')
   (True, False)
   >>> 'def'.isidentifier(), iskeyword('def')
   (True, True)

```

### Method: `str.islower()`

   Return `True` if all cased characters [4]_ in the string are lowercase and
   there is at least one cased character, `False` otherwise.

### Method: `str.isnumeric()`

   Return `True` if all characters in the string are numeric
   characters, and there is at least one character, `False`
   otherwise. Numeric characters include digit characters, and all characters
   that have the Unicode numeric value property, e.g. U+2155,
   VULGAR FRACTION ONE FIFTH.  Formally, numeric characters are those with the property
   value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.
   For example:

.. doctest

```python

   >>> '0123456789'.isnumeric()
   True
   >>> '٠١٢٣٤٥٦٧٨٩'.isnumeric()  # Arabic-Indic digits zero to nine
   True
   >>> '⅕'.isnumeric()  # Vulgar fraction one fifth
   True
   >>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
   (False, True, True)

See also :meth:`isdecimal` and :meth:`isdigit`.

```

### Method: `str.isprintable()`

   Return `True` if all characters in the string are printable, `False` if it
   contains at least one non-printable character.

   Here "printable" means the character is suitable for `repr()` to use in
   its output; "non-printable" means that `repr()` on built-in types will
   hex-escape the character.  It has no bearing on the handling of strings
   written to `data` or `data`.

   The printable characters are those which in the Unicode character database
   (see `mod`) have a general category in group Letter, Mark,
   Number, Punctuation, or Symbol (L, M, N, P, or S); plus the ASCII space 0x20.
   Nonprintable characters are those in group Separator or Other (Z or C),
   except the ASCII space.

   For example:

.. doctest

```python

   >>> ''.isprintable(), ' '.isprintable()
   (True, True)
   >>> '\t'.isprintable(), '\n'.isprintable()
   (False, False)

See also :meth:`isspace`.

```

### Method: `str.isspace()`

   Return `True` if there are only whitespace characters in the string and there is
   at least one character, `False` otherwise.

   For example:

.. doctest

```python

   >>> ''.isspace()
   False
   >>> ' '.isspace()
   True
   >>> '\t\n'.isspace() # TAB and BREAK LINE
   True
   >>> '\u3000'.isspace() # IDEOGRAPHIC SPACE
   True

A character is *whitespace* if in the Unicode character database
(see :mod:`unicodedata`), either its general category is ``Zs``
("Separator, space"), or its bidirectional class is one of ``WS``,
``B``, or ``S``.

See also :meth:`isprintable`.

```

### Method: `str.istitle()`

   Return `True` if the string is a titlecased string and there is at least one
   character, for example uppercase characters may only follow uncased characters
   and lowercase characters only cased ones.  Return `False` otherwise.

   For example:

.. doctest

```python

   >>> 'Spam, Spam, Spam'.istitle()
   True
   >>> 'spam, spam, spam'.istitle()
   False
   >>> 'SPAM, SPAM, SPAM'.istitle()
   False

See also :meth:`title`.

```

### Method: `str.isupper()`

   Return `True` if all cased characters [4]_ in the string are uppercase and
   there is at least one cased character, `False` otherwise.

      >>> 'BANANA'.isupper()
      True
      >>> 'banana'.isupper()
      False
      >>> 'baNana'.isupper()
      False
      >>> ' '.isupper()
      False

### Method: `str.join(iterable, /)`

   Return a string which is the concatenation of the strings in *iterable*.
   A `exc` will be raised if there are any non-string values in
   *iterable*, including `class` objects.  The separator between
   elements is the string providing this method. For example:

.. doctest

```python

   >>> ', '.join(['spam', 'spam', 'spam'])
   'spam, spam, spam'
   >>> '-'.join('Python')
   'P-y-t-h-o-n'

See also :meth:`split`.

```

### Method: `str.ljust(width, fillchar=' ', /)`

   Return the string left justified in a string of length *width*. Padding is
   done using the specified *fillchar* (default is an ASCII space). The
   original string is returned if *width* is less than or equal to `len(s)`.

   For example:

.. doctest

```python

   >>> 'Python'.ljust(10)
   'Python    '
   >>> 'Python'.ljust(10, '.')
   'Python....'
   >>> 'Monty Python'.ljust(10, '.')
   'Monty Python'

See also :meth:`rjust`.

```

### Method: `str.lower()`

   Return a copy of the string with all the cased characters [4]_ converted to
   lowercase. For example:

.. doctest

```python

   >>> 'Lower Method Example'.lower()
   'lower method example'

The lowercasing algorithm used is `described in section 3.13.2 'Default Case
Conversion' of the Unicode Standard
<https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G34078>`__.

```

### Method: `str.lstrip(chars=None, /)`

   Return a copy of the string with leading characters removed.  The *chars*
   argument is a string specifying the set of characters to be removed.  If omitted
   or `None`, the *chars* argument defaults to removing whitespace, that is
   characters for which `str.isspace()` is true.  The *chars*
argument is not a prefix; rather, all combinations of its values are stripped

```python

   >>> '   spacious   '.lstrip()
   'spacious   '
   >>> 'www.example.com'.lstrip('cmowz.')
   'example.com'

See :meth:`str.removeprefix` for a method that will remove a single prefix
string rather than all of a set of characters.  For example::

   >>> 'Arthur: three!'.lstrip('Arthur: ')
   'ee!'
   >>> 'Arthur: three!'.removeprefix('Arthur: ')
   'three!'

```

                  str.maketrans(from, to, remove='', /)

   This static method returns a translation table usable for `str.translate()`.

   If there is only one argument, it must be a dictionary mapping Unicode
   ordinals (integers) or characters (strings of length 1) to Unicode ordinals,
   strings (of arbitrary lengths) or `None`.  Character keys will then be
   converted to ordinals.

   If there are two arguments, they must be strings of equal length, and in the
   resulting dictionary, each character in *from* will be mapped to the character at
   the same position in *to*.  If there is a third argument, it must be a string,
   whose characters will be mapped to `None` in the result.

   .. versionchanged:: 3.15

      *dict* can now be a `class`.

### Method: `str.partition(sep, /)`

   Split the string at the first occurrence of *sep*, and return a 3-tuple
   containing the part before the separator, the separator itself, and the part
   after the separator.  If the separator is not found, return a 3-tuple containing
   the string itself, followed by two empty strings.

   For example:

.. doctest

```python

   >>> 'Monty Python'.partition(' ')
   ('Monty', ' ', 'Python')
   >>> "Monty Python's Flying Circus".partition(' ')
   ('Monty', ' ', "Python's Flying Circus")
   >>> 'Monty Python'.partition('-')
   ('Monty Python', '', '')

See also :meth:`rpartition`.

```

### Method: `str.removeprefix(prefix, /)`

   If the string starts with the *prefix* string, return
   `string[len(prefix):]`. Otherwise, return a copy of the original
   string:

.. doctest

```python

   >>> 'TestHook'.removeprefix('Test')
   'Hook'
   >>> 'BaseTestCase'.removeprefix('Test')
   'BaseTestCase'

.. versionadded:: 3.9

See also :meth:`removesuffix` and :meth:`startswith`.

```

### Method: `str.removesuffix(suffix, /)`

   If the string ends with the *suffix* string and that *suffix* is not empty,
   return `string[:-len(suffix)]`. Otherwise, return a copy of the
   original string:

.. doctest

```python

   >>> 'MiscTests'.removesuffix('Tests')
   'Misc'
   >>> 'TmpDirMixin'.removesuffix('Tests')
   'TmpDirMixin'

.. versionadded:: 3.9

See also :meth:`removeprefix` and :meth:`endswith`.

```

### Method: `str.replace(old, new, /, count=-1)`

   Return a copy of the string with all occurrences of substring *old* replaced by
   *new*.  If *count* is given, only the first *count* occurrences are replaced.
   If *count* is not specified or `-1`, then all occurrences are replaced.
   For example:

.. doctest

```python

   >>> 'spam, spam, spam'.replace('spam', 'eggs')
   'eggs, eggs, eggs'
   >>> 'spam, spam, spam'.replace('spam', 'eggs', 1)
   'eggs, spam, spam'

.. versionchanged:: 3.13
   *count* is now supported as a keyword argument.

```

### Method: `str.rfind(sub[, start[, end]])`

   Return the highest index in the string where substring *sub* is found, such
   that *sub* is contained within `s[start:end]`.  Optional arguments *start*
   and *end* are interpreted as in slice notation.  Return `-1` on failure.
   For example:

.. doctest

```python

   >>> 'spam, spam, spam'.rfind('sp')
   12
   >>> 'spam, spam, spam'.rfind('sp', 0, 10)
   6

See also :meth:`find` and :meth:`rindex`.

```

### Method: `str.rindex(sub[, start[, end]])`

   Like `rfind()` but raises `exc` when the substring *sub* is not
   found.
   For example:

.. doctest

```python

   >>> 'spam, spam, spam'.rindex('spam')
   12
   >>> 'spam, spam, spam'.rindex('eggs')
   Traceback (most recent call last):
     File "<stdin-0>", line 1, in <module>
       'spam, spam, spam'.rindex('eggs')
       ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
   ValueError: substring not found

See also :meth:`index` and :meth:`find`.

```

### Method: `str.rjust(width, fillchar=' ', /)`

   Return the string right justified in a string of length *width*. Padding is
   done using the specified *fillchar* (default is an ASCII space). The
   original string is returned if *width* is less than or equal to `len(s)`.

   For example:

.. doctest

```python

   >>> 'Python'.rjust(10)
   '    Python'
   >>> 'Python'.rjust(10, '.')
   '....Python'
   >>> 'Monty Python'.rjust(10, '.')
   'Monty Python'

See also :meth:`ljust` and :meth:`zfill`.

```

### Method: `str.rpartition(sep, /)`

   Split the string at the last occurrence of *sep*, and return a 3-tuple
   containing the part before the separator, the separator itself, and the part
   after the separator.  If the separator is not found, return a 3-tuple containing
   two empty strings, followed by the string itself.

   For example:

.. doctest

```python

   >>> 'Monty Python'.rpartition(' ')
   ('Monty', ' ', 'Python')
   >>> "Monty Python's Flying Circus".rpartition(' ')
   ("Monty Python's Flying", ' ', 'Circus')
   >>> 'Monty Python'.rpartition('-')
   ('', '', 'Monty Python')

See also :meth:`partition`.

```

### Method: `str.rsplit(sep=None, maxsplit=-1)`

   Return a list of the words in the string, using *sep* as the delimiter string.
   If *maxsplit* is given, at most *maxsplit* splits are done, the *rightmost*
   ones.  If *sep* is not specified or `None`, any
   `whitespace <str.isspace>()` string is a
   separator.  Except for splitting from the right, `rsplit()` behaves like
   `split()` which is described in detail below.

### Method: `str.rstrip(chars=None, /)`

   Return a copy of the string with trailing characters removed.  The *chars*
   argument is a string specifying the set of characters to be removed.  If omitted
   or `None`, the *chars* argument defaults to removing whitespace, that is
   characters for which `str.isspace()` is true.  The *chars*
   argument is not a suffix; rather, all combinations of its values are stripped.
   For example:

.. doctest

```python

   >>> '   spacious   '.rstrip()
   '   spacious'
   >>> 'mississippi'.rstrip('ipz')
   'mississ'

See :meth:`removesuffix` for a method that will remove a single suffix
string rather than all of a set of characters.  For example::

   >>> 'Monty Python'.rstrip(' Python')
   'M'
   >>> 'Monty Python'.removesuffix(' Python')
   'Monty'

See also :meth:`strip`.

```

### Method: `str.split(sep=None, maxsplit=-1)`

   Return a list of the words in the string, using *sep* as the delimiter
   string.  If *maxsplit* is given, at most *maxsplit* splits are done (thus,
   the list will have at most `maxsplit+1` elements).  If *maxsplit* is not
   specified or `-1`, then there is no limit on the number of splits
   (all possible splits are made).

   If *sep* is given, consecutive delimiters are not grouped together and are
   deemed to delimit empty strings (for example, `'1,,2'.split(',')` returns
   `['1', '', '2']`).  The *sep* argument may consist of multiple characters
   as a single delimiter (to split with multiple delimiters, use
   `re.split()`). Splitting an empty string with a specified separator
   returns `['']`.

   For example:

.. doctest

```python

   >>> '1,2,3'.split(',')
   ['1', '2', '3']
   >>> '1,2,3'.split(',', maxsplit=1)
   ['1', '2,3']
   >>> '1,2,,3,'.split(',')
   ['1', '2', '', '3', '']
   >>> '1<>2<>3<4'.split('<>')
   ['1', '2', '3<4']

If *sep* is not specified or is ``None``, a different splitting algorithm is
applied: runs of consecutive :meth:`whitespace <str.isspace>` are regarded
as a single separator,
and the result will contain no empty strings at the start or end if the
string has leading or trailing whitespace.  Consequently, splitting an empty
string or a string consisting of just whitespace with a ``None`` separator
returns ``[]``.

For example:

.. doctest::

   >>> '1 2 3'.split()
   ['1', '2', '3']
   >>> '1 2 3'.split(maxsplit=1)
   ['1', '2 3']
   >>> '   1   2   3   '.split()
   ['1', '2', '3']

If *sep* is not specified or is ``None`` and  *maxsplit* is ``0``, only
leading runs of consecutive whitespace are considered.

For example:

.. doctest::

   >>> "".split(None, 0)
   []
   >>> "   ".split(None, 0)
   []
   >>> "   foo   ".split(maxsplit=0)
   ['foo   ']

See also :meth:`join` and :meth:`rsplit`.

```

.. index

```python
single: universal newlines; str.splitlines method

```

### Method: `str.splitlines(keepends=False)`

   Return a list of the lines in the string, breaking at line boundaries.  Line
   breaks are not included in the resulting list unless *keepends* is given and
   true.

   This method splits on the following line boundaries.  In particular, the
   boundaries are a superset of `term`.

   +-----------------------+-----------------------------+
   | Representation        | Description                 |
   +=======================+=============================+
   | `\n`                | Line Feed                   |
   +-----------------------+-----------------------------+
   | `\r`                | Carriage Return             |
   +-----------------------+-----------------------------+
   | `\r\n`              | Carriage Return + Line Feed |
   +-----------------------+-----------------------------+
   | `\v` or `\x0b`    | Line Tabulation             |
   +-----------------------+-----------------------------+
   | `\f` or `\x0c`    | Form Feed                   |
   +-----------------------+-----------------------------+
   | `\x1c`              | File Separator              |
   +-----------------------+-----------------------------+
   | `\x1d`              | Group Separator             |
   +-----------------------+-----------------------------+
   | `\x1e`              | Record Separator            |
   +-----------------------+-----------------------------+
   | `\x85`              | Next Line (C1 Control Code) |
   +-----------------------+-----------------------------+
   | `\u2028`            | Line Separator              |
   +-----------------------+-----------------------------+
   | `\u2029`            | Paragraph Separator         |
   +-----------------------+-----------------------------+

   .. versionchanged:: 3.2

      `\v` and `\f` added to list of line boundaries.

For example

```python

   >>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
   ['ab c', '', 'de fg', 'kl']
   >>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
   ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

Unlike :meth:`~str.split` when a delimiter string *sep* is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line::

   >>> "".splitlines()
   []
   >>> "One line\n".splitlines()
   ['One line']

For comparison, ``split('\n')`` gives::

   >>> ''.split('\n')
   ['']
   >>> 'Two lines\n'.split('\n')
   ['Two lines', '']

```

### Method: `str.startswith(prefix[, start[, end]])`

   Return `True` if string starts with the *prefix*, otherwise return `False`.
   *prefix* can also be a tuple of prefixes to look for.  With optional *start*,
   test string beginning at that position.  With optional *end*, stop comparing
   string at that position.

   For example:

.. doctest

```python

   >>> 'Python'.startswith('Py')
   True
   >>> 'a tuple of prefixes'.startswith(('at', 'a'))
   True
   >>> 'Python is amazing'.startswith('is', 7)
   True

See also :meth:`endswith` and :meth:`removeprefix`.

```

### Method: `str.strip(chars=None, /)`

   Return a copy of the string with the leading and trailing characters removed.
   The *chars* argument is a string specifying the set of characters to be removed.
   If omitted or `None`, the *chars* argument defaults to removing whitespace,
   that is characters for which `str.isspace()` is true.  The *chars* argument
   is not a prefix or suffix; rather, all combinations of its values are stripped.

   For example:

.. doctest

```python

   >>> '   spacious   '.strip()
   'spacious'
   >>> 'www.example.com'.strip('cmowz.')
   'example'

The outermost leading and trailing *chars* argument values are stripped
from the string. Characters are removed from the leading end until
reaching a string character that is not contained in the set of
characters in *chars*. A similar action takes place on the trailing end.

For example:

.. doctest::

   >>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
   >>> comment_string.strip('.#! ')
   'Section 3.2.1 Issue #32'

See also :meth:`rstrip`.

```

### Method: `str.swapcase()`

   Return a copy of the string with uppercase characters converted to lowercase and
   vice versa. For example:

.. doctest

```python

   >>> 'Hello World'.swapcase()
   'hELLO wORLD'

Note that it is not necessarily true that ``s.swapcase().swapcase() == s``.
For example:

.. doctest::

   >>> 'straße'.swapcase().swapcase()
   'strasse'

See also :meth:`str.lower` and :meth:`str.upper`.

```

### Method: `str.title()`

   Return a titlecased version of the string where words start with an uppercase
   character and the remaining characters are lowercase.

For example

```python

   >>> 'Hello world'.title()
   'Hello World'

The algorithm uses a simple language-independent definition of a word as
groups of consecutive letters.  The definition works in many contexts but
it means that apostrophes in contractions and possessives form word
boundaries, which may not be the desired result::

     >>> "they're bill's friends from the UK".title()
     "They'Re Bill'S Friends From The Uk"

The :func:`string.capwords` function does not have this problem, as it
splits words on spaces only.

Alternatively, a workaround for apostrophes can be constructed using regular
expressions::

     >>> import re
     >>> def titlecase(s):
     ...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     ...                   lambda mo: mo.group(0).capitalize(),
     ...                   s)
     ...
     >>> titlecase("they're bill's friends.")
     "They're Bill's Friends."

See also :meth:`istitle` and :meth:`capitalize`.

```

### Method: `str.translate(table, /)`

   Return a copy of the string in which each character has been mapped through
   the given translation table.  The table must be an object that implements
   indexing via `object.__getitem__()`, typically a `term` or
   `term`.  When indexed by a Unicode ordinal (an integer), the
   table object can do any of the following: return a Unicode ordinal or a
   string, to map the character to one or more other characters; return
   `None`, to delete the character from the return string; or raise a
   `exc` exception, to map the character to itself.

   You can use `str.maketrans()` to create a translation map from
   character-to-character mappings in different formats.

   The following example uses a mapping to replace `'a'` with `'X'`,
   `'b'` with `'Y'`, and delete `'c'`:

.. doctest

```python

   >>> 'abc123'.translate({ord('a'): 'X', ord('b'): 'Y', ord('c'): None})
   'XY123'

See also the :mod:`codecs` module for a more flexible approach to custom
character mappings.

```

### Method: `str.upper()`

   Return a copy of the string with all the cased characters [4]_ converted to
   uppercase.  Note that `s.upper().isupper()` might be `False` if `s`
   contains no cased characters or if the Unicode category of the resulting
   character(s) is not "Lu" (Letter, uppercase), but e.g. "Lt" (Letter,
   titlecase).

   The uppercasing algorithm used is `described in section 3.13.2 'Default Case
   Conversion' of the Unicode Standard
   <https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G34078>`__.

### Method: `str.zfill(width, /)`

   Return a copy of the string left filled with ASCII `'0'` digits to
   make a string of length *width*. A leading sign prefix (`'+'`/`'-'`)
   is handled by inserting the padding *after* the sign character rather
   than before. The original string is returned if *width* is less than
   or equal to `len(s)`.

   For example:

.. doctest

```python

   >>> "42".zfill(5)
   '00042'
   >>> "-42".zfill(5)
   '-0042'

See also :meth:`rjust`.

```

.. index

```python
single: ! formatted string literal
single: formatted string literals
single: ! f-string
single: f-strings
single: fstring
single: interpolated string literal
single: string; formatted literal
single: string; interpolated literal
single: {} (curly brackets); in formatted string literal
single: ! (exclamation mark); in formatted string literal
single: : (colon); in formatted string literal
single: = (equals); for help in debugging using string literals

```

### Formatted String Literals (f-strings)

   The :keyword:`await` and :keyword:`async for` can be used in expressions
   within f-strings.
   Added the debug specifier (`=`)
   Many restrictions on expressions within f-strings have been removed.
   Notably, nested strings, comments, and backslashes are now permitted.

An :dfn:`f-string` (formally a :dfn:`formatted string literal`) is
a string literal that is prefixed with `f` or `F`.
This type of string literal allows embedding the results of arbitrary Python
expressions within *replacement fields*, which are delimited by curly
brackets (`{}`).
Each replacement field must contain an expression, optionally followed by:

* a *debug specifier* -- an equal sign (`=`);
* a *conversion specifier* -- `!s`, `!r` or `!a`; and/or
* a *format specifier* prefixed with a colon (`:`).

See the `ref` for details
on the syntax of these fields.

### Debug specifier

If a debug specifier -- an equal sign (`=`) -- appears after the replacement
field expression, the resulting f-string will contain the expression's source,
the equal sign, and the value of the expression.
This is often useful for debugging

```python

>>> number = 14.3
>>> f'{number=}'
'number=14.3'

```

Whitespace before, inside and after the expression, as well as whitespace
after the equal sign, is significant --- it is retained in the result

```python

>>> f'{ number  -  4  = }'
' number  -  4  = 10.3'

```

### Conversion specifier

By default, the value of a replacement field expression is converted to
a string using :func:`str`

```python

>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third}'
'1/3'

```

When a debug specifier but no format specifier is used, the default conversion
instead uses :func:`repr`

```python

>>> f'{one_third = }'
'one_third = Fraction(1, 3)'

```

The conversion can be specified explicitly using one of these specifiers:

* `!s` for `str()`
* `!r` for `repr()`
* `!a` for `ascii()`

For example

```python

>>> str(one_third)
'1/3'
>>> repr(one_third)
'Fraction(1, 3)'

>>> f'{one_third!s} is {one_third!r}'
'1/3 is Fraction(1, 3)'

>>> string = "¡kočka 😸!"
>>> ascii(string)
"'\\xa1ko\\u010dka \\U0001f638!'"

>>> f'{string = !a}'
"string = '\\xa1ko\\u010dka \\U0001f638!'"

```

### Format specifier

After the expression has been evaluated, and possibly converted using an
explicit conversion specifier, it is formatted using the `format()` function.
If the replacement field includes a *format specifier* introduced by a colon
(`:`), the specifier is passed to `!format()` as the second argument.
The result of `!format()` is then used as the final value for the
replacement field. For example

```python

>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third:.6f}'
'0.333333'
>>> f'{one_third:_^+10}'
'___+1/3___'
>>> f'{one_third!r:_^20}'
'___Fraction(1, 3)___'
>>> f'{one_third = :~>10}~'
'one_third = ~~~~~~~1/3~'

```

### Template String Literals (t-strings)

A :dfn:`t-string` (formally a :dfn:`template string literal`) is
a string literal that is prefixed with `t` or `T`.

These strings follow the same syntax and evaluation rules as
`ref`,
with the following differences:

* Rather than evaluating to a `str` object, template string literals evaluate
  to a `class` object.

* The `format()` protocol is not used.
  Instead, the format specifier and conversions (if any) are passed to
  a new `class` object that is created
  for each evaluated expression.
  It is up to code that processes the resulting `class`
  object to decide how to handle format specifiers and conversions.

* Format specifiers containing nested replacement fields are evaluated eagerly,
  prior to being passed to the `class` object.
  For instance, an interpolation of the form `{amount:.{precision}f}` will
  evaluate the inner expression `{precision}` to determine the value of the
  `format_spec` attribute.
  If `precision` were to be `2`, the resulting format specifier
  would be `'.2f'`.

* When the equals sign `'='` is provided in an interpolation expression,
  the text of the expression is appended to the literal string that precedes
  the relevant interpolation.
  This includes the equals sign and any surrounding whitespace.
  The `class` instance for the expression will be created as
  normal, except that :attr:`~string.templatelib.Interpolation.conversion` will
  be set to '`r`' (`repr()`) by default.
  If an explicit conversion or format specifier is provided,
  this will override the default behaviour.

### ``printf``-style String Formatting

.. index

```python
single: formatting, string (%)
single: interpolation, string (%)
single: string; formatting, printf
single: string; interpolation, printf
single: printf-style formatting
single: sprintf-style formatting
single: % (percent); printf-style formatting

```

.. note

```python

The formatting operations described here exhibit a variety of quirks that
lead to a number of common errors (such as failing to display tuples and
dictionaries correctly).

Using :ref:`formatted string literals <f-strings>`, the :meth:`str.format`
interface, or :class:`string.Template` may help avoid these errors.
Each of these alternatives provides their own trade-offs and benefits of
simplicity, flexibility, and/or extensibility.

```

String objects have one unique built-in operation: the `%` operator (modulo).
This is also known as the string *formatting* or *interpolation* operator.
Given `format % values` (where *format* is a string), `%` conversion
specifications in *format* are replaced with zero or more elements of *values*.
The effect is similar to using the :c`sprintf()` function in the C language.
For example:

.. doctest

```python

>>> print('%s has %d quote types.' % ('Python', 2))
Python has 2 quote types.

```

If *format* requires a single argument, *values* may be a single non-tuple
object. [5]_  Otherwise, *values* must be a tuple with exactly the number of
items specified by the format string, or a single mapping object (for example, a
dictionary).

.. index

```python
single: () (parentheses); in printf-style formatting
single: * (asterisk); in printf-style formatting
single: . (dot); in printf-style formatting

```

A conversion specifier contains two or more characters and has the following
components, which must occur in this order:

#. The `'%'` character, which marks the start of the specifier.

#. Mapping key (optional), consisting of a parenthesised sequence of characters
   (for example, `(somename)`).

#. Conversion flags (optional), which affect the result of some conversion
   types.

#. Minimum field width (optional).  If specified as an `'*'` (asterisk), the
   actual width is read from the next element of the tuple in *values*, and the
   object to convert comes after the minimum field width and optional precision.

#. Precision (optional), given as a `'.'` (dot) followed by the precision.  If
   specified as `'*'` (an asterisk), the actual precision is read from the next
   element of the tuple in *values*, and the value to convert comes after the
   precision.

#. Length modifier (optional).

#. Conversion type.

When the right argument is a dictionary (or other mapping type), then the
formats in the string *must* include a parenthesised mapping key into that
dictionary inserted immediately after the `'%'` character. The mapping key
selects the value to be formatted from the mapping.  For example:

   >>> print('%(language)s has %(number)03d quote types.' %
   ...       {'language': "Python", "number": 2})
   Python has 002 quote types.

In this case no `*` specifiers may occur in a format (since they require a
sequential parameter list).

The conversion flag characters are:

.. index

```python
single: # (hash); in printf-style formatting
single: - (minus); in printf-style formatting
single: + (plus); in printf-style formatting
single: space; in printf-style formatting

```

+---------+---------------------------------------------------------------------+
| Flag    | Meaning                                                             |
+=========+=====================================================================+
| `'#'` | The value conversion will use the "alternate form" (where defined   |
|         | below).                                                             |
+---------+---------------------------------------------------------------------+
| `'0'` | The conversion will be zero padded for numeric values.              |
+---------+---------------------------------------------------------------------+
| `'-'` | The converted value is left adjusted (overrides the `'0'`         |
|         | conversion if both are given).                                      |
+---------+---------------------------------------------------------------------+
| `' '` | (a space) A blank should be left before a positive number (or empty |
|         | string) produced by a signed conversion.                            |
+---------+---------------------------------------------------------------------+
| `'+'` | A sign character (`'+'` or `'-'`) will precede the conversion   |
|         | (overrides a "space" flag).                                         |
+---------+---------------------------------------------------------------------+

A length modifier (`h`, `l`, or `L`) may be present, but is ignored as it
is not necessary for Python -- so e.g. `%ld` is identical to `%d`.

The conversion types are:

+------------+-----------------------------------------------------+-------+
| Conversion | Meaning                                             | Notes |
+============+=====================================================+=======+
| `'d'`    | Signed integer decimal.                             |       |
+------------+-----------------------------------------------------+-------+
| `'i'`    | Signed integer decimal.                             |       |
+------------+-----------------------------------------------------+-------+
| `'o'`    | Signed octal value.                                 | \(1)  |
+------------+-----------------------------------------------------+-------+
| `'u'`    | Obsolete type -- it is identical to `'d'`.        | \(6)  |
+------------+-----------------------------------------------------+-------+
| `'x'`    | Signed hexadecimal (lowercase).                     | \(2)  |
+------------+-----------------------------------------------------+-------+
| `'X'`    | Signed hexadecimal (uppercase).                     | \(2)  |
+------------+-----------------------------------------------------+-------+
| `'e'`    | Floating-point exponential format (lowercase).      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'E'`    | Floating-point exponential format (uppercase).      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'f'`    | Floating-point decimal format.                      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'F'`    | Floating-point decimal format.                      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'g'`    | Floating-point format. Uses lowercase exponential   | \(4)  |
|            | format if exponent is less than -4 or not less than |       |
|            | precision, decimal format otherwise.                |       |
+------------+-----------------------------------------------------+-------+
| `'G'`    | Floating-point format. Uses uppercase exponential   | \(4)  |
|            | format if exponent is less than -4 or not less than |       |
|            | precision, decimal format otherwise.                |       |
+------------+-----------------------------------------------------+-------+
| `'c'`    | Single character (accepts integer or single         |       |
|            | character string).                                  |       |
+------------+-----------------------------------------------------+-------+
| `'r'`    | String (converts any Python object using            | \(5)  |
|            | `repr()`).                                      |       |
+------------+-----------------------------------------------------+-------+
| `'s'`    | String (converts any Python object using            | \(5)  |
|            | `str()`).                                       |       |
+------------+-----------------------------------------------------+-------+
| `'a'`    | String (converts any Python object using            | \(5)  |
|            | `ascii()`).                                     |       |
+------------+-----------------------------------------------------+-------+
| `'%'`    | No argument is converted, results in a `'%'`      |       |
|            | character in the result.                            |       |
+------------+-----------------------------------------------------+-------+

For floating-point formats, the result should be correctly rounded to the
specified precision.  The rounding mode matches that of the `round()` builtin.

Notes:

(1)
   The alternate form causes a leading octal specifier (`'0o'`) to be
   inserted before the first digit.

(2)
   The alternate form causes a leading `'0x'` or `'0X'` (depending on whether
   the `'x'` or `'X'` format was used) to be inserted before the first digit.

(3)
   The alternate form causes the result to always contain a decimal point, even if
   no digits follow it.

   The precision determines the number of digits after the decimal point and
   defaults to 6.

(4)
   The alternate form causes the result to always contain a decimal point, and
   trailing zeroes are not removed as they would otherwise be.

   The precision determines the number of significant digits before and after the
   decimal point and defaults to 6.

(5)
   If precision is `N`, the output is truncated to `N` characters.

(6)
   See `pep`.

Since Python strings have an explicit length, `%s` conversions do not assume
that `'\0'` is the end of the string.

   `%f` conversions for numbers whose absolute value is over 1e50 are no
   longer replaced by `%g` conversions.

.. index

```python
single: buffer protocol; binary sequence types

```

## Binary Sequence Types --- :class:`bytes`, :class:`bytearray`, :class:`memoryview`

.. index

```python
pair: object; bytes
pair: object; bytearray
pair: object; memoryview
pair: module; array

```

The core built-in types for manipulating binary data are `class` and
`class`. They are supported by `class` which uses
the `ref` to access the memory of other
binary objects without needing to make a copy.

The `mod` module supports efficient storage of basic data types like
32-bit integers and IEEE754 double-precision floating values.

### Bytes Objects

Bytes objects are immutable sequences of single bytes. Since many major
binary protocols are based on the ASCII text encoding, bytes objects offer
several methods that are only valid when working with ASCII compatible
data and are closely related to string objects in a variety of other ways.

### Class: `bytes(source=b'')`

           bytes(source, encoding, errors='strict')

   Firstly, the syntax for bytes literals is largely the same as that for string
   literals, except that a `b` prefix is added:

   * Single quotes: `b'still allows embedded "double" quotes'`
   * Double quotes: `b"still allows embedded 'single' quotes"`
   * Triple quoted: `b'''3 single quotes'''`, `b"""3 double quotes"""`

   Only ASCII characters are permitted in bytes literals (regardless of the
   declared source code encoding). Any binary values over 127 must be entered
   into bytes literals using the appropriate escape sequence.

   As with string literals, bytes literals may also use a `r` prefix to disable
   processing of escape sequences. See `ref` for more about the various
   forms of bytes literal, including supported escape sequences.

   While bytes literals and representations are based on ASCII text, bytes
   objects actually behave like immutable sequences of integers, with each
   value in the sequence restricted such that `0 <= x < 256` (attempts to
   violate this restriction will trigger `exc`). This is done
   deliberately to emphasise that while many binary formats include ASCII based
   elements and can be usefully manipulated with some text-oriented algorithms,
   this is not generally the case for arbitrary binary data (blindly applying
   text processing algorithms to binary data formats that are not ASCII
   compatible will usually lead to data corruption).

   In addition to the literal forms, bytes objects can be created in a number of
   other ways:

   * A zero-filled bytes object of a specified length: `bytes(10)`
   * From an iterable of integers: `bytes(range(20))`
   * Copying existing binary data via the buffer protocol:  `bytes(obj)`

   Also see the `ref` built-in.

   Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal
   numbers are a commonly used format for describing binary data. Accordingly,
   the bytes type has an additional class method to read data in that format:

   .. classmethod:: fromhex(string, /)

      This `class` class method returns a bytes object, decoding the
      given string object.  The string must contain two hexadecimal digits per
      byte, with ASCII whitespace being ignored.

      >>> bytes.fromhex('2Ef0 F1f2  ')
      b'.\xf0\xf1\xf2'

      .. versionchanged:: 3.7
         `bytes.fromhex()` now skips all ASCII whitespace in the string,
         not just spaces.

      .. versionchanged:: 3.14
         `bytes.fromhex()` now accepts ASCII `class` and
         `term` as input.

   A reverse conversion function exists to transform a bytes object into its
   hexadecimal representation.

   .. method:: hex(*, bytes_per_sep=1)
               hex(sep, bytes_per_sep=1)

      Return a string object containing two hexadecimal digits for each
      byte in the instance.

      >>> b'\xf0\xf1\xf2'.hex()
      'f0f1f2'

      If you want to make the hex string easier to read, you can specify a
      single character separator *sep* parameter to include in the output.
      By default, this separator will be included between each byte.
      A second optional *bytes_per_sep* parameter controls the spacing.
      Positive values calculate the separator position from the right,
      negative values from the left.

      >>> value = b'\xf0\xf1\xf2'
      >>> value.hex('-')
      'f0-f1-f2'
      >>> value.hex('_', 2)
      'f0_f1f2'
      >>> b'UUDDLRLRAB'.hex(' ', -4)
      '55554444 4c524c52 4142'

      .. versionadded:: 3.5

      .. versionchanged:: 3.8
         `bytes.hex()` now supports optional *sep* and *bytes_per_sep*
         parameters to insert separators between bytes in the hex output.

Since bytes objects are sequences of integers (akin to a tuple), for a bytes
object *b*, `b[0]` will be an integer, while `b[0:1]` will be a bytes
object of length 1.  (This contrasts with text strings, where both indexing
and slicing will produce a string of length 1)

The representation of bytes objects uses the literal format (`b'...'`)
since it is often more useful than e.g. `bytes([46, 46, 46])`.  You can
always convert a bytes object into a list of integers using `list(b)`.

### Bytearray Objects

`class` objects are a mutable counterpart to `class`
objects.

### Class: `bytearray(source=b'')`

           bytearray(source, encoding, errors='strict')

   There is no dedicated literal syntax for bytearray objects, instead
   they are always created by calling the constructor:

   * Creating an empty instance: `bytearray()`
   * Creating a zero-filled instance with a given length: `bytearray(10)`
   * From an iterable of integers: `bytearray(range(20))`
   * Copying existing binary data via the buffer protocol:  `bytearray(b'Hi!')`

   As bytearray objects are mutable, they support the
   `ref` sequence operations in addition to the
   common bytes and bytearray operations described in `ref`.

   Also see the `ref` built-in.

   Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal
   numbers are a commonly used format for describing binary data. Accordingly,
   the bytearray type has an additional class method to read data in that format:

   .. classmethod:: fromhex(string, /)

      This `class` class method returns a bytearray object, decoding
      the given string object.  The string must contain two hexadecimal digits
      per byte, with ASCII whitespace being ignored.

      >>> bytearray.fromhex('2Ef0 F1f2  ')
      bytearray(b'.\xf0\xf1\xf2')

      .. versionchanged:: 3.7
         `bytearray.fromhex()` now skips all ASCII whitespace in the string,
         not just spaces.

      .. versionchanged:: 3.14
         `bytearray.fromhex()` now accepts ASCII `class` and
         `term` as input.

   A reverse conversion function exists to transform a bytearray object into its
   hexadecimal representation.

   .. method:: hex(*, bytes_per_sep=1)
               hex(sep, bytes_per_sep=1)

      Return a string object containing two hexadecimal digits for each
      byte in the instance.

      >>> bytearray(b'\xf0\xf1\xf2').hex()
      'f0f1f2'

      .. versionadded:: 3.5

      .. versionchanged:: 3.8
         Similar to `bytes.hex()`, `bytearray.hex()` now supports
         optional *sep* and *bytes_per_sep* parameters to insert separators
         between bytes in the hex output.

   .. method:: resize(size, /)

      Resize the `class` to contain *size* bytes. *size* must be
      greater than or equal to 0.

      If the `class` needs to shrink, bytes beyond *size* are truncated.

      If the `class` needs to grow, all new bytes will be set to null
      bytes.

      This is equivalent to:

      >>> def resize(ba, size):
      ...     if len(ba) > size:
      ...         del ba[size:]
      ...     else:
      ...         ba += b'\0' * (size - len(ba))

      Examples:

      >>> shrink = bytearray(b'abc')
      >>> shrink.resize(1)
      >>> (shrink, len(shrink))
      (bytearray(b'a'), 1)
      >>> grow = bytearray(b'abc')
      >>> grow.resize(5)
      >>> (grow, len(grow))
      (bytearray(b'abc\x00\x00'), 5)

      .. versionadded:: 3.14

   .. method:: take_bytes(n=None, /)

      Remove the first *n* bytes from the bytearray and return them as an immutable
      `class`.
      By default (if *n* is `None`), return all bytes and clear the bytearray.

      If *n* is negative, index from the end and take the first `len()`
      plus *n* bytes. If *n* is out of bounds, raise `exc`.

      Taking less than the full length will leave remaining bytes in the
      `class`, which requires a copy. If the remaining bytes should be
      discarded, use `bytearray.resize()` or :keyword:`del` to truncate
      then `bytearray.take_bytes()` without a size.

.. impl-detail

```python

      Taking all bytes is a zero-copy operation.

   .. versionadded:: 3.15

      See the :ref:`What's New <whatsnew315-bytearray-take-bytes>` entry for
      common code patterns which can be optimized with
      :meth:`bytearray.take_bytes`.

```

Since bytearray objects are sequences of integers (akin to a list), for a
bytearray object *b*, `b[0]` will be an integer, while `b[0:1]` will be
a bytearray object of length 1.  (This contrasts with text strings, where
both indexing and slicing will produce a string of length 1)

The representation of bytearray objects uses the bytes literal format
(`bytearray(b'...')`) since it is often more useful than e.g.
`bytearray([46, 46, 46])`.  You can always convert a bytearray object into
a list of integers using `list(b)`.

.. seealso

```python

For detailed information on thread-safety guarantees for :class:`bytearray`
objects, see :ref:`thread-safety-bytearray`.

```

### Bytes and Bytearray Operations

           pair: bytearray; methods

Both bytes and bytearray objects support the `ref`
sequence operations. They interoperate not just with operands of the same
type, but with any `term`. Due to this flexibility, they can be
freely mixed in operations without causing errors. However, the return type
of the result may depend on the order of operands.

.. note

```python

The methods on bytes and bytearray objects don't accept strings as their
arguments, just as the methods on strings don't accept bytes as their
arguments.  For example, you have to write::

   a = "abc"
   b = a.replace("a", "f")

and::

   a = b"abc"
   b = a.replace(b"a", b"f")

```

Some bytes and bytearray operations assume the use of ASCII compatible
binary formats, and hence should be avoided when working with arbitrary
binary data. These restrictions are covered below.

.. note

```python
Using these ASCII based operations to manipulate binary data that is not
stored in an ASCII based format may lead to data corruption.

```

The following methods on bytes and bytearray objects can be used with
arbitrary binary data.

### Method: `bytes.count(sub[, start[, end]])`

            bytearray.count(sub[, start[, end]])

   Return the number of non-overlapping occurrences of subsequence *sub* in
   the range [*start*, *end*].  Optional arguments *start* and *end* are
   interpreted as in slice notation.

   The subsequence to search for may be any `term` or an
   integer in the range 0 to 255.

   If *sub* is empty, returns the number of empty slices between characters
   which is the length of the bytes object plus one.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.

### Method: `bytes.removeprefix(prefix, /)`

            bytearray.removeprefix(prefix, /)

   If the binary data starts with the *prefix* string, return
   `bytes[len(prefix):]`. Otherwise, return a copy of the original
binary data

```python

   >>> b'TestHook'.removeprefix(b'Test')
   b'Hook'
   >>> b'BaseTestCase'.removeprefix(b'Test')
   b'BaseTestCase'

The *prefix* may be any :term:`bytes-like object`.

.. note::

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

.. versionadded:: 3.9

```

### Method: `bytes.removesuffix(suffix, /)`

            bytearray.removesuffix(suffix, /)

   If the binary data ends with the *suffix* string and that *suffix* is
   not empty, return `bytes[:-len(suffix)]`.  Otherwise, return a copy of
the original binary data

```python

   >>> b'MiscTests'.removesuffix(b'Tests')
   b'Misc'
   >>> b'TmpDirMixin'.removesuffix(b'Tests')
   b'TmpDirMixin'

The *suffix* may be any :term:`bytes-like object`.

.. note::

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

.. versionadded:: 3.9

```

### Method: `bytes.decode(encoding="utf-8", errors="strict")`

            bytearray.decode(encoding="utf-8", errors="strict")

   Return the bytes decoded to a `class`.

   *encoding* defaults to `'utf-8'`;
   see `ref` for possible values.

   *errors* controls how decoding errors are handled.
   If `'strict'` (the default), a `exc` exception is raised.
   Other possible values are `'ignore'`, `'replace'`,
   and any other name registered via `codecs.register_error()`.
   See `ref` for details.

   For performance reasons, the value of *errors* is not checked for validity
   unless a decoding error actually occurs,
   `ref` is enabled or a `ref` is used.

.. note

```python

   Passing the *encoding* argument to :class:`str` allows decoding any
   :term:`bytes-like object` directly, without needing to make a temporary
   :class:`!bytes` or :class:`!bytearray` object.

.. versionchanged:: 3.1
   Added support for keyword arguments.

.. versionchanged:: 3.9
   The value of the *errors* argument is now checked in :ref:`devmode` and
   in :ref:`debug mode <debug-build>`.

```

### Method: `bytes.endswith(suffix[, start[, end]])`

            bytearray.endswith(suffix[, start[, end]])

   Return `True` if the binary data ends with the specified *suffix*,
   otherwise return `False`.  *suffix* can also be a tuple of suffixes to
   look for.  With optional *start*, test beginning at that position.  With
   optional *end*, stop comparing at that position.

   The suffix(es) to search for may be any `term`.

### Method: `bytes.find(sub[, start[, end]])`

            bytearray.find(sub[, start[, end]])

   Return the lowest index in the data where the subsequence *sub* is found,
   such that *sub* is contained in the slice `s[start:end]`.  Optional
   arguments *start* and *end* are interpreted as in slice notation.  Return
   `-1` if *sub* is not found.

   The subsequence to search for may be any `term` or an
   integer in the range 0 to 255.

.. note

```python

   The :meth:`~bytes.find` method should be used only if you need to know the
   position of *sub*.  To check if *sub* is a substring or not, use the
   :keyword:`in` operator::

      >>> b'Py' in b'Python'
      True

.. versionchanged:: 3.3
   Also accept an integer in the range 0 to 255 as the subsequence.

```

### Method: `bytes.index(sub[, start[, end]])`

            bytearray.index(sub[, start[, end]])

   Like `bytes.find()`, but raise `exc` when the
   subsequence is not found.

   The subsequence to search for may be any `term` or an
   integer in the range 0 to 255.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.

### Method: `bytes.join(iterable, /)`

            bytearray.join(iterable, /)

   Return a bytes or bytearray object which is the concatenation of the
   binary data sequences in *iterable*.  A `exc` will be raised
   if there are any values in *iterable* that are not :term:`bytes-like
   objects <bytes-like object>`, including `class` objects.  The
   separator between elements is the contents of the bytes or
   bytearray object providing this method.

                  bytearray.maketrans(from, to, /)

   This static method returns a translation table usable for
   `bytes.translate()` that will map each character in *from* into the
   character at the same position in *to*; *from* and *to* must both be
   `term` and have the same length.

   .. versionadded:: 3.1

### Method: `bytes.partition(sep, /)`

            bytearray.partition(sep, /)

   Split the sequence at the first occurrence of *sep*, and return a 3-tuple
   containing the part before the separator, the separator itself or its
   bytearray copy, and the part after the separator.
   If the separator is not found, return a 3-tuple
   containing a copy of the original sequence, followed by two empty bytes or
   bytearray objects.

   The separator to search for may be any `term`.

### Method: `bytes.replace(old, new, /, count=-1)`

            bytearray.replace(old, new, /, count=-1)

   Return a copy of the sequence with all occurrences of subsequence *old*
   replaced by *new*.  If *count* is given, only the first *count* occurrences
   are replaced.  If *count* is not specified or `-1`, then all occurrences
   are replaced.

   The subsequence to search for and its replacement may be any
   `term`.

.. note

```python

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

.. versionchanged:: 3.15
   *count* is now supported as a keyword argument.

```

### Method: `bytes.rfind(sub[, start[, end]])`

            bytearray.rfind(sub[, start[, end]])

   Return the highest index in the sequence where the subsequence *sub* is
   found, such that *sub* is contained within `s[start:end]`.  Optional
   arguments *start* and *end* are interpreted as in slice notation. Return
   `-1` on failure.

   The subsequence to search for may be any `term` or an
   integer in the range 0 to 255.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.

### Method: `bytes.rindex(sub[, start[, end]])`

            bytearray.rindex(sub[, start[, end]])

   Like `bytes.rfind()` but raises `exc` when the
   subsequence *sub* is not found.

   The subsequence to search for may be any `term` or an
   integer in the range 0 to 255.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.

### Method: `bytes.rpartition(sep, /)`

            bytearray.rpartition(sep, /)

   Split the sequence at the last occurrence of *sep*, and return a 3-tuple
   containing the part before the separator, the separator itself or its
   bytearray copy, and the part after the separator.
   If the separator is not found, return a 3-tuple
   containing two empty bytes or bytearray objects, followed by a copy of the
   original sequence.

   The separator to search for may be any `term`.

### Method: `bytes.startswith(prefix[, start[, end]])`

            bytearray.startswith(prefix[, start[, end]])

   Return `True` if the binary data starts with the specified *prefix*,
   otherwise return `False`.  *prefix* can also be a tuple of prefixes to
   look for.  With optional *start*, test beginning at that position.  With
   optional *end*, stop comparing at that position.

   The prefix(es) to search for may be any `term`.

### Method: `bytes.translate(table, /, delete=b'')`

            bytearray.translate(table, /, delete=b'')

   Return a copy of the bytes or bytearray object where all bytes occurring in
   the optional argument *delete* are removed, and the remaining bytes have
   been mapped through the given translation table, which must be a bytes
   object of length 256.

   You can use the `bytes.maketrans()` method to create a translation
   table.

   Set the *table* argument to `None` for translations that only delete
characters

```python

   >>> b'read this short text'.translate(None, b'aeiou')
   b'rd ths shrt txt'

.. versionchanged:: 3.6
   *delete* is now supported as a keyword argument.

```

The following methods on bytes and bytearray objects have default behaviours
that assume the use of ASCII compatible binary formats, but can still be used
with arbitrary binary data by passing appropriate arguments. Note that all of
the bytearray methods in this section do *not* operate in place, and instead
produce new objects.

### Method: `bytes.center(width, fillbyte=b' ', /)`

            bytearray.center(width, fillbyte=b' ', /)

   Return a copy of the object centered in a sequence of length *width*.
   Padding is done using the specified *fillbyte* (default is an ASCII
   space). For `class` objects, the original sequence is returned if
   *width* is less than or equal to `len(s)`.

.. note

```python

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

```

### Method: `bytes.ljust(width, fillbyte=b' ', /)`

            bytearray.ljust(width, fillbyte=b' ', /)

   Return a copy of the object left justified in a sequence of length *width*.
   Padding is done using the specified *fillbyte* (default is an ASCII
   space). For `class` objects, the original sequence is returned if
   *width* is less than or equal to `len(s)`.

.. note

```python

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

```

### Method: `bytes.lstrip(bytes=None, /)`

            bytearray.lstrip(bytes=None, /)

   Return a copy of the sequence with specified leading bytes removed.  The
   *bytes* argument is a binary sequence specifying the set of byte values to
   be removed.  If omitted or `None`, the *bytes* argument defaults
   to removing `ASCII whitespace <bytes.isspace>()`.
   The *bytes* argument is not a prefix;
rather, all combinations of its values are stripped

```python

   >>> b'   spacious   '.lstrip()
   b'spacious   '
   >>> b'www.example.com'.lstrip(b'cmowz.')
   b'example.com'

The binary sequence of byte values to remove may be any
:term:`bytes-like object`. See :meth:`~bytes.removeprefix` for a method
that will remove a single prefix string rather than all of a set of
characters.  For example::

   >>> b'Arthur: three!'.lstrip(b'Arthur: ')
   b'ee!'
   >>> b'Arthur: three!'.removeprefix(b'Arthur: ')
   b'three!'

.. note::

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

```

### Method: `bytes.rjust(width, fillbyte=b' ', /)`

            bytearray.rjust(width, fillbyte=b' ', /)

   Return a copy of the object right justified in a sequence of length *width*.
   Padding is done using the specified *fillbyte* (default is an ASCII
   space). For `class` objects, the original sequence is returned if
   *width* is less than or equal to `len(s)`.

.. note

```python

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

```

### Method: `bytes.rsplit(sep=None, maxsplit=-1)`

            bytearray.rsplit(sep=None, maxsplit=-1)

   Split the binary sequence into subsequences of the same type, using *sep*
   as the delimiter string. If *maxsplit* is given, at most *maxsplit* splits
   are done, the *rightmost* ones.  If *sep* is not specified or `None`,
   any subsequence consisting solely of
   `ASCII whitespace <bytes.isspace>()` is a separator.
   Except for splitting from the right, `rsplit()` behaves like
   `split()` which is described in detail below.

### Method: `bytes.rstrip(bytes=None, /)`

            bytearray.rstrip(bytes=None, /)

   Return a copy of the sequence with specified trailing bytes removed.  The
   *bytes* argument is a binary sequence specifying the set of byte values to
   be removed.  If omitted or `None`, the *bytes* argument defaults to
   removing `ASCII whitespace <bytes.isspace>()`.
   The *bytes* argument is not a suffix; rather,
all combinations of its values are stripped

```python

   >>> b'   spacious   '.rstrip()
   b'   spacious'
   >>> b'mississippi'.rstrip(b'ipz')
   b'mississ'

The binary sequence of byte values to remove may be any
:term:`bytes-like object`. See :meth:`~bytes.removesuffix` for a method
that will remove a single suffix string rather than all of a set of
characters.  For example::

   >>> b'Monty Python'.rstrip(b' Python')
   b'M'
   >>> b'Monty Python'.removesuffix(b' Python')
   b'Monty'

.. note::

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

```

### Method: `bytes.split(sep=None, maxsplit=-1)`

            bytearray.split(sep=None, maxsplit=-1)

   Split the binary sequence into subsequences of the same type, using *sep*
   as the delimiter string. If *maxsplit* is given and non-negative, at most
   *maxsplit* splits are done (thus, the list will have at most `maxsplit+1`
   elements).  If *maxsplit* is not specified or is `-1`, then there is no
   limit on the number of splits (all possible splits are made).

   If *sep* is given, consecutive delimiters are not grouped together and are
   deemed to delimit empty subsequences (for example, `b'1,,2'.split(b',')`
   returns `[b'1', b'', b'2']`).  The *sep* argument may consist of a
   multibyte sequence as a single delimiter. Splitting an empty sequence with
   a specified separator returns `[b'']` or `[bytearray(b'')]` depending
   on the type of object being split.  The *sep* argument may be any
   `term`.

For example

```python

   >>> b'1,2,3'.split(b',')
   [b'1', b'2', b'3']
   >>> b'1,2,3'.split(b',', maxsplit=1)
   [b'1', b'2,3']
   >>> b'1,2,,3,'.split(b',')
   [b'1', b'2', b'', b'3', b'']
   >>> b'1<>2<>3<4'.split(b'<>')
   [b'1', b'2', b'3<4']

If *sep* is not specified or is ``None``, a different splitting algorithm
is applied: runs of consecutive :meth:`ASCII whitespace <bytes.isspace>`
are regarded as a single
separator, and the result will contain no empty strings at the start or
end if the sequence has leading or trailing whitespace.  Consequently,
splitting an empty sequence or a sequence consisting solely of ASCII
whitespace without a specified separator returns ``[]``.

For example::

   >>> b'1 2 3'.split()
   [b'1', b'2', b'3']
   >>> b'1 2 3'.split(maxsplit=1)
   [b'1', b'2 3']
   >>> b'   1   2   3   '.split()
   [b'1', b'2', b'3']

```

### Method: `bytes.strip(bytes=None, /)`

            bytearray.strip(bytes=None, /)

   Return a copy of the sequence with specified leading and trailing bytes
   removed. The *bytes* argument is a binary sequence specifying the set of
   byte values to be removed.  If omitted or `None`, the *bytes*
   argument defaults to removing `ASCII whitespace <bytes.isspace>()`.
   The *bytes* argument is
   not a prefix or suffix; rather, all combinations of its values are
stripped

```python

   >>> b'   spacious   '.strip()
   b'spacious'
   >>> b'www.example.com'.strip(b'cmowz.')
   b'example'

The binary sequence of byte values to remove may be any
:term:`bytes-like object`.

.. note::

   The bytearray version of this method does *not* operate in place -
   it always produces a new object, even if no changes were made.

```

The following methods on bytes and bytearray objects assume the use of ASCII
compatible binary formats and should not be applied to arbitrary binary data.
Note that all of the bytearray methods in this section do *not* operate in
place, and instead produce new objects.

### Method: `bytes.capitalize()`

            bytearray.capitalize()

   Return a copy of the sequence with each byte interpreted as an ASCII
   character, and the first byte capitalized and the rest lowercased.
   Non-ASCII byte values are passed through unchanged.

.. note

```python

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

```

### Method: `bytes.expandtabs(tabsize=8)`

            bytearray.expandtabs(tabsize=8)

   Return a copy of the sequence where all ASCII tab characters are replaced
   by one or more ASCII spaces, depending on the current column and the given
   tab size.  Tab positions occur every *tabsize* bytes (default is 8,
   giving tab positions at columns 0, 8, 16 and so on).  To expand the
   sequence, the current column is set to zero and the sequence is examined
   byte by byte.  If the byte is an ASCII tab character (`b'\t'`), one or
   more space characters are inserted in the result until the current column
   is equal to the next tab position. (The tab character itself is not
   copied.)  If the current byte is an ASCII newline (`b'\n'`) or
   carriage return (`b'\r'`), it is copied and the current column is reset
   to zero.  Any other byte value is copied unchanged and the current column
   is incremented by one regardless of how the byte value is represented when
printed

```python

   >>> b'01\t012\t0123\t01234'.expandtabs()
   b'01      012     0123    01234'
   >>> b'01\t012\t0123\t01234'.expandtabs(4)
   b'01  012 0123    01234'

.. note::

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

```

### Method: `bytes.isalnum()`

            bytearray.isalnum()

   Return `True` if all bytes in the sequence are alphabetical ASCII characters
   or ASCII decimal digits and the sequence is not empty, `False` otherwise.
   Alphabetic ASCII characters are those byte values in the sequence
   `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`. ASCII decimal
   digits are those byte values in the sequence `b'0123456789'`.

For example

```python

   >>> b'ABCabc1'.isalnum()
   True
   >>> b'ABC abc1'.isalnum()
   False

```

### Method: `bytes.isalpha()`

            bytearray.isalpha()

   Return `True` if all bytes in the sequence are alphabetic ASCII characters
   and the sequence is not empty, `False` otherwise.  Alphabetic ASCII
   characters are those byte values in the sequence
   `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

For example

```python

   >>> b'ABCabc'.isalpha()
   True
   >>> b'ABCabc1'.isalpha()
   False

```

### Method: `bytes.isascii()`

            bytearray.isascii()

   Return `True` if the sequence is empty or all bytes in the sequence are ASCII,
   `False` otherwise.
   ASCII bytes are in the range 0-0x7F.

   .. versionadded:: 3.7

### Method: `bytes.isdigit()`

            bytearray.isdigit()

   Return `True` if all bytes in the sequence are ASCII decimal digits
   and the sequence is not empty, `False` otherwise. ASCII decimal digits are
   those byte values in the sequence `b'0123456789'`.

For example

```python

   >>> b'1234'.isdigit()
   True
   >>> b'1.23'.isdigit()
   False

```

### Method: `bytes.islower()`

            bytearray.islower()

   Return `True` if there is at least one lowercase ASCII character
   in the sequence and no uppercase ASCII characters, `False` otherwise.

For example

```python

   >>> b'hello world'.islower()
   True
   >>> b'Hello world'.islower()
   False

Lowercase ASCII characters are those byte values in the sequence
``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

```

### Method: `bytes.isspace()`

            bytearray.isspace()

   Return `True` if all bytes in the sequence are ASCII whitespace and the
   sequence is not empty, `False` otherwise.  ASCII whitespace characters are
   those byte values in the sequence `b' \t\n\r\x0b\f'` (space, tab, newline,
   carriage return, vertical tab, form feed).

### Method: `bytes.istitle()`

            bytearray.istitle()

   Return `True` if the sequence is ASCII titlecase and the sequence is not
   empty, `False` otherwise. See `bytes.title()` for more details on the
   definition of "titlecase".

For example

```python

   >>> b'Hello World'.istitle()
   True
   >>> b'Hello world'.istitle()
   False

```

### Method: `bytes.isupper()`

            bytearray.isupper()

   Return `True` if there is at least one uppercase alphabetic ASCII character
   in the sequence and no lowercase ASCII characters, `False` otherwise.

For example

```python

   >>> b'HELLO WORLD'.isupper()
   True
   >>> b'Hello world'.isupper()
   False

Lowercase ASCII characters are those byte values in the sequence
``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

```

### Method: `bytes.lower()`

            bytearray.lower()

   Return a copy of the sequence with all the uppercase ASCII characters
   converted to their corresponding lowercase counterpart.

For example

```python

   >>> b'Hello World'.lower()
   b'hello world'

Lowercase ASCII characters are those byte values in the sequence
``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

.. note::

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

```

.. index

```python
single: universal newlines; bytes.splitlines method
single: universal newlines; bytearray.splitlines method

```

### Method: `bytes.splitlines(keepends=False)`

            bytearray.splitlines(keepends=False)

   Return a list of the lines in the binary sequence, breaking at ASCII
   line boundaries. This method uses the `term` approach
   to splitting lines. Line breaks are not included in the resulting list
   unless *keepends* is given and true.

For example

```python

   >>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
   [b'ab c', b'', b'de fg', b'kl']
   >>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
   [b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']

Unlike :meth:`~bytes.split` when a delimiter string *sep* is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line::

   >>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
   ([b''], [b'Two lines', b''])
   >>> b"".splitlines(), b"One line\n".splitlines()
   ([], [b'One line'])

```

### Method: `bytes.swapcase()`

            bytearray.swapcase()

   Return a copy of the sequence with all the lowercase ASCII characters
   converted to their corresponding uppercase counterpart and vice-versa.

For example

```python

   >>> b'Hello World'.swapcase()
   b'hELLO wORLD'

Lowercase ASCII characters are those byte values in the sequence
``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

Unlike :func:`str.swapcase`, it is always the case that
``bin.swapcase().swapcase() == bin`` for the binary versions. Case
conversions are symmetrical in ASCII, even though that is not generally
true for arbitrary Unicode code points.

.. note::

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

```

### Method: `bytes.title()`

            bytearray.title()

   Return a titlecased version of the binary sequence where words start with
   an uppercase ASCII character and the remaining characters are lowercase.
   Uncased byte values are left unmodified.

For example

```python

   >>> b'Hello world'.title()
   b'Hello World'

Lowercase ASCII characters are those byte values in the sequence
``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.
All other byte values are uncased.

The algorithm uses a simple language-independent definition of a word as
groups of consecutive letters.  The definition works in many contexts but
it means that apostrophes in contractions and possessives form word
boundaries, which may not be the desired result::

     >>> b"they're bill's friends from the UK".title()
     b"They'Re Bill'S Friends From The Uk"

A workaround for apostrophes can be constructed using regular expressions::

     >>> import re
     >>> def titlecase(s):
     ...     return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
     ...                   lambda mo: mo.group(0)[0:1].upper() +
     ...                              mo.group(0)[1:].lower(),
     ...                   s)
     ...
     >>> titlecase(b"they're bill's friends.")
     b"They're Bill's Friends."

.. note::

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

```

### Method: `bytes.upper()`

            bytearray.upper()

   Return a copy of the sequence with all the lowercase ASCII characters
   converted to their corresponding uppercase counterpart.

For example

```python

   >>> b'Hello World'.upper()
   b'HELLO WORLD'

Lowercase ASCII characters are those byte values in the sequence
``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

.. note::

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

```

### Method: `bytes.zfill(width, /)`

            bytearray.zfill(width, /)

   Return a copy of the sequence left filled with ASCII `b'0'` digits to
   make a sequence of length *width*. A leading sign prefix (`b'+'`/
   `b'-'`) is handled by inserting the padding *after* the sign character
   rather than before. For `class` objects, the original sequence is
   returned if *width* is less than or equal to `len(seq)`.

For example

```python

   >>> b"42".zfill(5)
   b'00042'
   >>> b"-42".zfill(5)
   b'-0042'

.. note::

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

```

### ``printf``-style Bytes Formatting

.. index

```python
single: formatting; bytes (%)
single: formatting; bytearray (%)
single: interpolation; bytes (%)
single: interpolation; bytearray (%)
single: bytes; formatting
single: bytearray; formatting
single: bytes; interpolation
single: bytearray; interpolation
single: printf-style formatting
single: sprintf-style formatting
single: % (percent); printf-style formatting

```

.. note

```python

The formatting operations described here exhibit a variety of quirks that
lead to a number of common errors (such as failing to display tuples and
dictionaries correctly).  If the value being printed may be a tuple or
dictionary, wrap it in a tuple.

```

Bytes objects (`bytes`/`bytearray`) have one unique built-in operation:
the `%` operator (modulo).
This is also known as the bytes *formatting* or *interpolation* operator.
Given `format % values` (where *format* is a bytes object), `%` conversion
specifications in *format* are replaced with zero or more elements of *values*.
The effect is similar to using the :c`sprintf()` function in the C language.

If *format* requires a single argument, *values* may be a single non-tuple
object. [5]_  Otherwise, *values* must be a tuple with exactly the number of
items specified by the format bytes object, or a single mapping object (for
example, a dictionary).

.. index

```python
single: () (parentheses); in printf-style formatting
single: * (asterisk); in printf-style formatting
single: . (dot); in printf-style formatting

```

A conversion specifier contains two or more characters and has the following
components, which must occur in this order:

#. The `'%'` character, which marks the start of the specifier.

#. Mapping key (optional), consisting of a parenthesised sequence of characters
   (for example, `(somename)`).

#. Conversion flags (optional), which affect the result of some conversion
   types.

#. Minimum field width (optional).  If specified as an `'*'` (asterisk), the
   actual width is read from the next element of the tuple in *values*, and the
   object to convert comes after the minimum field width and optional precision.

#. Precision (optional), given as a `'.'` (dot) followed by the precision.  If
   specified as `'*'` (an asterisk), the actual precision is read from the next
   element of the tuple in *values*, and the value to convert comes after the
   precision.

#. Length modifier (optional).

#. Conversion type.

When the right argument is a dictionary (or other mapping type), then the
formats in the bytes object *must* include a parenthesised mapping key into that
dictionary inserted immediately after the `'%'` character. The mapping key
selects the value to be formatted from the mapping.  For example:

   >>> print(b'%(language)s has %(number)03d quote types.' %
   ...       {b'language': b"Python", b"number": 2})
   b'Python has 002 quote types.'

In this case no `*` specifiers may occur in a format (since they require a
sequential parameter list).

The conversion flag characters are:

.. index

```python
single: # (hash); in printf-style formatting
single: - (minus); in printf-style formatting
single: + (plus); in printf-style formatting
single: space; in printf-style formatting

```

+---------+---------------------------------------------------------------------+
| Flag    | Meaning                                                             |
+=========+=====================================================================+
| `'#'` | The value conversion will use the "alternate form" (where defined   |
|         | below).                                                             |
+---------+---------------------------------------------------------------------+
| `'0'` | The conversion will be zero padded for numeric values.              |
+---------+---------------------------------------------------------------------+
| `'-'` | The converted value is left adjusted (overrides the `'0'`         |
|         | conversion if both are given).                                      |
+---------+---------------------------------------------------------------------+
| `' '` | (a space) A blank should be left before a positive number (or empty |
|         | string) produced by a signed conversion.                            |
+---------+---------------------------------------------------------------------+
| `'+'` | A sign character (`'+'` or `'-'`) will precede the conversion   |
|         | (overrides a "space" flag).                                         |
+---------+---------------------------------------------------------------------+

A length modifier (`h`, `l`, or `L`) may be present, but is ignored as it
is not necessary for Python -- so e.g. `%ld` is identical to `%d`.

The conversion types are:

+------------+-----------------------------------------------------+-------+
| Conversion | Meaning                                             | Notes |
+============+=====================================================+=======+
| `'d'`    | Signed integer decimal.                             |       |
+------------+-----------------------------------------------------+-------+
| `'i'`    | Signed integer decimal.                             |       |
+------------+-----------------------------------------------------+-------+
| `'o'`    | Signed octal value.                                 | \(1)  |
+------------+-----------------------------------------------------+-------+
| `'u'`    | Obsolete type -- it is identical to `'d'`.        | \(8)  |
+------------+-----------------------------------------------------+-------+
| `'x'`    | Signed hexadecimal (lowercase).                     | \(2)  |
+------------+-----------------------------------------------------+-------+
| `'X'`    | Signed hexadecimal (uppercase).                     | \(2)  |
+------------+-----------------------------------------------------+-------+
| `'e'`    | Floating-point exponential format (lowercase).      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'E'`    | Floating-point exponential format (uppercase).      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'f'`    | Floating-point decimal format.                      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'F'`    | Floating-point decimal format.                      | \(3)  |
+------------+-----------------------------------------------------+-------+
| `'g'`    | Floating-point format. Uses lowercase exponential   | \(4)  |
|            | format if exponent is less than -4 or not less than |       |
|            | precision, decimal format otherwise.                |       |
+------------+-----------------------------------------------------+-------+
| `'G'`    | Floating-point format. Uses uppercase exponential   | \(4)  |
|            | format if exponent is less than -4 or not less than |       |
|            | precision, decimal format otherwise.                |       |
+------------+-----------------------------------------------------+-------+
| `'c'`    | Single byte (accepts integer or single              |       |
|            | byte objects).                                      |       |
+------------+-----------------------------------------------------+-------+
| `'b'`    | Bytes (any object that follows the                  | \(5)  |
|            | `ref` or has       |       |
|            | `object.__bytes__()`).                         |       |
+------------+-----------------------------------------------------+-------+
| `'s'`    | `'s'` is an alias for `'b'` and should only     | \(6)  |
|            | be used for Python2/3 code bases.                   |       |
+------------+-----------------------------------------------------+-------+
| `'a'`    | Bytes (converts any Python object using             | \(5)  |
|            | `repr(obj).encode('ascii', 'backslashreplace')`). |       |
+------------+-----------------------------------------------------+-------+
| `'r'`    | `'r'` is an alias for `'a'` and should only     | \(7)  |
|            | be used for Python2/3 code bases.                   |       |
+------------+-----------------------------------------------------+-------+
| `'%'`    | No argument is converted, results in a `'%'`      |       |
|            | character in the result.                            |       |
+------------+-----------------------------------------------------+-------+

Notes:

(1)
   The alternate form causes a leading octal specifier (`'0o'`) to be
   inserted before the first digit.

(2)
   The alternate form causes a leading `'0x'` or `'0X'` (depending on whether
   the `'x'` or `'X'` format was used) to be inserted before the first digit.

(3)
   The alternate form causes the result to always contain a decimal point, even if
   no digits follow it.

   The precision determines the number of digits after the decimal point and
   defaults to 6.

(4)
   The alternate form causes the result to always contain a decimal point, and
   trailing zeroes are not removed as they would otherwise be.

   The precision determines the number of significant digits before and after the
   decimal point and defaults to 6.

(5)
   If precision is `N`, the output is truncated to `N` characters.

(6)
   `b'%s'` is deprecated, but will not be removed during the 3.x series.

(7)
   `b'%r'` is deprecated, but will not be removed during the 3.x series.

(8)
   See `pep`.

.. note

```python

The bytearray version of this method does *not* operate in place - it
always produces a new object, even if no changes were made.

```

.. seealso

```python

:pep:`461` - Adding % formatting to bytes and bytearray

```

### Memory Views

`class` objects allow Python code to access the internal data
of an object that supports the `ref` without
copying.

### Class: `memoryview(object)`

   Create a `class` that references *object*.  *object* must
   support the buffer protocol.  Built-in objects that support the buffer
   protocol include `class` and `class`.

   A `class` has the notion of an *element*, which is the
   atomic memory unit handled by the originating *object*.  For many simple
   types such as `class` and `class`, an element is a single
   byte, but other types such as `class` may have bigger elements.

   `class`\s are `ref` over the type of their
   underlying data.

   `len(view)` is equal to the length of `memoryview.tolist()`, which
   is the nested list representation of the view. If `view.ndim == 1`,
   this is equal to the number of elements in the view.

   .. versionchanged:: 3.12
      If `view.ndim == 0`, `len(view)` now raises `exc` instead of returning 1.

   The `class` attribute will give you the number of
   bytes in a single element.

   A `class` supports slicing and indexing to expose its data.
One-dimensional slicing will result in a subview

```python

 >>> v = memoryview(b'abcefg')
 >>> v[1]
 98
 >>> v[-1]
 103
 >>> v[1:4]
 <memory at 0x7f3ddc9f4350>
 >>> bytes(v[1:4])
 b'bce'

If :class:`~memoryview.format` is one of the native format specifiers
from the :mod:`struct` module, indexing with an integer or a tuple of
integers is also supported and returns a single *element* with
the correct type.  One-dimensional memoryviews can be indexed
with an integer or a one-integer tuple.  Multi-dimensional memoryviews
can be indexed with tuples of exactly *ndim* integers where *ndim* is
the number of dimensions.  Zero-dimensional memoryviews can be indexed
with the empty tuple.

Here is an example with a non-byte format::

   >>> import array
   >>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
   >>> m = memoryview(a)
   >>> m[0]
   -11111111
   >>> m[-1]
   44444444
   >>> m[::2].tolist()
   [-11111111, -33333333]

If the underlying object is writable, the memoryview supports
one-dimensional slice assignment. Resizing is not allowed::

   >>> data = bytearray(b'abcefg')
   >>> v = memoryview(data)
   >>> v.readonly
   False
   >>> v[0] = ord(b'z')
   >>> data
   bytearray(b'zbcefg')
   >>> v[1:4] = b'123'
   >>> data
   bytearray(b'z123fg')
   >>> v[2:3] = b'spam'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: memoryview assignment: lvalue and rvalue have different structures
   >>> v[2:6] = b'spam'
   >>> data
   bytearray(b'z1spam')

One-dimensional memoryviews of :term:`hashable` (read-only) types with formats
'B', 'b' or 'c' are also hashable. The hash is defined as
``hash(m) == hash(m.tobytes())``::

   >>> v = memoryview(b'abcefg')
   >>> hash(v) == hash(b'abcefg')
   True
   >>> hash(v[2:4]) == hash(b'ce')
   True
   >>> hash(v[::-2]) == hash(b'abcefg'[::-2])
   True

.. versionchanged:: 3.3
   One-dimensional memoryviews can now be sliced.
   One-dimensional memoryviews with formats 'B', 'b' or 'c' are now :term:`hashable`.

.. versionchanged:: 3.4
   memoryview is now registered automatically with
   :class:`collections.abc.Sequence`

.. versionchanged:: 3.5
   memoryviews can now be indexed with a tuple of integers.

.. versionchanged:: 3.14
   memoryview is now a :term:`generic type`.

:class:`memoryview` has several methods:

.. method:: __eq__(exporter)

   A memoryview and a :pep:`3118` exporter are equal if their shapes are
   equivalent and if all corresponding values are equal when the operands'
   respective format codes are interpreted using :mod:`struct` syntax.

   For the subset of :mod:`struct` format strings currently supported by
   :meth:`tolist`, ``v`` and ``w`` are equal if ``v.tolist() == w.tolist()``::

      >>> import array
      >>> a = array.array('I', [1, 2, 3, 4, 5])
      >>> b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
      >>> c = array.array('b', [5, 3, 1])
      >>> x = memoryview(a)
      >>> y = memoryview(b)
      >>> x == a == y == b
      True
      >>> x.tolist() == a.tolist() == y.tolist() == b.tolist()
      True
      >>> z = y[::-2]
      >>> z == c
      True
      >>> z.tolist() == c.tolist()
      True

   If either format string is not supported by the :mod:`struct` module,
   then the objects will always compare as unequal (even if the format
   strings and buffer contents are identical)::

      >>> from ctypes import BigEndianStructure, c_long
      >>> class BEPoint(BigEndianStructure):
      ...     _fields_ = [("x", c_long), ("y", c_long)]
      ...
      >>> point = BEPoint(100, 200)
      >>> a = memoryview(point)
      >>> b = memoryview(point)
      >>> a == point
      False
      >>> a == b
      False

   Note that, as with floating-point numbers, ``v is w`` does *not* imply
   ``v == w`` for memoryview objects.

   .. versionchanged:: 3.3
      Previous versions compared the raw memory disregarding the item format
      and the logical array structure.

.. method:: tobytes(order='C')

   Return the data in the buffer as a bytestring.  This is equivalent to
   calling the :class:`bytes` constructor on the memoryview. ::

      >>> m = memoryview(b"abc")
      >>> m.tobytes()
      b'abc'
      >>> bytes(m)
      b'abc'

   For non-contiguous arrays the result is equal to the flattened list
   representation with all elements converted to bytes. :meth:`tobytes`
   supports all format strings, including those that are not in
   :mod:`struct` module syntax.

   .. versionadded:: 3.8
      *order* can be {'C', 'F', 'A'}.  When *order* is 'C' or 'F', the data
      of the original array is converted to C or Fortran order. For contiguous
      views, 'A' returns an exact copy of the physical memory. In particular,
      in-memory Fortran order is preserved. For non-contiguous views, the
      data is converted to C first. *order=None* is the same as *order='C'*.

.. method:: hex(*, bytes_per_sep=1)
            hex(sep, bytes_per_sep=1)

   Return a string object containing two hexadecimal digits for each
   byte in the buffer. ::

      >>> m = memoryview(b"abc")
      >>> m.hex()
      '616263'

   .. versionadded:: 3.5

   .. versionchanged:: 3.8
      Similar to :meth:`bytes.hex`, :meth:`memoryview.hex` now supports
      optional *sep* and *bytes_per_sep* parameters to insert separators
      between bytes in the hex output.

.. method:: tolist()

   Return the data in the buffer as a list of elements. ::

      >>> memoryview(b'abc').tolist()
      [97, 98, 99]
      >>> import array
      >>> a = array.array('d', [1.1, 2.2, 3.3])
      >>> m = memoryview(a)
      >>> m.tolist()
      [1.1, 2.2, 3.3]

   .. versionchanged:: 3.3
      :meth:`tolist` now supports all single character native formats in
      :mod:`struct` module syntax as well as multi-dimensional
      representations.

.. method:: toreadonly()

   Return a readonly version of the memoryview object.  The original
   memoryview object is unchanged. ::

      >>> m = memoryview(bytearray(b'abc'))
      >>> mm = m.toreadonly()
      >>> mm.tolist()
      [97, 98, 99]
      >>> mm[0] = 42
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      TypeError: cannot modify read-only memory
      >>> m[0] = 43
      >>> mm.tolist()
      [43, 98, 99]

   .. versionadded:: 3.8

.. method:: release()

   Release the underlying buffer exposed by the memoryview object.  Many
   objects take special actions when a view is held on them (for example,
   a :class:`bytearray` would temporarily forbid resizing); therefore,
   calling release() is handy to remove these restrictions (and free any
   dangling resources) as soon as possible.

   After this method has been called, any further operation on the view
   raises a :class:`ValueError` (except :meth:`release` itself which can
   be called multiple times)::

      >>> m = memoryview(b'abc')
      >>> m.release()
      >>> m[0]
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      ValueError: operation forbidden on released memoryview object

   The context management protocol can be used for a similar effect,
   using the ``with`` statement::

      >>> with memoryview(b'abc') as m:
      ...     m[0]
      ...
      97
      >>> m[0]
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      ValueError: operation forbidden on released memoryview object

   .. versionadded:: 3.2

.. method:: cast(format, /)
            cast(format, shape, /, *, order='C')

   Cast a memoryview to a new format or shape. *shape* defaults to
   ``[byte_length//new_itemsize]``, which means that the result view
   will be one-dimensional. The return value is a new memoryview, but
   the buffer itself is not copied. Supported casts are
   1D -> C-:term:`contiguous`, C-contiguous -> 1D, and
   F-contiguous -> 1D.

   With a multidimensional *shape*, *order* selects the memory layout of
   the result: ``'C'`` for C-contiguous (row-major, the default) or ``'F'``
   for Fortran-contiguous (column-major).  The buffer is still not copied,
   so ``order='F'`` gives a zero-copy view over a buffer holding
   column-major data.

   The destination format is restricted to a single element native format in
   :mod:`struct` syntax. One of the formats must be a byte format
   ('B', 'b' or 'c'). The byte length of the result must be the same
   as the original length.
   Note that all byte lengths may depend on the operating system.

   Cast 1D/long to 1D/unsigned bytes::

      >>> import array
      >>> a = array.array('l', [1,2,3])
      >>> x = memoryview(a)
      >>> x.format
      'l'
      >>> x.itemsize
      8
      >>> len(x)
      3
      >>> x.nbytes
      24
      >>> y = x.cast('B')
      >>> y.format
      'B'
      >>> y.itemsize
      1
      >>> len(y)
      24
      >>> y.nbytes
      24

   Cast 1D/unsigned bytes to 1D/char::

      >>> b = bytearray(b'zyz')
      >>> x = memoryview(b)
      >>> x[0] = b'a'
      Traceback (most recent call last):
        ...
      TypeError: memoryview: invalid type for format 'B'
      >>> y = x.cast('c')
      >>> y[0] = b'a'
      >>> b
      bytearray(b'ayz')

   Cast 1D/bytes to 3D/ints to 1D/signed char::

      >>> import struct
      >>> buf = struct.pack("i"*12, *list(range(12)))
      >>> x = memoryview(buf)
      >>> y = x.cast('i', shape=[2,2,3])
      >>> y.tolist()
      [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
      >>> y.format
      'i'
      >>> y.itemsize
      4
      >>> len(y)
      2
      >>> y.nbytes
      48
      >>> z = y.cast('b')
      >>> z.format
      'b'
      >>> z.itemsize
      1
      >>> len(z)
      48
      >>> z.nbytes
      48

   Cast 1D/unsigned long to 2D/unsigned long::

      >>> buf = struct.pack("L"*6, *list(range(6)))
      >>> x = memoryview(buf)
      >>> y = x.cast('L', shape=[2,3])
      >>> len(y)
      2
      >>> y.nbytes
      48
      >>> y.tolist()
      [[0, 1, 2], [3, 4, 5]]

   .. versionadded:: 3.3

   .. versionchanged:: 3.5
      The source format is no longer restricted when casting to a byte view.

   .. versionchanged:: 3.16
      Casting a multi-dimensional F-contiguous view to a one-dimensional
      view is now supported.

.. method:: count(value, /)

   Count the number of occurrences of *value*.

   .. versionadded:: 3.14

.. method:: index(value, start=0, stop=sys.maxsize, /)

   Return the index of the first occurrence of *value* (at or after
   index *start* and before index *stop*).

   Raises a :exc:`ValueError` if *value* cannot be found.

   .. versionadded:: 3.14

There are also several readonly attributes available:

.. attribute:: obj

   The underlying object of the memoryview::

      >>> b  = bytearray(b'xyz')
      >>> m = memoryview(b)
      >>> m.obj is b
      True

   .. versionadded:: 3.3

.. attribute:: nbytes

   ``nbytes == product(shape) * itemsize == len(m.tobytes())``. This is
   the amount of space in bytes that the array would use in a contiguous
   representation. It is not necessarily equal to ``len(m)``::

      >>> import array
      >>> a = array.array('i', [1,2,3,4,5])
      >>> m = memoryview(a)
      >>> len(m)
      5
      >>> m.nbytes
      20
      >>> y = m[::2]
      >>> len(y)
      3
      >>> y.nbytes
      12
      >>> len(y.tobytes())
      12

   Multi-dimensional arrays::

      >>> import struct
      >>> buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
      >>> x = memoryview(buf)
      >>> y = x.cast('d', shape=[3,4])
      >>> y.tolist()
      [[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]
      >>> len(y)
      3
      >>> y.nbytes
      96

   Interpret a flat buffer as a Fortran-contiguous (column-major) array::

      >>> buf = bytes(range(6))
      >>> y = memoryview(buf).cast('B', shape=[3, 2], order='F')
      >>> y.f_contiguous
      True
      >>> y.tolist()
      [[0, 3], [1, 4], [2, 5]]

   .. versionadded:: 3.3

   .. versionchanged:: 3.16
      Added the *order* parameter.

.. attribute:: readonly

   A bool indicating whether the memory is read only.

.. attribute:: format

   A string containing the format (in :mod:`struct` module style) for each
   element in the view. A memoryview can be created from exporters with
   arbitrary format strings, but some methods (e.g. :meth:`tolist`) are
   restricted to native single element formats.

   .. versionchanged:: 3.3
      format ``'B'`` is now handled according to the struct module syntax.
      This means that ``memoryview(b'abc')[0] == b'abc'[0] == 97``.

.. attribute:: itemsize

   The size in bytes of each element of the memoryview::

      >>> import array, struct
      >>> m = memoryview(array.array('H', [32000, 32001, 32002]))
      >>> m.itemsize
      2
      >>> m[0]
      32000
      >>> struct.calcsize('H') == m.itemsize
      True

.. attribute:: ndim

   An integer indicating how many dimensions of a multi-dimensional array the
   memory represents.

.. attribute:: shape

   A tuple of integers the length of :attr:`ndim` giving the shape of the
   memory as an N-dimensional array.

   .. versionchanged:: 3.3
      An empty tuple instead of ``None`` when ndim = 0.

.. attribute:: strides

   A tuple of integers the length of :attr:`ndim` giving the size in bytes to
   access each element for each dimension of the array.

   .. versionchanged:: 3.3
      An empty tuple instead of ``None`` when ndim = 0.

.. attribute:: suboffsets

   Used internally for PIL-style arrays. The value is informational only.

.. attribute:: c_contiguous

   A bool indicating whether the memory is C-:term:`contiguous`.

   .. versionadded:: 3.3

.. attribute:: f_contiguous

   A bool indicating whether the memory is Fortran :term:`contiguous`.

   .. versionadded:: 3.3

.. attribute:: contiguous

   A bool indicating whether the memory is :term:`contiguous`.

   .. versionadded:: 3.3

```

For information on the thread safety of `class` objects in
the `term`, see `ref`.

## Set Types --- :class:`set`, :class:`frozenset`

A :dfn:`set` object is an unordered collection of distinct `term` objects.
Common uses include membership testing, removing duplicates from a sequence, and
computing mathematical operations such as intersection, union, difference, and
symmetric difference.
(For other containers see the built-in `class`, `class`,
and `class` classes, and the `mod` module.)
See `ref` for the costs of the various set operations.

Like other collections, sets support `x in set`, `len(set)`, and ``for x in
set``.  Being an unordered collection, sets do not record element position or
order of insertion.  Accordingly, sets do not support indexing, slicing, or
other sequence-like behavior.

There are currently two built-in set types, `class` and `class`.
The `class` type is mutable --- the contents can be changed using methods
like `set.add()` and `set.remove()`.
Since it is mutable, it has no hash value and cannot be used as
either a dictionary key or as an element of another set.
The `class` type is immutable and `term` ---
its contents cannot be altered after it is created;
it can therefore be used as a dictionary key or as an element of another set.

Non-empty sets (not frozensets) can be created by placing a comma-separated list
of elements within braces, for example: `{'jack', 'sjoerd'}`, in addition to the
`class` constructor.

The constructors for both classes work the same:

### Class: `set(iterable=(), /)`

           frozenset(iterable=(), /)

   Return a new set or frozenset object whose elements are taken from
   *iterable*.  The elements of a set must be `term`.  To
   represent sets of sets, the inner sets must be `class`
   objects.  If *iterable* is not specified, a new empty set is
   returned.

Sets can be created by several means:

* Use a comma-separated list of elements within braces: `{'jack', 'sjoerd'}`
* Use a set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`
* Use the type constructor: `set()`, `set('foobar')`, `set(['a', 'b', 'foo'])`

Instances of `class` and `class` provide the following
operations:

### Describe: `len(s)`

   Return the number of elements in set *s* (cardinality of *s*).

### Describe: `x in s`

   Test *x* for membership in *s*.

### Describe: `x not in s`

   Test *x* for non-membership in *s*.

### Method: `frozenset.isdisjoint(other, /)`

            set.isdisjoint(other, /)

   Return `True` if the set has no elements in common with *other*.  Sets are
   disjoint if and only if their intersection is the empty set.

### Method: `frozenset.issubset(other, /)`

            set.issubset(other, /)

### Describe: `set <= other`

   Test whether every element in the set is in *other*.

### Describe: `set < other`

   Test whether the set is a proper subset of *other*, that is,
   `set <= other and set != other`.

### Method: `frozenset.issuperset(other, /)`

            set.issuperset(other, /)

### Describe: `set >= other`

   Test whether every element in *other* is in the set.

### Describe: `set > other`

   Test whether the set is a proper superset of *other*, that is, ``set >=
   other and set != other``.

### Method: `frozenset.union(*others)`

            set.union(*others)

### Describe: `set | other | ...`

   Return a new set with elements from the set and all others.

### Method: `frozenset.intersection(*others)`

            set.intersection(*others)

### Describe: `set & other & ...`

   Return a new set with elements common to the set and all others.

### Method: `frozenset.difference(*others)`

            set.difference(*others)

### Describe: `set - other - ...`

   Return a new set with elements in the set that are not in the others.

### Method: `frozenset.symmetric_difference(other, /)`

            set.symmetric_difference(other, /)

### Describe: `set ^ other`

   Return a new set with elements in either the set or *other* but not both.

### Method: `frozenset.copy()`

            set.copy()

   Return a shallow copy of the set.

Note, the non-operator versions of `frozenset.union()`,
`frozenset.intersection()`, `frozenset.difference()`, `frozenset.symmetric_difference()`, `frozenset.issubset()`, and
`frozenset.issuperset()` methods will accept any iterable as an argument.  In
contrast, their operator based counterparts require their arguments to be
sets.  This precludes error-prone constructions like `set('abc') & 'cbs'`
in favor of the more readable `set('abc').intersection('cbs')`.

Both `class` and `class` support set to set comparisons. Two
sets are equal if and only if every element of each set is contained in the
other (each is a subset of the other). A set is less than another set if and
only if the first set is a proper subset of the second set (is a subset, but
is not equal). A set is greater than another set if and only if the first set
is a proper superset of the second set (is a superset, but is not equal).

Instances of `class` are compared to instances of `class`
based on their members.  For example, `set('abc') == frozenset('abc')`
returns `True` and so does `set('abc') in set([frozenset('abc')])`.

The subset and equality comparisons do not generalize to a total ordering
function.  For example, any two nonempty disjoint sets are not equal and are not
subsets of each other, so *all* of the following return `False`: `a<b`,
`a==b`, or `a>b`.

Since sets only define partial ordering (subset relationships), the output of
the `list.sort()` method is undefined for lists of sets.

Set elements, like dictionary keys, must be `term`.

Binary operations that mix `class` instances with `class`
return the type of the first operand.  For example: ``frozenset('ab') |
set('bc')`` returns an instance of `class`.

The following table lists operations available for `class` that do not
apply to immutable instances of `class`:

### Method: `set.update(*others)`

### Describe: `set |= other | ...`

   Update the set, adding elements from all others.

### Method: `set.intersection_update(*others)`

### Describe: `set &= other & ...`

   Update the set, keeping only elements found in it and all others.

### Method: `set.difference_update(*others)`

### Describe: `set -= other | ...`

   Update the set, removing elements found in others.

### Method: `set.symmetric_difference_update(other, /)`

### Describe: `set ^= other`

   Update the set, keeping only elements found in either set, but not in both.

### Method: `set.add(elem, /)`

   Add element *elem* to the set.

### Method: `set.remove(elem, /)`

   Remove element *elem* from the set.  Raises `exc` if *elem* is
   not contained in the set.

### Method: `set.discard(elem, /)`

   Remove element *elem* from the set if it is present.

### Method: `set.pop()`

   Remove and return an arbitrary element from the set.  Raises
   `exc` if the set is empty.

### Method: `set.clear()`

   Remove all elements from the set.

Note, the non-operator versions of the `set.update()`,
`set.intersection_update()`, `set.difference_update()`, and
`set.symmetric_difference_update()` methods will accept any iterable as an
argument.

Note, the *elem* argument to the `object.__contains__()`,
`set.remove()`, and `set.discard()` methods may be a set.  In this case,
an equivalent frozenset is searched for.

Sets and frozensets are `ref` over the type of their elements.

.. seealso

```python

For detailed information on thread-safety guarantees for :class:`set`
objects, see :ref:`thread-safety-set`.

```

## Mapping types --- :class:`!dict`, :class:`!frozendict`

.. index

```python
pair: object; mapping
pair: object; dictionary
triple: operations on; mapping; types
triple: operations on; dictionary; type
pair: statement; del
pair: built-in function; len

```

A `term` object maps `term` values to arbitrary objects.
There are currently two standard mapping types, the :dfn:`dictionary` and
`class`.
(For other containers see the built-in
`class`, `class`, and `class` classes, and the
`mod` module.)
See `ref` for the costs of the various dictionary
operations.

A dictionary's keys are *almost* arbitrary values.  Values that are not
`term`, that is, values containing lists, dictionaries or other
mutable types (that are compared by value rather than by object identity) may
not be used as keys.
Values that compare equal (such as `1`, `1.0`, and `True`)
can be used interchangeably to index the same dictionary entry.

### Class: `dict(**kwargs)`

           dict(mapping, /, **kwargs)
           dict(iterable, /, **kwargs)

   Return a new dictionary initialized from an optional positional argument
   and a possibly empty set of keyword arguments.

   Dictionaries can be created by several means:

   * Use a comma-separated list of `key: value` pairs within braces:
     `{'jack': 4098, 'sjoerd': 4127}` or `{4098: 'jack', 4127: 'sjoerd'}`
   * Use a dict comprehension: `{x: x ** 2 for x in range(10)}`
   * Use the type constructor: `dict()`,
     `dict([('foo', 100), ('bar', 200)])`, `dict(foo=100, bar=200)`

   If no positional argument is given, an empty dictionary is created.
   If a positional argument is given and it defines a `keys()` method, a
   dictionary is created by calling `object.__getitem__()` on the argument with
   each returned key from the method.  Otherwise, the positional argument must be an
   `term` object.  Each item in the iterable must itself be an iterable
   with exactly two elements.  The first element of each item becomes a key in the
   new dictionary, and the second element the corresponding value.  If a key occurs
   more than once, the last value for that key becomes the corresponding value in
   the new dictionary.

   If keyword arguments are given, the keyword arguments and their values are
   added to the dictionary created from the positional argument.  If a key
   being added is already present, the value from the keyword argument
   replaces the value from the positional argument.

   Dictionaries compare equal if and only if they have the same ``(key,
   value)`` pairs (regardless of ordering). Order comparisons ('<', '<=', '>=', '>') raise
   `exc`.  To illustrate dictionary creation and equality,
   the following examples all return a dictionary equal to
``{"one": 1, "two": 2, "three": 3}``

```python

   >>> a = dict(one=1, two=2, three=3)
   >>> b = {'one': 1, 'two': 2, 'three': 3}
   >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
   >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
   >>> e = dict({'three': 3, 'one': 1, 'two': 2})
   >>> f = dict({'one': 1, 'three': 3}, two=2)
   >>> a == b == c == d == e == f
   True

Providing keyword arguments as in the first example only works for keys that
are valid Python identifiers.  Otherwise, any valid keys can be used.

Dictionaries preserve insertion order.  Note that updating a key does not
affect the order.  Keys added after deletion are inserted at the end. ::

   >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
   >>> d
   {'one': 1, 'two': 2, 'three': 3, 'four': 4}
   >>> list(d)
   ['one', 'two', 'three', 'four']
   >>> list(d.values())
   [1, 2, 3, 4]
   >>> d["one"] = 42
   >>> d
   {'one': 42, 'two': 2, 'three': 3, 'four': 4}
   >>> del d["two"]
   >>> d["two"] = None
   >>> d
   {'one': 42, 'three': 3, 'four': 4, 'two': None}

.. versionchanged:: 3.7
   Dictionary order is guaranteed to be insertion order.  This behavior was
   an implementation detail of CPython from 3.6.

Dictionaries are :ref:`generic <generics>` over two types, signifying
(respectively) the types of the dictionary's keys and values.

These are the operations that dictionaries support (and therefore, custom
mapping types should support too):

.. describe:: list(d)

   Return a list of all the keys used in the dictionary *d*.

.. describe:: len(d)

   Return the number of items in the dictionary *d*.

.. describe:: d[key]

   Return the item of *d* with key *key*.  Raises a :exc:`KeyError` if *key* is
   not in the map.

   .. index:: __missing__()

   If a subclass of dict defines a method :meth:`~object.__missing__` and *key*
   is not present, the ``d[key]`` operation calls that method with the key *key*
   as argument.  The ``d[key]`` operation then returns or raises whatever is
   returned or raised by the ``__missing__(key)`` call.
   No other operations or methods invoke :meth:`~object.__missing__`. If
   :meth:`~object.__missing__` is not defined, :exc:`KeyError` is raised.
   :meth:`~object.__missing__` must be a method; it cannot be an instance variable::

       >>> class Counter(dict):
       ...     def __missing__(self, key):
       ...         return 0
       ...
       >>> c = Counter()
       >>> c['red']
       0
       >>> c['red'] += 1
       >>> c['red']
       1

   The example above shows part of the implementation of
   :class:`collections.Counter`.
   A different :meth:`!__missing__` method is used
   by :class:`collections.defaultdict`.

.. describe:: d[key] = value

   Set ``d[key]`` to *value*.

.. describe:: del d[key]

   Remove ``d[key]`` from *d*.  Raises a :exc:`KeyError` if *key* is not in the
   map.

.. describe:: key in d

   Return ``True`` if *d* has a key *key*, else ``False``.

.. describe:: key not in d

   Equivalent to ``not key in d``.

.. describe:: iter(d)

   Return an iterator over the keys of the dictionary.  This is a shortcut
   for ``iter(d.keys())``.

.. method:: clear()

   Remove all items from the dictionary.

.. method:: copy()

   Return a shallow copy of the dictionary.

.. classmethod:: fromkeys(iterable, value=None, /)

   Create a new dictionary with keys from *iterable* and values set to *value*.

   :meth:`fromkeys` is a class method that returns a new dictionary. *value*
   defaults to ``None``.  All of the values refer to just a single instance,
   so it generally doesn't make sense for *value* to be a mutable object
   such as an empty list.  To get distinct values, use a :ref:`dict
   comprehension <dict>` instead.

.. method:: get(key, default=None, /)

   Return the value for *key* if *key* is in the dictionary, else *default*.
   If *default* is not given, it defaults to ``None``, so that this method
   never raises a :exc:`KeyError`.

.. method:: items()

   Return a new view of the dictionary's items (``(key, value)`` pairs).
   See the :ref:`documentation of view objects <dict-views>`.

.. method:: keys()

   Return a new view of the dictionary's keys.  See the :ref:`documentation
   of view objects <dict-views>`.

.. method:: pop(key, /)
            pop(key, default, /)

   If *key* is in the dictionary, remove it and return its value, else return
   *default*.  If *default* is not given and *key* is not in the dictionary,
   a :exc:`KeyError` is raised.

.. method:: popitem()

   Remove and return a ``(key, value)`` pair from the dictionary.
   Pairs are returned in :abbr:`LIFO (last-in, first-out)` order.

   :meth:`popitem` is useful to destructively iterate over a dictionary, as
   often used in set algorithms.  If the dictionary is empty, calling
   :meth:`popitem` raises a :exc:`KeyError`.

   .. versionchanged:: 3.7
      LIFO order is now guaranteed. In prior versions, :meth:`popitem` would
      return an arbitrary key/value pair.

.. describe:: reversed(d)

   Return a reverse iterator over the keys of the dictionary. This is a
   shortcut for ``reversed(d.keys())``.

   .. versionadded:: 3.8

.. method:: setdefault(key, default=None, /)

   If *key* is in the dictionary, return its value.  If not, insert *key*
   with a value of *default* and return *default*.  *default* defaults to
   ``None``.

.. method:: update(**kwargs)
            update(mapping, /, **kwargs)
            update(iterable, /, **kwargs)

   Update the dictionary with the key/value pairs from *mapping* or *iterable* and *kwargs*, overwriting
   existing keys.  Return ``None``.

   :meth:`update` accepts either another object with a ``keys()`` method (in
   which case :meth:`~object.__getitem__` is called with every key returned from
   the method) or an iterable of key/value pairs (as tuples or other iterables
   of length two). If keyword arguments are specified, the dictionary is then
   updated with those key/value pairs: ``d.update(red=1, blue=2)``.

.. method:: values()

   Return a new view of the dictionary's values.  See the
   :ref:`documentation of view objects <dict-views>`.

   An equality comparison between two distinct ``dict.values()`` views
   will always return ``False``, even for views of the same dictionary::

      >>> d = {'a': 1}
      >>> d.values() == d.values()
      False

.. describe:: d | other

   Create a new dictionary with the merged keys and values of *d* and
   *other*, which must both be dictionaries. The values of *other* take
   priority when *d* and *other* share keys.

   .. versionadded:: 3.9

.. describe:: d |= other

   Update the dictionary *d* with keys and values from *other*, which may be
   either a :term:`mapping` or an :term:`iterable` of key/value pairs. The
   values of *other* take priority when *d* and *other* share keys.

   .. versionadded:: 3.9

Dictionaries and dictionary views are reversible. ::

   >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
   >>> d
   {'one': 1, 'two': 2, 'three': 3, 'four': 4}
   >>> list(reversed(d))
   ['four', 'three', 'two', 'one']
   >>> list(reversed(d.values()))
   [4, 3, 2, 1]
   >>> list(reversed(d.items()))
   [('four', 4), ('three', 3), ('two', 2), ('one', 1)]

.. versionchanged:: 3.8
   Dictionaries are now reversible.

.. seealso::
   :class:`types.MappingProxyType` can be used to create a read-only view
   of a :class:`dict`.  :class:`frozendict` is an immutable version of
   :class:`dict`.

```

.. seealso

```python

For detailed information on thread-safety guarantees for :class:`dict`
objects, see :ref:`thread-safety-dict`.

```

### Dictionary view objects

The objects returned by `dict.keys()`, `dict.values()` and
`dict.items()` are *view objects*.  They provide a dynamic view on the
dictionary's entries, which means that when the dictionary changes, the view
reflects these changes.

Dictionary views can be iterated over to yield their respective data, and
support membership tests:

### Describe: `len(dictview)`

   Return the number of entries in the dictionary.

### Describe: `iter(dictview)`

   Return an iterator over the keys, values or items (represented as tuples of
   `(key, value)`) in the dictionary.

   Keys and values are iterated over in insertion order.
   This allows the creation of `(value, key)` pairs
   using `zip()`: `pairs = zip(d.values(), d.keys())`.  Another way to
   create the same list is `pairs = [(v, k) for (k, v) in d.items()]`.

   Iterating views while adding or deleting entries in the dictionary may raise
   a `exc` or fail to iterate over all entries.

   .. versionchanged:: 3.7
      Dictionary order is guaranteed to be insertion order.

### Describe: `x in dictview`

   Return `True` if *x* is in the underlying dictionary's keys, values or
   items (in the latter case, *x* should be a `(key, value)` tuple).

### Describe: `reversed(dictview)`

   Return a reverse iterator over the keys, values or items of the dictionary.
   The view will be iterated in reverse order of the insertion.

   .. versionchanged:: 3.8
      Dictionary views are now reversible.

### Describe: `dictview.mapping`

   Return a `class` that wraps the original
   dictionary to which the view refers.

   .. versionadded:: 3.10

Keys views are set-like since their entries are unique and `term`.
Items views also have set-like operations since the (key, value) pairs
are unique and the keys are hashable.
If all values in an items view are hashable as well,
then the items view can interoperate with other sets.
(Values views are not treated as set-like
since the entries are generally not unique.)  For set-like views, all of the
operations defined for the abstract base class `class` are
available (for example, `==`, `<`, or `^`).  While using set operators,
set-like views accept any iterable as the other operand,
unlike sets which only accept sets as the input.

An example of dictionary view usage

```python

>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> values = dishes.values()

>>> # iteration
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504

>>> # keys and values are iterated over in the same order (insertion order)
>>> list(keys)
['eggs', 'sausage', 'bacon', 'spam']
>>> list(values)
[2, 1, 1, 500]

>>> # view objects are dynamic and reflect dict changes
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']

>>> # set operations
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
>>> keys ^ {'sausage', 'juice'} == {'juice', 'sausage', 'bacon', 'spam'}
True
>>> keys | ['juice', 'juice', 'juice'] == {'bacon', 'spam', 'juice'}
True

>>> # get back a read-only proxy for the original dictionary
>>> values.mapping
mappingproxy({'bacon': 1, 'spam': 500})
>>> values.mapping['spam']
500

```

### Frozen dictionaries

### Class: `frozendict(**kwargs)`

           frozendict(mapping, /, **kwargs)
           frozendict(iterable, /, **kwargs)

   Return a new frozen dictionary initialized from an optional positional
   argument and a possibly empty set of keyword arguments.

   A `class` has a similar API to the `class` API, with the
   following differences:

   * `class` has more methods than `class`:

      * `!__delitem__()`
      * `!__setitem__()`
      * `dict.clear()`
      * `dict.pop()`
      * `dict.popitem()`
      * `dict.setdefault()`
      * `dict.update()`

   * A `class` can be hashed with `hash(frozendict)` if all keys and
     values can be hashed.

   * `frozendict |= other` does not modify the `class` in-place but
     creates a new frozen dictionary.

   `class` is not a `class` subclass but inherits directly
   from `object`.

   Like dictionaries, frozendicts are `ref` over two types,
   signifying (respectively) the types of the frozendict's keys and values.

   .. classmethod:: fromkeys(iterable, value=None, /)

      Similar to `dict.fromkeys()`, but call again the type constructor
      with an initialized `class` if the type is a
      `class` subclass.

   .. versionadded:: 3.15

## Context Manager Types

.. index

```python
single: context manager
single: context management protocol
single: protocol; context management

```

Python's :keyword:`with` statement supports the concept of a runtime context
defined by a context manager.  This is implemented using a pair of methods
that allow user-defined classes to define a runtime context that is entered
before the statement body is executed and exited when the statement ends:

### Method: `contextmanager.__enter__()`

   Enter the runtime context and return either this object or another object
   related to the runtime context. The value returned by this method is bound to
   the identifier in the :keyword:`!as` clause of :keyword:`with` statements using
   this context manager.

   An example of a context manager that returns itself is a `term`.
   File objects return themselves from __enter__() to allow `open()` to be
   used as the context expression in a :keyword:`with` statement.

   An example of a context manager that returns a related object is the one
   returned by `decimal.localcontext()`. These managers set the active
   decimal context to a copy of the original decimal context and then return the
   copy. This allows changes to be made to the current decimal context in the body
   of the :keyword:`with` statement without affecting code outside the
   :keyword:`!with` statement.

### Method: `contextmanager.__exit__(exc_type, exc_val, exc_tb)`

   Exit the runtime context and return a Boolean flag indicating if any exception
   that occurred should be suppressed. If an exception occurred while executing the
   body of the :keyword:`with` statement, the arguments contain the exception type,
   value and traceback information. Otherwise, all three arguments are `None`.

   Returning a true value from this method will cause the :keyword:`with` statement
   to suppress the exception and continue execution with the statement immediately
   following the :keyword:`!with` statement. Otherwise the exception continues
   propagating after this method has finished executing.

   If this method raises an exception while handling an earlier exception from the
   :keyword:`with` block, the new exception is raised, and the original exception
   is stored in its :attr:`~BaseException.__context__` attribute.

   The exception passed in should never be reraised explicitly - instead, this
   method should return a false value to indicate that the method completed
   successfully and does not want to suppress the raised exception. This allows
   context management code to easily detect whether or not an `object.__exit__()`
   method has actually failed.

Python defines several context managers to support easy thread synchronisation,
prompt closure of files or other objects, and simpler manipulation of the active
decimal arithmetic context. The specific types are not treated specially beyond
their implementation of the context management protocol. See the
`mod` module for some examples.

Python's `term`\s and the `class` decorator
provide a convenient way to implement these protocols.  If a generator function is
decorated with the `class` decorator, it will return a
context manager implementing the necessary `contextmanager.__enter__()` and
`contextmanager.__exit__()` methods, rather than the iterator produced by an
undecorated generator function.

Note that there is no specific slot for any of these methods in the type
structure for Python objects in the Python/C API. Extension types wanting to
define these methods must provide them as a normal Python accessible method.
Compared to the overhead of setting up the runtime context, the overhead of a
single class dictionary lookup is negligible.

## Type Annotation Types --- :ref:`Generic Alias <types-genericalias>`, :ref:`Union <types-union>`

.. index

```python
single: annotation; type annotation; type hint

```

The core built-in types for `term` are
`ref` and `ref`.

### Generic Alias Type

.. index

```python
pair: object; GenericAlias
pair: Generic; Alias

```

`GenericAlias` objects are generally created by
`ref` a class. They are most often used with
`ref`, such as `class` or
`class`. For example, `list[int]` is a `GenericAlias` object created
by subscripting the `list` class with the argument `class`.
`GenericAlias` objects are intended primarily for use with
`term`.

.. note

```python

It is generally only possible to subscript a class if the class implements
the special method :meth:`~object.__class_getitem__`.

```

A `GenericAlias` object acts as a proxy for a `term`,
implementing *parameterized generics*.

For a container class, the
argument(s) supplied to a `ref` of the class may
indicate the type(s) of the elements an object contains. For example,
`set[bytes]` can be used in type annotations to signify a `class` in
which all the elements are of type `class`.

For a class which defines `object.__class_getitem__()` but is not a
container, the argument(s) supplied to a subscription of the class will often
indicate the return type(s) of one or more methods defined on an object. For
example, `mod` can be used on both the `class` data
type and the `class` data type:

* If `x = re.search('foo', 'foo')`, `x` will be a
  `ref` object where the return values of
  `x.group(0)` and `x[0]` will both be of type `class`. We can
  represent this kind of object in type annotations with the `GenericAlias`
  `re.Match[str]`.

* If `y = re.search(b'bar', b'bar')`, (note the `b` for `class`),
  `y` will also be an instance of `re.Match`, but the return
  values of `y.group(0)` and `y[0]` will both be of type
  `class`. In type annotations, we would represent this
  variety of `ref` objects with `re.Match[bytes]`.

`GenericAlias` objects are instances of the class
`class`, which can also be used to create `GenericAlias`
objects directly. Specializations of user-defined `ref`
may not be instances of `class`, but they provide similar functionality.

### Describe: `T[X, Y, ...]`

   Creates a `GenericAlias` representing a type `T` parameterized by types
   *X*, *Y*, and more depending on the `T` used.
   For example, a function expecting a `class` containing
:class:`float` elements

```python

   def average(values: list[float]) -> float:
       return sum(values) / len(values)

Another example for :term:`mapping` objects, using a :class:`dict`, which
is a generic type expecting two type parameters representing the key type
and the value type.  In this example, the function expects a ``dict`` with
keys of type :class:`str` and values of type :class:`int`::

   def send_post_request(url: str, body: dict[str, int]) -> None:
       ...

```

The builtin functions `isinstance()` and `issubclass()` do not accept
``GenericAlias`` types for their second argument

```python

>>> isinstance([1, 2], list[str])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: isinstance() argument 2 cannot be a parameterized generic

```

The Python runtime does not enforce `term`.
This extends to generic types and their type parameters. When creating
a container object from a `GenericAlias`, the elements in the container are not checked
against their type. For example, the following code is discouraged, but will
run without errors

```python

>>> t = list[str]
>>> t([1, 2, 3])
[1, 2, 3]

```

Furthermore, parameterized generics erase type parameters during object
creation

```python

>>> t = list[str]
>>> type(t)
<class 'types.GenericAlias'>

>>> l = t()
>>> type(l)
<class 'list'>

```

Instances of ``GenericAlias`` are not classes at runtime, even though they behave like classes (they can be instantiated and subclassed)

```python

>>> import inspect
>>> inspect.isclass(list[int])
False

```

This is true for `ref` also.

Calling :func:`repr` or :func:`str` on a generic shows the parameterized type

```python

>>> repr(list[int])
'list[int]'

>>> str(list[int])
'list[int]'

```

The `object.__getitem__()` method of generic containers will raise an
exception to disallow mistakes like ``dict[str][str]``

```python

>>> dict[str][str]
Traceback (most recent call last):
  ...
TypeError: dict[str] is not a generic class

```

However, such expressions are valid when `ref` are
used.  The index must have as many elements as there are type variable items
in the ``GenericAlias`` object's :attr:`~genericalias.__args__`.

```python

>>> from typing import TypeVar
>>> Y = TypeVar('Y')
>>> dict[str, Y][int]
dict[str, int]

```

### Standard Generic Classes

The following standard library classes support parameterized generics. This
list is non-exhaustive.

* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `ref`
* `ref`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`
* `class`

### Special Attributes of ``GenericAlias`` objects

All parameterized generics implement special read-only attributes.

This attribute points at the non-parameterized generic class

```python

   >>> list[int].__origin__
   <class 'list'>

```

   This attribute is a `class` (possibly of length 1) of generic
   types passed to the original `object.__class_getitem__()` of the
generic class

```python

   >>> dict[str, list[int]].__args__
   (<class 'str'>, list[int])

```

   This attribute is a lazily computed tuple (possibly empty) of unique type
variables found in ``__args__``

```python

   >>> from typing import TypeVar

   >>> T = TypeVar('T')
   >>> list[T].__parameters__
   (~T,)

.. note::
   A ``GenericAlias`` object with :class:`typing.ParamSpec` parameters may not
   have correct ``__parameters__`` after substitution because
   :class:`typing.ParamSpec` is intended primarily for static type checking.

```

   A boolean that is true if the alias has been unpacked using the
   `*` operator (see `data`).

   .. versionadded:: 3.11

.. seealso

```python

:pep:`484` - Type Hints
   Introducing Python's framework for type annotations.

:pep:`585` - Type Hinting Generics In Standard Collections
   Introducing the ability to natively parameterize standard-library
   classes, provided they implement the special class method
   :meth:`~object.__class_getitem__`.

:ref:`Generics`, :ref:`user-defined generics <user-defined-generics>` and :class:`typing.Generic`
   Documentation on how to implement generic classes that can be
   parameterized at runtime and understood by static type-checkers.

```

### Union Type

.. index

```python
pair: object; Union
pair: union; type

```

A union object holds the value of the `|` (bitwise or) operation on
multiple `ref`.  These types are intended
primarily for `term`. The union type expression
enables cleaner type hinting syntax compared to subscripting `class`.

### Describe: `X | Y | ...`

   Defines a union object which holds types *X*, *Y*, and so forth. `X | Y`
   means either X or Y.  It is equivalent to `typing.Union[X, Y]`.
   For example, the following function expects an argument of type
:class:`int` or :class:`float`

```python

   def square(number: int | float) -> int | float:
       return number ** 2

.. note::

   The ``|`` operator cannot be used at runtime to define unions where one or
   more members is a forward reference. For example, ``int | "Foo"``, where
   ``"Foo"`` is a reference to a class not yet defined, will fail at
   runtime. For unions which include forward references, present the
   whole expression as a string, e.g. ``"int | Foo"``.

```

### Describe: `union_object == other`

   Union objects can be tested for equality with other union objects.  Details:

* Unions of unions are flattened

```python

    (int | str) | float == int | str | float

* Redundant types are removed::

    int | str | int == int | str

* When comparing unions, the order is ignored::

   int | str == str | int

* It creates instances of :class:`typing.Union`::

   int | str == typing.Union[int, str]
   type(int | str) is typing.Union

* Optional types can be spelled as a union with ``None``::

   str | None == typing.Optional[str]

```

### Describe: `isinstance(obj, union_object)`

### Describe: `issubclass(obj, union_object)`

   Calls to `isinstance()` and `issubclass()` are also supported with a
union object

```python

   >>> isinstance("", int | str)
   True

However, :ref:`parameterized generics <types-genericalias>` in
union objects cannot be checked::

   >>> isinstance(1, int | list[int])  # short-circuit evaluation
   True
   >>> isinstance([1], int | list[int])
   Traceback (most recent call last):
     ...
   TypeError: isinstance() argument 2 cannot be a parameterized generic

```

The user-exposed type for the union object can be accessed from
:class:`typing.Union` and used for :func:`isinstance` checks

```python

>>> import typing
>>> isinstance(int | str, typing.Union)
True
>>> typing.Union()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create 'typing.Union' instances

```

.. note

```python
The :meth:`!__or__` method for type objects was added to support the syntax
``X | Y``.  If a metaclass implements :meth:`!__or__`, it may override
the default behavior of creating a union:

.. doctest::

   >>> class M(type):
   ...     def __or__(self, other):
   ...         return "Hello"
   ...
   >>> class C(metaclass=M):
   ...     pass
   ...
   >>> C | int
   'Hello'
   >>> int | C
   int | C

```

.. seealso

```python

:pep:`604` -- PEP proposing the ``X | Y`` syntax and the Union type.

```

   Union objects are now instances of `class`. Previously, they were instances
   of `class`, which remains an alias for `class`.

## Other Built-in Types

The interpreter supports several other kinds of objects. Most of these support
only one or two operations.

### Modules

The only special operation on a module is attribute access: `m.name`, where
*m* is a module and *name* accesses a name defined in *m*'s symbol table.
Module attributes can be assigned to.  (Note that the :keyword:`import`
statement is not, strictly speaking, an operation on a module object; ``import
foo`` does not require a module object named *foo* to exist, rather it requires
an (external) *definition* for a module named *foo* somewhere.)

A special attribute of every module is :attr:`~object.__dict__`. This is the
dictionary containing the module's symbol table. Modifying this dictionary will
actually change the module's symbol table, but direct assignment to the
:attr:`~object.__dict__` attribute is not possible (you can write
`m.__dict__['a'] = 1`, which defines `m.a` to be `1`, but you can't write
`m.__dict__ = {}`).  Modifying :attr:`~object.__dict__` directly is
not recommended.

Modules built into the interpreter are written like this: ``<module 'sys'
(built-in)>`.  If loaded from a file, they are written as `<module 'os' from
'/usr/local/lib/pythonX.Y/os.pyc'>``.

### Classes and Class Instances

See `ref` and `ref` for these.

### Functions

Function objects are created by function definitions.  The only operation on a
function object is to call it: `func(argument-list)`.

There are really two flavors of function objects: built-in functions and
user-defined functions.  Both support the same operation (to call the function),
but the implementation is different, hence the different object types.

See `ref` for more information.

### Methods

Methods are functions that are called using the attribute notation.
There are two flavors: `ref`
(such as `list.append()` on lists)
and `ref`.
Built-in methods are described with the types that support them.

If you access a method (a function defined in a class namespace) through an
instance, you get a special object: a :dfn:`bound method` (also called
`ref`) object. When called, it will add
the `self` argument
to the argument list.  Bound methods have two special read-only attributes:
:attr:`m.__self__ <method.__self__>` is the object on which the method
operates, and :attr:`m.__func__ <method.__func__>` is
the function implementing the method.  Calling `m(arg-1, arg-2, ..., arg-n)`
is completely equivalent to calling ``m.__func__(m.__self__, arg-1, arg-2, ...,
arg-n)``.

Like `ref`, bound method objects support
getting arbitrary
attributes.  However, since method attributes are actually stored on the
underlying function object (:attr:`method.__func__`), setting method attributes on
bound methods is disallowed.  Attempting to set an attribute on a method
results in an `exc` being raised.  In order to set a method
attribute, you need to explicitly set it on the underlying function object:

.. doctest

```python

>>> class C:
...     def method(self):
...         pass
...
>>> c = C()
>>> c.method.whoami = 'my name is method'  # can't set on the method
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'method' object has no attribute 'whoami'
>>> c.method.__func__.whoami = 'my name is method'
>>> c.method.whoami
'my name is method'

```

See `ref` for more information.

### Code Objects

.. index

```python
pair: built-in function; compile
single: __code__ (function object attribute)

```

Code objects are used by the implementation to represent "pseudo-compiled"
executable Python code such as a function body. They differ from function
objects because they don't contain a reference to their global execution
environment.  Code objects are returned by the built-in `compile()` function
and can be extracted from function objects through their
:attr:`~function.__code__` attribute. See also the `mod` module.

Accessing :attr:`~function.__code__` raises an `ref`
`object.__getattr__` with arguments `obj` and `"__code__"`.

.. index

```python
pair: built-in function; exec
pair: built-in function; eval

```

A code object can be executed or evaluated by passing it (instead of a source
string) to the `exec()` or `eval()`  built-in functions.

See `ref` for more information.

### Type Objects

.. index

```python
pair: built-in function; type
pair: module; types

```

Type objects represent the various object types.  An object's type is accessed
by the built-in function `type()`.  There are no special operations on
types.  The standard module `mod` defines names for all standard built-in
types.

Types are written like this: `<class 'int'>`.

### The Null Object

This object is returned by functions that don't explicitly return a value.  It
supports no special operations.  There is exactly one null object, named
`None` (a built-in name).  `type(None)()` produces the same singleton.

It is written as `None`.

### The Ellipsis Object

This object is commonly used to indicate that something is omitted.
It supports no special operations.  There is exactly one ellipsis object, named
`const` (a built-in name).  `type(Ellipsis)()` produces the
`const` singleton.

It is written as `Ellipsis` or `...`.

In typical use, `...` as the `Ellipsis` object appears in a few different
places, for instance:

- In type annotations, such as `ref`
  or `ref`.

- As the body of a function instead of a `ref`.

- In third-party libraries, such as `Numpy's slicing and striding
  <https://numpy.org/doc/stable/user/basics.indexing.html#slicing-and-striding>`_.

Python also uses three dots in ways that are not `Ellipsis` objects, for instance:

- Doctest's `const`, as a pattern for missing content.

- The default Python prompt of the `term` shell when partial input is incomplete.

Lastly, the Python documentation often uses three dots in conventional English
usage to mean omitted content, even in code examples that also use them as the
`Ellipsis`.

### The NotImplemented Object

This object is returned from comparisons and binary operations when they are
asked to operate on types they don't support. See `ref` for more
information.  There is exactly one `data` object.
:code:`type(NotImplemented)()` produces the singleton instance.

It is written as :code:`NotImplemented`.

### Internal Objects

See `ref` for this information.  It describes
`ref`,
`ref`, and slice objects.

## Special Attributes

The implementation adds a few special read-only attributes to several object
types, where they are relevant.  Some of these are not reported by the
`dir()` built-in function.

   The name of the class, function, method, descriptor, or
   generator instance.

   The `term` of the class, function, method, descriptor,
   or generator instance.

   .. versionadded:: 3.3

   The name of the module in which a class or function was defined.

   The documentation string of a class or function, or `None` if undefined.

   The `ref` of generic classes, functions,
   and `ref`. For classes and functions that
   are not generic, this will be an empty tuple.

   .. versionadded:: 3.12

## Integer string conversion length limitation

CPython has a global limit for converting between `class` and `class`
to mitigate denial of service attacks. This limit *only* applies to decimal or
other non-power-of-two number bases. Hexadecimal, octal, and binary conversions
are unlimited. The limit can be configured.

The `class` type in CPython is an arbitrary length number stored in binary
form (commonly known as a "bignum"). There exists no algorithm that can convert
a string to a binary integer or a binary integer to a string in linear time,
*unless* the base is a power of 2. Even the best known algorithms for base 10
have sub-quadratic complexity. Converting a large value such as ``int('1' *
500_000)`` can take over a second on a fast CPU.

Limiting conversion size offers a practical way to avoid :cve:`2020-10735`.

The limit is applied to the number of digit characters in the input or output
string when a non-linear conversion algorithm would be involved.  Underscores
and the sign are not counted towards the limit.

When an operation would exceed the limit, a `exc` is raised:

.. doctest

```python

>>> import sys
>>> sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
>>> _ = int('2' * 5432)
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5432 digits; use sys.set_int_max_str_digits() to increase the limit
>>> i = int('2' * 4300)
>>> len(str(i))
4300
>>> i_squared = i*i
>>> len(str(i_squared))
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
>>> len(hex(i_squared))
7144
>>> assert int(hex(i_squared), base=16) == i*i  # Hexadecimal is unlimited.

```

The default limit is 4300 digits as provided in
`data`.
The lowest limit that can be configured is 640 digits as provided in
`data`.

Verification:

.. doctest

```python

>>> import sys
>>> assert sys.int_info.default_max_str_digits == 4300, sys.int_info
>>> assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
>>> msg = int('578966293710682886880994035146873798396722250538762761564'
...           '9252925514383915483333812743580549779436104706260696366600'
...           '571186405732').to_bytes(53, 'big')
...

```

### Affected APIs

The limitation only applies to potentially slow conversions between `class`
and `class` or `class`:

* `int(string)` with default base 10.
* `int(string, base)` for all bases that are not a power of 2.
* `str(integer)`.
* `repr(integer)`.
* any other string conversion to base 10, for example `f"{integer}"`,
  `"{}".format(integer)`, or `b"%d" % integer`.

The limitations do not apply to functions with a linear algorithm:

* `int(string, base)` with base 2, 4, 8, 16, or 32.
* `int.from_bytes()` and `int.to_bytes()`.
* `hex()`, `oct()`, `bin()`.
* `ref` for hex, octal, and binary numbers.
* `class` to `class`.
* `class` to `class`.

### Configuring the limit

Before Python starts up you can use an environment variable or an interpreter
command line flag to configure the limit:

* :envvar:`PYTHONINTMAXSTRDIGITS`, e.g.
  `PYTHONINTMAXSTRDIGITS=640 python3` to set the limit to 640 or
  `PYTHONINTMAXSTRDIGITS=0 python3` to disable the limitation.
* :option:`-X int_max_str_digits <-X>`, e.g.
  `python3 -X int_max_str_digits=640`
* `data` contains the value of
  :envvar:`PYTHONINTMAXSTRDIGITS` or :option:`-X int_max_str_digits <-X>`.
  If both the env var and the `-X` option are set, the `-X` option takes
  precedence. A value of *-1* indicates that both were unset, thus a value of
  `data` was used during initialization.

From code, you can inspect the current limit and set a new one using these
`mod` APIs:

* `sys.get_int_max_str_digits()` and `sys.set_int_max_str_digits()` are
  a getter and setter for the interpreter-wide limit. Subinterpreters have
  their own limit.

Information about the default and minimum can be found in `data`:

* `data` is the compiled-in
  default limit.
* `data` is the lowest
  accepted value for the limit (other than 0 which disables it).

.. caution

```python

Setting a low limit *can* lead to problems. While rare, code exists that
contains integer constants in decimal in their source that exceed the
minimum threshold. A consequence of setting the limit is that Python source
code containing decimal integer literals longer than the limit will
encounter an error during parsing, usually at startup time or import time or
even at installation time - anytime an up to date ``.pyc`` does not already
exist for the code. A workaround for source that contains such large
constants is to convert them to ``0x`` hexadecimal form as it has no limit.

Test your application thoroughly if you use a low limit. Ensure your tests
run with the limit set early via the environment or flag so that it applies
during startup and even during any installation step that may invoke Python
to precompile ``.py`` sources to ``.pyc`` files.

```

### Recommended configuration

The default `data` is expected to be
reasonable for most applications. If your application requires a different
limit, set it from your main entry point using Python version agnostic code as
these APIs were added in security patch releases in versions before 3.12.

Example

```python

>>> import sys
>>> if hasattr(sys, "set_int_max_str_digits"):
...     upper_bound = 68000
...     lower_bound = 4004
...     current_limit = sys.get_int_max_str_digits()
...     if current_limit == 0 or current_limit > upper_bound:
...         sys.set_int_max_str_digits(upper_bound)
...     elif current_limit < lower_bound:
...         sys.set_int_max_str_digits(lower_bound)

```

If you need to disable it entirely, set it to `0`.

   Reference Manual (`ref`).

   similarly for tuples.

   "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).

   element is the tuple to be formatted.
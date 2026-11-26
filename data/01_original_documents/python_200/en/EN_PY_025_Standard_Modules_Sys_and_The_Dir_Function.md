<!-- page: 1 -->
# EN_PY_025: Standard Modules: The sys Module, Caching (__pycache__), and dir() Introspection

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Modules | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

  input script is calculated after the symlink is followed. In other
  words the directory containing the symlink is **not** added to the
  module search path.

After initialization, Python programs can modify "sys.path".  The
directory containing the script being run is placed at the beginning
of the search path, ahead of the standard library path. This means
that scripts in that directory will be loaded instead of modules of
the same name in the library directory. This is an error unless the
replacement is intended.  See section Standard Modules for more
information.


6.1.3. “Compiled” Python files
------------------------------

To speed up loading modules, Python caches the compiled version of
each module in the "__pycache__" directory under the name
"module.*version*.pyc", where the version encodes the format of the
compiled file; it generally contains the Python version number.  For
example, in CPython release 3.3 the compiled version of spam.py would
be cached as "__pycache__/spam.cpython-33.pyc".  This naming
convention allows compiled modules from different releases and
different versions of Python to coexist.

Python checks the modification date of the source against the compiled
version to see if it’s out of date and needs to be recompiled.  This
is a completely automatic process.  Also, the compiled modules are
platform-independent, so the same library can be shared among systems
with different architectures.

Python does not check the cache in two circumstances.  First, it
always recompiles and does not store the result for the module that’s
loaded directly from the command line.  Second, it does not check the

<!-- page: 2 -->

cache if there is no source module.  To support a non-source (compiled
only) distribution, the compiled module must be in the source
directory, and there must not be a source module.

Some tips for experts:

* You can use the "-O" or "-OO" switches on the Python command to
  reduce the size of a compiled module.  The "-O" switch removes
  assert statements, the "-OO" switch removes both assert statements
  and __doc__ strings.  Since some programs may rely on having these
  available, you should only use this option if you know what you’re
  doing.  “Optimized” modules have an "opt-" tag and are usually
  smaller.  Future releases may change the effects of optimization.

* A program doesn’t run any faster when it is read from a ".pyc" file
  than when it is read from a ".py" file; the only thing that’s faster
  about ".pyc" files is the speed with which they are loaded.

* The module "compileall" can create .pyc files for all modules in a
  directory.

* There is more detail on this process, including a flow chart of the
  decisions, in **PEP 3147**.


6.2. Standard Modules
=====================

Python comes with a library of standard modules, described in a
separate document, the Python Library Reference (“Library Reference”
hereafter).  Some modules are built into the interpreter; these
provide access to operations that are not part of the core of the
language but are nevertheless built in, either for efficiency or to
provide access to operating system primitives such as system calls.
The set of such modules is a configuration option which also depends
on the underlying platform.  For example, the "winreg" module is only
provided on Windows systems. One particular module deserves some
attention: "sys", which is built into every Python interpreter.  The
variables "sys.ps1" and "sys.ps2" define the strings used as primary
and secondary prompts:

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

```

<!-- page: 3 -->

These two variables are only defined if the interpreter is in
interactive mode.

The variable "sys.path" is a list of strings that determines the
interpreter’s search path for modules. It is initialized to a default
path taken from the environment variable "PYTHONPATH", or from a
built-in default if "PYTHONPATH" is not set.  You can modify it using
standard list operations:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')


```
6.3. The "dir()" Function
=========================

The built-in function "dir()" is used to find out which names a module
defines.  It returns a sorted list of strings:

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']

```

<!-- page: 4 -->

Without arguments, "dir()" lists the names you have defined currently:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

```
Note that it lists all types of names: variables, modules, functions,
etc.

"dir()" does not list the names of built-in functions and variables.
If you want a list of those, they are defined in the standard module
"builtins":

```python
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']


```

<!-- page: 5 -->

6.4. Packages
=============
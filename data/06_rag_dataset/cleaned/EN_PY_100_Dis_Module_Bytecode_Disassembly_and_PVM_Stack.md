# EN_PY_100: dis Module: Python Bytecode Disassembly, PVM Stack Evaluation, and Opcode Analysis

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: CPython Internals | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

"dis" — Disassembler for Python bytecode
****************************************

**Source code:** Lib/dis.py

======================================================================

The "dis" module supports the analysis of CPython *bytecode* by
disassembling it. The CPython bytecode which this module takes as an
input is defined in the file "Include/opcode.h" and used by the
compiler and the interpreter.

**CPython implementation detail:** Bytecode is an implementation
detail of the CPython interpreter.  No guarantees are made that
bytecode will not be added, removed, or changed between versions of
Python.  Use of this module should not be considered to work across
Python VMs or Python releases.

Changed in version 3.6: Use 2 bytes for each instruction. Previously
the number of bytes varied by instruction.

Changed in version 3.10: The argument of jump, exception handling and
loop instructions is now the instruction offset rather than the byte
offset.

Changed in version 3.11: Some instructions are accompanied by one or
more inline cache entries, which take the form of "CACHE"
instructions. These instructions are hidden by default, but can be
shown by passing "show_caches=True" to any "dis" utility. Furthermore,
the interpreter now adapts the bytecode to specialize it for different
runtime conditions. The adaptive bytecode can be shown by passing
"adaptive=True".

Changed in version 3.12: The argument of a jump is the offset of the

target instruction relative to the instruction that appears
immediately after the jump instruction’s "CACHE" entries.As a
consequence, the presence of the "CACHE" instructions is transparent
for forward jumps but needs to be taken into account when reasoning
about backward jumps.

Example: Given the function "myfunc()":

```python
def myfunc(alist):
    return len(alist)

```

the following command can be used to display the disassembly of
"myfunc()":

```python
>>> dis.dis(myfunc)
  2           0 RESUME                   0

  3           2 LOAD_GLOBAL              1 (NULL + len)
             12 LOAD_FAST                0 (alist)
             14 CALL                     1
             22 RETURN_VALUE

```

(The “2” is a line number).

Command-line interface
======================

The "dis" module can be invoked as a script from the command line:

   python -m dis [-h] [infile]

The following options are accepted:

-h, --help

   Display usage and exit.

If "infile" is specified, its disassembled code will be written to
stdout. Otherwise, disassembly is performed on compiled source code
recieved from stdin.

Bytecode analysis
=================

Added in version 3.4.

The bytecode analysis API allows pieces of Python code to be wrapped
in a "Bytecode" object that provides easy access to details of the
compiled code.

class dis.Bytecode(x, *, first_line=None, current_offset=None, show_caches=False, adaptive=False)

   Analyse the bytecode corresponding to a function, generator,
   asynchronous generator, coroutine, method, string of source code,
   or a code object (as returned by "compile()").

   This is a convenience wrapper around many of the functions listed
   below, most notably "get_instructions()", as iterating over a
   "Bytecode" instance yields the bytecode operations as "Instruction"
   instances.

   If *first_line* is not "None", it indicates the line number that

```python
should be reported for the first source line in the disassembled
code.  Otherwise, the source line information (if any) is taken
directly from the disassembled code object.

If *current_offset* is not "None", it refers to an instruction
offset in the disassembled code. Setting this means "dis()" will
display a “current instruction” marker against the specified
opcode.

If *show_caches* is "True", "dis()" will display inline cache
entries used by the interpreter to specialize the bytecode.

If *adaptive* is "True", "dis()" will display specialized bytecode
that may be different from the original bytecode.

classmethod from_traceback(tb, *, show_caches=False)

   Construct a "Bytecode" instance from the given traceback,
   setting *current_offset* to the instruction responsible for the
   exception.

codeobj

   The compiled code object.

first_line

   The first source line of the code object (if available)

dis()

   Return a formatted view of the bytecode operations (the same as
   printed by "dis.dis()", but returned as a multi-line string).

info()

   Return a formatted multi-line string with detailed information
   about the code object, like "code_info()".

Changed in version 3.7: This can now handle coroutine and
asynchronous generator objects.

Changed in version 3.11: Added the *show_caches* and *adaptive*
parameters.

```

Example:

```python
>>> bytecode = dis.Bytecode(myfunc)
>>> for instr in bytecode:
...     print(instr.opname)
...
RESUME
LOAD_GLOBAL
LOAD_FAST
CALL
RETURN_VALUE

```

Analysis functions
==================

The "dis" module also defines the following analysis functions that
convert the input directly to the desired output. They can be useful
if only a single operation is being performed, so the intermediate
analysis object isn’t useful:

dis.code_info(x)

```python
Return a formatted multi-line string with detailed code object
information for the supplied function, generator, asynchronous
generator, coroutine, method, source code string or code object.

Note that the exact contents of code info strings are highly
implementation dependent and they may change arbitrarily across
Python VMs or Python releases.

Added in version 3.2.

Changed in version 3.7: This can now handle coroutine and
asynchronous generator objects.

```

dis.show_code(x, *, file=None)

```python
Print detailed code object information for the supplied function,
method, source code string or code object to *file* (or
"sys.stdout" if *file* is not specified).

This is a convenient shorthand for "print(code_info(x),
file=file)", intended for interactive exploration at the
interpreter prompt.

Added in version 3.2.

Changed in version 3.4: Added *file* parameter.

```

dis.dis(x=None, *, file=None, depth=None, show_caches=False, adaptive=False)

   Disassemble the *x* object.  *x* can denote either a module, a
   class, a method, a function, a generator, an asynchronous
   generator, a coroutine, a code object, a string of source code or a
   byte sequence of raw bytecode. For a module, it disassembles all
   functions. For a class, it disassembles all methods (including

```python
class and static methods). For a code object or sequence of raw
bytecode, it prints one line per bytecode instruction. It also
recursively disassembles nested code objects. These can include
generator expressions, nested functions, the bodies of nested
classes, and the code objects used for annotation scopes. Strings
are first compiled to code objects with the "compile()" built-in
function before being disassembled.  If no object is provided, this
function disassembles the last traceback.

The disassembly is written as text to the supplied *file* argument
if provided and to "sys.stdout" otherwise.

The maximal depth of recursion is limited by *depth* unless it is
"None". "depth=0" means no recursion.

If *show_caches* is "True", this function will display inline cache
entries used by the interpreter to specialize the bytecode.

If *adaptive* is "True", this function will display specialized
bytecode that may be different from the original bytecode.

Changed in version 3.4: Added *file* parameter.

Changed in version 3.7: Implemented recursive disassembling and
added *depth* parameter.

Changed in version 3.7: This can now handle coroutine and
asynchronous generator objects.

Changed in version 3.11: Added the *show_caches* and *adaptive*
parameters.

```

dis.distb(tb=None, *, file=None, show_caches=False, adaptive=False)

   Disassemble the top-of-stack function of a traceback, using the

```python
last traceback if none was passed.  The instruction causing the
exception is indicated.

The disassembly is written as text to the supplied *file* argument
if provided and to "sys.stdout" otherwise.

Changed in version 3.4: Added *file* parameter.

Changed in version 3.11: Added the *show_caches* and *adaptive*
parameters.

```

dis.disassemble(code, lasti=-1, *, file=None, show_caches=False, adaptive=False)
dis.disco(code, lasti=-1, *, file=None, show_caches=False, adaptive=False)

   Disassemble a code object, indicating the last instruction if
   *lasti* was provided.  The output is divided in the following
   columns:

```python
1. the line number, for the first instruction of each line

2. the current instruction, indicated as "-->",

3. a labelled instruction, indicated with ">>",

4. the address of the instruction,

5. the operation code name,

6. operation parameters, and

7. interpretation of the parameters in parentheses.

The parameter interpretation recognizes local and global variable
names, constant values, branch targets, and compare operators.

The disassembly is written as text to the supplied *file* argument
if provided and to "sys.stdout" otherwise.

Changed in version 3.4: Added *file* parameter.

Changed in version 3.11: Added the *show_caches* and *adaptive*
parameters.

```

dis.get_instructions(x, *, first_line=None, show_caches=False, adaptive=False)

   Return an iterator over the instructions in the supplied function,
   method, source code string or code object.

   The iterator generates a series of "Instruction" named tuples
   giving the details of each operation in the supplied code.

   If *first_line* is not "None", it indicates the line number that

```python
should be reported for the first source line in the disassembled
code.  Otherwise, the source line information (if any) is taken
directly from the disassembled code object.

The *show_caches* and *adaptive* parameters work as they do in
"dis()".

Added in version 3.4.

Changed in version 3.11: Added the *show_caches* and *adaptive*
parameters.

```

dis.findlinestarts(code)

   This generator function uses the "co_lines()" method of the code
   object *code* to find the offsets which are starts of lines in the
   source code.  They are generated as "(offset, lineno)" pairs.

   Changed in version 3.6: Line numbers can be decreasing. Before,
   they were always increasing.

   Changed in version 3.10: The **PEP 626** "co_lines()" method is
   used instead of the "co_firstlineno" and "co_lnotab" attributes of
   the code object.

dis.findlabels(code)

   Detect all offsets in the raw compiled bytecode string *code* which

```python
are jump targets, and return a list of these offsets.

```

dis.stack_effect(opcode, oparg=None, *, jump=None)

```python
Compute the stack effect of *opcode* with argument *oparg*.

If the code has a jump target and *jump* is "True",
"stack_effect()" will return the stack effect of jumping.  If
*jump* is "False", it will return the stack effect of not jumping.
And if *jump* is "None" (default), it will return the maximal stack
effect of both cases.

Added in version 3.4.

Changed in version 3.8: Added *jump* parameter.

```

Python Bytecode Instructions
============================

The "get_instructions()" function and "Bytecode" class provide details
of bytecode instructions as "Instruction" instances:

class dis.Instruction

```python
Details for a bytecode operation

opcode

   numeric code for operation, corresponding to the opcode values
   listed below and the bytecode values in the Opcode collections.

opname

   human readable name for operation

arg

   numeric argument to operation (if any), otherwise "None"

argval

   resolved arg value (if any), otherwise "None"

argrepr

   human readable description of operation argument (if any),
   otherwise an empty string.

offset

   start index of operation within bytecode sequence

starts_line

   line started by this opcode (if any), otherwise "None"

is_jump_target

   "True" if other code jumps to here, otherwise "False"

positions

   "dis.Positions" object holding the start and end locations that
   are covered by this instruction.

Added in version 3.4.

Changed in version 3.11: Field "positions" is added.

```

class dis.Positions

   In case the information is not available, some fields might be
   "None".

   lineno

   end_lineno

   col_offset

   end_col_offset

   Added in version 3.11.

The Python compiler currently generates the following bytecode
instructions.

**General instructions**

In the following, We will refer to the interpreter stack as "STACK"
and describe operations on it as if it was a Python list. The top of
the stack corresponds to "STACK[-1]" in this language.

NOP

   Do nothing code.  Used as a placeholder by the bytecode optimizer,
   and to generate line tracing events.

POP_TOP

   Removes the top-of-stack item:

      STACK.pop()

END_FOR

```python
Removes the top two values from the stack. Equivalent to "POP_TOP";
"POP_TOP". Used to clean up at the end of loops, hence the name.

Added in version 3.12.

```

END_SEND

   Implements "del STACK[-2]". Used to clean up when a generator
   exits.

   Added in version 3.12.

COPY(i)

   Push the i-th item to the top of the stack without removing it from
   its original location:

```python
   assert i > 0
   STACK.append(STACK[-i])

Added in version 3.11.

```

SWAP(i)

```python
Swap the top of the stack with the i-th element:

   STACK[-i], STACK[-1] = STACK[-1], STACK[-i]
```
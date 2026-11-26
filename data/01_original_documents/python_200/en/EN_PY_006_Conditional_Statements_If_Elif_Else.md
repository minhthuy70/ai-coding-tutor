<!-- page: 1 -->
# EN_PY_006: Conditional Statements (if, elif, else) and Boolean Evaluation

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Control Flow | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

4.1. "if" Statements
====================

Perhaps the most well-known statement type is the "if" statement.  For
example:

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More

```
There can be zero or more "elif" parts, and the "else" part is
optional.  The keyword ‘"elif"’ is short for ‘else if’, and is useful
to avoid excessive indentation.  An  "if" … "elif" … "elif" … sequence
is a substitute for the "switch" or "case" statements found in other
languages.

If you’re comparing the same value to several constants, or checking
for specific types or attributes, you may also find the "match"
statement useful. For more details see match Statements.

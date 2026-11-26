<!-- page: 1 -->
# EN_PY_008: Loop Controls: break, continue, and the else Clause on Loops

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Control Flow | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

4.4. "break" and "continue" Statements
======================================

The "break" statement breaks out of the innermost enclosing "for" or
"while" loop:

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(f"{n} equals {x} * {n//x}")
...             break
...
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3

```
The "continue" statement continues with the next iteration of the
loop:

```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print(f"Found an even number {num}")
...         continue
...     print(f"Found an odd number {num}")
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9


```

<!-- page: 2 -->

4.5. "else" Clauses on Loops
============================

In a "for" or "while" loop the "break" statement may be paired with an
"else" clause.  If the loop finishes without executing the "break",
the "else" clause executes.

In a "for" loop, the "else" clause is executed after the loop finishes
its final iteration, that is, if no break occurred.

In a "while" loop, it’s executed after the loop’s condition becomes
false.

In either kind of loop, the "else" clause is **not** executed if the
loop was terminated by a "break".  Of course, other ways of ending the
loop early, such as a "return" or a raised exception, will also skip
execution of the "else" clause.

This is exemplified in the following "for" loop, which searches for
prime numbers:

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

```
(Yes, this is the correct code.  Look closely: the "else" clause
belongs to the "for" loop, **not** the "if" statement.)

One way to think of the else clause is to imagine it paired with the

<!-- page: 3 -->

"if" inside the loop.  As the loop executes, it will run a sequence
like if/if/if/else. The "if" is inside the loop, encountered a number
of times. If the condition is ever true, a "break" will happen. If the
condition is never true, the "else" clause outside the loop will
execute.

When used with a loop, the "else" clause has more in common with the
"else" clause of a "try" statement than it does with that of "if"
statements: a "try" statement’s "else" clause runs when no exception
occurs, and a loop’s "else" clause runs when no "break" occurs. For
more on the "try" statement and exceptions, see Handling Exceptions.

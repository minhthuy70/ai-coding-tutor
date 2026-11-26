# EN_PY_058: Standard Library: Decimal Floating Point Arithmetic for Financial Systems

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Data Types | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

The difference becomes significant if the results are rounded to the
nearest cent:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73

```

The "Decimal" result keeps a trailing zero, automatically inferring
four place significance from multiplicands with two place
significance.  Decimal reproduces mathematics as done by hand and
avoids issues that can arise when binary floating point cannot exactly
represent decimal quantities.

Exact representation enables the "Decimal" class to perform modulo
calculations and equality tests that are unsuitable for binary
floating point:

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False

```

The "decimal" module provides arithmetic with as much precision as

needed:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```
# EN_PY_042: Multiple Inheritance, Cooperative Method Resolution, and C3 MRO

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

9.5.1. Multiple Inheritance
---------------------------

Python supports a form of multiple inheritance as well.  A class
definition with multiple base classes looks like this:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

```

For most purposes, in the simplest cases, you can think of the search
for attributes inherited from a parent class as depth-first, left-to-
right, not searching twice in the same class where there is an overlap
in the hierarchy. Thus, if an attribute is not found in
"DerivedClassName", it is searched for in "Base1", then (recursively)
in the base classes of "Base1", and if it was not found there, it was
searched for in "Base2", and so on.

In fact, it is slightly more complex than that; the method resolution
order changes dynamically to support cooperative calls to "super()".
This approach is known in some other multiple-inheritance languages as
call-next-method and is more powerful than the super call found in
single-inheritance languages.

Dynamic ordering is necessary because all cases of multiple
inheritance exhibit one or more diamond relationships (where at least
one of the parent classes can be accessed through multiple paths from
the bottommost class).  For example, all classes inherit from
"object", so any case of multiple inheritance provides more than one

path to reach "object".  To keep the base classes from being accessed
more than once, the dynamic algorithm linearizes the search order in a
way that preserves the left-to-right ordering specified in each class,
that calls each parent only once, and that is monotonic (meaning that
a class can be subclassed without affecting the precedence order of
its parents). Taken together, these properties make it possible to
design reliable and extensible classes with multiple inheritance.  For
more detail, see The Python 2.3 Method Resolution Order.
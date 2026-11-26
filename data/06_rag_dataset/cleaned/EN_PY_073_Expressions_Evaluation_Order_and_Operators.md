# EN_PY_073: Expressions: Operator Precedence, Evaluation Order, and Short-Circuit Semantics

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Language Reference | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

6. Expressions
**************

This chapter explains the meaning of the elements of expressions in
Python.

**Syntax Notes:** In this and the following chapters, extended BNF
notation will be used to describe syntax, not lexical analysis.  When
(one alternative of) a syntax rule has the form

   name ::= othername

and no semantics are given, the semantics of this form of "name" are
the same as for "othername".

6.1. Arithmetic conversions
===========================

When a description of an arithmetic operator below uses the phrase
“the numeric arguments are converted to a common type”, this means
that the operator implementation for built-in types works as follows:

* If either argument is a complex number, the other is converted to
  complex;

* otherwise, if either argument is a floating-point number, the other
  is converted to floating point;

* otherwise, both must be integers and no conversion is necessary.

Some additional rules apply for certain operators (e.g., a string as a
left argument to the ‘%’ operator).  Extensions must define their own
conversion behavior.

6.2. Atoms
==========

Atoms are the most basic elements of expressions.  The simplest atoms
are identifiers or literals.  Forms enclosed in parentheses, brackets
or braces are also categorized syntactically as atoms.  The syntax for
atoms is:

   atom      ::= identifier | literal | enclosure
   enclosure ::= parenth_form | list_display | dict_display | set_display
                 | generator_expression | yield_atom

6.2.1. Identifiers (Names)
--------------------------

An identifier occurring as an atom is a name.  See section Identifiers
and keywords for lexical definition and section Naming and binding for
documentation of naming and binding.

When the name is bound to an object, evaluation of the atom yields
that object. When a name is not bound, an attempt to evaluate it
raises a "NameError" exception.

6.2.1.1. Private name mangling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an identifier that textually occurs in a class definition begins
with two or more underscore characters and does not end in two or more
underscores, it is considered a *private name* of that class.

See also: The class specifications.

More precisely, private names are transformed to a longer form before
code is generated for them.  If the transformed name is longer than
255 characters, implementation-defined truncation may happen.

The transformation is independent of the syntactical context in which
the identifier is used but only the following private identifiers are
mangled:

* Any name used as the name of a variable that is assigned or read or

  any name of an attribute being accessed.

  The "__name__" attribute of nested functions, classes, and type
  aliases is however not mangled.

* The name of imported modules, e.g., "__spam" in "import __spam". If
  the module is part of a package (i.e., its name contains a dot), the
  name is *not* mangled, e.g., the "__foo" in "import __foo.bar" is
  not mangled.

* The name of an imported member, e.g., "__f" in "from spam import
  __f".

The transformation rule is defined as follows:

* The class name, with leading underscores removed and a single
  leading underscore inserted, is inserted in front of the identifier,
  e.g., the identifier "__spam" occurring in a class named "Foo",
  "_Foo" or "__Foo" is transformed to "_Foo__spam".

* If the class name consists only of underscores, the transformation
  is the identity, e.g., the identifier "__spam" occurring in a class
  named "_" or "__" is left as is.

6.2.2. Literals
---------------

Python supports string and bytes literals and various numeric
literals:

   literal ::= stringliteral | bytesliteral
               | integer | floatnumber | imagnumber

Evaluation of a literal yields an object of the given type (string,
bytes, integer, floating-point number, complex number) with the given
value.  The value may be approximated in the case of floating-point
and imaginary (complex) literals.  See section Literals for details.

All literals correspond to immutable data types, and hence the
object’s identity is less important than its value.  Multiple
evaluations of literals with the same value (either the same
occurrence in the program text or a different occurrence) may obtain
the same object or a different object with the same value.

6.2.3. Parenthesized forms
--------------------------

A parenthesized form is an optional expression list enclosed in
parentheses:

   parenth_form ::= "(" [starred_expression] ")"

A parenthesized expression list yields whatever that expression list
yields: if the list contains at least one comma, it yields a tuple;
otherwise, it yields the single expression that makes up the
expression list.

An empty pair of parentheses yields an empty tuple object.  Since
tuples are immutable, the same rules as for literals apply (i.e., two
occurrences of the empty tuple may or may not yield the same object).

Note that tuples are not formed by the parentheses, but rather by use
of the comma.  The exception is the empty tuple, for which parentheses
*are* required — allowing unparenthesized “nothing” in expressions
would cause ambiguities and allow common typos to pass uncaught.

6.2.4. Displays for lists, sets and dictionaries
------------------------------------------------

For constructing a list, a set or a dictionary Python provides special
syntax called “displays”, each of them in two flavors:

* either the container contents are listed explicitly, or

* they are computed via a set of looping and filtering instructions,
  called a *comprehension*.

Common syntax elements for comprehensions are:

   comprehension ::= assignment_expression comp_for

```python
comp_for      ::= ["async"] "for" target_list "in" or_test [comp_iter]
comp_iter     ::= comp_for | comp_if
comp_if       ::= "if" or_test [comp_iter]

```

The comprehension consists of a single expression followed by at least

one "for" clause and zero or more "for" or "if" clauses. In this case,
the elements of the new container are those that would be produced by
considering each of the "for" or "if" clauses a block, nesting from
left to right, and evaluating the expression to produce an element
each time the innermost block is reached.

However, aside from the iterable expression in the leftmost "for"
clause, the comprehension is executed in a separate implicitly nested
scope. This ensures that names assigned to in the target list don’t
“leak” into the enclosing scope.

The iterable expression in the leftmost "for" clause is evaluated
directly in the enclosing scope and then passed as an argument to the
implicitly nested scope. Subsequent "for" clauses and any filter
condition in the leftmost "for" clause cannot be evaluated in the
enclosing scope as they may depend on the values obtained from the
leftmost iterable. For example: "[x*y for x in range(10) for y in
range(x, x+10)]".

To ensure the comprehension always results in a container of the
appropriate type, "yield" and "yield from" expressions are prohibited
in the implicitly nested scope.

Since Python 3.6, in an "async def" function, an "async for" clause
may be used to iterate over a *asynchronous iterator*. A comprehension
in an "async def" function may consist of either a "for" or "async
for" clause following the leading expression, may contain additional
"for" or "async for" clauses, and may also use "await" expressions.

If a comprehension contains "async for" clauses, or if it contains
"await" expressions or other asynchronous comprehensions anywhere
except the iterable expression in the leftmost "for" clause, it is
called an *asynchronous comprehension*. An asynchronous comprehension
may suspend the execution of the coroutine function in which it
appears. See also **PEP 530**.

Added in version 3.6: Asynchronous comprehensions were introduced.

Changed in version 3.8: "yield" and "yield from" prohibited in the
implicitly nested scope.

Changed in version 3.11: Asynchronous comprehensions are now allowed
inside comprehensions in asynchronous functions. Outer comprehensions
implicitly become asynchronous.

6.2.5. List displays
--------------------

A list display is a possibly empty series of expressions enclosed in
square brackets:

   list_display ::= "[" [flexible_expression_list | comprehension] "]"

A list display yields a new list object, the contents being specified
by either a list of expressions or a comprehension.  When a comma-
separated list of expressions is supplied, its elements are evaluated
from left to right and placed into the list object in that order.
When a comprehension is supplied, the list is constructed from the
elements resulting from the comprehension.

6.2.6. Set displays
-------------------

A set display is denoted by curly braces and distinguishable from
dictionary displays by the lack of colons separating keys and values:

   set_display ::= "{" (flexible_expression_list | comprehension) "}"

A set display yields a new mutable set object, the contents being
specified by either a sequence of expressions or a comprehension.
When a comma-separated list of expressions is supplied, its elements
are evaluated from left to right and added to the set object.  When a
comprehension is supplied, the set is constructed from the elements
resulting from the comprehension.

An empty set cannot be constructed with "{}"; this literal constructs
an empty dictionary.

6.2.7. Dictionary displays
--------------------------

A dictionary display is a possibly empty series of dict items
(key/value pairs) enclosed in curly braces:

   dict_display       ::= "{" [dict_item_list | dict_comprehension] "}"
   dict_item_list     ::= dict_item ("," dict_item)* [","]
   dict_item          ::= expression ":" expression | "**" or_expr

   dict_comprehension ::= expression ":" expression comp_for

A dictionary display yields a new dictionary object.

If a comma-separated sequence of dict items is given, they are
evaluated from left to right to define the entries of the dictionary:
each key object is used as a key into the dictionary to store the
corresponding value.  This means that you can specify the same key
multiple times in the dict item list, and the final dictionary’s value
for that key will be the last one given.

A double asterisk "**" denotes *dictionary unpacking*. Its operand
must be a *mapping*.  Each mapping item is added to the new
dictionary.  Later values replace values already set by earlier dict
items and earlier dictionary unpackings.

Added in version 3.5: Unpacking into dictionary displays, originally
proposed by **PEP 448**.

A dict comprehension, in contrast to list and set comprehensions,
needs two expressions separated with a colon followed by the usual
“for” and “if” clauses. When the comprehension is run, the resulting
key and value elements are inserted in the new dictionary in the order
they are produced.

Restrictions on the types of the key values are listed earlier in
section The standard type hierarchy.  (To summarize, the key type
should be *hashable*, which excludes all mutable objects.)  Clashes
between duplicate keys are not detected; the last value (textually
rightmost in the display) stored for a given key value prevails.

Changed in version 3.8: Prior to Python 3.8, in dict comprehensions,
the evaluation order of key and value was not well-defined.  In
CPython, the value was evaluated before the key.  Starting with 3.8,
the key is evaluated before the value, as proposed by **PEP 572**.

6.2.8. Generator expressions
----------------------------

A generator expression is a compact generator notation in parentheses:

```python
generator_expression ::= "(" expression comp_for ")"
```
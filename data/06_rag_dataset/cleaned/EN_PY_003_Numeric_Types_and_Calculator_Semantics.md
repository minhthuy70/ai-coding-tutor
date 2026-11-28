# EN_PY_003: Using Python as a Calculator: Numbers and Arithmetic

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Data Types | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

3. An Informal Introduction to Python
*************************************

In the following examples, input and output are distinguished by the
presence or absence of prompts (*>>>* and *…*): to repeat the example,
you must type everything after the prompt, when the prompt appears;
lines that do not begin with a prompt are output from the interpreter.
Note that a secondary prompt on a line by itself in an example means
you must type a blank line; this is used to end a multi-line command.

Many of the examples in this manual, even those entered at the
interactive prompt, include comments.  Comments in Python start with
the hash character, "#", and extend to the end of the physical line.
A comment may appear at the start of a line or following whitespace or
code, but not within a string literal.  A hash character within a
string literal is just a hash character. Since comments are to clarify
code and are not interpreted by Python, they may be omitted when
typing in examples.

Some examples:

   # this is the first comment
   spam = 1  # and this is the second comment
             # ... and now a third!
   text = "# This is not a comment because it's inside quotes."

3.1. Using Python as a Calculator
=================================

Let’s try some simple Python commands.  Start the interpreter and wait
for the primary prompt, ">>>".  (It shouldn’t take long.)

3.1.1. Numbers
--------------

The interpreter acts as a simple calculator: you can type an
expression at it and it will write the value.  Expression syntax is
straightforward: the operators "+", "-", "*" and "/" can be used to
perform arithmetic; parentheses ("()") can be used for grouping. For
example:

```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating-point number
1.6

```

The integer numbers (e.g. "2", "4", "20") have type "int", the ones
with a fractional part (e.g. "5.0", "1.6") have type "float".  We will
see more about numeric types later in the tutorial.

Division ("/") always returns a float.  To do *floor division* and get
an integer result you can use the "//" operator; to calculate the
remainder you can use "%":

```python
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17

```

With Python, it is possible to use the "**" operator to calculate
powers [1]:

```python
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128

```

The equal sign ("=") is used to assign a value to a variable.
Afterwards, no result is displayed before the next interactive prompt:

```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900

```

If a variable is not “defined” (assigned a value), trying to use it
will give you an error:

```python
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

```

There is full support for floating point; operators with mixed type
operands convert the integer operand to floating point:

```python
>>> 4 * 3.75 - 1
14.0

```

In interactive mode, the last printed expression is assigned to the
variable "_".  This means that when you are using Python as a desk
calculator, it is somewhat easier to continue calculations, for
example:

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06

```

This variable should be treated as read-only by the user.  Don’t

explicitly assign a value to it — you would create an independent
local variable with the same name masking the built-in variable with
its magic behavior.

In addition to "int" and "float", Python supports other types of
numbers, such as "Decimal" and "Fraction". Python also has built-in
support for complex numbers, and uses the "j" or "J" suffix to
indicate the imaginary part (e.g. "3+5j").

3.1.2. Text
-----------

Python can manipulate text (represented by type "str", so-called
“strings”) as well as numbers.  This includes characters “"!"”, words
“"rabbit"”, names “"Paris"”, sentences “"Got your back."”, etc. “"Yay!
:)"”. They can be enclosed in single quotes ("'...'") or double quotes
(""..."") with the same result [2].

```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
>>> '1975'  # digits and numerals enclosed in quotes are also strings
'1975'
```

To quote a quote, we need to “escape” it, by preceding it with "\".
Alternatively, we can use the other type of quotation marks:

```python
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'

```

In the Python shell, the string definition and output string can look
different.  The "print()" function produces a more readable output, by
omitting the enclosing quotes and by printing escaped and special

characters:
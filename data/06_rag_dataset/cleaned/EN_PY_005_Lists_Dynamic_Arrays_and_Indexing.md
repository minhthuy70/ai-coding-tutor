# EN_PY_005: Lists: Mutable Dynamic Sequences and Slicing

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Data Structures | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

   25

```python
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]

```

Lists also support operations like concatenation:

```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

```

Unlike strings, which are *immutable*, lists are a *mutable* type,
i.e. it is possible to change their content:

```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]

```

You can also add new items at the end of the list, by using the
"list.append()" *method* (we will see more about methods later):

```python
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]

```

Simple assignment in Python never copies data. When you assign a list
to a variable, the variable refers to the *existing list*. Any changes
you make to the list through one variable will be seen through all
other variables that refer to it.:

```python
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]

```

All slice operations return a new list containing the requested
elements.  This means that the following slice returns a shallow copy
of the list:

```python
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
["Red", "Green", "Blue", "Alpha"]
>>> rgba
["Red", "Green", "Blue", "Alph"]

```

Assignment to slices is also possible, and this can even change the
size of the list or clear it entirely:

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]

```

The built-in function "len()" also applies to lists:

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4

```

It is possible to nest lists (create lists containing other lists),
for example:

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'

```

3.2. First Steps Towards Programming
====================================

Of course, we can use Python for more complicated tasks than adding
two and two together.  For instance, we can write an initial sub-
sequence of the Fibonacci series as follows:

```python
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
0
1
1
2
3
5
8

```

This example introduces several new features.

* The first line contains a *multiple assignment*: the variables "a"
  and "b" simultaneously get the new values 0 and 1.  On the last line
  this is used again, demonstrating that the expressions on the right-
  hand side are all evaluated first before any of the assignments take
  place.  The right-hand side expressions are evaluated  from the left
  to the right.

* The "while" loop executes as long as the condition (here: "a < 10")
  remains true.  In Python, like in C, any non-zero integer value is
  true; zero is false.  The condition may also be a string or list
  value, in fact any sequence; anything with a non-zero length is
  true, empty sequences are false.  The test used in the example is a
  simple comparison.  The standard comparison operators are written
  the same as in C: "<" (less than), ">" (greater than), "==" (equal
  to), "<=" (less than or equal to), ">=" (greater than or equal to)
  and "!=" (not equal to).

* The *body* of the loop is *indented*: indentation is Python’s way of
  grouping statements.  At the interactive prompt, you have to type a
  tab or space(s) for each indented line.  In practice you will
  prepare more complicated input for Python with a text editor; all
  decent text editors have an auto-indent facility.  When a compound
  statement is entered interactively, it must be followed by a blank
  line to indicate completion (since the parser cannot guess when you
  have typed the last line).  Note that each line within a basic block
  must be indented by the same amount.

* The "print()" function writes the value of the argument(s) it is
  given. It differs from just writing the expression you want to write
  (as we did earlier in the calculator examples) in the way it handles
  multiple arguments, floating-point quantities, and strings.  Strings
  are printed without quotes, and a space is inserted between items,
  so you can format things nicely, like this:

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536

```

  The keyword argument *end* can be used to avoid the newline after
  the output, or end the output with a different string:

```python
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

```

-[ Footnotes ]-

[1] Since "**" has higher precedence than "-", "-3**2" will be
    interpreted as "-(3**2)" and thus result in "-9".  To avoid this
    and get "9", you can use "(-3)**2".

[2] Unlike other languages, special characters such as "\n" have the

```python
same meaning with both single ("'...'") and double (""..."")
quotes. The only difference between the two is that within single
quotes you don’t need to escape """ (but you have to escape "\'")
and vice versa.
```
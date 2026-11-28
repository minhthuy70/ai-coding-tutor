## Case Study: Fractions

• Want to add a new **type**

class Fraction(object):

§ Values are fractions: ½, ¾

"""Instance is a fraction n/d"""

\# INSTANCE ATTRIBUTES:

§ Operations are standard multiply, divide, etc.

\# \_numerator: an int

§ **Example**: $1/2^{*3}/4 = 3/8$

\# \_denominator: an int > 0

• Can do this with a class

§ Values are fraction objects

def \_\_init\_\_(self,n=0,d=1):

§ Operations are methods

"""Init: makes a Fraction"""

• **Example**: frac1.py

self.\_numerator = n

self.\_denominator = d

## Problem: Doing Math is Unwieldy

**What We Want**

$$
\left(\frac {1}{2} + \frac {1}{3} + \frac {1}{4}\right) * \frac {5}{4}
$$

**What We Get**

Why not use the standard Python math operations? >>> p = Fraction(1,2)

```python
>>> q = Fraction(1,3)
```

```python
>>> r = Fraction(1,4)
```

```python
>>> s = Fraction(5,4)
```

```python
>>> (p.add(q.add(r))).mult(s)
```

This is confusing!

## Operator Overloading

• Many operators in Python a special symbols § +, -, /, \*, \*\* for mathematics

==, !=, <, > for comparisons

• The meaning of these symbols depends on type

§ 1 + 2 vs 'Hello' + 'World'

§ 1 < 2 vs 'Hello' < 'World'

• Our new type might want to use these symbols

§ We overload them to support our new type

## Returning to Fractions

**What We Want**

$$
\left(\frac {1}{2} + \frac {1}{3} + \frac {1}{4}\right) * \frac {5}{4}
$$

Why not use the standard Python math operations?

## Operator Overloading

• Python has methods that correspond to built-in ops

§ \_\_add\_\_ corresponds to +

§ \_\_mul\_\_ corresponds to \*

§ \_\_eq\_\_ corresponds to ==

§ Not implemented by default

• To overload operators you implement these methods

## Operator Overloading: Multiplication

## class Fraction(object):

"""Instance is a fraction n/d"""

$$
> > > \mathrm{p} = \text {Fraction} (1, 2)
$$

\# \_numerator: an int

$$
> > > \mathrm{q} = \text {Fraction} (3, 4)
$$

\# \_denominator: an int > 0

$$
> > > \mathrm{r} = \mathrm{p} ^ {*} \mathrm{q}
$$

## def \_\_mul\_\_(self,q):

"""Returns: Product of self, q

Makes a new Fraction; does not

modify contents of self or q

Python converts to

Precondition: q a Fraction"""

assert type(q) == Fraction

$$
\ggg \mathrm{r} = \mathrm{p._mul_(q)}
$$

top= self.\_numerator\*q.\_numerator

bot= self.\_denominator\*q.\_denominator

return Fraction(top,bot)

Operator overloading uses method in object on left.

## Operator Overloading: Addition

## class Fraction(object):

$$
> > > \mathrm{p} = \text {Fraction} (1, 2)
$$

"'Instance is a fraction n/d'"

$$
> > > \mathrm{q} = \text {Fraction} (3, 4)
$$

\# \_numerator:  an int

\# \_denominator: an int > 0

$$
> > > \mathrm{r} = \mathrm{p} + \mathrm{q}
$$

$$
\text {def \_ add \_ (self,q):}
$$

"""Returns: Sum of self, q

Makes a new Fraction

Python converts to

Precondition: q a Fraction"""

assert type(q) == Fraction

$$
\ggg \mathrm{r} = \mathrm{p._add} (\mathrm{q})
$$

bot= self.\_denominator\*q.\_denominator

top= (self.\_numerator\*q.\_denominator+

self.\_denominator\*q.\_numerator)

return Fraction(top,bot)

Operator overloading uses method in object on left.

## Comparing Objects for Equality

• Earlier in course, we saw ==

## class Fraction(object):

compare object contents

"""Instance is a fraction n/d"""

\# \_numerator: an int

§ This is not the default

\# \_denominator: an int > 0

§ **Default**: folder names

• Must implement \_\_eq\_\_

## def \_\_eq\_\_(self,q):

§ Operator overloading!

"""Returns: True if self, q equal,

False if not, or q not a Fraction"""

§ Not limited to simple attribute comparison if type(q) != Fraction:

§ **Ex**: cross multiplying

return False

left = self.\_numerator\*q.\_denominator

rght = self.\_denominator\*q.\_numerator

return left == rght

## Recall: Overloading Multiplication

## class Fraction(object):

"""Instance is a fraction n/d"""

```python
>>> p = Fraction(1,2)
```

\# \_numerator: an int

\# \_denominator: an int > 0

```python
>>> q = 2 # an int
```

```python
>>> r = p\*q
```

def \_\_mul\_\_(self,q):

"""Returns: Product of self, q

Makes a new Fraction; does not

modify contents of self or q

~~Precondition: q a Fraction""~~"

Python converts to

<u>assert type(q) == Fraction</u>

```python
>>> r = p.\_\_mul\_\_(q) # ERROR
```

top = self.\_numerator\*q.\_numerator

bot= self.\_denominator\*q.\_denominator

return Fraction(top,bot)

Can only multiply fractions.

But ints “make sense” too.

## is Versus ==

Always use (x is None) **not** (x == None)

p **id2**

• p is q evaluates to False

§ Compares folder names

• p == q evaluates to True

§ Cannot change this

## Solution: Look at Argument Type

§ But only because method \_\_eq\_\_ compares contents

• Overloading use **left** type

§ p\*q => p.\_\_mul\_\_(q)

## class Fraction(object):

§ Done for us automatically

• What about type on **right**? § Have to handle ourselves § Looks in class definition

def \_\_mul\_\_(self,q):

• Can implement with ifs

§ Check type in method

§ Write helper for each type

§ Send to appropriate helper

"""Returns: Product of self, q

Precondition: q a Fraction or int"""

if type(q) == Fraction:

if type(q) == Fraction:

return self.\_mulFrac(q)

elif type(q) == int:

return self.\_mulInt(q)

def \_mulInt(self,q): # Hidden method

return self.\_mulInt(q)

return Fraction(self.\_numerator\*q,

self.\_denominator)

## A Better Multiplication

## class Fraction(object):

def \_\_mul\_\_(self,q):

return self.\_mulFrac(q)

"""Returns: Product of self, q

Precondition: q a Fraction or int"""

```python
>>> r = p.\_mul\_(q) # OK!
```

elif type(q) == int:

See frac3.py for a full example of this method

$$
> > > \mathrm{r} = \mathrm{p} ^ {*} \mathrm{q}
$$

```python
>>> q = 2 # an int
```

def \_mulInt(self,q): # Hidden method

return Fraction(self.\_numerator\*q,

```python
>>> p = Fraction(1,2)
```

self.\_denominator)

Python converts to

## We Have Come Full Circle

• On the first day, saw that a **type** is both

§ a set of values, and

§ the operations on them

• In Python, **all values are objects**

§ Everything has a folder in the heap

§ Just ignore it for immutable, basic types

• In Python, **all operations are methods**

§ Each operator has a double-underscore helper

§ Looks at type of object on left to process
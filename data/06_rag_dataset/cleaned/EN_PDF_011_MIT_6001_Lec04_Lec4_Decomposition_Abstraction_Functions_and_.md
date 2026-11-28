## DECOMPOSITION, ABSTRACTION, FUNCTIONS

(download slides and .py files Ă

6.0001 LECTU RE 4

Ěfollow along!)

## LAST TIME

while loops vs for loops

should know how to write both kinds

should know when to use them

guess-and-check and approximation methods

bisection method to speed up programs

## TODAY

structuring programs and hiding details

functions

specifications

keywords: return vs print

scope

## HOW DO WE WRITE CODE?

• covered language mechanisms

• know how to write different files for each computation

• each file is some piece of code

• each code is a sequence of instructions

problems with this approach

• easy for small-scale problems

• messy for larger problems

• hard to keep track of details

• how do you know the right info is supplied to the right part of code

## GOOD PROGRAMMING

more code not necessarily a good thing

measure good programmers by the amount of functionality

introduce **functions**

mechanism to achieve **decomposition** and **abstraction**

## EXAMPLE – PROJECTOR

a projector is a black box

don’t know how it works

know the interface: input/output

connect any electronic to it that can communicate with that input

black box somehow converts image from input source to a wall, magnifying it

**ABSTRACTION IDEA**: do not need to know how projector works to use it

## EXAMPLE – PROJECTOR

projecting large image for Olympics decomposed into separate tasks for separate projectors

each projector takes input and produces separate output

all projectors work together to produce larger image

**DECOMPOSITION IDEA**: different devices work together to achieve an end goal

## APPLY THESE CONCEPTS

## TO PROGRAMMING!

## CREATE STRUCTURE with DECOMPOSITION

in projector example, separate devices

in programming, divide code into **modules**

• are **self-contained**

• used to **break up** code 7

• intended to be **reusable**

• keep code **organized**

• **keep code coherent**

this lecture, achieve decomposition with **functions**

in a few weeks, achieve decomposition with **classes**

## SUPRESS DETAILS with ABSTRACTION

in projector example, instructions for how to use it are sufficient, no need to know how to build one

in programming, think of a piece of code as a **black box**

• cannot see details

• do not need to see details

• do not want to see details

• hide tedious coding details

## achieve abstraction with function specifications or docstrings

## FUNCTIONS

write reusable pieces/chunks of code, called **functions**

functions are not run in a program until they are “**called**” or “**invoked**” in a program

function characteristics:

• has a **name**

• has **parameters** (0 or more)

• has a **docstring** (optional but recommended)

• has a **body**

**returns** something

## HOW TO WRITE and CALL/INVOKE A FUNCTION

```python
def is_even( i ): parameters or arguments
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("inside is_even")
    return i%2 == 0

    is_even(3)
```

## IN THE FUNCTION BODY

```python
def is_even( i ):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("inside is_even")
    return i%2 == 0
```

## VARIABLE SCOPE

**formal parameter** gets bound to the value of **actual parameter** when function is called

new **scope/frame/environment** created when enter a function

**scope** is mapping of names to objects

$$
\begin{array}{l} \text {def f(\boxed {x}):} \\ \text {x = x + 1} \\ \text {print('in f(x): x =', x)} \\ \text {return x} \end{array}
$$

$$
\begin{array}{r c l} \mathbf {x} & = & 3 \\ \mathbf {z} & = & f (\boxed {\mathbf {x}}) \end{array} \quad \begin{array}{l} \text {actual} \\ \text {parameter} \end{array}
$$

## VARIABLE SCOPE

```python
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f( x )

Global scope
f      Some
code
x       3

f scope
x       3
```

## VARIABLE SCOPE

```python
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f( x )

Global scope
f      Some
code
x       3

f scope
x       4
```

## VARIABLE SCOPE

```python
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f( x )
```

## VARIABLE SCOPE

```python
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f( x )
```

# ONE WARNING IF NO return STATEMENT

```python
def is_even( i ):
    """
    Input: i, a positive int
    Does not return anything
    """
    i%2 == 0
```

Python returns the value **None, if no return given**

represents the absence of a value

## return

return only has meaning **inside** a function

only **one** return executed inside a function

code inside function but after return statement not executed

has a value associated with it, **given to function caller**

## print

print can be used **outside** functions

can execute **many** print statements inside a function

code inside function can be executed after a print statement

has a value associated with it, **outputted** to the console

## FUNCTIONS AS ARGUMENTS

```python
■ arguments can take on any type, even functions
def func_a():
    print 'inside func_a'
def func_b(y):
    print 'inside func_b'
    return y
def func_c(z):
    print 'inside func_c'
    return z()
print func_a()
print 5 + func_b(2)
print func_c(func_a)
```

## FUNCTIONS AS ARGUMENTS

```python
def func_a():
    print 'inside func_a'
def func_b(y):
    print 'inside func_b'
    return y
def func_c(z):
    print 'inside func_c'
    return z()
print func_a()
print 5 + func_b(2)
print func_c(func_a)
```

## FUNCTIONS AS ARGUMENTS

```python
def func_a():
    print 'inside func_a'
def func_b(y):
    print 'inside func_b'
    return y
def func_c(z):
    print 'inside func_c'
    return z()
print func_a()
print 5 + func_b(2)
print func_c(func_a)
txt
Global scope
func_a
func_b
func_c
Some code
Some code
Some code
None
7
func_b scope
y
2
returns 2
```

## FUNCTIONS AS ARGUMENTS

```python
def func_a():
    print 'inside func_a'
def func_b(y):
    print 'inside func_b'
    return y
def func_c(z):
    print 'inside func_c'
    return z()
print func_a()
print 5 + func_b(2)
print func_c(func_a)
```

## SCOPE EXAMPLE

inside a function, **can access** a variable defined outside

inside a function, **cannot modify** a variable defined outside -- can using **global variables**, but frowned upon

$$
\begin{array}{l} \text {def f(y):} \\ \text {x is re-defined in scope of f} \quad \boxed {\mathrm{x=1}} \\ \text {print(x)} \\ \boxed {\mathrm{x=5}} \\ \text {f(x)} \\ \text {print(x)} \end{array}
$$

$$
\begin{array}{l} \text {def g(y):} \\ \text {x from outside g print(x) print(x + 1)} \\ \boxed {\mathrm{x=5}} \\ \text {g(x)} \\ \text {print(x)} \end{array}
$$

$$
\mathrm{x} + = 1
$$

$$
\mathrm{x} = 5
$$

print(x)

## SCOPE EXAMPLE

inside a function, **can access** a variable defined outside

inside a function, **cannot modify** a variable defined outside -- can using **global variables**, but frowned upon

$$
\begin{array}{l} \text {def f(y):} \\ \quad \mathrm{x=1} \\ \quad \mathrm{x+=1} \\ \quad \text {print(x)} \\ \text {x=5} \\ \text {f(x)} \\ \text {print(x)} \end{array}
$$

$$
\begin{array}{l} \text {def h(y):} \\ \text {x += 1} \\ \text {x = 5} \\ \text {h(x)} \\ \text {print(x)} \end{array}
$$

## HARDER SCOPE EXAMPLE

IMPORTANT and TRICKY!

## Python Tutor is your best friend to help sort this out!

[**http://www.pythontutor.com/**](http://www.pythontutor.com/)

## SCOPE DETAILS

```python
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x
x = 3
z = g(x)
```

## SCOPE DETAILS

```python
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x

x = 3
z = g(x)
txt
Global scope
g    Some code
x    3
z

g scope
x    3
h    Some code
```

## SCOPE DETAILS

```python
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x

x = 3
z = g(x)
txt
Global scope
g    Some code
x    3
z

g scope
x    4
h    Some code
```

## SCOPE DETAILS

```python
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x

x = 3
z = g(x)
csv
Global scope
g Some code
x 3
z
g scope
x 4
h Some code
x "abc"
h scope
x "abc"
returns None
```

## SCOPE DETAILS

```python
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x

x = 3
z = g(x)
txt
Global scope
g Some code
x 3
z
g scope
x 4
h Some code
None
returns 4
```

## SCOPE DETAILS

```python
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x

x = 3
z = g(x)
```

## DECOMPOSITION & ABSTRACTION

powerful together

code can be used many times but only has to be debugged once!

6.0001 Introduction to Computer Science and Programming in Python Fall 2016

For information about citing these materials or our Terms of Use, visit: [https://ocw.mit.edu/terms](https://ocw.mit.edu/terms).
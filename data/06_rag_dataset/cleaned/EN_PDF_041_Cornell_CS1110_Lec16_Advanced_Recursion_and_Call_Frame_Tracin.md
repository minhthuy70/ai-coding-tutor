Lecture 16

## More Recursion

## Announcements for This Lecture

## Prelim 1

• Grades are back!

§ **80+:** A-/A/A+

§ **60-79:** B-/B/B+

§ **35-60:** C-/C/C+

§ **34-:** D/F

• Regrades are open

§ Handled in Gradescope

§ But grades can do **down!**

## Assignments & Videos

• Begin working on A4!

§ Just reading takes a while

§ Slightly longer than A3

§ Problems are harder

**Finish Pt. 1-3 this week!**

• Lecture Videos

§ **Videos 17.1-17.11** today

§ **Videos 19.1-19.7** Thurs

## Recall: Divide and Conquer

**Goal**: Solve problem P on a piece of data

## data

**Idea**: Split data into two parts and solve problem

**data 1**

**data 2**

Solve Problem P

Solve Problem P

**Combine Answer!**

## Example: Reversing a String

```python
def reverse(s):
    """Returns: reverse of s
python
Precondition: s a string"""
# 1. Handle small data
if len(s) <= 1:
    return s
```

\# 2. Break into two parts

\# 3. Combine the result

## Example: Reversing a String

```python
def reverse(s):
    """Returns: reverse of s
python
Precondition: s a string"""
# 1. Handle small data
if len(s) <= 1:
    return s
txt
# 2. Break into two parts
left = s[0]
right = reverse(s[1:])
```

\# 3. Combine the result

## Example: Reversing a String

```python
def reverse(s):
    """Returns: reverse of s
python
Precondition: s a string"""
# 1. Handle small data
if len(s) <= 1:
    return s
txt
# 2. Break into two parts
left = s[0]
right = reverse(s[l:])
txt
# 3. Combine the result
return right+left
```

## Example: Reversing a String

```python
def reverse(s):
    """Returns: reverse of s
    Precondition: s a string"""
    # 1. Handle small data
    if len(s) <= 1:
        return s

    # 2. Break into two parts
    left = s[0]
    right = reverse(s[1:])

    # 3. Combine the result
    return right+left

More Recursion
```

## Example: Reversing a String

```python
def reverse(s):
    """Returns: reverse of s
```

\# 2. Break

Remove

nto tw<u>o parts</u>recursive call

\# 3. Combine the result return right+left

Base Case

Recursive Case

## How to Break Up a Recursive Function?

def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267' Precondition: s represents a non-negative int"""

**Approach 1**

```txt
5 341267
```

## How to Break Up a Recursive Function?

## def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267' Precondition: s represents a non-negative int"""

## Approach 1

## How to Break Up a Recursive Function?

## def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267' Precondition: s represents a non-negative int"""

## Approach 1

341,267

## How to Break Up a Recursive Function?

## def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267' Precondition: s represents a non-negative int"""

## Approach 1

Always? When?

## How to Break Up a Recursive Function?

## def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267' Precondition: s represents a non-negative int"""

## Approach 1

341267

commafy

267

5341

## Approach 2

341,267

## How to Break Up a Recursive Function?

## def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267'

Precondition: s represents a non-negative int"""

## Approach 1

commafy

## Approach 2

commafy

Always? When?

commafy

## How to Break Up a Recursive Function?

## def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267'

Precondition: s represents a non-negative int"""

## Approach 1

## Approach 2

commafy

Always? When?

267

Always? When?

## How to Break Up a Recursive Function?

## def commafy(s):

"""Returns: string with commas every 3 digits e.g. commafy('5341267') = '5,341,267'

Precondition: s represents a non-negative int"""

## Approach 1

commafy

## Approach 2

commafy

More Recursion

## How to Break Up a Recursive Function?

```python
def commafy(s):
    """Returns: string with commas every 3 digits
    e.g. commafy('5341267') = '5,341,267'
    Precondition: s represents a non-negative int"""
    # 1. Handle small data.
    if len(s) <= 3:
        return s
    # 2. Break into two parts
    left = commafy(s[:-3])
    right = s[-3:] # Small part on RIGHT
    # 3. Combine the result
    return left + ',' + right
    More Recursion
```

## Complex Combination Steps

def separate(nums):

"""Returns: A tuple separating nums into neg and non-neg parts

This function returns a tuple (neg,pos). The value neg is a list of all the negative elements of nums (in their order from nums), while pos is a list of all the non-negative elements of nums (in their order from nums).

Example: separate([1, -1, 2, -5, -3, 0]) returns ([-1, -5, -3], [1, 2, 0])

Example: separate([-1, -5, -3]) returns ([-1, -5, -3],[])

Example: separate([1, 2, 0]) returns ([],[1, 2, 0])

Precond: nums is a (possibly empty) list of integers"""

```python
elif len(nums) == 1:
python
"'''Returns: A tuple separating nums into neg and non-neg parts'"
python
if nums[0] < 0:
    return ( nums[:], [] )
```

## Complex Combination Steps

```python
def separate(nums):
python
if len(nums) == 0:
    return ( [], [] )
```

Nothing in nums

All negative

All positive

## Complex Combination Steps

## def separate(nums):

"""Returns: A tuple separating nums into neg and non-neg parts""" # small data

\# break up the list

left = separate(nums[:1])

Breaking up is simple

rght = separate(nums[1:])

## Complex Combination Steps

def separate(nums):

"""Returns: A tuple separating nums into neg and non-neg parts"""

\# small data

\# break up the list

left = separate(nums[:1])

rght = separate(nums[1:])

\# combine the answers

neg = left[0]+right[0]

pos = left[1]+right[1]

return (neg,pos)

Breaking up is simple

Combining is not so simple

## Recursion and Objects

## • Class Person (person.py)

§ Objects have 3 attributes

name: String

§ mom: Person (or None)

§ dad: Person (or None)

• Represents the “family tree”

§ Goes as far back as known

§ Attributes mom and dad are None if not known

• **Constructor**: Person(n,m,d)

• Or Person(n) if no mom, dad

## Recursion and Objects

def num\_ancestors(p):

"""Returns: num of known ancestors Pre: p is a Person""" # 1. Handle small data. # No mom or dad (no ancestors)

\# 2. Break into two parts # Has mom or dad # Count ancestors of each one # (plus mom, dad themselves)

\# 3. Combine the result

## Recursion and Objects

```python
ef num_ancestors(p):
    """Returns: num of known ancestors
    Pre: p is a Person"""
    # 1. Handle small data.
    if p.mom == None and p.dad == None:
        return 0

    # 2. Break into two parts
    moms = 0
    if not p.mom == None:
        moms = 1+num_ancestors(p.mom)
    dads = 0
    if not p.dad== None:
        dads = 1+num_ancestors(p.dad)

    # 3. Combine the result
    return moms+dads
```

## Is All Recursion Divide and Conquer?

• Divide and conquer implies two halves “equal”

§ Performing the same check on each half

§ With some optimization for small halves

• Sometimes we are given a **recursive definition**

§ Math formula to compute that is recursive

§ String definition to check that is recursive

§ Picture to draw that is recursive

§ **Example**: n! = n (n-1)!

• In that case, we are just implementing definition

## Example: Palindromes

• String with ≥ 2 characters is a palindrome if:

§ its first and last characters are equal, and

§ the rest of the characters form a palindrome

• **Example:**

have to be the same

has to be a palindrome

• **Function to Implement:**

def ispalindrome(s):

"""Returns: True if s is a palindrome"""

```python
- its first and last characters are equal, and
- the rest of the characters form a palindrome
def ispalindrome(s):
    """Returns: True if s is a palindrome"""
    if len(s) < 2:
        return True
    # Halves not the same; not divide and conquer
    ends = s[0] == s[-1]
    middle = ispalindrome(s[1:-1])
    return ends and middle
    Recursive case
    Recursive Definition
```

## Example: Palindromes

• String with ≥ 2 characters is a palindrome if:

## Recursive Functions and Helpers

```python
ef ispalindrome2(s):
    """Returns: True if s is a palindrome
    Case of characters is ignored."""
    if len(s) < 2:
        return True
    # Halves not the same; not divide and conquer
    ends = equals_ignore_case(s[0], s[-1])
    middle = ispalindrome(s[1:-1])
    return ends and middle
```

## Recursive Functions and Helpers

```python
ef ispalindrome2(s):
    """Returns: True if s is a palindrome
    Case of characters is ignored."""
    if len(s) < 2:
        return True
    # Halves not the same; not divide and conquer
    ends = equals_ignore_case(s[0], s[-1])
    middle = ispalindrome(s[1:-1])
    return ends and middle
```

## Recursive Functions and Helpers

```python
def ispalindrome2(s):
    """Returns: True if s is a palindrome
    Case of characters is ignored."""
    if len(s) < 2:
        return True
    # Halves not the same; not divide and conquer
    ends = equals_ignore_case(s[0], s[-1])
    middle = ispalindrome(s[1:-1])
    return ends and middle

def equals_ignore_case(a, b):
    """Returns: True if a and b are same ignoring case"""
    return a.upper() == b.upper()
```

## Example: More Palindromes

```python
def ispalindrome3(s):
    """Returns: True if s is a palindrome
    Case of characters and non-letters ignored."""
    return ispalindrome2(depunct(s))

def depunct(s):
    """Returns: s with non-letters removed"""
    if s == ":
        return s
    # Combine left and right
    if s[0] in string.letters:
        return s[0]+depunct(s[1:])
    # Ignore left if it is not a letter
    return depunct(s[1:])
```

## Implicit Recursive Definitions

```python
def exp(b, c):
    """Returns: b^c
    Precondition: b a float, c ≥ 0 an int"""
```

• Not obviously a recursive definition

§ $b^{c}=b\times b\times\ldots\times b\times b$

• But remember what we did with factorial

§ We can rewrite it recursively (by regrouping)!

§ This time there is more than one way to do it

## Implicit Recursive Definitions

def exp(b, c):

"""Returns: $b^{c}$Precondition: b a float,$c \geq 0$ an int"""

**Approach 1**

$$
12^{256} = 12 \times (12^{255})
$$

$$
\mathsf {b} ^ {\mathrm{c}} = \mathsf {b} \times (\mathsf {b} ^ {\mathrm{c-1}})
$$

**Approach 2**

$$
1 2 ^ {2 5 6} = (1 2 ^ {1 2 8}) \times (1 2 ^ {1 2 8})
$$

$\mathbf{b}^{\mathrm{c}} = (\mathbf{b}\times \mathbf{b})^{\mathrm{c / 2}}$ if c even

## Raising a Number to an Exponent

```python
Approach 1
def exp(b, c):
    """Returns: b^c
    Precond: b a float, c ≥ 0 an int"""
    # b^0 is 1
    if c == 0:
        return 1
    # b^c = b(b^{c-1})
    left = b
    right = exp(b,c-1)
    return left*right

Approach 2
def exp(b, c):
    """Returns: b^c
    Precond: b a float, c ≥ 0 an int"""
    # b^0 is 1
    if c == 0:
        return 1
    # c > 0
    if c % 2 == 0:
        return exp(b*b,c//2)
    return b*exp(b*b,(c-1)//2)

10/20/26
More Recursion
34
```

## Raising a Number to an Exponent

```python
def exp(b, c):
    """Returns: b^c
    Precond: b a float, c ≥ 0 an int"""
    # b^0 is 1
    if c == 0:
        return 1

    # c > 0
    if c % 2 == 0:
        return exp(b*b,c//2)
    return b*exp(b*b,(c-1)//2)
```

| c | # of calls |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 4 | 3 |
| 8 | 4 |
| 16 | 5 |
| 32 | 6 |
| 2<sup>n</sup> | n + 1 |

32768 is 215 b<sup>32768</sup> needs only 215 calls!

## Example: Space Filling Curves

- Draw a curve that
- - Starts in the left corner
- - Ends in the right corner
- - Touches every grid point
- - Does not touch or cross
- itself anywhere
- - Useful for analysis of
- 2-dimensional data
- Starts
- Here
- Ends
- Here

## Challenge

## Hilbert’s Space Filling Curve

$$
\begin{array}{c} 2 ^ {n} \\ \hline \end{array}
$$

Hilbert(1):

Hilbert(2):

Hilbert(n):

## Hilbert’s Space Filling Curve

## Basic Idea

• Given a box

• Draw $2^{n} \times 2^{n}$ grid in box

• Trace the curve

• As n goes to ∞, curve fills box

SCS韩车车店强5 HS

## “Turtle” Graphics: Assignment A4

**Turn**

**Move**

**Draw Line**

**Change Color**
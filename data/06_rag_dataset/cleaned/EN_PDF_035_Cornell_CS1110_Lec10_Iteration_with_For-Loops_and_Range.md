Lecture 10

## Memory in Python

## Announcements For This Lecture

## Assignment 1

• Work on your revisions

§ Read feedback carefully

§ Partial credit after Friday

• Early survey results

§ 380 responded so far

§ Deadline is Friday

§ **Avg Time**: 6.6 hours

§ **STD Dev**: 3.6 hours

## More Assignments

• Assignment 2 due **Sunday**

§ Scan and submit online

§ Upload before midnight

§ **Late:** -10% per day

§ No lates after Wednesday

• Assignment 3 up **Sunday**

§ Due Fri October 9

§ Should take as long as A1

§ Graded before exam

## Speaking of the Exam

## • Prelim 1 is Oct 15<sup>th</sup> at 7:30-9:00

§ Material is up to October 1<sup>st</sup>

§ Questions come from labs or assignments

## • How do you study for it?

§ Will post a study guide this weekend

§ Can also look at old exams on web page

## • Conflict with Prelim time?

§ Amy will post a Prelim 1 Conflict form

§ Do not submit if you have no conflict

## The Three “Areas” of Memory

## Global Space

• This is the **area you “start with”**

§ First memory area you learned to visualize

§ A place to store “global variables”

§ Lasts until you quit Python

p

**id2**

• What are **global variables**?

§ **Any assignment not in a function definition**

§ Also **modules & function definitions!**

§ Will see more on this in a bit

## The Call Stack

## • The area where call frames live

§ Call frames are created on a function call

§ May be several frames (functions call functions)

§ Each frame deleted as the call completes

• Area of volatile, temporary memory

§ Less permanent than global space

§ Think of as “scratch” space

• Primary focus of Assignment 2

## Heap Space or “The Heap”

## • Where the “folders” live

§ Stores only folders

• Can only **access indirectly**

§ Must have a variable with identifier

§ Can be in global space, call stack

## • MUST have variable with id

§ If no variable has id, it is forgotten

§ Disappears in Tutor immediately

§ But not necessarily in practice

§ Role of the garbage collector

## Everything is an Object!

• Last time we saw that everything is an object

§ Must have a folder in the heap

§ Must have variable in global space, call stack

§ But ignore basic types (int, float, bool, str)

• Includes **modules** and **function definitions**!

§ Object is created by import

§ Object is created by def

§ Already seen this in Python Tutor

## Modules and Global Space

## • Importing a module:

§ Creates a global variable (same name as module)

§ Puts contents in a **folder**

• Module variables

• Module functions

§ Puts folder id in variable

## • from keyword dumps contents to global space

## import math

**Global Space**

**Heap Space**

math

id5

**id5**

**module**

3.141592

2.718281

functions

## Modules vs Objects

**Module**

math

**id2**

**id2**

math.pi math.cos(1)

**Object**

**id3**

**id3**

## Modules vs Objects

## So Why Have Both?

• Question is a matter of program design

§ Some software will use modules like objects

• Classes can have **many instances**

§ Infinitely many objects for the Point3 class

§ Reason we need a constructor function

• Each module is **a unique instance**

§ Only one possibility for pi, cosine

§ That is why we import them

§ Sometimes refer to as singleton objects

## So Why Have Both?

• Question is a matter of program design

§ Some software will use modules like objects

• Classes can have many instanc

§ Infinitely m ise is an advanced surse § Re Chornd scope of this co • ach Each nce

§ Only one possibility for pi, cosine

§ That is why we import them

§ Sometimes refer to as singleton objects

## How About import \*?

## Functions and Global Space

## • A function definition…

§ Creates a global variable (same name as function)

§ Creates a **folder** for body

§ Puts folder id in variable

## def to\_centigrade(x):

<u>Body</u>

return 5\*(x-32)/9.0

**Global Space**

to\_centigrade **id6**

## • Variable vs. Call

```python
>>> to\_centigrade
```

&lt;fun to_centigrade at 0x100498de8&gt;

```python
>>> to\_centigrade (32)
```

## Heap Space

**id6**

**function**

## Working with Function Variables

• So function definitions are **objects**

§ Function names are just variables

§ Variable refers to a folder storing the code

§ If you reassign the variable, it is lost

• You can assign them to other **variables**

§ Variable now refers to that function

§ You can use that **NEW** variable to call it

§ Just use variable in place of function name

```python
def add_one(x):
    """Returns x+1"""
    return x+1

y = add_one
z = y(2)
```

## Example: add\_one

## Example: add\_one

## ona tnge is an advanced ourse Usagod scope of this cour x2

Frame remembers <u>the original name</u>

## Why Show All This?

• Many of these are **advanced topics**

§ Only advanced programmers need

§ Will never need in the context of 1110

• But you might use them by accident

• **Goal: Teach you to read error messages**

§ Need to understand what messages say

§ Only way to debug your own code

§ This means understanding the **call stack**

```python
def to_centigrade(x):
    return 5*(x-32)/9.0
```

## Recall: Call Frames

1. Draw a frame for the call

2. Assign the argument value to the parameter (in frame)

3. Execute the function body

§ Look for variables in the frame

If not there, look for global variables with that name

4. Erase the frame for the call

## Call: to\_centigrade(50.0)

## Aside: What Happens Each Frame Step?

• The instruction counter **always** changes

• The contents only **change** if

§ You add a new variable

§ You change an existing variable

§ You delete a variable

• If a variable refers to a **mutable object**

§ The contents of the folder might change

## Recall: Call Frames

1. Draw a frame for the call

2. Assign the argument value to the parameter (in frame)

3. Execute the function body

§ <u>Look for variables in the f</u>rame

§ If not there, look for global variables with that name

4. Erase the frame for the call

**def** to\_centigrade(x):

return 5\*(x-32)/9.0

## Call: to\_centigrade(50.0)

**to\_centigrade**

x 50.0

<strong><u>What is happening here?</u></strong>

## Function Access to Global Space

• Consider code to right

§ Global variable a

§ Function definition get\_a

• Consider the call get\_a()

§ Call frame to the right

§ What happens?

A: It crashes

B: Returns None

C: Returns 4

D: I don’t know

**Global Space** (for globals.py)

a 4

**get\_a**

\# globals.py

"""Show how globals work"""

a = 4 # global space

**def** get\_a():

return a

## Function Access to Global Space

• Consider code to right

§ Global variable a

§ Function definition get\_a

• Consider the call get\_a()

§ Call frame to the right

§ What happens?

A: It crashes

B: Returns None

C: Returns 4 **CORRECT**

D: I don’t know

**Global Space** (for globals.py)

a 4

**get\_a**

\# globals.py

"""Show how globals work"""

a = 4 # global space

**def** get\_a(): return a

## Function Access to Global Space

• All function definitions are in some module

• Call can access global space for **that module**

§ math.cos: global for math

§ temperature.to\_centigrade uses global for temperature

• But **cannot** change values

§ Makes a new local variable!

§ Why we limit to constants

**Global Space** (for globals.py) a 4

\# globals.py

"""Show how globals work"""

a = 4 # global space

**def** get\_a(): return a

## Function Access to Global Space

• All function definitions are in some module

• Call can access global space for **that module**

§ math.cos: global for math

§ temperature.to\_centigrade uses global for temperature

• But **cannot** change values

§ Makes a new local variable!

§ Why we limit to constants

**Global Space** (for globals.py) a

\# globals.py

"""Show how globals work"""

a = 4 # global space

**def** change\_a():

a = 3.5 # local variable

## Frames and Helper Functions

```python
def last_name_first(s):
    """Precond: s in the form
    'first-name last-name' """
    first = first_name(s)
    last = last_name(s)
    return last + ',' + first

def first_name(s):
    """Precond: see above"""
    end = s.find(' ')
    return s[0:end]
```

## Frames and Helper Functions

```python
def last_name_first(s):
    """Precond: s in the form
    'first-name last-name' """
    first = first_name(s)
    last = last_name(s)
    return last + ',' + first

def first_name(s):
    """Precond: see above"""
    end = s.find(' ')
    return s[0:end]
```

## Frames and Helper Functions

```python
def last_name_first(s):
    """Precond: s in the form
    'first-name last-name' """
    first = first_name(s)
    last = last_name(s)
    return last + ',' + first

def first_name(s):
    """Precond: see above"""
    end = s.find(' ')
    return s[0:end]
```

## Frames and Helper Functions

```python
def last_name_first(s):
    """Precond: s in the form
    'first-name last-name' """
    first = first_name(s)
    last = last_name(s)
    return last + ',' + first

def first_name(s):
    """Precond: see above"""
    end = s.find(' ')
    return s[0:end]
```

## Frames and Helper Functions

```python
def last_name_first(s):
    """Precond: s in the form
    'first-name last-name' """
    first = first_name(s)
    last = last_name(s)
    return last + ',' + first

def first_name(s):
    """Precond: see above"""
    end = s.find(' ')
    return s[0:end]
txt
last_name_first | 5
s 'Walker White'
first 'Walker'
last_name | 15
s 'Walker White'
```

## Frames and Helper Functions

```python
def last_name_first(s):
    """Precond: s in the form
    'first-name last-name' """
    first = first_name(s)
    last = last_name(s)
    return last + ',' + first
python
def last_name(s):
    """Precond: see above"""
    end = s.rfind(' ')
    return s[end+1:]
```

## Call: last\_name\_first('Walker White'):

## The Call Stack

## • Functions are stacked

§ Cannot remove one above w/o removing one below

§ Sometimes draw bottom up (better fits the metaphor)

• Stack represents memory as a **high water mark**

§ Must have enough to keep the **entire stack in memory**

§ Error if cannot hold stack

Frame 1

Frame 2

Frame 3

Frame 4

Frame 6  5

## The Call Stack

## • Functions are stacked

§ Cannot remove one above w/o removing one below

§ Sometimes draw bottom up (better fits the metaphor)

• Stack represents memory as a **high water mark**

§ Must have enough to keep the **entire stack in memory**

§ Error if cannot hold stack

Frame 1

Frame 2

Frame 3

Frame 4

calls

## The Call Stack

## • Functions are stacked

§ Cannot remove one above w/o removing one below

§ Sometimes draw bottom up (better fits the metaphor)

• Stack represents memory as a **high water mark**

§ Must have enough to keep the **entire stack in memory**

§ Error if cannot hold stack

Frame 1

Frame 2

Frame 3

Frame 4

Frame 6

## Anglicize Example

```python
def tens(n):
    """Returns: tens-word for n

    Parameter: the integer to anglicize
    Precondition: n in 2..9"""
    if n == 2:
        return 'twenty'
    elif n == 3:
        return 'thirty'
    elif n == 4:
        return 'forty'
    elif n == 5:
        return 'fifty'
    elif n == 6:
        return 'sixty'
    elif n == 7:
        return 'seventy'
    elif n == 8:
        return 'eighty'

    return 'ninety'
txt
Frames
Objects
Global frame
    anglicize
    anglicize1000
    anglicize1to19
    anglicize20to99
    anglicize100to999
    tens
    function anglicize(n)
    function anglicize1000(n)
    function anglicize1to19(n)
    function anglicize20to99(n)
    anglicize
    n 234756
    anglicize1000
        n 756
    anglicize100to999
        n 756
    hundreds 56
    suffix ""
    anglicize20to99
        n 56
    tens
        n 5
```

## Anglicize Example
Lecture 18

## Classes

## Announcements for This Lecture

## Assignments

• **A4 Thursday** at midnight

§ Hopefully you are on Task 5

§ Will have a follow-up lab!

• Will post **A5** on Friday

§ Written assignment like A2

§ Needs material from next Tues

• Will also post **A6** Friday.

§ Not due until November 15

§ But you need to **start it first**!

## Optional Videos

• **Videos 20.1-20.8** today

• **Videos 20.9-20.10** next time

• Also **Lesson 21** next time

## Exams

• Last week for regrades

§ Limit them to valid issues

• We will do them eventually

## Recall: Objects as Data in Folders

• An object is like a **manila folder**

• It contains other variables

§ Variables are called **attributes**

Can change values of an attribute (with assignment statements)

• It has a “tab” that identifies it

§ Unique number assigned by Python

§ Fixed for lifetime of the object

Unique tab identifier

## Recall: Classes are Types for Objects

• Values must have a type

§ An **object** is a **value**

§ A **class** is its **type**

**id2**

<u>class name</u>

• Classes are how we add new types to Python

**Types**

• int

• float

• bool

• str

**Classes**

• Point3

• RGB

• Turtle

• Window

## Recall: Classes are Types for Objects

• Values must have a type

§ An **object** is a **value**

§ A **class** is its **type**

**id2**

• Classes are how we add new types to Python

**Types**

**Point3**In Python3, type and class 0 <u>class name</u> • • floatare ~~now bo~~th **synonyms**

• str

• Turtle

• Window

## Classes Have Folders Too

## Object Folders

• Separate for each instance

**Point3**

## Class Folders

• Data common to all instances

**Point3**

## The Class Definition

Goes inside a module, just like a function definition.

## class &lt;class-name&gt;(object):

"""Class specification"""

&lt;function definitions&gt;

&lt;assignment statements&gt;

&lt;any other statements also allowed&gt;

```python
class Example(object):
    """The simplest possible class."""
    pass
```

## Example

keyword class Beginning of a <u>class definition</u>

Specification (similar to one <u>for a function)</u>

to define **methods**

to define **attributes**

## The Class Definition

class

(object):

Goes inside a module, just like a function definition.

"""Class specification"""

Do not forget the colon!

&lt;function definitions&gt;

more on this later

&lt;assignment statements&gt;

…but not often used

&lt;any other statements also allowed&gt;

**class** Example(object): """The simplest possible class." pass

## Example

Python creates after reading the class definition

## Recall: Constructors

• Function to create new instances

§ Function name == class name

§ Created for you automatically

• Calling the constructor:

§ Makes a new object folder

§ Initializes attributes

§ Returns the id of the folder

Will come

back to this

• By default, takes no arguments

§ e = Example()

**id2**

e

**id2**

**Example**

**Example**

## Instances and Attributes

• Assignments add object attributes

§ &lt;object&gt;.&lt;att&gt; = &lt;expression&gt;

§ **Example**: e.b = 42

• Assignments can add class attributes

§ &lt;class&gt;.&lt;att&gt; = &lt;expression&gt;

§ **Example**: Example.a = 29

• Objects can access class attributes

§ **Example**: print(e.a)

§ But assigning it creates object attribute

§ **Example**: e.a = 10

• **Rule**: check object first, then class

**id2**

**id2**

**Example**

b

42

**Example**

a

29

## Instances and Attributes

• Assignments add object attributes

§ &lt;object&gt;.&lt;att&gt; = &lt;expression&gt;

§ **Example**: e.b = 42

Not how usually done

• Assignments can add c~~lass attribute~~s

§ &lt;class&gt;.&lt;att&gt; = &lt;expression&gt;

§ **Example**: Example.a = 29

• Objects can access class attributes

§ **Example**: print(e.a)

§ But assigning it creates object attribute

§ **Example**: e.a = 10

• **Rule**: check object first, then class

e

**id2**

**id2**

**Example**

b

42

**Example**

a

29

## Instances and Attributes

• Assignments add object attributes

§ &lt;object&gt;.&lt;att&gt; = &lt;expression&gt;

§ **Example**: e.b = 42

• Assignments can add class attributes

§ &lt;class&gt;.&lt;att&gt; = &lt;expression&gt;

§ **Example**: Example.a = 29

• Objects can access class attributes

§ **Example**: print(e.a)

§ But assign<u>ing it cre</u>ates object attribute

**Example**: <u>e.a = 10</u>

• **Rule**: check object first, then class

## Invariants

• Properties of an attribute that must be true

• Works like a precondition:

§ If invariant satisfied, object works properly

§ If not satisfied, object is “corrupted”

## • Examples:

§ Point3 class: all attributes must be floats

§ RGB class: all attributes must be ints in 0..255

• Purpose of the **class specification**

## The Class Specification

class Worker(object):

"""A class representing a worker in a certain organization

Instance has basic worker info, but no salary information.

Attribute lname: The worker last name

Invariant: lname is a string

Attribute ssn: The Social Security number

Invariant: ssn is an int in the range 0..999999999

Attribute boss: The worker's boss

Invariant: boss is an instace of Worker, or None if no boss"""

## The Class Specification

class Worker(object):

"""A class representing a worker in a certain organization

Instance has basic worker info, but no salary information.

Attribute lname: The worker last name

Description

Invariant: lname is a string

Invariant

Attribute ssn: The Social Security number

Invariant: ssn is an int in the range 0..999999999

Attribute boss: The worker's boss

Invariant: boss is an instace of Worker, or None if no boss"""

Short <u>summary</u>

More detail

## Recall: Objects can have Methods

• Object before the name is an implicit argument

• **Example**: distance

```txt
>>> p = Point3(0,0,0)
txt
>>> q = Point3(1,0,0)
txt
>>> r = Point3(0,0,1)
txt
>>> p.distance(r)
txt
1.0
txt
>>> q.distance(r)
```

1.4142135623730951

\# First point

\# Second point

\# Third point

\# Distance between p, r

\# Distance between q, r

## Method Definitions

## • Looks like a function def

§ Indented inside class

§ First param is always self

§ But otherwise the same

## • In a method call:

§ One less argument in ()

§ Obj in front goes to self

• **Example**: a.distance(b)

```python
class Point3(object):
    """Class for points in 3d space
    Invariant: x is a float
    Invariant y is a float
    Invariant z is a float    """
    def distance(self,q):
        """Returns dist from self to q
        Precondition: q a Point3"""
        assert type(q) == Point3
        sqrdst = ((self.x-q.x)**2 +
                (self.y-q.y)**2 +
                (self.z-q.z)**2)
        return math.sqrt(sqrdst)
```

## Methods Calls

• <strong><u>Exampl</u></strong>**e**: a.dist<u>ance(b)</u>

a

**id2**

b

**id3**

**id2**

**id3**

$$
\mathrm{x} \quad \boxed {1. 0}
$$

**Point3**

**Point3**

$$
\mathrm{y} \quad \boxed {2. 0}
$$

$$
\mathrm{z} \quad \boxed {3. 0}
$$

```python
class Point3(object):

    """Class for points in 3d space

    Invariant: x is a float

    Invariant y is a float

    Invariant z is a float    """

    def distance(self,q):

        """Returns dist from self to q
        Precondition: q a Point3"""
        assert type(q) == Point3
        sqrdst = ((self.x-q.x)**2 +
                (self.y-q.y)**2 +
                (self.z-q.z)**2)
        return math.sqrt(sqrdst)
```

## Methods Calls

• <strong><u>Exampl</u></strong>**e**: a.dist<u>ance(b)</u>

b

**id3**

**Point3**

**Point3**

**Point3.distance**

**id2**

```python
class Point3(object):

    """Class for points in 3d space

    Invariant: x is a float

    Invariant y is a float

    Invariant z is a float    """

    def distance(self,q):

        """Returns dist from self to q
        Precondition: q a Point3"""
        assert type(q) == Point3
        sqrdst = ((self.x-q.x)**2 +
                (self.y-q.y)**2 +
                (self.z-q.z)**2)
        return math.sqrt(sqrtst)
```

## Methods and Folders

• Function definitions…

§ make a folder in heap

§ assign name as variable

§ variable in global space

• Methods are similar...

§ Variable in **class folder**

§ But otherwise the same

## • Rule of this course

§ Put header in class folder

§ Nothing else!

1. class Point3(object):

"""Class for points in 3d space

3. Invariant: x is a float

4. Invariant y is a float

5. Invariant z is a float """

6. def **distance**(self,q):

**Point3**

distance(self,q)

## Methods and Folders

```python
class Point3(object):
    """Class for points in 3d space
    Invariant: x is a float
    Invariant y is a float
    Invariant z is a float    """
    def distance(self,q):
        """Returns: dist from self to q
        Precondition: q a Point3"""
        assert type(q) == Point3
        sqrdst = ((self.x-q.x)**2 +
                          (self.y-q.y)**2 +
                          (self.z-q.z)**2)
        return math.sqrt(sqrdst)
```

## Initializing the Attributes of an Object (Folder)

• Creating a new Worker is a <u>multi-step process:</u>

§ w = Worker()

Instance is empty

§ w.lname = 'White'

§

• Want to use something like

w = Worker('White', 1234, None)

§ Create a new Worker **and** assign attributes

§ lname to 'White', ssn to 1234, and boss to None

• Need a **custom constructor**

## Special Method: \_\_init

```python
w = Worker('White', 1234, None)
python
def __init__(self, n, s, b):
    """Initializes a Worker object

    Has last name n, SSN s, and boss b

    Precondition: n a string,
    s an int in range 0..999999999,
    b either a Worker or None.  """

    self.lname = n
    self.ssn = s
    self.boss = b
```

Called by the constructor

## id8

**Worker**

lname

'White'

ssn

1234

boss

None

## Special Method: \_\_init

```python
two underscores
w - worker( with n, 1234, None)
don't forget self

def __init__(self, n, s, b):
    """Initializes a Worker object
    Has last name n, SSN s, and boss b
    Precondition: n a string,
    s an int in range 0..999999999,
    b either a Worker or None.  """
    self.lname = n
    self.ssn = s
    self.boss = b

use self to assign attributes
```

Called by the constructor

## id8

## Evaluating a Constructor Expression

## Worker('White', 1234, None)

1. Creates a new object (folder) of the class Worker

§ Instance is initially empty

2. Puts the folder into heap space

3. Executes the method \_\_init\_\_

§ Passes folder name to self

§ Passes other arguments in order

Executes the (assignment) commands in initializer body

4. Returns the object (folder) name

**id8**

lname

**Worker**

ssn

'White'

1234

boss

None

## Aside: The Value None

• The boss field is a problem.

§ boss refers to a Worker object

§ Some workers have no boss

Or maybe not assigned yet (the buck stops there)

• **Solution**: use value None

§ **None**: Lack of (folder) name

§ Will reassign the field later!

• Be careful with None values

§ var3.x gives error!

§ There is no name in var3

§ Which Point3 to use?

## A Class Definition

```python
class Example(object):
>>> a = Example(3)
12 def __init__(self,x):
13 | self.x = x
14
15 def foo(self,y):
16 | x = self.bar(y+1)
17 | return x
18
19 def bar(self,y):
20 | self.x = y-1
21 | return self.x
10/27/26
Classes
```

## Which One is Closest to Your Answer?

<strong><u>Example</u></strong>

## A Class Definition

```python
class Example(object):
    def __init__(self,x):
        self.x = x
    def foo(self,y):
        x = self.bar(y+1)
        return x
    def bar(self,y):
        self.x = y-1
        return self.x
```

## Which One is Closest to Your Answer?

A:

**id1**

Ex.\_\_init

B:

13

**id1**

13

Ex.\_\_init

x

<strong><u>Example</u></strong>

3

self

id1

x

3

D:

<strong><u>Example</u></strong>

self

id1

x

3

**id1**

<strong><u>Example</u></strong>

x

3

Ex.

x

13

3

**id1**

<strong><u>Example</u></strong>

x

13

3

## A Class Definition

```python
class Example(object):
    def __init__(self,x):
        self.x = x
    def foo(self,y):
        x = self.bar(y+1)
        return x
    def bar(self,y):
        self.x = y-1
        return self.x
```

## Making Arguments Optional

• We can assign default values to \_\_init\_\_ arguments

Write as assignments to parameters in definition

§ Parameters with default values are optional

• **Examples**:

p = Point3()

§ p = Point3(1,2,3) # (1,2,3)

§ p = Point3(1,2) # (1,2,0) 11.

§ p = Point3(y=3) # (0,3,0) 12.

§ p = Point3(1,z=2) # (1,0,2) 13.

1. class Point3(object):

"""Class for points in 3d space

4.

Invariant: x is a float

5.

Invariant y is a float

6.

Invariant z is a float """

def \_\_init\_\_(self,x=0,y=0,z=0): """Initializes a new Point3 Precond: x,y,z are numbers""" self.x = x self.y = y self.z = z

## Making Arguments Optional

• We can assign default values to \_\_init\_\_ arguments

§ Write as assignments to parameters in definition

§ Parameters with default values are optional

• **Examples**:

§ p = Point3(1

Assigns in order

§ p = Point3(1,2)

§ p = Point3(y=3)

§ p = Point3(1,z=2)

\# (1,2,0)Use parameter name

when out of order

(1,0,2)Can mix two approaches

2.

3.

4.

1. class Point3(object):

5.

6.

7.

8.

9.

10.

"""Class for points in 3d space

Invariant: x is a float

Invariant y is a float

Invariant z is a float """

def \_\_init\_\_(self,x=0,y=0,z=0):

"""Initializes a new Point3

Precond: x,y,z are numbers"""

self.x = x

self.y = y

self.z = z

## Making Arguments Optional

• We can assign default values to \_\_init\_\_ arguments

§ Write as assignments to parameters in definition

§ Parameters with default values are optional

1. class Point3(object):

"""Class for points in 3d space

3. Invariant: x is a float

4. Invariant y is a float

5. Invariant z is a float """

## • Examples:

§ p = Point3()

§ p = Point3(1

§ p = Point3(1,2)

§ p = Point3(y=3)

§ p = Point3(1,z=2)

\# (0,0,0)

Assigns in order

8. 9. 10.

\# (1,2,0)Use parameter name

when out of order

(1,0,2)Can mix two approaches

def \_\_init\_\_(self,x=0,y=0,z=0):

"""Initializes a

Precond: x,y,z are numbers self.x = x

elf.z = z
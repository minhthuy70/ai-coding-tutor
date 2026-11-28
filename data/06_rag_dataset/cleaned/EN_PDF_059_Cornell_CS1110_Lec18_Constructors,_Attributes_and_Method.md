## Recall: Objects as Data in Folders

• An object is like a **manila folder**

• It contains other variables

§ Variables are called **attributes**

§ Can change values of an attribute (with assignment statements)

• It has a “tab” that identifies it

§ Unique number assigned by Python

§ Fixed for lifetime of the object

## Name Resolution for Objects

• ⟨object⟩.⟨name⟩ means

§ Go the folder for object

§ Find attribute/method name

§ If missing, check **class folder**

§ If not in either, raise error

• What is in the class folder?

§ Data common to **all** objects

§ First must understand the **class definition**

## Instances and Attributes

• Assignments add object attributes

§ &lt;object&gt;.&lt;att&gt; = &lt;expression&gt;

§ **Example**: Example.a = 29

§ **Example**: e.b = 42

• Assignments can add class attributes § &lt;class&gt;.&lt;att&gt; = &lt;expression&gt;

• Objects can access class attributes § **Example**: print e.a

§ But assign<u>ing it cre</u>ates object attribute

## Classes Have Folders Too

§ **Example**: <u>e.a = 10</u>

• **Rule**: check object first, then class

## The Class Specification

"""A class representing a worker in a certain organization Short <u>summary</u>

Instance has basic worker info, but no salary information.

Attribute ssn: The Social Security number Invariant: ssn is an int in the range 0..999999999

Attribute boss: The worker's boss Invariant: boss is an instace of Worker, or None if no boss"""

## Method Definitions

• Looks like a function def

class Point3(object):

§ Indented inside class

"""Class for points in 3d space

Invariant: x is a float

§ First param is always self

Invariant y is a float

§ But otherwise the same

Invariant z is a float """

• In a **method call**:

def **distance**(self,q):

§ One less argument in ()

"""Returns dist from self to q

§ Obj in front goes to self

Precondition: q a Point3"""

• **Example**: a.distance(b)

assert type(q) == Point3

sqrdst = ((self.x-q.x)\*\*2 +

return math.sqrt(sqrdst)

1. class Point3(object):

2. """Class for points in 3d space

3. Invariant: x is a float

## Methods and Folders

• Function definitions…

4. Invariant y is a float

§ make a folder in heap

## Methods Calls

§ assign name as variable

5. Invariant z is a float """

"""Returns dist from self to q

§ variable in global space

• <strong><u>Exampl</u></strong>**e**: a.dist<u>ance(b)</u>

assert type(q) == Point3

6. def **distance**(self,q):

return math.sqrt(sqrdst)

• Methods are similar...

**Point3**

**id3**

§ Variable in **class folder**

§ But otherwise the same

def **distance**(self,q):

• **Rule of this course**

distance(self,q)

§ Put header in class folder

class Point3(object):

§ Nothing else!

"""Class for points in 3d space

Invariant: x is a float

Invariant z is a float """

Invariant y is a float

## Special Method: \_\_init

two underscores w Worker('Whi 1234, None) don’t forget self

**def** \_\_init\_\_(self, n, s, b):

Called by the constructor

"""Initializes a Worker object

**id8**

Has last name n, SSN s, and boss b

**Worker**

lname 'White'

boss None

use self to assign attributes

## Evaluating a Constructor Expression

## Worker('White', 1234, None)

1. Creates a new object (folder) of the class Worker

§ Instance is initially empty

**id8**

2. Puts the folder into heap space

**Worker**

3. Executes the method \_\_init\_

lname 'White'

§ Passes folder name to self

ssn 1234

§ Passes other arguments in order

§ Executes the (assignment) commands in initializer body

bossNone

4. Returns the object (folder) name

## Making Arguments Optional

• We can assign default values to \_\_init\_\_ arguments

§ Write as assignments to parameters in definition

§ Parameters with default values are optional

## • Examples:

§ p = Point3() # (0,0,0)

## 1. class Point3(object):

§ p = Point3(1,2,3) # (1,2,3)

"""Class for points in 3d space

Invariant: x is a float

def \_\_init\_\_(self,x=0,y=0,z=0):

§ p = Point3(1,2)

Invariant y is a float

Invariant z is a float

"""Initializes a new Point3

Precond: x,y,z are numbers"""

§ p = Point3(y=3) # (0,3,0)

§ p = Point3(1,z=2) # (1,0,2)

self.x = x

self.y = y

self.z = z
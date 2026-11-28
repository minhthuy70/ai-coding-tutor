Lecture 12

## Lists (& Sequences)

## Announcements for Today

## (Optional) Videos

• **Videos 15.1-15.7** for today

• **Videos 16.1-16.7** next time

• **Prelim, 10/15 at 7:30 pm**

Material up to **Today**

§ Study guide is posted

• **Conflict with Prelim time?**

§ Submit the form from Corey

§ She wants to close this Tues

§ Will talk about SDS next week

## Assignments

• A2 still not graded

§ Grade posted Sunday

§ Survey still open

§ Quiz in lab Thur/Fri

• A3 due next **Friday**

§ Will grade over break

§ Check in on Tues/Wed

§ Quiz **after** Prelim 1

## Sequences: Lists of Values

## String

• s = 'abc d'

| 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |

| a | b | c |  | d |
| --- | --- | --- | --- | --- |

• Put characters in quotes

§ Use \' for quote character

• Access characters with []

§ s[0] is 'a'

s[5] causes an error

§ s[0:2] is 'ab' (excludes c)

§ s[2:] is 'c d'

## List

• x = [5, 6, 5, 9, 15, 23]

| 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |

| 5 | 6 | 5 | 9 | 15 | 23 |
| --- | --- | --- | --- | --- | --- |

• Put values inside [ ]

§ Separate by commas

• Access **values** with []

§ x[0] is 5

§ x[6] causes an error

§ x[0:2] is [5, 6] (excludes $2^{\mathrm{nd}}$ 5)

§ x[3:] is [9, 15, 23]

## Sequences: Lists of Values

## String

• s = 'abc d'

| 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |

| a | b | c |  | d |
| --- | --- | --- | --- | --- |

• Put characters in quotes

§ Use \' for quote character

• Access cha § s[0] is 'a'

§ s[5] causes

## List

§ s[0:2] is 'ab' (excludes c)

§ s[2:] is 'c d'

0 $\mathbf{x} = [5, 6, 5, 9, 15, 23]$

| 5 | 6 | 5 | 9 | 15 | 23 |
| --- | --- | --- | --- | --- | --- |

0 1 2 3 45

• Put values inside [ ]

## racters with []• Access value

mmas

§ x[6] causes an error

§ x[0:2] is [5, 6] (excludes $2^{\mathrm{nd}}$ 5)

§ x[3:] is [9, 15, 23]

## Lists Have Methods Similar to String

## x = [5, 6, 5, 9, 15, 23]

## • index(value)

§ Return position of the value

§ **ERROR** if value is not there

§ x.index(9) evaluates to 3

But you get length of a list with a regular function, not method:

len(x)

## • count(value)

§ Returns number of times value appears in list

§ x.count(5) evaluates to 2

## Representing Lists

Box is “too small” to hold the list

Unique tab identifier

$$
\mathbf {x} = [ 5, 7, 4, - 2 ]
$$

## Lists vs. Class Objects

## List

• Attributes are indexed

§ Example: x[2]

## RGB

Attributes are named Example: c.red c **id3** id3 RGB red 128 green 64 blue 255

## When Do We Need to Draw a Folder?

• When the value **contains** other values

§ This is essentially want we mean by ‘object’

• When the value is **mutable**

| Type | Container? | Mutable? |
| --- | --- | --- |
| int | No | No |
| float | No | No |
| str | Yes* | No |
| Point3 | Yes | Yes |
| RGB | Yes | Yes |
| list | Yes | Yes |

## Lists are Mutable

## • List assignment:

&lt;var&gt;[&lt;index&gt;] = &lt;value&gt;

§ Reassign at index

§ Affects folder contents

§ Variable is unchanged

• Strings cannot do this

§ s = 'Hello World!'

s[0] = 'J' **ERROR**

§ String are **immutable**

• $\mathrm{x} = [5, 7, 4, -2]$

$$
\begin{array}{c c c c} 0 & 1 & 2 & 3 \end{array}
$$

| 5 | 7 | 4 | -2 |
| --- | --- | --- | --- |

x[1] = 8

**id1**

**id1**

$$
\begin{array}{c c} \hline 0 & 5 \\ \hline 1 & 7 \\ \hline 2 & 4 \\ \hline 3 & - 2 \\ \hline \end{array}
$$

## Lists are Mutable

## • List assignment:

&lt;var&gt;[&lt;index&gt;] = &lt;value&gt;

§ Reassign at index

§ Affects folder contents

§ Variable is unchanged

• Strings cannot do this

§ s = 'Hello World!'

s[0] = 'J' **ERROR**

§ String are **immutable**

• x = [5, 7, 4, -2]

• x[1] = 8

**id1**

**id1**

$$
\begin{array}{c c} \hline 0 & 5 \\ \hline 1 & \times 8 \\ \hline 2 & 4 \\ \hline 3 & - 2 \\ \hline \end{array}
$$

## Slice Assignment

• Can embed a new list inside of a list

§ **Syntax:** &lt;var&gt;[&lt;start&gt;:&lt;end&gt;] = &lt;list&gt;

§ Replaces that range with content of list

• **Example:**

$$
> > > a = [ 1, 2, 3 ]
$$

$$
> > > b = [ 4, 5 ]
$$

$$
> > > a [: 2 ] = b
$$

$$
> > > > a
$$

[4, 5, 3]

Replaces [1,2] with [4,5]

## List Methods Can Alter the List

$$
\mathbf {x} = [ 5, 6, 5, 9 ]
$$

## • append(value)

§ A **procedure method**, not a fruitful method

§ Adds a new value to the end of list

§ x.append(-1) changes the list to [5, 6, 5, 9, -1]

## • insert(index, value)

§ Put the value into list at index; shift rest of list right

§ x.insert(2,-1) changes the list to [5, 6, -1, 5, 9,]

## • sort()

## List Methods Can Alter the List

$$
\mathbf {x} = [ 5, 6, 5, 9 ]
$$

## • append(value)

§ A **procedure method**, not a fruitful method

§ Adds a new value to the end of list

§ x.append(-1) changes the list to [5, 6, 5, 9, -1]

## • insert(index, value)

§ Put the value into list at index; shift rest of list right

§ x.inser<u>t(2,-1) changes the list to [5, 6, -1,</u> 5, 9,]

• sort()

What do you think this does?

# Where To Learn About List Methods?

## 5.1. More on Lists

The list data type has some more methods. Here are all of the methods of list objects:

## list.append(x)

Add an item to the end of the list. Equivalent toa[len(a) :] = [x]

## 1ist.extend(iterable)

Extend the list by appending all the items from the

## In the documentation!

## 1ist.insert(i, x)

Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, anda.insert(len(a), x)is equivalent to a.append(x).

## 1ist.remove(x)

Remove the first item from the list whose value is equal to x. It raises a valueError if there is no such item.

## list.pop([])

Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the iin the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

## Lists and Functions: Swap

1. def swap(b, h, k):

""" Swaps b[h] and b[k] in b

3. **Precond**: b is a mutable list,

4. h, k are valid positions"""

```txt
5. temp = b[h]
```

6. b[h]= b[k]

$$
\mathrm{b[k]=temp}
$$

**swap**

**id4**

swap(x, 3, 4)

$$
\begin{array}{c c} \hline \text {h} & 3 \\ \hline \end{array}
$$

$$
k \boxed {4}
$$

Swaps b[h] and b[k], because parameter b contains name of list.

**id4**

$$
\begin{array}{c c} \hline 0 & 5 \\ \hline 1 & 4 \\ \hline 2 & 7 \\ \hline 3 & 6 \\ \hline 4 & 5 \\ \hline \end{array}
$$

x

**id4**

## Lists and Functions: Swap

1. def swap(b, h, k):

2.

""" Swaps b[h] and b[k] in b

3. **Precond**: b is a mutable list,

4. h, k are valid positions"""

5. temp= b[h]

6. b[h]= b[k]

$$
\mathrm{b[k]=temp}
$$

**swap**

**id4**

temp

6

swap(x, 3, 4)

h

6

$$
\boxed {3}
$$

$$
k \boxed {4}
$$

Swaps b[h] and b[k], because parameter b contains name of list.

**id4**

$$
\begin{array}{c c} \hline 0 & 5 \\ \hline 1 & 4 \\ \hline 2 & 7 \\ \hline 3 & 6 \\ \hline 4 & 5 \\ \hline \end{array}
$$

x

**id4**

## Lists and Functions: Swap

1. def swap(b, h, k):

""" Swaps b[h] and b[k] in b

3. **Precond**: b is a mutable list,

4. h, k are valid positions"""

```txt
5. temp = b[h]
```

6. b[h]= b[k]

$$
\mathrm{b[k]=temp}
$$

**swap**

swap(x, 3, 4)

**id4**

temp

6

$$
7
$$

h

$$
\boxed {3}
$$

$$
k \boxed {4}
$$

Swaps b[h] and b[k], because parameter b contains name of list.

**id4**

$$
\begin{array}{c c} \hline 0 & 5 \\ \hline 1 & 4 \\ \hline 2 & 7 \\ \hline 3 & 6 \quad 5 \\ \hline 4 & 5 \\ \hline \end{array}
$$

x

**id4**

## Lists and Functions: Swap

1. def swap(b, h, k):

""" Swaps b[h] and b[k] in b

3. **Precond**: b is a mutable list,

4. h, k are valid positions"""

```txt
5. temp = b[h]
```

6. b[h]= b[k]

$$
\mathrm{b[k]=temp}
$$

**swap**

**id4**

swap(x, 3, 4)

temp

h

6

3

$$
\mathrm{k} \boxed {4}
$$

Swaps b[h] and b[k], because parameter b contains name of list.

**id4**

$$
\begin{array}{c c} \hline 0 & 5 \\ \hline 1 & 4 \\ \hline 2 & 7 \\ \hline 3 & 6 \quad 5 \\ \hline 4 & 5 \quad 6 \\ \hline \end{array}
$$

x

**id4**

## List Slices Make Copies

$$
\mathbf {x} = [ 5, 6, 5, 9 ]
$$

$$
\mathrm{y} = \mathrm{x} [ 1: 3 ]
$$

X

**id5**

y

**id6**

**id5**

**list**

**id6**

$$
\begin{array}{c c} \hline 0 & 5 \\ \hline 1 & 6 \\ \hline 2 & 5 \\ \hline 3 & 9 \\ \hline \end{array}
$$

**list**

$$
\begin{array}{c c} 0 & \framebox {6} \\ \hline 1 & \framebox {5} \end{array}
$$

<u>copy = new folder</u>

## Exercise Time

• Execute the following:

$$
> > > \mathrm{x} = [ 5, 6, 5, 9, 1 0 ]
$$

$$
\ggg \mathrm{x} [ 3 ] = - 1
$$

• What is x[4]?

```yaml
A: 10
B: 9
C: -1
D: ERROR
E: I don't know
```

## Exercise Time

• Execute the following:

$$
> > > \mathrm{x} = [ 5, 6, 5, 9, 1 0 ]
$$

$$
\ggg \mathrm{x} [ 3 ] = - 1
$$

```python
>>> x.insert(1,2)
```

• What is x[4]?

$$
- 1
$$

• Execute the following:

$$
> > > \mathrm{x} = [ 5, 6, 5, 9, 1 0 ]
$$

$$
> > > \mathbf {y} = \mathbf {x} [ 1: ]
$$

$$
> > > \mathbf {y} [ 0 ] = 7
$$

• What is x[1]?

$$
\begin{array}{l} \text {A: 7} \\ \text {B: 5} \\ \text {C: 6} \end{array}
$$

D: **ERROR**

E: I don’t know

## Exercise Time

• Execute the following:

$$
> > > \mathrm{x} = [ 5, 6, 5, 9, 1 0 ]
$$

$$
\ggg \mathrm{x} [ 3 ] = - 1
$$

```python
>>> x.insert(1,2)
```

• What is x[4]?

$$
- 1
$$

• Execute the following:

$$
> > > \mathrm{x} = [ 5, 6, 5, 9, 1 0 ]
$$

$$
> > > \mathrm{y} = \mathrm{x} [ 1: ]
$$

$$
> > > \mathbf {y} [ 0 ] = 7
$$

• What is x[1]?

$$
\boxed {6}
$$

```txt
A: 'a+b'
B: 12
C: 57
D: ERROR
E: I don't know
```

## Lists and Expressions

• List brackets [] can contain expressions

• This is a list **expression**

§ Python must evaluate it

§ Evaluates each expression

§ Puts the value in the list

• Example:

$$
> > > a = [ 1 + 2, 3 + 4, 5 + 6 ]
$$

$$
> > > > \mathrm{a}
$$

$$
[ 3, 7, 1 1 ]
$$

• Execute the following:

$$
> > > a = 5
$$

$$
> > > b = 7
$$

$$
\ggg x = [ a, b, a + b ]
$$

• What is x[2]?

## Lists and Expressions

• List brackets [] can contain expressions

• This is a list **expression**

§ Python must evaluate it

§ Evaluates each expression

§ Puts the value in the list

• Example:

$$
> > > a = [ 1 + 2, 3 + 4, 5 + 6 ]
$$

$$
> > > > \text {a}
$$

$$
[ 3, 7, 1 1 ]
$$

• Execute the following:

$$
> > > > \mathsf {a} = 5
$$

$$
> > > b = 7
$$

$$
> > > \mathrm{x} = [ \mathrm{a}, \mathrm{b}, \mathrm{a} + \mathrm{b} ]
$$

• What is x[2]?

$$
\boxed {1 2}
$$

## Lists of Objects

• List positions are variables

§ Can store base types

§ But cannot store folders

§ Can store folder identifiers

• Folders linking to folders

§ Top folder for the list

§ Other folders for contents

• Example:

$$
> > > \mathrm{r} = \text {introcs.RGB(255,0,0)}
$$

$$
> > > g = \text {introcs.RGB} (0, 2 5 5, 0)
$$

$$
> > > b = \text {introcs.RGB} (0, 0, 2 5 5)
$$

$$
> > > \mathrm{x} = [ \mathrm{r}, \mathrm{g}, \mathrm{b} ]
$$

r

**id10**

**id11**

g

**id12**

x

**id13**

**id10**

**RGB**

red

**id11**

green

255

0

blue

0

<strong><u>id12</u></strong>

green

**list**

red

blue

0

**id13**

**id11**

<strong><u>id10</u></strong>

2

1

**RGB**

**id12**

**RGB**

0

red

0

0

255

green

0

blue

255

## Lists of Objects

• List positions are variables

§ Can store base types

§ But cannot store folders

§ Can store folder identifiers

• Folders linking to folders

§ Top folder for the list

§ Other folders for contents

• Example:

$$
> > > \mathrm{r} = \text {introcs.RGB(255,0,0)}
$$

$$
> > > g = \text {introcs.RGB} (0, 2 5 5, 0)
$$

$$
> > > b = \text {introcs.RGB} (0, 0, 2 5 5)
$$

$$
> > > \mathrm{x} = [ \mathrm{r}, \mathrm{g}, \mathrm{b} ]
$$
## ENTHOUGHT

## Introduction to Numerical Computing with Numpy

© 2001-2019, Enthought, Inc.

All Rights Reserved. Use only permitted under license. Copying, sharing, redistributing or other unauthorized use strictly prohibited.

All trademarks and registered trademarks are the property of their respective owners.

Enthought, Inc.

200 W Cesar Chavez

Suite 202

Austin, TX 78701

www.enthought.com

Q2-2019

letter

# Introduction to Numerical Computing with Numpy

Enthought, Inc.
www.enthought.com

## Introduction 1

NumPy 2
An interlude: Matplotlib basics 4
Introducing NumPy Arrays 17
Multi-Dimensional Arrays 21
Slicing/Indexing Arrays 22
Fancy Indexing 28
Creating arrays 32
Array Creation Functions 34
Array Calculation Methods 37
Array Broadcasting 45
Universal Function Methods 53
The array data structure 59

## Hi there!

## Matplotlib's "State Machine"

## Matplotlib behaves like a state machine. Any command is applied to the current plotting area:

```python
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> t = np.linspace(0,2*np.pi,
...                          50)
>>> x = np.sin(t)
>>> y = np.cos(t)

# Now create a figure
>>> plt.figure()
# and plot x inside it
>>> plt.plot(x)

# Now create a new figure
>>> plt.figure()
# and plot y inside it...
>>> plt.plot(y)
# ...and add a title
>>> plt.title("Cos")

© 2008-2018 Enthought, Inc.
```

## Line Plots

```python
>>> x = np.linspace(0, 2*np.pi, 50)
>>> y1 = np.sin(x)
>>> y2 = np.sin(2*x)

>>> plt.figure() # Create figure
>>> plt.plot(y1)
>>> plt.plot(x, y1)

# red dot-dash circle
>>> plt.plot(x, y1, 'r-o')

# red marker only circle
>>> plt.plot(x, y1, 'ro')

# clear figure then plot 2 curves
>>> plt.slf()
>>> plt.plot(x, y1, 'g-o',
...             x, y2, 'b-+')
>>> plt.legend(['sin(x)',
...                       'sin(2x)'])

© 2008-2018 Enthought, Inc.
```

| Symbol | Color |
| --- | --- |
| b | Blue |
| g | Green |
| r | Red |
| c | Cyan |
| m | Magenta |
| y | Yellow |
| k | Black |
| w | White |

| Symbol | Marker |
| --- | --- |
| . | Point |
| o | Circle |
| &lt; > ^ v | Triangles |
| 8 | Octagon |
| s | Square |
| * | Star |
| + | Plus |
|  | ...and more |

## Scatter Plots

```python
>>> N = 50 # no. of points
>>> x = np.linspace(0, 10, N)
>>> from numpy.random \
...     import rand
>>> e = rand(N)*5.0 # noise
>>> y1 = x + e

>>> areas = rand(N)*300
>>> plt.scatter(x, y1, s=areas)
>>> colors = rand(N)
>>> plt.scatter(x, y1, s=areas,
...             c=colors)
>>> plt.colorbar()
>>> plt.title("Random scatter")
```

```python
>>> # Create some data
>>> e1 = rand(100)
>>> e2 = rand(100)*2
>>> e3 = rand(100)*10
>>> e4 = rand(100)*100
>>> corrmatrix = \
...     np.corrcoef([e1, e2,
...                             e3, e4])

>>> # Plot corr matrix as image
>>> plt.imshow(corrmatrix,
...       cmap='GnBu')
>>> plt.colorbar()
```

Multiple Plots Using subplot

## Legends, Titles, and Axis Labels

## LEGEND LABELS WITH PLOT

```python
# Add labels in plot command.
>>> plt.plot(np.sin(t),
...         label='sin')
>>> plt.plot(np.cos(t),
...         label='cos')
>>> plt.legend()
```

## TITLES AND AXIS LABELS

```python
>>> plt.plot(t, np.sin(t))
>>> plt.xlabel('radians')
# Keywords set text properties.
>>> plt.ylabel('amplitude',
...          fontsize='large')
>>> plt.title('Sin(x)')
```

## MPL Exercise: Desired Output

## Other Visualization Libraries

Seaborn: Better looking, high-level plots based on matplotlib

bokeh: D3-like visualization in web browsers (HTML file, or inline in IPython notebooks)

plot.ly: D3-based visualization with support for multiple languages (R, Python, Matlab, Julia and more.)

chaco: For interactive, custom plots embedded in user applications

mayavi: 3D visualization, based on VTK

## Introducing NumPy Arrays

## SIMPLE ARRAY CREATION

```python
>>> a = np.array([0, 1, 2, 3])
>>> a
array([0, 1, 2, 3])
```

## CHECKING THE TYPE

```python
>>> type(a)
numpy.ndarray
```

## NUMERIC "TYPE" OF ELEMENTS

```python
>>> a.dtype
dtype('int32')
```

## NUMBER OF DIMENSIONS

```python
>>> a.ndim
1
```

## ARRAY SHAPE

\# Shape returns a tuple
# listing the length of the
# array along each dimension.

```python
>>> a.shape
(4,)
```

## BYTES PER ELEMENT

## >>> a.itemsize

4

## BYTES OF MEMORY USED

\# Return the number of bytes

\# used by the data portion of

\# the array.

```python
>>> a.nbytes
16
```

## Setting Array Elements

## ARRAY INDEXING

```python
>>> a[0]
```

```python
>>> a[0] = 10
```

```python
>>> a
```

array([10, 1, 2, 3])

## BEWARE OF TYPE COERCION

## >>> a.dtype

dtype('int32')

\# assigning a float into

\# an int32 array truncates

\# the decimal part

```python
>>> a[0] = 10.6
```

```python
>>> a
```

array([10, 1, 2, 3])

\# fill has the same behavior

```python
>>> a.fill(-4.8)
```

```python
>>> a
```

array([-4, -4, -4, -4])

# Multi-Dimensional Arrays

## MULTI-DIMENSIONAL ARRAYS

```python
>>> a = np.array([[ 0, 1, 2, 3],
...                 [10,11,12,13]])
```

array([[ 0, 1, 2, 3],
       [10,11,12,13]])

## SHAPE = (ROWS, COLUMNS)

```python
>>> a.shape
(2, 4)
```

## ELEMENT COUNT

```python
>>> a.size
8
```

## NUMBER OF DIMENSIONS

© 2008-2018 Enthought, Inc.

## GET / SET ELEMENTS

```python
>>> a[1, 3]
```

13

```python
>>> a[1, 3] = -1
```

```python
>>> a
```

array([[ 0, 1, 2, 3],
       [10,11,12,-1]])

## ADDRESS SECOND (ONETH) ROW USING SINGLE INDEX

```python
>>> a[1]
array([10, 11, 12, -1])
```

## Array Slicing

## SLICING WORKS MUCH LIKE STANDARD PYTHON SLICING

```python
>>> a[0, 3:5]
array([3, 4])
```

```python
>>> a[4:, 4:]
```

array([[44, 45],
       [54, 55]])

```python
>>> a[:, 2]
```

array([2, 12, 22, 32, 42, 52])

## STRIDED ARE ALSO POSSIBLE

```python
>>> a[2::2, ::2]
```

array([[20, 22, 24],
       [40, 42, 44]])

|  | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 2 | 3 | 4 | 5 |
| 1 | 10 | 11 | 12 | 13 | 14 | 15 |
| 2 | 20 | 21 | 22 | 23 | 24 | 25 |
| 3 | 30 | 31 | 32 | 33 | 34 | 35 |
| 4 | 40 | 41 | 42 | 43 | 44 | 45 |
| 5 | 50 | 51 | 52 | 53 | 54 | 55 |

## Give it a try!

```txt
Create the array below with the command
a = np.arange(25).reshape(5, 5)
and extract the slices as indicated.
```

```python
# manual creation of masks
>>> mask = np.array(
...       [0, 1, 1, 0, 0, 1, 0, 0],
...       dtype=bool)
python
Sliced Arrays Share Data
Arrays created by slicing share data with the originating array.
Changing values in a slice also changes the original array.

>>> a = np.array([0, 1, 2, 3, 4])

# create a slice containing two elements of a
>>> b = a[2:4]
>>> b
array([2, 3])
>>> b[0] = 10

# changing b changed a!
>>> a
array([ 0,  1, 10, 3, 4])
```

## Fancy Indexing

## INDEXING BY POSITION

```python
>>> a = np.arange(0, 80, 10)

# fancy indexing
>>> indices = [1, 2, -3]
>>> y = a[indices]
>>> print(y)
[10 20 50]

# this also works with setting
>>> a[indices] = 99
>>> a
array([ 0, 99, 99, 30, 40, 99,
60, 70])
```

## INDEXING WITH BOOLEAN

```markdown
# fancy indexing
>>> y = a[mask]
>>> print(y)
array([99, 99, 99])
```

## Give it a try!

1. Create the array below with
a = np.arange(25).reshape(5, 5)
and extract the elements indicated in blue.

2. Extract all the numbers divisible by 3 using a boolean mask.

|  | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 5 | 6 | 7 | 8 | 9 |
| 2 | 10 | 11 | 12 | 13 | 14 |
| 3 | 15 | 16 | 17 | 18 | 19 |
| 4 | 20 | 21 | 22 | 23 | 24 |

```python
>>> np.ones((2, 3),
...        dtype='float32')
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.]],
       dtype=float32)
```

## Array Creation Functions

## ARANGE

arange([start,] stop[, step],
                       dtype=None)

Nearly identical to Python's range().
Creates an array of values in the range
[start,stop) with the specified step value.
Allows non-integer values for start, stop, and
step. Default dtype is derived from the start,
stop, and step values.

```txt
>>> np.arange(4)
array([0, 1, 2, 3])
>>> np.arange(0, 2*pi, pi/4)
array([ 0.000, 0.785, 1.571,
2.356, 3.142, 3.927, 4.712,
5.497])
```

## ONES, ZEROS

ones(shape, dtype='float64')
zeros(shape, dtype='float64')

shape is a number or sequence specifying the dimensions of the array. If dtype is not specified, it defaults to float64.

## Array Creation Functions (cont'd)

## LINSPACE

\# Generate N evenly spaced

## LOGSPACE

\# Generate N evenly spaced

\# elements on a log scale

\# between base\*\*start and

\# base\*\*stop (default base=10)

```python
>>> np.logspace(0, 1, 5)
```

array([1., 1.78, 3.16, 5.62, 10.])

## ARRAYS FROM/TO TXT FILES

```csv
BEGINNING OF THE FILE
% Day, Month, Year, Skip, Avg Power
01, 01, 2000, x876, 13 % crazy day!
% we don't have Jan 03rd
04, 01, 2000, xfed, 55
```

## Data.txt

\# generates an array from the
# txt file

```python
# Save an array into a txt file
javascript
np.savetxt('filename', arr)
```

## Computations with Arrays

Rule 1: Operations between multiple array objects are first checked for proper shape match.

Rule 2: Mathematical operators (+ - \* / exp, log, ...) apply element by element, on the values.

Rule 3: Reduction operations (mean, std, skew, kurt, sum, prod, ...) apply to the whole array, unless an axis is specified.

Rule 4: Missing values propagate unless explicitly ignored (nanmean, nansum, ...).

# Array Calculation Methods

## SUM METHOD

```python
# Methods act on data stored
# in the array
>>> a = np.array([[1,2,3],
        [4,5,6]])

# .sum() defaults to adding up
all the values in an array.
>>> a.sum()
21

# supply the keyword axis to
# sum along the 0th axis
>>> a.sum(axis=0)
array([5, 7, 9])

# supply the keyword axis to
# sum along the last axis
>>> a.sum(axis=-1)
array([ 6, 15])

© 2008-2018 Enthought, Inc.
```

## Other Operations on Arrays

## SUM FUNCTION

```python
# Functions work on data
# passed to it
>>> a = np.array([[1,2,3],
                  [4,5,6]])
txt
# sum() defaults to adding
# up all values in an array.
>>> np.sum(a)
21
txt
# supply an axis argument to
# sum along a specific axis
>>> np.sum(a, axis=0)
array([5, 7, 9])
```

## OTHER METHODS AND FUNCTIONS

## Mathematical functions

\- sum, prod

\- min, max, argmin, argmax

\- ptp (max - min)

## Statistics

\- mean, std, var

## Truth value testing

\- any, all

See the Numpy appendix for more.

## Where

## COORDINATE LOCATIONS

```txt
# NumPy's where function has two
# distinct uses. One is to
# provide coordinates from masks
>>> a = np.arange(-2, 2) ** 2
>>> a
array([4, 1, 0, 1])
>>> mask = a % 2 == 0
array([ True, False,   True,
False], dtype=bool)
# Coordinates are returned as
# a tuple of arrays, one for
# each axis
>>> np.where(mask)
(array([0, 2]),)
```

## CONDITIONAL ARRAY CREATION

```txt
# Where can also be used to
# construct a new array by
# choosing values from other
# arrays of the same shape
>>> positives = np.arange(4)
>>> negatives = -positives
>>> np.where(mask, positives,
...       negatives)
array([ 0, -1,  2, -3])
# Or from scalar values.
# This can be useful for
# recoding arrays
>>> np.where(mask, 1, 0)
array([1, 0, 1, 0])
# Or from both
>>> np.where(mask, positives, 0)
array([0, 0, 2, 0])
```

## Give it a try!

## Create the array below with

```txt
a = np.arange(-15, 15).reshape(5, 6) ** 2
and compute:
```

1. The maximum of each row (one max per row)

2. The mean of each column (one mean per column)

3. The position of the overall minimum (requires 2-3 steps)

|  | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 225 | 196 | 169 | 144 | 121 | 100 |
| 1 | 81 | 64 | 49 | 36 | 25 | 16 |
| 2 | 9 | 4 | 1 | 0 | 1 | 4 |
| 3 | 9 | 16 | 25 | 36 | 49 | 64 |
| 4 | 81 | 100 | 121 | 144 | 169 | 196 |

## Array Broadcasting

## RULE 1: PREPEND ONES TO SMALLER ARRAY'S SHAPE

```python
>>> import numpy as np
>>> a = np.ones((3, 5)) # a.shape == (3, 5)
>>> b = np.ones((5,)) # b.shape == (5,)
>>> b.reshape(1, 5) # result is a (1,5)-shaped array.
>>> b[np.newaxis, :] # equivalent, more concise.
```

## RULE 2: DIMENSIONS OF SIZE 1 ARE REPEATED WITHOUT COPYING

```python
>>> c = a + b # c.shape == (3, 5)
# is logically equivalent to...
>>> tmp_b = b.reshape(1, 5)
>>> tmp_b_repeat = tmp_b.repeat(3, axis=0)
>>> c = a + tmp_b_repeat
# But broadcasting makes no copies of "b"s data!
```

## Array Broadcasting

## Broadcasting Rules

```python
>>> import matplotlib.pyplot as plt
>>> a = np.linspace(0, 1, 15) - 0.5
>>> b = a[:, np.newaxis] # b.shape == (15, 1)
>>> dist2 = a**2 + b**2 # broadcasting sum.
>>> dist = np.sqrt(dist2)
>>> plt.imshow(dist)
>>> plt.colorbar()
```

## Application: Distance from Center

## Broadcasting's Usefulness

Broadcasting can often be used to replace needless data replication inside a NumPy array expression.

np.meshgrid() - use newaxis appropriately in broadcasting expressions.

np. repeat() – broadcasting makes repeating an array along a dimension of size 1 unnecessary.

## MESHGRID: COPIES DATA

```txt
>>> x, y = \
...     np.meshgrid([1,2],
...                          [3,4,5])
>>> z = x + y
© 2008-2017 Enthought, Inc.
```

## BROADCASTING: NO COPIES

```txt
>>> x = np.array([1, 2])
>>> y = np.array([3, 4, 5])
>>> z = x[np.newaxis, :] \
...         + y[:, np.newaxis]
```

## Broadcasting Indices

```python
>>> data_cube = np.arange(27).reshape(3, 3, 3)
>>> yi, xi = np.meshgrid(np.arange(3), np.arange(3),
...                 sparse=True)
>>> zi = np.array([[0, 1, 2],
...             [1, 1, 2],
...             [2, 2, 2]])
>>> horizon = data_cube[xi, yi, zi]
```

Indices

data\_cube

zi

Selected Data

```txt
op.reduce(a,axis=0)
op.accumulate(a,axis=0)
op.outer(a,b)
op.reduceat(a,indices)
```

## Universal Function Methods

```txt
The mathematical, comparative, logical, and bitwise operators op that take two arguments (binary operators) have special methods that operate on arrays:
```

## op.reduce()

op.reduce(a) applies op to all the elements in a 1-D array a reducing it to a single value.

For example:

$\begin{aligned} &amp; \mathrm{y} = \text{add.reduce(a)} \\ &amp; = \sum_{n=0}^{N-1} a[n] \\ &amp; = a[0] + a[1] + \dots + a[N-1] \end{aligned}$

## ADD EXAMPLE

## STRING LIST EXAMPLE

```python
>>> a = np.array(
    ['ab','cd','ef'],
    dtype='object')
>>> np.add.reduce(a)
'abcdef'
```

## LOGICAL OP EXAMPLES

```python
>>> np.add.reduce(a)
array([60, 64, 68])
```

## op.reduce()

For multidimensional arrays, op.reduce(a, axis) applies op to the elements of a along the specified axis. The resulting array has dimensionality one less than a. The default value for axis is 0.

## SUMMING UP EACH ROW

```python
>>> a = np.arange(3) + np.arange(0, 40,
...                      10).reshape(-1, 1)
>>> np.add.reduce(a,1)
array([ 3, 33, 63, 93])
```

## SUM COLUMNS BY DEFAULT

## op.accumulate()

op.accumulate(a) creates a new array containing the intermediate results of the reduce operation at each element in a.

For example:

$$
\begin{array}{c} \mathrm{y=add.accumulate(a)} \\ = \left[ \sum_ {n = 0} ^ {0} a [ n ], \sum_ {n = 0} ^ {1} a [ n ], \dots , \sum_ {n = 0} ^ {N - 1} a [ n ] \right] \end{array}
$$

## ADD EXAMPLE

## STRING LIST EXAMPLE

```python
>>> a = np.array(
    ['ab','cd','ef'],
    dtype='object')
>>> np.add.accumulate(a)
array([ab,abcd,abcdef],
        dtype=object)
```

## LOGICAL OP EXAMPLES

## op.reduceat()

## op.reduceat(a, indices)

applies op to ranges in the 1-D array a defined by the values in indices. The resulting array has the same length as indices.

## For example:

y = add.reduceat(a, indices)

$$
\mathrm{y} [ \mathrm{i} ] = \sum_ {n = i n d i c e \S i ]} ^ {i n d i c e \S i + 1 ]} a [ n ]
$$

## EXAMPLE

```txt
>>> a = np.array(
    [0,10,20,30,40,50])
>>> indices = np.array([1,4])
>>> np.add.reduceat(a,indices)
array([60, 90])
```

## For multidimensional arrays,

reduceat() is always applied along the last axis (sum of rows for 2-D arrays). This is different from the default for reduce() and accumulate().

## op.outer()

## >>> np.add.outer(a,b)

| a[0]+b[0] | a[0]+b[1] | a[0]+b[2] |
| --- | --- | --- |
| a[1]+b[0] | a[1]+b[1] | a[1]+b[2] |
| a[2]+b[0] | a[2]+b[1] | a[2]+b[2] |
| a[3]+b[0] | a[3]+b[1] | a[3]+b[2] |

Array Data Structure

Memory Block

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Python View:

| 0 | 1 | 2 |
| --- | --- | --- |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

## Transpose

## TRANSPOSE

```python
>>> a = np.array([[0,1,2],
...                 [3,4,5]])
```

```python
>>> a.shape
```

(2, 3)

\# Transpose swaps the order
# of axes.

```python
>>> a.T
```

```python
>>> a.T.shape
```

(3, 2)

## TRANSPOSE RETURNS VIEWS

\# Transpose does not move

\# values around in memory.

\# It only changes the order

\# of "strides" in the array

```python
>>> a.strides
```

(24, 8)

```python
>>> a.T.strides
```

(8, 24)

```elixir
# Flatten out elements to 1-D
>>> b = a.ravel()
>>> b
array([0,1,2,3])

# Changing b does change a
>>> b[0] = 10
>>> b
array([10,1,2,3])
>>> a
array([[10, 1],
       [ 2, 3]])
txt
# Changing b does not change a
>>> b[0] = 10
>>> b
array([10,1,2,3])
>>> a
array([[0, 1],
       [2, 3]])
```

## Flattening Arrays

## FLATTEN (SAFE)

a.flatten() converts a multi-dimensional array into a 1-D array. The new array is a copy of the original data.

```python
# Create a 2D array
>>> a = np.array([[0,1],
...                      [2,3]])
txt
# Flatten out elements to 1D
>>> b = a.flatten()
>>> b
array([0,1,2,3])
```

## RAVEL (EFFICIENT)

a.ravel() is the same as a.flatten(), but returns a reference (or view) of the array if possible (i.e., the memory is contiguous). Otherwise the new array copies the data.
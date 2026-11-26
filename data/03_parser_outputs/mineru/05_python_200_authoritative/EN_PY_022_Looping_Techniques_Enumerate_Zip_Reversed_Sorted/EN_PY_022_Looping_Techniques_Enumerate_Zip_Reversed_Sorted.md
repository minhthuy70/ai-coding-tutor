<!-- page: 1 -->
# EN_PY_022: Looping Techniques: enumerate(), zip(), reversed(), sorted(), and dict.items()

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Control Flow | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

5.6. Looping Techniques
=======================

When looping through dictionaries, the key and corresponding value can
be retrieved at the same time using the "items()" method.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave

```
When looping through a sequence, the position index and corresponding
value can be retrieved at the same time using the "enumerate()"
function.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

```
To loop over two or more sequences at the same time, the entries can
be paired with the "zip()" function.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

```

<!-- page: 2 -->

To loop over a sequence in reverse, first specify the sequence in a
forward direction and then call the "reversed()" function.

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

```
To loop over a sequence in sorted order, use the "sorted()" function
which returns a new sorted list while leaving the source unaltered.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear

```
Using "set()" on a sequence eliminates duplicate elements. The use of
"sorted()" in combination with "set()" over a sequence is an idiomatic
way to loop over unique elements of the sequence in sorted order.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear

```

<!-- page: 3 -->

It is sometimes tempting to change a list while you are looping over
it; however, it is often simpler and safer to create a new list
instead.

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]

```
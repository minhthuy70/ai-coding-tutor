# EN_PY_048: Standard Library: Command Line Arguments (sys.argv and argparse)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Standard Library | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

=============================

The "re" module provides regular expression tools for advanced string
processing. For complex matching and manipulation, regular expressions
offer succinct, optimized solutions:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'

```

When only simple capabilities are needed, string methods are preferred
because they are easier to read and debug:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'

```

10.6. Mathematics
=================

The "math" module gives access to the underlying C library functions
for floating-point math:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0

```

The "random" module provides tools for making random selections:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4

```

The "statistics" module calculates basic statistical properties (the
mean, median, variance, etc.) of numeric data:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095

```

The SciPy project <https://scipy.org> has many other modules for
numerical computations.

10.7. Internet Access
=====================

There are a number of modules for accessing the internet and
processing internet protocols. Two of the simplest are
"urllib.request" for retrieving data from URLs and "smtplib" for
sending mail:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
... Beware the Ides of March.
... """)
>>> server.quit()

```

(Note that the second example needs a mailserver running on
localhost.)

10.8. Dates and Times
=====================

The "datetime" module supplies classes for manipulating dates and
times in both simple and complex ways. While date and time arithmetic
is supported, the focus of the implementation is on efficient member
extraction for output formatting and manipulation.  The module also
supports objects that are timezone aware.

```python
>>> # dates are easily constructed and formatted
```
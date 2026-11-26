<!-- page: 1 -->
# EN_PY_047: Standard Library: Operating System Interface (os, shutil, glob)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Standard Library | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

10. Brief Tour of the Standard Library
**************************************


10.1. Operating System Interface
================================

The "os" module provides dozens of functions for interacting with the
operating system:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python312'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0

```
Be sure to use the "import os" style instead of "from os import *".
This will keep "os.open()" from shadowing the built-in "open()"
function which operates much differently.

The built-in "dir()" and "help()" functions are useful as interactive
aids for working with large modules like "os":

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>

```

<!-- page: 2 -->

For daily file and directory management tasks, the "shutil" module
provides a higher level interface that is easier to use:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'


```
10.2. File Wildcards
====================

The "glob" module provides a function for making file lists from
directory wildcard searches:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']


```
10.3. Command Line Arguments
============================

Common utility scripts often need to process command line arguments.
These arguments are stored in the "sys" module’s *argv* attribute as a
list.  For instance, let’s take the following "demo.py" file:

   # File demo.py
```python
import sys
print(sys.argv)

```
Here is the output from running "python demo.py one two three" at the
command line:

   ['demo.py', 'one', 'two', 'three']

The "argparse" module provides a more sophisticated mechanism to
process command line arguments.  The following script extracts one or

<!-- page: 3 -->

more filenames and an optional number of lines to be displayed:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

```
When run at the command line with "python top.py --lines=5 alpha.txt
beta.txt", the script sets "args.lines" to "5" and "args.filenames" to
"['alpha.txt', 'beta.txt']".


10.4. Error Output Redirection and Program Termination
======================================================

The "sys" module also has attributes for *stdin*, *stdout*, and
*stderr*. The latter is useful for emitting warnings and error
messages to make them visible even when *stdout* has been redirected:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one

```
The most direct way to terminate a script is to use "sys.exit()".


10.5. String Pattern Matching
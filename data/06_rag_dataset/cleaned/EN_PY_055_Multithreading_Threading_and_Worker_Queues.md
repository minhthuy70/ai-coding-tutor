# EN_PY_055: Standard Library: Multi-threading with threading and Worker Queues

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Concurrency | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

11. Brief Tour of the Standard Library — Part II
************************************************

This second tour covers more advanced modules that support
professional programming needs.  These modules rarely occur in small
scripts.

11.1. Output Formatting
=======================

The "reprlib" module provides a version of "repr()" customized for
abbreviated displays of large or deeply nested containers:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"

```

The "pprint" module offers more sophisticated control over printing
both built-in and user defined objects in a way that is readable by
the interpreter. When the result is longer than one line, the “pretty
printer” adds line breaks and indentation to more clearly reveal data
structure:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]

```

The "textwrap" module formats paragraphs of text to fit a given screen
width:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.

```

The "locale" module accesses a database of culture specific data
formats. The grouping attribute of locale’s format function provides a
direct way of formatting numbers with group separators:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format_string("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'

```

11.2. Templating
================

The "string" module includes a versatile "Template" class with a
simplified syntax suitable for editing by end-users.  This allows
users to customize their applications without having to alter the
application.

The format uses placeholder names formed by "$" with valid Python
identifiers (alphanumeric characters and underscores).  Surrounding
the placeholder with braces allows it to be followed by more

alphanumeric letters with no intervening spaces.  Writing "$$" creates
a single escaped "$":

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'

```

The "substitute()" method raises a "KeyError" when a placeholder is
not supplied in a dictionary or a keyword argument.  For mail-merge
style applications, user supplied data may be incomplete and the
"safe_substitute()" method may be more appropriate — it will leave
placeholders unchanged if data is missing:

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'

```

Template subclasses can specify a custom delimiter.  For example, a
batch renaming utility for a photo browser may elect to use percent
signs for placeholders such as the current date, image sequence
number, or file format:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
...
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
```
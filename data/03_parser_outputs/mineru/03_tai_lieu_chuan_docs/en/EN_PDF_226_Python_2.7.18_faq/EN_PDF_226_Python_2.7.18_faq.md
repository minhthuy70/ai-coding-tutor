<!-- page: 1 -->

# Python Frequently Asked Questions Release 2.7.18

**Guido van Rossum**

**and the Python development team**

**May 20, 2020**

**Python Software Foundation Email: docs@python.org**

<!-- page: 2 -->

<!-- page: 3 -->

- **1 General Python FAQ** 1
- **2 Programming FAQ** 9
- **3 Design and History FAQ 41**
- **4 Library and Extension FAQ 55**
- **5 Extending/Embedding FAQ 69**
- **6 Python on Windows FAQ 77**
- **7 Graphic User Interface FAQ 83**
- **8 “Why is Python Installed on my Computer?” FAQ 87**
- **A Glossary 89**
- **B About these documents 97**
- **C History and License 99**
- **D Copyright 115**
- **Index 117**

<!-- page: 4 -->

<!-- page: 5 -->

# GENERAL PYTHON FAQ

## 1.1 General Information

## 1.1.1 What is Python?

Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants, on the Mac, and on PCs under MS-DOS, Windows, Windows NT, and OS/2.

To find out more, start with tutorial-index. The [Beginner’s Guide to Python](https://wiki.python.org/moin/BeginnersGuide) links to other introductory tutorials and resources for learning Python.

## 1.1.2 What is the Python Software Foundation?

The Python Software Foundation is an independent non-profit organization that holds the copyright on Python versions 2.1 and newer. The PSF’s mission is to advance open source technology related to the Python programming language and to publicize the use of Python. The PSF’s home page is at [https://www.python.org/psf/](https://www.python.org/psf/).

Donations to the PSF are tax-exempt in the US. If you use Python and find it helpful, please contribute via [the PSF donation page](https://www.python.org/psf/donations/).

## 1.1.3 Are there copyright restrictions on the use of Python?

You can do anything you want with the source, as long as you leave the copyrights in and display those copyrights in any documentation about Python that you produce. If you honor the copyright rules, it’s OK to use Python for commercial use, to sell copies of Python in source or binary form (modified or unmodified), or to sell products that incorporate Python in some form. We would still like to know about all commercial use of Python, of course.

See [the PSF license page](https://www.python.org/psf/license/) to find further explanations and a link to the full text of the license.

The Python logo is trademarked, and in certain cases permission is required to use it. Consult [the Trademark Usage Policy](https://www.python.org/psf/trademarks/) for more information.

<!-- page: 6 -->

## 1.1.4 Why was Python created in the first place?

Here’s a very brief summary of what started it all, written by Guido van Rossum:

I had extensive experience with implementing an interpreted language in the ABC group at CWI, and from working with this group I had learned a lot about language design. This is the origin of many Python features, including the use of indentation for statement grouping and the inclusion of very-high-level data types (although the details are all different in Python).

I had a number of gripes about the ABC language, but also liked many of its features. It was impossible to extend the ABC language (or its implementation) to remedy my complaints – in fact its lack of extensibility was one of its biggest problems. I had some experience with using Modula-2+ and talked with the designers of Modula-3 and read the Modula-3 report. Modula-3 is the origin of the syntax and semantics used for exceptions, and some other Python features.

I was working in the Amoeba distributed operating system group at CWI. We needed a better way to do system administration than by writing either C programs or Bourne shell scripts, since Amoeba had its own system call interface which wasn’t easily accessible from the Bourne shell. My experience with error handling in Amoeba made me acutely aware of the importance of exceptions as a programming language feature.

It occurred to me that a scripting language with a syntax like ABC but with access to the Amoeba system calls would fill the need. I realized that it would be foolish to write an Amoeba-specific language, so I decided that I needed a language that was generally extensible.

During the 1989 Christmas holidays, I had a lot of time on my hand, so I decided to give it a try. During the next year, while still mostly working on it in my own time, Python was used in the Amoeba project with increasing success, and the feedback from colleagues made me add many early improvements.

In February 1991, after just over a year of development, I decided to post to USENET. The rest is in the Misc/HISTORY file.

## 1.1.5 What is Python good for?

Python is a high-level general-purpose programming language that can be applied to many different classes of problems.

The language comes with a large standard library that covers areas such as string processing (regular expressions, Unicode, calculating differences between files), Internet protocols (HTTP, FTP, SMTP, XML-RPC, POP, IMAP, CGI programming), software engineering (unit testing, logging, profiling, parsing Python code), and operating system interfaces (system calls, filesystems, TCP/IP sockets). Look at the table of contents for library-index to get an idea of what’s available. A wide variety of third-party extensions are also available. Consult [the Python Package Index](https://pypi.org) to find packages of interest to you.

## 1.1.6 How does the Python version numbering scheme work?

Python versions are numbered A.B.C or A.B. A is the major version number – it is only incremented for really major changes in the language. B is the minor version number, incremented for less earth-shattering changes. C is the micro-level – it is incremented for each bugfix release. See [**PEP 6**](https://www.python.org/dev/peps/pep-0006) for more information about bugfix releases.

Not all releases are bugfix releases. In the run-up to a new major release, a series of development releases are made, denoted as alpha, beta, or release candidate. Alphas are early releases in which interfaces aren’t yet finalized; it’s not unexpected to see an interface change between two alpha releases. Betas are more stable, preserving existing interfaces but possibly adding new modules, and release candidates are frozen, making no changes except as needed to fix critical bugs.

Alpha, beta and release candidate versions have an additional suffix. The suffix for an alpha version is “aN” for some small number N, the suffix for a beta version is “bN” for some small number N, and the suffix for a release candidate version

<!-- page: 7 -->

is “cN” for some small number N. In other words, all versions labeled 2.0aN precede the versions labeled 2.0bN, which precede versions labeled 2.0cN, and those precede 2.0.

You may also find version numbers with a “+” suffix, e.g. “2.2+”. These are unreleased versions, built directly from the CPython development repository. In practice, after a final minor release is made, the version is incremented to the next minor version, which becomes the “a0” version, e.g. “2.4a0”.

See also the documentation for sys.version, sys.hexversion, and sys.version\_info.

## 1.1.7 How do I obtain a copy of the Python source?

The latest Python source distribution is always available from python.org, at [https://www.python.org/downloads/](https://www.python.org/downloads/). The latest development sources can be obtained at [https://github.com/python/cpython/](https://github.com/python/cpython/).

The source distribution is a gzipped tar file containing the complete C source, Sphinx-formatted documentation, Python library modules, example programs, and several useful pieces of freely distributable software. The source will compile and run out of the box on most UNIX platforms.

Consult the [Getting Started section of the Python Developer’s Guide](https://docs.python.org/devguide/setup.html) for more information on getting the source code and compiling it.

## 1.1.8 How do I get documentation on Python?

The standard documentation for the current stable version of Python is available at [https://docs.python.org/3/](https://docs.python.org/3/). PDF, plain text, and downloadable HTML versions are also available at [https://docs.python.org/3/download.html](https://docs.python.org/3/download.html).

The documentation is written in reStructuredText and processed by [the Sphinx documentation tool](http://sphinx-doc.org/). The reStructuredText source for the documentation is part of the Python source distribution.

## 1.1.9 I’ve never programmed before. Is there a Python tutorial?

There are numerous tutorials and books available. The standard documentation includes tutorial-index.

Consult [the Beginner’s Guide](https://wiki.python.org/moin/BeginnersGuide) to find information for beginning Python programmers, including lists of tutorials.

## 1.1.10 Is there a newsgroup or mailing list devoted to Python?

There is a newsgroup, comp.lang.python, and a mailing list, [python-list](https://mail.python.org/mailman/listinfo/python-list). The newsgroup and mailing list are gatewayed into each other – if you can read news it’s unnecessary to subscribe to the mailing list. comp.lang.python is high-traffic, receiving hundreds of postings every day, and Usenet readers are often more able to cope with this volume.

Announcements of new software releases and events can be found in comp.lang.python.announce, a low-traffic moderated list that receives about five postings per day. It’s available as [the python-announce mailing list](https://mail.python.org/mailman/listinfo/python-announce-list).

More info about other mailing lists and newsgroups can be found at [https://www.python.org/community/lists/](https://www.python.org/community/lists/).

<!-- page: 8 -->

## 1.1.11 How do I get a beta test version of Python?

Alpha and beta releases are available from [https://www.python.org/downloads/](https://www.python.org/downloads/). All releases are announced on the comp.lang.python and comp.lang.python.announce newsgroups and on the Python home page at [https://www.python.org/](https://www.python.org/);an RSS feed of news is available.

You can also access the development version of Python through Git. See [The Python Developer’s Guide](https://docs.python.org/devguide/) for details.

## 1.1.12 How do I submit bug reports and patches for Python?

To report a bug or submit a patch, please use the Roundup installation at [https://bugs.python.org/](https://bugs.python.org/).

You must have a Roundup account to report bugs; this makes it possible for us to contact you if we have follow-up questions. It will also enable Roundup to send you updates as we act on your bug. If you had previously used SourceForge to report bugs to Python, you can obtain your Roundup password through Roundup’s [password reset procedure](https://bugs.python.org/user?@template=forgotten).

For more information on how Python is developed, consult [the Python Developer’s Guide](https://docs.python.org/devguide/).

## 1.1.13 Are there any published articles about Python that I can reference?

It’s probably best to cite your favorite book about Python.

The very first article about Python was written in 1991 and is now quite outdated.

Guido van Rossum and Jelke de Boer, “Interactively Testing Remote Servers Using the Python Programming Language”, CWI Quarterly, Volume 4, Issue 4 (December 1991), Amsterdam, pp 283–303.

## 1.1.14 Are there any books on Python?

Yes, there are many, and more are being published. See the python.org wiki at [https://wiki.python.org/moin/PythonBooks](https://wiki.python.org/moin/PythonBooks)for a list.

You can also search online bookstores for “Python” and filter out the Monty Python references; or perhaps search for “Python” and “language”.

## 1.1.15 Where in the world is www.python.org located?

The Python project’s infrastructure is located all over the world and is managed by the Python Infrastructure Team. Details [here](http://infra.psf.io).

## 1.1.16 Why is it called Python?

When he began implementing Python, Guido van Rossum was also reading the published scripts from [“Monty Python’s Flying Circus”](https://en.wikipedia.org/wiki/Monty_Python), a BBC comedy series from the 1970s. Van Rossum thought he needed a name that was short, unique, and slightly mysterious, so he decided to call the language Python.

<!-- page: 9 -->

## 1.1.17 Do I have to like “Monty Python’s Flying Circus”?

No, but it helps. :)

## 1.2 Python in the real world

## 1.2.1 How stable is Python?

Very stable. New, stable releases have been coming out roughly every 6 to 18 months since 1991, and this seems likely to continue. Currently there are usually around 18 months between major releases.

The developers issue “bugfix” releases of older versions, so the stability of existing releases gradually improves. Bugfix releases, indicated by a third component of the version number (e.g. 3.5.3, 3.6.2), are managed for stability; only fixes for known problems are included in a bugfix release, and it’s guaranteed that interfaces will remain the same throughout a series of bugfix releases.

The latest stable releases can always be found on the [Python download page](https://www.python.org/downloads/). There are two production-ready versions of Python: 2.x and 3.x. The recommended version is 3.x, which is supported by most widely used libraries. Although 2.x is still widely used, [it will not be maintained after January 1, 2020](https://www.python.org/dev/peps/pep-0373/).

## 1.2.2 How many people are using Python?

There are probably tens of thousands of users, though it’s difficult to obtain an exact count.

Python is available for free download, so there are no sales figures, and it’s available from many different sites and packaged with many Linux distributions, so download statistics don’t tell the whole story either.

The comp.lang.python newsgroup is very active, but not all Python users post to the group or even read it.

## 1.2.3 Have any significant projects been done in Python?

See [https://www.python.org/about/success](https://www.python.org/about/success) for a list of projects that use Python. Consulting the proceedings for [past Python conferences](https://www.python.org/community/workshops/) will reveal contributions from many different companies and organizations.

High-profile Python projects include [the Mailman mailing list manager](http://www.list.org) and [the Zope application server](http://www.zope.org). Several Linux distributions, most notably [Red Hat](https://www.redhat.com), have written part or all of their installer and system administration software in Python. Companies that use Python internally include Google, Yahoo, and Lucasfilm Ltd.

## 1.2.4 What new developments are expected for Python in the future?

See [https://www.python.org/dev/peps/](https://www.python.org/dev/peps/) for the Python Enhancement Proposals (PEPs). PEPs are design documents describing a suggested new feature for Python, providing a concise technical specification and a rationale. Look for a PEP titled “Python X.Y Release Schedule”, where X.Y is a version that hasn’t been publicly released yet.

New development is discussed on [the python-dev mailing list](https://mail.python.org/mailman/listinfo/python-dev/).

<!-- page: 10 -->

## 1.2.5 Is it reasonable to propose incompatible changes to Python?

In general, no. There are already millions of lines of Python code around the world, so any change in the language that invalidates more than a very small fraction of existing programs has to be frowned upon. Even if you can provide a conversion program, there’s still the problem of updating all documentation; many books have been written about Python, and we don’t want to invalidate them all at a single stroke.

Providing a gradual upgrade path is necessary if a feature has to be changed. [**PEP 5**](https://www.python.org/dev/peps/pep-0005) describes the procedure followed for introducing backward-incompatible changes while minimizing disruption for users.

## 1.2.6 Is Python a good language for beginning programmers?

Yes.

It is still common to start students with a procedural and statically typed language such as Pascal, C, or a subset of C++ or Java. Students may be better served by learning Python as their first language. Python has a very simple and consistent syntax and a large standard library and, most importantly, using Python in a beginning programming course lets students concentrate on important programming skills such as problem decomposition and data type design. With Python, students can be quickly introduced to basic concepts such as loops and procedures. They can probably even work with user-defined objects in their very first course.

For a student who has never programmed before, using a statically typed language seems unnatural. It presents additional complexity that the student must master and slows the pace of the course. The students are trying to learn to think like a computer, decompose problems, design consistent interfaces, and encapsulate data. While learning to use a statically typed language is important in the long term, it is not necessarily the best topic to address in the students’ first programming course.

Many other aspects of Python make it a good first language. Like Java, Python has a large standard library so that students can be assigned programming projects very early in the course that do something. Assignments aren’t restricted to the standard four-function calculator and check balancing programs. By using the standard library, students can gain the satisfaction of working on realistic applications as they learn the fundamentals of programming. Using the standard library also teaches students about code reuse. Third-party modules such as PyGame are also helpful in extending the students’ reach.

Python’s interactive interpreter enables students to test language features while they’re programming. They can keep a window with the interpreter running while they enter their program’s source in another window. If they can’t remember the methods for a list, they can do something like this:

```txt
>>> L = []
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
'__delslice__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getslice__', '__gt__',
'__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__',
'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
'__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
'__subclasshook__', 'append', 'count', 'extend', 'index', 'insert',
'pop', 'remove', 'reverse', 'sort']
>>> help(L.append)
Help on built-in function append:

append(...)
    L.append(object) -- append object to end

>>> L.append(1)
```

(continues on next page)

<!-- page: 11 -->

```txt
>>> L
[1]
```

(continued from previous page)

With the interpreter, documentation is never far from the student as he’s programming.

There are also good IDEs for Python. IDLE is a cross-platform IDE for Python that is written in Python using Tkinter. PythonWin is a Windows-specific IDE. Emacs users will be happy to know that there is a very good Python mode for Emacs. All of these programming environments provide syntax highlighting, auto-indenting, and access to the interactive interpreter while coding. Consult [the Python wiki](https://wiki.python.org/moin/PythonEditors) for a full list of Python editing environments.

If you want to discuss Python’s use in education, you may be interested in joining [the edu-sig mailing list](https://www.python.org/community/sigs/current/edu-sig).

## 1.3 Upgrading Python

## 1.3.1 What is this bsddb185 module my application keeps complaining about?

Starting with Python2.3, the distribution includes the PyBSDDB package &lt;http://pybsddb.sf.net/&gt; as a replacement for the old bsddb module. It includes functions which provide backward compatibility at the API level, but requires a newer version of the underlying [Berkeley DB](http://www.sleepycat.com) library. Files created with the older bsddb module can’t be opened directly using the new module.

Using your old version of Python and a pair of scripts which are part of Python 2.3 (db2pickle.py and pickle2db.py, in the Tools/scripts directory) you can convert your old database files to the new format. Using your old Python version, run the db2pickle.py script to convert it to a pickle, e.g.:

python2.2 &lt;pathto&gt;/db2pickley.py database.db database.pck

Rename your database file:

```txt
mv database.db olddatabase.db
```

Now convert the pickle file to a new format database:

```batch
python <pathto>/pickle2db.py database.db database.pck
```

The precise commands you use will vary depending on the particulars of your installation. For full details about operation of these two scripts check the doc string at the start of each one.

<!-- page: 12 -->

<!-- page: 13 -->

# PROGRAMMING FAQ

## 2.1 General Questions

## 2.1.1 Is there a source code level debugger with breakpoints, single-stepping, etc.? Yes.

The pdb module is a simple but adequate console-mode debugger for Python. It is part of the standard Python library, and is documented in the Library Reference Manual. You can also write your own debugger by using the code for pdb as an example.

The IDLE interactive development environment, which is part of the standard Python distribution (normally available as Tools/scripts/idle), includes a graphical debugger.

PythonWin is a Python IDE that includes a GUI debugger based on pdb. The Pythonwin debugger colors breakpoints and has quite a few cool features such as debugging non-Pythonwin programs. Pythonwin is available as part of the [Python for Windows Extensions](https://sourceforge.net/projects/pywin32/) project and as a part of the ActivePython distribution (see [https://www.activestate.com/activepython](https://www.activestate.com/activepython)).

[Boa Constructor](http://boa-constructor.sourceforge.net/) is an IDE and GUI builder that uses wxWidgets. It offers visual frame creation and manipulation, an object inspector, many views on the source like object browsers, inheritance hierarchies, doc string generated html documentation, an advanced debugger, integrated help, and Zope support.

[Eric](http://eric-ide.python-projects.org/) is an IDE built on PyQt and the Scintilla editing component.

Pydb is a version of the standard Python debugger pdb, modified for use with DDD (Data Display Debugger), a popular graphical debugger front end. Pydb can be found at [http://bashdb.sourceforge.net/pydb/](http://bashdb.sourceforge.net/pydb/) and DDD can be found at [https://www.gnu.org/software/ddd](https://www.gnu.org/software/ddd).

There are a number of commercial Python IDEs that include graphical debuggers. They include:

• Wing IDE ([https://wingware.com/](https://wingware.com/))

• Komodo IDE ([https://komodoide.com/](https://komodoide.com/))

• PyCharm ([https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/))

<!-- page: 14 -->

## 2.1.2 Is there a tool to help find bugs or perform static analysis?

Yes.

PyChecker is a static analysis tool that finds bugs in Python source code and warns about code complexity and style. You can get PyChecker from [http://pychecker.sourceforge.net/](http://pychecker.sourceforge.net/).

[Pylint](https://www.pylint.org/) is another tool that checks if a module satisfies a coding standard, and also makes it possible to write plug-ins to add a custom feature. In addition to the bug checking that PyChecker performs, Pylint offers some additional features such as checking line length, whether variable names are well-formed according to your coding standard, whether declared interfaces are fully implemented, and more. [https://docs.pylint.org/](https://docs.pylint.org/) provides a full list of Pylint’s features.

## 2.1.3 How can I create a stand-alone binary from a Python script?

You don’t need the ability to compile Python to C code if all you want is a stand-alone program that users can download and run without having to install the Python distribution first. There are a number of tools that determine the set of modules required by a program and bind these modules together with a Python binary to produce a single executable.

One is to use the freeze tool, which is included in the Python source tree as Tools/freeze. It converts Python byte code to C arrays; a C compiler you can embed all your modules into a new program, which is then linked with the standard Python modules.

It works by scanning your source recursively for import statements (in both forms) and looking for the modules in the standard Python path as well as in the source directory (for built-in modules). It then turns the bytecode for modules written in Python into C code (array initializers that can be turned into code objects using the marshal module) and creates a custom-made config file that only contains those built-in modules which are actually used in the program. It then compiles the generated C code and links it with the rest of the Python interpreter to form a self-contained binary which acts exactly like your script.

Obviously, freeze requires a C compiler. There are several other utilities which don’t. One is Thomas Heller’s py2exe (Windows only) at

[http://www.py2exe.org/](http://www.py2exe.org/)

Another tool is Anthony Tuininga’s [cx\_Freeze](http://cx-freeze.sourceforge.net/).

## 2.1.4 Are there coding standards or a style guide for Python programs?

Yes. The coding style required for standard library modules is documented as [**PEP 8**](https://www.python.org/dev/peps/pep-0008).

## 2.1.5 My program is too slow. How do I speed it up?

That’s a tough one, in general. There are many tricks to speed up Python code; consider rewriting parts in C as a last resort.

In some cases it’s possible to automatically translate Python to C or x86 assembly language, meaning that you don’t have to modify your code to gain increased speed.

[Pyrex](http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/) can compile a slightly modified version of Python code into a C extension, and can be used on many different platforms.

[Psyco](http://psyco.sourceforge.net) is a just-in-time compiler that translates Python code into x86 assembly language. If you can use it, Psyco can provide dramatic speedups for critical functions.

The rest of this answer will discuss various tricks for squeezing a bit more speed out of Python code. Never apply any optimization tricks unless you know you need them, after profiling has indicated that a particular function is the heavily executed hot spot in the code. Optimizations almost always make the code less clear, and you shouldn’t pay the costs of

<!-- page: 15 -->

reduced clarity (increased development time, greater likelihood of bugs) unless the resulting performance benefit is worth it.

There is a page on the wiki devoted to [performance tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips).

Guido van Rossum has written up an anecdote related to optimization at [https://www.python.org/doc/essays/list2str](https://www.python.org/doc/essays/list2str).

One thing to notice is that function and (especially) method calls are rather expensive; if you have designed a purely OO interface with lots of tiny functions that don’t do much more than get or set an instance variable or call another method, you might consider using a more direct way such as directly accessing instance variables. Also see the standard module profile which makes it possible to find out where your program is spending most of its time (if you have some patience – the profiling itself can slow your program down by an order of magnitude).

Remember that many standard optimization heuristics you may know from other programming experience may well apply to Python. For example it may be faster to send output to output devices using larger writes rather than smaller ones in order to reduce the overhead of kernel system calls. Thus CGI scripts that write all output in “one shot” may be faster than those that write lots of small pieces of output.

Also, be sure to use Python’s core features where appropriate. For example, slicing allows programs to chop up lists and other sequence objects in a single tick of the interpreter’s mainloop using highly optimized C implementations. Thus to get the same effect as:

```python
L2 = []
for i in range(3):
    L2.append(L1[i])
```

it is much shorter and far faster to use

```txt
L2 = list(L1[:3])  # "list" is redundant if L1 is a list.
```

Note that the functionally-oriented built-in functions such as map(), zip(), and friends can be a convenient accelerator for loops that perform a single task. For example to pair the elements of two lists together:

```txt
>>> zip([1, 2, 3], [4, 5, 6])
[(1, 4), (2, 5), (3, 6)]
```

or to compute a number of sines:

```txt
>>> map(math.sin, (1, 2, 3, 4))
[0.841470984808, 0.909297426826, 0.14112000806, -0.756802495308]
```

The operation completes very quickly in such cases.

Other examples include the join() and split() methods of string objects. For example if s1..s7 are large (10K+) strings then "".join([s1,s2,s3,s4,s5,s6,s7]) may be far faster than the more obvious s1+s2+s3+s4+s5+s6+s7, since the “summation” will compute many subexpressions, whereas join() does all the copying in one pass. For manipulating strings, use the replace() and the format() methods on string objects. Use regular expressions only when you’re not dealing with constant string patterns. You may still use the old % operations string % tuple and string % dictionary.

Be sure to use the list.sort() built-in method to do sorting, and see the [sorting mini-HOWTO](https://wiki.python.org/moin/HowTo/Sorting) for examples of moderately advanced usage. list.sort() beats other techniques for sorting in all but the most extreme circumstances.

Another common trick is to “push loops into functions or methods.” For example suppose you have a program that runs slowly and you use the profiler to determine that a Python function ff() is being called lots of times. If you notice that ff():

```python
def ff(x):
    ... # do something with x computing result...
    return result
```

<!-- page: 16 -->

tends to be called in loops like:

```txt
list = map(ff, oldlist)
```

or:

```python
for x in sequence:
    value = ff(x)
    ... # do something with value...
```

then you can often eliminate function call overhead by rewriting ff() to:

```python
def ffseq(seq):
    resultseq = []
    for x in seq:
        ... # do something with x computing result...
        resultseq.append(result)
    return resultseq
```

and rewrite the two examples to list = ffseq(oldlist) and to:

```python
for value in ffseq(sequence):
    ... # do something with value...
```

Single calls to ff(x) translate to ffseq([x])[0] with little penalty. Of course this technique is not always appropriate and there are other variants which you can figure out.

You can gain some performance by explicitly storing the results of a function or method lookup into a local variable. A loop like:

```python
for key in token:
    dict[key] = dict.get(key, 0) + 1
```

resolves dict.get every iteration. If the method isn’t going to change, a slightly faster implementation is:

```python
dict_get = dict.get  # look up the method once
for key in token:
    dict[key] = dict_get(key, 0) + 1
```

Default arguments can be used to determine values once, at compile time instead of at run time. This can only be done for functions or objects which will not be changed during program execution, such as replacing

```python
def degree_sin(deg):
    return math.sin(deg * math.pi / 180.0)
```

with

```python
def degree_sin(deg, factor=math.pi/180.0, sin=math.sin):
    return sin(deg * factor)
```

Because this trick uses default arguments for terms which should not be changed, it should only be used when you are not concerned with presenting a possibly confusing API to your users.

<!-- page: 17 -->

## 2.2 Core Language

## 2.2.1 Why am I getting an UnboundLocalError when the variable has a value?

It can be a surprise to get the UnboundLocalError in previously working code when it is modified by adding an assignment statement somewhere in the body of a function.

This code:

```txt
>>> x = 10
>>> def bar():
...     print x
>>> bar()
10
```

works, but this code:

```python
>>> x = 10
>>> def foo():
...     print x
...     x += 1
```

results in an UnboundLocalError:

```txt
>>> foo()
Traceback (most recent call last):
  ...
UnboundLocalError: local variable 'x' referenced before assignment
```

This is because when you make an assignment to a variable in a scope, that variable becomes local to that scope and shadows any similarly named variable in the outer scope. Since the last statement in foo assigns a new value to x, the compiler recognizes it as a local variable. Consequently when the earlier print x attempts to print the uninitialized local variable and an error results.

In the example above you can access the outer scope variable by declaring it global:

```python
>>> x = 10
>>> def foobar():
...     global x
...     print x
...     x += 1
>>> foobar()
10
```

This explicit declaration is required in order to remind you that (unlike the superficially analogous situation with class and instance variables) you are actually modifying the value of the variable in the outer scope:

```txt
>>> print x
11
```

<!-- page: 18 -->

## 2.2.2 What are the rules for local and global variables in Python?

In Python, variables that are only referenced inside a function are implicitly global. If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.

Though a bit surprising at first, a moment’s consideration explains this. On one hand, requiring global for assigned variables provides a bar against unintended side-effects. On the other hand, if global was required for all global references, you’d be using global all the time. You’d have to declare as global every reference to a built-in function or to a component of an imported module. This clutter would defeat the usefulness of the global declaration for identifying side-effects.

## 2.2.3 Why do lambdas defined in a loop with different values all return the same result?

Assume you use a for loop to define a few different lambdas (or even plain functions), e.g.:

```txt
>>> squares = []
>>> for x in range(5):
...     squares.append(lambda: x**2)
```

This gives you a list that contains 5 lambdas that calculate x\*\*2. You might expect that, when called, they would return, respectively, 0, 1, 4, 9, and 16. However, when you actually try you will see that they all return 16:

```txt
>>> squares[2]()
16
>>> squares[4]()
16
```

This happens because x is not local to the lambdas, but is defined in the outer scope, and it is accessed when the lambda is called — not when it is defined. At the end of the loop, the value of x is 4, so all the functions now return 4\*\*2, i.e. 16. You can also verify this by changing the value of x and see how the results of the lambdas change:

```txt
>>> x = 8
>>> squares[2]()
64
```

In order to avoid this, you need to save the values in variables local to the lambdas, so that they don’t rely on the value of the global x:

```txt
>>> squares = []
>>> for x in range(5):
...     squares.append(lambda n=x: n**2)
```

Here, n=x creates a new variable n local to the lambda and computed when the lambda is defined so that it has the same value that x had at that point in the loop. This means that the value of n will be 0 in the first lambda, 1 in the second, 2 in the third, and so on. Therefore each lambda will now return the correct result:

```txt
>>> squares[2] ()
4
>>> squares[4] ()
16
```

Note that this behaviour is not peculiar to lambdas, but applies to regular functions too.

<!-- page: 19 -->

## 2.2.4 How do I share global variables across modules?

The canonical way to share information across modules within a single program is to create a special module (often called config or cfg). Just import the config module in all modules of your application; the module then becomes available as a global name. Because there is only one instance of each module, any changes made to the module object get reflected everywhere. For example:

config.py:

```ruby
x = 0    # Default value of the 'x' configuration setting
```

mod.py:

```python
import config
config.x = 1
```

main.py:

```python
import config
import mod
print config.x
```

Note that using a module is also the basis for implementing the Singleton design pattern, for the same reason.

## 2.2.5 What are the “best practices” for using import in a module?

In general, don’t use from modulename import \*. Doing so clutters the importer’s namespace, and makes it much harder for linters to detect undefined names.

Import modules at the top of a file. Doing so makes it clear what other modules your code requires and avoids questions of whether the module name is in scope. Using one import per line makes it easy to add and delete module imports, but using multiple imports per line uses less screen space.

It’s good practice if you import modules in the following order:

1. standard library modules – e.g. sys, os, getopt, re

2. third-party library modules (anything installed in Python’s site-packages directory) – e.g. mx.DateTime, ZODB, PIL.Image, etc.

## 3. locally-developed modules

Only use explicit relative package imports. If you’re writing code that’s in the package.sub.m1 module and want to import package.sub.m2, do not just write import m2, even though it’s legal. Write from package.sub import m2 or from . import m2 instead.

It is sometimes necessary to move imports to a function or class to avoid problems with circular imports. Gordon McMillan says:

Circular imports are fine where both modules use the “import &lt;module&gt;” form of import. They fail when the 2nd module wants to grab a name out of the first (“from module import name”) and the import is at the top level. That’s because names in the 1st are not yet available, because the first module is busy importing the 2nd.

In this case, if the second module is only used in one function, then the import can easily be moved into that function. By the time the import is called, the first module will have finished initializing, and the second module can do its import.

It may also be necessary to move imports out of the top level of code if some of the modules are platform-specific. In that case, it may not even be possible to import all of the modules at the top of the file. In this case, importing the correct modules in the corresponding platform-specific code is a good option.

<!-- page: 20 -->

Only move imports into a local scope, such as inside a function definition, if it’s necessary to solve a problem such as avoiding a circular import or are trying to reduce the initialization time of a module. This technique is especially helpful if many of the imports are unnecessary depending on how the program executes. You may also want to move imports into a function if the modules are only ever used in that function. Note that loading a module the first time may be expensive because of the one time initialization of the module, but loading a module multiple times is virtually free, costing only a couple of dictionary lookups. Even if the module name has gone out of scope, the module is probably available in sys.modules.

## 2.2.6 Why are default values shared between objects?

This type of bug commonly bites neophyte programmers. Consider this function:

```python
def foo(mydict={}):  # Danger: shared reference to one dict for all calls
    ... compute something ...
    mydict[key] = value
    return mydict
```

The first time you call this function, mydict contains a single item. The second time, mydict contains two items because when foo() begins executing, mydict starts out with an item already in it.

It is often expected that a function call creates new objects for default values. This is not what happens. Default values are created exactly once, when the function is defined. If that object is changed, like the dictionary in this example, subsequent calls to the function will refer to this changed object.

By definition, immutable objects such as numbers, strings, tuples, and None, are safe from change. Changes to mutable objects such as dictionaries, lists, and class instances can lead to confusion.

Because of this feature, it is good programming practice to not use mutable objects as default values. Instead, use None as the default value and inside the function, check if the parameter is None and create a new list/dictionary/whatever if it is. For example, don’t write:

```txt
def foo(mydict={}):
```

but:

```python
def foo(mydict=None):
    if mydict is None:
        mydict = {}  # create a new dict for local namespace
```

This feature can be useful. When you have a function that’s time-consuming to compute, a common technique is to cache the parameters and the resulting value of each call to the function, and return the cached value if the same value is requested again. This is called “memoizing”, and can be implemented like this:

```python
# Callers will never provide a third parameter for this function.
def expensive(arg1, arg2, _cache={}):
    if (arg1, arg2) in _cache:
        return _cache[(arg1, arg2)]

    # Calculate the value
    result = ... expensive computation ...
    _cache[(arg1, arg2)] = result          # Store result in the cache
    return result
```

You could use a global variable containing a dictionary instead of the default value; it’s a matter of taste.

<!-- page: 21 -->

## 2.2.7 How can I pass optional or keyword parameters from one function to another?

Collect the arguments using the \* and \*\* specifiers in the function’s parameter list; this gives you the positional arguments as a tuple and the keyword arguments as a dictionary. You can then pass these arguments when calling another function by using \* and \*\*:

```python
def f(x, *args, **kwargs):
    ...
    kwargs['width'] = '14.3c'
    ...
    g(x, *args, **kwargs)
```

In the unlikely case that you care about Python versions older than 2.0, use apply():

```matlab
def f(x, *args, **kwargs):
    ...
    kwargs['width'] = '14.3c'
    ...
    apply(g, (x,)+args, kwargs)
```

## 2.2.8 What is the difference between arguments and parameters?

Parameters are defined by the names that appear in a function definition, whereas arguments are the values actually passed to a function when calling it. Parameters define what types of arguments a function can accept. For example, given the function definition:

```python
def func(foo, bar=None, **kwargs):
    pass
```

foo, bar and kwargs are parameters of func. However, when calling func, for example:

```txt
func(42, bar=314, extra=somevar)
```

the values 42, 314, and somevar are arguments.

## 2.2.9 Why did changing list ‘y’ also change list ‘x’?

If you wrote code like:

```txt
>>> x = []
>>> y = x
>>> y.append(10)
>>> y
[10]
>>> x
[10]
```

you might be wondering why appending an element to y changed x too.

There are two factors that produce this result:

1) Variables are simply names that refer to objects. Doing y = x doesn’t create a copy of the list – it creates a new variable y that refers to the same object x refers to. This means that there is only one object (the list), and both x and y refer to it.

<!-- page: 22 -->

2) Lists are mutable, which means that you can change their content.

After the call to append(), the content of the mutable object has changed from [] to [10]. Since both the variables refer to the same object, using either name accesses the modified value [10].

If we instead assign an immutable object to x:

```diff
>>> x = 5  # ints are immutable
>>> y = x
>>> x = x + 1  # 5 can't be mutated, we are creating a new object here
>>> x
6
>>> y
5
```

we can see that in this case x and y are not equal anymore. This is because integers are immutable, and when we do x = x + 1 we are not mutating the int 5 by incrementing its value; instead, we are creating a new object (the int 6) and assigning it to x (that is, changing which object x refers to). After this assignment we have two objects (the ints 6 and 5) and two variables that refer to them (x now refers to 6 but y still refers to 5).

Some operations (for example y.append(10) and y.sort()) mutate the object, whereas superficially similar operations (for example y = y + [10] and sorted(y)) create a new object. In general in Python (and in all cases in the standard library) a method that mutates an object will return None to help avoid getting the two types of operations confused. So if you mistakenly write y.sort() thinking it will give you a sorted copy of y, you’ll instead end up with None, which will likely cause your program to generate an easily diagnosed error.

However, there is one class of operations where the same operation sometimes has different behaviors with different types: the augmented assignment operators. For example, += mutates lists but not tuples or ints (a\_list += [1, 2, 3] is equivalent to a\_list.extend([1, 2, 3]) and mutates a\_list, whereas some\_tuple += (1, 2, 3) and some\_int += 1 create new objects).

In other words:

• If we have a mutable object (list, dict, set, etc.), we can use some specific operations to mutate it and all the variables that refer to it will see the change.

• If we have an immutable object (str, int, tuple, etc.), all the variables that refer to it will always see the same value, but operations that transform that value into a new value always return a new object.

If you want to know if two variables refer to the same object or not, you can use the is operator, or the built-in function id().

## 2.2.10 How do I write a function with output parameters (call by reference)?

Remember that arguments are passed by assignment in Python. Since assignment just creates references to objects, there’s no alias between an argument name in the caller and callee, and so no call-by-reference per se. You can achieve the desired effect in a number of ways.

1) By returning a tuple of the results:

```python
def func2(a, b):
    a = 'new-value'          # a and b are local names
    b = b + 1                  # assigned to new objects
    return a, b              # return new values

x, y = 'old-value', 99
x, y = func2(x, y)
print x, y                     # output: new-value 100
```

<!-- page: 23 -->

This is almost always the clearest solution.

2) By using global variables. This isn’t thread-safe, and is not recommended.

3) By passing a mutable (changeable in-place) object:

```python
def func1(a):
    a[0] = 'new-value'      # 'a' references a mutable list
    a[1] = a[1] + 1          # changes a shared object

args = ['old-value', 99]
func1(args)
print args[0], args[1]     # output: new-value 100
```

4) By passing in a dictionary that gets mutated:

```python
def func3(args):
    args['a'] = 'new-value'      # args is a mutable dictionary
    args['b'] = args['b'] + 1   # change it in-place

args = {'a': 'old-value', 'b': 99}
func3(args)
print args['a'], args['b']
```

5) Or bundle up values in a class instance:

```python
class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)

def func4(args):
    args.a = 'new-value'          # args is a mutable callByRef
    args.b = args.b + 1           # change object in-place

args = callByRef(a='old-value', b=99)
func4(args)
print args.a, args.b
```

There’s almost never a good reason to get this complicated.

Your best choice is to return a tuple containing the multiple results.

## 2.2.11 How do you make a higher order function in Python?

You have two choices: you can use nested scopes or you can use callable objects. For example, suppose you wanted to define linear(a,b) which returns a function f(x) that computes the value a\*x+b. Using nested scopes:

```python
def linear(a, b):
    def result(x):
        return a * x + b
    return result
```

Or using a callable object:

```txt
class linear:
```

(continues on next page)

## 2.2. Core Language

<!-- page: 24 -->

```python
def __init__(self, a, b):
    self.a, self.b = a, b

def __call__(self, x):
    return self.a * x + self.b
```

(continued from previous page)

In both cases,

```txt
taxes = linear(0.3, 2)
```

gives a callable object where taxes(10e6) == 0.3 \* 10e6 + 2.

The callable object approach has the disadvantage that it is a bit slower and results in slightly longer code. However, note that a collection of callables can share their signature via inheritance:

```python
class exponential(linear):
    # __init__ inherited
    def __call__(self, x):
        return self.a * (x ** self.b)
```

Object can encapsulate state for several methods:

```python
class counter:

    value = 0

    def set(self, x):
        self.value = x

    def up(self):
        self.value = self.value + 1

    def down(self):
        self.value = self.value - 1

count = counter()
inc, dec, reset = count.up, count.down, count.set
```

Here inc(), dec() and reset() act like functions which share the same counting variable.

## 2.2.12 How do I copy an object in Python?

In general, try copy.copy() or copy.deepcopy() for the general case. Not all objects can be copied, but most can.

Some objects can be copied more easily. Dictionaries have a copy() method:

```txt
newdict = olddict.copy()
```

Sequences can be copied by slicing:

```python
new_l = l[:]
```

<!-- page: 25 -->

## 2.2.13 How can I find the methods or attributes of an object?

For an instance x of a user-defined class, dir(x) returns an alphabetized list of the names containing the instance attributes and methods and attributes defined by its class.

## 2.2.14 How can my code discover the name of an object?

Generally speaking, it can’t, because objects don’t really have names. Essentially, assignment always binds a name to a value; The same is true of def and class statements, but in that case the value is a callable. Consider the following code:

```python
>>> class A:
...     pass
...
>>> B = A
>>> a = B()
>>> b = a
>>> print b
<__main__.A instance at 0x16D07CC>
>>> print a
<__main__.A instance at 0x16D07CC>
```

Arguably the class has a name: even though it is bound to two names and invoked through the name B the created instance is still reported as an instance of class A. However, it is impossible to say whether the instance’s name is a or b, since both names are bound to the same value.

Generally speaking it should not be necessary for your code to “know the names” of particular values. Unless you are deliberately writing introspective programs, this is usually an indication that a change of approach might be beneficial.

In comp.lang.python, Fredrik Lundh once gave an excellent analogy in answer to this question:

The same way as you get the name of that cat you found on your porch: the cat (object) itself cannot tell you its name, and it doesn’t really care – so the only way to find out what it’s called is to ask all your neighbours (namespaces) if it’s their cat (object)…

….and don’t be surprised if you’ll find that it’s known by many names, or no name at all!

## 2.2.15 What’s up with the comma operator’s precedence?

Comma is not an operator in Python. Consider this session:

```txt
>>> "a" in "b", "a"
(False, 'a')
```

Since the comma is not an operator, but a separator between expressions the above is evaluated as if you had entered:

```python
("a" in "b"), "a"
```

not:

```javascript
"a" in ("b", "a")
```

The same is true of the various assignment operators (=, += etc). They are not truly operators but syntactic delimiters in assignment statements.

<!-- page: 26 -->

## 2.2.16 Is there an equivalent of C’s “?:” ternary operator?

Yes, this feature was added in Python 2.5. The syntax would be as follows:

```ini
[on_true] if [expression] else [on_false]
x, y = 50, 25
small = x if x < y else y
```

For versions previous to 2.5 the answer would be ‘No’.

## 2.2.17 Is it possible to write obfuscated one-liners in Python?

Yes. Usually this is done by nesting lambda within lambda. See the following three examples, due to Ulf Bartelt:

```txt
# Primes < 1000
print filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))

# First 10 Fibonacci numbers
print map(lambda x,f=lambda x,f:(f(x-1,f)+f(x-2,f)) if x>1 else 1: f(x,f),
range(10))

# Mandelbrot set
print (lambda Ru,Ro,Iu,Io,IM,Sx,Sy:reduce(lambda x,y:x+y,map(lambda y,
Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,Sy=Sy,L=lambda yc,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,i=IM,
Sx=Sx,Sy=Sy:reduce(lambda x,y:x+y,map(lambda x,xc=Ru,yc=yc,Ru=Ru,Ro=Ro,
i=i,Sx=Sx,F=lambda xc,yc,x,y,k,f=lambda xc,yc,x,y,k,f:(k<=0)or (x*x+y*y
>=4.0) or 1+f(xc,yc,x*x-y*y+xc,2.0*x*y+yc,k-1,f):f(xc,yc,x,y,k,f):chr(
64+F(Ru+x*(Ro-Ru)/Sx,yc,0,0,i)),range(Sx))):L(Iu+y*(Io-Iu)/Sy),range(Sy
))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 24)
# \____ __/ \____ __/ | | |____ lines on screen
# V V | |____ columns on screen
# | | /____ maximum of "iterations"
# | /____ range on y axis
# |____ range on x axis
```

Don’t try this at home, kids!

## 2.3 Numbers and strings

## 2.3.1 How do I specify hexadecimal and octal integers?

To specify an octal digit, precede the octal value with a zero, and then a lower or uppercase “o”. For example, to set the variable “a” to the octal value “10” (8 in decimal), type:

```txt
>>> a = 0o10
>>> a
8
```

Hexadecimal is just as easy. Simply precede the hexadecimal number with a zero, and then a lower or uppercase “x”. Hexadecimal digits can be specified in lower or uppercase. For example, in the Python interpreter:

<!-- page: 27 -->

```txt
>>> a = 0xa5
>>> a
165
>>> b = 0XB2
>>> b
178
```

## 2.3.2 Why does -22 // 10 return -3?

It’s primarily driven by the desire that i % j have the same sign as j. If you want that, and also want:

```txt
i == (i // j) * j + (i % j)
```

then integer division has to return the floor. C also requires that identity to hold, and then compilers that truncate i // j need to make i % j have the same sign as i.

There are few real use cases for i % j when j is negative. When j is positive, there are many, and in virtually all of them it’s more useful for i % j to be >= 0. If the clock says 10 now, what did it say 200 hours ago? -190 % 12 == 2 is useful; -190 % 12 == -10 is a bug waiting to bite.

**Note:** On Python 2, a / b returns the same as a // b if \_\_future\_\_.division is not in effect. This is also known as “classic” division.

## 2.3.3 How do I convert a string to a number?

For integers, use the built-in int() type constructor, e.g. int('144') == 144. Similarly, float() converts to floating-point, e.g. float('144') == 144.0.

By default, these interpret the number as decimal, so that int('0144') == 144 and int('0x144') raises ValueError. int(string, base) takes the base to convert from as a second optional argument, so int('0x144', 16) == 324. If the base is specified as 0, the number is interpreted using Python’s rules: a leading ‘0’ indicates octal, and ‘0x’ indicates a hex number.

Do not use the built-in function eval() if all you need is to convert strings to numbers. eval() will be significantly slower and it presents a security risk: someone could pass you a Python expression that might have unwanted side effects. For example, someone could pass \_\_import\_\_('os').system("rm -rf \$HOME") which would erase your home directory.

eval() also has the effect of interpreting numbers as Python expressions, so that e.g. eval('09') gives a syntax error because Python regards numbers starting with ‘0’ as octal (base 8).

## 2.3.4 How do I convert a number to a string?

To convert, e.g., the number 144 to the string ‘144’, use the built-in type constructor str(). If you want a hexadecimal or octal representation, use the built-in functions hex() or oct(). For fancy formatting, see the formatstrings section, e.g. "{:04d}".format(144) yields '0144' and "{:.3f}".format(1.0/3.0) yields '0.333'. In Python 2, the division (/) operator returns the floor of the mathematical result of division if the arguments are ints or longs, but it returns a reasonable approximation of the division result if the arguments are floats or complex:

<!-- page: 28 -->

```txt
>>> print('{:.3f}'.format(1/3))
0.000
>>> print('{:.3f}'.format(1.0/3))
0.333
```

In Python 3, the default behaviour of the division operator (see [**PEP 238**](https://www.python.org/dev/peps/pep-0238)) has been changed but you can have the same behaviour in Python 2 if you import division from \_\_future\_\_:

```python
>>> from __future__ import division
>>> print('{:.3f}'.format(1/3))
0.333
```

You may also use the % operator on strings. See the library reference manual for details.

## 2.3.5 How do I modify a string in place?

You can’t, because strings are immutable. If you need an object with this ability, try converting the string to a list or use the array module:

```python
>>> import io
>>> s = "Hello, world"
>>> a = list(s)
>>> print a
['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd']
>>> a[7:] = list("there!")
>>> ''.join(a)
'Hello, there!'

>>> import array
>>> a = array.array('c', s)
>>> print a
array('c', 'Hello, world')
>>> a[0] = 'y'; print a
array('c', 'yello, world')
>>> a.tostring()
'yello, world'
```

## 2.3.6 How do I use strings to call functions/methods?

There are various techniques.

• The best is to use a dictionary that maps strings to functions. The primary advantage of this technique is that the strings do not need to match the names of the functions. This is also the primary technique used to emulate a case construct:

```python
def a():
    pass

def b():
    pass

dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs
dispatch[get_input()]()  # Note trailing parens to call function
```

<!-- page: 29 -->

• Use the built-in function getattr():

```python
import foo
getattr(foo, 'bar')()
```

Note that getattr() works on any object, including classes, class instances, modules, and so on.

This is used in several places in the standard library, like this:

```python
class Foo:
    def do_foo(self):
        ...

    def do_bar(self):
        ...

f = getattr(foo_instance, 'do_' + opname)
f()
```

• Use locals() or eval() to resolve the function name:

```txt
def myFunc():
    print "hello"

fname = "myFunc"

f = locals()[fname]
f()

f = eval(fname)
f()
```

Note: Using eval() is slow and dangerous. If you don’t have absolute control over the contents of the string, someone could pass a string that resulted in an arbitrary function being executed.

## 2.3.7 Is there an equivalent to Perl’s chomp() for removing trailing newlines from strings?

Starting with Python 2.2, you can use S.rstrip("\r\n") to remove all occurrences of any line terminator from the end of the string S without removing other trailing whitespace. If the string S represents more than one line, with several empty lines at the end, the line terminators for all the blank lines will be removed:

```python
>>> lines = ("line 1 \r\n"
...             "\r\n"
...             "\r\n")
>>> lines.rstrip("\\n\r")
'line 1 '
```

Since this is typically only desired when reading text one line at a time, using S.rstrip() this way works well.

For older versions of Python, there are two partial substitutes:

• If you want to remove all trailing whitespace, use the rstrip() method of string objects. This removes all trailing whitespace, not just a single newline.

• Otherwise, if there is only one line in the string S, use S.splitlines()[0].

<!-- page: 30 -->

## 2.3.8 Is there a scanf() or sscanf() equivalent?

Not as such.

For simple input parsing, the easiest approach is usually to split the line into whitespace-delimited words using the split() method of string objects and then convert decimal strings to numeric values using int() or float(). split() supports an optional “sep” parameter which is useful if the line uses something other than whitespace as a separator.

For more complicated input parsing, regular expressions are more powerful than C’s sscanf() and better suited for the task.

## 2.3.9 What does ‘UnicodeError: ASCII [decoding,encoding] error: ordinal not in range(128)’ mean?

This error indicates that your Python installation can handle only 7-bit ASCII strings. There are a couple ways to fix or work around the problem.

If your programs must handle data in arbitrary character set encodings, the environment the application runs in will generally identify the encoding of the data it is handing you. You need to convert the input to Unicode data using that encoding. For example, a program that handles email or web input will typically find character set encoding information in Content-Type headers. This can then be used to properly convert input data to Unicode. Assuming the string referred to by value is encoded as UTF-8:

```txt
value = unicode(value, "utf-8")
```

will return a Unicode object. If the data is not correctly encoded as UTF-8, the above call will raise a UnicodeError exception.

If you only want strings converted to Unicode which have non-ASCII data, you can try converting them first assuming an ASCII encoding, and then generate Unicode objects if that fails:

```python
try:
    x = unicode(value, "ascii")
except UnicodeError:
    value = unicode(value, "utf-8")
else:
    # value was valid ASCII data
    pass
```

It’s possible to set a default encoding in a file called sitecustomize.py that’s part of the Python library. However, this isn’t recommended because changing the Python-wide default encoding may cause third-party extension modules to fail.

Note that on Windows, there is an encoding known as “mbcs”, which uses an encoding specific to your current locale. In many cases, and particularly when working with COM, this may be an appropriate default encoding to use.

<!-- page: 31 -->

## 2.4 Sequences (Tuples/Lists)

## 2.4.1 How do I convert between tuples and lists?

The type constructor tuple(seq) converts any sequence (actually, any iterable) into a tuple with the same items in the same order.

For example, tuple([1, 2, 3]) yields (1, 2, 3) and tuple('abc') yields ('a', 'b', 'c'). If the argument is a tuple, it does not make a copy but returns the same object, so it is cheap to call tuple() when you aren’t sure that an object is already a tuple.

The type constructor list(seq) converts any sequence or iterable into a list with the same items in the same order. For example, list((1, 2, 3)) yields [1, 2, 3] and list('abc') yields ['a', 'b', 'c']. If the argument is a list, it makes a copy just like seq[:] would.

## 2.4.2 What’s a negative index?

Python sequences are indexed with positive numbers and negative numbers. For positive numbers 0 is the first index 1 is the second index and so forth. For negative indices -1 is the last index and -2 is the penultimate (next to last) index and so forth. Think of seq[-n] as the same as seq[len(seq)-n].

Using negative indices can be very convenient. For example S[:-1] is all of the string except for its last character, which is useful for removing the trailing newline from a string.

## 2.4.3 How do I iterate over a sequence in reverse order?

Use the reversed() built-in function, which is new in Python 2.4:

```python
for x in reversed(sequence):
    ...  # do something with x ...
```

This won’t touch your original sequence, but build a new copy with reversed order to iterate over.

With Python 2.3, you can use an extended slice syntax:

```python
for x in sequence[::-1]:
    ...  # do something with x ...
```

## 2.4.4 How do you remove duplicates from a list?

See the Python Cookbook for a long discussion of many ways to do this:

[https://code.activestate.com/recipes/52560/](https://code.activestate.com/recipes/52560/)

If you don’t mind reordering the list, sort it and then scan from the end of the list, deleting duplicates as you go:

```python
if mylist:
    mylist.sort()
    last = mylist[-1]
    for i in range(len(mylist)-2, -1, -1):
        if last == mylist[i]:
            del mylist[i]
        else:
            last = mylist[i]
```

<!-- page: 32 -->

If all elements of the list may be used as dictionary keys (i.e. they are all hashable) this is often faster

```txt
d = {}
for x in mylist:
    d[x] = 1
mylist = list(d.keys())
```

In Python 2.5 and later, the following is possible instead:

```julia
mylist = list(set(mylist))
```

This converts the list into a set, thereby removing duplicates, and then back into a list.

## 2.4.5 How do you make an array in Python?

Use a list:

```txt
["this", 1, "is", "an", "array"]
```

Lists are equivalent to C or Pascal arrays in their time complexity; the primary difference is that a Python list can contain objects of many different types.

The array module also provides methods for creating arrays of fixed types with compact representations, but they are slower to index than lists. Also note that the Numeric extensions and others define array-like structures with various characteristics as well.

To get Lisp-style linked lists, you can emulate cons cells using tuples:

```python
lisp_list = ("like",  ("this",  ("example", None) ) )
```

If mutability is desired, you could use lists instead of tuples. Here the analogue of lisp car is lisp\_list[0] and the analogue of cdr is lisp\_list[1]. Only do this if you’re sure you really need to, because it’s usually a lot slower than using Python lists.

## 2.4.6 How do I create a multidimensional list?

You probably tried to make a multidimensional array like this:

```txt
>>> A = [[None] * 2] * 3
```

This looks correct if you print it:

```json
>>> A
[[None, None], [None, None], [None, None]]
```

But when you assign a value, it shows up in multiple places:

```txt
>>> A[0][0] = 5
>>> A
[[5, None], [5, None], [5, None]]
```

The reason is that replicating a list with \* doesn’t create copies, it only creates references to the existing objects. The \*3 creates a list containing 3 references to the same list of length two. Changes to one row will show in all rows, which is almost certainly not what you want.

The suggested approach is to create a list of the desired length first and then fill in each element with a newly created list:

<!-- page: 33 -->

```python
A = [None] * 3
for i in range(3):
    A[i] = [None] * 2
```

This generates a list containing 3 different lists of length two. You can also use a list comprehension:

```python
w, h = 2, 3
A = [[None] * w for i in range(h)]
```

Or, you can use an extension that provides a matrix datatype; [NumPy](http://www.numpy.org/) is the best known.

## 2.4.7 How do I apply a method to a sequence of objects?

Use a list comprehension:

```txt
result = [obj.method() for obj in mylist]
```

More generically, you can try the following function:

```python
def method_map(objects, method, arguments):
    """method_map([a,b], "meth", (1,2)) gives [a.meth(1,2), b.meth(1,2)]"""
    nobjects = len(objects)
    methods = map(getattr, objects, [method]*nobjects)
    return map(apply, methods, [arguments]*nobjects)
```

## 2.4.8 Why does a\_tuple[i] += [‘item’] raise an exception when the addition works?

This is because of a combination of the fact that augmented assignment operators are assignment operators, and the difference between mutable and immutable objects in Python.

This discussion applies in general when augmented assignment operators are applied to elements of a tuple that point to mutable objects, but we’ll use a list and += as our exemplar.

If you wrote:

```python
>>> a_tuple = (1, 2)
>>> a_tuple[0] += 1
Traceback (most recent call last):
    ...
TypeError: 'tuple' object does not support item assignment
```

The reason for the exception should be immediately clear: 1 is added to the object a\_tuple[0] points to (1), producing the result object, 2, but when we attempt to assign the result of the computation, 2, to element 0 of the tuple, we get an error because we can’t change what an element of a tuple points to.

Under the covers, what this augmented assignment statement is doing is approximately this:

```python
>>> result = a_tuple[0] + 1
>>> a_tuple[0] = result
Traceback (most recent call last):
    ...
TypeError: 'tuple' object does not support item assignment
```

It is the assignment part of the operation that produces the error, since a tuple is immutable.

When you write something like:

## 2.4. Sequences (Tuples/Lists)

<!-- page: 34 -->

```python
>>> a_tuple =(['foo'], 'bar')
>>> a_tuple[0] += ['item']
Traceback (most recent call last):
  ...
TypeError: 'tuple' object does not support item assignment
```

The exception is a bit more surprising, and even more surprising is the fact that even though there was an error, the append worked:

```txt
>>> a_tuple[0]
['foo', 'item']
```

To see why this happens, you need to know that (a) if an object implements an \_\_iadd\_\_ magic method, it gets called when the += augmented assignment is executed, and its return value is what gets used in the assignment statement; and (b) for lists, \_\_iadd\_\_ is equivalent to calling extend on the list and returning the list. That’s why we say that for lists, += is a “shorthand” for list.extend:

```txt
>>> a_list = []
>>> a_list += [1]
>>> a_list
[1]
```

This is equivalent to:

```python
>>> result = a_list.__iadd__([1])
>>> a_list = result
```

The object pointed to by a\_list has been mutated, and the pointer to the mutated object is assigned back to a\_list. The end result of the assignment is a no-op, since it is a pointer to the same object that a\_list was previously pointing to, but the assignment still happens.

Thus, in our tuple example what is happening is equivalent to:

```python
>>> result = a_tuple[0].__iadd_(['item'])
>>> a_tuple[0] = result
Traceback (most recent call last):
  ...
TypeError: 'tuple' object does not support item assignment
```

The \_\_iadd\_\_ succeeds, and thus the list is extended, but even though result points to the same object that a\_tuple[0] already points to, that final assignment still results in an error, because tuples are immutable.

## 2.5 Dictionaries

## 2.5.1 How can I get a dictionary to display its keys in a consistent order?

You can’t. Dictionaries store their keys in an unpredictable order, so the display order of a dictionary’s elements will be similarly unpredictable.

This can be frustrating if you want to save a printable version to a file, make some changes and then compare it with some other printed dictionary. In this case, use the pprint module to pretty-print the dictionary; the items will be presented in order sorted by the key.

A more complicated solution is to subclass dict to create a SortedDict class that prints itself in a predictable order. Here’s one simpleminded implementation of such a class:

<!-- page: 35 -->

```python
class SortedDict(dict):
    def __repr__(self):
        keys = sorted(self.keys())
        result = ("{!r}: {!r}".format(k, self[k]) for k in keys)
        return "{{{}}".format(", ".join(result))

    __str__ = __repr__
```

This will work for many common situations you might encounter, though it’s far from a perfect solution. The largest flaw is that if some values in the dictionary are also dictionaries, their values won’t be presented in any particular order.

## 2.5.2 I want to do a complicated sort: can you do a Schwartzian Transform in Python?

The technique, attributed to Randal Schwartz of the Perl community, sorts the elements of a list by a metric which maps each element to its “sort value”. In Python, use the key argument for the sort() function:

```txt
Isorted = L[:]
Isorted.sort(key=lambda s: int(s[10:15]))
```

## 2.5.3 How can I sort one list by values from another list?

Merge them into a single list of tuples, sort the resulting list, and then pick out the element you want.

```txt
>>> list1 = ["what", "I'm", "sorting", "by"]
>>> list2 = ["something", "else", "to", "sort"]
>>> pairs = zip(list1, list2)
>>> pairs
[('what', 'something'), ("I'm", 'else'), ('sorting', 'to'), ('by', 'sort')]
>>> pairs.sort()
>>> result = [ x[1] for x in pairs ]
>>> result
['else', 'sort', 'to', 'something']
```

An alternative for the last step is:

```txt
>>> result = []
>>> for p in pairs: result.append(p[1])
```

If you find this more legible, you might prefer to use this instead of the final list comprehension. However, it is almost twice as slow for long lists. Why? First, the append() operation has to reallocate memory, and while it uses some tricks to avoid doing that each time, it still has to do it occasionally, and that costs quite a bit. Second, the expression “result.append” requires an extra attribute lookup, and third, there’s a speed reduction from having to make all those function calls.

<!-- page: 36 -->

## 2.6 Objects

## 2.6.1 What is a class?

A class is the particular object type created by executing a class statement. Class objects are used as templates to create instance objects, which embody both the data (attributes) and code (methods) specific to a datatype.

A class can be based on one or more other classes, called its base class(es). It then inherits the attributes and methods of its base classes. This allows an object model to be successively refined by inheritance. You might have a generic Mailbox class that provides basic accessor methods for a mailbox, and subclasses such as MboxMailbox, MaildirMailbox, OutlookMailbox that handle various specific mailbox formats.

## 2.6.2 What is a method?

A method is a function on some object x that you normally call as x.name(arguments...). Methods are defined as functions inside the class definition:

```python
class C:
    def meth(self, arg):
        return arg * 2 + self.attribute
```

## 2.6.3 What is self?

Self is merely a conventional name for the first argument of a method. A method defined as meth(self, a, b, c) should be called as x.meth(a, b, c) for some instance x of the class in which the definition occurs; the called method will think it is called as meth(x, a, b, c).

See also Why must ‘self’ be used explicitly in method definitions and calls?.

## 2.6.4 How do I check if an object is an instance of a given class or of a subclass of it?

Use the built-in function isinstance(obj, cls). You can check if an object is an instance of any of a number of classes by providing a tuple instead of a single class, e.g. isinstance(obj, (class1, class2, ...)), and can also check whether an object is one of Python’s built-in types, e.g. isinstance(obj, str) or isinstance(obj, (int, long, float, complex)).

Note that most programs do not use isinstance() on user-defined classes very often. If you are developing the classes yourself, a more proper object-oriented style is to define methods on the classes that encapsulate a particular behaviour, instead of checking the object’s class and doing a different thing based on what class it is. For example, if you have a function that does something:

```python
def search(obj):
    if isinstance(obj, Mailbox):
        ...  # code to search a mailbox
    elif isinstance(obj, Document):
        ...  # code to search a document
    elif ...
```

A better approach is to define a search() method on all the classes and just call it:

<!-- page: 37 -->

```python
class Mailbox:
    def search(self):
        ...  # code to search a mailbox

class Document:
    def search(self):
        ...  # code to search a document

obj.search()
```

## 2.6.5 What is delegation?

Delegation is an object oriented technique (also called a design pattern). Let’s say you have an object x and want to change the behaviour of just one of its methods. You can create a new class that provides a new implementation of the method you’re interested in changing and delegates all other methods to the corresponding method of x.

Python programmers can easily implement delegation. For example, the following class implements a class that behaves like a file but converts all written data to uppercase:

```python
class UpperOut:

    def __init__(self, outfile):
        self._outfile = outfile

    def write(self, s):
        self._outfile.write(s.upper())

    def __getattr__(self, name):
        return getattr(self._outfile, name)
```

Here the UpperOut class redefines the write() method to convert the argument string to uppercase before calling the underlying self.\_\_outfile.write() method. All other methods are delegated to the underlying self. \_outfile object. The delegation is accomplished via the \_\_getattr\_\_ method; consult the language reference for more information about controlling attribute access.

Note that for more general cases delegation can get trickier. When attributes must be set as well as retrieved, the class must define a \_\_setattr\_\_() method too, and it must do so carefully. The basic implementation of \_\_setattr\_\_() is roughly equivalent to the following:

```python
class X:
    ...
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    ...
```

Most \_\_setattr\_\_() implementations must modify self.\_\_dict\_\_ to store local state for self without causing an infinite recursion.

<!-- page: 38 -->

## 2.6.6 How do I call a method defined in a base class from a derived class that overrides it?

If you’re using new-style classes, use the built-in super() function:

```python
class Derived(Base):
    def meth(self):
        super(Derived, self).meth()
```

If you’re using classic classes: For a class definition such as class Derived(Base): ... you can call method meth() defined in Base (or one of Base’s base classes) as Base.meth(self, arguments...). Here, Base. meth is an unbound method, so you need to provide the self argument.

## 2.6.7 How can I organize my code to make it easier to change the base class?

You could define an alias for the base class, assign the real base class to it before your class definition, and use the alias throughout your class. Then all you have to change is the value assigned to the alias. Incidentally, this trick is also handy if you want to decide dynamically (e.g. depending on availability of resources) which base class to use. Example:

```python
BaseAlias = <real base class>

class Derived(BaseAlias):
    def meth(self):
        BaseAlias.meth(self)
        ...
```

## 2.6.8 How do I create static class data and static class methods?

Both static data and static methods (in the sense of C++ or Java) are supported in Python.

For static data, simply define a class attribute. To assign a new value to the attribute, you have to explicitly use the class name in the assignment:

```python
class C:
    count = 0   # number of times C.__init__ called

    def __init__(self):
        C.count = C.count + 1

    def getcount(self):
        return C.count  # or return self.count
```

c.count also refers to C.count for any c such that isinstance(c, C) holds, unless overridden by c itself or by some class on the base-class search path from c.\_\_class\_\_ back to C.

Caution: within a method of C, an assignment like self.count = 42 creates a new and unrelated instance named “count” in self’s own dict. Rebinding of a class-static data name must always specify the class whether inside a method or not:

```txt
C.count = 314
```

Static methods are possible since Python 2.2:

<!-- page: 39 -->

```python
class C:
    def static(arg1, arg2, arg3):
        # No 'self' parameter!
        ...
    static = staticmethod(static)
```

With Python 2.4’s decorators, this can also be written as

```python
class C:
    @staticmethod
    def static(arg1, arg2, arg3):
        # No 'self' parameter!
        ...
```

However, a far more straightforward way to get the effect of a static method is via a simple module-level function:

```python
def getcount():
    return C.count
```

If your code is structured so as to define one class (or tightly related class hierarchy) per module, this supplies the desired encapsulation.

## 2.6.9 How can I overload constructors (or methods) in Python?

This answer actually applies to all methods, but the question usually comes up first in the context of constructors.

In C++ you’d write

```cpp
class C {
    C() { cout << "No arguments\n"; }
    C(int i) { cout << "Argument is " << i << "\n"; }
}
```

In Python you have to write a single constructor that catches all cases using default arguments. For example:

```python
class C:
    def __init__(self, i=None):
        if i is None:
            print "No arguments"
        else:
            print "Argument is", i
```

This is not entirely equivalent, but close enough in practice.

You could also try a variable-length argument list, e.g.

```python
def __init__(self, *args):
    ...
```

The same approach works for all method definitions.

<!-- page: 40 -->

## 2.6.10 I try to use \_\_spam and I get an error about \_SomeClassName\_\_spam.

Variable names with double leading underscores are “mangled” to provide a simple but effective way to define class private variables. Any identifier of the form \_\_spam (at least two leading underscores, at most one trailing underscore) is textually replaced with \_classname\_\_spam, where classname is the current class name with any leading underscores stripped.

This doesn’t guarantee privacy: an outside user can still deliberately access the “\_classname\_\_spam” attribute, and private values are visible in the object’s \_\_dict\_\_. Many Python programmers never bother to use private variable names at all.

## 2.6.11 My class defines \_\_del\_\_ but it is not called when I delete the object.

There are several possible reasons for this.

The del statement does not necessarily call \_\_del\_\_() – it simply decrements the object’s reference count, and if this reaches zero \_\_del\_\_() is called.

If your data structures contain circular links (e.g. a tree where each child has a parent reference and each parent has a list of children) the reference counts will never go back to zero. Once in a while Python runs an algorithm to detect such cycles, but the garbage collector might run some time after the last reference to your data structure vanishes, so your \_\_del\_\_() method may be called at an inconvenient and random time. This is inconvenient if you’re trying to reproduce a problem. Worse, the order in which object’s \_\_del\_\_() methods are executed is arbitrary. You can run gc.collect() to force a collection, but there are pathological cases where objects will never be collected.

Despite the cycle collector, it’s still a good idea to define an explicit close() method on objects to be called whenever you’re done with them. The close() method can then remove attributes that refer to subobjecs. Don’t call \_\_del\_\_() directly – \_\_del\_\_() should call close() and close() should make sure that it can be called more than once for the same object.

Another way to avoid cyclical references is to use the weakref module, which allows you to point to objects without incrementing their reference count. Tree data structures, for instance, should use weak references for their parent and sibling references (if they need them!).

If the object has ever been a local variable in a function that caught an expression in an except clause, chances are that a reference to the object still exists in that function’s stack frame as contained in the stack trace. Normally, calling sys.exc\_clear() will take care of this by clearing the last recorded exception.

Finally, if your \_\_del\_\_() method raises an exception, a warning message is printed to sys.stderr.

## 2.6.12 How do I get a list of all instances of a given class?

Python does not keep track of all instances of a class (or of a built-in type). You can program the class’s constructor to keep track of all instances by keeping a list of weak references to each instance.

<!-- page: 41 -->

## 2.6.13 Why does the result of id() appear to be not unique?

The id() builtin returns an integer that is guaranteed to be unique during the lifetime of the object. Since in CPython, this is the object’s memory address, it happens frequently that after an object is deleted from memory, the next freshly created object is allocated at the same position in memory. This is illustrated by this example:

```txt
>>> id(1000)
13901272
>>> id(2000)
13901272
```

The two ids belong to different integer objects that are created before, and deleted immediately after execution of the id() call. To be sure that objects whose id you want to examine are still alive, create another reference to the object:

```txt
>>> a = 1000; b = 2000
>>> id(a)
13901272
>>> id(b)
13891296
```

## 2.7 Modules

## 2.7.1 How do I create a .pyc file?

When a module is imported for the first time (or when the source is more recent than the current compiled file) a .pyc file containing the compiled code should be created in the same directory as the .py file.

One reason that a .pyc file may not be created is permissions problems with the directory. This can happen, for example, if you develop as one user but run as another, such as if you are testing with a web server. Creation of a .pyc file is automatic if you’re importing a module and Python has the ability (permissions, free space, etc…) to write the compiled module back to the directory.

Running Python on a top level script is not considered an import and no .pyc will be created. For example, if you have a top-level module foo.py that imports another module xyz.py, when you run foo, xyz.pyc will be created since xyz is imported, but no foo.pyc file will be created since foo.py isn’t being imported.

If you need to create foo.pyc – that is, to create a .pyc file for a module that is not imported – you can, using the py\_compile and compileall modules.

The py\_compile module can manually compile any module. One way is to use the compile() function in that module interactively:

```python
>>> import py_compile
>>> py_compile.compile('foo.py')
```

This will write the .pyc to the same location as foo.py (or you can override that with the optional parameter cfile).

You can also automatically compile all files in a directory or directories using the compileall module. You can do it from the shell prompt by running compileall.py and providing the path of a directory containing Python files to compile:

```batch
python -m compileall .
```

<!-- page: 42 -->

## 2.7.2 How do I find the current module name?

A module can find out its own module name by looking at the predefined global variable \_\_name\_\_. If this has the value \_\_main\_\_', the program is running as a script. Many modules that are usually used by importing them also provide a command-line interface or a self-test, and only execute this code after checking \_\_name\_\_:

```python
def main():
    print 'Running test...'
    ...

if __name__ == '__main__':
    main()
```

## 2.7.3 How can I have modules that mutually import each other?

Suppose you have the following modules:

foo.py:

```python
from bar import bar_var
foo_var = 1
```

bar.py:

```python
from foo import foo_var
bar_var = 2
```

The problem is that the interpreter will perform the following steps:

• main imports foo

• Empty globals for foo are created

• foo is compiled and starts executing

• foo imports bar

• Empty globals for bar are created

• bar is compiled and starts executing

• bar imports foo (which is a no-op since there already is a module named foo)

• bar.foo\_var = foo.foo\_var

The last step fails, because Python isn’t done with interpreting foo yet and the global symbol dictionary for foo is still empty.

The same thing happens when you use import foo, and then try to access foo.foo\_var in global code.

There are (at least) three possible workarounds for this problem.

Guido van Rossum recommends avoiding all uses of from &lt;module&gt; import ..., and placing all code inside functions. Initializations of global variables and class variables should use constants or built-in functions only. This means everything from an imported module is referenced as &lt;module&gt;.&lt;name&gt;.

Jim Roskind suggests performing steps in the following order in each module:

• exports (globals, functions, and classes that don’t need imported base classes)

• import statements

<!-- page: 43 -->

• active code (including globals that are initialized from imported values). van Rossum doesn’t like this approach much because the imports appear in a strange place, but it does work. Matthias Urlichs recommends restructuring your code so that the recursive import is not necessary in the first place. These solutions are not mutually exclusive.

## 2.7.4 \_\_import\_\_(‘x.y.z’) returns &lt;module ‘x’&gt;; how do I get z?

Consider using the convenience function import\_module() from importlib instead:

```python
z = importlib.import_module('x.y.z')
```

## 2.7.5 When I edit an imported module and reimport it, the changes don’t show up. Why does this happen?

For reasons of efficiency as well as consistency, Python only reads the module file on the first time a module is imported. If it didn’t, in a program consisting of many modules where each one imports the same basic module, the basic module would be parsed and re-parsed many times. To force rereading of a changed module, do this:

```txt
import modname
reload(modname)
```

Warning: this technique is not 100% fool-proof. In particular, modules containing statements like

```python
from modname import some_objects
```

will continue to work with the old version of the imported objects. If the module contains class definitions, existing class instances will not be updated to use the new class definition. This can result in the following paradoxical behaviour:

```python
>>> import cls
>>> c = cls.C()                      # Create an instance of C
>>> reload(cls)
<module 'cls' from 'cls.pyc'>
>>> isinstance(c, cls.C)        # isinstance is false?!?
False
```

The nature of the problem is made clear if you print out the class objects:

```txt
>>> c.__class__
<class cls.C at 0x7352a0>
>>> cls.C
<class cls.C at 0x4198d0>
```

<!-- page: 44 -->

<!-- page: 45 -->

## DESIGN AND HISTORY FAQ

## 3.1 Why does Python use indentation for grouping of statements?

Guido van Rossum believes that using indentation for grouping is extremely elegant and contributes a lot to the clarity of the average Python program. Most people learn to love this feature after a while.

Since there are no begin/end brackets there cannot be a disagreement between grouping perceived by the parser and the human reader. Occasionally C programmers will encounter a fragment of code like this:

```txt
if (x <= y)
    x++;
    y--;
z++;
```

Only the x++ statement is executed if the condition is true, but the indentation leads you to believe otherwise. Even experienced C programmers will sometimes stare at it a long time wondering why y is being decremented even for x > y.

Because there are no begin/end brackets, Python is much less prone to coding-style conflicts. In C there are many different ways to place the braces. If you’re used to reading and writing code that uses one style, you will feel at least slightly uneasy when reading (or being required to write) another style.

Many coding styles place begin/end brackets on a line by themselves. This makes programs considerably longer and wastes valuable screen space, making it harder to get a good overview of a program. Ideally, a function should fit on one screen (say, 20–30 lines). 20 lines of Python can do a lot more work than 20 lines of C. This is not solely due to the lack of begin/end brackets – the lack of declarations and the high-level data types are also responsible – but the indentation-based syntax certainly helps.

## 3.2 Why am I getting strange results with simple arithmetic operations?

See the next question.

<!-- page: 46 -->

## 3.3 Why are floating point calculations so inaccurate?

People are often very surprised by results like this:

```txt
>>> 1.2 - 1.0
0.199999999999999996
```

and think it is a bug in Python. It’s not. This has nothing to do with Python, but with how the underlying C platform handles floating point numbers, and ultimately with the inaccuracies introduced when writing down numbers as a string of a fixed number of digits.

The internal representation of floating point numbers uses a fixed number of binary digits to represent a decimal number. Some decimal numbers can’t be represented exactly in binary, resulting in small roundoff errors.

In decimal math, there are many numbers that can’t be represented with a fixed number of decimal digits, e.g. 1/3 = 0.3333333333…….

In base 2, 1/2 = 0.1, 1/4 = 0.01, 1/8 = 0.001, etc. .2 equals 2/10 equals 1/5, resulting in the binary fractional number 0.001100110011001…

Floating point numbers only have 32 or 64 bits of precision, so the digits are cut off at some point, and the resulting number is 0.199999999999999996 in decimal, not 0.2.

A floating point number’s repr() function prints as many digits are necessary to make eval(repr(f)) == f true for any float f. The str() function prints fewer digits and this often results in the more sensible number that was probably intended:

```txt
>>> 1.1 - 0.9
0.20000000000000007
>>> print 1.1 - 0.9
0.2
```

One of the consequences of this is that it is error-prone to compare the result of some computation to a float with ==. Tiny inaccuracies may mean that == fails. Instead, you have to check that the difference between the two numbers is less than a certain threshold:

```python
epsilon = 0.000000000001  # Tiny allowed error
expected_result = 0.4

if expected_result-epsilon <= computation() <= expected_result+epsilon:
    ...
```

Please see the chapter on floating point arithmetic in the Python tutorial for more information.

## 3.4 Why are Python strings immutable?

There are several advantages.

One is performance: knowing that a string is immutable means we can allocate space for it at creation time, and the storage requirements are fixed and unchanging. This is also one of the reasons for the distinction between tuples and lists.

Another advantage is that strings in Python are considered as “elemental” as numbers. No amount of activity will change the value 8 to anything else, and in Python, no amount of activity will change the string “eight” to anything else.

<!-- page: 47 -->

## 3.5 Why must ‘self’ be used explicitly in method definitions and calls?

The idea was borrowed from Modula-3. It turns out to be very useful, for a variety of reasons.

First, it’s more obvious that you are using a method or instance attribute instead of a local variable. Reading self.x or self.meth() makes it absolutely clear that an instance variable or method is used even if you don’t know the class definition by heart. In C++, you can sort of tell by the lack of a local variable declaration (assuming globals are rare or easily recognizable) – but in Python, there are no local variable declarations, so you’d have to look up the class definition to be sure. Some C++ and Java coding standards call for instance attributes to have an m\_ prefix, so this explicitness is still useful in those languages, too.

Second, it means that no special syntax is necessary if you want to explicitly reference or call the method from a particular class. In C++, if you want to use a method from a base class which is overridden in a derived class, you have to use the :: operator – in Python you can write baseclass.methodname(self, &lt;argument list&gt;). This is particularly useful for \_\_init\_\_() methods, and in general in cases where a derived class method wants to extend the base class method of the same name and thus has to call the base class method somehow.

Finally, for instance variables it solves a syntactic problem with assignment: since local variables in Python are (by definition!) those variables to which a value is assigned in a function body (and that aren’t explicitly declared global), there has to be some way to tell the interpreter that an assignment was meant to assign to an instance variable instead of to a local variable, and it should preferably be syntactic (for efficiency reasons). C++ does this through declarations, but Python doesn’t have declarations and it would be a pity having to introduce them just for this purpose. Using the explicit self.var solves this nicely. Similarly, for using instance variables, having to write self.var means that references to unqualified names inside a method don’t have to search the instance’s directories. To put it another way, local variables and instance variables live in two different namespaces, and you need to tell Python which namespace to use.

## 3.6 Why can’t I use an assignment in an expression?

Many people used to C or Perl complain that they want to use this C idiom:

```txt
while (line = readline(f)) {
    // do something with line
}
```

where in Python you’re forced to write this:

```python
while True:
    line = f.readline()
    if not line:
        break
    ...  # do something with line
```

The reason for not allowing assignment in Python expressions is a common, hard-to-find bug in those other languages, caused by this construct:

```txt
if (x = 0) {
    // error handling
}
else {
    // code that only works for nonzero x
}
```

The error is a simple typo: x = 0, which assigns 0 to the variable x, was written while the comparison x == 0 is certainly what was intended.

<!-- page: 48 -->

Many alternatives have been proposed. Most are hacks that save some typing but use arbitrary or cryptic syntax or keywords, and fail the simple criterion for language change proposals: it should intuitively suggest the proper meaning to a human reader who has not yet been introduced to the construct.

An interesting phenomenon is that most experienced Python programmers recognize the while True idiom and don’t seem to be missing the assignment in expression construct much; it’s only newcomers who express a strong desire to add this to the language.

There’s an alternative way of spelling this that seems attractive but is generally less robust than the “while True” solution:

```python
line = f.readline()
while line:
    ...  # do something with line...
    line = f.readline()
```

The problem with this is that if you change your mind about exactly how you get the next line (e.g. you want to change it into sys.stdin.readline()) you have to remember to change two places in your program – the second occurrence is hidden at the bottom of the loop.

The best approach is to use iterators, making it possible to loop through objects using the for statement. For example, in the current version of Python file objects support the iterator protocol, so you can now write simply:

```python
for line in f:
    ...  # do something with line...
```

## 3.7 Why does Python use methods for some functionality (e.g. list.index()) but functions for other (e.g. len(list))?

As Guido said:

(a) For some operations, prefix notation just reads better than postfix – prefix (and infix!) operations have a long tradition in mathematics which likes notations where the visuals help the mathematician thinking about a problem. Compare the easy with which we rewrite a formula like x\*(a+b) into x\*a + x\*b to the clumsiness of doing the same thing using a raw OO notation.

(b) When I read code that says len(x) I know that it is asking for the length of something. This tells me two things: the result is an integer, and the argument is some kind of container. To the contrary, when I read x.len(), I have to already know that x is some kind of container implementing an interface or inheriting from a class that has a standard len(). Witness the confusion we occasionally have when a class that is not implementing a mapping has a get() or keys() method, or something that isn’t a file has a write() method.

—[https://mail.python.org/pipermail/python-3000/2006-November/004643.html](https://mail.python.org/pipermail/python-3000/2006-November/004643.html)

## 3.8 Why is join() a string method instead of a list or tuple method?

Strings became much more like other standard types starting in Python 1.6, when methods were added which give the same functionality that has always been available using the functions of the string module. Most of these new methods have been widely accepted, but the one which appears to make some programmers feel uncomfortable is:

```javascript
", ".join(['1', '2', '4', '8', '16'])
```

which gives the result:

<!-- page: 49 -->

```txt
"1, 2, 4, 8, 16"
```

There are two common arguments against this usage.

The first runs along the lines of: “It looks really ugly using a method of a string literal (string constant)”, to which the answer is that it might, but a string literal is just a fixed value. If the methods are to be allowed on names bound to strings there is no logical reason to make them unavailable on literals.

The second objection is typically cast as: “I am really telling a sequence to join its members together with a string constant”. Sadly, you aren’t. For some reason there seems to be much less difficulty with having split() as a string method, since in that case it is easy to see that

```python
"1, 2, 4, 8, 16".split(", ")
```

is an instruction to a string literal to return the substrings delimited by the given separator (or, by default, arbitrary runs of white space). In this case a Unicode string returns a list of Unicode strings, an ASCII string returns a list of ASCII strings, and everyone is happy.

join() is a string method because in using it you are telling the separator string to iterate over a sequence of strings and insert itself between adjacent elements. This method can be used with any argument which obeys the rules for sequence objects, including any new classes you might define yourself.

Because this is a string method it can work for Unicode strings as well as plain ASCII strings. If join() were a method of the sequence types then the sequence types would have to decide which type of string to return depending on the type of the separator.

If none of these arguments persuade you, then for the moment you can continue to use the join() function from the string module, which allows you to write

```javascript
string.join(['1', '2', '4', '8', '16'], "", ")
```

## 3.9 How fast are exceptions?

A try/except block is extremely efficient if no exceptions are raised. Actually catching an exception is expensive. In versions of Python prior to 2.0 it was common to use this idiom:

```python
try:
    value = mydict[key]
except KeyError:
    mydict[key] = getvalue(key)
    value = mydict[key]
```

This only made sense when you expected the dict to have the key almost all the time. If that wasn’t the case, you coded it like this:

```python
if key in mydict:
    value = mydict[key]
else:
    value = mydict[key] = getvalue(key)
```

**Note:** In Python 2.0 and higher, you can code this as value = mydict.setdefault(key, getvalue(key)).

<!-- page: 50 -->

## 3.10 Why isn’t there a switch or case statement in Python?

You can do this easily enough with a sequence of if... elif... elif... else. There have been some proposals for switch statement syntax, but there is no consensus (yet) on whether and how to do range tests. See [**PEP 275**](https://www.python.org/dev/peps/pep-0275) for complete details and the current status.

For cases where you need to choose from a very large number of possibilities, you can create a dictionary mapping case values to functions to call. For example:

```python
def function_1(...):
    ...

functions = {'a': function_1,
            'b': function_2,
            'c': self.method_1, ...}

func = functions[value]
func()
```

For calling methods on objects, you can simplify yet further by using the getattr() built-in to retrieve methods with a particular name:

```python
def visit_a(self, ...):
    ...
...

def dispatch(self, value):
    method_name = 'visit_' + str(value)
    method = getattr(self, method_name)
    method()
```

It’s suggested that you use a prefix for the method names, such as visit\_ in this example. Without such a prefix, if values are coming from an untrusted source, an attacker would be able to call any method on your object.

## 3.11 Can’t you emulate threads in the interpreter instead of relying on an OS-specific thread implementation?

Answer 1: Unfortunately, the interpreter pushes at least one C stack frame for each Python stack frame. Also, extensions can call back into Python at almost random moments. Therefore, a complete threads implementation requires thread support for C.

Answer 2: Fortunately, there is [Stackless Python](http://www.stackless.com), which has a completely redesigned interpreter loop that avoids the C stack.

<!-- page: 51 -->

## 3.12 Why can’t lambda expressions contain statements?

Python lambda expressions cannot contain statements because Python’s syntactic framework can’t handle statements nested inside expressions. However, in Python, this is not a serious problem. Unlike lambda forms in other languages, where they add functionality, Python lambdas are only a shorthand notation if you’re too lazy to define a function.

Functions are already first class objects in Python, and can be declared in a local scope. Therefore the only advantage of using a lambda instead of a locally-defined function is that you don’t need to invent a name for the function – but that’s just a local variable to which the function object (which is exactly the same type of object that a lambda expression yields) is assigned!

## 3.13 Can Python be compiled to machine code, C or some other language?

[Cython](http://cython.org/) compiles a modified version of Python with optional annotations into C extensions. [Nuitka](http://www.nuitka.net/) is an up-and-coming compiler of Python into C++ code, aiming to support the full Python language. For compiling to Java you can consider [VOC](https://voc.readthedocs.io).

## 3.14 How does Python manage memory?

The details of Python memory management depend on the implementation. The standard C implementation of Python uses reference counting to detect inaccessible objects, and another mechanism to collect reference cycles, periodically executing a cycle detection algorithm which looks for inaccessible cycles and deletes the objects involved. The gc module provides functions to perform a garbage collection, obtain debugging statistics, and tune the collector’s parameters.

Jython relies on the Java runtime so the JVM’s garbage collector is used. This difference can cause some subtle porting problems if your Python code depends on the behavior of the reference counting implementation.

Sometimes objects get stuck in tracebacks temporarily and hence are not deallocated when you might expect. Clear the tracebacks with:

```python
import sys
sys.exc_clear()
sys.exc_traceback = sys.last_traceback = None
```

Tracebacks are used for reporting errors, implementing debuggers and related things. They contain a portion of the program state extracted during the handling of an exception (usually the most recent exception).

In the absence of circularities and tracebacks, Python programs do not need to manage memory explicitly.

Why doesn’t Python use a more traditional garbage collection scheme? For one thing, this is not a C standard feature and hence it’s not portable. (Yes, we know about the Boehm GC library. It has bits of assembler code for most common platforms, not for all of them, and although it is mostly transparent, it isn’t completely transparent; patches are required to get Python to work with it.)

Traditional GC also becomes a problem when Python is embedded into other applications. While in a standalone Python it’s fine to replace the standard malloc() and free() with versions provided by the GC library, an application embedding Python may want to have its own substitute for malloc() and free(), and may not want Python’s. Right now, Python works with anything that implements malloc() and free() properly.

In Jython, the following code (which is fine in CPython) will probably run out of file descriptors long before it runs out of memory:

<!-- page: 52 -->

```python
for file in very_long_list_of_files:
    f = open(file)
    c = f.read(1)
```

Using the current reference counting and destructor scheme, each new assignment to f closes the previous file. Using GC, this is not guaranteed. If you want to write code that will work with any Python implementation, you should explicitly close the file or use the with statement; this will work regardless of GC:

```python
for file in very_long_list_of_files:
    with open(file) as f:
        c = f.read(1)
```

## 3.15 Why isn’t all memory freed when Python exits?

Objects referenced from the global namespaces of Python modules are not always deallocated when Python exits. This may happen if there are circular references. There are also certain bits of memory that are allocated by the C library that are impossible to free (e.g. a tool like Purify will complain about these). Python is, however, aggressive about cleaning up memory on exit and does try to destroy every single object.

If you want to force Python to delete certain things on deallocation use the atexit module to run a function that will force those deletions.

## 3.16 Why are there separate tuple and list data types?

Lists and tuples, while similar in many respects, are generally used in fundamentally different ways. Tuples can be thought of as being similar to Pascal records or C structs; they’re small collections of related data which may be of different types which are operated on as a group. For example, a Cartesian coordinate is appropriately represented as a tuple of two or three numbers.

Lists, on the other hand, are more like arrays in other languages. They tend to hold a varying number of objects all of which have the same type and which are operated on one-by-one. For example, os.listdir('.') returns a list of strings representing the files in the current directory. Functions which operate on this output would generally not break if you added another file or two to the directory.

Tuples are immutable, meaning that once a tuple has been created, you can’t replace any of its elements with a new value. Lists are mutable, meaning that you can always change a list’s elements. Only immutable elements can be used as dictionary keys, and hence only tuples and not lists can be used as keys.

## 3.17 How are lists implemented in CPython?

CPython’s lists are really variable-length arrays, not Lisp-style linked lists. The implementation uses a contiguous array of references to other objects, and keeps a pointer to this array and the array’s length in a list head structure.

This makes indexing a list a[i] an operation whose cost is independent of the size of the list or the value of the index.

When items are appended or inserted, the array of references is resized. Some cleverness is applied to improve the performance of appending items repeatedly; when the array must be grown, some extra space is allocated so the next few times don’t require an actual resize.

<!-- page: 53 -->

## 3.18 How are dictionaries implemented in CPython?

CPython’s dictionaries are implemented as resizable hash tables. Compared to B-trees, this gives better performance for lookup (the most common operation by far) under most circumstances, and the implementation is simpler.

Dictionaries work by computing a hash code for each key stored in the dictionary using the hash() built-in function. The hash code varies widely depending on the key; for example, “Python” hashes to -539294296 while “python”, a string that differs by a single bit, hashes to 1142331976. The hash code is then used to calculate a location in an internal array where the value will be stored. Assuming that you’re storing keys that all have different hash values, this means that dictionaries take constant time – O(1), in computer science notation – to retrieve a key. It also means that no sorted order of the keys is maintained, and traversing the array as the .keys() and .items() do will output the dictionary’s content in some arbitrary jumbled order.

## 3.19 Why must dictionary keys be immutable?

The hash table implementation of dictionaries uses a hash value calculated from the key value to find the key. If the key were a mutable object, its value could change, and thus its hash could also change. But since whoever changes the key object can’t tell that it was being used as a dictionary key, it can’t move the entry around in the dictionary. Then, when you try to look up the same object in the dictionary it won’t be found because its hash value is different. If you tried to look up the old value it wouldn’t be found either, because the value of the object found in that hash bin would be different.

If you want a dictionary indexed with a list, simply convert the list to a tuple first; the function tuple(L) creates a tuple with the same entries as the list L. Tuples are immutable and can therefore be used as dictionary keys.

Some unacceptable solutions that have been proposed:

• Hash lists by their address (object ID). This doesn’t work because if you construct a new list with the same value it won’t be found; e.g.:

```lua
mydict = {[1, 2]: '12'}
print mydict[[1, 2]]
```

would raise a KeyError exception because the id of the [1, 2] used in the second line differs from that in the first line. In other words, dictionary keys should be compared using ==, not using is.

• Make a copy when using a list as a key. This doesn’t work because the list, being a mutable object, could contain a reference to itself, and then the copying code would run into an infinite loop.

• Allow lists as keys but tell the user not to modify them. This would allow a class of hard-to-track bugs in programs when you forgot or modified a list by accident. It also invalidates an important invariant of dictionaries: every value in d.keys() is usable as a key of the dictionary.

• Mark lists as read-only once they are used as a dictionary key. The problem is that it’s not just the top-level object that could change its value; you could use a tuple containing a list as a key. Entering anything as a key into a dictionary would require marking all objects reachable from there as read-only – and again, self-referential objects could cause an infinite loop.

There is a trick to get around this if you need to, but use it at your own risk: You can wrap a mutable structure inside a class instance which has both a \_\_eq\_\_() and a \_\_hash\_\_() method. You must then make sure that the hash value for all such wrapper objects that reside in a dictionary (or other hash based structure), remain fixed while the object is in the dictionary (or other structure).

```python
class ListWrapper:
    def __init__(self, the_list):
        self.the_list = the_list
```

(continues on next page)

<!-- page: 54 -->

(continued from previous page)

```python
def __eq__(self, other):
    return self.the_list == other.the_list

def __hash__(self):
    l = self.the_list
    result = 98767 - len(l)*555
    for i, el in enumerate(l):
        try:
            result = result + (hash(el) % 9999999) * 1001 + i
        except Exception:
            result = (result % 7777777) + i * 333
    return result
```

Note that the hash computation is complicated by the possibility that some members of the list may be unhashable and also by the possibility of arithmetic overflow.

Furthermore it must always be the case that if o1 == o2 (ie o1.\_\_eq\_\_(o2) is True) then hash(o1) == hash(o2) (ie, o1.\_\_hash\_\_() == o2.\_\_hash\_\_()), regardless of whether the object is in a dictionary or not. If you fail to meet these restrictions dictionaries and other hash based structures will misbehave.

In the case of ListWrapper, whenever the wrapper object is in a dictionary the wrapped list must not change to avoid anomalies. Don’t do this unless you are prepared to think hard about the requirements and the consequences of not meeting them correctly. Consider yourself warned.

## 3.20 Why doesn’t list.sort() return the sorted list?

In situations where performance matters, making a copy of the list just to sort it would be wasteful. Therefore, list. sort() sorts the list in place. In order to remind you of that fact, it does not return the sorted list. This way, you won’t be fooled into accidentally overwriting a list when you need a sorted copy but also need to keep the unsorted version around.

In Python 2.4 a new built-in function – sorted() – has been added. This function creates a new list from a provided iterable, sorts it and returns it. For example, here’s how to iterate over the keys of a dictionary in sorted order:

```python
for key in sorted(mydict):
    ...  # do whatever with mydict[key]...
```

## 3.21 How do you specify and enforce an interface spec in Python?

An interface specification for a module as provided by languages such as C++ and Java describes the prototypes for the methods and functions of the module. Many feel that compile-time enforcement of interface specifications helps in the construction of large programs.

Python 2.6 adds an abc module that lets you define Abstract Base Classes (ABCs). You can then use isinstance() and issubclass() to check whether an instance or a class implements a particular ABC. The collections module defines a set of useful ABCs such as Iterable, Container, and MutableMapping.

For Python, many of the advantages of interface specifications can be obtained by an appropriate test discipline for components. There is also a tool, PyChecker, which can be used to find problems due to subclassing.

A good test suite for a module can both provide a regression test and serve as a module interface specification and a set of examples. Many Python modules can be run as a script to provide a simple “self test.” Even modules which use complex external interfaces can often be tested in isolation using trivial “stub” emulations of the external interface. The doctest

<!-- page: 55 -->

and unittest modules or third-party test frameworks can be used to construct exhaustive test suites that exercise every line of code in a module.

An appropriate testing discipline can help build large complex applications in Python as well as having interface specifications would. In fact, it can be better because an interface specification cannot test certain properties of a program. For example, the append() method is expected to add new elements to the end of some internal list; an interface specification cannot test that your append() implementation will actually do this correctly, but it’s trivial to check this property in a test suite.

Writing test suites is very helpful, and you might want to design your code with an eye to making it easily tested. One increasingly popular technique, test-directed development, calls for writing parts of the test suite first, before you write any of the actual code. Of course Python allows you to be sloppy and not write test cases at all.

## 3.22 Why is there no goto?

You can use exceptions to provide a “structured goto” that even works across function calls. Many feel that exceptions can conveniently emulate all reasonable uses of the “go” or “goto” constructs of C, Fortran, and other languages. For example:

```python
class label: pass  # declare a label

try:
    ...
    if condition: raise label()  # goto label
    ...
except label:  # where to goto
    pass
...
```

This doesn’t allow you to jump into the middle of a loop, but that’s usually considered an abuse of goto anyway. Use sparingly.

## 3.23 Why can’t raw strings (r-strings) end with a backslash?

More precisely, they can’t end with an odd number of backslashes: the unpaired backslash at the end escapes the closing quote character, leaving an unterminated string.

Raw strings were designed to ease creating input for processors (chiefly regular expression engines) that want to do their own backslash escape processing. Such processors consider an unmatched trailing backslash to be an error anyway, so raw strings disallow that. In return, they allow you to pass on the string quote character by escaping it with a backslash. These rules work well when r-strings are used for their intended purpose.

If you’re trying to build Windows pathnames, note that all Windows system calls accept forward slashes too:

```python
f = open("/mydir/file.txt")  # works fine!
```

If you’re trying to build a pathname for a DOS command, try e.g. one of

```txt
dir = r"\this\is\my\dos\dir" "\\"
dir = r"\this\is\my\dos\dir" "[:-1]
dir = "\\this\is\my\dos\dir\"
```

<!-- page: 56 -->

## 3.24 Why doesn’t Python have a “with” statement for attribute assignments?

Python has a ‘with’ statement that wraps the execution of a block, calling code on the entrance and exit from the block. Some language have a construct that looks like this:

```python
with obj:
    a = 1          # equivalent to obj.a = 1
    total = total + 1   # obj.total = obj.total + 1
```

In Python, such a construct would be ambiguous.

Other languages, such as Object Pascal, Delphi, and C++, use static types, so it’s possible to know, in an unambiguous way, what member is being assigned to. This is the main point of static typing – the compiler always knows the scope of every variable at compile time.

Python uses dynamic types. It is impossible to know in advance which attribute will be referenced at runtime. Member attributes may be added or removed from objects on the fly. This makes it impossible to know, from a simple reading, what attribute is being referenced: a local one, a global one, or a member attribute?

For instance, take the following incomplete snippet:

```python
def foo(a):
    with a:
        print x
```

The snippet assumes that “a” must have a member attribute called “x”. However, there is nothing in Python that tells the interpreter this. What should happen if “a” is, let us say, an integer? If there is a global variable named “x”, will it be used inside the with block? As you see, the dynamic nature of Python makes such choices much harder.

The primary benefit of “with” and similar language features (reduction of code volume) can, however, easily be achieved in Python by assignment. Instead of:

```javascript
function(args).mydict[index][index].a = 21
function(args).mydict[index][index].b = 42
function(args).mydict[index][index].c = 63
```

write this:

```txt
ref = function(args).mydict[index][index]
ref.a = 21
ref.b = 42
ref.c = 63
```

This also has the side-effect of increasing execution speed because name bindings are resolved at run-time in Python, and the second version only needs to perform the resolution once.

<!-- page: 57 -->

## 3.25 Why are colons required for the if/while/def/class statements?

The colon is required primarily to enhance readability (one of the results of the experimental ABC language). Consider this:

```txt
if a == b
    print a
```

versus

```python
if a == b:
    print a
```

Notice how the second one is slightly easier to read. Notice further how a colon sets off the example in this FAQ answer; it’s a standard usage in English.

Another minor reason is that the colon makes it easier for editors with syntax highlighting; they can look for colons to decide when indentation needs to be increased instead of having to do a more elaborate parsing of the program text.

## 3.26 Why does Python allow commas at the end of lists and tuples?

Python lets you add a trailing comma at the end of lists, tuples, and dictionaries:

```python
[1, 2, 3,]
('a', 'b', 'c',)
d = {
    "A": [1, 5],
    "B": [6, 7],  # last trailing comma is optional but good style
}
```

There are several reasons to allow this.

When you have a literal value for a list, tuple, or dictionary spread across multiple lines, it’s easier to add more elements because you don’t have to remember to add a comma to the previous line. The lines can also be reordered without creating a syntax error.

Accidentally omitting the comma can lead to errors that are hard to diagnose. For example:

```hcl
x = [
    "fee",
    "fie"
    "foo",
    "fum"
]
```

This list looks like it has four elements, but it actually contains three: “fee”, “fiefoo” and “fum”. Always adding the comma avoids this source of error.

Allowing the trailing comma may also make programmatic code generation easier.

<!-- page: 58 -->

<!-- page: 59 -->

# LIBRARY AND EXTENSION FAQ

## 4.1 General Library Questions

## 4.1.1 How do I find a module or application to perform task X?

Check the Library Reference to see if there’s a relevant standard library module. (Eventually you’ll learn what’s in the standard library and will be able to skip this step.)

For third-party packages, search the [Python Package Index](https://pypi.org) or try [Google](https://www.google.com) or another Web search engine. Searching for “Python” plus a keyword or two for your topic of interest will usually find something helpful.

## 4.1.2 Where is the math.py (socket.py, regex.py, etc.) source file?

If you can’t find a source file for a module it may be a built-in or dynamically loaded module implemented in C, C++ or other compiled language. In this case you may not have the source file or it may be something like mathmodule.c, somewhere in a C source directory (not on the Python Path).

There are (at least) three kinds of modules in Python:

1) modules written in Python (.py);

2) modules written in C and dynamically loaded (.dll, .pyd, .so, .sl, etc);

3) modules written in C and linked with the interpreter; to get a list of these, type:

```python
import sys
print sys.builtin_module_names
```

## 4.1.3 How do I make a Python script executable on Unix?

You need to do two things: the script file’s mode must be executable and the first line must begin with #! followed by the path of the Python interpreter.

The first is done by executing chmod +x scriptfile or perhaps chmod 755 scriptfile.

The second can be done in a number of ways. The most straightforward way is to write

```txt
#!/usr/local/bin/python
```

as the very first line of your file, using the pathname for where the Python interpreter is installed on your platform.

If you would like the script to be independent of where the Python interpreter lives, you can use the **env** program. Almost all Unix variants support the following, assuming the Python interpreter is in a directory on the user’s PATH:

<!-- page: 60 -->

```txt
#!/usr/bin/env python
```

Don’t do this for CGI scripts. The PATH variable for CGI scripts is often very minimal, so you need to use the actual absolute pathname of the interpreter.

Occasionally, a user’s environment is so full that the **/usr/bin/env** program fails; or there’s no env program at all. In that case, you can try the following hack (due to Alex Rezinsky):

```shell
#!/bin/sh
""":"
exec python $0 ${1+"$@"
"""
```

The minor disadvantage is that this defines the script’s \_\_doc\_\_ string. However, you can fix that by adding

```python
__doc__ = """....Whatever..."""
```

## 4.1.4 Is there a curses/termcap package for Python?

For Unix variants the standard Python source distribution comes with a curses module in the [Modules](https://github.com/python/cpython/tree/2.7/Modules) subdirectory, though it’s not compiled by default. (Note that this is not available in the Windows distribution – there is no curses module for Windows.)

The curses module supports basic curses features as well as many additional functions from ncurses and SYSV curses such as colour, alternative character set support, pads, and mouse support. This means the module isn’t compatible with operating systems that only have BSD curses, but there don’t seem to be any currently maintained OSes that fall into this category.

For Windows: use [the consolelib module](http://effbot.org/zone/console-index.htm).

## 4.1.5 Is there an equivalent to C’s onexit() in Python?

The atexit module provides a register function that is similar to C’s onexit().

## 4.1.6 Why don’t my signal handlers work?

The most common problem is that the signal handler is declared with the wrong argument list. It is called as

```txt
handler(signum, frame)
```

so it should be declared with two arguments:

```python
def handler(signum, frame):
    ...
```

<!-- page: 61 -->

## 4.2 Common tasks

## 4.2.1 How do I test a Python program or component?

Python comes with two testing frameworks. The doctest module finds examples in the docstrings for a module and runs them, comparing the output with the expected output given in the docstring.

The unittest module is a fancier testing framework modelled on Java and Smalltalk testing frameworks.

To make testing easier, you should use good modular design in your program. Your program should have almost all functionality encapsulated in either functions or class methods – and this sometimes has the surprising and delightful effect of making the program run faster (because local variable accesses are faster than global accesses). Furthermore the program should avoid depending on mutating global variables, since this makes testing much more difficult to do.

The “global main logic” of your program may be as simple as

```python
if __name__ == "__main__":
    main_logic()
```

at the bottom of the main module of your program.

Once your program is organized as a tractable collection of functions and class behaviours you should write test functions that exercise the behaviours. A test suite that automates a sequence of tests can be associated with each module. This sounds like a lot of work, but since Python is so terse and flexible it’s surprisingly easy. You can make coding much more pleasant and fun by writing your test functions in parallel with the “production code”, since this makes it easy to find bugs and even design flaws earlier.

“Support modules” that are not intended to be the main module of a program may include a self-test of the module.

```python
if __name__ == "__main__":
    self_test()
```

Even programs that interact with complex external interfaces may be tested when the external interfaces are unavailable by using “fake” interfaces implemented in Python.

## 4.2.2 How do I create documentation from doc strings?

The pydoc module can create HTML from the doc strings in your Python source code. An alternative for creating API documentation purely from docstrings is [epydoc](http://epydoc.sourceforge.net/). [Sphinx](http://sphinx-doc.org) can also include docstring content.

## 4.2.3 How do I get a single keypress at a time?

For Unix variants there are several solutions. It’s straightforward to do this using curses, but curses is a fairly large module to learn. Here’s a solution without curses:

```python
import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
```

(continues on next page)

<!-- page: 62 -->

```python
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            print "Got character", repr(c)
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
```

(continued from previous page)

You need the termios and the fcntl module for any of this to work, and I’ve only tried it on Linux, though it should work elsewhere. In this code, characters are read and printed one at a time.

termios.tcsetattr() turns off stdin’s echoing and disables canonical mode. fcntl.fnctl() is used to obtain stdin’s file descriptor flags and modify them for non-blocking mode. Since reading stdin when it is empty results in an IOError, this error is caught and ignored.

## 4.3 Threads

## 4.3.1 How do I program using threads?

Be sure to use the threading module and not the thread module. The threading module builds convenient abstractions on top of the low-level primitives provided by the thread module.

Aahz has a set of slides from his threading tutorial that are helpful; see [http://www.pythoncraft.com/OSCON2001/](http://www.pythoncraft.com/OSCON2001/).

## 4.3.2 None of my threads seem to run: why?

As soon as the main thread exits, all threads are killed. Your main thread is running too quickly, giving the threads no time to do any work.

A simple fix is to add a sleep to the end of the program that’s long enough for all the threads to finish:

```python
import threading, time

def thread_task(name, n):
    for i in range(n): print name, i

for i in range(10):
    T = threading.Thread(target=thread_task, args=(str(i), i))
    T.start()

time.sleep(10) # <-----------------!
```

But now (on many platforms) the threads don’t run in parallel, but appear to run sequentially, one at a time! The reason is that the OS thread scheduler doesn’t start a new thread until the previous thread is blocked.

A simple fix is to add a tiny sleep to the start of the run function:

```python
def thread_task(name, n):
    time.sleep(0.001) # <-----------------!
```

(continues on next page)

<!-- page: 63 -->

```python
for i in range(n): print name, i

for i in range(10):
    T = threading.Thread(target=thread_task, args=(str(i), i))
    T.start()

time.sleep(10)
```

(continued from previous page)

Instead of trying to guess a good delay value for time.sleep(), it’s better to use some kind of semaphore mechanism. One idea is to use the Queue module to create a queue object, let each thread append a token to the queue when it finishes, and let the main thread read as many tokens from the queue as there are threads.

## 4.3.3 How do I parcel out work among a bunch of worker threads?

Use the Queue module to create a queue containing a list of jobs. The Queue class maintains a list of objects and has a .put(obj) method that adds items to the queue and a .get() method to return them. The class will take care of the locking necessary to ensure that each job is handed out exactly once.

Here’s a trivial example:

```python
import threading, Queue, time

# The worker thread gets jobs off the queue.  When the queue is empty, it
# assumes there will be no more work and exits.
# (Realistically workers will run until terminated.)
def worker():
    print 'Running worker'
    time.sleep(0.1)
    while True:
        try:
            arg = q.get(block=False)
        except Queue.Empty:
            print 'Worker', threading.currentThread(),
            print 'queue empty'
            break
        else:
            print 'Worker', threading.currentThread(),
            print 'running with argument', arg
            time.sleep(0.5)

# Create queue
q = Queue.Queue()

# Start a pool of 5 workers
for i in range(5):
    t = threading.Thread(target=worker, name='worker %i' % (i+1))
    t.start()

# Begin adding work to the queue
for i in range(50):
    q.put(i)

# Give threads time to run
print 'Main thread sleeping'
time.sleep(5)
```

## 4.3. Threads

<!-- page: 64 -->

When run, this will produce the following output:

```txt
Running worker
Running worker
Running worker
Running worker
Running worker
Main thread sleeping
Worker <Thread(worker 1, started)> running with argument 0
Worker <Thread(worker 2, started)> running with argument 1
Worker <Thread(worker 3, started)> running with argument 2
Worker <Thread(worker 4, started)> running with argument 3
Worker <Thread(worker 5, started)> running with argument 4
Worker <Thread(worker 1, started)> running with argument 5
...
```

Consult the module’s documentation for more details; the Queue class provides a featureful interface.

## 4.3.4 What kinds of global value mutation are thread-safe?

A global interpreter lock (GIL) is used internally to ensure that only one thread runs in the Python VM at a time. In general, Python offers to switch among threads only between bytecode instructions; how frequently it switches can be set via sys.setcheckinterval(). Each bytecode instruction and therefore all the C implementation code reached from each instruction is therefore atomic from the point of view of a Python program.

In theory, this means an exact accounting requires an exact understanding of the PVM bytecode implementation. In practice, it means that operations on shared variables of built-in data types (ints, lists, dicts, etc) that “look atomic” really are.

For example, the following operations are all atomic (L, L1, L2 are lists, D, D1, D2 are dicts, x, y are objects, i, j are ints):

```python
L.append(x)
L1.extend(L2)
x = L[i]
x = L.pop()
L1[i:j] = L2
L.sort()
x = y
x.field = y
D[x] = y
D1.update(D2)
D.keys()
```

These aren’t:

```txt
i = i+1
L.append(L[-1])
L[i] = L[j]
D[x] = D[x] + 1
```

Operations that replace other objects may invoke those other objects’ \_\_del\_\_() method when their reference count reaches zero, and that can affect things. This is especially true for the mass updates to dictionaries and lists. When in doubt, use a mutex!

<!-- page: 65 -->

## 4.3.5 Can’t we get rid of the Global Interpreter Lock?

The global interpreter lock (GIL) is often seen as a hindrance to Python’s deployment on high-end multiprocessor server machines, because a multi-threaded Python program effectively only uses one CPU, due to the insistence that (almost) all Python code can only run while the GIL is held.

Back in the days of Python 1.5, Greg Stein actually implemented a comprehensive patch set (the “free threading” patches) that removed the GIL and replaced it with fine-grained locking. Unfortunately, even on Windows (where locks are very efficient) this ran ordinary Python code about twice as slow as the interpreter using the GIL. On Linux the performance loss was even worse because pthread locks aren’t as efficient.

Since then, the idea of getting rid of the GIL has occasionally come up but nobody has found a way to deal with the expected slowdown, and users who don’t use threads would not be happy if their code ran at half the speed. Greg’s free threading patch set has not been kept up-to-date for later Python versions.

This doesn’t mean that you can’t make good use of Python on multi-CPU machines! You just have to be creative with dividing the work up between multiple processes rather than multiple threads. Judicious use of C extensions will also help; if you use a C extension to perform a time-consuming task, the extension can release the GIL while the thread of execution is in the C code and allow other threads to get some work done.

It has been suggested that the GIL should be a per-interpreter-state lock rather than truly global; interpreters then wouldn’t be able to share objects. Unfortunately, this isn’t likely to happen either. It would be a tremendous amount of work, because many object implementations currently have global state. For example, small integers and short strings are cached; these caches would have to be moved to the interpreter state. Other object types have their own free list; these free lists would have to be moved to the interpreter state. And so on.

And I doubt that it can even be done in finite time, because the same problem exists for 3rd party extensions. It is likely that 3rd party extensions are being written at a faster rate than you can convert them to store all their global state in the interpreter state.

And finally, once you have multiple interpreters not sharing any state, what have you gained over running each interpreter in a separate process?

## 4.4 Input and Output

## 4.4.1 How do I delete a file? (And other file questions…)

Use os.remove(filename) or os.unlink(filename); for documentation, see the os module. The two functions are identical; unlink() is simply the name of the Unix system call for this function.

To remove a directory, use os.rmdir(); use os.mkdir() to create one. os.makedirs(path) will create any intermediate directories in path that don’t exist. os.removedirs(path) will remove intermediate directories as long as they’re empty; if you want to delete an entire directory tree and its contents, use shutil.rmtree().

To rename a file, use os.rename(old\_path, new\_path).

To truncate a file, open it using f = open(filename, "r+"), and use f.truncate(offset); offset defaults to the current seek position. There’s also os.ftruncate(fd, offset) for files opened with os.open(), where fd is the file descriptor (a small integer).

The shutil module also contains a number of functions to work on files including copyfile(), copytree(), and rmtree().

<!-- page: 66 -->

## 4.4.2 How do I copy a file?

The shutil module contains a copyfile() function. Note that on MacOS 9 it doesn’t copy the resource fork and Finder info.

## 4.4.3 How do I read (or write) binary data?

To read or write complex binary data formats, it’s best to use the struct module. It allows you to take a string containing binary data (usually numbers) and convert it to Python objects; and vice versa.

For example, the following code reads two 2-byte integers and one 4-byte integer in big-endian format from a file:

```python
import struct

f = open(filename, "rb")  # Open in binary mode for portability
s = f.read(8)
x, y, z = struct.unpack(">hhl", s)
```

The ‘>’ in the format string forces big-endian data; the letter ‘h’ reads one “short integer” (2 bytes), and ‘l’ reads one “long integer” (4 bytes) from the string.

For data that is more regular (e.g. a homogeneous list of ints or floats), you can also use the array module.

## 4.4.4 I can’t seem to use os.read() on a pipe created with os.popen(); why?

os.read() is a low-level function which takes a file descriptor, a small integer representing the opened file. os. popen() creates a high-level file object, the same type returned by the built-in open() function. Thus, to read n bytes from a pipe p created with os.popen(), you need to use p.read(n).

## 4.4.5 How do I run a subprocess with pipes connected to both input and output?

Use the popen2 module. For example:

```python
import popen2
fromchild, tochild = popen2.popen2("command")
tochild.write("input\n")
tochild.flush()
output = fromchild.readline()
```

Warning: in general it is unwise to do this because you can easily cause a deadlock where your process is blocked waiting for output from the child while the child is blocked waiting for input from you. This can be caused by the parent expecting the child to output more text than it does or by data being stuck in stdio buffers due to lack of flushing. The Python parent can of course explicitly flush the data it sends to the child before it reads any output, but if the child is a naive C program it may have been written to never explicitly flush its output, even if it is interactive, since flushing is normally automatic.

Note that a deadlock is also possible if you use popen3() to read stdout and stderr. If one of the two is too large for the internal buffer (increasing the buffer size does not help) and you read() the other one first, there is a deadlock, too.

Note on a bug in popen2: unless your program calls wait() or waitpid(), finished child processes are never removed, and eventually calls to popen2 will fail because of a limit on the number of child processes. Calling os.waitpid() with the os.WNOHANG option can prevent this; a good place to insert such a call would be before calling popen2 again.

In many cases, all you really need is to run some data through a command and get the result back. Unless the amount of data is very large, the easiest way to do this is to write it to a temporary file and run the command with that temporary file as input. The standard module tempfile exports a mktemp() function to generate unique temporary file names.

<!-- page: 67 -->

```python
import tempfile
import os

class Popen3:
    """
    This is a deadlock-safe version of popen that returns
    an object with errorlevel, out (a string) and err (a string).
    (capturestderr may not work under windows.)
    Example: print Popen3('grep spam','\n\nhere spam\n\n').out
    """
    def __init__(self,command,input=None,capturestderr=None):
        outfile=tempfile.mktemp()
        command="( %s ) > %s" % (command,outfile)
        if input:
            infile=tempfile.mktemp()
            open(infile,"w").write(input)
            command=command+" <+infile
        if capturestderr:
            errfile=tempfile.mktemp()
            command=command+" 2>+errfile
        self.errorlevel=os.system(command) >> 8
        self.out=open(outfile,"r").read()
        os.remove(outfile)
        if input:
            os.remove(infile)
        if capturestderr:
            self.err=open(errfile,"r").read()
            os.remove(errfile)
```

Note that many interactive programs (e.g. vi) don’t work well with pipes substituted for standard input and output. You will have to use pseudo ttys (“ptys”) instead of pipes. Or you can use a Python interface to Don Libes’ “expect” library. A Python extension that interfaces to expect is called “expy” and available from [http://expectpy.sourceforge.net](http://expectpy.sourceforge.net). A pure Python solution that works like expect is [pexpect](https://pypi.org/project/pexpect/).

## 4.4.6 How do I access the serial (RS232) port?

For Win32, POSIX (Linux, BSD, etc.), Jython:

[http://pyserial.sourceforge.net](http://pyserial.sourceforge.net)

For Unix, see a Usenet post by Mitch Chapman:

[https://groups.google.com/groups?selm=34A04430.CF9@ohioee.com](https://groups.google.com/groups?selm=34A04430.CF9@ohioee.com)

## 4.4.7 Why doesn’t closing sys.stdout (stdin, stderr) really close it?

Python file objects are a high-level layer of abstraction on top of C streams, which in turn are a medium-level layer of abstraction on top of (among other things) low-level C file descriptors.

For most file objects you create in Python via the built-in file constructor, f.close() marks the Python file object as being closed from Python’s point of view, and also arranges to close the underlying C stream. This also happens automatically in f’s destructor, when f becomes garbage.

But stdin, stdout and stderr are treated specially by Python, because of the special status also given to them by C. Running sys.stdout.close() marks the Python-level file object as being closed, but does not close the associated C stream.

<!-- page: 68 -->

To close the underlying C stream for one of these three, you should first be sure that’s what you really want to do (e.g., you may confuse extension modules trying to do I/O). If it is, use os.close:

```python
os.close(0)    # close C's stdin stream
os.close(1)    # close C's stdout stream
os.close(2)    # close C's stderr stream
```

## 4.5 Network/Internet Programming

## 4.5.1 What WWW tools are there for Python?

See the chapters titled internet and netdata in the Library Reference Manual. Python has many modules that will help you build server-side and client-side web systems.

A summary of available frameworks is maintained by Paul Boddie at [https://wiki.python.org/moin/WebProgramming](https://wiki.python.org/moin/WebProgramming).

Cameron Laird maintains a useful set of pages about Python web technologies at [http://phaseit.net/claird/comp.lang.python/web\_python](http://phaseit.net/claird/comp.lang.python/web_python).

## 4.5.2 How can I mimic CGI form submission (METHOD=POST)?

I would like to retrieve web pages that are the result of POSTing a form. Is there existing code that would let me do this easily?

Yes. Here’s a simple example that uses httplib:

```python
#!/usr/local/bin/python

import httplib, sys, time

# build the query string
qs = "First=Josephine&MI=Q&Last=Public"

# connect and send the server a path
httpobj = httplib.HTTP('www.some-server.out-there', 80)
httpobj.putrequest('POST', '/cgi-bin/some-cgi-script')
# now generate the rest of the HTTP headers...
httpobj.putheader('Accept', '*/*')
httpobj.putheader('Connection', 'Keep-Alive')
httpobj.putheader('Content-type', 'application/x-www-form-urlencoded')
httpobj.putheader('Content-length', '%d' % len(qs))
httpobj.endheaders()
httpobj.send(qs)
# find out what the server said in response...
reply, msg, hdrs = httpobj.getreply()
if reply != 200:
    sys.stdout.write(httpobj.getfile().read())
```

Note that in general for percent-encoded POST operations, query strings must be quoted using urllib. urlencode(). For example, to send name=Guy Steele, Jr.:

```txt
>>> import urllib
>>> urllib.urlencode({'name': 'Guy Steele, Jr.'})
'name=Guy+Steele%2C+Jr.'
```

<!-- page: 69 -->

## 4.5.3 What module should I use to help with generating HTML?

You can find a collection of useful links on the [Web Programming wiki page](https://wiki.python.org/moin/WebProgramming).

## 4.5.4 How do I send mail from a Python script?

Use the standard library module smtplib.

Here’s a very simple interactive mail sender that uses it. This method will work on any host that supports an SMTP listener.

```python
import sys, smtplib

fromaddr = raw_input("From: ")
toaddrs  = raw_input("To: ").split(',')
print "Enter message, end with ^D:"
msg = ''
while True:
    line = sys.stdin.readline()
    if not line:
        break
    msg += line

# The actual mail send
server = smtplib.SMTP('localhost')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
```

A Unix-only alternative uses sendmail. The location of the sendmail program varies between systems; sometimes it is /usr/lib/sendmail, sometimes /usr/sbin/sendmail. The sendmail manual page will help you out. Here’s some sample code:

```python
import os

SENDMAIL = "/usr/sbin/sendmail"  # sendmail location
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write("To: receiver@example.com\n")
p.write("Subject: test\n")
p.write("\n") # blank line separating headers from body
p.write("Some text\n")
p.write("some more text\n")
sts = p.close()
if sts != 0:
    print "Sendmail exit status", sts
```

## 4.5.5 How do I avoid blocking in the connect() method of a socket?

The select module is commonly used to help with asynchronous I/O on sockets.

To prevent the TCP connect from blocking, you can set the socket to non-blocking mode. Then when you do the connect(), you will either connect immediately (unlikely) or get an exception that contains the error number as . errno. errno.EINPROGRESS indicates that the connection is in progress, but hasn’t finished yet. Different OSes will return different values, so you’re going to have to check what’s returned on your system.

<!-- page: 70 -->

You can use the connect\_ex() method to avoid creating an exception. It will just return the errno value. To poll, you can call connect\_ex() again later – 0 or errno.EISCONN indicate that you’re connected – or you can pass this socket to select to check if it’s writable.

## 4.6 Databases

## 4.6.1 Are there any interfaces to database packages in Python?

Yes.

Python 2.3 includes the bsddb package which provides an interface to the BerkeleyDB library. Interfaces to disk-based hashes such as DBM and GDBM are also included with standard Python.

Support for most relational databases is available. See the [DatabaseProgramming wiki page](https://wiki.python.org/moin/DatabaseProgramming) for details.

## 4.6.2 How do you implement persistent objects in Python?

The pickle library module solves this in a very general way (though you still can’t store things like open files, sockets or windows), and the shelve library module uses pickle and (g)dbm to create persistent mappings containing arbitrary Python objects. For better performance, you can use the cPickle module.

A more awkward way of doing things is to use pickle’s little sister, marshal. The marshal module provides very fast ways to store noncircular basic Python types to files and strings, and back again. Although marshal does not do fancy things like store instances or handle shared references properly, it does run extremely fast. For example, loading a half megabyte of data may take less than a third of a second. This often beats doing something more complex and general such as using gdbm with pickle/shelve.

## 4.6.3 Why is cPickle so slow?

By default pickle uses a relatively old and slow format for backward compatibility. You can however specify other protocol versions that are faster:

```python
largeString = 'z' * (100 * 1024)
myPickle = cPickle.dumps(largeString, protocol=1)
```

## 4.6.4 If my program crashes with a bsddb (or anydbm) database open, it gets corrupted. How come?

Databases opened for write access with the bsddb module (and often by the anydbm module, since it will preferentially use bsddb) must explicitly be closed using the .close() method of the database. The underlying library caches database contents which need to be converted to on-disk form and written.

If you have initialized a new bsddb database but not written anything to it before the program crashes, you will often wind up with a zero-length file and encounter an exception the next time the file is opened.

<!-- page: 71 -->

## 4.6.5 I tried to open Berkeley DB file, but bsddb produces bsddb.error: (22, ‘Invalid argument’). Help! How can I restore my data?

Don’t panic! Your data is probably intact. The most frequent cause for the error is that you tried to open an earlier Berkeley DB file with a later version of the Berkeley DB library.

Many Linux systems now have all three versions of Berkeley DB available. If you are migrating from version 1 to a newer version use db\_dump185 to dump a plain text version of the database. If you are migrating from version 2 to version 3 use db2\_dump to create a plain text version of the database. In either case, use db\_load to create a new native database for the latest version installed on your computer. If you have version 3 of Berkeley DB installed, you should be able to use db2\_load to create a native version 2 database.

You should move away from Berkeley DB version 1 files because the hash file code contains known bugs that can corrupt your data.

## 4.7 Mathematics and Numerics

## 4.7.1 How do I generate random numbers in Python?

The standard module random implements a random number generator. Usage is simple:

```python
import random
random.random()
```

This returns a random floating point number in the range [0, 1).

There are also many other specialized generators in this module, such as:

• randrange(a, b) chooses an integer in the range [a, b).

• uniform(a, b) chooses a floating point number in the range [a, b).

• normalvariate(mean, sdev) samples the normal (Gaussian) distribution.

Some higher-level functions operate on sequences directly, such as:

• choice(S) chooses random element from a given sequence

• shuffle(L) shuffles a list in-place, i.e. permutes it randomly

There’s also a Random class you can instantiate to create independent multiple random number generators.

<!-- page: 72 -->

<!-- page: 73 -->

# EXTENDING/EMBEDDING FAQ

## 5.1 Can I create my own functions in C?

Yes, you can create built-in modules containing functions, variables, exceptions and even new types in C. This is explained in the document extending-index.

Most intermediate or advanced Python books will also cover this topic.

## 5.2 Can I create my own functions in C++?

Yes, using the C compatibility features found in C++. Place extern "C" { ... } around the Python include files and put extern "C" before each function that is going to be called by the Python interpreter. Global or static C++ objects with constructors are probably not a good idea.

## 5.3 Writing C is hard; are there any alternatives?

There are a number of alternatives to writing your own C extensions, depending on what you’re trying to do.

If you need more speed, [Psyco](http://psyco.sourceforge.net/) generates x86 assembly code from Python bytecode. You can use Psyco to compile the most time-critical functions in your code, and gain a significant improvement with very little effort, as long as you’re running on a machine with an x86-compatible processor.

[Cython](http://cython.org) and its relative [Pyrex](https://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/) are compilers that accept a slightly modified form of Python and generate the corresponding C code. Pyrex makes it possible to write an extension without having to learn Python’s C API.

If you need to interface to some C or C++ library for which no Python extension currently exists, you can try wrapping the library’s data types and functions with a tool such as [SWIG](http://www.swig.org). [SIP](https://riverbankcomputing.com/software/sip/intro), [CXX](http://cxx.sourceforge.net/) [Boost](http://www.boost.org/libs/python/doc/index.html), or [Weave](https://github.com/scipy/weave) are also alternatives for wrapping C++ libraries.

<!-- page: 74 -->

## 5.4 How can I execute arbitrary Python statements from C?

The highest-level function to do this is PyRun\_SimpleString() which takes a single string argument to be executed in the context of the module \_\_main\_\_ and returns 0 for success and -1 when an exception occurred (including SyntaxError). If you want more control, use PyRun\_String(); see the source for PyRun\_SimpleString() in Python/pythonrun.c.

## 5.5 How can I evaluate an arbitrary Python expression from C?

Call the function PyRun\_String() from the previous question with the start symbol Py\_eval\_input; it parses an expression, evaluates it and returns its value.

## 5.6 How do I extract C values from a Python object?

That depends on the object’s type. If it’s a tuple, PyTuple\_Size() returns its length and PyTuple\_GetItem() returns the item at a specified index. Lists have similar functions, PyListSize() and PyList\_GetItem().

For strings, PyString\_Size() returns its length and PyString\_AsString() a pointer to its value. Note that Python strings may contain null bytes so C’s strlen() should not be used.

To test the type of an object, first make sure it isn’t NULL, and then use PyString\_Check(), PyTuple\_Check(), PyList\_Check(), etc.

There is also a high-level API to Python objects which is provided by the so-called ‘abstract’ interface – read Include/abstract.h for further details. It allows interfacing with any kind of Python sequence using calls like PySequence\_Length(), PySequence\_GetItem(), etc.) as well as many other useful protocols.

## 5.7 How do I use Py\_BuildValue() to create a tuple of arbitrary length?

You can’t. Use t = PyTuple\_New(n) instead, and fill it with objects using PyTuple\_SetItem(t, i, o) – note that this “eats” a reference count of o, so you have to Py\_INCREF() it. Lists have similar functions PyList\_New(n) and PyList\_SetItem(l, i, o). Note that you must set all the tuple items to some value before you pass the tuple to Python code – PyTuple\_New(n) initializes them to NULL, which isn’t a valid Python value.

## 5.8 How do I call an object’s method from C?

The PyObject\_CallMethod() function can be used to call an arbitrary method of an object. The parameters are the object, the name of the method to call, a format string like that used with Py\_BuildValue(), and the argument values:

```c
PyObject *
PyObject_CallMethod(PyObject *object, char *method_name,
                     char *arg_format, ...);
```

This works for any object that has methods – whether built-in or user-defined. You are responsible for eventually Py\_DECREF()’ing the return value.

To call, e.g., a file object’s “seek” method with arguments 10, 0 (assuming the file object pointer is “f”):

<!-- page: 75 -->

```txt
res = PyObject_CallMethod(f, "seek", "(ii)", 10, 0);
if (res == NULL) {
    ... an exception occurred ...
}
else {
    Py_DECREF(res);
}
```

Note that since PyObject\_CallObject() always wants a tuple for the argument list, to call a function without arguments, pass “()” for the format, and to call a function with one argument, surround the argument in parentheses, e.g. “(i)”.

## 5.9 How do I catch the output from PyErr\_Print() (or anything that prints to stdout/stderr)?

In Python code, define an object that supports the write() method. Assign this object to sys.stdout and sys. stderr. Call print\_error, or just allow the standard traceback mechanism to work. Then, the output will go wherever your write() method sends it.

The easiest way to do this is to use the StringIO class in the standard library.

Sample code and use for catching stdout:

```python
>>> class StdoutCatcher:
...     def __init__(self):
...         self.data = ''
...     def write(self, stuff):
...         self.data = self.data + stuff
...
>>> import sys
>>> sys.stdout = StdoutCatcher()
>>> print 'foo'
>>> print 'hello world!'
>>> sys.stderr.write(sys.stdout.data)
foo
hello world!
```

## 5.10 How do I access a module written in Python from C?

You can get a pointer to the module object as follows:

```txt
module = PyImport_ImportModule("<modulename>");
```

If the module hasn’t been imported yet (i.e. it is not yet present in sys.modules), this initializes the module; otherwise it simply returns the value of sys.modules["&lt;modulename&gt;"]. Note that it doesn’t enter the module into any namespace – it only ensures it has been initialized and is stored in sys.modules.

You can then access the module’s attributes (i.e. any name defined in the module) as follows:

```txt
attr = PyObject_GetAttrString(module, "<attrname>");
```

Calling PyObject\_SetAttrString() to assign to variables in the module also works.

<!-- page: 76 -->

## 5.11 How do I interface to C++ objects from Python?

Depending on your requirements, there are many approaches. To do this manually, begin by reading the “Extending and Embedding” document. Realize that for the Python run-time system, there isn’t a whole lot of difference between C and C++ – so the strategy of building a new Python type around a C structure (pointer) type will also work for C++ objects.

For C++ libraries, see Writing C is hard; are there any alternatives?.

## 5.12 I added a module using the Setup file and the make fails; why?

Setup must end in a newline, if there is no newline there, the build process fails. (Fixing this requires some ugly shell script hackery, and this bug is so minor that it doesn’t seem worth the effort.)

## 5.13 How do I debug an extension?

When using GDB with dynamically loaded extensions, you can’t set a breakpoint in your extension until your extension is loaded.

In your .gdbinit file (or interactively), add the command:

```javascript
br _PyImport_LoadDynamicModule
```

Then, when you run GDB:

```txt
\$ gdb /local/bin/python
gdb) run myscript.py
gdb) continue # repeat until your extension is loaded
gdb) finish  # so that your extension is loaded
gdb) br myfunction.c:50
gdb) continue
```

## 5.14 I want to compile a Python module on my Linux system, but some files are missing. Why?

Most packaged versions of Python don’t include the /usr/lib/python2.x/config/ directory, which contains various files required for compiling Python extensions.

For Red Hat, install the python-devel RPM to get the necessary files.

For Debian, run apt-get install python-dev.

<!-- page: 77 -->

## 5.15 What does “SystemError: \_PyImport\_FixupExtension: module yourmodule not loaded” mean?

This means that you have created an extension module named “yourmodule”, but your module init function does not initialize with that name.

Every module init function will have a line similar to:

```txt
module = Py_InitModule("yourmodule", yourmodule_functions);
```

If the string passed to this function is not the same name as your extension module, the SystemError exception will be raised.

## 5.16 How do I tell “incomplete input” from “invalid input”?

Sometimes you want to emulate the Python interactive interpreter’s behavior, where it gives you a continuation prompt when the input is incomplete (e.g. you typed the start of an “if” statement or you didn’t close your parentheses or triple string quotes), but it gives you a syntax error message immediately when the input is invalid.

In Python you can use the codeop module, which approximates the parser’s behavior sufficiently. IDLE uses this, for example.

The easiest way to do it in C is to call PyRun\_InteractiveLoop() (perhaps in a separate thread) and let the Python interpreter handle the input for you. You can also set the PyOS\_ReadlineFunctionPointer() to point at your custom input function. See Modules/readline.c and Parser/myreadline.c for more hints.

However sometimes you have to run the embedded Python interpreter in the same thread as your rest application and you can’t allow the PyRun\_InteractiveLoop() to stop while waiting for user input. The one solution then is to call PyParser\_ParseString() and test for e.error equal to E\_EOF, which means the input is incomplete. Here’s a sample code fragment, untested, inspired by code from Alex Farber:

```c
#include <Python.h>
#include <node.h>
#include <errcode.h>
#include <grammar.h>
#include <parsetok.h>
#include <compile.h>

int testcomplete(char *code)
    /* code should end in \n */
    /* return -1 for error, 0 for incomplete, 1 for complete */
{
    node *n;
    perrdetail e;

    n = PyParser_ParseString(code, &_PyParser_Grammar,
                               Py_file_input, &e);
    if (n == NULL) {
        if (e.error == E_EOF)
            return 0;
        return -1;
    }

    PyNode_Free(n);
```

(continues on next page)

<!-- page: 78 -->

```scss
return 1;
}
```

(continued from previous page)

Another solution is trying to compile the received string with Py\_CompileString(). If it compiles without errors, try to execute the returned code object by calling PyEval\_EvalCode(). Otherwise save the input for later. If the compilation fails, find out if it’s an error or just more input is required - by extracting the message string from the exception tuple and comparing it to the string “unexpected EOF while parsing”. Here is a complete example using the GNU readline library (you may want to ignore **SIGINT** while calling readline()):

```c
#include <stdio.h>
#include <readline.h>

#include <Python.h>
#include <object.h>
#include <compile.h>
#include <eval.h>

int main (int argc, char* argv[])
{
    int i, j, done = 0;                      /* lengths of line, code */
    char ps1[] = ">>> ";
    char ps2[] = "... ";
    char *prompt = ps1;
    char *msg, *line, *code = NULL;
    PyObject *src, *glb, *loc;
    PyObject *exc, *val, *trb, *obj, *dum;

    Py_Initialize ();
    loc = PyDict_New ();
    glb = PyDict_New ();
    PyDict_SetItemString (glb, "__builtins__", PyEval_GetBuiltins ());

    while (!done)
    {
        line = readline (prompt);

        if (NULL == line)                     /* Ctrl-D pressed */
        {
            done = 1;
        }
        else
        {
            i = strlen (line);

            if (i > 0)
                add_history (line);                 /* save non-empty lines */

            if (NULL == code)                     /* nothing in code yet */
                j = 0;
            else
                j = strlen (code);

            code = realloc (code, i + j + 2);
            if (NULL == code)                    /* out of memory */
                exit (1);
```

(continues on next page)

<!-- page: 79 -->

(continued from previous page)

```lisp
if (0 == j)
    code[0] = '\0';
/* code was empty, so */
/* keep strncat happy */

strncat (code, line, i);
/* append line to code */
code[i + j] = '\n';
/* append '\n' to code */
code[i + j + 1] = '\0';

src = Py_CompileString (code, "<stdin>", Py_single_input);

if (NULL != src)
/* compiled just fine - */
{
    if (ps1 == prompt ||
/* ">>> " or */
        '\n' == code[i + j - 1])
/* "... " and double '\n' */
    {
        /* so execute it */
        dum = PyEval_EvalCode ((PyCodeObject *)src, glb, loc);
        Py_XDECREF (dum);
        Py_XDECREF (src);
        free (code);
        code = NULL;
        if (PyErr_Occurred())
            PyErr_Print();
        prompt = ps1;
    }
}
/* syntax error or E_EOF? */
else if (PyErr_ExceptionMatches (PyExc_SyntaxError))
{
    PyErr_Fetch (&exc, &val, &trb);
/* clears exception! */

    if (PyArg_ParseTuple (val, "sO", &msg, &obj) &&
        !strcmp (msg, "unexpected EOF while parsing")) /* E_EOF */
    {
        Py_XDECREF (exc);
        Py_XDECREF (val);
        Py_XDECREF (trb);
        prompt = ps2;
    }
    else
/* some other syntax error */
    {
        PyErr_Restore (exc, val, trb);
        PyErr_Print ();
        free (code);
        code = NULL;
        prompt = ps1;
    }
}
else
/* some non-syntax error */
{
    PyErr_Print ();
    free (code);
    code = NULL;
    prompt = ps1;
}

free (line);
}
}
```

(continues on next page)

<!-- page: 80 -->

```c
(continued from previous page)

Py_XDECREF (glb);
Py_XDECREF (loc);
Py_Finalize();
exit (0);
}
```

## 5.17 How do I find undefined g++ symbols \_\_builtin\_new or \_\_ pure\_virtual?

To dynamically load g++ extension modules, you must recompile Python, relink it using g++ (change LINKCC in the Python Modules Makefile), and link your extension module using g++ (e.g., g++ -shared -o mymodule.so mymodule.o).

## 5.18 Can I create an object class with some methods implemented in C and others in Python (e.g. through inheritance)?

Yes, you can inherit from built-in classes such as int, list, dict, etc.

The Boost Python Library (BPL, [http://www.boost.org/libs/python/doc/index.html](http://www.boost.org/libs/python/doc/index.html)) provides a way of doing this from C++ (i.e. you can inherit from an extension class written in C++ using the BPL).

## 5.19 When importing module X, why do I get “undefined symbol: PyUnicodeUCS2\*”?

You are using a version of Python that uses a 4-byte representation for Unicode characters, but some C extension module you are importing was compiled using a Python that uses a 2-byte representation for Unicode characters (the default).

If instead the name of the undefined symbol starts with PyUnicodeUCS4, the problem is the reverse: Python was built using 2-byte Unicode characters, and the extension module was compiled using a Python with 4-byte Unicode characters.

This can easily occur when using pre-built extension packages. RedHat Linux 7.x, in particular, provided a “python2” binary that is compiled with 4-byte Unicode. This only causes the link failure if the extension uses any of the PyUnicode\_\*() functions. It is also a problem if an extension uses any of the Unicode-related format specifiers for Py\_BuildValue() (or similar) or parameter specifications for PyArg\_ParseTuple().

You can check the size of the Unicode character a Python interpreter is using by checking the value of sys.maxunicode:

```python
>>> import sys
>>> if sys.maxunicode > 65535:
...     print 'UCS4 build'
... else:
...     print 'UCS2 build'
```

The only way to solve this problem is to use extension modules compiled with a Python binary built using the same size for Unicode characters.

<!-- page: 81 -->

## PYTHON ON WINDOWS FAQ

## 6.1 How do I run a Python program under Windows?

This is not necessarily a straightforward question. If you are already familiar with running programs from the Windows command line then everything will seem obvious; otherwise, you might need a little more guidance.

Unless you use some sort of integrated development environment, you will end up typing Windows commands into what is variously referred to as a “DOS window” or “Command prompt window”. Usually you can create such a window from your Start menu; under Windows 7 the menu selection is Start ‣ Programs ‣ Accessories ‣ Command Prompt. You should be able to recognize when you have started such a window because you will see a Windows “command prompt”, which usually looks like this:

```txt
C:\>
```

The letter may be different, and there might be other things after it, so you might just as easily see something like:

```batch
D:\YourName\Projects\Python>
```

depending on how your computer has been set up and what else you have recently done with it. Once you have started such a window, you are well on the way to running Python programs.

You need to realize that your Python scripts have to be processed by another program called the Python interpreter. The interpreter reads your script, compiles it into bytecodes, and then executes the bytecodes to run your program. So, how do you arrange for the interpreter to handle your Python?

First, you need to make sure that your command window recognises the word “python” as an instruction to start the interpreter. If you have opened a command window, you should try entering the command python and hitting return.:

```batch
C:\Users\YourName> python
```

You should then see something like:

```txt
Python 2.7.3 (default, Apr 10 2012, 22.71:26) [MSC v.1500 32 bit (Intel)] on win32 Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You have started the interpreter in “interactive mode”. That means you can enter Python statements or expressions interactively and have them executed or evaluated while you wait. This is one of Python’s strongest features. Check it by entering a few expressions of your choice and seeing the results:

```txt
>>> print "Hello"
Hello
>>> "Hello" * 3
'HelloHelloHello'
```

<!-- page: 82 -->

Many people use the interactive mode as a convenient yet highly programmable calculator. When you want to end your interactive Python session, hold the Ctrl key down while you enter a Z, then hit the “Enter” key to get back to your Windows command prompt.

You may also find that you have a Start-menu entry such as Start ‣ Programs ‣ Python 2.7 ‣ Python (command line) that results in you seeing the >>> prompt in a new window. If so, the window will disappear after you enter the Ctrl-Z character; Windows is running a single “python” command in the window, and closes it when you terminate the interpreter.

If the python command, instead of displaying the interpreter prompt >>>, gives you a message like:

```txt
'python' is not recognized as an internal or external command, operable program or batch file.
```

or:

```txt
Bad command or filename
```

then you need to make sure that your computer knows where to find the Python interpreter. To do this you will have to modify a setting called PATH, which is a list of directories where Windows will look for programs.

You should arrange for Python’s installation directory to be added to the PATH of every command window as it starts. If you installed Python fairly recently then the command

```batch
dir C:\py*
```

will probably tell you where it is installed; the usual location is something like C:\Python27. Otherwise you will be reduced to a search of your whole disk … use Tools ‣ Find or hit the Search button and look for “python.exe”. Supposing you discover that Python is installed in the C:\Python27 directory (the default at the time of writing), you should make sure that entering the command

```batch
c:\Python27\python
```

starts up the interpreter as above (and don’t forget you’ll need a “Ctrl-Z” and an “Enter” to get out of it). Once you have verified the directory, you can add it to the system path to make it easier to start Python by just running the python command. This is currently an option in the installer as of CPython 2.7.

More information about environment variables can be found on the Using Python on Windows page.

<!-- page: 83 -->

## 6.2 How do I make Python scripts executable?

On Windows, the standard Python installer already associates the .py extension with a file type (Python.File) and gives that file type an open command that runs the interpreter (D:\Program Files\Python\python.exe "%1" %\*). This is enough to make scripts executable from the command prompt as ‘foo.py’. If you’d rather be able to execute the script by simple typing ‘foo’ with no extension you need to add .py to the PATHEXT environment variable.

## 6.3 Why does Python sometimes take so long to start?

Usually Python starts very quickly on Windows, but occasionally there are bug reports that Python suddenly begins to take a long time to start up. This is made even more puzzling because Python will work fine on other Windows systems which appear to be configured identically.

The problem may be caused by a misconfiguration of virus checking software on the problem machine. Some virus scanners have been known to introduce startup overhead of two orders of magnitude when the scanner is configured to monitor all reads from the filesystem. Try checking the configuration of virus scanning software on your systems to ensure that they are indeed configured identically. McAfee, when configured to scan all file system read activity, is a particular offender.

## 6.4 How do I make an executable from a Python script?

See [http://www.py2exe.org/](http://www.py2exe.org/) for a distutils extension that allows you to create console and GUI executables from Python code.

## 6.5 Is a \*.pyd file the same as a DLL?

Yes, .pyd files are dll’s, but there are a few differences. If you have a DLL named foo.pyd, then it must have a function initfoo(). You can then write Python “import foo”, and Python will search for foo.pyd (as well as foo.py, foo.pyc) and if it finds it, will attempt to call initfoo() to initialize it. You do not link your .exe with foo.lib, as that would cause Windows to require the DLL to be present.

Note that the search path for foo.pyd is PYTHONPATH, not the same as the path that Windows uses to search for foo.dll. Also, foo.pyd need not be present to run your program, whereas if you linked your program with a dll, the dll is required. Of course, foo.pyd is required if you want to say import foo. In a DLL, linkage is declared in the source code with declspec(dllexport). In a .pyd, linkage is defined in a list of available functions.

## 6.6 How can I embed Python into a Windows application?

Embedding the Python interpreter in a Windows app can be summarized as follows:

1. Do \_not\_ build Python into your .exe file directly. On Windows, Python must be a DLL to handle importing modules that are themselves DLL’s. (This is the first key undocumented fact.) Instead, link to pythonNN.dll; it is typically installed in C:\Windows\System. NN is the Python version, a number such as “27” for Python 2.7.

You can link to Python in two different ways. Load-time linking means linking against pythonNN.lib, while run-time linking means linking against pythonNN.dll. (General note: pythonNN.lib is the so-called “import lib” corresponding to pythonNN.dll. It merely defines symbols for the linker.)

<!-- page: 84 -->

Run-time linking greatly simplifies link options; everything happens at run time. Your code must load pythonNN. dll using the Windows LoadLibraryEx() routine. The code must also use access routines and data in pythonNN.dll (that is, Python’s C API’s) using pointers obtained by the Windows GetProcAddress() routine. Macros can make using these pointers transparent to any C code that calls routines in Python’s C API.

Borland note: convert pythonNN.lib to OMF format using Coff2Omf.exe first.

2. If you use SWIG, it is easy to create a Python “extension module” that will make the app’s data and methods available to Python. SWIG will handle just about all the grungy details for you. The result is C code that you link into your .exe file (!) You do \_not\_ have to create a DLL file, and this also simplifies linking.

3. SWIG will create an init function (a C function) whose name depends on the name of the extension module. For example, if the name of the module is leo, the init function will be called initleo(). If you use SWIG shadow classes, as you should, the init function will be called initleoc(). This initializes a mostly hidden helper class used by the shadow class.

The reason you can link the C code in step 2 into your .exe file is that calling the initialization function is equivalent to importing the module into Python! (This is the second key undocumented fact.)

4. In short, you can use the following code to initialize the Python interpreter with your extension module.

```cpp
#include "python.h"
...
Py_Initialize();  // Initialize Python.
initmyAppc();  // Initialize (import) the helper class.
PyRun_SimpleString("import myApp");  // Import the shadow class.
```

5. There are two problems with Python’s C API which will become apparent if you use a compiler other than MSVC, the compiler used to build pythonNN.dll.

Problem 1: The so-called “Very High Level” functions that take FILE \* arguments will not work in a multi-compiler environment because each compiler’s notion of a struct FILE will be different. From an implementation standpoint these are very \_low\_ level functions.

Problem 2: SWIG generates the following code when generating wrappers to void functions:

```c
Py_INcref(Py_None);
_resultobj = Py_None;
return _resultobj;
```

Alas, Py\_None is a macro that expands to a reference to a complex data structure called \_Py\_NoneStruct inside pythonNN.dll. Again, this code will fail in a mult-compiler environment. Replace such code by:

```txt
return Py_BuildValue("");
```

It may be possible to use SWIG’s %typemap command to make the change automatically, though I have not been able to get this to work (I’m a complete SWIG newbie).

6. Using a Python shell script to put up a Python interpreter window from inside your Windows app is not a good idea; the resulting window will be independent of your app’s windowing system. Rather, you (or the wxPythonWindow class) should create a “native” interpreter window. It is easy to connect that window to the Python interpreter. You can redirect Python’s i/o to \_any\_ object that supports read and write, so all you need is a Python object (defined in your extension module) that contains read() and write() methods.

<!-- page: 85 -->

## 6.7 How do I keep editors from inserting tabs into my Python source?

The FAQ does not recommend using tabs, and the Python style guide, [**PEP 8**](https://www.python.org/dev/peps/pep-0008), recommends 4 spaces for distributed Python code; this is also the Emacs python-mode default.

Under any editor, mixing tabs and spaces is a bad idea. MSVC is no different in this respect, and is easily configured to use spaces: Take Tools ‣ Options ‣ Tabs, and for file type “Default” set “Tab size” and “Indent size” to 4, and select the “Insert spaces” radio button.

If you suspect mixed tabs and spaces are causing problems in leading whitespace, run Python with the -t switch or run the tabnanny module to check a directory tree in batch mode.

## 6.8 How do I check for a keypress without blocking?

Use the msvcrt module. This is a standard Windows-specific extension module. It defines a function kbhit() which checks whether a keyboard hit is present, and getch() which gets one character without echoing it.

## 6.9 How do I emulate os.kill() in Windows?

Prior to Python 2.7 and 3.2, to terminate a process, you can use ctypes:

```python
import ctypes

def kill(pid):
    """kill function for Win32"""
    kernel32 = ctypes.wind11.kernel32
    handle = kernel32.OpenProcess(1, 0, pid)
    return (0 != kernel32.TerminateProcess(handle, 0))
```

In 2.7 and 3.2, os.kill() is implemented similar to the above function, with the additional feature of being able to send Ctrl+C and Ctrl+Break to console subprocesses which are designed to handle those signals. See os.kill() for further details.

## 6.10 How do I extract the downloaded documentation on Windows?

Sometimes, when you download the documentation package to a Windows machine using a web browser, the file extension of the saved file ends up being .EXE. This is a mistake; the extension should be .TGZ.

Simply rename the downloaded file to have the .TGZ extension, and WinZip will be able to handle it. (If your copy of WinZip doesn’t, get a newer one from [https://www.winzip.com](https://www.winzip.com).)

<!-- page: 86 -->

<!-- page: 87 -->

# GRAPHIC USER INTERFACE FAQ

## 7.1 What platform-independent GUI toolkits exist for Python?

Depending on what platform(s) you are aiming at, there are several.

## 7.1.1 Tkinter

Standard builds of Python include an object-oriented interface to the Tcl/Tk widget set, called Tkinter. This is probably the easiest to install and use. For more info about Tk, including pointers to the source, see the Tcl/Tk home page at [https://www.tcl.tk](https://www.tcl.tk). Tcl/Tk is fully portable to the Mac OS X, Windows, and Unix platforms.

## 7.1.2 wxWidgets

wxWidgets ([https://www.wxwidgets.org](https://www.wxwidgets.org)) is a free, portable GUI class library written in C++ that provides a native look and feel on a number of platforms, with Windows, Mac OS X, GTK, X11, all listed as current stable targets. Language bindings are available for a number of languages including Python, Perl, Ruby, etc.

wxPython ([http://www.wxpython.org](http://www.wxpython.org)) is the Python binding for wxwidgets. While it often lags slightly behind the official wxWidgets releases, it also offers a number of features via pure Python extensions that are not available in other language bindings. There is an active wxPython user and developer community.

Both wxWidgets and wxPython are free, open source, software with permissive licences that allow their use in commercial products as well as in freeware or shareware.

## 7.1.3 Qt

There are bindings available for the Qt toolkit (using either [PyQt](https://riverbankcomputing.com/software/pyqt/intro) or [PySide](https://wiki.qt.io/PySide)) and for KDE ([PyKDE4](https://techbase.kde.org/Languages/Python/Using_PyKDE_4)). PyQt is currently more mature than PySide, but you must buy a PyQt license from [Riverbank Computing](https://www.riverbankcomputing.com/commercial/license-faq) if you want to write proprietary applications. PySide is free for all applications.

Qt 4.5 upwards is licensed under the LGPL license; also, commercial licenses are available from [The Qt Company](https://www.qt.io/licensing/).

<!-- page: 88 -->

## 7.1.4 Gtk+

PyGtk bindings for the [Gtk+ toolkit](http://www.gtk.org) have been implemented by James Henstridge; see <[http://www.pygtk.org](http://www.pygtk.org)>.

## 7.1.5 FLTK

Python bindings for [the FLTK toolkit](http://www.fltk.org), a simple yet powerful and mature cross-platform windowing system, are available from [the PyFLTK project](http://pyfltk.sourceforge.net).

## 7.1.6 OpenGL

For OpenGL bindings, see [PyOpenGL](http://pyopengl.sourceforge.net).

## 7.2 What platform-specific GUI toolkits exist for Python?

By installing the [PyObjc Objective-C bridge](https://pythonhosted.org/pyobjc/), Python programs can use Mac OS X’s Cocoa libraries.

Pythonwin by Mark Hammond includes an interface to the Microsoft Foundation Classes and a Python programming environment that’s written mostly in Python using the MFC classes.

## 7.3 Tkinter questions

## 7.3.1 How do I freeze Tkinter applications?

Freeze is a tool to create stand-alone applications. When freezing Tkinter applications, the applications will not be truly stand-alone, as the application will still need the Tcl and Tk libraries.

One solution is to ship the application with the Tcl and Tk libraries, and point to them at run-time using the TCL\_LIBRARY and TK\_LIBRARY environment variables.

To get truly stand-alone applications, the Tcl scripts that form the library have to be integrated into the application as well. One tool supporting that is SAM (stand-alone modules), which is part of the Tix distribution ([http://tix.sourceforge.net/](http://tix.sourceforge.net/)).

Build Tix with SAM enabled, perform the appropriate call to Tclsam\_init(), etc. inside Python’s Modules/ tkappinit.c, and link with libtclsam and libtksam (you might include the Tix libraries as well).

## 7.3.2 Can I have Tk events handled while waiting for I/O?

On platforms other than Windows, yes, and you don’t even need threads! But you’ll have to restructure your I/O code a bit. Tk has the equivalent of Xt’s XtAddInput() call, which allows you to register a callback function which will be called from the Tk mainloop when I/O is possible on a file descriptor. See tkinter-file-handlers.

<!-- page: 89 -->

## 7.3.3 I can’t get key bindings to work in Tkinter: why?

An often-heard complaint is that event handlers bound to events with the bind() method don’t get handled even when the appropriate key is pressed.

The most common cause is that the widget to which the binding applies doesn’t have “keyboard focus”. Check out the Tk documentation for the focus command. Usually a widget is given the keyboard focus by clicking in it (but not for labels; see the takefocus option).

<!-- page: 90 -->

<!-- page: 91 -->

# “WHY IS PYTHON INSTALLED ON MY COMPUTER?” FAQ

## 8.1 What is Python?

Python is a programming language. It’s used for many different applications. It’s used in some high schools and colleges as an introductory programming language because Python is easy to learn, but it’s also used by professional software developers at places such as Google, NASA, and Lucasfilm Ltd.

If you wish to learn more about Python, start with the [Beginner’s Guide to Python](https://wiki.python.org/moin/BeginnersGuide).

## 8.2 Why is Python installed on my machine?

If you find Python installed on your system but don’t remember installing it, there are several possible ways it could have gotten there.

• Perhaps another user on the computer wanted to learn programming and installed it; you’ll have to figure out who’s been using the machine and might have installed it.

• A third-party application installed on the machine might have been written in Python and included a Python installation. For a home computer, the most common such application is [PySol](http://pysolfc.sourceforge.net/), a solitaire game that includes over 1000 different games and variations.

• Some Windows machines also have Python installed. At this writing we’re aware of computers from Hewlett-Packard and Compaq that include Python. Apparently some of HP/Compaq’s administrative tools are written in Python.

• All Apple computers running Mac OS X have Python installed; it’s included in the base installation.

## 8.3 Can I delete Python?

That depends on where Python came from.

If someone installed it deliberately, you can remove it without hurting anything. On Windows, use the Add/Remove Programs icon in the Control Panel.

If Python was installed by a third-party application, you can also remove it, but that application will no longer work. You should use that application’s uninstaller rather than removing Python directly.

If Python came with your operating system, removing it is not recommended. If you remove it, whatever tools were written in Python will no longer run, and some of them might be important to you. Reinstalling the whole system would then be required to fix things again.

<!-- page: 92 -->

<!-- page: 93 -->

# GLOSSARY

**>>>** The default Python prompt of the interactive shell. Often seen for code examples which can be executed interactively in the interpreter.

The default Python prompt of the interactive shell when entering code for an indented code block, when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator.

**2to3** A tool that tries to convert Python 2.x code to Python 3.x code by handling most of the incompatibilities which can be detected by parsing the source and traversing the parse tree.

2to3 is available in the standard library as lib2to3; a standalone entry point is provided as Tools/scripts/ 2to3. See 2to3-reference.

**abstract base class** Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like hasattr() would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and issubclass(); see the abc module documentation. Python comes with many built-in ABCs for data structures (in the collections module), numbers (in the numbers module), and streams (in the io module). You can create your own ABCs with the abc module.

**argument** A value passed to a function (or method) when calling the function. There are two types of arguments:

• keyword argument: an argument preceded by an identifier (e.g. name=) in a function call or passed as a value in a dictionary preceded by \*\*. For example, 3 and 5 are both keyword arguments in the following calls to complex():

```python
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
```

• positional argument: an argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list and/or be passed as elements of an iterable preceded by \*. For example, 3 and 5 are both positional arguments in the following calls:

```txt
complex(3, 5)
complex(*(3, 5))
```

Arguments are assigned to the named local variables in a function body. See the calls section for the rules governing this assignment. Syntactically, any expression can be used to represent an argument; the evaluated value is assigned to the local variable.

See also the parameter glossary entry and the FAQ question on the difference between arguments and parameters.

**attribute** A value associated with an object which is referenced by name using dotted expressions. For example, if an object o has an attribute a it would be referenced as o.a.

**BDFL** Benevolent Dictator For Life, a.k.a. [Guido van Rossum](https://www.python.org/~guido/), Python’s creator.

<!-- page: 94 -->

**bytes-like object** An object that supports the buffer protocol, like str, bytearray or memoryview. Bytes-like objects can be used for various operations that expect binary data, such as compression, saving to a binary file or sending over a socket. Some operations need the binary data to be mutable, in which case not all bytes-like objects can apply.

**bytecode** Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter. The bytecode is also cached in .pyc and .pyo files so that executing the same file is faster the second time (recompilation from source to bytecode can be avoided). This “intermediate language” is said to run on a virtual machine that executes the machine code corresponding to each bytecode. Do note that bytecodes are not expected to work between different Python virtual machines, nor to be stable between Python releases.

A list of bytecode instructions can be found in the documentation for the dis module.

**class** A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

**classic class** Any class which does not inherit from object. See new-style class. Classic classes have been removed in Python 3.

**coercion** The implicit conversion of an instance of one type to another during an operation which involves two arguments of the same type. For example, int(3.15) converts the floating point number to the integer 3, but in 3+4.5, each argument is of a different type (one int, one float), and both must be converted to the same type before they can be added or it will raise a TypeError. Coercion between two operands can be performed with the coerce built-in function; thus, 3+4.5 is equivalent to calling operator.add(\*coerce(3, 4.5)) and results in operator.add(3.0, 4.5). Without coercion, all arguments of even compatible types would have to be normalized to the same value by the programmer, e.g., float(3)+4.5 rather than just 3+4.5.

**complex number** An extension of the familiar real number system in which all numbers are expressed as a sum of a real part and an imaginary part. Imaginary numbers are real multiples of the imaginary unit (the square root of -1), often written i in mathematics or j in engineering. Python has built-in support for complex numbers, which are written with this latter notation; the imaginary part is written with a j suffix, e.g., 3+1j. To get access to complex equivalents of the math module, use cmath. Use of complex numbers is a fairly advanced mathematical feature. If you’re not aware of a need for them, it’s almost certain you can safely ignore them.

**context manager** An object which controls the environment seen in a with statement by defining \_\_enter\_\_() and exit\_\_() methods. See [**PEP 343**](https://www.python.org/dev/peps/pep-0343).

**CPython** The canonical implementation of the Python programming language, as distributed on [python.org](https://www.python.org). The term “CPython” is used when necessary to distinguish this implementation from others such as Jython or IronPython.

**decorator** A function returning another function, usually applied as a function transformation using the @wrapper syntax. Common examples for decorators are classmethod() and staticmethod().

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:

```python
def f(...):
    ...
f = staticmethod(f)

@staticmethod
def f(...):
    ...
```

The same concept exists for classes, but is less commonly used there. See the documentation for function definitions and class definitions for more about decorators.

**descriptor** Any new-style object which defines the methods \_\_get\_\_(), \_\_set\_\_(), or \_\_delete\_\_(). When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using a.b to get, set or delete an attribute looks up the object named b in the class dictionary for a, but if b is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python

<!-- page: 95 -->

because they are the basis for many features including functions, methods, properties, class methods, static methods, and reference to super classes.

For more information about descriptors’ methods, see descriptors.

**dictionary** An associative array, where arbitrary keys are mapped to values. The keys can be any object with \_\_hash\_\_() and \_\_eq\_\_() methods. Called a hash in Perl.

**dictionary view** The objects returned from dict.viewkeys(), dict.viewvalues(), and dict. viewitems() are called dictionary views. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes. To force the dictionary view to become a full list use list(dictview). See dict-views.

**docstring** A string literal which appears as the first expression in a class, function or module. While ignored when the suite is executed, it is recognized by the compiler and put into the \_\_doc\_\_ attribute of the enclosing class, function or module. Since it is available via introspection, it is the canonical place for documentation of the object.

**duck-typing** A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitution. Duck-typing avoids tests using type() or isinstance(). (Note, however, that duck-typing can be complemented with abstract base classes.) Instead, it typically employs hasattr() tests or EAFP programming.

**EAFP** Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.

**expression** A piece of syntax which can be evaluated to some value. In other words, an expression is an accumulation of expression elements like literals, names, attribute access, operators or function calls which all return a value. In contrast to many other languages, not all language constructs are expressions. There are also statements which cannot be used as expressions, such as print or if. Assignments are also statements, not expressions.

**extension module** A module written in C or C++, using Python’s C API to interact with the core and with user code.

**file object** An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource. Depending on the way it was created, a file object can mediate access to a real on-disk file or to another type of storage or communication device (for example standard input/output, in-memory buffers, sockets, pipes, etc.). File objects are also called file-like objects or streams.

There are actually three categories of file objects: raw binary files, buffered binary files and text files. Their interfaces are defined in the io module. The canonical way to create a file object is by using the open() function.

**file-like object** A synonym for file object.

**finder** An object that tries to find the loader for a module. It must implement a method named find\_module(). See [**PEP 302**](https://www.python.org/dev/peps/pep-0302) for details.

**floor division** Mathematical division that rounds down to nearest integer. The floor division operator is //. For example, the expression 11 // 4 evaluates to 2 in contrast to the 2.75 returned by float true division. Note that (-11) // 4 is -3 because that is -2.75 rounded downward. See [**PEP 238**](https://www.python.org/dev/peps/pep-0238).

**function** A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body. See also parameter, method, and the function section.

future\_\_ A pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter. For example, the expression 11/4 currently evaluates to 2. If the module in which it is executed had enabled true division by executing:

<!-- page: 96 -->

```python
from __future__ import division
```

the expression 11/4 would evaluate to 2.75. By importing the \_\_future\_\_ module and evaluating its variables, you can see when a new feature was first added to the language and when it will become the default:

```python
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
```

**garbage collection** The process of freeing memory when it is not used anymore. Python performs garbage collection via reference counting and a cyclic garbage collector that is able to detect and break reference cycles.

**generator** A function which returns an iterator. It looks like a normal function except that it contains yield statements for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function. Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the generator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

**generator expression** An expression that returns an iterator. It looks like a normal expression followed by a for expression defining a loop variable, range, and an optional if expression. The combined expression generates values for an enclosing function:

```txt
>>> sum(i*i for i in range(10))
285
```

```txt
# sum of squares 0, 1, 4, ... 81
```

**GIL** See global interpreter lock.

**global interpreter lock** The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This simplifies the CPython implementation by making the object model (including critical built-in types such as dict) implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

However, some extension modules, either standard or third-party, are designed so as to release the GIL when doing computationally-intensive tasks such as compression or hashing. Also, the GIL is always released when doing I/O.

Past efforts to create a “free-threaded” interpreter (one which locks shared data at a much finer granularity) have not been successful because performance suffered in the common single-processor case. It is believed that overcoming this performance issue would make the implementation much more complicated and therefore costlier to maintain.

**hashable** An object is hashable if it has a hash value which never changes during its lifetime (it needs a \_\_hash\_\_() method), and can be compared to other objects (it needs an \_\_eq\_\_() or \_\_cmp\_\_() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal (except with themselves), and their hash value is derived from their id().

**IDLE** An Integrated Development Environment for Python. IDLE is a basic editor and interpreter environment which ships with the standard distribution of Python.

**immutable** An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.

**integer division** Mathematical division discarding any remainder. For example, the expression 11/4 currently evaluates to 2 in contrast to the 2.75 returned by float division. Also called floor division. When dividing two integers the

<!-- page: 97 -->

outcome will always be another integer (having the floor function applied to it). However, if one of the operands is another numeric type (such as a float), the result will be coerced (see coercion) to a common type. For example, an integer divided by a float will result in a float value, possibly with a decimal fraction. Integer division can be forced by using the // operator instead of the / operator. See also \_\_future\_\_.

**importing** The process by which Python code in one module is made available to Python code in another module.

**importer** An object that both finds and loads a module; both a finder and loader object.

**interactive** Python has an interactive interpreter which means you can enter statements and expressions at the interpreter prompt, immediately execute them and see their results. Just launch python with no arguments (possibly by selecting it from your computer’s main menu). It is a very powerful way to test out new ideas or inspect modules and packages (remember help(x)).

**interpreted** Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. This means that source files can be run directly without explicitly creating an executable which is then run. Interpreted languages typically have a shorter development/debug cycle than compiled ones, though their programs generally also run more slowly. See also interactive.

**iterable** An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict and file and objects of any classes you define with an \_\_iter\_\_() or \_\_getitem\_\_() method. Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.

**iterator** An object representing a stream of data. Repeated calls to the iterator’s next() method return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its next() method just raise StopIteration again. Iterators are required to have an \_\_iter\_\_() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

More information can be found in typeiter.

**key function** A key function or collation function is a callable that returns a value used for sorting or ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale specific sort conventions.

A number of tools in Python accept key functions to control how elements are ordered or grouped. They include min(), max(), sorted(), list.sort(), heapq.nsmallest(), heapq.nlargest(), and itertools.groupby().

There are several ways to create a key function. For example. the str.lower() method can serve as a key function for case insensitive sorts. Alternatively, an ad-hoc key function can be built from a lambda expression such as lambda r: (r[0], r[2]). Also, the operator module provides three key function constructors: attrgetter(), itemgetter(), and methodcaller(). See the Sorting HOW TO for examples of how to create and use key functions.

## keyword argument See argument.

**lambda** An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [parameters]: expression

**LBYL** Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the EAFP approach and is characterized by the presence of many if statements.

<!-- page: 98 -->

In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the looking” and “the leaping”. For example, the code, if key in mapping: return mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. This issue can be solved with locks or by using the EAFP approach.

**list** A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).

**list comprehension** A compact way to process all or part of the elements in a sequence and return a list with the results. result = ["0x%02x" % x for x in range(256) if x % 2 == 0] generates a list of strings containing even hex numbers (0x..) in the range from 0 to 255. The if clause is optional. If omitted, all elements in range(256) are processed.

**loader** An object that loads a module. It must define a method named load\_module(). A loader is typically returned by a finder. See [**PEP 302**](https://www.python.org/dev/peps/pep-0302) for details.

**magic method** An informal synonym for special method.

**mapping** A container object that supports arbitrary key lookups and implements the methods specified in the Mapping or MutableMapping abstract base classes. Examples include dict, collections.defaultdict, collections.OrderedDict and collections.Counter.

**metaclass** The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses. Most users never need this tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have been used for logging attribute access, adding thread-safety, tracking object creation, implementing singletons, and many other tasks.

More information can be found in metaclasses.

**method** A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self). See function and nested scope.

**method resolution order** Method Resolution Order is the order in which base classes are searched for a member during lookup. See [The Python 2.3 Method Resolution Order](https://www.python.org/download/releases/2.3/mro/) for details of the algorithm used by the Python interpreter since the 2.3 release.

**module** An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

See also package.

**MRO** See method resolution order.

**mutable** Mutable objects can change their value but keep their id(). See also immutable.

**named tuple** Any tuple-like class whose indexable elements are also accessible using named attributes (for example, time.localtime() returns a tuple-like object where the year is accessible either with an index such as t[0] or with a named attribute like t.tm\_year).

A named tuple can be a built-in type such as time.struct\_time, or it can be created with a regular class definition. A full featured named tuple can also be created with the factory function collections. namedtuple(). The latter approach automatically provides extra features such as a self-documenting representation like Employee(name='jones', title='programmer').

**namespace** The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions \_\_builtin\_\_.open() and os.open() are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.izip() makes it clear that those functions are implemented by the random and itertools modules, respectively.

<!-- page: 99 -->

**nested scope** The ability to refer to a variable in an enclosing definition. For instance, a function defined inside another function can refer to variables in the outer function. Note that nested scopes work only for reference and not for assignment which will always write to the innermost scope. In contrast, local variables both read and write in the innermost scope. Likewise, global variables read and write to the global namespace.

**new-style class** Any class which inherits from object. This includes all built-in types like list and dict. Only new-style classes can use Python’s newer, versatile features like \_\_slots\_\_, descriptors, properties, and \_getattribute\_\_().

More information can be found in newstyle.

**object** Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.

**package** A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an \_\_path\_\_ attribute.

**parameter** A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept. There are four types of parameters:

• positional-or-keyword: specifies an argument that can be passed either positionally or as a keyword argument. This is the default kind of parameter, for example foo and bar in the following:

```txt
def func(foo, bar=None): ...
```

• positional-only: specifies an argument that can be supplied only by position. Python has no syntax for defining positional-only parameters. However, some built-in functions have positional-only parameters (e.g. abs()).

• var-positional: specifies that an arbitrary sequence of positional arguments can be provided (in addition to any positional arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with \*, for example args in the following:

```txt
def func(*args, **kwargs): ...
```

• var-keyword: specifies that arbitrarily many keyword arguments can be provided (in addition to any keyword arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with \*\*, for example kwargs in the example above.

Parameters can specify both optional and required arguments, as well as default values for some optional arguments.

See also the argument glossary entry, the FAQ question on the difference between arguments and parameters, and the function section.

**PEP** Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. PEPs should provide a concise technical specification and a rationale for proposed features.

PEPs are intended to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.

See [**PEP 1**](https://www.python.org/dev/peps/pep-0001).

**positional argument** See argument.

**Python 3000** Nickname for the Python 3.x release line (coined long ago when the release of version 3 was something in the distant future.) This is also abbreviated “Py3k”.

**Pythonic** An idea or piece of code which closely follows the most common idioms of the Python language, rather than implementing code using concepts common to other languages. For example, a common idiom in Python is to loop over all elements of an iterable using a for statement. Many other languages don’t have this type of construct, so people unfamiliar with Python sometimes use a numerical counter instead:

<!-- page: 100 -->

```python
for i in range(len(food)):
    print food[i]
```

As opposed to the cleaner, Pythonic method:

```python
for piece in food:
    print piece
```

**reference count** The number of references to an object. When the reference count of an object drops to zero, it is deallocated. Reference counting is generally not visible to Python code, but it is a key element of the CPython implementation. The sys module defines a getrefcount() function that programmers can call to return the reference count for a particular object.

\_slots\_\_ A declaration inside a new-style class that saves memory by pre-declaring space for instance attributes and eliminating instance dictionaries. Though popular, the technique is somewhat tricky to get right and is best reserved for rare cases where there are large numbers of instances in a memory-critical application.

**sequence** An iterable which supports efficient element access using integer indices via the \_\_getitem\_\_() special method and defines a len() method that returns the length of the sequence. Some built-in sequence types are list, str, tuple, and unicode. Note that dict also supports \_\_getitem\_\_() and \_\_len\_\_(), but is considered a mapping rather than a sequence because the lookups use arbitrary immutable keys rather than integers.

**slice** An object usually containing a portion of a sequence. A slice is created using the subscript notation, [] with colons between numbers when several are given, such as in variable\_name[1:3:5]. The bracket (subscript) notation uses slice objects internally (or in older versions, \_\_getslice\_\_() and \_\_setslice\_\_()).

**special method** A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. Special methods are documented in specialnames.

**statement** A statement is part of a suite (a “block” of code). A statement is either an expression or one of several constructs with a keyword, such as if, while or for.

**struct sequence** A tuple with named elements. Struct sequences expose an interface similiar to named tuple in that elements can be accessed either by index or as an attribute. However, they do not have any of the named tuple methods like \_make() or \_asdict(). Examples of struct sequences include sys.float\_info and the return value of os.stat().

**triple-quoted string** A string which is bound by three instances of either a quotation mark (“) or an apostrophe (‘). While they don’t provide any functionality not available with single-quoted strings, they are useful for a number of reasons. They allow you to include unescaped single and double quotes within a string and they can span multiple lines without the use of the continuation character, making them especially useful when writing docstrings.

**type** The type of a Python object determines what kind of object it is; every object has a type. An object’s type is accessible as its \_\_class\_\_ attribute or can be retrieved with type(obj).

**universal newlines** A manner of interpreting text streams in which all of the following are recognized as ending a line: the Unix end-of-line convention '\n', the Windows convention '\r\n', and the old Macintosh convention '\ r'. See [**PEP 278**](https://www.python.org/dev/peps/pep-0278) and [**PEP 3116**](https://www.python.org/dev/peps/pep-3116), as well as str.splitlines() for an additional use.

**virtual environment** A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.

**virtual machine** A computer defined entirely in software. Python’s virtual machine executes the bytecode emitted by the bytecode compiler.

**Zen of Python** Listing of Python design principles and philosophies that are helpful in understanding and using the language. The listing can be found by typing “import this” at the interactive prompt.

<!-- page: 101 -->

## ABOUT THESE DOCUMENTS

These documents are generated from [reStructuredText](http://docutils.sourceforge.net/rst.html) sources by [Sphinx](http://sphinx-doc.org/), a document processor specifically written for the Python documentation.

Development of the documentation and its toolchain is an entirely volunteer effort, just like Python itself. If you want to contribute, please take a look at the reporting-bugs page for information on how to do so. New volunteers are always welcome!

Many thanks go to:

• Fred L. Drake, Jr., the creator of the original Python documentation toolset and writer of much of the content;

• the [Docutils](http://docutils.sourceforge.net/) project for creating reStructuredText and the Docutils suite;

• Fredrik Lundh for his [Alternative Python Reference](http://effbot.org/zone/pyref.htm) project from which Sphinx got many good ideas.

## B.1 Contributors to the Python Documentation

Many people have contributed to the Python language, the Python standard library, and the Python documentation. See [Misc/ACKS](https://github.com/python/cpython/tree/2.7/Misc/ACKS) in the Python source distribution for a partial list of contributors.

It is only with the input and contributions of the Python community that Python has such wonderful documentation – Thank You!

<!-- page: 102 -->

<!-- page: 103 -->

# HISTORY AND LICENSE

## C.1 History of the software

Python was created in the early 1990s by Guido van Rossum at Stichting Mathematisch Centrum (CWI, see [https://www.cwi.nl/](https://www.cwi.nl/)) in the Netherlands as a successor of a language called ABC. Guido remains Python’s principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for National Research Initiatives (CNRI, see [https://www.cnri.reston.va.us/](https://www.cnri.reston.va.us/)) in Reston, Virginia where he released several versions of the software.

In May 2000, Guido and the Python core development team moved to BeOpen.com to form the BeOpen PythonLabs team. In October of the same year, the PythonLabs team moved to Digital Creations (now Zope Corporation; see [https://www.zope.org/](https://www.zope.org/)). In 2001, the Python Software Foundation (PSF, see [https://www.python.org/psf/](https://www.python.org/psf/)) was formed, a non-profit organization created specifically to own Python-related Intellectual Property. Zope Corporation is a sponsoring member of the PSF.

All Python releases are Open Source (see [https://opensource.org/](https://opensource.org/) for the Open Source Definition). Historically, most, but not all, Python releases have also been GPL-compatible; the table below summarizes the various releases.

| Release | Derived from | Year | Owner | GPL compatible? |
| --- | --- | --- | --- | --- |
| 0.9.0 thru 1.2 | n/a | 1991-1995 | CWI | yes |
| 1.3 thru 1.5.2 | 1.2 | 1995-1999 | CNRI | yes |
| 1.6 | 1.5.2 | 2000 | CNRI | no |
| 2.0 | 1.6 | 2000 | BeOpen.com | no |
| 1.6.1 | 1.6 | 2001 | CNRI | no |
| 2.1 | 2.0+1.6.1 | 2001 | PSF | no |
| 2.0.1 | 2.0+1.6.1 | 2001 | PSF | yes |
| 2.1.1 | 2.1+2.0.1 | 2001 | PSF | yes |
| 2.1.2 | 2.1.1 | 2002 | PSF | yes |
| 2.1.3 | 2.1.2 | 2002 | PSF | yes |
| 2.2 and above | 2.1.1 | 2001-now | PSF | yes |

**Note:** GPL-compatible doesn’t mean that we’re distributing Python under the GPL. All Python licenses, unlike the GPL, let you distribute a modified version without making your changes open source. The GPL-compatible licenses make it possible to combine Python with other software that is released under the GPL; the others don’t.

<!-- page: 104 -->

## C.2 Terms and conditions for accessing or otherwise using Python

## C.2.1 PSF LICENSE AGREEMENT FOR PYTHON 2.7.18

1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"),␣,→and the Individual or Organization ("Licensee") accessing and otherwise using␣,→Python 2.7.18 software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, PSF hereby grants Licensee a nonexclusive, royalty-free, world-wide license to␣,→reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use Python 2.7.18 alone or in any derivative version, provided, however, that PSF's License Agreement and PSF's notice␣,→of copyright, i.e., "Copyright © 2001-2020 Python Software Foundation; All␣,→Rights Reserved" are retained in Python 2.7.18 alone or in any derivative version prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on or incorporates Python 2.7.18 or any part thereof, and wants to make the derivative work available to others as provided herein, then Licensee␣,→hereby agrees to include in any such work a brief summary of the changes made to␣,→Python 2.7.18.

4. PSF is making Python 2.7.18 available to Licensee on an "AS IS" basis. PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION␣,→OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT␣,→THE USE OF PYTHON 2.7.18 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 2.7.18 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT␣,→OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 2.7.18, OR ANY␣,→DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach␣,→of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any␣,→relationship of agency, partnership, or joint venture between PSF and Licensee. This␣,→License

<!-- page: 105 -->

```txt
Agreement does not grant permission to use PSF trademarks or trade name in a trademark sense to endorse or promote products or services of Licensee, or any third party.
```

8. By copying, installing or otherwise using Python 2.7.18, Licensee agrees to be bound by the terms and conditions of this License Agreement.

## C.2.2 BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0

## BEOPEN PYTHON OPEN SOURCE LICENSE AGREEMENT VERSION 1

```txt
This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an office at 160 Saratoga Avenue, Santa Clara, CA 95051, and the Individual or Organization ("Licensee") accessing and otherwise using this software in source or binary form and its associated documentation ("the Software").
Subject to the terms and conditions of this BeOpen Python License Agreement, BeOpen hereby grants Licensee a non-exclusive, royalty-free, world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use the Software alone or in any derivative version, provided, however, that the BeOpen Python License is retained in the Software, alone or in any derivative version prepared by Licensee.
BeOpen is making the Software available to Licensee on an "AS IS" basis. BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE SOFTWARE WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE SOFTWARE FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THE SOFTWARE, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.
This License Agreement will automatically terminate upon a material breach of its terms and conditions.
This License Agreement shall be governed by and interpreted in all respects by the law of the State of California, excluding conflict of law provisions. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between BeOpen and Licensee. This License Agreement does not grant permission to use BeOpen trademarks or trade names in a trademark sense to endorse or promote products or services of Licensee, or any third party. As an exception, the "BeOpen Python" logos available at http://www.pythonlabs.com/logos.html may be used according to the permissions granted on that web page.
By copying, installing or otherwise using the software, Licensee agrees to be bound by the terms and conditions of this License Agreement.
```

<!-- page: 106 -->

```txt
1. This LICENSE AGREEMENT is between the Corporation for National Research Initiatives, having an office at 1895 Preston White Drive, Reston, VA 20191 ("CNRI"), and the Individual or Organization ("Licensee") accessing and otherwise using Python 1.6.1 software in source or binary form and its associated documentation.
2. Subject to the terms and conditions of this License Agreement, CNRI hereby grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use Python 1.6.1 alone or in any derivative version, provided, however, that CNRI's License Agreement and CNRI's notice of copyright, i.e., "Copyright © 1995-2001 Corporation for National Research Initiatives; All Rights Reserved" are retained in Python 1.6.1 alone or in any derivative version prepared by Licensee. Alternately, in lieu of CNRI's License Agreement, Licensee may substitute the following text (omitting the quotes): "Python 1.6.1 is made available subject to the terms and conditions in CNRI's License Agreement. This Agreement together with Python 1.6.1 may be located on the Internet using the following unique, persistent identifier (known as a handle): 1895.22/1013. This Agreement may also be obtained from a proxy server on the Internet using the following URL: http://hdl.handle.net/1895.22/1013."
3. In the event Licensee prepares a derivative work that is based on or incorporates Python 1.6.1 or any part thereof, and wants to make the derivative work available to others as provided herein, then Licensee hereby agrees to include in any such work a brief summary of the changes made to Python 1.6.1.
4. CNRI is making Python 1.6.1 available to Licensee on an "AS IS" basis. CNRI MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, CNRI MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON 1.6.1 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
5. CNRI SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 1.6.1 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 1.6.1, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.
6. This License Agreement will automatically terminate upon a material breach of its terms and conditions.
7. This License Agreement shall be governed by the federal intellectual property law of the United States, including without limitation the federal copyright law, and, to the extent such U.S. federal law does not apply, by the law of the Commonwealth of Virginia, excluding Virginia's conflict of law provisions. Notwithstanding the foregoing, with regard to derivative works based on Python 1.6.1 that incorporate non-separable material that was previously distributed under the GNU General Public License (GPL), the law of the Commonwealth of Virginia shall govern this License Agreement only as to issues arising under or with respect to Paragraphs 4, 5, and 7 of this License Agreement. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between CNRI and Licensee. This License Agreement does not grant permission to use CNRI trademarks or trade name in a trademark sense to endorse or promote products or services of Licensee, or any third party.
```

## C.2.3 CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1

(continues on next page)

<!-- page: 107 -->

```txt
8. By clicking on the "ACCEPT" button where indicated, or by copying, installing or otherwise using Python 1.6.1, Licensee agrees to be bound by the terms and conditions of this License Agreement.
```

(continued from previous page)

## C.2.4 CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2

```txt
Copyright © 1991 - 1995, Stichting Mathematisch Centrum Amsterdam, The Netherlands. All rights reserved.

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Stichting Mathematisch Centrum or CWI not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

STICHTING MATHEMATISCH CENTRUM DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL STICHTING MATHEMATISCH CENTRUM BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3 Licenses and Acknowledgements for Incorporated Software

This section is an incomplete, but growing list of licenses and acknowledgements for third-party software incorporated in the Python distribution.

## C.3.1 Mersenne Twister

The \_random module includes code based on a download from [http://www.math.sci.hiroshima-u.ac.jp/\~m-mat/MT/MT2002/emt19937ar.html](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/emt19937ar.html). The following are the verbatim comments from the original code:

```txt
A C-program for MT19937, with initialization improved 2002/1/26.
Coded by Takuji Nishimura and Makoto Matsumoto.

Before using, initialize the state by using init_genrand(seed)
or init_by_array(init_key, key_length).

Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
```

(continues on next page)

<!-- page: 108 -->

(continued from previous page)

```txt
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. The names of its contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Any feedback is very welcome.
http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
email: m-mat @ math.sci.hiroshima-u.ac.jp (remove space)
```

## C.3.2 Sockets

The socket module uses the functions, getaddrinfo(), and getnameinfo(), which are coded in separate source files from the WIDE Project, [http://www.wide.ad.jp/](http://www.wide.ad.jp/).

```txt
Copyright (C) 1995, 1996, 1997, and 1998 WIDE Project.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the project nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
```

(continues on next page)

<!-- page: 109 -->

(continued from previous page)

```txt
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.3 Floating point exception control

The source for the fpectl module includes the following notice:

```txt
Copyright (c) 1996.
The Regents of the University of California.
All rights reserved.

Permission to use, copy, modify, and distribute this software for any purpose without fee is hereby granted, provided that this entire notice is included in all copies of any software which is or includes a copy or modification of this software and in all copies of the supporting documentation for such software.

This work was produced at the University of California, Lawrence Livermore National Laboratory under contract no. W-7405-ENG-48 between the U.S. Department of Energy and The Regents of the University of California for the operation of UC LLNL.
```

## DISCLAIMER

```txt
This software was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor the University of California nor any of their employees, makes any warranty, express or implied, or assumes any liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately-owned rights. Reference herein to any specific commercial products, process, or service by trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or the University of California. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or the University of California, and shall not be used for advertising or product endorsement purposes.
```

## C.3.4 MD5 message digest algorithm

The source code for the md5 module contains the following notice:

```txt
Copyright (C) 1999, 2002 Aladdin Enterprises. All rights reserved.
This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.
```

(continues on next page)

<!-- page: 110 -->

(continued from previous page)

```txt
Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.

L. Peter Deutsch
ghost@aladdin.com

Independent implementation of MD5 (RFC 1321).

This code implements the MD5 Algorithm defined in RFC 1321, whose text is available at
    http://www.ietf.org/rfc/rfc1321.txt
The code is derived from the text of the RFC, including the test suite (section A.5) but excluding the rest of Appendix A. It does not include any code or documentation that is identified in the RFC as being copyrighted.

The original and principal author of md5.h is L. Peter Deutsch <ghost@aladdin.com>. Other authors are noted in the change history that follows (in reverse chronological order):

2002-04-13 lpd Removed support for non-ANSI compilers; removed references to Ghostscript; clarified derivation from RFC 1321; now handles byte order either statically or dynamically.
1999-11-04 lpd Edited comments slightly for automatic TOC extraction.
1999-10-18 lpd Fixed typo in header comment (ansi2knr rather than md5); added conditionalization for C++ compilation from Martin Purschke <purschke@bnl.gov>.
1999-05-03 lpd Original version.
```

## C.3.5 Asynchronous socket services

The asynchat and asyncore modules contain the following notice:

```txt
Copyright 1996 by Sam Rushing

All Rights Reserved

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Sam Rushing not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.
```

(continues on next page)

<!-- page: 111 -->

(continued from previous page)

```txt
SAM RUSHING DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL SAM RUSHING BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.6 Cookie management

The Cookie module contains the following notice:

```txt
Copyright 2000 by Timothy O'Malley <timo@alum.mit.edu>

All Rights Reserved

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Timothy O'Malley not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

Timothy O'Malley DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL Timothy O'Malley BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.7 Execution tracing

The trace module contains the following notice:

```txt
portions copyright 2001, Autonomous Zones Industries, Inc., all rights...
err... reserved and offered to the public under the terms of the
Python 2.2 license.
Author: Zooko O'Whielacronx
http://zooko.com/
mailto:zooko@zooko.com

Copyright 2000, Mojam Media, Inc., all rights reserved.
Author: Skip Montanaro

Copyright 1999, Bioreason, Inc., all rights reserved.
Author: Andrew Dalke

Copyright 1995-1997, Automatrix, Inc., all rights reserved.
Author: Skip Montanaro
```

(continues on next page)

<!-- page: 112 -->

(continued from previous page)

```txt
Copyright 1991-1995, Stichting Mathematisch Centrum, all rights reserved.

Permission to use, copy, modify, and distribute this Python software and its associated documentation for any purpose without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of neither Automatrix, Bioreason or Mojam Media be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.
```

## C.3.8 UUencode and UUdecode functions

The uu module contains the following notice:

```txt
Copyright 1994 by Lance Ellinghouse
Cathedral City, California Republic, United States of America.
All Rights Reserved

Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Lance Ellinghouse not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

LANCE ELLINGHOUSE DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL LANCE ELLINGHOUSE CENTRUM BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Modified by Jack Jansen, CWI, July 1995:
- Use binascii module to do the actual line-by-line conversion between ascii and binary. This results in a 1000-fold speedup. The C version is still 5 times faster, though.
- Arguments more compliant with Python standard
```

## C.3.9 XML Remote Procedure Calls

The xmlrpclib module contains the following notice:

```txt
The XML-RPC client interface is

Copyright (c) 1999-2002 by Secret Labs AB
Copyright (c) 1999-2002 by Fredrik Lundh

By obtaining, using, and/or copying this software and/or its associated documentation, you agree that you have read, understood, and will comply with the following terms and conditions:
```

(continues on next page)

<!-- page: 113 -->

(continued from previous page)

```txt
Permission to use, copy, modify, and distribute this software and its associated documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Secret Labs AB or the author not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## C.3.10 test\_epoll

The test\_epoll contains the following notice:

```txt
Copyright (c) 2001-2006 Twisted Matrix Laboratories.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## C.3.11 Select kqueue

The select and contains the following notice for the kqueue interface:

```txt
Copyright (c) 2000 Doug White, 2006 James Knight, 2007 Christian Heimes All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
```

(continues on next page)

<!-- page: 114 -->

(continued from previous page)

```txt
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## C.3.12 strtod and dtoa

The file Python/dtoa.c, which supplies C functions dtoa and strtod for conversion of C doubles to and from strings, is derived from the file of the same name by David M. Gay, currently available from [http://www.netlib.org/fp/](http://www.netlib.org/fp/). The original file, as retrieved on March 16, 2009, contains the following copyright and licensing notice:

```c
/******************************************************************
*
* The author of this software is David M. Gay.
*
* Copyright (c) 1991, 2000, 2001 by Lucent Technologies.
*
* Permission to use, copy, modify, and distribute this software for any
* purpose without fee is hereby granted, provided that this entire notice
* is included in all copies of any software which is or includes a copy
* or modification of this software and in all copies of the supporting
* documentation for such software.
*
* THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
* WARRANTY. IN PARTICULAR, NEITHER THE AUTHOR NOR LUCENT MAKES ANY
* REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY
* OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.
*
**********************************************************************/
```

## C.3.13 OpenSSL

The modules hashlib, posix, ssl, crypt use the OpenSSL library for added performance if made available by the operating system. Additionally, the Windows and Mac OS X installers for Python may include a copy of the OpenSSL libraries, so we include a copy of the OpenSSL license here:

```txt
LICENSE ISSUES
================

The OpenSSL toolkit stays under a dual license, i.e. both the conditions of
```

(continues on next page)

<!-- page: 115 -->

(continued from previous page)

```txt
the OpenSSL License and the original SSLeay license apply to the toolkit.
See below for the actual license texts. Actually both licenses are BSD-style
Open Source licenses. In case of any license issues related to OpenSSL
please contact openssl-core@openssl.org.

OpenSSL License
-----------------------------------
/* ====================
* Copyright (c) 1998-2008 The OpenSSL Project. All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
*
* 1. Redistributions of source code must retain the above copyright
* notice, this list of conditions and the following disclaimer.
*
* 2. Redistributions in binary form must reproduce the above copyright
* notice, this list of conditions and the following disclaimer in
* the documentation and/or other materials provided with the
* distribution.
*
* 3. All advertising materials mentioning features or use of this
* software must display the following acknowledgment:
* "This product includes software developed by the OpenSSL Project
* for use in the OpenSSL Toolkit. (http://www.openssl.org/)"
*
* 4. The names "OpenSSL Toolkit" and "OpenSSL Project" must not be used to
* endorse or promote products derived from this software without
* prior written permission. For written permission, please contact
* openssl-core@openssl.org.
*
* 5. Products derived from this software may not be called "OpenSSL"
* nor may "OpenSSL" appear in their names without prior written
* permission of the OpenSSL Project.
*
* 6. Redistributions of any form whatsoever must retain the following
* acknowledgment:
* "This product includes software developed by the OpenSSL Project
* for use in the OpenSSL Toolkit (http://www.openssl.org/)"
*
* THIS SOFTWARE IS PROVIDED BY THE OpenSSL PROJECT ``AS IS'' AND ANY
* EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
* PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE OpenSSL PROJECT OR
* ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
* SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
* NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
* STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
* ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
* OF THE POSSIBILITY OF SUCH DAMAGE.
* ====================
*
* This product includes cryptographic software written by Eric Young
```

(continues on next page)

<!-- page: 116 -->

(continued from previous page)

```txt
*(eay@cryptsoft.com). This product includes software written by Tim
* Hudson (tjh@cryptsoft.com).
*
*/

Original SSLeay License
------------------------------------------------------------------*

/* Copyright (C) 1995-1998 Eric Young (eay@cryptsoft.com)
* All rights reserved.
*
* This package is an SSL implementation written
* by Eric Young (eay@cryptsoft.com).
* The implementation was written so as to conform with Netscapes SSL.
*
* This library is free for commercial and non-commercial use as long as
* the following conditions are aheared to. The following conditions
* apply to all code found in this distribution, be it the RC4, RSA,
* lhash, DES, etc., code; not just the SSL code. The SSL documentation
* included with this distribution is covered by the same copyright terms
* except that the holder is Tim Hudson (tjh@cryptsoft.com).
*
* Copyright remains Eric Young's, and as such any Copyright notices in
* the code are not to be removed.
* If this package is used in a product, Eric Young should be given attribution
* as the author of the parts of the library used.
* This can be in the form of a textual message at program startup or
* in documentation (online or textual) provided with the package.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
* 1. Redistributions of source code must retain the copyright
* notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
* notice, this list of conditions and the following disclaimer in the
* documentation and/or other materials provided with the distribution.
* 3. All advertising materials mentioning features or use of this software
* must display the following acknowledgement:
* "This product includes cryptographic software written by
* Eric Young (eay@cryptsoft.com)"
* The word 'cryptographic' can be left out if the routines from the library
* being used are not cryptographic related :-).
* 4. If you include any Windows specific code (or a derivative thereof) from
* the apps directory (application code) you must include an acknowledgement:
* "This product includes software written by Tim Hudson (tjh@cryptsoft.com)"
*
* THIS SOFTWARE IS PROVIDED BY ERIC YOUNG ``AS IS'' AND
* ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
* ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
* OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
```

(continues on next page)

<!-- page: 117 -->

(continued from previous page)

```txt
* SUCH DAMAGE.
*
* The licence and distribution terms for any publically available version or
* derivative of this code cannot be changed. i.e. this code cannot simply be
* copied and put under another distribution licence
* [including the GNU Public Licence.]
*/
```

## C.3.14 expat

The pyexpat extension is built using an included copy of the expat sources unless the build is configured --with-system-expat:

```txt
Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd and Clark Cooper

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## C.3.15 libffi

The \_ctypes extension is built using an included copy of the libffi sources unless the build is configured --with-system-libffi:

```txt
Copyright (c) 1996-2008 Red Hat, Inc and others.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ``Software''), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```

(continues on next page)

<!-- page: 118 -->

```txt
THE SOFTWARE IS PROVIDED ``AS IS'', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

(continued from previous page)

## C.3.16 zlib

The zlib extension is built using an included copy of the zlib sources if the zlib version found on the system is too old to be used for the build:

```txt
Copyright (C) 1995-2010 Jean-loup Gailly and Mark Adler

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source distribution.

Jean-loup Gailly          Mark Adler
jloup@gzip.org           madler@alumni.caltech.edu
```

<!-- page: 119 -->

## COPYRIGHT

Python and this documentation is:

Copyright © 2001-2020 Python Software Foundation. All rights reserved.

Copyright © 2000 BeOpen.com. All rights reserved.

Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.

Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.

See History and License for complete license and permissions information.

<!-- page: 120 -->

<!-- page: 121 -->

## Non-alphabetical

..., **89** 2to3, **89** >>>, **89** future\_\_, 91 slots\_\_, 96

## A

abstract base class, **89** argument, **89** difference from parameter, 17 attribute, **89**

## B

BDFL, **89** bytecode, **90** bytes-like object, **90**

## C

class, **90** classic class, **90** coercion, **90** complex number, **90** context manager, **90** CPython, **90**

## D

decorator, **90** descriptor, **90** dictionary, **91** dictionary view, **91** docstring, **91** duck-typing, **91**

## E

EAFP, **91** environment variable PATH, 55, 56 TCL\_LIBRARY, 84 TK\_LIBRARY, 84 expression, **91**

extension module, **91**

## F

file object, **91** file-like object, **91** finder, **91** floor division, **91** function, **91**

## G

garbage collection, **92** generator, **92** generator expression, **92** GIL, **92** global interpreter lock, **92**

## H

hashable, **92**

## I

IDLE, **92** immutable, **92** importer, **93** importing, **93** integer division, **92** interactive, **93** interpreted, **93** iterable, **93** iterator, **93**

## K

key function, **93** keyword argument, **93**

lambda, **93** LBYL, **93** list, **94** list comprehension, **94** loader, **94**

<!-- page: 122 -->

## M

magic method, 94 magic method, **94** mapping, **94** metaclass, **94** method, **94** magic, 94 special, 96 method resolution order, **94** module, **94** MRO, **94** mutable, **94**

## N

named tuple, **94** namespace, **94** nested scope, **95** new-style class, **95**

object, **95**

## P

package, **95** parameter, **95** difference from argument, 17 PATH, 55, 56 PEP, **95** positional argument, **95** Python 3000, **95** Python Enhancement Proposals PEP 1, 95 PEP 5, 6 PEP 6, 2 PEP 8, 10, 81 PEP 238, 24, 91 PEP 275, 46 PEP 278, 96 PEP 302, 91, 94 PEP 343, 90 PEP 3116, 96 Pythonic, **95**

## R

reference count, **96**

## S

sequence, **96** slice, **96** special method, 96 special method, **96** statement, **96** struct sequence, **96**

## T

TCL\_LIBRARY, 84 TK\_LIBRARY, 84 triple-quoted string, **96** type, **96**

universal newlines, **96**

## V

virtual environment, **96** virtual machine, **96**

## Z

Zen of Python, **96**

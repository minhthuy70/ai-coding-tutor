# EN_PY_081: Regular Expression HOWTO: Metacharacters, Character Classes, and re Module

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Regex | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

Regular Expression HOWTO
************************

Author:
   A.M. Kuchling <amk@amk.ca>

Abstract
^^^^^^^^

This document is an introductory tutorial to using regular expressions
in Python with the "re" module.  It provides a gentler introduction
than the corresponding section in the Library Reference.

Introduction
============

Regular expressions (called REs, or regexes, or regex patterns) are
essentially a tiny, highly specialized programming language embedded
inside Python and made available through the "re" module. Using this
little language, you specify the rules for the set of possible strings
that you want to match; this set might contain English sentences, or
e-mail addresses, or TeX commands, or anything you like.  You can then
ask questions such as “Does this string match the pattern?”, or “Is
there a match for the pattern anywhere in this string?”.  You can also
use REs to modify a string or to split it apart in various ways.

Regular expression patterns are compiled into a series of bytecodes
which are then executed by a matching engine written in C.  For
advanced use, it may be necessary to pay careful attention to how the
engine will execute a given RE, and write the RE in a certain way in
order to produce bytecode that runs faster. Optimization isn’t covered
in this document, because it requires that you have a good

understanding of the matching engine’s internals.

The regular expression language is relatively small and restricted, so
not all possible string processing tasks can be done using regular
expressions.  There are also tasks that *can* be done with regular
expressions, but the expressions turn out to be very complicated.  In
these cases, you may be better off writing Python code to do the
processing; while Python code will be slower than an elaborate regular
expression, it will also probably be more understandable.

Simple Patterns
===============

We’ll start by learning about the simplest possible regular
expressions.  Since regular expressions are used to operate on
strings, we’ll begin with the most common task: matching characters.

For a detailed explanation of the computer science underlying regular
expressions (deterministic and non-deterministic finite automata), you
can refer to almost any textbook on writing compilers.

Matching Characters
-------------------

Most letters and characters will simply match themselves.  For
example, the regular expression "test" will match the string "test"
exactly.  (You can enable a case-insensitive mode that would let this
RE match "Test" or "TEST" as well; more about this later.)

There are exceptions to this rule; some characters are special
*metacharacters*, and don’t match themselves.  Instead, they signal
that some out-of-the-ordinary thing should be matched, or they affect
other portions of the RE by repeating them or changing their meaning.
Much of this document is devoted to discussing various metacharacters
and what they do.

Here’s a complete list of the metacharacters; their meanings will be
discussed in the rest of this HOWTO.

   . ^ $ * + ? { } [ ] \ | ( )

The first metacharacters we’ll look at are "[" and "]". They’re used
for specifying a character class, which is a set of characters that

you wish to match.  Characters can be listed individually, or a range
of characters can be indicated by giving two characters and separating
them by a "'-'".  For example, "[abc]" will match any of the
characters "a", "b", or "c"; this is the same as "[a-c]", which uses a
range to express the same set of characters.  If you wanted to match
only lowercase letters, your RE would be "[a-z]".

Metacharacters (except "\") are not active inside classes.  For
example, "[akm$]" will match any of the characters "'a'", "'k'",
"'m'", or "'$'"; "'$'" is usually a metacharacter, but inside a
character class it’s stripped of its special nature.

You can match the characters not listed within the class by
*complementing* the set.  This is indicated by including a "'^'" as
the first character of the class. For example, "[^5]" will match any
character except "'5'".  If the caret appears elsewhere in a character
class, it does not have special meaning. For example: "[5^]" will
match either a "'5'" or a "'^'".

Perhaps the most important metacharacter is the backslash, "\".   As
in Python string literals, the backslash can be followed by various
characters to signal various special sequences.  It’s also used to
escape all the metacharacters so you can still match them in patterns;
for example, if you need to match a "[" or  "\", you can precede them
with a backslash to remove their special meaning: "\[" or "\\".

Some of the special sequences beginning with "'\'" represent
predefined sets of characters that are often useful, such as the set
of digits, the set of letters, or the set of anything that isn’t
whitespace.

Let’s take an example: "\w" matches any alphanumeric character.  If
the regex pattern is expressed in bytes, this is equivalent to the
class "[a-zA-Z0-9_]".  If the regex pattern is a string, "\w" will
match all the characters marked as letters in the Unicode database
provided by the "unicodedata" module.  You can use the more restricted
definition of "\w" in a string pattern by supplying the "re.ASCII"
flag when compiling the regular expression.

The following list of special sequences isn’t complete. For a complete
list of sequences and expanded class definitions for Unicode string
patterns, see the last part of Regular Expression Syntax in the
Standard Library reference.  In general, the Unicode versions match
any character that’s in the appropriate category in the Unicode
database.

"\d"

```python
Matches any decimal digit; this is equivalent to the class "[0-9]".

```

"\D"
   Matches any non-digit character; this is equivalent to the class
   "[^0-9]".

"\s"
   Matches any whitespace character; this is equivalent to the class
   "[ \t\n\r\f\v]".

"\S"
   Matches any non-whitespace character; this is equivalent to the

```python
class "[^ \t\n\r\f\v]".

```

"\w"
   Matches any alphanumeric character; this is equivalent to the class
   "[a-zA-Z0-9_]".

"\W"
   Matches any non-alphanumeric character; this is equivalent to the

```python
class "[^a-zA-Z0-9_]".

```

These sequences can be included inside a character class.  For
example, "[\s,.]" is a character class that will match any whitespace
character, or "','" or "'.'".

The final metacharacter in this section is ".".  It matches anything
except a newline character, and there’s an alternate mode
("re.DOTALL") where it will match even a newline.  "." is often used
where you want to match “any character”.

Repeating Things
----------------

Being able to match varying sets of characters is the first thing
regular expressions can do that isn’t already possible with the

methods available on strings.  However, if that was the only
additional capability of regexes, they wouldn’t be much of an advance.
Another capability is that you can specify that portions of the RE
must be repeated a certain number of times.

The first metacharacter for repeating things that we’ll look at is
"*".  "*" doesn’t match the literal character "'*'"; instead, it
specifies that the previous character can be matched zero or more
times, instead of exactly once.

For example, "ca*t" will match "'ct'" (0 "'a'" characters), "'cat'" (1
"'a'"), "'caaat'" (3 "'a'" characters), and so forth.

Repetitions such as "*" are *greedy*; when repeating a RE, the
matching engine will try to repeat it as many times as possible. If
later portions of the pattern don’t match, the matching engine will
then back up and try again with fewer repetitions.

A step-by-step example will make this more obvious.  Let’s consider
the expression "a[bcd]*b".  This matches the letter "'a'", zero or
more letters from the class "[bcd]", and finally ends with a "'b'".
Now imagine matching this RE against the string "'abcbd'".

+--------+-------------+-----------------------------------+
| Step   | Matched     | Explanation                       |
|========|=============|===================================|
| 1      | "a"         | The "a" in the RE matches.        |
+--------+-------------+-----------------------------------+
| 2      | "abcbd"     | The engine matches "[bcd]*",      |
|        |             | going as far as it can, which is  |
|        |             | to the end of the string.         |
+--------+-------------+-----------------------------------+
| 3      | *Failure*   | The engine tries to match "b",    |
|        |             | but the current position is at    |
|        |             | the end of the string, so it      |
|        |             | fails.                            |
+--------+-------------+-----------------------------------+
| 4      | "abcb"      | Back up, so that  "[bcd]*"        |
|        |             | matches one less character.       |
+--------+-------------+-----------------------------------+
| 5      | *Failure*   | Try "b" again, but the current    |
|        |             | position is at the last           |
|        |             | character, which is a "'d'".      |
+--------+-------------+-----------------------------------+
| 6      | "abc"       | Back up again, so that "[bcd]*"   |

|        |             | is only matching "bc".            |
+--------+-------------+-----------------------------------+
| 6      | "abcb"      | Try "b" again.  This time the     |
|        |             | character at the current position |
|        |             | is "'b'", so it succeeds.         |
+--------+-------------+-----------------------------------+

The end of the RE has now been reached, and it has matched "'abcb'".
This demonstrates how the matching engine goes as far as it can at
first, and if no match is found it will then progressively back up and
retry the rest of the RE again and again.  It will back up until it
has tried zero matches for "[bcd]*", and if that subsequently fails,
the engine will conclude that the string doesn’t match the RE at all.

Another repeating metacharacter is "+", which matches one or more
times.  Pay careful attention to the difference between "*" and "+";
"*" matches *zero* or more times, so whatever’s being repeated may not
be present at all, while "+" requires at least *one* occurrence.  To
use a similar example, "ca+t" will match "'cat'" (1 "'a'"), "'caaat'"
(3 "'a'"s), but won’t match "'ct'".

There are two more repeating operators or quantifiers.  The question
mark character, "?", matches either once or zero times; you can think
of it as marking something as being optional.  For example,
"home-?brew" matches either "'homebrew'" or "'home-brew'".

The most complicated quantifier is "{m,n}", where *m* and *n* are
decimal integers.  This quantifier means there must be at least *m*
repetitions, and at most *n*.  For example, "a/{1,3}b" will match
"'a/b'", "'a//b'", and "'a///b'".  It won’t match "'ab'", which has no
slashes, or "'a////b'", which has four.

You can omit either *m* or *n*; in that case, a reasonable value is
assumed for the missing value.  Omitting *m* is interpreted as a lower
limit of 0, while omitting *n* results in an upper bound of infinity.

The simplest case "{m}" matches the preceding item exactly *m* times.
For example, "a/{2}b" will only match "'a//b'".

Readers of a reductionist bent may notice that the three other
quantifiers can all be expressed using this notation.  "{0,}" is the
same as "*", "{1,}" is equivalent to "+", and "{0,1}" is the same as
"?".  It’s better to use "*", "+", or "?" when you can, simply because
they’re shorter and easier to read.

Using Regular Expressions
=========================

Now that we’ve looked at some simple regular expressions, how do we
actually use them in Python?  The "re" module provides an interface to
the regular expression engine, allowing you to compile REs into
objects and then perform matches with them.

Compiling Regular Expressions
-----------------------------

Regular expressions are compiled into pattern objects, which have
methods for various operations such as searching for pattern matches
or performing string substitutions.

```python
>>> import re
>>> p = re.compile('ab*')
>>> p
re.compile('ab*')

```

"re.compile()" also accepts an optional *flags* argument, used to
enable various special features and syntax variations.  We’ll go over
the available settings later, but for now a single example will do:

```python
>>> p = re.compile('ab*', re.IGNORECASE)

```

The RE is passed to "re.compile()" as a string.  REs are handled as
strings because regular expressions aren’t part of the core Python
language, and no special syntax was created for expressing them.
(There are applications that don’t need REs at all, so there’s no need
to bloat the language specification by including them.) Instead, the
"re" module is simply a C extension module included with Python, just
like the "socket" or "zlib" modules.

Putting REs in strings keeps the Python language simpler, but has one
disadvantage which is the topic of the next section.

The Backslash Plague

--------------------

As stated earlier, regular expressions use the backslash character
("'\'") to indicate special forms or to allow special characters to be
used without invoking their special meaning. This conflicts with
Python’s usage of the same character for the same purpose in string
literals.

Let’s say you want to write a RE that matches the string "\section",
which might be found in a LaTeX file.  To figure out what to write in
the program code, start with the desired string to be matched.  Next,
you must escape any backslashes and other metacharacters by preceding
them with a backslash, resulting in the string "\\section".  The
resulting string that must be passed to "re.compile()" must be
"\\section".  However, to express this as a Python string literal,
both backslashes must be escaped *again*.

+---------------------+--------------------------------------------+
| Characters          | Stage                                      |
|=====================|============================================|
| "\section"          | Text string to be matched                  |
+---------------------+--------------------------------------------+
| "\\section"         | Escaped backslash for "re.compile()"       |
+---------------------+--------------------------------------------+
| ""\\\\section""     | Escaped backslashes for a string literal   |
+---------------------+--------------------------------------------+

In short, to match a literal backslash, one has to write "'\\\\'" as
the RE string, because the regular expression must be "\\", and each
backslash must be expressed as "\\" inside a regular Python string
literal.  In REs that feature backslashes repeatedly, this leads to
lots of repeated backslashes and makes the resulting strings difficult
to understand.

The solution is to use Python’s raw string notation for regular
expressions; backslashes are not handled in any special way in a
string literal prefixed with "'r'", so "r"\n"" is a two-character
string containing "'\'" and "'n'", while ""\n"" is a one-character
string containing a newline. Regular expressions will often be written
in Python code using this raw string notation.

In addition, special escape sequences that are valid in regular
expressions, but not valid as Python string literals, now result in a
"DeprecationWarning" and will eventually become a "SyntaxError", which
means the sequences will be invalid if raw string notation or escaping

the backslashes isn’t used.

+---------------------+--------------------+
| Regular String      | Raw string         |
|=====================|====================|
| ""ab*""             | "r"ab*""           |
+---------------------+--------------------+
| ""\\\\section""     | "r"\\section""     |
+---------------------+--------------------+
| ""\\w+\\s+\\1""     | "r"\w+\s+\1""      |
+---------------------+--------------------+

Performing Matches
------------------

Once you have an object representing a compiled regular expression,
what do you do with it?  Pattern objects have several methods and
attributes. Only the most significant ones will be covered here;
consult the "re" docs for a complete listing.

+--------------------+-------------------------------------------------+
| Method/Attribute   | Purpose                                         |
|====================|=================================================|
| "match()"          | Determine if the RE matches at the beginning of |
|                    | the string.                                     |
+--------------------+-------------------------------------------------+
| "search()"         | Scan through a string, looking for any location |
|                    | where this RE matches.                          |
+--------------------+-------------------------------------------------+
| "findall()"        | Find all substrings where the RE matches, and   |
|                    | returns them as a list.                         |
+--------------------+-------------------------------------------------+
| "finditer()"       | Find all substrings where the RE matches, and   |
|                    | returns them as an *iterator*.                  |
+--------------------+-------------------------------------------------+

"match()" and "search()" return "None" if no match can be found.  If
they’re successful, a match object instance is returned, containing
information about the match: where it starts and ends, the substring
it matched, and more.

You can learn about this by interactively experimenting with the "re"
module.

This HOWTO uses the standard Python interpreter for its examples.
First, run the Python interpreter, import the "re" module, and compile
a RE:

```python
>>> import re
>>> p = re.compile('[a-z]+')
>>> p
re.compile('[a-z]+')

```

Now, you can try matching various strings against the RE "[a-z]+".  An
empty string shouldn’t match at all, since "+" means ‘one or more
repetitions’. "match()" should return "None" in this case, which will
cause the interpreter to print no output.  You can explicitly print
the result of "match()" to make this clear.

```python
>>> p.match("")
```
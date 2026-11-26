# EN_PY_082: Regular Expression HOWTO: Grouping, Capturing, Non-Capturing, and Lookahead

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Regex | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

```python
>>> print(p.match(""))
None

```

Now, let’s try it on a string that it should match, such as "tempo".
In this case, "match()" will return a match object, so you should
store the result in a variable for later use.

```python
>>> m = p.match('tempo')
>>> m
<re.Match object; span=(0, 5), match='tempo'>

```

Now you can query the match object for information about the matching
string.  Match object instances also have several methods and
attributes; the most important ones are:

+--------------------+----------------------------------------------+
| Method/Attribute   | Purpose                                      |
|====================|==============================================|
| "group()"          | Return the string matched by the RE          |
+--------------------+----------------------------------------------+
| "start()"          | Return the starting position of the match    |
+--------------------+----------------------------------------------+
| "end()"            | Return the ending position of the match      |
+--------------------+----------------------------------------------+
| "span()"           | Return a tuple containing the (start, end)   |
|                    | positions  of the match                      |
+--------------------+----------------------------------------------+

Trying these methods will soon clarify their meaning:

```python
>>> m.group()
'tempo'
>>> m.start(), m.end()
(0, 5)
>>> m.span()
(0, 5)

```

"group()" returns the substring that was matched by the RE.  "start()"
and "end()" return the starting and ending index of the match.
"span()" returns both start and end indexes in a single tuple.  Since
the "match()" method only checks if the RE matches at the start of a
string, "start()" will always be zero.  However, the "search()" method
of patterns scans through the string, so  the match may not start at
zero in that case.

```python
>>> print(p.match('::: message'))
None
>>> m = p.search('::: message'); print(m)
<re.Match object; span=(4, 11), match='message'>
>>> m.group()
'message'
>>> m.span()
(4, 11)

```

In actual programs, the most common style is to store the match object
in a variable, and then check if it was "None".  This usually looks
like:

   p = re.compile( ... )
   m = p.match( 'string goes here' )

```python
if m:
    print('Match found: ', m.group())
else:
    print('No match')

```

Two pattern methods return all of the matches for a pattern.
"findall()" returns a list of matching strings:

```python
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']

```

The "r" prefix, making the literal a raw string literal, is needed in
this example because escape sequences in a normal “cooked” string
literal that are not recognized by Python, as opposed to regular
expressions, now result in a "DeprecationWarning" and will eventually
become a "SyntaxError".  See The Backslash Plague.

"findall()" has to create the entire list before it can be returned as
the result.  The "finditer()" method returns a sequence of match
object instances as an *iterator*:

```python
>>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
>>> iterator
<callable_iterator object at 0x...>
>>> for match in iterator:
...     print(match.span())
...
(0, 2)
(22, 24)
(29, 31)

```

Module-Level Functions
----------------------

You don’t have to create a pattern object and call its methods; the
"re" module also provides top-level functions called "match()",
"search()", "findall()", "sub()", and so forth.  These functions take
the same arguments as the corresponding pattern method with the RE
string added as the first argument, and still return either "None" or
a match object instance.

```python
>>> print(re.match(r'From\s+', 'Fromage amk'))
None
>>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
<re.Match object; span=(0, 5), match='From '>

```

Under the hood, these functions simply create a pattern object for you
and call the appropriate method on it.  They also store the compiled
object in a cache, so future calls using the same RE won’t need to
parse the pattern again and again.

Should you use these module-level functions, or should you get the
pattern and call its methods yourself?  If you’re accessing a regex
within a loop, pre-compiling it will save a few function calls.
Outside of loops, there’s not much difference thanks to the internal
cache.

Compilation Flags
-----------------

Compilation flags let you modify some aspects of how regular
expressions work. Flags are available in the "re" module under two
names, a long name such as "IGNORECASE" and a short, one-letter form
such as "I".  (If you’re familiar with Perl’s pattern modifiers, the
one-letter forms use the same letters; the short form of "re.VERBOSE"
is "re.X", for example.) Multiple flags can be specified by bitwise
OR-ing them; "re.I | re.M" sets both the "I" and "M" flags, for
example.

Here’s a table of the available flags, followed by a more detailed
explanation of each one.

+-----------------------------------+----------------------------------------------+
| Flag                              | Meaning                                      |
|===================================|==============================================|
| "ASCII", "A"                      | Makes several escapes like "\w", "\b", "\s"  |
|                                   | and "\d" match only on ASCII characters with |
|                                   | the respective property.                     |
+-----------------------------------+----------------------------------------------+
| "DOTALL", "S"                     | Make "." match any character, including      |
|                                   | newlines.                                    |
+-----------------------------------+----------------------------------------------+
| "IGNORECASE", "I"                 | Do case-insensitive matches.                 |
+-----------------------------------+----------------------------------------------+
| "LOCALE", "L"                     | Do a locale-aware match.                     |
+-----------------------------------+----------------------------------------------+
| "MULTILINE", "M"                  | Multi-line matching, affecting "^" and "\$".  |
+-----------------------------------+----------------------------------------------+
| "VERBOSE", "X" (for ‘extended’)   | Enable verbose REs, which can be organized   |
|                                   | more cleanly and understandably.             |
+-----------------------------------+----------------------------------------------+

re.I
re.IGNORECASE

```python
Perform case-insensitive matching; character class and literal
strings will match letters by ignoring case.  For example, "[A-Z]"
will match lowercase letters, too. Full Unicode matching also works
unless the "ASCII" flag is used to disable non-ASCII matches.  When
the Unicode patterns "[a-z]" or "[A-Z]" are used in combination
with the "IGNORECASE" flag, they will match the 52 ASCII letters
and 4 additional non-ASCII letters: ‘İ’ (U+0130, Latin capital
letter I with dot above), ‘ı’ (U+0131, Latin small letter dotless
i), ‘ſ’ (U+017F, Latin small letter long s) and ‘K’ (U+212A, Kelvin
sign).  "Spam" will match "'Spam'", "'spam'", "'spAM'", or "'ſpam'"
(the latter is matched only in Unicode mode). This lowercasing
doesn’t take the current locale into account; it will if you also
set the "LOCALE" flag.

```

re.L
re.LOCALE

   Make "\w", "\W", "\b", "\B" and case-insensitive matching dependent
   on the current locale instead of the Unicode database.

   Locales are a feature of the C library intended to help in writing
   programs that take account of language differences.  For example,

```python
if you’re processing encoded French text, you’d want to be able to
write "\w+" to match words, but "\w" only matches the character
class "[A-Za-z]" in bytes patterns; it won’t match bytes
corresponding to "é" or "ç". If your system is configured properly
and a French locale is selected, certain C functions will tell the
program that the byte corresponding to "é" should also be
considered a letter. Setting the "LOCALE" flag when compiling a
regular expression will cause the resulting compiled object to use
these C functions for "\w"; this is slower, but also enables "\w+"
to match French words as you’d expect. The use of this flag is
discouraged in Python 3 as the locale mechanism is very unreliable,
it only handles one “culture” at a time, and it only works with
8-bit locales.  Unicode matching is already enabled by default in
Python 3 for Unicode (str) patterns, and it is able to handle
different locales/languages.

```

re.M
re.MULTILINE

   ("^" and "$" haven’t been explained yet;  they’ll be introduced in
   section More Metacharacters.)

   Usually "^" matches only at the beginning of the string, and "$"
   matches only at the end of the string and immediately before the

```python
newline (if any) at the end of the string. When this flag is
specified, "^" matches at the beginning of the string and at the
beginning of each line within the string, immediately following
each newline.  Similarly, the "$" metacharacter matches either at
the end of the string and at the end of each line (immediately
preceding each newline).

```

re.S
re.DOTALL

   Makes the "'.'" special character match any character at all,
   including a newline; without this flag, "'.'" will match anything
   *except* a newline.

re.A
re.ASCII

   Make "\w", "\W", "\b", "\B", "\s" and "\S" perform ASCII-only
   matching instead of full Unicode matching. This is only meaningful

```python
for Unicode patterns, and is ignored for byte patterns.

```

re.X
re.VERBOSE

   This flag allows you to write regular expressions that are more
   readable by granting you more flexibility in how you can format
   them.  When this flag has been specified, whitespace within the RE

```python
string is ignored, except when the whitespace is in a character
class or preceded by an unescaped backslash; this lets you organize
and indent the RE more clearly.  This flag also lets you put
comments within a RE that will be ignored by the engine; comments
are marked by a "'#'" that’s neither in a character class or
preceded by an unescaped backslash.

For example, here’s a RE that uses "re.VERBOSE"; see how much
easier it is to read?

   charref = re.compile(r"""
    &[#]                # Start of a numeric entity reference
    (
        0[0-7]+         # Octal form
      | [0-9]+          # Decimal form
      | x[0-9a-fA-F]+   # Hexadecimal form
    )
    ;                   # Trailing semicolon
   """, re.VERBOSE)

Without the verbose setting, the RE would look like this:

   charref = re.compile("&#(0[0-7]+"
                        "|[0-9]+"
                        "|x[0-9a-fA-F]+);")

In the above example, Python’s automatic concatenation of string
literals has been used to break up the RE into smaller pieces, but
it’s still more difficult to understand than the version using
"re.VERBOSE".

```

More Pattern Power
==================

So far we’ve only covered a part of the features of regular
expressions.  In this section, we’ll cover some new metacharacters,
and how to use groups to retrieve portions of the text that was
matched.

More Metacharacters
-------------------

There are some metacharacters that we haven’t covered yet.  Most of
them will be covered in this section.

Some of the remaining metacharacters to be discussed are *zero-width
assertions*.  They don’t cause the engine to advance through the
string; instead, they consume no characters at all, and simply succeed
or fail.  For example, "\b" is an assertion that the current position
is located at a word boundary; the position isn’t changed by the "\b"
at all.  This means that zero-width assertions should never be
repeated, because if they match once at a given location, they can
obviously be matched an infinite number of times.

"|"
   Alternation, or the “or” operator.   If *A* and *B* are regular
   expressions, "A|B" will match any string that matches either *A* or
   *B*. "|" has very low precedence in order to make it work
   reasonably when you’re alternating multi-character strings.
   "Crow|Servo" will match either "'Crow'" or "'Servo'", not "'Cro'",
   a "'w'" or an "'S'", and "'ervo'".

   To match a literal "'|'", use "\|", or enclose it inside a
   character class, as in "[|]".

"^"
   Matches at the beginning of lines.  Unless the "MULTILINE" flag has
   been set, this will only match at the beginning of the string.  In
   "MULTILINE" mode, this also matches immediately after each newline
   within the string.

```python
For example, if you wish to match the word "From" only at the
beginning of a line, the RE to use is "^From".

   >>> print(re.search('^From', 'From Here to Eternity'))
   <re.Match object; span=(0, 4), match='From'>
   >>> print(re.search('^From', 'Reciting From Memory'))
   None

To match a literal "'^'", use "\^".

```

"\$"
   Matches at the end of a line, which is defined as either the end of
   the string, or any location followed by a newline character.

```python
   >>> print(re.search('}$', '{block}'))
   <re.Match object; span=(6, 7), match='}'>
   >>> print(re.search('}$', '{block} '))
   None
   >>> print(re.search('}$', '{block}\n'))
   <re.Match object; span=(6, 7), match='}'>

To match a literal "'$'", use "\$" or enclose it inside a character
class, as in  "[$]".

```

"\A"
   Matches only at the start of the string.  When not in "MULTILINE"
   mode, "\A" and "^" are effectively the same.  In "MULTILINE" mode,
   they’re different: "\A" still matches only at the beginning of the
   string, but "^" may match at any location inside the string that
   follows a newline character.

"\Z"
   Matches only at the end of the string.

"\b"
   Word boundary.  This is a zero-width assertion that matches only at
   the beginning or end of a word.  A word is defined as a sequence of
   alphanumeric characters, so the end of a word is indicated by
   whitespace or a non-alphanumeric character.

   The following example matches "class" only when it’s a complete
   word; it won’t match when it’s contained inside another word.

```python
   >>> p = re.compile(r'\bclass\b')
   >>> print(p.search('no class at all'))
   <re.Match object; span=(3, 8), match='class'>
   >>> print(p.search('the declassified algorithm'))
   None
   >>> print(p.search('one subclass is'))
   None

There are two subtleties you should remember when using this
special sequence. First, this is the worst collision between
Python’s string literals and regular expression sequences.  In
Python’s string literals, "\b" is the backspace character, ASCII
value 8.  If you’re not using raw strings, then Python will convert
the "\b" to a backspace, and your RE won’t match as you expect it
to. The following example looks the same as our previous RE, but
omits the "'r'" in front of the RE string.

   >>> p = re.compile('\bclass\b')
   >>> print(p.search('no class at all'))
   None
   >>> print(p.search('\b' + 'class' + '\b'))
   <re.Match object; span=(0, 7), match='\x08class\x08'>

Second, inside a character class, where there’s no use for this
assertion, "\b" represents the backspace character, for
compatibility with Python’s string literals.

```

"\B"
   Another zero-width assertion, this is the opposite of "\b", only
   matching when the current position is not at a word boundary.

Grouping
--------

Frequently you need to obtain more information than just whether the
RE matched or not.  Regular expressions are often used to dissect
strings by writing a RE divided into several subgroups which match
different components of interest. For example, an RFC-822 header line
is divided into a header name and a value, separated by a "':'", like
this:

   From: author@example.com
   User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
   MIME-Version: 1.0
   To: editor@example.com

This can be handled by writing a regular expression which matches an
entire header line, and has one group which matches the header name,
and another group which matches the header’s value.

Groups are marked by the "'('", "')'" metacharacters. "'('" and "')'"
have much the same meaning as they do in mathematical expressions;
they group together the expressions contained inside them, and you can
repeat the contents of a group with a quantifier, such as "*", "+",
"?", or "{m,n}".  For example, "(ab)*" will match zero or more
repetitions of "ab".

```python
>>> p = re.compile('(ab)*')
>>> print(p.match('ababababab').span())
(0, 10)

```

Groups indicated with "'('", "')'" also capture the starting and
ending index of the text that they match; this can be retrieved by
passing an argument to "group()", "start()", "end()", and "span()".
Groups are numbered starting with 0.  Group 0 is always present; it’s
the whole RE, so match object methods all have group 0 as their
default argument.  Later we’ll see how to express groups that don’t
capture the span of text that they match.

```python
>>> p = re.compile('(a)b')
>>> m = p.match('ab')
>>> m.group()
'ab'
>>> m.group(0)
'ab'

```

Subgroups are numbered from left to right, from 1 upward.  Groups can
be nested; to determine the number, just count the opening parenthesis
characters, going from left to right.

```python
>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group(0)
'abcd'
>>> m.group(1)
'abc'
>>> m.group(2)
'b'

```

"group()" can be passed multiple group numbers at a time, in which
case it will return a tuple containing the corresponding values for
those groups.

```python
>>> m.group(2,1,2)
('b', 'abc', 'b')

```

The "groups()" method returns a tuple containing the strings for all
the subgroups, from 1 up to however many there are.

```python
>>> m.groups()
('abc', 'b')
```
<!-- page: 1 -->
# EN_PY_098: sqlite3 Module: Embedded SQL Database, Transactions, and Parameterized Queries

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Databases | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

"sqlite3" — DB-API 2.0 interface for SQLite databases
*****************************************************

**Source code:** Lib/sqlite3/

SQLite is a C library that provides a lightweight disk-based database
that doesn’t require a separate server process and allows accessing
the database using a nonstandard variant of the SQL query language.
Some applications can use SQLite for internal data storage.  It’s also
possible to prototype an application using SQLite and then port the
code to a larger database such as PostgreSQL or Oracle.

The "sqlite3" module was written by Gerhard Häring.  It provides an
SQL interface compliant with the DB-API 2.0 specification described by
**PEP 249**, and requires SQLite 3.7.15 or newer.

This document includes four main sections:

* Tutorial teaches how to use the "sqlite3" module.

* Reference describes the classes and functions this module defines.

* How-to guides details how to handle specific tasks.

* Explanation provides in-depth background on transaction control.

See also:

  https://www.sqlite.org
     The SQLite web page; the documentation describes the syntax and
```python
the available data types for the supported SQL dialect.

```

<!-- page: 2 -->

  https://www.w3schools.com/sql/
```python
Tutorial, reference and examples for learning SQL syntax.

```
  **PEP 249** - Database API Specification 2.0
     PEP written by Marc-André Lemburg.


Tutorial
========

In this tutorial, you will create a database of Monty Python movies
using basic "sqlite3" functionality. It assumes a fundamental
understanding of database concepts, including cursors and
transactions.

First, we need to create a new database and open a database connection
to allow "sqlite3" to work with it. Call "sqlite3.connect()" to create
a connection to the database "tutorial.db" in the current working
directory, implicitly creating it if it does not exist:

```python
import sqlite3
con = sqlite3.connect("tutorial.db")

```
The returned "Connection" object "con" represents the connection to
the on-disk database.

In order to execute SQL statements and fetch results from SQL queries,
we will need to use a database cursor. Call "con.cursor()" to create
the "Cursor":

   cur = con.cursor()

Now that we’ve got a database connection and a cursor, we can create a
database table "movie" with columns for title, release year, and
review score. For simplicity, we can just use column names in the
table declaration – thanks to the flexible typing feature of SQLite,
specifying the data types is optional. Execute the "CREATE TABLE"
statement by calling "cur.execute(...)":

   cur.execute("CREATE TABLE movie(title, year, score)")


<!-- page: 3 -->

We can verify that the new table has been created by querying the
"sqlite_master" table built-in to SQLite, which should now contain an
entry for the "movie" table definition (see The Schema Table for
details). Execute that query by calling "cur.execute(...)", assign the
result to "res", and call "res.fetchone()" to fetch the resulting row:

```python
>>> res = cur.execute("SELECT name FROM sqlite_master")
>>> res.fetchone()
('movie',)

```
We can see that the table has been created, as the query returns a
"tuple" containing the table’s name. If we query "sqlite_master" for a
non-existent table "spam", "res.fetchone()" will return "None":

```python
>>> res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
>>> res.fetchone() is None
True

```
Now, add two rows of data supplied as SQL literals by executing an
"INSERT" statement, once again by calling "cur.execute(...)":

   cur.execute("""
       INSERT INTO movie VALUES
           ('Monty Python and the Holy Grail', 1975, 8.2),
```python
        ('And Now for Something Completely Different', 1971, 7.5)
""")

```
The "INSERT" statement implicitly opens a transaction, which needs to
be committed before changes are saved in the database (see Transaction
control for details). Call "con.commit()" on the connection object to
commit the transaction:

   con.commit()

We can verify that the data was inserted correctly by executing a
"SELECT" query. Use the now-familiar "cur.execute(...)" to assign the
result to "res", and call "res.fetchall()" to return all resulting
rows:


<!-- page: 4 -->

```python
>>> res = cur.execute("SELECT score FROM movie")
>>> res.fetchall()
[(8.2,), (7.5,)]

```
The result is a "list" of two "tuple"s, one per row, each containing
that row’s "score" value.

Now, insert three more rows by calling "cur.executemany(...)":

   data = [
       ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
       ("Monty Python's The Meaning of Life", 1983, 7.5),
       ("Monty Python's Life of Brian", 1979, 8.0),
   ]
   cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
   con.commit()  # Remember to commit the transaction after executing INSERT.

Notice that "?" placeholders are used to bind "data" to the query.
Always use placeholders instead of string formatting to bind Python
values to SQL statements, to avoid SQL injection attacks (see How to
use placeholders to bind values in SQL queries for more details).

We can verify that the new rows were inserted by executing a "SELECT"
query, this time iterating over the results of the query:

```python
>>> for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
...     print(row)
(1971, 'And Now for Something Completely Different')
(1975, 'Monty Python and the Holy Grail')
(1979, "Monty Python's Life of Brian")
(1982, 'Monty Python Live at the Hollywood Bowl')
(1983, "Monty Python's The Meaning of Life")

```
Each row is a two-item "tuple" of "(year, title)", matching the
columns selected in the query.

Finally, verify that the database has been written to disk by calling
"con.close()" to close the existing connection, opening a new one,
creating a new cursor, then querying the database:

```python
>>> con.close()
>>> new_con = sqlite3.connect("tutorial.db")
>>> new_cur = new_con.cursor()
>>> res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
>>> title, year = res.fetchone()
>>> print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
The highest scoring Monty Python movie is 'Monty Python and the Holy Grail', released in 1975
>>> new_con.close()

```

<!-- page: 5 -->

You’ve now created an SQLite database using the "sqlite3" module,
inserted data and retrieved values from it in multiple ways.

See also:

  * How-to guides for further reading:

    * How to use placeholders to bind values in SQL queries

    * How to adapt custom Python types to SQLite values

    * How to convert SQLite values to custom Python types

    * How to use the connection context manager

    * How to create and use row factories

  * Explanation for in-depth background on transaction control.


Reference
=========


Module functions
----------------

sqlite3.connect(database, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False, *, autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL)

   Open a connection to an SQLite database.

   Parameters:
      * **database** (*path-like object*) – The path to the database
        file to be opened. You can pass "":memory:"" to create an
        SQLite database existing only in memory, and open a connection
        to it.

      * **timeout** (*float*) – How many seconds the connection should
        wait before raising an "OperationalError" when a table is
        locked. If another connection opens a transaction to modify a
        table, that table will be locked until the transaction is
        committed. Default five seconds.

      * **detect_types** (*int*) – Control whether and how data types
        not natively supported by SQLite are looked up to be converted

<!-- page: 6 -->

        to Python types, using the converters registered with
        "register_converter()". Set it to any combination (using "|",
        bitwise or) of "PARSE_DECLTYPES" and "PARSE_COLNAMES" to
        enable this. Column names takes precedence over declared types
```python
     if both flags are set. Types cannot be detected for generated
     fields (for example "max(data)"), even when the *detect_types*
     parameter is set; "str" will be returned instead. By default
     ("0"), type detection is disabled.

   * **isolation_level** (*str** | **None*) – Control legacy
     transaction handling behaviour. See
     "Connection.isolation_level" and Transaction control via the
     isolation_level attribute for more information. Can be
     ""DEFERRED"" (default), ""EXCLUSIVE"" or ""IMMEDIATE""; or
     "None" to disable opening transactions implicitly. Has no
     effect unless "Connection.autocommit" is set to
     "LEGACY_TRANSACTION_CONTROL" (the default).

   * **check_same_thread** (*bool*) – If "True" (default),
     "ProgrammingError" will be raised if the database connection
     is used by a thread other than the one that created it. If
     "False", the connection may be accessed in multiple threads;
     write operations may need to be serialized by the user to
     avoid data corruption. See "threadsafety" for more
     information.

   * **factory** (*Connection*) – A custom subclass of "Connection"
     to create the connection with, if not the default "Connection"
     class.

   * **cached_statements** (*int*) – The number of statements that
     "sqlite3" should internally cache for this connection, to
     avoid parsing overhead. By default, 128 statements.

   * **uri** (*bool*) – If set to "True", *database* is interpreted
     as a URI (Uniform Resource Identifier) with a file path and an
     optional query string. The scheme part *must* be ""file:"",
     and the path can be relative or absolute. The query string
     allows passing parameters to SQLite, enabling various How to
     work with SQLite URIs.

   * **autocommit** (*bool*) – Control **PEP 249** transaction
     handling behaviour. See "Connection.autocommit" and
     Transaction control via the autocommit attribute for more
     information. *autocommit* currently defaults to
     "LEGACY_TRANSACTION_CONTROL". The default will change to
     "False" in a future Python release.

Return type:
   *Connection*

Raises an auditing event "sqlite3.connect" with argument
"database".

Raises an auditing event "sqlite3.connect/handle" with argument
"connection_handle".

Changed in version 3.4: Added the *uri* parameter.

Changed in version 3.7: *database* can now also be a *path-like
object*, not only a string.

Changed in version 3.10: Added the "sqlite3.connect/handle"
auditing event.

Changed in version 3.12: Added the *autocommit* parameter.

```

<!-- page: 7 -->

sqlite3.complete_statement(statement)

```python
Return "True" if the string *statement* appears to contain one or
more complete SQL statements. No syntactic verification or parsing
of any kind is performed, other than checking that there are no
unclosed string literals and the statement is terminated by a
semicolon.

For example:

   >>> sqlite3.complete_statement("SELECT foo FROM bar;")
   True
   >>> sqlite3.complete_statement("SELECT foo")
   False

This function may be useful during command-line input to determine
if the entered text seems to form a complete SQL statement, or if
additional input is needed before calling "execute()".

See "runsource()" in Lib/sqlite3/__main__.py for real-world use.

```
sqlite3.enable_callback_tracebacks(flag, /)

   Enable or disable callback tracebacks. By default you will not get
   any tracebacks in user-defined functions, aggregates, converters,
   authorizer callbacks etc. If you want to debug them, you can call
```python
this function with *flag* set to "True". Afterwards, you will get
tracebacks from callbacks on "sys.stderr". Use "False" to disable
the feature again.

Note:

  Errors in user-defined function callbacks are logged as
  unraisable exceptions. Use an "unraisable hook handler" for
  introspection of the failed callback.

```
sqlite3.register_adapter(type, adapter, /)

   Register an *adapter* *callable* to adapt the Python type *type*
```python
into an SQLite type. The adapter is called with a Python object of
type *type* as its sole argument, and must return a value of a type
that SQLite natively understands.

```

<!-- page: 8 -->

sqlite3.register_converter(typename, converter, /)

   Register the *converter* *callable* to convert SQLite objects of
   type *typename* into a Python object of a specific type. The
```python
converter is invoked for all SQLite values of type *typename*; it
is passed a "bytes" object and should return an object of the
desired Python type. Consult the parameter *detect_types* of
"connect()" for information regarding how type detection works.

Note: *typename* and the name of the type in your query are matched
case-insensitively.


```
Module constants
----------------

sqlite3.LEGACY_TRANSACTION_CONTROL

   Set "autocommit" to this constant to select old style (pre-Python
   3.12) transaction control behaviour. See Transaction control via
```python
the isolation_level attribute for more information.

```
sqlite3.PARSE_COLNAMES

   Pass this flag value to the *detect_types* parameter of "connect()"
   to look up a converter function by using the type name, parsed from
   the query column name, as the converter dictionary key. The type
   name must be wrapped in square brackets ("[]").

      SELECT p as "p [point]" FROM test;  ! will look up converter "point"

```python
This flag may be combined with "PARSE_DECLTYPES" using the "|"
(bitwise or) operator.

```
sqlite3.PARSE_DECLTYPES

   Pass this flag value to the *detect_types* parameter of "connect()"
```python
to look up a converter function using the declared types for each
column. The types are declared when the database table is created.
"sqlite3" will look up a converter function using the first word of
the declared type as the converter dictionary key. For example:

   CREATE TABLE test(
      i integer primary key,  ! will look up a converter named "integer"
      p point,                ! will look up a converter named "point"
      n number(10)            ! will look up a converter named "number"
    )

This flag may be combined with "PARSE_COLNAMES" using the "|"
(bitwise or) operator.

```

<!-- page: 9 -->

sqlite3.SQLITE_OK
sqlite3.SQLITE_DENY
sqlite3.SQLITE_IGNORE

   Flags that should be returned by the *authorizer_callback*
   *callable* passed to "Connection.set_authorizer()", to indicate
   whether:

   * Access is allowed ("SQLITE_OK"),

```python
* The SQL statement should be aborted with an error ("SQLITE_DENY")

* The column should be treated as a "NULL" value ("SQLITE_IGNORE")

```
sqlite3.apilevel

   String constant stating the supported DB-API level. Required by the
   DB-API. Hard-coded to ""2.0"".

sqlite3.paramstyle

   String constant stating the type of parameter marker formatting
   expected by the "sqlite3" module. Required by the DB-API. Hard-
   coded to ""qmark"".

   Note:

     The "named" DB-API parameter style is also supported.

sqlite3.sqlite_version

   Version number of the runtime SQLite library as a "string".

sqlite3.sqlite_version_info

   Version number of the runtime SQLite library as a "tuple" of
   "integers".

sqlite3.threadsafety

   Integer constant required by the DB-API 2.0, stating the level of
   thread safety the "sqlite3" module supports. This attribute is set
   based on the default threading mode the underlying SQLite library

<!-- page: 10 -->

   is compiled with. The SQLite threading modes are:

   1. **Single-thread**: In this mode, all mutexes are disabled and
      SQLite is unsafe to use in more than a single thread at once.

   2. **Multi-thread**: In this mode, SQLite can be safely used by
      multiple threads provided that no single database connection is
      used simultaneously in two or more threads.

   3. **Serialized**: In serialized mode, SQLite can be safely used by
```python
   multiple threads with no restriction.

The mappings from SQLite threading modes to DB-API 2.0 threadsafety
levels are as follows:

+--------------------+------------------------+------------------------+---------------------------------+
| SQLite threading   | **threadsafety**       | SQLITE_THREADSAFE      | DB-API 2.0 meaning              |
| mode               |                        |                        |                                 |
|====================|========================|========================|=================================|
| single-thread      | 0                      | 0                      | Threads may not share the       |
|                    |                        |                        | module                          |
+--------------------+------------------------+------------------------+---------------------------------+
| multi-thread       | 1                      | 2                      | Threads may share the module,   |
|                    |                        |                        | but not connections             |
+--------------------+------------------------+------------------------+---------------------------------+
| serialized         | 3                      | 1                      | Threads may share the module,   |
|                    |                        |                        | connections and cursors         |
+--------------------+------------------------+------------------------+---------------------------------+

Changed in version 3.11: Set *threadsafety* dynamically instead of
hard-coding it to "1".

```
sqlite3.version

   Version number of this module as a "string". This is not the
   version of the SQLite library.

   Deprecated since version 3.12, will be removed in version 3.14:
   This constant used to reflect the version number of the "pysqlite"
   package, a third-party library which used to upstream changes to
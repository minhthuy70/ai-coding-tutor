# EN_PY_084: Logging HOWTO: Advanced Logging Flow, Custom Handlers, and Formatters

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Systems | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

By default, no destination is set for any logging messages. You can
specify a destination (such as console or file) by using
"basicConfig()" as in the tutorial examples. If you call the functions
"debug()", "info()", "warning()", "error()" and "critical()", they
will check to see if no destination is set; and if one is not set,
they will set a destination of the console ("sys.stderr") and a
default format for the displayed message before delegating to the root
logger to do the actual message output.

The default format set by "basicConfig()" for messages is:

   severity:logger name:message

You can change this by passing a format string to "basicConfig()" with
the *format* keyword argument. For all options regarding how a format
string is constructed, see Formatter Objects.

Logging Flow
------------

The flow of log event information in loggers and handlers is
illustrated in the following diagram.

[image]

Loggers
-------

"Logger" objects have a threefold job.  First, they expose several
methods to application code so that applications can log messages at
runtime. Second, logger objects determine which log messages to act

upon based upon severity (the default filtering facility) or filter
objects.  Third, logger objects pass along relevant log messages to
all interested log handlers.

The most widely used methods on logger objects fall into two
categories: configuration and message sending.

These are the most common configuration methods:

* "Logger.setLevel()" specifies the lowest-severity log message a
  logger will handle, where debug is the lowest built-in severity
  level and critical is the highest built-in severity.  For example,
  if the severity level is INFO, the logger will handle only INFO,
  WARNING, ERROR, and CRITICAL messages and will ignore DEBUG
  messages.

* "Logger.addHandler()" and "Logger.removeHandler()" add and remove
  handler objects from the logger object.  Handlers are covered in
  more detail in Handlers.

* "Logger.addFilter()" and "Logger.removeFilter()" add and remove
  filter objects from the logger object.  Filters are covered in more
  detail in Filter Objects.

You don’t need to always call these methods on every logger you
create. See the last two paragraphs in this section.

With the logger object configured, the following methods create log
messages:

* "Logger.debug()", "Logger.info()", "Logger.warning()",
  "Logger.error()", and "Logger.critical()" all create log records
  with a message and a level that corresponds to their respective
  method names. The message is actually a format string, which may
  contain the standard string substitution syntax of "%s", "%d", "%f",
  and so on.  The rest of their arguments is a list of objects that
  correspond with the substitution fields in the message.  With regard
  to "**kwargs", the logging methods care only about a keyword of
  "exc_info" and use it to determine whether to log exception
  information.

* "Logger.exception()" creates a log message similar to
  "Logger.error()".  The difference is that "Logger.exception()" dumps
  a stack trace along with it.  Call this method only from an
  exception handler.

* "Logger.log()" takes a log level as an explicit argument.  This is a
  little more verbose for logging messages than using the log level
  convenience methods listed above, but this is how to log at custom
  log levels.

"getLogger()" returns a reference to a logger instance with the
specified name if it is provided, or "root" if not.  The names are
period-separated hierarchical structures.  Multiple calls to
"getLogger()" with the same name will return a reference to the same
logger object.  Loggers that are further down in the hierarchical list
are children of loggers higher up in the list. For example, given a
logger with a name of "foo", loggers with names of "foo.bar",
"foo.bar.baz", and "foo.bam" are all descendants of "foo".

Loggers have a concept of *effective level*. If a level is not
explicitly set on a logger, the level of its parent is used instead as
its effective level. If the parent has no explicit level set, *its*
parent is examined, and so on - all ancestors are searched until an
explicitly set level is found. The root logger always has an explicit
level set ("WARNING" by default). When deciding whether to process an
event, the effective level of the logger is used to determine whether
the event is passed to the logger’s handlers.

Child loggers propagate messages up to the handlers associated with
their ancestor loggers. Because of this, it is unnecessary to define
and configure handlers for all the loggers an application uses. It is
sufficient to configure handlers for a top-level logger and create
child loggers as needed. (You can, however, turn off propagation by
setting the *propagate* attribute of a logger to "False".)

Handlers
--------

"Handler" objects are responsible for dispatching the appropriate log
messages (based on the log messages’ severity) to the handler’s
specified destination.  "Logger" objects can add zero or more handler
objects to themselves with an "addHandler()" method.  As an example
scenario, an application may want to send all log messages to a log
file, all log messages of error or higher to stdout, and all messages
of critical to an email address. This scenario requires three
individual handlers where each handler is responsible for sending
messages of a specific severity to a specific location.

The standard library includes quite a few handler types (see Useful
Handlers); the tutorials use mainly "StreamHandler" and "FileHandler"
in its examples.

There are very few methods in a handler for application developers to
concern themselves with.  The only handler methods that seem relevant
for application developers who are using the built-in handler objects
(that is, not creating custom handlers) are the following
configuration methods:

* The "setLevel()" method, just as in logger objects, specifies the
  lowest severity that will be dispatched to the appropriate
  destination.  Why are there two "setLevel()" methods?  The level set
  in the logger determines which severity of messages it will pass to
  its handlers.  The level set in each handler determines which
  messages that handler will send on.

* "setFormatter()" selects a Formatter object for this handler to use.

* "addFilter()" and "removeFilter()" respectively configure and
  deconfigure filter objects on handlers.

Application code should not directly instantiate and use instances of
"Handler".  Instead, the "Handler" class is a base class that defines
the interface that all handlers should have and establishes some
default behavior that child classes can use (or override).

Formatters
----------

Formatter objects configure the final order, structure, and contents
of the log message.  Unlike the base "logging.Handler" class,
application code may instantiate formatter classes, although you could
likely subclass the formatter if your application needs special
behavior.  The constructor takes three optional arguments – a message
format string, a date format string and a style indicator.

logging.Formatter.__init__(fmt=None, datefmt=None, style='%')

If there is no message format string, the default is to use the raw
message.  If there is no date format string, the default date format
is:

   %Y-%m-%d %H:%M:%S

with the milliseconds tacked on at the end. The "style" is one of
"'%'", "'{'", or "'$'". If one of these is not specified, then "'%'"
will be used.

If the "style" is "'%'", the message format string uses "%(<dictionary
key>)s" styled string substitution; the possible keys are documented
in LogRecord attributes. If the style is "'{'", the message format
string is assumed to be compatible with "str.format()" (using keyword
arguments), while if the style is "'$'" then the message format string
should conform to what is expected by "string.Template.substitute()".

Changed in version 3.2: Added the "style" parameter.

The following message format string will log the time in a human-
readable format, the severity of the message, and the contents of the
message, in that order:

   '%(asctime)s - %(levelname)s - %(message)s'

Formatters use a user-configurable function to convert the creation
time of a record to a tuple. By default, "time.localtime()" is used;
to change this for a particular formatter instance, set the
"converter" attribute of the instance to a function with the same
signature as "time.localtime()" or "time.gmtime()". To change it for
all formatters, for example if you want all logging times to be shown
in GMT, set the "converter" attribute in the Formatter class (to
"time.gmtime" for GMT display).

Configuring Logging
-------------------

Programmers can configure logging in three ways:

1. Creating loggers, handlers, and formatters explicitly using Python
   code that calls the configuration methods listed above.

2. Creating a logging config file and reading it using the
   "fileConfig()" function.

3. Creating a dictionary of configuration information and passing it
   to the "dictConfig()" function.

For the reference documentation on the last two options, see

Configuration functions.  The following example configures a very
simple logger, a console handler, and a simple formatter using Python
code:

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

```

Running this module from the command line produces the following
output:

   \$ python simple_logging_module.py
   2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
   2005-03-19 15:10:26,620 - simple_example - INFO - info message
   2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
   2005-03-19 15:10:26,697 - simple_example - ERROR - error message
   2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message

The following Python module creates a logger, handler, and formatter
nearly identical to those in the example listed above, with the only
difference being the names of the objects:

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

```

Here is the logging.conf file:

   [loggers]
   keys=root,simpleExample

   [handlers]
   keys=consoleHandler

   [formatters]
   keys=simpleFormatter

   [logger_root]
   level=DEBUG
   handlers=consoleHandler

   [logger_simpleExample]
   level=DEBUG
   handlers=consoleHandler
   qualname=simpleExample
   propagate=0

   [handler_consoleHandler]
   class=StreamHandler
   level=DEBUG
   formatter=simpleFormatter
   args=(sys.stdout,)

   [formatter_simpleFormatter]
   format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

The output is nearly identical to that of the non-config-file-based
example:

   \$ python simple_logging_config.py
   2005-03-19 15:38:55,977 - simpleExample - DEBUG - debug message
   2005-03-19 15:38:55,979 - simpleExample - INFO - info message
   2005-03-19 15:38:56,054 - simpleExample - WARNING - warn message
   2005-03-19 15:38:56,055 - simpleExample - ERROR - error message
   2005-03-19 15:38:56,130 - simpleExample - CRITICAL - critical message

You can see that the config file approach has a few advantages over
the Python code approach, mainly separation of configuration and code
and the ability of noncoders to easily modify the logging properties.

Warning:

  The "fileConfig()" function takes a default parameter,
  "disable_existing_loggers", which defaults to "True" for reasons of
  backward compatibility. This may or may not be what you want, since
  it will cause any non-root loggers existing before the
  "fileConfig()" call to be disabled unless they (or an ancestor) are
  explicitly named in the configuration. Please refer to the reference
  documentation for more information, and specify "False" for this
  parameter if you wish.The dictionary passed to "dictConfig()" can
  also specify a Boolean value with key "disable_existing_loggers",
  which if not specified explicitly in the dictionary also defaults to
  being interpreted as "True". This leads to the logger-disabling
  behaviour described above, which may not be what you want - in which
  case, provide the key explicitly with a value of "False".

Note that the class names referenced in config files need to be either
relative to the logging module, or absolute values which can be
resolved using normal import mechanisms. Thus, you could use either
"WatchedFileHandler" (relative to the logging module) or
"mypackage.mymodule.MyHandler" (for a class defined in package
"mypackage" and module "mymodule", where "mypackage" is available on
the Python import path).

In Python 3.2, a new means of configuring logging has been introduced,
using dictionaries to hold configuration information. This provides a
superset of the functionality of the config-file-based approach
outlined above, and is the recommended configuration method for new

applications and deployments. Because a Python dictionary is used to
hold configuration information, and since you can populate that
dictionary using different means, you have more options for
configuration. For example, you can use a configuration file in JSON
format, or, if you have access to YAML processing functionality, a
file in YAML format, to populate the configuration dictionary. Or, of
course, you can construct the dictionary in Python code, receive it in
pickled form over a socket, or use whatever approach makes sense for
your application.

Here’s an example of the same configuration as above, in YAML format
for the new dictionary-based approach:

   version: 1
   formatters:
     simple:
       format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   handlers:
     console:
       class: logging.StreamHandler
       level: DEBUG
       formatter: simple
       stream: ext://sys.stdout
   loggers:
     simpleExample:
       level: DEBUG
       handlers: [console]
       propagate: no
   root:
     level: DEBUG
     handlers: [console]

For more information about logging using a dictionary, see
Configuration functions.

What happens if no configuration is provided
--------------------------------------------

If no logging configuration is provided, it is possible to have a
situation where a logging event needs to be output, but no handlers
can be found to output the event.

The event is output using a ‘handler of last resort’, stored in
"lastResort". This internal handler is not associated with any logger,

and acts like a "StreamHandler" which writes the event description
message to the current value of "sys.stderr" (therefore respecting any
redirections which may be in effect). No formatting is done on the
message - just the bare event description message is printed. The
handler’s level is set to "WARNING", so all events at this and greater
severities will be output.

Changed in version 3.2: For versions of Python prior to 3.2, the
behaviour is as follows:
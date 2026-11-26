<!-- page: 1 -->
# EN_PY_056: Standard Library: Logging Architecture (Loggers, Handlers, Formatters)

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Standard Library | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

   img_1076.jpg --> Ashley_1.jpg
   img_1077.jpg --> Ashley_2.jpg

Another application for templating is separating program logic from
the details of multiple output formats.  This makes it possible to
substitute custom templates for XML files, plain text reports, and
HTML web reports.


11.3. Working with Binary Data Record Layouts
=============================================

The "struct" module provides "pack()" and "unpack()" functions for
working with variable length binary record formats.  The following
example shows how to loop through header information in a ZIP file
without using the "zipfile" module.  Pack codes ""H"" and ""I""
represent two and four byte unsigned numbers respectively.  The ""<""
indicates that they are standard size and in little-endian byte order:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header


```

<!-- page: 2 -->

11.4. Multi-threading
=====================

Threading is a technique for decoupling tasks which are not
sequentially dependent.  Threads can be used to improve the
responsiveness of applications that accept user input while other
tasks run in the background.  A related use case is running I/O in
parallel with computations in another thread.

The following code shows how the high level "threading" module can run
tasks in background while the main program continues to run:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

```
The principal challenge of multi-threaded applications is coordinating
threads that share data or other resources.  To that end, the
threading module provides a number of synchronization primitives
including locks, events, condition variables, and semaphores.

While those tools are powerful, minor design errors can result in
problems that are difficult to reproduce.  So, the preferred approach
to task coordination is to concentrate all access to a resource in a
single thread and then use the "queue" module to feed that thread with
requests from other threads. Applications using "Queue" objects for

<!-- page: 3 -->

inter-thread communication and coordination are easier to design, more
readable, and more reliable.


11.5. Logging
=============

The "logging" module offers a full featured and flexible logging
system. At its simplest, log messages are sent to a file or to
"sys.stderr":

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

```
This produces the following output:

   WARNING:root:Warning:config file server.conf not found
   ERROR:root:Error occurred
   CRITICAL:root:Critical error -- shutting down

By default, informational and debugging messages are suppressed and
the output is sent to standard error.  Other output options include
routing messages through email, datagrams, sockets, or to an HTTP
Server.  New filters can select different routing based on message
priority: "DEBUG", "INFO", "WARNING", "ERROR", and "CRITICAL".

The logging system can be configured directly from Python or can be
loaded from a user editable configuration file for customized logging
without altering the application.


11.6. Weak References
=====================
# EN_PY_068: Metaclasses: Type Construction, __init_subclass__, and Class Creation Hooks

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Advanced OOP | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

     typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds.
     If an object’s   "__hash__()" must interoperate on builds of
     different bit sizes, be sure to check the width on all supported

```python
  builds.  An easy way to do this is with "python -c "import sys;
  print(sys.hash_info.width)"".

If a class does not define an "__eq__()" method it should not
define a "__hash__()" operation either; if it defines "__eq__()"
but not "__hash__()", its instances will not be usable as items in
hashable collections.  If a class defines mutable objects and
implements an "__eq__()" method, it should not implement
"__hash__()", since the implementation of *hashable* collections
requires that a key’s hash value is immutable (if the object’s hash
value changes, it will be in the wrong hash bucket).

User-defined classes have "__eq__()" and "__hash__()" methods by
default (inherited from the "object" class); with them, all objects
compare unequal (except with themselves) and "x.__hash__()" returns
an appropriate value such that "x == y" implies both that "x is y"
and "hash(x) == hash(y)".

A class that overrides "__eq__()" and does not define "__hash__()"
will have its "__hash__()" implicitly set to "None".  When the
"__hash__()" method of a class is "None", instances of the class
will raise an appropriate "TypeError" when a program attempts to
retrieve their hash value, and will also be correctly identified as
unhashable when checking "isinstance(obj,
collections.abc.Hashable)".

If a class that overrides "__eq__()" needs to retain the
implementation of "__hash__()" from a parent class, the interpreter
must be told this explicitly by setting "__hash__ =
<ParentClass>.__hash__".

If a class that does not override "__eq__()" wishes to suppress
hash support, it should include "__hash__ = None" in the class
definition. A class which defines its own "__hash__()" that
explicitly raises a "TypeError" would be incorrectly identified as
hashable by an "isinstance(obj, collections.abc.Hashable)" call.

Note:

  By default, the "__hash__()" values of str and bytes objects are
  “salted” with an unpredictable random value.  Although they
  remain constant within an individual Python process, they are not
  predictable between repeated invocations of Python.This is
  intended to provide protection against a denial-of-service caused
  by carefully chosen inputs that exploit the worst case
  performance of a dict insertion, *O*(*n*^2) complexity.  See
  http://ocert.org/advisories/ocert-2011-003.html for
  details.Changing hash values affects the iteration order of sets.
  Python has never made guarantees about this ordering (and it
  typically varies between 32-bit and 64-bit builds).See also
  "PYTHONHASHSEED".

Changed in version 3.3: Hash randomization is enabled by default.

```

object.__bool__(self)

   Called to implement truth value testing and the built-in operation

```python
"bool()"; should return "False" or "True".  When this method is not
defined, "__len__()" is called, if it is defined, and the object is
considered true if its result is nonzero.  If a class defines
neither "__len__()" nor "__bool__()" (which is true of the "object"
class itself), all its instances are considered true.

```

3.3.2. Customizing attribute access
-----------------------------------

The following methods can be defined to customize the meaning of
attribute access (use of, assignment to, or deletion of "x.name") for
class instances.

object.__getattr__(self, name)

```python
Called when the default attribute access fails with an
"AttributeError" (either "__getattribute__()" raises an
"AttributeError" because *name* is not an instance attribute or an
attribute in the class tree for "self"; or "__get__()" of a *name*
property raises "AttributeError").  This method should either
return the (computed) attribute value or raise an "AttributeError"
exception. The "object" class itself does not provide this method.

Note that if the attribute is found through the normal mechanism,
"__getattr__()" is not called.  (This is an intentional asymmetry
between "__getattr__()" and "__setattr__()".) This is done both for
efficiency reasons and because otherwise "__getattr__()" would have
no way to access other attributes of the instance.  Note that at
least for instance variables, you can fake total control by not
inserting any values in the instance attribute dictionary (but
instead inserting them in another object).  See the
"__getattribute__()" method below for a way to actually get total
control over attribute access.

```

object.__getattribute__(self, name)

   Called unconditionally to implement attribute accesses for

```python
instances of the class. If the class also defines "__getattr__()",
the latter will not be called unless "__getattribute__()" either
calls it explicitly or raises an "AttributeError". This method
should return the (computed) attribute value or raise an
"AttributeError" exception. In order to avoid infinite recursion in
this method, its implementation should always call the base class
method with the same name to access any attributes it needs, for
example, "object.__getattribute__(self, name)".

Note:

  This method may still be bypassed when looking up special methods
  as the result of implicit invocation via language syntax or
  built-in functions. See Special method lookup.

For certain sensitive attribute accesses, raises an auditing event
"object.__getattr__" with arguments "obj" and "name".

```

object.__setattr__(self, name, value)

   Called when an attribute assignment is attempted.  This is called
   instead of the normal mechanism (i.e. store the value in the
   instance dictionary). *name* is the attribute name, *value* is the
   value to be assigned to it.

   If "__setattr__()" wants to assign to an instance attribute, it

```python
should call the base class method with the same name, for example,
"object.__setattr__(self, name, value)".

For certain sensitive attribute assignments, raises an auditing
event "object.__setattr__" with arguments "obj", "name", "value".

```

object.__delattr__(self, name)

```python
Like "__setattr__()" but for attribute deletion instead of
assignment.  This should only be implemented if "del obj.name" is
meaningful for the object.

For certain sensitive attribute deletions, raises an auditing event
"object.__delattr__" with arguments "obj" and "name".

```

object.__dir__(self)

   Called when "dir()" is called on the object. An iterable must be
   returned. "dir()" converts the returned iterable to a list and
   sorts it.

3.3.2.1. Customizing module attribute access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Special names "__getattr__" and "__dir__" can be also used to
customize access to module attributes. The "__getattr__" function at
the module level should accept one argument which is the name of an
attribute and return the computed value or raise an "AttributeError".
If an attribute is not found on a module object through the normal
lookup, i.e. "object.__getattribute__()", then "__getattr__" is
searched in the module "__dict__" before raising an "AttributeError".
If found, it is called with the attribute name and the result is
returned.

The "__dir__" function should accept no arguments, and return an
iterable of strings that represents the names accessible on module. If
present, this function overrides the standard "dir()" search on a
module.

For a more fine grained customization of the module behavior (setting
attributes, properties, etc.), one can set the "__class__" attribute
of a module object to a subclass of "types.ModuleType". For example:

```python
import sys
from types import ModuleType

class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)

sys.modules[__name__].__class__ = VerboseModule

```

Note:

  Defining module "__getattr__" and setting module "__class__" only
  affect lookups made using the attribute access syntax – directly
  accessing the module globals (whether by code within the module, or
  via a reference to the module’s globals dictionary) is unaffected.

Changed in version 3.5: "__class__" module attribute is now writable.

Added in version 3.7: "__getattr__" and "__dir__" module attributes.

See also:

  **PEP 562** - Module __getattr__ and __dir__
     Describes the "__getattr__" and "__dir__" functions on modules.

3.3.2.2. Implementing Descriptors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following methods only apply when an instance of the class
containing the method (a so-called *descriptor* class) appears in an
*owner* class (the descriptor must be in either the owner’s class
dictionary or in the class dictionary for one of its parents).  In the
examples below, “the attribute” refers to the attribute whose name is
the key of the property in the owner class’ "__dict__".  The "object"
class itself does not implement any of these protocols.

object.__get__(self, instance, owner=None)

```python
Called to get the attribute of the owner class (class attribute
access) or of an instance of that class (instance attribute
access). The optional *owner* argument is the owner class, while
*instance* is the instance that the attribute was accessed through,
or "None" when the attribute is accessed through the *owner*.

This method should return the computed attribute value or raise an
"AttributeError" exception.

**PEP 252** specifies that "__get__()" is callable with one or two
arguments.  Python’s own built-in descriptors support this
specification; however, it is likely that some third-party tools
have descriptors that require both arguments.  Python’s own
"__getattribute__()" implementation always passes in both arguments
whether they are required or not.

```

object.__set__(self, instance, value)

   Called to set the attribute on an instance *instance* of the owner

```python
class to a new value, *value*.

Note, adding "__set__()" or "__delete__()" changes the kind of
descriptor to a “data descriptor”.  See Invoking Descriptors for
more details.

```

object.__delete__(self, instance)

   Called to delete the attribute on an instance *instance* of the
   owner class.

Instances of descriptors may also have the "__objclass__" attribute
present:

object.__objclass__

   The attribute "__objclass__" is interpreted by the "inspect" module

```python
as specifying the class where this object was defined (setting this
appropriately can assist in runtime introspection of dynamic class
attributes). For callables, it may indicate that an instance of the
given type (or a subclass) is expected or required as the first
positional argument (for example, CPython sets this attribute for
unbound methods that are implemented in C).

```

3.3.2.3. Invoking Descriptors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, a descriptor is an object attribute with “binding
behavior”, one whose attribute access has been overridden by methods
in the descriptor protocol:  "__get__()", "__set__()", and
"__delete__()". If any of those methods are defined for an object, it
is said to be a descriptor.

The default behavior for attribute access is to get, set, or delete
the attribute from an object’s dictionary. For instance, "a.x" has a
lookup chain starting with "a.__dict__['x']", then
"type(a).__dict__['x']", and continuing through the base classes of

"type(a)" excluding metaclasses.

However, if the looked-up value is an object defining one of the
descriptor methods, then Python may override the default behavior and
invoke the descriptor method instead.  Where this occurs in the
precedence chain depends on which descriptor methods were defined and
how they were called.

The starting point for descriptor invocation is a binding, "a.x". How
the arguments are assembled depends on "a":

Direct Call
   The simplest and least common call is when user code directly
   invokes a descriptor method:    "x.__get__(a)".

Instance Binding
   If binding to an object instance, "a.x" is transformed into the
   call: "type(a).__dict__['x'].__get__(a, type(a))".

Class Binding
   If binding to a class, "A.x" is transformed into the call:
   "A.__dict__['x'].__get__(None, A)".

Super Binding
   A dotted lookup such as "super(A, a).x" searches

```python
"a.__class__.__mro__" for a base class "B" following "A" and then
returns "B.__dict__['x'].__get__(a, A)".  If not a descriptor, "x"
is returned unchanged.

```

For instance bindings, the precedence of descriptor invocation depends
on which descriptor methods are defined.  A descriptor can define any
combination of "__get__()", "__set__()" and "__delete__()".  If it
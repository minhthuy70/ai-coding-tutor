<!-- page: 1 -->
# EN_PY_069: Emulating Container Types: __len__, __getitem__, __setitem__, __contains__

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)  
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers  
**Domain**: Magic Methods | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

does not define "__get__()", then accessing the attribute will return
the descriptor object itself unless there is a value in the object’s
instance dictionary.  If the descriptor defines "__set__()" and/or
"__delete__()", it is a data descriptor; if it defines neither, it is
a non-data descriptor.  Normally, data descriptors define both
"__get__()" and "__set__()", while non-data descriptors have just the
"__get__()" method.  Data descriptors with "__get__()" and "__set__()"
(and/or "__delete__()") defined always override a redefinition in an
instance dictionary.  In contrast, non-data descriptors can be
overridden by instances.

Python methods (including those decorated with "@staticmethod" and
"@classmethod") are implemented as non-data descriptors.  Accordingly,
instances can redefine and override methods.  This allows individual
instances to acquire behaviors that differ from other instances of the
same class.

The "property()" function is implemented as a data descriptor.
Accordingly, instances cannot override the behavior of a property.


3.3.2.4. __slots__
~~~~~~~~~~~~~~~~~~

*__slots__* allow us to explicitly declare data members (like
properties) and deny the creation of "__dict__" and *__weakref__*
(unless explicitly declared in *__slots__* or available in a parent.)

The space saved over using "__dict__" can be significant. Attribute
lookup speed can be significantly improved as well.

object.__slots__

```python
This class variable can be assigned a string, iterable, or sequence
of strings with variable names used by instances.  *__slots__*
reserves space for the declared variables and prevents the
automatic creation of "__dict__" and *__weakref__* for each
instance.

```

<!-- page: 2 -->

Notes on using *__slots__*:

* When inheriting from a class without *__slots__*, the "__dict__" and
  *__weakref__* attribute of the instances will always be accessible.

* Without a "__dict__" variable, instances cannot be assigned new
  variables not listed in the *__slots__* definition.  Attempts to
  assign to an unlisted variable name raises "AttributeError". If
  dynamic assignment of new variables is desired, then add
  "'__dict__'" to the sequence of strings in the *__slots__*
  declaration.

* Without a *__weakref__* variable for each instance, classes defining
  *__slots__* do not support "weak references" to its instances. If
  weak reference support is needed, then add "'__weakref__'" to the
  sequence of strings in the *__slots__* declaration.

* *__slots__* are implemented at the class level by creating
  descriptors for each variable name.  As a result, class attributes
  cannot be used to set default values for instance variables defined
  by *__slots__*; otherwise, the class attribute would overwrite the
  descriptor assignment.

* The action of a *__slots__* declaration is not limited to the class
  where it is defined.  *__slots__* declared in parents are available
  in child classes. However, instances of a child subclass will get a
  "__dict__" and *__weakref__* unless the subclass also defines
  *__slots__* (which should only contain names of any *additional*
  slots).

* If a class defines a slot also defined in a base class, the instance
  variable defined by the base class slot is inaccessible (except by
  retrieving its descriptor directly from the base class). This
  renders the meaning of the program undefined.  In the future, a
  check may be added to prevent this.

* "TypeError" will be raised if nonempty *__slots__* are defined for a
  class derived from a ""variable-length" built-in type" such as
  "int", "bytes", and "tuple".

* Any non-string *iterable* may be assigned to *__slots__*.

* If a "dictionary" is used to assign *__slots__*, the dictionary keys
  will be used as the slot names. The values of the dictionary can be
  used to provide per-attribute docstrings that will be recognised by

<!-- page: 3 -->

  "inspect.getdoc()" and displayed in the output of "help()".

* "__class__" assignment works only if both classes have the same
  *__slots__*.

* Multiple inheritance with multiple slotted parent classes can be
  used, but only one parent is allowed to have attributes created by
  slots (the other bases must have empty slot layouts) - violations
  raise "TypeError".

* If an *iterator* is used for *__slots__* then a *descriptor* is
  created for each of the iterator’s values. However, the *__slots__*
  attribute will be an empty iterator.


3.3.3. Customizing class creation
---------------------------------

Whenever a class inherits from another class, "__init_subclass__()" is
called on the parent class. This way, it is possible to write classes
which change the behavior of subclasses. This is closely related to
class decorators, but where class decorators only affect the specific
class they’re applied to, "__init_subclass__" solely applies to future
subclasses of the class defining the method.

classmethod object.__init_subclass__(cls)

```python
This method is called whenever the containing class is subclassed.
*cls* is then the new subclass. If defined as a normal instance
method, this method is implicitly converted to a class method.

Keyword arguments which are given to a new class are passed to the
parent class’s "__init_subclass__". For compatibility with other
classes using "__init_subclass__", one should take out the needed
keyword arguments and pass the others over to the base class, as
in:

   class Philosopher:
       def __init_subclass__(cls, /, default_name, **kwargs):
           super().__init_subclass__(**kwargs)
           cls.default_name = default_name

   class AustralianPhilosopher(Philosopher, default_name="Bruce"):
       pass

The default implementation "object.__init_subclass__" does nothing,
but raises an error if it is called with any arguments.

Note:

  The metaclass hint "metaclass" is consumed by the rest of the
  type machinery, and is never passed to "__init_subclass__"
  implementations. The actual metaclass (rather than the explicit
  hint) can be accessed as "type(cls)".

Added in version 3.6.

```

<!-- page: 4 -->

When a class is created, "type.__new__()" scans the class variables
and makes callbacks to those with a "__set_name__()" hook.

object.__set_name__(self, owner, name)

```python
Automatically called at the time the owning class *owner* is
created. The object has been assigned to *name* in that class:

   class A:
       x = C()  # Automatically calls: x.__set_name__(A, 'x')

If the class variable is assigned after the class is created,
"__set_name__()" will not be called automatically. If needed,
"__set_name__()" can be called directly:

   class A:
      pass

   c = C()
   A.x = c                  # The hook is not called
   c.__set_name__(A, 'x')   # Manually invoke the hook

See Creating the class object for more details.

Added in version 3.6.


```
3.3.3.1. Metaclasses
~~~~~~~~~~~~~~~~~~~~

By default, classes are constructed using "type()". The class body is
executed in a new namespace and the class name is bound locally to the
result of "type(name, bases, namespace)".

The class creation process can be customized by passing the
"metaclass" keyword argument in the class definition line, or by
inheriting from an existing class that included such an argument. In
the following example, both "MyClass" and "MySubclass" are instances
of "Meta":

```python
class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass

class MySubclass(MyClass):
    pass

```

<!-- page: 5 -->

Any other keyword arguments that are specified in the class definition
are passed through to all metaclass operations described below.

When a class definition is executed, the following steps occur:

* MRO entries are resolved;

* the appropriate metaclass is determined;

* the class namespace is prepared;

* the class body is executed;

* the class object is created.


3.3.3.2. Resolving MRO entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

object.__mro_entries__(self, bases)

```python
If a base that appears in a class definition is not an instance of
"type", then an "__mro_entries__()" method is searched on the base.
If an "__mro_entries__()" method is found, the base is substituted
with the result of a call to "__mro_entries__()" when creating the
class. The method is called with the original bases tuple passed to
the *bases* parameter, and must return a tuple of classes that will
be used instead of the base. The returned tuple may be empty: in
these cases, the original base is ignored.

```
See also:

  "types.resolve_bases()"
     Dynamically resolve bases that are not instances of "type".

  "types.get_original_bases()"
     Retrieve a class’s “original bases” prior to modifications by
     "__mro_entries__()".

  **PEP 560**
```python
Core support for typing module and generic types.


```

<!-- page: 6 -->

3.3.3.3. Determining the appropriate metaclass
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The appropriate metaclass for a class definition is determined as
follows:

* if no bases and no explicit metaclass are given, then "type()" is
  used;

* if an explicit metaclass is given and it is *not* an instance of
  "type()", then it is used directly as the metaclass;

* if an instance of "type()" is given as the explicit metaclass, or
  bases are defined, then the most derived metaclass is used.

The most derived metaclass is selected from the explicitly specified
metaclass (if any) and the metaclasses (i.e. "type(cls)") of all
specified base classes. The most derived metaclass is one which is a
subtype of *all* of these candidate metaclasses. If none of the
candidate metaclasses meets that criterion, then the class definition
will fail with "TypeError".


3.3.3.4. Preparing the class namespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the appropriate metaclass has been identified, then the class
namespace is prepared. If the metaclass has a "__prepare__" attribute,
it is called as "namespace = metaclass.__prepare__(name, bases,
**kwds)" (where the additional keyword arguments, if any, come from
the class definition). The "__prepare__" method should be implemented
as a "classmethod". The namespace returned by "__prepare__" is passed
in to "__new__", but when the final class object is created the
namespace is copied into a new "dict".

If the metaclass has no "__prepare__" attribute, then the class
namespace is initialised as an empty ordered mapping.

See also:

  **PEP 3115** - Metaclasses in Python 3000
     Introduced the "__prepare__" namespace hook


3.3.3.5. Executing the class body

<!-- page: 7 -->

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The class body is executed (approximately) as "exec(body, globals(),
namespace)". The key difference from a normal call to "exec()" is that
lexical scoping allows the class body (including any methods) to
reference names from the current and outer scopes when the class
definition occurs inside a function.

However, even when the class definition occurs inside the function,
methods defined inside the class still cannot see names defined at the
class scope. Class variables must be accessed through the first
parameter of instance or class methods, or through the implicit
lexically scoped "__class__" reference described in the next section.


3.3.3.6. Creating the class object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the class namespace has been populated by executing the class
body, the class object is created by calling "metaclass(name, bases,
namespace, **kwds)" (the additional keywords passed here are the same
as those passed to "__prepare__").
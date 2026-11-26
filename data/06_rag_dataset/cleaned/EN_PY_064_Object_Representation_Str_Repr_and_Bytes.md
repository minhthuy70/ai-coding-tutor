# EN_PY_064: Customizing Object Representation: __repr__, __str__, __bytes__, __format__

**Authoritative Source**: Python Software Foundation (CPython 3.12 Official Documentation & Language Reference)
**Authors**: Guido van Rossum, Raymond Hettinger, Vinay Sajip, A.M. Kuchling, and CPython Core Developers
**Domain**: Magic Methods | **Target Audience**: Computer Science Undergraduate & Advanced Developers
**Language Specification**: Python 3.12 (CPython Standard Implementation)

---

## Technical Overview & Formal Specification

```python
>>> typing.__spec__.name = 'spelling'
>>> typing.__name__, typing.__spec__.name
('typing', 'spelling')
>>> typing.__name__ = 'keyboard_smashing'
>>> typing.__name__, typing.__spec__.name
('keyboard_smashing', 'spelling')

```

module.__name__

```python
The name used to uniquely identify the module in the import system.
For a directly executed module, this will be set to ""__main__"".

This attribute must be set to the fully qualified name of the
module. It is expected to match the value of
"module.__spec__.name".

```

module.__spec__

   A record of the module’s import-system-related state.

   Set to the "module spec" that was used when importing the module.

```python
See Module specs for more details.

Added in version 3.4.

```

module.__package__

   The *package* a module belongs to.

   If the module is top-level (that is, not a part of any specific
   package) then the attribute should be set to "''" (the empty
   string). Otherwise, it should be set to the name of the module’s

```python
package (which can be equal to "module.__name__" if the module
itself is a package). See **PEP 366** for further details.

This attribute is used instead of "__name__" to calculate explicit
relative imports for main modules. It defaults to "None" for
modules created dynamically using the "types.ModuleType"
constructor; use "importlib.util.module_from_spec()" instead to
ensure the attribute is set to a "str".

It is **strongly** recommended that you use
"module.__spec__.parent" instead of "module.__package__".
"__package__" is now only used as a fallback if "__spec__.parent"
is not set, and this fallback path is deprecated.

Changed in version 3.4: This attribute now defaults to "None" for
modules created dynamically using the "types.ModuleType"
constructor. Previously the attribute was optional.

Changed in version 3.6: The value of "__package__" is expected to
be the same as "__spec__.parent". "__package__" is now only used as
a fallback during import resolution if "__spec__.parent" is not
defined.

Changed in version 3.10: "ImportWarning" is raised if an import
resolution falls back to "__package__" instead of
"__spec__.parent".

Changed in version 3.12: Raise "DeprecationWarning" instead of
"ImportWarning" when falling back to "__package__" during import
resolution.

```

module.__loader__

```python
The *loader* object that the import machinery used to load the
module.

This attribute is mostly useful for introspection, but can be used
for additional loader-specific functionality, for example getting
data associated with a loader.

"__loader__" defaults to "None" for modules created dynamically
using the "types.ModuleType" constructor; use
"importlib.util.module_from_spec()" instead to ensure the attribute
is set to a *loader* object.

It is **strongly** recommended that you use
"module.__spec__.loader" instead of "module.__loader__".

Changed in version 3.4: This attribute now defaults to "None" for
modules created dynamically using the "types.ModuleType"
constructor. Previously the attribute was optional.

Deprecated since version 3.12, will be removed in version 3.16:
Setting "__loader__" on a module while failing to set
"__spec__.loader" is deprecated. In Python 3.16, "__loader__" will
cease to be set or taken into consideration by the import system or
the standard library.

```

module.__path__

   A (possibly empty) *sequence* of strings enumerating the locations
   where the package’s submodules will be found. Non-package modules
   should not have a "__path__" attribute. See __path__ attributes on

```python
modules for more details.

It is **strongly** recommended that you use
"module.__spec__.submodule_search_locations" instead of
"module.__path__".

```

module.__file__

module.__cached__

   "__file__" and "__cached__" are both optional attributes that may
   or may not be set. Both attributes should be a "str" when they are
   available.

```python
"__file__" indicates the pathname of the file from which the module
was loaded (if loaded from a file), or the pathname of the shared
library file for extension modules loaded dynamically from a shared
library. It might be missing for certain types of modules, such as
C modules that are statically linked into the interpreter, and the
import system may opt to leave it unset if it has no semantic
meaning (for example, a module loaded from a database).

If "__file__" is set then the "__cached__" attribute might also be
set,  which is the path to any compiled version of the code (for
example, a byte-compiled file). The file does not need to exist to
set this attribute; the path can simply point to where the compiled
file *would* exist (see **PEP 3147**).

Note that "__cached__" may be set even if "__file__" is not set.
However, that scenario is quite atypical.  Ultimately, the *loader*
is what makes use of the module spec provided by the *finder* (from
which "__file__" and "__cached__" are derived).  So if a loader can
load from a cached module but otherwise does not load from a file,
that atypical scenario may be appropriate.

It is **strongly** recommended that you use
"module.__spec__.cached" instead of "module.__cached__".

```

3.2.9.2. Other writable attributes on module objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As well as the import-related attributes listed above, module objects
also have the following writable attributes:

module.__doc__

```python
The module’s documentation string, or "None" if unavailable. See
also: "__doc__ attributes".

```

module.__annotations__

   A dictionary containing *variable annotations* collected during
   module body execution.  For best practices on working with
   "__annotations__", please see Annotations Best Practices.

3.2.9.3. Module dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module objects also have the following special read-only attribute:

module.__dict__

   The module’s namespace as a dictionary object. Uniquely among the
   attributes listed here, "__dict__" cannot be accessed as a global

```python
variable from within a module; it can only be accessed as an
attribute on module objects.

**CPython implementation detail:** Because of the way CPython
clears module dictionaries, the module dictionary will be cleared
when the module falls out of scope even if the dictionary still has
live references.  To avoid this, copy the dictionary or keep the
module around while using its dictionary directly.

```

3.2.10. Custom classes
----------------------

Custom class types are typically created by class definitions (see

section Class definitions).  A class has a namespace implemented by a
dictionary object. Class attribute references are translated to
lookups in this dictionary, e.g., "C.x" is translated to
"C.__dict__["x"]" (although there are a number of hooks which allow
for other means of locating attributes). When the attribute name is
not found there, the attribute search continues in the base classes.
This search of the base classes uses the C3 method resolution order
which behaves correctly even in the presence of ‘diamond’ inheritance
structures where there are multiple inheritance paths leading back to
a common ancestor. Additional details on the C3 MRO used by Python can
be found at The Python 2.3 Method Resolution Order.

When a class attribute reference (for class "C", say) would yield a
class method object, it is transformed into an instance method object
whose "__self__" attribute is "C". When it would yield a
"staticmethod" object, it is transformed into the object wrapped by
the static method object. See section Implementing Descriptors for
another way in which attributes retrieved from a class may differ from
those actually contained in its "__dict__".

Class attribute assignments update the class’s dictionary, never the
dictionary of a base class.

A class object can be called (see above) to yield a class instance
(see below).

3.2.10.1. Special attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+----------------------------------------------------+
| Attribute                                          | Meaning                                            |
|====================================================|====================================================|
| type.__name__                                      | The class’s name. See also: "__name__ attributes". |
+----------------------------------------------------+----------------------------------------------------+
| type.__qualname__                                  | The class’s *qualified name*. See also:            |
|                                                    | "__qualname__ attributes".                         |
+----------------------------------------------------+----------------------------------------------------+
| type.__module__                                    | The name of the module in which the class was      |
|                                                    | defined.                                           |
+----------------------------------------------------+----------------------------------------------------+
| type.__dict__                                      | A "mapping proxy" providing a read-only view of    |
|                                                    | the class’s namespace. See also: "__dict__         |
|                                                    | attributes".                                       |
+----------------------------------------------------+----------------------------------------------------+
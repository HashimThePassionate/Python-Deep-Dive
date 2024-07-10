# The Meaning of Variable Annotations

## Introduction
In the "No Runtime Effect" section, we saw that type hints have no effect at runtime. However, at import time—when a module is loaded—Python reads them to build the `__annotations__` dictionary, which `typing.NamedTuple` and `@dataclass` use to enhance the class.

This guide explores the differences in behavior between a plain class with type hints, a class built with `typing.NamedTuple`, and a class decorated with `@dataclass`.

## Example: Plain Class with Type Hints
Let's start with a simple class to see what extra features are added by `typing.NamedTuple` and `@dataclass`.

### Example Code:
```python
# 03_meaning_of_variable_annotations/demo_plain.py: a plain class with type hints
class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'
```

### Explanation:
- `a` becomes an entry in `__annotations__` but is otherwise discarded; no attribute named `a` is created in the class.
- `b` is saved as an annotation and also becomes a class attribute with value `1.1`.
- `c` is just a plain old class attribute, not an annotation.

### Verification:
```python
from demo_plain import DemoPlainClass

print(DemoPlainClass.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'float'>}

print(DemoPlainClass.b)
# Output: 1.1

print(DemoPlainClass.c)
# Output: 'spam'

try:
    print(DemoPlainClass.a)
except AttributeError as e:
    print(e)
# Output: AttributeError: type object 'DemoPlainClass' has no attribute 'a'
```

**Explanation**:
- The `__annotations__` dictionary records the type hints of `a` and `b`.
- Accessing `DemoPlainClass.b` returns `1.1` because it is both an annotation and a class attribute with a default value.
- Accessing `DemoPlainClass.c` returns `'spam'` because it is a plain class attribute.
- Accessing `DemoPlainClass.a` raises an `AttributeError` because `a` is only recorded in `__annotations__` and not as a class attribute.

## Example: Class Built with `typing.NamedTuple`
Now let's examine a class built with `typing.NamedTuple` using the same attributes and annotations.

### Example Code:
```python
# 03_meaning_of_variable_annotations/demo_plain.py: a class built with typing.NamedTuple
import typing

class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'
```

### Explanation:
- `a` becomes an annotation and also an instance attribute.
- `b` is another annotation and also becomes an instance attribute with default value `1.1`.
- `c` is just a plain old class attribute; no annotation will refer to it.

### Verification:
```python
from demo_plain import DemoNTClass

print(DemoNTClass.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'float'>}

print(DemoNTClass.b)
# Output: _tuplegetter(1, 'Alias for field number 1')

print(DemoNTClass.c)
# Output: 'spam'

print(DemoNTClass.a)
# Output: _tuplegetter(0, 'Alias for field number 0')

nt = DemoNTClass(8)
print(nt.a)
# Output: 8

print(nt.b)
# Output: 1.1

print(nt.c)
# Output: 'spam'
```

**Explanation**:
- The `__annotations__` dictionary records the type hints of `a` and `b`.
- `DemoNTClass.b` and `DemoNTClass.a` return `_tuplegetter` objects, which are descriptors that act like read-only instance attributes.
- `DemoNTClass.c` returns `'spam'` because it is a plain class attribute.
- Creating an instance `nt = DemoNTClass(8)` sets `nt.a` to `8`, `nt.b` to the default value `1.1`, and `nt.c` is inherited from the class attribute.

## Example: Class Decorated with `@dataclass`
Now let's examine a class decorated with `@dataclass`.

### Example Code:
```python
# 03_meaning_of_variable_annotations/demo_dc.py: a class decorated with @dataclass
from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'
```

### Explanation:
- `a` becomes an annotation and also an instance attribute controlled by a descriptor.
- `b` is another annotation and also becomes an instance attribute with a descriptor and a default value `1.1`.
- `c` is just a plain old class attribute; no annotation will refer to it.

### Verification:
```python
from demo_plain import DemoDataClass

print(DemoDataClass.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'float'>}

print(DemoDataClass.__doc__)
# Output: 'DemoDataClass(a: int, b: float = 1.1)'

print(DemoDataClass.b)
# Output: 1.1

print(DemoDataClass.c)
# Output: 'spam'

try:
    print(DemoDataClass.a)
except AttributeError as e:
    print(e)
# Output: AttributeError: type object 'DemoDataClass' has no attribute 'a'

dc = DemoDataClass(9)
print(dc.a)
# Output: 9

print(dc.b)
# Output: 1.1

print(dc.c)
# Output: 'spam'

# Mutability demonstration
dc.a = 10
print(dc.a)
# Output: 10

dc.b = 'oops'
print(dc.b)
# Output: 'oops'

dc.c = 'whatever'
print(dc.c)
# Output: 'whatever'

dc.z = 'secret stash'
print(dc.z)
# Output: 'secret stash'
```

**Explanation**:
- The `__annotations__` dictionary records the type hints of `a` and `b`.
- `DemoDataClass.__doc__` provides a description of the class.
- `DemoDataClass.b` returns `1.1` because it is an instance attribute with a default value.
- `DemoDataClass.c` returns `'spam'` because it is a plain class attribute.
- `DemoDataClass.a` does not exist as a class attribute; it only exists in instances.
- Creating an instance `dc = DemoDataClass(9)` sets `dc.a` to `9`, `dc.b` to the default value `1.1`, and `dc.c` is inherited from the class attribute.
- The instance `dc` is mutable, allowing changes to its attributes and addition of new attributes.

## Conclusion
- Type hints recorded in `__annotations__` provide metadata but do not enforce type constraints at runtime.
- `typing.NamedTuple` and `@dataclass` enhance classes by making use of these annotations to create instance attributes and provide additional features like default values and immutability (in the case of NamedTuple).
- The examples demonstrate how these enhancements work in practice, showing the differences in behavior between plain classes, NamedTuple classes, and dataclass-decorated classes.

# Generic Collections

## Introduction
Most Python collections are heterogeneous, meaning they can hold a mix of different types. However, in practice, it's often more useful to have collections with items that share a common type or method. Generic types allow you to specify the type of items a collection can hold, making it easier to work with them later.

## Declaring Generic Types
You can declare generic types with type parameters to specify the type of the items they can handle. For example, you can parameterize a list to constrain the type of its elements.

### Example: Tokenize Function with Type Hints
```python
def tokenize(text: str) -> list[str]:
    return text.upper().split()
```
In Python 3.9 and later, this function returns a list where every item is of type `str`.

## Type Annotations for Lists
The annotation `list[str]` means that the list contains items of type `str`. Similarly, `list[Any]` means the list can contain items of any type.

### Example: Python 3.10 or Later
In Python 3.10 and later, you can use the new syntax for type hints, which is simpler and more concise.

```python
def tokenize(text: str) -> list[str]:
    return text.upper().split()

print(tokenize("hello world"))  # Output: ['HELLO', 'WORLD']
```

### Legacy Support for Older Python Versions
For Python 3.7 and 3.8, you need to use a `__future__` import to make the `[]` notation work with built-in collections.

### Example: Tokenize Function for Python ≥ 3.7
```python
from __future__ import annotations

def tokenize(text: str) -> list[str]:
    return text.upper().split()

print(tokenize("hello world"))  # Output: ['HELLO', 'WORLD']
```
For Python 3.6 and earlier, you need to use the `typing` module.

### Example: Tokenize Function for Python ≥ 3.5
```python
from typing import List

def tokenize(text: str) -> List[str]:
    return text.upper().split()

print(tokenize("hello world"))  # Output: ['HELLO', 'WORLD']
```

## Collections Supporting Generic Type Hints
PEP 585—Type Hinting Generics In Standard Collections lists the collections from the standard library that accept generic type hints. Here are some of the collections that use the simplest form of generic type hint, `container[item]`:

- `list`
- `collections.deque`
- `abc.Sequence`
- `abc.MutableSequence`
- `set`
- `abc.Container`
- `abc.Set`
- `abc.MutableSet`
- `frozenset`
- `abc.Collection`

The tuple and mapping types support more complex type hints, which we will discuss in their respective sections.

## Limitations with Some Collections
As of Python 3.10, there is no good way to annotate `array.array`, taking into account the `typecode` constructor argument, which determines whether integers or floats are stored in the array. Handling integer ranges to prevent `OverflowError` at runtime when adding elements to arrays is also a challenge. For example, an array with `typecode='B'` can only hold `int` values from 0 to 255. Currently, Python’s static type system cannot address this challenge.

## Deprecated Collection Types
To provide initial support for generic type hints, the authors of PEP 484 created generic types in the `typing` module. Here are some collection types and their type hint equivalents:

| Collection           | Type hint equivalent          |
|----------------------|-------------------------------|
| list                 | `typing.List`                 |
| set                  | `typing.Set`                  |
| frozenset            | `typing.FrozenSet`            |
| collections.deque    | `typing.Deque`                |
| collections.abc.MutableSequence | `typing.MutableSequence` |
| collections.abc.Sequence        | `typing.Sequence`        |
| collections.abc.Set             | `typing.AbstractSet`     |
| collections.abc.MutableSet      | `typing.MutableSet`      |

### Summary of PEP 585 Process
PEP 585 started a multiyear process to improve the usability of generic type hints. Here are the four steps:

1. Introduce `from __future__ import annotations` in Python 3.7 to enable the use of standard library classes as generics with `list[str]` notation.
2. Make that behavior the default in Python 3.9: `list[str]` now works without the `future` import.
3. Deprecate all the redundant generic types from the `typing` module. Deprecation warnings will not be issued by the Python interpreter because type checkers should flag the deprecated types when the checked program targets Python 3.9 or newer.
4. Remove those redundant generic types in the first version of Python released five years after Python 3.9. At the current cadence, that could be Python 3.14, also known as Python Pi.

## Conclusion
Generic collections in Python allow you to specify the types of items they contain, making your code more robust and easier to understand. With the improvements brought by PEP 585, using generic type hints has become simpler and more intuitive.
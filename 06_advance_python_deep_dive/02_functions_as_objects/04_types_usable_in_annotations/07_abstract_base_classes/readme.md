# Abstract Base Classes (ABCs)

## Overview

**Postel’s Law (Robustness Principle)**: 
- **Be conservative in what you send, be liberal in what you accept.**

Using abstract base classes from `collections.abc` allows functions to accept more flexible argument types, increasing the flexibility for the caller.

## Key Abstract Base Classes

Several abstract classes from `collections.abc` are commonly used in type hints for better flexibility and robustness. Here are a few important ones:

| Abstract Class         | Description                                     |
|------------------------|-------------------------------------------------|
| `Mapping`              | Represents a collection of key-value pairs.     |
| `MutableMapping`       | Represents a mutable collection of key-value pairs.|
| `Sequence`             | Represents an ordered collection of items.      |
| `Iterable`             | Represents any object capable of returning its members one at a time. |

## Example: Using `Mapping` for Flexibility

Consider the function signature using `Mapping`:

```python
from collections.abc import Mapping

def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    ...
```

- **Benefit**: Allows the caller to pass any object that is a subtype of `Mapping`, such as `dict`, `defaultdict`, `ChainMap`, `UserDict`, etc.
  
In contrast, using a concrete type like `dict` restricts the flexibility:

```python
def name2hex(name: str, color_map: dict[str, int]) -> str:
    ...
```

- **Limitation**: The `color_map` must be a `dict` or one of its subtypes, but not a `UserDict`, even though `UserDict` is a subtype of `MutableMapping`.

### Example Code Using `Mapping`

```python
from collections.abc import Mapping

def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    hex_value = color_map.get(name)
    if hex_value is None:
        raise ValueError(f"Name '{name}' not found in color_map.")
    return f"#{hex_value:06x}"
```

### Example Usage

```python
color_map = {
    'red': 0xff0000,
    'green': 0x00ff00,
    'blue': 0x0000ff
}

print(name2hex('red', color_map))  # Output: #ff0000
```

## Return Type Hints

**Postel’s Law** also suggests being conservative in what we send. For return type hints, use concrete types for clarity:

```python
def tokenize(text: str) -> list[str]:
    return text.upper().split()
```

- **Reason**: The return value of a function is always a concrete object.

## Type Hinting in Python ≥ 3.9

Most ABCs and concrete classes from `collections` support generic type hint notation like `collections.deque[str]` starting with Python 3.9. Use the `typing` module for code compatibility with Python 3.8 or earlier.

## Numeric Tower

The `numbers` package defines a numeric tower, but these ABCs are not supported for static type checking. Use concrete types or numeric protocols for annotations.

### Numeric Tower Hierarchy

- `Number`
- `Complex`
- `Real`
- `Rational`
- `Integral`

### Practical Recommendations for Numeric Annotations

1. **Use concrete types**: `int`, `float`, or `complex`.
2. **Union types**: `Union[float, Decimal, Fraction]`.
3. **Numeric protocols**: Use `SupportsFloat` and other runtime checkable static protocols.

### Example: Using `SupportsFloat`

```python
from typing import SupportsFloat

def to_float(value: SupportsFloat) -> float:
    return float(value)
```

## Iterable ABC

The `Iterable` ABC is one of the most useful for type hints, representing any object capable of returning its members one at a time.

### Example Code Using `Iterable`

```python
from collections.abc import Iterable

def flatten(items: Iterable[Iterable[int]]) -> list[int]:
    return [item for sublist in items for item in sublist]
```

### Example Usage

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

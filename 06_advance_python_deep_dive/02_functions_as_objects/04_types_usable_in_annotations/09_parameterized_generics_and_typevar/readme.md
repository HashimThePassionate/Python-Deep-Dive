# Parameterized Generics and TypeVar

## Overview

Parameterized generics and `TypeVar` allow you to write functions that can handle different types in a flexible way. This is particularly useful for creating functions that can work with various types of inputs while ensuring type safety.

### What is a Parameterized Generic?

A parameterized generic is a way to define a type that can be parameterized with another type. For example, `list[T]` means a list where all elements are of type `T`.

### What is a Type Variable?

A `TypeVar` is a type variable that can be used to parameterize generics. It allows you to write functions that can accept different types and return values of the same type.

## Example: Using TypeVar

Let's start with a simple example to explain the concept.

### Function Definition

The following function `sample` takes:
- A `Sequence` of elements of type `T`.
- An `int` representing the number of items to sample.

It returns a `list` of elements of the same type `T`.

### Example: `sample.py`

```python
from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar('T')

def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError('size must be >= 1')
    result = list(population)
    shuffle(result)
    return result[:size]
```

### Explanation

- **TypeVar**: `T` is a type variable, meaning it can represent any type.
- **Function Signature**: The function `sample` takes a `Sequence` of `T` and an `int`. It returns a `list` of `T`.

### Usage Examples

1. **With a tuple of integers**:
    ```python
    population = (1, 2, 3, 4, 5)
    print(sample(population, 3))  # Output: [2, 4, 1] (example, actual output will be random)
    ```

2. **With a string**:
    ```python
    population = "abcdef"
    print(sample(population, 3))  # Output: ['e', 'a', 'b'] (example, actual output will be random)
    ```

In the first example, `T` is `int`, so the return type is `list[int]`. In the second example, `T` is `str`, so the return type is `list[str]`.

### Why Is TypeVar Needed?

The `TypeVar` constructor is necessary because Python's type hinting system needs a way to introduce the type variable in the current namespace. This allows for parameterized types without changing the core language syntax.

## Example: statistics.mode Function

The `statistics.mode` function returns the most common data point from a series.

### Without TypeVar

Here's how you might write the `mode` function without using `TypeVar`:

```python
from collections import Counter
from collections.abc import Iterable

def mode(data: Iterable[float]) -> float:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]
```

### With TypeVar

To make `mode` more flexible, we can use `TypeVar`:

```python
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar('T')

def mode(data: Iterable[T]) -> T:
    from collections import Counter
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]
```

### Explanation

- **TypeVar**: `T` allows `mode` to accept and return any type.
- **Iterable**: The function accepts an `Iterable` of `T`.

## Restricted TypeVar

Sometimes, you want to restrict the types that a `TypeVar` can represent. For example, you might want `mode` to only work with numerical types.

### Example

```python
from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

NumberT = TypeVar('NumberT', float, Decimal, Fraction)

def mode(data: Iterable[NumberT]) -> NumberT:
    from collections import Counter
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]
```

### Explanation

- **TypeVar with Restrictions**: `NumberT` can only be `float`, `Decimal`, or `Fraction`.
- **Function Signature**: `mode` now only accepts an `Iterable` of `NumberT` and returns a `NumberT`.

### Handling Strings

If `mode` also needs to handle strings, you can include `str` in the `TypeVar`:

```python
NumberT = TypeVar('NumberT', float, Decimal, Fraction, str)
```

### Better Approach with Bounded TypeVar

A more flexible way to handle this is by using a bounded `TypeVar`:

```python
from collections.abc import Iterable, Hashable
from typing import TypeVar

HashableT = TypeVar('HashableT', bound=Hashable)

def mode(data: Iterable[HashableT]) -> HashableT:
    from collections import Counter
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]
```

### Explanation

- **Bounded TypeVar**: `HashableT` can be any type that is a subtype of `Hashable`.
- **Function Signature**: `mode` accepts an `Iterable` of `HashableT` and returns a `HashableT`.

## Summary

- **Restricted TypeVar**: Limits the type variable to specific types.
- **Bounded TypeVar**: Sets an upper boundary for acceptable types.

### The AnyStr Predefined Type Variable

`AnyStr` is a predefined `TypeVar` in the `typing` module:

```python
from typing import TypeVar

AnyStr = TypeVar('AnyStr', bytes, str)
```

- **Usage**: Functions that accept either `bytes` or `str`, and return values of the same type.

### Next Topic: Typing Protocol

The next section covers `typing.Protocol`, a feature introduced in Python 3.8 for more Pythonic use of type hints.

# Using Iterable for Function Parameters

## Overview

When defining function parameter type hints, using abstract types like `Sequence` and `Iterable` is recommended over concrete types like `list`. This provides more flexibility to the caller.

### Example from Standard Library

The `math.fsum` function in the standard library is a great example of using `Iterable` for function parameters:
```python
def fsum(__seq: Iterable[float]) -> float:
```

- **__seq**: The leading underscores indicate positional-only parameters.
- **Iterable[float]**: Accepts any iterable of floats, not just lists.

## Stub Files and the Typeshed Project

As of Python 3.10, the standard library itself does not have annotations, but tools like Mypy and PyCharm can find the necessary type hints in the Typeshed project. These are provided in the form of stub files with a `.pyi` extension, containing annotated function and method signatures without implementations.

For example, the signature for `math.fsum` can be found in `/stdlib/2and3/math.pyi`.

## Example: Iterable Parameter

Here is an example of using an `Iterable` parameter that processes items of type `tuple[str, str]`.

### Usage Example

```python
>>> l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0')]
>>> text = 'mad skilled noob powned leet'
>>> from replacer import zip_replace
>>> zip_replace(text, l33t)
'm4d sk1ll3d n00b p0wn3d l33t'
```

### Implementation (replacer.py)

```python
from collections.abc import Iterable

FromTo = tuple[str, str]

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text
```

### Explanation

- **Type Alias**: `FromTo` is defined as `tuple[str, str]` to make the function signature more readable.
- **Function Signature**: `zip_replace` takes a string `text` and an iterable of `FromTo` tuples (`Iterable[FromTo]`).

### Python 3.10 Feature: Explicit TypeAlias

PEP 613 introduced `TypeAlias` to make type aliases more visible and easier to type check.

```python
from typing import TypeAlias

FromTo: TypeAlias = tuple[str, str]
```

## Iterable vs. Sequence

### Iterable Parameter

Functions like `math.fsum` and `replacer.zip_replace` accept an `Iterable` parameter and iterate over the entire input to return a result. This allows the caller to provide input data as a generator, which can save memory if the number of input items is large.

### Sequence Parameter

In contrast, functions that need to know the length of the input up front, such as `columnize`, require a `Sequence` parameter instead of an `Iterable`.

### Example: Sequence Parameter

```python
from collections.abc import Sequence

def columnize(items: Sequence[str], num_columns: int) -> list[str]:
    num_rows = len(items) // num_columns
    ...
```

### Summary

- **Iterable**: Best used as a parameter type, especially when the function needs to process the input completely.
- **Sequence**: Required when the function needs to know the length of the input up front.

### Note on Return Types

While `Iterable` is useful as a parameter type, it is too vague as a return type. Functions should be more precise about the concrete type they return.

### Related Types

- **Iterator**: Closely related to `Iterable` and used as a return type for functions that generate items one at a time. This will be covered in detail in Chapter 17, which focuses on generators and iterators.
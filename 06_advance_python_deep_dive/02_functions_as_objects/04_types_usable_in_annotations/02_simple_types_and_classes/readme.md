# Simple Types and Classes

Simple types like `int`, `float`, `str`, and `bytes` can be used directly in type hints. Concrete classes from the standard library, external packages, or user-defined classes like `FrenchDeck`, `Vector2d`, and `Duck` may also be used in type hints.

### Example:

```python
# Example using simple types and classes in type hints

from typing import List, Union

# Simple types
def add_numbers(a: int, b: float) -> float:
    return a + b

# Concrete class
class Vector2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector2d({self.x}, {self.y})'

# Abstract base class example (later in the section)
from collections.abc import Iterable

def process_items(items: Iterable[Union[int, float]]) -> float:
    return sum(items)

# User-defined class example
class Duck:
    def quack(self) -> str:
        return "Quack!"

def make_it_quack(duck: Duck) -> str:
    return duck.quack()
```

### int Is Consistent-With complex

There is no nominal subtype relationship between the built-in types `int`, `float`, and `complex`: they are direct subclasses of `object`. However, PEP 484 declares that `int` is consistent with `float`, and `float` is consistent with `complex`.

This practical approach makes sense because `int` implements all the operations that `float` does and more, such as bitwise operations like `&`, `|`, `<<`, etc. Therefore, `int` is considered consistent with `complex`. For example, for `i = 3`, `i.real` is 3, and `i.imag` is 0.

#### Example:

```python
# Example demonstrating int is consistent with complex

def process_number(num: complex) -> str:
    return f"Real part: {num.real}, Imaginary part: {num.imag}"

# Using an int, which is consistent with complex
result = process_number(3)
print(result)  # Output: Real part: 3.0, Imaginary part: 0.0

# Using a float, which is consistent with complex
result = process_number(3.5)
print(result)  # Output: Real part: 3.5, Imaginary part: 0.0

# Using a complex number
result = process_number(3 + 4j)
print(result)  # Output: Real part: 3.0, Imaginary part: 4.0

# Type Hints
### Introduction
Type hints, also known as type annotations, are used to declare the expected types of function arguments, return values, variables, and attributes in Python.

### Key Points:
1. **Type Hints Purpose**: 
   - They specify what types of values are expected.
   - They help with code readability and maintenance.

2. **Non-Enforcement**:
   - Python’s bytecode compiler and interpreter do not enforce type hints.
   - They serve as guidance for developers and tools like type checkers.

### Overview:
- This guide provides a brief introduction to type hints.
- It explains the basic syntax and meaning of annotations, focusing on `typing.NamedTuple` and `@dataclass` declarations.
- More detailed information on function signatures and advanced annotations will be covered in later chapters.

### Common Types:
- Simple built-in types such as `str`, `int`, and `float` are commonly used in type hints.
- These types are often used to annotate fields in data classes.

## Example Usage:
### Annotating Variables:
```python
name: str = "Hashim"
age: int = 25
height: float = 5.9
```

### Function Arguments and Return Values:
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### Data Classes with Type Hints:
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    height: float
```

## Future Topics:
- Detailed type hints for function signatures upcomimg repository section.
- Advanced annotations also come in upcomimg repository section.

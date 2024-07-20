# Understanding Types and Supported Operations

## Introduction
This section covers the concept of types in Python, focusing on how types are defined by the operations they support. It also explores the differences between duck typing and nominal typing, using examples to illustrate these concepts.

## Key Concepts

### Types and Supported Operations
A type in Python can be understood as a set of values and a set of functions (operations) that can be applied to these values.

**PEP 483** defines type as a set of values and functions applicable to these values.

```python
def double(x):
    return x * 2
```
In the above function, `x` can be of various types:
- Numeric types: `int`, `complex`, `Fraction`, `numpy.uint32`
- Sequence types: `str`, `tuple`, `list`, `array`
- Any type that implements the `__mul__` method with an `int` argument.

#### Explanation of `__mul__` Method

In Python, the `__mul__` method is a special method used to define the behavior of the multiplication operator (`*`) for objects of a class. When you use the `*` operator with an object, Python internally calls the `__mul__` method of that object.

When we say "any type that implements the `__mul__` method with an `int` argument," we mean that the type (class) of the object must have a `__mul__` method defined, and this method should be able to accept an `int` as an argument. This allows the object to be multiplied by an integer.

Here's an example to illustrate this:

```python
class CustomType:
    def __mul__(self, other):
        if isinstance(other, int):
            return "Multiplication with int"
        else:
            return "Unsupported operation"

# Creating an instance of CustomType
obj = CustomType()

# Multiplying the object by an integer
result = obj * 2  # This calls obj.__mul__(2)
print(result)  # Output: Multiplication with int

# Multiplying the object by a non-integer
result = obj * 2.0  # This calls obj.__mul__(2.0)
print(result)  # Output: Unsupported operation
```

In this example:
- The `CustomType` class has a `__mul__` method that checks if the other argument is an integer.
- If it is an integer, it returns a specific message.
- If it is not an integer, it returns a different message indicating the operation is unsupported.

This means that for the `double(x)` function to work, `x` must be of a type that has a `__mul__` method capable of handling an integer. This includes built-in types like `int`, `str`, `list`, `tuple`, and custom types like the `CustomType` shown above.

**When using type hints, a type checker ensures the correct types are used according to the annotations**

```python
from collections import abc

def double(x: abc.Sequence):
    return x * 2
```
```sh
main.py:4: error: Unsupported operand types for * ("Sequence[Any]" and "int")  [operator]
Found 1 error in 1 file (checked 1 source file)
```

>Here, a type checker like Mypy will flag `x * 2` as an error because `abc.Sequence` does not define a `__mul__` method. Although the code may work at runtime, the type checker strictly follows the declared types.

### Complete Example: Implementing `__mul__` Method

Here's a custom class `CustomSequence` that implements the `__mul__` method using generics. We'll also show how to use this class with the `double` function and ensure that Mypy does not show any errors.

**Example: custom_sequence.py**
```python
from typing import List, TypeVar, Generic

T = TypeVar('T')

class CustomSequence(Generic[T]):
    def __init__(self, items: List[T]):
        self.items = items

    def __getitem__(self, index: int) -> T:
        return self.items[index]

    def __len__(self) -> int:
        return len(self.items)

    def __mul__(self, other: int) -> 'CustomSequence[T]':
        if isinstance(other, int):
            return CustomSequence(self.items * other)
        else:
            return NotImplemented

def double(x: CustomSequence[T]) -> CustomSequence[T]:
    return x * 2

# Testing the double function with CustomSequence
seq = CustomSequence([1, 2, 3])
result = double(seq)
print(result.items)  # Output: [1, 2, 3, 1, 2, 3]
```

**Explanation:**
- The `CustomSequence` class inherits from `Generic[T]`, making it a valid sequence that can handle any type `T`.
- The `__mul__` method is implemented to handle multiplication with an integer.
- The `double` function takes a `CustomSequence` and multiplies it by 2.
- We create an instance of `CustomSequence` and pass it to the `double` function. The result is printed to show that the multiplication works correctly.

**Running Mypy:**
```sh
$ mypy main.py
Success: no issues found in 1 source file
```

>Mypy does not show any errors because the `CustomSequence` class correctly implements the `__mul__` method, and the `double` function is properly annotated to accept any `CustomSequence`.

### Duck Typing vs. Nominal Typing

#### Duck Typing
- Used by languages like Python, JavaScript, and Ruby.
- Objects have types, but variables do not.
- Operations are checked at runtime.
- Flexible but allows more runtime errors.

```python
class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack!')

def alert(birdie):
    birdie.quack()
```

In the above example, `alert` function works with any object that has a `quack` method.

#### Nominal Typing
- Used by languages like C++, Java, and C#.
- Both objects and variables have types.
- Types are checked at compile-time or using a type checker.
- Rigid but catches errors early.

```python
def alert_duck(birdie: Duck) -> None:
    birdie.quack()

def alert_bird(birdie: Bird) -> None:
    birdie.quack()
```

Here, Mypy will flag `alert_bird` as problematic because `Bird` does not have a `quack` method, even though `Duck` does.

### Example: Birds and Ducks

**Example 1: birds.py**
```python
class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack!')

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck) -> None:
    birdie.quack()

def alert_bird(birdie: Bird) -> None:
    birdie.quack()
```

**Example 2: daffy.py**
```python
from main import *
daffy = Duck()
alert(daffy)        # Valid call, no type hints
alert_duck(daffy)   # Valid call, daffy is a Duck
alert_bird(daffy)   # Valid call, daffy is also a Bird
```

Running Mypy on `daffy.py` shows no issues, but it flags `alert_bird` in `birds.py` as problematic:
```sh
$ mypy birds.py
birds.py:16: error: "Bird" has no attribute "quack"
```

**Example 3: woody.py**
```python
from main import *
woody = Bird()
alert(woody)        # Runtime error: 'Bird' object has no attribute 'quack'
alert_duck(woody)   # Runtime error: Argument 1 to "alert_duck" has incompatible type "Bird"; expected "Duck"
alert_bird(woody)   # Runtime error: 'Bird' object has no attribute 'quack'
```

Mypy helps catch errors early:
```sh
$ mypy woody.py
birds.py:16: error: "Bird" has no attribute "quack"
woody.py:5: error: Argument 1 to "alert_duck" has incompatible type "Bird"; expected "Duck"
```

## Conclusion
Type hints provide significant benefits, especially in large codebases. They help catch errors early and ensure code reliability. Companies like Dropbox, Google, and Facebook extensively use type hints in their Python codebases.

# Generic Methods 

```python
from typing import TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other):
        return NotImplemented

def max_util(first: T, second: T) -> T:
    return second if first < second else first

max_value_int = max_util(1, 2)  # Using integers
print(max_value_int)  # Output: 2

max_value_float = max_util(1.5, 2.5)  # Using floats
print(max_value_float)  # Output: 2.5

max_value_str = max_util("apple", "banana")  # Using strings
print(max_value_str) 

```

### 1. **Importing TypeVar from typing Module**
```python
from typing import TypeVar
```
The `typing` module is used to provide type hints. `TypeVar` allows you to define a generic type variable.

### 2. **Defining a Type Variable**
```python
T = TypeVar('T', bound='Comparable')
```
Here, `T` is a type variable that can be any type that extends the `Comparable` class. The `bound='Comparable'` part means that `T` must be a type that supports the comparison operations defined in the `Comparable` class.

### 3. **Defining the Comparable Class**
```python
class Comparable:
    def __lt__(self, other):
        return NotImplemented
```
The `Comparable` class is a minimal implementation of a comparable interface. The method `__lt__` (less than) is defined but not implemented, indicating that any subclass should provide its own implementation.

### 4. **Defining the Generic Method**
```python
def max_util(first: T, second: T) -> T:
    return second if first < second else first
```
The `max_util` function is a generic method. It takes two arguments, `first` and `second`, both of type `T`, and returns a value of type `T`. The function compares the two arguments using the less than operator (`<`) and returns the greater of the two.

### 5. **Using the Generic Method**
The `max_util` function can be used with any types that support the comparison operations (`<`). Here's how it's used with integers, floats, and strings:

#### Using Integers
```python
max_value_int = max_util(1, 2)  # Using integers
print(max_value_int)  # Output: 2
```
The `max_util` function is called with integers `1` and `2`. Since `1 < 2`, the function returns `2`.

#### Using Floats
```python
max_value_float = max_util(1.5, 2.5)  # Using floats
print(max_value_float)  # Output: 2.5
```
The `max_util` function is called with floats `1.5` and `2.5`. Since `1.5 < 2.5`, the function returns `2.5`.

#### Using Strings
```python
max_value_str = max_util("apple", "banana")  # Using strings
print(max_value_str)
```
The `max_util` function is called with strings `"apple"` and `"banana"`. Since `"apple" < "banana"` (lexicographical comparison), the function returns `"banana"`.

### Summary
This example demonstrates the following benefits of using a generic method:

- **Flexibility**: The `max_util` function can handle different types (integers, floats, strings) as long as they implement the comparison operations.
- **Reusability**: The same function can be reused for different types, reducing code duplication.
- **Type Safety**: The use of type hints ensures that the arguments passed to the function are of the correct type, providing compile-time checks and better code readability.

This is a powerful feature in Python that allows for writing more abstract and reusable code, similar to the use of generics in languages like Java and C#.
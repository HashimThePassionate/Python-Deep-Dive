# Generics with inheritance:

### Importing Required Modules
```python
from typing import Generic, TypeVar, List
```
The `typing` module is imported to use type hints, including `Generic`, `TypeVar`, and `List`.

### Declaring a Type Variable
```python
T = TypeVar('T')  # Type variable for elements in the container
```
A type variable `T` is declared using `TypeVar`. This variable represents the type of elements that will be stored in the container.

### Defining a Generic Class
```python
class Container(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
```
`Container` is a generic class that takes a type parameter `T`. It initializes a list `_items` to store elements of type `T`.

### Implementing Methods in the Generic Class
```python
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def get_all(self) -> List[T]:
        return self._items
```
Two methods are implemented in the `Container` class:
- `add`: Adds an item of type `T` to the container.
- `get_all`: Returns a list of all items in the container.

### Subclass Inheriting from Container
```python
class StringContainer(Container[str]):
    def __init__(self) -> None:
        super().__init__()  # Call the constructor of the base class
```
`StringContainer` is a subclass of `Container`, specialized to work with strings (`str`). It inherits from `Container[str]`, indicating that it uses `str` as the type parameter `T`.

### Adding a Custom Method in the Subclass
```python
    def join_strings(self, delimiter: str = ' ') -> str:
        return delimiter.join(self.get_all())
```
`StringContainer` adds a custom method `join_strings`, which joins all strings in the container using a delimiter.

### Example Usage
```python
if __name__ == "__main__":
    string_container = StringContainer()
    string_container.add("Hello")
    string_container.add("World")
    string_container.add("!")

    print(string_container.join_strings())  # Output: Hello World !
```
- An instance of `StringContainer` is created.
- Strings `"Hello"`, `"World"`, and `"!"` are added to the container using the `add` method.
- The `join_strings` method is called to join all strings in the container with a space delimiter and printed.

### Summary
- Using generics with inheritance allows for creating specialized subclasses of generic classes, tailored to work with specific types.
- In this example, `StringContainer` inherits from `Container[str]`, enabling it to work with strings.
- Subclasses can extend the functionality of the base class by adding custom methods or overriding existing ones.
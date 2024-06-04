#   Multiple type parameters

### Importing Required Modules
```python
from typing import Generic, TypeVar, Dict
```
Here, we import `Generic` from the `typing` module to define a generic class, `TypeVar` to declare type variables, and `Dict` to use a dictionary data structure.

### Declaring Type Variables
```python
K = TypeVar('K')  # Key type
V = TypeVar('V')  # Value type
```
Two type variables, `K` and `V`, are declared using `TypeVar`. `K` represents the type of keys in the dictionary, and `V` represents the type of values in the dictionary.

### Defining the Generic Class
```python
class GenericDict(Generic[K, V]):
    def __init__(self) -> None:
        self._store: Dict[K, V] = {}
```
`GenericDict` is a generic class that takes two type parameters, `K` and `V`. Inside the class, a dictionary `_store` is initialized with keys of type `K` and values of type `V`.

### Implementing Methods
```python
def set_item(self, key: K, value: V) -> None:
    self._store[key] = value

def get_item(self, key: K) -> V:
    return self._store[key]
```
These methods allow setting and getting items from the dictionary. The `key` parameter is of type `K`, and the `value` parameter is of type `V`.

### Overriding the `__str__` Method
```python
def __str__(self) -> str:
    items = [f"{key} = '{value}'" for key, value in self._store.items()]
    return ", ".join(items)
```
This method overrides the default string representation of the class. It iterates through the key-value pairs in the dictionary and constructs a string representation of the items.

### Example Usage
```python
if __name__ == "__main__":
    str_int_dict = GenericDict[str, int]()
    str_int_dict.set_item("one", 1)
    str_int_dict.set_item("two", 2)
    
    print(str_int_dict)  # Output: one = '1', two = '2'

    int_str_dict = GenericDict[int, str]()
    int_str_dict.set_item(1, "one")
    int_str_dict.set_item(2, "two")
    
    print(int_str_dict)  # Output: 1 = 'one', 2 = 'two'
```
- Two instances of `GenericDict` are created: `str_int_dict` with string keys and integer values, and `int_str_dict` with integer keys and string values.
- Items are added to each dictionary using the `set_item` method.
- The dictionaries are printed, showing the key-value pairs.

### Summary
Using multiple type parameters in a generic class allows for creating flexible and reusable data structures or utilities that can work with different types. In this example, `GenericDict` can handle dictionaries with keys and values of any specified types, enhancing code flexibility and readability.
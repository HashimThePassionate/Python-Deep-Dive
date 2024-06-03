# Generic Classes

We achieve a generic type class in Python using the `typing` module and the `TypeVar` function. Let's break down how it works:

### 1. Importing Necessary Modules and Declaring Type Variable:

```python
from typing import TypeVar, List

T = TypeVar('T')  # Declare a type variable 'T'
```

- We import the `TypeVar` and `List` classes from the `typing` module.
- We declare a type variable `T` using `TypeVar('T')`, which represents a generic type that can be specified later.

### 2. Defining the Generic Class:

```python
class GenericList:
    def __init__(self):
        self.items: List[T] = []

    def add_item(self, item: T):
        self.items.append(item)

    def get_items(self) -> List[T]:
        return self.items

    def check_type(self):
        if self.items:
            return type(self.items[0])
        else:
            return None
```

- We define a class named `GenericList`, which represents a generic list.
- Inside the class, we use the type variable `T` to specify that the `items` attribute is a list of elements of type `T`.
- The `add_item` method allows adding an item of type `T` to the list.
- The `get_items` method returns the list of items.
- The `check_type` method checks the type of the first item in the list and returns it.

### 3. Testing the GenericList Class:

```python
# Test the GenericList class with different data types

# Create a GenericList for integers
int_list = GenericList()
int_list.add_item(1)
int_list.add_item(2)
int_list.add_item(3)
print("Integer List:", int_list.get_items())
print("Type of items in Integer List:", int_list.check_type())

# Create a GenericList for strings
str_list = GenericList()
str_list.add_item("apple")
str_list.add_item("banana")
str_list.add_item("orange")
print("String List:", str_list.get_items())
print("Type of items in String List:", str_list.check_type())
```

- We create instances of the `GenericList` class for integers and strings.
- We add items to each list and print the list of items and the type of items in each list.

### Summary:

In this code, we achieve a generic type class in Python by using the `TypeVar` function from the `typing` module. By declaring a type variable `T`, we can create a class (`GenericList`) that can work with different types of data while maintaining type safety. This approach allows for greater flexibility and reusability in our code, as the same class can be used with various data types without modification.
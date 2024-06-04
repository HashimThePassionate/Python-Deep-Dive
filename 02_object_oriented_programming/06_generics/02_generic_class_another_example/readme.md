# Generic Class Example two

### Defining the Generic Class

```python
from typing import Dict, Generic, TypeVar

T = TypeVar("T")

class Registry(Generic[T]):
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}
          
    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v
    
    def get_item(self, k: str) -> T:
        return self._store[k]
```

- `TypeVar("T")`: Defines a type variable `T` which can be any type. This is used to create a generic class.
- `class Registry(Generic[T])`: Defines a generic class `Registry` that takes a single type parameter `T`.
- `self._store: Dict[str, T]`: This dictionary will store values of type `T` indexed by strings.
- `def set_item(self, k: str, v: T) -> None`: This method accepts a key of type `str` and a value of type `T` and stores them in the dictionary.
- `def get_item(self, k: str) -> T`: This method returns a value of type `T` corresponding to the provided key.

### Using the Generic Class

```python
family_name_reg = Registry[str]()
family_age_reg = Registry[int]()
```

- `Registry[str]`: Creates an instance of `Registry` where the type `T` is specified as `str`. This means the `family_name_reg` will store string values.
- `Registry[int]`: Creates an instance of `Registry` where the type `T` is specified as `int`. This means the `family_age_reg` will store integer values.

### Storing and Retrieving Data

```python
family_name_reg.set_item("husband", "steve")
print(family_name_reg.get_item('husband'))
print(type(family_name_reg.get_item('husband')))
family_name_reg.set_item("dad", "john")

family_age_reg.set_item("steve", 30)
print(family_age_reg.get_item('steve'))
print(type(family_age_reg.get_item('steve')))
```

- `family_name_reg.set_item("husband", "steve")`: Stores the string `"steve"` with the key `"husband"` in `family_name_reg`.
- `print(family_name_reg.get_item('husband'))`: Retrieves the value associated with `"husband"`, which is `"steve"`, and prints it.
- `print(type(family_name_reg.get_item('husband')))`: Prints the type of the value retrieved, which is `<class 'str'>`.
- `family_name_reg.set_item("dad", "john")`: Stores the string `"john"` with the key `"dad"` in `family_name_reg`.

- `family_age_reg.set_item("steve", 30)`: Stores the integer `30` with the key `"steve"` in `family_age_reg`.
- `print(family_age_reg.get_item('steve'))`: Retrieves the value associated with `"steve"`, which is `30`, and prints it.
- `print(type(family_age_reg.get_item('steve')))`: Prints the type of the value retrieved, which is `<class 'int'>`.

### Output

```
steve
<class 'str'>
30
<class 'int'>
```

The output shows that the `Registry` class can store and retrieve data of different types (`str` and `int` in this case), demonstrating how generics provide flexibility while maintaining type safety.
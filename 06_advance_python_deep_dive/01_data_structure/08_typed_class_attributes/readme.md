# Typed Class Attributes in dataclass

## Introduction
When using `@dataclass` in Python, it's important to correctly annotate class attributes for type checking. This section explains how to handle typed class attributes, particularly using `typing.ClassVar` to ensure proper type checking and avoid issues with `@dataclass`.

### Problem
If you run type checking with Mypy on a dataclass with class-level attributes, you might encounter errors. For example:

```bash
$ mypy main.py
hackerclub.py:37: error: Need type annotation for "all_handles"
(hint: "all_handles: Set[<type>] = ...")
Found 1 error in 1 file (checked 1 source file)
```

This error occurs because Mypy requires a type annotation for the class attribute `all_handles`.

### Incorrect Hint
Mypy's hint suggests using `Set`, but with Python 3.9, you can use `set` directly. Additionally, simply adding a type hint like `set[...]` will make `@dataclass` treat `all_handles` as an instance field, which is not desired.

### Solution: Using `ClassVar`
To correctly annotate class attributes without making them instance fields, use `ClassVar` from the `typing` module.

### Example
Here's how to modify the `HackerClubMember` class to use `ClassVar` for the `all_handles` attribute:

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class HackerClubMember(ClubMember):
    all_handles: ClassVar[set[str]] = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__  # Get the class of the current instance
        if self.handle == '':
            self.handle = self.name.split()[0]  # Take the first part of the name
        if self.handle in cls.all_handles:
            raise ValueError(f'handle {self.handle!r} already exists.')
        cls.all_handles.add(self.handle)
```

### Explanation

#### Class Attribute with `ClassVar`
- **`all_handles: ClassVar[set[str]] = set()`**: This line declares `all_handles` as a class attribute of type `set` containing strings, with an empty set as its default value.
  - **`ClassVar`**: Imported from the `typing` module, used to indicate that `all_handles` is a class variable and should not be treated as an instance variable by `@dataclass`.

#### Instance Attribute
- **`handle`**: A string attribute with a default value of an empty string.

#### `__post_init__` Method
- **Retrieve Class**: `cls = self.__class__` gets the class of the current instance.
- **Default Handle**: If `handle` is not provided, set it to the first part of the `name` using `self.name.split()[0]`.
- **Unique Handle Validation**: Check if the `handle` is already in `all_handles`. If it is, raise a `ValueError`.
- **Add Handle**: Add the new unique `handle` to `all_handles`.

### Benefits
- **Type Safety**: Ensures that class attributes are properly type-checked.
- **Avoids Instance Fields**: Prevents `@dataclass` from treating class attributes as instance fields.

### Additional Note
The `@dataclass` decorator doesn’t care about the types in the annotations except in two cases:
1. **ClassVar**: Ensures an attribute is not treated as an instance field.
2. **Init-only Variables**: Declaring variables that should only be initialized once (explained in further detail in subsequent topics).

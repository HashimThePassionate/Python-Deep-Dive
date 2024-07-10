# Post-init Processing in dataclass

## Introduction
The `@dataclass` decorator in Python simplifies the creation of classes by automatically generating special methods like `__init__`. However, the generated `__init__` method only handles simple assignment of arguments to instance attributes. For more complex initialization, you can use the `__post_init__` method. This README explains how to use `__post_init__` for additional initialization tasks, such as validation and computing field values.

### Purpose of `__post_init__`
- **Additional Initialization**: Perform tasks beyond simple attribute assignment.
- **Validation**: Ensure the instance adheres to certain constraints.
- **Field Computation**: Derive some field values based on others.

### Example: HackerClubMember
Consider a subclass `HackerClubMember` of `ClubMember`. We want each `HackerClubMember` to have a unique `handle`, which defaults to the first part of the member's name if not provided.

Code **club.py**
```python
from dataclasses import dataclass, field
@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
```
Code **club.py**
```python
from dataclasses import dataclass
from club import ClubMember

@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)
```

### Expected Behavior
Here are the expected behaviors described by doctests:

#### Example Tests
```python
"""
`HackerClubMember` objects accept an optional `handle` argument:
>>> anna = HackerClubMember('Anna Ravenscroft', handle='AnnaRaven')
>>> anna
HackerClubMember(name='Anna Ravenscroft', guests=[], handle='AnnaRaven')

If `handle` is omitted, it's set to the first part of the member's name:
>>> leo = HackerClubMember('Leo Rochael')
>>> leo
HackerClubMember(name='Leo Rochael', guests=[], handle='Leo')

Members must have a unique handle. The following `leo2` will not be created,
because its `handle` would be 'Leo', which was taken by `leo`:
>>> leo2 = HackerClubMember('Leo DaVinci')
Traceback (most recent call last):
...
ValueError: handle 'Leo' already exists.

To fix, `leo2` must be created with an explicit `handle`:
>>> leo2 = HackerClubMember('Leo DaVinci', handle='Neo')
>>> leo2
HackerClubMember(name='Leo DaVinci', guests=[], handle='Neo')
"""
```
### Explanation

#### Class Definition and Inheritance
- **HackerClubMember extends ClubMember**: This means `HackerClubMember` inherits all attributes and methods from `ClubMember`.
- **Class Attribute `all_handles`**: A set that keeps track of all unique handles across instances of `HackerClubMember`.

#### Instance Attribute
- **`handle`**: A string attribute with a default value of an empty string. This makes it optional during instance creation.

#### `__post_init__` Method
- **Retrieve Class**: `cls = self.__class__` assigns the class of the instance to `cls`.
- **Default Handle**: `if self.handle == '': self.handle = self.name.split()[0]` sets the `handle` to the first part of the `name` if `handle` is not provided.
- **Unique Handle Validation**: 
  - `if self.handle in cls.all_handles`: Checks if the `handle` is already taken.
  - `msg = f'handle {self.handle!r} already exists.'`: Prepares an error message.
  - `raise ValueError(msg)`: Raises a `ValueError` if the `handle` is not unique.
- **Add Handle**: `cls.all_handles.add(self.handle)` adds the new unique `handle` to the set of all handles.

### Detailed Example with Explanation

#### Creating an instance with a specific handle

```python
anna = HackerClubMember(name='Anna Ravenscroft', handle='AnnaRaven')
print(anna)
# Output: HackerClubMember(name='Anna Ravenscroft', guests=[], handle='AnnaRaven')
```
- **Explanation**: 
  - Here, `anna` is created with a specific `handle` 'AnnaRaven'.
  - The `__post_init__` method verifies that 'AnnaRaven' is unique and adds it to `all_handles`.

#### Creating an instance without a handle

```python
leo = HackerClubMember(name='Leo Rochael')
print(leo)
# Output: HackerClubMember(name='Leo Rochael', guests=[], handle='Leo')
```
- **Explanation**:
  - `leo` is created without specifying a `handle`.
  - The `__post_init__` method sets `handle` to 'Leo', the first part of `name`, and adds it to `all_handles`.

#### Attempting to create another instance with a duplicate handle

```python
try:
    leo2 = HackerClubMember(name='Leo DaVinci')
except ValueError as e:
    print(e)
# Output: handle 'Leo' already exists.
```
- **Explanation**:
  - An attempt is made to create `leo2` without specifying a `handle`.
  - The `__post_init__` method defaults the `handle` to 'Leo', which already exists in `all_handles`, so it raises a `ValueError`.

#### Creating an instance with a unique handle

```python
leo2 = HackerClubMember(name='Leo DaVinci', handle='Neo')
print(leo2)
# Output: HackerClubMember(name='Leo DaVinci', guests=[], handle='Neo')
```
- **Explanation**:
  - `leo2` is successfully created with the unique `handle` 'Neo'.
  - The `__post_init__` method verifies that 'Neo' is unique and adds it to `all_handles`.

By using `__post_init__`, we ensure that each `HackerClubMember` has a unique handle and provide a default handle based on the member's name if none is provided. This additional initialization logic goes beyond the simple assignment handled by the `__init__` method generated by `@dataclass`.


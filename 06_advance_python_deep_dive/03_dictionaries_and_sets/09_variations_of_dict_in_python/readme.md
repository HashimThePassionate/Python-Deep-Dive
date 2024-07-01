# Variations of `dict` in Python

This document provides an overview of various mapping types included in the Python standard library, besides `defaultdict`.

## `collections.OrderedDict`

An `OrderedDict` is a dictionary that maintains the order of keys as they are added. Although the built-in `dict` also keeps keys ordered since Python 3.6, `OrderedDict` has additional features and differences:

### Features and Differences

- **Equality**: Checks for matching order.
  ```python
  from collections import OrderedDict

  # Creating two OrderedDicts
  od1 = OrderedDict([('a', 1), ('b', 2)])
  od2 = OrderedDict([('b', 2), ('a', 1)])

  # Equality check (order matters)
  print(od1 == od2)  # Output: False

  od3 = OrderedDict([('a', 1), ('b', 2)])
  print(od1 == od3)  # Output: True
  ```

- **popitem()**: Has a different signature and accepts an optional argument to specify which item is popped.
  ```python
  od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

  # Popping items
  print(od.popitem())  # Output: ('c', 3)
  print(od.popitem(last=False))  # Output: ('a', 1)
  ```

- **move_to_end()**: Efficiently repositions an element to an endpoint.
  ```python
  od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

  # Move 'a' to the end
  od.move_to_end('a')
  print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

  # Move 'b' to the start
  od.move_to_end('b', last=False)
  print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])
  ```

- **Design**: `OrderedDict` is optimized for reordering operations, whereas `dict` is optimized for mapping operations.

  - `OrderedDict` handles frequent reordering operations better than `dict`. This makes it suitable for tracking recent accesses, such as in an LRU (Least Recently Used) cache.

### Example Usage

```python
from collections import OrderedDict

# Creating an OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Accessing items
print(od['a'])  # Output: 1

# Adding and reordering items
od['d'] = 4
od.move_to_end('a')
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])
```

## `collections.ChainMap`

A `ChainMap` holds a list of mappings that can be searched as one. Lookups are performed on each mapping in the order they appear in the constructor.

### Example Usage

```python
from collections import ChainMap

# Creating dictionaries
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

# Creating a ChainMap
chain = ChainMap(d1, d2)

# Accessing items
print(chain['a'])  # Output: 1 (from d1)
print(chain['c'])  # Output: 6 (from d2)
```

### Explanation

- The `ChainMap` instance does not copy the input mappings but holds references to them.
- Updates or insertions to a `ChainMap` only affect the first input mapping.

```python
# Updating items in ChainMap
chain['c'] = -1
print(d1)  # Output: {'a': 1, 'b': 3, 'c': -1}
print(d2)  # Output: {'a': 2, 'b': 4, 'c': 6}
```

### Use Case

`ChainMap` is useful for implementing interpreters for languages with nested scopes, where each mapping represents a scope context.

## `collections.Counter`

A `Counter` is a dictionary subclass for counting hashable objects. It can be used to count instances or as a multiset.

### Example Usage

```python
from collections import Counter

# Counting letters in a word
ct = Counter('abracadabra')
print(ct)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Updating counts
ct.update('aaaaazzz')
print(ct)  # Output: Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Most common items
print(ct.most_common(3))  # Output: [('a', 10), ('z', 3), ('b', 2)]
```

### Explanation

- `Counter` holds an integer count for each key.
- Updating an existing key adds to its count.

### Using as a Multiset

To use `Counter` as a multiset, pretend each key is an element in the set, and the count is the number of occurrences of that element.

## `shelve.Shelf`

The `shelve` module provides persistent storage for a mapping of string keys to Python objects serialized in the pickle format.

### Example Usage

```python
import shelve

# Creating and using a shelf
with shelve.open('my_shelf.db') as shelf:
    shelf['key'] = 'value'
    print(shelf['key'])  # Output: value

# The shelf is automatically closed when exiting the with block
```

### Characteristics

- Subclasses `abc.MutableMapping`.
- Provides additional I/O management methods like `sync` and `close`.
- Context manager support ensures proper resource management.
- Keys must be strings, and values must be picklable objects.

## `collections.UserDict`

`UserDict` is intended to be a base class for creating custom mapping types by extending it rather than `dict`.

### Example: StrKeyDict Using `UserDict`

Here is an improved version of `StrKeyDict` using `UserDict` that ensures any keys added to the mapping are stored as strings.

```python
import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# Creating an object of StrKeyDict
d = StrKeyDict([('2', 'two'), ('4', 'four')])

# Accessing items
print(d[4])  # Output: 'four' (4 is converted to '4')

# Checking membership
print(2 in d)  # Output: True (2 is converted to '2')

# Setting items
d[1] = 'one'
print(d['1'])  # Output: 'one'
```

### Explanation

- **`__missing__` Method**: Handles missing keys by converting them to strings.
- **`__contains__` Method**: Simplified to check in `self.data` directly.
- **`__setitem__` Method**: Converts any key to a string before storing it.

### Advantages of Using `UserDict`

- Avoids implementation shortcuts in `dict` that complicate subclassing.
- Uses composition (an internal `data` dictionary) to hold items, simplifying method overrides and avoiding recursion issues.

## Conclusion

The Python standard library provides several variations of `dict` for different use cases, each with unique features and behaviors. Understanding these variations and their appropriate use cases can help you choose the right tool for your specific needs.

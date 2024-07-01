# Overview of Common Mapping Methods

The basic API for mappings in Python is quite rich. Below are the methods implemented by `dict` and two popular variations: `defaultdict` and `OrderedDict`, both defined in the `collections` module.

## Table of Mapping Methods

### Legend
- `●` indicates that the method is implemented in the respective mapping type.
- Optional arguments are enclosed in `[]`.

### Methods of `dict`, `collections.defaultdict`, and `collections.OrderedDict`

| Method                     | `dict` | `defaultdict` | `OrderedDict` | Description |
|----------------------------|--------|---------------|---------------|-------------|
| `d.clear()`                | ●      | ●             | ●             | Remove all items |
| `d.__contains__(k)`        | ●      | ●             | ●             | Check if key `k` is in `d` |
| `d.copy()`                 | ●      | ●             | ●             | Shallow copy |
| `d.__copy__()`             |        | ●             |               | Support for `copy.copy(d)` |
| `d.default_factory`        |        | ●             |               | Callable invoked by `__missing__` to set missing values |
| `d.__delitem__(k)`         | ●      | ●             | ●             | Remove item with key `k` |
| `d.fromkeys(it, [initial])`| ●      | ●             | ●             | Create new mapping from keys in iterable, with optional initial value (defaults to `None`) |
| `d.get(k, [default])`      | ●      | ●             | ●             | Get item with key `k`, return `default` or `None` if missing |
| `d.__getitem__(k)`         | ●      | ●             | ●             | Get item with key `k` |
| `d.items()`                | ●      | ●             | ●             | Get view over items—(key, value) pairs |
| `d.__iter__()`             | ●      | ●             | ●             | Get iterator over keys |
| `d.keys()`                 | ●      | ●             | ●             | Get view over keys |
| `d.__len__()`              | ●      | ●             | ●             | Get number of items |
| `d.__missing__(k)`         |        | ●             |               | Called when `__getitem__` cannot find the key |
| `d.move_to_end(k, [last])` |        |               | ●             | Move key `k` to the first or last position (default is last) |
| `d.__or__(other)`          | ●      | ●             | ●             | Support for `d1 | d2` to create new dict merging `d1` and `d2` (Python ≥ 3.9) |
| `d.__ior__(other)`         | ●      | ●             | ●             | Support for `d1 |= d2` to update `d1` with `d2` (Python ≥ 3.9) |
| `d.pop(k, [default])`      | ●      | ●             | ●             | Remove and return value at key `k`, or return `default` or `None` if missing |
| `d.popitem()`              | ●      | ●             | ●             | Remove and return the last inserted item as (key, value) |
| `d.__reversed__()`         | ●      | ●             | ●             | Support for `reversed(d)`—returns iterator for keys from last to first inserted |
| `d.__ror__(other)`         | ●      | ●             | ●             | Support for `other | d`—reversed union operator (Python ≥ 3.9) |
| `d.setdefault(k, [default])` | ●    | ●             | ●             | If key `k` is in `d`, return `d[k]`; else set `d[k] = default` and return it |
| `d.__setitem__(k, v)`      | ●      | ●             | ●             | Set item with key `k` to value `v` |
| `d.update(m, [**kwargs])`  | ●      | ●             | ●             | Update `d` with items from mapping or iterable of (key, value) pairs |
| `d.values()`               | ●      | ●             | ●             | Get view over values |

### Special Methods and Attributes
- **`default_factory`**: Not a method but a callable attribute set by the end user when a `defaultdict` is instantiated. It is invoked by the `__missing__` method to set missing values.
- **`move_to_end(k, [last])`**: In `OrderedDict`, this method moves the key `k` to the first or last position (default is last).
- **`popitem()`**: In `OrderedDict`, `popitem(last=False)` removes the first item inserted (FIFO). The `last` keyword argument is not supported in `dict` or `defaultdict` as recently as Python 3.10b3.

### Duck Typing Example
The way `d.update(m)` handles its first argument `m` is a prime example of duck typing: it first checks whether `m` has a `keys` method and, if it does, assumes it is a mapping. Otherwise, `update()` falls back to iterating over `m`, assuming its items are (key, value) pairs. The constructor for most Python mappings uses the logic of `update()` internally, which means they can be initialized from other mappings or from any iterable object producing (key, value) pairs.

### Subtle Method: `setdefault()`
A subtle mapping method is `setdefault()`. It avoids redundant key lookups when we need to update the value of an item in place.

Example:
```python
d = {}
value = d.setdefault('key', 'default_value')
print(d)  # Output: {'key': 'default_value'}
print(value)  # Output: 'default_value'
```

In this example, if 'key' is not already in the dictionary, it is set to 'default_value', and 'default_value' is returned. If 'key' is already in the dictionary, its value is returned without changing the dictionary.

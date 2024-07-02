# Unpacking Mappings

PEP 448—Additional Unpacking Generalizations enhanced the support of mapping unpackings in two ways since Python 3.5.

## Applying `**` to Multiple Arguments in Function Calls

We can apply `**` to more than one argument in a function call. This works when keys are all strings and unique across all arguments (because duplicate keyword arguments are forbidden):

```python
def dump(**kwargs):
    return kwargs

print(dump(**{'x': 1}, y=2, **{'z': 3}))
```

Output:
```python
{'x': 1, 'y': 2, 'z': 3}
```

### Explanation
- **Function Definition**: `def dump(**kwargs):` defines a function that accepts any number of keyword arguments and returns them as a dictionary.
- **Function Call**: `dump(**{'x': 1}, y=2, **{'z': 3})`:
  - `**{'x': 1}` unpacks the dictionary `{'x': 1}` into the function call.
  - `y=2` adds the key-value pair `'y': 2`.
  - `**{'z': 3}` unpacks the dictionary `{'z': 3}` into the function call.
- **Result**: Combines all key-value pairs into a single dictionary `{'x': 1, 'y': 2, 'z': 3}`.

## Using `**` Inside a Dict Literal

`**` can be used inside a dict literal—also multiple times:

```python
print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})
```

Output:
```python
{'a': 0, 'x': 4, 'y': 2, 'z': 3}
```

### Explanation
- **Dict Literal**: `{'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}`:
  - `**{'x': 1}` unpacks the dictionary `{'x': 1}`.
  - `'y': 2` adds the key-value pair `'y': 2`.
  - `**{'z': 3, 'x': 4}` unpacks the dictionary `{'z': 3, 'x': 4}`.
- **Duplicate Keys**: In this case, duplicate keys are allowed. Later occurrences overwrite previous ones. Thus, the value of `'x'` is `4` (from the last dictionary) instead of `1`.

## Merging Mappings with `|`

Python 3.9 supports using `|` and `|=` to merge mappings. These operators are also the set union operators.

### Creating a New Mapping with `|`

The `|` operator creates a new mapping:

```python
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
print(d1 | d2)
```

Output:
```python
{'a': 2, 'b': 4, 'c': 6}
```

### Explanation
- **Input Dictionaries**: `d1 = {'a': 1, 'b': 3}` and `d2 = {'a': 2, 'b': 4, 'c': 6}`.
- **Union Operator**: `d1 | d2` merges `d1` and `d2`:
  - `'a'` from `d2` (value `2`) overwrites `'a'` from `d1` (value `1`).
  - `'b'` from `d2` (value `4`) overwrites `'b'` from `d1` (value `3`).
  - `'c'` from `d2` (value `6`) is added to the result.
- **Result**: Creates a new dictionary `{'a': 2, 'b': 4, 'c': 6}`.

### Updating an Existing Mapping In-Place with `|=`

To update an existing mapping in place, use `|=`:

```python
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 |= d2
print(d1)
```

Output:
```python
{'a': 2, 'b': 4, 'c': 6}
```

### Explanation
- **Initial Dictionary**: `d1 = {'a': 1, 'b': 3}`.
- **Union Assignment Operator**: `d1 |= d2` merges `d2` into `d1`:
  - `'a'` from `d2` (value `2`) overwrites `'a'` from `d1` (value `1`).
  - `'b'` from `d2` (value `4`) overwrites `'b'` from `d1` (value `3`).
  - `'c'` from `d2` (value `6`) is added to `d1`.
- **Result**: Updates `d1` to `{'a': 2, 'b': 4, 'c': 6}`.

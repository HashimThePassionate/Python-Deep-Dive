### Comparing Tuple and List Methods

When using a tuple as an immutable variation of a list, it is useful to understand how similar their APIs are. Here’s a comparison of the methods available in both tuples and lists, based on the provided table.

#### Shared Methods

Both tuples and lists support the following methods:
- `s.__add__(s2)`: Concatenation
  - Example: `s + s2`
- `s.__contains__(e)`: Membership test
  - Example: `e in s`

#### List-Only Methods

Lists support additional methods that are not available for tuples, primarily because lists are mutable while tuples are not:
- `s.__iadd__(s2)`: In-place concatenation
  - Example: `s += s2`
- `s.append(e)`: Append one element after the last
  - Example: `s.append(e)`
- `s.clear()`: Delete all items
  - Example: `s.clear()`
- `s.copy()`: Shallow copy of the list
  - Example: `s.copy()`

| Method | List | Tuple | Description |
|--------|------|-------|-------------|
| `s.__add__(s2)` | ✔️ | ✔️ | Concatenation: `s + s2` |
| `s.__iadd__(s2)` | ✔️ | ❌ | In-place concatenation: `s += s2` |
| `s.append(e)` | ✔️ | ❌ | Append one element after last |
| `s.clear()` | ✔️ | ❌ | Delete all items |
| `s.__contains__(e)` | ✔️ | ✔️ | Membership test: `e in s` |
| `s.copy()` | ✔️ | ❌ | Shallow copy of the list |

#### Summary
- **Tuples**:
  - Support methods that do not alter their contents.
  - Cannot use methods that add or remove elements (`append`, `clear`, etc.).
  - Can be concatenated using `+`.
  - Support membership tests using `in`.

- **Lists**:
  - Support all the methods tuples do.
  - Additionally, support methods for in-place modification (`append`, `clear`, `copy`, etc.).


### Comparing Tuple and List Methods (Continued)

The table below lists methods and attributes found in `list` or `tuple`. It highlights which methods are available for each data type and provides a brief description of each method.

#### Methods in List and Tuple

| Method               | List | Tuple | Description                                                               |
|----------------------|------|-------|---------------------------------------------------------------------------|
| `s.count(e)`         | ✔️   | ✔️    | Count occurrences of an element                                           |
| `s.__delitem__(p)`   | ✔️   | ❌    | Remove item at position `p`                                               |
| `s.extend(it)`       | ✔️   | ❌    | Append items from iterable `it`                                           |
| `s.__getitem__(p)`   | ✔️   | ✔️    | `s[p]` — get item at position                                             |
| `s.__getnewargs__()` | ✔️   | ❌    | Support for optimized serialization with `pickle`                         |
| `s.index(e)`         | ✔️   | ✔️    | Find position of first occurrence of `e`                                  |
| `s.insert(p, e)`     | ✔️   | ❌    | Insert element `e` before the item at position `p`                        |
| `s.__iter__()`       | ✔️   | ✔️    | Get iterator                                                              |
| `s.__len__()`        | ✔️   | ✔️    | `len(s)` — number of items                                                |
| `s.__mul__(n)`       | ✔️   | ✔️    | `s * n` — repeated concatenation                                          |
| `s.__imul__(n)`      | ✔️   | ❌    | `s *= n` — in-place repeated concatenation                                |
| `s.__rmul__(n)`      | ✔️   | ✔️    | `n * s` — reversed repeated concatenation                                 |
| `s.pop([p])`         | ✔️   | ❌    | Remove and return last item or item at optional position `p`              |
| `s.remove(e)`        | ✔️   | ❌    | Remove first occurrence of element `e` by value                           |
| `s.reverse()`        | ✔️   | ❌    | Reverse the order of the items in place                                   |
| `s.__reversed__()`   | ✔️   | ❌    | Get iterator to scan items from last to first                             |
| `s.__setitem__(p, e)`| ✔️   | ❌    | `s[p] = e` — put `e` in position `p`, overwriting existing item           |
| `s.sort([key], [reverse])`| ✔️ | ❌ | Sort items in place with optional keyword arguments `key` and `reverse`   |

### Summary of Key Points:
- **Common Methods**:
  - Both `list` and `tuple` support methods that do not modify their contents, such as `count`, `__getitem__`, `index`, `__iter__`, `__len__`, `__mul__`, and `__rmul__`.
  
- **List-Only Methods**:
  - Lists have several methods for modifying their contents, including `__delitem__`, `extend`, `insert`, `pop`, `remove`, `reverse`, `__reversed__`, `__setitem__`, and `sort`.

### Explanation:
- **Tuples**:
  - Tuples are immutable, meaning they cannot be modified after creation. As such, they lack methods that add, remove, or change items.
  - Tuples support methods for accessing items, counting occurrences, finding indices, and iterating over elements.
  
- **Lists**:
  - Lists are mutable, meaning they can be changed after creation. They support a wide range of methods for modifying their contents.
  - Lists have methods for appending, inserting, removing, reversing, and sorting elements.

### Conclusion:
Understanding the differences between tuples and lists in Python can help you choose the appropriate data structure for your needs. Tuples are ideal for fixed collections of items where immutability is desired, while lists are better suited for dynamic collections that require frequent updates.
# Arrays

If a list only contains numbers, an `array.array` is a more efficient replacement. Arrays support all mutable sequence operations (including `.pop`, `.insert`, and `.extend`), as well as additional methods for fast loading and saving, such as `.frombytes` and `.tofile`.

A Python array is as lean as a C array. An array of float values does not hold full-fledged float instances, but only the packed bytes representing their machine values—similar to an array of `double` in the C language. When creating an array, you provide a type code, a letter to determine the underlying C type used to store each item in the array. For example, `b` is the type code for what C calls a signed char, an integer ranging from –128 to 127. If you create an `array('b')`, then each item will be stored in a single byte and interpreted as an integer. For large sequences of numbers, this saves a lot of memory. And Python will not let you put any number that does not match the type for the array.

## Example: Creating, Saving, and Loading a Large Array of Floats

### Creating and Saving an Array
```python
from array import array
from random import random

# Create an array of double-precision floats (typecode 'd') from a generator expression
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])  # Inspect the last number in the array

# Save the array to a binary file
with open('floats.bin', 'wb') as fp:
    floats.tofile(fp)
```

### Loading the Array
```python
# Create an empty array of doubles
floats2 = array('d')

# Read 10 million numbers from the binary file
with open('floats.bin', 'rb') as fp:
    floats2.fromfile(fp, 10**7)

print(floats2[-1])  # Inspect the last number in the array
print(floats2 == floats)  # Verify that the contents of the arrays match
```

### Explanation
1. **Import the `array` type.**
2. **Create an array of double-precision floats (typecode 'd') from any iterable object—in this case, a generator expression.**
3. **Inspect the last number in the array.**
4. **Save the array to a binary file using `tofile()`.**
5. **Create an empty array of doubles.**
6. **Read 10 million numbers from the binary file using `fromfile()`.**
7. **Inspect the last number in the array.**
8. **Verify that the contents of the arrays match.**

### Methods for Fast Loading and Saving
- **`.tofile(file_object)`:** Writes the items of the array to a binary file.
- **`.fromfile(file_object, count)`:** Reads `count` items from a binary file and appends them to the array.
- **`.frombytes(bytes_object)`:** Appends items from a byte sequence interpreted as packed machine values.

### Performance
- **Speed:** Loading 10 million double-precision floats from a binary file created with `array.tofile` takes about 0.1 seconds, which is nearly 60 times faster than reading from a text file.
- **File Size:** The binary file with 10 million doubles is 80,000,000 bytes (8 bytes per double, zero overhead), whereas the text file has 181,515,739 bytes for the same data.

## Comparison of `list` and `array.array`

| Method               | `list` | `array` | Description                                                                 |
|----------------------|--------|---------|-----------------------------------------------------------------------------|
| `s.__add__(s2)`      | ●      | ●       | `s + s2` — concatenation                                                    |
| `s.__iadd__(s2)`     | ●      | ●       | `s += s2` — in-place concatenation                                          |
| `s.append(e)`        | ●      | ●       | Append one element after the last                                           |
| `s.byteswap()`       |        | ●       | Swap bytes of all items in array for endianness conversion                  |
| `s.clear()`          | ●      |         | Delete all items                                                            |
| `s.__contains__(e)`  | ●      | ●       | `e in s`                                                                    |
| `s.copy()`           | ●      |         | Shallow copy of the list                                                    |
| `s.__copy__()`       | ●      |         | Support for `copy.copy`                                                     |
| `s.count(e)`         | ●      | ●       | Count occurrences of an element                                             |
| `s.__deepcopy__()`   | ●      |         | Optimized support for `copy.deepcopy`                                       |
| `s.__delitem__(p)`   | ●      | ●       | Remove item at position `p`                                                 |
| `s.extend(it)`       | ●      | ●       | Append items from iterable `it`                                             |
| `s.frombytes(b)`     |        | ●       | Append items from byte sequence interpreted as packed machine values        |
| `s.fromfile(f, n)`   |        | ●       | Append `n` items from binary file `f` interpreted as packed machine values  |
| `s.fromlist(l)`      |        | ●       | Append items from list; if one causes `TypeError`, none are appended        |
| `s.__getitem__(p)`   | ●      | ●       | `s[p]` — get item or slice at position                                      |
| `s.index(e)`         | ●      | ●       | Find position of the first occurrence of `e`                                |
| `s.insert(p, e)`     | ●      | ●       | Insert element `e` before the item at position `p`                          |
| `s.itemsize`         |        | ●       | Length in bytes of each array item                                          |
| `s.__iter__()`       | ●      | ●       | Get iterator                                                                |
| `s.__len__()`        | ●      | ●       | `len(s)` — number of items                                                  |
| `s.__mul__(n)`       | ●      | ●       | `s * n` — repeated concatenation                                            |
| `s.__imul__(n)`      | ●      | ●       | `s *= n` — in-place repeated concatenation                                  |
| `s.__rmul__(n)`      | ●      | ●       | `n * s` — reversed repeated concatenation                                   |
| `s.pop([p])`         | ●      | ●       | Remove and return item at position `p` (default: last)                      |
| `s.remove(e)`        | ●      | ●       | Remove first occurrence of element `e` by value                             |
| `s.reverse()`        | ●      | ●       | Reverse the order of the items in place                                     |
| `s.__reversed__()`   | ●      |         | Get iterator to scan items from last to first                               |
| `s.__setitem__(p, e)`| ●      | ●       | `s[p] = e` — put `e` in position `p`, overwriting existing item or slice    |
| `s.sort([key], [reverse])` | ● |         | Sort items in place with optional keyword arguments `key` and `reverse`     |
| `s.tobytes()`        |        | ●       | Return items as packed machine values in a bytes object                     |
| `s.tofile(f)`        |        | ●       | Save items as packed machine values to binary file `f`                      |
| `s.tolist()`         |        | ●       | Return items as numeric objects in a list                                   |
| `s.typecode`         |        | ●       | One-character string identifying the C type of the items                    |

## Notes

- **Sorting Arrays:** As of Python 3.10, the `array` type does not have an in-place sort method like `list.sort()`. To sort an array, use the built-in `sorted` function to rebuild the array:
  ```python
  a = array.array(a.typecode, sorted(a))
  ```
- **Maintaining Sorted Arrays:** To keep a sorted array sorted while adding items to it, use the `bisect.insort` function.

If you do a lot of work with arrays and don’t know about `memoryview`, you’re missing out. See the next topic for more information.
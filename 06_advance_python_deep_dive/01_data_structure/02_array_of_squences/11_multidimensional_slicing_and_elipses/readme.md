# Multidimensional Slicing and Ellipsis 

## Introduction
In Python, the `[]` operator can handle multiple indexes or slices separated by commas. This is managed by the `__getitem__` and `__setitem__` special methods, which receive the indices in `a[i, j]` as a tuple. For example, evaluating `a[i, j]` calls `a.__getitem__((i, j))`.

## Usage with NumPy
This feature is used in the external NumPy package, allowing you to fetch items of a two-dimensional `numpy.ndarray` using the syntax `a[i, j]` and obtain a two-dimensional slice with an expression like `a[m:n, k:l]`.

### Example with NumPy
Here's an example to demonstrate multidimensional slicing with NumPy:

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1, 2])  # Output: 6

# Slicing a 2D array
# This will select rows 0 and 1 (0:2) and columns 1 and 2 (1:3)
print(a[0:2, 1:3])  # Output: [[2, 3], [5, 6]]
```

### Graphical Representation
#### Original Array
Consider the following 2D NumPy array:
```
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
```

#### Slicing Explanation
The slicing `a[0:2, 1:3]` means:
- `0:2` selects rows from index 0 to 1 (up to but not including index 2).
- `1:3` selects columns from index 1 to 2 (up to but not including index 3).

Here's a step-by-step graphical representation:

1. **Original Array:**
   ```
   [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
   ```

2. **Row Selection (`0:2`):**
   ```
   Rows selected:
   [[1, 2, 3],
    [4, 5, 6]]
   ```

3. **Column Selection (`1:3`):**
   ```
   Columns selected from the selected rows:
   [[2, 3],
    [5, 6]]
   ```

#### Graphical Breakdown
```
Original Array:

    Col0 Col1 Col2
Row0  1    2    3
Row1  4    5    6
Row2  7    8    9

Step 1: Select Rows 0 to 1 (0:2):

    Col0 Col1 Col2
Row0  1    2    3
Row1  4    5    6

Step 2: Select Columns 1 to 2 (1:3):

    Col1 Col2
Row0  2    3
Row1  5    6

Final Result:
[[2, 3],
 [5, 6]]
```

By selecting the specified rows and columns, the resulting subarray is `[[2, 3], [5, 6]]`.

## Built-in Sequence Types
Except for `memoryview`, the built-in sequence types in Python are one-dimensional, so they support only one index or slice, and not a tuple of them.

## The Ellipsis (`...`)
The ellipsis (`...`) is recognized as a token by the Python parser and is an alias to the `Ellipsis` object. It can be used as an argument to functions and as part of a slice specification, as in `f(a, ..., z)` or `a[i:...]`.

### Example with NumPy and Ellipsis
NumPy uses `...` as a shortcut when slicing arrays of many dimensions. For example, if `x` is a four-dimensional array, `x[i, ...]` is a shortcut for `x[i, :, :, :,]`.

```python
x = np.random.rand(3, 4, 5, 6)
print(x[1, ...].shape)  # Output: (4, 5, 6)
```

#### Explanation of Ellipsis Example
In this example:
- `x` is a four-dimensional array with shape `(3, 4, 5, 6)`.
- `x[1, ...]` selects the second element along the first dimension and includes all elements along the remaining dimensions.
- This is equivalent to `x[1, :, :, :,]`, resulting in a three-dimensional array with shape `(4, 5, 6)`.

## Standard Library
As of this writing, there are no known uses of `Ellipsis` or multidimensional indexes and slices in the Python standard library. These features are primarily for user-defined types and extensions such as NumPy.

## Modifying Mutable Sequences
Slices can also be used to change mutable sequences in place without rebuilding them from scratch.

### Example of Modifying a List
```python
lst = [1, 2, 3, 4, 5]
lst[1:3] = [20, 30]
print(lst)  # Output: [1, 20, 30, 4, 5]
```

## Conclusion
Understanding multidimensional slicing and the use of `Ellipsis` can greatly enhance your ability to work with complex data structures, especially when using libraries like NumPy.

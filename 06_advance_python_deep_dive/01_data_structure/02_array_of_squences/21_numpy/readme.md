# NumPy

NumPy is a powerful library for advanced array and matrix operations, making Python a mainstream tool in scientific computing applications. NumPy implements multidimensional, homogeneous arrays and matrix types that hold not only numbers but also user-defined records and provides efficient element-wise operations.

## SciPy

SciPy is a library built on top of NumPy, offering many scientific computing algorithms from linear algebra, numerical calculus, and statistics. SciPy is fast and reliable because it leverages the widely used C and Fortran codebase from the Netlib Repository. SciPy combines high-level Python APIs with industrial-strength number-crunching functions optimized in C and Fortran.

## Basic NumPy Operations

### Example 2-22: Basic operations with rows and columns in a numpy.ndarray
```python
import numpy as np

# Build and inspect a numpy.ndarray with integers 0 to 11
a = np.arange(12)
print(a)  # Output: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(type(a))  # Output: <class 'numpy.ndarray'>
print(a.shape)  # Output: (12,)

# Change the shape of the array, adding one dimension
a.shape = 3, 4
print(a)
# Output:
# array([[ 0, 1, 2, 3],
#        [ 4, 5, 6, 7],
#        [ 8, 9, 10, 11]])

# Get row at index 2
print(a[2])  # Output: array([ 8, 9, 10, 11])

# Get element at index 2, 1
print(a[2, 1])  # Output: 9

# Get column at index 1
print(a[:, 1])  # Output: array([1, 5, 9])

# Create a new array by transposing (swapping columns with rows)
print(a.transpose())
# Output:
# array([[ 0, 4, 8],
#        [ 1, 5, 9],
#        [ 2, 6, 10],
#        [ 3, 7, 11]])
```

### Explanation
1. **Import NumPy:** Conventionally, NumPy is imported as `np`.
2. **Create an Array:** `np.arange(12)` creates a 1D array with integers from 0 to 11.
3. **Inspect the Array:** Use `type()` and `shape` attributes to inspect the array's type and dimensions.
4. **Reshape the Array:** Change the array's shape to 3 rows and 4 columns.
5. **Access Rows and Columns:** Use indexing to access specific rows, columns, and elements.
6. **Transpose the Array:** Use the `transpose()` method to swap rows and columns.

## High-Level Operations

NumPy also supports high-level operations for loading, saving, and operating on all elements of a `numpy.ndarray`.

```python
import numpy as np

# Load 10 million floating-point numbers from a text file
floats = np.loadtxt('floats-10M-lines.txt')
print(floats[-3:])  # Output: array([ 3016362.69195522, 535281.10514262, 4566560.44373946])

# Multiply every element in the floats array by 0.5
floats *= 0.5
print(floats[-3:])  # Output: array([ 1508181.34597761, 267640.55257131, 2283280.22186973])

# Divide every element by 3; the elapsed time for 10 million floats is less than 40 milliseconds
from time import perf_counter as pc
t0 = pc(); floats /= 3; print(pc() - t0)  # Example Output: 0.03690556302899495

# Save the array in a .npy binary file
np.save('floats-10M', floats)

# Load the data as a memory-mapped file into another array
floats2 = np.load('floats-10M.npy', 'r+')
floats2 *= 6
print(floats2[-3:])  # Output: memmap([ 3016362.69195522, 535281.10514262, 4566560.44373946])
```

### Explanation
1. **Load Data:** Use `numpy.loadtxt()` to load 10 million floating-point numbers from a text file.
2. **Inspect Data:** Use slicing notation to inspect the last three numbers.
3. **Element-wise Operations:** Multiply and divide all elements in the array efficiently.
4. **Performance Measurement:** Use `perf_counter` to measure the time taken for operations.
5. **Save and Load Data:** Save the array to a binary file with `numpy.save()` and load it back with `numpy.load()`.
6. **Memory-Mapped Files:** Load the data as a memory-mapped file for efficient processing of large datasets.

## Advanced Libraries Built on NumPy

- **Pandas:** Implements efficient array types that can hold non-numeric data and provides import/export functions for many formats (e.g., .csv, .xls, SQL dumps, HDF5).
- **scikit-learn:** A widely used Machine Learning toolset.
- **Dask:** Supports parallelizing NumPy, Pandas, and scikit-learn processing across clusters of machines.

These packages leverage NumPy and SciPy functions, which are implemented in C or C++ and can utilize all CPU cores by releasing Python’s GIL (Global Interpreter Lock).

## Conclusion

NumPy and SciPy are formidable libraries, providing the foundation for many other powerful tools in the scientific and data science communities. While this book does not delve deeply into these libraries, no overview of Python sequences would be complete without at least a quick look at NumPy arrays.

Having looked at flat sequences—standard arrays and NumPy arrays—we now turn to a completely different set of replacements for the plain old list: queues.
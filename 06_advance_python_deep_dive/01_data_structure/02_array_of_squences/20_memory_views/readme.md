# Memory Views

The built-in `memoryview` class is a shared-memory sequence type that allows you to handle slices of arrays without copying bytes. It was inspired by the NumPy library. A `memoryview` enables you to share memory between data structures (like PIL images, SQLite databases, NumPy arrays, etc.) without first copying. This is crucial for handling large datasets efficiently.

## Key Features
- **Shared Memory:** `memoryview` allows sharing memory between different data structures without copying.
- **Casting:** The `memoryview.cast` method lets you change the way multiple bytes are read or written as units without moving bits around.

## Example: Creating Alternate Views on the Same Array

### Example 2-20: Handling 6 bytes of memory as 1×6, 2×3, and 3×2 views
```python
from array import array

# Build array of 6 bytes (typecode 'B')
octets = array('B', range(6))

# Build memoryview from that array
m1 = memoryview(octets)
print(m1.tolist())  # Output: [0, 1, 2, 3, 4, 5]

# Build new memoryview from that previous one, but with 2 rows and 3 columns
m2 = m1.cast('B', [2, 3])
print(m2.tolist())  # Output: [[0, 1, 2], [3, 4, 5]]

# Yet another memoryview, now with 3 rows and 2 columns
m3 = m1.cast('B', [3, 2])
print(m3.tolist())  # Output: [[0, 1], [2, 3], [4, 5]]

# Overwrite byte in m2 at row 1, column 1 with 22
m2[1, 1] = 22

# Overwrite byte in m3 at row 1, column 1 with 33
m3[1, 1] = 33

# Display original array, proving that the memory was shared among octets, m1, m2, and m3
print(octets)  # Output: array('B', [0, 1, 2, 33, 22, 5])
```
**Type Code**
```python
## Type code

| Type code | C Type              | Python Type 	    | Minimum size in bytes | Notes          |
|-----------|---------------------|-----------------	|-----------------------|----------------|
| 'b'       | signed char         | int        	    	| 1                     |                |
| 'B'       | unsigned char       | int         	    | 1                     |                |
| 'u'       | wchar_t             | Unicode character 	| 2                	    | (1)            |
| 'h'       | signed short        | int        		    | 2                     |                |
| 'H'       | unsigned short      | int         	    | 2                     |                |
| 'i'       | signed int          | int         	    | 2                     |                |
| 'I'       | unsigned int        | int         	    | 2                     |                |
| 'l'       | signed long         | int         	    | 4                     |                |
| 'L'       | unsigned long       | int             	| 4                     |                |
| 'q'       | signed long long    | int          	    | 8                     |                |
| 'Q'       | unsigned long long  | int         	    | 8                     |                |
| 'f'       | float               | float       	    | 4                     |                |
| 'd'       | double              | float       	    | 8                     |                |
```

### Explanation
1. **Build array of 6 bytes (typecode 'B').**
2. **Create a `memoryview` from that array and export it as a list.**
3. **Create new `memoryview` from the previous one with 2 rows and 3 columns.**
4. **Create another `memoryview` with 3 rows and 2 columns.**
5. **Overwrite bytes in `m2` and `m3`.**
6. **Display the original array to show shared memory.**

## Example: Changing a Single Byte of an Item in an Array of 16-bit Integers

### Example 2-21: Changing the value of a 16-bit integer array item by modifying one of its bytes
```python
from array import array

# Build array of 5 16-bit signed integers (typecode 'h')
numbers = array('h', [-2, -1, 0, 1, 2])

# Create a memoryview from the array
memv = memoryview(numbers)
print(len(memv))  # Output: 5
print(memv[0])    # Output: -2

# Create memv_oct by casting the elements of memv to bytes (typecode 'B')
memv_oct = memv.cast('B')
print(memv_oct.tolist())  # Output: [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

# Assign value 4 to byte offset 5
memv_oct[5] = 4

# Note the change to numbers
print(numbers)  # Output: array('h', [-2, -1, 1024, 1, 2])
```

### Explanation
1. **Build an array of 5 16-bit signed integers:** `array('h', [-2, -1, 0, 1, 2])` creates an array with typecode 'h' for 16-bit signed integers.
2. **Create a `memoryview` from the array:** `memv = memoryview(numbers)` creates a memoryview object from the `numbers` array.
3. **Inspect the memoryview:** `len(memv)` gives the length (5), and `memv[0]` returns the first item (-2).
4. **Cast the memoryview to bytes:** `memv_oct = memv.cast('B')` casts the memoryview to bytes (typecode 'B').
5. **Inspect the byte representation:** `memv_oct.tolist()` outputs `[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]`.
6. **Modify a byte:** `memv_oct[5] = 4` changes the value at byte offset 5.
7. **Observe the change in the original array:** `print(numbers)` shows that the array has been modified to `array('h', [-2, -1, 1024, 1, 2])`. The value 4 in the most significant byte of the third element results in 1024.


## Notes
- **Memory Corruption:** `memoryview` can be used to corrupt data if not used carefully.
- **Advanced Numeric Processing:** For advanced numeric processing in arrays, consider using the NumPy libraries.

## Further Reading
- **NumPy:** The next topic covers the NumPy library, which provides advanced mathematical functions and operations on arrays.
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
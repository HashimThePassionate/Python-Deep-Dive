import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1, 2])  # Output: 6

# Slicing a 2D array
# This will select rows 0 and 1 (0:2) and columns 1 and 2 (1:3)
print(a[0:2, 1:3])  # Output: [[2, 3], [5, 6]]

x = np.random.rand(3, 4, 5, 6)
print(x[0, ...].shape)  # Output: (4, 5, 6)

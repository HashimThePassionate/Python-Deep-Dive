from array import array

# Build array of 5 16-bit signed integers (typecode 'h')
numbers = array('h', [-2, -1, 0, 1, 2])
print('Numbers')
print(numbers)
# Create a memoryview from the array
print(numbers)
memv = memoryview(numbers)
print(len(memv))  # Output: 5
print(memv[0])    # Output: -2
print('Memv')
print(memv)

# Create memv_oct by casting the elements of memv to bytes (typecode 'B')
memv_oct = memv.cast('B')
print('Memv_oct')
print(memv_oct)
print(memv_oct.tolist())  # Output: [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

# Assign value 4 to byte offset 5
memv_oct[5] = 4

# Note the change to numbers
print(numbers)  # Output: array('h', [-2, -1, 1024, 1, 2])
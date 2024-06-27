from collections import deque

# Create a deque with a fixed maximum length
dq = deque(range(10), maxlen=10)
print(dq)  # Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# Rotate the deque 3 steps to the right
dq.rotate(3)
print(dq)  # Output: deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

# Rotate the deque 4 steps to the left
dq.rotate(-4)
print(dq)  # Output: deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

# Add an element to the left end
dq.appendleft(-1)
print(dq)  # Output: deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# Add multiple elements to the right end
dq.extend([11, 22, 33])
print(dq)  # Output: deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)

# Add multiple elements to the left end
dq.extendleft([10, 20, 30, 40])
print(dq)  # Output: deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
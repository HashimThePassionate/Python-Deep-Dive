import array
from collections import deque
# Create an array of double-precision floating-point numbers
arr = array.array('d', [1.0, 2.0, 3.5, 4.75])
print(arr)  # Output: array('d', [1.0, 2.0, 3.5, 4.75])
# Create a deque
dq = deque([1, 2, 3, 4])
dq.appendleft(0)
dq.append(5)
print(dq)  # Output: deque([0, 1, 2, 3, 4, 5])

dq.popleft()
dq.pop()
print(dq)  # Output: deque([1, 2, 3, 4])


# Create a set
my_set = {1, 2, 3, 4, 5}

# Check membership
print(3 in my_set)  # Output: True

# Add and remove elements
my_set.add(6)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}

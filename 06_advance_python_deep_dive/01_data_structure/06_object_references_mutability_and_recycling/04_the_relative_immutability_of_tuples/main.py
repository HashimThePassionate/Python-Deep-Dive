# Define two tuples containing a mutable object (a list)
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

# t1 and t2 initially compare equal
print(t1 == t2)  # Output: True

# Inspect the identity of the list at t1[-1]
print(id(t1[-1]),t1[-1])  # Example output: 4302515784

# Modify the list in place
t1[-1].append(99)

# Check the value of t1
print(t1)  # Output: (1, 2, [30, 40, 99])

# Inspect the identity of the list at t1[-1] again
print(id(t1[-1]),t1[-1])  # Example output: 4302515784 (same as before)

# t1 and t2 are now different
print(t1 == t2)  # Output: False


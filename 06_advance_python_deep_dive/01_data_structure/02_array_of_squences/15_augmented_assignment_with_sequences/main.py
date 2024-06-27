l = [1, 2, 3]
print(id(l))  # Output: ID of the initial list

l *= 2
print(l)  # Output: [1, 2, 3, 1, 2, 3]
print(id(l))  # Output: Same ID as initial list


t = (1, 2, 3)
print(id(t))  # Output: ID of the initial tuple

t *= 2
print(t)  # Output: (1, 2, 3, 1, 2, 3)
print(id(t))  # Output: Different ID from initial tuple

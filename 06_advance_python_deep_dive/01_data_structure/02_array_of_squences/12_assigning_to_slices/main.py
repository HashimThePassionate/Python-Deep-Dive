l = list(range(10))
print(l)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l[2:5] = [20, 30]
print(l)  # Output: [0, 1, 20, 30, 5, 6, 7, 8, 9]

del l[5:7]
print(l)  # Output: [0, 1, 20, 30, 5, 8, 9]

l[3::2] = [11, 22]
print(l)  # Output: [0, 1, 20, 11, 5, 22, 9]

# try:
#     l[2:5] = 100
# except TypeError as e:
#     print(e)  # Output: can only assign an iterable

l[2:5] = [100]
print(l)  # Output: [0, 1, 100, 22, 9]
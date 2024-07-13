def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))  # Output: 3
print(x, y)     # Output: (1, 2)

a = [1, 2]
b = [3, 4]
print(f(a, b))  # Output: [1, 2, 3, 4]
print(a, b)     # Output: ([1, 2, 3, 4], [3, 4])

t = (10, 20)
u = (30, 40)
print(f(t, u))  # Output: (10, 20, 30, 40)
print(t, u)     # Output: ((10, 20), (30, 40))
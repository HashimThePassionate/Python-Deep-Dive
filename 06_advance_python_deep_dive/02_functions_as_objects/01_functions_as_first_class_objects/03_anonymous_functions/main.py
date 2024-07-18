fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))

# Original lambda function
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2 if x % 2 == 0 else x**3, numbers)))

def process_number(x):
    if x % 2 == 0:
        return x**2
    else:
        return x**3

print(list(map(process_number, numbers)))
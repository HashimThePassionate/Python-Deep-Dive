alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)


alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('points', 'No point value assigned.'))


user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")


favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust'}
for name in favorite_languages.keys():
    print(name.title())


print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

user_info = {'name': 'Alice', 'age': 30}

# Unpacking the dictionary into the function call
greet_user(**user_info)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)

original = {'x': 1, 'y': 2}
new_dict = {**original, 'z': 3}
print(new_dict)

numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print(squares)

cubes = {num: num ** 3 for num in numbers if num > 2}
print(cubes)



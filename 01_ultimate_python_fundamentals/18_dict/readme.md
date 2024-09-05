# 🐍 Python Dictionaries 

## 📚 What is a Dictionary?

A **dictionary** in Python is a collection of **key-value pairs**. Each key is connected to a value, and you can use a key to access the value associated with that key.

### 🔑 Key Points About Dictionaries:
- A dictionary is defined using curly braces `{}`.
- **Keys** must be unique and can be of any **immutable** type (like strings, numbers, or tuples).
- **Values** can be of any type (including other dictionaries).

Think of a dictionary like a real-life dictionary where you have a word (key) and its meaning (value).

### 🔍 A Simple Dictionary Example

Consider a game featuring aliens that can have different colors and point values. This simple dictionary stores information about a particular alien:

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

**Output:**
```
green
5
```

Explanation: The dictionary `alien_0` stores the alien’s color and point value. The `print` statements access and display the information stored in the dictionary.

---

## 🛠️ Working with Dictionaries

### 🔧 Adding New Key-Value Pairs

Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. To add a new key-value pair, you use the name of the dictionary followed by the new key in square brackets and the new value.

```python
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

**Output:**
```
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

Explanation: We added two new key-value pairs to `alien_0`: `'x_position': 0` and `'y_position': 25`. The updated dictionary is printed.

### 🖊️ Modifying Values in a Dictionary

To modify a value in a dictionary, specify the dictionary name followed by the key in square brackets and then the new value you want associated with that key.

```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
```

**Output:**
```
The alien is green.
The alien is now yellow.
```

Explanation: The value associated with the key `'color'` is modified from `'green'` to `'yellow'`.

### ❌ Removing Key-Value Pairs

To remove a key-value pair, use the `del` statement with the dictionary name and the key to be removed.

```python
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)
```

**Output:**
```
{'color': 'green'}
```

Explanation: The `del` statement removes the key `'points'` and its value from `alien_0`.

### 🔍 Using `get()` to Access Values

The `get()` method is useful when you want to access a key's value without risking a KeyError if the key does not exist.

```python
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('points', 'No point value assigned.'))
```

**Output:**
```
No point value assigned.
```

Explanation: The `get()` method checks for the key `'points'`. If it doesn't exist, it returns the default message `'No point value assigned.'`.

---

## 🔄 Looping Through a Dictionary

### 🔑 Looping Through All Key-Value Pairs

You can loop through all key-value pairs using the `.items()` method:

```python
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
```

**Output:**
```
Key: username
Value: efermi
Key: first
Value: enrico
Key: last
Value: fermi
```

Explanation: The loop goes through each key-value pair in `user_0`, printing both the key and its associated value.

### 🔑 Looping Through All Keys

To loop through all keys in a dictionary, use the `.keys()` method:

```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust'}
for name in favorite_languages.keys():
    print(name.title())
```

**Output:**
```
Jen
Sarah
Edward
```

Explanation: The loop iterates through all the keys in the dictionary `favorite_languages` and prints them in title case.

### 🔑 Looping Through All Values

To loop through all values in a dictionary, use the `.values()` method:

```python
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

**Output:**
```
The following languages have been mentioned:
Python
C
Rust
```

Explanation: The loop iterates through all the values in the dictionary `favorite_languages` and prints them.

### 🔄 Using `sorted()` to Loop in Order

To loop through keys in a specific order, use the `sorted()` function:

```python
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

**Output:**
```
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

Explanation: The `sorted()` function sorts the keys in `favorite_languages` alphabetically before looping through them.

---

## 🛠️ Dictionary Unpacking in Python

### 🔍 What is Dictionary Unpacking?

**Dictionary unpacking** allows you to extract key-value pairs from a dictionary and assign them to variables. This feature makes the code more readable and allows for more concise variable assignments.

#### 🎯 Example: Function Call with Unpacked Dictionary

```python
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

user_info = {'name': 'Alice', 'age': 30}

# Unpacking the dictionary into the function call
greet_user(**user_info)
```

**Output:**
```
Hello, Alice! You are 30 years old.
```

Explanation: The `**` operator unpacks the dictionary `user_info` into keyword arguments for the function `greet_user()`.

### 🛠️ Merging Dictionaries Using `**`

You can also use dictionary unpacking to merge multiple dictionaries into one:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)
```

**Output:**
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

Explanation: The `**` operator merges `dict1` and `dict2` into a single dictionary.

### 🚀 Example: Creating New Dictionaries with Modified Values

```python
original = {'x': 1, 'y': 2}
new_dict = {**original, 'z': 3}
print(new_dict)
```

**Output:**
```
{'x': 1, 'y': 2, 'z': 3}
```

Explanation: The new dictionary `new_dict` is created by unpacking `original` and adding a new key-value pair `'z': 3`.

---

## 🌟 Dictionary Comprehensions

### 🔍 What are Dictionary Comprehensions?

**Dictionary comprehensions** provide a concise way to create dictionaries. They are similar to list comprehensions but allow you to generate key-value pairs for dictionaries in a readable, single-line format.

### 📚 Basic Syntax of Dictionary Comprehensions

```python
{key_expression: value_expression for item in iterable}
```

### 🛠️ Example: Creating a Dictionary from a List

```python
numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print(squares)
```

**Output:**
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Explanation: The dictionary comprehension iterates over `numbers` and creates key-value pairs where the key is the number and the value is its square.

### 🚀 Example: Filtering with Dictionary Comprehensions

```python
cubes = {num: num ** 3 for num in numbers if num > 2}
print(cubes)
```

**Output:**
```
{3: 27, 4: 64, 5: 125}
```

Explanation: The dictionary comprehension includes an `if` condition to filter numbers greater than 2.

### 🛠️ Example: Inverting a Dictionary

```python
original_dict = {'a': 1, 'b': 2, 'c

': 3}
inverted_dict = {v: k for k, v in original_dict.items()}
print(inverted_dict)
```

**Output:**
```
{1: 'a', 2: 'b', 3: 'c'}
```

Explanation: The comprehension iterates over `original_dict.items()` and creates an inverted dictionary where keys and values are swapped.

### 📖 Combining Multiple Dictionaries

```python
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

person_info = {key: value for key, value in zip(keys, values)}
print(person_info)
```

**Output:**
```
{'name': 'Alice', 'age': 30, 'city': 'New York'}
```

Explanation: The `zip()` function pairs the `keys` and `values` lists, and the comprehension creates a dictionary from them.


## Conclusion

Python dictionaries are incredibly versatile, and with the power of **dictionary unpacking** and **dictionary comprehensions**, they become even more powerful and expressive. 🚀 Practice these concepts, experiment with different methods, and you'll master Python dictionaries in no time!
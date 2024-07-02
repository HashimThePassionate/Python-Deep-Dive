my_dict = {'a': 1, 'b': 2, 'c': 3}

# Accessing an existing key
print(my_dict['a'])  # Output: 1

# Accessing a non-existing key
print(my_dict['d'])  # Raises KeyError: 'd'


my_dict = {'a': 1, 'b': 2, 'c': 3}

# Accessing an existing key
print(my_dict.get('a', 0))  # Output: 1

# Accessing a non-existing key with a default value
print(my_dict.get('d', 0))  # Output: 0



# List of words
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

# Create an empty dictionary to store word counts
word_counts = {}

for word in words:
    # Use dict.get() to handle missing keys
    count = word_counts.get(word, 0)
    count += 1
    word_counts[word] = count

# Display the word counts
print(word_counts)




# List of words
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

# Create an empty dictionary to store word counts
word_counts = {}

for word in words:
    # Use dict.setdefault() to handle missing keys
    word_counts.setdefault(word, 0)
    word_counts[word] += 1

# Display the word counts
print(word_counts)
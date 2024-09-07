# Solutions for Dictionary Challenges

## 1. 🌟 Build a Custom User Profile

### Problem Statement
Create a function that accepts a dictionary of user data and returns a formatted user profile using unpacking.

### Solution

```python
def create_user_profile(user_data):
    # Unpack user data to format a profile string
    profile = f"👤 User Profile:\n"
    profile += f"Name: {user_data.get('name', 'N/A')}\n"
    profile += f"Age: {user_data.get('age', 'N/A')}\n"
    profile += f"Location: {user_data.get('location', 'N/A')}\n"
    profile += f"Profession: {user_data.get('profession', 'N/A')}\n"
    return profile

# Example Usage
user_info = {'name': 'Alice', 'age': 30, 'location': 'New York', 'profession': 'Engineer'}
print(create_user_profile(user_info))
```

**Output:**
```
👤 User Profile:
Name: Alice
Age: 30
Location: New York
Profession: Engineer
```

### Explanation
- The function `create_user_profile` uses dictionary unpacking (`**user_data`) to extract values from the dictionary and format them into a user profile string.
- The `get()` method is used to handle missing keys gracefully, returning `'N/A'` if a key is not present. 

---

## 2. 🌈 Combine and Filter Dictionaries

### Problem Statement
Write a program that merges two dictionaries and filters out key-value pairs based on a specific condition.

### Solution

```python
def merge_and_filter(dict1, dict2, threshold):
    # Merge dictionaries using dictionary unpacking
    combined_dict = {**dict1, **dict2}

    # Filter out items where the value is below the threshold
    filtered_dict = {k: v for k, v in combined_dict.items() if v >= threshold}
    return filtered_dict

# Example Usage
dict1 = {'a': 5, 'b': 8, 'c': 3}
dict2 = {'b': 6, 'd': 10, 'e': 2}
print(merge_and_filter(dict1, dict2, 5))
```

**Output:**
```
{'a': 5, 'b': 6, 'd': 10}
```

### Explanation
- We merge two dictionaries `dict1` and `dict2` using dictionary unpacking (`{**dict1, **dict2}`).
- We then use a dictionary comprehension to filter out key-value pairs where the value is less than the specified `threshold`.

---

## 3. 📊 Create a Frequency Dictionary

### Problem Statement
Use dictionary comprehensions to count the frequency of each word in a given sentence.

### Solution

```python
def word_frequency(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Use dictionary comprehension to count frequencies
    frequency_dict = {word: words.count(word) for word in set(words)}
    return frequency_dict

# Example Usage
sentence = "hello world hello everyone in this beautiful world"
print(word_frequency(sentence))
```

**Output:**
```
{'everyone': 1, 'in': 1, 'this': 1, 'world': 2, 'hello': 2, 'beautiful': 1}
```

### Explanation
- The function `word_frequency` splits the sentence into words and then uses a dictionary comprehension to count the occurrences of each unique word.
- `set(words)` is used to ensure we only loop over unique words, making the counting more efficient.

---

## 4. 🔄 Nested Dictionary Manipulation

### Problem Statement
Use dictionary comprehensions to flatten a nested dictionary structure.

### Solution

```python
def flatten_nested_dict(nested_dict):
    # Use a dictionary comprehension to flatten the dictionary
    flat_dict = {f"{outer_key}_{inner_key}": inner_value 
                 for outer_key, inner_dict in nested_dict.items()
                 for inner_key, inner_value in inner_dict.items()}
    return flat_dict

# Example Usage
nested_dict = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25},
    'person3': {'name': 'Charlie', 'age': 35}
}
print(flatten_nested_dict(nested_dict))
```

**Output:**
```
{'person1_name': 'Alice', 'person1_age': 30, 'person2_name': 'Bob', 'person2_age': 25, 'person3_name': 'Charlie', 'person3_age': 35}
```

### Explanation
- The function `flatten_nested_dict` uses a nested dictionary comprehension to flatten the structure.
- Each key in the flattened dictionary is a combination of the outer and inner keys (`outer_key_inner_key`).

---

## 5. ⚙️ Advanced Dictionary Unpacking

### Problem Statement
Create a function that merges multiple dictionaries using dictionary unpacking and handles conflicting keys by summing the values.

### Solution

```python
def merge_and_sum_dicts(*dicts):
    # Initialize an empty dictionary to store the result
    merged_dict = {}

    # Loop through each dictionary
    for d in dicts:
        # Use dictionary unpacking to merge and sum values
        for key, value in d.items():
            if key in merged_dict:
                merged_dict[key] += value  # Sum the values for conflicting keys
            else:
                merged_dict[key] = value
    return merged_dict

# Example Usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 2, 'b': 3, 'd': 4}
dict3 = {'a': 3, 'e': 5}
print(merge_and_sum_dicts(dict1, dict2, dict3))
```

**Output:**
```
{'a': 6, 'b': 5, 'c': 3, 'd': 4, 'e': 5}
```

### Explanation
- The function `merge_and_sum_dicts` takes multiple dictionaries as arguments (`*dicts`).
- It iterates through each dictionary and each key-value pair, adding values if the key already exists or creating new entries otherwise.

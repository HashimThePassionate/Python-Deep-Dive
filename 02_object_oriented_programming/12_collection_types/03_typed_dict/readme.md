# 🗂️ Leveraging `TypedDict` in Python 

Welcome to this in-depth guide on **`TypedDict`** in Python! 🎉 This guide covers how to use `TypedDict` for handling structured data in dictionaries, ensuring type safety, improving readability, and simplifying the management of complex data structures. Let’s get started! 🚀

## 📚 Table of Contents

- [🗂️ Leveraging `TypedDict` in Python](#️-leveraging-typeddict-in-python)
  - [📚 Table of Contents](#-table-of-contents)
  - [📖 Introduction](#-introduction)
  - [🛠️ Understanding `TypedDict`](#️-understanding-typeddict)
  - [🔍 Real-World Example: User Profile Management System 👤](#-real-world-example-user-profile-management-system-)
    - [🤔 The Problem Statement](#-the-problem-statement)
    - [🛠️ Implementing `TypedDict`](#️-implementing-typeddict)
    - [Enhanced Type Safety with Optional Fields 🌟](#enhanced-type-safety-with-optional-fields-)
  - [⚠️ Important Considerations](#️-important-considerations)
  - [🏆 Best Practices](#-best-practices)
  - [🧩 Complete Code Example with `mypy` Check](#-complete-code-example-with-mypy-check)
  - [](#)
  - [🌈 Additional Resources](#-additional-resources)

## 📖 Introduction

Dictionaries in Python are highly flexible, enabling you to store key-value pairs and easily access data. However, as data structures grow in complexity, it becomes challenging to enforce consistent types and data layouts across different parts of your code. This is where **`TypedDict`** comes in, offering a powerful way to define dictionary structures with specific key-value types, adding clarity, safety, and predictability. 🌟

`TypedDict` is part of Python’s `typing` module, and it lets you define the required structure of a dictionary by specifying types for each key. This improves code readability, enforces static type checking, and ensures consistent data formats. 🛡️

## 🛠️ Understanding `TypedDict`

A **`TypedDict`** allows you to define the expected keys and associated value types within a dictionary, creating a schema that acts as a contract for data shape and types.

**Basic Syntax Example:**

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str
```

**Explanation:**

- The `Person` `TypedDict` specifies a dictionary structure where:
  - `name` is a `str`.
  - `age` is an `int`.
  - `email` is a `str`.

This allows any dictionary annotated with `Person` to be statically checked, ensuring it matches the defined types and structure, improving type safety.

## 🔍 Real-World Example: User Profile Management System 👤

Let’s look at a **User Profile Management System** to see how `TypedDict` can ensure consistency in handling user data. Here, we’ll use `TypedDict` to define a structured schema for user profiles and updates, making sure that data adheres to the specified types across different functions.

### 🤔 The Problem Statement

Imagine you’re building a user profile system where each profile consists of details like username, email, age, and user preferences. Profiles are represented as dictionaries, and without type annotations, it’s easy to introduce issues such as missing keys, incorrect data types, or inconsistent data structures.

**Challenges:**

1. **Data Structure Consistency**: Profiles may differ in structure and type, leading to potential issues.
2. **Type Safety**: Without type-checking, errors like assigning a string to an integer field can occur.
3. **Scalability**: As the profile structure grows, it’s harder to enforce consistency without a clear schema.

**Problematic Code Without `TypedDict`:**

```python
def update_user_profile(profile: dict, updates: dict) -> dict:
    profile.update(updates)
    return profile

user_profile = {
    "username": "MuhammadHashim",
    "email": "hashim@example.com",
    "age": 24,
    "preferences": {"theme": "dark", "notifications": True}
}

updated_profile = update_user_profile(user_profile, {"age": "twenty-five"})  # Potential issue!
```

**Issues:**

- The `age` field is updated with a string instead of an integer, which can cause runtime errors.
- There’s no way to enforce that `profile` and `updates` have the expected structure or types.

### 🛠️ Implementing `TypedDict`

With `TypedDict`, we can explicitly define the structure of user profiles and updates, ensuring consistency and reducing bugs.

**Step 1: Define `TypedDict` Classes for Profile Structure and Updates**

```python
from typing import TypedDict, Optional, Union

class Preferences(TypedDict):
    theme: str
    notifications: bool

class UserProfile(TypedDict):
    username: str
    email: str
    age: int
    preferences: Preferences

class ProfileUpdates(TypedDict, total=False):
    username: Optional[str]
    email: Optional[str]
    age: Optional[int]  # Ensure `age` is expected to be an int
    preferences: Optional[Preferences]
```

**Explanation of TypedDict Classes:**

- **`Preferences`** defines user preferences:
  - `theme`: A `str` indicating the theme.
  - `notifications`: A `bool` indicating whether notifications are enabled.
  
- **`UserProfile`** defines the main profile structure:
  - `username`: A `str` for the unique identifier.
  - `email`: A `str` for the user’s email.
  - `age`: An `int` representing the user’s age.
  - `preferences`: A nested `Preferences` `TypedDict`.
  
- **`ProfileUpdates`** represents updates to the profile:
  - Each field is marked as `Optional`, meaning it may or may not be present in updates.
  - `total=False` allows fields to be optional, making it easier to handle partial updates.

**Step 2: Update Profile with Typed Dictionaries**

```python
def update_user_profile(profile: UserProfile, updates: ProfileUpdates) -> UserProfile:
    for key, value in updates.items():
        if key in profile:
            profile[key] = value
        else:
            raise KeyError(f"Invalid key: {key}")
    return profile
```

**Functionality Explanation:**

- **Type Safety**: The function enforces a `UserProfile` structure, ensuring consistency.
- **Key Validation**: If an update contains an invalid key, an error is raised.
- **Type Consistency**: By using `UserProfile` and `ProfileUpdates`, the code adheres to defined types.

### Enhanced Type Safety with Optional Fields 🌟

With `ProfileUpdates` as an optional `TypedDict`, we allow partial updates to profiles while still enforcing type safety. Here’s how it works:

**Example Usage and mypy Check:**

```python
# Define a correct user profile
user_profile: UserProfile = {
    "username": "MuhammadHashim",
    "email": "hashim@example.com",
    "age": 24,
    "preferences": {"theme": "dark", "notifications": True}
}

# Define updates with an incorrect type for `age`
updates: ProfileUpdates = {"age": "twenty-five", "preferences": {"theme": "light", "notifications": False}}

# Apply updates (mypy will flag this as an error due to incorrect type for `age`)
updated_profile = update_user_profile(user_profile, updates)
print(updated_profile)
```

**Type Checking Output with `mypy`:**

Run `mypy` on this script to see how static type checking prevents type mismatches:

```bash
mypy main.py
```

**Error from `mypy`:**

```
error: Incompatible types in assignment (expression has type "str", TypedDict item "age" has type "int")
```

`mypy` correctly identifies that `age` is expected to be an integer, highlighting a potential issue before runtime. This helps prevent bugs related to inconsistent types and provides a robust way to handle structured data.

## ⚠️ Important Considerations

1. **No Runtime Enforcement**: `TypedDict` is only for type-checking and doesn’t enforce constraints at runtime.
   
2. **Nested Structures**: Use `TypedDict` for relatively flat structures. For deeply nested or more complex structures, consider using data classes.
  
3. **Optional Fields**: Use optional fields carefully to keep `TypedDict` definitions clear.

4. **Type Checkers**: Ensure you’re using a static type-checking tool, like `mypy`, to get the full benefit of `TypedDict`.

## 🏆 Best Practices

1. **Define Clear `TypedDict` Structures**: Use `TypedDict` to define dictionary structures with type safety, ensuring consistency across the code.

2. **Type Aliases for Reusability**: Use aliases for commonly used `TypedDict` structures to promote code readability.

3. **Integrate Static Type Checkers**: Regularly use `mypy` to catch type inconsistencies.

   ```bash
   mypy main.py
   ```

4. **Combine with Data Classes for Complex Logic**: Use data classes if you need complex behaviors or data transformations.


## 🧩 Complete Code Example with `mypy` Check

Here’s the final code, incorporating `TypedDict`, type-checking, and error handling.

```python
from typing import TypedDict, Optional

class Preferences(TypedDict):
    theme: str
    notifications: bool

class UserProfile(TypedDict):
    username: str
    email: str
    age: int
    preferences: Preferences

class ProfileUpdates(TypedDict, total=False):
    username: Optional[str]
    email: Optional[str]
    age: Optional[int]
    preferences: Optional[Preferences]

def update_user_profile(profile: UserProfile, updates: ProfileUpdates) -> UserProfile:
    for key, value in updates.items():
        if key in profile:
            profile[key] = value
        else:
            raise KeyError(f"Invalid key: {key}")
    return profile

# Correct user profile
user_profile: UserProfile = {
    "username": "MuhammadHashim",
    "email": "hashim@example.com",
    "age": 24,
    "preferences": {"theme": "dark", "notifications": True}
}

# Incorrect update with a string for `age`
updates: ProfileUpdates = {"age": "twenty-five", "preferences": {"theme": "light", "notifications": False}}

# Type checking with `mypy` will show an error for the incorrect type
updated_profile = update_user_profile(user_profile, updates)
print(updated_profile)
```
##

 🎯 Conclusion

`TypedDict` in Python 3.12 is a powerful tool for ensuring type safety and consistency in dictionaries with diverse key-value types. By defining specific types for each key, you make your code clearer, safer, and easier to maintain.

In our **User Profile Management System** example, `TypedDict` transformed a potentially error-prone and ambiguous dictionary structure into a well-defined, type-safe system. Embrace `TypedDict` for structured, reliable data handling in your Python projects! 😊🚀

## 🌈 Additional Resources

- [Python Official Documentation on `TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict)
- [PEP 589 – Typed Dictionaries](https://www.python.org/dev/peps/pep-0589/)
- [Mypy: Optional Static Typing for Python](http://mypy-lang.org/)

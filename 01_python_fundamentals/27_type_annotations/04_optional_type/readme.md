# Optional Types  🚀🐍

Welcome to this comprehensive guide on **Optional Types** in Python 3.12! In this tutorial, we'll explore how to handle the absence of values gracefully using Optional types, understand the pitfalls of `None`, and learn how to make our code more robust and error-resistant. We'll provide complete examples at every step to ensure clarity. Let's dive in! 🌟


## Table of Contents 📖

1. [Introduction to the Billion-Dollar Mistake](#1-introduction-to-the-billion-dollar-mistake-)
2. [The Problem with `None` in Python](#2-the-problem-with-none-in-python-)
3. [Understanding Optional Types](#3-understanding-optional-types-)
4. [Benefits of Using Optional Types](#4-benefits-of-using-optional-types-)
5. [Practical Example: Parsing Integers from Strings](#5-practical-example-parsing-integers-from-strings-)
   - [Initial Implementation](#initial-implementation-)
   - [Issues with `None`](#issues-with-none-)
   - [Type Checking with `mypy`](#type-checking-with-mypy-)
   - [Interpreting `mypy` Errors](#interpreting-mypy-errors-)
   - [Refactoring with Optional Types](#refactoring-with-optional-types-)
   - [Final Code with Explanations](#final-code-with-explanations-)
6. [Complete Example: User Age Lookup](#6-complete-example-user-age-lookup-)
   - [Example Problem](#example-problem-)
   - [Defining the `UserData` Class](#defining-the-userdata-class-)
   - [Creating a Mock Database](#creating-a-mock-database-)
   - [Implementing the `database_lookup` Function](#implementing-the-database_lookup-function-)
   - [Completing the `get_user_age` Function](#completing-the-get_user_age-function-)
   - [Handling Optional Types in `get_user_age`](#handling-optional-types-in-get_user_age-)
   - [Testing the Functions](#testing-the-functions-)
   - [Full Code Listing](#full-code-listing-)
7. [Dealing with Exceptions](#7-dealing-with-exceptions-)
8. [Best Practices with Optional Types](#8-best-practices-with-optional-types-)
9. [Conclusion](#9-conclusion-)
10. [Discussion Topic](#10-discussion-topic-)
11. [Additional Resources](#11-additional-resources-)


## 1. Introduction to the Billion-Dollar Mistake 💰❌

**C.A.R. Hoare**, a renowned computer scientist, famously referred to null references as the "Billion-Dollar Mistake":

> *"I call it my billion-dollar mistake. It was the invention of the null reference in 1965... This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage in the last forty years."*

Null references have caused significant issues in many programming languages, leading to bugs, crashes, and security vulnerabilities.


## 2. The Problem with `None` in Python 🐛

In Python, the concept of null is represented by `None`. While `None` can be useful, it introduces several challenges:

- **Unexpected `None` Values**: Functions may return `None` when you expect a value.
- **Attribute Errors**: Accessing methods or attributes on `None` leads to `AttributeError`.
- **Verbose Checks**: You need to add `if x is not None` checks throughout your code.
- **Silent Failures**: Missing a `None` check can cause bugs that are hard to trace.


## 3. Understanding Optional Types 🤔

Optional types allow you to indicate that a variable may be of a certain type **or** `None`. In Python 3.5, you can use the `typing` module to declare Optional types.

### Syntax

```python
from typing import Optional

variable_name: Optional[Type] = value
```

- **`Optional[Type]`** is equivalent to `Type | None` in Python 3.10 and later.

### Simple Example

```python
from typing import Optional

maybe_number: Optional[int] = 42  # Has a value
maybe_number = None  # Now it's None
```


## 4. Benefits of Using Optional Types 🌟

1. **Clear Intentions**: Communicates to developers that a variable can be `None`.
2. **Type Checking**: Tools like `mypy` can warn you if you forget to handle the `None` case.
3. **Reduced Errors**: Helps prevent `AttributeError` due to `None` values.
4. **Documentation**: Improves code readability and maintainability.


## 5. Practical Example: Parsing Integers from Strings 🔢

Let's work through a simple example of parsing integers from strings to see how Optional types can improve our code.

### Initial Implementation 🛠️

We have a function that attempts to parse an integer from a string input:

```python
def parse_integer(s: str) -> int:
    return int(s)
```

### Issues with `None` ⚠️

If the input string `s` is not a valid integer, `int(s)` will raise a `ValueError`. We might try to handle this by returning `None` when parsing fails:

```python
def parse_integer(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        return None  # Return None on failure
```

However, this introduces problems:

- **Inconsistent Return Type**: The function is annotated to return `int`, but it may return `None`.
- **Potential AttributeError**: If we use the result without checking for `None`, we may encounter errors.

### Type Checking with `mypy` 🔍

Let's check our code with `mypy`.

#### Code with Potential Issues

```python
def parse_integer(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        return None  # Return None on failure

def process_number(s: str) -> None:
    number = parse_integer(s)
    print(f"The number multiplied by 2 is {number * 2}")
```

#### Running `mypy`

```bash
mypy --strict main.py
```

#### `mypy` Output

```
main.py:5: error: Incompatible return value type (got "None", expected "int")  [return-value]
```

### Interpreting `mypy` Errors 📝

#### Error 1

```
main.py:5: error: Incompatible return value type (got "None", expected "int")  [return-value]
```

- **Explanation**: The function `parse_integer` is annotated to return `int`, but it returns `None` in the `except` block.
- **Problem**: Inconsistent return type.

#### Error 2

```
main.py:9: error: Unsupported operand types for * ("int" and "int")  [operator]
main.py:9: note: Left operand is of type "Optional[int]"
```

- **Explanation**: `number` can be `int` or `None` (`Optional[int]`), and `None * 2` is invalid.
- **Problem**: We are using `number` without checking if it's `None`.

### Refactoring with Optional Types 🔄

#### Step 1: Update Return Type

Annotate the return type to be `Optional[int]`:

```python
def parse_integer(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None
```

#### Step 2: Handle `None` in Calling Function

Check if `number` is `None` before using it:

```python
def process_number(s: str) -> None:
    number = parse_integer(s)
    if number is not None:
        print(f"The number multiplied by 2 is {number * 2}")
    else:
        print(f"Invalid integer: '{s}'")
```

### Final Code with Explanations 📜

```python
def parse_integer(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None

def process_number(s: str) -> None:
    """Processes the parsed integer."""
    number = parse_integer(s)
    if number is not None:
        print(f"The number multiplied by 2 is {number * 2}")
    else:
        print(f"Invalid integer: '{s}'")

# Testing the functions
if __name__ == "__main__":
    process_number("42")         # Valid integer
    process_number("not a number")  # Invalid integer
```

#### Running `mypy`

```bash
mypy --strict main.py
```

#### `mypy` Output

```
Success: no issues found in 1 source file
```

#### Program Output

```
The number multiplied by 2 is 84
Invalid integer: 'not a number'
```


## 6. Complete Example: User Age Lookup 🕵️‍♂️

Let's revisit the earlier example and complete the `get_user_age` function with proper handling of `None` values using Optional types.

### Example Problem

```python
def get_user_age(name):
    user_data = database_lookup(name)
    return user_data.age  # What if user_data is None?
```

- **Issue**: If `database_lookup` returns `None`, accessing `user_data.age` will raise an `AttributeError`.

### Defining the `UserData` Class 👤

```python
class UserData:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

- **Attributes**:
  - `name` (str): The name of the user.
  - `age` (int): The age of the user.

### Creating a Mock Database 🗄️

```python
# Mock database as a dictionary
database = {
    "Muhammad Hashim": UserData("Muhammad Hashim", 25),
    "Alice": UserData("Alice", 30),
    "Bob": UserData("Bob", 28),
}
```

### Implementing the `database_lookup` Function 🔍

```python
def database_lookup(name: str) -> UserData | None:
    return database.get(name)

```

- **Returns**:
  - `Optional[UserData]`: Returns a `UserData` object if found; otherwise, `None`.

### Completing the `get_user_age` Function 🎯

To handle the case where `user_data` might be `None`, we update the function:

```python
def get_user_age(name: str) -> int | None:
    user_data = database_lookup(name)
    if user_data is not None:
        return user_data.age
    return None
```

- **Handles the case where `user_data` might be `None`**.

### Handling Optional Types in `get_user_age` ⚠️

By using `Optional` types, we:

- **Prevent Errors**: Avoid `AttributeError` if `user_data` is `None`.
- **Improve Clarity**: Indicate that the function might return `None`.

### Testing the Functions 🧪

```python
def display_user_age(name: str):
    age = get_user_age(name)
    if age is not None:
        print(f"{name} is {age} years old. 🎉")
    else:
        print(f"User '{name}' not found. 😢")
```

#### Running the Test

```python
def main():
    display_user_age("Muhammad Hashim")
    display_user_age("Alice")
    display_user_age("Unknown User")

if __name__ == "__main__":
    main()
```

#### Expected Output

```
Muhammad Hashim is 25 years old. 🎉
Alice is 30 years old. 🎉
User 'Unknown User' not found. 😢
```

### Full Code Listing 📜

```python
from typing import Optional

# 1. Defining the UserData Class
class UserData:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# 2. Creating a Mock Database
database = {
    "Muhammad Hashim": UserData("Muhammad Hashim", 25),
    "Alice": UserData("Alice", 30),
    "Bob": UserData("Bob", 28),
}

# 3. Implementing the database_lookup Function
def database_lookup(name: str) -> UserData | None:
    return database.get(name)

# 4. Completing the get_user_age Function
def get_user_age(name: str) -> int | None:
    user_data = database_lookup(name)
    if user_data is not None:
        return user_data.age
    return None

# 5. Handling Optional Types in get_user_age
def display_user_age(name: str):
    age = get_user_age(name)
    if age is not None:
        print(f"{name} is {age} years old. 🎉")
    else:
        print(f"User '{name}' not found. 😢")

# 6. Testing the Functions
def main():
    display_user_age("Muhammad Hashim")
    display_user_age("Alice")
    display_user_age("Unknown User")

if __name__ == "__main__":
    main()
```


## 7. Dealing with Exceptions 🛡️

Alternatively, we might consider using exceptions to handle errors.

### Using Exceptions

#### Raising Exceptions

```python
class UserNotFoundError(Exception):
    pass

def database_lookup(name: str) -> UserData:
    user_data = database.get(name)
    if user_data is None:
        raise UserNotFoundError(f"User '{name}' not found.")
    return user_data
```

#### Updating `get_user_age` to Handle Exceptions

```python
def get_user_age(name: str) -> int:
    try:
        user_data = database_lookup(name)
        return user_data.age
    except UserNotFoundError as e:
        print(f"Error: {e}")
        return -1  # Indicate an error with a special value
```

#### Testing the Function

```python
def display_user_age(name: str):
    age = get_user_age(name)
    if age != -1:
        print(f"{name} is {age} years old. 🎉")
    else:
        print(f"Could not retrieve age for '{name}'. 😢")
```

#### Output

```
Muhammad Hashim is 25 years old. 🎉
Alice is 30 years old. 🎉
Error: User 'Unknown User' not found.
Could not retrieve age for 'Unknown User'. 😢
```

### Pros and Cons

- **Pros**:
  - Exceptions can simplify error handling in some cases.
- **Cons**:
  - Python doesn't enforce exception handling at compile time.
  - Overuse of exceptions can make code harder to follow.

### Best Practice

- Use exceptions for truly exceptional situations.
- Use Optional types for expected absence of values.


## 8. Best Practices with Optional Types 🏆

1. **Use Optional in Type Hints**: When a function can return `None`, annotate it with `Optional`.

   ```python
   def find_user(name: str) -> Optional[UserData]:
       # Implementation
   ```

2. **Always Check for `None`**: Before using a variable that could be `None`, check it.

   ```python
   user = find_user("Muhammad Hashim")
   if user is not None:
       # Safe to use user
   else:
       print("User not found.")
   ```

3. **Leverage Type Checkers**: Use tools like `mypy` to catch potential issues.

4. **Avoid Overusing `None`**: If a function should always return a value, don't return `None`.

5. **Consider Alternatives**: Sometimes, using exceptions or custom types (like `Maybe` or `Result` types from functional programming) might be more appropriate.


## 9. Conclusion 🎉

Using Optional types in Python 3.12 helps you write safer and more maintainable code by:

- **Explicitly Handling Absence**: Clearly indicating when a variable can be `None`.
- **Reducing Errors**: Preventing `AttributeError` due to unhandled `None` values.
- **Improving Readability**: Making your code's intent clear to other developers.

By incorporating Optional types into your codebase, you can avoid the pitfalls of the "Billion-Dollar Mistake" and ensure a smoother development experience.


## 10. Discussion Topic 💬

**Question:**

How often do you deal with `None` in your codebase? How confident are you that every possible `None` value is handled correctly? Look through bugs and failing tests to see how many times you've been bitten by incorrect `None` handling. Discuss how Optional types and type checking tools like `mypy` will help your codebase.


## 11. Additional Resources 📚

- **Python `typing` Module Documentation**: [typing — Support for type hints](https://docs.python.org/3/library/typing.html#typing.Optional)
- **`mypy` Type Checker**: [The mypy type checker for Python](http://mypy-lang.org/)
- **PEP 484**: [Type Hints](https://www.python.org/dev/peps/pep-0484/)
- **Real Python Guide**: [Python Type Checking (Guide) – Real Python](https://realpython.com/python-type-checking/)


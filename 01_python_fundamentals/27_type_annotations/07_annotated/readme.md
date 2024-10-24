# Annotated Types 🚀📝

Welcome to this guide on **Annotated Types** in Python 3.12! In this section, we'll explore how to provide extra constraints and metadata using the `Annotated` type. This allows you to communicate more complex requirements about your data without needing to write lengthy and repetitive code. We’ll explain what `Annotated` is, how to use it, and include complete examples for clarity. Let's dive in! 🌟


## Table of Contents 📖

- [Annotated Types 🚀📝](#annotated-types-)
  - [Table of Contents 📖](#table-of-contents-)
  - [1. Introduction to Annotated Types 🤔](#1-introduction-to-annotated-types-)
    - [Basic Syntax](#basic-syntax)
  - [2. Why Use Annotated Types? 📋](#2-why-use-annotated-types-)
  - [3. Practical Examples 🌟](#3-practical-examples-)
    - [Example 1: Value Range 📊](#example-1-value-range-)
    - [Example 2: Regular Expression Match 🔍](#example-2-regular-expression-match-)
    - [Example 3: String Length Constraint 📏](#example-3-string-length-constraint-)
  - [4. Implementing Custom Constraints 🔧](#4-implementing-custom-constraints-)
    - [Step 1: Create the Constraints](#step-1-create-the-constraints)
    - [Step 2: Implement Validation Logic](#step-2-implement-validation-logic)
    - [Step 3: Use and Test Annotations](#step-3-use-and-test-annotations)
  - [5. Benefits and Best Practices 🏆](#5-benefits-and-best-practices-)
    - [Benefits 🌈](#benefits-)
    - [Best Practices ✅](#best-practices-)
  - [6. Conclusion 🎉](#6-conclusion-)
  - [7. Discussion Topic 💬](#7-discussion-topic-)
  - [8. Additional Resources 📚](#8-additional-resources-)


## 1. Introduction to Annotated Types 🤔

The `Annotated` type allows you to attach **metadata** to a type. This metadata can be used for documentation, validation, or other purposes that require more information about the expected data. For example, you might want to specify that a string should match a particular **pattern** or that an integer must be within a **certain range**.

### Basic Syntax

```python
from typing import Annotated

x: Annotated[int, "Value must be between 3 and 5"]
y: Annotated[str, "Must match the pattern '[0-9]{4}'"]
```

In this syntax, `Annotated` wraps around a type (e.g., `int`, `str`) and is followed by one or more **metadata values**.


## 2. Why Use Annotated Types? 📋

1. **Clarity**: Adds more context to your code, making it easier to understand and maintain.
2. **Documentation**: Useful for specifying constraints directly alongside your type hints.
3. **Validation**: Helps set up rules for validation even if they aren't directly enforced by Python.

**Note**: Python itself does not enforce these annotations, but they can be used with external libraries or your custom validation code to enforce constraints.


## 3. Practical Examples 🌟

Let's see some practical use cases for Annotated types!

### Example 1: Value Range 📊

You might want to specify that a particular integer should always be between **3 and 5**.

```python
from typing import Annotated

class ValueRange:
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

x: Annotated[int, ValueRange(3, 5)] = 4  # Valid, within the range
```

**Enhanced Example with Validation:**

```python
from typing import Annotated

class ValueRange:
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

x: Annotated[int, ValueRange(3, 5)] = 6  # Invalid, outside the range

def validate_annotated(var, metadata) -> None:
    if isinstance(metadata, ValueRange):
        if not (metadata.min_val <= var <= metadata.max_val):
            raise ValueError(f"Value {var} is not between {metadata.min_val} and {metadata.max_val}.")

# Validation
try:
    validate_annotated(x, ValueRange(3, 5))
    print(f"{x} is valid!")
except ValueError as e:
    print(e)
```

**Output:**
```
Value 6 is not between 3 and 5.
```

**Code Explanation:**

In this example:

1. **Defining Metadata Class**: The `ValueRange` class is defined to hold the minimum and maximum values for the range constraint.
2. **Annotated Variable**: The variable `x` is annotated with `Annotated[int, ValueRange(3, 5)]`, indicating that `x` should be an integer between 3 and 5.
3. **Invalid Assignment**: `x` is assigned the value `6`, which is outside the specified range.
4. **Validation Function**: The `validate_annotated` function checks if the value of `x` falls within the specified range. If not, it raises a `ValueError`.
5. **Testing Validation**: When `validate_annotated` is called with `x` and its metadata, it detects that `6` is outside the range and prints an error message.


### Example 2: Regular Expression Match 🔍

You might need a string to match a **specific pattern**, like a 4-digit code.

```python
from typing import Annotated
import re

class MatchesRegex:
    def __init__(self, pattern: str):
        self.pattern = re.compile(pattern)

y: Annotated[str, MatchesRegex(r'^\d{4}$')] = "2024"  # Valid, matches the regex
```

**Enhanced Example with Validation:**

```python
from typing import Annotated
import re

class MatchesRegex:
    def __init__(self, pattern: str):
        self.pattern = re.compile(pattern)

y: Annotated[str, MatchesRegex(r'^\d{4}$')] = "20A4"  # Invalid, contains a non-digit character

def validate_annotated(var, metadata) -> None:
    if isinstance(metadata, MatchesRegex):
        if not metadata.pattern.match(var):
            raise ValueError(f"Value '{var}' does not match the pattern {metadata.pattern.pattern}.")

# Validation
try:
    validate_annotated(y, MatchesRegex(r'^\d{4}$'))
    print(f"'{y}' is valid!")
except ValueError as e:
    print(e)
```

**Output:**
```
Value '20A4' does not match the pattern ^\d{4}$.
```

**Code Explanation:**

In this example:

1. **Defining Metadata Class**: The `MatchesRegex` class is created to store a compiled regular expression pattern.
2. **Annotated Variable**: The variable `y` is annotated with `Annotated[str, MatchesRegex(r'^\d{4}$')]`, indicating that `y` should be a string matching exactly four digits.
3. **Invalid Assignment**: `y` is assigned the value `"20A4"`, which contains a non-digit character `'A'` and thus does not match the regex pattern.
4. **Validation Function**: The `validate_annotated` function checks if `y` matches the specified regex pattern. If it doesn't, a `ValueError` is raised.
5. **Testing Validation**: When `validate_annotated` is invoked with `y` and its metadata, it identifies that `"20A4"` does not conform to the pattern and prints an error message.


### Example 3: String Length Constraint 📏

If a string must have **a specific length**, you can add a constraint for that too.

```python
from typing import Annotated

class StringLength:
    def __init__(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len

username: Annotated[str, StringLength(5, 15)] = "Hashim123"  # Valid, length within range
```

**Enhanced Example with Validation:**

```python
from typing import Annotated

class StringLength:
    def __init__(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len

username: Annotated[str, StringLength(5, 15)] = "Hi"  # Invalid, too short

def validate_annotated(var, metadata) -> None:
    if isinstance(metadata, StringLength):
        if not (metadata.min_len <= len(var) <= metadata.max_len):
            raise ValueError(f"Length of '{var}' is not between {metadata.min_len} and {metadata.max_len}.")

# Validation
try:
    validate_annotated(username, StringLength(5, 15))
    print(f"'{username}' is valid!")
except ValueError as e:
    print(e)
```

**Output:**
```
Length of 'Hi' is not between 5 and 15.
```

**Code Explanation:**

In this example:

1. **Defining Metadata Class**: The `StringLength` class is defined to hold the minimum and maximum length constraints for a string.
2. **Annotated Variable**: The variable `username` is annotated with `Annotated[str, StringLength(5, 15)]`, indicating that `username` should be a string with a length between 5 and 15 characters.
3. **Invalid Assignment**: `username` is assigned the value `"Hi"`, which has a length of 2, falling below the minimum required length.
4. **Validation Function**: The `validate_annotated` function checks if the length of `username` is within the specified range. If not, it raises a `ValueError`.
5. **Testing Validation**: When `validate_annotated` is called with `username` and its metadata, it detects that `"Hi"` is too short and prints an error message.


## 4. Implementing Custom Constraints 🔧

Since Python doesn’t enforce the `Annotated` constraints, you need to write **custom validation**. Here's how:

### Step 1: Create the Constraints

```python
class ValueRange:
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

class MatchesRegex:
    def __init__(self, pattern: str):
        self.pattern = re.compile(pattern)

class StringLength:
    def __init__(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len
```

### Step 2: Implement Validation Logic

```python
def validate_annotated(var, metadata) -> bool:
    if isinstance(metadata, ValueRange):
        if not (metadata.min_val <= var <= metadata.max_val):
            print(f"Error: {var} is not between {metadata.min_val} and {metadata.max_val}.")
            return False
    if isinstance(metadata, MatchesRegex):
        if not metadata.pattern.match(var):
            print(f"Error: '{var}' does not match the pattern {metadata.pattern.pattern}.")
            return False
    if isinstance(metadata, StringLength):
        if not (metadata.min_len <= len(var) <= metadata.max_len):
            print(f"Error: Length of '{var}' is not between {metadata.min_len} and {metadata.max_len}.")
            return False
    return True
```

### Step 3: Use and Test Annotations

```python
from typing import Annotated

# Define Annotated variables
x: Annotated[int, ValueRange(3, 5)] = 4
y: Annotated[str, MatchesRegex(r'^\d{4}$')] = "1234"
username: Annotated[str, StringLength(5, 15)] = "Hashim123"

# Invalid Annotated variables
invalid_x: Annotated[int, ValueRange(3, 5)] = 6
invalid_y: Annotated[str, MatchesRegex(r'^\d{4}$')] = "12A4"
invalid_username: Annotated[str, StringLength(5, 15)] = "Hi"

# Testing function
def test_values():
    annotations = [
        (x, ValueRange(3, 5)),
        (y, MatchesRegex(r'^\d{4}$')),
        (username, StringLength(5, 15)),
        (invalid_x, ValueRange(3, 5)),
        (invalid_y, MatchesRegex(r'^\d{4}$')),
        (invalid_username, StringLength(5, 15)),
    ]

    for var, metadata in annotations:
        if validate_annotated(var, metadata):
            print(f"{var} is valid! ✅")
        else:
            print(f"{var} is invalid! ❌")

test_values()
```

**Output:**
```
4 is valid! ✅
1234 is valid! ✅
Hashim123 is valid! ✅
Error: 6 is not between 3 and 5.
6 is invalid! ❌
Error: '12A4' does not match the pattern ^\d{4}$.
12A4 is invalid! ❌
Error: Length of 'Hi' is not between 5 and 15.
Hi is invalid! ❌
```

**Code Explanation:**

In this comprehensive validation setup:

1. **Defining Metadata Classes**: Three classes (`ValueRange`, `MatchesRegex`, and `StringLength`) are defined to encapsulate different types of constraints.
2. **Annotated Variables**: Variables `x`, `y`, and `username` are annotated with their respective constraints. Additionally, `invalid_x`, `invalid_y`, and `invalid_username` are defined with values that intentionally violate these constraints.
3. **Validation Function**: The `validate_annotated` function checks each variable against its metadata. It prints an error message and returns `False` if the constraint is not met; otherwise, it returns `True`.
4. **Testing Function**: The `test_values` function iterates over all annotated variables, both valid and invalid, and applies the validation function to each. It prints whether each value is valid or invalid based on the constraints.
5. **Execution and Output**: Running `test_values()` will validate each variable and output the corresponding messages, demonstrating both successful validations and error handling for invalid values.


## 5. Benefits and Best Practices 🏆

### Benefits 🌈

- **Improved Readability**: Knowing what a variable represents and its constraints makes code easier to understand.
- **Documentation**: Acts as inline documentation, giving you hints about expected values.
- **Cleaner Code**: Allows specifying constraints without needing extra comments or external documentation.

### Best Practices ✅

1. **Clearly Define Metadata**: Make sure your metadata classes (`ValueRange`, `MatchesRegex`, etc.) are straightforward and self-explanatory.
2. **Custom Validation**: Always implement custom validation logic if you plan to enforce these constraints.
3. **Tool Integration**: Consider using external tools or libraries that can interpret and act upon `Annotated` metadata.


## 6. Conclusion 🎉

**Annotated types** are a powerful way to add additional context to your variables, making your code clearer, more maintainable, and potentially easier to validate. While Python doesn’t enforce these annotations directly, you can leverage them in your custom logic, effectively creating a more structured and predictable codebase.


## 7. Discussion Topic 💬

**Question:**

Have you found cases where you needed more detailed constraints than what standard types provide? How would using `Annotated` help clarify your code? Discuss your experiences and any challenges you foresee.


## 8. Additional Resources 📚

- **PEP 593**: [Flexible function and variable annotations](https://www.python.org/dev/peps/pep-0593/)
- **Python `typing` Module**: [typing — Support for type hints](https://docs.python.org/3/library/typing.html#typing.Annotated)
- **Real Python Guide**: [Type Annotations and Type Hints in Python](https://realpython.com/python-type-checking/)
- **Mypy Documentation**: [Mypy and Annotated Types](https://mypy.readthedocs.io/en/stable/extension_declarations.html#annotated-types)



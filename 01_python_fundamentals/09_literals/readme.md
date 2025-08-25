# Literals in Python 🔢📜

In this section, we'll explore **literals** in Python. A **literal** is a direct way to represent a data value (such as numbers, strings, or containers) in your code. Literals are essential for initializing variables and working with data in Python.

## Table of Contents 📋

- [Literals in Python 🔢📜](#literals-in-python-)
  - [Table of Contents 📋](#table-of-contents-)
  - [Number and String Literals 🔢📄](#number-and-string-literals-)
    - [Number Literals](#number-literals)
    - [Example:](#example)
    - [String Literals](#string-literals)
    - [Example:](#example-1)
  - [Container Literals 📦](#container-literals-)
    - [Example:](#example-2)
    - [Important Note 📝](#important-note-)
    - [Example:](#example-3)

## Number and String Literals 🔢📄

### Number Literals

| **Literal** | **Type**                   | **Example**             |
|-------------|----------------------------|-------------------------|
| Integer     | Whole numbers               | `42`                    |
| Floating-point | Numbers with decimals       | `3.14`                  |
| Imaginary   | Complex numbers (imaginary part) | `1.0j`                |

### Example:
```python
42       # Integer literal
3.14     # Floating-point literal
1.0j     # Imaginary literal
```

### String Literals

| **Literal**        | **Description**                              | **Example**                  |
|--------------------|----------------------------------------------|------------------------------|
| Single-quoted      | A string wrapped in single quotes `' '`      | `'hello'`                    |
| Double-quoted      | A string wrapped in double quotes `" "`      | `"world"`                    |
| Triple-quoted      | A string spanning multiple lines             | `"""Good\nnight"""`          |

### Example:
```python
'hello'       # Single-quoted string literal
"world"       # Double-quoted string literal
"""Good
night"""      # Triple-quoted string literal (spans multiple lines)
```

## Container Literals 📦

Combining number and string literals with appropriate delimiters allows you to create container literals, which directly denote data values of container types.

| **Container Type** | **Literal**                    | **Example**                        |
|--------------------|--------------------------------|------------------------------------|
| List               | Enclosed in square brackets `[]` | `[42, 3.14, 'hello']`             |
| Empty List         | Empty square brackets `[]`     | `[]`                              |
| Tuple              | Values separated by commas     | `100, 200, 300`                   |
| Empty Tuple        | Empty parentheses `()`         | `()`                              |
| Dictionary         | Key-value pairs enclosed in `{}` | `{'x':42, 'y':3.14}`             |
| Empty Dictionary   | Empty curly braces `{}`        | `{}`                              |
| Set                | Values enclosed in `{}`        | `{1, 2, 4, 8, 'string'}`          |

### Example:
```python
[42, 3.14, 'hello']    # List
[]                     # Empty list
100, 200, 300          # Tuple
()                     # Empty tuple
{'x':42, 'y':3.14}     # Dictionary
{}                     # Empty dictionary
{1, 2, 4, 8, 'string'} # Set
```

### Important Note 📝
- There is **no literal** to denote an **empty set**. To create an empty set, use the `set()` function.

### Example:
```python
empty_set = set()  # Correct way to create an empty set
```
This section covered the basics of **literals** in Python, including different types of number, string, and container literals. Literals are the building blocks for creating and manipulating data in your Python programs. 🛠️

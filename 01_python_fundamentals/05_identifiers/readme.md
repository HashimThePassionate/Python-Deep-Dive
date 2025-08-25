# Identifiers in Python 🆔

## Table of Contents 📋
- [Identifiers in Python 🆔](#identifiers-in-python-)
  - [Table of Contents 📋](#table-of-contents-)
  - [What is an Identifier? 🔍](#what-is-an-identifier-)
  - [Rules for Creating Identifiers 📏](#rules-for-creating-identifiers-)
    - [Example:](#example)
  - [Naming Conventions 📚](#naming-conventions-)
    - [Example:](#example-1)
    - [Private Identifiers 🔒](#private-identifiers-)
    - [Example:](#example-2)
  - [Special Use of Underscore in Interactive Sessions 🖥️](#special-use-of-underscore-in-interactive-sessions-️)
    - [Example:](#example-3)

---

In this section, we'll explore what **identifiers** are in Python and how to use them correctly. Identifiers are fundamental in Python as they represent variables, functions, classes, and other objects.

## What is an Identifier? 🔍

- An **identifier** is a name used to specify a variable, function, class, module, or any other object in Python.
- **Identifiers** help in naming various entities in your Python code, making it easier to reference them later.

## Rules for Creating Identifiers 📏

- An identifier must start with:
  - A letter (A-Z or a-z in Python v2).
  - An underscore `_`.
  - In Python v3, any character classified as a letter by Unicode can also be used to start an identifier.

- After the first character, an identifier can include:
  - Letters (A-Z, a-z).
  - Digits (0-9).
  - Underscores `_`.
  - In Python v3, any character classified as a letter by Unicode can also be used to start an identifier.
  - In Python v3, Unicode characters classified as digits or combining marks are also allowed.

- **Case Sensitivity**: Identifiers are case-sensitive, meaning `myVariable`, `MyVariable`, and `MYVARIABLE` are all different identifiers.

- **Punctuation**: Characters like `@`, `$`, and `!` are **not allowed** in identifiers.

### Example:
```python
my_variable = 10  # Valid identifier
MyVariable = 20   # Another valid identifier (different from the first due to case sensitivity)
1stVariable = 30  # Invalid identifier (cannot start with a digit)
नंबर१ = 5 
نمبر۲  = 10
result = नंबर१ + نمبر۲
print(result)
print(result) # In Python v3, Unicode characters classified as digits or combining marks are also allowed.
```

## Naming Conventions 📚

- **Class Names**: Typically start with an uppercase letter.
- **Other Identifiers**: Typically start with a lowercase letter.

### Example:
```python
class MyClass:  # Class name starts with an uppercase letter
    pass

def my_function():  # Function name starts with a lowercase letter
    pass
```

### Private Identifiers 🔒

- Starting an identifier with a single leading underscore `_` indicates that the identifier is intended to be **private**.
- Starting with two leading underscores `__` indicates a **strongly private** identifier.
- If an identifier starts and ends with double underscores `__name__`, it is a **language-defined special name**.

### Example:
```python
_private_var = 10  # Indicates a private variable
__strong_private_var = 20  # Indicates a strongly private variable
__init__ = 30  # Special language-defined name (used in class constructors)
```

## Special Use of Underscore in Interactive Sessions 🖥️

- In the interactive Python interpreter, the identifier `_` (a single underscore) is special.
- It is automatically bound to the result of the last expression statement evaluated.

### Example:
```python
>>> 5 + 3
8
>>> _ * 2
16  # _ refers to the last result, which was 8
```

---

This section provided an overview of **identifiers** in Python, including the rules for creating them and the conventions for naming. Proper use of identifiers is crucial for writing clear, maintainable, and functional Python code. 🚀

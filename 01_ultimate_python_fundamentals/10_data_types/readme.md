# Data Types in Python 🧮📊

In this section, we'll explore the various **data types** in Python. Understanding these data types is crucial as they form the foundation of any Python program, determining the kind of data the program can handle and how that data can be manipulated.

## Introduction to Data Types 🔍

- **Objects**: In Python, data values are referred to as **objects**.
- **Type**: Each object has a **type** that defines the operations the object supports, its attributes, items, and whether it can be altered.
- **Mutable vs Immutable**:
  - **Mutable objects**: Objects that can be changed after their creation (e.g., lists, dictionaries).
  - **Immutable objects**: Objects that cannot be changed once created (e.g., numbers, strings, tuples).

### Example:
```python
x = 42  # Immutable integer object
y = [1, 2, 3]  # Mutable list object
```

- **Type Checking**:
  - `type(obj)`: Returns the type of the object `obj`.
  - `isinstance(obj, type)`: Returns `True` if `obj` is an instance of `type` or any subclass thereof.

### Example:
```python
x = 42
print(type(x))  # <class 'int'>
print(isinstance(x, int))  # True
```

## Numeric Data Types 🔢

Python supports several built-in numeric types:

### Integer Numbers 🔡

- **Integer literals** can be:
  - **Decimal**: A sequence of digits (e.g., `1, 23, 3493`).
  - **Binary**: Prefixed with `0b` (e.g., `0b010101, 0b110010`).
  - **Octal**: Prefixed with `0o` (e.g., `0o1, 0o27, 0o6645`).
  - **Hexadecimal**: Prefixed with `0x` (e.g., `0x1, 0x17, 0xDA5`).

- **Integer literals** have no upper bound in Python v3.

### Example:
```python
1, 23, 3493        # Decimal integer literals
0b010101, 0b110010 # Binary integer literals
0o1, 0o27, 0o6645  # Octal integer literals
0x1, 0x17, 0xDA5   # Hexadecimal integer literals
```

### Floating-Point Numbers 🌊

- **Floating-point literals** include:
  - A **decimal point** `.` (e.g., `3.14`).
  - An **exponent suffix** `e` or `E` (e.g., `1e3, 2.5e-2`).
  
- A Python floating-point value corresponds to a C double and typically has 53 bits of precision.

### Example:
```python
0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0e0  # Floating-point literals
```

### Complex Numbers 🔮

- A **complex number** consists of two floating-point values: the real part and the imaginary part.
- **Imaginary literals** are created by appending `j` or `J` to a floating-point or decimal literal.

### Example:
```python
0j, 0.j, 0.0j, .0j, 1j, 1.j, 1.0j, 1e0j, 1.e0j, 1.0e0j  # Imaginary literals
```

- To denote a complex number, add or subtract a floating-point literal and an imaginary one.

### Example:
```python
1+0j, 1.0+0.0j  # Complex numbers
```

## New in Python 3.6: Underscores in Numeric Literals 🆕

- From Python 3.6 onward, you can include underscores `_` in numeric literals for better readability.

### Example:
```python
100_000.000_0001, 0x_FF_FF, 0o7_777, 0b_1010_1010
# Outputs: (100000.0000001, 65535, 4095, 170)
```

## String Data Types 📝

Strings in Python are sequences of characters enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`). Strings are immutable, meaning once a string is created, it cannot be modified.

### Example:
```python
'hello'       # Single-quoted string
"world"       # Double-quoted string
"""Good
night"""      # Triple-quoted string, spans multiple lines
```

## Container Data Types 📦

Python supports various container types, such as lists, tuples, dictionaries, and sets.

### Lists 📋

- Lists are ordered sequences of elements, enclosed in square brackets `[]`.
  
### Example:
```python
[42, 3.14, 'hello']  # List with different types of elements
[]                   # Empty list
```

### Tuples 🍰

- Tuples are ordered, immutable sequences, typically enclosed in parentheses `()`.

### Example:
```python
100, 200, 300  # Tuple
()             # Empty tuple
```

### Dictionaries 📖

- Dictionaries are unordered collections of key-value pairs, enclosed in curly braces `{}`.

### Example:
```python
{'x':42, 'y':3.14}  # Dictionary with two key-value pairs
{}                  # Empty dictionary
```

### Sets 🗃️

- Sets are unordered collections of unique elements, enclosed in curly braces `{}`.

### Example:
```python
{1, 2, 4, 8, 'string'}  # Set with different types of elements
```

- Note: There is no literal for an empty set; use `set()` instead.

### Example:
```python
empty_set = set()  # Correct way to create an empty set
```

This section covered the **data types** in Python, including numeric types, strings, and containers. Understanding these data types allows you to effectively manipulate and work with data in Python. 🛠️

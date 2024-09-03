# Python Primitive Data Types 🧮📊

Understanding **data types** is fundamental to programming in Python, as they define the types of values that can be manipulated and the operations that can be performed on them. In Python, all data is represented as **objects**, and each object has a specific **type**.

## What is an Object in Python? 🧱

An **object** is a core concept in Python. It is an instance of a data type that contains both data (attributes) and methods (functions) that operate on the data. In Python, everything is treated as an object, which makes Python an **object-oriented programming (OOP)** language.

- **Definition**: An **object** in Python is a collection of data (variables) and methods (functions) that act on the data. Objects are instances of classes, and every object has a **type** (or class) that defines what operations it supports and what attributes it has.
- **Example**: An integer like `42` is an object of type `int`, and a string like `"hello"` is an object of type `str`.

### Key Points:
- **Data and Behavior**: Objects encapsulate both **data** (attributes) and **behavior** (methods).
- **Type**: Every object has a type that defines the operations it supports.
- **Instance of a Class**: Objects are instances of classes, which are blueprints for creating objects.

### Example: 🖥️
```python
x = 42  # x is an object of type 'int'
y = "Hello"  # y is an object of type 'str'
```

## Introduction to Data Types 🔍

- **Objects**: In Python, every value is represented as an **object**.
- **Type**: Each object has a **type** that defines what kind of operations can be performed on it, what attributes it has, and whether it can be changed or not.
- **Mutable vs Immutable**:
  - **Mutable Objects**: These are objects that can be changed after they are created. For example, lists and dictionaries (which we are not covering here).
  - **Immutable Objects**: These are objects that cannot be changed once they are created. For example, integers, floats, strings, and tuples.

### How are Objects Immutable? 🤔

- **Immutable Integer (`int`)**: When you assign `42` to `x`, Python creates an `int` object with the value `42` in memory. `x` is just a reference (or pointer) to that object. If you try to change `x` (e.g., `x = x + 1`), Python doesn't modify the existing object; instead, it creates a new `int` object with the value `43` and makes `x` point to the new object. The original object `42` remains unchanged.

- **Immutable String (`str`)**: Similarly, when you assign `"Hello"` to `y`, Python creates a `str` object with the value `"Hello"` in memory. If you attempt to modify the string (e.g., `y += " World"`), Python does not alter the original string. Instead, it creates a new `str` object with the concatenated value `"Hello World"` and assigns this new object to `y`. The original `"Hello"` string remains unchanged.

### Example: 📘
```python
x = 42  # Immutable integer object
y = "Hello"  # Immutable string object

x = x + 1  # x now points to a new integer object 43
y += " World"  # y now points to a new string object "Hello World"
```

In the example above:
- After `x = x + 1`, `x` points to a new object `43`. The original `42` is unchanged.
- After `y += " World"`, `y` points to a new object `"Hello World"`. The original `"Hello"` is unchanged.

### Type Checking in Python 🔍

Python provides two built-in functions to check the type of an object:

- **`type(obj)`**: Returns the type of the object `obj`.
- **`isinstance(obj, type)`**: Returns `True` if `obj` is an instance of `type` or any subclass thereof.

### Example: 🕵️‍♂️
```python
x = 42
print(type(x))  # Output: <class 'int'>
print(isinstance(x, int))  # Output: True
```

## Accessing Previous Object Values 🕵️‍♂️

### How to Preserve the Original Object Value? 🤔

To access the original value after changing a variable, you must first **store the original value** in another variable.

### Example: 📘
```python
x = 42  # Original immutable integer object
original_x = x  # Storing the original value in a different variable

x = x + 1  # Now x points to a new integer object 43

print("Current x:", x)  # Output: Current x: 43
print("Original x:", original_x)  # Output: Original x: 42
```

### How Does This Work?

1. **Initial Assignment**: `x` is assigned the value `42`, which is an immutable integer object.
2. **Storing the Original**: `original_x` is set to `x`, so `original_x` also points to the integer object `42`.
3. **Modification**: `x = x + 1` creates a new integer object with the value `43` and `x` now points to this new object.
4. **Accessing Both Values**: The original value (`42`) is still accessible through `original_x`, while the updated value (`43`) is accessible through `x`.

### Key Takeaway 📝

- **Immutable Objects**: Once modified, the original object is not accessible unless it was saved to another variable beforehand.
- **Memory Management**: Python manages memory automatically and will clean up (garbage collect) objects that are no longer referenced.

## Numeric Data Types 🔢

Python provides several built-in numeric types to handle numbers:

1. **Integers (int)**
2. **Floating-Point Numbers (float)**
3. **Complex Numbers (complex)**

### Integer Numbers 🔡

- **Description**: Integers are whole numbers without a decimal point. They can be positive, negative, or zero.
- **Integer Literals** can be:
  - **Decimal**: A simple sequence of digits (e.g., `1, 23, 3493`).
  - **Binary**: Prefixed with `0b` (e.g., `0b010101, 0b110010`).
  - **Octal**: Prefixed with `0o` (e.g., `0o1, 0o27, 0o6645`).
  - **Hexadecimal**: Prefixed with `0x` (e.g., `0x1, 0x17, 0xDA5`).

### Key Points:
- **Unlimited Precision**: In Python, integers have unlimited precision, meaning they can grow as large as your memory allows.
- **Type Conversion**: You can convert between different bases using `int()` with the base specified.

### Example: 🧮
```python
# Decimal integer literals
print(1, 23, 3493)

# Binary integer literals
print(0b010101, 0b110010)

# Octal integer literals
print(0o1, 0o27, 0o6645)

# Hexadecimal integer literals
print(0x1, 0x17, 0xDA5)
```

### Floating-Point Numbers 🌊

- **Description**: Floating-point numbers (floats) are numbers that have a decimal point. They can represent real numbers and are used when more precision is required than an integer.
- **Floating-Point Literals** include:
  - A **decimal point** `.` (e.g., `3.14`).
  - An **exponent suffix** `e` or `E` that represents scientific notation (e.g., `1e3` which is `1000`, `2.5e-2` which is `0.025`).

### Key Points:
- **Double Precision**: Python's floating-point numbers are implemented using double in C, giving them approximately 15-17 decimal digits of precision.
- **Representation Error**: Due to the way floating-point numbers are stored, some numbers cannot be represented exactly.

### Example: 🔢
```python
# Examples of floating-point literals
print(0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0e0)
# Output: 0.0 0.0 0.0 1.0 1.0 1.0 1.0 1.0
```

### Complex Numbers 🔮

- **Description**: Complex numbers are numbers that have a real part and an imaginary part. In Python, they are represented as `a + bj`, where `a` is the real part, and `b` is the imaginary part.
- **Imaginary literals** are created by appending `j` or `J` to a floating-point or decimal literal.

### Key Points:
- **Complex Numbers in Python**: Python handles complex numbers natively with the `complex` type

.
- **Arithmetic Operations**: You can perform arithmetic operations (+, -, *, /) on complex numbers.

### Example: 🔍
```python
# Examples of imaginary literals
print(0j, 0.j, 0.0j, .0j, 1j, 1.j, 1.0j, 1e0j, 1.e0j, 1.0e0j)

# Complex numbers
print(1+0j, 1.0+0.0j)
```

## New in Python 3.6: Underscores in Numeric Literals 🆕

- **Description**: To improve readability, Python 3.6 introduced the use of underscores (`_`) in numeric literals.
- **Usage**: You can use underscores to separate groups of digits in numeric literals, making them easier to read.

### Example: 📝
```python
print(100_000.000_0001, 0x_FF_FF, 0o7_777, 0b_1010_1010)
# Outputs: (100000.0000001, 65535, 4095, 170)
```

## String Data Types 📝

- **Description**: Strings in Python are sequences of characters enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`). They are immutable, meaning once a string is created, it cannot be modified.
- **Types of Strings**:
  - **Single-quoted strings**: `'hello'`
  - **Double-quoted strings**: `"world"`
  - **Triple-quoted strings**: Useful for multi-line strings or strings that contain both single and double quotes.

### Key Points:
- **Concatenation**: Strings can be concatenated using the `+` operator.
- **Repetition**: Strings can be repeated using the `*` operator.
- **Immutability**: Once defined, the contents of a string cannot be changed.

### Example: 💬
```python
print('hello')       # Single-quoted string
print("world")       # Double-quoted string
print("""Good
night""")  # Triple-quoted string, spans multiple lines
```

## Boolean Data Type 🟢🔴

- **Description**: Booleans represent one of two values: `True` or `False`. Booleans are used for conditional statements and logical operations.
- **Logical Operations**:
  - **AND (`and`)**: Returns `True` if both operands are true.
  - **OR (`or`)**: Returns `True` if at least one operand is true.
  - **NOT (`not`)**: Inverts the value; `True` becomes `False` and vice versa.

### Example: 🤔
```python
is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>
print(is_python_fun and False)  # Output: False
print(not is_python_fun)  # Output: False
```

## Primitive Data Types in Python 🧱

1. **Integers (int)**: Whole numbers without a decimal point.
2. **Floating-Point Numbers (float)**: Numbers with a decimal point.
3. **Complex Numbers (complex)**: Numbers with a real and an imaginary part.
4. **Strings (str)**: Sequence of characters enclosed in quotes.
5. **Booleans (bool)**: Represents `True` or `False` values.

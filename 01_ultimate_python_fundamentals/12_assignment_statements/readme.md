# Assignment Statements in Python 📝

In this section, we'll explore **assignment statements** in Python, which are used to bind variables, attributes, or items to objects. Understanding how assignment works is key to managing data and references effectively in your Python programs.

## Plain Assignment Statements 🧮

A **plain assignment statement** is the most common way to create or rebind variables and other references in Python.

### Basic Syntax

The basic syntax of a plain assignment is:
```python
target = expression
```
- **Target (LHS)**: The variable or reference you want to bind to an object.
- **Expression (RHS)**: The value or object that you want to assign to the target.

### Examples of Plain Assignment

- **Variable Assignment**: 
  - Binding a variable to an object.
  ```python
  name = "Hashim"
  ```
  
- **Attribute Assignment**:
  - Binding an attribute of an object.
  ```python
  x.attr = 42
  ```
  
- **Item Assignment in a Container**:
  - Binding an item in a list, dictionary, or other container types.
  ```python
  my_list[0] = "First item"
  my_dict['key'] = "Value"
  ```

### Multiple Assignments

You can bind multiple variables to the same value in a single statement:
```python
a = b = c = 0
```
- In this case, `a`, `b`, and `c` all refer to the same object, `0`. The RHS expression is evaluated once, and all targets are bound to the resulting object.

### Unpacking Assignments

- **Unpacking** allows you to assign values from an iterable to multiple variables at once:
```python
a, b, c = [1, 2, 3]
```
- **Extended Unpacking (Python 3.x)**:
  - In Python 3.x, you can use a starred expression to capture the remaining items:
  ```python
  first, *middle, last = [1, 2, 3, 4, 5]
  ```
  - `first` is `1`, `middle` is `[2, 3, 4]`, and `last` is `5`.

### Swapping Variables

- You can easily swap the values of two variables using unpacking:
```python
a, b = b, a
```

## Augmented Assignment Statements 🔄

An **augmented assignment** statement is a more concise way to perform an operation and assign the result to the same variable.

### Basic Syntax

The basic syntax of augmented assignment is:
```python
target += expression
```
- **Augmented Operators**: Python supports several augmented operators like `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `>>=`, `<<=`, and (in Python 3.x) `@=`.

### How Augmented Assignment Works

1. **Evaluate RHS Expression**: The expression on the right-hand side is evaluated first.
2. **In-place Modification**:
   - If the object referenced by the LHS has an in-place method for the operation (e.g., `__iadd__` for `+=`), Python will call this method.
   - This method modifies the object in place and returns the modified object.
3. **Rebinding**:
   - If there is no in-place method, Python will perform the operation and then rebind the reference to a new object.

### Example:
```python
x = 5
x += 2  # Equivalent to x = x + 2
print(x)  # Outputs: 7
```

### Key Differences Between Plain and Augmented Assignment

- **Plain Assignment**:
  - Can create or rebind the target reference, but it does not modify the object itself.
  - Example:
    ```python
    x = [1, 2, 3]
    x = x + [4]  # Creates a new list and rebinds x to it
    ```
  
- **Augmented Assignment**:
  - Modifies the object itself if an in-place method exists; otherwise, it behaves like plain assignment.
  - Example:
    ```python
    x = [1, 2, 3]
    x += [4]  # Modifies the original list in place
    ```

### Restrictions

- **Single Target**: Augmented assignments can have only one target on the LHS.
- **No Creation**: Augmented assignment cannot create a new reference; the target must already exist.

---

This section covered **assignment statements** in Python, including both plain and augmented assignments. Understanding these concepts is essential for efficient data management and manipulation in Python. 🛠️

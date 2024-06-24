### Special Methods
#### 1. Special Methods Are for the Python Interpreter

- **Intended Use**:
  - Special methods (also known as "magic methods" or "dunder methods") are designed to be called by the Python interpreter, not directly by the user.
  - For example, you should not call `my_object.__len__()`. Instead, you should use the built-in `len(my_object)`. This makes your code more readable and leverages Python’s design.

- **Implicit Calls**:
  - When you use Python’s built-in functions (like `len()`, `iter()`, `str()`), these functions internally call the corresponding special methods (`__len__`, `__iter__`, `__str__`).

#### 2. Optimization for Built-in Types

- **Performance Shortcut**:
  - For built-in types like `list`, `str`, `bytearray`, and extensions like NumPy arrays, Python takes shortcuts to enhance performance.
  - These built-in types are implemented in C and include a structure called `PyVarObject`, which contains an `ob_size` field that stores the number of items.
  - When you call `len()` on these types, Python directly accesses the `ob_size` field, making the operation much faster than invoking a method.

#### 3. Implicit Special Method Calls

- **Loop Example**:
  - Consider the loop `for i in x:`. This statement implicitly calls `iter(x)`, which in turn may call `x.__iter__()`. If `__iter__` is not available, it may use `x.__getitem__()`, as seen in the `FrenchDeck` example.

- **Avoid Direct Calls**:
  - Generally, you should avoid direct calls to special methods. Instead, use the related built-in functions. These functions not only call the special methods but also provide additional functionalities and optimizations.
  - The exception is `__init__`, which is frequently called directly in user code, especially to invoke the initializer of a superclass.

#### 4. Implementing Special Methods

- **Implementation Over Invocation**:
  - Focus more on implementing special methods in your custom classes rather than invoking them explicitly. This makes your classes integrate better with Python’s built-in functions and idioms.

- **Built-in Functions**:
  - Use built-in functions like `len()`, `iter()`, and `str()` instead of directly calling `__len__()`, `__iter__()`, and `__str__()`. These functions are optimized for performance, especially for built-in types.

### Summary

- **Use Special Methods Indirectly**: Special methods are designed to be called by the Python interpreter through built-in functions, not directly by your code.
- **Performance Optimizations**: Built-in types have optimizations that make operations like `len()` faster by directly accessing internal fields.
- **Implicit Method Calls**: Many special methods are called implicitly by Python’s syntax and built-in functions.
- **Focus on Implementation**: Implement special methods in your custom classes to enable them to work seamlessly with Python’s built-in features and idioms.
- **Use Built-in Functions**: Prefer using built-in functions (e.g., `len`, `iter`, `str`) over directly calling special methods, as they are optimized and provide additional functionalities.

By following these guidelines, you can write more efficient, readable, and Pythonic code.
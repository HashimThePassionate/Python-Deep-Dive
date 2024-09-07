# Variables and Other References in Python 🔗

In this section, we'll explore how Python programs access and manipulate data values through **references**. Understanding how variables and references work in Python is essential for effective programming.

## References in Python 🔍

- A **reference** is essentially a "name" that refers to a value (object) in Python.
- **References** can take various forms, including **variables**, **attributes**, and **items**.
- In Python, a reference itself does not have an intrinsic type; the type is determined by the object to which the reference is currently bound.
- A single reference can be bound to objects of different types over the course of a program's execution.

### Example:
```python
x = 42       # x is a reference to an integer object
x = "hello"  # x is now a reference to a string object
```

## Variables in Python 📝

- In Python, variables are **references** to objects. There are no explicit variable declarations as seen in some other programming languages.
- A variable comes into existence when it is **bound** to an object through a statement.
- Variables can be **rebound** to new objects, and they can also be **unbound**, meaning they no longer refer to any object.

### Binding and Rebinding

- **Binding**: The process of associating a reference (such as a variable) with an object.
- **Rebinding**: When a reference that is already bound to an object is associated with a new object.

### Example:
```python
x = 10    # Binding: x is now a reference to the integer 10
x = 20    # Rebinding: x is now a reference to the integer 20
```

- **Unbinding**: The process of removing the reference from a variable. This is done using the `del` statement.

### Example:
```python
x = 10    # x is bound to the integer 10
del x     # x is unbound, and the name x no longer exists
```

- When a reference is unbound, the object it was referring to may be cleaned up by Python's **garbage collector** if no other references exist to that object.

### Example:
```python
x = [1, 2, 3]  # x is bound to a list object
y = x          # y is also bound to the same list object
del x          # x is unbound, but the list object still exists because y refers to it
```

## Naming Variables 🏷️

- You can name a variable using any valid **identifier**, except for the 30-plus reserved keywords in Python.
- Variables can be **global** or **local**:
  - **Global Variable**: A variable that is accessible throughout the entire module. It is an attribute of the module object.
  - **Local Variable**: A variable that is accessible only within the function in which it is defined. It exists within the function’s local namespace.

### Example:
```python
global_var = "I am global"  # Global variable

def my_function():
    local_var = "I am local"  # Local variable
    print(local_var)

my_function()  # Outputs: I am local
print(global_var)  # Outputs: I am global
```

---

This section covered the concepts of **variables** and **references** in Python, including how they are bound, rebound, and unbound. Understanding these concepts is key to managing data and memory effectively in Python programs. 🧠

# Keywords in Python 🔑

## Table of Contents 📖

- [Keywords in Python 🔑](#keywords-in-python-)
  - [Table of Contents 📖](#table-of-contents-)
  - [What are Keywords? 🔍](#what-are-keywords-)
    - [Python v2 vs. Python v3 🧩](#python-v2-vs-python-v3-)
    - [Example:](#example)
  - [Categories of Keywords 📚](#categories-of-keywords-)
    - [1. **Simple Statements and Clauses** 📝](#1-simple-statements-and-clauses-)
    - [2. **Operators** ➗](#2-operators-)
  - [Python v2 Keywords 🔡](#python-v2-keywords-)
    - [Notable Points in Python v3 🆕](#notable-points-in-python-v3-)
    - [Python v3 Keywords 🔡](#python-v3-keywords-)
  - [Common Keywords and Their Uses 📋](#common-keywords-and-their-uses-)

---

In this section, we will discuss **keywords** in Python—special identifiers reserved for specific syntactic purposes. Understanding keywords is essential as they form the foundation of Python's syntax and structure.

## What are Keywords? 🔍

- **Keywords** are reserved words in Python that have special meanings and cannot be used as regular identifiers (like variable names or function names).
- Python's keywords consist only of **lowercase letters**.

### Python v2 vs. Python v3 🧩

- **Python v2** has **31 keywords**.
- **Python v3** has **35 keywords**.

### Example:
```python
# Keywords that cannot be used as identifiers
if = 10  # ❌ Invalid: 'if' is a keyword
def = 20  # ❌ Invalid: 'def' is a keyword
```

## Categories of Keywords 📚

### 1. **Simple Statements and Clauses** 📝
- Some keywords begin simple statements or clauses within compound statements.

### 2. **Operators** ➗
- Other keywords serve as operators within expressions.

## Python v2 Keywords 🔡

In Python v2, the keywords include:

```plaintext
and       continue   except   global    lambda   raise     yield
as        def        exec     if        not      return
assert    del        finally  import    or       try
break     elif       for      in        pass     while
class     else       from     is        print    with
```

### Notable Points in Python v3 🆕
- In **Python v3**:
  - `exec` and `print` are no longer keywords. They were statements in Python v2 but are now functions in Python v3.
  - To use the `print` function in Python v2, you can start your source file with:
    ```python
    from __future__ import print_function
    ```
  - **New keywords** in Python v3 include `False`, `None`, `True`, and `nonlocal`.
    - `False`, `None`, and `True` were built-in constants in Python v2, but they were not technically keywords.
  - **Additional Keywords** in Python v3 include:
    - `async` and `await`: Used for asynchronous programming.
  
### Python v3 Keywords 🔡

In Python v3, the updated list of keywords includes:

```plaintext
and       as         assert    async     await    break
class     continue   def       del       elif     else
except    False      finally   for       from     global
if        import     in        is        lambda   None
nonlocal  not        or        pass      raise    return
True      try        while     with      yield
```
## Common Keywords and Their Uses 📋

| **Keyword**    | **Description**                                                   | **Code Example**                                                                                          |
|----------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `False`, `True`| Data values from the data type Boolean                             | `False == (1 > 2)`<br>`True == (2 > 1)`                                                                    |
| `and`, `or`, `not`| Logical operators:<br>- `(x and y)` → both x and y must be True<br>- `(x or y)` → either x or y must be True<br>- `(not x)` → x must be false | `x, y = True, False`<br>`(x or y) == True  # True`<br>`(x and y) == False  # True`<br>`(not y) == True  # True`|
| `break`        | Ends loop prematurely                                             | `while(True):`<br>`   break  # no infinite loop`<br>`print("hello world")`                                 |
| `continue`     | Finishes current loop iteration                                   | `while(True):`<br>`   continue`<br>`   print("43")  # dead code`                                           |
| `class`, `def` | `class` defines a new class.<br>`def` defines a new function or method.| `class Beer:`<br>`   def __init__(self):`<br>`       self.content = 1.0`<br>`   def drink(self):`<br>`       self.content = 0.0`<br>`becks = Beer()`<br>`becks.drink()`<br>`# empty beer bottle`|
| `if`, `elif`, `else` | Conditional program execution: program starts with `if`, tries `elif`, and ends with `else`.| `x = int(input("your val: "))`<br>`if x > 3:`<br>`   print("Big")`<br>`elif x == 3:`<br>`   print("Medium")`<br>`else:`<br>`   print("Small")`|
| `for`, `while` | Looping constructs: `for` loop iterates over a sequence, `while` continues as long as the condition is true. | `for i in [0, 1, 2]:`<br>`   print(i)`<br>`j = 0`<br>`while j < 3:`<br>`   print(j)`<br>`   j += 1`         |
| `in`           | Checks whether an element is in a sequence                        | `42 in [2, 39, 42]  # True`                                                                                |
| `is`           | Checks whether two references point to the same object            | `y = x = 3`<br>`x is y  # True`<br>`[3] is [3]  # False`                                                   |
| `None`         | Represents a null value or absence of value                       | `def f():`<br>`   x = 2`<br>`f() is None  # True`                                                          |
| `lambda`       | Defines a small anonymous function                                | `(lambda x: x + 3)(3)  # returns 6`                                                                        |
| `return`       | Ends the execution of a function and optionally returns a value   | `def incrementor(x):`<br>`   return x + 1`<br>`incrementor(4)  # returns 5`                                |

---

This section provided an overview of **keywords** in Python and their specific uses. Keywords are fundamental building blocks of Python syntax, and knowing them is key to mastering the language. 🚀


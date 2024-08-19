# Keywords in Python 🔑

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

---

This section provided an overview of **keywords** in Python, highlighting their importance and differences between Python v2 and v3. We also covered the addition of `async` and `await` in Python v3, which are crucial for asynchronous programming. Understanding keywords is crucial for writing syntactically correct and functional Python code. 🧠


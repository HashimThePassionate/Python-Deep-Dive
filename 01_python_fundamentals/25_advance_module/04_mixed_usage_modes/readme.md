# 📚 **Mixed Usage Modes** 🐍

In Python, modules can serve **dual purposes**: they can be used as libraries that other programs import, or as standalone programs that run directly. The secret to enabling this flexibility lies in the special `__name__` variable. This section will explore how `__name__` works, how to leverage it to create dual-mode modules, and provide practical real-world examples.


## **Table of Contents** 📖

- [📚 **Mixed Usage Modes** 🐍](#-mixed-usage-modes-)
  - [**Table of Contents** 📖](#table-of-contents-)
  - [**Introduction** 📚](#introduction-)
  - [**Understanding `__name__` and `__main__`** 🧩](#understanding-__name__-and-__main__-)
    - [**How It Works**](#how-it-works)
  - [**Practical Examples**](#practical-examples)
    - [**Example 1: Running Code Conditionally** 🏃‍♂️](#example-1-running-code-conditionally-️)
    - [**Example 2: Creating a Utility Library** 📦](#example-2-creating-a-utility-library-)
  - [**Real-World Scenario**](#real-world-scenario)
    - [**Scenario: Utility for Text Formatting** 📝](#scenario-utility-for-text-formatting-)
    - [**Code Implementation**](#code-implementation)
    - [**Running the Utility**](#running-the-utility)
  - [**Benefits of Using `__name__` Checks** 🏆](#benefits-of-using-__name__-checks-)
  - [**Best Practices** 🛠️](#best-practices-️)
  - [**Summary** 📜](#summary-)


## **Introduction** 📚

Python’s `__name__` variable allows you to write modules that can be used as **standalone programs** or **imported libraries**. This is achieved by checking if `__name__` equals `"__main__"`. This technique is fundamental to writing reusable and testable Python code, and it is a pattern you will encounter frequently in Python projects.

## **Understanding `__name__` and `__main__`** 🧩

### **How It Works**

- When a Python script is **run directly**, its `__name__` variable is set to `"__main__"`. This allows the script to detect that it is being executed as the main program.
- When a Python script is **imported as a module**, its `__name__` variable is set to the module’s name (e.g., `"mymodule"`).

This difference enables you to write code that **behaves differently** depending on whether it is run or imported. The standard pattern is:
```python
if __name__ == "__main__":
    # Code here will only run if this file is executed directly
    print("This script is running as the main program")
else:
    # Code here will only run if this file is imported as a module
    print("This script is imported as a module")
```


## **Practical Examples**

### **Example 1: Running Code Conditionally** 🏃‍♂️

Let's say you have a Python file named `greetings.py`:
```python
# File: greetings.py

def say_hello():
    print("Hello, World!")

if __name__ == "__main__":
    # This will only run if the script is executed directly
    say_hello()
```

**Usage**:
- **Run Directly**: `python greetings.py` will output:
  ```
  Hello, World!
  ```
- **Import**: If imported using `import greetings`, it will not run the `say_hello` function unless explicitly called.

### **Example 2: Creating a Utility Library** 📦

```python
# File: calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # Run tests when executed directly
    print("Testing calculator functions:")
    print("3 + 5 =", add(3, 5))
    print("10 - 4 =", subtract(10, 4))
```

**Output When Run Directly**:
```
Testing calculator functions:
3 + 5 = 8
10 - 4 = 6
```

**Usage as a Module**:
```python
# Another script or interactive shell
from calculator import add
result = add(7, 3)
print("7 + 3 =", result)
```

**Output**:
```
7 + 3 = 10
```


## **Real-World Scenario**

### **Scenario: Utility for Text Formatting** 📝

Suppose you are building a **utility script** to format numbers with commas (e.g., `1,000,000`) and format currency. You want this utility to be usable as both a **command-line tool** and an **importable module**.

### **Code Implementation**

```python
# File: text_formatter.py

def add_commas(number):
    return "{:,}".format(number)

def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:,.2f}"

if __name__ == "__main__":
    import sys
    # Run tests or process command-line arguments
    if len(sys.argv) > 1:
        num = float(sys.argv[1])
        print("Formatted Number:", add_commas(num))
        print("Formatted Currency:", format_currency(num))
    else:
        print("Usage: python text_formatter.py <number>")
        print("Example: python text_formatter.py 1234567.89")
```

### **Running the Utility**

- **Command Line**:
  ```
  python text_formatter.py 1234567.89
  ```
  **Output**:
  ```
  Formatted Number: 1,234,567.89
  Formatted Currency: $1,234,567.89
  ```

- **As a Module**:
  ```python
  from text_formatter import add_commas, format_currency

  print(add_commas(987654321))
  print(format_currency(987654321, "€"))
  ```
  **Output**:
  ```
  987,654,321
  €987,654,321.00
  ```

By using `if __name__ == "__main__":`, you allow the script to function both as a **command-line tool** and an **importable library**, making the code **reusable** and **flexible**.


## **Benefits of Using `__name__` Checks** 🏆

1. **Code Reusability**:
   - Write code once and use it in different scenarios, like running as a script or importing as a library.
  
2. **Efficient Testing**:
   - Include **self-test code** in the module, which runs only when the script is executed directly. This avoids unintended execution during imports.
  
3. **Cleaner Code**:
   - Separate code intended for **execution** and **importing**, leading to **more organized** and **maintainable** projects.


## **Best Practices** 🛠️

1. **Keep Tests in `__main__` Section**:
   - Place self-test code or command-line interfaces within the `if __name__ == "__main__":` block to avoid unintended execution during imports.

2. **Consistent Usage**:
   - Always use this pattern when creating modules. It’s a **standard convention** in Python programming, and most developers expect this behavior.

3. **Readable and Clean Code**:
   - Clearly separate **function definitions** and **execution logic**. This makes the module more **understandable** and **easier to debug**.


## **Summary** 📜

In this section, we explored how to use the `__name__` variable to make Python modules function as both **importable libraries** and **standalone scripts**:
- The `__name__` variable determines whether a script is **run directly** or **imported**.
- The `if __name__ == "__main__":` pattern allows you to write **dual-mode code**, which is flexible and reusable.
- **Practical examples** showed how to use this feature for testing, creating utilities, and building command-line tools.
- **Best practices** were discussed to help you write clean, modular, and maintainable Python code.

By adopting this pattern, you ensure that your modules are **versatile** and **user-friendly**, making them easier to integrate into other projects or use as standalone tools.
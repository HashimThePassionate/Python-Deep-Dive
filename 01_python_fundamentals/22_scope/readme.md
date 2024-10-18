# 📝 **Scope**

## **Explanation**:
In Python, **scope** refers to the part of the program where a **variable** can be **accessed** or **modified**. Understanding scope is essential when writing code, especially when working with **functions**, because it affects how variables are created, accessed, and maintained.

## 📋 **Key Concepts of Scope**:
1. **Local Scope**:
   - Variables **defined within a function**.
   - Only **accessible** within that function.
2. **Nonlocal Scope**:
   - Variables **defined in an enclosing function**.
   - **Accessible** in **nested functions** but **not** in the **outermost scope**.
3. **Global Scope**:
   - Variables **defined outside of all functions**.
   - **Accessible** from **anywhere** within the file.

## 📋 **Understanding Lexical Scoping**:
- **Lexical scoping** (or **static scoping**) means that the **location** of a variable’s assignment in the **source code** determines its **scope**.
- For example, a variable defined **inside a function** is **local** to that function, even if that function is called from another part of the program.

## 📂 **Examples of Different Scopes**

###**1. Local Scope: Variables Inside a Function**
Variables defined within a function are **local** to that function.

```python
def greet():
    name = "Muhammad Hashim"  # Local variable
    print(f"Hello, {name}!")

greet()  # Output: Hello, Muhammad Hashim
print(name)  # Error: name is not defined
```

###**Explanation**:
- **`name`** is a **local variable** defined inside the `greet()` function.
- It is only accessible within the `greet()` function. Trying to access it **outside** the function will result in an **error** because **`name` does not exist** in the global scope.

###**2. Global Scope: Variables Defined Outside Functions**
Variables defined **outside** of all functions are **global** and can be accessed anywhere.

```python
name = "Muhammad Hashim"  # Global variable

def greet():
    print(f"Hello, {name}!")

greet()  # Output: Hello, Muhammad Hashim
print(name)  # Output: Muhammad Hashim
```

###**Explanation**:
- The **`name`** variable is defined **outside** any function, so it is **global**.
- Both the `greet()` function and the **main program** can access it.

###**3. Local and Global Variables with the Same Name**
Even if a local and global variable have the **same name**, they are treated as **different variables**.

```python
name = "Muhammad Hashim"  # Global variable

def greet():
    name = "Hashim"  # Local variable
    print(f"Hello, {name}!")

greet()  # Output: Hello, Hashim
print(name)  # Output: Muhammad Hashim
```

###**Explanation**:
- The **`name`** inside `greet()` is **local** to the function and **different** from the **global `name`**.
- When **`greet()`** is called, it prints **"Hashim"** (the local `name`). Outside of `greet()`, it prints **"Muhammad Hashim"** (the global `name`).

## 📂 **Understanding Nonlocal Scope with Nested Functions**

###**4. Nonlocal Variables: Variables in an Enclosing Function**
If you have **nested functions**, a variable defined in the **enclosing function** is **nonlocal** to the nested function.

```python
def outer():
    name = "Hashim"  # Nonlocal variable

    def inner():
        nonlocal name
        name = "Muhammad Hashim"
        print(f"Inside inner: {name}")

    inner()
    print(f"Inside outer: {name}")

outer()
```

###**Output**:
```
Inside inner: Muhammad Hashim
Inside outer: Muhammad Hashim
```

###**Explanation**:
- The `name` defined inside `outer()` is **nonlocal** because it is **enclosing** for `inner()`.
- By using **`nonlocal`**, the `inner()` function can **modify** the **`name`** variable from `outer()`. Without **`nonlocal`**, a new **local variable** would have been created inside `inner()`.

## 📋 **Important Rules**:
1. **Names assigned inside a `def`** (function) can **only be seen** by the code **within that `def`**. 
2. **Names assigned inside a `def`** do **not clash** with variables **outside** the `def`, even if the **same names** are used elsewhere. 
3. The **scope** of a variable is determined by **where** it is **assigned** in your code.

## 📂 **Example: Local, Nonlocal, and Global Variables in Action**

```python
X = "Global X"  # Global variable

def outer():
    X = "Outer X"  # Nonlocal variable

    def inner():
        nonlocal X  # Refers to the nonlocal X in `outer`
        X = "Inner X"  # Local to inner, modifies outer's X
        print(f"Inside inner: {X}")

    inner()
    print(f"Inside outer: {X}")

outer()
print(f"Outside all: {X}")
```

###**Output**:
```
Inside inner: Inner X
Inside outer: Inner X
Outside all: Global X
```

###**Explanation**:
- **Global X** is defined at the **module level**.
- **`X = "Outer X"`** is **nonlocal** because it's inside the `outer()` function, and it **can be accessed** by `inner()` if **`nonlocal`** is used.
- **`inner()`** modifies **nonlocal X** because **`nonlocal`** allows it to change the variable defined in `outer()`.

## 📋 **Key Points to Remember**:

1. **Local Variables**:
   - Declared **inside a function**.
   - Accessible **only within that function**.

2. **Nonlocal Variables**:
   - Declared in an **enclosing function**.
   - Accessible **inside nested functions**, but not in the **global scope**.

3. **Global Variables**:
   - Declared **outside of all functions**.
   - Accessible **anywhere** in the program file.

4. **Lexical Scoping** ensures that **variable access** is determined by **where** the **variable** is **declared**, not **where** it is **used**.

--- 

## 🔄 **The LEGB Rule**
Python follows the **LEGB rule** to resolve variable names:
1. **Local (L)**: Variables defined **inside the current function**.
2. **Enclosing (E)**: Variables in the **outer function** (if the current function is nested).
3. **Global (G)**: Variables defined at the **module level**.
4. **Built-in (B)**: Predefined Python functions and constants.

### 📂 **Example: LEGB Rule in Action**

```python
# Global Scope
name = "Muhammad Hashim"  # Global variable

def outer():
    name = "Hashim"  # Enclosing (Nonlocal) variable

    def inner():
        name = "Local Hashim"  # Local variable
        print(f"Inside inner: {name}")

    inner()
    print(f"Inside outer: {name}")

outer()
print(f"Global scope: {name}")
```

#### **Output**:
```
Inside inner: Local Hashim
Inside outer: Hashim
Global scope: Muhammad Hashim
```

#### **Explanation**:
1. **`inner()`** function prints **`"Local Hashim"`** because **`name`** is a **local variable** inside `inner`.
2. **`outer()`** function prints **`"Hashim"`** because **`name`** refers to the **enclosing nonlocal variable** in `outer`.
3. **Global scope** prints **`"Muhammad Hashim"`**, the **global variable**.

### 📋 **Detailed Rules and Use Cases**:

1. **Assignments Create Local Variables**:
   - When you **assign** a variable inside a function, Python treats it as **local** unless explicitly declared otherwise.
   - **Example**:
     ```python
     def test():
         x = 10  # Local variable
         print(x)

     test()
     print(x)  # Error: x is not defined (outside local scope)
     ```

2. **Using `global`**:
   - The **`global`** keyword tells Python to **use** a **global variable** instead of creating a new **local variable**.
   - **Example**:
     ```python
     count = 0  # Global variable

     def increment():
         global count
         count += 1

     increment()
     print(count)  # Output: 1
     ```
   - **Explanation**: The `global` keyword allows `increment` to modify the `count` variable globally.

3. **Using `nonlocal`**:
   - The **`nonlocal`** keyword is used to refer to **enclosing variables** from the outer function.
   - **Example**:
     ```python
     def outer():
         count = 0

         def inner():
             nonlocal count
             count += 1
             print(f"Inner count: {count}")

         inner()
         print(f"Outer count: {count}")

     outer()
     # Output:
     # Inner count: 1
     # Outer count: 1
     ```
   - **Explanation**: The `nonlocal` keyword allows `inner` to modify `count` in `outer`, so the change is visible in both scopes.

### 📂 **Advanced Example Demonstrating Scope**:

```python
# Global Scope
X = 99  # Global variable

def func(Y):  # Y is a local variable
    # Local Scope
    Z = X + Y  # X is global, Y and Z are local
    return Z

result = func(1)  # func is called with Y=1
print(result)  # Output: 100
```

#### **Explanation**:
1. **Global Scope**:
   - **`X`** is **global** because it's defined at the **module level**.
   - **`func`** is also global, available throughout the module.
2. **Local Scope**:
   - **`Y`** and **`Z`** are **local** to **`func()`**, created and used only when **`func()`** runs.
3. **Variable References**:
   - When **`Z = X + Y`** is executed, Python uses the **LEGB** rule:
     - **`X`** is found in the **global scope**.
     - **`Y`** is found in the **local scope**.
     - **`Z`** is assigned locally and can only be accessed **within** `func()`.

--- 

## 📝 **Understanding Built-in Scope and Redefining Names in Python**

In Python, there are several built-in functions, constants, and modules that you can use without importing anything. These are available because they reside in the **built-in scope**. Let's discuss how Python handles the built-in scope, what it means to redefine these built-ins, and some best practices to avoid common pitfalls.

---

### 📋 **What is Built-in Scope?**
The **built-in scope** in Python consists of names that are predefined and always available. This includes:
- Functions like `print()`, `len()`, `open()`
- Constants like `True`, `False`, `None`
- Exceptions like `ValueError`, `TypeError`

Python will check the **built-in scope** last when it tries to resolve a variable name, following the **LEGB rule**:
1. **Local**: Inside the current function.
2. **Enclosing**: In the local scope of any enclosing function.
3. **Global**: At the module level.
4. **Built-in**: Predefined names.

### 📋 **How to View All Built-in Names**
To get a list of all built-in names in Python, you can use the **`dir()`** function on the `builtins` module:
```python
import builtins
print(dir(builtins))
```

#### **Example Output**:
```
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', ... ]
```
This will print a list of all available **functions**, **exceptions**, and **constants** in the built-in scope.

---

### 🔄 **Redefining Built-in Names: Be Careful!**
Python allows you to **redefine built-in names**, but doing so can lead to unexpected behavior. Here’s why:
- If you create a variable named `open`, you **hide** the built-in `open()` function.
- Once overridden, you can't use the original `open()` function unless you specifically reference it from the `builtins` module.

#### 📂 **Example: Redefining a Built-in Name**
```python
# Redefine the built-in open function
open = "This is not a function anymore!"  # Overrides the built-in open
print(open)  # Output: This is not a function anymore!

# Now, try to use open() to open a file:
try:
    open("example.txt", "r")
except TypeError as e:
    print(f"Error: {e}")
```

#### **Output**:
```
This is not a function anymore!
Error: 'str' object is not callable
```

#### **Explanation**:
1. **`open`** is redefined as a **string**. This hides the built-in **`open()`** function within the local or global scope.
2. Trying to use **`open()`** after redefinition causes a **TypeError** because `open` is no longer a function; it's a string.

### 📋 **How to Safely Access Built-ins After Overriding**
If you accidentally override a built-in name, you can still access the original function using the **`builtins`** module:
```python
import builtins

# Safely using built-ins after overriding
open = "Overridden Open"  # Overrides the built-in open
print(open)  # Prints the string

# Access the original built-in open
with builtins.open("example.txt", "w") as file:
    file.write("This is safe!")
```
- **Explanation**: The `builtins.open` lets you safely access the original `open` function even after it’s been redefined locally.

### 📋 **Best Practices to Avoid Overriding Built-ins**
1. **Choose unique variable names** that do not clash with built-ins.
2. **Avoid using built-in names** such as `list`, `str`, `sum`, etc., for your variables.
3. **Restore built-in functionality** if overridden by using `del`:
   ```python
   list = [1, 2, 3]  # Overrides built-in list function
   print(list)  # Output: [1, 2, 3]
   del list  # Remove override
   print(list("123"))  # Built-in list function works again
   ```

### 📝 **Example: Safely Overriding and Using Built-in Functions**
```python
# Safely using built-ins after overriding
import builtins

def process_data():
    len = "Overridden Length"  # Override the built-in len function
    print(len)  # Prints the string
    print(builtins.len([1, 2, 3, 4]))  # Safely use the original len function

process_data()
```

#### **Output**:
```
Overridden Length
4
```

--- 

## 📝 **Understanding Global Variables and Best Practices in Python**

When programming in Python, it’s crucial to manage how your functions handle variables to avoid common pitfalls. While global variables can be useful, overreliance on them may lead to bugs and difficult-to-maintain code. Let’s explore the concept of global variables, why we should minimize their use, and the preferred way of passing data using function arguments and return values. We'll also see practical examples featuring Muhammad Hashim.

### 📋 **What Are Global Variables?**
- **Global variables** are defined at the top level of a script or module, making them accessible throughout the entire file.
- These variables can be read or modified by any function within the same module, leading to potential issues when multiple functions modify them.

#### 📂 **Example of a Global Variable**
```python
age = 25  # Global variable

def print_age():
    print(f"Muhammad Hashim is {age} years old.")  # Accessing global variable inside a function

print_age()  # Output: Muhammad Hashim is 25 years old.
```

- **Explanation**: The variable `age` is defined globally, making it accessible to `print_age()`. However, if `age` were to be modified elsewhere, it could cause unintended side effects.

### 📋 **The `global` Statement**
To modify a global variable inside a function, you need to use the **`global`** statement. Without it, Python treats the variable as local.

#### 📂 **Example of Modifying a Global Variable**
```python
experience = 3  # Global variable representing years of experience

def update_experience():
    global experience  # Declare as global
    experience = 5  # Modify the global variable

print("Before:", experience)  # Output: 3
update_experience()
print("After:", experience)  # Output: 5
```

- **Explanation**: The `global` statement allows `update_experience()` to modify the global variable `experience`. However, overusing global variables can lead to harder-to-debug code.

### 📋 **Why Minimize Global Variables?**
Global variables can cause several issues:
1. **Hard to Debug**: Changes in one part of the program can affect other parts unexpectedly.
2. **Difficult to Reuse Code**: Functions relying on global variables are harder to reuse because they depend on data defined outside their scope.
3. **Unintended Overwrites**: Accidentally modifying a global variable can lead to unexpected behavior.

#### **Best Practice**: Use **function arguments** and **return values** instead of global variables. This leads to cleaner and more maintainable code.

### 📋 **Preferred Approach: Use Function Arguments & Return Values**
Instead of relying on global variables, a better approach is to use **function arguments** to pass data into functions and **return values** to get data out of functions. This ensures that each function is self-contained and predictable.

#### ✅ **Better Practice: Passing Arguments & Using Return Values**
```python
# Recommended
def calculate_age(birth_year):
    current_year = 2024
    return current_year - birth_year

muhammad_age = calculate_age(1999)
print(f"Muhammad Hashim is {muhammad_age} years old.")  # Output: Muhammad Hashim is 25 years old.
```

- **Explanation**: Here, `birth_year` is passed as an argument to `calculate_age`, making the function self-contained and flexible. The function doesn’t rely on any external data, and its behavior is predictable.

### 📋 **Combining Concepts: Managing State Without Globals**
Suppose you want to calculate Muhammad Hashim's yearly savings based on income and expenses. Instead of using global variables, let’s see how you can write clean and modular code using function arguments.

#### 🚫 **Avoid Using Globals:**
```python
# Not recommended
monthly_income = 5000
monthly_expenses = 3000

def calculate_monthly_savings():
    return monthly_income - monthly_expenses

def predict_yearly_savings():
    return calculate_monthly_savings() * 12

print(f"Predicted Yearly Savings: {predict_yearly_savings()}")  # Output: 24000
```

- **Explanation**: The functions depend on global variables, making them harder to reuse or test with different inputs.

#### ✅ **Better Practice: Pass as Arguments & Return Values**
```python
# Recommended
def calculate_monthly_savings(income, expenses):
    return income - expenses

def predict_yearly_savings(income, expenses):
    monthly_savings = calculate_monthly_savings(income, expenses)
    return monthly_savings * 12

income = 5000
expenses = 3000
yearly_savings = predict_yearly_savings(income, expenses)

print(f"Predicted Yearly Savings: {yearly_savings}")  # Output: 24000
```

- **Explanation**: By passing `income` and `expenses` as arguments, the functions are now independent of any external data. They can be reused or tested with different inputs without any changes to the global state.

### 📝 **Understanding Global Variables and Best Practices in Python (Using Muhammad Hashim)**

Global variables can be powerful but should be used carefully to maintain clean, efficient, and error-free code. Let’s explore how they work, their best practices, and how to use them effectively in Python with examples featuring Muhammad Hashim.

---

### 📋 **What Are Global Variables?**
- **Global variables** are defined at the top level of a module or script, making them accessible throughout the entire file. They allow data to be shared across different functions.
- Python’s **LEGB (Local, Enclosing, Global, Built-in)** rule determines how variables are searched for. Global variables fall under the **Global (G)** scope.

#### 📂 **Example of a Global Variable**
```python
age = 25  # Global variable

def print_age():
    print(f"Muhammad Hashim is {age} years old.")  # Accessing global variable inside a function
```

### 📋 **Global Variables Across Multiple Files**
You can access global variables from other modules, but this should be done cautiously.

#### 📂 **Example of Accessing Globals from Another File**
- **File 1: `muhammad.py`**
    ```python
    city = "Lahore"  # Global variable in muhammad.py
    ```

- **File 2: `details.py`**
    ```python
    import muhammad

    print(f"Muhammad Hashim lives in {muhammad.city}.")  # Access global variable from muhammad.py
    muhammad.city = "Islamabad"  # Modify global variable from muhammad.py
    ```

- **Explanation**: When `details.py` imports `muhammad`, it can access and modify `city`. This can lead to **cross-file dependencies**, which may make the code difficult to manage.

### 📋 **Better Practice: Use Accessor Functions**
Instead of directly modifying global variables, it's better to manage changes through functions. This makes the code clearer and easier to maintain.

#### 📂 **Example with Accessor Functions**
- **File 1: `muhammad.py`**
    ```python
    skill_level = "Intermediate"

    def set_skill_level(level):
        global skill_level
        skill_level = level  # Modify global variable explicitly

    def get_skill_level():
        return skill_level
    ```

- **File 2: `details.py`**
    ```python
    import muhammad

    print(f"Muhammad Hashim's skill level: {muhammad.get_skill_level()}.")  # Output: Intermediate
    muhammad.set_skill_level("Expert")  # Modify using accessor function
    print(f"Updated skill level: {muhammad.get_skill_level()}.")  # Output: Expert
    ```

- **Explanation**: Using `set_skill_level()` and `get_skill_level()` makes it explicit that any changes happen through controlled functions.

### 📋 **Global Variables in Multithreading**
Global variables can be used as **shared memory** between threads. When multiple threads access and modify the same global variable, it may lead to **race conditions**. Always use **thread synchronization** (e.g., `threading.Lock`) when working with threads and global variables.

### 📋 **Alternative Approach: Using `sys.modules` to Access Globals**
Another way to manage global variables is to access them as module attributes. Here’s an example that demonstrates this:

#### 📂 **Example: Using `sys.modules`**
- **File: `hashim.py`**
    ```python
    import sys

    projects_completed = 15  # Global variable

    def increment_projects():
        sys.modules[__name__].projects_completed += 1  # Access and modify global variable
    ```

- **Explanation**: Using `sys.modules` lets you access the module itself, which allows for modifying global variables explicitly.

### 📋 **Detailed Example: Managing Global Configuration with Proper Techniques**
```python
# File: config.py
settings = {
    "name": "Muhammad Hashim",
    "profession": "Software Engineer",
    "projects": 10
}

def update_settings(key, value):
    global settings
    if key in settings:
        settings[key] = value
    else:
        raise KeyError("Key does not exist in settings")

# File: app.py
from config import settings, update_settings

print("Before Update:", settings)
update_settings("projects", 12)
print("After Update:", settings)
```

#### **Output**:
```
Before Update: {'name': 'Muhammad Hashim', 'profession': 'Software Engineer', 'projects': 10}
After Update: {'name': 'Muhammad Hashim', 'profession': 'Software Engineer', 'projects': 12}
```

- **Explanation**: This approach of managing settings through functions allows clear, controlled updates and avoids accidental modifications.


---

### 📋 **The Concept of Nested Functions and Enclosing Scope**

A **nested function** is a function defined inside another function. This creates an **enclosing scope**—the outer function's local variables can be accessed by the inner function.

#### ✅ **Example: Nested Function Accessing Enclosing Scope**
```python
def greet():
    message = "Hello, Muhammad Hashim!"  # Enclosing scope

    def print_message():
        print(message)  # Accessing 'message' from enclosing scope

    print_message()

greet()  # Output: Hello, Muhammad Hashim!
```
- **Explanation**: The inner function `print_message` can access `message`, even though `message` is not defined within it. This is due to the **Enclosing scope** created by `greet()`.

### 📋 **The `global` Keyword: Access and Modify Global Variables**

The **`global`** keyword allows you to modify a global variable from within a function. Without declaring it as `global`, Python treats it as a local variable.

#### 🚫 **Example: Without `global` (Incorrect Usage)**
```python
counter = 0

def increment():
    counter += 1  # Error: Python treats 'counter' as local, which is not yet assigned

increment()  # Raises UnboundLocalError
```

#### ✅ **Correct Usage with `global`**
```python
counter = 0  # Global variable

def increment():
    global counter  # Declaring 'counter' as global
    counter += 1

increment()
print(counter)  # Output: 1
```
- **Explanation**: Using `global` tells Python that the `counter` inside `increment()` refers to the global `counter`.

### 📋 **The `nonlocal` Keyword: Modify Variables in Enclosing Scopes (Python 3.x)**

The **`nonlocal`** keyword is used to modify variables in the nearest **enclosing scope**. This allows inner functions to change variables defined in their enclosing function.

#### ✅ **Example: Using `nonlocal`**
```python
def outer():
    age = 25  # Enclosing scope

    def inner():
        nonlocal age  # Declaring 'age' as nonlocal
        age = 30  # Modify the enclosing 'age'
    
    inner()
    print(f"Muhammad Hashim's updated age: {age}")

outer()  # Output: Muhammad Hashim's updated age: 30
```
- **Explanation**: By declaring `age` as `nonlocal`, the inner function can modify `age` in `outer()`.

### 📋 **Factory Functions and Closures**

**Closures** are nested functions that "remember" values from their enclosing scopes even after the outer function has completed execution. This can be a useful way to create functions with customized behavior.

#### ✅ **Example: Creating a Closure**
```python
def multiplier(factor):
    def multiply(number):
        return number * factor  # 'factor' is remembered from enclosing scope
    
    return multiply

double = multiplier(2)
print(double(5))  # Output: 10

triple = multiplier(3)
print(triple(5))  # Output: 15
```
- **Explanation**: 
  - `double` and `triple` are closures created by `multiplier(2)` and `multiplier(3)`, respectively. 
  - Each closure "remembers" its own `factor`, allowing you to reuse `multiplier` flexibly.

### 📋 **Loop Variables and the Default Argument Trap**

If you create functions within a loop, be cautious—loop variables may not behave as you expect. To avoid unexpected behavior, use **default arguments**.

#### 🚫 **Incorrect Example: Loop Variables in Closures**
```python
def create_actions():
    actions = []
    for i in range(3):
        actions.append(lambda: print(i))  # Each lambda will reference the same 'i'
    return actions

actions = create_actions()
actions[0]()  # Output: 2
actions[1]()  # Output: 2
actions[2]()  # Output: 2
```
- **Problem**: Each lambda references `i` as it was when the loop ended, which is `2`.

#### ✅ **Correct Usage: Preserve Loop Variable with Default Arguments**
```python
def create_actions():
    actions = []
    for i in range(3):
        actions.append(lambda i=i: print(i))  # Capture 'i' at each iteration
    return actions

actions = create_actions()
actions[0]()  # Output: 0
actions[1]()  # Output: 1
actions[2]()  # Output: 2
```
- **Explanation**: By setting `i=i` in the lambda, each function captures its own value of `i`.

---
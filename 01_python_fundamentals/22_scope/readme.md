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
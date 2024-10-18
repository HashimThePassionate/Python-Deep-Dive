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


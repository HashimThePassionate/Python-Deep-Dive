# **Overview of Data Types and Objects in Python** 📌

## 🔍 Introduction

When solving a problem using a computer program, we first design an **algorithm** —a **step-by-step** set of instructions that a computer follows to reach a solution. Algorithms are implemented in any ***programming languages***, and their efficiency heavily depends on how ***data is stored in memory***.

The way data is **structured and stored** impacts the performance and speed of a program. Choosing the right **data types** ensures that memory usage is optimized, and the program runs efficiently. In Python, variables act as **containers** that store different types of values.

---

## 🏗 Understanding Data Types in Python

Python is a **dynamically typed language**, meaning that variables **do not need explicit type declarations**. The interpreter assigns the data type **at runtime**.

### 🏷 What Are Data Types?

A **data type** defines the nature of the values that can be stored in a variable. Some common data types in Python include:

| Data Type | Description                                       |
| --------- | ------------------------------------------------- |
| `int`     | Stores integer values (whole numbers)             |
| `float`   | Stores real numbers (decimal values)              |
| `str`     | Stores sequences of characters (text)             |
| `complex` | Stores complex numbers (e.g., 3 + 4j)             |
| `bool`    | Stores Boolean values (`True` or `False`)         |
| `list`    | Stores an ordered collection of items (mutable)   |
| `tuple`   | Stores an ordered collection of items (immutable) |
| `dict`    | Stores key-value pairs                            |
| `set`     | Stores an unordered collection of unique items    |

---

## 🎯 Dynamic Typing in Python

Unlike other languages like C, C++, or Java, where **data types must be declared explicitly**, Python allows assigning values directly to variables without specifying their type. The **Python interpreter automatically infers** the data type.

### 🛠 Example: Checking Data Types

Let's see how Python dynamically assigns data types:

```python
p = "Hello World"
q = 10
r = 10.2

print(type(p))  # Output: <class 'str'>
print(type(q))  # Output: <class 'int'>
print(type(r))  # Output: <class 'float'>
print(type(12+31j))  # Output: <class 'complex'>
```

🔹 The `type()` function helps determine the type of a variable in Python.

---

## 🔄 Variable Reassignment in Python

Python allows **reassigning** variables with different data types.

### 🛠 Example: Changing Data Types

```python
var = 13.2  # Initially a float
print(var)
print(type(var))  # Output: <class 'float'>

var = "Now the type is string"  # Reassigned as a string
print(type(var))  # Output: <class 'str'>
```


<div align="center">
  <img src="./images/01.jpg" alt="" width="300px"/>

  **Figure 1.3**: Variable assignment

</div>


📌 Here, the same variable `var` initially holds a **float** value (`13.2`), but later, it is assigned a **string** value (`"Now the type is string"`). Python allows such **flexible variable reassignment** due to **dynamic typing**.

---

## 🔍 Understanding Objects in Python

In Python, **everything is an object**. When a variable is assigned a value, the interpreter creates an **object** of that data type and binds it to the variable.

### 🔄 How Python Handles Variable Assignment

1. The **Python interpreter creates an object** when a value is assigned to a variable.
2. The **variable acts as a reference** (or pointer) to that object.
3. If a variable is reassigned, it **points to a new object**, and the previous object may be discarded (garbage collected).

📌 Example:

```python
x = 42  # An integer object is created
x = 3.14  # Now, a float object is created and x points to it
```

🔹 Initially, `x` holds an **integer object** (`42`), but when reassigned to `3.14`, it now refers to a **float object** instead.

---


<div align="center">

# `New Section Basic Data Types`

</div>

# 📌 **Python Data Types**

## 📖 Introduction
Python is an **easy-to-learn, object-oriented** language with a rich set of built-in data types. These data types help developers store, manipulate, and process different kinds of data efficiently. Python's built-in types are categorized as follows:

### 🔹 Principal Built-in Data Types:
- **Numeric types**: `int`, `float`, `complex`
- **Boolean type**: `bool`
- **Sequence types**: `str` (string), `range`, `list`, `tuple`
- **Mapping type**: `dict` (dictionary)
- **Set types**: `set`, `frozenset`

To make things simpler, we will divide these into:
- **Basic Data Types**: Numeric, Boolean, and Sequence types
- **Complex Data Types**: Mapping and Set types

Each type will be explained in detail in subsequent sections. 🚀

---

## 🛠️ Basic Data Types
### 🔢 Numeric Data Types
Numeric data types store numerical values and include:

#### 1️⃣ Integer (`int`)
- Stores whole numbers, positive or negative, without a decimal point.
- Examples:
  ```python
  num1 = 45
  num2 = 1000
  num3 = -25
  print(type(num1))  # Output: <class 'int'>
  ```

#### 2️⃣ Float (`float`)
- Stores decimal numbers and floating-point values.
- Accurate up to **15 decimal places**.
- Examples:
  ```python
  pi = 3.14159
  price = 100.98
  print(type(pi))  # Output: <class 'float'>
  ```

#### 3️⃣ Complex (`complex`)
- Used to store **complex numbers** with a real and an imaginary part.
- The imaginary part is denoted by `j` (not `i` like in mathematics).
- Examples:
  ```python
  comp1 = 3.0 + 1.3j
  comp2 = 4.0j
  print(type(comp1))  # Output: <class 'complex'>
  ```

---

### 🔘 Boolean Data Type (`bool`)
The Boolean type represents **truth values**: `True` or `False`. It is used for decision-making and logic operations.

- Any **non-zero** value is `True`.
- `0` (zero) is `False`.
- Examples:
  ```python
  print(type(bool(22)))  # Output: <class 'bool'>
  print(type(True))      # Output: <class 'bool'>
  print(type(False))     # Output: <class 'bool'>
  ```

#### ✅ Using Boolean with Numeric Types
- The `bool()` function can be used to evaluate numeric values as `True` or `False`.
- Examples:
  ```python
  print(bool(False))  # Output: False
  val1 = 0
  print(bool(val1))   # Output: False
  val2 = 11
  print(bool(val2))   # Output: True
  val3 = -2.3
  print(bool(val3))   # Output: True
  ```

---

## 📌 Sequence Data Types
Sequence data types allow storing multiple values in an organized and efficient manner. Python provides four basic sequence types:
- **Strings (`str`)**
- **Range (`range`)**
- **Lists (`list`)**
- **Tuples (`tuple`)**

### 📜 Strings (`str`)
- A string is an **immutable** sequence of characters enclosed in single, double, or triple quotes.
- **Immutable** means that once a string is created, it **cannot** be changed.
- Triple-quoted strings allow multiline text.
- Examples:
  ```python
  str1 = 'Hello how are you'
  str2 = "Hello how are you"
  str3 = """multiline
  String"""
  print(str1)
  print(str2)
  print(str3)
  ```
  **Output:**
  ```
  Hello how are you
  Hello how are you
  multiline
  String
  ```
- **String Concatenation (`+`)**
  ```python
  f = 'data'
  s = 'structure'
  print(f + s)  # Output: datastructure
  print('Data ' + 'structure')  # Output: Data structure
  ```
- **String Repetition (`*`)**
  ```python
  st = 'data.'
  print(st * 3)  # Output: data.data.data.
  ```

---

### 🔢 Range (`range`)
- Represents an **immutable** sequence of numbers.
- Used primarily in loops.
- Syntax:
  ```python
  range(start, stop, step)
  ```
- Examples:
  ```python
  print(list(range(10)))  # [0, 1, 2, ..., 9]
  print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
  print(list(range(20, 10, -2)))  # [20, 18, 16, 14, 12]
  ```

---

### 📋 Lists (`list`)
- Stores multiple values, allowing duplicates and mixed data types.
- Lists are **mutable**, meaning elements can be modified.
- Syntax:
  ```python
  mylist = [10, "world", "world", 8]
  print(mylist[1])  # Output: world
  ```
- **Properties of Lists:**
  - **Ordered**: Elements maintain their defined order.
  - **Dynamic**: Can grow or shrink.
  - **Mixed Data Types**: Lists can contain numbers, strings, etc.
  - **Indexing & Slicing**: Supports positive and negative indexing.
  - **Mutable**: Elements can be modified.

#### 🔧 List Operations
- **Accessing Elements:**
  ```python
  a = ['data', 'structures', 'using', 'python']
  print(a[0])  # Output: data
  print(a[-1])  # Output: python
  print(a[1:3])  # Output: ['structures', 'using']
  ```
- **Modifying Elements:**
  ```python
  a[1] = 'and'
  print(a)  # Output: ['data', 'and', 'using', 'python']
  ```
- **List Operators:**
  ```python
  a = ['data', 'python']
  print(a + ['new', 'elements'])  # Concatenation
  print(a * 2)  # Replication
  print(len(a))  # Length
  ```

## 📊 Properties of Lists

| Property                  | Description                                                                                                  | Example                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **Ordered** ✅             | Lists maintain the order in which elements are added. The order remains **fixed** unless explicitly changed. | `[10, 12, 31, 14] == [14, 10, 31, 12] → False`                                      |
| **Dynamic** 🔄            | Lists can **grow or shrink** dynamically by adding or removing elements.                                     | `b = ['data', 'and', 'book']; b += [32]; del b[0]`                                  |
| **Heterogeneous** 🎭      | Lists can contain multiple data types, including numbers, strings, and booleans.                             | `['python', 31, False, 2.2]`                                                        |
| **Indexing & Slicing** 🔍 | Supports zero-based indexing, negative indexing, and slicing for retrieving elements.                        | `a[0] → 'data'`, `a[-1] → 'learning'`, `a[1:4] → ['structures', 'using', 'python']` |
| **Mutable** ✏️            | List elements can be modified using indexing and slicing.                                                    | `a[1] = 'new_value'`, `a[2:4] = [1, 2, 3]`                                          |
| **Operators** 🛠️         | Lists support `in`, `+`, `*`, `len()`, `min()`, `max()` operations.                                          | `a + ['new']`, `len(a)`, `min(a)`                                                   |

# **Membership, identity, and logical operations** 📋
Python supports membership, identity, and logical operators. Several data types in Python support them. In order to understand how these operators work, we’ll discuss each of these operations in this section.

# **Membership Operators**  🚀

## Introduction 📌

Membership operators in Python are used to ***validate the membership*** of an item within a sequence. A sequence can be a ***string, list, or tuple***. These operators help us determine whether a given value exists in the specified sequence or not.

Python provides **two membership operators**:

1. `in` 👉 Returns `True` if the value exists in the sequence, otherwise returns `False`.
2. `not in` 👉 Returns `True` if the value **does not** exist in the sequence, otherwise returns `False`.

---

## 1️⃣ `in` Operator 🔍

The `in` operator checks if an element exists in a sequence. If found, it returns **`True`**, otherwise, it returns **`False`**.

### Example:

```python
# Python program to check if an item exists in another list
mylist1 = [100, 20, 30, 40]
mylist2 = [10, 50, 60, 90]

if mylist1[1] in mylist2:
    print("Elements are overlapping")
else:
    print("Elements are not overlapping")
```

### Output:

```
Elements are not overlapping
```

✅ Since `mylist1[1]` (which is `20`) is not present in `mylist2`, the output is **"Elements are not overlapping"**.

---

## 2️⃣ `not in` Operator ❌

The `not in` operator checks if an element **does not exist** in a sequence. If the element is absent, it returns **`True`**, otherwise, it returns **`False`**.

### Example:

```python
val = 104
mylist = [100, 210, 430, 840, 108]

if val not in mylist:
    print("Value is NOT present in mylist")
else:
    print("Value is present in mylist")
```

### Output:

```
Value is NOT present in mylist
```

✅ Since `104` is **not present** in `mylist`, the output is **"Value is NOT present in mylist"**.

---
# **Identity Operators in Python** 🆔

## Introduction 📌
Identity operators in Python are used to **compare objects** based on their memory location rather than their values. Python provides two identity operators:

1. **`is`** 👉 Checks if two variables refer to the **same object** in memory.
2. **`is not`** 👉 Checks if two variables refer to **different objects** in memory.

These operators are **different from the equality (`==`) operator**, which checks if the values of two variables are the same, not their memory locations.

---

## 1️⃣ `is` Operator 🔍
The `is` operator checks whether two variables point to the **same object** in memory. It returns **`True`** if both variables reference the same object; otherwise, it returns **`False`**.

### Example:
```python
Firstlist = []
Secondlist = []

if Firstlist == Secondlist:
    print("Both are equal")
else:
    print("Both are not equal")

if Firstlist is Secondlist:
    print("Both variables are pointing to the same object")
else:
    print("Both variables are not pointing to the same object")

thirdList = Firstlist
if thirdList is Secondlist:
    print("Both are pointing to the same object")
else:
    print("Both are not pointing to the same object")
```

### Output:
```
Both are equal
Both variables are not pointing to the same object
Both are not pointing to the same object
```
✅ Here, `Firstlist` and `Secondlist` have **equal values**, but they are **different objects** in memory. That’s why `is` returns `False`.

---

## 2️⃣ `is not` Operator ❌
The `is not` operator checks whether two variables **do not** refer to the same object in memory. If they refer to **different objects**, it returns **`True`**; otherwise, it returns **`False`**.

### Example:
```python
Firstlist = []
Secondlist = []

if Firstlist is not Secondlist:
    print("Both Firstlist and Secondlist variables are different objects")
else:
    print("Both Firstlist and Secondlist variables are the same object")
```

### Output:
```
Both Firstlist and Secondlist variables are different objects
```
✅ Here, `Firstlist` and `Secondlist` are two **different objects** in memory, so `is not` returns `True`.

---

## Visual Representation 🖼️
To understand `is` and `is not`, let's visualize memory allocation:

### **Memory Representation**
```md
Firstlist  --->  [ ]  (Memory Location: 0x1234)
Secondlist --->  [ ]  (Memory Location: 0x5678)
```
Since `Firstlist` and `Secondlist` are created separately, they occupy different memory locations. Hence, `Firstlist is not Secondlist` returns `True`.

### **Comparison Table**
| Expression                | Description                                      | Output |
|---------------------------|--------------------------------------------------|--------|
| `Firstlist == Secondlist` | Checks if values are equal                      | `True`  |
| `Firstlist is Secondlist` | Checks if objects are the same in memory        | `False` |
| `Firstlist is not Secondlist` | Checks if objects are different in memory | `True`  |

---

# **Logical Operators**&#x20;

## Introduction 📌

Logical operators in Python are used to **combine conditional statements** that evaluate to **True or False**. These operators help in decision-making by allowing multiple conditions to be checked within a single statement.

Python provides **three types** of logical operators:

1. **`and`** 👉 Returns `True` if **both conditions** are `True`, otherwise returns `False`.
2. **`or`** 👉 Returns `True` if **at least one condition** is `True`, otherwise returns `False`.
3. **`not`** 👉 Reverses the Boolean value of a condition.

---

## 1️⃣ Logical `and` Operator 🔗

The `and` operator returns `True` **only if both conditions are \*\*\*\*\*\*\*\*****`True`**. If any one condition is `False`, it returns `False`.

### Syntax:

```python
A and B
```

### Example:

```python
a = 32
b = 132

if a > 0 and b > 0:
    print("Both a and b are greater than zero")
else:
    print("At least one variable is less than 0")
```

### Output:

```
Both a and b are greater than zero
```

✅ Since **both ************`a`************ and ************`b`************ are greater than zero**, the condition evaluates to `True`.

---

## 2️⃣ Logical `or` Operator 🔀

The `or` operator returns `True` **if at least one condition is \*\*\*\*\*\*\*\*****`True`**. It returns `False` **only if both conditions are \*\*\*\*\*\*\*\*****`False`**.

### Syntax:

```python
A or B
```

### Example:

```python
a = 32
b = -32

if a > 0 or b > 0:
    print("At least one variable is greater than zero")
else:
    print("Both variables are less than 0")
```

### Output:

```
At least one variable is greater than zero
```

✅ Since **`a`**\*\* is greater than zero\*\*, the condition evaluates to `True`, even though `b` is negative.

---

## 3️⃣ Logical `not` Operator ❌

The `not` operator **reverses the Boolean value** of a condition. If a condition is `True`, `not` makes it `False`, and vice versa.

### Example:

```python
a = 32

if not a < 0:
    print("Boolean value of a is True")
else:
    print("Boolean value of a is False")
```

### Output:

```
Boolean value of a is True
```

✅ Here, `not a < 0` means **`a`**\*\* is not less than 0\*\*, which is `True`, so the statement prints correctly.

---

## Visual Representation 🖼️

To better understand logical operators, consider the following **truth table**:

### **Truth Table for ************`and`************, ************`or`************, and ************`not`************ Operators**

| A (Condition 1) | B (Condition 2) | `A and B` | `A or B` | `not A` |
| --------------- | --------------- | --------- | -------- | ------- |
| `True`          | `True`          | `True`    | `True`   | `False` |
| `True`          | `False`         | `False`   | `True`   | `False` |
| `False`         | `True`          | `False`   | `True`   | `True`  |
| `False`         | `False`         | `False`   | `False`  | `True`  |


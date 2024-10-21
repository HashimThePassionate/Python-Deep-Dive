# 📘 **Typing Systems in python** 🐍

In this section, we explore **typing systems**—a fundamental aspect of programming that dictates how data types are managed, interpreted, and enforced. We’ll discuss **strong vs. weak** typing, **dynamic vs. static** typing, and how these concepts are applied in **Python 3.12**. Understanding typing systems can help you write **cleaner, more robust, and maintainable** code. 🚀

## **Table of Contents** 📖

- [Introduction](#introduction)
- [Strong vs. Weak Typing](#strong-vs-weak-typing)
  - [What Makes a Language Strongly or Weakly Typed?](#what-makes-a-language-strongly-or-weakly-typed)
  - [Real-World Examples](#real-world-examples)
- [Dynamic vs. Static Typing](#dynamic-vs-static-typing)
  - [Understanding Python's Dynamic Typing](#understanding-pythons-dynamic-typing)
  - [Real-World Example: Runtime Flexibility](#real-world-example-runtime-flexibility)
- [Are Weak or Dynamic Typing Systems Less Robust?](#are-weak-or-dynamic-typing-systems-less-robust)
- [Conclusion](#conclusion)

## **Introduction** 🏁

**Typing systems** define how programming languages handle **data types**. They determine how data is **checked, converted**, and **validated**. Gaining a solid understanding of typing can help you write **cleaner and more reliable code**, especially with Python 3.12’s **dynamic and strong typing system**.

## **Strong vs. Weak Typing** 💪🤏

### **What Makes a Language Strongly or Weakly Typed?**

- **Strongly Typed Languages** 💪: These languages enforce **strict type rules**. If you try to perform an operation on incompatible types, the language will raise an error. Examples include **Python, Haskell, TypeScript**, and **Rust**.
  
- **Weakly Typed Languages** 🤏: These languages often **coerce types** to make operations work, even if they don’t naturally fit. Examples include **JavaScript**, **Perl**, and **older versions of C**.

**Example in Python 3.12 (Strong Typing):**
```python
# Trying to add a list and a dictionary will raise an error.
print([] + {})  
# Output: TypeError: can only concatenate list (not "dict") to list
```

**Example in JavaScript (Weak Typing):**
```javascript
console.log([] + {});  // Output: "[object Object]"
console.log({} + []);  // Output: "[object Object]"
```

**Key Takeaway:** 
In Python 3.12, combining incompatible types will raise an **immediate error**, ensuring that issues are caught early, making your code **predictable** and **reliable**. Weakly typed languages might **convert** types automatically, which can lead to **unexpected behavior**.

### **Real-World Examples** 🌐

Imagine you're building a system to process user data:
```python
def process_age(age: int) -> int:
    return age + 1

# Using a string accidentally
print(process_age("25"))
# Output: TypeError: can only concatenate str (not "int") to str
```

In Python, you'll see an error if `age` is not an integer. This **forces** you to **correct the issue**, resulting in **more robust code**.

## **Dynamic vs. Static Typing** ⚡📝

### **Understanding Python's Dynamic Typing**

- **Static Typing** 📝: In statically typed languages, data types are determined at **compile time**. Variables must have a fixed type, and this does not change.
- **Dynamic Typing** ⚡: In dynamically typed languages, such as Python 3.12, types are determined at **runtime**. Variables can change their types during execution.

**Example of Dynamic Typing in Python 3.12:**
```python
a = 5          # `a` is an integer
a = "string"   # Now, `a` is a string
a = (1, 2, 3)  # Now, `a` is a tuple
print(a)       # Output: (1, 2, 3)
```

**Key Takeaway:**
The **flexibility** of dynamic typing allows for faster development. You don’t have to **declare types** explicitly, and you can **change** the type of a variable if needed. However, this can also lead to **runtime errors** if the code’s behavior isn’t clearly defined.

### **Real-World Example: Runtime Flexibility** 🕒

Consider a situation where you’re building a **data parser**:
```python
def parse_input(data: str | list[int]) -> list[str]:
    if isinstance(data, str):
        return data.split(',')
    elif isinstance(data, list):
        return [str(item) for item in data]
    else:
        raise ValueError("Unsupported data type!")

# This function can handle both strings and lists
print(parse_input("apple,banana,cherry"))  # Output: ['apple', 'banana', 'cherry']
print(parse_input([1, 2, 3]))              # Output: ['1', '2', '3']
```

Dynamic typing allows your function to **adapt** to different input types without requiring explicit **type declarations**. This is **great for flexibility**, but can lead to **bugs** if the data is **not what you expect**.

## **Are Weak or Dynamic Typing Systems Less Robust?** 🧐

- **Weakly Typed Languages:** While they allow rapid iteration, they can **mask bugs** due to unexpected **type coercions**. You need to **rely heavily** on tools like linters and **unit tests** to catch errors.
- **Dynamically Typed Languages:** Python 3.12’s dynamic typing makes coding **fast and flexible**, but can lead to **runtime errors** if variables change types unexpectedly. Proper **testing** and using **type annotations** can mitigate these issues.

**Example Using Type Annotations for Clarity:**
```python
def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))  # Output: 3.0
```

Type annotations in Python 3.12 help **document** your code, making it easier to understand what each function expects and returns. This improves code **readability** and **maintainability**.



## **Conclusion** 🏁

Understanding **typing systems** helps you make **informed decisions** when writing code. Python 3.12’s **strong** and **dynamic** typing strikes a balance between **rigidity** (to catch bugs) and **flexibility** (to enable quick changes). By leveraging the **strengths** of Python’s typing system, you can write code that is **clean, robust, and easy to maintain**.

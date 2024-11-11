# 📘 **Literal Types** 🐍

In this section, we'll explore **Literal Types** and **Enums** in Python. Literal types help in constraining the values that a variable can take, which ensures better control and reduces errors. We'll also dive into **Enums**, a handy tool for representing a set of named constants. Let's get started! 🚀


## **Table of Contents** 📖

- [📘 **Literal Types** 🐍](#-literal-types-)
  - [**Table of Contents** 📖](#table-of-contents-)
  - [1. **Introduction to Literal Types** 📜](#1-introduction-to-literal-types-)
    - [**Why Use Literal Types?** 🤔](#why-use-literal-types-)
    - [**Syntax of Literal Types**](#syntax-of-literal-types)
  - [2. **Practical Examples of Literal Types** 🔧](#2-practical-examples-of-literal-types-)
    - [**Simple Validation**](#simple-validation)
    - [**Runtime Validationsn**](#runtime-validations)
    - [**Setting Fixed Options**](#setting-fixed-options)
  - [3. **Introduction to Enums** 🌟](#3-introduction-to-enums-)
    - [**What Are Enums?**](#what-are-enums)
    - [**Benefits of Using Enums**](#benefits-of-using-enums)
  - [4. **Practical Examples of Enums** 🛠️](#4-practical-examples-of-enums-️)
    - [**Real-World Example: Representing Days of the Week** 📅](#real-world-example-representing-days-of-the-week-)
    - [**Example: User Access Levels**](#example-user-access-levels)
  - [5. **Combining Literals and Enums** 🏷️🛡️](#5-combining-literals-and-enums-️️)
  - [6. **Conclusion** 🏁](#6-conclusion-)
  - [7. **Discussion Topic** 💬](#7-discussion-topic-)


## 1. **Introduction to Literal Types** 📜

Literal types allow you to **restrict** the possible values a variable can hold to a specific set of values. This helps avoid invalid data being passed around in your code, enhancing its safety and predictability.

### **Why Use Literal Types?** 🤔

1. **Enforce strict input validation**: Only specific values can be assigned.
2. **Prevent errors early**: Type checkers like `mypy` can catch issues before runtime.
3. **Improve code readability**: Clearly states the possible values a variable can take.

### **Syntax of Literal Types**

To use Literal types, you need to import the `Literal` from the `typing` module. 

```python
from typing import Literal

def serve_drink(drink: Literal["Tea", "Coffee", "Juice"]) -> str:
    return f"Here is your {drink}!"
```

In the example above, the function `serve_drink` will only accept "Tea," "Coffee," or "Juice" as inputs. 🚫 No other strings allowed!


## 2. **Practical Examples of Literal Types** 🔧

### **Simple Validation**

Suppose we have a function that processes orders. Using Literal types ensures that only valid order types are processed.

```python
from typing import Literal

def order_item(item: Literal["Pizza", "Burger", "Fries"]) -> str:
    return f"Order placed for: {item}."

# Valid call
print(order_item("Pizza"))  # Output: Order placed for: Pizza.

# Invalid call (Type checker will warn)
# print(order_item("Sandwich")) 
```

### **Runtime Validations**
```python
from typing import Literal

def order_tea(tea: Literal['doodhpatti', 'sulaimani', 'greentea']) -> str:
    # Run-time validation
    valid_teas = ['doodhpatti', 'sulaimani', 'greentea']
    if tea not in valid_teas:
        raise ValueError(f"Invalid tea selection: {tea}. Please choose from {valid_teas}.")
    return f"Here is your {tea}."

# Valid order
print(order_tea('doodhpatti'))  # Output: Here is your doodh patti.

# Invalid order (will raise ValueError)
try:
    print(order_tea('coffee'))  # This will raise an error at run-time.
except ValueError as e:
    print(e)

```

### **Setting Fixed Options**

Here’s how you might define user roles with strict types:

```python
def set_user_role(role: Literal["Admin", "Editor", "Viewer"]) -> str:
    return f"User set to role: {role}"

# Examples
print(set_user_role("Admin"))   # Valid
# print(set_user_role("Guest")) # Invalid
```


## 3. **Introduction to Enums** 🌟

### **What Are Enums?**

**Enums** (short for Enumerations) are a way to define a **set of named constant values**. They are often used when you have a fixed number of options, and each option is unique and identifiable.

Think of enums as a collection of **unique, immutable constants**. Unlike literals, enums can represent more complex sets of values, including numbers, strings, or a mix.

### **Benefits of Using Enums**

1. **Improves readability**: Makes the code self-explanatory.
2. **Reduces errors**: Enforces strict values and prevents invalid data from creeping in.
3. **Flexible to update**: Easy to add or change values without breaking code.


## 4. **Practical Examples of Enums** 🛠️

### **Real-World Example: Representing Days of the Week** 📅

```python
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def is_weekend(day: Day) -> bool:
    return day in (Day.SATURDAY, Day.SUNDAY)

# Example usage
print(is_weekend(Day.FRIDAY))     # Output: False
print(is_weekend(Day.SUNDAY))     # Output: True
```

In the above code, `Day` is an Enum class where each member is a constant. The `is_weekend` function checks whether the given day is a weekend.

### **Example: User Access Levels**

```python
from enum import Enum

class AccessLevel(Enum):
    GUEST = "guest"
    USER = "user"
    ADMIN = "admin"

def check_access(user_level: AccessLevel) -> str:
    if user_level == AccessLevel.ADMIN:
        return "Full Access Granted."
    elif user_level == AccessLevel.USER:
        return "Limited Access Granted."
    return "Guest Access Only."

# Examples
print(check_access(AccessLevel.ADMIN))  # Full Access Granted.
print(check_access(AccessLevel.GUEST))  # Guest Access Only.
```


## 5. **Combining Literals and Enums** 🏷️🛡️

Combining Literal types with Enums can enhance your control over input and improve error handling. Here’s an example:

```python
from typing import Literal
from enum import Enum

class OrderType(Enum):
    DELIVERY = "Delivery"
    PICKUP = "Pickup"

def process_order(order: Literal[OrderType.DELIVERY, OrderType.PICKUP]) -> str:
    return f"Processing {order.value} order."

print(process_order(OrderType.DELIVERY))  # Output: Processing Delivery order.
```

In this example, `OrderType` enum restricts the possible order types, and Literal ensures that only these types are accepted.


## 6. **Conclusion** 🏁

Using **Literal Types** and **Enums** in Python 3.12 provides a **safer**, **more robust**, and **clearer** way to handle fixed sets of values in your code. Whether you're managing user roles, processing orders, or setting configurations, these tools give you the precision and readability you need. 🌟


## 7. **Discussion Topic** 💬

**Question:**

How can you use Literal Types and Enums to simplify and make your code more error-resistant? Have you encountered any bugs that could have been prevented by using these tools?


# 📚 Annotating Collections in Python 

Welcome to this comprehensive guide on **Annotating Collections** in Python! 🚀 In this README, we’ll dive into the concept of type annotations for collections, covering best practices, real-world examples, and explanations of how annotations make your code more robust, readable, and maintainable. Let’s get started! 🎉

## 📖 Table of Contents

- [📚 Annotating Collections in Python](#-annotating-collections-in-python)
  - [📖 Table of Contents](#-table-of-contents)
  - [📋 Introduction](#-introduction)
  - [🧐 Understanding Collection Annotations](#-understanding-collection-annotations)
    - [📦 Homogeneous Collections](#-homogeneous-collections)
    - [🎭 Heterogeneous Collections](#-heterogeneous-collections)
  - [🛒 Real-World Example: E-Commerce Order Processing](#-real-world-example-e-commerce-order-processing)
    - [🤔 The Problem Statement](#-the-problem-statement)
    - [🛠️ Annotating Collections in Practice](#️-annotating-collections-in-practice)
      - [Step 1: Define the `Item` Class](#step-1-define-the-item-class)
      - [Step 2: Write the `calculate_order_total` Function](#step-2-write-the-calculate_order_total-function)
      - [Step 3: Adding Discounts Using Dictionaries](#step-3-adding-discounts-using-dictionaries)
      - [Step 4: Handling Multiple Orders with Tuples](#step-4-handling-multiple-orders-with-tuples)
  - [🌟 Benefits of Proper Annotations](#-benefits-of-proper-annotations)
  - [🏆 Best Practices](#-best-practices)
  - [🎯 Conclusion](#-conclusion)

## 📋 Introduction

Type annotations in Python provide valuable information about the expected types of variables, function parameters, and return values. While basic annotations (like `int` or `str`) are straightforward, collections such as lists, dictionaries, and tuples often require specifying the types of elements they contain. Annotating collections accurately makes your code:
- **Easier to understand:** Clearly defined types show how data flows through your code.
- **More robust:** Type checkers like `mypy` can detect errors at development time.
- **Better documented:** Annotations act as self-documenting code, aiding other developers.

Let’s look at how to annotate collections properly in Python 3.12! 📝

## 🧐 Understanding Collection Annotations

When working with collections, you often encounter two types:
- **Homogeneous collections**: Contain elements of the same type.
- **Heterogeneous collections**: Contain elements of varying types.

### 📦 Homogeneous Collections

Homogeneous collections are collections where all elements are of the same type. Common examples include lists of numbers, sets of strings, or dictionaries with consistent key-value pairs.

**Example of a Homogeneous List**:
```python
# A list containing only integers
numbers: list[int] = [1, 2, 3, 4, 5]
```

In this example:
- The annotation `list[int]` specifies that `numbers` is a list containing `int` elements only.
- By being explicit about the list’s contents, type checkers can help catch errors if we accidentally add a non-integer to the list.

### 🎭 Heterogeneous Collections

Heterogeneous collections contain elements of multiple types, making them useful for more complex data structures. For example, a list of elements where some items are strings and others are integers.

**Example of a Heterogeneous List**:
```python
from typing import Union

# A list that can contain both strings and integers
mixed_list: list[Union[int, str]] = [1, "two", 3, "four"]
```

In this example:
- `Union[int, str]` means that each element in the list can be either an `int` or a `str`.
- By specifying the possible types, we provide clarity and allow type checkers to enforce correct usage when adding or accessing items.

## 🛒 Real-World Example: E-Commerce Order Processing

Let’s consider a practical scenario to see how collection annotations are helpful in real-world applications.

### 🤔 The Problem Statement

Imagine you’re building an e-commerce application where customers place orders, and each order contains multiple items. Each item has attributes like `name`, `quantity`, and `price`. Our goal is to:
1. Define an `Item` class for individual items.
2. Write a function to calculate the total price of an order.
3. Properly annotate collections to ensure each function and variable is clear and type-safe.

### 🛠️ Annotating Collections in Practice

#### Step 1: Define the `Item` Class

We start by defining an `Item` class using Python’s `dataclass` decorator to make our data structure simple and readable.

```python
from dataclasses import dataclass

@dataclass
class Item:
    name: str          # Name of the item (e.g., "Laptop")
    quantity: int      # Quantity of the item ordered
    price_per_unit: float  # Price per unit of the item
```

In this class:
- Each attribute is annotated with its type (`str`, `int`, and `float`).
- Using `@dataclass` automatically generates an `__init__` method, which helps streamline object creation.

#### Step 2: Write the `calculate_order_total` Function

Now, let’s create a function to calculate the total cost of an order. An order is essentially a list of `Item` objects, so we’ll annotate the parameter accordingly.

```python
from typing import List

def calculate_order_total(items: List[Item]) -> float:
    total = 0.0
    for item in items:
        total += item.quantity * item.price_per_unit
    return total
```

**Explanation:**
- We annotate `items` as `List[Item]`, meaning it’s a list where each element is an `Item` instance.
- The function returns a `float`, representing the total cost.

**Using the Function:**
```python
# Define a list of items for the order
order_items = [
    Item(name="Laptop", quantity=1, price_per_unit=1500.0),
    Item(name="Mouse", quantity=2, price_per_unit=25.0),
    Item(name="Keyboard", quantity=1, price_per_unit=75.0),
]

# Calculate the total price of the order
total_price = calculate_order_total(order_items)
print(f"Total Order Price: ${total_price:.2f}")  # Output: $1625.00
```

#### Step 3: Adding Discounts Using Dictionaries

Suppose we want to apply discounts to specific items. We can use a dictionary to store the discounts as a mapping between item names and discount percentages. Each entry in the dictionary has a string key (`str`) representing the item name, and a float value (`float`) representing the discount percentage.

```python
from typing import Dict

# Mapping item names to discount percentages
discounts: Dict[str, float] = {
    "Laptop": 0.10,     # 10% discount on Laptop
    "Keyboard": 0.05,   # 5% discount on Keyboard
}
```

Now, let’s update our function to include discounts.

```python
def calculate_order_total_with_discounts(items: List[Item], discounts: Dict[str, float]) -> float:
    total = 0.0
    for item in items:
        discount = discounts.get(item.name, 0.0)  # Default discount is 0 if not found
        total += item.quantity * item.price_per_unit * (1 - discount)
    return total
```

**Explanation:**
- `discounts` is annotated as `Dict[str, float]`, meaning it’s a dictionary with `str` keys (item names) and `float` values (discount percentages).
- The function calculates the total price with applicable discounts by fetching each item’s discount with `discounts.get(item.name, 0.0)`.

**Using the Updated Function:**
```python
total_price_with_discounts = calculate_order_total_with_discounts(order_items, discounts)
print(f"Total Price with Discounts: ${total_price_with_discounts:.2f}")  # Output: $1542.50
```

#### Step 4: Handling Multiple Orders with Tuples

If we need to process multiple orders, each containing a list of items, we can use `List[Order]` to represent all orders, where each `Order` is a `List[Item]`.

```python
from typing import List

# Define type aliases for readability
Order = List[Item]
Orders = List[Order]

def process_orders(orders: Orders) -> List[float]:
    totals: List[float] = []
    for order in orders:
        total = calculate_order_total(order)
        totals.append(total)
    return totals
```

**Explanation:**
- `Order` is a type alias for `List[Item]`, representing a single order.
- `Orders` is a list of orders, where each order is itself a list of `Item`s.
- `process_orders` takes a list of orders and returns a list of total prices for each order.

**Using the Function:**
```python
order1 = [
    Item(name="Laptop", quantity=1, price_per_unit=1500.0),
    Item(name="Mouse", quantity=2, price_per_unit=25.0),
]

order2 = [
    Item(name="Monitor", quantity=2, price_per_unit=300.0),
    Item(name="HDMI Cable", quantity=3, price_per_unit=15.0),
]

all_orders = [order1, order2]
order_totals = process_orders(all_orders)

for i, total in enumerate(order_totals, 1):
    print(f"Total for Order {i}: ${total:.2f}")
```

**Output:**
```
Total for Order 1: $1550.00
Total for Order 2: $645.00
```

## 🌟 Benefits of Proper Annotations

1. **Improved Readability**

: Type annotations clarify the expected contents of collections, making code more understandable at a glance.
2. **Error Detection**: Type checkers like `mypy` can catch type-related issues before runtime, reducing debugging time.
3. **Enhanced Tooling Support**: IDEs can offer better autocompletion and suggestions based on annotations.
4. **Documentation**: Annotations act as documentation, showing other developers what types of data are expected.

## 🏆 Best Practices

1. **Use Type Aliases for Complex Types**:
   ```python
   Order = List[Item]
   Discounts = Dict[str, float]
   ```

2. **Be Specific with Collection Contents**:
   ```python
   # Good
   items: List[Item]

   # Bad
   items: list
   ```

3. **Consistency in Annotations**: Maintain consistency in type annotations across the codebase for readability and predictability.

4. **Leverage Type Checking Tools**: Use `mypy` or other type-checking tools to verify annotations.

## 🎯 Conclusion

Annotating collections in Python 3.12 makes your code more readable, predictable, and robust. By clearly specifying the types within collections, you help prevent bugs, improve tooling support, and make your code easier for others to understand. Embrace type annotations to elevate your Python coding experience! 🎉

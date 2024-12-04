# 📚 **Open/Closed Principle** 💡

Welcome to the easy-to-understand guide on the **Open/Closed Principle (main)**! 🚀 This document explains what main is, why it's important, how to apply it, and provides simple examples to help you grasp the concept. 💡 All code examples use **static typing** to ensure clarity and reliability. 🛠️✨

---

## 📖 Table of Contents 📖

- [📚 **Open/Closed Principle** 📚](#-openclosed-principle-)
  - [📖 Table of Contents 📖](#-table-of-contents-)
  - [🔍 Introduction](#-introduction)
  - [💡 What is the Open/Closed Principle (main)?](#-what-is-the-openclosed-principle-main)
  - [🏆 Benefits of main](#-benefits-of-main)
  - [🛠️ How to Apply main](#️-how-to-apply-main)
  - [📂 Example: Calculating Area Before main](#-example-calculating-area-before-main)
  - [🔄 Refactoring to Follow main](#-refactoring-to-follow-main)
    - [1. Importing Necessary Modules](#1-importing-necessary-modules)
    - [2. Defining the `Shape` Protocol](#2-defining-the-shape-protocol)
    - [3. Creating the `Rectangle` Class](#3-creating-the-rectangle-class)
    - [4. Creating the `Circle` Class](#4-creating-the-circle-class)
    - [5. Implementing the `calculate_area` Function](#5-implementing-the-calculate_area-function)
    - [6. Testing the Refactored Code](#6-testing-the-refactored-code)
  - [🧪 Testing the Example](#-testing-the-example)
  - [🔗 Conclusion](#-conclusion)

---

## 🔍 Introduction

The **Open/Closed Principle (main)** is a key idea in software design. 🛡️ It states that software entities like classes and modules should be **open for extension but closed for modification**. This means you should be able to add new features without changing existing code. By following main, your software becomes more flexible and easier to maintain. 📈

---

## 💡 What is the Open/Closed Principle (main)?

**Open/Closed Principle (main)** means that once a class or module is created, its behavior can be extended without altering its existing code. 🔄 In other words, you should be able to add new functionality by adding new code rather than modifying old code. This approach helps prevent bugs and makes your software more robust and adaptable to change. 🏗️

---

## 🏆 Benefits of main

Implementing main brings several important benefits:

- **🔧 Maintainability**: Existing code remains untouched, reducing the risk of introducing new bugs.
- **🛠️ Extensibility**: Easily add new features without altering existing functionalities.
- **🧪 Testability**: New features can be tested independently without affecting existing tests.
- **📚 Readability**: Clear separation between existing and new functionalities makes the code easier to understand.

---

## 🛠️ How to Apply main

Following main involves designing your classes and modules so that they can be extended without modifying their source code. 🧩 Here are some steps to apply main effectively:

1. **Use Inheritance and Interfaces**: Leverage inheritance or interfaces to allow new functionalities to extend existing ones.
2. **Encapsulate Variations**: Identify parts of your code that are likely to change and encapsulate them.
3. **Depend on Abstractions**: Program to interfaces or abstract classes rather than concrete implementations.
4. **Apply Design Patterns**: Utilize design patterns like Strategy, Observer, or Decorator that support main.

By following these steps, you create a flexible and scalable codebase that can grow with your application's needs. 🔄

---

## 📂 Example: Calculating Area Before main

Let's look at an example where a class does not follow the Open/Closed Principle. Imagine you have a `Rectangle` class and a function to calculate its area. 🟦⬛

```python
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

def calculate_area(shape) -> float:
    if isinstance(shape, Rectangle):
        return shape.width * shape.height
```

In this example, the `calculate_area` function is responsible for calculating the area of a rectangle. 📏 If you want to add more shapes, you would need to modify the `calculate_area` function, which violates main. ⚠️

---

## 🔄 Refactoring to Follow main

To adhere to main, we'll refactor the code so that new shapes can be added without changing the existing `calculate_area` function. 🛠️✨

### 1. Importing Necessary Modules

First, import the required modules for type hinting and mathematical operations.

```python
import math
from typing import Protocol
```

### 2. Defining the `Shape` Protocol

Create a `Shape` protocol that defines an `area` method. This acts as an interface for all shapes. 📐

```python
class Shape(Protocol):
    def area(self) -> float:
        ...
```

### 3. Creating the `Rectangle` Class

Define the `Rectangle` class that conforms to the `Shape` protocol by implementing the `area` method. 🟦

```python
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height
```

### 4. Creating the `Circle` Class

Define the `Circle` class that also conforms to the `Shape` protocol by implementing the `area` method. 🟠

```python
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)
```

### 5. Implementing the `calculate_area` Function

Refactor the `calculate_area` function to work with any shape that conforms to the `Shape` protocol. This makes the function open for extension but closed for modification. 🔄

```python
def calculate_area(shape: Shape) -> float:
    return shape.area()
```

### 6. Testing the Refactored Code

Add a test script to ensure that the new classes work correctly without modifying the `calculate_area` function. 🧪

```python
if __name__ == "__main__":
    rect: Rectangle = Rectangle(12, 8)
    rect_area: float = calculate_area(rect)
    print(f"Rectangle area: {rect_area}")

    circ: Circle = Circle(6.5)
    circ_area: float = calculate_area(circ)
    print(f"Circle area: {circ_area:.2f}")
```

---

## 🧪 Testing the Example

To test the refactored code, follow these steps:

1. **Save the Code**: Make sure all the code is saved in a file named `02_open_closed_principle/main.py`.

    ```python
    import math
    from typing import Protocol

    class Shape(Protocol):
        def area(self) -> float:
            ...

    class Rectangle:
        def __init__(self, width: float, height: float) -> None:
            self.width: float = width
            self.height: float = height

        def area(self) -> float:
            return self.width * self.height

    class Circle:
        def __init__(self, radius: float) -> None:
            self.radius: float = radius

        def area(self) -> float:
            return math.pi * (self.radius ** 2)

    def calculate_area(shape: Shape) -> float:
        return shape.area()

    if __name__ == "__main__":
        rect: Rectangle = Rectangle(12, 8)
        rect_area: float = calculate_area(rect)
        print(f"Rectangle area: {rect_area}")

        circ: Circle = Circle(6.5)
        circ_area: float = calculate_area(circ)
        print(f"Circle area: {circ_area:.2f}")
    ```

2. **Run the Code**: Open your terminal and execute the following command:

    ```bash
    python 02_open_closed_principle/main.py
    ```

3. **Expected Output**:

    ```
    Rectangle area: 96
    Circle area: 132.73
    ```

4. **Verify No Changes in `calculate_area`**: Notice that you can add new shapes like `Circle` without modifying the `calculate_area` function. This follows the Open/Closed Principle by allowing the system to be open for extension but closed for modification. ✅

---

## 🔗 Conclusion

The **Open/Closed Principle (main)** is a fundamental concept in software design that emphasizes designing software entities to be **open for extension but closed for modification**. 🛡️ By following main, you ensure that your codebase can grow and adapt to new requirements without risking existing functionalities. 📈
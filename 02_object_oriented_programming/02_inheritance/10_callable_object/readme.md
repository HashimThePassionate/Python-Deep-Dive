# 🧮 Callable Objects in Inheritance

Welcome to the guide on using Callable Objects in Inheritance in Python! 🎉 This section will dive into abstract base classes (ABC), concrete subclasses, and callable objects in Python. We'll explore how to create a structured and extensible way to calculate areas of shapes using inheritance and callable objects. By the end, you’ll understand how to implement callable behavior in Python objects to add flexibility and simplicity to your code. Let’s get started! 🐍


## 📖 Table of Contents

- [🧮 Callable Objects in Inheritance](#-callable-objects-in-inheritance)
  - [📖 Table of Contents](#-table-of-contents)
  - [1. Introduction to Callable Objects in Inheritance 📝](#1-introduction-to-callable-objects-in-inheritance-)
  - [2. Abstract Base Class (ABC) - `Shape` 🔹](#2-abstract-base-class-abc---shape-)
  - [3. Concrete Subclasses - `Circle` and `Square` 🔹](#3-concrete-subclasses---circle-and-square-)
  - [4. Callable Object - `AreaCalculator` 🔹](#4-callable-object---areacalculator-)
  - [5. Usage and Execution 🔹](#5-usage-and-execution-)
  - [6. Output 🎉](#6-output-)
  - [7. Why This Approach Works Well 🎯](#7-why-this-approach-works-well-)
  - [8. Complete Code 🧩](#8-complete-code-)


## 1. Introduction to Callable Objects in Inheritance 📝

**Callable objects** provide a clean and intuitive way to represent actions or calculations in object-oriented design. This example demonstrates how **abstract base classes (ABCs)** and callable objects work together in Python. By defining abstract methods and using callable wrappers, we create a reusable and extensible way to calculate areas of shapes, achieving **separation of concerns** and **code reusability**.


## 2. Abstract Base Class (ABC) - `Shape` 🔹

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass
```

- **Purpose**: The `Shape` class is an abstract base class (ABC) defining an interface with an abstract method `area`.
- **Enforcement**: Using the `@abstractmethod` decorator ensures that every subclass of `Shape` **must implement** the `area` method.
- **Benefit**: This structure provides a consistent interface for calculating areas, ensuring that each shape subclass will have its own `area` calculation logic.


## 3. Concrete Subclasses - `Circle` and `Square` 🔹

```python
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
```

- **`Circle` and `Square`**: Both are concrete subclasses of `Shape`.
- **Implementation of `area`**: Each subclass provides its specific implementation of `area`:
  - `Circle` calculates area as \( \pi \times \text{radius}^2 \).
  - `Square` calculates area as \( \text{side\_length}^2 \).
- **Explanation**: Each shape now has a well-defined way of calculating its area, following the interface contract set by `Shape`.


## 4. Callable Object - `AreaCalculator` 🔹

```python
class AreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def __call__(self):
        return self.shape.area()
```

- **Purpose**: `AreaCalculator` is a **callable wrapper** for `Shape` objects.
- **The `__call__` Method**: By defining `__call__`, instances of `AreaCalculator` can be used like functions. When an `AreaCalculator` instance is called, it calculates and returns the area of the shape it holds.
- **Encapsulation**: This wrapper class provides a simple, function-like interface for area calculation, keeping the `area` logic encapsulated within each shape.


## 5. Usage and Execution 🔹

```python
# Create instances of Circle and Square
circle = Circle("Circle", 5)
square = Square("Square", 4)

# Create instances of AreaCalculator with Circle and Square objects
circle_calculator = AreaCalculator(circle)
square_calculator = AreaCalculator(square)

# Call the instances of AreaCalculator as if they were functions to calculate the area
circle_area = circle_calculator()
square_area = square_calculator()

# Output the results
print("Area of", circle.name, ":", circle_area)
print("Area of", square.name, ":", square_area)
```

1. **Create Shape Instances**: We create instances of `Circle` and `Square`.
2. **Wrap Shapes in Calculator**: Each shape is wrapped in an `AreaCalculator` instance, making it callable.
3. **Call Calculators**: We call `circle_calculator()` and `square_calculator()` as if they were functions. This triggers the `__call__` method to calculate and return each shape's area.


## 6. Output 🎉

```plaintext
Area of Circle : 78.5
Area of Square : 16
```

Each `AreaCalculator` instance returns the area of its associated shape. This setup allows us to easily add more shapes or customize calculations without modifying existing code, promoting code flexibility and extensibility.


## 7. Why This Approach Works Well 🎯

- **Modularity**: The `Shape` abstract base class defines a clear interface, allowing any subclass to implement its specific `area` logic.
- **Callable Objects**: `AreaCalculator` instances are callable, providing a clean, function-like interface to calculate areas.
- **Encapsulation**: The area calculation is encapsulated in the shape class, while `AreaCalculator` only facilitates the calculation without knowing the specifics.
- **Ease of Extension**: Adding new shapes with their own `area` calculations is straightforward and doesn’t require changes to `AreaCalculator`.

This pattern highlights the **power of callable objects** and **inheritance** in Python, offering a clean and flexible approach to designing object-oriented systems. 🐍


## 8. Complete Code 🧩

Here is the complete code with all sections combined:

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

# Concrete Subclasses
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Callable Object
class AreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def __call__(self):
        return self.shape.area()

# Usage
circle = Circle("Circle", 5)
square = Square("Square", 4)
circle_calculator = AreaCalculator(circle)
square_calculator = AreaCalculator(square)

# Execution
circle_area = circle_calculator()
square_area = square_calculator()

# Output
print("Area of", circle.name, ":", circle_area)
print("Area of", square.name, ":", square_area)
```

This complete code combines the abstract base class, concrete subclasses, and callable object implementation, showcasing how Python’s inheritance and callable objects work together to create a flexible area calculation system.


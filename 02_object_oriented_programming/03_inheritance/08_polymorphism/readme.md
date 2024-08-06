# What is polymorphism?
**Poly-morph-ism** means **Many Forms**

Polymorphism, in the context of object-oriented programming, refers to the ability of different classes to be treated as instances of a common superclass. In Python, polymorphism is achieved through inheritance and method overriding. Let's see how polymorphism is demonstrated in the provided code:

### Polymorphism in Action:

1. **Common Interface (`Shape` Class):**
    ```python
    class Shape:
        def area(self):
            ...
    ```
    - The `Shape` class defines a common interface for all shapes by providing a method `area()`.
    - This method raises a `NotImplementedError`, indicating that subclasses must override it with their own implementations.

2. **Subclasses Override `area()` Method:**
    Both `Circle` and `Square` subclasses override the `area()` method inherited from the `Shape` class with their own implementations.
    ```python
    import math 
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return math.pi * self.radius**2

    class Square(Shape):
        def __init__(self, side_length):
            self.side_length = side_length
        def area(self):
            return self.side_length**2
    ```
    - Despite `Circle` and `Square` having different implementations for the `area()` method, they share the same method signature as defined in the `Shape` class.

3. **Polymorphic Behavior:**
    ```python
    shapes = [Circle(5), Square(4)]

    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.area()}")
    ```
    - In the example usage, a list `shapes` is created containing instances of both `Circle` and `Square`.
    - The `for` loop iterates over each shape in the list.
    - Despite each shape being of a different class (`Circle` or `Square`), they are all treated uniformly as instances of the `Shape` superclass.
    - When `shape.area()` is called, Python dynamically dispatches the call to the appropriate method based on the actual type of the object (`Circle` or `Square`), resulting in the correct area calculation for each shape.

### Summary:

Polymorphism in Python allows objects of different classes to be treated uniformly if they share a common interface (e.g., methods with the same signature). This promotes code reuse, flexibility, and readability by enabling the use of generic functions and data structures that can operate on objects of different types. In the provided code, polymorphism is demonstrated through method overriding (`area()` method in subclasses) and the common interface provided by the `Shape` superclass.

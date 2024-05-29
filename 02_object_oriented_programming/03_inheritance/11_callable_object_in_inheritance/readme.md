# Callable Objects in inheritance

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):)


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


class AreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def __call__(self):
        return self.shape.area()


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

1. **Abstract Base Class (ABC)**:
   - We define an abstract base class `Shape` using the `ABC` module.
   - It has an abstract method `area`, which needs to be implemented by its subclasses.
   - This abstract method ensures that any subclass of `Shape` must provide its own implementation of the `area` method.

2. **Concrete Subclasses**:
   - We have two concrete subclasses of `Shape`: `Circle` and `Square`.
   - Each subclass implements its own `area` method, providing the specific logic to calculate the area of that shape.

3. **Callable Object - `AreaCalculator`**:
   - The `AreaCalculator` class is responsible for calculating the area of a given shape.
   - It takes an instance of a `Shape` object as its input during initialization.
   - The `AreaCalculator` class defines a `__call__` method, making its instances callable.
   - When an instance of `AreaCalculator` is called (i.e., treated like a function), it internally calls the `area` method of the `Shape` object it was initialized with.
   - This allows us to treat instances of `AreaCalculator` as if they were functions, and they will calculate and return the area of the associated shape.

4. **Creating Instances**:
   - We create instances of `Circle` and `Square` classes: `circle` and `square`, respectively.
   - We then create instances of `AreaCalculator` using these shapes: `circle_calculator` and `square_calculator`.

5. **Calling Instances**:
   - We call the instances of `AreaCalculator` as if they were functions (`circle_calculator()` and `square_calculator()`).
   - Internally, these calls invoke the `__call__` method of the `AreaCalculator` instances, which in turn calls the `area` method of the associated `Shape` object.
   - This calculates and returns the area of the respective shape.

6. **Outputting Results**:
   - Finally, we print the calculated areas of the circle and square.

This implementation allows for a separation of concerns, where the `Shape` classes are responsible for defining the area calculation logic for each shape, and the `AreaCalculator` class is responsible for encapsulating the behavior of calculating the area of any given shape. It also demonstrates the use of a callable object (`AreaCalculator`) to provide a clean interface for performing the calculation.
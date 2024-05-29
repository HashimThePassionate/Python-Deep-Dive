from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")


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

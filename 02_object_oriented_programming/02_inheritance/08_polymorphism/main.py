import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")


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


# Example usage
shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.area()}")

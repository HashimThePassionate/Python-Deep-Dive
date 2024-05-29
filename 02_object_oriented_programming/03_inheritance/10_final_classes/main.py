import math
class FinalMeta(type):
    def __new__(cls, name, bases, dct):
        for base in bases:
            if isinstance(base, FinalMeta):
                raise TypeError(
                    f"Type '{base.__name__}' is final and cannot be subclassed")
        return super().__new__(cls, name, bases, dct)

class PI():
    def get_pi(self):
        return math.pi


class AreaOfCircle(PI, metaclass=FinalMeta):
    def calculate_area(self, radius):
        return self.get_pi() * radius * radius

# Trying to subclass AreaOfCircle should raise an error
try:
    class SubClass(AreaOfCircle):
        pass
except TypeError as e:
    print(e)


# Testing the functionality
circle = AreaOfCircle()
print("Pi value:", circle.get_pi())
print("Area of circle with radius 2:", circle.calculate_area(2))
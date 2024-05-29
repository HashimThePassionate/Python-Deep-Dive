## Final Classes

A final class is a class that cannot be subclassed. Once a class is marked as final, it cannot be extended further. This concept comes from languages like Java and C#, where marking a class as final prevents inheritance.

### Why Decorate a Class with Final?

1. **Preventing Subclassing**: By marking a class as final, you explicitly state that the class should not be extended. This can be useful when you want to ensure that a class's behavior or structure remains unchanged.
2. **Design Clarity**: It provides clarity in design by indicating that a class is intended to be used as-is, without further extensions. This can improve code readability and maintainability by preventing unintended inheritance.

### Benefits of Final Classes

- **Security**: Final classes prevent unintended or malicious modifications to critical components of the system by disallowing subclassing.
- **Code Stability**: By preventing subclassing, final classes ensure that the behavior and structure of the class remain stable, reducing the risk of unintended side effects from subclass modifications.
- **Performance**: Final classes may offer performance benefits, as the compiler or interpreter can optimize the code more aggressively knowing that the class cannot be subclassed.

### Implementation in Python

In Python, the concept of final classes is not built into the language like in Java or C#. However, you can emulate final classes using metaclasses.

### Explanation of the Provided Code

```python
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
```

- `FinalMeta` is a metaclass defined to enforce the finality of classes.
- In the `__new__` method of `FinalMeta`, it checks if any base class is also using `FinalMeta`. If so, it raises a `TypeError`.
- `PI` is a simple class providing a method `get_pi` to return the value of Pi.
- `AreaOfCircle` is a class that calculates the area of a circle. It inherits from `PI` and uses `FinalMeta` as its metaclass, indicating that it is a final class.
- An attempt to subclass `AreaOfCircle` (`SubClass`) raises a `TypeError`, as expected.
- The script then tests the functionality of `AreaOfCircle` by creating an instance and calling its methods.

### Output

The output of the provided code will be:
```
Type 'AreaOfCircle' is final and cannot be subclassed
Pi value: 3.141592653589793
Area of circle with radius 2: 12.566370614359172
```

This demonstrates how to emulate final classes in Python using metaclasses.
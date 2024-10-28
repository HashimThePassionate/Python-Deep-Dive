In Python, the `object` class is the base class for all classes. Every class in Python implicitly inherits from the `object` class, directly or indirectly. 

The `object` class provides some default behaviors that are inherited by all other classes. Some of the methods provided by the `object` class include:

- `__new__()`: Responsible for creating a new instance of the class.
- `__init__()`: Initializes the newly created object.
- `__del__()`: Called when the object is about to be destroyed.
- `__repr__()`: Returns a string representation of the object.
- `__str__()`: Returns a string representation of the object suitable for display to end-users.
- `__hash__()`: Returns a hash value for the object, used by hash tables.
- `__eq__()`: Defines behavior for the equality operator `==`.
- `__ne__()`: Defines behavior for the inequality operator `!=`.
- `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`: Defines behavior for comparison operators `<`, `<=`, `>`, `>=`.
- And many more.

Since every class implicitly inherits from `object`, you can call these methods on any object in Python. However, you can also override these methods in subclasses to customize their behavior based on your requirements.

Sure! Let's enhance the examples to be more illustrative and explanatory:

### `__doc__`: 
```python
class Car:
    """A simple class representing a car."""

print(Car.__doc__)
```
**Output**
```output
A simple class representing a car.
```
**Explanation**: The `__doc__` attribute contains the documentation string (docstring) for the class. In this example, the docstring describes what the class represents.

### `__dict__`: 
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.__dict__)
```
**Output**
```output
{'name': 'Alice', 'age': 30}
```
**Explanation**: The `__dict__` attribute contains a dictionary that holds the namespace of the object (attribute names and their corresponding values). This example shows the attributes of a `Person` object stored in its `__dict__`.

### `__module__`: 
```python
class Dog:
    pass

print(Dog.__module__)
```
**Output**
```output
__main__
```
**Explanation**: The `__module__` attribute contains the name of the module in which the class was defined. This example prints the name of the module where the `Dog` class is defined.

### `__annotations__`: 
```python
class Rectangle:
    width: float
    height: float

print(Rectangle.__annotations__)
```
**Output**
```output
{'width': <class 'float'>, 'height': <class 'float'>}
```
**Explanation**: The `__annotations__` attribute contains the annotations defined for attributes and methods within the class. This example shows the annotations for the `width` and `height` attributes of a `Rectangle`.

### `@property`
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.area)
```
**Output**
```output
78.5
```
**Explanation**: The `@property` decorator allows defining a method as a property of an object, allowing access like an attribute. This example calculates the area of a circle using the `area` property.

### `__class__`: 
```python
class Animal:
    pass

animal = Animal()
print(animal.__class__)
```
**Output**
```output
<class '__main__.Animal'>
```
**Explanation**: The `__class__` attribute contains a reference to the class of an object. This example prints the class of the `animal` object.

### `__init__`: 
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show(self):
        print(f'''
Title is : {self.title}
Author is  : {self.author}
''')

book = Book("Python Programming", "John Smith")
book.show()
```
**Output**
```output
Title is : Python Programming
Author is  : John Smith
```
**Explanation**: The `__init__` method is called when an object is initialized. It initializes the object's attributes. This example initializes a `Book` object with a title and an author.

### `__new__`: 
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
```
**Output**
```output
True
```
**Explanation**: The `__new__` method is called to create a new instance of a class before `__init__` is called. This example demonstrates implementing the Singleton design pattern using `__new__` to ensure only one instance of the class is created.

### `__setattr__`: 
```python
class Person:
    def __setattr__(self, name, value):
        print(f"Setting attribute '{name}' to '{value}'")

person = Person()
person.name = "Alice"
```
**Output**
```output
Setting attribute 'name' to 'Alice'
```
**Explanation**: The `__setattr__` method is called when an attribute assignment is attempted on an object. This example prints a message when setting an attribute on a `Person` object.

### `__delattr__`: 
```python
class Person:
    def __setattr__(self, name, value):
        print(f"Setting attribute '{name}' to '{value}'")

    def __delattr__(self, name):
        print(f"Deleting attribute '{name}'")

person = Person()
person.name = "Alice"
del person.name
```
**Output**
```output
Setting attribute 'name' to 'Alice'
Deleting attribute 'name'
```
**Explanation**: The `__delattr__` method is called when an attribute deletion is attempted on an object. This example prints a message when deleting an attribute from a `Person` object.

### `__eq__`: 
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
```
**Output**
```output
True
```
**Explanation**: The `__eq__` method is called to determine if two objects are equal. This example compares two `Point` objects based on their `x` and `y` coordinates.

### `__ne__`: 
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __ne__(self, other):
        return not self.__eq__(other)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 != p2)
```
**Explanation**: The `__ne__` method is called to determine if two objects are not equal. This example provides an implementation for `__ne__` based on `__eq__`.

### `__str__`: 
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person)
```
**Output**
```output
Name: Alice, Age: 30
```
**Explanation**: The `__str__` method returns a string representation of the object. This example provides a custom string representation for a `Person` object.

### `__repr__`: 
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(str(person))
print(repr(person))
```
**Output**
```output
Name: Alice, Age: 30
Person(name='Alice', age=30)
```
**Explanation**: The `__repr__` method returns a string representation of the object that can be used to recreate the object. This example provides a custom representation for a `Person` object.

### `__hash__`: 
```python
class Point:
    def __init__(self, hash):
        self.hash = hash

    def __hash__(self):
        return hash((self.hash))

point = Point('12b32bd')
print(hash(point))
```
**Output**
```output
8514614484448761486
```
**Explanation**: The `__hash__` method returns the hash value of the object if it's hashable. This example demonstrates hashing a `Point` object.

### `__format__`: 
```python
class Person:
    def __format__(self, format_spec):
        if format_spec == 'short':
            return "Name: Alice"
        elif format_spec == 'long':
            return "Name: Alice, Age: 30"
        else:
            return "Unknown format"

person = Person()
print(format(person, 'long'))
```
**Output**
```output
Name: Alice, Age: 30
```
**Explanation**: The `__format__` method returns a formatted string representation of the object. This example provides

custom formatting options for a `Person` object.

### `__getattribute__`: 
```python
class Logger:
    def __getattribute__(self, name):
        if name == 'log':
            # Accessing the 'log' attribute directly without recursion
            return super().__getattribute__(name)
        else:
            print(f"Accessing attribute '{name}'")
            return super().__getattribute__(name)

    def log(self, message):
        print("Logging:", message)

logger = Logger()
logger.log("An important message")
```
**Output**
```output
Logging: An important message
```
**Explanation**: The `__getattribute__` method is called whenever an attribute is accessed on the object. This example prints a message when accessing an attribute of a `Logger` object.

### `__sizeof__`: 
```python
class Object:
    pass

obj = Object()
print(obj.__sizeof__())
```
**Explanation**: The `__sizeof__` method returns the size of the object in memory. This example prints the size of an empty `Object` object.

### `__reduce__`: 
```python
import pickle

class Person:
    def __reduce__(self):
        return (self.__class__, ())

person = Person()
pickled_person = pickle.dumps(person)
print(pickled_person)
```
**Output**
```output
b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x06Person\x94\x93\x94)R\x94.'
```
**Explanation**: The `__reduce__` method returns a tuple that instructs how to pickle (serialize) the object. This example demonstrates pickling a `Person` object.

### `__reduce_ex__`: 
```python
import pickle

class Person:
    def __reduce_ex__(self, protocol):
        return (self.__class__, ())

person = Person()
pickled_person = pickle.dumps(person, protocol=2)
```
**Explanation**: The `__reduce_ex__` method is an extended version of `__reduce__` that allows specifying a protocol for pickling. This example demonstrates pickling a `Person` object with a specific protocol.

### `__getstate__` (Python 3.11 and above):
```python
import pickle

class Person:
    def __getstate__(self):
        return {'name': 'Alice', 'age': 30}

person = Person()
state = person.__getstate__()
```
**Explanation**: The `__getstate__` method returns the state of the object for pickling (serialization). This example provides the state of a `Person` object for pickling.

### `__dir__`: 
```python
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(dir(calc))
```
**Output**
```output
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'subtract']
```
**Explanation**: The `__dir__` method returns the list of attributes and methods of the object. This example prints the attributes and methods of a `Calculator` object.

### `__init_subclass__`: 
```python
class Base:
    def __init_subclass__(cls):
        print(f"Subclassing {cls.__name__}")

class Derived(Base):
    pass
```
**Explanation**: The `__init_subclass__` method is called when a class is subclassed. This example prints a message when subclassing `Base` to create `Derived`.

### `__subclasshook__`: 
```python
class Shape:
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'area') and callable(subclass.area) and hasattr(subclass, 'perimeter') and callable(subclass.perimeter)

class Rectangle:
    def area(self):
        pass

    def perimeter(self):
        pass

print(issubclass(Rectangle, Shape))
```
**Explanation**: The `__subclasshook__` method is used to customize the behavior of the `issubclass` function for a class. This example defines a custom rule for determining if a class is a subclass of `Shape`.
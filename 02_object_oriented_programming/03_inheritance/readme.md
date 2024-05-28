Inheritance in Python is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. This promotes code reuse and can lead to a more natural and hierarchical organization of code. 

### Key Concepts of Inheritance in Python

1. **Inheritance**: One class (child or subclass) inherits the attributes and methods of another class (parent or superclass).

2. **Constructor**: A special method `__init__` used to initialize the objects of a class. When a class inherits another class, the constructor of the parent class can be called within the constructor of the child class.

3. **Access Modifiers**: Python uses naming conventions to define the accessibility of variables and methods.
   - **Public**: Accessible from anywhere (e.g., `self.var`).
   - **Protected**: Indicated by a single underscore (e.g., `self._var`), intended to be used within the class and its subclasses.
   - **Private**: Indicated by a double underscore (e.g., `self.__var`), intended to be used only within the class.

4. **Overriding Methods**: A child class can provide a specific implementation of a method that is already defined in its parent class.

5. **Comparing Objects**: Customizing object comparisons by overriding special methods like `__eq__` and `__lt__`.

6. **Polymorphism**: The ability to use a single interface to represent different data types. In Python, this is often achieved through method overriding and interfaces.

Let's dive into each concept with Python code examples.

### Example: Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

### Constructor and Super() Function

The `super()` function allows you to call methods of the superclass.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the constructor of the superclass
        self.breed = breed

# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Golden Retriever
```

### Access Modifiers

```python
class Animal:
    def __init__(self, name):
        self.name = name  # Public
        self._species = "Unknown"  # Protected
        self.__habitat = "Unknown"  # Private
    
    def get_habitat(self):
        return self.__habitat

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def set_habitat(self, habitat):
        self.__habitat = habitat

# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Output: Buddy
print(dog._species)  # Output: Unknown
# print(dog.__habitat)  # This will raise an AttributeError
print(dog.get_habitat())  # Correct way to access private attribute
```

### Method Overriding

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Usage
dog = Dog()
print(dog.speak())  # Output: Woof!
```

### Comparing Objects

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):
        if isinstance(other, Animal):
            return self.age < other.age
        return NotImplemented

# Usage
dog1 = Animal("Buddy", 5)
dog2 = Animal("Buddy", 5)
dog3 = Animal("Max", 3)

print(dog1 == dog2)  # Output: True
print(dog1 < dog3)  # Output: False
print(dog3 < dog1)  # Output: True
```

### Polymorphism

```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())

# Usage
dog = Dog()
cat = Cat()

animal_speak(dog)  # Output: Woof!
animal_speak(cat)  # Output: Meow!
```

These examples illustrate the core concepts of inheritance in Python, including how to define and use constructors, access modifiers, method overriding, object comparison, and polymorphism.
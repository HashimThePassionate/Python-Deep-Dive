# Person Class Example with `__hash__` and `__eq__` Methods

This example demonstrates how to implement the `__hash__` and `__eq__` methods in a custom Python class to make instances of the class hashable and comparable. This allows the instances to be used as keys in dictionaries and elements in sets.

## Class Definition

We define a class `Person` with `name` and `age` attributes and implement the `__hash__` and `__eq__` methods.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        # Combine name and age to create a unique hash value
        return hash((self.name, self.age))

    def __eq__(self, other):
        # Check if another object is a Person and has the same name and age
        return isinstance(other, Person) and self.name == other.name and self.age == other.age
```

## Example Usage

### Creating Instances of Person

We create several instances of the `Person` class.

```python
# Creating instances of Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 30)
```

### Using Person Instances as Dictionary Keys

We use instances of the `Person` class as keys in a dictionary.

```python
# Using Person instances as dictionary keys
person_dict = {person1: "Engineer", person2: "Doctor"}
print(person_dict[person1])  # Output: "Engineer"
print(person_dict[person3])  # Output: "Engineer" because person1 and person3 are considered equal
```

### Using Person Instances as Set Elements

We use instances of the `Person` class as elements in a set.

```python
# Using Person instances as set elements
person_set = {person1, person2, person3}
print(len(person_set))  # Output: 2 because person1 and person3 are considered equal
```

### Checking Equality

We check the equality of different `Person` instances.

```python
# Checking equality
print(person1 == person3)  # Output: True because they have the same name and age
print(person1 == person2)  # Output: False because they have different names and ages
```

## Summary

- The `__hash__` method allows the `Person` instances to generate unique hash values based on their attributes.
- The `__eq__` method allows the `Person` instances to be compared for equality.
- These methods enable the use of `Person` instances as dictionary keys and set elements.

This example demonstrates how to make custom objects hashable and comparable, which is essential for using them in data structures like dictionaries and sets.

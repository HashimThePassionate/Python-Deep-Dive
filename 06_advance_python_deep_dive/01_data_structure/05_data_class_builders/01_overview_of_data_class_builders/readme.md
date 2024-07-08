# Overview of Data Class Builders

## Introduction
This document explains how to simplify the creation of data classes in Python using various builders. We'll start with a basic class example and progress to more advanced techniques.

## Basic Class Example
Consider a simple class to represent geographic coordinates.

### Example 5-1: Basic Coordinate Class
```python
class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
```
This class holds latitude and longitude attributes. However, writing the `__init__` method repeatedly can become tedious, especially for classes with many attributes. Additionally, this class lacks useful methods like `__repr__` and `__eq__`.

### Problems with Basic Class
1. **Unhelpful `__repr__` Output**
    ```python
    >>> moscow = Coordinate(55.76, 37.62)
    >>> moscow
    <coordinates.Coordinate object at 0x107142f10>
    ```
2. **Meaningless `==` Comparison**
    ```python
    >>> location = Coordinate(55.76, 37.62)
    >>> location == moscow
    False
    >>> (location.lat, location.lon) == (moscow.lat, moscow.lon)
    True
    ```

### Explanation of Problems
- **`__repr__` Method**: This method is supposed to provide a string representation of the object that is helpful for debugging. Without a custom `__repr__` method, the output is not very informative (e.g., `<coordinates.Coordinate object at 0x107142f10>`).
- **`__eq__` Method**: This method is used to compare two objects for equality. By default, Python compares objects based on their memory addresses (object IDs), which means two objects with the same data are not considered equal unless this method is explicitly defined. In the provided example, `location == moscow` returns `False` even though they have the same latitude and longitude.

## Using Data Class Builders
Data class builders provide `__init__`, `__repr__`, and `__eq__` methods automatically, among other features.

### Namedtuples
A `namedtuple` is a factory function that builds a subclass of `tuple` with the specified name and fields.

### Example: Using `namedtuple`
```python
from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')

moscow = Coordinate(55.756, 37.617)
print(moscow)  # Output: Coordinate(lat=55.756, lon=37.617)
print(moscow == Coordinate(lat=55.756, lon=37.617))  # Output: True
```
- **Useful `__repr__`**: The `__repr__` output is informative.
- **Meaningful `__eq__`**: The equality operator works as expected.

### Typing NamedTuple
`typing.NamedTuple` provides similar functionality with added type annotations.

### Example: Using `typing.NamedTuple`
```python
import typing

Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])

print(issubclass(Coordinate, tuple))  # Output: True
print(typing.get_type_hints(Coordinate))  # Output: {'lat': <class 'float'>, 'lon': <class 'float'>}
```
- **Typed NamedTuple**: Fields can also be provided as keyword arguments.
```python
Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)
```

### Class Statement with Typing.NamedTuple
Since Python 3.6, `typing.NamedTuple` can be used in a class statement with type annotations.

### Example 5-2: Class Statement with Typing.NamedTuple
```python
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
```
- **Custom `__str__`**: This class displays coordinates in a formatted string.

## Using Dataclass
The `dataclass` decorator automates the creation of methods like `__init__`, `__repr__`, and `__eq__` using PEP 526 syntax.

### Example 5-3: Using Dataclass
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
```
- **No Inheritance Dependency**: The `@dataclass` decorator does not rely on inheritance or metaclasses.

## Conclusion
Using data class builders like `namedtuple`, `typing.NamedTuple`, and `dataclass`, you can create more efficient and readable Python classes with automatic method generation. These tools reduce boilerplate code and enhance the functionality of your classes.
# Main Features of Data Class Builders

## Overview

This repository provides a summary of the main features of different data class builders in Python: `namedtuple`, `NamedTuple`, and `dataclass`. Each builder has unique characteristics and use cases.

## Feature Comparison

The table below summarizes the key features of each data class builder:

| Feature                         | namedtuple          | NamedTuple            | dataclass                      |
|---------------------------------|---------------------|-----------------------|--------------------------------|
| Mutable instances               | NO                  | NO                    | YES                            |
| Class statement syntax          | NO                  | YES                   | YES                            |
| Construct dict                  | `x._asdict()`       | `x._asdict()`         | `dataclasses.asdict(x)`        |
| Get field names                 | `x._fields`         | `x._fields`           | `[f.name for f in dataclasses.fields(x)]` |
| Get defaults                    | `x._field_defaults` | `x._field_defaults`   | `[f.default for f in dataclasses.fields(x)]` |
| Get field types                 | N/A                 | `x.__annotations__`   | `x.__annotations__`            |
| New instance with changes       | `x._replace(...)`   | `x._replace(...)`     | `dataclasses.replace(x, ...)`  |
| New class at runtime            | `namedtuple(...)`   | `NamedTuple(...)`     | `dataclasses.make_dataclass(...)` |

## Detailed Feature Explanation

### Mutable Instances

- **`namedtuple` and `NamedTuple`**: Instances are immutable, meaning you cannot change their values after creation.

#### Example: Immutable Instances with `namedtuple`
```python
from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')
moscow = Coordinate(55.756, 37.617)

# Attempting to change the value will result in an error
# moscow.lat = 55.8  # AttributeError: can't set attribute
```

#### Example: Immutable Instances with `NamedTuple`
```python
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

moscow = Coordinate(55.756, 37.617)

# Attempting to change the value will result in an error
# moscow.lat = 55.8  # AttributeError: can't set attribute
```

- **`dataclass`**: By default, instances are mutable. However, you can make them immutable by using `frozen=True` in the decorator.

#### Example: Mutable Instances with `dataclass`
```python
from dataclasses import dataclass

@dataclass
class Coordinate:
    lat: float
    lon: float

moscow = Coordinate(55.756, 37.617)
moscow.lat = 55.8  # This will work as the instance is mutable
print(moscow)  # Output: Coordinate(lat=55.8, lon=37.617)
```

#### Example: Immutable Instances with `dataclass` (frozen)
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

moscow = Coordinate(55.756, 37.617)

# Attempting to change the value will result in an error
# moscow.lat = 55.8  # FrozenInstanceError: cannot assign to field 'lat'
```

### Class Statement Syntax

- **`NamedTuple` and `dataclass`**: Support regular class statement syntax, which makes it easier to add methods and docstrings to the class.

#### Example: Class Statement Syntax with `NamedTuple`
```python
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinate(55.756, 37.617)
print(moscow)  # Output: 55.8°N, 37.6°E
```

#### Example: Class Statement Syntax with `dataclass`
```python
from dataclasses import dataclass

@dataclass
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinate(55.756, 37.617)
print(moscow)  # Output: 55.8°N, 37.6°E
```

### Construct Dictionary

- **`namedtuple` and `NamedTuple`**: Use the method `._asdict()` to convert the instance to a dictionary.
- **`dataclass`**: Use the function `dataclasses.asdict(x)` to achieve the same result.

#### Example: Construct Dictionary with `namedtuple`
```python
moscow_dict = moscow._asdict()
print(moscow_dict)  # Output: {'lat': 55.756, 'lon': 37.617}
```

#### Example: Construct Dictionary with `dataclass`
```python
from dataclasses import asdict

moscow_dict = asdict(moscow)
print(moscow_dict)  # Output: {'lat': 55.756, 'lon': 37.617}
```

### Get Field Names and Default Values

- **`namedtuple` and `NamedTuple`**: Use `._fields` to get field names and `._field_defaults` to get default values.
- **`dataclass`**: Use the function `dataclasses.fields(x)` to get a list of field objects, which include attributes for name and default value.

#### Example: Get Field Names and Default Values with `namedtuple`
```python
fields = moscow._fields
defaults = moscow._field_defaults
print(fields)  # Output: ('lat', 'lon')
print(defaults)  # Output: {}
```

#### Example: Get Field Names and Default Values with `dataclass`
```python
from dataclasses import fields

field_names = [f.name for f in fields(Coordinate)]
default_values = [f.default for f in fields(Coordinate)]
print(field_names)  # Output: ['lat', 'lon']
print(default_values)  # Output: [<dataclasses._MISSING_TYPE object at ...>, <dataclasses._MISSING_TYPE object at ...>]
```

### Get Field Types

- **`NamedTuple` and `dataclass`**: Have a mapping of field names to types in the `__annotations__` class attribute. It is recommended to use `typing.get_type_hints(MyClass)` instead of reading `__annotations__` directly for better handling of type hints and forward references.

#### Example: Get Field Types with `NamedTuple`
```python
from typing import get_type_hints

type_hints = get_type_hints(Coordinate)
print(type_hints)  # Output: {'lat': <class 'float'>, 'lon': <class 'float'>}
```

#### Example: Get Field Types with `dataclass`
```python
type_hints = get_type_hints(Coordinate)
print(type_hints)  # Output: {'lat': <class 'float'>, 'lon': <class 'float'>}
```

### New Instance with Changes

- **`namedtuple` and `NamedTuple`**: Use `x._replace(**kwargs)` to create a new instance with some attributes replaced.
- **`dataclass`**: Use `dataclasses.replace(x, **kwargs)` to achieve the same.

#### Example: New Instance with Changes using `namedtuple`
```python
moscow_updated = moscow._replace(lat=55.8)
print(moscow_updated)  # Output: Coordinate(lat=55.8, lon=37.617)
```

#### Example: New Instance with Changes using `dataclass`
```python
from dataclasses import replace

moscow_updated = replace(moscow, lat=55.8)
print(moscow_updated)  # Output: Coordinate(lat=55.8, lon=37.617)
```

### New Class at Runtime

- **`namedtuple` and `NamedTuple`**: Support creating a new class at runtime using the function call syntax.
- **`dataclass`**: Use `dataclasses.make_dataclass(...)` to create a new class at runtime.

#### Example: New Class at Runtime using `namedtuple`
```python
DynamicCoordinate = namedtuple('DynamicCoordinate', 'lat lon')
dynamic_instance = DynamicCoordinate(55.756, 37.617)
print(dynamic_instance)  # Output: DynamicCoordinate(lat=55.756, lon=37.617)
```

#### Example: New Class at Runtime using `dataclass`
```python
from dataclasses import make_dataclass

DynamicCoordinate = make_dataclass('DynamicCoordinate', [('lat', float), ('lon', float)])
dynamic_instance = DynamicCoordinate(55.756, 37.617)
print(dynamic_instance)  # Output: DynamicCoordinate(lat=55.756, lon=37.617)
```

## Conclusion

Each data class builder in Python (`namedtuple`, `NamedTuple`, and `dataclass`) provides different features suited for various use cases. Understanding these features helps in selecting the appropriate builder for your specific requirements.


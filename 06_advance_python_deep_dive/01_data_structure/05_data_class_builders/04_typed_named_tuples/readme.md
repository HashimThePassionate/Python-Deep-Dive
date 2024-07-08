# Typed Named Tuples

The `typing.NamedTuple` provides a way to define tuple-like classes with named fields and type annotations. This enhances readability and type safety in your code.

## Features

- **Type Annotations**: Every instance field must be annotated with a type.
- **Default Values**: Fields can have default values.
- **Inheritance**: Inherits methods from `collections.namedtuple` and `tuple`.
- **Type Information**: Includes `__annotations__` attribute for type hints.

## Example: Defining and Using a Typed Named Tuple

### Example 5-8: Coordinate Class with Typed NamedTuple

```python
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'
```

### Explanation

- **Type Annotations**: Each field is annotated with its type (`lat` and `lon` as `float`, `reference` as `str`).
- **Default Value**: The `reference` field has a default value of `'WGS84'`.

### Usage

```python
# Creating an instance of the Coordinate class
coord = Coordinate(0.0, 0.0)

# Accessing fields
print(coord.lat)       # Output: 0.0
print(coord.reference) # Output: WGS84

# Displaying the named tuple
print(coord)           # Output: Coordinate(lat=0.0, lon=0.0, reference='WGS84')
```

## Key Points

- **No Additional Methods**: `typing.NamedTuple` does not add any methods beyond those provided by `collections.namedtuple` and `tuple`.
- **Type Annotations Ignored at Runtime**: The `__annotations__` attribute holds type hints, but Python ignores these annotations at runtime. They are primarily for static type checkers and IDEs.

## Handling Unannotated Fields

If fields are not annotated, Python will raise an error. Every field in a `NamedTuple` must have a type annotation. 

### Example: Error with Unannotated Fields

```python
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference = 'WGS84'  # Missing type annotation

# This will raise a TypeError
# TypeError: NamedTuple('Coordinate', ['lat', 'lon', 'reference']) missing 1 required positional argument
```

To avoid errors, ensure that every field is annotated with a type.

## Conclusion

`typing.NamedTuple` enhances `collections.namedtuple` by adding type annotations, making your code more readable and type-safe. It is a simple and effective way to define immutable, tuple-like classes with named fields and optional default values. Ensure that all fields are properly annotated to avoid errors.
# Classic Named Tuples

## Overview

The `collections.namedtuple` function is a factory that builds subclasses of `tuple` enhanced with field names, a class name, and an informative `__repr__`. Classes built with `namedtuple` can be used anywhere tuples are needed. Many functions in the Python standard library that return tuples now return named tuples for convenience without affecting the user’s code.

## Features

- **Memory Efficiency**: Instances of named tuples take the same amount of memory as tuples because field names are stored in the class.
- **Field Access**: Fields can be accessed by name or position.
- **Inheritance**: Named tuples inherit useful methods from `tuple`, such as `__eq__` and comparison operators like `__lt__`.

## Creating and Using Named Tuples

To create a named tuple, you need two parameters: a class name and a list of field names, which can be given as an iterable of strings or as a single space-delimited string.

### Example 5-4: Defining and Using a Named Tuple

```python
from collections import namedtuple

# Define a named tuple type
City = namedtuple('City', 'name country population coordinates')

# Create an instance of the named tuple
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# Access fields by name
print(tokyo.name)          # Output: Tokyo
print(tokyo.population)    # Output: 36.933

# Access fields by position
print(tokyo[1])            # Output: JP

# Display the named tuple
print(tokyo)
# Output: City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
```

### Accessing Fields

- By name: `tokyo.name`
- By position: `tokyo[1]`

### Example 5-5: Named Tuple Attributes and Methods

```python
# Define a named tuple type
City = namedtuple('City', 'name country population location')

# Define another named tuple for coordinates
Coordinate = namedtuple('Coordinate', 'lat lon')

# Create an instance using _make() method
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
delhi = City._make(delhi_data)

# Convert named tuple to a dictionary
delhi_dict = delhi._asdict()
print(delhi_dict)
# Output: {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'location': Coordinate(lat=28.613889, lon=77.208889)}

# Serialize named tuple to JSON
import json
print(json.dumps(delhi_dict))
# Output: '{"name": "Delhi NCR", "country": "IN", "population": 21.935, "location": [28.613889, 77.208889]}'
```

#### Attributes and Methods

- **`._fields`**: Tuple with the field names of the class.
    ```python
    print(City._fields)
    # Output: ('name', 'country', 'population', 'location')
    ```

- **`._make(iterable)`**: Builds a named tuple from an iterable.
    ```python
    delhi = City._make(delhi_data)
    ```

- **`._asdict()`**: Returns a dictionary built from the named tuple instance.
    ```python
    delhi_dict = delhi._asdict()
    ```

### Example 5-6: Named Tuple with Default Values

Since Python 3.7, `namedtuple` accepts the `defaults` keyword-only argument, providing an iterable of N default values for each of the N rightmost fields of the class.

```python
# Define a named tuple with default values
Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])

# Create an instance without specifying the reference
coord = Coordinate(0, 0)
print(coord)
# Output: Coordinate(lat=0, lon=0, reference='WGS84')

# Access default values
print(Coordinate._field_defaults)
# Output: {'reference': 'WGS84'}
```

## Conclusion

Named tuples offer a memory-efficient, readable, and convenient way to work with tuples that have named fields. They provide additional methods and attributes to enhance usability while maintaining the immutability and performance benefits of tuples.
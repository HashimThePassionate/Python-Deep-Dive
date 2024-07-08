# nametuple features
from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')
moscow = Coordinate(55.756, 37.617)
# Attempting to change the value will result in an error
# moscow.lat = 55.8  # AttributeError: can't set attribute

# Example: Construct Dictionary with namedtuple
moscow_dict = moscow._asdict()
print(moscow_dict)  # Output: {'lat': 55.756, 'lon': 37.617}
# Example: Get Field Names and Default Values with namedtuple
fields = moscow._fields
defaults = moscow._field_defaults
print(fields)  # Output: ('lat', 'lon')
print(defaults)  # Output: {}

# Example: New Instance with Changes using namedtuple
moscow_updated = moscow._replace(lat=55.8)
print(moscow_updated)  # Output: Coordinate(lat=55.8, lon=37.617)

# Example: New Class at Runtime using namedtuple
DynamicCoordinate = namedtuple('DynamicCoordinate', 'lat lon')
dynamic_instance = DynamicCoordinate(55.756, 37.617)
print(dynamic_instance)  # Output: DynamicCoordinate(lat=55.756, lon=37.617)

# ----------------------------------------------------------------------------------------------

# Feature NamedTuple
from typing import NamedTuple
class Coordinatee(NamedTuple):
    lat: float
    lon: float

moscow = Coordinatee(55.756, 37.617)

# Attempting to change the value will result in an error
# moscow.lat = 55.8  # AttributeError: can't set attribute

# Example: Class Statement Syntax with NamedTuple
class Coordinateee(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinateee(55.756, 37.617)
print(moscow)  # Output: 55.8°N, 37.6°E



# Example: Get Field Types with NamedTuple
from typing import get_type_hints

type_hints = get_type_hints(Coordinate)
print(type_hints)  # Output: {'lat': <class 'float'>, 'lon': <class 'float'>}


# ----------------------------------------------------------------------------------------------
# Feature DataClass
from dataclasses import dataclass, fields

@dataclass
class Coordinateeee:
    lat: float
    lon: float

moscow = Coordinateeee(55.756, 37.617)
moscow.lat = 55.8  # This will work as the instance is mutable
print(moscow)  # Output: Coordinate(lat=55.8, lon=37.617)

# Example: Immutable Instances with dataclass (frozen)
@dataclass(frozen=True)
class Coordinateeeee:
    lat: float
    lon: float

moscow = Coordinateeeee(55.756, 37.617)

# Attempting to change the value will result in an error
# moscow.lat = 55.8  # FrozenInstanceError: cannot assign to field 'lat'

# Example: Class Statement Syntax with dataclass
@dataclass
class Coordinateeeeeee:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinateeeeeee(55.756, 37.617)
print(moscow)  # Output: 55.8°N, 37.6°E
# Example: Construct Dictionary with dataclass
from dataclasses import asdict

moscow_dict = asdict(moscow)
print(moscow_dict)  # Output: {'lat': 55.756, 'lon': 37.617}



field_names = [f.name for f in fields(Coordinateeee)]
default_values = [f.default for f in fields(Coordinateeee)]
print(field_names)  # Output: ['lat', 'lon']
print(default_values)  # Output: [<dataclasses._MISSING_TYPE object at ...>, <dataclasses._MISSING_TYPE object at ...>]

# Example: Get Field Types with dataclass
type_hints = get_type_hints(Coordinate)
print(type_hints)  # Output: {'lat': <class 'float'>, 'lon': <class 'float'>

from dataclasses import replace

moscow_updated = replace(moscow, lat=55.8)
print(moscow_updated)  # Output: Coordinate(lat=55.8, lon=37.617)

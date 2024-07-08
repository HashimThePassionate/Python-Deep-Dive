# Basic Class Example
from dataclasses import dataclass
from typing import NamedTuple
import typing
from collections import namedtuple


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


moscow = Coordinate(55.76, 37.62)
print(moscow)

# Comparsion
location = Coordinate(55.76, 37.62)
print(moscow == location)
print((location.lat, location.lon) == (moscow.lat, moscow.lon))

# Using Data Class Builders
# Namedtuple
coordinate = namedtuple('Coordinate', 'lat lon')
moscow = coordinate(55.756, 37.617)
print(moscow)  # Output: Coordinate(lat=55.756, lon=37.617)
print(moscow == coordinate(lat=55.756, lon=37.617))  # Output: True


# Typing NamedTuple
cr = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
print(issubclass(cr, tuple))  # Output: True
# Output: {'lat': <class 'float'>, 'lon': <class 'float'>}
print(typing.get_type_hints(cr))


# Class Statement with Typing.NamedTuple


class cordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


c = cordinate(55.756, 37.617)
print(c)  # Output: 55.8°N, 37.6°E


# Data Class


@dataclass(frozen=True)
class CT:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


# CT = CT(55.756, 37.617)
print(CT)  # Output: 55.8°N, 37.6°E

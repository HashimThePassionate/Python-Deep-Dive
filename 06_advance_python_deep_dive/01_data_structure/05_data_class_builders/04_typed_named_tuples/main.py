from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'


# Creating an instance of the Coordinate class
coord = Coordinate(0.0, 0.0)

# Accessing fields
print(coord.lat)       # Output: 0.0
print(coord.reference) # Output: WGS84

# Displaying the named tuple
print(coord)           # Output: Coordinate(lat=0.0, lon=0.0, reference='WGS84')
# Example 5-4: Defining and Using a Named Tuple
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

# Example 5-5: Named Tuple Attributes and Methods
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


# Example 5-6: Named Tuple with Default Values
# Since Python 3.7, namedtuple accepts the defaults keyword-only argument, providing an iterable of N default values for each of the N rightmost fields of the class.

# Define a named tuple with default values
Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])

# Create an instance without specifying the reference
coord = Coordinate(0, 0)
print(coord)
# Output: Coordinate(lat=0, lon=0, reference='WGS84')

# Access default values
print(Coordinate._field_defaults)
# Output: {'reference': 'WGS84'}
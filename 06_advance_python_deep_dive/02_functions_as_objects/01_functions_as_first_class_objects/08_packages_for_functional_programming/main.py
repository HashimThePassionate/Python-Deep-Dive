from functools import reduce
from operator import mul, itemgetter
def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

print(factorial(5))  # 120



def factorial_(n):
    return reduce(mul, range(1, n + 1))

print(factorial_(5))  # 120

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print(metro_data)
print(sorted(metro_data))
print(itemgetter(1)(metro_data[0]))  # JP



from collections import namedtuple
from operator import attrgetter

LatLon = namedtuple('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]

name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
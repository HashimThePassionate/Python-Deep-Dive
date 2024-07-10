import typing

class Coordinate(typing.NamedTuple):
    lat: float
    lon: float

trash = Coordinate('Ni!', None)

print(trash)

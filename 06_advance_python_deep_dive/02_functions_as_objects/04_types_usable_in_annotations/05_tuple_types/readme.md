# Tuple Types

## Introduction
There are three main ways to annotate tuple types in Python:
1. Tuples as records
2. Tuples as records with named fields
3. Tuples as immutable sequences

## Tuples as Records
When using a tuple as a record, use the `tuple` built-in and declare the types of the fields within `[]`.

### Example: Using Tuple as Records
For example, the type hint `tuple[str, float, str]` accepts a tuple with a city name, population, and country: `('Shanghai', 24.28, 'China')`.

### Example: Geohash Function with Tuples
Consider a function that takes a pair of geographic coordinates and returns a Geohash.

```python
from geolib import geohash as gh  # type: ignore
PRECISION = 9

def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)

shanghai = (31.2304, 121.4737)
print(geohash(shanghai))  # Output: 'wtw3sjq6q'
```

**Explanation:**
- `from geolib import geohash as gh`: Imports the `geohash` function from the `geolib` package and renames it to `gh`.
- `PRECISION = 9`: Defines a constant for the precision of the geohash.
- `def geohash(lat_lon: tuple[float, float]) -> str`: Defines a function that takes a tuple of two floats (latitude and longitude) and returns a string.
- `return gh.encode(*lat_lon, PRECISION)`: Encodes the latitude and longitude into a geohash string.
- `shanghai = (31.2304, 121.4737)`: Defines a tuple with the coordinates of Shanghai.
- `print(geohash(shanghai))`: Prints the geohash of Shanghai.

For Python < 3.9, import and use `typing.Tuple` in type hints. It is deprecated but will remain in the standard library at least until 2024.

```python
from typing import Tuple

def geohash(lat_lon: Tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)
```

## Tuples as Records with Named Fields
For tuples with many fields or specific types of tuples used in many places, use `typing.NamedTuple`.

### Example: Using NamedTuple for Coordinates
```python
from typing import NamedTuple
from geolib import geohash as gh  # type: ignore
PRECISION = 9

class Coordinate(NamedTuple):
    lat: float
    lon: float

def geohash(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, PRECISION)

shanghai = Coordinate(31.2304, 121.4737)
print(geohash(shanghai))  # Output: 'wtw3sjq6q'
```

**Explanation:**
- `from typing import NamedTuple`: Imports the `NamedTuple` class from the `typing` module.
- `class Coordinate(NamedTuple)`: Defines a `NamedTuple` class with two fields: `lat` and `lon`, both of type `float`.
- `def geohash(lat_lon: Coordinate) -> str`: Defines a function that takes a `Coordinate` instance and returns a string.
- `return gh.encode(*lat_lon, PRECISION)`: Encodes the latitude and longitude into a geohash string.
- `shanghai = Coordinate(31.2304, 121.4737)`: Creates an instance of `Coordinate` with the coordinates of Shanghai.
- `print(geohash(shanghai))`: Prints the geohash of Shanghai.

### Example: Display Function
It is type-safe to pass a `Coordinate` instance to a function expecting a `tuple[float, float]`.

```python
def display(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    ew = 'E' if lon >= 0 else 'W'
    return f'{abs(lat):0.1f}°{ns}, {abs(lon):0.1f}°{ew}'

shanghai = Coordinate(31.2304, 121.4737)
print(display(shanghai))  # Output: '31.2°N, 121.5°E'
```

**Explanation:**
- `def display(lat_lon: tuple[float, float]) -> str`: Defines a function that takes a tuple of two floats and returns a formatted string.
- `lat, lon = lat_lon`: Unpacks the tuple into `lat` and `lon` variables.
- `ns = 'N' if lat >= 0 else 'S'`: Determines the north/south direction based on the latitude.
- `ew = 'E' if lon >= 0 else 'W'`: Determines the east/west direction based on the longitude.
- `return f'{abs(lat):0.1f}°{ns}, {abs(lon):0.1f}°{ew}'`: Returns the formatted string.
- `shanghai = Coordinate(31.2304, 121.4737)`: Creates an instance of `Coordinate` with the coordinates of Shanghai.
- `print(display(shanghai))`: Prints the formatted coordinates of Shanghai.

## Tuples as Immutable Sequences
To annotate tuples of unspecified length that are used as immutable lists, specify a single type followed by a comma and `...` (ellipsis).

### Example: Tuple of Integers
```python
def process_numbers(numbers: tuple[int, ...]) -> None:
    for number in numbers:
        print(number)

numbers = (1, 2, 3, 4, 5)
process_numbers(numbers)
```

**Explanation:**
- `def process_numbers(numbers: tuple[int, ...]) -> None`: Defines a function that takes a tuple of integers of any length and returns `None`.
- `for number in numbers`: Iterates over the numbers in the tuple.
- `print(number)`: Prints each number.
- `numbers = (1, 2, 3, 4, 5)`: Creates a tuple of integers.
- `process_numbers(numbers)`: Calls the function with the tuple of numbers.

The ellipsis indicates that any number of elements >= 1 is acceptable. There is no way to specify fields of different types for tuples of arbitrary length.

### Example: Columnize Function
The `columnize` function transforms a sequence into a table of rows and cells in the form of a list of tuples with unspecified lengths.

```python
from collections.abc import Sequence

def columnize(sequence: Sequence[str], num_columns: int = 0) -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** 0.5)
    num_rows, reminder = divmod(len(sequence), num_columns)
    num_rows += bool(reminder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]

animals = 'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()
table = columnize(animals)

for row in table:
    print(''.join(f'{word:10}' for word in row))
```

**Explanation:**
- `from collections.abc import Sequence`: Imports the `Sequence` class from the `collections.abc` module.
- `def columnize(sequence: Sequence[str], num_columns: int = 0) -> list[tuple[str, ...]]`: Defines a function that takes a sequence of strings and an optional number of columns, and returns a list of tuples of strings.
- `if num_columns == 0`: Checks if the number of columns is not provided.
- `num_columns = round(len(sequence) ** 0.5)`: Sets the number of columns to the square root of the length of the sequence, rounded to the nearest integer.
- `num_rows, reminder = divmod(len(sequence), num_columns)`: Divides the sequence into rows and columns.
- `num_rows += bool(reminder)`: Adds an extra row if there is a remainder.
- `return [tuple(sequence[i::num_rows]) for i in range(num_rows)]`: Returns a list of tuples, where each tuple is a column of the sequence.
- `animals = 'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()`: Splits a string of animal names into a list.
- `table = columnize(animals)`: Calls the `columnize` function with the list of animal names.
- `for row in table`: Iterates over the rows in the table.
- `print(''.join(f'{word:10}' for word in row))`: Prints each row, formatting each word to be 10 characters wide.

Output:
```
drake     koala     yak       
fawn      lynx      zapus     
heron     tahr                 
ibex      xerus
```

## Conclusion
Tuples in Python can be annotated in various ways depending on their usage. Whether used as records, records with named fields, or immutable sequences, understanding how to annotate tuples can make your code more robust and easier to understand.
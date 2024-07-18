# Packages for Functional Programming

## Introduction
Python, while not specifically designed as a functional programming language, supports a functional coding style through first-class functions, pattern matching, and supportive packages such as `operator` and `functools`. This README will cover the usage of these packages to enhance your functional programming in Python.

## The `operator` Module

The `operator` module provides function equivalents for many arithmetic and comparison operators, which can simplify and enhance readability in functional programming.

### Example 7-11: Factorial with `reduce` and Lambda

Using `reduce` and a lambda function to calculate the factorial of a number:

```python
from functools import reduce

def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))
```

### Example 7-12: Factorial with `reduce` and `operator.mul`

Rewriting the factorial calculation using `operator.mul`:

```python
from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1))
```

### Explanation:
- **Using `reduce` with Lambda:**
  - `reduce(lambda a, b: a * b, range(1, n + 1))` multiplies elements in the range to calculate factorial.
- **Using `reduce` with `operator.mul`:**
  - `reduce(mul, range(1, n + 1))` uses `operator.mul` for multiplication, making the code cleaner and more readable.

### Example 7-13: Using `itemgetter` to Sort a List of Tuples

`itemgetter` from the `operator` module is used to sort a list of tuples by a specific field.

```python
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
```

#### Explanation:
- `itemgetter(1)` creates a function that retrieves the item at index 1, allowing sorting by country code.

### Example 7-14: Using `attrgetter` to Sort a List of Named Tuples

`attrgetter` is used to sort a list of named tuples by an attribute.

```python
from collections import namedtuple
from operator import attrgetter

LatLon = namedtuple('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]

name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
```

#### Explanation:
- `attrgetter('name', 'coord.lat')` retrieves the name and latitude, allowing sorting by latitude.

### Example 7-15: Using `methodcaller`

`methodcaller` creates a function that calls a method on its operand.

```python
from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))  # Output: 'THE TIME HAS COME'

hyphenate = methodcaller('replace', ' ', '-')
print(hyphenate(s))  # Output: 'The-time-has-come'
```

#### Explanation:
- `methodcaller('upper')` creates a function that calls the `upper` method on a string.
- `methodcaller('replace', ' ', '-')` creates a function that replaces spaces with hyphens in a string.

## Freezing Arguments with `functools.partial`

The `functools` module provides higher-order functions like `partial`, which allows freezing some arguments of a function, creating a new function with fewer arguments.

### Example 7-16: Using `partial` to Create a Triple Function

```python
from operator import mul
from functools import partial

triple = partial(mul, 3)
print(triple(7))  # Output: 21
print(list(map(triple, range(1, 10))))  # Output: [3, 6, 9, 12, 15, 18, 21, 24, 27]
```

#### Explanation:
- `partial(mul, 3)` creates a new function `triple` that multiplies its argument by 3.

### Example 7-17: Normalizing Unicode with `partial`

Creating a convenient function for Unicode normalization:

```python
import unicodedata
from functools import partial

nfc = partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)  # Output: False
print(nfc(s1) == nfc(s2))  # Output: True
```

#### Explanation:
- `partial(unicodedata.normalize, 'NFC')` creates a new function `nfc` that normalizes strings to NFC format.

### Example 7-18: Using `partial` with the `tag` Function

```python
from functools import partial
from tagger import tag

picture = partial(tag, 'img', class_='pic-frame')
print(picture(src='wumpus.jpeg'))  # Output: <img class="pic-frame" src="wumpus.jpeg" />
```

#### Explanation:
- `partial(tag, 'img', class_='pic-frame')` creates a new function `picture` that sets the tag name to 'img' and the class to 'pic-frame'.

## Conclusion

The `operator` and `functools` modules provide powerful tools for functional programming in Python. These modules simplify common tasks, improve code readability, and offer flexible ways to handle functions and arguments. Understanding and utilizing these tools can greatly enhance your functional programming capabilities in Python.
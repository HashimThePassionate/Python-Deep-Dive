#  Pattern Matching Class Instances

This section provides an overview of how to use pattern matching with class instances in Python. We'll cover the three types of class patterns: simple, keyword, and positional. Examples will be provided to illustrate each type.

# Section 1: Simple Class Patterns
Simple class patterns are used to match class instances based on their type and, optionally, attributes.
### Example 1: Matching a Sequence with Simple Class Patterns

The following pattern matches a four-item sequence where the first item must be a string and the last item must be a tuple containing two floats.

```python
def match_sequence(seq):
    match seq:
        case [str(name), _, _, (float(lat), float(lon))]:
            print(f"Name: {name}, Latitude: {lat}, Longitude: {lon}")
        case _:
            print("No match")

sequence = ["John", 25, "Data", (37.7749, -122.4194)]
match_sequence(sequence)
```

**Output:**
```
Name: John, Latitude: 37.7749, Longitude: -122.4194
```

### Example 2: Matching a Float Value

The syntax for class patterns looks like a constructor invocation. This example matches a float value without binding a variable:

```python
def process_value(x):
    match x:
        case float():
            print(f"Processing float value: {x}")
        case _:
            print("Not a float")

value = 12.34
process_value(value)
```

**Output:**
```
Processing float value: 12.34
```

### Common Mistake

Be cautious with this syntax as it may introduce bugs.

```python
def process_value_bug(x):
    match x:
        case float:  # DANGER!!!
            print(f"Processing float value: {x}")
        case _:
            print("Not a float")

value = 12.34
process_value_bug(value)
```

**Output:**
```
File "c:\Users\aaaa\Desktop\Python-Deep-Dive\06_advance_python_deep_dive\01_data_structure\05_data_class_builders\11_ pattern_matching_class_instances\main.py", line 3
case float:  # DANGER!!!
         ^^^^^
SyntaxError: name capture 'float' makes remaining patterns unreachable
```

### Built-in Types with Special Syntax

The special pattern syntax of `float(x)` applies only to nine blessed built-in types: `bytes`, `dict`, `float`, `frozenset`, `int`, `list`, `set`, `str`, and `tuple`. For these types, the variable in the pattern is bound to the subject instance or the part of the subject that matches a subpattern.

Example:

```python
def match_float_value(x):
    match x:
        case float(y):
            print(f"Matched float value: {y}")
        case int(y):
            print(f"Matched int value: {y}")
        case (str(name), (int(a), int(b))):
            print(f"Matched nested tuple value: ({name}, ({a}, {b}))")
        case [str(name), (str(a), float(b))]:
            print(f"Matched List with tuple value: [{name}, ({a}, {b})]")
        case _:
            print("Not a float")

match_float_value(1)
match_float_value(1.3)
t = ('Hashim', (2, 3))
match_float_value(t)
l = ['Muhammad', ('Hey', 1.2)]
match_float_value(l)
```

**Output:**
```
Matched int value: 1
Matched float value: 1.3
Matched nested tuple value: (Hashim, (2, 3))
Matched List with tuple value: [Muhammad, (Hey, 1.2)]
```

### Explanation

1. **float(y)**: This pattern matches if `x` is a float. The value of `x` is assigned to `y`.
2. **int(y)**: This pattern matches if `x` is an integer. The value of `x` is assigned to `y`.
3. **(str(name), (int(a), int(b)))**: This pattern matches if `x` is a tuple where the first element is a string (assigned to `name`), and the second element is a tuple containing two integers (assigned to `a` and `b`).
4. **[str(name), (str(a), float(b))]**: This pattern matches if `x` is a list where the first element is a string (assigned to `name`), and the second element is a tuple containing a string (assigned to `a`) and a float (assigned to `b`).

For these patterns, Python checks the type and structure of `x`. If `x` matches a pattern, the corresponding variables are bound to parts of `x`, and the associated block of code is executed.

# Section 2: Keyword Class Patterns

Keyword class patterns match class instances based on specific attribute values.

### Example 3: Matching City Instances by Continent

Consider the following `City` class and a list of instances:

```python
import typing

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str

cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]

def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results

asian_cities = match_asian_cities()
for city in asian_cities:
    print(city)
```

**Output:**
```
City(continent='Asia', name='Tokyo', country='JP')
City(continent='Asia', name='Delhi', country='IN')
```

### Example 4: Matching and Collecting Country Attribute

To collect the value of the `country` attribute, use the following pattern:

```python
def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc):
                results.append(cc)
    return results

asian_countries = match_asian_countries()
for country in asian_countries:
    print(country)
```

**Output:**
```
JP
IN
```

You can also use the attribute name directly:

```python
def match_asian_countries_direct():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=country):
                results.append(country)
    return results

asian_countries_direct = match_asian_countries_direct()
for country in asian_countries_direct:
    print(country)
```

**Output:**
```
JP
IN
```

# Section 3: Positional Class Patterns

Positional class patterns match class instances based on the order of their attributes.

### Example 5: Matching City Instances by Continent (Positional)

Using the same `City` class, the following function returns a list of Asian cities:

```python
def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia'):
                results.append(city)
    return results

asian_cities_pos = match_asian_cities_pos()
for city in asian_cities_pos:
    print(city)
```

**Output:**
```
City(continent='Asia', name='Tokyo', country='JP')
City(continent='Asia', name='Delhi', country='IN')
```

### Example 6: Matching and Collecting Country Attribute (Positional)

To collect the value of the `country` attribute, use the following pattern:

```python
def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                results.append(country)
    return results

asian_countries_pos = match_asian_countries_pos()
for country in asian_countries_pos:
    print(country)
```

**Output:**
```
JP
IN
```

### Explanation of `__match_args__`

The special attribute `__match_args__` determines the order of attributes for positional patterns. For the `City` class, it looks like this:

```python
>>> City.__match_args__
('continent', 'name', 'country')
```

This attribute is automatically created by class builders and declares the names of attributes in the order they are used in positional patterns.

### Combining Keyword and Positional Patterns

You can combine keyword and positional arguments in a pattern. Note that not all instance attributes available for matching may be listed in `__match_args__`, so sometimes you may need to use both keyword and positional arguments.

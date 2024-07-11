# Simple Class Patterns

# Example 1: Matching a Sequence with Simple Class Patterns
def match_sequence(seq):
    match seq:
        case [str(name), _, _, (float(lat), float(lon))]:
            print(f"Name: {name}, Latitude: {lat}, Longitude: {lon}")
        case _:
            print("No match")

sequence = ["John", 25, "Data", (37.7749, -122.4194)]
match_sequence(sequence)


# Example 2: Matching a Float Value
def process_value(x):
    match x:
        case float():
            print(f"Processing float value: {x}")
        case _:
            print("Not a float")

value = 12.34
process_value(value)


# Built-in Types with Special Syntax
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

# --------------------------------------------------------------------------------------
# Keyword Class Patterns
# Example 3: Matching City Instances by Continent
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


# Example 4: Matching and Collecting Country Attribute
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

# --------------------------------------------------------------------------------------
# Positional Class Patterns

# Example 5: Matching City Instances by Continent (Positional)
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

# Example 6: Matching and Collecting Country Attribute (Positional)
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



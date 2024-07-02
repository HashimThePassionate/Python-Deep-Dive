# Pattern Matching with Mappings

The `match/case` statement in Python supports subjects that are mapping objects. Patterns for mappings look like dict literals, but they can match instances of any actual or virtual subclass of `collections.abc.Mapping`.

## Combining and Nesting Patterns

Different types of patterns can be combined and nested. Pattern matching is a powerful tool for processing records structured like nested mappings and sequences, which we often need to read from JSON APIs and databases with semi-structured schemas, like MongoDB, EdgeDB, or PostgreSQL.

## Example 3-2: `get_creators()` Extracts Names of Creators from Media Records

The function `get_creators` takes a dictionary (`record`) and returns a list of creators' names.

```python
def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
```

### Explanation
- **Case 1**: Matches any mapping with `'type': 'book'`, `'api': 2`, and an `'authors'` key mapped to a sequence. Returns the items in the sequence as a new list.
- **Case 2**: Matches any mapping with `'type': 'book'`, `'api': 1`, and an `'author'` key mapped to any object. Returns the object inside a list.
- **Case 3**: Any other mapping with `'type': 'book'` is invalid, raises a `ValueError`.
- **Case 4**: Matches any mapping with `'type': 'movie'` and a `'director'` key mapped to a single object. Returns the object inside a list.
- **Default Case**: Any other subject is invalid, raises a `ValueError`.

### Useful Practices for Handling Semi-Structured Data
- Include a field describing the kind of record (e.g., `'type': 'movie'`).
- Include a field identifying the schema version (e.g., `'api': 2'`) to allow for future evolution of public APIs.
- Have case clauses to handle invalid records of a specific type (e.g., `'book'`), as well as a catch-all case.

## Doctests for `get_creators`

### Test Case 1
```python
b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
print(get_creators(b1))
```
Output:
```python
['Douglas Hofstadter']
```

### Test Case 2
```python
from collections import OrderedDict
b2 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())
print(get_creators(b2))
```
Output:
```python
['Martelli', 'Ravenscroft', 'Holden']
```

### Test Case 3
```python
print(get_creators({'type': 'book', 'pages': 770}))
```
Output:
```python
Traceback (most recent call last):
 ...
ValueError: Invalid 'book' record: {'type': 'book', 'pages': 770}
```

### Test Case 4
```python
print(get_creators('Spam, spam, spam'))
```
Output:
```python
Traceback (most recent call last):
 ...
ValueError: Invalid record: 'Spam, spam, spam'
```

### Explanation
- **Order of Keys**: The order of the keys in the patterns is irrelevant, even if the subject is an `OrderedDict` like `b2`.
- **Partial Matches**: Mapping patterns succeed on partial matches. In the doctests, the `b1` and `b2` subjects include a `'title'` key that does not appear in any `'book'` pattern, yet they match.

### Capturing Extra Key-Value Pairs

To capture extra key-value pairs as a dictionary, use `**variable`. It must be the last in the pattern, and `**_` is forbidden because it would be redundant.

```python
food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')
```
Output:
```python
Ice cream details: {'flavor': 'vanilla', 'cost': 199}
```

### Explanation
- **Dict Unpacking**: `{'category': 'ice cream', **details}` captures all other key-value pairs in the `details` dictionary.



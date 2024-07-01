# Dict Comprehensions

Since Python 2.7, the syntax of list comprehensions (listcomps) and generator expressions (genexps) was adapted to dict comprehensions (dictcomps). A dict comprehension builds a dictionary instance by taking key:value pairs from any iterable.

## Example 3-1: Dict Comprehensions

Here are examples of using dict comprehensions to build two dictionaries from the same list of tuples.

```python
dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {country: code for code, country in dial_codes}
print(country_dial)
```

Output:
```python
{'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62, 
 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}
```

### Explanation
- **Input Data**: A list of tuples named `dial_codes`, where each tuple contains a country dial code and the corresponding country name.
- **Dict Comprehension**: `{country: code for code, country in dial_codes}`
  - **Iterates** through each tuple in `dial_codes`.
  - **Assigns** `country` as the key and `code` as the value.
  - **Builds** the dictionary `country_dial` with country names as keys and their corresponding dial codes as values.

### Advanced Example

```python
filtered_country_dial = {code: country.upper()
                         for country, code in sorted(country_dial.items())
                         if code < 70}
print(filtered_country_dial)
```

Output:
```python
{55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}
```

### Explanation
Certainly! Let's break down and explain the dict comprehension:

```python
{code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
```

### Detailed Explanation

1. **Input Dictionary:**
   We start with the dictionary `country_dial` which looks like this:
   ```python
   country_dial = {
       'Bangladesh': 880, 
       'Brazil': 55, 
       'China': 86, 
       'India': 91, 
       'Indonesia': 62, 
       'Japan': 81, 
       'Nigeria': 234, 
       'Pakistan': 92, 
       'Russia': 7, 
       'United States': 1
   }
   ```

2. **Sorting Items:**
   The comprehension starts with sorting the items of the dictionary by country name:
   ```python
   sorted(country_dial.items())
   ```
   This sorts the items in alphabetical order of the country names:
   ```python
   [
       ('Bangladesh', 880), 
       ('Brazil', 55), 
       ('China', 86), 
       ('India', 91), 
       ('Indonesia', 62), 
       ('Japan', 81), 
       ('Nigeria', 234), 
       ('Pakistan', 92), 
       ('Russia', 7), 
       ('United States', 1)
   ]
   ```

3. **Iterating and Filtering:**
   The dict comprehension iterates through these sorted items. For each pair `(country, code)`, it includes only those pairs where the `code` is less than 70:
   ```python
   if code < 70
   ```
   This filters the list to:
   ```python
   [
       ('Brazil', 55), 
       ('Indonesia', 62), 
       ('Russia', 7), 
       ('United States', 1)
   ]
   ```

4. **Transforming and Constructing:**
   For each filtered pair `(country, code)`, it constructs a new dictionary with `code` as the key and the uppercase version of `country` as the value:
   ```python
   {code: country.upper()}
   ```
   This transforms the filtered pairs to:
   ```python
   {
       55: 'BRAZIL', 
       62: 'INDONESIA', 
       7: 'RUSSIA', 
       1: 'UNITED STATES'
   }
   ```

### Step-by-Step Breakdown

Let's walk through the entire comprehension step by step:

1. **Sort `country_dial.items()`:**
   - Sorted items: 
     ```python
     [('Bangladesh', 880), ('Brazil', 55), ('China', 86), ('India', 91), ('Indonesia', 62), 
      ('Japan', 81), ('Nigeria', 234), ('Pakistan', 92), ('Russia', 7), ('United States', 1)]
     ```

2. **Iterate and filter:**
   - Iteration 1: ('Bangladesh', 880) -> code is not less than 70 -> not included
   - Iteration 2: ('Brazil', 55) -> code is less than 70 -> included
   - Iteration 3: ('China', 86) -> code is not less than 70 -> not included
   - Iteration 4: ('India', 91) -> code is not less than 70 -> not included
   - Iteration 5: ('Indonesia', 62) -> code is less than 70 -> included
   - Iteration 6: ('Japan', 81) -> code is not less than 70 -> not included
   - Iteration 7: ('Nigeria', 234) -> code is not less than 70 -> not included
   - Iteration 8: ('Pakistan', 92) -> code is not less than 70 -> not included
   - Iteration 9: ('Russia', 7) -> code is less than 70 -> included
   - Iteration 10: ('United States', 1) -> code is less than 70 -> included

3. **Transform and construct:**
   - ('Brazil', 55) -> {55: 'BRAZIL'}
   - ('Indonesia', 62) -> {62: 'INDONESIA'}
   - ('Russia', 7) -> {7: 'RUSSIA'}
   - ('United States', 1) -> {1: 'UNITED STATES'}

### Final Output

The final dictionary constructed by the comprehension:
```python
{55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}
```
## Summary
- **Dict Comprehensions**: An efficient way to create dictionaries from iterables.
- **Key-Value Pairs**: You can swap keys and values, sort, filter, and modify values during the comprehension process.
- **Advanced Usage**: Combine sorting, filtering, and value transformations for more complex dictionary creation.

Dict comprehensions are a natural next step if you're familiar with list comprehensions. They are powerful tools in Python for building dictionaries in a clear and concise way. Becoming fluent in comprehension syntax is highly beneficial for writing clean and efficient Python code.

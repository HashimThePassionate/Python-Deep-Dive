# Generic Mappings

## Overview

Generic mapping types are annotated as `MappingType[KeyType, ValueType]`. In Python ≥ 3.9, the built-in `dict` and the mapping types in `collections` and `collections.abc` accept this notation. For earlier versions, you must use `typing.Dict` and other mapping types from the `typing` module.

## Practical Example

The following example demonstrates a function returning an inverted index to search Unicode characters by name. This is a variation of Example 4-21, more suitable for server-side code.

### Function Explanation

Given starting and ending Unicode character codes, the `name_index` function returns a `dict[str, set[str]]`. This is an inverted index mapping each word to a set of characters that have that word in their names.

For example, after indexing ASCII characters from 32 to 64:
```python
index = name_index(32, 65)
print(index['SIGN'])  # Output: {'$', '>', '=', '+', '<', '%', '#'}
print(index['DIGIT']) # Output: {'8', '5', '6', '2', '3', '0', '1', '4', '7', '9'}
print(index['DIGIT'] & index['EIGHT']) # Output: {'8'}
```

### Example Code (charindex.py)

```python
import sys
import re
import unicodedata
from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1

def tokenize(text: str) -> Iterator[str]:
    """Return iterable of uppercased words"""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()

def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index
```

### Key Points

1. **Generator Function**: The `tokenize` function is a generator function. It returns an iterable of uppercased words.
   
2. **Type Annotation**: The local variable `index` is annotated. Without the hint, Mypy would indicate the need for a type annotation.
   
3. **Walrus Operator**: The walrus operator `:=` is used in the `if` condition to assign the result of `unicodedata.name()` to `name`. If the result is an empty string `''` (falsy), the index is not updated.

### Explanation of Components

- **Imports**: 
  - `sys`, `re`, `unicodedata` are standard libraries.
  - `Iterator` is imported from `collections.abc`.

- **Constants**:
  - `RE_WORD` is a regex pattern to find words.
  - `STOP_CODE` is set to the maximum Unicode code point.

- **Functions**:
  - `tokenize(text: str) -> Iterator[str]`: Yields uppercased words from the input text.
  - `name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]`: Creates an inverted index mapping words to sets of characters with those words in their names.

### Detailed Example

#### `tokenize` Function

```python
def tokenize(text: str) -> Iterator[str]:
    """Return iterable of uppercased words"""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()
```
- **Purpose**: To split the input text into words and yield them in uppercase.
- **Usage**: 
  ```python
  words = list(tokenize("Hello World"))
  print(words)  # Output: ['HELLO', 'WORLD']
  ```

#### Explanation:
- The `tokenize` function takes a string `text` and uses a regular expression (`RE_WORD`) to find all word matches.
- It then yields each matched word in uppercase using `match.group().upper()`.
- This function returns an iterator of uppercased words.

#### `name_index` Function

```python
def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index
```
- **Purpose**: To create an inverted index of Unicode character names.
- **Usage**: 
  ```python
  index = name_index(32, 65)
  print(index['SIGN'])  # Output: {'$', '>', '=', '+', '<', '%', '#'}
  print(index['DIGIT']) # Output: {'8', '5', '6', '2', '3', '0', '1', '4', '7', '9'}
  ```

#### Explanation:
- The `name_index` function takes two integer arguments `start` and `end`, defaulting to 32 and `STOP_CODE` (maximum Unicode value) respectively.
- It initializes an empty dictionary `index` to store the inverted index.
- It iterates over the Unicode characters in the specified range.
- For each character, it gets the Unicode name using `unicodedata.name(char, '')`. If the name is not an empty string, it tokenizes the name into words.
- Each word is used as a key in the `index` dictionary, with the character being added to the set of characters for that word.
- The function returns the `index` dictionary.

### Python > 3.10 Features

Python 3.10 introduced structural pattern matching. Here’s an example of using pattern matching to classify characters based on their Unicode names:

#### `classify_characters` Function

```python
def classify_characters(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    classification: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            match name:
                case name if "SIGN" in name:
                    classification.setdefault('SIGN', set()).add(char)
                case name if "DIGIT" in name:
                    classification.setdefault('DIGIT', set()).add(char)
                case _:
                    classification.setdefault('OTHER', set()).add(char)
    return classification

# Usage
classification = classify_characters(32, 65)
print(classification['SIGN'])  # Output: {'$', '>', '=', '+', '<', '%', '#'}
print(classification['DIGIT']) # Output: {'8', '5', '6', '2', '3', '0', '1', '4', '7', '9'}
```

### Explanation:

- **Purpose**: To classify Unicode characters based on the presence of certain words in their names using pattern matching.
- **Pattern Matching**: The `match name` statement matches the name against specific patterns:
  - If "SIGN" is in the name, the character is added to the 'SIGN' set.
  - If "DIGIT" is in the name, the character is added to the 'DIGIT' set.
  - Otherwise, the character is added to the 'OTHER' set.

#### Detailed Breakdown:

- The `classify_characters` function takes two integer arguments `start` and `end`, defaulting to 32 and `STOP_CODE` respectively.
- It initializes an empty dictionary `classification` to store the classified characters.
- It iterates over the Unicode characters in the specified range.
- For each character, it gets the Unicode name using `unicodedata.name(char, '')`. If the name is not an empty string, it uses pattern matching to classify the character based on the presence of certain words in the name.
- The function returns the `classification` dictionary.

This section has covered the basics of generic mappings and provided practical examples of creating an inverted index and classifying characters using both traditional methods and features introduced in Python > 3.10. The examples illustrate the use of type annotations, generator functions, the walrus operator, and structural pattern matching.
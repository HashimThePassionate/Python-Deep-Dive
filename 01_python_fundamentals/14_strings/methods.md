# ✨ Methods of String and Bytes Objects

## 📋 Table of Contents

- [✨ Methods of String and Bytes Objects](#-methods-of-string-and-bytes-objects)
  - [📋 Table of Contents](#-table-of-contents)
    - [🌟 String and Bytes Object Methods Overview](#-string-and-bytes-object-methods-overview)
    - [🎨 `capitalize()`](#-capitalize)
    - [🎨 `center()`](#-center)
    - [🎨 `count()`](#-count)
    - [🎨 `decode()` (bytes only)](#-decode-bytes-only)
    - [🎨 `encode()` (str only)](#-encode-str-only)
    - [🎨 `endswith()`](#-endswith)
    - [🎨 `expandtabs()`](#-expandtabs)
    - [🎨 `find()`](#-find)
    - [🎨 `format()` (str only)](#-format-str-only)
    - [🎨 `format_map()` (str only, v3 only)](#-format_map-str-only-v3-only)
    - [🎨 `index()`](#-index)
    - [🎨 `isalnum()`](#-isalnum)
    - [🎨 `isalpha()`](#-isalpha)
    - [🎨 `isdecimal()` (str only, v3 only)](#-isdecimal-str-only-v3-only)
    - [🎨 `isdigit()`](#-isdigit)
    - [🎨 `isidentifier()` (str only, v3 only)](#-isidentifier-str-only-v3-only)
    - [🎨 `islower()`](#-islower)
    - [🎨 `isnumeric()` (str only, v3 only)](#-isnumeric-str-only-v3-only)
    - [🎨 `isprintable()` (str only, v3 only)](#-isprintable-str-only-v3-only)
    - [🎨 `isspace()`](#-isspace)
    - [🎨 `istitle()`](#-istitle)
    - [🎨 `isupper()`](#-isupper)
    - [🎨 `join()`](#-join)
    - [🎨 `ljust()`](#-ljust)
    - [🎨 `lower()`](#-lower)
    - [🎨 `lstrip()`](#-lstrip)
    - [🎨 `replace()`](#-replace)
    - [🎨 `rfind()`](#-rfind)
    - [🎨 `rindex()`](#-rindex)
    - [🎨 `rjust()`](#-rjust)
    - [🎨 `rstrip()`](#-rstrip)
    - [🎨 `split()`](#-split)
    - [🎨 `splitlines()`](#-splitlines)
    - [🎨 `startswith()`](#-startswith)
    - [🎨 `strip()`](#-strip)
    - [🎨 `swapcase()`](#-swapcase)
    - [🎨 `title()`](#-title)
    - [🎨 `translate()`](#-translate)
    - [🎨 `upper()`](#-upper)
  - [🛠️ Section: The string Module](#️-section-the-string-module)
    - [🛠️ `ascii_letters`](#️-ascii_letters)
    - [🛠️ `ascii_lowercase`](#️-ascii_lowercase)
    - [🛠️ `ascii_uppercase`](#️-ascii_uppercase)
    - [🛠️ `digits`](#️-digits)
    - [🛠️ `hexdigits`](#️-hexdigits)
    - [🛠️ `octdigits`](#️-octdigits)
    - [🛠️ `punctuation`](#️-punctuation)
    - [🛠️ `printable`](#️-printable)
    - [🛠️ `whitespace`](#️-whitespace)
  - [✨ Section: String Formatting](#-section-string-formatting)
    - [🌟 Basic Formatting with `format()`](#-basic-formatting-with-format)
    - [🌟 Positional and Keyword Arguments](#-positional-and-keyword-arguments)
    - [🌟 Nested Formatting](#-nested-formatting)
  - [🎨 Section: Legacy String Formatting with `%`](#-section-legacy-string-formatting-with-)
    - [🌟 Basic Usage](#-basic-usage)
    - [🌟 Common Format Specifiers](#-common-format-specifiers)
  - [🛠️ Section: Text Wrapping and Filling](#️-section-text-wrapping-and-filling)
    - [🌟 `wrap()`](#-wrap)
    - [🌟 `fill()`](#-fill)
  - [🎨 Section: The pprint Module](#-section-the-pprint-module)
    - [🌟 `pprint()`](#-pprint)

---

In Python, both `str` and `bytes` objects are immutable sequences. This means that once a string or bytes object is created, it cannot be altered. All operations performed on these objects, such as repetition, concatenation, indexing, and slicing, return a new object of the same type. Let's dive into the methods provided by these objects, keeping in mind that the string (`str`) methods return a Unicode string, while the `bytes` methods return a bytestring.

---




### 🌟 String and Bytes Object Methods Overview

Python provides various methods to manipulate strings and bytes. These methods do not alter the original object but return new objects based on the operations performed. This section will guide you through the most commonly used methods.

---

### 🎨 `capitalize()`

- **Usage**: `s.capitalize()`
- **Description**: Returns a copy of the string `s` with the first character capitalized (uppercase) and all other characters in lowercase.
  
```python
example_str = "hello World"
capitalized_str = example_str.capitalize()
print(capitalized_str)  # Output: "Hello world"
```

---

### 🎨 `center()`

- **Usage**: `s.center(n, fillchar=' ')`
- **Description**: Returns a string of length `n`, with the original string `s` centered and surrounded by the `fillchar` character on both sides.

```python
example_str = "hi"
centered_str = example_str.center(6, '_')
print(centered_str)  # Output: "__hi__"
```

---

### 🎨 `count()`

- **Usage**: `s.count(sub, start=0, end=sys.maxsize)`
- **Description**: Returns the number of non-overlapping occurrences of substring `sub` in the string `s` between the `start` and `end` positions.

```python
example_str = "banana"
count_na = example_str.count('na')
print(count_na)  # Output: 2
```

---

### 🎨 `decode()` (bytes only)

- **Usage**: `s.decode(encoding='utf-8', errors='strict')`
- **Description**: Converts a bytestring `s` to a string using the specified `encoding`. Handles errors based on the `errors` parameter.

```python
byte_data = b'hello'
decoded_str = byte_data.decode('utf-8')
print(decoded_str)  # Output: "hello"
```

---

### 🎨 `encode()` (str only)

- **Usage**: `s.encode(encoding=None, errors='strict')`
- **Description**: Converts a string `s` to a bytes object using the specified `encoding`. Handles errors based on the `errors` parameter.

```python
str_data = "hello"
encoded_data = str_data.encode('utf-8')
print(encoded_data)  # Output: b'hello'
```

---

### 🎨 `endswith()`

- **Usage**: `s.endswith(suffix, start=0, end=sys.maxsize)`
- **Description**: Returns `True` if the string `s` ends with the specified `suffix`; otherwise, returns `False`. The `suffix` can be a tuple of strings to check for multiple endings.

```python
example_str = "python"
ends_with_on = example_str.endswith('on')
print(ends_with_on)  # Output: True
```

---

### 🎨 `expandtabs()`

- **Usage**: `s.expandtabs(tabsize=8)`
- **Description**: Returns a copy of the string `s` where each tab character is replaced with spaces. The number of spaces is determined by the `tabsize` parameter.

```python
example_str = "hello\tworld"
expanded_str = example_str.expandtabs(4)
print(expanded_str)  # Output: "hello   world"
```

---

### 🎨 `find()`

- **Usage**: `s.find(sub, start=0, end=sys.maxsize)`
- **Description**: Returns the lowest index in `s` where substring `sub` is found. Returns `-1` if the substring is not found.

```python
example_str = "banana"
index_na = example_str.find('na')
print(index_na)  # Output: 2
```

---

### 🎨 `format()` (str only)

- **Usage**: `s.format(*args, **kwargs)`
- **Description**: Returns a formatted string using the given positional and keyword arguments.

```python
formatted_str = "Hello, {}!".format("World")
print(formatted_str)  # Output: "Hello, World!"
```

---

### 🎨 `format_map()` (str only, v3 only)

- **Usage**: `s.format_map(mapping)`
- **Description**: Similar to `format()`, but uses a mapping dictionary to format the string.

```python
mapping = {'name': 'Alice', 'age': 25}
formatted_str = "Name: {name}, Age: {age}".format_map(mapping)
print(formatted_str)  # Output: "Name: Alice, Age: 25"
```

---

### 🎨 `index()`

- **Usage**: `s.index(sub, start=0, end=sys.maxsize)`
- **Description**: Similar to `find()`, but raises a `ValueError` if the substring is not found.

```python
example_str = "banana"
try:
    index_na = example_str.index('na')
    print(index_na)  # Output: 2
except ValueError:
    print("Substring not found")
```

---

### 🎨 `isalnum()`

- **Usage**: `s.isalnum()`
- **Description**: Returns `True` if all characters in `s` are alphanumeric (letters or digits) and the string is not empty.

```python
example_str = "abc123"
is_alnum = example_str.isalnum()
print(is_alnum)  # Output: True
```

---

### 🎨 `isalpha()`

- **Usage**: `s.isalpha()`
- **Description**: Returns `True` if all characters in `s` are alphabetic (letters) and the string is not empty.

```python
example_str = "abc"
is_alpha = example_str.isalpha()
print(is_alpha)  # Output: True
```

---

### 🎨 `isdecimal()` (str only, v3 only)

- **Usage**: `s.isdecimal()`
- **Description**: Returns `True` if all characters in `s` are decimal digits and the string is not empty.

```python
example_str = "123"
is_decimal = example_str.isdecimal()
print(is_decimal)  # Output: True
```

---

### 🎨 `isdigit()`

- **Usage**: `s.isdigit()`
- **Description**: Returns `True` if all characters in `s` are digits and the string is not empty.

```python
example_str = "123"
is_digit = example_str.isdigit()
print(is_digit)  # Output: True
```

---

### 🎨 `isidentifier()` (str only, v3 only)

- **Usage**: `s.isidentifier()`
- **Description**: Returns `True` if `s` is a valid Python identifier.

```python
example_str = "variable_name"
is_identifier = example_str.isidentifier()
print(is_identifier)  # Output: True
```

---

### 🎨 `islower()`

- **Usage**: `s.islower()`
- **Description**: Returns `True` if all alphabetic characters in `s` are lowercase.

```python
example_str = "hello"
is_lower = example_str.islower()
print(is_lower)  # Output: True
```

---

### 🎨 `isnumeric()` (str only, v3 only)

- **Usage**: `s.isnumeric()`
- **Description**: Returns `True` if all characters in `s` are numeric characters.

```python
example_str = "123"
is_numeric = example_str.isnumeric()
print(is_numeric)  # Output: True
```

---

### 🎨 `isprintable()` (str only, v3 only)

- **Usage**: `s.isprintable()`
- **Description**: Returns `True` if all characters in `s` are printable or the string is empty.

```python
example_str = "Hello, World!"
is_printable = example_str.isprintable()
print(is_printable)  # Output: True
```

---

### 🎨 `isspace()`

- **Usage**: `s.isspace()`
- **Description**: Returns `True` if all characters in `s` are whitespace and the string is not empty.

```python
example_str = "   "
is_space = example_str.isspace()
print(is_space)  # Output: True
```

---

### 🎨 `istitle()`

- **Usage**: `s.istitle()`
-

 **Description**: Returns `True` if `s` is titlecased (first letter of each word is uppercase).

```python
example_str = "Hello World"
is_title = example_str.istitle()
print(is_title)  # Output: True
```

---

### 🎨 `isupper()`

- **Usage**: `s.isupper()`
- **Description**: Returns `True` if all alphabetic characters in `s` are uppercase.

```python
example_str = "HELLO"
is_upper = example_str.isupper()
print(is_upper)  # Output: True
```

---

### 🎨 `join()`

- **Usage**: `s.join(seq)`
- **Description**: Returns a string that is the concatenation of the strings in `seq`, with `s` as the separator.

```python
seq = ["Hello", "World"]
joined_str = " ".join(seq)
print(joined_str)  # Output: "Hello World"
```

---

### 🎨 `ljust()`

- **Usage**: `s.ljust(n, fillchar=' ')`
- **Description**: Returns a string of length `n`, with the original string `s` left-justified, and the remaining space filled with `fillchar`.

```python
example_str = "hello"
ljust_str = example_str.ljust(10, '_')
print(ljust_str)  # Output: "hello_____"
```

---

### 🎨 `lower()`

- **Usage**: `s.lower()`
- **Description**: Returns a copy of `s` with all characters converted to lowercase.

```python
example_str = "HELLO"
lower_str = example_str.lower()
print(lower_str)  # Output: "hello"
```

---

### 🎨 `lstrip()`

- **Usage**: `s.lstrip(x=string.whitespace)`
- **Description**: Returns a copy of `s` with leading characters removed, based on the characters found in `x`.

```python
example_str = "   hello"
lstrip_str = example_str.lstrip()
print(lstrip_str)  # Output: "hello"
```

---

### 🎨 `replace()`

- **Usage**: `s.replace(old, new, maxsplit=sys.maxsize)`
- **Description**: Returns a copy of `s` with occurrences of the substring `old` replaced by `new`. The `maxsplit` parameter limits the number of replacements.

```python
example_str = "banana"
replaced_str = example_str.replace('a', 'o', 2)
print(replaced_str)  # Output: "bonona"
```

---

### 🎨 `rfind()`

- **Usage**: `s.rfind(sub, start=0, end=sys.maxsize)`
- **Description**: Returns the highest index in `s` where substring `sub` is found. Returns `-1` if the substring is not found.

```python
example_str = "banana"
index_na = example_str.rfind('na')
print(index_na)  # Output: 4
```

---

### 🎨 `rindex()`

- **Usage**: `s.rindex(sub, start=0, end=sys.maxsize)`
- **Description**: Similar to `rfind()`, but raises a `ValueError` if the substring is not found.

```python
example_str = "banana"
try:
    index_na = example_str.rindex('na')
    print(index_na)  # Output: 4
except ValueError:
    print("Substring not found")
```

---

### 🎨 `rjust()`

- **Usage**: `s.rjust(n, fillchar=' ')`
- **Description**: Returns a string of length `n`, with the original string `s` right-justified, and the remaining space filled with `fillchar`.

```python
example_str = "hello"
rjust_str = example_str.rjust(10, '_')
print(rjust_str)  # Output: "_____hello"
```

---

### 🎨 `rstrip()`

- **Usage**: `s.rstrip(x=string.whitespace)`
- **Description**: Returns a copy of `s` with trailing characters removed, based on the characters found in `x`.

```python
example_str = "hello   "
rstrip_str = example_str.rstrip()
print(rstrip_str)  # Output: "hello"
```

---

### 🎨 `split()`

- **Usage**: `s.split(sep=None, maxsplit=sys.maxsize)`
- **Description**: Returns a list of words in `s`, using `sep` as the delimiter. If `sep` is not specified, any whitespace string is a separator.

```python
example_str = "hello world"
split_str = example_str.split()
print(split_str)  # Output: ["hello", "world"]
```

---

### 🎨 `splitlines()`

- **Usage**: `s.splitlines(keepends=False)`
- **Description**: Returns a list of lines in `s`, breaking at line boundaries. If `keepends` is `True`, line breaks are included in the result.

```python
example_str = "hello\nworld"
splitlines_str = example_str.splitlines()
print(splitlines_str)  # Output: ["hello", "world"]
```

---

### 🎨 `startswith()`

- **Usage**: `s.startswith(prefix, start=0, end=sys.maxsize)`
- **Description**: Returns `True` if the string `s` starts with the specified `prefix`; otherwise, returns `False`.

```python
example_str = "python"
starts_with_py = example_str.startswith('py')
print(starts_with_py)  # Output: True
```

---

### 🎨 `strip()`

- **Usage**: `s.strip(x=string.whitespace)`
- **Description**: Returns a copy of `s` with leading and trailing characters removed, based on the characters found in `x`.

```python
example_str = "   hello   "
strip_str = example_str.strip()
print(strip_str)  # Output: "hello"
```

---

### 🎨 `swapcase()`

- **Usage**: `s.swapcase()`
- **Description**: Returns a copy of `s` with uppercase characters converted to lowercase and vice versa.

```python
example_str = "Hello World"
swapcase_str = example_str.swapcase()
print(swapcase_str)  # Output: "hELLO wORLD"
```

---

### 🎨 `title()`

- **Usage**: `s.title()`
- **Description**: Returns a copy of `s` with the first character of each word capitalized and all other letters in lowercase.

```python
example_str = "hello world"
title_str = example_str.title()
print(title_str)  # Output: "Hello World"
```

---

### 🎨 `translate()`

- **Usage**: `s.translate(table)`
- **Description**: Returns a copy of `s` where each character in `s` is mapped to the character in the `table` dictionary.

```python
translation_table = str.maketrans('aeiou', '12345')
example_str = "hello world"
translated_str = example_str.translate(translation_table)
print(translated_str)  # Output: "h2ll4 w4rld"
```

---

### 🎨 `upper()`

- **Usage**: `s.upper()`
- **Description**: Returns a copy of `s` with all characters converted to uppercase.

```python
example_str = "hello"
upper_str = example_str.upper()
print(upper_str)  # Output: "HELLO"
```

---

## 🛠️ Section: The string Module

The `string` module provides several constants and classes for working with strings. Let's go over some of the most useful attributes:

---

### 🛠️ `ascii_letters`

- **Description**: A string containing all the lowercase and uppercase letters in ASCII.

```python
import string
print(string.ascii_letters)  # Output: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

---

### 🛠️ `ascii_lowercase`

- **Description**: A string containing all the lowercase letters in ASCII.

```python
import string
print(string.ascii_lowercase)  # Output: "abcdefghijklmnopqrstuvwxyz"
```

---

### 🛠️ `ascii_uppercase`

- **Description**: A string containing all the uppercase letters in ASCII.

```python
import string
print(string.ascii_uppercase)  # Output: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

---

### 🛠️ `digits`

- **Description**: A string containing all the digits from 0 to 9.

```python
import string
print(string.digits)  # Output: "0123456789"
```

---

### 🛠️ `hexdigits`

- **Description**: A string containing all the hexadecimal digits (0-9, a-f, A-F).

```python
import string
print(string.hexdigits)  # Output: "0123456789abcdefABCDEF"
```

---

### 🛠️ `octdigits`

- **Description**: A string containing all the octal digits (0-7).

```python
import string
print(string.octdigits)  # Output: "01234567"
```

---

### 🛠️ `punctuation`

- **Description**: A string containing all ASCII punctuation characters.

```python
import string
print(string.punctuation)  # Output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

---

### 🛠️ `printable`

- **Description**: A string containing all characters that

 are considered printable.

```python
import string
print(string.printable)  # Output: Digits, letters, punctuation, and whitespace characters
```

---

### 🛠️ `whitespace`

- **Description**: A string containing all characters that are considered whitespace.

```python
import string
print(string.whitespace)  # Output: "\t\n\x0b\x0c\r "
```

---

## ✨ Section: String Formatting

Python's string formatting allows you to create formatted strings using placeholders, which are replaced with specific values. Let's explore the different ways you can format strings.

---

### 🌟 Basic Formatting with `format()`

- **Usage**: `'{}'.format(value)`
- **Description**: The `format()` method allows you to format strings using placeholders. The placeholders are defined using curly braces `{}`.

```python
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # Output: "My name is Alice and I am 30 years old."
```

---

### 🌟 Positional and Keyword Arguments

- **Usage**: `'{} {}`.format(arg1, arg2)` or `'{name} {age}'.format(name='Alice', age=30)`
- **Description**: You can use both positional and keyword arguments in the `format()` method.

```python
formatted_str = "Name: {0}, Age: {1}".format("Alice", 30)
print(formatted_str)  # Output: "Name: Alice, Age: 30"

formatted_str = "Name: {name}, Age: {age}".format(name="Alice", age=30)
print(formatted_str)  # Output: "Name: Alice, Age: 30"
```

---

### 🌟 Nested Formatting

- **Description**: You can nest formatting expressions within the `format()` method to create complex formatting rules.

```python
nested_str = "The result is {0:.2f}".format(3.14159)
print(nested_str)  # Output: "The result is 3.14"
```

---

## 🎨 Section: Legacy String Formatting with `%`

Python also supports an older method of string formatting using the `%` operator, similar to C's `printf` style.

---

### 🌟 Basic Usage

- **Usage**: `format % values`
- **Description**: The `%` operator is used for string formatting, where `format` is a string containing format specifiers, and `values` are the values to format.

```python
name = "Alice"
age = 30
formatted_str = "My name is %s and I am %d years old." % (name, age)
print(formatted_str)  # Output: "My name is Alice and I am 30 years old."
```

---

### 🌟 Common Format Specifiers

- **`%d`**: Integer
- **`%f`**: Floating-point number
- **`%s`**: String

---

## 🛠️ Section: Text Wrapping and Filling

The `textwrap` module provides functions to format text by wrapping it into lines of a specified width.

---

### 🌟 `wrap()`

- **Usage**: `textwrap.wrap(s, width=70)`
- **Description**: Returns a list of strings, each no longer than the specified width.

```python
import textwrap

text = "This is a very long line of text that needs to be wrapped."
wrapped_text = textwrap.wrap(text, width=20)
print(wrapped_text)  # Output: ['This is a very long', 'line of text that', 'needs to be wrapped.']
```

---

### 🌟 `fill()`

- **Usage**: `textwrap.fill(s, width=70)`
- **Description**: Returns a single string, with the text wrapped into lines of the specified width.

```python
import textwrap

text = "This is a very long line of text that needs to be wrapped."
filled_text = textwrap.fill(text, width=20)
print(filled_text)  
# Output:
# This is a very long
# line of text that
# needs to be wrapped.
```

---

## 🎨 Section: The pprint Module

The `pprint` module provides a way to pretty-print complex data structures in a more readable format.

---

### 🌟 `pprint()`

- **Usage**: `pprint.pprint(object, stream=sys.stdout)`
- **Description**: Pretty-prints the `object` to the specified `stream`. By default, it prints to `sys.stdout`.

```python
import pprint

data = {'name': 'Alice', 'age': 30, 'job': 'Engineer'}
pprint.pprint(data)
# Output:
# {'age': 30, 'job': 'Engineer', 'name': 'Alice'}
```
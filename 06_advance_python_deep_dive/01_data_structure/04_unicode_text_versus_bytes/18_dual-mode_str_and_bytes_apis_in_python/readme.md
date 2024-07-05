#   Dual-Mode `str` and `bytes` APIs in Python

## Introduction
Python’s standard library has functions that can accept `str` (string) or `bytes` (binary data) arguments and behave differently depending on the type. This behavior can be observed in modules like `re` (regular expressions) and `os`.

## Regular Expressions with `str` and `bytes`
Regular expressions (regex) in Python can be created with `str` or `bytes`. The type used affects the behavior of the regex patterns.

### Example: Regular Expressions with `str` and `bytes`
In this example, we'll see how `str` and `bytes` patterns differ when matching Unicode and ASCII characters using the name 'Hashim'.

```python
import re

# Compile regular expressions for str and bytes
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

# Unicode text containing Tamil digits and the name 'Hashim'
text_str = ("Hashim saw \u0be7\u0bed\u0be8\u0bef as 1729 = 1³ + 12³ = 9³ + 10³.")
text_bytes = text_str.encode('utf_8')

# Print text in both formats
print(f'Text\n {text_str!r}')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str))
print(' bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print(' str :', re_words_str.findall(text_str))
print(' bytes:', re_words_bytes.findall(text_bytes))
```

### Explanation of Example
1. **Importing the `re` Module**: The `re` module is used for working with regular expressions in Python.
   
2. **Compiling Regular Expressions**:
   - `re_numbers_str = re.compile(r'\d+')`: Compiles a regex pattern to match one or more digits. Since the pattern is a string (`str`), it will match Unicode digits.
   - `re_words_str = re.compile(r'\w+')`: Compiles a regex pattern to match one or more word characters (letters, digits, or underscores). As a `str` pattern, it matches Unicode characters.
   - `re_numbers_bytes = re.compile(rb'\d+')`: Compiles a regex pattern to match one or more digits. Since the pattern is bytes (`bytes`), it will match only ASCII digits.
   - `re_words_bytes = re.compile(rb'\w+')`: Compiles a regex pattern to match one or more word characters. As a `bytes` pattern, it matches only ASCII characters.

3. **Text to Search**:
   - `text_str`: A string containing Unicode text with Tamil digits and the name 'Hashim'.
   - `text_bytes`: The byte-encoded version of `text_str`.

4. **Printing Text**:
   - `print(f'Text\n {text_str!r}')`: Prints the raw representation of the string `text_str`. The `!r` format specifier shows the internal format of the string, including escape sequences like `\u0be7`.

5. **Finding Matches**:
   - `print('Numbers')`:
     - `print(' str :', re_numbers_str.findall(text_str))`: Finds all sequences of digits in `text_str` using the `str` pattern. This will match both ASCII and Tamil digits.
     - `print(' bytes:', re_numbers_bytes.findall(text_bytes))`: Finds all sequences of digits in `text_bytes` using the `bytes` pattern. This will match only ASCII digits.
   - `print('Words')`:
     - `print(' str :', re_words_str.findall(text_str))`: Finds all sequences of word characters in `text_str` using the `str` pattern. This will match letters (including 'Hashim'), superscripts, Tamil, and ASCII digits.
     - `print(' bytes:', re_words_bytes.findall(text_bytes))`: Finds all sequences of word characters in `text_bytes` using the `bytes` pattern. This will match only ASCII letters and digits (including 'Hashim').

### Detailed Explanation of Output
When you run the above script, you'll get the following output:

#### Text Output
The line `print(f'Text\n {text_str!r}')` prints the raw representation of the `text_str`. The `!r` format specifier calls the `__repr__` method of the object, which includes escape sequences in the output.

#### Numbers Output
- **`str` pattern**: `print(' str :', re_numbers_str.findall(text_str))` will print all sequences of digits found in the string `text_str`, including both ASCII and Tamil digits.
- **`bytes` pattern**: `print(' bytes:', re_numbers_bytes.findall(text_bytes))` will print all sequences of ASCII digits found in the byte-encoded text `text_bytes`.

#### Words Output
- **`str` pattern**: `print(' str :', re_words_str.findall(text_str))` will print all sequences of word characters found in the string `text_str`, including letters (such as 'Hashim'), superscripts, Tamil, and ASCII digits.
- **`bytes` pattern**: `print(' bytes:', re_words_bytes.findall(text_bytes))` will print all sequences of ASCII word characters found in the byte-encoded text `text_bytes`, including letters (such as 'Hashim') and ASCII digits.

### ASCII-only Matching in Regular Expressions
You can make `str` regex patterns match only ASCII characters by using the `re.ASCII` flag. This can be useful if you want the behavior of `str` patterns to be similar to `bytes` patterns.

#### Example: ASCII-only Matching with `re.ASCII` Flag
```python
import re

# Compile regular expressions with re.ASCII flag
re_numbers_ascii = re.compile(r'\d+', re.ASCII)
re_words_ascii = re.compile(r'\w+', re.ASCII)

# Text containing Unicode and ASCII characters
text_str = "Hashim saw 123 and \u0be7\u0bed\u0be8\u0bef."

# Print ASCII-only matches
print('Numbers (ASCII-only)')
print(' str :', re_numbers_ascii.findall(text_str))
print('Words (ASCII-only)')
print(' str :', re_words_ascii.findall(text_str))
```

#### Explanation of Example
- `re_numbers_ascii = re.compile(r'\d+', re.ASCII)`: Compiles a regex pattern to match one or more ASCII digits.
- `re_words_ascii = re.compile(r'\w+', re.ASCII)`: Compiles a regex pattern to match one or more ASCII word characters.
- `print(' str :', re_numbers_ascii.findall(text_str))`: Finds all sequences of ASCII digits in `text_str`.
- `print(' str :', re_words_ascii.findall(text_str))`: Finds all sequences of ASCII word characters in `text_str`.

## Working with `os` Functions
The `os` module functions that accept filenames or pathnames can take `str` or `bytes` arguments. This is useful because not all filenames can be decoded into `str`.

### Example: `os.listdir` with `str` and `bytes`
Let's see how `os.listdir` behaves differently with `str` and `bytes` arguments.

```python
import os

# List directory contents with str argument
print(os.listdir('.'))

# List directory contents with bytes argument
print(os.listdir(b'.'))
```

### Explanation of Example
- **`os.listdir('.')`** returns filenames as `str`.
- **`os.listdir(b'.')`** returns filenames as `bytes`. For example, the filename `digits-of-π.txt` is returned as `b'digits-of-\xcf\x80.txt'` where `\xcf\x80` is the UTF-8 encoding of the Greek letter pi.

### Encoding and Decoding with `os.fencode` and `os.fsdecode`
These functions help in manually handling `str` or `bytes` sequences for filenames or pathnames.

#### Example: Encoding and Decoding Filenames
```python
import os

# Encode a str to bytes
encoded_path = os.fsencode('digits-of-π.txt')
print(f'Encoded: {encoded_path}')

# Decode bytes to str
decoded_path = os.fsdecode(encoded_path)
print(f'Decoded: {decoded_path}')
```

#### Explanation of Example
- `encoded_path = os.fsencode('digits-of-π.txt')`: Encodes the `str` filename `digits-of-π.txt` to `bytes`.
- `print(f'Encoded: {encoded_path}')`: Prints the encoded `bytes` representation of the filename.
- `decoded_path = os.fsdecode(encoded_path)`: Decodes the `bytes` filename back to `str`.
- `print(f'Decoded: {decoded_path}')`: Prints the decoded `str` representation of the filename.

## Conclusion
Understanding the difference between `str` and `bytes` in Python is crucial, especially when dealing with text and filenames that may not be ASCII. By using the right type and functions, you can handle any text or filename scenario in your Python applications.

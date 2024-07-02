# Byte Essentials
The new binary sequence types in Python 3 are different from the `str` type in Python 2. There are two basic built-in types for binary sequences:

- `bytes` (immutable)
- `bytearray` (mutable)

The Python documentation may refer to both as "byte string," but we will avoid this term to prevent confusion.

## Basics of Binary Sequences

- Each item in `bytes` or `bytearray` is an integer from 0 to 255, not a one-character string.
- A slice of a binary sequence produces a binary sequence of the same type, including slices of length 1.

### Example 4-2: Bytes and Bytearray

```python
cafe = bytes('café', encoding='utf_8')
print(cafe)  # Output: b'caf\xc3\xa9'

print(cafe[0])  # Output: 99

print(cafe[:1])  # Output: b'c'

cafe_arr = bytearray(cafe)
print(cafe_arr)  # Output: bytearray(b'caf\xc3\xa9')

print(cafe_arr[-1:])  # Output: bytearray(b'\xa9')
```

- `bytes` can be built from a `str` with an encoding.
- Each item is an integer in the range(256).
- Slices of `bytes` are also `bytes`, even slices of a single byte.
- There is no literal syntax for `bytearray`; they are shown as `bytearray()` with a `bytes` literal as an argument.
- A slice of `bytearray` is also a `bytearray`.

### Understanding the Outputs

- `cafe[0]` retrieves an integer (99).
- `cafe[:1]` returns a `bytes` sequence of length 1 (b'c').

This is different from the `str` type in Python, where `s[0] == s[:1]`. For other sequence types, one item is not the same as a slice of length 1.

### Literal Notation for Binary Sequences

Binary sequences often contain ASCII text, so their literal notation reflects this:

- For bytes with decimal codes 32 to 126 (space to ~), the ASCII character is used.
- For tab, newline, carriage return, and \, escape sequences \t, \n, \r, and \\ are used.
- If both string delimiters ' and " appear, the sequence is delimited by ' and any ' inside are escaped as \'.
- For other byte values, a hexadecimal escape sequence is used (e.g., \x00 for the null byte).

Example:

```python
print(cafe)  # Output: b'caf\xc3\xa9'
```

The first three bytes `b'caf'` are in the printable ASCII range; the last two are not.

## Methods Supported by Bytes and Bytearray

`bytes` and `bytearray` support almost all `str` methods except those for formatting and Unicode data. You can use methods like `endswith`, `replace`, `strip`, `translate`, `upper`, and more with binary sequences.

Example:

```python
data = b'hello world'
print(data.upper())  # Output: b'HELLO WORLD'
```

Regular expression functions in the `re` module also work on binary sequences if the regex is compiled from a binary sequence.

### Binary Sequence Construction

- `bytes` and `bytearray` can be constructed from:
  - A `str` and an encoding keyword argument.
  - An iterable providing items with values from 0 to 255.
  - An object implementing the buffer protocol (e.g., `bytes`, `bytearray`, `memoryview`, `array.array`).

Example:

```python
hex_data = bytes.fromhex('31 4B CE A9')
print(hex_data)  # Output: b'1K\xce\xa9'
```

### Example 4-3: Initializing Bytes from Raw Data

```python
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)  # Output: b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
```

- `Typecode 'h'` creates an array of short integers (16 bits).
- `octets` holds a copy of the bytes that make up `numbers`.
- These are the 10 bytes representing the 5 short integers.

## Memory Views

Creating a `bytes` or `bytearray` object from any buffer-like source will always copy the bytes. In contrast, `memoryview` objects let you share memory between binary data structures.

## Conversion to/from Strings

Binary sequences can be converted to and from strings, which will be covered in further sections.
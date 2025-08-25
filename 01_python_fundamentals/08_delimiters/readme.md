# Delimiters in Python 🔢

In this section, we'll explore **delimiters** in Python. Delimiters are characters or combinations of characters that Python uses for various purposes, such as in expressions, list, dictionary, and set literals, as well as in different statements.

## Table of Contents 📖

- [Delimiters in Python 🔢](#delimiters-in-python-)
  - [Table of Contents 📖](#table-of-contents-)
  - [Common Delimiters in Python ✂️](#common-delimiters-in-python-️)
  - [Augmented Assignment Operators 🔄](#augmented-assignment-operators-)
  - [Special Characters and Their Uses 🛠️](#special-characters-and-their-uses-️)
    - [Example:](#example)
  - [Restrictions on Certain Characters ❌](#restrictions-on-certain-characters-)

## Common Delimiters in Python ✂️

Python uses the following characters as delimiters:

| **Delimiter** | **Purpose/Usage**                                                                 |
|---------------|-----------------------------------------------------------------------------------|
| `()`          | Used for grouping expressions, function calls, and tuples.                        |
| `[]`          | Used for indexing, slicing, and list literals.                                    |
| `{}`          | Used for dictionary and set literals, as well as formatting strings.              |
| `,`           | Used to separate items in lists, tuples, dictionaries, function arguments, etc.   |
| `:`           | Used in dictionaries to separate keys and values, and in various statements like `for`, `if`, and function definitions. |
| `.`           | Used for accessing object attributes or methods, and for floating-point literals. |
| `` ` ``       | Used for string literals (backticks are deprecated in Python 3).                  |
| `=`           | Used for assignment.                                                              |
| `;`           | Used to separate multiple statements on a single line.                            |
| `@`           | Used for decorators.                                                              |

## Augmented Assignment Operators 🔄

Python also uses augmented assignment operators, which are a combination of a delimiter and an operation. These operators perform an operation and then assign the result to a variable.

| **Operator** | **Description**                                     |
|--------------|-----------------------------------------------------|
| `+=`         | Adds and assigns (e.g., `x += 2` is equivalent to `x = x + 2`). |
| `-=`         | Subtracts and assigns (e.g., `x -= 2` is equivalent to `x = x - 2`). |
| `*=`         | Multiplies and assigns (e.g., `x *= 2` is equivalent to `x = x * 2`). |
| `/=`         | Divides and assigns (e.g., `x /= 2` is equivalent to `x = x / 2`). |
| `//=`        | Floor divides and assigns (e.g., `x //= 2` is equivalent to `x = x // 2`). |
| `%=`         | Takes modulus and assigns (e.g., `x %= 2` is equivalent to `x = x % 2`). |
| `&=`         | Bitwise AND and assigns (e.g., `x &= 2` is equivalent to `x = x & 2`). |
| `|=`         | Bitwise OR and assigns (e.g., `x |= 2` is equivalent to `x = x | 2`). |
| `^=`         | Bitwise XOR and assigns (e.g., `x ^= 2` is equivalent to `x = x ^ 2`). |
| `>>=`        | Bitwise right shift and assigns (e.g., `x >>= 2` is equivalent to `x = x >> 2`). |
| `<<=`        | Bitwise left shift and assigns (e.g., `x <<= 2` is equivalent to `x = x << 2`). |
| `**=`        | Exponentiates and assigns (e.g., `x **= 2` is equivalent to `x = x ** 2`). |

## Special Characters and Their Uses 🛠️

Certain characters have specific meanings as part of other tokens in Python:

| **Character** | **Special Meaning**                                                                 |
|---------------|-------------------------------------------------------------------------------------|
| `'`           | Surrounds string literals.                                                          |
| `"`           | Surrounds string literals.                                                          |
| `#`           | Starts a comment outside of a string.                                               |
| `\`           | Used at the end of a physical line to join the next line into a single logical line. Also acts as an escape character in strings. |

### Example:
```python
# This is a comment

text = "Hello, World!"  # Double quotes for string
path = 'C:\\Users\\Hashim\\Documents'  # Escape character in string
```

## Restrictions on Certain Characters ❌

Some characters are not allowed in the main text of a Python program (except in comments or string literals):

- `$` and `?`
- All control characters (except whitespace).
- In Python v2, all characters with ISO codes above 126 (non-ASCII characters, like accented letters).

---

This section provided an overview of **delimiters** in Python, including their uses and restrictions. Understanding these delimiters is essential for writing clear and effective Python code. 📝

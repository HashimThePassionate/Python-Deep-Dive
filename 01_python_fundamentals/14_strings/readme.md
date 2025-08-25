# ✨ Using Python to Manipulate Strings

## 📋 Table of Contents

- [✨ Using Python to Manipulate Strings](#-using-python-to-manipulate-strings)
  - [📋 Table of Contents](#-table-of-contents)
  - [🌟 **Creating Strings in Python**](#-creating-strings-in-python)
    - [📝 **Examples:**](#-examples)
    - [🌟 **Strings Indexing and Splitting**](#-strings-indexing-and-splitting)
      - [📝 **Examples:**](#-examples-1)
    - [🌟 **String Methods**](#-string-methods)
      - [🛠️ **Common String Methods:**](#️-common-string-methods)
      - [📝 **Examples:**](#-examples-2)
    - [🌟 **String Indexing and Slicing**](#-string-indexing-and-slicing)
      - [📝 **Examples:**](#-examples-3)
    - [🌟 **String Operators**](#-string-operators)
      - [📝 **Examples:**](#-examples-4)
    - [🌟 **String Formatting**](#-string-formatting)
      - [🛠️ **Using `format()` Method:**](#️-using-format-method)
      - [🛠️ **Using `%` Operator:**](#️-using--operator)
    - [🌟 **Escape Sequences in Strings**](#-escape-sequences-in-strings)
      - [🛠️ **Common Escape Sequences:**](#️-common-escape-sequences)
    - [🌟 **Escape Sequences in Strings**](#-escape-sequences-in-strings-1)
      - [🛠️ **Common Escape Sequences Examples:**](#️-common-escape-sequences-examples)
    - [🌟 **Raw Strings**](#-raw-strings)
      - [📝 **Example:**](#-example)

---

Python provides powerful ways to manipulate strings, allowing us to perform a variety of operations on them. Let's explore how strings work in Python, including their creation, indexing, methods, and formatting.

---

## 🌟 **Creating Strings in Python**

Strings in Python can be created using single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`). Triple quotes are particularly useful for creating multiline strings or docstrings.

### 📝 **Examples:**

```python
# Using single quotes
str1 = 'Hello Python'
print(str1)  # Output: Hello Python

# Using double quotes
str2 = "Hello Python"
print(str2)  # Output: Hello Python

# Using triple quotes
str3 = '''Triple quotes are generally used for
multiline strings or docstrings.'''
print(str3)
```

---

### 🌟 **Strings Indexing and Splitting**

Python strings are indexed starting from `0` for the first character. You can also use negative indices to access characters from the end of the string, starting with `-1`.

#### 📝 **Examples:**

```python
str = "HELLO"

# Positive indexing
print(str[0])  # Output: H
print(str[1])  # Output: E

# Negative indexing
print(str[-1])  # Output: O
print(str[-2])  # Output: L
```

---

### 🌟 **String Methods**

Python provides a variety of built-in methods to work with strings. These methods do not modify the original string but return new strings based on the operations performed.

#### 🛠️ **Common String Methods:**

- **capitalize()**: Converts the first character to uppercase.
- **lower()**: Converts the entire string to lowercase.
- **upper()**: Converts the entire string to uppercase.
- **find()**: Searches the string for a specified value and returns the position of where it was found.
- **replace()**: Returns a string where a specified value is replaced with another value.

#### 📝 **Examples:**

```python
str = "hello world"

# Capitalize the first letter
print(str.capitalize())  # Output: Hello world

# Convert to uppercase
print(str.upper())  # Output: HELLO WORLD

# Find a substring
print(str.find("world"))  # Output: 6

# Replace a substring
print(str.replace("world", "Python"))  # Output: hello Python
```

---

### 🌟 **String Indexing and Slicing**

You can access individual characters or a range of characters in a string using indexing and slicing.

#### 📝 **Examples:**

```python
word = 'Didcoding'

# Accessing individual characters
print(word[0])  # Output: D
print(word[5])  # Output: d

# Slicing
print(word[0:2])  # Output: Di
print(word[2:5])  # Output: dco
print(word[::-1])  # Output: gnidcoDid (Reversed string)
```

---

### 🌟 **String Operators**

Python supports various operators for string manipulation, including concatenation (`+`), repetition (`*`), and membership (`in`, `not in`).

#### 📝 **Examples:**

```python
str1 = "Hello"
str2 = " World"

# Concatenation
print(str1 + str2)  # Output: Hello World

# Repetition
print(str1 * 3)  # Output: HelloHelloHello

# Membership
print('H' in str1)  # Output: True
```

---

### 🌟 **String Formatting**

Python offers several ways to format strings. The `format()` method and the `%` operator are two common approaches.

#### 🛠️ **Using `format()` Method:**

```python
name1 = "Hamza"
name2 = "Hashim"

# Using positional arguments
print("{} and {} are best friends.".format(name1, name2))  # Output: Hamza and Hashim are best friends.

# Using keyword arguments
print("{a} and {b} are best friends.".format(a="Hamza", b="Hashim"))  # Output: Hamza and Hashim are best friends.
```

#### 🛠️ **Using `%` Operator:**

```python
Integer = 10
Float = 1.29
String = "Hamza"

print("Integer: %d, Float: %f, String: %s" % (Integer, Float, String))
# Output: Integer: 10, Float: 1.290000, String: Hamza
```

---

### 🌟 **Escape Sequences in Strings**

Escape sequences allow you to include special characters in strings, such as newline (`\n`), tab (`\t`), or backslash (`\\`).

#### 🛠️ **Common Escape Sequences:**

| **Escape Sequence** | **Description**                                              | **Example Code**                           | **Output/Effect**                       |
|---------------------|--------------------------------------------------------------|---------------------------------------------|------------------------------------------|
| `\n`                | Newline                                                      | `print("Hello\nWorld")`                    | Hello <br> World                        |
| `\t`                | Horizontal Tab                                               | `print("Hello\tWorld")`                    | Hello   World                           |
| `\\`                | Backslash                                                    | `print("This is a backslash: \\")`         | This is a backslash: \                  |
| `\'`                | Single Quote                                                 | `print('It\'s a sunny day!')`              | It's a sunny day!                       |
| `\"`                | Double Quote                                                 | `print("She said, \"Hello!\"")`            | She said, "Hello!"                      |
| `\r`                | Carriage Return                                              | `print("Hello\rWorld")`                    | World                                   |
| `\b`                | Backspace                                                    | `print("Hello\bWorld")`                    | HellWorld                               |
| `\f`                | Form Feed                                                    | `print("Hello\fWorld")`                    | Hello (new page effect) World           |
| `\a`                | Bell (Alert)                                                 | `print("Hello\aWorld")`                    | Beep sound (if supported)               |
| `\v`                | Vertical Tab                                                 | `print("Hello\vWorld")`                    | Hello (vertical space) World            |
| `\0`                | Null Character                                               | `print("Hello\0World")`                    | HelloWorld (null is invisible)          |
| `\N{name}`          | Unicode Character by Name                                    | `print("\N{Greek Capital Letter Omega}")`  | Ω                                       |
| `\uXXXX`            | Unicode Character with 16-bit hex value                      | `print("\u03A9")`                          | Ω (Greek Omega)                         |
| `\UXXXXXXXX`        | Unicode Character with 32-bit hex value                      | `print("\U0001F600")`                      | 😀 (Smiling Face Emoji)                 |
| `\xXX`              | Character with the given hexadecimal value                   | `print("\x48\x65\x6c\x6c\x6f")`            | Hello                                   |

---

### 🌟 **Escape Sequences in Strings**
Escape sequences allow you to include special characters in strings, such as newline (`\n`), tab (`\t`), or backslash (`\\`). They are used with a backslash (`\`) followed by a character to represent special characters.

#### 🛠️ **Common Escape Sequences Examples:**

1. **`\n` - Newline**  
   Moves the text following it to a new line.

   ```python
   print("Hello\nWorld")  # Output:
   # Hello
   # World
   ```

2. **`\t` - Tab**  
   Adds a horizontal tab space.

   ```python
   print("Hello\tWorld")  # Output: Hello   World
   ```

3. **`\\` - Backslash**  
   Represents a literal backslash character.

   ```python
   print("This is a backslash: \\")  # Output: This is a backslash: \
   ```

4. **`\'` - Single Quote**  
   Allows you to include a single quote inside a single-quoted string.

   ```python
   print('It\'s a sunny day!')  # Output: It's a sunny day!
   ```

5. **`\"` - Double Quote**  
   Allows you to include a double quote inside a double-quoted string.

   ```python
   print("She said, \"Hello!\"")  # Output: She said, "Hello!"
   ```

6. **`\r` - Carriage Return**  
   Moves the cursor to the beginning of the line. If any characters follow, they will overwrite the beginning characters.

   ```python
   print("Hello\rWorld")  # Output: World
   ```

7. **`\b` - Backspace**  
   Deletes the character before it (one step back).

   ```python
   print("Hello\bWorld")  # Output: HellWorld
   ```

8. **`\f` - Form Feed**  
   Moves the cursor to the next page (used mainly in printing).

   ```python
   print("Hello\fWorld")  # Output: Hello (moves vertically to World on printers)
   ```

9. **`\a` - Bell (Alert)**  
   Produces a beep sound in some systems.

   ```python
   print("Hello\aWorld")  # Produces a beep sound (if the system supports it)
   ```

10. **`\v` - Vertical Tab**  
    Moves the text to the next vertical tab position.

   ```python
   print("Hello\vWorld")  # Output: Hello (vertical space) World
   ```

11. **`\0` - Null Character**  
    Represents a null character in strings.

   ```python
   print("Hello\0World")  # Output: Hello World (null is invisible)
   ```

12. **`\N{name}` - Unicode Character by Name**  
    Inserts a character by its Unicode name.

   ```python
   print("\N{Greek Capital Letter Omega}")  # Output: Ω
   ```

13. **`\uXXXX` - Unicode (16-bit) Character**  
    Inserts a Unicode character with a 16-bit hex value.

   ```python
   print("\u03A9")  # Output: Ω (Greek Omega)
   ```

14. **`\UXXXXXXXX` - Unicode (32-bit) Character**  
    Inserts a Unicode character with a 32-bit hex value.

   ```python
   print("\U0001F600")  # Output: 😀 (Smiling Face Emoji)
   ```

15. **`\xXX` - Hexadecimal Character**  
    Inserts a character with the given hexadecimal value.

   ```python
   print("\x48\x65\x6c\x6c\x6f")  # Output: Hello
   ```

### 🌟 **Raw Strings**

Raw strings treat backslashes as literal characters, making them useful for regular expressions and file paths. You define a raw string by adding an `r` or `R` before the string.

#### 📝 **Example:**

```python
print(r"C:\Users\Hashim\Python")  # Output: C:\Users\Hashim\Python
```
In this example, the `r` prefix before the string tells Python to treat backslashes as literal characters instead of escape sequences.




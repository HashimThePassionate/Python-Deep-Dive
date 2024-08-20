# ✨ Using Python to Manipulate Strings

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

- `\n`: Newline
- `\t`: Tab
- `\\`: Backslash
- `\'`: Single Quote
- `\"`: Double Quote

#### 📝 **Examples:**

```python
# Newline and tab
print("Hello\nWorld")  # Output: Hello
                       #         World
print("Hello\tWorld")  # Output: Hello   World

# Escaping quotes
print('They said, "What\'s going on?"')  # Output: They said, "What's going on?"
```

---

### 🌟 **Raw Strings**

Raw strings treat backslashes as literal characters, making them useful for regular expressions and file paths.

#### 📝 **Example:**

```python
print(r"C:\Users\Hashim\Python")  # Output: C:\Users\Hashim\Python
```


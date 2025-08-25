# Character Sets in Python 🅰️🅱️🔤

## Table of Contents 📚
- [Character Sets in Python 🅰️🅱️🔤](#character-sets-in-python-️️)
  - [Table of Contents 📚](#table-of-contents-)
  - [Unicode and ASCII in Python 🌐](#unicode-and-ascii-in-python-)
    - [Python v3](#python-v3)
    - [Python v2](#python-v2)
  - [Specifying a Different Encoding 🎨](#specifying-a-different-encoding-)
    - [Example:](#example)
  - [Using Non-ASCII Characters ✒️](#using-non-ascii-characters-️)
    - [Example:](#example-1)
  - [Best Practices for Encoding 🚀](#best-practices-for-encoding-)
    - [Example:](#example-2)

---

In this section, we will explore how Python handles different character sets in source files. Understanding character encoding is crucial for writing Python code that works across different languages and platforms.

## Unicode and ASCII in Python 🌐

### Python v3

- **Python v3** source files can use **any Unicode character**, encoded as **UTF-8**.
  - **UTF-8** is a variable-width character encoding that can represent every character in the Unicode character set.
  - **ASCII characters** (with codes between 0 and 127) are encoded in UTF-8 as single bytes, making an ASCII text file perfectly valid as a Python v3 source file.

### Python v2

- **Python v2** source files are typically made up of characters from the **ASCII set**.
  - ASCII characters have codes between 0 and 127.

## Specifying a Different Encoding 🎨

- In both Python v2 and v3, you can inform Python that a source file uses a different encoding.
- Python will use this specified encoding to read the file.

### Example:
```python
# coding: utf-8
```

- This comment should be placed at the very beginning of your Python source file (right after the “shebang line” if present).
- The `coding:` directive is also known as an **encoding declaration**.

## Using Non-ASCII Characters ✒️

- In **Python v2**, non-ASCII characters can only be used in **comments** and **string literals**.
- The **coding directive** allows you to use these characters by specifying the appropriate encoding.

### Example:
```python
# coding: iso-8859-1
# This is a comment with a non-ASCII character: ñ
print("Hola, señor!")
```

## Best Practices for Encoding 🚀

- It is considered best practice to use **UTF-8** for all your text files, including Python source files.
  - **UTF-8** is widely supported and ensures that your code can handle a wide variety of characters from different languages.

### Example:
```python
# coding: utf-8
print("こんにちは, 世界!")  # Prints "Hello, World!" in Japanese
```

---
This section covered how Python handles character sets and encodings. By understanding and using the correct encoding, you can write Python code that is robust, flexible, and compatible across different systems. 🌍

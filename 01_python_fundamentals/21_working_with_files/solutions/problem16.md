# 📝 **Quiz 16: Changing Unicode Encoding of an Open File**

### Problem:
You want to **change the Unicode encoding** of an already open file without closing and reopening it.

### 💡 **Hint**:
You can use Python’s **`io.TextIOWrapper()`** to change the encoding of an **already open file** on the fly. This allows you to wrap an existing binary file object and change its encoding without closing the file.

### 🔧 **Solution: Using `io.TextIOWrapper()` to Change Encoding**

The **`io.TextIOWrapper()`** method wraps an existing binary file object and changes the encoding. This is useful when you want to handle different encodings dynamically, especially when working with open file streams.

### 📂 **Complete Example: Changing Encoding of an Open File**

#### **1. Changing the Encoding of an Open File**

```python
import io

# Open a binary file in read mode
with open('example.txt', 'rb') as binary_file:
    # Read the file with UTF-8 encoding
    text_file_utf8 = io.TextIOWrapper(binary_file, encoding='utf-8')
    content_utf8 = text_file_utf8.read()
    print(f"Content with UTF-8 encoding:\n{content_utf8}")
    
    # Rewind the binary file back to the start
    binary_file.seek(0)
    
    # Change encoding to ISO-8859-1 (Latin-1) without closing the file
    text_file_latin1 = io.TextIOWrapper(binary_file, encoding='iso-8859-1')
    content_latin1 = text_file_latin1.read()
    print(f"Content with ISO-8859-1 encoding:\n{content_latin1}")
```

#### **Explanation**:
1. The file **`example.txt`** is opened in **binary mode** (`'rb'`), which allows it to be wrapped with different encodings.
2. **`io.TextIOWrapper()`** is used to change the encoding from **UTF-8** to **ISO-8859-1** (Latin-1) **on the fly**, without closing and reopening the file.
3. **`seek(0)`** rewinds the binary file back to the start before changing the encoding.

### 📂 **Example: Changing Encoding When Writing to a File**

You can also change the encoding **when writing** to a file using `io.TextIOWrapper()`.

#### **Example: Writing to a File with Different Encodings**

```python
import io

# Open a file in binary write mode
with open('output.txt', 'wb') as binary_file:
    # Write to the file with UTF-8 encoding
    text_file_utf8 = io.TextIOWrapper(binary_file, encoding='utf-8')
    text_file_utf8.write("Hello, this is UTF-8 encoded text!\n")
    text_file_utf8.flush()  # Make sure the data is written to the file
    
    # Change encoding to ISO-8859-1 (Latin-1) and write more text
    text_file_latin1 = io.TextIOWrapper(binary_file, encoding='iso-8859-1')
    text_file_latin1.write("¡Hola, esto es texto codificado en ISO-8859-1!\n")
    text_file_latin1.flush()

print("Content written with different encodings.")
```

#### **Explanation**:
- The file is opened in **binary write mode** (`'wb'`), and we switch between **UTF-8** and **ISO-8859-1** encodings using **`io.TextIOWrapper()`**.
- **`flush()`** ensures that the content is written to the file before switching to a different encoding.

### 📋 **Key Points**:

- **`io.TextIOWrapper()`** allows you to wrap an open file object and change its encoding on the fly, without needing to close and reopen the file.
- You can change the encoding of both **reading** and **writing** operations using **`io.TextIOWrapper()`**.
- This method is useful for **dynamic encoding handling** when working with files that require multiple encodings.

### 🔄 **Practical Use Case: Reading a File in Different Encodings**

If you have a file that may contain text in different encodings, you can use `io.TextIOWrapper()` to read sections of the file with different encodings.

```python
import io

# Open a file in binary mode
with open('multilingual.txt', 'rb') as binary_file:
    # Read the first part of the file as UTF-8
    text_file_utf8 = io.TextIOWrapper(binary_file, encoding='utf-8')
    content_utf8 = text_file_utf8.read(50)  # Read first 50 characters
    print(f"Content in UTF-8:\n{content_utf8}")
    
    # Rewind and switch to ISO-8859-1 for the next part
    binary_file.seek(50)
    text_file_latin1 = io.TextIOWrapper(binary_file, encoding='iso-8859-1')
    content_latin1 = text_file_latin1.read(50)  # Read next 50 characters
    print(f"Content in ISO-8859-1:\n{content_latin1}")
```

#### **Explanation**:
- This approach can handle **multilingual files** that may have sections in different encodings.
- By reading specific sections of the file with different encodings, you can handle **mixed encoding** content efficiently.

### 📋 **Summary**:

- **`io.TextIOWrapper()`** is a powerful tool for changing the encoding of an **already open file** without closing it.
- It allows you to **read** and **write** files with different encodings dynamically.
- This method is particularly useful when working with **multilingual files** or files that may have varying encoding formats.

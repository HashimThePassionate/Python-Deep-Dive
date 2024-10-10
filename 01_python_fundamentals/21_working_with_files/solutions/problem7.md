# 📝 **Quiz 7: Working with Compressed Files (gzip or bz2)**

### Problem:
You need to **read** or **write** data from a file with **gzip** or **bz2** compression.

### 💡 **Hint**:
Python’s **`gzip`** and **`bz2`** modules allow you to work with files that are compressed using **gzip** or **bz2** compression algorithms. These libraries provide functionality to read from and write to compressed files similarly to how you work with regular files.

### 🔧 **Solution: Reading and Writing Compressed Files with `gzip` or `bz2`**

You can use the **`gzip`** module to handle **gzip-compressed** files and the **`bz2`** module to work with **bz2-compressed** files. Both libraries offer file-like interfaces, allowing you to use familiar file operations (`read()`, `write()`, etc.) on compressed files.

### 📂 **Complete Example: Using `gzip` for Reading and Writing Compressed Files**

#### **1. Writing to a Gzip-Compressed File**

```python
import gzip

# Data to be written
data = "This is some text data that will be compressed using gzip."

# Write data to a gzip-compressed file
with gzip.open('data_compressed.gz', 'wt') as file:
    file.write(data)
    print("Data has been compressed and written to 'data_compressed.gz'.")
```

#### **Explanation**:
- The `gzip.open()` function is used with mode `'wt'` (write text) to **write text data** to a **gzip-compressed** file.
- The text `"This is some text data..."` is compressed and written to `data_compressed.gz`.

#### **2. Reading from a Gzip-Compressed File**

```python
# Read the data from the gzip-compressed file
with gzip.open('data_compressed.gz', 'rt') as file:
    decompressed_data = file.read()
    print("Decompressed data from gzip file:")
    print(decompressed_data)
```

#### **Explanation**:
- The `gzip.open()` function is used with mode `'rt'` (read text) to **read** from the compressed file.
- The file `data_compressed.gz` is opened, decompressed, and the original text data is printed.

#### **Output**:
```
Data has been compressed and written to 'data_compressed.gz'.
Decompressed data from gzip file:
This is some text data that will be compressed using gzip.
```

### 📂 **Complete Example: Using `bz2` for Reading and Writing Compressed Files**

#### **1. Writing to a Bz2-Compressed File**

```python
import bz2

# Data to be written
data = "This is some text data that will be compressed using bz2."

# Write data to a bz2-compressed file
with bz2.open('data_compressed.bz2', 'wt') as file:
    file.write(data)
    print("Data has been compressed and written to 'data_compressed.bz2'.")
```

#### **Explanation**:
- The `bz2.open()` function is used with mode `'wt'` (write text) to **write** text data to a **bz2-compressed** file.
- The text data is compressed and written to `data_compressed.bz2`.

#### **2. Reading from a Bz2-Compressed File**

```python
# Read the data from the bz2-compressed file
with bz2.open('data_compressed.bz2', 'rt') as file:
    decompressed_data = file.read()
    print("Decompressed data from bz2 file:")
    print(decompressed_data)
```

#### **Explanation**:
- The `bz2.open()` function is used with mode `'rt'` (read text) to **read** from the compressed file.
- The file `data_compressed.bz2` is opened, decompressed, and the original text data is printed.

#### **Output**:
```
Data has been compressed and written to 'data_compressed.bz2'.
Decompressed data from bz2 file:
This is some text data that will be compressed using bz2.
```

### 📋 **Key Points**:

- **`gzip.open()`**: Use this for handling **gzip**-compressed files. Modes like `'wt'` (write text) or `'rt'` (read text) help you work with compressed text data.
- **`bz2.open()`**: Use this for handling **bz2**-compressed files. It supports similar modes as `gzip`.
- **Binary Modes**: If you're dealing with **binary** data, use `'wb'` (write binary) and `'rb'` (read binary) instead of `'wt'` and `'rt'`.

### 🔄 **Complete Workflow**: Compressing and Decompressing Text Files Using `gzip`

```python
import gzip

# Step 1: Compress the text and save it to a gzip file
with gzip.open('example.gz', 'wt') as file:
    file.write("This is some text that will be compressed using gzip.")

# Step 2: Read and decompress the gzip file
with gzip.open('example.gz', 'rt') as file:
    decompressed_text = file.read()
    print(decompressed_text)
```

This workflow demonstrates how to **compress** and then **decompress** text data using **gzip**.

### 📋 **Summary**:

- Use **`gzip`** or **`bz2`** modules to work with **compressed files**.
- Both libraries provide an easy-to-use **file-like interface** for working with compressed text or binary data.
- Modes like `'wt'`, `'rt'`, `'wb'`, and `'rb'` allow you to switch between reading and writing **text** or **binary** data.

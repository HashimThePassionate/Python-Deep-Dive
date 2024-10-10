# 📝 **Quiz 12: Testing File/Directory Existence**

### Problem:
You need to **check whether a file or directory exists** in the file system.

### 💡 **Hint**:
You can use **`os.path.exists()`** or **`pathlib.Path.exists()`** to check if a file or directory exists. These methods return **`True`** if the file or directory exists, and **`False`** otherwise.

### 🔧 **Solution: Using `os.path.exists()` or `pathlib.Path.exists()`**

Both **`os.path`** and **`pathlib`** modules provide easy ways to check the existence of files or directories.

### 📂 **Complete Example: Using `os.path.exists()` to Check Existence**

#### **1. Using `os.path.exists()` for Files and Directories**

```python
import os

# Define a file path and a directory path
file_path = "/home/muhammad/documents/sample.txt"
dir_path = "/home/muhammad/projects/"

# Check if the file exists
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

# Check if the directory exists
if os.path.exists(dir_path):
    print(f"The directory '{dir_path}' exists.")
else:
    print(f"The directory '{dir_path}' does not exist.")
```

#### **Explanation**:
- **`os.path.exists()`** checks whether the given path (either file or directory) exists.
- It works for both **files** and **directories**.
- The code prints a message depending on whether the path exists.

### 📂 **Complete Example: Using `pathlib.Path.exists()` to Check Existence**

#### **2. Using `pathlib.Path.exists()` for Files and Directories**

```python
from pathlib import Path

# Define a file path and a directory path
file_path = Path("/home/muhammad/documents/sample.txt")
dir_path = Path("/home/muhammad/projects/")

# Check if the file exists
if file_path.exists():
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

# Check if the directory exists
if dir_path.exists():
    print(f"The directory '{dir_path}' exists.")
else:
    print(f"The directory '{dir_path}' does not exist.")
```

#### **Explanation**:
- **`pathlib.Path.exists()`** checks whether the path exists.
- It works for both **files** and **directories**.
- The `Path` object is more flexible, allowing you to work with paths in an object-oriented manner.

### 📂 **Checking File Type: Is it a File or Directory?**

You can also check whether a given path is a **file** or a **directory**:

#### **1. Using `os.path`**:

```python
import os

path = "/home/muhammad/documents/sample.txt"

# Check if it's a file
if os.path.isfile(path):
    print(f"'{path}' is a file.")
elif os.path.isdir(path):
    print(f"'{path}' is a directory.")
else:
    print(f"'{path}' does not exist.")
```

#### **2. Using `pathlib`**:

```python
from pathlib import Path

path = Path("/home/muhammad/documents/sample.txt")

# Check if it's a file
if path.is_file():
    print(f"'{path}' is a file.")
elif path.is_dir():
    print(f"'{path}' is a directory.")
else:
    print(f"'{path}' does not exist.")
```

#### **Explanation**:
- **`os.path.isfile()`** and **`os.path.isdir()`** determine whether the path points to a **file** or **directory**.
- Similarly, **`Path.is_file()`** and **`Path.is_dir()`** do the same in `pathlib`.

### 📋 **Key Points**:

- **`os.path.exists()`**: Returns `True` if the path (file or directory) exists, and `False` otherwise.
- **`pathlib.Path.exists()`**: Provides an object-oriented way to check for existence of a file or directory.
- **File/Directory Checks**:
  - **`os.path.isfile()`** and **`os.path.isdir()`** for `os.path`.
  - **`Path.is_file()`** and **`Path.is_dir()`** for `pathlib`.

### 🔄 **Practical Use Case: Checking and Creating Directories**

You can check if a directory exists and create it if it doesn't:

```python
from pathlib import Path

# Define a directory path
dir_path = Path("/home/muhammad/projects/new_folder")

# Check if the directory exists, create it if not
if not dir_path.exists():
    dir_path.mkdir(parents=True)  # Create directory and parent directories if needed
    print(f"Created directory: {dir_path}")
else:
    print(f"The directory '{dir_path}' already exists.")
```

#### **Explanation**:
- **`mkdir(parents=True)`** creates the directory if it doesn't exist, including any parent directories.
- This is useful for ensuring directories are in place before creating files in them.

### 📋 **Summary**:

- **`os.path.exists()`** and **`pathlib.Path.exists()`** are used to check if a file or directory exists.
- You can also use **`isfile()`** or **`isdir()`** to check whether the path points to a file or directory.
- **`pathlib`** offers a more modern and flexible way to handle paths, while **`os.path`** is the traditional approach.
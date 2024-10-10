# 📝 **Quiz 11: Manipulating Pathnames**

### Problem:
You need to **manipulate pathnames** to find the **base filename**, **directory name**, or **absolute path**.

### 💡 **Hint**:
Python’s **`os.path`** and **`pathlib`** modules provide several utilities for **path manipulation**, allowing you to extract the filename, directory name, and work with paths in an easy and platform-independent way.

### 🔧 **Solution: Using `os.path` and `pathlib` for Path Manipulation**

You can use both **`os.path`** (traditional approach) and **`pathlib`** (modern approach) to handle different path manipulation tasks such as getting the **file name**, **directory name**, **absolute path**, etc.

### 📂 **Complete Example: Path Manipulation Using `os.path`**

#### **1. Using `os.path` for Path Manipulation**

```python
import os

# Define a sample file path
file_path = "/home/muhammad/projects/code/example.py"

# Get the base filename
base_name = os.path.basename(file_path)
print(f"Base filename: {base_name}")

# Get the directory name
dir_name = os.path.dirname(file_path)
print(f"Directory name: {dir_name}")

# Get the absolute path (if the path is relative)
absolute_path = os.path.abspath(file_path)
print(f"Absolute path: {absolute_path}")

# Split the path into directory and file
split_path = os.path.split(file_path)
print(f"Split path (dir, file): {split_path}")
```

#### **Explanation**:
1. **`os.path.basename()`**: Returns the **base filename** from a path (e.g., `"example.py"` from `"/home/muhammad/projects/code/example.py"`).
2. **`os.path.dirname()`**: Returns the **directory path** (e.g., `"/home/muhammad/projects/code"`).
3. **`os.path.abspath()`**: Returns the **absolute path** to the file, resolving any relative paths.
4. **`os.path.split()`**: Splits the path into the directory and the file name.

#### **Output**:
```
Base filename: example.py
Directory name: /home/muhammad/projects/code
Absolute path: /home/muhammad/projects/code/example.py
Split path (dir, file): ('/home/muhammad/projects/code', 'example.py')
```

### 📂 **Complete Example: Path Manipulation Using `pathlib` (Modern Approach)**

The **`pathlib`** module provides an object-oriented way to handle paths, making it more intuitive and flexible.

#### **2. Using `pathlib` for Path Manipulation**

```python
from pathlib import Path

# Define a sample file path
file_path = Path("/home/muhammad/projects/code/example.py")

# Get the base filename
base_name = file_path.name
print(f"Base filename: {base_name}")

# Get the directory name
dir_name = file_path.parent
print(f"Directory name: {dir_name}")

# Get the absolute path (if the path is relative)
absolute_path = file_path.resolve()
print(f"Absolute path: {absolute_path}")

# Split the path into directory and file
print(f"Split path (dir, file): ({file_path.parent}, {file_path.name})")
```

#### **Explanation**:
1. **`file_path.name`**: Returns the **base filename** (equivalent to `os.path.basename()`).
2. **`file_path.parent`**: Returns the **parent directory** (equivalent to `os.path.dirname()`).
3. **`file_path.resolve()`**: Returns the **absolute path**, resolving any relative paths.
4. **Direct access**: You can access different parts of the path directly using object-oriented methods.

#### **Output**:
```
Base filename: example.py
Directory name: /home/muhammad/projects/code
Absolute path: /home/muhammad/projects/code/example.py
Split path (dir, file): (/home/muhammad/projects/code, example.py)
```

### 📋 **Key Points**:

- **`os.path` Module**:
  - **`os.path.basename()`**: Extracts the base filename from a path.
  - **`os.path.dirname()`**: Extracts the directory name from a path.
  - **`os.path.abspath()`**: Resolves relative paths to absolute paths.
  - **`os.path.split()`**: Splits a path into directory and file components.

- **`pathlib` Module**:
  - **Object-Oriented Approach**: `Path` objects allow easy manipulation of paths using methods like `.name`, `.parent`, and `.resolve()`.
  - It’s a more modern and flexible way to handle file paths, especially for **cross-platform** compatibility.

### 🔄 **Practical Use Case: Combining Paths and Checking Existence**

You can use these modules to **combine paths** and check if files or directories exist.

```python
from pathlib import Path

# Combine paths
project_dir = Path("/home/muhammad/projects")
new_file = project_dir / "new_script.py"  # This joins the paths
print(f"New file path: {new_file}")

# Check if a file or directory exists
if new_file.exists():
    print(f"{new_file} exists.")
else:
    print(f"{new_file} does not exist.")
```

#### **Explanation**:
- **`Path / "new_script.py"`** combines paths in a clean and platform-independent way.
- **`.exists()`** checks if the file or directory exists.

### 📋 **Summary**:

- **`os.path`** provides **traditional functions** for manipulating paths.
- **`pathlib`** offers a **modern object-oriented approach** with powerful path manipulation capabilities.
- Both methods allow you to easily handle tasks like extracting the filename, directory, or resolving absolute paths.
# 📝 **Quiz 13: Listing Files in a Directory**

### Problem:
You want to get a **list of files** contained in a **directory**.

### 💡 **Hint**:
You can use **`os.listdir()`** or **`pathlib.Path().iterdir()`** to list the contents of a directory. These methods return the **files** and **subdirectories** present in the specified directory.

### 🔧 **Solution: Using `os.listdir()` or `pathlib.Path().iterdir()`**

Both **`os`** and **`pathlib`** provide ways to list files in a directory. You can filter out files, directories, or specific file types as needed.

### 📂 **Complete Example: Using `os.listdir()` to List Files**

#### **1. Listing Files Using `os.listdir()`**

```python
import os

# Define the directory path
directory = "/home/muhammad/projects"

# List all files and directories in the directory
all_items = os.listdir(directory)
print("All items in the directory:")
print(all_items)

# Filter only files
files = [f for f in all_items if os.path.isfile(os.path.join(directory, f))]
print("\nFiles in the directory:")
print(files)
```

#### **Explanation**:
- **`os.listdir()`**: Returns a **list of all items** (files and subdirectories) in the specified directory.
- **Filtering Files**: We use **`os.path.isfile()`** to filter out only **files**, ignoring directories.
- **`os.path.join()`**: Combines the directory path with the filename to check if it’s a file.

#### **Output**:
```
All items in the directory:
['file1.py', 'file2.txt', 'subdir']

Files in the directory:
['file1.py', 'file2.txt']
```

### 📂 **Complete Example: Using `pathlib.Path().iterdir()` to List Files**

#### **2. Listing Files Using `pathlib.Path().iterdir()`**

```python
from pathlib import Path

# Define the directory path
directory = Path("/home/muhammad/projects")

# List all files and directories in the directory
all_items = list(directory.iterdir())
print("All items in the directory:")
for item in all_items:
    print(item)

# Filter only files
files = [f for f in directory.iterdir() if f.is_file()]
print("\nFiles in the directory:")
for file in files:
    print(file)
```

#### **Explanation**:
- **`directory.iterdir()`**: Returns an iterator of **Path** objects, representing all items (files and directories) in the directory.
- **Filtering Files**: The **`is_file()`** method is used to check if the item is a file.
- **Path Objects**: You get a **Path object** for each file, which can be used directly for further operations.

#### **Output**:
```
All items in the directory:
/home/muhammad/projects/file1.py
/home/muhammad/projects/file2.txt
/home/muhammad/projects/subdir

Files in the directory:
/home/muhammad/projects/file1.py
/home/muhammad/projects/file2.txt
```

### 📋 **Key Points**:

- **`os.listdir()`**:
  - Lists all files and directories in a directory.
  - You can filter files using **`os.path.isfile()`**.

- **`pathlib.Path().iterdir()`**:
  - Returns an iterator of **Path objects** for all items in the directory.
  - You can filter files using **`.is_file()`** and directories using **`.is_dir()`**.

### 🔄 **Practical Use Case: Listing Specific File Types (e.g., `.txt` files)**

You can filter for specific file types (e.g., `.txt` files) using either method:

#### **1. Using `os.listdir()`**:

```python
import os

directory = "/home/muhammad/projects"

# Filter for .txt files
txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
print("Text files in the directory:")
print(txt_files)
```

#### **2. Using `pathlib`**:

```python
from pathlib import Path

directory = Path("/home/muhammad/projects")

# Filter for .txt files
txt_files = [f for f in directory.iterdir() if f.is_file() and f.suffix == '.txt']
print("Text files in the directory:")
for txt_file in txt_files:
    print(txt_file)
```

#### **Explanation**:
- **File Extension Filtering**: In `os`, we use **`endswith('.txt')`**. In `pathlib`, we use **`.suffix == '.txt'`** to filter by file extension.

### 📋 **Summary**:

- **`os.listdir()`** provides a **simple list** of all items in a directory, and you can filter files using **`os.path.isfile()`**.
- **`pathlib.Path().iterdir()`** returns **Path objects**, offering a more modern and flexible way to list and filter files.
- You can easily filter files based on **file type** or other criteria by checking file extensions.
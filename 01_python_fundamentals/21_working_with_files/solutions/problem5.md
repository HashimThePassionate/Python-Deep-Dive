# 📝 **Quiz 5: Writing to a File (Only if it Doesn’t Exist)**

### Problem:
You want to **write data to a file**, but only if the file **does not already exist** on the filesystem. If the file already exists, you want to avoid overwriting it.
### 💡 **Hint**:
The **'x' mode** in Python is used for opening a file exclusively for writing. It raises a **FileExistsError** if the file already exists. This ensures that data is written to a new file without accidentally overwriting any existing file.
### 🔧 **Solution: Using `'x'` Mode to Write Data**

The `'x'` mode stands for **exclusive creation**. When you open a file with this mode:
- It will **create the file** if it doesn't exist.
- If the file **already exists**, Python will raise a **FileExistsError**, preventing you from overwriting the file.
### 📂 **Complete Example: Writing to a File Only if It Doesn't Exist**

```python
# Data to be written to the file
data = "This is some important data that should not be overwritten."

# Trying to create and write to a file in 'x' mode
try:
    with open('new_file.txt', 'x') as file:
        file.write(data)
        print("File 'new_file.txt' was created and data was written successfully.")
except FileExistsError:
    print("Error: 'new_file.txt' already exists. The file was not overwritten.")
```
### 📋 **Explanation**:

1. **Opening the File in 'x' Mode**: 
   - The file is opened using the **'x' mode**. This ensures that the file will only be created if it doesn’t already exist.
   - If the file **exists**, Python raises a **FileExistsError**, and the program handles this in the `except` block.

2. **Handling FileExistsError**: 
   - The `except` block catches the `FileExistsError` and prints a message indicating that the file already exists and was not overwritten.

3. **File Creation and Writing**:
   - If the file doesn't exist, it is created and the specified data is written to the file.
### 🖥 **Example Output**:

#### Case 1: If the file **does not exist**:
```
File 'new_file.txt' was created and data was written successfully.
```

#### Case 2: If the file **already exists**:
```
Error: 'new_file.txt' already exists. The file was not overwritten.
```
### 📝 **Key Points**:

- **'x' Mode**: The `'x'` mode ensures **exclusive creation** of a file. It raises an error if the file already exists, which prevents accidental overwrites.
- **FileExistsError**: This is raised when trying to open a file in `'x'` mode that already exists. You can handle this error to gracefully prevent overwriting files.
### 🔄 **Alternate Approach: Checking File Existence Before Writing**

Instead of using the `'x'` mode, you can manually check if a file exists before writing to it using Python’s `os.path.exists()` method:

```python
import os

# Data to be written
data = "Some important information."

# Check if the file exists before writing
if not os.path.exists('new_file.txt'):
    with open('new_file.txt', 'w') as file:
        file.write(data)
        print("File 'new_file.txt' was created and data was written.")
else:
    print("Error: 'new_file.txt' already exists.")
```

- **Explanation**: This checks if the file already exists using `os.path.exists()`. If the file exists, it prints an error. If not, it creates and writes to the file.
Both approaches ensure you don't accidentally overwrite a file when writing data. The `'x'` mode simplifies the process by raising an error if the file exists, while checking with `os.path.exists()` gives you more control.

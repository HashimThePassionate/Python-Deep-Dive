# 📝 **Quiz 2: Redirecting `print()` Output to a File**

### Problem:
You want to **redirect the output** of the `print()` function to a **file** instead of displaying it on the console.

### 💡 **Hint**:
The `print()` function has an optional **`file`** argument that allows you to send its output to a **file object**. By default, `print()` sends output to the console (`sys.stdout`), but you can specify a file object to send the output to a file instead.

### 🔧 **Solution: Redirecting `print()` Output to a File**

You can use the `file` parameter in the `print()` function to write its output directly to a file. This way, anything printed is saved in the file rather than displayed on the console.

#### **Example: Redirecting `print()` Output to a File**

```python
# Create a file object in write mode
with open('output_log.txt', 'w') as file:
    # Redirect print output to the file
    print("This is the first log entry.", file=file)
    print("This is the second log entry.", file=file)

# After running this code, the text will be written to 'output_log.txt'
```

### 📋 **Explanation**:

1. **Opening the File**: We open a file (`output_log.txt`) in **write mode** (`'w'`), which creates the file if it doesn't exist, or overwrites it if it does.
   
2. **Redirecting Output**: By passing `file=file` as an argument to the `print()` function, all the printed text is **redirected** to the file instead of being shown on the console.
   
3. **Using `with` Statement**: The `with` statement ensures that the file is automatically closed after the block of code is executed, making the operation more efficient and safe.

### 🖥 **Example: Reading the File after Redirecting Output**

```python
# Read the contents of the file to verify the output
with open('output_log.txt', 'r') as file:
    content = file.read()
    print("Content of output_log.txt:")
    print(content)
```

### 📋 **Key Points**:

- **`file=file`**: This argument in `print()` sends the output to the file rather than the console.
- **File Mode**: Opening the file in `'w'` mode ensures that it is ready for writing. Use `'a'` mode if you want to **append** to an existing file without overwriting it.
- **Automatic File Closing**: Using `with open()` ensures that the file is automatically closed once the block is finished.

### 🔄 **Alternative Approach: Using `sys.stdout`**

If you want to temporarily redirect the **entire output** of `print()` to a file, you can **redirect `sys.stdout`**.

#### **Example: Redirecting `sys.stdout` to a File**

```python
import sys

# Redirect print output to a file using sys.stdout
with open('output_log.txt', 'w') as file:
    original_stdout = sys.stdout  # Save the current stdout
    sys.stdout = file  # Redirect to file
    print("This will go to the file, not the console.")
    print("Another line for the file.")
    sys.stdout = original_stdout  # Reset to the original stdout

# Now, 'output_log.txt' will contain the redirected print statements
```

### 📋 **Key Takeaways**:

- **Redirection using `print()`**: Use the `file` argument in `print()` to redirect output.
- **Temporary Redirection using `sys.stdout`**: Redirect the entire output to a file using `sys.stdout`, and then reset it after.

# Try **with** resources statement 

#### Class and Method Definition

```python
class ExceptionsDemo:
    @staticmethod
    def show():
        reader = None
        try:
            reader = open("file.txt", "r")
            with reader:
                value = reader.read()
                print(value)  # This line prints the read content for demonstration purposes
                print("The 'with' statement automatically closed the file.")
        except FileNotFoundError:
            print("File not found.")
        except IOError as e:
            print("Could not read data")
            print(e)
        finally:
            if reader is not None:
                if not reader.closed:
                    reader.close()
                    print("File closed manually.")
                else:
                    print("File was already closed by 'with' statement.")

# Call the show method to demonstrate
ExceptionsDemo.show()
```

#### Method Body

1. **Variable Initialization:**
   - `reader = None` initializes the `reader` variable to `None`.

2. **Try Block:**

   ```python
   try:
       reader = open("file.txt", "r")
       with reader:
           value = reader.read()
           print(value)
           print("The 'with' statement automatically closed the file.")
   ```

   - `reader = open("file.txt", "r")`: Attempts to open the file `file.txt` in read mode.
   - `with reader:`: This `with` statement creates a context manager using the file object `reader`. It ensures that the file is automatically closed when the block is exited.
   - `value = reader.read()`: Reads the content of the file.
   - `print(value)`: Prints the content read from the file.
   - `print("The 'with' statement automatically closed the file.")`: Indicates that the `with` statement has automatically closed the file.

3. **Except Blocks:**
   - `except FileNotFoundError:` handles the case where the file is not found.
   - `except IOError as e:` handles other input/output errors and prints the error message.

4. **Finally Block:**

   ```python
   finally:
       if reader is not None:
           if not reader.closed:
               reader.close()
               print("File closed manually.")
           else:
               print("File was already closed by 'with' statement.")
   ```

   - This `finally` block ensures that the file is closed even if an exception occurs.
   - It first checks if `reader` is not `None` and then if the file is not already closed using the `closed` attribute.
   - If the file is still open, it manually closes it and prints a message indicating that the file was closed manually. If it's already closed, it prints a message indicating that it was closed by the `with` statement.

### How the `with` Statement Smartly Closes Resources

- **Automatic Resource Management:** The `with` statement creates a context manager that automatically manages the lifecycle of the resource (in this case, the file).
- **Automatic Closure:** When the block of code within the `with` statement is exited, regardless of whether an exception occurs or not, the context manager ensures that the resource is properly closed.
- **No Need for `finally`:** Because the `with` statement handles the resource closure automatically, there's no need for an explicit `finally` block to ensure cleanup.

### Summary

The `with` statement provides a clean and efficient way to manage resources by automatically closing them when they are no longer needed. This leads to more robust and concise code, as it eliminates the need for explicit cleanup code and reduces the likelihood of resource leaks. In the provided code, the `with` statement ensures that the file is closed properly, even if an exception occurs, improving the reliability of the program.
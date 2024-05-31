# Catching the exceptions

```python
class ExceptionsDemo:
    @staticmethod
    def show():
        try:
            with open("file.txt") as reader:  # Try to open the file "file.txt"
                if reader:  # Check if the file was successfully opened
                    print("File opened")  # If so, print a message indicating that the file was opened
        except FileNotFoundError as e:  # If a FileNotFoundError occurs during the execution of the try block, catch it
            print("File not found")  # Print a message indicating that the file was not found
            print(e)  # Print the error message associated with the FileNotFoundError
```

Explanation:
1. The `show()` method of the `ExceptionsDemo` class is defined as a static method.
2. Inside the `show()` method, a `try` block is used to encapsulate the code that may raise an exception.
3. Within the `try` block, the `open()` function is used to open the file named "file.txt" in the current directory. This is done using a `with` statement, which ensures that the file is properly closed after its suite finishes, even if an exception is raised.
4. The `if reader:` condition is used to check if the file was successfully opened. In Python, a file object evaluates to `True` if it is successfully opened and `False` otherwise.
5. If the file was opened successfully, a message "File opened" is printed.
6. If a `FileNotFoundError` occurs during the execution of the `try` block (i.e., if the file "file.txt" does not exist or cannot be opened), the execution jumps to the `except` block.
7. Inside the `except` block, a message "File not found" is printed to indicate that the file was not found.
8. Additionally, the `print(e)` statement is used to print the error message associated with the `FileNotFoundError`, providing more information about the specific error that occurred.

By using a `try-except` block, the program can handle potential errors gracefully without crashing. Instead of crashing, it prints informative error messages to the console, allowing the program to continue executing.
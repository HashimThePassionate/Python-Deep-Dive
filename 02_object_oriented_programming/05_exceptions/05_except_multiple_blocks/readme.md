# Accept Multiple Except Blocks:

#### Try Block

```python
try:
    x = int(input("Enter a number: "))
    y = 10 / x
    my_list = [1, 2, 3]
    print(my_list[x])
```

1. **`x = int(input("Enter a number: "))`:** 
   - Prompts the user to enter a number.
   - Converts the input from a string to an integer.
   - If the input is not a valid integer (e.g., if the user enters a letter or special character), a `ValueError` will be raised.

2. **`y = 10 / x`:**
   - Divides 10 by the number provided by the user (`x`).
   - If `x` is zero, a `ZeroDivisionError` will be raised because division by zero is not allowed in Python.

3. **`my_list = [1, 2, 3]`:**
   - Initializes a list with three elements: `[1, 2, 3]`.

4. **`print(my_list[x])`:**
   - Attempts to print the element at index `x` of `my_list`.
   - If `x` is not a valid index for the list (i.e., if `x` is greater than the highest index of the list or negative), an `IndexError` will be raised.

#### Except Blocks

```python
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
    print(f"Exception details: {e}")
    
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.")
    print(f"Exception details: {e}")
    
except IndexError as e:
    print("Error: List index out of range.")
    print(f"Exception details: {e}")
```

1. **`except ZeroDivisionError as e:`**
   - Catches the `ZeroDivisionError` if it is raised.
   - Prints an error message indicating that division by zero is not allowed.
   - Prints the exception details for further information.

2. **`except ValueError as e:`**
   - Catches the `ValueError` if it is raised.
   - Prints an error message indicating that the input was invalid.
   - Prints the exception details for further information.

3. **`except IndexError as e:`**
   - Catches the `IndexError` if it is raised.
   - Prints an error message indicating that the list index is out of range.
   - Prints the exception details for further information.

### How `try-except` Blocks Work

- The `try` block is used to wrap the code that may raise exceptions. 
- If an exception occurs, the `try` block is exited, and Python looks for an `except` block that matches the type of exception.
- When a matching `except` block is found, the code inside that block is executed.
- If no matching `except` block is found, the program will terminate with an unhandled exception.

### Example Scenarios

1. **User enters "a":**
   - `ValueError` will be raised because "a" cannot be converted to an integer.
   - The `except ValueError as e:` block will handle this exception.

2. **User enters "0":**
   - `x` becomes 0.
   - `ZeroDivisionError` will be raised during `y = 10 / x`.
   - The `except ZeroDivisionError as e:` block will handle this exception.

3. **User enters "5":**
   - `x` becomes 5.
   - No exception is raised during `y = 10 / x`.
   - `IndexError` will be raised during `print(my_list[x])` because the list `my_list` has only 3 elements (indices 0, 1, 2).
   - The `except IndexError as e:` block will handle this exception.

By using multiple `except` blocks, you can handle different types of exceptions in a granular and specific manner, allowing for more informative error messages and better control over the program's behavior in the face of errors.
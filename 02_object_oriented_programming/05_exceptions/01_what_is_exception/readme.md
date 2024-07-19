# Understanding and Handling Exceptions in Python

## What is an Exception?

An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. When an error occurs within a program, Python creates an exception object. If this exception is not handled, the program will terminate abruptly. 

Exceptions can be handled using `try`, `except`, `else`, and `finally` blocks.

### How to Handle Exceptions?

To handle exceptions, you can use a `try` block to wrap the code that may cause an exception, followed by one or more `except` blocks to handle specific exceptions. An `else` block can be used to execute code if no exceptions are raised, and a `finally` block can be used to execute code regardless of whether an exception occurred or not.

### Code Explanation: Custom Exceptions and Handling in Python

This code demonstrates how to create and handle custom exceptions in Python.

#### Classes and Methods

1. **Custom Exception Classes:**
    - `StringException`: Raised when a non-string type is provided.
    - `IntegerNotAllowedException`: Raised when an integer type is provided.

2. **ExceptionsDemo Class:**
    - `show`: Static method that attempts to call `say_hello` and handles any exceptions that occur.
    - `say_hello`: Static method that checks the type of `name` and raises appropriate exceptions or prints the name in uppercase if no exception occurs.

```python
class StringException(Exception):
    def __init__(self, name):
        super().__init__(f'Nonetype is not allowed, you entered /{name}/')

class IntegerNotAllowedException(Exception):
    def __init__(self, i):
        super().__init__(f'Integers are not allowed, you entered /{i}/')

class ExceptionsDemo:
    @staticmethod
    def show(name):
        try:
            ExceptionsDemo.say_hello(name)
        except (StringException, IntegerNotAllowedException) as error:
            print(error)

    @staticmethod
    def say_hello(name):
        if isinstance(name, int):
            raise IntegerNotAllowedException(name)
        if not isinstance(name, str):
            raise StringException(name)
        print(name.upper())

# Testing the functionality:
ExceptionsDemo.show(None)  # Should raise StringException
ExceptionsDemo.show('John')  # Should print 'JOHN'
ExceptionsDemo.show(1)  # Should raise IntegerNotAllowedException
```

#### Detailed Breakdown

1. **Custom Exception Classes:**
    - `StringException`: Inherits from `Exception`. It customizes the initialization to display a message indicating that `NoneType` (or any non-string) is not allowed.
    - `IntegerNotAllowedException`: Inherits from `Exception`. It customizes the initialization to display a message indicating that integers are not allowed.

2. **ExceptionsDemo Class:**
    - `show`: This method tries to call `say_hello` with the provided `name`. If a `StringException` or `IntegerNotAllowedException` is raised, it catches the exception and prints the error message.
    - `say_hello`: This method checks if `name` is an integer, raises `IntegerNotAllowedException` if true. If `name` is not a string, it raises `StringException`. Otherwise, it prints the `name` in uppercase.

#### Examples:

1. `ExceptionsDemo.show(None)`:
   - This call will raise `StringException` because `None` is not a string.
   - **Output**: `Nonetype is not allowed, you entered /None/`

2. `ExceptionsDemo.show('John')`:
   - This call will print `JOHN` because 'John' is a valid string.
   - **Output**: `JOHN`

3. `ExceptionsDemo.show(1)`:
   - This call will raise `IntegerNotAllowedException` because `1` is an integer.
   - **Output**: `Integers are not allowed, you entered /1/`

This demonstrates how custom exceptions can be created and handled in Python to enforce specific input types and provide meaningful error messages.

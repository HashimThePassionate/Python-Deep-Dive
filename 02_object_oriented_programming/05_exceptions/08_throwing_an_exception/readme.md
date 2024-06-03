# Throwing an exception

#### Custom Exception Class

```python
class IllegalArgumentError(Exception):
    pass
```

- We define a custom exception class `IllegalArgumentError` that inherits from the built-in `Exception` class. This allows us to create a specialized exception type for our application.

#### Account Class

```python
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, value):
        if value <= 0:
            raise IllegalArgumentError()
```

- The `Account` class represents a basic account with a balance.
- The `deposit` method allows depositing money into the account. However, it raises an `IllegalArgumentError` if the deposited amount is less than or equal to zero.

#### ExceptionsDemo Class

```python
class ExceptionsDemo:
    @staticmethod
    def show():
        account = Account()
        try:
            account.deposit(1)
        except IllegalArgumentError:
            print("Invalid deposit amount. Value must be greater than zero.")
```

- The `ExceptionsDemo` class contains a static method `show` to demonstrate how to handle the `IllegalArgumentError`.
- Inside the `try` block, we create an `Account` object and attempt to deposit an amount (1 in this case) using the `deposit` method.
- If the `deposit` method raises an `IllegalArgumentError`, we catch it in the `except` block and print an error message indicating that the deposit amount is invalid.

#### Calling the Method

```python
ExceptionsDemo.show()
```

- Finally, we call the `show` method of the `ExceptionsDemo` class to demonstrate the handling of the `IllegalArgumentError`.

### How Exceptions Are Raised

- In the `deposit` method of the `Account` class, an `IllegalArgumentError` is raised using the `raise` keyword if the deposit value is less than or equal to zero.
- When an exception is raised, the normal program flow is disrupted, and Python starts looking for an appropriate exception handler to handle it.

### Summary

By raising custom exceptions, we can signal exceptional conditions in our code and handle them gracefully using `try-except` blocks. Custom exceptions allow us to provide meaningful error messages and separate the concerns of error handling from the core logic of the program. In this example, `IllegalArgumentError` is raised when an invalid deposit amount is provided, and it is caught and handled appropriately in the `ExceptionsDemo` class.
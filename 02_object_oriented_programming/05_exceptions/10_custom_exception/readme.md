# Custom Exceptions

We create a custom exception class named `InsufficientFundsException` to handle the scenario where a withdrawal operation is attempted with insufficient funds in the account. 
### Code Explanation

#### Custom Exception Class

```python
class InsufficientFundsException(Exception):
    def __init__(self):
        super().__init__("Insufficient funds in your account.")
```

- We define a custom exception class `InsufficientFundsException` that inherits from the built-in `Exception` class.
- In the `__init__` method, we call the `__init__` method of the parent class (`Exception`) using `super().__init__()` to initialize the exception with a default error message.

#### Account Class

```python
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, value):
        if value <= 0:
            raise ValueError("Deposit value must be greater than zero.")

    def withdraw(self, value):
        if value > self.balance:
            raise InsufficientFundsException()
```

- The `Account` class represents a basic account with a balance.
- The `deposit` method allows depositing money into the account. It raises a `ValueError` if the deposited amount is less than or equal to zero.
- The `withdraw` method attempts to withdraw money from the account. It raises an `InsufficientFundsException` if the withdrawal amount exceeds the current balance.

#### ExceptionsDemo Class

```python
class ExceptionsDemo:
    @staticmethod
    def show():
        account = Account()
        try:
            account.withdraw(10)
        except InsufficientFundsException as e:
            print(e)
```

- The `ExceptionsDemo` class contains a static method `show` to demonstrate how to handle the `InsufficientFundsException`.
- Inside the `try` block, we create an `Account` object and attempt to withdraw an amount (10 in this case).
- If an `InsufficientFundsException` is caught in the `except` block, we print the exception message.

#### Calling the Method

```python
ExceptionsDemo.show()
```

- Finally, we call the `show` method of the `ExceptionsDemo` class to demonstrate the handling of the `InsufficientFundsException`.

### How Custom Exceptions Are Created and Used

1. **Custom Exception Class:**
   - We define a custom exception class `InsufficientFundsException` by inheriting from the base `Exception` class.
   - We can provide additional functionality, such as initializing the exception with a custom error message.

2. **Raising the Custom Exception:**
   - In the `withdraw` method of the `Account` class, we raise an instance of `InsufficientFundsException` when a withdrawal is attempted with insufficient funds.

3. **Handling the Custom Exception:**
   - In the `ExceptionsDemo` class, we catch the `InsufficientFundsException` in the `except` block and print the exception message.

### Summary

Custom exceptions allow us to create specialized error classes tailored to specific scenarios in our application. By defining custom exception classes, we can provide more descriptive error messages and handle exceptional conditions more effectively. In this example, the `InsufficientFundsException` class is created to handle cases where a withdrawal operation is attempted with insufficient funds, providing better clarity and control over error handling in the program.
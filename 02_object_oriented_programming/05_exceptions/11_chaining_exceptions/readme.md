# Chaining an exception
We demonstrate how to implement exception chaining, where one exception is raised as a direct cause of another exception.

### Complete Code
```python
class AccountException(Exception):
    def __init__(self, cause):
        super().__init__(cause)


class InsufficientFundsException(Exception):
    def __init__(self):
        super().__init__("Insufficient funds in your account.")


class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, value):
        if value <= 0:
            raise ValueError("Deposit value must be greater than zero.")

    def withdraw(self, value):
        if value > self.balance:
            raise AccountException(InsufficientFundsException())


class ExceptionsDemo:
    @staticmethod
    def show():
        account = Account()
        try:
            account.withdraw(10)
        except AccountException as e:
            cause = e.args[0]  # Get the cause from the tuple of arguments
            print(cause)
ExceptionsDemo.show()
```

#### Custom Exception Classes

```python
class AccountException(Exception):
    def __init__(self, cause):
        super().__init__(cause)

class InsufficientFundsException(Exception):
    def __init__(self):
        super().__init__("Insufficient funds in your account.")
```

- We define two custom exception classes, `AccountException` and `InsufficientFundsException`.

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
            raise AccountException(InsufficientFundsException())
```

- The `Account` class remains similar to the previous examples.
- The `withdraw` method raises an `AccountException` with an `InsufficientFundsException` as its cause if the withdrawal amount exceeds the current balance.

#### ExceptionsDemo Class

```python
class ExceptionsDemo:
    @staticmethod
    def show():
        account = Account()
        try:
            account.withdraw(10)
        except AccountException as e:
            cause = e.args[0]  # Get the cause from the tuple of arguments
            print(cause)
```

- The `ExceptionsDemo` class contains a static method `show` to demonstrate how to handle the `AccountException`.
- Inside the `try` block, we create an `Account` object and attempt to withdraw an amount (10 in this case).
- If an `AccountException` is caught in the `except` block, we extract the cause from the exception object and print it.

#### Calling the Method

```python
ExceptionsDemo.show()
```

- Finally, we call the `show` method of the `ExceptionsDemo` class to demonstrate the handling of the `AccountException` and the chained `InsufficientFundsException`.

### How Exception Chaining Is Implemented

- When raising the `AccountException` in the `withdraw` method of the `Account` class, we pass an instance of `InsufficientFundsException` as the cause.
- The `AccountException` class takes the cause as an argument in its constructor and passes it to the constructor of the parent class (`Exception`) using `super().__init__(cause)`.
- In the `ExceptionsDemo` class, when we catch the `AccountException`, we can access the cause of the exception from the tuple of arguments using `e.args[0]`.

### Summary

Exception chaining allows us to associate one exception with another, providing additional context about the cause of an error. By chaining exceptions, we can propagate more detailed information about the error conditions, making it easier to diagnose and handle exceptional situations in our code. In this example, the `AccountException` is chained with an `InsufficientFundsException`, indicating that the account withdrawal failed due to insufficient funds.

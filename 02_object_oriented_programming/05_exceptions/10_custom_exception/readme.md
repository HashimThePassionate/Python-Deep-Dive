# Understanding and Handling Custom Exceptions in Python

## What is a Custom Exception?

A custom exception in Python is a user-defined error type that extends the base `Exception` class. Creating custom exceptions allows you to handle specific error conditions in a way that is meaningful for your application, providing more descriptive error messages and making your code more robust and readable.

### How to Create and Use Custom Exceptions?

To create a custom exception, define a new class that inherits from the `Exception` class. You can customize the initialization method to accept additional arguments and provide a more descriptive error message. 

### Code Explanation: Custom Exceptions and Handling in Python

This code demonstrates how to create and handle custom exceptions for a simple bank account management system.

#### Classes and Methods

1. **Custom Exception Class:**
    - `InsufficientFunds`: Raised when a withdrawal amount exceeds the current balance.

2. **Account Class:**
    - `__init__`: Initializes the account with a given balance.
    - `withdraw`: Withdraws a specified amount from the account, raising `InsufficientFunds` if the balance is insufficient.
    - `deposit`: Deposits a specified amount into the account, raising a `ValueError` if the amount is non-positive.
    - `__str__`: Returns a string representation of the account balance.

```python
class InsufficientFunds(Exception):
    def __init__(self, balance, amount):
        super().__init__(f'Insufficient funds: You have {balance} in your account and you are trying to withdraw {amount}')

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds(self.balance, amount)
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be greater than 0')
        self.balance += amount
        return self.balance
    
    def __str__(self):
        return f'Account balance: {self.balance}'

# Example Usage:

try:
    account = Account(100)
    account.withdraw(200)
except InsufficientFunds as e:
    print(e)

try:
    account = Account(100)
    account.deposit(-10)
except ValueError as e:
    print(e)

try:
    account = Account(100)
    account.withdraw(50)
    account.deposit(30)
    print(account)
except InsufficientFunds as e:
    print(e)
```

#### Detailed Breakdown

1. **Custom Exception Class:**
    - `InsufficientFunds`: Inherits from `Exception`. The initialization method takes `balance` and `amount` as arguments and constructs an error message indicating the insufficient funds.

2. **Account Class:**
    - `__init__(self, balance)`: Initializes the account with a given balance.
    - `withdraw(self, amount)`: 
      - Checks if the withdrawal amount is greater than the current balance.
      - Raises `InsufficientFunds` if true.
      - Deducts the amount from the balance and returns the new balance.
    - `deposit(self, amount)`:
      - Checks if the deposit amount is less than or equal to zero.
      - Raises `ValueError` if true.
      - Adds the amount to the balance and returns the new balance.
    - `__str__(self)`: Returns the account balance as a string.

#### Examples:

1. **Handling InsufficientFunds Exception:**
    ```python
    try:
        account = Account(100)
        account.withdraw(200)
    except InsufficientFunds as e:
        print(e)
    ```
    - This will raise `InsufficientFunds` because the withdrawal amount exceeds the balance.
    - **Output**: `Insufficient funds: You have 100 in your account and you are trying to withdraw 200`

2. **Handling ValueError Exception:**
    ```python
    try:
        account = Account(100)
        account.deposit(-10)
    except ValueError as e:
        print(e)
    ```
    - This will raise `ValueError` because the deposit amount is non-positive.
    - **Output**: `Amount must be greater than 0`

3. **Successful Withdrawal and Deposit:**
    ```python
    try:
        account = Account(100)
        account.withdraw(50)
        account.deposit(30)
        print(account)
    except InsufficientFunds as e:
        print(e)
    ```
    - This will successfully withdraw 50 and deposit 30 into the account.
    - **Output**: `Account balance: 80`

This demonstrates how custom exceptions can be created and handled in Python to manage specific error conditions in an application.

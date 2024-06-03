# Re-throwing an exception

Lets demonstrate how to re-throw an exception after performing some logging or additional processing. 

### Code Explanation

#### Custom Exception Class

```python
class IllegalArgumentError(Exception):
    pass
```

- We define a custom exception class `IllegalArgumentError` similar to the previous example.

#### Account Class

```python
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, value):
        if value <= 0:
            raise IllegalArgumentError()
```

- The `Account` class remains the same as before, with the `deposit` method raising an `IllegalArgumentError` if the deposited amount is less than or equal to zero.

#### ExceptionsDemo Class

```python
class ExceptionsDemo:
    @staticmethod
    def show():
        account = Account()
        try:
            account.deposit(-1)
        except IllegalArgumentError as e:
            print("Logging")
            raise e
```

- The `ExceptionsDemo` class contains a static method `show` to demonstrate re-throwing an exception.
- Inside the `try` block, we create an `Account` object and attempt to deposit an invalid amount (-1 in this case).
- If an `IllegalArgumentError` is caught in the `except` block, we print "Logging" to indicate that we are performing some logging.
- Then, we re-raise the caught exception using `raise e`, which effectively propagates the exception to the calling code.

#### Handling the Exception

```python
try:
    ExceptionsDemo.show()
except IllegalArgumentError as e:
    print("Unexpected Error Occurred")
```

- We call the `show` method of the `ExceptionsDemo` class inside a `try-except` block.
- If an `IllegalArgumentError` is raised during the execution of `ExceptionsDemo.show()`, it will be caught in the `except` block.
- In this case, we print "Unexpected Error Occurred" to indicate that an unexpected error was encountered.

### How Re-throwing Exceptions Works

- When we catch an exception (`IllegalArgumentError` in this case) in the `ExceptionsDemo.show()` method, we can perform additional processing, such as logging.
- After performing the necessary processing, we re-raise the caught exception using `raise e`.
- This re-raises the exception, causing it to propagate up the call stack until it is caught by another exception handler, or if it is uncaught, it will cause the program to terminate and display the traceback.

### Summary

Re-throwing exceptions allows us to perform additional processing or logging before propagating the exception to higher levels of the program. It can be useful for adding context to exceptions or for handling exceptions at different levels of abstraction. In this example, we catch and re-throw the `IllegalArgumentError` in the `ExceptionsDemo.show()` method, allowing the calling code to handle the exception appropriately.
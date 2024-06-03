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

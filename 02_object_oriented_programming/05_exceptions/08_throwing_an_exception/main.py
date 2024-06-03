class IllegalArgumentError(Exception):
    pass

class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, value):
        if value <= 0:
            raise IllegalArgumentError()

class ExceptionsDemo:
    @staticmethod
    def show():
        account = Account()
        try:
            account.deposit(1)
        except IllegalArgumentError:
            print("Invalid deposit amount. Value must be greater than zero.")

# Call the show method to demonstrate
ExceptionsDemo.show()

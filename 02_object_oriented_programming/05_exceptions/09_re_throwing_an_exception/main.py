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
            account.deposit(-1)
        except IllegalArgumentError as e:
            print("Logging")
            raise e


try:
    ExceptionsDemo.show()
except IllegalArgumentError as e:
    print("Unexpected Error Occurred")

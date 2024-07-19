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

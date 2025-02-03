class InsufficientFunds(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds, balance: {balance}, withdraw: {amount}")

    def deficit(self):
        return self.amount - self.balance


class InvalidTransaction(Exception):
    """Raise when an invalid transaction (negative or zero amount) is attempted."""
    def __init__(self, amount):
        super().__init__(f"Invalid transaction: amount must be positive, got {amount}")


class Bank:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidTransaction(amount)
        if amount > self.balance:
            raise InsufficientFunds(self.balance, amount)
        self.balance -= amount
        return f"Withdrew ${amount}, remaining balance is ${self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidTransaction(amount)
        self.balance += amount
        return f"Deposited ${amount}, total balance is ${self.balance}"

    def __str__(self):
        return f"BankAccount(balance=${self.balance})"


# ✅ Testing the improved Bank class
account = Bank(5000)
print(account)

print(account.deposit(1000))  # ✅ Valid deposit
print(account)

print(account.withdraw(2000))  # ✅ Valid withdrawal
print(account)

try:
    account.withdraw(6000)  # ❌ Insufficient funds
except InsufficientFunds as e:
    print(e)
    print(f"Deficit: ${e.deficit()}")

try:
    account.deposit(-500)  # ❌ Invalid deposit
except InvalidTransaction as e:
    print(e)

try:
    account.withdraw(-100)  # ❌ Invalid withdrawal
except InvalidTransaction as e:
    print(e)

print(account.deposit(2000))  # ✅ Valid deposit
print(account)

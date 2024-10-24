# Union Types 🏦💳💸

In this section, we'll explore Union types through a practical example of a **Payment Processing System**. This will demonstrate how Union types allow for handling multiple types within a single function, making your code clean, flexible, and robust. 🌟

## **Table of Contents** 📖

1. [Introduction to Union Types](#1-introduction-to-union-types-)
2. [Benefits of Using Union Types](#2-benefits-of-using-union-types-)
3. [Practical Example: Payment Processing System](#3-practical-example-payment-processing-system-)
   - [Initial Implementation](#initial-implementation-)
   - [Adding Multiple Payment Methods](#adding-multiple-payment-methods-)
   - [Using Union Types for Flexibility](#using-union-types-for-flexibility-)
   - [Type Checking with `mypy`](#type-checking-with-mypy-)
   - [Full Code Listing](#full-code-listing-)
4. [Understanding Product and Sum Types](#4-understanding-product-and-sum-types-)
5. [Conclusion](#5-conclusion-)
6. [Discussion Topic](#6-discussion-topic-)
7. [Additional Resources](#7-additional-resources-)


## **1. Introduction to Union Types** 🤔

A **Union Type** allows you to specify that a variable can take multiple types. This is particularly useful when you need to handle different types of inputs or outputs within a single function.

### **Syntax** 🖋️

```python
from typing import Union

variable: Union[Type1, Type2] = value
```

In Python 3.10 and later, a simpler syntax is also available:

```python
variable: int | str = 42
```

### **Example**

```python
from typing import Union

def parse_user_input(value: str) -> int | str:
    if value.isdigit():
        return int(value)
    return value

result: Union[int, str] = parse_user_input("hello")
print(result)  # Output: "hello" (as a str)
```


## **2. Benefits of Using Union Types** 🌟

1. **Simplifies Code**: Handles different data types within the same function without complex conditions.
2. **Clear Communication**: Makes it obvious to other developers what types a variable can hold.
3. **Better Type Checking**: Tools like `mypy` can help catch errors, ensuring your code is robust and error-free.
4. **Backwards Compatibility**: Maintains compatibility by supporting multiple types as needed.


## **3. Practical Example: Payment Processing System** 💳💵🪙

Let's look at a real-world example where Union types are particularly useful: a **Payment Processing System**. Our goal is to allow users to pay using **Credit Card**, **PayPal**, or **Cryptocurrency**.

### **Initial Implementation** 🛠️

```python
class CreditCardPayment:
    def __init__(self, card_number: str, amount: float):
        self.card_number = card_number
        self.amount = amount

class PayPalPayment:
    def __init__(self, email: str, amount: float):
        self.email = email
        self.amount = amount

class CryptoPayment:
    def __init__(self, wallet_address: str, amount: float):
        self.wallet_address = wallet_address
        self.amount = amount
```

**Explanation**: We have three separate classes for handling **Credit Card**, **PayPal**, and **Crypto Payments**.

### **Adding Multiple Payment Methods** 🏦

Now, we want to create a **unified function** that can handle all these types of payments. Without Union types, this would require complex conditions or multiple functions.

### **Using Union Types for Flexibility** ✨

```python
from typing import Union

def process_payment(payment: CreditCardPayment | PayPalPayment | CryptoPayment) -> None:
    if isinstance(payment, CreditCardPayment):
        print(f"Processing Credit Card payment of ${payment.amount} using card: {payment.card_number}. 💳")
    elif isinstance(payment, PayPalPayment):
        print(f"Processing PayPal payment of ${payment.amount} using email: {payment.email}. 📧")
    elif isinstance(payment, CryptoPayment):
        print(f"Processing Crypto payment of ${payment.amount} using wallet: {payment.wallet_address}. 🪙")
    else:
        raise ValueError("Invalid payment method.")
```

**Explanation**: The function `process_payment` can now handle multiple types of payments using a **Union** type, making it versatile and easy to maintain.

### **Type Checking with `mypy`** 🔍

```bash
mypy --strict main.py
```

**Expected Output:**

```
Success: no issues found in 1 source file
```

### **Full Code Listing** 📜

```python
from typing import Union

class CreditCardPayment:
    def __init__(self, card_number: str, amount: float):
        self.card_number = card_number
        self.amount = amount

class PayPalPayment:
    def __init__(self, email: str, amount: float):
        self.email = email
        self.amount = amount

class CryptoPayment:
    def __init__(self, wallet_address: str, amount: float):
        self.wallet_address = wallet_address
        self.amount = amount

def process_payment(payment: CreditCardPayment | PayPalPayment | CryptoPayment) -> None:
    if isinstance(payment, CreditCardPayment):
        print(f"Processing Credit Card payment of ${payment.amount} using card: {payment.card_number}. 💳")
    elif isinstance(payment, PayPalPayment):
        print(f"Processing PayPal payment of ${payment.amount} using email: {payment.email}. 📧")
    elif isinstance(payment, CryptoPayment):
        print(f"Processing Crypto payment of ${payment.amount} using wallet: {payment.wallet_address}. 🪙")
    else:
        raise ValueError("Invalid payment method.")

# Testing the function
def main():
    card_payment = CreditCardPayment("1234-5678-9012-3456", 100.00)
    paypal_payment = PayPalPayment("user@example.com", 75.00)
    crypto_payment = CryptoPayment("0xABC12345", 50.00)

    process_payment(card_payment)
    process_payment(paypal_payment)
    process_payment(crypto_payment)

if __name__ == "__main__":
    main()
```

### **Program Output**

```
Processing Credit Card payment of $100.0 using card: 1234-5678-9012-3456. 💳
Processing PayPal payment of $75.0 using email: user@example.com. 📧
Processing Crypto payment of $50.0 using wallet: 0xABC12345. 🪙
```


## **4. Understanding Product and Sum Types** 📊

### **Example of Product Types** ✖️

When you have combinations of types, the total possible states multiply:

```python
class Payment:
    def __init__(self, payment_type: str, amount: float, success: bool):
        self.payment_type = payment_type
        self.amount = amount
        self.success = success
```

**State Space**: Multiple values can lead to `3 × 5 × 2 = 30` combinations, making error handling difficult.

### **Example of Sum Types** ➕

By using Union Types (Sum Types), you reduce state space:

```python
from typing import Union

payment: Union[CreditCardPayment, PayPalPayment, CryptoPayment]
```

**Benefit**: Less complexity, clear separation of states, and reduced potential errors.


## **5. Conclusion** 🎯

Union Types in Python allow you to handle variables of multiple types effectively:

1. **Simplifies Code**: Reduces the need for complex structures or multiple functions.
2. **Improves Clarity**: Makes it easy for other developers to understand what types are being handled.
3. **Catches Errors**: Ensures proper handling of all cases, reducing bugs and errors.


## **6. Discussion Topic** 💬

**Question**: Have you ever faced a situation where Union Types could have simplified your code? How did you handle it? Share your experiences, and let’s discuss how Union Types can help make your code cleaner.


## **7. Additional Resources** 📚

- [Python `typing` Module Documentation](https://docs.python.org/3/library/typing.html)
- [Python Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Python Type Checking (Guide)](https://realpython.com/python-type-checking/)


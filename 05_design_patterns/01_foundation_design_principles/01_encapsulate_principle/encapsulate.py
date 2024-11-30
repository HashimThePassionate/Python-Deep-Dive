class PaymentBase:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount

    def process_payment(self) -> None:
        pass

class CreditCard(PaymentBase):
    def process_payment(self) -> None:
        print(f"Credit card payment: {self.amount}")

class PayPal(PaymentBase):
    def process_payment(self) -> None:
        print(f"PayPal payment: {self.amount}")


if __name__ == "__main__":
    payments: list[PaymentBase] = [CreditCard(100), PayPal(200)]
    for payment in payments:
        payment.process_payment()

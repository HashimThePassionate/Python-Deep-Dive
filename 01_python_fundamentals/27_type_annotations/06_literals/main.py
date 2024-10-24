from typing import Literal
def process_payment(method: Literal["Credit Card", "PayPal", "Crypto"]) -> str:
    return f"Processing {method} payment."

# Valid Examples
print(process_payment("Credit Card"))  # ✅
print(process_payment("PayPal"))       # ✅

# Invalid Example
print(process_payment("Cash"))  # ❌ Type error

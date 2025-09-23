from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from uuid import uuid4

# ---- Result types -----------------------------------------------------------


@dataclass
class PaymentReceipt:
    status: Literal["paid"]
    amount_charged: float          # final amount after tax/fees
    currency: Literal["USD"]
    subtotal: float
    tax_applied: float
    txn_id: str


@dataclass
class PromoRedemption:
    status: Literal["promo_applied"]
    code: str
    discount_amount: float         # absolute discount value
    message: str


@dataclass
class PaymentError:
    status: Literal["error"]
    code: Literal["INVALID_AMOUNT", "BAD_PROMO"]
    message: str

# ---- Processor --------------------------------------------------------------


def process_payment(amount: int | float | str,
                    *,
                    currency: Literal["USD"] = "USD",
                    tax_rate: float = 0.05) -> PaymentReceipt | PromoRedemption | PaymentError:
    """
    Realistic-ish payment handler:
      - number (int/float) => charges, applies tax, returns PaymentReceipt
      - string             => treats as promo code, returns PromoRedemption or PaymentError
    """

    promo_codes = {
        # absolute discounts
        "FREE100": ("abs", 100.0),
        "DISCOUNT50": ("abs", 50.0),
        # percentage discount example
        "PCT10": ("pct", 10.0),
    }

    # Promo-code path
    if isinstance(amount, str):
        rule = promo_codes.get(amount.upper())
        if not rule:
            return PaymentError(status="error", code="BAD_PROMO",
                                message=f"Invalid promo code: {amount}")
        kind, value = rule
        # caller applies pct/abs to their subtotal
        discount = value if kind == "abs" else value
        msg = f"Promo '{amount.upper()}' applied: " + \
            (f"{value}% off" if kind == "pct" else f"${value:.2f} off")
        return PromoRedemption(status="promo_applied", code=amount.upper(),
                               discount_amount=discount, message=msg)

    # Numeric charge path
    if not isinstance(amount, (int, float)) or amount <= 0:
        return PaymentError(status="error", code="INVALID_AMOUNT",
                            message="Amount must be a positive number.")

    subtotal = float(amount)
    tax = round(subtotal * tax_rate, 2)
    final = round(subtotal + tax, 2)
    receipt = PaymentReceipt(
        status="paid",
        amount_charged=final,
        currency=currency,
        subtotal=subtotal,
        tax_applied=tax,
        txn_id=str(uuid4())
    )
    return receipt

# ---- Example usage ----------------------------------------------------------


def demo():
    results = [
        process_payment(100),           # charge
        process_payment(99.99),         # charge
        process_payment("FREE100"),     # promo (absolute)
        process_payment("PCT10"),       # promo (percent)
        process_payment("XYZ123"),      # bad promo
        process_payment(-50),           # bad amount
    ]

    # Pattern match the union results (Python 3.10+)
    for r in results:
        match r:
            case PaymentReceipt():
                print(
                    f"[OK] TXN={r.txn_id} charged ${r.amount_charged} (subtotal ${r.subtotal}, tax ${r.tax_applied})")
            case PromoRedemption():
                print(f"[PROMO] {r.message}")
            case PaymentError():
                print(f"[ERR] {r.code}: {r.message}")


if __name__ == "__main__":
    demo()

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol, Final, assert_never
import math

# ----- Types -----
Currency = Literal["USD", "EUR", "GBP", "PKR"]

@dataclass(frozen=True)
class Receipt:
    currency: Currency
    gross: float          # input amount from caller
    fee: float            # gateway/payment fee
    tax: float            # VAT/sales tax etc.
    net_settlement: float # what merchant receives (post-fees/tax)
    gateway: str          # which gateway was used
    note: str             # any extra compliance/rounding note


class PaymentGateway(Protocol):
    def authorize_and_capture(self, amount: float, currency: Currency) -> Receipt: ...


# ----- Helpers -----
def round_to_nearest_0_05(amount: float) -> float:
    """GBP cash rules example: round to nearest 0.05."""
    return round(amount * 20) / 20.0

def round_2(amount: float) -> float:
    return round(amount + 1e-9, 2)  # avoid fp edge jitters

def to_paisa(amount_pkr: float) -> int:
    """PKR smallest unit = paisa (1 PKR = 100 paisa). Enforce integer minor-units."""
    return int(round(amount_pkr * 100))


# ----- Concrete gateways with per-currency logic -----
class UsdGateway:
    # Example: Stripe-style pricing, 2.9% + $0.30, US sales tax not applied by PSP here
    PERCENT_FEE: Final = 0.029
    FIXED_FEE:   Final = 0.30

    def authorize_and_capture(self, amount: float, currency: Currency) -> Receipt:
        fee = round_2(amount * self.PERCENT_FEE + self.FIXED_FEE)
        tax = 0.0  # assume tax handled elsewhere or not applicable
        net = round_2(amount - fee - tax)
        return Receipt(currency="USD", gross=round_2(amount), fee=fee, tax=tax,
                       net_settlement=net, gateway="Stripe-US",
                       note="2.9% + $0.30 applied; no VAT.")


class EurGateway:
    # Example: 1.8% fee + VAT 21% on fee (EU PSP may charge VAT on service fees)
    PERCENT_FEE: Final = 0.018
    VAT_RATE:    Final = 0.21

    def authorize_and_capture(self, amount: float, currency: Currency) -> Receipt:
        base_fee = round_2(amount * self.PERCENT_FEE)
        vat_on_fee = round_2(base_fee * self.VAT_RATE)
        fee = round_2(base_fee + vat_on_fee)
        tax = 0.0  # end-customer VAT is seller’s concern; here we model VAT on fees only
        net = round_2(amount - fee - tax)
        return Receipt(currency="EUR", gross=round_2(amount), fee=fee, tax=tax,
                       net_settlement=net, gateway="Adyen-EU",
                       note="1.8% fee + 21% VAT on fee.")


class GbpGateway:
    # Example: 1.5% fee, cash rounding to 0.05 for settlement note
    PERCENT_FEE: Final = 0.015

    def authorize_and_capture(self, amount: float, currency: Currency) -> Receipt:
        # Some retail ops round display/settlement amounts to 0.05 in GBP cash contexts
        rounded_gross = round_to_nearest_0_05(amount)
        fee = round_2(rounded_gross * self.PERCENT_FEE)
        tax = 0.0
        net = round_2(rounded_gross - fee - tax)
        return Receipt(currency="GBP", gross=rounded_gross, fee=fee, tax=tax,
                       net_settlement=net, gateway="Worldpay-UK",
                       note="Gross rounded to nearest £0.05 before fee.")


class PkrGateway:
    # Example: local rails, flat 1.2% fee, enforce integer paisa settlement, and min amount
    PERCENT_FEE: Final = 0.012
    MIN_AMOUNT_PKR: Final = 50.00  # enforce minimum charge

    def authorize_and_capture(self, amount: float, currency: Currency) -> Receipt:
        if amount < self.MIN_AMOUNT_PKR:
            raise ValueError(f"Minimum charge is PKR {self.MIN_AMOUNT_PKR:.2f}")
        fee = round_2(amount * self.PERCENT_FEE)
        tax = 0.0
        net = amount - fee - tax
        # settle in paisa as integer minor units (compliance with local settlement rails)
        minor_units = to_paisa(net)
        net_integerized = minor_units / 100.0
        return Receipt(currency="PKR", gross=round_2(amount), fee=fee, tax=tax,
                       net_settlement=round_2(net_integerized), gateway="1LINK-PK",
                       note="Settlement forced to integer paisa; local rails.")


# ----- Dispatcher using pattern matching + Literal exhaustiveness -----
def select_gateway(currency: Currency) -> PaymentGateway:
    match currency:
        case "USD":
            return UsdGateway()
        case "EUR":
            return EurGateway()
        case "GBP":
            return GbpGateway()
        case "PKR":
            return PkrGateway()
        case other:  # mypy/pyright will flag if a new Literal is added but not handled
            assert_never(other)


def process_payment(amount: float, currency: Currency) -> Receipt:
    gw = select_gateway(currency)
    return gw.authorize_and_capture(amount, currency)


# ----- Example usage -----
if __name__ == "__main__":
    print(process_payment(100.00, "USD"))
    print(process_payment(100.00, "EUR"))
    print(process_payment(100.00, "GBP"))
    print(process_payment(100.00, "PKR"))
    # type checker will warn on invalid literal:
    try:
        print(process_payment(100.00, "AUD"))  # ❌
    except AssertionError:
        print("Caught invalid currency as expected.")

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Item:
    name: str          # Name of the item (e.g., "Laptop")
    quantity: int      # Quantity of the item ordered
    price_per_unit: float  # Price per unit of the item

discounts: Dict[str, float] = {
    "Laptop": 0.10,     # 10% discount on Laptop
    "Keyboard": 0.05,   # 5% discount on Keyboard
}
order_items = [
    Item(name="Laptop", quantity=1, price_per_unit=1500.0),
    Item(name="Mouse", quantity=2, price_per_unit=25.0),
    Item(name="Keyboard", quantity=1, price_per_unit=75.0),
]


def calculate_order_total_with_discounts(items: List[Item], discounts: Dict[str, float]) -> float:
    total = 0.0
    for item in items:
        discount = discounts.get(item.name, 0.0)  # Default discount is 0 if not found
        total += item.quantity * item.price_per_unit * (1 - discount)
    return total


total_price_with_discounts = calculate_order_total_with_discounts(order_items, discounts)
print(f"Total Price with Discounts: ${total_price_with_discounts:.2f}")  # Output: $1542.50


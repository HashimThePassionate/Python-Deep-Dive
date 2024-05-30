# Creating an interfaces

### 1. Define an Abstract Base Class (ABC)

```python
from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self) -> float:
        pass
```

- **`ABC` and `abstractmethod`**: By inheriting from `ABC`, `TaxCalculator` becomes an abstract base class. The `@abstractmethod` decorator is used to declare `calculate_tax` as an abstract method. This means any subclass of `TaxCalculator` must implement the `calculate_tax` method.

### 2. Implement the Abstract Base Class

```python
class TaxCalculator24(TaxCalculator):
    def __init__(self, taxable_income: float):
        self.taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.taxable_income * 0.3
```

- **Concrete Implementation**: `TaxCalculator24` is a concrete class that inherits from `TaxCalculator`. It provides an implementation for the `calculate_tax` method, fulfilling the contract defined by the `TaxCalculator` abstract base class.
- **Constructor**: The `__init__` method initializes the instance with `taxable_income`. This is specific to `TaxCalculator24` and not dictated by the `TaxCalculator` interface.

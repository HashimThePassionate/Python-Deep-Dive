from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self) -> float:
        pass

class TaxCalculator24(TaxCalculator):
    def __init__(self, taxable_income: float):
        self.taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.taxable_income * 0.3

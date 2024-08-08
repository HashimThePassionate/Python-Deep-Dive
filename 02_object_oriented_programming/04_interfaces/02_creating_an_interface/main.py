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

class TaxReport:
    def __init__(self, calculator: TaxCalculator):
        self.calculator = calculator

    def show(self):
        tax = self.calculator.calculate_tax()
        print(f"The calculated tax is: {tax}")

# Example usage:
taxable_income = 1000000
calculator = TaxCalculator24(taxable_income)
report = TaxReport(calculator)
report.show()

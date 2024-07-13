from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self) -> float:
        pass

class TaxCalculator24(TaxCalculator):
    def __init__(self, taxable_income: float):
        self.__taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.__taxable_income * 0.3

class TaxReport:
    def __init__(self, calculator: TaxCalculator24):
        self.__calculator = calculator

    def show(self):
        tax = self.__calculator.calculate_tax()
        print(tax)

# Example usage
if __name__ == "__main__":
    calculator = TaxCalculator24(100000)
    report = TaxReport(calculator)
    report.show()

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

class TaxCalculator23(TaxCalculator):
    def calculate_tax(self) -> float:
        return 0.0

class TaxReport:
    def __init__(self):
        self.__calculator = None

    def show(self, calculator: TaxCalculator):
        tax = calculator.calculate_tax()
        print(tax)

calculator = TaxCalculator24(100000)
report = TaxReport()
report.show(calculator)
report.show(TaxCalculator23())

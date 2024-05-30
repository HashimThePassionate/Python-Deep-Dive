class TaxCalculator:
    def __init__(self, taxable_income: float):
        self.__taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.__taxable_income * 0.3

class TaxReport:
    def __init__(self):
        self.__calculator = TaxCalculator(1000000)

    def show(self):
        tax = self.__calculator.calculate_tax()
        print(tax)

# Create an instance of TaxReport and show the tax
report = TaxReport()
report.show()

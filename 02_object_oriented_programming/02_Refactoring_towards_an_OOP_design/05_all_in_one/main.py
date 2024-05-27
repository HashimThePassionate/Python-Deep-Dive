import math
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class Console:
    @staticmethod
    def read_number(prompt, min_value=None, max_value=None):
        while True:
            try:
                value = float(input(prompt))
                if min_value is not None and max_value is not None:
                    if min_value <= value <= max_value:
                        return value
                    else:
                        print(f"Enter a value between {
                              min_value} and {max_value}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a numeric value.")


class MortgageCalculator:
    MONTHS_IN_YEAR = 12
    PERCENT = 100

    def __init__(self, principal, annual_interest, years):
        self.principal = principal
        self.annual_interest = annual_interest
        self.years = years

    def calculate_balance(self, number_of_payments_made):
        monthly_interest = self.get_monthly_interest()
        number_of_payments = self.get_number_of_payments()

        balance = (self.principal *
                   (math.pow(1 + monthly_interest, number_of_payments) -
                    math.pow(1 + monthly_interest, number_of_payments_made)) /
                   (math.pow(1 + monthly_interest, number_of_payments) - 1))

        return balance

    def calculate_mortgage(self):
        monthly_interest = self.get_monthly_interest()
        number_of_payments = self.get_number_of_payments()

        mortgage = (self.principal *
                    (monthly_interest * math.pow(1 + monthly_interest, number_of_payments)) /
                    (math.pow(1 + monthly_interest, number_of_payments) - 1))

        return mortgage

    def get_remaining_balances(self):
        balances = []
        number_of_payments = self.get_number_of_payments()
        for month in range(1, number_of_payments + 1):
            balances.append(self.calculate_balance(month))
        return balances

    def get_monthly_interest(self):
        return self.annual_interest / self.PERCENT / self.MONTHS_IN_YEAR

    def get_number_of_payments(self):
        return self.years * self.MONTHS_IN_YEAR


class MortgageReport:
    def __init__(self, calculator):
        self.calculator = calculator
        self.currency = locale.currency

    def print_payment_schedule(self):
        print("\nPAYMENT SCHEDULE")
        print("----------------")
        for balance in self.calculator.get_remaining_balances():
            print(self.currency(balance))

    def print_mortgage(self):
        mortgage = self.calculator.calculate_mortgage()
        mortgage_formatted = self.currency(mortgage, grouping=True)
        print("\nMORTGAGE")
        print("--------")
        print("Monthly Payments:", mortgage_formatted)


def main():
    # Set locale for currency formatting
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    principal = int(Console.read_number("Principal: ", 1000, 1_000_000))
    annual_interest = float(Console.read_number(
        "Annual Interest Rate: ", 1, 30))
    years = int(Console.read_number("Period (Years): ", 1, 30))

    calculator = MortgageCalculator(principal, annual_interest, years)

    report = MortgageReport(calculator)
    report.print_mortgage()
    report.print_payment_schedule()


main()

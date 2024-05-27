import locale


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
        

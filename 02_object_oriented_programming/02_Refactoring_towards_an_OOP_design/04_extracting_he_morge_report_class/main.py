import math

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

# Example usage
# calculator = MortgageCalculator(100000, 5, 30)
# print(calculator.calculate_mortgage())
# print(calculator.get_remaining_balances())

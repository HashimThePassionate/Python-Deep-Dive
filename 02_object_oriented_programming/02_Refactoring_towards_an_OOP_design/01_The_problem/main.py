import math
import locale

locale.setlocale(locale.LC_ALL, '')

MONTHS_IN_YEAR = 12
PERCENT = 100.0  # Convert to float

def main():
    principal = read_number("Principal: ", 1000, 1_000_000)
    annual_interest = read_number("Annual Interest Rate: ", 1, 30)
    years = read_number("Period (Years): ", 1, 30)

    print_mortgage(principal, annual_interest, years)
    print_payment_schedule(principal, annual_interest, years)

def print_mortgage(principal, annual_interest, years):
    mortgage = calculate_mortgage(principal, annual_interest, years)
    mortgage_formatted = locale.currency(mortgage, grouping=True)
    print("\nMORTGAGE")
    print("--------")
    print("Monthly Payments:", mortgage_formatted)

def print_payment_schedule(principal, annual_interest, years):
    print("\nPAYMENT SCHEDULE")
    print("----------------")
    for month in range(1, int(years * MONTHS_IN_YEAR) + 1):  # Convert years to int
        balance = calculate_balance(principal, annual_interest, years, month)
        balance_formatted = locale.currency(balance, grouping=True)
        print(balance_formatted)

def read_number(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Enter a value between {min_value} and {max_value}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_balance(principal, annual_interest, years, number_of_payments_made):
    monthly_interest = annual_interest / PERCENT / MONTHS_IN_YEAR
    number_of_payments = years * MONTHS_IN_YEAR

    balance = principal * ((1 + monthly_interest) ** number_of_payments - (1 + monthly_interest) ** number_of_payments_made) / ((1 + monthly_interest) ** number_of_payments - 1)
    return balance

def calculate_mortgage(principal, annual_interest, years):
    monthly_interest = annual_interest / PERCENT / MONTHS_IN_YEAR
    number_of_payments = years * MONTHS_IN_YEAR

    mortgage = principal * (monthly_interest * (1 + monthly_interest) ** number_of_payments) / ((1 + monthly_interest) ** number_of_payments - 1)
    return mortgage

if __name__ == "__main__":
    main()

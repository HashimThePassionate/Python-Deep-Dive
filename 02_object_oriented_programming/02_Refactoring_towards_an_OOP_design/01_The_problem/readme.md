# The Problem

```python
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
```

Explanation:

1. `import math`: Imports the math module, which provides mathematical functions.

2. `import locale`: Imports the locale module, which allows for locale-specific formatting.

3. `locale.setlocale(locale.LC_ALL, '')`: Sets the locale to the user's default settings, enabling locale-specific formatting such as currency.

4. `MONTHS_IN_YEAR = 12`: Defines a constant representing the number of months in a year.

5. `PERCENT = 100.0`: Defines a constant representing 100.0 as a float. This is used for converting percentages to decimal values.

6. `def main():`: Defines the main function where the program execution starts.

7. `principal = read_number("Principal: ", 1000, 1_000_000)`: Prompts the user to input the principal amount, ensuring it falls within the range of 1000 to 1,000,000.

8. `annual_interest = read_number("Annual Interest Rate: ", 1, 30)`: Prompts the user to input the annual interest rate, ensuring it falls within the range of 1 to 30.

9. `years = read_number("Period (Years): ", 1, 30)`: Prompts the user to input the loan period in years, ensuring it falls within the range of 1 to 30.

10. `print_mortgage(principal, annual_interest, years)`: Calls the `print_mortgage` function to calculate and print the mortgage details.

11. `print_payment_schedule(principal, annual_interest, years)`: Calls the `print_payment_schedule` function to print the payment schedule.

12. `def print_mortgage(principal, annual_interest, years):`: Defines a function to calculate and print mortgage details based on principal, annual interest rate, and loan period.

13. `def print_payment_schedule(principal, annual_interest, years):`: Defines a function to print the payment schedule based on principal, annual interest rate, and loan period.

14. `def read_number(prompt, min_value, max_value):`: Defines a function to read a number from the user, displaying a prompt and ensuring the input falls within a specified range.

15. `def calculate_balance(principal, annual_interest, years, number_of_payments_made):`: Defines a function to calculate the remaining balance of the loan after a certain number of payments.

16. `def calculate_mortgage(principal, annual_interest, years):`: Defines a function to calculate the monthly mortgage payment based on principal, annual interest rate, and loan period.

17. `if __name__ == "__main__":`: Checks if the script is being run directly (not imported as a module).

18. `main()`: Calls the main function to start the program execution.
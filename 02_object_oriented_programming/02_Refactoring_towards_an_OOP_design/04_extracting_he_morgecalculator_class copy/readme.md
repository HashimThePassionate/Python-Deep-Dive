This code defines a `MortgageCalculator` class responsible for calculating mortgage-related values such as monthly payments and remaining balances. Let's break down the code and its functionalities:

### Importing the `math` Module

```python
import math
```

- **`import math`**: This statement imports the `math` module, which provides mathematical functions and constants.

### Class Definition: `MortgageCalculator`

```python
class MortgageCalculator:
```

- **`class MortgageCalculator:`**: This defines a class named `MortgageCalculator` for performing mortgage calculations.

### Class Constants

```python
    MONTHS_IN_YEAR = 12
    PERCENT = 100
```

- **`MONTHS_IN_YEAR = 12`**: This class constant represents the number of months in a year.
- **`PERCENT = 100`**: This class constant represents the value of 100, used for percentage calculations.

### Constructor Method: `__init__()`

```python
    def __init__(self, principal, annual_interest, years):
        self.principal = principal
        self.annual_interest = annual_interest
        self.years = years
```

- **`def __init__(self, principal, annual_interest, years):`**: This is the constructor method of the `MortgageCalculator` class. It initializes instances of the class with three parameters:
  - `principal`: The principal loan amount.
  - `annual_interest`: The annual interest rate.
  - `years`: The duration of the mortgage in years.

### Method: `calculate_balance()`

```python
    def calculate_balance(self, number_of_payments_made):
        monthly_interest = self.get_monthly_interest()
        number_of_payments = self.get_number_of_payments()

        balance = (self.principal * 
                   (math.pow(1 + monthly_interest, number_of_payments) - 
                    math.pow(1 + monthly_interest, number_of_payments_made)) /
                   (math.pow(1 + monthly_interest, number_of_payments) - 1))

        return balance
```

- **`def calculate_balance(self, number_of_payments_made):`**: This method calculates the remaining balance on the mortgage after a certain number of payments.
  - **`monthly_interest = self.get_monthly_interest()`**: This calculates the monthly interest rate.
  - **`number_of_payments = self.get_number_of_payments()`**: This calculates the total number of payments over the life of the mortgage.
  - **`balance = ...`**: This formula calculates the remaining balance based on the number of payments made.

### Method: `calculate_mortgage()`

```python
    def calculate_mortgage(self):
        monthly_interest = self.get_monthly_interest()
        number_of_payments = self.get_number_of_payments()

        mortgage = (self.principal * 
                    (monthly_interest * math.pow(1 + monthly_interest, number_of_payments)) / 
                    (math.pow(1 + monthly_interest, number_of_payments) - 1))

        return mortgage
```

- **`def calculate_mortgage(self):`**: This method calculates the monthly mortgage payment.
  - **`monthly_interest = self.get_monthly_interest()`**: This calculates the monthly interest rate.
  - **`number_of_payments = self.get_number_of_payments()`**: This calculates the total number of payments over the life of the mortgage.
  - **`mortgage = ...`**: This formula calculates the monthly mortgage payment.

### Method: `get_remaining_balances()`

```python
    def get_remaining_balances(self):
        balances = []
        number_of_payments = self.get_number_of_payments()
        for month in range(1, number_of_payments + 1):
            balances.append(self.calculate_balance(month))
        return balances
```

- **`def get_remaining_balances(self):`**: This method calculates and returns the remaining balances on the mortgage for each month.
  - **`balances = []`**: This initializes an empty list to store the balances.
  - **`number_of_payments = self.get_number_of_payments()`**: This calculates the total number of payments over the life of the mortgage.
  - **`for month in range(1, number_of_payments + 1):`**: This iterates over each month of payments.
    - **`balances.append(self.calculate_balance(month))`**: This calculates the balance for each month and appends it to the `balances` list.
  - **`return balances`**: This returns the list of remaining balances.

### Helper Methods: `get_monthly_interest()` and `get_number_of_payments()`

```python
    def get_monthly_interest(self):
        return self.annual_interest / self.PERCENT / self.MONTHS_IN_YEAR

    def get_number_of_payments(self):
        return self.years * self.MONTHS_IN_YEAR
```

- **`def get_monthly_interest(self):`**: This method calculates and returns the monthly interest rate.
- **`def get_number_of_payments(self):`**: This method calculates and returns the total number of payments over the life of the mortgage.

### Summary

The `MortgageCalculator` class encapsulates methods for calculating mortgage-related values such as monthly payments and remaining balances. It provides flexibility for calculating different aspects of a mortgage and allows for easy extension and reuse. The class makes use of class constants and helper methods to perform calculations efficiently.
# Employee Class

This Python script defines an `Employee` class to manage employee-related data and operations.

## Overview

The `Employee` class provides functionality to manage employee details such as base salary, hourly rate, and calculating wages.

## Complete Code
```python
class Employee:
    number_of_employees = 0  # Class variable to keep track of the number of employees

    def __init__(self, base_salary, hourly_rate=None):
        """
        Constructor method to initialize an Employee object.

        Parameters:
        - base_salary: Base salary of the employee.
        - hourly_rate: Hourly rate for extra hours worked (default is None).
        """
        self.__set_base_salary(base_salary)  # Set base salary using a private method
        if hourly_rate is None:
            self.hourly_rate = 0  # If hourly_rate is not provided, set it to 0
        else:
            self.__set_hourly_rate(hourly_rate)  # Set hourly rate using a private method
        Employee.number_of_employees += 1  # Increment the number of employees

    @staticmethod
    def print_number_of_employees():
        """Static method to print the total number of employees."""
        print(f'Number of Employees is {Employee.number_of_employees}')

    def calculate_wage(self, extra_hours=0):
        """
        Method to calculate the wage of the employee.

        Parameters:
        - extra_hours: Number of extra hours worked (default is 0).

        Returns:
        - Total wage of the employee.
        """
        return self.base_salary + (self.hourly_rate * extra_hours)

    def __set_base_salary(self, base_salary):
        """
        Private method to set the base salary of the employee.

        Parameters:
        - base_salary: Base salary of the employee.
        """
        if base_salary < 0:
            raise ValueError("Salary cannot be less than 0.")
        self.base_salary = base_salary

    def __set_hourly_rate(self, hourly_rate):
        """
        Private method to set the hourly rate of the employee.

        Parameters:
        - hourly_rate: Hourly rate for extra hours worked.
        """
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.hourly_rate = hourly_rate


# Creating employee objects
employee1 = Employee(10000)
employee2 = Employee(50000, 20)

# Calculating wages for each employee
wage1 = employee1.calculate_wage()
wage2 = employee2.calculate_wage()

# Printing wages
print(wage1)
print(wage2)

# Printing the total number of employees
Employee.print_number_of_employees()
```

## Code Explanation

### Class Definition

```python
class Employee:
    number_of_employees = 0

    def __init__(self, base_salary, hourly_rate=None):
        self.__set_base_salary(base_salary)
        if hourly_rate is None:
            self.hourly_rate = 0
        else:
            self.__set_hourly_rate(hourly_rate)
        Employee.number_of_employees += 1
```

- `number_of_employees`: Class attribute to keep track of the total number of employees. Initialized to 0.
- `__init__`: Constructor method to initialize instance variables. It takes `base_salary` as a required argument and `hourly_rate` as an optional argument.

### Static Method

```python
    @staticmethod
    def print_number_of_employees():
        print(f'Number of Employees is {Employee.number_of_employees}')
```
-   Why we use Static Members?
-   We represent a concept that should be in a single place. The number of employees.
-   This concept does not belong to any individual employee
- `print_number_of_employees()`: Static method to print the total number of employees.

### Instance Methods

```python
    def calculate_wage(self, extra_hours=0):
        return self.base_salary + (self.hourly_rate * extra_hours)

    def __set_base_salary(self, base_salary):
        if base_salary < 0:
            raise ValueError("Salary cannot be less than 0.")
        self.base_salary = base_salary

    def __set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.hourly_rate = hourly_rate
```

- `calculate_wage`: Instance method to calculate the total wage based on the base salary and extra hours worked.
- `__set_base_salary` and `__set_hourly_rate`: Private methods used to set the base salary and hourly rate respectively, with validation for non-negative values.

### Main Block

```python
    employee1 = Employee(10000)
    employee2 = Employee(50000, 20)
    wage1 = employee1.calculate_wage()
    wage2 = employee2.calculate_wage()
    print(wage1)
    print(wage2)
    Employee.print_number_of_employees()
```

- The main block creates two `Employee` instances, calculates their wages, and prints the results along with the total number of employees.

## Usage

To use the `Employee` class, simply create instances of it with appropriate parameters and call its methods as demonstrated in the main block.

```python
employee1 = Employee(10000)
employee2 = Employee(50000, 20)
wage1 = employee1.calculate_wage()
wage2 = employee2.calculate_wage()
print(wage1)
print(wage2)
Employee.print_number_of_employees()
```

```plaintext
Output:
10000
51000
Number of Employees is 2
```

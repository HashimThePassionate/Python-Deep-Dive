# Getter and Setter Example in Python

## Introduction
This Python code demonstrates the implementation of getter and setter methods in a class called `Employee`. Getter and setter methods are used to encapsulate access to class attributes and ensure controlled access to them.

## Class Definition

```python
class Employee:
    def __init__(self, salary, hours):
        self.__salary = salary
        self.__hours = hours

    def calculate_wage(self, extra_hours):
        return f"The Calculated Wage is {self.__salary * self.__hours + 50 * extra_hours}"

    def set_base_salary(self, s):
        if s <= 0:
            raise ValueError("Salary must be greater than 0")
        self.__salary = s

    def get_base_salary(self):
        return self.__salary
    
    def set_hourly_rate(self, h):
        if h <0:
            raise ValueError("Hourly rate cannot be negative")
        self.__hours = h
    
    def get_hourly_rate(self):
        return self.__hours

e = Employee(10000,20)
print(e.calculate_wage(10))
print(e.__salary)

```

## Explanation

- **Class Definition (`Employee`):**
  - The `Employee` class is defined with two private attributes: `_base_salary` and `_hourly_rate`, both initialized to 0 in the constructor (`__init__` method).
  - It contains methods for calculating wages (`calculate_wage()`), setting base salary (`set_base_salary()`), getting base salary (`get_base_salary()`), getting hourly rate (`get_hourly_rate()`), and setting hourly rate (`set_hourly_rate()`).

- **Getter and Setter Methods:**
  - Getter methods (`get_base_salary()` and `get_hourly_rate()`) are used to access the values of private attributes (`_base_salary` and `_hourly_rate`) from outside the class.
  - Setter methods (`set_base_salary()` and `set_hourly_rate()`) are used to set the values of private attributes with validation checks.

- **Encapsulation:**
  - Encapsulation is maintained by making the attributes `_base_salary` and `_hourly_rate` private (by prefixing them with an underscore `_`). This restricts direct access to these attributes from outside the class and ensures controlled access through getter and setter methods.

## Usage
To use this code, follow these steps:
1. Create an instance of the `Employee` class.
2. Set the base salary and hourly rate using the setter methods (`set_base_salary()` and `set_hourly_rate()`).
3. Retrieve the base salary and hourly rate using the getter methods (`get_base_salary()` and `get_hourly_rate()`).
4. Calculate the wage using the `calculate_wage()` method.

## Example Output
For the given example:
- Base salary is set to $50,000 using the `set_base_salary()` method.
- Hourly rate is set to $20 using the `set_hourly_rate()` method.
- The base salary is retrieved using the `get_base_salary()` method.
- The hourly rate is retrieved using the `get_hourly_rate()` method.
- Wage is calculated for 10 extra hours using the `calculate_wage()` method.

## Conclusion
This code demonstrates the implementation of getter and setter methods in Python to ensure controlled access to class attributes, thus maintaining encapsulation.

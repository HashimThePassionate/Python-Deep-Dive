# Employee Wage Calculation

## Introduction
This Python code defines a class called `Employee` to manage employee data and calculate wages based on base salary and hourly rate.

## Class Definition

```python
class Employee:
    def __init__(self):
        self.base_salary = 0
        self.hourly_rate = 0
        
    def calculate_wage(self, extra_hours):
        return self.base_salary + (self.hourly_rate * extra_hours)
```

## Explanation

- **Class Definition (`Employee`):**
  - The `Employee` class is defined with two attributes: `base_salary` and `hourly_rate`, both initialized to 0 in the constructor (`__init__` method).
  - It also contains a method `calculate_wage()` to calculate the total wage based on the base salary and hourly rate, taking extra hours as input.

- **Encapsulation:**
  - Encapsulation is the bundling of data (attributes) and methods that operate on the data within a single unit, called a class.
  - In this code:
    - Data encapsulation is achieved by defining attributes (`base_salary` and `hourly_rate`) within the class `Employee`. These attributes are accessible only through the class's methods.
    - Method encapsulation is evident in the `calculate_wage()` method, which encapsulates the logic for calculating the total wage.

- **Initialization and Calculation:**
  - An instance of the `Employee` class is created.
  - Base salary and hourly rate are set for the employee instance.
  - The `calculate_wage()` method is called with the parameter `20` representing extra hours worked.
  - The calculated wage is printed.

## Usage
To use this code, follow these steps:
1. Create an instance of the `Employee` class.
2. Set the `base_salary` and `hourly_rate` attributes for the employee.
3. Call the `calculate_wage()` method with the number of extra hours worked as an argument.
4. The method will return the calculated wage.

## Example Output
For the given example:
- Base salary: $50,000
- Hourly rate: $20
- Extra hours worked: 20
The calculated wage is printed.

## Conclusion
This code demonstrates the use of encapsulation in Python classes to manage employee data and calculate wages.
# 👔 Static Methods and Class Variable

This Python script defines an `Employee` class to manage employee-related data and operations, including tracking the total number of employees and calculating wages based on base salary and extra hours worked.

---

## 📑 Table of Contents

- [👔 Static Methods and Class Variable](#-static-methods-and-class-variable)
  - [📑 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [⚙️ Complete Code](#️-complete-code)
  - [📝 Code Explanation](#-code-explanation)
    - [🏗️ Class Definition](#️-class-definition)
    - [📊 Static Method](#-static-method)
    - [🧮 Instance Methods](#-instance-methods)
    - [🔄 Main Block](#-main-block)
  - [💡 Usage](#-usage)
  - [📜 Example Output](#-example-output)

---

## 🔍 Overview

The `Employee` class models an employee with attributes for **base salary** and **hourly rate** and includes methods for calculating wages. A class attribute keeps track of the total number of employees, and a static method displays this information.

---

## ⚙️ Complete Code

```python
class Employee:
    number_of_employees = 0  # Class variable to keep track of the number of employees

    def __init__(self, base_salary, hourly_rate=None):
        self.__set_base_salary(base_salary)  # Set base salary using a private method
        if hourly_rate is None:
            self.hourly_rate = 0  # Default hourly rate if not provided
        else:
            self.__set_hourly_rate(hourly_rate)  # Set hourly rate with validation
        Employee.number_of_employees += 1  # Increment employee count

    @staticmethod
    def print_number_of_employees():
        """Static method to print the total number of employees."""
        print(f'Number of Employees is {Employee.number_of_employees}')

    def calculate_wage(self, extra_hours=0):
        """Calculate the wage based on base salary and extra hours."""
        return self.base_salary + (self.hourly_rate * extra_hours)

    def __set_base_salary(self, base_salary):
        """Private method to set the base salary with validation."""
        if base_salary < 0:
            raise ValueError("Salary cannot be less than 0.")
        self.base_salary = base_salary

    def __set_hourly_rate(self, hourly_rate):
        """Private method to set the hourly rate with validation."""
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.hourly_rate = hourly_rate


# Creating employee objects
employee1 = Employee(10000)
employee2 = Employee(50000, 20)

# Calculating wages
wage1 = employee1.calculate_wage()
wage2 = employee2.calculate_wage()

# Printing wages and total number of employees
print(wage1)
print(wage2)
Employee.print_number_of_employees()
```

---

## 📝 Code Explanation

### 🏗️ Class Definition

```python
class Employee:
    number_of_employees = 0
```

- **`number_of_employees`**: A class attribute that tracks the total number of employees.

```python
def __init__(self, base_salary, hourly_rate=None):
    self.__set_base_salary(base_salary)
    if hourly_rate is None:
        self.hourly_rate = 0
    else:
        self.__set_hourly_rate(hourly_rate)
    Employee.number_of_employees += 1
```

- **`__init__`**: Constructor initializes `base_salary` and `hourly_rate` (default is 0). Each time an `Employee` is created, `number_of_employees` is incremented.

### 📊 Static Method

```python
@staticmethod
def print_number_of_employees():
    print(f'Number of Employees is {Employee.number_of_employees}')
```

- **Purpose**: This static method prints the total number of employees, as `number_of_employees` applies to the class itself rather than individual instances.

### 🧮 Instance Methods

```python
def calculate_wage(self, extra_hours=0):
    return self.base_salary + (self.hourly_rate * extra_hours)
```

- **`calculate_wage`**: Calculates the total wage based on the base salary and extra hours.

```python
def __set_base_salary(self, base_salary):
    if base_salary < 0:
        raise ValueError("Salary cannot be less than 0.")
    self.base_salary = base_salary
```

- **`__set_base_salary`**: A private method to set `base_salary` with validation to ensure it's non-negative.

```python
def __set_hourly_rate(self, hourly_rate):
    if hourly_rate < 0:
        raise ValueError("Hourly rate cannot be negative.")
    self.hourly_rate = hourly_rate
```

- **`__set_hourly_rate`**: A private method to set `hourly_rate` with validation to ensure it's non-negative.

### 🔄 Main Block

```python
employee1 = Employee(10000)
employee2 = Employee(50000, 20)
wage1 = employee1.calculate_wage()
wage2 = employee2.calculate_wage()
print(wage1)
print(wage2)
Employee.print_number_of_employees()
```

- **Creates Instances**: `Employee` objects are created with base salary, and optionally with hourly rate.
- **Calculates Wages**: Calls `calculate_wage` to compute wages based on hours.
- **Prints Total Employees**: Displays the total count of employees.

---

## 💡 Usage

To use the `Employee` class, create instances with `base_salary` and optionally `hourly_rate`. Call `calculate_wage` to calculate wages and `print_number_of_employees` to display the total employee count.

```python
employee1 = Employee(10000)
employee2 = Employee(50000, 20)
wage1 = employee1.calculate_wage()
wage2 = employee2.calculate_wage()
print(wage1)
print(wage2)
Employee.print_number_of_employees()
```

---

## 📜 Example Output

```plaintext
10000
51000
Number of Employees is 2
```

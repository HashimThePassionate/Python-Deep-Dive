# 👔 Constructor Overloading

This example demonstrates how to achieve **constructor overloading** in Python using **default parameters** and **conditional logic**. The `Employee` class allows flexible initialization by making the `hourly_rate` parameter optional, ensuring both simplicity and functionality.

---

## 📑 Table of Contents

- [👔 Constructor Overloading](#-constructor-overloading)
  - [📑 Table of Contents](#-table-of-contents)
    - [🔍 Overview](#-overview)
  - [⚙️ Complete Code](#️-complete-code)
    - [📝 Key Components Explained](#-key-components-explained)
      - [🏗️ Constructor with Default Parameters](#️-constructor-with-default-parameters)
      - [🔧 Handling Default Values](#-handling-default-values)
      - [🔒 Encapsulation with Getters and Setters](#-encapsulation-with-getters-and-setters)
    - [💡 Example Usage](#-example-usage)
    - [📜 Summary](#-summary)

---

### 🔍 Overview

The `Employee` class models an employee with attributes for **base salary** and **hourly rate**. By making `hourly_rate` optional, we can create instances with just a base salary, or both a base salary and hourly rate. This is a convenient way to handle cases where hourly rate information may not always be provided.

---

## ⚙️ Complete Code

```python
class Employee:
    def __init__(self, base_salary, hourly_rate=None):
        self.__set_base_salary(base_salary)
        if hourly_rate is None:
            self.hourly_rate = 0
        else:
            self.__set_hourly_rate(hourly_rate)

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

---

### 📝 Key Components Explained

#### 🏗️ Constructor with Default Parameters

```python
def __init__(self, base_salary, hourly_rate=None):
```

- **Parameters**: `base_salary` (required) and `hourly_rate` (optional, defaults to `None`).
- **Purpose**: Allows flexible instance creation by enabling initialization with just `base_salary` or both `base_salary` and `hourly_rate`.

#### 🔧 Handling Default Values

```python
if hourly_rate is None:
    self.hourly_rate = 0
else:
    self.__set_hourly_rate(hourly_rate)
```

- **Default Behavior**: When `hourly_rate` is not provided, it defaults to `0`.
- **Data Validation**: Both `base_salary` and `hourly_rate` are assigned through private methods to ensure valid input values.

#### 🔒 Encapsulation with Getters and Setters

```python
def __set_base_salary(self, base_salary):
    if base_salary < 0:
        raise ValueError("Salary cannot be less than 0.")
    self.base_salary = base_salary

def __set_hourly_rate(self, hourly_rate):
    if hourly_rate < 0:
        raise ValueError("Hourly rate cannot be negative.")
    self.hourly_rate = hourly_rate
```

- **Purpose**: Enforces data integrity for `base_salary` and `hourly_rate` by validating values before assignment.
- **Encapsulation**: These attributes are made private, ensuring they are modified only through controlled methods within the class.

---

### 💡 Example Usage

```python
# Creating an Employee instance with only base_salary
employee1 = Employee(10000)
# Creating an Employee instance with both base_salary and hourly_rate
employee2 = Employee(50000, 20)

# Calculating wages
wage1 = employee1.calculate_wage()      # Wage with default extra hours (0)
wage2 = employee2.calculate_wage(10)    # Wage with 10 extra hours

# Printing results
print(wage1)   # Output: 10000
print(wage2)   # Output: 52000
```

---

### 📜 Summary

This `Employee` class demonstrates a way to **simulate constructor overloading** in Python by using default parameters and conditional logic:

- **Optional Parameters**: Allows creating instances with either only `base_salary` or both `base_salary` and `hourly_rate`.
- **Encapsulation**: Uses private methods to validate and control access to key attributes.
- **Default Handling**: Sets `hourly_rate` to `0` by default, making the class adaptable to various requirements.


# 👔 Employee Class

This Python `Employee` class models an employee's base salary and hourly rate, allowing for the calculation of total wages based on additional hours worked.

---

## 📑 Table of Contents

- [👔 Employee Class](#-employee-class)
  - [📑 Table of Contents](#-table-of-contents)
    - [🔍 Overview](#-overview)
    - [⚙️ Class Definition](#️-class-definition)
      - [Constructor (`__init__`)](#constructor-__init__)
      - [`calculate_wage` Method](#calculate_wage-method)
      - [Private Setter Methods](#private-setter-methods)
      - [Getter Methods](#getter-methods)
    - [💡 Usage](#-usage)
    - [📜 Example Output](#-example-output)
    - [📝 Notes](#-notes)
  - [Code example](#code-example)

---

### 🔍 Overview

The `Employee` class represents an employee with attributes for **base salary** and **hourly rate**. It calculates the wage by combining the base salary and additional earnings from extra hours worked.

---

### ⚙️ Class Definition

#### Constructor (`__init__`)

- **Parameters**: `base_salary`, `hourly_rate`
- **Purpose**: Initializes an `Employee` object with validated `base_salary` and `hourly_rate` values.
- **Private Attributes**:
  - `__base_salary`: Stores the employee’s base salary.
  - `__hourly_rate`: Stores the employee’s hourly rate.

#### `calculate_wage` Method

- **Parameters**: `extra_hours`
- **Return**: Total wage calculated as `base_salary + (hourly_rate * extra_hours)`.
- **Purpose**: Calculates wages based on base salary and additional hours worked.

#### Private Setter Methods

- **Methods**: `__set_base_salary`, `__set_hourly_rate`
- **Purpose**: Validate and set values for `__base_salary` and `__hourly_rate`. They raise a `ValueError` if invalid values are provided.

#### Getter Methods

- **Methods**: `get_base_salary`, `get_hourly_rate`
- **Purpose**: Allow controlled access to private attributes `__base_salary` and `__hourly_rate`.

---

### 💡 Usage

In the example provided:

1. An `Employee` object is created with a base salary of $50,000 and an hourly rate of $20.
2. The `calculate_wage` method is called with `extra_hours` set to 10.
3. The result is printed.

```python
if __name__ == "__main__":
    employee = Employee(50000, 20)
    wage = employee.calculate_wage(10)
    print(f'Calculate wages: {wage}')
```

---

### 📜 Example Output

```
Calculate wages: 52000
```

---

### 📝 Notes

- **Private Attributes**: Double underscores (`__`) restrict direct access to `__base_salary` and `__hourly_rate` from outside the class.
- **Controlled Access**: Getter methods provide safe access to private attributes.
- **Validation**: Ensures `base_salary` is positive and `hourly_rate` is non-negative, raising a `ValueError` otherwise.
- **Limitations**: The `calculate_wage` method doesn’t handle overtime or additional conditions, focusing solely on extra hours worked at the standard hourly rate.

## Code example
```python 
class Employee:
    def __init__(self, base_salary, hourly_rate):
        self.__set_base_salary(base_salary)
        self.__set_hourly_rate(hourly_rate)

    def calculate_wage(self, extra_hours):
        return self.__base_salary + (self.__hourly_rate * extra_hours)

    def __set_base_salary(self, base_salary):
        if base_salary <= 0:
            raise ValueError("Salary cannot be 0 or less.")
        self.__base_salary = base_salary

    def __set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.__hourly_rate = hourly_rate

    # Getter methods can be public if needed
    def get_base_salary(self):
        return self.__base_salary

    def get_hourly_rate(self):
        return self.__hourly_rate


if __name__ == "__main__":
    employee = Employee(50000, 20)
    wage = employee.calculate_wage(10)
    print(f'Calculate wages: {wage}')
```


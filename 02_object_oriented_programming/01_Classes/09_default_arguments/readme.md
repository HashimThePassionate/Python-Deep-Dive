# 👔 Default Parameter

This `Employee` class demonstrates the use of **default parameters**, **encapsulation**, and a **class variable** to track the number of employees in Python. It models an employee's base salary and hourly rate, allowing for wage calculation based on additional hours.

---

## 📑 Table of Contents

- [👔 Default Parameter](#-default-parameter)
  - [📑 Table of Contents](#-table-of-contents)
    - [🔍 Overview](#-overview)
    - [⚙️ Key Components](#️-key-components)
      - [📊 Class Variable](#-class-variable)
      - [🏗️ Constructor (`__init__`)](#️-constructor-__init__)
      - [💸 `calculate_wage` Method](#-calculate_wage-method)
      - [🧮 Static Method](#-static-method)
      - [🔒 Getter and Setter Methods](#-getter-and-setter-methods)
    - [💡 Example Usage](#-example-usage)
    - [📜 Example Output](#-example-output)
    - [📝 Notes](#-notes)

---

### 🔍 Overview

The `Employee` class models an employee with attributes for **base salary** and **hourly rate**. It provides a method for calculating the total wage based on the base salary and any additional hours worked, with optional parameters and encapsulated data.

---

### ⚙️ Key Components

#### 📊 Class Variable

- **`numberOfEmployees`**: Tracks the total number of employees created across all instances, making it easy to monitor the workforce size.

#### 🏗️ Constructor (`__init__`)

```python
def __init__(self, base_salary, hourly_rate=0):
    self.__set_base_salary(base_salary)
    self.__set_hourly_rate(hourly_rate)
    Employee.numberOfEmployees += 1
```

- **Parameters**:
  - `base_salary`: Mandatory starting salary for each employee.
  - `hourly_rate`: Optional rate per hour (defaults to 0 if not provided).
- **Purpose**: Initializes an employee's salary and hourly rate while incrementing the `numberOfEmployees` counter by 1 for each new employee instance.

#### 💸 `calculate_wage` Method

```python
def calculate_wage(self, extra_hours=0):
    return self.base_salary + (self.hourly_rate * extra_hours)
```

- **Parameters**:
  - `extra_hours`: Optional additional hours worked (defaults to 0).
- **Purpose**: Calculates the wage as `base_salary + (hourly_rate * extra_hours)`, providing flexibility to account for extra hours worked.

#### 🧮 Static Method

```python
@staticmethod
def print_number_of_employees():
    print(Employee.numberOfEmployees)
```

- **Purpose**: A static method that prints the total number of employees, accessible directly via the class without requiring an instance.

#### 🔒 Getter and Setter Methods

- **Purpose**: Encapsulate access to `base_salary` and `hourly_rate` with validation, ensuring values are valid and preventing unintended modifications.

```python
def __set_base_salary(self, base_salary):
    if base_salary <= 0:
        raise ValueError("Salary cannot be 0 or less.")
    self.base_salary = base_salary

def __set_hourly_rate(self, hourly_rate):
    if hourly_rate < 0:
        raise ValueError("Hourly rate cannot be negative.")
    self.hourly_rate = hourly_rate
```

---

### 💡 Example Usage

```python
if __name__ == "__main__":
    employee = Employee(50000, 20)   # Creating an employee with base salary and hourly rate
    Employee.print_number_of_employees()  # Prints the number of employees
    wage = employee.calculate_wage()  # Calculates wage with default extra hours (0)
    print(wage)                       # Outputs the calculated wage
```

---

### 📜 Example Output

```
1
50000
```

---

### 📝 Notes

- **Private Attributes**: Double underscores (`__`) restrict direct access to `base_salary` and `hourly_rate`, enhancing data security.
- **Encapsulation**: Getter and setter methods allow controlled access and modification of salary and hourly rate.
- **Default Parameters**: `hourly_rate` in the constructor and `extra_hours` in `calculate_wage` demonstrate flexibility with default values.
- **Data Validation**: Ensures the base salary is positive and hourly rate is non-negative, raising a `ValueError` otherwise.

---
# 💼 OOP Encapsulation Approach

## 📘 Introduction

This Python code defines a class called `Employee` to manage employee data and calculate wages based on **base salary** and **hourly rate**. It demonstrates how to use encapsulation to keep data and methods organized within a single unit, making code easier to manage and reuse.

---

## 📑 Table of Contents

- [💼 OOP Encapsulation Approach](#-oop-encapsulation-approach)
  - [📘 Introduction](#-introduction)
  - [📑 Table of Contents](#-table-of-contents)
  - [🛠️ Class Definition](#️-class-definition)
  - [📝 Explanation](#-explanation)
    - [🔒 Encapsulation](#-encapsulation)
    - [🚀 Initialization and Calculation](#-initialization-and-calculation)
  - [⚙️ Usage](#️-usage)
  - [💻 Example Output](#-example-output)
  - [📜 Conclusion](#-conclusion)

---

## 🛠️ Class Definition

```python
class Employee:
    def __init__(self):
        self.base_salary = 0
        self.hourly_rate = 0
        
    def calculate_wage(self, extra_hours):
        return self.base_salary + (self.hourly_rate * extra_hours)
```

This `Employee` class encapsulates the data (attributes) and behavior (method) for calculating an employee's wage.

---

## 📝 Explanation

### 🔒 Encapsulation

Encapsulation is the bundling of data and methods within a single unit (class), ensuring better data control and security. 

- **Attributes (`base_salary` and `hourly_rate`)**:
  - Defined within the `Employee` class, these attributes are accessible only through class methods, safeguarding the employee’s data.
  
- **Method (`calculate_wage()`)**:
  - Encapsulates the logic for calculating the total wage, making it easy to use and modify without affecting other parts of the code.

### 🚀 Initialization and Calculation

1. **Instance Creation**: An `Employee` instance is created.
2. **Setting Attributes**: Base salary and hourly rate are set for the employee instance.
3. **Calculating Wage**: The `calculate_wage()` method calculates the total wage based on extra hours worked.
4. **Output**: The calculated wage is printed.

---

## ⚙️ Usage

To use this code, follow these steps:

1. Create an instance of the `Employee` class.
2. Set the `base_salary` and `hourly_rate` attributes for the employee.
3. Call the `calculate_wage()` method with the number of extra hours worked as an argument.
4. The method will return the calculated wage based on the provided extra hours.

---

## 💻 Example Output

For an employee with:
- **Base salary**: $50,000
- **Hourly rate**: $20
- **Extra hours worked**: 20

The calculated wage would be printed as the output.

---

## 📜 Conclusion

This example demonstrates how to use encapsulation in Python classes to manage employee data and calculate wages. By grouping attributes and methods within a single class, code becomes more modular, reusable, and easier to maintain.
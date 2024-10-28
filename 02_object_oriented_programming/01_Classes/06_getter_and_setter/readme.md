# 🔐 Getter and Setter

## 📘 Introduction

This Python code demonstrates the implementation of **getter and setter methods** in a class called `Employee`. These methods help **encapsulate** access to class attributes, ensuring controlled and secure management of data within the class.

---

## 📑 Table of Contents

- [🔐 Getter and Setter](#-getter-and-setter)
  - [📘 Introduction](#-introduction)
  - [📑 Table of Contents](#-table-of-contents)
  - [🛠️ Class Definition](#️-class-definition)
  - [📝 Explanation](#-explanation)
    - [🔑 Getter and Setter Methods](#-getter-and-setter-methods)
    - [🔒 Encapsulation](#-encapsulation)
  - [❓ Why Use Getter and Setter Methods?](#-why-use-getter-and-setter-methods)
  - [⚙️ Usage](#️-usage)
  - [💻 Example Output](#-example-output)
  - [📜 Conclusion](#-conclusion)

---

## 🛠️ Class Definition

```python
class Employee:
    def __init__(self, s, h):
        self.__salary = s
        self.__hours = h

    def calculate_wage(self, extra_hours):
        return f"The Calculated Wage is {self.__salary * self.__hours + 50 * extra_hours}"

    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary cannot be less than or equal to zero")
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_hours(self, hours):
        if hours <= 0:
            raise ValueError("Hours cannot be less than or equal to zero")
        self.__hours = hours

    def get_hours(self):
        return self.__hours


e = Employee(10000, 20)
print(e.calculate_wage(10))
e.set_salary(2000000.124)
e.set_hours(30)
print(e.calculate_wage(10))
try:
    print(e.set_salary(0))
except ValueError as e:
    print("Salary cannot be less than or equal to zero")
```

The `Employee` class uses getter and setter methods to securely manage data, providing validation checks to prevent invalid data.

---

## 📝 Explanation

### 🔑 Getter and Setter Methods

- **Getter Methods**: 
  - `get_salary()` and `get_hours()` allow controlled access to the values of private attributes (`__salary` and `__hours`).
- **Setter Methods**: 
  - `set_salary()` and `set_hours()` enable setting values for private attributes while enforcing validation. 
  - If a value is invalid (e.g., negative or zero), a `ValueError` is raised to prevent assignment.

### 🔒 Encapsulation

Encapsulation is achieved by making the attributes `__salary` and `__hours` private (using double underscores `__`). This:
- **Restricts Direct Access**: Only accessible through getters and setters.
- **Protects Data Integrity**: Validation checks within setter methods ensure only valid data is assigned.

---

## ❓ Why Use Getter and Setter Methods?

Getter and setter methods are used to provide **controlled access** to class attributes, especially when working with **private variables** (like `__salary` and `__hours` in this example). Here’s why they’re essential:

1. **Data Validation**: Setter methods can include validation logic (e.g., ensuring a salary is greater than zero). This prevents invalid or inappropriate values from being assigned.

2. **Encapsulation**: Getters and setters are part of **encapsulation** by keeping attributes private and exposing them only through controlled methods. This reduces the risk of accidental modification from outside the class.

3. **Flexibility for Future Changes**: Using getters and setters allows internal implementation to change without impacting the external interface. For example, if `salary` needs to be modified to a calculated value in the future, we can update the getter or setter without changing other parts of the code.

4. **Consistent Access Pattern**: Using getters and setters provides a standard way to access and modify attributes, which improves code readability and maintains consistency throughout the program.

5. **Enhanced Security**: By restricting direct access to class attributes, we protect the internal state of objects, maintaining data integrity and security.

---

## ⚙️ Usage

To use this code, follow these steps:

1. **Create an Instance**: Initialize the `Employee` class with initial values for salary and hours.
2. **Set Attributes**: Use `set_salary()` and `set_hours()` methods to set valid salary and hour values.
3. **Retrieve Attributes**: Access the current salary and hours using `get_salary()` and `get_hours()` methods.
4. **Calculate Wage**: Call `calculate_wage()` with the number of extra hours to get the total wage.

---

## 💻 Example Output

In the provided example:
- An instance of `Employee` is created with initial values.
- The salary is updated using `set_salary()`, and hours using `set_hours()`.
- Attempting to set an invalid salary triggers an error message.

Sample Output:
```plaintext
The Calculated Wage is 200500
The Calculated Wage is 600050
Salary cannot be less than or equal to zero
```

---

## 📜 Conclusion

This code demonstrates how to use **getter and setter methods** in Python to ensure controlled access to class attributes. By enforcing validation and encapsulating data, this approach promotes secure, maintainable, and flexible code.
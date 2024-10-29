# 🔗 Reducing Coupling in  `Employee` Class Example

This guide shows how **encapsulation** in the `Employee` class helps reduce **coupling**—the dependency between parts of the code. By controlling access to data, encapsulation improves flexibility and maintainability.

---

## 📑 Table of Contents

- [🔗 Reducing Coupling in  `Employee` Class Example](#-reducing-coupling-in--employee-class-example)
  - [📑 Table of Contents](#-table-of-contents)
    - [⚙️ Original Code](#️-original-code)
    - [🔍 How the Code Reduces Coupling](#-how-the-code-reduces-coupling)
      - [🔒 Encapsulation](#-encapsulation)
      - [🔐 Controlled Access](#-controlled-access)
    - [📜 Summary](#-summary)

---

### ⚙️ Original Code

```python
class Employee:
    def __init__(self):
        self._base_salary = 0
        self._hourly_rate = 0

    def calculate_wage(self, extra_hours):
        return self._base_salary + (self._hourly_rate * extra_hours)

    def set_base_salary(self, base_salary):
        if base_salary <= 0:
            raise ValueError("Salary cannot be 0 or less.")
        self._base_salary = base_salary

    def _get_base_salary(self):
        return self._base_salary

    def _get_hourly_rate(self):
        return self._hourly_rate

    def set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self._hourly_rate = hourly_rate
```

---

### 🔍 How the Code Reduces Coupling

#### 🔒 Encapsulation

- **Private Attributes**: `_base_salary` and `_hourly_rate` are private and cannot be accessed directly, so only class methods control them.
- **Single Control Point**: The `Employee` class fully manages its internal state, minimizing outside dependencies and making the class self-contained.

#### 🔐 Controlled Access

- **Setters with Validation**: `set_base_salary` and `set_hourly_rate` validate inputs, ensuring that only valid data is assigned, protecting the object’s state.
- **Getters**: `_get_base_salary` and `_get_hourly_rate` provide a controlled way to access private attributes without exposing details.
- **Loose Coupling**: Methods let external code interact with the class without knowing how attributes are stored or processed, reducing dependency on the class’s internals.

---

### 📜 Summary

Encapsulation in the `Employee` class reduces coupling by:

- Hiding internal data,
- Providing controlled access through methods,
- Making code easier to maintain, test, and extend.


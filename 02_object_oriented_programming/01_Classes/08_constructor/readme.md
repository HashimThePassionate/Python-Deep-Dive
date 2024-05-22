## Employee Class

### Overview
This Python code defines a class `Employee` which represents an employee with a base salary and an hourly rate. It allows for calculating the wage based on the base salary and additional hours worked.

### Class Definition
The `Employee` class has the following methods and attributes:

#### Constructor (`__init__` method)
- **Parameters**: `base_salary`, `hourly_rate`
- **Purpose**: Initializes an `Employee` object with the provided `base_salary` and `hourly_rate`.
- **Private Attributes**:
  - `__base_salary`: Stores the base salary of the employee.
  - `__hourly_rate`: Stores the hourly rate of the employee.

#### `calculate_wage` method
- **Parameters**: `extra_hours`
- **Return**: Calculated wage based on base salary and additional hours worked.
- **Purpose**: Calculates the wage of the employee by adding the base salary to the product of the hourly rate and the additional hours worked.

#### Private Setter Methods (`__set_base_salary` and `__set_hourly_rate`)
- **Parameters**: `base_salary` and `hourly_rate`
- **Purpose**: Sets the base salary and hourly rate of the employee, respectively. These methods are private and are called internally by the constructor to enforce data validation.

#### Getter Methods (`get_base_salary` and `get_hourly_rate`)
- **Return**: The base salary and hourly rate of the employee, respectively.
- **Purpose**: Provides access to the private attributes `__base_salary` and `__hourly_rate` for retrieval purposes.

### Usage
The `if __name__ == "__main__":` block demonstrates the usage of the `Employee` class:
1. An `Employee` object is created with a base salary of $50,000 and an hourly rate of $20.
2. The `calculate_wage` method is called with `extra_hours` set to 10 to calculate the wage for additional hours worked.
3. The calculated wage is printed to the console.

#### Example Output
```
Calculate wages: 52000
```

### Notes
- The attributes `__base_salary` and `__hourly_rate` are prefixed with double underscores, making them private. This restricts direct access to these attributes from outside the class.
- Getter methods (`get_base_salary` and `get_hourly_rate`) are provided for accessing the private attributes in a controlled manner.
- The code includes input validation to ensure that the base salary is greater than zero and the hourly rate is non-negative. If invalid values are provided, `ValueError` exceptions are raised.
- The `calculate_wage` method does not account for overtime pay or any other special conditions. It simply calculates the wage based on the provided hourly rate and additional hours worked.
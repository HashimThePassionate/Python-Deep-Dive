# Default Parameter

1. **Class Definition**:
    ```python
    class Employee:
        numberOfEmployees = 0
    ```
    - This creates a class named `Employee`. 
    - `numberOfEmployees` is a class variable which is initialized to 0. This variable will be used to keep track of the total number of employees.

2. **Constructor Method (`__init__`)**:
    ```python
    def __init__(self, base_salary, hourly_rate=0):
        self.base_salary = base_salary
        self.hourly_rate = hourly_rate
        Employee.numberOfEmployees += 1
    ```
    - This method is called when a new instance of the `Employee` class is created.
    - It takes two parameters: `base_salary` (mandatory) and `hourly_rate` (optional, default value is 0).
    - Inside the constructor, the instance variables `base_salary` and `hourly_rate` are initialized with the provided values.
    - It also increments the `numberOfEmployees` class variable by 1 each time a new employee is created.

3. **Instance Method (`calculate_wage`)**:
    ```python
    def calculate_wage(self, extra_hours=0):
        return self.base_salary + (self.hourly_rate * extra_hours)
    ```
    - This method calculates the wage for the employee.
    - It takes an optional parameter `extra_hours` which defaults to 0.
    - The wage is calculated by adding the base salary to the product of hourly rate and extra hours.

4. **Static Method (`print_number_of_employees`)**:
    ```python
    @staticmethod
    def print_number_of_employees():
        print(Employee.numberOfEmployees)
    ```
    - This is a static method which doesn't operate on instance data.
    - It simply prints the total number of employees stored in the `numberOfEmployees` class variable.

5. **Getter and Setter Methods for `base_salary` and `hourly_rate`**:
    ```python
    def set_base_salary(self, base_salary):
        if base_salary <= 0:
            raise ValueError("Salary cannot be 0 or less.")
        self.base_salary = base_salary

    def get_base_salary(self):
        return self.base_salary

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.hourly_rate = hourly_rate
    ```
    - These methods provide encapsulation for the `base_salary` and `hourly_rate` instance variables.
    - They allow getting and setting these variables, with validation to ensure that the values are valid.

6. **Main Block**:
    ```python
    if __name__ == "__main__":
        employee = Employee(50000, 20)
        Employee.print_number_of_employees()
        wage = employee.calculate_wage()
        print(wage)
    ```
    - This block is executed when the script is run directly (not imported as a module).
    - It creates an instance of the `Employee` class with a base salary of 50000 and an hourly rate of 20.
    - It then prints the total number of employees using the static method `print_number_of_employees()`.
    - Finally, it calculates and prints the wage of the employee using the `calculate_wage()` method, without specifying any extra hours (defaulting to 0).
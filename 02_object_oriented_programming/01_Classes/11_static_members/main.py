class Employee:
    number_of_employees = 0  # Class variable to keep track of the number of employees

    def __init__(self, base_salary, hourly_rate=None):
        """
        Constructor method to initialize an Employee object.

        Parameters:
        - base_salary: Base salary of the employee.
        - hourly_rate: Hourly rate for extra hours worked (default is None).
        """
        self.__set_base_salary(base_salary)  # Set base salary using a private method
        if hourly_rate is None:
            self.hourly_rate = 0  # If hourly_rate is not provided, set it to 0
        else:
            self.__set_hourly_rate(hourly_rate)  # Set hourly rate using a private method
        Employee.number_of_employees += 1  # Increment the number of employees

    @staticmethod
    def print_number_of_employees():
        """Static method to print the total number of employees."""
        print(f'Number of Employees is {Employee.number_of_employees}')

    def calculate_wage(self, extra_hours=0):
        """
        Method to calculate the wage of the employee.

        Parameters:
        - extra_hours: Number of extra hours worked (default is 0).

        Returns:
        - Total wage of the employee.
        """
        return self.base_salary + (self.hourly_rate * extra_hours)

    def __set_base_salary(self, base_salary):
        """
        Private method to set the base salary of the employee.

        Parameters:
        - base_salary: Base salary of the employee.
        """
        if base_salary < 0:
            raise ValueError("Salary cannot be less than 0.")
        self.base_salary = base_salary

    def __set_hourly_rate(self, hourly_rate):
        """
        Private method to set the hourly rate of the employee.

        Parameters:
        - hourly_rate: Hourly rate for extra hours worked.
        """
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.hourly_rate = hourly_rate


# Creating employee objects
employee1 = Employee(10000)
employee2 = Employee(50000, 20)

# Calculating wages for each employee
wage1 = employee1.calculate_wage()
wage2 = employee2.calculate_wage()

# Printing wages
print(wage1)
print(wage2)

# Printing the total number of employees
Employee.print_number_of_employees()

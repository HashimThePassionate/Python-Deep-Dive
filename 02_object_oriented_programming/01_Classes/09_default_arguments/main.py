class Employee:
    numberOfEmployees = 0

    def __init__(self, base_salary, hourly_rate=0):
        self.__set_base_salary(base_salary)
        self.__set_hourly_rate(hourly_rate)
        Employee.numberOfEmployees += 1

    def calculate_wage(self, extra_hours=0):
        return self.base_salary + (self.hourly_rate * extra_hours)

    @staticmethod
    def print_number_of_employees():
        print(Employee.numberOfEmployees)

    def __set_base_salary(self, base_salary):
        if base_salary <= 0:
            raise ValueError("Salary cannot be 0 or less.")
        self.base_salary = base_salary

    def __get_base_salary(self):
        return self.base_salary

    def __get_hourly_rate(self):
        return self.hourly_rate

    def __set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.hourly_rate = hourly_rate


if __name__ == "__main__":
    employee = Employee(50000, 20)
    Employee.print_number_of_employees()
    wage = employee.calculate_wage()
    print(wage)


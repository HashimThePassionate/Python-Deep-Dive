class Employee:
    def __init__(self):
        self.base_salary = 0
        self.hourly_rate = 0

    def calculate_wage(self, extra_hours):
        return self.base_salary + (self.hourly_rate * extra_hours)


if __name__ == "__main__":
    employee = Employee()
    employee.base_salary = 50000
    employee.hourly_rate = 20
    wage = employee.calculate_wage(20)
    print(wage)

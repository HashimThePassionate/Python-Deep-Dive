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

    def __get_base_salary(self):
        return self._base_salary

    def __get_hourly_rate(self):
        return self._hourly_rate

    def set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self._hourly_rate = hourly_rate


if __name__ == "__main__":
    employee = Employee()
    employee.set_base_salary(50000)
    employee.set_hourly_rate(20)
    print(f'Get Base Salary: {employee._get_base_salary()}')
    employee._get_hourly_rate()
    print(f'Get Hourly Rate: {employee._get_hourly_rate()}')
    wage = employee.calculate_wage(10)
    print(f'Calculate wages: {wage}')
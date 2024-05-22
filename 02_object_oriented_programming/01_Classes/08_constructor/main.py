class Employee:
    def __init__(self, base_salary, hourly_rate):
        self.__set_base_salary(base_salary)
        self.__set_hourly_rate(hourly_rate)

    def calculate_wage(self, extra_hours):
        return self.__base_salary + (self.__hourly_rate * extra_hours)

    def __set_base_salary(self, base_salary):
        if base_salary <= 0:
            raise ValueError("Salary cannot be 0 or less.")
        self.__base_salary = base_salary

    def __set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.__hourly_rate = hourly_rate

    # Getter methods can be public if needed
    def get_base_salary(self):
        return self.__base_salary

    def get_hourly_rate(self):
        return self.__hourly_rate


if __name__ == "__main__":
    employee = Employee(50000, 20)
    wage = employee.calculate_wage(10)
    print(f'Calculate wages: {wage}')
class Employee:
    def __init__(self, base_salary, hourly_rate=None):
        self.__set_base_salary(base_salary)
        if hourly_rate is None:
            self.hourly_rate = 0
        else:
            self.__set_hourly_rate(hourly_rate)

    def calculate_wage(self, extra_hours=0):
        return self.base_salary + (self.hourly_rate * extra_hours)

    def __set_base_salary(self, base_salary):
        if base_salary < 0:
            raise ValueError("Salary cannot be less than 0.")
        self.base_salary = base_salary

    def __get_base_salary(self):
        return self.base_salary

    def __get_hourly_rate(self):
        return self.hourly_rate

    def __set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.hourly_rate = hourly_rate



employee1 = Employee(10000)
employee2 = Employee(50000, 20)
wage1 = employee1.calculate_wage()
wage2 = employee2.calculate_wage()
print(wage1)
print(wage2)

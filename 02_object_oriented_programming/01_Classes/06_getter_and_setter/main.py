class Employee:
    def __init__(self, salary, hours):
        self.__salary = salary
        self.__hours = hours

    def calculate_wage(self, extra_hours):
        return f"The Calculated Wage is {self.__salary * self.__hours + 50 * extra_hours}"

    def set_base_salary(self, s):
        if s <= 0:
            raise ValueError("Salary must be greater than 0")
        self.__salary = s

    def get_base_salary(self):
        return self.__salary
    
    def set_hourly_rate(self, h):
        if h <0:
            raise ValueError("Hourly rate cannot be negative")
        self.__hours = h
    
    def get_hourly_rate(self):
        return self.__hours


e = Employee(10000,20)
print(e.calculate_wage(10))
print(e.__salary)

class Employee:
    def __init__(self, s, h):
        self.__salary = s
        self.__hours = h

    def calculate_wage(self, extra_hours):
        return f"The Calculated Wage is {self.__salary * self.__hours + 50 * extra_hours}"

    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary can not less then or equal to zero")
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_hours(self, hours):
        if hours <= 0:
            raise ValueError("Hours can not less then or equal to zero")
        self.__hours = hours

    def get_hours(self):
        return self.__hours
        
e = Employee(10000, 20)
print(e.calculate_wage(10))
e.set_salary(2000000.124)
e.set_hours(30)
print(e.calculate_wage(10))
try:
    print(e.set_salary(0))
except ValueError as e:
    print("Salary can not less then or equal to zero")

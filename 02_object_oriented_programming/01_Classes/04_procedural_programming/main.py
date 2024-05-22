def create_employee(base_salary, hourly_rate):
    return {
        "base_salary": base_salary,
        "hourly_rate": hourly_rate
    }

def calculate_wage(employee, extra_hours):
    return employee["base_salary"] + (employee["hourly_rate"] * extra_hours)

if __name__ == "__main__":
    employee = create_employee(50000, 20)
    wage = calculate_wage(employee, 20)
    print(wage)



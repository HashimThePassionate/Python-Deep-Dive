In Python, constructor overloading isn't directly supported as it is in some other languages like Java or C++. However, you can achieve similar behavior by using default parameter values and conditional logic within the constructor. Let's break down how the code achieves this:

1. **Constructor with Default Parameters**:
    ```python
    def __init__(self, base_salary, hourly_rate=None):
    ```
    - The constructor accepts two parameters: `base_salary` (mandatory) and `hourly_rate` (optional). 
    - The `hourly_rate` parameter is set to `None` by default.

2. **Handling Default Values**:
    ```python
    self.__set_base_salary(base_salary)
    if hourly_rate is None:
        self.hourly_rate = 0
    else:
        self.__set_hourly_rate(hourly_rate)
    ```
    - Inside the constructor, the `base_salary` is always set using the `__set_base_salary()` method.
    - If no `hourly_rate` is provided (i.e., it's `None`), it defaults to 0.
    - If a `hourly_rate` is provided, it's set using the `__set_hourly_rate()` method.

3. **Getter and Setter Methods**:
    ```python
    def __set_base_salary(self, base_salary):
    def __get_base_salary(self):
    def __get_hourly_rate(self):
    def __set_hourly_rate(self, hourly_rate):
    ```
    - These methods provide encapsulation for `base_salary` and `hourly_rate`, similar to the previous example.
    - They use double underscores (`__`) to make them "private", meaning they can only be accessed from within the class.

4. **Main Block**:
    ```python
    if __name__ == "__main__":
        employee1 = Employee(10000)
        employee2 = Employee(50000, 20)
        wage1 = employee1.calculate_wage()
        wage2 = employee2.calculate_wage()
        print(wage1)
        print(wage2)
    ```
    - This block demonstrates the usage of the `Employee` class.
    - It creates two instances of the `Employee` class, one with only the `base_salary` provided and another with both `base_salary` and `hourly_rate`.
    - It calculates and prints the wages for both employees using the `calculate_wage()` method.

So, by using default parameter values and conditional logic, you can achieve constructor overloading-like behavior in Python.
Certainly! Let's go through the code step by step and understand how the two classes, `TaxCalculator` and `TaxReport`, work together, and why they are tightly coupled.

### Code Explanation

#### Class `TaxCalculator`

1. **Initialization**:
    ```python
    class TaxCalculator:
        def __init__(self, taxable_income: float):
            self.__taxable_income = taxable_income
    ```
    - The `TaxCalculator` class has an `__init__` method that initializes an instance of the class with a `taxable_income` parameter.
    - The `taxable_income` is stored as a private attribute (`self.__taxable_income`).

2. **Calculate Tax**:
    ```python
        def calculate_tax(self) -> float:
            return self.__taxable_income * 0.3
    ```
    - The `calculate_tax` method calculates the tax by multiplying the `taxable_income` by 30% (0.3).
    - It returns the computed tax amount.

#### Class `TaxReport`

1. **Initialization**:
    ```python
    class TaxReport:
        def __init__(self):
            self.__calculator = TaxCalculator(1000000)
    ```
    - The `TaxReport` class has an `__init__` method that initializes an instance of the class.
    - It creates an instance of `TaxCalculator` with a fixed taxable income of 1,000,000 and assigns it to a private attribute (`self.__calculator`).

2. **Show Tax**:
    ```python
        def show(self):
            tax = self.__calculator.calculate_tax()
            print(tax)
    ```
    - The `show` method calculates the tax using the `calculate_tax` method of the `TaxCalculator` instance (`self.__calculator`).
    - It then prints the calculated tax.

#### Creating and Using the Report

1. **Creating an Instance of `TaxReport`**:
    ```python
    report = TaxReport()
    ```
    - An instance of the `TaxReport` class is created and assigned to the variable `report`.

2. **Showing the Tax**:
    ```python
    report.show()
    ```
    - The `show` method of the `report` instance is called, which calculates and prints the tax.

### Tight Coupling

The concept of coupling refers to the degree of direct knowledge that one class has about another. In this code, the `TaxReport` class is tightly coupled to the `TaxCalculator` class. This tight coupling is evident in the following ways:

1. **Direct Instance Creation**:
    - The `TaxReport` class directly creates an instance of `TaxCalculator` with a specific taxable income value (`1000000`). This means `TaxReport` relies on the specific implementation and existence of `TaxCalculator`.

    ```python
    self.__calculator = TaxCalculator(1000000)
    ```

2. **Fixed Dependency**:
    - The `TaxReport` class cannot easily switch to a different tax calculator without modifying the code. This makes the design inflexible and hard to extend or modify.

3. **Private Attributes**:
    - Both classes use private attributes (prefixed with double underscores), which means they encapsulate their data tightly. While encapsulation is generally good practice, in this case, it emphasizes that `TaxReport` cannot function without `TaxCalculator`.

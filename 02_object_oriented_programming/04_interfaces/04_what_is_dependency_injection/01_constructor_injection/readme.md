# Constructor Injection

### 1. `TaxCalculator` Abstract Base Class

```python
from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self) -> float:
        pass
```

- This defines an abstract base class `TaxCalculator` with a single abstract method `calculate_tax()`. Concrete implementations of this class will provide the actual tax calculation logic.

### 2. `TaxCalculator24` Concrete Implementation

```python
class TaxCalculator24(TaxCalculator):
    def __init__(self, taxable_income: float):
        self.__taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.__taxable_income * 0.3
```

- `TaxCalculator24` is a concrete implementation of `TaxCalculator`. It implements the `calculate_tax()` method, calculating tax based on a taxable income of 30%.

### 3. `TaxReport` Class

```python
class TaxReport:
    def __init__(self, calculator: TaxCalculator24):
        self.__calculator = calculator

    def show(self):
        tax = self.__calculator.calculate_tax()
        print(tax)
```

- `TaxReport` is a class responsible for generating tax reports.
- It takes a `calculator` object as a parameter during initialization. This is where constructor injection occurs. The `calculator` parameter is of type `TaxCalculator`, the abstract base class.
- The `show()` method calculates and displays the tax using the injected `calculator` object.

### 4. Example Usage

```python
if __name__ == "__main__":
    calculator = TaxCalculator24(100000)
    report = TaxReport(calculator)
    report.show()
```

- In the example usage, an instance of `TaxCalculator24` is created with a taxable income of 100,000.
- This instance is then passed as an argument to the `TaxReport` constructor, injecting the dependency.
- Finally, the `show()` method of `TaxReport` is called, which internally uses the injected `calculator` object to calculate and display the tax.

### Key Points

- **Constructor Injection**: Dependencies are injected into a class via its constructor. This promotes loose coupling and makes the class easier to test and maintain.
- **Abstraction**: The use of abstract base classes allows for flexibility in implementing different tax calculation strategies while enforcing a common interface.
- **Encapsulation**: The `taxable_income` attribute in `TaxCalculator24` is encapsulated with double underscores (`__taxable_income`), making it private to the class.

This design pattern facilitates modular and extensible code, where different implementations of `TaxCalculator` can be easily plugged into `TaxReport` without modifying its code.

# 🎯 Method Injection 🚀

**Method Injection** is a pattern in which a method (or function) is passed as a parameter to another method, enabling dynamic behavior and flexibility. This pattern is particularly useful in creating loosely coupled, easily testable code by allowing the receiving method to invoke a method that performs specific operations. Let's explore method injection through a **Tax Report** example! 📊

## 📖 Table of Contents

- [🎯 Method Injection 🚀](#-method-injection-)
  - [📖 Table of Contents](#-table-of-contents)
  - [🔍 What is Method Injection?](#-what-is-method-injection)
  - [💼 Why Use Method Injection?](#-why-use-method-injection)
  - [🛠️ Implementation of Method Injection](#️-implementation-of-method-injection)
    - [Step 1: Define the `TaxCalculator` Abstract Base Class](#step-1-define-the-taxcalculator-abstract-base-class)
    - [Step 2: Implement a Concrete `TaxCalculator24` Class](#step-2-implement-a-concrete-taxcalculator24-class)
    - [Step 3: Define the `TaxReport` Class Using Method Injection](#step-3-define-the-taxreport-class-using-method-injection)
  - [🚀 Example Usage](#-example-usage)
  - [🎯 Key Points](#-key-points)

## 🔍 What is Method Injection?

In **Method Injection**, instead of creating dependencies internally or setting them through constructors or setters, a class receives methods as parameters. This approach allows methods to be passed in at runtime, enabling more flexible and dynamic code behavior. In our example, we’ll pass the `calculate_tax` method from various tax calculators to a `TaxReport` class to dynamically calculate tax based on the method provided. 🧩

## 💼 Why Use Method Injection?

1. **🧩 Dynamic Behavior**:
   - Method injection allows for flexible behavior. The logic in the `TaxReport` class can change based on the `calculate_tax` method passed in, making it adaptable to different scenarios.

2. **🔗 Loose Coupling**:
   - By injecting methods rather than hard-coding dependencies, we reduce the dependency of `TaxReport` on specific tax calculators, promoting modularity.

3. **🧪 Enhanced Testability**:
   - Allows for easy injection of mock or stub methods for unit testing, enabling isolated testing of `TaxReport`.

## 🛠️ Implementation of Method Injection

Let's implement method injection in a `TaxReport` class, where the `show` method accepts a tax calculation method as a parameter.

### Step 1: Define the `TaxCalculator` Abstract Base Class

```python
from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self) -> float:
        pass
```

- **Abstract Base Class**: `TaxCalculator` defines a `calculate_tax` method that concrete tax calculator classes must implement.

### Step 2: Implement a Concrete `TaxCalculator24` Class

```python
class TaxCalculator24(TaxCalculator):
    def __init__(self, taxable_income: float):
        self.__taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.__taxable_income * 0.3  # 30% tax rate
```

- **Concrete Implementation**: `TaxCalculator24` calculates tax at a rate of 30%.

### Step 3: Define the `TaxReport` Class Using Method Injection

```python
class TaxReport:
    def __init__(self):
        self.__calculator = None

    def show(self, calculator: TaxCalculator):
        tax = calculator.calculate_tax()
        print(f"Calculated Tax: {tax}")
```

- **Method Injection**: The `show` method takes a `calculator` parameter, calls its `calculate_tax` method, and prints the result.
- **Loose Coupling**: `TaxReport` doesn’t store the calculator permanently; it uses the passed-in calculator only within `show`.

## 🚀 Example Usage

Here's how to use the `TaxReport` class with different tax calculators.

```python
if __name__ == "__main__":
    # Creating a TaxCalculator24 instance with a taxable income
    calculator = TaxCalculator24(100000)
    
    # Creating a TaxReport instance
    report = TaxReport()
    
    # Displaying the tax using the TaxCalculator24 instance
    report.show(calculator)  # Output: Calculated Tax: 30000.0

    # Hypothetically switching to a different tax calculator
    class TaxCalculator23(TaxCalculator):
        def calculate_tax(self) -> float:
            return 0.0  # Assuming 0% tax

    # Using the new calculator
    report.show(TaxCalculator23())  # Output: Calculated Tax: 0.0
```

- **🎛️ Dynamic Method Injection**: By passing different calculators to `show`, `TaxReport` adapts to varying tax calculation logic.
- **📊 Real-Time Adaptability**: `TaxReport` changes behavior based on the calculator passed in, without requiring permanent dependency on any specific calculator.

## 🎯 Key Points

- **🧩 Flexible Dependency Management**: Method injection provides flexibility by enabling methods to be injected dynamically at runtime.
- **🔗 Loose Coupling**: Promotes loose coupling by not binding `TaxReport` directly to any particular `TaxCalculator` implementation.
- **🧪 Enhanced Testability**: Allows for easy testing by injecting mock or stub methods.
- **💡 Ideal for Variable Logic**: Method injection is especially useful when the logic might vary frequently or depend on runtime conditions.

Method injection provides an elegant way to handle dynamic dependencies in Python. By injecting only the required method, you gain flexibility, maintainability, and simplicity in designing classes like `TaxReport`. 🎉
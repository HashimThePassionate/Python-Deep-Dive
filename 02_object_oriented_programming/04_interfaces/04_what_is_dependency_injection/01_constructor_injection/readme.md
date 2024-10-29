# 🌟 Constructor Injection

In this guide, we’ll explore **Constructor Injection** in Python through a practical example involving tax calculation. Constructor Injection is a design pattern that promotes loose coupling, flexibility, and testability by passing dependencies into a class through its constructor. Let’s dive into the details! 🚀


## 📖 Table of Contents

- [🌟 Constructor Injection](#-constructor-injection)
  - [📖 Table of Contents](#-table-of-contents)
  - [🔍 Introduction to Constructor Injection](#-introduction-to-constructor-injection)
  - [📝 Defining the TaxCalculator Interface](#-defining-the-taxcalculator-interface)
  - [💡 Creating a Concrete Tax Calculator (TaxCalculator24)](#-creating-a-concrete-tax-calculator-taxcalculator24)
  - [📊 Building the TaxReport Class](#-building-the-taxreport-class)
  - [🚀 Example Usage](#-example-usage)
  - [🎯 Key Takeaways](#-key-takeaways)


## 🔍 Introduction to Constructor Injection

Constructor Injection is a type of **Dependency Injection (DI)** that allows dependencies to be passed into a class via its constructor. This pattern is effective for:

- **🔓 Loose Coupling**: Classes depend on abstractions, not specific implementations.
- **🧪 Testability**: Dependencies can be replaced with mock objects for testing.
- **⚙️ Flexibility**: Easily swap different implementations without changing the dependent class.
- **🛠️ Maintainability**: Dependencies are managed centrally, making complex applications easier to maintain.

In this example, we’ll use a **TaxCalculator** interface to demonstrate how different tax calculation strategies can be injected into a **TaxReport** class.


## 📝 Defining the TaxCalculator Interface

The first step is to define an interface (or abstract base class) for our tax calculator. This interface ensures that any class implementing it will have a `calculate_tax` method.

```python
from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self) -> float:
        pass
```

- **📜 `ABC` and `abstractmethod`**: This makes `TaxCalculator` an abstract base class, enforcing that any subclass must implement the `calculate_tax` method.
- **🧩 Abstraction**: The interface specifies **what** the calculator should do but not **how**.


## 💡 Creating a Concrete Tax Calculator (TaxCalculator24)

Now, we’ll create a specific implementation of the `TaxCalculator` interface called `TaxCalculator24`. This class will calculate tax based on a fixed rate.

```python
class TaxCalculator24(TaxCalculator):
    def __init__(self, taxable_income: float):
        self.__taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.__taxable_income * 0.3  # 30% tax rate
```

- **🏗️ Implementation**: `TaxCalculator24` calculates tax based on a 30% rate.
- **🔒 Encapsulation**: The `taxable_income` attribute is private, ensuring it can’t be accessed directly outside the class.
- **⚙️ Flexibility**: Allows for other tax calculation strategies by implementing different subclasses of `TaxCalculator`.


## 📊 Building the TaxReport Class

The `TaxReport` class is responsible for generating tax reports. Instead of creating its own `TaxCalculator`, it accepts a calculator as a dependency through **constructor injection**.

```python
class TaxReport:
    def __init__(self, calculator: TaxCalculator):
        self.__calculator = calculator

    def show(self):
        tax = self.__calculator.calculate_tax()
        print(f"Calculated Tax: {tax}")
```

- **💼 Constructor Injection**: `TaxReport` receives an instance of `TaxCalculator` via its constructor, making it loosely coupled to any specific tax calculation implementation.
- **🔗 Dependency on Abstraction**: By using `TaxCalculator` as a parameter type, `TaxReport` can accept any object that implements `TaxCalculator`.
- **📈 Scalability**: `TaxReport` can use various implementations of `TaxCalculator` without modification.


## 🚀 Example Usage

Now, let’s see how we can use the `TaxReport` class with `TaxCalculator24`.

```python
if __name__ == "__main__":
    calculator = TaxCalculator24(100000)  # Taxable income of 100,000
    report = TaxReport(calculator)        # Injecting dependency
    report.show()                         # Output: Calculated Tax: 30000.0
```

- **🛠️ Instance Creation**: We create an instance of `TaxCalculator24` with a taxable income of 100,000.
- **🔗 Dependency Injection**: We pass `calculator` as an argument to `TaxReport`, injecting the dependency.
- **📊 Output**: The `show()` method of `TaxReport` calculates and prints the tax using `TaxCalculator24`.


## 🎯 Key Takeaways

1. **🔌 Constructor Injection**: Dependencies are passed into a class through its constructor, promoting loose coupling and better testability.
2. **🧩 Abstraction**: Using an abstract base class (interface) like `TaxCalculator` allows for flexible implementations of the tax calculation logic.
3. **🔒 Encapsulation**: Keeping attributes private ensures that they can only be accessed through defined methods.
4. **🔄 Modularity**: This design pattern supports modularity and scalability, allowing different `TaxCalculator` implementations to be used without altering the `TaxReport` class.

Constructor Injection is an excellent approach for structuring dependencies, especially in complex applications, as it fosters clean, organized, and easily testable code. 🎉
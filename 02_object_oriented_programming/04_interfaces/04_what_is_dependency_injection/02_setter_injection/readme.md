# 📚 Setter Injection 🚀

In this guide, we’ll explore **Setter Injection** in Python. Setter Injection is a design pattern that provides flexibility by allowing dependencies to be set or updated after object creation. This approach promotes **dynamic dependency assignment**, **testability**, and **loose coupling**, making it an invaluable technique for maintaining and testing complex systems. Let’s dive in! 🎉

## 📖 Table of Contents

- [📚 Setter Injection 🚀](#-setter-injection-)
  - [📖 Table of Contents](#-table-of-contents)
  - [🔍 What is Setter Injection?](#-what-is-setter-injection)
  - [💼 Why Use Setter Injection?](#-why-use-setter-injection)
    - [⚙️ Flexibility](#️-flexibility)
    - [🧪 Testing](#-testing)
    - [🔄 Avoiding Circular Dependencies](#-avoiding-circular-dependencies)
    - [🔗 Reducing Coupling](#-reducing-coupling)
    - [⏳ Delayed Initialization](#-delayed-initialization)
  - [🛠️ Implementation of Setter Injection](#️-implementation-of-setter-injection)
    - [Step 1: Define an Abstract `TaxCalculator` Base Class](#step-1-define-an-abstract-taxcalculator-base-class)
    - [Step 2: Implement a Concrete `TaxCalculator24` Class](#step-2-implement-a-concrete-taxcalculator24-class)
    - [Step 3: Implement the `TaxReport` Class with Setter Injection](#step-3-implement-the-taxreport-class-with-setter-injection)
  - [🚀 Example Usage](#-example-usage)
  - [🎯 Key Points](#-key-points)

## 🔍 What is Setter Injection?

**Setter Injection** is a dependency injection technique where dependencies are provided through setter methods instead of constructors. This means that the dependency is not injected at the time of object creation but can be set or modified at any point afterward. This approach is highly **flexible** and allows **runtime changes** to dependencies without recreating objects. 💡

## 💼 Why Use Setter Injection?

### ⚙️ Flexibility
- **Dynamic Dependency Changes**: Setter injection enables changing dependencies at runtime based on changing requirements or conditions.
- **Runtime Adaptability**: Allows adapting behavior dynamically by switching between different dependency implementations.

### 🧪 Testing
- **Easier Isolation in Tests**: By injecting mock or stub dependencies, setter injection makes it easier to isolate and test specific parts of a system.
- **Controlled Test Scenarios**: Enables swapping dependencies to verify various interactions and behaviors.

### 🔄 Avoiding Circular Dependencies
- **Breaking Dependency Loops**: Setter injection helps prevent circular dependencies, where classes rely on each other directly, making code more maintainable.

### 🔗 Reducing Coupling
- **Decoupling Dependencies**: Since dependencies aren’t hard-coded, setter injection reduces coupling, promoting modularity and making it easier to extend functionality.

### ⏳ Delayed Initialization
- **Lazy Dependency Assignment**: You can delay initializing dependencies until they’re actually needed, which can optimize resource usage and improve application performance.

## 🛠️ Implementation of Setter Injection

Let’s implement setter injection in a `TaxReport` class that can dynamically change its dependency on different `TaxCalculator` instances.

### Step 1: Define an Abstract `TaxCalculator` Base Class

```python
from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self) -> float:
        pass
```

- **📝 Abstract Base Class**: `TaxCalculator` serves as an interface with a `calculate_tax` method that subclasses must implement.
- **📐 Abstraction**: Allows multiple `TaxCalculator` implementations to share a common interface.

### Step 2: Implement a Concrete `TaxCalculator24` Class

```python
class TaxCalculator24(TaxCalculator):
    def __init__(self, taxable_income: float):
        self.__taxable_income = taxable_income

    def calculate_tax(self) -> float:
        return self.__taxable_income * 0.3  # 30% tax rate
```

- **🔍 Concrete Implementation**: `TaxCalculator24` calculates tax based on a fixed 30% rate.
- **🔒 Encapsulation**: The taxable income is private, preventing direct external access.

### Step 3: Implement the `TaxReport` Class with Setter Injection

```python
class TaxReport:
    def __init__(self, calculator: TaxCalculator):
        self.__calculator = calculator

    def set_calculator(self, calculator: TaxCalculator):
        self.__calculator = calculator

    def show(self):
        tax = self.__calculator.calculate_tax()
        print(f"Calculated Tax: {tax}")
```

- **🔗 Setter Injection**: The `set_calculator` method allows for dynamically changing the `calculator` dependency at runtime.
- **🔒 Encapsulation**: The `__calculator` attribute is private, maintaining control over dependency access.

## 🚀 Example Usage

Here’s how to use `TaxReport` with setter injection for switching between different tax calculators.

```python
if __name__ == "__main__":
    # Initial setup with TaxCalculator24
    calculator = TaxCalculator24(100000)
    report = TaxReport(calculator)
    report.show()  # Output: Calculated Tax: 30000.0
    
    # Dynamically switching to a new calculator (TaxCalculator23, hypothetically with 0% tax)
    report.set_calculator(TaxCalculator24(200000))
    report.show()  # Output may vary based on new calculator logic
```

- **🎛️ Dynamic Dependency Changes**: After setting an initial `TaxCalculator24`, the dependency is switched using `set_calculator`, demonstrating flexibility.
- **📊 Real-Time Adaptability**: With setter injection, we adapt the behavior of `TaxReport` without recreating it.

## 🎯 Key Points

- **🔄 Dynamic Dependency Injection**: Setter injection allows dependencies to be updated dynamically, promoting flexible and adaptable code.
- **🔍 Testability**: Easily inject mock or stub dependencies, simplifying unit testing.
- **🧩 Decoupling**: Reduces coupling between classes, enhancing modularity and maintainability.
- **⏳ Delayed Initialization**: Useful for initializing dependencies only when needed, saving resources.
- **💡 Practical for Design Patterns**: Setter injection is widely applicable across design patterns, promoting robust and scalable architectures.

Setter Injection provides a powerful mechanism for handling dependencies with flexibility, adaptability, and maintainability in mind. It’s a valuable tool in any developer’s toolkit for designing cleaner, more modular, and testable code. 🎉
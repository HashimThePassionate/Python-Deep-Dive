# Method injection
Method injection involves passing a method (or function) as a parameter to another method, allowing the receiving method to call the passed method to perform certain operations. In the provided code, we implement method injection in the `TaxReport` class by passing the `calculate_tax` method of a `TaxCalculator` object as a parameter to the `show` method. Here's how it works:

### Implementation of Method Injection:

```python
class TaxReport:
    def __init__(self):
        self.__calculator = None

    def show(self, calculator: TaxCalculator):
        tax = calculator.calculate_tax()
        print(tax)
```

- The `TaxReport` class has an instance variable `__calculator` to store a `TaxCalculator` object.
- The `show` method of `TaxReport` takes a `calculator` parameter of type `TaxCalculator`. Instead of storing the calculator instance directly, it calls the `calculate_tax` method of the passed `calculator` parameter to calculate and display the tax.

### Example Usage:

```python
calculator = TaxCalculator24(100000)
report = TaxReport()
report.show(calculator)

report.show(TaxCalculator23())
```

- We create instances of `TaxCalculator24` and `TaxCalculator23`.
- We create an instance of `TaxReport`.
- We call the `show` method of `TaxReport`, passing a `TaxCalculator` instance as a parameter. This instance's `calculate_tax` method is called internally by `show` to calculate and print the tax.
- We call the `show` method again, this time passing a different `TaxCalculator` instance (`TaxCalculator23`). Again, the `calculate_tax` method of this instance is called to calculate and print the tax.

### Key Points:

- **Dynamic Behavior**: Method injection allows for dynamic behavior because the behavior of the method being injected can vary based on the method passed as a parameter.
- **Loose Coupling**: By injecting the method as a parameter, the `TaxReport` class remains loosely coupled with the `TaxCalculator` implementations. It doesn't depend directly on concrete implementations but relies on the behavior defined by the method passed to it.
- **Testability**: Method injection facilitates testing because you can pass mock or stub methods for testing purposes, allowing you to isolate the behavior being tested.

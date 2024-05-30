# Setter injection is used for several reasons:

1. **Flexibility**: Setter injection allows you to change dependencies dynamically at runtime. This flexibility is valuable when you need to switch between different implementations of an interface or when you need to update dependencies based on changing requirements or conditions.

2. **Testing**: Setter injection can facilitate testing by allowing you to inject mock or stub dependencies for testing purposes. This enables you to isolate the behavior of the class being tested and verify its interactions with its dependencies more easily.

3. **Avoiding Circular Dependencies**: Setter injection can help avoid circular dependencies between classes. Circular dependencies can make code harder to understand and maintain, and setter injection allows you to break these cycles more easily by injecting dependencies after object creation.

4. **Reducing Coupling**: Setter injection reduces the coupling between classes because the dependency is not hard-coded into the constructor. This makes classes more modular and easier to maintain, as changes to one class do not necessarily require changes to other classes.

5. **Delayed Initialization**: Setter injection allows you to delay the initialization of dependencies until they are actually needed. This can be useful when creating objects in advance but deferring the configuration or initialization of dependencies until later in the program's execution.

Overall, setter injection provides flexibility, testability, and reduced coupling, making it a useful technique for managing dependencies in object-oriented systems. However, like any design pattern, it should be used judiciously and in alignment with the principles of good software design.

### Implementation of Setter Injection

```python
class TaxReport:
    def __init__(self, calculator: TaxCalculator):
        self.__calculator = calculator

    def set_calculator(self, calculator: TaxCalculator):
        self.__calculator = calculator
```

- The `TaxReport` class has a constructor that takes a `calculator` parameter of type `TaxCalculator`. This parameter is used to initialize the `__calculator` attribute.
- Additionally, the class contains a `set_calculator` method which takes a `TaxCalculator` object as its argument. This method allows for dynamically changing the `calculator` dependency.

### How Setter Injection is Used

```python
calculator = TaxCalculator24(100000)
report = TaxReport(calculator)
report.show()

report.set_calculator(TaxCalculator23())
report.show()
```

- Initially, an instance of `TaxCalculator24` is created with a taxable income of 100,000 and passed to the `TaxReport` constructor. This sets the initial calculator for the report.
- The `show()` method of `TaxReport` is then called, which calculates and displays the tax using the `TaxCalculator24` instance.
- Later, the `set_calculator` method of `TaxReport` is used to switch the calculator to `TaxCalculator23`. This effectively changes the calculator dependency.
- Finally, the `show()` method is called again, this time using the `TaxCalculator23` instance to calculate and display the tax, resulting in a tax of 0.0 being printed.

### Key Points

- **Dynamic Dependency Changes**: Setter injection allows for the dynamic change of dependencies at runtime, providing flexibility in the behavior of the `TaxReport` class.
- **Encapsulation**: The `__calculator` attribute is encapsulated within the `TaxReport` class, and the setter method provides controlled access to modify this dependency.
- **Flexibility**: Setter injection is useful when you want to allow the flexibility of changing dependencies even after the object is created, without needing to recreate the object.

Overall, setter injection provides a mechanism to decouple the dependency assignment from the object construction, promoting flexibility and maintainability in the codebase.
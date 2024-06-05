# The Comparable Interface

```python
from functools import total_ordering

@total_ordering
class Customer:
    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

# Create Customer instances
customer1 = Customer("Blice")
customer2 = Customer("Cob")

# Compare customers
if customer1 < customer2:
    print(f"{customer1} comes before {customer2}")
elif customer1 == customer2:
    print(f"{customer1} and {customer2} are equal")
else:
    print(f"{customer1} comes after {customer2}")

```
This code demonstrates the implementation of the `Comparable` interface in Python using the `total_ordering` decorator from the `functools` module.

Here's a breakdown of the code:

1. `from functools import total_ordering`: This imports the `total_ordering` decorator from the `functools` module. This decorator is used to minimize the number of comparison methods that need to be implemented for a class to support all comparison operators.

2. `@total_ordering`: This decorator is applied to the `Customer` class to enable total ordering. It automatically provides implementations for the remaining rich comparison methods (`__le__`, `__gt__`, and `__ge__`) based on the ones provided (`__lt__` and `__eq__`).

3. `class Customer:`: This defines the `Customer` class.

4. `def __init__(self, name):`: This is the constructor method for the `Customer` class. It initializes a `Customer` object with a `name` attribute.

5. `def __lt__(self, other):`: This method defines the less-than comparison (`<`) for `Customer` objects. It returns `True` if the `name` of the current `Customer` object is less than the `name` of the `other` object.

6. `def __eq__(self, other):`: This method defines the equality (`==`) comparison for `Customer` objects. It returns `True` if the `name` of the current `Customer` object is equal to the `name` of the `other` object.

7. `def __str__(self):`: This method defines the string representation of a `Customer` object. It returns the `name` attribute of the `Customer`.

8. Creating `Customer` instances: Two `Customer` instances, `customer1` and `customer2`, are created with names "Blice" and "Cob", respectively.

9. Comparing customers: The code then compares `customer1` and `customer2` using the `<` operator. Depending on the comparison result, it prints whether `customer1` comes before `customer2`, if they are equal, or if `customer1` comes after `customer2`.

This code illustrates how you can implement the `Comparable` interface in Python using the `total_ordering` decorator, allowing you to compare objects of a custom class using standard comparison operators.
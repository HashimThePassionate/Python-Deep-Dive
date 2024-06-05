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

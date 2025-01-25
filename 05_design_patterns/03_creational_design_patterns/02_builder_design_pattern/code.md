### **Imports and Constants**
```python
import time
from enum import Enum
```
1. **`import time`**: This module provides time-related functions. Here, it’s used to simulate delays in pizza preparation steps.
2. **`from enum import Enum`**: This module allows the creation of enumerations. Enums are used here to define specific constants like pizza progress stages, dough types, and toppings.

```python
PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum(
    "PizzaTopping",
    "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano",
)
STEP_DELAY = 3  # Delay between steps in seconds
```
3. **`PizzaProgress`**: Enum representing the stages of pizza preparation (queued → preparation → baking → ready).
4. **`PizzaDough`**: Enum for different types of pizza dough (thin or thick).
5. **`PizzaSauce`**: Enum for sauces (tomato or crème fraîche).
6. **`PizzaTopping`**: Enum listing toppings (mozzarella, ham, etc.).
7. **`STEP_DELAY`**: A constant delay of 3 seconds to mimic real-world preparation.

---

### **The Pizza Class**
```python
class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
```
8. **`class Pizza`**: Represents the pizza being created.
9. **`__init__(self, name)`**: Initializes the pizza object with:
   - **`name`**: The name of the pizza (e.g., Margarita, Creamy Bacon).
   - **`dough`**, **`sauce`**, and **`topping`**: Set to default `None` or empty.

```python
    def __str__(self):
        return self.name
```
10. **`__str__`**: Ensures that when the pizza object is printed, its name is displayed (e.g., “margarita”).

```python
    def prepare_dough(self, dough):
        self.dough = dough
        print(f"Preparing the {self.dough.name} dough of your {self}...")
        time.sleep(STEP_DELAY)
        print(f"Done with the {self.dough.name} dough")
```
11. **`prepare_dough(self, dough)`**: Handles dough preparation:
    - Sets the dough type.
    - Prints a message indicating the dough is being prepared.
    - Introduces a delay using `time.sleep`.

---

### **Builders**
#### **MargaritaBuilder**
```python
class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5
```
12. **`class MargaritaBuilder`**: Handles the construction of a Margarita pizza.
13. **`__init__`**:
    - Creates a `Pizza` object named "margarita".
    - Sets progress to `queued` (initial stage).
    - Sets the baking time to 5 seconds.

```python
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)
```
14. **`prepare_dough`**:
    - Updates progress to `preparation`.
    - Calls the `prepare_dough` method of the `Pizza` class with `thin` dough.

```python
    def add_sauce(self):
        print(f"Adding the tomato sauce to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the tomato sauce")
```
15. **`add_sauce`**: Adds tomato sauce to the pizza with a delay for realism.

```python
    def add_topping(self):
        print(f"Adding the topping (double mozzarella, oregano) to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the topping")
```
16. **`add_topping`**: Adds toppings specific to a Margarita pizza.

```python
    def bake(self):
        print(f"Baking your {self.pizza} for {self.baking_time} seconds...")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"Your {self.pizza} is ready!")
```
17. **`bake`**:
    - Simulates baking the pizza for 5 seconds.
    - Updates progress to `ready`.

#### **CreamyBaconBuilder**
```python
class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7
```
18. **`class CreamyBaconBuilder`**: Similar to `MargaritaBuilder`, but for a Creamy Bacon pizza with:
    - 7 seconds baking time.
    - Different dough and toppings.

```python
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)
```
19. **`prepare_dough`**: Uses `thick` dough instead of `thin`.

```python
    def add_sauce(self):
        print(f"Adding the crème fraîche sauce to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the crème fraîche sauce")
```
20. **`add_sauce`**: Adds crème fraîche instead of tomato sauce.

```python
    def add_topping(self):
        print(f"Adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the topping")
```
21. **`add_topping`**: Adds a richer set of toppings, including bacon and mushrooms.

```python
    def bake(self):
        print(f"Baking your {self.pizza} for {self.baking_time} seconds...")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"Your {self.pizza} is ready!")
```
22. **`bake`**: Bakes for 7 seconds, specific to the creamy bacon pizza.

---

### **The Waiter (Director)**
```python
class Waiter:
    def __init__(self):
        self.builder = None
```
23. **`class Waiter`**: Acts as the director controlling the pizza-building process.
24. **`__init__`**: Initializes without a specific builder.

```python
    def construct_pizza(self, builder):
        self.builder = builder
        steps = (
            builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake,
        )
        [step() for step in steps]
```
25. **`construct_pizza`**:
    - Accepts a builder.
    - Executes the pizza-building steps (dough → sauce → topping → baking) in order.

```python
    @property
    def pizza(self):
        return self.builder.pizza
```
26. **`pizza`**: Returns the final constructed pizza.

---

### **Validation Function**
```python
def validate_style(builders):
    try:
        pizza_style = input("What pizza would you like, [m]argarita or [c]reamy bacon? ")
        builder = builders[pizza_style]()
        return (True, builder)
    except KeyError:
        print("Sorry, only margarita (key m) and creamy bacon (key c) are available")
        return (False, None)
```
27. **`validate_style`**:
    - Ensures valid user input.
    - Maps input (`m` or `c`) to the respective builder.
    - Handles invalid input gracefully with a message.

---

### **Main Function**
```python
def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False

    while not valid_input:
        valid_input, builder = validate_style(builders)

    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print(f"Enjoy your {pizza}!")
```
28. **`main`**:
    - Defines available builders (`MargaritaBuilder` and `CreamyBaconBuilder`).
    - Validates user input.
    - Directs the pizza-building process using the `Waiter`.
    - Displays the completed pizza.

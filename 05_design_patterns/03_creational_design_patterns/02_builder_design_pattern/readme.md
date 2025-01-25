# Builder Design Pattern 📦🍕

## Table of Contents 📋

- [Builder Design Pattern 📦🍕](#builder-design-pattern-)
  - [Table of Contents 📋](#table-of-contents-)
  - [Introduction 🏗️](#introduction-️)
  - [Real-World Examples 🌍](#real-world-examples-)
    - [1. Fast-Food Restaurants 🍔](#1-fast-food-restaurants-)
    - [2. Django Query Builder 🖥️](#2-django-query-builder-️)
  - [Comparison with the Factory Pattern 🏭](#comparison-with-the-factory-pattern-)
  - [Use Cases for the Builder Pattern ⚙️](#use-cases-for-the-builder-pattern-️)
  - [Implementing the Builder Pattern 🛠️](#implementing-the-builder-pattern-️)
    - [Step 1: Imports and Constants](#step-1-imports-and-constants)
    - [Step 2: The Pizza Class](#step-2-the-pizza-class)
    - [Step 3: The Builders](#step-3-the-builders)
      - [MargaritaBuilder](#margaritabuilder)
      - [CreamyBaconBuilder](#creamybaconbuilder)
    - [Step 4: The Waiter (Director)](#step-4-the-waiter-director)
    - [Step 5: Validation](#step-5-validation)
    - [Step 6: Main Function](#step-6-main-function)
  - [Output of the Program 📤](#output-of-the-program-)
  - [Extending the Pattern 🔄](#extending-the-pattern-)

---

## Introduction 🏗️

The **Builder Pattern** is a creational design pattern that helps in constructing complex objects step by step. Unlike other patterns like the Factory Method or Abstract Factory, the Builder Pattern is used when:

- Objects need to be created in multiple steps.
- The creation process involves assembling multiple parts.
- The object is not considered complete until all parts are constructed.

**Key Concept:** The Builder Pattern separates the construction of an object from its representation, enabling the same construction process to create different representations.

---

## Real-World Examples 🌍

### 1. Fast-Food Restaurants 🍔

- A **burger** is always prepared using the same steps (making the patty, adding toppings, packaging).
- The **differences** between a classic burger and a cheeseburger lie in their representation (type of cheese, sauce, etc.), not the construction steps.

**Actors in this Example:**

- **Director:** The cashier, who gives instructions on what needs to be prepared.
- **Builder:** The cook, who follows the instructions to prepare the order.

### 2. Django Query Builder 🖥️

- The `django-query-builder` library allows dynamic SQL query creation by following the Builder Pattern.
- Developers can dynamically build queries ranging from simple to complex using this library.

---

## Comparison with the Factory Pattern 🏭

The Builder Pattern differs from the Factory Pattern in the following ways:

| Feature                  | Factory Pattern      | Builder Pattern                  |
| ------------------------ | -------------------- | -------------------------------- |
| **Construction Process** | Single step          | Multiple steps                   |
| **Control Over Process** | Minimal              | Full control over each step      |
| **Director Role**        | Not required         | Often involves a director        |
| **Return Object**        | Returned immediately | Returned explicitly upon request |

---

## Use Cases for the Builder Pattern ⚙️

1. **Complex Object Creation:**

   - Useful when creating objects involves multiple steps or configurations.

2. **Avoiding Confusion:**

   - Prevents confusion caused by having multiple constructors with different parameters.

3. **Encapsulating Complexity:**

   - Handles scenarios where object construction involves validations, setting up data structures, or external calls.

---

## Implementing the Builder Pattern 🛠️

Let's create a **Pizza Ordering Application** to demonstrate the Builder Pattern. 🍕

### Step 1: Imports and Constants

We start with the necessary imports and constants:
**[Complete Code Explanations](./code.md)**
```python
import time
from enum import Enum

PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum(
    "PizzaTopping",
    "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano",
)
STEP_DELAY = 3  # Delay between steps in seconds
```

**Explanation:**

- Enums like `PizzaProgress`, `PizzaDough`, and `PizzaSauce` represent different attributes of a pizza.
- `STEP_DELAY` introduces a pause between each preparation step to mimic a real-world delay.

---

### Step 2: The Pizza Class

The `Pizza` class represents the end product. It is minimal and relies on the builder for its construction.

```python
class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f"Preparing the {self.dough.name} dough of your {self}...")
        time.sleep(STEP_DELAY)
        print(f"Done with the {self.dough.name} dough")
```

**Explanation:**

- The `Pizza` class initializes attributes like `name`, `dough`, `sauce`, and `topping`.
- The `prepare_dough` method simulates dough preparation with a delay.

---

### Step 3: The Builders

Builders handle the step-by-step construction of the pizza.

#### MargaritaBuilder

```python
class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print(f"Adding the tomato sauce to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the tomato sauce")

    def add_topping(self):
        print(f"Adding the topping (double mozzarella, oregano) to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the topping")

    def bake(self):
        print(f"Baking your {self.pizza} for {self.baking_time} seconds...")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"Your {self.pizza} is ready!")
```

#### CreamyBaconBuilder

```python
class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print(f"Adding the crème fraîche sauce to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the crème fraîche sauce")

    def add_topping(self):
        print(f"Adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your {self.pizza}...")
        time.sleep(STEP_DELAY)
        print("Done with the topping")

    def bake(self):
        print(f"Baking your {self.pizza} for {self.baking_time} seconds...")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"Your {self.pizza} is ready!")
```

**Explanation:**

- Each builder initializes a specific pizza and handles its unique attributes.
- Additional methods like `add_sauce()`, `add_topping()`, and `bake()` handle specific steps in the pizza-making process.

---

### Step 4: The Waiter (Director)

The `Waiter` directs the pizza-building process.

```python
class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (
            builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake,
        )
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza
```

---

### Step 5: Validation

The `validate_style` function ensures valid user input:

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

---

### Step 6: Main Function

The main function orchestrates the program:

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

---

## Output of the Program 📤

Example output when running the program:

```
What pizza would you like, [m]argarita or [c]reamy bacon? c
Preparing the thick dough of your creamy bacon...
Done with the thick dough
Adding the crème fraîche sauce to your creamy bacon
Done with the crème fraîche sauce
Adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon
Done with the topping
Baking your creamy bacon for 7 seconds
Your creamy bacon is ready
Enjoy your creamy bacon!
```

---

## Extending the Pattern 🔄

Want more pizza types? You can add a new builder (e.g., **HawaiianPizzaBuilder**) by inheriting from the existing builders or using composition for flexibility. 🍍🍕


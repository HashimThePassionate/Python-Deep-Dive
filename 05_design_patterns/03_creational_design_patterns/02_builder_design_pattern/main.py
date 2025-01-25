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

def validate_style(builders):
    try:
        pizza_style = input("What pizza would you like, [m]argarita or [c]reamy bacon? ")
        builder = builders[pizza_style]()
        return (True, builder)
    except KeyError:
        print("Sorry, only margarita (key m) and creamy bacon (key c) are available")
        return (False, None)

def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False

    while not valid_input:
        valid_input, builder = validate_style(builders)

    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print(f"Enjoy your {pizza}!")


if __name__ == "__main__":
    main()

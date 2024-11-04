# 🛠️ Data Classes in Action 🐍✨

Welcome to the **Data Classes in Action** section! 🎉 Data classes in Python provide a convenient and efficient way to create classes that primarily store data. They help reduce boilerplate code, enhance readability, and enforce type safety. This guide will delve deep into data classes, explaining their features with detailed, real-world, and easy-to-understand examples. Let’s get started! 🌟

## 📚 Table of Contents

1. [🔹 Introduction to Data Classes](#-introduction-to-data-classes)
2. [🛠️ Creating a Basic Data Class](#-creating-a-basic-data-class)
3. [🔗 Nesting Data Classes](#-nesting-data-classes)
4. [🧩 Adding Methods to Data Classes](#-adding-methods-to-data-classes)
5. [🔄 Immutability with `frozen=True`](#-immutability-with-frozentrue)
6. [🔢 Equality and Comparison](#-equality-and-comparison)
7. [🔒 Ensuring Uniqueness with `@unique`](#-ensuring-uniqueness-withunique)
8. [💡 Best Practices for Using Data Classes](#-best-practices-for-using-data-classes)
9. [🎯 Conclusion 🎯](#-conclusion-🎯)
10. [🌈 Additional Resources 🌈](#-additional-resources-🌈)

## 🔹 Introduction to Data Classes

**Data classes** in Python are a decorator and functions that automatically add special methods to user-defined classes. These methods include `__init__()`, `__repr__()`, `__eq__()`, and others, based on the class attributes. Introduced in Python 3.7 via [PEP 557](https://www.python.org/dev/peps/pep-0557/), data classes simplify the process of creating classes that primarily store data.

**Key Features:**
- **Automatic Method Generation:** Reduces boilerplate by auto-generating methods like `__init__`, `__repr__`, and `__eq__`.
- **Type Annotations:** Enforces type hints, enhancing code clarity and type safety.
- **Immutability:** Optionally makes instances immutable.
- **Customization:** Allows customization of generated methods and behavior.

## 🛠️ Creating a Basic Data Class

Let's start by creating a simple data class to represent a fraction, which consists of a numerator and a denominator.

### **Example: Representing a Fraction**

```python
from dataclasses import dataclass

@dataclass
class Fraction:
    numerator: int = 0
    denominator: int = 1
```

**Explanation:**

1. **Importing `dataclass`:**
   ```python
   from dataclasses import dataclass
   ```
   - `@dataclass` is a decorator that transforms the class below it into a data class.

2. **Defining the `Fraction` Data Class:**
   ```python
   @dataclass
   class Fraction:
       numerator: int = 0
       denominator: int = 1
   ```
   - **`@dataclass`:** Automatically adds an `__init__` method and others.
   - **Attributes:**
     - `numerator`: An integer representing the top part of the fraction. Defaults to `0`.
     - `denominator`: An integer representing the bottom part of the fraction. Defaults to `1`.

### **Usage:**

```python
# Creating a Fraction instance
half = Fraction(numerator=1, denominator=2)
print(half)  # Output: Fraction(numerator=1, denominator=2)
```

**Benefits:**
- **Simplicity:** Quickly define classes to store data without writing boilerplate code.
- **Readability:** Clear definition of what data the class holds.
- **Type Safety:** Enforces type annotations, reducing errors.

## 🔗 Nesting Data Classes

Data classes can be nested within each other, allowing you to model complex relationships and hierarchies. Let's explore a real-world scenario involving recipes and ingredients.

### **Real-World Example: Recipe Management**

Imagine you're building an application to manage recipes. Each recipe consists of various ingredients, categorized into aromatics, vegetables, meats, starches, and garnishes. Additionally, you need to specify the type of broth and the cooking time.

### **Step 1: Define Enumerations for Measures and Broth Types**

```python
from enum import Enum, auto

class ImperialMeasure(Enum):
    TEASPOON = auto()
    TABLESPOON = auto()
    CUP = auto()

class Broth(Enum):
    VEGETABLE = auto()
    CHICKEN = auto()
    BEEF = auto()
    FISH = auto()
```

**Explanation:**
- **`ImperialMeasure`:** Enum to represent units of measurement.
- **`Broth`:** Enum to represent types of broth used in recipes.

### **Step 2: Define the `Ingredient` Data Class**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP
```

**Explanation:**
- **`@dataclass(frozen=True)`:** Makes the instance immutable; fields cannot be changed after creation.
- **Attributes:**
  - `name`: Name of the ingredient.
  - `amount`: Quantity needed (defaults to `1`).
  - `units`: Measurement unit (defaults to `CUP`).

### **Step 3: Define the `Recipe` Data Class**

```python
import datetime
from dataclasses import dataclass
from typing import Set

@dataclass
class Recipe:
    aromatics: Set[Ingredient]
    broth: Broth
    vegetables: Set[Ingredient]
    meats: Set[Ingredient]
    starches: Set[Ingredient]
    garnishes: Set[Ingredient]
    time_to_cook: datetime.timedelta
```

**Explanation:**
- **Attributes:**
  - `aromatics`, `vegetables`, `meats`, `starches`, `garnishes`: Sets of `Ingredient` instances, ensuring uniqueness.
  - `broth`: Type of broth used.
  - `time_to_cook`: Duration required to cook the recipe.

### **Step 4: Creating Instances**

```python
from copy import deepcopy

# Define Ingredients
pepper = Ingredient(name="Pepper", amount=1, units=ImperialMeasure.TABLESPOON)
garlic = Ingredient(name="Garlic", amount=2, units=ImperialMeasure.TEASPOON)
carrots = Ingredient(name="Carrots", amount=0.25, units=ImperialMeasure.CUP)
celery = Ingredient(name="Celery", amount=0.25, units=ImperialMeasure.CUP)
onions = Ingredient(name="Onions", amount=0.25, units=ImperialMeasure.CUP)
parsley = Ingredient(name="Parsley", amount=2, units=ImperialMeasure.TABLESPOON)
noodles = Ingredient(name="Noodles", amount=1.5, units=ImperialMeasure.CUP)
chicken = Ingredient(name="Chicken", amount=1.5, units=ImperialMeasure.CUP)

# Create a Recipe Instance
chicken_noodle_soup = Recipe(
    aromatics={pepper, garlic},
    broth=Broth.CHICKEN,
    vegetables={celery, onions, carrots},
    meats={chicken},
    starches={noodles},
    garnishes={parsley},
    time_to_cook=datetime.timedelta(minutes=60)
)

print(chicken_noodle_soup)
```

**Output:**
```
Recipe(aromatics={Ingredient(name='Pepper', amount=1, units=<ImperialMeasure.TABLESPOON: 2>), Ingredient(name='Garlic', amount=2, units=<ImperialMeasure.TEASPOON: 1>)}, broth=<Broth.CHICKEN: 2>, vegetables={Ingredient(name='Carrots', amount=0.25, units=<ImperialMeasure.CUP: 3>), Ingredient(name='Celery', amount=0.25, units=<ImperialMeasure.CUP: 3>), Ingredient(name='Onions', amount=0.25, units=<ImperialMeasure.CUP: 3>)}, meats={Ingredient(name='Chicken', amount=1.5, units=<ImperialMeasure.CUP: 3>)}, starches={Ingredient(name='Noodles', amount=1.5, units=<ImperialMeasure.CUP: 3>)}, garnishes={Ingredient(name='Parsley', amount=2, units=<ImperialMeasure.TABLESPOON: 2>)}, time_to_cook=datetime.timedelta(seconds=3600))
```

**Benefits:**
- **Structured Data:** Clearly groups related data together.
- **Immutability:** Ensures that ingredients cannot be altered once defined, preventing accidental modifications.
- **Type Safety:** Enforces that each field contains data of the specified type.

## 🧩 Adding Methods to Data Classes

Data classes aren't limited to just storing data; you can also add methods to encapsulate behaviors and functionality related to the data they hold. This enhances reusability and maintainability.

### **Real-World Example: Modifying a Recipe**

Suppose you want to add functionality to your `Recipe` data class to make the recipe vegetarian by removing meats and changing the broth type. Additionally, you want to list all ingredient names for verification.

### **Step 1: Add Methods to the `Recipe` Data Class**

```python
@dataclass
class Recipe:
    aromatics: Set[Ingredient]
    broth: Broth
    vegetables: Set[Ingredient]
    meats: Set[Ingredient]
    starches: Set[Ingredient]
    garnishes: Set[Ingredient]
    time_to_cook: datetime.timedelta

    def make_vegetarian(self):
        """
        Makes the recipe vegetarian by removing all meats and switching to vegetable broth.
        """
        self.meats.clear()  # Removes all meats
        self.broth = Broth.VEGETABLE  # Changes broth type

    def get_ingredient_names(self) -> Set[str]:
        """
        Retrieves a set of all ingredient names used in the recipe.
        """
        ingredients = self.aromatics | self.vegetables | self.meats | self.starches | self.garnishes
        return {ingredient.name for ingredient in ingredients} | {self.broth.name.capitalize() + " Broth"}
```

**Explanation:**

1. **`make_vegetarian` Method:**
   - **Purpose:** Converts the recipe to a vegetarian version.
   - **Actions:**
     - `self.meats.clear()`: Removes all meat ingredients.
     - `self.broth = Broth.VEGETABLE`: Changes the broth type to vegetable.

2. **`get_ingredient_names` Method:**
   - **Purpose:** Retrieves all ingredient names for easy verification.
   - **Actions:**
     - Combines all ingredient sets using the `|` operator.
     - Extracts the `name` attribute from each `Ingredient`.
     - Adds the broth type to the set of ingredient names.

### **Step 2: Using the Methods**

```python
from copy import deepcopy

# Create a deep copy to avoid modifying the original recipe
vegetarian_soup = deepcopy(chicken_noodle_soup)

# Make the copy vegetarian
vegetarian_soup.make_vegetarian()

# Retrieve ingredient names
ingredient_names = vegetarian_soup.get_ingredient_names()
print(ingredient_names)
```

**Output:**
```
{'Garlic', 'Pepper', 'Carrots', 'Celery', 'Onions', 'Noodles', 'Parsley', 'Vegetable Broth'}
```

**Benefits:**
- **Encapsulation:** Encapsulates behavior related to the recipe within the class.
- **Reusability:** Methods can be reused across different instances without rewriting code.
- **Maintainability:** Changes to behavior are localized within the class, making updates easier.

## 🔄 Immutability with `frozen=True`

Immutability ensures that once an instance of a data class is created, its fields cannot be altered. This is crucial for maintaining data integrity, especially in multi-threaded environments or when using instances as dictionary keys.

### **Defining an Immutable Data Class**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP
```

**Explanation:**
- **`frozen=True`:** Makes the instance immutable. Any attempt to modify its fields will raise a `FrozenInstanceError`.

### **Attempting to Modify an Immutable Instance**

```python
# Create an Ingredient instance
garlic = Ingredient(name="Garlic", amount=2, units=ImperialMeasure.TEASPOON)

# Attempt to modify the 'amount'
garlic.amount = 3  # Raises dataclasses.FrozenInstanceError
```

**Output:**
```
dataclasses.FrozenInstanceError: cannot assign to field 'amount'
```

**Benefits:**
- **Data Integrity:** Prevents accidental or intentional modifications to critical data.
- **Hashability:** Immutable instances can be hashed, allowing them to be used as keys in dictionaries or elements in sets.
- **Thread Safety:** Eliminates the need for synchronization mechanisms when accessing shared data across threads.

### **Caveats:**
- **Nested Mutability:** While the outer instance is immutable, if it contains mutable fields (like lists or sets), those can still be modified.
  
  ```python
  # Assuming 'aromatics' is a mutable set
  chicken_noodle_soup.aromatics.add(Ingredient(name="Pepper", amount=1, units=ImperialMeasure.TABLESPOON))
  # This is allowed even if Recipe is frozen, because 'aromatics' is a mutable set
  ```

- **Final Fields:** To enforce deeper immutability, ensure that all fields are themselves immutable or use immutable collections.

## 🔢 Equality and Comparison

Data classes come with built-in support for equality (`==`, `!=`) and, optionally, comparison operations (`<`, `>`, `<=`, `>=`).

### **Equality (`__eq__`)**

By default, data classes generate the `__eq__` method, allowing comparison of instances based on their field values.

**Example:**

```python
from dataclasses import dataclass

@dataclass(eq=True)
class Point:
    x: int
    y: int

point1 = Point(x=1, y=2)
point2 = Point(x=1, y=2)
point3 = Point(x=3, y=4)

print(point1 == point2)  # Output: True
print(point1 == point3)  # Output: False
```

**Explanation:**
- **`eq=True` (default):** Generates the `__eq__` method.
- **Comparison:** Instances are considered equal if all their fields are equal.

### **Comparison Operators (`__lt__`, `__le__`, `__gt__`, `__ge__`)**

Data classes can also generate ordering methods if specified. This allows instances to be compared using relational operators.

**Example:**

```python
from dataclasses import dataclass

@dataclass(order=True)
class NutritionInfo:
    calories: int
    fat: int
    carbohydrates: int

nutrition1 = NutritionInfo(calories=100, fat=1, carbohydrates=3)
nutrition2 = NutritionInfo(calories=50, fat=6, carbohydrates=4)
nutrition3 = NutritionInfo(calories=125, fat=12, carbohydrates=3)

nutritionals = [nutrition1, nutrition2, nutrition3]
sorted_nutritionals = sorted(nutritionals)

for n in sorted_nutritionals:
    print(n)
```

**Output:**
```
NutritionInfo(calories=50, fat=6, carbohydrates=4)
NutritionInfo(calories=100, fat=1, carbohydrates=3)
NutritionInfo(calories=125, fat=12, carbohydrates=3)
```

**Explanation:**
- **`order=True`:** Generates comparison methods based on the order of fields defined.
- **Sorting:** Instances are compared field by field in the order they are defined.

### **Customizing Comparison Behavior**

If the default field-wise comparison doesn't suit your needs, you can override the comparison methods.

**Example: Sorting by Fat, Then Carbohydrates, Then Calories**

```python
from dataclasses import dataclass

@dataclass(eq=True)
class NutritionInfo:
    calories: int
    fat: int
    carbohydrates: int

    def __lt__(self, other) -> bool:
        return (self.fat, self.carbohydrates, self.calories) < (other.fat, other.carbohydrates, other.calories)

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __gt__(self, other) -> bool:
        return not self <= other

    def __ge__(self, other) -> bool:
        return not self < other

nutrition1 = NutritionInfo(calories=100, fat=1, carbohydrates=3)
nutrition2 = NutritionInfo(calories=50, fat=6, carbohydrates=4)
nutrition3 = NutritionInfo(calories=125, fat=12, carbohydrates=3)

nutritionals = [nutrition1, nutrition2, nutrition3]
sorted_nutritionals = sorted(nutritionals)

for n in sorted_nutritionals:
    print(n)
```

**Output:**
```
NutritionInfo(calories=100, fat=1, carbohydrates=3)
NutritionInfo(calories=50, fat=6, carbohydrates=4)
NutritionInfo(calories=125, fat=12, carbohydrates=3)
```

**Caveats:**
- **Conflicting with `order=True`:** If you manually override comparison methods, avoid setting `order=True` to prevent `ValueError`.

## 🔒 Ensuring Uniqueness with `@unique`

Sometimes, you may inadvertently assign the same value to multiple Enum members, leading to aliases. While aliases can be useful, they might introduce confusion or bugs. Python provides the `@unique` decorator to enforce that all Enum members have distinct values.

### **Using `@unique` Decorator**

```python
from enum import Enum, auto, unique

@unique
class MotherSauce(Enum):
    BECHAMEL = auto()
    VELOUTE = auto()
    ESPAGNOLE = auto()
    TOMATO = auto()
    HOLLANDAISE = auto()
    # Accidental duplicate
    BECHAMEL_DUPLICATE = auto()  # Raises ValueError
```

**Explanation:**
- **`@unique`:** Ensures that all Enum members have unique values.
- **Duplicate Assignment:** Attempting to assign a duplicate value (`BECHAMEL_DUPLICATE`) raises a `ValueError`.

**Output:**
```
ValueError: duplicate values found in <enum 'MotherSauce'>: BECHAMEL_DUPLICATE -> BECHAMEL
```

### **Without `@unique`: Allowing Aliases**

By default, Python Enums allow multiple members to share the same value, creating aliases. This does not raise an error unless `@unique` is used.

**Example:**

```python
from enum import Enum, auto

class MotherSauce(Enum):
    BECHAMEL = auto()
    VELOUTE = auto()
    ESPAGNOLE = auto()
    TOMATO = auto()
    HOLLANDAISE = auto()
    BECHAMEL_ALIAS = BECHAMEL  # Alias

# Usage
print(list(MotherSauce))
```

**Output:**
```
[<MotherSauce.BECHAMEL: 1>, <MotherSauce.VELOUTE: 2>, <MotherSauce.ESPAGNOLE: 3>, <MotherSauce.TOMATO: 4>, <MotherSauce.HOLLANDAISE: 5>, <MotherSauce.BECHAMEL_ALIAS: 1>]
```

**Explanation:**
- **`BECHAMEL_ALIAS`:** Shares the same value as `BECHAMEL` without raising an error.

### **Caveats:**
- **Unintentional Aliases:** Without `@unique`, accidental duplicates can lead to unexpected behavior.
- **Intentional Aliases:** If you intentionally want multiple names for the same value, omit `@unique`.

## 💡 Best Practices for Using Data Classes

To maximize the benefits of data classes and maintain clean, efficient, and bug-free codebases, adhere to the following best practices:

### 1. **Use `auto()` for Value Assignment Whenever Possible 🔄🛠️**

**Why:**
- Reduces manual errors and ensures unique, sequential values without extra effort.

**When Not to Use:**
- When specific values are required for business logic or interoperability with other systems.

**Example:**

```python
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()
```

### 2. **Override `_generate_next_value_()` for Customized Value Generation 🛠️✨**

**Why:**
- Allows you to assign meaningful or domain-specific values automatically.

**Use Cases:**
- When Enum member values need to be more descriptive or align with external data.

**Example:**

```python
from enum import Enum, auto

class PaymentStatus(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()
    
    PENDING = auto()
    COMPLETED = auto()
    FAILED = auto()

# Usage
print(list(PaymentStatus))
# Output: [<PaymentStatus.PENDING: 'pending'>, <PaymentStatus.COMPLETED: 'completed'>, <PaymentStatus.FAILED: 'failed'>]
```

### 3. **Prefer `Enum` Over `IntEnum` for Type Safety 🔒🐍**

**Why:**
- Avoids unintended behavior and maintains strong type safety by preventing implicit integer comparisons.

**Exception:**
- Use `IntEnum` only when interfacing with systems or protocols that require integer values.

**Example:**

```python
from enum import Enum

class DeviceStatus(Enum):
    OFF = 0
    ON = 1
    STANDBY = 2
```

### 4. **Utilize `Flag` and `IntFlag` for Bitwise Combinations ⚙️🔢**

**Why:**
- Efficiently represents combinations of Enum members, such as multiple options or states.

**Use Cases:**
- Feature flags, permission systems, or any scenario requiring multiple concurrent states.

**Example:**

```python
from enum import Flag, auto

class Permissions(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

# Assigning multiple permissions
user_permissions = Permissions.READ | Permissions.WRITE

# Checking permissions
if Permissions.READ in user_permissions:
    print("User can read.")

if Permissions.EXECUTE not in user_permissions:
    print("User cannot execute.")
```

**Output:**
```
User can read.
User cannot execute.
```

### 5. **Ensure Uniqueness with `@unique` When Necessary 🔒✅**

**Why:**
- Prevents accidental value duplication, enhancing Enum reliability.

**When to Use:**
- For critical Enums where each member must represent a distinct value.

**Example:**

```python
from enum import Enum, auto, unique

@unique
class CountryCode(Enum):
    USA = "US"
    CANADA = "CA"
    MEXICO = "MX"
```

### 6. **Document Enums and Data Classes Clearly for Better Maintainability 📝📚**

**Why:**
- Enhances code readability and helps team members understand the purpose and usage of each Enum and data class.

**How:**
- Use docstrings and comments to explain the role of each Enum and its members.

**Example:**

```python
from enum import Enum, auto

class Broth(Enum):
    """
    Represents the type of broth used in a recipe.
    """
    VEGETABLE = auto()
    CHICKEN = auto()
    BEEF = auto()
    FISH = auto()
```

```python
from dataclasses import dataclass
from typing import Set

@dataclass
class Recipe:
    """
    Represents a soup recipe with categorized ingredients and cooking time.
    """
    aromatics: Set[Ingredient]
    broth: Broth
    vegetables: Set[Ingredient]
    meats: Set[Ingredient]
    starches: Set[Ingredient]
    garnishes: Set[Ingredient]
    time_to_cook: datetime.timedelta
```

### 7. **Leverage Enum Methods and Data Class Methods for Additional Functionality 🛠️🔗**

**Why:**
- Encapsulates behavior related to data, enhancing reusability and maintainability.

**Use Cases:**
- Validations, formatted representations, or business logic tied to Enum members or data class instances.

**Example:**

```python
from dataclasses import dataclass

@dataclass
class Recipe:
    aromatics: Set[Ingredient]
    broth: Broth
    vegetables: Set[Ingredient]
    meats: Set[Ingredient]
    starches: Set[Ingredient]
    garnishes: Set[Ingredient]
    time_to_cook: datetime.timedelta

    def make_vegetarian(self):
        """
        Converts the recipe to a vegetarian version by removing meats and changing broth to vegetable.
        """
        self.meats.clear()
        self.broth = Broth.VEGETABLE

    def get_ingredient_names(self) -> Set[str]:
        """
        Returns a set of all ingredient names in the recipe, including the broth type.
        """
        ingredients = self.aromatics | self.vegetables | self.meats | self.starches | self.garnishes
        return {ingredient.name for ingredient in ingredients} | {self.broth.name.capitalize() + " Broth"}
```

### 8. **Avoid Overusing `Any` in Enums and Data Classes 🛑❌**

**Why:**
- Using `Any` defeats the purpose of type safety and clarity provided by Enums and data classes.

**Best Practice:**
- Define Enums and data classes with specific types and avoid generic or ambiguous values.

**Example of What to Avoid:**

```python
from enum import Enum
from typing import Any

class FlexibleEnum(Enum):
    ITEM1 = "Value1"
    ITEM2 = 2
    ITEM3 = Any  # ❌ Avoid using Any
```

**Improved Version:**

```python
from enum import Enum

class ProductCategory(Enum):
    ELECTRONICS = "Electronics"
    FASHION = "Fashion"
    GROCERY = "Grocery"
```

## 🎯 Conclusion 🎯

**Data classes** in Python are powerful tools that simplify the creation of classes meant primarily for storing data. By leveraging features like automatic method generation, type annotations, immutability, and nesting, you can build robust, readable, and maintainable codebases with ease.

### **Key Takeaways:**

1. **Simplify Data Storage:**
   - Use `@dataclass` to auto-generate essential methods, reducing boilerplate.

2. **Enforce Type Safety:**
   - Clearly define types for each field, minimizing type-related errors.

3. **Enhance Immutability:**
   - Use `frozen=True` to create immutable instances, ensuring data integrity.

4. **Model Complex Relationships:**
   - Nest data classes and use Enums to represent intricate relationships and hierarchies.

5. **Encapsulate Behavior:**
   - Add methods to data classes to encapsulate related behaviors, promoting reusability.

6. **Ensure Uniqueness:**
   - Apply the `@unique` decorator to Enums when distinct values are critical.

7. **Maintain Clarity:**
   - Document your data classes and Enums to enhance understanding and collaboration.

### **Final Thoughts:**

Embracing data classes elevates your Python programming by providing a structured, efficient, and type-safe way to manage data. Whether you're handling simple data structures or complex relational models, data classes offer the flexibility and power needed to build scalable and maintainable applications.

**Happy Coding!** 🚀😊🎉

## 🌈 Additional Resources 🌈

To further enhance your understanding and mastery of data classes in Python, explore the following **valuable resources**:

- [**Python Official Documentation on `dataclasses`**](https://docs.python.org/3/library/dataclasses.html) 📘
- [**PEP 557 – Data Classes**](https://www.python.org/dev/peps/pep-0557/) 📄✨
- [**Real Python: Using Python Data Classes**](https://realpython.com/python-data-classes/) 🛠️🔍
- [**Mypy Official Documentation on Data Classes**](https://mypy.readthedocs.io/en/stable/data_classes.html) 📈🔧
- [**Type Checking in Python: Data Classes and Beyond**](https://www.typing.io/docs/dataclasses) 📚🧠
- [**Data Classes in Python Tutorial by Programiz**](https://www.programiz.com/python-programming/dataclass) 📄🔧

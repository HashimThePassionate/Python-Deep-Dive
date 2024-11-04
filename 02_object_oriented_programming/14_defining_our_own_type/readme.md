# 🛠️ Defining Custom Types in Python 🚀

Welcome to this **comprehensive guide** on creating custom types in **Python 3.12**! 🎉 Defining your own types enhances code **readability**, **safety**, and **maintainability** by setting clear expectations for your data. Python's type system is flexible, allowing you to create precise and expressive types that make your codebase more robust. Let’s explore how to define and use custom types, from simple aliases to advanced `TypedDict` and `NewType` structures! 🐍✨


## 📚 Table of Contents

- [🛠️ Defining Custom Types in Python 3.12 🚀](#️-defining-custom-types-in-python-312-)
  - [📚 Table of Contents](#-table-of-contents)
  - [🔍 Why Define Custom Types?](#-why-define-custom-types)
  - [📝 Basic Type Aliases](#-basic-type-aliases)
    - [🔧 How to Define a Type Alias](#-how-to-define-a-type-alias)
    - [✨ Usage](#-usage)
  - [🔧 Using `NewType` for Unique Type Distinctions](#-using-newtype-for-unique-type-distinctions)
    - [🔧 How to Use `NewType`](#-how-to-use-newtype)
    - [✨ Usage](#-usage-1)
  - [📋 Defining `TypedDict` for Structured Data](#-defining-typeddict-for-structured-data)
    - [🔧 How to Use `TypedDict`](#-how-to-use-typeddict)
    - [✨ Usage](#-usage-2)
  - [🛠️ Customizing with Protocols](#️-customizing-with-protocols)
    - [🔧 How to Use Protocols](#-how-to-use-protocols)
    - [✨ Usage](#-usage-3)
  - [🏆 Example Scenarios for Custom Types](#-example-scenarios-for-custom-types)
    - [Scenario 1: E-commerce Application](#scenario-1-e-commerce-application)
    - [Scenario 2: Processing User Profiles](#scenario-2-processing-user-profiles)
    - [Scenario 3: Robotics Control System](#scenario-3-robotics-control-system)
  - [🎯 Conclusion](#-conclusion)
  - [🌈 Additional Resources](#-additional-resources)


## 🔍 Why Define Custom Types?

Python’s **type annotations** enhance code clarity, but defining **custom types** goes a step further. Custom types:

- **Increase Readability**: By providing meaningful names, they clarify the intent of your data.
- **Improve Code Safety**: Type checkers like **Mypy** verify that data matches expected types.
- **Simplify Refactoring**: If a type changes, only the type definition needs updating, not every instance.

Defining custom types can benefit **any project** by making data structures more expressive and preventing errors. Let’s dive into some popular ways to define custom types in Python 3.12! 🚀


## 📝 Basic Type Aliases

A **Type Alias** is a simple way to assign a more descriptive name to an existing type. This can make complex data types easier to understand and work with. 🎨

### 🔧 How to Define a Type Alias

In Python, you define a type alias by assigning an existing type to a new name.

```python
from typing import List, Tuple, Union

# Define a type alias
Coordinate = Tuple[float, float]
Color = Union[str, Tuple[int, int, int]]
Points = List[Coordinate]
```

### ✨ Usage

Using type aliases makes your code more readable and self-documenting.

```python
# Example usage of type aliases
location: Coordinate = (52.5200, 13.4050)  # Tuple of floats representing latitude and longitude
color: Color = (255, 0, 0)  # RGB color as a tuple of integers
route: Points = [(34.0522, -118.2437), (36.1699, -115.1398)]  # List of coordinates
```

**Benefits**:
- **Clarity**: `Coordinate` is more descriptive than a raw tuple `(float, float)`.
- **Consistency**: Any change to `Coordinate` only needs to be made in one place.


## 🔧 Using `NewType` for Unique Type Distinctions

**`NewType`** creates a **distinct type** that behaves like an existing type but is treated as a unique type by type checkers. This is helpful when you want to distinguish between values with the same underlying type but different meanings. 🧩

### 🔧 How to Use `NewType`

To use `NewType`, import it from the `typing` module and create a new type based on an existing one.

```python
from typing import NewType

# Define custom types using NewType
UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)
```

### ✨ Usage

`NewType` enforces that you can’t interchange values of `UserId` and `OrderId`, even though both are integers.

```python
def get_user(user_id: UserId) -> str:
    return f"User: {user_id}"

def get_order(order_id: OrderId) -> str:
    return f"Order: {order_id}"

user_id = UserId(123)
order_id = OrderId(456)

print(get_user(user_id))  # ✅ Works fine
print(get_order(order_id))  # ✅ Works fine
# print(get_user(order_id))  # ❌ Type error if type checker is used
```

**Benefits**:
- **Type Safety**: Prevents accidental interchange of values with similar data types but different meanings.
- **Improves Documentation**: Specifies intent more clearly than raw data types.


## 📋 Defining `TypedDict` for Structured Data

A **`TypedDict`** allows you to define a **dictionary structure with specific key-value types**. This is useful when working with JSON-like data where each key has a known type. 📋

### 🔧 How to Use `TypedDict`

To use `TypedDict`, import it from the `typing` module and define the keys and their types.

```python
from typing import TypedDict

# Define a TypedDict
class UserProfile(TypedDict):
    username: str
    age: int
    email: str
    location: Tuple[float, float]  # Use previously defined Coordinate type
```

### ✨ Usage

`TypedDict` enables type-checking for dictionaries that have specific structures.

```python
def print_user_profile(user: UserProfile) -> None:
    print(f"Username: {user['username']}")
    print(f"Age: {user['age']}")
    print(f"Email: {user['email']}")
    print(f"Location: {user['location']}")

# Example usage
profile: UserProfile = {
    "username": "johndoe",
    "age": 30,
    "email": "johndoe@example.com",
    "location": (40.7128, -74.0060)
}

print_user_profile(profile)
```

**Benefits**:
- **Structured Type Checking**: Ensures that each key has the correct type, making code more reliable.
- **Improves Readability**: Clearly documents the structure of complex dictionary-like data.


## 🛠️ Customizing with Protocols

Protocols are **interfaces** that define expected methods and properties without specifying an implementation. This is helpful when you want to specify that a class must have certain methods to be used with your code. 🛠️

### 🔧 How to Use Protocols

To use a Protocol, import it from the `typing` module, define your protocol, and specify the required methods.

```python
from typing import Protocol

# Define a protocol
class Flyable(Protocol):
    def fly(self) -> None:
        ...

class Bird:
    def fly(self) -> None:
        print("The bird is flying!")

class Airplane:
    def fly(self) -> None:
        print("The airplane is flying!")

def make_it_fly(flyable: Flyable) -> None:
    flyable.fly()
```

### ✨ Usage

Protocols allow you to enforce that a class implements specific methods without needing a shared base class.

```python
bird = Bird()
plane = Airplane()

make_it_fly(bird)  # ✅ Works fine
make_it_fly(plane)  # ✅ Works fine
```

**Benefits**:
- **Flexible Type Checking**: Ensures that objects meet a certain interface without requiring inheritance.
- **Promotes Loose Coupling**: Classes don’t need a common parent class, just the required methods.


## 🏆 Example Scenarios for Custom Types

Let’s look at a few practical examples to see how custom types can simplify real-world problems. 🎉

### Scenario 1: E-commerce Application

In an e-commerce application, you might use **NewType** for distinct ID types, ensuring **type safety** for each unique identifier.

```python
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

user_id = UserId(101)
product_id = ProductId(202)

# Functions accepting specific IDs
def get_user_data(user_id: UserId) -> str:
    return f"User data for user {user_id}"

def get_product_data(product_id: ProductId) -> str:
    return f"Product data for product {product_id}"

print(get_user_data(user_id))  # Works fine
# print(get_user_data(product_id))  # ❌ Type error if checked
```

### Scenario 2: Processing User Profiles

For handling structured data like user profiles, **TypedDict** can ensure that dictionaries passed to functions contain all the required fields.

```python
from typing import TypedDict, Tuple

class UserProfile(TypedDict):
    name: str
    age: int
    location: Tuple[float, float]

def print_profile(profile: UserProfile) -> None:
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Location: {profile['location']}")

user_profile: UserProfile = {
    "name": "Jane Doe",
    "age": 25,
    "location": (40.7128, -74.0060)
}

print_profile(user_profile)
```

### Scenario 3: Robotics Control System



For a robotics control system where any object that can **move** must implement a `move` method, you might use **Protocols** to define the expected interface without enforcing a specific base class.

```python
from typing import Protocol

class Movable(Protocol):
    def move(self) -> None:
        ...

class Robot:
    def move(self) -> None:
        print("Robot moving!")

class Drone:
    def move(self) -> None:
        print("Drone moving!")

def initiate_movement(entity: Movable) -> None:
    entity.move()

robot = Robot()
drone = Drone()

initiate_movement(robot)  # Works fine
initiate_movement(drone)  # Works fine
```


## 🎯 Conclusion

Defining custom types in Python 3.12 opens up powerful ways to improve **type safety**, **clarity**, and **maintainability** in your code! Whether you’re renaming complex types with **Type Aliases**, enforcing unique identities with **NewType**, creating structured dictionaries with **TypedDict**, or defining flexible interfaces with **Protocols**, these tools allow you to write more expressive and error-resistant Python code. 🐍✨

Start defining custom types in your projects today and experience the benefits of a more readable, robust codebase! 🚀


## 🌈 Additional Resources

- [**Python Official Documentation on Type Hints**](https://docs.python.org/3/library/typing.html) 📖
- [**Mypy Documentation**](http://mypy-lang.org/) 📘
- [**PEP 484 – Type Hints**](https://www.python.org/dev/peps/pep-0484/) 📄
- [**PEP 544 – Protocols: Structural Subtyping**](https://www.python.org/dev/peps/pep-0544/) 🦆


# 📦✨ Encapsulate What Varies Principle 📚🔍

Welcome to a **comprehensive and professional** guide on the **Encapsulate What Varies** principle! 🛠️ This principle is essential for writing flexible, maintainable, and high-quality code, even as requirements and technologies evolve.Let’s get started! 🚀💡


## 📑🗂️ Table of Contents 📋📌

- [📦✨ Encapsulate What Varies Principle 📚🔍](#-encapsulate-what-varies-principle-)
  - [📑🗂️ Table of Contents 📋📌](#️-table-of-contents-)
  - [🔰 Introduction](#-introduction)
  - [🔍 Understanding the Principle](#-understanding-the-principle)
    - [🤔 What Does It Mean?](#-what-does-it-mean)
    - [🎯 Benefits](#-benefits)
  - [🛠️ Techniques for Encapsulation](#️-techniques-for-encapsulation)
    - [🌀 Polymorphism](#-polymorphism)
    - [🔑 Getters and Setters](#-getters-and-setters)
    - [🏡 The Property Technique](#-the-property-technique)
  - [💡 Practical Examples](#-practical-examples)
    - [💳 Using Polymorphism](#-using-polymorphism)
    - [🔵 Using a Property](#-using-a-property)
  - [🎓 Conclusion](#-conclusion)


## 🔰 Introduction

The **Encapsulate What Varies** principle is a fundamental concept in software development aimed at enhancing code flexibility and maintainability. 🧩 It emphasizes isolating the parts of your code that are likely to change, thereby minimizing the impact of these changes on the overall system. This approach leads to more robust and adaptable applications, capable of evolving alongside shifting requirements and technological advancements. 🛠️💪


## 🔍 Understanding the Principle

### 🤔 What Does It Mean?

The **Encapsulate What Varies** principle focuses on identifying and isolating the aspects of your code that are subject to change. 🛡️ By creating boundaries around these variable elements, you prevent changes from causing widespread modifications throughout your codebase. This isolation facilitates easier updates and reduces the risk of introducing bugs when adjustments are necessary. 💡🔄

**Key Points:**
- 🧱 **Isolation of Change-Prone Elements**: Identify components that are likely to vary.
- 🛡️ **Protective Barrier**: Shield the rest of your code from these variable parts.
- 🌊 **Minimized Ripple Effect**: Changes in one area do not necessitate widespread modifications.

### 🎯 Benefits

Adopting the **Encapsulate What Varies** principle offers several significant advantages:

1. 🛠️🔧 **Ease of Maintenance**
   - ✂️ **Simplified Modifications**: Changes are confined to encapsulated parts, reducing the risk of introducing bugs elsewhere.
   - 🔄 **Streamlined Updates**: Easier to understand and update specific components without delving into the entire codebase.

2. 🔄🧩 **Enhanced Flexibility**
   - 🏗️ **Modular Architecture**: Encapsulated components can be easily swapped or extended, allowing your architecture to adapt to new requirements or technologies.
   - 📏 **Scalable Design**: Facilitates the growth and scaling of your application by making it adaptable to future changes.

3. 📖👓 **Improved Readability**
   - 🗂️ **Organized Codebase**: Isolating varying elements leads to a more structured and organized codebase.
   - 🧠 **Easier Understanding**: Clear separation of concerns makes the code easier to read and comprehend for developers.


## 🛠️ Techniques for Encapsulation

To effectively encapsulate what varies, several key techniques can be employed, particularly in Python. These techniques promote data hiding and expose only the necessary functionalities, enhancing the overall design and maintainability of your code. Below are the primary methods:

### 🌀 Polymorphism

**Polymorphism** is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. 🧩 This enables a single interface to represent different types, fostering flexibility and reusability in your code.

**Benefits of Polymorphism:**
- 🎨 **Elegant Design Patterns**: Facilitates the implementation of design patterns like the strategy pattern.
- 🧼 **Maintainable Code**: Promotes clean and maintainable code by allowing different implementations to coexist seamlessly.

**Example Use Case:**
Imagine a payment processing system where the payment method can vary (e.g., Credit Card, PayPal). Polymorphism allows you to handle different payment methods uniformly through a common interface.


### 🔑 Getters and Setters

**Getters and Setters** are methods that allow controlled access to an object's attributes. 🛡️

- 👁️ **Getters**: Allow reading the values of attributes.
- ✏️ **Setters**: Enable modifying the values of attributes.

**Advantages:**
- 🔒 **Controlled Access**: Add validation logic or side effects (e.g., logging) when accessing or modifying attributes.
- 🛡️ **Data Protection**: Protect the internal state of an object from unintended or harmful changes.

**Use Case:**
When you have complex attributes derived from other instance variables, getters and setters ensure that any changes to these attributes are managed correctly and safely.


### 🏡 The Property Technique

Python offers a more elegant approach known as the **Property Technique** to complement getters and setters. 🏷️ This built-in feature allows you to convert attribute access into method calls seamlessly, aligning with Python’s design philosophy for clean and readable code.

**How It Works:**
- 📜 **@property Decorator**: Defines a method that is automatically invoked when an attribute is accessed, acting as a getter.
- 🔄 **@attribute_name.setter Decorator**: Defines a method that is invoked when attempting to change the value of an attribute, acting as a setter.

**Benefits:**
- 🔗 **Seamless Integration**: Attribute access and modification appear as regular attribute operations, hiding the underlying method calls.
- 🛡️ **Enhanced Encapsulation**: Embed validation or other actions directly within these methods without explicitly defining separate getter and setter methods.

**Example:**
Creating a property for a class attribute ensures that any access or modification to the attribute is controlled and validated, maintaining the integrity of the object's state.


## 💡 Practical Examples

Let's explore practical examples to understand how the **Encapsulate What Varies** principle can be implemented using the techniques discussed.

### 💳 Using Polymorphism

**Scenario:**
You have a payment system that can handle different payment methods like Credit Card and PayPal. 🛒

**Step-by-Step Implementation:**

1. **Create a Base Class** 🏗️:

   Start by defining a base class `PaymentBase` that outlines the structure for payment methods. This class includes an initializer to set the payment amount and a `process_payment` method that will be overridden by subclasses.

   ```python
   class PaymentBase:
       def __init__(self, amount: int) -> None:
           self.amount: int = amount

       def process_payment(self) -> None:
           pass
   ```

   **Explanation:**
   - `__init__`: Initializes the payment amount.
   - `process_payment`: A placeholder method meant to be overridden by subclasses.

2. **Create Subclasses** 🛠️:

   Define subclasses `CreditCard` and `PayPal` that inherit from `PaymentBase`. Each subclass implements its own version of the `process_payment` method.

   ```python
   class CreditCard(PaymentBase):
       def process_payment(self) -> None:
           print(f"Credit card payment: {self.amount}")

   class PayPal(PaymentBase):
       def process_payment(self) -> None:
           print(f"PayPal payment: {self.amount}")
   ```

   **Explanation:**
   - `CreditCard.process_payment`: Processes a credit card payment and prints a confirmation message.
   - `PayPal.process_payment`: Processes a PayPal payment and prints a confirmation message.

3. **Use the Classes** 🧪:

   Instantiate objects of each payment method and call their `process_payment` methods to see polymorphism in action.

   ```python
   if __name__ == "__main__":
       payments: list[PaymentBase] = [CreditCard(100), PayPal(200)]
       for payment in payments:
           payment.process_payment()
   ```

   **Explanation:**
   - Creates a list `payments` containing instances of `CreditCard` and `PayPal`.
   - Iterates over each payment object and calls the `process_payment` method, demonstrating polymorphism.

**Complete Code (`encapsulate.py`):**

```python
class PaymentBase:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount

    def process_payment(self) -> None:
        pass

class CreditCard(PaymentBase):
    def process_payment(self) -> None:
        print(f"Credit card payment: {self.amount}")

class PayPal(PaymentBase):
    def process_payment(self) -> None:
        print(f"PayPal payment: {self.amount}")

if __name__ == "__main__":
    payments: list[PaymentBase] = [CreditCard(100), PayPal(200)]
    for payment in payments:
        payment.process_payment()
```

**Running the Code:**

Execute the following command to test the payment processing system:

```bash
python encapsulate.py
```

**Expected Output:**

```
Credit card payment: 100
PayPal payment: 200
```

**Detailed Explanation:**

- **Instantiation:**
  - `CreditCard(100)`: Creates a `CreditCard` object with an amount of 100.
  - `PayPal(200)`: Creates a `PayPal` object with an amount of 200.
  
- **Processing Payments:**
  - The `for` loop iterates over each payment object in the `payments` list.
  - `payment.process_payment()`: Calls the appropriate `process_payment` method based on the object's class (`CreditCard` or `PayPal`).

**Benefits Demonstrated:**
- 🔄 **Flexibility:** Easily add new payment methods by creating new subclasses without modifying existing code.
- 🧼 **Maintainability:** Changes in payment processing logic for one method do not affect others.


### 🔵 Using a Property

**Scenario:**
You have a `Circle` class, and you want to ensure that the radius is always positive. 📐

**Step-by-Step Implementation:**

1. **Create the Class** 🏗️:

   Define the `Circle` class with an initializer that sets the radius. The radius is stored in a protected attribute `_radius`.

   ```python
   class Circle:
       def __init__(self, radius: int) -> None:
           self._radius: int = radius
   ```

   **Explanation:**
   - `__init__`: Initializes the `_radius` attribute with the provided value.

2. **Add a Getter** 👁️:

   Use the `@property` decorator to create a getter method for the `radius` attribute.

   ```python
       @property
       def radius(self) -> int:
           return self._radius
   ```

   **Explanation:**
   - `@property`: Turns the `radius` method into a getter.
   - `radius`: Returns the value of `_radius`.

3. **Add a Setter** ✏️:

   Use the `@radius.setter` decorator to create a setter method that validates the radius before setting it.

   ```python
       @radius.setter
       def radius(self, value: int) -> None:
           if value < 0:
               raise ValueError("Radius cannot be negative!")
           self._radius = value
   ```

   **Explanation:**
   - `@radius.setter`: Turns the `radius` method into a setter.
   - `radius`: Validates the new value to ensure it's non-negative before setting `_radius`.

4. **Use the Class** 🧪:

   Create an instance of `Circle`, print its initial radius, modify the radius, and print the updated radius. Additionally, attempt to set a negative radius to demonstrate error handling.

   ```python
   if __name__ == "__main__":
       circle: Circle = Circle(10)
       print(f"Initial radius: {circle.radius}")
       circle.radius = 15
       print(f"New radius: {circle.radius}")
       
       try:
           circle.radius = -5
       except ValueError as e:
           print(e)
           print(f"Current radius: {circle.radius}")
   ```

   **Explanation:**
   - Instantiates a `Circle` object with an initial radius of 10.
   - Prints the initial radius using the getter.
   - Sets a new radius of 15 using the setter.
   - Prints the updated radius using the getter.
   - Attempts to set the radius to -5, which triggers the `ValueError`.
   - Catches the exception and prints the error message and the current valid radius.

**Complete Code (`encapsulate_bis.py`):**

```python
class Circle:
    def __init__(self, radius: int) -> None:
        self._radius: int = radius

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value: int) -> None:
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value

if __name__ == "__main__":
    circle: Circle = Circle(10)
    print(f"Initial radius: {circle.radius}")
    circle.radius = 15
    print(f"New radius: {circle.radius}")
    
    try:
        circle.radius = -5
    except ValueError as e:
        print(e)
        print(f"Current radius: {circle.radius}")
```

**Running the Code:**

Execute the following command to test the `Circle` class:

```bash
python encapsulate_bis.py
```

**Expected Output:**

```
Initial radius: 10
New radius: 15
Radius cannot be negative!
Current radius: 15
```

**Detailed Explanation:**

- **Instantiation:**
  - `Circle(10)`: Creates a `Circle` object with an initial radius of 10.
  
- **Getting the Radius:**
  - `circle.radius`: Calls the getter method to retrieve the current radius (`10`).

- **Setting the Radius:**
  - `circle.radius = 15`: Calls the setter method to update the radius to `15`. The setter validates that `15` is non-negative before setting `_radius`.
  
- **Validation with Try-Except:**
  - `circle.radius = -5`: Attempts to set the radius to `-5`, which violates the validation rule.
  - `except ValueError as e`: Catches the `ValueError` raised by the setter.
  - `print(e)`: Prints the error message `"Radius cannot be negative!"`.
  - `print(f"Current radius: {circle.radius}")`: Prints the current valid radius (`15`), demonstrating that the invalid change was not applied.

**Benefits Demonstrated:**
- 📐 **Data Protection:** Prevents invalid states by ensuring the radius cannot be negative.
- 🛡️ **Encapsulation:** Hides the internal representation (`_radius`) and provides controlled access through properties.
- 🔄 **Error Handling:** Ensures that invalid operations are gracefully handled without breaking the application.


## 🎓 Conclusion

The **Encapsulate What Varies** principle is pivotal for building flexible, maintainable, and robust software systems. 🧩 By isolating the parts of your code that are prone to change and encapsulating them using techniques like polymorphism, getters and setters, and the property technique, you significantly enhance your code's adaptability and readability. 🛠️✨

Implementing this principle not only simplifies maintenance and updates but also fosters a cleaner and more organized codebase, ultimately leading to higher-quality software solutions. Embrace encapsulation to ensure your applications can gracefully adapt to the evolving landscape of software development. 🌟💼


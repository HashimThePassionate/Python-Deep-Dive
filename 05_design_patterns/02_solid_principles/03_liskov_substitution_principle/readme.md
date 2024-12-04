# 🦅 **Liskov Substitution Principle** 🦅
Welcome to the **Liskov Substitution Principle (main)** guide! 🚀 This document breaks down what main is, why it's important, how to apply it, and provides detailed examples to help you understand the concept thoroughly. 💡 All code examples use **static typing** to ensure clarity and reliability. 🛠️✨

---

## 📖 Table of Contents 📖

- [🦅 **Liskov Substitution Principle** 🦅](#-liskov-substitution-principle-)
  - [📖 Table of Contents 📖](#-table-of-contents-)
  - [🔍 Introduction](#-introduction)
  - [💡 What is the Liskov Substitution Principle (main)?](#-what-is-the-liskov-substitution-principle-main)
    - [📌 Key Points of main:](#-key-points-of-main)
  - [🏆 Benefits of main](#-benefits-of-main)
  - [🛠️ How to Apply main](#️-how-to-apply-main)
  - [📂 Example: Bird and Penguin Before main](#-example-bird-and-penguin-before-main)
    - [📝 Explanation:](#-explanation)
    - [⚠️ Issue:](#️-issue)
  - [🔄 Refactoring to Follow main](#-refactoring-to-follow-main)
    - [1. Creating the `Bird` Class](#1-creating-the-bird-class)
    - [📌 Explanation:](#-explanation-1)
    - [2. Creating the `FlyingBird` and `FlightlessBird` Classes](#2-creating-the-flyingbird-and-flightlessbird-classes)
    - [📌 Explanation:](#-explanation-2)
    - [3. Implementing the `make_bird_move` Function](#3-implementing-the-make_bird_move-function)
    - [📌 Explanation:](#-explanation-3)
    - [4. Testing the Refactored Classes](#4-testing-the-refactored-classes)
    - [📌 Explanation:](#-explanation-4)
  - [🧪 Testing the Example](#-testing-the-example)
    - [1. Save the Code](#1-save-the-code)
    - [2. Run the Code](#2-run-the-code)
    - [3. Expected Output](#3-expected-output)
    - [4. Verify Behavior](#4-verify-behavior)
  - [🔗 Conclusion](#-conclusion)

---

## 🔍 Introduction

The **Liskov Substitution Principle (main)** is a fundamental concept in object-oriented programming and design. 🛡️ It ensures that subclasses can stand in for their superclasses without causing unexpected behavior or errors in the program. By following main, your software remains robust, flexible, and easier to maintain. 📈

---

## 💡 What is the Liskov Substitution Principle (main)?

**Liskov Substitution Principle (main)** states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. 🔄 In other words, if you have a function that works with a superclass, it should work just as well with any subclass derived from that superclass. This principle ensures that subclasses enhance or specialize behavior without altering the fundamental expectations set by the superclass. 🏗️

### 📌 Key Points of main:

- **Substitutability**: Subclasses should be able to replace superclasses seamlessly.
- **Behavioral Consistency**: The behavior expected from the superclass should remain unchanged when using a subclass.
- **No Unexpected Side Effects**: Subclasses should not introduce behaviors that violate the expectations set by the superclass.

---

## 🏆 Benefits of main

Implementing main brings several significant advantages to your software projects:

- **🔧 Maintainability**: Ensures that extending classes do not break existing functionality, making the codebase easier to maintain.
- **🛠️ Extensibility**: Allows you to add new features or behaviors through subclasses without modifying existing code.
- **🧪 Testability**: Simplifies testing as subclasses adhere to the same contracts as their superclasses, allowing for consistent and reliable tests.
- **📚 Readability**: Clear and consistent class hierarchies make the code easier to understand and navigate.
- **🚀 Scalability**: Facilitates the growth of your codebase by allowing new functionalities to be added smoothly.

---

## 🛠️ How to Apply main

Following main involves designing your classes and subclasses in a way that maintains behavioral consistency. 🧩 Here are detailed steps to apply main effectively:

1. **🔍 Understand the Superclass**:
   - **Identify Contracts**: Determine the methods and behaviors that the superclass provides.
   - **Define Expectations**: Clearly outline what is expected from any subclass in terms of behavior and functionality.

2. **✅ Adhere to Contracts**:
   - **Implement All Superclass Methods**: Ensure that subclasses implement all methods of the superclass without altering their intended behavior.
   - **Maintain Method Signatures**: Subclasses should not change the method signatures of the superclass.

3. **🚫 Avoid Overriding Methods Incorrectly**:
   - **Consistent Behavior**: When overriding methods, subclasses should not introduce behaviors that contradict the superclass's methods.
   - **Respect Pre-conditions and Post-conditions**: Subclasses should not strengthen pre-conditions or weaken post-conditions of the superclass methods.

4. **🔄 Use Abstractions**:
   - **Interfaces and Abstract Classes**: Define clear contracts using interfaces or abstract classes that subclasses must adhere to.
   - **Promote Polymorphism**: Design your system to leverage polymorphism, allowing objects to be treated as instances of their superclass or interface.

5. **🧩 Promote Polymorphism**:
   - **Interchangeable Objects**: Design your system so that objects of subclasses can be used interchangeably with objects of their superclass without affecting the program's behavior.
   - **Flexible Design**: Encourage a flexible and modular design where components can be easily swapped or extended.

6. **🔄 Encapsulate Variations**:
   - **Separate Concerns**: Isolate varying behaviors in subclasses while keeping the common behaviors in the superclass.
   - **Avoid Conditional Logic**: Reduce the need for conditional statements that check for specific subclass types by leveraging polymorphism.

By meticulously applying these steps, you ensure that your subclasses can seamlessly integrate into your system, enhancing functionality without compromising existing behaviors. 🔄

---

## 📂 Example: Bird and Penguin Before main

Let's examine an example where the Liskov Substitution Principle is violated. Imagine you have a `Bird` class and a `Penguin` class that inherits from `Bird`. 🐦🐧

```python
class Bird:
    def fly(self) -> None:
        print("I can fly")

class Penguin(Bird):
    def fly(self) -> None:
        print("I can't fly")

def make_bird_fly(bird: Bird) -> None:
    bird.fly()
```

### 📝 Explanation:

- **`Bird` Class**:
  - Has a method `fly` that prints "I can fly".
  
- **`Penguin` Class**:
  - Inherits from `Bird` and overrides the `fly` method to print "I can't fly".
  
- **`make_bird_fly` Function**:
  - Accepts any `Bird` object and calls its `fly` method.

### ⚠️ Issue:

When you pass a `Penguin` instance to `make_bird_fly`, it violates the expected behavior defined by the `Bird` class. The function expects the bird to fly, but the penguin cannot fly. This inconsistency breaks the main because substituting a superclass (`Bird`) with a subclass (`Penguin`) alters the program's correctness and expected behavior.

---

## 🔄 Refactoring to Follow main

To adhere to main, we'll refactor the code to ensure that subclasses can replace their superclasses without altering the program's behavior. 🛠️✨ Here's how we can achieve this:

### 1. Creating the `Bird` Class

First, we'll redefine the `Bird` class to represent general movement instead of specifically flying. This makes the superclass more flexible and avoids imposing a behavior that not all birds share.

```python
class Bird:
    def move(self) -> None:
        print("I'm moving")
```

### 📌 Explanation:

- **`move` Method**:
  - Represents general movement, which can be flying, walking, swimming, etc.
  - Provides a more abstract and versatile behavior that all bird types can share.

### 2. Creating the `FlyingBird` and `FlightlessBird` Classes

Next, we'll create two subclasses: `FlyingBird` and `FlightlessBird`, each implementing the `move` method according to their specific behaviors. 🦅🐧

```python
class FlyingBird(Bird):
    def move(self) -> None:
        print("I'm flying")

class FlightlessBird(Bird):
    def move(self) -> None:
        print("I'm walking")
```

### 📌 Explanation:

- **`FlyingBird` Class**:
  - Inherits from `Bird`.
  - Overrides the `move` method to implement flying behavior.
  
- **`FlightlessBird` Class**:
  - Inherits from `Bird`.
  - Overrides the `move` method to implement walking behavior.

### 3. Implementing the `make_bird_move` Function

We'll update the `make_bird_move` function to use the generalized `move` method. This ensures that the function works consistently with any subclass of `Bird` without knowing the specific type of movement.

```python
def make_bird_move(bird: Bird) -> None:
    bird.move()
```

### 📌 Explanation:

- **Polymorphism**:
  - The function relies on the `move` method, which is defined in the superclass `Bird` and overridden in subclasses.
  - This allows the function to work seamlessly with any `Bird` subclass, adhering to main.

### 4. Testing the Refactored Classes

Finally, we'll add a test script to verify that our refactored classes work as expected without violating main. 🧪

```python
if __name__ == "__main__":
    generic_bird: Bird = Bird()
    eagle: FlyingBird = FlyingBird()
    penguin: FlightlessBird = FlightlessBird()

    make_bird_move(generic_bird)  # Output: I'm moving
    make_bird_move(eagle)         # Output: I'm flying
    make_bird_move(penguin)       # Output: I'm walking
```

### 📌 Explanation:

- **`generic_bird` Instance**:
  - An instance of `Bird` using the general `move` method.
  
- **`eagle` Instance**:
  - An instance of `FlyingBird` using the overridden `move` method for flying.
  
- **`penguin` Instance**:
  - An instance of `FlightlessBird` using the overridden `move` method for walking.
  
- **Function Calls**:
  - Each call to `make_bird_move` passes a different bird instance, and the correct behavior is exhibited without any unexpected side effects.

---

## 🧪 Testing the Example

To ensure that our refactored code adheres to the Liskov Substitution Principle, follow these detailed steps:

### 1. Save the Code

Ensure that all the code is saved in a file named `03_liskov_substitution_principle/main.py`.

```python
class Bird:
    def move(self) -> None:
        print("I'm moving")

class FlyingBird(Bird):
    def move(self) -> None:
        print("I'm flying")

class FlightlessBird(Bird):
    def move(self) -> None:
        print("I'm walking")

def make_bird_move(bird: Bird) -> None:
    bird.move()

if __name__ == "__main__":
    generic_bird: Bird = Bird()
    eagle: FlyingBird = FlyingBird()
    penguin: FlightlessBird = FlightlessBird()

    make_bird_move(generic_bird)  # Output: I'm moving
    make_bird_move(eagle)         # Output: I'm flying
    make_bird_move(penguin)       # Output: I'm walking
```

### 2. Run the Code

Open your terminal and execute the following command to run the script:

```bash
python 03_liskov_substitution_principle/main.py
```

### 3. Expected Output

You should see the following output in your terminal:

```
I'm moving
I'm flying
I'm walking
```

### 4. Verify Behavior

- **`generic_bird`**: Prints "I'm moving" as expected.
- **`eagle`**: Prints "I'm flying" without issues.
- **`penguin`**: Prints "I'm walking" without affecting other parts of the program.

This confirms that our refactored classes adhere to the Liskov Substitution Principle. Each subclass can replace the superclass without altering the program's behavior, ensuring consistency and reliability. ✅

---

## 🔗 Conclusion

The **Liskov Substitution Principle (main)** is a cornerstone of object-oriented design that ensures your subclasses can seamlessly replace their superclasses without disrupting the program's functionality. 🛡️ By adhering to main, you create flexible, maintainable, and robust software systems that can evolve gracefully over time. 📈
# 🖨️ **Inheritance vs. Protocols in Python** 🐍✨

Understanding the difference between **inheritance-based typing** and **protocol-based typing** (also known as **structural subtyping**) is crucial for writing flexible and maintainable Python code. This guide provides a **simple, real-world example** to help you grasp these concepts effectively.


## 📚 **Table of Contents**

- [🖨️ **Inheritance vs. Protocols in Python** 🐍✨](#️-inheritance-vs-protocols-in-python-)
  - [📚 **Table of Contents**](#-table-of-contents)
  - [🌟 Overview](#-overview)
  - [🔑 Key Concepts](#-key-concepts)
    - [👨‍👩‍👧 Inheritance-Based Typing](#-inheritance-based-typing)
    - [🦆 Protocol-Based Typing](#-protocol-based-typing)
  - [🖨️ Real-World Example: Printable Documents](#️-real-world-example-printable-documents)
    - [🔄 Inheritance-Based Approach](#-inheritance-based-approach)
    - [🪶 Protocol-Based Approach](#-protocol-based-approach)
  - [✅ Comparison and Best Practices](#-comparison-and-best-practices)
  - [💬 Discussion Topics](#-discussion-topics)
  - [🎯 Conclusion](#-conclusion)
  - [🌐 Additional Resources](#-additional-resources)


## 🌟 Overview

In Python, **inheritance** and **protocols** are two mechanisms to achieve **subtyping**, allowing different types to be used interchangeably based on certain criteria.

- **Inheritance-Based Typing**: Relies on explicit class hierarchies where child classes inherit from parent classes. Type checkers recognize a type as a subtype only if it explicitly inherits from the expected parent class.

- **Protocol-Based Typing**: Also known as **structural subtyping**, allows classes to be considered subtypes based on their structure (methods and attributes) rather than their inheritance hierarchy. If a class implements the required methods and attributes, it satisfies the protocol, regardless of its actual inheritance.

This guide uses a **Printable Documents** example to illustrate both approaches, demonstrating their differences, benefits, and appropriate use cases.

---

## 🔑 Key Concepts

### 👨‍👩‍👧 Inheritance-Based Typing

**Inheritance** establishes an **is-a** relationship between classes. A child class inherits attributes and methods from a parent class, promoting **code reuse** and **extensibility**.

- **Pros**:
  - Clear hierarchical relationships.
  - Promotes code reuse.
  - Easy to understand and maintain for simple hierarchies.

- **Cons**:
  - Rigid structure; changes in parent classes can affect all child classes.
  - Can lead to complex and deep hierarchies.
  - Not flexible for classes that share behaviors but don't fit a strict hierarchy.

### 🦆 Protocol-Based Typing

**Protocols** define a set of methods and attributes that a class must implement to be considered compatible, without enforcing inheritance. This aligns with the **duck typing** philosophy: *"If it walks like a duck and quacks like a duck, it's a duck."*

- **Pros**:
  - Flexible; no need for explicit inheritance.
  - Promotes loose coupling.
  - Easier to extend and maintain, especially in large codebases.

- **Cons**:
  - Less explicit; requires careful documentation and understanding.
  - Type checkers may need more sophisticated configurations.
  - Can be less intuitive for developers accustomed to inheritance.

---

## 🖨️ Real-World Example: Printable Documents

Imagine you're building a system that handles different types of documents, such as PDFs, Word documents, and images. All these documents need to be printable. We'll explore two approaches to type the `print_document` function: one using inheritance and the other using protocols.

### 🔄 Inheritance-Based Approach

**Step 1: Define a Base Class**

Create an abstract base class `Printable` that defines the `print` method. All printable documents will inherit from this class.

```python
# printable_inheritance.py

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self) -> None:
        """Print the document."""
        pass
```

**Step 2: Define Specific Document Classes**

Create classes for specific document types that inherit from `Printable` and implement the `print` method.

```python
# documents_inheritance.py

from printable_inheritance import Printable

class PDFDocument(Printable):
    def __init__(self, content: str):
        self.content = content

    def print(self) -> None:
        print(f"Printing PDF Document: {self.content}")

class WordDocument(Printable):
    def __init__(self, content: str):
        self.content = content

    def print(self) -> None:
        print(f"Printing Word Document: {self.content}")

class ImageDocument:
    def __init__(self, image_path: str):
        self.image_path = image_path

    # No print method
```

**Step 3: Define the `print_document` Function**

```python
# printer_inheritance.py

from typing import Union
from printable_inheritance import Printable

def print_document(document: Printable) -> None:
    document.print()
```

**Step 4: Demonstrate Usage**

```python
# main_inheritance.py

from documents_inheritance import PDFDocument, WordDocument, ImageDocument
from printer_inheritance import print_document

def main():
    pdf = PDFDocument(content="Annual Report 2024")
    word = WordDocument(content="Meeting Minutes")
    image = ImageDocument(image_path="/images/logo.png")
    
    print_document(pdf)    # Works
    print_document(word)   # Works
    # print_document(image)  # Type checker will flag this as an error

    # Attempting to print a non-printable document (will raise AttributeError at runtime)
    try:
        print_document(image)  # This will cause a runtime error
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**📌 Explanation:**

1. **Base Class `Printable`**:
   - An abstract base class enforcing the implementation of the `print` method.
   - Prevents instantiation of `Printable` directly.

2. **Specific Document Classes**:
   - `PDFDocument` and `WordDocument` inherit from `Printable` and implement the `print` method.
   - `ImageDocument` does **not** inherit from `Printable` and lacks the `print` method.

3. **`print_document` Function**:
   - Accepts only instances of `Printable`.
   - Type checkers like `mypy` will enforce that only printable documents are passed.

4. **Usage in `main_inheritance.py`**:
   - Successfully prints `PDFDocument` and `WordDocument`.
   - Attempting to print `ImageDocument` without inheriting from `Printable` will cause type checkers to flag an error and raise an `AttributeError` at runtime.

**🔍 Running the Inheritance-Based Example:**

```bash
$ python main_inheritance.py
Printing PDF Document: Annual Report 2024
Printing Word Document: Meeting Minutes
Error: 'ImageDocument' object has no attribute 'print'
```

**Running Type Checker (`mypy`):**

```bash
$ mypy main_inheritance.py
main_inheritance.py:13: error: Argument 1 to "print_document" has incompatible type "ImageDocument"; expected "Printable"
Found 1 error in 1 file (checked 1 source file)
```

---

### 🪶 Protocol-Based Approach

To achieve greater flexibility and avoid rigid inheritance hierarchies, we'll use **protocols**. This allows any class that implements the required methods and attributes to be considered a subtype, without explicit inheritance.

**Step 1: Define the Protocol**

```python
# printable_protocol.py

from typing import Protocol

class Printable(Protocol):
    def print(self) -> None:
        """Print the document."""
        ...
```

**📌 Explanation:**

- **`Printable` Protocol**:
  - Specifies that any class with a `print` method returning `None` satisfies the protocol.
  - No need to inherit from `Protocol`; any class with the required method structure is considered compliant.

**Step 2: Define Specific Document Classes Without Inheriting from `Printable`**

```python
# documents_protocol.py

from printable_protocol import Printable

class PDFDocument:
    def __init__(self, content: str):
        self.content = content

    def print(self) -> None:
        print(f"Printing PDF Document: {self.content}")

class WordDocument:
    def __init__(self, content: str):
        self.content = content

    def print(self) -> None:
        print(f"Printing Word Document: {self.content}")

class ImageDocument:
    def __init__(self, image_path: str):
        self.image_path = image_path

    # No print method
```

**📌 Explanation:**

- **`PDFDocument` and `WordDocument` Classes**:
  - Implement the `print` method as specified by the `Printable` protocol.
  - Do **not** inherit from any base class.

- **`ImageDocument` Class**:
  - Does **not** implement the `print` method, hence does not satisfy the `Printable` protocol.

**Step 3: Define the `print_document` Function Using Protocols**

```python
# printer_protocol.py

from typing import Protocol
from printable_protocol import Printable

def print_document(document: Printable) -> None:
    document.print()
```

**📌 Explanation:**

- **`print_document` Function**:
  - Accepts any object that satisfies the `Printable` protocol.
  - No inheritance is required; type checkers will verify structural compatibility.

**Step 4: Demonstrate Usage**

```python
# main_protocol.py

from documents_protocol import PDFDocument, WordDocument, ImageDocument
from printer_protocol import print_document

def main():
    pdf = PDFDocument(content="Annual Report 2024")
    word = WordDocument(content="Meeting Minutes")
    image = ImageDocument(image_path="/images/logo.png")
    
    print_document(pdf)    # Works
    print_document(word)   # Works
    # print_document(image)  # Type checker will flag this as an error

    # Attempting to print a non-printable document (will raise AttributeError at runtime)
    try:
        print_document(image)  # This will cause a runtime error
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**📌 Explanation:**

1. **Specific Document Classes**:
   - `PDFDocument` and `WordDocument` implement the `print` method, satisfying the `Printable` protocol.
   - `ImageDocument` does **not** implement the `print` method, hence does not satisfy the protocol.

2. **`print_document` Function**:
   - Accepts any object adhering to the `Printable` protocol.
   - Type checkers like `mypy` will enforce structural compatibility.

3. **Usage in `main_protocol.py`**:
   - Successfully prints `PDFDocument` and `WordDocument`.
   - Attempting to print `ImageDocument` without implementing `print` will cause type checkers to flag an error and raise an `AttributeError` at runtime.

**🔍 Running the Protocol-Based Example:**

```bash
$ python main_protocol.py
Printing PDF Document: Annual Report 2024
Printing Word Document: Meeting Minutes
Error: 'ImageDocument' object has no attribute 'print'
```

**Running Type Checker (`mypy`):**

```bash
$ mypy main_protocol.py
main_protocol.py:13: error: Argument 1 to "print_document" has incompatible type "ImageDocument"; expected "Printable"
Found 1 error in 1 file (checked 1 source file)
```


## ✅ Comparison and Best Practices

| Aspect                      | Inheritance-Based Typing                                    | Protocol-Based Typing                                |
|-----------------------------|------------------------------------------------------------|------------------------------------------------------|
| **Relationship**            | Establishes an explicit **is-a** relationship.            | Based on **behavioral compatibility** (duck typing). |
| **Flexibility**             | Rigid; requires inheritance hierarchy.                    | Flexible; no inheritance required.                   |
| **Code Reuse**              | Promotes reuse through shared parent classes.             | Encourages reuse by adhering to common protocols.    |
| **Maintenance**             | Can become complex with deep hierarchies.                  | Easier to maintain; adding new classes doesn't affect hierarchy. |
| **Type Checking**           | Enforced by inheritance; type checkers rely on class hierarchy. | Enforced by structural compatibility; type checkers verify method signatures. |
| **Use Cases**               | When classes share a clear hierarchical relationship.      | When classes share common behaviors but aren't related hierarchically. |
| **Example Scenario**        | Vehicles (Car is a Vehicle).                               | Any object with a `print` method is Printable.       |

**Best Practices:**

1. **Use Inheritance When:**
   - There's a clear **is-a** relationship.
   - You want to share common implementation details.
   - The hierarchy is unlikely to change frequently.

2. **Use Protocols When:**
   - You need flexibility and loose coupling.
   - Classes share behaviors but don't fit into a strict hierarchy.
   - You want to leverage duck typing with type safety.

3. **Combine Both Approaches:**
   - Use inheritance for hierarchical relationships and protocols for shared behaviors across different hierarchies.

4. **Leverage Type Checkers:**
   - Tools like `mypy` can help enforce type safety and catch errors early, especially when using protocols.


## 💬 Discussion Topics

1. **When to Prefer Protocols Over Inheritance:**
   - Discuss scenarios where protocol-based typing offers significant advantages, such as plugin architectures or when integrating third-party classes that cannot be modified to inherit from a common base class.

2. **Combining Protocols and Inheritance:**
   - Explore how protocols can coexist with inheritance, allowing for both hierarchical and structural subtyping. For example, a base class might provide core functionality, while protocols define additional behaviors.

3. **Maintaining Code Consistency with Protocols:**
   - Strategies to ensure that classes correctly implement required protocols, such as thorough documentation, adhering to naming conventions, and using static type checkers.

4. **Real-World Applications of Protocols:**
   - Examine how popular Python libraries leverage protocols for flexibility. For instance, Python's built-in iterable protocol allows any object with `__iter__` and `__next__` methods to be used in loops, regardless of inheritance.

## 🎯 Conclusion

Both **inheritance-based typing** and **protocol-based typing** are valuable tools in Python, each with its strengths and ideal use cases.

- **Inheritance** is best suited for scenarios with clear hierarchical relationships, promoting code reuse and shared behavior through parent classes.

- **Protocols** provide flexibility by allowing any class that matches a specific structure to be used interchangeably, promoting loose coupling and easier maintenance.

By understanding and appropriately applying both approaches, you can design Python applications that are both robust and adaptable to evolving requirements.

## 🌐 Additional Resources

To further enhance your understanding of inheritance, protocols, and type hinting in Python, explore the following **valuable resources**:

- [**Python Official Documentation on Inheritance**](https://docs.python.org/3/tutorial/classes.html#inheritance) 📘
- [**PEP 544 – Structural Subtyping (Protocols)**](https://peps.python.org/pep-0544/) 📄✨
- [**Real Python: Inheritance in Python**](https://realpython.com/python-inheritance/) 🛠️🔍
- [**Real Python: Python Protocols**](https://realpython.com/python-protocols/) 🛠️🔍
- [**Mypy Official Documentation on Protocols**](https://mypy.readthedocs.io/en/stable/protocols.html) 📈🔧
- [**Programiz: Python Classes and Objects**](https://www.programiz.com/python-programming/class) 📄🔧
- [**Effective Python: 59 Specific Ways to Write Better Python**](https://effectivepython.com/) 📚🧠
- [**Design Patterns in Python**](https://refactoring.guru/design-patterns/python) 🛠️🔍
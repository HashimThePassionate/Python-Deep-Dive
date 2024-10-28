# 📘 Classes vs Objects in OOP

Welcome! This guide breaks down the concepts of **classes** and **objects** in Object-Oriented Programming (OOP), along with a practical example using a **TextBox** class. Let's explore these foundational concepts in detail! 🚀

---

## 📑 Table of Contents

- [📘 Classes vs Objects in OOP](#-classes-vs-objects-in-oop)
  - [📑 Table of Contents](#-table-of-contents)
    - [💡 Understanding Classes](#-understanding-classes)
    - [🔍 Understanding Objects](#-understanding-objects)
    - [🔄 Classes vs. Objects: Key Differences](#-classes-vs-objects-key-differences)
    - [📝 Example: TextBox Class](#-example-textbox-class)
      - [🖼️ Graphical Representation of TextBox Class](#️-graphical-representation-of-textbox-class)
      - [📋 Properties](#-properties)
      - [📌 Methods](#-methods)
    - [📜 Summary](#-summary)

---

### 💡 Understanding Classes

A **class** serves as a **blueprint** or **template** for creating objects. It defines the structure and behavior of its objects by specifying:

- **Properties (Attributes)**: These are variables that store data or characteristics of the class’s objects.
- **Methods (Behaviors)**: These are functions within the class that define actions or behaviors the objects can perform.

In short, a class is a model that outlines what properties and behaviors each object created from it will possess.

---

### 🔍 Understanding Objects

An **object** is a **concrete instance** of a class. When we create an object from a class, we’re using the class blueprint to build a specific, unique entity that has:

- **Its Own State**: The object’s property values, like specific text or size, which can differ from other objects created from the same class.
- **Defined Behavior**: Access to the methods specified by the class, allowing it to perform specific actions or functions.

Objects are the actual entities that interact within a program, embodying both the structure and behavior defined by their class.

---

### 🔄 Classes vs. Objects: Key Differences

| Aspect               | Class                                                                                       | Object                                                                                          |
|----------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Definition**       | A blueprint or template that defines structure and behavior for objects                     | A concrete instance of a class with its own state and behavior                                  |
| **Purpose**          | Provides a framework for creating objects                                                   | Represents a unique, specific entity created from the class blueprint                           |
| **Attributes**       | General definitions of properties that objects will have                                    | Contains actual values of properties specific to that object                                    |
| **Behavior**         | Defines methods that all instances will have access to                                      | Executes methods as specified by the class, but can maintain unique values for properties       |
| **Reusability**      | Can be reused to create multiple objects                                                    | Each object represents a separate instance with its own unique characteristics                  |

---

### 📝 Example: TextBox Class

Consider a **TextBox** class that represents a graphical user interface (GUI) textbox component. This class has attributes for **text content** and **size** and methods to manipulate them.

#### 🖼️ Graphical Representation of TextBox Class

```
+----------------------------------+
|            TextBox               |
+----------------------------------+
|    text: str                     | 
|    size: int                     |
+----------------------------------+
|    setText(text: str): void      |
|    getText(): str                |
|    setSize(size: int): void      |
|    getSize(): int                |
+----------------------------------+
```

#### 📋 Properties

1. **text**: Represents the content displayed within the textbox.
2. **size**: Represents the display size of the textbox.

#### 📌 Methods

1. **setText(text: str)**: Sets the text content of the textbox to the provided value.
2. **getText() -> str**: Retrieves the current text content from the textbox.
3. **setSize(size: int)**: Sets the size of the textbox to the specified integer value.
4. **getSize() -> int**: Retrieves the current size of the textbox.

---

### 📜 Summary

- **Classes** are the blueprints that define the general structure and behavior of objects. They specify the properties (attributes) and methods (behaviors) that objects will have.
- **Objects** are instances created from a class. They represent unique, concrete entities with their own state (property values) and access to the class-defined methods.

Using the **TextBox** example, you can see how classes organize properties and behaviors, while objects bring those properties and behaviors to life in specific instances. Each object created from the TextBox class can have different text and sizes, but all share the same structure and capabilities defined by the class.

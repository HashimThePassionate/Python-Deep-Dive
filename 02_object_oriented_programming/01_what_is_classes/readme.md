## Classes vs Objects

**Classes** are blueprints or templates for creating objects. They define the structure and behavior that objects of the class will have. A class specifies the properties (attributes) and behaviors (methods) that its objects will possess.

**Objects**, on the other hand, are instances of classes. They are concrete entities created from the class blueprint and have their own unique state (property values) and behavior (method implementations). Multiple objects can be created from the same class, each with its own distinct state.

In summary, classes define the structure and behavior of objects, while objects are instances of classes that have their own state and behavior.

## TextBox Class Example
Consider a TextBox class representing a graphical user interface (GUI) textbox component. Here's a graphical representation of the TextBox class with its properties and methods:

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

- **Properties**: 
  - `text`: Represents the text content of the textbox.
  - `size`: Represents the size of the textbox.

- **Methods**:
  - `setText(text: str)`: Sets the text content of the textbox.
  - `getText(): str`: Retrieves the current text content of the textbox.
  - `setSize(size: int)`: Sets the size of the textbox.
  - `getSize(): int`: Retrieves the current size of the textbox.
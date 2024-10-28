# 🖥️ TextBox Class Example

This guide covers the **TextBox** class—a simple implementation for managing text content within a graphical user interface (GUI) component. The class provides essential functionality to **set** and **clear** text content.

---

## 📑 Table of Contents

- [🖥️ TextBox Class Example](#️-textbox-class-example)
  - [📑 Table of Contents](#-table-of-contents)
    - [🔍 Class Definition and Code](#-class-definition-and-code)
    - [⚙️ Methods in TextBox](#️-methods-in-textbox)
      - [🔹 `__init__` Method](#-__init__-method)
      - [🔹 `set_text` Method](#-set_text-method)
      - [🔹 `clear` Method](#-clear-method)
    - [💻 Usage Example](#-usage-example)
    - [📜 Summary](#-summary)

---

### 🔍 Class Definition and Code

Here’s the complete code for the **TextBox** class, along with an explanation of each method:

```python
class TextBox:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def clear(self):
        self.text = ""
```

- **Purpose**: The `TextBox` class is designed to manage simple text content.
- **Attributes**:
  - `text` (str): Stores the text content for each instance of `TextBox`.
- **Initialization**:
  - When a new `TextBox` instance is created, the `__init__` method sets `text` to an empty string.

---

### ⚙️ Methods in TextBox

The **TextBox** class includes two main methods—**set_text** and **clear**—each providing distinct functionality to manage text.

#### 🔹 `__init__` Method

- **Purpose**: Initializes a new `TextBox` object with the `text` attribute set to an empty string.
- **Description**: This method is called automatically when a `TextBox` instance is created, ensuring that each instance starts with `text` as an empty string.

#### 🔹 `set_text` Method

```python
def set_text(self, text):
    self.text = text
```

- **Purpose**: Assigns the `text` attribute to a specified value.
- **Parameter**:
  - `text` (str): The new text to set as the `text` attribute’s value.
- **Description**: Allows the `TextBox` instance to update its content with a new string value.

#### 🔹 `clear` Method

```python
def clear(self):
    self.text = ""
```

- **Purpose**: Resets the `text` attribute to an empty string.
- **Description**: Clears the current text content in the `TextBox`, useful for removing text without creating a new instance.

---

### 💻 Usage Example

Here’s a practical example demonstrating how to use the **TextBox** class:

```python
# Create a TextBox instance
textbox = TextBox()

# Set text content
textbox.set_text("Hello, Python!")
print(textbox.text)  # Output: Hello, Python!

# Clear the text content
textbox.clear()
print(textbox.text)  # Output: (empty string)
```

**Explanation**:
- We start by creating a `TextBox` instance named `textbox`.
- The `set_text` method assigns "Hello, Python!" to `textbox.text`.
- The `clear` method then resets `textbox.text` to an empty string, effectively clearing the content.

---

### 📜 Summary

The **TextBox** class provides a simple structure for managing text in a GUI component, featuring:

- **__init__**: Initializes `text` to an empty string when a new instance is created.
- **set_text**: Allows setting the `text` attribute with a specific value.
- **clear**: Clears the `text` content, resetting it to an empty string.

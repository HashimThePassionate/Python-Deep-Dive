## Abstract Classes

An abstract class is a class that cannot be instantiated on its own and is designed to be subclassed. Abstract classes often include abstract methods, which are methods declared in an abstract class but do not contain any implementation. These methods must be implemented by subclasses of the abstract class. In Python, the `abc` module provides the infrastructure for defining abstract base classes (ABCs).

### Why We Need Abstract Classes

1. **Enforce a Contract**: Abstract classes allow you to define a contract for subclasses. Subclasses must implement certain methods, ensuring a consistent interface.
2. **Promote Code Reusability**: By defining common methods and properties in an abstract class, you can reduce code duplication and promote code reuse across multiple subclasses.
3. **Facilitate Polymorphism**: Abstract classes allow for polymorphism, where you can treat instances of different subclasses as instances of the abstract class, making your code more flexible and easier to maintain.

### Use Case

Abstract classes are useful in scenarios where you have a common interface or behavior that multiple subclasses should follow but where the actual implementation details may differ. For example, in a UI framework, you might have different types of UI controls (like buttons, text boxes, check boxes) that share some common behavior but need to render themselves differently.

## Explanation of the Provided Code

Let's break down the provided code and explain each part:

### Importing Required Modules

```python
from abc import ABC, abstractmethod
```

This imports `ABC` and `abstractmethod` from the `abc` module. `ABC` is used to define abstract base classes, and `abstractmethod` is used to declare abstract methods.

### Defining the Abstract Class

```python
class UIControl(ABC):
    def __init__(self):
        self._is_enabled = True

    @abstractmethod
    def render(self):
        pass

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    def is_enabled(self):
        return self._is_enabled
```

- `UIControl` is an abstract class that inherits from `ABC`.
- The `__init__` method initializes an instance variable `_is_enabled` to `True`.
- `render` is an abstract method, meaning that any subclass of `UIControl` must implement this method.
- `enable`, `disable`, and `is_enabled` are concrete methods providing common functionality to enable or disable the control and check if it is enabled.

### Defining a Subclass (TextBox)

```python
class TextBox(UIControl):
    def __init__(self):
        super().__init__()
        self._text = ""

    def render(self):
        print("Render TextBox")

    def __str__(self):
        return self._text

    def set_text(self, text):
        self._text = text

    def clear(self):
        self._text = ""
```

- `TextBox` is a subclass of `UIControl`.
- The `__init__` method initializes a `_text` variable and calls the superclass's `__init__` method.
- The `render` method provides the implementation required by the abstract method in `UIControl`.
- The `__str__` method returns the current text in the text box.
- `set_text` and `clear` methods are specific to `TextBox` for managing the text content.

### Defining Another Subclass (CheckBox)

```python
class CheckBox(UIControl):
    def render(self):
        print("Render CheckBox")
```

- `CheckBox` is another subclass of `UIControl`.
- The `render` method provides the required implementation, printing "Render CheckBox".

### Usage

```python
# Usage
textbox = TextBox()
checkbox = CheckBox()
textbox.set_text("Muhammad Hashim")
print(textbox)
textbox.render()
checkbox.render()
```

- Instances of `TextBox` and `CheckBox` are created.
- The `set_text` method sets the text of the `TextBox`.
- The `print` function calls the `__str__` method of `TextBox`, printing the text.
- The `render` method of both `TextBox` and `CheckBox` is called, demonstrating polymorphism.

### Output

The output of the provided code will be:
```
Muhammad Hashim
Render TextBox
Render CheckBox
```

This demonstrates how abstract classes and methods can enforce a consistent interface while allowing for specific implementations in subclasses.
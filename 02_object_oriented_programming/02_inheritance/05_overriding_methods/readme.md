# What is Methods Overriding:
Method overriding is a concept in object-oriented programming where a subclass provides a specific implementation of a method that is already defined in its superclass. In Python, method overriding occurs when a subclass provides its own implementation of a method that is already defined in its superclass. 

### Benefits of Method Overriding:
1. **Polymorphism**: Method overriding allows objects of different classes to be treated uniformly through a common interface, enhancing code flexibility and readability.
2. **Customization**: Subclasses can tailor methods to suit their specific requirements, providing specialized behavior while inheriting common functionality from the superclass.
3. **Extensibility**: Method overriding enables the extension of existing classes by refining or altering their behavior without modifying the superclass, thus promoting code reuse and maintainability.

### Implementing Method Overriding in Python:

In the provided Python code, method overriding is demonstrated in the `TextBox` subclass where it overrides the `__str__` method of its superclass `UIControl`. Here's how method overriding is implemented:

1. **Superclass (`UIControl`)**:
   - Defines the `__str__` method, which returns a string representation of the object's state, in this case, whether it's enabled or not.
   - Provides other methods such as `enable`, `disable`, and `is_enabled`.

2. **Subclass (`TextBox`)**:
   - Inherits from `UIControl`.
   - Overrides the `__str__` method to return a string representation of its own state, specifically the `text` attribute.
   - Provides additional methods like `set_text` and `clear` for manipulating the `text` attribute.

Here's the code with comments explaining the implementation of method overriding:

```python
class UIControl:
    def __init__(self, is_enabled=True):
        self._is_enabled = is_enabled

    def __str__(self):
        return str(self.is_enabled())

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    def is_enabled(self):
        return self._is_enabled


class TextBox(UIControl):
    def __init__(self):
        super().__init__(True)
        self.text = ""

    def __str__(self):
        return self.text  # Overrides __str__ method to return text attribute

    def set_text(self, text):
        self.text = text

    def clear(self):
        self.text = ""


# Creating an instance of TextBox and setting text
control = UIControl()
print(str(control))  # Output: "True" (string representation of is_enabled status)
textbox = TextBox()
textbox.set_text("Muhammad Hashim")
print(textbox)  # Output: "Muhammad Hashim" (string representation of textbox's text)
```

### Explanation:
- **Inheritance**: `TextBox` inherits from `UIControl`.
- **Override**: `TextBox` overrides the `__str__` method of `UIControl` to provide a custom string representation (`text` attribute).
- **Polymorphism**: Even though `textbox` is an instance of `TextBox`, when `print(textbox)` is called, it invokes the overridden `__str__` method in `TextBox` instead of the one in `UIControl`, demonstrating polymorphic behavior.

This example illustrates how method overriding allows subclasses to provide their own behavior for inherited methods, providing flexibility and customization within the inheritance hierarchy.
# Constructors and Inheritance

### Class `UIControl`
This class represents a generic user interface control with basic functionality to enable and disable it.

1. **Initialization Method (`__init__`)**:
    ```python
    def __init__(self, is_enabled=True):
        self._is_enabled = is_enabled
    ```
    - The `__init__` method is the constructor of the class.
    - It takes an optional parameter `is_enabled` which defaults to `True`.
    - It initializes an instance variable `_is_enabled` to the value of `is_enabled`.

2. **Method to Enable the Control (`enable`)**:
    ```python
    def enable(self):
        self._is_enabled = True
    ```
    - The `enable` method sets the `_is_enabled` attribute to `True`.

3. **Method to Disable the Control (`disable`)**:
    ```python
    def disable(self):
        self._is_enabled = False
    ```
    - The `disable` method sets the `_is_enabled` attribute to `False`.

4. **Method to Check if the Control is Enabled (`is_enabled`)**:
    ```python
    def is_enabled(self):
        return self._is_enabled
    ```
    - The `is_enabled` method returns the value of the `_is_enabled` attribute, indicating whether the control is enabled or not.

### Class `TextBox`
This class represents a text box control that inherits from `UIControl`.

1. **Initialization Method (`__init__`)**:
    ```python
    def __init__(self):
        super().__init__(True)
        self._text = ""
    ```
    - The `__init__` method is the constructor of the class.
    - It calls the constructor of the `UIControl` class using `super().__init__(True)`, which initializes the text box as enabled (`True`).
    - It initializes an additional instance variable `_text` to an empty string `""`.

2. **Method to Set the Text (`set_text`)**:
    ```python
    def set_text(self, text):
        self._text = text
    ```
    - The `set_text` method takes a parameter `text` and sets the `_text` attribute to this value.

3. **Method to Clear the Text (`clear`)**:
    ```python
    def clear(self):
        self._text = ""
    ```
    - The `clear` method sets the `_text` attribute to an empty string `""`.

### Creating and Using an Instance of `TextBox`
This part of the code demonstrates creating an instance of `TextBox` and using its methods.

1. **Creating an Instance**:
    ```python
    control = TextBox()
    ```
    - This line creates an instance of the `TextBox` class and assigns it to the variable `control`.

2. **Disabling the Control**:
    ```python
    control.disable()
    ```
    - This line calls the `disable` method on the `control` object, setting its `_is_enabled` attribute to `False`.

3. **Checking if the Control is Enabled**:
    ```python
    print(control.is_enabled())  # This will print: False
    ```
    - This line calls the `is_enabled` method on the `control` object and prints the result.
    - Since the control was disabled in the previous step, this will print `False`.

### Summary
- The `UIControl` class provides basic enable/disable functionality for user interface controls.
- The `TextBox` class extends `UIControl` and adds text management functionality.
- An instance of `TextBox` is created, disabled, and its enabled state is checked and printed, demonstrating the inheritance and functionality of the classes.
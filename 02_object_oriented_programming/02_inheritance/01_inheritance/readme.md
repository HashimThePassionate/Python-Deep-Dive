# Inheritance
```python
# Define a class named UIControl
class UIControl:
    # Initialize the class with a constructor
    def __init__(self):
        # Set the initial state of _is_enabled to True
        self._is_enabled = True

    # Define a method to enable the control
    def enable(self):
        # Set _is_enabled to True
        self._is_enabled = True

    # Define a method to disable the control
    def disable(self):
        # Set _is_enabled to False
        self._is_enabled = False

    # Define a method to check if the control is enabled
    def is_enabled(self):
        # Return the current state of _is_enabled
        return self._is_enabled

# Define a class named TextBox that inherits from UIControl
class TextBox(UIControl):
    # Initialize the class with a constructor
    def __init__(self):
        # Call the constructor of the parent class (UIControl)
        super().__init__()
        # Set the initial state of _text to an empty string
        self._text = ""

    # Define a method to set the text of the TextBox
    def set_text(self, text):
        # Set _text to the provided text
        self._text = text

    # Define a method to clear the text of the TextBox
    def clear(self):
        # Set _text to an empty string
        self._text = ""

# Create an instance of the TextBox class
control = TextBox()
# Call the disable method on the control object
control.disable()
# Print the result of the is_enabled method, which checks if the control is enabled
print(control.is_enabled())
```

### Explanation:

1. **Class Definition**: The code defines two classes, `UIControl` and `TextBox`. The `TextBox` class inherits from `UIControl`.
   
2. **`UIControl` Class**:
    - **`__init__` Method**: The constructor initializes an instance variable `_is_enabled` and sets it to `True`.
    - **`enable` Method**: This method sets `_is_enabled` to `True`.
    - **`disable` Method**: This method sets `_is_enabled` to `False`.
    - **`is_enabled` Method**: This method returns the value of `_is_enabled`.

3. **`TextBox` Class**:
    - **Inheritance**: The `TextBox` class inherits from `UIControl`, meaning it has all the methods and properties of `UIControl`.
    - **`__init__` Method**: The constructor calls the parent class's constructor using `super()` and initializes an instance variable `_text` to an empty string.
    - **`set_text` Method**: This method sets the `_text` variable to the provided `text`.
    - **`clear` Method**: This method sets the `_text` variable to an empty string.

4. **Creating an Instance**:
    - An instance of `TextBox` is created and assigned to the variable `control`.
    - The `disable` method is called on `control`, setting `_is_enabled` to `False`.
    - The result of the `is_enabled` method (which is `False`) is printed to the console.
# Upcasting and Downcasting in Python

### Upcasting
Upcasting is when a subclass instance is treated as an instance of a superclass. In your example, `TextBox` is a subclass of `UIControl`. When you pass an instance of `TextBox` to a function expecting a `UIControl`, upcasting occurs automatically because `TextBox` is a `UIControl`.

### Downcasting
Downcasting is when you take an instance of a superclass and treat it as an instance of a subclass. This is less common in Python and should be done with caution, as it can lead to runtime errors if the object is not actually an instance of the subclass you are downcasting to.

Here's the corrected version of your function with proper handling of downcasting:

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
        return self.text

    def set_text(self, text):
        self.text = text

    def clear(self):
        self.text = ""


# Function to demonstrate upcasting and downcasting
def show(control: UIControl):
    if isinstance(control, TextBox):  # Check if control is actually a TextBox (downcasting)
        textbox = control  # No need for explicit cast, just use the control as a TextBox
        textbox.set_text('Hello World')
        print(control)
    else:
        print("Provided control is not a TextBox")

# Creating an instance of TextBox and setting text
control = UIControl(is_enabled=True)
textbox = TextBox()
show(control=textbox)  # This will print 'Hello World'
```

### Explanation

1. **Upcasting**: When you call `show(control=textbox)`, the `textbox` instance of `TextBox` is passed to a function expecting a `UIControl`. This is upcasting and is automatic because `TextBox` is a subclass of `UIControl`.

2. **Downcasting**: Inside the `show` function, we use `isinstance` to check if the `control` is actually a `TextBox`. If it is, we can safely treat it as a `TextBox`. 

3. **Setting Text**: After confirming that `control` is a `TextBox`, we call `set_text` and print the control, which now prints 'Hello World'.

4. **Safety**: Using `isinstance` ensures that we avoid runtime errors by verifying the type before treating the object as a `TextBox`.


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

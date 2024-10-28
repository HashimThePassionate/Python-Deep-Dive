class UIControl:
    def __init__(self, is_enabled=True):
        self._is_enabled = is_enabled
        print('UIControl Constructor')

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    def is_enabled(self):
        return self._is_enabled


class TextBox(UIControl):
    def __init__(self):
        super().__init__(True)
        self._text = ""
        print('TextBox Constructor')

    def set_text(self, text):
        self._text = text

    def clear(self):
        self._text = ""


# Creating an instance of TextBox
control = TextBox()
control.disable()
print(control.is_enabled())  # This will print: False

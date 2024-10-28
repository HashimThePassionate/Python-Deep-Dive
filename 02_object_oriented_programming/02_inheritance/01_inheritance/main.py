class UIControl:
    def __init__(self):
        self._is_enabled = True

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    def is_enabled(self):
        return self._is_enabled

class TextBox(UIControl):
    def __init__(self):
        super().__init__()
        self._text = ""

    def set_text(self, text):
        self._text = text

    def clear(self):
        self._text = ""

control = TextBox()
control.disable()
print(control.is_enabled())


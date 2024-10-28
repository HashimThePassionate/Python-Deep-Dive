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


# Creating an instance of TextBox and setting text
control = UIControl()
print(str(control))
textbox = TextBox()
textbox.set_text("Muhammad Hashim")
print(textbox)

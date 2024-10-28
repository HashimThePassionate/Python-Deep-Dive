from abc import ABC, abstractmethod

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


class CheckBox(UIControl):
    def render(self):
        print("Render CheckBox")


# Usage
textbox = TextBox()
checkbox = CheckBox()
textbox.set_text("Muhammad Hashim")
print(textbox)
textbox.render()
checkbox.render()

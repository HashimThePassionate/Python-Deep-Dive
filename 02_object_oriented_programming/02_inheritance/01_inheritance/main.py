class UIControl:
    def __init__(self):
        self._is_enabled = True
    
    def enable(self):
        self._is_enabled = True
        print("Control enabled")
    
    def disable(self):
        self._is_enabled = False
        print("Control disabled")

    def get_is_enabled(self):
        return self._is_enabled
    

class TextBox(UIControl):
    def __init__(self):
        super().__init__()
        self.text = ""
    
    def set_text(self, text):
        if self._is_enabled:
            self.text = text
            print(f"Text set to: {self.text}")
        else:
            print("Cannot set text, control is disabled")
    
    def get_text(self):
        return self.text
    
    def clear_text(self):
        if self._is_enabled:
            self.text = None
            print("Text cleared")
        else:
            print("Cannot clear text, control is disabled")


textbox1 = TextBox()
print(textbox1.get_is_enabled())  # True
textbox1.disable()
print(textbox1.get_is_enabled())  # True

textbox1.set_text("Hello")  # Cannot set text, control is disabled
textbox1.enable()
textbox1.set_text('Muhammad Hashim')
print(textbox1.get_text())  # Muhammad Hashim
textbox1.clear_text()
print(textbox1.get_text())  # Muhammad Hashim

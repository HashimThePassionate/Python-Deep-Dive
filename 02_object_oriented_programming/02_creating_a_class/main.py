class TextBox:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def clear(self):
        self.text = ""

textbox = TextBox()
textbox.set_text("Hello, Python!")
print(textbox.text) 
textbox.clear()
print(textbox.text)
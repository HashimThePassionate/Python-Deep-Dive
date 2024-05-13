class TextBox:
    def __init__(self):
        self.text = ""  # Default text content is an empty string
        self.size = 0   # Default size is 0

    def set_text(self, text: str):
        """Sets the text content of the textbox."""
        self.text = text

    def get_text(self) -> str:
        """Retrieves the current text content of the textbox."""
        return self.text

    def set_size(self, size: int):
        """Sets the size of the textbox."""
        self.size = size

    def get_size(self) -> int:
        """Retrieves the current size of the textbox."""
        return self.size


# Create an instance of the TextBox class
textbox = TextBox()

# Set text content
textbox.set_text("Hello, World!")

# Set size
textbox.set_size(10)

# Retrieve text content and size
print("Text content:", textbox.get_text())
print("Size:", textbox.get_size())

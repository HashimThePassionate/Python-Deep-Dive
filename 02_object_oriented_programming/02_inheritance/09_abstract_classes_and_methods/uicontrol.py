from abc import ABC, abstractmethod
import tkinter as tk

# Abstract base class for GUI elements
class GUIElement(ABC):
    def __init__(self, master, x, y):
        self.master = master
        self.x = x
        self.y = y

    @abstractmethod
    def create(self):
        pass

# Concrete class for Textbox
class Textbox(GUIElement):
    def create(self):
        self.entry = tk.Entry(self.master)
        self.entry.place(x=self.x, y=self.y)

# Concrete class for Checkbox
class Checkbox(GUIElement):
    def create(self):
        self.var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.master, text="Check me", variable=self.var)
        self.checkbox.place(x=self.x, y=self.y)

# Concrete class for Radiobutton
class Radiobutton(GUIElement):
    def create(self):
        self.var = tk.StringVar()
        self.radio1 = tk.Radiobutton(self.master, text="Option 1", variable=self.var, value="1")
        self.radio2 = tk.Radiobutton(self.master, text="Option 2", variable=self.var, value="2")
        self.radio1.place(x=self.x, y=self.y)
        self.radio2.place(x=self.x, y=self.y + 30)

# Main GUI application
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Abstract Class GUI Elements")
        self.geometry("300x200")

        # Creating GUI elements
        textbox = Textbox(self, 50, 20)
        textbox.create()

        checkbox = Checkbox(self, 50, 60)
        checkbox.create()

        radiobutton = Radiobutton(self, 50, 100)
        radiobutton.create()


app = Application()
app.mainloop()

```python
class User:
    def __init__(self, name):  # Constructor method
        self.name = name  # Initialize the 'name' attribute with the provided name

    def say_hello(self):  # Method to greet
        print("- Hi, my name is", self.name)  # Print a greeting message including the user's name

if __name__ == "__main__":  # Check if this script is being run directly
    user = User('Hashim')  # Create a User object with the name 'Hashim'
    user.say_hello()  # Call the say_hello method of the User object


Explanation:

- **User Class**: Defines a class named `User`.
  - **`__init__` Method**: This is the constructor method, called when a new instance of the class is created. It initializes the `name` attribute of the User object with the provided `name` parameter.
  - **`say_hello` Method**: This method prints a greeting message including the user's name.

- **`if __name__ == "__main__":`**: This line checks whether the current script is being run directly as the main program. If it is, the code block beneath it will be executed.
  - **Creating a User Object**: Creates a `User` object with the name 'Hashim'.
  - **Calling the `say_hello` Method**: Calls the `say_hello` method of the `User` object, which prints a greeting message.

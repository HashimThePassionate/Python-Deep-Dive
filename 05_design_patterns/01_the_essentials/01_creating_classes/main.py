class User:
    def __init__(self, name):  # Constructor method
        self.name = name  # Initialize the 'name' attribute with the provided name

    def say_hello(self):  # Method to greet
        print("- Hi, my name is", self.name)  # Print a greeting message including the user's name

if __name__ == "__main__":  # Check if this script is being run directly
    user = User('Hashim')  # Create a User object with the name 'Hashim'
    user.say_hello()  # Call the say_hello method of the User object

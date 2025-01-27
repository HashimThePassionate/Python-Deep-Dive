class User(object):
    def __new__(cls, username, *args, **kwargs):
        # Ensure username is always stored in uppercase
        username = username.upper()  # Convert to uppercase
        # Create the instance using the superclass's __new__ method
        instance = super().__new__(cls)
        # Store the converted username in the instance
        instance.username = username
        return instance

    def __init__(self, username):
        # Constructor will not modify username; __new__ handles it
        self.original_username = username  # Just to store the original (if needed)

    def __str__(self):
        # Provide a friendly string representation of the object
        return f"User(username={self.username})"
# Creating User objects with different username inputs
user1 = User("hashim")
user2 = User("ali")
user3 = User("Fatima")

# Displaying the users
print(user1)  # Output: User(username=HASHIM)
print(user2)  # Output: User(username=ALI)
print(user3)  # Output: User(username=FATIMA)

# Accessing the username attribute
print(user1.username)  # Output: HASHIM
print(user1.original_username)  # Output: hashim
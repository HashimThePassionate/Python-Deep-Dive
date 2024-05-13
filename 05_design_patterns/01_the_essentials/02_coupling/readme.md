# Example 1: Low Coupling
```python
    class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
```
# User Class
- **User Class**: Defines a class named User.
- **__init__ Method**: Initializes the name and age attributes of the User object with the provided parameters.
- **get_name Method**: Returns the name of the user.
- **get_age Method**: Returns the age of the user.

In this example, the User class is self-contained and does not rely on other classes or external modules. It only interacts with its own attributes.

# Example 2: High Coupling
```python
class Database:
    def save_user(self, user):
        # Save user data to the database
        pass

    def load_user(self, name):
        # Load user data from the database
        pass

class User:
    def __init__(self, name):
        self.name = name

    def save_to_database(self):
        database = Database()
        database.save_user(self)

    @classmethod
    def load_from_database(cls, name):
        database = Database()
        user_data = database.load_user(name)
        return cls(user_data['name'])
```
## Explanation:
## User Class:

### __init__ Method:

- This method is the constructor of the User class.
- It initializes the name attribute of the User object with the provided name parameter.

### save_to_database Method:

- This method is used to save a User object to the database.
- It creates an instance of the Database class.
- Then it calls the save_user method of the Database class, passing itself (self) as the argument.
- This method assumes that there's a Database class with a save_user method that accepts a User object and saves it to the database.

### load_from_database Method:

- This is a class method (decorated with @classmethod), which means it can be called on the class itself (User) rather than on an instance of the class.
- It takes the name of the user as a parameter.
- It creates an instance of the Database class.
- Then it calls the load_user method of the Database class, passing the name parameter.
- The load_user method presumably retrieves user data from the database based on the provided name and returns it.
- It then returns a new instance of the User class initialized with the retrieved name data.

## Database Class (not shown in the provided code):

### save_user Method:

- This method would typically be defined in a separate Database class.
- It accepts a User object as a parameter and saves the user data to the database.

### load_user Method:

- This method would typically be defined in the same Database class.
- It accepts the name of a user as a parameter and retrieves user data from the database based on that name.

## Coupling:

This code example demonstrates a high level of coupling between the User and Database classes. The User class is tightly coupled to the Database class because it directly creates instances of the Database class and calls its methods (save_user and load_user) within its own methods (save_to_database and load_from_database). This tight coupling can make the code harder to maintain and less flexible because changes to the Database class might require corresponding changes to the User class.


## A simple example to illustrate how changes to the Database class can affect the User class due to tight coupling:

Now, suppose there's a change in the database structure, and we need to modify the save_user method in the Database class to accept additional user information:
```python
class Database:
    def save_user(self, user, email):
        # Save user data along with email to the database
        pass

    def load_user(self, name):
        # Load user data from the database
        pass
```
Since the User class directly calls the save_user method of the Database class within its save_to_database method, the User class will need to be updated accordingly to accommodate this change:

```python
class User:
    def __init__(self, name, email):  # Update to accept email
        self.name = name
        self.email = email  # New attribute for email

    def save_to_database(self):
        database = Database()
        database.save_user(self, self.email)  # Pass email to save_user

    @classmethod
    def load_from_database(cls, name):
        database = Database()
        user_data = database.load_user(name)
        # Assuming email is also loaded from the database
        return cls(user_data['name'], user_data['email'])  # Update to accept email

```
In this example, changes to the Database class (adding an email parameter to save_user) necessitated corresponding changes to the User class to maintain compatibility. This demonstrates the tight coupling between the two classes, where changes in one class can directly impact the other, making the code less flexible and harder to maintain.
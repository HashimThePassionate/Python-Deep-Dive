# Low coupling

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

# High coupling


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

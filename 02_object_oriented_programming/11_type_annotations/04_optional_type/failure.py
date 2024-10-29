def get_user_age(name):
    user_data = database_lookup(name)
    return user_data.age  # What if user_data is None?


def database_lookup(name):
    return None  # Simulate a database lookup failure


get_user_age("Alice")  # AttributeError: 'NoneType' object has no attribute 'age'
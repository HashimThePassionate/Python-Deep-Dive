class UserData:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# Mock database as a dictionary
database = {
    "Muhammad Hashim": UserData("Muhammad Hashim", 25),
    "Alice": UserData("Alice", 30),
    "Bob": UserData("Bob", 28),
}

def database_lookup(name: str) -> UserData | None:
    return database.get(name)


def get_user_age(name: str) -> int | None:
    user_data = database_lookup(name)
    if user_data is not None:
        return user_data.age
    return None


def display_user_age(name: str):
    age = get_user_age(name)
    if age is not None:
        print(f"{name} is {age} years old. 🎉")
    else:
        print(f"User '{name}' not found. 😢")


def main():
    display_user_age("Muhammad Hashim")
    display_user_age("Alice")
    display_user_age("Unknown User")

if __name__ == "__main__":
    main()


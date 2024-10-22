# 📘 **Constraining Types** 🐍

These advanced type annotations allow you to **restrict types**, making it impossible to represent illegal states. This means fewer bugs and a smoother coding experience! ✨


## **Table of Contents** 📖

1. [Introduction](#introduction-)
2. [Optional](#1-optional-)
3. [Union](#2-union-)
4. [Literal](#3-literal-)
5. [Annotated](4-#annotated-)
6. [NewType](#5-newtype-)
7. [Final](#6-final-)
8. [Conclusion](#conclusion-)


## **Introduction** 🏁

Type annotations are more than just hints. They can be **constrained** to make your code safer by eliminating possibilities of invalid states. Let’s explore six techniques to achieve this! 🚀


## **1. Optional** ❓

The `Optional` type is used when a variable **might be `None`**, but could also be of another type. 

**Example:**
```python
from datetime import datetime

# Optional datetime can be None or a datetime object
def log_event(event: str, event_time: datetime | None = None) -> None:
    event_time = event_time or datetime.now()
    print(f"{event} happened at {event_time}")

# Examples
log_event("Server started")  # Uses current time
log_event("Error", datetime(2024, 10, 21, 18, 30))  # Uses provided time
```

**Why use it?** It clarifies that the variable could be `None`, making it **explicit** and preventing confusion.


## **2. Union** 🔀

The `Union` type (or `|` in Python 3.10+) allows a variable to be **one of multiple types**.

**Example:**
```python
# Function can accept either an int or a str
def display_id(user_id: int | str) -> None:
    print(f"User ID: {user_id}")

# Examples
display_id(1234)        # Accepts an integer
display_id("user_567")  # Accepts a string
```

**Why use it?** It allows **flexibility** when you need to support **multiple types**, while still keeping type safety.


## **3. Literal** 🔒

The `Literal` type constrains a variable to **specific values** only.

**Example:**
```python
from typing import Literal

# Function accepts only specific strings
def set_status(status: Literal["active", "inactive", "pending"]) -> None:
    print(f"Status set to: {status}")

# Examples
set_status("active")    # ✔️ Valid
set_status("inactive")  # ✔️ Valid
# set_status("unknown")  # ❌ Error: Not a valid Literal
```

**Why use it?** It restricts input to **predetermined values**, preventing invalid entries and making your functions safer.


## **4. Annotated** 🏷️

The `Annotated` type allows you to add **metadata** to your types, providing extra **context** or **restrictions**.

**Example:**
```python
from typing import Annotated
from datetime import datetime

# Assume this function will only be used within the 'UTC' timezone
def record_utc_event(event_time: Annotated[datetime, "UTC time"]) -> None:
    print(f"Event recorded at {event_time} in UTC")
```

**Why use it?** It helps convey **extra information** or **assumptions** about how a variable should be used, adding an extra layer of documentation.


## **5. NewType** 🆕

`NewType` allows you to create a **distinct type** from an existing one, which can help prevent **misuse** in different contexts.

**Example:**
```python
from typing import NewType

UserID = NewType('UserID', int)

# Function explicitly expects a UserID type
def get_user_data(user_id: UserID) -> str:
    return f"Data for user {user_id}"

# Example usage
my_user_id = UserID(1024)
print(get_user_data(my_user_id))  # ✔️ Correct

# get_user_data(1024)  # ❌ Error: Direct integer is not allowed, use UserID
```

**Why use it?** It makes your code **clearer** and prevents **mixing up** different types of IDs or other values.


## **6. Final** 🏁

The `Final` type ensures that **once a variable is set**, it **cannot be changed**. This is especially useful for **constants** or variables that shouldn’t be modified after initial assignment.

**Example:**
```python
from typing import Final

# Constants
PI: Final[float] = 3.14159
URL: Final[str] = "https://example.com"

def show_constants() -> None:
    print(f"PI: {PI}, URL: {URL}")

show_constants()

# PI = 3.14  # ❌ Error: Cannot reassign Final variable
```

**Why use it?** It prevents **unintended changes** to variables, ensuring your constants remain **constant**.


## **Conclusion** 🏁

Advanced type annotations give you more **control** over how data is used and handled in your code. By restricting **types**, you eliminate potential errors before they even have a chance to occur. This leads to **safer**, **more predictable**, and **easier-to-maintain** code. 🐍🚀

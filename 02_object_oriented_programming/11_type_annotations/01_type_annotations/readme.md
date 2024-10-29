# 📘 **Type Annotations** 🐍

In this section, we will explore **type annotations**—a feature that allows developers to specify expected types for variables, function parameters, and return values. This helps improve code **readability, maintainability**, and **robustness**, even though Python is a **dynamically typed** language. Type annotations were introduced in Python 3.5, but we will cover how they work in the latest version, Python 3.12, where typing has been simplified. Let's dive in! 🚀


## **Table of Contents** 📖

- [Introduction](#introduction-)
- [What Are Type Annotations?](#what-are-type-annotations-)
  - [Why Use Type Annotations?](#why-use-type-annotations)
- [Annotating Variables and Functions](#annotating-variables-and-functions-)
  - [Function Parameters and Return Types](#function-parameters-and-return-types)
  - [Collections and Complex Types](#collections-and-complex-types)
- [Practical Example: A Real-World Scenario](#practical-example-a-real-world-scenario-)
- [Type Checkers: Enforcing Type Annotations](#type-checkers-enforcing-type-annotations)
- [Conclusion](#conclusion-)


## **Introduction** 🏁

Python’s dynamic typing provides flexibility but can lead to **runtime errors** if incorrect types are used. **Type annotations** help address this by letting you **explicitly declare** the types you expect, which makes your code clearer for other developers and even for your future self. 💡

While type annotations don’t enforce types at runtime, they serve as **hints** and can be checked using external tools like **mypy** to catch type-related errors during development.


## **What Are Type Annotations?** 🧑‍💻

Type annotations allow you to **explicitly specify** the types of variables, function parameters, and return values. They act as **guides** for what the code expects, making it easier to **understand** and **debug**. 

Type annotations are not used by Python during runtime, meaning your code will run even if the types are incorrect. However, this can lead to unexpected behaviors, so it's best to **follow the intended usage**.

### **Why Use Type Annotations?**

1. **Improved Readability** 📖: Makes code intuitive and easier to understand.
2. **Better Tool Support** 🔧: IDEs can offer better **auto-completion** and **error checking**.
3. **Early Error Detection** 🐞: Helps catch type-related bugs before they reach production.
4. **Self-Documentation** 📝: Functions and variables describe themselves, reducing the need for external documentation.


## **Annotating Variables and Functions** 📝

### **Function Parameters and Return Types**

Let’s look at how to annotate function **parameters** and **return types**:
```python
from datetime import datetime

def close_kitchen_if_past_close(point_in_time: datetime) -> None:
    if point_in_time >= closing_time():
        close_kitchen()
        log_time_closed(point_in_time)

# Mock supporting functions for the example
def closing_time() -> datetime:
    return datetime(2024, 10, 8, 22, 0)  # Closes at 10 PM

def close_kitchen() -> None:
    print("Kitchen is closed.")

def log_time_closed(time: datetime) -> None:
    print(f"Kitchen closed at {time}.")
```

In the example above:
- `point_in_time: datetime` indicates that `point_in_time` should be of type `datetime`.
- `-> None` specifies that the function does not return a value.

**Calling the Function:**
```python
now = datetime(2024, 10, 8, 23, 30)  # Current time is 11:30 PM
close_kitchen_if_past_close(now)
# Output:
# Kitchen is closed.
# Kitchen closed at 2024-10-08 23:30:00.
```

### **Collections and Complex Types**

In Python 3.12, you can directly specify **collections** without importing from `typing`. 
```python
from datetime import datetime
import random

def schedule_restaurant_open(open_time: datetime, workers_needed: int) -> None:
    workers = find_workers_available_for_time(open_time)
    for worker in random.sample(workers, workers_needed):
        worker.schedule(open_time)

# Mock class and supporting function
class Worker:
    def __init__(self, name: str):
        self.name = name

    def schedule(self, time: datetime) -> None:
        print(f"Worker {self.name} scheduled at {time}.")

def find_workers_available_for_time(open_time: datetime) -> list[Worker]:
    return [Worker("Alice"), Worker("Bob"), Worker("Charlie")]

# Call the function
schedule_restaurant_open(datetime(2024, 10, 9, 9, 0), 2)
# Output:
# Worker Alice scheduled at 2024-10-09 09:00:00.
# Worker Bob scheduled at 2024-10-09 09:00:00.
```

For **lists** and **dictionaries**, you can annotate as follows:
```python
def get_student_scores() -> dict[str, int]:
    return {"Hashim": 90, "Ali": 85, "Zain": 92}

def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

# Calling the functions
scores = get_student_scores()
print(scores)  # Output: {'Hashim': 90, 'Ali': 85, 'Zain': 92}

average = calculate_average([90, 85, 92])
print(f"Average score: {average}")  # Output: Average score: 89.0
```


## **Practical Example: A Real-World Scenario** 🌐

Suppose you are working on a scheduling system for a restaurant:
```python
from datetime import datetime
import random

def schedule_restaurant_open(open_time: datetime, workers_needed: int) -> None:
    available_workers: list[Worker] = find_workers_available_for_time(open_time)
    if len(available_workers) < workers_needed:
        print("Not enough workers available.")
    else:
        # Use random.sample to pick the required number of workers
        for worker in random.sample(available_workers, workers_needed):
            worker.schedule(open_time)

class Worker:
    def __init__(self, name: str):
        self.name = name

    def schedule(self, time: datetime) -> None:
        print(f"Worker {self.name} scheduled at {time}.")

def find_workers_available_for_time(open_time: datetime) -> list[Worker]:
    return [Worker("Alice"), Worker("Bob"), Worker("Charlie")]

# Call the function
schedule_restaurant_open(datetime(2024, 10, 9, 9, 0), 2)
```

**Output:**
```
Worker Alice scheduled at 2024-10-09 09:00:00.
Worker Bob scheduled at 2024-10-09 09:00:00.
```


## **Type Checkers: Enforcing Type Annotations** 🛡️

**Type annotations** are not enforced by Python at runtime. Instead, you can use tools like **mypy** to check your code for type correctness during development.

### **Using `mypy` for Type Checking**
1. **Install mypy**:
   ```bash
   pip install mypy
   ```
2. **Run mypy on your Python file**:
   ```bash
   mypy your_script.py
   ```

**Example:**
```python
def add_numbers(a: int, b: int) -> int:
    return a + b

# Correct usage
print(add_numbers(5, 3))       # Output: 8

# Incorrect usage - mypy will catch this
print(add_numbers("5", 3))     # mypy error: Argument 1 to "add_numbers" has incompatible type "str"; expected "int"
```

Running `mypy` will **highlight** where types do not match, helping you catch bugs before they make it to production.


## **Conclusion** 🏁

**Type annotations** in Python 3.12 make your code more **robust** by **clarifying** what is expected, improving **readability**, and **catching bugs** early during development. While Python won’t enforce types at runtime, tools like **mypy** can be used to **validate** your annotations and ensure your code behaves as intended. 

By embracing **type annotations**, you write code that is **cleaner, self-documented,** and easier to **maintain**. Start using **type annotations** today, and make your coding experience more efficient and enjoyable! 🐍🚀
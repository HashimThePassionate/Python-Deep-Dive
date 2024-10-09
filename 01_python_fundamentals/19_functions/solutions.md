# Solutions 🚀
## 📝 **Problem: Function with Unlimited Arguments**
### 🔧 **Solution**:
```python
def accept_multiple_args(*args):
    """Print all the arguments passed to the function."""
    for arg in args:
        print(f"Argument: {arg}")

# Calling the function with different numbers of arguments
accept_multiple_args('apple', 'banana', 'cherry')
accept_multiple_args(1, 2, 3, 4, 5)
```

### 🖥 **Output**:

```
Argument: apple
Argument: banana
Argument: cherry
Argument: 1
Argument: 2
Argument: 3
Argument: 4
Argument: 5
```

### 🔍 **How It Works**:
- The `*args` in the function definition tells Python to accept any number of positional arguments and store them in a tuple called `args`.
- Inside the function, we loop through the `args` tuple and print each argument.

---

## 📝 **Problem: Restrict Function to Keyword-Only Arguments**

You want a function to **only accept certain arguments** by **keyword** and not allow positional arguments for those specific parameters.

### 🔧 **Solution**:
```python
def order_pizza(size, *, crust_type='regular', cheese=True, sauce='tomato'):
    """Summarize the pizza order, with certain keyword-only arguments."""
    print(f"\nOrdering a {size}-inch pizza.")
    print(f"Crust type: {crust_type}")
    print(f"Cheese: {'Yes' if cheese else 'No'}")
    print(f"Sauce: {sauce}")

# Correct usage with keyword arguments
order_pizza(12, crust_type='thin', cheese=False)
order_pizza(16, sauce='pesto')

# Incorrect usage: passing keyword-only arguments as positional arguments will raise an error
# order_pizza(16, 'thin', False) # This will raise a TypeError
```

### 🖥 **Output**:

```
Ordering a 12-inch pizza.
Crust type: thin
Cheese: No
Sauce: tomato

Ordering a 16-inch pizza.
Crust type: regular
Cheese: Yes
Sauce: pesto
```
### 🔍 **How It Works**:
- The `*` in the function definition tells Python that any parameter after the `*` (like `crust_type`, `cheese`, and `sauce`) **must be passed as keyword arguments**.
- If you try to pass these arguments as **positional arguments**, Python will raise a `TypeError`.
  
For example, calling `order_pizza(16, 'thin', False)` would raise an error because `crust_type` and `cheese` must be passed as **keyword arguments**, not positional arguments.

---

To attach **additional information** to the arguments of a function so that others know how it’s supposed to be used, you can use **function annotations** in Python.

---

## 📝 **Problem: Providing Additional Information for Function Arguments**

You’ve written a function but would like to attach extra information to the arguments so that others know more about how to use it (e.g., expected types, usage hints, etc.).

### 🔧 **Solution: Using Function Annotations**

Here’s an example of how to add **annotations** to your function:

```python
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given the length and width.
    
    Arguments:
    length (float): The length of the rectangle in meters.
    width (float): The width of the rectangle in meters.
    
    Returns:
    float: The area of the rectangle in square meters.
    """
    return length * width

# Calling the function
area = calculate_area(5.0, 3.0)
print(f"Area: {area} square meters")
```

### 🔍 **How It Works**:
- The `length: float` and `width: float` annotations specify that the function expects `length` and `width` to be **floats**.
- The `-> float` after the function signature indicates that the function **returns** a value of type **float**.
- These annotations serve as **hints** and documentation for other developers (or yourself) to understand the expected argument types and return type.

### 🖥 **Output**:

```
Area: 15.0 square meters
```

### 💡 **More About Function Annotations**:

- Function annotations are **optional** and don’t enforce type checking. They are just **hints**.
- You can attach annotations to any argument and the return value.
- These annotations help others **understand** how to use the function and what kinds of values are expected.

For example, you can attach any extra information or expected types to the function:

```python
def greet(name: str, age: int) -> str:
    """Greet someone by name and age."""
    return f"Hello, {name}. You are {age} years old."

print(greet("Muhammad Hashim", 24))
```

---

To return **multiple values** from a function in Python, you can use several techniques, including returning a **tuple**, a **list**, or a **dictionary**. Each method is useful depending on the context and what you want to achieve.

---

## 📝 **Problem: Returning Multiple Values from a Function**

You want to write a function that can return more than one value when it's called.

### 🔧 **Solution 1: Returning Multiple Values as a Tuple**

A tuple is a simple and effective way to return multiple values:

```python
def get_user_info():
    """Return multiple pieces of information about the user."""
    name = "Muhammad Hashim"
    age = 24
    location = "Asia"
    return name, age, location  # Returns a tuple

# Calling the function
user_name, user_age, user_location = get_user_info()

print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Location: {user_location}")
```

### 🖥 **Output**:

```
Name: Muhammad Hashim
Age: 24
Location: Asia
```

### 🔍 **How It Works**:
- The function `get_user_info()` returns a **tuple** containing three values.
- When calling the function, you can **unpack** the returned tuple into multiple variables (`user_name`, `user_age`, `user_location`).

### 🔧 **Solution 2: Returning Multiple Values as a List**

If the number of values you’re returning may vary or if you want a mutable structure, you can return a **list**:

```python
def get_user_roles():
    """Return a list of roles the user has."""
    roles = ["admin", "editor", "moderator"]
    return roles  # Returns a list

# Calling the function
user_roles = get_user_roles()
print(f"User roles: {user_roles}")
```

### 🖥 **Output**:

```
User roles: ['admin', 'editor', 'moderator']
```

### 🔧 **Solution 3: Returning Multiple Values as a Dictionary**

For more complex data, where the returned values need to have **associated keys**, you can return a **dictionary**:

```python
def get_product_details():
    """Return details of a product as a dictionary."""
    product = {
        'name': 'Laptop',
        'price': 1500,
        'available': True
    }
    return product

# Calling the function
product_info = get_product_details()
print(f"Product: {product_info['name']}")
print(f"Price: ${product_info['price']}")
print(f"Available: {product_info['available']}")
```

### 🖥 **Output**:

```
Product: Laptop
Price: $1500
Available: True
```

## 🎯 **When to Use Each Method**

- **Tuples**: Use when you want to return **fixed** values and don’t need to modify them.
- **Lists**: Use when you want to return a collection of values where the number of values may **change** or where you might want to modify the values later.
- **Dictionaries**: Use when you want to return **labeled** data (key-value pairs), making it clear what each value represents.

---

In Python, you can define a function or method with **optional arguments** by providing **default values** for those arguments in the function definition. This way, the function can be called with or without those optional arguments, and the default value will be used if no value is provided.

---

## 📝 **Problem: Defining a Function with Optional Arguments**

You want to define a function where some arguments are **optional** and can have a **default value** if not explicitly provided.

### 🔧 **Solution: Defining Optional Arguments with Default Values**

Here’s an example where we define a function to order a pizza, but some parameters (like `crust_type` and `toppings`) are **optional** with default values:

```python
def order_pizza(size, crust_type='regular', cheese=True):
    """Order a pizza with an optional crust type and cheese."""
    print(f"Ordering a {size}-inch pizza.")
    print(f"Crust type: {crust_type}")
    print(f"Cheese: {'Yes' if cheese else 'No'}")

# Calling the function with all arguments
order_pizza(12, 'thin', cheese=False)

# Calling the function with only the required argument
order_pizza(16)
```

### 🖥 **Output**:

```
Ordering a 12-inch pizza.
Crust type: thin
Cheese: No

Ordering a 16-inch pizza.
Crust type: regular
Cheese: Yes
```

### 🔍 **How It Works**:
1. **`size`**: This is a required argument with no default value.
2. **`crust_type='regular'`**: This is an optional argument with a default value of `'regular'`.
3. **`cheese=True`**: This is another optional argument, defaulting to `True`.

- If the function is called with only the required argument (`size`), Python uses the **default values** for `crust_type` and `cheese`.
- If the caller provides values for all the arguments, the provided values are used instead.

### 🔧 **Using Multiple Optional Arguments**

You can define functions with **multiple optional arguments** as well. Just make sure to put all optional arguments **after** the required ones in the function definition.

```python
def describe_pet(pet_name, animal_type='dog', age=2):
    """Describe a pet with optional parameters for type and age."""
    print(f"\nI have a {age}-year-old {animal_type} named {pet_name}.")

# Calling the function with only the required argument
describe_pet('Buddy')

# Calling the function with all arguments
describe_pet('Whiskers', 'cat', age=5)
```

### 🖥 **Output**:

```
I have a 2-year-old dog named Buddy.

I have a 5-year-old cat named Whiskers.
```

### 🔧 **Order of Parameters: Required vs. Optional**

When defining a function, **required arguments** must always come **before** optional ones. For example, this is correct:

```python
def example_func(required_arg, optional_arg='default'):
    pass
```

But this would raise a syntax error:

```python
# Incorrect! Optional arguments cannot come before required ones.
def example_func(optional_arg='default', required_arg):
    pass
```
To solve this problem, you can use **lambda functions** in Python, which are short, **anonymous functions** that allow you to specify a function **in line** without needing to define a separate one using the `def` statement.

---

## 📝 **Problem: Using a Callback Function In-Line**

You need to supply a short callback function (such as for sorting), but you want to avoid writing a separate, one-line function with `def`. You’d like a shortcut that lets you define the function directly.

### 🔧 **Solution: Using a Lambda Function for Sorting**

Let’s say you have a list of tuples, where each tuple contains a person's name and age. You want to **sort** the list by the second value (the age). Instead of writing a separate sorting function, you can use a **lambda function** directly in the `sort()` call:

```python
people = [('Muhammad Hashim', 24), ('Ayesha', 30), ('Ali', 20), ('Sara', 28)]

# Using a lambda function to sort by the second item (age)
people.sort(key=lambda person: person[1])

# Printing the sorted list
print(people)
```

### 🖥 **Output**:

```
[('Ali', 20), ('Muhammad Hashim', 24), ('Sara', 28), ('Ayesha', 30)]
```

### 🔍 **How It Works**:
- **`lambda person: person[1]`**: This lambda function takes a `person` (which is a tuple) and returns the second element (`person[1]`, the age). This function is used as the `key` for sorting the list.
- The `lambda` function is defined **in line** and used directly without needing to create a separate named function.

### 🔧 **Solution: Using a Lambda Function with `map()`**

You can also use a lambda function with operations like `map()` to apply a function to each element in a list.

```python
numbers = [1, 2, 3, 4, 5]

# Using a lambda function to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Printing the result
print(squared_numbers)
```

### 🖥 **Output**:

```
[1, 4, 9, 16, 25]
```

### 🔍 **How It Works**:
- **`lambda x: x ** 2`**: This lambda function takes each element `x` from `numbers` and returns its square (`x ** 2`).
- The `lambda` function is passed directly to `map()` without creating a separate function.

### 🔧 **Solution: Using a Lambda Function with `filter()`**

Lambda functions can also be used to filter elements based on a condition:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Printing the result
print(even_numbers)
```

### 🖥 **Output**:

```
[2, 4, 6, 8, 10]
```

### 🔍 **How It Works**:
- **`lambda x: x % 2 == 0`**: This lambda function checks if a number `x` is even by using the modulo operation.
- The `lambda` function is passed directly to `filter()` to return only the numbers that satisfy the condition.

---

To capture the values of variables at the time of defining a **lambda function**, you need to ensure that the **current value** of the variable is "frozen" at the time of the lambda’s creation. If you don't handle it carefully, the lambda may capture a **reference** to the variable instead of its **current value**, which could lead to unintended behavior when the variable changes later.

---

## 📝 **Problem: Capturing Variable Values in Lambda Functions**

You want to define a **lambda function**, but also ensure that certain variables' values are captured **at the time of definition**, so that the function behaves as expected even if the variable changes later.

🔧 **Solution: Capturing Variable Values Using Default Arguments**

When defining a **lambda function**, you can use **default arguments** to capture the current value of a variable. This ensures that the lambda retains the value as it was when the lambda was created, even if the variable changes later.

Here’s how you can do it:

```python
# Define a variable
factor = 10

# Create a lambda function that captures the current value of 'factor'
multiply = lambda x, factor=factor: x * factor

# Change the value of 'factor' after defining the lambda
factor = 20

# Call the lambda function
print(multiply(5))  # This will still use the original value of factor (10)
```

### 🖥 **Output**:

```
50
```

### 🔍 **How It Works**:
- **`lambda x, factor=factor: x * factor`**: The default value for `factor` is set to the **current value** of `factor` (which is 10) at the time of the lambda’s creation.
- Even though `factor` is later changed to 20, the lambda still uses the **captured value** of 10 because the default argument stores the value.

### 🔧 **Example: Capturing Variables in a Loop**

This problem commonly occurs when using lambdas inside loops, where you want each lambda to capture the **current iteration value**. Without the proper capture, all lambdas may reference the **final value** of the loop variable.

Here’s how you can properly capture values inside a loop using default arguments:

```python
# Create a list of lambda functions that multiply by i
lambdas = []
for i in range(5):
    lambdas.append(lambda x, i=i: x * i)  # Capture the current value of i

# Call each lambda with a value of 2
for func in lambdas:
    print(func(2))
```

### 🖥 **Output**:

```
0
2
4
6
8
```

### 🔍 **How It Works**:
- **`lambda x, i=i: x * i`**: Here, the default argument `i=i` captures the value of `i` **at each iteration** of the loop.
- As a result, each lambda function holds the correct value of `i` for that iteration, ensuring that each lambda behaves as expected when called.

## 🎯 **Why Use This Approach?**

When defining a **lambda function** in Python, using **default arguments** is a reliable way to **freeze** the values of variables at the time of the lambda’s definition. This ensures that the lambda’s behavior doesn’t change unexpectedly if those variables change later in the program.

---

To solve the problem where a **callable** (such as a function) takes too many arguments and causes an exception when used as a **callback** or **handler**, you can use techniques like **`functools.partial`** or a **lambda function** to reduce the number of arguments passed to the callable.

---

## 📝 **Problem: Handling a Callable That Takes Too Many Arguments**

You want to use a callable (like a function) with another piece of code, such as a callback or handler, but the callable takes **too many arguments**, causing an exception when it’s called with fewer arguments.

### 🔧 **Solution 1: Using `functools.partial` to Pre-Fill Arguments**

The `functools.partial()` function lets you create a new version of a callable with **fewer arguments** by **pre-filling** some of the arguments. This allows you to use a function that takes too many arguments by reducing the number of required arguments.

```python
import functools

def full_function(a, b, c):
    """A function that takes three arguments."""
    print(f"a = {a}, b = {b}, c = {c}")

# Use functools.partial to create a new version of the function with 'a' pre-filled
partial_function = functools.partial(full_function, a=1)

# Now we can call the partial function with fewer arguments (only b and c)
partial_function(b=2, c=3)
```

### 🖥 **Output**:

```
a = 1, b = 2, c = 3
```

### 🔍 **How It Works**:
- **`functools.partial(full_function, a=1)`**: This creates a new function `partial_function` where the first argument (`a`) is pre-filled with the value `1`.
- Now, when `partial_function()` is called, it only needs to provide the remaining arguments (`b` and `c`).

### 🔧 **Solution 2: Using a Lambda Function to Reduce Arguments**

You can also use a **lambda function** to wrap the original callable and control how many arguments are passed to it. This is useful for callback functions or event handlers.

```python
def full_function(a, b, c):
    """A function that takes three arguments."""
    print(f"a = {a}, b = {b}, c = {c}")

# Create a lambda to reduce the number of arguments to the callable
callback_function = lambda b, c: full_function(1, b, c)

# Now call the lambda function with two arguments
callback_function(2, 3)
```

### 🖥 **Output**:

```
a = 1, b = 2, c = 3
```

### 🔍 **How It Works**:
- **`lambda b, c: full_function(1, b, c)`**: The lambda function wraps `full_function()` and "locks in" the value of `a` to `1`. This way, when the lambda is called with only `b` and `c`, it internally calls `full_function()` with all three arguments.
- This allows you to use `full_function()` in contexts where fewer arguments are passed.

### 🔧 **Solution 3: Ignoring Extra Arguments**

If the callback or handler might pass **extra arguments** that your function doesn’t need, you can modify the function to accept `*args` and ignore the extra arguments:

```python
def simple_function(a, b):
    """A function that only needs two arguments."""
    print(f"a = {a}, b = {b}")

# Modify the function to accept extra arguments using *args
def handler_function(a, b, *args):
    """This function ignores extra arguments."""
    print(f"a = {a}, b = {b}")

# Call the function with extra arguments
handler_function(1, 2, 3, 4)  # Extra arguments are ignored
```

### 🖥 **Output**:

```
a = 1, b = 2
```

### 🔍 **How It Works**:
- **`*args`** allows the function to accept any number of additional arguments without raising an exception. These extra arguments are ignored.
- This approach is useful if you don’t care about the extra arguments passed by the callback or event handler.

---

To solve the problem where you want a **callback function** (such as an event handler or completion callback) to carry **extra state** for use inside the callback function, you can use several techniques. These include using **closures**, **functools.partial**, or creating a **class** to encapsulate the state.

---

## 📝 **Problem: Callback Functions with Extra State**

You need to write a callback function, such as an event handler or completion callback, that carries **extra state** (data or context) for use inside the callback function.

### 🔧 **Solution 1: Using Closures to Carry Extra State**

A **closure** allows you to create a function that captures variables from its surrounding scope. This means that a callback function can "remember" the state that was available at the time of its definition.

```python
def create_callback(extra_data):
    """Return a callback function that uses extra state."""
    def callback(event):
        print(f"Event: {event}")
        print(f"Extra data: {extra_data}")
    return callback

# Create a callback with extra state
my_callback = create_callback(extra_data="Some important info")

# Simulate calling the callback with an event
my_callback("User clicked a button")
```

### 🖥 **Output**:

```
Event: User clicked a button
Extra data: Some important info
```

### 🔍 **How It Works**:
- The `create_callback()` function defines a **closure** that captures the `extra_data` parameter.
- When `callback(event)` is called later, it still has access to `extra_data` that was provided when the callback was created.
- This allows the callback to carry **extra state** without needing to pass additional arguments during the callback itself.

### 🔧 **Solution 2: Using `functools.partial` to Pre-Fill Extra State**

The `functools.partial()` function allows you to pre-fill some arguments of a function, effectively "carrying" extra state into the callback without needing to modify the function definition.

```python
import functools

def my_callback(event, extra_data):
    """A callback function that uses extra data."""
    print(f"Event: {event}")
    print(f"Extra data: {extra_data}")

# Pre-fill the extra_data argument using functools.partial
callback_with_state = functools.partial(my_callback, extra_data="Stateful data")

# Simulate calling the callback with an event
callback_with_state("File uploaded")
```

### 🖥 **Output**:

```
Event: File uploaded
Extra data: Stateful data
```

### 🔍 **How It Works**:
- **`functools.partial()`** creates a new version of `my_callback()` where the `extra_data` argument is pre-filled with `"Stateful data"`.
- When the callback is called later with an event (e.g., `"File uploaded"`), the **pre-filled** `extra_data` is passed automatically, allowing the callback to use the extra state.

### 🔧 **Solution 3: Using a Class to Store Extra State**

Another approach is to use a **class** to encapsulate the callback logic and state together. This allows you to store and manage **state** across multiple calls to the callback function.

```python
class EventHandler:
    def __init__(self, extra_data):
        self.extra_data = extra_data

    def handle_event(self, event):
        """Callback method that uses extra state."""
        print(f"Event: {event}")
        print(f"Extra data: {self.extra_data}")

# Create an instance of the handler with extra state
handler = EventHandler(extra_data="Important event data")

# Simulate calling the callback method
handler.handle_event("User logged in")
```

### 🖥 **Output**:

```
Event: User logged in
Extra data: Important event data
```

### 🔍 **How It Works**:
- The `EventHandler` class stores the **extra state** (`extra_data`) as an instance variable.
- The `handle_event()` method is the callback function, and it can access `self.extra_data` to use the state.
- This approach works well when you need a more **object-oriented** structure or when the callback requires more complex behavior.

---

To solve the problem of managing **callback functions** in a way that keeps your code **clear** and **sequential**, avoiding the proliferation of small functions and complex control flow, you can use techniques such as **coroutines**, **async/await** syntax, or even **promises** (in asynchronous frameworks like JavaScript). In Python, using **generators**, **coroutines**, or **asyncio** allows you to write code that behaves like callbacks internally but **looks procedural**, making it easier to follow.

---

## 📝 **Problem: Simplifying Control Flow with Callbacks**

You are using **callback functions** but want to make the code look more like a normal, sequential flow of operations to avoid the confusion caused by too many small functions and complex control flow.
### 🔧 **Solution 1: Using `asyncio` and `async/await` for Procedural-Like Flow**

The **`asyncio`** module in Python allows you to write asynchronous code using the **`async/await`** syntax. This makes your code look like a normal sequence of steps while handling asynchronous operations internally, avoiding the need for many small callbacks.

Here’s how you can use **`async/await`** to structure asynchronous code in a more readable, procedural way:

```python
import asyncio

async def fetch_data():
    """Simulate an asynchronous data fetch operation."""
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a delay
    print("Data fetched.")
    return {"data": "Sample data"}

async def process_data():
    """Process the data in a sequential manner."""
    print("Processing started.")
    data = await fetch_data()
    print(f"Processing {data}")
    await asyncio.sleep(1)  # Simulate processing time
    print("Processing completed.")

# Main event loop to run the async function
asyncio.run(process_data())
```

### 🖥 **Output**:

```
Processing started.
Fetching data...
Data fetched.
Processing {'data': 'Sample data'}
Processing completed.
```

### 🔍 **How It Works**:
- The **`async`** keyword is used to define **asynchronous functions**.
- The **`await`** keyword pauses the function execution until the awaited operation (like `fetch_data()`) completes. This allows the function to run **sequentially**, even though it's asynchronous.
- This approach provides **sequential control flow** that reads like normal procedural code, avoiding the complexity of managing multiple small callback functions.

### 🔧 **Solution 2: Using Generators as Coroutines**

In Python, you can use **generators** to write code that behaves like a coroutine. This allows you to **yield** control and wait for asynchronous events, while keeping the code **sequential** and easy to follow.

```python
def task_coroutine():
    print("Starting task...")
    result = yield "Task in progress"
    print(f"Task result: {result}")
    yield "Task completed"

# Simulate running the coroutine
coroutine = task_coroutine()

# Start the coroutine
print(next(coroutine))  # Output: "Task in progress"

# Resume the coroutine and send the result
print(coroutine.send("Success"))
```

### 🖥 **Output**:

```
Starting task...
Task in progress
Task result: Success
Task completed
```

### 🔍 **How It Works**:
- The `yield` statement in the **generator** acts like a pause in execution, similar to **`await`**.
- The **`send()`** method allows you to **resume** the coroutine and pass data back into the function, similar to how callbacks work.
- This approach allows you to break up complex tasks into **sequential steps** while still maintaining the procedural flow of the code.

---

To solve the problem of extending a **closure** with functions that allow the **inner variables** to be **accessed** and **modified**, you can achieve this by returning a set of functions from the closure. These functions will have access to the **enclosed variables** and can be designed to get, set, or update the values inside the closure.

Closures in Python allow you to encapsulate variables and retain their state, but to make those variables more accessible (like getters and setters in object-oriented programming), you can return **multiple functions** from the closure that interact with the internal state.

---

## 📝 **Problem: Extending a Closure to Access and Modify Inner Variables**

You want to write a closure that encapsulates inner variables, but also provide **functions** to **access** and **modify** those inner variables from outside the closure.

### 🔧 **Solution: Extending a Closure with Getters and Setters**

You can return multiple functions from a closure to interact with the internal variables:

```python
def counter_closure():
    count = 0  # Inner variable in the closure

    def get_count():
        """Return the current value of count."""
        return count

    def increment():
        """Increment the count by 1."""
        nonlocal count  # Declare that we want to modify the enclosed variable
        count += 1
        return count

    def reset():
        """Reset the count to 0."""
        nonlocal count
        count = 0

    # Return the functions to access and modify the inner variable
    return get_count, increment, reset

# Create a closure instance
get_count, increment, reset = counter_closure()

# Use the closure functions
print(get_count())  # Output: 0
print(increment())  # Output: 1
print(increment())  # Output: 2
reset()
print(get_count())  # Output: 0
```

### 🖥 **Output**:

```
0
1
2
0
```

### 🔍 **How It Works**:
- **`counter_closure()`** defines an inner variable `count` that is enclosed by the returned functions.
- **`get_count()`** allows the inner variable `count` to be accessed.
- **`increment()`** allows the inner variable `count` to be modified (incremented), using the `nonlocal` keyword to modify the enclosed variable.
- **`reset()`** allows the inner variable `count` to be reset to its original value.
- The closure functions can **access** and **modify** the inner state while preserving encapsulation.


### 🔧 **Using Closures for Encapsulated State Management**

Closures are a powerful tool for encapsulating state, and extending them with additional functions can turn them into **state managers**. For example, you can create a **bank account** closure that manages a balance and provides functions to deposit, withdraw, and check the balance.

```python
def bank_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        """Deposit money into the account."""
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        """Withdraw money from the account."""
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance

    def get_balance():
        """Return the current balance."""
        return balance

    return deposit, withdraw, get_balance

# Create an account with an initial balance of 100
deposit, withdraw, get_balance = bank_account(100)

# Use the closure functions
print(get_balance())  # Output: 100
print(deposit(50))    # Output: 150
print(withdraw(30))   # Output: 120
print(withdraw(200))  # Output: Insufficient funds
print(get_balance())  # Output: 120
```

### 🖥 **Output**:

```
100
150
120
Insufficient funds
120
```

### 🔍 **How It Works**:
- **`balance`** is encapsulated within the closure and can only be accessed or modified via the **closure functions** (`deposit`, `withdraw`, `get_balance`).
- **`deposit()`** and **`withdraw()`** modify the balance using the `nonlocal` keyword to refer to the enclosed `balance` variable.
- **`get_balance()`** provides read access to the encapsulated balance.
  
This pattern mimics the behavior of **class methods** without needing to define a class, while still maintaining encapsulation and control over the internal state.

---

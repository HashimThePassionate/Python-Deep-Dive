# 📦 **Storing Your Functions in Modules in Python**

## 🛠 **Why Store Functions in Modules?**

Storing your functions in a separate file, known as a **module**, allows you to organize your code better and reuse functions across multiple programs. Modules also help hide the details of your code, allowing you to focus on the higher-level logic of your program. Once your functions are stored in a module, you can import them into your main program or share them with others easily.

## 📝 **How to Create and Import a Module**

A **module** is simply a Python file that contains functions. You can create a module by writing your functions in a `.py` file, and then **import** that file into other Python programs.

Let’s go through an example where we store a function for making pizzas in a module and then import it into another program.

### 1. **Creating the Module**

First, we’ll create a file called `pizza.py` that contains the `make_pizza()` function:

```python
# pizza.py
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

Now we have a module `pizza.py` that contains a function for making pizzas. We can import this module into other programs.

### 2. **Importing the Module**

Next, we’ll create a file called `making_pizzas.py` where we import the `pizza` module and call the `make_pizza()` function.

```python
# making_pizzas.py
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 🔍 **How It Works**:
1. **`import pizza`**: This tells Python to import the `pizza.py` file into the current program.
2. **Calling the function**: To use the `make_pizza()` function from the `pizza` module, we call it using `pizza.make_pizza()`. The syntax is `module_name.function_name()`.

### 🖥 **Output**:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

By separating the pizza-making logic into the `pizza.py` module, we’ve made our code more modular and reusable.

## 🔄 **Advantages of Using Modules**

1. **Organization**: By storing functions in separate files (modules), your main program remains clean and focused on higher-level logic.
2. **Reusability**: You can reuse functions across different programs by importing the module.
3. **Collaboration**: Sharing modules is easier. You can give others access to specific functions without sharing the entire program.
4. **Maintenance**: If the function needs to be updated, you can update it in one place (the module), and every program that imports it will benefit from the update.

## 🎯 **Calling Functions from Modules**

Once you import a module, you can call any function within it using the following syntax:

```python
module_name.function_name()
```

For example, in our case, we use:

```python
pizza.make_pizza(16, 'pepperoni')
```

This tells Python to use the `make_pizza()` function from the `pizza` module.

## 💡 **Try It Yourself!**

### 1. **Creating a Sandwich Module**

Create a module `sandwich.py` that contains a function for making sandwiches:

```python
# sandwich.py
def make_sandwich(*ingredients):
    """Summarize the sandwich being made."""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
```

Next, create a program called `making_sandwiches.py` that imports the `sandwich` module and calls the function:

```python
# making_sandwiches.py
import sandwich

sandwich.make_sandwich('ham', 'cheese', 'lettuce')
sandwich.make_sandwich('turkey', 'tomato', 'mayo')
```

### 2. **Creating a Car Module**

Create a module `car.py` that stores information about a car:

```python
# car.py
def describe_car(manufacturer, model, **options):
    """Build a dictionary containing car information."""
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(options)
    return car_info
```

In another file, import the module and describe a car:

```python
# describing_car.py
import car

car_info = car.describe_car('tesla', 'model s', color='red', autopilot=True)
print(car_info)
```

---

# 📦 **Importing Specific Functions in Python**

## 🛠 **Why Import Specific Functions?**

When working with modules, you can import **specific functions** instead of the entire module. This is useful when you only need to use a few functions from a module. By importing just what you need, you can write cleaner and more focused code.

## 📝 **How to Import Specific Functions**

The general syntax for importing specific functions from a module looks like this:

```python
from module_name import function_name
```

You can also import multiple specific functions by separating them with commas:

```python
from module_name import function_0, function_1, function_2
```

### **Example: Importing `make_pizza()` Function**

Let’s take our pizza example. If you only want to use the `make_pizza()` function from the `pizza.py` module, you can import it like this:

```python
# Importing only the make_pizza function from the pizza module
from pizza import make_pizza

# Now we can call make_pizza() directly
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 🖥 **Output**:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

### 🔍 **How It Works**:
- **`from pizza import make_pizza`**: This imports only the `make_pizza()` function from the `pizza.py` module.
- Because we explicitly imported the function, there’s no need to use the dot notation (`pizza.make_pizza()`), and we can call `make_pizza()` directly.

## 🔄 **Importing Multiple Specific Functions**

You can import multiple functions from a module by listing them in the import statement, separated by commas:

```python
from pizza import make_pizza, add_toppings, bake_pizza
```

Now you can call each of these functions directly without the need for dot notation.

## 🎯 **Why Use This Approach?**

- **Clean Code**: You only import what you need, which makes your code more focused and easier to read.
- **No Dot Notation**: You can call the function directly by name, making the code more concise.

However, if you’re going to use several functions from a module, it might be better to import the entire module to keep the code more maintainable.

## 💡 **Try It Yourself!**

### 1. **Importing Specific Functions from a Sandwich Module**

Let’s create a `sandwich.py` module with multiple functions:

```python
# sandwich.py
def make_sandwich(*ingredients):
    """Summarize the sandwich being made."""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

def add_sauce(sauce):
    """Add a sauce to the sandwich."""
    print(f"Adding {sauce} sauce to the sandwich.")
```

Now, in another file, import only the functions you need:

```python
from sandwich import make_sandwich, add_sauce

make_sandwich('turkey', 'cheese', 'lettuce')
add_sauce('mayo')
```

### 🖥 **Output**:

```
Making a sandwich with the following ingredients:
- turkey
- cheese
- lettuce

Adding mayo sauce to the sandwich.
```
---

# 🔄 **Using `as` to Give a Function or Module an Alias in Python**

## 🛠 **Why Use Aliases in Python?**

In Python, you can use the `as` keyword to give a function or module an **alias**. This is especially useful when:
- The function or module name is long.
- You want to avoid conflicts with other names in your code.
- You want to make your code **shorter** and more **readable**.

By using an alias, you can call a function or module by a **shorter name**, making it easier to work with.

## 📝 **Example: Giving a Function an Alias**

Let’s say you have the `make_pizza()` function, but it has a long name, or it might conflict with another function in your code. You can give it an **alias** using `as` to make it shorter:

```python
from pizza import make_pizza as mp

# Calling the function using its alias
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 🔍 **How It Works**:
1. The `make_pizza()` function is imported and given the alias `mp`.
2. Now, instead of calling `make_pizza()`, you can simply call `mp()`.
3. The alias makes the code more concise, and there’s no conflict with other function names.

### 🖥 **Output**:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

## 📝 **Giving a Module an Alias**

You can also give an **entire module** an alias using the same approach. This is particularly useful when the module name is long, or you want to make function calls from the module more concise.

```python
import pizza as p

# Calling the function from the module using its alias
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 🔍 **How It Works**:
1. The entire `pizza` module is given the alias `p`.
2. Now, you can call any function from the `pizza` module by using `p.function_name()`.
3. This reduces the need to type the full module name repeatedly, keeping the code shorter and more focused on the function names.

## 💡 **Importing All Functions from a Module**

If you want to import **all functions** from a module, you can use the asterisk (`*`), but be cautious! This can sometimes lead to **naming conflicts**.

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

While this allows you to call functions without the module name or alias, it’s generally not recommended for large modules, as it can overwrite existing function names in your program.

---
# 🎨 **Styling Functions in Python**

## 🛠 **Why Style Your Functions?**

Styling your functions properly is crucial for writing **readable**, **maintainable**, and **understandable** code. Python has a style guide called **PEP 8** that outlines best practices for naming, commenting, and structuring functions. These conventions ensure that your code is clean, easy to follow, and collaborative-friendly.

## 📝 **Best Practices for Function Styling**

Here are the key guidelines for styling your functions in Python:

### 1. **Descriptive Function Names**

Functions should have **descriptive names** that clearly indicate what the function does. Use **lowercase letters** and **underscores** to separate words.

```python
# Good function name
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Avoid function names that are too vague or unclear
def mp():
    # Not descriptive
    pass
```
### 2. **Docstrings for Documentation**

Every function should have a **docstring** immediately following the function definition. This docstring should **concise** and explain what the function does, what parameters it takes, and what it returns (if applicable).

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
```

- The docstring allows other developers to understand the purpose of the function without having to read the code itself.
- This is especially useful when you collaborate with others or revisit your code after a long time.

### 3. **Using Default Values**

When specifying default values for parameters, **no spaces** should be used around the `=` sign:

```python
# Correct way
def make_sandwich(bread_type, fillings='cheese'):
    """Make a sandwich with a specific bread and fillings."""
    print(f"Making a {bread_type} sandwich with {fillings}.")

# Incorrect way
def make_sandwich(bread_type, fillings = 'cheese'):
    pass
```

This convention also applies to **keyword arguments** in function calls:

```python
make_sandwich('whole wheat', fillings='turkey')
```

### 4. **Line Length and Formatting**

PEP 8 recommends limiting each line of code to **79 characters** for readability. If a function has too many parameters and exceeds this limit, you can break the line after the opening parenthesis and indent the next line.

```python
def describe_car(
        manufacturer, model, year, color, engine_type):
    """Display car details."""
    print(f"{manufacturer} {model}, {year}, {color}, {engine_type}")
```

### 5. **Separate Functions with Blank Lines**

When you have multiple functions in a module, separate them with **two blank lines** to improve readability.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    pass


def make_sandwich(bread_type, fillings='cheese'):
    """Make a sandwich with a specific bread and fillings."""
    pass
```

### 6. **Import Statements**

All **import statements** should be placed at the **beginning** of the file. The only exception is if the file starts with comments that describe the overall program.

```python
# Correct placement of imports
import os
import sys

# Program starts here
def main():
    pass
```

## 💡 **Try It Yourself!**

### 1. **Printing Models Example**

Move the `print_models()` and `show_completed_models()` functions from the `printing_models.py` example into a separate file called `printing_functions.py`. Then, use the following import styles in the main program:
- `import printing_functions`
- `from printing_functions import print_models`
- `from printing_functions import print_models as pm`
- `import printing_functions as pf`
- `from printing_functions import *`

---

## 📋 **Key Points**:
- Use **descriptive function names** that use lowercase letters and underscores.
- Add **docstrings** immediately after the function definition to describe what the function does.
- Avoid spaces around the `=` sign when using **default parameter values**.
- Keep **line length** under 79 characters, and use proper indentation for longer function definitions.
- Separate functions with **two blank lines** for clarity.
- Place all **import statements** at the beginning of your file.

Following these guidelines ensures that your code remains clean, readable, and easy to maintain, especially when working in teams or revisiting your projects later! 🚀

---


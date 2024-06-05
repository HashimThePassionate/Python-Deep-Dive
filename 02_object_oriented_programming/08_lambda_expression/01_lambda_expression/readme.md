# What is lambda expression?

In Python, a lambda expression is a concise way to create small anonymous functions. They are defined using the `lambda` keyword followed by parameters (if any), a colon `:`, and then the expression or code block.

Let's break down your code:

```python
# Define the Printer interface as a function type
Printer = lambda message: print(message)
```

Here, you're using a lambda expression to define a function `Printer` that takes a single parameter `message` and prints it using the `print` function. This lambda expression essentially creates a function that behaves similarly to a regular function defined with `def`.

```python
# Define the greet function
def greet(printer):
    printer('Hashim')
```

You've defined a function called `greet` which takes a single parameter called `printer`. Inside `greet`, you're calling the `printer` function with the string `'Hashim'`.

```python
# Define the show function
def show():
    # Call the greet function with a lambda expression
    greet(lambda message: print("Hey " + message))
```

The `show` function is defined here. Inside `show`, you're calling the `greet` function with a lambda expression as an argument. This lambda expression takes a single parameter `message` and concatenates the string `"Hey "` with the `message` before printing it.

```python
# Call the show function to execute the code
show()
```

Finally, you're calling the `show` function to execute the code. This will trigger the `show` function, which in turn calls the `greet` function with a lambda expression, resulting in the message `"Hey Hashim"` being printed.

In summary, lambda expressions are used here to define small, one-time-use anonymous functions, particularly useful when you need to pass a simple function as an argument to another function, like in this example.
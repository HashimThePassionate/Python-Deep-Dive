# Treating a Function Like an Object in Python

## Understanding Functions as Objects

In Python, functions are treated as objects. This means they have attributes and can be manipulated like any other object in the language.

### Creating and Testing a Function

Let's create a function, call it, read its `__doc__` attribute, and check its type.

#### Example 7-1: Create and Test a Function

```python
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)

# Calling the function
print(factorial(4))  # Output: 24

# Reading the __doc__ attribute
print(factorial.__doc__)  # Output: 'returns n!'

# Checking the type of the function
print(type(factorial))  # Output: <class 'function'>
```

- **Runtime Creation:** This example shows that we are creating a function at runtime.
- **`__doc__` Attribute:** This attribute is used to generate the help text of an object.
- **Function Class Instance:** The `factorial` function is an instance of the function class.

### Using the `__doc__` Attribute

The `__doc__` attribute contains the documentation string for the function. This can be used to generate help text.

```python
help(factorial)
```

Running `help(factorial)` in the Python console will display a help screen generated from the `__doc__` attribute of the function.

### Treating Functions as First-Class Objects

Functions in Python can be assigned to variables, passed as arguments to other functions, and used in various ways that highlight their first-class nature.

#### Example 7-2: Using Functions as First-Class Objects

```python
# Assigning the function to a variable
fact = factorial
print(fact)  # Output: <function factorial at 0x...>
print(fact(5))  # Output: 120

# Passing the function as an argument to map
result = map(factorial, range(11))
print(result)  # Output: <map object at 0x...>
print(list(result))  # Output: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
```

- **Variable Assignment:** The `factorial` function is assigned to the variable `fact`.
- **Function as an Argument:** The `factorial` function is passed as an argument to the `map` function.
  - `map(function, iterable)` returns an iterable where each item is the result of calling the function on each element of the iterable.

## Importance of First-Class Functions

Having first-class functions allows for programming in a functional style. One hallmark of functional programming is the use of higher-order functions, which we will discuss next.

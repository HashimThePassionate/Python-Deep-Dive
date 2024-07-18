def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)

# Calling the function
print(factorial(4))  # Output: 24

# Reading the __doc__ attribute
print(factorial.__doc__)  # Output: 'returns n!'

# Checking the type of the function
print(type(factorial))  # Output: <class 'function'>

help(factorial)


# Assigning the function to a variable
fact = factorial
print(fact)  # Output: <function factorial at 0x...>
print(fact(5))  # Output: 120

# Passing the function as an argument to map
result = map(factorial, range(11))
print(result)  # Output: <map object at 0x...>
print(list(result))  # Output: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

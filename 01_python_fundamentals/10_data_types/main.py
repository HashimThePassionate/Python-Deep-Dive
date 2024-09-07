x = 42  # x is an object of type 'int'
y = "Hello"  # y is an object of type 'str'


x = 42  # Immutable integer object
y = "Hello"  # Immutable string object

x = x + 1  # x now points to a new integer object 43
y += " World"  # y now points to a new string object "Hello World"


x = 42
print(type(x))  # Output: <class 'int'>
print(isinstance(x, int))  # Output: True



x = 42  # Original immutable integer object
original_x = x  # Storing the original value in a different variable

x = x + 1  # Now x points to a new integer object 43

print("Current x:", x)  # Output: Current x: 43
print("Original x:", original_x)  # Output: Original x: 42



# Decimal integer literals
print(1, 23, 3493)

# Binary integer literals
print(0b010101, 0b110010)

# Octal integer literals
print(0o1, 0o27, 0o6645)

# Hexadecimal integer literals
print(0x1, 0x17, 0xDA5)


# Examples of floating-point literals
print(0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0e0)
# Output: 0.0 0.0 0.0 1.0 1.0 1.0 1.0 1.0


# Examples of imaginary literals
print(0j, 0.j, 0.0j, .0j, 1j, 1.j, 1.0j, 1e0j, 1.e0j, 1.0e0j)

# Complex numbers
print(1+0j, 1.0+0.0j)


print(100_000.000_0001, 0x_FF_FF, 0o7_777, 0b_1010_1010)
# Outputs: (100000.0000001, 65535, 4095, 170)


print('hello')       # Single-quoted string
print("world")       # Double-quoted string
print("""Good
night""")  # Triple-quoted string, spans multiple lines



is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>
print(is_python_fun and False)  # Output: False
print(not is_python_fun)  # Output: False




x = 42  # Immutable integer object
y = [1, 2, 3]  # Mutable list obj

x = 42
print(type(x))  # <class 'int'>
print(isinstance(x, int))  # Tr

1, 23, 3493        # Decimal integer literals
0b010101, 0b110010 # Binary integer literals
0o1, 0o27, 0o6645  # Octal integer literals
0x1, 0x17, 0xDA5   # Hexadecimal integer literals


0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0e0  # Floating-point literals


0j, 0.j, 0.0j, .0j, 1j, 1.j, 1.0j, 1e0j, 1.e0j, 1.0e0j  # Imaginary literals

100_000.000_0001, 0x_FF_FF, 0o7_777, 0b_1010_1010
# Outputs: (100000.0000001, 65535, 4095, 170)


'hello'       # Single-quoted string
"world"       # Double-quoted string
"""Good
night"""      # Triple-quoted string, spans multiple lines

[42, 3.14, 'hello']  # List with different types of elements
[] 


100, 200, 300  # Tuple
()    


{1, 2, 4, 8, 'string'}  # Set with different types of elements


empty_set = set()  # Correct way to create an empty set
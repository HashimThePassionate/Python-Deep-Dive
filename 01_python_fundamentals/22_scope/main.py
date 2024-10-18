import builtins

# Safely using built-ins after overriding
open = "Overridden Open"  # Overrides the built-in open
print(open)  # Prints the string

# Access the original built-in open
with builtins.open("example.txt", "w") as file:
    file.write("This is safe!")

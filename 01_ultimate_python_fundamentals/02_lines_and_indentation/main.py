x = 10  # This is a comment
y = 20  # Python will ignore everything after the hash sign


# Using a backslash to continue the statement
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Using parentheses to continue the statement
total = (1 + 2 + 3 +
         4 + 5 + 6)


text = """This is a long string
that spans multiple lines."""


if x > 0:
    print("Positive number")
    y = x
else:
    print("Non-positive number")
    y = 0

def greet(name):
    print(f"Hello, {name}!")  # Correct: 4 spaces for indentation

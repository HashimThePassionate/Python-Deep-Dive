# Define the Printer interface as a function type
Printer = lambda message: print(message)

# Define the greet function
def greet(printer):
    printer('Hashim')

# Define the show function
def show():
    # Call the greet function with a lambda expression
    greet(lambda message: print("Hey " + message))

# Call the show function to execute the code
show()

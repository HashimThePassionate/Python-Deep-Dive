x = 42       # x is a reference to an integer object
x = "hello"  # x is now a reference to a string object

x = 10    # Binding: x is now a reference to the integer 10
x = 20    # Rebinding: x is now a reference to the integer 20

x = 10    # x is bound to the integer 10
del x     # x is unbound, and the name x no longer exists

x = [1, 2, 3]  # x is bound to a list object
y = x          # y is also bound to the same list object
del x          # x is unbound, but the list object still exists because y refers to 

global_var = "I am global"  # Global variable

def my_function():
    local_var = "I am local"  # Local variable
    print(local_var)

my_function()  # Outputs: I am local
print(global_var)  # Outputs: I am global
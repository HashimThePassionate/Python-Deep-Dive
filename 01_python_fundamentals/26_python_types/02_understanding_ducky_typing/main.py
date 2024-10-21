from typing import Iterable
def print_items(items: Iterable):
    for item in items:
        print(item)
        print(" ",end='')

print_items([1, 2, 3])            # List input
print_items({4, 5, 6})            # Set input
print_items({"A": 1, "B": 2})     # Dictionary input

# This will raise an error because an integer is not iterable.
# print_items(5)  
# Output: TypeError: 'int' object is not iterable

def double_value(value):
    return value + value

print(double_value(5))            # Output: 10
print(double_value("abc"))        # Output: abcabc
print(double_value([1, 2, 3]))    # Output: [1, 2, 3, 1, 2, 3]

import re

# Custom replacement function
def multiply_by_two(match):
    # Extract the matched text (a number)
    number = int(match.group())
    # Multiply the number by two
    return str(number * 2)

# Regular expression pattern to find numbers
pattern = r'\d+'

# The text in which we want to replace the numbers
example_text = 'The numbers are 1, 2, 3, 4, and 5.'

# Using re.sub() with the custom replacement function
result_text = re.sub(pattern, multiply_by_two, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)

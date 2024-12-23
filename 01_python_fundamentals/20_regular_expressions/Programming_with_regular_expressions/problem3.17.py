import re

# Regular expression pattern to find numbers
number_pattern = re.compile(r'\d+')

# The text in which we want to search for the numbers
example_text = 'The lucky numbers are 7, 13, 26, 39, 52, 65, and 99.'

# Using re.findall() to retrieve all matches
all_matches = number_pattern.findall(example_text)

# Function to filter matches based on additional criteria
def filter_lucky_numbers(matches):
    # Convert matched strings to integers and filter those that are multiples of 13
    lucky_numbers = [int(num) for num in matches if int(num) % 13 == 0]
    return lucky_numbers

# Applying the filter function
lucky_numbers = filter_lucky_numbers(all_matches)

# Printing the result
print("All matches:", all_matches)
print("Lucky numbers:", lucky_numbers)

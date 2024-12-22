import re

# Regular expression to find bold sections
bold_section_pattern = re.compile(r'<b>(.*?)</b>', re.IGNORECASE | re.DOTALL)

# Regular expression to find numbers
number_pattern = re.compile(r'\d+')

# The text in which we want to search for the patterns
example_text = '1 <b>2</b> 3 4 <b>5 6 7</b>'

# Using finditer to get an iterator over all bold sections
bold_sections = bold_section_pattern.finditer(example_text)

# List to store all numbers found within bold sections
numbers_in_bold = []

# Iterating over all bold sections
for section in bold_sections:
    # Extracting the content within the bold tags
    bold_content = section.group(1)
    # Finding all numbers within the bold content
    numbers = number_pattern.findall(bold_content)
    # Adding the numbers to the list
    numbers_in_bold.extend(numbers)

# Printing all numbers found within bold sections
print("Numbers found within bold sections:", numbers_in_bold)

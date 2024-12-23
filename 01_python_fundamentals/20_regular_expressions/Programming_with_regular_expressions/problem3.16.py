import re

# Regular expression pattern to match HTML tags
html_tag_pattern = re.compile(r'<[^>]+>')

# The text we want to split
example_text = 'I●like●<b>bold</b>●and●<i>italic</i>●fonts'

# Using re.split() to split the text along HTML tags
result_list = html_tag_pattern.split(example_text)

# Printing the result
print("Original text:", example_text)
print("Split list:", result_list)

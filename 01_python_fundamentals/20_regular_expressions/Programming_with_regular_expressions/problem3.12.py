import re

# Regular expression pattern to match word pairs delimited by an equals sign
pattern = r'(\w+)=\w+'

# Replacement pattern to swap the words
replacement = r'\2=\1'

# The text in which we want to swap the word pairs
example_text = 'foo=bar fizz=buzz'

# Using re.sub() to replace all matches with the swapped words
result_text = re.sub(pattern, replacement, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)

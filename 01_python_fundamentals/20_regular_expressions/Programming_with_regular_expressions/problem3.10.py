import re

# String constant representing the regular expression
regex_pattern = r'\d+'

# The text in which we want to search for the pattern
example_text = 'The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.'

# Using finditer to get an iterator over all matches
matches = re.finditer(regex_pattern, example_text)

# Iterating over all matches
for match in matches:
    # Extracting the matched text
    matched_text = match.group()
    # Getting the start and end positions of the match
    start_position = match.start()
    end_position = match.end()
    # Printing match details
    print(f"Match found: {matched_text} at position {start_position}-{end_position}")

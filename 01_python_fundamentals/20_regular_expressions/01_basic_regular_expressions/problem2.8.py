import re

# Regular expression with comments using free-spacing mode
regex_pattern = r'''
    \d{4}  # Year (four digits)
    -      # Separator (hyphen)
    \d{2}  # Month (two digits)
    -      # Separator (hyphen)
    \d{2}  # Day (two digits)
'''

# Sample text
text = "The date is 2024-08-19."

# Finding matches with re.VERBOSE to allow comments and spaces
matches = re.findall(regex_pattern, text, re.VERBOSE)
print("Matches:", matches)


import re

# Regular expression with inline comments
regex_pattern = r'(?#Year)\d{4}-(?#Separator)\d{2}-(?#Day)\d{2}'

# Sample text
text = "The date is 2024-08-19."

# Finding matches without re.VERBOSE
matches = re.findall(regex_pattern, text)
print("Matches with inline comments:", matches)
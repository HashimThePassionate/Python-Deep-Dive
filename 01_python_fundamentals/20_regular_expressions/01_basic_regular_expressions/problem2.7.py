import re

# Sample list of comma-separated words
text = "one,two,three,one,two"

# Regex pattern with conditionals to ensure each word appears at least once
regex_pattern = r'\b(?:(?:(one)|(two)|(three))(?:,|\b)){3,}(?(1)|(?!))(?(2)|(?!))(?(3)|(?!))'

# Test for matches
match = re.match(regex_pattern, text)

# Check if the pattern matched the text
if match:
    print("Valid match: All three words are present at least once.")
else:
    print("Invalid match: Not all three words are present.")
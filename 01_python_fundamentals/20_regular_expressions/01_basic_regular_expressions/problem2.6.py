import re

# Sample text with bold tags
text = "My <b>cat</b> is furry"

# Regex pattern with lookbehind and lookahead
regex_pattern = r"(?<=<b>)\w+(?=</b>)"

# Find matches
matches = re.findall(regex_pattern, text)
print("Matches:", matches)
import re

# Sample text to perform search-and-replace
text = "This is a test: 123-456."

# Regex pattern to match any three-digit number
regex_pattern = r"\d{3}"

# Replacement text: insert literal text including backreferences
replacement_text = r"$%\*$1\\1"

# Perform search-and-replace
# `re.sub` is used to substitute matches with replacement text
result = re.sub(regex_pattern, replacement_text, text)

print("Result after replacement:", result)
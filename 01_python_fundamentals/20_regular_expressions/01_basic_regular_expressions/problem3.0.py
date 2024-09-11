import re

# Sample text where we want to wrap matches in <a> tags
text = "Visit example.com for more info."

# Regex pattern to match words (simple example)
regex_pattern = r"\b\w+\b"

# Replacement text: wrap the entire match (group 0) with an <a> tag
replacement_text = r'<a href="\g<0>">\g<0></a>'

# Perform search-and-replace
result = re.sub(regex_pattern, replacement_text, text)

print("Result after replacement:", result)
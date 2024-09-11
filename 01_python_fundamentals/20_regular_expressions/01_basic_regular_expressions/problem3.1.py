import re

# Sample text containing a 10-digit number
text = "My number is 1234567890, please call me!"

# Regex pattern to match a 10-digit phone number
regex_pattern = r"\b(\d{3})(\d{3})(\d{4})\b"

# Replacement pattern to format the matched phone number
replacement_text = r"(\1) \2-\3"

# Perform search-and-replace using re.sub()
formatted_text = re.sub(regex_pattern, replacement_text, text)

print("Formatted text:", formatted_text)
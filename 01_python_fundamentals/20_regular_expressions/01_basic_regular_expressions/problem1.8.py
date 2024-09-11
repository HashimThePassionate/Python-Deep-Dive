import re

# Regex to match "Muhammad", "Hashim", or "Ali"
regex_names = r'Muhammad|Hashim|Ali'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']


# Regex to match whole words "Muhammad", "Hashim", or "Ali"
regex_names_whole = r'\bMuhammad\b|\bHashim\b|\bAli\b'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names_whole, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
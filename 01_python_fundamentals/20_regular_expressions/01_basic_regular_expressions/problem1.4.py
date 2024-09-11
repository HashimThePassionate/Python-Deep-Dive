import re
regex_any_char_except_linebreaks = r'.'
text = "Hello! How are \nyou?"
matches = re.findall(regex_any_char_except_linebreaks, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']


regex_any_char_including_linebreaks = r'[\s\S]'
text = "Hello!\nHow are you?"
matches = re.findall(regex_any_char_including_linebreaks, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', '\n', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']


# Regex with mode modifier to match any character, including line breaks
regex_with_mode_modifier = r'(?s).'
# Example usage
text = "Hello!\nHow are you?"
matches = re.findall(regex_with_mode_modifier, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', '\n', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
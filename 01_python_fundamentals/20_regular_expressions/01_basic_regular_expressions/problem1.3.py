import re
calendar_regex = r'c[ae]l[ae]nd[ae]r'
text = "calender, calandar, celendar, celandar, cielendar, cialendar cAlandAr"
matches = re.findall(calendar_regex, text)
print(matches)  # Output: ['calender', 'calandar', 'celendar', 'celandar']


# Regex to match a single hexadecimal character
hex_char_regex = r'[a-fA-F0-9]'
# Example usage
text = "1, A, g, 3F, Z"
matches = re.findall(hex_char_regex, text)
print(matches)  # Output: ['1', 'A', '3', 'F']


# Regex to match a single non-hexadecimal character
non_hex_char_regex = r'[^a-fA-F0-9]'
# Example usage
text = "1, A, g, 3F, Z, !"
matches = re.findall(non_hex_char_regex, text)
print(matches)  # Output: [',', ' ', ',', ' ', 'g', ',', ' ', ',', ' ', 'Z', ',', ' ', '!']


# Case insensitive match for hexadecimal characters
case_insensitive_hex_regex = r'(?i)[a-f0-9]'
# Example usage
text = "A, b, C, d, 3, F"
matches = re.findall(case_insensitive_hex_regex, text)
print(matches)  # Output: ['A', 'b', 'C', 'd', '3', 'F']
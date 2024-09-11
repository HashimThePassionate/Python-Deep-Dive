import re

# Regex to match "alpha" at the start of the text
regex_start_alpha = r'^\balpha\b'

# Example usage
text1 = "alpha is at the beginning. Not in between."
text2 = "Is alpha at the beginning. Not in between."
matche1 = re.findall(regex_start_alpha, text1)
matche2 = re.findall(regex_start_alpha, text2)
print(matche1)  # Output: ['alpha']
print(matche2)  # Output: No match


# Regex to match "omega" at the end of the text
regex_end_omega = r'\bomega\b$'
# Example usage
text1 = "Not in between, but omega is at the end."
text2 = "Not in between, but  is at the end omega"
matche1 = re.findall(regex_end_omega, text1)
matche2 = re.findall(regex_end_omega, text2)
print(matche1)  # Output: no  match
print(matche2)  # Output: no  ['omega']


# Regex to match "begin" at the start of a line
regex_line_start_begin = r'^begin'
# Example usage
text1 = "Not in between.\nbegin is at the start of a line."
text2 = "Not in between.\n begin is at the start of a line."
matche1 = re.findall(regex_line_start_begin, text1, re.MULTILINE)
matche2 = re.findall(regex_line_start_begin, text2, re.MULTILINE)
print(matche1)  # Output: ['begin']
print(matche2)  # Output: no match

regex_line_end_end = r'end$'

# Example usage
text1 = "Not in between.\nBut this line ends with end"
text2 = "Not in between.\nBut this line ends end with"
matche1 = re.findall(regex_line_end_end, text1, re.MULTILINE)
matche2 = re.findall(regex_line_end_end, text2, re.MULTILINE)
print(matche1)  # Output: ['end']
print(matche2)  # Output: no match
import re

# Match a googol (100-digit number)
regex_googol = r'\b\d{100}\b'

text = "Number: 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890."

matches = re.findall(regex_googol, text)
print("Googol Matches:", matches)




# Match a 32-bit hexadecimal number
regex_hex = r'\b[a-f0-9]{1,8}\b'

text = "Hex numbers: 1a2b, deadbeef, 01234567."

matches = re.findall(regex_hex, text, re.IGNORECASE)
print("Hexadecimal Matches:", matches)



# Match a 32-bit hexadecimal number with optional 'h'
regex_hex_suffix = r'\b[a-f0-9]{1,8}h?\b'

text = "Hex numbers: 1a2bh, deadbeef, 01234567h."

matches = re.findall(regex_hex_suffix, text, re.IGNORECASE)
print("Hexadecimal Matches with 'h' suffix:", matches)


# Match a floating-point number
regex_float = r'\d*\.\d+(?:e\d+)?'

text = "Floating-point numbers: 0.5, 1.23e10, .75."

matches = re.findall(regex_float, text)
print("Floating-Point Matches:", matches)
      



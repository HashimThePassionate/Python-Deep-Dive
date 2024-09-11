import re
nonprintable_string = "\a\x1B\f\n\r\t\v"
pattern = r"\a\x1B\f\n\r\t\v"
if re.fullmatch(pattern, nonprintable_string):
    print("The text matches the pattern exactly! ✅")
else:
    print("The text does not match the pattern. ❌")

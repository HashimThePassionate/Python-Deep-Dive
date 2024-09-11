import re
text_to_match = """The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~."""
pattern = r"The punctuation characters in the ASCII table are: !\"#\$%&'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`\{\|}~\."
if re.fullmatch(pattern, text_to_match):
    print("The text matches the pattern exactly! ✅")
else:
    print("The text does not match the pattern. ❌")




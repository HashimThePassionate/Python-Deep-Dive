import re as r
import regex as re
# Regex to find the trademark sign (™)
regex_trademark = r'\u2122'

text = "This is a trademark symbol ™ and here is another one: ™."
matches = r.findall(regex_trademark, text)
print(matches)  # Output: ['™', '™']

regex_currency = r'\p{Sc}'
text = "The price is $100 or €85 or ¥1000."
matches = re.findall(regex_currency, text, re.UNICODE)
print(matches)  # Output: ['$', '€', '¥']

# Regex to match any character in the "Greek Extended" block
regex_greek_extended = r'[\u1F00-\u1FFF]'

text = "Greek letters: ἀ ἁ ἂ ἃ."
matches = r.findall(regex_greek_extended, text)
print(matches)  # Output: ['ἀ', 'ἁ', 'ἂ', 'ἃ']

# Regex to match any character in the "Greek" script
regex_greek_script = r'[\u0370-\u03FF]'

text = "Greek letters: Α, Β, Γ, Δ, ε, ζ."
matches = r.findall(regex_greek_script, text)
print(matches)  # Output: ['Α', 'Β', 'Γ', 'Δ', 'ε', 'ζ']

# Regex to match a grapheme (base character + combining marks)
regex_grapheme = r'(\P{M}\p{M}*)'

text = "à is a grapheme."
matches = re.findall(regex_grapheme, text)
print(matches)  # Output: ['à', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'r', 'a', 'p', 'h', 'e', 'm', 'e', '.']


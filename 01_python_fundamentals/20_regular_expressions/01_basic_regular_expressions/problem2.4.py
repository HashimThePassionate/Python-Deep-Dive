import re

# Example text with numbers and letters
text = "123abc 456"

# Greedy quantifier example
regex_greedy = r'\b\d+\b'
matches_greedy = re.findall(regex_greedy, text)
print("Greedy Matches:", matches_greedy)

# Lazy quantifier example
regex_lazy = r'\b\d+?\b'
matches_lazy = re.findall(regex_lazy, text)
print("Lazy Matches:", matches_lazy)
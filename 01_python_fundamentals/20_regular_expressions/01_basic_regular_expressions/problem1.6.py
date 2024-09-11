import re

# Regex to match "cat" as a whole word
regex_whole_word_cat = r'\bcat\b'

# Example usage
text = "My cat is brown. A category is different from a cat."
matches = re.findall(regex_whole_word_cat, text)
print(matches)  # Output: ['cat', 'cat']



# Regex to match "cat" only if it is part of another word
regex_non_whole_word_cat = r'\Bcat\B'

# Example usage
text = "My cat is brown. staccato is a word, and so is bobcat."
matches = re.findall(regex_non_whole_word_cat, text)
print(matches)  # Output: ['cat', 'cat']
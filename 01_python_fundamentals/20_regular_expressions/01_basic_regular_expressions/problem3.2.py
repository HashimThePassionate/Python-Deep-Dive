import re

# Sample text where "Match" is the regex match
text = "BeforeMatchAfter"

# Regex pattern to capture the left context, the match, and the right context
regex_pattern = r"(.*?)(Match)(.*)"

# Replacement function to construct the desired replacement text
def replacement_function(match):
    # Group 1: Left context (text before the match)
    left_context = match.group(1)
    # Group 2: The regex match (the word "Match")
    matched_text = match.group(2)
    # Group 3: Right context (text after the match)
    right_context = match.group(3)
    
    # Construct the replacement text: Left + Whole + Right
    return f"{left_context}{left_context}{matched_text}{right_context}{right_context}"

# Perform the search-and-replace using re.sub()
result = re.sub(regex_pattern, replacement_function, text)

print("Result after replacement:", result)
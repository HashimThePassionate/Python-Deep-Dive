import re

# Regular expression pattern to match
pattern = re.compile(r'\bbold\b', re.IGNORECASE)

# Multiline string to process
multiline_text = """I like bold statements.
This is a bold move.
Do you prefer bold or italic?
No boldness here."""

# Split the multiline string into individual lines
lines = multiline_text.split('\n')

# Function to process each line and match the pattern
def grep_lines(pattern, lines, invert_match=False):
    matched_lines = []
    for line in lines:
        if pattern.search(line):
            if not invert_match:
                matched_lines.append(line)
        else:
            if invert_match:
                matched_lines.append(line)
    return matched_lines

# Using the function to get matching lines
matching_lines = grep_lines(pattern, lines)

# Printing the result
print("Original text:\n", multiline_text)
print("\nMatching lines:")
for line in matching_lines:
    print(line)

import re

# Regular expression to find bold sections
bold_section_pattern = re.compile(r'(<b>.*?</b>)', re.IGNORECASE | re.DOTALL)

# Regular expression to find the target pattern within bold sections
target_pattern = re.compile(r'before')

# Replacement text
replacement_text = 'after'

# The text in which we want to search for the patterns
example_text = 'before <b>first before</b> before <b>before before</b>'

# Function to replace the target pattern within bold sections
def replace_within_bold(match):
    # Extract the content within the bold tags
    bold_content = match.group(0)
    # Replace the target pattern within the bold content
    modified_content = target_pattern.sub(replacement_text, bold_content)
    return modified_content

# Using re.sub() to replace the target pattern within all bold sections
result_text = bold_section_pattern.sub(replace_within_bold, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)

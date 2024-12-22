import re

# Regular expression to find HTML tags
html_tag_pattern = re.compile(r'<[^>]+>')

# Regular expression to find straight double quotes
quote_pattern = re.compile(r'"')

# Replacement text for smart quotes
left_smart_quote = '“'
right_smart_quote = '”'

# The text in which we want to replace the quotes
example_text = '"text" <span class="middle">"text"</span> "text"'

# Function to replace quotes outside of HTML tags
def replace_quotes_outside_html(text):
    segments = []
    last_end = 0
    
    # Iterate over all HTML tags
    for match in html_tag_pattern.finditer(text):
        start, end = match.span()
        
        # Process the text segment before the HTML tag
        segment_before_tag = text[last_end:start]
        segment_before_tag = quote_pattern.sub(left_smart_quote, segment_before_tag, 1)
        segment_before_tag = quote_pattern.sub(right_smart_quote, segment_before_tag)
        segments.append(segment_before_tag)
        
        # Add the HTML tag itself unchanged
        segments.append(text[start:end])
        
        # Update the position for the next iteration
        last_end = end
    
    # Process the remaining text segment after the last HTML tag
    remaining_segment = text[last_end:]
    remaining_segment = quote_pattern.sub(left_smart_quote, remaining_segment, 1)
    remaining_segment = quote_pattern.sub(right_smart_quote, remaining_segment)
    segments.append(remaining_segment)
    
    # Join all segments back into a single string
    return ''.join(segments)

# Using the custom function to replace quotes
result_text = replace_quotes_outside_html(example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)

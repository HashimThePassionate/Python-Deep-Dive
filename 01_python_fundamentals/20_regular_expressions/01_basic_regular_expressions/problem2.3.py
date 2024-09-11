import re

# Correct regex to match text between <p> and </p> tags
regex_lazy = r'<p>.*?</p>'

text = """
<p>
The very <em>first</em> task is to find the beginning of a paragraph.
</p>
<p>
Then you have to find the end of the paragraph
</p>
"""

# Find all matches for text between <p> and </p> tags
matches = re.findall(regex_lazy, text, re.DOTALL)
print("Matched Paragraphs:", matches)
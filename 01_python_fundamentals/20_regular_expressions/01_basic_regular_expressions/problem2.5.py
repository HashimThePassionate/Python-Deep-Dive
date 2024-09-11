import re

# Sample HTML text where there is content after </body> but before </html>
text = """
<html>
  <body>
    Some content here.
  </body>
  <div>
    More content without closing the HTML tag.
"""

# Updated regex with atomic grouping to prevent runaway repetition
regex_atomic = r'(?>.*?</body>).*?</html>'

# Try to find matches
matches_atomic = re.findall(regex_atomic, text, re.DOTALL)
print("Matches with Atomic Grouping:", matches_atomic)

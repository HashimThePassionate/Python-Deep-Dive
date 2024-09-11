import re

# Regex to match "magical" dates in yyyy-mm-dd format
regex_magical_date = r'\b\d\d(\d\d)-\1-\1\b'

# Example text containing dates
text_dates = "Here are some dates: 2008-08-08, 1999-12-12, 2024-09-12, and 2011-11-11, 2010-10-10."

# Find all magical dates
matches_magical_dates = re.findall(regex_magical_date, text_dates)
print("Magical Dates:", matches_magical_dates)
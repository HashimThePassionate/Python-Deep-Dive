import re

# Regex to match dates and capture year, month, and day
regex_named_date = r'\b(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\b'

# Example text containing dates
text_dates = "Here are some dates: 2024-09-12, 1999-12-25, 2008-08-08."

# Find all matches and extract named groups
matches_dates = re.finditer(regex_named_date, text_dates)
for match in matches_dates:
    print(f"Year: {match.group('year')}, Month: {match.group('month')}, Day: {match.group('day')}")



# Regex to match "magical" dates and capture the magical number
regex_magical_named = r'\b\d{2}(?P<magic>\d{2})-(?P=magic)-(?P=magic)\b'

# Example text containing dates
text_magical_dates = "Some magical dates are: 2008-08-08, 2024-09-12, and 2011-11-11."

# Find all matches and extract the "magic" number
matches_magical = re.finditer(regex_magical_named, text_magical_dates)
for match in matches_magical:
    print(f"Magical Number: {match.group('magic')}")
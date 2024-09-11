import re

regex_names = r'\b(Muhammad|Hashim|Ali)\b'
text = "Muhammad, Hashim, and Ali went to Muhammad's house."
matches = re.findall(regex_names, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']

# Regex to match and capture date parts in yyyy-mm-dd format
regex_date = r'\b(\d{4})-(\d{2})-(\d{2})\b'
regex_date_without_capture = r'\b(?:\d{4})-(?:\d{2})-(?:\d{2})\b'
# Example text with today's date
text = "The event is scheduled for 2024-09-12."

# Find all matches with captured groups
matches = re.findall(regex_date, text)
print(matches)  # Output: [('2024', '09', '12')]
# Extracting year, month, and day from the first match
if matches:
    year, month, day = matches[0]
    print(f"Year: {year}, Month: {month}, Day: {day}")
    # Output: Year: 2024, Month: 09, Day: 12
    
matches = re.findall(regex_date_without_capture, text)
print(matches)  # Output: ['2024-09-12']


# File: web_scraper/main.py

from web_scraper import * 
from web_scraper.utils import clean_html, format_url

# Example usage
html = "    <html>Welcome to my site!</html>    "
cleaned_html = clean_html(html)
print(cleaned_html)  # Outputs: <html>Welcome to my site!</html>

formatted_url = format_url("HTTP://EXAMPLE.COM")
print(formatted_url)  # Outputs: http://example.com

parsed_content = parse_page(cleaned_html)
print(parsed_content)  # Outputs: Parsed content from: <html>Welcome to my site!</html>

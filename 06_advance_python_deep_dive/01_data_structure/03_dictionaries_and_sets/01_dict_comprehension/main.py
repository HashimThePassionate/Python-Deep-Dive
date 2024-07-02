# List of tuples containing country dial codes and country names
dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

# Creating a dictionary with country names as keys and dial codes as values
country_dial = {country: code for code, country in dial_codes}
print(country_dial)

# Filtering and creating a new dictionary with country names in uppercase
# for countries with dial codes less than 70
filtered_country_dial = {
    code: country.upper()
    for country, code in sorted(country_dial.items())  # Sort the dictionary items by country name
    if code < 70  # Include only entries with dial codes less than 70
}
print(filtered_country_dial)

